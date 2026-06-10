---
schema: human-scale-entry/v1
id: ezh2
name: EZH2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "EZH2 is the catalytic subunit of PRC2, trimethylating H3K27 → gene silencing; EZH2 Y641 gain-of-function mutation in ~25% of follicular lymphoma and ~10% of DLBCL silences tumor suppressors including CDKN2A; tazemetostat (EZH2 inhibitor) is FDA-approved for EZH2-mutant FL."
aliases: ["EZH2", "enhancer of zeste homolog 2", "PRC2", "Polycomb repressive complex 2", "H3K27me3", "tazemetostat", "EZH2 Y641", "EZH2 inhibitor", "histone methyltransferase"]
sources:
  - id: margueron-2011-prc2
    type: peer-reviewed
    cite: "Margueron R, Reinberg D. The Polycomb complex PRC2 and its mark in life. Nature. 2011;469(7330):343-349."
    doi: "10.1038/nature09784"
    pmid: "21248841"
    url: "https://doi.org/10.1038/nature09784"
  - id: morschhauser-2020-tazemetostat
    type: peer-reviewed
    cite: "Morschhauser F, Tilly H, Chaidos A, et al. Tazemetostat for patients with relapsed or refractory follicular lymphoma (E7438-G-003): a multicentre, open-label, single-arm, phase 2 trial. Lancet Oncol. 2020;21(11):1433-1442."
    doi: "10.1016/S1470-2045(20)30441-1"
    pmid: "33035457"
    url: "https://doi.org/10.1016/S1470-2045(20)30441-1"
cross_links:
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "t(14;18) BCL-2-IGH in germinal center B-cells → BCL-2 overexpression → apoptosis resistance; EZH2 Y641 cooperates with BCL-2 overexpression by silencing CDKN2A (p16/ARF) → removes senescence checkpoint; venetoclax is active in BCL-2-high follicular lymphoma."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC activates EZH2 transcription; EZH2 → H3K27me3 at CDKN2A and HOXA loci → silences tumor suppressors enabling MYC-driven proliferation; double-expressor DLBCL (MYC+BCL-2 protein) frequently co-expresses EZH2; double-hit lymphoma has high EZH2 activity."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "EZH2 silences TNFAIP3/A20 and PRDM1 (BLIMP1) via H3K27me3 → enhanced NF-κB and blocked plasma cell differentiation in GCB-DLBCL and FL; CREBBP/EP300 HAT mutations co-occur with EZH2 mutations in ~30% of FL → dual epigenetic reprogramming toward GC B-cell maintenance."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "EZH2 silences CDKN2A (p14/ARF) via H3K27me3 → ARF loss → MDM2-mediated p53 degradation without TP53 mutation; EZH2 → blunted p53-pathway response in FL; tazemetostat restores CDKN2A expression → p53 reactivation in EZH2-mutant cells."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "EZH2 Y641 gain-of-function in ~25% of follicular lymphoma cooperates with BCL-2 overexpression to silence CDKN2A and differentiation regulators; tazemetostat ORR 69% in EZH2-mutant FL vs. 35% in WT FL; FL transformation to DLBCL is accelerated by EZH2+CREBBP co-mutations."
  - target: 01-human/03-molecular/ewsr1
    relation: connects-to
    note: "EWSR1-FLI1 recruits PRC2/EZH2 to repress differentiation loci (ID2, IGJ) in Ewing sarcoma; tazemetostat (EZH2 inhibitor) restores differentiation and has anti-tumor activity in Ewing preclinically; EZH2 co-inhibition is evaluated in refractory Ewing sarcoma."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "EZH2 → H3K27me3 at CDKN2A silences p16 (CDK4/6 inhibitor) and ARF (MDM2 inhibitor); CDKN2A silencing links EZH2 gain-of-function to cell cycle dysregulation and p53 blunting in follicular lymphoma; tazemetostat restores CDKN2A → synthetic lethality in EZH2-mutant cells."
---

# EZH2

## Overview

**EZH2 (Enhancer of Zeste Homolog 2)** is the catalytic histone methyltransferase subunit of **Polycomb Repressive Complex 2 (PRC2)**, which writes the repressive histone mark H3K27me3 (trimethylation of histone H3 lysine 27). PRC2 — composed of EZH2, EED, SUZ12, and RBBP4/7 — establishes and maintains transcriptional silencing of developmental regulators (HOXA/HOXB clusters), tumor suppressors (CDKN2A, PTEN, MLH1), and lineage-specifying genes that must be silenced for self-renewal and differentiation. In cancer, EZH2 is both a gain-of-function oncogene (recurrent activating point mutations in lymphoma) and a gene amplified/overexpressed without mutation in solid tumors. The **EZH2 Y641** hotspot mutation (seen in ~25% of follicular lymphoma and ~10% of GCB-DLBCL) alters the substrate specificity of EZH2 toward H3K27me3 production, globally silencing tumor suppressor programs in germinal center B-cells. **Tazemetostat (Tazverik)**, an allosteric EZH2 inhibitor, is FDA-approved for EZH2-mutant relapsed/refractory follicular lymphoma and for epithelioid sarcoma (EZH2/SMARCB1 loss) [^morschhauser-2020-tazemetostat].

**EZH2 in cancer:**
- **Follicular lymphoma (FL):** EZH2 Y641 gain-of-function ~25%; cooperates with t(14;18) BCL-2 overexpression; tazemetostat ORR 69% in EZH2-mutant FL vs. 35% in EZH2 WT FL
- **GCB-DLBCL:** EZH2 Y641 ~10%; additional gain-of-function mutations at A677, A687
- **DLBCL transformation from FL:** EZH2 co-mutation with CREBBP/EP300; increased silencing of differentiation regulators
- **Solid tumors (overexpression, not mutation):** Breast (~25%), prostate, bladder, gastric — EZH2 amplification or elevated expression; correlation with aggressive phenotype
- **Epithelioid sarcoma:** Loss of SMARCB1 (INI1, a SWI/SNF subunit) → PRC2 activity unopposed → H3K27me3 accumulation → tumor suppressor silencing; tazemetostat FDA approved for SMARCB1-deficient epithelioid sarcoma regardless of EZH2 mutation
- **MPN (loss-of-function):** EZH2 mutation in ~5-10% of MF as poor prognosis co-mutation; EZH2 loss → reduced H3K27me3 → derepression of inflammatory genes

## Structure

### PRC2 complex architecture

**PRC2 core complex:**
- **EZH2:** SET domain (aa 613-727) carries histone methyltransferase activity; requires allosteric activation by EED and SUZ12; 860 amino acids; PRC2 SET domain = su(var)3-9, Enhancer-of-zeste, Trithorax domain (canonical Class V HMT domain)
- **EED:** WD40 repeat β-propeller; binds H3K27me3 → allosterically stimulates EZH2 catalytic activity → H3K27me3 propagation (positive feedback loop)
- **SUZ12:** Coiled-coil + VEFS domain; structural scaffold; essential for PRC2 stability and activity
- **RBBP4/RBBP7 (RbAp46/48):** WD40 repeat proteins; bind histone H4 tail → nucleosome binding

**PRC2 accessory subunits (context-specific):**
- JARID2: Facilitates PRC2 recruitment to unmodified chromatin; stimulates EZH2 activity ~2-fold
- AEBP2: Binds DNA and chromatin; stimulates PRC2 ~2-fold; preferred in tissues
- PCL1/PCL2/PCL3 (Polycomb-like): Tudor domain + PHD finger → recognize H3K36me3-free nucleosomes (marking transcriptionally silent genes); guide PRC2 to CGI promoters

**EZH2 catalytic mechanism:**
S-adenosylmethionine (SAM) → methyl donor; EZH2 SET domain binds H3K27 peptide + SAM → transfer of methyl group to ε-amino of K27 → H3K27me1 → H3K27me2 (via EZH2 or EZH1) → H3K27me3 (EZH2 preferentially); H3K27me3 → recruits Polycomb Repressive Complex 1 (PRC1) via CBX subunit chromodomain → H2AK119 ubiquitination → compaction → gene silencing.

**EZH2 gain-of-function mutations:**
- **Y641F/N/S/C/H** (Tyr641 in SET domain): Most common; Y641 mutations reduce catalytic activity for H3K27me0 → me1 (monomethylation) but paradoxically increase affinity for H3K27me2 → H3K27me3 (trimethylation); in lymphoma, WT EZH2 converts me0→me2, and mutant EZH2 converts me2→me3 → global H3K27me3 accumulation (complementary activity)
- **A677G/V:** Increases catalytic rate for H3K27me3 directly; phenotypically similar to Y641 mutations
- **A687V:** Less common; similar gain-of-function toward trimethylation

### EZH2 inhibitor mechanism

**Tazemetostat (Tazverik — Epizyme/Ipsen):**
S-adenosylmethionine (SAM)-competitive inhibitor of EZH2 SET domain; binds allosteric pocket between EZH2 and EED → blocks SAM access → no methyl transfer → global reduction in H3K27me3 → reactivation of silenced tumor suppressors (CDKN2A, PTEN) and differentiation genes. Highly selective for EZH2 over EZH1; IC50: EZH2 WT ~11 nM; EZH2 Y641 ~2.5 nM (more potent vs. mutant EZH2).

## Function

### Normal PRC2 roles

**Developmental gene silencing:**
PRC2 silences HOXA/HOXB clusters and other developmental regulators in lineage-committed cells — preventing inappropriate expression of anterior body patterning genes in differentiated tissues. PRC2 maintains embryonic stem cell pluripotency by silencing differentiation genes; EZH2 knockout → early embryonic lethality (gastrulation failure).

**Germinal center (GC) B-cell program:**
PRC2 silences PRDM1 (BLIMP1) → prevents premature plasma cell differentiation in GC B-cells; EZH2 expression peaks in GC B-cells during somatic hypermutation; EZH2 maintains GC B-cell identity while antibody affinity maturation occurs. EZH2 Y641 mutation extends and amplifies this GC B-cell program → pathologic GC B-cell self-renewal → FL/DLBCL.

**H3K27me3 as repressive mark:**
H3K27me3 recruits PRC1 (CBX, RING1A/B, BMI1) → H2AK119 ubiquitination → chromatin compaction → gene silencing; opposing mark is H3K27ac (acetylation) catalyzed by CBP/p300 (CREBBP/EP300) → active enhancers/promoters; balance between EZH2 (H3K27me3) and CBP/p300 (H3K27ac) determines gene expression state — frequently deregulated in lymphoma (EZH2 gain-of-function + CREBBP loss-of-function).

### EZH2 in tumor suppressor silencing

**CDKN2A (p16/ARF) silencing:**
EZH2 → H3K27me3 at CDKN2A locus → p16 (cyclin D1/CDK4 inhibitor) and p14/ARF (MDM2 inhibitor) transcriptional silencing → unchecked CDK4/6-RB axis + reduced p53 activity in BCL-2-overexpressing GC B-cells → FL transformation.

**PTEN silencing:**
EZH2 → H3K27me3 at PTEN promoter in solid tumors → PI3K-AKT pathway activation (cooperates with PIK3CA mutations in breast/prostate cancer).

**Immune evasion:**
EZH2 silences type I interferon response genes, antigen presentation (HLA-A, -B, -C, β2M) in tumor cells → reduced immunogenicity → immune evasion; tazemetostat → restores IFN-pathway gene expression → re-sensitization to PD-1 blockade.

## Mechanism

### Tazemetostat clinical activity

**E7438-G-003 trial (follicular lymphoma):** [^morschhauser-2020-tazemetostat]
- Phase 2, open-label; tazemetostat 800 mg BID; 2 cohorts: EZH2 mutation-positive (Y641/A677/A687) and EZH2 WT
- EZH2-mutant FL: ORR 69% (CR 12%); median DOR 10.9 months
- EZH2 WT FL: ORR 35%; median DOR 13 months
- Well-tolerated; common toxicities: nausea, asthenia, diarrhea; no significant hematologic toxicity
- FDA approved January 2020 for relapsed/refractory FL with EZH2 gain-of-function mutation after ≥2 prior therapies; also approved (regardless of EZH2 mutation status) for FL with no satisfactory alternative treatment options

**Epithelioid sarcoma (SMARCB1-deficient):**
- SMARCB1 (INI1) is a SWI/SNF subunit that normally competes with PRC2 for nucleosome access; SMARCB1 loss → unopposed PRC2/EZH2 activity → global H3K27me3 → deep silencing of tumor suppressors; tazemetostat approved for SMARCB1-deficient epithelioid sarcoma (FDA 2020); ORR ~15% but durable responses

**Combinations under investigation:**
- Tazemetostat + R-CHOP/R-bendamustine: Phase 1b/2 in FL; tazemetostat + rituximab (SYMPHONY-1 trial)
- EZH2 inhibitor + PD-1 blockade: Rationale — EZH2 → epigenetic immune evasion → tazemetostat restores IFN/HLA expression → synergistic with anti-PD-1
- EZH2 inhibitor + CDK4/6 inhibitor: EZH2 silences CDKN2A → CDK4/6 active → combined EZH2+CDK4/6 inhibition → synthetic lethality in CDKN2A-null tumors

### EZH2 vs. EZH1 redundancy

EZH1 is a catalytically less active EZH2 paralog; EZH1-containing PRC2 maintains H3K27me3 at a subset of loci when EZH2 is inhibited (acquired resistance). PRC2/EZH1 → residual H3K27me3 → partial resistance to EZH2-selective inhibitors. Dual EZH1/EZH2 inhibitors (valemetostat) under development for hematologic malignancies (approved in Japan for adult T-cell leukemia/lymphoma).

## Connections

- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — t(14;18) BCL-2-IGH in germinal center B-cells → BCL-2 overexpression → apoptosis resistance; EZH2 Y641 cooperates with BCL-2 overexpression by silencing CDKN2A (p16/ARF) → removes senescence checkpoint; venetoclax is active in BCL-2-high follicular lymphoma.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC activates EZH2 transcription; EZH2 → H3K27me3 at CDKN2A and HOXA loci → silences tumor suppressors enabling MYC-driven proliferation; double-expressor DLBCL (MYC+BCL-2 protein) frequently co-expresses EZH2; double-hit lymphoma has high EZH2 activity.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — EZH2 silences TNFAIP3/A20 and PRDM1 (BLIMP1) via H3K27me3 → enhanced NF-κB and blocked plasma cell differentiation in GCB-DLBCL and FL; CREBBP/EP300 HAT mutations co-occur with EZH2 mutations in ~30% of FL → dual epigenetic reprogramming toward GC B-cell maintenance.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — EZH2 silences CDKN2A (p14/ARF) via H3K27me3 → ARF loss → MDM2-mediated p53 degradation without TP53 mutation; EZH2 → blunted p53-pathway response in FL; tazemetostat restores CDKN2A expression → p53 reactivation in EZH2-mutant cells.
- `connects-to` → **[Follicular Lymphoma](../../07-system/follicular-lymphoma/README.md)** — EZH2 Y641 gain-of-function in ~25% of follicular lymphoma cooperates with BCL-2 overexpression to silence CDKN2A and differentiation regulators; tazemetostat ORR 69% in EZH2-mutant FL vs. 35% in WT FL; FL transformation to DLBCL is accelerated by EZH2+CREBBP co-mutations.
- `connects-to` → **[EWSR1](../../03-molecular/ewsr1/README.md)** — EWSR1-FLI1 recruits PRC2/EZH2 to repress differentiation loci (ID2, IGJ) in Ewing sarcoma; tazemetostat (EZH2 inhibitor) restores differentiation and has anti-tumor activity in Ewing preclinically; EZH2 co-inhibition is evaluated in refractory Ewing sarcoma.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — EZH2 → H3K27me3 at CDKN2A silences p16 (CDK4/6 inhibitor) and ARF (MDM2 inhibitor); CDKN2A silencing links EZH2 gain-of-function to cell cycle dysregulation and p53 blunting in follicular lymphoma; tazemetostat restores CDKN2A → synthetic lethality in EZH2-mutant cells.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^margueron-2011-prc2]: Margueron R, Reinberg D. The Polycomb complex PRC2 and its mark in life. *Nature.* 2011;469(7330):343-349. [doi:10.1038/nature09784](https://doi.org/10.1038/nature09784) · [PubMed 21248841](https://pubmed.ncbi.nlm.nih.gov/21248841/)
[^morschhauser-2020-tazemetostat]: Morschhauser F, Tilly H, Chaidos A, et al. Tazemetostat for patients with relapsed or refractory follicular lymphoma (E7438-G-003). *Lancet Oncol.* 2020;21(11):1433-1442. [doi:10.1016/S1470-2045(20)30441-1](https://doi.org/10.1016/S1470-2045(20)30441-1) · [PubMed 33035457](https://pubmed.ncbi.nlm.nih.gov/33035457/)
