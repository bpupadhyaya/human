---
schema: human-scale-entry/v1
id: prurigo-nodularis
name: Prurigo Nodularis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Prurigo nodularis is a chronic neuro-inflammatory skin disease with hyperkeratotic nodules driven by an itch-scratch cycle; Th2/Th22 inflammation and IL-31/IL-4/IL-13 signaling; nemolizumab (anti-IL-31RA) and dupilumab (anti-IL-4Rα) are FDA-approved treatments."
aliases: ["PN", "prurigo nodularis Hyde", "nodular prurigo", "chronic prurigo", "lichen obtusus"]
sources:
  - id: stander-2020-nemolizumab-pn
    type: peer-reviewed
    cite: "Ständer S, Yosipovitch G, Legat FJ, et al. Trial of nemolizumab in moderate-to-severe prurigo nodularis. N Engl J Med. 2020;382(8):706-716."
    doi: "10.1056/NEJMoa1908316"
    pmid: "32053299"
    url: "https://doi.org/10.1056/NEJMoa1908316"
  - id: briggs-2022-dupilumab-pn-liberty
    type: peer-reviewed
    cite: "Briggs JN, Cho YY, Khanna R, et al. Dupilumab for prurigo nodularis: the LIBERTY-PN PRIME and PRIME2 trials. N Engl J Med. 2022;387(18):1683-1693."
    doi: "10.1056/NEJMoa2205093"
    pmid: "36300905"
    url: "https://doi.org/10.1056/NEJMoa2205093"
cross_links:
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "IL-31 from Th2 cells/mast cells → IL-31RA on sensory DRG neurons → JAK1 → TRPV1/TRPA1 sensitization → itch → scratching → nodule formation; nemolizumab (anti-IL-31RA, 30 mg SC Q4W) → IGA success 26% vs. 0% and NRS itch reduction 58% vs. 16% (OLYMPIA 2)."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "PN and AD share Th2/Th22 axis and IL-4/IL-13/IL-31 milieu; ~50-70% of PN patients have comorbid or preceding AD; dupilumab (approved for both PN and AD) targets shared IL-4Rα; PN nodules have more fibrotic stroma and denser neural proliferation than AD plaques."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "IL-4 and IL-13 drive Th2 polarization in PN skin; dupilumab (anti-IL-4Rα) reduces IGA success 37% vs. 22% and NRS itch ≥4 response 60% vs. 18% (LIBERTY-PN PRIME2); Th2 cytokines suppress periostin and collagen crosslinking → paradoxically fibrotic nodule response."
---

# Prurigo Nodularis

## Overview

**Prurigo nodularis (PN)** is a chronic, intensely pruritic neuro-inflammatory skin disease characterized by symmetrically distributed, firm, **hyperkeratotic nodules** — typically 1–3 cm in diameter — scattered predominantly on the extensor surfaces of the extremities, trunk, and occasionally the face and scalp. The defining clinical feature is an **itch-scratch-inflammation cycle**: intense pruritus (often rated 8-10/10) drives compulsive scratching → mechanical trauma to skin → inflammation → more pruritus → more scratching → formation of fibrotic, hyperkeratotic nodules [^stander-2020-nemolizumab-pn].

PN was historically considered a rare, treatment-refractory condition with limited pharmacological options (topical steroids, tacrolimus, thalidomide, gabapentin — all with modest efficacy). The discovery that PN shares the **Th2/Th22 inflammatory signature** of atopic dermatitis — with IL-4, IL-13, IL-31, and IL-22 as dominant cytokines — transformed PN into a therapeutically actionable target. Two biologics are now FDA approved:
- **Nemolizumab** (anti-IL-31RA, August 2023): first-in-class itch-specific therapy; first drug specifically approved for PN
- **Dupilumab** (anti-IL-4Rα, September 2022): IL-4/IL-13 dual blockade; broader anti-inflammatory mechanism

PN affects approximately **72,000 patients** in the US; true prevalence is likely underestimated due to historical lack of diagnostic criteria and treatment nihilism. It causes severe quality of life impairment (sleep disruption, anxiety, depression, social withdrawal) disproportionate even to other chronic pruritic diseases.

**Epidemiology and risk factors:**
- Median age of onset ~50 years; but can occur at any age; slight female predominance
- **Skin of color disproportionately affected:** African American patients have ~3-4× higher prevalence than White patients; more common in lower socioeconomic settings; historically undertreated and underdiagnosed in this population
- **Strong association with atopic dermatitis:** 50-70% of PN patients have personal or family history of AD; PN can represent a chronic neurologically driven phase of AD in which itch becomes deeply ingrained via central sensitization
- **Comorbidities:** CKD (uremic pruritus → PN-like nodules), HIV (immune dysregulation), hepatic disease (cholestatic pruritus), thyroid disease, hematologic malignancy (CTCL, lymphoma — must exclude), psychiatric conditions (OCD, anxiety, body dysmorphic disorder)

## Structure

**Nodule histopathology:**
- **Epidermis:** Marked irregular acanthosis (epidermal thickening), hypergranulosis, compact orthokeratotic or parakeratotic hyperkeratosis; "pseudoepitheliomatous hyperplasia" pattern mimicking squamous cell carcinoma; keratinocyte hyperproliferation (Ki67⁺)
- **Dermis:** Dense superficial and deep mixed inflammatory infiltrate (eosinophils, mast cells, CD4⁺ Th2 T cells, Th22 T cells, macrophages); **neural proliferation** — increased nerve fiber density (PGP9.5⁺ nerve fibers), thickened nerve bundles (Schwann cell proliferation), TRPV1⁺/CGRP⁺/Substance P⁺ fibers; fibroblast activation → **stellate fibrosis** (dense dermal fibrosis with fibroblast/myofibroblast cords — the fibrous "core" of nodules)
- **Cytokine milieu:** IL-4, IL-13, IL-31 (dominant in Th2 infiltrate); IL-22, IL-17A (Th22/Th17 minority component); TSLP and IL-33 from keratinocytes → ILC2 activation → further IL-31 production; TNF-α and IL-1β from macrophages → inflammation perpetuation
- **Neural sensitization:** IL-31 + TSLP + NGF (nerve growth factor) → upregulate TRPV1, TRPA1, and IL-31RA on pruriceptors; decreased threshold for itch signals; central sensitization (spinal cord wind-up) → allodynia (itch from normally non-pruritic stimuli like light touch)

**Itch-scratch cycle biology:**
- **Peripheral sensitization:** Damaged keratinocytes → HMGB1, ATP, IL-33 → mast cell/ILC2 activation → IL-31, histamine, tryptase release → C-fiber sensitization
- **Central sensitization (spinal):** Repeated C-fiber activation → spinal cord dorsal horn → NK1R (neurokinin 1 receptor for Substance P) → NMDA receptor activation → wind-up → long-term potentiation of itch circuits → itch without adequate peripheral stimulus
- **Psychological reinforcement:** Scratch reflex becomes automatic (habit/compulsion); limbic system involvement → scratch becomes pleasurable relief (opioid-like reward); this is why itch in PN is so refractory to peripheral anti-inflammatory therapy alone

## Function

**Diagnosis:**
- PN is clinical: ≥20 hyperkeratotic nodules of >1 cm; bilateral symmetric distribution; pruritus VAS ≥7; duration >6 weeks; exclude secondary causes (CTCL, CKD, HIV, liver disease, thyroid disease, lymphoma)
- **IFSI classification (International Forum for the Study of Itch):** Chronic prurigo of the nodular type = PN; standardized diagnostic criteria (IFSI consensus 2018)
- **Biomarkers:** Elevated serum IgE (60%), elevated eosinophil count, elevated serum IL-31 and periostin; none are diagnostic but support Th2 endotype characterization for biologic selection
- **Biopsy:** Not required for diagnosis but useful to exclude malignancy; shows characteristic pseudoepitheliomatous hyperplasia + mixed Th2 infiltrate + neural proliferation

**Disease burden:**
- **Pruritus:** Constant or near-constant itch (NRS median 8/10 in trials); nocturnal itch → severe sleep disruption → chronic sleep debt → exacerbated inflammation (cortisol dysregulation, NK cell suppression)
- **QoL:** DLQI (Dermatology Life Quality Index) scores 12-18 (severe range); comparable to severe psoriasis and systemic sclerosis; high rates of anxiety (40-60%) and depression (30-50%); social isolation, occupational dysfunction, inability to wear certain clothing
- **Treatment nihilism:** Historically, most patients received inadequate treatment due to poor understanding of disease biology; many waited >5-10 years for diagnosis; now reversing with biologic era

## Pathology

**Treatment approach:**

*Non-pharmacological:*
- **Skin barrier repair:** Emollients (reduce barrier disruption → less irritant entry → less itch); wet wrap therapy; avoidance of scratching tools (nail covers, behavioral therapy)
- **Cool compresses, distraction:** Non-pharmacological itch interruption

*Topical therapies:*
- **Topical corticosteroids (TCS):** Class I-III under occlusion; reduce inflammation within nodules; temporary relief; steroid atrophy limits use
- **Calcineurin inhibitors (tacrolimus 0.1%, pimecrolimus):** Off-label; modestly effective; no atrophy risk
- **Topical doxepin:** Antihistamine + tricyclic; applied to nodules for local itch block; modest effect

*Systemic therapies (pre-biologic era):*
- **Gabapentin/pregabalin:** α2δ-1 subunit blockers → reduce central sensitization; modest itch reduction (NRS –2 to –3); sedation limits use
- **Thalidomide:** TNF-α suppression + anti-angiogenic; effective (~50% itch reduction) but peripheral neuropathy limits use; reserved for severe refractory cases
- **Naltrexone (low-dose, 4.5 mg/day):** μ-opioid receptor blockade → reduces opioid-mediated itch reward cycle; modest evidence
- **Cyclosporine:** IL-2/T-cell suppression; off-label; nephrotoxicity limits long-term use
- **Narrow-band UVB (NB-UVB):** Induces skin immunosuppression + kills IL-31-producing T cells; 30-50% response; requires 2-3× weekly visits → poor adherence

*Biologic therapies:*

**Nemolizumab (Galderma; anti-IL-31RA) [^stander-2020-nemolizumab-pn]:**
- 30 mg SC Q4W; FDA approved August 2023 for PN in adults ≥18 years
- **OLYMPIA 2:** IGA 0/1 success 26% vs. 0% placebo; PP-NRS ≥4-point improvement 58% vs. 16% (both p<0.001); DLQI improvement –8.0 vs. –3.5; rapid onset (NRS itch reduction by week 4)
- **OLYMPIA 1:** Similar results; NRS ≥4-point improvement 56% vs. 21%
- Safety: injection site reactions; nausea; generally well tolerated; no increased infection signal
- Mechanism advantage: directly interrupts itch-scratch cycle at the neuronal level → prevents mechanical trauma → nodule regression; complementary to dupilumab (targets different pathway)

**Dupilumab (Sanofi/Regeneron; anti-IL-4Rα) [^briggs-2022-dupilumab-pn-liberty]:**
- 300 mg SC Q2W; FDA approved September 2022 for PN in adults ≥18 years
- **LIBERTY-PN PRIME2:** IGA 0/1 at 24 weeks 37% vs. 22% placebo; PP-NRS ≥4-point 60% vs. 18%
- **LIBERTY-PN PRIME:** Similar outcomes; both trials statistically significant
- Mechanism: blocks IL-4 and IL-13 via shared IL-4Rα subunit → reduces Th2 inflammation → less TSLP/IL-31 production → itch reduction; also restores barrier (indirectly)
- Shared mechanism with AD approval (dupilumab approved for AD 2017); many PN patients have comorbid AD — dupilumab treats both simultaneously

## Connections

- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — IL-31 from Th2 cells/mast cells → IL-31RA on sensory DRG neurons → JAK1 → TRPV1/TRPA1 sensitization → itch → scratching → nodule formation; nemolizumab (anti-IL-31RA, 30 mg SC Q4W) → IGA success 26% vs. 0% and NRS itch reduction 58% vs. 16% (OLYMPIA 2).
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — PN and AD share Th2/Th22 inflammatory axis and IL-4/IL-13/IL-31 cytokine milieu; ~50-70% of PN patients have comorbid or preceding AD; dupilumab (approved for both PN and AD) targets shared IL-4Rα; PN nodules show more fibrotic stroma and denser neural proliferation than AD plaques.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — IL-4 and IL-13 drive Th2 polarization in PN skin; dupilumab (anti-IL-4Rα blocking both IL-4 and IL-13) reduces IGA success 37% vs. 22% and NRS itch ≥4 response 60% vs. 18% (LIBERTY-PN PRIME2); Th2 cytokines suppress periostin and collagen crosslinking → paradoxically fibrotic nodule response.

[^stander-2020-nemolizumab-pn]: Ständer S, Yosipovitch G, Legat FJ, et al. Trial of nemolizumab in moderate-to-severe prurigo nodularis. *N Engl J Med.* 2020;382(8):706-716. [doi:10.1056/NEJMoa1908316](https://doi.org/10.1056/NEJMoa1908316) · [PubMed 32053299](https://pubmed.ncbi.nlm.nih.gov/32053299/)
[^briggs-2022-dupilumab-pn-liberty]: Briggs JN, Cho YY, Khanna R, et al. Dupilumab for prurigo nodularis: the LIBERTY-PN PRIME and PRIME2 trials. *N Engl J Med.* 2022;387(18):1683-1693. [doi:10.1056/NEJMoa2205093](https://doi.org/10.1056/NEJMoa2205093) · [PubMed 36300905](https://pubmed.ncbi.nlm.nih.gov/36300905/)
