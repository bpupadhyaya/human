---
schema: human-scale-entry/v1
id: t-helper-cell
name: T Helper Cell
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-04
summary: "CD4+ T lymphocyte that orchestrates adaptive immunity. Activated by pMHC-II on dendritic cells, differentiates into Th1/Th2/Th17/Tfh/Treg subsets. Tfh cells drive germinal center reactions and durable antibody production."
aliases: ["CD4+ T cell", "CD4 T lymphocyte", "T helper lymphocyte", "Tfh cell", "Th1 cell", "Th2 cell", "Th17 cell"]
sources:
  - id: zhu-paul-2010-th-differentiation
    type: peer-reviewed
    cite: "Zhu J, Paul WE. Heterogeneity and plasticity of T helper cells. Cell Res. 2010;20(1):4-12."
    doi: "10.1038/cr.2009.138"
    pmid: "20010916"
  - id: crotty-2011-tfh
    type: peer-reviewed
    cite: "Crotty S. Follicular helper CD4 T cells (TFH). Annu Rev Immunol. 2011;29:621-63."
    doi: "10.1146/annurev-immunol-031210-101400"
    pmid: "21314428"
  - id: sallusto-2010-cd4-memory
    type: peer-reviewed
    cite: "Sallusto F, Lanzavecchia A, Araki K, Ahmed R. From vaccines to memory and back. Immunity. 2010;33(4):451-63."
    doi: "10.1016/j.immuni.2010.10.008"
    pmid: "21029957"
  - id: abbas-immunology-9e
    type: textbook
    cite: "Abbas AK, Lichtman AH, Pillai S. Cellular and Molecular Immunology. 9th ed. Elsevier; 2018."
    url: "https://www.elsevier.com/books/cellular-and-molecular-immunology/abbas/978-0-323-52323-3"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "T helper cells are central coordinators of the adaptive immune response, regulating both cellular and humoral immunity."
  - target: 01-human/04-cellular/dendritic-cell
    relation: modulated-by
    note: "Mature dendritic cells present pMHC-II complexes and co-stimulatory signals that activate naïve CD4+ T cells and determine effector subset differentiation."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: modulated-by
    note: "Peptide:MHC-II complexes on APCs are the essential activating ligand for CD4+ TCR; without pMHC-II engagement, T helper cell activation cannot proceed."
  - target: 01-human/04-cellular/b-cell
    relation: modulates
    note: "Tfh cells in germinal centers provide obligatory help to B cells via CD40L–CD40 interaction and IL-21/IL-4 cytokines, enabling class-switch recombination, somatic hypermutation, and plasma cell differentiation."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: infected-by
    note: "SARS-CoV-2 can infect a subset of CD4+ T cells via ACE2 or CD147; viral RNA has been detected in T cells from severe COVID-19 patients, potentially contributing to lymphopenia and immune dysregulation."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: infected-by
    note: "HIV-1 preferentially depletes CD4+ T helper cells via CCR5/CXCR4-mediated entry; progressive loss below 200 cells/μL defines AIDS and abrogates all T-cell-dependent adaptive immunity."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: damaged-by
    note: "HIV-induced CD4+ T cell depletion occurs via direct cytopathic killing, pyroptosis of bystander cells, immune activation exhaustion, and Nef-mediated MHC-II downregulation impairing antigen presentation."
  - target: 01-human/03-molecular/il-6
    relation: expresses
    note: "Activated CD4+ T helper cells, particularly Th17 precursors, co-produce IL-6 with TGF-β, driving autocrine Th17 differentiation and amplifying local inflammatory circuits."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: modulated-by
    evidence: zhu-paul-2010-th-differentiation
    note: "NK cells suppress T helper cell activation through cytotoxic elimination of antigen-presenting dendritic cells and regulatory cytokine secretion."
  - target: 01-human/06-organ/thymus
    relation: part-of
    evidence: zhu-paul-2010-th-differentiation
    note: "CD4⁺ T helper cells undergo positive selection on MHC class II and negative selection on self-antigens in the thymus; exported as naive CD4⁺ T cells to peripheral lymphoid organs to initiate adaptive immune responses."
  - target: 01-human/03-molecular/leptin
    relation: modulated-by
    note: "Modulated by Leptin."
  - target: 01-human/02-atomic/zinc
    relation: modulated-by
    note: "Modulated by Zinc."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulated-by
    note: "Modulated by Regulatory T Cell."
  - target: 01-human/04-cellular/mast-cell
    relation: modulated-by
    note: "Modulated by Mast Cell."
  - target: 02-pathogen/01-viruses/measles-virus
    relation: infected-by
    note: "Infected by Measles Virus."
  - target: 03-medicine/03-food/zinc-dietary
    relation: modulated-by
    note: "Modulated by Dietary Zinc."
  - target: 01-human/03-molecular/il-2
    relation: modulated-by
    note: "IL-2 is the primary autocrine/paracrine Th cell growth factor after TCR + CD28 co-stimulation; NFAT drives IL-2 transcription (blocked by calcineurin inhibitors); IL-2 → JAK1/JAK3/STAT5 → cyclin D/BCL-2/BCL-XL → T cell proliferation and survival in immune responses."
  - target: 01-human/03-molecular/calcineurin
    relation: modulated-by
    note: "Calcineurin dephosphorylates NFATc1-4 in activated T helper cells → nuclear entry → IL-2, IL-4, IFN-γ, TNF-α transcription; cyclosporine·cyclophilin and tacrolimus·FKBP12 inhibit calcineurin → block T cell cytokine production."
---

# T Helper Cell

## Overview

The CD4+ T helper cell (Th cell) is the master orchestrator of adaptive immunity — the lymphocyte subset that decides the character, magnitude, and duration of nearly every immune response [^zhu-paul-2010-th-differentiation]. Named for their role in "helping" other immune cells, T helper cells provide the cognate signals (direct cell contact and cytokines) that are essential for B cell class switching and affinity maturation, CD8+ cytotoxic T cell activation, macrophage polarization, and the establishment of immunological memory.

CD4+ T cells recognize antigen exclusively as peptide fragments presented on MHC class II molecules — expressed only on professional antigen-presenting cells (dendritic cells, B cells, macrophages). This MHC-II restriction means T helper cells respond to extracellular pathogens and protein antigens, and are the primary responders to vaccine antigens delivered to the lymph node.

The importance of CD4+ T cells to vaccine-elicited immunity cannot be overstated: depletion of CD4+ T cells in animal models abolishes germinal center formation, long-lived plasma cell generation, and memory B cell development. In HIV-1 infection, progressive CD4+ T cell depletion (by a virus that itself preferentially infects these cells) leads to AIDS — total collapse of both humoral and cellular adaptive immunity.

## Structure

### Surface phenotype

| Marker | Expression | Function |
|:---|:---|:---|
| CD4 | Constitutive | Co-receptor for MHC-II; binds β2 domain; carries Lck |
| TCRαβ | Constitutive | Antigen receptor; recognizes pMHC-II |
| CD3 (γδεζ) | Constitutive | TCR signaling complex |
| CD28 | Naïve/memory | Co-stimulatory receptor for CD80/86 on APC |
| CD45RA | Naïve | Protein tyrosine phosphatase; isoform switch on memory formation |
| CCR7 | Naïve + central memory | Lymph-node homing chemokine receptor |
| CXCR5 | Tfh | Follicle-homing receptor (CXCL13 gradient) |
| PD-1 | Tfh + exhausted | Inhibitory checkpoint |

### CD4+ T cell subsets — effector diversification

Upon activation in a specific cytokine milieu, naïve CD4+ T cells differentiate into functionally distinct effector subsets [^zhu-paul-2010-th-differentiation]:

| Subset | Inducing cytokines | Master TF | Signature cytokines | Function |
|:---|:---|:---|:---|:---|
| **Th1** | IL-12, IFN-γ | T-bet | IFN-γ, TNF, LTα | Macrophage activation; intracellular pathogen clearance; anti-tumor |
| **Th2** | IL-4 | GATA-3 | IL-4, IL-5, IL-13 | B cell IgE class switch; eosinophil activation; anti-helminth; allergy |
| **Th17** | TGF-β + IL-6, IL-23 | RORγt | IL-17A, IL-17F, IL-22 | Neutrophil recruitment; mucosal barrier defense; autoimmunity |
| **Tfh** | IL-6, IL-21, ICOS-L | Bcl-6 | IL-21, IL-4, CXCL13 | Germinal center formation; B cell help; antibody class switching |
| **Treg** | TGF-β, IL-2 | FoxP3 | IL-10, TGF-β | Immune suppression; self-tolerance; peripheral tolerance |
| **Th9** | TGF-β + IL-4 | PU.1/IRF4 | IL-9, IL-10 | Anti-parasitic; anti-tumor; allergy |

## Function

### Signal requirements for activation

Three signals are required for naïve CD4+ T cell activation:
1. **Signal 1** — TCR engagement with cognate pMHC-II: Lck (associated with CD4) phosphorylates ITAM motifs in CD3ζ → ZAP-70 → LAT/SLP-76 → PLCγ1 → DAG + IP3 → PKCθ + calcineurin/NFAT → gene transcription.
2. **Signal 2** — Co-stimulation: CD28 on T cell engages CD80/CD86 on APC → PI3K → Akt → NF-κB + AP-1 amplification; prevents anergy.
3. **Signal 3** — Cytokines from APC: IL-12 drives Th1; IL-4 drives Th2; TGF-β + IL-6 drives Th17/Treg; IL-6 + IL-21 + ICOS-L drives Tfh.

Without all three signals, T cells become anergic or die by activation-induced cell death.

### Tfh cells and the germinal center reaction

Follicular helper T cells (Tfh) are the CD4+ subset essential for durable antibody production — the cellular basis of vaccine-elicited long-term immunity [^crotty-2011-tfh]. After initial activation by DCs, a subset of activated CD4+ T cells upregulates Bcl-6, CXCR5, PD-1, and ICOS, and downregulates CCR7, allowing migration from the T cell zone into B cell follicles.

In **germinal centers**, Tfh cells provide:
- **CD40L (CD154)** — binds CD40 on B cells; obligatory for B cell activation, class-switch recombination, and plasma cell differentiation
- **IL-21** — the primary Tfh effector cytokine; promotes B cell proliferation, somatic hypermutation, and plasma cell differentiation
- **CXCL13** — produced by Tfh; recruits CXCR5+ cells into the follicle
- **Competitive selection** — Tfh cells select B cell clones for limited antigen on follicular DCs, driving affinity maturation

Loss of Tfh function (e.g., in HIV-1 infection depleting CD4+ cells, or in conditions disrupting ICOS–ICOS-L interactions) results in poor germinal center formation, low-affinity antibodies, and failed immunological memory — explaining why CD4+ T cell help is non-negotiable for protective vaccination.

### Memory T helper cells

After the primary response, most effector T helper cells die (~90–95 %) [^sallusto-2010-cd4-memory]. Survivors become long-lived **memory T cells** (central memory: CCR7+CD45RO+; effector memory: CCR7−CD45RO+). Memory CD4+ T cells can respond within hours of pathogen re-encounter (vs. days for naïve cells), provide accelerated B cell help, and can persist for decades in humans.

## Lifecycle

### Development in the thymus

CD4+ T cells arise from common lymphoid progenitors (CLPs) in bone marrow that seed the thymus. In the thymus:
1. **Double-negative (DN) stage**: TCR loci rearrange (RAG1/RAG2 recombinase)
2. **Double-positive (DP) stage**: CD4+CD8+ thymocytes undergo positive selection — TCRs with sufficient affinity for self-MHC survive; weak-affinity cells die by neglect
3. **Lineage commitment**: DP cells commit to CD4 or CD8 lineage based on MHC class (MHC-II signals → CD4; MHC-I → CD8); Thpok/GATA-3 drives CD4 fate
4. **Negative selection**: strong self-reactive TCRs are deleted (central tolerance); FoxP3+ Tregs are generated from moderately self-reactive cells
5. **Export**: single-positive CD4+CD8− naïve T cells exit to the periphery

### Peripheral survival

Naïve CD4+ T cells require tonic TCR signaling (low-affinity self-pMHC-II contact) and IL-7 for peripheral homeostatic survival. The naïve T cell pool is large (~300 million cells in adults) and slowly divides.

### Activation, expansion, and contraction

After antigen recognition: rapid clonal expansion (10³–10⁴-fold, ~2–3 days), peak response ~7–10 days, contraction to ~5–10 % of peak by day 14–21. Memory cells persist for years.

## Connections

- **Part of:** [immune-system](../../07-system/immune-system/README.md)
- **Activated by (modulated-by):** [dendritic-cell](../dendritic-cell/README.md) — DC presents pMHC-II
- **Activated by (modulated-by):** [mhc-class-ii](../../03-molecular/mhc-class-ii/README.md) — essential activating ligand
- **Modulates:** [b-cell](../b-cell/README.md) — Tfh provides germinal center help for antibody class switching
- **Infected by:** [sars-cov-2](../../../../02-pathogen/01-viruses/sars-cov-2/README.md) — direct infection and lymphopenia contribute to COVID-19 immunopathology
- `modulated-by` → **[IL-2](../../03-molecular/il-2/README.md)** — IL-2 is the primary autocrine/paracrine Th cell growth factor; NFAT drives IL-2 transcription (blocked by cyclosporine/tacrolimus); IL-2 → JAK1/JAK3/STAT5 → cyclin D/BCL-2/BCL-XL → proliferation and survival.
- `modulated-by` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin dephosphorylates NFATc1-4 in activated T helper cells → nuclear entry → IL-2, IL-4, IFN-γ, TNF-α transcription; cyclosporine·cyclophilin and tacrolimus·FKBP12 inhibit calcineurin → block T cell cytokine production.

[^zhu-paul-2010-th-differentiation]: Zhu J, Paul WE. Heterogeneity and plasticity of T helper cells. *Cell Res.* 2010;20(1):4-12. [doi:10.1038/cr.2009.138](https://doi.org/10.1038/cr.2009.138) · [PubMed 20010916](https://pubmed.ncbi.nlm.nih.gov/20010916/)
[^crotty-2011-tfh]: Crotty S. Follicular helper CD4 T cells (TFH). *Annu Rev Immunol.* 2011;29:621-63. [doi:10.1146/annurev-immunol-031210-101400](https://doi.org/10.1146/annurev-immunol-031210-101400) · [PubMed 21314428](https://pubmed.ncbi.nlm.nih.gov/21314428/)
[^sallusto-2010-cd4-memory]: Sallusto F, Lanzavecchia A, Araki K, Ahmed R. From vaccines to memory and back. *Immunity.* 2010;33(4):451-63. [doi:10.1016/j.immuni.2010.10.008](https://doi.org/10.1016/j.immuni.2010.10.008) · [PubMed 21029957](https://pubmed.ncbi.nlm.nih.gov/21029957/)
[^abbas-immunology-9e]: Abbas AK, Lichtman AH, Pillai S. *Cellular and Molecular Immunology.* 9th ed. Elsevier; 2018.
