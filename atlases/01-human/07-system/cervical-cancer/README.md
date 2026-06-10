---
schema: human-scale-entry/v1
id: cervical-cancer
name: Cervical Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Cervical cancer is HPV-driven in >99% of cases; HPV E6/E7 oncoproteins degrade p53 and inactivate RB → immortalization. Cisplatin + chemoradiation is standard for locally advanced; pembrolizumab + chemotherapy (KEYNOTE-826) is approved for PD-L1+ recurrent/metastatic disease."
aliases: ["cervical cancer", "cervical carcinoma", "HPV cervical cancer", "squamous cell carcinoma cervix", "cervical adenocarcinoma", "FIGO cervical cancer", "invasive cervical cancer"]
sources:
  - id: tewari-2014-gog240
    type: peer-reviewed
    cite: "Tewari KS, Sill MW, Long HJ 3rd, et al. Improved survival with bevacizumab in advanced cervical cancer. N Engl J Med. 2014;370(8):734-743."
    doi: "10.1056/NEJMoa1309748"
    pmid: "24552320"
    url: "https://doi.org/10.1056/NEJMoa1309748"
  - id: colombo-2021-keynote826
    type: peer-reviewed
    cite: "Colombo N, Dubot C, Lorusso D, et al. Pembrolizumab for persistent, recurrent, or metastatic cervical cancer. N Engl J Med. 2021;385(20):1856-1867."
    doi: "10.1056/NEJMoa2112435"
    pmid: "34534430"
    url: "https://doi.org/10.1056/NEJMoa2112435"
cross_links:
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Pembrolizumab + cisplatin/paclitaxel ± bevacizumab (KEYNOTE-826) improved OS vs chemotherapy in PD-L1 CPS≥1 persistent/recurrent/metastatic cervical cancer (24.4 vs 16.5 months); FDA approved 2021; cemiplimab showed similar OS benefit in EMPOWER-Cervical 1."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "HPV E7 oncoprotein binds RB LXCXE motif → RB inactivation → E2F release → S-phase entry; p16 INK4a (CDKN2A) overexpression is IHC surrogate for RB inactivation in cervical cancer; functional RB loss without mutation is universal in HPV-driven cervical carcinogenesis."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "HPV E6 recruits E6AP (UBE3A) ubiquitin ligase → p53 proteasomal degradation → loss of G1 checkpoint and apoptosis; p53 is wild-type but functionally absent in HPV+ cervical cancer; p53 mutation is rare and not required for HPV-driven carcinogenesis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Bevacizumab + cisplatin/paclitaxel (GOG-0240) improved OS vs chemotherapy alone (17.0 vs 13.3 months) in recurrent/metastatic cervical cancer; bevacizumab is standard for metastatic disease; KEYNOTE-826 added pembrolizumab to bevacizumab + chemotherapy for PD-L1+ patients."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: connects-to
    note: "HPV16/18 infect cervical transformation zone → E6-mediated p53 degradation + E7-mediated RB inactivation → CIN1-3 → invasive carcinoma; HPV16 accounts for ~55% of cervical SCC; viral genome integration disrupts E2 repressor → constitutive E6/E7 overexpression."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA mutations (E542K, E545K, H1047R) occur in ~35-40% of cervical SCC and adenocarcinoma → AKT-mTOR activation → proliferation; PIK3CA mutation cooperates with HPV E6/E7 in transformation; PI3K inhibitors (alpelisib) being studied in PIK3CA-mutant recurrent cervical cancer."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS mutations occur in ~10-15% of endocervical adenocarcinoma; gastric-type adenocarcinoma is HPV-independent with frequent KRAS + STK11 mutations; KRAS mutation predicts poor response to platinum chemotherapy; no approved KRAS inhibitors for cervical adenocarcinoma."
---

# Cervical Cancer

## Overview

**Cervical cancer** is the fourth most common cancer in women worldwide (~604,000 new cases/year, ~342,000 deaths/year), with the vast majority of cases driven by persistent **human papillomavirus (HPV)** infection — present in >99% of tumors. HPV16 and HPV18 together account for ~70% of cervical cancers; nonavalent vaccination (Gardasil 9, covering HPV6/11/16/18/31/33/45/52/58) and Pap/HPV co-test screening programs have dramatically reduced incidence in high-income countries, while the global burden remains concentrated in low-and-middle-income countries with limited access to vaccination and screening. HPV oncoproteins **E6** (degrades p53 via E6AP) and **E7** (inactivates RB) together immortalize cervical epithelial cells and suppress the DNA damage response. The systemic therapy landscape has been transformed by KEYNOTE-826, demonstrating that adding pembrolizumab to chemotherapy ± bevacizumab significantly prolongs survival in PD-L1-positive recurrent/metastatic disease [^colombo-2021-keynote826].

**Epidemiology:**
- ~14,000 new cases/year in the US; ~4,100 deaths/year; incidence declining due to HPV vaccination and Pap screening
- Globally: ~604,000 cases/year; most in sub-Saharan Africa, South Asia (limited screening/vaccination access)
- Peak incidence: 35-44 years (invasive cancer); CIN3/carcinoma in situ: 25-35 years
- 5-year survival: ~91% localized; ~58% regional; ~17% distant/metastatic
- Risk factors: HPV infection (necessary cause), smoking (2× risk), immunosuppression (HIV/organ transplant), multiple sexual partners, OCP use (weakly associated)

**Prevention:**
- **Gardasil 9 vaccination:** Covers 9 HPV types → ~90% of cervical cancer-causing types; recommended ages 9-26 (up to 45 shared decision-making); must be given before HPV exposure for full efficacy
- **Screening (US guidelines):** Pap smear alone every 3 years (21-29); Pap + HPV co-testing every 5 years or Pap alone every 3 years (30-65); colposcopy + biopsy for abnormal results → CIN1/2/3 → LEEP/cone biopsy

## Structure

### Histological subtypes

**Squamous cell carcinoma (SCC, ~70-75%):**
Arises from squamocolumnar junction (transformation zone) — the interface between ectocervical squamous epithelium and endocervical columnar epithelium; high-grade squamous intraepithelial lesion (HSIL/CIN3) is the obligate precursor; keratinizing and non-keratinizing variants; p16 IHC diffuse-positive as HPV surrogate; HPV16 most common

**Adenocarcinoma (~20-25%):**
Arises from endocervical columnar epithelium; HPV18 more commonly associated; usual-type endocervical adenocarcinoma (HPVA — HPV-associated adenocarcinoma) most common; gastric-type adenocarcinoma is HPV-independent (STK11/CDKN2A); adenocarcinoma of the endocervix is more difficult to detect on Pap smear → often presents at more advanced stage than SCC

**Adenosquamous carcinoma (<5%):**
Mixed squamous and glandular differentiation; aggressive; associated with HPV

**Rare subtypes:**
- Neuroendocrine carcinoma (small cell/large cell NEC): Aggressive; MYC amplification; treated with platinum+etoposide + chemoradiation; atezolizumab studied; similar to lung SCLC biology
- Clear cell carcinoma: DES-associated (diethylstilbestrol) in older patients; rare; non-HPV-driven; RNF43 mutation
- Undifferentiated carcinoma

### Molecular landscape

**HPV-driven (>99%):**
- HPV16 (~55-60%): High-risk; SCC-associated; highly oncogenic E6/E7
- HPV18 (~10-15%): Adenocarcinoma-associated; faster progression to invasion
- HPV31/33/45/52/58: Additional high-risk types in Gardasil 9

**Key somatic mutations (TCGA 2017):**
- **PIK3CA** mutations: ~35-40% of cervical SCC and adenocarcinoma; helical domain (E542K, E545K) and kinase domain (H1047R) mutations → AKT-mTOR pathway activation → PI3K inhibitors studied
- **PTEN** loss: ~15-20%; cooperates with PIK3CA in adenocarcinoma
- **FBXW7** mutation: ~15%; ubiquitin ligase targeting cyclin E, MYC, NOTCH for degradation
- **KRAS** mutations: ~10-15% of adenocarcinoma; less common in SCC
- **STK11/CDKN2A**: Gastric-type cervical adenocarcinoma (HPV-independent variant)
- **ERBB2 (HER2) amplification**: ~10% of adenocarcinoma; potential target
- **TMB:** Generally moderate; cervical cancer has ~2-3 mutations/Mb; not reliably TMB-high
- **PD-L1 CPS≥1:** ~75% of recurrent/metastatic cervical cancer; PD-L1 CPS≥10: ~50%

## Function

### HPV oncogenesis

**HPV life cycle and malignant transformation:**
HPV16/18 infects basal keratinocytes of the transformation zone via microabrasions → episomal replication → productive infection with viral particle production in differentiated upper layers. In cells that fail to complete the productive cycle, viral DNA may integrate into the host genome → disruption of the E2 open reading frame (which normally suppresses E6/E7) → constitutive E6/E7 overexpression → immortalization and malignant transformation.

**E6 oncoprotein — p53 destruction:**
HPV E6 binds E6AP (UBE3A, a HECT ubiquitin ligase) → E6-E6AP complex binds p53 tumor suppressor → ubiquitination of p53 → proteasomal degradation. Without functional p53, cells cannot arrest at G1 in response to DNA damage and cannot undergo p53-mediated apoptosis → accumulation of mutations → progression from CIN1 → CIN2 → CIN3 → invasive cancer.

**E7 oncoprotein — RB inactivation:**
HPV E7 binds the RB pocket domain at the LXCXE motif → dissociation of RB-E2F complexes → release of free E2F transcription factors → activation of E2F target genes (cyclin A, CDK2, thymidine kinase) → cell cycle entry without mitogenic signals. E7-driven RB inactivation also induces compensatory p16 INK4a (CDKN2A) overexpression — the basis for p16 IHC as a diagnostic marker for HPV infection in cervical pathology.

**Progression from CIN to invasive cancer:**
CIN1 (mild dysplasia) → HPV productive infection, often clears spontaneously (~70% within 1 year)
CIN2 → intermediate dysplasia; ~40-50% regression; high-risk E6/E7 expression
CIN3 (severe dysplasia/carcinoma in situ) → high-risk HPV; p53 + RB inactivated; near-zero spontaneous regression; direct precursor to invasive SCC
Invasive SCC → basement membrane penetration → lymphovascular invasion → nodal spread and distant metastasis

### Normal cervical transformation zone biology

The cervical transformation zone (TZ) — the area between the original and new squamocolumnar junctions — undergoes squamous metaplasia from columnar to squamous epithelium driven by acidic vaginal pH and hormonal changes at puberty. This area of active epithelial remodeling is particularly susceptible to HPV infection because basal cells are exposed during metaplastic transformation. Colposcopy identifies the TZ for targeted biopsy of abnormal areas.

## Pathology

### Staging and workup

**FIGO 2018 staging (clinical and pathological):**
- **Stage I:** Confined to cervix
  - IA1: Stromal invasion ≤3 mm; IA2: >3 to ≤5 mm
  - IB1: >5 mm to ≤2 cm; IB2: >2 to ≤4 cm; IB3: >4 cm
- **Stage II:** Beyond cervix, not to pelvic wall or lower vagina
  - IIA: Upper 2/3 vagina (IIA1: ≤4 cm; IIA2: >4 cm); IIB: Parametrial invasion
- **Stage III:** Pelvic wall, lower vagina, hydronephrosis, or positive nodes (pelvic → IIIC1; para-aortic → IIIC2)
- **Stage IV:** IVA: Bladder/rectal mucosa; IVB: Distant metastasis

**Staging workup:**
- MRI pelvis/abdomen: Primary tumor extent, parametrial invasion, nodal staging — superior to CT for soft tissue assessment
- CT chest/abdomen/pelvis: Lymph node and distant metastasis staging
- FDG-PET/CT: Standard for node-positive or ≥IB3 disease; detects para-aortic lymph node metastasis → alters radiation field; superior sensitivity to CT for nodal staging
- Cystoscopy/proctoscopy: For suspected IVA disease (bladder/rectal involvement)
- Biopsy: Colposcopy-directed or simple punch biopsy of visible lesion for diagnosis

### Treatment

**Early-stage (IA1 with no LVI to IB2):**
- **Surgery:** Radical hysterectomy + bilateral pelvic lymph node dissection (BPLND) ± sentinel lymph node mapping; preferred for young women wishing to avoid radiation-induced ovarian failure
  - IA1 without LVI: Simple hysterectomy or cone biopsy (fertility preservation)
  - IA1 with LVI / IA2 / IB1: Modified radical or radical hysterectomy + PLND
- **Adjuvant chemoradiation** for high-risk pathologic features: Positive margins, positive pelvic nodes, parametrial invasion (GOG-92: pelvic RT; GOG-109: cisplatin+RT superior to RT alone)
- **Fertility-preserving:** Radical trachelectomy + PLND for select IB1 (<2 cm, no LVI, negative MRI nodes)

**Locally advanced (IB3-IVA):**
- **Concurrent cisplatin (40 mg/m² weekly) + external beam radiation therapy (EBRT) + brachytherapy:** Standard of care; based on multiple RTOG trials (GOG-120, GOG-123, RTOG 90-01); cisplatin sensitizes tumor to radiation; EBRT 45-50 Gy to pelvis → high-dose-rate (HDR) intracavitary brachytherapy boost (85-90 Gy EQD2 to HRCTV); 5-year OS ~65-70% for IIB-IIIA
- Carboplatin as cisplatin alternative in renal insufficiency; inferior but acceptable
- **Extended-field RT:** Para-aortic RT for PET-positive para-aortic nodes → improved regional control

**Recurrent/metastatic (persistent or R/M) first-line:**
- **Pembrolizumab + cisplatin/paclitaxel ± bevacizumab (KEYNOTE-826):** [^colombo-2021-keynote826] OS 24.4 vs 16.5 months (PD-L1 CPS≥1) vs chemotherapy alone; PFS 10.4 vs 8.2 months; FDA approved 2021; standard first-line for PD-L1+ R/M cervical cancer
- **Bevacizumab + cisplatin/paclitaxel (GOG-0240):** [^tewari-2014-gog240] OS 17.0 vs 13.3 months vs chemo alone; FDA approved 2014; first targeted agent to improve OS in cervical cancer; ORR 48%; now used with pembrolizumab for PD-L1+ patients
- **Cemiplimab + chemotherapy ± bevacizumab (EMPOWER-Cervical 1):** OS benefit vs chemotherapy in PD-L1+ population; cemiplimab approved 2022 for R/M cervical cancer

**Second-line and beyond:**
- **Tisotumab vedotin (TV, Tivdak):** Antibody-drug conjugate targeting tissue factor (TF) with MMAE warhead; ORR ~24% (innovaTV 204 single-arm); OS benefit vs investigator's choice in TV-301 (phase III); FDA approved 2021 (accelerated), 2023 (regular approval)
- **Pembrolizumab monotherapy:** Active in PD-L1+ recurrent cervical cancer (ORR ~12-14% as monotherapy in KEYNOTE-158)
- **Topotecan:** Standard cytotoxic in 2nd-line; ORR ~13%; used with bevacizumab
- **Ifosfamide:** Active in sarcomatoid variant

## Connections

- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Pembrolizumab + cisplatin/paclitaxel ± bevacizumab (KEYNOTE-826) improved OS vs chemotherapy in PD-L1 CPS≥1 persistent/recurrent/metastatic cervical cancer (24.4 vs 16.5 months); FDA approved 2021; cemiplimab showed similar OS benefit in EMPOWER-Cervical 1.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — HPV E7 oncoprotein binds RB LXCXE motif → RB inactivation → E2F release → S-phase entry; p16 INK4a (CDKN2A) overexpression is IHC surrogate for RB inactivation in cervical cancer; functional RB loss without mutation is universal in HPV-driven cervical carcinogenesis.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — HPV E6 recruits E6AP (UBE3A) ubiquitin ligase → p53 proteasomal degradation → loss of G1 checkpoint and apoptosis; p53 is wild-type but functionally absent in HPV+ cervical cancer; p53 mutation is rare and not required for HPV-driven carcinogenesis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Bevacizumab + cisplatin/paclitaxel (GOG-0240) improved OS vs chemotherapy alone (17.0 vs 13.3 months) in recurrent/metastatic cervical cancer; bevacizumab is standard for metastatic disease; KEYNOTE-826 added pembrolizumab to bevacizumab + chemotherapy for PD-L1+ patients.
- `connects-to` → **[HPV-16](../../../02-pathogen/01-viruses/hpv-16/README.md)** — HPV16/18 infect cervical transformation zone → E6-mediated p53 degradation + E7-mediated RB inactivation → CIN1-3 → invasive carcinoma; HPV16 accounts for ~55% of cervical SCC; viral genome integration disrupts E2 repressor → constitutive E6/E7 overexpression.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutations (E542K, E545K, H1047R) occur in ~35-40% of cervical SCC and adenocarcinoma → AKT-mTOR activation → proliferation; PIK3CA mutation cooperates with HPV E6/E7 in transformation; PI3K inhibitors (alpelisib) being studied in PIK3CA-mutant recurrent cervical cancer.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS mutations occur in ~10-15% of endocervical adenocarcinoma; gastric-type adenocarcinoma is HPV-independent with frequent KRAS + STK11 mutations; KRAS mutation predicts poor response to platinum chemotherapy; no approved KRAS inhibitors for cervical adenocarcinoma.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^tewari-2014-gog240]: Tewari KS, Sill MW, Long HJ 3rd, et al. Improved survival with bevacizumab in advanced cervical cancer. *N Engl J Med.* 2014;370(8):734-743. [doi:10.1056/NEJMoa1309748](https://doi.org/10.1056/NEJMoa1309748) · [PubMed 24552320](https://pubmed.ncbi.nlm.nih.gov/24552320/)
[^colombo-2021-keynote826]: Colombo N, Dubot C, Lorusso D, et al. Pembrolizumab for persistent, recurrent, or metastatic cervical cancer. *N Engl J Med.* 2021;385(20):1856-1867. [doi:10.1056/NEJMoa2112435](https://doi.org/10.1056/NEJMoa2112435) · [PubMed 34534430](https://pubmed.ncbi.nlm.nih.gov/34534430/)
