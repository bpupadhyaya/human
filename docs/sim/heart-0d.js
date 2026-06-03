// 0D coupled cardiovascular model.
//
// Time-varying-elastance ventricles drive a closed-loop circulation via four
// diode-like valves and two Windkessel arterial compartments. State is a
// 6-element volume vector; all pressures are computed from state at every
// derivative evaluation; integration is fixed-step RK4.
//
// Reference: Smith BW et al. "Minimal haemodynamic system model including
// ventricular interaction and valve dynamics." Med Eng Phys. 2004;26(2):131-9.
// (and the long lineage of teaching-grade lumped cardiovascular models that
// trace back to Suga-Sagawa elastance and Otto Frank's Windkessel.)

/**
 * @typedef {Object} ChamberParams
 * @property {number} Emax  maximum elastance, mmHg/mL (peak systole)
 * @property {number} Emin  minimum elastance, mmHg/mL (diastole)
 * @property {number} V0    unstressed volume, mL
 */

/**
 * @typedef {Object} VesselParams
 * @property {number} C   compliance, mL/mmHg
 * @property {number} V0  unstressed volume, mL
 */

/**
 * @typedef {Object} ValveParams
 * @property {number} R   resistance when forward-flowing, mmHg·s/mL
 */

/**
 * @typedef {Object} HeartParams
 * @property {number} HR             heart rate, bpm
 * @property {number} Tsystole       systolic duration, s (typical ~0.3)
 * @property {ChamberParams} LV
 * @property {ChamberParams} RV
 * @property {VesselParams}  Ao      systemic arteries
 * @property {VesselParams}  Pa      pulmonary arteries
 * @property {VesselParams}  Pv      pulmonary veins
 * @property {VesselParams}  Vc      systemic veins (vena cava + venules)
 * @property {ValveParams}   MV      mitral
 * @property {ValveParams}   AV      aortic
 * @property {ValveParams}   TV      tricuspid
 * @property {ValveParams}   PuV     pulmonary
 * @property {number} R_sys          systemic resistance, mmHg·s/mL
 * @property {number} R_pulm         pulmonary resistance, mmHg·s/mL
 */

/**
 * Healthy-adult parameter set. Tuned so that at steady state:
 *   MAP ~93 mmHg (LV peak ~120, trough ~80)
 *   Pulmonary artery mean ~14 mmHg
 *   LV EDV ~125 mL, ESV ~55 mL → SV ~70 mL → EF ~56 % at HR 75
 *   Cardiac output ~5.2 L/min
 *
 * @type {HeartParams}
 */
export const HEALTHY = {
  HR: 75,
  Tsystole: 0.30,

  LV:  { Emax: 2.5,  Emin: 0.06, V0: 15 },
  RV:  { Emax: 0.55, Emin: 0.04, V0: 10 },

  Ao:  { C: 1.0,  V0: 30 },
  Pa:  { C: 4.0,  V0: 20 },
  Pv:  { C: 25.0, V0: 50 },
  Vc:  { C: 50.0, V0: 100 },

  MV:  { R: 0.006 },
  AV:  { R: 0.005 },
  TV:  { R: 0.006 },
  PuV: { R: 0.004 },

  R_sys:  1.00,
  R_pulm: 0.10,
};

// State vector indices.
const IDX_VLV = 0;
const IDX_VRV = 1;
const IDX_VAO = 2;
const IDX_VPA = 3;
const IDX_VPV = 4;
const IDX_VVC = 5;
const N_STATE = 6;

/** Initial state, mL. Sums to ~720 mL of *stressed* volume. */
const INITIAL_STATE = new Float64Array([
  /* V_lv */ 125,
  /* V_rv */ 100,
  /* V_ao */ 80,
  /* V_pa */ 35,
  /* V_pv */ 175,
  /* V_vc */ 205,
]);

/**
 * Cardiac activation function — normalized 0..1 across the cycle.
 * Squared-sine pulse during systole (peak at mid-systole), zero in diastole.
 *
 * @param {number} cyclePhase  fraction of cycle, 0..1
 * @param {number} systoleFrac fraction of cycle that is systole
 * @returns {number} en(t) ∈ [0, 1]
 */
function activation(cyclePhase, systoleFrac) {
  if (cyclePhase >= systoleFrac) return 0;
  const x = Math.PI * cyclePhase / systoleFrac;
  const s = Math.sin(x);
  return s * s;
}

/**
 * Forward-only valve flow.  Q = max(0, ΔP / R) — diode model.
 * @param {number} pUp upstream pressure, mmHg
 * @param {number} pDn downstream pressure, mmHg
 * @param {number} R   resistance when open, mmHg·s/mL
 * @returns {number} flow, mL/s
 */
function valveFlow(pUp, pDn, R) {
  const dp = pUp - pDn;
  return dp > 0 ? dp / R : 0;
}

/**
 * 0D coupled cardiovascular simulator.  Owns its own state, advances time
 * via fixed-step RK4, exposes a snapshot for rendering.
 */
export class HeartSim {
  /** @param {HeartParams} [params] */
  constructor(params = HEALTHY) {
    /** @type {HeartParams} */
    this.params = structuredClone(params);
    this.t = 0;
    /** @type {Float64Array} */
    this.state = new Float64Array(INITIAL_STATE);
    this._scratch = new Float64Array(N_STATE);
    this._k1 = new Float64Array(N_STATE);
    this._k2 = new Float64Array(N_STATE);
    this._k3 = new Float64Array(N_STATE);
    this._k4 = new Float64Array(N_STATE);
  }

  /** Reset to a fresh simulation at t = 0. */
  reset() {
    this.t = 0;
    this.state.set(INITIAL_STATE);
  }

  /**
   * Replace parameters in place. Caller may pass a partial object; only the
   * provided fields override defaults from {@link HEALTHY}.
   * @param {Partial<HeartParams>} patch
   */
  setParams(patch) {
    Object.assign(this.params, patch);
  }

  /**
   * Compute pressures from a state vector at time t.
   * @param {Float64Array} y
   * @param {number} t
   * @returns {{P_lv:number, P_rv:number, P_ao:number, P_pa:number, P_pv:number, P_vc:number, e:number}}
   */
  pressures(y, t) {
    const p = this.params;
    const T = 60 / p.HR;
    const phase = (t % T) / T;
    const e = activation(phase, p.Tsystole / T);

    const E_lv = p.LV.Emin + (p.LV.Emax - p.LV.Emin) * e;
    const E_rv = p.RV.Emin + (p.RV.Emax - p.RV.Emin) * e;

    return {
      P_lv: E_lv * (y[IDX_VLV] - p.LV.V0),
      P_rv: E_rv * (y[IDX_VRV] - p.RV.V0),
      P_ao: (y[IDX_VAO] - p.Ao.V0) / p.Ao.C,
      P_pa: (y[IDX_VPA] - p.Pa.V0) / p.Pa.C,
      P_pv: (y[IDX_VPV] - p.Pv.V0) / p.Pv.C,
      P_vc: (y[IDX_VVC] - p.Vc.V0) / p.Vc.C,
      e,
    };
  }

  /**
   * Compute volume derivatives.
   * @param {Float64Array} y
   * @param {number} t
   * @param {Float64Array} out  destination for derivative (length 6)
   */
  derivs(y, t, out) {
    const p = this.params;
    const P = this.pressures(y, t);

    const Q_mv = valveFlow(P.P_pv, P.P_lv, p.MV.R);
    const Q_av = valveFlow(P.P_lv, P.P_ao, p.AV.R);
    const Q_tv = valveFlow(P.P_vc, P.P_rv, p.TV.R);
    const Q_pv = valveFlow(P.P_rv, P.P_pa, p.PuV.R);
    const Q_sys  = (P.P_ao - P.P_vc) / p.R_sys;
    const Q_pulm = (P.P_pa - P.P_pv) / p.R_pulm;

    out[IDX_VLV] = Q_mv  - Q_av;
    out[IDX_VRV] = Q_tv  - Q_pv;
    out[IDX_VAO] = Q_av  - Q_sys;
    out[IDX_VPA] = Q_pv  - Q_pulm;
    out[IDX_VPV] = Q_pulm - Q_mv;
    out[IDX_VVC] = Q_sys  - Q_tv;
  }

  /**
   * Advance the simulation by dt seconds using a single RK4 step.
   * For numerical stability with stiff valve dynamics, callers should chunk
   * larger advances into many small RK4 steps (~1 ms each).
   * @param {number} dt seconds
   */
  rk4(dt) {
    const y = this.state;
    const t = this.t;
    const k1 = this._k1, k2 = this._k2, k3 = this._k3, k4 = this._k4;
    const tmp = this._scratch;

    this.derivs(y, t, k1);

    for (let i = 0; i < N_STATE; i++) tmp[i] = y[i] + 0.5 * dt * k1[i];
    this.derivs(tmp, t + 0.5 * dt, k2);

    for (let i = 0; i < N_STATE; i++) tmp[i] = y[i] + 0.5 * dt * k2[i];
    this.derivs(tmp, t + 0.5 * dt, k3);

    for (let i = 0; i < N_STATE; i++) tmp[i] = y[i] + dt * k3[i];
    this.derivs(tmp, t + dt, k4);

    for (let i = 0; i < N_STATE; i++) {
      y[i] += dt * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6;
    }
    this.t += dt;
  }

  /**
   * Advance simulation by `wallSeconds` of real time, sub-stepped at `dt`.
   * Default sub-step is 1 ms — enough for valve transitions to remain stable.
   * @param {number} wallSeconds  total seconds of simulated time to advance
   * @param {number} [dt=0.001]   integrator step size, s
   */
  advance(wallSeconds, dt = 0.001) {
    let remaining = wallSeconds;
    while (remaining > 0) {
      const step = Math.min(dt, remaining);
      this.rk4(step);
      remaining -= step;
    }
  }

  /**
   * Snapshot of derived quantities for rendering. Recomputes pressures and
   * flows from current state — read-only, safe to call every frame.
   * @returns {Snapshot}
   */
  snapshot() {
    const p = this.params;
    const y = this.state;
    const P = this.pressures(y, this.t);
    const T = 60 / p.HR;
    const phase = (this.t % T) / T;

    const Q_mv = valveFlow(P.P_pv, P.P_lv, p.MV.R);
    const Q_av = valveFlow(P.P_lv, P.P_ao, p.AV.R);
    const Q_tv = valveFlow(P.P_vc, P.P_rv, p.TV.R);
    const Q_pv = valveFlow(P.P_rv, P.P_pa, p.PuV.R);

    return {
      t: this.t,
      cyclePeriod: T,
      cyclePhase: phase,
      activation: P.e,
      V_lv: y[IDX_VLV], V_rv: y[IDX_VRV],
      V_ao: y[IDX_VAO], V_pa: y[IDX_VPA],
      V_pv: y[IDX_VPV], V_vc: y[IDX_VVC],
      P_lv: P.P_lv, P_rv: P.P_rv,
      P_ao: P.P_ao, P_pa: P.P_pa,
      P_pv: P.P_pv, P_vc: P.P_vc,
      Q_mv, Q_av, Q_tv, Q_pv,
      valves: {
        mitral:    Q_mv > 0,
        aortic:    Q_av > 0,
        tricuspid: Q_tv > 0,
        pulmonary: Q_pv > 0,
      },
    };
  }
}

/**
 * @typedef {Object} Snapshot
 * @property {number} t
 * @property {number} cyclePeriod
 * @property {number} cyclePhase
 * @property {number} activation
 * @property {number} V_lv  @property {number} V_rv
 * @property {number} V_ao  @property {number} V_pa
 * @property {number} V_pv  @property {number} V_vc
 * @property {number} P_lv  @property {number} P_rv
 * @property {number} P_ao  @property {number} P_pa
 * @property {number} P_pv  @property {number} P_vc
 * @property {number} Q_mv  @property {number} Q_av
 * @property {number} Q_tv  @property {number} Q_pv
 * @property {{mitral:boolean,aortic:boolean,tricuspid:boolean,pulmonary:boolean}} valves
 */

/**
 * Synthesize a phenomenological 12-lead-style ECG signal from the cycle phase.
 * Not a true bidomain projection — just the canonical P-Q-R-S-T waveform shape
 * scaled and timed so the ECG aligns with the cardiac cycle visible elsewhere.
 * Returns a normalized millivolt-like value; callers can scale to taste.
 *
 * @param {number} cyclePhase  0..1
 * @returns {number}
 */
export function syntheticEcg(cyclePhase) {
  // Wave parameters (timing as fraction of cycle, amplitude, half-width).
  const waves = [
    { center: 0.05, amp:  0.15, sigma: 0.022 },  // P wave
    { center: 0.16, amp: -0.10, sigma: 0.005 },  // Q
    { center: 0.18, amp:  1.00, sigma: 0.006 },  // R
    { center: 0.20, amp: -0.20, sigma: 0.008 },  // S
    { center: 0.40, amp:  0.30, sigma: 0.040 },  // T
  ];
  let v = 0;
  for (const w of waves) {
    const z = (cyclePhase - w.center) / w.sigma;
    v += w.amp * Math.exp(-0.5 * z * z);
  }
  return v;
}

/** Built-in scenario presets — parameter overlays applied on top of HEALTHY. */
export const SCENARIOS = {
  healthy: {
    label: "Healthy adult",
    description: "Resting hemodynamics in a 30-year-old, HR 75, MAP ~93 mmHg.",
    patch: {},
  },
  heartFailure: {
    label: "Heart failure (HFrEF)",
    description: "Reduced LV contractility; chamber dilates; EF falls.",
    patch: {
      LV: { Emax: 1.0, Emin: 0.10, V0: 25 },
      R_sys: 1.40,
    },
  },
  aorticStenosis: {
    label: "Aortic stenosis",
    description: "Stenotic aortic valve raises ejection resistance fivefold; LV pressure rises sharply during systole.",
    patch: {
      AV: { R: 0.025 },
    },
  },
  hypertension: {
    label: "Hypertension",
    description: "Elevated systemic vascular resistance; chronic afterload increase.",
    patch: {
      R_sys: 1.80,
    },
  },
  tachycardia: {
    label: "Sinus tachycardia",
    description: "HR 130, shortened diastole, reduced filling time.",
    patch: {
      HR: 130,
      Tsystole: 0.22,
    },
  },
  bradycardia: {
    label: "Sinus bradycardia",
    description: "HR 45, prolonged diastole, larger SV from increased filling.",
    patch: {
      HR: 45,
      Tsystole: 0.34,
    },
  },
};
