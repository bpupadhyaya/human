---
schema: human-scale-entry/v1
id: pheochromocytoma-paraganglioma
name: Pheochromocytoma/Paraganglioma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Pheochromocytoma/paraganglioma are chromaffin cell tumors; ~40% hereditary (SDHx, VHL, RET, NF1); biochemical diagnosis: plasma/urine metanephrines; sunitinib (FIRSTMAPPP) and 177Lu-DOTATATE for metastatic disease; alpha-adrenergic blockade mandatory preoperatively."
aliases: ["pheochromocytoma", "paraganglioma", "PHEO", "PGL", "PHEO/PGL", "chromaffin tumor", "hereditary paraganglioma", "catecholamine-secreting tumor", "adrenal pheochromocytoma", "head-neck paraganglioma", "SDHx tumor", "MEN2 pheochromocytoma"]
sources:
  - id: lenders-2014-pheo-guideline
    type: peer-reviewed
    cite: "Lenders JW, Duh QY, Eisenhofer G, et al. Pheochromocytoma and paraganglioma: an endocrine society clinical practice guideline. J Clin Endocrinol Metab. 2014;99(6):1915-1942."
    doi: "10.1210/jc.2014-1498"
    pmid: "24893135"
    url: "https://doi.org/10.1210/jc.2014-1498"
  - id: baudin-2021-firstmappp-sunitinib
    type: peer-reviewed
    cite: "Baudin E, Goichot B, Berruti A, et al. First International Randomized Study in Malignant Progressive Pheochromocytoma and Paragangliomas (FIRSTMAPPP). Ann Oncol. 2021;32(10):1245-1254."
    doi: "10.1016/j.annonc.2021.07.009"
    pmid: "34246769"
    url: "https://doi.org/10.1016/j.annonc.2021.07.009"
cross_links:
  - target: 01-human/03-molecular/sdhb
    relation: connects-to
    note: "Hereditary PHEO/PGL caused by SDHB biallelic LOF → PGL4 syndrome; SDHB germline carriers: ~30-40% develop malignant PHEO/PGL (vs <5% SDHD/SDHC); highest malignant risk of all SDHx loci; SDHB IHC (granular cytoplasmic staining) used for initial SDH-deficient tumor screening."
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "VHL-mutant PHEO/PGL: Cluster 1 pseudohypoxia; bilateral PHEO in ~10-20% VHL patients; VHL type 2C (missense): PHEO-only phenotype; VHL-mutant PHEO is predominantly norepinephrine-secreting; sunitinib active in VHL-mutant metastatic PHEO/PGL; 68Ga-DOTATATE PET for staging."
  - target: 01-human/03-molecular/ret
    relation: connects-to
    note: "RET mutations in PHEO/PGL: Cluster 2 kinase signaling; RET M918T (MEN2B, most aggressive) or C634F/Y (MEN2A) → PHEO in ~40-50% MEN2A/B; epinephrine-predominant secretion; bilateral adrenal PHEO; prophylactic adrenalectomy in MEN2B; vandetanib/cabozantinib active in MTC."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "PHEO/PGL Cluster 1 (SDHx, VHL) activate HIF-1α by pseudohypoxia → VEGF, GLUT1 transcription; HIF-1α drives tumor angiogenesis; HIF-1α target expression predicts malignant behavior; 18F-FDG PET avidity in SDHB-mutant PHEO correlates with HIF-1α-driven metabolic reprogramming."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Pheochromocytomas arise in the adrenal medulla from chromaffin cells, pouring epinephrine and norepinephrine into the adrenal vein; surgery demands 10-14 days of alpha-adrenergic blockade first (beta only after) to prevent intraoperative hypertensive crisis."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Neurofibromatosis type 1 is a Cluster 2 (kinase-signaling) hereditary pheochromocytoma syndrome: ~3-4% of NF1 patients develop adrenal, epinephrine-secreting PHEO; loss of neurofibromin's RAS-GAP activity drives the chromaffin tumor, paralleling RET-driven MEN2 PHEO."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Chromaffin tumors synthesize epinephrine and norepinephrine but are best detected by their continuously produced O-methylated metabolites — plasma free metanephrines (~97-99% sensitive); paroxysmal catecholamine surges cause episodic hypertension, palpitations, and headache."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Pheochromocytoma/paraganglioma and clear-cell RCC are linked by pseudohypoxia: VHL loss (and SDHx/FH defects) stabilizes HIF-2α even in normoxia, driving VEGF and a hypervascular tumor in both; VHL disease produces them together, and HIF-2α inhibitors like belzutifan treat both."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "VHL disease is a leading hereditary cause of pheochromocytoma/paraganglioma: germline VHL loss drives Cluster-1 pseudohypoxia, producing bilateral, often norepinephrine-secreting PHEO in 10-20% alongside clear-cell RCC — so young or bilateral PHEO warrants VHL testing."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Pheochromocytoma/paraganglioma and neuroblastoma are both neural-crest, catecholamine-handling sympathoadrenal tumors that take up MIBG and secrete catecholamine metabolites, but PPGL is an adult chromaffin tumor while neuroblastoma is an aggressive embryonal cancer of children."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Pheochromocytoma is the classic curable secondary cause of hypertension: episodic catecholamine release produces the paroxysmal triad of headache, palpitations, and sweating with severe spikes, so resistant or paroxysmal hypertension warrants plasma/urine metanephrine screening."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Paragangliomas appear in Carney-related syndromes—but not Carney complex itself: the SDH-deficient Carney triad (paraganglioma, gastric GIST, pulmonary chondroma) and Carney-Stratakis dyad are distinct from PRKAR1A-driven Carney complex, a common point of confusion."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "Pheochromocytoma/paraganglioma and HLRCC share a pseudohypoxia mechanism: both belong to the TCA-cycle tumor family where SDH or FH loss accumulates succinate/fumarate, inhibits HIF prolyl-hydroxylases, and stabilizes HIF—rarely yielding FH-mutant PPGL itself."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Pheochromocytoma is defined by the catecholamines it secretes: chromaffin tumors release norepinephrine and epinephrine, driving paroxysmal hypertension, while their breakdown products are the diagnostic test—an unregulated norepinephrine factory."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Pheochromocytoma is the organic disease that most convincingly mimics panic disorder: surges of catecholamines cause sudden palpitations and a sense of doom identical to a panic attack, so atypical 'panic' with hypertension warrants metanephrine testing."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "Paraganglioma and GIST are joined in Carney triad: SDH-deficient tumors—paragangliomas plus wild-type GISTs—arise together when succinate dehydrogenase loss drives pseudohypoxia, so finding one SDH-deficient tumor prompts a search for the other."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1 is one of several genes causing hereditary pheochromocytoma: neurofibromin loss (like RET, VHL and SDH mutations) predisposes to catecholamine-secreting tumors, so a pheochromocytoma should prompt genetic testing—up to a third are hereditary."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Pheochromocytoma can devastate the heart: catecholamine surges cause hypertensive crises, arrhythmias and a stress (Takotsubo) cardiomyopathy, so the tumor's adrenaline output threatens the heart—and alpha-blockade before surgery prevents catastrophic crises."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "Pheochromocytoma belongs to MEN2, not MEN1: it arises with medullary thyroid cancer in RET-driven MEN2, whereas MEN1 (menin) causes parathyroid, pituitary and pancreatic tumors—so the two MEN syndromes are distinguished partly by whether pheochromocytoma occurs."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Pheochromocytoma is a cardiovascular emergency in waiting: surges of catecholamines cause paroxysmal hypertension, palpitations and arrhythmia, and can trigger catecholamine cardiomyopathy or crisis—so alpha-blockade before surgery is essential to prevent fatal swings."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Paragangliomas arise along the autonomic nervous system: these tumors grow in sympathetic and parasympathetic paraganglia (from adrenal medulla to carotid body), so they are neural-crest tumors of the nervous system that happen to flood the body with catecholamines."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Pheochromocytoma is a hormone-secreting tumor of the endocrine adrenal medulla: it autonomously pours catecholamines into blood, so it belongs among the functional endocrine tumors and clusters in syndromes (MEN2, VHL, NF1) with other endocrine neoplasia."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Pheochromocytoma and paraganglioma are imaged and treated with radioactive iodine via MIBG: these catecholamine-handling tumors take up I-123/I-131 metaiodobenzylguanidine, lighting them up on scans and delivering targeted radiation in metastatic disease."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Many paragangliomas express SSTR2, opening a second nuclear-medicine route: 68Ga-DOTATATE PET often detects SDHx-related and head-and-neck tumors better than MIBG, and 177Lu-DOTATATE delivers peptide receptor radiotherapy in metastatic cases."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Pheochromocytoma and paraganglioma spring from neural-crest lineage: the chromaffin and paraganglion cells share an origin with neurons of the sympathetic nervous system, which is why these tumors secrete catecholamines like nerve cells do."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Some pheochromocytomas and paragangliomas secrete dopamine: especially SDHB-driven head-and-neck tumors release dopamine and its metabolite 3-methoxytyramine, a biochemical signature that flags a hereditary, more malignant-prone tumor."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Pheochromocytoma-paraganglioma is tied to oxygen sensing: carotid-body paragangliomas are literal oxygen sensors, and SDH/VHL mutations fake low oxygen (pseudohypoxia), stabilizing HIF to drive the 'cluster 1' hereditary tumors."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Pheochromocytomas are intensely vascular through VEGF: pseudohypoxic HIF signaling pumps out VEGF, so these tumors are richly perfused and prone to bleeding—and anti-angiogenic drugs are tried against metastatic disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Pheochromocytomas dump catecholamines via calcium: chromaffin cells release adrenaline by calcium-triggered exocytosis, so the tumor's surges of hormone—and the spells of pounding blood pressure they cause—run on this calcium-dependent machinery."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages fill the pheochromocytoma's vascular stroma: drawn into the richly perfused, pseudohypoxic tumor, they support its blood supply and shape an immune niche of interest in the hard-to-treat metastatic disease."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Pheochromocytoma punishes the kidneys through catecholamines: the surges of adrenaline and noradrenaline drive severe hypertension that damages the kidney's vessels, and extra-adrenal paragangliomas can also arise near the renal hilum."
---

# Pheochromocytoma/Paraganglioma

## Overview

**Pheochromocytoma (PHEO)** and **paraganglioma (PGL)** are rare catecholamine-secreting neuroendocrine tumors arising from **chromaffin cells** (neural crest-derived, adrenergic-lineage cells). PHEO arises in the adrenal medulla; PGL arises from extra-adrenal paraganglia and is further classified as:
- **Sympathetic PGL**: extra-adrenal abdominal (organ of Zuckerkandl, periaortic), thoracic, pelvic, bladder; catecholamine-secreting; biochemically active
- **Parasympathetic/head-neck PGL (HNPGL)**: carotid body, jugulotympanic, vagal, laryngeal; predominantly non-secretory; located adjacent to parasympathetic ganglia

**Epidemiology:**
- Incidence: ~8-12 per million/year (combined PHEO + PGL); PHEO ~80-85% of chromaffin tumors; PGL ~15-20%
- Most are diagnosed at age 40-50 years; hereditary forms present earlier (20s-30s)
- ~40% are hereditary — the highest proportion of any human tumor type, exceeding even medullary thyroid carcinoma [^lenders-2014-pheo-guideline]
- "Rule of 10s" (historical, now outdated): 10% bilateral, 10% extra-adrenal, 10% malignant, 10% hereditary — modern genetics reveals all four proportions were underestimates

**Hereditary syndromes — genetic testing recommended for ALL patients at diagnosis:**

| Gene | Syndrome | PHEO/PGL type | Malignancy risk | Co-manifestations |
|---|---|---|---|---|
| SDHB | PGL4 | Sympathetic PGL > PHEO | ~30-40% | SDH-deficient GIST (rare) |
| SDHD | PGL1 | HNPGL (parasympathetic) | <5% | Paternal imprinting |
| SDHC | PGL3 | HNPGL | <5% | Low penetrance |
| SDHA | PGL5 | Mixed | ~7-10% | GIST, pituitary adenoma |
| VHL | VHL disease | Bilateral PHEO | <5% | Hemangioblastoma, ccRCC |
| RET | MEN2A/MEN2B | Bilateral adrenal PHEO | <5% | MTC, hyperparathyroidism |
| NF1 | Neurofibromatosis 1 | Adrenal PHEO | <5% | Café-au-lait, Lisch nodules |
| TMEM127 | — | Adrenal PHEO bilateral | Low | Rare |
| MAX | — | Bilateral adrenal PHEO | Low | Paternal imprinting |

## Structure

### Molecular cluster classification

Two major cluster subtypes with distinct biology, secretory profile, and malignancy risk:

**Cluster 1 — Pseudohypoxia/Krebs cycle:**
- Genes: SDHB, SDHD, SDHC, SDHA, SDHAF2 (SDHx), VHL, FH (fumarate hydratase), MDH2
- Mechanism: SDH or VHL LOF → HIF-1α stabilized (pseudohypoxia) → VEGF, GLUT1, EPO (SDHx) or direct VHL E3 ligase failure (VHL)
- Biochemistry: predominantly **norepinephrine-secreting** (or non-secretory in HNPGL)
- Location: often extra-adrenal or bilateral; HNPGL (Cluster 1 SDHD/SDHC)
- Malignancy: highest risk (especially SDHB); multiple tumors
- Imaging: 68Ga-DOTATATE PET (SSTR2-avid); 18F-FDG PET (high avidity in SDHB-mutant due to HIF-1α-driven glycolysis)

**Cluster 2 — Kinase/RAS signaling:**
- Genes: RET, NF1, TMEM127, MAX
- Mechanism: RET tyrosine kinase activation (MEN2) or NF1/RAS hyperactivation → MAPK, PI3K/AKT
- Biochemistry: predominantly **epinephrine-secreting** (adrenal; PNMT expressed)
- Location: adrenal medulla; bilateral
- Malignancy: lower risk (<5-10%); mostly benign
- Imaging: 123I-MIBG (NET-avid, catecholamine transporter intact)

### Adrenal medulla anatomy

The adrenal medulla constitutes ~10-20% of adrenal gland volume (cortex = 80-90%):
- Chromaffin cells are neuroendocrine, modified postganglionic sympathetic neurons
- Secrete epinephrine (~80%) and norepinephrine (~20%) into venous blood (not via synaptic release)
- Chromaffin cells express: tyrosine hydroxylase (TH), dopamine β-hydroxylase (DBH), phenylethanolamine-N-methyltransferase (PNMT — converts NE→E; cortisol-dependent), SSTR2, NET (SLC6A2)
- Blood supply via adrenal vein (into inferior vena cava on right, renal vein on left)

## Function

### Catecholamine biosynthesis and release

Normal chromaffin cell catecholamine synthesis:
Tyrosine → DOPA (TH, rate-limiting) → Dopamine (DOPA decarboxylase) → Norepinephrine (DBH) → Epinephrine (PNMT)

In PHEO/PGL:
- Tumors secrete catecholamines constitutively and episodically
- Metanephrines (normetanephrine, metanephrine, methoxytyramine) are O-methylated metabolites produced continuously within the tumor (via COMT) — superior biomarkers to parent catecholamines
- Parasympathetic HNPGLs secrete dopamine or methoxytyramine (low/absent PNMT); often biochemically silent on NE/E panels

### Biochemical diagnosis

**Plasma free metanephrines** (preferred for hereditary/high-risk patients): sensitivity ~97% (normetanephrine), ~99% (metanephrine); specificity ~85-90%; gold standard for detection; posture affects NE (supine preferred)

**24-hour urinary fractionated metanephrines and catecholamines**: equivalent sensitivity for large tumors; preferred in some labs; interference: catecholamine-containing foods, labetalol, methyldopa, tricyclics

**Methoxytyramine (plasma or urine)**: elevated in dopamine-secreting PGL (often SDHx-driven, HNPGL); rises in metastatic disease; aids malignancy risk stratification

**Biochemical confirmation required before imaging** — chance adrenal incidentalomas ("incidentalomas") and beta-blocker use can cause false-positive elevations; repeat testing on standardized diet (avoid coffee, bananas, vanilla 48h before)

## Pathology

### Surgical management

**Preoperative medical preparation (mandatory, non-negotiable):** [^lenders-2014-pheo-guideline]
Alpha-adrenergic blockade must be established 10-14 days before surgery to prevent intraoperative hypertensive crisis:
- **Phenoxybenzamine** (irreversible α1+α2 blocker): 10-40 mg BID; superior preoperative preparation in most centers; side effects: orthostatic hypotension, reflex tachycardia, nasal congestion
- **Doxazosin** (selective α1 blocker): 2-16 mg QD; fewer side effects; comparable outcomes in many series
- **Beta-blockade** (propranolol, atenolol): initiated ONLY after alpha blockade established (≥3-5 days) to control tachycardia — giving beta-blocker first → unopposed alpha → hypertensive crisis
- **High-sodium diet + IV fluids**: counteract catecholamine-induced plasma volume depletion

**Surgical approach:**
- Laparoscopic adrenalectomy: standard for adrenal PHEO ≤6-8 cm; retroperitoneal endoscopic approach increasingly preferred (direct adrenal access, less bowel manipulation)
- Open adrenalectomy: PHEO >6-8 cm, suspected malignant, extra-adrenal PGL with vascular involvement
- Cortical-sparing adrenalectomy: bilateral PHEO (VHL, MEN2) → preserve adrenal cortex to avoid lifelong glucocorticoid dependence if possible

**Intraoperative management:**
- Anesthesiologist must anticipate catecholamine surges (tumor manipulation) → IV phentolamine (alpha blocker) + nitroprusside/nicardipine for hypertensive crisis; esmolol for tachycardia
- Hypotension after tumor removal (catecholamine withdrawal) → IV fluids + vasopressors

### Malignant PHEO/PGL

**Definition**: presence of metastases in sites where chromaffin tissue is not normally found (regional LN, bone, liver, lung, peritoneum) — no histologic criteria (Ki-67, mitoses, necrosis) reliably predict malignancy

**Risk stratification:**
- SDHB mutation: ~30-40% risk of metastases
- Tumor size >5 cm, extra-adrenal location, norepinephrine-only secretion: higher risk
- **PASS score** (Pheochromocytoma of Adrenal gland Scaled Score) and **GAPP** (grading system for adrenal pheochromocytoma and paraganglioma): pathological scoring systems; moderate predictive value
- 18F-FDG PET avidity: high avidity predicts malignancy in SDHB-mutant tumors

**Imaging for staging and surveillance:**
- 68Ga-DOTATATE PET: first-line functional imaging; superior to 123I-MIBG for staging, especially Cluster 1 tumors
- 123I-MIBG: required if considering 131I-MIBG therapy (must be MIBG-avid); ~30-40% of malignant PHEO are MIBG-negative
- 18F-FDG PET: best for SDHB-mutant and high-grade tumors; correlates with HIF-1α-driven metabolic activity

**Systemic therapy for malignant PHEO/PGL:**

**Sunitinib** (VEGFR1/2/3, PDGFR, KIT, RET inhibitor):
FIRSTMAPPP trial (Baudin 2021) [^baudin-2021-firstmappp-sunitinib]: N=78 progressive malignant PHEO/PGL; sunitinib 37.5 mg/day vs placebo; primary endpoint PFS; HR 0.50 (95% CI 0.28-0.88); p=0.017; 12-month PFS 35.9% vs 19.2%; OS not different (crossover confounded); standard of care for progressive disease

**177Lu-DOTATATE** (lutetium-177 PRRT):
Targets SSTR2 on chromaffin cells; eligibility: 68Ga-DOTATATE PET avid (Krenning score ≥2); ORR ~25-30% in PHEO/PGL series (retrospective); COMPETE trial ongoing; 68Ga-DOTATATE PET superior to 123I-MIBG for eligibility selection in Cluster 1 tumors

**131I-MIBG** (Azedra, high specific activity iobenguane I-131):
FDA-approved 2018 for iobenguane-avid unresectable/metastatic PHEO/PGL ≥12 years; eligibility: 123I-MIBG scan positive; ORR ~25%; main toxicity: bone marrow suppression (stem cell storage recommended); not preferred for SDHB-mutant (often MIBG-negative)

**CVD chemotherapy** (cyclophosphamide + vincristine + dacarbazine):
Oldest regimen; ORR ~37% (biochemical response); PFS ~3-4 months; partial response more common than CR; used in rapidly progressive disease when targeted/PRRT not available

**Cabozantinib** (VEGFR2/MET/RET/AXL):
Active in Cluster 1 (MET/AXL co-expressed in SDH-deficient tumors); Phase 2 CABOPHEN: ORR ~15%, PFS ~5-6 months in malignant PHEO/PGL; also active in RET-driven (Cluster 2) malignant PHEO

**Prognosis:**
- Localized PHEO: 5-year OS ~95%; curative after adrenalectomy
- Malignant PHEO/PGL (all): 5-year OS ~50-60%
- SDHB-mutant malignant: 5-year OS ~20-30%; most aggressive
- SDHD/VHL malignant: intermediate prognosis (~50-70% 5-year OS)
- 20-year surveillance recommended for all SDHx carriers (multiple primaries common)

## Connections

- `connects-to` → **[SDHB](../../03-molecular/sdhb/README.md)** — Hereditary PHEO/PGL caused by SDHB biallelic LOF → PGL4 syndrome; SDHB germline carriers: ~30-40% develop malignant PHEO/PGL (vs <5% SDHD/SDHC); highest malignant risk of all SDHx loci; SDHB IHC (granular cytoplasmic staining) used for initial SDH-deficient tumor screening.
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — VHL-mutant PHEO/PGL: Cluster 1 pseudohypoxia; bilateral PHEO in ~10-20% VHL patients; VHL type 2C (missense): PHEO-only phenotype; VHL-mutant PHEO is predominantly norepinephrine-secreting; sunitinib active in VHL-mutant metastatic PHEO/PGL; 68Ga-DOTATATE PET for staging.
- `connects-to` → **[RET](../../03-molecular/ret/README.md)** — RET mutations in PHEO/PGL: Cluster 2 kinase signaling; RET M918T (MEN2B, most aggressive) or C634F/Y (MEN2A) → PHEO in ~40-50% MEN2A/B; epinephrine-predominant secretion; bilateral adrenal PHEO; prophylactic adrenalectomy in MEN2B; vandetanib/cabozantinib active in MTC.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — PHEO/PGL Cluster 1 (SDHx, VHL) activate HIF-1α by pseudohypoxia → VEGF, GLUT1 transcription; HIF-1α drives tumor angiogenesis; HIF-1α target expression predicts malignant behavior; 18F-FDG PET avidity in SDHB-mutant PHEO correlates with HIF-1α-driven metabolic reprogramming.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Pheochromocytomas arise in the adrenal medulla from chromaffin cells, pouring epinephrine and norepinephrine into the adrenal vein; surgery demands 10-14 days of alpha-adrenergic blockade first (beta only after) to prevent intraoperative hypertensive crisis.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Neurofibromatosis type 1 is a Cluster 2 (kinase-signaling) hereditary pheochromocytoma syndrome: ~3-4% of NF1 patients develop adrenal, epinephrine-secreting PHEO; loss of neurofibromin's RAS-GAP activity drives the chromaffin tumor, paralleling RET-driven MEN2 PHEO.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Chromaffin tumors synthesize epinephrine and norepinephrine but are best detected by their continuously produced O-methylated metabolites — plasma free metanephrines (~97-99% sensitive); paroxysmal catecholamine surges cause episodic hypertension, palpitations, and headache.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Pheochromocytoma/paraganglioma and clear-cell RCC are linked by pseudohypoxia: VHL loss (and SDHx/FH defects) stabilizes HIF-2α even in normoxia, driving VEGF and a hypervascular tumor in both; VHL disease produces them together, and HIF-2α inhibitors like belzutifan treat both.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — VHL disease is a leading hereditary cause of pheochromocytoma/paraganglioma: germline VHL loss drives Cluster-1 pseudohypoxia, producing bilateral, often norepinephrine-secreting PHEO in 10-20% alongside clear-cell RCC — so young or bilateral PHEO warrants VHL testing.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Pheochromocytoma/paraganglioma and neuroblastoma are both neural-crest, catecholamine-handling sympathoadrenal tumors that take up MIBG and secrete catecholamine metabolites, but PPGL is an adult chromaffin tumor while neuroblastoma is an aggressive embryonal cancer of children.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Pheochromocytoma is the classic curable secondary cause of hypertension: episodic catecholamine release produces the paroxysmal triad of headache, palpitations, and sweating with severe spikes, so resistant or paroxysmal hypertension warrants plasma/urine metanephrine screening.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — Paragangliomas appear in Carney-related syndromes—but not Carney complex itself: the SDH-deficient Carney triad (paraganglioma, gastric GIST, pulmonary chondroma) and Carney-Stratakis dyad are distinct from PRKAR1A-driven Carney complex, a common point of confusion.
- `connects-to` → **[HLRCC](../hlrcc/README.md)** — Pheochromocytoma/paraganglioma and HLRCC share a pseudohypoxia mechanism: both belong to the TCA-cycle tumor family where SDH or FH loss accumulates succinate/fumarate, inhibits HIF prolyl-hydroxylases, and stabilizes HIF—rarely yielding FH-mutant PPGL itself.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Pheochromocytoma is defined by the catecholamines it secretes: chromaffin tumors release norepinephrine and epinephrine, driving paroxysmal hypertension, while their breakdown products are the diagnostic test—an unregulated norepinephrine factory.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Pheochromocytoma is the organic disease that most convincingly mimics panic disorder: surges of catecholamines cause sudden palpitations and a sense of doom identical to a panic attack, so atypical 'panic' with hypertension warrants metanephrine testing.
- `connects-to` → **[GIST](../gist/README.md)** — Paraganglioma and GIST are joined in Carney triad: SDH-deficient tumors—paragangliomas plus wild-type GISTs—arise together when succinate dehydrogenase loss drives pseudohypoxia, so finding one SDH-deficient tumor prompts a search for the other.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — NF1 is one of several genes causing hereditary pheochromocytoma: neurofibromin loss (like RET, VHL and SDH mutations) predisposes to catecholamine-secreting tumors, so a pheochromocytoma should prompt genetic testing—up to a third are hereditary.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Pheochromocytoma can devastate the heart: catecholamine surges cause hypertensive crises, arrhythmias and a stress (Takotsubo) cardiomyopathy, so the tumor's adrenaline output threatens the heart—and alpha-blockade before surgery prevents catastrophic crises.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — Pheochromocytoma belongs to MEN2, not MEN1: it arises with medullary thyroid cancer in RET-driven MEN2, whereas MEN1 (menin) causes parathyroid, pituitary and pancreatic tumors—so the two MEN syndromes are distinguished partly by whether pheochromocytoma occurs.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Pheochromocytoma is a cardiovascular emergency in waiting: surges of catecholamines cause paroxysmal hypertension, palpitations and arrhythmia, and can trigger catecholamine cardiomyopathy or crisis—so alpha-blockade before surgery is essential to prevent fatal swings.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Paragangliomas arise along the autonomic nervous system: these tumors grow in sympathetic and parasympathetic paraganglia (from adrenal medulla to carotid body), so they are neural-crest tumors of the nervous system that happen to flood the body with catecholamines.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Pheochromocytoma is a hormone-secreting tumor of the endocrine adrenal medulla: it autonomously pours catecholamines into blood, so it belongs among the functional endocrine tumors and clusters in syndromes (MEN2, VHL, NF1) with other endocrine neoplasia.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Pheochromocytoma and paraganglioma are imaged and treated with radioactive iodine via MIBG: these catecholamine-handling tumors take up I-123/I-131 metaiodobenzylguanidine, lighting them up on scans and delivering targeted radiation in metastatic disease.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — Many paragangliomas express SSTR2, opening a second nuclear-medicine route: 68Ga-DOTATATE PET often detects SDHx-related and head-and-neck tumors better than MIBG, and 177Lu-DOTATATE delivers peptide receptor radiotherapy in metastatic cases.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Pheochromocytoma and paraganglioma spring from neural-crest lineage: the chromaffin and paraganglion cells share an origin with neurons of the sympathetic nervous system, which is why these tumors secrete catecholamines like nerve cells do.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Some pheochromocytomas and paragangliomas secrete dopamine: especially SDHB-driven head-and-neck tumors release dopamine and its metabolite 3-methoxytyramine, a biochemical signature that flags a hereditary, more malignant-prone tumor.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Pheochromocytoma-paraganglioma is tied to oxygen sensing: carotid-body paragangliomas are literal oxygen sensors, and SDH/VHL mutations fake low oxygen (pseudohypoxia), stabilizing HIF to drive the 'cluster 1' hereditary tumors.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Pheochromocytomas are intensely vascular through VEGF: pseudohypoxic HIF signaling pumps out VEGF, so these tumors are richly perfused and prone to bleeding—and anti-angiogenic drugs are tried against metastatic disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Pheochromocytomas dump catecholamines via calcium: chromaffin cells release adrenaline by calcium-triggered exocytosis, so the tumor's surges of hormone—and the spells of pounding blood pressure they cause—run on this calcium-dependent machinery.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages fill the pheochromocytoma's vascular stroma: drawn into the richly perfused, pseudohypoxic tumor, they support its blood supply and shape an immune niche of interest in the hard-to-treat metastatic disease.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Pheochromocytoma punishes the kidneys through catecholamines: the surges of adrenaline and noradrenaline drive severe hypertension that damages the kidney's vessels, and extra-adrenal paragangliomas can also arise near the renal hilum.

[^lenders-2014-pheo-guideline]: Lenders JW, Duh QY, Eisenhofer G, et al. Pheochromocytoma and paraganglioma: an endocrine society clinical practice guideline. *J Clin Endocrinol Metab.* 2014;99(6):1915-1942. [doi:10.1210/jc.2014-1498](https://doi.org/10.1210/jc.2014-1498) · [PubMed 24893135](https://pubmed.ncbi.nlm.nih.gov/24893135/)
[^baudin-2021-firstmappp-sunitinib]: Baudin E, Goichot B, Berruti A, et al. First International Randomized Study in Malignant Progressive Pheochromocytoma and Paragangliomas (FIRSTMAPPP). *Ann Oncol.* 2021;32(10):1245-1254. [doi:10.1016/j.annonc.2021.07.009](https://doi.org/10.1016/j.annonc.2021.07.009) · [PubMed 34246769](https://pubmed.ncbi.nlm.nih.gov/34246769/)
