---
schema: human-scale-entry/v1
id: integumentary-system
name: Integumentary System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-05
summary: "Skin, hair, nails, and glands (~2 m², 4 kg) forming the body's primary physical and immunological barrier, regulating temperature via sweating and vasomotion, and synthesizing vitamin D from UVB."
aliases: ["skin system", "cutaneous system", "dermis", "epidermis", "skin and appendages"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/04-cellular/dendritic-cell
    relation: contains
    note: "Langerhans cells are epidermal DCs (CD207+/langerin+, MHCII+) forming a surveillance network; they capture antigens and migrate to skin-draining lymph nodes to prime T cells; keratinocyte TSLP activates LCs toward Th2-skewing."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Skin harbours Langerhans cells, dermal DCs, mast cells, and macrophages; keratinocyte-derived TSLP, IL-25, IL-33 drive type 2 allergic responses; filaggrin mutations break the barrier → atopic march (eczema→asthma→rhinitis)."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Skin contains ~1 million sensory receptors: TRPV1/TRPA1 (pain/temp), Meissner corpuscles (discriminative touch), Pacinian (vibration), Merkel discs (sustained touch), Ruffini (stretch); processed via dorsal horn → thalamus → cortex."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Cutaneous vasodilation (AV anastomoses) is the primary thermoregulatory cardiovascular response; 15% of CO reaches skin at rest, up to 60% during heat stress; vasoconstriction in shock redistributes blood to vital organs."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: infected-by
    note: "HPV-16 infects basal keratinocytes of stratified squamous epithelium at the cervical transformation zone; L1 binds heparan sulphate proteoglycans at microtrauma sites; viral replication is stratification-coupled — L1/L2 expressed only in terminally differentiated keratinocytes."
---

# Integumentary System

## Overview

The integumentary system is the body's largest organ by surface area (~1.5–2.0 m²) and mass (~4 kg, approximately 6–8% of body weight), comprising the skin and its derivatives — hair follicles, sebaceous glands, eccrine and apocrine sweat glands, and nails [^guyton-hall]. As the boundary between the organism and the external environment, the integumentary system simultaneously performs functions that few other organ systems can match in breadth: physical and chemical barrier, immune surveillance, thermoregulation, sensory transduction, vitamin D photosynthesis, and wound healing.

The critical insight about skin is that it is not merely a passive barrier. The epidermis actively manufactures a multi-layered impermeability barrier (the cornified envelope, lipid lamellae, and tight junctions) whose integrity requires ongoing keratinocyte turnover every ~28 days. Simultaneously, the skin houses a resident immune network — Langerhans cells, dermal dendritic cells, mast cells, macrophages, and T cells — that is constantly sampling environmental antigens and calibrating systemic immune tone.

## Structure

### Epidermis

The epidermis is a stratified squamous keratinising epithelium, ranging from 0.05 mm (eyelids) to 1.5 mm (palms and soles), completely renewed every ~28 days [^guyton-hall].

**Layers (superficial to deep)**:

| Layer | Key features |
|:---|:---|
| **Stratum corneum** | 15–30 layers of dead anucleate corneocytes embedded in lipid lamellae (ceramides, cholesterol, fatty acids); primary permeability barrier; transepidermal water loss (TEWL) <5 g/m²/h normal |
| **Stratum lucidum** | Present only in thick skin (palms, soles); homogeneous, densely packed cells |
| **Stratum granulosum** | Keratohyalin granules (filaggrin, loricrin, involucrin → cornified cell envelope); lamellar body exocytosis → lipid lamellae; tight junctions (claudin-1/4) — inner permeability barrier |
| **Stratum spinosum** | Keratin 1/10 expression; abundant desmosomes (desmoglein 1/3 — target in pemphigus); Langerhans cells here |
| **Stratum basale** | Single layer of proliferating basal keratinocytes (KRT5/KRT14, Ki67+); hemidesmosomes (integrin α6β4 → laminin-332 → basement membrane); melanocytes (1:10 basal keratinocytes); Merkel cells (mechanoreceptors, neuroendocrine, synapse with Aβ fibres) |

**Resident non-keratinocyte cells**:
- **Melanocytes**: neural crest-derived; produce melanin (eumelanin [brown-black] and pheomelanin [yellow-red]) via tyrosinase, TYRP1, DOPA-chrome tautomerase; transfer melanosomes to keratinocytes via filopodia; melanin caps nuclei → UV photo-protection; 1:10 basal ratio
- **Langerhans cells (LCs)**: bone marrow-derived DCs residing in stratum spinosum; CD1a+, CD207+/langerin+ (forms Birbeck granules — X-shaped ECS compartments), MHCII+; form a tight surveillance network via long dendritic processes between keratinocytes; upon skin injury or allergen capture, LCs mature and migrate to lymph nodes via dermal lymphatics
- **Merkel cells**: slowly adapting mechanoreceptors at the epidermal-dermal junction, particularly in fingertips, lips; synapse with Aβ Merkel neurite complex → sustained pressure and texture discrimination; also neuroendocrine (somatostatin, VIP, CGRP expression)

### Dermis

The dermis (0.5–3 mm) is a dense fibrous connective tissue providing mechanical strength (tensile strength up to 5 MPa) and housing all skin appendages, blood/lymphatic vessels, and sensory nerves [^guyton-hall].

- **Papillary dermis** (superficial): thin, loose connective tissue; dermal papillae interdigitating with epidermal rete ridges → increases surface area → fingerprints; type III collagen, fine elastic fibres; capillary loops supplying epidermis; Meissner corpuscles (rapidly adapting, discriminative touch, fingers/lips)
- **Reticular dermis** (deep): thick, dense irregular connective tissue; type I collagen bundles (oriented along Langer's lines — skin tension lines, relevant to surgical incisions); coarse elastic fibres (elastin + fibrillin); fibroblasts (fibroblastic reticular cells) producing collagens, GAGs (hyaluronic acid, decorin, versican), fibronectin; mast cells (armed with IgE, histamine, tryptase, prostaglandins, leukotrienes — allergy); macrophages; sensory nerve endings — Pacinian corpuscles (rapidly adapting, vibration/deep pressure, fingers/genitalia), Ruffini endings (slowly adapting, skin stretch, joint position); free nerve endings (Aδ and C fibres — pain, temperature, itch [pruriceptors])

**Hypodermis/subcutis**: technically below the dermis (not part of skin proper); adipose tissue + loose connective tissue providing thermal insulation, mechanical cushioning, and energy storage; anchors skin to underlying fascia.

### Skin Appendages

**Hair follicles**: complex mini-organs cycling through anagen (active growth, 2–7 years on scalp), catagen (regression, ~2–3 weeks), and telogen (resting, ~3 months) under control of WNT/BMP signals from the dermal papilla (DP) and IGF-1, androgens, and thyroid hormone systemically.

**Sebaceous glands**: holocrine glands (whole cell disintegrates releasing sebum — triglycerides, wax esters, squalene, cholesterol, free fatty acids); sebum waterproofs hair, is antimicrobial (FAs inhibit Staphylococcus aureus, Streptococcus), and contributes to skin surface pH (~5.5 — acid mantle). Androgen-sensitive (testosterone → DHT via 5α-reductase → sebaceous hyperplasia → acne in adolescence).

**Eccrine sweat glands**: 2–4 million, distributed across the body (densest on palms, soles, axilla, forehead); coiled secretory tubule (deeper, produces isotonic primary secretion: NaCl + water + small molecules, stimulated by cholinergic [muscarinic M3] innervation under hypothalamic thermoregulatory control) + straight duct (reabsorbs NaCl → hypotonic final sweat; active Na⁺ absorption via ENaC + CFTR Cl⁻ channel — defective in cystic fibrosis → salty sweat); can produce 1–2 L/h/m² in maximum heat stress.

**Apocrine glands**: larger, in axilla, groin, areolae; open into hair follicle above sebaceous gland; produce viscous, protein-rich secretion triggered by emotional (adrenergic) rather than thermal stimuli; secretion odourless until modified by skin microbiota (Corynebacterium spp., Staphylococcus spp.) → body odour.

**Nails**: hard keratin plates (KRT86, KRT31) produced by nail matrix; growth ~3 mm/month (fingernails), ~1 mm/month (toenails); lunula (visible portion of matrix); nail plate rests on vascular nail bed → pink appearance; reflects systemic disease (Muehrcke's lines — hypoalbuminaemia; Beau's lines — systemic illness/chemotherapy; koilonychia — iron deficiency; clubbing — hypoxia/malignancy/cirrhosis; half-and-half nails [Lindsay's nails] — renal failure; yellow nail syndrome — lymphoedema).

## Function

### Barrier Functions

**Physical barrier**: stratum corneum provides primary defence against water loss (TEWL), mechanical trauma, and transcutaneous chemical penetration. The brick-and-mortar structure (corneocytes = bricks; lipid lamellae [ceramides, cholesterol, FAs] = mortar) creates a tortuous diffusion path. TEWL increases dramatically in eczema (filaggrin deficiency), burns, and psoriasis (rapid turnover) [^guyton-hall].

**Microbial barrier**: skin surface pH ~5.5 (acid mantle from lactic acid, FAs) inhibits pathogen colonization; AMPs (defensins, cathelicidin LL-37, dermcidin in sweat) kill bacteria, fungi, and some viruses; the skin microbiome (~1.8 million bacteria/cm² on face; dominated by Cutibacterium [sebaceous sites], Staphylococcus [moist sites], Corynebacterium [moist/dry sites], Malassezia [sebaceous sites]) competes with pathogens.

### Immunological Functions

The skin is a primary immunological organ, not merely a physical barrier [^alberts-mol-cell-biology]. Key mechanisms:
- Keratinocyte TSLP (thymic stromal lymphopoietin), IL-25 (IL-17E), and IL-33 are the three canonical epithelial alarmins that activate ILC2s, DCs, and mast cells to initiate type 2 immune responses (eosinophilia, IgE production, goblet cell metaplasia) — the atopic march: atopic dermatitis → food allergy → allergic asthma → allergic rhinitis follows barrier disruption and sensitisation
- Langerhans cells form a continuous monitoring network in the epidermis, capturing antigens and presenting to naïve T cells in draining lymph nodes; they are responsible for allergic contact sensitisation (e.g., nickel, poison ivy urushiol → Th1/Th17 contact hypersensitivity)
- Dermal macrophages and DCs provide ongoing innate surveillance; mast cells (FcεRI armed with IgE) trigger immediate hypersensitivity reactions (urticaria, angioedema, anaphylaxis) upon allergen re-exposure

### Thermoregulation

Body temperature homeostasis at 37°C is mediated primarily through cutaneous blood flow and eccrine sweating [^guyton-hall]:

- **Heat dissipation**: preoptic nucleus of anterior hypothalamus detects rising core T° → sympathetic cholinergic fibres → eccrine glands → sweat (evaporative cooling, up to ~580 kcal/L evaporated); simultaneously, cutaneous vasodilation (sympathetic noradrenergic withdrawal + active cholinergic vasodilator fibres) → ↑blood flow through cutaneous AV anastomoses (arteriovenous shunts in fingertips, toes, nose, ears — glomus bodies) → convective/radiative heat loss. At maximum heat load, up to 60% of cardiac output can be redirected to skin.
- **Heat conservation**: cold → sympathetic vasoconstriction → ↓cutaneous blood flow → ↓heat loss; piloerection (arrector pili muscles, adrenergic) → small insulating air layer (vestigial in humans); shivering thermogenesis (skeletal muscle — see Musculoskeletal System entry)

### Sensory Functions

Five classes of mechanoreceptors transduce distinct mechanical stimuli [^guyton-hall]:
| Receptor | Adaptation | Stimulus | Location |
|:---|:---|:---|:---|
| Meissner corpuscles | Rapidly adapting | Discriminative touch, flutter (10–50 Hz) | Dermal papillae, glabrous skin |
| Pacinian corpuscles | Rapidly adapting | Vibration (200–300 Hz), deep pressure | Reticular dermis, periosteum |
| Merkel discs | Slowly adapting I | Sustained pressure, edges, texture | Stratum basale, fingertips |
| Ruffini endings | Slowly adapting II | Skin stretch, joint position | Reticular dermis |
| Free nerve endings | Not encapsulated | Pain (Aδ, C), temperature (TRPV1 heat; TRPM8 cold), itch (C-pruriceptors via TRPA1) | Epidermis/dermis |

### Vitamin D Synthesis

Skin is the only site of vitamin D₃ (cholecalciferol) biosynthesis [^guyton-hall]: UVB photons (290–320 nm) convert 7-dehydrocholesterol (7-DHC) → pre-vitamin D₃ (thermally isomerises to vitamin D₃). Vitamin D₃ → liver (CYP2R1/CYP27A1 → 25-OH vitamin D₃ [calcidiol, t½ ~3 weeks, stored; serum marker of vitamin D status]) → kidney (CYP27B1 in proximal tubule, stimulated by PTH and low Pi → 1,25(OH)₂D₃ [calcitriol, active hormone]). Calcitriol acts via VDR (nuclear receptor): ↑duodenal Ca²⁺ absorption (TRPV6, calbindin), ↑renal Ca²⁺ reabsorption, ↑osteoclastogenesis (RANKL), ↑muscle function, ↓PTH, immune modulation (↑Treg, ↓Th17). Synthesis declines with age (↓7-DHC in elderly skin), high latitude, dark skin (melanin competes for UVB), and sun avoidance.

### Wound Healing

Wound healing is a precisely orchestrated process in four overlapping phases [^guyton-hall][^alberts-mol-cell-biology]:

**1. Haemostasis (0–2 hours)**: vessel injury → vasoconstriction (thromboxane A₂) + platelet adhesion (collagen → vWF → GpIb-IX-V → GpIIb/IIIa → fibrinogen crosslinking) + coagulation cascade (tissue factor → thrombin → fibrin clot + platelet plug). Platelets release PDGF, TGF-β, EGF from α-granules → recruit repair cells.

**2. Inflammation (0–7 days)**: neutrophils (day 0–3, recruited via CXCL8/IL-8) → débridement of bacteria and matrix fragments → NET release; mast cells → histamine → vasodilation/permeability. Macrophages (monocyte-derived, day 3 onwards): M1 phase (classical, pro-inflammatory: IL-1β, TNF-α, IL-6, CXCL8 → kill bacteria, amplify inflammation) → M2 phase (alternative, day 5+: TGF-β, VEGF, PDGF, IGF-1 → initiate repair, angiogenesis).

**3. Proliferation (days 3–21)**: key events driven by macrophage and keratinocyte growth factors (EGF, TGF-α, KGF/FGF7):
- **Re-epithelialisation**: basal keratinocytes at wound margins dedifferentiate (↓E-cadherin, integrin switch to αvβ6) → migrate across fibrin provisional matrix → proliferate → stratify
- **Fibroplasia**: dermal fibroblasts proliferate and deposit type III collagen (granulation tissue); myofibroblasts (α-SMA+ fibroblasts, driven by TGF-β + mechanical tension) contract the wound
- **Angiogenesis**: VEGF-A/C from macrophages → VEGFR2 on endothelial cells → new capillaries (hypervascular granulation tissue — "proud flesh")

**4. Remodelling (weeks–months–years)**: type III collagen progressively replaced by type I collagen (stronger); MMPs (MMP-1/collagenase, MMP-2/gelatinase, MMP-9) regulated by TIMPs; scar matures → ↓cellularity → ↓vascularity → white avascular scar. Keloids (excess collagen, overactive TGF-β signalling, extends beyond wound margins) and hypertrophic scars (within wound margins) represent pathological remodelling.

## Connections

- **Contains:** [dendritic-cell](../../04-cellular/dendritic-cell/README.md) — Langerhans cells are epidermal DCs forming a continuous antigen-surveillance network
- **Modulates:** [immune-system](../../07-system/immune-system/README.md) — epithelial alarmins (TSLP, IL-25, IL-33) drive systemic type 2 immunity; barrier defects initiate atopic march
- **Modulates:** [nervous-system](../../07-system/nervous-system/README.md) — ~1 million cutaneous sensory receptors transduce touch, pain, temperature, itch; central processing via dorsal horn → thalamus → somatosensory cortex
- **Modulates:** [cardiovascular-system](../../07-system/cardiovascular-system/README.md) — cutaneous vasodilation/vasoconstriction controls up to 60% of cardiac output for thermoregulation
- `infected-by` → **[HPV-16](../../../../02-pathogen/01-viruses/hpv-16/README.md)** — HPV-16 infects basal keratinocytes of stratified squamous epithelium at the cervical transformation zone; L1 binds heparan sulphate proteoglycans at microtrauma sites; viral replication is stratification-coupled — L1/L2 expressed only in terminally differentiated keratinocytes.

## Pathology

### Atopic Dermatitis (Eczema)

Loss-of-function mutations in **filaggrin** (FLG, chromosome 1q21) — the key cornified envelope protein — weaken the epidermal barrier → ↑TEWL, ↑allergen penetration, ↑keratinocyte alarmins (TSLP, IL-33, IL-25) → DC and ILC2 activation → Th2 polarisation → IL-4/IL-13 (suppress FLG and other barrier proteins, creating a vicious cycle) + IL-31 (type 2 cytokine, major itch mediator via IL-31RA/OSMR on dorsal root ganglia sensory neurons). Prevalence: 15–20% of children, 7–10% of adults. Standard: topical corticosteroids, topical calcineurin inhibitors (tacrolimus); biologics: dupilumab (anti-IL-4Rα → blocks IL-4 and IL-13 simultaneously); JAK inhibitors (baricitinib, upadacitinib — targeting JAK1/2-STAT6 downstream of IL-4/IL-13/IL-31).

### Psoriasis

Chronic, immune-mediated skin disease characterised by rapid keratinocyte turnover (epidermis renews in 4 days instead of 28) driven by Th17 cells and IL-17A (via keratinocyte IL-17RA → NF-κB → antimicrobial peptides + chemokines → neutrophil recruitment → Munro microabscesses). Plaques: well-demarcated, erythematous, silver-scaled; Auspitz sign (pinpoint bleeding on scale removal — dilated dermal capillaries). Systemic inflammation: psoriatic arthritis (30%), cardiovascular risk (↑C-reactive protein, ↑IL-6, ↑TNF-α). Therapy: topical corticosteroids/vitamin D analogues → phototherapy (NB-UVB) → systemic (methotrexate, acitretin, ciclosporin) → biologics (anti-TNF [adalimumab], anti-IL-12/23 [ustekinumab], anti-IL-17A [secukinumab, ixekizumab], anti-IL-23 [risankizumab]).

### Melanoma

Malignant transformation of melanocytes: UV-induced DNA damage (cyclobutane pyrimidine dimers) → mutations in BRAF (V600E, ~50%), NRAS (20%), NF1 (15%), CDKN2A, TERT. BRAF V600E → constitutively active MEK/ERK → ↑proliferation, ↑survival. Metastatic melanoma: poor prognosis prior to 2011 (median OS <12 months). Targeted therapy: BRAF inhibitors (vemurafenib, dabrafenib) + MEK inhibitors (trametinib, cobimetinib) → rapid responses but acquired resistance via NRAS mutations/BRAF amplification. Immunotherapy: ipilimumab (anti-CTLA4), nivolumab/pembrolizumab (anti-PD-1) → durable responses (40% 5-year OS in metastatic setting). Combined ipilimumab + nivolumab: ~50% objective response rate.

### Burns

Depth classification: superficial (epidermal only — erythema, no blistering; heals 3–5 days); partial-thickness superficial (epidermis + papillary dermis — blisters, painful, intact sensation; heals 7–21 days from follicle/gland remnants); partial-thickness deep (into reticular dermis — decreased pain, risk of hypertrophic scarring, often requires grafting); full-thickness (all skin layers destroyed — leathery/white, painless, always requires grafting). Systemic effects of large burns (>20% TBSA): massive fluid shifts (Starling forces → oedema — Parkland formula: 4 mL × weight kg × %TBSA in first 24h), hypermetabolic state (↑cortisol, catecholamines, glucagon → muscle wasting), immunosuppression → Pseudomonas/Staphylococcus/Candida sepsis.

### Skin Cancer (BCC and SCC)

**Basal cell carcinoma (BCC)**: most common human cancer (~3 million/year USA); arises from basal layer keratinocytes; UV damage + PTCH1 loss → constitutive Hedgehog/Smoothened pathway activation → Gli transcription → tumour growth. Locally invasive; rarely metastasises. Vismodegib/sonidegib (Smo inhibitors) for advanced/metastatic.

**Squamous cell carcinoma (SCC)**: from differentiated keratinocytes; UV-induced TP53 mutations + TP63 mutations; risk factors: UV, immunosuppression, HPV (type 16/18 on mucosal SCC), chronic wounds. Metastatic SCC: cemiplimab/pembrolizumab (anti-PD-1) effective.

## See Also

- [dendritic-cell](../../04-cellular/dendritic-cell/README.md) — Langerhans cells as epidermal DCs
- [immune-system](../../07-system/immune-system/README.md) — skin-immune crosstalk, atopic march
- [nervous-system](../../07-system/nervous-system/README.md) — cutaneous sensory transduction
- [cardiovascular-system](../../07-system/cardiovascular-system/README.md) — cutaneous thermoregulatory vasomotion
- [collagen](../../03-molecular/collagen/README.md) — structural protein of dermis, wound healing
- [tnf-alpha](../../03-molecular/tnf-alpha/README.md) — key cytokine in skin inflammation (psoriasis, wound healing)

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022.
