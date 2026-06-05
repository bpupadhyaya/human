---
schema: human-scale-entry/v1
id: magnesium
name: Magnesium
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "Magnesium (Mg, Z=12, [Ne] 3s²). ~25g total; 4th most abundant cation. Cofactor for >300 enzymes; all ATP-utilising reactions require Mg-ATP²⁻. Mg²⁺ blocks NMDA receptor pores at rest and competes with Ca²⁺ in cardiomyocytes."
aliases: ["Mg", "Mg2+", "magnesium ion", "magnesium-24"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "~25g total (~0.034% body mass); 4th most abundant cation. 60% in bone, 38% intracellular; cofactor for >300 enzymes and every ATP-utilising reaction in the body."
  - target: 01-human/03-molecular/atp
    relation: modulates
    note: "All kinases and ATPases bind Mg-ATP²⁻, not free ATP; Mg²⁺ chelates the β,γ-phosphates of ATP, activating the complex and positioning the γ-phosphate for nucleophilic attack by substrate."
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "Mg²⁺ provides voltage-dependent block of the NMDA receptor channel pore at resting membrane potential; depolarisation relieves the block, enabling Ca²⁺ influx essential for long-term potentiation."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: modulates
    note: "Mg²⁺ competes with Ca²⁺ at L-type Ca²⁺ channels and myosin binding sites; hypomagnesaemia predisposes to early afterdepolarisations and torsades de pointes arrhythmia."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: composed-of
    note: "Composed Of by Dietary Magnesium."
---

# Magnesium

## Overview

Magnesium (symbol Mg, atomic number 12, atomic mass 24.31 u) is an alkaline earth metal in Group 2 of the periodic table, with ground-state electron configuration [Ne] 3s². In aqueous solution it exists exclusively as the divalent cation **Mg²⁺** — it carries two positive charges and has a small ionic radius (72 pm), resulting in a very high charge density and slow water exchange kinetics that make it an excellent scaffolding ion for nucleic acids and an obligatory cofactor for ATP-dependent enzymes.

Total body magnesium in a 70 kg adult is approximately **25 g** (~1,000 mmol), making Mg²⁺ the **fourth most abundant cation** after calcium, potassium, and sodium. Despite this abundance, serum concentrations (normal range 0.75–0.95 mmol/L total; ~0.55 mmol/L ionised) represent less than 1% of total body stores, making serum Mg²⁺ a poor indicator of total body magnesium status. More than **300 enzymes** require Mg²⁺ as a cofactor, including all ATP-utilising enzymes, nucleic acid polymerases, helicases, and topoisomerases [^stryer-biochemistry].

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 12 |
| Atomic mass | 24.31 u |
| Electron configuration | [Ne] 3s² |
| Ionic form in biology | Mg²⁺ (exclusively divalent) |
| Ionic radius | 72 pm (hexacoordinate) |
| Electronegativity (Pauling) | 1.31 |
| Water exchange rate | ~10⁵–10⁶ s⁻¹ (slower than Ca²⁺, faster than other divalent metals) |

### Body Compartments

| Compartment | Fraction | Amount (~70 kg adult) | Form |
|:---|:---|:---|:---|
| Bone (surface-bound) | ~60% | ~600 mmol | Exchangeable surface Mg²⁺ on hydroxyapatite crystal faces |
| Intracellular | ~38% | ~380 mmol | Mostly protein-bound and Mg-ATP²⁻; free [Mg²⁺]i ~0.5–1 mmol/L |
| Extracellular/serum | ~2% | ~20 mmol | ~55% ionised Mg²⁺; ~30% protein-bound (albumin); ~15% complexed |

### Mg²⁺ Coordination Chemistry

Mg²⁺ forms strong, kinetically stable **octahedral hexacoordinate** complexes. In biological settings it coordinates to:
- Oxygen atoms of phosphate groups (key for Mg-ATP and Mg-GTP complexes)
- Carboxylate oxygens of Asp/Glu residues in enzyme active sites
- Nitrogen N7 of guanine/adenine in nucleic acid folds (rRNA, ribozymes)
- Water molecules completing the coordination shell

The high charge density and slow ligand exchange of Mg²⁺ (compared to Ca²⁺, which has a larger radius and faster exchange) explains why Mg²⁺ is the preferred structural cation for ribosomes and catalytic RNAs, while Ca²⁺ is preferred for fast signaling [^stryer-biochemistry].

## Function

### Mg-ATP — the Active Form of ATP

A critical and often overlooked fact: **kinases and ATPases bind Mg-ATP²⁻, not free ATP⁴⁻.** Mg²⁺ chelates the β- and γ-phosphates of ATP, partially neutralising the four negative charges and positioning the γ-phosphate for nucleophilic attack by the substrate (protein Ser/Thr/Tyr in kinases; ion-binding sites in ATPases). Without Mg²⁺:

- ATP hydrolysis rates by enzymes drop by orders of magnitude.
- The active-site geometry of kinases cannot be achieved (Mg²⁺ bridges the phosphates and positions the DFG-motif Asp residue in the kinase activation loop).

Given that cellular [ATP] is ~3–5 mmol/L and free [Mg²⁺]i is ~0.5–1 mmol/L, essentially all intracellular ATP is present as Mg-ATP²⁻ — making intracellular Mg²⁺ and ATP functionally inseparable [^stryer-biochemistry].

### Ribosome Structure and Translation Fidelity

Each bacterial 70S ribosome harbours approximately **120 Mg²⁺ ions**, and eukaryotic ribosomes contain comparable numbers. These ions:

1. Neutralise the high local negative charge density of rRNA phosphodiester backbone, enabling tertiary folding that brings distal sequences into the peptidyl transferase center and decoding center.
2. Stabilise the A, P, and E sites — correct Mg²⁺ concentration (&gt;1 mmol/L) is required for translational accuracy (discrimination against near-cognate tRNAs).
3. Low Mg²⁺ leads to ribosome subunit dissociation (disassembly of 80S → 40S + 60S), globally suppressing protein synthesis — relevant in severe hypomagnesaemia.

### NMDA Receptor Mg²⁺ Block — Coincidence Detector

The NMDA-type glutamate receptor (NR1/NR2 subunit heterotetramer) is the molecular basis for Hebbian long-term potentiation (LTP), the cellular correlate of learning and memory. At the resting membrane potential (~−70 mV):

- **Mg²⁺ occludes the ion channel pore** in a voltage-dependent manner, blocking Na⁺ and Ca²⁺ influx even when glutamate is bound.
- Depolarisation of the postsynaptic membrane (by AMPA receptor activity) **relieves the Mg²⁺ block**, allowing NMDA receptor activation.
- This coincidence detection property (presynaptic glutamate release AND postsynaptic depolarisation required simultaneously) is the molecular implementation of Hebb's rule: "neurons that fire together wire together."
- Mg²⁺ deficiency reduces the threshold for NMDA receptor activation → hyperexcitability → seizures, a recognized complication of severe hypomagnesaemia [^guyton-hall].

### Cardiac Electrophysiology — Ca²⁺ Antagonism

Magnesium competes with calcium at two key sites in cardiomyocytes:

1. **L-type Ca²⁺ channels (Cav1.2)**: Mg²⁺ partially occludes the channel at physiological concentrations, dampening the inward Ca²⁺ current (ICaL). Low Mg²⁺ → augmented ICaL → prolonged action potential plateau → risk of early afterdepolarisations (EADs).
2. **Myosin binding to actin**: Mg-ATP is the substrate for myosin ATPase, but excess free Mg²⁺ can compete with Ca²⁺ for troponin C — fine-tuning the sensitivity of the contractile apparatus.

Clinical consequence: **hypomagnesaemia** (serum Mg²⁺ &lt;0.75 mmol/L) is a recognized risk factor for **torsades de pointes** (TdP), a polymorphic ventricular tachycardia associated with QT prolongation. Intravenous magnesium sulphate (MgSO₄ 2 g IV over 15 min) is the first-line treatment for TdP and for refractory ventricular fibrillation in the ALS algorithm [^guyton-hall].

### Vascular Smooth Muscle — Physiological Vasodilator

Mg²⁺ acts as a **physiological calcium channel antagonist** in vascular smooth muscle cells:

- Competes with Ca²⁺ entry through voltage-operated Ca²⁺ channels (VOCCs), reducing intracellular [Ca²⁺] and thereby reducing vascular tone.
- Reduces agonist-stimulated Ca²⁺ release from SR (by competing at IP₃R/RyR Ca²⁺ channels).
- Hypomagnesaemia → increased vascular tone → endothelial dysfunction → hypertension.

This mechanism underlies the use of **magnesium sulphate IV** in pre-eclampsia/eclampsia: it causes vasodilatation (lowering blood pressure) and blocks NMDA receptors (preventing eclamptic seizures), providing a dual mechanism of action.

### Magnesium Homeostasis

| Process | Mechanism | Regulation |
|:---|:---|:---|
| Intestinal absorption | TRPM6 and TRPM7 channels in enterocytes (transcellular, ~30–40% of dietary Mg absorbed); paracellular claudin-3/7/12 tight-junction pathway | Calcitriol may upregulate intestinal TRPM6 |
| Renal reabsorption | 60% in thick ascending limb (TAL) — paracellular via claudin-16/19; 10% in distal convoluted tubule (DCT) — TRPM6 (transcellular, fine-tuning) | PTH (↑ DCT reabsorption); aldosterone (↓ reabsorption); metabolic alkalosis (↑ reabsorption) |
| Bone reservoir | Surface Mg²⁺ on hydroxyapatite is readily exchangeable with plasma | Acts as buffer, limiting extreme fluctuations in serum Mg²⁺ |

## Connections

- **Part-of** → [Human Body](../../08-whole-body/human-body/README.md): ~25g total (~0.034% body mass); 4th most abundant cation; 60% in bone and 38% intracellular; cofactor for >300 enzymes and every ATP-utilising reaction throughout the body.
- **Modulates** → [ATP](../../03-molecular/atp/README.md): All kinases and ATPases bind Mg-ATP²⁻, not free ATP; Mg²⁺ chelates the β,γ-phosphates of ATP, activating the complex and precisely positioning the γ-phosphate for nucleophilic attack by substrate.
- **Modulates** → [Neuron](../../04-cellular/neuron/README.md): Mg²⁺ provides voltage-dependent block of the NMDA receptor channel pore at resting membrane potential; depolarisation relieves the block, enabling Ca²⁺ influx essential for long-term potentiation and Hebbian learning.
- **Modulates** → [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md): Mg²⁺ competes with Ca²⁺ at L-type Ca²⁺ channels and myosin binding sites; hypomagnesaemia predisposes to early afterdepolarisations and torsades de pointes arrhythmia; IV MgSO₄ is the first-line treatment.

## Pathology

| Condition | Mechanism | Key features |
|:---|:---|:---|
| **Hypomagnesaemia** | Chronic PPI use (TRPM6 downregulation in gut), loop/thiazide diuretics, alcoholism, aminoglycosides, cisplatin, EGFR inhibitors (cetuximab, panitumumab) | Serum Mg²⁺ &lt;0.75 mmol/L → hypocalcaemia (impairs PTH secretion and action), hypokalaemia (impairs renal K⁺ conservation), arrhythmias, seizures, Chvostek/Trousseau signs |
| **Torsades de pointes** | Hypomagnesaemia + QT-prolonging drugs → EADs | Polymorphic VT; first-line treatment: 2g MgSO₄ IV |
| **Pre-eclampsia/Eclampsia** | Incompletely understood; Mg²⁺ sulphate is first-line prophylaxis/treatment for seizures | Magnesium nimodipine of cerebral vasospasm; maternal and fetal toxicity monitoring required (loss of deep tendon reflexes at ~4 mmol/L, respiratory arrest at ~7 mmol/L) |
| **Hypermagnesaemia** | Renal failure (cannot excrete Mg²⁺) + excessive antacid/laxative use | Hyporeflexia, bradycardia, hypotension, respiratory depression; cardiac arrest at extreme levels |
| **Primary hypomagnesaemia (FHHNC)** | CLDN16 or CLDN19 mutations → defective TAL paracellular Mg²⁺ reabsorption | Familial hypomagnesaemia with hypercalciuria and nephrocalcinosis; progressive CKD |

## See Also

- [ATP](../../03-molecular/atp/README.md) — Mg-ATP²⁻ is the active form of ATP used by all kinases and ATPases.
- [Neuron](../../04-cellular/neuron/README.md) — NMDA receptor Mg²⁺ block is central to synaptic plasticity.
- [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md) — Mg²⁺ modulates cardiac excitation-contraction coupling.
- [Calcium](../calcium/README.md) — the complementary divalent cation; Mg²⁺ and Ca²⁺ compete across many biological sites.
- [Potassium](../potassium/README.md) — hypomagnesaemia causes refractory hypokalaemia (Mg²⁺ required for ROMK function in the distal tubule).

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [elsevier.com](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
