---
schema: human-scale-entry/v1
id: dendritic-cell
name: Dendritic Cell
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-04
summary: "Professional antigen-presenting cell bridging innate and adaptive immunity. Immature DCs patrol tissues; mature DCs upregulate MHC-II and migrate to lymph nodes to prime T cells. Two major subsets: cDC1/cDC2 and pDC."
aliases: ["DC", "professional APC", "plasmacytoid DC", "conventional DC"]
sources:
  - id: banchereau-steinman-1998
    type: peer-reviewed
    cite: "Banchereau J, Steinman RM. Dendritic cells and the control of immunity. Nature. 1998;392(6673):245-52."
    doi: "10.1038/32588"
    pmid: "9521319"
  - id: merad-2013-dc-biology
    type: peer-reviewed
    cite: "Merad M, Sathe P, Helft J, Miller J, Mortha A. The dendritic cell lineage: ontogeny and function of dendritic cells and their precursors in steady state and the inflamed setting. Annu Rev Immunol. 2013;31:563-604."
    doi: "10.1146/annurev-immunol-020711-074950"
    pmid: "23516985"
  - id: guilliams-2022-dc-classification
    type: peer-reviewed
    cite: "Guilliams M, et al. Dendritic cells and monocytes with distinct inflammatory responses reside in lung mucosa of mild COVID-19 patients. J Exp Med. 2020;217(12):e20201228."
    doi: "10.1084/jem.20201228"
    pmid: "33027508"
  - id: steinman-2007-dc-nobel
    type: peer-reviewed
    cite: "Steinman RM. Dendritic cells: understanding immunogenicity. Eur J Immunol. 2007;37 Suppl 1:S53-60."
    doi: "10.1002/eji.200737400"
    pmid: "17972355"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "Dendritic cells are central cellular components of both the innate and adaptive arms of the immune system."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: expresses
    note: "Mature dendritic cells express very high surface densities of MHC-II loaded with processed peptides; this is the key molecular signal that activates naïve CD4+ T cells."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "Mature DCs present pMHC-II complexes and supply co-stimulatory signals (CD80, CD86) and cytokines that determine which CD4+ T helper subset develops."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: infected-by
    note: "Plasmacytoid DCs and some monocyte-derived DCs are susceptible to SARS-CoV-2 infection; viral accessory proteins suppress MHC-II expression and type I IFN production, impairing antigen presentation."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: infected-by
    note: "Plasmacytoid and myeloid DCs express CD4 and CCR5/CXCR4; HIV-1 infects and impairs DCs, suppressing type I IFN production and MHC-II-mediated antigen presentation to T cells, facilitating immune escape."
  - target: 02-pathogen/01-viruses/dengue-virus
    relation: infected-by
    note: "Skin-resident immature DCs (Langerhans cells) are the primary target of initial dengue infection via DC-SIGN (CD209) and AXL; viral replication in DCs leads to systemic dissemination via lymphatics."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: modulated-by
    evidence: banchereau-steinman-1998
    note: "NK cells activate dendritic cells via IFN-γ, enhancing DC maturation, IL-12 production, and antigen presentation."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: modulated-by
    evidence: merad-2013-dc-biology
    note: "Intestinal epithelium provides TSLP and IL-25 signals that programme gut DCs toward tolerogenic Th2/Treg phenotypes."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: damaged-by
    evidence: banchereau-steinman-1998
    note: "S. aureus leukotoxins including PVL form pores in DC membranes, inducing cell death and impairing adaptive immune priming."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: damaged-by
    evidence: merad-2013-dc-biology
    note: "A. fumigatus gliotoxin induces apoptosis in dendritic cells, impairing fungal antigen presentation and enabling immune evasion."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: infected-by
    evidence: merad-2013-dc-biology
    note: "Candida albicans is recognised by DC Dectin-1 and TLR2; in immunocompromised hosts DCs may harbour intracellular yeast, impairing killing."
  - target: 01-human/06-organ/thymus
    relation: part-of
    evidence: merad-2013-dc-biology
    note: "Thymic DCs present self-antigens to developing thymocytes in the medulla, deleting autoreactive T cells (negative selection); medullary thymic DCs also generate natural Tregs via low-affinity self-peptide recognition."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: infected-by
    evidence: banchereau-steinman-1998
    note: "HPV-16 infects keratinocytes and may be carried by Langerhans cells (skin DCs) to lymph nodes; HPV E7 impairs IRF3 and TLR9 signalling in DCs, reducing IFN-β production and allowing persistent mucosal infection."
---

# Dendritic Cell

## Overview

The dendritic cell (DC) is the most potent professional antigen-presenting cell in the body and the master link between the innate and adaptive immune systems [^banchereau-steinman-1998]. Described by Ralph Steinman and Zanvil Cohn in 1973 (Steinman received the Nobel Prize in Physiology or Medicine in 2011), DCs are the only cells that can efficiently prime naïve T lymphocytes — a capacity that sets them apart from macrophages, B cells, and other APCs that activate only pre-sensitized lymphocytes.

DCs reside in virtually every tissue in an **immature state**, continuously sampling the environment by macropinocytosis, phagocytosis, and receptor-mediated endocytosis. Upon encountering a pathogen-associated molecular pattern (PAMP) or danger signal (DAMP), they undergo **maturation** — a profound phenotypic transformation — upregulating MHC-II and co-stimulatory molecules, producing inflammatory cytokines, and migrating via lymphatics to the draining lymph node, where they present processed antigens to naïve T cells and initiate adaptive immunity.

DCs are also the target cells that vaccine platforms such as lipid-nanoparticle mRNA vaccines must efficiently reach. Spike-encoding mRNA delivered by LNPs is taken up by tissue-resident DCs at the injection site and draining lymph-node DCs; these cells translate spike protein, process it, load MHC-II (and cross-present via MHC-I), and prime both CD4+ and CD8+ T cell responses alongside B cell help.

## Structure

### Morphology

Mature DCs are large cells (12–20 µm) with characteristic **stellate morphology** — multiple long cytoplasmic projections (dendrites, veils) that dramatically increase membrane surface area for T cell contacts. In lymph nodes, a single DC can contact hundreds of T cells via these processes.

| Feature | Immature DC (tissue) | Mature DC (lymph node) |
|:---|:---|:---|
| MHC-II surface | Low (mostly intracellular) | Very high |
| CD80/CD86 (co-stim) | Low | High |
| Antigen uptake | High | Low |
| CCR7 | Low | High (drives lymph node migration) |
| IL-12 production | Low/variable | High (cDC1 especially) |
| T cell priming capacity | Low | Very high |

### Subset diversity

Two major lineages, distinct in ontogeny, surface markers, and function [^merad-2013-dc-biology]:

**Classical/conventional DCs (cDC):**
- **cDC1** (CD8α+ in mouse lymphoid tissue; CD103+ in mouse non-lymphoid; BDCA-3+/CD141+ in human): Specialize in MHC-I cross-presentation of intracellular antigens; produce IL-12; prime CD8+ cytotoxic T cells. Require IRF8 and BATF3 for development.
- **cDC2** (CD11b+, BDCA-1+/CD1c+ in human): Major subset in peripheral tissues; present antigen primarily via MHC-II; prime CD4+ T helper cells; require IRF4 for development.

**Plasmacytoid DCs (pDC):**
- BDCA-2+/CD123+ in human. Do not specialize in antigen presentation; primary function is massive production of **type I interferons** (IFN-α, IFN-β) via TLR7/TLR9 sensing of ssRNA and CpG DNA in endosomes. Critical in early antiviral responses.
- pDCs can be infected by SARS-CoV-2, diminishing their IFN output and contributing to the defective type I IFN response seen in severe COVID-19 [^guilliams-2022-dc-classification].

**Monocyte-derived DCs (mo-DC):**
- Arise from circulating monocytes recruited to inflamed tissues; functionally resemble cDC2; important in chronic infection and vaccine site inflammation.

### Key surface molecules

| Category | Molecules |
|:---|:---|
| Antigen presentation | MHC-II (HLA-DR, DQ, DP), MHC-I |
| Pattern recognition | TLR1–9, CLRs (DC-SIGN/CD209, Dectin-1), NLRs, RIG-I, cGAS–STING |
| Co-stimulatory | CD80 (B7.1), CD86 (B7.2), CD40, OX40L, 4-1BBL |
| Migration | CCR7 (lymph-node homing), CCR1/5 (tissue homing) |
| Fc receptors | FcγRI, FcγRIIA/III (enhanced antigen uptake of immune complexes) |

## Function

### Antigen capture and processing

Immature tissue DCs capture antigens via multiple routes:
- **Macropinocytosis** — bulk fluid uptake; samples soluble antigens non-specifically
- **Receptor-mediated endocytosis** — C-type lectins (DC-SIGN, Dectin-1), Fc receptors, complement receptors; targeted, highly efficient
- **Phagocytosis** — uptake of particles, dead cells, opsonized bacteria

Internalized antigens are delivered to endolysosomes where proteases degrade them; peptides are loaded onto MHC-II (or, via cross-presentation pathways involving the ER or recycling endosomes, onto MHC-I).

### Maturation — the critical switch

TLR or NLR engagement by microbial products triggers a transcriptional switch via NF-κB, AP-1, and IRF factors. Within hours to 1–2 days:
1. MHC-II synthesis is massively upregulated; lysosomal MHC-II complexes are stabilized and trafficked to the surface
2. CD80 and CD86 expression provides Signal 2 for T cells
3. CCR7 expression enables chemokine-guided migration to lymph nodes via CCL19/CCL21 gradients
4. IL-12, IL-6, IL-23, TNF production shapes the T cell differentiation milieu (Th1, Th17, or tolerogenic)
5. Antigen uptake capacity is reduced — the DC focuses on presenting what it has already captured

### T cell priming in the lymph node

In the lymph node T cell zone, mature DCs extend dendrites and make serial brief contacts with hundreds of naïve T cells via immunological kinapses, until a T cell with matching TCR specificity is found [^steinman-2007-dc-nobel]. The cognate T cell then forms a stable immunological synapse (signal 1: TCR–pMHC-II; signal 2: CD28–CD80/86; signal 3: cytokines). Sustained signaling (~6–24 h) commits the T cell to clonal expansion.

## Lifecycle

### Development

DCs arise from **common dendritic cell progenitors (CDPs)** in the bone marrow, derived from the common myeloid progenitor (CMP) via macrophage/DC progenitor (MDP). The transcription factor cascade includes: **PU.1** (all myeloid cells) → **GFI1** → **BATF3 + IRF8** (for cDC1) or **IRF4** (for cDC2) → **E2-2 (TCF4)** (for pDC). CDPs circulate and seed peripheral tissues as pre-DCs.

### Tissue residency and turnover

Tissue DCs have short lifespans (days to weeks) and are continuously replenished from circulating precursors. Langerhans cells (epidermal DCs) are an exception — they are long-lived, self-renewing cells of embryonic origin (yolk-sac macrophage progenitors) that persist in the epidermis without bone-marrow replenishment under steady-state conditions.

### Maturation and death

After delivering their antigenic cargo to T cells, mature DCs in lymph nodes undergo apoptosis within 1–2 weeks, limiting the duration of the priming signal. IL-10 and T cell-derived signals can suppress DC maturation in tolerogenic contexts.

## Connections

- **Part of:** [immune-system](../../07-system/immune-system/README.md) — cellular bridge between innate detection and adaptive priming
- **Expresses:** [mhc-class-ii](../../03-molecular/mhc-class-ii/README.md) — the key antigen-presenting molecule
- **Modulates:** [t-helper-cell](../../04-cellular/t-helper-cell/README.md) — DC activation of naïve CD4+ T cells is the rate-limiting step in humoral and cellular adaptive immunity
- **Infected by:** [sars-cov-2](../../../../02-pathogen/01-viruses/sars-cov-2/README.md) — viral impairment of DC function contributes to the immunopathology of severe COVID-19

[^banchereau-steinman-1998]: Banchereau J, Steinman RM. Dendritic cells and the control of immunity. *Nature.* 1998;392(6673):245-52. [doi:10.1038/32588](https://doi.org/10.1038/32588) · [PubMed 9521319](https://pubmed.ncbi.nlm.nih.gov/9521319/)
[^merad-2013-dc-biology]: Merad M, Sathe P, Helft J, Miller J, Mortha A. The dendritic cell lineage: ontogeny and function of dendritic cells and their precursors in steady state and the inflamed setting. *Annu Rev Immunol.* 2013;31:563-604. [doi:10.1146/annurev-immunol-020711-074950](https://doi.org/10.1146/annurev-immunol-020711-074950) · [PubMed 23516985](https://pubmed.ncbi.nlm.nih.gov/23516985/)
[^guilliams-2022-dc-classification]: Guilliams M, et al. Dendritic cells and monocytes with distinct inflammatory responses reside in lung mucosa of mild COVID-19 patients. *J Exp Med.* 2020;217(12):e20201228. [doi:10.1084/jem.20201228](https://doi.org/10.1084/jem.20201228) · [PubMed 33027508](https://pubmed.ncbi.nlm.nih.gov/33027508/)
[^steinman-2007-dc-nobel]: Steinman RM. Dendritic cells: understanding immunogenicity. *Eur J Immunol.* 2007;37 Suppl 1:S53-60. [doi:10.1002/eji.200737400](https://doi.org/10.1002/eji.200737400) · [PubMed 17972355](https://pubmed.ncbi.nlm.nih.gov/17972355/)
