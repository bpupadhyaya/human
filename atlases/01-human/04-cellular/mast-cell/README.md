---
schema: human-scale-entry/v1
id: mast-cell
name: Mast Cell
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Tissue-resident innate immune cells with electron-dense metachromatic granules. IgE-FcεRI crosslinking triggers rapid degranulation releasing histamine, tryptase, leukotrienes, and PGD2. Central to type I hypersensitivity, allergic asthma, and host defence against parasites."
aliases: ["mastocyte", "tissue mast cell", "connective tissue mast cell", "mucosal mast cell", "MC"]
sources:
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "Mast cells are tissue-resident innate sentinels at host-environment interfaces; IgE-FcεRI crosslinking triggers degranulation (histamine, tryptase, LTC4, PGD2) initiating type I hypersensitivity and first-line defence against parasites and venoms."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "Mast cell-derived IL-4, IL-13, and PGD2 drive Th2 polarisation and ILC2 activation; degranulation products recruit Th2 cells to mucosal sites; IL-4 also promotes B cell IgE class switching in early sensitisation."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Mast cells are anatomically adjacent to sensory nerves; tryptase activates PAR2 on C-fibres → itch/pain; neuropeptides (substance P, CGRP) activate MRGPRX2 → degranulation; mast cell-neuron cross-talk drives IBS, rosacea, fibromyalgia pain."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Cardiac mast cells (perivascular MCTC) degranulate in MI/reperfusion → histamine → coronary vasoconstriction; chymase generates local Ang II → vasoconstriction; LTC4/LTD4 → coronary spasm in Kounis syndrome."
---

# Mast Cell

## Overview

Mast cells are tissue-resident innate immune cells of haematopoietic origin, specialised for rapid release of a vast arsenal of vasoactive, pro-inflammatory, and immunomodulatory mediators in response to allergen-IgE-FcεRI crosslinking, complement anaphylatoxins, neuropeptides, and pathogen-associated signals. They were originally identified by Paul Ehrlich in 1878 ("Mastzellen" — well-fed cells) based on their characteristic large metachromatic cytoplasmic granules, which store pre-formed mediators including histamine, heparin, tryptase, chymase (tissue subtype), and TNF-α.[^alberts-mol-cell-biology]

Unlike basophils — their circulating haematopoietic cousins — mast cells complete their differentiation within tissues, not in the bone marrow or blood. They are the quintessential "first responders" at host-environment interfaces (skin dermis, respiratory mucosa, GI mucosa, genitourinary tract, peritoneum, meninges) where they serve dual roles: defending against parasitic helminths and arthropod venoms (protective), and mediating pathological type I (IgE-mediated) hypersensitivity including anaphylaxis, allergic asthma, allergic rhinitis, and urticaria.[^guyton-hall]

## Structure

**Morphology.** Mast cells are 10–20 µm in diameter, roughly spherical to oval in tissue sections. Their defining feature is an abundance of large (0.2–0.8 µm), electron-dense secretory granules that stain metachromatic purple with toluidine blue or Giemsa — owing to the anionic heparin proteoglycan binding the cationic dye and shifting its emission wavelength. On H&E, granules appear lightly eosinophilic; safranin and alcian blue distinguish connective tissue (safranin+) from mucosal (alcian blue only) subtypes.

**Nucleus.** Single, central, round-to-oval nucleus; chromatin is typically less condensed than in neutrophils, consistent with transcriptional activity. No nuclear segmentation (distinguishes mast cells from basophils, which have bilobed nuclei).

**Two tissue subtypes (human):**
- **MCT (mucosal mast cell):** Contains tryptase only (TPSAB1 α-tryptase and βI/II-tryptase); found in GI mucosa and alveolar wall; differentiation is T-cell dependent (IL-9, IL-3); responds to Th2 cytokines; granules smaller, fewer.
- **MCTC (connective tissue mast cell):** Contains both tryptase and chymase (CMA1), plus carboxypeptidase A3 (CPA3) and cathepsin G; found in skin dermis, peritoneum, myocardium, synovium; larger granules, more numerous; not T-cell dependent.[^alberts-mol-cell-biology]

**Key surface molecules.** FcεRI (high-affinity IgE receptor, αβγ₂ tetrameric complex — α subunit binds IgE Cε3/Cε4 domains; β and γ₂ ITAM signalling chains); c-Kit (CD117, SCF receptor — critical for development and survival); C3aR, C5aR (complement anaphylatoxin receptors); FcγRIII (CD16, IgG receptor); MRGPRX2 (basic peptide receptor — non-IgE degranulation); ST2 (IL-33 receptor); IL-4Rα, IL-9R, TSLPR; TLR1/2/4/6 (innate pattern recognition); PAR1/2 (protease-activated receptors).

**Granule contents (pre-formed mediators):**
- Histamine (major vasoactive amine, 3–8 pg/cell; stored ionically complexed with heparin proteoglycan; released within 30 s of activation; H₁R → itch, vasodilation, bronchoconstriction; H₂R → gastric acid, vasodilation; H₄R → eosinophil chemotaxis)
- Heparin (anticoagulant proteoglycan, also scaffolds/stores other granule mediators including tryptase)
- Tryptase (α and β isoforms; TPSAB1/TPSB2; the diagnostic serum marker of mast cell activation/anaphylaxis; activates PAR-2 on epithelium, fibroblasts, and neurons; activates MMP-3; cleaves fibronectin; plasma half-life ~2 h — must be drawn within 3 h of anaphylaxis)
- Chymase (MCTC type; degrades Ang I → Ang II via chymase-dependent pathway in tissues — particularly important in skin and heart; cleaves SCF, releases membrane-bound TGF-β)
- Carboxypeptidase A3 (CPA3 — metalloexopeptidase, degrades neurotensin and peptides)
- TNF-α (uniquely, mast cells store pre-formed TNF-α in granules, enabling rapid TNF-α release distinct from transcription-dependent macrophage TNF-α)
- Eosinophil/neutrophil chemotactic factors (ECF-A, NCF-A)

## Function

**De novo-synthesised mediators (minutes–hours post-activation):**

*Eicosanoids (arachidonic acid → COX/5-LOX):*
- Prostaglandin D₂ (PGD₂): mast cells are the richest source; DP1 receptor → bronchorelaxation (paradoxically), vasodilation; CRTH2/DP2 receptor on eosinophils, Th2 cells, ILC2 → chemoattractant → eosinophil and Th2 recruitment to allergic sites
- LTC₄ → LTD₄ → LTE₄ (cysteinyl leukotrienes, CysLTs): generated by 5-LOX + FLAP → LTA₄ + glutathione → LTC₄ via LTC₄ synthase; CysLT₁R/CysLT₂R on airway smooth muscle → bronchoconstriction (1000× more potent than histamine), mucus hypersecretion, vascular oedema; montelukast/zafirlukast antagonise CysLT₁R
- LTB₄: 5-LOX product without glutathione; BLT1R on neutrophils → potent neutrophil chemotaxis; amplifies early innate inflammatory infiltrate

*Platelet-activating factor (PAF):* phospholipid mediator → PAFR on platelets and neutrophils → bronchoconstriction, platelet aggregation, neutrophil priming

*Cytokines and growth factors (hours):* IL-4, IL-5, IL-13 (Th2 programme amplification; IL-13 → goblet cell hyperplasia, mucus, smooth muscle hyperresponsiveness; IL-5 → eosinophil survival/activation), IL-33 (amplification loop), TNF-α (both pre-formed and newly synthesised), IL-6 (acute phase), IL-10 (regulatory, anti-inflammatory), TGF-β (fibrosis in chronic allergy), VEGF (angiogenesis in tumour microenvironment and wound healing), SCF (autocrine survival loop), bFGF/FGF-2 (fibroblast proliferation/airway remodelling).[^guyton-hall]

**Activation pathways:**

1. **IgE-FcεRI crosslinking (canonical allergic pathway):** Allergen-specific IgE coats FcεRI on resting mast cells (sensitisation); subsequent allergen exposure crosslinks ≥2 FcεRI-bound IgE → Lyn kinase phosphorylates FcεRI β and γ ITAM tyrosines → Syk recruitment → LAT (linker for activation of T cells) scaffold → PLCγ1/2 → IP₃ (Ca²⁺ release from ER) + DAG (PKCβ activation) → degranulation; MAP kinases (ERK, JNK, p38) → eicosanoid synthesis and cytokine transcription.[^alberts-mol-cell-biology]

2. **Complement anaphylatoxins:** C3a (C3aR → Gαi → ↑Ca²⁺, weaker than FcεRI) and C5a (C5aR/CD88 → Gαi → degranulation + cytokine release) — important in non-IgE-mediated pseudo-allergic reactions (e.g., radiocontrast media reactions, some drug reactions).

3. **SCF/c-Kit:** PI3K, MAPK signalling → cell survival, proliferation, migration, sensitisation (lowers threshold for FcεRI crosslinking); gain-of-function D816V KIT mutation → constitutive activation → mastocytosis.

4. **IL-33/ST2:** ST2 + IL-1RAcP → MyD88 → IRAK4 → TRAF6 → NF-κB + p38 → cytokine release (IL-6, IL-13, TNF-α) without degranulation; major amplification signal in allergic inflammation and epithelial injury.

5. **MRGPRX2 (non-IgE degranulation):** Basic peptides — substance P, CGRP, VIP, mastoparan, compound 48/80, some antibiotics (fluoroquinolones, vancomycin), and opioids (morphine, codeine) → MRGPRX2 (Mas-related G protein-coupled receptor X2, Gαq) → Ca²⁺ → degranulation within seconds; pseudo-allergic (not IgE-mediated, no sensitisation required, not detected by skin tests/specific IgE).

6. **Physical stimuli:** Cold (TRPA1-mediated), heat (TRPV1), pressure/mechanical (Piezo channels) → Ca²⁺ → degranulation; basis of dermographism, cold urticaria, pressure urticaria.

## Lifecycle

Mast cells arise from the basophil-mast cell common progenitor (BMCP) in the bone marrow:

HSC → CMP → basophil-mast cell progenitor (BMCP, Kit+FcεRI−/low) → committed mast cell progenitor (MCp, Kit++FcεRI+Lin−) → exit bone marrow as circulating immature precursors (no granules) → enter tissues via CXCR2/CXCR4/CCR2 → complete differentiation under local tissue signals:
- SCF (KIT-L/KITLG, the dominant factor — produced by fibroblasts, endothelium, keratinocytes) → c-Kit signalling: Akt (survival), ERK (proliferation), STAT3 (Mcl-1, anti-apoptosis)
- IL-3 (initial priming, basophil/mast cell common factor), IL-4, IL-9, IL-33, TSLP (mucosal subtype)
- Tissue TGF-β and IL-10 → modulate phenotype toward regulatory/tolerogenic roles in certain contexts (peritoneal mast cells express IL-10 in helminth infection)[^alberts-mol-cell-biology]

**Lifespan:** Fully mature tissue mast cells are long-lived (weeks to months in rodents; estimated months to years in humans). They can undergo multiple rounds of degranulation and regranulation without cell death (partial degranulation). Apoptosis is triggered by cytokine withdrawal (SCF deprivation) or steroid treatment (glucocorticoids → ↑apoptosis, ↓FcεRI expression — mechanism of corticosteroid efficacy in allergic disease). After degranulation, regranulation takes 24–72 hours.[^guyton-hall]

## Connections

- **Part-of immune-system [^alberts-mol-cell-biology]:** Mast cells are tissue-resident innate sentinels at host-environment interfaces; IgE-FcεRI crosslinking triggers rapid degranulation (histamine, tryptase, LTC₄, PGD₂) initiating type I hypersensitivity and first-line defence against parasites and venoms.
- **Modulates T-helper-cell [^alberts-mol-cell-biology]:** Mast cell-derived IL-4, IL-13, and PGD₂ drive Th2 polarisation and ILC2 activation; degranulation products recruit Th2 cells to mucosal sites; IL-4 promotes B cell IgE class switching in early sensitisation.
- **Modulates nervous-system [^guyton-hall]:** Mast cells lie anatomically adjacent to sensory nerves; tryptase activates PAR-2 on C-fibres → itch/pain amplification; neuropeptides (substance P, CGRP) activate MRGPRX2 → degranulation; mast cell-neuron cross-talk drives IBS, rosacea, and fibromyalgia.
- **Modulates cardiovascular-system [^guyton-hall]:** Cardiac mast cells (perivascular MCTC) degranulate in MI/reperfusion → histamine → coronary vasoconstriction; chymase generates local Ang II → vasoconstriction; LTC₄/LTD₄ → coronary spasm in Kounis syndrome (allergic MI).

## Pathology

**Anaphylaxis.** Systemic IgE-mediated FcεRI crosslinking → massive simultaneous mast cell + basophil degranulation → histamine (↓BP, urticaria), LTD₄ (bronchoconstriction), PGD₂ (↓BP), tryptase (PAR-2 activation, vascular permeability), PAF (platelet aggregation, bronchoconstriction) → within minutes: hypotension, bronchospasm, laryngeal oedema, urticaria/angioedema, vomiting. Biphasic reaction in ~20% (late phase 4–12 h later from inflammatory cell recruitment). Serum tryptase >11.4 µg/L confirms mast cell activation. Treatment: IM epinephrine (α₁ → vasoconstriction, β₂ → bronchodilation, β₁ → ↑cardiac output; also ↑cAMP → inhibits mast cell degranulation) is the only life-saving first-line agent; H₁-antihistamines and corticosteroids are adjunctive.

**Allergic Asthma.** Airway mast cells (both MCT and MCTC) are sensitised by inhaled allergen-specific IgE; re-exposure → crosslinking → release of histamine, PGD₂, LTC₄/LTD₄ → immediate bronchoconstriction; IL-4, IL-13, IL-5 → late-phase eosinophilic inflammation, goblet cell hyperplasia, airway smooth muscle hypertrophy/hyperplasia → airway remodelling. Anti-IgE (omalizumab, binds free IgE Cε3 domain, blocks FcεRI binding → ↓mast cell sensitisation) is effective in moderate-severe allergic asthma; also anti-IL-5 (mepolizumab — eosinophil arm), anti-IL-13 (tralokinumab), dupilumab (anti-IL-4Rα, blocks IL-4 + IL-13).

**Urticaria and Angioedema.** IgE-dependent (allergen-triggered) or IgE-independent (autoimmune IgG anti-FcεRI, anti-IgE; physical stimuli; infections) mast cell activation → histamine + CysLTs → dermal (urticaria, wheals) or deep tissue (angioedema) oedema. Chronic spontaneous urticaria (CSU): sgumab (anti-IgE) effective; bilastine/cetirizine (H₁-antihistamines) first-line. Hereditary angioedema (C1-inhibitor deficiency) is NOT mast cell-mediated — it is a bradykinin-driven condition (kallikrein-kinin system); C1-INH concentrate, icatibant (B₂R antagonist), lanadelumab (anti-kallikrein prophylaxis) are appropriate.

**Mastocytosis.** KIT D816V somatic gain-of-function mutation → constitutive c-Kit signalling → autonomous mast cell proliferation. Cutaneous mastocytosis (urticaria pigmentosa/maculopapular CM): orange-brown macules that urticulate with stroking (Darier's sign); peaks in children, often remits. Systemic mastocytosis (SM): bone marrow infiltration (multifocal dense mast cell aggregates, CD117+CD25+tryptase+), often with D816V; serum baseline tryptase >20 ng/mL (major criterion). Indolent SM: good prognosis; aggressive SM (organopathy) → poor prognosis; SM with associated haematological neoplasm (SM-AHN, often AML, MDS). Treatment: antihistamines + cromolyn for symptom control; midostaurin (KIT inhibitor, FDA 2017, type I inhibitor — active against D816V) for advanced SM; avapritinib (BLU-285, type I KIT inhibitor, more potent D816V activity, FDA 2021); allogenic SCT in aggressive SM.

**Food Allergy.** Gastrointestinal mast cells (MCT type) sensitised by food allergen-specific IgE; re-exposure → rapid GI mast cell degranulation → histamine + LTD₄ + PGD₂ → nausea, vomiting, abdominal cramps, diarrhoea; systemic spread → anaphylaxis. Peanut, tree nuts, fish, shellfish, milk, egg — most common. Oral immunotherapy (OIT): gradually desensitises via mast cell/basophil threshold elevation; omalizumab as adjunct pre-treatment facilitates OIT by reducing baseline mast cell sensitisation.

## See Also

- `../../07-system/immune-system/README.md` — type I hypersensitivity, IgE-mediated allergy
- `../t-helper-cell/README.md` — Th2-mast cell crosstalk in allergic inflammation
- `../../07-system/nervous-system/README.md` — neurogenic inflammation, mast cell-nerve interaction
- `../../07-system/cardiovascular-system/README.md` — Kounis syndrome, cardiac mast cells
- `../dendritic-cell/README.md` — allergen presentation, IgE class switching coordination
