---
schema: human-scale-entry/v1
id: cd30
name: CD30
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "CD30 (TNFRSF8) is a TNF receptor family member expressed on Reed-Sternberg cells (~100% cHL), ALCL (~100%), and activated lymphocytes; CD30L → TRAF2/5 → NF-κB; brentuximab vedotin (anti-CD30 ADC, MMAE) is the principal CD30-targeting therapy across cHL, ALCL, and CD30+ PTCL."
aliases: ["CD30", "TNFRSF8", "Ki-1 antigen", "CD30 lymphoma", "CD30 Reed-Sternberg", "brentuximab target", "CD30 ALCL", "CD30 Hodgkin lymphoma"]
sources:
  - id: connors-2018-echelon1
    type: peer-reviewed
    cite: "Connors JM, Jurczak W, Straus DJ, et al. Brentuximab vedotin with chemotherapy for stage III or IV Hodgkin's lymphoma. N Engl J Med. 2018;378(4):331-344."
    doi: "10.1056/NEJMoa1708984"
    pmid: "29360494"
    url: "https://doi.org/10.1056/NEJMoa1708984"
  - id: pro-2012-bv-alcl
    type: peer-reviewed
    cite: "Pro B, Advani R, Brice P, et al. Brentuximab vedotin (SGN-35) in patients with relapsed or refractory systemic anaplastic large-cell lymphoma: results of a phase II study. J Clin Oncol. 2012;30(18):2190-2196."
    doi: "10.1200/JCO.2011.38.0402"
    pmid: "22614995"
    url: "https://doi.org/10.1200/JCO.2011.38.0402"
cross_links:
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "CD30-CD30L engagement recruits TRAF2/TRAF5 → NF-κB canonical and non-canonical pathway activation → RS cell survival; NF-κB is constitutively active in RS cells via CD30, CD40, LMP1 (EBV), and CARD11 signals; NF-κB inhibition is a therapeutic goal in relapsed/refractory cHL."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "CD30 and PD-L1/PD-L2 are co-amplified at 9p24.1 in RS cells → dual immune evasion; brentuximab + nivolumab combination active in R/R cHL (ORR ~82%); PD-1 checkpoint inhibition complements CD30 targeting in cHL."
  - target: 01-human/03-molecular/alk
    relation: connects-to
    note: "CD30 is co-expressed with NPM1-ALK in ALK+ ALCL (CD30 nearly 100% in ALCL); brentuximab vedotin (anti-CD30) and ALK inhibitors (crizotinib) are both active in ALCL; combined CD30+ALK targeting in ALK+ ALCL is synergistic preclinically; A+CHP is standard for CD30+ PTCL."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "CD30 belongs to the TNFRSF alongside CD40, RANK, and TNFR1/2; CD30 signaling overlaps with TNFR2 via TRAF2 recruitment; TNF-α drives inflammation in the RS microenvironment; eosinophils and mast cells express CD30L → paracrine RS cell activation."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "CD30 is universally expressed on Reed-Sternberg cells and is a WHO diagnostic criterion for cHL; brentuximab vedotin (anti-CD30 ADC) + AVD is the frontline standard for advanced-stage cHL (ECHELON-1: 6-year OS 93.9% vs 89.4% vs ABVD); CD30 IHC guides brentuximab prescribing."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "RS cells are GC B-cell-derived (clonal IgV rearrangements with SHM) but have lost B-cell transcription program (PAX5 dim, OCT2−/BOB1−); CD30 transiently expressed on activated GC B cells and upregulated ~100-fold in RS cells via constitutive NF-κB and 9p24.1 amplification."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Reed-Sternberg cells originate from GC B cells that failed positive selection; CD30 upregulation is driven by NF-κB (constitutive via CD30/CD40/LMP1), EBV-LMP1, and 9p24.1 copy gain; EBV+ RS cells derive from GC centroblasts expressing Latency IIb."
---

# CD30

## Overview

**CD30 (TNFRSF8, cluster of differentiation 30)**, historically known as the **Ki-1 antigen** (named after the Kiel cell line from which it was first described), is a type I transmembrane glycoprotein and member of the tumor necrosis factor receptor superfamily (TNFRSF). CD30 is the **defining surface antigen of classical Hodgkin lymphoma Reed-Sternberg (RS) cells** (~100% expression) and anaplastic large cell lymphoma (ALCL, ~100%), making it the prototype tumor-associated antigen for antibody-drug conjugate (ADC) therapy. CD30 serves as the therapeutic target of **brentuximab vedotin (Adcetris, anti-CD30 IgG1-MMAE ADC)** — the first ADC to demonstrate randomized Phase 3 survival benefit in lymphoma and the backbone of modern front-line Hodgkin lymphoma therapy [^connors-2018-echelon1][^pro-2012-bv-alcl]. CD30 signaling through TRAF2/TRAF5 activates NF-κB and AP-1, promoting lymphocyte survival and proliferation in both physiologic and neoplastic contexts.

**CD30 expression landscape:**
- **Classical Hodgkin lymphoma (cHL):** RS cells ~100%; CD30 is a WHO diagnostic criterion; intensity variable (strong diffuse in NSHL); eosinophils and plasma cells in microenvironment express CD30L (CD153)
- **ALK+ ALCL:** CD30 ~100%; strong uniform membranous+Golgi pattern; hallmark of the entity
- **ALK- ALCL:** CD30 ~100%; strong; includes BIA-ALCL
- **Primary mediastinal large B-cell lymphoma (PMBL):** CD30 ~80% (weaker than HL); shares 9p24.1 amplification with cHL; brentuximab active
- **PTCL-NOS:** CD30 ~20-30%; variable; ECHELON-2 enrolled CD30 ≥10% by IHC
- **DLBCL:** CD30 ~10-15% (ABC-DLBCL subtype more likely); CD30+ DLBCL may benefit from brentuximab + R-CHOP
- **Mycosis fungoides / Sézary syndrome (CTCL):** CD30 upregulated in transformed MF (~50-60%); brentuximab FDA approved 2017 for CTCL
- **Activated normal lymphocytes:** Transient CD30 on activated B and T cells; not exploitable clinically due to transient expression; soluble CD30 (sCD30) in serum correlates with activated lymphocyte mass

## Structure

### CD30 protein architecture

CD30 is a 595-amino-acid glycoprotein; apparent molecular weight ~90-120 kDa (heavily N- and O-glycosylated):

**Extracellular domain (ECD, 1-365):**
- Six cysteine-rich pseudo-repeats (CRD1-6): hallmark of all TNFRSF members; three-loop structure stabilized by disulfide bonds (two Cys per loop); CD30 ligand (CD30L/CD153) binds CRD2-4
- **Shedding:** Matrix metalloproteinases (MMP) and ADAM proteases cleave the ectodomain → release soluble CD30 (sCD30, ~50-90 kDa in serum); sCD30 correlates with cHL disease burden and response; rising sCD30 during remission may indicate relapse

**Transmembrane domain (366-388):**
Single-pass type I membrane topology; linker region between ECD and intracellular domain; no intrinsic kinase activity (CD30 is a receptor-only signaling molecule)

**Intracellular domain (ICD, 389-595):**
- Contains three TRAF-binding sites: TRAF2 recruitment → IKK activation → NF-κB p65/p50 (canonical); TRAF3 → NF-κB NIK/RelB (non-canonical); TRAF5 → JNK/AP-1 activation
- **TRAF binding motifs:** PVQET (TRAF2 high-affinity), EMEGQGT (TRAF3), PTEETA (TRAF5) — these are consensus TRAF binding sequences in the ICD
- NO death domain (unlike FAS/TNFR1) → CD30 is a survival/proliferation receptor, not an apoptosis inducer in lymphoma context

### CD30 signaling axis

**CD30-mediated signaling (ligand-dependent):**
CD30L (CD153, TNFSF8) expressed on mast cells, activated T cells, macrophages, eosinophils → binds CD30 ECD → receptor oligomerization → TRAF2/TRAF3/TRAF5 recruitment to ICD → divergent pathways:
1. TRAF2 → MEKK1 → JNK → AP-1 → proliferative and survival gene expression (FOS, JUN)
2. TRAF2 → IKKβ → IκBα phosphorylation/degradation → NF-κB (p65/p50) nuclear translocation → survival genes (BCL-2, BCL-XL, cFLIP, XIAP)
3. TRAF3 → NIK stabilization → IKKα → NF-κB (RelB/p52) non-canonical → lymphoid organogenesis and alternative survival signals
4. TRAF2/TRAF5 → ERK → MAPK survival signals

**CD30 in RS cells (constitutive activation):**
RS cells express CD30 at extremely high levels; CD30 signaling is constitutive in RS cells due to: (1) CD30L on microenvironmental eosinophils/mast cells → autocrine/paracrine loop; (2) CD30 overexpression → spontaneous oligomerization without ligand; (3) synergy with CD40 (expressed on RS cells, ligated by CD40L on T cells) and EBV-LMP1 → additive NF-κB activation; RS cell survival is NF-κB-dependent.

### Brentuximab vedotin mechanism

**ADC structure:**
- Anti-CD30 IgG1 mAb (cAC10/brentuximab): targets CRD3-4 of CD30 ECD; high affinity (Kd ~3 nM); human IgG1 backbone → ADCC activity
- Cleavable dipeptide linker (val-cit): stable in plasma; cleaved by cathepsin B (lysosomal protease) after intracellular trafficking
- MMAE (monomethyl auristatin E): microtubule-disrupting agent; tubulin polymerization inhibitor; cell cycle arrest at G2/M; potent cytotoxicity (IC₅₀ low picomolar)

**ADC mechanism:**
1. brentuximab vedotin binds CD30 on tumor cell surface → receptor-mediated endocytosis → trafficking to lysosome
2. Lysosomal cathepsin B cleaves val-cit linker → releases free MMAE intracellularly
3. MMAE inhibits tubulin polymerization → mitotic arrest → apoptosis in CD30+ cell
4. **Bystander effect:** MMAE diffuses across cell membrane to adjacent CD30-negative cells → kills tumor microenvironment cells and CD30-negative tumor cells; this membrane permeability amplifies efficacy in heterogeneous tumors

## Function

### Normal CD30 biology

CD30 expression on normal lymphocytes is transient and activation-dependent: GC B cells transiently express CD30 during affinity maturation; activated CD4+ and CD8+ T cells express CD30 during antigen response; CD30 on normal T cells promotes T-cell survival (anti-apoptotic) and cytokine production after TCR stimulation. CD30-null mice have normal lymphoid development but impaired T-cell memory formation. CD30 signaling normally promotes regulatory T-cell (Treg) and T effector memory (TEM) cell survival, suggesting a homeostatic role in lymphocyte persistence.

### Reed-Sternberg cell identity and CD30

RS cells represent ~0.1-1% of the Hodgkin lymphoma tumor mass; the remainder is reactive inflammatory infiltrate (eosinophils, neutrophils, mast cells, lymphocytes, plasma cells, fibroblasts) recruited by RS cell-secreted cytokines (IL-5, IL-13, CCL5, TARC/CCL17, CXCL5). RS cells are GC B cell-derived (carry clonal Ig V gene rearrangements with somatic hypermutation) but have lost the B-cell transcription program (PAX5 dim; lost BOB1, OCT2, PU.1). CD30 overexpression is a hallmark of RS cell identity: the exact mechanism of CD30 upregulation involves NF-κB-driven CD30 transcription (positive feedback loop), EBV LMP1 (in EBV+ HL), and 9p24.1 copy gains.

## Mechanism

### Clinical use of brentuximab vedotin

**Frontline cHL (advanced stage, ECHELON-1):**
Phase 3 RCT (N=1334): A+AVD (brentuximab vedotin + doxorubicin, vinblastine, dacarbazine) vs ABVD for stage III-IV cHL; primary endpoint modified PFS: 82.1% vs 77.2% at 2 years (HR 0.77, p=0.04); 6-year OS: 93.9% vs 89.4% (HR 0.59, p=0.009); peripheral neuropathy higher with A+AVD (~67% any grade, ~11% Grade 3+); bleomycin lung toxicity eliminated (bleomycin removed from A+AVD); standard of care for advanced stage cHL [^connors-2018-echelon1]

**Consolidation post-auto-SCT (AETHERA):**
Phase 3 RCT: brentuximab vedotin maintenance ×18 cycles vs placebo post-autologous SCT for high-risk R/R cHL; 5-year PFS 59% vs 41% (HR 0.52, p=0.001); FDA approved 2015.

**Relapsed/Refractory cHL:**
- Brentuximab vedotin single-agent: ORR ~75%, CR ~34% (pivotal Phase 2, N=102); median duration of response ~20 months
- Nivolumab or pembrolizumab: ORR ~65-70% in auto-SCT-relapsed cHL
- Brentuximab + nivolumab: ORR ~82% in R/R cHL (Phase 1/2, N=61); being explored in frontline

**ALCL (R/R systemic, FDA 2011):**
Phase 2 (N=58, ALK+ and ALK-, R/R): ORR ~86%, CR ~57%; durable CRs in some patients (sustained off-therapy); approved for systemic ALCL after ≥1 prior therapy [^pro-2012-bv-alcl]

**CD30+ PTCL (frontline, FDA 2018, ECHELON-2):**
A+CHP vs CHOP for CD30+ PTCL (majority PTCL-NOS and ALCL): PFS 48.2 vs 20.8 months; 5-year OS 70.1% vs 61.0%.

**CTCL (FDA 2017):**
ALCANZA trial (CD30+ MF/pALCL): brentuximab vs physician's choice (MTX or bexarotene): objective response lasting ≥4 months: 56.3% vs 12.5%; approved for CD30+ CTCL after ≥1 prior systemic therapy.

**CD30 IHC testing:**
- No universal threshold for CD30 positivity; ECHELON-2 used ≥10%; CTCL approval for CD30 ≥10% by histopathology
- FDA-approved CDx for ALCL (cAC10 IHC); no CDx required for cHL (universally CD30+)

## Connections

- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — CD30-CD30L engagement recruits TRAF2/TRAF5 → NF-κB canonical and non-canonical pathway activation → RS cell survival; NF-κB is constitutively active in RS cells via CD30, CD40, LMP1 (EBV), and CARD11 signals; NF-κB inhibition is a therapeutic goal in relapsed/refractory cHL.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — CD30 and PD-L1/PD-L2 are co-amplified at 9p24.1 in RS cells → dual immune evasion; brentuximab + nivolumab combination active in R/R cHL (ORR ~82%); PD-1 checkpoint inhibition complements CD30 targeting in cHL.
- `connects-to` → **[ALK](../../03-molecular/alk/README.md)** — CD30 is co-expressed with NPM1-ALK in ALK+ ALCL (CD30 nearly 100% in ALCL); brentuximab vedotin (anti-CD30) and ALK inhibitors (crizotinib) are both active in ALCL; combined CD30+ALK targeting in ALK+ ALCL is synergistic preclinically; A+CHP is standard for CD30+ PTCL.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — CD30 belongs to the TNFRSF alongside CD40, RANK, and TNFR1/2; CD30 signaling overlaps with TNFR2 via TRAF2 recruitment; TNF-α drives inflammation in the RS microenvironment; eosinophils and mast cells express CD30L → paracrine RS cell activation.
- `connects-to` → **[Hodgkin Lymphoma](../../07-system/hodgkin-lymphoma/README.md)** — CD30 is universally expressed on Reed-Sternberg cells and is a WHO diagnostic criterion for cHL; brentuximab vedotin (anti-CD30 ADC) + AVD is the frontline standard for advanced-stage cHL (ECHELON-1: 6-year OS 93.9% vs 89.4% vs ABVD); CD30 IHC guides brentuximab prescribing.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — RS cells are GC B-cell-derived (clonal IgV rearrangements with SHM) but have lost B-cell transcription program (PAX5 dim, OCT2−/BOB1−); CD30 transiently expressed on activated GC B cells and upregulated ~100-fold in RS cells via constitutive NF-κB and 9p24.1 amplification.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Reed-Sternberg cells originate from GC B cells that failed positive selection; CD30 upregulation is driven by NF-κB (constitutive via CD30/CD40/LMP1), EBV-LMP1, and 9p24.1 copy gain; EBV+ RS cells derive from GC centroblasts expressing Latency IIb.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^connors-2018-echelon1]: Connors JM, Jurczak W, Straus DJ, et al. Brentuximab vedotin with chemotherapy for stage III or IV Hodgkin's lymphoma. *N Engl J Med.* 2018;378(4):331-344. [doi:10.1056/NEJMoa1708984](https://doi.org/10.1056/NEJMoa1708984) · [PubMed 29360494](https://pubmed.ncbi.nlm.nih.gov/29360494/)
[^pro-2012-bv-alcl]: Pro B, Advani R, Brice P, et al. Brentuximab vedotin (SGN-35) in patients with relapsed or refractory systemic anaplastic large-cell lymphoma: results of a phase II study. *J Clin Oncol.* 2012;30(18):2190-2196. [doi:10.1200/JCO.2011.38.0402](https://doi.org/10.1200/JCO.2011.38.0402) · [PubMed 22614995](https://pubmed.ncbi.nlm.nih.gov/22614995/)
