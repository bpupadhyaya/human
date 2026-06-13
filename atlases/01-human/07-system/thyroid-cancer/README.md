---
schema: human-scale-entry/v1
id: thyroid-cancer
name: Thyroid Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Malignant thyroid tumors: papillary (BRAF V600E ~60%, RET/PTC fusions ~20%), follicular, medullary (RET mutation MEN2), and anaplastic; differentiated thyroid cancer treated with RAI and lenvatinib/sorafenib; RET-mutant MTC → selpercatinib; BRAF+ ATC → dabrafenib+trametinib."
aliases: ["thyroid cancer", "thyroid carcinoma", "papillary thyroid carcinoma", "medullary thyroid carcinoma", "anaplastic thyroid carcinoma", "differentiated thyroid cancer", "PTC", "MTC", "ATC", "DTC"]
sources:
  - id: schlumberger-2015-lenvatinib
    type: peer-reviewed
    cite: "Schlumberger M, Tahara M, Wirth LJ, et al. Lenvatinib versus placebo in radioiodine-refractory differentiated thyroid cancer. N Engl J Med. 2015;372(7):621-630."
    doi: "10.1056/NEJMoa1406470"
    pmid: "25671254"
    url: "https://doi.org/10.1056/NEJMoa1406470"
  - id: subbiah-2018-atc-dabrafenib
    type: peer-reviewed
    cite: "Subbiah V, Kreitman RJ, Wainberg ZA, et al. Dabrafenib and trametinib treatment in patients with locally advanced or metastatic BRAF V600-mutant anaplastic thyroid cancer. J Clin Oncol. 2018;36(1):7-13."
    doi: "10.1200/JCO.2017.73.6785"
    pmid: "28892432"
    url: "https://doi.org/10.1200/JCO.2017.73.6785"
cross_links:
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E in ~60% of papillary thyroid carcinoma → ERK activation → dedifferentiation → radioiodine resistance; dabrafenib+trametinib approved for BRAF V600E-mutant ATC (2018, first targeted therapy for ATC); vemurafenib+cobimetinib in radioiodine-refractory DTC under study."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Differentiated thyroid cancer is highly vascular; VEGF and VEGFR2 overexpressed in PTC and FTC → promotes metastasis; lenvatinib (multikinase: VEGFR1-3, RET, FGFR, PDGFRβ) approved for RAI-refractory DTC; sorafenib (VEGFR2/3 + BRAF + RET) also approved for RAI-refractory DTC."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PTEN loss and PIK3CA mutations activate mTOR in follicular thyroid carcinoma and ATC; everolimus (mTORC1 inhibitor) studied in RAI-refractory DTC; mTOR pathway activation mediates resistance to VEGFR-targeted TKIs (lenvatinib, sorafenib) in DTC → mTOR combination strategies."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-L1 expressed in ~30-50% of papillary and ~50-70% of anaplastic thyroid carcinoma → T cell exclusion; pembrolizumab studied with lenvatinib for RAI-refractory DTC and ATC; spartalizumab + dabrafenib+trametinib in BRAF+ ATC; anti-PD-1 active in radioiodine-refractory DTC."
  - target: 01-human/03-molecular/ret
    relation: connects-to
    note: "RET drives the C-cell lineage of thyroid cancer: germline RET mutations cause MEN2 medullary thyroid carcinoma, somatic RET ~40% of sporadic MTC, and RET/PTC fusions ~20% of papillary cancer; selective RET inhibitors selpercatinib and pralsetinib are highly active."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Differentiated thyroid cancers retain the sodium-iodide symporter (NIS), letting them concentrate radioiodine (I-131) whose beta emission ablates tumor — a targeted therapy; BRAF V600E silences NIS, causing radioiodine refractoriness that MEK inhibitors can partly reverse."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Medullary thyroid carcinoma arises from calcitonin-secreting C cells, so serum calcitonin (and CEA) is both a screen before thyroid surgery and the key tumor marker afterward; a calcitonin doubling time under 6 months signals aggressive disease and prompts early systemic therapy."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Medullary thyroid carcinoma is a neuroendocrine tumor: it arises from calcitonin-secreting parafollicular C cells (neural-crest-derived), not iodine-handling follicular cells, so it ignores radioiodine and is tracked by calcitonin/CEA — closer to other NETs than papillary cancer."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "FAP confers a distinctive thyroid risk: cribriform-morular thyroid carcinoma, a rare papillary variant occurring almost exclusively in young women with germline APC mutations, can be the presenting sign of undiagnosed FAP — prompting colonoscopy and APC testing."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunotherapy is reshaping the worst thyroid cancers: anaplastic and radioiodine-refractory tumors express PD-L1 and exclude cytotoxic T cells, so anti-PD-1 (pembrolizumab), often with lenvatinib or BRAF/MEK inhibitors, reactivates CD8+ killing in these rapidly fatal cancers."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Medullary thyroid carcinoma and pheochromocytoma are the linked tumors of MEN2: a germline RET mutation drives both, so a patient with medullary thyroid cancer must be screened for pheochromocytoma before any surgery to avoid an intraoperative hypertensive crisis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Thyroid cancer is the commonest endocrine malignancy: most are differentiated (papillary/follicular) tumors of iodine-avid follicular cells curable with surgery and radioiodine, while medullary (C-cell, calcitonin) and anaplastic types behave very differently."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Cowden syndrome is a hereditary cause of thyroid cancer: germline PTEN loss unleashes PI3K/mTOR signaling, predisposing to follicular thyroid carcinoma alongside breast and endometrial cancer, so multinodular goiter in a Cowden patient warrants close thyroid surveillance."
---

# Thyroid Cancer

## Overview

**Thyroid cancer** encompasses a spectrum of malignancies arising from follicular epithelial cells (papillary, follicular, Hürthle cell, anaplastic) or parafollicular C cells (medullary). The majority (~90%) are **well-differentiated thyroid cancers (DTC)** — papillary (PTC) and follicular (FTC) — with excellent prognosis: 10-year survival >95% for low-risk PTC. In sharp contrast, **anaplastic thyroid carcinoma (ATC)** is one of the most lethal solid tumors, with median OS of 3-7 months. The molecular landscape of each histotype is now well-characterized, enabling targeted therapy for advanced/refractory disease [^schlumberger-2015-lenvatinib].

**Epidemiology:**
- ~43,000 new cases/year in the United States; most common endocrine malignancy
- 3:1 female predominance (follicular-derived cancers); no sex predilection in MTC
- Incidence rising (largely due to detection of small papillary cancers on imaging)
- Risk factors: ionizing radiation (especially childhood cranial/neck RT), iodine deficiency (FTC), obesity (PTC), family history; MEN2 for MTC (RET germline)

**Histological classification:**

| Type | Frequency | Cell of origin | Molecular drivers | 10-yr survival |
|------|-----------|---------------|-------------------|----------------|
| Papillary (PTC) | ~80% | Follicular epithelium | BRAF V600E (~60%), RET/PTC fusions (~20%), RAS mutations (~10%) | >95% (intrathyroidal) |
| Follicular (FTC) | ~10% | Follicular epithelium | RAS mutations (~50%), PAX8-PPARγ fusion (~30%), PIK3CA/PTEN | ~85% |
| Hürthle cell | ~3% | Oncocytic follicular cell | mtDNA mutations, TERT, NF2 | ~75% |
| Medullary (MTC) | ~4% | C cell (calcitonin) | RET mutation (germline MEN2 ~25%; somatic ~40%), RAS | ~80% |
| Anaplastic (ATC) | ~2% | Dedifferentiated | BRAF V600E (~50%), TP53 (~70%), TERT, PIK3CA, NF1 | ~10% at 1 year |
| Poorly differentiated (PDTC) | ~1-2% | Follicular | TERT (~50%), BRAF, RAS, TP53 | ~50% at 5yr |

## Structure

### Thyroid gland architecture

**Follicular cells:**
- Cuboidal-to-columnar epithelial cells surrounding thyroid follicles containing colloid (thyroglobulin)
- Function: thyroglobulin synthesis → iodination → T3/T4 production → secretion (TSH-dependent)
- Express NIS (Na/I symporter) → iodide uptake → basis for radioiodine (RAI) therapy in DTC
- TSH receptor (TSHR) → cAMP → thyroglobulin synthesis and NIS expression → RAI uptake

**C cells (parafollicular cells):**
- Derived from neural crest; ~0.1% of thyroid cells
- Secrete calcitonin (serum calcitonin → MTC biomarker and monitoring tool)
- RET expression in normal C cells → GDNF-GFRα → C cell survival

### Molecular landscape by histotype

**Papillary thyroid carcinoma (PTC):**
- **BRAF V600E (~60%):** MAPK activation without RAS involvement; associated with aggressive features (extrathyroidal extension, lymph node metastasis), higher recurrence, and radioiodine refractoriness; standard BRAF+ PTC treated with RAI still unless refractory
- **RET/PTC fusions (~20%):** RET/PTC1 (CCDC6-RET), RET/PTC3 (NCOA4-RET); enriched in radiation-associated PTC; generally favorable prognosis; targetable with selpercatinib
- **RAS mutations (~10%):** NRAS Q61R/K most common; associated with less aggressive PTC; also seen in FTC
- **TERT promoter mutation:** C228T/C250T; associated with older age, larger tumor, and poor prognosis when co-occurring with BRAF V600E (BRAF + TERT co-mutation → significantly higher recurrence and mortality)
- **NTRKfusions (~1-2%):** NTRK1/3 fusions; targetable with larotrectinib/entrectinib

**Follicular thyroid carcinoma (FTC):**
- RAS mutations (NRAS Q61, HRAS Q61, KRAS): Common; FTC biologically distinct from PTC → hematogenous metastasis (bone, lung) > lymph node
- PAX8-PPARγ rearrangement (~30%): t(2;3) → fusion oncoprotein; dominant negative for PPARγ tumor suppressor; minimally invasive FTC with good prognosis
- PTEN/PIK3CA mutations: PI3K-AKT-mTOR pathway activation; associated with more aggressive FTC

**Anaplastic thyroid carcinoma (ATC):**
- Likely dedifferentiated from preexisting PTC (BRAF+ ATC) or FTC/PDTC (RAS+ ATC)
- BRAF V600E (~45-50%): targetable — the discovery that led to the first ATC targeted therapy approval [^subbiah-2018-atc-dabrafenib]
- TP53 mutation (~70%): loss of p53 checkpoint → rapid progression
- TERT promoter (~50%), PIK3CA (~20%), NF1 (~15%), CDKN2A deletion (~40%)
- Co-occurring with PTC/FTC elements in the same specimen → confirms dedifferentiation pathway

## Function

### Thyroid hormone biosynthesis and cancer biology

**Normal thyroid function:**
TSH → TSHR → adenylyl cyclase → cAMP → PKA → (1) NIS expression and thyroglobulin synthesis, (2) T3/T4 synthesis and secretion. Differentiated thyroid cancers partially retain this axis — the basis for TSH suppression (levothyroxine) and RAI therapy.

**Radioiodine (RAI) therapy mechanism:**
DTC cells retain NIS expression → concentrate iodine-131 → beta emission → DNA double-strand breaks → tumor cell death. RAI is effective in metastatic DTC with NIS expression. BRAF V600E → MAPK → transcriptional downregulation of NIS, pendrin, and thyroglobulin → RAI refractoriness. MEK inhibitors (selumetinib) can restore RAI uptake in BRAF-mutant DTC (ASTRA trial).

**TSH-driven growth:**
Elevated TSH → TSHR → proliferation of thyroid cancer cells; TSH suppression (levothyraxine to TSH <0.1 mU/L) slows DTC growth — a pillar of post-thyroidectomy management in high-risk DTC.

## Pathology

### Diagnosis and staging

**Initial workup:**
- Thyroid ultrasound: size, composition, calcifications, lymphadenopathy (ACR TI-RADS, ATA sonographic risk classification)
- Fine needle aspiration (FNA) biopsy: Bethesda system reporting (I-VI); Bethesda IV/V/VI → thyroidectomy; Bethesda III/IV → molecular testing (ThyroSeq, Afirma GSC) to guide surgery
- Serum calcitonin: screen for MTC before thyroid surgery; baseline monitoring post-thyroidectomy
- CEA: MTC marker; elevated CEA with normal calcitonin → aggressive dedifferentiated MTC
- Genetic testing: RET germline testing in all MTC patients; if positive → screen family members

**TNM staging (AJCC 8th edition):**
- All differentiated thyroid cancers: age ≥55 at diagnosis → more aggressive staging (reflects biology)
- PTC/FTC ≥55: pT3-T4/N1/M1 → stage III-IV; <55 → even M1 disease = stage II
- MTC: standard TNM; calcitonin doubling time predicts survival

**Surveillance post-thyroidectomy (DTC):**
- Stimulated thyroglobulin (sTg) + anti-Tg antibody: Biochemical disease detection
- RAI whole-body scan (post-remnant ablation): Anatomic disease localization
- Neck ultrasound at 6-12 months: structural recurrence
- Response-adapted follow-up: Excellent response (suppressed Tg undetectable, negative imaging) → decreasing surveillance intensity

### Treatment

**Differentiated thyroid cancer (DTC):**

*Surgery:*
- Total thyroidectomy for tumors >1 cm, bilateral, aggressive features, or prior neck RT
- Hemithyroidectomy for unifocal T1 tumors (<4 cm) with low-risk features
- Prophylactic central neck dissection in high-risk PTC (controversial)

*Radioiodine adjuvant therapy:*
- Post-thyroidectomy RAI ablation for remnant thyroid and residual cancer
- Indications: high-risk features (T3/T4, N1, M1, aggressive histology)
- Preparation: thyroid hormone withdrawal (TSH stimulation) or recombinant TSH (Thyrogen)
- Activity: 30-100 mCi for remnant ablation; 100-200 mCi for high-risk/metastatic DTC

*RAI-refractory DTC (systemic therapy):*
- **Lenvatinib (SELECT trial):** PFS 18.3 vs. 3.6 months vs. placebo; 65% ORR; FDA approved 2015 for RAI-refractory DTC [^schlumberger-2015-lenvatinib]
- **Sorafenib (DECISION trial):** PFS 10.8 vs. 5.8 months; 12% ORR; approved 2013 for RAI-refractory DTC
- **Lenvatinib + pembrolizumab (LEAP-018):** Under investigation

*Targeted therapy for molecular alterations:*
- RET fusion/mutation → selpercatinib or pralsetinib (LIBRETTO-001)
- NTRK fusion → larotrectinib or entrectinib (basket trials)
- BRAF V600E (non-ATC DTC refractory) → dabrafenib+trametinib or vemurafenib+cobimetinib

**Medullary thyroid carcinoma (MTC):**

*Surgery:*
- Total thyroidectomy + bilateral central neck dissection; lateral neck dissection if N1b
- MEN2B → prophylactic thyroidectomy in neonatal period
- Prophylactic adrenalectomy for pheochromocytoma before thyroid surgery (pheo must be treated first)

*Systemic therapy (advanced MTC):*
- **Vandetanib (ZETA trial):** PFS 30.5 vs. 19.3 months; ORR 45%; approved 2011 [^wells-2012-vandetanib reference — indirectly, via RET entry]
- **Cabozantinib (EXAM trial):** PFS 7.2 vs. 4.0 months; active after vandetanib
- **Selpercatinib (LIBRETTO-001):** ORR 69% in pretreated RET-mutant MTC; 73% treatment-naive; now preferred first-line selective option for RET-mutant MTC
- **Pralsetinib (ARROW trial):** ORR 60% pretreated; alternative to selpercatinib

*Calcitonin monitoring:*
Calcitonin doubling time <6 months → poor prognosis → early systemic therapy; CEA doubling time provides independent prognostic information

**Anaplastic thyroid carcinoma (ATC):**
- **BRAF V600E (~50% of ATC):** Dabrafenib (BRAF inhibitor) + trametinib (MEK inhibitor); ORR 69%; 1-year OS 80% in BRAF+ ATC vs. historical ~5%; FDA approved 2018 [^subbiah-2018-atc-dabrafenib]
- **BRAF wild-type ATC:** No targeted therapy; may use pembrolizumab ± lenvatinib; clinical trial strongly recommended
- Multimodal approach: surgery (if feasible) + RT + systemic therapy; IMRT for unresectable local disease
- Immunotherapy: Pembrolizumab alone (~12% ORR in ATC); higher responses in combination

## Connections

- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E in ~60% of papillary thyroid carcinoma → ERK activation → dedifferentiation → radioiodine resistance; dabrafenib+trametinib approved for BRAF V600E-mutant ATC (2018, first targeted therapy for ATC); vemurafenib+cobimetinib in radioiodine-refractory DTC under study.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Differentiated thyroid cancer is highly vascular; VEGF and VEGFR2 overexpressed in PTC and FTC → promotes metastasis; lenvatinib (multikinase: VEGFR1-3, RET, FGFR, PDGFRβ) approved for RAI-refractory DTC; sorafenib (VEGFR2/3 + BRAF + RET) also approved for RAI-refractory DTC.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PTEN loss and PIK3CA mutations activate mTOR in follicular thyroid carcinoma and ATC; everolimus (mTORC1 inhibitor) studied in RAI-refractory DTC; mTOR pathway activation mediates resistance to VEGFR-targeted TKIs (lenvatinib, sorafenib) in DTC → mTOR combination strategies.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-L1 expressed in ~30-50% of papillary and ~50-70% of anaplastic thyroid carcinoma → T cell exclusion; pembrolizumab studied with lenvatinib for RAI-refractory DTC and ATC; spartalizumab + dabrafenib+trametinib in BRAF+ ATC; anti-PD-1 active in radioiodine-refractory DTC.
- `connects-to` → **[RET](../../03-molecular/ret/README.md)** — RET drives the C-cell lineage of thyroid cancer: germline RET mutations cause MEN2 medullary thyroid carcinoma, somatic RET ~40% of sporadic MTC, and RET/PTC fusions ~20% of papillary cancer; selective RET inhibitors selpercatinib and pralsetinib are highly active.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Differentiated thyroid cancers retain the sodium-iodide symporter (NIS), letting them concentrate radioiodine (I-131) whose beta emission ablates tumor — a targeted therapy; BRAF V600E silences NIS, causing radioiodine refractoriness that MEK inhibitors can partly reverse.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Medullary thyroid carcinoma arises from calcitonin-secreting C cells, so serum calcitonin (and CEA) is both a screen before thyroid surgery and the key tumor marker afterward; a calcitonin doubling time under 6 months signals aggressive disease and prompts early systemic therapy.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Medullary thyroid carcinoma is a neuroendocrine tumor: it arises from calcitonin-secreting parafollicular C cells (neural-crest-derived), not iodine-handling follicular cells, so it ignores radioiodine and is tracked by calcitonin/CEA — closer to other NETs than papillary cancer.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — FAP confers a distinctive thyroid risk: cribriform-morular thyroid carcinoma, a rare papillary variant occurring almost exclusively in young women with germline APC mutations, can be the presenting sign of undiagnosed FAP — prompting colonoscopy and APC testing.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunotherapy is reshaping the worst thyroid cancers: anaplastic and radioiodine-refractory tumors express PD-L1 and exclude cytotoxic T cells, so anti-PD-1 (pembrolizumab), often with lenvatinib or BRAF/MEK inhibitors, reactivates CD8+ killing in these rapidly fatal cancers.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Medullary thyroid carcinoma and pheochromocytoma are the linked tumors of MEN2: a germline RET mutation drives both, so a patient with medullary thyroid cancer must be screened for pheochromocytoma before any surgery to avoid an intraoperative hypertensive crisis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Thyroid cancer is the commonest endocrine malignancy: most are differentiated (papillary/follicular) tumors of iodine-avid follicular cells curable with surgery and radioiodine, while medullary (C-cell, calcitonin) and anaplastic types behave very differently.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Cowden syndrome is a hereditary cause of thyroid cancer: germline PTEN loss unleashes PI3K/mTOR signaling, predisposing to follicular thyroid carcinoma alongside breast and endometrial cancer, so multinodular goiter in a Cowden patient warrants close thyroid surveillance.

[^schlumberger-2015-lenvatinib]: Schlumberger M, Tahara M, Wirth LJ, et al. Lenvatinib versus placebo in radioiodine-refractory differentiated thyroid cancer. *N Engl J Med.* 2015;372(7):621-630. [doi:10.1056/NEJMoa1406470](https://doi.org/10.1056/NEJMoa1406470) · [PubMed 25671254](https://pubmed.ncbi.nlm.nih.gov/25671254/)
[^subbiah-2018-atc-dabrafenib]: Subbiah V, Kreitman RJ, Wainberg ZA, et al. Dabrafenib and trametinib treatment in patients with locally advanced or metastatic BRAF V600-mutant anaplastic thyroid cancer. *J Clin Oncol.* 2018;36(1):7-13. [doi:10.1200/JCO.2017.73.6785](https://doi.org/10.1200/JCO.2017.73.6785) · [PubMed 28892432](https://pubmed.ncbi.nlm.nih.gov/28892432/)
