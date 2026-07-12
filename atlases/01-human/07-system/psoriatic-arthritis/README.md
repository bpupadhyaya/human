---
schema: human-scale-entry/v1
id: psoriatic-arthritis
name: Psoriatic Arthritis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Seronegative inflammatory arthritis in ~30% of psoriasis patients; 5 clinical patterns; CASPAR criteria. Driven by IL-17A, IL-23, TNF-α, and IL-36 axes targeting skin, entheses, and joints. Approved biologics: anti-TNF, anti-IL-17A, anti-IL-23, anti-IL-12/23, JAK/TYK2 inhibitors."
aliases: ["PsA", "psoriatic spondylitis", "psoriatic spondyloarthritis"]
sources:
  - id: ritchlin-2017-psa-review
    type: peer-reviewed
    cite: "Ritchlin CT, Colbert RA, Gladman DD. Psoriatic arthritis. N Engl J Med. 2017;376(10):957-970."
    doi: "10.1056/NEJMra1505557"
    pmid: "28273019"
  - id: mease-2015-secukinumab-psa-future2
    type: peer-reviewed
    cite: "Mease PJ, McInnes IB, Kirkham B, et al. Secukinumab inhibition of interleukin-17A in patients with psoriatic arthritis. N Engl J Med. 2015;373(14):1329-1339."
    doi: "10.1056/NEJMoa1503317"
    pmid: "26422723"
  - id: deodhar-2020-guselkumab-discover1
    type: peer-reviewed
    cite: "Deodhar A, Helliwell PS, Boehncke WH, et al. Guselkumab in patients with active psoriatic arthritis who were biologic-naive or had previously received TNFalpha inhibitor treatment (DISCOVER-1). Lancet. 2020;395(10230):1115-1125."
    doi: "10.1016/S0140-6736(20)30263-4"
    pmid: "32178765"
  - id: gladman-2005-caspar-criteria
    type: peer-reviewed
    cite: "Taylor W, Gladman D, Helliwell P, et al. Classification criteria for psoriatic arthritis: development of new criteria from a large international study. Arthritis Rheum. 2006;54(8):2665-2673."
    doi: "10.1002/art.21972"
    pmid: "16871531"
cross_links:
  - target: 01-human/03-molecular/il-36
    relation: modulated-by
    note: "IL-36α/β/γ overexpressed in PsA skin and synovium → NF-κB → IL-6/CXCL8/CCL20 → neutrophil and DC recruitment at entheses; IL36RN mutations link GPP to PsA; spesolimab (anti-IL-36R; FDA 2022) under investigation in PsA."
  - target: 01-human/03-molecular/il-17a
    relation: modulated-by
    note: "IL-17A drives PsA enthesitis, synovitis, and new bone formation; secukinumab (FUTURE 2: ACR20 54% vs 15%; FDA 2016) and ixekizumab (SPIRIT-P1/2) are approved; entheseal ILC3 produce IL-17A independently of IL-23 in some PsA patients."
  - target: 01-human/03-molecular/il-23
    relation: modulated-by
    note: "IL-23 drives the Th17/IL-17A axis in PsA skin and entheses; guselkumab (DISCOVER-1/2: ACR20 ~59-64%; FDA 2020) and risankizumab (KEEPsAKE; FDA 2022) are approved; ustekinumab (anti-p40) targets both IL-12 and IL-23 in PsA and psoriasis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: modulated-by
    note: "TNF-α drives PsA synovitis, enthesitis, and structural damage; adalimumab, certolizumab (RAPID-PsA: ACR20 58% vs 24%; FDA 2013), etanercept, golimumab, and infliximab are approved; TNF + IL-36 co-activation amplifies synovial inflammation."
  - target: 01-human/03-molecular/hla-b27
    relation: connects-to
    note: "HLA-B27 in ~20% of PsA overall but ~60-70% with axial PsA; axial PsA shares sacroiliitis with axSpA; HLA-C*06:02 is primary genetic risk for cutaneous psoriasis and polyarticular PsA; ERAP1 epistasis with HLA-B27 modulates axial risk."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "Axial PsA and AS share HLA-B27, sacroiliitis, and IL-17A/TNF-α pathobiology; distinguished by psoriasis, DIP involvement, and asymmetric new bone formation (periostitis); anti-IL-17A and anti-TNF are effective across both spondyloarthropathies."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "PsA occurs in ~30% of plaque psoriasis patients; skin disease severity (PASI) often precedes joint involvement by ~10 years; shared IL-17A/IL-23 pathobiology explains why biologics effective in psoriasis (PASI 90/100 endpoints) also treat PsA."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Psoriatic arthritis grows out of psoriasis: ~30% of psoriasis patients develop it, usually years after the skin disease, and both run on the same IL-23/IL-17 axis — why biologics that clear psoriatic plaques (anti-IL-17, anti-IL-23) also treat the joints."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Psoriatic arthritis attacks the musculoskeletal system distinctively: asymmetric oligoarthritis, distal interphalangeal disease, enthesitis, dactylitis ('sausage digit'), and sacroiliitis — combining erosion with new bone formation, unlike the pure erosion of RA."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Psoriatic arthritis is driven by Th17 helper T cells: IL-23 expands IL-17-producing CD4+ T cells (and innate IL-17 at entheses) that activate neutrophils and osteoclasts — driving inflammation, erosion, and new-bone formation, the rationale for anti-IL-17/IL-23 biologics."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Psoriatic and rheumatoid arthritis are the two major chronic inflammatory arthritides but differ: PsA is a seronegative spondyloarthropathy with enthesitis, dactylitis, DIP involvement, and psoriasis, while RA is a symmetric, RF/anti-CCP-positive synovitis sparing the DIP joints."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Psoriatic arthritis and gout can mimic and coexist: high cell turnover in psoriasis raises uric acid, so PsA patients get gout more often, and an acutely swollen toe (dactylitis vs podagra) may need joint aspiration to tell crystal arthritis from psoriatic disease."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Psoriatic arthritis uniquely combines bone erosion and new bone formation: TNF and IL-17 drive osteoclasts to erode joints (pencil-in-cup deformity) while stimulating osteoblasts to build syndesmophytes and enthesophytes—a remodeling signature distinct from RA."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Psoriatic arthritis and IBD belong to the same IL-23/Th17 spondyloarthritis family: both share gut-skin-joint inflammation and respond to IL-23 and TNF blockers—though IL-17 inhibitors that help PsA can paradoxically worsen IBD."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Psoriatic arthritis is strongly tied to obesity: adipose tissue is pro-inflammatory (TNF, IL-6, leptin), raising PsA risk and severity and blunting response to therapy, while weight loss improves disease control—so PsA is as much a metabolic as an immune disease."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Psoriatic arthritis clusters with type 2 diabetes in a metabolic-syndrome phenotype: shared systemic inflammation (TNF, IL-6) drives insulin resistance, so PsA patients have excess diabetes—screening for metabolic risk is part of comprehensive PsA care."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Synovial fibroblasts help drive the joint destruction of psoriatic arthritis: activated by IL-17/TNF, they proliferate, invade and erode cartilage and bone at inflamed joints and entheses—so fibroblast-driven tissue remodeling, not just immune cells, damages the joint."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Psoriatic arthritis can inflame the eye: as a spondyloarthritis, it predisposes to uveitis and conjunctivitis, so eye symptoms join the skin, nail and joint features—prompting ophthalmologic care alongside rheumatologic and dermatologic management."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Psoriatic arthritis raises cardiovascular risk through systemic inflammation: chronic IL-17/TNF inflammation accelerates atherosclerosis and pairs with obesity and metabolic syndrome, so heart attacks and strokes are excess causes of death in PsA."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK inhibitors treat psoriatic arthritis: the IL-23/IL-17 and other cytokines driving joint and skin inflammation signal through JAK, so oral JAK inhibitors (tofacitinib, upadacitinib) work across both domains where older drugs target one pathway."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Psoriatic arthritis links skin and joints in the integumentary system: it develops in some people with psoriasis, and skin and nail disease often precede the arthritis, so the rash is both a clue and part of one systemic inflammatory disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Psoriatic arthritis is an immune-mediated spondyloarthritis: dysregulated innate and Th17 immunity inflames entheses, joints and skin, so it sits in the seronegative spondyloarthritis family and responds to the same cytokine-targeting biologics."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Psoriatic arthritis both destroys and builds bone: alongside osteoclast erosions it activates osteoblasts to lay down new bone—periostitis, enthesophytes and the 'pencil-in-cup' deformity—a bone-proliferation pattern that sets it apart from rheumatoid arthritis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12 shares the p40 subunit with IL-23 in psoriatic arthritis: the antibody ustekinumab blocks both by targeting p40, easing skin and joint disease, though IL-23-specific blockade has shown the IL-23/IL-17 axis matters more for the arthritis."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Gut dysbiosis ties psoriatic arthritis to the spondyloarthritis family: an altered microbiome and subclinical gut inflammation can drive the IL-23/IL-17 response, part of why psoriatic and inflammatory-bowel disease overlap."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Psoriatic arthritis attacks where collagen anchors tendon to bone: enthesitis—inflammation at these collagen-rich insertion sites—is its defining lesion, and the same process lays down pathologic new bone alongside the erosions."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Psoriatic arthritis is inflamed by synovial macrophages: these cells flood the joint lining and pour out TNF, a central driver that anti-TNF biologics blunt, making macrophage-derived cytokines a therapeutic linchpin."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Psoriatic arthritis is kindled by dendritic cells: they sense triggers and secrete IL-23 that ignites the IL-17 pathway in skin and joint, sitting at the top of the cytokine cascade that newer IL-23 blockers aim to shut off."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells drive psoriatic arthritis at the joint: CD8 T cells, many making IL-17, accumulate in the inflamed synovium and entheses, so the disease is fueled by killer T cells as much as by the T-helper response."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Psoriatic arthritis both erodes and builds bone with calcium: unlike pure erosive arthritis, it lays down new calcified bone at entheses and joints (enthesophytes, ankylosis), so disordered calcium-bone turnover gives it its distinctive radiographic look."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "A gut-joint axis feeds psoriatic arthritis: subclinical bowel inflammation and a disturbed microbiome prime the IL-23/IL-17 response that strikes the joints, linking the large intestine to the arthritis and to its overlap with inflammatory bowel disease."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Salt may inflame psoriatic arthritis: high sodium pushes naive T cells toward the IL-17-producing Th17 lineage that drives both the skin and joint disease, a dietary link to its core immune axis."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Psoriatic arthritis smolders in the bone marrow: subchondral bone-marrow edema (osteitis) on MRI is a hallmark of the disease, marking the inflammation at entheses and joints before erosions appear."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils tie psoriatic skin to joint: they form the micro-abscesses of psoriatic plaques and pour into inflamed entheses and joints, linking the IL-17-driven skin and arthritis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons capture psoriatic arthritis's signature damage: X-rays show the 'pencil-in-cup' deformity of eroded finger joints, while MRI and ultrasound catch the enthesitis and dactylitis early, before the bone destruction becomes irreversible."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Psoriatic arthritis is hard on the heart: the same chronic IL-17 and TNF inflammation that swells joints accelerates atherosclerosis, raising the risk of heart attack independent of the usual cardiac risk factors."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D sits on both sides of psoriatic disease: deficiency is common and may worsen the Th17/IL-17 inflammation behind it, and vitamin D analogs applied to the skin are a mainstay for the psoriasis that accompanies the arthritis."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Treating PsA keeps an eye on the liver: methotrexate, a first-line DMARD, can scar it over time, and the fatty liver that rides along with the metabolic syndrome common in PsA compounds the risk, so liver enzymes are watched."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "PsA therapy opens the lungs to harm: methotrexate can rarely trigger a hypersensitivity pneumonitis, and the TNF and IL-17 biologics that quiet the disease raise the risk of pneumonia and reactivated tuberculosis."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Fat fuels psoriatic disease: enlarged adipocytes pour out inflammatory adipokines, and the obesity common in PsA both raises the risk of developing it and blunts the response to treatment, tying metabolism to the joints."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "PsA is 'seronegative' yet treated with antibodies: rheumatoid factor and anti-CCP are characteristically absent, separating it from RA, while monoclonal antibodies against TNF, IL-17, and IL-23 are the mainstay that controls both skin and joints."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Chronic inflammation scars the arteries: PsA carries excess cardiovascular risk as circulating cytokines injure the endothelial lining and accelerate atherosclerosis, so heart-attack and stroke prevention is woven into managing the joints."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Body and mood suffer together: depression is markedly more common in PsA, driven by chronic pain, visible skin disease, and the same inflammatory cytokines that act on the brain, so screening for low mood is part of comprehensive care."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Psoriatic disease and fatty liver travel together: shared metabolic syndrome and systemic inflammation make NAFLD and NASH common in PsA, a risk compounded by methotrexate's own liver toxicity that must be monitored during treatment."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The IL-23/Th17 axis signals through STAT3: this transcription factor relays the cytokine drive that expands the pathogenic Th17 cells of PsA, the node downstream of the IL-23 that biologics and JAK inhibitors aim to silence."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells inflame the enthesis: resident at the tendon-bone insertions that PsA targets, they are a major innate source of IL-17, helping ignite the enthesitis and dactylitis that distinguish psoriatic from other arthritis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "PsA both erodes and builds bone: while inflammation eats away joints, Wnt/β-catenin signaling drives the new bone formation — enthesophytes and syndesmophytes — that sets psoriatic apart from rheumatoid arthritis, where this pathway is suppressed."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The brakes on inflammation slip: a relative deficiency and dysfunction of regulatory T cells lets the Th17 response run unchecked in PsA, tilting the balance toward the IL-17-driven joint and skin inflammation."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Chronic inflammation hardens the arteries: the systemic cytokine load of PsA accelerates atherosclerosis, so patients carry a raised risk of heart attack and stroke that persists beyond their joint and skin disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is the inflammatory hub: TNF and IL-17/IL-23 signals converge on NF-κB in synovial and entheseal cells, switching on the cytokine programs that drive the joint inflammation and bone remodeling of PsA."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Widespread pain confounds the joint disease: fibromyalgia is a common comorbidity in PsA, and its pain and tender points can inflate disease-activity scores, complicating the assessment of whether the arthritis is truly active."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Systemic inflammation tips toward clotting: like other chronic inflammatory arthritides, PsA carries an increased risk of venous thromboembolism, adding a venous hazard to its better-known arterial cardiovascular risk."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "The IL-17 blockers expose its niche: secukinumab and other anti-IL-17 biologics used for PsA disarm the very pathway guarding mucosa against Candida, so mucocutaneous candidiasis is a class side effect of treatment."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Inflammation and steroids thin the bone: chronic cytokine-driven bone loss in PsA, compounded by any corticosteroid use and reduced activity, lowers bone density and adds osteoporotic fracture risk to the erosive joint damage."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Persistent inflammation blunts the marrow: the sustained IL-6 and inflammatory drive of active PsA raises hepcidin and suppresses erythropoiesis, producing the anemia of chronic disease seen in poorly controlled patients."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Its TNF-blocking biologics can wake latent TB: tumor-necrosis-factor is essential to containing tuberculosis in granulomas, so TNF inhibitors for PsA risk reactivating latent infection — making screening mandatory before treatment."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Immunosuppressive biologics can reactivate hepatitis B: the TNF inhibitors and other immune-modulating drugs used for PsA can let a dormant hepatitis B virus rebound, so serologic screening is required before starting therapy."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Chronic systemic inflammation accelerates the arteries: the persistent inflammatory burden of PsA, on top of its frequent metabolic syndrome, speeds atherosclerosis and raises the long-term risk of stroke."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its immunomodulatory drugs reawaken shingles: the TNF, IL-17 and especially JAK inhibitors used for PsA blunt antiviral immunity and raise the risk of herpes-zoster reactivation."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Long-term NSAIDs wear on the kidneys: the chronic non-steroidal anti-inflammatory use that controls PsA joint pain can cause analgesic nephropathy and a gradual decline in kidney function."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A painful, visible, lifelong disease breeds worry: the unpredictable flares, skin and joint disfigurement and disability of PsA foster chronic health anxiety alongside its well-documented depression."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its drugs and gut inflammation trouble the digestive tract: NSAIDs cause gastritis, methotrexate and leflunomide are hepatotoxic, and PsA shares the subclinical gut inflammation of the spondyloarthritis spectrum."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its therapies reach the lungs: methotrexate can cause a hypersensitivity pneumonitis, and the biologics for PsA raise the risk of respiratory infections including reactivated tuberculosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Immunosuppression slows surgical healing: the methotrexate and biologics that control PsA blunt the immune and inflammatory steps of repair, so wounds and joint surgery heal more slowly and infect more readily."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Chronic inflammation and its drugs reach the kidney: sustained inflammation can deposit secondary AA amyloid in the kidney causing proteinuria, and NSAIDs used for symptoms are nephrotoxic."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Spine, eye and drugs touch the nervous system: axial disease can compress the cord, anterior uveitis affects the eye, and TNF-inhibitor therapy rarely triggers demyelination."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Immune activation modestly raises lymphoma risk: chronic immune activation and TNF-inhibitor therapy slightly increase lymphoma risk, with reactive lymphadenopathy during active disease."
  - target: 03-medicine/01-modern/11-biologics/adalimumab
    relation: connects-to
    note: "Biologics target its cytokines: anti-TNF agents like adalimumab, along with IL-17 and IL-23 inhibitors, control the joint and skin inflammation of psoriatic arthritis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It clusters with metabolic disease: psoriatic arthritis is strongly associated with obesity, insulin resistance and the metabolic syndrome, which also worsen its activity."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It shapes pregnancy planning: psoriatic arthritis often improves or flares in pregnancy, and the safety of its biologic and methotrexate therapy guides conception decisions."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Methotrexate is the conventional DMARD: low-dose methotrexate, a chemotherapy agent repurposed as an anti-inflammatory, treats the skin and peripheral joints of psoriatic arthritis before or alongside biologics."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It both erodes and builds bone: psoriatic arthritis uniquely combines joint erosion with new-bone formation, producing the pencil-in-cup deformity and enthesophytes that distinguish it radiographically from rheumatoid arthritis."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "TB must be excluded before biologics: anti-TNF and other biologics used for psoriatic arthritis can reactivate latent tuberculosis, so screening with IGRA or skin test is mandatory before starting them."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "HLA-B27 reaches the heart's wiring: like ankylosing spondylitis, psoriatic and other HLA-B27 spondyloarthropathies can cause atrioventricular conduction block and aortic-root inflammation, adding cardiac risk beyond their accelerated atherosclerosis."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "A gut-joint-kidney axis: the IL-17/IL-23 mucosal immunity that drives psoriatic arthritis also dysregulates IgA, and spondyloarthropathies carry an increased risk of IgA nephropathy—inflammation surfacing in the kidney."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "A caution for its biologics: the TNF inhibitors central to psoriatic arthritis can unmask or worsen demyelinating disease, so multiple sclerosis contraindicates them—one cytokine blockade helping joints yet harming nerves."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Erosion and new bone at once: PsA combines osteoclast-driven bone erosion (RANKL) with paradoxical new bone formation and enthesophytes (Wnt), a dual remodelling that distinguishes it from rheumatoid arthritis."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Cardiovascular risk beyond the joints: PsA's systemic IL-17 and TNF inflammation accelerates atherosclerosis of the arterial wall, raising cardiovascular mortality independent of the skin and joint disease."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Secondary renal involvement: chronic psoriatic-arthritis inflammation can cause IgA nephropathy and, rarely, AA amyloidosis that damages the kidney, a systemic spillover of joint and skin disease."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The gut-joint axis: subclinical gut inflammation and microbiome changes drive spondyloarthritis including psoriatic arthritis through IL-23 from the intestinal epithelium, and IL-17 inhibitors can paradoxically flare bowel disease."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Th17 versus Th2: psoriatic arthritis sits at the IL-17/23 (Th17) pole of skin immunity opposite the Th2-driven atopic dermatitis, and biologics for one can paradoxically induce eczematous eruptions resembling the other."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Immunosuppression and infection: the TNF, IL-17/23 and JAK inhibitors that control psoriatic arthritis modulate immunity, a consideration for COVID-19 severity and vaccine response in treated patients."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Systemic inflammation: IL-6 contributes to the synovitis of psoriatic arthritis and to its comorbid cardiovascular and metabolic disease burden."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Eicosanoid pain pathway: COX-derived prostaglandins drive the joint pain and inflammation of psoriatic arthritis, the target of NSAIDs used for first-line symptom relief."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Distinctive synovial vasculature: VEGF-driven angiogenesis produces the tortuous, bushy synovial vessels characteristic of psoriatic arthritis, differing from the pattern in rheumatoid arthritis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Innate inflammation: IL-1β contributes to the enthesitis and joint inflammation of psoriatic arthritis, part of the innate immune activation upstream of the IL-23/IL-17 axis."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: NLRP3-inflammasome activation matures the IL-1β that drives the enthesitis and synovitis of psoriatic arthritis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 component: IFN-γ from Th1 cells adds to the mixed cytokine milieu of psoriatic arthritis alongside the dominant Th17/IL-17 response."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Alarmin biomarker: calprotectin (S100A8/A9) released by activated neutrophils and monocytes amplifies synovial and skin inflammation in psoriatic arthritis and serves as a circulating marker of disease activity."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "T-cell costimulation: abatacept (CTLA-4-Ig) blocks the CD28 costimulation that activates the autoreactive T cells of psoriatic arthritis, an approved mechanism distinct from the dominant cytokine-blocking biologics."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes into the inflamed synovium and entheses of psoriatic arthritis, where they differentiate into macrophages and RANKL-responsive osteoclast precursors that drive joint erosion."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Pathological new bone: unlike the pure erosion of rheumatoid arthritis, psoriatic arthritis also forms new bone at entheses (enthesophytes, periostitis), and low sclerostin — releasing the Wnt brake on osteoblasts — drives this osteoproliferation."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Entheseal alarmin: IL-33 released from stressed stromal cells at the enthesis activates innate lymphoid cells and γδ T cells to produce IL-17, an upstream alarmin feeding the IL-23/IL-17 axis that drives psoriatic enthesitis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine link to comorbidity: obesity-associated leptin is elevated in psoriatic disease and promotes Th17 differentiation, mechanistically tying the metabolic syndrome and cardiovascular risk of psoriatic arthritis to its joint and skin inflammation."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Th17 and new bone: with the IL-6 already mapped, TGF-β licenses the pathogenic Th17 cells central to psoriatic arthritis, and its pro-osteogenic activity contributes to the entheseal new-bone formation that distinguishes PsA from rheumatoid arthritis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Counter-regulatory adipokine: alongside the leptin already mapped, adiponectin from adipose tissue modulates joint inflammation, and the adiponectin-leptin imbalance of obesity helps explain the metabolic comorbidity and disease activity of psoriatic arthritis."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Immune-bone bridge: osteopontin is elevated in psoriatic arthritis serum and synovium, promoting both Th17 inflammation and the osteoclastogenesis behind erosive joint damage, linking the immune drive to the bone destruction of the disease."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate signalling hub: the IL-1 receptor family (IL-36 and IL-1β mapped) and TLRs signal through MyD88 to activate NF-κB (mapped), an innate-immune hub amplifying the inflammation of psoriatic arthritis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Regulatory balance: a relative deficiency of anti-inflammatory IL-10 against the dominant IL-23/IL-17 axis (mapped) contributes to the unchecked synovial and entheseal inflammation of psoriatic arthritis."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Neuro-immune enthesitis: sensory neuropeptide CGRP at entheses links neurogenic signalling to the enthesitis and new-bone formation that distinguish psoriatic arthritis from rheumatoid arthritis."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate initiation: TLR4 innate sensing of microbial and damage signals (with MyD88 already mapped) contributes to the initiation of the synovial and entheseal inflammation of psoriatic arthritis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Immunometabolic activation: mTOR-driven metabolic activation of Th17 cells and synovial fibroblasts supports the persistent inflammation of psoriatic arthritis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Synovial survival: PI3K-AKT signalling promotes the survival and proliferation of the activated synovial fibroblasts and immune cells driving the joint destruction of psoriatic arthritis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling drives the fibroblast-like synoviocyte proliferation and inflammatory response of psoriatic-arthritis synovitis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the synovial inflammation and is elevated in the joints of psoriatic arthritis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) contributes to the entheseal new-bone formation characteristic of psoriatic arthritis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling contributes to the Th1/interferon component of the mixed inflammatory milieu of psoriatic arthritis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the innate inflammatory activation of the synovium and enthesis in psoriatic arthritis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated CD8 cytotoxicity contributes to the entheseal and synovial tissue injury of psoriatic arthritis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the survival and cytokine responses of the T cells and synovial fibroblasts driving psoriatic arthritis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB and Wnt signaling that couples inflammation to the pathological bone remodeling of psoriatic arthritis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoxic inflamed synovium drives the angiogenesis and glycolytic immune-cell metabolism of psoriatic arthritis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the synovial and immune cells of psoriatic arthritis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of the T-cell and Fc receptors participates in the immune-cell activation of psoriatic arthritis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the immune-cell and synoviocyte responses of psoriatic arthritis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the autoreactive T-cell and synovial-cell metabolism of psoriatic arthritis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the synovium and entheses contributes to the inflammation of psoriatic arthritis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the immune responses of psoriatic arthritis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking into the inflamed synovium and entheses of psoriatic arthritis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the innate immune activation of psoriatic arthritis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling, a target of ciclosporin, participates in the T-cell activation of psoriatic arthritis."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Vascular synovitis: psoriatic synovium shows tortuous, elongated vessels driven by angiopoietin-Tie2 and VEGF (VEGF already mapped), a distinctive angiogenic pattern that separates it morphologically from rheumatoid synovitis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic comorbidity: psoriatic arthritis clusters with obesity and insulin resistance, and the adipokine resistin links inflamed adipose tissue to systemic inflammation, extending the leptin/adiponectin metabolic axis already mapped."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Cardiovascular risk: the systemic inflammation of psoriatic arthritis impairs endothelial nitric-oxide function, a mechanism underlying the accelerated atherosclerosis and elevated cardiovascular mortality that accompany the joint disease."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "HLA and antigen presentation: beyond the HLA-B27 (already mapped) axial association, HLA class II and MHC-restricted antigen presentation shape the autoreactive T-cell response driving the synovial and entheseal inflammation of psoriatic arthritis."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell activation: IL-2-driven expansion of the autoreactive and IL-17-producing T cells sustains the joint inflammation of psoriatic arthritis, and the T-cell costimulation blocker abatacept (CTLA-4 already mapped) exploits this dependency."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiovascular comorbidity: the accelerated atherosclerosis of psoriatic arthritis (nitric oxide already mapped) raises the risk of myocardial infarction, and troponin elevation marks the cardiac injury of the events that shorten patients' lives."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia of inflammation: the chronic systemic inflammation of psoriatic arthritis (IL-6 already mapped) suppresses erythropoiesis, and the resulting anaemia of chronic disease lowers haemoglobin, adding to the fatigue that burdens patients."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic-vascular risk: psoriatic arthritis clusters with the metabolic syndrome and dyslipidaemia (leptin, adiponectin and resistin already mapped), and the altered cholesterol handling contributes to the accelerated atherosclerosis and cardiovascular risk."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress and urate: the systemic inflammation of psoriatic arthritis and the high cell turnover of psoriasis raise oxidative stress and urate through xanthine oxidase, contributing to the hyperuricaemia and gout that overlap with the disease."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance: psoriatic arthritis clusters with the metabolic syndrome, and insulin resistance (leptin, adiponectin and resistin already mapped) both accompanies the systemic inflammation and worsens the cardiovascular risk of the disease."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Neurogenic enthesitis: substance P, with CGRP (already mapped), mediates the neurogenic inflammation of the entheses, contributing to the enthesitis and pain characteristic of psoriatic arthritis."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Synovial proliferation: PDGF drives the proliferation of the synovial fibroblasts and the pannus, and with the Wnt-driven new bone (already mapped), it contributes to the joint remodelling of psoriatic arthritis."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Enthesis innervation: the entheses are richly innervated, and the neurogenic inflammation from the sensory nerves (substance P and CGRP already mapped) drives the enthesitis that is a defining feature of psoriatic arthritis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophilic inflammation: the neutrophils form the pustules of the psoriatic skin and infiltrate the inflamed synovium (S100A8/9 already mapped), part of the innate arm of the inflammation of psoriatic arthritis."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Spondyloarthropathy overlap: psoriatic arthritis and inflammatory bowel disease co-occur within the seronegative spondyloarthropathies (IL-23 and HLA-B27 already mapped), sharing the gut-joint axis and the IL-23/17-targeting biologics."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 counter-arm: IL-4 and the type-2/regulatory arm counterbalance the dominant Th17 (IL-17 and IL-23 already mapped) axis that drives the joint and skin inflammation of psoriatic arthritis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), completes the type-2 immune arm balancing the Th17 (IL-17 already mapped) drive of psoriatic arthritis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and produces the anaemia of chronic disease (haemoglobin already mapped) of the chronic inflammation of psoriatic arthritis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "pDC innate interferon: the type-I interferon of the plasmacytoid dendritic cells is part of the innate-immune initiation of the psoriasis (skin already mapped) that underlies psoriatic arthritis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm balancing the Th17 (IL-17 already mapped) drive of psoriatic arthritis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension balancing the dominant Th17 axis of psoriatic arthritis."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate lymphoid arm: the NK cells and the innate lymphoid cells (perforin already mapped) are part of the innate immune dysregulation of the synovium and enthesis of psoriatic arthritis."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Synovial B cells: the B cells form the synovial lymphoid aggregates and contribute to the local autoantibody (immunoglobulin already mapped) and cytokine milieu of psoriatic arthritis."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma-cell arm: the plasma cells, downstream of the B cells (already mapped), secrete the antibodies of the synovial humoral component of psoriatic arthritis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Synovial complement: the complement C5 and its C5a (with C3 already mapped) contribute to the complement activation in the inflamed synovium of psoriatic arthritis."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Pruritus cytokine: IL-31 is the pruritogenic type-2 (IL-4 and IL-13 already mapped) cytokine contributing to the itch of the psoriatic skin lesions associated with psoriatic arthritis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, a selenoprotein antioxidant cofactor, is part of the micronutrient dimension whose deficiency is associated with the psoriatic disease of psoriatic arthritis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil recruitment and the innate inflammation of the psoriatic synovium and entheses."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active in the inflamed synovium of psoriatic arthritis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic systemic inflammation of psoriatic arthritis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Skin–joint alarmin: TSLP released by keratinocytes drives the Th2 and Th17 (IL-17A already mapped) polarisation that links psoriatic skin inflammation to the synovial and entheseal disease of psoriatic arthritis."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Synovial mast-cell effector: histamine from the abundant mast cells of the psoriatic synovium amplifies vascular permeability, IL-17A (already mapped) release and the joint swelling central to psoriatic arthritis flares."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Entheseal ECM remodelling: periostin, induced by IL-13 and TGF-β in the psoriatic entheses and synovium, promotes the fibroblast invasion and new bone formation of the enthesitis-driven joint damage that distinguishes psoriatic arthritis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Synovial kinin: bradykinin generated in the inflamed psoriatic synovium activates B1/B2 receptors on synoviocytes and nociceptors, amplifying joint pain, oedema and the IL-17A (already mapped)-driven inflammatory cascade of psoriatic arthritis flares."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation: C1-esterase inhibitor restrains the classical complement (C3, C5 and C5aR1 already mapped) within the psoriatic synovium, limiting complement-driven myeloid recruitment and the angiogenesis (VEGF already mapped) of joint inflammation."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Chronic-disease anaemia support: erythropoietin addresses the normocytic anaemia of chronic psoriatic arthritis inflammation (TNF-α and IL-6 already mapped); EPOR expression on synoviocytes additionally modulates joint inflammation."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "PsA melatonin: melatonin regulates circadian TNF-α (already mapped) and IL-17A (already mapped)-driven synovial inflammation, with nocturnal inflammatory peaks in psoriatic arthritis corresponding to melatonin's anti-inflammatory MT2 receptor signalling."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "PsA androgen axis: testosterone exerts immunosuppressive effects on the IL-17A (already mapped) and TNF-α (already mapped)-driven psoriatic arthritis inflammation, modulating Th17/Th1 (already mapped) balance and the sex-dimorphic joint vs skin involvement of PsA."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "PsA serotonin: serotonin from psoriatic skin (already mapped) mast cells and platelets (already mapped) activates 5-HT2 receptors on synoviocytes and nociceptors, amplifying joint pain and the IL-17A (already mapped)-driven synovial inflammatory cascade of psoriatic arthritis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "PsA oxytocin: oxytocin modulates neuroimmune crosstalk and mast-cell (already mapped) degranulation in the psoriatic synovium, intersecting the IL-17A (already mapped) and TNF-α (already mapped)-driven joint inflammation of psoriatic arthritis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "PsA vasopressin: vasopressin via V1aR on synoviocytes and mast cells (already mapped) potentiates HPA-axis stress-inflammatory responses, amplifying the TNF-α (already mapped) and IL-17A (already mapped)-driven synovial inflammation and bone erosion of psoriatic arthritis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "PsA prolactin: prolactin promotes Th17 (IL-17A already mapped) and Th1 (IFN-γ already mapped) polarisation and stimulates synoviocyte (already mapped) proliferation, amplifying the NF-κB (already mapped) and TNF-α (already mapped)-driven joint inflammation of psoriatic arthritis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "PsA iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and dendritic-cell (already mapped) differentiation; iodine deficiency amplifies the NF-κB (already mapped) and IL-17A (already mapped) joint-inflammatory cascade of psoriatic arthritis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "PsA magnesium: magnesium, as ATP cofactor in osteoclasts (already mapped) and fibroblasts (already mapped), modulates bone-remodelling; magnesium deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) erosive cascade of psoriatic arthritis."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "PsA copper: copper, as lysyl oxidase cofactor in fibroblasts (already mapped) and osteoblasts (already mapped), drives synovial ECM crosslinking; copper deficiency amplifies NF-κB (already mapped) and IL-17A (already mapped) bone-erosion cascade of psoriatic arthritis."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "PsA iron: iron supports macrophage (already mapped) and osteoclast (already mapped) activation; iron overload amplifies NF-κB (already mapped) and TNF-α (already mapped) synovial inflammatory cascade driving the IL-17A (already mapped) bone-erosion of psoriatic arthritis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "PsA potassium: potassium, via Kir channels in macrophages (already mapped) and fibroblasts (already mapped), regulates synovial inflammation; potassium dysregulation amplifies NF-κB (already mapped) and IL-17A (already mapped) joint-erosion cascade of psoriatic arthritis."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "PsA phosphorus: phosphorus, as ATP precursor in osteoclasts (already mapped) and macrophages (already mapped), drives bone-remodelling energy; phosphorus deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) erosive cascade of psoriatic arthritis."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "PsA carbon: carbon as backbone of IL-17A (already mapped) and NF-κB (already mapped) proteins in macrophages (already mapped) sustains joint-erosion signalling; carbon depletion amplifies NF-κB (already mapped) and TNF-α (already mapped) cascade of PsA."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "PsA chloride: chloride channels in macrophages (already mapped) and synoviocytes regulate synovial fluid ion balance; chloride dysregulation amplifies NF-κB (already mapped) and IL-17A (already mapped) inflammatory joint-erosion cascade of psoriatic arthritis."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "PsA hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and osteoclasts (already mapped), supports collagen cross-linking; hydrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) erosive cascade of psoriatic arthritis."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "PsA nitrogen: nitrogen in amino-acid scaffold of IL-17A (already mapped) and TNF-α (already mapped) proteins in macrophages (already mapped) sustains joint-erosion signalling; nitrogen dysregulation amplifies NF-κB (already mapped) cascade of psoriatic arthritis."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "PsA oxygen: oxygen, via mitochondrial respiration in macrophages (already mapped) and osteoclasts (already mapped), sustains IL-17A (already mapped) signalling; oxygen depletion amplifies NF-κB (already mapped) and TNF-α (already mapped) erosive cascade of psoriatic arthritis."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "PsA sulfur: sulfur in cysteine residues of IL-17A (already mapped) and NF-κB (already mapped) proteins in synoviocytes sustains thiol-redox balance; sulfur depletion amplifies NF-κB (already mapped) and TNF-α (already mapped) erosive cascade of psoriatic arthritis."
---

# Psoriatic Arthritis

## Overview

Psoriatic arthritis (PsA) is a chronic, seronegative inflammatory arthritis occurring in approximately 30% of patients with psoriasis, affecting roughly 0.3–1% of the general population [^ritchlin-2017-psa-review]. It is classified within the **spondyloarthropathies (SpA)** alongside ankylosing spondylitis, reactive arthritis, and IBD-associated arthritis, unified by enthesitis as a central pathologic process. PsA is clinically heterogeneous, affecting peripheral joints, spine, entheses, tendons, and nails, with wide variation among patients and over time within individuals.

The molecular drivers — IL-17A, IL-23, TNF-α, and IL-36 — connect PsA to psoriatic skin disease and explain why drugs targeting these pathways benefit both cutaneous and articular manifestations simultaneously. Genetic susceptibility involves **HLA-C*06:02** (cutaneous psoriasis) and **HLA-B27** (axial involvement), reinforcing its spondyloarthropathic biology [^gladman-2005-caspar-criteria].

## Structure

Moll and Wright (1973) described five clinical subtypes; modern data show patients transition between patterns over time:

| Pattern | Frequency | Characteristics |
|:--------|:----------|:----------------|
| Oligoarticular asymmetric | ~30–50% | <5 joints, large and small; often hand + knee |
| Polyarticular symmetric | ~30–40% | ≥5 joints; resembles RA but RF-negative |
| Distal interphalangeal (DIP) predominant | ~5–10% | DIP joints + nail disease; uncommon in RA |
| Axial | ~5% isolated; ~40–50% have some axial | Sacroiliitis and spondylitis; HLA-B27-associated |
| Arthritis mutilans | ~5% | Severe osteolysis; telescoping "opera-glass" deformities |

**Dactylitis** ("sausage digit") — diffuse flexor tenosynovitis + joint and periarticular edema — is a characteristic feature of PsA (and reactive arthritis) not seen in RA.

**Enthesitis** is the primary pathological lesion: insertion-site inflammation at Achilles tendon, plantar fascia, patellar tendon, iliac crest, and vertebral endplates.

## Function

PsA impairs musculoskeletal function through three parallel processes:

1. **Synovitis and joint destruction** — pannus formation with FLS proliferation and MMPs → cartilage degradation; structural damage (erosions + new bone) progressively restricts range of motion, particularly in DIP joints (pencil-in-cup), wrists, and sacroiliac joints in axial disease.

2. **Enthesitis** — inflammation at tendon and ligament insertion sites causes pain with activity, morning stiffness, and impaired ambulation (Achilles, plantar fascia) or reduced grip strength; entheseal new bone (enthesophytes) may fuse joints in advanced disease.

3. **Systemic inflammatory burden** — sustained IL-17A/TNF-α-driven inflammation → accelerated atherosclerosis, metabolic syndrome (insulin resistance, obesity, dyslipidemia), and elevated cardiovascular mortality independent of traditional risk factors. Fatigue is a major functional impairment driven by systemic inflammation and sleep disruption.

The combined skin, nail, joint, and entheseal burden produces substantial quality-of-life impairment (HAQ-DI, DLQI); MDA (Minimal Disease Activity) is the validated treat-to-target endpoint capturing multiple domains simultaneously.

## Diagnosis — CASPAR Criteria

The **Classification Criteria for Psoriatic Arthritis (CASPAR)** require inflammatory musculoskeletal disease + ≥3 points from:

| Feature | Points |
|:--------|:-------|
| Current psoriasis | 2 |
| Personal history of psoriasis (if no current) | 1 |
| Family history of psoriasis (if no current/personal) | 1 |
| Psoriatic nail dystrophy | 1 |
| Negative RF | 1 |
| Current dactylitis or history of dactylitis (documented by rheumatologist) | 1 |
| Juxta-articular new bone formation on X-ray | 1 |

Sensitivity 91.4%, specificity 98.7% for PsA vs. other inflammatory arthritis [^gladman-2005-caspar-criteria].

### Laboratory and Imaging

- **Seronegative**: RF and anti-CCP negative (CCP positive in ~8–15% — associated with erosive disease)
- **Acute-phase reactants**: CRP/ESR elevated in active disease, but may be normal in purely oligoarticular disease
- **HLA typing**: HLA-B27 (axial PsA), HLA-C*06:02 (skin/polyarticular)
- **Plain radiographs**: Erosions (joint margin and central) + **periostitis** and **new bone formation** (distinguishes from RA); DIP: "pencil-in-cup" deformity in arthritis mutilans
- **MRI**: STIR for bone marrow edema at entheses and sacroiliitis; SPARCC scoring of sacroiliitis
- **Ultrasound**: Power Doppler for entheseal blood flow (enthesophytes, bursitis, erosions)

### Disease Activity Measures

| Tool | Measures |
|:-----|:---------|
| DAPSA (Disease Activity in PsA) | TJC28 + SJC28 + patient global + pain VAS + CRP |
| MDA (Minimal Disease Activity) | 7 criteria; 5/7 = MDA (treatment target) |
| PASI | Psoriasis Area and Severity Index (skin) |
| NAPSI | Nail Psoriasis Severity Index |
| LEI | Leeds Enthesitis Index (6 sites) |
| LEDI | Leeds Dactylitis Index |

## Pathology

### Immunopathogenesis

PsA shares enthesitis biology with AS but is distinguished by its obligate cutaneous psoriasis connection. The current model invokes:

1. **Psoriatic skin as the initiating immune niche** — IL-36, IL-17A, and TNF-α produced by skin-resident DCs, Th17, and keratinocytes enter circulation and are amplified at mechanical stress sites (entheses)
2. **Enthesitis** — IL-23 from resident myeloid cells activates entheseal ILC3 → IL-17A + IL-22 → local bone remodeling; CD8+ T cells predominate (unlike RA which is CD4+)
3. **Synovitis** — prominent **neoangiogenesis** (VEGF-driven) and CD68+ macrophage accumulation; TNF-α drives synoviocyte proliferation and MMPs
4. **New bone formation** — paradoxical coexistence of erosion and new bone (osteoproliferation); Wnt signaling (DKK1 downregulation), BMP pathway → syndesmophytes and enthesophytes; IL-17A drives RANKL → osteoclast-mediated erosion

### Genetics

- **HLA-C*06:02**: Strongest genetic risk for plaque psoriasis and polyarticular PsA
- **HLA-B27**: ~20% of all PsA; ~60–70% in axial PsA (but lower than AS where ~90%+ are B27+)
- **HLA-B38, B39**: Associated with polyarticular erosive PsA
- **IL23R, IL12B, TNFAIP3, TRAF3IP2 (act1)**: GWAS-confirmed non-HLA risk loci shared with psoriasis and/or AS
- **ERAP1**: Epistatic with HLA-B27 in axial PsA (same as in AS)

### Extra-articular Features

| Feature | Frequency |
|:--------|:----------|
| Psoriasis (prerequisite or history) | 100% |
| Nail disease (pitting, onycholysis, oil drop sign) | 80–90% |
| Uveitis (anterior; less common than in AS) | 7–20% |
| IBD (Crohn's, UC) | 3–5% |
| Metabolic syndrome, cardiovascular comorbidity | Increased |

## Treatment

### Treat-to-Target

Target: **MDA (Minimal Disease Activity)** — simultaneously achieving low disease burden across TJC, SJC, PASI, pain, patient global, HAQ, and enthesitis. TICOPA trial demonstrated superiority of tight MDA-targeted control vs. standard care.

### Stepwise Approach

**Step 1 — NSAIDs + local therapy**
Naproxen, diclofenac, or celecoxib for enthesitis pain; intra-articular corticosteroids for active joints; topical agents for skin.

**Step 2 — Conventional DMARDs**
- **Methotrexate (MTX)**: effective for skin and peripheral joint disease; **no proven effect on axial disease or radiographic progression**
- **Leflunomide**: alternative to MTX; moderate effect on peripheral joints
- **Apremilast** (PDE4 inhibitor): oral small molecule; PALACE trials; moderate efficacy for skin, joints, dactylitis, enthesitis; no DMARD bridging concerns

**Step 3 — Biologics**

*Anti-TNF (first-line biologic, highest-quality evidence):*
- Adalimumab (ADEPT trial: ACR20 58% vs 14%; FDA 2005)
- Etanercept (PsARC response; FDA 2002)
- Certolizumab pegol (RAPID-PsA: ACR20 58% vs 24%; FDA 2013)
- Golimumab (GO-REVEAL trial; FDA 2009)
- Infliximab (IMPACT-2; FDA 2004)

*Anti-IL-17A:*
- **Secukinumab** — **FUTURE 2** (N=397): ACR20 **54%** vs **15%** placebo; MDA 36% vs 9% at wk 24; radiographic progression inhibition; **FDA January 2016** [^mease-2015-secukinumab-psa-future2]
- **Ixekizumab** — SPIRIT-P1 (biologic-naive) and SPIRIT-P2 (TNFi-experienced): ACR50 ~34% and ~25%; FDA 2017

*Anti-IL-23p19:*
- **Guselkumab** — DISCOVER-1 (biologic-naive and TNFi-experienced): ACR20 **59%** vs **22%**; MDA 27% vs 11% at wk 24; FDA 2020 [^deodhar-2020-guselkumab-discover1]
- **Risankizumab** — KEEPsAKE-1/2 trials: ACR20 ~57% vs 33%; FDA 2022
- **Ustekinumab** (anti-IL-12/23 p40) — PSUMMIT-1/2: ACR20 42–43% vs 20–23%; FDA 2013

*JAK inhibitors (oral):*
- **Tofacitinib** (JAK1/3): OPAL Broaden/Beyond: ACR20 ~50% vs 33%; FDA 2017
- **Upadacitinib** (JAK1-selective): SELECT-PsA-1/2: ACR20 71% vs 36%; FDA 2021
- **Filgotinib** (JAK1): European approval 2024

*TYK2 inhibitor:*
- **Deucravacitinib** — POETYK PsA-1/2 (Phase 3): ACR20 ~52–53% vs ~30–32%; data emerging for PsA; already FDA-approved for plaque psoriasis (September 2022)

### Anti-IL-23 Paradox in SpA

Risankizumab (anti-IL-23p19) **failed primary endpoints** in the SURPASS trial for AS — contrasting with its PsA efficacy. This demonstrates divergent IL-23 dependence: entheseal ILC3 in AS/axial SpA produce IL-17A independently of IL-23 via alternative stimuli, while in PsA skin and peripheral joints the IL-23 → Th17 axis is more dominant.

## Connections

- **Modulated by** → **[IL-36](../../03-molecular/il-36/README.md)** — IL-36α/β/γ overexpressed in PsA skin and synovium → NF-κB → IL-6/CXCL8/CCL20 → neutrophil and DC recruitment at entheses; IL36RN mutations link GPP to PsA; spesolimab under investigation.
- **Modulated by** → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A drives PsA enthesitis, synovitis, and new bone formation; secukinumab and ixekizumab are approved; entheseal ILC3 produce IL-17A independently of IL-23 in some PsA patients.
- **Modulated by** → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 drives Th17/IL-17A axis in PsA skin and entheses; guselkumab and risankizumab are approved; ustekinumab (anti-p40) targets IL-12 and IL-23 in PsA and psoriasis.
- **Modulated by** → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α drives synovitis, enthesitis, and structural damage; multiple anti-TNF agents are first-line biologics in PsA; co-activation with IL-36 amplifies synovial inflammation.
- `connects-to` → **[HLA-B27](../../03-molecular/hla-b27/README.md)** — HLA-B27 in ~20% of PsA overall, ~60–70% with axial PsA; HLA-C*06:02 is primary risk allele for psoriasis/polyarticular PsA; ERAP1 epistasis modulates axial PsA risk.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — Axial PsA and AS share HLA-B27, sacroiliitis, and IL-17A/TNF-α pathobiology; distinguished by psoriasis, DIP involvement, and asymmetric periostitis; anti-IL-17A and anti-TNF effective in both.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — PsA occurs in ~30% of psoriasis patients; skin disease often precedes joints by ~10 years; shared IL-17A/IL-23 biology explains why biologics achieving PASI 90/100 in psoriasis also treat PsA joints.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Psoriatic arthritis grows out of psoriasis: ~30% of psoriasis patients develop it, usually years after the skin disease, and both run on the same IL-23/IL-17 axis — why biologics that clear psoriatic plaques (anti-IL-17, anti-IL-23) also treat the joints.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Psoriatic arthritis attacks the musculoskeletal system distinctively: asymmetric oligoarthritis, distal interphalangeal disease, enthesitis, dactylitis ('sausage digit'), and sacroiliitis — combining erosion with new bone formation, unlike the pure erosion of RA.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Psoriatic arthritis is driven by Th17 helper T cells: IL-23 expands IL-17-producing CD4+ T cells (and innate IL-17 at entheses) that activate neutrophils and osteoclasts — driving inflammation, erosion, and new-bone formation, the rationale for anti-IL-17/IL-23 biologics.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Psoriatic and rheumatoid arthritis are the two major chronic inflammatory arthritides but differ: PsA is a seronegative spondyloarthropathy with enthesitis, dactylitis, DIP involvement, and psoriasis, while RA is a symmetric, RF/anti-CCP-positive synovitis sparing the DIP joints.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Methotrexate is the conventional DMARD: low-dose methotrexate, a chemotherapy agent repurposed as an anti-inflammatory, treats the skin and peripheral joints of psoriatic arthritis before or alongside biologics.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It both erodes and builds bone: psoriatic arthritis uniquely combines joint erosion with new-bone formation, producing the pencil-in-cup deformity and enthesophytes that distinguish it radiographically from rheumatoid arthritis.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — TB must be excluded before biologics: anti-TNF and other biologics used for psoriatic arthritis can reactivate latent tuberculosis, so screening with IGRA or skin test is mandatory before starting them.
- `connects-to` → **[Gout](../gout/README.md)** — Psoriatic arthritis and gout can mimic and coexist: high cell turnover in psoriasis raises uric acid, so PsA patients get gout more often, and an acutely swollen toe (dactylitis vs podagra) may need joint aspiration to tell crystal arthritis from psoriatic disease.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Psoriatic arthritis uniquely combines bone erosion and new bone formation: TNF and IL-17 drive osteoclasts to erode joints (pencil-in-cup deformity) while stimulating osteoblasts to build syndesmophytes and enthesophytes—a remodeling signature distinct from RA.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Psoriatic arthritis and IBD belong to the same IL-23/Th17 spondyloarthritis family: both share gut-skin-joint inflammation and respond to IL-23 and TNF blockers—though IL-17 inhibitors that help PsA can paradoxically worsen IBD.
- `connects-to` → **[Obesity](../obesity/README.md)** — Psoriatic arthritis is strongly tied to obesity: adipose tissue is pro-inflammatory (TNF, IL-6, leptin), raising PsA risk and severity and blunting response to therapy, while weight loss improves disease control—so PsA is as much a metabolic as an immune disease.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Psoriatic arthritis clusters with type 2 diabetes in a metabolic-syndrome phenotype: shared systemic inflammation (TNF, IL-6) drives insulin resistance, so PsA patients have excess diabetes—screening for metabolic risk is part of comprehensive PsA care.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Synovial fibroblasts help drive the joint destruction of psoriatic arthritis: activated by IL-17/TNF, they proliferate, invade and erode cartilage and bone at inflamed joints and entheses—so fibroblast-driven tissue remodeling, not just immune cells, damages the joint.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Psoriatic arthritis can inflame the eye: as a spondyloarthritis, it predisposes to uveitis and conjunctivitis, so eye symptoms join the skin, nail and joint features—prompting ophthalmologic care alongside rheumatologic and dermatologic management.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Psoriatic arthritis raises cardiovascular risk through systemic inflammation: chronic IL-17/TNF inflammation accelerates atherosclerosis and pairs with obesity and metabolic syndrome, so heart attacks and strokes are excess causes of death in PsA.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK inhibitors treat psoriatic arthritis: the IL-23/IL-17 and other cytokines driving joint and skin inflammation signal through JAK, so oral JAK inhibitors (tofacitinib, upadacitinib) work across both domains where older drugs target one pathway.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Psoriatic arthritis links skin and joints in the integumentary system: it develops in some people with psoriasis, and skin and nail disease often precede the arthritis, so the rash is both a clue and part of one systemic inflammatory disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Psoriatic arthritis is an immune-mediated spondyloarthritis: dysregulated innate and Th17 immunity inflames entheses, joints and skin, so it sits in the seronegative spondyloarthritis family and responds to the same cytokine-targeting biologics.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Psoriatic arthritis both destroys and builds bone: alongside osteoclast erosions it activates osteoblasts to lay down new bone—periostitis, enthesophytes and the 'pencil-in-cup' deformity—a bone-proliferation pattern that sets it apart from rheumatoid arthritis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 shares the p40 subunit with IL-23 in psoriatic arthritis: the antibody ustekinumab blocks both by targeting p40, easing skin and joint disease, though IL-23-specific blockade has shown the IL-23/IL-17 axis matters more for the arthritis.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Gut dysbiosis ties psoriatic arthritis to the spondyloarthritis family: an altered microbiome and subclinical gut inflammation can drive the IL-23/IL-17 response, part of why psoriatic and inflammatory-bowel disease overlap.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Psoriatic arthritis attacks where collagen anchors tendon to bone: enthesitis—inflammation at these collagen-rich insertion sites—is its defining lesion, and the same process lays down pathologic new bone alongside the erosions.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Psoriatic arthritis is inflamed by synovial macrophages: these cells flood the joint lining and pour out TNF, a central driver that anti-TNF biologics blunt, making macrophage-derived cytokines a therapeutic linchpin.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Psoriatic arthritis is kindled by dendritic cells: they sense triggers and secrete IL-23 that ignites the IL-17 pathway in skin and joint, sitting at the top of the cytokine cascade that newer IL-23 blockers aim to shut off.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells drive psoriatic arthritis at the joint: CD8 T cells, many making IL-17, accumulate in the inflamed synovium and entheses, so the disease is fueled by killer T cells as much as by the T-helper response.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Psoriatic arthritis both erodes and builds bone with calcium: unlike pure erosive arthritis, it lays down new calcified bone at entheses and joints (enthesophytes, ankylosis), so disordered calcium-bone turnover gives it its distinctive radiographic look.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — A gut-joint axis feeds psoriatic arthritis: subclinical bowel inflammation and a disturbed microbiome prime the IL-23/IL-17 response that strikes the joints, linking the large intestine to the arthritis and to its overlap with inflammatory bowel disease.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Salt may inflame psoriatic arthritis: high sodium pushes naive T cells toward the IL-17-producing Th17 lineage that drives both the skin and joint disease, a dietary link to its core immune axis.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Psoriatic arthritis smolders in the bone marrow: subchondral bone-marrow edema (osteitis) on MRI is a hallmark of the disease, marking the inflammation at entheses and joints before erosions appear.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils tie psoriatic skin to joint: they form the micro-abscesses of psoriatic plaques and pour into inflamed entheses and joints, linking the IL-17-driven skin and arthritis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons capture psoriatic arthritis's signature damage: X-rays show the 'pencil-in-cup' deformity of eroded finger joints, while MRI and ultrasound catch the enthesitis and dactylitis early, before the bone destruction becomes irreversible.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Psoriatic arthritis is hard on the heart: the same chronic IL-17 and TNF inflammation that swells joints accelerates atherosclerosis, raising the risk of heart attack independent of the usual cardiac risk factors.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D sits on both sides of psoriatic disease: deficiency is common and may worsen the Th17/IL-17 inflammation behind it, and vitamin D analogs applied to the skin are a mainstay for the psoriasis that accompanies the arthritis.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Treating PsA keeps an eye on the liver: methotrexate, a first-line DMARD, can scar it over time, and the fatty liver that rides along with the metabolic syndrome common in PsA compounds the risk, so liver enzymes are watched.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — PsA therapy opens the lungs to harm: methotrexate can rarely trigger a hypersensitivity pneumonitis, and the TNF and IL-17 biologics that quiet the disease raise the risk of pneumonia and reactivated tuberculosis.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Fat fuels psoriatic disease: enlarged adipocytes pour out inflammatory adipokines, and the obesity common in PsA both raises the risk of developing it and blunts the response to treatment, tying metabolism to the joints.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — PsA is 'seronegative' yet treated with antibodies: rheumatoid factor and anti-CCP are characteristically absent, separating it from RA, while monoclonal antibodies against TNF, IL-17, and IL-23 are the mainstay that controls both skin and joints.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Chronic inflammation scars the arteries: PsA carries excess cardiovascular risk as circulating cytokines injure the endothelial lining and accelerate atherosclerosis, so heart-attack and stroke prevention is woven into managing the joints.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Body and mood suffer together: depression is markedly more common in PsA, driven by chronic pain, visible skin disease, and the same inflammatory cytokines that act on the brain, so screening for low mood is part of comprehensive care.
- `connects-to` → **[NASH](../nash/README.md)** — Psoriatic disease and fatty liver travel together: shared metabolic syndrome and systemic inflammation make NAFLD and NASH common in PsA, a risk compounded by methotrexate's own liver toxicity that must be monitored during treatment.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The IL-23/Th17 axis signals through STAT3: this transcription factor relays the cytokine drive that expands the pathogenic Th17 cells of PsA, the node downstream of the IL-23 that biologics and JAK inhibitors aim to silence.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells inflame the enthesis: resident at the tendon-bone insertions that PsA targets, they are a major innate source of IL-17, helping ignite the enthesitis and dactylitis that distinguish psoriatic from other arthritis.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — PsA both erodes and builds bone: while inflammation eats away joints, Wnt/β-catenin signaling drives the new bone formation — enthesophytes and syndesmophytes — that sets psoriatic apart from rheumatoid arthritis, where this pathway is suppressed.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The brakes on inflammation slip: a relative deficiency and dysfunction of regulatory T cells lets the Th17 response run unchecked in PsA, tilting the balance toward the IL-17-driven joint and skin inflammation.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Chronic inflammation hardens the arteries: the systemic cytokine load of PsA accelerates atherosclerosis, so patients carry a raised risk of heart attack and stroke that persists beyond their joint and skin disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is the inflammatory hub: TNF and IL-17/IL-23 signals converge on NF-κB in synovial and entheseal cells, switching on the cytokine programs that drive the joint inflammation and bone remodeling of PsA.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Widespread pain confounds the joint disease: fibromyalgia is a common comorbidity in PsA, and its pain and tender points can inflate disease-activity scores, complicating the assessment of whether the arthritis is truly active.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Systemic inflammation tips toward clotting: like other chronic inflammatory arthritides, PsA carries an increased risk of venous thromboembolism, adding a venous hazard to its better-known arterial cardiovascular risk.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — The IL-17 blockers expose its niche: secukinumab and other anti-IL-17 biologics used for PsA disarm the very pathway guarding mucosa against Candida, so mucocutaneous candidiasis is a class side effect of treatment.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Inflammation and steroids thin the bone: chronic cytokine-driven bone loss in PsA, compounded by any corticosteroid use and reduced activity, lowers bone density and adds osteoporotic fracture risk to the erosive joint damage.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Persistent inflammation blunts the marrow: the sustained IL-6 and inflammatory drive of active PsA raises hepcidin and suppresses erythropoiesis, producing the anemia of chronic disease seen in poorly controlled patients.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Its TNF-blocking biologics can wake latent TB: tumor-necrosis-factor is essential to containing tuberculosis in granulomas, so TNF inhibitors for PsA risk reactivating latent infection — making screening mandatory before treatment.
- `connects-to` → **[Hepatitis B virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Immunosuppressive biologics can reactivate hepatitis B: the TNF inhibitors and other immune-modulating drugs used for PsA can let a dormant hepatitis B virus rebound, so serologic screening is required before starting therapy.
- `connects-to` → **[Stroke](../stroke/README.md)** — Chronic systemic inflammation accelerates the arteries: the persistent inflammatory burden of PsA, on top of its frequent metabolic syndrome, speeds atherosclerosis and raises the long-term risk of stroke.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its immunomodulatory drugs reawaken shingles: the TNF, IL-17 and especially JAK inhibitors used for PsA blunt antiviral immunity and raise the risk of herpes-zoster reactivation.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Long-term NSAIDs wear on the kidneys: the chronic non-steroidal anti-inflammatory use that controls PsA joint pain can cause analgesic nephropathy and a gradual decline in kidney function.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A painful, visible, lifelong disease breeds worry: the unpredictable flares, skin and joint disfigurement and disability of PsA foster chronic health anxiety alongside its well-documented depression.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its drugs and gut inflammation trouble the digestive tract: NSAIDs cause gastritis, methotrexate and leflunomide are hepatotoxic, and PsA shares the subclinical gut inflammation of the spondyloarthritis spectrum.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its therapies reach the lungs: methotrexate can cause a hypersensitivity pneumonitis, and the biologics for PsA raise the risk of respiratory infections including reactivated tuberculosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Immunosuppression slows surgical healing: the methotrexate and biologics that control PsA blunt the immune and inflammatory steps of repair, so wounds and joint surgery heal more slowly and infect more readily.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Chronic inflammation and its drugs reach the kidney: sustained inflammation can deposit secondary AA amyloid in the kidney causing proteinuria, and NSAIDs used for symptoms are nephrotoxic.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Spine, eye and drugs touch the nervous system: axial disease can compress the cord, anterior uveitis affects the eye, and TNF-inhibitor therapy rarely triggers demyelination.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Immune activation modestly raises lymphoma risk: chronic immune activation and TNF-inhibitor therapy slightly increase lymphoma risk, with reactive lymphadenopathy during active disease.
- `connects-to` → **[Adalimumab](../../../03-medicine/01-modern/11-biologics/adalimumab/README.md)** — Biologics target its cytokines: anti-TNF agents like adalimumab, along with IL-17 and IL-23 inhibitors, control the joint and skin inflammation of psoriatic arthritis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It clusters with metabolic disease: psoriatic arthritis is strongly associated with obesity, insulin resistance and the metabolic syndrome, which also worsen its activity.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It shapes pregnancy planning: psoriatic arthritis often improves or flares in pregnancy, and the safety of its biologic and methotrexate therapy guides conception decisions.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — HLA-B27 reaches the heart's wiring: like ankylosing spondylitis, psoriatic and other HLA-B27 spondyloarthropathies can cause atrioventricular conduction block and aortic-root inflammation, adding cardiac risk beyond their accelerated atherosclerosis.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — A gut-joint-kidney axis: the IL-17/IL-23 mucosal immunity that drives psoriatic arthritis also dysregulates IgA, and spondyloarthropathies carry an increased risk of IgA nephropathy—inflammation surfacing in the kidney.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — A caution for its biologics: the TNF inhibitors central to psoriatic arthritis can unmask or worsen demyelinating disease, so multiple sclerosis contraindicates them—one cytokine blockade helping joints yet harming nerves.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Erosion and new bone at once: PsA combines osteoclast-driven bone erosion (RANKL) with paradoxical new bone formation and enthesophytes (Wnt), a dual remodelling that distinguishes it from rheumatoid arthritis.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Cardiovascular risk beyond the joints: PsA's systemic IL-17 and TNF inflammation accelerates atherosclerosis of the arterial wall, raising cardiovascular mortality independent of the skin and joint disease.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Secondary renal involvement: chronic psoriatic-arthritis inflammation can cause IgA nephropathy and, rarely, AA amyloidosis that damages the kidney, a systemic spillover of joint and skin disease.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The gut-joint axis: subclinical gut inflammation and microbiome changes drive spondyloarthritis including psoriatic arthritis through IL-23 from the intestinal epithelium, and IL-17 inhibitors can paradoxically flare bowel disease.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Th17 versus Th2: psoriatic arthritis sits at the IL-17/23 (Th17) pole of skin immunity opposite the Th2-driven atopic dermatitis, and biologics for one can paradoxically induce eczematous eruptions resembling the other.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Immunosuppression and infection: the TNF, IL-17/23 and JAK inhibitors that control psoriatic arthritis modulate immunity, a consideration for COVID-19 severity and vaccine response in treated patients.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Systemic inflammation: IL-6 contributes to the synovitis of psoriatic arthritis and to its comorbid cardiovascular and metabolic disease burden.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Eicosanoid pain pathway: COX-derived prostaglandins drive the joint pain and inflammation of psoriatic arthritis, the target of NSAIDs used for first-line symptom relief.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Distinctive synovial vasculature: VEGF-driven angiogenesis produces the tortuous, bushy synovial vessels characteristic of psoriatic arthritis, differing from the pattern in rheumatoid arthritis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Innate inflammation: IL-1β contributes to the enthesitis and joint inflammation of psoriatic arthritis, part of the innate immune activation upstream of the IL-23/IL-17 axis.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: NLRP3-inflammasome activation matures the IL-1β that drives the enthesitis and synovitis of psoriatic arthritis.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 component: IFN-γ from Th1 cells adds to the mixed cytokine milieu of psoriatic arthritis alongside the dominant Th17/IL-17 response.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Calprotectin (S100A8/A9) released by activated neutrophils and monocytes amplifies synovial and skin inflammation in psoriatic arthritis and serves as a circulating biomarker of disease activity that tracks treatment response.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Abatacept (CTLA-4-Ig) blocks the CD28 costimulation that activates the autoreactive T cells of psoriatic arthritis—an approved mechanism distinct from the cytokine-blocking biologics that dominate treatment, useful when those fail.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 draws monocytes into the inflamed synovium and entheses of psoriatic arthritis, where they differentiate into macrophages and RANKL-responsive osteoclast precursors that drive the bone erosion characteristic of the disease.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — Unlike the pure erosion of rheumatoid arthritis, psoriatic arthritis also forms new bone at entheses (enthesophytes, periostitis), and low sclerostin—releasing the Wnt brake on osteoblasts—drives this osteoproliferation.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 released from stressed stromal cells at the enthesis activates innate lymphoid cells and γδ T cells to produce IL-17, an upstream alarmin feeding the IL-23/IL-17 axis that drives psoriatic enthesitis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity-associated leptin is elevated in psoriatic disease and promotes Th17 differentiation, mechanistically tying the metabolic syndrome and cardiovascular risk of psoriatic arthritis to its joint and skin inflammation.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — With the IL-6 already mapped, TGF-β licenses the pathogenic Th17 cells central to psoriatic arthritis, and its pro-osteogenic activity contributes to the entheseal new-bone formation that distinguishes PsA from rheumatoid arthritis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Alongside the leptin already mapped, adiponectin from adipose tissue modulates joint inflammation, and the adiponectin-leptin imbalance of obesity helps explain the metabolic comorbidity and disease activity of psoriatic arthritis.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin is elevated in psoriatic arthritis serum and synovium, promoting both Th17 inflammation and the osteoclastogenesis behind erosive joint damage, linking the immune drive to the bone destruction of the disease.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — The IL-1 receptor family (IL-36 and IL-1β mapped) and TLRs signal through MyD88 to activate NF-κB (mapped), an innate-immune hub amplifying the inflammation of psoriatic arthritis.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — A relative deficiency of anti-inflammatory IL-10 against the dominant IL-23/IL-17 axis (mapped) contributes to the unchecked synovial and entheseal inflammation of psoriatic arthritis.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Sensory neuropeptide CGRP at entheses links neurogenic signaling to the enthesitis and new-bone formation that distinguish psoriatic arthritis from rheumatoid arthritis.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 innate sensing of microbial and damage signals (with MyD88 already mapped) contributes to the initiation of the synovial and entheseal inflammation of psoriatic arthritis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-driven metabolic activation of Th17 cells and synovial fibroblasts supports the persistent inflammation of psoriatic arthritis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling promotes the survival and proliferation of the activated synovial fibroblasts and immune cells driving the joint destruction of psoriatic arthritis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling drives the fibroblast-like synoviocyte proliferation and inflammatory response of psoriatic-arthritis synovitis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the synovial inflammation and is elevated in the joints of psoriatic arthritis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) contributes to the entheseal new-bone formation characteristic of psoriatic arthritis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling contributes to the Th1/interferon component of the mixed inflammatory milieu of psoriatic arthritis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the innate inflammatory activation of the synovium and enthesis in psoriatic arthritis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated CD8 cytotoxicity contributes to the entheseal and synovial tissue injury of psoriatic arthritis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the survival and cytokine responses of the T cells and synovial fibroblasts driving psoriatic arthritis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB and Wnt signaling that couples inflammation to the pathological bone remodeling of psoriatic arthritis.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoxic inflamed synovium drives the angiogenesis and glycolytic immune-cell metabolism of psoriatic arthritis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the synovial and immune cells of psoriatic arthritis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of the T-cell and Fc receptors participates in the immune-cell activation of psoriatic arthritis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the immune-cell and synoviocyte responses of psoriatic arthritis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the autoreactive T-cell and synovial-cell metabolism of psoriatic arthritis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the synovium and entheses contributes to the inflammation of psoriatic arthritis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the immune responses of psoriatic arthritis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking into the inflamed synovium and entheses of psoriatic arthritis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the innate immune activation of psoriatic arthritis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling, a target of ciclosporin, participates in the T-cell activation of psoriatic arthritis.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Vascular synovitis: psoriatic synovium shows tortuous, elongated vessels driven by angiopoietin-Tie2 and VEGF (VEGF already mapped), a distinctive angiogenic pattern that separates it morphologically from rheumatoid synovitis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic comorbidity: psoriatic arthritis clusters with obesity and insulin resistance, and the adipokine resistin links inflamed adipose tissue to systemic inflammation, extending the leptin/adiponectin metabolic axis already mapped.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Cardiovascular risk: the systemic inflammation of psoriatic arthritis impairs endothelial nitric-oxide function, a mechanism underlying the accelerated atherosclerosis and elevated cardiovascular mortality that accompany the joint disease.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — HLA and antigen presentation: beyond the HLA-B27 (already mapped) axial association, HLA class II and MHC-restricted antigen presentation shape the autoreactive T-cell response driving the synovial and entheseal inflammation of psoriatic arthritis.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell activation: IL-2-driven expansion of the autoreactive and IL-17-producing T cells sustains the joint inflammation of psoriatic arthritis, and the T-cell costimulation blocker abatacept (CTLA-4 already mapped) exploits this dependency.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiovascular comorbidity: the accelerated atherosclerosis of psoriatic arthritis (nitric oxide already mapped) raises the risk of myocardial infarction, and troponin elevation marks the cardiac injury of the events that shorten patients' lives.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia of inflammation: the chronic systemic inflammation of psoriatic arthritis (IL-6 already mapped) suppresses erythropoiesis, and the resulting anaemia of chronic disease lowers haemoglobin, adding to the fatigue that burdens patients.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Metabolic-vascular risk: psoriatic arthritis clusters with the metabolic syndrome and dyslipidaemia (leptin, adiponectin and resistin already mapped), and the altered cholesterol handling contributes to the accelerated atherosclerosis and cardiovascular risk.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress and urate: the systemic inflammation of psoriatic arthritis and the high cell turnover of psoriasis raise oxidative stress and urate through xanthine oxidase, contributing to the hyperuricaemia and gout that overlap with the disease.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance: psoriatic arthritis clusters with the metabolic syndrome, and insulin resistance (leptin, adiponectin and resistin already mapped) both accompanies the systemic inflammation and worsens the cardiovascular risk of the disease.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Neurogenic enthesitis: substance P, with CGRP (already mapped), mediates the neurogenic inflammation of the entheses, contributing to the enthesitis and pain characteristic of psoriatic arthritis.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Synovial proliferation: PDGF drives the proliferation of the synovial fibroblasts and the pannus, and with the Wnt-driven new bone (already mapped), it contributes to the joint remodelling of psoriatic arthritis.
- `connects-to` → **[Peripheral nerve](../../05-tissue/peripheral-nerve/README.md)** — Enthesis innervation: the entheses are richly innervated, and the neurogenic inflammation from the sensory nerves (substance P and CGRP already mapped) drives the enthesitis that is a defining feature of psoriatic arthritis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophilic inflammation: the neutrophils form the pustules of the psoriatic skin and infiltrate the inflamed synovium (S100A8/9 already mapped), part of the innate arm of the inflammation of psoriatic arthritis.
- `connects-to` → **[Inflammatory bowel disease](../inflammatory-bowel-disease/README.md)** — Spondyloarthropathy overlap: psoriatic arthritis and inflammatory bowel disease co-occur within the seronegative spondyloarthropathies (IL-23 and HLA-B27 already mapped), sharing the gut-joint axis and the IL-23/17-targeting biologics.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 counter-arm: IL-4 and the type-2/regulatory arm counterbalance the dominant Th17 (IL-17 and IL-23 already mapped) axis that drives the joint and skin inflammation of psoriatic arthritis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), completes the type-2 immune arm balancing the Th17 (IL-17 already mapped) drive of psoriatic arthritis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and produces the anaemia of chronic disease (haemoglobin already mapped) of the chronic inflammation of psoriatic arthritis.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — pDC innate interferon: the type-I interferon of the plasmacytoid dendritic cells is part of the innate-immune initiation of the psoriasis (skin already mapped) that underlies psoriatic arthritis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm balancing the Th17 (IL-17 already mapped) drive of psoriatic arthritis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension balancing the dominant Th17 axis of psoriatic arthritis.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate lymphoid arm: the NK cells and the innate lymphoid cells (perforin already mapped) are part of the innate immune dysregulation of the synovium and enthesis of psoriatic arthritis.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Synovial B cells: the B cells form the synovial lymphoid aggregates and contribute to the local autoantibody (immunoglobulin already mapped) and cytokine milieu of psoriatic arthritis.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Plasma-cell arm: the plasma cells, downstream of the B cells (already mapped), secrete the antibodies of the synovial humoral component of psoriatic arthritis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Synovial complement: the complement C5 and its C5a (with C3 already mapped) contribute to the complement activation in the inflamed synovium of psoriatic arthritis.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Pruritus cytokine: IL-31 is the pruritogenic type-2 (IL-4 and IL-13 already mapped) cytokine contributing to the itch of the psoriatic skin lesions associated with psoriatic arthritis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant micronutrient: selenium, a selenoprotein antioxidant cofactor, is part of the micronutrient dimension whose deficiency is associated with the psoriatic disease of psoriatic arthritis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil recruitment and the innate inflammation of the psoriatic synovium and entheses.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active in the inflamed synovium of psoriatic arthritis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic systemic inflammation of psoriatic arthritis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Skin–joint alarmin: TSLP released by keratinocytes drives the Th2 and Th17 (IL-17A already mapped) polarisation that links psoriatic skin inflammation to the synovial and entheseal disease of psoriatic arthritis.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Synovial mast-cell effector: histamine from the abundant mast cells of the psoriatic synovium amplifies vascular permeability, IL-17A (already mapped) release and the joint swelling central to psoriatic arthritis flares.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Entheseal ECM remodelling: periostin, induced by IL-13 and TGF-β in the psoriatic entheses and synovium, promotes the fibroblast invasion and new bone formation of the enthesitis-driven joint damage that distinguishes psoriatic arthritis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Synovial kinin: bradykinin generated in the inflamed psoriatic synovium activates B1/B2 receptors on synoviocytes and nociceptors, amplifying joint pain, oedema and the IL-17A (already mapped)-driven inflammatory cascade of psoriatic arthritis flares.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation: C1-esterase inhibitor restrains the classical complement (C3, C5 and C5aR1 already mapped) within the psoriatic synovium, limiting complement-driven myeloid recruitment and the angiogenesis (VEGF already mapped) of joint inflammation.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Chronic-disease anaemia support: erythropoietin addresses the normocytic anaemia of chronic psoriatic arthritis inflammation (TNF-α and IL-6 already mapped); EPOR expression on synoviocytes additionally modulates joint inflammation.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — PsA melatonin: melatonin regulates circadian TNF-α (already mapped) and IL-17A (already mapped)-driven synovial inflammation, with nocturnal inflammatory peaks in psoriatic arthritis corresponding to melatonin's anti-inflammatory MT2 receptor signalling.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — PsA androgen axis: testosterone exerts immunosuppressive effects on the IL-17A (already mapped) and TNF-α (already mapped)-driven psoriatic arthritis inflammation, modulating Th17/Th1 (already mapped) balance and the sex-dimorphic joint vs skin involvement of PsA.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — PsA serotonin: serotonin from psoriatic skin (already mapped) mast cells and platelets (already mapped) activates 5-HT2 receptors on synoviocytes and nociceptors, amplifying joint pain and the IL-17A (already mapped)-driven synovial inflammatory cascade of psoriatic arthritis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — PsA oxytocin: oxytocin modulates neuroimmune crosstalk and mast-cell (already mapped) degranulation in the psoriatic synovium, intersecting the IL-17A (already mapped) and TNF-α (already mapped)-driven joint inflammation of psoriatic arthritis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — PsA vasopressin: vasopressin via V1aR on synoviocytes and mast cells (already mapped) potentiates HPA-axis stress-inflammatory responses, amplifying the TNF-α (already mapped) and IL-17A (already mapped)-driven synovial inflammation and bone erosion of psoriatic arthritis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — PsA prolactin: prolactin promotes Th17 (IL-17A already mapped) and Th1 (IFN-γ already mapped) polarisation and stimulates synoviocyte (already mapped) proliferation, amplifying the NF-κB (already mapped) and TNF-α (already mapped)-driven joint inflammation of psoriatic arthritis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — PsA iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and dendritic-cell (already mapped) differentiation; iodine deficiency amplifies the NF-κB (already mapped) and IL-17A (already mapped) joint-inflammatory cascade of psoriatic arthritis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — PsA magnesium: magnesium, as ATP cofactor in osteoclasts (already mapped) and fibroblasts (already mapped), modulates bone-remodelling; magnesium deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) erosive cascade of psoriatic arthritis.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — PsA copper: copper, as lysyl oxidase cofactor in fibroblasts (already mapped) and osteoblasts (already mapped), drives synovial ECM crosslinking; copper deficiency amplifies NF-κB (already mapped) and IL-17A (already mapped) bone-erosion cascade of psoriatic arthritis.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — PsA iron: iron supports macrophage (already mapped) and osteoclast (already mapped) activation; iron overload amplifies NF-κB (already mapped) and TNF-α (already mapped) synovial inflammatory cascade driving the IL-17A (already mapped) bone-erosion of psoriatic arthritis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — PsA potassium: potassium, via Kir channels in macrophages (already mapped) and fibroblasts (already mapped), regulates synovial inflammation; potassium dysregulation amplifies NF-κB (already mapped) and IL-17A (already mapped) joint-erosion cascade of psoriatic arthritis.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — PsA phosphorus: phosphorus, as ATP precursor in osteoclasts (already mapped) and macrophages (already mapped), drives bone-remodelling energy; phosphorus deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) erosive cascade of psoriatic arthritis.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — PsA carbon: carbon as backbone of IL-17A (already mapped) and NF-κB (already mapped) proteins in macrophages (already mapped) sustains joint-erosion signalling; carbon depletion amplifies NF-κB (already mapped) and TNF-α (already mapped) cascade of PsA.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — PsA chloride: chloride channels in macrophages (already mapped) and synoviocytes regulate synovial fluid ion balance; chloride dysregulation amplifies NF-κB (already mapped) and IL-17A (already mapped) inflammatory joint-erosion cascade of psoriatic arthritis.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — PsA hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and osteoclasts (already mapped), supports collagen cross-linking; hydrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) erosive cascade of psoriatic arthritis.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — PsA nitrogen: nitrogen in amino-acid scaffold of IL-17A (already mapped) and TNF-α (already mapped) proteins in macrophages (already mapped) sustains joint-erosion signalling; nitrogen dysregulation amplifies NF-κB (already mapped) cascade of psoriatic arthritis.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — PsA oxygen: oxygen, via mitochondrial respiration in macrophages (already mapped) and osteoclasts (already mapped), sustains IL-17A (already mapped) signalling; oxygen depletion amplifies NF-κB (already mapped) and TNF-α (already mapped) erosive cascade of psoriatic arthritis.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — PsA sulfur: sulfur in cysteine residues of IL-17A (already mapped) and NF-κB (already mapped) proteins in synoviocytes sustains thiol-redox balance; sulfur depletion amplifies NF-κB (already mapped) and TNF-α (already mapped) erosive cascade of psoriatic arthritis.

[^ritchlin-2017-psa-review]: Ritchlin CT, Colbert RA, Gladman DD. Psoriatic arthritis. *N Engl J Med.* 2017;376(10):957-970. [doi:10.1056/NEJMra1505557](https://doi.org/10.1056/NEJMra1505557) · [PubMed 28273019](https://pubmed.ncbi.nlm.nih.gov/28273019/)
[^mease-2015-secukinumab-psa-future2]: Mease PJ, et al. Secukinumab inhibition of interleukin-17A in patients with psoriatic arthritis. *N Engl J Med.* 2015;373(14):1329-1339. [doi:10.1056/NEJMoa1503317](https://doi.org/10.1056/NEJMoa1503317) · [PubMed 26422723](https://pubmed.ncbi.nlm.nih.gov/26422723/)
[^deodhar-2020-guselkumab-discover1]: Deodhar A, et al. Guselkumab in patients with active psoriatic arthritis (DISCOVER-1). *Lancet.* 2020;395(10230):1115-1125. [doi:10.1016/S0140-6736(20)30263-4](https://doi.org/10.1016/S0140-6736(20)30263-4) · [PubMed 32178765](https://pubmed.ncbi.nlm.nih.gov/32178765/)
[^gladman-2005-caspar-criteria]: Taylor W, et al. Classification criteria for psoriatic arthritis. *Arthritis Rheum.* 2006;54(8):2665-2673. [doi:10.1002/art.21972](https://doi.org/10.1002/art.21972) · [PubMed 16871531](https://pubmed.ncbi.nlm.nih.gov/16871531/)
