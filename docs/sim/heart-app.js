// Glue layer: instantiate the model, wire UI controls, run the animation loop.
//
// Imported by docs/heart.html via <script type="module">. Targets a specific
// set of element IDs in the page. If you fork this for another organ, the
// wiring pattern is the same: one model module, one render module, one app
// module that ties them together.

import { HeartSim, HEALTHY, SCENARIOS, syntheticEcg } from "./heart-0d.js";
import { AnatomyView, TimeSeriesPlot, PvLoop } from "./heart-render.js";

const SLIDER_DEFS = [
  { id: "slider-hr",     label: "Heart rate (bpm)",         min: 30,  max: 180, step: 1,    value: HEALTHY.HR,           apply: (v, p) => { p.HR = v; } },
  { id: "slider-emax",   label: "LV contractility (Emax)",  min: 0.4, max: 4.0, step: 0.05, value: HEALTHY.LV.Emax,      apply: (v, p) => { p.LV = { ...p.LV, Emax: v }; } },
  { id: "slider-rsys",   label: "Systemic resistance",      min: 0.4, max: 2.5, step: 0.02, value: HEALTHY.R_sys,        apply: (v, p) => { p.R_sys = v; } },
  { id: "slider-rav",    label: "Aortic-valve resistance",  min: 0.003, max: 0.05, step: 0.001, value: HEALTHY.AV.R,    apply: (v, p) => { p.AV = { ...p.AV, R: v }; } },
];

let sim;
let anatomy;
let plotEcg;
let plotPressure;
let plotVolumes;
let pvLoop;
let lastFrameMs = 0;
let speedMultiplier = 1.0;
let isPaused = false;

const SIM_DT = 0.001;            // 1 ms integrator step
const MAX_SIM_SECONDS_PER_FRAME = 0.05;  // safety: cap catch-up to 50 ms of sim per frame

export function init() {
  sim = new HeartSim();
  anatomy = new AnatomyView(document.getElementById("anatomy-svg"));

  plotEcg = new TimeSeriesPlot(document.getElementById("plot-ecg"), {
    windowSeconds: 4,
    traces: [{ key: "ecg", color: "#34d399", label: "ECG (synthetic)", yMin: -0.4, yMax: 1.2 }],
  });

  plotPressure = new TimeSeriesPlot(document.getElementById("plot-pressure"), {
    windowSeconds: 4,
    traces: [
      { key: "P_ao", color: "#f87171", label: "Aortic", yMin: 0, yMax: 160 },
      { key: "P_lv", color: "#60a5fa", label: "LV",     yMin: 0, yMax: 160 },
      { key: "P_pv", color: "#a78bfa", label: "LA (≈ pulm. vein)", yMin: 0, yMax: 160 },
    ],
  });

  plotVolumes = new TimeSeriesPlot(document.getElementById("plot-volumes"), {
    windowSeconds: 4,
    traces: [
      { key: "V_lv", color: "#fb923c", label: "LV volume", yMin: 0, yMax: 220 },
      { key: "V_rv", color: "#22d3ee", label: "RV volume", yMin: 0, yMax: 220 },
    ],
  });

  pvLoop = new PvLoop(document.getElementById("plot-pv"), { color: "#fb923c" });

  buildSliders();
  buildScenarioButtons();
  buildPlaybackControls();

  // Burn-in: simulate 5 seconds so we start at steady state.
  sim.advance(5.0, SIM_DT);

  requestAnimationFrame(loop);
}

function buildSliders() {
  const container = document.getElementById("sliders");
  if (!container) return;
  for (const def of SLIDER_DEFS) {
    const wrap = document.createElement("div");
    wrap.className = "slider";
    const labelRow = document.createElement("div");
    labelRow.className = "slider-row";
    const label = document.createElement("label");
    label.htmlFor = def.id;
    label.textContent = def.label;
    const value = document.createElement("span");
    value.id = `${def.id}-value`;
    value.textContent = formatSliderValue(def, def.value);
    labelRow.append(label, value);

    const input = document.createElement("input");
    input.type = "range";
    input.id = def.id;
    input.min = String(def.min);
    input.max = String(def.max);
    input.step = String(def.step);
    input.value = String(def.value);

    input.addEventListener("input", () => {
      const v = parseFloat(input.value);
      value.textContent = formatSliderValue(def, v);
      def.apply(v, sim.params);
    });

    wrap.append(labelRow, input);
    container.append(wrap);
  }
}

function formatSliderValue(def, v) {
  if (def.step >= 1) return v.toFixed(0);
  if (def.step >= 0.1) return v.toFixed(1);
  if (def.step >= 0.01) return v.toFixed(2);
  return v.toFixed(3);
}

function buildScenarioButtons() {
  const container = document.getElementById("scenarios");
  if (!container) return;
  for (const [key, scenario] of Object.entries(SCENARIOS)) {
    const btn = document.createElement("button");
    btn.className = "scenario";
    btn.dataset.scenario = key;
    btn.innerHTML = `<strong>${scenario.label}</strong><br><small>${scenario.description}</small>`;
    btn.addEventListener("click", () => applyScenario(key));
    container.append(btn);
  }
}

function applyScenario(key) {
  const scenario = SCENARIOS[key];
  if (!scenario) return;
  // Reset to healthy baseline, apply patch, refresh sliders to match.
  const p = structuredClone(HEALTHY);
  applyPatch(p, scenario.patch);
  sim.params = p;
  syncSlidersFromParams();
  // Highlight the active scenario button.
  for (const btn of document.querySelectorAll(".scenario")) {
    btn.classList.toggle("active", btn.dataset.scenario === key);
  }
}

function applyPatch(target, patch) {
  for (const [k, v] of Object.entries(patch)) {
    if (v && typeof v === "object" && !Array.isArray(v)) {
      target[k] = { ...target[k], ...v };
    } else {
      target[k] = v;
    }
  }
}

function syncSlidersFromParams() {
  for (const def of SLIDER_DEFS) {
    const input = /** @type {HTMLInputElement|null} */ (document.getElementById(def.id));
    const value = document.getElementById(`${def.id}-value`);
    if (!input || !value) continue;
    let current;
    if (def.id === "slider-hr") current = sim.params.HR;
    else if (def.id === "slider-emax") current = sim.params.LV.Emax;
    else if (def.id === "slider-rsys") current = sim.params.R_sys;
    else if (def.id === "slider-rav") current = sim.params.AV.R;
    if (current != null) {
      input.value = String(current);
      value.textContent = formatSliderValue(def, current);
    }
  }
}

function buildPlaybackControls() {
  const playBtn = document.getElementById("btn-pause");
  if (playBtn) {
    playBtn.addEventListener("click", () => {
      isPaused = !isPaused;
      playBtn.textContent = isPaused ? "▶ Play" : "⏸ Pause";
    });
  }
  const speedSelect = document.getElementById("speed");
  if (speedSelect) {
    speedSelect.addEventListener("change", () => {
      speedMultiplier = parseFloat(speedSelect.value);
    });
  }
  const resetBtn = document.getElementById("btn-reset");
  if (resetBtn) {
    resetBtn.addEventListener("click", () => {
      sim.reset();
      sim.advance(5.0, SIM_DT);
    });
  }
}

function loop(nowMs) {
  const dtSec = lastFrameMs ? Math.min((nowMs - lastFrameMs) / 1000, 0.1) : 0;
  lastFrameMs = nowMs;

  if (!isPaused && dtSec > 0) {
    const wallToSim = Math.min(dtSec * speedMultiplier, MAX_SIM_SECONDS_PER_FRAME);
    sim.advance(wallToSim, SIM_DT);
  }

  const snap = sim.snapshot();
  anatomy.update(snap);
  plotEcg.push(snap.t, { ecg: syntheticEcg(snap.cyclePhase) });
  plotPressure.push(snap.t, { P_ao: snap.P_ao, P_lv: snap.P_lv, P_pv: snap.P_pv });
  plotVolumes.push(snap.t, { V_lv: snap.V_lv, V_rv: snap.V_rv });
  pvLoop.push(snap);

  plotEcg.draw();
  plotPressure.draw();
  plotVolumes.draw();
  pvLoop.draw();

  requestAnimationFrame(loop);
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
