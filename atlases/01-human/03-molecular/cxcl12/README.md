---
schema: human-scale-entry/v1
id: cxcl12
name: CXCL12
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "CXCL12 (SDF-1, chr10q11.21) is a constitutive CXC chemokine; CXCR4 → Gαi → PI3K/Akt retains HSC in bone marrow; plerixafor (CXCR4 antagonist) mobilizes HSC for transplantation; CXCR4 drives cancer metastasis to CXCL12-rich organs and is the X4-tropic HIV-1 co-receptor."
aliases: ["CXCL12", "SDF-1", "stromal cell-derived factor 1", "SDF1", "PBSF", "CXCL12α", "CXCL12β"]
cross_links:
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "CXCL12 from CAR cells (CXCL12-abundant reticular cells) → CXCR4 on HSC → Gαi → PI3K/Akt + actin polymerization → HSC retention in bone marrow niches; plerixafor (AMD3100, CXCR4 antagonist) blocks this → HSC egress into blood → collection for autologous transplant."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "CXCR4 gain-of-function mutations (WHIM-type S338X, C1013G) in 30-40% of WM → impaired receptor desensitization → enhanced CXCL12/CXCR4 bone marrow retention and resistance to BTK inhibitor ibrutinib; CXCR4 mutation status predicts ibrutinib response and PFS in WM."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "CXCL12/CXCR4 is essential for B and T lymphocyte development: pro-B cells and immature B cells migrate within bone marrow guided by CXCL12; T cell thymic export → SDF-1 gradients; HIV-1 X4-tropic strains use CXCR4 as co-receptor (CD4 primary + CXCR4 secondary → cell entry)."
sources:
  - id: nagasawa-1996-cxcl12
    type: peer-reviewed
    cite: "Nagasawa T, Hirota S, Tachibana K, et al. Defects of B-cell lymphopoiesis and bone-marrow myelopoiesis in mice lacking the CXC chemokine PBSF/SDF-1. Nature. 1996;382(6592):635-638."
    doi: "10.1038/382635a0"
    pmid: "8757135"
    url: "https://doi.org/10.1038/382635a0"
  - id: dipersio-2009-plerixafor
    type: peer-reviewed
    cite: "DiPersio JF, Stadtmauer EA, Nademanee A, et al. Plerixafor and G-CSF versus placebo and G-CSF to mobilize hematopoietic stem cells for autologous stem-cell transplantation in patients with multiple myeloma. Blood. 2009;113(23):5720-5726."
    doi: "10.1182/blood-2008-08-174946"
    pmid: "19363221"
    url: "https://doi.org/10.1182/blood-2008-08-174946"
---

# CXCL12

## Overview

**CXCL12 (stromal cell-derived factor 1, SDF-1)** (gene *CXCL12*, chromosome 10q11.21) is a **constitutively expressed CXC chemokine** — unlike most inflammatory chemokines which are induced transiently, CXCL12 is produced constitutively by stromal cells in the **bone marrow, lymph nodes, thymus, liver, lung, and brain**, creating permanent chemotactic gradients that govern the **homing, retention, and trafficking of hematopoietic stem cells (HSC), lymphocytes, and progenitor cells** throughout life.

CXCL12 signals through two G protein-coupled receptors: **CXCR4** (the primary signaling receptor) and **CXCR7/ACKR3** (an atypical receptor, primarily acts as scavenger/decoy to regulate CXCL12 gradients). The CXCL12/CXCR4 axis is one of the most evolutionarily conserved chemokine-receptor pairs — CXCR4 and CXCL12 knockouts in mice are embryonic lethal (cardiovascular and hematopoietic defects) — underscoring its fundamental developmental role.

**Three major clinical contexts:**
1. **Hematopoietic stem cell mobilization** — plerixafor (AMD3100, Mozobil) blocks CXCR4 → releases HSC from bone marrow → peripheral blood collection for autologous transplantation; combined with G-CSF for superior mobilization in myeloma, lymphoma, SCID
2. **Cancer metastasis** — CXCR4 overexpressed on breast, lung, pancreatic, prostate, and renal cell cancers → tumor cells home to CXCL12-rich organs (bone, liver, brain, lung) → organ-specific metastasis patterns; CXCR4 antagonism under investigation
3. **Waldenstrom's macroglobulinemia** — CXCR4 GOF mutations (WHIM-type) impair receptor internalization → enhanced BM retention → resistance to ibrutinib; CXCR4 mutational status guides therapy selection

## Structure

**CXCL12 protein:**
CXCL12 exists as **six splice variants** (CXCL12α-ζ) from alternative exon inclusion; α (68 aa mature form) and β (72 aa) are the dominant forms.
- **Signal peptide (21 aa):** Cleaved → secreted mature CXCL12
- **CXC motif (N-terminal):** Glu26-Leu27-Arg28 (ELR sequence absent — CXCL12 is ELR-negative, unlike CXCL8/IL-8); CXCL12 does NOT attract neutrophils (ELR-negative CXC chemokines attract lymphocytes and T cells)
- **N-loop + 30s loop:** Primary CXCR4 binding surfaces; CXCL12 Tyr7 and Pro9 essential for CXCR4 N-terminus contacts
- **Three-strand β-sheet + C-terminal α-helix:** Classic chemokine scaffold (shared with IL-8, MCP-1, RANTES)
- **Dimerization:** CXCL12α forms homodimers at high concentrations via β-strand interface; monomers are the active CXCR4-binding form; dimers may bind CXCR4 differently (potential biased signaling)

**CXCR4 receptor (CXCR4 gene, chr2q22.1; 352 aa):**
- Class A GPCR; constitutively expressed on HSC, B/T lymphocytes, monocytes, endothelial cells
- **Gαi-coupled:** CXCL12 → CXCR4 → Gαi → **↓cAMP** → reduced PKA; Gβγ → **PI3Kγ → Akt** (survival, migration) + PLC-β → IP3/Ca²⁺ → actin cytoskeleton remodeling → chemotaxis
- **β-arrestin pathway:** CXCR4 → β-arrestin-2 → ERK1/2 → proliferation; CXCR4 internalization requires β-arrestin; impaired in WHIM syndrome (GOF mutations impair β-arrestin recruitment → excessive CXCR4 signaling duration)
- **CXCR7/ACKR3:** Does not couple to G proteins; acts as scavenger/decoy → internalizes and degrades CXCL12 → shapes tissue CXCL12 gradients; also activates β-arrestin directly

**Bone marrow retention niche:**
CXCL12-abundant reticular (CAR) cells in bone marrow → CXCL12 gradient → CXCR4 on HSC → Rac1-mediated actin polymerization → **lamellipodia formation → attachment to marrow stroma**; co-factors: VLA-4/VCAM-1 (adhesion), CXCL12-induced FAK activation → strengthened HSC-niche contact; disrupting any component → HSC egress.

## Function

**Hematopoietic stem cell biology:**
- CXCL12-null mice: bone marrow is depleted of HSC; B cell progenitors and myeloid progenitors fail to home to marrow; lethal from cardiovascular and hematopoietic defects (embryonic day E18-19) [^nagasawa-1996-cxcl12]
- In adults: HSC circulate at very low levels (~1-10/mL blood) under normal conditions; CXCL12 gradient maintains 99%+ of HSC in bone marrow niches (endosteal and perivascular)
- **Aging and myeloid bias:** Older HSC express less CXCR4 → weaker bone marrow retention → increased circulating HSC → altered niche sensing; contributes to clonal hematopoiesis (CHIP) age-related shifts

**Cancer homing and metastasis:**
- CXCR4 is the most widely expressed chemokine receptor in cancers (>23 tumor types)
- Breast cancer: CXCR4 overexpression → bone and lung metastasis (CXCL12-rich sites); CXCL12 from breast stroma amplifies primary tumor growth; CXCR4 expression correlates with lymph node involvement and poor prognosis
- Pancreatic cancer: tumor cells co-express CXCR4 + CXCL12 (autocrine loop) → invasion; stromal PSC (pancreatic stellate cells) secrete CXCL12 → chemotherapy resistance (BMS-936564, anti-CXCR4 mAb, under investigation)
- AML: leukemic blasts hijack CXCL12/CXCR4 for bone marrow retention and chemotherapy protection; plerixafor + G-CSF mobilizes blasts → enhanced chemotherapy exposure (preclinical)
- CNS tumors: glioblastoma cells express CXCR4 → CXCL12 from perivascular niches → tumor invasion and treatment resistance

**HIV-1 tropism:**
- **R5-tropic HIV-1:** Uses CD4 + CCR5 (main receptor at transmission); target of maraviroc (CCR5 antagonist)
- **X4-tropic HIV-1:** Uses CD4 + CXCR4; emerges in late-stage AIDS when CD4+ T cells are depleted; CXCR4-using strains more pathogenic in advanced disease
- CXCR4 was the first discovered HIV co-receptor (fusin, 1996); structural basis for CXCL12 competition with HIV envelope gp120 for CXCR4 N-terminus

**WHIM syndrome:**
- **WHIM (Warts, Hypogammaglobulinemia, Infections, Myelokathexis):** Rare primary immunodeficiency from **autosomal dominant CXCR4 GOF mutations** (typically C-terminal truncations deleting internalization signals; most common: S338X, R334X)
- Truncated CXCR4 → impaired β-arrestin recruitment → receptor fails to internalize after CXCL12 binding → prolonged CXCR4 signaling → neutrophil retention in bone marrow (myelokathexis) + B cell lymphopenia → recurrent infections and HPV-driven warts/cancer
- Treatment: plerixafor (CXCR4 antagonist) mobilizes myeloid cells in WHIM; mavorixafor (oral CXCR4 antagonist) FDA-approved February 2024 for WHIM — the only approved disease-specific therapy

## Mechanism

**Plerixafor in stem cell mobilization [^dipersio-2009-plerixafor]:**
- AMD3100 (plerixafor, Mozobil): bicyclam small molecule → CXCR4 antagonist; binds CXCR4 transmembrane domain → blocks CXCL12 binding → HSC no longer retained → egress into blood within 1-2 hours; **reversible** — HSC return to marrow after plerixafor clears
- Standard mobilization: G-CSF alone for 4-5 days → HSC mobilization via CXCL12/CXCL12R disruption + protease release; some patients are "poor mobilizers" with G-CSF alone
- **AMBER trial (myeloma):** Plerixafor + G-CSF vs. G-CSF alone; plerixafor arm: 72% of patients collected target CD34+ cells on first day vs. 34% G-CSF alone; superior total CD34+ yield; FDA-approved 2008
- **CRYSTAL trial (NHL):** Similar benefit; plerixafor + G-CSF doubles CD34+ yield in poor mobilizers

**CXCR4 mutations in Waldenström's macroglobulinemia:**
- WM (IgM-secreting lymphoplasmacytic lymphoma): >90% harbor MYD88 L265P + 30-40% have CXCR4 mutations (WHIM-type S338X most common)
- CXCR4 mutation → impaired internalization → enhanced marrow retention of WM cells → BM disease burden
- **Ibrutinib resistance:** CXCR4-mutant WM has lower response rates to ibrutinib (BTK inhibitor) → patients may require BORTEzomib or BENDAMUSTINE + anti-CD20 regimens
- Zanubrutinib (BTK inhibitor): partially overcomes CXCR4-mutant ibrutinib resistance; higher MRR in CXCR4-mutant WM than ibrutinib

## Connections

CXCL12 from CAR cells (CXCL12-abundant reticular cells) → CXCR4 on HSC → Gαi → PI3K/Akt + actin polymerization → HSC retention in bone marrow niches; plerixafor (AMD3100, CXCR4 antagonist) blocks this → HSC egress into blood → collection for autologous transplant.

CXCR4 gain-of-function mutations (WHIM-type S338X, C1013G) in 30-40% of WM → impaired receptor desensitization → enhanced CXCL12/CXCR4 bone marrow retention and resistance to BTK inhibitor ibrutinib; CXCR4 mutation status predicts ibrutinib response and PFS in WM.

CXCL12/CXCR4 is essential for B and T lymphocyte development: pro-B cells and immature B cells migrate within bone marrow guided by CXCL12; T cell thymic export → SDF-1 gradients; HIV-1 X4-tropic strains use CXCR4 as co-receptor (CD4 primary + CXCR4 secondary → cell entry).

[^nagasawa-1996-cxcl12]: Nagasawa T, Hirota S, Tachibana K, et al. Defects of B-cell lymphopoiesis and bone-marrow myelopoiesis in mice lacking the CXC chemokine PBSF/SDF-1. *Nature.* 1996;382(6592):635-638. [doi:10.1038/382635a0](https://doi.org/10.1038/382635a0) · [PubMed 8757135](https://pubmed.ncbi.nlm.nih.gov/8757135/)
[^dipersio-2009-plerixafor]: DiPersio JF, Stadtmauer EA, Nademanee A, et al. Plerixafor and G-CSF versus placebo and G-CSF to mobilize hematopoietic stem cells for autologous stem-cell transplantation in patients with multiple myeloma. *Blood.* 2009;113(23):5720-5726. [doi:10.1182/blood-2008-08-174946](https://doi.org/10.1182/blood-2008-08-174946) · [PubMed 19363221](https://pubmed.ncbi.nlm.nih.gov/19363221/)
