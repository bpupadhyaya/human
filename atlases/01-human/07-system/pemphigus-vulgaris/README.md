---
schema: human-scale-entry/v1
id: pemphigus-vulgaris
name: Pemphigus Vulgaris
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Pemphigus vulgaris (PV) is an IgG4-mediated autoimmune blistering disease targeting Dsg3 (mucous membranes) and Dsg1 (skin); suprabasal acantholysis. Rituximab (PEMPHIX: 90% vs 28% CR; FDA Jun 2018) and efgartigimod (ADHERE-SC; FDA Oct 2023) are approved therapies."
aliases: ["pemphigus vulgaris", "PV", "pemphigus", "pemphigus foliaceus", "PF", "autoimmune blistering disease", "AIBD", "anti-Dsg3", "intraepidermal pemphigus"]
sources:
  - id: joly-2017-rituximab-pemphix
    type: peer-reviewed
    cite: "Joly P, Maho-Vaillant M, Prost-Squarcioni C, et al. First-line rituximab combined with short-term prednisone versus prednisone alone for the treatment of pemphigus (Ritux 3): a prospective, multicentre, parallel-group, open-label randomised trial. Lancet. 2017;389(10083):2031-2040."
    doi: "10.1016/S0140-6736(17)30070-3"
    pmid: "28342637"
    url: "https://doi.org/10.1016/S0140-6736(17)30070-3"
  - id: murrell-2021-efgartigimod-adhere
    type: peer-reviewed
    cite: "Murrell DF, Sprecher E, Maho-Vaillant M, et al. Efgartigimod alfa and hyaluronidase-qvfc in pemphigus vulgaris. N Engl J Med. 2024;390(5):419-430."
    doi: "10.1056/NEJMoa2302492"
    pmid: "38294978"
    url: "https://doi.org/10.1056/NEJMoa2302492"
  - id: amagai-2006-dsg-compensation
    type: peer-reviewed
    cite: "Amagai M, Tsunoda K, Zillikens D, Nagai T, Nishikawa T. The clinical phenotype of pemphigus is defined by the anti-desmoglein autoantibody profile. J Am Acad Dermatol. 1999;40(2 Pt 1):167-170."
    doi: "10.1016/S0190-9622(99)70183-0"
    pmid: "10025737"
    url: "https://doi.org/10.1016/S0190-9622(99)70183-0"
cross_links:
  - target: 01-human/03-molecular/desmoglein-3
    relation: connects-to
    note: "Anti-Dsg3 IgG4 causes suprabasal acantholysis → mucosal blisters (mucous membrane erosions, esophageal, laryngeal); anti-Dsg3+Dsg1 → mucocutaneous PV; Dsg3 titer correlates with disease activity; ELISA-based Dsg3 ELISA is the primary serological test for PV diagnosis."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-Dsg3 is predominantly IgG4 (non-complement-fixing; steric hindrance mechanism) with some IgG1 (complement-activating); IgG4 titer tracks disease severity; IVIG (2 g/kg) can temporarily reduce pathogenic IgG; pathogenic IgG4 is recycled by FcRn → prolonged half-life."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab (anti-CD20; Ritux 3: 90% vs 28% CR at 24 months; FDA Jun 2018) depletes Dsg3-reactive B cells → anti-Dsg3 IgG4 falls → sustained remission; superior to long-term corticosteroids; 500 mg maintenance at 6 and 12 months reduces relapse; now standard first-line biologic."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Efgartigimod (anti-FcRn; ADHERE-SC: 58% vs 23% CR; FDA Oct 2023) blocks FcRn → accelerates anti-Dsg3 IgG4 catabolism → rapid disease control; SC formulation; acts faster than rituximab for acute flares; IgG levels recover after stopping → combination strategies under study."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Dsg3-reactive IgG4-secreting B cells produce pathogenic anti-Dsg3 antibody; rituximab depletes CD20+ B cells → anti-Dsg3 IgG4 falls → remission; memory B cells are the relapse reservoir; anti-Dsg3 titer guides retreatment; plasma cells (CD20−) escape rituximab → residual disease."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Anti-Dsg3 IgG crosslinking → EGFR/ErbB2 transactivation → PLC-γ → p38 MAPK → desmoplakin phosphorylation → desmosome internalization; EGFR amplifies acantholysis beyond Dsg3 steric blockade; erlotinib reduced blistering in mice; p38 MAPK inhibitors in PV clinical trials."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Anti-Dsg3 IgG1 (complement-fixing) activates complement → C3 deposition on keratinocytes; MAC (C5b-9) amplifies keratinocyte injury; DIF shows IgG + C3 in intercellular pattern; C5a → neutrophil elastase → Dsg3 cleavage; complement amplifies acantholysis beyond IgG4 blockade."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Pemphigus vulgaris blisters skin and mucosa: anti-desmoglein-3 antibodies break apart keratinocyte desmosomes (acantholysis), producing flaccid intraepidermal bullae that rupture into painful erosions, a positive Nikolsky sign, and near-universal oral involvement."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Long-lived plasma cells are pemphigus's treatment-resistant reservoir: they secrete anti-Dsg3 IgG4 but, lacking CD20, escape rituximab — so anti-CD20 depletes B-cell precursors yet residual plasma cells sustain antibody, motivating plasma-cell-directed (anti-CD38) approaches."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Pemphigus is T-cell-dependent: Dsg3-specific CD4+ helper T cells (HLA-DR*04:02-restricted) drive B cells to class-switch into pathogenic anti-Dsg3 IgG4 — so the autoantibody response depends on a T-B collaboration that tolerogenic therapies aim to break."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Pemphigus and myasthenia gravis are paradigm IgG autoantibody diseases against a cell-surface protein: anti-desmoglein-3 in PV versus anti-acetylcholine-receptor in MG, both can associate with thymoma, and both respond to plasma exchange, IVIG, and rituximab."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Pemphigus vulgaris and lupus are both autoantibody-driven but differ in target: PV's IgG attacks desmoglein at keratinocyte junctions causing flaccid blisters, while SLE's antinuclear antibodies form immune complexes that injure skin, kidney, and joints via complement."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Pemphigus vulgaris and dermatomyositis are autoimmune diseases whose skin findings can flag malignancy: paraneoplastic pemphigus accompanies lymphoma/Castleman, and dermatomyositis is a classic paraneoplastic dermatosis—so new disease prompts a cancer search."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Pemphigus vulgaris reflects failed immune tolerance: regulatory T cells that should suppress desmoglein-reactive B and T cells are deficient, so autoantibodies against keratinocyte adhesion molecules form—restoring Treg control is an experimental therapy."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Pemphigus vulgaris and rheumatoid arthritis are both B-cell-driven autoimmune diseases transformed by rituximab: depleting CD20+ B cells induces durable remission in PV and controls RA—so an anti-B-cell drug links a blistering skin disease to inflammatory arthritis."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Pemphigus vulgaris and type 1 diabetes are both HLA-associated autoimmune diseases with different effectors: PV is antibody-mediated (anti-desmoglein IgG destroying skin adhesion), while T1DM is T-cell-mediated β-cell destruction—two ends of the autoimmune spectrum."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help break tolerance in pemphigus vulgaris: they present desmoglein peptides to autoreactive T cells that drive B cells to make anti-desmoglein IgG, so the antigen-presentation step sits upstream of the antibodies that blister the skin."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "IL-4 steers pemphigus toward pathogenic IgG4 antibodies: this Th2 cytokine drives the class switch to IgG4 anti-desmoglein-3, the dominant blistering autoantibody, so the Th2 axis shapes which antibody isotype mediates the disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Pemphigus vulgaris attacks mucous membranes including the eye: painful erosions typically start in the mouth and can involve conjunctiva and other mucosae before skin blisters appear—so mucosal, not just cutaneous, lesions define and often herald the disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Pemphigus vulgaris is an antibody-mediated autoimmune disease: IgG autoantibodies against desmoglein break the bonds between keratinocytes, so it responds to immunosuppression and B-cell depletion (rituximab)—immunity turned against the body's own cell adhesion."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Pemphigus vulgaris is a blistering disease of the integumentary system: loss of keratinocyte adhesion causes flaccid blisters and painful erosions that shear with pressure (Nikolsky sign), so the skin barrier fails—once fatal before immunosuppressive therapy."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Pemphigus vulgaris often starts in the digestive tract's lining: painful, non-healing oral and esophageal erosions usually precede skin blisters, so mouth ulcers that won't heal can be the first sign—mucosal involvement distinguishing it from pemphigus foliaceus."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Pemphigus vulgaris is strongly HLA-linked: MHC class II alleles such as HLA-DRB1*04:02 present desmoglein peptides to helper T cells, the genetic basis for why certain populations develop the anti-desmoglein autoantibodies that blister skin and mucosa."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Pemphigus is largely complement-independent, unlike pemphigoid: although complement including C5 can be deposited, the IgG autoantibodies blister skin mainly by direct steric and signaling disruption of desmoglein adhesion—a key mechanistic contrast."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 tracks pemphigus activity: this inflammatory cytokine rises in active disease and correlates with severity, part of the cytokine milieu that accompanies autoantibody-driven blistering and a candidate biomarker for monitoring flares."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Pemphigus vulgaris attacks a calcium-dependent glue: desmoglein-3 is a calcium-reliant cadherin that rivets skin cells together, so when autoantibodies block it the cells lose adhesion (acantholysis) and the epidermis blisters apart."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Pemphigus vulgaris is rescued by cortisol's synthetic cousins: once frequently fatal, it is now controlled with corticosteroids that suppress the autoantibody response, usually paired with rituximab to spare long-term steroid harm."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells inflame the pemphigus blister: recruited into lesional skin, they release proteases and mediators that amplify the autoantibody-driven separation, adding an inflammatory push to the loss of cell adhesion."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Pemphigus antibodies trigger keratinocyte signaling through NF-kB: binding desmoglein-3 sets off p38 and NF-kB cascades inside the cell that actively drive the cells apart (acantholysis), so blistering is more than passive unsticking."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "A Th17/IL-17 arm adds to pemphigus inflammation: beyond the Th2 help that drives the autoantibodies, IL-17 amplifies the inflammatory damage in lesional skin, broadening the immune picture and possible drug targets."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "T cells, including cytotoxic subsets, infiltrate the pemphigus blister: autoreactive T-cell help is essential for the anti-desmoglein antibodies, and the T-cell response in lesions is studied as the upstream driver B-cell-depleting therapy aims at."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Widespread pemphigus blisters leak sodium and fluid: losing the skin barrier over large areas lets fluid, sodium, and protein escape, as in a burn, risking dehydration and electrolyte imbalance."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Pemphigus can be paraneoplastic, tied to the thymus: paraneoplastic pemphigus arises with tumors including thymoma—the same gland linked to myasthenia gravis—so an underlying neoplasm is sought in atypical cases."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils mark the IgA pemphigus variant: while classic pemphigus is antibody-and-T-cell driven, the IgA form fills the epidermis with neutrophils, a distinct cellular pattern of pustular blistering."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows pemphigus tearing the skin apart cell by cell: the desmosomes that rivet keratinocytes together dissolve, intercellular gaps widen, and the cells round up and float free — the ultrastructure of acantholysis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Fluorescent light clinches the diagnosis: direct immunofluorescence on a skin biopsy lights up IgG deposited between epidermal cells in a 'fishnet' or chicken-wire pattern, the test that separates pemphigus from other blistering diseases."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Pemphigus may attack more than desmogleins: autoantibodies also target keratinocyte acetylcholine receptors, and since cholinergic signaling helps keep these cells stuck together, blocking it is thought to add to the acantholysis."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "The blister's depth tells the disease apart: pemphigus splits keratinocytes from each other high in the epidermis (acantholysis), sparing the collagen-anchored basement membrane that bullous pemphigoid attacks below — a level that decides the diagnosis."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Controlling pemphigus weakens the bones: the long courses of high-dose corticosteroids that suppress the autoantibodies drive glucocorticoid-induced osteoporosis, so patients need bone protection alongside their immunosuppression."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The real danger in pemphigus is infection: deep immunosuppression with steroids and rituximab opens the door to pneumonia and opportunistic lung infections, which — not the blisters themselves — are the leading cause of death."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Pemphigus is a pure autoantibody disease: IgG against desmoglein-3 unglues keratinocytes directly, direct immunofluorescence shows the 'chicken-wire' intercellular IgG, and the antibody titer tracks activity — which is why removing the B cells that make it cures it."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Denuded skin is an open wound: the raw erosions of pemphigus are readily colonized and invaded by Staphylococcus aureus, the impetiginization and skin sepsis adding to the fluid loss that, before steroids, made the disease so often fatal."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pemphigus is a mucosal disease, and mucosa includes the genitals: painful vulvar, vaginal, and penile erosions cause dyspareunia and scarring, the genital involvement that is easily missed unless the skin disease prompts a careful look."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "Autoreactive B cells live on BAFF: the survival factor keeps alive the clones making anti-desmoglein antibodies, so depleting B cells with rituximab — and targeting the BAFF axis — has become a mainstay that drives lasting remission."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "A lymphoma can hide behind the blisters: paraneoplastic pemphigus, a severe variant, is driven by underlying B-cell cancers like CLL and lymphoma, so resistant or atypical disease warrants a search for an occult lymphoproliferative tumor."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Long steroid courses demand bone protection: the high-dose corticosteroids that control pemphigus drive bone loss, so vitamin D and calcium are given alongside to guard against the steroid-induced osteoporosis that shadows treatment."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "A kinase offers a gentler way to silence the autoimmunity: BTK inhibitors like rilzabrutinib damp the B-cell receptor signaling that fuels the anti-desmoglein antibody response, an emerging steroid-sparing option that spares broad immunosuppression."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The stripped skin becomes a deadly gateway: widespread blistering erosions lose the barrier and weep fluid, so infection and sepsis through the denuded surface — worsened by the immunosuppression used to treat it — are the leading cause of death."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "It rarely comes alone: pemphigus clusters with other autoimmune diseases, especially autoimmune thyroid disease, reflecting the shared genetic susceptibility that lets self-tolerance break down across more than one organ."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory cytokines amplify the blistering: TNF-α rises in pemphigus lesions and serum, adding an inflammatory layer to the antibody-driven loss of keratinocyte adhesion that forms the blisters."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Autoimmunity runs in company: pemphigus is over-represented alongside Sjögren's syndrome and other connective-tissue autoimmune diseases, a co-occurrence reflecting shared loss of self-tolerance."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Severe disease and its steroids clot the veins: hospitalization for extensive pemphigus, systemic inflammation, and high-dose corticosteroids together raise the risk of venous thromboembolism."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The cytokine wiring runs through it: IL-6 and other autoimmune cytokines elevated in pemphigus signal via JAK-STAT3, and JAK inhibitors that blunt this axis are being explored when rituximab and steroids fail."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Heavy immunosuppression opens the lung to it: the rituximab plus high-dose steroids that control severe pemphigus deplete the T-cell defenses against Pneumocystis, so prophylaxis is weighed during prolonged therapy."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Raw mucosa and steroids invite the yeast: painful oral erosions of pemphigus combined with corticosteroid immunosuppression readily superinfect with Candida, complicating the eating difficulty and mouth pain."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Its long steroid courses raise blood sugar: controlling pemphigus often requires months of high-dose corticosteroids, which induce insulin resistance and frequently unmask or precipitate steroid-induced diabetes."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Combined immunosuppression opens the lung to mold: high-dose steroids plus rituximab or other immunosuppressants for refractory pemphigus deeply blunt immunity, occasionally allowing inhaled Aspergillus to invade as pulmonary aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A chronic, painful, disfiguring disease wears on mood: the relentless blistering, eating difficulty and visible erosions of pemphigus, compounded by corticosteroid mood effects, drive substantial depression and impaired quality of life."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its immunosuppression reawakens shingles: the rituximab and high-dose steroids used to control pemphigus deplete B- and T-cell immunity, allowing latent varicella-zoster to reactivate, so antiviral prophylaxis is considered."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Rituximab can resurrect hepatitis B: the B-cell-depleting therapy for refractory pemphigus removes the immune control of latent HBV, risking viral reactivation and hepatitis, so screening before treatment is mandatory."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An unpredictable relapsing disease breeds worry: the flares, painful mucosal erosions and long immunosuppressive treatment of pemphigus foster chronic health anxiety alongside its well-known depression."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its erosions resist healing: the denuded skin and mucosa of pemphigus are chronic open wounds, and the high-dose steroids used to control it further impair their repair and invite infection."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Months of high-dose steroids reshape metabolism: the prolonged corticosteroids needed to control pemphigus cause steroid-induced diabetes, adrenal suppression and a Cushingoid state."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Steroids waste muscle and bone: the chronic high-dose corticosteroids for pemphigus cause proximal steroid myopathy, osteoporosis and avascular necrosis over time."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its blisters spread to the airway: pemphigus erodes the mucosa of the larynx, pharynx and oesophagus causing hoarseness and painful swallowing with aspiration risk, and immunosuppression invites pneumonia."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its long steroid courses strain the circulation: chronic high-dose corticosteroids cause hypertension, fluid retention and accelerated atherosclerosis."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "A paraneoplastic variant flags lymphoma: paraneoplastic pemphigus is associated with underlying lymphoproliferative disorders such as lymphoma and Castleman disease."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids are the backbone of control: high-dose corticosteroids, now with rituximab, suppress the autoantibody attack of pemphigus vulgaris, though their long-term toxicity is substantial."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Immunosuppression reaches the kidney: the long courses of steroids and immunosuppressants for pemphigus vulgaris can be nephrotoxic and demand infection and metabolic monitoring."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Broken skin invites the herpes virus: pemphigus erosions can be superinfected by herpes simplex, worsening blistering and mimicking a disease flare unless recognised and treated."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Immunosuppression beyond steroids: rituximab (anti-CD20) is now first-line with steroids, and cyclophosphamide, azathioprine and mycophenolate are used as steroid-sparing immunosuppressants in pemphigus vulgaris."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "A fellow antibody-mediated autoimmune disease: like CIDP, pemphigus vulgaris is driven by pathogenic autoantibodies and responds to B-cell depletion, IVIG and plasma exchange that remove or block them."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "Antibody and complement attack in common: like neuromyelitis optica, pemphigus vulgaris is an antibody-driven disease where complement and B-cell-derived IgG cause the tissue damage, both treated by rituximab."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Where its autoantibody is born: pemphigus vulgaris arises from autoreactive B cells and plasma cells in germinal centres that secrete anti-desmoglein-3 IgG, which is why rituximab—depleting CD20+ B cells—has become first-line therapy."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Two immune skin diseases, opposite mechanisms: pemphigus vulgaris is an antibody/B-cell-driven blistering disease that splits the epidermis, while psoriasis is a T-cell and IL-17-driven hyperproliferation—autoantibody versus cytokine immunopathology."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "A fellow autoantibody connective-tissue disease: like systemic sclerosis, pemphigus vulgaris is an HLA-associated autoimmune disorder defined by pathogenic autoantibodies, though PV blisters the skin while scleroderma fibroses it."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Mucosal erosions beyond the mouth: pemphigus can erode the oesophageal and other gastrointestinal epithelia—the gut counterpart of desmoglein-joined skin keratinocytes—causing painful erosions and dysphagia."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Paraneoplastic pemphigus and the lung: the paraneoplastic variant attacks respiratory epithelium too, causing a fatal bronchiolitis obliterans that obstructs airflow toward the alveoli."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Paraneoplastic pemphigus: indolent B-cell lymphomas like follicular lymphoma (and CLL and Castleman disease) can trigger paraneoplastic pemphigus, where anti-plakin and anti-desmoglein antibodies blister skin and mucosa."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Another lymphoproliferative trigger: Waldenstrom macroglobulinaemia and other low-grade B-cell neoplasms can underlie paraneoplastic pemphigus, so a new severe pemphigus in an older adult warrants a search for occult lymphoma."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "B-cell depletion across autoimmunity: like ANCA vasculitis, pemphigus vulgaris is an autoantibody-mediated disease for which rituximab (anti-CD20) is now first-line, showcasing B-cell-targeted therapy beyond cancer."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Immunosuppressed and exposed: the rituximab and corticosteroids used to control pemphigus deplete B cells and blunt vaccine responses, leaving patients vulnerable to severe and prolonged COVID-19."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "Adhesion molecule overlap: beyond desmoglein-3, E-cadherin (CDH1) maintains keratinocyte adhesion and is a reported pemphigus autoantigen, widening the loss of cell-cell cohesion that causes blistering."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 contribution: alongside the Th2 response, IFN-γ-producing T cells help drive the autoimmune attack on desmogleins in pemphigus vulgaris."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory amplification: IL-1β and other inflammatory cytokines released in pemphigus lesions amplify keratinocyte injury and blister formation."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Regulatory imbalance: defective IL-10 and regulatory T-cell function in pemphigus vulgaris fails to restrain the autoreactive B cells producing anti-desmoglein antibodies."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: NLRP3-inflammasome activation in pemphigus skin matures IL-1β, amplifying the inflammation that accompanies acantholytic blistering."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Lesional infiltrate: macrophages recruited to pemphigus lesions secrete cytokines and proteases that contribute to the inflammation around the blistering epidermis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "Acantholytic signalling: anti-desmoglein-3 antibody binding triggers Src and EGFR phosphorylation in keratinocytes, the intracellular signalling cascade that drives the cell-cell detachment (acantholysis) of pemphigus blistering."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptolysis: pemphigus autoantibodies activate caspase-3-mediated apoptotic pathways in keratinocytes, the 'apoptolysis' that contributes to cell shrinkage and detachment alongside direct desmosomal disruption."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "T-cell costimulation: autoreactive desmoglein-specific T-helper cells provide the help for autoantibody production in pemphigus, the rationale for CTLA-4-Ig (abatacept) costimulation blockade under study in the disease."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-signalling blockade: the Th2 and Th1 cytokines driving desmoglein autoantibody production signal through JAK-STAT, and JAK inhibitors are being explored in refractory pemphigus to switch off the cytokine circuits sustaining the autoreactive response."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Regulatory-T restoration: pemphigus features a deficit of desmoglein-specific regulatory T cells, and low-dose IL-2 — which preferentially expands Tregs over effector cells — is a tolerance-restoring strategy under investigation in the disease."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Plasma-cell persistence: long-lived autoreactive plasma cells survive on BCL-2 and lack CD20, so they escape rituximab — the basis for the relapses that follow B-cell depletion and the rationale for plasma-cell-directed therapy in pemphigus."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Th2 class-switch: IL-13 partners IL-4 to drive the IgG4-skewed class switch of the desmoglein-3 autoantibodies in pemphigus, so blocking the shared IL-4Rα with dupilumab is being explored to dampen autoantibody production."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Lost tolerance: defective TGF-β-dependent regulatory T-cell control of desmoglein-3-reactive lymphocytes permits the autoreactive T- and B-cell response that fuels autoantibody production in pemphigus vulgaris."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 maintenance: IL-23 sustains the pathogenic Th17 cells whose IL-17A contributes to the inflammatory infiltrate and tissue injury of pemphigus lesions, an axis being assessed for targeted therapy."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Acantholysis signalling: binding of anti-desmoglein-3 IgG triggers intracellular p38-MAPK and ERK signalling in keratinocytes that actively drives the cell-cell detachment of acantholysis, beyond simple steric blockade."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Keratinocyte signalling: Dsg3-antibody binding perturbs PI3K-AKT survival signalling in keratinocytes, contributing to the apoptosis-like 'apoptolysis' that accompanies loss of adhesion in pemphigus."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Th2 skew: IL-5, alongside the IL-4 and IL-13 already mapped, marks the Th2 polarisation that drives the IgG4-skewed anti-desmoglein autoantibody response of pemphigus vulgaris."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 helper drive: IL-12-driven Th1 polarisation (IFN-γ already mapped) contributes to the autoreactive T-cell help underlying anti-desmoglein autoantibody production in pemphigus vulgaris."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate contribution: TLR-MyD88-NF-κB innate signalling (NF-κB already mapped) provides an innate-immune contribution to the inflammatory blistering of pemphigus vulgaris."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Acantholysis signalling: PI3K (PIK3CA)-AKT signalling (AKT already mapped), activated downstream of desmoglein-3 antibody binding, participates in the intracellular signalling that drives keratinocyte acantholysis in pemphigus vulgaris."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "The mTOR-regulated metabolic program supports the autoreactive B-cell and plasmablast expansion producing anti-desmoglein-3 antibodies in pemphigus vulgaris."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates the cutaneous inflammation and immune dysregulation of pemphigus vulgaris."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) modulates the regulatory-T-cell tolerance whose impairment permits the anti-desmoglein autoimmunity of pemphigus vulgaris."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ-STAT1 signalling shapes the Th1 component of the autoimmune response that drives the anti-desmoglein-3 antibody production of pemphigus vulgaris."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA released by acantholytic keratinocyte injury can engage cGAS-STING, amplifying the inflammation of pemphigus vulgaris lesions."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors modulate the keratinocyte survival and apoptosis balance perturbed by the desmoglein-3-directed signalling of pemphigus vulgaris."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the innate inflammation of the pemphigus vulgaris blistering lesion."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β participates in the intracellular signaling downstream of desmoglein-3 antibody binding that promotes acantholysis in pemphigus vulgaris."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic activity by desmoglein-3-specific CD8 T cells contributes to the keratinocyte injury of pemphigus vulgaris."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the keratinocyte stress responses to the desmoglein-3-antibody-induced signaling of pemphigus vulgaris."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of the autoreactive immune responses of pemphigus vulgaris."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2-driven monocyte recruitment contributes to the inflammatory infiltrate of the lesional skin of pemphigus vulgaris."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the autoreactive T- and B-cell metabolism of pemphigus vulgaris."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the dermal inflammation of pemphigus vulgaris."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling, a target of immunosuppressive therapy, participates in the autoreactive T-cell activation of pemphigus vulgaris."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte skin-infiltration and lymphoid interactions of pemphigus vulgaris."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the skin inflammation of pemphigus vulgaris."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon signaling participates in the autoimmune activation of pemphigus vulgaris."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Corticosteroid cornerstone: systemic glucocorticoids remain first-line for pemphigus, acting through the glucocorticoid receptor to suppress the autoreactive T- and B-cell response and cytokine output, the axis underlying rapid disease control before steroid-sparing agents work."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "IgE autoantibody subset: alongside pathogenic IgG, a fraction of pemphigus patients harbour IgE anti-desmoglein antibodies that correlate with disease activity, a rationale for anti-IgE (omalizumab) trials and a mechanism distinct from the dominant IgG4 acantholysis."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Autoimmune clustering: pemphigus vulgaris co-occurs with autoimmune thyroid disease at elevated rates, reflecting the shared tendency to break tolerance, so thyroid-hormone dysfunction is a recognised comorbidity of the pemphigus autoimmune diathesis."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "IgA pemphigus variant: while IgG drives classic pemphigus, a rarer IgA pemphigus targets desmosomal proteins with IgA autoantibodies, and secretory IgA at the oral mucosa is part of the antibody landscape of these blistering diseases."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Erosion pain: the widespread painful oral and skin erosions of pemphigus vulgaris are a major source of suffering, often requiring opioid analgesia acting at the mu-opioid receptor alongside disease-directed immunosuppression."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Pregnancy and neonatal disease: pemphigus can flare in pregnancy, and maternal IgG crossing the placenta (FcRn already mapped) can cause transient neonatal pemphigus, implicating the reproductive-hormone (estrogen) milieu in disease activity."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Erosion inflammation and healing: nitric oxide from the inflamed, eroded skin participates in the local vasodilation and wound-healing response of pemphigus vulgaris lesions, alongside the immune injury driven by the autoantibodies."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Wound-healing angiogenesis: VEGF drives the angiogenesis of the granulation and re-epithelialisation that heals the extensive erosions of pemphigus vulgaris, part of the repair response once immunosuppression controls the autoantibody attack."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative injury: the inflamed, eroded skin of pemphigus vulgaris generates reactive oxygen species, to which xanthine oxidase contributes, and this oxidative stress adds to the tissue damage of the acantholytic blistering."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the inflamed, eroded skin (IL-6, TNF and IL-1 already mapped) amplify the inflammation and pain of the acantholytic blistering of pemphigus vulgaris."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell inflammation: mast cells (already mapped) in the blistering skin release histamine, contributing to the erythema, itch and inflammation that accompany the acantholytic erosions of pemphigus vulgaris."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Wound healing and micronutrient loss: zinc is essential to the re-epithelialisation of the extensive erosions, and the exudative loss and poor intake of severe pemphigus can deplete zinc, impairing the wound healing of the skin."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia and blood loss: the blood and exudate loss through the extensive erosions and the poor intake from the painful oral disease cause the anaemia and iron deficiency that accompany severe pemphigus vulgaris."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Electrolyte loss: the extensive denuded erosions of severe pemphigus lose fluid, protein and electrolytes like a burn, depleting potassium (sodium already mapped) and disturbing the fluid-electrolyte balance."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium depletion: the transcutaneous loss through the widespread erosions and the poor intake of severe pemphigus deplete magnesium, part of the burn-like fluid and electrolyte (sodium and potassium already mapped) disturbance."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Steroid metabolic adipokine: leptin is disturbed by the long-term corticosteroid (cortisol already mapped) therapy of pemphigus, part of the steroid metabolic complications of the disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the steroid-related metabolic disturbance of pemphigus vulgaris."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the steroid-related metabolic disturbance and the inflammation (IL-6 already mapped) of pemphigus."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "ADCC effectors: the NK cells mediate the antibody-dependent cellular cytotoxicity of the anti-CD20 (already mapped) rituximab (Ritux 3) against the autoreactive B cells of pemphigus vulgaris."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Pruritus cytokine: IL-31, part of the type-2 (IL-4 and IL-13 already mapped) response, mediates the pruritus of the cutaneous involvement of pemphigus vulgaris."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial alarmin: the keratinocyte-derived TSLP alarmin drives the type-2 (IL-4 already mapped) skin immunity of the blistering autoimmunity of pemphigus vulgaris."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Type-2 dermatosis overlap: pemphigus vulgaris shares the type-2 (IL-4, IL-13, IL-31 and TSLP already mapped) skin-immune dimension with atopic dermatitis, and the dupilumab is explored in the refractory disease."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "Type-2 itch overlap: the type-2 (IL-31 and TSLP already mapped) neuroimmune itch links the cutaneous pruritus of pemphigus vulgaris to prurigo nodularis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Type-2 remodelling: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines, is part of the type-2 tissue-remodelling dimension of the cutaneous involvement of pemphigus vulgaris."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the complement-mediated inflammation at the site of the acantholytic blisters of pemphigus vulgaris."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Autoimmune micronutrient: selenium, a selenoprotein antioxidant cofactor, is part of the micronutrient dimension (with vitamin D and zinc already mapped) of the autoimmune susceptibility of pemphigus vulgaris."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Neurogenic inflammation: substance P, from the cutaneous sensory nerves, contributes to the neurogenic inflammation and the itch/pain of the mucocutaneous lesions of pemphigus vulgaris."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) activated on the anti-desmoglein-3 (already mapped) immune complexes at the keratinocyte surface in pemphigus vulgaris."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-desmoglein-3 IgG (immunoglobulin already mapped) at the desmosome in pemphigus vulgaris."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Erosion iron: transferrin, the iron carrier, reflects the disordered iron handling of the anaemia of the chronic mucocutaneous erosions and the systemic inflammation of pemphigus vulgaris."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Blister-fluid kinin: bradykinin accumulates in the blister fluid of pemphigus vulgaris, amplifying the painful mucosal oedema and pain at desmosome-disrupted erosions where the kallikrein-kinin system is activated by local proteases."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erosion-related anaemia: the chronic cutaneous and mucosal protein loss of extensive pemphigus vulgaris drives a normocytic anaemia; erythropoietin supports erythropoiesis in patients requiring prolonged immunosuppressive therapy."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Autoimmune amplifier: hyperprolactinaemia can exacerbate autoimmune bullous diseases including pemphigus vulgaris by promoting B-cell survival and autoantibody production, a recognised neuro-endocrine–immune axis in organ-specific autoimmunity."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian autoimmune modulator: melatonin modulates T-helper-cell (already mapped) and B-cell (already mapped) activity, influencing IgG autoantibody production against desmoglein-3 in pemphigus vulgaris, with nocturnal flare patterns reported."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Neuroendocrine skin-immune axis: oxytocin modulates the stress-immune axis and keratinocyte (skin already mapped) integrity; psychosocial stress is a recognised pemphigus-vulgaris trigger, implicating the hypothalamic–skin neuroendocrine pathway."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone immune modulation: testosterone exerts an immunosuppressive effect on the Th2-skewed (IL-4, IL-13 already mapped) autoimmune response of pemphigus vulgaris, consistent with the female sex predominance of this bullous disease."
---

# Pemphigus Vulgaris

## Overview

**Pemphigus vulgaris (PV)** is a potentially life-threatening **autoimmune intraepidermal blistering disease** characterized by IgG autoantibodies directed against **desmoglein-3 (Dsg3)** — a transmembrane cadherin essential for keratinocyte-keratinocyte adhesion in stratified squamous epithelia [^amagai-2006-dsg-compensation]. The autoantibodies disrupt desmosomal adhesion → **acantholysis** (loss of cell-cell adhesion within the epithelium) → formation of **flaccid blisters and erosions** that preferentially involve mucous membranes and skin.

Pemphigus belongs to the **pemphigus group of autoimmune bullous diseases** (AIBD), distinct from the **pemphigoid group** (which is subepidermal — targeting basement membrane proteins):

| Pemphigus type | Autoantigen | Blister plane | Dominant feature |
|:---------------|:------------|:--------------|:-----------------|
| **Pemphigus vulgaris** | Dsg3 (± Dsg1) | Suprabasal, intraepidermal | Mucosal erosions ± cutaneous blisters |
| **Pemphigus foliaceus** | Dsg1 only | Subcorneal, superficial | Superficial cutaneous blisters; no mucosae |
| **Paraneoplastic pemphigus (PNP)** | Dsg3, Dsg1, desmoplakin, envoplakin, periplakin + others | Variable | Associated with B-cell neoplasms; severe bronchiolitis obliterans |
| **Drug-induced pemphigus** | Dsg3 and/or Dsg1 | Variable | Triggered by thiol drugs (penicillamine, captopril) |
| **IgA pemphigus** | Desmocollin 1 | Intraepidermal | Vesicles/pustules; unusual |

**Epidemiology:**
- Incidence: 1–5 per million per year in Europe; higher in Mediterranean, Jewish, and South Asian populations (HLA-DRB1 association)
- Peak onset: 40–60 years; slight female predominance; can occur at any age
- **Pre-treatment mortality:** ~75% (from sepsis and iatrogenic complications of high-dose corticosteroids); now <5% with modern management

## Structure

### Immunopathogenesis

**Stage 1 — Loss of B cell tolerance to Dsg3:**
- Thymic presentation of Dsg3 peptides (Dsg3 is expressed in thymic epithelium) normally induces central tolerance; genetic susceptibility (HLA-DRB1*04:02, HLA-DQB1*05:03 in Caucasians; HLA-DRB1*14:01 in Japanese/Korean) → Dsg3-reactive T cells escape negative selection
- Environmental trigger? (thiol drugs, UV, viral epitope mimicry) may break peripheral tolerance in susceptible individuals

**Stage 2 — Dsg3-reactive CD4+ T cells provide help for B cells:**
- Dsg3-specific Th2 cells and Tfh cells drive germinal center reactions → affinity maturation → high-affinity IgG4 anti-Dsg3 antibodies
- IgG4 is characteristically produced in chronic antigen exposure with Th2 cytokines (IL-4, IL-13) → the dominant PV antibody subclass
- Anti-Dsg3 IgG1 also present (complement-activating) → contributes to blister formation via MAC

**Stage 3 — Acantholysis mechanisms:**

1. **Steric hindrance:** Anti-Dsg3 IgG4 binds EC1/EC2 domains → blocks Dsg3 trans-dimer formation between adjacent keratinocytes → desmosome disassembly → acantholysis
2. **Signaling cascade:** Anti-Dsg3 IgG crosslinking → EGFR/ErbB2 transactivation → PLC-γ → PKC → p38 MAPK → phosphorylation of desmoplakin → desmosome internalization; separately, Src kinase → plakophilin phosphorylation
3. **Protease activation:** Anti-Dsg3 IgG → tPA/plasminogen → plasmin → Dsg3 ectodomain cleavage; serine protease inhibitors (aprotinin) block blister formation in mouse models

**Stage 4 — Blister formation:**
- Suprabasal acantholysis: loss of Dsg3-mediated adhesion in the suprabasal layer while basal cells remain attached to the basement membrane (basal cells are Dsg1-dominant; no anti-Dsg1 in mucosal PV) → "row of tombstones" on histology
- Fluid accumulates in the intraepidermal space → **flaccid blister** (thin roof → easily ruptures → painful erosions)
- **Nikolsky sign:** Lateral pressure on perilesional skin → skin slides/detaches = positive (presence of intraepidermal acantholysis)

### HLA and genetic susceptibility

- **HLA-DRB1*04:02** and **DQB1*05:03**: Major risk alleles in Caucasian and Ashkenazi Jewish populations; DRB1*04:02 is the primary susceptibility gene (OR ~15)
- **HLA-DRB1*14:01**: Dominant susceptibility allele in Japanese/Korean populations
- HLA susceptibility reflects antigen presentation of Dsg3 peptides to autoreactive CD4+ T helper cells

## Function

### Clinical presentations

**Mucosal pemphigus vulgaris (Dsg3 only; ~50%):**
- Oral erosions are the presenting feature in >80% of PV; painful, irregular erosions on buccal mucosa, palate, gingiva; severe impairment of eating, speaking; often misdiagnosed as aphthous stomatitis for months
- Laryngeal/pharyngeal involvement → hoarseness, dysphagia
- Esophageal involvement → odynophagia, esophageal stricture (rare)
- Conjunctival, nasal, genital, and anal mucosae also affected
- Skin spared (unless Dsg1 antibodies develop)

**Mucocutaneous pemphigus vulgaris (Dsg3+Dsg1; ~50%):**
- Oral erosions + cutaneous flaccid blisters on face, scalp, trunk, intertriginous areas
- Blisters rupture easily → extensive painful erosions → risk of infection, fluid loss
- Nikolsky sign positive
- Scalp involvement → alopecia (typically non-scarring)

**Pemphigus foliaceus (PF; Dsg1 only):**
- Superficial blistering → crusted erosions (honey-crusted) on seborrheic distribution (face, scalp, chest, upper back); NO mucous membrane involvement
- Fogo Selvagem (endemic PF in Brazil): triggered by insect bites; anti-Dsg1 IgG cross-reactive with sand fly salivary antigen

**Complications:**
- Bacterial superinfection (Staph aureus most common; risk of bacteremia/sepsis)
- Fluid/electrolyte imbalance in extensive disease
- Malnutrition (inability to eat)
- Corticosteroid adverse effects (Cushingoid features, diabetes, osteoporosis, infections)

### Diagnosis

**Clinical:**
- Flaccid blisters and erosions; positive Nikolsky sign; mucosal involvement (in PV)
- Exclude: bullous pemphigoid (tense blisters, elderly, basement membrane zone), Stevens-Johnson, mucous membrane pemphigoid

**Histopathology (punch biopsy of fresh blister edge):**
- Suprabasal acantholysis with "tombstone" appearance of basal cells
- Eosinophilic spongiosis may be present early
- No subepidermal split (distinguishes from pemphigoid)

**Direct immunofluorescence (DIF) — perilesional skin biopsy:**
- **Intercellular IgG and C3 deposition** in a "chicken-wire/net" pattern throughout the epidermis
- DIF is the gold standard; positive in >95% of active disease

**Indirect immunofluorescence (IDIF) — monkey esophagus substrate:**
- Circulating anti-epithelial antibodies → esophageal epithelial staining
- Positive in most PV; titer correlates with disease activity

**ELISA (anti-Dsg3 and anti-Dsg1):**
- Anti-Dsg3 ELISA (≥7 U/mL): sensitive and specific for PV; titers correlate with mucosal disease activity
- Anti-Dsg1 ELISA (≥7 U/mL): correlates with skin involvement
- Serial monitoring guides treatment response and relapse prediction

**Tzanck smear:** Acantholytic cells (Tzanck cells) in blister fluid — rapid but non-specific

## Pathology

### Treatment

**Corticosteroids (historical backbone, increasingly replaced):**
- Prednisone 0.5–1.5 mg/kg/day for disease control; taper slowly
- **Current approach:** Short-course + rituximab (see below) — reduces cumulative steroid exposure
- Adverse effects of high-dose, long-term steroids remain a major driver of morbidity and mortality

**Rituximab (Rituxan; anti-CD20 mAb; Roche/Genentech):**
- **Ritux 3 / PEMPHIX Phase 3** (N=90; France; rituximab + 3-week prednisone vs. prednisone alone × 18 months): Complete remission (CR) at month 24: **90% vs. 28%** (p<0.0001); anti-Dsg3 titer reduction faster and more sustained [^joly-2017-rituximab-pemphix]
- FDA approved **June 2018** for moderate-to-severe PV — first FDA approval for pemphigus
- Dosing: 1000 mg IV at weeks 0 and 2 (induction); 500 mg at months 6 and 12 (maintenance)
- Mechanism: Depletes CD20+ B cells → reduces Dsg3-reactive B cell precursors → anti-Dsg3 IgG4 titer falls; long-lived plasma cells may persist → some patients relapse
- PML (progressive multifocal leukoencephalopathy) risk (rare); HBV reactivation screening required

**Efgartigimod alfa + hyaluronidase (Vyvgart Hytrulo; SC form; Argenx):**
- **ADHERE-SC Phase 3** (N=214; efgartigimod SC 1000 mg Q1W × 4-cycle blocks vs. placebo): CR off systemic therapy at cycle 4: **58% vs. 23%** (p<0.001); anti-Dsg3 titer reduction >70% [^murrell-2021-efgartigimod-adhere]
- FDA approved **October 2023** for PV/PF
- Mechanism: FcRn blockade → accelerated catabolism of all IgG subclasses including anti-Dsg3 IgG4 → rapid disease control (faster onset than rituximab)
- Does NOT cause B-cell depletion — IgG and disease can return after stopping → combined with rituximab or continued as maintenance in clinical practice
- Does not increase infection risk as dramatically as B-cell depletion

**Batoclimab (IMVT-1402; Immunovant; anti-FcRn):**
- Phase 3 trials ongoing in PV; high-affinity anti-FcRn; SC dosing

**Immunosuppressive adjuncts:**
- **Azathioprine (AZA):** TPMT/NUDT15 genotyping required; reduces steroid dose; modest efficacy
- **Mycophenolate mofetil (MMF):** Better tolerated than AZA; reduces steroid dose; less evidence vs. rituximab
- **Dapsone:** For mild disease or adjunct; anti-inflammatory; screen G6PD deficiency
- **IVIG (2 g/kg):** Rapid effect via Fc receptor blockade and anti-idiotypic antibody dilution; used for acute severe flares while awaiting rituximab onset; not curative
- **Plasmapheresis:** Removes circulating anti-Dsg3 IgG; combined with immunosuppression; rapid but transient effect; mainly for life-threatening disease

**JAAD/EDF (European Dermatology Forum) guidelines (2020):**
- First-line: Rituximab + short-term prednisone (based on Ritux 3)
- For mild disease: Prednisone + AZA or MMF
- Efgartigimod for acute flares and patients with contraindications to rituximab
- Disease activity monitoring: Dsg3/Dsg1 ELISA + clinical assessment (PDAI or BPDAI score)

## Connections

- `connects-to` → **[Desmoglein-3](../../03-molecular/desmoglein-3/README.md)** — Anti-Dsg3 IgG4 is the pathogenic autoantibody; steric hindrance of Dsg3 trans-adhesion + signaling (p38 MAPK, EGFR) → suprabasal acantholysis; Dsg3 ELISA titer tracks disease activity; anti-Dsg3+Dsg1 → mucocutaneous PV; Dsg3 compensation explains mucosal-only vs. cutaneous involvement.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Anti-Dsg3 IgG4 (steric hindrance) and IgG1 (complement) are the pathogenic subclasses; IgG4 titer correlates with disease activity; FcRn recycles anti-Dsg3 IgG → prolonged blister induction; IVIG can dilute pathogenic antibodies acutely; anti-Dsg3 IgG4 falls after rituximab → remission.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab (anti-CD20; Ritux 3: 90% vs. 28% CR at 24 months; FDA Jun 2018) depletes Dsg3-reactive B cells → sustained remission; 500 mg maintenance dosing at months 6 and 12 reduces relapse; now the standard first-line biologic replacing long-term high-dose corticosteroids in moderate-severe PV.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — FcRn recycles anti-Dsg3 IgG4 prolonging pathogenic antibody half-life; efgartigimod (anti-FcRn; ADHERE-SC: 58% vs. 23% CR; FDA Oct 2023) accelerates IgG4 catabolism → rapid disease control without B-cell depletion; SC efgartigimod approved for PV/PF; batoclimab Phase 3 ongoing.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Dsg3-reactive IgG4-secreting B cells produce pathogenic anti-Dsg3 antibody; rituximab depletes CD20+ B cells → anti-Dsg3 IgG4 falls → remission; memory B cells are the relapse reservoir; anti-Dsg3 titer guides retreatment; plasma cells (CD20−) escape rituximab → residual disease.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Anti-Dsg3 IgG crosslinking → EGFR/ErbB2 transactivation → PLC-γ → p38 MAPK → desmoplakin phosphorylation → desmosome internalization; EGFR amplifies acantholysis beyond Dsg3 steric blockade; erlotinib reduced blistering in mice; p38 MAPK inhibitors in PV clinical trials.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Anti-Dsg3 IgG1 (complement-fixing) activates complement → C3 deposition on keratinocytes; MAC (C5b-9) amplifies keratinocyte injury; DIF shows IgG + C3 in intercellular pattern; C5a → neutrophil elastase → Dsg3 cleavage; complement amplifies acantholysis beyond IgG4 blockade.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Pemphigus vulgaris blisters skin and mucosa: anti-desmoglein-3 antibodies break apart keratinocyte desmosomes (acantholysis), producing flaccid intraepidermal bullae that rupture into painful erosions, a positive Nikolsky sign, and near-universal oral involvement.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Long-lived plasma cells are pemphigus's treatment-resistant reservoir: they secrete anti-Dsg3 IgG4 but, lacking CD20, escape rituximab — so anti-CD20 depletes B-cell precursors yet residual plasma cells sustain antibody, motivating plasma-cell-directed (anti-CD38) approaches.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Pemphigus is T-cell-dependent: Dsg3-specific CD4+ helper T cells (HLA-DR*04:02-restricted) drive B cells to class-switch into pathogenic anti-Dsg3 IgG4 — so the autoantibody response depends on a T-B collaboration that tolerogenic therapies aim to break.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — Pemphigus and myasthenia gravis are paradigm IgG autoantibody diseases against a cell-surface protein: anti-desmoglein-3 in PV versus anti-acetylcholine-receptor in MG, both can associate with thymoma, and both respond to plasma exchange, IVIG, and rituximab.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Pemphigus vulgaris and lupus are both autoantibody-driven but differ in target: PV's IgG attacks desmoglein at keratinocyte junctions causing flaccid blisters, while SLE's antinuclear antibodies form immune complexes that injure skin, kidney, and joints via complement.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — Pemphigus vulgaris and dermatomyositis are autoimmune diseases whose skin findings can flag malignancy: paraneoplastic pemphigus accompanies lymphoma/Castleman, and dermatomyositis is a classic paraneoplastic dermatosis—so new disease prompts a cancer search.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Pemphigus vulgaris reflects failed immune tolerance: regulatory T cells that should suppress desmoglein-reactive B and T cells are deficient, so autoantibodies against keratinocyte adhesion molecules form—restoring Treg control is an experimental therapy.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Pemphigus vulgaris and rheumatoid arthritis are both B-cell-driven autoimmune diseases transformed by rituximab: depleting CD20+ B cells induces durable remission in PV and controls RA—so an anti-B-cell drug links a blistering skin disease to inflammatory arthritis.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Pemphigus vulgaris and type 1 diabetes are both HLA-associated autoimmune diseases with different effectors: PV is antibody-mediated (anti-desmoglein IgG destroying skin adhesion), while T1DM is T-cell-mediated β-cell destruction—two ends of the autoimmune spectrum.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help break tolerance in pemphigus vulgaris: they present desmoglein peptides to autoreactive T cells that drive B cells to make anti-desmoglein IgG, so the antigen-presentation step sits upstream of the antibodies that blister the skin.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — IL-4 steers pemphigus toward pathogenic IgG4 antibodies: this Th2 cytokine drives the class switch to IgG4 anti-desmoglein-3, the dominant blistering autoantibody, so the Th2 axis shapes which antibody isotype mediates the disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Pemphigus vulgaris attacks mucous membranes including the eye: painful erosions typically start in the mouth and can involve conjunctiva and other mucosae before skin blisters appear—so mucosal, not just cutaneous, lesions define and often herald the disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Pemphigus vulgaris is an antibody-mediated autoimmune disease: IgG autoantibodies against desmoglein break the bonds between keratinocytes, so it responds to immunosuppression and B-cell depletion (rituximab)—immunity turned against the body's own cell adhesion.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Pemphigus vulgaris is a blistering disease of the integumentary system: loss of keratinocyte adhesion causes flaccid blisters and painful erosions that shear with pressure (Nikolsky sign), so the skin barrier fails—once fatal before immunosuppressive therapy.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Pemphigus vulgaris often starts in the digestive tract's lining: painful, non-healing oral and esophageal erosions usually precede skin blisters, so mouth ulcers that won't heal can be the first sign—mucosal involvement distinguishing it from pemphigus foliaceus.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Pemphigus vulgaris is strongly HLA-linked: MHC class II alleles such as HLA-DRB1*04:02 present desmoglein peptides to helper T cells, the genetic basis for why certain populations develop the anti-desmoglein autoantibodies that blister skin and mucosa.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Pemphigus is largely complement-independent, unlike pemphigoid: although complement including C5 can be deposited, the IgG autoantibodies blister skin mainly by direct steric and signaling disruption of desmoglein adhesion—a key mechanistic contrast.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 tracks pemphigus activity: this inflammatory cytokine rises in active disease and correlates with severity, part of the cytokine milieu that accompanies autoantibody-driven blistering and a candidate biomarker for monitoring flares.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Pemphigus vulgaris attacks a calcium-dependent glue: desmoglein-3 is a calcium-reliant cadherin that rivets skin cells together, so when autoantibodies block it the cells lose adhesion (acantholysis) and the epidermis blisters apart.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Pemphigus vulgaris is rescued by cortisol's synthetic cousins: once frequently fatal, it is now controlled with corticosteroids that suppress the autoantibody response, usually paired with rituximab to spare long-term steroid harm.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells inflame the pemphigus blister: recruited into lesional skin, they release proteases and mediators that amplify the autoantibody-driven separation, adding an inflammatory push to the loss of cell adhesion.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Pemphigus antibodies trigger keratinocyte signaling through NF-kB: binding desmoglein-3 sets off p38 and NF-kB cascades inside the cell that actively drive the cells apart (acantholysis), so blistering is more than passive unsticking.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — A Th17/IL-17 arm adds to pemphigus inflammation: beyond the Th2 help that drives the autoantibodies, IL-17 amplifies the inflammatory damage in lesional skin, broadening the immune picture and possible drug targets.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — T cells, including cytotoxic subsets, infiltrate the pemphigus blister: autoreactive T-cell help is essential for the anti-desmoglein antibodies, and the T-cell response in lesions is studied as the upstream driver B-cell-depleting therapy aims at.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Widespread pemphigus blisters leak sodium and fluid: losing the skin barrier over large areas lets fluid, sodium, and protein escape, as in a burn, risking dehydration and electrolyte imbalance.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Pemphigus can be paraneoplastic, tied to the thymus: paraneoplastic pemphigus arises with tumors including thymoma—the same gland linked to myasthenia gravis—so an underlying neoplasm is sought in atypical cases.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils mark the IgA pemphigus variant: while classic pemphigus is antibody-and-T-cell driven, the IgA form fills the epidermis with neutrophils, a distinct cellular pattern of pustular blistering.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows pemphigus tearing the skin apart cell by cell: the desmosomes that rivet keratinocytes together dissolve, intercellular gaps widen, and the cells round up and float free — the ultrastructure of acantholysis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Fluorescent light clinches the diagnosis: direct immunofluorescence on a skin biopsy lights up IgG deposited between epidermal cells in a 'fishnet' or chicken-wire pattern, the test that separates pemphigus from other blistering diseases.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Pemphigus may attack more than desmogleins: autoantibodies also target keratinocyte acetylcholine receptors, and since cholinergic signaling helps keep these cells stuck together, blocking it is thought to add to the acantholysis.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — The blister's depth tells the disease apart: pemphigus splits keratinocytes from each other high in the epidermis (acantholysis), sparing the collagen-anchored basement membrane that bullous pemphigoid attacks below — a level that decides the diagnosis.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Controlling pemphigus weakens the bones: the long courses of high-dose corticosteroids that suppress the autoantibodies drive glucocorticoid-induced osteoporosis, so patients need bone protection alongside their immunosuppression.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The real danger in pemphigus is infection: deep immunosuppression with steroids and rituximab opens the door to pneumonia and opportunistic lung infections, which — not the blisters themselves — are the leading cause of death.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Pemphigus is a pure autoantibody disease: IgG against desmoglein-3 unglues keratinocytes directly, direct immunofluorescence shows the 'chicken-wire' intercellular IgG, and the antibody titer tracks activity — which is why removing the B cells that make it cures it.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Denuded skin is an open wound: the raw erosions of pemphigus are readily colonized and invaded by Staphylococcus aureus, the impetiginization and skin sepsis adding to the fluid loss that, before steroids, made the disease so often fatal.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pemphigus is a mucosal disease, and mucosa includes the genitals: painful vulvar, vaginal, and penile erosions cause dyspareunia and scarring, the genital involvement that is easily missed unless the skin disease prompts a careful look.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — Autoreactive B cells live on BAFF: the survival factor keeps alive the clones making anti-desmoglein antibodies, so depleting B cells with rituximab — and targeting the BAFF axis — has become a mainstay that drives lasting remission.
- `connects-to` → **[CLL](../cll/README.md)** — A lymphoma can hide behind the blisters: paraneoplastic pemphigus, a severe variant, is driven by underlying B-cell cancers like CLL and lymphoma, so resistant or atypical disease warrants a search for an occult lymphoproliferative tumor.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Long steroid courses demand bone protection: the high-dose corticosteroids that control pemphigus drive bone loss, so vitamin D and calcium are given alongside to guard against the steroid-induced osteoporosis that shadows treatment.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — A kinase offers a gentler way to silence the autoimmunity: BTK inhibitors like rilzabrutinib damp the B-cell receptor signaling that fuels the anti-desmoglein antibody response, an emerging steroid-sparing option that spares broad immunosuppression.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The stripped skin becomes a deadly gateway: widespread blistering erosions lose the barrier and weep fluid, so infection and sepsis through the denuded surface — worsened by the immunosuppression used to treat it — are the leading cause of death.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — It rarely comes alone: pemphigus clusters with other autoimmune diseases, especially autoimmune thyroid disease, reflecting the shared genetic susceptibility that lets self-tolerance break down across more than one organ.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Inflammatory cytokines amplify the blistering: TNF-α rises in pemphigus lesions and serum, adding an inflammatory layer to the antibody-driven loss of keratinocyte adhesion that forms the blisters.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Autoimmunity runs in company: pemphigus is over-represented alongside Sjögren's syndrome and other connective-tissue autoimmune diseases, a co-occurrence reflecting shared loss of self-tolerance.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Severe disease and its steroids clot the veins: hospitalization for extensive pemphigus, systemic inflammation, and high-dose corticosteroids together raise the risk of venous thromboembolism.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The cytokine wiring runs through it: IL-6 and other autoimmune cytokines elevated in pemphigus signal via JAK-STAT3, and JAK inhibitors that blunt this axis are being explored when rituximab and steroids fail.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Heavy immunosuppression opens the lung to it: the rituximab plus high-dose steroids that control severe pemphigus deplete the T-cell defenses against Pneumocystis, so prophylaxis is weighed during prolonged therapy.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Raw mucosa and steroids invite the yeast: painful oral erosions of pemphigus combined with corticosteroid immunosuppression readily superinfect with Candida, complicating the eating difficulty and mouth pain.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Its long steroid courses raise blood sugar: controlling pemphigus often requires months of high-dose corticosteroids, which induce insulin resistance and frequently unmask or precipitate steroid-induced diabetes.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Combined immunosuppression opens the lung to mold: high-dose steroids plus rituximab or other immunosuppressants for refractory pemphigus deeply blunt immunity, occasionally allowing inhaled Aspergillus to invade as pulmonary aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A chronic, painful, disfiguring disease wears on mood: the relentless blistering, eating difficulty and visible erosions of pemphigus, compounded by corticosteroid mood effects, drive substantial depression and impaired quality of life.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its immunosuppression reawakens shingles: the rituximab and high-dose steroids used to control pemphigus deplete B- and T-cell immunity, allowing latent varicella-zoster to reactivate, so antiviral prophylaxis is considered.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Rituximab can resurrect hepatitis B: the B-cell-depleting therapy for refractory pemphigus removes the immune control of latent HBV, risking viral reactivation and hepatitis, so screening before treatment is mandatory.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An unpredictable relapsing disease breeds worry: the flares, painful mucosal erosions and long immunosuppressive treatment of pemphigus foster chronic health anxiety alongside its well-known depression.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its erosions resist healing: the denuded skin and mucosa of pemphigus are chronic open wounds, and the high-dose steroids used to control it further impair their repair and invite infection.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Months of high-dose steroids reshape metabolism: the prolonged corticosteroids needed to control pemphigus cause steroid-induced diabetes, adrenal suppression and a Cushingoid state.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Steroids waste muscle and bone: the chronic high-dose corticosteroids for pemphigus cause proximal steroid myopathy, osteoporosis and avascular necrosis over time.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its blisters spread to the airway: pemphigus erodes the mucosa of the larynx, pharynx and oesophagus causing hoarseness and painful swallowing with aspiration risk, and immunosuppression invites pneumonia.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its long steroid courses strain the circulation: chronic high-dose corticosteroids cause hypertension, fluid retention and accelerated atherosclerosis.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — A paraneoplastic variant flags lymphoma: paraneoplastic pemphigus is associated with underlying lymphoproliferative disorders such as lymphoma and Castleman disease.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids are the backbone of control: high-dose corticosteroids, now with rituximab, suppress the autoantibody attack of pemphigus vulgaris, though their long-term toxicity is substantial.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Immunosuppression reaches the kidney: the long courses of steroids and immunosuppressants for pemphigus vulgaris can be nephrotoxic and demand infection and metabolic monitoring.
- `connects-to` → **[Herpesvirus](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Broken skin invites the herpes virus: pemphigus erosions can be superinfected by herpes simplex, worsening blistering and mimicking a disease flare unless recognised and treated.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Immunosuppression beyond steroids: rituximab (anti-CD20) is now first-line with steroids, and cyclophosphamide, azathioprine and mycophenolate are used as steroid-sparing immunosuppressants in pemphigus vulgaris.
- `connects-to` → **[CIDP](../cidp/README.md)** — A fellow antibody-mediated autoimmune disease: like CIDP, pemphigus vulgaris is driven by pathogenic autoantibodies and responds to B-cell depletion, IVIG and plasma exchange that remove or block them.
- `connects-to` → **[NMO](../nmo/README.md)** — Antibody and complement attack in common: like neuromyelitis optica, pemphigus vulgaris is an antibody-driven disease where complement and B-cell-derived IgG cause the tissue damage, both treated by rituximab.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Where its autoantibody is born: pemphigus vulgaris arises from autoreactive B cells and plasma cells in germinal centres that secrete anti-desmoglein-3 IgG, which is why rituximab—depleting CD20+ B cells—has become first-line therapy.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Two immune skin diseases, opposite mechanisms: pemphigus vulgaris is an antibody/B-cell-driven blistering disease that splits the epidermis, while psoriasis is a T-cell and IL-17-driven hyperproliferation—autoantibody versus cytokine immunopathology.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — A fellow autoantibody connective-tissue disease: like systemic sclerosis, pemphigus vulgaris is an HLA-associated autoimmune disorder defined by pathogenic autoantibodies, though PV blisters the skin while scleroderma fibroses it.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Mucosal erosions beyond the mouth: pemphigus can erode the oesophageal and other gastrointestinal epithelia—the gut counterpart of desmoglein-joined skin keratinocytes—causing painful erosions and dysphagia.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Paraneoplastic pemphigus and the lung: the paraneoplastic variant attacks respiratory epithelium too, causing a fatal bronchiolitis obliterans that obstructs airflow toward the alveoli.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Paraneoplastic pemphigus: indolent B-cell lymphomas like follicular lymphoma (and CLL and Castleman disease) can trigger paraneoplastic pemphigus, where anti-plakin and anti-desmoglein antibodies blister skin and mucosa.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Another lymphoproliferative trigger: Waldenstrom macroglobulinaemia and other low-grade B-cell neoplasms can underlie paraneoplastic pemphigus, so a new severe pemphigus in an older adult warrants a search for occult lymphoma.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — B-cell depletion across autoimmunity: like ANCA vasculitis, pemphigus vulgaris is an autoantibody-mediated disease for which rituximab (anti-CD20) is now first-line, showcasing B-cell-targeted therapy beyond cancer.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Immunosuppressed and exposed: the rituximab and corticosteroids used to control pemphigus deplete B cells and blunt vaccine responses, leaving patients vulnerable to severe and prolonged COVID-19.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Adhesion molecule overlap: beyond desmoglein-3, E-cadherin (CDH1) maintains keratinocyte adhesion and is a reported pemphigus autoantigen, widening the loss of cell-cell cohesion that causes blistering.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 contribution: alongside the Th2 response, IFN-γ-producing T cells help drive the autoimmune attack on desmogleins in pemphigus vulgaris.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory amplification: IL-1β and other inflammatory cytokines released in pemphigus lesions amplify keratinocyte injury and blister formation.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Regulatory imbalance: defective IL-10 and regulatory T-cell function in pemphigus vulgaris fails to restrain the autoreactive B cells producing anti-desmoglein antibodies.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: NLRP3-inflammasome activation in pemphigus skin matures IL-1β, amplifying the inflammation that accompanies acantholytic blistering.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Lesional infiltrate: macrophages recruited to pemphigus lesions secrete cytokines and proteases that contribute to the inflammation around the blistering epidermis.
- `connects-to` → **[Src kinase](../../03-molecular/src-kinase/README.md)** — Anti-desmoglein-3 antibody binding triggers Src and EGFR phosphorylation in keratinocytes, the intracellular signaling cascade that drives the cell-cell detachment (acantholysis) of pemphigus blistering beyond simple steric disruption of desmosomes.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Pemphigus autoantibodies activate caspase-3-mediated apoptotic pathways in keratinocytes—the "apoptolysis" that contributes to cell shrinkage and detachment alongside the direct desmosomal disruption that produces the suprabasal split.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Autoreactive desmoglein-specific T-helper cells provide the help that licenses autoantibody production in pemphigus, the rationale for CTLA-4-Ig (abatacept) costimulation blockade being explored to switch off the autoreactive response.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The Th2 and Th1 cytokines driving desmoglein autoantibody production signal through JAK-STAT, and JAK inhibitors are being explored in refractory pemphigus to switch off the cytokine circuits sustaining the autoreactive response.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Pemphigus features a deficit of desmoglein-specific regulatory T cells, and low-dose IL-2—which preferentially expands Tregs over effector cells—is a tolerance-restoring strategy under investigation in the disease.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Long-lived autoreactive plasma cells survive on BCL-2 and lack CD20, so they escape rituximab—the basis for the relapses that follow B-cell depletion and the rationale for plasma-cell-directed therapy in pemphigus.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — IL-13 partners IL-4 to drive the IgG4-skewed class switch of the desmoglein-3 autoantibodies in pemphigus, so blocking the shared IL-4Rα with dupilumab is being explored to dampen autoantibody production.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Defective TGF-β-dependent regulatory T-cell control of desmoglein-3-reactive lymphocytes permits the autoreactive T- and B-cell response that fuels autoantibody production in pemphigus vulgaris.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains the pathogenic Th17 cells whose IL-17A contributes to the inflammatory infiltrate and tissue injury of pemphigus lesions, an axis being assessed for targeted therapy.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Binding of anti-desmoglein-3 IgG triggers intracellular p38-MAPK and ERK signaling in keratinocytes that actively drives the cell-cell detachment of acantholysis, beyond simple steric blockade.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Dsg3-antibody binding perturbs PI3K-AKT survival signaling in keratinocytes, contributing to the apoptosis-like "apoptolysis" that accompanies loss of adhesion in pemphigus.
- `connects-to` → **[Interleukin-5](../../03-molecular/il-5/README.md)** — IL-5, alongside the IL-4 and IL-13 already mapped, marks the Th2 polarization that drives the IgG4-skewed anti-desmoglein autoantibody response of pemphigus vulgaris.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12-driven Th1 polarization (IFN-γ already mapped) contributes to the autoreactive T-cell help underlying anti-desmoglein autoantibody production in pemphigus vulgaris.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (NF-κB already mapped) provides an innate-immune contribution to the inflammatory blistering of pemphigus vulgaris.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped), activated downstream of desmoglein-3 antibody binding, participates in the intracellular signaling that drives keratinocyte acantholysis in pemphigus vulgaris.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The mTOR-regulated metabolic program supports the autoreactive B-cell and plasmablast expansion producing anti-desmoglein-3 antibodies in pemphigus vulgaris.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates the cutaneous inflammation and immune dysregulation of pemphigus vulgaris.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) modulates the regulatory-T-cell tolerance whose impairment permits the anti-desmoglein autoimmunity of pemphigus vulgaris.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ-STAT1 signaling shapes the Th1 component of the autoimmune response that drives the anti-desmoglein-3 antibody production of pemphigus vulgaris.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA released by acantholytic keratinocyte injury can engage cGAS-STING, amplifying the inflammation of pemphigus vulgaris lesions.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors modulate the keratinocyte survival and apoptosis balance perturbed by the desmoglein-3-directed signaling of pemphigus vulgaris.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the innate inflammation of the pemphigus vulgaris blistering lesion.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β participates in the intracellular signaling downstream of desmoglein-3 antibody binding that promotes acantholysis in pemphigus vulgaris.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic activity by desmoglein-3-specific CD8 T cells contributes to the keratinocyte injury of pemphigus vulgaris.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the keratinocyte stress responses to the desmoglein-3-antibody-induced signaling of pemphigus vulgaris.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of the autoreactive immune responses of pemphigus vulgaris.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2-driven monocyte recruitment contributes to the inflammatory infiltrate of the lesional skin of pemphigus vulgaris.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the autoreactive T- and B-cell metabolism of pemphigus vulgaris.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the dermal inflammation of pemphigus vulgaris.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling, a target of immunosuppressive therapy, participates in the autoreactive T-cell activation of pemphigus vulgaris.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte skin-infiltration and lymphoid interactions of pemphigus vulgaris.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the skin inflammation of pemphigus vulgaris.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon signaling participates in the autoimmune activation of pemphigus vulgaris.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Corticosteroid cornerstone: systemic glucocorticoids remain first-line for pemphigus, acting through the glucocorticoid receptor to suppress the autoreactive T- and B-cell response and cytokine output, the axis underlying rapid disease control before steroid-sparing agents work.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — IgE autoantibody subset: alongside pathogenic IgG, a fraction of pemphigus patients harbour IgE anti-desmoglein antibodies that correlate with disease activity, a rationale for anti-IgE (omalizumab) trials and a mechanism distinct from the dominant IgG4 acantholysis.
- `connects-to` → **[Thyroid hormones](../../03-molecular/thyroid-hormones/README.md)** — Autoimmune clustering: pemphigus vulgaris co-occurs with autoimmune thyroid disease at elevated rates, reflecting the shared tendency to break tolerance, so thyroid-hormone dysfunction is a recognised comorbidity of the pemphigus autoimmune diathesis.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — IgA pemphigus variant: while IgG drives classic pemphigus, a rarer IgA pemphigus targets desmosomal proteins with IgA autoantibodies, and secretory IgA at the oral mucosa is part of the antibody landscape of these blistering diseases.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Erosion pain: the widespread painful oral and skin erosions of pemphigus vulgaris are a major source of suffering, often requiring opioid analgesia acting at the mu-opioid receptor alongside disease-directed immunosuppression.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Pregnancy and neonatal disease: pemphigus can flare in pregnancy, and maternal IgG crossing the placenta (FcRn already mapped) can cause transient neonatal pemphigus, implicating the reproductive-hormone (estrogen) milieu in disease activity.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Erosion inflammation and healing: nitric oxide from the inflamed, eroded skin participates in the local vasodilation and wound-healing response of pemphigus vulgaris lesions, alongside the immune injury driven by the autoantibodies.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Wound-healing angiogenesis: VEGF drives the angiogenesis of the granulation and re-epithelialisation that heals the extensive erosions of pemphigus vulgaris, part of the repair response once immunosuppression controls the autoantibody attack.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative injury: the inflamed, eroded skin of pemphigus vulgaris generates reactive oxygen species, to which xanthine oxidase contributes, and this oxidative stress adds to the tissue damage of the acantholytic blistering.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the inflamed, eroded skin (IL-6, TNF and IL-1 already mapped) amplify the inflammation and pain of the acantholytic blistering of pemphigus vulgaris.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell inflammation: mast cells (already mapped) in the blistering skin release histamine, contributing to the erythema, itch and inflammation that accompany the acantholytic erosions of pemphigus vulgaris.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Wound healing and micronutrient loss: zinc is essential to the re-epithelialisation of the extensive erosions, and the exudative loss and poor intake of severe pemphigus can deplete zinc, impairing the wound healing of the skin.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia and blood loss: the blood and exudate loss through the extensive erosions and the poor intake from the painful oral disease cause the anaemia and iron deficiency that accompany severe pemphigus vulgaris.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Electrolyte loss: the extensive denuded erosions of severe pemphigus lose fluid, protein and electrolytes like a burn, depleting potassium (sodium already mapped) and disturbing the fluid-electrolyte balance.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium depletion: the transcutaneous loss through the widespread erosions and the poor intake of severe pemphigus deplete magnesium, part of the burn-like fluid and electrolyte (sodium and potassium already mapped) disturbance.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Steroid metabolic adipokine: leptin is disturbed by the long-term corticosteroid (cortisol already mapped) therapy of pemphigus, part of the steroid metabolic complications of the disease.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the steroid-related metabolic disturbance of pemphigus vulgaris.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the steroid-related metabolic disturbance and the inflammation (IL-6 already mapped) of pemphigus.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — ADCC effectors: the NK cells mediate the antibody-dependent cellular cytotoxicity of the anti-CD20 (already mapped) rituximab (Ritux 3) against the autoreactive B cells of pemphigus vulgaris.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Pruritus cytokine: IL-31, part of the type-2 (IL-4 and IL-13 already mapped) response, mediates the pruritus of the cutaneous involvement of pemphigus vulgaris.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial alarmin: the keratinocyte-derived TSLP alarmin drives the type-2 (IL-4 already mapped) skin immunity of the blistering autoimmunity of pemphigus vulgaris.
- `connects-to` → **[Atopic dermatitis](../atopic-dermatitis/README.md)** — Type-2 dermatosis overlap: pemphigus vulgaris shares the type-2 (IL-4, IL-13, IL-31 and TSLP already mapped) skin-immune dimension with atopic dermatitis, and the dupilumab is explored in the refractory disease.
- `connects-to` → **[Prurigo nodularis](../prurigo-nodularis/README.md)** — Type-2 itch overlap: the type-2 (IL-31 and TSLP already mapped) neuroimmune itch links the cutaneous pruritus of pemphigus vulgaris to prurigo nodularis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Type-2 remodelling: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines, is part of the type-2 tissue-remodelling dimension of the cutaneous involvement of pemphigus vulgaris.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the complement-mediated inflammation at the site of the acantholytic blisters of pemphigus vulgaris.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Autoimmune micronutrient: selenium, a selenoprotein antioxidant cofactor, is part of the micronutrient dimension (with vitamin D and zinc already mapped) of the autoimmune susceptibility of pemphigus vulgaris.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Neurogenic inflammation: substance P, from the cutaneous sensory nerves, contributes to the neurogenic inflammation and the itch/pain of the mucocutaneous lesions of pemphigus vulgaris.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) activated on the anti-desmoglein-3 (already mapped) immune complexes at the keratinocyte surface in pemphigus vulgaris.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-desmoglein-3 IgG (immunoglobulin already mapped) at the desmosome in pemphigus vulgaris.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Erosion iron: transferrin, the iron carrier, reflects the disordered iron handling of the anaemia of the chronic mucocutaneous erosions and the systemic inflammation of pemphigus vulgaris.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Blister-fluid kinin: bradykinin accumulates in the blister fluid of pemphigus vulgaris, amplifying the painful mucosal oedema and pain at desmosome-disrupted erosions where the kallikrein-kinin system is activated by local proteases.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erosion-related anaemia: the chronic cutaneous and mucosal protein loss of extensive pemphigus vulgaris drives a normocytic anaemia; erythropoietin supports erythropoiesis in patients requiring prolonged immunosuppressive therapy.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Autoimmune amplifier: hyperprolactinaemia can exacerbate autoimmune bullous diseases including pemphigus vulgaris by promoting B-cell survival and autoantibody production, a recognised neuro-endocrine–immune axis in organ-specific autoimmunity.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian autoimmune modulator: melatonin modulates T-helper-cell (already mapped) and B-cell (already mapped) activity, influencing IgG autoantibody production against desmoglein-3 in pemphigus vulgaris, with nocturnal flare patterns reported.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Neuroendocrine skin-immune axis: oxytocin modulates the stress-immune axis and keratinocyte (skin already mapped) integrity; psychosocial stress is a recognised pemphigus-vulgaris trigger, implicating the hypothalamic–skin neuroendocrine pathway.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex-hormone immune modulation: testosterone exerts an immunosuppressive effect on the Th2-skewed (IL-4, IL-13 already mapped) autoimmune response of pemphigus vulgaris, consistent with the female sex predominance of this bullous disease.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^joly-2017-rituximab-pemphix]: Joly P, Maho-Vaillant M, Prost-Squarcioni C, et al. First-line rituximab combined with short-term prednisone versus prednisone alone for the treatment of pemphigus (Ritux 3): a prospective, multicentre, parallel-group, open-label randomised trial. *Lancet.* 2017;389(10083):2031-2040. [doi:10.1016/S0140-6736(17)30070-3](https://doi.org/10.1016/S0140-6736(17)30070-3) · [PubMed 28342637](https://pubmed.ncbi.nlm.nih.gov/28342637/)
[^murrell-2021-efgartigimod-adhere]: Murrell DF, Sprecher E, Maho-Vaillant M, et al. Efgartigimod alfa and hyaluronidase-qvfc in pemphigus vulgaris. *N Engl J Med.* 2024;390(5):419-430. [doi:10.1056/NEJMoa2302492](https://doi.org/10.1056/NEJMoa2302492) · [PubMed 38294978](https://pubmed.ncbi.nlm.nih.gov/38294978/)
[^amagai-2006-dsg-compensation]: Amagai M, Tsunoda K, Zillikens D, Nagai T, Nishikawa T. The clinical phenotype of pemphigus is defined by the anti-desmoglein autoantibody profile. *J Am Acad Dermatol.* 1999;40(2 Pt 1):167-170. [doi:10.1016/S0190-9622(99)70183-0](https://doi.org/10.1016/S0190-9622(99)70183-0) · [PubMed 10025737](https://pubmed.ncbi.nlm.nih.gov/10025737/)
