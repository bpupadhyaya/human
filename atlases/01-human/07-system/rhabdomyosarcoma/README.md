---
schema: human-scale-entry/v1
id: rhabdomyosarcoma
name: Rhabdomyosarcoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Rhabdomyosarcoma is the most common pediatric soft tissue sarcoma; embryonal (~60%, VAC backbone, 5-year FFS ~90% low-risk) and alveolar (~25%, PAX3/PAX7-FOXO1 fusions, high-risk) subtypes; VAC±irinotecan; RT; metastatic disease 5-year OS ~20-30%."
aliases: ["rhabdomyosarcoma", "RMS", "embryonal RMS", "alveolar RMS", "ERMS", "ARMS", "pediatric soft tissue sarcoma", "botryoid RMS"]
sources:
  - id: crist-2001-irs4-rms
    type: peer-reviewed
    cite: "Crist WM, Anderson JR, Meza JL, et al. Intergroup rhabdomyosarcoma study-IV: results for patients with nonmetastatic disease. J Clin Oncol. 2001;19(12):3091-3102."
    doi: "10.1200/JCO.2001.19.12.3091"
    pmid: "11408506"
    url: "https://doi.org/10.1200/JCO.2001.19.12.3091"
  - id: oberlin-2012-mmt95-rms
    type: peer-reviewed
    cite: "Oberlin O, Rey A, Sanchez de Toledo J, et al. Randomized comparison of intensified six-drug versus standard three-drug chemotherapy for high-risk nonmetastatic rhabdomyosarcoma and other chemotherapy-sensitive childhood soft tissue sarcomas. J Clin Oncol. 2012;30(19):2457-2465."
    doi: "10.1200/JCO.2011.39.3538"
    pmid: "22665546"
    url: "https://doi.org/10.1200/JCO.2011.39.3538"
cross_links:
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "PAX3-FOXO1 t(2;13) (~55% ARMS) and PAX7-FOXO1 t(1;13) (~20% ARMS) are the defining fusions of alveolar RMS; PAX3-FOXO1 confers worse prognosis than PAX7-FOXO1; fusion status is the most important molecular prognostic factor in RMS."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "PAX3-FOXO1 drives MYCN expression in ARMS; MYCN amplification in fusion-negative RMS → poor prognosis; MYC amplification in pleomorphic RMS; BET inhibitors suppress MYC/MYCN in RMS preclinically; CDK4 is also a downstream PAX3-FOXO1 target."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT is constitutively active in most RMS subtypes via PTEN deletion (~10%), PIK3CA mutation, or IGF2 overexpression; AKT inactivates FOXO1 → removes cell cycle arrest; CDK4/6 inhibitors and PI3K inhibitors are explored in combination for RMS."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "PAX3-FOXO1 transcriptionally activates MET (HGF receptor) → invasion in alveolar RMS; MET overexpression in >50% ARMS; crizotinib active in MET-expressing pediatric solid tumors; MET amplification is an additional adverse prognostic factor in fusion-positive ARMS."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Rhabdomyosarcoma — especially embryonal, in young children — is one of the sentinel soft-tissue sarcomas of Li-Fraumeni syndrome; germline TP53 should be considered in any child with RMS under 3 or with a suggestive family history, as it also signals radiation-sparing caution."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Embryonal RMS is driven by an IGF2/IGF1R autocrine loop: 11p15.5 loss of imprinting unleashes biallelic IGF2, which signals through IGF1R → PI3K-AKT-mTOR for proliferation and survival; IGF1R antibodies have been tried but show limited single-agent activity."
  - target: 01-human/03-molecular/dicer1
    relation: connects-to
    note: "DICER1 syndrome predisposes to embryonal rhabdomyosarcoma, classically of the uterine cervix and in pleuropulmonary blastoma–associated tumors; biallelic DICER1 disrupts miRNA processing, so a young woman's cervical botryoid RMS should prompt germline DICER1 testing."
---

# Rhabdomyosarcoma

## Overview

**Rhabdomyosarcoma (RMS)** is the most common **pediatric soft tissue sarcoma**, accounting for ~3-4% of all childhood cancers and ~50% of pediatric soft tissue sarcomas. RMS arises from primitive mesenchymal precursors committed to the skeletal muscle lineage (expressing myogenic TFs: MYOD1, myogenin), though it can occur in sites without skeletal muscle (bladder, vagina, middle ear) — reflecting the myogenic progenitor origin from embryonic mesoderm. The two major clinically relevant histological subtypes are **embryonal RMS (ERMS, ~60%)** and **alveolar RMS (ARMS, ~25%)**: ERMS is driven by complex copy number alterations and loss of heterozygosity at 11p15 (IGF2 imprinting loss); ARMS is defined by PAX3-FOXO1 or PAX7-FOXO1 chromosomal translocations that create chimeric oncogenic transcription factors. Treatment is multimodal: the **VAC backbone** (vincristine+actinomycin D+cyclophosphamide) established by the Intergroup Rhabdomyosarcoma Studies (IRS) remains the cornerstone [^crist-2001-irs4-rms]; radiation therapy is critical for residual/unresected disease; intensified regimens (VAC+irinotecan, six-drug therapy) have been explored for high-risk disease but do not clearly improve outcomes in metastatic RMS [^oberlin-2012-mmt95-rms].

**Epidemiology:**
- ~350-400 cases/year USA; ~5,000/year globally
- Median age: ~5 years (ERMS bimodal: peak <5 and 10-17); ~16 years for ARMS
- Male predominance (~1.4:1 overall); orbital RMS: female slight predominance
- Primary sites: head/neck (~35%), genitourinary (~25%), extremity (~20%), trunk/retroperitoneum (~15%)
- ~15-20% have metastatic disease at diagnosis; 5-year OS: localized ~70-80%, metastatic ~20-30%

## Structure

### Molecular classification

**Embryonal RMS (ERMS, ~60%):**
- Molecular: No fusion gene; 11p15.5 loss of heterozygosity → IGF2 imprinting loss → IGF2 overexpression → IGF1R signaling; complex karyotype; gain of whole chromosomes (7, 8, 13); NRAS mutations (~10%), KRAS mutations, PIK3CA mutations; MYOD1 L122R in sclerosing variant; CTNNB1 mutations rare; DICER1 mutations in embryonal pleural pulmonary blastoma-associated RMS
- Prognosis: Generally better than ARMS; low-risk ERMS: 5-year FFS ~90%; intermediate-risk: ~65-80%
- Location: Head/neck (orbital — best prognosis, parameningeal — high-risk), genitourinary (bladder/prostate, vagina/uterus), extremity

**Alveolar RMS (ARMS, ~25%):**
- Molecular: PAX3-FOXO1 t(2;13)(q35;q14) ~55%; PAX7-FOXO1 t(1;13)(p36;q14) ~20%; fusion-negative ARMS ~25% (behaves like ERMS molecularly and prognostically); FISH for FOXO1 rearrangement is essential for all histologically ARMS and RMS-ambiguous cases
- Prognosis: Fusion-positive ARMS (especially PAX3-FOXO1): 5-year OS ~50-60%; PAX7-FOXO1: ~70-75%; fusion-negative ARMS: ~75% (reclassified as ERMS in practice)
- Location: Extremity, trunk, parameningeal — typically non-genitourinary

**Sclerosing/Spindle Cell RMS:**
- Molecular: MYOD1 L122R mutation (~25%); VGLL2 and NCOA2 fusions (in infantile spindle cell variant — good prognosis); SRF-NCOA2 fusion
- Prognosis: Highly variable; MYOD1 L122R → poor prognosis despite relatively low-grade histological appearance; NCOA2-fused: excellent prognosis in infants

**Pleomorphic RMS:**
- Adults (rare in children); no fusion genes; complex karyotype; myogenic markers (desmin, myogenin) positive; very poor prognosis (5-year OS <20%); treated as adult high-grade sarcoma (gemcitabine/docetaxel, ifos/doxo)

### Histology and immunophenotype

**ERMS:** Hypercellular areas alternating with loosely myxoid stroma; rhabdomyoblasts (elongated, tadpole-shaped cells with abundant eosinophilic cytoplasm); cross-striations may be visible; variable differentiation; **botryoid RMS** (variant): polypoid grape-like clusters beneath mucosal surface in hollow organs (bladder, vagina, nasopharynx) → "cambium layer" (hypercellular zone immediately deep to surface epithelium) → diagnostic feature.

**ARMS:** Pseudo-alveolar spaces separated by fibrovascular septa; loosely cohesive small round blue cells lining the septa like a respiratory alveolus; solid variant (may lack alveolar pattern) → FISH essential.

**Immunophenotype:**
- Desmin+, vimentin+ (mesenchymal)
- Myogenin+ (nuclear; more diffuse in ARMS — ~75% cells; focal in ERMS — <10% cells)
- MYOD1+ (nuclear; present in all variants)
- MyoD1 (protein) and Myogenin are the most diagnostic IHC markers for any RMS type
- CD99 variable (positive in ~50% — can cause confusion with Ewing)
- ALK negative (unlike inflammatory myofibroblastic tumor)
- SMA variable, S100 negative

## Function

### Pathophysiology

**RMS as an arrested myogenic differentiation:**
Normal skeletal muscle regeneration: satellite cells (Pax7+, Myf5+) activate → MYOD1 expression → myoblast → MYOG (myogenin) → myocyte → fusion → myofiber; PAX3-FOXO1 recapitulates early myogenic gene activation (MYOD1, FGFR4, MET) without allowing terminal differentiation → cells express early myogenic markers but cannot complete the differentiation program → arrested blast state that proliferates.

**IGF2-IGF1R autocrine in ERMS:**
11p15 LOH → biallelic IGF2 expression → autocrine IGF2 → IGF1R → PI3K-AKT-mTOR → ERMS proliferation and survival; FOXO1 is inactivated by AKT in ERMS → loss of FOXO1-mediated differentiation signals; PI3K inhibitors and IGF1R antibodies explored but have limited single-agent activity.

**PAX3-FOXO1 myogenic reprogramming:**
PAX3-FOXO1 hijacks the PAX3 myogenic regulatory network → activates MYOD1 enhancers → MYOD1 expression without differentiation context (because PAX3-FOXO1 also represses myogenin's differentiation program through competitive binding); the result: high MYOD1 with low differentiated muscle gene expression → proliferative blast state; CDK4 overexpression from PAX3-FOXO1 → sustained cell cycle progression.

## Pathology

### Staging — IRS grouping

| IRS Group | Definition |
|----------|-----------|
| I | Complete resection, no microscopic residual |
| II | Regional disease; complete resection with microscopic residual (Group IIA) or positive regional lymph nodes, completely resected (Group IIB/C) |
| III | Incomplete resection with gross residual disease |
| IV | Distant metastases at onset |

**TNM staging** also applied (T1/T2 × a/b + N + M); combined to create risk groups for treatment.

**Risk groups (COG):**
- **Low risk:** Stage 1 or 2, Group I/II, ERMS histology; or Stage 1, Group I/II, ARMS; 5-year FFS ~90%
- **Intermediate risk:** Stage 1-3, Group III, ERMS; or Stage 2-3, Group I/II/III, ARMS; or Stage 4 <10 years ERMS; 5-year FFS ~55-65%
- **High risk:** Stage 4 (metastatic), any age, ARMS; or Stage 4, ≥10 years; 5-year FFS ~20-30%

### Treatment

**Chemotherapy backbone — VAC:**
Vincristine (1.5 mg/m² IV weekly, max 2 mg) + actinomycin D (0.045 mg/kg or 1.5 mg/m² IV Days 1-5, max 2 mg) + cyclophosphamide (2.2 g/m² IV) every 3 weeks; mesna uroprotection; IRS-IV established VAC as standard backbone; IRS-IV (N=883): randomized comparison of VAC vs VAI (ifosfamide substituted) vs VIE (ifosfamide+etoposide) → no significant difference in outcome, confirming VAC as standard [^crist-2001-irs4-rms]; G-CSF support required for subsequent courses.

**VAC + irinotecan (intermediate/high-risk):**
Irinotecan added to VAC for intermediate and high-risk RMS: ARST0431 (high-risk, N=109): VAC/IE with vincristine, irinotecan → 3-year EFS ~38% for metastatic ARMS; ARST0531 (intermediate-risk): VAC+irinotecan improved 5-year EFS slightly vs VAC alone; current COG standard incorporates irinotecan for intermediate/high-risk RMS.

**Intensified regimens (six-drug):**
SIOP MMT95 (Oberlin 2012): randomized comparison 6-drug (IVA+vincristine/doxorubicin/etoposide, 6-drug) vs 3-drug (IVA) in high-risk non-metastatic RMS → no benefit from intensification (5-year EFS 64% vs 64%); intensification not superior to standard 3-drug for non-metastatic high-risk RMS [^oberlin-2012-mmt95-rms].

**Radiation therapy:**
RT is mandatory for all Group II-IV disease and Group I ARMS:
- Embryonal low-risk Group I: VAC alone × 24 weeks, no RT
- Orbital/parameningeal: 45-50.4 Gy (IMRT or proton preferred); CNS extension → craniospinal RT
- Extremity: 45-50.4 Gy; proton beam to spare growth plate/normal tissue
- Bladder/prostate: 45 Gy proton; if complete resection achievable by surgery → surgery preferred to preserve bladder function
- Whole-lung: 15-18 Gy for lung metastases (concurrent with maintenance chemo)

**Surgery:**
Maximal safe resection with negative margins (R0) wherever achievable without mutilation; for orbital, parameningeal, bladder-prostate, vaginal primaries — extensive upfront surgery avoided; preoperative (induction) chemotherapy to shrink tumor → delayed definitive surgery (DSS) after response evaluation; second-look surgery after induction to assess response and achieve resection.

**Novel/investigational agents:**
- **CDK4/6 inhibitors (palbociclib):** PAX3-FOXO1 → CDK4; SARC037: palbociclib in pediatric RMS — Phase 1 data favorable; ongoing Phase 2 randomized
- **Anti-GD2 (dinutuximab):** GD2 expressed on RMS; COG ANBL1422: dinutuximab + irinotecan+temsirolimus in pediatric solid tumors including RMS
- **MET inhibitors (crizotinib):** COG ADVL1312: crizotinib Phase 1 including RMS cohort; RMS responses observed in MET-positive tumors
- **Anti-PD-1/PD-L1:** PD-L1 expressed in ~40% RMS; pembrolizumab Phase 2 in pediatric solid tumors including RMS; limited data; genomically quiet ERMS may be less immunogenic
- **Cabozantinib:** Multi-TKI (MET/VEGFR/AXL/RET); Phase 2 in R/R pediatric solid tumors
- **BET inhibitors:** Phase 1 studies evaluating BRD4/MYC suppression in ARMS; combination with CDK4/6 inhibitors explored

**Relapsed RMS:**
- Topotecan+cyclophosphamide (TC): ORR ~30-35%; standard salvage
- Irinotecan+temozolomide (IT): ORR ~25%
- Gemcitabine+docetaxel: ORR ~15-20% in pediatric RMS; better in adult pleomorphic RMS
- Vinorelbine+cyclophosphamide (metronomic): modest ORR; less toxicity; continuous low-dose oral
- Allo-SCT: No established role in R/R RMS; high TRM without demonstrated survival benefit

### Long-term effects

- **Infertility:** Cyclophosphamide → gonadal damage; cryopreservation recommended; LMWD (lowest-effective-dose) cyclophosphamide strategies
- **Growth:** RT to bone → growth plate damage → limb length discrepancy, scoliosis
- **Bladder function:** Pelvic/bladder RT → urinary dysfunction; bladder-prostate RMS — bladder-preservation approach has reduced late urinary morbidity substantially
- **Secondary malignancy:** Alkylator → MDS/AML; RT field → secondary sarcoma (10+ year latency)
- **Cardiac:** Cyclophosphamide → hemorrhagic cystitis (with mesna prophylaxis); late cardiomyopathy if doxorubicin used (most protocols minimize doxorubicin in RMS)

## Connections

- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — PAX3-FOXO1 t(2;13) (~55% ARMS) and PAX7-FOXO1 t(1;13) (~20% ARMS) are the defining fusions of alveolar RMS; PAX3-FOXO1 confers worse prognosis than PAX7-FOXO1; fusion status is the most important molecular prognostic factor in RMS.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — PAX3-FOXO1 drives MYCN expression in ARMS; MYCN amplification in fusion-negative RMS → poor prognosis; MYC amplification in pleomorphic RMS; BET inhibitors suppress MYC/MYCN in RMS preclinically; CDK4 is also a downstream PAX3-FOXO1 target.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT is constitutively active in most RMS subtypes via PTEN deletion (~10%), PIK3CA mutation, or IGF2 overexpression; AKT inactivates FOXO1 → removes cell cycle arrest; CDK4/6 inhibitors and PI3K inhibitors are explored in combination for RMS.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — PAX3-FOXO1 transcriptionally activates MET (HGF receptor) → invasion in alveolar RMS; MET overexpression in >50% ARMS; crizotinib active in MET-expressing pediatric solid tumors; MET amplification is an additional adverse prognostic factor in fusion-positive ARMS.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Rhabdomyosarcoma — especially embryonal, in young children — is one of the sentinel soft-tissue sarcomas of Li-Fraumeni syndrome; germline TP53 should be considered in any child with RMS under 3 or with a suggestive family history, as it also signals radiation-sparing caution.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Embryonal RMS is driven by an IGF2/IGF1R autocrine loop: 11p15.5 loss of imprinting unleashes biallelic IGF2, which signals through IGF1R → PI3K-AKT-mTOR for proliferation and survival; IGF1R antibodies have been tried but show limited single-agent activity.
- `connects-to` → **[DICER1](../../03-molecular/dicer1/README.md)** — DICER1 syndrome predisposes to embryonal rhabdomyosarcoma, classically of the uterine cervix and in pleuropulmonary blastoma–associated tumors; biallelic DICER1 disrupts miRNA processing, so a young woman's cervical botryoid RMS should prompt germline DICER1 testing.

[^crist-2001-irs4-rms]: Crist WM, Anderson JR, Meza JL, et al. Intergroup rhabdomyosarcoma study-IV: results for patients with nonmetastatic disease. *J Clin Oncol.* 2001;19(12):3091-3102. [doi:10.1200/JCO.2001.19.12.3091](https://doi.org/10.1200/JCO.2001.19.12.3091) · [PubMed 11408506](https://pubmed.ncbi.nlm.nih.gov/11408506/)
[^oberlin-2012-mmt95-rms]: Oberlin O, Rey A, Sanchez de Toledo J, et al. Randomized comparison of intensified six-drug versus standard three-drug chemotherapy for high-risk nonmetastatic rhabdomyosarcoma and other chemotherapy-sensitive childhood soft tissue sarcomas. *J Clin Oncol.* 2012;30(19):2457-2465. [doi:10.1200/JCO.2011.39.3538](https://doi.org/10.1200/JCO.2011.39.3538) · [PubMed 22665546](https://pubmed.ncbi.nlm.nih.gov/22665546/)
