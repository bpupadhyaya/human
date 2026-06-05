---
schema: human-scale-entry/v1
id: human-body
name: Human body
atlas: 01-human
scale: 08-whole-body
status: draft
last_reviewed: 2026-06-03
summary: "The integrated human organism — the scale at which disease presents and treatment is evaluated. Cardiovascular focus: Fick principle linking cardiac output to O₂ delivery, HRV as autonomic readout, and RAAS as whole-body volume/pressure regulator."
aliases: ["whole body", "organism", "human physiology"]
sources:
  - id: guyton-hall-textbook
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2020. ISBN 978-0-323-59712-8."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-03"
  - id: saltin-calbet-2006-vo2max
    type: peer-reviewed
    cite: "Saltin B, Calbet JA. Point: in health and in a normoxic environment, VO2max is limited by cardiac output. J Appl Physiol. 2006;100(2):744-748."
    doi: "10.1152/japplphysiol.01431.2005"
    pmid: "16428358"
    url: "https://doi.org/10.1152/japplphysiol.01431.2005"
  - id: levine-2008-vo2max
    type: peer-reviewed
    cite: "Levine BD. VO2max: what do we know, and what do we still need to know? J Physiol. 2008;586(1):25-34."
    doi: "10.1113/jphysiol.2007.147629"
    pmid: "17855754"
    url: "https://doi.org/10.1113/jphysiol.2007.147629"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: contains
    note: "The cardiovascular system is part of the whole-body organism; whole-body metrics (BP, CO, VO₂max) integrate cardiovascular function."
  - target: 01-human/06-organ/heart
    relation: contains
    note: "The heart is the pump of the cardiovascular system, which is the primary determinant of VO₂max and whole-body oxygen delivery."
  - target: 01-human/07-system/respiratory-system
    relation: contains
    note: "The respiratory system is one of the eleven major organ systems of the human body; it provides O₂ to the blood and removes CO₂, working in concert with the cardiovascular system to sustain aerobic metabolism."
  - target: 01-human/07-system/nervous-system
    relation: contains
    note: "The nervous system coordinates sensation, motor control, cognition, and autonomic regulation; the brain alone consumes ~20% of the body's resting energy."
  - target: 01-human/07-system/immune-system
    relation: contains
    note: "The immune system defends the body against pathogens and neoplastic cells; its lymphoid organs (bone marrow, thymus, lymph nodes, spleen, MALT) are distributed throughout the body."
  - target: 01-human/07-system/renal-system
    relation: contains
    note: "The renal system maintains fluid, electrolyte, and acid-base homeostasis; the kidneys produce renin, erythropoietin, and calcitriol as systemic hormones."
  - target: 01-human/07-system/digestive-system
    relation: contains
    note: "The digestive system absorbs nutrients from food; the liver is the central metabolic processor linking portal absorption to systemic circulation."
  - target: 01-human/02-atomic/carbon
    relation: contains
    evidence: guyton-hall-textbook
    note: "Carbon is 18% of body mass — ~12.6 kg in a 70 kg adult — the structural backbone of all proteins, lipids, nucleic acids, and carbohydrates."
  - target: 01-human/02-atomic/hydrogen
    relation: contains
    evidence: guyton-hall-textbook
    note: "Hydrogen is the most abundant element by atom count (~60% of atoms), present in every water molecule and every organic bond in the body."
  - target: 01-human/02-atomic/nitrogen
    relation: contains
    evidence: guyton-hall-textbook
    note: "Nitrogen is ~3% of body mass (~2.1 kg), present in all proteins, nucleotide bases, haem porphyrin rings, and signalling molecules including nitric oxide."
  - target: 01-human/02-atomic/sodium
    relation: contains
    evidence: guyton-hall-textbook
    note: "Sodium is ~92 g total body content; as Na⁺ it is the principal extracellular cation determining plasma osmolality and action potential generation."
  - target: 01-human/02-atomic/potassium
    relation: contains
    evidence: guyton-hall-textbook
    note: "Potassium is ~140 g total body content; as K⁺ it is the principal intracellular cation setting resting membrane potential in all excitable and non-excitable cells."
  - target: 01-human/04-cellular/erythrocyte
    relation: contains
    evidence: guyton-hall-textbook
    note: "The human body contains ~25 trillion erythrocytes, the most abundant cell type, circulating continuously to deliver O₂ to every tissue."
  - target: 01-human/04-cellular/macrophage
    relation: contains
    evidence: guyton-hall-textbook
    note: "Macrophages number ~200–400 billion in the human body, resident in all tissues as Kupffer cells, alveolar macrophages, microglia, and other tissue-specific forms."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: contains
    evidence: guyton-hall-textbook
    note: "NK cells number ~2–7 billion in the human body, circulating in blood and residing in liver, lung, uterus, and lymphoid tissues as innate immune sentinels."
  - target: 01-human/05-tissue/bone-marrow
    relation: contains
    evidence: guyton-hall-textbook
    note: "Bone marrow (~1.5 kg in adults) fills the medullary cavities of flat and long bones, producing ~500 billion blood cells per day."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: contains
    evidence: guyton-hall-textbook
    note: "Intestinal epithelium lines ~32 m² of bowel surface, replaced every 3–5 days; the largest renewable epithelial surface in the human body."
---

# Human body

## Overview

The human body is the scale at which medicine operates: where symptoms are experienced, where diagnoses are made, where therapies are applied, and where outcomes are measured. All seven scales below — from the electron configuration of calcium to the cardiovascular system — contribute constraints and behaviors that emerge, at the organism level, as the physiology (and pathology) of a living person [^guyton-hall-textbook].

This entry focuses on **cardiovascular coupling at the whole-body level**: the quantitative relationships between cardiac pump function, oxygen delivery, and whole-body metabolic demand; the autonomic nervous system's role in moment-to-moment homeostasis; the RAAS as a multi-organ pressure-volume regulator; and the whole-body metrics (VO₂max, HRV, blood pressure, BNP) that serve as observable windows into multi-scale function.

## Structure

The human body at scale 08 is composed of eleven major organ systems that function as a tightly coupled network. For the purposes of this atlas and the cardiovascular focus of the current vertical slice, the most important functional relationships are:

| System pair | Coupling mechanism |
|:---|:---|
| **Heart — vasculature** | Frank-Starling (venous return → EDV → SV), arterial baroreflex (BP → HR/SVR) |
| **Heart — lungs** | Pulmonary circuit delivers oxygenated blood to left heart; VE/VCO₂ coupling |
| **Heart — kidneys** | RAAS (renin from JG cells), fluid balance, natriuretic peptides (ANP, BNP) |
| **Heart — autonomic nervous system** | Sympathetic (β1-AR, α1, renin) and parasympathetic (M2, vagal) modulation |
| **Cardiovascular — skeletal muscle** | Oxygen delivery (CO × arterial O₂ content) drives aerobic capacity |

## Function

### Cardiovascular Coupling and the Fick Principle

The **Fick principle** is the quantitative heart of whole-body oxygen physiology:

$$
\text{VO}_2 = \text{CO} \times (C_{a\text{O}_2} - C_{v\text{O}_2})
$$

where VO₂ is whole-body oxygen consumption (mL/min), CO is cardiac output (L/min), and (C_aO₂ − C_vO₂) is the arteriovenous oxygen content difference. At rest, VO₂ ≈ 250 mL/min; at maximal exercise, VO₂max ≈ 3–5 L/min in trained individuals.

**VO₂max is primarily limited by cardiac output** — this is the consensus of the Saltin-Calbet analysis [^saltin-calbet-2006-vo2max]: in normoxia and health, the oxygen extraction by exercising muscle can exceed what a trained heart can deliver, making cardiac output the bottleneck. Endurance training increases CO_max from ~20 L/min to ~35–40 L/min in elite athletes, almost entirely through increased maximal stroke volume (via eccentric remodeling) rather than increased maximal heart rate.

Levine (2008) provides the most rigorous analysis of what VO₂max measures and what limits it [^levine-2008-vo2max]: central (cardiac output) and peripheral (muscle oxidative capacity, mitochondrial density, capillarization) factors both contribute, with cardiac output dominant in normally sedentary adults and muscle capacity becoming more important in highly trained states.

### Autonomic Regulation and Heart Rate Variability

The autonomic nervous system modulates cardiovascular function on a beat-to-beat basis through two limbs:

- **Sympathetic:** Norepinephrine at β1-AR (heart: ↑HR, ↑contractility, ↑conduction) and α1 (vasculature: vasoconstriction, ↑SVR). Epinephrine from adrenal medulla amplifies during stress.
- **Parasympathetic:** Acetylcholine at M2 muscarinic receptors (SA node: ↓HR via IKAch; AV node: ↓dromotropy). Vagal tone is dominant at rest (resting HR = intrinsic SA rate ~100 bpm minus vagal inhibition to ~60–80 bpm).

**Heart rate variability (HRV)** — the variation in R-R intervals on ECG — is a whole-body metric reflecting the balance of sympathetic and parasympathetic modulation of SA-nodal firing. High HRV (particularly the high-frequency component, HF-HRV) reflects strong vagal tone and is associated with better cardiovascular health, lower all-cause mortality, and greater cardiac reserve. HRV declines with age, heart failure, diabetes, and autonomic neuropathy. It can be measured non-invasively from a 24-hour Holter ECG [^guyton-hall-textbook].

### RAAS — The Whole-Body Volume/Pressure Regulator

The renin-angiotensin-aldosterone system is the body's primary multi-organ mechanism for long-term regulation of blood pressure and extracellular fluid volume:

1. **Renal JG cells** detect reduced renal perfusion pressure, sympathetic stimulation (via β1-AR), and hyponatremia → release **renin**.
2. **Renin** cleaves angiotensinogen (liver) → **angiotensin I** (inactive).
3. **ACE** (lung, vascular endothelium) converts Ang I → **angiotensin II** (Ang II).
4. **Ang II effects:**
   - Vasoconstriction (AT1 receptor on vascular smooth muscle → ↑SVR → ↑MAP)
   - Adrenal cortex → **aldosterone** → Na⁺/H₂O retention → ↑blood volume → ↑venous return → ↑CO
   - ADH release (posterior pituitary) → renal water retention
   - Thirst (hypothalamus)
   - Cardiac fibrosis and hypertrophy (maladaptive in chronic heart failure)

RAAS dysregulation is central to hypertension and heart failure. The most evidence-based treatments in HFrEF target RAAS: ACE inhibitors, ARBs, and the combination ARNi (sacubitril/valsartan) — all block Ang II production or action.

### Exercise Physiology at the Organism Scale

During exercise, cardiac output must increase 4–5 fold (from ~5 to ~20–25 L/min) within seconds-to-minutes. The integrated response involves:

1. **Anticipatory heart rate rise** (central command, before exercise begins)
2. **Muscle metaboreflex** (local muscle metabolites activate afferent group III/IV fibers → ↑sympathetic output)
3. **Venous return augmentation** (muscle pump action, venous tone, respiratory pump)
4. **Frank-Starling augmentation of SV** (increased EDV with higher venous return)
5. **Sympathetic-mediated vasodilation in muscle** (β2-AR), vasoconstriction in gut/kidney (α1), maintaining MAP

At peak exercise, stroke volume is near-maximal and further CO increase comes from heart rate. Cardiac output is the primary determinant of VO₂max.

## Connections

- **Contains** → [Cardiovascular System](../../07-system/cardiovascular-system/README.md): The cardiovascular system is the primary whole-body transport network; CO and MAP are the dominant whole-body hemodynamic variables.
- **Contains** → [Heart](../../06-organ/heart/README.md): The heart as pump is the central determinant of VO₂max and cardiovascular reserve at the organism scale.
- **Cross-atlas (planned):** The whole-body scale is where clinical trials measure outcomes — mortality, VO₂max, 6-minute walk distance, quality of life. Medicine Atlas entries will cross-link to this scale when documenting whole-body effects of pharmacotherapy.

## Pathology

Whole-body cardiovascular disease — emergent from multi-scale dysfunction:

| Whole-body phenotype | Multi-scale origin |
|:---|:---|
| **Hypertension** | Na⁺ retention (kidney), ↑RAAS, ↑SNS, ↑vascular tone, arterial stiffness |
| **Exercise intolerance** | ↓VO₂max from ↓CO_max (HFrEF), ↓skeletal muscle oxidative capacity, or both |
| **Heart failure syndrome** | ↓CO → renal retention (RAAS/ADH) → fluid overload (edema, ascites, pulmonary edema) + ↓tissue perfusion |
| **Orthostatic hypotension** | ↓baroreflex sensitivity, ↓venous return compensation on standing |
| **Shock** | Failure of CO or SVR to maintain MAP ≥ 60 mmHg → organ hypoperfusion → failure cascade |

## Variation

- **Sex.** Women have higher resting HR, lower VO₂max (per kg body weight) partly due to lower hemoglobin mass, smaller LV EDV, and lower SV at rest; exercise training narrows the gap.
- **Age.** VO₂max declines ~10% per decade after age 25 (cardiac and peripheral factors); HRV declines; baroreflex sensitivity declines; arterial stiffness increases.
- **Athletic training.** The most trainable cardiovascular variable is maximal CO — primarily through SV augmentation (eccentric cardiac hypertrophy, increased plasma volume, enhanced venous return). Resting HRV increases; resting HR falls.
- **Altitude.** At high altitude, reduced O₂ partial pressure decreases CaO₂ → VO₂max falls (Fick equation); the body adapts by increasing HR, Hgb synthesis (EPO), and ventilation.

## Open Questions

- **What limits VO₂max at the whole-body level in sedentary vs. elite athletes?** The relative contributions of cardiac output, blood O₂ content, and muscle oxidative capacity remain an area of active study [^levine-2008-vo2max].
- **HRV as a prognostic tool.** While low HRV strongly predicts cardiovascular mortality, whether HRV-guided therapy improves outcomes has not been definitively demonstrated.
- **Sex-specific VO₂max trajectories.** How much of the male-female VO₂max difference is biological vs. historical societal differences in activity levels? This is now measurable with large population studies.

## See Also

- [Cardiovascular system](../../07-system/cardiovascular-system/README.md)
- [Heart](../../06-organ/heart/README.md)

[^guyton-hall-textbook]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2020. [elsevier.com](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
[^saltin-calbet-2006-vo2max]: Saltin B, Calbet JA. Point: in health and in a normoxic environment, VO2max is limited by cardiac output. *J Appl Physiol.* 2006;100(2):744-748. [doi:10.1152/japplphysiol.01431.2005](https://doi.org/10.1152/japplphysiol.01431.2005) · [PubMed 16428358](https://pubmed.ncbi.nlm.nih.gov/16428358/)
[^levine-2008-vo2max]: Levine BD. VO2max: what do we know, and what do we still need to know? *J Physiol.* 2008;586(1):25-34. [doi:10.1113/jphysiol.2007.147629](https://doi.org/10.1113/jphysiol.2007.147629) · [PubMed 17855754](https://pubmed.ncbi.nlm.nih.gov/17855754/)
