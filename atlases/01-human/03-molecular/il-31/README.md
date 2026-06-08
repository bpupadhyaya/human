---
schema: human-scale-entry/v1
id: il-31
name: IL-31
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-31 (IL31, chr12q24.31) is a Th2 cytokine signaling via IL-31RA/OSMR → JAK1/JAK2 → STAT3/STAT5; activates sensory neurons driving itch; nemolizumab (anti-IL-31RA) reduced prurigo nodularis itch 71% (OLYMPIA 2) and is approved for AD pruritus."
aliases: ["IL-31", "interleukin-31", "itch cytokine", "pruritic cytokine", "neuroinflammation cytokine"]
cross_links:
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "IL-31 is the dominant itch cytokine in AD; elevated in lesional skin and serum correlating with pruritus VAS; IL-31 from Th2 cells/mast cells → IL-31RA on sensory DRG neurons → JAK1 → TRPV1/TRPA1 sensitization; nemolizumab (anti-IL-31RA) reduces AD itch 60% vs. 20% placebo."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "IL-31 is a key mediator of PN pruritus; mast cells and Th2 cells in PN nodules produce IL-31 → sensory nerve IL-31RA → itch-scratch cycle; nemolizumab 60 mg SC Q4W reduced IGA success 26% vs. 0% placebo at 16 weeks (OLYMPIA 2, FDA approved Aug 2023)."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "IL-4 promotes Th2 differentiation and IL-31 production; IL-4 + IL-13 downregulate FLG in keratinocytes → barrier disruption → sensitization to IL-31 signaling; dupilumab (anti-IL-4Rα) indirectly reduces IL-31 by suppressing Th2 environment driving IL-31 production."
sources:
  - id: dillon-2004-il-31
    type: peer-reviewed
    cite: "Dillon SR, Sprecher C, Hammond A, et al. Interleukin 31, a cytokine produced by activated T cells, induces dermatitis in mice. Nat Immunol. 2004;5(7):752-760."
    doi: "10.1038/ni1084"
    pmid: "15184896"
    url: "https://doi.org/10.1038/ni1084"
  - id: stander-2020-nemolizumab-pn
    type: peer-reviewed
    cite: "Ständer S, Yosipovitch G, Legat FJ, et al. Trial of nemolizumab in moderate-to-severe prurigo nodularis. N Engl J Med. 2020;382(8):706-716."
    doi: "10.1056/NEJMoa1908316"
    pmid: "32053299"
    url: "https://doi.org/10.1056/NEJMoa1908316"
  - id: yosipovitch-2023-nemolizumab-ad
    type: peer-reviewed
    cite: "Yosipovitch G, Ständer S, Kerby MB, et al. Nemolizumab in patients with moderate-to-severe atopic dermatitis: randomized, phase 3, ARCADIA 1 and ARCADIA 2 trials. J Am Acad Dermatol. 2023;89(1):38-49."
    doi: "10.1016/j.jaad.2023.01.006"
    pmid: "36669666"
    url: "https://doi.org/10.1016/j.jaad.2023.01.006"
---

# IL-31

## Overview

**IL-31** (interleukin-31; gene *IL31*, chromosome 12q24.31) is a four-helix-bundle cytokine produced primarily by activated **CD4⁺ Th2 cells**, with additional contributions from mast cells, basophils, and innate lymphoid cells type 2 (ILC2s). It is uniquely distinguished among interleukins as the **principal mediator of pruritus (itch)** in inflammatory skin diseases, acting directly on sensory neurons (dorsal root ganglia, DRG) that innervate skin — making it a neuro-immune bridge between adaptive Th2 inflammation and the nervous system sensation of itch [^dillon-2004-il-31].

IL-31 signals through a heterodimeric receptor complex composed of **IL-31RA** (IL-31 receptor alpha; also known as GPL or gp130-like receptor) and **OSMR** (oncostatin M receptor beta). IL-31RA is highly expressed on small-diameter unmyelinated (C-fiber) and lightly myelinated (Aδ-fiber) sensory neurons in skin, as well as on keratinocytes, dorsal root ganglia, and peripheral blood monocytes. The discovery that IL-31 directly activates sensory neurons to trigger itch (rather than acting indirectly via histamine) established a new paradigm of **cytokine-driven neurogenic itch** distinct from histamine-mediated mechanisms — explaining why antihistamines fail in atopic dermatitis and prurigo nodularis.

**Nemolizumab** (Galderma; anti-IL-31RA IgG4 monoclonal antibody) is the first approved therapy targeting this cytokine axis. FDA approved for **prurigo nodularis** (August 2023, OLYMPIA trials) and for the **itch component of moderate-to-severe atopic dermatitis** in adults and adolescents ≥12 years (2024, ARCADIA trials). This dual approval positions IL-31/IL-31RA as one of the most therapeutically important cytokine axes in dermatology.

## Structure

**IL-31 protein:**
- 164 aa; molecular weight ~26 kDa (monomer); member of the **IL-6/gp130 family** (structural homology with IL-6, OSM, CNTF, LIF — all share four-helix-bundle topology with up-up-down-down connectivity)
- Three-dimensional structure: classic short-chain four-helix bundle (helices A, B, C, D); lacks a domain equivalent to the IL-6 receptor site III (which explains dependence on IL-31RA rather than gp130 for signaling); possesses both site I (IL-31RA interaction) and site II (OSMR interaction) epitopes
- No signal peptide cleavage product variation; secreted as a full-length glycoprotein; circulates as monomer; N-glycosylation at Asn96 stabilizes secretion

**Receptor complex:**
- **IL-31RA (IL-31 receptor alpha; gene *IL31RA*, chr5q11.2):** Type I cytokine receptor; single-pass TM; extracellular domain contains two cytokine-binding homology regions (CHR1 and CHR2) with conserved WSXWS motif; CHR2 binds IL-31 site I (high-affinity primary interaction; Kd ~20-50 pM); cytoplasmic tail has Box 1/Box 2 for JAK1 association; expression is highest on sensory neurons, keratinocytes, monocytes, and eosinophils
- **OSMR (oncostatin M receptor β; gene *OSMR*, chr5p13.1):** Shared with oncostatin M (OSM) signaling; recruited by IL-31RA after IL-31 binding → forms functional signaling dimer; cytoplasmic tail associates with JAK2
- **Signal transduction:** IL-31 → IL-31RA → OSMR recruitment → JAK1 (on IL-31RA) + JAK2 (on OSMR) trans-phosphorylation → **STAT3** (dominant; OSMR cytoplasmic Y819 is the primary STAT3 docking site) + **STAT5** (secondary via IL-31RA Y652/Y658) → nuclear translocation → gene transcription; also activates **PI3K/Akt → PDK1 → PKC** (survival/proliferation) and **ERK1/2 MAPK** (via SHC-Grb2-SOS → Ras)

**Nemolizumab (anti-IL-31RA):**
- IgG4 κ monoclonal antibody (Galderma/Sanofi); binds CHR2 of IL-31RA → prevents IL-31 interaction at site I → no receptor complex formation → no JAK-STAT signaling
- Dose: 30 mg (prurigo nodularis) or 60 mg (AD) SC Q4W; half-life ~21 days; FDA approved
- Mechanism advantage over anti-cytokine: IL-31RA blockade also prevents any endogenous IL-31 isoform variants from signaling; longer receptor occupancy

## Function

**Neurogenic itch mechanism:**
- Th2-skewed skin microenvironment (AD, PN, urticaria, cutaneous T-cell lymphoma) → IL-31 produced by Th2 cells and mast cells → IL-31 diffuses to dermis → binds **IL-31RA on TRPV1⁺/TRPA1⁺ C-fiber sensory neurons** in the dermis
- IL-31 → JAK1 → STAT3 in neurons → rapid depolarization (within minutes, before gene transcription) + **acute Ca²⁺ influx via TRPV1/TRPA1 channel sensitization** → action potential propagation along C-fibers → spinothalamic tract → somatosensory cortex + anterior cingulate cortex (emotional itch processing) → itch perception → scratching
- Long-term (hours-days): STAT3 nuclear signaling → TRPV1 upregulation, neuropeptide (CGRP, Substance P) expression → neurogenic inflammation → mast cell degranulation → further IL-31 release → itch-scratch-inflammation cycle
- **Pruriceptor sensitization:** IL-31 acts synergistically with IL-4 and IL-13 to upregulate TRPV1 and IL-31RA expression on sensory neurons, amplifying itch sensitivity; explains why dupilumab (anti-IL-4Rα) also reduces itch despite not directly targeting IL-31

**Keratinocyte effects:**
- IL-31 → IL-31RA on keratinocytes → STAT3 → ↑cytokine and chemokine production (CCL2, CCL17, CCL22, CXCL10) → Th2 and eosinophil recruitment → perpetuation of Th2 inflammation
- **Barrier function:** IL-31 → ↓filaggrin (FLG), ↓involucrin, ↓loricrin (epidermal differentiation complex) → skin barrier disruption → allergen penetration → IgE sensitization → further Th2 activation; part of the outside-in barrier disruption pathway
- **Inhibition of differentiation:** STAT3 → STAT3 target genes suppress late differentiation markers; IL-31-treated keratinocytes show features similar to psoriatic "suprabasal keratinocytes" — hyperproliferative and hypo-differentiated

**IL-31 regulation:**
- **Induction:** Th2 cell TCR activation + costimulation → IL-31 transcription (NFATc1, NF-κB, AP-1); TSLP + IL-4 → Th2 polarization → IL-31 production; Staphylococcus aureus superantigens (TSST-1, SEB) → Th2 TCR stimulation → rapid IL-31 surge; scratching itself (mechanical keratinocyte stress) → HMGB1 release → RAGE → IL-31 → itch cascade amplification
- **Seasonal variation:** Higher IL-31 serum levels in autumn/winter in AD patients (lower humidity → barrier disruption → S. aureus colonization → IL-31 surge); correlates with disease flares
- **Serum IL-31 as biomarker:** Elevated in AD, PN, cutaneous T-cell lymphoma (CTCL — Sézary syndrome), chronic idiopathic urticaria; correlates with EASI score and pruritus VAS in AD but with large individual variation; not routinely used clinically

## Mechanism

**Nemolizumab in Prurigo Nodularis [^stander-2020-nemolizumab-pn]:**
- **OLYMPIA 1 and OLYMPIA 2 (Phase 3):** ~450 patients each; moderate-to-severe PN (IGA ≥3; ≥20 nodules; NRS itch ≥7); nemolizumab 30 mg SC Q4W vs. placebo × 16 weeks
- **OLYMPIA 2 primary endpoints:**
  - IGA success (IGA 0/1 with ≥2-grade improvement): **26% vs. 0%** (p<0.001)
  - Pruritus NRS ≥4-point improvement: **58% vs. 16%** (p<0.001)
  - POEM-Q4W: itch reduction onset within 1 week; maintained through 24 weeks (OLE extension)
- **FDA approval:** August 2023; first drug approved specifically for prurigo nodularis
- Mechanism in PN: nodular skin in PN has enriched IL-31⁺ mast cells + Th22/Th2 infiltrate + dense sensory nerve network hyperinnervated with IL-31RA⁺ fibers; nemolizumab rapidly interrupts itch-scratch cycle → nodule resolution

**Nemolizumab in Atopic Dermatitis [^yosipovitch-2023-nemolizumab-ad]:**
- **ARCADIA 1 and ARCADIA 2 (Phase 3):** ~1,700 patients total; moderate-to-severe AD; nemolizumab 30 mg SC Q4W added to TCS vs. placebo + TCS
- **Endpoints at 16 weeks:**
  - IGA 0/1: ~36% vs. ~25% (significant in both trials)
  - EASI-75: ~45% vs. ~29%
  - Peak Pruritus NRS ≥4-point: ~50% vs. ~21%
- FDA approved for itch in AD (adults and adolescents ≥12 years); complement to dupilumab (which addresses inflammation and skin lesions; nemolizumab adds specific itch targeting)
- **Differentiation from dupilumab:** Nemolizumab targets the neuro-immune itch axis; dupilumab targets inflammation and barrier; patients on dupilumab with residual pruritus may benefit from addition of nemolizumab (combination not yet approved)

**IL-31 in other conditions:**
- **CTCL (Sézary syndrome):** Malignant Th2/Th22 cells produce IL-31 → severe refractory pruritus; elevated serum IL-31 in Sézary correlates with disease activity; nemolizumab under study
- **Chronic idiopathic urticaria:** IL-31 contributes to itch in IgE-independent urticaria; not currently a treatment target
- **Alopecia areata:** Some evidence for IL-31 contribution to scalp itch in AA; under investigation

## Connections

IL-31 is the dominant itch cytokine in AD; elevated in lesional skin and serum correlating with pruritus VAS; IL-31 from Th2 cells/mast cells → IL-31RA on sensory DRG neurons → JAK1 → TRPV1/TRPA1 sensitization; nemolizumab (anti-IL-31RA) reduces AD itch 60% vs. 20% placebo.

IL-31 is a key mediator of PN pruritus; mast cells and Th2 cells in PN nodules produce IL-31 → sensory nerve IL-31RA → itch-scratch cycle; nemolizumab 60 mg SC Q4W reduced IGA success 26% vs. 0% placebo at 16 weeks (OLYMPIA 2, FDA approved Aug 2023).

IL-4 promotes Th2 differentiation and IL-31 production; IL-4 + IL-13 downregulate FLG in keratinocytes → barrier disruption → sensitization to IL-31 signaling; dupilumab (anti-IL-4Rα) indirectly reduces IL-31 by suppressing Th2 environment driving IL-31 production.

[^dillon-2004-il-31]: Dillon SR, Sprecher C, Hammond A, et al. Interleukin 31, a cytokine produced by activated T cells, induces dermatitis in mice. *Nat Immunol.* 2004;5(7):752-760. [doi:10.1038/ni1084](https://doi.org/10.1038/ni1084) · [PubMed 15184896](https://pubmed.ncbi.nlm.nih.gov/15184896/)
[^stander-2020-nemolizumab-pn]: Ständer S, Yosipovitch G, Legat FJ, et al. Trial of nemolizumab in moderate-to-severe prurigo nodularis. *N Engl J Med.* 2020;382(8):706-716. [doi:10.1056/NEJMoa1908316](https://doi.org/10.1056/NEJMoa1908316) · [PubMed 32053299](https://pubmed.ncbi.nlm.nih.gov/32053299/)
[^yosipovitch-2023-nemolizumab-ad]: Yosipovitch G, Ständer S, Kerby MB, et al. Nemolizumab in patients with moderate-to-severe atopic dermatitis: randomized, phase 3, ARCADIA 1 and ARCADIA 2 trials. *J Am Acad Dermatol.* 2023;89(1):38-49. [doi:10.1016/j.jaad.2023.01.006](https://doi.org/10.1016/j.jaad.2023.01.006) · [PubMed 36669666](https://pubmed.ncbi.nlm.nih.gov/36669666/)
