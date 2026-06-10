---
schema: human-scale-entry/v1
id: peyers-patches
name: "Peyer's Patches"
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-06
summary: "Unencapsulated lymphoid nodules in ileal submucosa; primary inductive site of gut mucosal immunity. M cells in follicle-associated epithelium sample luminal antigens; germinal centers produce IgA-committed B cells that migrate to lamina propria for secretory IgA synthesis."
aliases: ["Peyer patches", "ileal lymphoid nodules", "GALT", "gut-associated lymphoid tissue"]
sources:
  - id: cornes-1965-peyers-patches
    type: peer-reviewed
    cite: "Cornes JS. Number, size, and distribution of Peyer's patches in the human small intestine. Gut. 1965;6(3):225-233."
    doi: "10.1136/gut.6.3.225"
    pmid: "5826791"
    url: "https://doi.org/10.1136/gut.6.3.225"
  - id: neutra-1996-m-cells
    type: peer-reviewed
    cite: "Neutra MR, Frey A, Kraehenbuhl JP. Epithelial M cells: gateways for mucosal infection and immunization. Cell. 1996;86(3):345-348."
    doi: "10.1016/S0092-8674(00)80106-3"
    pmid: "8756715"
    url: "https://doi.org/10.1016/S0092-8674(00)80106-3"
  - id: fagarasan-2003-iga
    type: peer-reviewed
    cite: "Fagarasan S, Honjo T. Intestinal IgA synthesis: regulation of front-line body defences. Nat Rev Immunol. 2003;3(1):63-72."
    doi: "10.1038/nri982"
    pmid: "12511876"
    url: "https://doi.org/10.1038/nri982"
cross_links:
  - target: 01-human/06-organ/small-intestine
    relation: part-of
    note: "Peyer's patches are embedded in the submucosa and lamina propria of the small intestine (predominantly ileum); they are the primary organized lymphoid tissue of the gut wall."
  - target: 01-human/04-cellular/b-cell
    relation: contains
    note: "B-cell follicles with germinal centers are the dominant structural feature of Peyer's patches; IgA class-switching driven by TGF-β and IL-10 from local Tfh and regulatory cells produces IgA-committed B cell blasts that migrate to lamina propria."
  - target: 01-human/04-cellular/dendritic-cell
    relation: contains
    note: "Subepithelial dome DCs capture antigens transcytosed by M cells and present them to T and B cells in the patch; CD103+ DCs drive retinoic acid-mediated IgA class switching and gut-homing receptor (α4β7, CCR9) imprinting."
  - target: 01-human/05-tissue/germinal-center
    relation: contains
    note: "Each Peyer's patch contains multiple B-cell follicles with germinal centers; antigen-driven GC reactions in Peyer's patches are the primary source of IgA-committed B cells populating the intestinal lamina propria."
---

# Peyer's Patches

## Overview

**Peyer's patches** are discrete, unencapsulated aggregates of lymphoid follicles embedded in the submucosa of the small intestine (predominantly the **ileum**). First described by the Swiss anatomist Johann Conrad Peyer in 1677, they constitute the largest component of **gut-associated lymphoid tissue (GALT)** and represent the primary inductive site for intestinal mucosal immune responses.

In adult humans, the small intestine contains approximately **30–40 Peyer's patches** — the number peaking in the second decade of life and declining with age — each measuring 1–3 cm in length and visible as oval elevations on the anti-mesenteric wall of the ileum [^cornes-1965-peyers-patches]. Together, they comprise a substantial fraction of the body's total lymphoid mass and orchestrate the **intestinal IgA response** that is the dominant antibody in the gut lumen, colostrum, and mucosal secretions.

The strategic position of Peyer's patches — sampling the luminal contents of the most densely microbially colonized region of the gut — makes them central to both **oral tolerance** (suppressing immune responses to dietary antigens and commensal microbes) and **protective immunity** against enteric pathogens.

## Structure

### Follicle-associated epithelium (FAE) and M cells

The epithelium overlying each Peyer's patch — the **follicle-associated epithelium (FAE)** — is fundamentally distinct from the absorptive villi of surrounding mucosa [^neutra-1996-m-cells]:

- **M cells (microfold cells):** Specialized epithelial cells (5–10% of FAE) with a unique morphology: apical surface has irregular microfolds rather than microvilli, reduced glycocalyx, and minimal alkaline phosphatase activity. Their basolateral surface forms an **intraepithelial pocket** containing DCs, macrophages, B cells, and occasional T cells.
  - Function: **transcytosis** of luminal macromolecules, bacteria, viruses, and particles from the lumen to the subepithelial dome — without degradation
  - M cells are the entry point for numerous enteric pathogens: Salmonella typhi, Yersinia, poliovirus, and prions exploit M-cell transcytosis for invasion
  - M cell differentiation is induced by RANKL (expressed by stromal cells under B cell/T cell signals) acting on FAE precursor cells

**Subepithelial dome (SED):** The region immediately beneath the FAE; rich in macrophages, DCs, and a heterogeneous population of B cells. Antigens transcytosed by M cells are captured here and presented to resident lymphocytes.

### Lymphoid follicles

Each Peyer's patch contains multiple (**B-cell follicles**) arranged in a crescent. Each follicle has:
- A **germinal center** with centroblasts/centrocytes and FDCs (see `05-tissue/germinal-center`)
- An **IgA-committed microenvironment:** follicular DCs express APRIL and BAFF; Tfh produce IL-10, IL-21, and TGF-β → drive IgA class switch recombination in GC B cells
- A **mantle zone** of naïve B cells surrounding the GC
- Follicular T cells (Tfh, BCL6⁺CXCR5⁺) in the light zone

**T-cell zone:** Each Peyer's patch contains an interfollicular T-cell zone with HEV (high endothelial venules) for lymphocyte entry. CD4⁺ T cells predominate; retinoic acid-producing DCs and stromal cells imprint gut-homing receptors (α4β7 integrin + CCR9) on activated lymphocytes.

## Function

**Antigen sampling:** M-cell transcytosis delivers luminal antigens — both pathogenic and commensal — to the subepithelial dome without disrupting the epithelial barrier. This enables the adaptive immune system to "see" the lumen without direct mucosal breach [^neutra-1996-m-cells].

**IgA induction [^fagarasan-2003-iga]:**
1. DCs capture antigen from SED → migrate into follicle → present to Tfh and B cells
2. GC reaction in follicles: B cells undergo AID-mediated IgA class switch recombination (predominant isotype switch in Peyer's patches, driven by TGF-β + IL-10 + APRIL/BAFF)
3. IgA-committed B cell blasts exit via efferent lymphatics → thoracic duct → blood → home to intestinal lamina propria (via α4β7–MAdCAM-1 interaction)
4. In lamina propria: differentiate into IgA-secreting plasma cells → dimeric IgA → transported across epithelium by pIgR → secretory IgA in lumen
5. Secretory IgA binds and neutralizes luminal pathogens, toxins, and antigens via **immune exclusion**

**Oral tolerance:** The regulatory microenvironment of Peyer's patches — retinoic acid from DCs, TGF-β, IL-10 — promotes conversion of naive CD4⁺ T cells to Foxp3⁺ regulatory T cells (iTregs). This is essential for preventing inflammatory responses to dietary antigens and commensal microbes.

**Role in mucosal vaccines:** Live oral vaccines (OPV, live oral typhoid Ty21a, oral cholera vaccines) engage Peyer's patches as the inductive site — driving mucosal IgA responses that protect the intestinal entry portal directly.

## Connections

- `part-of` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Peyer's patches are the primary organized lymphoid tissue of the small intestinal wall.
- `contains` → **[B Cell](../../04-cellular/b-cell/README.md)** — IgA-committed B cells are generated in Peyer's patch GCs and home to the lamina propria.
- `contains` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — subepithelial dome DCs capture M-cell-transcytosed antigens and drive IgA class switching via retinoic acid and BAFF/APRIL.
- `contains` → **[Germinal Center](../germinal-center/README.md)** — B-cell follicles within Peyer's patches contain active germinal centers driving IgA affinity maturation and class switch recombination.
- `connects-to` → **[OPV (Oral Polio Vaccine)](../../../../04-vaccine/05-live-attenuated/oral-polio-vaccine/README.md)** — OPV poliovirus binds CD155 on M cells in Peyer's patches; GALT replication drives lamina propria B cells → sIgA via pIgR transcytosis; mucosal sIgA blocks gut re-infection — the eradication-critical response absent from injected IPV.

[^cornes-1965-peyers-patches]: Cornes JS. Number, size, and distribution of Peyer's patches in the human small intestine. *Gut.* 1965;6(3):225-233. [doi:10.1136/gut.6.3.225](https://doi.org/10.1136/gut.6.3.225) · [PubMed 5826791](https://pubmed.ncbi.nlm.nih.gov/5826791/)
[^neutra-1996-m-cells]: Neutra MR, Frey A, Kraehenbuhl JP. Epithelial M cells: gateways for mucosal infection and immunization. *Cell.* 1996;86(3):345-348. [doi:10.1016/S0092-8674(00)80106-3](https://doi.org/10.1016/S0092-8674(00)80106-3) · [PubMed 8756715](https://pubmed.ncbi.nlm.nih.gov/8756715/)
[^fagarasan-2003-iga]: Fagarasan S, Honjo T. Intestinal IgA synthesis: regulation of front-line body defences. *Nat Rev Immunol.* 2003;3(1):63-72. [doi:10.1038/nri982](https://doi.org/10.1038/nri982) · [PubMed 12511876](https://pubmed.ncbi.nlm.nih.gov/12511876/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
