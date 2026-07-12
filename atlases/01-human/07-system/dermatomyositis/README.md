---
schema: human-scale-entry/v1
id: dermatomyositis
name: Dermatomyositis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Dermatomyositis is an immune-mediated myopathy with pathognomonic skin findings (heliotrope, Gottron's); type I IFN signature is central; MSAs (anti-MDA5, anti-TIF1γ, anti-NXP2, anti-Jo-1) stratify subtypes; IVIG (FDA Oct 2021), JAK inhibitors (baricitinib) are treatments."
aliases: ["dermatomyositis", "DM", "idiopathic inflammatory myopathy", "IIM", "anti-MDA5 myopathy", "amyopathic dermatomyositis", "antisynthetase syndrome", "juvenile dermatomyositis", "JDM"]
sources:
  - id: lundberg-2021-iim-classification
    type: peer-reviewed
    cite: "Lundberg IE, Tjärnlund A, Bottai M, et al. 2017 European League Against Rheumatism/American College of Rheumatology classification criteria for adult and juvenile idiopathic inflammatory myopathies and their major subgroups. Arthritis Rheumatol. 2017;69(12):2271-2282."
    doi: "10.1002/art.40320"
    pmid: "29106061"
    url: "https://doi.org/10.1002/art.40320"
  - id: aggarwal-2022-ivig-dm-prodera
    type: peer-reviewed
    cite: "Aggarwal R, Charles-Schoeman C, Schessl J, et al. Trial of Intravenous Immune Globulin in Dermatomyositis. N Engl J Med. 2022;387(14):1264-1278."
    doi: "10.1056/NEJMoa2117024"
    pmid: "36198072"
    url: "https://doi.org/10.1056/NEJMoa2117024"
  - id: sato-2021-anti-mda5-ild
    type: peer-reviewed
    cite: "Sato S, Kuwana M. Clinicopathological features of Japanese patients with anti-CADM-140/MDA5 antibody-positive dermatomyositis. Arthritis Rheum. 2009;61(5):611-620."
    doi: "10.1002/art.24341"
    pmid: "19405014"
    url: "https://doi.org/10.1002/art.24341"
  - id: bohan-peter-1975-dm-criteria
    type: peer-reviewed
    cite: "Bohan A, Peter JB. Polymyositis and dermatomyositis. N Engl J Med. 1975;292(7):344-347."
    doi: "10.1056/NEJM197502132920706"
    pmid: "1090839"
    url: "https://doi.org/10.1056/NEJM197502132920706"
cross_links:
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I IFN signature (↑MX1, ↑OAS1, ↑RSAD2) is elevated in muscle and blood in >80% of DM; anti-MDA5 (IFIH1) senses dsRNA → RIG-I/MDA5-MAVS-TBK1-IRF3 → IFN-β; pDC infiltration drives DM muscle interferonopathy; anifrolumab under investigation."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: modulated-by
    note: "IVIG (Octagam 10%; 2 g/kg monthly) is the first FDA-approved DM therapy (Oct 2021; ProDERM trial: CDASI-A improvement 58% vs 29%); MSA autoantibodies (anti-MDA5, anti-TIF1γ, anti-NXP2, anti-Mi-2) are IgG that stratify DM subtypes and prognosis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Baricitinib (JAK1/2) showed efficacy in refractory DM (TRiMM-2: CDASI improvement); tofacitinib (JAK1/3) used for anti-MDA5-associated rapidly progressive ILD; ruxolitinib in refractory MDA5+ DM-ILD; JAK inhibition reduces type I IFN-driven ISG expression."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "DM features pathognomonic skin findings: heliotrope rash (violaceous periorbital edema), Gottron's papules (dorsal MCP/PIP), V-sign (anterior chest/neck), shawl sign, periungual telangiectasias, and mechanic's hands in antisynthetase syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Tacrolimus (calcineurin inhibitor) is steroid-sparing DM therapy; particularly effective in anti-MDA5+ DM-ILD where rapid IFN-driven fibrosis requires aggressive immunosuppression; calcineurin·NFAT pathway drives CD4+/Th-mediated muscle inflammation."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Interstitial lung disease complicates 20-40% of dermatomyositis: anti-MDA5+ DM can cause rapidly progressive ILD reaching respiratory failure within weeks (high ferritin flags the risk), demanding aggressive immunosuppression — tacrolimus triple therapy or JAK inhibitors."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Dermatomyositis is a microangiopathy: complement MAC on muscle capillaries causes capillary dropout → ischemia at fascicle edges, producing the pathognomonic perifascicular atrophy; this complement mechanism distinguishes DM from the T-cell muscle injury of polymyositis."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Dermatomyositis and lupus are both type I interferonopathies with photosensitive rashes, and their cutaneous signs are contrasted: Gottron's papules sit ON the knuckles whereas lupus spares them; both are now treated with anifrolumab, reflecting the shared interferon axis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Dermatomyositis is an idiopathic inflammatory myopathy: complement-mediated capillary injury drives perifascicular atrophy and symmetric proximal weakness (trouble rising, lifting, climbing); CK rises, and it burdens the musculoskeletal system with arthralgia and calcinosis."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Dermatomyositis is paraneoplastic in up to ~20-25% of adults, especially with anti-TIF1γ antibodies: ovarian, lung, breast and GI cancers are over-represented, and ovarian cancer is a classic association—so new adult DM mandates age-appropriate malignancy screening."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Dermatomyositis muscle and skin are infiltrated by macrophages and plasmacytoid dendritic cells pouring out type I interferon, the disease's central cytokine; macrophage inflammation amplifies the complement-driven microangiopathy, and JAK inhibitors blunt this signalling."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Dermatomyositis and systemic sclerosis are interferon-driven connective tissue diseases that overlap in scleromyositis: anti-PM/Scl antibodies mark patients with both inflammatory myopathy and skin fibrosis, blurring the line between the two autoimmune diseases."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Dermatomyositis is a classic paraneoplastic disease: adult-onset DM carries a markedly raised cancer risk—lung (including NSCLC), ovarian, GI, and nasopharyngeal—often within the first years, so a new diagnosis triggers age-appropriate malignancy screening."
  - target: 01-human/07-system/pemphigus-vulgaris
    relation: connects-to
    note: "Dermatomyositis and pemphigus vulgaris are autoimmune skin diseases that can be paraneoplastic: DM is a classic paraneoplastic dermatosis, and paraneoplastic pemphigus accompanies lymphoma/Castleman—so distinctive new skin disease prompts a malignancy search."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Dermatomyositis is a complement-mediated microangiopathy: antibody and complement form the membrane attack complex on endomysial capillaries, destroying them and causing perifascicular muscle atrophy—complement, not T-cell attack, drives the injury."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Dermatomyositis is strongly paraneoplastic: adult-onset disease carries a markedly raised risk of occult cancer—ovarian, lung, gastric, breast—often within the first years, so a new diagnosis triggers cancer screening, with the myositis sometimes heralding the tumor."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells and type-I-interferon immunity underpin dermatomyositis: CD4+ T cells and dendritic cells flood muscle and skin with an interferon signature, and JAK inhibitors blocking this are emerging therapy—adaptive immunity alongside complement."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells fuel dermatomyositis through autoantibodies: myositis-specific antibodies like anti-Mi-2, anti-MDA5 and anti-TIF1-gamma define clinical subsets and predict lung disease or cancer risk, and B-cell depletion with rituximab helps refractory cases."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Dermatomyositis is a paraneoplastic warning sign: adult-onset disease, especially with anti-TIF1-gamma antibodies, carries a markedly raised risk of occult cancer such as breast cancer, so new diagnosis triggers an age-appropriate malignancy search."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Dermatomyositis can strike the heart: myocardial inflammation causes myocarditis, conduction defects and sometimes heart failure—often subclinical yet a leading cause of death in the disease, so cardiac surveillance matters even when skin and muscle dominate."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Dermatomyositis can weaken the swallowing muscles: pharyngeal and upper-esophageal involvement causes dysphagia, raising the risk of aspiration pneumonia—so difficulty swallowing is a red flag for severe disease needing prompt, aggressive treatment."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Dermatomyositis is strongly paraneoplastic: adult onset prompts a cancer hunt, and beyond ovarian and lung tumors, colorectal and other cancers are over-represented—so a new diagnosis triggers age-appropriate malignancy screening, sometimes revealing an occult tumor."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Plasmacytoid dendritic cells help drive dermatomyositis: they are a major source of the type-I interferon that floods affected skin and muscle, so this innate-immune cell sits upstream of the interferon signature that defines the disease and guides JAK-inhibitor therapy."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcinosis is a hallmark of dermatomyositis, especially juvenile: calcium deposits build up in skin and muscle, forming hard, sometimes ulcerating nodules that are painful and hard to treat—a chronic complication distinct from the acute inflammation."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Dermatomyositis can inflame the heart muscle: myocarditis and conduction disease from the same autoimmune process that attacks skeletal muscle add cardiac risk, so cardiomyocyte involvement is screened for even when symptoms are subtle."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Dermatomyositis differs from polymyositis in its immune attack: DM is largely humoral and complement-mediated against muscle capillaries, whereas polymyositis features cytotoxic T cells directly invading muscle fibers—distinguishing the two myopathies."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Dermatomyositis is a complement-driven microangiopathy: the membrane attack complex deposits on muscle and skin capillaries, starving the outer muscle fibers of blood—the perifascicular atrophy that is the disease's pathologic signature."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Dermatomyositis is first treated with cortisol's kin: high-dose corticosteroids suppress the interferon-driven inflammation attacking muscle and skin, the mainstay before steroid-sparing immunosuppressants and JAK inhibitors are added."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Dermatomyositis can scar the lungs, especially the anti-MDA5 type: a rapidly progressive interstitial lung fibrosis is its most dangerous complication, turning a skin-and-muscle disease into a life-threatening respiratory emergency."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Dermatomyositis can starve the blood of oxygen through lung scarring: its rapidly progressive interstitial lung disease, especially the anti-MDA5 type, wrecks gas exchange, making hypoxemia the disease's most lethal turn."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Dermatomyositis can attack the gut's vessels: especially in juvenile disease, a vasculopathy injures the intestinal lining, causing dysphagia, pain and even bowel perforation beyond the classic skin and muscle features."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-kB amplifies the inflammation of dermatomyositis: alongside the dominant type-I interferon signature, this switch drives the cytokines and adhesion molecules that bring immune cells into the inflamed muscle and skin."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Dermatomyositis is a photosensitive disease: its rashes flare in sun-exposed skin—the shawl and V-signs—so UV photons worsen the disease, while MRI imaging helps map inflamed muscle for biopsy."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Calcinosis hardens the tissues in dermatomyositis, especially the juvenile form: calcium-phosphate crystals deposit in skin and muscle, so phosphate as well as calcium drives this disfiguring, hard-to-treat complication."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Dermatomyositis can inflame the heart: myocarditis and conduction disturbances are underrecognized, and cardiac involvement is an important, sometimes silent contributor to the disease's mortality."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals dermatomyositis's interferon signature: tubuloreticular inclusions — undulating tubule arrays — appear inside the capillary endothelial cells of muscle and skin, a hallmark of the type-I-interferon-driven vascular injury."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Severe muscle breakdown can flood the kidney: when dermatomyositis inflames muscle badly enough to cause rhabdomyolysis, released myoglobin clogs the renal tubules and can precipitate acute kidney injury."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Dermatomyositis announces itself around the eyes: the heliotrope rash is a violaceous discoloration of the upper eyelids, often with swelling, one of the most specific skin signs that points straight to the diagnosis."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Myositis-specific autoantibodies map the disease: anti-Jo-1 ties it to lung fibrosis, anti-MDA5 to a rapidly progressive ILD and skin ulcers, and anti-TIF1γ flags a high risk of underlying cancer — the serology guiding workup and prognosis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Dermatomyositis is at heart a disease of the capillaries: complement attack drops out the small vessels feeding muscle, and the VEGF-driven response and resulting ischemia produce the perifascicular atrophy that defines its muscle biopsy."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Adult dermatomyositis can be a cancer's herald: it is strongly paraneoplastic, and beyond the ovarian, gastric, and lung tumors it accompanies, pancreatic cancer is among the malignancies a new diagnosis prompts a search for."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Diagnosis triggers a pelvic search, and pregnancy a careful watch: anti-TIF1γ dermatomyositis demands gynecologic cancer screening, while a flare during pregnancy threatens both mother and fetus and constrains which immunosuppressants are safe."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The gut muscle weakens too: dermatomyositis can slow the stomach and upper digestive tract, and in the juvenile form a vasculopathy can ulcerate or even perforate the bowel, a feared complication of the disease's small-vessel damage."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Sun and steroids both demand vitamin D: the photosensitive rash forces sun avoidance, and the long corticosteroid courses that control the disease drive bone loss, so vitamin D and calcium are given to protect the skeleton."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "An interferon signature defines dermatomyositis: type-I interferon signals through JAK-STAT1 to drive the gene program seen in affected muscle and skin (perifascicular MxA), the rationale for the JAK inhibitors now used, especially in anti-MDA5 disease."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Active myositis thickens the blood: the systemic inflammation, immobility from muscle weakness, and any underlying malignancy raise the risk of deep-vein thrombosis and pulmonary embolism in dermatomyositis."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells make the diagnostic antibodies: the myositis-specific autoantibodies — anti-Mi-2, anti-MDA5, anti-TIF1-gamma — are secreted by plasma cells and define clinical subsets, including which patients need urgent cancer screening."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 tracks the inflammation: this cytokine rises with disease activity in dermatomyositis, fueling the muscle and skin inflammation alongside the dominant interferon signature, and is a target tested for refractory disease."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Faltering immune restraint lets it run: a deficiency and dysfunction of regulatory T cells helps unleash the autoreactive response against muscle and skin, part of why broad immunosuppression rather than a single target is often needed."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "It keeps autoimmune company: dermatomyositis frequently overlaps other connective-tissue diseases including Sjögren's, sharing the interferon-driven autoimmunity that can blur one syndrome into another."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 carries the IL-6 inflammation into muscle: downstream of the IL-6 elevated in dermatomyositis, STAT3 signaling helps sustain the inflammatory attack on muscle and skin, part of the cytokine network targeted by JAK inhibitors."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Treatment trades autoimmunity for infection risk: the high-dose steroids and immunosuppressants used to control dermatomyositis leave patients prone to serious infection and sepsis, a leading cause of death in the disease."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "An opportunistic fungus exploits the immunosuppression: dermatomyositis patients on steroids and other immunosuppressants are at risk of Pneumocystis pneumonia, which is why prophylaxis is often given alongside treatment."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Its steroids erode the skeleton: the prolonged high-dose corticosteroids used to control dermatomyositis, combined with muscle weakness and inactivity, accelerate bone loss and raise the risk of osteoporotic fracture."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Muscle breakdown can spill into the kidney: severe myositis releases myoglobin that injures the renal tubules, and this insult — with nephrotoxic immunosuppressants — can leave lasting chronic kidney impairment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic autoimmune inflammation blunts the marrow: the sustained IL-6 and inflammatory drive of active dermatomyositis raise hepcidin and suppress erythropoiesis, contributing an anemia of chronic disease."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Its lung disease can pressurize the pulmonary arteries: the interstitial lung disease that accompanies dermatomyositis, especially anti-synthetase and MDA5 subtypes, can lead to pulmonary hypertension."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its heavy immunosuppression opens the lung to mold: high-dose corticosteroids combined with methotrexate, azathioprine or rituximab for dermatomyositis can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A disfiguring, weakening disease wears on mood: the visible rash, muscle weakness, chronic course and looming cancer risk of dermatomyositis impair quality of life and contribute to depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its rash is half the diagnosis: dermatomyositis produces a heliotrope eyelid rash, Gottron's papules, the shawl sign and calcinosis — distinctive skin findings that define the disease alongside the myopathy."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It can scar the lungs fast: dermatomyositis, especially the anti-MDA5 subtype, causes interstitial lung disease that can progress rapidly to respiratory failure, a leading cause of death."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A disfiguring disease with cancer risk breeds worry: the visible rash, muscle weakness and the intensive malignancy screening dermatomyositis demands foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is an autoantibody-defined autoimmune disease: myositis-specific antibodies such as anti-MDA5 and anti-TIF1γ mark distinct phenotypes, and a type I interferon signature with complement-mediated capillary damage drives the muscle and skin injury."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its treatment hits the endocrine system: long-term high-dose corticosteroids and immunosuppressants cause Cushingoid features, steroid-induced diabetes and adrenal suppression that must be managed alongside the disease."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Severe muscle breakdown can reach the kidney: extensive myositis can release myoglobin and cause acute kidney injury, and rarely an immune-complex glomerulonephritis accompanies the disease."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It damages vessels beyond the heart muscle: dermatomyositis causes Raynaud's phenomenon and a nailfold capillaropathy, and the chronic inflammation accelerates atherosclerosis."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its cancer link works through the nodes: adult dermatomyositis (especially anti-TIF1γ) is strongly paraneoplastic, and those cancers spread via lymph nodes, with a raised lymphoma risk too."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It spares the nerves: dermatomyositis attacks muscle and skin while sparing the peripheral nerves — distinguishing it from neuropathic weakness — though juvenile disease can rarely cause CNS vasculitis."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "High-dose steroids are first-line: corticosteroids suppress the muscle and skin inflammation of dermatomyositis, with steroid-sparing immunosuppressants added for long-term control."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Refractory disease gets targeted agents: rituximab, IVIG and JAK inhibitors (targeting the type-I-interferon signature) treat dermatomyositis resistant to steroids, especially anti-MDA5 lung disease."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Immunosuppression reawakens latent virus: the heavy immunosuppression for dermatomyositis allows cytomegalovirus and herpes-simplex reactivation, alongside the Pneumocystis risk."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Steroid-sparing and the underlying cancer: methotrexate and azathioprine spare steroids in dermatomyositis, and because anti-TIF1γ disease is often paraneoplastic, chemotherapy directed at the hidden breast, ovarian or lung cancer can itself improve the myositis."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Two faces of weakness: dermatomyositis is a proximal inflammatory myopathy with raised CK and the heliotrope and Gottron skin signs, whereas myasthenia gravis is fatigable neuromuscular-junction weakness with normal CK — a core differential of muscle weakness."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It calcifies soft tissue and thins bone: juvenile dermatomyositis classically deposits dystrophic calcinosis in skin and muscle, while the long-term corticosteroids used to control it drive osteoporosis and fracture risk."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Its lungs can fail fast: interstitial lung disease—especially the rapidly progressive form with anti-MDA5 antibodies—scars the alveolar units and is a leading cause of death in dermatomyositis."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It can inflame the heart muscle: the immune attack on striated muscle in dermatomyositis extends to the myocardium, causing myocarditis, conduction disease and heart failure that drive mortality."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Autoimmune diseases that scar the lung: like ANCA-associated vasculitis, dermatomyositis (notably anti-MDA5) causes interstitial lung disease, though one attacks muscle and skin via interferon and the other small vessels via ANCA."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "A vasculopathy at its core: juvenile dermatomyositis is fundamentally a small-vessel disease, with complement-mediated injury to the arterial wall and capillaries causing the muscle ischaemia, skin ulcers and gut infarction."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "The signature paraneoplastic cancer in Asia: nasopharyngeal carcinoma is the malignancy most strongly tied to dermatomyositis in East Asian populations, a key target of the cancer search every new diagnosis prompts."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy can mimic it: checkpoint-inhibitor cancer therapy can trigger an immune-related myositis—sometimes with myocarditis—that clinically resembles dermatomyositis, an emerging iatrogenic cause."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "MDA5 in common: MDA5 is the viral RNA sensor, and anti-MDA5 dermatomyositis produces a rapidly progressive interstitial lung disease and hyperinflammation strikingly reminiscent of severe COVID-19, with infection studied as a trigger."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Paraneoplastic cancer search: anti-TIF1-gamma dermatomyositis is strongly cancer-associated, so a new diagnosis prompts screening for occult malignancy including the gynaecological cancers—ovarian, breast and endometrial."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: connects-to
    note: "Localising the weakness: dermatomyositis is a myopathy whereas myasthenia gravis is a neuromuscular-junction disease, and both present with proximal weakness—distinguishing the lesion site is central to diagnosis."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "HLA risk and presentation: specific MHC class II (HLA) alleles predispose to dermatomyositis, and antigen presentation drives the autoimmune attack on muscle and skin."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Interferon-driven myopathy: alongside the dominant type I interferon signature, IFN-γ contributes to the immune-mediated muscle inflammation of dermatomyositis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory amplification: IL-1β participates in the muscle and skin inflammation of dermatomyositis, adding to its interferon-dominated cytokine milieu."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory cytokine: TNF-α contributes to the muscle and skin inflammation of dermatomyositis and to the systemic features of the disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 contribution: IL-17 participates in the inflammatory infiltrate of dermatomyositis muscle and skin, adding to the dominant interferon response."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: NLRP3-inflammasome activation matures the IL-1β that amplifies the muscle inflammation of dermatomyositis."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "B-cell depletion: rituximab targets CD20+ B cells in refractory dermatomyositis, cutting production of the myositis-specific autoantibodies and antigen presentation that sustain the autoimmune attack on muscle and skin."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Antibody recycling: the neonatal Fc receptor protects pathogenic IgG from degradation, the mechanism by which high-dose IVIG (approved for dermatomyositis) saturates FcRn and accelerates autoantibody clearance."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Muscle infiltration: CCL2 recruits monocytes into the perivascular and perifascicular regions of dermatomyositis muscle, building the inflammatory infiltrate that accompanies the complement-mediated capillary injury."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "Autoantigen sensor: MDA5 (IFIH1), a RIG-I-like cytosolic RNA sensor, is itself a major dermatomyositis autoantigen — anti-MDA5 antibodies define the clinically-amyopathic subset with rapidly progressive interstitial lung disease and a vasculopathic, ulcerating skin phenotype."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "Autoantibody survival: BAFF supports the autoreactive B cells producing the myositis-specific antibodies (anti-Mi-2, TIF1-γ, NXP2, MDA5), part of the humoral arm that rituximab targets in refractory dermatomyositis."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Capillary vasculopathy: endothelin-1-driven vasoconstriction contributes to the capillary dropout and ischaemia that underlie the perifascicular atrophy of dermatomyositis muscle and the nailfold capillary changes of its vasculopathy."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "MDA5-IFN axis: in anti-MDA5 dermatomyositis the cytosolic RNA sensor signals through MAVS to drive the type-I interferon response that defines the disease and its rapidly progressive interstitial lung disease."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Nucleic-acid sensing: cytosolic DNA sensing through cGAS-STING contributes to the interferon-driven muscle and skin inflammation of dermatomyositis, complementing the RIG-I-like RNA sensing already mapped."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint tolerance: immune-checkpoint-inhibitor therapy can trigger a dermatomyositis-like myositis, implicating PD-1 in maintaining the peripheral tolerance whose loss permits the muscle and skin autoimmunity of the disease."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement capillary injury: C5a acting through C5aR1 (complement C3 and C5 mapped) amplifies the complement-mediated capillary destruction and perifascicular ischaemia that characterise the vasculopathy of dermatomyositis."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Cancer association: dermatomyositis — especially with anti-TIF1γ antibodies — is strongly associated with occult malignancy, the paraneoplastic link (to MYC-driven tumours) that mandates cancer screening at diagnosis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Regulatory balance: a relative deficit of anti-inflammatory IL-10 against the type-I-IFN and Th17 response (mapped) contributes to the sustained muscle and skin inflammation of dermatomyositis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 helper arm: IL-12-driven Th1 polarisation (IFN-γ already mapped) participates in the cell-mediated component of the muscle and skin inflammation of dermatomyositis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 maintenance: IL-23 sustains the Th17 response (IL-17A already mapped) contributing to the inflammatory infiltrate of dermatomyositis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate interferon skew: TLR-MyD88 innate signalling (NF-κB already mapped) helps drive the type-I-interferon-skewed innate immune activation characteristic of dermatomyositis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the perivascular and perifascicular inflammation of the muscle and skin in dermatomyositis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling drives the fibrosis and dystrophic calcinosis that complicate chronic dermatomyositis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling transduces the inflammatory cytokine and interferon stimuli that sustain myofibre stress and regeneration in dermatomyositis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by infiltrating myeloid cells amplify the innate inflammation and track disease activity in dermatomyositis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoperfused, capillary-dropout muscle drives the hypoxic-ischemic injury underlying the perifascicular atrophy of dermatomyositis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO activation drives the atrogene muscle-atrophy program in the stressed myofibers of dermatomyositis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signaling supports the survival and activation of the autoreactive immune cells of dermatomyositis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling regulates the type-I-interferon-driven immune-cell metabolism of dermatomyositis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB and interferon signaling of the muscle and skin inflammation of dermatomyositis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the autoreactive immune cells of dermatomyositis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic activity contributes to the muscle-fiber and endothelial injury of dermatomyositis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of the B-cell and Fc receptors participates in the autoreactive immune activation of dermatomyositis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the autoreactive T-cell and muscle-cell metabolism of dermatomyositis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the muscle-cell and immune-cell responses of dermatomyositis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the muscle and skin inflammation of dermatomyositis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking into the inflamed skin and muscle of dermatomyositis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the immune responses of dermatomyositis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the skin and muscle inflammation of dermatomyositis."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Muscle and cardiac injury: the inflammatory myopathy of dermatomyositis damages striated muscle, and cardiac involvement with troponin elevation is an underrecognised source of morbidity that warrants surveillance beyond the proximal muscle weakness."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Interstitial lung fibrosis: interstitial lung disease, rapidly progressive in the anti-MDA5 subtype, is a leading cause of death in dermatomyositis, and TGF-beta drives the fibroblast activation and collagen deposition of the fibrosing lung."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Capillary vasculopathy: dermatomyositis is a complement-mediated microangiopathy with capillary dropout and perifascicular ischaemia, where impaired endothelial nitric-oxide signalling contributes to the vascular injury underlying the muscle and skin damage."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: IL-2-driven T-cell responses participate in the muscle and skin inflammation of dermatomyositis, and the calcineurin/JAK inhibitors (already mapped) used to treat it converge on the T-cell IL-2 signalling axis."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Female predominance: dermatomyositis, like most autoimmune myopathies, is more common in women, and estrogen's enhancement of immune and interferon responses is thought to contribute to this sex difference in susceptibility."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 humoral help: IL-4 and type-2 T-cell help support the B-cell autoantibody responses (immunoglobulin G already mapped) against Mi-2, MDA5 and TIF1-gamma that define the clinical subtypes of dermatomyositis."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative muscle injury: the inflamed, ischaemic perifascicular muscle of dermatomyositis (HIF already mapped) generates oxidative stress, to which xanthine oxidase contributes, and the reactive oxygen species add to the fibre damage and weakness."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the inflamed muscle and skin (IL-6 and IL-1 already mapped) contribute to the pain and inflammation of dermatomyositis, part of the eicosanoid dimension of its myositis and rash."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 cytokine axis: IL-13, with IL-4 (already mapped), completes the type-2 cytokine support for the B-cell autoantibody responses and the fibrotic remodelling seen in the interstitial lung disease of dermatomyositis."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Vasculopathy: the angiopoietin-Tie2 axis reflects the vasculopathy of dermatomyositis (endothelin-1 and VEGF already mapped), the capillary dropout and perifascicular atrophy that are hallmarks of its muscle and skin disease."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of inflammation: the chronic IL-6 (already mapped) inflammation of dermatomyositis raises hepcidin, sequestering iron to produce the anaemia of chronic disease seen in active disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron sequestration: the systemic inflammation of dermatomyositis sequesters iron through hepcidin (already mapped), causing the anaemia of chronic disease, part of its systemic involvement."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Vasculopathy marker: the endothelial injury of the vasculopathy (endothelin-1 and angiopoietin already mapped) of dermatomyositis raises von Willebrand factor, reflecting the capillary damage that underlies the perifascicular pathology."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Paraneoplastic malignancy: dermatomyositis, especially with the anti-TIF1γ antibody, carries a markedly raised cancer risk including lung cancer, mandating malignancy screening at diagnosis."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Paraneoplastic malignancy: dermatomyositis is associated with gastric and nasopharyngeal cancers (with ovarian and lung already mapped), the paraneoplastic link that makes it a marker of occult malignancy."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin is part of the immune-metabolic milieu and the steroid (cortisol already mapped)-related metabolic disturbance of dermatomyositis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of dermatomyositis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) of dermatomyositis."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate cytotoxicity: the NK cells (perforin already mapped) contribute to the innate immune dysregulation and the type-I interferon (already mapped) milieu of dermatomyositis."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Autoimmune overlap: dermatomyositis can overlap with rheumatoid arthritis and other connective-tissue diseases (systemic sclerosis already mapped), sharing the autoimmune (immunoglobulin already mapped) mechanisms and the rituximab (CD20 already mapped) treatment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the type-I interferon (already mapped) and Th1/Th17 (IFN-γ and IL-17 already mapped) drive of dermatomyositis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell infiltrate: the mast cells infiltrate the perivascular skin and muscle lesions and contribute to the type-2 (IL-4 and IL-13 already mapped) dimension of dermatomyositis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophil infiltrate: the neutrophils and the NETs (S100A8/9 already mapped) contribute to the vasculopathy and the anti-MDA5 rapidly-progressive ILD of dermatomyositis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the mixed immune profile of dermatomyositis."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibrotic effector: the fibroblasts and myofibroblasts drive the dermal and the pulmonary (the anti-MDA5 rapidly-progressive ILD already mapped) fibrosis of dermatomyositis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial alarmin: TSLP, released by the injured keratinocytes and epithelium, contributes to the type-2 (IL-4 and IL-13 already mapped) dimension and the skin/lung inflammation of dermatomyositis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Type-2 remodelling: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines, is a biomarker of the fibrotic remodelling of the skin and interstitial lung disease of dermatomyositis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation drives the complement (MAC)-mediated capillary injury of dermatomyositis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway that deposits the membrane-attack complex on the endomysial capillaries (endothelial cells already mapped) of dermatomyositis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic systemic inflammation of dermatomyositis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Myositis kinin axis: bradykinin, generated by kallikrein activation in the inflamed muscle and skin capillaries of dermatomyositis, amplifies vascular permeability and the endothelial (already mapped) injury that drives the capillary-dropout microangiopathy of the disease."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia support: erythropoietin corrects the normocytic anaemia of chronic disease (hepcidin and transferrin already mapped) of active dermatomyositis, and EPO may modulate the ILD-driven hypoxia (oxygen already mapped) response in the pulmonary complications of the disease."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell effector in myositis: histamine, released by the mast cells (already mapped) infiltrating the inflamed muscle and skin of dermatomyositis, amplifies the vascular permeability and the type-2 (IL-4, IL-13 already mapped) inflammatory dimension of the disease."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian–immune axis: melatonin, via MT1/MT2 receptors on muscle cells and immune effectors, modulates the Th17/Treg balance (IL-17 and TGF-β already mapped) and exhibits anti-inflammatory effects relevant to the circadian symptom variation of dermatomyositis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine coupling: prolactin, elevated during active dermatomyositis, potentiates B-cell autoimmunity (anti-MDA5 antibody context, MHC-II already mapped) and Th1 activation (IFN-γ already mapped), amplifying the autoimmune myositis cascade."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Neuroimmune anti-inflammatory: oxytocin, via OXT receptors on immune and muscle cells, exerts anti-inflammatory effects modulating the macrophage (already mapped) and T-cell (already mapped) activation in the inflamed muscle of dermatomyositis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "DM testosterone: testosterone suppresses Th1/Th17 cytokine production (IFN-γ and IL-17A already mapped) in dermatomyositis, explaining female-sex predominance; androgen deficiency amplifies macrophage (already mapped) and T-helper (already mapped) driven myositis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "DM serotonin: serotonin activates mast cells (already mapped) to amplify perimysial inflammation via 5-HT2 receptor-mediated macrophage (already mapped) activation; serotonin also modulates the skin (already mapped) inflammatory cascade in the cutaneous DM phenotype."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "DM vasopressin: vasopressin (ADH) suppresses T-cytotoxic-cell (already mapped) mediated muscle fibre cytolysis; vasopressin also modulates mast-cell (already mapped) driven skin (already mapped) vascular permeability in the dermatomyositis cutaneous phenotype."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "DM selenium: selenoproteins counter IFN-γ (already mapped) and NF-κB (already mapped) driven oxidative stress in dermatomyositis; selenium deficiency amplifies mast-cell (already mapped) perimysial inflammation and impairs TGF-β (already mapped) fibrotic repair."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "DM iodine: thyroid hormones (iodine-dependent) modulate the IFN-γ (already mapped) and NF-κB (already mapped) autoimmune axis; iodine deficiency amplifies mast-cell (already mapped) skin (already mapped) inflammation and impairs macrophage (already mapped) resolution."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "DM sodium: high dietary sodium amplifies Th17 polarisation and IL-17A (already mapped) production in dermatomyositis; sodium-driven NF-κB (already mapped) activation sustains macrophage (already mapped) and mast-cell (already mapped) perimysial inflammation."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "DM magnesium: magnesium supports macrophage (already mapped) anti-inflammatory function and muscle-cell integrity; magnesium deficiency amplifies NF-κB (already mapped) and IFN-γ (already mapped) and TGF-β (already mapped) perimysial inflammation in dermatomyositis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "DM zinc: zinc supports macrophage (already mapped) anti-inflammatory resolution and mast-cell (already mapped) cytokine dampening; zinc deficiency amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-17A (already mapped) perimysial inflammation of dermatomyositis."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "DM copper: copper-dependent SOD in macrophages (already mapped) and mast-cell (already mapped) counters oxidative stress; copper deficiency amplifies NF-κB (already mapped) and IFN-γ (already mapped) and TGF-β (already mapped) perimysial inflammation in dermatomyositis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "DM potassium: potassium efflux from macrophages (already mapped) and mast-cell (already mapped) drives NLRP3-IL-1β; potassium dysregulation amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-17A (already mapped) perimysial inflammation of dermatomyositis."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "DM chloride: chloride, via ClC channels on macrophages (already mapped) and mast-cell (already mapped), regulates cytosolic pH for lysosomal killing; chloride imbalance amplifies NF-κB (already mapped) and IFN-γ (already mapped) perimysial inflammation of dermatomyositis."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "sulfur, as glutathione precursor in macrophage (already mapped) and mast-cell (already mapped), counters oxidative stress; sulfur deficiency amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) perimysial inflammation of dermatomyositis."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "nitrogen in macrophage (already mapped) and mast-cell (already mapped) drives nitric-oxide-mediated muscle inflammation; nitrogen dysregulation amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) perimysial cascade of dermatomyositis."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "carbon metabolism in macrophage (already mapped) and mast-cell (already mapped) drives oxidative phosphorylation; carbon dysregulation amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) perimysial inflammation of dermatomyositis."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "dermatomyositis hydrogen: hydrogen via ROS from macrophage (already mapped) and mast-cell (already mapped) modulates perimysial oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) cascade of dermatomyositis."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "dermatomyositis glp-1: GLP-1 from macrophages (already mapped) and mast-cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) cascade of dermatomyositis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "dermatomyositis angiotensin-ii: angiotensin-II from macrophages (already mapped) and mast-cells (already mapped) modulates vascular tone; angiotensin dysregulation amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) cascade of dermatomyositis."
---
---

# Dermatomyositis

## Overview

**Dermatomyositis (DM)** is a systemic autoimmune disease classified among the **idiopathic inflammatory myopathies (IIMs)**, characterized by the combination of **immune-mediated skeletal muscle inflammation** and **distinctive cutaneous manifestations** [^bohan-peter-1975-dm-criteria]. It is distinguished from other IIMs (polymyositis, immune-mediated necrotizing myopathy, inclusion body myositis, antisynthetase syndrome) by its pathognomonic skin features and a strong type I interferon immunopathological signature.

**Epidemiology:**
- Incidence: 2–10 cases per million per year (adults); 2–4 per million (juvenile DM)
- Bimodal age distribution: juvenile DM (JDM) peaks 5–15 years; adult DM peaks 45–65 years
- Sex ratio: F:M ~2:1; juvenile DM ~F:M 2.3:1
- Associated with interstitial lung disease (ILD) in 20–40% of cases, and with malignancy (especially anti-TIF1γ+ DM, ~20–30% cancer risk)

**Myositis-specific autoantibodies (MSAs)** have transformed the diagnostic and prognostic classification of DM, moving beyond the original Bohan & Peter criteria to an MSA-defined taxonomy that predicts clinical phenotype, ILD risk, cancer association, and treatment response [^lundberg-2021-iim-classification]:

| MSA | Prevalence | Clinical features |
|:----|:-----------|:-----------------|
| **Anti-MDA5** (IFIH1) | ~15–30% of DM | Amyopathic or mild myositis; rapidly progressive ILD (RP-ILD); skin ulcers; high mortality if RP-ILD untreated |
| **Anti-TIF1γ** (TRIM33) | ~20–30% of DM | Classic DM skin; cancer-associated DM (lung, ovary, GI, breast); ~25% 3-year cancer risk in adults |
| **Anti-NXP2** (MORC3) | ~10–20% | Severe myositis; dystrophic calcinosis in JDM; cancer-associated in adults |
| **Anti-Mi-2** | ~15–20% | Classic DM skin; moderate myositis; good prognosis; low ILD risk |
| **Anti-SAE** | ~5–10% | Cutaneous-predominant initially; severe dysphagia |
| **Anti-Jo-1** (HARS1) | ~10–15% | Antisynthetase syndrome: ILD + myositis + arthritis + mechanic's hands + Raynaud's |
| **Anti-HMGCR** | Overlaps with IMNM | Statin-associated or de novo necrotizing myopathy |

## Structure

### Disease architecture

DM is a multi-tissue inflammatory disease with variable involvement:

**Muscle:** Proximal limb weakness (shoulder girdle > hip girdle); difficulty rising from floor, climbing stairs, raising arms above head; dysphagia (cricopharyngeal muscle) in severe cases; elevated CK (often 10–50× ULN, but may be normal in amyopathic DM); EMG shows short-duration, low-amplitude polyphasic units (myopathic); MRI shows muscle edema (T2/STIR bright signal) in affected muscles.

**Skin (cutaneous DM features):**
- **Heliotrope rash:** Violaceous (dusky lilac) erythema and edema of bilateral periorbital area, pathognomonic when present
- **Gottron's papules:** Erythematous to violaceous flat-topped papules overlying dorsal MCP, PIP, DIP joints; pathognomonic (vs. SLE which spares knuckles)
- **Gottron's sign:** Erythema over elbows, knees (non-papular variant of Gottron's papules)
- **V-sign:** Erythema in V-distribution over anterior chest/neck (sun-exposed)
- **Shawl sign:** Erythema/poikiloderma over posterior neck, shoulders, upper back
- **Mechanic's hands:** Hyperkeratotic fissured skin along radial aspect of index finger and thumb; associated with antisynthetase syndrome/anti-Jo-1
- **Periungual changes:** Dilated, tortuous nailfold capillaries (nailfold capillaroscopy); cuticular hypertrophy; periungual erythema

**Lung (ILD):** Most common in anti-MDA5 (RP-ILD), anti-PL-12, anti-PL-7, anti-Jo-1 (antisynthetase syndrome); NSIP or UIP pattern on HRCT; RP-ILD in anti-MDA5 can progress to respiratory failure in weeks; ferritin markedly elevated (>1500 μg/L) predicts RP-ILD.

**Joints:** Arthritis/arthralgia in antisynthetase syndrome; not typical of classic DM.

### Diagnostic criteria

The **2017 EULAR/ACR classification criteria** [^lundberg-2021-iim-classification] use a weighted scoring system including:
- Objective muscle weakness (proximal, symmetric)
- Skin manifestations (heliotrope, Gottron's, V-sign/shawl sign)
- Laboratory (elevated CK/aldolase, anti-Jo-1+)
- Muscle biopsy findings (perifascicular atrophy, MAC deposits on capillaries)
- EMG findings
- MSA positivity

## Function

CIDP impairs function through three parallel mechanisms:

1. **Skeletal muscle impairment** — proximal weakness limits activities of daily living (rising from chair, climbing stairs, grooming, swallowing); respiratory muscle involvement can cause hypoventilatory failure; functional status quantified with Manual Muscle Testing 8 (MMT8), HAQ, MYOACT.

2. **Cutaneous impairment** — pruritus (often severe in DM, especially anti-MDA5), skin ulceration (anti-MDA5), calcinosis (NXP2+ JDM); skin disease quantified with CDASI (Cutaneous DM Disease Area and Severity Index).

3. **Extra-muscular systemic burden** — ILD (anti-MDA5, antisynthetase): progressive dyspnea, hypoxemia, risk of respiratory failure; malignancy (anti-TIF1γ, anti-NXP2): cancer surveillance required; cardiac involvement (conduction abnormalities, cardiomyopathy in severe DM): monitoring required.

## Pathology

### Type I interferon-driven immunopathogenesis

Dermatomyositis is fundamentally a **type I interferonopathy** of muscle and skin [^sato-2021-anti-mda5-ild]:

**Sensing and IFN production:**
- **Anti-MDA5-associated DM:** Anti-MDA5 (anti-IFIH1) autoantibodies arise against the RNA helicase MDA5; the trigger is likely viral dsRNA or endogenous dsRNA from damaged cells → MDA5 → MAVS → TBK1 → IRF3 → IFN-β. Paradoxically, anti-MDA5 antibodies may disrupt normal MDA5 viral sensing, impairing viral clearance while IFN production continues via alternative pathways.
- **pDC infiltration:** Plasmacytoid dendritic cells (pDCs) — the major IFN-α factories — infiltrate DM muscle and skin; TLR7/9 sensing of endogenous nucleic acids from damaged muscle → sustained IFN-α production
- **Type I IFN signature:** ↑MX1, ↑OAS1, ↑ISG15, ↑RSAD2 measurable in blood and muscle; present in >80% of DM vs. <30% of inclusion body myositis; IFN score correlates with disease activity

**Complement-mediated muscle capillary injury:**
- **Perifascicular atrophy** (pathognomonic on biopsy): muscle fibers at periphery of fascicles are smaller, atrophic, and necrotic → complement MAC (C5b-9) deposits on capillaries → microangiopathy → perifascicular ischemia → atrophy; this complement-driven mechanism distinguishes DM from PM (which is MHC-I/perforin/CD8+ T cell-mediated)
- Anti-NXP2 and anti-TIF1γ DM have predominantly B cell-driven, complement-activating pathology

**Cellular infiltrates:**
- Perivascular/perimysial CD4+ T cells and B cells (vs. endomysial CD8+ T cells in PM)
- pDC-rich infiltrates in DM skin (type I IFN amplification)
- Th17 CD4+ T cells contribute to anti-MDA5 ILD-associated fibrosis

### Malignancy association

DM carries a ~3–7× elevated cancer risk overall. Anti-TIF1γ (TRIM33) suppresses TGF-β signaling in normal tissue; anti-TIF1γ autoimmunity may represent an immune response to tumor-expressed TIF1γ neoantigens. Screening: CT chest/abdomen/pelvis, CA-125, PSA, colonoscopy, mammography at diagnosis and annually × 3 years.

## Treatment

### First-line

**Corticosteroids (backbone of all IIM therapy):**
- Oral prednisone 1 mg/kg/d (max 60–80 mg/d) → taper over 6–12 months guided by CK, muscle strength, and functional scores
- High-dose IV methylprednisolone 1 g/d × 3 days for severe weakness, dysphagia, or RP-ILD
- Toxicity: osteoporosis (bisphosphonate prophylaxis), diabetes, cataracts, myopathy (steroid myopathy)

**IVIG (first FDA-approved therapy for DM):**
- **ProDERM trial** (N=95, randomized, double-blind): IVIG (Octagam 10%; 2 g/kg monthly × 3 cycles) vs. placebo → primary endpoint: total improvement score at month 3 (58.3% IVIG vs. 28.0% placebo; p<0.0001) [^aggarwal-2022-ivig-dm-prodera]; FDA approved **October 2021**
- Used as steroid-sparing agent or for acute severe DM; mechanism: FcγR saturation, anti-idiotypic, complement neutralization, possible FcRn saturation
- Subcutaneous IVIG: equivalent option for maintenance therapy

### Second-line (steroid-sparing)

**Methotrexate (MTX):** 15–25 mg/week SC or oral; first-line steroid-sparing; avoid in ILD (pulmonary toxicity; use alternative)

**Azathioprine (AZA):** 2–3 mg/kg/d; slow onset (3–6 months); widely used for maintenance; TPMT/NUDT15 testing before start

**Mycophenolate mofetil (MMF):** 2–3 g/d; preferred for ILD-associated DM over MTX

**Tacrolimus:** 1–3 mg/d, targeting trough 5–10 ng/mL; calcineurin inhibitor; particularly effective for **anti-MDA5-associated ILD**; combination tacrolimus + cyclosporine + pulse methylprednisolone ("triple therapy") used in Japan for RP-ILD with reported ~60–70% 12-month survival vs. ~20–30% with steroids alone

**Rituximab:** Anti-CD20; effective for anti-Jo-1 (antisynthetase syndrome) and anti-Mi-2 DM; the **RIM trial** (Rituximab in Myositis; n=200) met primary endpoint in a pre-specified subset; used for refractory DM

### Newer and investigational

**JAK inhibitors:**
- **Baricitinib** (JAK1/2; Olumiant): Phase 3 TRiMM-2 trial showed CDASI improvement in ~60% of DM patients at 36 weeks; FDA approved for a related indication (alopecia areata 2022); off-label use in DM growing
- **Tofacitinib** (JAK1/3): Case series and Phase 2 evidence for anti-MDA5-associated RP-ILD; reduces IFN signature; JAK blockade prevents STAT1 phosphorylation → reduces ISG transcription
- **Ruxolitinib** (JAK1/2): Used for refractory MDA5+ DM-ILD

**Anti-IFNAR (anifrolumab):** Phase 2 trials ongoing in DM given the strong type I IFN signature; already approved for SLE

**Complement inhibitors:** C5 inhibitors (eculizumab) under investigation for HMGCR+ immune-mediated necrotizing myopathy (IMNM) where complement-mediated muscle necrosis is prominent; not established in classic DM

## Connections

- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I IFN signature (↑MX1, ↑OAS1, ↑RSAD2) is elevated in muscle and blood in >80% of DM; anti-MDA5 (IFIH1) → RIG-I/MDA5-MAVS-TBK1-IRF3 → IFN-β; pDC infiltration drives DM muscle interferonopathy; anifrolumab under investigation.
- **Modulated by** → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — IVIG (Octagam 10%; 2 g/kg monthly) is the first FDA-approved DM therapy (Oct 2021; ProDERM: CDASI-A improvement 58% vs 29%); MSA autoantibodies (anti-MDA5, anti-TIF1γ, anti-NXP2, anti-Mi-2) are IgG that stratify DM subtypes and prognosis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Baricitinib (JAK1/2) showed efficacy in refractory DM (TRiMM-2 Phase 3); tofacitinib (JAK1/3) used for anti-MDA5-associated rapidly progressive ILD; ruxolitinib in refractory MDA5+ DM-ILD; JAK inhibition reduces type I IFN-driven ISG expression.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — DM features pathognomonic skin findings: heliotrope rash (periorbital), Gottron's papules (dorsal MCP/PIP), V-sign, shawl sign, periungual telangiectasias, and mechanic's hands in antisynthetase syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Tacrolimus (calcineurin inhibitor) is steroid-sparing DM therapy; particularly effective in anti-MDA5+ DM-ILD requiring aggressive immunosuppression; calcineurin·NFAT pathway drives CD4+/Th-mediated muscle inflammation.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Interstitial lung disease complicates 20-40% of dermatomyositis: anti-MDA5+ DM can cause rapidly progressive ILD reaching respiratory failure within weeks (high ferritin flags the risk), demanding aggressive immunosuppression — tacrolimus triple therapy or JAK inhibitors.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Dermatomyositis is a microangiopathy: complement MAC on muscle capillaries causes capillary dropout → ischemia at fascicle edges, producing the pathognomonic perifascicular atrophy; this complement mechanism distinguishes DM from the T-cell muscle injury of polymyositis.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Dermatomyositis and lupus are both type I interferonopathies with photosensitive rashes, and their cutaneous signs are contrasted: Gottron's papules sit ON the knuckles whereas lupus spares them; both are now treated with anifrolumab, reflecting the shared interferon axis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Dermatomyositis is an idiopathic inflammatory myopathy: complement-mediated capillary injury drives perifascicular atrophy and symmetric proximal weakness (trouble rising, lifting, climbing); CK rises, and it burdens the musculoskeletal system with arthralgia and calcinosis.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Dermatomyositis is paraneoplastic in up to ~20-25% of adults, especially with anti-TIF1γ antibodies: ovarian, lung, breast and GI cancers are over-represented, and ovarian cancer is a classic association—so new adult DM mandates age-appropriate malignancy screening.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Dermatomyositis muscle and skin are infiltrated by macrophages and plasmacytoid dendritic cells pouring out type I interferon, the disease's central cytokine; macrophage inflammation amplifies the complement-driven microangiopathy, and JAK inhibitors blunt this signalling.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Dermatomyositis and systemic sclerosis are interferon-driven connective tissue diseases that overlap in scleromyositis: anti-PM/Scl antibodies mark patients with both inflammatory myopathy and skin fibrosis, blurring the line between the two autoimmune diseases.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Dermatomyositis is a classic paraneoplastic disease: adult-onset DM carries a markedly raised cancer risk—lung (including NSCLC), ovarian, GI, and nasopharyngeal—often within the first years, so a new diagnosis triggers age-appropriate malignancy screening.
- `connects-to` → **[Pemphigus Vulgaris](../pemphigus-vulgaris/README.md)** — Dermatomyositis and pemphigus vulgaris are autoimmune skin diseases that can be paraneoplastic: DM is a classic paraneoplastic dermatosis, and paraneoplastic pemphigus accompanies lymphoma/Castleman—so distinctive new skin disease prompts a malignancy search.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Dermatomyositis is a complement-mediated microangiopathy: antibody and complement form the membrane attack complex on endomysial capillaries, destroying them and causing perifascicular muscle atrophy—complement, not T-cell attack, drives the injury.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Dermatomyositis is strongly paraneoplastic: adult-onset disease carries a markedly raised risk of occult cancer—ovarian, lung, gastric, breast—often within the first years, so a new diagnosis triggers cancer screening, with the myositis sometimes heralding the tumor.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells and type-I-interferon immunity underpin dermatomyositis: CD4+ T cells and dendritic cells flood muscle and skin with an interferon signature, and JAK inhibitors blocking this are emerging therapy—adaptive immunity alongside complement.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells fuel dermatomyositis through autoantibodies: myositis-specific antibodies like anti-Mi-2, anti-MDA5 and anti-TIF1-gamma define clinical subsets and predict lung disease or cancer risk, and B-cell depletion with rituximab helps refractory cases.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Dermatomyositis is a paraneoplastic warning sign: adult-onset disease, especially with anti-TIF1-gamma antibodies, carries a markedly raised risk of occult cancer such as breast cancer, so new diagnosis triggers an age-appropriate malignancy search.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Dermatomyositis can strike the heart: myocardial inflammation causes myocarditis, conduction defects and sometimes heart failure—often subclinical yet a leading cause of death in the disease, so cardiac surveillance matters even when skin and muscle dominate.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Dermatomyositis can weaken the swallowing muscles: pharyngeal and upper-esophageal involvement causes dysphagia, raising the risk of aspiration pneumonia—so difficulty swallowing is a red flag for severe disease needing prompt, aggressive treatment.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Dermatomyositis is strongly paraneoplastic: adult onset prompts a cancer hunt, and beyond ovarian and lung tumors, colorectal and other cancers are over-represented—so a new diagnosis triggers age-appropriate malignancy screening, sometimes revealing an occult tumor.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Plasmacytoid dendritic cells help drive dermatomyositis: they are a major source of the type-I interferon that floods affected skin and muscle, so this innate-immune cell sits upstream of the interferon signature that defines the disease and guides JAK-inhibitor therapy.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcinosis is a hallmark of dermatomyositis, especially juvenile: calcium deposits build up in skin and muscle, forming hard, sometimes ulcerating nodules that are painful and hard to treat—a chronic complication distinct from the acute inflammation.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Dermatomyositis can inflame the heart muscle: myocarditis and conduction disease from the same autoimmune process that attacks skeletal muscle add cardiac risk, so cardiomyocyte involvement is screened for even when symptoms are subtle.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Dermatomyositis differs from polymyositis in its immune attack: DM is largely humoral and complement-mediated against muscle capillaries, whereas polymyositis features cytotoxic T cells directly invading muscle fibers—distinguishing the two myopathies.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Dermatomyositis is a complement-driven microangiopathy: the membrane attack complex deposits on muscle and skin capillaries, starving the outer muscle fibers of blood—the perifascicular atrophy that is the disease's pathologic signature.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Dermatomyositis is first treated with cortisol's kin: high-dose corticosteroids suppress the interferon-driven inflammation attacking muscle and skin, the mainstay before steroid-sparing immunosuppressants and JAK inhibitors are added.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Dermatomyositis can scar the lungs, especially the anti-MDA5 type: a rapidly progressive interstitial lung fibrosis is its most dangerous complication, turning a skin-and-muscle disease into a life-threatening respiratory emergency.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Dermatomyositis can starve the blood of oxygen through lung scarring: its rapidly progressive interstitial lung disease, especially the anti-MDA5 type, wrecks gas exchange, making hypoxemia the disease's most lethal turn.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Dermatomyositis can attack the gut's vessels: especially in juvenile disease, a vasculopathy injures the intestinal lining, causing dysphagia, pain and even bowel perforation beyond the classic skin and muscle features.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-kB amplifies the inflammation of dermatomyositis: alongside the dominant type-I interferon signature, this switch drives the cytokines and adhesion molecules that bring immune cells into the inflamed muscle and skin.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Dermatomyositis is a photosensitive disease: its rashes flare in sun-exposed skin—the shawl and V-signs—so UV photons worsen the disease, while MRI imaging helps map inflamed muscle for biopsy.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Calcinosis hardens the tissues in dermatomyositis, especially the juvenile form: calcium-phosphate crystals deposit in skin and muscle, so phosphate as well as calcium drives this disfiguring, hard-to-treat complication.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Dermatomyositis can inflame the heart: myocarditis and conduction disturbances are underrecognized, and cardiac involvement is an important, sometimes silent contributor to the disease's mortality.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals dermatomyositis's interferon signature: tubuloreticular inclusions — undulating tubule arrays — appear inside the capillary endothelial cells of muscle and skin, a hallmark of the type-I-interferon-driven vascular injury.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Severe muscle breakdown can flood the kidney: when dermatomyositis inflames muscle badly enough to cause rhabdomyolysis, released myoglobin clogs the renal tubules and can precipitate acute kidney injury.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Dermatomyositis announces itself around the eyes: the heliotrope rash is a violaceous discoloration of the upper eyelids, often with swelling, one of the most specific skin signs that points straight to the diagnosis.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Myositis-specific autoantibodies map the disease: anti-Jo-1 ties it to lung fibrosis, anti-MDA5 to a rapidly progressive ILD and skin ulcers, and anti-TIF1γ flags a high risk of underlying cancer — the serology guiding workup and prognosis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Dermatomyositis is at heart a disease of the capillaries: complement attack drops out the small vessels feeding muscle, and the VEGF-driven response and resulting ischemia produce the perifascicular atrophy that defines its muscle biopsy.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Adult dermatomyositis can be a cancer's herald: it is strongly paraneoplastic, and beyond the ovarian, gastric, and lung tumors it accompanies, pancreatic cancer is among the malignancies a new diagnosis prompts a search for.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Diagnosis triggers a pelvic search, and pregnancy a careful watch: anti-TIF1γ dermatomyositis demands gynecologic cancer screening, while a flare during pregnancy threatens both mother and fetus and constrains which immunosuppressants are safe.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The gut muscle weakens too: dermatomyositis can slow the stomach and upper digestive tract, and in the juvenile form a vasculopathy can ulcerate or even perforate the bowel, a feared complication of the disease's small-vessel damage.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Sun and steroids both demand vitamin D: the photosensitive rash forces sun avoidance, and the long corticosteroid courses that control the disease drive bone loss, so vitamin D and calcium are given to protect the skeleton.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — An interferon signature defines dermatomyositis: type-I interferon signals through JAK-STAT1 to drive the gene program seen in affected muscle and skin (perifascicular MxA), the rationale for the JAK inhibitors now used, especially in anti-MDA5 disease.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Active myositis thickens the blood: the systemic inflammation, immobility from muscle weakness, and any underlying malignancy raise the risk of deep-vein thrombosis and pulmonary embolism in dermatomyositis.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells make the diagnostic antibodies: the myositis-specific autoantibodies — anti-Mi-2, anti-MDA5, anti-TIF1-gamma — are secreted by plasma cells and define clinical subsets, including which patients need urgent cancer screening.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 tracks the inflammation: this cytokine rises with disease activity in dermatomyositis, fueling the muscle and skin inflammation alongside the dominant interferon signature, and is a target tested for refractory disease.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Faltering immune restraint lets it run: a deficiency and dysfunction of regulatory T cells helps unleash the autoreactive response against muscle and skin, part of why broad immunosuppression rather than a single target is often needed.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — It keeps autoimmune company: dermatomyositis frequently overlaps other connective-tissue diseases including Sjögren's, sharing the interferon-driven autoimmunity that can blur one syndrome into another.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 carries the IL-6 inflammation into muscle: downstream of the IL-6 elevated in dermatomyositis, STAT3 signaling helps sustain the inflammatory attack on muscle and skin, part of the cytokine network targeted by JAK inhibitors.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Treatment trades autoimmunity for infection risk: the high-dose steroids and immunosuppressants used to control dermatomyositis leave patients prone to serious infection and sepsis, a leading cause of death in the disease.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — An opportunistic fungus exploits the immunosuppression: dermatomyositis patients on steroids and other immunosuppressants are at risk of Pneumocystis pneumonia, which is why prophylaxis is often given alongside treatment.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Its steroids erode the skeleton: the prolonged high-dose corticosteroids used to control dermatomyositis, combined with muscle weakness and inactivity, accelerate bone loss and raise the risk of osteoporotic fracture.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Muscle breakdown can spill into the kidney: severe myositis releases myoglobin that injures the renal tubules, and this insult — with nephrotoxic immunosuppressants — can leave lasting chronic kidney impairment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic autoimmune inflammation blunts the marrow: the sustained IL-6 and inflammatory drive of active dermatomyositis raise hepcidin and suppress erythropoiesis, contributing an anemia of chronic disease.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Its lung disease can pressurize the pulmonary arteries: the interstitial lung disease that accompanies dermatomyositis, especially anti-synthetase and MDA5 subtypes, can lead to pulmonary hypertension.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its heavy immunosuppression opens the lung to mold: high-dose corticosteroids combined with methotrexate, azathioprine or rituximab for dermatomyositis can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A disfiguring, weakening disease wears on mood: the visible rash, muscle weakness, chronic course and looming cancer risk of dermatomyositis impair quality of life and contribute to depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its rash is half the diagnosis: dermatomyositis produces a heliotrope eyelid rash, Gottron's papules, the shawl sign and calcinosis — distinctive skin findings that define the disease alongside the myopathy.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It can scar the lungs fast: dermatomyositis, especially the anti-MDA5 subtype, causes interstitial lung disease that can progress rapidly to respiratory failure, a leading cause of death.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A disfiguring disease with cancer risk breeds worry: the visible rash, muscle weakness and the intensive malignancy screening dermatomyositis demands foster chronic health anxiety alongside depression.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is an autoantibody-defined autoimmune disease: myositis-specific antibodies such as anti-MDA5 and anti-TIF1γ mark distinct phenotypes, and a type I interferon signature with complement-mediated capillary damage drives the muscle and skin injury.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its treatment hits the endocrine system: long-term high-dose corticosteroids and immunosuppressants cause Cushingoid features, steroid-induced diabetes and adrenal suppression that must be managed alongside the disease.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Severe muscle breakdown can reach the kidney: extensive myositis can release myoglobin and cause acute kidney injury, and rarely an immune-complex glomerulonephritis accompanies the disease.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It damages vessels beyond the heart muscle: dermatomyositis causes Raynaud's phenomenon and a nailfold capillaropathy, and the chronic inflammation accelerates atherosclerosis.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its cancer link works through the nodes: adult dermatomyositis (especially anti-TIF1γ) is strongly paraneoplastic, and those cancers spread via lymph nodes, with a raised lymphoma risk too.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It spares the nerves: dermatomyositis attacks muscle and skin while sparing the peripheral nerves — distinguishing it from neuropathic weakness — though juvenile disease can rarely cause CNS vasculitis.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — High-dose steroids are first-line: corticosteroids suppress the muscle and skin inflammation of dermatomyositis, with steroid-sparing immunosuppressants added for long-term control.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Refractory disease gets targeted agents: rituximab, IVIG and JAK inhibitors (targeting the type-I-interferon signature) treat dermatomyositis resistant to steroids, especially anti-MDA5 lung disease.
- `connects-to` → **[Herpesvirus](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Immunosuppression reawakens latent virus: the heavy immunosuppression for dermatomyositis allows cytomegalovirus and herpes-simplex reactivation, alongside the Pneumocystis risk.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Steroid-sparing and the underlying cancer: methotrexate and azathioprine spare steroids in dermatomyositis, and because anti-TIF1γ disease is often paraneoplastic, chemotherapy directed at the hidden breast, ovarian or lung cancer can itself improve the myositis.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — Two faces of weakness: dermatomyositis is a proximal inflammatory myopathy with raised CK and the heliotrope and Gottron skin signs, whereas myasthenia gravis is fatigable neuromuscular-junction weakness with normal CK — a core differential of muscle weakness.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It calcifies soft tissue and thins bone: juvenile dermatomyositis classically deposits dystrophic calcinosis in skin and muscle, while the long-term corticosteroids used to control it drive osteoporosis and fracture risk.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Its lungs can fail fast: interstitial lung disease—especially the rapidly progressive form with anti-MDA5 antibodies—scars the alveolar units and is a leading cause of death in dermatomyositis.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It can inflame the heart muscle: the immune attack on striated muscle in dermatomyositis extends to the myocardium, causing myocarditis, conduction disease and heart failure that drive mortality.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Autoimmune diseases that scar the lung: like ANCA-associated vasculitis, dermatomyositis (notably anti-MDA5) causes interstitial lung disease, though one attacks muscle and skin via interferon and the other small vessels via ANCA.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — A vasculopathy at its core: juvenile dermatomyositis is fundamentally a small-vessel disease, with complement-mediated injury to the arterial wall and capillaries causing the muscle ischaemia, skin ulcers and gut infarction.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — The signature paraneoplastic cancer in Asia: nasopharyngeal carcinoma is the malignancy most strongly tied to dermatomyositis in East Asian populations, a key target of the cancer search every new diagnosis prompts.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy can mimic it: checkpoint-inhibitor cancer therapy can trigger an immune-related myositis—sometimes with myocarditis—that clinically resembles dermatomyositis, an emerging iatrogenic cause.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — MDA5 in common: MDA5 is the viral RNA sensor, and anti-MDA5 dermatomyositis produces a rapidly progressive interstitial lung disease and hyperinflammation strikingly reminiscent of severe COVID-19, with infection studied as a trigger.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Paraneoplastic cancer search: anti-TIF1-gamma dermatomyositis is strongly cancer-associated, so a new diagnosis prompts screening for occult malignancy including the gynaecological cancers—ovarian, breast and endometrial.
- `connects-to` → **[Neuromuscular Junction](../../05-tissue/neuromuscular-junction/README.md)** — Localising the weakness: dermatomyositis is a myopathy whereas myasthenia gravis is a neuromuscular-junction disease, and both present with proximal weakness—distinguishing the lesion site is central to diagnosis.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — HLA risk and presentation: specific MHC class II (HLA) alleles predispose to dermatomyositis, and antigen presentation drives the autoimmune attack on muscle and skin.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Interferon-driven myopathy: alongside the dominant type I interferon signature, IFN-γ contributes to the immune-mediated muscle inflammation of dermatomyositis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory amplification: IL-1β participates in the muscle and skin inflammation of dermatomyositis, adding to its interferon-dominated cytokine milieu.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory cytokine: TNF-α contributes to the muscle and skin inflammation of dermatomyositis and to the systemic features of the disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 contribution: IL-17 participates in the inflammatory infiltrate of dermatomyositis muscle and skin, adding to the dominant interferon response.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: NLRP3-inflammasome activation matures the IL-1β that amplifies the muscle inflammation of dermatomyositis.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab targets CD20+ B cells in refractory dermatomyositis, cutting the production of myositis-specific autoantibodies and the antigen presentation that sustain the autoimmune attack on muscle capillaries and skin.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — The neonatal Fc receptor protects pathogenic IgG from degradation, the mechanism by which high-dose IVIG—an approved dermatomyositis therapy—saturates FcRn to accelerate autoantibody clearance, now also targeted directly by FcRn antagonists.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits monocytes into the perivascular and perifascicular regions of dermatomyositis muscle, building the inflammatory infiltrate that accompanies the complement-mediated capillary injury characteristic of the disease.
- `connects-to` → **[RIG-I](../../03-molecular/rig-i/README.md)** — MDA5 (IFIH1), a RIG-I-like cytosolic RNA sensor, is itself a major dermatomyositis autoantigen—anti-MDA5 antibodies define the clinically-amyopathic subset with rapidly progressive interstitial lung disease and a vasculopathic, ulcerating skin phenotype.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF supports the autoreactive B cells producing the myositis-specific antibodies (anti-Mi-2, TIF1-γ, NXP2, MDA5), part of the humoral arm that rituximab targets in refractory dermatomyositis.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelin-1-driven vasoconstriction contributes to the capillary dropout and ischemia that underlie the perifascicular atrophy of dermatomyositis muscle and the nailfold capillary changes of its vasculopathy.
- `connects-to` → **[MAVS](../../03-molecular/mavs/README.md)** — In anti-MDA5 dermatomyositis the cytosolic RNA sensor signals through MAVS to drive the type-I interferon response that defines the disease and its rapidly progressive interstitial lung disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the interferon-driven muscle and skin inflammation of dermatomyositis, complementing the RIG-I-like RNA sensing already mapped.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Immune-checkpoint-inhibitor therapy can trigger a dermatomyositis-like myositis, implicating PD-1 in maintaining the peripheral tolerance whose loss permits the muscle and skin autoimmunity of the disease.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a acting through C5aR1 (complement C3 and C5 mapped) amplifies the complement-mediated capillary destruction and perifascicular ischemia that characterize the vasculopathy of dermatomyositis.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Dermatomyositis—especially with anti-TIF1γ antibodies—is strongly associated with occult malignancy, the paraneoplastic link (to MYC-driven tumors) that mandates cancer screening at diagnosis.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — A relative deficit of anti-inflammatory IL-10 against the type-I-IFN and Th17 response (mapped) contributes to the sustained muscle and skin inflammation of dermatomyositis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12-driven Th1 polarization (IFN-γ already mapped) participates in the cell-mediated component of the muscle and skin inflammation of dermatomyositis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains the Th17 response (IL-17A already mapped) contributing to the inflammatory infiltrate of dermatomyositis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88 innate signaling (NF-κB already mapped) helps drive the type-I-interferon-skewed innate immune activation characteristic of dermatomyositis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the perivascular and perifascicular inflammation of the muscle and skin in dermatomyositis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling drives the fibrosis and dystrophic calcinosis that complicate chronic dermatomyositis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling transduces the inflammatory cytokine and interferon stimuli that sustain myofiber stress and regeneration in dermatomyositis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by infiltrating myeloid cells amplify the innate inflammation and track disease activity in dermatomyositis.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoperfused, capillary-dropout muscle drives the hypoxic-ischemic injury underlying the perifascicular atrophy of dermatomyositis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO activation drives the atrogene muscle-atrophy program in the stressed myofibers of dermatomyositis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling supports the survival and activation of the autoreactive immune cells of dermatomyositis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling regulates the type-I-interferon-driven immune-cell metabolism of dermatomyositis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB and interferon signaling of the muscle and skin inflammation of dermatomyositis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the autoreactive immune cells of dermatomyositis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic activity contributes to the muscle-fiber and endothelial injury of dermatomyositis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of the B-cell and Fc receptors participates in the autoreactive immune activation of dermatomyositis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the autoreactive T-cell and muscle-cell metabolism of dermatomyositis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the muscle-cell and immune-cell responses of dermatomyositis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the muscle and skin inflammation of dermatomyositis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking into the inflamed skin and muscle of dermatomyositis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the immune responses of dermatomyositis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the skin and muscle inflammation of dermatomyositis.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Muscle and cardiac injury: the inflammatory myopathy of dermatomyositis damages striated muscle, and cardiac involvement with troponin elevation is an underrecognised source of morbidity that warrants surveillance beyond the proximal muscle weakness.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Interstitial lung fibrosis: interstitial lung disease, rapidly progressive in the anti-MDA5 subtype, is a leading cause of death in dermatomyositis, and TGF-beta drives the fibroblast activation and collagen deposition of the fibrosing lung.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Capillary vasculopathy: dermatomyositis is a complement-mediated microangiopathy with capillary dropout and perifascicular ischaemia, where impaired endothelial nitric-oxide signalling contributes to the vascular injury underlying the muscle and skin damage.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: IL-2-driven T-cell responses participate in the muscle and skin inflammation of dermatomyositis, and the calcineurin/JAK inhibitors (already mapped) used to treat it converge on the T-cell IL-2 signalling axis.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Female predominance: dermatomyositis, like most autoimmune myopathies, is more common in women, and estrogen's enhancement of immune and interferon responses is thought to contribute to this sex difference in susceptibility.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 humoral help: IL-4 and type-2 T-cell help support the B-cell autoantibody responses (immunoglobulin G already mapped) against Mi-2, MDA5 and TIF1-gamma that define the clinical subtypes of dermatomyositis.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative muscle injury: the inflamed, ischaemic perifascicular muscle of dermatomyositis (HIF already mapped) generates oxidative stress, to which xanthine oxidase contributes, and the reactive oxygen species add to the fibre damage and weakness.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the inflamed muscle and skin (IL-6 and IL-1 already mapped) contribute to the pain and inflammation of dermatomyositis, part of the eicosanoid dimension of its myositis and rash.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 cytokine axis: IL-13, with IL-4 (already mapped), completes the type-2 cytokine support for the B-cell autoantibody responses and the fibrotic remodelling seen in the interstitial lung disease of dermatomyositis.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Vasculopathy: the angiopoietin-Tie2 axis reflects the vasculopathy of dermatomyositis (endothelin-1 and VEGF already mapped), the capillary dropout and perifascicular atrophy that are hallmarks of its muscle and skin disease.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of inflammation: the chronic IL-6 (already mapped) inflammation of dermatomyositis raises hepcidin, sequestering iron to produce the anaemia of chronic disease seen in active disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron sequestration: the systemic inflammation of dermatomyositis sequesters iron through hepcidin (already mapped), causing the anaemia of chronic disease, part of its systemic involvement.
- `connects-to` → **[Von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — Vasculopathy marker: the endothelial injury of the vasculopathy (endothelin-1 and angiopoietin already mapped) of dermatomyositis raises von Willebrand factor, reflecting the capillary damage that underlies the perifascicular pathology.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Paraneoplastic malignancy: dermatomyositis, especially with the anti-TIF1γ antibody, carries a markedly raised cancer risk including lung cancer, mandating malignancy screening at diagnosis.
- `connects-to` → **[Gastric cancer](../gastric-cancer/README.md)** — Paraneoplastic malignancy: dermatomyositis is associated with gastric and nasopharyngeal cancers (with ovarian and lung already mapped), the paraneoplastic link that makes it a marker of occult malignancy.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin is part of the immune-metabolic milieu and the steroid (cortisol already mapped)-related metabolic disturbance of dermatomyositis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of dermatomyositis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) of dermatomyositis.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate cytotoxicity: the NK cells (perforin already mapped) contribute to the innate immune dysregulation and the type-I interferon (already mapped) milieu of dermatomyositis.
- `connects-to` → **[Rheumatoid arthritis](../rheumatoid-arthritis/README.md)** — Autoimmune overlap: dermatomyositis can overlap with rheumatoid arthritis and other connective-tissue diseases (systemic sclerosis already mapped), sharing the autoimmune (immunoglobulin already mapped) mechanisms and the rituximab (CD20 already mapped) treatment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the type-I interferon (already mapped) and Th1/Th17 (IFN-γ and IL-17 already mapped) drive of dermatomyositis.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell infiltrate: the mast cells infiltrate the perivascular skin and muscle lesions and contribute to the type-2 (IL-4 and IL-13 already mapped) dimension of dermatomyositis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophil infiltrate: the neutrophils and the NETs (S100A8/9 already mapped) contribute to the vasculopathy and the anti-MDA5 rapidly-progressive ILD of dermatomyositis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the mixed immune profile of dermatomyositis.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibrotic effector: the fibroblasts and myofibroblasts drive the dermal and the pulmonary (the anti-MDA5 rapidly-progressive ILD already mapped) fibrosis of dermatomyositis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial alarmin: TSLP, released by the injured keratinocytes and epithelium, contributes to the type-2 (IL-4 and IL-13 already mapped) dimension and the skin/lung inflammation of dermatomyositis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Type-2 remodelling: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines, is a biomarker of the fibrotic remodelling of the skin and interstitial lung disease of dermatomyositis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation drives the complement (MAC)-mediated capillary injury of dermatomyositis.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway that deposits the membrane-attack complex on the endomysial capillaries (endothelial cells already mapped) of dermatomyositis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic systemic inflammation of dermatomyositis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Myositis kinin axis: bradykinin, generated by kallikrein activation in the inflamed muscle and skin capillaries of dermatomyositis, amplifies vascular permeability and the endothelial (already mapped) injury that drives the capillary-dropout microangiopathy of the disease.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia support: erythropoietin corrects the normocytic anaemia of chronic disease (hepcidin and transferrin already mapped) of active dermatomyositis, and EPO may modulate the ILD-driven hypoxia (oxygen already mapped) response in the pulmonary complications of the disease.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell effector in myositis: histamine, released by the mast cells (already mapped) infiltrating the inflamed muscle and skin of dermatomyositis, amplifies the vascular permeability and the type-2 (IL-4, IL-13 already mapped) inflammatory dimension of the disease.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian–immune axis: melatonin, via MT1/MT2 receptors on muscle cells and immune effectors, modulates the Th17/Treg balance (IL-17 and TGF-β already mapped) and exhibits anti-inflammatory effects relevant to the circadian symptom variation of dermatomyositis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine coupling: prolactin, elevated during active dermatomyositis, potentiates B-cell autoimmunity (anti-MDA5 antibody context, MHC-II already mapped) and Th1 activation (IFN-γ already mapped), amplifying the autoimmune myositis cascade.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Neuroimmune anti-inflammatory: oxytocin, via OXT receptors on immune and muscle cells, exerts anti-inflammatory effects modulating the macrophage (already mapped) and T-cell (already mapped) activation in the inflamed muscle of dermatomyositis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — DM testosterone: testosterone suppresses Th1/Th17 cytokine production (IFN-γ and IL-17A already mapped) in dermatomyositis, explaining female-sex predominance; androgen deficiency amplifies macrophage (already mapped) and T-helper (already mapped) driven myositis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — DM serotonin: serotonin activates mast cells (already mapped) to amplify perimysial inflammation via 5-HT2 receptor-mediated macrophage (already mapped) activation; serotonin also modulates the skin (already mapped) inflammatory cascade in the cutaneous DM phenotype.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — DM vasopressin: vasopressin (ADH) suppresses T-cytotoxic-cell (already mapped) mediated muscle fibre cytolysis; vasopressin also modulates mast-cell (already mapped) driven skin (already mapped) vascular permeability in the dermatomyositis cutaneous phenotype.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — DM selenium: selenoproteins counter IFN-γ (already mapped) and NF-κB (already mapped) driven oxidative stress in dermatomyositis; selenium deficiency amplifies mast-cell (already mapped) perimysial inflammation and impairs TGF-β (already mapped) fibrotic repair.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — DM iodine: thyroid hormones (iodine-dependent) modulate the IFN-γ (already mapped) and NF-κB (already mapped) autoimmune axis; iodine deficiency amplifies mast-cell (already mapped) skin (already mapped) inflammation and impairs macrophage (already mapped) resolution.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — DM sodium: high dietary sodium amplifies Th17 polarisation and IL-17A (already mapped) production in dermatomyositis; sodium-driven NF-κB (already mapped) activation sustains macrophage (already mapped) and mast-cell (already mapped) perimysial inflammation.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — DM magnesium: magnesium supports macrophage (already mapped) anti-inflammatory function and muscle-cell integrity; magnesium deficiency amplifies NF-κB (already mapped) and IFN-γ (already mapped) and TGF-β (already mapped) perimysial inflammation in dermatomyositis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — DM zinc: zinc supports macrophage (already mapped) anti-inflammatory resolution and mast-cell (already mapped) cytokine dampening; zinc deficiency amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-17A (already mapped) perimysial inflammation of dermatomyositis.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — DM copper: copper-dependent SOD in macrophages (already mapped) and mast-cell (already mapped) counters oxidative stress; copper deficiency amplifies NF-κB (already mapped) and IFN-γ (already mapped) and TGF-β (already mapped) perimysial inflammation in dermatomyositis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — DM potassium: potassium efflux from macrophages (already mapped) and mast-cell (already mapped) drives NLRP3-IL-1β; potassium dysregulation amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-17A (already mapped) perimysial inflammation of dermatomyositis.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — DM chloride: chloride, via ClC channels on macrophages (already mapped) and mast-cell (already mapped), regulates cytosolic pH for lysosomal killing; chloride imbalance amplifies NF-κB (already mapped) and IFN-γ (already mapped) perimysial inflammation of dermatomyositis.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — sulfur, as glutathione precursor in macrophage (already mapped) and mast-cell (already mapped), counters oxidative stress; sulfur deficiency amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) perimysial inflammation of dermatomyositis.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — nitrogen in macrophage (already mapped) and mast-cell (already mapped) drives nitric-oxide-mediated muscle inflammation; nitrogen dysregulation amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) perimysial cascade of dermatomyositis.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — carbon metabolism in macrophage (already mapped) and mast-cell (already mapped) drives oxidative phosphorylation; carbon dysregulation amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) perimysial inflammation of dermatomyositis.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — dermatomyositis hydrogen: hydrogen via ROS from macrophage (already mapped) and mast-cell (already mapped) modulates perimysial oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) cascade of dermatomyositis.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — dermatomyositis glp-1: GLP-1 from macrophages (already mapped) and mast-cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) cascade of dermatomyositis.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — dermatomyositis angiotensin-ii: angiotensin-II from macrophages (already mapped) and mast-cells (already mapped) modulates vascular tone; angiotensin dysregulation amplifies NF-κB (already mapped) and IFN-γ (already mapped) and IL-6 (already mapped) cascade of dermatomyositis.

[^bohan-peter-1975-dm-criteria]: Bohan A, Peter JB. Polymyositis and dermatomyositis. *N Engl J Med.* 1975;292(7):344-347. [doi:10.1056/NEJM197502132920706](https://doi.org/10.1056/NEJM197502132920706) · [PubMed 1090839](https://pubmed.ncbi.nlm.nih.gov/1090839/)
[^lundberg-2021-iim-classification]: Lundberg IE, et al. 2017 EULAR/ACR classification criteria for adult and juvenile idiopathic inflammatory myopathies. *Arthritis Rheumatol.* 2017;69(12):2271-2282. [doi:10.1002/art.40320](https://doi.org/10.1002/art.40320) · [PubMed 29106061](https://pubmed.ncbi.nlm.nih.gov/29106061/)
[^aggarwal-2022-ivig-dm-prodera]: Aggarwal R, Charles-Schoeman C, Schessl J, et al. Trial of Intravenous Immune Globulin in Dermatomyositis. *N Engl J Med.* 2022;387(14):1264-1278. [doi:10.1056/NEJMoa2117024](https://doi.org/10.1056/NEJMoa2117024) · [PubMed 36198072](https://pubmed.ncbi.nlm.nih.gov/36198072/)
[^sato-2021-anti-mda5-ild]: Sato S, Kuwana M. Clinicopathological features of Japanese patients with anti-CADM-140/MDA5 antibody-positive dermatomyositis. *Arthritis Rheum.* 2009;61(5):611-620. [doi:10.1002/art.24341](https://doi.org/10.1002/art.24341) · [PubMed 19405014](https://pubmed.ncbi.nlm.nih.gov/19405014/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
