---
schema: human-scale-entry/v1
id: sodium
name: Sodium
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "Na⁺, atomic number 11. Principal extracellular cation (137–145 mmol/L plasma). Inward Na⁺ flux through Nav channels generates the depolarising upstroke of action potentials in neurons and cardiomyocytes. The Na⁺/K⁺-ATPase maintains the gradient; NCX1 couples Na⁺ to Ca²⁺ efflux."
aliases: ["Na", "Na⁺", "sodium ion", "natrium", "hypernatraemia", "hyponatraemia"]
sources:
  - id: hodgkin-huxley-1952
    type: peer-reviewed
    cite: "Hodgkin AL, Huxley AF. A quantitative description of membrane current and its application to conduction and excitation in nerve. J Physiol. 1952;117(4):500-44."
    doi: "10.1113/jphysiol.1952.sp004764"
    pmid: "12991237"
    url: "https://doi.org/10.1113/jphysiol.1952.sp004764"
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
    url: "https://doi.org/10.1038/415198a"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Na⁺ is the principal extracellular cation. Total body sodium is ~92 g (~4000 mmol): ~70% in ECF/plasma (137–145 mmol/L), ~30% complexed in bone hydroxyapatite. Plasma [Na⁺] is the primary determinant of plasma osmolality and total body water distribution."
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "Nav1.2/1.6 open at ~−55 mV, generating inward INa that drives the depolarising upstroke (+40 mV in ~1 ms) of the neuronal action potential. Nav inactivation (1–2 ms) terminates Na⁺ entry; the Hodgkin-Huxley m³h model quantitatively describes this gating."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: modulates
    note: "Nav1.5 (SCN5A) generates fast INa driving Phase 0 depolarisation in cardiomyocytes. The Na⁺ gradient drives NCX1 forward mode (3 Na⁺ in, 1 Ca²⁺ out), removing ~28% of systolic Ca²⁺ per beat. Na⁺ overload in ischaemia reverses NCX1, causing Ca²⁺ overload."
---

# Sodium

## Overview

Sodium (symbol Na, from Latin *natrium*; atomic number 11, atomic mass 22.990 u) is an alkali metal in Group 1 of the periodic table. In biology, it exists exclusively as the monovalent cation **Na⁺**, having lost its single 3s valence electron. It is the **principal cation of the extracellular fluid** and plasma, maintained at 137–145 mmol/L in human blood versus ~12–14 mmol/L intracellularly — a ~10-fold electrochemical gradient across the plasma membrane that is the thermodynamic foundation for neuronal signalling, muscle excitation, and secondary active transport of sugars and amino acids [^hodgkin-huxley-1952].

The physiological importance of sodium was gradually understood through the nineteenth and early twentieth centuries. Sydney Ringer's 1882 experiments established that isotonic NaCl solution was insufficient to keep a frog heart beating — Ca²⁺ and K⁺ were also required — but NaCl (normal saline, 0.9% by mass) provided the osmotic backbone of extracellular fluid. The molecular underpinning of Na⁺'s role in action potentials was established by Hodgkin and Huxley's definitive 1952 series of papers on the squid giant axon, quantifying the voltage- and time-dependence of Na⁺ and K⁺ conductances in mathematical form [^hodgkin-huxley-1952]. Their model — the Hodgkin-Huxley equations — remains the foundational description of membrane excitability and earned them the 1963 Nobel Prize in Physiology or Medicine.

Jens Skou's discovery of the Na⁺/K⁺-ATPase in 1957 — the pump that continuously re-establishes the Na⁺ gradient consumed by each action potential — completed the Na⁺ cycle and earned the 1997 Nobel Prize in Chemistry.

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 11 |
| Atomic mass | 22.990 u |
| Electron configuration | [Ne] 3s¹ |
| Ionic form | Na⁺ (loses 3s¹ electron) |
| Ionic radius (Na⁺) | 102 pm |
| Electronegativity (Pauling) | 0.93 (very low — high tendency to lose electron) |
| Hydration enthalpy (Na⁺) | −406 kJ/mol |
| Coordination number in water | 6 (octahedral) |

### Selectivity of Na⁺ vs. K⁺ Ion Channels

Na⁺ and K⁺ are both monovalent cations, but Nav and Kv channels discriminate between them with >100:1 selectivity. The selectivity filter of the Nav channel — a ring of carbonyl oxygens from four DEKA residues (Asp, Glu, Lys, Ala in the four channel domains) — mimics the hydration shell of Na⁺ (ionic radius 102 pm) but does not accommodate K⁺ (ionic radius 138 pm) efficiently. The opposite selectivity applies in Kv channels (TVGYG selectivity filter, per Doyle et al. crystallography), which perfectly coordinate K⁺ at two sites simultaneously but are too wide to stably bind the smaller Na⁺. This size-based discrimination is the atomic foundation of the action potential.

## Function

### The Sodium Gradient — Electrochemical Basis

The concentration gradient of Na⁺ (extracellular ~140 mmol/L, intracellular ~12 mmol/L) combined with the electrical potential (membrane potential, Vm ~−70 to −90 mV at rest) constitutes the **sodium electrochemical gradient**, quantified by the Nernst equation:

**ENa = (RT/F) · ln([Na⁺]out / [Na⁺]in) ≈ +60 to +65 mV**

At resting Vm of −70 mV, there is ~130 mV of electrochemical driving force for Na⁺ entry into cells. When Nav channels open, Na⁺ rushes inward down this combined concentration and electrical gradient, generating the inward current that depolarises the membrane.

### The Action Potential — Hodgkin-Huxley Model

Hodgkin and Huxley described the neuronal action potential in terms of three conductance changes [^hodgkin-huxley-1952]:

**Phase 1 — Rising phase (upstroke):**
Membrane depolarisation (e.g., from a synaptic input) opens voltage-gated Nav channels. Na⁺ conductance (gNa) increases ~500-fold within 0.1–0.5 ms. INa = gNa × (Vm − ENa) drives Vm from −70 mV toward ENa (+60 mV). Peak Na⁺ current density: ~500 pA/pF in neurons, ~150 pA/pF (Nav1.5) in cardiomyocytes.

**Phase 2 — Inactivation:**
Nav channels inactivate within 1–2 ms (h-gate closure in Hodgkin-Huxley m³h formalism), terminating Na⁺ influx. Membrane potential peaks at ~+20 to +40 mV.

**Phase 3 — Repolarisation:**
K⁺ conductance (gK) increases (Kv channels open with slower kinetics); K⁺ efflux returns Vm toward EK (~−90 mV).

**Absolute refractory period:** Nav channels in their inactivated state cannot reopen until membrane repolarisation allows recovery (~1–2 ms). This unidirectional propagation ensures each action potential travels away from its origin without back-propagation.

**In the heart (Nav1.5):** The cardiac action potential has a longer plateau phase (Phase 2, ~200–400 ms) due to L-type Ca²⁺ channel activation and the absence of the fast Kv channels that repolarise neurons rapidly. But the Phase 0 upstroke is still driven by Nav1.5, with a maximum upstroke velocity (dV/dt)max of 200–300 V/s in ventricular myocytes [^bers-2002-cardiac-ec-coupling].

### Na⁺/K⁺-ATPase — Restoring the Gradient

The Na⁺/K⁺-ATPase (sodium-potassium pump) uses the energy of one ATP to move **3 Na⁺ out** and **2 K⁺ in** per cycle, electrogenic net charge movement of +1 per cycle. This pump consumes ~20–30% of total cellular ATP in neurons and ~10% in resting cardiomyocytes (more during rapid pacing). Pump rate: 100–300 cycles/sec at physiological [Na⁺]i, Vm, and temperature.

Regulation:
- **Intracellular Na⁺:** Primary driver of pump rate — rising [Na⁺]i (as occurs during action potential firing or ischaemia) stimulates the pump.
- **Membrane potential:** Electrogenic; more negative Vm slightly inhibits pump (reduced driving force for net charge extrusion).
- **Phospholemman (PLM):** In cardiac cells, PLM inhibits Na⁺/K⁺-ATPase; PKA phosphorylation of PLM (downstream of β1-AR) relieves inhibition, accelerating pump activity during sympathetic stimulation.
- **Cardiac glycosides (ouabain, digoxin):** Bind to the extracellular aspect of the α-subunit, inhibiting the pump. Used therapeutically in heart failure (modest [Na⁺]i increase → NCX reverse mode → slight Ca²⁺ elevation → positive inotropy), but narrow therapeutic window due to risk of arrhythmia.

### Na⁺/Ca²⁺ Exchanger (NCX1) — Coupling Na⁺ to Ca²⁺

In cardiomyocytes, the Na⁺/Ca²⁺ exchanger NCX1 (SLC8A1) couples Na⁺ and Ca²⁺ fluxes with a 3:1 stoichiometry (3 Na⁺ : 1 Ca²⁺), electrogenic (net charge +1 per forward-mode cycle) [^bers-2002-cardiac-ec-coupling]:

- **Forward mode (net Na⁺ in, Ca²⁺ out):** Thermodynamically favoured at normal [Na⁺]i (~12 mmol/L) and [Ca²⁺]i (~100 nM rest, ~1 µM systole). Removes ~28% of systolic Ca²⁺ per beat.
- **Reverse mode (net Na⁺ out, Ca²⁺ in):** Favoured when [Na⁺]i rises (e.g., ischaemia, heart failure, digitalis toxicity) or during early depolarisation when Na⁺ driving force is transiently reversed. Contributes a small Ca²⁺ trigger in some species.

The NCX1 reversal potential (ENCX) depends on [Na⁺]i, [Ca²⁺]i, and Vm. In ischaemia: glycolytic Na⁺ accumulation + NHE1 activation → [Na⁺]i rises to 20–25 mmol/L → ENCX shifts positive → NCX1 runs in reverse → massive Ca²⁺ entry on reperfusion → cardiomyocyte hypercontracture and necrosis. Elevated [Na⁺]i in failing hearts is a major contributor to blunted Ca²⁺ transients and impaired contractility.

### Secondary Active Transport

The Na⁺ electrochemical gradient established by Na⁺/K⁺-ATPase drives numerous **secondary active transporters** that co-transport other solutes with Na⁺ (symporters) or in exchange (antiporters):

| Transporter | Solute(s) transported | Key location |
|:---|:---|:---|
| SGLT1 (SLC5A1) | 2 Na⁺ : 1 glucose | Intestinal brush border; renal proximal tubule |
| SGLT2 (SLC5A2) | 1 Na⁺ : 1 glucose | Renal proximal tubule (target of gliflozin drugs) |
| GLUT (facilitated) | Glucose (Na-independent) | Muscle, brain |
| NAT (neutral amino acid transporter) | 1 Na⁺ : 1 amino acid | Intestine, kidney |
| NHE1 (Na⁺/H⁺ exchanger) | 1 Na⁺ in : 1 H⁺ out | All cells; cardiac ischaemia-reperfusion Na⁺ loading |
| NET (norepinephrine transporter) | 1 Na⁺ + 1 Cl⁻ : 1 NE | Sympathetic nerve terminals |

### Osmolality and Volume Regulation

Plasma osmolality is ~285–295 mOsm/kg. Since Na⁺ and its associated anions (Cl⁻, HCO₃⁻) account for ~280 mOsm/kg (~95% of plasma osmolality), **[Na⁺]plasma is the primary determinant of plasma volume and, through osmosis, of brain and cell volume**.

Osmolality = 2×[Na⁺] + [glucose]/18 + [BUN]/2.8 (clinical approximation).

The hypothalamic osmoregulatory axis (osmoreceptors → ADH/vasopressin → aquaporin-2 insertion in collecting duct) adjusts renal water reabsorption to maintain plasma [Na⁺] within ±3 mmol/L despite large variations in water intake.

## Connections

- **Part-of** → [Human Body](../../08-whole-body/human-body/README.md): Na⁺ is the dominant extracellular cation, determining plasma osmolality, total extracellular fluid volume, and the electrochemical gradient that powers action potentials.

- **Modulates** → [Neuron](../../04-cellular/neuron/README.md): Inward Na⁺ flux through Nav1.x channels is the molecular event of neural action potential generation; the Hodgkin-Huxley model of m³h gating quantitatively describes how Na⁺ conductance rises and inactivates to produce the all-or-none depolarisation.

- **Modulates** → [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md): Nav1.5 (INa) generates the Phase 0 depolarisation of the cardiac action potential. The Na⁺ gradient maintained by Na⁺/K⁺-ATPase drives NCX1 forward-mode Ca²⁺ extrusion; Na⁺ loading in ischaemia reverses NCX1, causing injurious Ca²⁺ overload.

## Pathology

| Condition | Sodium mechanism |
|:---|:---|
| **Hypernatraemia** ([Na⁺] > 145 mmol/L) | Cellular dehydration → cerebral shrinkage → subdural haemorrhage; causes: ADH deficiency (diabetes insipidus), water loss > Na⁺ loss |
| **Hyponatraemia** ([Na⁺] < 135 mmol/L) | Cellular oedema → cerebral swelling → herniation; causes: SIADH, heart failure (dilutional), cirrhosis, thiazide diuretics |
| **Long QT syndrome (LQT3)** | SCN5A gain-of-function: persistent late INa (late Na⁺ current) prolongs Phase 2–3 of cardiac AP → QT prolongation → torsades de pointes → sudden cardiac death |
| **Brugada syndrome** | SCN5A loss-of-function: reduced Phase 0 INa in right ventricular outflow tract → ST-segment elevation pattern → VT/VF |
| **Ischaemia-reperfusion injury** | NHE1 activation during ischaemia → Na⁺ overload → NCX1 reversal on reperfusion → Ca²⁺ overload → hypercontracture |
| **Primary aldosteronism** | Excess aldosterone → ENaC overactivation in collecting duct → excess Na⁺ reabsorption → volume expansion → hypertension |

## Open Questions

- **Cardiac late Na⁺ current (late INa):** A small persistent Na⁺ current (1–3% of peak INa) through incompletely inactivating Nav1.5 channels appears disproportionately important in action potential duration regulation and Ca²⁺ handling. Ranolazine (late INa inhibitor) improves Ca²⁺ handling in failing hearts; whether this effect is sufficient to alter mortality is being evaluated in ongoing trials.
- **Na⁺ imaging:** ²³Na MRI enables non-invasive imaging of tissue Na⁺ concentration in vivo. Elevated intracellular ²³Na in myocardium has been detected in heart failure patients; whether this predicts pump function or guides therapy is an active research question.

## See Also

- [Neuron](../../04-cellular/neuron/README.md) — Na⁺ is the ion of the action potential upstroke.
- [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md) — Na⁺/K⁺-ATPase and NCX1 link Na⁺ to Ca²⁺ cycling.
- [Potassium](../potassium/README.md) — the complementary intracellular cation; K⁺ efflux repolarises what Na⁺ influx depolarises.

[^hodgkin-huxley-1952]: Hodgkin AL, Huxley AF. A quantitative description of membrane current and its application to conduction and excitation in nerve. *J Physiol.* 1952;117(4):500-44. [doi:10.1113/jphysiol.1952.sp004764](https://doi.org/10.1113/jphysiol.1952.sp004764) · [PubMed 12991237](https://pubmed.ncbi.nlm.nih.gov/12991237/)
[^bers-2002-cardiac-ec-coupling]: Bers DM. Cardiac excitation-contraction coupling. *Nature.* 2002;415(6868):198-205. [doi:10.1038/415198a](https://doi.org/10.1038/415198a) · [PubMed 11805843](https://pubmed.ncbi.nlm.nih.gov/11805843/)
