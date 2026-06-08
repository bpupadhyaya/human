---
schema: human-scale-entry/v1
id: plasma-cell
name: Plasma Cell
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-04
summary: "Terminal effector of B cell differentiation — large oval cell with eccentric nucleus, clock-face chromatin, and massive rough ER secreting 1,000–10,000 antibodies/sec. Long-lived plasma cells in bone marrow are the cellular basis of durable humoral immunity."
aliases: ["plasmablast", "LLPC", "long-lived plasma cell", "antibody-secreting cell", "ASC"]
sources:
  - id: slifka-1998-llpc
    type: peer-reviewed
    cite: "Slifka MK, Antia R, Whitmire JK, Ahmed R. Humoral immunity due to long-lived plasma cells. Immunity. 1998;8(3):363-72."
    doi: "10.1016/S1074-7613(00)80541-5"
    pmid: "9529153"
  - id: nutt-2015-b-cell-fate
    type: peer-reviewed
    cite: "Nutt SL, Hodgkin PD, Tarlinton DM, Corcoran LM. The generation of antibody-secreting plasma cells. Nat Rev Immunol. 2015;15(3):160-71."
    doi: "10.1038/nri3795"
    pmid: "25698678"
  - id: amanna-slifka-2010-durability
    type: peer-reviewed
    cite: "Amanna IJ, Slifka MK. Mechanisms that determine plasma cell lifespan and the duration of humoral immunity. Immunol Rev. 2010;236(1):125-38."
    doi: "10.1111/j.1600-065X.2010.00912.x"
    pmid: "20636813"
  - id: turner-2021-vaccine-llpc
    type: peer-reviewed
    cite: "Turner JS, et al. SARS-CoV-2 mRNA vaccines induce persistent human germinal centre responses. Nature. 2021;596(7870):109-113."
    doi: "10.1038/s41586-021-03738-2"
    pmid: "34182569"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "Plasma cells are the terminal effector cells of humoral adaptive immunity, secreting the antibodies that circulate throughout the immune system."
  - target: 01-human/04-cellular/b-cell
    relation: modulated-by
    note: "Plasma cells differentiate from germinal-center B cells that have received sufficient T cell help and undergone class-switch recombination and affinity maturation."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: expresses
    note: "Long-lived plasma cells are the primary source of circulating IgG; each LLPC secretes thousands of IgG molecules per second continuously for years."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "BAFF via BCMA and APRIL via BCMA/TACI provide long-lived plasma cell survival signals in bone marrow niches; atacicept (anti-BAFF+APRIL) depletes plasma cells; BCMA-directed therapies (teclistamab, idecabtagene vicleucel CAR-T) target plasma cells in multiple myeloma."
---

# Plasma Cell

## Overview

The plasma cell is the terminal differentiation product of the B lymphocyte lineage — a cell that has abandoned antigen recognition and become a dedicated **antibody factory** [^nutt-2015-b-cell-fate]. Unlike naïve and memory B cells, plasma cells have little or no surface immunoglobulin and cannot recognize antigen. Instead, their entire biosynthetic machinery is oriented toward one task: secreting antibody at extraordinary rates of **1,000–10,000 molecules per second**, sustained continuously for the life of the cell.

The discovery that long-lived plasma cells (LLPCs) can persist in bone marrow niches for decades — secreting antigen-specific antibody without further antigen stimulation — resolved a long-standing mystery of immunological memory [^slifka-1998-llpc]. Serum antibody titers against measles and yellow fever, detectable for 50+ years after vaccination, are maintained by these cells. The duration of vaccine-elicited protection is therefore, in large part, a function of whether the vaccine succeeds in generating long-lived bone-marrow plasma cells.

## Structure

### Morphology

The plasma cell has a characteristic histological appearance immediately recognizable under light microscopy:

| Feature | Description |
|:---|:---|
| Size | Large, 12–20 µm diameter |
| Shape | Oval/round; eccentric nucleus |
| Nucleus | Peripheral ("clock-face" or "cartwheel" chromatin — heterochromatin arranged in spokes) |
| Cytoplasm | Abundant, deeply basophilic (massive ribosome + rough ER density) |
| Perinuclear hof | Clear zone adjacent to nucleus (distended Golgi apparatus) |
| Surface Ig | None or very low (contrast with naïve B cells) |

### Ultrastructure — secretory specialization

The rough endoplasmic reticulum (rER) in plasma cells is among the most extensively developed in any human cell type. Stacks of rER cisternae fill the cytoplasm, reflecting the enormous translational load of antibody production. The Golgi is dilated and active, processing the N-linked glycosylation at Asn297 of each IgG heavy chain before secretory vesicle packaging.

**Key transcription factor — Blimp-1 (PRDM1):** Blimp-1 is the master regulator of plasma cell identity. It represses PAX5 (the B cell master regulator), c-Myc (proliferation), and BCL-6 (GC B cell program), while activating IRF4 (plasma cell gene program) and XBP-1 (UPR/ER expansion). The transition B cell → plasma cell is essentially the suppression of the B cell program by Blimp-1 and the activation of the secretory program by XBP-1.

**Unfolded protein response (UPR):** The enormous antibody secretion rate places massive stress on the ER. Plasma cells constitutively activate the UPR — particularly the IRE1α–XBP-1 axis — to expand ER capacity, increase protein folding chaperones (BiP/GRP78), and upregulate ERAD (ER-associated degradation) to clear misfolded chains. Failure to sustain this UPR leads to ER stress and plasma cell death.

### Plasmablast vs. long-lived plasma cell

Two kinetically distinct populations arise after immunization:

| Feature | Plasmablast | Long-lived plasma cell (LLPC) |
|:---|:---|:---|
| Timing | Days 5–14 post-immunization | Weeks to months; then persist |
| Location | Germinal center egress → blood → extrafollicular foci | Bone marrow niches (CXCL12-rich) |
| Affinity | Lower (less SHM) | Higher (more rounds of GC selection) |
| Lifespan | Days to weeks | Months to decades |
| CXCR4 | Low | High (bone marrow homing) |
| CD138 (SDC1) | + | ++ |
| Ki67 | + | − (non-dividing) |

LLPCs are non-dividing, terminally differentiated cells that have ceased expressing most surface molecules including MHC-II. They survive in specialized bone marrow niches that provide survival signals including APRIL (TNFSF13), BAFF (TNFSF13B), IL-6, SDF-1 (CXCL12), and stromal cell contact.

## Function

### Antibody secretion kinetics

A single activated B cell–derived plasmablast can secrete ~1000 antibody molecules/sec [^amanna-slifka-2010-durability]. A long-lived plasma cell, while secreting at similar rates, maintains this production for years. At a serum IgG concentration of ~10 mg/mL and IgG half-life of ~21 days, the steady-state secretion rate required to maintain this pool in an adult (blood volume ~5 L; extravascular IgG roughly equal) is approximately 2 g of IgG per day — one of the highest protein secretion rates in the body.

### Isotype and subclass specification

Plasma cells are "locked" into the immunoglobulin isotype (IgG1, IgG3, IgA, IgE, etc.) that was established during class-switch recombination in the germinal center. Cytokine signals received during the GC reaction (IL-4 → IgG1/IgE; IFN-γ → IgG3; TGF-β → IgA) determine which CH constant region was recombined, and this is irreversible in the plasma cell.

### Niche maintenance and vaccine correlates

The bone marrow plasma cell niche — a spatially defined zone with CXCL12-secreting stromal cells, megakaryocytes, eosinophils, and mesenchymal stem cells — can accommodate only a limited number of LLPCs at any time. Competition between newly generated plasma cells and pre-existing LLPCs for niche access may explain why repeated booster immunizations or new infections can displace older plasma cell populations, raising concerns about waning of long-term vaccine immunity under repeated boosting regimens.

mRNA vaccines (BNT162b2, mRNA-1273) have been shown to elicit sustained germinal center reactions detectable in lymph nodes for at least 12 weeks post-vaccination, generating LLPCs with continuously improving affinity [^turner-2021-vaccine-llpc].

## Lifecycle

### Differentiation cascade

The plasma cell differentiation cascade is driven by sequential transcription factor activation:

1. **Antigen activation + T cell help** → upregulation of IRF4 at intermediate levels
2. **Blimp-1 (PRDM1) induction** → repression of PAX5, BCL-6, AID; loss of BCR, MHC-II, and GC program
3. **XBP-1 activation** (via IRE1α splicing) → ER expansion, secretory pathway upregulation
4. **CXCR4 upregulation** → bone marrow homing
5. **CD138 (syndecan-1) upregulation** → canonical plasma cell surface marker

The entire process from naive B cell activation to bone marrow residency takes ~3–4 weeks via the germinal center route.

### Senescence vs. longevity mechanisms

LLPCs avoid apoptosis via constitutive expression of anti-apoptotic BCL-2 family members (BCL-2, BCL-XL, MCL-1) and tonic survival signaling from niche factors. Removal from the bone marrow niche in vitro results in rapid apoptosis, demonstrating that LLPC survival is niche-dependent, not cell-autonomous.

## Connections

- **Part of:** [immune-system](../../07-system/immune-system/README.md)
- **Differentiated from (modulated-by):** [b-cell](../b-cell/README.md) — germinal-center B cells differentiate into plasma cells after class switching and affinity maturation
- **Expresses:** [immunoglobulin-g](../../03-molecular/immunoglobulin-g/README.md) — primary antibody product; each LLPC secretes thousands of IgG molecules per second continuously
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF via BCMA and APRIL via BCMA/TACI provide long-lived plasma cell survival signals in bone marrow niches; atacicept (anti-BAFF+APRIL) depletes plasma cells; BCMA-directed therapies (teclistamab, idecabtagene vicleucel CAR-T) target plasma cells in multiple myeloma.

[^slifka-1998-llpc]: Slifka MK, Antia R, Whitmire JK, Ahmed R. Humoral immunity due to long-lived plasma cells. *Immunity.* 1998;8(3):363-72. [doi:10.1016/S1074-7613(00)80541-5](https://doi.org/10.1016/S1074-7613(00)80541-5) · [PubMed 9529153](https://pubmed.ncbi.nlm.nih.gov/9529153/)
[^nutt-2015-b-cell-fate]: Nutt SL, Hodgkin PD, Tarlinton DM, Corcoran LM. The generation of antibody-secreting plasma cells. *Nat Rev Immunol.* 2015;15(3):160-71. [doi:10.1038/nri3795](https://doi.org/10.1038/nri3795) · [PubMed 25698678](https://pubmed.ncbi.nlm.nih.gov/25698678/)
[^amanna-slifka-2010-durability]: Amanna IJ, Slifka MK. Mechanisms that determine plasma cell lifespan and the duration of humoral immunity. *Immunol Rev.* 2010;236(1):125-38. [doi:10.1111/j.1600-065X.2010.00912.x](https://doi.org/10.1111/j.1600-065X.2010.00912.x) · [PubMed 20636813](https://pubmed.ncbi.nlm.nih.gov/20636813/)
[^turner-2021-vaccine-llpc]: Turner JS, et al. SARS-CoV-2 mRNA vaccines induce persistent human germinal centre responses. *Nature.* 2021;596(7870):109-113. [doi:10.1038/s41586-021-03738-2](https://doi.org/10.1038/s41586-021-03738-2) · [PubMed 34182569](https://pubmed.ncbi.nlm.nih.gov/34182569/)
