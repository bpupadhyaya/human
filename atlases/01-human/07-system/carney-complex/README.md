---
schema: human-scale-entry/v1
id: carney-complex
name: Carney Complex
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Carney complex is caused by germline PRKAR1A mutations; spotty skin pigmentation, cardiac myxomas, primary pigmented nodular adrenocortical disease (PPNAD) causing Cushing syndrome, pituitary GH adenomas, and Sertoli cell tumors; annual cardiac MRI surveillance."
aliases: ["Carney complex", "PRKAR1A syndrome", "CNC", "Carney PPNAD", "Carney cardiac myxoma", "Carney Cushing", "PPNAD hereditary", "Carney lentiginosis", "Carney complex PRKAR1A"]
sources:
  - id: bertherat-2009-carney
    type: peer-reviewed
    cite: "Bertherat J, Horvath A, Groussin L, et al. Mutations in regulatory subunit type 1A of cyclic adenosine 5'-monophosphate-dependent protein kinase (PRKAR1A): phenotype analysis in 353 patients and 80 different genotypes. J Clin Endocrinol Metab. 2009;94(6):2085-2091."
    doi: "10.1210/jc.2008-2333"
    pmid: "19293268"
    url: "https://doi.org/10.1210/jc.2008-2333"
  - id: kirschner-2000-prkar1a
    type: peer-reviewed
    cite: "Kirschner LS, Carney JA, Pack SD, et al. Mutations of the gene encoding the protein kinase A type I-alpha regulatory subunit in patients with the Carney complex. Nat Genet. 2000;26(1):89-92."
    doi: "10.1038/79238"
    pmid: "10973256"
    url: "https://doi.org/10.1038/79238"
cross_links:
  - target: 01-human/03-molecular/prkar1a
    relation: connects-to
    note: "PRKAR1A R1α sequesters PKA catalytic subunit; cAMP → R1α release → PKA active → steroidogenesis and proliferation; germline PRKAR1A LOF → constitutive PKA → PPNAD, cardiac myxomas, LCCSCT; paradoxical dexamethasone stimulation of cortisol is hallmark of PPNAD."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "PPNAD causes ACTH-independent Cushing syndrome; bilateral adrenocortical micronodular hyperplasia with black pigmented nodules → autonomous cortisol overproduction; paradoxical cortisol increase with low-dose dexamethasone (Liddle test); bilateral adrenalectomy curative."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Pituitary GH-secreting adenomas (acromegaly) occur in ~10-12% of Carney complex patients; thyroid adenomas and carcinomas are reported; testicular large-cell calcifying Sertoli cell tumors (LCCSCT) are sex cord stromal tumors; all driven by PKA-mediated proliferation."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Rare PRKAR1A germline carriers develop pheochromocytoma; some Carney complex patients have pheo as an isolated or combined manifestation; pheo evaluation (plasma free metanephrines, 24h urine) recommended in Carney complex surveillance; most pheo in Carney complex are benign."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Cardiac myxomas are the primary cause of mortality in Carney complex; CNC myxomas are multifocal and recur after resection (~20% vs <5% sporadic); complications include systemic embolism, mitral obstruction, and sudden death; annual echocardiographic surveillance is mandatory."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "PPNAD causes ACTH-independent Cushing via constitutive PKA in bilateral adrenocortical micronodular hyperplasia; paradoxical cortisol rise with low-dose dexamethasone distinguishes PPNAD from ACTH-dependent disease; bilateral adrenalectomy is curative with lifelong replacement."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "GH-secreting pituitary adenomas (acromegaly) in ~10-12% of CNC patients; IGF-1 is the annual screening biomarker; elevated IGF-1 → pituitary MRI; somatostatin receptor ligands or pegvisomant treat GH excess; PKA-mediated proliferation drives CNC somato-mammotroph adenomas."
---

# Carney Complex

## Overview

**Carney complex (CNC)** is a rare autosomal dominant multiple endocrine neoplasia and myxomatosis syndrome caused predominantly by germline pathogenic variants in **PRKAR1A** (chromosome 17q24.2; ~70% of CNC) or, less commonly, by alterations at chromosome 2p16 (CNC2 locus; gene unknown; ~30%). Carney complex was defined by J. Aidan Carney in 1985 as the combination of **spotty skin pigmentation** (lentigines and blue nevi), **cardiac and cutaneous myxomas**, and **endocrine hyperactivity**. The primary endocrine manifestations include **primary pigmented nodular adrenocortical disease (PPNAD)** — the most common cause of ACTH-independent Cushing syndrome in children and young adults — as well as **GH-secreting pituitary adenomas** (acromegaly) and **testicular large-cell calcifying Sertoli cell tumors (LCCSCT)**. Carney complex affects approximately **1 in 1,000,000** individuals; the small number of affected individuals globally contrasts with high clinical impact because cardiac myxomas are life-threatening if undetected [^bertherat-2009-carney] [^kirschner-2000-prkar1a].

**Carney complex diagnostic criteria (Stratakis 2001; requires ≥2 major criteria OR 1 major + genetic confirmation):**

**Major criteria:**
1. Spotty skin pigmentation (lentigines, blue nevi) — particularly of lips, conjunctivae, inner/outer canthi
2. Myxoma (cardiac, cutaneous, or mucosal)
3. Breast myxomatosis or fat necrosis on imaging
4. Primary pigmented nodular adrenocortical disease (PPNAD, by biopsy or imaging)
5. Acromegaly due to GH-producing pituitary adenoma
6. Large-cell calcifying Sertoli cell tumor (LCCSCT) or testicular calcification
7. Thyroid carcinoma or adenoma on imaging
8. Melanotic schwannoma
9. Blue nevus (epithelioid blue nevus)
10. Ductal adenoma of the breast
11. First-degree relative with Carney complex
12. Inactivating mutation of PRKAR1A (confirmed)

## Structure

### Genetic basis

**PRKAR1A (17q24.2):**
- 11 coding exons; 381 aa; encodes R1α regulatory subunit of PKA type I
- Germline pathogenic variants: frameshift (~40%), nonsense (~25%), splice (~15%), missense (~15%), large deletions (~5%)
- Most variants cause haploinsufficiency via nonsense-mediated mRNA decay (NMD); protein is absent or reduced
- De novo rate: ~30% of Carney complex patients; no family history
- Penetrance: essentially complete for some features (lentigines in >90% of carriers by age 20); PPNAD ~25-50%; cardiac myxoma ~20-30% lifetime; LCCSCT ~33% of males; GH adenoma ~10%

**CNC2 locus (2p16):**
- Gene not identified as of 2025; linked in families without PRKAR1A mutation; may harbor a second PKA pathway regulatory gene
- Clinically indistinguishable from PRKAR1A-CNC; same management

**Relationship to sporadic adrenocortical pathology:**
PRKAR1A somatic LOH occurs in ~15-20% of sporadic adrenocortical adenomas and carcinomas. Somatic gain-of-function PRKACA mutations (L206R) cause the same ACTH-independent Cushing syndrome as PPNAD in sporadic cortisol-producing adenomas, establishing the PKA pathway as the central driver of adrenocortical autonomous cortisol secretion.

## Function

### Clinical manifestations

**Spotty skin pigmentation:**
- Lentigines: small (1-5 mm), flat, dark brown hyperpigmented macules; appear on sun-exposed AND non-sun-exposed areas; lips (characteristic location), periorbital skin, conjunctivae, inner/outer canthi, sclera; facial lentigines may fade after puberty; distinct from common freckles (freckles appear at sun-exposed sites only)
- Blue nevi: dermal melanocytic nevi with blue-gray color due to deep dermal melanin; epithelioid blue nevi on Carney complex → pathognomonic histological finding
- Differentiation from Peutz-Jeghers (STK11 germline): Peutz-Jeghers lentigines appear on lips/buccal mucosa/fingers — overlap with CNC; Peutz-Jeghers has GI hamartomas, CNC has myxomas/PPNAD → clinical and molecular distinction required

**Cardiac myxomas:**
- Most dangerous Carney complex manifestation; **the primary cause of morbidity and mortality**
- Location: predominantly left atrium (atrial septum); may occur in right atrium, right or left ventricle, or be multifocal/bilateral; CNC myxomas are more often multifocal and recur after resection compared to sporadic myxomas
- Sporadic cardiac myxoma: single, left atrial, peak 50s-60s, females > males
- CNC cardiac myxoma: recurrent (after resection), multifocal/bilateral, younger age (teens-30s); any chamber; recurrence rate after resection ~20% in CNC vs <5% sporadic
- Complications: systemic embolism (stroke, limb ischemia from friable tumor fragments); mitral valve obstruction → heart failure; arrhythmia; sudden death
- Surveillance: annual echocardiogram (transthoracic) from diagnosis; MRI for anatomic detail before surgery
- Treatment: surgical excision; pericardium/myocardium sacrifice may be needed for multiply recurrent lesions

**Cutaneous and other myxomas:**
- Cutaneous myxomas: soft, pedunculated or flat, translucent papules/nodules; eyelid, external ear canal, nipple, trunk; detected by clinical exam; histology: paucicellular loose myxoid stroma with stellate fibroblasts; not premalignant but cosmetically significant
- Oral mucosal myxomas: palate, tongue; common
- Breast myxomatosis: bilateral stippled myxoid areas in breast stroma on ultrasound/mammography; distinct from myxoid fibroadenoma; may appear as ductal adenoma on biopsy

**PPNAD (Primary Pigmented Nodular Adrenocortical Disease):**
- ACTH-independent Cushing syndrome: most common endocrine manifestation of CNC; typically young adults (teens-30s); less common in children
- Bilateral adrenocortical disease: small (1-3 mm) black/brown pigmented cortical nodules separated by atrophic internodular cortex; bilateral but asymmetric; CT may appear normal (nodules are small) or show bilateral micronodularity
- Paradoxical response to dexamethasone (Liddle test): hallmark of PPNAD — cortisol INCREASES with low-dose dexamethasone (1 mg overnight or 2-day low-dose) due to constitutive PKA activation in nodular cells that paradoxically respond to GR-mediated signals; this distinguishes PPNAD from ACTH-dependent Cushing disease
- Cyclic Cushing syndrome: PPNAD can present with intermittent cortisol excess (cyclic), making biochemical diagnosis challenging; multiple 24h urine cortisol measurements required
- Treatment: bilateral adrenalectomy (definitive); requires lifelong glucocorticoid + mineralocorticoid replacement; unilateral adrenalectomy leads to recurrence in the contralateral gland

**Pituitary GH adenoma:**
- Acromegaly in ~10-12% of CNC patients; onset teens-30s; often somatostatin-producing tumors (somato-mammotroph); less commonly pure GH or prolactin-producing
- Treatment: transsphenoidal surgery; somatostatin receptor ligands (octreotide, lanreotide); pegvisomant (GH receptor antagonist); radiotherapy if medical therapy fails
- Screening: IGF-1 levels annually; MRI pituitary at diagnosis and every 3-5 years if no known adenoma

**Testicular LCCSCT:**
- Large-cell calcifying Sertoli cell tumor: scrotal ultrasound detects hyperechoic calcified intratesticular masses; present in ~33% of male CNC patients; usually bilateral (10% bilateral); appear in teens/young adults
- Biology: benign (>90%); may elaborate estrogens → gynecomastia, accelerated bone age; malignant transformation rare (bilateral; >3 cm; older age)
- Treatment: observation (if bilateral benign tumors, avoid orchidectomy → preserve hormonal function); orchidectomy if unilateral or malignant transformation suspected

**Melanotic schwannoma:**
- Pigmented (melanin-containing) schwannoma; most commonly spinal; can be located paraspinally, gastrointestinal (omentum), sympathetic chain; ~10% of CNC patients
- Features: psammomatous bodies; melanin pigment; nuclear atypia; locally aggressive; ~15% have malignant behavior (metastasis); distinct from conventional schwannoma which is entirely benign
- Treatment: surgical excision; adjuvant RT if incomplete resection of malignant variant

## Pathology

### Surveillance and management

**Annual assessments:**
- **Echocardiography** (transthoracic; cardiac myxoma detection): annually from diagnosis; lifelong
- **Endocrine screen**: 24h urine free cortisol × 2 (PPNAD); IGF-1 (pituitary GH adenoma); testosterone + estradiol + LH/FSH (LCCSCT)
- **Scrotal ultrasound** (males): annually from puberty (LCCSCT)
- **Pituitary MRI**: at diagnosis; every 3-5 years if no adenoma; more frequent if IGF-1 elevated
- **Thyroid ultrasound**: annually (thyroid adenoma/DTC)
- **Full-skin examination**: annually

**Genetic testing:**
- PRKAR1A sequencing + MLPA (large deletions): first-line; ~70% CNC yield
- If negative: 2p16 locus testing (research setting); next-gen panel for second-tier
- Cascade testing: 50% risk to first-degree relatives; test before or at puberty
- Prenatal/preimplantation testing: available for PRKAR1A pathogenic variants

**Prognosis:**
- Cardiac myxoma: major mortality risk; most deaths in untreated patients; excellent prognosis with surveillance and timely surgical resection
- PPNAD-Cushing: high morbidity if untreated (metabolic syndrome, cardiovascular, osteoporotic fractures); excellent after bilateral adrenalectomy (Addisonian state managed with replacement)
- LCCSCT: excellent prognosis (>90% benign); fertility preservation with testis-sparing approach

**Carney complex vs. MEN1 vs. McCune-Albright — quick comparison:**

| Feature | Carney Complex | MEN1 | McCune-Albright |
|---|---|---|---|
| Gene | PRKAR1A (AD) | MEN1 (AD) | GNAS (mosaic somatic) |
| Pituitary | GH adenoma | Any (PRL, GH, non-functioning) | GH/PRL excess |
| Adrenal | PPNAD (bilateral micronodular) | Cortical tumors (rare) | Bilateral macro-nodular |
| Parathyroid | Normal | >95% hyperplasia/adenoma | Rarely |
| Skin | Lentigines, blue nevi | Lipomas, angiofibromas | Café-au-lait (irregular) |
| Cardiac | Myxoma (life-threatening) | Not characteristic | Not characteristic |

## Connections

- `connects-to` → **[PRKAR1A](../../03-molecular/prkar1a/README.md)** — PRKAR1A R1α sequesters PKA catalytic subunit; cAMP → R1α release → PKA active → steroidogenesis and proliferation; germline PRKAR1A LOF → constitutive PKA → PPNAD, cardiac myxomas, LCCSCT; paradoxical dexamethasone stimulation of cortisol is hallmark of PPNAD.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — PPNAD causes ACTH-independent Cushing syndrome; bilateral adrenocortical micronodular hyperplasia with black pigmented nodules → autonomous cortisol overproduction; paradoxical cortisol increase with low-dose dexamethasone (Liddle test); bilateral adrenalectomy curative.
- `connects-to` → **[Neuroendocrine Tumors](../../07-system/neuroendocrine-tumors/README.md)** — Pituitary GH-secreting adenomas (acromegaly) occur in ~10-12% of Carney complex patients; thyroid adenomas and carcinomas are reported; testicular large-cell calcifying Sertoli cell tumors (LCCSCT) are sex cord stromal tumors; all driven by PKA-mediated proliferation.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../../07-system/pheochromocytoma-paraganglioma/README.md)** — Rare PRKAR1A germline carriers develop pheochromocytoma; some Carney complex patients have pheo as an isolated or combined manifestation; pheo evaluation (plasma free metanephrines, 24h urine) recommended in Carney complex surveillance; most pheo in Carney complex are benign.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — cardiac myxomas are the primary cause of mortality in Carney complex; CNC myxomas are multifocal and recur after resection (~20% vs <5% sporadic); complications include systemic embolism, mitral obstruction, and sudden death; annual echocardiographic surveillance is mandatory.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — PPNAD causes ACTH-independent Cushing via constitutive PKA in bilateral adrenocortical micronodular hyperplasia; paradoxical cortisol rise with low-dose dexamethasone distinguishes PPNAD from ACTH-dependent disease; bilateral adrenalectomy is curative with lifelong replacement.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — GH-secreting pituitary adenomas (acromegaly) in ~10-12% of CNC patients; IGF-1 is the annual screening biomarker; elevated IGF-1 → pituitary MRI; somatostatin receptor ligands or pegvisomant treat GH excess; PKA-mediated proliferation drives CNC somato-mammotroph adenomas.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^bertherat-2009-carney]: Bertherat J, Horvath A, Groussin L, et al. Mutations in regulatory subunit type 1A of cyclic adenosine 5'-monophosphate-dependent protein kinase (PRKAR1A): phenotype analysis in 353 patients and 80 different genotypes. *J Clin Endocrinol Metab.* 2009;94(6):2085-2091. [doi:10.1210/jc.2008-2333](https://doi.org/10.1210/jc.2008-2333) · [PubMed 19293268](https://pubmed.ncbi.nlm.nih.gov/19293268/)
[^kirschner-2000-prkar1a]: Kirschner LS, Carney JA, Pack SD, et al. Mutations of the gene encoding the protein kinase A type I-alpha regulatory subunit in patients with the Carney complex. *Nat Genet.* 2000;26(1):89-92. [doi:10.1038/79238](https://doi.org/10.1038/79238) · [PubMed 10973256](https://pubmed.ncbi.nlm.nih.gov/10973256/)
