---
schema: human-scale-entry/v1
id: myd88
name: MYD88
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "MYD88 is the universal TLR/IL-1R adaptor protein that activates NF-κB and JAK-STAT3 via IRAK4-TRAF6; MYD88 L265P gain-of-function mutation in ~90% of Waldenström macroglobulinemia and ~25% of ABC-DLBCL drives constitutive NF-κB; ibrutinib highly active in MYD88 L265P WM."
aliases: ["MYD88", "myeloid differentiation primary response 88", "MYD88 L265P", "toll-like receptor adaptor", "IRAK4", "myddosome", "TLR signaling adaptor"]
sources:
  - id: treon-2012-myd88
    type: peer-reviewed
    cite: "Treon SP, Xu L, Yang G, et al. MYD88 L265P somatic mutation in Waldenström's macroglobulinemia. N Engl J Med. 2012;367(9):826-833."
    doi: "10.1056/NEJMoa1200710"
    pmid: "22931316"
    url: "https://doi.org/10.1056/NEJMoa1200710"
  - id: kawai-2010-tlr-review
    type: peer-reviewed
    cite: "Kawai T, Akira S. The role of pattern-recognition receptors in innate immunity: update on Toll-like receptors. Nat Immunol. 2010;11(5):373-384."
    doi: "10.1038/ni.1863"
    pmid: "20404851"
    url: "https://doi.org/10.1038/ni.1863"
cross_links:
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "MYD88 DD domain recruits IRAK4-IRAK1 (myddosome) → TRAF6 → IKK → IκBα degradation → NF-κB nuclear translocation → BCL-2, IRF4, MYC → B-cell survival; MYD88 L265P constitutively forms myddosome without TLR ligand → autonomous NF-κB in WM and ABC-DLBCL."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "MYD88 L265P → IRAK1 directly phosphorylates and activates JAK1 → STAT3 phosphorylation → BCL-XL and MYC → survival in WM; this non-canonical MYD88-JAK1-STAT3 axis is distinct from cytokine receptor-JAK2 signaling; combined BTK+JAK inhibition studied in WM."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "MYD88/NF-κB transcriptionally activates BCL-2, BCL-XL → apoptosis resistance in WM and ABC-DLBCL; venetoclax (BCL-2 inhibitor) shows modest single-agent activity in WM; combined ibrutinib+venetoclax studied in R/R WM; BCL-2 protein expression is high in most WM cases."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "MYD88 L265P → IRAK1 → JAK1 → STAT3 Tyr705 phosphorylation → BCL-XL, MYC, SOCS3 → autonomous B-cell survival in WM; STAT3 inhibition attenuates MYD88 L265P-driven growth in WM cell lines; STAT3 pathway activation also downstream of CD40L and BAFF in WM microenvironment."
---

# MYD88

## Overview

**MYD88 (Myeloid Differentiation Primary Response Protein 88)** is the canonical adaptor protein shared by nearly all Toll-like receptors (TLRs 1-9, except TLR3) and all members of the IL-1 receptor (IL-1R) superfamily. MYD88 couples receptor activation to downstream innate immune signaling: upon ligand-induced receptor activation, MYD88 recruits IRAK4 and IRAK1 into a supramolecular complex called the **myddosome** via homotypic Death Domain (DD) interactions → IRAK4 auto-phosphorylation → IRAK1 trans-phosphorylation → TRAF6 ubiquitin ligase activation → TAK1 → IKK complex → IκBα degradation → **NF-κB nuclear translocation** → expression of cytokines (TNF-α, IL-1β, IL-6, IL-12) and co-stimulatory molecules. The discovery of **MYD88 L265P** (Leu265Pro in the TIR domain) in Waldenström macroglobulinemia (2012) revealed that gain-of-function MYD88 mutations drive autonomous NF-κB signaling in B-cell malignancies without TLR engagement, creating a druggable dependency on BTK (which is activated downstream of BCR-NF-κB cross-talk in B-cells) [^treon-2012-myd88].

**MYD88 L265P in B-cell malignancies:**
- **Waldenström macroglobulinemia (WM/LPL):** MYD88 L265P ~90%; near-universal; high predictive value for ibrutinib response; basis for routine MYD88 mutation testing in LPL
- **ABC-DLBCL (activated B-cell like DLBCL):** MYD88 L265P ~25%; co-mutation with CD79A/B (BCR signaling) → poor prognosis subtype; MYD88/CD79B double mutant (DLBCL subtype) → BTK inhibition active (ibrutinib + lenalidomide + rituximab, PHOENIX trial)
- **Marginal zone lymphoma (MZL):** MYD88 L265P ~10-15%; especially splenic and nodal MZL; predicts BTK inhibitor activity
- **Primary CNS lymphoma (PCNSL):** MYD88 L265P ~70%; high frequency in immune-privileged site lymphomas; BTK inhibitors (ibrutinib, zanubrutinib) show high CNS penetration and activity in PCNSL

**Wild-type MYD88 in immunity:**
MYD88 is required for innate immune responses to bacterial LPS (TLR4), flagellin (TLR5), CpG DNA (TLR9), single-stranded RNA (TLR7/8), and lipoteichoic acid (TLR2); MyD88-deficient mice are highly susceptible to infection; MYD88 germline mutations cause primary immunodeficiency (MYD88 deficiency — severe pyogenic bacterial infections in childhood).

## Structure

### MYD88 protein architecture

MYD88 is a 296-amino-acid, 33 kDa adaptor with three functional domains:

**Death Domain (DD, 1-108):**
- Homotypic DD-DD interactions → recruits IRAK4 (via DD), then IRAK1/2 (via DD) → myddosome assembly
- L265P mutation (Leu265Pro) is in the TIR domain (below); not the DD — but DD interactions are required for L265P to constitutively signal
- MyD88 DD-IRAK4 DD interaction: first step in myddosome; DD-only fragments can serve as dominant negatives in TLR research

**Intermediate domain (ID, 109-155):**
- Connects DD to TIR domain; structurally flexible; required for signal relay but not primary protein-protein interactions

**TIR domain (Toll/IL-1R homology, 156-296):**
- ~150 aa conserved domain; present in all TLRs, IL-1Rs, and TIR-domain adaptors (TRIF, TIRAP, TICAM)
- TIR-TIR homotypic interactions → receptor:adaptor coupling (MYD88 TIR binds TLR cytoplasmic TIR domains)
- BB loop (central TIR motif): Contains the critical signaling residue
- **L265P:** Leu265 is in the BB loop of the TIR domain → Pro substitution creates structural rigidity → constitutive myddosome assembly without receptor engagement → chronic NF-κB signaling → B-cell lymphomagenesis

### Myddosome assembly and NF-κB activation

**Normal (TLR-stimulated) myddosome:**
TLR agonist → TLR TIR dimerization → MYD88 TIR-TIR homotypic interaction → MYD88 DD recruits IRAK4 DD → IRAK4 recruits IRAK1 DD + IRAK2 DD → helical myddosome tower (6-8 molecules) → IRAK4 auto-phosphorylation (Thr342, Thr345) → IRAK1 Thr387/Thr391 phosphorylation → IRAK1 Lys63-polyubiquitination (via Pellino E3 ligases) → TRAF6 K63 polyubiquitin chain → TAK1/TAB1/TAB2 → IKKβ → IκBα Ser32/Ser36 phosphorylation → β-TrCP → IκBα proteasomal degradation → NF-κB (p65/p50) nuclear translocation → cytokine gene transcription.

**L265P constitutive myddosome:**
Pro265 rigidifies BB loop → MYD88 TIR adopts conformation that mimics receptor-engaged state → spontaneous myddosome assembly in absence of TLR ligand → constitutive IRAK4/IRAK1 → NF-κB → BCL-2, IRF4, CXCR4, MYC → B-cell survival and growth. In B-cells, L265P MYD88 also activates BTK (downstream of BCR signaling → PI3K → AKT → NF-κB) via IRAK1 → BTK Tyr551 phosphorylation (non-canonical BTK activation independent of BCR).

### MYD88 L265P detection

**Clinical testing:**
- Bone marrow aspirate or lymph node biopsy: Allele-specific PCR (AS-PCR) or NGS
- Peripheral blood: Cell-free DNA (cfDNA) testing in WM if BM biopsy not feasible
- Sensitivity requirement: >1-5% variant allele frequency for reliable detection; AS-PCR: sensitivity ~0.01%
- MYD88 L265P testing recommended at WM diagnosis to guide BTK inhibitor use and CXCR4 mutation co-testing

## Function

### TLR signaling in innate immunity

**Pattern recognition:**
TLRs detect conserved pathogen-associated molecular patterns (PAMPs): LPS (TLR4), flagellin (TLR5), dsRNA (TLR3-TRIF pathway, MYD88-independent), ssRNA (TLR7/8), CpG DNA (TLR9), lipoteichoic acid (TLR2). All TLRs except TLR3 signal via MYD88.

**Cell type-specific outcomes:**
- Macrophages: MYD88 → NF-κB → TNF-α, IL-1β, IL-6, IL-12 → inflammation
- Dendritic cells: MYD88 → IRF7 (via IRAK4 → IKKα) → type I IFN (in plasmacytoid DCs) and cytokine production
- B-cells: TLR7/9 → MYD88 → NF-κB → BCR co-stimulation → T-independent antibody responses; chronic TLR-MYD88 stimulation → risk of B-cell lymphoma (particularly splenic MZL, LPL)

### Non-canonical MYD88-JAK1-STAT3 in WM

In WM cells carrying MYD88 L265P, IRAK1 directly binds and phosphorylates JAK1 (via IRAK1 kinase domain → JAK1 Tyr1022/1023) → STAT3 Tyr705 phosphorylation → STAT3 target genes (BCL-XL, MYC, PIM2). This MYD88-IRAK1-JAK1-STAT3 axis operates independently of cytokine receptors and is a parallel survival pathway alongside NF-κB; inhibiting both NF-κB (via BTK inhibition) and STAT3 (via JAK inhibition) → synergistic killing of MYD88 L265P WM cells.

## Mechanism

### BTK inhibition in MYD88 L265P malignancies

**Ibrutinib (imbruvica, BTK inhibitor) in WM:**
Ibrutinib covalently inhibits BTK Cys481 → blocks BCR-NF-κB and MYD88-BTK (non-canonical) → profound clinical activity in MYD88 L265P WM (ORR >90% in IGHV3-23 rearranged, MYD88 L265P cases); response varies by CXCR4 mutation status: MYD88 L265P/CXCR4 WT → ibrutinib ORR ~100%; MYD88 L265P/CXCR4 mutant → ibrutinib ORR ~60%; MYD88 WT/CXCR4 mutant → ibrutinib ORR ~25%.

**CXCR4 mutation as ibrutinib resistance mechanism:**
CXCR4 WHIM mutations (gain-of-function) → enhanced CXCR4-CXCL12 signaling → AKT-ERK activation → cell survival independent of BTK; CXCL12-rich BM microenvironment drives CXCR4-mediated ibrutinib resistance → zanubrutinib may have modest advantage.

**Zanubrutinib vs. ibrutinib (ASPEN trial):**
Randomized; CXCR4 WT and mutant WM; zanubrutinib showed higher VGPR/CR rate (28% vs. 19% at 19 months) and similar ORR; fewer cardiac toxicities (atrial fibrillation ~2% vs. ~15% ibrutinib); FDA approved 2021 for WM.

**MYD88 L265P in DLBCL (R-CHOP-E + ibrutinib):**
PHOENIX trial (ibrutinib + R-CHOP vs. R-CHOP): Overall trial negative but OS benefit in patients ≤60 years with ABC-DLBCL; MYD88 L265P/CD79B double-mutant DLBCL → best ibrutinib response; btk inhibitor combinations ongoing for non-GCB DLBCL.

## Connections

- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — MYD88 DD domain recruits IRAK4-IRAK1 (myddosome) → TRAF6 → IKK → IκBα degradation → NF-κB nuclear translocation → BCL-2, IRF4, MYC → B-cell survival; MYD88 L265P constitutively forms myddosome without TLR ligand → autonomous NF-κB in WM and ABC-DLBCL.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — MYD88 L265P → IRAK1 directly phosphorylates and activates JAK1 → STAT3 phosphorylation → BCL-XL and MYC → survival in WM; this non-canonical MYD88-JAK1-STAT3 axis is distinct from cytokine receptor-JAK2 signaling; combined BTK+JAK inhibition studied in WM.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — MYD88/NF-κB transcriptionally activates BCL-2, BCL-XL → apoptosis resistance in WM and ABC-DLBCL; venetoclax (BCL-2 inhibitor) shows modest single-agent activity in WM; combined ibrutinib+venetoclax studied in R/R WM; BCL-2 protein expression is high in most WM cases.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — MYD88 L265P → IRAK1 → JAK1 → STAT3 Tyr705 phosphorylation → BCL-XL, MYC, SOCS3 → autonomous B-cell survival in WM; STAT3 inhibition attenuates MYD88 L265P-driven growth in WM cell lines; STAT3 pathway activation also downstream of CD40L and BAFF in WM microenvironment.

[^treon-2012-myd88]: Treon SP, Xu L, Yang G, et al. MYD88 L265P somatic mutation in Waldenström's macroglobulinemia. *N Engl J Med.* 2012;367(9):826-833. [doi:10.1056/NEJMoa1200710](https://doi.org/10.1056/NEJMoa1200710) · [PubMed 22931316](https://pubmed.ncbi.nlm.nih.gov/22931316/)
[^kawai-2010-tlr-review]: Kawai T, Akira S. The role of pattern-recognition receptors in innate immunity: update on Toll-like receptors. *Nat Immunol.* 2010;11(5):373-384. [doi:10.1038/ni.1863](https://doi.org/10.1038/ni.1863) · [PubMed 20404851](https://pubmed.ncbi.nlm.nih.gov/20404851/)
