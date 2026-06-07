---
schema: human-scale-entry/v1
id: ewsr1
name: EWSR1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "EWSR1 is an RNA-binding protein (FUS/EWS/TAF15 family); EWSR1-FLI1 t(11;22) fusion (~85% Ewing sarcoma) creates a neo-TF that activates GGAA microsatellite enhancers and drives neuroectodermal oncogenesis; EWSR1 also fuses with ATF1, DDIT3, and WT1 in other sarcomas."
aliases: ["EWSR1", "EWS", "EWSR1-FLI1", "EWS-FLI1", "Ewing sarcoma fusion", "EWSR1 sarcoma", "EWSR1-ERG", "EWSR1 fusion oncogene"]
sources:
  - id: delattre-1992-ewsr1-fli1
    type: peer-reviewed
    cite: "Delattre O, Zucman J, Plougastel B, et al. Gene fusion with an ETS DNA-binding domain caused by chromosome translocation in human tumours. Nature. 1992;359(6391):162-165."
    doi: "10.1038/359162a0"
    pmid: "1522903"
    url: "https://doi.org/10.1038/359162a0"
  - id: grier-2003-ewing-vdc-ie
    type: peer-reviewed
    cite: "Grier HE, Krailo MD, Tarbell NJ, et al. Addition of ifosfamide and etoposide to standard chemotherapy for Ewing's sarcoma and primitive neuroectodermal tumor of bone. N Engl J Med. 2003;348(8):694-701."
    doi: "10.1056/NEJMoa020890"
    pmid: "12594313"
    url: "https://doi.org/10.1056/NEJMoa020890"
cross_links:
  - target: 01-human/03-molecular/wt1
    relation: connects-to
    note: "EWSR1-WT1 fusion drives desmoplastic small round cell tumor (DSRCT); EWSR1 TAD + WT1 zinc fingers → neo-TF activating PDGFRα and IGF1R; DSRCT: abdominal peritoneal sarcoma in young males; DSRCT and Ewing sarcoma are both EWSR1-fusion-driven round cell sarcomas."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "EWSR1-FLI1 transcriptionally activates MYC from GGAA microsatellite enhancers; MYC is a downstream effector of the Ewing oncogenic program; BET inhibitors suppress MYC in Ewing preclinically; EWSR1-FLI1+MYC co-activation drives the neuroectodermal blast phenotype."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "EWSR1-FLI1 activates IGF1R/RAS → ERK1/2 → survival and proliferation; ERK1/2 promotes NKX2-2 transcription (master Ewing neuroectodermal regulator); MEK inhibitors explored in refractory Ewing; EWSR1-FLI1 and ERK signaling co-suppress neuroectodermal differentiation."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "IGF1R signaling → PI3K-AKT-mTOR is required for EWSR1-FLI1-driven transformation; mTOR inhibitors have modest single-agent activity in Ewing; dual IGF1R+mTOR inhibition explored in Phase 1/2; EWSR1-FLI1 upregulates IGF1R → autocrine IGF loop in Ewing cells."
---

# EWSR1

## Overview

**EWSR1 (EWS RNA Binding Protein 1)** encodes a member of the **FUS/EWS/TAF15 (FET) family** of RNA-binding proteins — a class of nuclear proteins with low-complexity prion-like N-terminal domains and C-terminal RNA recognition modules. EWSR1 participates in mRNA processing, co-transcriptional RNA surveillance, and transcription-coupled splicing regulation in normal cells. EWSR1 gained clinical importance in 1992 when Delattre et al. identified the **t(11;22)(q24;q12) translocation** that fuses the EWSR1 N-terminal transactivation domain (TAD) to the FLI1 C-terminal ETS DNA-binding domain, creating the **EWSR1-FLI1 (EWS-FLI1) fusion oncoprotein** that drives ~85% of Ewing sarcomas [^delattre-1992-ewsr1-fli1]. EWSR1-FLI1 functions as a **neo-transcription factor** with a fundamentally different DNA-binding specificity from wild-type FLI1: it preferentially binds **GGAA microsatellite repeats** (absent in the normal FLI1 binding repertoire) → creates de novo enhancers at hundreds of genomic loci → activates a neuroectodermal stem cell transcriptional program incompatible with terminal differentiation. Beyond Ewing sarcoma, EWSR1 participates in tumor-defining fusions in multiple other round cell sarcomas: **EWSR1-ATF1** (clear cell sarcoma), **EWSR1-DDIT3** (myxoid liposarcoma), **EWSR1-WT1** (desmoplastic small round cell tumor/DSRCT), **EWSR1-NR4A3** (extraskeletal myxoid chondrosarcoma), **EWSR1-CREB1** (angiomatoid fibrous histiocytoma) [^grier-2003-ewing-vdc-ie].

**EWSR1 fusion oncogenes across tumors:**

| Tumor | Fusion | Frequency |
|-------|--------|-----------|
| Ewing sarcoma | EWSR1-FLI1 t(11;22) | ~85% |
| Ewing sarcoma | EWSR1-ERG t(21;22) | ~10% |
| Ewing sarcoma | EWSR1-ETV1/4/5 | <5% |
| Clear cell sarcoma | EWSR1-ATF1 t(12;22) | ~90% |
| Myxoid liposarcoma | EWSR1-DDIT3 t(12;22) | ~90% |
| DSRCT | EWSR1-WT1 t(11;22) | ~100% |
| Extraskeletal myxoid chondrosarcoma | EWSR1-NR4A3 t(9;22) | ~75% |
| Angiomatoid fibrous histiocytoma | EWSR1-CREB1 or EWSR1-ATF1 | ~90% |

## Structure

### EWSR1 protein architecture

EWSR1 is an 656-amino-acid nuclear RNA-binding protein (~68 kDa):

**N-terminal Low-Complexity/Prion-Like Domain (LCD, 1-285) — the TAD:**
Also called the EAD (EWS activation domain) or NTD (N-terminal domain); composed of repetitive amino acid units (SYGQQS repeats and variants) similar to prion-forming sequences; these repeats form condensates (liquid-liquid phase separation) with RNA Pol II CTD → promotes transcriptional elongation at target gene loci; the LCD is intrinsically disordered and highly flexible; undergoes phase transitions → assembles into nuclear granules with other FET proteins; **this domain is retained in all Ewing/sarcoma EWSR1 fusions** → provides transcriptional activation capacity to the fusion partner's DNA-binding domain.

**RGG boxes (Arg-Gly-Gly repeats, 282-385):**
Three RGG regions flanking the central RRM; RGG boxes bind G-quadruplex RNA structures in specific mRNA 3' UTRs; regulate mRNA stability and splicing; in EWSR1-FLI1 fusion, RGG3 (closest to C-terminus) is typically deleted → removes RNA-binding contribution of the fusion protein → net effect: EWSR1-FLI1 is a DNA-bound TF, not an RNA-processing protein.

**RNA Recognition Motif (RRM, 385-447):**
Classical βαβαββ fold; binds AUUAAA polyadenylation signal sequences in pre-mRNA → EWSR1 participates in 3' end processing; also binds telomeric repeat-containing RNA (TERRA); in Ewing, EWSR1 fusions typically include none or a partial RRM → RNA-binding function eliminated.

**ZF (zinc finger, 448-524):**
Cys3His1 zinc finger; binds single-stranded DNA/RNA; contributes to EWSR1 nuclear localization; typically deleted in EWSR1-FLI1 fusion (breakpoint at EWSR1 intron 7 typically → fusion includes aa 1-264 of EWSR1; breakpoints vary by type A/B/C/D fusion type).

### EWSR1-FLI1 fusion structure

**Type 1 (most common, ~60%):** EWSR1 exons 1-7 fused to FLI1 exons 6-9; generates the EWS exon 7 – FLI1 exon 6 junction; smallest fusion; retains FLI1 ETS domain + RGG3 deletion.

**Type 2 (~25%):** EWSR1 exons 1-7 fused to FLI1 exons 5-9; includes additional FLI1 N-terminal residues; slightly larger.

All fusion types share:
- EWSR1 N-terminal LCD (TAD): transactivates at FLI1-bound loci AND newly acquired GGAA repeat loci
- FLI1 ETS domain: binds canonical ETS sequences (GGA[A/T]); in EWSR1-FLI1, the ETS domain ALSO gains affinity for long GGAA microsatellite repeats (absent from normal FLI1) — this neo-binding specificity is the key oncogenic property

### GGAA microsatellite neo-enhancer mechanism

**Normal FLI1:** Binds single or short ETS sites; activates lymphoid/endothelial differentiation genes.

**EWSR1-FLI1 neo-binding:**
GGAA microsatellite repeats (>8 GGAA units) are unique binding sites for EWSR1-FLI1 (not bound by WT FLI1); ~1,300 such microsatellites genome-wide are activated as neo-enhancers by EWSR1-FLI1; key genes activated from GGAA microsatellite neo-enhancers: **NKX2-2** (primary target; master neuroectodermal TF in Ewing), FOXQ1, PRKCB, CAV1; NKX2-2 is a homeobox TF expressed in pancreatic β-cells and certain neural progenitors; in Ewing, NKX2-2 suppresses differentiation → maintains stem cell-like state; EWSR1-FLI1 also **represses** genes at ETS-motif sites: IGJ (B-cell lineage gene), ID2 (pro-differentiation HLH) — silencing lineage differentiation programs.

## Function

### Normal EWSR1 roles

**Phase separation and transcription:**
Wild-type EWSR1 (along with FUS and TAF15) forms dynamic nuclear condensates with RNA Pol II through LCD phase separation → concentrates transcription machinery at active gene loci → enhances burst transcription; EWSR1 is recruited to sites of RNA Pol II pausing → promotes pause release → productive elongation; EWSR1-null mice: early embryonic lethality (implantation defect); EWSR1 heterozygous mice: meiotic defects (required for synapsis).

**Alternative splicing:**
EWSR1 co-transcriptionally regulates alternative splicing of hundreds of pre-mRNAs by binding to RGG/RRM sequences near splice sites → promotes exon inclusion or exclusion; EWSR1 targets include calcitonin/CGRP mRNA (alternative splicing in thyroid vs neural tissues), vascular endothelial growth factor (VEGF) isoforms, and many cell cycle regulators.

**DNA damage response:**
EWSR1 is recruited to DNA double-strand breaks → interacts with BRCA1 and p53 → promotes homologous recombination; EWSR1 loss sensitizes cells to ionizing radiation and DNA-damaging agents; in the context of EWSR1-FLI1, the fusion protein disrupts normal EWSR1-mediated HR → Ewing sarcoma may have partial HR deficiency → PARP inhibitor sensitivity being explored.

### EWSR1-FLI1 oncogenic program

**SWI/SNF requirement:**
EWSR1-FLI1 recruits BAF complex (BRG1/SMARCA4 + ARID1A + SMARCD1) to GGAA microsatellite neo-enhancers → nucleosome remodeling → H3K27ac deposition → active enhancer mark → neo-enhancer activation; EWSR1-FLI1-driven gene program requires functional SWI/SNF; ARID1A loss reduces EWSR1-FLI1 target gene activation → SWI/SNF inhibitors (PROTAC-mediated BRG1/BRM degradation) disrupt the Ewing transcriptional program.

**IGF1R/mTOR dependency:**
EWSR1-FLI1 directly transcriptionally activates IGF1R → autocrine IGF2 loop → constitutive PI3K-AKT-mTOR → Ewing survival and proliferation; also: EWSR1-FLI1 suppresses IGFBP3 (IGF-binding protein 3, negative regulator of free IGF) → net increase in available IGF → enhanced IGF1R signaling; mTOR-dependent ribosome biogenesis supports the rapid growth of Ewing sarcoma.

## Mechanism

### Diagnostic use of EWSR1 FISH

**EWSR1 break-apart FISH:**
The gold standard for Ewing sarcoma diagnosis: probes flanking EWSR1 locus at 22q12 → split signal (separate green and red dots) confirms EWSR1 rearrangement; positive in ~95% of Ewing; does NOT specify fusion partner (FLI1 vs ERG vs FEV vs ATF1, etc.) — partner-specific FISH or RNA sequencing needed to confirm fusion type and exclude other EWSR1-driven sarcomas (especially clear cell sarcoma with EWSR1-ATF1 which can be EWSR1 FISH positive but has completely different biology and prognosis).

**RNA sequencing:**
Next-generation RNA sequencing (RNA-seq) with fusion caller algorithms: highest sensitivity and specificity; detects all EWSR1 fusions; identifies partner genes; preferred in diagnostic workup of round cell sarcomas; also detects novel/rare fusions; important for molecular classification of CIC-rearranged sarcomas (formerly called Ewing-like; now WHO 2020 separate entities — CIC::DUX4, BCOR::CCNB3).

### Therapeutic targeting of EWSR1-FLI1

**Direct EWS-FLI1 inhibition:**
No small molecule directly inhibits the EWSR1-FLI1 protein effectively; the LCD is disordered (no druggable pocket); FLI1 ETS domain is flat (poor small molecule binding); **TK216** (trabectedin analog; alkylates the minor groove → disrupts EWS-FLI1 from target loci): Phase 1/2 in R/R Ewing (ORR ~15%); limited activity as single agent.

**Indirect targeting via downstream effectors:**
- AURKA inhibition: EWSR1-FLI1 activates AURKA → AURKA inhibitors (alisertib) → mitotic arrest → apoptosis in Ewing; alisertib Phase 2 in Ewing
- CDK4/6 inhibition: EWSR1-FLI1 → cyclin D1/CDK4 → palbociclib Phase 1/2
- EZH2 inhibition: EWSR1-FLI1 recruits PRC2/EZH2 to repress differentiation loci; tazemetostat (EZH2 inhibitor) restores differentiation → anti-tumor in Ewing preclinically
- PARP inhibition: HR deficiency from EWSR1 loss-of-function (the fusion eliminates WT EWSR1 HR activity) → olaparib + temozolomide Phase 1/2 in pediatric solid tumors including Ewing

## Connections

- `connects-to` → **[WT1](../../03-molecular/wt1/README.md)** — EWSR1-WT1 fusion drives desmoplastic small round cell tumor (DSRCT); EWSR1 TAD + WT1 zinc fingers → neo-TF activating PDGFRα and IGF1R; DSRCT: abdominal peritoneal sarcoma in young males; DSRCT and Ewing sarcoma are both EWSR1-fusion-driven round cell sarcomas.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — EWSR1-FLI1 transcriptionally activates MYC from GGAA microsatellite enhancers; MYC is a downstream effector of the Ewing oncogenic program; BET inhibitors suppress MYC in Ewing preclinically; EWSR1-FLI1+MYC co-activation drives the neuroectodermal blast phenotype.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EWSR1-FLI1 activates IGF1R/RAS → ERK1/2 → survival and proliferation; ERK1/2 promotes NKX2-2 transcription (master Ewing neuroectodermal regulator); MEK inhibitors explored in refractory Ewing; EWSR1-FLI1 and ERK signaling co-suppress neuroectodermal differentiation.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — IGF1R signaling → PI3K-AKT-mTOR is required for EWSR1-FLI1-driven transformation; mTOR inhibitors have modest single-agent activity in Ewing; dual IGF1R+mTOR inhibition explored in Phase 1/2; EWSR1-FLI1 upregulates IGF1R → autocrine IGF loop in Ewing cells.

[^delattre-1992-ewsr1-fli1]: Delattre O, Zucman J, Plougastel B, et al. Gene fusion with an ETS DNA-binding domain caused by chromosome translocation in human tumours. *Nature.* 1992;359(6391):162-165. [doi:10.1038/359162a0](https://doi.org/10.1038/359162a0) · [PubMed 1522903](https://pubmed.ncbi.nlm.nih.gov/1522903/)
[^grier-2003-ewing-vdc-ie]: Grier HE, Krailo MD, Tarbell NJ, et al. Addition of ifosfamide and etoposide to standard chemotherapy for Ewing's sarcoma and primitive neuroectodermal tumor of bone. *N Engl J Med.* 2003;348(8):694-701. [doi:10.1056/NEJMoa020890](https://doi.org/10.1056/NEJMoa020890) · [PubMed 12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/)
