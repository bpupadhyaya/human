---
schema: human-scale-entry/v1
id: men1-syndrome
name: MEN1 Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Multiple Endocrine Neoplasia type 1 (MEN1) is caused by germline MEN1 mutations; triad of parathyroid adenomas (>95%), pituitary adenomas (20-65%), and pancreatic NETs (30-80%); everolimus FDA-approved for pNETs; annual biochemical + MRI surveillance."
aliases: ["MEN1 syndrome", "multiple endocrine neoplasia type 1", "Wermer syndrome", "MEN type 1", "MEN-1", "hereditary pNET", "parathyroid-pituitary-pancreas syndrome", "MEN1 hereditary cancer"]
sources:
  - id: thakker-2012-men1-guidelines
    type: peer-reviewed
    cite: "Thakker RV, Newey PJ, Walls GV, et al. Clinical practice guidelines for multiple endocrine neoplasia type 1 (MEN1). J Clin Endocrinol Metab. 2012;97(9):2990-3011."
    doi: "10.1210/jc.2012-1174"
    pmid: "22392070"
    url: "https://doi.org/10.1210/jc.2012-1174"
  - id: chandrasekharappa-1997-men1
    type: peer-reviewed
    cite: "Chandrasekharappa SC, Guru SC, Manickam P, et al. Positional cloning of the gene for multiple endocrine neoplasia-type 1. Science. 1997;276(5311):404-407."
    doi: "10.1126/science.276.5311.404"
    pmid: "9103196"
    url: "https://doi.org/10.1126/science.276.5311.404"
cross_links:
  - target: 01-human/03-molecular/men1
    relation: connects-to
    note: "Germline MEN1 mutations cause MEN1 syndrome by haploinsufficiency; somatic second-hit (LOH at 11q13) confirms two-hit model; menin LOF depletes H3K4me3 at CDKN1B/CDKN2C → CDK4/6 activation → neuroendocrine proliferation."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Somatostatin analogs (octreotide LAR, lanreotide autogel) are first-line for functional MEN1-associated NETs; Ga-68 DOTATATE PET/CT is preferred for staging; SSTR2 expression guides peptide receptor radionuclide therapy (PRRT) eligibility."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "MEN1-associated pNETs are multifocal, arise earlier than sporadic NETs, and include functioning (insulinoma, gastrinoma) and non-functioning tumors; RADIANT-3 trial: everolimus (mTOR inhibitor) improved PFS from 4.6 to 11.0 months vs placebo in pNET."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "MEN1 pNETs are classified and treated as well-differentiated NETs, not PDAC; surgical threshold is >2 cm for non-functioning pNETs; CLARINET trial: lanreotide autogel extended PFS vs placebo (HR 0.47) in G1/G2 gastroenteropancreatic NETs."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Everolimus (mTOR inhibitor, RADIANT-3) improved PFS from 4.6 to 11.0 months vs placebo in advanced pNET; mTOR constitutively activated by menin LOF via CDK4/6 → mTORC1; everolimus FDA-approved for non-functioning progressive pNET; sunitinib is the alternative VEGFR/PDGFR option."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulinoma occurs in ~10-20% of MEN1; autonomous insulin → hypoglycemia (Whipple's triad); often multifocal, small (<2 cm); diazoxide suppresses insulin secretion; EUS is most sensitive for small insulinoma localization; everolimus is anti-secretory in MEN1 insulinoma."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Prolactinoma is the most common pituitary adenoma in MEN1 (~60% of pituitary lesions); hyperprolactinaemia → hypogonadism + galactorrhea; cabergoline/bromocriptine first-line; MEN1 prolactinomas are more cabergoline-resistant; transsphenoidal surgery for resistant cases."
  - target: 01-human/07-system/men4-syndrome
    relation: connects-to
    note: "MEN1 and MEN4 are clinically near-identical multiple endocrine neoplasia syndromes — both cause parathyroid, pituitary, and pancreatic neuroendocrine tumors — but differ in gene: MEN1 from menin loss, MEN4 from CDKN1B/p27 loss; CDKN1B testing follows a negative MEN1 result."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Primary hyperparathyroidism is the earliest and most penetrant MEN1 manifestation (~95% by age 50): menin loss drives multigland parathyroid hyperplasia → excess PTH → hypercalcemia, kidney stones, and bone loss; subtotal parathyroidectomy is standard as all glands are at risk."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The pancreas is the most dangerous MEN1 site: multifocal pancreatic neuroendocrine tumors — gastrinomas (Zollinger-Ellison), insulinomas, non-functioning pNETs — arise young and are the leading cause of MEN1 mortality; surveillance MRI and a >2 cm surgical threshold guide care."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "MEN1 and Carney complex are both hereditary multiple-endocrine-neoplasia syndromes with different drivers: MEN1 (menin loss) gives parathyroid, islet and pituitary tumors; Carney (PRKAR1A/PKA) adds cardiac myxomas, skin pigmentation and PPNAD, with overlapping pituitary disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "MEN1 is the archetypal disease of the endocrine system as a network: a single menin mutation simultaneously transforms the parathyroids, pancreatic islets and anterior pituitary (the '3 Ps'), showing how one tumor-suppressor's loss dysregulates multiple endocrine glands at once."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Pituitary adenomas are one of MEN1's three core tumors and frequently disturb growth hormone: GH-secreting somatotroph adenomas cause acromegaly, while prolactinomas are the commonest MEN1 pituitary tumor—so IGF-1/GH and prolactin screening is part of MEN1 surveillance."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "MEN1 and pheochromocytoma belong to the inherited endocrine-tumor syndromes but rarely overlap: MEN1's parathyroid, pancreatic and pituitary tumors contrast with the adrenal-medullary catecholamine tumors of MEN2 and VHL—so a pheochromocytoma points away from MEN1."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "MEN1 and von Hippel-Lindau are both dominant tumor-suppressor syndromes causing multi-organ tumors: MEN1 gives parathyroid, islet and pituitary tumors, while VHL gives pheochromocytoma, renal cancer and pancreatic NETs—overlapping in the pancreas, differing elsewhere."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal gland is a frequent but often silent MEN1 target: up to 40% of MEN1 patients develop adrenal cortical enlargement or adenomas, usually nonfunctioning, so surveillance imaging covers the adrenals even though parathyroid, pancreatic and pituitary tumors dominate."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Thyroid tumors occur in MEN1 beyond the classic three glands: while parathyroid, pituitary and pancreas dominate, menin loss also predisposes to thyroid adenomas and carcinoma, so the syndrome's reach extends across endocrine organs—warranting broad surveillance."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cushing's syndrome arises in MEN1 from two routes: ACTH-secreting pituitary tumors or adrenal/ectopic neuroendocrine tumors raise cortisol, so hypercortisolism in a MEN1 patient demands working out whether the pituitary, adrenal or a pancreatic NET is the source."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Primary hyperparathyroidism—MEN1's earliest, commonest feature—drives bone loss: excess PTH from multigland parathyroid tumors pulls calcium from bone, causing osteoporosis and stones, so early parathyroidectomy protects the skeleton in MEN1."
---

# MEN1 Syndrome

## Overview

**Multiple Endocrine Neoplasia type 1 (MEN1 syndrome)**, historically called Wermer syndrome, is an autosomal dominant hereditary cancer predisposition syndrome caused by germline pathogenic variants in the **MEN1** tumor suppressor gene (chromosome 11q13). MEN1 syndrome affects approximately **1 in 20,000-30,000** individuals and is characterized by the clinical triad of **parathyroid adenomas** (>95% penetrance), **anterior pituitary adenomas** (20-65% penetrance), and **gastroenteropancreatic neuroendocrine tumors** (GEP-NETs, 30-80% penetrance). An estimated 10% of cases arise from de novo germline mutations. MEN1 syndrome accounts for approximately 1-2% of primary hyperparathyroidism and a significant proportion of sporadic-appearing pNETs in young patients [^thakker-2012-men1-guidelines] [^chandrasekharappa-1997-men1].

**MEN1 syndrome penetrance by manifestation (cumulative by age 50):**

| Manifestation | Penetrance | Typical onset age |
|---|---|---|
| Parathyroid adenoma (pHPT) | >95% | 20-30 years |
| Gastrinoma / ZES | 40-50% | 25-35 years |
| Non-functioning pNET | 20-40% | 30-40 years |
| Insulinoma | 10-20% | 25-35 years |
| Anterior pituitary adenoma | 20-65% | 25-40 years |
| Adrenocortical tumor (non-functioning) | 20-40% | 30-50 years |
| Thymic NET | ~5-10% | 35-50 years |
| Bronchial carcinoid | ~5-10% | 35-50 years |
| Skin: angiofibroma, collagenoma | >80% | 20-40 years |

## Structure

### Genetic basis

- **Gene**: MEN1 (chromosome 11q13.1, 67 kb, 10 exons)
- **Inheritance**: autosomal dominant; 50% offspring risk from carrier parent
- **De novo rate**: ~10% of index cases
- **Mutation spectrum**: ~1,000 unique germline variants catalogued in the MEN1 database; frameshift/nonsense (~45%), missense (~35%), splice (~10%), large deletions (~10%)
- **Hotspot**: no single hotspot mutation; each family tends to have a private variant; codon 83 and exon 2 are disproportionately affected
- **Genotype-phenotype correlation**: weak; same mutation within a family can produce highly variable expression; modifier genes and somatic events drive phenotype
- **Somatic second hit**: LOH at 11q13 (most common); small deletion; rarely a second point mutation

### Parathyroid disease

Primary hyperparathyroidism (pHPT) is the **first and most common** manifestation. MEN1-associated pHPT is multiglandular (all four glands eventually involved) and distinct from sporadic adenoma (typically single gland):
- Biochemical: elevated serum calcium + elevated or inappropriately normal intact PTH
- Histology: multiple adenomas (earliest) progressing to four-gland hyperplasia (later); carcinoma is rare (<1%)
- Consequences: nephrolithiasis (most common), nephrocalcinosis, osteoporosis, neuropsychiatric symptoms (fatigue, depression), GI (constipation)
- Treatment: **3.5-gland parathyroidectomy** (subtotal) with cryopreservation of remnant, or **total parathyroidectomy with autotransplantation** to forearm; intraoperative PTH monitoring; recurrence rate ~50% at 10 years (vs <5% for sporadic adenoma); cinacalcet (calcimimetic) for medical management or post-operative recurrence

### Pancreatic/duodenal NETs (GEP-NETs)

**Gastrinoma / Zollinger-Ellison syndrome (ZES):**
Most common functional GEP-NET in MEN1; 60-90% arise in the duodenum (tiny microgastrinomas, 1-3 mm), not the pancreas; duodenal gastrinomas may metastasize to regional lymph nodes despite tiny primary size; ZES: gastric acid hypersecretion → peptic ulcers resistant to standard doses + diarrhea; treatment: high-dose PPI (omeprazole 40-60 mg BID) controls acid; surgical cure less common in MEN1-associated ZES than sporadic due to multifocality

**Insulinoma:**
- Second most common functional pNET; hypoglycemia (Whipple's triad: symptoms + glucose <55 mg/dL + relief with glucose)
- Often multifocal in MEN1; typically small (<2 cm) when symptomatic
- Localization: EUS (endoscopic ultrasound) most sensitive for small insulinomas; ⁶⁸Ga-DOTATATE PET less sensitive than EUS for insulinoma (lower SSTR2 expression)
- Treatment: diazoxide (K-ATP channel opener, suppresses insulin secretion) for inoperable; surgical enucleation for localized; everolimus (RADIANT-3) has anti-secretory effect on insulinoma

**Non-functioning pNETs (NF-pNETs):**
- Most common pNET overall; detected incidentally or by surveillance imaging
- Risk of malignancy correlates with size: >2 cm → 25-35% risk of metastasis → surgical resection recommended; <2 cm with stable growth → surveillance with annual MRI
- MEN1 pNETs generally well-differentiated (G1-G2); G3 NETs rare

**VIPoma, glucagonoma, somatostatinoma**: rare in MEN1 (<5% each); VIPoma → watery diarrhea/hypokalemia; glucagonoma → necrolytic migratory erythema, diabetes

### Pituitary tumors

- Prolactinoma (most common, ~60% of MEN1 pituitary adenomas): prolactin ↑ → hypogonadism, galactorrhea; treatment: dopamine agonists (cabergoline, bromocriptine); resistance in MEN1-associated prolactinomas is higher than sporadic
- Somatotroph adenoma (GH-secreting, ~25%): acromegaly; treatment: somatostatin analogs (octreotide LAR, lanreotide autogel), cabergoline, pegvisomant (GH receptor antagonist), transsphenoidal surgery, radiotherapy
- Corticotroph adenoma (ACTH-secreting, ~5%): Cushing disease; transsphenoidal surgery; ketoconazole/osilodrostat for medical management
- Non-functioning (gonadotroph, ~10%): detected by mass effect; visual field defects; transsphenoidal decompression

### Other manifestations

- **Adrenocortical tumors**: 20-40% of MEN1 patients; usually non-functioning; cortical adenoma or hyperplasia; rarely adrenocortical carcinoma (~2%); biochemical screen (DHEA-S, UFC, midnight cortisol, aldosterone/renin ratio)
- **Thymic NET**: most lethal MEN1 manifestation in some series; strongly male-predominant (M:F 4:1); smoking increases risk; prophylactic thymectomy at parathyroid surgery debated; surveillance: CT chest annually
- **Bronchial carcinoid**: less aggressive than thymic; female predominant; surveillance: CT chest/MRI annually
- **Skin**: facial angiofibromas (94%, pathognomonic for MEN1 in multiples), truncal collagenomas (72%), café-au-lait macules, lipomas; angiofibromas precede endocrine manifestations by years
- **Meningioma**: ~8% in some series; spinal ependymoma reported

## Function

### Disease mechanism

Menin haploinsufficiency (one functional allele) creates susceptibility: cells appear normal until the remaining wild-type MEN1 allele undergoes somatic second hit (LOH at 11q13). Biallelic MEN1 LOF → complete menin loss → H3K4me3 depletion at CDKN1B (p27) and CDKN2C (p18) promoters → CDK4/6 activation → Rb phosphorylation → E2F release → cell cycle entry → proliferation in neuroendocrine-lineage cells. Parathyroid chief cells, pituitary lactotrophs/somatotrophs, and islet β-cells/δ-cells are particularly dependent on menin for p27/p18-mediated G1 arrest.

### Distinguishing MEN1 from MEN2/MEN4

| Feature | MEN1 (Wermer) | MEN2A (Sipple) | MEN2B | MEN4 |
|---|---|---|---|---|
| Gene | MEN1 (11q13) | RET (10q11) | RET (10q11) | CDKN1B (12p13) |
| Parathyroid | >95% | 20-30% | Rare | Parathyroid tumor |
| Pituitary | 20-65% | Absent | Absent | Pituitary adenoma |
| Pancreatic NET | 30-80% | Absent | Absent | Rare |
| Thyroid | Absent | Medullary Ca (>95%) | Medullary Ca (>95%) | Absent |
| Pheochromocytoma | Absent | 50% | 50% | Absent |
| Treatment paradigm | Menin pathway | RET kinase inhibitors | RET kinase inhibitors | CDK inhibitors |

## Pathology

### Surveillance protocol (Thakker 2012 guidelines)

**Biochemical (annual from age 8-10 in gene carriers):**
- Ionized calcium + intact PTH (parathyroid)
- Fasting gastrin (gastrinoma screen); if abnormal: secretin stimulation test
- Fasting insulin/glucose (insulinoma screen)
- Chromogranin A (NF-pNET marker; ↑ = tumor burden)
- Prolactin, IGF-1/GH (pituitary)
- DHEA-S, 24h urinary free cortisol (adrenal)
- Glucagon, VIP (if symptoms suggest)

**Imaging:**
- **MRI abdomen** (preferred over CT to avoid radiation): every 1-3 years; pNET detection; liver metastasis
- **EUS (endoscopic ultrasound)**: most sensitive for small pNETs and duodenal gastrinomas; every 1-2 years
- **⁶⁸Ga-DOTATATE PET/CT**: superior functional imaging for SSTR2-positive NETs; preferred over ¹¹¹In-octreotide SPECT; staging at diagnosis of functioning NET or NF-pNET >1 cm
- **MRI pituitary** (gadolinium): at diagnosis + every 3-5 years or if symptoms
- **CT chest**: annual for thymic/bronchial carcinoid surveillance

### Surgical indications

- **Parathyroid**: symptomatic pHPT (stones, osteoporosis, calcium >1 mg/dL above normal); 3.5-gland resection or total + autotransplant
- **pNET**: NF-pNET >2 cm (resection); functioning pNET (insulinoma/glucagonoma) regardless of size; gastrinoma: surgical cure less achievable due to multifocality; pancreaticoduodenectomy (Whipple) debated for duodenal microgastrinomas
- **Pituitary**: visual field compromise; cabergoline failure for prolactinoma; transsphenoidal surgery

## Connections

- `connects-to` → **[MEN1](../../03-molecular/men1/README.md)** — Germline MEN1 mutations cause MEN1 syndrome by haploinsufficiency; somatic second-hit (LOH at 11q13) confirms two-hit model; menin LOF depletes H3K4me3 at CDKN1B/CDKN2C → CDK4/6 activation → neuroendocrine proliferation.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — Somatostatin analogs (octreotide LAR, lanreotide autogel) are first-line for functional MEN1-associated NETs; Ga-68 DOTATATE PET/CT is preferred for staging; SSTR2 expression guides peptide receptor radionuclide therapy (PRRT) eligibility.
- `connects-to` → **[Neuroendocrine Tumors](../../07-system/neuroendocrine-tumors/README.md)** — MEN1-associated pNETs are multifocal, arise earlier than sporadic NETs, and include functioning (insulinoma, gastrinoma) and non-functioning tumors; RADIANT-3 trial: everolimus (mTOR inhibitor) improved PFS from 4.6 to 11.0 months vs placebo in pNET.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — MEN1 pNETs are classified and treated as well-differentiated NETs, not PDAC; surgical threshold is >2 cm for non-functioning pNETs; CLARINET trial: lanreotide autogel extended PFS vs placebo (HR 0.47) in G1/G2 gastroenteropancreatic NETs.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Everolimus (mTOR inhibitor, RADIANT-3) improved PFS from 4.6 to 11.0 months vs placebo in advanced pNET; mTOR constitutively activated by menin LOF via CDK4/6 → mTORC1; everolimus FDA-approved for non-functioning progressive pNET; sunitinib is the alternative VEGFR/PDGFR option.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulinoma occurs in ~10-20% of MEN1; autonomous insulin → hypoglycemia (Whipple's triad); often multifocal, small (<2 cm); diazoxide suppresses insulin secretion; EUS is most sensitive for small insulinoma localization; everolimus is anti-secretory in MEN1 insulinoma.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Prolactinoma is the most common pituitary adenoma in MEN1 (~60% of pituitary lesions); hyperprolactinaemia → hypogonadism + galactorrhea; cabergoline/bromocriptine first-line; MEN1 prolactinomas are more cabergoline-resistant; transsphenoidal surgery for resistant cases.
- `connects-to` → **[MEN4 Syndrome](../men4-syndrome/README.md)** — MEN1 and MEN4 are clinically near-identical multiple endocrine neoplasia syndromes — both cause parathyroid, pituitary, and pancreatic neuroendocrine tumors — but differ in gene: MEN1 from menin loss, MEN4 from CDKN1B/p27 loss; CDKN1B testing follows a negative MEN1 result.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Primary hyperparathyroidism is the earliest and most penetrant MEN1 manifestation (~95% by age 50): menin loss drives multigland parathyroid hyperplasia → excess PTH → hypercalcemia, kidney stones, and bone loss; subtotal parathyroidectomy is standard as all glands are at risk.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The pancreas is the most dangerous MEN1 site: multifocal pancreatic neuroendocrine tumors — gastrinomas (Zollinger-Ellison), insulinomas, non-functioning pNETs — arise young and are the leading cause of MEN1 mortality; surveillance MRI and a >2 cm surgical threshold guide care.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — MEN1 and Carney complex are both hereditary multiple-endocrine-neoplasia syndromes with different drivers: MEN1 (menin loss) gives parathyroid, islet and pituitary tumors; Carney (PRKAR1A/PKA) adds cardiac myxomas, skin pigmentation and PPNAD, with overlapping pituitary disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — MEN1 is the archetypal disease of the endocrine system as a network: a single menin mutation simultaneously transforms the parathyroids, pancreatic islets and anterior pituitary (the '3 Ps'), showing how one tumor-suppressor's loss dysregulates multiple endocrine glands at once.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Pituitary adenomas are one of MEN1's three core tumors and frequently disturb growth hormone: GH-secreting somatotroph adenomas cause acromegaly, while prolactinomas are the commonest MEN1 pituitary tumor—so IGF-1/GH and prolactin screening is part of MEN1 surveillance.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — MEN1 and pheochromocytoma belong to the inherited endocrine-tumor syndromes but rarely overlap: MEN1's parathyroid, pancreatic and pituitary tumors contrast with the adrenal-medullary catecholamine tumors of MEN2 and VHL—so a pheochromocytoma points away from MEN1.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — MEN1 and von Hippel-Lindau are both dominant tumor-suppressor syndromes causing multi-organ tumors: MEN1 gives parathyroid, islet and pituitary tumors, while VHL gives pheochromocytoma, renal cancer and pancreatic NETs—overlapping in the pancreas, differing elsewhere.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal gland is a frequent but often silent MEN1 target: up to 40% of MEN1 patients develop adrenal cortical enlargement or adenomas, usually nonfunctioning, so surveillance imaging covers the adrenals even though parathyroid, pancreatic and pituitary tumors dominate.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Thyroid tumors occur in MEN1 beyond the classic three glands: while parathyroid, pituitary and pancreas dominate, menin loss also predisposes to thyroid adenomas and carcinoma, so the syndrome's reach extends across endocrine organs—warranting broad surveillance.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cushing's syndrome arises in MEN1 from two routes: ACTH-secreting pituitary tumors or adrenal/ectopic neuroendocrine tumors raise cortisol, so hypercortisolism in a MEN1 patient demands working out whether the pituitary, adrenal or a pancreatic NET is the source.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Primary hyperparathyroidism—MEN1's earliest, commonest feature—drives bone loss: excess PTH from multigland parathyroid tumors pulls calcium from bone, causing osteoporosis and stones, so early parathyroidectomy protects the skeleton in MEN1.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^thakker-2012-men1-guidelines]: Thakker RV, Newey PJ, Walls GV, et al. Clinical practice guidelines for multiple endocrine neoplasia type 1 (MEN1). *J Clin Endocrinol Metab.* 2012;97(9):2990-3011. [doi:10.1210/jc.2012-1174](https://doi.org/10.1210/jc.2012-1174) · [PubMed 22392070](https://pubmed.ncbi.nlm.nih.gov/22392070/)
[^chandrasekharappa-1997-men1]: Chandrasekharappa SC, Guru SC, Manickam P, et al. Positional cloning of the gene for multiple endocrine neoplasia-type 1. *Science.* 1997;276(5311):404-407. [doi:10.1126/science.276.5311.404](https://doi.org/10.1126/science.276.5311.404) · [PubMed 9103196](https://pubmed.ncbi.nlm.nih.gov/9103196/)
