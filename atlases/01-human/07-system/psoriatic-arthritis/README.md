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
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Psoriatic arthritis grows out of psoriasis: ~30% of psoriasis patients develop it, usually years after the skin disease, and both run on the same IL-23/IL-17 axis — why biologics that clear psoriatic plaques (anti-IL-17, anti-IL-23) also treat the joints."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Psoriatic arthritis attacks the musculoskeletal system distinctively: asymmetric oligoarthritis, distal interphalangeal disease, enthesitis, dactylitis ('sausage digit'), and sacroiliitis — combining erosion with new bone formation, unlike the pure erosion of RA."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Psoriatic arthritis is driven by Th17 helper T cells: IL-23 expands IL-17-producing CD4+ T cells (and innate IL-17 at entheses) that activate neutrophils and osteoclasts — driving inflammation, erosion, and new-bone formation, the rationale for anti-IL-17/IL-23 biologics."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Psoriatic and rheumatoid arthritis are the two major chronic inflammatory arthritides but differ: PsA is a seronegative spondyloarthropathy with enthesitis, dactylitis, DIP involvement, and psoriasis, while RA is a symmetric, RF/anti-CCP-positive synovitis sparing the DIP joints."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Psoriatic arthritis and gout can mimic and coexist: high cell turnover in psoriasis raises uric acid, so PsA patients get gout more often, and an acutely swollen toe (dactylitis vs podagra) may need joint aspiration to tell crystal arthritis from psoriatic disease."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Psoriatic arthritis uniquely combines bone erosion and new bone formation: TNF and IL-17 drive osteoclasts to erode joints (pencil-in-cup deformity) while stimulating osteoblasts to build syndesmophytes and enthesophytes—a remodeling signature distinct from RA."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Psoriatic arthritis and IBD belong to the same IL-23/Th17 spondyloarthritis family: both share gut-skin-joint inflammation and respond to IL-23 and TNF blockers—though IL-17 inhibitors that help PsA can paradoxically worsen IBD."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Psoriatic arthritis is strongly tied to obesity: adipose tissue is pro-inflammatory (TNF, IL-6, leptin), raising PsA risk and severity and blunting response to therapy, while weight loss improves disease control—so PsA is as much a metabolic as an immune disease."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Psoriatic arthritis clusters with type 2 diabetes in a metabolic-syndrome phenotype: shared systemic inflammation (TNF, IL-6) drives insulin resistance, so PsA patients have excess diabetes—screening for metabolic risk is part of comprehensive PsA care."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Synovial fibroblasts help drive the joint destruction of psoriatic arthritis: activated by IL-17/TNF, they proliferate, invade and erode cartilage and bone at inflamed joints and entheses—so fibroblast-driven tissue remodeling, not just immune cells, damages the joint."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Psoriatic arthritis can inflame the eye: as a spondyloarthritis, it predisposes to uveitis and conjunctivitis, so eye symptoms join the skin, nail and joint features—prompting ophthalmologic care alongside rheumatologic and dermatologic management."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Psoriatic arthritis raises cardiovascular risk through systemic inflammation: chronic IL-17/TNF inflammation accelerates atherosclerosis and pairs with obesity and metabolic syndrome, so heart attacks and strokes are excess causes of death in PsA."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK inhibitors treat psoriatic arthritis: the IL-23/IL-17 and other cytokines driving joint and skin inflammation signal through JAK, so oral JAK inhibitors (tofacitinib, upadacitinib) work across both domains where older drugs target one pathway."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Psoriatic arthritis links skin and joints in the integumentary system: it develops in some people with psoriasis, and skin and nail disease often precede the arthritis, so the rash is both a clue and part of one systemic inflammatory disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Psoriatic arthritis is an immune-mediated spondyloarthritis: dysregulated innate and Th17 immunity inflames entheses, joints and skin, so it sits in the seronegative spondyloarthritis family and responds to the same cytokine-targeting biologics."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Psoriatic arthritis both destroys and builds bone: alongside osteoclast erosions it activates osteoblasts to lay down new bone—periostitis, enthesophytes and the 'pencil-in-cup' deformity—a bone-proliferation pattern that sets it apart from rheumatoid arthritis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12 shares the p40 subunit with IL-23 in psoriatic arthritis: the antibody ustekinumab blocks both by targeting p40, easing skin and joint disease, though IL-23-specific blockade has shown the IL-23/IL-17 axis matters more for the arthritis."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Gut dysbiosis ties psoriatic arthritis to the spondyloarthritis family: an altered microbiome and subclinical gut inflammation can drive the IL-23/IL-17 response, part of why psoriatic and inflammatory-bowel disease overlap."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Psoriatic arthritis attacks where collagen anchors tendon to bone: enthesitis—inflammation at these collagen-rich insertion sites—is its defining lesion, and the same process lays down pathologic new bone alongside the erosions."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Psoriatic arthritis is inflamed by synovial macrophages: these cells flood the joint lining and pour out TNF, a central driver that anti-TNF biologics blunt, making macrophage-derived cytokines a therapeutic linchpin."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Psoriatic arthritis is kindled by dendritic cells: they sense triggers and secrete IL-23 that ignites the IL-17 pathway in skin and joint, sitting at the top of the cytokine cascade that newer IL-23 blockers aim to shut off."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells drive psoriatic arthritis at the joint: CD8 T cells, many making IL-17, accumulate in the inflamed synovium and entheses, so the disease is fueled by killer T cells as much as by the T-helper response."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Psoriatic arthritis both erodes and builds bone with calcium: unlike pure erosive arthritis, it lays down new calcified bone at entheses and joints (enthesophytes, ankylosis), so disordered calcium-bone turnover gives it its distinctive radiographic look."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "A gut-joint axis feeds psoriatic arthritis: subclinical bowel inflammation and a disturbed microbiome prime the IL-23/IL-17 response that strikes the joints, linking the large intestine to the arthritis and to its overlap with inflammatory bowel disease."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Salt may inflame psoriatic arthritis: high sodium pushes naive T cells toward the IL-17-producing Th17 lineage that drives both the skin and joint disease, a dietary link to its core immune axis."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Psoriatic arthritis smolders in the bone marrow: subchondral bone-marrow edema (osteitis) on MRI is a hallmark of the disease, marking the inflammation at entheses and joints before erosions appear."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils tie psoriatic skin to joint: they form the micro-abscesses of psoriatic plaques and pour into inflamed entheses and joints, linking the IL-17-driven skin and arthritis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons capture psoriatic arthritis's signature damage: X-rays show the 'pencil-in-cup' deformity of eroded finger joints, while MRI and ultrasound catch the enthesitis and dactylitis early, before the bone destruction becomes irreversible."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Psoriatic arthritis is hard on the heart: the same chronic IL-17 and TNF inflammation that swells joints accelerates atherosclerosis, raising the risk of heart attack independent of the usual cardiac risk factors."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D sits on both sides of psoriatic disease: deficiency is common and may worsen the Th17/IL-17 inflammation behind it, and vitamin D analogs applied to the skin are a mainstay for the psoriasis that accompanies the arthritis."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Treating PsA keeps an eye on the liver: methotrexate, a first-line DMARD, can scar it over time, and the fatty liver that rides along with the metabolic syndrome common in PsA compounds the risk, so liver enzymes are watched."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "PsA therapy opens the lungs to harm: methotrexate can rarely trigger a hypersensitivity pneumonitis, and the TNF and IL-17 biologics that quiet the disease raise the risk of pneumonia and reactivated tuberculosis."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Fat fuels psoriatic disease: enlarged adipocytes pour out inflammatory adipokines, and the obesity common in PsA both raises the risk of developing it and blunts the response to treatment, tying metabolism to the joints."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "PsA is 'seronegative' yet treated with antibodies: rheumatoid factor and anti-CCP are characteristically absent, separating it from RA, while monoclonal antibodies against TNF, IL-17, and IL-23 are the mainstay that controls both skin and joints."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Chronic inflammation scars the arteries: PsA carries excess cardiovascular risk as circulating cytokines injure the endothelial lining and accelerate atherosclerosis, so heart-attack and stroke prevention is woven into managing the joints."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Body and mood suffer together: depression is markedly more common in PsA, driven by chronic pain, visible skin disease, and the same inflammatory cytokines that act on the brain, so screening for low mood is part of comprehensive care."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Psoriatic disease and fatty liver travel together: shared metabolic syndrome and systemic inflammation make NAFLD and NASH common in PsA, a risk compounded by methotrexate's own liver toxicity that must be monitored during treatment."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The IL-23/Th17 axis signals through STAT3: this transcription factor relays the cytokine drive that expands the pathogenic Th17 cells of PsA, the node downstream of the IL-23 that biologics and JAK inhibitors aim to silence."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells inflame the enthesis: resident at the tendon-bone insertions that PsA targets, they are a major innate source of IL-17, helping ignite the enthesitis and dactylitis that distinguish psoriatic from other arthritis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "PsA both erodes and builds bone: while inflammation eats away joints, Wnt/β-catenin signaling drives the new bone formation — enthesophytes and syndesmophytes — that sets psoriatic apart from rheumatoid arthritis, where this pathway is suppressed."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The brakes on inflammation slip: a relative deficiency and dysfunction of regulatory T cells lets the Th17 response run unchecked in PsA, tilting the balance toward the IL-17-driven joint and skin inflammation."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Chronic inflammation hardens the arteries: the systemic cytokine load of PsA accelerates atherosclerosis, so patients carry a raised risk of heart attack and stroke that persists beyond their joint and skin disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is the inflammatory hub: TNF and IL-17/IL-23 signals converge on NF-κB in synovial and entheseal cells, switching on the cytokine programs that drive the joint inflammation and bone remodeling of PsA."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Widespread pain confounds the joint disease: fibromyalgia is a common comorbidity in PsA, and its pain and tender points can inflate disease-activity scores, complicating the assessment of whether the arthritis is truly active."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Systemic inflammation tips toward clotting: like other chronic inflammatory arthritides, PsA carries an increased risk of venous thromboembolism, adding a venous hazard to its better-known arterial cardiovascular risk."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "The IL-17 blockers expose its niche: secukinumab and other anti-IL-17 biologics used for PsA disarm the very pathway guarding mucosa against Candida, so mucocutaneous candidiasis is a class side effect of treatment."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Inflammation and steroids thin the bone: chronic cytokine-driven bone loss in PsA, compounded by any corticosteroid use and reduced activity, lowers bone density and adds osteoporotic fracture risk to the erosive joint damage."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Persistent inflammation blunts the marrow: the sustained IL-6 and inflammatory drive of active PsA raises hepcidin and suppresses erythropoiesis, producing the anemia of chronic disease seen in poorly controlled patients."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Its TNF-blocking biologics can wake latent TB: tumor-necrosis-factor is essential to containing tuberculosis in granulomas, so TNF inhibitors for PsA risk reactivating latent infection — making screening mandatory before treatment."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Immunosuppressive biologics can reactivate hepatitis B: the TNF inhibitors and other immune-modulating drugs used for PsA can let a dormant hepatitis B virus rebound, so serologic screening is required before starting therapy."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Chronic systemic inflammation accelerates the arteries: the persistent inflammatory burden of PsA, on top of its frequent metabolic syndrome, speeds atherosclerosis and raises the long-term risk of stroke."
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
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Psoriatic arthritis grows out of psoriasis: ~30% of psoriasis patients develop it, usually years after the skin disease, and both run on the same IL-23/IL-17 axis — why biologics that clear psoriatic plaques (anti-IL-17, anti-IL-23) also treat the joints.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Psoriatic arthritis attacks the musculoskeletal system distinctively: asymmetric oligoarthritis, distal interphalangeal disease, enthesitis, dactylitis ('sausage digit'), and sacroiliitis — combining erosion with new bone formation, unlike the pure erosion of RA.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Psoriatic arthritis is driven by Th17 helper T cells: IL-23 expands IL-17-producing CD4+ T cells (and innate IL-17 at entheses) that activate neutrophils and osteoclasts — driving inflammation, erosion, and new-bone formation, the rationale for anti-IL-17/IL-23 biologics.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Psoriatic and rheumatoid arthritis are the two major chronic inflammatory arthritides but differ: PsA is a seronegative spondyloarthropathy with enthesitis, dactylitis, DIP involvement, and psoriasis, while RA is a symmetric, RF/anti-CCP-positive synovitis sparing the DIP joints.
- `connects-to` → **[Gout](../gout/README.md)** — Psoriatic arthritis and gout can mimic and coexist: high cell turnover in psoriasis raises uric acid, so PsA patients get gout more often, and an acutely swollen toe (dactylitis vs podagra) may need joint aspiration to tell crystal arthritis from psoriatic disease.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Psoriatic arthritis uniquely combines bone erosion and new bone formation: TNF and IL-17 drive osteoclasts to erode joints (pencil-in-cup deformity) while stimulating osteoblasts to build syndesmophytes and enthesophytes—a remodeling signature distinct from RA.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Psoriatic arthritis and IBD belong to the same IL-23/Th17 spondyloarthritis family: both share gut-skin-joint inflammation and respond to IL-23 and TNF blockers—though IL-17 inhibitors that help PsA can paradoxically worsen IBD.
- `connects-to` → **[Obesity](../obesity/README.md)** — Psoriatic arthritis is strongly tied to obesity: adipose tissue is pro-inflammatory (TNF, IL-6, leptin), raising PsA risk and severity and blunting response to therapy, while weight loss improves disease control—so PsA is as much a metabolic as an immune disease.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Psoriatic arthritis clusters with type 2 diabetes in a metabolic-syndrome phenotype: shared systemic inflammation (TNF, IL-6) drives insulin resistance, so PsA patients have excess diabetes—screening for metabolic risk is part of comprehensive PsA care.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Synovial fibroblasts help drive the joint destruction of psoriatic arthritis: activated by IL-17/TNF, they proliferate, invade and erode cartilage and bone at inflamed joints and entheses—so fibroblast-driven tissue remodeling, not just immune cells, damages the joint.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Psoriatic arthritis can inflame the eye: as a spondyloarthritis, it predisposes to uveitis and conjunctivitis, so eye symptoms join the skin, nail and joint features—prompting ophthalmologic care alongside rheumatologic and dermatologic management.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Psoriatic arthritis raises cardiovascular risk through systemic inflammation: chronic IL-17/TNF inflammation accelerates atherosclerosis and pairs with obesity and metabolic syndrome, so heart attacks and strokes are excess causes of death in PsA.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK inhibitors treat psoriatic arthritis: the IL-23/IL-17 and other cytokines driving joint and skin inflammation signal through JAK, so oral JAK inhibitors (tofacitinib, upadacitinib) work across both domains where older drugs target one pathway.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Psoriatic arthritis links skin and joints in the integumentary system: it develops in some people with psoriasis, and skin and nail disease often precede the arthritis, so the rash is both a clue and part of one systemic inflammatory disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Psoriatic arthritis is an immune-mediated spondyloarthritis: dysregulated innate and Th17 immunity inflames entheses, joints and skin, so it sits in the seronegative spondyloarthritis family and responds to the same cytokine-targeting biologics.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Psoriatic arthritis both destroys and builds bone: alongside osteoclast erosions it activates osteoblasts to lay down new bone—periostitis, enthesophytes and the 'pencil-in-cup' deformity—a bone-proliferation pattern that sets it apart from rheumatoid arthritis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 shares the p40 subunit with IL-23 in psoriatic arthritis: the antibody ustekinumab blocks both by targeting p40, easing skin and joint disease, though IL-23-specific blockade has shown the IL-23/IL-17 axis matters more for the arthritis.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Gut dysbiosis ties psoriatic arthritis to the spondyloarthritis family: an altered microbiome and subclinical gut inflammation can drive the IL-23/IL-17 response, part of why psoriatic and inflammatory-bowel disease overlap.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Psoriatic arthritis attacks where collagen anchors tendon to bone: enthesitis—inflammation at these collagen-rich insertion sites—is its defining lesion, and the same process lays down pathologic new bone alongside the erosions.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Psoriatic arthritis is inflamed by synovial macrophages: these cells flood the joint lining and pour out TNF, a central driver that anti-TNF biologics blunt, making macrophage-derived cytokines a therapeutic linchpin.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Psoriatic arthritis is kindled by dendritic cells: they sense triggers and secrete IL-23 that ignites the IL-17 pathway in skin and joint, sitting at the top of the cytokine cascade that newer IL-23 blockers aim to shut off.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells drive psoriatic arthritis at the joint: CD8 T cells, many making IL-17, accumulate in the inflamed synovium and entheses, so the disease is fueled by killer T cells as much as by the T-helper response.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Psoriatic arthritis both erodes and builds bone with calcium: unlike pure erosive arthritis, it lays down new calcified bone at entheses and joints (enthesophytes, ankylosis), so disordered calcium-bone turnover gives it its distinctive radiographic look.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — A gut-joint axis feeds psoriatic arthritis: subclinical bowel inflammation and a disturbed microbiome prime the IL-23/IL-17 response that strikes the joints, linking the large intestine to the arthritis and to its overlap with inflammatory bowel disease.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Salt may inflame psoriatic arthritis: high sodium pushes naive T cells toward the IL-17-producing Th17 lineage that drives both the skin and joint disease, a dietary link to its core immune axis.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Psoriatic arthritis smolders in the bone marrow: subchondral bone-marrow edema (osteitis) on MRI is a hallmark of the disease, marking the inflammation at entheses and joints before erosions appear.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils tie psoriatic skin to joint: they form the micro-abscesses of psoriatic plaques and pour into inflamed entheses and joints, linking the IL-17-driven skin and arthritis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons capture psoriatic arthritis's signature damage: X-rays show the 'pencil-in-cup' deformity of eroded finger joints, while MRI and ultrasound catch the enthesitis and dactylitis early, before the bone destruction becomes irreversible.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Psoriatic arthritis is hard on the heart: the same chronic IL-17 and TNF inflammation that swells joints accelerates atherosclerosis, raising the risk of heart attack independent of the usual cardiac risk factors.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D sits on both sides of psoriatic disease: deficiency is common and may worsen the Th17/IL-17 inflammation behind it, and vitamin D analogs applied to the skin are a mainstay for the psoriasis that accompanies the arthritis.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Treating PsA keeps an eye on the liver: methotrexate, a first-line DMARD, can scar it over time, and the fatty liver that rides along with the metabolic syndrome common in PsA compounds the risk, so liver enzymes are watched.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — PsA therapy opens the lungs to harm: methotrexate can rarely trigger a hypersensitivity pneumonitis, and the TNF and IL-17 biologics that quiet the disease raise the risk of pneumonia and reactivated tuberculosis.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Fat fuels psoriatic disease: enlarged adipocytes pour out inflammatory adipokines, and the obesity common in PsA both raises the risk of developing it and blunts the response to treatment, tying metabolism to the joints.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — PsA is 'seronegative' yet treated with antibodies: rheumatoid factor and anti-CCP are characteristically absent, separating it from RA, while monoclonal antibodies against TNF, IL-17, and IL-23 are the mainstay that controls both skin and joints.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Chronic inflammation scars the arteries: PsA carries excess cardiovascular risk as circulating cytokines injure the endothelial lining and accelerate atherosclerosis, so heart-attack and stroke prevention is woven into managing the joints.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Body and mood suffer together: depression is markedly more common in PsA, driven by chronic pain, visible skin disease, and the same inflammatory cytokines that act on the brain, so screening for low mood is part of comprehensive care.
- `connects-to` → **[NASH](../nash/README.md)** — Psoriatic disease and fatty liver travel together: shared metabolic syndrome and systemic inflammation make NAFLD and NASH common in PsA, a risk compounded by methotrexate's own liver toxicity that must be monitored during treatment.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The IL-23/Th17 axis signals through STAT3: this transcription factor relays the cytokine drive that expands the pathogenic Th17 cells of PsA, the node downstream of the IL-23 that biologics and JAK inhibitors aim to silence.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells inflame the enthesis: resident at the tendon-bone insertions that PsA targets, they are a major innate source of IL-17, helping ignite the enthesitis and dactylitis that distinguish psoriatic from other arthritis.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — PsA both erodes and builds bone: while inflammation eats away joints, Wnt/β-catenin signaling drives the new bone formation — enthesophytes and syndesmophytes — that sets psoriatic apart from rheumatoid arthritis, where this pathway is suppressed.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The brakes on inflammation slip: a relative deficiency and dysfunction of regulatory T cells lets the Th17 response run unchecked in PsA, tilting the balance toward the IL-17-driven joint and skin inflammation.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Chronic inflammation hardens the arteries: the systemic cytokine load of PsA accelerates atherosclerosis, so patients carry a raised risk of heart attack and stroke that persists beyond their joint and skin disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is the inflammatory hub: TNF and IL-17/IL-23 signals converge on NF-κB in synovial and entheseal cells, switching on the cytokine programs that drive the joint inflammation and bone remodeling of PsA.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Widespread pain confounds the joint disease: fibromyalgia is a common comorbidity in PsA, and its pain and tender points can inflate disease-activity scores, complicating the assessment of whether the arthritis is truly active.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Systemic inflammation tips toward clotting: like other chronic inflammatory arthritides, PsA carries an increased risk of venous thromboembolism, adding a venous hazard to its better-known arterial cardiovascular risk.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — The IL-17 blockers expose its niche: secukinumab and other anti-IL-17 biologics used for PsA disarm the very pathway guarding mucosa against Candida, so mucocutaneous candidiasis is a class side effect of treatment.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Inflammation and steroids thin the bone: chronic cytokine-driven bone loss in PsA, compounded by any corticosteroid use and reduced activity, lowers bone density and adds osteoporotic fracture risk to the erosive joint damage.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Persistent inflammation blunts the marrow: the sustained IL-6 and inflammatory drive of active PsA raises hepcidin and suppresses erythropoiesis, producing the anemia of chronic disease seen in poorly controlled patients.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Its TNF-blocking biologics can wake latent TB: tumor-necrosis-factor is essential to containing tuberculosis in granulomas, so TNF inhibitors for PsA risk reactivating latent infection — making screening mandatory before treatment.
- `connects-to` → **[Hepatitis B virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Immunosuppressive biologics can reactivate hepatitis B: the TNF inhibitors and other immune-modulating drugs used for PsA can let a dormant hepatitis B virus rebound, so serologic screening is required before starting therapy.
- `connects-to` → **[Stroke](../stroke/README.md)** — Chronic systemic inflammation accelerates the arteries: the persistent inflammatory burden of PsA, on top of its frequent metabolic syndrome, speeds atherosclerosis and raises the long-term risk of stroke.

[^ritchlin-2017-psa-review]: Ritchlin CT, Colbert RA, Gladman DD. Psoriatic arthritis. *N Engl J Med.* 2017;376(10):957-970. [doi:10.1056/NEJMra1505557](https://doi.org/10.1056/NEJMra1505557) · [PubMed 28273019](https://pubmed.ncbi.nlm.nih.gov/28273019/)
[^mease-2015-secukinumab-psa-future2]: Mease PJ, et al. Secukinumab inhibition of interleukin-17A in patients with psoriatic arthritis. *N Engl J Med.* 2015;373(14):1329-1339. [doi:10.1056/NEJMoa1503317](https://doi.org/10.1056/NEJMoa1503317) · [PubMed 26422723](https://pubmed.ncbi.nlm.nih.gov/26422723/)
[^deodhar-2020-guselkumab-discover1]: Deodhar A, et al. Guselkumab in patients with active psoriatic arthritis (DISCOVER-1). *Lancet.* 2020;395(10230):1115-1125. [doi:10.1016/S0140-6736(20)30263-4](https://doi.org/10.1016/S0140-6736(20)30263-4) · [PubMed 32178765](https://pubmed.ncbi.nlm.nih.gov/32178765/)
[^gladman-2005-caspar-criteria]: Taylor W, et al. Classification criteria for psoriatic arthritis. *Arthritis Rheum.* 2006;54(8):2665-2673. [doi:10.1002/art.21972](https://doi.org/10.1002/art.21972) · [PubMed 16871531](https://pubmed.ncbi.nlm.nih.gov/16871531/)
