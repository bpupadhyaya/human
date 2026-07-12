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
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin is the principal organ of the integumentary system — a ~2 m² epidermis-over-dermis barrier renewed every ~28 days that, with hair, nails, and glands, handles physical and immune defense, thermoregulation, sensation, and vitamin D synthesis."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Skin is the body's sole site of vitamin D₃ synthesis: UVB photons (290-320 nm) convert 7-dehydrocholesterol in the epidermis to pre-vitamin D₃; melanin, ageing, high latitude, and sunscreen all cut this output, linking skin pigmentation to systemic calcium and bone health."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Collagen is the structural backbone of the dermis: type I bundles along Langer's lines give skin its tensile strength, and the ordered swap of type III for type I collagen during wound remodeling sets scar quality — with overactive TGF-β-driven deposition producing keloids."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The integumentary and musculoskeletal systems are the body's structural envelope and frame: skin's collagen-rich dermis is continuous with fascia over muscle and bone, both depend on vitamin D and collagen, and disorders like scleroderma, EDS and dermatomyositis injure both."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Psoriasis is the archetypal disease of the integumentary system: Th17/IL-17-driven keratinocyte hyperproliferation produces scaly plaques, showing the skin's role as an immune barrier; its systemic inflammation links skin to joints (psoriatic arthritis) and metabolic disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells in the dermis are key effectors of the skin's immune barrier: IgE- or MRGPRX2-triggered degranulation releases histamine → wheal-and-flare urticaria, angioedema and itch; they also orchestrate wound healing and the response to venoms and irritants at the body surface."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The skin is a target organ of reproductive hormones: androgens drive sebaceous glands, acne, and male-pattern hair, estrogen maintains dermal collagen, and pregnancy alters pigmentation—so the integument reflects the reproductive system's hormonal state."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "The integumentary system is both an endocrine target and an endocrine organ: thyroid, cortisol, and sex hormones reshape skin and hair, while the skin makes vitamin D from sunlight—so endocrine disease often first shows in the skin (myxedema, striae)."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Wound healing is the integumentary system's core repair program: after injury the skin runs hemostasis, inflammation, proliferation, and remodeling to rebuild epidermis and dermis—imperfectly, leaving scar that lacks follicles and full strength."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Melanoma is the deadliest cancer of the integumentary system: arising from epidermal melanocytes, it—unlike keratinocyte cancers—readily metastasizes, so UV-driven melanoma makes the integument's own pigment system a lethal cancer source."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "Basal cell carcinoma is the commonest cancer of the integumentary system: chronic UV damage to basal keratinocytes activates Hedgehog/PTCH1 signaling, producing slow-growing tumors that almost never metastasize—the indolent counterpart to melanoma in the skin."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibroblasts build the integumentary system's dermal scaffold: they synthesize the collagen and elastin that give skin strength and elasticity, and their decline underlies wrinkling and aging—so dermal fibroblasts determine how skin holds up over a lifetime."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Atopic dermatitis is the integumentary system's barrier disease: filaggrin-deficient skin loses water and lets allergens in, triggering itch-scratch inflammation—showing how the epidermal barrier, immune cells and nerves of the skin act as one integrated organ system."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The integumentary and lymphatic systems are intertwined in the skin: dermal lymphatics drain interstitial fluid and ferry antigen-laden dendritic cells to nodes, so when they fail, lymphedema swells the limb and thickens the overlying skin."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Systemic sclerosis turns the integument rigid: autoimmune fibroblast activation deposits excess collagen in the dermis, hardening and tethering the skin—the visible hallmark of a disease that shows how the skin's connective tissue can drive systemic illness."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "The skin is the body's main interface with photons: UV light damages DNA, driving skin cancers and photoaging, yet also powers vitamin D synthesis—so sunlight is both essential to and the chief carcinogen of the integument."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "The skin's deepest layer is built of adipocytes: the subcutaneous hypodermis stores fat for insulation, cushioning, and energy, anchors skin to muscle, and secretes hormones like leptin—so body-fat changes visibly reshape the skin's contour and thickness."
  - target: 01-human/07-system/pemphigus-vulgaris
    relation: connects-to
    note: "Pemphigus vulgaris shows how autoimmunity can unglue the skin: antibodies against desmoglein dissolve the desmosomes binding keratinocytes, so the epidermis blisters and sloughs—revealing how much the integument depends on cell-to-cell adhesion to stay intact."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "The skin is the front line against Staphylococcus aureus: it colonizes skin and, when the barrier breaks, causes impetigo, cellulitis and abscesses—so the integument's physical and antimicrobial defenses are what normally keep this common pathogen out."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Skin is an estrogen-responsive organ: estrogen maintains dermal collagen, thickness and hydration, so its fall at menopause thins and dries skin and slows wound healing—why hormonal status shapes skin aging."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The skin is an immune organ patrolled by T-helper cells: resident and recruited helper T cells survey the epidermis and dermis for pathogens, and their misdirection drives inflammatory skin diseases like psoriasis and eczema."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "The skin is a thermostat that sheds sodium: sweat glands pour out water and sodium to cool the body by evaporation, so the integument regulates temperature and electrolytes—heavy sweating can drain enough salt to matter."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Skin is built and protected by cholesterol: ceramides and cholesterol cement the outer barrier against water loss, and skin's 7-dehydrocholesterol is the very molecule UV light converts into vitamin D—so the organ both shields and synthesizes."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "The skin itches and welts through histamine: mast cells in the dermis release histamine that dilates vessels and fires itch nerves, producing the hives, flares, and wheals of allergic and urticarial skin reactions."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Skin's outer layer matures along a calcium gradient: rising calcium up through the epidermis drives keratinocytes to differentiate and build the barrier, so disrupting that gradient unravels how the skin renews and seals itself."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "The skin is patrolled by cytotoxic T cells: these killers reside in the epidermis as immune memory, destroying virus-infected and malignant cells but, when misdirected, driving the blistering rashes of severe drug reactions."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Skin tunes body temperature with nitric oxide: it relaxes dermal blood vessels to flush heat to the surface, the vasodilation behind blushing and warmth—and faulty control underlies flushing disorders and cold, poorly perfused skin."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "The skin is the body's largest sensory organ: packed with peripheral nerve endings for touch, temperature, and pain, it is how we feel the world—and where neuropathy first robs sensation."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc keeps skin intact: deficiency causes the rash of acrodermatitis enteropathica and stalls wound healing, because the mineral fuels the rapid epidermal turnover and repair the skin depends on."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "The skin's dense dermal vasculature, lined by endothelial cells, both feeds it and serves thermoregulation, dilating to dump body heat or constricting to conserve it as the surface flushes or pales."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows how skin holds together and waterproofs: keratinocytes are riveted by desmosomes and anchored to the basement membrane by hemidesmosomes, their cytoplasm filled with keratin bundles and melanosomes handed over from melanocytes."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper colors and strengthens the skin: it is the catalytic metal in tyrosinase, the enzyme that makes melanin pigment, and in lysyl oxidase, which cross-links the collagen and elastin that give the dermis its resilience."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Sulfur is what makes hair and nails tough: keratin is rich in the amino acid cysteine, whose sulfur atoms form disulfide bridges that lock the protein into hard, springy fibers — the bonds a perm breaks and reforms."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid hormone tunes the skin: too little leaves it dry, cool, and puffy with myxedema and brittle hair, while too much makes it warm, moist, and flushed — so the skin and its appendages often read out thyroid status at a glance."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "The skin is a window onto the blood: its color reflects hemoglobin — pallor in anemia, bluish cyanosis when deoxygenated hemoglobin rises, and the yellow of jaundice when its breakdown pigment bilirubin builds up."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Skin and kidney share the vitamin D relay: the skin makes vitamin D₃ from sunlight, the kidney performs its final activation, and failing kidneys repay the skin with the relentless itch of uremic pruritus."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol thins and weakens the skin: chronic steroid excess, from Cushing's or long treatment, atrophies the dermis into purple striae, easy bruising, and poor wound healing, making the skin a visible readout of glucocorticoid load."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron status writes itself on skin, hair, and nails: deficiency brings pallor, hair loss, and spoon-shaped koilonychia, while iron overload in hemochromatosis bronzes the skin — the integument reporting the body's iron stores."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Dermal macrophages are the skin's clean-up and defense corps: they engulf invaders and debris breaching the barrier, orchestrate wound repair, and even carry the tattoo pigment that stays locked in the dermis for life."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The skin is the body's largest sensory sheet: specialized nerve endings and Merkel-cell complexes wire it for touch, pressure, temperature, and pain, so neurons turn the integument into a vast field of receptors reporting the outside world."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "The skin is a frontline organ in lupus: photosensitive malar and discoid rashes mark cutaneous SLE, where UV light and autoantibodies drive immune attack at the dermal-epidermal junction, often the disease's first visible sign."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "The skin barrier holds back fungal overgrowth: when warmth, moisture, or immune suppression breach it, Candida colonizes skin folds, nails, and mucocutaneous surfaces, turning a commensal into intertrigo, paronychia, and thrush."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "A virus hides in the skin's nerves and returns: after chickenpox, varicella-zoster lies dormant in sensory ganglia and reawakens as shingles, a painful dermatomal rash that maps the very nerve territory supplying that patch of skin."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "The skin cools itself on an odd nerve signal: eccrine sweat glands are driven by sympathetic fibers that, unusually, release acetylcholine rather than noradrenaline, the cholinergic switch that turns on sweating for thermoregulation."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "When the barrier is breached, neutrophils rush in: they are the front line against skin-invading bacteria, forming the pus of abscesses and cellulitis and clearing the infection that a broken epidermis lets through."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "One bacterium owns the skin's classic infections: Streptococcus pyogenes causes impetigo, erysipelas and cellulitis, and when it invades the fascia it drives the flesh-eating necrotizing fasciitis that is a surgical emergency."
  - target: 02-pathogen/01-viruses/measles-virus
    relation: connects-to
    note: "A systemic virus announces itself in the skin: measles produces a spreading maculopapular rash as infected immune cells seed the dermis, the visible sign of an infection whose real danger lies in its deep immune suppression."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Breach the barrier widely and infection goes systemic: extensive burns, pressure ulcers or severe cellulitis let skin flora into the bloodstream, making the skin's failure a common gateway to life-threatening sepsis."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Skin disease can spread to the joints: in a fraction of people with psoriasis of the skin, the same immune process attacks the joints as psoriatic arthritis, a skin-to-joint axis driven by shared IL-17/IL-23 inflammation."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Its rash is a window onto systemic disease: the heliotrope eyelids and Gottron's papules of dermatomyositis are skin signs of an autoimmune myopathy, the integument flagging a deeper muscle and sometimes malignant process."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Broken skin lets the mold in directly: in burns, surgical wounds and immunocompromised patients, Aspergillus can establish a primary cutaneous infection at the breach, bypassing its usual respiratory route."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Visible skin disease wounds the psyche: disfiguring or itchy conditions like psoriasis, eczema and acne carry high rates of depression, and stress in turn flares the skin — the basis of psychodermatology."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "The skin announces metabolic disease: acanthosis nigricans, diabetic dermopathy, recurrent skin infections and impaired wound healing make the integument an early and telling window onto type 2 diabetes."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Pallor and brittle nails betray low iron: the skin, nails and hair show iron deficiency through pallor, spoon-shaped koilonychia and hair loss, making the integument a visible readout of the body's iron stores."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The skin mirrors the gut and liver: a gut-skin axis links bowel disease to conditions like dermatitis herpetiformis and pyoderma gangrenosum, while liver failure shows as jaundice and malabsorption as hair and nail change."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Failing kidneys are written on the skin: chronic kidney disease causes intractable uraemic pruritus, a sallow complexion and calciphylaxis, and gadolinium in renal failure can trigger nephrogenic systemic fibrosis."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Herpesviruses erupt on the skin: HSV causes cold sores and genital lesions and can spread catastrophically across eczematous skin as eczema herpeticum, while VZV produces chickenpox and shingles."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The skin announces lung disease: finger clubbing, central cyanosis and tar staining flag chronic respiratory illness, and granulomatous diseases like sarcoidosis strike skin and lung together."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "A rash that signals an emergency: meningococcal sepsis produces a non-blanching petechial and purpuric rash that can progress to purpura fulminans with skin necrosis, demanding immediate antibiotics."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Tuberculosis can settle in the skin: cutaneous TB such as lupus vulgaris and scrofuloderma, and the reactive panniculitis of erythema nodosum, are dermatological signs of mycobacterial infection."
  - target: 02-pathogen/04-parasites/leishmania-donovani
    relation: connects-to
    note: "A sandfly parasite scars the skin: cutaneous and post-kala-azar dermal leishmaniasis produce chronic disfiguring skin lesions, a major cause of skin disease in endemic regions."
  - target: 03-medicine/01-modern/12-anti-inflammatory/dexamethasone
    relation: connects-to
    note: "Steroids heal and harm the skin: corticosteroids treat inflammatory skin disease, but long-term use thins the skin and causes striae, easy bruising, acne and impaired wound healing."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Zinc keeps the skin intact: zinc is essential for skin integrity and repair, so deficiency causes acrodermatitis enteropathica with perioral and acral dermatitis."
  - target: 02-pathogen/01-viruses/coxsackievirus-b
    relation: connects-to
    note: "An enterovirus erupts on the skin: Coxsackievirus causes hand-foot-and-mouth disease with its vesicular rash, and on atopic skin can spread widely as eczema coxsackium."
  - target: 03-medicine/01-modern/11-biologics/adalimumab
    relation: connects-to
    note: "Biologics clear severe skin disease: anti-TNF antibodies like adalimumab, with IL-17 and IL-23 inhibitors, treat severe psoriasis and hidradenitis suppurativa of the skin."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Dietary fats support the barrier: omega-3 fatty acids contribute to the skin's lipid barrier and have anti-inflammatory effects studied in eczema and psoriasis."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "The skin shows immunotherapy's signature: checkpoint inhibitors cause the commonest immune-related adverse events in the skin — maculopapular rash, pruritus, lichenoid eruptions and vitiligo — and also treat the melanoma and skin cancers arising there."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "It writes its toxicity on the skin: cytotoxic chemotherapy causes alopecia, painful hand-foot syndrome, mucositis, nail changes and photosensitivity, the visible price of drugs that target all rapidly dividing cells including the skin."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "The skin scars and hardens: dermal fibrosis underlies hypertrophic scars and keloids after injury, the tight bound-down skin of scleroderma, and radiation dermatitis — excess collagen replacing the normal supple dermis."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "When the skin makes too many cancers: Gorlin (nevoid basal cell carcinoma) syndrome causes hundreds of basal cell carcinomas across the skin from germline PTCH1/Hedgehog activation, the heritable extreme of the skin's commonest cancer."
  - target: 01-human/07-system/rothmund-thomson
    relation: connects-to
    note: "A congenital poikiloderma: Rothmund-Thomson syndrome marbles the skin with the reticulate pigmentation, telangiectasia and atrophy of poikiloderma, a genodermatosis from RECQL4 loss with photosensitivity and cancer risk."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "Premature ageing of the skin: Werner syndrome gives scleroderma-like tight, atrophic skin with intractable leg ulcers and early greying, a progeroid genodermatosis from WRN-helicase loss."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "A barometer of immune status: HIV/AIDS produces a parade of skin diseases—Kaposi sarcoma, severe seborrhoea, eosinophilic folliculitis—the integument often the first signal of the underlying immunodeficiency."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Where vasculitis shows itself: small-vessel vasculitis like ANCA-associated disease announces itself in the skin as palpable purpura, making the integument a window onto systemic vascular inflammation."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Skin as casualty of systemic disease: chronic, painful leg ulcers over the malleoli are a hard-to-heal complication of sickle cell disease, reflecting the skin's vulnerability to microvascular ischaemia."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "The skin as a window on infection: COVID-19 produces a range of cutaneous signs—chilblain-like 'COVID toes', urticarial, vesicular and maculopapular rashes—that reflect the systemic vascular and immune response."
  - target: 01-human/07-system/ptcl
    relation: connects-to
    note: "Lymphoma born in the skin: primary cutaneous T-cell lymphomas like mycosis fungoides and Sézary syndrome arise in the integument itself, making the skin a primary site of lymphoid malignancy."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "The first organ of GVHD: the skin is the earliest and commonest target of graft-versus-host disease, its rash and later sclerodermatous change central to diagnosing and grading the alloimmune attack."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Neurogenic itch and inflammation: substance P released by cutaneous sensory nerves drives neurogenic inflammation and the itch sensation central to many skin diseases."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "The itch cytokine: IL-31 is the principal pruritogenic cytokine of the skin, the target of nemolizumab in atopic dermatitis and prurigo nodularis."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "Neuroimmune itch disease: prurigo nodularis is a chronic, intensely itchy skin disorder that exemplifies the neuroimmune itch circuit linking cutaneous nerves and immune cells."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Epidermal renewal: EGFR signalling drives keratinocyte proliferation and re-epithelialisation, which is why anti-EGFR cancer drugs cause the characteristic acneiform rash and skin toxicity."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Dermal vasculature: VEGF-driven angiogenesis supplies the skin's microcirculation and granulation tissue in wound healing, and its overactivity feeds the dilated vessels of psoriatic and inflamed skin."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Barrier alarmin: damaged keratinocytes release TSLP, the epithelial alarm signal that initiates the type 2 immune response and itch underlying atopic dermatitis and the atopic march."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Skin appendages: androgens acting through the androgen receptor drive sebaceous-gland activity and hair-follicle patterning, the basis of acne, androgenetic alopecia and hirsutism among the most common dermatologic complaints."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Keratinocyte growth: IGF-1 promotes keratinocyte proliferation and hair-follicle growth, linking the endocrine and nutritional state to epidermal turnover and contributing to the skin manifestations of acromegaly and acne."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Cutaneous eicosanoids: prostaglandins mediate the erythema, oedema and pain of sunburn and skin inflammation, and prostaglandin analogues both drive eyelash growth and are implicated in the hair-cycle changes of alopecia."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Appendage regeneration: Wnt/β-catenin signalling drives the cyclical regeneration of hair follicles and the self-renewal of epidermal stem cells, the developmental pathway that patterns skin appendages and whose dysregulation contributes to alopecia and skin tumours."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Barrier differentiation: a calcium gradient rising from the basal to the outer epidermis drives keratinocytes through their differentiation programme into the cornified barrier, the ionic signal that builds the skin's waterproof outer layer."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Topical anti-inflammatory: corticosteroids acting through the glucocorticoid receptor are the mainstay anti-inflammatory therapy across dermatology, suppressing the cutaneous immune response in eczema, psoriasis and dermatitis."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Epidermal differentiation: NOTCH signalling drives keratinocyte differentiation as cells move outward through the epidermal layers and patterns the hair-follicle and sebaceous-gland lineages of the skin."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Dermal homeostasis: TGF-β governs dermal fibroblast activity, wound repair and hair-follicle cycling, and its dysregulation underlies the cutaneous fibrosis of scleroderma and keloids."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Cutaneous immunity: the skin is a principal site of IL-17A-driven immunity, central both to its antifungal defence and to the inflammatory skin diseases (psoriasis already mapped) of the integument."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Atopic Th2 axis: IL-13, with the TSLP and IL-31 already mapped, drives the barrier dysfunction and itch of atopic dermatitis, the archetypal type-2 inflammatory disease of the skin."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Psoriatic axis: the IL-23/IL-17 axis (IL-17A already mapped) drives the keratinocyte hyperproliferation and inflammation of psoriasis, a defining immune disease of the integument."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Neurocutaneous innervation: the densely innervated skin relies on BDNF and neurotrophins to maintain its sensory nerves, and their upregulation sensitises the cutaneous itch-and-pain network in inflammatory skin disease."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "NRF2 governs the keratinocyte antioxidant response to UV and environmental oxidative stress, central to epidermal barrier maintenance and photoprotection."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α coordinates the cutaneous response to hypoxia during wound healing and supports dermal angiogenesis (VEGF mapped)."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is a key cutaneous inflammatory cytokine driving keratinocyte responses and dermal inflammation across many skin diseases."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 signalling governs keratinocyte proliferation, the hair-follicle cycle and the IL-6/IL-23-Th17 immunity that is central to inflammatory skin disease."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates cutaneous immunity, wound healing and dermal fibrosis across the disorders of the integumentary system."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING senses the cytosolic DNA generated by UV damage and infection in the skin, linking the integumentary barrier to innate antiviral and inflammatory responses."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling (TGF-β already mapped) governs keratinocyte differentiation, wound repair, and dermal fibrosis across the integumentary system."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate keratinocyte oxidative-stress defense, hair-follicle cycling, and epidermal homeostasis in the skin."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of EGFR (EGFR already mapped) drives the keratinocyte proliferation and epidermal renewal of the integumentary system."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signaling governs the proliferation and survival of keratinocytes and the epidermal barrier renewal of the integumentary system."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β, within the Wnt signaling that patterns hair follicles (Wnt already mapped), regulates the skin-appendage development and epidermal homeostasis of the integumentary system."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the antimicrobial and immune-surveillance functions of the skin in the integumentary system."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the keratinocyte and hair-follicle proliferation and survival of the integumentary system."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling integrates nutrient and growth-factor cues to drive the epidermal proliferation and barrier renewal of the integumentary system."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB signaling governs the keratinocyte inflammatory and barrier-defense responses of the integumentary system."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the keratinocyte and sebocyte energy metabolism of the integumentary system."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the keratinocyte differentiation, barrier formation, and melanocyte homeostasis of the integumentary system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the keratinocyte adhesion, migration, and growth-factor responses of the integumentary system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven chemokine signaling participates in the cutaneous immune-cell trafficking of the integumentary system."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the dermal-epidermal and immune-cell interactions of the integumentary system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the keratinocyte differentiation and skin-immune gene programs of the integumentary system."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic skin signs: insulin and IGF acting on keratinocytes drive acanthosis nigricans, the velvety hyperpigmentation that signals insulin resistance, making the skin a visible window onto systemic metabolic disease."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Pigmentation and vascular tone: endothelin-1 signalling through EDNRB supports melanocyte survival and pigment production and regulates dermal vascular tone, contributing to both skin colour and cutaneous blood flow."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Cutaneous protection: the skin both produces and responds to melatonin, which acts as a local antioxidant against ultraviolet damage and participates in the circadian regulation of the hair follicle cycle."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant selenoproteins: selenium-dependent glutathione peroxidases protect skin and hair from oxidative and ultraviolet damage (NFE2L2 already mapped), and selenium deficiency causes skin and hair changes, part of the integument's antioxidant defence."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Cutaneous serotonin: the skin synthesises and responds to serotonin, which modulates itch, keratinocyte proliferation and dermal blood flow, one of several neurotransmitter systems (substance P already mapped) active in the integument."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine signalling: subcutaneous adipose tissue is part of the integument, and its adipokine leptin influences hair-follicle cycling, wound healing and dermal homeostasis, linking the skin's fat layer to its regenerative biology."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Photo-oxidative stress: ultraviolet exposure (photon already mapped) generates reactive oxygen species in the skin, to which xanthine oxidase contributes, driving the photoaging and DNA damage that the NRF2 antioxidant response (already mapped) counters."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 skin inflammation: IL-4, with IL-13 and IL-31 (already mapped), drives the itch and barrier disruption of atopic dermatitis, part of the type-2 immune axis prominent in inflammatory skin disease of the integument."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Eccrine sweat electrolytes: aldosterone drives sodium reabsorption in the eccrine sweat ducts (acetylcholine already mapped for sweat secretion), conserving salt during heat acclimatisation, a mineralocorticoid function of the integument's sweat glands."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Skin-resident T cells: the CD4 T-helper cells resident in the skin, driving the Th17 and type-2 responses (IL-17, IL-23 and IL-13 already mapped), are central to the inflammatory diseases of the integument such as psoriasis and atopic dermatitis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and skin integrity: zinc is essential for keratinocyte proliferation, wound healing and the many cutaneous enzymes, and its deficiency causes the acrodermatitis and impaired barrier of the integument."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Dermal macrophages: the macrophages of the dermis provide immune surveillance, clear debris and orchestrate the repair (collagen already mapped) of the skin, part of the integument's role as an immune organ."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory skin disease: TNF drives psoriasis and the inflammatory dermatoses (IL-17 and IL-23 already mapped), the target of the anti-TNF biologics that transformed the treatment of severe skin disease."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Type-2 dermal remodelling: periostin, a matricellular protein induced by the type-2 cytokines (IL-13 already mapped), drives the dermal remodelling and chronic itch of atopic dermatitis, a biomarker of the barrier-disrupted skin."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Keratinocyte alarmin: IL-1β released by the keratinocytes is an alarm cytokine of the skin, driving the inflammation of hidradenitis suppurativa, neutrophilic dermatoses and the response to barrier injury."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Dermal mast cells: the dermal mast cells (histamine already mapped) mediate the itch, the urticaria and the immediate hypersensitivity of the skin of the integumentary system."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Skin-integrity zinc: the zinc essential for the skin integrity and wound healing; the zinc deficiency causes the acrodermatitis enteropathica of the integumentary system."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Melanin and collagen copper: the copper-dependent tyrosinase makes the melanin (endothelin-1 already mapped), and the lysyl oxidase cross-links the dermal collagen (already mapped) and elastin of the skin."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Cutaneous type-2 IgE: the IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped) and the alarmins (TSLP already mapped), drives the atopic and urticarial dermatoses of the integumentary system."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil skin arm: IL-5 recruits the eosinophils of the type-2 (IL-4 and IL-13 already mapped) inflammation of the atopic and eosinophilic dermatoses of the skin."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Plasmacytoid-DC interferon: the type-I interferon of the plasmacytoid dendritic cells (already mapped) drives the interface dermatoses — the cutaneous lupus and the psoriasis (IL-17 and IL-23 already mapped) — of the integumentary system."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 skin immunity: the IFN-γ of the skin T cells is the type-II interferon arm of the Th1 immunity of the interface dermatoses and the antimicrobial defence of the integumentary system."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the cutaneous immune response of the integumentary system."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Skin innate surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance against the virally-infected keratinocytes and the skin cancers of the integumentary system."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Cutaneous complement: the complement C3, deposited and locally produced in the skin, is part of the innate antimicrobial defence and the immune-complex dimension of the cutaneous immunity of the integumentary system."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling recruits the neutrophils and myeloid cells to the site of the cutaneous inflammation of the integumentary system."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Dermal humoral arm: the plasma cells of the dermis secrete the antibodies of the humoral arm of the cutaneous immunity of the integumentary system."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) complete the complement cascade of the innate cutaneous defence of the integumentary system."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) on the skin surface, restraining the complement attack on the host tissue of the integumentary system."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Dermal B cells: the B cells, upstream of the plasma cells (already mapped), contribute to the humoral and organised immune response of the cutaneous immunity of the integumentary system."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Cutaneous kinin signalling: bradykinin, released from skin mast cells (already mapped) and by kallikrein-driven contact activation in wounded epidermis, amplifies the vasodilatation, pruritus, and neurogenic inflammation of the integumentary system."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor restrains classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) activation at the epidermal barrier, controlling the inflammatory response of the integumentary system."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Epidermal EPO axis: erythropoietin, produced locally by dermal fibroblasts (already mapped) and keratinocytes under hypoxic stress (HIF-1α already mapped), supports wound healing (already mapped), epithelial repair, and angiogenesis of the integumentary system."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Cutaneous immune modulator: prolactin, secreted by keratinocytes (already mapped) and dermal fibroblasts (already mapped) in addition to the pituitary, modulates the mast-cell (already mapped) and T-cell (already mapped) responses of the skin immune barrier."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Neuroimmune skin axis: oxytocin, via OXT receptors on keratinocytes (already mapped), melanocytes (already mapped) and dermal fibroblasts (already mapped), promotes wound healing (already mapped) and collagen remodelling of the integumentary system."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sebaceous-follicular androgen: testosterone, converted to DHT by 5α-reductase in sebaceous glands (already mapped) and hair follicles (already mapped), drives sebum production and the androgenic regulation of the pilosebaceous unit of the integumentary system."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "IS vasopressin: vasopressin (ADH) constricts cutaneous microvessels via V1 receptor on skin (already mapped) endothelium; vasopressin also modulates mast-cell (already mapped) degranulation and the wound-healing (already mapped) fibroblast (already mapped) response."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "IS transferrin: transferrin delivers iron for collagen (already mapped) synthesis by fibroblasts (already mapped) in skin (already mapped) wound-healing (already mapped); iron deficiency impairs skin (already mapped) barrier repair and IL-6 (already mapped) regeneration."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "IS magnesium: magnesium supports collagen (already mapped) crosslinking and fibroblast (already mapped) function in skin (already mapped); magnesium deficiency amplifies mast-cell (already mapped) degranulation and IL-6 (already mapped) cutaneous inflammation."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "IS iodine: thyroid-hormone signalling drives keratinocyte differentiation and skin (already mapped) barrier integrity; iodine deficiency impairs wound-healing (already mapped) via NF-κB (already mapped) and IL-6 (already mapped) mediated fibroblast (already mapped) dysfunction."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "IS potassium: potassium channels regulate keratinocyte proliferation and skin (already mapped) barrier; potassium imbalance disrupts NF-κB (already mapped) and IL-6 (already mapped) mediated mast-cell (already mapped) responses and impairs collagen (already mapped) deposition."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "IS phosphorus: phosphorus supports ATP-driven synthesis of collagen (already mapped) by fibroblasts (already mapped) and keratinocyte integrity; hypophosphataemia impairs skin (already mapped) wound-healing (already mapped) and amplifies NF-κB (already mapped) inflammation."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "IS chloride: chloride, via ion channels in macrophages (already mapped) and mast cells (already mapped), maintains epidermal homeostasis; chloride dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of the integumentary system."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "IS nitrogen: nitrogen, as backbone of collagen (already mapped) in fibroblasts (already mapped) and skin (already mapped), supports structural integrity; nitrogen deficiency impairs wound-healing (already mapped) and amplifies the IL-6 (already mapped) inflammatory cascade."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "IS carbon: carbon, forming the backbone of ceramide lipids and melanin in skin (already mapped) and fibroblasts (already mapped), maintains epidermal barrier; carbon-skeleton insufficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) skin-barrier cascade."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "IS oxygen: oxygen, via ROS in fibroblasts (already mapped) and macrophages (already mapped), drives epidermal oxidative stress; oxygen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of the integumentary system."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "IS hydrogen: hydrogen, as water framework in skin (already mapped) and fibroblasts (already mapped), maintains epidermal hydration; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and wound-healing (already mapped) cascade."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Integumentary PD-1: PD-1 checkpoint on skin-resident T-cells (already mapped) suppresses anti-tumour immunity; PD-1 dysregulation amplifies IL-6 (already mapped) and TNF-α (already mapped) and VEGF (already mapped) signalling in integumentary immune surveillance."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Integumentary GLP-1: GLP-1 from skin adipocytes modulates keratinocyte (already mapped) proliferation and wound healing; GLP-1 dysregulation amplifies TNF-α (already mapped) and IL-6 (already mapped) inflammatory cascade of integumentary barrier."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Integumentary angiotensin-II: angiotensin-II mediates dermal vasoconstriction (already mapped) and fibroblast (already mapped) activation; angiotensin-II amplifies TGF-β (already mapped) and IL-6 (already mapped) fibrotic cascade of integumentary system."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Integumentary rankl: RANKL from keratinocytes (already mapped) and macrophages (already mapped) amplifies skin immune activation; rankl dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Integumentary il-2: IL-2 from skin-resident T-cells (already mapped) and macrophages (already mapped) amplifies adaptive immune responses; il-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Integumentary notch: Notch in keratinocytes (already mapped) and fibroblasts (already mapped) regulates epidermal differentiation; notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of integumentary system."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Integumentary fibronectin: fibronectin in fibroblasts (already mapped) and keratinocytes (already mapped) anchors dermal ECM; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of integumentary system."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Integumentary activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) drives fibrotic remodelling; activin-a dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of integumentary system."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Integumentary cgrp: CGRP from sensory neurons (already mapped) and mast cells (already mapped) drives neurogenic skin inflammation; cgrp dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Integumentary calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates skin calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "Integumentary fgf23: FGF23 from macrophages (already mapped) and fibroblasts (already mapped) regulates skin phosphate and keratinocyte growth; fgf23 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Integumentary insulin-receptor: insulin-receptor on fibroblasts (already mapped) and macrophages (already mapped) modulates homeostasis; receptor dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system."
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
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin is the principal organ of the integumentary system — a ~2 m² epidermis-over-dermis barrier renewed every ~28 days that, with hair, nails, and glands, handles physical and immune defense, thermoregulation, sensation, and vitamin D synthesis.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — One bacterium owns the skin's classic infections: Streptococcus pyogenes causes impetigo, erysipelas and cellulitis, and when it invades the fascia it drives the flesh-eating necrotizing fasciitis that is a surgical emergency.
- `connects-to` → **[Measles Virus](../../../02-pathogen/01-viruses/measles-virus/README.md)** — A systemic virus announces itself in the skin: measles produces a spreading maculopapular rash as infected immune cells seed the dermis, the visible sign of an infection whose real danger lies in its deep immune suppression.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Breach the barrier widely and infection goes systemic: extensive burns, pressure ulcers or severe cellulitis let skin flora into the bloodstream, making the skin's failure a common gateway to life-threatening sepsis.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Skin is the body's sole site of vitamin D₃ synthesis: UVB photons (290-320 nm) convert 7-dehydrocholesterol in the epidermis to pre-vitamin D₃; melanin, ageing, high latitude, and sunscreen all cut this output, linking skin pigmentation to systemic calcium and bone health.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Collagen is the structural backbone of the dermis: type I bundles along Langer's lines give skin its tensile strength, and the ordered swap of type III for type I collagen during wound remodeling sets scar quality — with overactive TGF-β-driven deposition producing keloids.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The integumentary and musculoskeletal systems are the body's structural envelope and frame: skin's collagen-rich dermis is continuous with fascia over muscle and bone, both depend on vitamin D and collagen, and disorders like scleroderma, EDS and dermatomyositis injure both.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Psoriasis is the archetypal disease of the integumentary system: Th17/IL-17-driven keratinocyte hyperproliferation produces scaly plaques, showing the skin's role as an immune barrier; its systemic inflammation links skin to joints (psoriatic arthritis) and metabolic disease.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells in the dermis are key effectors of the skin's immune barrier: IgE- or MRGPRX2-triggered degranulation releases histamine → wheal-and-flare urticaria, angioedema and itch; they also orchestrate wound healing and the response to venoms and irritants at the body surface.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The skin is a target organ of reproductive hormones: androgens drive sebaceous glands, acne, and male-pattern hair, estrogen maintains dermal collagen, and pregnancy alters pigmentation—so the integument reflects the reproductive system's hormonal state.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — The integumentary system is both an endocrine target and an endocrine organ: thyroid, cortisol, and sex hormones reshape skin and hair, while the skin makes vitamin D from sunlight—so endocrine disease often first shows in the skin (myxedema, striae).
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Wound healing is the integumentary system's core repair program: after injury the skin runs hemostasis, inflammation, proliferation, and remodeling to rebuild epidermis and dermis—imperfectly, leaving scar that lacks follicles and full strength.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Melanoma is the deadliest cancer of the integumentary system: arising from epidermal melanocytes, it—unlike keratinocyte cancers—readily metastasizes, so UV-driven melanoma makes the integument's own pigment system a lethal cancer source.
- `connects-to` → **[Basal Cell Carcinoma](../basal-cell-carcinoma/README.md)** — Basal cell carcinoma is the commonest cancer of the integumentary system: chronic UV damage to basal keratinocytes activates Hedgehog/PTCH1 signaling, producing slow-growing tumors that almost never metastasize—the indolent counterpart to melanoma in the skin.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibroblasts build the integumentary system's dermal scaffold: they synthesize the collagen and elastin that give skin strength and elasticity, and their decline underlies wrinkling and aging—so dermal fibroblasts determine how skin holds up over a lifetime.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Atopic dermatitis is the integumentary system's barrier disease: filaggrin-deficient skin loses water and lets allergens in, triggering itch-scratch inflammation—showing how the epidermal barrier, immune cells and nerves of the skin act as one integrated organ system.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The integumentary and lymphatic systems are intertwined in the skin: dermal lymphatics drain interstitial fluid and ferry antigen-laden dendritic cells to nodes, so when they fail, lymphedema swells the limb and thickens the overlying skin.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Systemic sclerosis turns the integument rigid: autoimmune fibroblast activation deposits excess collagen in the dermis, hardening and tethering the skin—the visible hallmark of a disease that shows how the skin's connective tissue can drive systemic illness.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — The skin is the body's main interface with photons: UV light damages DNA, driving skin cancers and photoaging, yet also powers vitamin D synthesis—so sunlight is both essential to and the chief carcinogen of the integument.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — The skin's deepest layer is built of adipocytes: the subcutaneous hypodermis stores fat for insulation, cushioning, and energy, anchors skin to muscle, and secretes hormones like leptin—so body-fat changes visibly reshape the skin's contour and thickness.
- `connects-to` → **[Pemphigus Vulgaris](../pemphigus-vulgaris/README.md)** — Pemphigus vulgaris shows how autoimmunity can unglue the skin: antibodies against desmoglein dissolve the desmosomes binding keratinocytes, so the epidermis blisters and sloughs—revealing how much the integument depends on cell-to-cell adhesion to stay intact.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — The skin is the front line against Staphylococcus aureus: it colonizes skin and, when the barrier breaks, causes impetigo, cellulitis and abscesses—so the integument's physical and antimicrobial defenses are what normally keep this common pathogen out.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Skin is an estrogen-responsive organ: estrogen maintains dermal collagen, thickness and hydration, so its fall at menopause thins and dries skin and slows wound healing—why hormonal status shapes skin aging.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The skin is an immune organ patrolled by T-helper cells: resident and recruited helper T cells survey the epidermis and dermis for pathogens, and their misdirection drives inflammatory skin diseases like psoriasis and eczema.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — The skin is a thermostat that sheds sodium: sweat glands pour out water and sodium to cool the body by evaporation, so the integument regulates temperature and electrolytes—heavy sweating can drain enough salt to matter.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Skin is built and protected by cholesterol: ceramides and cholesterol cement the outer barrier against water loss, and skin's 7-dehydrocholesterol is the very molecule UV light converts into vitamin D—so the organ both shields and synthesizes.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — The skin itches and welts through histamine: mast cells in the dermis release histamine that dilates vessels and fires itch nerves, producing the hives, flares, and wheals of allergic and urticarial skin reactions.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Skin's outer layer matures along a calcium gradient: rising calcium up through the epidermis drives keratinocytes to differentiate and build the barrier, so disrupting that gradient unravels how the skin renews and seals itself.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — The skin is patrolled by cytotoxic T cells: these killers reside in the epidermis as immune memory, destroying virus-infected and malignant cells but, when misdirected, driving the blistering rashes of severe drug reactions.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Skin tunes body temperature with nitric oxide: it relaxes dermal blood vessels to flush heat to the surface, the vasodilation behind blushing and warmth—and faulty control underlies flushing disorders and cold, poorly perfused skin.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — The skin is the body's largest sensory organ: packed with peripheral nerve endings for touch, temperature, and pain, it is how we feel the world—and where neuropathy first robs sensation.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc keeps skin intact: deficiency causes the rash of acrodermatitis enteropathica and stalls wound healing, because the mineral fuels the rapid epidermal turnover and repair the skin depends on.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — The skin's dense dermal vasculature, lined by endothelial cells, both feeds it and serves thermoregulation, dilating to dump body heat or constricting to conserve it as the surface flushes or pales.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows how skin holds together and waterproofs: keratinocytes are riveted by desmosomes and anchored to the basement membrane by hemidesmosomes, their cytoplasm filled with keratin bundles and melanosomes handed over from melanocytes.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper colors and strengthens the skin: it is the catalytic metal in tyrosinase, the enzyme that makes melanin pigment, and in lysyl oxidase, which cross-links the collagen and elastin that give the dermis its resilience.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Sulfur is what makes hair and nails tough: keratin is rich in the amino acid cysteine, whose sulfur atoms form disulfide bridges that lock the protein into hard, springy fibers — the bonds a perm breaks and reforms.
- `connects-to` → **[Thyroid Hormones (T3/T4)](../../03-molecular/thyroid-hormones/README.md)** — Thyroid hormone tunes the skin: too little leaves it dry, cool, and puffy with myxedema and brittle hair, while too much makes it warm, moist, and flushed — so the skin and its appendages often read out thyroid status at a glance.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — The skin is a window onto the blood: its color reflects hemoglobin — pallor in anemia, bluish cyanosis when deoxygenated hemoglobin rises, and the yellow of jaundice when its breakdown pigment bilirubin builds up.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Skin and kidney share the vitamin D relay: the skin makes vitamin D₃ from sunlight, the kidney performs its final activation, and failing kidneys repay the skin with the relentless itch of uremic pruritus.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol thins and weakens the skin: chronic steroid excess, from Cushing's or long treatment, atrophies the dermis into purple striae, easy bruising, and poor wound healing, making the skin a visible readout of glucocorticoid load.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron status writes itself on skin, hair, and nails: deficiency brings pallor, hair loss, and spoon-shaped koilonychia, while iron overload in hemochromatosis bronzes the skin — the integument reporting the body's iron stores.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Dermal macrophages are the skin's clean-up and defense corps: they engulf invaders and debris breaching the barrier, orchestrate wound repair, and even carry the tattoo pigment that stays locked in the dermis for life.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The skin is the body's largest sensory sheet: specialized nerve endings and Merkel-cell complexes wire it for touch, pressure, temperature, and pain, so neurons turn the integument into a vast field of receptors reporting the outside world.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — The skin is a frontline organ in lupus: photosensitive malar and discoid rashes mark cutaneous SLE, where UV light and autoantibodies drive immune attack at the dermal-epidermal junction, often the disease's first visible sign.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — The skin barrier holds back fungal overgrowth: when warmth, moisture, or immune suppression breach it, Candida colonizes skin folds, nails, and mucocutaneous surfaces, turning a commensal into intertrigo, paronychia, and thrush.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — A virus hides in the skin's nerves and returns: after chickenpox, varicella-zoster lies dormant in sensory ganglia and reawakens as shingles, a painful dermatomal rash that maps the very nerve territory supplying that patch of skin.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — The skin cools itself on an odd nerve signal: eccrine sweat glands are driven by sympathetic fibers that, unusually, release acetylcholine rather than noradrenaline, the cholinergic switch that turns on sweating for thermoregulation.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — When the barrier is breached, neutrophils rush in: they are the front line against skin-invading bacteria, forming the pus of abscesses and cellulitis and clearing the infection that a broken epidermis lets through.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Skin disease can spread to the joints: in a fraction of people with psoriasis of the skin, the same immune process attacks the joints as psoriatic arthritis, a skin-to-joint axis driven by shared IL-17/IL-23 inflammation.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — Its rash is a window onto systemic disease: the heliotrope eyelids and Gottron's papules of dermatomyositis are skin signs of an autoimmune myopathy, the integument flagging a deeper muscle and sometimes malignant process.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Broken skin lets the mold in directly: in burns, surgical wounds and immunocompromised patients, Aspergillus can establish a primary cutaneous infection at the breach, bypassing its usual respiratory route.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Visible skin disease wounds the psyche: disfiguring or itchy conditions like psoriasis, eczema and acne carry high rates of depression, and stress in turn flares the skin — the basis of psychodermatology.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — The skin announces metabolic disease: acanthosis nigricans, diabetic dermopathy, recurrent skin infections and impaired wound healing make the integument an early and telling window onto type 2 diabetes.
- `connects-to` → **[Iron-Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Pallor and brittle nails betray low iron: the skin, nails and hair show iron deficiency through pallor, spoon-shaped koilonychia and hair loss, making the integument a visible readout of the body's iron stores.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The skin mirrors the gut and liver: a gut-skin axis links bowel disease to conditions like dermatitis herpetiformis and pyoderma gangrenosum, while liver failure shows as jaundice and malabsorption as hair and nail change.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Failing kidneys are written on the skin: chronic kidney disease causes intractable uraemic pruritus, a sallow complexion and calciphylaxis, and gadolinium in renal failure can trigger nephrogenic systemic fibrosis.
- `connects-to` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Herpesviruses erupt on the skin: HSV causes cold sores and genital lesions and can spread catastrophically across eczematous skin as eczema herpeticum, while VZV produces chickenpox and shingles.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — The skin announces lung disease: finger clubbing, central cyanosis and tar staining flag chronic respiratory illness, and granulomatous diseases like sarcoidosis strike skin and lung together.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — A rash that signals an emergency: meningococcal sepsis produces a non-blanching petechial and purpuric rash that can progress to purpura fulminans with skin necrosis, demanding immediate antibiotics.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Tuberculosis can settle in the skin: cutaneous TB such as lupus vulgaris and scrofuloderma, and the reactive panniculitis of erythema nodosum, are dermatological signs of mycobacterial infection.
- `connects-to` → **[Leishmania donovani](../../../02-pathogen/04-parasites/leishmania-donovani/README.md)** — A sandfly parasite scars the skin: cutaneous and post-kala-azar dermal leishmaniasis produce chronic disfiguring skin lesions, a major cause of skin disease in endemic regions.
- `connects-to` → **[Dexamethasone](../../../03-medicine/01-modern/12-anti-inflammatory/dexamethasone/README.md)** — Steroids heal and harm the skin: corticosteroids treat inflammatory skin disease, but long-term use thins the skin and causes striae, easy bruising, acne and impaired wound healing.
- `connects-to` → **[Zinc (Dietary)](../../../03-medicine/03-food/zinc-dietary/README.md)** — Zinc keeps the skin intact: zinc is essential for skin integrity and repair, so deficiency causes acrodermatitis enteropathica with perioral and acral dermatitis.
- `connects-to` → **[Coxsackievirus B](../../../02-pathogen/01-viruses/coxsackievirus-b/README.md)** — An enterovirus erupts on the skin: Coxsackievirus causes hand-foot-and-mouth disease with its vesicular rash, and on atopic skin can spread widely as eczema coxsackium.
- `connects-to` → **[Adalimumab](../../../03-medicine/01-modern/11-biologics/adalimumab/README.md)** — Biologics clear severe skin disease: anti-TNF antibodies like adalimumab, with IL-17 and IL-23 inhibitors, treat severe psoriasis and hidradenitis suppurativa of the skin.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Dietary fats support the barrier: omega-3 fatty acids contribute to the skin's lipid barrier and have anti-inflammatory effects studied in eczema and psoriasis.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — The skin shows immunotherapy's signature: checkpoint inhibitors cause the commonest immune-related adverse events in the skin — maculopapular rash, pruritus, lichenoid eruptions and vitiligo — and also treat the melanoma and skin cancers arising there.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — It writes its toxicity on the skin: cytotoxic chemotherapy causes alopecia, painful hand-foot syndrome, mucositis, nail changes and photosensitivity, the visible price of drugs that target all rapidly dividing cells including the skin.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — The skin scars and hardens: dermal fibrosis underlies hypertrophic scars and keloids after injury, the tight bound-down skin of scleroderma, and radiation dermatitis — excess collagen replacing the normal supple dermis.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — When the skin makes too many cancers: Gorlin (nevoid basal cell carcinoma) syndrome causes hundreds of basal cell carcinomas across the skin from germline PTCH1/Hedgehog activation, the heritable extreme of the skin's commonest cancer.
- `connects-to` → **[Rothmund-Thomson](../rothmund-thomson/README.md)** — A congenital poikiloderma: Rothmund-Thomson syndrome marbles the skin with the reticulate pigmentation, telangiectasia and atrophy of poikiloderma, a genodermatosis from RECQL4 loss with photosensitivity and cancer risk.
- `connects-to` → **[Werner Syndrome](../werner-syndrome/README.md)** — Premature ageing of the skin: Werner syndrome gives scleroderma-like tight, atrophic skin with intractable leg ulcers and early greying, a progeroid genodermatosis from WRN-helicase loss.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — A barometer of immune status: HIV/AIDS produces a parade of skin diseases—Kaposi sarcoma, severe seborrhoea, eosinophilic folliculitis—the integument often the first signal of the underlying immunodeficiency.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Where vasculitis shows itself: small-vessel vasculitis like ANCA-associated disease announces itself in the skin as palpable purpura, making the integument a window onto systemic vascular inflammation.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Skin as casualty of systemic disease: chronic, painful leg ulcers over the malleoli are a hard-to-heal complication of sickle cell disease, reflecting the skin's vulnerability to microvascular ischaemia.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — The skin as a window on infection: COVID-19 produces a range of cutaneous signs—chilblain-like 'COVID toes', urticarial, vesicular and maculopapular rashes—that reflect the systemic vascular and immune response.
- `connects-to` → **[PTCL](../ptcl/README.md)** — Lymphoma born in the skin: primary cutaneous T-cell lymphomas like mycosis fungoides and Sézary syndrome arise in the integument itself, making the skin a primary site of lymphoid malignancy.
- `connects-to` → **[GVHD](../gvhd/README.md)** — The first organ of GVHD: the skin is the earliest and commonest target of graft-versus-host disease, its rash and later sclerodermatous change central to diagnosing and grading the alloimmune attack.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Neurogenic itch and inflammation: substance P released by cutaneous sensory nerves drives neurogenic inflammation and the itch sensation central to many skin diseases.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — The itch cytokine: IL-31 is the principal pruritogenic cytokine of the skin, the target of nemolizumab in atopic dermatitis and prurigo nodularis.
- `connects-to` → **[Prurigo Nodularis](../prurigo-nodularis/README.md)** — Neuroimmune itch disease: prurigo nodularis is a chronic, intensely itchy skin disorder that exemplifies the neuroimmune itch circuit linking cutaneous nerves and immune cells.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Epidermal renewal: EGFR signalling drives keratinocyte proliferation and re-epithelialisation, which is why anti-EGFR cancer drugs cause the characteristic acneiform rash and skin toxicity.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Dermal vasculature: VEGF-driven angiogenesis supplies the skin's microcirculation and granulation tissue in wound healing, and its overactivity feeds the dilated vessels of psoriatic and inflamed skin.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Barrier alarmin: damaged keratinocytes release TSLP, the epithelial alarm signal that initiates the type 2 immune response and itch underlying atopic dermatitis and the atopic march.
- `connects-to` → **[Androgen receptor](../../03-molecular/androgen-receptor/README.md)** — Androgens acting through the androgen receptor drive sebaceous-gland activity and hair-follicle patterning, the basis of acne, androgenetic alopecia, and hirsutism—among the most common dermatologic complaints and the target of anti-androgen therapy.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IGF-1 promotes keratinocyte proliferation and hair-follicle growth, linking endocrine and nutritional state to epidermal turnover and contributing to the skin tags and coarse skin of acromegaly as well as to acne pathogenesis.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Prostaglandins mediate the erythema, edema, and pain of sunburn and inflammatory skin disease, and prostaglandin analogues both stimulate eyelash growth and are implicated in the hair-cycle changes of androgenetic alopecia.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt/β-catenin signaling drives the cyclical regeneration of hair follicles and the self-renewal of epidermal stem cells, the developmental pathway that patterns skin appendages and whose dysregulation contributes to alopecia and skin tumors.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — A calcium gradient rising from the basal to the outer epidermis drives keratinocytes through their differentiation program into the cornified barrier, the ionic signal that builds the skin's waterproof outer layer.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Corticosteroids acting through the glucocorticoid receptor are the mainstay anti-inflammatory therapy across dermatology, suppressing the cutaneous immune response in eczema, psoriasis and dermatitis.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling drives keratinocyte differentiation as cells move outward through the epidermal layers and patterns the hair-follicle and sebaceous-gland lineages of the skin.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β governs dermal fibroblast activity, wound repair and hair-follicle cycling, and its dysregulation underlies the cutaneous fibrosis of scleroderma and keloids.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — The skin is a principal site of IL-17A-driven immunity, central both to its antifungal defense and to the inflammatory skin diseases (psoriasis already mapped) of the integument.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — IL-13, with the TSLP and IL-31 already mapped, drives the barrier dysfunction and itch of atopic dermatitis, the archetypal type-2 inflammatory disease of the skin.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — The IL-23/IL-17 axis (IL-17A already mapped) drives the keratinocyte hyperproliferation and inflammation of psoriasis, a defining immune disease of the integument.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — The densely innervated skin relies on BDNF and neurotrophins to maintain its sensory nerves, and their upregulation sensitizes the cutaneous itch-and-pain network in inflammatory skin disease.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 governs the keratinocyte antioxidant response to UV and environmental oxidative stress, central to epidermal barrier maintenance and photoprotection.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α coordinates the cutaneous response to hypoxia during wound healing and supports dermal angiogenesis (VEGF mapped).
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 is a key cutaneous inflammatory cytokine driving keratinocyte responses and dermal inflammation across many skin diseases.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 signaling governs keratinocyte proliferation, the hair-follicle cycle and the IL-6/IL-23-Th17 immunity that is central to inflammatory skin disease.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates cutaneous immunity, wound healing and dermal fibrosis across the disorders of the integumentary system.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — cGAS-STING senses the cytosolic DNA generated by UV damage and infection in the skin, linking the integumentary barrier to innate antiviral and inflammatory responses.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) governs keratinocyte differentiation, wound repair, and dermal fibrosis across the integumentary system.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate keratinocyte oxidative-stress defense, hair-follicle cycling, and epidermal homeostasis in the skin.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of EGFR (EGFR already mapped) drives the keratinocyte proliferation and epidermal renewal of the integumentary system.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling governs the proliferation and survival of keratinocytes and the epidermal barrier renewal of the integumentary system.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β, within the Wnt signaling that patterns hair follicles (Wnt already mapped), regulates the skin-appendage development and epidermal homeostasis of the integumentary system.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antimicrobial and immune-surveillance functions of the skin in the integumentary system.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the keratinocyte and hair-follicle proliferation and survival of the integumentary system.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling integrates nutrient and growth-factor cues to drive the epidermal proliferation and barrier renewal of the integumentary system.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB signaling governs the keratinocyte inflammatory and barrier-defense responses of the integumentary system.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the keratinocyte and sebocyte energy metabolism of the integumentary system.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy maintains the keratinocyte differentiation, barrier formation, and melanocyte homeostasis of the integumentary system.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the keratinocyte adhesion, migration, and growth-factor responses of the integumentary system.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven chemokine signaling participates in the cutaneous immune-cell trafficking of the integumentary system.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the dermal-epidermal and immune-cell interactions of the integumentary system.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the keratinocyte differentiation and skin-immune gene programs of the integumentary system.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic skin signs: insulin and IGF acting on keratinocytes drive acanthosis nigricans, the velvety hyperpigmentation that signals insulin resistance, making the skin a visible window onto systemic metabolic disease.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Pigmentation and vascular tone: endothelin-1 signalling through EDNRB supports melanocyte survival and pigment production and regulates dermal vascular tone, contributing to both skin colour and cutaneous blood flow.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Cutaneous protection: the skin both produces and responds to melatonin, which acts as a local antioxidant against ultraviolet damage and participates in the circadian regulation of the hair follicle cycle.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant selenoproteins: selenium-dependent glutathione peroxidases protect skin and hair from oxidative and ultraviolet damage (NFE2L2 already mapped), and selenium deficiency causes skin and hair changes, part of the integument's antioxidant defence.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Cutaneous serotonin: the skin synthesises and responds to serotonin, which modulates itch, keratinocyte proliferation and dermal blood flow, one of several neurotransmitter systems (substance P already mapped) active in the integument.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine signalling: subcutaneous adipose tissue is part of the integument, and its adipokine leptin influences hair-follicle cycling, wound healing and dermal homeostasis, linking the skin's fat layer to its regenerative biology.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Photo-oxidative stress: ultraviolet exposure (photon already mapped) generates reactive oxygen species in the skin, to which xanthine oxidase contributes, driving the photoaging and DNA damage that the NRF2 antioxidant response (already mapped) counters.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 skin inflammation: IL-4, with IL-13 and IL-31 (already mapped), drives the itch and barrier disruption of atopic dermatitis, part of the type-2 immune axis prominent in inflammatory skin disease of the integument.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Eccrine sweat electrolytes: aldosterone drives sodium reabsorption in the eccrine sweat ducts (acetylcholine already mapped for sweat secretion), conserving salt during heat acclimatisation, a mineralocorticoid function of the integument's sweat glands.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Skin-resident T cells: the CD4 T-helper cells resident in the skin, driving the Th17 and type-2 responses (IL-17, IL-23 and IL-13 already mapped), are central to the inflammatory diseases of the integument such as psoriasis and atopic dermatitis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and skin integrity: zinc is essential for keratinocyte proliferation, wound healing and the many cutaneous enzymes, and its deficiency causes the acrodermatitis and impaired barrier of the integument.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Dermal macrophages: the macrophages of the dermis provide immune surveillance, clear debris and orchestrate the repair (collagen already mapped) of the skin, part of the integument's role as an immune organ.
- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — Inflammatory skin disease: TNF drives psoriasis and the inflammatory dermatoses (IL-17 and IL-23 already mapped), the target of the anti-TNF biologics that transformed the treatment of severe skin disease.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Type-2 dermal remodelling: periostin, a matricellular protein induced by the type-2 cytokines (IL-13 already mapped), drives the dermal remodelling and chronic itch of atopic dermatitis, a biomarker of the barrier-disrupted skin.
- `connects-to` → **[IL-1b](../../03-molecular/il-1b/README.md)** — Keratinocyte alarmin: IL-1β released by the keratinocytes is an alarm cytokine of the skin, driving the inflammation of hidradenitis suppurativa, neutrophilic dermatoses and the response to barrier injury.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Dermal mast cells: the dermal mast cells (histamine already mapped) mediate the itch, the urticaria and the immediate hypersensitivity of the skin of the integumentary system.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Skin-integrity zinc: the zinc essential for the skin integrity and wound healing; the zinc deficiency causes the acrodermatitis enteropathica of the integumentary system.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Melanin and collagen copper: the copper-dependent tyrosinase makes the melanin (endothelin-1 already mapped), and the lysyl oxidase cross-links the dermal collagen (already mapped) and elastin of the skin.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Cutaneous type-2 IgE: the IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped) and the alarmins (TSLP already mapped), drives the atopic and urticarial dermatoses of the integumentary system.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil skin arm: IL-5 recruits the eosinophils of the type-2 (IL-4 and IL-13 already mapped) inflammation of the atopic and eosinophilic dermatoses of the skin.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Plasmacytoid-DC interferon: the type-I interferon of the plasmacytoid dendritic cells (already mapped) drives the interface dermatoses — the cutaneous lupus and the psoriasis (IL-17 and IL-23 already mapped) — of the integumentary system.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 skin immunity: the IFN-γ of the skin T cells is the type-II interferon arm of the Th1 immunity of the interface dermatoses and the antimicrobial defence of the integumentary system.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the cutaneous immune response of the integumentary system.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Skin innate surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance against the virally-infected keratinocytes and the skin cancers of the integumentary system.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Cutaneous complement: the complement C3, deposited and locally produced in the skin, is part of the innate antimicrobial defence and the immune-complex dimension of the cutaneous immunity of the integumentary system.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling recruits the neutrophils and myeloid cells to the site of the cutaneous inflammation of the integumentary system.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Dermal humoral arm: the plasma cells of the dermis secrete the antibodies of the humoral arm of the cutaneous immunity of the integumentary system.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) complete the complement cascade of the innate cutaneous defence of the integumentary system.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) on the skin surface, restraining the complement attack on the host tissue of the integumentary system.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Dermal B cells: the B cells, upstream of the plasma cells (already mapped), contribute to the humoral and organised immune response of the cutaneous immunity of the integumentary system.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Cutaneous kinin signalling: bradykinin, released from skin mast cells (already mapped) and by kallikrein-driven contact activation in wounded epidermis, amplifies the vasodilatation, pruritus, and neurogenic inflammation of the integumentary system.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor restrains classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) activation at the epidermal barrier, controlling the inflammatory response of the integumentary system.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Epidermal EPO axis: erythropoietin, produced locally by dermal fibroblasts (already mapped) and keratinocytes under hypoxic stress (HIF-1α already mapped), supports wound healing (already mapped), epithelial repair, and angiogenesis of the integumentary system.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Cutaneous immune modulator: prolactin, secreted by keratinocytes (already mapped) and dermal fibroblasts (already mapped) in addition to the pituitary, modulates the mast-cell (already mapped) and T-cell (already mapped) responses of the skin immune barrier.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Neuroimmune skin axis: oxytocin, via OXT receptors on keratinocytes (already mapped), melanocytes (already mapped) and dermal fibroblasts (already mapped), promotes wound healing (already mapped) and collagen remodelling of the integumentary system.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sebaceous-follicular androgen: testosterone, converted to DHT by 5α-reductase in sebaceous glands (already mapped) and hair follicles (already mapped), drives sebum production and the androgenic regulation of the pilosebaceous unit of the integumentary system.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — IS vasopressin: vasopressin (ADH) constricts cutaneous microvessels via V1 receptor on skin (already mapped) endothelium; vasopressin also modulates mast-cell (already mapped) degranulation and the wound-healing (already mapped) fibroblast (already mapped) response.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — IS transferrin: transferrin delivers iron for collagen (already mapped) synthesis by fibroblasts (already mapped) in skin (already mapped) wound-healing (already mapped); iron deficiency impairs skin (already mapped) barrier repair and IL-6 (already mapped) regeneration.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — IS magnesium: magnesium supports collagen (already mapped) crosslinking and fibroblast (already mapped) function in skin (already mapped); magnesium deficiency amplifies mast-cell (already mapped) degranulation and IL-6 (already mapped) cutaneous inflammation.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — IS iodine: thyroid-hormone signalling drives keratinocyte differentiation and skin (already mapped) barrier integrity; iodine deficiency impairs wound-healing (already mapped) via NF-κB (already mapped) and IL-6 (already mapped) mediated fibroblast (already mapped) dysfunction.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — IS potassium: potassium channels regulate keratinocyte proliferation and skin (already mapped) barrier; potassium imbalance disrupts NF-κB (already mapped) and IL-6 (already mapped) mediated mast-cell (already mapped) responses and impairs collagen (already mapped) deposition.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — IS phosphorus: phosphorus supports ATP-driven synthesis of collagen (already mapped) by fibroblasts (already mapped) and keratinocyte integrity; hypophosphataemia impairs skin (already mapped) wound-healing (already mapped) and amplifies NF-κB (already mapped) inflammation.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — IS chloride: chloride, via ion channels in macrophages (already mapped) and mast cells (already mapped), maintains epidermal homeostasis; chloride dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of the integumentary system.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — IS nitrogen: nitrogen, as backbone of collagen (already mapped) in fibroblasts (already mapped) and skin (already mapped), supports structural integrity; nitrogen deficiency impairs wound-healing (already mapped) and amplifies the IL-6 (already mapped) inflammatory cascade.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — IS carbon: carbon, forming the backbone of ceramide lipids and melanin in skin (already mapped) and fibroblasts (already mapped), maintains epidermal barrier; carbon-skeleton insufficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) skin-barrier cascade.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — IS oxygen: oxygen, via ROS in fibroblasts (already mapped) and macrophages (already mapped), drives epidermal oxidative stress; oxygen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of the integumentary system.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — IS hydrogen: hydrogen, as water framework in skin (already mapped) and fibroblasts (already mapped), maintains epidermal hydration; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and wound-healing (already mapped) cascade.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Integumentary PD-1: PD-1 checkpoint on skin-resident T-cells (already mapped) suppresses anti-tumour immunity; PD-1 dysregulation amplifies IL-6 (already mapped) and TNF-α (already mapped) and VEGF (already mapped) signalling in integumentary immune surveillance.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Integumentary GLP-1: GLP-1 from skin adipocytes modulates keratinocyte (already mapped) proliferation and wound healing; GLP-1 dysregulation amplifies TNF-α (already mapped) and IL-6 (already mapped) inflammatory cascade of integumentary barrier.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — Integumentary angiotensin-II: angiotensin-II mediates dermal vasoconstriction (already mapped) and fibroblast (already mapped) activation; angiotensin-II amplifies TGF-β (already mapped) and IL-6 (already mapped) fibrotic cascade of integumentary system.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Integumentary rankl: RANKL from keratinocytes (already mapped) and macrophages (already mapped) amplifies skin immune activation; rankl dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Integumentary il-2: IL-2 from skin-resident T-cells (already mapped) and macrophages (already mapped) amplifies adaptive immune responses; il-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Integumentary notch: Notch in keratinocytes (already mapped) and fibroblasts (already mapped) regulates epidermal differentiation; notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of integumentary system.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Integumentary fibronectin: fibronectin in fibroblasts (already mapped) and keratinocytes (already mapped) anchors dermal ECM; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of integumentary system.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Integumentary activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) drives fibrotic remodelling; activin-a dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of integumentary system.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Integumentary cgrp: CGRP from sensory neurons (already mapped) and mast cells (already mapped) drives neurogenic skin inflammation; cgrp dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Integumentary calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates skin calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — Integumentary fgf23: FGF23 from macrophages (already mapped) and fibroblasts (already mapped) regulates skin phosphate and keratinocyte growth; fgf23 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — Integumentary insulin-receptor: insulin-receptor on fibroblasts (already mapped) and macrophages (already mapped) modulates homeostasis; receptor dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of integumentary system.

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
