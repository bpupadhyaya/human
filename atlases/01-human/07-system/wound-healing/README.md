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

[^singer-1999-wound-healing-review]: Singer AJ, Clark RA. Cutaneous wound healing. *N Engl J Med.* 1999;341(10):738-746. [doi:10.1056/NEJM199909023411006](https://doi.org/10.1056/NEJM199909023411006) · [PubMed 10471461](https://pubmed.ncbi.nlm.nih.gov/10471461/)
[^gurtner-2008-wound-repair-regeneration]: Gurtner GC, Werner S, Barrandon Y, Longaker MT. Wound repair and regeneration. *Nature.* 2008;453(7193):314-321. [doi:10.1038/nature07039](https://doi.org/10.1038/nature07039) · [PubMed 18480812](https://pubmed.ncbi.nlm.nih.gov/18480812/)
[^eming-2014-wound-repair-mechanisms]: Eming SA, Martin P, Tomic-Canic M. Wound repair and regeneration: mechanisms, signaling, and translation. *Sci Transl Med.* 2014;6(265):265sr6. [doi:10.1126/scitranslmed.3009337](https://doi.org/10.1126/scitranslmed.3009337) · [PubMed 25473038](https://pubmed.ncbi.nlm.nih.gov/25473038/)
