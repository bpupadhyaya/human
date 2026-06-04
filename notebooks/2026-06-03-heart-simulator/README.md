# Heart Simulator — Programmatic Access (Python / Jupyter)

**Date:** 2026-06-03  
**Author:** Human Engineering project  
**Contact:** bpupadhyaya@gmail.com

## Purpose

This notebook provides programmatic access to the 0D coupled cardiovascular simulator for parameter sweeps, batch scenario comparisons, and research use. It is a Python translation of the browser-runnable simulator at [`docs/sim/heart-0d.js`](../../docs/sim/heart-0d.js), implementing the same physics and parameters using `scipy.integrate.solve_ivp` with the RK45 method (equivalent to the fixed-step RK4 used in the JS version).

## Relation to other project components

- **Browser simulator:** [`docs/heart.html`](../../docs/heart.html) — interactive, real-time simulation in the browser; same model, visualized with SVG anatomy and canvas plots.
- **JS model source:** [`docs/sim/heart-0d.js`](../../docs/sim/heart-0d.js) — the reference implementation.
- **Atlas entries:** The biology modeled here is documented in:
  - [Heart](../../atlases/01-human/06-organ/heart/README.md) — the organ
  - [Cardiovascular System](../../atlases/01-human/07-system/cardiovascular-system/README.md) — the system
  - [Cardiomyocyte](../../atlases/01-human/04-cellular/cardiomyocyte/README.md) — EC coupling
  - [Calcium](../../atlases/01-human/02-atomic/calcium/README.md) — the Ca²⁺ transient that this model abstracts

## Contents

| File | Description |
|:---|:---|
| `heart_simulator_0d.ipynb` | Main Jupyter notebook — model implementation, simulation, plotting, and scenario sweep |

## Reference

Smith BW, Chase JG, Nokes RI, Shaw GM, Wake G. Minimal haemodynamic system model including ventricular interaction and valve dynamics. *Med Eng Phys.* 2004;26(2):131-139. [doi:10.1016/j.medengphy.2003.10.001](https://doi.org/10.1016/j.medengphy.2003.10.001)

## Running the notebook

```bash
pip install numpy scipy matplotlib jupyter
jupyter notebook heart_simulator_0d.ipynb
```
