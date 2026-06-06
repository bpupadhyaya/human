---
schema: medicine-entry/v1
id: targeted-therapy
name: Targeted Therapy
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Small molecules or antibodies targeting specific oncoproteins driving tumor growth: kinase inhibitors (imatinib/BCR-ABL, erlotinib/EGFR, vemurafenib/BRAF), HER2 inhibitors (trastuzumab), VEGF inhibitors (bevacizumab). Exploits oncogene addiction."
aliases: ["molecularly targeted therapy", "precision oncology", "kinase inhibitors", "targeted cancer therapy", "oncogene-targeted therapy", "tyrosine kinase inhibitors", "TKI"]
drug_class: targeted antineoplastic
modality: small molecule / monoclonal antibody
key_agents:
  - imatinib (Gleevec/Glivec) — BCR-ABL/KIT/PDGFR inhibitor
  - erlotinib (Tarceva) — EGFR kinase inhibitor
  - vemurafenib (Zelboraf) — BRAF V600E inhibitor
  - trastuzumab (Herceptin) — anti-HER2 monoclonal antibody
  - bevacizumab (Avastin) — anti-VEGF monoclonal antibody
  - crizotinib (Xalkori) — ALK/ROS1/MET inhibitor
sources:
  - id: druker-2001-imatinib
    type: peer-reviewed
    cite: "Druker BJ, Talpaz M, Resta DJ, et al. Efficacy and safety of a specific inhibitor of the BCR-ABL tyrosine kinase in chronic myeloid leukemia. N Engl J Med. 2001;344(14):1031-7."
    doi: "10.1056/NEJM200104053441401"
    pmid: "11287972"
    url: "https://doi.org/10.1056/NEJM200104053441401"
  - id: slamon-2001-trastuzumab
    type: peer-reviewed
    cite: "Slamon DJ, Leyland-Jones B, Shak S, et al. Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. N Engl J Med. 2001;344(11):783-92."
    doi: "10.1056/NEJM200103153441101"
    pmid: "11248153"
    url: "https://doi.org/10.1056/NEJM200103153441101"
  - id: lynch-2004-egfr-mutation
    type: peer-reviewed
    cite: "Lynch TJ, Bell DW, Sordella R, et al. Activating mutations in the epidermal growth factor receptor underlying responsiveness of non-small-cell lung cancer to gefitinib. N Engl J Med. 2004;350(21):2129-39."
    doi: "10.1056/NEJMoa040938"
    pmid: "15118073"
    url: "https://doi.org/10.1056/NEJMoa040938"
cross_links:
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: modulates
    evidence: druker-2001-imatinib
    note: "Some targeted therapies (imatinib, vemurafenib) increase tumour immunogenicity by reducing immunosuppressive signaling in the tumour microenvironment, enhancing CD8+ T cell infiltration and synergising with checkpoint inhibitor combinations."
  - target: 01-human/03-molecular/tnf-alpha
    relation: modulates
    evidence: slamon-2001-trastuzumab
    note: "EGFR/HER2 signaling activates NF-κB which drives TNF-α and pro-inflammatory cytokine production in tumor cells; EGFR inhibitors and trastuzumab reduce this NF-κB activation, shifting the tumour microenvironment cytokine milieu."
  - target: 01-human/07-system/immune-system
    relation: modulates
    evidence: druker-2001-imatinib
    note: "Targeted therapies have selective effects on immune cells: VEGF inhibition (bevacizumab) reduces immunosuppressive regulatory T cells and improves T cell trafficking into tumors; imatinib depletes immunosuppressive MDSCs; some EGFR inhibitors enhance antigen presentation."
---

# Targeted Therapy

## Overview

Targeted cancer therapy encompasses **small molecules and monoclonal antibodies** designed to interfere with specific molecular targets — proteins encoded by oncogenes or amplified/mutated signaling components — that cancer cells depend on for survival and proliferation, a concept termed **oncogene addiction**. Unlike conventional chemotherapy, which kills all rapidly dividing cells, targeted agents exploit the specific molecular vulnerabilities of tumor cells while sparing most normal tissues, producing a more favorable therapeutic index.

The conceptual breakthrough came from two simultaneously published 2001 NEJM papers:

1. **Druker et al.** demonstrating that imatinib — a BCR-ABL tyrosine kinase inhibitor — produced complete haematological responses in nearly all chronic myeloid leukaemia (CML) patients, converting a disease requiring allogeneic bone marrow transplant into one manageable with a daily oral pill [^druker-2001-imatinib]

2. **Slamon et al.** demonstrating that adding trastuzumab (anti-HER2 monoclonal antibody) to chemotherapy dramatically improved survival in HER2-overexpressing metastatic breast cancer [^slamon-2001-trastuzumab]

These landmark results established the **molecular target + driver mutation/amplification → matched drug** paradigm that now defines precision oncology. Companion diagnostic testing (e.g., FISH for HER2 amplification, PCR/NGS for EGFR/BRAF/ALK mutations) to identify the target is an integral part of treatment eligibility.

## Mechanism

### Classes and Targets

**Kinase Inhibitors — Small Molecules**

Protein kinases (phosphotransferases) are the most heavily mutated/amplified oncoproteins in cancer; kinase inhibitors occupy the ATP-binding pocket and compete with ATP for binding, preventing phosphorylation of downstream substrates:

| Drug | Target | Cancer | Resistance Mechanism |
|:---|:---|:---|:---|
| **Imatinib** (Gleevec) | BCR-ABL, c-KIT, PDGFRα/β | CML, GIST, Ph+ ALL | ABL T315I gatekeeper mutation; BCR-ABL amplification |
| **Dasatinib** | BCR-ABL (+ Src family), covers most imatinib resistance | CML | T315I (dasatinib-resistant) |
| **Erlotinib / gefitinib** | EGFR (sensitising mutations: exon 19 del, exon 21 L858R) | NSCLC | EGFR T790M (exon 20); bypass via MET amp |
| **Osimertinib** (Tagrisso) | EGFR (3rd gen; covers T790M) | NSCLC (1st and 2nd line) | C797S; MET amplification |
| **Vemurafenib / dabrafenib** | BRAF V600E | Melanoma, NSCLC | BRAF splice variants; RAS mutations; MEK-ERK reactivation |
| **Crizotinib** | ALK, ROS1, MET | NSCLC (ALK-rearranged), MET-amplified | ALK secondary mutations; bypass via EGFR/KIT |
| **Alectinib** (2nd gen) | ALK (covers crizotinib resistance) | NSCLC | ALK G1202R |
| **Ibrutinib** | BTK (Bruton's tyrosine kinase) | CLL, MCL, WM | BTK C481S mutation |
| **Palbociclib / ribociclib** | CDK4/6 (cell cycle kinases) | HR+/HER2- breast cancer | Rb loss; CDK6 amplification |

**Monoclonal Antibodies**

| Drug | Target | Cancer | Mechanism |
|:---|:---|:---|:---|
| **Trastuzumab** (Herceptin) | HER2 extracellular domain IV | HER2+ breast cancer, gastric cancer | Blocks HER2 dimerisation + PI3K-Akt; ADCC via IgG1 Fc; internalisation/degradation |
| **Pertuzumab** | HER2 extracellular domain II | HER2+ breast cancer | Prevents HER2:HER3 heterodimer; synergistic with trastuzumab |
| **Bevacizumab** (Avastin) | VEGF-A | CRC, ovarian, NSCLC, glioblastoma | Neutralises VEGF → prevents tumour angiogenesis → ischaemia-driven tumour growth arrest |
| **Cetuximab** | EGFR extracellular domain | CRC (RAS wild-type), HNC | Blocks EGF binding; ADCC; internalisation |
| **Ramucirumab** | VEGFR-2 | Gastric, NSCLC, CRC | Blocks VEGF-A/C/D binding → anti-angiogenic |

**Antibody-Drug Conjugates (ADCs)** — next generation targeted agents:

| Drug | Target + Payload | Indication |
|:---|:---|:---|
| **Ado-trastuzumab emtansine (T-DM1, Kadcyla)** | HER2 + emtansine (microtubule inhibitor) | HER2+ breast cancer (after trastuzumab + taxane) |
| **Trastuzumab deruxtecan (T-DXd, Enhertu)** | HER2 + topoisomerase I inhibitor (DXd) | HER2+ and HER2-low breast, gastric, NSCLC |
| **Sacituzumab govitecan (Trodelvy)** | TROP2 + SN-38 (irinotecan metabolite) | TNBC, urothelial carcinoma |

### Oncogene Addiction Principle

Cancer cells that have acquired an activating driver mutation in an oncogene (e.g., EGFR L858R, BRAF V600E, BCR-ABL fusion) often become **dependent on that single pathway for proliferation and survival** — rewiring their signaling so that inhibition of the mutant oncoprotein is lethal while normal cells, which have redundant signaling networks, can survive. This "oncogene addiction" provides the therapeutic window for targeted inhibitors and explains why inhibition of a single kinase is sufficient for profound tumour regression in selected patients.

### Acquired Resistance Mechanisms

All targeted therapies eventually develop resistance (median ~12 months for first-generation EGFR inhibitors, several years for imatinib in CML):

- **On-target resistance:** Secondary mutations in the ATP-binding pocket or regulatory domains (e.g., EGFR T790M, ABL T315I, BRAF splice variants) — overcome by next-generation agents (osimertinib for T790M)
- **Off-target bypass:** Amplification or mutation of a downstream or parallel pathway node (e.g., MET amplification bypassing EGFR; NF1 loss reactivating RAS bypassing BRAF inhibition; RET rearrangement after EGFR inhibitor)
- **Phenotypic transformation:** Epithelial-to-mesenchymal transition (EMT); NSCLC → small-cell transformation (~5% on EGFR inhibitors)
- **Histological: Clonal evolution:** Pre-existing resistant subclones (polyclonal tumours) selected under drug pressure

## Clinical Use

### CML and Imatinib — Disease Transformation

Chronic myeloid leukaemia (CML) is driven by the **Philadelphia chromosome** t(9;22)(q34;q11) translocation, creating the **BCR-ABL1 fusion oncogene** — a constitutively active tyrosine kinase. Before imatinib, CML required allogeneic bone marrow transplant for potential cure (long-term OS ~50–60% with significant transplant mortality) or was managed with IFN-α (cytogenetic responses in ~20–30%).

Imatinib transformed CML into a **chronic, manageable condition**:
- 10-year follow-up of IRIS trial: 83% complete cytogenetic response; 10-year OS ~82%; most patients never progress to blast crisis
- Current practice: patients achieving deep molecular response (MR4.5) can attempt treatment-free remission — ~50% sustain remission off imatinib (functional cure)

### HER2+ Breast Cancer and Trastuzumab

Slamon et al. [^slamon-2001-trastuzumab] randomised 469 women with HER2-overexpressing metastatic breast cancer to chemotherapy ± trastuzumab:
- **Time to progression: 7.4 vs. 4.6 months** (HR 0.51, p<0.001)
- **Median OS: 25.1 vs. 20.3 months** (p=0.046) — meaningful survival extension
- Subsequent adjuvant trials (HERA, NSABP B-31, NCCTG N9831): trastuzumab reduced recurrence by ~50% and mortality by ~33% in early HER2+ breast cancer — major practice-changing outcome

### EGFR-Mutant NSCLC

Lynch et al. [^lynch-2004-egfr-mutation] identified activating **EGFR mutations (exon 19 deletions, exon 21 L858R)** in NSCLC adenocarcinoma tumors sensitive to gefitinib, explaining the dramatically differential response rates observed in Asian women non-smokers with adenocarcinoma vs. unselected populations:
- In EGFR-mutant NSCLC: erlotinib/gefitinib → ORR ~60–70% vs. 10–15% with chemotherapy; median PFS 9–11 months
- Osimertinib (3rd gen) achieves 18.9-month median PFS in EGFR-mutant NSCLC (FLAURA trial) and penetrates CNS metastases — now preferred first-line

### BRAF V600E Melanoma

BRAF V600E mutation occurs in ~50% of cutaneous melanomas. Vemurafenib/dabrafenib + MEK inhibitor (trametinib/cobimetinib) combinations:
- **ORR: ~70%** in BRAF V600E melanoma
- Median PFS: 11–12 months (combination); single agent ~6–7 months
- Combination outperforms monotherapy (reduces paradoxical MAPK reactivation and cutaneous toxicities including squamous cell carcinoma)
- Checkpoint inhibitor combinations (dabrafenib + trametinib + pembrolizumab) under active investigation

## Evidence

| Trial | Agents | Population | Key Result |
|:---|:---|:---|:---|
| **IRIS** (Druker 2001/O'Brien 2003) | Imatinib vs. IFN+Ara-C | CML chronic phase | CCyR: 83% vs. 17%; 10-y OS: 82% |
| **HER2 metastatic trial** (Slamon 2001) | Trastuzumab + chemo vs. chemo | HER2+ metastatic BC | TTP HR 0.51; OS benefit 4.8 months |
| **HERA** (2011 update) | Adjuvant trastuzumab 1 year | Early HER2+ BC | DFS HR 0.76; OS HR 0.74 |
| **FLAURA** | Osimertinib vs. erlotinib/gefitinib | EGFR-mutant NSCLC | PFS 18.9 vs. 10.2 months; OS HR 0.80 |
| **COMBI-d** | Dabrafenib + trametinib | BRAF V600E melanoma | PFS 11.0 vs. 8.8 months; OS 25.1 vs. 18.7 months |
| **DESTINY-Breast04** | T-DXd vs. chemo | HER2-low BC | PFS 9.9 vs. 5.1 months; OS 23.4 vs. 16.8 months |

## Connections

- **Modulates** → [Cytotoxic T Cell](../../../../01-human/04-cellular/t-cytotoxic-cell/README.md): Kinase inhibitors (imatinib, vemurafenib) increase tumour immunogenicity by reducing immunosuppressive cytokines in the TME, enhancing CD8+ T cell infiltration and synergising with checkpoint inhibitors in combination strategies.
- **Modulates** → [TNF-α](../../../../01-human/03-molecular/tnf-alpha/README.md): EGFR/HER2/RAS signaling activates NF-κB-driven TNF-α production in tumor cells; targeted kinase inhibitors reduce this NF-κB activation, shifting the TME cytokine milieu toward a less immunosuppressive state.
- **Modulates** → [Immune System](../../../../01-human/07-system/immune-system/README.md): Bevacizumab (anti-VEGF) reduces immunosuppressive MDSC/Treg recruitment by blocking VEGF-mediated immunosuppression; normalises tumour vasculature, improving T cell trafficking; imatinib depletes MDSCs; EGFR inhibitors upregulate MHC-I on tumour cells.

[^druker-2001-imatinib]: Druker BJ, Talpaz M, Resta DJ, et al. Efficacy and safety of a specific inhibitor of the BCR-ABL tyrosine kinase in chronic myeloid leukemia. *N Engl J Med.* 2001;344(14):1031-7. [doi:10.1056/NEJM200104053441401](https://doi.org/10.1056/NEJM200104053441401) · [PubMed 11287972](https://pubmed.ncbi.nlm.nih.gov/11287972/)
[^slamon-2001-trastuzumab]: Slamon DJ, Leyland-Jones B, Shak S, et al. Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. *N Engl J Med.* 2001;344(11):783-92. [doi:10.1056/NEJM200103153441101](https://doi.org/10.1056/NEJM200103153441101) · [PubMed 11248153](https://pubmed.ncbi.nlm.nih.gov/11248153/)
[^lynch-2004-egfr-mutation]: Lynch TJ, Bell DW, Sordella R, et al. Activating mutations in the epidermal growth factor receptor underlying responsiveness of non-small-cell lung cancer to gefitinib. *N Engl J Med.* 2004;350(21):2129-39. [doi:10.1056/NEJMoa040938](https://doi.org/10.1056/NEJMoa040938) · [PubMed 15118073](https://pubmed.ncbi.nlm.nih.gov/15118073/)
