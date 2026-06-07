---
schema: human-scale-entry/v1
id: pdgf
name: PDGF
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Growth factor family (PDGF-AA/AB/BB) signaling via PDGFR-alpha/beta → RAS-MAPK and PI3K-AKT → fibroblast and smooth muscle proliferation. Drives cancer stroma fibrosis with TGF-beta; imatinib and sunitinib target PDGFR in GIST, systemic mastocytosis, and dermatofibrosarcoma."
aliases: ["platelet-derived growth factor", "PDGFR", "PDGF-AA", "PDGF-BB", "PDGFR-alpha", "PDGFR-beta", "PDGFA", "PDGFB", "PDGFRA", "PDGFRB"]
sources:
  - id: heldin-1998-pdgf-review
    type: peer-reviewed
    cite: "Heldin CH, Östman A, Rönnstrand L. Signal transduction via platelet-derived growth factor receptors. Biochim Biophys Acta. 1998;1378(1):F79-F113."
    doi: "10.1016/S0304-419X(98)00015-8"
    pmid: "9739761"
    url: "https://doi.org/10.1016/S0304-419X(98)00015-8"
  - id: demetri-2002-imatinib-gist
    type: peer-reviewed
    cite: "Demetri GD, von Mehren M, Blanke CD, et al. Efficacy and safety of imatinib mesylate in advanced gastrointestinal stromal tumors. N Engl J Med. 2002;347(7):472-480."
    doi: "10.1056/NEJMoa020461"
    pmid: "12181401"
    url: "https://doi.org/10.1056/NEJMoa020461"
  - id: andrae-2008-pdgf-cancer
    type: peer-reviewed
    cite: "Andrae J, Gallini R, Betsholtz C. Role of platelet-derived growth factors in physiology and medicine. Genes Dev. 2008;22(10):1276-1312."
    doi: "10.1101/gad.1653708"
    pmid: "18483217"
    url: "https://doi.org/10.1101/gad.1653708"
cross_links:
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "PDGF-BB and TGF-beta cooperate to activate hepatic stellate cells and cancer-associated fibroblasts → fibrosis; PDGF drives CAF proliferation; TGF-beta drives collagen synthesis; dual PDGFR/TGF-beta inhibition reduces tumor stroma in experimental pancreatic and hepatic fibrosis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PDGFR-alpha/beta signal via PI3K-AKT → mTORC1 activation → fibroblast and smooth muscle cell proliferation; mTOR inhibitors reduce PDGF-driven SMC proliferation in pulmonary arterial hypertension; PDGFR + mTOR inhibition has preclinical synergy in GIST and sarcomas."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "PDGFR and EGFR activate overlapping RAS-ERK and PI3K-AKT downstream pathways; PDGF transactivates EGFR via Src → amplified signaling; multi-kinase inhibitors (sunitinib, sorafenib) targeting both PDGFR and RAS-pathway RTKs exploit these downstream convergences."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "PDGFR-B on pericytes is required for vessel maturation after VEGF-driven sprouting; PDGF-BB → pericyte recruitment → stable vessels; anti-VEGF therapy → PDGF-B dependency → resistance; sunitinib and sorafenib co-target VEGFR + PDGFR → broader antiangiogenic activity."
---

# PDGF

## Overview

**Platelet-derived growth factor (PDGF)** is a **family of dimeric growth factors** that signal through tyrosine kinase receptors (PDGFR-alpha and PDGFR-beta) to drive **mesenchymal cell proliferation, migration, and survival** — particularly fibroblasts, smooth muscle cells, pericytes, and their precursors [^heldin-1998-pdgf-review]. Originally identified in platelets as a mitogen for smooth muscle cells (thus "platelet-derived"), PDGF is now understood to be widely expressed in many cell types and plays essential roles in embryonic development, wound healing, and tissue homeostasis — as well as in pathological processes including fibrosis, cancer stroma formation, pulmonary arterial hypertension (PAH), and tumor angiogenesis.

**PDGF isoforms:**
- **PDGF-AA:** Binds PDGFR-alpha homodimer; expressed by neurons, fibroblasts; regulates oligodendrocyte precursor recruitment and differentiation; important in CNS development
- **PDGF-AB:** Binds PDGFR-alpha homodimer and PDGFR-alpha/beta heterodimer; widely expressed
- **PDGF-BB:** Binds all PDGFR isoforms (alpha-alpha, alpha-beta, beta-beta); most potent PDGF; produced by platelets, macrophages, endothelial cells; key driver of pericyte recruitment and smooth muscle cell proliferation; **oncogenic in GIST and dermatofibrosarcoma protuberans (DFSP)**
- **PDGF-CC and PDGF-DD:** Discovered later; require proteolytic activation; PDGF-CC → PDGFR-alpha; PDGF-DD → PDGFR-beta; expressed in mesenchymal and epithelial tissues; roles in heart, liver fibrosis

**PDGFR-alpha and PDGFR-beta:**
- Both are single-pass transmembrane receptor tyrosine kinases with 5 extracellular Ig-like loops, transmembrane domain, and split intracellular kinase domain
- **PDGFR-alpha:** Broadly expressed on fibroblasts, neural progenitors, glial progenitors, smooth muscle, pericytes; ligands: PDGF-AA, AB, BB, CC
- **PDGFR-beta:** More restricted — pericytes, smooth muscle cells, mesangial cells; key for vascular development; ligands: PDGF-BB, AB, DD; PDGFR-beta on pericytes is required for blood vessel maturation
- **Dimerization:** Ligand binding → receptor dimerization → trans-autophosphorylation of activation loop tyrosines (Y849/Y857 for PDGFR-beta) → kinase activation → recruitment of SH2-domain adaptors (GRB2, SOS → RAS; PI3K-p85 → PI3K-p110 → AKT; PLCgamma → PKC; SHP-2 → ERK amplification)

## Structure

### PDGFR signaling cascade [^heldin-1998-pdgf-review]

**Primary PDGFR downstream pathways:**

**RAS-RAF-MEK-ERK (proliferation, survival):**
- PDGFR → GRB2-SOS → RAS-GTP → RAF → MEK1/2 → ERK1/2 → RSK → gene transcription; promotes cyclin D1, MYC, FOS expression → cell cycle entry; PI3K also amplifies RAS via AKT → RAF → ERK

**PI3K-AKT-mTOR (survival, growth, migration):**
- PDGFR → p85-PI3K → PI3K-110 → PIP3 → AKT Thr308/Ser473 → mTORC1 → S6K/4EBP1 → protein synthesis and growth; also AKT → FOXO → p21/BIM suppression → survival

**PLCgamma-PKC-Ca²⁺ (proliferation, migration):**
- PDGFR → PLCgamma → IP3 + DAG → IP3 → ER Ca²⁺ release; DAG → PKC → NF-kB, AP-1 → gene transcription; Ca²⁺ → calmodulin → MLCK → actin-myosin → cell migration

**SRC-STATs (transcription):**
- PDGFR → Src family kinases → STAT3/STAT5 phosphorylation → gene transcription; STAT3 → VEGF, MYC, survivin → cancer cell survival; PDGFR-Src axis is a mechanism of PDGFR inhibitor resistance (SRC compensates)

### Oncogenic PDGFR alterations in cancer [^andrae-2008-pdgf-cancer]

**GIST (gastrointestinal stromal tumors):**
- 85% of GISTs harbor activating mutations in either **KIT (75%)** or **PDGFRA (10-15%)**; PDGFRA mutations: exon 18 D842V is the most common (imatinib-resistant) and exon 12/14; avapritinib (selective KIT/PDGFRA D842V inhibitor) specifically approved for PDGFRA D842V-mutant GIST — overcomes imatinib/sunitinib resistance; exon 18 V561D, N659K, H845Y are imatinib-sensitive [^demetri-2002-imatinib-gist]

**Dermatofibrosarcoma protuberans (DFSP):**
- t(17;22)(q21;q13) → COL1A1-PDGFB fusion gene → constitutive PDGF-BB production → autocrine PDGFR-beta activation → mesenchymal cell proliferation; imatinib approved for unresectable/metastatic DFSP (50-75% ORR); the fusion makes imatinib highly active (no resistance mutations in most)

**Glioblastoma (GBM):**
- PDGFRA amplification in ~10-15% of GBM; co-occurs with IDH1 wildtype; PDGFRA-amplified GBM subtype ("PDGF subtype") → autocrine PDGF loop → receptor tyrosine kinase hyperactivation; PDGFR inhibitors disappointing in GBM (blood-brain barrier penetration, heterogeneity, bypass pathways)

**Ewing sarcoma, leukemia:**
- ETV6-PDGFRB and other PDGFRB translocations in rare leukemias and hypereosinophilic syndrome → PDGFRB constitutive activation → eosinophilia; imatinib curative in PDGFRB-rearranged eosinophilic disorders (FIP1L1-PDGFRA in CEL/HES)

**Systemic mastocytosis:**
- FIP1L1-PDGFRA (del(4)(q12q12)) fusion → constitutive PDGFRA kinase → eosinophilia, mast cell proliferation; imatinib curative in D816V-negative FIP1L1-PDGFRA; D816V mutation (most SM) → imatinib-resistant → midostaurin (KIT D816V inhibitor) approved

**Cancer stroma and tumor microenvironment:**
- PDGF-BB secreted by tumors and platelets → PDGFR-beta on pericytes and cancer-associated fibroblasts (CAFs) → CAF proliferation and VEGF production → tumor angiogenesis and stroma; PDGF signaling is a major driver of the desmoplastic stroma of pancreatic cancer (PC) — the dense stroma that limits drug delivery and immune access; anti-PDGFR strategies (pazopanib, olaratumab) to deplete cancer stroma are in clinical trials

## Function

### PDGF in physiology [^andrae-2008-pdgf-cancer]

**Embryonic development:**
- **Vascular development:** PDGF-BB-PDGFR-beta essential for pericyte recruitment to newly formed vessels; PDGFB or PDGFRB knockout mice → microvascular aneurysms, leaky vessels, edema (pericyte loss); PDGFR-B on pericytes is the fundamental reason sunitinib (VEGFR + PDGFR TKI) is effective in RCC (anti-angiogenic via dual mechanism)
- **Kidney development:** PDGF-BB → mesangial cell recruitment to glomeruli; PDGFB or PDGFRB KO → glomerulosclerosis
- **CNS development:** PDGF-AA → oligodendrocyte precursor cell (OPC) migration and proliferation; PDGFR-alpha on OPCs; PDGFR-alpha KO → reduced myelination; PDGF-CC → neural stem cell maintenance

**Wound healing:**
- Platelets degranulate at wound → PDGF-AB/BB release → recruits fibroblasts and smooth muscle cells → granulation tissue formation → wound closure; PDGF-BB (becaplermin/Regranex) is FDA-approved topical growth factor for diabetic foot ulcers — accelerates wound healing by stimulating granulation tissue

**Fibrosis:**
- PDGF-BB and PDGF-CC → hepatic stellate cell activation (in conjunction with TGF-beta) → liver fibrosis and cirrhosis; pulmonary fibrosis: PDGF-AA → myofibroblast proliferation; **renal fibrosis:** PDGF-B → mesangial cell proliferation → glomerulosclerosis; PDGFR inhibitors reduce fibrosis in experimental models (mouse CCl4-induced liver fibrosis: imatinib → reduced stellate cell proliferation)

**Pulmonary arterial hypertension (PAH):**
- PDGF-BB → pulmonary artery smooth muscle cell (PASMC) proliferation → intimal and medial hypertrophy → lumen narrowing → elevated pulmonary vascular resistance; imatinib improved 6-minute walk distance in refractory PAH (IMPRES trial) but CNS side effects limit use; PDGFR pathway is a secondary therapeutic target in PAH alongside prostacyclin/PDE5 inhibitors/endothelin antagonists

## Mechanism

### Therapeutic targeting of PDGFR

**Imatinib (Gleevec, Glivec — BCR-ABL1 + KIT + PDGFR inhibitor):**
- First-generation PDGFR TKI; targets ABL1, KIT, PDGFR-alpha, PDGFR-beta, CSF1R; approved for CML, Ph+ ALL, GIST (KIT or PDGFRA-mutant), DFSP (COL1A1-PDGFB), and PDGFRB-rearranged myeloid neoplasms with eosinophilia; mechanism: ATP-competitive KIT/PDGFR inhibitor → blocks receptor autophosphorylation → downstream signaling abrogation → apoptosis [^demetri-2002-imatinib-gist]

**Sunitinib (Sutent — multi-kinase inhibitor including PDGFR, VEGFR, KIT, RET, FLT3):**
- Second-line GIST (after imatinib resistance); first-line RCC, PNET (pancreatic neuroendocrine tumors); broad antiangiogenic activity via combined VEGFR + PDGFR inhibition → anti-tumor vasculature pruning

**Avapritinib (Ayvakit — PDGFRA D842V-selective):**
- Highly selective PDGFRA inhibitor active against D842V mutation (imatinib-resistant) and exon 18 non-D842V mutations; NAVIGATOR trial: 89% ORR in PDGFRA D842V-mutant GIST; dramatically changed treatment of this previously refractory patient population; FDA approved 2020

**Olaratumab (Lartruvo — anti-PDGFR-alpha monoclonal antibody):**
- Phase 2 showed OS benefit in soft tissue sarcoma + doxorubicin; Phase 3 (ANNOUNCE) did not confirm; FDA approval withdrawn 2019; illustrates challenge of tumor stroma targeting in clinical trials

**Nintedanib (Ofev/Vargatef — FGFR, VEGFR, PDGFR inhibitor):**
- Approved for IPF (idiopathic pulmonary fibrosis) and NSCLC (Vargatef, second-line adenocarcinoma in EU); anti-fibrotic mechanism via PDGFR and FGFR inhibition → reduced fibroblast/myofibroblast proliferation → slows IPF progression

## Connections

- `connects-to` → **[TGF-beta](../tgf-beta/README.md)** — PDGF-BB and TGF-beta cooperate to activate hepatic stellate cells and cancer-associated fibroblasts → fibrosis; PDGF drives CAF proliferation; TGF-beta drives collagen synthesis; dual PDGFR/TGF-beta inhibition reduces tumor stroma in experimental pancreatic and hepatic fibrosis.
- `connects-to` → **[mTOR](../mtor/README.md)** — PDGFR-alpha/beta signal via PI3K-AKT → mTORC1 activation → fibroblast and smooth muscle cell proliferation; mTOR inhibitors reduce PDGF-driven SMC proliferation in pulmonary arterial hypertension; PDGFR + mTOR inhibition has preclinical synergy in GIST and sarcomas.
- `connects-to` → **[EGFR](../egfr/README.md)** — PDGFR and EGFR activate overlapping RAS-ERK and PI3K-AKT downstream pathways; PDGF transactivates EGFR via Src → amplified signaling; multi-kinase inhibitors (sunitinib, sorafenib) targeting both PDGFR and RAS-pathway RTKs exploit these downstream convergences.
- `connects-to` → **[VEGF](../vegf/README.md)** — PDGFR-B on pericytes is required for vessel maturation after VEGF-driven sprouting; PDGF-BB → pericyte recruitment → stable vessels; anti-VEGF therapy → PDGF-B dependency → resistance; sunitinib and sorafenib co-target VEGFR + PDGFR for broader antiangiogenic activity.

[^heldin-1998-pdgf-review]: Heldin CH, Östman A, Rönnstrand L. Signal transduction via platelet-derived growth factor receptors. *Biochim Biophys Acta.* 1998;1378(1):F79-F113. [doi:10.1016/S0304-419X(98)00015-8](https://doi.org/10.1016/S0304-419X(98)00015-8) · [PubMed 9739761](https://pubmed.ncbi.nlm.nih.gov/9739761/)
[^demetri-2002-imatinib-gist]: Demetri GD, von Mehren M, Blanke CD, et al. Efficacy and safety of imatinib mesylate in advanced gastrointestinal stromal tumors. *N Engl J Med.* 2002;347(7):472-480. [doi:10.1056/NEJMoa020461](https://doi.org/10.1056/NEJMoa020461) · [PubMed 12181401](https://pubmed.ncbi.nlm.nih.gov/12181401/)
[^andrae-2008-pdgf-cancer]: Andrae J, Gallini R, Betsholtz C. Role of platelet-derived growth factors in physiology and medicine. *Genes Dev.* 2008;22(10):1276-1312. [doi:10.1101/gad.1653708](https://doi.org/10.1101/gad.1653708) · [PubMed 18483217](https://pubmed.ncbi.nlm.nih.gov/18483217/)
