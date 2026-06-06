---
schema: human-scale-entry/v1
id: myc
name: MYC
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "bHLH-LZ transcription factor; master oncogene amplified or overexpressed in >50% of cancers. Drives ribosome biogenesis and cell cycle entry via E-box/MAX binding. Protein-level targeting is difficult; BET bromodomain inhibitors (JQ1) suppress MYC transcription indirectly."
aliases: ["c-MYC", "c-Myc", "proto-oncogene c-Myc", "MYCC", "MYC oncogene"]
sources:
  - id: dang-2012-myc
    type: peer-reviewed
    cite: "Dang CV. MYC on the path to cancer. Cell. 2012;149(1):22-35."
    doi: "10.1016/j.cell.2012.03.003"
    pmid: "22464321"
    url: "https://doi.org/10.1016/j.cell.2012.03.003"
  - id: stine-2015-myc-metabolism
    type: peer-reviewed
    cite: "Stine ZE, Walton ZE, Altman BJ, Hsieh AL, Dang CV. MYC, metabolism, and cancer. Cancer Discov. 2015;5(10):1024-1039."
    doi: "10.1158/2159-8290.CD-15-0507"
    pmid: "26382145"
    url: "https://doi.org/10.1158/2159-8290.CD-15-0507"
  - id: filippakopoulos-2010-jq1
    type: peer-reviewed
    cite: "Filippakopoulos P, Qi J, Picaud S, et al. Selective inhibition of BET bromodomains. Nature. 2010;468(7327):1067-1073."
    doi: "10.1038/nature09504"
    pmid: "20871596"
    url: "https://doi.org/10.1038/nature09504"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS-ERK signaling phosphorylates MYC (Ser62) → stabilization; PI3K-Akt phosphorylates GSK-3β → prevents MYC Thr58 phosphorylation → blocks MYC ubiquitination; oncogenic KRAS-driven MYC stabilization amplifies the proliferative output of RAS pathway in PDAC, CRC, and NSCLC."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTORC1 → S6K1 and 4E-BP1 → increases MYC mRNA translation rate; MYC in turn drives ribosome biogenesis (rRNA and ribosomal protein genes) → amplifies translational capacity; MYC and mTORC1 form a feed-forward anabolic growth loop in rapidly proliferating tumor cells."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "MYC is a direct Wnt/β-catenin target (TCF/LEF site in MYC promoter); APC-mutant CRC constitutively expresses MYC via nuclear β-catenin; MYC amplification can substitute for Wnt pathway mutation — both converge on the same proliferative transcriptional program."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "MYC overexpression drives ARF (CDKN2A) → p53 stabilization → apoptosis (oncogene surveillance); cancers surviving MYC amplification typically lack p53 or ARF; TP53 and CDKN2A mutations are enriched as co-occurring alterations in MYC-amplified tumors."
---

# MYC

## Overview

**MYC (c-Myc)** is a **basic helix-loop-helix leucine zipper (bHLH-LZ) transcription factor** and proto-oncogene that functions as the dominant cell-intrinsic driver of cell growth — defined as the increase in cell mass and biosynthetic capacity that precedes cell division. Originally discovered as the cellular homolog of the v-Myc viral oncogene in 1982, MYC has since been recognized as the most broadly and frequently deregulated oncogene in human cancer: amplified or overexpressed in **>50% of all human tumors** [^dang-2012-myc].

MYC operates primarily as a heterodimer with **MAX (MYC-associated factor X)**, a bHLH-LZ protein, binding to **E-box sequences** (5'-CACGTG-3') in promoter and enhancer regions. Unlike conventional transcription factors that activate specific gene sets, MYC is a **transcriptional amplifier** — it does not select new gene programs but rather **amplifies the transcription of already-active genes** proportionally to their basal activity (genome-wide transcriptional amplification model). In this sense, MYC acts as a cellular "growth rheostat": low MYC → homeostatic growth; high MYC → maximal growth and proliferation; pathologically high MYC → oncogenic transformation.

**MYC target gene programs:**
- **Ribosome biogenesis:** rRNA synthesis (RNA Pol I), ribosomal protein genes, rRNA processing enzymes (>100 direct MYC targets) → increased translational capacity → enables all downstream anabolic programs
- **Cell cycle:** Cyclin D2, CDK4, CDC25A → G1→S phase progression; represses p21/CDKN1A and p27/CDKN1B → removes cell cycle brakes
- **Metabolic reprogramming:** LDHA, PKM2 (glycolytic), glutaminase (GLS) → Warburg glycolysis and glutamine addiction [^stine-2015-myc-metabolism]
- **Protein synthesis:** eIF4E, eIF4G, eIF2B → promotes cap-dependent translation; also promotes nucleotide synthesis
- **Anti-apoptosis (paradox):** MYC simultaneously drives ARF→p53→apoptosis (tumor suppression); cancer cells that survive MYC amplification have typically lost p53 or ARF → reveals the cell-intrinsic tumor surveillance mechanism

**MYC oncogenic activation mechanisms:**
- **Amplification (8q24):** Burkitt lymphoma (100% MYC translocation), triple-negative breast cancer (~25%), SCLC (~20%), medulloblastoma, neuroblastoma (MYCN amplification)
- **Chromosomal translocation:** t(8;14) in Burkitt lymphoma → IGH enhancer-driven MYC → analogous to BCL-2 in follicular lymphoma
- **Wnt/β-catenin:** Direct TCF/LEF-driven transcription (CRC, hepatocellular carcinoma, Wnt-activated cancers)
- **KRAS/ERK:** Phospho-Ser62 stabilization → prevents ubiquitination
- **RB1 loss:** E2F1 → MYC transcription

## Structure

### MYC protein architecture [^dang-2012-myc]

MYC (c-Myc) is a **439 amino acid, ~67 kDa (apparent)** nuclear phosphoprotein (migrates at ~62-67 kDa despite 49 kDa predicted MW due to extensive proline content):

**N-terminal transactivation domain (TAD, aa 1-143):**
- Contains two conserved **MYC boxes (MBI, MBII)** — protein interaction and post-translational modification hubs
- **MBI (aa 45-63):** Contains Thr58 (GSK-3β phosphorylation → ubiquitination → degradation by Fbw7 E3 ligase); also required for p300/CBP and TRRAP (TIP60 complex) co-activator recruitment
- **MBII (aa 128-143):** Required for transformation; interacts with TRRAP, SKI, CDK8; mutations in MBII abolish oncogenic activity without affecting MAX dimerization
- TAD recruits: SP1, TFIID, p300/CBP, TRRAP (a component of HAT complexes) → chromatin opening at target promoters

**Central region (aa 144-320):**
- Contains MBIII (aa 188-200) and MBIV (aa 318-340) — regulatory regions
- Nuclear localization signal (NLS, ~aa 320-328)

**C-terminal bHLH-LZ domain (aa 355-439):**
- **Basic region (aa 355-368):** DNA binding; contacts major groove of E-box CACGTG
- **Helix-loop-helix (HLH, aa 368-410):** Mediates MAX dimerization
- **Leucine zipper (LZ, aa 410-439):** Reinforces MAX dimerization; leucine residues at every 7th position form hydrophobic contacts

**MYC:MAX:E-box ternary complex:** MYC-MAX heterodimer binds E-box as obligate pair; MAX homodimers are transcriptionally inert but compete with MYC for MAX → regulate MYC activity; MXD family proteins (Mad1/MXD1, Mad3/MXD3, MXI1, MNT) also dimerize with MAX → recruit HDAC/Sin3A repressor → actively repress MYC target genes (tumor suppressive MXD program)

### Post-translational regulation: the MYC stability switch

MYC protein has a short half-life (~20-30 minutes) in normal cells, creating a tight proliferative rheostat:

- **Mitogenic signaling (ON → stable MYC):**
  - ERK → RSK2 → MYC Ser62 phosphorylation → stabilization (blocks ubiquitination)
  - Akt → GSK-3β phosphorylation (inhibition) → prevents Thr58 phosphorylation → stabilization
  - Aurora A → directly stabilizes MYC against proteasomal degradation
  
- **Growth arrest/quiescence (OFF → unstable MYC):**
  - GSK-3β → MYC Thr58 phosphorylation (after PIN1-mediated proline isomerization that requires pSer62) → FBXW7 (F-box E3 ubiquitin ligase) recognition → polyubiquitination → proteasomal degradation
  - PP2A → dephosphorylates Ser62 → facilitates Thr58 phosphorylation → degradation

**FBXW7 as MYC tumor suppressor:** FBXW7 is mutated in ~20% of cancers (especially T-cell leukemia, CRC, NSCLC) → stabilized MYC → oncogenic amplification; FBXW7 mutations co-occur with MYC amplification in aggressive tumors.

## Function

### MYC in normal cellular growth

In non-transformed cells, MYC expression is tightly coupled to mitogenic signals:
- Growth factor → RTK → RAS-ERK → MYC transcription (ETS factors) + MYC stabilization (Ser62)
- MYC → target gene amplification → ribosome biogenesis → protein synthesis capacity → cell growth (enlargement)
- CDK4/6 activation (via cyclin D induction) → RB phosphorylation → E2F1 release → S-phase genes → cell division
- Withdrawal of growth factors → ERK drops → MYC destabilized → growth arrest (quiescence, G0)

**MYC and MYC paralogues:**
- MYCN (N-Myc): expressed in neural tissues; amplified in neuroblastoma (MYCN amp → Stage 4, poor prognosis), medulloblastoma, retinoblastoma, SCLC
- MYCL (L-Myc): limited expression; amplified in SCLC

### MYC-driven metabolic reprogramming [^stine-2015-myc-metabolism]

MYC is the **transcriptional master of tumor metabolism**, driving both glycolysis and glutamine utilization:

**Aerobic glycolysis (Warburg effect):**
- Upregulates: GLUT1 (glucose uptake), HK2 (hexokinase, glucose trapping), PFKL (phosphofructokinase, committed step), PKM2 (pyruvate kinase isoform favoring anabolic shunting), LDHA (lactate dehydrogenase A, regenerates NAD+)
- Promotes: pentose phosphate pathway (via G6PD) → ribose-5-phosphate for nucleotide synthesis
- Net: glucose → lactate, with branching to biosynthesis (nucleotides, lipids)

**Glutamine metabolism:**
- Upregulates: GLS (glutaminase) → glutamine → glutamate → α-ketoglutarate → TCA cycle (anaplerosis)
- MYC-driven glutamine addiction: cells cannot survive glutamine withdrawal → rationale for glutaminase inhibitors (CB-839/telaglenastat) in MYC-high tumors
- MYC also upregulates: asparagine synthetase (ASNS), proline synthesis, serine biosynthesis pathway

### MYC-driven immune evasion

MYC drives tumor immune evasion through multiple mechanisms:
- **CD47 upregulation:** "Don't eat me" signal → prevents macrophage phagocytosis
- **PD-L1 upregulation (CD274):** Direct MYC binding to PD-L1 promoter; explains correlation between MYC amplification and PD-L1 expression in NSCLC and TNBC
- **CXCL9/CXCL10 suppression:** Reduces chemokines that recruit cytotoxic T cells → immune exclusion
- **CD47+PD-L1 co-expression:** MYC-amplified tumors are "doubly armored" against innate and adaptive immune clearance

## Mechanism

### BET bromodomain inhibition — the path to MYC suppression [^filippakopoulos-2010-jq1]

MYC is considered "undruggable" at the protein level because:
- No traditional small molecule binding pocket (bHLH-LZ domain is a protein-protein interaction surface)
- Structurally disordered N-terminal TAD — no defined ligandable groove

**BET bromodomain inhibitors (JQ1, I-BET762, OTX015/MK-8628):**
- Discovered by Bradner lab (JQ1, 2010): thienodiazepine that competes with acetylated lysine for BRD2/3/4 BD1 domain
- BRD4 binds acetylated histones (H3K27ac, H3K9ac) at enhancers and promoters → recruits P-TEFb (CDK9/cyclin T1) → elongating RNA Pol II phosphorylation → transcriptional elongation
- **Super-enhancers (SE):** MYC and other oncogenes are regulated by clustered enhancers with exceptionally high BRD4/Mediator occupancy; SEs are disproportionately sensitive to BET inhibition
- JQ1 displaces BRD4 from MYC super-enhancer → preferential MYC transcriptional suppression (vs. housekeeping genes with typical enhancers)
- **Clinical candidates:** OTX015 (MK-8628, Phase I/II AML, lymphoma, TNBC); BMS-986158 (Phase I); birabresib (Phase I)
- **Resistance mechanisms:** BRD4 bromodomain mutations; alternative enhancer activation; Wnt/β-catenin maintaining MYC via different mechanism

**PROTAC MYC degraders:**
- MYC-targeted PROTACs using VHL or CRBN as E3 ligase recruiters are in early development; MZ1 (BRD4-targeting PROTAC) indirectly suppresses MYC
- Direct MYCMAX interface disruptors: 10058-F4, 10074-G5 — in vitro activity; no clinical candidates due to poor pharmacokinetics

**Synthetic lethality approaches:**
- Aurora B kinase synthetic lethal with MYC
- USP28/USP25 (deubiquitinases stabilizing MYC) — in preclinical development
- ODC1 (ornithine decarboxylase → polyamines required for MYC-driven growth): DFMO (difluoromethylornithine) reduces neuroblastoma recurrence in high-risk disease (Phase II positive)

## Connections

- `connects-to` → **[KRAS](../kras/README.md)** — KRAS-ERK phosphorylates MYC (Ser62) → stabilization; Akt phosphorylates and inactivates GSK-3β → prevents MYC degradation; oncogenic KRAS amplifies MYC activity as a core effector of RAS-driven proliferation in PDAC, CRC, and NSCLC.
- `connects-to` → **[mTOR](../mtor/README.md)** — mTORC1 increases MYC translation; MYC drives ribosome biogenesis → amplifies mTOR's anabolic output; MYC and mTOR form a feed-forward growth amplifier, with dual inhibition producing synergistic anti-tumor effects.
- `connects-to` → **[Wnt/beta-catenin](../wnt-beta-catenin/README.md)** — MYC is a direct Wnt target gene (TCF/LEF E-box in MYC promoter); APC-mutant CRC and all Wnt-activated cancers depend on MYC as the primary downstream proliferative effector; MYC amplification can substitute for Wnt pathway mutations.
- `connects-to` → **[p53](../p53/README.md)** — MYC overexpression induces ARF (CDKN2A p14) → p53 stabilization → apoptosis (oncogene surveillance); cancers with MYC amplification are enriched for TP53 and ARF mutations that disable this barrier; MYC and p53 are thus in a functional opposition in cancer evolution.

[^dang-2012-myc]: Dang CV. MYC on the path to cancer. *Cell.* 2012;149(1):22-35. [doi:10.1016/j.cell.2012.03.003](https://doi.org/10.1016/j.cell.2012.03.003) · [PubMed 22464321](https://pubmed.ncbi.nlm.nih.gov/22464321/)
[^stine-2015-myc-metabolism]: Stine ZE, Walton ZE, Altman BJ, Hsieh AL, Dang CV. MYC, metabolism, and cancer. *Cancer Discov.* 2015;5(10):1024-1039. [doi:10.1158/2159-8290.CD-15-0507](https://doi.org/10.1158/2159-8290.CD-15-0507) · [PubMed 26382145](https://pubmed.ncbi.nlm.nih.gov/26382145/)
[^filippakopoulos-2010-jq1]: Filippakopoulos P, Qi J, Picaud S, et al. Selective inhibition of BET bromodomains. *Nature.* 2010;468(7327):1067-1073. [doi:10.1038/nature09504](https://doi.org/10.1038/nature09504) · [PubMed 20871596](https://pubmed.ncbi.nlm.nih.gov/20871596/)
