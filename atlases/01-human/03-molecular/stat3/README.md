---
schema: human-scale-entry/v1
id: stat3
name: STAT3
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Transcription factor activated by JAK-STAT pathway downstream of IL-6, IL-10, IFN-γ, and EGF. JAK1/2 phosphorylates STAT3 Tyr705 → dimerisation → nuclear translocation → target genes (MCL-1, BCL-XL, cyclin D1, VEGF, MMP-9). Constitutively active in many cancers."
aliases: ["Signal transducer and activator of transcription 3", "Acute-phase response factor", "APRF"]
taxonomy:
  gene_symbol: "STAT3"
  uniprot: "P40763"
sources:
  - id: darnell-1994-stat
    type: peer-reviewed
    cite: "Darnell JE Jr, Kerr IM, Stark GR. Jak-STAT pathways and transcriptional activation in response to IFNs and other extracellular signaling proteins. Science. 1994;264(5164):1415-21."
    doi: "10.1126/science.8197455"
  - id: yu-2009-stat3-cancer
    type: peer-reviewed
    cite: "Yu H, Pardoll D, Jove R. STATs in cancer inflammation and immunity: a leading role for STAT3. Nat Rev Cancer. 2009;9(11):798-809."
    doi: "10.1038/nrc2734"
  - id: bromberg-1999-stat3-oncogene
    type: peer-reviewed
    cite: "Bromberg JF, Wrzeszczynska MH, Devgan G, et al. Stat3 as an oncogene. Cell. 1999;98(3):295-303."
    doi: "10.1016/S0092-8674(00)81959-5"
  - id: johnson-2018-stat3-review
    type: peer-reviewed
    cite: "Johnson DE, O'Keefe RA, Grandis JR. Targeting the IL-6/JAK/STAT3 signalling axis in cancer. Nat Rev Clin Oncol. 2018;15(4):234-248."
    doi: "10.1038/nrclinonc.2018.8"
cross_links:
  - target: 01-human/03-molecular/il-6
    relation: modulated-by
    evidence: johnson-2018-stat3-review
    note: "IL-6 trans-signals via sIL-6R→gp130→JAK1/JAK2→STAT3 Tyr705 phosphorylation; this is the dominant STAT3 activation pathway in inflammation and cancer."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    evidence: yu-2009-stat3-cancer
    note: "STAT3 activation downstream of IL-10 drives anti-inflammatory M2-like macrophage polarisation; constitutive STAT3 in tumour-associated macrophages suppresses antitumour immunity."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    evidence: johnson-2018-stat3-review
    note: "STAT3 mediates the hepatic acute-phase response downstream of IL-6; drives fibrinogen, CRP, and SAA expression; contributes to NASH progression when constitutively active."
  - target: 01-human/07-system/immune-system
    relation: modulates
    evidence: yu-2009-stat3-cancer
    note: "STAT3 is the primary transcription factor mediating IL-6 and IL-10 downstream immunomodulation in both innate and adaptive immunity."
---

# STAT3

## Overview

STAT3 (Signal Transducer and Activator of Transcription 3) is a **latent cytoplasmic transcription factor** that serves as the central intracellular effector of the JAK-STAT signaling pathway. It was first cloned in 1994 by Darnell, Kerr, and Stark as part of the canonical IFN/STAT signal transduction system [^darnell-1994-stat], and has since emerged as one of the most intensively studied signaling proteins in cancer biology. STAT3 transduces signals from a remarkably broad array of cytokines — IL-6, IL-10, IL-11, IL-21, IL-22, IFN-γ, leptin, and EGF among them — integrating extracellular context into transcriptional programs governing cell survival, proliferation, angiogenesis, immune evasion, and inflammation.

Under normal physiology, STAT3 activation is **transient**: cytokine stimulation triggers a rapid burst of phosphorylation, gene transcription, and then signal termination via negative regulators including SOCS3 and protein tyrosine phosphatases. In cancer, however, STAT3 is **constitutively activated** — continuously phosphorylated in the absence of upstream ligand — in more than 70% of human solid tumors and many hematological malignancies [^bromberg-1999-stat3-oncogene]. This constitutive activity drives persistent transcription of genes encoding anti-apoptotic proteins (MCL-1, BCL-XL), cell cycle regulators (cyclin D1), and angiogenic factors (VEGF), creating a self-reinforcing oncogenic state.

Beyond cancer, STAT3 plays indispensable physiological roles in immune regulation: it is the dominant downstream transcription factor mediating IL-6's acute-phase response in the liver, IL-10's anti-inflammatory programming in macrophages, and Th17 differentiation in the adaptive immune system.

## Structure

### Protein domains

STAT3 is a **92 kDa** modular protein (770 amino acids) composed of six functional domains:

| Domain | Residues (approx.) | Function |
|:---|:---|:---|
| **N-terminal domain (NTD)** | 1–130 | Cooperative DNA binding; STAT3 tetramerisation on tandem sites |
| **Coiled-coil domain (CCD)** | 130–320 | Protein–protein interactions; nuclear import regulation |
| **DNA-binding domain (DBD)** | 320–480 | Sequence-specific binding to STAT-response elements (TTCNnNGAA) |
| **Linker domain** | 480–576 | Connects DBD to SH2; contributes to phospho-tyrosine recognition |
| **SH2 domain** | 576–683 | Receptor docking via phospho-tyrosine; phospho-STAT3 dimerisation interface |
| **Transactivation domain (TAD)** | 683–770 | Transcriptional activation; contains **Tyr705** (phosphorylation site) and **Ser727** |

### Key phosphorylation sites

- **Tyr705** (Y705): Phosphorylated by JAK1/JAK2/TYK2; essential for SH2-mediated dimerisation, nuclear translocation, and DNA binding. The primary pharmacological target for STAT3 inhibitors.
- **Ser727** (S727): Phosphorylated by MAPK, CDK5, mTOR; modulates transcriptional activity without affecting dimerisation; can be stimulatory or inhibitory depending on context.

### STAT3 isoforms

The *STAT3* gene produces two isoforms via alternative splicing:
- **STAT3α** (full-length, 92 kDa) — the dominant transcriptionally active form in most tissues
- **STAT3β** (truncated TAD, 83 kDa) — lacks 55 residues of the TAD; can act as a dominant-negative or in specific pro-apoptotic contexts; expressed in leukocytes

### Dimerisation

Upon Y705 phosphorylation by JAK kinases, STAT3 monomers form **parallel homodimers** via reciprocal SH2–phosphotyrosine interactions (each SH2 domain of one monomer binds the pTyr705 of the other). The dimer translocates to the nucleus and binds **GAS (γ-interferon-activated sequence)** elements with consensus TTCNnNGAA. STAT3 can also form STAT3:STAT1 heterodimers, shifting transcriptional specificity.

## Function

### Acute-phase response and liver biology

In hepatocytes — which express high levels of the IL-6 receptor — STAT3 is the dominant mediator of the **hepatic acute-phase response**. IL-6 signaling via gp130 → JAK1 → STAT3 drives rapid transcriptional induction of:

- **C-reactive protein (CRP)** — prototypic positive acute-phase reactant; rises from <1 to >100 mg/L within 24 h
- **Fibrinogen** (FGA, FGB, FGG) — elevated in acute inflammation; contributes to thrombotic risk
- **Serum amyloid A (SAA)** — rises up to 1000-fold; apo-lipoprotein with antimicrobial properties
- **Ferritin** — iron sequestration; extreme elevation is a biomarker of cytokine storm

STAT3 simultaneously suppresses **albumin** transcription, explaining hypoalbuminemia in chronic inflammatory states. In the context of metabolic liver disease, chronic low-level STAT3 activation from visceral adipose IL-6 contributes to non-alcoholic steatohepatitis (NASH) progression.

### Immune regulation

STAT3 is the **dominant downstream transcription factor** shared by the entire IL-6 cytokine family (IL-6, IL-11, IL-27, LIF, OSM, CNTF) and is also activated by IL-10, IL-21, and IL-22 in different immune cell contexts:

- **Macrophage polarisation**: IL-10 → STAT3 → anti-inflammatory (M2-like) gene program (IL-10 itself, arginase-1, CD206, IL-1RA); drives resolution of inflammation. In tumor-associated macrophages (TAMs), constitutive STAT3 promotes immunosuppression by inducing IL-10, TGF-β, and PD-L1.
- **Th17 differentiation**: IL-6 + TGF-β → phospho-STAT3 → RORγt expression → Th17 commitment. STAT3-deficient CD4⁺ T cells cannot form Th17 cells; this underlies the susceptibility to mucosal infections in humans with dominant-negative STAT3 mutations (hyper-IgE syndrome).
- **Treg vs. Th17 balance**: IL-6-driven STAT3 activation opposes TGF-β-driven Foxp3/Treg development, tipping the balance toward Th17 in inflammatory microenvironments.
- **B cell differentiation**: STAT3 (downstream of IL-21) drives plasmablast differentiation and antibody class switching.

### Cancer biology

STAT3 is considered a non-classical oncogene — it is not mutated in most cancers but is constitutively activated by upstream mutations in JAK2 (*JAK2* V617F in myeloproliferative neoplasms), *IL6* autocrine loops, receptor tyrosine kinase fusions (*BCR-ABL*, *ALK*), or loss of negative regulators (SOCS3, PTPRD) [^yu-2009-stat3-cancer]:

- **Anti-apoptotic**: induces MCL-1, BCL-XL, BCL-2, and survivin → resistance to chemotherapy-induced apoptosis
- **Proliferative**: induces cyclin D1, c-Myc → G1/S cell cycle progression
- **Angiogenic**: transcribes VEGF, FGF → tumor vascularisation
- **Immune evasion**: upregulates PD-L1, IL-10, VEGF in tumor microenvironment → suppresses cytotoxic T cell function
- **Invasion/metastasis**: induces MMP-2, MMP-9, TWIST → epithelial-mesenchymal transition

## Mechanism

### Canonical JAK-STAT3 cascade

The canonical STAT3 activation sequence:

1. Cytokine (IL-6, IL-10, etc.) binds its receptor complex (e.g., IL-6 + IL-6Rα + gp130)
2. Receptor oligomerization → juxtaposition of intracellular JAK kinases (**JAK1** constitutively associated with gp130 Box1/Box2)
3. JAK1 trans-phosphorylates itself and JAK2/TYK2 → activated JAK1 phosphorylates gp130 cytoplasmic tail tyrosines (Y767, Y814, Y905, Y915)
4. **STAT3 SH2 domain** docks onto gp130 pTyr → STAT3 Tyr705 is phosphorylated by JAK1
5. pTyr705-STAT3 dissociates from receptor → forms **parallel homodimer** via reciprocal SH2–pTyr705 interactions
6. Importin-α3/α6-mediated **nuclear import** of STAT3 dimer
7. DNA binding to GAS elements (TTCNnNGAA) in target gene promoters and enhancers → transcriptional activation via TAD recruitment of coactivators (CBP/p300, BRD4)
8. Nuclear export → dephosphorylation by TC45 phosphatase → return to cytoplasmic pool

### Negative regulation

- **SOCS3** (Suppressor of Cytokine Signaling 3): a STAT3 target gene that feeds back to inhibit JAK1 by competing for the gp130 docking site and presenting JAK to the elongin BC/CUL5 E3 ubiquitin ligase for degradation — the primary acute negative-feedback brake
- **PTPRD** and **PTPRT** (receptor protein tyrosine phosphatases): constitutively dephosphorylate nuclear STAT3; frequently deleted in colorectal and head/neck cancers, explaining STAT3 hyperactivation
- **PIAS3** (Protein Inhibitor of Activated STAT3): binds STAT3 dimer in the nucleus and blocks DNA binding
- **TC45 / TCPTP**: nuclear phosphatase that dephosphorylates pTyr705-STAT3

### Non-canonical STAT3 signaling

Beyond the classical pY705-driven pathway, STAT3 also signals through:
- **Mitochondrial STAT3** (mSTAT3): pS727-STAT3 localizes to the mitochondrial inner membrane and regulates electron transport chain complex I and II activity, Warburg metabolism, and ROS production — independent of transcription
- **Acetylated STAT3**: STAT3 acetylated at K685 by CBP/p300 dimerizes and is required for DNMT3a-mediated epigenetic silencing of tumor suppressor genes

### Therapeutic targeting

STAT3 has long been considered an "undruggable" transcription factor, but several inhibitor classes have emerged [^johnson-2018-stat3-review]:

| Class | Mechanism | Examples | Status |
|:---|:---|:---|:---|
| **JAK inhibitors** | Block JAK1/2 upstream of STAT3 | Ruxolitinib, tofacitinib, baricitinib | FDA-approved (RA, MF, GVHD) |
| **SH2 domain inhibitors** | Compete with pTyr705 docking | Stattic, SH-4-54, TTI-101 | Clinical trials |
| **Oligonucleotide/siRNA** | Downregulate STAT3 mRNA | AZD9150 (antisense) | Phase I/II |
| **PROTAC degraders** | Ubiquitin-mediated STAT3 degradation | SD-36, KT-333 | Clinical trials |

## Connections

- `modulated-by` → **[il-6](../il-6/README.md)** — IL-6/gp130/JAK1/2 is the dominant STAT3 activation pathway
- `modulates` → **[macrophage](../../04-cellular/macrophage/README.md)** — IL-10/STAT3 drives M2 polarisation; constitutive STAT3 in TAMs suppresses antitumour immunity
- `modulates` → **[hepatocyte](../../04-cellular/hepatocyte/README.md)** — acute-phase response, fibrinogen/CRP/SAA induction, NASH progression
- `modulates` → **[immune-system](../../07-system/immune-system/README.md)** — central mediator of IL-6 and IL-10 immunomodulation; Th17/Treg balance

## Pathology

| Disease | STAT3 role | Therapeutic implication |
|:---|:---|:---|
| **Rheumatoid arthritis** | IL-6/JAK1/STAT3 drives synovitis, Th17 responses, acute-phase proteins | JAK inhibitors (tofacitinib, baricitinib, upadacitinib); IL-6R blockade (tocilizumab) |
| **Multiple myeloma** | IL-6 autocrine → constitutive STAT3 → MCL-1/BCL-XL survival; VEGF angiogenesis | JAK inhibitors; proteasome inhibitors impair STAT3 indirectly |
| **Hepatocellular carcinoma** | Constitutive STAT3 via IL-6 or HBV/HCV activation; drives MMP-9, VEGF, cyclin D1 | Sorafenib; investigational STAT3 inhibitors |
| **Diffuse large B-cell lymphoma** | Activating STAT3 mutations; constitutive nuclear STAT3 in ABC-DLBCL subtype | JAK inhibitors; BTK inhibitors; anti-IL-6R |
| **JAK2 V617F myeloproliferative neoplasms** | Constitutive JAK2 → STAT3/STAT5 → erythroid/megakaryocyte hyperproliferation | Ruxolitinib (JAK1/2 inhibitor) |
| **Hyper-IgE syndrome** | Dominant-negative STAT3 mutations → impaired Th17, recurrent skin/lung infections, eczema | Supportive; IVIg; dupilumab for eczema component |
| **Inflammatory bowel disease** | Mucosal IL-6/IL-10/STAT3 dysregulation; STAT3 in IECs promotes barrier repair | Anti-IL-6R; JAK inhibitors (upadacitinib in UC) |
| **COVID-19 cytokine storm** | IL-6 → STAT3 → MCL-1, VEGF → endothelial injury, cytokine amplification | Tocilizumab + dexamethasone; baricitinib |
| **Colorectal cancer** | PTPRT/PTPRD deletion → constitutive STAT3; drives invasion via MMP-9, TWIST | Investigational STAT3 degraders (SD-36) |
| **Head and neck squamous cell carcinoma** | IL-6 autocrine loop + EGFR → STAT3; correlates with poor prognosis | Cetuximab (EGFR); TTI-101 (STAT3 SH2 inhibitor, clinical trials) |

[^darnell-1994-stat]: Darnell JE Jr, Kerr IM, Stark GR. Jak-STAT pathways and transcriptional activation in response to IFNs and other extracellular signaling proteins. *Science.* 1994;264(5164):1415-21. [doi:10.1126/science.8197455](https://doi.org/10.1126/science.8197455)
[^yu-2009-stat3-cancer]: Yu H, Pardoll D, Jove R. STATs in cancer inflammation and immunity: a leading role for STAT3. *Nat Rev Cancer.* 2009;9(11):798-809. [doi:10.1038/nrc2734](https://doi.org/10.1038/nrc2734)
[^bromberg-1999-stat3-oncogene]: Bromberg JF, Wrzeszczynska MH, Devgan G, et al. Stat3 as an oncogene. *Cell.* 1999;98(3):295-303. [doi:10.1016/S0092-8674(00)81959-5](https://doi.org/10.1016/S0092-8674(00)81959-5)
[^johnson-2018-stat3-review]: Johnson DE, O'Keefe RA, Grandis JR. Targeting the IL-6/JAK/STAT3 signalling axis in cancer. *Nat Rev Clin Oncol.* 2018;15(4):234-248. [doi:10.1038/nrclinonc.2018.8](https://doi.org/10.1038/nrclinonc.2018.8)
