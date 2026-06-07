---
schema: human-scale-entry/v1
id: atypical-teratoid-rhabdoid-tumor
name: Atypical Teratoid/Rhabdoid Tumor
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "AT/RT (atypical teratoid/rhabdoid tumor) is an aggressive CNS WHO grade 4 pediatric tumor defined by SMARCB1 biallelic LOF (~95%) or SMARCA4 LOF (~5%); peak <3 years; three molecular subgroups (TYR, SHH, MYC); multimodal therapy; 2-year OS ~40-50%; germline SMARCB1 → RTPS1."
aliases: ["AT/RT", "atypical teratoid rhabdoid tumor", "ATRT", "rhabdoid tumor brain", "INI1-deficient CNS tumor", "SMARCB1 brain tumor", "SMARCB1-deficient tumor", "pediatric CNS rhabdoid", "rhabdoid tumor predisposition"]
sources:
  - id: biegel-1999-ini1-atrt
    type: peer-reviewed
    cite: "Biegel JA, Zhou JY, Rorke LB, Stenstrom C, Wainwright LM, Fogelgren B. Germ-line and acquired mutations of INI1 in atypical teratoid and rhabdoid tumors. Cancer Res. 1999;59(1):74-79."
    doi: "10.1158/0008-5472.CAN-58-1-74"
    pmid: "9892189"
    url: "https://pubmed.ncbi.nlm.nih.gov/9892189/"
  - id: fruhwald-2020-atrt-subgroups
    type: peer-reviewed
    cite: "Frühwald MC, Hasselblatt M, Nemes K, et al. Age and DNA methylation subgroup as potential treatment targets in children with atypical teratoid rhabdoid tumors. Neuro Oncol. 2020;22(7):1006-1017."
    doi: "10.1093/neuonc/noz244"
    pmid: "31900478"
    url: "https://doi.org/10.1093/neuonc/noz244"
cross_links:
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "SMARCB1 biallelic LOF defines AT/RT (~95% of cases); INI1 IHC (loss of nuclear staining) is the diagnostic standard; germline SMARCB1 → RTPS1 with multi-focal rhabdoid tumors at birth; SMARCA4-mutant AT/RT (~5%) is clinically similar."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "SMARCB1 LOF → PRC2/EZH2 unrestricted → H3K27me3 at BAF-target loci (CDKN2A, HOX, differentiation genes); AT/RT cells are EZH2-dependent; tazemetostat reduces H3K27me3 and restores differentiation markers; AT/RT EZH2 inhibition is in clinical trials."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "AT/RT-MYC subgroup (~30%): MYC overexpression via BRD4-occupied super-enhancers (SMARCB1 loss → BRD4 unrestricted); supratentorial, older patients; BET inhibitors (JQ1) suppress MYC in AT/RT-MYC cells; ONC201 (DRD2 antagonist) investigated in AT/RT."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations are absent in most AT/RT; SMARCB1 loss → ARF epigenetically silenced → MDM2 unrestricted → p53 degraded without TP53 mutation; p53 suppression via ARF silencing (not TP53 mutation) is the primary p53-pathway inactivation mechanism in SMARCB1-null rhabdoid tumors."
---

# Atypical Teratoid/Rhabdoid Tumor

## Overview

**Atypical teratoid/rhabdoid tumor (AT/RT)** is a highly malignant CNS neoplasm (WHO grade 4, 2021) defined by biallelic inactivation of **SMARCB1** (INI1/BAF47, chromosome 22q11.23) in ~95% of cases, or **SMARCA4** (BRG1) in ~5%. AT/RT is the most common malignant brain tumor in **infants under 1 year** (~50% of pediatric malignant brain tumors <12 months) and accounts for ~1-2% of all pediatric CNS tumors. Approximately 50-60 cases are diagnosed per year in the USA. Despite intensive multimodal therapy, AT/RT remains one of the most devastating pediatric cancers, with 2-year OS ~40-50% and a markedly worse prognosis in infants (<18 months) and patients with disseminated disease [^fruhwald-2020-atrt-subgroups].

The tumor derives its name from its mixed histology: rhabdoid cells (classic morphology) co-exist with primitive neuroectodermal, mesenchymal, and epithelial components — resembling a teratoma. However, unlike true teratomas, AT/RT has a single driver molecular event (SMARCB1/SMARCA4 LOF) underlying its apparent lineage plasticity.

**Sites:** Infratentorial (posterior fossa, ~50-60%): cerebellar hemisphere, brainstem, cerebellopontine angle; supratentorial (~30-40%); spinal cord/cauda equina (~5-10%); leptomeningeal dissemination at diagnosis in ~30-40%.

**Germline SMARCB1 (RTPS1):**
~30-35% of AT/RT patients carry germline SMARCB1 mutations (compared to ~5% for most pediatric brain tumors). Rhabdoid tumor predisposition syndrome type 1 (RTPS1) confers risk for AT/RT, malignant rhabdoid tumor of the kidney (MRT), and extra-renal rhabdoid tumors; infants with synchronous CNS + renal rhabdoid tumors typically carry germline mutations; genetic testing at diagnosis is mandatory for all AT/RT patients.

## Structure

### Molecular subgroups (WHO 2021 / DNA methylation-based)

Three AT/RT subgroups defined by DNA methylation profiling and gene expression [^fruhwald-2020-atrt-subgroups]:

**AT/RT-TYR (~35%):**
- Dominant gene expression: tyrosinase (TYR), MITF overexpression → melanocytic differentiation signature
- Location: posterior fossa (cerebellum, brainstem)
- Age: youngest patients (median ~5-9 months)
- Genetic: SMARCB1 LOF (deletion predominant); high CDKN2A deletion rate (~30%)
- Prognosis: worst OS among subgroups (~30-35% 2-year OS); aggressive; responds poorly to chemotherapy

**AT/RT-SHH (~35%):**
- Dominant gene expression: GLI2, MYCN, PTCH1 → SHH pathway activation
- Location: supratentorial and posterior fossa; spinal cord
- Age: broader age range (median ~18-24 months), some older children
- Genetic: SMARCB1 LOF (point mutations and deletions); highest rate of germline SMARCB1
- Prognosis: intermediate (~45-55% 2-year OS)

**AT/RT-MYC (~30%):**
- Dominant gene expression: MYC, HOTAIR, mesenchymal markers
- Location: supratentorial predominant; suprasellar/3rd ventricular region
- Age: older children (median ~24-36 months); some school-age children
- Genetic: SMARCB1 LOF (point mutations predominant); CDKN2A deletion less frequent
- Prognosis: relatively better (~55-65% 2-year OS); longer PFS after HDC/ASCR in some series

### Histology

**Classic rhabdoid cells:**
Large cells (15-25 μm) with eccentric nuclei, prominent eosinophilic nucleoli ("owl-eye"), and abundant pale eosinophilic cytoplasm with fibrillary or globular inclusions (intermediate filament whorls); cells mimic skeletal muscle cells (rhabdomyoblasts) morphologically but are not myogenic.

**IHC panel:**
- **INI1 (SMARCB1) by IHC**: complete loss of nuclear staining in tumor cells (retained in endothelium, lymphocytes, normal glia) — diagnostic; ~95-100% sensitive for AT/RT; negative INI1 in any undifferentiated pediatric brain tumor should trigger molecular workup
- Vimentin: ~90-100% positive
- EMA (epithelial membrane antigen): ~80% positive
- SMA (smooth muscle actin): ~40-50% positive
- Synaptophysin, GFAP, cytokeratin: variable (reflects lineage plasticity)
- CD99: variable; MIB-1 (Ki-67): typically >80%

**Ultra-rare variant:**
SMARCA4-deficient AT/RT: identical morphology and prognosis; SMARCA4 IHC (BRG1) shows loss of nuclear staining; SMARCB1 IHC intact; must test both in INI1-intact rhabdoid-appearing tumors.

## Function

### Normal SWI/SNF biology in CNS

In the normal CNS, SMARCB1-containing BAF complex is essential for:
- Neural stem cell self-renewal and lineage restriction
- Neuron differentiation (BAF complexes switch subunit composition from npBAF in neural progenitors → nBAF in postmitotic neurons)
- Oligodendrocyte maturation (BRG1-containing BAF required for myelination gene activation)
- SMARCB1 specifically maintains open chromatin at enhancers of differentiation TFs → loss of SMARCB1 → epigenetic reprogramming toward an undifferentiated rhabdoid state

AT/RT epigenome is characterized by global **H3K27me3 accumulation** (due to unopposed PRC2 activity) at genes that mediate neural differentiation, lineage identity, and the G1 checkpoint — explaining the morphologic primitiveness and mixed lineage marker expression.

## Pathology

### Molecular drivers

**Primary driver (obligate):**
- **SMARCB1 biallelic LOF** (~95%): deletions (single exon, partial gene, or whole-gene deletion at 22q11.23) in ~60%; intragenic frameshift/truncating mutations in ~35%; rarely inactivating missense
- **SMARCA4 biallelic LOF** (~5%): equivalent mechanism via BRG1 loss (also SMARCB1-independent BRG1 loss in aggressive undifferentiated thoracic tumors — a distinct entity)

**Secondary alterations (rare in AT/RT — oligogenomic tumor):**
- **CDKN2A deletion** (~15-25%): second most common alteration; SMARCB1-mediated CDKN2A silencing is epigenetic (reversible), but true deletion is permanent and associated with worse prognosis
- **TP53 mutations**: rare (~5-8%); when present, correlate with Li-Fraumeni background
- **PIK3CA mutations**: ~5%; mTOR pathway activation
- **MYC amplification** (<5%): distinct from AT/RT-MYC subgroup (which has high MYC expression without amplification in most cases)
- AT/RT has remarkably simple genomic landscape (compared to GBM or medulloblastoma) — SMARCB1 LOF is sufficient for full oncogenic transformation

### Treatment

AT/RT has no established standard of care; protocols are protocol-driven and center-specific, with COG and EU-RHAB providing the largest prospective datasets.

**Standard multimodal approach:**
1. **Surgery**: maximal safe resection (GTR associated with better OS in all series); ETV/VP shunt for hydrocephalus
2. **Induction chemotherapy**: typically ICT (ifosfamide, carboplatin, etoposide) or High-Dose Intensive Chemotherapy regimens (IVADo: ifosfamide, vincristine, dactinomycin + doxorubicin); European SIOPE/EU-RHAB protocols use VEC (vincristine, etoposide, carboplatin) + HD-MTX
3. **Consolidation**: HDC + autologous stem cell rescue (HDC/ASCR): most common regimen — thiotepa-based or carboplatin+thiotepa+etoposide; shown to improve EFS vs non-HDC historical controls; tandem ASCR in some centers
4. **Radiation therapy**: CSI + local boost; deferred in infants <36 months (severe neurocognitive effects); focal stereotactic RT for older children; proton preferred (reduce integral dose); role of radiation in AT/RT-TYR vs AT/RT-MYC subgroups may differ

**COG ACNS0333 (published 2023):** N=65 evaluable patients; head-trauma (HD) induction + HDC/ASCR × 2 cycles + focal RT; 4-year EFS 37%; 4-year OS 43%; best results in non-disseminated AT/RT-SHH; AT/RT-TYR had worst outcomes; no late relapses beyond 3 years.

**EU-RHAB registry (Frühwald 2020):** [^fruhwald-2020-atrt-subgroups] N=147 patients; intensive multimodal treatment (surgery + chemotherapy ± HDC ± RT); 3-year OS 43%; subgroup differences: AT/RT-SHH and AT/RT-MYC showed significantly better OS than AT/RT-TYR (log-rank p<0.001); germline SMARCB1 did NOT independently predict worse outcome after stratification by subgroup and metastasis.

**Prognosis by clinical factors:**
- Non-disseminated + GTR + AT/RT-SHH or AT/RT-MYC + age >18 months: 3-year OS ~60-70%
- Disseminated disease at diagnosis: 3-year OS ~15-25%
- Age <12 months: 3-year OS ~25-35% (radiation not given, limiting local control)
- Germline SMARCB1 (RTPS1): prognosis similar to sporadic AT/RT when matched for subgroup

**Novel therapies (investigational):**
- **Tazemetostat (EZH2 inhibitor)**: FDA-approved for epithelioid sarcoma (SMARCB1-null); Phase 1/2 in AT/RT (COG ADVL1213/PBTC): NCT trials ongoing; H3K27me3 reduction documented in tumor biopsies; response rates ~10-20% in early data
- **ONC201 (DRD2/DRD3 antagonist)**: activity in Group 4 MB; being evaluated in AT/RT-MYC (MYC overexpression downstream of dopaminergic signaling); Phase 1 pediatric trial
- **Anti-PD-1 (pembrolizumab, nivolumab)**: low TMB in AT/RT limits expected immunotherapy benefit; PD-L1 expressed variably; trials ongoing in recurrent AT/RT
- **Alisertib (AURKA inhibitor)**: Phase 2 in recurrent AT/RT; modest activity; synergizes with SMARCB1 rescue in preclinical models
- **BET inhibitors**: strong preclinical rationale (MYC suppression in AT/RT-MYC); mivebresib and ZEN-3694 in early trials

**Radiation considerations:**
- CSI 36 Gy + boost 54-59.4 Gy (standard for non-infant, localized AT/RT)
- Focal RT 54-59.4 Gy (some centers for localized non-disseminated AT/RT >12-18 months)
- Proton beam preferred (HiRES trial ongoing comparing proton vs photon in pediatric CNS)
- Radiation omission in infants → high local and distant failure rates; some centers use focal stereotactic for isolated posterior fossa disease

## Connections

- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — SMARCB1 biallelic LOF defines AT/RT (~95% of cases); INI1 IHC (loss of nuclear staining) is the diagnostic standard; germline SMARCB1 → RTPS1 with multi-focal rhabdoid tumors at birth; SMARCA4-mutant AT/RT (~5%) is clinically similar.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — SMARCB1 LOF → PRC2/EZH2 unrestricted → H3K27me3 at BAF-target loci (CDKN2A, HOX, differentiation genes); AT/RT cells are EZH2-dependent; tazemetostat reduces H3K27me3 and restores differentiation markers; AT/RT EZH2 inhibition is in clinical trials.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — AT/RT-MYC subgroup (~30%): MYC overexpression via BRD4-occupied super-enhancers (SMARCB1 loss → BRD4 unrestricted); supratentorial, older patients; BET inhibitors (JQ1) suppress MYC in AT/RT-MYC cells; ONC201 (DRD2 antagonist) investigated in AT/RT.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations are absent in most AT/RT; SMARCB1 loss → ARF epigenetically silenced → MDM2 unrestricted → p53 degraded without TP53 mutation; p53 suppression via ARF silencing (not TP53 mutation) is the primary p53-pathway inactivation mechanism in SMARCB1-null rhabdoid tumors.

[^biegel-1999-ini1-atrt]: Biegel JA, Zhou JY, Rorke LB, Stenstrom C, Wainwright LM, Fogelgren B. Germ-line and acquired mutations of INI1 in atypical teratoid and rhabdoid tumors. *Cancer Res.* 1999;59(1):74-79. [PubMed 9892189](https://pubmed.ncbi.nlm.nih.gov/9892189/)
[^fruhwald-2020-atrt-subgroups]: Frühwald MC, Hasselblatt M, Nemes K, et al. Age and DNA methylation subgroup as potential treatment targets in children with atypical teratoid rhabdoid tumors. *Neuro Oncol.* 2020;22(7):1006-1017. [doi:10.1093/neuonc/noz244](https://doi.org/10.1093/neuonc/noz244) · [PubMed 31900478](https://pubmed.ncbi.nlm.nih.gov/31900478/)
