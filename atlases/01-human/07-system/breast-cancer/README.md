---
schema: human-scale-entry/v1
id: breast-cancer
name: Breast Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common cancer in women; driven by ER/PR hormone signaling, HER2 amplification, and basal TNBC subtypes. BRCA1/2 mutations drive hereditary cases; CDK4/6 inhibitors (palbociclib), anti-HER2 (trastuzumab), PARP inhibitors (olaparib), and immunotherapy are mainstays."
aliases: ["breast carcinoma", "HR+ breast cancer", "HER2+ breast cancer", "TNBC", "triple-negative breast cancer", "luminal A", "luminal B", "invasive ductal carcinoma", "invasive lobular carcinoma", "DCIS"]
sources:
  - id: siegel-2024-cancer-statistics
    type: peer-reviewed
    cite: "Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. CA Cancer J Clin. 2024;74(1):12-49."
    doi: "10.3322/caac.21820"
    pmid: "38230766"
    url: "https://doi.org/10.3322/caac.21820"
  - id: slamon-2001-trastuzumab-trial
    type: peer-reviewed
    cite: "Slamon DJ, Leyland-Jones B, Shak S, et al. Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. N Engl J Med. 2001;344(11):783-792."
    doi: "10.1056/NEJM200103153441101"
    pmid: "11248153"
    url: "https://doi.org/10.1056/NEJM200103153441101"
  - id: finn-2016-palbociclib-paloma2
    type: peer-reviewed
    cite: "Finn RS, Martin M, Rugo HS, et al. Palbociclib and letrozole in advanced breast cancer. N Engl J Med. 2016;375(20):1925-1936."
    doi: "10.1056/NEJMoa1607303"
    pmid: "27959613"
    url: "https://doi.org/10.1056/NEJMoa1607303"
cross_links:
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "HER2 amplification (~20% of breast cancers) → constitutive kinase → PI3K-AKT-mTOR and RAS-ERK → aggressive biology; trastuzumab + pertuzumab + docetaxel is first-line HER2+ metastatic (CLEOPATRA OS 57 vs. 41 months); T-DM1 and T-DXd (DESTINY-Breast03) are second-line."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA mutations occur in 30-40% of HR+/HER2- breast cancer → PI3K-AKT-mTOR activation → endocrine therapy resistance; alpelisib (PI3K-alpha inhibitor) + fulvestrant is approved for PIK3CA-mutant HR+/HER2- metastatic breast cancer (SOLAR-1, PFS 11.0 vs. 5.7 months)."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1 germline mutations confer ~70% lifetime breast cancer risk (predominantly TNBC); BRCA1 loss → HR deficiency → PARP inhibitor sensitivity; olaparib (OlympiAD) and talazoparib (EMBRACA) are approved for BRCA1/2-mutant HER2-negative metastatic breast cancer."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) + AI are standard-of-care first-line for HR+/HER2- metastatic breast cancer; ribociclib + letrozole improved OS to 63.9 vs. 51.4 months (MONALEESA-2); abemaciclib is approved adjuvantly for high-risk early-stage disease."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "ERα (ESR1) drives ~70-75% of breast cancers; aromatase inhibitors (anastrozole, letrozole) are first-line adjuvant for postmenopausal ER+ disease; fulvestrant (SERD) degrades ERα; ESR1 LBD mutations (D538G, Y537S) cause AI resistance in metastatic HR+ disease."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "PR+ breast cancers have better prognosis than PR- tumors; combined E2+progestogen HRT (WHI) increased breast cancer risk vs. estrogen-only; progestins in combined OCP contribute to VTE risk; PR agonists (megestrol, medroxyprogesterone) treat endometrial hyperplasia and EC."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Breast cancer bone metastases exploit the RANKL axis: PTHrP from tumor cells → osteoblast RANKL → osteoclast osteolysis releases TGF-β and IGF-1 → vicious cycle of tumor-bone crosstalk; denosumab (Xgeva) delays skeletal-related events by ~8.5 months vs. zoledronate (HALT-BC)."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Breast cancer overexpresses CXCR4 → homing to CXCL12-rich organs (bone marrow, lung, liver, brain) → organ-specific metastasis; stromal CXCL12 promotes primary tumor growth; CXCR4 correlates with lymph node involvement and poor prognosis; anti-CXCR4 therapy in trials."
---

# Breast Cancer

## Overview

**Breast cancer** is the **most common cancer in women worldwide** and the second leading cause of cancer-related death in women. In 2024, approximately **310,720 new cases** of invasive breast cancer will be diagnosed in the United States, with ~42,000 deaths [^siegel-2024-cancer-statistics]. It is now surpassed by lung cancer in global cancer deaths but remains the most diagnosed cancer among women globally.

**Breast cancer is biologically heterogeneous** — it is best understood as multiple distinct diseases with different molecular drivers, natural histories, prognoses, and treatment strategies, unified by their tissue of origin in mammary epithelium.

**Intrinsic molecular subtypes (PAM50 classification):**
- **Luminal A (~40%):** ER+/PR+, HER2-, low Ki-67 (grade 1-2); best prognosis; driven by estrogen signaling; responds well to hormone therapy; chemotherapy often unnecessary; 10-year DFS >85%; endocrine therapy is sufficient in most
- **Luminal B (~20%):** ER+, HER2-/+, high Ki-67 or grade 3; more proliferative than Luminal A; may benefit from chemotherapy; worse prognosis than Luminal A; CDK4/6 inhibitors have greatest benefit
- **HER2-enriched (~15%):** HER2 amplification/overexpression; ER-negative; aggressive; transformed by advent of HER2-targeted therapy; trastuzumab + pertuzumab + chemotherapy → DFS ~90% at 3 years in early stage; T-DXd highly active in metastatic
- **Basal-like/TNBC (~15%):** ER-, PR-, HER2-; high grade; aggressive; BRCA1-associated tumors mostly in this subtype; no hormonal targets; chemotherapy, immunotherapy (pembrolizumab), PARP inhibitors (BRCA1/2-mutant); worst prognosis but higher rate of pathological complete response to neoadjuvant chemotherapy
- **Normal-like (~5-10%):** Resembles normal breast tissue; variable prognosis

**Hereditary breast cancer:**
- **BRCA1/2 (~5-10% of all breast cancers):** BRCA1 → predominantly TNBC/basal-like; BRCA2 → Luminal/HER2-enriched; BRCA1/2 mutations → 70%/45% lifetime risk respectively; management: prophylactic mastectomy, bilateral salpingo-oophorectomy (also prevents ovarian cancer), intensive surveillance (annual MRI + mammography from age 25-30)
- **Other hereditary genes:** PALB2 (40-60% lifetime risk, similar to BRCA2), ATM (20-30%), CHEK2 (15-25%), CDH1 (hereditary diffuse gastric + lobular breast cancer), TP53 (Li-Fraumeni — 50-90% lifetime risk), PTEN (Cowden syndrome), STK11 (Peutz-Jeghers)

**Epidemiology and risk factors:**
- **Age:** Incidence rises sharply after 40; peak incidence 60-70 years; younger-onset more likely hereditary or TNBC
- **Hormonal:** Early menarche, late menopause, nulliparity, late first birth, hormone replacement therapy (combined estrogen/progesterone HRT → increased risk), oral contraceptives (modest)
- **Lifestyle:** Obesity (postmenopausal), alcohol consumption, physical inactivity, dense breast tissue (imaging-based risk factor)
- **Prior breast biopsy:** ADH (atypical ductal hyperplasia), ALH → 4-5× increased risk; LCIS → 7-10× risk (marker not obligate precursor)
- **Race:** Black women have lower incidence but higher mortality (later stage at diagnosis, more TNBC, higher grade, socioeconomic/access factors)

## Structure

### Histopathology and staging

**Histological types:**
- **Invasive ductal carcinoma (IDC/NST, no special type, ~75%):** Most common; forms infiltrating cords/nests; graded by Nottingham grade (tubule formation, nuclear pleomorphism, mitotic rate; Grade 1-3)
- **Invasive lobular carcinoma (ILC, ~15%):** CDH1 (E-cadherin) loss → discohesive single-file "Indian file" infiltration; often ER+/lobular; associated with bilateral disease; may be occult on mammogram; responds to endocrine therapy
- **Special types (better prognosis):** Mucinous (colloid), tubular, medullary, cribriform, adenoid cystic (TNBC but indolent)
- **DCIS (ductal carcinoma in situ):** Non-invasive; precursor lesion; managed by excision ± radiation ± endocrine therapy (tamoxifen reduces ipsilateral invasive recurrence); controversial: subset of low-grade DCIS may never become invasive (active surveillance trials: COMET, LORIS, LORD)

**TNM staging (AJCC 8th edition — includes molecular subtype):**
- Stage I-III: Locoregional; curative intent; Stage IV: Distant metastasis (bone, lung, liver, brain most common) — generally incurable but increasingly manageable as chronic disease (median OS in HR+/HER2- metastatic: 3-4 years; HR+ HER2-: improving)
- Prognostic genomic tests (Oncotype DX [21-gene RS], MammaPrint [70-gene], PAM50/Prosigna, EndoPredict) identify which early-stage HR+ breast cancers benefit from adjuvant chemotherapy vs. endocrine therapy alone

### Molecular oncogenesis

**HR+ pathway (estrogen receptor-driven):**
- Estrogen → ER-alpha binding → ER dimerization → ERE binding → cyclin D1, MYC, BCL-2 transcription → G1-S progression
- **PI3K-AKT-mTOR axis:** PIK3CA gain-of-function (30-40% of HR+ tumors) → AKT-mTOR → ER-independent growth → endocrine resistance; PTEN loss (25-30%) → same net effect
- **CDK4/6-Rb axis:** Cyclin D1-CDK4/6 → Rb phosphorylation → E2F activation → S-phase; CDK4/6 inhibitors restore Rb-mediated G1 arrest
- **Endocrine resistance mechanisms:** ESR1 mutations (D538G, Y537S — acquired, found in cfDNA) → ligand-independent ER activation; PI3K pathway activation; CDK4/6 pathway amplification (cyclin D1, CDK4 amplification)

**HER2+ pathway:** See HER2 cross-link entry.

**TNBC/Basal-like:**
- High genomic instability, TP53 mutations (>80%), BRCA1 loss, RB1 loss; driven by PI3K-AKT, EGFR, FGFR, AR (androgen receptor — ~30% of TNBC express AR → potential therapeutic target)
- High tumor-infiltrating lymphocytes (TILs) correlate with better prognosis and immunotherapy response; high PD-L1 expression in ~40% of TNBC → pembrolizumab + chemotherapy approved in PD-L1+ metastatic TNBC (KEYNOTE-522 in early-stage regardless of PD-L1)

## Function

### Clinical presentation and screening

**Presentation:**
- Most common: painless, hard, irregular breast lump; asymmetric thickening
- Nipple discharge (bloody → suspicious), skin changes (peau d'orange = lymphatic obstruction, dimpling, nipple retraction, erythema)
- Inflammatory breast cancer (IBC, 1-3%): Rapid-onset erythema, warmth, edema, peau d'orange of breast skin without palpable mass → dermal lymphatic invasion; aggressive; requires neoadjuvant chemotherapy before surgery
- Paget's disease: Eczematous nipple rash → intraepidermal carcinoma cells (Paget cells); associated with underlying DCIS or invasive cancer in most cases

**Screening:**
- **Mammography:** Annual from age 40-74 (USPSTF updated 2024: recommends starting at 40, previously 50); reduces breast cancer mortality ~15-20% in screened populations; digital breast tomosynthesis (3D mammography) improves cancer detection and reduces false positives vs. 2D
- **MRI:** Annual breast MRI + mammography for high-risk (BRCA1/2, >20% lifetime risk); superior sensitivity in dense breasts; false-positive rate higher
- **Ultrasound:** Supplement to mammography in dense breasts; not a standalone screening tool in average risk

## Pathology

### Diagnosis and biomarkers

**Core needle biopsy:** Ultrasound or stereotactic-guided; provides histology, grade, ER/PR (IHC, % cells + Allred score), HER2 (IHC 0/1+/2+/3+; 2+ → FISH/ISH reflex), Ki-67 (proliferation index)

**Genomic testing in early-stage HR+/HER2- breast cancer:**
- **Oncotype DX (21-gene recurrence score, RS):** Predicts 10-year distant recurrence risk and chemotherapy benefit in node-negative (TAILORx trial) and 1-3 node-positive (RxPONDER) ER+/HER2- early breast cancer; RS <26 → endocrine therapy alone (chemotherapy no benefit in postmenopausal); RS ≥26 → chemotherapy benefit; now standard of care globally
- **MammaPrint (70-gene):** MINDACT trial: ~46% of clinically high-risk/genomic low-risk patients spared chemotherapy; approved in US for node-negative or 1-3 node-positive HR+/HER2-

### Treatment

**Early-stage (curative intent):**

*Surgery:*
- Breast-conserving surgery (lumpectomy + radiation) equivalent to mastectomy in OS for stages I-II; sentinel lymph node biopsy standard (avoids axillary lymph node dissection in sentinel-negative; Z0011 trial validates omission of ALND in limited nodal disease); nipple-sparing mastectomy with reconstruction increasingly used

*Radiation:*
- Post-lumpectomy whole-breast radiation reduces local recurrence 50-70%; hypofractionation (40 Gy/15 fractions) vs. conventional (50 Gy/25 fractions) equivalent efficacy; partial breast irradiation for select low-risk early-stage; regional nodal irradiation for ≥4 positive nodes

*Adjuvant systemic therapy by subtype:*
- **HR+:** Endocrine therapy 5-10 years (tamoxifen premenopausal; AI postmenopausal ± ovarian suppression); CDK4/6 inhibitors (abemaciclib × 2 years for high-risk, monarchE: significantly improved DFS)
- **HER2+:** Trastuzumab × 1 year ± pertuzumab (APHINITY); T-DM1 for residual disease after neoadjuvant (KATHERINE: iDFS 88% vs. 77% trastuzumab)
- **TNBC:** Pembrolizumab + chemotherapy neoadjuvant → pembrolizumab adjuvant (KEYNOTE-522: EFS benefit regardless of pCR); capecitabine for non-pCR; olaparib adjuvant for BRCA1/2-mutant (OlympiA: distant DFS benefit) [^slamon-2001-trastuzumab-trial]

**Metastatic HR+/HER2- (chronic disease management):**
- **First-line:** CDK4/6 inhibitor + AI (palbociclib/PALOMA-2, ribociclib/MONALEESA-2, abemaciclib/MONARCH-3); OS benefit confirmed for ribociclib (63.9 vs. 51.4 months, MONALEESA-2) [^finn-2016-palbociclib-paloma2]
- **Second-line (post-CDK4/6 + ESR1 mutation):** Elacestrant (oral SERD, EMERALD trial: PFS benefit in ESR1-mutant); fulvestrant + alpelisib (SOLAR-1, PIK3CA-mutant)
- **mTOR inhibitors:** Everolimus + exemestane (BOLERO-2: PFS 10.6 vs. 4.1 months); capivasertib (AKT inhibitor) + fulvestrant (CAPItello-291: approved for PIK3CA/AKT/PTEN-altered)
- **ADC (antibody-drug conjugate):** Sacituzumab govitecan (TROPION-Breast01 in HR+) and trastuzumab deruxtecan (T-DXd, DESTINY-Breast06 in HER2-low HR+) expanding options

**Metastatic TNBC:**
- **PD-L1+ (CPS ≥10):** Pembrolizumab + chemotherapy (KEYNOTE-355: OS 23.0 vs. 16.1 months)
- **BRCA1/2-mutant:** Olaparib (OlympiAD) or talazoparib (EMBRACA) superior to chemotherapy
- **Sacituzumab govitecan (Trodelvy, Trop-2 ADC):** ASCENT trial: OS 12.1 vs. 6.7 months vs. chemotherapy; approved for 2L+ TNBC

## Connections

- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — HER2 amplification (~20% of breast cancers) → constitutive kinase → PI3K-AKT-mTOR and RAS-ERK → aggressive biology; trastuzumab + pertuzumab + docetaxel is first-line HER2+ metastatic (CLEOPATRA: OS 57 vs. 41 months); T-DXd leads in second-line.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutations in 30-40% of HR+/HER2- breast cancer → PI3K-AKT-mTOR → endocrine therapy resistance; alpelisib + fulvestrant is approved for PIK3CA-mutant HR+/HER2- metastatic breast cancer (SOLAR-1, PFS 11.0 vs. 5.7 months).
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BRCA1 germline mutations confer ~70% lifetime breast cancer risk (predominantly TNBC); BRCA1 loss → HR deficiency → PARP inhibitor sensitivity; olaparib (OlympiAD) and talazoparib (EMBRACA) approved for BRCA1/2-mutant HER2-negative metastatic breast cancer.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) + AI are standard-of-care first-line for HR+/HER2- metastatic breast cancer; ribociclib + letrozole improved OS to 63.9 vs. 51.4 months (MONALEESA-2); abemaciclib approved adjuvantly for high-risk early-stage HR+ disease.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — ERα (ESR1) drives ~70-75% of breast cancers; aromatase inhibitors (anastrozole, letrozole) are first-line adjuvant for postmenopausal ER+ disease; fulvestrant (SERD) degrades ERα; ESR1 LBD mutations (D538G, Y537S) cause AI resistance in metastatic HR+ disease.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — PR+ breast cancers have better prognosis than PR- tumors; combined E2+progestogen HRT (WHI) increased breast cancer risk vs. estrogen-only; progestins in combined OCP contribute to VTE risk; PR agonists (megestrol, medroxyprogesterone) treat endometrial hyperplasia and EC.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — breast cancer bone metastases exploit the RANKL axis: PTHrP from tumor cells → osteoblast RANKL → osteoclast osteolysis releases TGF-β and IGF-1 → vicious cycle of tumor-bone crosstalk; denosumab (Xgeva) delays skeletal-related events by ~8.5 months vs. zoledronate (HALT-BC).
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Breast cancer overexpresses CXCR4 → homing to CXCL12-rich organs (bone marrow, lung, liver, brain) → organ-specific metastasis; stromal CXCL12 promotes primary tumor growth; CXCR4 correlates with lymph node involvement and poor prognosis; anti-CXCR4 therapy in trials.

[^siegel-2024-cancer-statistics]: Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. *CA Cancer J Clin.* 2024;74(1):12-49. [doi:10.3322/caac.21820](https://doi.org/10.3322/caac.21820) · [PubMed 38230766](https://pubmed.ncbi.nlm.nih.gov/38230766/)
[^slamon-2001-trastuzumab-trial]: Slamon DJ, Leyland-Jones B, Shak S, et al. Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. *N Engl J Med.* 2001;344(11):783-792. [doi:10.1056/NEJM200103153441101](https://doi.org/10.1056/NEJM200103153441101) · [PubMed 11248153](https://pubmed.ncbi.nlm.nih.gov/11248153/)
[^finn-2016-palbociclib-paloma2]: Finn RS, Martin M, Rugo HS, et al. Palbociclib and letrozole in advanced breast cancer. *N Engl J Med.* 2016;375(20):1925-1936. [doi:10.1056/NEJMoa1607303](https://doi.org/10.1056/NEJMoa1607303) · [PubMed 27959613](https://pubmed.ncbi.nlm.nih.gov/27959613/)
