---
schema: human-scale-entry/v1
id: tbxt
name: TBXT
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "TBXT (brachyury) is a T-box TF specifying notochordal lineage; overexpression/amplification defines chordoma (>95%); tandem TBXT duplication causes familial chordoma; TBXT is a lineage dependency factor; EZH2, FGFR, and mTOR inhibitors are active in TBXT-driven chordoma."
aliases: ["TBXT", "brachyury", "T gene", "T-box transcription factor T", "chordoma brachyury", "notochordal transcription factor", "T gene chordoma", "TBXT amplification", "familial chordoma gene"]
sources:
  - id: yang-2009-tbxt-chordoma
    type: peer-reviewed
    cite: "Yang XR, Ng D, Alcorta DA, et al. T (brachyury) gene duplication confers major susceptibility to familial chordoma. Nat Genet. 2009;41(11):1176-1178."
    doi: "10.1038/ng.454"
    pmid: "19801977"
    url: "https://doi.org/10.1038/ng.454"
  - id: vujovic-2006-brachyury-chordoma
    type: peer-reviewed
    cite: "Vujovic S, Henderson S, Presneau N, et al. Brachyury, a crucial regulator of notochordal development, is a novel biomarker for chordomas. J Pathol. 2006;209(2):157-165."
    doi: "10.1002/path.1969"
    pmid: "16538613"
    url: "https://doi.org/10.1002/path.1969"
cross_links:
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "TBXT activates Wnt target genes (LEF1, AXIN2, MYC) via T-box binding elements; Wnt co-activation amplifies notochordal self-renewal in chordoma; beta-catenin nuclear in ~30% chordomas; dual TBXT + Wnt inhibition shows preclinical synergy in chordoma cell lines."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "TBXT activates mTOR via PI3K/AKT and FGF/FGFR → mTORC1/mTORC2 in chordoma; PTEN loss in ~15-20% chordomas → AKT/mTOR hyperactivation; mTOR inhibitors (rapamycin, everolimus) show modest single-agent activity in chordoma; mTOR + EGFR combination being evaluated."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "FGFR1/2/3 overexpressed in ~50% chordomas; FGFR-driven MAPK/PI3K → tumor growth; erdafitinib (pan-FGFR) active in FGFR-altered chordoma (Phase 2); FGF4/FGF8 autocrine loop driven by TBXT transcription; FGFR inhibitors synergize with mTOR inhibitors in preclinical models."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGFRA/PDGFRB overexpressed in >80% chordomas; imatinib (PDGFR inhibitor) achieves stable disease in ~35-40% (Stacchiotti 2012, Phase 2); PDGF-BB autocrine loop in chordoma cells; erlotinib + imatinib combination achieves partial response in small Phase 2 series."
---

# TBXT

## Overview

**TBXT** (T-box transcription factor T; historically **brachyury**, Latin for "short tail") encodes a 435-amino-acid T-box transcription factor that is the master regulator of **notochordal lineage specification** during vertebrate embryogenesis. TBXT is expressed transiently in the primitive streak, mesoderm, and notochord during gastrulation; its expression is normally silenced in all adult tissues. In **chordoma**, TBXT is persistently overexpressed — in >95% of cases — either through germline tandem duplication of the TBXT locus, somatic amplification, or epigenetic de-repression, creating a dependency on TBXT for tumor survival [^yang-2009-tbxt-chordoma] [^vujovic-2006-brachyury-chordoma].

**TBXT genetic alterations in chordoma:**
- **Tandem germline duplication of TBXT** (6q27): identified in familial chordoma kindreds; heterozygous duplication → increased TBXT dosage → chordoma predisposition; ~2-5x higher copy number than normal diploid; penetrance incomplete (~50-65%)
- **Somatic TBXT amplification**: present in a subset of sporadic chordomas; higher copy number correlates with more aggressive behavior
- **TBXT overexpression without amplification**: most sporadic chordomas; mechanism involves promoter hypomethylation and transcription factor dysregulation
- **Single nucleotide variant (SNV) rs2305089** (G177D in T-box domain): a common TBXT polymorphism associated with sporadic chordoma risk (OR ~3-5 in population studies); does not ablate TBXT function but alters binding affinity
- TBXT mutations (LOF) cause Caudal Regression Syndrome and mesodermal defects in humans (germline heterozygous truncating)

**TBXT IHC — diagnostic utility:** [^vujovic-2006-brachyury-chordoma]
Nuclear brachyury/TBXT IHC (rabbit anti-brachyury, EP17, clone D9F7U) is the gold standard confirmatory test for chordoma: sensitivity ~95%, specificity >99% (among spinal/skull base tumors); positive in notochordal rests; negative in chondrosarcoma, hemangioperictytoma, carcinoma

## Structure

### TBXT protein architecture

**N-terminal domain (aa 1-90):**
Flexible; low-complexity sequences; interacts with CTNNB1 (beta-catenin) and assists nuclear localization; no transcriptional activity on its own; required for homodimerization

**T-box DNA-binding domain (aa 91-255):**
Conserved 200-aa domain; binds palindromic T-box response elements (TBREs: AGGTGTGAAATT) as homodimers or heterodimers with other T-box factors; binds the minor groove of target gene promoters; directly activates mesoderm and notochordal target genes (FGF8, VEGFA, LEFTY1, WNT3A, NODAL)

**C-terminal activation/repression domain (aa 256-435):**
Context-dependent; contains a transactivation domain and a nuclear export sequence; the C-terminal domain recruits BRG1 (SMARCA4) and other BAF complex components → open chromatin at TBXT target loci; also contains interaction surfaces for SOX17 (repression) and beta-catenin (co-activation)

**TBXT target genes in chordoma:**
- **FGF4, FGF8, FGFR2**: FGFR pathway activation → MAPK/PI3K → proliferation
- **WNT3A, LEF1**: Wnt target gene activation → beta-catenin → EMT
- **VEGFA**: angiogenesis (HIF-1α-independent)
- **CDH2 (N-cadherin)**: mesenchymal identity → invasion
- **BRACHYURY itself** (autoregulation): TBXT binds its own promoter → sustains expression in chordoma
- **MMP3, MMP13**: matrix metalloproteinases → extracellular matrix invasion

### T-box family context

The T-box family includes 17 members in humans (TBX1-22, TBXT, EOMES, TBR1); all share the T-box domain but have distinct target genes and expression patterns:
- TBXT: primitive streak, mesoderm, notochord → only T-box factor in notochordal lineage
- TBX5: heart development (Holt-Oram syndrome)
- TBX3: mammary gland (ulnar-mammary syndrome); amplified in melanoma
- TBR1: cortical neuron development
- EOMES (TBX21): trophoblast, NK cells, CD8+ T cells

TBXT uniqueness: it is the only T-box factor expressed in the notochord; no functional redundancy exists for notochordal specification → explains why TBXT knockdown is lethal to chordoma cells (lineage dependency) while sparing other cell types

## Function

### Normal TBXT roles in notochordal development

**Gastrulation and primitive streak:**
TBXT expression is induced at onset of gastrulation by Wnt3a + BMP4 signaling → TBXT activates FGF8 (mesoderm induction), WNT3A (positive feedback), NODAL (endoderm specification), MIXL1 (pan-mesoderm) → loss of TBXT in mice → failure of gastrulation, absence of the notochord and all mesodermal structures posterior to the anterior somites → immediate lethality

**Notochord specification and maintenance:**
TBXT activates SOX9 (chondrocyte fate), COL2A1 (collagen type II), AGC1 (aggrecan) → nucleus pulposus (intervertebral disc) identity in postnatal notochordal remnants; TBXT expression normally silenced in nucleus pulposus cells postnatally via DNA methylation at the TBXT promoter → notochordal cell maturation

**Epithelial-to-mesenchymal transition (EMT):**
TBXT directly represses E-cadherin (CDH1) and activates N-cadherin (CDH2), fibronectin (FN1) → mesenchymal transition; this EMT-inducing function is relevant to chordoma invasion

### TBXT as a "lineage dependency" transcription factor

Chordoma arises from notochordal remnants or ectopic notochordal cells; these cells retain TBXT expression, which was never silenced during development. This creates a **lineage dependency**: chordoma cells require persistent TBXT activity for:
1. **Survival**: TBXT promotes BCL-2 and MCL-1 → anti-apoptotic; TBXT knockdown → rapid apoptosis
2. **Identity**: TBXT maintains notochordal cell morphology (physaliferous = vacuolated); loss → loss of chondroid features
3. **Proliferation**: TBXT drives CDK4/6 and cyclin D1 → G1 progression; TBXT knockdown → G1 arrest

This lineage dependency makes TBXT an attractive therapeutic target — but direct TBXT inhibition has proven difficult (no enzymatic pocket; transcription factor targeting is technically challenging).

## Mechanism

### Therapeutic strategies in TBXT-driven chordoma

**mTOR inhibitors:**
Rationale: TBXT → FGF/FGFR → PI3K/AKT → mTOR; also PTEN loss (~15-20% chordomas) directly activates AKT/mTOR; rapamycin (sirolimus) and everolimus show preclinical activity; Phase 2 clinical data: everolimus achieves stable disease in ~50% but rare objective responses; combination strategies (everolimus + lapatinib, everolimus + imatinib) explored

**FGFR inhibitors:**
TBXT directly transcribes FGF4/FGF8 → autocrine FGF/FGFR loop → MAPK/PI3K; erdafitinib (pan-FGFR inhibitor) in Phase 2 chordoma trial; BGJ398 (infigratinib) also studied; FGFR2 amplification in sacral chordoma subsets may predict response; FGFR + mTOR combination: synergistic in chordoma cell lines (dual MAPK + PI3K blockade)

**PDGFR/imatinib:**
Imatinib (PDGFR/KIT/ABL inhibitor): Phase 2 study (Stacchiotti 2012, N=50): median PFS 9 months; stable disease in ~35-40%; low objective response rate; PDGFRA/B expression by IHC predicts imatinib response in chordoma; imatinib + everolimus: tolerable but not superior to single agents in randomized Phase 2

**Targeted protein degradation (PROTACs — investigational):**
T-box domain of TBXT lacks druggable enzymatic pocket → direct small-molecule inhibition difficult; TBXT-targeted PROTACs (proteolysis-targeting chimeras) in early development; alternatively, upstream regulators (BRD4, CDK7, CDK9 → TBXT transcription) are targeted preclinically; JQ1 (BET inhibitor) suppresses TBXT transcription in chordoma cells by evicting BRD4 from the TBXT super-enhancer

**Proton beam radiation:**
High-dose radiation (74-78 Gy in 2 Gy equivalents) in combination with surgery remains the cornerstone of local control; proton beam delivers sharp Bragg-peak dose at tumor while minimizing dose to adjacent critical structures (brainstem, optic chiasm, spinal cord); carbon ion radiotherapy also used in sacral chordoma (Japan, Germany); local control at 5 years: skull base ~60-70%, sacral ~50-60%

## Connections

- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — TBXT activates Wnt target genes (LEF1, AXIN2, MYC) via T-box binding elements; Wnt co-activation amplifies notochordal self-renewal in chordoma; beta-catenin nuclear in ~30% chordomas; dual TBXT + Wnt inhibition shows preclinical synergy in chordoma cell lines.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — TBXT activates mTOR via PI3K/AKT and FGF/FGFR → mTORC1/mTORC2 in chordoma; PTEN loss in ~15-20% chordomas → AKT/mTOR hyperactivation; mTOR inhibitors (rapamycin, everolimus) show modest single-agent activity in chordoma; mTOR + EGFR combination being evaluated.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGFR1/2/3 overexpressed in ~50% chordomas; FGFR-driven MAPK/PI3K → tumor growth; erdafitinib (pan-FGFR) active in FGFR-altered chordoma (Phase 2); FGF4/FGF8 autocrine loop driven by TBXT transcription; FGFR inhibitors synergize with mTOR inhibitors in preclinical models.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGFRA/PDGFRB overexpressed in >80% chordomas; imatinib (PDGFR inhibitor) achieves stable disease in ~35-40% (Stacchiotti 2012, Phase 2); PDGF-BB autocrine loop in chordoma cells; erlotinib + imatinib combination achieves partial response in small Phase 2 series.

[^yang-2009-tbxt-chordoma]: Yang XR, Ng D, Alcorta DA, et al. T (brachyury) gene duplication confers major susceptibility to familial chordoma. *Nat Genet.* 2009;41(11):1176-1178. [doi:10.1038/ng.454](https://doi.org/10.1038/ng.454) · [PubMed 19801977](https://pubmed.ncbi.nlm.nih.gov/19801977/)
[^vujovic-2006-brachyury-chordoma]: Vujovic S, Henderson S, Presneau N, et al. Brachyury, a crucial regulator of notochordal development, is a novel biomarker for chordomas. *J Pathol.* 2006;209(2):157-165. [doi:10.1002/path.1969](https://doi.org/10.1002/path.1969) · [PubMed 16538613](https://pubmed.ncbi.nlm.nih.gov/16538613/)
