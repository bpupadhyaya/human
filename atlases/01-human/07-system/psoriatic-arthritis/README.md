---
schema: human-scale-entry/v1
id: psoriatic-arthritis
name: Psoriatic Arthritis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Seronegative inflammatory arthritis in ~30% of psoriasis patients; 5 clinical patterns; CASPAR criteria. Driven by IL-17A, IL-23, TNF-α, and IL-36 axes targeting skin, entheses, and joints. Approved biologics: anti-TNF, anti-IL-17A, anti-IL-23, anti-IL-12/23, JAK/TYK2 inhibitors."
aliases: ["PsA", "psoriatic spondylitis", "psoriatic spondyloarthritis"]
sources:
  - id: ritchlin-2017-psa-review
    type: peer-reviewed
    cite: "Ritchlin CT, Colbert RA, Gladman DD. Psoriatic arthritis. N Engl J Med. 2017;376(10):957-970."
    doi: "10.1056/NEJMra1505557"
    pmid: "28273019"
  - id: mease-2015-secukinumab-psa-future2
    type: peer-reviewed
    cite: "Mease PJ, McInnes IB, Kirkham B, et al. Secukinumab inhibition of interleukin-17A in patients with psoriatic arthritis. N Engl J Med. 2015;373(14):1329-1339."
    doi: "10.1056/NEJMoa1503317"
    pmid: "26422723"
  - id: deodhar-2020-guselkumab-discover1
    type: peer-reviewed
    cite: "Deodhar A, Helliwell PS, Boehncke WH, et al. Guselkumab in patients with active psoriatic arthritis who were biologic-naive or had previously received TNFalpha inhibitor treatment (DISCOVER-1). Lancet. 2020;395(10230):1115-1125."
    doi: "10.1016/S0140-6736(20)30263-4"
    pmid: "32178765"
  - id: gladman-2005-caspar-criteria
    type: peer-reviewed
    cite: "Taylor W, Gladman D, Helliwell P, et al. Classification criteria for psoriatic arthritis: development of new criteria from a large international study. Arthritis Rheum. 2006;54(8):2665-2673."
    doi: "10.1002/art.21972"
    pmid: "16871531"
cross_links:
  - target: 01-human/03-molecular/il-36
    relation: modulated-by
    note: "IL-36α/β/γ overexpressed in PsA skin and synovium → NF-κB → IL-6/CXCL8/CCL20 → neutrophil and DC recruitment at entheses; IL36RN mutations link GPP to PsA; spesolimab (anti-IL-36R; FDA 2022) under investigation in PsA."
  - target: 01-human/03-molecular/il-17a
    relation: modulated-by
    note: "IL-17A drives PsA enthesitis, synovitis, and new bone formation; secukinumab (FUTURE 2: ACR20 54% vs 15%; FDA 2016) and ixekizumab (SPIRIT-P1/2) are approved; entheseal ILC3 produce IL-17A independently of IL-23 in some PsA patients."
  - target: 01-human/03-molecular/il-23
    relation: modulated-by
    note: "IL-23 drives the Th17/IL-17A axis in PsA skin and entheses; guselkumab (DISCOVER-1/2: ACR20 ~59-64%; FDA 2020) and risankizumab (KEEPsAKE; FDA 2022) are approved; ustekinumab (anti-p40) targets both IL-12 and IL-23 in PsA and psoriasis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: modulated-by
    note: "TNF-α drives PsA synovitis, enthesitis, and structural damage; adalimumab, certolizumab (RAPID-PsA: ACR20 58% vs 24%; FDA 2013), etanercept, golimumab, and infliximab are approved; TNF + IL-36 co-activation amplifies synovial inflammation."
  - target: 01-human/03-molecular/hla-b27
    relation: connects-to
    note: "HLA-B27 in ~20% of PsA overall but ~60-70% with axial PsA; axial PsA shares sacroiliitis with axSpA; HLA-C*06:02 is primary genetic risk for cutaneous psoriasis and polyarticular PsA; ERAP1 epistasis with HLA-B27 modulates axial risk."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "Axial PsA and AS share HLA-B27, sacroiliitis, and IL-17A/TNF-α pathobiology; distinguished by psoriasis, DIP involvement, and asymmetric new bone formation (periostitis); anti-IL-17A and anti-TNF are effective across both spondyloarthropathies."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "PsA occurs in ~30% of plaque psoriasis patients; skin disease severity (PASI) often precedes joint involvement by ~10 years; shared IL-17A/IL-23 pathobiology explains why biologics effective in psoriasis (PASI 90/100 endpoints) also treat PsA."
---

# Psoriatic Arthritis

## Overview

Psoriatic arthritis (PsA) is a chronic, seronegative inflammatory arthritis occurring in approximately 30% of patients with psoriasis, affecting roughly 0.3–1% of the general population [^ritchlin-2017-psa-review]. It is classified within the **spondyloarthropathies (SpA)** alongside ankylosing spondylitis, reactive arthritis, and IBD-associated arthritis, unified by enthesitis as a central pathologic process. PsA is clinically heterogeneous, affecting peripheral joints, spine, entheses, tendons, and nails, with wide variation among patients and over time within individuals.

The molecular drivers — IL-17A, IL-23, TNF-α, and IL-36 — connect PsA to psoriatic skin disease and explain why drugs targeting these pathways benefit both cutaneous and articular manifestations simultaneously. Genetic susceptibility involves **HLA-C*06:02** (cutaneous psoriasis) and **HLA-B27** (axial involvement), reinforcing its spondyloarthropathic biology [^gladman-2005-caspar-criteria].

## Structure

Moll and Wright (1973) described five clinical subtypes; modern data show patients transition between patterns over time:

| Pattern | Frequency | Characteristics |
|:--------|:----------|:----------------|
| Oligoarticular asymmetric | ~30–50% | <5 joints, large and small; often hand + knee |
| Polyarticular symmetric | ~30–40% | ≥5 joints; resembles RA but RF-negative |
| Distal interphalangeal (DIP) predominant | ~5–10% | DIP joints + nail disease; uncommon in RA |
| Axial | ~5% isolated; ~40–50% have some axial | Sacroiliitis and spondylitis; HLA-B27-associated |
| Arthritis mutilans | ~5% | Severe osteolysis; telescoping "opera-glass" deformities |

**Dactylitis** ("sausage digit") — diffuse flexor tenosynovitis + joint and periarticular edema — is a characteristic feature of PsA (and reactive arthritis) not seen in RA.

**Enthesitis** is the primary pathological lesion: insertion-site inflammation at Achilles tendon, plantar fascia, patellar tendon, iliac crest, and vertebral endplates.

## Function

PsA impairs musculoskeletal function through three parallel processes:

1. **Synovitis and joint destruction** — pannus formation with FLS proliferation and MMPs → cartilage degradation; structural damage (erosions + new bone) progressively restricts range of motion, particularly in DIP joints (pencil-in-cup), wrists, and sacroiliac joints in axial disease.

2. **Enthesitis** — inflammation at tendon and ligament insertion sites causes pain with activity, morning stiffness, and impaired ambulation (Achilles, plantar fascia) or reduced grip strength; entheseal new bone (enthesophytes) may fuse joints in advanced disease.

3. **Systemic inflammatory burden** — sustained IL-17A/TNF-α-driven inflammation → accelerated atherosclerosis, metabolic syndrome (insulin resistance, obesity, dyslipidemia), and elevated cardiovascular mortality independent of traditional risk factors. Fatigue is a major functional impairment driven by systemic inflammation and sleep disruption.

The combined skin, nail, joint, and entheseal burden produces substantial quality-of-life impairment (HAQ-DI, DLQI); MDA (Minimal Disease Activity) is the validated treat-to-target endpoint capturing multiple domains simultaneously.

## Diagnosis — CASPAR Criteria

The **Classification Criteria for Psoriatic Arthritis (CASPAR)** require inflammatory musculoskeletal disease + ≥3 points from:

| Feature | Points |
|:--------|:-------|
| Current psoriasis | 2 |
| Personal history of psoriasis (if no current) | 1 |
| Family history of psoriasis (if no current/personal) | 1 |
| Psoriatic nail dystrophy | 1 |
| Negative RF | 1 |
| Current dactylitis or history of dactylitis (documented by rheumatologist) | 1 |
| Juxta-articular new bone formation on X-ray | 1 |

Sensitivity 91.4%, specificity 98.7% for PsA vs. other inflammatory arthritis [^gladman-2005-caspar-criteria].

### Laboratory and Imaging

- **Seronegative**: RF and anti-CCP negative (CCP positive in ~8–15% — associated with erosive disease)
- **Acute-phase reactants**: CRP/ESR elevated in active disease, but may be normal in purely oligoarticular disease
- **HLA typing**: HLA-B27 (axial PsA), HLA-C*06:02 (skin/polyarticular)
- **Plain radiographs**: Erosions (joint margin and central) + **periostitis** and **new bone formation** (distinguishes from RA); DIP: "pencil-in-cup" deformity in arthritis mutilans
- **MRI**: STIR for bone marrow edema at entheses and sacroiliitis; SPARCC scoring of sacroiliitis
- **Ultrasound**: Power Doppler for entheseal blood flow (enthesophytes, bursitis, erosions)

### Disease Activity Measures

| Tool | Measures |
|:-----|:---------|
| DAPSA (Disease Activity in PsA) | TJC28 + SJC28 + patient global + pain VAS + CRP |
| MDA (Minimal Disease Activity) | 7 criteria; 5/7 = MDA (treatment target) |
| PASI | Psoriasis Area and Severity Index (skin) |
| NAPSI | Nail Psoriasis Severity Index |
| LEI | Leeds Enthesitis Index (6 sites) |
| LEDI | Leeds Dactylitis Index |

## Pathology

### Immunopathogenesis

PsA shares enthesitis biology with AS but is distinguished by its obligate cutaneous psoriasis connection. The current model invokes:

1. **Psoriatic skin as the initiating immune niche** — IL-36, IL-17A, and TNF-α produced by skin-resident DCs, Th17, and keratinocytes enter circulation and are amplified at mechanical stress sites (entheses)
2. **Enthesitis** — IL-23 from resident myeloid cells activates entheseal ILC3 → IL-17A + IL-22 → local bone remodeling; CD8+ T cells predominate (unlike RA which is CD4+)
3. **Synovitis** — prominent **neoangiogenesis** (VEGF-driven) and CD68+ macrophage accumulation; TNF-α drives synoviocyte proliferation and MMPs
4. **New bone formation** — paradoxical coexistence of erosion and new bone (osteoproliferation); Wnt signaling (DKK1 downregulation), BMP pathway → syndesmophytes and enthesophytes; IL-17A drives RANKL → osteoclast-mediated erosion

### Genetics

- **HLA-C*06:02**: Strongest genetic risk for plaque psoriasis and polyarticular PsA
- **HLA-B27**: ~20% of all PsA; ~60–70% in axial PsA (but lower than AS where ~90%+ are B27+)
- **HLA-B38, B39**: Associated with polyarticular erosive PsA
- **IL23R, IL12B, TNFAIP3, TRAF3IP2 (act1)**: GWAS-confirmed non-HLA risk loci shared with psoriasis and/or AS
- **ERAP1**: Epistatic with HLA-B27 in axial PsA (same as in AS)

### Extra-articular Features

| Feature | Frequency |
|:--------|:----------|
| Psoriasis (prerequisite or history) | 100% |
| Nail disease (pitting, onycholysis, oil drop sign) | 80–90% |
| Uveitis (anterior; less common than in AS) | 7–20% |
| IBD (Crohn's, UC) | 3–5% |
| Metabolic syndrome, cardiovascular comorbidity | Increased |

## Treatment

### Treat-to-Target

Target: **MDA (Minimal Disease Activity)** — simultaneously achieving low disease burden across TJC, SJC, PASI, pain, patient global, HAQ, and enthesitis. TICOPA trial demonstrated superiority of tight MDA-targeted control vs. standard care.

### Stepwise Approach

**Step 1 — NSAIDs + local therapy**
Naproxen, diclofenac, or celecoxib for enthesitis pain; intra-articular corticosteroids for active joints; topical agents for skin.

**Step 2 — Conventional DMARDs**
- **Methotrexate (MTX)**: effective for skin and peripheral joint disease; **no proven effect on axial disease or radiographic progression**
- **Leflunomide**: alternative to MTX; moderate effect on peripheral joints
- **Apremilast** (PDE4 inhibitor): oral small molecule; PALACE trials; moderate efficacy for skin, joints, dactylitis, enthesitis; no DMARD bridging concerns

**Step 3 — Biologics**

*Anti-TNF (first-line biologic, highest-quality evidence):*
- Adalimumab (ADEPT trial: ACR20 58% vs 14%; FDA 2005)
- Etanercept (PsARC response; FDA 2002)
- Certolizumab pegol (RAPID-PsA: ACR20 58% vs 24%; FDA 2013)
- Golimumab (GO-REVEAL trial; FDA 2009)
- Infliximab (IMPACT-2; FDA 2004)

*Anti-IL-17A:*
- **Secukinumab** — **FUTURE 2** (N=397): ACR20 **54%** vs **15%** placebo; MDA 36% vs 9% at wk 24; radiographic progression inhibition; **FDA January 2016** [^mease-2015-secukinumab-psa-future2]
- **Ixekizumab** — SPIRIT-P1 (biologic-naive) and SPIRIT-P2 (TNFi-experienced): ACR50 ~34% and ~25%; FDA 2017

*Anti-IL-23p19:*
- **Guselkumab** — DISCOVER-1 (biologic-naive and TNFi-experienced): ACR20 **59%** vs **22%**; MDA 27% vs 11% at wk 24; FDA 2020 [^deodhar-2020-guselkumab-discover1]
- **Risankizumab** — KEEPsAKE-1/2 trials: ACR20 ~57% vs 33%; FDA 2022
- **Ustekinumab** (anti-IL-12/23 p40) — PSUMMIT-1/2: ACR20 42–43% vs 20–23%; FDA 2013

*JAK inhibitors (oral):*
- **Tofacitinib** (JAK1/3): OPAL Broaden/Beyond: ACR20 ~50% vs 33%; FDA 2017
- **Upadacitinib** (JAK1-selective): SELECT-PsA-1/2: ACR20 71% vs 36%; FDA 2021
- **Filgotinib** (JAK1): European approval 2024

*TYK2 inhibitor:*
- **Deucravacitinib** — POETYK PsA-1/2 (Phase 3): ACR20 ~52–53% vs ~30–32%; data emerging for PsA; already FDA-approved for plaque psoriasis (September 2022)

### Anti-IL-23 Paradox in SpA

Risankizumab (anti-IL-23p19) **failed primary endpoints** in the SURPASS trial for AS — contrasting with its PsA efficacy. This demonstrates divergent IL-23 dependence: entheseal ILC3 in AS/axial SpA produce IL-17A independently of IL-23 via alternative stimuli, while in PsA skin and peripheral joints the IL-23 → Th17 axis is more dominant.

## Connections

- **Modulated by** → **[IL-36](../../03-molecular/il-36/README.md)** — IL-36α/β/γ overexpressed in PsA skin and synovium → NF-κB → IL-6/CXCL8/CCL20 → neutrophil and DC recruitment at entheses; IL36RN mutations link GPP to PsA; spesolimab under investigation.
- **Modulated by** → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A drives PsA enthesitis, synovitis, and new bone formation; secukinumab and ixekizumab are approved; entheseal ILC3 produce IL-17A independently of IL-23 in some PsA patients.
- **Modulated by** → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 drives Th17/IL-17A axis in PsA skin and entheses; guselkumab and risankizumab are approved; ustekinumab (anti-p40) targets IL-12 and IL-23 in PsA and psoriasis.
- **Modulated by** → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α drives synovitis, enthesitis, and structural damage; multiple anti-TNF agents are first-line biologics in PsA; co-activation with IL-36 amplifies synovial inflammation.
- `connects-to` → **[HLA-B27](../../03-molecular/hla-b27/README.md)** — HLA-B27 in ~20% of PsA overall, ~60–70% with axial PsA; HLA-C*06:02 is primary risk allele for psoriasis/polyarticular PsA; ERAP1 epistasis modulates axial PsA risk.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — Axial PsA and AS share HLA-B27, sacroiliitis, and IL-17A/TNF-α pathobiology; distinguished by psoriasis, DIP involvement, and asymmetric periostitis; anti-IL-17A and anti-TNF effective in both.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — PsA occurs in ~30% of psoriasis patients; skin disease often precedes joints by ~10 years; shared IL-17A/IL-23 biology explains why biologics achieving PASI 90/100 in psoriasis also treat PsA joints.

[^ritchlin-2017-psa-review]: Ritchlin CT, Colbert RA, Gladman DD. Psoriatic arthritis. *N Engl J Med.* 2017;376(10):957-970. [doi:10.1056/NEJMra1505557](https://doi.org/10.1056/NEJMra1505557) · [PubMed 28273019](https://pubmed.ncbi.nlm.nih.gov/28273019/)
[^mease-2015-secukinumab-psa-future2]: Mease PJ, et al. Secukinumab inhibition of interleukin-17A in patients with psoriatic arthritis. *N Engl J Med.* 2015;373(14):1329-1339. [doi:10.1056/NEJMoa1503317](https://doi.org/10.1056/NEJMoa1503317) · [PubMed 26422723](https://pubmed.ncbi.nlm.nih.gov/26422723/)
[^deodhar-2020-guselkumab-discover1]: Deodhar A, et al. Guselkumab in patients with active psoriatic arthritis (DISCOVER-1). *Lancet.* 2020;395(10230):1115-1125. [doi:10.1016/S0140-6736(20)30263-4](https://doi.org/10.1016/S0140-6736(20)30263-4) · [PubMed 32178765](https://pubmed.ncbi.nlm.nih.gov/32178765/)
[^gladman-2005-caspar-criteria]: Taylor W, et al. Classification criteria for psoriatic arthritis. *Arthritis Rheum.* 2006;54(8):2665-2673. [doi:10.1002/art.21972](https://doi.org/10.1002/art.21972) · [PubMed 16871531](https://pubmed.ncbi.nlm.nih.gov/16871531/)
