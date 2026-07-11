---
schema: human-scale-entry/v1
id: wound-healing
name: Wound Healing
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Wound healing: hemostasis → inflammation → proliferation (granulation + re-epithelialization) → remodeling. PDGF, TGF-β, VEGF, FN, and EGF orchestrate each phase. Chronic wounds arise from impaired M1→M2 switch; diabetic ulcers are the leading cause of non-traumatic amputation."
aliases: ["wound repair", "cutaneous wound healing", "tissue repair", "skin healing", "chronic wound", "diabetic wound"]
sources:
  - id: singer-1999-wound-healing-review
    type: peer-reviewed
    cite: "Singer AJ, Clark RA. Cutaneous wound healing. N Engl J Med. 1999;341(10):738-746."
    doi: "10.1056/NEJM199909023411006"
    pmid: "10471461"
    url: "https://doi.org/10.1056/NEJM199909023411006"
  - id: gurtner-2008-wound-repair-regeneration
    type: peer-reviewed
    cite: "Gurtner GC, Werner S, Barrandon Y, Longaker MT. Wound repair and regeneration. Nature. 2008;453(7193):314-321."
    doi: "10.1038/nature07039"
    pmid: "18480812"
    url: "https://doi.org/10.1038/nature07039"
  - id: eming-2014-wound-repair-mechanisms
    type: peer-reviewed
    cite: "Eming SA, Martin P, Tomic-Canic M. Wound repair and regeneration: mechanisms, signaling, and translation. Sci Transl Med. 2014;6(265):265sr6."
    doi: "10.1126/scitranslmed.3009337"
    pmid: "25473038"
    url: "https://doi.org/10.1126/scitranslmed.3009337"
cross_links:
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Plasma FN is cross-linked into fibrin clots → provisional scaffold for platelets, neutrophils, and fibroblasts; cellular FN from fibroblasts drives granulation tissue; FN-integrin α5β1 → fibroblast migration and myofibroblast differentiation → wound contraction and closure."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 from platelets and macrophages drives myofibroblast differentiation (α-SMA+ → wound contraction), collagen I synthesis, and re-epithelialization; excess TGF-β → hypertrophic scar and keloid; TGF-β3 promotes scarless fetal healing; pirfenidone inhibits fibrogenic signaling."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-A from keratinocytes and macrophages drives angiogenesis into the wound bed; HIF-1α (hypoxic wound center) → VEGF → new vessel formation in granulation tissue; anti-VEGF therapy impairs wound healing — a known adverse effect of bevacizumab and other anti-VEGF agents."
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Diabetes impairs wound healing through AGE accumulation, pericyte dysfunction, impaired neutrophil function, and reduced HIF-1α/VEGF response; diabetic foot ulcers affect ~15% of people with diabetes and are the leading cause of non-traumatic amputation."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages orchestrate wound healing's inflammatory-to-proliferative switch: M1 cells clear debris, then become M2 cells that secrete TGF-β1, PDGF, VEGF, and IGF-1 to drive fibroblasts, angiogenesis, and re-epithelialization; a failed M1→M2 switch defines chronic wounds."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Wound fibroblasts migrate along the fibronectin scaffold and lay down the type III collagen of granulation tissue; TGF-β1 plus tension converts them into α-SMA+ myofibroblasts that contract the wound and, failing to apoptose, produce hypertrophic scars and keloids."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Cutaneous repair is the canonical wound-healing model — hemostasis, inflammation, proliferation, remodeling — restoring the skin barrier with a fibrotic scar rather than regeneration; chronic non-healing ulcers (diabetic, venous, pressure) carry a ~$31 billion annual US burden."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets fire the starting gun of wound healing: at injury they form the hemostatic plug and degranulate, releasing PDGF, TGF-β, and VEGF that recruit neutrophils and macrophages and prime fibroblasts — the growth-factor surge launching the inflammatory phase."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Collagen is the structural endpoint of wound healing: fibroblasts first lay down weak type III collagen in granulation tissue, which remodeling replaces with cross-linked type I collagen regaining ~80% of tensile strength over months; dysregulated turnover yields keloids."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Systemic sclerosis is wound healing that never stops: the TGF-β-driven myofibroblast activation and collagen deposition that should close a wound and resolve becomes self-sustaining and widespread, scarring skin and organs — fibrosis is dysregulated persistent repair."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes is the leading cause of chronic non-healing wounds: hyperglycemia impairs every healing phase—blunting neutrophil and macrophage function, stiffening capillaries, adding neuropathy—so diabetic foot ulcers stall and drive most non-traumatic amputations."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Angiogenesis by endothelial cells is essential to wound healing: VEGF from the wound bed drives endothelial sprouting that forms granulation tissue's capillaries, restoring oxygen—when this fails (ischemia, diabetes), the wound cannot progress to repair."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Wound healing is the integumentary system restoring its barrier: hemostasis, inflammation, proliferation, and remodeling rebuild epidermis and dermis after injury, but imperfectly—scar replaces the original architecture, lacking hair follicles and full strength."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils lead the inflammatory phase of wound healing: arriving within hours, they kill bacteria and clear debris, but their proteases also damage tissue—so timely resolution is essential, and persistent neutrophilia underlies chronic non-healing wounds."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGF is a master growth factor of wound repair: released by degranulating platelets, it recruits and activates fibroblasts and smooth muscle, driving granulation tissue and collagen deposition—and recombinant PDGF (becaplermin) treats diabetic foot ulcers."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity impairs wound healing: poor tissue perfusion, chronic low-grade inflammation, and frequent coexisting diabetes slow each phase of repair, so obese and diabetic patients suffer more wound dehiscence, infection and chronic ulcers—a major surgical burden."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Wound healing tips into fibrosis when it overshoots: the same fibroblast and TGF-beta program that repairs a wound, if unresolved, lays down excess collagen as hypertrophic scars, keloids or organ fibrosis—so pathological fibrosis is wound healing that never stops."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Oxygen is rate-limiting for wound healing: collagen synthesis and the bacteria-killing oxidative burst both need it, so hypoxic, poorly perfused wounds (diabetes, vascular disease) heal slowly—why perfusion and hyperbaric oxygen matter for chronic wounds."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells regulate the wound's transition from inflammation to repair: their cytokines orchestrate macrophage switching and fibroblast activity, so the adaptive immune balance shapes whether a wound heals cleanly or scars—or fails to close in chronic wounds."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Intact peripheral nerves are needed for wounds to heal: sensory loss removes the protective reflexes that prevent repeat injury and the neuropeptides that aid repair, so diabetic neuropathy turns minor foot wounds into chronic, non-healing ulcers."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Wound closure depends on contractile cells: fibroblasts differentiate into smooth-muscle-like myofibroblasts that pull wound edges together and lay down matrix, so this contraction shrinks the defect—but if unchecked it drives contractures and excess scarring."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells help orchestrate early wound healing: degranulating to release histamine, heparin, and growth factors, they boost vascular permeability and recruit inflammatory cells—useful for repair, yet their excess is implicated in hypertrophic scars and keloids."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Wound healing begins with thrombin building the clot: it converts fibrinogen to fibrin, forming the provisional matrix that stops bleeding and scaffolds incoming cells, while also activating platelets—launching the cascade toward repair."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Wound hypoxia drives repair through HIF-1alpha: the low-oxygen wound bed stabilizes HIF-1alpha, which switches on VEGF and other genes to sprout vessels and recruit cells—so impaired HIF signaling (as in diabetes) helps explain chronic non-healing wounds."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc is an essential cofactor for wound healing: it supports the metalloproteinases, DNA synthesis and immune cells that rebuild tissue, so zinc deficiency slows healing—one reason nutritional status shapes how wounds close."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Wound healing needs copper to knit collagen: the enzyme lysyl oxidase uses copper to cross-link collagen into strong scar, and copper also spurs new vessels, so copper deficiency leaves wounds weak and slow to close."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol sabotages wound healing: glucocorticoids suppress the inflammatory cleanup, blunt fibroblast collagen synthesis, and slow re-epithelialization, so steroid use is a classic cause of dehiscence and chronic non-healing wounds."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells steer wounds from inflammation to repair: Tregs accumulate in healing skin and damp down the inflammatory phase while promoting tissue regeneration, helping resolve the wound rather than scar it excessively."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 runs the inflammatory phase of wound healing: released early by immune cells, it recruits neutrophils and macrophages and switches on repair programs, so balanced IL-6 is needed—too little stalls healing, too much scars."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Healing isn't just skin-deep—the gut must heal too: surgical anastomoses and mucosal ulcers in the large intestine knit back together by the same phases, and failure of this internal repair causes leaks, a feared surgical complication."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help orchestrate the healing wound: sampling the injured tissue, they bridge innate and adaptive immunity and release signals that guide the shift from inflammation to repair, tuning how cleanly a wound closes."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Light is harnessed to heal: photobiomodulation with low-level laser or LED photons, and UV light for infected wounds, are used to coax stubborn chronic wounds toward closure, the optics of skin shaping how deep the photons reach."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver underwrites wound repair from afar: it makes the clotting factors that seal the wound and the proteins healing demands, so liver failure brings coagulopathy and slow, poor healing."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron is built into the chemistry of repair: it is a cofactor for the prolyl hydroxylases that mature collagen, so iron deficiency and poor oxygen delivery leave a wound unable to lay down strong scar."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy watches a wound pull itself shut: fibroblasts transform into myofibroblasts studded with actin stress fibers that contract the edges together, while newly secreted collagen fibrils assemble into the banded scaffold of scar."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium signals the wound from the first second: it is the ion that fires the clotting cascade to stop bleeding, then sets up the gradient that drives keratinocytes to migrate and differentiate as they resurface the skin."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D arms the healing skin: it spurs keratinocytes to make cathelicidin, the antimicrobial peptide that guards a fresh wound from infection, so deficiency leaves repair slower and more prone to breaking down."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Healing runs on protein: building new collagen and tissue demands amino acids, so the low albumin of malnutrition signals a body that cannot keep up — slowing repair and, through low oncotic pressure, swelling the wound with edema."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Repair is hungry for oxygen the red cells carry: collagen cross-linking and the respiratory burst that kills bacteria both need it, so anemia or poor perfusion starves the wound bed and stalls healing."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide orchestrates the repair: released by endothelium and macrophages, it dilates vessels to feed the wound, spurs angiogenesis and collagen deposition, and kills microbes — and its deficiency is one reason diabetic wounds heal so poorly."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "New vessels must be built and then stabilized: in the proliferative phase angiopoietins work with VEGF to sprout and mature the capillaries that feed granulation tissue, the blood supply without which a wound cannot fill in."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Infection is the great stall: Staphylococcus aureus colonizes wounds and builds biofilms that lock healing in a chronic inflammatory phase, the prime reason surgical and chronic wounds fail to close."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A wound is a doorway to the bloodstream: when local infection breaches the granulation barrier, bacteria and their toxins spill into the circulation, and wound sepsis turns a local repair problem into a life-threatening systemic one."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen speeds repair: it boosts collagen deposition and dampens the excessive inflammation that stalls healing, which is why wounds close more slowly after menopause and topical estrogen has been tried to accelerate them."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Fat cells join the repair crew: dermal adipocytes and adipose-derived stem cells help recruit fibroblasts and rebuild the wound bed, while the dysfunctional adipose of obesity instead impairs healing."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Failing kidneys slow every wound: the uremia, anemia, and poor perfusion of chronic kidney disease blunt the inflammatory and proliferative phases, making non-healing wounds and ulcers a common, stubborn problem in these patients."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammation that won't switch off stalls repair: TNF-α drives the early inflammatory phase, but its persistence — as in diabetic and chronic wounds — keeps the wound stuck in inflammation, degrading matrix and blocking the move to proliferation and closure."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "The first responders open the vessels: histamine released by mast cells at the injury dilates capillaries and raises their permeability, letting plasma, clotting factors and immune cells flood in to begin the healing cascade."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "A kinin both inflames and rebuilds: bradykinin generated at the wound widens vessels and signals pain, but also stimulates the fibroblast proliferation and angiogenesis that drive the repair, linking the inflammatory and rebuilding phases."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 drives the skin to close: downstream of IL-6 and growth factors, STAT3 signaling pushes keratinocyte migration and proliferation across the wound bed, so its loss markedly slows re-epithelialization."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB runs the inflammatory phase: activated in immune cells and keratinocytes at the injury, it switches on the cytokines and antimicrobial defenses that clear debris and pathogens before the rebuilding phase can begin."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The same clotting that seals wounds can misfire: the surgery and immobility that accompany major wound repair, layered on the body's natural post-injury hypercoagulable state, raise the risk of deep-vein thrombosis."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "It colonizes wounds that won't close: Candida joins bacteria in the biofilms of chronic non-healing ulcers, and its presence sustains the inflammatory, proteolytic environment that keeps a wound stuck in the inflammatory phase."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Starved of blood, tissue cannot rebuild: peripheral arterial disease from atherosclerosis cuts oxygen and nutrient delivery to a wound bed, a leading cause of ischemic, non-healing lower-limb ulcers and amputation."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Low oxygen-carrying capacity stalls repair: anemia of chronic disease reduces the oxygen reaching the wound bed needed for collagen cross-linking and the respiratory burst, slowing closure in chronically ill patients."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Its drugs impair the healing it needs after surgery: corticosteroids, methotrexate and biologics used in rheumatoid arthritis blunt inflammation and collagen synthesis, raising the rate of wound dehiscence and infection after operations."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Bone repair is wound healing of the skeleton: fracture union recapitulates the same inflammatory, proliferative and remodeling phases, so the impaired healing of aging and chronic disease also delays the union of osteoporotic fractures."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Mind and wound feed back on each other: the cortisol and inflammation of depression measurably slow wound closure, while chronic non-healing wounds, pain and disability in turn drive depression."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Immune cells orchestrate repair: neutrophils and macrophages clear debris and release the growth factors that drive proliferation, so immunodeficiency, neutropenia and immunosuppressive drugs all delay healing."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Lymphatic drainage is needed to close a wound: the lymphatics clear interstitial fluid and inflammatory debris from the wound bed, so lymphedema leaves a swollen, stagnant field where chronic ulcers fail to heal."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "A breached barrier invites invasive strep: an open wound is a portal for Streptococcus pyogenes, which causes wound cellulitis, erysipelas and, at its worst, rapidly spreading necrotising fasciitis."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Nerves help wounds close: sensory neuropeptides like substance P drive the inflammatory and angiogenic phases, so denervation and diabetic or pressure-related neuropathy produce chronic, slow-healing ulcers."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones tune repair: glucocorticoid excess from Cushing's or steroids blunts inflammation and collagen synthesis, while thyroid hormone, growth hormone and sex steroids each modulate the speed and strength of healing."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The same cascade rebuilds bone and tendon: fracture and tendon repair follow the inflammation-proliferation-remodelling sequence of wound healing, so the conditions that impair skin healing also delay bony union."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Repair depends on blood supply: healing requires perfusion and an angiogenic phase, so ischaemia from peripheral arterial disease and poor perfusion produce chronic, non-healing wounds."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Oxygen drives collagen synthesis: adequate tissue oxygenation is essential for repair, so hypoxia and the vasoconstriction of smoking markedly impair wound healing."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hormones and life-stage shape healing: oestrogen promotes wound repair so healing slows after menopause, while fetal wounds heal scarlessly — a model for regenerative repair."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Nutrition and the gut underpin repair: protein, energy and the gut's absorptive function fuel healing, and anastomotic wounds in the bowel must heal against constant mechanical and bacterial stress."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Uraemia stalls healing: chronic kidney disease impairs wound repair through uraemic toxins, anaemia and poor nutrition, a major reason dialysis-access and surgical wounds heal poorly."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Zinc is essential to repair: it is a cofactor for the enzymes of collagen synthesis and cell proliferation, so zinc deficiency markedly delays wound healing."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "They stall repair: glucocorticoids suppress the inflammatory phase, fibroblast proliferation and collagen synthesis of healing, thinning skin and causing wound dehiscence — why chronic steroid users heal slowly after surgery and injury."
  - target: 02-pathogen/02-bacteria/clostridium-tetani
    relation: connects-to
    note: "Wounds are its gateway: Clostridium tetani spores enter through deep, dirty puncture wounds and germinate in the low-oxygen necrotic tissue, releasing tetanospasmin — making tetanus immunisation status a routine part of wound assessment."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "It delays surgical healing: cytotoxic chemotherapy blunts the proliferating fibroblasts and immune cells of repair, and anti-angiogenic agents like bevacizumab impair new vessel growth, so operations are timed around treatment to avoid dehiscence."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Fracture repair is wound healing of bone: a broken bone runs the same haemostasis-inflammation-proliferation-remodelling cascade, replacing the haematoma with a cartilaginous then bony callus instead of a fibrous scar."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Diabetes cripples repair: hyperglycaemia in type 1 (as in type 2) diabetes impairs every phase of wound healing—poor angiogenesis, dysfunctional neutrophils and neuropathy—producing the chronic diabetic foot ulcers that are a leading cause of amputation."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "The heart heals by scarring: after a myocardial infarction the dead myocardium is replaced by a collagen scar through the same fibroblast-driven repair as skin, since adult cardiomyocytes cannot regenerate."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Mucosal healing as the goal: in inflammatory bowel disease, achieving wound healing of the ulcerated gut lining—'mucosal healing'—is the modern treatment endpoint that predicts durable remission and fewer complications."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Tumours as wounds that never heal: cancers like pancreatic adenocarcinoma hijack the wound-healing programme—angiogenesis, fibroblast activation and immune suppression—to build their desmoplastic stroma, Dvorak's classic insight."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Aberrant repair scars the lung: pulmonary fibrosis is dysregulated wound healing in the alveolus, where repeated injury drives fibroblast-myofibroblast scarring instead of restoring the thin gas-exchange surface."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Granulation needs new vessels: wound healing depends on VEGF-driven angiogenesis to build the capillary-rich granulation tissue, and poor arterial perfusion as in peripheral artery disease stalls repair into chronic non-healing wounds."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The regeneration paradigm: the liver is the body's premier regenerating organ, and the same wound-healing programmes that restore the hepatic lobule after injury, when chronic, lay down the scar of cirrhosis."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Growth-factor drive: FGF signalling through FGFR spurs the keratinocyte proliferation, angiogenesis and fibroblast activation of wound repair, one of the core pathways re-epithelialising and rebuilding injured tissue."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Re-epithelialisation: EGF signalling through EGFR drives the keratinocyte proliferation and migration that resurface a wound, the phase whose failure leaves a chronic ulcer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory phase: IL-1β orchestrates the early inflammatory response to injury, but its persistence in chronic wounds stalls them in a non-healing inflammatory state."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Proliferative repair: IGF-1 stimulates fibroblast proliferation, collagen synthesis and granulation tissue, and its deficiency contributes to impaired healing in diabetes and ageing."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 draws monocytes into the wound, where they mature into the macrophages that clear debris and orchestrate the transition from inflammation to repair."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Resolution phase: IL-10 dampens the inflammatory phase and promotes scarless, regenerative healing, and its deficiency biases wounds toward excessive scarring."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Re-epithelialisation: Wnt/β-catenin signalling drives the keratinocyte proliferation and migration that resurface the wound and regenerate skin appendages."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory phase: prostaglandins produced at the wound drive the vasodilation, increased permeability and pain of the early inflammatory phase, which is why NSAIDs that block them can blunt the inflammation needed for normal healing."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Matricellular remodelling: periostin secreted by activated fibroblasts organises collagen cross-linking and myofibroblast differentiation in the proliferative and remodelling phases, supporting wound contraction and matrix maturation."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Neurogenic healing: sensory-nerve-derived substance P promotes the angiogenesis and inflammatory cell recruitment of healing, and its loss in denervated or diabetic skin is a key reason those wounds heal poorly."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Reparative macrophages: IL-4 polarises wound macrophages to the M2 phenotype that resolves inflammation and drives the proliferative phase, secreting growth factors for fibroblasts and angiogenesis — the switch from clearing debris to rebuilding tissue."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Diabetic non-healing: advanced glycation end-products signalling through RAGE sustains a chronic inflammatory, pro-oxidant state in diabetic skin that stalls wounds in the inflammatory phase, a central reason diabetic foot ulcers fail to heal."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Neutrophil amplification: S100A8/A9 (calprotectin) released by the neutrophils of the early wound amplifies inflammation, and its persistence marks the stalled, neutrophil-dominated inflammatory phase of chronic non-healing wounds."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Re-epithelialisation: HGF acting through the MET receptor drives the keratinocyte migration and proliferation that resurface a wound, together with endothelial responses supporting granulation-tissue angiogenesis."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Gap-junction remodelling: connexin-43 is downregulated at the wound edge to permit keratinocyte and fibroblast migration, and its abnormal persistence in chronic and diabetic wounds impairs closure, making Cx43 a wound-healing target."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Progenitor recruitment: CXCL12 (SDF-1) recruits bone-marrow-derived endothelial and mesenchymal progenitor cells into the wound to support angiogenesis and granulation, an axis blunted in diabetic non-healing wounds."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Proliferative phase: EGF, PDGF and FGF (all mapped) drive the MAPK-ERK cascade that powers the keratinocyte re-epithelialisation and fibroblast proliferation of the wound's proliferative phase."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival and migration: PI3K-AKT signalling downstream of the wound growth factors promotes the cell survival, migration and angiogenesis that build granulation tissue."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Remodeling and scar: TGF-β signals through SMAD4 (TGF-β mapped) to drive fibroblast-to-myofibroblast transition and the collagen deposition (collagen mapped) of the remodeling phase, and its excess produces fibrotic scarring."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Injury sensing: TLR4 sensing of damage-associated molecular patterns released by tissue injury initiates the inflammatory phase of wound healing (with NF-κB already mapped)."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Proliferative phase: mTOR-driven protein synthesis and cell growth power the proliferative phase of wound healing, supporting keratinocyte migration, fibroblast proliferation and granulation-tissue formation."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Redox-balanced repair: NRF2-regulated redox balance governs the reactive-oxygen-species signalling that drives wound healing while limiting the oxidative damage that impairs chronic-wound closure."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes macrophage activation, re-epithelialisation and the fibrotic phase of tissue repair in wound healing."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the inflammatory phase of wound healing and the macrophage polarisation balance that governs resolution versus chronic non-healing."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA released by damaged cells engages cGAS-STING to drive the early inflammatory signalling that initiates wound healing."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate keratinocyte migration, oxidative-stress handling, and TGF-β output during repair; their dysregulation underlies chronic non-healing diabetic wounds."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2-STAT signaling downstream of inflammatory cytokines (IL-6 already mapped) coordinates the inflammatory-to-proliferative transition of wound healing."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the keratinocyte and fibroblast migration and proliferation of the proliferative phase of wound healing."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the Wnt/β-catenin and metabolic signaling that governs keratinocyte migration and fibroblast activation during wound healing."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling drives the keratinocyte migration and focal-adhesion turnover of re-epithelialization in wound healing."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D-driven proliferation of keratinocytes and fibroblasts sustains the proliferative phase of wound healing."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling regulates the energy state and metabolic transitions of the cells across the phases of wound healing."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the keratinocyte, fibroblast, and immune-cell responses across the phases of wound healing."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the re-epithelialization and angiogenesis of the proliferative phase of wound healing."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte and macrophage recruitment participates in the inflammatory phase of wound healing."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the macrophage and fibroblast phenotype transitions of wound healing."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Fibrinogen and the fibrin clot provide the provisional matrix of the hemostasis phase that initiates wound healing."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory and tissue-repair phases of wound healing."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory phase and antimicrobial defense of wound healing."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the cellular reprogramming during wound healing."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic control of repair: insulin signalling promotes keratinocyte migration and collagen synthesis, and its impairment in diabetes is a leading cause of chronic non-healing wounds, the rationale for glucose control and even topical insulin."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Hemostasis and contraction: platelet-released serotonin drives the early vasoconstriction of hemostasis and later stimulates fibroblast proliferation and wound contraction, linking the platelet plug to the remodeling phase of repair."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammatory phase: the NLRP3 inflammasome matures IL-1beta (already mapped) during the inflammatory phase of healing, and its persistent activation sustains the chronic inflammation that stalls diabetic and pressure-ulcer wounds."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Resolution of inflammation: omega-3 fatty acids are converted to specialised pro-resolving mediators (resolvins, protectins) that actively terminate the inflammatory phase of healing, a process whose failure perpetuates chronic non-healing wounds."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine support: leptin promotes keratinocyte proliferation and angiogenesis in healing skin, and leptin resistance in obesity and diabetes contributes to the impaired wound repair seen in those conditions."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Fibrotic remodeling: IL-13, with IL-4 (already mapped), polarises macrophages to the reparative M2 phenotype and drives fibroblast collagen production, and its excess underlies the hypertrophic scars and keloids of dysregulated healing."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Reactive oxygen species: xanthine-oxidase-derived reactive oxygen species, at low levels, support signalling and microbial killing in healing wounds, but in excess and in chronic wounds they cause oxidative damage (NRF2 already mapped) that stalls repair."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Neurogenic repair: CGRP released from sensory nerves, with substance P (already mapped), promotes the vasodilation, angiogenesis and keratinocyte proliferation of wound healing, and denervation impairs repair as in diabetic foot ulcers."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Purinergic angiogenesis: adenosine accumulating in the hypoxic wound promotes angiogenesis and a reparative, anti-inflammatory macrophage phenotype (already mapped), a purinergic signal supporting the transition to tissue rebuilding."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Inflammatory phase: neutrophils are the first cells recruited to the wound, debriding debris and killing bacteria (S100A8/A9 already mapped), and their timely clearance by macrophages (already mapped) lets healing progress to the reparative phase."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Impaired diabetic healing: type 2 diabetes impairs wound healing through microvascular disease, neuropathy (CGRP already mapped) and hyperglycaemia, producing the chronic diabetic foot ulcers that are a major cause of amputation."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Wound oxygenation: hypoxia (HIF already mapped) initiates the angiogenic signal, but adequate oxygen is needed for the collagen cross-linking and oxidative bacterial killing of repair, the rationale for hyperbaric oxygen in problem wounds."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Reparative adipokine: adiponectin promotes the keratinocyte and fibroblast (already mapped) proliferation and migration of wound repair, and its deficiency in obesity contributes to the impaired healing (leptin already mapped)."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine inflammation: resistin, with leptin and adiponectin (already mapped), links the adipose state to the inflammation of the wound, contributing to the impaired healing of the obese and diabetic (insulin already mapped) wound."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Chronic-wound iron: the persistent inflammation (IL-6 already mapped) of the chronic non-healing wound raises hepcidin, sequestering the iron (already mapped) needed for the repair and the oxygen (already mapped) delivery."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "M1-to-M2 transition: the macrophages transition from the inflammatory M1 to the reparative M2 (IL-4 and IL-13 already mapped) phenotype, orchestrating the debridement, the angiogenesis (VEGF already mapped) and the resolution of wound healing."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Haemostatic plug: the platelets form the initial haemostatic plug (thrombin and fibrinogen already mapped) and release the PDGF and TGF-β (already mapped) growth factors that initiate wound healing."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Lysyl-oxidase crosslinking: the copper-dependent lysyl oxidase cross-links the collagen (already mapped) and elastin, and the copper promotes the angiogenesis (VEGF and HIF already mapped) of wound healing."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive resolution: the T cells (perforin already mapped) accumulate in the later phases and modulate the resolution and the scar quality of wound healing."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "M1 phase regulation: the IFN-γ activates the inflammatory M1 macrophages (already mapped) and antagonises the profibrotic type-2 (IL-4 and IL-13 already mapped) arm, tuning the scarring of wound healing."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil repair arm: IL-5 recruits the eosinophils that, via the type-2 (IL-4 and IL-13 already mapped) cytokines, promote the reparative M2 macrophage (already mapped) programme of wound healing."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "M1 Th1 arm: IL-12 polarises the Th1 (IFN-γ already mapped) and the M1 macrophage (already mapped) programme of the inflammatory phase of wound healing."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 arm: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory phase and the antimicrobial defence of wound healing."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate wound interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the damage- and pathogen-associated DNA, modulates the inflammatory phase of wound healing."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension that supports the proliferative and remodelling phases of wound healing."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial alarmin: TSLP, released by the injured keratinocytes, initiates the type-2 (IL-4 and IL-13 already mapped) immunity that, with periostin (already mapped), promotes the re-epithelialisation and remodelling of wound healing."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Itch cytokine: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, is the pruritogenic effector of the itch that accompanies the proliferative and remodelling phases of wound healing."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Inflammatory-phase complement: the complement C3 activation and its C3a anaphylatoxin amplify the early inflammatory phase, recruiting the neutrophils (already mapped) and mast cells (already mapped) of wound healing."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a chemotaxis: the C5aR1 signalling (with the complement C3 already mapped) mediates the C5a-driven chemotaxis of the neutrophils and monocytes into the wound during the inflammatory phase of healing."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Resolution regulation: factor H regulates the alternative complement pathway (complement C3 and C5aR1 already mapped), tempering the complement activation to allow the resolution and remodelling phases of wound healing."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-complement regulation: C1-esterase inhibitor restrains the classical complement pathway (complement C3 and C5aR1 already mapped) at the wound site, limiting collateral tissue destruction and facilitating the transition from inflammation to repair in wound healing."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Tissue-protective EPO: erythropoietin, acting via EPOR on keratinocytes (skin already mapped) and endothelial cells (already mapped), accelerates re-epithelialisation and angiogenesis (VEGF already mapped) and reduces the oxidative-stress burden during wound healing."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Inflammatory-phase C5a: complement C5 (upstream of C5aR1 already mapped) is activated at the wound site, generating C5a that amplifies the early neutrophil (already mapped) and mast-cell (already mapped) recruitment into the inflammatory phase of wound healing."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian wound repair: melatonin accelerates wound healing by promoting keratinocyte (skin already mapped) migration and fibroblast (already mapped) collagen synthesis, with antioxidant effects that reduce the oxidative damage of the inflammatory phase."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Epithelial re-epithelialisation: prolactin receptors on keratinocytes (skin already mapped) and fibroblasts (already mapped) promote cell proliferation and migration in the proliferative phase; wound-fluid prolactin is elevated above circulating levels."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Neuroendocrine wound modulator: oxytocin receptors on keratinocytes (skin already mapped) and fibroblasts (already mapped) accelerate re-epithelialisation and collagen (already mapped) remodelling; oxytocin deficiency in stress and aging impairs wound healing."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Wound testosterone: testosterone impairs cutaneous healing by suppressing macrophage (already mapped) M2 polarisation and fibroblast (already mapped) collagen (already mapped) synthesis; androgens explain the male sex disadvantage in wound-repair kinetics."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Wound vasopressin: vasopressin (ADH) vasoconstricts the wound-bed microcirculation and modulates platelet aggregation (nitric-oxide already mapped) in haemostasis; V1aR on fibroblasts (already mapped) promotes TGF-β (already mapped) driven wound contraction."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Wound selenium: selenoprotein antioxidants (GPx) counter the ROS burst of the inflammatory phase; selenium deficiency impairs macrophage (already mapped) bactericidal activity and fibroblast (already mapped) collagen (already mapped) cross-linking in chronic wounds."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Wound iodine: topical iodine (cadexomer-iodide) provides antimicrobial activity in wound care; systemic iodine-dependent thyroid hormones regulate macrophage (already mapped) polarisation and fibroblast (already mapped) proliferative responses in wound healing."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Wound sodium: sodium-driven osmotic signalling modulates macrophage (already mapped) inflammatory polarisation and NF-κB (already mapped) cytokine production in the wound inflammatory phase; local sodium accumulation amplifies pro-inflammatory and anti-fibrotic responses."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Wound magnesium: magnesium is required for fibroblast (already mapped) collagen (already mapped) cross-linking and matrix metalloproteinase activity in wound remodelling; magnesium deficiency impairs macrophage (already mapped) M2 polarisation and delays wound closure."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Wound potassium: potassium efflux activates macrophage (already mapped) NLRP3 inflammasome in wound inflammation; potassium signalling modulates NF-κB (already mapped) and IL-6 (already mapped) cytokine output and fibroblast (already mapped) proliferation in wound healing."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Wound phosphorus: phosphorus fuels fibroblast (already mapped) collagen synthesis and macrophage (already mapped) phagocytosis; phosphorus deficiency impairs TGF-β (already mapped) and VEGF (already mapped) and mTOR (already mapped)-driven proliferative phase of wound healing."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Wound chloride: chloride channels on macrophages (already mapped) and neutrophils (already mapped) modulate ROS burst and bacterial killing; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory signalling in the wound inflammatory phase."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Wound sulfur: H2S from sulfur-amino acids in fibroblasts (already mapped) and macrophages (already mapped) promotes vasodilation; sulfur deficiency impairs TGF-β (already mapped) and VEGF (already mapped) collagen (already mapped) synthesis and prolongs wound inflammation."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Wound nitrogen: nitric oxide from iNOS in macrophages (already mapped) and fibroblasts (already mapped) promotes vasodilation and collagen (already mapped) crosslinking; nitrogen deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of wound healing."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Wound carbon: CO2 in bicarbonate buffering of macrophages (already mapped) and fibroblasts (already mapped) regulates pH for collagen (already mapped) synthesis; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory phase of wound healing."
---

# Wound Healing

## Overview

**Wound healing** is the fundamental biological process by which multicellular organisms restore tissue integrity after injury. In mammals, cutaneous wound healing (skin) is the most studied model and proceeds through **four overlapping, coordinated phases** [^singer-1999-wound-healing-review]:

1. **Hemostasis (seconds to hours):** Platelet activation, fibrin clot formation, and provisional matrix deposition
2. **Inflammation (hours to days):** Neutrophil and macrophage infiltration; debridement, antimicrobial defense, and growth factor release
3. **Proliferation (days to weeks):** Fibroblast migration, granulation tissue formation, angiogenesis, re-epithelialization, and wound contraction
4. **Remodeling (weeks to years):** Scar maturation, collagen crosslinking and reorganization, and vasculature regression

**Evolutionary context:** Complete regeneration (scarless repair with restoration of hair follicles, glands, and full tissue architecture) occurs in some vertebrates (axolotl, zebrafish) and in mammalian fetal wounds (<18 weeks gestation). Adult mammalian repair is predominantly fibrotic and scar-forming — a trade-off favoring rapid barrier restoration over perfect structural restoration.

**Clinical burden of impaired healing:**
- **Chronic wounds** (non-healing >3 months): Diabetic foot ulcers (~6.4 million US), venous leg ulcers (~2.5 million US), pressure ulcers (~2 million US); total burden ~$31 billion/year in the US
- **Hypertrophic scars and keloids:** Pathological fibroproliferative responses; affected by genetic predisposition (darker skin types), wound location (sternum, shoulder, earlobe), and infection
- **Pathological under-healing:** Anastomotic dehiscence post-surgery; pressure ulcers in the spinal cord injured; radiation-induced impaired healing

## Structure

### Four-phase molecular framework

**Phase 1 — Hemostasis (seconds to ~30 min):**
- Vascular injury → sub-endothelial collagen exposed → **von Willebrand factor (vWF)** bridges collagen to platelet GPIbα → platelet adherence → **platelet activation** (shape change, degranulation)
- Platelet α-granule contents released: **fibrinogen, FN, vWF, thrombospondin, PDGF-AB/BB, TGF-β1, EGF, FGF-2** — the initial growth factor payload at wound sites
- Extrinsic coagulation cascade: tissue factor (TF) from injured fibroblasts/endothelium → VIIa → Xa/Va → thrombin → fibrinogen → **fibrin clot**; cross-linked by FXIIIa (transglutaminase) → fibrin-FN provisional matrix
- **Provisional matrix composition:** Fibrin + fibronectin + vitronectin + tenascin-C; serves as scaffold for neutrophil and macrophage migration and as a reservoir for growth factors (PDGF, TGF-β, FGF bound to matrix)

**Phase 2 — Inflammation (hours to days 1-5):**

*Neutrophil phase (0-72h):*
- Platelet-derived **CXCL4 (PF4), CXCL7 (NAP-2), CCL3** + mast cell histamine → neutrophil recruitment
- Neutrophils: phagocytosis of bacteria, debris; **NETs (neutrophil extracellular traps)** in infected wounds; elastase + MMP-8 debridement; ROS generation (respiratory burst)
- Resolution: neutrophil apoptosis → efferocytosis by macrophages → switch from M1 → M2 phenotype

*Macrophage phase (day 2-5):*
- **M1 macrophages** (classically activated): CCL2 + CXCL8-driven recruitment → TNF-α, IL-1β, IL-6, MMP-9 → antimicrobial; remove neutrophil corpses
- **M2 macrophages** (alternatively activated): IL-4/IL-13 (from eosinophils/mast cells) → Arg-1, CD163, TGF-β1, PDGF, VEGF, IGF-1 → transition to proliferative phase; impaired M1→M2 switch = hallmark of chronic wounds
- Macrophage VEGF → capillary ingrowth; macrophage TGF-β1 → fibroblast activation; macrophage IGF-1 → keratinocyte proliferation

**Phase 3 — Proliferation (day 4 to week 3):**

*Fibroblast activation and granulation tissue:*
- PDGF-BB (from platelets + macrophages) + TGF-β1 → fibroblast chemotaxis into wound via α5β1-FN haptotaxis → fibroblast proliferation (FGF-2) → **granulation tissue**: type III collagen + fibronectin + hyaluronic acid + abundant capillaries (from VEGF-driven angiogenesis)
- **Myofibroblast differentiation** (critical event): TGF-β1 + mechanical tension + EDA-FN → α-SMA incorporation into stress fibers → **wound contraction** (~30-40% of wound closure area reduction) via myofibroblast isometric contraction; myofibroblasts produce type I/III collagen, FN, fibrillin

*Re-epithelialization:*
- Within hours of injury, leading-edge keratinocytes dissolve hemidesmosomes, extend lamellipodia, and migrate across the provisional matrix (integrin αvβ5-FN, α5β1-FN, α2β1-collagen)
- EGF (from platelets) + KGF/FGF-7 (from fibroblasts) + HGF → keratinocyte migration and proliferation; MMP-1 (collagenase) cleaves type I collagen for keratinocyte path-clearing
- Contact inhibition and TGF-β1 → regeneration of stratified epidermis and basement membrane (laminin-5, collagen IV) once wound surface is covered
- **Stem cell contribution:** Bulge stem cells of hair follicles → accelerate re-epithelialization; important in deep partial-thickness burns

*Angiogenesis:*
- Wound hypoxia → HIF-1α → VEGF-A + PDGF-B + Ang-2 → endothelial tip cells sprout from wound margins; pericyte recruitment (PDGF-B/PDGFR-β) → vessel stabilization
- Granulation tissue is among the most vascularized tissues transiently; vasculature density ~50% higher than normal dermis

**Phase 4 — Remodeling (week 3 to 1-2 years):**
- Type III collagen (flexible, rapid; predominates in granulation tissue) → replaced by type I collagen (stronger, stiffer) via MMP-1/3/13 + TIMP-1/2 balance
- Collagen fiber reorganization: random fibers (in early scar) → parallel arrays (in mature scar; tensile strength returns to ~80% of unwounded skin by 12 months — never reaches 100%)
- **Myofibroblast apoptosis:** TGF-β withdrawal + mechanical unloading → myofibroblast apoptosis; failure of apoptosis → hypertrophic scar or keloid (persistent α-SMA+ fibroblasts)
- Vasculature regression: Ang-1/Tie2 stabilization + VEGF withdrawal → capillary pruning → mature scar is less vascular than granulation tissue

## Function

### Key growth factor axes in wound healing

| Growth Factor | Source | Primary wound effect |
|:---|:---|:---|
| **PDGF-BB** | Platelets, macrophages | Fibroblast/pericyte chemotaxis and proliferation; most potent fibroblast mitogen |
| **TGF-β1** | Platelets, macrophages, fibroblasts | Myofibroblast differentiation; collagen synthesis; re-epithelialization; scar formation |
| **EGF/EGFR** | Platelets, macrophages | Keratinocyte migration and proliferation; re-epithelialization |
| **VEGF-A** | Macrophages, keratinocytes | Angiogenesis into granulation tissue; wound vasculature formation |
| **FGF-2 (bFGF)** | Fibroblasts, endothelium | Fibroblast and endothelial proliferation; angiogenesis; basement membrane reconstitution |
| **KGF/FGF-7** | Fibroblasts (paracrine) | Keratinocyte-specific mitogen; re-epithelialization |
| **IGF-1** | Macrophages, fibroblasts | Fibroblast and keratinocyte proliferation; synergizes with PDGF/EGF |

### Therapeutic interventions

**Topical growth factors (approved):**
- **Becaplermin (Regranex; recombinant PDGF-BB):** FDA-approved for diabetic foot ulcers; 30% complete healing improvement vs. placebo; Black Box Warning: increased cancer risk at ≥3 tube applications (controversial, epidemiologic signal)
- **Epidermal growth factor (EGF) topical:** Approved in some countries for diabetic and burn wounds; accelerates re-epithelialization

**Advanced wound dressings:**
- **Negative pressure wound therapy (NPWT; VAC therapy):** Mechanical suction removes exudate, reduces edema, promotes granulation tissue by increasing local perfusion; standard of care for complex wounds, dehiscence, and diabetic foot ulcers
- **Collagen/ORC matrix dressings:** Provide provisional ECM scaffold; promote FN deposition; inhibit excess MMPs in chronic wounds
- **Skin substitutes:** Apligraf (bilayered living cell construct — allogeneic fibroblasts + keratinocytes) and Dermagraft (fibroblast-seeded scaffold) — FDA-approved for venous leg ulcers and diabetic foot ulcers; temporary coverage and growth factor delivery

**Gene and cell therapy (investigational):**
- Adipose-derived MSC and bone marrow MSC: Paracrine VEGF/PDGF/FGF secretion → accelerated neovascularization; Phase 2/3 trials in diabetic foot ulcers
- HIF-1α gene therapy: Increased VEGF expression → angiogenesis; studied in critical limb ischemia + wound healing

### Impaired wound healing — chronic wounds

**Diabetic wounds:**
- Hyperglycemia → AGE → RAGE activation → NF-κB → inflammatory cytokines; impaired neutrophil function (reduced phagocytosis); impaired keratinocyte EGFR signaling; reduced HIF-1α (prolyl hydroxylase overactive in high glucose) → reduced VEGF → poor angiogenesis
- Peripheral neuropathy → insensate foot → repetitive trauma; peripheral vascular disease → ischemia
- **Diabetic foot ulcers:** Texas classification (depth, infection, ischemia); off-loading is critical; MDT (vascular surgery, orthotics, wound care, endocrinology)

**Venous leg ulcers:**
- Chronic venous hypertension → fibrin/fibronectin pericapillary cuffing → diffusion barrier + growth factor trapping → impaired wound healing; elevated MMP-1/MMP-9 in wound fluid degrades provisional matrix faster than it can be deposited

**Pressure ulcers:**
- Sustained pressure > capillary closing pressure → ischemia → necrosis; common over bony prominences (sacrum, heel, trochanter); staged I-IV by NPIAP classification; reactive oxygen species burst upon reperfusion → additional injury

## Pathology

**Hypertrophic scars:**
- Elevated scar confined to wound margins; TGF-β1 excess → persistent myofibroblasts; type III collagen dominance; spontaneous resolution possible (12-24 months); treatment: intralesional triamcinolone, silicone sheets, pressure garments

**Keloids:**
- Scar tissue extends beyond original wound margins; genetic predisposition (particularly Fitzpatrick IV-VI skin types; Chr15q21, FN1, NEDD4 risk variants); MMP-1↓ + TIMP-2↑ → collagen accumulation; myofibroblasts resist apoptosis; treatment difficult: triamcinolone ± 5-FU ± surgery ± radiation; 50-80% recurrence without adjuvant therapy

**Wound infection:**
- Biofilm formation (Staphylococcus aureus, Pseudomonas aeruginosa) prevents healing; S. aureus virulence factors degrade FN (staphylokinase, SplA/B proteases) → disrupts provisional matrix; biofilm-embedded bacteria resist antibiotics (100-1000× higher MIC); require mechanical debridement + biofilm-disrupting agents (cadexomer iodine, DACC dressings)

**Scarless fetal healing:**
- Fetal wounds (<18-20 weeks gestation) heal without scar; high hyaluronic acid → anti-inflammatory; TGF-β3 > TGF-β1/2 → less myofibroblast activation; robust inflammation resolution; therapeutic target: TGF-β3 analogs (avotermin — Phase 2; failed Phase 3 vs. placebo for improved scar appearance)

## Connections

- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Plasma FN is cross-linked into fibrin clots → provisional scaffold for platelets, neutrophils, and fibroblasts; cellular FN from fibroblasts drives granulation tissue; FN-integrin α5β1 → fibroblast migration and myofibroblast differentiation → wound contraction and closure.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 from platelets and macrophages drives myofibroblast differentiation (α-SMA+ → wound contraction), collagen I synthesis, and re-epithelialization; excess TGF-β → hypertrophic scar and keloid; TGF-β3 promotes scarless fetal healing; pirfenidone inhibits fibrogenic signaling.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-A from keratinocytes and macrophages drives angiogenesis into the wound bed; HIF-1α (hypoxic wound center) → VEGF → new vessel formation in granulation tissue; anti-VEGF therapy impairs wound healing — a known adverse effect of bevacizumab and other anti-VEGF agents.
- `connects-to` → **[Diabetic Retinopathy](../diabetic-retinopathy/README.md)** — Diabetes impairs wound healing through AGE accumulation, pericyte dysfunction, impaired neutrophil function, and reduced HIF-1α/VEGF response; diabetic foot ulcers affect ~15% of people with diabetes and are the leading cause of non-traumatic amputation.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages orchestrate wound healing's inflammatory-to-proliferative switch: M1 cells clear debris, then become M2 cells that secrete TGF-β1, PDGF, VEGF, and IGF-1 to drive fibroblasts, angiogenesis, and re-epithelialization; a failed M1→M2 switch defines chronic wounds.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Wound fibroblasts migrate along the fibronectin scaffold and lay down the type III collagen of granulation tissue; TGF-β1 plus tension converts them into α-SMA+ myofibroblasts that contract the wound and, failing to apoptose, produce hypertrophic scars and keloids.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Cutaneous repair is the canonical wound-healing model — hemostasis, inflammation, proliferation, remodeling — restoring the skin barrier with a fibrotic scar rather than regeneration; chronic non-healing ulcers (diabetic, venous, pressure) carry a ~$31 billion annual US burden.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets fire the starting gun of wound healing: at injury they form the hemostatic plug and degranulate, releasing PDGF, TGF-β, and VEGF that recruit neutrophils and macrophages and prime fibroblasts — the growth-factor surge launching the inflammatory phase.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Collagen is the structural endpoint of wound healing: fibroblasts first lay down weak type III collagen in granulation tissue, which remodeling replaces with cross-linked type I collagen regaining ~80% of tensile strength over months; dysregulated turnover yields keloids.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Systemic sclerosis is wound healing that never stops: the TGF-β-driven myofibroblast activation and collagen deposition that should close a wound and resolve becomes self-sustaining and widespread, scarring skin and organs — fibrosis is dysregulated persistent repair.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes is the leading cause of chronic non-healing wounds: hyperglycemia impairs every healing phase—blunting neutrophil and macrophage function, stiffening capillaries, adding neuropathy—so diabetic foot ulcers stall and drive most non-traumatic amputations.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Angiogenesis by endothelial cells is essential to wound healing: VEGF from the wound bed drives endothelial sprouting that forms granulation tissue's capillaries, restoring oxygen—when this fails (ischemia, diabetes), the wound cannot progress to repair.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Wound healing is the integumentary system restoring its barrier: hemostasis, inflammation, proliferation, and remodeling rebuild epidermis and dermis after injury, but imperfectly—scar replaces the original architecture, lacking hair follicles and full strength.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils lead the inflammatory phase of wound healing: arriving within hours, they kill bacteria and clear debris, but their proteases also damage tissue—so timely resolution is essential, and persistent neutrophilia underlies chronic non-healing wounds.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF is a master growth factor of wound repair: released by degranulating platelets, it recruits and activates fibroblasts and smooth muscle, driving granulation tissue and collagen deposition—and recombinant PDGF (becaplermin) treats diabetic foot ulcers.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity impairs wound healing: poor tissue perfusion, chronic low-grade inflammation, and frequent coexisting diabetes slow each phase of repair, so obese and diabetic patients suffer more wound dehiscence, infection and chronic ulcers—a major surgical burden.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Wound healing tips into fibrosis when it overshoots: the same fibroblast and TGF-beta program that repairs a wound, if unresolved, lays down excess collagen as hypertrophic scars, keloids or organ fibrosis—so pathological fibrosis is wound healing that never stops.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Oxygen is rate-limiting for wound healing: collagen synthesis and the bacteria-killing oxidative burst both need it, so hypoxic, poorly perfused wounds (diabetes, vascular disease) heal slowly—why perfusion and hyperbaric oxygen matter for chronic wounds.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells regulate the wound's transition from inflammation to repair: their cytokines orchestrate macrophage switching and fibroblast activity, so the adaptive immune balance shapes whether a wound heals cleanly or scars—or fails to close in chronic wounds.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Intact peripheral nerves are needed for wounds to heal: sensory loss removes the protective reflexes that prevent repeat injury and the neuropeptides that aid repair, so diabetic neuropathy turns minor foot wounds into chronic, non-healing ulcers.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Wound closure depends on contractile cells: fibroblasts differentiate into smooth-muscle-like myofibroblasts that pull wound edges together and lay down matrix, so this contraction shrinks the defect—but if unchecked it drives contractures and excess scarring.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells help orchestrate early wound healing: degranulating to release histamine, heparin, and growth factors, they boost vascular permeability and recruit inflammatory cells—useful for repair, yet their excess is implicated in hypertrophic scars and keloids.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Wound healing begins with thrombin building the clot: it converts fibrinogen to fibrin, forming the provisional matrix that stops bleeding and scaffolds incoming cells, while also activating platelets—launching the cascade toward repair.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Wound hypoxia drives repair through HIF-1alpha: the low-oxygen wound bed stabilizes HIF-1alpha, which switches on VEGF and other genes to sprout vessels and recruit cells—so impaired HIF signaling (as in diabetes) helps explain chronic non-healing wounds.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc is an essential cofactor for wound healing: it supports the metalloproteinases, DNA synthesis and immune cells that rebuild tissue, so zinc deficiency slows healing—one reason nutritional status shapes how wounds close.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Wound healing needs copper to knit collagen: the enzyme lysyl oxidase uses copper to cross-link collagen into strong scar, and copper also spurs new vessels, so copper deficiency leaves wounds weak and slow to close.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol sabotages wound healing: glucocorticoids suppress the inflammatory cleanup, blunt fibroblast collagen synthesis, and slow re-epithelialization, so steroid use is a classic cause of dehiscence and chronic non-healing wounds.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells steer wounds from inflammation to repair: Tregs accumulate in healing skin and damp down the inflammatory phase while promoting tissue regeneration, helping resolve the wound rather than scar it excessively.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 runs the inflammatory phase of wound healing: released early by immune cells, it recruits neutrophils and macrophages and switches on repair programs, so balanced IL-6 is needed—too little stalls healing, too much scars.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Healing isn't just skin-deep—the gut must heal too: surgical anastomoses and mucosal ulcers in the large intestine knit back together by the same phases, and failure of this internal repair causes leaks, a feared surgical complication.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help orchestrate the healing wound: sampling the injured tissue, they bridge innate and adaptive immunity and release signals that guide the shift from inflammation to repair, tuning how cleanly a wound closes.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Light is harnessed to heal: photobiomodulation with low-level laser or LED photons, and UV light for infected wounds, are used to coax stubborn chronic wounds toward closure, the optics of skin shaping how deep the photons reach.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver underwrites wound repair from afar: it makes the clotting factors that seal the wound and the proteins healing demands, so liver failure brings coagulopathy and slow, poor healing.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron is built into the chemistry of repair: it is a cofactor for the prolyl hydroxylases that mature collagen, so iron deficiency and poor oxygen delivery leave a wound unable to lay down strong scar.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy watches a wound pull itself shut: fibroblasts transform into myofibroblasts studded with actin stress fibers that contract the edges together, while newly secreted collagen fibrils assemble into the banded scaffold of scar.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium signals the wound from the first second: it is the ion that fires the clotting cascade to stop bleeding, then sets up the gradient that drives keratinocytes to migrate and differentiate as they resurface the skin.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D arms the healing skin: it spurs keratinocytes to make cathelicidin, the antimicrobial peptide that guards a fresh wound from infection, so deficiency leaves repair slower and more prone to breaking down.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Healing runs on protein: building new collagen and tissue demands amino acids, so the low albumin of malnutrition signals a body that cannot keep up — slowing repair and, through low oncotic pressure, swelling the wound with edema.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Repair is hungry for oxygen the red cells carry: collagen cross-linking and the respiratory burst that kills bacteria both need it, so anemia or poor perfusion starves the wound bed and stalls healing.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Nitric oxide orchestrates the repair: released by endothelium and macrophages, it dilates vessels to feed the wound, spurs angiogenesis and collagen deposition, and kills microbes — and its deficiency is one reason diabetic wounds heal so poorly.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — New vessels must be built and then stabilized: in the proliferative phase angiopoietins work with VEGF to sprout and mature the capillaries that feed granulation tissue, the blood supply without which a wound cannot fill in.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Infection is the great stall: Staphylococcus aureus colonizes wounds and builds biofilms that lock healing in a chronic inflammatory phase, the prime reason surgical and chronic wounds fail to close.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A wound is a doorway to the bloodstream: when local infection breaches the granulation barrier, bacteria and their toxins spill into the circulation, and wound sepsis turns a local repair problem into a life-threatening systemic one.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen speeds repair: it boosts collagen deposition and dampens the excessive inflammation that stalls healing, which is why wounds close more slowly after menopause and topical estrogen has been tried to accelerate them.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Fat cells join the repair crew: dermal adipocytes and adipose-derived stem cells help recruit fibroblasts and rebuild the wound bed, while the dysfunctional adipose of obesity instead impairs healing.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Failing kidneys slow every wound: the uremia, anemia, and poor perfusion of chronic kidney disease blunt the inflammatory and proliferative phases, making non-healing wounds and ulcers a common, stubborn problem in these patients.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammation that won't switch off stalls repair: TNF-α drives the early inflammatory phase, but its persistence — as in diabetic and chronic wounds — keeps the wound stuck in inflammation, degrading matrix and blocking the move to proliferation and closure.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — The first responders open the vessels: histamine released by mast cells at the injury dilates capillaries and raises their permeability, letting plasma, clotting factors and immune cells flood in to begin the healing cascade.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — A kinin both inflames and rebuilds: bradykinin generated at the wound widens vessels and signals pain, but also stimulates the fibroblast proliferation and angiogenesis that drive the repair, linking the inflammatory and rebuilding phases.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 drives the skin to close: downstream of IL-6 and growth factors, STAT3 signaling pushes keratinocyte migration and proliferation across the wound bed, so its loss markedly slows re-epithelialization.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB runs the inflammatory phase: activated in immune cells and keratinocytes at the injury, it switches on the cytokines and antimicrobial defenses that clear debris and pathogens before the rebuilding phase can begin.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The same clotting that seals wounds can misfire: the surgery and immobility that accompany major wound repair, layered on the body's natural post-injury hypercoagulable state, raise the risk of deep-vein thrombosis.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — It colonizes wounds that won't close: Candida joins bacteria in the biofilms of chronic non-healing ulcers, and its presence sustains the inflammatory, proteolytic environment that keeps a wound stuck in the inflammatory phase.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Starved of blood, tissue cannot rebuild: peripheral arterial disease from atherosclerosis cuts oxygen and nutrient delivery to a wound bed, a leading cause of ischemic, non-healing lower-limb ulcers and amputation.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Low oxygen-carrying capacity stalls repair: anemia of chronic disease reduces the oxygen reaching the wound bed needed for collagen cross-linking and the respiratory burst, slowing closure in chronically ill patients.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Its drugs impair the healing it needs after surgery: corticosteroids, methotrexate and biologics used in rheumatoid arthritis blunt inflammation and collagen synthesis, raising the rate of wound dehiscence and infection after operations.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Bone repair is wound healing of the skeleton: fracture union recapitulates the same inflammatory, proliferative and remodeling phases, so the impaired healing of aging and chronic disease also delays the union of osteoporotic fractures.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Mind and wound feed back on each other: the cortisol and inflammation of depression measurably slow wound closure, while chronic non-healing wounds, pain and disability in turn drive depression.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Immune cells orchestrate repair: neutrophils and macrophages clear debris and release the growth factors that drive proliferation, so immunodeficiency, neutropenia and immunosuppressive drugs all delay healing.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Lymphatic drainage is needed to close a wound: the lymphatics clear interstitial fluid and inflammatory debris from the wound bed, so lymphedema leaves a swollen, stagnant field where chronic ulcers fail to heal.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — A breached barrier invites invasive strep: an open wound is a portal for Streptococcus pyogenes, which causes wound cellulitis, erysipelas and, at its worst, rapidly spreading necrotising fasciitis.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Nerves help wounds close: sensory neuropeptides like substance P drive the inflammatory and angiogenic phases, so denervation and diabetic or pressure-related neuropathy produce chronic, slow-healing ulcers.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones tune repair: glucocorticoid excess from Cushing's or steroids blunts inflammation and collagen synthesis, while thyroid hormone, growth hormone and sex steroids each modulate the speed and strength of healing.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The same cascade rebuilds bone and tendon: fracture and tendon repair follow the inflammation-proliferation-remodelling sequence of wound healing, so the conditions that impair skin healing also delay bony union.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Repair depends on blood supply: healing requires perfusion and an angiogenic phase, so ischaemia from peripheral arterial disease and poor perfusion produce chronic, non-healing wounds.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Oxygen drives collagen synthesis: adequate tissue oxygenation is essential for repair, so hypoxia and the vasoconstriction of smoking markedly impair wound healing.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hormones and life-stage shape healing: oestrogen promotes wound repair so healing slows after menopause, while fetal wounds heal scarlessly — a model for regenerative repair.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Nutrition and the gut underpin repair: protein, energy and the gut's absorptive function fuel healing, and anastomotic wounds in the bowel must heal against constant mechanical and bacterial stress.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Uraemia stalls healing: chronic kidney disease impairs wound repair through uraemic toxins, anaemia and poor nutrition, a major reason dialysis-access and surgical wounds heal poorly.
- `connects-to` → **[Dietary Zinc](../../../03-medicine/03-food/zinc-dietary/README.md)** — Zinc is essential to repair: it is a cofactor for the enzymes of collagen synthesis and cell proliferation, so zinc deficiency markedly delays wound healing.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — They stall repair: glucocorticoids suppress the inflammatory phase, fibroblast proliferation and collagen synthesis of healing, thinning skin and causing wound dehiscence — why chronic steroid users heal slowly after surgery and injury.
- `connects-to` → **[Clostridium tetani](../../../02-pathogen/02-bacteria/clostridium-tetani/README.md)** — Wounds are its gateway: Clostridium tetani spores enter through deep, dirty puncture wounds and germinate in the low-oxygen necrotic tissue, releasing tetanospasmin — making tetanus immunisation status a routine part of wound assessment.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — It delays surgical healing: cytotoxic chemotherapy blunts the proliferating fibroblasts and immune cells of repair, and anti-angiogenic agents like bevacizumab impair new vessel growth, so operations are timed around treatment to avoid dehiscence.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Fracture repair is wound healing of bone: a broken bone runs the same haemostasis-inflammation-proliferation-remodelling cascade, replacing the haematoma with a cartilaginous then bony callus instead of a fibrous scar.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Diabetes cripples repair: hyperglycaemia in type 1 (as in type 2) diabetes impairs every phase of wound healing—poor angiogenesis, dysfunctional neutrophils and neuropathy—producing the chronic diabetic foot ulcers that are a leading cause of amputation.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — The heart heals by scarring: after a myocardial infarction the dead myocardium is replaced by a collagen scar through the same fibroblast-driven repair as skin, since adult cardiomyocytes cannot regenerate.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Mucosal healing as the goal: in inflammatory bowel disease, achieving wound healing of the ulcerated gut lining—'mucosal healing'—is the modern treatment endpoint that predicts durable remission and fewer complications.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Tumours as wounds that never heal: cancers like pancreatic adenocarcinoma hijack the wound-healing programme—angiogenesis, fibroblast activation and immune suppression—to build their desmoplastic stroma, Dvorak's classic insight.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Aberrant repair scars the lung: pulmonary fibrosis is dysregulated wound healing in the alveolus, where repeated injury drives fibroblast-myofibroblast scarring instead of restoring the thin gas-exchange surface.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Granulation needs new vessels: wound healing depends on VEGF-driven angiogenesis to build the capillary-rich granulation tissue, and poor arterial perfusion as in peripheral artery disease stalls repair into chronic non-healing wounds.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The regeneration paradigm: the liver is the body's premier regenerating organ, and the same wound-healing programmes that restore the hepatic lobule after injury, when chronic, lay down the scar of cirrhosis.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Growth-factor drive: FGF signalling through FGFR spurs the keratinocyte proliferation, angiogenesis and fibroblast activation of wound repair, one of the core pathways re-epithelialising and rebuilding injured tissue.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Re-epithelialisation: EGF signalling through EGFR drives the keratinocyte proliferation and migration that resurface a wound, the phase whose failure leaves a chronic ulcer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory phase: IL-1β orchestrates the early inflammatory response to injury, but its persistence in chronic wounds stalls them in a non-healing inflammatory state.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Proliferative repair: IGF-1 stimulates fibroblast proliferation, collagen synthesis and granulation tissue, and its deficiency contributes to impaired healing in diabetes and ageing.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 draws monocytes into the wound, where they mature into the macrophages that clear debris and orchestrate the transition from inflammation to repair.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Resolution phase: IL-10 dampens the inflammatory phase and promotes scarless, regenerative healing, and its deficiency biases wounds toward excessive scarring.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Re-epithelialisation: Wnt/β-catenin signalling drives the keratinocyte proliferation and migration that resurface the wound and regenerate skin appendages.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Prostaglandins produced at the wound drive the vasodilation, increased permeability, and pain of the early inflammatory phase—which is why NSAIDs that block their synthesis can blunt the controlled inflammation that normal healing requires.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Periostin secreted by activated fibroblasts organizes collagen cross-linking and myofibroblast differentiation in the proliferative and remodeling phases, supporting the wound contraction and matrix maturation that restore tissue strength.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Sensory-nerve-derived substance P promotes the angiogenesis and inflammatory-cell recruitment of healing, and its loss in denervated or diabetic skin is a key reason those wounds become chronic and heal so poorly.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — IL-4 polarizes wound macrophages to the M2 phenotype that resolves inflammation and drives the proliferative phase, secreting growth factors for fibroblasts and angiogenesis—the switch from clearing debris to rebuilding tissue.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — Advanced glycation end-products signaling through RAGE sustains a chronic inflammatory, pro-oxidant state in diabetic skin that stalls wounds in the inflammatory phase, a central reason diabetic foot ulcers fail to heal.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 (calprotectin) released by the neutrophils of the early wound amplifies inflammation, and its persistence marks the stalled, neutrophil-dominated inflammatory phase of chronic non-healing wounds.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — HGF acting through the MET receptor drives the keratinocyte migration and proliferation that resurface a wound, together with endothelial responses supporting granulation-tissue angiogenesis.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Connexin-43 is downregulated at the wound edge to permit keratinocyte and fibroblast migration, and its abnormal persistence in chronic and diabetic wounds impairs closure, making Cx43 a wound-healing target.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 (SDF-1) recruits bone-marrow-derived endothelial and mesenchymal progenitor cells into the wound to support angiogenesis and granulation, an axis blunted in diabetic non-healing wounds.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EGF, PDGF and FGF (all mapped) drive the MAPK-ERK cascade that powers the keratinocyte re-epithelialization and fibroblast proliferation of the wound's proliferative phase.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling downstream of the wound growth factors promotes the cell survival, migration and angiogenesis that build granulation tissue.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β signals through SMAD4 (TGF-β mapped) to drive fibroblast-to-myofibroblast transition and the collagen deposition (collagen mapped) of the remodeling phase, and its excess produces fibrotic scarring.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of damage-associated molecular patterns released by tissue injury initiates the inflammatory phase of wound healing (with NF-κB already mapped).
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-driven protein synthesis and cell growth power the proliferative phase of wound healing, supporting keratinocyte migration, fibroblast proliferation and granulation-tissue formation.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2-regulated redox balance governs the reactive-oxygen-species signaling that drives wound healing while limiting the oxidative damage that impairs chronic-wound closure.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes macrophage activation, re-epithelialization and the fibrotic phase of tissue repair in wound healing.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the inflammatory phase of wound healing and the macrophage polarization balance that governs resolution versus chronic non-healing.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA released by damaged cells engages cGAS-STING to drive the early inflammatory signaling that initiates wound healing.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate keratinocyte migration, oxidative-stress handling, and TGF-β output during repair; their dysregulation underlies chronic non-healing diabetic wounds.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2-STAT signaling downstream of inflammatory cytokines (IL-6 already mapped) coordinates the inflammatory-to-proliferative transition of wound healing.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the keratinocyte and fibroblast migration and proliferation of the proliferative phase of wound healing.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the Wnt/β-catenin and metabolic signaling that governs keratinocyte migration and fibroblast activation during wound healing.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling drives the keratinocyte migration and focal-adhesion turnover of re-epithelialization in wound healing.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D-driven proliferation of keratinocytes and fibroblasts sustains the proliferative phase of wound healing.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling regulates the energy state and metabolic transitions of the cells across the phases of wound healing.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the keratinocyte, fibroblast, and immune-cell responses across the phases of wound healing.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the re-epithelialization and angiogenesis of the proliferative phase of wound healing.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte and macrophage recruitment participates in the inflammatory phase of wound healing.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the macrophage and fibroblast phenotype transitions of wound healing.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Fibrinogen and the fibrin clot provide the provisional matrix of the hemostasis phase that initiates wound healing.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory and tissue-repair phases of wound healing.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory phase and antimicrobial defense of wound healing.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the cellular reprogramming during wound healing.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic control of repair: insulin signalling promotes keratinocyte migration and collagen synthesis, and its impairment in diabetes is a leading cause of chronic non-healing wounds, the rationale for glucose control and even topical insulin.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Hemostasis and contraction: platelet-released serotonin drives the early vasoconstriction of hemostasis and later stimulates fibroblast proliferation and wound contraction, linking the platelet plug to the remodeling phase of repair.
- `connects-to` → **[NLRP3 inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammatory phase: the NLRP3 inflammasome matures IL-1beta (already mapped) during the inflammatory phase of healing, and its persistent activation sustains the chronic inflammation that stalls diabetic and pressure-ulcer wounds.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Resolution of inflammation: omega-3 fatty acids are converted to specialised pro-resolving mediators (resolvins, protectins) that actively terminate the inflammatory phase of healing, a process whose failure perpetuates chronic non-healing wounds.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine support: leptin promotes keratinocyte proliferation and angiogenesis in healing skin, and leptin resistance in obesity and diabetes contributes to the impaired wound repair seen in those conditions.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Fibrotic remodeling: IL-13, with IL-4 (already mapped), polarises macrophages to the reparative M2 phenotype and drives fibroblast collagen production, and its excess underlies the hypertrophic scars and keloids of dysregulated healing.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Reactive oxygen species: xanthine-oxidase-derived reactive oxygen species, at low levels, support signalling and microbial killing in healing wounds, but in excess and in chronic wounds they cause oxidative damage (NRF2 already mapped) that stalls repair.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Neurogenic repair: CGRP released from sensory nerves, with substance P (already mapped), promotes the vasodilation, angiogenesis and keratinocyte proliferation of wound healing, and denervation impairs repair as in diabetic foot ulcers.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Purinergic angiogenesis: adenosine accumulating in the hypoxic wound promotes angiogenesis and a reparative, anti-inflammatory macrophage phenotype (already mapped), a purinergic signal supporting the transition to tissue rebuilding.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Inflammatory phase: neutrophils are the first cells recruited to the wound, debriding debris and killing bacteria (S100A8/A9 already mapped), and their timely clearance by macrophages (already mapped) lets healing progress to the reparative phase.
- `connects-to` → **[Type 2 diabetes](../type-2-diabetes/README.md)** — Impaired diabetic healing: type 2 diabetes impairs wound healing through microvascular disease, neuropathy (CGRP already mapped) and hyperglycaemia, producing the chronic diabetic foot ulcers that are a major cause of amputation.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Wound oxygenation: hypoxia (HIF already mapped) initiates the angiogenic signal, but adequate oxygen is needed for the collagen cross-linking and oxidative bacterial killing of repair, the rationale for hyperbaric oxygen in problem wounds.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Reparative adipokine: adiponectin promotes the keratinocyte and fibroblast (already mapped) proliferation and migration of wound repair, and its deficiency in obesity contributes to the impaired healing (leptin already mapped).
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine inflammation: resistin, with leptin and adiponectin (already mapped), links the adipose state to the inflammation of the wound, contributing to the impaired healing of the obese and diabetic (insulin already mapped) wound.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Chronic-wound iron: the persistent inflammation (IL-6 already mapped) of the chronic non-healing wound raises hepcidin, sequestering the iron (already mapped) needed for the repair and the oxygen (already mapped) delivery.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — M1-to-M2 transition: the macrophages transition from the inflammatory M1 to the reparative M2 (IL-4 and IL-13 already mapped) phenotype, orchestrating the debridement, the angiogenesis (VEGF already mapped) and the resolution of wound healing.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Haemostatic plug: the platelets form the initial haemostatic plug (thrombin and fibrinogen already mapped) and release the PDGF and TGF-β (already mapped) growth factors that initiate wound healing.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Lysyl-oxidase crosslinking: the copper-dependent lysyl oxidase cross-links the collagen (already mapped) and elastin, and the copper promotes the angiogenesis (VEGF and HIF already mapped) of wound healing.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive resolution: the T cells (perforin already mapped) accumulate in the later phases and modulate the resolution and the scar quality of wound healing.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — M1 phase regulation: the IFN-γ activates the inflammatory M1 macrophages (already mapped) and antagonises the profibrotic type-2 (IL-4 and IL-13 already mapped) arm, tuning the scarring of wound healing.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil repair arm: IL-5 recruits the eosinophils that, via the type-2 (IL-4 and IL-13 already mapped) cytokines, promote the reparative M2 macrophage (already mapped) programme of wound healing.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — M1 Th1 arm: IL-12 polarises the Th1 (IFN-γ already mapped) and the M1 macrophage (already mapped) programme of the inflammatory phase of wound healing.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 arm: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory phase and the antimicrobial defence of wound healing.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate wound interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the damage- and pathogen-associated DNA, modulates the inflammatory phase of wound healing.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension that supports the proliferative and remodelling phases of wound healing.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial alarmin: TSLP, released by the injured keratinocytes, initiates the type-2 (IL-4 and IL-13 already mapped) immunity that, with periostin (already mapped), promotes the re-epithelialisation and remodelling of wound healing.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Itch cytokine: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, is the pruritogenic effector of the itch that accompanies the proliferative and remodelling phases of wound healing.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Inflammatory-phase complement: the complement C3 activation and its C3a anaphylatoxin amplify the early inflammatory phase, recruiting the neutrophils (already mapped) and mast cells (already mapped) of wound healing.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a chemotaxis: the C5aR1 signalling (with the complement C3 already mapped) mediates the C5a-driven chemotaxis of the neutrophils and monocytes into the wound during the inflammatory phase of healing.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Resolution regulation: factor H regulates the alternative complement pathway (complement C3 and C5aR1 already mapped), tempering the complement activation to allow the resolution and remodelling phases of wound healing.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-complement regulation: C1-esterase inhibitor restrains the classical complement pathway (complement C3 and C5aR1 already mapped) at the wound site, limiting collateral tissue destruction and facilitating the transition from inflammation to repair in wound healing.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Tissue-protective EPO: erythropoietin, acting via EPOR on keratinocytes (skin already mapped) and endothelial cells (already mapped), accelerates re-epithelialisation and angiogenesis (VEGF already mapped) and reduces the oxidative-stress burden during wound healing.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Inflammatory-phase C5a: complement C5 (upstream of C5aR1 already mapped) is activated at the wound site, generating C5a that amplifies the early neutrophil (already mapped) and mast-cell (already mapped) recruitment into the inflammatory phase of wound healing.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian wound repair: melatonin accelerates wound healing by promoting keratinocyte (skin already mapped) migration and fibroblast (already mapped) collagen synthesis, with antioxidant effects that reduce the oxidative damage of the inflammatory phase.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Epithelial re-epithelialisation: prolactin receptors on keratinocytes (skin already mapped) and fibroblasts (already mapped) promote cell proliferation and migration in the proliferative phase; wound-fluid prolactin is elevated above circulating levels.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Neuroendocrine wound modulator: oxytocin receptors on keratinocytes (skin already mapped) and fibroblasts (already mapped) accelerate re-epithelialisation and collagen (already mapped) remodelling; oxytocin deficiency in stress and aging impairs wound healing.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Wound testosterone: testosterone impairs cutaneous healing by suppressing macrophage (already mapped) M2 polarisation and fibroblast (already mapped) collagen (already mapped) synthesis; androgens explain the male sex disadvantage in wound-repair kinetics.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Wound vasopressin: vasopressin (ADH) vasoconstricts the wound-bed microcirculation and modulates platelet aggregation (nitric-oxide already mapped) in haemostasis; V1aR on fibroblasts (already mapped) promotes TGF-β (already mapped) driven wound contraction.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Wound selenium: selenoprotein antioxidants (GPx) counter the ROS burst of the inflammatory phase; selenium deficiency impairs macrophage (already mapped) bactericidal activity and fibroblast (already mapped) collagen (already mapped) cross-linking in chronic wounds.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Wound iodine: topical iodine (cadexomer-iodide) provides antimicrobial activity in wound care; systemic iodine-dependent thyroid hormones regulate macrophage (already mapped) polarisation and fibroblast (already mapped) proliferative responses in wound healing.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Wound sodium: sodium-driven osmotic signalling modulates macrophage (already mapped) inflammatory polarisation and NF-κB (already mapped) cytokine production in the wound inflammatory phase; local sodium accumulation amplifies pro-inflammatory and anti-fibrotic responses.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Wound magnesium: magnesium is required for fibroblast (already mapped) collagen (already mapped) cross-linking and matrix metalloproteinase activity in wound remodelling; magnesium deficiency impairs macrophage (already mapped) M2 polarisation and delays wound closure.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Wound potassium: potassium efflux activates macrophage (already mapped) NLRP3 inflammasome in wound inflammation; potassium signalling modulates NF-κB (already mapped) and IL-6 (already mapped) cytokine output and fibroblast (already mapped) proliferation in wound healing.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Wound phosphorus: phosphorus fuels fibroblast (already mapped) collagen synthesis and macrophage (already mapped) phagocytosis; phosphorus deficiency impairs TGF-β (already mapped) and VEGF (already mapped) and mTOR (already mapped)-driven proliferative phase of wound healing.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Wound chloride: chloride channels on macrophages (already mapped) and neutrophils (already mapped) modulate ROS burst and bacterial killing; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory signalling in the wound inflammatory phase.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Wound sulfur: H2S from sulfur-amino acids in fibroblasts (already mapped) and macrophages (already mapped) promotes vasodilation; sulfur deficiency impairs TGF-β (already mapped) and VEGF (already mapped) collagen (already mapped) synthesis and prolongs wound inflammation.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Wound nitrogen: nitric oxide from iNOS in macrophages (already mapped) and fibroblasts (already mapped) promotes vasodilation and collagen (already mapped) crosslinking; nitrogen deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of wound healing.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Wound carbon: CO2 in bicarbonate buffering of macrophages (already mapped) and fibroblasts (already mapped) regulates pH for collagen (already mapped) synthesis; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory phase of wound healing.

[^singer-1999-wound-healing-review]: Singer AJ, Clark RA. Cutaneous wound healing. *N Engl J Med.* 1999;341(10):738-746. [doi:10.1056/NEJM199909023411006](https://doi.org/10.1056/NEJM199909023411006) · [PubMed 10471461](https://pubmed.ncbi.nlm.nih.gov/10471461/)
[^gurtner-2008-wound-repair-regeneration]: Gurtner GC, Werner S, Barrandon Y, Longaker MT. Wound repair and regeneration. *Nature.* 2008;453(7193):314-321. [doi:10.1038/nature07039](https://doi.org/10.1038/nature07039) · [PubMed 18480812](https://pubmed.ncbi.nlm.nih.gov/18480812/)
[^eming-2014-wound-repair-mechanisms]: Eming SA, Martin P, Tomic-Canic M. Wound repair and regeneration: mechanisms, signaling, and translation. *Sci Transl Med.* 2014;6(265):265sr6. [doi:10.1126/scitranslmed.3009337](https://doi.org/10.1126/scitranslmed.3009337) · [PubMed 25473038](https://pubmed.ncbi.nlm.nih.gov/25473038/)
