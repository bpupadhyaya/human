---
schema: human-scale-entry/v1
id: klln
name: KLLN
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "KLLN (KILLIN) is a p53 transcriptional target that binds PCNA to stall DNA replication forks during S-phase; germline KLLN promoter hypermethylation silences KLLN in PTEN-mutation-negative Cowden syndrome; LOF → unconstrained replication → genomic instability → tumorigenesis."
aliases: ["KLLN", "KILLIN", "KLLN tumor suppressor", "KLLN PCNA", "KLLN p53 target", "KLLN Cowden syndrome", "KLLN epigenetic silencing", "KILLIN DNA replication", "KLLN 10q23"]
sources:
  - id: bennett-2010-klln-cowden
    type: peer-reviewed
    cite: "Bennett KL, Mester J, Eng C. Germline epigenetic regulation of KILLIN in Cowden and Cowden-like syndrome. JAMA. 2010;304(24):2724-2731."
    doi: "10.1001/jama.2010.1877"
    pmid: "21177507"
    url: "https://doi.org/10.1001/jama.2010.1877"
  - id: eng-2003-pten-syndromes
    type: peer-reviewed
    cite: "Eng C. PTEN: one gene, many syndromes. Hum Mutat. 2003;22(3):183-198."
    doi: "10.1002/humu.10257"
    pmid: "12938083"
    url: "https://doi.org/10.1002/humu.10257"
cross_links:
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "KLLN promoter CpG hypermethylation silences KLLN in ~30-35% of PTEN-mutation-negative Cowden patients; KLLN and PTEN are co-located at 10q23 and regulate overlapping tumor suppressor functions; KLLN LOF → replication stress → genomic instability → PHTS tumors."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "KLLN is co-located at 10q23 antisense to PTEN; both regulate PI3K-AKT-mTOR by distinct mechanisms: PTEN dephosphorylates PIP3; KLLN inhibits DNA replication via PCNA binding; KLLN promoter hypermethylation occurs in PTEN-wildtype Cowden patients."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "KLLN is a direct p53 transcriptional target via p53 response element in KLLN promoter; p53 → KLLN induction → PCNA binding → S-phase replication arrest; KLLN acts at a checkpoint distinct from p21 (G1/S) and p16 (CDK4/6 G1); KLLN is a p53 effector for replication stress."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "KLLN LOF at 10q23 disinhibits PI3K-AKT-mTOR via PTEN colocalization; mTOR inhibitors (everolimus, sirolimus) are rationally applied in PTEN hamartoma tumor syndrome (Cowden/TSC overlap); mTOR complex 1 drives protein synthesis and cell growth downstream of PTEN/AKT loss."
---

# KLLN

## Overview

**KLLN** (KILLIN; Killing protein) is a 213 amino acid (~24 kDa) **intrinsically disordered nuclear protein** encoded by a single-exon gene at chromosomal locus **10q23.31** — positioned on the antisense strand approximately 1 kb upstream of the PTEN transcription start site. KLLN was identified as a direct **p53 transcriptional target** by Lin et al. (2008), and its clinical significance was established by Bennett et al. (2010) who demonstrated that germline epigenetic silencing of KLLN by promoter CpG island hypermethylation accounts for ~30-35% of PTEN-mutation-negative Cowden and Cowden-like syndrome patients. KLLN acts as a **replication checkpoint effector**: upon p53 activation, KLLN accumulates in the nucleus and binds **PCNA** (proliferating cell nuclear antigen), competing with DNA polymerase δ for the PCNA replication clamp → stalling replication fork elongation during S-phase. KLLN thus provides an intra-S checkpoint that complements p21's G1/S arrest function, and its silencing leads to unconstrained DNA replication → genomic instability → tumorigenesis in hormone-sensitive tissues [^bennett-2010-klln-cowden] [^eng-2003-pten-syndromes].

**KLLN in the 10q23 tumor suppressor landscape:**

| Gene | Strand | Position | Function | LOF Mechanism |
|---|---|---|---|---|
| PTEN | Sense | 10q23.31 | PIP3 phosphatase | Mutation (coding/regulatory) |
| KLLN | Antisense | 10q23.31 | PCNA-binding replication blocker | Promoter CpG methylation |
| MKI67 (Ki-67) | Unrelated | Separate | Proliferation marker | N/A |

## Structure

### KLLN protein domains

**PCNA-interacting protein (PIP) box (aa 1-9):**
- N-terminal PIP box motif (consensus: Q-x-x-[LIM]-x-x-[AF]-[AF]); KLLN N-terminal QEDLEEF-like sequence; contacts the hydrophobic pocket of PCNA at the interdomain connecting loop (IDCL) of each PCNA subunit
- PCNA is a homotrimeric ring-shaped sliding clamp that encircles dsDNA at replication forks; serves as a processivity platform for DNA polymerase δ (pol δ), pol ε, PCNA-interacting DNA repair proteins, and cell cycle regulators
- KLLN PIP box binds the same hydrophobic pocket as pol δ's PIP box — direct competition → KLLN displaces pol δ from PCNA → replication fork elongation stalls
- This is a steric competition mechanism; KLLN does not catalytically inactivate PCNA, pol δ, or any other enzyme

**Nuclear localization signal (NLS, C-terminal):**
- Bipartite NLS in C-terminal region → importin-α/β → constitutive nuclear localization
- KLLN has no known cytoplasmic function; no membrane-anchoring domains; no enzymatic activity
- No post-translational modifications identified that regulate KLLN stability or localization (contrast with p27's phospho-regulation by AKT and CDK2); KLLN abundance is primarily regulated at the transcriptional level by p53

**Intrinsically disordered core (aa 10-200):**
- Central region: no structured domains identified by X-ray or NMR; intrinsically disordered (IDP); disordered proteins often function as scaffolds or competitive inhibitors via short linear motifs (SLiMs)
- KLLN likely uses its PIP box as a SLiM to engage PCNA while the remainder of the molecule projects away without folding

**KLLN promoter CpG island:**
- CpG island spans ~650 bp overlapping the KLLN TSS; contains a canonical p53 response element (two p53 half-sites: RRRCWWGYYY motif × 2, separated by 10 bp) within the CpG island
- DNMT3A-mediated CpG methylation at the KLLN CpG island is the primary mechanism of germline epigenetic silencing in PTEN-mutation-negative Cowden patients
- KLLN methylation is heritable (germline epigenetic, transmitted like a germline mutation but via chromatin state rather than DNA sequence alteration) — documented family transmission in Bennett 2010

## Function

### KLLN as a p53-induced intra-S checkpoint effector

**p53-KLLN-PCNA signaling cascade:**
1. DNA damage (DSBs, replication stress, UV) → ATM/ATR kinases → p53 phosphorylation (Ser15 by ATM, Ser317 by ATR) → p53 tetramer stability
2. p53 tetramer binds p53 response element in KLLN promoter → KLLN mRNA induction (simultaneous with p21/CDKN1A, MDM2, BAX, PUMA induction)
3. KLLN protein accumulates in nucleus within 3-6 hours of p53 activation
4. KLLN N-terminal PIP box displaces pol δ PIP box from PCNA at active replication forks → fork elongation stalls → CDC45-MCM-GINS (CMG) helicase continues unwinding briefly → ssDNA accumulation → RPA coating → ATR-ATRIP recruitment → CHK1 phosphorylation → intra-S checkpoint
5. S-phase arrest: cells halt DNA synthesis; DNA damage repair proteins (RAD51, FANCD2) are recruited via their own PCNA interactions (which remain functional — KLLN competes specifically with pol δ, not all PCNA partners)

**Complementarity with p21 (CDKN1A):**
- p21 acts at G1/S: inhibits CDK2-CyclinE → Rb remains hypophosphorylated → E2F1 sequestered → S-phase gene program not activated → cells arrest in G1
- KLLN acts within S-phase: once cells enter S (past the G1/S checkpoint) → KLLN stalls ongoing forks → prevents completion of DNA replication under conditions of unrepaired damage
- Together p21 (G1 arrest) + KLLN (S arrest) create a two-stage p53-mediated cell cycle arrest that completely suppresses replication under genotoxic conditions
- In KLLN-deficient cells: p21 is intact (PTEN-wildtype, p53-wildtype) but KLLN is absent → G1 arrest is maintained but intra-S checkpoint is impaired → if any cells escape G1 arrest and enter S-phase, replication continues despite DNA damage → increased mutation rate

**Tissue-specific vulnerability to KLLN LOF:**
- KLLN mRNA is highest in breast, thyroid, endometrial, and renal tissues (consistent with Cowden cancer spectrum)
- RRAS2 equivalent: just as RRAS2 is specifically expressed in Schwann cells (LZTR1-schwannoma specificity), high KLLN expression in these endocrine/reproductive tissues means KLLN LOF creates a tissue-specific replication checkpoint deficiency
- Under estrogen/thyroid hormone mitogenic stimulation: KLLN normally limits replication velocity; KLLN loss → hormonal mitogenic drive is unchecked → accumulation of oncogenic mutations

## Mechanism

### Epigenetic co-regulation of KLLN and PTEN at 10q23

**10q23 chromatin domain:**
- KLLN and PTEN are separated by ~1 kb in a bidirectional promoter-like configuration; the region between them contains enhancer elements active in breast and thyroid epithelium (H3K27ac, H3K4me1 marks)
- CTCF insulators flank the ~15 kb region containing both genes, creating a shared TAD (topologically associating domain); CTCF binding at this locus prevents KLLN/PTEN enhancers from acting on neighboring genes
- 10q23 LOH (allelic loss) in sporadic tumors: simultaneously deletes both PTEN and KLLN → complete loss of both tumor suppressors from that allele; in combination with somatic PTEN mutation on the other allele → biallelic PTEN inactivation + hemizygous or complete KLLN loss

**Germline KLLN epigenetic mutation:**
- In Cowden-like patients with KLLN promoter hypermethylation: PTEN coding sequence, splice sites, and regulatory regions are wildtype; but KLLN CpG island methylation silences KLLN → haploinsufficiency of KLLN from birth → impaired intra-S checkpoint in hormone-sensitive tissues → cancer predisposition matching classic Cowden
- Methylation testing: bisulfite pyrosequencing quantifies methylation at 3-5 CpG sites within the KLLN island; >10-15% methylation (vs <5% in controls) is diagnostic; distinguishable from somatic methylation by its presence in normal blood (germline = constitutional methylation)
- Demethylation: DNMT inhibitors (5-azacytidine, decitabine) restore KLLN mRNA in cell models; clinical application in KLLN-methylated PHTS tumors is investigational

**KLLN somatic inactivation in sporadic cancers:**
- KLLN promoter methylation in sporadic tumors: ~12-15% of breast, ~8-10% of thyroid, ~12% of endometrial carcinomas — same organs as germline PHTS tumors; rare somatic mutations (frameshifts/nonsense) contribute additionally in <2-3% of cases
- KLLN expression loss by IHC: nuclear KLLN protein absent in tumor vs present in adjacent normal epithelium; correlates with higher tumor grade and more aggressive behavior in breast cancer series

**Pharmacological implications:**
- MEK inhibitors: not directly applicable (KLLN/PTEN pathway is PI3K, not RAS-MAPK; some crosstalk exists)
- mTOR inhibitors (everolimus, sirolimus): directly relevant in PTEN/KLLN-deficient tumors; PTEN LOF → PI3K-AKT → mTORC1 → S6K1/4EBP1 → protein synthesis/cell growth; mTORC1 inhibition is synthetic lethal with PI3K pathway addiction; everolimus approved for PTEN-associated tumors (HR+ BC, renal angiomyolipomas in TSC, pNETs)
- No KLLN activators available; DNMT inhibitors (demethylating agents) as potential KLLN de-repressors: in early investigation

## Connections

- `connects-to` → **[Cowden Syndrome](../../07-system/cowden-syndrome/README.md)** — KLLN promoter CpG hypermethylation silences KLLN in ~30-35% of PTEN-mutation-negative Cowden patients; KLLN and PTEN are co-located at 10q23 and regulate overlapping tumor suppressor functions; KLLN LOF → replication stress → genomic instability → PHTS tumors.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — KLLN is co-located at 10q23 antisense to PTEN; both regulate PI3K-AKT-mTOR by distinct mechanisms: PTEN dephosphorylates PIP3; KLLN inhibits DNA replication via PCNA binding; KLLN promoter hypermethylation occurs in PTEN-wildtype Cowden patients.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — KLLN is a direct p53 transcriptional target via p53 response element in KLLN promoter; p53 → KLLN induction → PCNA binding → S-phase replication arrest; KLLN acts at a checkpoint distinct from p21 (G1/S) and p16 (CDK4/6 G1); KLLN is a p53 effector for replication stress.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — KLLN LOF at 10q23 disinhibits PI3K-AKT-mTOR via PTEN colocalization; mTOR inhibitors (everolimus, sirolimus) are rationally applied in PTEN hamartoma tumor syndrome (Cowden/TSC overlap); mTOR complex 1 drives protein synthesis and cell growth downstream of PTEN/AKT loss.

[^bennett-2010-klln-cowden]: Bennett KL, Mester J, Eng C. Germline epigenetic regulation of KILLIN in Cowden and Cowden-like syndrome. *JAMA.* 2010;304(24):2724-2731. [doi:10.1001/jama.2010.1877](https://doi.org/10.1001/jama.2010.1877) · [PubMed 21177507](https://pubmed.ncbi.nlm.nih.gov/21177507/)
[^eng-2003-pten-syndromes]: Eng C. PTEN: one gene, many syndromes. *Hum Mutat.* 2003;22(3):183-198. [doi:10.1002/humu.10257](https://doi.org/10.1002/humu.10257) · [PubMed 12938083](https://pubmed.ncbi.nlm.nih.gov/12938083/)
