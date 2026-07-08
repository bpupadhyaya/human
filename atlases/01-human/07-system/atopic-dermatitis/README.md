---
schema: human-scale-entry/v1
id: atopic-dermatitis
name: Atopic Dermatitis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Chronic relapsing type 2 inflammatory skin disease; IL-4/IL-13 → STAT6 → filaggrin and barrier protein suppression → epidermal barrier failure and Th2 sensitization; dupilumab (anti-IL-4Rα) and JAK1 inhibitors (upadacitinib) are first-line biologics."
aliases: ["atopic dermatitis", "AD", "eczema", "atopic eczema", "IgE-mediated dermatitis"]
sources:
  - id: weidinger-2018-atopic-dermatitis
    type: peer-reviewed
    cite: "Weidinger S, Beck LA, Bieber T, Kabashima K, Steinhoff M. Atopic dermatitis. Nat Rev Dis Primers. 2018;4(1):1."
    doi: "10.1038/s41572-018-0001-z"
    pmid: "30464227"
    url: "https://doi.org/10.1038/s41572-018-0001-z"
  - id: simpson-2016-dupilumab-ad
    type: peer-reviewed
    cite: "Simpson EL, Bieber T, Guttman-Yassky E, et al. Two Phase 3 Trials of Dupilumab versus Placebo in Atopic Dermatitis. N Engl J Med. 2016;375(24):2335-2348."
    doi: "10.1056/NEJMoa1610020"
    pmid: "27690741"
    url: "https://doi.org/10.1056/NEJMoa1610020"
cross_links:
  - target: 01-human/03-molecular/il-4
    relation: modulated-by
    note: "IL-4 → IL-4Rα/STAT6 → filaggrin (FLG), claudin-1, and loricrin suppression → barrier dysfunction; Th2 polarization and IgE class switching; dupilumab (anti-IL-4Rα) blocks IL-4 and IL-13 → 51% EASI-75 at 16 weeks in Phase 3 trials."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Atopic dermatitis initiates the atopic march: IL-4/IL-13 drives IgE class switching and mast cell sensitization; mast cell FcεRI → histamine and PGD2 on allergen exposure; systemic IgE sensitization to food/aeroallergens predisposes to allergic rhinitis and asthma."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Chronic AD scratching cycles → IL-4/IL-13 → TGF-β from keratinocytes and fibroblasts → skin fibrosis (lichenification); TGF-β also promotes peripheral Treg induction and restrains the acute phase; elevated skin TGF-β1 is a marker of chronic-phase barrier fibrosis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Pediatric and Asian-predominant AD phenotypes have increased Th17 (IL-17A/IL-22) inflammation alongside Th2; IL-17A → antimicrobial peptide induction but also barrier disruption synergy with IL-4/IL-13; lebrikizumab, tralokinumab (anti-IL-13) provide IL-13-selective blockade."
  - target: 01-human/03-molecular/il-13
    relation: modulated-by
    note: "IL-13 → IL-13Rα1/IL-4Rα → STAT6 → FLG, claudin-1, loricrin suppression → barrier failure; IL-13 is the dominant effector in chronic AD lichenification and fibrosis; tralokinumab (ECZTRA 1/2: 38% IGA 0/1) and lebrikizumab (ADVOCATE: 43% IGA 0/1) target IL-13 specifically."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 from damaged keratinocytes → ST2+ mast cells and ILC2 → Th2 priming and histamine release; TSLP + IL-33 + IL-25 cooperate as the three-alarmin cascade; scratching-induced epidermal damage releases IL-33 from keratinocyte nuclei and amplifies itch-scratch cycles."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "IL-31 from Th2/mast cells in AD → IL-31RA on DRG sensory neurons → JAK1 → TRPV1/TRPA1 → itch; serum IL-31 correlates with AD pruritus severity; nemolizumab (anti-IL-31RA, 30 mg Q4W) reduces AD itch NRS ≥4-point in ~50% vs. ~21% (ARCADIA trials)."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "~50-70% of PN patients have comorbid or preceding AD; both share Th2/Th22 axis and respond to dupilumab; PN represents a neural end-stage of the AD itch-scratch cycle with fibrotic nodules and central sensitization; dupilumab is approved for both PN and AD."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10 from regulatory B cells and Th2 cells dampens AD inflammation; paradoxically, Th2-skewed IL-4/IL-13 environment suppresses macrophage IL-10 production; imbalance between IL-10 and type-2 cytokines determines AD chronicity; IL-10 serum levels inversely correlate with SCORAD."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Periostin is a type 2 biomarker in AD: IL-4/IL-13 → STAT6 → dermal fibroblast POSTN → serum periostin correlates with AD severity; dermal periostin → integrin αvβ3 on keratinocytes → TSLP production; periostin tracks type 2 skin inflammation and dupilumab response."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Atopic dermatitis is the prototypical chronic inflammatory skin disease: a defective epidermal barrier (filaggrin loss) lets allergens and microbes in, triggering Th2/IL-4/IL-13 inflammation → itchy, eczematous, lichenified plaques; barrier repair is central to treatment."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Atopic dermatitis is usually the first step of the atopic march: early-life skin-barrier breakdown promotes allergic sensitization that progresses to food allergy, asthma and allergic rhinitis; AD and asthma share Th2/IL-4/IL-13 biology, so dupilumab treats both."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Staphylococcus aureus densely colonizes atopic-dermatitis skin and drives flares: barrier defects and reduced antimicrobial peptides let S. aureus dominate the skin microbiome, and its superantigens and toxins amplify Th2 inflammation and itch—so its load tracks disease severity."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Atopic dermatitis and psoriasis are the two major inflammatory skin diseases but immunologically opposite: AD is Th2-driven (IL-4/13/31) with itchy eczema and a leaky barrier, while psoriasis is Th17/IL-23-driven with sharp scaly plaques—dictating different biologics."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Atopic dermatitis is a prototypic Th2 helper-T-cell disease: Th2 cells release IL-4, IL-13, and IL-31 that drive IgE switching, barrier disruption, and itch—why dupilumab (IL-4/13 blockade) and JAK inhibitors interrupting this signaling are transformative."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells initiate atopic dermatitis at the skin barrier: Langerhans cells and inflammatory dendritic epidermal cells capture allergens entering through the defective barrier and prime Th2 responses, sitting at the start of the cascade from barrier failure to inflammation."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine drives the acute hives of atopic dermatitis but not the chronic itch: mast-cell histamine causes early wheal-and-flare, yet AD's relentless scratching is largely non-histaminergic, so antihistamines help little beyond sedation."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells amplify atopic dermatitis: IgE-primed skin mast cells release histamine and cytokines that fuel itch and type 2 inflammation, and their numbers rise in chronic lesions—linking the allergic sensitization of AD to the visible eczema and the itch-scratch cycle."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "TSLP is a master switch in atopic dermatitis: damaged keratinocytes release this alarmin that activates dendritic cells and drives the Th2 response and itch, positioning TSLP upstream of the IL-4/IL-13 axis—and making it a target for newer biologic therapies."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK inhibitors are a powerful new class for atopic dermatitis: the disease's type 2 cytokines (IL-4, IL-13, IL-31) signal through JAK, so oral JAK inhibitors and the IL-4/13 blocker dupilumab can clear severe eczema that resists topical steroids."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Atopic dermatitis is the integumentary system's signature inflammatory disease: a defective skin barrier (often from filaggrin loss) lets in allergens and microbes that ignite type 2 inflammation, so it exemplifies how barrier and immunity fail together in skin."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Atopic dermatitis is dominated by itch wired through the nervous system: cytokines like IL-31 directly excite sensory nerves, and chronic scratching sensitizes itch pathways—so eczema's torment is as much a neural as an inflammatory disease."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells fuel atopic dermatitis through IgE: in the allergic skin, B cells class-switch to make the IgE that arms mast cells, so elevated IgE marks the atopic phenotype—and B-cell-derived antibodies tie eczema to the broader allergic march."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut (and skin) microbiome shapes atopic dermatitis: early-life dysbiosis skews immunity toward allergy, and the eczematous skin is overrun by Staphylococcus aureus, so microbial balance influences both onset and flares of the disease."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D modulates atopic dermatitis: it supports the skin barrier and antimicrobial defense and tempers type-2 inflammation, so deficiency is linked to more severe eczema and supplementation is studied as adjunct therapy."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Atopic dermatitis is first treated with cortisol's synthetic cousins: topical corticosteroids calm the Th2 inflammation that drives the itch-scratch eczema, though long-term potent use thins skin and can suppress the body's own cortisol axis."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Atopic dermatitis reflects failed immune tolerance: regulatory T cells normally restrain Th2 responses to harmless allergens, and when they underperform the skin's barrier breakdown lets allergens provoke the chronic allergic inflammation of eczema."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc deficiency mimics atopic dermatitis: too little zinc produces an eczema-like rash (acrodermatitis) and impairs the skin barrier and immune regulation, so refractory 'eczema' sometimes turns out to be a correctable zinc shortfall."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The itch of atopic dermatitis is wired through sensory neurons: cytokines like IL-31 sensitize skin nerve endings, so even light touch triggers itch, and the resulting scratch damages the barrier and worsens inflammation—the itch-scratch cycle."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Substance P links nerves to the eczema flare: sensory nerves release this neuropeptide, which activates mast cells and immune cells to amplify itch and inflammation, a neurogenic loop that helps explain why stress can worsen atopic dermatitis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "A calcium gradient builds the skin barrier that eczema lacks: keratinocytes use rising calcium to mature into the protective outer layer, so disrupted calcium signaling impairs the barrier whose leakiness lets allergens and microbes in."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Light can heal eczema: narrowband UVB phototherapy delivers controlled photons that calm the overactive skin immune cells and itch, a mainstay for widespread atopic dermatitis, while sunlight also makes vitamin D."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Atopic dermatitis often inflames the eyes: eyelid eczema and atopic keratoconjunctivitis are common, and the biologic dupilumab can itself cause conjunctivitis, so eye care is part of managing severe disease."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Eczema is tied to the gut: through the gut-skin axis, dysbiosis and food sensitization in the large intestine shape the atopic march, linking infant eczema to later food allergy and asthma."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Atopic dermatitis itches through nerves: sensitized peripheral nerve fibers, fired by IL-31 and inflammation, drive the relentless itch-scratch cycle that defines the disease."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Atopic dermatitis often begins the atopic march: the same Th2 allergy that breaks the skin barrier later inflames the lungs, so infant eczema predicts childhood asthma."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibroblasts thicken chronic eczema: in lichenified skin they lay down extra collagen in response to persistent scratching and inflammation, producing the leathery, deeply lined plaques."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the leaky barrier of eczema: filaggrin-deficient skin makes too few of the lamellar lipid layers that seal the stratum corneum, and inflamed cells pull apart in spongiosis, letting water out and allergens in."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Eczema reaches the mind: the relentless itch wrecks sleep and the disorder is strongly comorbid with anxiety, depression, and ADHD, so the skin disease casts a heavy neuropsychiatric shadow."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Severe eczema may tax the heart: like other chronic inflammatory skin diseases, long-standing atopic dermatitis is linked to a modestly raised cardiovascular risk from its systemic inflammation."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Biologic antibodies rewrote eczema care: dupilumab blocks the shared IL-4/IL-13 receptor and tralokinumab targets IL-13, monoclonal antibodies that calm the type-2 inflammation — while sky-high IgE marks the atopic state behind it."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "The itch is worst at night: eczema flares as cortisol falls and skin loses water in the evening, and the disrupted melatonin and broken sleep that follow blunt mood, growth, and the next day's coping."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Scratched eczema invites infection: the broken barrier is readily colonized by Staphylococcus aureus, and frank impetiginization draws neutrophils as the oozing, crusted flare of secondary bacterial infection sets in."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Visible, sleepless itch wears down the mind: atopic dermatitis carries high rates of depression and anxiety from chronic itch, broken sleep, and the social toll of inflamed skin, so mental health is part of its care."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy unsettles the eczema: atopic dermatitis commonly flares in pregnancy (atopic eruption of pregnancy), and the safety of systemic drugs and dupilumab must be weighed when treating an expecting patient."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Chronic scratching remodels the skin: years of rubbing thicken it into leathery, lichenified plaques as fibroblasts lay down dermal collagen, the fibrotic end-stage of long-standing atopic dermatitis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "The type-2 storm recruits eosinophils: IL-5 from Th2 cells draws eosinophils into the inflamed skin and raises the blood eosinophil count, part of the allergic cytokine signature that ties eczema to asthma and allergy."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "The broken barrier invites fungi: the impaired skin defense of atopic dermatitis lets Candida and Malassezia colonize and flare the rash, one of the microbial overgrowths that complicate eczema alongside Staph."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "The itch wears on the mind: relentless pruritus, broken sleep, and visible skin disease drive anxiety and depression, so atopic dermatitis carries a heavy psychiatric comorbidity that worsens its course."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Eczema steals sleep: nighttime itch and scratching fragment sleep in atopic dermatitis, and the chronic sleep loss compounds the daytime fatigue, mood disturbance, and impaired quality of life central to the disease's burden."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "The damaged barrier alarms the inflammasome: irritants and microbes crossing the broken skin activate keratinocyte NLRP3, releasing IL-1β that adds an innate-inflammatory layer to the type-2 immune drive of atopic dermatitis."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Visible eczema breeds social fear: the appearance of widespread inflamed skin drives embarrassment and avoidance, so atopic dermatitis carries elevated social anxiety distinct from its general mood burden."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The itch and Th2 signals funnel through JAK-STAT: IL-4, IL-13 and IL-31 act via STAT signaling including STAT3 in keratinocytes and sensory neurons, the pathway that JAK inhibitors block to calm atopic dermatitis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "A broken barrier keeps NF-κB switched on: microbes and irritants crossing the disrupted skin activate NF-κB in keratinocytes, sustaining the cytokine and antimicrobial-peptide output that drives chronic eczema inflammation."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Broken skin colonized by Staph can turn invasive: severe atopic dermatitis is heavily colonized by Staphylococcus aureus, and widespread barrier breakdown or eczema herpeticum can let infection reach the bloodstream as sepsis."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "The itch-disrupted brain wires toward inattention: atopic dermatitis is associated with a higher rate of ADHD, mediated partly by sleep disruption from nocturnal itch and shared inflammatory effects on the developing brain."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Severe eczema and obesity reinforce each other: obesity's adipokine-driven inflammation worsens atopic dermatitis, and the sleep loss and reduced activity of severe disease in turn promote weight gain."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Chronic inflammation nudges toward metabolic disease: severe atopic dermatitis is associated with features of the metabolic syndrome, its systemic type-2 and innate inflammation contributing to insulin resistance and type 2 diabetes risk."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Scratching breaks the barrier it depends on: the relentless itch of atopic dermatitis drives excoriation that erodes the skin and impairs its barrier, leaving wounds slow to heal and prone to infection."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Broken eczematous skin invites strep: alongside Staphylococcus, the disrupted barrier of atopic dermatitis is readily superinfected by Streptococcus pyogenes, causing impetiginized eczema and cellulitis."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "The itch-scratch cycle meets compulsion: the chronic urge to scratch in atopic dermatitis overlaps with OCD-spectrum skin-picking, the two reinforcing each other and worsening skin damage."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is a Th2 immune disease: atopic dermatitis is driven by type-2 inflammation with IL-4 and IL-13, the basis of the atopic march and the target of biologics like dupilumab."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Herpes can race across broken skin: HSV infecting eczematous skin causes eczema herpeticum, a rapidly spreading, painful vesicular eruption that is a dermatological emergency in atopic dermatitis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its steroid treatment reaches the glands: prolonged topical and systemic corticosteroids for severe atopic dermatitis can suppress the adrenal axis and, in children, blunt growth."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It begins the atopic march: infant atopic dermatitis predicts later asthma and allergic rhinitis, sharing the type 2 IL-4/IL-13 inflammation that dupilumab now treats across both."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Widespread disease swells the nodes: erythrodermic and extensive atopic dermatitis causes dermatopathic lymphadenopathy, and barrier breakdown lets infection drain to and inflame the lymph nodes."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chronic skin inflammation reaches the vessels: severe atopic dermatitis carries a modestly increased cardiovascular risk attributed to its sustained systemic inflammation."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Part of the atopic march: atopic dermatitis predisposes to food allergy and eosinophilic oesophagitis, and an impaired gut barrier interacts with the same allergic immune drive."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "First-line calms the flare: topical corticosteroids are the mainstay of treatment, with short courses of systemic steroids reserved for severe disease despite their skin-thinning and rebound risks."
  - target: 02-pathogen/01-viruses/coxsackievirus-b
    relation: connects-to
    note: "A broken barrier invites viral spread: atopic skin is prone to eczema coxsackium, a widespread eruption when Coxsackie virus disseminates across the damaged skin, akin to eczema herpeticum."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet draws prevention interest: omega-3 supplementation, especially in infancy, has been studied for preventing and easing atopic dermatitis, with modest and inconsistent evidence."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Shared immune dysregulation links them: atopic dermatitis and inflammatory bowel disease co-occur more than expected, sharing barrier and immune-pathway defects, and JAK inhibitors treat both."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Chronic skin inflammation reaches the arteries: like psoriasis, severe atopic dermatitis is associated with higher cardiovascular and atherosclerotic risk through sustained systemic inflammation."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Type-2 biologics transformed it: dupilumab against IL-4Rα and tralokinumab against IL-13, with oral JAK inhibitors, clear moderate-to-severe atopic dermatitis by blocking the IL-4/IL-13 type-2 inflammation that drives it."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Older systemic immunosuppressants still serve: methotrexate, azathioprine, mycophenolate and ciclosporin are used for severe atopic dermatitis before or alongside biologics, broad suppressors of the immune flare."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "A gut-skin barrier parallel: the same barrier and type-2 immune dysregulation of atopic dermatitis extends to the gut, where altered intestinal-epithelial integrity and the microbiome shape food sensitisation and the atopic march."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Making the allergic antibody: IgE class-switching in the germinal centres of lymphoid tissue produces the allergen-specific IgE that drives the atopic march from eczema to asthma."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Itch that rewires the cord: chronic scratching in atopic dermatitis sensitises itch-processing synapses in the spinal cord and brain, so the itch outlasts the rash—central sensitisation of pruritus."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "The IgE factory: plasma cells differentiating from atopic B cells secrete the allergen-specific IgE that arms mast cells, sustaining the allergic inflammation of atopic dermatitis."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "The atopic march begins early: severe infant RSV bronchiolitis is linked to later recurrent wheeze and asthma, part of the atopic march that often starts with atopic dermatitis."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Skin-brain comorbidity: atopic dermatitis is associated with higher rates of ADHD and autism spectrum disorder, possibly through chronic itch, sleep loss and shared inflammatory pathways."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Steroids and bone: long courses of systemic corticosteroids for severe atopic dermatitis, plus chronic inflammation, can lower bone mineral density and raise fracture risk."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Cutaneous viral spread: the broken skin barrier of atopic dermatitis predisposes to widespread cutaneous viral infection, including disseminated varicella-zoster, alongside the classic eczema herpeticum."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine link to obesity: leptin, a pro-inflammatory adipokine raised in obesity, helps explain the association between higher body weight and more severe atopic dermatitis."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Th2 versus Th1 axis: atopic, Th2-skewed dermatitis shows an inverse epidemiological relationship with Th1-driven type 1 diabetes, illustrating the immune system's Th1/Th2 balance."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Neurogenic itch: CGRP released from cutaneous sensory nerves drives the neurogenic inflammation and itch-scratch cycle of atopic dermatitis, linking the nervous system to the skin lesions."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Chronic-phase inflammation: TNF-α contributes to the mixed inflammation of chronic, lichenified atopic dermatitis lesions, beyond the Th2 cytokines that dominate the acute phase."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory amplifier: IL-6 is elevated in atopic dermatitis and correlates with severity, contributing to systemic inflammation and the comorbidities that accompany the disease."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Barrier and proliferation: EGFR signalling drives keratinocyte proliferation and barrier repair, and the type 2 cytokines of atopic dermatitis disrupt this and the differentiation that maintains the skin barrier."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Dermal vascularity: VEGF rises in atopic dermatitis lesions, driving the dermal angiogenesis and vascular leak that accompany the chronic inflammation of eczematous skin."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 helps recruit monocytes and inflammatory cells into atopic dermatitis lesions, supporting the cellular infiltrate that sustains chronic eczema."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neural sensitisation: nerve growth factor signalling through TrkA drives the cutaneous nerve sprouting and sensitisation of atopic dermatitis, lowering the itch threshold and perpetuating the itch-scratch cycle."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Mast-cell itch: KIT-dependent mast cells accumulate in atopic dermatitis lesions, releasing histamine and type-2 mediators that drive itch and amplify the allergic inflammation of the disease."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Barrier lipid deficiency: the skin barrier depends on lamellar lipids — ceramides, cholesterol and free fatty acids — and their deficiency in atopic dermatitis impairs the permeability barrier, driving transepidermal water loss and allergen entry."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Topical mainstay: corticosteroids acting through the glucocorticoid receptor are the first-line topical anti-inflammatory for atopic dermatitis, broadly suppressing the type-2 immune response of the eczematous skin lesion."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Barrier differentiation: the epidermal calcium gradient that drives keratinocyte differentiation into the cornified barrier is disordered in atopic dermatitis, contributing to the defective barrier that lets allergens and microbes penetrate the skin."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Cholinergic itch: in atopic skin, acetylcholine provokes itch rather than the pain it evokes in normal skin, a switched neural response that contributes to the intense, treatment-resistant pruritus of atopic dermatitis."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Spongiosis: T-cell-driven caspase-3 apoptosis of keratinocytes produces the intercellular oedema (spongiosis) of acute atopic-dermatitis lesions, disrupting the epidermal barrier."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Innate alarmin: IL-1β released by stressed keratinocytes, alongside the TSLP and IL-33 already mapped, amplifies the innate inflammation that initiates and sustains the atopic-dermatitis lesion."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Barrier oxidative defence: barrier disruption and inflammation in atopic dermatitis impose oxidative stress, and the NRF2 antioxidant pathway that normally supports keratinocyte barrier function is impaired in the disease."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate skin inflammation: TLR4 sensing of Staphylococcus aureus products and barrier-disruption signals drives the innate skin inflammation that, with cutaneous dysbiosis, amplifies atopic-dermatitis flares."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17/Th22 arm: IL-23 sustains the Th17/Th22 responses (IL-17A already mapped) that contribute to the chronic and intrinsic-type inflammation of atopic dermatitis alongside the dominant Th2 axis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Epidermal hyperplasia: mTOR-driven keratinocyte proliferation contributes to the epidermal hyperplasia (acanthosis) and barrier remodelling of chronic atopic-dermatitis lesions."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling upstream of mTOR (mTOR mapped) drives the keratinocyte proliferation and survival accompanying the epidermal barrier disruption of atopic dermatitis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates the dermal Th2 inflammation and dendritic-cell responses contributing to atopic dermatitis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "EGFR-ERK-MAPK signalling (EGFR mapped) regulates keratinocyte proliferation and barrier responses in atopic dermatitis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antiviral skin defence whose impairment predisposes to the eczema herpeticum that complicates atopic dermatitis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) shapes the skin-barrier homeostasis and remodelling perturbed in atopic dermatitis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING sensing of cytosolic DNA from barrier-damaged keratinocytes contributes to the innate inflammation of atopic dermatitis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the keratinocyte differentiation and oxidative-stress responses relevant to the epidermal barrier dysfunction of atopic dermatitis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the innate inflammation and epidermal activation of atopic dermatitis lesions."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-expressing cytotoxic T cells contribute to the keratinocyte apoptosis and epidermal injury of atopic dermatitis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven inflammatory and keratinocyte signaling of the atopic-dermatitis skin barrier and itch cycle."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the keratinocyte survival and Th2-cell activation of atopic dermatitis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of KIT and IgE-receptor engagement (KIT already mapped) drives the mast-cell activation of atopic dermatitis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the keratinocyte and immune-cell metabolism relevant to atopic dermatitis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the keratinocyte differentiation, barrier function, and innate immune responses of atopic dermatitis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the dermal T-helper-cell infiltration of atopic dermatitis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the keratinocyte-barrier and immune gene programs of atopic dermatitis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte recruitment and skin-immune interactions of atopic dermatitis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the innate immune and inflammatory milieu of atopic-dermatitis skin lesions."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the keratinocyte-barrier and immune gene programs of atopic dermatitis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling, a target of topical calcineurin inhibitors (tacrolimus/pimecrolimus), participates in the T-cell activation of atopic dermatitis."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the neuroimmune and itch modulation of atopic dermatitis."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen presentation: HLA-restricted presentation of allergens by skin dendritic cells drives the Th2 response (IL-4/IL-13 already mapped) of atopic dermatitis, and HLA associations contribute to genetic susceptibility."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormonal flares: atopic dermatitis often fluctuates with the menstrual cycle and pregnancy, implicating estrogen and reproductive-hormone changes in the variation of disease activity in affected women."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Itch and inflammation: nitric oxide modulates the cutaneous sensory neurons and vasodilation of the itch response, contributing to the neurogenic inflammation and flare erythema of atopic dermatitis."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Hormonal flares: atopic dermatitis often fluctuates with the menstrual cycle and pregnancy, implicating progesterone alongside estrogen (already mapped) in the reproductive-hormone variation of disease activity in affected women."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Type-2 macrophages: alternatively activated (M2) macrophages, polarised by the IL-4 and IL-13 (already mapped) of the lesion, contribute to the chronic inflammation and tissue remodelling of long-standing atopic dermatitis."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative skin stress: scratching and chronic inflammation in atopic dermatitis generate oxidative stress, to which xanthine-oxidase-derived reactive oxygen species contribute, further damaging the epidermal barrier already weakened in the disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Itch and inflammation: prostaglandins, especially prostaglandin D2, and the eicosanoids from the inflamed skin contribute to the itch and inflammation of atopic dermatitis (histamine already mapped), part of its pruritic biology."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonergic itch: serotonin contributes to the peripheral and central itch pathways of atopic dermatitis (substance P already mapped), part of the neuroimmune signalling that drives the intractable pruritus."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic association: atopic dermatitis is associated with insulin resistance and the metabolic syndrome (cholesterol already mapped), part of the systemic comorbidity that accompanies the skin disease."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant defence: selenium is essential for the glutathione peroxidases that quench the oxidative stress (xanthine oxidase already mapped) of inflamed skin, and low selenium status has been linked to the severity of atopic dermatitis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine comorbidity: resistin, with leptin (already mapped), is a pro-inflammatory adipokine of the metabolic syndrome (insulin already mapped) that accompanies atopic dermatitis, part of its systemic inflammatory dimension."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and skin: copper is the cofactor of lysyl oxidase that cross-links the dermal collagen (already mapped), and copper handling supports the skin's structural and antioxidant function disturbed in atopic dermatitis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine comorbidity: adiponectin, with leptin and resistin (already mapped), is part of the adipokine dimension of the metabolic-syndrome comorbidity that accompanies atopic dermatitis."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Reciprocal skin disease: atopic dermatitis (type-2, IL-4 and IL-13 already mapped) sits at the opposite immunological pole to psoriasis (Th17, IL-17 already mapped), and blocking IL-4 can occasionally unmask a psoriasiform eruption."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium and skin oxidative defence: selenium supports the antioxidant selenoprotein defence of the skin, and its deficiency contributes to the oxidative and barrier dysfunction of atopic dermatitis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Itch mast cells: the mast cells (KIT and histamine already mapped) release the pruritogens and the type-2 mediators onto the sensitised nerves (substance-P and NGF already mapped) of atopic dermatitis."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Langerhans sensitisation: the epidermal Langerhans/dendritic cells present the allergen and drive the Th2 (already mapped) sensitisation of atopic dermatitis."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "Itch overlap: atopic dermatitis and prurigo nodularis share the type-2 (IL-31, IL-4 and IL-13 already mapped) neuroimmune itch, and the dupilumab treats both."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 chronic-phase arm: the IFN-γ of the T cells is the type-II interferon arm of the Th1 shift seen in the chronic, lichenified lesions of atopic dermatitis, counter to the acute Th2 (IL-4 and IL-13 already mapped)."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the chronic-phase inflammation of atopic dermatitis."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate immunity: the NK cells (perforin already mapped) are part of the innate immune dysregulation and the antiviral (eczema herpeticum) susceptibility of atopic dermatitis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Antiviral interferon defect: the impaired type-I interferon response, downstream of the cGAS-STING (already mapped) and pDC sensing, underlies the antiviral defect and the eczema herpeticum susceptibility of atopic dermatitis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement in skin: the complement C5, with C3 (already mapped), is activated in the atopic-dermatitis skin and contributes to the inflammation and the Staphylococcus aureus (already mapped) response."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling amplifies the neutrophil (already mapped) recruitment and the innate inflammation of the atopic-dermatitis skin."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Tc2 skin infiltrate: the cytotoxic T cells (perforin already mapped), including the type-2 Tc2 subset, are part of the lesional infiltrate contributing to the barrier damage of atopic dermatitis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active in the atopic-dermatitis skin and on the Staphylococcus aureus (already mapped) surface."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement and contact pathways activated in the inflamed atopic-dermatitis skin."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Type-2 matricellular: osteopontin, elevated in the atopic-dermatitis skin and serum, is a matricellular cytokine amplifying the type-2 (IL-4 and IL-13 already mapped) and myeloid inflammation of the eczema."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Chronic-lesion remodelling: collagen, the dermal extracellular-matrix scaffold, is remodelled in the lichenification and dermal fibrosis of the chronic atopic-dermatitis plaque."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Chronic-inflammation iron: transferrin, the iron carrier, reflects the disordered iron handling of the systemic inflammation of severe atopic dermatitis."
---

# Atopic Dermatitis

## Overview

**Atopic dermatitis (AD)** is a **chronic, relapsing, pruritic inflammatory skin disease** affecting approximately **230 million people** worldwide — the most prevalent non-communicable skin disease globally [^weidinger-2018-atopic-dermatitis]. Prevalence is 15–30% in children and 2–10% in adults in developed countries. AD is the initiating disease of the **atopic march**: sensitized individuals progress through AD → allergic rhinitis → asthma in a sequence driven by systemic Th2 immune activation beginning in early childhood.

AD is a **biologically heterogeneous disease** unified by two interdependent defects:
1. **Epidermal barrier failure** — driven by genetic loss-of-function in filaggrin (*FLG*), claudin-1, and other structural proteins, amplified by IL-4/IL-13 suppression of barrier genes
2. **Type 2 (Th2) immune dysregulation** — allergen penetration through the disrupted barrier → Th2 polarization → IL-4, IL-5, IL-13, IL-31 → amplified itch (IL-31 → dorsal root ganglion neurons), IgE sensitization, and further barrier damage

The discovery that **IL-4Rα blockade** with dupilumab breaks this cycle provided the first targeted treatment and confirmed that IL-4/IL-13 is the central pathogenic axis [^simpson-2016-dupilumab-ad].

**Phenotypic subtypes of AD:**

| Phenotype | Dominant cytokines | Features |
|---|---|---|
| European/adult-onset intrinsic | Th2 (IL-4/IL-13) + Th22 | Flexural/lichenified; high IgE; FLG mutations |
| Asian/pediatric | Th2 + Th17 (IL-17A/IL-22) | Nummular; seborrheic distribution; less IgE |
| Pediatric US/Black skin | Th2 + Th17 | Follicular; papular; annular; discoid patterns |
| Elderly-onset | Th2 + Th1 (IFN-γ) | Thicker lichenification; lower IgE; itch-scratch |

## Structure

### Epidermal Barrier Architecture

The epidermal barrier is a multi-layered structural and biochemical defense:

**Stratum corneum (SC):**
- "Brick and mortar" model: corneocytes (anucleate, keratin-filled, cornified envelope) embedded in a lamellar lipid matrix (ceramides, free fatty acids, cholesterol)
- **Tight junctions** (claudin-1, occludin, ZO-1): paracellular seal in stratum granulosum
- **Natural moisturizing factor (NMF):** filaggrin degradation products (urocanic acid, pyrrolidone carboxylic acid) → humectants → retain SC hydration

**Filaggrin (FLG) — the central barrier protein:**
- 400 kDa profilaggrin → processed into 10-12 individual filaggrin monomers in the granular layer
- Filaggrin monomers: bundle and aggregate keratin intermediate filaments → compact corneocytes
- Degradation → NMF components; filaggrin loss → reduced NMF → reduced water-binding → xerosis (dry skin)
- **FLG loss-of-function mutations** (R501X, 2282del4, and ≥50 others): present in 50% of European AD patients; 10% of European population carries ≥1 FLG LOF variant; the single largest genetic risk factor for AD (OR 3–5)
- IL-4 and IL-13 → STAT6 → *FLG* promoter suppression → acquired filaggrin deficiency even in non-FLG mutation carriers

**Lipid barrier:**
- Lamellar bodies (membrane-coating granules) secreted at the SG-SC junction → ceramides, free fatty acids, cholesterol → lipid lamellae
- AD: abnormal ceramide composition (increased short-chain ceramides; reduced ceramide/cholesterol ratio) → impaired lamellar bilayer → transepidermal water loss (TEWL) ↑

### Immunological Compartments in AD Skin

**Acute-phase (2-3 days after allergen challenge):**
- Keratinocyte TSLP, IL-33, IL-25 → ILC2 and mast cell activation → IL-4, IL-5, IL-13 immediate wave
- Th2 infiltration → IL-4/IL-13 → STAT6 → TARC/CCL17 and MDC/CCL22 → additional Th2 recruitment
- Dendritic cells with surface IgE (via FcεRI) → antigen capture → Th2 priming

**Chronic-phase:**
- Persistent Th2 + Th22 (IL-22 → epidermal hyperplasia → acanthosis and lichenification) + some Th1 (IFN-γ)
- Reduced Th17 (relative to psoriasis) in European adults — a key immunological distinction from psoriasis
- IL-31 (Th2 cell-derived): acts on IL-31RA/OSMR on cutaneous sensory neurons → JAK1 → TRPA1 upregulation → intractable itch (prurigo axis)

## Function

### Pathogenic Cascade

**Initiating events:**
1. Genetic predisposition: FLG LOF + immune gene variants (*IL4*, *IL13*, *IL4R*, *SPINK5*, *EMID1*, *OVOL1*, *KIF3A*, *LRCH4* GWAS loci)
2. Environmental exposures: early life microbial dysbiosis, hard water (calcium carbonate → surfactant deposition), detergent exposure, low humidity
3. FLG/barrier gene deficiency → TEWL ↑ → dry skin → mechanical micro-injury from scratching → hapten/allergen penetration

**Sensitization and amplification:**
1. Barrier breach → allergen contact with epidermal DCs and ILC2s
2. Keratinocytes release alarmins (TSLP, IL-33, IL-25) → ILC2 → IL-4, IL-13, IL-5 in hours (innate wave)
3. DCs migrate to regional LN → allergen presentation to naive T cells → IL-4 milieu → Th2 differentiation (GATA-3 induction)
4. Allergen-specific Th2 cells → skin homing (CCR4+ via TARC gradient) → IL-4/IL-13 production → STAT6 → IL-4/IL-13 amplification loop
5. IgE class switching (B cells via IL-4) → systemic IgE → mast cell sensitization in skin and airways → atopic march initiation

**Itch-scratch cycle:**
- IL-31 → IL-31RA on sensory neurons → JAK1/TYK2 → TRPA1/TRPV1 upregulation → itch
- Thymic stromal lymphopoietin (TSLP) also acts directly on sensory neurons via TRPA1 → itch (non-histamine mediated — explains why H1 antihistamines fail in AD)
- Scratching → keratinocyte injury → TSLP, IL-33 release → more immune activation → more itch (vicious cycle)

### Staphylococcus aureus in AD

S. aureus colonizes >90% of AD lesional skin (vs. 20% normal skin):
- **Mechanism:** IL-4/IL-13 → suppresses FLG and β-defensin-2/3, LL-37 → S. aureus ecological advantage
- **Amplification:** S. aureus toxins (alpha toxin, V8 protease, staphylococcal superantigens) → TLR2/TLR4 → TSLP, IL-33 → Th2 amplification; superantigens activate Th2 cells non-specifically → polyclonal IgE production
- **Dupilumab effect:** Reduces S. aureus colonization by restoring barrier protein expression → one mechanism of AD improvement

## Pathology

### Assessment Tools

**EASI (Eczema Area and Severity Index):** 0–72; grades erythema, infiltration, excoriation, lichenification; area-weighted; primary endpoint in clinical trials
- EASI-50/75/90/100: 50%/75%/90%/100% improvement = meaningful clinical thresholds
- IGA (Investigator's Global Assessment) 0/1 = clear or almost clear; secondary endpoint

**SCORAD:** 0–103; combines objective (103-point) + subjective (itch + sleep)

**NRS (Numerical Rating Scale):** 0–10; patient-reported pruritus severity

### Drug Classes

**Dupilumab (Dupixent; anti-IL-4Rα mAb):**
- Blocks both IL-4 and IL-13 via IL-4Rα blockade — the shared receptor component
- SOLO 1/SOLO 2 (Phase 3): 300 mg Q2W → 51% EASI-75; 36% IGA 0/1 vs. 10% placebo at 16 weeks [^simpson-2016-dupilumab-ad]
- Generally well-tolerated; conjunctivitis (15–20%) is the main adverse effect; no immunosuppression-related serious infections
- FDA approved 2017 for moderate-severe AD ≥18 years; subsequently expanded to ≥6 months; also adolescents 12–17 and 6–11 years

**IL-13-selective biologics:**
- **Tralokinumab (Adbry):** Anti-IL-13 mAb; binds IL-13 directly (does not block IL-4); ECZTRA Phase 3: 25% IGA 0/1 at 16 weeks as monotherapy
- **Lebrikizumab (Ebglyss):** Anti-IL-13 mAb; ADvocate Phase 3: 43% IGA 0/1; faster onset than dupilumab claimed; FDA approved 2023

**JAK inhibitors:**
- **Upadacitinib (Rinvoq; JAK1i):** Heads Up trial vs. dupilumab: 71% EASI-75 vs. 61% (superior); FDA approved for moderate-severe AD ≥12 years; BOXED WARNING: malignancy, thrombosis, infections, MACE
- **Baricitinib (Olumiant; JAK1/2i):** BREEZE-AD Phase 3: 40% EASI-75 at 16 weeks; FDA approved; limited to ≥18 years
- **Abrocitinib (Cibinqo; JAK1i):** JADE Phase 3: 63% EASI-75; rapid itch relief (day 2-4); FDA approved; BOXED WARNING shared with class

**IL-31 pathway:**
- **Nemolizumab (anti-IL-31RA):** FDA approved 2024 for prurigo nodularis (first approval); Phase 3 AD trials (ARCADIA): 68% EASI-75 vs. 25% placebo; primarily targets itch; combined with TCS

**Topical therapies:**
- **Topical corticosteroids (TCS):** First-line for flares; tachyphylaxis and skin atrophy with overuse
- **Tacrolimus/pimecrolimus** (topical calcineurin inhibitors): Anti-inflammatory without atrophy; face/folds; BOXED WARNING for rare lymphoma (epidemiological data weak)
- **Ruxolitinib cream (Opzelura; topical JAK1/2i):** FDA approved for mild-moderate AD ≥12 years; avoids systemic toxicity
- **Crisaborole (Eucrisa; PDE4i):** FDA approved for mild-moderate; modest efficacy; now somewhat superseded by topical JAKi

## Connections

- `modulated-by` → **[IL-4](../../03-molecular/il-4/README.md)** — IL-4 → IL-4Rα/STAT6 → filaggrin (FLG), claudin-1, and loricrin suppression → barrier dysfunction; Th2 polarization and IgE class switching; dupilumab (anti-IL-4Rα) blocks IL-4 and IL-13 → 51% EASI-75 at 16 weeks in Phase 3 trials.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — atopic dermatitis is the cardinal atopic disease: IL-4/IL-13-driven IgE class switching and elevated total IgE correlate with AD severity; sensitized mast cells and basophils release histamine and PGD2; IgE-mediated sensitization predisposes to allergic rhinitis and asthma (atopic march).
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — chronic AD scratching cycles → IL-4/IL-13 → TGF-β from keratinocytes and fibroblasts → skin fibrosis (lichenification); TGF-β also promotes peripheral Treg induction and restrains the acute phase; elevated skin TGF-β1 is a marker of chronic-phase barrier fibrosis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — pediatric and Asian-predominant AD phenotypes have increased Th17 (IL-17A/IL-22) inflammation alongside Th2; IL-17A → antimicrobial peptide induction but also barrier disruption synergy with IL-4/IL-13; lebrikizumab, tralokinumab (anti-IL-13) provide IL-13-selective blockade.
- `modulated-by` → **[IL-13](../../03-molecular/il-13/README.md)** — IL-13 → IL-13Rα1/IL-4Rα → STAT6 → FLG, claudin-1, loricrin suppression → barrier failure; IL-13 is the dominant effector in chronic AD lichenification and fibrosis; tralokinumab (ECZTRA 1/2: 38% IGA 0/1) and lebrikizumab (ADVOCATE: 43% IGA 0/1) target IL-13 specifically.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — IL-31 from Th2/mast cells in AD → IL-31RA on DRG sensory neurons → JAK1 → TRPV1/TRPA1 → itch; serum IL-31 correlates with AD pruritus severity; nemolizumab (anti-IL-31RA, 30 mg Q4W) reduces AD itch NRS ≥4-point in ~50% vs. ~21% (ARCADIA trials).
- `connects-to` → **[Prurigo Nodularis](../prurigo-nodularis/README.md)** — ~50-70% of PN patients have comorbid or preceding AD; both share Th2/Th22 axis and respond to dupilumab; PN represents a neural end-stage of the AD itch-scratch cycle with fibrotic nodules and central sensitization; dupilumab is approved for both PN and AD.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10 from regulatory B cells and Th2 cells dampens AD inflammation; paradoxically, Th2-skewed IL-4/IL-13 environment suppresses macrophage IL-10 production; imbalance between IL-10 and type-2 cytokines determines AD chronicity; IL-10 serum levels inversely correlate with SCORAD.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Periostin is a type 2 biomarker in AD: IL-4/IL-13 → STAT6 → dermal fibroblast POSTN → serum periostin correlates with AD severity; dermal periostin → integrin αvβ3 on keratinocytes → TSLP production; periostin tracks type 2 skin inflammation and dupilumab response.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Atopic dermatitis is the prototypical chronic inflammatory skin disease: a defective epidermal barrier (filaggrin loss) lets allergens and microbes in, triggering Th2/IL-4/IL-13 inflammation → itchy, eczematous, lichenified plaques; barrier repair is central to treatment.
- `connects-to` → **[Asthma](../asthma/README.md)** — Atopic dermatitis is usually the first step of the atopic march: early-life skin-barrier breakdown promotes allergic sensitization that progresses to food allergy, asthma and allergic rhinitis; AD and asthma share Th2/IL-4/IL-13 biology, so dupilumab treats both.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Staphylococcus aureus densely colonizes atopic-dermatitis skin and drives flares: barrier defects and reduced antimicrobial peptides let S. aureus dominate the skin microbiome, and its superantigens and toxins amplify Th2 inflammation and itch—so its load tracks disease severity.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Atopic dermatitis and psoriasis are the two major inflammatory skin diseases but immunologically opposite: AD is Th2-driven (IL-4/13/31) with itchy eczema and a leaky barrier, while psoriasis is Th17/IL-23-driven with sharp scaly plaques—dictating different biologics.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Atopic dermatitis is a prototypic Th2 helper-T-cell disease: Th2 cells release IL-4, IL-13, and IL-31 that drive IgE switching, barrier disruption, and itch—why dupilumab (IL-4/13 blockade) and JAK inhibitors interrupting this signaling are transformative.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells initiate atopic dermatitis at the skin barrier: Langerhans cells and inflammatory dendritic epidermal cells capture allergens entering through the defective barrier and prime Th2 responses, sitting at the start of the cascade from barrier failure to inflammation.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine drives the acute hives of atopic dermatitis but not the chronic itch: mast-cell histamine causes early wheal-and-flare, yet AD's relentless scratching is largely non-histaminergic, so antihistamines help little beyond sedation.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells amplify atopic dermatitis: IgE-primed skin mast cells release histamine and cytokines that fuel itch and type 2 inflammation, and their numbers rise in chronic lesions—linking the allergic sensitization of AD to the visible eczema and the itch-scratch cycle.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — TSLP is a master switch in atopic dermatitis: damaged keratinocytes release this alarmin that activates dendritic cells and drives the Th2 response and itch, positioning TSLP upstream of the IL-4/IL-13 axis—and making it a target for newer biologic therapies.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK inhibitors are a powerful new class for atopic dermatitis: the disease's type 2 cytokines (IL-4, IL-13, IL-31) signal through JAK, so oral JAK inhibitors and the IL-4/13 blocker dupilumab can clear severe eczema that resists topical steroids.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Atopic dermatitis is the integumentary system's signature inflammatory disease: a defective skin barrier (often from filaggrin loss) lets in allergens and microbes that ignite type 2 inflammation, so it exemplifies how barrier and immunity fail together in skin.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Atopic dermatitis is dominated by itch wired through the nervous system: cytokines like IL-31 directly excite sensory nerves, and chronic scratching sensitizes itch pathways—so eczema's torment is as much a neural as an inflammatory disease.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells fuel atopic dermatitis through IgE: in the allergic skin, B cells class-switch to make the IgE that arms mast cells, so elevated IgE marks the atopic phenotype—and B-cell-derived antibodies tie eczema to the broader allergic march.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut (and skin) microbiome shapes atopic dermatitis: early-life dysbiosis skews immunity toward allergy, and the eczematous skin is overrun by Staphylococcus aureus, so microbial balance influences both onset and flares of the disease.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D modulates atopic dermatitis: it supports the skin barrier and antimicrobial defense and tempers type-2 inflammation, so deficiency is linked to more severe eczema and supplementation is studied as adjunct therapy.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Atopic dermatitis is first treated with cortisol's synthetic cousins: topical corticosteroids calm the Th2 inflammation that drives the itch-scratch eczema, though long-term potent use thins skin and can suppress the body's own cortisol axis.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Atopic dermatitis reflects failed immune tolerance: regulatory T cells normally restrain Th2 responses to harmless allergens, and when they underperform the skin's barrier breakdown lets allergens provoke the chronic allergic inflammation of eczema.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc deficiency mimics atopic dermatitis: too little zinc produces an eczema-like rash (acrodermatitis) and impairs the skin barrier and immune regulation, so refractory 'eczema' sometimes turns out to be a correctable zinc shortfall.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The itch of atopic dermatitis is wired through sensory neurons: cytokines like IL-31 sensitize skin nerve endings, so even light touch triggers itch, and the resulting scratch damages the barrier and worsens inflammation—the itch-scratch cycle.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Substance P links nerves to the eczema flare: sensory nerves release this neuropeptide, which activates mast cells and immune cells to amplify itch and inflammation, a neurogenic loop that helps explain why stress can worsen atopic dermatitis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — A calcium gradient builds the skin barrier that eczema lacks: keratinocytes use rising calcium to mature into the protective outer layer, so disrupted calcium signaling impairs the barrier whose leakiness lets allergens and microbes in.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Light can heal eczema: narrowband UVB phototherapy delivers controlled photons that calm the overactive skin immune cells and itch, a mainstay for widespread atopic dermatitis, while sunlight also makes vitamin D.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Atopic dermatitis often inflames the eyes: eyelid eczema and atopic keratoconjunctivitis are common, and the biologic dupilumab can itself cause conjunctivitis, so eye care is part of managing severe disease.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Eczema is tied to the gut: through the gut-skin axis, dysbiosis and food sensitization in the large intestine shape the atopic march, linking infant eczema to later food allergy and asthma.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Atopic dermatitis itches through nerves: sensitized peripheral nerve fibers, fired by IL-31 and inflammation, drive the relentless itch-scratch cycle that defines the disease.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Atopic dermatitis often begins the atopic march: the same Th2 allergy that breaks the skin barrier later inflames the lungs, so infant eczema predicts childhood asthma.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibroblasts thicken chronic eczema: in lichenified skin they lay down extra collagen in response to persistent scratching and inflammation, producing the leathery, deeply lined plaques.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the leaky barrier of eczema: filaggrin-deficient skin makes too few of the lamellar lipid layers that seal the stratum corneum, and inflamed cells pull apart in spongiosis, letting water out and allergens in.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Eczema reaches the mind: the relentless itch wrecks sleep and the disorder is strongly comorbid with anxiety, depression, and ADHD, so the skin disease casts a heavy neuropsychiatric shadow.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Severe eczema may tax the heart: like other chronic inflammatory skin diseases, long-standing atopic dermatitis is linked to a modestly raised cardiovascular risk from its systemic inflammation.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Biologic antibodies rewrote eczema care: dupilumab blocks the shared IL-4/IL-13 receptor and tralokinumab targets IL-13, monoclonal antibodies that calm the type-2 inflammation — while sky-high IgE marks the atopic state behind it.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — The itch is worst at night: eczema flares as cortisol falls and skin loses water in the evening, and the disrupted melatonin and broken sleep that follow blunt mood, growth, and the next day's coping.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Scratched eczema invites infection: the broken barrier is readily colonized by Staphylococcus aureus, and frank impetiginization draws neutrophils as the oozing, crusted flare of secondary bacterial infection sets in.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Visible, sleepless itch wears down the mind: atopic dermatitis carries high rates of depression and anxiety from chronic itch, broken sleep, and the social toll of inflamed skin, so mental health is part of its care.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy unsettles the eczema: atopic dermatitis commonly flares in pregnancy (atopic eruption of pregnancy), and the safety of systemic drugs and dupilumab must be weighed when treating an expecting patient.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Chronic scratching remodels the skin: years of rubbing thicken it into leathery, lichenified plaques as fibroblasts lay down dermal collagen, the fibrotic end-stage of long-standing atopic dermatitis.
- `connects-to` → **[Interleukin-5](../../03-molecular/il-5/README.md)** — The type-2 storm recruits eosinophils: IL-5 from Th2 cells draws eosinophils into the inflamed skin and raises the blood eosinophil count, part of the allergic cytokine signature that ties eczema to asthma and allergy.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — The broken barrier invites fungi: the impaired skin defense of atopic dermatitis lets Candida and Malassezia colonize and flare the rash, one of the microbial overgrowths that complicate eczema alongside Staph.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — The itch wears on the mind: relentless pruritus, broken sleep, and visible skin disease drive anxiety and depression, so atopic dermatitis carries a heavy psychiatric comorbidity that worsens its course.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Eczema steals sleep: nighttime itch and scratching fragment sleep in atopic dermatitis, and the chronic sleep loss compounds the daytime fatigue, mood disturbance, and impaired quality of life central to the disease's burden.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The damaged barrier alarms the inflammasome: irritants and microbes crossing the broken skin activate keratinocyte NLRP3, releasing IL-1β that adds an innate-inflammatory layer to the type-2 immune drive of atopic dermatitis.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — Visible eczema breeds social fear: the appearance of widespread inflamed skin drives embarrassment and avoidance, so atopic dermatitis carries elevated social anxiety distinct from its general mood burden.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The itch and Th2 signals funnel through JAK-STAT: IL-4, IL-13 and IL-31 act via STAT signaling including STAT3 in keratinocytes and sensory neurons, the pathway that JAK inhibitors block to calm atopic dermatitis.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — A broken barrier keeps NF-κB switched on: microbes and irritants crossing the disrupted skin activate NF-κB in keratinocytes, sustaining the cytokine and antimicrobial-peptide output that drives chronic eczema inflammation.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Broken skin colonized by Staph can turn invasive: severe atopic dermatitis is heavily colonized by Staphylococcus aureus, and widespread barrier breakdown or eczema herpeticum can let infection reach the bloodstream as sepsis.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — The itch-disrupted brain wires toward inattention: atopic dermatitis is associated with a higher rate of ADHD, mediated partly by sleep disruption from nocturnal itch and shared inflammatory effects on the developing brain.
- `connects-to` → **[Obesity](../obesity/README.md)** — Severe eczema and obesity reinforce each other: obesity's adipokine-driven inflammation worsens atopic dermatitis, and the sleep loss and reduced activity of severe disease in turn promote weight gain.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Chronic inflammation nudges toward metabolic disease: severe atopic dermatitis is associated with features of the metabolic syndrome, its systemic type-2 and innate inflammation contributing to insulin resistance and type 2 diabetes risk.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Scratching breaks the barrier it depends on: the relentless itch of atopic dermatitis drives excoriation that erodes the skin and impairs its barrier, leaving wounds slow to heal and prone to infection.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — Broken eczematous skin invites strep: alongside Staphylococcus, the disrupted barrier of atopic dermatitis is readily superinfected by Streptococcus pyogenes, causing impetiginized eczema and cellulitis.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — The itch-scratch cycle meets compulsion: the chronic urge to scratch in atopic dermatitis overlaps with OCD-spectrum skin-picking, the two reinforcing each other and worsening skin damage.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is a Th2 immune disease: atopic dermatitis is driven by type-2 inflammation with IL-4 and IL-13, the basis of the atopic march and the target of biologics like dupilumab.
- `connects-to` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Herpes can race across broken skin: HSV infecting eczematous skin causes eczema herpeticum, a rapidly spreading, painful vesicular eruption that is a dermatological emergency in atopic dermatitis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its steroid treatment reaches the glands: prolonged topical and systemic corticosteroids for severe atopic dermatitis can suppress the adrenal axis and, in children, blunt growth.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It begins the atopic march: infant atopic dermatitis predicts later asthma and allergic rhinitis, sharing the type 2 IL-4/IL-13 inflammation that dupilumab now treats across both.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Widespread disease swells the nodes: erythrodermic and extensive atopic dermatitis causes dermatopathic lymphadenopathy, and barrier breakdown lets infection drain to and inflame the lymph nodes.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Chronic skin inflammation reaches the vessels: severe atopic dermatitis carries a modestly increased cardiovascular risk attributed to its sustained systemic inflammation.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Part of the atopic march: atopic dermatitis predisposes to food allergy and eosinophilic oesophagitis, and an impaired gut barrier interacts with the same allergic immune drive.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — First-line calms the flare: topical corticosteroids are the mainstay of treatment, with short courses of systemic steroids reserved for severe disease despite their skin-thinning and rebound risks.
- `connects-to` → **[Coxsackievirus B](../../../02-pathogen/01-viruses/coxsackievirus-b/README.md)** — A broken barrier invites viral spread: atopic skin is prone to eczema coxsackium, a widespread eruption when Coxsackie virus disseminates across the damaged skin, akin to eczema herpeticum.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet draws prevention interest: omega-3 supplementation, especially in infancy, has been studied for preventing and easing atopic dermatitis, with modest and inconsistent evidence.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Shared immune dysregulation links them: atopic dermatitis and inflammatory bowel disease co-occur more than expected, sharing barrier and immune-pathway defects, and JAK inhibitors treat both.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Chronic skin inflammation reaches the arteries: like psoriasis, severe atopic dermatitis is associated with higher cardiovascular and atherosclerotic risk through sustained systemic inflammation.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Type-2 biologics transformed it: dupilumab against IL-4Rα and tralokinumab against IL-13, with oral JAK inhibitors, clear moderate-to-severe atopic dermatitis by blocking the IL-4/IL-13 type-2 inflammation that drives it.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Older systemic immunosuppressants still serve: methotrexate, azathioprine, mycophenolate and ciclosporin are used for severe atopic dermatitis before or alongside biologics, broad suppressors of the immune flare.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — A gut-skin barrier parallel: the same barrier and type-2 immune dysregulation of atopic dermatitis extends to the gut, where altered intestinal-epithelial integrity and the microbiome shape food sensitisation and the atopic march.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Making the allergic antibody: IgE class-switching in the germinal centres of lymphoid tissue produces the allergen-specific IgE that drives the atopic march from eczema to asthma.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Itch that rewires the cord: chronic scratching in atopic dermatitis sensitises itch-processing synapses in the spinal cord and brain, so the itch outlasts the rash—central sensitisation of pruritus.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — The IgE factory: plasma cells differentiating from atopic B cells secrete the allergen-specific IgE that arms mast cells, sustaining the allergic inflammation of atopic dermatitis.
- `connects-to` → **[RSV](../rsv/README.md)** — The atopic march begins early: severe infant RSV bronchiolitis is linked to later recurrent wheeze and asthma, part of the atopic march that often starts with atopic dermatitis.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — Skin-brain comorbidity: atopic dermatitis is associated with higher rates of ADHD and autism spectrum disorder, possibly through chronic itch, sleep loss and shared inflammatory pathways.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Steroids and bone: long courses of systemic corticosteroids for severe atopic dermatitis, plus chronic inflammation, can lower bone mineral density and raise fracture risk.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Cutaneous viral spread: the broken skin barrier of atopic dermatitis predisposes to widespread cutaneous viral infection, including disseminated varicella-zoster, alongside the classic eczema herpeticum.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine link to obesity: leptin, a pro-inflammatory adipokine raised in obesity, helps explain the association between higher body weight and more severe atopic dermatitis.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Th2 versus Th1 axis: atopic, Th2-skewed dermatitis shows an inverse epidemiological relationship with Th1-driven type 1 diabetes, illustrating the immune system's Th1/Th2 balance.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Neurogenic itch: CGRP released from cutaneous sensory nerves drives the neurogenic inflammation and itch-scratch cycle of atopic dermatitis, linking the nervous system to the skin lesions.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Chronic-phase inflammation: TNF-α contributes to the mixed inflammation of chronic, lichenified atopic dermatitis lesions, beyond the Th2 cytokines that dominate the acute phase.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory amplifier: IL-6 is elevated in atopic dermatitis and correlates with severity, contributing to systemic inflammation and the comorbidities that accompany the disease.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Barrier and proliferation: EGFR signalling drives keratinocyte proliferation and barrier repair, and the type 2 cytokines of atopic dermatitis disrupt this and the differentiation that maintains the skin barrier.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Dermal vascularity: VEGF rises in atopic dermatitis lesions, driving the dermal angiogenesis and vascular leak that accompany the chronic inflammation of eczematous skin.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 helps recruit monocytes and inflammatory cells into atopic dermatitis lesions, supporting the cellular infiltrate that sustains chronic eczema.
- `connects-to` → **[NTRK / TrkA](../../03-molecular/ntrk/README.md)** — Nerve growth factor signaling through TrkA drives the cutaneous nerve sprouting and sensitization of atopic dermatitis, lowering the itch threshold and perpetuating the itch-scratch cycle that thickens lichenified skin.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT-dependent mast cells accumulate in atopic dermatitis lesions, releasing histamine and type-2 mediators that drive itch and amplify the allergic inflammation underlying the eczematous response.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — The skin barrier depends on lamellar lipids—ceramides, cholesterol, and free fatty acids—and their deficiency in atopic dermatitis impairs the permeability barrier, driving the transepidermal water loss and allergen entry that initiate disease.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Corticosteroids acting through the glucocorticoid receptor are the first-line topical anti-inflammatory for atopic dermatitis, broadly suppressing the type-2 immune response of the eczematous skin lesion.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — The epidermal calcium gradient that drives keratinocyte differentiation into the cornified barrier is disordered in atopic dermatitis, contributing to the defective barrier that lets allergens and microbes penetrate the skin.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — In atopic skin, acetylcholine provokes itch rather than the pain it evokes in normal skin, a switched neural response that contributes to the intense, treatment-resistant pruritus of atopic dermatitis.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — T-cell-driven caspase-3 apoptosis of keratinocytes produces the intercellular edema (spongiosis) of acute atopic-dermatitis lesions, disrupting the epidermal barrier.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β released by stressed keratinocytes, alongside the TSLP and IL-33 already mapped, amplifies the innate inflammation that initiates and sustains the atopic-dermatitis lesion.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Barrier disruption and inflammation in atopic dermatitis impose oxidative stress, and the NRF2 antioxidant pathway that normally supports keratinocyte barrier function is impaired in the disease.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of Staphylococcus aureus products and barrier-disruption signals drives the innate skin inflammation that, with cutaneous dysbiosis, amplifies atopic-dermatitis flares.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains the Th17/Th22 responses (IL-17A already mapped) that contribute to the chronic and intrinsic-type inflammation of atopic dermatitis alongside the dominant Th2 axis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-driven keratinocyte proliferation contributes to the epidermal hyperplasia (acanthosis) and barrier remodeling of chronic atopic-dermatitis lesions.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling upstream of mTOR (mTOR mapped) drives the keratinocyte proliferation and survival accompanying the epidermal barrier disruption of atopic dermatitis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates the dermal Th2 inflammation and dendritic-cell responses contributing to atopic dermatitis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EGFR-ERK-MAPK signaling (EGFR mapped) regulates keratinocyte proliferation and barrier responses in atopic dermatitis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antiviral skin defense whose impairment predisposes to the eczema herpeticum that complicates atopic dermatitis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) shapes the skin-barrier homeostasis and remodeling perturbed in atopic dermatitis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — cGAS-STING sensing of cytosolic DNA from barrier-damaged keratinocytes contributes to the innate inflammation of atopic dermatitis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the keratinocyte differentiation and oxidative-stress responses relevant to the epidermal barrier dysfunction of atopic dermatitis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the innate inflammation and epidermal activation of atopic dermatitis lesions.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-expressing cytotoxic T cells contribute to the keratinocyte apoptosis and epidermal injury of atopic dermatitis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven inflammatory and keratinocyte signaling of the atopic-dermatitis skin barrier and itch cycle.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the keratinocyte survival and Th2-cell activation of atopic dermatitis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of KIT and IgE-receptor engagement (KIT already mapped) drives the mast-cell activation of atopic dermatitis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the keratinocyte and immune-cell metabolism relevant to atopic dermatitis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the keratinocyte differentiation, barrier function, and innate immune responses of atopic dermatitis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the dermal T-helper-cell infiltration of atopic dermatitis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the keratinocyte-barrier and immune gene programs of atopic dermatitis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte recruitment and skin-immune interactions of atopic dermatitis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the innate immune and inflammatory milieu of atopic-dermatitis skin lesions.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the keratinocyte-barrier and immune gene programs of atopic dermatitis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling, a target of topical calcineurin inhibitors (tacrolimus/pimecrolimus), participates in the T-cell activation of atopic dermatitis.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the neuroimmune and itch modulation of atopic dermatitis.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Antigen presentation: HLA-restricted presentation of allergens by skin dendritic cells drives the Th2 response (IL-4/IL-13 already mapped) of atopic dermatitis, and HLA associations contribute to genetic susceptibility.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Hormonal flares: atopic dermatitis often fluctuates with the menstrual cycle and pregnancy, implicating estrogen and reproductive-hormone changes in the variation of disease activity in affected women.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Itch and inflammation: nitric oxide modulates the cutaneous sensory neurons and vasodilation of the itch response, contributing to the neurogenic inflammation and flare erythema of atopic dermatitis.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Hormonal flares: atopic dermatitis often fluctuates with the menstrual cycle and pregnancy, implicating progesterone alongside estrogen (already mapped) in the reproductive-hormone variation of disease activity in affected women.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Type-2 macrophages: alternatively activated (M2) macrophages, polarised by the IL-4 and IL-13 (already mapped) of the lesion, contribute to the chronic inflammation and tissue remodelling of long-standing atopic dermatitis.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative skin stress: scratching and chronic inflammation in atopic dermatitis generate oxidative stress, to which xanthine-oxidase-derived reactive oxygen species contribute, further damaging the epidermal barrier already weakened in the disease.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Itch and inflammation: prostaglandins, especially prostaglandin D2, and the eicosanoids from the inflamed skin contribute to the itch and inflammation of atopic dermatitis (histamine already mapped), part of its pruritic biology.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonergic itch: serotonin contributes to the peripheral and central itch pathways of atopic dermatitis (substance P already mapped), part of the neuroimmune signalling that drives the intractable pruritus.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic association: atopic dermatitis is associated with insulin resistance and the metabolic syndrome (cholesterol already mapped), part of the systemic comorbidity that accompanies the skin disease.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant defence: selenium is essential for the glutathione peroxidases that quench the oxidative stress (xanthine oxidase already mapped) of inflamed skin, and low selenium status has been linked to the severity of atopic dermatitis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine comorbidity: resistin, with leptin (already mapped), is a pro-inflammatory adipokine of the metabolic syndrome (insulin already mapped) that accompanies atopic dermatitis, part of its systemic inflammatory dimension.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and skin: copper is the cofactor of lysyl oxidase that cross-links the dermal collagen (already mapped), and copper handling supports the skin's structural and antioxidant function disturbed in atopic dermatitis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine comorbidity: adiponectin, with leptin and resistin (already mapped), is part of the adipokine dimension of the metabolic-syndrome comorbidity that accompanies atopic dermatitis.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Reciprocal skin disease: atopic dermatitis (type-2, IL-4 and IL-13 already mapped) sits at the opposite immunological pole to psoriasis (Th17, IL-17 already mapped), and blocking IL-4 can occasionally unmask a psoriasiform eruption.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium and skin oxidative defence: selenium supports the antioxidant selenoprotein defence of the skin, and its deficiency contributes to the oxidative and barrier dysfunction of atopic dermatitis.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Itch mast cells: the mast cells (KIT and histamine already mapped) release the pruritogens and the type-2 mediators onto the sensitised nerves (substance-P and NGF already mapped) of atopic dermatitis.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Langerhans sensitisation: the epidermal Langerhans/dendritic cells present the allergen and drive the Th2 (already mapped) sensitisation of atopic dermatitis.
- `connects-to` → **[Prurigo nodularis](../prurigo-nodularis/README.md)** — Itch overlap: atopic dermatitis and prurigo nodularis share the type-2 (IL-31, IL-4 and IL-13 already mapped) neuroimmune itch, and the dupilumab treats both.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 chronic-phase arm: the IFN-γ of the T cells is the type-II interferon arm of the Th1 shift seen in the chronic, lichenified lesions of atopic dermatitis, counter to the acute Th2 (IL-4 and IL-13 already mapped).
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the chronic-phase inflammation of atopic dermatitis.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate immunity: the NK cells (perforin already mapped) are part of the innate immune dysregulation and the antiviral (eczema herpeticum) susceptibility of atopic dermatitis.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Antiviral interferon defect: the impaired type-I interferon response, downstream of the cGAS-STING (already mapped) and pDC sensing, underlies the antiviral defect and the eczema herpeticum susceptibility of atopic dermatitis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement in skin: the complement C5, with C3 (already mapped), is activated in the atopic-dermatitis skin and contributes to the inflammation and the Staphylococcus aureus (already mapped) response.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling amplifies the neutrophil (already mapped) recruitment and the innate inflammation of the atopic-dermatitis skin.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Tc2 skin infiltrate: the cytotoxic T cells (perforin already mapped), including the type-2 Tc2 subset, are part of the lesional infiltrate contributing to the barrier damage of atopic dermatitis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active in the atopic-dermatitis skin and on the Staphylococcus aureus (already mapped) surface.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement and contact pathways activated in the inflamed atopic-dermatitis skin.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Type-2 matricellular: osteopontin, elevated in the atopic-dermatitis skin and serum, is a matricellular cytokine amplifying the type-2 (IL-4 and IL-13 already mapped) and myeloid inflammation of the eczema.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Chronic-lesion remodelling: collagen, the dermal extracellular-matrix scaffold, is remodelled in the lichenification and dermal fibrosis of the chronic atopic-dermatitis plaque.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Chronic-inflammation iron: transferrin, the iron carrier, reflects the disordered iron handling of the systemic inflammation of severe atopic dermatitis.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^weidinger-2018-atopic-dermatitis]: Weidinger S, Beck LA, Bieber T, Kabashima K, Steinhoff M. Atopic dermatitis. *Nat Rev Dis Primers.* 2018;4(1):1. [doi:10.1038/s41572-018-0001-z](https://doi.org/10.1038/s41572-018-0001-z) · [PubMed 30464227](https://pubmed.ncbi.nlm.nih.gov/30464227/)
[^simpson-2016-dupilumab-ad]: Simpson EL, Bieber T, Guttman-Yassky E, et al. Two Phase 3 Trials of Dupilumab versus Placebo in Atopic Dermatitis. *N Engl J Med.* 2016;375(24):2335-2348. [doi:10.1056/NEJMoa1610020](https://doi.org/10.1056/NEJMoa1610020) · [PubMed 27690741](https://pubmed.ncbi.nlm.nih.gov/27690741/)
