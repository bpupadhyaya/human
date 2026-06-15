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
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "IL-23 from dermal DCs activates Th17 and γδ T cells → IL-17A/F and IL-22 → keratinocyte hyperproliferation, acanthosis, and neutrophil recruitment in psoriatic plaques; anti-IL-23p19 antibodies (risankizumab, guselkumab) achieve PASI 90 response in ~50% of patients."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A from skin Th17 and γδ T cells activates keratinocyte IL-17RA/RC → NF-kB → CXCL8, S100A proteins, and AMPs → neutrophil influx and epidermal hyperproliferation; secukinumab (anti-IL-17A) and ixekizumab achieve PASI 90 in ~60% of plaque psoriasis patients at 16 weeks."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "IL-31 contributes to pruritus in psoriasis despite the Th17 cytokine environment; psoriatic skin ILC2 cells produce IL-31; IL-31 correlates with itch VAS independently of PASI; JAK inhibitors (deucravacitinib, upadacitinib) reduce psoriatic inflammation and IL-31-mediated itch."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Narrow-band UVB (311–313 nm) phototherapy induces T-cell apoptosis in psoriatic plaques and suppresses the Th17/IL-17A axis; NBUVB achieves PASI 75 in 50–70% of patients; safe in pregnancy; requires 2–3 sessions/week for 6–10 weeks induction."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "Psoriasis and AS sit on the spondyloarthritis spectrum, sharing the IL-23/Th17→IL-17A axis and responding to IL-17 (secukinumab, ixekizumab) and IL-23 blockade; ~20-30% of psoriasis patients develop inflammatory arthritis, and axial psoriatic arthritis overlaps with AS."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Up to ~30% of plaque-psoriasis patients develop psoriatic arthritis, usually years after skin disease; both share the IL-23/Th17→IL-17A/TNF axis, so IL-17, IL-23 and TNF inhibitors treat skin and joints together; nail and scalp psoriasis flag higher PsA risk."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Psoriasis is the archetypal immune-mediated skin disease: Th17-derived IL-17A/IL-22 drive keratinocyte hyperproliferation → thickened scaly plaques with parakeratosis and acanthosis; epidermal turnover shortens from ~28 to ~4 days, and skin is the primary treated site."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Psoriasis and atopic dermatitis are the two major inflammatory skin diseases but immunologically opposite: psoriasis is Th17/IL-23-driven with sharp scaly plaques, while atopic dermatitis is Th2-driven with itchy, ill-defined eczema—dictating different biologics."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Psoriasis and inflammatory bowel disease share the IL-23/Th17 axis and co-occur: both respond to anti-IL-23 and anti-TNF biologics, though anti-IL-17 can paradoxically worsen Crohn's—so the shared pathway also constrains drug choice across the two diseases."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Psoriasis is an independent cardiovascular risk factor: chronic systemic Th17 inflammation accelerates atherosclerosis, so severe psoriasis raises heart attack and stroke risk beyond shared metabolic factors—and effective skin treatment may lower vascular inflammation."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Psoriasis and obesity are bidirectionally linked through inflammation: adipose-derived cytokines worsen psoriatic inflammation, while psoriasis raises metabolic-syndrome risk, so obese psoriasis patients have more severe disease and weight loss improves it."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Psoriasis raises the risk of type 2 diabetes: shared systemic inflammation (TNF, IL-6, IL-17) drives insulin resistance, so psoriasis is an independent cardiometabolic risk factor—part of why it is now treated as a systemic, not just skin, disease."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D both treats and modulates psoriasis: topical vitamin D analogs slow the hyperproliferation of psoriatic keratinocytes and are first-line therapy, while the immunomodulatory role of vitamin D ties skin immunity to this hormone—a vitamin used as a drug."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Psoriasis is an independent cardiovascular risk factor: systemic IL-17/TNF inflammation accelerates atherosclerosis, so severe psoriasis raises heart-attack and stroke risk beyond its shared metabolic-syndrome links—reframing it as more than a skin disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Plasmacytoid dendritic cells ignite psoriasis: they sense self-DNA and release type I interferon that, with myeloid dendritic cells, launches the IL-23/Th17 cascade—so dendritic cells sit at the very start of the inflammatory loop that thickens the skin."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12/IL-23 sit at the heart of psoriasis: their shared p40 subunit drives the Th1/Th17 response that fuels keratinocyte hyperproliferation, which is why ustekinumab (anti-p40) and IL-23-specific biologics clear psoriasis plaques so effectively."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils mark the psoriatic plaque: they swarm into the epidermis to form Munro microabscesses, and in pustular psoriasis they fill visible pustules—so although T cells drive the disease, neutrophils are its histologic signature and dominate its pustular forms."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Strep throat can ignite psoriasis: streptococcal infection classically triggers guttate psoriasis, especially in children, as bacterial superantigens activate T cells that cross-react with skin—one of the clearest infection-to-autoimmunity links in dermatology."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Psoriasis carries a heavy mental-health toll: visible plaques, stigma, and chronic inflammation roughly double the risk of depression and suicidal thoughts, so screening for depression is part of good psoriasis care—and clearing skin often lifts mood."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Oral JAK and TYK2 inhibitors now treat psoriasis: blocking JAK-family signaling downstream of IL-23 and other cytokines (e.g., deucravacitinib targeting TYK2) controls plaques without injections, extending the IL-23/IL-17-targeted revolution to pills."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Psoriasis and fatty-liver disease travel together: shared systemic inflammation and metabolic syndrome raise the risk of MASH in psoriasis patients, part of why psoriasis is now seen as a systemic inflammatory disease, not just skin-deep."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psoriasis plaques recur in the same spots because of cytotoxic T cells: epidermal resident-memory CD8 T cells persist after lesions clear, forming a 'disease memory' that reignites plaques at old sites—why the disease relapses where it was."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Psoriasis is first treated with cortisol's kin: topical corticosteroids calm the IL-17/Th17 inflammation driving the plaques, the most-used therapy—though rebound on stopping and skin thinning limit long-term potent use."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Psoriasis is treated by restoring keratinocyte calcium signaling: vitamin D analogs (calcipotriol) normalize the calcium-dependent differentiation that runs amok in psoriatic skin, slowing the overgrowth—often paired with a steroid."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Psoriasis reflects failed restraint by regulatory T cells: dysfunctional Tregs let the IL-23/Th17 axis run unchecked against the skin, so the imbalance between effector and regulatory T cells underlies the chronic plaques."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Psoriasis travels with fatty liver: its systemic inflammation and shared metabolic syndrome make non-alcoholic fatty liver disease common, and the methotrexate used to treat psoriasis can itself scar the liver, so liver health must be watched."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Psoriatic plaques are richly vascular: VEGF drives dermal endothelial cells to build dilated, leaky capillaries near the surface, which is why scraping a plaque produces pinpoint bleeding (the Auspitz sign)."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Salt may inflame psoriasis: high sodium accumulates in skin and pushes naive T cells toward the IL-17-producing Th17 lineage that drives psoriatic plaques, a dietary link between salt and the disease's core immune axis."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Psoriasis itches and reacts through nerves: sensory peripheral-nerve fibers, fired by IL-31 and inflammation, carry the itch, and nerve injury can clear plaques in a denervated patch—evidence the skin's nerves help sustain the disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Psoriasis is more than skin-deep: its systemic inflammation accelerates atherosclerosis, so severe disease raises the risk of heart attack independently of the usual cardiovascular risk factors."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells lurk in psoriatic skin: degranulating near nerves and vessels, they release mediators that amplify the early inflammation and itch, linking neurogenic triggers to the plaque."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the psoriatic plaque's hyperdrive: keratinocytes pile up far too fast with retained nuclei in the surface scale, and neutrophils collect into Munro microabscesses, the ultrastructure of runaway epidermal turnover."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Psoriasis can inflame the eye: it is associated with uveitis, conjunctivitis, and dry, scaly blepharitis of the lids, ocular involvement that parallels the immune attack on the skin and joints."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc matters to the psoriatic skin: levels often run low in the rapidly shedding epidermis, and because the mineral fuels skin repair and tempers inflammation, its deficiency can aggravate the plaques."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Psoriasis itches and flares through the nerves: sensory neurons in the plaque release substance P and CGRP that fuel neurogenic inflammation, the same wiring behind the stress-triggered flares and the maddening itch."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Treating psoriasis keeps an eye on the lungs: methotrexate can rarely cause a hypersensitivity pneumonitis, and the TNF and IL-17 biologics that clear the plaques raise the risk of pneumonia and reactivated tuberculosis."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Psoriasis and fat inflame each other: enlarged adipocytes pour out the same cytokines that drive the plaques, so obesity worsens psoriasis and blunts treatment — a metabolic link in the 'psoriatic march' toward heart disease."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies revolutionized psoriasis care: monoclonal antibodies against TNF, IL-17, and IL-23 (secukinumab, guselkumab, ustekinumab) clear the plaques by neutralizing the exact cytokines driving them, often where older drugs failed."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Skin disease reaches intimate places: genital psoriasis and the visible plaques impair sexual health and self-image, while pregnancy often calms psoriasis through its immune shift, only for it to flare again after delivery."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "A gut-skin axis links plaque to flora: psoriasis patients show gut dysbiosis and a high overlap with inflammatory bowel disease, the shared mucosal-barrier and IL-23 immunology tying the bowel's microbes to the skin's inflammation."
  - target: 01-human/03-molecular/il-36
    relation: connects-to
    note: "A different cytokine drives the pustular form: in generalized pustular psoriasis, loss of the IL-36 receptor antagonist unleashes IL-36, flooding the skin with neutrophils into sterile pustules — now treatable by the IL-36 blocker spesolimab."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Plaques keep their own inflammatory engine: dermal macrophages pour out TNF and recruit more immune cells, sustaining the lesion and feeding the systemic inflammation that links psoriasis to heart and metabolic disease."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV paradoxically ignites psoriasis: as immunity collapses the disease often appears or turns severe and treatment-resistant, a striking exception to its T-cell-driven model that improves with antiretroviral therapy."
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
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 from dermal DCs activates Th17 and γδ T cells → IL-17A/F and IL-22 → keratinocyte hyperproliferation, acanthosis, and neutrophil recruitment in psoriatic plaques; anti-IL-23p19 antibodies (risankizumab, guselkumab) achieve PASI 90 response in ~50% of patients.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A from skin Th17 and γδ T cells activates keratinocyte IL-17RA/RC → NF-kB → CXCL8, S100A proteins, and AMPs → neutrophil influx and epidermal hyperproliferation; secukinumab (anti-IL-17A) and ixekizumab achieve PASI 90 in ~60% of plaque psoriasis patients at 16 weeks.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — IL-31 contributes to pruritus in psoriasis despite the Th17 cytokine environment; psoriatic skin ILC2 cells produce IL-31; IL-31 correlates with itch VAS independently of PASI; JAK inhibitors (deucravacitinib, upadacitinib) reduce psoriatic inflammation and IL-31-mediated itch.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Narrow-band UVB (311–313 nm) phototherapy induces T-cell apoptosis in psoriatic plaques and suppresses the Th17/IL-17A axis; NBUVB achieves PASI 75 in 50–70% of patients; safe in pregnancy; requires 2–3 sessions/week for 6–10 weeks induction.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — Psoriasis and AS sit on the spondyloarthritis spectrum, sharing the IL-23/Th17→IL-17A axis and responding to IL-17 (secukinumab, ixekizumab) and IL-23 blockade; ~20-30% of psoriasis patients develop inflammatory arthritis, and axial psoriatic arthritis overlaps with AS.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Up to ~30% of plaque-psoriasis patients develop psoriatic arthritis, usually years after skin disease; both share the IL-23/Th17→IL-17A/TNF axis, so IL-17, IL-23 and TNF inhibitors treat skin and joints together; nail and scalp psoriasis flag higher PsA risk.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Psoriasis is the archetypal immune-mediated skin disease: Th17-derived IL-17A/IL-22 drive keratinocyte hyperproliferation → thickened scaly plaques with parakeratosis and acanthosis; epidermal turnover shortens from ~28 to ~4 days, and skin is the primary treated site.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Psoriasis and atopic dermatitis are the two major inflammatory skin diseases but immunologically opposite: psoriasis is Th17/IL-23-driven with sharp scaly plaques, while atopic dermatitis is Th2-driven with itchy, ill-defined eczema—dictating different biologics.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Psoriasis and inflammatory bowel disease share the IL-23/Th17 axis and co-occur: both respond to anti-IL-23 and anti-TNF biologics, though anti-IL-17 can paradoxically worsen Crohn's—so the shared pathway also constrains drug choice across the two diseases.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Psoriasis is an independent cardiovascular risk factor: chronic systemic Th17 inflammation accelerates atherosclerosis, so severe psoriasis raises heart attack and stroke risk beyond shared metabolic factors—and effective skin treatment may lower vascular inflammation.
- `connects-to` → **[Obesity](../obesity/README.md)** — Psoriasis and obesity are bidirectionally linked through inflammation: adipose-derived cytokines worsen psoriatic inflammation, while psoriasis raises metabolic-syndrome risk, so obese psoriasis patients have more severe disease and weight loss improves it.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Psoriasis raises the risk of type 2 diabetes: shared systemic inflammation (TNF, IL-6, IL-17) drives insulin resistance, so psoriasis is an independent cardiometabolic risk factor—part of why it is now treated as a systemic, not just skin, disease.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D both treats and modulates psoriasis: topical vitamin D analogs slow the hyperproliferation of psoriatic keratinocytes and are first-line therapy, while the immunomodulatory role of vitamin D ties skin immunity to this hormone—a vitamin used as a drug.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Psoriasis is an independent cardiovascular risk factor: systemic IL-17/TNF inflammation accelerates atherosclerosis, so severe psoriasis raises heart-attack and stroke risk beyond its shared metabolic-syndrome links—reframing it as more than a skin disease.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Plasmacytoid dendritic cells ignite psoriasis: they sense self-DNA and release type I interferon that, with myeloid dendritic cells, launches the IL-23/Th17 cascade—so dendritic cells sit at the very start of the inflammatory loop that thickens the skin.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12/IL-23 sit at the heart of psoriasis: their shared p40 subunit drives the Th1/Th17 response that fuels keratinocyte hyperproliferation, which is why ustekinumab (anti-p40) and IL-23-specific biologics clear psoriasis plaques so effectively.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils mark the psoriatic plaque: they swarm into the epidermis to form Munro microabscesses, and in pustular psoriasis they fill visible pustules—so although T cells drive the disease, neutrophils are its histologic signature and dominate its pustular forms.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — Strep throat can ignite psoriasis: streptococcal infection classically triggers guttate psoriasis, especially in children, as bacterial superantigens activate T cells that cross-react with skin—one of the clearest infection-to-autoimmunity links in dermatology.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Psoriasis carries a heavy mental-health toll: visible plaques, stigma, and chronic inflammation roughly double the risk of depression and suicidal thoughts, so screening for depression is part of good psoriasis care—and clearing skin often lifts mood.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Oral JAK and TYK2 inhibitors now treat psoriasis: blocking JAK-family signaling downstream of IL-23 and other cytokines (e.g., deucravacitinib targeting TYK2) controls plaques without injections, extending the IL-23/IL-17-targeted revolution to pills.
- `connects-to` → **[NASH](../nash/README.md)** — Psoriasis and fatty-liver disease travel together: shared systemic inflammation and metabolic syndrome raise the risk of MASH in psoriasis patients, part of why psoriasis is now seen as a systemic inflammatory disease, not just skin-deep.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psoriasis plaques recur in the same spots because of cytotoxic T cells: epidermal resident-memory CD8 T cells persist after lesions clear, forming a 'disease memory' that reignites plaques at old sites—why the disease relapses where it was.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Psoriasis is first treated with cortisol's kin: topical corticosteroids calm the IL-17/Th17 inflammation driving the plaques, the most-used therapy—though rebound on stopping and skin thinning limit long-term potent use.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Psoriasis is treated by restoring keratinocyte calcium signaling: vitamin D analogs (calcipotriol) normalize the calcium-dependent differentiation that runs amok in psoriatic skin, slowing the overgrowth—often paired with a steroid.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Psoriasis reflects failed restraint by regulatory T cells: dysfunctional Tregs let the IL-23/Th17 axis run unchecked against the skin, so the imbalance between effector and regulatory T cells underlies the chronic plaques.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Psoriasis travels with fatty liver: its systemic inflammation and shared metabolic syndrome make non-alcoholic fatty liver disease common, and the methotrexate used to treat psoriasis can itself scar the liver, so liver health must be watched.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Psoriatic plaques are richly vascular: VEGF drives dermal endothelial cells to build dilated, leaky capillaries near the surface, which is why scraping a plaque produces pinpoint bleeding (the Auspitz sign).
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Salt may inflame psoriasis: high sodium accumulates in skin and pushes naive T cells toward the IL-17-producing Th17 lineage that drives psoriatic plaques, a dietary link between salt and the disease's core immune axis.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Psoriasis itches and reacts through nerves: sensory peripheral-nerve fibers, fired by IL-31 and inflammation, carry the itch, and nerve injury can clear plaques in a denervated patch—evidence the skin's nerves help sustain the disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Psoriasis is more than skin-deep: its systemic inflammation accelerates atherosclerosis, so severe disease raises the risk of heart attack independently of the usual cardiovascular risk factors.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells lurk in psoriatic skin: degranulating near nerves and vessels, they release mediators that amplify the early inflammation and itch, linking neurogenic triggers to the plaque.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the psoriatic plaque's hyperdrive: keratinocytes pile up far too fast with retained nuclei in the surface scale, and neutrophils collect into Munro microabscesses, the ultrastructure of runaway epidermal turnover.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Psoriasis can inflame the eye: it is associated with uveitis, conjunctivitis, and dry, scaly blepharitis of the lids, ocular involvement that parallels the immune attack on the skin and joints.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc matters to the psoriatic skin: levels often run low in the rapidly shedding epidermis, and because the mineral fuels skin repair and tempers inflammation, its deficiency can aggravate the plaques.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Psoriasis itches and flares through the nerves: sensory neurons in the plaque release substance P and CGRP that fuel neurogenic inflammation, the same wiring behind the stress-triggered flares and the maddening itch.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Treating psoriasis keeps an eye on the lungs: methotrexate can rarely cause a hypersensitivity pneumonitis, and the TNF and IL-17 biologics that clear the plaques raise the risk of pneumonia and reactivated tuberculosis.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Psoriasis and fat inflame each other: enlarged adipocytes pour out the same cytokines that drive the plaques, so obesity worsens psoriasis and blunts treatment — a metabolic link in the 'psoriatic march' toward heart disease.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies revolutionized psoriasis care: monoclonal antibodies against TNF, IL-17, and IL-23 (secukinumab, guselkumab, ustekinumab) clear the plaques by neutralizing the exact cytokines driving them, often where older drugs failed.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Skin disease reaches intimate places: genital psoriasis and the visible plaques impair sexual health and self-image, while pregnancy often calms psoriasis through its immune shift, only for it to flare again after delivery.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — A gut-skin axis links plaque to flora: psoriasis patients show gut dysbiosis and a high overlap with inflammatory bowel disease, the shared mucosal-barrier and IL-23 immunology tying the bowel's microbes to the skin's inflammation.
- `connects-to` → **[IL-36](../../03-molecular/il-36/README.md)** — A different cytokine drives the pustular form: in generalized pustular psoriasis, loss of the IL-36 receptor antagonist unleashes IL-36, flooding the skin with neutrophils into sterile pustules — now treatable by the IL-36 blocker spesolimab.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Plaques keep their own inflammatory engine: dermal macrophages pour out TNF and recruit more immune cells, sustaining the lesion and feeding the systemic inflammation that links psoriasis to heart and metabolic disease.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV paradoxically ignites psoriasis: as immunity collapses the disease often appears or turns severe and treatment-resistant, a striking exception to its T-cell-driven model that improves with antiretroviral therapy.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^nestle-2009-psoriasis-review]: Nestle FO, Kaplan DH, Barker J. Psoriasis. *N Engl J Med.* 2009;361(5):496-509. [doi:10.1056/NEJMra0804595](https://doi.org/10.1056/NEJMra0804595) · [PubMed 19641206](https://pubmed.ncbi.nlm.nih.gov/19641206/)
[^langley-2014-secukinumab]: Langley RG, Elewski BE, Lebwohl M, et al. Secukinumab in plaque psoriasis — results of two phase 3 trials. *N Engl J Med.* 2014;371(4):326-338. [doi:10.1056/NEJMoa1406095](https://doi.org/10.1056/NEJMoa1406095) · [PubMed 25007392](https://pubmed.ncbi.nlm.nih.gov/25007392/)
[^gordon-2018-risankizumab]: Gordon KB, Strober B, Lebwohl M, et al. Efficacy and safety of risankizumab in moderate-to-severe plaque psoriasis (UltIMMa-1 and UltIMMa-2). *Lancet.* 2018;392(10148):650-661. [doi:10.1016/S0140-6736(18)31713-6](https://doi.org/10.1016/S0140-6736(18)31713-6) · [PubMed 30097359](https://pubmed.ncbi.nlm.nih.gov/30097359/)
