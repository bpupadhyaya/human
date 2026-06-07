---
schema: human-scale-entry/v1
id: rb1
name: RB1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Cell cycle gatekeeper; CDK4/6-cyclin D phosphorylates RB → E2F release → S phase entry. Biallelic RB1 loss causes retinoblastoma and SCLC; also lost in NEPC, osteosarcoma, and bladder cancer; CDK4/6 inhibitors (palbociclib) restore RB pathway function in RB-intact tumors."
aliases: ["RB", "retinoblastoma protein", "pRb", "p110-RB", "retinoblastoma tumor suppressor", "RB pocket protein", "E2F repressor"]
sources:
  - id: dyson-2016-rb-review
    type: peer-reviewed
    cite: "Dyson NJ. RB1: a prototype tumor suppressor and an enigma. Genes Dev. 2016;30(13):1492-1502."
    doi: "10.1101/gad.282145.116"
    pmid: "27401552"
    url: "https://doi.org/10.1101/gad.282145.116"
  - id: beroukhim-2010-deletion
    type: peer-reviewed
    cite: "Beroukhim R, Mermel CH, Porter D, et al. The landscape of somatic copy-number alteration across human cancers. Nature. 2010;463(7283):899-905."
    doi: "10.1038/nature08822"
    pmid: "20164920"
    url: "https://doi.org/10.1038/nature08822"
cross_links:
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin D1 phosphorylates RB at S780/S795/T821 → E2F-DP release → S phase entry; CDK4/6 inhibitors (palbociclib, abemaciclib) block RB phosphorylation → G1 arrest; RB1 mutation or deletion renders CDK4/6 inhibition ineffective — a key resistance biomarker in breast cancer."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "CDKN2A encodes p16/INK4a (CDK4/6 inhibitor → RB) and p14/ARF (MDM2 inhibitor → p53); CDKN2A deletion loses both tumor suppressors simultaneously; RB and p53 are the two canonical checkpoint gatekeepers; co-loss in SCLC, NEPC, and glioblastoma drives aggressive progression."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "E2F1/2/3 released from RB → transcribe MYC, CDC25A, and cyclin E → RB hyperphosphorylation (positive feedback); MYC upregulates CDK4/cyclin D → RB phosphorylation; RB loss → unconstrained E2F-MYC transcription axis; RB-null SCLC is MYC-amplified in ~15% of cases."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "RB represses HIF-1alpha target genes at chromatin via E2F repressor complexes; RB loss in SCLC → derepression of HIF-1alpha → VEGF and glycolysis genes constitutively expressed; RB-HIF-1alpha axis links cell cycle control to metabolic adaptation in aggressive cancers."
---

# RB1

## Overview

**RB1 (retinoblastoma protein, pRb)** is the founding member of the **pocket protein family** and the prototypical tumor suppressor. The *RB1* gene (chromosome 13q14) was the first tumor suppressor identified (Knudson's "two-hit hypothesis," 1971): hereditary retinoblastoma requires only one additional somatic mutation to lose the second allele; sporadic retinoblastoma requires two somatic events — establishing the paradigm of tumor suppressor biology. RB protein functions as the **master regulator of the G1/S cell cycle transition** by restraining E2F transcription factors; its inactivation by CDK4/6-cyclin D phosphorylation is a universal requirement for S phase entry in all proliferating cells [^dyson-2016-rb-review].

**RB1 in cancer:**
- **Retinoblastoma:** 100% of tumors harbor biallelic RB1 loss; hereditary (40%) and sporadic (60%); germline *RB1* mutation → 85% penetrance for retinoblastoma by age 5 + elevated lifetime risk of osteosarcoma, SCLC, and other cancers
- **Small cell lung cancer (SCLC):** RB1 loss in ~90% of SCLC (most commonly combined with TP53 mutation — "double-whammy" of checkpoint loss); RB loss is effectively a prerequisite for SCLC histology
- **Neuroendocrine prostate cancer (NEPC):** RB1 + TP53 co-loss drives lineage plasticity from adenocarcinoma to AR-negative NEPC under enzalutamide treatment pressure; NEPC is the dominant form of enzalutamide-resistant CRPC
- **Osteosarcoma:** RB1 deletion in ~30-50%
- **Bladder cancer (muscle-invasive, MIBC):** RB1 deletion in ~20%
- **EGFR-mutant NSCLC:** RB1 loss in ~10% (mediates transformation to SCLC upon EGFR-TKI treatment — "histological transformation")
- **Breast cancer:** CDK4/6 inhibitor resistance via RB1 loss (acquired in ~15% of palbociclib-resistant HR+ breast cancer)

**The pocket protein family:**
- **pRb (RB1, p110-RB):** The canonical member; primary G1/S gatekeeper
- **p107 (RBL1):** Most homologous to pRb; partially redundant; important during embryogenesis
- **p130 (RBL2, RB2):** Preferentially represses E2F targets in quiescent cells; key regulator of G0 entry; often silenced in cancer by promoter methylation

## Structure

### RB1 protein architecture

RB1 is a 928-amino-acid, ~110 kDa nuclear protein with three structural regions:

**N-terminal domain (NTD, residues 1-372):**
- Relatively unstructured; contains a cyclin-binding RxL motif → cyclin D interaction; also contains domains mediating interaction with MCM loading complex (MCM7) and LXCXE-independent interaction with E2F
- **LXCXE motif binding groove on NTD-B pocket:** The primary binding site for viral oncoproteins (HPV E7, adenovirus E1A, SV40 Large T antigen) that contain the LXCXE motif; these viral proteins mimic cellular CDK phosphorylation by sterically displacing E2F from RB; LXCXE motif is also used by cellular proteins (HDAC1/2, EZH2) recruited by RB for transcriptional repression

**Pocket domain (residues 373-792) — the functional core:**
- Divided into A (373-572) and B (646-772) subdomains separated by a spacer (573-645) that is not required for E2F binding but recruits additional corepressors
- The A-B pocket fold creates a conserved surface that binds multiple cellular proteins
- **E2F binding:** The E2F transactivation domain (TAD) DIEL motif binds the B subdomain pocket; the E2F C-terminal "marked box" domain binds the NTD-A junction in a secondary interaction → RBID motif
- **Cyclin-CDK phosphorylation sites:** 16 CDK consensus phosphorylation sites (SP and TP motifs) distributed through the NTD and pocket → progressive "serial phosphorylation" model: CDK4/6-cyclin D phosphorylates early (S780, S795) → partial E2F release → CDK2-cyclin E phosphorylates late (T821, T826) → complete E2F release → irreversible G1/S commitment
- **HDAC recruitment:** RB recruits HDAC1/2/3 via the LXCXE groove → active transcriptional repression of E2F targets (not just steric blockade of E2F); CDK phosphorylation disrupts HDAC-RB → loss of active repression + loss of E2F sequestration

**C-terminal domain (CTD, residues 793-928):**
- Contains a nuclear localization signal
- Mediates interaction with coiled-coil domains in RBBP proteins (retinoblastoma binding proteins)
- Alternatively spliced (exon 22 inclusion/exclusion) in some tumor types, affecting LXCXE binding affinity

### RB phosphorylation cascade (cell cycle timing)

**G0 → G1:** Mitogens → CDK4/6-cyclin D expression → initial RB phosphorylation (S780/S795); this first wave partially releases HDAC from RB but E2F is not yet completely freed
**Mid-G1:** CDK2-cyclin E (induced by E2F after partial release) → T821/T826 phosphorylation → complete E2F release → **bistable switch** (RB hypophosphorylation → hyperphosphorylation is irreversible once committed)
**S phase → M:** CDK2-cyclin A, CDK1-cyclin B maintain RB in hyperphosphorylated state → E2F-target transcription sustained
**M → G1 (exit):** PP1 and PP2A phosphatases dephosphorylate RB at mitotic exit → RB hypophosphorylation restored → re-establishment of G0 or G1 control

## Function

### E2F transcription factor control

**E2F family:**
- E2F1/2/3a: "Activating E2Fs" — induce S phase gene expression when released from RB; CDK4/6-cyclin D → RB phosphorylation → E2F1/2/3 release → transcription of: cyclin E (CCNE1), CDC25A, DNA polymerase delta, PCNA, RNR, DHFR, thymidine kinase, and E2F1 itself (positive feedback)
- E2F3b/4/5: "Repressive E2Fs" — associate with p107/p130 in quiescent cells to maintain G0; E2F4/5 do not have nuclear localization signals — dependent on pocket protein for nuclear retention
- E2F6/7/8: "DP-independent" repressors; function in differentiation reprogramming (E2F7/8 are ATM targets that buffer E2F1-driven apoptosis after DNA damage)

**RB-E2F repressor complexes:**
- pRb-E2F1: Represses E2F1 target genes (CDC25A, cyclin E → S phase entry); also represses anti-apoptotic targets (MCL-1, BCL-XL); pRb-E2F1 is a pro-apoptotic complex that protects against oncogenesis while allowing normal cell cycle control
- pRb-HDAC-SWI/SNF: At E2F target promoters in G0; active repression → gene silencing; this complex is disrupted by CDK4/6 phosphorylation or viral LXCXE-containing oncoproteins

**RB in differentiation and senescence:**
- RB is required for terminal differentiation of many cell types: muscle (MyoD-RB interaction → withdrawal from cell cycle), erythrocytes (erythroblast enucleation → RB-dependent), neurons (RB required for post-mitotic neuronal state)
- **Oncogene-induced senescence (OIS):** KRAS/BRAF oncogene → p16/INK4a → CDK4/6 inhibition → RB hypophosphorylation → E2F repression → senescence; senescence is a tumor-suppressive state dependent on RB (RB1 loss → bypass of OIS)
- **DREAM complex:** RB family (p130) + MuvB + BMYB + FOXM1 → G2/M gene repression in G0/G1; disrupted in cancer by CDK4/6 activity

## Mechanism

### RB inactivation in cancer

**Biallelic RB1 loss (mutation/deletion):** Most common in SCLC, retinoblastoma, osteosarcoma, NEPC; defined by genetic analysis; loss of both alleles required (Knudson two-hit model)

**CDKN2A (p16/INK4a) deletion:** Most common mechanism of functional RB inactivation in cancer; homozygous deletion at chr 9p21 → loss of p16 → CDK4/6 not inhibited → constitutive RB phosphorylation → E2F1 constitutively active; ~50% of all human cancers; particularly common in melanoma, glioblastoma, HNSCC, bladder cancer, and PDAC

**Cyclin D amplification:** CCND1 amplification (chr 11q13) → cyclin D1 excess → CDK4-cyclin D1 complex → RB hyperphosphorylation; in breast cancer, HNSCC, mantle cell lymphoma (t(11;14) → cyclin D1 overexpression)

**CDK4 amplification:** Chr 12q13-14; CDK4 amplification → constitutive CDK4 activity; in liposarcoma (~20% of WD/DDLPS), glioblastoma, and some sarcomas; CDK4-amplified liposarcoma is treated with palbociclib/CDK4/6 inhibitors

**CDK6 amplification:** Less common; amplification in T-ALL, DLBCL, and some solid tumors; CDK6 is an E2F target gene — positive feedback in CDK6-amplified tumors

**Viral LXCXE oncoproteins:**
- **HPV E7 (high-risk HPV 16/18):** Binds RB via LXCXE → constitutive E2F release → S phase; simultaneously, HPV E6 targets p53 for degradation → double checkpoint loss → cervical/oropharyngeal carcinogenesis; MDM2 gene (p53 regulator) amplified in HPV-negative HNSCC as an alternative p53 bypass mechanism
- **Adenovirus E1A:** LXCXE motif → RB disruption; used as gene therapy vector for cancer
- **SV40 Large T antigen:** LXCXE → RB; also binds p53 → dual checkpoint bypass

### CDK4/6 inhibitors: RB as a pharmacodynamic biomarker

CDK4/6 inhibitor efficacy is entirely dependent on an intact RB pathway:
- **RB1 intact** → CDK4/6 inhibitor → RB hypophosphorylation → E2F repression → G1 arrest → efficacy
- **RB1 mutant/deleted** → CDK4/6 inhibitor has no substrate → no target → no efficacy
- RB protein expression by immunohistochemistry is routinely assessed in clinical trials of CDK4/6 inhibitors; RB loss is an exclusion criterion or resistance indicator
- Acquired *RB1* loss (by LOH, truncating mutation, or promoter methylation) is a mechanism of acquired resistance to palbociclib in ~15% of HR+ breast cancer

## Connections

- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin D1 phosphorylates RB at S780/S795/T821 → E2F-DP release → S phase entry; CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) block RB phosphorylation → G1 arrest; RB1 mutation or deletion renders CDK4/6 inhibition ineffective — a key resistance biomarker in breast cancer.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — CDKN2A encodes p16/INK4a (CDK4/6 inhibitor → RB) and p14/ARF (MDM2 inhibitor → p53); CDKN2A deletion loses both tumor suppressors simultaneously; RB and p53 are the two canonical checkpoint gatekeepers; co-loss in SCLC, NEPC, and glioblastoma drives aggressive progression.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — E2F1/2/3 released from RB → transcribe MYC, CDC25A, and cyclin E → RB hyperphosphorylation (positive feedback); MYC upregulates CDK4/cyclin D → RB phosphorylation; RB loss → unconstrained E2F-MYC transcription axis; RB-null SCLC is MYC-amplified in ~15% of cases.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — RB represses HIF-1alpha target genes at chromatin via E2F repressor complexes; RB loss in SCLC → derepression of HIF-1alpha → VEGF and glycolysis genes constitutively expressed; RB-HIF-1alpha axis links cell cycle control to metabolic adaptation in aggressive cancers.

[^dyson-2016-rb-review]: Dyson NJ. RB1: a prototype tumor suppressor and an enigma. *Genes Dev.* 2016;30(13):1492-1502. [doi:10.1101/gad.282145.116](https://doi.org/10.1101/gad.282145.116) · [PubMed 27401552](https://pubmed.ncbi.nlm.nih.gov/27401552/)
[^beroukhim-2010-deletion]: Beroukhim R, Mermel CH, Porter D, et al. The landscape of somatic copy-number alteration across human cancers. *Nature.* 2010;463(7283):899-905. [doi:10.1038/nature08822](https://doi.org/10.1038/nature08822) · [PubMed 20164920](https://pubmed.ncbi.nlm.nih.gov/20164920/)
