---
schema: human-scale-entry/v1
id: nsclc
name: NSCLC
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common lung cancer subtype (~85%); adenocarcinoma (KRAS/EGFR/ALK drivers), squamous cell carcinoma, and large cell. EGFR TKIs (osimertinib) and ALK inhibitors (alectinib) are highly active; pembrolizumab + chemotherapy transforms KRAS/squamous disease."
aliases: ["non-small cell lung cancer", "lung adenocarcinoma", "squamous cell lung carcinoma", "LUAD", "LUSC", "lung cancer", "NSCLC adenocarcinoma"]
sources:
  - id: soria-2018-osimertinib-flaura
    type: peer-reviewed
    cite: "Soria JC, Ohe Y, Vansteenkiste J, et al. Osimertinib in untreated EGFR-mutated advanced non-small-cell lung cancer. N Engl J Med. 2018;378(2):113-125."
    doi: "10.1056/NEJMoa1713137"
    pmid: "29151359"
    url: "https://doi.org/10.1056/NEJMoa1713137"
  - id: reck-2016-pembrolizumab-keynote024
    type: peer-reviewed
    cite: "Reck M, Rodríguez-Abreu D, Robinson AG, et al. Pembrolizumab versus chemotherapy for PD-L1-positive non-small-cell lung cancer. N Engl J Med. 2016;375(19):1823-1833."
    doi: "10.1056/NEJMoa1606774"
    pmid: "27718347"
    url: "https://doi.org/10.1056/NEJMoa1606774"
  - id: halliday-2023-kras-nsclc
    type: peer-reviewed
    cite: "Riely GJ, Ou SHI, Rybkin I, et al. KRYSTAL-1: activity and preliminary pharmacodynamic (PD) analysis of adagrasib (MRTX849) in patients (Pts) with advanced/metastatic non-small cell lung cancer (NSCLC) harboring KRASG12C mutation. J Thorac Oncol. 2022;17(10):1248-1258."
    doi: "10.1016/j.jtho.2022.06.020"
    pmid: "35817313"
    url: "https://doi.org/10.1016/j.jtho.2022.06.020"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS G12C is the most common oncogenic driver in NSCLC adenocarcinoma (~13%); sotorasib (CodeBreaK-100) and adagrasib (KRYSTAL-1) are approved for KRAS G12C-mutant NSCLC; KRAS G12D and G12V — next-generation pan-KRAS and T cell-engaging approaches in clinical development."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR mutations (exon 19 del, L858R) drive 15-20% of NSCLC adenocarcinoma; osimertinib (FLAURA: PFS 18.9 vs. 10.2 months vs. erlotinib) is first-line; resistance via C797S and MET amplification; exon 20 insertions → amivantamab + lazertinib."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E occurs in ~2% of NSCLC adenocarcinoma; dabrafenib + trametinib (BRAF + MEK inhibition) approved for BRAF V600E-mutant NSCLC (ORR ~64%, PFS 14.6 months); non-V600E BRAF mutations require pan-RAF or ERK-directed approaches."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1/PD-L1 blockade transformed NSCLC: pembrolizumab is standard-of-care in PD-L1 ≥50% first-line (KEYNOTE-024: OS 26.3 vs. 13.8 months) and + chemotherapy in all-comers (KEYNOTE-189); atezolizumab, nivolumab, and durvalumab (post-CRT consolidation) are also approved."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "NSCLC is ~85% of lung cancer: squamous tumors arise centrally near the hilum (cough, hemoptysis) while adenocarcinomas arise peripherally and are often found incidentally; annual low-dose CT screening of heavy smokers cuts lung-cancer mortality ~20% (NLST)."
  - target: 01-human/03-molecular/alk
    relation: connects-to
    note: "ALK rearrangements (EML4-ALK, ~5-7%) define a distinct NSCLC of young never-smokers that is exquisitely targetable: alectinib and lorlatinib far outperform chemotherapy with strong CNS penetration for brain metastases; lorlatinib covers the G1202R resistance mutation."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "Lung adenocarcinoma arises from alveolar type II pneumocytes (and club cells), retaining their TTF-1 and napsin-A markers; it progresses through adenocarcinoma-in-situ → minimally invasive → invasive adenocarcinoma, the peripheral lepidic-to-solid sequence."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "NSCLC and melanoma are the twin proving grounds of checkpoint immunotherapy: both accumulate heavy carcinogen-driven mutational burdens (tobacco, UV) yielding neoantigens, so PD-1/PD-L1 (and CTLA-4) blockade gives durable responses in both, and both carry targetable BRAF V600E."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "NSCLC's response to immunotherapy hinges on cytotoxic T cells: a high tobacco-driven mutational burden generates neoantigens, and PD-1/PD-L1 blockade (pembrolizumab, first-line at PD-L1 ≥50%) reinvigorates exhausted CD8+ T cells — absent in never-smoker EGFR/ALK subsets."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "NSCLC and small-cell lung cancer are the two divisions of lung cancer: NSCLC (~85%, adeno/squamous) is driver-rich and often resectable or targetable, while SCLC is a fast neuroendocrine tumor of heavy smokers that disseminates early, is rarely operable, and is RB1/TP53-driven."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "NSCLC and mesothelioma are the two major thoracic cancers tied to inhaled carcinogens but distinct: NSCLC arises in lung parenchyma (smoking, EGFR/KRAS-driven), while mesothelioma arises from the pleura decades after asbestos exposure—different cells and treatment."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is central to NSCLC: stereotactic body photon radiotherapy can cure inoperable early-stage tumors, while conventional chemoradiation treats locally advanced disease—and consolidation immunotherapy after radiation now improves survival."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages shape the NSCLC microenvironment: M2-polarized macrophages suppress cytotoxic T cells and promote angiogenesis, contributing to immunotherapy resistance—so they are studied as both a biomarker and a target alongside PD-1 blockade."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain is a frequent NSCLC metastatic site: lung adenocarcinomas, especially EGFR/ALK-driven, commonly seed the brain, so staging includes brain MRI and CNS-penetrant targeted drugs (osimertinib, lorlatinib)—brain metastases strongly shape prognosis."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Carbon-based tobacco carcinogens are the dominant cause of NSCLC: smoke's PAHs and nitrosamines form DNA adducts that mutate KRAS and TP53, driving most squamous and many adenocarcinomas—though EGFR-mutant adenocarcinoma in never-smokers takes a distinct path."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "NSCLC and head and neck cancer share tobacco-driven field cancerization: carcinogens injure the whole aerodigestive tract, so smokers with one cancer face high risk of a second primary in the other—both demand smoking cessation and surveillance."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "MET is a targetable NSCLC driver: MET exon-14 skipping mutations and MET amplification drive a subset of non-small-cell lung cancers and confer resistance to EGFR inhibitors, so MET-directed drugs extend the precision-oncology toolkit beyond EGFR, ALK and KRAS."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal gland is a classic NSCLC metastatic site: lung cancer characteristically spreads to the adrenals (along with brain, bone and liver), so an adrenal mass in a lung-cancer patient demands staging workup—adrenal involvement often marks stage IV disease."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "NSCLC and COPD are linked by shared tobacco injury: smoking drives both, COPD independently raises lung-cancer risk through chronic inflammation, and the two coexist so often that emphysema complicates surgery and screening targets this overlapping high-risk population."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 is among the most mutated genes in NSCLC: smoking-driven DNA damage frequently inactivates p53, removing a key brake on the cell cycle and apoptosis, so its loss—often alongside KRAS—marks aggressive, treatment-resistant lung adenocarcinoma."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "NSCLC is the dominant cancer of the respiratory system: arising in bronchial and alveolar cells mostly from smoking, it accounts for ~85% of lung cancers and destroys lung function as it grows—the leading cause of cancer death worldwide."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "NSCLC staging hinges on the lymphatic system: spread to hilar and mediastinal lymph nodes (the N stage) determines whether disease is surgically curable, so nodal sampling by EBUS or mediastinoscopy is decisive in planning treatment."
---

# NSCLC

## Overview

**Non-small cell lung cancer (NSCLC)** accounts for **~85% of all lung cancers** and is the leading cause of cancer-related death globally, responsible for approximately 1.8 million deaths per year worldwide. It encompasses **three major histological subtypes** — adenocarcinoma, squamous cell carcinoma, and large cell carcinoma — unified by their non-neuroendocrine biology but with distinct molecular drivers and treatment strategies.

**Histological subtypes:**
- **Adenocarcinoma (LUAD, ~40% of NSCLC):** Peripheral lung; lepidic/acinar/micropapillary/solid and mucinous growth patterns; KRAS, EGFR, ALK, ROS1, RET, MET, BRAF V600E, NTRK1/2/3 drivers; most molecularly characterized subtype; all patients should receive comprehensive molecular profiling
- **Squamous cell carcinoma (LUSC, ~25-30% of NSCLC):** Central, hilar location; FGFR1 amplification (~20%), KEAP1/NFE2L2 (oxidative stress pathway), TP53 (>80%), CDKN2A loss, DDR2 mutation; fewer targetable oncogenes; standard treatment: chemotherapy + immunotherapy (pembrolizumab); necitumumab (anti-EGFR) + cisplatin for EGFR IHC+ squamous
- **Large cell carcinoma (~10-15%):** Poorly differentiated; diagnosis of exclusion after ruling out adeno/squamous by IHC; treated as adenocarcinoma unless otherwise specified

**Genomic landscape of lung adenocarcinoma:**
- **KRAS mutations (33% overall; G12C = 13%):** Mutually exclusive with EGFR, ALK; KRAS G12C now targetable; G12D, G12V — next-generation inhibitors
- **EGFR mutations (15-20% Western; 40-50% Asian):** Exon 19 del, L858R (~85% of EGFR mutations); exon 20 insertions (~5-10%); uncommon mutations (G719X, L861Q, S768I)
- **ALK rearrangements (5-7%):** EML4-ALK most common fusion; young non-smokers; highly responsive to ALK TKIs
- **ROS1 rearrangements (1-2%):** CD74-ROS1 most common; crizotinib, entrectinib, ceritinib active
- **RET rearrangements (1-2%):** KIF5B-RET; selpercatinib (LIBRETTO-001) highly active
- **MET exon 14 skipping (3-4%):** Capmatinib (GEOMETRY), tepotinib approved
- **HER2 mutations (2-3%):** Exon 20 insertions dominant; trastuzumab deruxtecan (T-DXd) approved (DESTINY-Lung01/02)
- **BRAF V600E (~2%):** Dabrafenib + trametinib approved
- **NTRK1/2/3 fusions (<1%):** Larotrectinib and entrectinib (tissue-agnostic approval)
- **TP53 mutations (>50%):** Co-mutation with KRAS in ~30% of LUAD; no direct therapy
- **KEAP1/STK11 mutations:** Co-occur with KRAS; suppress NRF2-regulated antioxidant → immunotherapy resistance markers; STK11 loss → "cold" tumor, resistance to pembrolizumab

**Small cell lung cancer (SCLC) — distinct entity (not covered here):**
- Neuroendocrine; 15% of lung cancers; virtually universal RB1 + TP53 loss; atezolizumab + carboplatin + etoposide (first-line); extensive-stage SCLC median OS ~12 months; rapid chemosensitivity but universal relapse

## Structure

### Pathogenesis and tumor microenvironment

**Carcinogenesis:**
- **Smoking (80-85% of NSCLC):** Tobacco carcinogens (PAHs, nitrosamines) → DNA adducts → predominantly C>A transversions in TP53, KRAS G12C, and other driver genes; squamous cell carcinoma is more strongly tobacco-related than adenocarcinoma
- **Never-smoker NSCLC:** More likely to be EGFR-mutant, ALK/ROS1-rearranged, HER2-mutant; adenocarcinoma histology; younger patients; better prognosis per matched stage
- **Preinvasive lesions:** Adenocarcinoma in situ (AIS, previously BAC) → minimally invasive adenocarcinoma → invasive adenocarcinoma; squamous: normal epithelium → squamous metaplasia → dysplasia → carcinoma in situ → invasive SCC

**NSCLC tumor microenvironment (TME):**
- Variable TME composition by subtype: squamous tumors (higher TIL density, higher TMB) vs. KRAS/STK11-mutant adenocarcinoma (immune excluded/desert)
- **PD-L1 expression:** Driven by IFN-gamma signaling in TME; ~30% TPS ≥50%; ~55% TPS ≥1%; IFN-gamma → STAT1 → IRF1 → PD-L1 transcription; used for pembrolizumab mono (≥50%) and combination (≥1%) decisions
- **Tumor mutational burden (TMB):** Higher in squamous (smoking-related) vs. adenocarcinoma; TMB-H (≥10 mut/Mb) → pembrolizumab monotherapy approval (KEYNOTE-158, tumor-agnostic); modest predictive biomarker for NSCLC specifically vs. PD-L1

## Function

### Clinical presentation and staging

**Presentation:**
- Central NSCLC (squamous): Cough, hemoptysis, post-obstructive pneumonia, wheezing; occasionally endobronchial
- Peripheral NSCLC (adenocarcinoma): Often asymptomatic until advanced; chest pain, dyspnea with pleural effusion; peripheral nodule discovered incidentally on CT
- **Pancoast tumor (superior sulcus):** Shoulder/arm pain, Horner syndrome (ptosis, miosis, anhidrosis), hand atrophy — brachial plexus and sympathetic chain invasion; special treatment: concurrent chemo-RT → surgery
- **Paraneoplastic:** SIADH (squamous SCC), hypercalcemia (PTHrP from squamous), Eaton-Lambert (SCLC more common), hypertrophic pulmonary osteoarthropathy (periosteal new bone formation, clubbing → mostly adenocarcinoma)

**Staging (TNM, 8th edition):**
- Stage I-IIIA: Locoregional; curative intent with surgery ± adjuvant; landmark improvement: adjuvant osimertinib (ADAURA: DFS HR 0.17 in stage II-III EGFR-mutant) and adjuvant atezolizumab (IMpower010: PD-L1 ≥1%, stage II-IIIA after platinum chemotherapy)
- Stage IIIB-C: Unresectable locally advanced; concurrent cisplatin/etoposide + RT → durvalumab consolidation (PACIFIC trial: 5-year OS 42.9% vs. 33.4%)
- Stage IV: Metastatic; molecular-directed or immunotherapy-based; brain metastases common (especially EGFR/ALK — high CNS penetrance of osimertinib and lorlatinib important)

**Screening:**
- Low-dose CT (LDCT) annually: US Preventive Services Task Force recommends for adults 50-80 years, 20+ pack-year history, currently smoking or quit <15 years; reduces lung cancer mortality ~20% (NLST trial); widespread implementation ongoing; requires structured reporting (Lung-RADS)

## Pathology

### Diagnosis and molecular profiling

**Tissue biopsy:** CT-guided percutaneous or bronchoscopic biopsy → histology (hematoxylin/eosin), IHC (TTF-1/NapsinA for adenocarcinoma; p40/CK5/6 for squamous), and comprehensive molecular testing

**Molecular profiling — mandatory for all newly diagnosed advanced NSCLC:**
- **Comprehensive genomic profiling (CGP, e.g., FoundationOne CDx, MSK-IMPACT):** Single test provides all relevant biomarkers (EGFR, KRAS, ALK, ROS1, MET, RET, BRAF, NTRK, HER2, TMB, MSI); preferred over sequential single-gene testing
- **PD-L1 IHC (22C3 pharmDx):** TPS (tumor proportion score) 0/1-49/≥50%; guides pembrolizumab monotherapy vs. combination; required in all newly diagnosed metastatic NSCLC

### Treatment [^soria-2018-osimertinib-flaura] [^reck-2016-pembrolizumab-keynote024]

**EGFR-mutant NSCLC (exon 19 del or L858R):**
- **First-line:** Osimertinib (3rd-gen EGFR TKI, FLAURA: PFS 18.9 vs. 10.2 months vs. 1st-gen; OS 38.6 vs. 31.8 months; CNS penetrant; approved for adjuvant after resection and for stage IV first-line) [^soria-2018-osimertinib-flaura]
- **Resistance mechanisms:** On-target (C797S in cis with T790M, or new EGFR amplification), off-target (MET amplification, HER2 amplification, PIK3CA mutation, RET/ALK/RAS transformation); liquid biopsy (ctDNA) tracks resistance earlier than imaging
- **Osimertinib + chemotherapy (FLAURA2):** Improved PFS (25.5 vs. 16.7 months) but added toxicity → selected high-risk patients

**ALK-rearranged NSCLC:**
- **First-line:** Alectinib (ALEX: PFS 34.8 vs. 10.9 months vs. crizotinib; superior CNS penetration); brigatinib and lorlatinib also active first-line; lorlatinib (CROWN trial) may be preferred in patients with brain metastases (intracranial ORR 82%)
- **Resistance:** Lorlatinib covers most ALK secondary mutations (G1202R — most common alectinib resistance)

**KRAS G12C-mutant NSCLC:** [^halliday-2023-kras-nsclc]
- **Sotorasib (Lumakras, CodeBreaK-100):** ORR 37%, median DFS 6.8 months; FDA approved 2021
- **Adagrasib (Krazati, KRYSTAL-1):** ORR 43%, median PFS 6.5 months; FDA approved 2022; CNS active; MAESTRA-3 Phase 3 first-line trial vs. chemotherapy ongoing
- **Combination strategies:** KRAS G12C + SHP2, MEK, or EGFR inhibitors to overcome adaptive RAS pathway reactivation

**PD-L1 ≥50%, no oncogenic driver:**
- **Pembrolizumab monotherapy (KEYNOTE-024):** OS 26.3 vs. 13.8 months vs. chemotherapy in PD-L1 ≥50%; 5-year OS 31.9% vs. 16.3% — durable survival benefit [^reck-2016-pembrolizumab-keynote024]; approved first-line
- **Nivolumab + ipilimumab (CHECKMATE-227):** Dual checkpoint blockade; OS benefit in TMB-H subgroup; approved first-line regardless of PD-L1 based on CHECKMATE-9LA (+ 2 cycles chemotherapy)

**Squamous NSCLC or adenocarcinoma with PD-L1 1-49% or undetermined:**
- **Pembrolizumab + carboplatin + paclitaxel/nab-paclitaxel (KEYNOTE-189 [adeno], KEYNOTE-407 [squamous]):** OS benefit vs. chemotherapy alone regardless of PD-L1; OS 15.9 vs. 11.3 months (squamous); now standard-of-care for eligible patients

**BRAF V600E-mutant NSCLC:**
- **Dabrafenib + trametinib:** ORR 64%, PFS 14.6 months (BRF113928 trial); FDA approved for BRAF V600E-mutant NSCLC

**Adjuvant and consolidation therapies:**
- **Osimertinib adjuvant (ADAURA):** After resection of stage IB-IIIA EGFR-mutant; DFS HR 0.17; 5-year DFS ~85% vs. ~44% placebo → transformative; 3-year course
- **Durvalumab consolidation (PACIFIC):** After concurrent CRT for unresectable stage III NSCLC; 5-year OS 42.9% vs. 33.4%; standard of care globally
- **Pembrolizumab adjuvant (KEYNOTE-091):** After resection stages IB-IIIA, regardless of PD-L1; DFS benefit; atezolizumab adjuvant (IMpower010) in PD-L1 ≥1%

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS G12C is the most common oncogenic driver in NSCLC adenocarcinoma (~13%); sotorasib (CodeBreaK-100) and adagrasib (KRYSTAL-1) are approved for KRAS G12C-mutant NSCLC; next-generation pan-KRAS and T cell-engaging approaches in clinical development.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR mutations (exon 19 del, L858R) drive 15-20% of NSCLC; osimertinib (FLAURA: PFS 18.9 vs. 10.2 months vs. erlotinib) is first-line standard; acquired resistance via C797S and MET amplification drives second-line decisions.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E occurs in ~2% of NSCLC adenocarcinoma; dabrafenib + trametinib is approved for BRAF V600E-mutant NSCLC (ORR ~64%, PFS 14.6 months); non-V600E BRAF mutations require pan-RAF or ERK-directed approaches.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1/PD-L1 blockade transformed NSCLC: pembrolizumab is standard-of-care in PD-L1 ≥50% first-line (KEYNOTE-024: OS 26.3 vs. 13.8 months) and + chemotherapy in all-comers; atezolizumab, nivolumab, and durvalumab are also approved.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — NSCLC is ~85% of lung cancer: squamous tumors arise centrally near the hilum (cough, hemoptysis) while adenocarcinomas arise peripherally and are often found incidentally; annual low-dose CT screening of heavy smokers cuts lung-cancer mortality ~20% (NLST).
- `connects-to` → **[ALK](../../03-molecular/alk/README.md)** — ALK rearrangements (EML4-ALK, ~5-7%) define a distinct NSCLC of young never-smokers that is exquisitely targetable: alectinib and lorlatinib far outperform chemotherapy with strong CNS penetration for brain metastases; lorlatinib covers the G1202R resistance mutation.
- `connects-to` → **[Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — Lung adenocarcinoma arises from alveolar type II pneumocytes (and club cells), retaining their TTF-1 and napsin-A markers; it progresses through adenocarcinoma-in-situ → minimally invasive → invasive adenocarcinoma, the peripheral lepidic-to-solid sequence.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — NSCLC and melanoma are the twin proving grounds of checkpoint immunotherapy: both accumulate heavy carcinogen-driven mutational burdens (tobacco, UV) yielding neoantigens, so PD-1/PD-L1 (and CTLA-4) blockade gives durable responses in both, and both carry targetable BRAF V600E.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — NSCLC's response to immunotherapy hinges on cytotoxic T cells: a high tobacco-driven mutational burden generates neoantigens, and PD-1/PD-L1 blockade (pembrolizumab, first-line at PD-L1 ≥50%) reinvigorates exhausted CD8+ T cells — absent in never-smoker EGFR/ALK subsets.
- `connects-to` → **[Small Cell Lung Cancer](../sclc/README.md)** — NSCLC and small-cell lung cancer are the two divisions of lung cancer: NSCLC (~85%, adeno/squamous) is driver-rich and often resectable or targetable, while SCLC is a fast neuroendocrine tumor of heavy smokers that disseminates early, is rarely operable, and is RB1/TP53-driven.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — NSCLC and mesothelioma are the two major thoracic cancers tied to inhaled carcinogens but distinct: NSCLC arises in lung parenchyma (smoking, EGFR/KRAS-driven), while mesothelioma arises from the pleura decades after asbestos exposure—different cells and treatment.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is central to NSCLC: stereotactic body photon radiotherapy can cure inoperable early-stage tumors, while conventional chemoradiation treats locally advanced disease—and consolidation immunotherapy after radiation now improves survival.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages shape the NSCLC microenvironment: M2-polarized macrophages suppress cytotoxic T cells and promote angiogenesis, contributing to immunotherapy resistance—so they are studied as both a biomarker and a target alongside PD-1 blockade.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain is a frequent NSCLC metastatic site: lung adenocarcinomas, especially EGFR/ALK-driven, commonly seed the brain, so staging includes brain MRI and CNS-penetrant targeted drugs (osimertinib, lorlatinib)—brain metastases strongly shape prognosis.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Carbon-based tobacco carcinogens are the dominant cause of NSCLC: smoke's PAHs and nitrosamines form DNA adducts that mutate KRAS and TP53, driving most squamous and many adenocarcinomas—though EGFR-mutant adenocarcinoma in never-smokers takes a distinct path.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — NSCLC and head and neck cancer share tobacco-driven field cancerization: carcinogens injure the whole aerodigestive tract, so smokers with one cancer face high risk of a second primary in the other—both demand smoking cessation and surveillance.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — MET is a targetable NSCLC driver: MET exon-14 skipping mutations and MET amplification drive a subset of non-small-cell lung cancers and confer resistance to EGFR inhibitors, so MET-directed drugs extend the precision-oncology toolkit beyond EGFR, ALK and KRAS.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal gland is a classic NSCLC metastatic site: lung cancer characteristically spreads to the adrenals (along with brain, bone and liver), so an adrenal mass in a lung-cancer patient demands staging workup—adrenal involvement often marks stage IV disease.
- `connects-to` → **[COPD](../copd/README.md)** — NSCLC and COPD are linked by shared tobacco injury: smoking drives both, COPD independently raises lung-cancer risk through chronic inflammation, and the two coexist so often that emphysema complicates surgery and screening targets this overlapping high-risk population.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 is among the most mutated genes in NSCLC: smoking-driven DNA damage frequently inactivates p53, removing a key brake on the cell cycle and apoptosis, so its loss—often alongside KRAS—marks aggressive, treatment-resistant lung adenocarcinoma.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — NSCLC is the dominant cancer of the respiratory system: arising in bronchial and alveolar cells mostly from smoking, it accounts for ~85% of lung cancers and destroys lung function as it grows—the leading cause of cancer death worldwide.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — NSCLC staging hinges on the lymphatic system: spread to hilar and mediastinal lymph nodes (the N stage) determines whether disease is surgically curable, so nodal sampling by EBUS or mediastinoscopy is decisive in planning treatment.

[^soria-2018-osimertinib-flaura]: Soria JC, Ohe Y, Vansteenkiste J, et al. Osimertinib in untreated EGFR-mutated advanced non-small-cell lung cancer. *N Engl J Med.* 2018;378(2):113-125. [doi:10.1056/NEJMoa1713137](https://doi.org/10.1056/NEJMoa1713137) · [PubMed 29151359](https://pubmed.ncbi.nlm.nih.gov/29151359/)
[^reck-2016-pembrolizumab-keynote024]: Reck M, Rodríguez-Abreu D, Robinson AG, et al. Pembrolizumab versus chemotherapy for PD-L1-positive non-small-cell lung cancer. *N Engl J Med.* 2016;375(19):1823-1833. [doi:10.1056/NEJMoa1606774](https://doi.org/10.1056/NEJMoa1606774) · [PubMed 27718347](https://pubmed.ncbi.nlm.nih.gov/27718347/)
[^halliday-2023-kras-nsclc]: Riely GJ, Ou SHI, Rybkin I, et al. KRYSTAL-1: activity and preliminary pharmacodynamic analysis of adagrasib in patients with advanced NSCLC harboring KRAS G12C mutation. *J Thorac Oncol.* 2022;17(10):1248-1258. [doi:10.1016/j.jtho.2022.06.020](https://doi.org/10.1016/j.jtho.2022.06.020) · [PubMed 35817313](https://pubmed.ncbi.nlm.nih.gov/35817313/)
