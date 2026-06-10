---
schema: human-scale-entry/v1
id: epinephrine
name: Epinephrine
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Catecholamine (MW 183.21) synthesised from norepinephrine by PNMT in adrenal medulla chromaffin cells. Activates α₁, α₂, β₁, β₂, β₃ adrenergic receptors mediating fight-or-flight response. First-line treatment for anaphylaxis. Phaeochromocytoma causes paroxysmal hypertension."
aliases: ["adrenaline", "Epi", "epinephrin", "4-(1-hydroxy-2-(methylamino)ethyl)-1,2-benzenediol"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: blaschko-1939
    type: peer-reviewed
    cite: "Blaschko H. The specific action of L-DOPA decarboxylase. J Physiol. 1939;96(1):50-51."
    url: "https://doi.org/10.1113/jphysiol.1939.sp003748"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: modulates
    note: "Epinephrine binds β₁AR (Gs) on SA node and ventricular cardiomyocytes → ↑cAMP → PKA phosphorylates L-type Ca channel, RyR2, phospholamban, troponin I → ↑HR, ↑contractility, faster relaxation."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Epinephrine drives fight-or-flight CV response: ↑HR (β₁), ↑contractility (β₁), selective vasoconstriction (α₁ skin/gut) and vasodilation (β₂ muscle) → ↑cardiac output and ↑BP."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "Epinephrine via β₂/α₁ in hepatocytes activates glycogen phosphorylase (cAMP→PKA or IP3→Ca²⁺ pathways) → glycogenolysis → ↑blood glucose; also activates gluconeogenic enzymes."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: modulated-by
    note: "PNMT (Epi-synthesising enzyme in adrenal medulla) is induced by cortisol from portal blood of the adrenal cortex — GR activation in chromaffin cells maintains high epinephrine:norepinephrine ratio."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Epinephrine is synthesised from norepinephrine by PNMT in adrenal chromaffin cells; NE is the primary sympathetic neurotransmitter while Epi predominates in adrenal medullary secretion (~80% Epi, ~20% NE); both catecholamines are degraded by MAO/COMT to urinary metanephrines."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol from adrenal cortex reaches chromaffin cells via intra-adrenal portal circulation at 10-100× systemic levels → GR activation → PNMT induction → Epi synthesis; stress co-activates HPA (cortisol) and sympathoadrenal (Epi) axes; hypophysectomy reduces PNMT → ↓Epi/NE ratio."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine is the immediate precursor to norepinephrine in the Blaschko pathway; TH (tyrosine hydroxylase) is the rate-limiting step for all catecholamines; dopamine β-hydroxylase converts dopamine to NE in chromaffin granules; PNMT methylates NE to epinephrine using SAM."
---

# Epinephrine

## Overview

Epinephrine (adrenaline) is a catecholamine hormone and neurotransmitter (MW 183.21 Da) secreted primarily by the **chromaffin cells of the adrenal medulla** in response to stress, exercise, hypoglycaemia, or haemorrhage. It is the terminal product of the **Blaschko biosynthetic pathway**, synthesised from norepinephrine by phenylethanolamine-N-methyltransferase (PNMT).[^blaschko-1939] Circulating epinephrine acts on α₁, α₂, β₁, β₂, and β₃ adrenergic receptors throughout the body to co-ordinate the **fight-or-flight response** — increasing cardiac output, redistributing blood flow, mobilising glucose, and dilating airways.[^stryer-biochemistry] Pharmacologically, it is the first-line agent for anaphylaxis and cardiac arrest.

## Structure

Epinephrine is a **catechol** (3,4-dihydroxybenzene) with an **aminoethanol** side chain bearing a methyl group on the amino nitrogen — hence: **N-methylnorepinephrine**. Key chemical features:

- **Catechol ring** (3,4-diOH): critical for adrenergic receptor binding; oxidised by COMT (O-methylation at 3-OH) in catabolism.
- **Chiral centre** at the benzylic carbon (C-1 of the side chain): the **L-(R)-isomer** (natural) is ~10–100× more potent than D-(S)-epinephrine at adrenergic receptors.
- **Secondary amine** (N-methyl): distinguishes epinephrine from norepinephrine (primary amine); the methyl group confers higher β₂-receptor affinity than NE.[^stryer-biochemistry]

**Storage**: chromaffin granules contain epinephrine packaged with chromogranin A/B, ATP, enkephalins, and neuropeptide Y (NPY), at high concentration (~0.5 M in acidic granule lumen).

## Function

### Adrenergic Receptor Profile

| Receptor | G-protein | Second messenger | Primary tissue | Epinephrine effect |
|----------|-----------|-----------------|---------------|-------------------|
| α₁ | Gq | PLC → IP3/DAG → ↑Ca²⁺ | Vascular smooth muscle, iris | Vasoconstriction, mydriasis |
| α₂ | Gi | ↓adenylyl cyclase | Presynaptic terminals, β-cells, platelets | ↓NE release (autoreceptor), ↓insulin, platelet aggregation |
| β₁ | Gs | ↑cAMP → PKA | Heart, kidney | ↑HR, ↑contractility, ↑renin |
| β₂ | Gs | ↑cAMP → PKA | Bronchi, skeletal muscle vessels, liver, uterus | Bronchodilation, vasodilation, glycogenolysis, ↑glucagon |
| β₃ | Gs | ↑cAMP → PKA | Adipose, BAT | Lipolysis, thermogenesis |

Epi has higher **β₂ affinity** than NE — central to its bronchodilating and metabolic effects.

### Metabolic Role

- **Hepatic glycogenolysis**: β₂ → ↑cAMP → PKA → phosphorylase kinase → glycogen phosphorylase → glycogen → glucose-1-phosphate → glucose released.[^stryer-biochemistry]
- **Adipose lipolysis**: β₃/β₁ → ↑cAMP → PKA → hormone-sensitive lipase (HSL) phosphorylation + perilipin A phosphorylation → triglyceride hydrolysis → FFA + glycerol released.
- **Gluconeogenesis**: indirect — ↑FFA (substrate), ↑glucagon (β₂ on pancreatic α-cells), ↑lactate from muscle (Cori cycle substrate).
- **↓Insulin**: α₂ on pancreatic β-cells → ↓cAMP → ↓insulin secretion; together with ↑glucagon shifts liver toward net glucose output.

## Mechanism

### Biosynthesis — Blaschko Pathway

All five steps occur in adrenal medulla chromaffin cells:[^blaschko-1939][^stryer-biochemistry]

```
L-Phenylalanine
     ↓  PAH (phenylalanine hydroxylase)
L-Tyrosine
     ↓  TH (tyrosine hydroxylase) — RATE-LIMITING
         cofactors: Fe²⁺, BH4, O₂; product inhibition by NE
L-DOPA
     ↓  AADC (aromatic L-amino acid decarboxylase / DOPA decarboxylase)
         cofactor: pyridoxal phosphate (PLP)
Dopamine
     ↓  DβH (dopamine β-hydroxylase) — VESICULAR, Cu²⁺/ascorbate/O₂
Norepinephrine
     ↓  PNMT (phenylethanolamine-N-methyltransferase) — CYTOSOLIC
         methyl donor: SAM (S-adenosyl-methionine)
         INDUCED by glucocorticoid (cortisol via portal blood from adrenal cortex → GR activation)
Epinephrine
```

**PNMT regulation**: cortisol from the adrenal cortex reaches chromaffin cells via the intra-adrenal portal circulation at high concentration (~10–100× systemic), sustaining PNMT expression. Hypophysectomy or adrenalectomy reduces PNMT → ↓ Epi/NE ratio.[^alberts-mol-cell-biology]

### Secretion

Splanchnic nerve (preganglionic sympathetic, ACh) → **nicotinic nAChR** on chromaffin cells → depolarisation → **VGCCs** open → Ca²⁺ influx → exocytosis of chromaffin granules into the adrenal vein → systemic circulation. t½ ~2 min.[^alberts-mol-cell-biology]

### Signal Transduction (β₂ example)

Epi binds β₂AR → conformational change → Gαs dissociates → activates **adenylyl cyclase (AC)** → ↑cAMP → activates **PKA (protein kinase A)** → phosphorylates effectors:
- Bronchial smooth muscle: MLCK inhibition + K⁺ channel activation → relaxation → bronchodilation
- Cardiomyocyte (β₁): L-type Ca²⁺ channel (Cav1.2), RyR2, phospholamban → ↑Ca²⁺ transient → ↑contractility + ↑relaxation rate

β-Arrestin desensitisation: PKA phosphorylates the β₂AR itself (and GRKs phosphorylate further) → β-arrestin binding → receptor internalisation (endocytosis) → signal termination after sustained stimulation.[^alberts-mol-cell-biology]

### Catabolism

Primary enzymes:
- **MAO** (monoamine oxidase, mitochondrial, MAO-A > MAO-B): oxidative deamination → DOPGAL
- **COMT** (catechol-O-methyltransferase, cytosolic, SAM-dependent): O-methylation of the 3-OH → metanephrine

Sequential action → **vanillylmandelic acid (VMA)** + **metanephrine** (and normetanephrine from NE). Both are excreted in urine — measured in 24h urine or plasma for phaeochromocytoma diagnosis.[^stryer-biochemistry]

## Connections

- `modulates` → **[β₁-Adrenergic Receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — Epinephrine binds β₁AR (Gs) on SA node and ventricular cardiomyocytes → ↑cAMP → PKA phosphorylates L-type Ca channel, RyR2, phospholamban, troponin I → ↑HR, ↑contractility, faster relaxation.
- `modulates` → **[Cardiovascular System](../../07-system/cardiovascular-system/README.md)** — Epinephrine drives fight-or-flight CV response: ↑HR (β₁), ↑contractility (β₁), selective vasoconstriction (α₁ skin/gut) and vasodilation (β₂ muscle) → ↑cardiac output and ↑BP.
- `modulates` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Epinephrine via β₂/α₁ in hepatocytes activates glycogen phosphorylase (cAMP→PKA or IP3→Ca²⁺ pathways) → glycogenolysis → ↑blood glucose; also activates gluconeogenic enzymes.
- `modulated-by` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — PNMT (Epi-synthesising enzyme in adrenal medulla) is induced by cortisol from portal blood of the adrenal cortex — GR activation in chromaffin cells maintains high epinephrine:norepinephrine ratio.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Epinephrine is synthesised from norepinephrine by PNMT in adrenal chromaffin cells; NE is the primary sympathetic neurotransmitter while Epi predominates in adrenal medullary secretion (~80% Epi, ~20% NE); both catecholamines are degraded by MAO/COMT to urinary metanephrines.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol from adrenal cortex reaches chromaffin cells via intra-adrenal portal circulation at 10-100× systemic levels → GR activation → PNMT induction → Epi synthesis; stress co-activates HPA (cortisol) and sympathoadrenal (Epi) axes; hypophysectomy reduces PNMT → ↓Epi/NE ratio.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine is the immediate precursor to norepinephrine in the Blaschko pathway; TH (tyrosine hydroxylase) is the rate-limiting step for all catecholamines; dopamine β-hydroxylase converts dopamine to NE in chromaffin granules; PNMT methylates NE to epinephrine using SAM.

## Pathology

### Phaeochromocytoma
Adrenal medullary chromaffin cell tumour (90% benign; "rule of 10s": 10% bilateral, 10% extra-adrenal, 10% malignant, 10% paediatric). Excess Epi/NE secretion (often paroxysmal): **headache, diaphoresis, palpitations, paroxysmal hypertension** (triad). Diagnosis: plasma/24h urine **fractionated metanephrines** (normetanephrine + metanephrine — most sensitive/specific); imaging (CT/MRI → MIBG scan for extra-adrenal). Treatment: **alpha-blockade first** (phenoxybenzamine irreversible α1/α2, then β-blocker added — NEVER β-blocker first as unopposed α → hypertensive crisis) → surgical adrenalectomy.[^stryer-biochemistry]

### Anaphylaxis
Immediate hypersensitivity (IgE → mast cell degranulation → histamine, leukotrienes, tryptase) → ↓BP (vasodilation, capillary leak), bronchospasm, laryngeal oedema, urticaria. Treatment: **IM epinephrine 0.3–0.5 mg (1:1000)** — β₂ → bronchodilation, α₁ → vasoconstriction ↑BP, β₁ → ↑HR. Must be given before antihistamines/corticosteroids (which are adjuncts).[^alberts-mol-cell-biology]

### Cardiogenic Shock
Epinephrine IV (low dose: β₁/β₂ predominate; high dose: α₁ adds vasoconstriction) is used when norepinephrine + dobutamine insufficient. Risk: ↑myocardial O₂ demand, arrhythmia.

### Hypoglycaemia Response
Falling blood glucose → hypothalamic → splanchnic nerve → Epi release → glycogenolysis + gluconeogenesis + ↑glucagon → glucose recovery. **Hypoglycaemia unawareness** in type 1 DM: repeated hypoglycaemia blunts this counter-regulatory Epi response (hypoglycaemia-associated autonomic failure, HAAF).

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry*. 9th ed. W.H. Freeman; 2019.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell*. 7th ed. W.W. Norton; 2022.
[^blaschko-1939]: Blaschko H. The specific action of L-DOPA decarboxylase. *J Physiol*. 1939;96(1):50-51.
