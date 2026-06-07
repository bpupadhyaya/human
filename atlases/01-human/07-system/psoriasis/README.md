---
schema: human-scale-entry/v1
id: psoriasis
name: Psoriasis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic skin disease driven by Th17/IL-17 axis, TNF-alpha, and keratinocyte hyperproliferation; thickened scaly erythematous plaques. IL-17 inhibitors (secukinumab, ixekizumab), IL-23 inhibitors (risankizumab), and anti-TNF (adalimumab) provide near-complete skin clearance."
aliases: ["plaque psoriasis", "psoriasis vulgaris", "PsO", "PsA", "psoriatic arthritis", "palmoplantar psoriasis"]
sources:
  - id: nestle-2009-psoriasis-review
    type: peer-reviewed
    cite: "Nestle FO, Kaplan DH, Barker J. Psoriasis. N Engl J Med. 2009;361(5):496-509."
    doi: "10.1056/NEJMra0804595"
    pmid: "19641206"
    url: "https://doi.org/10.1056/NEJMra0804595"
  - id: langley-2014-secukinumab
    type: peer-reviewed
    cite: "Langley RG, Elewski BE, Lebwohl M, et al. Secukinumab in plaque psoriasis — results of two phase 3 trials. N Engl J Med. 2014;371(4):326-338."
    doi: "10.1056/NEJMoa1406095"
    pmid: "25007392"
    url: "https://doi.org/10.1056/NEJMoa1406095"
  - id: gordon-2018-risankizumab
    type: peer-reviewed
    cite: "Gordon KB, Strober B, Lebwohl M, et al. Efficacy and safety of risankizumab in moderate-to-severe plaque psoriasis (UltIMMa-1 and UltIMMa-2): results from two double-blind, randomised, placebo-controlled and ustekinumab-controlled phase 3 trials. Lancet. 2018;392(10148):650-661."
    doi: "10.1016/S0140-6736(18)31713-6"
    pmid: "30097359"
    url: "https://doi.org/10.1016/S0140-6736(18)31713-6"
cross_links:
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Th17 cells are the primary psoriasis pathogenic T cells; IL-17A/F activate keratinocyte NF-kB and STAT3 → CXCL8 and S100 proteins → neutrophil recruitment and epidermal hyperproliferation; IL-22 drives keratinocyte proliferation and anti-apoptosis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha activates keratinocyte NF-kB → CXCL1/IL-8, ICAM-1, and survival genes → epidermal thickening; adalimumab, infliximab, etanercept, and certolizumab achieve ~60% PASI 75 in moderate-severe psoriasis and treat psoriatic arthritis."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 amplifies Th17 polarization (with TGF-beta) in psoriasis; STAT3-driven keratinocyte hyperproliferation; elevated serum IL-6 correlates with psoriasis severity and psoriatic arthritis; tocilizumab has limited psoriasis efficacy vs. Th17-targeting biologics."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-kB is activated in psoriatic keratinocytes by TNF-alpha and IL-17A → drives AMP expression (LL-37, beta-defensins), CXCL8 (neutrophil chemotaxis), IL-6, and CCL20 (DC recruitment); NF-kB inhibition is a downstream convergence point of most anti-psoriasis biologics."
---

# Psoriasis

## Overview

**Psoriasis** is a **chronic, immune-mediated inflammatory skin disease** affecting approximately **125 million people worldwide** (~2-4% of Western populations; 1-2% in Asia). It presents most commonly as **plaque psoriasis** — well-demarcated, erythematous, silvery-scaled plaques on extensor surfaces (elbows, knees), scalp, and lumbosacral region — resulting from epidermal hyperproliferation driven by a dysregulated **Th17/IL-17 axis** [^nestle-2009-psoriasis-review].

Psoriasis is now understood as a **systemic inflammatory disease** with skin manifestations — associated with significant comorbidities including psoriatic arthritis (~30%), cardiovascular disease (increased MACE ~25-50%), metabolic syndrome, inflammatory bowel disease, depression/anxiety, and uveitis. The **psoriatic disease** concept encompasses the full spectrum of these manifestations.

**Psoriasis subtypes:**
- **Plaque psoriasis (psoriasis vulgaris, ~85-90%):** Chronic, most common; stable thick plaques
- **Guttate psoriasis (~10%):** Small droplet-like lesions; often post-streptococcal (streptococcal pharyngitis → guttate flare); commoner in children/young adults; may evolve to plaque
- **Palmoplantar psoriasis:** Palms and soles; functionally debilitating; pustular variant
- **Nail psoriasis (~80% with PsA):** Pitting, onycholysis, oil drop, subungual hyperkeratosis; predictive of PsA development
- **Scalp psoriasis:** ~70% of plaque psoriasis; resistant to treatment due to hair; dandruff-like or thick plaques
- **Inverse psoriasis (flexural):** Intertriginous areas (groin, axillae, submammary); no scale (macerated); diagnostic challenge
- **Erythrodermic psoriasis:** Full body skin involvement (>90% BSA); rare but severe; thermoregulatory failure, protein loss; medical emergency
- **Generalized pustular psoriasis (GPP):** Sterile neutrophilic pustules on erythematous skin; IL-36 pathway mutations (IL36RN, CARD14); spesolimab (anti-IL-36R) FDA approved 2022

**Genetics:**
- **PSORS1 (HLA-Cw*0602):** Strongest genetic signal; ~65% of early-onset psoriasis; presents HLA-C-restricted peptides to CD8+ T cells; associated with guttate subtype and streptococcal trigger
- **IL23R, IL12B, TNFAIP3, CARD14:** Multiple IL-23/IL-17 axis and NF-kB pathway GWAS loci
- **CARD14 mutations:** Gain-of-function → NF-kB activation in keratinocytes → psoriasis-like skin inflammation

## Structure

### Psoriatic plaque histology [^nestle-2009-psoriasis-review]

Normal skin: Ordered stratified squamous epithelium; 28-day epidermal turnover; differentiation from basal layer to stratum corneum.

**Psoriatic plaque:**
- **Acanthosis:** Markedly thickened epidermis (4-5× normal) due to keratinocyte hyperproliferation; epidermal turnover reduced to 3-4 days from 28 days
- **Parakeratosis:** Retention of nuclei in stratum corneum (incomplete differentiation → hallmark of psoriasis histology)
- **Munro microabscesses:** Accumulation of neutrophils in stratum corneum (neutrophil-driven by IL-17A/CXCL8)
- **Dilated blood vessels (dermal papillae):** Angiogenesis (VEGF, TNF-alpha) → tortuous vessels → erythema; visible as Auspitz sign (pinpoint bleeding when scale removed)
- **Dense T cell and DC infiltrate:** CD8+ T cells in epidermis; CD4+ T cells and DCs (mDC1+) in dermis; plasmacytoid DCs (pDCs) produce IFN-alpha initially; mDC1s sustain chronic Th17 response

### Immunopathogenesis

**Initiation phase:**
1. Trigger (physical trauma = Koebner phenomenon, streptococcal infection, stress, drugs [beta-blockers, lithium, antimalarials]) → epithelial damage → release of LL-37 (cathelicidin, an AMP)
2. LL-37 complexes with self-DNA/RNA → activates pDCs via TLR7/9 → type I IFN production → activation of skin mDCs
3. mDCs mature → upregulate IL-12 and IL-23 (shared p40 subunit targeted by ustekinumab; IL-23 p19 targeted by risankizumab, guselkumab, tildrakizumab)
4. IL-23 → Th17 cell differentiation and maintenance → IL-17A, IL-17F, IL-22 production

**Chronic maintenance phase (perpetuating Th17/17 loop):**
- Th17 IL-17A/IL-17F → bind IL-17RA/IL-17RC on keratinocytes → NF-kB and MAPK → S100 proteins (S100A7/A8/A9) → activate more DCs, trigger further IL-23 production → self-amplifying loop
- IL-17 → CXCL1/IL-8 → neutrophil recruitment → Munro microabscesses
- IL-22 → JAK1/STAT3 → keratinocyte hyperproliferation and anti-apoptosis → acanthosis
- TNF-alpha (from DCs, macrophages, keratinocytes) → ICAM-1, VCAM-1 on vasculature → further T cell recruitment; synergizes with IL-17 → additive/synergistic keratinocyte activation
- **Memory T-resident (Trm) cells in skin:** CD8+ Trm cells maintain psoriasis between flares and drive rapid plaque recurrence at previously affected sites upon trigger exposure — explains the "memory" of psoriatic plaques

## Function

### Clinical presentation

**Skin disease:**
- Well-demarcated erythematous plaques with thick adherent silvery scales; pruritus variable (25-70%); Koebner phenomenon (new lesions at trauma sites); Auspitz sign (pinpoint bleeding after scale removal)
- **BSA (body surface area) assessment:** Mild <3%, moderate 3-10%, severe >10%; also PASI (Psoriasis Area and Severity Index), IGA (Investigator's Global Assessment), DLQI (quality of life)
- Scalp, nails, palmoplantar, and genital involvement are high-impact sites regardless of BSA

**Psoriatic arthritis (PsA):**
- ~30% of psoriasis patients; inflammatory arthritis with distinctive features: asymmetric oligoarthritis, DIP joint involvement, dactylitis ("sausage digit"), enthesitis (Achilles tendon, plantar fascia), spondylitis, arthritis mutilans (severe deforming)
- CASPAR criteria: Inflammatory arthritis + 3 points from: psoriasis (current=2, history=1), nail changes, RF-negative, dactylitis, periarticular bone formation on X-ray
- Treatment: MTX (peripheral joints only), anti-TNF, anti-IL-17 (secukinumab, ixekizumab), anti-IL-12/23 (ustekinumab), JAK inhibitors (upadacitinib, tofacitinib, filgotinib), PDE-4 inhibitor (apremilast)

**Cardiovascular comorbidity:**
- ~1.4× increased MACE in moderate-severe psoriasis; chronic systemic inflammation → atherosclerosis acceleration; psoriasis patients have higher CRP, IL-6, TNF-alpha → endothelial dysfunction; anti-TNF and IL-17 biologics reduce cardiovascular inflammation and event rates
- Screen and treat cardiovascular risk factors aggressively in moderate-severe psoriasis

## Pathology

### Diagnosis

Clinical diagnosis in most cases; biopsy if uncertain (psoriasiform dermatitis pattern: acanthosis, parakeratosis, Munro microabscesses, dilated papillary vessels); rule out tinea (KOH prep), seborrheic dermatitis (more greasy, ill-defined), nummular eczema (pruritic vesicles).

Differential: Seborrheic dermatitis (common), pityriasis rosea (herald patch, Christmas tree pattern), mycosis fungoides (patch/plaque, epidermotropism), reactive arthritis (Reiter syndrome — skin lesions + urethritis + arthritis).

### Treatment [^langley-2014-secukinumab] [^gordon-2018-risankizumab]

**Topical therapy (mild psoriasis):**
- High-potency corticosteroids (clobetasol) — first-line; rapid efficacy; skin atrophy with chronic use; taper after control
- Vitamin D analogues (calcipotriol/calcipotriene): Anti-proliferative; combined with corticosteroid (Taclonex/Dovobet) → superior; non-atrophogenic; first-line maintenance
- Calcineurin inhibitors (tacrolimus, pimecrolimus): Face, flexures, genital; avoid atrophy-prone areas; no steroid adverse effects
- Roflumilast cream (Zoryve, PDE-4 inhibitor): New approval 2022; non-steroidal option including for intertriginous psoriasis

**Phototherapy (moderate psoriasis or topical-refractory):**
- **Narrowband UVB (NB-UVB, 311 nm):** First-line phototherapy; suppresses Th17 cells; 3× weekly × 3-4 months; 70-80% clearance; home units available; minimal systemic effects
- **PUVA (psoralen + UVA):** More effective than NB-UVB; psoralen photosensitizer + UVA → DNA cross-links in keratinocytes; increased squamous cell carcinoma risk with cumulative exposure; less commonly used now

**Systemic conventional therapy (moderate-severe):**
- **Methotrexate:** Folate antagonist → anti-proliferative and anti-inflammatory; 15-25 mg/week; effective but teratogenic; hepatotoxicity (transient elastography instead of routine liver biopsy); baseline PFTs
- **Cyclosporine:** Calcineurin inhibitor → T cell suppression; rapid clearance; reserved for short-term (≤1 year) for severe flares; hypertension and renal toxicity limit long-term use
- **Acitretin:** Oral retinoid; anti-proliferative; pustular psoriasis preferred; teratogenic (avoid 3 years post-treatment in women); dyslipidemia; liver toxicity
- **Apremilast (Otezla, PDE-4 inhibitor):** Oral; cAMP elevation → reduced TNF-alpha and IL-17 production; 33% PASI 75 at week 16; safer profile (no labs beyond baseline); mild efficacy; particularly useful for mild-moderate or biologic-contraindicated patients

**Biologic therapies:**

*Anti-TNF (first generation):*
- Adalimumab, infliximab, etanercept, certolizumab: ~60% PASI 75; well-established safety; screen TB; avoid live vaccines; second-line now in many guidelines due to superior efficacy of anti-IL-17/IL-23

*Anti-IL-12/23 (targeting p40 subunit):*
- **Ustekinumab (Stelara):** SC Q12W maintenance; ~70% PASI 75; excellent safety; but less efficacious than anti-IL-17/IL-23 in direct comparisons; dual approval for psoriasis and PsA

*Anti-IL-17 (most efficacious skin class):*
- **Secukinumab (Cosentyx, anti-IL-17A):** SC weekly × 5 then monthly; ERASURE/FIXTURE trials: ~77% PASI 90 at week 16; 59% PASI 100 at week 52 — first biologic to reach >50% complete clearance in trials [^langley-2014-secukinumab]; approved psoriasis, PsA, AS, nr-axSpA
- **Ixekizumab (Taltz, anti-IL-17A):** SC biweekly × 3 then monthly; slightly superior to secukinumab in IXORA-S head-to-head; ~81% PASI 90 at week 12
- **Bimekizumab (Bimzelx, anti-IL-17A/F):** Dual IL-17A and IL-17F blockade; BE READY trial: 67% PASI 100 (complete clearance) at week 16 — highest complete clearance rate; oral candidiasis higher (~10%) due to dual IL-17 blockade; SC monthly after initial doses; EU approved 2023, FDA approved 2023

*Anti-IL-23 p19 (most selective, best-in-class durability):*
- **Risankizumab (Skyrizi):** Anti-IL-23 p19; SC Q12W after 2 Q4W doses; UltIMMa-1/2: 75% PASI 90 at week 16; 56% PASI 100 at 52 weeks; superior to ustekinumab and adalimumab in head-to-heads; approved psoriasis, PsA, CD, UC [^gordon-2018-risankizumab]
- **Guselkumab (Tremfya):** Anti-IL-23 p19; SC Q8W; VOYAGE trials: 73% PASI 90 at week 24
- **Tildrakizumab (Ilumya):** Anti-IL-23 p19; Q12W; approved moderate-severe plaque psoriasis
- **Deucravacitinib (Sotyktu, TYK2 inhibitor):** Oral; inhibits TYK2 pseudokinase (allosteric) → reduces IL-23 and IL-12 signaling; POETYK PSO-1/2: 53-58% PASI 75 vs. 35% apremilast; FDA approved 2022; oral biologic-like efficacy; no VTE/MACE boxed warning unlike pan-JAK inhibitors

## Connections

- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Th17 cells are the primary psoriasis pathogenic effectors; IL-17A/F activate keratinocyte NF-kB and STAT3 → AMP expression, CXCL8, and S100 proteins → neutrophil recruitment and epidermal hyperproliferation; IL-22 drives keratinocyte proliferation and anti-apoptotic programs.
- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — TNF-alpha activates keratinocyte NF-kB → CXCL1/IL-8, ICAM-1, and survival genes → epidermal thickening and vascular activation; adalimumab, infliximab, etanercept, and certolizumab achieve ~60% PASI 75 in plaque psoriasis and treat psoriatic arthritis.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 amplifies Th17 polarization (with TGF-beta) in psoriasis; STAT3-dependent keratinocyte hyperproliferation; elevated serum IL-6 correlates with psoriasis severity and psoriatic arthritis activity; IL-6 trans-signaling drives systemic cardiovascular risk.
- `connects-to` → **[NF-kB](../../03-molecular/nf-kb/README.md)** — NF-kB activated in psoriatic keratinocytes by TNF-alpha and IL-17A → AMP expression (LL-37, beta-defensins), CXCL8 (neutrophil chemotaxis), and CCL20 (DC recruitment); CARD14 gain-of-function mutations constitutively activate keratinocyte NF-kB → psoriasis without external trigger.

[^nestle-2009-psoriasis-review]: Nestle FO, Kaplan DH, Barker J. Psoriasis. *N Engl J Med.* 2009;361(5):496-509. [doi:10.1056/NEJMra0804595](https://doi.org/10.1056/NEJMra0804595) · [PubMed 19641206](https://pubmed.ncbi.nlm.nih.gov/19641206/)
[^langley-2014-secukinumab]: Langley RG, Elewski BE, Lebwohl M, et al. Secukinumab in plaque psoriasis — results of two phase 3 trials. *N Engl J Med.* 2014;371(4):326-338. [doi:10.1056/NEJMoa1406095](https://doi.org/10.1056/NEJMoa1406095) · [PubMed 25007392](https://pubmed.ncbi.nlm.nih.gov/25007392/)
[^gordon-2018-risankizumab]: Gordon KB, Strober B, Lebwohl M, et al. Efficacy and safety of risankizumab in moderate-to-severe plaque psoriasis (UltIMMa-1 and UltIMMa-2). *Lancet.* 2018;392(10148):650-661. [doi:10.1016/S0140-6736(18)31713-6](https://doi.org/10.1016/S0140-6736(18)31713-6) · [PubMed 30097359](https://pubmed.ncbi.nlm.nih.gov/30097359/)
