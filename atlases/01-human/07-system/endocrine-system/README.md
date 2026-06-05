---
schema: human-scale-entry/v1
id: endocrine-system
name: Endocrine System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-05
summary: "Network of glands releasing hormones into blood to regulate metabolism, growth, reproduction, stress, and water balance. Integrates nervous and immune systems via hypothalamic-pituitary axes (HPA, HPT, HPG). Encompasses peptide, steroid, and tyrosine-derived hormone classes."
aliases: ["hormonal system", "endocrine glands", "HPA axis", "HPT axis", "HPG axis"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/pancreas
    relation: contains
    note: "Pancreatic islets of Langerhans (insulin [β-cells], glucagon [α-cells], somatostatin [δ-cells]) are central glucose regulators; T1DM = autoimmune β-cell destruction; T2DM = insulin resistance + progressive β-cell failure."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Hypothalamus integrates nervous and endocrine systems; CRH, TRH, GnRH, GHRH control anterior pituitary; AVP and oxytocin store in posterior pituitary; glucocorticoids, thyroid hormones, and sex steroids feed back to regulate CNS and behaviour."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Cortisol, oestrogens, and androgens regulate immune cell trafficking, cytokine production, and lymphocyte apoptosis; HPA-axis cortisol → immunosuppression; thymic involution driven by sex steroids reduces T-cell output with age."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "ANP/BNP (heart), aldosterone (adrenal), ADH (posterior pituitary), EPO (kidney), and catecholamines (adrenal medulla) together regulate blood pressure, volume, and cardiac output; hyperthyroidism, Cushing's, and phaeochromocytoma cause CVD."
---

# Endocrine System

## Overview

The endocrine system is the body's long-range chemical communication network — a distributed collection of specialised secretory cells, tissues, and glands that synthesise and release **hormones** (from Greek *hormao* — to set in motion) directly into the bloodstream, enabling the regulation of distant target organs and tissues [^guyton-hall]. This distinguishes endocrine signalling (blood-borne, systemic, acting minutes to hours) from:
- **Paracrine signalling** — local mediators acting on adjacent cells (prostaglandins, NO, histamine)
- **Autocrine signalling** — cell acts on itself
- **Exocrine secretion** — secreted via ducts to body surfaces (saliva, pancreatic enzymes, bile)
- **Neurotransmitter signalling** — rapid, point-to-point (milliseconds), synaptic cleft

The endocrine system regulates virtually every physiological process: **metabolism** (thyroid hormones, insulin, glucagon, cortisol), **growth and development** (GH, IGF-1, thyroid hormones, sex steroids), **reproduction** (LH, FSH, oestrogen, progesterone, testosterone), **stress response** (cortisol, epinephrine, norepinephrine), **water and electrolyte balance** (ADH/vasopressin, aldosterone, ANP, PTH), and **circadian rhythms** (melatonin, cortisol diurnal cycle) [^stryer-biochemistry].

Critically, the endocrine system does not operate in isolation. It is deeply integrated with:
- **The nervous system** (neuroendocrine integration: hypothalamus is both a brain region and the apex of endocrine axes; autonomic nerves directly control adrenal medulla)
- **The immune system** (immunoendocrine crosstalk: glucocorticoids suppress inflammation; cytokines IL-1β and IL-6 activate the HPA axis; thymus produces thymic hormones; sex steroids modulate immune cell trafficking)
- **The cardiovascular and renal systems** (RAAS — renin-angiotensin-aldosterone system; ANP/BNP; EPO; ADH)

## Structure

### Major Endocrine Glands and Their Hormones

#### Hypothalamus

The hypothalamus is the neuroendocrine master controller, receiving neural inputs from limbic cortex, brainstem, retina, and peripheral sensors, and translating them into peptide hormone outputs [^guyton-hall]:

| Hypothalamic hormone | Target | Effect |
|:---|:---|:---|
| CRH (corticotropin-releasing hormone) | Anterior pituitary | ↑ ACTH release |
| TRH (thyrotropin-releasing hormone) | Anterior pituitary | ↑ TSH release |
| GnRH (gonadotropin-releasing hormone) | Anterior pituitary | ↑ LH and FSH release (pulsatile) |
| GHRH (GH-releasing hormone) | Anterior pituitary | ↑ GH release |
| Somatostatin (SST/SRIF) | Anterior pituitary, pancreas | ↓ GH, TSH, insulin, glucagon |
| Dopamine (DA) | Anterior pituitary | ↓ Prolactin |
| ADH/Vasopressin (AVP) | Posterior pituitary (storage), kidney | ↑ Water reabsorption (V2R → AQP2) |
| Oxytocin | Posterior pituitary (storage), uterus, breast | Uterine contraction, milk letdown, bonding |

Parvocellular neuroendocrine neurons in the paraventricular nucleus (PVN) and arcuate nucleus project to the median eminence → release into the hypophyseal portal system → reach the anterior pituitary. Magnocellular neurons (PVN + supraoptic nucleus) project axons directly to the posterior pituitary neurohaemal region → store and release AVP and OXT.

#### Anterior Pituitary (Adenohypophysis)

Six main cell types and their hormones [^guyton-hall]:

| Cell type | Hormone | Primary targets and effects |
|:---|:---|:---|
| Somatotroph (50%) | GH (growth hormone) | Liver (IGF-1 production), bone (long bone growth), adipose (lipolysis), muscle (protein synthesis) |
| Corticotroph (20%) | ACTH (adrenocorticotropin) | Adrenal cortex → cortisol and DHEA |
| Thyrotroph (5%) | TSH (thyroid-stimulating hormone) | Thyroid → T3 and T4 synthesis and secretion |
| Gonadotroph (10%) | LH, FSH | Gonads → steroid and gamete production |
| Lactotroph (15%) | Prolactin | Breast → lactation; reproductive axis suppression |
| Melanotroph | MSH (α-MSH) | Melanocytes → pigmentation; MC4R in hypothalamus → satiety |

#### Posterior Pituitary (Neurohypophysis)

Not a true gland — a storage and release site for AVP and oxytocin synthesised in hypothalamic magnocellular neurons and transported down axons [^guyton-hall].

| Hormone | Stimuli | Effects |
|:---|:---|:---|
| ADH/AVP | ↑plasma osmolarity (>285 mOsm/kg), ↓blood volume, pain, nausea | V2R on collecting duct → cAMP → AQP2 insertion → water reabsorption; V1aR on VSM → vasoconstriction |
| Oxytocin | Cervical stretch (Ferguson reflex), suckling | Uterine contraction (positive feedback with PGE2); myoepithelial cell contraction → milk ejection; CNS: pair bonding, trust, social behaviour |

#### Thyroid Gland

Follicular cells synthesise T3 (3,5,3'-triiodothyronine — the active form) and T4 (thyroxine — prohormone, 99.97% protein-bound [TBG, albumin, transthyretin]); peripheral tissues convert T4 → T3 via iodothyronine deiodinases (D1/D2/D3) [^stryer-biochemistry].

Synthesis: dietary iodide → thyroid → NIS (Na+/I- symporter) uptake → oxidised by TPO → organification of thyroglobulin (iodination of Tyr residues → MIT, DIT → T3, T4) → colloid storage → TSH → pinocytosis → lysosomal proteolysis → T3/T4 secretion.

Parafollicular C-cells: calcitonin (↓serum Ca²⁺ by inhibiting osteoclasts; marker for medullary thyroid carcinoma).

Thyroid hormone actions (via nuclear receptor TR-α/β → gene transcription):
- ↑ BMR (↑Na⁺/K⁺-ATPase expression, ↑mitochondrial uncoupling, ↑β-oxidation)
- ↑ Cardiac output (↑heart rate, ↑contractility, ↑CO)
- ↑ GI motility; ↑bone turnover; ↑catecholamine sensitivity
- CNS maturation (critical in fetal/neonatal period — deficiency → cretinism)

#### Parathyroid Glands (×4)

Chief cells secrete PTH (parathyroid hormone) in response to ↓[Ca²⁺] sensed by calcium-sensing receptor (CaSR on parathyroid cell membrane) [^guyton-hall]:
- **Bone:** PTH → osteoblast RANKL → osteoclast activation → bone resorption → ↑Ca²⁺, ↑Pi (paradoxically — intermittent PTH is anabolic: teriparatide)
- **Kidney (DCT/collecting duct):** ↑Ca²⁺ reabsorption (TRPV5), ↑phosphate excretion (↓NaPi IIa/IIc), ↑1α-hydroxylase → ↑1,25-VitD synthesis
- **Gut (indirect):** via ↑1,25-VitD → ↑Ca²⁺ absorption (TRPV6 + calbindin)

#### Adrenal Glands

**Adrenal cortex** (three zones) [^stryer-biochemistry]:
- *Zona glomerulosa* (outermost): Aldosterone (mineralocorticoid) — regulated by angiotensin II and K⁺, NOT by ACTH. Actions: ↑Na⁺ reabsorption (ENaC), ↑K⁺ and H⁺ secretion in collecting duct (principal cells). Net: ↑blood volume, ↑blood pressure.
- *Zona fasciculata* (middle): Cortisol (glucocorticoid) — regulated by ACTH. Actions: ↑gluconeogenesis + ↑proteolysis + ↑lipolysis (peripheral) = ↑blood glucose; anti-inflammatory (↓NF-κB, ↓COX-2, ↓cytokines); permissive for catecholamine action; ↑PHMT (epinephrine synthesis in medulla). Negative feedback to hypothalamus (↓CRH) and pituitary (↓ACTH).
- *Zona reticularis* (inner): DHEA/DHEAS (weak androgens) → converted peripherally to testosterone and oestradiol; regulated by ACTH; important for adrenarche (pubic/axillary hair) and post-menopausal oestrogen.

**Adrenal medulla** (chromaffin cells — modified postganglionic sympathetic neurons): Epinephrine (Epi, ~80%) and norepinephrine (NE, ~20%) released en masse via preganglionic sympathetic ACh → nicotinic receptor → catecholamine secretion. Actions: ↑HR, ↑CO, ↑bronchodilation (β2), ↑glycogenolysis, ↑lipolysis, ↑sweating, ↑alertness [^guyton-hall].

#### Pancreatic Islets of Langerhans

~1 million islets (~2% of pancreatic mass) scattered within exocrine pancreas [^stryer-biochemistry]:

| Cell type | Hormone | Stimulus | Effect |
|:---|:---|:---|:---|
| β-cells (~70%) | Insulin | ↑glucose (GLUT2 → glucokinase → ATP/K+ channel closure → depolarisation → Ca²⁺ → exocytosis); amino acids; GLP-1, GIP (incretins) | ↓blood glucose (↑GLUT4 in muscle/fat, ↑glycogen synthesis, ↑glycolysis, ↑lipogenesis, ↓gluconeogenesis) |
| α-cells (~20%) | Glucagon | ↓glucose; amino acids; sympathetic NS | ↑blood glucose (↑hepatic glycogenolysis, ↑gluconeogenesis) |
| δ-cells (~5%) | Somatostatin | ↑glucose, ↑amino acids | Paracrine ↓insulin and glucagon secretion |
| γ-cells (<5%) | Pancreatic polypeptide (PP) | Meals, fasting | ↓pancreatic exocrine secretion, ↓appetite |
| ε-cells (<1%) | Ghrelin | Fasting | ↑appetite (hypothalamic NPY/AgRP) |

#### Gonads

**Testes:** Leydig cells → testosterone (LH-stimulated → CYP17A1/CYP11A1 pathway from cholesterol); Sertoli cells → inhibin B (suppresses FSH), AMH (Müllerian inhibiting substance), activin, oestradiol (from aromatase). Testosterone: male secondary sexual characteristics, spermatogenesis (high intratesticular concentration via Sertoli SHBG), anabolism, bone mineralisation, erythropoiesis (↑EPO), CNS (aggression, libido, spatial cognition).

**Ovaries:** Granulosa cells → oestradiol (FSH-stimulated, aromatase) → endometrial proliferation, vaginal epithelium, breast development, positive feedback on LH surge (mid-cycle). Luteal corpus luteum → progesterone (LH-stimulated) → endometrial secretory phase, decidualisation, thermogenesis. Granulosa/theca → inhibin A, activin, AMH (follicle reserve marker).

#### Other Endocrine Sources

| Gland/Tissue | Hormone | Function |
|:---|:---|:---|
| Pineal gland | Melatonin (from serotonin, light-suppressed) | Circadian entrainment; sleep onset signal |
| Thymus | Thymosin α1, thymulin | T-cell maturation; declines with age (thymic involution) |
| Adipose tissue | Leptin (adiponectin, resistin) | Leptin: hypothalamic satiety (JAK2/STAT3 → ↓NPY/AgRP, ↑POMC); adiponectin: ↑insulin sensitivity (AMPK) |
| Heart | ANP, BNP | ↓Na⁺ reabsorption (inhibit ENaC, RAAS), ↓preload, ↑GFR |
| Kidney | EPO (juxta-glomerular cells), 1,25-VitD, Renin | EPO: ↑RBC production; Renin: RAAS cascade → Ang II → aldosterone → ↑BP/volume |
| GI tract | GLP-1, GIP (incretins); Gastrin; CCK; Secretin; GIP; PYY; Ghrelin (stomach) | Incretin effect (↑insulin post-meal); digestion coordination; appetite regulation |
| Liver | IGF-1 (GH-stimulated), angiotensinogen, thrombopoietin, hepcidin, FGF21 | Growth mediation; RAAS precursor; platelet production; iron regulation |

### Hormone Chemistry and Receptor Mechanisms

**Peptide/protein hormones** (water-soluble; cannot cross cell membranes; membrane receptors): insulin, GH, PTH, LH, FSH, glucagon, prolactin, ACTH, ADH, oxytocin, GLP-1, leptin. Receptors: GPCRs (→ cAMP, IP3/Ca²⁺, DAG/PKC), RTKs (insulin → IR/IRS-1→PI3K→Akt; GH → JAK2→STAT5), cytokine receptors. Rapid onset (seconds to minutes) via second messenger cascades [^stryer-biochemistry].

**Steroid hormones** (lipophilic; derived from cholesterol; freely cross cell membranes; nuclear/cytoplasmic receptors): cortisol (GR), aldosterone (MR), testosterone (AR), oestradiol (ERα/ERβ), progesterone (PR), calcitriol/1,25-VitD (VDR), DHEA. Nuclear receptor superfamily: ligand-binding domain + zinc-finger DNA-binding domain + AF-2 transactivation domain → bind GREs (glucocorticoid response elements) or HREs → gene transcription (hours to days). Also rapid non-genomic signalling via membrane-associated steroid receptors [^stryer-biochemistry].

**Tyrosine-derived hormones:** Catecholamines (dopamine, NE, epinephrine — synthesised from Tyr → DOPA → dopamine → NE → Epi; water-soluble → membrane receptors [α/β-adrenergic GPCRs]). Thyroid hormones (T3/T4 — iodinated Tyr residues on thyroglobulin; lipophilic → nuclear receptors TRα/TRβ; major genomic effects) [^guyton-hall].

**Gaseous mediators:** NO (eNOS/nNOS/iNOS — from Arg; → sGC → cGMP → vasodilation), CO (HO-1/2 — from haem → cGMP), H₂S (CSE/CBS — paracrine mediators).

## Function

### Feedback Regulation

Most endocrine axes operate under **negative feedback** — the classical servo-control mechanism preventing hormone excess [^guyton-hall]:

- **HPA axis:** Stressor → hypothalamus CRH → anterior pituitary ACTH → adrenal cortex cortisol → cortisol feeds back to hypothalamus (↓CRH) and pituitary (↓ACTH). Long-loop negative feedback; short-loop feedback (ACTH → hypothalamus); ultra-short-loop (CRH → CRH neurons).
- **HPT axis:** TRH → TSH → T3/T4 → T3 (more potent) feeds back to pituitary (↓TSH) and hypothalamus (↓TRH).
- **RAAS:** ↓BP/↓Na⁺/↑renal sympathetics → renin (JGA) → Ang I → ACE (lung) → Ang II → aldosterone → ↑Na⁺ reabsorption → ↑blood volume → ↑BP → ↓renin.
- **Calcium homeostasis:** ↓Ca²⁺ → CaSR on parathyroid → ↑PTH → ↑Ca²⁺ (bone, kidney, gut) → ↑Ca²⁺ → CaSR → ↓PTH.

**Positive feedback** (uncommon; amplifies a deviation rather than correcting it): Mid-cycle LH surge — rising oestradiol (day 12) → switches pituitary gonadotrophs from negative to positive feedback → massive LH surge → ovulation. Oxytocin + cervical distension (Ferguson reflex) → more oxytocin → more contractions → more distension (until delivery breaks the loop).

**Circadian and ultradian rhythms:** Cortisol peaks at 06:00–08:00 (driven by CRH/ACTH pulse amplitude), nadir ~00:00; GH secreted in pulses (especially first hour of slow-wave sleep); LH/FSH pulsatile (GnRH pulse frequency: every 60–90 min follicular phase; every 3–4 h luteal phase); melatonin rises at dusk (~21:00) under dim light conditions, peaks 02:00–03:00, suppressed by light [^guyton-hall].

**Permissive effects:** Cortisol is permissive for catecholamine responsiveness (upregulates β-adrenergic receptor expression and sensitises vascular smooth muscle) — explains why Addisonian patients are poorly responsive to pressor agents. T3 is permissive for GH secretion and normal growth.

### Metabolic Coordination

The endocrine system coordinates fuel metabolism across multiple organs in response to feeding and fasting [^stryer-biochemistry]:

**Fed state (post-prandial):** ↑blood glucose → ↑insulin secretion (β-cells) + GLP-1 (incretin, L-cells in ileum) → insulin: ↑GLUT4 in muscle and adipose (→ glucose uptake), ↑glycogen synthesis (muscle + liver), ↓hepatic gluconeogenesis, ↑lipogenesis (adipose), ↓lipolysis, ↑protein synthesis.

**Fasted state:** ↓blood glucose → ↓insulin, ↑glucagon (α-cells) → glucagon: ↑hepatic glycogenolysis (PKA → phosphorylase kinase → glycogen phosphorylase), ↑gluconeogenesis (↑PEPCK, ↑FBPase), ↑lipolysis in adipose (PKA → HSL) → ↑FFA → hepatic β-oxidation → ketogenesis. After 12–16 h: GH + cortisol amplify lipolysis and gluconeogenesis.

**Stress response:** CRH → ACTH → cortisol + sympathetic → epinephrine → combined: ↑blood glucose, ↑cardiac output, ↑bronchodilation, ↑alertness, ↑pain threshold — the "fight-or-flight" + HPA arm of stress physiology.

## Connections

- **Contains:** [pancreas](../../06-organ/pancreas/README.md) — islets of Langerhans (insulin, glucagon, somatostatin) are the central regulators of glucose homeostasis.
- **Modulates:** [nervous-system](../nervous-system/README.md) — hypothalamus integrates neural and endocrine signals; glucocorticoids, thyroid hormones, and sex steroids modulate CNS function, mood, and cognition.
- **Modulates:** [immune-system](../immune-system/README.md) — cortisol (HPA axis), sex steroids (gonadal/adrenal), and thymic hormones regulate immunity; stress-driven cortisol suppresses inflammation; thymic involution reduces T-cell output.
- **Modulates:** [cardiovascular-system](../cardiovascular-system/README.md) — ANP/BNP, aldosterone, ADH, EPO, and catecholamines regulate blood pressure, blood volume, and cardiac output; endocrine pathology (hyperthyroidism, Cushing's, phaeochromocytoma) causes secondary CVD.

## Pathology

### Diabetes Mellitus

The most prevalent endocrine disorder globally [^guyton-hall]:

**Type 1 DM (T1DM):** Autoimmune destruction of pancreatic β-cells (CD8+ CTL-mediated, Th1-driven; HLA-DR4/DQ8 association) → absolute insulin deficiency → hyperglycaemia + ketoacidosis (DKA). Requires exogenous insulin. Complications: retinopathy (non-proliferative → proliferative, tractional RD), nephropathy (Kimmelstiel-Wilson nodular glomerulosclerosis), peripheral neuropathy (stocking-glove), autonomic neuropathy, accelerated CVD.

**Type 2 DM (T2DM):** Peripheral insulin resistance (↓IRS-1/PI3K/Akt signalling in muscle and liver; ↑FFA → DAG → PKC-ε → inhibits IR kinase) → compensatory ↑insulin → progressive β-cell failure (ER stress, glucolipotoxicity, IL-1β-mediated apoptosis, islet amyloid [IAPP]) → absolute insulin deficiency (late stage). Strongly linked to obesity, sedentary lifestyle, metabolic syndrome.

**Treatment targets:** insulin resistance (metformin/AMPK → ↑GLUT4; pioglitazone/PPARγ); β-cell stimulation (sulfonylureas → KATP closure); GLP-1 receptor agonists (semaglutide, liraglutide → ↑insulin, ↓glucagon, ↓appetite, ↓weight); SGLT2 inhibitors (empagliflozin → ↑urinary glucose excretion → ↓blood glucose, ↑diuresis, cardioprotection) [^stryer-biochemistry].

### Thyroid Disorders

**Hypothyroidism:** Most common cause — Hashimoto's thyroiditis (autoimmune — anti-TPO and anti-thyroglobulin antibodies → lymphocytic infiltration → Hürthle cell metaplasia → gland destruction → ↓T3/T4 → ↑TSH). Clinical: fatigue, weight gain, cold intolerance, constipation, bradycardia, depression, myxoedema. Treatment: levothyroxine (L-T4).

**Hyperthyroidism:** Graves' disease (TSI/TSAb — thyroid-stimulating immunoglobulins, IgG activating TSH receptor → autonomous thyroid hormone synthesis → ↓TSH [suppressed], ↑FT4, ↑FT3). Clinical: weight loss, heat intolerance, tremor, palpitations, exophthalmos (orbital GAG accumulation), pretibial myxoedema, onycholysis. Treatment: antithyroids (methimazole/PTU), radioiodine (I-131), thyroidectomy.

### Adrenal Disorders

**Addison's disease (primary adrenal insufficiency):** Autoimmune (anti-21-hydroxylase antibodies) → adrenal cortical destruction → ↓cortisol + ↓aldosterone → hypotension, hyponatraemia, hyperkalaemia, hyperpigmentation (↑ACTH → ↑α-MSH via POMC cleavage → melanocyte MC1R). Life-threatening adrenal crisis (hypotension, vomiting, collapse) on stress. Treatment: hydrocortisone + fludrocortisone [^guyton-hall].

**Cushing's syndrome:** Excess cortisol. Causes: Cushing's disease (pituitary ACTH-secreting adenoma — ~70%), ectopic ACTH (small cell lung cancer, carcinoid — ~10%), adrenal adenoma/carcinoma (~20%), iatrogenic (glucocorticoid therapy — most common). Features: central obesity (visceral fat ↑), moon face, buffalo hump, striae, skin thinning, hypertension, osteoporosis, insulin resistance, immune suppression, proximal myopathy, psychiatric disturbance.

**Phaeochromocytoma:** Chromaffin cell tumour of adrenal medulla (or paraganglioma if extra-adrenal) → paroxysmal catecholamine secretion → hypertensive crisis, headache, sweating, palpitations ("rule of 10s": 10% malignant, 10% bilateral, 10% extra-adrenal, 10% in children, 10% familial). Associated with MEN2A/2B (RET mutation), VHL (von Hippel-Lindau), NF1 (neurofibromatosis), SDH mutations. Diagnosis: plasma metanephrines + 24h urine catecholamines [^guyton-hall].

### Pituitary Adenomas

Benign pituitary tumours (~10% prevalence on MRI):
- **Prolactinoma** (most common, 40%): hyperprolactinaemia → amenorrhoea, galactorrhoea (women); hypogonadism, erectile dysfunction (men); ↓GnRH pulsatility via TIDA neurons. Treatment: dopamine agonists (cabergoline, bromocriptine — dopamine = physiological prolactin inhibitor).
- **GH-secreting adenoma** (15–20%): acromegaly (in adults — enlarged hands, feet, jaw, soft tissue; ↑IGF-1; ↑glucose; cardiovascular complications; sleep apnoea); gigantism (in children — linear growth before epiphyseal fusion).
- **ACTH-secreting adenoma** (Cushing's disease, 10–15%): see above.
- **Non-functioning adenomas** (30–40%): mass effects (bitemporal hemianopia via optic chiasm compression; hypopituitarism from pituitary stalk compression).

### Multiple Endocrine Neoplasia (MEN) Syndromes

Autosomal dominant cancer predisposition syndromes [^guyton-hall]:

| Syndrome | Gene | Tumours |
|:---|:---|:---|
| MEN1 | MEN1 (menin — tumour suppressor) | Parathyroid adenomas (>95%), pituitary adenomas (prolactinoma common), pancreatic NETs (gastrinoma/Zollinger-Ellison, insulinoma, VIPoma) |
| MEN2A | RET (gain-of-function — codon 634) | Medullary thyroid carcinoma (MTC; 95%), phaeochromocytoma (50%), primary hyperparathyroidism (25%) |
| MEN2B | RET (codon 918) | MTC (aggressive, early), phaeochromocytoma, marfanoid habitus, mucosal neuromas, ganglioneuromatosis of GI tract |
| MEN4 | CDKN1B (p27) | Similar to MEN1 but RET/MEN1 mutation-negative |

### Metabolic Syndrome

Cluster of insulin resistance-driven metabolic abnormalities (WHO/NCEP-ATP III criteria: central obesity [waist >102 cm M, >88 cm F] + ≥2 of: TG ≥1.7 mmol/L; HDL <1.0/1.3 mmol/L; BP ≥130/85; fasting glucose ≥5.6 mmol/L) [^stryer-biochemistry]. Underlying mechanism: visceral adipose tissue ↑FFA + ↑TNF-α + ↓adiponectin → hepatic/peripheral insulin resistance → hyperinsulinaemia → dyslipidaemia (↑VLDL, ↓HDL, ↑small dense LDL) + hypertension (↑RAAS + SNS) + T2DM risk. Strongly predicts T2DM, cardiovascular disease, NAFLD, PCOS, sleep apnoea, and certain cancers.

## See Also

- [pancreas](../../06-organ/pancreas/README.md)
- [liver](../../06-organ/liver/README.md)
- [thymus](../../06-organ/thymus/README.md)
- [nervous-system](../nervous-system/README.md)
- [immune-system](../immune-system/README.md)
- [cardiovascular-system](../cardiovascular-system/README.md)
- [renal-system](../renal-system/README.md)
- [insulin](../../03-molecular/insulin/README.md)
- [cortisol](../../03-molecular/cortisol/README.md)
- [glucocorticoid-receptor](../../03-molecular/glucocorticoid-receptor/README.md)
- [dopamine](../../03-molecular/dopamine/README.md)

---

> **AI co-maintenance notice:** This entry is maintained with AI assistance. Content reflects standard textbook and peer-reviewed sources as cited; verify critical details against primary literature before clinical or research application.

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [Publisher →](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [Publisher →](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
