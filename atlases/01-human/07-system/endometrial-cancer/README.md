---
schema: human-scale-entry/v1
id: endometrial-cancer
name: Endometrial Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common gynecologic malignancy in the US (~67,000/year); POLE-ultramutated and MSI-H subtypes respond to pembrolizumab; endometrioid type driven by PTEN/PIK3CA/KRAS; serous by TP53/ERBB2. Carboplatin+paclitaxel is standard; dostarlimab approved for dMMR endometrial cancer."
aliases: ["endometrial cancer", "endometrial carcinoma", "uterine cancer", "endometrioid adenocarcinoma", "uterine serous carcinoma", "POLE-ultramutated", "Lynch-associated endometrial cancer"]
sources:
  - id: konstantinopoulos-2019-dostarlimab
    type: peer-reviewed
    cite: "Konstantinopoulos PA, Lheureux S, Moore KN. PARP inhibitors for ovarian and endometrial cancers: state of the art and clinical perspectives. J Clin Oncol. 2020;38(25):2896-2909."
    doi: "10.1200/JCO.20.00571"
    pmid: "32706635"
    url: "https://doi.org/10.1200/JCO.20.00571"
  - id: eskander-2023-ruby
    type: peer-reviewed
    cite: "Eskander RN, Sill MW, Beffa L, et al. Pembrolizumab plus chemotherapy in advanced endometrial cancer. N Engl J Med. 2023;388(23):2159-2170."
    doi: "10.1056/NEJMoa2302312"
    pmid: "37166384"
    url: "https://doi.org/10.1056/NEJMoa2302312"
cross_links:
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss in ~50-80% of endometrioid endometrial cancer; earliest molecular event in endometrial carcinogenesis; PTEN loss → PI3K-AKT-mTOR activation → proliferation; mTOR inhibitors (everolimus+letrozole) active in ER+ disease; germline PTEN mutations cause Cowden syndrome."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "dMMR endometrial cancer (~25-30%) responds to pembrolizumab; KEYNOTE-158 ORR 57%; dostarlimab FDA approved 2021 for dMMR recurrent endometrial; RUBY trial improved OS in dMMR subset; PD-1 blockade is standard for dMMR recurrent disease."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "ERBB2/HER2 amplification in ~30% of uterine serous carcinoma and carcinosarcoma; trastuzumab+carboplatin/paclitaxel improved PFS (Fader 2018); HER2+ USC is actionable; T-DXd studied in HER2-low endometrial; HER2 testing recommended for serous histology."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PI3K/AKT/mTOR activated in ~70% of endometrioid endometrial cancer (PTEN loss, PIK3CA ~40%, AKT1 E17K); everolimus+letrozole → 32% clinical benefit in ER+ disease; lenvatinib+pembrolizumab (KEYNOTE-146) active in non-MSI-H recurrent endometrial cancer."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Unopposed estrogen drives endometrial hyperplasia → EIN → type 1 endometrioid cancer; obesity → adipose aromatase → androgen-to-estrogen conversion → ~3× EC risk at BMI >30; aromatase inhibitors active in ER+ endometrial cancer; combined HRT (with progestogen) prevents EC risk."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Progesterone drives endometrial secretory transformation opposing estrogen proliferation; mifepristone (PR/GR antagonist) blocks P4 receptor → decidual breakdown → pregnancy termination; progesterone supplementation treats luteal phase deficiency and recurrent miscarriage."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Endometrial cancer is the sentinel cancer of Lynch syndrome: about half of female carriers present with it before any colorectal cancer, so a young or dMMR endometrial tumour should prompt germline testing — and these MSI-H cancers respond well to PD-1 immunotherapy."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity is the dominant modifiable driver of endometrial cancer: adipose aromatase converts androgens to estrogen, and this unopposed estrogen pushes endometrium through hyperplasia to type-1 endometrioid cancer — roughly tripling risk at BMI >30 and fueling rising incidence."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation defines the most aggressive endometrial cancers: near-universal (~90%) in uterine serous carcinoma, it marks the copy-number-high TCGA group with the worst prognosis, unlike the estrogen-driven endometrioid tumours — a split that now guides adjuvant therapy."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Endometrial and breast cancers are linked estrogen-driven cancers: unopposed estrogen and obesity raise risk of both, and tamoxifen used for breast cancer acts as a uterine estrogen agonist that increases endometrial cancer risk—so bleeding on tamoxifen warrants evaluation."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Endometrial and ovarian cancers frequently co-occur: ~10% of endometrioid endometrial cancers have a synchronous endometrioid ovarian primary, and both are core Lynch-syndrome tumors from mismatch-repair deficiency—so MMR/MSI testing and gynecologic surveillance span the two."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Endometrial and colorectal cancer are the defining Lynch-syndrome malignancies: germline mismatch-repair mutations (MLH1, MSH2/6, PMS2) drive microsatellite instability in both, endometrial cancer is often the sentinel cancer in women, and MSI-high tumors take immunotherapy."
---

# Endometrial Cancer

## Overview

**Endometrial cancer** is the most common gynecologic malignancy in the United States, with ~67,000 new cases and ~13,000 deaths per year. It arises from the endometrial lining of the uterus and is diagnosed in two broad histological categories: **Type I (endometrioid, estrogen-driven, ~80%)** and **Type II (serous, clear cell, carcinosarcoma, ~20%)** — a distinction reflected in their divergent molecular landscapes, treatment responses, and prognoses. The TCGA molecular classification (2013) — now integrated into WHO 2020 — stratified endometrial cancer into four prognostic groups: **POLE-ultramutated** (best prognosis), **MSI-H/dMMR** (good prognosis; responds to pembrolizumab), **copy-number low** (intermediate), and **copy-number high/TP53-mutant** (worst prognosis). This classification guides modern adjuvant and systemic therapy decisions [^eskander-2023-ruby].

**Epidemiology:**
- ~67,000 cases/year in the US; worldwide ~400,000/year; incidence rising (obesity epidemic)
- Median age at diagnosis: ~60 years; ~75% diagnosed at stage I (favorable prognosis)
- 5-year survival: ~83% overall; ~95% for stage I; ~17% for stage IV
- Risk factors: Obesity (estrogen excess from adipose conversion of androgens), unopposed estrogen exposure (anovulation, hormone replacement without progestin, tamoxifen), nulliparity, diabetes, PCOS, Lynch syndrome
- Protective: Oral contraceptives (>50% risk reduction), multiparity, physical activity, smoking (weakly protective via anti-estrogen effect)

**Lynch syndrome and endometrial cancer:**
- Lynch syndrome (germline MLH1, MSH2, MSH6, PMS2 mutation) → endometrial cancer is the sentinel cancer in ~50% of female Lynch carriers (diagnosed before CRC)
- Lifetime endometrial cancer risk: ~40-60% for MLH1/MSH2 carriers; ~15-26% for MSH6 carriers; ~15% for PMS2 carriers
- Lynch-associated endometrial cancer: Often diagnosed at younger age (<50), MSI-H, favorable prognosis with surgery, excellent ICI response

## Structure

### Histological subtypes and molecular features

**Endometrioid adenocarcinoma (Type I):**
- Well-differentiated (Grade 1-2): PTEN loss, PIK3CA mutation (~40%), KRAS mutation (~30%), microsatellite instability (~25-30%)
- Grade 3 endometrioid: More aggressive; overlaps with serous carcinoma molecularly
- POLE-ultramutated: ~5-10% of endometrioid; POLE proofreading domain mutations → ultrahigh TMB (>100 mut/Mb) → exceptional ICI response; excellent prognosis

**Uterine serous carcinoma (Type II, ~10%):**
- Near-universal TP53 mutation (~90%); ERBB2 amplification (~30%); CCNE1 amplification (~20%); HR deficient in ~25%
- Behaves like HGSOC (often presents at advanced stage, highly aggressive, platinum-sensitive)
- Intraepithelial serous carcinoma (SEIC) = precursor lesion in polyps/surface epithelium

**Clear cell carcinoma (Type II, ~5%):**
- ARID1A mutations (~30%); TP53 mutations; POLE mutations in subset; MSI-H in ~10%
- Platinum-partially sensitive; SMAD2/3 mutations in some

**Carcinosarcoma (malignant mixed Müllerian tumor, ~5%):**
- Most aggressive; metastatic disease in >50% at presentation; HER2 amplification ~30%
- Carboplatin + paclitaxel ± trastuzumab (if HER2+); carboplatin + ifosfamide is historical alternative

**TCGA/WHO 2020 molecular classification:**

| Subtype | Frequency | Key alterations | Prognosis |
|---------|-----------|-----------------|-----------|
| POLE-ultramutated | ~5-10% | POLE exonuclease domain mutations | Excellent |
| MSI-H/dMMR | ~25-30% | MLH1/MSH2/MSH6/PMS2 loss | Favorable |
| Copy-number low (NSMP) | ~40% | PTEN/KRAS/PIK3CA; low genomic instability | Intermediate |
| Copy-number high/p53abn | ~20% | TP53 mutation; ERBB2 amp; CCNE1 amp | Poor |

### Molecular landscape

**PTEN (50-80% of endometrioid):**
- PTEN loss → PI3K-AKT activation → mTORC1 → proliferation; cooperates with PIK3CA mutation
- PTEN is also lost in endometrial intraepithelial neoplasia (EIN = precancer), establishing it as an early driver

**KRAS/NRAS/BRAF mutations (~30% of endometrioid):**
- KRAS mutations (mainly G12D/G12V): activate MAPK and PI3K; co-occur with PTEN loss

**CTNNB1 (β-catenin, ~40% of endometrioid Grade 1-2):**
- Exon 3 mutations stabilize β-catenin → nuclear Wnt signaling → cyclin D1, MYC
- Associated with squamoid morule differentiation; better prognosis subgroup within copy-number low

**ARID1A (~30% of endometrioid and CCC):**
- SWI/SNF chromatin remodeling subunit; tumor suppressor; loss promotes DNA damage tolerance and EZH2 synthetic lethality

## Function

### Normal endometrial biology

**Hormonal cycling:**
- Estrogen (follicular phase) → endometrial proliferation via ERα → PTEN/PIK3CA mutation-harboring clones expand
- Progesterone (luteal phase) → secretory differentiation → antiproliferative; also suppresses endometrial proliferation
- Anovulatory cycles (PCOS, obesity, perimenopause) → prolonged unopposed estrogen → endometrial hyperplasia → EIN → endometrioid cancer

**Estrogen receptor (ERα) signaling:**
- ERα → cyclin D1 upregulation → CDK4/6 activation → RB phosphorylation → S-phase entry
- Aromatase in adipose tissue converts androgens to estrogens → central mechanism for obesity-associated endometrial cancer; BMI >30 → 3× higher risk; BMI >40 → 6× higher risk

## Pathology

### Staging and diagnosis

**FIGO 2023 staging (revised):**
- Stage I: Confined to uterus
  - IA: Limited to endometrium or <50% myometrial invasion (low-risk histology)
  - IB: ≥50% myometrial invasion; or low-grade endometrioid with LVSI
  - IC: p53-abnormal (serous/CCNE1-high) stage I tumors
- Stage II: Cervical stromal invasion
- Stage III: Pelvic/para-aortic lymph node or adnexal/vaginal extension
- Stage IV: Bladder/bowel invasion (IVA) or distant metastasis (IVB)

**Diagnosis:**
- Postmenopausal uterine bleeding: diagnostic in 90% → evaluate with transvaginal ultrasound (endometrial thickness ≥4 mm → biopsy)
- Endometrial biopsy (Pipelle): Office procedure; sensitivity ~90% for Type II histologies; hysteroscopy + D&C if initial biopsy non-diagnostic
- MRI: Best for myometrial invasion depth; CT for staging/lymph node assessment

**Surgical staging:**
- Total hysterectomy + bilateral salpingo-oophorectomy (TH-BSO) is curative for early-stage disease; sentinel lymph node (SLN) mapping has replaced full pelvic lymphadenectomy in most centers
- Molecular testing at surgery: POLE, MMR/MSI, TP53 IHC guides adjuvant therapy decisions

### Treatment

**Stage I-II low-risk (Grade 1-2 endometrioid, <50% MI, no LVSI):**
- Surgery alone (TH-BSO ± SLN); no adjuvant therapy; recurrence rate <5%
- Vaginal brachytherapy (VBT) for Grade 3 or with LVSI → reduces vaginal recurrence

**Stage I-II high-risk / Stage III:**
- Carboplatin (AUC5) + paclitaxel (175 mg/m²) × 6 cycles ± pelvic radiation
- **Pembrolizumab + carboplatin/paclitaxel (KEYNOTE-868):** dMMR: PFS not reached vs. 13.1 months; pMMR: PFS 13.1 vs. 8.7 months; FDA approved 2023 for 1st-line advanced/recurrent endometrial cancer (all comers, based on both dMMR and pMMR benefit) [^eskander-2023-ruby]
- **Dostarlimab + carboplatin/paclitaxel (RUBY trial):** dMMR subset: OS not reached vs. 30.2 months; FDA approved 2023

**Recurrent/metastatic:**
- **dMMR/MSI-H:** Pembrolizumab (ORR 57%); dostarlimab (ORR 44%); nivolumab; durvalumab — exceptional responses possible
- **pMMR (mismatch repair proficient):** Lenvatinib (VEGFR TKI) + pembrolizumab (KEYNOTE-146): ORR 38%, median PFS 7.2 months vs. 3.8 months; FDA approved 2019 for pMMR advanced endometrial cancer
- **ER+/PR+ endometrioid recurrence:** Progestin (medroxyprogesterone acetate, megestrol); aromatase inhibitor (letrozole); fulvestrant; everolimus + letrozole (32% CBR)
- **HER2+ serous:** Trastuzumab + carboplatin/paclitaxel (phase II benefit; ongoing phase III)
- **POLE-ultramutated:** Excellent ICI response even in advanced disease; single-agent pembrolizumab ORR ~75%

**Lynch syndrome-associated endometrial cancer:**
- Standard hysterectomy + BSO; Lynch patients benefit from prophylactic BSO at time of surgery (eliminates ovarian cancer risk)
- MSI-H → immunotherapy-responsive; adjuvant pembrolizumab under study in stage III-IV dMMR

## Connections

- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss-of-function mutations in ~50-80% of low-grade endometrioid endometrial cancer; earliest molecular event in endometrial carcinogenesis; PTEN loss → PI3K-AKT-mTOR activation → cell proliferation; mTOR inhibitors (everolimus + letrozole) active in ER+ endometrial cancer; germline PTEN mutations cause Cowden syndrome.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — dMMR/MSI-H endometrial cancer (~25-30%) responds to pembrolizumab; KEYNOTE-158 ORR 57% in dMMR endometrial; dostarlimab FDA approved 2021 for dMMR recurrent endometrial; RUBY trial (dostarlimab+carboplatin/paclitaxel) improved OS in dMMR subset; PD-1 blockade is standard for dMMR recurrent disease.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — ERBB2 (HER2) amplification in ~30% of uterine serous carcinoma (USC) and carcinosarcoma; trastuzumab + carboplatin/paclitaxel improved PFS vs. chemo alone (phase II, Fader 2018); HER2-positive USC is an actionable subset; T-DXd studied in HER2-low endometrial cancer; HER2 testing recommended for serous histology.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K/AKT/mTOR pathway activated in ~70% of endometrioid endometrial cancer via PTEN loss, PIK3CA mutation (~40%), or AKT1 E17K (~5%); everolimus + letrozole showed 32% clinical benefit rate in ER+ endometrial cancer; lenvatinib + pembrolizumab (KEYNOTE-146) active in non-MSI-H recurrent endometrial cancer.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Unopposed estrogen drives endometrial hyperplasia → EIN → type 1 endometrioid cancer; obesity → adipose aromatase → androgen-to-estrogen conversion → ~3× EC risk at BMI >30; aromatase inhibitors active in ER+ endometrial cancer; combined HRT (with progestogen) prevents EC risk.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Progesterone drives endometrial secretory transformation opposing estrogen proliferation; mifepristone (PR/GR antagonist) blocks P4 receptor → decidual breakdown → pregnancy termination; progesterone supplementation treats luteal phase deficiency and recurrent miscarriage.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Endometrial cancer is the sentinel cancer of Lynch syndrome: about half of female carriers present with it before any colorectal cancer, so a young or dMMR endometrial tumour should prompt germline testing — and these MSI-H cancers respond well to PD-1 immunotherapy.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity is the dominant modifiable driver of endometrial cancer: adipose aromatase converts androgens to estrogen, and this unopposed estrogen pushes endometrium through hyperplasia to type-1 endometrioid cancer — roughly tripling risk at BMI >30 and fueling rising incidence.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation defines the most aggressive endometrial cancers: near-universal (~90%) in uterine serous carcinoma, it marks the copy-number-high TCGA group with the worst prognosis, unlike the estrogen-driven endometrioid tumours — a split that now guides adjuvant therapy.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Endometrial and breast cancers are linked estrogen-driven cancers: unopposed estrogen and obesity raise risk of both, and tamoxifen used for breast cancer acts as a uterine estrogen agonist that increases endometrial cancer risk—so bleeding on tamoxifen warrants evaluation.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Endometrial and ovarian cancers frequently co-occur: ~10% of endometrioid endometrial cancers have a synchronous endometrioid ovarian primary, and both are core Lynch-syndrome tumors from mismatch-repair deficiency—so MMR/MSI testing and gynecologic surveillance span the two.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Endometrial and colorectal cancer are the defining Lynch-syndrome malignancies: germline mismatch-repair mutations (MLH1, MSH2/6, PMS2) drive microsatellite instability in both, endometrial cancer is often the sentinel cancer in women, and MSI-high tumors take immunotherapy.

[^konstantinopoulos-2019-dostarlimab]: Konstantinopoulos PA, Lheureux S, Moore KN. PARP inhibitors for ovarian and endometrial cancers: state of the art and clinical perspectives. *J Clin Oncol.* 2020;38(25):2896-2909. [doi:10.1200/JCO.20.00571](https://doi.org/10.1200/JCO.20.00571) · [PubMed 32706635](https://pubmed.ncbi.nlm.nih.gov/32706635/)
[^eskander-2023-ruby]: Eskander RN, Sill MW, Beffa L, et al. Pembrolizumab plus chemotherapy in advanced endometrial cancer. *N Engl J Med.* 2023;388(23):2159-2170. [doi:10.1056/NEJMoa2302312](https://doi.org/10.1056/NEJMoa2302312) · [PubMed 37166384](https://pubmed.ncbi.nlm.nih.gov/37166384/)
