---
schema: human-scale-entry/v1
id: baff
name: BAFF
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "BAFF (BLyS; TNFSF13B; chr13q34) is a TNF-family B-cell survival cytokine; signals via BAFF-R (non-canonical NF-κB2/RelB), TACI, and BCMA. Belimumab (anti-BAFF; FDA Mar 2011) is approved for SLE; ianalumab (anti-BAFFR) met Phase 3 endpoint in Sjögren's (TWINSS 2023)."
aliases: ["BAFF", "BLyS", "B-cell activating factor", "TNFSF13B", "B lymphocyte stimulator", "CD257", "TALL-1", "THANK", "belimumab target"]
sources:
  - id: mackay-2002-baff-b-cell
    type: peer-reviewed
    cite: "Mackay F, Silveira PA, Brink R. B cells and the BAFF/APRIL axis: fast-forward on autoimmunity and signaling. Curr Opin Immunol. 2007;19(3):327-336."
    doi: "10.1016/j.coi.2007.04.008"
    pmid: "17433875"
    url: "https://doi.org/10.1016/j.coi.2007.04.008"
  - id: navarra-2011-belimumab-bliss76
    type: peer-reviewed
    cite: "Navarra SV, Guzmán RM, Gallacher AE, et al. Efficacy and safety of belimumab in patients with active systemic lupus erythematosus: a randomised, placebo-controlled, phase 3 trial. Lancet. 2011;377(9767):721-731."
    doi: "10.1016/S0140-6736(10)61354-2"
    pmid: "21296403"
    url: "https://doi.org/10.1016/S0140-6736(10)61354-2"
  - id: dorner-2023-ianalumab-twinss
    type: peer-reviewed
    cite: "Dörner T, Bowman SJ, Fox R, et al. Ianalumab (VAY736) in patients with primary Sjögren's syndrome: a multicentre, randomised, double-blind, placebo-controlled, phase 3 trial (TWINSS). Lancet. 2023;402(10400):477-489."
    doi: "10.1016/S0140-6736(23)00454-4"
    pmid: "37499657"
    url: "https://doi.org/10.1016/S0140-6736(23)00454-4"
cross_links:
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "BAFF-R engagement activates non-canonical NF-κB (NIK → IKKα → p100 processing → p52/RelB nuclear translocation) → BCL-2/BCL-XL → B cell survival; TACI activates canonical NF-κB1 → IgA/IgM class-switch recombination and T-independent B cell responses."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "BAFF is elevated in SLE and drives survival of autoreactive B cells that escape negative selection; belimumab (anti-BAFF IgG1; BLISS-52/76; FDA Mar 2011) reduces BAFF-driven B-cell survival → 15-20% flare reduction; BLISS-LN: belimumab + SoC → 43% vs 32% renal response."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "BAFF is overexpressed in salivary glands and serum of pSS patients; BAFF drives B-cell hyperactivation → anti-Ro/SSA production and lymphoma risk; ianalumab (anti-BAFFR; TWINSS: ESSDAI –5.1 vs –2.7 at week 24) demonstrated efficacy in primary Sjögren's syndrome."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "BAFF via BCMA (TNFRSF17) on plasma cells promotes long-lived plasma cell survival; APRIL (TNFSF13A) also signals via BCMA → atacicept (anti-BAFF+APRIL) depletes plasma cells more deeply than anti-BAFF alone; BCMA is therapeutic target in myeloma (teclistamab, CAR-T)."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "BAFF is the critical B-cell survival factor; BAFF-R → NIK → IKKα → p52/RelB → BCL-2/BCL-XL → transitional and naive B-cell survival; excess BAFF expands the peripheral B-cell niche → autoreactive B-cell escape → autoimmunity; BAFF-Tg mice develop SLE-like disease."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "BCMA (TNFRSF17), a BAFF/APRIL receptor on plasma cells, is the validated myeloma target; teclistamab (bispecific T-cell engager; MajesTEC-1) and ciltacabtagene autoleucel (CARTITUDE-1) target BCMA; atacicept (anti-BAFF+APRIL) depletes plasma cells more deeply than belimumab."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "BAFF and IL-6 are co-elevated in SLE, Sjögren's, and RA; IL-6 drives plasma cell differentiation and IgG production downstream of BAFF-driven B-cell activation; tocilizumab (anti-IL-6R) and belimumab (anti-BAFF) target complementary axes of B-cell/plasma cell-driven autoimmunity."
---

# BAFF

## Overview

**BAFF (B-cell activating factor; BLyS, B lymphocyte stimulator; gene *TNFSF13B*, chromosome 13q34)** is a member of the **tumor necrosis factor (TNF) superfamily** and is the central cytokine regulating **peripheral B-cell survival, maturation, and tolerance checkpoints** [^mackay-2002-baff-b-cell]. BAFF is produced primarily by myeloid cells — monocytes, macrophages, neutrophils, dendritic cells — and, to a lesser extent, by T cells and stromal cells. Production is upregulated by type I IFN, IFN-γ, and innate immune signals.

BAFF functions as a **critical survival factor** for transitional B cells maturing into follicular or marginal zone B cells: in the absence of BAFF signaling, most peripheral B cells die by apoptosis within days. In autoimmune diseases, excess BAFF permits survival of autoreactive B cells that would normally be eliminated during peripheral tolerance checkpoints, driving pathogenic autoantibody production.

**Clinical significance:**
- **SLE:** Belimumab (Benlysta; anti-BAFF IgG1 mAb; Human Genome Sciences/GSK) became the first FDA-approved biologic for SLE in March 2011 — ending a 50-year gap in SLE drug approvals
- **Sjögren's syndrome:** BAFF is overexpressed in salivary glands; ianalumab (anti-BAFF-R mAb; Novartis) met the Phase 3 TWINSS trial primary endpoint in 2023 — a major advance for a disease with no approved biologic
- **Multiple myeloma:** BCMA (a BAFF/APRIL receptor on plasma cells) is a validated target; teclistamab, elranatamab, belantamab mafodotin target BCMA

## Structure

### Protein and gene

| Feature | Detail |
|:--------|:-------|
| Gene | *TNFSF13B*, chromosome 13q34 |
| Protein | 285 amino acids; type II transmembrane protein |
| Soluble form | Furin cleavage at Arg133 → soluble homotrimer (17 kDa per monomer; 51 kDa trimeric active form) |
| Family | TNF superfamily; related to APRIL (TNFSF13A), TWEAK, TL1A |
| Expression | Monocytes, macrophages, DCs, neutrophils, T cells, stromal/follicular cells |

### Receptors — BAFF-R, TACI, BCMA

BAFF signals via three receptors with distinct B-lineage expression patterns and downstream signaling:

**BAFF-R (TNFRSF13C; CD268):**
- Expressed on transitional and mature naive B cells; greatly reduced on plasma cells and germinal center B cells
- High specificity for BAFF (does not bind APRIL)
- **Non-canonical NF-κB:** TRAF3 → NIK → IKKα → p100 processing → p52/RelB heterodimer → nuclear translocation → BCL-2↑, BCL-XL↑ → B cell survival
- Loss-of-function BAFF-R → common variable immunodeficiency (CVID)-like phenotype

**TACI (TNFRSF13B; CD267; transmembrane activator and calcium-modulator and cyclophilin ligand interactor):**
- Expressed on mature B cells and plasma cells; binds both BAFF and APRIL
- **Canonical NF-κB:** TRAF2/5/6 → IKKβ → p65/p50 → Ig class-switch recombination (to IgA, IgG) and T-independent antibody responses
- TACI gain-of-function mutations → autoimmunity; loss-of-function → CVID or SLE susceptibility (paradoxical because TACI also delivers negative signals for B cell survival)
- Atacicept (anti-BAFF + anti-APRIL fusion protein) targets TACI-mediated signaling

**BCMA (TNFRSF17; CD269; B-cell maturation antigen):**
- Highly expressed on plasma cells and late-stage germinal center B cells; low on naive B cells
- Binds both BAFF and APRIL; APRIL is the preferred ligand
- Promotes plasma cell survival in bone marrow niches; BCMA-APRIL signaling supports long-lived plasma cell survival → durable IgG titers (beneficial for vaccine memory; pathogenic in autoimmune disease with long-lived autoreactive plasma cells)
- **Multiple myeloma target:** BCMA targeted by anti-BCMA immunotoxin (belantamab mafodotin), CAR-T cells (idecabtagene vicleucel, ciltacabtagene autoleucel), bispecific T-cell engagers (teclistamab, elranatamab)

### APRIL — the BAFF paralogue

**APRIL (a proliferation-inducing ligand; TNFSF13A)** shares ~30% sequence homology with BAFF and binds TACI and BCMA (but not BAFF-R). APRIL promotes T-independent class-switch recombination to IgA and IgM and long-lived plasma cell survival. Atacicept (TACI-Fc fusion; binds both BAFF and APRIL) depletes plasma cells more deeply than belimumab but was associated with worsened infection outcomes in MS trials.

## Function

### Peripheral B-cell survival and selection

BAFF is rate-limiting for survival of **transitional 2 (T2) and follicular B cells** — the stage at which most autoreactive B cells are eliminated by peripheral anergy. When BAFF levels are elevated:
- Autoreactive B cells that would normally undergo apoptosis (due to BCR self-antigen engagement without T-cell help) receive survival rescue via BAFF-R → NF-κB2 → antiapoptotic proteins
- B cell occupancy of BAFF niche is normally competitive; excess BAFF expands the niche → more autoreactive cells survive
- **BAFF-transgenic mice** develop SLE-like disease: elevated ANA, glomerulonephritis, lymphadenopathy

### Class-switch recombination and Ig production

BAFF via TACI → canonical NF-κB → AID (activation-induced cytidine deaminase) upregulation → class-switch to IgG and IgA. BAFF is therefore not only a survival factor but also drives affinity maturation-independent Ig production — relevant to mucosal immunity (IgA in gut) and to pathogenic autoantibody production (anti-dsDNA IgG in SLE).

### Germinal center regulation

Within germinal centers, BAFF provides survival signals to GC B cells that compete for antigen on follicular dendritic cells; dysregulated BAFF → expanded GC reactions → more somatic hypermutation → higher-affinity autoantibodies. B cells in Sjögren's salivary gland form ectopic germinal centers (termed "tertiary lymphoid structures" or "ectopic lymphoid tissue") that depend on BAFF.

## Mechanism

### Belimumab — anti-BAFF antibody

**Belimumab (Benlysta; human IgG1λ anti-BAFF mAb; GSK/Human Genome Sciences):**
- Binds soluble BAFF → prevents BAFF-R, TACI, BCMA engagement → reduces B-cell survival signals
- Does NOT bind APRIL → plasma cell survival partially preserved (rationale for atacicept)
- **BLISS-52 (Asia-Pacific) and BLISS-76 (global)** (N=2133 combined): Belimumab 10 mg/kg IV Q4W vs. placebo + standard of care in active SLE; primary endpoint SRI (SLE Responder Index) at week 52: 57.6% vs. 43.6% (p<0.001); anti-dsDNA reduction, complement normalization [^navarra-2011-belimumab-bliss76]
- **BLISS-LN:** Lupus nephritis (class III/IV/V); primary renal response 43% vs. 32% (p=0.03) at week 104; FDA approved for LN April 2021
- **BLISS-SC:** SC belimumab (200 mg weekly SC) — non-inferior to IV; SC approval 2017; convenient for self-administration
- FDA approved **March 2011** for active SLE (first new SLE drug in 50 years)

### Ianalumab — anti-BAFF-R antibody

**Ianalumab (VAY736; Novartis):**
- Humanized IgG1 anti-BAFF-R (CD268) mAb; targets BAFF-R rather than BAFF itself → depletes B cells via ADCC in addition to blocking BAFF-R signaling
- More complete B-cell depletion than belimumab (which only blocks soluble BAFF)
- **TWINSS Phase 3** (N=290 primary Sjögren's syndrome; ESSDAI ≥5): Ianalumab 300 mg SC Q4W vs. placebo; primary endpoint ESSDAI (EULAR Sjögren's syndrome disease activity index) improvement at week 24: –5.1 vs. –2.7 (p<0.001); also improved ESSPRI (patient symptoms), lacrimal/salivary function [^dorner-2023-ianalumab-twinss]
- First Phase 3 trial to meet primary endpoint in primary Sjögren's syndrome

### Atacicept — anti-BAFF + anti-APRIL

**Atacicept (TACI-Ig; human recombinant fusion protein):**
- Binds both BAFF and APRIL → blocks BAFF-R, TACI, and BCMA signaling → depletes mature B cells and plasma cells
- Phase 2/3 trials in SLE (ADDRESS II): atacicept 75 mg SC Q2W vs. placebo; some evidence of efficacy particularly in IFNHI (IFN-high) patients; Phase 3 ongoing
- **APRIL-MS (MS trial):** Stopped early due to increased relapse rate — depletion of APRIL-dependent regulatory B cells may disinhibit MS activity; caution in demyelinating disease
- IgG reduction >50% (deeper than belimumab due to plasma cell BCMA targeting)

## Connections

- `connects-to` → **[NF-κB](../nf-kb/README.md)** — BAFF-R engagement activates non-canonical NF-κB (NIK → IKKα → p100 → p52/RelB) → B cell survival; TACI activates canonical NF-κB → class-switch recombination; dysregulated BAFF-R/NF-κB2 signaling drives autoreactive B cell survival in SLE and Sjögren's.
- `connects-to` → **[Systemic Lupus Erythematosus](../../07-system/systemic-lupus-erythematosus/README.md)** — BAFF elevated in SLE drives autoreactive B-cell survival; belimumab (anti-BAFF; BLISS-52/76; FDA Mar 2011) reduces flares by 15-20%; BLISS-LN: belimumab + SoC → 43% vs. 32% renal response; anti-BAFF is now a cornerstone of moderate-severe SLE management.
- `connects-to` → **[Sjögren's Syndrome](../../07-system/sjogrens-syndrome/README.md)** — BAFF overexpressed in Sjögren's salivary glands drives B-cell hyperactivation → anti-Ro/SSA and ectopic GC formation → lymphoma risk; ianalumab (anti-BAFFR; TWINSS: ESSDAI –5.1 vs –2.7; Lancet 2023) is the first Phase 3 positive biologic in pSS.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — BAFF via BCMA + APRIL promotes long-lived plasma cell survival; atacicept (anti-BAFF+APRIL) depletes plasma cells more deeply than belimumab; BCMA is the target of teclistamab, elranatamab (bispecific T-cell engagers), and idecabtagene vicleucel CAR-T in multiple myeloma.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — BAFF is the rate-limiting survival factor for transitional and naive B cells; BAFF-R → NIK → p52/RelB → BCL-2/BCL-XL → B cell survival; excess BAFF expands the B-cell niche → autoreactive B-cell escape; belimumab (anti-BAFF) and ianalumab (anti-BAFFR) reduce autoreactive B-cell pools in SLE and Sjögren's.
- `connects-to` → **[Multiple Myeloma](../../07-system/multiple-myeloma/README.md)** — BCMA (TNFRSF17) on plasma cells is the primary BAFF/APRIL receptor validated as a myeloma target; teclistamab (MajesTEC-1) and ciltacabtagene autoleucel (CARTITUDE-1) target BCMA; atacicept (anti-BAFF+APRIL) depletes plasma cells more deeply than belimumab for myeloma applications.
- `connects-to` → **[IL-6](../il-6/README.md)** — BAFF and IL-6 are co-elevated in SLE, Sjögren's, and RA; IL-6 drives plasma cell differentiation and IgG production downstream of BAFF-driven B-cell activation; tocilizumab (anti-IL-6R) and belimumab (anti-BAFF) target complementary axes of B-cell/plasma cell-driven autoimmunity.

[^mackay-2002-baff-b-cell]: Mackay F, Silveira PA, Brink R. B cells and the BAFF/APRIL axis: fast-forward on autoimmunity and signaling. *Curr Opin Immunol.* 2007;19(3):327-336. [doi:10.1016/j.coi.2007.04.008](https://doi.org/10.1016/j.coi.2007.04.008) · [PubMed 17433875](https://pubmed.ncbi.nlm.nih.gov/17433875/)
[^navarra-2011-belimumab-bliss76]: Navarra SV, Guzmán RM, Gallacher AE, et al. Efficacy and safety of belimumab in patients with active systemic lupus erythematosus: a randomised, placebo-controlled, phase 3 trial. *Lancet.* 2011;377(9767):721-731. [doi:10.1016/S0140-6736(10)61354-2](https://doi.org/10.1016/S0140-6736(10)61354-2) · [PubMed 21296403](https://pubmed.ncbi.nlm.nih.gov/21296403/)
[^dorner-2023-ianalumab-twinss]: Dörner T, Bowman SJ, Fox R, et al. Ianalumab (VAY736) in patients with primary Sjögren's syndrome: a multicentre, randomised, double-blind, placebo-controlled, phase 3 trial (TWINSS). *Lancet.* 2023;402(10400):477-489. [doi:10.1016/S0140-6736(23)00454-4](https://doi.org/10.1016/S0140-6736(23)00454-4) · [PubMed 37499657](https://pubmed.ncbi.nlm.nih.gov/37499657/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
