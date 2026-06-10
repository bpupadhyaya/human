---
schema: human-scale-entry/v1
id: b-cell
name: B Cell
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-04
summary: "B lymphocyte — antibody-producing cell of adaptive immunity. Surface IgM/IgD BCR binds antigen; with Tfh help undergoes class-switch recombination and affinity maturation in germinal centers; differentiates into plasma cells and memory B cells."
aliases: ["B lymphocyte", "B-lymphocyte", "naive B cell", "memory B cell", "germinal center B cell"]
sources:
  - id: nutt-2015-b-cell-fate
    type: peer-reviewed
    cite: "Nutt SL, Hodgkin PD, Tarlinton DM, Corcoran LM. The generation of antibody-secreting plasma cells. Nat Rev Immunol. 2015;15(3):160-71."
    doi: "10.1038/nri3795"
    pmid: "25698678"
  - id: victora-nussenzweig-2012-gc
    type: peer-reviewed
    cite: "Victora GD, Nussenzweig MC. Germinal centers. Annu Rev Immunol. 2012;30:429-57."
    doi: "10.1146/annurev-immunol-020711-075032"
    pmid: "22224772"
  - id: kurosaki-2010-b-signaling
    type: peer-reviewed
    cite: "Kurosaki T, Shinohara H, Baba Y. B cell signaling and fate decision. Annu Rev Immunol. 2010;28:21-55."
    doi: "10.1146/annurev.immunol.021908.132541"
    pmid: "20192804"
  - id: abbas-immunology-9e
    type: textbook
    cite: "Abbas AK, Lichtman AH, Pillai S. Cellular and Molecular Immunology. 9th ed. Elsevier; 2018."
    url: "https://www.elsevier.com/books/cellular-and-molecular-immunology/abbas/978-0-323-52323-3"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "B cells are the antibody-producing arm of adaptive immunity and a core cellular component of the humoral immune system."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulated-by
    note: "Tfh cells provide obligatory CD40L–CD40 contact and IL-21/IL-4 cytokines for B cell activation, class-switch recombination, and germinal center selection."
  - target: 01-human/04-cellular/plasma-cell
    relation: modulates
    note: "Activated B cells differentiate into antibody-secreting plasmablasts and long-lived plasma cells upon receiving sufficient T cell help and antigen stimulation."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: modulated-by
    evidence: nutt-2015-b-cell-fate
    note: "NK cells modulate B cell activation through IFN-γ and TNF secretion and direct cytotoxic control of abnormal B cell clones."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: modulated-by
    evidence: nutt-2015-b-cell-fate
    note: "Intestinal epithelium provides BAFF/APRIL signals driving IgA class switch in gut-associated B cells via GALT interaction."
  - target: 01-human/05-tissue/bone-marrow
    relation: part-of
    evidence: nutt-2015-b-cell-fate
    note: "B cell lymphopoiesis originates in bone marrow from CLPs; pro-B → pre-B → immature B cell maturation occurs in marrow stroma."
  - target: 01-human/06-organ/spleen
    relation: part-of
    evidence: nutt-2015-b-cell-fate
    note: "Splenic follicles contain B cells that mount T-dependent germinal centre responses and T-independent IgM responses to blood-borne antigens; marginal zone B cells are specialised for rapid responses to encapsulated bacteria."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: modulated-by
    note: "Modulated by Cytotoxic T Cell."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulated-by
    note: "Modulated by Regulatory T Cell."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: infected-by
    note: "Infected by Epstein-Barr Virus."
  - target: 01-human/07-system/norovirus
    relation: infected-by
    note: "Norovirus directly infects B cells via HBGA-like surface carbohydrates (Jones et al. Science 2014); B cell tropism may facilitate systemic dissemination; anti-VP1 IgA and IgG from B cell responses are the primary correlates of protection against norovirus reinfection."
  - target: 01-human/03-molecular/norovirus-vp1
    relation: target-of
    note: "Norovirus VP1 P2 subdomain binds HBGA-like carbohydrates on B cell surfaces → direct B cell infection; anti-VP1 secretory IgA and IgG are the primary correlates of protection; HBGA-blocking anti-VP1 IgA titer is the immunological endpoint of all norovirus vaccines."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "B cells differentiate into plasma cells that secrete anti-AChR IgG1/IgG3; rituximab (anti-CD20) depletes B cells → durable remission especially in MuSK+ MG; plasmablast-derived anti-AChR IgG levels guide treatment decisions in AChR+ vs. MuSK+ subsets."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: infected-by
    note: "EBV (HHV-4) establishes latency in memory B cells via EBNA-1-mediated episome maintenance and LMP1/LMP2A mimicking activated B cell receptors; Gammaherpesvirinae-driven B cell transformation underlies Burkitt lymphoma, Hodgkin lymphoma, PTLD, and NPC."
---

# B Cell

## Overview

The B lymphocyte (B cell) is the antibody-producing cell of adaptive immunity and the cellular basis of humoral protection against extracellular pathogens [^nutt-2015-b-cell-fate]. The "B" designation comes from the **bursa of Fabricius** in birds (the organ where B cells were first identified) and is retained in mammals where B cell development occurs in the **bone marrow**. Unlike T cells, B cells can recognize antigen directly — in its native three-dimensional form — via the **B cell receptor (BCR)**, a membrane-bound immunoglobulin. This capacity for direct antigen recognition makes B cells exquisitely sensitive to the structural features of pathogens and vaccine antigens.

The central output of B cell biology is the production of high-affinity, class-switched antibodies — particularly IgG — that neutralize pathogens, opsonize bacteria, activate complement, and mediate ADCC. The durability of antibody-mediated protection depends on two B cell descendants: **long-lived plasma cells** (LLPCs) in the bone marrow that continuously secrete antibody for years, and **memory B cells** that enable rapid re-expansion and antibody production upon re-exposure.

Vaccination strategies are fundamentally designed to elicit potent germinal center reactions that generate both memory B cells and LLPCs. mRNA vaccines, protein subunit vaccines, and live-attenuated vaccines all ultimately succeed or fail based on their ability to engage and sustain productive B cell responses with T helper cell collaboration.

## Structure

### Surface phenotype

| Marker | Naïve B cell | Germinal center B cell | Memory B cell |
|:---|:---|:---|:---|
| IgM surface | + (BCR) | Low | +/− |
| IgD surface | + | − | − |
| CD19 | + | + | + |
| CD20 | + | + | +/− |
| CD21 (CR2) | + | Low | + |
| CD23 | + | − | − |
| CD27 | − | +/− | + |
| GL-7/Fas | − | + | − |
| BCL-6 | − | + | − |
| AID | − | + | − |

### BCR complex

The **B cell receptor** is a multiprotein complex of:
- Membrane-bound immunoglobulin (initially IgM or IgD, the antigen-binding subunit) formed by two identical heavy and two identical light chains
- **Igα (CD79a) and Igβ (CD79b)** — signaling heterodimer with cytoplasmic ITAMs, non-covalently associated with mIg

BCR crosslinking by multivalent antigen triggers Igα/Igβ ITAM phosphorylation by Lyn → Syk → BLNK → PLCγ2 → Ca²⁺ flux + DAG → PKCβ + calcineurin/NFAT + NF-κB → activation gene transcription.

The **co-receptor complex** — CD21 (CR2, complement receptor 2) + CD19 + CD81 — amplifies BCR signaling ~1000-fold when complement fragment C3d deposits on antigen surface (C3d–antigen crosslinks BCR + CD21; CD19 boosts PI3K activity via Vav). This is a key reason why complement-fixing antibodies and complement-opsonized pathogens are highly immunogenic.

### Antigen receptor diversity

The human B cell repertoire is generated by **VDJ recombination** (heavy chain) and **VJ recombination** (light chain) in the bone marrow, producing an estimated ~10¹⁰–10¹² unique BCR specificities. CDR3 diversity, N-nucleotide additions at junctions, and combinatorial heavy/light chain pairing generate this vast repertoire from a few hundred germline gene segments.

## Function

### Antigen presentation by B cells

In addition to antibody production, B cells are **professional APCs**. After BCR-mediated antigen internalization, B cells process antigen in endolysosomes and present peptides on MHC-II to CD4+ T cells [^kurosaki-2010-b-signaling]. This B cell–T cell encounter at the follicle–T zone border is the critical first interaction that gates germinal center entry: Tfh cells that recognize pMHC-II on antigen-specific B cells license those B cells to enter the follicle.

### Germinal center reactions

The **germinal center** (GC) is a specialized microanatomical structure within secondary lymphoid follicles where the molecular mechanisms that convert a naïve B cell response into long-term humoral memory take place [^victora-nussenzweig-2012-gc]:

1. **Entry** — Antigen-activated B cells enter the follicle, interact with antigen-specific Tfh cells, form a primary focus, and ~10–20 % seed germinal centers
2. **Dark zone** — B cells in the dark zone proliferate at high rate and undergo **somatic hypermutation (SHM)** — AID introduces point mutations in V region genes at ~10⁻³/bp/division, generating BCR variants with altered affinities
3. **Light zone selection** — B cells compete for limiting antigen on follicular DCs (FDCs); clones with higher-affinity BCRs capture more antigen, present more pMHC-II, receive more Tfh help (CD40L + IL-21), and proliferate preferentially — **affinity maturation**
4. **Class-switch recombination (CSR)** — AID introduces double-strand breaks at switch regions; cytokines from Tfh specify the isotype (IL-4 → IgG1, IgE; IFN-γ → IgG3; TGF-β → IgA)
5. **Exit** — selected B cells exit the GC as either plasmablasts (rapid antibody production) or memory B cells (long-lived; can re-enter GC on re-exposure)

### T-independent B cell responses

Some antigens (T-independent type 2 — repetitive polysaccharide arrays) can activate B cells directly without Tfh help, via intense BCR crosslinking + complement. These responses produce mainly IgM with minimal class switching or affinity maturation and do not establish memory — a critical limitation that conjugate vaccines (e.g., Hib, MenC, PCV) overcome by coupling polysaccharide to protein carrier to recruit T cell help.

## Lifecycle

### Development — bone marrow stages

B cell ontogeny proceeds through defined stages defined by immunoglobulin gene rearrangement status and surface marker expression:

| Stage | Heavy chain | Light chain | Surface |
|:---|:---|:---|:---|
| Pro-B | DJ recombination | Germline | CD34+, CD19+, B220+ |
| Pre-B (large) | VDJ recombination → μ | Germline | Pre-BCR (μ + surrogate LC) |
| Pre-B (small) | Fixed μ | VJ recombination | Pre-BCR → surface BCR |
| Immature B | Fixed VDJ | Fixed VJ | IgM+ |
| Mature naïve | Fixed | Fixed | IgM+IgD+ |

Central tolerance removes autoreactive B cells by receptor editing (secondary VJ recombination to change light chain) or clonal deletion at the immature B cell stage.

### Peripheral maturation and activation

Transitional B cells exit the bone marrow to the spleen for final maturation into follicular (FO) B cells (long-lived, GC-competent) or marginal zone (MZ) B cells (short-lived, T-independent responses). Follicular B cells circulate through lymph nodes and spleen follicles, surveying antigen.

### Memory B cell longevity

Memory B cells are long-lived lymphocytes (estimated lifespan years–decades) that circulate between blood, lymph nodes, and non-lymphoid tissues [^nutt-2015-b-cell-fate]. Upon secondary antigen encounter, memory B cells respond within 1–3 days (vs. 7–14 days for naive), undergo additional rounds of affinity maturation, and rapidly differentiate into plasmablasts, generating the anamnestic (recall) antibody response.

## Connections

- **Part of:** [immune-system](../../07-system/immune-system/README.md)
- **Modulated by:** [t-helper-cell](../t-helper-cell/README.md) — Tfh provides germinal center help essential for class switching and memory
- **Modulates:** [plasma-cell](../plasma-cell/README.md) — B cell terminal differentiation produces antibody-secreting plasma cells
- **Infected by:** [Norovirus](../../07-system/norovirus/README.md) — norovirus directly infects B cells via HBGA-like surface carbohydrates (Jones et al. 2014); B cell tropism may enable systemic dissemination; anti-VP1 IgA and IgG from B cell responses are the primary correlates of protection against norovirus reinfection.
- **Targeted by:** [Norovirus VP1](../../03-molecular/norovirus-vp1/README.md) — VP1 P2 subdomain binds HBGA-like carbohydrates on B cell surfaces; anti-VP1 secretory IgA and IgG are the primary correlates of protection; HBGA-blocking anti-VP1 IgA titer is the immunological endpoint of all norovirus vaccines.
- `connects-to` → **[Myasthenia Gravis](../../07-system/myasthenia-gravis/README.md)** — B cells differentiate into plasma cells that secrete anti-AChR IgG1/IgG3; rituximab (anti-CD20) depletes B cells → durable remission especially in MuSK+ MG; plasmablast-derived anti-AChR IgG levels guide treatment decisions in AChR+ vs. MuSK+ subsets.
- `infected-by` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — EBV establishes latency in memory B cells via EBNA-1-mediated episome maintenance and LMP1/LMP2A mimicking activated B cell receptors; Gammaherpesvirinae-driven B cell transformation underlies Burkitt lymphoma, Hodgkin lymphoma, PTLD, and NPC.

[^nutt-2015-b-cell-fate]: Nutt SL, Hodgkin PD, Tarlinton DM, Corcoran LM. The generation of antibody-secreting plasma cells. *Nat Rev Immunol.* 2015;15(3):160-71. [doi:10.1038/nri3795](https://doi.org/10.1038/nri3795) · [PubMed 25698678](https://pubmed.ncbi.nlm.nih.gov/25698678/)
[^victora-nussenzweig-2012-gc]: Victora GD, Nussenzweig MC. Germinal centers. *Annu Rev Immunol.* 2012;30:429-57. [doi:10.1146/annurev-immunol-020711-075032](https://doi.org/10.1146/annurev-immunol-020711-075032) · [PubMed 22224772](https://pubmed.ncbi.nlm.nih.gov/22224772/)
[^kurosaki-2010-b-signaling]: Kurosaki T, Shinohara H, Baba Y. B cell signaling and fate decision. *Annu Rev Immunol.* 2010;28:21-55. [doi:10.1146/annurev.immunol.021908.132541](https://doi.org/10.1146/annurev.immunol.021908.132541) · [PubMed 20192804](https://pubmed.ncbi.nlm.nih.gov/20192804/)
[^abbas-immunology-9e]: Abbas AK, Lichtman AH, Pillai S. *Cellular and Molecular Immunology.* 9th ed. Elsevier; 2018.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
