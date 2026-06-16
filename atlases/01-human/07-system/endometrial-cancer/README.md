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
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Cowden syndrome is a hereditary cause of endometrial cancer: germline PTEN loss unleashes PI3K/mTOR signaling in the endometrium—the pathway mutated in most sporadic endometrioid tumors—so PTEN carriers face raised endometrial, breast, and thyroid cancer risk."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes and endometrial cancer are tied via obesity and hyperinsulinemia: excess insulin and adipose estrogen stimulate endometrial proliferation, so diabetic, obese women face much higher endometrial cancer risk—metformin is studied as prevention."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Mismatch-repair-deficient (MSI-high) endometrial cancer is highly immunotherapy-responsive: defective DNA repair generates abundant neoantigens that draw cytotoxic CD8+ T cells, so anti-PD-1 (dostarlimab, pembrolizumab) has transformed treatment of dMMR endometrial tumors."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is a key adjuvant in endometrial cancer: after hysterectomy, vaginal brachytherapy or pelvic external-beam photon radiation lowers local recurrence, and radiation can treat inoperable patients—complementing surgery in the commonest gynecologic cancer."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Endometrial cancer is the commonest gynecologic-tract cancer of the reproductive system: arising from the estrogen-responsive uterine lining, it is driven by unopposed estrogen, so the reproductive system's own hormonal milieu fuels the tumor."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "Endometrial and uterine tumors link endometrial cancer to HLRCC: fumarate-hydratase loss causes the uterine leiomyomas that name HLRCC and FH-deficient uterine cancers—so uterine smooth-muscle or endometrial tumors with a family history may flag the HLRCC mutation."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA mutation is among the commonest drivers of endometrial cancer: it activates the PI3K/AKT/mTOR growth pathway (often alongside PTEN loss), so this axis is a leading target for the mTOR and PI3K inhibitors being developed for the disease."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Endometrial cancer is tightly linked to insulin and metabolic excess: obesity and type 2 diabetes raise insulin and IGF-1, which—with the estrogen made by fat tissue—stimulate endometrial proliferation, explaining why metabolic disease so strongly raises risk."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Endometrial cancer is the prototypical hormone-dependent tumor of the endocrine system: unopposed estrogen without progesterone drives endometrial overgrowth, so conditions and drugs that disturb the estrogen-progesterone balance change the risk markedly."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Endometrial cancer is staged through the lymphatic system: spread to pelvic and para-aortic nodes drives staging and prognosis, so sentinel-lymph-node mapping now guides how aggressively surgery and adjuvant therapy are pursued."
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "CTNNB1 mutations define a deceptive endometrial subgroup: activating this Wnt/beta-catenin gene marks low-grade endometrioid tumors that look indolent but carry a surprisingly high recurrence risk—part of the molecular classification reshaping endometrial cancer care."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Endometrial cancer can spread to the lung: high-grade and serous subtypes disseminate hematogenously, making the lung a common distant metastatic site, so chest imaging is part of staging advanced or recurrent disease."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "Endometrial cancer's molecular classes hinge on MMR genes like MLH1: silencing of MLH1 by promoter methylation creates the common microsatellite-instability subtype, which is hypermutated and responds well to checkpoint immunotherapy—so MMR testing guides treatment."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Depth of myometrial invasion stages endometrial cancer, and fibroblasts pave the way: cancer-associated fibroblasts remodel the stroma to let tumor burrow into the muscle wall, and how deep it goes is a key prognostic factor guiding surgery."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Advanced endometrial cancer is treated by hitting VEGF: lenvatinib (a VEGFR inhibitor) plus pembrolizumab became a standard for recurrent disease, choking the tumor's blood supply while unleashing the immune system."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Body fat is the engine of endometrial cancer: adipocytes make aromatase that turns androgens into estrogen, so obesity floods the uterine lining with unopposed estrogen, making it the malignancy most strongly tied to excess weight."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver tunes endometrial-cancer risk through SHBG: it makes sex-hormone-binding globulin that mops up estrogen, and obesity and insulin resistance lower SHBG, raising the free estrogen that drives this hormone-sensitive tumor."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages connect obesity to endometrial cancer: inflamed fat draws macrophages that pour out cytokines, and tumor-associated macrophages in the uterine tumor promote its growth and blood supply, a cellular bridge from adiposity to malignancy."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Endometrial cancer announces itself by spending iron: abnormal uterine bleeding—especially after menopause—is the cardinal warning sign, and the chronic blood loss drains the body's iron into a deficiency anemia that often prompts the diagnosis."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells matter most in mismatch-repair-deficient endometrial cancer: these immunogenic tumors draw NK and T-cell attack, part of why such cancers respond well to immunotherapy that unleashes the immune assault."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Advanced endometrial cancer can threaten the kidneys: a bulky uterine tumor or its pelvic spread compresses the ureters, backing urine up into the kidneys (hydronephrosis) and causing post-renal kidney injury."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Endometrial cancer and its treatment leave fibrosis: a reactive desmoplastic stroma surrounds the tumor, and pelvic radiation scars nearby tissues, a late cause of bowel and bladder problems in survivors."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endometrial cancer drives angiogenesis: VEGF recruits endothelial cells to vascularize the tumor, and the fragile new vessels contribute to the abnormal bleeding that usually reveals it early."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Endometrial cancer can invade the bowel: locally advanced disease spreads to the rectum and sigmoid colon and seeds the peritoneum, complicating surgery and signaling advanced spread."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy separates endometrial cancer's two faces: the common endometrioid type keeps orderly glandular cells with microvilli, while the aggressive serous type shows papillary tufts and chaotic nuclei, an ultrastructural divide that tracks prognosis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Serous endometrial cancer leaves calcium fingerprints: like its ovarian counterpart it forms psammoma bodies, concentric calcium deposits whose presence on histology flags the high-grade serous subtype."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D ties into endometrial cancer through fat: deficiency travels with the obesity that is its biggest risk factor, and the vitamin's influence on cell growth and estrogen metabolism has made it a focus of prevention research."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The cancer announces itself in blood: postmenopausal bleeding is the cardinal early sign, and chronic abnormal uterine bleeding can drain enough red cells and iron to leave a woman anemic before the diagnosis is made."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Advanced disease draws on nerve-toxic chemotherapy: the carboplatin-paclitaxel regimen used for high-risk endometrial cancer injures peripheral sensory neurons, leaving the numbness and tingling of a taxane neuropathy."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Platinum chemotherapy wastes magnesium: the carboplatin paired with paclitaxel injures the kidney's tubular handling of the mineral, so magnesium is checked and replaced through endometrial cancer treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies now classify and treat it: mismatch-repair and p53 immunostains sort endometrial cancers into molecular groups, and the MMR-deficient tumors respond to checkpoint antibodies like dostarlimab and pembrolizumab."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The carboplatin-paclitaxel backbone empties the marrow: both drugs are myelosuppressive, dropping neutrophil counts between cycles so that growth-factor support and febrile-neutropenia watch run through advanced-disease treatment."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Diet and weight are the dominant levers: obesity-driven excess estrogen is the leading modifiable cause, so weight loss and a high-fiber, plant-rich diet that lowers circulating estrogen reduce endometrial cancer risk."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "The obesity-diabetes link runs through IGF-1: hyperinsulinemia raises bioactive IGF-1, a potent mitogen that, with excess estrogen, fuels endometrial proliferation — a molecular reason metabolic disease drives this cancer."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells help the tumor hide: they accumulate in the endometrial tumor microenvironment and damp the antitumor response, a dynamic that matters most in the mismatch-repair-deficient tumors targeted by immunotherapy."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "An STK11 syndrome raises the risk: Peutz-Jeghers syndrome predisposes to endometrial cancer and the rare cervical adenoma malignum, one of the inherited routes to gynecologic cancer beyond Lynch and Cowden."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "A chromatin gene falters early: ARID1A, part of the SWI/SNF remodeling complex, is frequently mutated in endometrioid endometrial cancer, loosening gene regulation as one of the disease's commonest driver events."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS pushes the endometrioid type: activating KRAS mutations fire the MAPK growth pathway in the estrogen-driven endometrioid subtype, often alongside PTEN and PIK3CA loss in the same tumor."
  - target: 01-human/03-molecular/msh2
    relation: connects-to
    note: "Lynch lands hardest on the womb: germline mismatch-repair defects in genes like MSH2 make endometrial cancer the sentinel cancer of Lynch syndrome in women, and the resulting MSI makes these tumors immunotherapy-responsive."
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
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Cowden syndrome is a hereditary cause of endometrial cancer: germline PTEN loss unleashes PI3K/mTOR signaling in the endometrium—the pathway mutated in most sporadic endometrioid tumors—so PTEN carriers face raised endometrial, breast, and thyroid cancer risk.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes and endometrial cancer are tied via obesity and hyperinsulinemia: excess insulin and adipose estrogen stimulate endometrial proliferation, so diabetic, obese women face much higher endometrial cancer risk—metformin is studied as prevention.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Mismatch-repair-deficient (MSI-high) endometrial cancer is highly immunotherapy-responsive: defective DNA repair generates abundant neoantigens that draw cytotoxic CD8+ T cells, so anti-PD-1 (dostarlimab, pembrolizumab) has transformed treatment of dMMR endometrial tumors.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is a key adjuvant in endometrial cancer: after hysterectomy, vaginal brachytherapy or pelvic external-beam photon radiation lowers local recurrence, and radiation can treat inoperable patients—complementing surgery in the commonest gynecologic cancer.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Endometrial cancer is the commonest gynecologic-tract cancer of the reproductive system: arising from the estrogen-responsive uterine lining, it is driven by unopposed estrogen, so the reproductive system's own hormonal milieu fuels the tumor.
- `connects-to` → **[HLRCC](../hlrcc/README.md)** — Endometrial and uterine tumors link endometrial cancer to HLRCC: fumarate-hydratase loss causes the uterine leiomyomas that name HLRCC and FH-deficient uterine cancers—so uterine smooth-muscle or endometrial tumors with a family history may flag the HLRCC mutation.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutation is among the commonest drivers of endometrial cancer: it activates the PI3K/AKT/mTOR growth pathway (often alongside PTEN loss), so this axis is a leading target for the mTOR and PI3K inhibitors being developed for the disease.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Endometrial cancer is tightly linked to insulin and metabolic excess: obesity and type 2 diabetes raise insulin and IGF-1, which—with the estrogen made by fat tissue—stimulate endometrial proliferation, explaining why metabolic disease so strongly raises risk.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Endometrial cancer is the prototypical hormone-dependent tumor of the endocrine system: unopposed estrogen without progesterone drives endometrial overgrowth, so conditions and drugs that disturb the estrogen-progesterone balance change the risk markedly.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Endometrial cancer is staged through the lymphatic system: spread to pelvic and para-aortic nodes drives staging and prognosis, so sentinel-lymph-node mapping now guides how aggressively surgery and adjuvant therapy are pursued.
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — CTNNB1 mutations define a deceptive endometrial subgroup: activating this Wnt/beta-catenin gene marks low-grade endometrioid tumors that look indolent but carry a surprisingly high recurrence risk—part of the molecular classification reshaping endometrial cancer care.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Endometrial cancer can spread to the lung: high-grade and serous subtypes disseminate hematogenously, making the lung a common distant metastatic site, so chest imaging is part of staging advanced or recurrent disease.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — Endometrial cancer's molecular classes hinge on MMR genes like MLH1: silencing of MLH1 by promoter methylation creates the common microsatellite-instability subtype, which is hypermutated and responds well to checkpoint immunotherapy—so MMR testing guides treatment.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Depth of myometrial invasion stages endometrial cancer, and fibroblasts pave the way: cancer-associated fibroblasts remodel the stroma to let tumor burrow into the muscle wall, and how deep it goes is a key prognostic factor guiding surgery.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Advanced endometrial cancer is treated by hitting VEGF: lenvatinib (a VEGFR inhibitor) plus pembrolizumab became a standard for recurrent disease, choking the tumor's blood supply while unleashing the immune system.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Body fat is the engine of endometrial cancer: adipocytes make aromatase that turns androgens into estrogen, so obesity floods the uterine lining with unopposed estrogen, making it the malignancy most strongly tied to excess weight.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver tunes endometrial-cancer risk through SHBG: it makes sex-hormone-binding globulin that mops up estrogen, and obesity and insulin resistance lower SHBG, raising the free estrogen that drives this hormone-sensitive tumor.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages connect obesity to endometrial cancer: inflamed fat draws macrophages that pour out cytokines, and tumor-associated macrophages in the uterine tumor promote its growth and blood supply, a cellular bridge from adiposity to malignancy.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Endometrial cancer announces itself by spending iron: abnormal uterine bleeding—especially after menopause—is the cardinal warning sign, and the chronic blood loss drains the body's iron into a deficiency anemia that often prompts the diagnosis.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells matter most in mismatch-repair-deficient endometrial cancer: these immunogenic tumors draw NK and T-cell attack, part of why such cancers respond well to immunotherapy that unleashes the immune assault.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Advanced endometrial cancer can threaten the kidneys: a bulky uterine tumor or its pelvic spread compresses the ureters, backing urine up into the kidneys (hydronephrosis) and causing post-renal kidney injury.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Endometrial cancer and its treatment leave fibrosis: a reactive desmoplastic stroma surrounds the tumor, and pelvic radiation scars nearby tissues, a late cause of bowel and bladder problems in survivors.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endometrial cancer drives angiogenesis: VEGF recruits endothelial cells to vascularize the tumor, and the fragile new vessels contribute to the abnormal bleeding that usually reveals it early.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Endometrial cancer can invade the bowel: locally advanced disease spreads to the rectum and sigmoid colon and seeds the peritoneum, complicating surgery and signaling advanced spread.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy separates endometrial cancer's two faces: the common endometrioid type keeps orderly glandular cells with microvilli, while the aggressive serous type shows papillary tufts and chaotic nuclei, an ultrastructural divide that tracks prognosis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Serous endometrial cancer leaves calcium fingerprints: like its ovarian counterpart it forms psammoma bodies, concentric calcium deposits whose presence on histology flags the high-grade serous subtype.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D ties into endometrial cancer through fat: deficiency travels with the obesity that is its biggest risk factor, and the vitamin's influence on cell growth and estrogen metabolism has made it a focus of prevention research.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The cancer announces itself in blood: postmenopausal bleeding is the cardinal early sign, and chronic abnormal uterine bleeding can drain enough red cells and iron to leave a woman anemic before the diagnosis is made.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Advanced disease draws on nerve-toxic chemotherapy: the carboplatin-paclitaxel regimen used for high-risk endometrial cancer injures peripheral sensory neurons, leaving the numbness and tingling of a taxane neuropathy.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Platinum chemotherapy wastes magnesium: the carboplatin paired with paclitaxel injures the kidney's tubular handling of the mineral, so magnesium is checked and replaced through endometrial cancer treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies now classify and treat it: mismatch-repair and p53 immunostains sort endometrial cancers into molecular groups, and the MMR-deficient tumors respond to checkpoint antibodies like dostarlimab and pembrolizumab.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The carboplatin-paclitaxel backbone empties the marrow: both drugs are myelosuppressive, dropping neutrophil counts between cycles so that growth-factor support and febrile-neutropenia watch run through advanced-disease treatment.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Diet and weight are the dominant levers: obesity-driven excess estrogen is the leading modifiable cause, so weight loss and a high-fiber, plant-rich diet that lowers circulating estrogen reduce endometrial cancer risk.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — The obesity-diabetes link runs through IGF-1: hyperinsulinemia raises bioactive IGF-1, a potent mitogen that, with excess estrogen, fuels endometrial proliferation — a molecular reason metabolic disease drives this cancer.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells help the tumor hide: they accumulate in the endometrial tumor microenvironment and damp the antitumor response, a dynamic that matters most in the mismatch-repair-deficient tumors targeted by immunotherapy.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — An STK11 syndrome raises the risk: Peutz-Jeghers syndrome predisposes to endometrial cancer and the rare cervical adenoma malignum, one of the inherited routes to gynecologic cancer beyond Lynch and Cowden.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — A chromatin gene falters early: ARID1A, part of the SWI/SNF remodeling complex, is frequently mutated in endometrioid endometrial cancer, loosening gene regulation as one of the disease's commonest driver events.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS pushes the endometrioid type: activating KRAS mutations fire the MAPK growth pathway in the estrogen-driven endometrioid subtype, often alongside PTEN and PIK3CA loss in the same tumor.
- `connects-to` → **[MSH2](../../03-molecular/msh2/README.md)** — Lynch lands hardest on the womb: germline mismatch-repair defects in genes like MSH2 make endometrial cancer the sentinel cancer of Lynch syndrome in women, and the resulting MSI makes these tumors immunotherapy-responsive.

[^konstantinopoulos-2019-dostarlimab]: Konstantinopoulos PA, Lheureux S, Moore KN. PARP inhibitors for ovarian and endometrial cancers: state of the art and clinical perspectives. *J Clin Oncol.* 2020;38(25):2896-2909. [doi:10.1200/JCO.20.00571](https://doi.org/10.1200/JCO.20.00571) · [PubMed 32706635](https://pubmed.ncbi.nlm.nih.gov/32706635/)
[^eskander-2023-ruby]: Eskander RN, Sill MW, Beffa L, et al. Pembrolizumab plus chemotherapy in advanced endometrial cancer. *N Engl J Med.* 2023;388(23):2159-2170. [doi:10.1056/NEJMoa2302312](https://doi.org/10.1056/NEJMoa2302312) · [PubMed 37166384](https://pubmed.ncbi.nlm.nih.gov/37166384/)
