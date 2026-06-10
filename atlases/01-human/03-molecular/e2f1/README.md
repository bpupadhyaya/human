---
schema: human-scale-entry/v1
id: e2f1
name: E2F1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "E2F1 is the primary activating E2F transcription factor released from Rb upon CDK4/6-mediated Rb phosphorylation; drives S-phase genes (CCNE1, MCM2-7, PCNA); pro-apoptotic via ARF-p53; RB1 LOF → unchecked E2F1 → proliferation in retinoblastoma and diverse cancers."
aliases: ["E2F1", "E2F transcription factor 1", "E2F-1", "Rb-E2F axis", "E2F1 cell cycle", "E2F1 apoptosis", "E2F1 S-phase", "E2F1 RB1", "activating E2F", "E2F1 cancer"]
sources:
  - id: helin-1992-e2f1
    type: peer-reviewed
    cite: "Helin K, Lees JA, Vidal M, Dyson N, Harlow E, Fattaey A. A cDNA encoding a pRB-binding protein with properties of the transcription factor E2F. Cell. 1992;70(2):337-350."
    doi: "10.1016/0092-8674(92)90107-n"
    pmid: "1638634"
    url: "https://doi.org/10.1016/0092-8674(92)90107-n"
  - id: deleo-2020-e2f1-review
    type: peer-reviewed
    cite: "DeGregori J, Johnson DG. Distinct and Overlapping Roles for E2F Family Members in Transcription, Proliferation and Apoptosis. Curr Mol Med. 2006;6(7):739-748."
    doi: "10.2174/156652406778195227"
    pmid: "17100600"
    url: "https://doi.org/10.2174/156652406778195227"
cross_links:
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB1 pocket domain binds E2F1 C-terminus and DP1 dimerization partner → E2F1 transactivation repressed; CDK4/6-CyclinD phosphorylates Rb at Ser780/Ser807/Ser811 → E2F1 released → G1/S gene transcription; RB1 LOF in cancer → constitutive E2F1 release → cell cycle entry."
  - target: 01-human/03-molecular/cdkn1a
    relation: connects-to
    note: "p21 inhibits CDK2-CyclinE and CDK4/6-CyclinD → Rb remains hypophosphorylated → E2F1-Rb complex stable → S-phase gene repression maintained; p21-Rb-E2F1 axis links p53 DNA damage checkpoint to cell cycle arrest; E2F1 overexpression overrides p21-induced Rb-mediated repression."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "E2F1 and Myc cooperate at overlapping S-phase gene promoters (CCNE1, CDC6, ORC1); Myc directly transcribes E2F1; E2F1 reciprocally activates Myc; both E2F1 and Myc also activate ARF/p14 as a failsafe → p53 → apoptosis; overexpression of either can initiate tumorigenesis."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "E2F1 is released constitutively when RB1 is biallelically lost in retinoblastoma; unchecked E2F1 drives retinal progenitor proliferation → tumor mass; retinoblastoma cells have MYCN amplification and additional mutations that cooperate with E2F1 dysregulation."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cyclin D1-CDK4/6 phosphorylates Rb → E2F1 dissociates → S-phase transcription; cyclin D1 is the upstream activator of E2F1; CDK4/6 inhibitors restore Rb-E2F1 repression → G1 arrest in HR+ breast cancer and other cyclin D-driven tumors."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "RB1 biallelic deletion in ~70% of osteosarcoma → constitutive E2F1 release → unchecked S-phase in osteoprogenitors; E2F1 drives DHFR/thymidylate synthase → methotrexate sensitivity; TP53 LOF co-occurs with RB1 loss in high-grade osteosarcoma, removing both cell cycle checkpoints."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "E2F1 is overexpressed in ER-/triple-negative breast cancer; CDK4/6-CyclinD1 → Rb phosphorylation → E2F1 release is primary growth mechanism in ER+ breast cancer; CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) restore Rb-E2F1 repression → FDA-approved for HR+/HER2- mBC."
---

# E2F1

## Overview

**E2F1** (E2F Transcription Factor 1) is the founding member of the E2F family of transcription factors and the primary downstream effector of the retinoblastoma (Rb) tumor suppressor pathway. E2F1 was identified as a protein that binds the Rb pocket domain and is released upon Rb hyperphosphorylation by cyclin-dependent kinases (Helin 1992). E2F1 encodes a 437 amino acid (48 kDa) protein that, when freed from Rb, activates the **S-phase gene expression program** necessary for DNA replication and cell cycle progression. Uniquely among activating E2F family members (E2F1/2/3a), E2F1 also possesses **pro-apoptotic activity** — activating ARF/p14, PUMA, APAF1, and caspase genes — functioning as a fail-safe mechanism against unchecked E2F activity [^helin-1992-e2f1] [^deleo-2020-e2f1-review].

**E2F family overview:**

| Family member | Classification | Rb family partner | Primary function |
|---|---|---|---|
| E2F1 | Activating | pRb (RB1) | S-phase + apoptosis (dual) |
| E2F2 | Activating | pRb (RB1) | S-phase genes |
| E2F3a | Activating | pRb (RB1) | S-phase genes |
| E2F3b | Repressive | pRb (RB1) | Gene silencing in quiescence |
| E2F4 | Repressive | p107 (RBL1), p130 (RBL2) | Gene repression in G0/G1 |
| E2F5 | Repressive | p130 (RBL2) | Differentiation repression |
| E2F6 | Repressive | None (Polycomb) | Epigenetic repression |
| E2F7/8 | Atypical | None (self-dimerize) | Late G1 repression of E2F targets |

## Structure

### E2F1 protein domains

**DNA binding domain (DBD, aa 131-191):**
- Winged-helix-turn-helix (wHTH) fold; contacts DNA at E2F-binding consensus: 5'-TTTSSCGC-3' (S = G or C)
- Requires heterodimerization with DP-1 or DP-2 for high-affinity DNA binding; E2F1-DP heterodimer binds cognate E2F sites much more avidly than E2F1 monomer
- DBD contacted by crystal structures: E2F1 DBD-DP2 DBD + DNA ternary complex; E2F and DP DBDs fold together as a pseudosymmetric dimer, each contacting alternate bases

**Dimerization domain (DD, aa 192-244):**
- Mediates E2F1-DP heterodimerization (marked leucine heptad repeats); E2F1-DP interaction is constitutive and required for DNA binding
- The E2F1-DP heterodimer = functional E2F unit; DP partner provides additional DNA-binding affinity and stabilizes E2F on chromatin

**Transactivation domain (TAD, aa 368-437):**
- C-terminal; intrinsically disordered; contains acidic activation sequences
- Directly contacts TFIID (TAF1) and CBP/p300 → recruits general transcription machinery and coactivators → gene activation
- **Rb-binding motif** within TAD: contains a modified LXCXE-related sequence (DLDX2DLDX2EF in E2F1 context); Rb pocket domain (A+B boxes) engages this motif to block TAD-mediated transactivation; Rb binding masks the TAD → transcriptional repression

**N-terminal cyclin A/CDK2 binding site (aa 1-17):**
- Cyclin A-CDK2 binds E2F1 N-terminus → phosphorylates DP partner → disrupts E2F1-DP-DNA complex → inactivates E2F1 at S/G2 boundary (ensures E2F1 activity is transient at G1/S); this auto-regulatory loop prevents excessive E2F1 accumulation in S-phase

**Nuclear localization signal (NLS):** embedded in DBD region; E2F1 is constitutively nuclear.

## Function

### Rb-E2F1 switch: the G1/S restriction point

The Rb-E2F1 pathway is the **central molecular switch** governing G1/S transition in mammalian cells:

**In quiescence (G0) and early G1:**
- Rb is hypophosphorylated (active)
- Rb pocket domain bound to E2F1 TAD → TAD activity masked → E2F1 target genes repressed
- E2F4/5-p130 complexes recruit HDAC1/2 and SUZ12 (PRC2) to E2F sites → stable epigenetic silencing of S-phase genes
- Result: cell remains in G0 or early G1; no DNA replication

**At the restriction point (mid-G1):**
- Mitogenic signals → RAS → RAF → MEK → ERK → cyclin D1 transcription → CDK4/6-CyclinD1 assembled
- CDK4/6-CyclinD1 (+ CDK2-CyclinE) phosphorylates Rb sequentially at Ser780 (CDK4), Ser807/811 (CDK4/6), Thr821/826 (CDK2): partial phosphorylation at Ser780 first → partial E2F1 release → CyclinE transcription → CDK2-CyclinE → full hyperphosphorylation → complete E2F1 release (positive feedback)
- **Hyperphosphorylated Rb cannot bind E2F1** → E2F1-DP complex binds S-phase gene promoters → transcription begins

**S-phase gene expression program activated by E2F1:**
- **Replication machinery**: MCM2-7 (helicase loading), ORC1 (origin recognition), CDC6 (origin firing), PCNA (processivity clamp), POLA1/POLE (DNA polymerases), RPA (ssDNA protection)
- **Nucleotide synthesis**: DHFR (dihydrofolate reductase), thymidine kinase (TK1), ribonucleotide reductase (RRM1/2)
- **CDK components**: CCNE1 (CyclinE), CCNA2 (CyclinA), CDC25A (CDK2 activating phosphatase)
- **Chromatin regulators**: MCM loading factors, CDC45, RIF1

### E2F1 pro-apoptotic activity (failsafe)

E2F1 is unique among activating E2Fs in its ability to directly induce apoptosis when unopposed by Rb. This failsafe prevents oncogenic E2F1 from causing unchecked proliferation:

- **ARF/p14 activation**: E2F1 binds ARF promoter → ARF (p14ARF in humans) transcription → ARF sequesters MDM2 in nucleolus → p53 stabilized → p53-dependent apoptosis (PUMA, NOXA → mitochondrial pathway)
- **Direct pro-apoptotic targets**: E2F1 also transcribes BBC3 (PUMA), CASP3, CASP7, APAF1, BIM (BCL2L11) independently of p53 → p53-independent apoptosis
- **Regulation of E2F1 apoptosis vs proliferation**: survival signals (growth factors → PI3K-AKT) promote E2F1 phosphorylation at Ser364/Ser403 → MDM2-mediated E2F1 ubiquitination → degradation of pro-apoptotic E2F1 → proliferative output dominates; in the absence of survival signals, E2F1 promotes apoptosis

### E2F1 in cancer

**Oncogenic E2F1 (RB1 LOF context):**
RB1 loss → constitutive E2F1 release → sustained S-phase gene transcription → proliferation. This is the mechanism of retinoblastoma (biallelic RB1), small cell lung cancer (SCLC, ~90% RB1 LOF), and contributes to many other cancers. Additionally, E2F1 gene amplification (rare) or overexpression driven by upstream oncoproteins (KRAS, MYC amplification, CDK4/6 amplification) can dysregulate E2F1.

**CDK4/6 inhibitor resistance:**
Palbociclib/ribociclib/abemaciclib block CDK4/6 → maintain Rb in hypophosphorylated state → E2F1 repressed → G1 arrest (mechanism of action). Resistance: RB1 LOF (Rb absent → CDK4/6i irrelevant); CCNE1 amplification (CDK2-CyclinE hyperphosphorylates Rb even when CDK4/6 blocked); CDK4/6 amplification; CDKN2A loss (no p16 to suppress CDK4/6 baseline activity in drug-free cells).

## Mechanism

### E2F1 as a therapeutic target

- **CDK4/6 inhibitors**: maintain Rb-E2F1 complex → anti-proliferative; FDA-approved in ER+/HER2-breast cancer (palbociclib, ribociclib, abemaciclib); emerging in bladder, liposarcoma, glioblastoma, lung
- **E2F1 direct inhibition**: experimental; peptides mimicking Rb TAD-binding groove; E2F1-DP dimerization inhibitors; no FDA-approved E2F1-direct drug yet
- **Exploiting E2F1 apoptosis**: oncolytic virus therapy (E1A viral protein binds Rb → releases E2F1 → p53-independent apoptosis in Rb-proficient tumor cells); E2F1 pro-apoptotic activity could be enhanced by MDM2 inhibition (stabilizes p53 → cooperates with E2F1-ARF axis)

## Connections

- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 pocket domain binds E2F1 C-terminus and DP1 dimerization partner → E2F1 transactivation repressed; CDK4/6-CyclinD phosphorylates Rb at Ser780/Ser807/Ser811 → E2F1 released → G1/S gene transcription; RB1 LOF in cancer → constitutive E2F1 release → cell cycle entry.
- `connects-to` → **[CDKN1A](../../03-molecular/cdkn1a/README.md)** — p21 inhibits CDK2-CyclinE and CDK4/6-CyclinD → Rb remains hypophosphorylated → E2F1-Rb complex stable → S-phase gene repression maintained; p21-Rb-E2F1 axis links p53 DNA damage checkpoint to cell cycle arrest; E2F1 overexpression overrides p21-induced Rb-mediated repression.
- `connects-to` → **[Myc](../../03-molecular/myc/README.md)** — E2F1 and Myc cooperate at overlapping S-phase gene promoters (CCNE1, CDC6, ORC1); Myc directly transcribes E2F1; E2F1 reciprocally activates Myc; both E2F1 and Myc also activate ARF/p14 as a failsafe → p53 → apoptosis; overexpression of either can initiate tumorigenesis.
- `connects-to` → **[Retinoblastoma](../../07-system/retinoblastoma/README.md)** — E2F1 is released constitutively when RB1 is biallelically lost in retinoblastoma; unchecked E2F1 drives retinal progenitor proliferation → tumor mass; retinoblastoma cells have MYCN amplification and additional mutations that cooperate with E2F1 dysregulation.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cyclin D1-CDK4/6 phosphorylates Rb → E2F1 dissociates → S-phase transcription; cyclin D1 is the upstream activator of E2F1; CDK4/6 inhibitors restore Rb-E2F1 repression → G1 arrest in HR+ breast cancer and other cyclin D-driven tumors.
- `connects-to` → **[Osteosarcoma](../../07-system/osteosarcoma/README.md)** — RB1 biallelic deletion in ~70% of osteosarcoma → constitutive E2F1 release → unchecked S-phase in osteoprogenitors; E2F1 drives DHFR/thymidylate synthase → methotrexate sensitivity; TP53 LOF co-occurs with RB1 loss in high-grade osteosarcoma, removing both cell cycle checkpoints.
- `connects-to` → **[Breast Cancer](../../07-system/breast-cancer/README.md)** — E2F1 is overexpressed in ER-/triple-negative breast cancer; CDK4/6-CyclinD1 → Rb phosphorylation → E2F1 release is primary growth mechanism in ER+ breast cancer; CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) restore Rb-E2F1 repression → FDA-approved for HR+/HER2- mBC.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^helin-1992-e2f1]: Helin K, Lees JA, Vidal M, Dyson N, Harlow E, Fattaey A. A cDNA encoding a pRB-binding protein with properties of the transcription factor E2F. *Cell.* 1992;70(2):337-350. [doi:10.1016/0092-8674(92)90107-n](https://doi.org/10.1016/0092-8674(92)90107-n) · [PubMed 1638634](https://pubmed.ncbi.nlm.nih.gov/1638634/)
[^deleo-2020-e2f1-review]: DeGregori J, Johnson DG. Distinct and Overlapping Roles for E2F Family Members in Transcription, Proliferation and Apoptosis. *Curr Mol Med.* 2006;6(7):739-748. [doi:10.2174/156652406778195227](https://doi.org/10.2174/156652406778195227) · [PubMed 17100600](https://pubmed.ncbi.nlm.nih.gov/17100600/)
