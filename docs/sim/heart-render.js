// Renderers for the 0D heart simulator.
//
// Three building blocks, each independent and reusable:
//   AnatomyView    — updates a static SVG of the heart based on a snapshot
//   TimeSeriesPlot — rolling-buffer line plot of one or more signals on canvas
//   PvLoop         — pressure-volume loop on canvas, with cycle-aware buffering

import { syntheticEcg } from "./heart-0d.js";

/**
 * @typedef {import("./heart-0d.js").Snapshot} Snapshot
 */

// ─────────────────────────────────────────────────────────────────────────
// AnatomyView
// ─────────────────────────────────────────────────────────────────────────

const CHAMBER_BASE_FILL = {
  lv: "#7a1a26",
  rv: "#1a3a7a",
  la: "#a64054",
  ra: "#3a5fa8",
};

/** Updates the schematic heart SVG to reflect the current sim state. */
export class AnatomyView {
  /** @param {SVGSVGElement} svgEl */
  constructor(svgEl) {
    this.svg = svgEl;
    this.elems = {
      lv: svgEl.querySelector("#chamber-lv"),
      rv: svgEl.querySelector("#chamber-rv"),
      la: svgEl.querySelector("#chamber-la"),
      ra: svgEl.querySelector("#chamber-ra"),
      valveMv: svgEl.querySelector("#valve-mv"),
      valveAv: svgEl.querySelector("#valve-av"),
      valveTv: svgEl.querySelector("#valve-tv"),
      valvePv: svgEl.querySelector("#valve-pv"),
      flowMv: svgEl.querySelector("#flow-mv"),
      flowAv: svgEl.querySelector("#flow-av"),
      flowTv: svgEl.querySelector("#flow-tv"),
      flowPv: svgEl.querySelector("#flow-pv"),
      saNode: svgEl.querySelector("#sa-node"),
      readouts: {
        hr:  svgEl.querySelector("#readout-hr"),
        sv:  svgEl.querySelector("#readout-sv"),
        co:  svgEl.querySelector("#readout-co"),
        ef:  svgEl.querySelector("#readout-ef"),
        map: svgEl.querySelector("#readout-map"),
      },
    };

    this._lastBeatVlvMin = Infinity;
    this._lastBeatVlvMax = -Infinity;
    this._lastSV = 70;
    this._lastEF = 0.55;
    this._mapEMA = 93;
    this._lastPhase = 0;
    this._lastPaoSum = 0;
    this._lastPaoCount = 0;
  }

  /** @param {Snapshot} s */
  update(s) {
    // Chamber activation tint — interpolate brightness with elastance pulse.
    this._tintChamber("lv", s.activation);
    this._tintChamber("rv", s.activation);
    this._tintChamber("la", 0); // atrial activation not modeled in this version
    this._tintChamber("ra", 0);

    // Valve open/closed glyphs.
    this._setValveOpen("valveMv", s.valves.mitral);
    this._setValveOpen("valveAv", s.valves.aortic);
    this._setValveOpen("valveTv", s.valves.tricuspid);
    this._setValveOpen("valvePv", s.valves.pulmonary);

    // Flow indicators — opacity scales with flow magnitude.
    this._setFlowOpacity("flowMv", s.Q_mv, 600);
    this._setFlowOpacity("flowAv", s.Q_av, 800);
    this._setFlowOpacity("flowTv", s.Q_tv, 600);
    this._setFlowOpacity("flowPv", s.Q_pv, 600);

    // SA-node pulse — bright at the start of each cycle.
    if (this.elems.saNode) {
      const intensity = Math.exp(-((s.cyclePhase * 12) ** 2));
      this.elems.saNode.setAttribute("opacity", String(0.3 + 0.7 * intensity));
    }

    // Track per-cycle SV, EF, and rolling MAP.
    this._lastBeatVlvMin = Math.min(this._lastBeatVlvMin, s.V_lv);
    this._lastBeatVlvMax = Math.max(this._lastBeatVlvMax, s.V_lv);
    this._lastPaoSum += s.P_ao;
    this._lastPaoCount += 1;

    if (s.cyclePhase < this._lastPhase) {
      // wrapped — start of a new cycle, latch beat-level metrics.
      const sv = this._lastBeatVlvMax - this._lastBeatVlvMin;
      const ef = this._lastBeatVlvMax > 0 ? sv / this._lastBeatVlvMax : 0;
      this._lastSV = sv;
      this._lastEF = ef;
      const meanPao = this._lastPaoCount ? this._lastPaoSum / this._lastPaoCount : 0;
      // Exponential moving average to smooth across multiple beats.
      this._mapEMA = 0.6 * this._mapEMA + 0.4 * meanPao;
      this._lastBeatVlvMin = s.V_lv;
      this._lastBeatVlvMax = s.V_lv;
      this._lastPaoSum = 0;
      this._lastPaoCount = 0;
    }
    this._lastPhase = s.cyclePhase;

    // Readouts.
    const hr = 60 / s.cyclePeriod;
    const co = (this._lastSV * hr) / 1000; // L/min
    if (this.elems.readouts.hr)  this.elems.readouts.hr.textContent  = hr.toFixed(0);
    if (this.elems.readouts.sv)  this.elems.readouts.sv.textContent  = this._lastSV.toFixed(0);
    if (this.elems.readouts.co)  this.elems.readouts.co.textContent  = co.toFixed(2);
    if (this.elems.readouts.ef)  this.elems.readouts.ef.textContent  = (this._lastEF * 100).toFixed(0);
    if (this.elems.readouts.map) this.elems.readouts.map.textContent = this._mapEMA.toFixed(0);
  }

  _tintChamber(name, activation) {
    const el = this.elems[name];
    if (!el) return;
    // Brightness from base color toward white as activation approaches 1.
    const lightness = 0.30 + 0.40 * activation;
    el.setAttribute("fill", lerpColor(CHAMBER_BASE_FILL[name], "#ffffff", activation * 0.55));
    el.setAttribute("opacity", String(0.55 + 0.45 * lightness));
  }

  _setValveOpen(name, isOpen) {
    const el = this.elems[name];
    if (!el) return;
    el.setAttribute("data-open", isOpen ? "true" : "false");
    el.setAttribute("opacity", isOpen ? "0.95" : "0.30");
  }

  _setFlowOpacity(name, q, qMax) {
    const el = this.elems[name];
    if (!el) return;
    const a = Math.max(0, Math.min(1, q / qMax));
    el.setAttribute("opacity", String(a));
  }
}

// ─────────────────────────────────────────────────────────────────────────
// TimeSeriesPlot — canvas, rolling buffer
// ─────────────────────────────────────────────────────────────────────────

/**
 * @typedef {Object} TraceConfig
 * @property {string} key       sample property name on objects pushed via push()
 * @property {string} color     stroke color
 * @property {number} [yMin]    fixed y-axis min (auto-scaled if absent)
 * @property {number} [yMax]    fixed y-axis max
 * @property {string} [label]
 * @property {number} [width]   stroke width, default 1.5
 */

export class TimeSeriesPlot {
  /**
   * @param {HTMLCanvasElement} canvas
   * @param {{traces: TraceConfig[], windowSeconds?: number, gridColor?: string, bg?: string}} opts
   */
  constructor(canvas, opts) {
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.traces = opts.traces;
    this.window = opts.windowSeconds ?? 6;
    this.gridColor = opts.gridColor ?? "#1c2230";
    this.bg = opts.bg ?? "#0a0d14";
    this.buffer = []; // {t, ...samples}
    this._resize();
    new ResizeObserver(() => this._resize()).observe(canvas);
  }

  _resize() {
    const dpr = window.devicePixelRatio || 1;
    const w = this.canvas.clientWidth;
    const h = this.canvas.clientHeight;
    this.canvas.width = Math.max(1, Math.floor(w * dpr));
    this.canvas.height = Math.max(1, Math.floor(h * dpr));
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    this.w = w;
    this.h = h;
  }

  /** @param {number} t @param {Record<string, number>} sample */
  push(t, sample) {
    this.buffer.push({ t, ...sample });
    const cutoff = t - this.window;
    while (this.buffer.length && this.buffer[0].t < cutoff) this.buffer.shift();
  }

  draw() {
    const { ctx, w, h, traces, buffer } = this;
    if (!buffer.length) return;
    ctx.fillStyle = this.bg;
    ctx.fillRect(0, 0, w, h);

    const tNow = buffer[buffer.length - 1].t;
    const t0 = tNow - this.window;

    // Horizontal grid lines.
    ctx.strokeStyle = this.gridColor;
    ctx.lineWidth = 1;
    ctx.beginPath();
    for (let i = 1; i < 4; i++) {
      const y = (i * h) / 4;
      ctx.moveTo(0, y);
      ctx.lineTo(w, y);
    }
    ctx.stroke();

    // Trace per series.
    const padTop = 10, padBot = 10;
    const drawHeight = h - padTop - padBot;

    for (const tr of traces) {
      let yMin = tr.yMin, yMax = tr.yMax;
      if (yMin == null || yMax == null) {
        let lo = Infinity, hi = -Infinity;
        for (const s of buffer) {
          const v = s[tr.key];
          if (v == null || !Number.isFinite(v)) continue;
          if (v < lo) lo = v;
          if (v > hi) hi = v;
        }
        if (lo === hi) { lo -= 1; hi += 1; }
        if (yMin == null) yMin = lo - (hi - lo) * 0.1;
        if (yMax == null) yMax = hi + (hi - lo) * 0.1;
      }

      ctx.strokeStyle = tr.color;
      ctx.lineWidth = tr.width ?? 1.5;
      ctx.beginPath();
      let drawn = false;
      for (const s of buffer) {
        const v = s[tr.key];
        if (v == null || !Number.isFinite(v)) continue;
        const x = ((s.t - t0) / this.window) * w;
        const y = padTop + drawHeight * (1 - (v - yMin) / (yMax - yMin));
        if (!drawn) { ctx.moveTo(x, y); drawn = true; }
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      if (tr.label) {
        ctx.fillStyle = tr.color;
        ctx.font = "11px ui-monospace, SFMono-Regular, Menlo, monospace";
        ctx.textBaseline = "top";
        ctx.fillText(tr.label, 8, 6);
      }
    }
  }
}

// ─────────────────────────────────────────────────────────────────────────
// PV loop — canvas, retained latest cycle
// ─────────────────────────────────────────────────────────────────────────

export class PvLoop {
  /**
   * @param {HTMLCanvasElement} canvas
   * @param {{vMin?:number, vMax?:number, pMin?:number, pMax?:number, color?:string, bg?:string, gridColor?:string}} [opts]
   */
  constructor(canvas, opts = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.vMin = opts.vMin ?? 0;
    this.vMax = opts.vMax ?? 200;
    this.pMin = opts.pMin ?? 0;
    this.pMax = opts.pMax ?? 160;
    this.color = opts.color ?? "#ff8a4c";
    this.bg = opts.bg ?? "#0a0d14";
    this.gridColor = opts.gridColor ?? "#1c2230";
    this.current = []; // [{V, P}] for the in-progress cycle
    this.last = []; // for the most recently completed cycle
    this._lastPhase = 0;
    this._resize();
    new ResizeObserver(() => this._resize()).observe(canvas);
  }

  _resize() {
    const dpr = window.devicePixelRatio || 1;
    const w = this.canvas.clientWidth;
    const h = this.canvas.clientHeight;
    this.canvas.width = Math.max(1, Math.floor(w * dpr));
    this.canvas.height = Math.max(1, Math.floor(h * dpr));
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    this.w = w;
    this.h = h;
  }

  /** @param {Snapshot} s */
  push(s) {
    this.current.push({ V: s.V_lv, P: s.P_lv });
    if (s.cyclePhase < this._lastPhase) {
      this.last = this.current;
      this.current = [];
    }
    this._lastPhase = s.cyclePhase;
  }

  draw() {
    const { ctx, w, h } = this;
    ctx.fillStyle = this.bg;
    ctx.fillRect(0, 0, w, h);

    const padL = 32, padR = 12, padT = 12, padB = 28;
    const plotW = w - padL - padR;
    const plotH = h - padT - padB;

    const xOf = (V) => padL + plotW * (V - this.vMin) / (this.vMax - this.vMin);
    const yOf = (P) => padT + plotH * (1 - (P - this.pMin) / (this.pMax - this.pMin));

    ctx.strokeStyle = this.gridColor;
    ctx.lineWidth = 1;
    ctx.beginPath();
    for (let v = this.vMin; v <= this.vMax; v += 50) {
      const x = xOf(v);
      ctx.moveTo(x, padT); ctx.lineTo(x, padT + plotH);
    }
    for (let p = this.pMin; p <= this.pMax; p += 40) {
      const y = yOf(p);
      ctx.moveTo(padL, y); ctx.lineTo(padL + plotW, y);
    }
    ctx.stroke();

    ctx.fillStyle = "#6a7282";
    ctx.font = "10px ui-monospace, SFMono-Regular, Menlo, monospace";
    ctx.textAlign = "center";
    ctx.fillText("LV volume (mL)", padL + plotW / 2, h - 8);
    ctx.save();
    ctx.translate(10, padT + plotH / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText("LV pressure (mmHg)", 0, 0);
    ctx.restore();

    // Last full cycle (dim).
    if (this.last.length > 1) {
      ctx.strokeStyle = this.color + "55";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(xOf(this.last[0].V), yOf(this.last[0].P));
      for (let i = 1; i < this.last.length; i++) {
        ctx.lineTo(xOf(this.last[i].V), yOf(this.last[i].P));
      }
      ctx.closePath();
      ctx.stroke();
    }

    // Current cycle (bright).
    if (this.current.length > 1) {
      ctx.strokeStyle = this.color;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(xOf(this.current[0].V), yOf(this.current[0].P));
      for (let i = 1; i < this.current.length; i++) {
        ctx.lineTo(xOf(this.current[i].V), yOf(this.current[i].P));
      }
      ctx.stroke();

      // Current point.
      const cur = this.current[this.current.length - 1];
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(xOf(cur.V), yOf(cur.P), 3, 0, 2 * Math.PI);
      ctx.fill();
    }
  }
}

// ─────────────────────────────────────────────────────────────────────────
// helpers
// ─────────────────────────────────────────────────────────────────────────

function lerpColor(a, b, t) {
  const ar = parseInt(a.slice(1, 3), 16), ag = parseInt(a.slice(3, 5), 16), ab = parseInt(a.slice(5, 7), 16);
  const br = parseInt(b.slice(1, 3), 16), bg = parseInt(b.slice(3, 5), 16), bb = parseInt(b.slice(5, 7), 16);
  const r = Math.round(ar + (br - ar) * t);
  const g = Math.round(ag + (bg - ag) * t);
  const bl = Math.round(ab + (bb - ab) * t);
  return `#${r.toString(16).padStart(2, "0")}${g.toString(16).padStart(2, "0")}${bl.toString(16).padStart(2, "0")}`;
}

/** Re-export the synthetic ECG so the page can sample it without importing the model. */
export { syntheticEcg };
