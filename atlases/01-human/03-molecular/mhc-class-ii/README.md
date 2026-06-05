---
schema: human-scale-entry/v1
id: mhc-class-ii
name: MHC Class II
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "Heterodimeric transmembrane glycoprotein (HLA-DR/DQ/DP) on professional APCs. Presents 13–25 aa exogenous peptides to CD4+ T helper cells via TCR–pMHC-II interaction. Central gating molecule for adaptive immune priming."
aliases: ["HLA class II", "MHC-II", "HLA-DR", "HLA-DQ", "HLA-DP"]
sources:
  - id: abbas-immunology-9e
    type: textbook
    cite: "Abbas AK, Lichtman AH, Pillai S. Cellular and Molecular Immunology. 9th ed. Elsevier; 2018."
    url: "https://www.elsevier.com/books/cellular-and-molecular-immunology/abbas/978-0-323-52323-3"
    accessed: "2026-06-04"
  - id: zinkernagel-doherty-1996
    type: peer-reviewed
    cite: "Zinkernagel RM, Doherty PC. The discovery of MHC restriction. Immunol Today. 1997;18(1):14-7."
    doi: "10.1016/S0167-5699(97)80008-4"
    pmid: "9018971"
  - id: roche-furuta-2015-mhcii-antigen
    type: peer-reviewed
    cite: "Roche PA, Furuta K. The ins and outs of MHC class II-mediated antigen processing and presentation. Nat Rev Immunol. 2015;15(4):203-16."
    doi: "10.1038/nri3818"
    pmid: "25720354"
  - id: imgt-hla-database
    type: database
    cite: "Robinson J, et al. IPD-IMGT/HLA Database. Nucleic Acids Res. 2020;48(D1):D948-D955."
    doi: "10.1093/nar/gkz950"
    pmid: "31667505"
    url: "https://www.ebi.ac.uk/ipd/imgt/hla/"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/04-cellular/dendritic-cell
    relation: expressed-by
    note: "Dendritic cells are the prototypic professional APC expressing high surface MHC-II; maturation dramatically upregulates MHC-II density and peptide loading."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "Peptide:MHC-II complexes on APCs engage the CD4+ T cell receptor; this pMHC-II–TCR interaction is obligatory for naive CD4+ T cell activation and differentiation."
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "MHC class II is the molecular interface linking innate antigen processing to adaptive T cell priming — a core component of humoral and cellular immune regulation."
---

# MHC Class II

## Overview

Major histocompatibility complex class II (MHC-II), encoded in humans by the **HLA** loci on chromosome 6p21.3, is the cell-surface glycoprotein that displays short peptide fragments derived from extracellular (exogenous) proteins to CD4+ T helper cells [^roche-furuta-2015-mhcii-antigen]. The discovery that T cells recognize antigen only when presented on self-MHC molecules — MHC restriction, described by Zinkernagel and Doherty in 1974 (Nobel Prize 1996) — defined MHC class II as the gating molecule of the entire adaptive immune response [^zinkernagel-doherty-1996].

In humans, three classical MHC-II isotypes are expressed: **HLA-DR**, **HLA-DQ**, and **HLA-DP**, each encoded by a distinct α/β pair. MHC-II is constitutively expressed on **professional antigen-presenting cells** — dendritic cells, B cells, and macrophages — and can be induced on non-professional APCs (e.g., thymic epithelium, intestinal epithelium, endothelium) by IFN-γ.

The extraordinary polymorphism of MHC-II genes (HLA-DRB1 alone has >2000 known alleles in the IPD-IMGT/HLA database [^imgt-hla-database]) means that different individuals present different peptide repertoires, shaping population-level immune responses to pathogens and vaccines. HLA type is the single most significant genetic determinant of autoimmune disease susceptibility and vaccine response variation.

## Structure

### Molecular architecture

MHC-II is an **αβ heterodimer** — a non-covalent complex of an α-chain (~33 kDa) and a β-chain (~28 kDa), both type I transmembrane glycoproteins. Each chain has two extracellular Ig-like domains, a transmembrane helix, and a short cytoplasmic tail:

| Segment | α-chain | β-chain |
|:---|:---|:---|
| Distal domain | α1 | β1 |
| Proximal domain | α2 | β2 |
| Membrane-proximal | — | β2 contacts CD4 co-receptor |

The **peptide-binding groove** is formed jointly by the α1 and β1 domains. Unlike MHC class I (which is a closed-ended groove accommodating 8–10 aa peptides), the MHC-II groove is **open at both ends**, allowing longer peptides (typically 13–25 aa) to protrude. A central nonameric core (P1–P9) makes the key anchoring contacts; flanking residues contribute to stability and T cell receptor contacts.

### Peptide-binding groove polymorphism

Most of the 500+ hypervariable positions across HLA-DR, DQ, and DP that distinguish alleles are clustered in the β1 (and to a lesser extent α1) domain forming the peptide-binding groove. Allele-specific anchor pockets determine which peptides bind stably — this structural polymorphism is why HLA alleles differentially confer susceptibility to autoimmune diseases (e.g., HLA-DRB1\*04:01 and rheumatoid arthritis; HLA-DQ2/DQ8 and celiac disease) and influence vaccine responsiveness.

### Invariant chain and CLIP

Newly synthesized MHC-II αβ dimers in the endoplasmic reticulum associate with the **invariant chain** (Ii/CD74), which:
1. Prevents premature peptide loading in the ER
2. Targets the MHC-II–Ii complex to endosomes via dileucine motifs in the Ii cytoplasmic tail
3. Is proteolytically degraded in the endosome, leaving only the **CLIP** fragment (class II-associated invariant chain peptide) blocking the groove

Displacement of CLIP by high-affinity antigenic peptides is catalyzed by the non-classical MHC-II molecule **HLA-DM** (in mice, H-2M), which acts as a peptide editor — promoting exchange of CLIP and low-stability peptides for high-stability ones.

## Function

### Antigen processing — the endolysosomal pathway

1. Professional APCs engulf extracellular protein via phagocytosis, macropinocytosis, or receptor-mediated endocytosis (FcR, complement receptors, C-type lectins).
2. The phagosome acidifies and fuses with lysosomes; proteases (cathepsins B, D, L, S, and others) degrade protein to peptides.
3. Newly synthesized MHC-II–Ii complexes are delivered to the endosomal compartment (MIICs — MHC-II-containing compartments, specialized late endosomes).
4. Ii is degraded, leaving CLIP; HLA-DM catalyzes CLIP exchange for the highest-affinity peptide available.
5. Stable pMHC-II complexes traffic to the cell surface where they are displayed for T cell inspection.

### T cell activation — the immunological synapse

When a naïve CD4+ T cell encounters a cognate pMHC-II on a mature dendritic cell [^roche-furuta-2015-mhcii-antigen]:
- The **T cell receptor (TCR)** contacts both the MHC-II α/β helices and the bound peptide (dual recognition)
- **CD4** co-receptor stabilizes the complex by binding the MHC-II β2 domain; CD4 carries Lck, which phosphorylates ITAM motifs in CD3ζ
- Signal 1 (TCR/CD3) + Signal 2 (CD28–CD80/86 co-stimulation) + Signal 3 (cytokines from APC) together activate the naive T cell
- Sustained signaling over hours (the immunological synapse) drives IL-2 production, clonal expansion, and differentiation into appropriate effector subsets

## Mechanism

### Cross-presentation and the distinction from MHC-I

MHC-II is distinguished from MHC class I by pathway and lineage:
- **MHC-I** is expressed on virtually all nucleated cells; it presents intracellular (endogenous) peptides (8–10 aa from proteasomal degradation via TAP) to **CD8+ cytotoxic T cells** — the T cells that kill infected or malignant cells.
- **MHC-II** is restricted to professional APCs; it presents exogenous peptides to **CD4+ T helper cells** — the T cells that orchestrate the rest of the adaptive response.

A specialized pathway — **cross-presentation** — allows dendritic cells to load exogenous antigens onto MHC-I as well, enabling CD8+ priming against viruses that do not directly infect DCs.

### Regulation of MHC-II expression

Surface MHC-II density is tightly regulated:
- **CIITA** (class II transactivator) is the master transcriptional regulator of MHC-II and accessory genes (Ii, HLA-DM). It is induced by IFN-γ (via STAT1–IRF1 axis) and constitutively active in professional APCs.
- During DC maturation (triggered by TLR ligation, innate immune sensors recognizing PAMPs), MHC-II synthesis increases, CLIP exchange accelerates, and surface pMHC-II half-life lengthens — converting an immature scanning cell into a potent APC.
- Viral immune evasion strategies often target MHC-II (e.g., HSV ICP47 blocks TAP; HCMV US2/US3 degrade MHC molecules; SARS-CoV-2 accessory proteins can downregulate MHC-II on infected monocytes).

## Connections

- **Expressed on:** [dendritic-cell](../../04-cellular/dendritic-cell/README.md) — the central professional APC for adaptive priming
- **Modulates:** [t-helper-cell](../../04-cellular/t-helper-cell/README.md) — pMHC-II complex is the essential activating ligand for CD4+ T cells
- **Part of:** [immune-system](../../07-system/immune-system/README.md) — the molecular gateway of adaptive immune surveillance

[^roche-furuta-2015-mhcii-antigen]: Roche PA, Furuta K. The ins and outs of MHC class II-mediated antigen processing and presentation. *Nat Rev Immunol.* 2015;15(4):203-16. [doi:10.1038/nri3818](https://doi.org/10.1038/nri3818) · [PubMed 25720354](https://pubmed.ncbi.nlm.nih.gov/25720354/)
[^zinkernagel-doherty-1996]: Zinkernagel RM, Doherty PC. The discovery of MHC restriction. *Immunol Today.* 1997;18(1):14-7. [doi:10.1016/S0167-5699(97)80008-4](https://doi.org/10.1016/S0167-5699(97)80008-4) · [PubMed 9018971](https://pubmed.ncbi.nlm.nih.gov/9018971/)
[^imgt-hla-database]: Robinson J, et al. IPD-IMGT/HLA Database. *Nucleic Acids Res.* 2020;48(D1):D948-D955. [doi:10.1093/nar/gkz950](https://doi.org/10.1093/nar/gkz950) · [PubMed 31667505](https://pubmed.ncbi.nlm.nih.gov/31667505/)
[^abbas-immunology-9e]: Abbas AK, Lichtman AH, Pillai S. *Cellular and Molecular Immunology.* 9th ed. Elsevier; 2018.
