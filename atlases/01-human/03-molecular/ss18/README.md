---
schema: human-scale-entry/v1
id: ss18
name: SS18
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "SS18 (SYT) is a canonical BAF complex subunit; SS18-SSX1/SSX2 fusion (t(X;18)) displaces SMARCB1 from BAF → EZH2/PRC2 gains access → H3K27me3 → transcriptional silencing; SS18-SSX fusion defines synovial sarcoma (100%); tazemetostat and trabectedin target SS18-SSX-driven tumors."
aliases: ["SS18", "SYT", "SS18-SSX", "SS18-SSX1", "SS18-SSX2", "synovial sarcoma translocation", "t(X;18)", "SS18 BAF complex", "SWI/SNF SS18", "SS18-SSX fusion"]
sources:
  - id: kadoch-2013-ss18-ssx-baf
    type: peer-reviewed
    cite: "Kadoch C, Crabtree GR. Reversible disruption of mSWI/SNF (BAF) complexes by the SS18-SSX oncogenic fusion in synovial sarcoma. Cell. 2013;153(1):71-85."
    doi: "10.1016/j.cell.2013.02.036"
    pmid: "23540691"
    url: "https://doi.org/10.1016/j.cell.2013.02.036"
  - id: ladanyi-2001-syt-ssx-synovial
    type: peer-reviewed
    cite: "Ladanyi M. Fusions of the SYT and SSX genes in synovial sarcoma. Oncogene. 2001;20(40):5755-5762."
    doi: "10.1038/sj.onc.1204601"
    pmid: "11607825"
    url: "https://doi.org/10.1038/sj.onc.1204601"
cross_links:
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "SS18-SSX fusion displaces SMARCB1 (INI1) from canonical BAF → SMARCB1 evicted and degraded → BAF destabilized → EZH2/PRC2 access to target loci; mechanism parallels biallelic SMARCB1 LOF in AT/RT but SMARCB1 protein is displaced, not mutated; EZH2 inhibitors rescue BAF targets."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "SS18-SSX displaces SMARCB1 → canonical BAF destabilized → PRC2/EZH2 unrestricted → H3K27me3 at CDKN2A, SOX2, and differentiation loci; SS is uniquely EZH2-dependent; tazemetostat (SARC057 trial, Tap 2022): ORR 22%, DCR 67% in heavily pretreated synovial sarcoma."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "SS18-SSX → BRD4-occupied super-enhancers at MYC and oncogene loci → MYC transcription; synovial sarcoma shows ETV4 (MYC target) overexpression; BET inhibitor JQ1 suppresses MYC in SS cells; MYC-driven proliferation in SS context is EZH2-dependent (EZH2 silences MYC inhibitors)."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Homozygous CDKN2A deletion in ~10-15% synovial sarcoma; EZH2/H3K27me3 epigenetically silences CDKN2A even without deletion → absent p16 → CDK4/6 hyperactivation → RB1 phosphorylation → E2F-driven S-phase; CDK4/6 inhibitors (palbociclib) under investigation in CDKN2A-deleted SS."
---

# SS18

## Overview

**SS18** (synovial sarcoma translocation gene, chromosome 18; formerly **SYT**) encodes a 392-amino-acid subunit of the **canonical BAF (cBAF) SWI/SNF** chromatin remodeling complex. In the normal BAF complex, SS18 contributes a glutamine/proline/glycine/tyrosine-rich (QPGY) activation domain that recruits transcriptional coactivators. In synovial sarcoma, chromosomal translocation t(X;18)(p11;q11) produces a **SS18-SSX1 or SS18-SSX2 fusion protein** that incorporates into the BAF complex in place of wild-type SS18, displacing SMARCB1 (INI1) and creating an EZH2-dependent transcriptional state [^kadoch-2013-ss18-ssx-baf]. The SS18-SSX fusion is **pathognomonic for synovial sarcoma** (~100% of cases) and is absent from all other sarcoma subtypes.

**Translocation variants:**
- **SS18-SSX1** [t(X;18)(p11.23;q11.2)]: ~65-70% of synovial sarcomas; associated with biphasic (epithelial + spindle) histology; slightly worse prognosis
- **SS18-SSX2** [t(X;18)(p11.21;q11.2)]: ~30-35%; predominantly monophasic (spindle cell); comparable or slightly better prognosis vs SSX1
- **SS18-SSX4** [t(X;18)(p11.22;q11.2)]: rare (<1%); similar biology; SSX4 on Xp11.22
- All fusions join exon 10 of SS18 (with loss of C-terminal 8 aa) to exon 6 of SSX (SSX C-terminal KRAB-like domain retained)

**Diagnostic utility:**
- FISH (SS18 break-apart probe): detects any SS18 rearrangement; sensitivity ~95%, specificity >99%
- RT-PCR (SS18-SSX1/SSX2 transcript-specific): confirms specific fusion partner; required for clinical trial eligibility in some studies
- RNA sequencing (fusion detection panels): comprehensive and increasingly standard in ambiguous spindle cell sarcomas
- **TLE1 IHC** (transducin-like enhancer protein 1): strong nuclear positivity; highly sensitive (~90%) and specific marker for SS; useful when molecular testing unavailable

## Structure

### SS18 protein architecture

**N-terminal domain (aa 1-100):**
Interaction surface for BAF complex subunits SMARCD1 and SMARCC2; required for BAF complex incorporation; retained intact in SS18-SSX fusion protein; mediates interaction with the SMARCA4 (BRG1) ATPase subunit

**QPGY activation domain (aa 180-350):**
Glutamine/proline/glycine/tyrosine-rich intrinsically disordered region; mediates transcriptional activation via phase-separation with YAP1, BRD4, and MED coactivators; this activation domain is retained and constitutively active in SS18-SSX

**C-terminal domain (aa 350-392):**
In normal SS18: interacts with SMARCB1 (INI1) and coordinates cBAF complex stability; in SS18-SSX: replaced by SSX C-terminus (aa 57-188) containing SSXRD (SSX repressor domain) and KRAB-like sequences → instead of stabilizing SMARCB1, the SSX tail physically displaces SMARCB1

### SS18-SSX fusion mechanism [^kadoch-2013-ss18-ssx-baf]

The SS18-SSX fusion protein incorporates into the canonical BAF (cBAF) complex:

1. **SS18-SSX competes with wild-type SS18** for cBAF complex incorporation → SS18-SSX progressively replaces normal SS18 in the complex
2. **SMARCB1 eviction**: the SSX C-terminal domain engages the SMARCB1 binding interface on the cBAF complex → SMARCB1 displaced → SMARCB1 protein is polyubiquitinated and degraded by the proteasome
3. **BAF complex destabilization**: without SMARCB1, the cBAF complex is less stable → PRC2/EZH2 access to BAF target gene loci is restored (contrast with normal BAF → PRC2 exclusion)
4. **H3K27me3 accumulation**: EZH2 methylates H3K27 → silences CDKN2A, SOX2, and differentiation loci
5. **Activation domain retained**: QPGY domain of SS18 drives oncogenic transcriptional activation of VEGF, ETV4, and MYC targets → tumor growth

**Key mechanistic insight** (Kadoch & Crabtree 2013): the SS18-SSX mechanism is **reversible** — knockdown of SS18-SSX with siRNA restores SMARCB1 to cBAF, reactivates BAF target genes, and induces G1 arrest and differentiation in SS cells. This validates SS18-SSX as the essential oncogenic driver and demonstrates that, unlike AT/RT (where SMARCB1 is genetically deleted), the BAF loss in SS is pharmacologically reversible.

### SSX protein domain structure

SSX1/SSX2 are nuclear proteins containing:
- **SSXRD (SSX repressor domain)**: interacts with Polycomb repressive complexes (PRC1 and PRC2) → recruits repressive chromatin modifiers
- **KRAB-like domain**: additional transcriptional repression via KAP1/TRIM28 co-repressor
- SSX proteins are normally expressed only in testis and trophoblasts (cancer-testis antigens)
- SSX1/SSX2 are encoded on the X chromosome → both alleles can be translocated in male SS (single fusion); female SS requires either X-inactivation escape or one functional allele remaining

## Function

### Normal SS18 roles

**BAF complex assembly:**
SS18 is a structural scaffold subunit of the cBAF complex, tethering the QPGY activation module to the BRG1/SMARCA4 ATPase core; required for cBAF stability at promoters and enhancers of actively transcribed genes

**Neural crest and mesenchymal differentiation:**
BAF-SS18 complexes are required for normal neural crest differentiation → specifies non-myogenic mesenchymal lineages; SS18 knockout mice show neural crest defects and perinatal lethality; this developmental role explains why SS18-SSX drives a tumor morphologically resembling both epithelial and mesenchymal lineages (synovial sarcoma's characteristic biphasic appearance)

**YAP coactivator function:**
SS18 QPGY domain interacts with YAP transcriptional coactivator → BRD4 recruitment → super-enhancer activity at pluripotency genes; this explains high ETV4 and MYC expression even in the absence of upstream RTK/RAS mutations in SS

### SS18-SSX-driven oncogenesis

The fusion protein oncogenically hijacks BAF function:
- **Loss of differentiation** (via CDKN2A, HOX gene silencing)
- **VEGF overexpression** (HIF-1α target; SS is a highly vascular tumor)
- **ETV4 overexpression** (ETS transcription factor, MYC target; drives invasion)
- **SOX2 re-expression** (stem cell factor; silenced in BAF-intact cells, re-expressed when EZH2 methylates differentiation loci)
- **Wnt pathway activation** (BAF normally limits Wnt target genes; SS18-SSX → de-repression of Wnt targets)

## Mechanism

### EZH2 inhibition (tazemetostat)

Tazemetostat (EPZ-6438) competitively inhibits EZH2 SET domain → H3K27me3 ↓ at SS18-SSX target loci → transcriptional de-repression → CDKN2A restoration → G1 arrest and differentiation

**SARC057 (Phase 2, Tap 2022):** N=~62 patients with relapsed/refractory SS; tazemetostat 800 mg BID; ORR 22%; DCR (disease control rate) ~67%; median PFS ~5-6 months; FDA granted breakthrough therapy designation for tazemetostat in SS; first molecularly targeted therapy with demonstrated activity in SS

**SMARCB1 IHC note**: in SS, SMARCB1 IHC is **retained** (contrast AT/RT where it is lost) — SMARCB1 is displaced from BAF but the protein persists in nuclei at detectable levels; SMARCB1 IHC cannot be used to diagnose or stratify SS

### Trabectedin

Trabectedin (ecteinascidin-743) binds the DNA minor groove at GC-rich sequences → stalls RNA Pol II at SS18-SSX target gene promoters → directly disrupts SS18-SSX binding to BAF at occupied genomic loci → SS18-SSX evicted from chromatin → target gene silencing partially reversed; this proposed mechanism is unique to translocation-positive sarcomas (SS, myxoid liposarcoma)

### BET inhibitors

BRD4 occupies super-enhancers at MYC and ETV4 loci in SS → MYC transcription; JQ1 (BET inhibitor) strongly suppresses MYC in SS cell lines; combination tazemetostat + JQ1: synergistic in preclinical SS models (EZH2 silences MYC suppressors while BRD4 drives MYC; dual inhibition blocks both arms)

## Connections

- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — SS18-SSX fusion displaces SMARCB1 (INI1) from canonical BAF → SMARCB1 evicted and degraded → BAF destabilized → EZH2/PRC2 access to target loci; mechanism parallels biallelic SMARCB1 LOF in AT/RT but SMARCB1 protein is displaced, not mutated; EZH2 inhibitors rescue BAF targets.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — SS18-SSX displaces SMARCB1 → canonical BAF destabilized → PRC2/EZH2 unrestricted → H3K27me3 at CDKN2A, SOX2, and differentiation loci; SS is uniquely EZH2-dependent; tazemetostat (SARC057 trial, Tap 2022): ORR 22%, DCR 67% in heavily pretreated synovial sarcoma.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — SS18-SSX → BRD4-occupied super-enhancers at MYC and oncogene loci → MYC transcription; synovial sarcoma shows ETV4 (MYC target) overexpression; BET inhibitor JQ1 suppresses MYC in SS cells; MYC-driven proliferation in SS context is EZH2-dependent (EZH2 silences MYC inhibitors).
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Homozygous CDKN2A deletion in ~10-15% synovial sarcoma; EZH2/H3K27me3 epigenetically silences CDKN2A even without deletion → absent p16 → CDK4/6 hyperactivation → RB1 phosphorylation → E2F-driven S-phase; CDK4/6 inhibitors (palbociclib) under investigation in CDKN2A-deleted SS.

[^kadoch-2013-ss18-ssx-baf]: Kadoch C, Crabtree GR. Reversible disruption of mSWI/SNF (BAF) complexes by the SS18-SSX oncogenic fusion in synovial sarcoma. *Cell.* 2013;153(1):71-85. [doi:10.1016/j.cell.2013.02.036](https://doi.org/10.1016/j.cell.2013.02.036) · [PubMed 23540691](https://pubmed.ncbi.nlm.nih.gov/23540691/)
[^ladanyi-2001-syt-ssx-synovial]: Ladanyi M. Fusions of the SYT and SSX genes in synovial sarcoma. *Oncogene.* 2001;20(40):5755-5762. [doi:10.1038/sj.onc.1204601](https://doi.org/10.1038/sj.onc.1204601) · [PubMed 11607825](https://pubmed.ncbi.nlm.nih.gov/11607825/)
