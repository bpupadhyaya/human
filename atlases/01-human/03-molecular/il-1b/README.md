---
schema: human-scale-entry/v1
id: il-1b
name: IL-1β
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-1β (IL1B; chr2q14.1) is a pro-inflammatory cytokine processed by NLRP3 inflammasome/caspase-1; signals via IL-1R1→NF-κB driving fever, acute-phase response, and synovitis. Approved blockers: anakinra (FDA 2001), canakinumab (FDA 2013), rilonacept (FDA 2021)."
aliases: ["IL-1β", "IL-1 beta", "interleukin-1 beta", "IL1B", "IL-1b", "anakinra target", "canakinumab target", "rilonacept target"]
sources:
  - id: dinarello-2018-il1-review
    type: peer-reviewed
    cite: "Dinarello CA. Overview of the IL-1 family in innate inflammation and acquired immunity. Immunol Rev. 2018;281(1):8-27."
    doi: "10.1111/imr.12621"
    pmid: "29247995"
    url: "https://doi.org/10.1111/imr.12621"
  - id: ridker-2017-cantos
    type: peer-reviewed
    cite: "Ridker PM, Everett BM, Thuren T, et al. Antiinflammatory therapy with canakinumab for atherosclerotic disease. N Engl J Med. 2017;377(12):1119-1131."
    doi: "10.1056/NEJMoa1707914"
    pmid: "28845751"
    url: "https://doi.org/10.1056/NEJMoa1707914"
  - id: klein-2021-rhapsody-rilonacept
    type: peer-reviewed
    cite: "Klein AL, Imazio M, Cremer P, et al. Phase 3 trial of interleukin-1 trap rilonacept in recurrent pericarditis. N Engl J Med. 2021;384(1):31-41."
    doi: "10.1056/NEJMoa2027892"
    pmid: "33405895"
    url: "https://doi.org/10.1056/NEJMoa2027892"
cross_links:
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "NLRP3 inflammasome (NLRP3+ASC+caspase-1) is the primary activator of IL-1β; NLRP3 activated by urate crystals, Ca²⁺ pyrophosphate, cholesterol, and ATP → caspase-1 cleaves pro-IL-1β (31 kDa) → active IL-1β (17.5 kDa) → secretion via gasdermin D pores → pyroptosis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "IL-1β signals via IL-1R1/IL-1RAP→MyD88→IRAK4→TRAF6→IKK→NF-κB → IL-6, TNF-α, COX-2, MMP transcription; NF-κB also drives IL-1β and NLRP3 expression creating amplification loops; NF-κB activation is the dominant downstream signaling arm of IL-1R1 in synovitis and fever."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-1β stimulates IL-6 production from macrophages and endothelial cells → acute-phase response (CRP, SAA), fever, and further NF-κB amplification; IL-1β and IL-6 co-drive vascular inflammation in GCA; targeting both (canakinumab + tocilizumab) is under investigation."
  - target: 01-human/07-system/giant-cell-arteritis
    relation: connects-to
    note: "IL-1β produced by activated macrophages in the arterial wall drives vascular NF-κB activation in GCA; anakinra and canakinumab (IL-1 blockers) are in Phase 2/3 investigation for GCA as steroid-sparing agents alongside the approved tocilizumab strategy."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "MSU crystals in gout activate NLRP3 inflammasome → caspase-1 cleaves pro-IL-1β → neutrophil influx → acute gouty arthritis; canakinumab (anti-IL-1β; EMA approved 2013 for gout flares) demonstrates IL-1β as a therapeutic target in crystal-induced arthropathy."
---

# IL-1β

## Overview

**Interleukin-1 beta (IL-1β; gene *IL1B*, chromosome 2q14.1)** is a **pleiotropic pro-inflammatory cytokine** of the IL-1 superfamily and one of the most potent mediators of innate immune activation in human biology [^dinarello-2018-il1-review]. Originally described as "endogenous pyrogen," IL-1β orchestrates the acute-phase response, drives fever, recruits neutrophils, and initiates the synovial inflammation of arthritis.

IL-1β is produced as an inactive **precursor (pro-IL-1β; 31 kDa)** that lacks a signal peptide and cannot be secreted via the conventional ER–Golgi pathway. Bioactivation requires two sequential signals:

1. **Signal 1 (priming):** TLR/NF-κB → *IL1B* transcription → pro-IL-1β accumulates intracellularly
2. **Signal 2 (activation):** Danger signal → NLRP3 inflammasome assembly → caspase-1 cleavage of pro-IL-1β → **mature IL-1β (17.5 kDa)** → secreted via gasdermin D pores

This two-signal requirement functions as a safety mechanism, preventing inadvertent IL-1β release in sterile tissues.

**Clinical significance:**
- **Autoinflammatory diseases (CAPS, TRAPS, FMF, DIRA):** gain-of-function NLRP3 or IL-1 pathway mutations → unchecked IL-1β → periodic fever, rash, serositis
- **Adult-onset Still's disease (AOSD):** elevated serum IL-1β; anakinra highly effective first-line
- **Gout/CPPD:** crystal-driven NLRP3 activation → IL-1β → acute arthritis
- **Atherosclerosis:** CANTOS trial (canakinumab → 15% MACE reduction independent of LDL lowering) [^ridker-2017-cantos]
- **Giant cell arteritis:** IL-1β + IL-6 drive granulomatous vascular inflammation
- **Recurrent pericarditis:** RHAPSODY trial (rilonacept; 96% recurrence reduction; FDA Mar 2021) [^klein-2021-rhapsody-rilonacept]

## Structure

### IL-1β protein architecture

| Feature | Detail |
|:--------|:-------|
| Gene | *IL1B*, chromosome 2q14.1; ~7.8 kb, 7 exons |
| Precursor | Pro-IL-1β: 269 aa, 31 kDa; no signal peptide |
| Mature form | 153 aa, 17.5 kDa; bioactive after caspase-1 cleavage at Asp116–Ala117 |
| Structure | 12-stranded β-trefoil fold; no disulfide bonds; Ca²⁺-independent |
| IL-1 family | Shares β-trefoil fold with IL-1α, IL-18, IL-33, IL-36α/β/γ, IL-37, IL-38 |

### IL-1R1 receptor complex

IL-1β signals through a trimeric surface receptor complex:

- **IL-1R1** (primary signaling receptor): type I transmembrane; three extracellular immunoglobulin-like domains bind IL-1β; intracellular TIR domain recruits MyD88
- **IL-1RAP (IL-1R3)** (co-receptor): recruited after IL-1β binds IL-1R1 → forms the signaling-competent heterodimer; IL-1RAP TIR domain is essential for downstream IRAK activation
- **IL-1R2** (decoy receptor): binds IL-1β with high affinity but lacks intracellular signaling domain → sequesters IL-1β; shed as soluble IL-1R2 after neutrophil activation
- **IL-1Ra** (IL-1 receptor antagonist): endogenous competitive inhibitor; occupies IL-1R1 without recruiting IL-1RAP → blocks IL-1β signaling; serum IL-1Ra constitutes the natural IL-1β brake; anakinra = recombinant IL-1Ra

### Endogenous regulation

| Regulator | Mechanism | Clinical relevance |
|:---------|:----------|:-----------------|
| IL-1Ra | Competes with IL-1β for IL-1R1; no agonist activity | Basis for anakinra (recombinant IL-1Ra; FDA 2001) |
| IL-1R2 (decoy) | Soluble + membrane-bound; binds IL-1β → prevents IL-1R1 engagement | Anti-inflammatory after neutrophil activation |
| IL-10 | Suppresses NLRP3 expression and NF-κB; reduces pro-IL-1β synthesis | Therapeutic target in inflammatory contexts |
| Caspase-1 inhibitor | Blocks caspase-1 → prevents pro-IL-1β cleavage | Belnacasan (VX-765) in clinical trials |

## Function

### Systemic actions of IL-1β

IL-1β acts locally (paracrine) and systemically (endocrine at high concentrations):

**Fever:** IL-1β crosses the blood-brain barrier at the organum vasculosum of the lamina terminalis (OVLT) → hypothalamic COX-2 → PGE2 → EP3R on thermoregulatory neurons → fever (pyrogen response); blocked by NSAIDs/aspirin via COX inhibition.

**Neutrophil mobilization:** IL-1β → bone marrow stromal CXCL12 reduction + CXCL8 induction → neutrophil egress from marrow → circulating neutrophilia within hours of infection.

**Acute-phase response:** IL-1β + IL-6 → hepatocyte STAT3 + NF-κB → CRP, serum amyloid A (SAA), fibrinogen, hepcidin, complement proteins → systemic biomarkers of inflammation elevated (ESR, CRP).

**Endothelial activation:** IL-1β → NF-κB in endothelial cells → E-selectin, VCAM-1, ICAM-1 upregulation → leukocyte rolling/adhesion/diapedesis → local amplification of inflammation.

**Cartilage/bone destruction:** IL-1β → chondrocyte MMPs (MMP-1, -3, -13) → cartilage matrix degradation; → osteoclast RANKL induction → bone resorption; dominant cytokine in acute joint destruction in RA, gout flares, and seronegative arthritis.

### NLRP3 inflammasome activation signals

| Signal type | Examples | Disease context |
|:-----------|:---------|:---------------|
| Crystalline | Monosodium urate (MSU), Ca²⁺ pyrophosphate, cholesterol crystals | Gout, CPPD, atherosclerosis |
| Pathogen-derived | ATP (via P2X7), flagellin, pore-forming toxins | Sepsis, bacterial infection |
| Genetic (GOF) | NLRP3 gain-of-function mutations | CAPS (MWS, FCAS, NOMID): cryopyrin disease |
| Metabolic | Saturated fatty acids, hyperglycemia, amyloid (IAPP in islets) | Type 2 diabetes, NASH |
| Cold/mechanical | Cold temperature → NLRP3 in FCAS | Cold-contact urticaria in CAPS |

## Mechanism

### Therapeutic IL-1 blockade

**Anakinra (Kineret; Swedish Orphan Biovitrum):**
- Recombinant IL-1Ra (glycosylated; 153 aa + N-terminal Met); blocks IL-1R1 competitively; no agonist activity
- Half-life: ~4-6 h → daily subcutaneous injection required (pharmacokinetic limitation)
- FDA approved November 2001 for moderate-severe RA; widely used off-label: AOSD, CAPS, COVID-19 cytokine storm, macrophage activation syndrome (MAS), recurrent pericarditis, DIRA (IL-1Ra deficiency)
- Key advantage: rapid offset allows dose adjustment; preferred in acute critical settings

**Canakinumab (Ilaris; Novartis):**
- Fully human anti-IL-1β IgG1κ; high-affinity neutralization of free IL-1β (Kd ~300 fM)
- Half-life: ~26 days → monthly or Q8W SC injection
- FDA approved: CAPS (Jun 2009 pediatric / 2013 adult); SJIA (May 2013); TRAPS/HIDS/FMF (2016); AOSD (2020)
- **CANTOS trial** (N=10,061; post-MI, hsCRP ≥2 mg/L; canakinumab 150 mg Q3M vs. placebo): 15% MACE reduction (HR 0.85; p=0.021); hsCRP reduced ~37%; lung cancer mortality reduced 67% (post-hoc) — demonstrates IL-1β as a cardiovascular target [^ridker-2017-cantos]

**Rilonacept (Arcalyst; Kiniksa):**
- Dimeric fusion protein: IL-1R1 ECD + IL-1RAP ECD fused to IgG1 Fc ("IL-1 Trap"); captures IL-1β, IL-1α, and IL-1Ra
- FDA approved: CAPS (Feb 2008); recurrent pericarditis (Mar 2021)
- **RHAPSODY trial** (N=86; rilonacept vs. placebo; recurrent pericarditis): 96% relative risk reduction in pericarditis recurrence; time to first recurrence: not reached vs. 8.6 weeks (p<0.001) [^klein-2021-rhapsody-rilonacept]

## Connections

- `connects-to` → **[NLRP3 Inflammasome](../nlrp3-inflammasome/README.md)** — NLRP3 inflammasome (NLRP3+ASC+caspase-1) is the primary activator of IL-1β; NLRP3 activated by urate crystals, Ca²⁺ pyrophosphate, cholesterol, and ATP → caspase-1 cleaves pro-IL-1β (31 kDa) → active IL-1β (17.5 kDa) → secretion via gasdermin D pores → pyroptosis.
- `connects-to` → **[NF-κB](../nf-kb/README.md)** — IL-1β signals via IL-1R1/IL-1RAP→MyD88→IRAK4→TRAF6→IKK→NF-κB → IL-6, TNF-α, COX-2, MMP transcription; NF-κB also drives IL-1β and NLRP3 expression creating amplification loops; NF-κB activation is the dominant downstream signaling arm of IL-1R1 in synovitis and fever.
- `connects-to` → **[IL-6](../il-6/README.md)** — IL-1β stimulates IL-6 production from macrophages and endothelial cells → acute-phase response (CRP, SAA), fever, and further NF-κB amplification; IL-1β and IL-6 co-drive vascular inflammation in GCA; targeting both (canakinumab + tocilizumab) is under investigation.
- `connects-to` → **[Giant Cell Arteritis](../../07-system/giant-cell-arteritis/README.md)** — IL-1β produced by activated macrophages in the arterial wall drives vascular NF-κB activation in GCA; anakinra and canakinumab (IL-1 blockers) are in Phase 2/3 investigation for GCA as steroid-sparing agents alongside the approved tocilizumab strategy.
- `connects-to` → **[Gout](../../07-system/gout/README.md)** — MSU crystals in gout activate NLRP3 inflammasome → caspase-1 cleaves pro-IL-1β → neutrophil influx → acute gouty arthritis; canakinumab (anti-IL-1β; EMA approved 2013 for gout flares) demonstrates IL-1β as a therapeutic target in crystal-induced arthropathy.

[^dinarello-2018-il1-review]: Dinarello CA. Overview of the IL-1 family in innate inflammation and acquired immunity. *Immunol Rev.* 2018;281(1):8-27. [doi:10.1111/imr.12621](https://doi.org/10.1111/imr.12621) · [PubMed 29247995](https://pubmed.ncbi.nlm.nih.gov/29247995/)
[^ridker-2017-cantos]: Ridker PM, Everett BM, Thuren T, et al. Antiinflammatory therapy with canakinumab for atherosclerotic disease. *N Engl J Med.* 2017;377(12):1119-1131. [doi:10.1056/NEJMoa1707914](https://doi.org/10.1056/NEJMoa1707914) · [PubMed 28845751](https://pubmed.ncbi.nlm.nih.gov/28845751/)
[^klein-2021-rhapsody-rilonacept]: Klein AL, Imazio M, Cremer P, et al. Phase 3 trial of interleukin-1 trap rilonacept in recurrent pericarditis. *N Engl J Med.* 2021;384(1):31-41. [doi:10.1056/NEJMoa2027892](https://doi.org/10.1056/NEJMoa2027892) · [PubMed 33405895](https://pubmed.ncbi.nlm.nih.gov/33405895/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
