---
schema: human-scale-entry/v1
id: iodine
name: Iodine
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "Iodine (I⁻, atomic number 53) — 15–20 mg total, ~75% in thyroid. Essential for T3/T4 synthesis via NIS uptake, TPO organification, and thyroglobulin coupling. Deficiency causes goitre, hypothyroidism, and cretinism — the leading preventable cause of intellectual disability."
aliases: ["I", "I-", "iodide", "iodine-127", "organically-bound iodine"]
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
  - id: bizhanova-kopp-nis
    type: peer-reviewed
    cite: "Bizhanova A, Kopp P. Minireview: The sodium-iodide symporter NIS and pendrin in iodide homeostasis of the thyroid. Endocrinology. 2009;150(3):1084-90."
    doi: "10.1210/en.2008-1437"
    pmid: "19196800"
    url: "https://doi.org/10.1210/en.2008-1437"
  - id: zimmermann-iodine-deficiency
    type: peer-reviewed
    cite: "Zimmermann MB, Boelaert K. Iodine deficiency and thyroid disorders. Lancet Diabetes Endocrinol. 2015;3(4):286-95."
    doi: "10.1016/S2213-8587(14)70225-6"
    pmid: "25591468"
    url: "https://doi.org/10.1016/S2213-8587(14)70225-6"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "15–20 mg total; 70–80% in thyroid as organically bound iodine within thyroglobulin. Essential for thyroid hormone synthesis; dietary requirement 150 µg/day adults, 250 µg/day pregnancy."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Thyroid hormones T3/T4 (iodine-containing) are essential for CNS myelination during fetal and neonatal development; severe deficiency causes cretinism — irreversible cognitive impairment."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "T3 increases cardiac output, heart rate, myocardial contractility, and O₂ consumption; hypothyroidism causes bradycardia, reduced CO; hyperthyroidism causes tachycardia and AF risk."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "DIO1, DIO2, and DIO3 — the three iodothyronine deiodinases — all contain selenocysteine; they catalyse T4→T3 (activation) and T3→T2 / T4→rT3 (inactivation); GPx and TrxR neutralise thyroidal DUOX2-generated H₂O₂; combined I+Se deficiency causes myxoedematous cretinism."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "NIS (SLC5A5) concentrates I⁻ 20–40-fold into follicular cells; TPO organifies iodide onto thyroglobulin tyrosines (MIT, DIT) and couples them to form T4 (DIT+DIT) and T3 (MIT+DIT); the thyroid stores 70–80% of total body iodine; TSH drives NIS expression and TPO activity."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "T4 contains 4 iodine atoms (65% of its 777 Da mass); T3 contains 3; iodine is the rate-limiting substrate for thyroid hormone synthesis; DIO1/2 peripherally deiodinate T4→T3; radioiodine (¹³¹I, t½=8 d) exploits NIS for targeted thyroid ablation therapy."
---

# Iodine

## Overview

Iodine (symbol I, atomic number 53) is a **halogen** in Group 17 of the periodic table, with atomic mass 126.90 u and electron configuration [Kr] 4d¹⁰ 5s² 5p⁵. In biology, iodine exists exclusively as the monovalent anion **iodide (I⁻)**; it is the heaviest stable element with an essential physiological function in humans. The total body iodine content is approximately **15–20 mg**, of which 70–80% is concentrated in the **thyroid gland** as organically bound iodine covalently attached to the protein thyroglobulin — a unique feature that distinguishes iodine from virtually every other essential trace element [^guyton-hall].

Iodine's sole confirmed physiological function is as a **building block of thyroid hormones**: thyroxine (T4, 3,5,3',5'-tetraiodothyronine) and triiodothyronine (T3, 3,5,3'-triiodothyronine). These iodinated amino acid derivatives act as ligands for nuclear thyroid hormone receptors (TRα, TRβ), regulating transcription of hundreds of genes involved in development, metabolism, thermoregulation, and cardiovascular function. The scale of iodine's global health impact is extraordinary: iodine deficiency disorders (IDDs) affect an estimated **2 billion people** worldwide and remain the **leading preventable cause of intellectual disability** [^zimmermann-iodine-deficiency].

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 53 |
| Atomic mass | 126.90 u |
| Electron configuration | [Kr] 4d¹⁰ 5s² 5p⁵ |
| Ionic form in biology | I⁻ (iodide; gains 1 electron) |
| Ionic radius (I⁻) | 0.220 nm (220 pm) |
| Electronegativity (Pauling) | 2.66 |
| Stable isotopes | ¹²⁷I (only stable isotope) |
| Relevant radioisotopes | ¹³¹I (t½ = 8.02 d; thyroid cancer therapy / diagnosis), ¹²³I (imaging) |

### Structure of Thyroid Hormones

Thyroid hormones are iodinated derivatives of the amino acid **L-tyrosine**, covalently coupled as T4 and T3:

| Hormone | Full name | Iodine atoms | Biological activity | Half-life |
|:---|:---|:---:|:---|:---|
| **T4** (thyroxine) | 3,5,3',5'-tetraiodothyronine | 4 | Prohormone; converted to T3 peripherally | ~7 days |
| **T3** | 3,5,3'-triiodothyronine | 3 | Active form; 3–5× more potent than T4 | ~1 day |
| **rT3** | 3,3',5'-triiodothyronine (reverse T3) | 3 | Inactive isomer; produced during illness/fasting | ~0.2 days |
| **MIT** | Monoiodotyrosine | 1 | Synthetic intermediate; not secreted | — |
| **DIT** | Diiodotyrosine | 2 | Synthetic intermediate; not secreted | — |

T4 and T3 are highly lipophilic and travel in blood bound to **thyroxine-binding globulin (TBG)** (~70%), **transthyretin** (~10–15%), and **albumin** (~15–20%). Only the free fractions (fT4 ~0.03%, fT3 ~0.3%) are biologically active and enter cells.

### Thyroglobulin (Tg)

Thyroglobulin is a massive homodimeric glycoprotein (660 kDa per dimer) that serves as both the **template** and **storage matrix** for thyroid hormone synthesis. Each Tg monomer contains ~140 tyrosine residues, of which only about 20–30 are accessible for iodination, and typically 2–3 T4 and 0.5–1.0 T3 molecules are formed per Tg dimer under euthyroid conditions. The follicle lumen (colloid) is filled with Tg solution at concentrations of ~100 mg/mL, representing a substantial intraglandular iodine/hormone reserve.

## Function

### Step-by-Step Thyroid Hormone Synthesis

**1. Dietary iodide absorption:** Ingested iodide (I⁻) is rapidly absorbed in the stomach and proximal small intestine. Iodide is not protein-bound and is freely filtered by the glomerulus; renal clearance of iodide is ~30 mL/min, and urinary iodide excretion is the standard measure of population iodine status (median UIE ≥100 µg/L = adequate).

**2. Thyroidal uptake via NIS:** The sodium-iodide symporter (**NIS, SLC5A5**) on the basolateral membrane of thyroid follicular cells cotransports **2 Na⁺ for every 1 I⁻**, driven by the Na⁺ gradient maintained by Na⁺/K⁺-ATPase. NIS achieves thyroid-to-plasma iodide ratios of 20–40:1 under normal conditions, rising to >100:1 in TSH-stimulated states. NIS is the molecular target of radioiodine (¹³¹I) therapy and is also expressed in the lactating breast and gastric mucosa [^bizhanova-kopp-nis].

**3. Pendrin-mediated apical transport:** Iodide exits the follicular cell apically via **pendrin (SLC26A4)** into the follicle lumen; pendrin functions as an I⁻/Cl⁻ exchanger at the apical membrane. Pendrin mutations cause Pendred syndrome (goitre + sensorineural deafness).

**4. Organification by TPO:** In the follicle lumen, **thyroid peroxidase (TPO)** oxidises I⁻ to a reactive intermediate (I⁰ or I⁺) using H₂O₂ generated by DUOX2 (dual oxidase 2). The reactive iodine then iodinates tyrosine residues on Tg:
- Tg-Tyr + I⁰ → MIT (monoiodotyrosine)
- Tg-Tyr-I + I⁰ → DIT (diiodotyrosine)

**5. Coupling:** TPO also catalyses the **coupling reaction** between adjacent iodotyrosine residues on Tg:
- DIT + DIT → T4 + dehydroalanine (on Tg backbone)
- MIT + DIT → T3 + dehydroalanine

The coupling efficiency depends on the local iodine content; iodine excess favours T4 production over T3.

**6. Tg endocytosis and proteolysis:** TSH stimulates follicular cells to endocytose Tg colloid via micro- and macropinocytosis. Tg-containing phagolysosomes fuse with lysosomes, where cathepsins (B, D, L) and dehalogenases liberate T4 and T3 for secretion into blood.

**7. MIT/DIT recycling:** Released MIT and DIT are deiodinated intracellularly by **iodotyrosine deiodinase (DEHAL1/IYD)**, recovering iodide for reutilisation within the gland — an important intra-thyroidal conservation mechanism.

### Peripheral T4 → T3 Conversion (Deiodinases)

Because T4 is a prohormone with low intrinsic TR affinity, ~80% of circulating T3 in euthyroid humans is derived from peripheral deiodination of T4:

| Deiodinase | Selenocysteine | Location | Reaction | Function |
|:---|:---:|:---|:---|:---|
| **DIO1** | Yes | Liver, kidney, thyroid | 5' and 5 deiodination | Generates circulating T3; also activates reverse T3 |
| **DIO2** | Yes | Brain, pituitary, brown adipose, placenta | 5' deiodination only | Local T3 production; pituitary TSH feedback |
| **DIO3** | Yes | Brain, placenta, fetal liver | 5 deiodination | T3 → T2 (inactive); T4 → rT3 (inactive); fetal protection |

DIO2 in the pituitary generates the T3 that suppresses TSH, making it the critical sensor for the negative feedback loop.

### Wolff-Chaikoff Effect and Iodine Autoregulation

When exposed to high plasma iodide concentrations (>10–6 M), the thyroid acutely **reduces organification** (the Wolff-Chaikoff effect), protecting against thyrotoxicosis. The mechanism involves iodinated lipids (iodolactones) that inhibit TPO and adenylyl cyclase. After ~1–2 weeks, the gland **escapes** from this block by down-regulating NIS expression, reducing intracellular iodide to sub-inhibitory concentrations. In pathological states (Hashimoto thyroiditis, post-partial thyroidectomy), the escape mechanism may fail, producing iodine-induced hypothyroidism (e.g., from amiodarone, povidone-iodine).

### Thyroid Hormone Actions

T3 enters cells and binds nuclear **thyroid hormone receptors (TRα1, TRα2, TRβ1, TRβ2)** — members of the nuclear receptor superfamily. T3-bound TRs dimerize with retinoid X receptors (RXR) and bind thyroid response elements (TRE: AGGTCA half-sites spaced by 4 bp) to activate or repress target genes.

Key physiological effects:
- **Metabolism:** T3 increases basal metabolic rate by upregulating mitochondrial uncoupling proteins and increasing Na⁺/K⁺-ATPase expression; increases glucose absorption and gluconeogenesis
- **Thermogenesis:** Stimulates non-shivering thermogenesis (UCP1 in brown adipose)
- **Development:** Obligatory for CNS myelination (oligodendrocyte maturation), hippocampal synaptogenesis, cochlear development, and normal bone ossification
- **Cardiovascular:** Increases heart rate (upregulates HCN4/If channels and β-adrenergic receptors), myocardial contractility (upregulates MHCα, downregulates phospholamban), and cardiac output; decreases peripheral vascular resistance
- **Pituitary feedback:** T3 produced locally from T4 by DIO2 in pituitary thyrotrophs suppresses TSH transcription and secretion (negative feedback)

## Connections

- `part-of` → **[Human Body](../../08-whole-body/human-body/README.md)** — 15–20 mg total body iodine; 70–80% concentrated in thyroid as organically bound iodine within thyroglobulin; dietary requirement 150 µg/day adults, 250 µg/day in pregnancy; urinary iodide excretion is the standard population status indicator.
- `modulates` → **[Nervous System](../../07-system/nervous-system/README.md)** — T3/T4 are obligatory for fetal and neonatal CNS myelination, hippocampal synaptogenesis, and cochlear development; severe maternal iodine deficiency causes cretinism — permanent, irreversible cognitive impairment and deafmutism.
- `modulates` → **[Cardiovascular System](../../07-system/cardiovascular-system/README.md)** — T3 increases heart rate (HCN4 upregulation), myocardial contractility (MHCα induction), and cardiac output; reduces peripheral vascular resistance; hypothyroidism → bradycardia; hyperthyroidism → tachycardia and AF risk.
- `connects-to` → **[Selenium](../selenium/README.md)** — DIO1/2/3 deiodinases (selenocysteine active site) catalyse T4→T3 activation and T3/T4 inactivation; GPx and TrxR neutralise DUOX2-generated H₂O₂ in the thyroid; combined I+Se deficiency causes myxoedematous cretinism.
- `connects-to` → **[Thyroid](../../06-organ/thyroid/README.md)** — NIS (SLC5A5) concentrates I⁻ 20–40-fold into follicular cells; TPO organifies iodide onto thyroglobulin tyrosines and couples MIT/DIT to form T4/T3; the thyroid stores 70–80% of total body iodine; TSH drives NIS expression.
- `connects-to` → **[Thyroid Hormones](../../03-molecular/thyroid-hormones/README.md)** — T4 contains 4 iodine atoms (65% of MW 777 Da), T3 contains 3; iodine is the rate-limiting substrate for synthesis; DIO1/2 deiodinate T4→T3 peripherally; ¹³¹I (t½=8 d) exploits NIS for targeted thyroid ablation.

## Pathology

### Iodine Deficiency Disorders (IDDs)

| Condition | Population | Mechanism | Features |
|:---|:---|:---|:---|
| **Simple goitre** | Any age | TSH-driven thyroid hypertrophy compensating for reduced T4/T3 | Enlarged, non-tender thyroid; euthyroid initially |
| **Hypothyroidism** | Adults | Prolonged iodine deficiency → insufficient T3/T4 despite TSH elevation | Fatigue, cold intolerance, weight gain, bradycardia, constipation, myxoedema |
| **Endemic cretinism (neurological)** | Fetus/neonate | Severe maternal + fetal iodine deficiency during critical CNS developmental window | Profound intellectual disability, deafmutism, spastic diplegia; partially preventable if supplementation starts before conception |
| **Endemic cretinism (myxoedematous)** | Infants in Se-deficient areas | Iodine + selenium deficiency → hypothyroidism + stunting | Stunted growth, intellectual disability, less neurological damage |
| **Subclinical hypothyroidism** | Adults | Marginal iodine deficiency; TSH elevated, fT4 normal | Often asymptomatic; possible subtle effects on cognition, cardiovascular risk |

### Iodine Excess Disorders

| Condition | Cause | Mechanism | Features |
|:---|:---|:---|:---|
| **Wolff-Chaikoff hypothyroidism** | Amiodarone, povidone-iodine, CT contrast | Failure to escape Wolff-Chaikoff block | Hypothyroidism; usually transient |
| **Jod-Basedow hyperthyroidism** | Iodine repletion in endemic areas or multinodular goitre | Autonomous nodules synthesise T3/T4 unrestricted | Thyrotoxicosis after iodine supplementation |
| **Thyroid cancer (papillary)** | ¹³¹I exposure (Chernobyl) | Radiation mutagenesis (RET/PTC rearrangements) | Most common thyroid malignancy; excellent prognosis; treated with surgery ± ¹³¹I ablation |

### Clinical Use of Radioiodine

**¹³¹I (t½ = 8.02 days)** is selectively taken up by thyroid follicular cells via NIS and emits beta particles that ablate thyroid tissue within a 1–2 mm radius. Applications include:
- Treatment of Graves disease (hyperthyroidism) — renders the patient permanently hypothyroid in a single dose
- Ablation of residual thyroid tissue after thyroidectomy for differentiated thyroid cancer
- Treatment of metastatic differentiated thyroid cancer (DTC) where the metastases retain NIS expression

**¹²³I** (pure gamma emitter) is used for thyroid scintigraphy (imaging nodule function) without ablation.

## See Also

- [Nervous system](../../07-system/nervous-system/README.md) — T3/T4-dependent CNS development.
- [Cardiovascular system](../../07-system/cardiovascular-system/README.md) — thyroid hormone regulation of cardiac function.
- [Selenium](../../02-atomic/selenium/README.md) — deiodinases DIO1–3 are selenoproteins; selenium and iodine deficiency interact to cause myxoedematous cretinism.

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [elsevier.com](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
[^bizhanova-kopp-nis]: Bizhanova A, Kopp P. Minireview: The sodium-iodide symporter NIS and pendrin in iodide homeostasis of the thyroid. *Endocrinology.* 2009;150(3):1084-90. [doi:10.1210/en.2008-1437](https://doi.org/10.1210/en.2008-1437) · [PubMed 19196800](https://pubmed.ncbi.nlm.nih.gov/19196800/)
[^zimmermann-iodine-deficiency]: Zimmermann MB, Boelaert K. Iodine deficiency and thyroid disorders. *Lancet Diabetes Endocrinol.* 2015;3(4):286-95. [doi:10.1016/S2213-8587(14)70225-6](https://doi.org/10.1016/S2213-8587(14)70225-6) · [PubMed 25591468](https://pubmed.ncbi.nlm.nih.gov/25591468/)

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
