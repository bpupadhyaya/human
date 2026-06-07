---
schema: human-scale-entry/v1
id: nfe2l2
name: NRF2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "NRF2 (NFE2L2) is the master antioxidant transcription factor sequestered by KEAP1; NFE2L2 gain-of-function mutations in ~15% of ESCC and ~15% of LUSC impair KEAP1 binding → constitutive NRF2 → chemotherapy/radiation resistance; no approved NRF2 inhibitor exists."
aliases: ["NRF2", "NFE2L2", "nuclear factor erythroid 2-related factor 2", "KEAP1-NRF2", "antioxidant response element", "ARE", "NRF2 cancer", "KEAP1 mutation NSCLC", "NRF2 esophageal"]
sources:
  - id: shibata-2008-nrf2-cancer
    type: peer-reviewed
    cite: "Shibata T, Kokubu A, Gotoh M, et al. Genetic alteration of Keap1 confers constitutive Nrf2 activation and resistance to chemotherapy in gallbladder cancer. Gastroenterology. 2008;135(4):1358-1368."
    doi: "10.1053/j.gastro.2008.06.082"
    pmid: "18692501"
    url: "https://doi.org/10.1053/j.gastro.2008.06.082"
  - id: taguchi-2017-keap1-nrf2
    type: peer-reviewed
    cite: "Taguchi K, Yamamoto M. The KEAP1-NRF2 system in cancer. Front Oncol. 2017;7:85."
    doi: "10.3389/fonc.2017.00085"
    pmid: "28529921"
    url: "https://doi.org/10.3389/fonc.2017.00085"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "NRF2 and KRAS are co-activated in KRAS-mutant LUSC and ESCC; KRAS activates NRF2 via NRF2-ARE; NRF2 neutralizes KRAS-driven ROS → cell survival; NRF2 inhibition sensitizes KRAS-mutant cancer cells to oxidative stress; NFE2L2/KRAS co-mutation seen in ~5% of NSCLC."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "NRF2 promotes mTORC1 activity via p62/SQSTM1 accumulation; mTOR → NRF2 transcription feedback; NRF2-mTOR axis drives metabolic reprogramming (pentose phosphate pathway, serine synthesis) in ESCC; mTOR+NRF2 dual inhibition is synergistic in ESCC cell models."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "NRF2 and HIF-1α both respond to oxidative and hypoxic stress; NRF2 antioxidant targets (HO-1, TXN) reduce ROS → lower PHD2/3 activity → HIF-1α stabilization → VEGF; HIF-1α can also repress NRF2; both drive metabolic reprogramming and angiogenesis in ESCC."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "NFE2L2 and TP53 mutations frequently co-occur in ESCC and LUSC; NRF2 activates MDM2 promoter → p53 degradation; TP53 can repress NRF2 via p21/CDKN1A; combined NFE2L2 gain-of-function + TP53 loss is a common co-mutation signature in ESCC and LUSC."
---

# NRF2

## Overview

**NRF2 (Nuclear factor erythroid 2-related factor 2, encoded by the NFE2L2 gene)** is the master transcription factor of the cellular antioxidant response, belonging to the CNC (Cap 'n' Collar) family of basic leucine zipper (bZIP) proteins. Under homeostatic conditions, NRF2 protein is constitutively ubiquitinated by the **KEAP1-CUL3-RBX1 E3 ubiquitin ligase complex** and targeted for proteasomal degradation, maintaining low cytoplasmic NRF2 levels. Upon **oxidative stress** (reactive oxygen species, electrophiles, heavy metals), critical cysteine residues in KEAP1 (C151, C273, C288) are chemically modified → KEAP1 conformational change → impaired NRF2 ubiquitination → NRF2 escapes degradation → nuclear translocation → heterodimerizes with **MAF proteins (sMAF: MAFG, MAFF, MAFK)** → binds **antioxidant response elements (AREs, 5'-TGA[C/T]NNNGC-3')** in target gene promoters → transcription of >250 cytoprotective genes (HO-1, NQO1, GCLC, GCLM, GPX2, GST family, TXNRD1, SRXN1, PRDX3, SLC7A11, G6PD, TALDO1). In cancer, **NFE2L2 gain-of-function mutations** or **KEAP1 loss-of-function mutations** cause constitutive NRF2 activation → enhanced antioxidant capacity → resistance to chemotherapy, radiation, and ROS-mediated apoptosis [^shibata-2008-nrf2-cancer] [^taguchi-2017-keap1-nrf2].

**NRF2/KEAP1 alterations in cancer:**
- **ESCC (esophageal squamous cell carcinoma):** NFE2L2 mutations in ~15% (hotspots E79K, E82K, E78K in the ETGE/DLG KEAP1-binding domains of the Neh2 domain); KEAP1 mutations in ~5%; poor prognosis; platinum resistance
- **LUSC (lung squamous cell carcinoma):** NFE2L2 mutations in ~15%; KEAP1 mutations in ~20%; among the highest NRF2 pathway alteration rates of any cancer; KEAP1 mutations (which prevent KEAP1-NRF2 interaction) are more common than NFE2L2 in LUSC
- **HNSCC (head and neck):** NFE2L2 mutations ~10%; particularly in oral cavity and oropharyngeal SCC
- **Bladder urothelial carcinoma:** NFE2L2 ~10%; KEAP1 ~5%; cisplatin resistance in bladder cancer associated with NRF2 pathway
- **Hepatocellular carcinoma:** KEAP1 mutations ~10%; NFE2L2 ~5%; NRF2 activation supports HCC metabolic reprogramming
- **Gallbladder carcinoma:** KEAP1 mutations frequently identified; first demonstration that KEAP1-NRF2 pathway is a cancer target

## Structure

### NRF2 protein architecture (7 domains: Neh1-7)

NRF2 is a 605-amino-acid, 68 kDa bZIP transcription factor:

**Neh2 domain (1-100, KEAP1-binding):**
- Contains **ETGE motif** (high-affinity KEAP1 binding, Kd ~20 nM) and **DLG motif** (low-affinity KEAP1 binding, Kd ~2 μM)
- Two-site substrate model: DLG and ETGE motifs each bind to one KEAP1 Kelch domain in the KEAP1 homodimer → both sites occupied → CUL3/RBX1 ubiquitinates Lys residues in the Neh2 domain → proteasomal degradation
- **Cancer mutations (hotspots):** E79K, E82K (in ETGE motif): Prevent ETGE-KEAP1 binding → NRF2 cannot be efficiently ubiquitinated → constitutive NRF2 accumulation; also D29H, T80K, R34Q; all cluster in DLG/ETGE motifs in Neh2
- **p62/SQSTM1 competition:** p62 (autophagy receptor, sequestosome-1) contains a KEAP1-binding motif (KELIM) homologous to NRF2 DLG → competes with NRF2 DLG for KEAP1 → accumulation of p62 (e.g., in autophagy deficiency) → partial NRF2 activation; KRAS activation → p62 accumulation → NRF2 activation

**Neh1 domain (basic leucine zipper, bZIP):**
- CNC-bZIP type; basic region binds ARE; leucine zipper mediates heterodimerization with sMAF proteins
- NRF2:sMAF heterodimer is the transcriptionally active form binding ARE sequences
- Bach1/2 (BTB-bZIP repressors) compete with NRF2 for sMAF → repress ARE-dependent transcription; HO-1 induces CO → inhibits Bach1 → Bach1 export → sustained NRF2 activity

**Neh3 (C-terminal transactivation), Neh4 (glutamine-rich TAD), Neh5 (acidic TAD):**
- Transactivation domains; recruit CBP/p300 coactivators; Neh4/5 interact with CBP → epigenetic NRF2 target gene activation; GSK-3 phosphorylates Neh6 domain → β-TrCP E3 ligase-mediated degradation (KEAP1-independent NRF2 regulation)

**Neh6 domain:**
- Contains DSGIS and DSAPGS degrons → GSK-3β phosphorylation → β-TrCP (SCF E3 ligase) recruitment → ubiquitination → proteasomal degradation; this KEAP1-independent pathway is relevant when KEAP1 is already saturated (e.g., in NRF2-mutant tumors with some residual KEAP1 activity)

### KEAP1 protein and NRF2 regulation

**KEAP1 protein (Kelch-like ECH-associated protein 1):**
KEAP1 is a 624-aa substrate adaptor protein for CUL3-RBX1 E3 ubiquitin ligase: N-terminal BTB domain (CUL3 binding + KEAP1 homodimerization); central IVR domain (27 cysteine "sensors": C151, C273, C288 are primary electrophile/ROS sensors); C-terminal Kelch repeat domain (6 Kelch repeats form a β-propeller → NRF2 ETGE/DLG binding).

**Cancer KEAP1 loss-of-function mutations:**
- C273 cluster mutations (C273Y/R): Eliminate the principal oxidant sensor → KEAP1 cannot respond to oxidative stress → cannot degrade NRF2 → constitutive NRF2
- Kelch domain missense mutations (R470, G333, G364 cluster): Impair NRF2 DLG/ETGE binding → NRF2 escapes → constitutive
- Whole-KEAP1 deletion: LOH/frameshift; especially in LUSC and esophageal cancer

### NRF2 target gene network

**Antioxidant genes:**
- HO-1 (HMOX1): Heme oxygenase-1; catabolizes heme → CO + biliverdin → anti-inflammatory, antioxidant
- NQO1: NAD(P)H quinone oxidoreductase 1; two-electron reduction of quinones → prevent ROS cycling
- GCLC + GCLM: γ-glutamylcysteine ligase (catalytic + modifier subunits) → rate-limiting step of glutathione (GSH) synthesis; NRF2 → GSH upregulation → platinum conjugation → cisplatin export

**Metabolic reprogramming genes:**
- SLC7A11 (xCT): Cystine/glutamate antiporter; imports cystine → reduces to cysteine → GSH synthesis; xCT overexpression in NRF2-active cancer → cystine addiction → ferroptosis resistance
- G6PD, TALDO1: Pentose phosphate pathway → NADPH → GSH and thioredoxin recycling
- ACSS2, IDH1: NADPH-generating metabolic enzymes upregulated by NRF2

**Drug resistance mechanism:**
NRF2-active ESCC/LUSC cells: ↑GSH → platinum (cisplatin) conjugation by glutathione S-transferases (GSTπ, GSTα) → cisplatin-GS conjugation → MRP1/MRP2 export → reduced intracellular platinum → resistance; ↑NQO1 → quinone reduction (reduces some cytotoxic agents); ↑HO-1 → anti-apoptotic; ↑TXNRD1 → thioredoxin → thioredoxin peroxidase → reduced H₂O₂ → less apoptotic signaling

## Function

### Normal NRF2 roles

**Antioxidant defense:**
NRF2 is activated transiently during physiological oxidative stress (exercise, inflammation) → cytoprotective gene expression → restoration of redox homeostasis; NRF2-knockout mice: Normal appearance but hypersensitive to toxins (acetaminophen hepatotoxicity, bleomycin lung fibrosis, LPS-induced sepsis); NRF2 is especially important in lung (respiratory epithelium exposed to oxygen), liver (biotransformation), and intestine (constant microbial ROS exposure).

**Inflammation modulation:**
NRF2 → HO-1 → CO → inhibits NLRP3 inflammasome and NF-κB → reduced IL-1β, IL-6, TNF-α; NRF2-mediated anti-inflammation is cytoprotective in autoimmune disease (MS, IBD) — bardoxolone methyl (NRF2 activator) is approved for CKD in Japan, studied in others; paradoxically, in cancer, NRF2 anti-inflammation may blunt anti-tumor immunity.

**Drug response phenotype in cancer:**
NFE2L2/KEAP1-mutant tumors: Benefit less from platinum-based chemotherapy; potentially benefit more from immune checkpoint inhibitors (immunostimulatory microenvironment shift from antioxidant environment — paradoxical in some studies); EGFR-mutant NSCLC with concurrent KEAP1 mutation: Worse response to osimertinib + reduced survival vs. KEAP1-WT EGFR-mutant.

### NRF2 and radiation resistance

Radiation → ROS burst → DNA damage; NRF2-active tumors → antioxidant scavenging of radiation-induced ROS → reduced DNA damage → radioresistance; combination of NRF2 inhibition + radiation is synergistic in ESCC preclinical models; ML385 (NRF2 inhibitor, non-clinical) and brusatol (NRF2 protein downregulator) sensitize ESCC to radiation; no NRF2 inhibitor is clinically approved.

## Mechanism

### Therapeutic implications of NRF2 pathway

**No approved NRF2 inhibitor in cancer:**
Despite NRF2's role in drug resistance, no NRF2 inhibitor has received FDA approval for cancer. Challenges include: NRF2 is cytoprotective in normal tissues → systemic NRF2 inhibition causes toxicity; difficulty achieving tumor-selective drug delivery. Research approaches:
- **Brusatol:** Promotes NRF2 ubiquitination → degradation; sensitizes cancer cells to platinum; off-target toxicity in normal tissues limits clinical development
- **ML385:** Binds NRF2 Neh1 bZIP domain → inhibits NRF2-sMAF interaction → reduces ARE transcription; potent but non-clinical tool compound only
- **AI-driven NRF2 allosteric inhibitors:** Early-stage drug discovery targeting Neh4/5 coactivator interactions

**NRF2 activators as cancer chemopreventives:**
Paradoxically, NRF2 ACTIVATORS (sulforaphane from broccoli, bardoxolone methyl, oltipraz) have been studied for cancer chemoprevention in chronic inflammation (colitis → colon cancer, Barrett's → EAC), as transient NRF2 activation reduces oxidative DNA damage; however, in established cancer with NFE2L2/KEAP1 mutations, activation of an already-constitutive pathway is not therapeutically relevant.

**KEAP1/NRF2 as biomarker for chemotherapy selection:**
NFE2L2 hotspot mutations (E79K, E82K) or KEAP1 loss → poor response to platinum/etoposide in ESCC and LUSC → these patients may benefit more from upfront immunotherapy (e.g., pembrolizumab monotherapy in PD-L1-high), targeted therapies, or alternative chemotherapy regimens; molecular testing increasingly informs treatment selection in ESCC.

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — NRF2 and KRAS are co-activated in KRAS-mutant LUSC and ESCC; KRAS activates NRF2 via NRF2-ARE; NRF2 neutralizes KRAS-driven ROS → cell survival; NRF2 inhibition sensitizes KRAS-mutant cancer cells to oxidative stress; NFE2L2/KRAS co-mutation seen in ~5% of NSCLC.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — NRF2 promotes mTORC1 activity via p62/SQSTM1 accumulation; mTOR → NRF2 transcription feedback; NRF2-mTOR axis drives metabolic reprogramming (pentose phosphate pathway, serine synthesis) in ESCC; mTOR+NRF2 dual inhibition is synergistic in ESCC cell models.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — NRF2 and HIF-1α both respond to oxidative and hypoxic stress; NRF2 antioxidant targets (HO-1, TXN) reduce ROS → lower PHD2/3 activity → HIF-1α stabilization → VEGF; HIF-1α can also repress NRF2; both drive metabolic reprogramming and angiogenesis in ESCC.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — NFE2L2 and TP53 mutations frequently co-occur in ESCC and LUSC; NRF2 activates MDM2 promoter → p53 degradation; TP53 can repress NRF2 via p21/CDKN1A; combined NFE2L2 gain-of-function + TP53 loss is a common co-mutation signature in ESCC and LUSC.

[^shibata-2008-nrf2-cancer]: Shibata T, Kokubu A, Gotoh M, et al. Genetic alteration of Keap1 confers constitutive Nrf2 activation and resistance to chemotherapy in gallbladder cancer. *Gastroenterology.* 2008;135(4):1358-1368. [doi:10.1053/j.gastro.2008.06.082](https://doi.org/10.1053/j.gastro.2008.06.082) · [PubMed 18692501](https://pubmed.ncbi.nlm.nih.gov/18692501/)
[^taguchi-2017-keap1-nrf2]: Taguchi K, Yamamoto M. The KEAP1-NRF2 system in cancer. *Front Oncol.* 2017;7:85. [doi:10.3389/fonc.2017.00085](https://doi.org/10.3389/fonc.2017.00085) · [PubMed 28529921](https://pubmed.ncbi.nlm.nih.gov/28529921/)
