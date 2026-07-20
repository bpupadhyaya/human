---
schema: human-scale-entry/v1
id: gout
name: Gout
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Inflammatory arthritis from monosodium urate (MSU) crystal deposition; hyperuricemia → crystals → NLRP3 inflammasome → IL-1beta → neutrophil-driven acute flares. Colchicine, NSAIDs, and IL-1 inhibitors treat flares; allopurinol and febuxostat reduce urate."
aliases: ["gouty arthritis", "hyperuricemia", "tophaceous gout", "MSU crystallopathy", "podagra"]
sources:
  - id: dalbeth-2019-gout-primer
    type: peer-reviewed
    cite: "Dalbeth N, Choi HK, Joosten LAB, et al. Gout. Nat Rev Dis Primers. 2019;5(1):69."
    doi: "10.1038/s41572-019-0115-y"
    pmid: "31558729"
    url: "https://doi.org/10.1038/s41572-019-0115-y"
  - id: martinon-2006-nlrp3-gout
    type: peer-reviewed
    cite: "Martinon F, Pétrilli V, Mayor A, Tardivel A, Tschopp J. Gout-associated uric acid crystals activate the NALP3 inflammasome. Nature. 2006;440(7081):237-241."
    doi: "10.1038/nature04516"
    pmid: "16407889"
    url: "https://doi.org/10.1038/nature04516"
  - id: fitzgerald-2020-acr-gout
    type: peer-reviewed
    cite: "FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. Arthritis Care Res (Hoboken). 2020;72(6):744-760."
    doi: "10.1002/acr.24180"
    pmid: "32391934"
    url: "https://doi.org/10.1002/acr.24180"
cross_links:
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "MSU crystals are a canonical NLRP3 activator: lysosomal destabilization → cathepsin B release → NLRP3-ASC-caspase-1 activation → IL-1beta and IL-18 secretion; IL-1 blockade (anakinra, canakinumab) rapidly resolves refractory gouty flares."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Synovial macrophages phagocytose MSU crystals → NLRP3 → IL-1beta; surface-activated macrophages produce IL-6, TNF-alpha, CXCL1 → neutrophil recruitment; colchicine blocks macrophage microtubule-dependent NLRP3 assembly and inflammasome activation."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils are the primary effectors of acute gout: IL-8/CXCL1 → neutrophil influx → MSU crystal phagocytosis → ROS and proteases → tissue damage; colchicine inhibits neutrophil migration and crystal phagocytosis via microtubule disruption."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "MSU crystals activate NF-kB in macrophages and synoviocytes via TLR4 and NLRP3 → IL-6, IL-8, TNF-alpha, COX-2 → synovial inflammation; NF-kB drives both acute flare cytokines and chronic tophus-associated synovial tissue remodeling."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Xanthine oxidase converts xanthine → uric acid; serum urate >6.8 mg/dL exceeds solubility threshold → MSU crystal nucleation in joints and soft tissue → phagocytosis by neutrophils and macrophages → NLRP3 activation → acute gouty flare; allopurinol/febuxostat target XOR."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β is the central acute gout mediator: MSU crystals → NLRP3 → caspase-1 → IL-1β → neutrophil influx and arthritis; anakinra (off-label) and canakinumab (EMA approved 2013 for gout flares) target IL-1β in refractory flares unresponsive to colchicine/NSAIDs."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: treated-by
    note: "NSAIDs including ibuprofen are first-line for acute gout (ACR 2020 guidelines): COX-2-driven PGE₂ amplifies NLRP3-IL-1β neutrophil recruitment to MSU crystals; 600–800 mg TDS × 7–10 days effective; contraindicated in eGFR <30."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Gout and hypertension are tightly linked: hyperuricemia independently raises blood pressure (urate impairs endothelial NO and activates the RAAS), while thiazide/loop diuretics for HTN raise serum urate and trigger gout flares — a two-way interaction that complicates treatment."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is central to gout: it excretes ~two-thirds of uric acid, so reduced urate clearance (URAT1/GLUT9 variants, CKD, diuretics) is the main cause of hyperuricemia; conversely MSU crystals damage the kidney (urate nephropathy, stones), so gout and CKD reinforce each other."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Gout is the most common inflammatory arthritis: MSU crystals deposit in cooler peripheral joints — classically the first metatarsophalangeal joint (podagra) — igniting excruciating attacks, and over years form tophi that erode bone and cartilage if urate isn't lowered."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Gout and chronic kidney disease feed each other: reduced renal urate excretion raises serum urate to cause gout, while urate crystals and inflammation injure the kidney; CKD also limits NSAID and colchicine use, so urate-lowering with allopurinol must be dose-adjusted."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Gout is a core feature of metabolic syndrome anchored by obesity: adiposity and insulin resistance raise serum urate by cutting renal excretion and boosting purine turnover, so weight loss lowers urate and flares; gout clusters with type 2 diabetes, hypertension and fatty liver."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Hyperuricemia and gout independently raise cardiovascular risk: urate crystals and NLRP3-driven inflammation promote endothelial dysfunction and atherosclerosis, and gout patients have excess MI and stroke—part of why gout is seen as a vascular as well as joint disease."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Gout is literally a sodium disease: when uric acid exceeds its solubility it crystallizes as monosodium urate, and these needle-shaped MSU crystals deposited in joints and tophi trigger the NLRP3-driven inflammation—dissolving them by lowering urate is the cure."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Gout and rheumatoid arthritis are both inflammatory arthritides but distinct: gout is a crystal-driven (MSU) innate attack with acute monoarticular flares, while RA is an autoantibody-driven symmetric polyarthritis—aspiration versus serology separates them."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Gout clusters with type 2 diabetes in the metabolic syndrome: insulin resistance reduces renal uric-acid excretion, raising urate, while obesity and high-purine, fructose-rich diets drive both—gout often flags an underlying cardiometabolic disorder."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol is a classic gout trigger: beer (rich in purines) and spirits raise uric acid by boosting production and blocking renal excretion, so binges precipitate acute attacks—making alcohol moderation a core part of gout prevention."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Gout signals and worsens heart disease: hyperuricemia and urate-crystal inflammation track with hypertension, coronary disease and higher cardiovascular mortality, so a gout diagnosis flags cardiovascular risk—and shared drivers like obesity link the two."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Gout has a calcium-crystal mimic, pseudogout: where gout deposits monosodium urate crystals, pseudogout (CPPD) deposits calcium pyrophosphate, causing similar acute joint inflammation—so polarized-light crystal analysis distinguishes the two arthritides."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Gout is strongly tied to cardiovascular disease: hyperuricemia and the chronic inflammation of gout independently raise the risk of hypertension, coronary disease and stroke, so gout flags cardiovascular risk beyond its joint and kidney damage."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The renal system both causes and suffers from gout: under-excretion of urate by the kidney is the main reason uric acid rises, and deposited crystals form kidney stones and urate nephropathy—so gout and kidney disease drive each other in a vicious cycle."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Tophi are the chronic granulomas of gout: persistent urate crystals provoke macrophages and fibroblasts to wall them off in firm, fibrous nodular deposits in joints and soft tissue, so fibroblast-rich tophi mark long-standing, undertreated disease."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Gout is a disease of nitrogen waste: uric acid is the nitrogen-rich end-product of purine breakdown that humans, lacking uricase, cannot degrade further, so this evolutionary loss leaves urate to crystallize in joints when it builds up."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Myeloproliferative neoplasms cause secondary gout: massive cell turnover in polycythemia vera and related disorders floods the blood with purines and urate, so gout flares can be the first clue to an underlying blood-cell overproduction."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Chronic gout deposits in the skin as tophi: long-standing high urate forms chalky subcutaneous nodules over joints and ears that can ulcerate and discharge crystals, so visible tophi mark years of untreated disease."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Gout flares can be quelled with cortisol: when NSAIDs and colchicine are unsafe—as in kidney disease—corticosteroids (oral or injected into the joint) calm the crystal-driven inflammation, a key fallback for treating an acute attack."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Chronic tophaceous gout erodes bone via osteoclasts: long-standing urate deposits activate bone-resorbing osteoclasts, carving the 'punched-out' periarticular erosions seen on X-ray that distinguish advanced gout from other arthritis."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Gout traces back to purine metabolism through adenosine: breaking down adenosine and other purines yields uric acid, so a high turnover of these nucleotides—from diet or cell breakdown—feeds the hyperuricemia that precipitates urate crystals."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut shares the job of clearing urate with the kidney: about a third of uric acid is excreted into the intestine, so gut transporters and microbes that break down urate influence blood levels—and impaired gut excretion can worsen gout."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 helps inflame the gouty joint: alongside IL-1beta, urate crystals trigger IL-6 release that amplifies the fever, pain and swelling of an acute attack, part of the cytokine cascade targeted to calm flares."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help ignite the gout flare: they take up monosodium urate crystals and, with macrophages, activate the inflammasome and prime the inflammatory response that turns crystal deposition into a sudden painful attack."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Acid urine turns gout into kidney stones: uric acid dissolves poorly when urine is acidic, so a low urinary pH lets it crystallize into stones, which is why alkalinizing the urine helps prevent them."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Chronic gout lays down fibrosis: long-standing tophi become fibrous nodules that erode joints, and persistent urate in the kidney drives interstitial scarring, the lasting damage beyond the acute flare."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells help fire the first hours of a gout attack: urate crystals trigger them to release histamine and mediators that dilate vessels and recruit neutrophils, kicking off the sudden inflammation."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Gout is confirmed by light: polarized-light microscopy of joint fluid reveals the negatively birefringent urate needles, and dual-energy CT photons map urate deposits without a tap."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Gout can spring from the marrow: myeloproliferative diseases and their rapid cell turnover flood the blood with purines that become uric acid, a secondary cause of the disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Gout can deposit in the eye: urate tophi form on the eyelids and conjunctiva and rarely inflame the sclera, an unusual but recognized site of crystal deposition."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron and polarized-light microscopy clinch the gout diagnosis: aspirated joint fluid shows needle-shaped monosodium urate crystals, negatively birefringent and packed into the tophi that the inflammasome attacks."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver makes the uric acid that crystallizes in gout: it is the main site where xanthine oxidase breaks purines down to urate, so the liver's metabolism — fueled by fructose and alcohol — sets the blood level."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Low magnesium tracks with gout: deficiency is common in the metabolic syndrome that accompanies it and is linked to higher uric acid, so magnesium status is part of the metabolic picture behind the crystals."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Treating the flare punishes the gut: colchicine causes diarrhea and the NSAIDs used for acute gout inflame the stomach into gastritis and ulcers, so the drugs that quell the joint must be balanced against the bowel."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Body fat fuels hyperuricemia: adipose tissue's inflammation and the insulin resistance of obesity cut the kidney's excretion of urate, which is why weight gain raises uric acid and weight loss helps lower it."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Gout rides with insulin resistance: the hyperinsulinemia of metabolic syndrome makes the kidney retain urate, tying the pancreatic insulin axis to the crystals — and gout flags a higher risk of type 2 diabetes."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Estrogen shields women from gout: the hormone is uricosuric, helping the kidney dump urate, so gout is uncommon before menopause and its incidence in women climbs once that protection is lost."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Rapid skin turnover feeds the urate pool: psoriasis's accelerated proliferation breaks down purines into extra uric acid, so gout is more common in psoriasis — and the two arthritides can be hard to tell apart in an inflamed joint."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Crystals also rouse the complement system: monosodium urate activates complement on its surface, generating C5a that pulls neutrophils into the joint — an arm of the acute flare working alongside the NLRP3-IL-1 pathway."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF amplifies the crystal storm: released by activated macrophages alongside IL-1β, it deepens the recruitment and activation of neutrophils that make the gout flare so exquisitely painful."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Urate injures the vessel lining: high uric acid impairs endothelial nitric-oxide and promotes inflammation, a mechanism tying gout to the hypertension and cardiovascular disease that shadow it."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The gut is gout's second drain: about a third of uric acid is excreted through the intestine via the ABCG2 transporter, so impaired gut elimination — not just the kidney — can raise urate into gout."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance fuels hyperuricemia: high insulin tells the kidney to retain urate, so the hyperinsulinemia of metabolic syndrome raises uric acid into gout — one reason gout clusters with obesity and type 2 diabetes."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "High cell turnover overproduces urate: the expanded marrow of polycythemia vera and other myeloproliferative disease floods the blood with purines, causing a secondary gout that can be the presenting clue to the hematologic disorder."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Hyperuricemia is an independent vascular risk: beyond its joint disease, elevated urate promotes endothelial dysfunction and is associated with a raised risk of stroke, part of gout's broader cardiovascular shadow."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Urate and the failing heart feed each other: hyperuricemia independently predicts heart failure and worsens its outcomes, while the disease and its diuretics raise urate — a bidirectional link in gout's cardiovascular burden."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A hot joint forces a critical question: acute gout closely mimics septic arthritis, which must be excluded by joint aspiration because a missed joint infection can seed sepsis, and tophi themselves can become infected."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Gouty inflammation tips toward clotting: the systemic inflammation of gout and hyperuricemia is associated with a higher risk of venous thromboembolism, adding a venous dimension to its vascular complications."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Hyperuricemia and fatty liver cluster: gout sits squarely in the metabolic syndrome, and its insulin resistance and fructose metabolism strongly associate it with non-alcoholic steatohepatitis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Recurrent disabling pain weighs on mood: the unpredictable, intensely painful flares and chronic joint damage of tophaceous gout reduce quality of life and carry an elevated rate of depression."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic inflammation and renal disease lower the count: longstanding tophaceous gout's persistent inflammation, compounded by the chronic kidney disease that so often accompanies it, can produce an anemia of chronic disease."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Tophi erode through the skin: large chronic tophi can ulcerate and discharge chalky urate, leaving open wounds over joints that are slow to heal and prone to infection."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Ulcerated tophi invite Staph: when a tophus breaks through the skin, Staphylococcus aureus readily colonizes and infects it, risking cellulitis, septic arthritis and bloodstream infection."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Chronic inflammation and immobility cost bone: longstanding gout's persistent inflammation, joint damage and reduced mobility are associated with lower bone density and a raised fracture risk."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Urate crystals trip the innate alarm: monosodium urate crystals activate the NLRP3 inflammasome to release IL-1β, the autoinflammatory burst that drives the acute gout flare and the target of IL-1 blockers."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Both the diet and the drugs hit the gut: purine- and fructose-rich food and alcohol drive hyperuricaemia, while colchicine causes diarrhoea and the NSAIDs used in flares inflame the stomach."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is woven into metabolic disease: hyperuricaemia is tightly linked to insulin resistance and the metabolic syndrome, so gout clusters with the endocrine disturbances of obesity and diabetes."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It deposits chalky lumps under the skin: tophi — subcutaneous urate crystal deposits on the ear helix, fingers and Achilles tendon — can ulcerate and discharge a white pasty material in chronic gout."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can rarely reach the spine: tophaceous urate deposits in the spine can compress nerve roots or the spinal cord, an uncommon but serious neurological complication of long-standing gout."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Sleep apnoea feeds it: obstructive sleep apnoea raises uric acid through intermittent hypoxia and nucleotide turnover, triggering nocturnal gout flares."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids treat the flare when others can't: oral or intra-articular corticosteroids relieve acute gout for patients in whom NSAIDs and colchicine are contraindicated, such as in kidney disease."
  - target: 03-medicine/03-food/quercetin
    relation: connects-to
    note: "A dietary urate-lowering flavonoid: quercetin inhibits xanthine oxidase, the same enzyme blocked by allopurinol, and trials show it modestly lowers serum uric acid."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet can calm the inflammation: omega-3 fatty acids have anti-inflammatory effects studied for reducing gout flare frequency, complementing urate-lowering therapy."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "High cell turnover floods urate: myeloproliferative neoplasms like essential thrombocythaemia overproduce cells whose breakdown raises uric acid, a frequent secondary cause of gout."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Inflammatory arthritis to tell apart: gout and psoriatic arthritis both inflame the joints, psoriasis itself raises urate, and the two enter each other's differential and can coexist."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Crystals erode the bone: chronic tophaceous gout deposits urate beside joints, producing the punched-out juxta-articular bone erosions with overhanging edges characteristic of the disease."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "The kidney both makes and suffers gout: about 90% of hyperuricaemia is renal under-excretion of urate, while deposited urate crystals cause interstitial inflammation and chronic urate nephropathy that scars the glomerulus and lowers filtration."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Urate inflames the vessel wall: soluble urate and monosodium urate crystals promote endothelial dysfunction and NLRP3-driven inflammation in the arterial wall, a mechanistic link between hyperuricaemia and the atherosclerosis and hypertension that accompany gout."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Cell turnover floods the blood with urate: myelofibrosis and other myeloproliferative neoplasms massively increase purine breakdown, raising serum urate and causing secondary gout—worsened further by cytoreductive therapy that lyses cells."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Tumour lysis hyperuricaemia: the rapid cell turnover of acute leukaemia and its chemotherapy floods the blood with purines and urate, triggering acute gout and urate nephropathy—prevented with allopurinol or rasburicase."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Urate and the arrhythmic heart: hyperuricaemia and gout are linked to atrial fibrillation through systemic NLRP3-driven inflammation and shared metabolic risk."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The gut excretes urate too: about a third of uric acid is cleared through the intestinal epithelium via the ABCG2 transporter, so gut dysfunction shifts the urate load onto the kidney and worsens gout."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Hyperuricaemia of high cell turnover: chronic haemolysis in sickle cell disease, like myeloproliferative disease, raises serum urate and causes secondary gout and urate nephropathy."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Tophi compress nerves: large tophaceous urate deposits can entrap peripheral nerves—classically carpal tunnel syndrome at the wrist—a mechanical complication of long-standing chronic gout."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Shared inflammasome biology: gout's anti-inflammatory colchicine was repurposed and trialled for COVID-19's hyperinflammation, the two diseases linked through NLRP3-inflammasome and IL-1β signalling."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "RAAS and urate handling: angiotensin II links hyperuricaemia to hypertension and renal urate retention, and the ARB losartan is uniquely uricosuric, lowering urate while treating blood pressure."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adiposity and urate: leptin, elevated in obesity, is associated with hyperuricaemia and gout, helping explain why excess body fat raises the risk of crystal disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Recruiting the flare: CCL2 (MCP-1) draws monocytes and macrophages to deposited urate crystals, amplifying the neutrophil-rich acute inflammation of a gout attack."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "Urate-lowering bonus: SGLT2 inhibitors increase urinary urate excretion and lower serum urate, reducing gout flares—an unexpected benefit of these diabetes and heart drugs."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Inflamed-joint hypoxia: the acutely inflamed gouty joint becomes hypoxic, stabilising HIF-1α in infiltrating cells and amplifying the inflammatory response to urate crystals."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Tophus and fibrosis: TGF-β contributes to the chronic granulomatous tophus and to the renal fibrosis of chronic urate nephropathy in long-standing gout."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Neutrophil flare and resolution: S100A8/A9 from the neutrophils flooding the gouty joint amplifies the acute flare, while aggregated neutrophil extracellular traps also drive its spontaneous resolution."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Crystal complement activation: monosodium urate crystals directly activate complement through to C5, generating chemoattractants that recruit the neutrophils igniting the acute gout attack."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory mediators: prostaglandins generated in the urate-inflamed joint drive the pain, vasodilation and swelling of an acute gout flare, the target of the NSAIDs used to treat it."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Inflammasome priming: monosodium urate crystals engage TLR2/TLR4 to provide the 'signal 1' that primes the NLRP3 inflammasome, licensing the IL-1β release that drives the explosive gout flare."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: hyperuricaemia reduces endothelial nitric-oxide bioavailability, a vascular mechanism linking gout to its strong association with hypertension and cardiovascular disease."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic clustering: gout clusters with the dyslipidaemia and insulin resistance of metabolic syndrome, the shared physiology behind the high cardiovascular risk that accompanies chronic hyperuricaemia."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Flare therapy: glucocorticoids acting through the glucocorticoid receptor are a mainstay for acute gout flares, especially when NSAIDs and colchicine are contraindicated, broadly suppressing the urate-crystal-triggered inflammation."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Crystal-arthropathy differential: gout (monosodium urate crystals) must be distinguished from pseudogout, in which calcium pyrophosphate crystals provoke a similar acute crystal arthritis — a key distinction made on polarised-light microscopy of joint fluid."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "DAMP amplification: monosodium urate crystals and the DAMPs of crystal-induced cell injury signal through RAGE to amplify the NF-κB-driven inflammation, adding to the NLRP3-IL-1β axis that drives the intense pain of a gout flare."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Signal relay: TLR4 and the IL-1 receptor (TLR4 mapped) signal through MyD88 to activate NF-κB (mapped), the adaptor relaying the crystal-triggered danger signal into the cytokine output of a gout flare."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Neutrophilic flare: IL-17-producing cells help recruit the dense neutrophil infiltrate that, ingesting urate crystals, produces the acute, intensely painful joint inflammation of gout."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic link: gout is tightly tied to metabolic syndrome (insulin and leptin mapped), and the low adiponectin of visceral adiposity reflects the adipose-driven milieu that raises urate and sustains inflammation."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Crystal oxidative stress: urate crystals and xanthine-oxidase activity (already mapped) generate reactive oxygen species, and NRF2 antioxidant signalling modulates the oxidative component of the gouty inflammatory response."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Flare amplification: IL-6 released during the gout flare signals through JAK-STAT (IL-6 already mapped) to amplify the systemic inflammatory response."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Macrophage metabolic activation: mTOR-dependent metabolic reprogramming of urate-crystal-activated macrophages supports the inflammatory cytokine output and trained-immunity features of acute gout."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is released by urate-crystal-activated macrophages, amplifying the inflammation and contributing to tophus formation in gout."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling (mTOR mapped) participates in the macrophage priming that licenses NLRP3-inflammasome activation by urate crystals in gout."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling is engaged by urate-crystal sensing, contributing to the neutrophil and macrophage activation of the acute gout flare."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response amplifying the acute and chronic inflammation of gout."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA within neutrophil extracellular traps and damaged cells around urate crystals engages cGAS-STING, amplifying the sterile inflammation of the gout flare."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling participates in the resolution of the gout flare and the fibrotic encapsulation of chronic tophi."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the macrophage oxidative-stress and metabolic responses to monosodium urate crystals in gout."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling modulates the macrophage activation accompanying the crystal-induced inflammation of gout."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β participates in the NF-κB- and NLRP3-driven inflammatory signaling of the gout flare."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, linked to purine and energy metabolism, is dysregulated in the metabolic milieu that promotes hyperuricemia and gout."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the macrophage activation of the NLRP3-driven inflammation of gout."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates NLRP3-inflammasome activation and thereby the intensity of the acute gouty inflammatory response."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the neutrophil and macrophage activation of acute gouty inflammation."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the neutrophilic inflammation of the gouty joint."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the inflammatory responses of gout."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte recruitment into the inflamed joint of gout."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the innate immune activation of the crystal-induced inflammation of gout."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven synovial angiogenesis participates in the chronic joint inflammation and tophus biology of gout."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the innate-immune gene programs of gout."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the myeloid-cell activation and inflammatory responses of gout."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the neutrophil/macrophage crystal-induced inflammation and tophus formation of gout."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Uricosuric hormone: estrogen promotes renal uric-acid excretion, which is why gout is uncommon in premenopausal women and its incidence rises after menopause, one of the clearest sex and age patterns in the disease."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiovascular risk: hyperuricaemia and gout are associated with an increased risk of myocardial infarction and cardiovascular death, and troponin elevation marks the cardiac injury of these events that complicate the disease."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "Cardiorenal link: diuretics used for heart failure raise serum urate and precipitate gout, and hyperuricaemia tracks with heart-failure severity, so the natriuretic-peptide axis connects gout to the cardiorenal syndrome."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Renal urate handling: the renin-angiotensin-aldosterone system (angiotensin II already mapped) and volume status modulate renal urate excretion, and the diuretic-induced volume contraction that activates it raises serum urate and precipitates gout."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Metabolic treatment overlap: GLP-1 receptor agonists lower body weight and, with SGLT2 inhibitors (already mapped), reduce serum urate and gout flares, linking the incretin axis to the metabolic management of hyperuricaemia."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Renal-bone axis: the chronic kidney disease that both causes and results from gout disturbs the parathyroid hormone-calcium-phosphate axis, tying urate retention to the mineral-bone derangements of renal impairment."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Uric-acid endothelial dysfunction: soluble urate impairs endothelial nitric oxide (already mapped) and raises endothelin-1, promoting the vasoconstriction and hypertension (already mapped) through which hyperuricaemia contributes to cardiovascular risk."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "RAAS activation: hyperuricaemia activates the renin-angiotensin-aldosterone system (angiotensin-II and aldosterone already mapped), a mechanism linking urate to hypertension and renal afferent-arteriolar disease."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Systemic inflammation: gout is a systemic inflammatory state, and the acute-phase fibrinogen rises with the IL-6 and IL-1 (already mapped) of flares, part of the inflammatory burden that raises cardiovascular risk."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Flare resolution: IL-4 helps switch the macrophages (already mapped) toward the M2 phenotype that resolves the acute gout flare, the anti-inflammatory arm countering the NLRP3-IL-1 (already mapped) drive."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 resolution: IL-13, with IL-4 (already mapped), supports the M2 macrophage arm that clears the crystals and resolves the inflammation of the self-limiting gout flare."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic adipokine: resistin, with leptin and the fall in adiponectin (already mapped), is a pro-inflammatory adipokine of the metabolic syndrome (insulin already mapped) that accompanies and worsens the hyperuricaemia of gout."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate crystal response: type-I interferon is a component of the innate-immune (NLRP3 already mapped) response to the monosodium urate crystals, part of the inflammatory signalling of the gout flare."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron and metabolic syndrome: hepcidin, driven by the inflammation (IL-6 already mapped), governs the iron handling whose disturbance links the iron overload to the hyperuricaemia and metabolic syndrome (insulin already mapped) of gout."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell mediator: histamine from the mast cells (already mapped) contributes to the vasodilation and the early inflammation of the acute gout flare."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Tophaceous bone erosion: the RANKL from the tophus stroma drives the osteoclastic juxta-articular bone erosion of chronic tophaceous gout."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Chronic-tophus lymphocytes: the CD4 T-helper cells infiltrate the granulomatous tophus, the adaptive component complementing the innate (NLRP3 and IL-1 already mapped) crystal inflammation of chronic gout."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 granulomatous arm: the IFN-γ of the tophus T cells is the Th1 arm of the chronic granulomatous inflammation surrounding the urate crystals in tophaceous gout."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the chronic granulomatous tophus inflammation of gout."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the crystal-driven inflammation of gout, complementing the innate (NLRP3 and IL-1 already mapped) response."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the mixed immune response of gout."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment to the urate crystals in the acute gout flare."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin flare: the bradykinin-kinin system contributes to the vasodilation, pain and vascular permeability of the acute gout flare."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the mixed immune response of gout."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive arm: the cytotoxic T cells (perforin pathway) are part of the adaptive-immune infiltrate of the chronic tophaceous inflammation of gout."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) activated on the monosodium-urate crystals of gout."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact (bradykinin already mapped) systems activated by the monosodium-urate crystals of the acute gout flare."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate arm: the NK cells (perforin pathway) are part of the innate-immune response to the monosodium-urate crystals of gout."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Tophaceous remodelling: periostin, a matricellular mediator, is part of the joint and soft-tissue remodelling around the tophi (with osteopontin already mapped) of chronic tophaceous gout."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Metabolic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) linked to the hyperuricaemia and the metabolic-syndrome comorbidity of gout."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-gout axis: TSLP, from the urate crystal-stimulated mast cells (already mapped) and synovial epithelium, primes dendritic cells (already mapped) and amplifies the Th2 dimension of the gouty inflammation beyond the canonical NLRP3 (already mapped) neutrophilic flare."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-gout axis: erythropoietin, modulated by the CKD (already mapped) comorbidity and the HIF-1α (already mapped) renal hypoxia of gout-related nephropathy, links the renal anaemia and the disordered iron handling (hepcidin already mapped) of chronic tophaceous gout."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-gout axis: melatonin, via its anti-inflammatory action on macrophages (already mapped) and mast cells (already mapped), attenuates NLRP3 (already mapped) inflammasome activation and the ROS (xanthine oxidase already mapped) dimension of the acute gouty inflammation."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-gout axis: testosterone, via androgen receptor signalling on renal tubular urate transporters (SLC22A12/URAT1 pathway) and macrophages (already mapped), modulates renal urate reabsorption and the well-established male sex predominance of gout."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin-gout axis: serotonin, released by activated platelets (already mapped) during the acute gouty attack, amplifies the periarticular vascular response, pain signalling, and the NLRP3 (already mapped) inflammasome-driven inflammatory cascade of gout."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Prolactin-gout axis: prolactin, acting on macrophage (already mapped) prolactin receptors, amplifies NLRP3 (already mapped) inflammasome priming and the IL-1β (already mapped) cytokine burst of the acute gouty inflammatory attack."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Gout oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the acute gouty inflammatory cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neutrophil-dominated cascade of gout."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Gout vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates periarticular vascular tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-driven cascade of gout."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Gout selenium: selenium, via selenoprotein antioxidant activity in macrophages (already mapped) and neutrophils (already mapped), suppresses the oxidative amplification of the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Gout iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and neutrophil (already mapped) activity; iodine deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Gout copper: copper, as cofactor of SOD1 in macrophages (already mapped) and neutrophils (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome urate cascade of gout."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Gout potassium: potassium depletion promotes macrophage (already mapped) and neutrophil (already mapped) pro-inflammatory activation; potassium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3 cascade of gout."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Gout zinc: zinc cofactors antioxidant enzymes in macrophages (already mapped) and neutrophils (already mapped); zinc deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Gout iron: iron excess drives ROS generation in macrophages (already mapped) and neutrophils (already mapped), amplifying oxidative stress; iron dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Gout phosphorus: phosphorus, as ATP in macrophages (already mapped) and neutrophils (already mapped), fuels kinase signalling; phosphorus dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Gout carbon: carbon backbone of purine rings and urate anchors xanthine-oxidase flux in macrophages (already mapped) and neutrophils (already mapped); carbon-driven metabolite accumulation amplifies the NF-κB (already mapped) and NLRP3 inflammasome cascade of gout."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Gout chloride: chloride channels regulate macrophage (already mapped) and neutrophil (already mapped) volume during urate-crystal phagocytosis; chloride dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome signalling in gout."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Gout oxygen: NADPH-oxidase generates ROS in macrophages (already mapped) and neutrophils (already mapped) during urate-crystal phagocytosis; oxygen-derived ROS amplifies NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Gout sulfur: glutathione from sulfur amino acids scavenges ROS in macrophages (already mapped) and neutrophils (already mapped) during urate-crystal phagocytosis; sulfur deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Gout pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses gout-associated immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) inflammasome cascade of gout."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Gout wnt-beta-catenin: WNT/β-catenin in macrophages (already mapped) and neutrophils (already mapped) modulates urate-crystal inflammatory resolution; wnt dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Gout il-2: IL-2 from T-helper cells (already mapped) and macrophages (already mapped) drives lymphocyte expansion; il-2 deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) inflammasome cascade of gout."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Gout notch: NOTCH on macrophages (already mapped) and neutrophils (already mapped) modulates crystal-driven inflammation; notch dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Gout igf-1: IGF-1 from macrophages (already mapped) and synovial cells (already mapped) modulates urate-crystal metabolic response; igf-1 dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Gout fibronectin: fibronectin in macrophages (already mapped) and synovial cells (already mapped) promotes joint ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Gout activin-a: activin-A from macrophages (already mapped) and synovial cells (already mapped) promotes joint fibrosis; activin-a excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Gout cgrp: CGRP from synovial cells (already mapped) and macrophages (already mapped) modulates joint pain signalling; cgrp excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Gout calcitonin: calcitonin from synovial cells (already mapped) and macrophages (already mapped) modulates joint calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Gout substance-p: substance-P from synovial cells (already mapped) and macrophages (already mapped) modulates joint pain tone; substance-P excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Gout insulin-receptor: insulin receptor on macrophages (already mapped) and synovial cells (already mapped) drives metabolic tone; insulin-receptor loss amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Gout androgen-receptor: androgen receptor on macrophages (already mapped) and synovial cells (already mapped) modulates gout androgen axis; androgen-receptor loss amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Gout norepinephrine: norepinephrine from macrophages (already mapped) and synovial cells (already mapped) modulates joint stress tone; norepinephrine excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Gout adrenomedullin: adrenomedullin from macrophages (already mapped) and synovial cells (already mapped) modulates joint vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Gout bdnf: BDNF from macrophages (already mapped) and synovial cells (already mapped) modulates joint neural tone; bdnf excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Gout fgfr: FGFR from macrophages (already mapped) and synovial cells (already mapped) modulates joint repair signalling; fgfr excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Gout epinephrine: epinephrine from macrophages (already mapped) and synovial cells (already mapped) modulates joint adrenergic tone; epinephrine excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "Gout myostatin: myostatin from macrophages (already mapped) and synovial cells (already mapped) modulates joint fibrotic axis; myostatin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Gout angiopoietin: angiopoietin from macrophages (already mapped) and synovial cells (already mapped) modulates joint vascular tone; angiopoietin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Gout ghrelin: ghrelin from macrophages (already mapped) and synovial cells (already mapped) modulates joint metabolic axis; ghrelin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout."
---

# Gout

## Overview

**Gout** is the most common inflammatory arthritis in adults, affecting ~4% of adults in Western countries (>41 million affected globally). It is caused by **monosodium urate (MSU) crystal deposition** in joints and periarticular tissues, driven by chronic **hyperuricemia** (serum urate >6.8 mg/dL, the saturation threshold for MSU crystallization at physiological pH and temperature) [^dalbeth-2019-gout-primer].

**The gout spectrum:**
- **Asymptomatic hyperuricemia:** Elevated serum urate without crystals or gout; not routinely treated but associated with incident gout, CKD, hypertension, and cardiovascular events over time
- **Acute gouty arthritis (flare):** Sudden-onset, severely painful joint inflammation; typically monoarticular initially (classically first metatarsophalangeal joint = podagra ~50%); self-limiting (3-10 days without treatment)
- **Intercritical gout:** Asymptomatic period between flares; MSU crystals persist in joints; progressive joint damage accumulates with recurrent flares
- **Chronic tophaceous gout:** Tophi (MSU crystal deposits in periarticular soft tissue, subcutaneous tissue, olecranon bursa, auricles, tendons) → joint destruction, deformity, functional impairment; urate-lowering therapy (ULT) can dissolve tophi over months-years

**Hyperuricemia mechanisms:**
- **Underexcretion (~90% of gout):** Impaired renal urate excretion; major genetic contributors: ABCG2 (urate transporter, gout risk alleles), SLC22A12 (URAT1, urate reabsorber in proximal tubule — target of benzbromarone, probenecid), SLC2A9 (GLUT9); risk factors: CKD, diuretics (thiazide, loop → compete with urate for renal tubular secretion), cyclosporine, low-dose aspirin
- **Overproduction (~10% of gout):** Purine overproduction from rapid cell turnover (myeloproliferative disease, tumor lysis syndrome), HPRT1 deficiency (Lesch-Nyhan syndrome), PRPP synthetase superactivity; dietary purines (meat, seafood, organ meats, fructose-sweetened beverages — fructose → rapid ATP consumption → AMP → uric acid)
- **Alcohol:** Ethanol → lactate → blocks urate renal excretion; beer contains purines; wine less strongly associated
- **Comorbidities:** CKD, hypertension, metabolic syndrome, obesity, type 2 diabetes — all associated with hyperuricemia; gout disproportionately affects men (estrogen promotes uricosuria → lower serum urate in premenopausal women) and postmenopausal women

## Structure

### NLRP3 inflammasome activation by MSU crystals [^martinon-2006-nlrp3-gout]

The central mechanism linking MSU crystals to acute gouty arthritis is **NLRP3 inflammasome activation** — first definitively demonstrated in macrophages by Martinon and Tschopp in 2006 [^martinon-2006-nlrp3-gout].

**Mechanism:**
1. MSU crystals phagocytosed by synovial macrophages → crystals rupture phagolysosomes → **lysosomal destabilization** → cytosolic cathepsin B release → NLRP3 oligomerization
2. Crystal surface-mediated ROS generation (NADPH oxidase-dependent) + cholesterol crystal co-stimulation → additional NLRP3 priming
3. Potassium efflux (crystals insert into plasma membrane → K⁺ channels) → NLRP3 conformational change → ASC pyroptosome assembly → caspase-1 autoactivation
4. Active caspase-1 → IL-1beta (pro-IL-1beta → mature IL-1beta) + IL-18 + gasdermin D (pore formation → pyroptosis in some macrophages)
5. **IL-1beta** is the central acute gout mediator: binds synovial fibroblast and endothelial IL-1R1 → NF-kB → IL-6, IL-8 (CXCL8), ICAM-1 → massive neutrophil influx

**Two-signal model for maximal inflammasome activation:**
- **Signal 1 (priming):** TLR4/TLR2 ligands (MSU crystal surface, urate at lower concentrations, LPS co-stimulation) → NF-kB → pro-IL-1beta, NLRP3, and ASC transcription
- **Signal 2 (activation):** MSU crystal phagocytosis → lysosomal rupture → NLRP3 activation

**Resolution of acute gout (spontaneous within 7-10 days):**
- Neutrophils undergo NET formation and apoptosis → efferocytosis by macrophages → anti-inflammatory macrophage polarization → IL-10, TGF-beta → resolution
- Lipid mediators: transition from pro-inflammatory prostaglandins and leukotrienes → pro-resolving lipoxins and resolvins → self-limited flare

### Crystal properties

- MSU crystals: needle-shaped (monosodium urate monohydrate), negatively birefringent under polarized light (gold/yellow parallel to polarizer) — diagnostic by synovial fluid microscopy; length 2-20 μm
- CPPD crystals (calcium pyrophosphate, pseudogout): rhomboid-shaped, weakly positively birefringent — distinct from gout; associated with OA, hemochromatosis, hyperparathyroidism

## Function

### Clinical presentation

**Acute gouty flare:**
- Sudden, severe pain (often awakening at night), swelling, erythema, warmth → maximal intensity within 12-24 hours
- First MTP joint (podagra) most common; also ankle, midfoot, knee; wrist, finger (less common initially; more frequent in patients on diuretics, transplant recipients)
- **Fever** (low-grade) and leukocytosis may be present → mimics septic arthritis (always aspirate if uncertain; gout and septic arthritis can co-exist)
- Precipitating triggers: alcohol (especially beer), dietary purine load, dehydration, illness/surgery (acute serum urate change), starting or stopping ULT (crystal mobilization)

**Tophi:**
- Whitish chalk-like deposits in periarticular tissue, extensor surfaces, olecranon bursa, ear cartilage (helix), tendons (Achilles, finger tendons)
- MSU crystal aggregates surrounded by chronic granulomatous inflammation; may ulcerate and drain chalky material; can destroy cartilage and bone
- **DECT (dual-energy CT):** Differentiates MSU (green coding) from calcium crystals → non-invasive tophus detection and monitoring; superior to ultrasound and plain X-ray for tophus burden

**Radiographic findings (late disease):**
- Punched-out erosions with sclerotic margins and overhanging edges (Martel sign) — pathognomonic for tophaceous gout; first MTP most common
- Tophaceous deposits as soft-tissue opacities; cartilage and joint space often preserved until late (unlike OA/RA)

## Pathology

### Diagnosis

**Gold standard:** Synovial fluid or tophus aspiration → polarized light microscopy demonstrating needle-shaped, negatively birefringent MSU crystals within or adjacent to neutrophils during acute flare.

**2015 ACR/EULAR Gout Classification Criteria:** Score-based (score ≥8/23 = gout); domains: clinical (joint involvement, synovitis characteristics), laboratory (serum urate, leukocytes in synovial fluid), imaging (ultrasound double contour sign, DECT urate deposits, X-ray erosions). Crystal demonstration = definitive classification regardless of score.

**Serum urate:** Cannot rule out gout during acute flare (urate may be normal or low during acute flare due to acute phase response → uricosuria); repeat when patient has recovered.

**Ultrasonography:** Double contour sign (urate coating on cartilage) and snowstorm appearance (hyperechoic foci in synovial fluid) — sensitive and specific for MSU deposits.

### Treatment [^fitzgerald-2020-acr-gout]

**Acute flare treatment:**
- **Colchicine (low-dose, 1.2 mg then 0.6 mg 1 hour later):** First-line; tubulin polymerization inhibitor → inhibits neutrophil chemotaxis, NLRP3 inflammasome assembly (microtubule-dependent), and inflammasome-mediated IL-1beta secretion; must be initiated within 36 hours of flare onset for maximal effect; avoid in severe renal/hepatic impairment; CYP3A4/P-gp substrate
- **NSAIDs (indomethacin, naproxen, celecoxib):** First-line alternative; COX inhibition → reduced prostaglandin-mediated vasodilation and pain; avoid in CKD, heart failure, GI ulcer history
- **Corticosteroids (prednisone 30-40 mg/day × 5-7 days):** Preferred when colchicine and NSAIDs are contraindicated (e.g., severe CKD, anticoagulated patients); intra-articular triamcinolone effective for monoarthritis
- **IL-1 inhibitors:** Anakinra (anti-IL-1R), canakinumab (anti-IL-1beta) → highly effective in recurrent refractory gout; canakinumab (Novartis) approved in EU for gout flares; anakinra used off-label; especially valuable in transplant patients (colchicine and NSAIDs contraindicated due to immunosuppressants and renal function)

**Urate-lowering therapy (ULT) — for recurrent or tophaceous gout:**
- **Indications (2020 ACR):** ≥2 flares/year, 1+ tophi, radiographic evidence of joint damage from gout, serum urate >9 mg/dL, or uric acid nephrolithiasis
- **Target serum urate:** <6 mg/dL (<5 mg/dL in tophaceous gout) for crystal dissolution
- **Allopurinol (xanthine oxidase inhibitor):** First-line; blocks urate synthesis; start low (100 mg/day) → titrate monthly to target; HLA-B*5801 screening required before use in Asian patients (SJS/TENS risk: 1-2% in HLA-B*5801 carriers); dose adjust for eGFR; drug interactions: azathioprine (XO inactivation → azathioprine toxicity → reduce azathioprine dose 75% if co-prescribed)
- **Febuxostat (Uloric):** Non-purine XO inhibitor; more potent than allopurinol at equivalent doses; CARES trial: non-inferior to allopurinol for gout endpoints but possible increased CV mortality signal → now boxed warning; reserved for allopurinol-intolerant patients
- **Uricosurics:** Probenecid (URAT1 inhibitor), benzbromarone (uricosuric, not available in US) — increase renal urate excretion; less effective in CKD; avoided with nephrolithiasis history
- **Pegloticase (Krystexxa):** Pegylated recombinant uricase; converts urate → allantoin (soluble) → dramatic serum urate lowering; IV Q2W; for refractory/tophaceous gout; anti-drug antibodies → loss of efficacy and infusion reactions in ~40%; co-administration with methotrexate reduces immunogenicity and improves durability (MIRROR trial); G6PD testing required (hemolysis risk)
- **Flare prophylaxis during ULT initiation (mandatory for ≥3-6 months):** Low-dose colchicine (0.6 mg QD-BID) or NSAID; urate mobilization from established deposits during ULT initiation triggers flares; this prophylaxis sharply reduces flare incidence during the critical ULT initiation period

## Connections

- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — MSU crystals are a canonical NLRP3 activator: lysosomal destabilization → cathepsin B → NLRP3-ASC-caspase-1 → IL-1beta secretion; IL-1 blockade (anakinra, canakinumab) rapidly resolves refractory gouty flares.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Synovial macrophages phagocytose MSU crystals → NLRP3 → IL-1beta; surface-activated macrophages produce IL-6, TNF-alpha, CXCL1 → neutrophil recruitment; colchicine blocks macrophage microtubule-dependent NLRP3 assembly.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils are the primary effectors of acute gout: IL-8/CXCL1 → neutrophil influx → MSU crystal phagocytosis → ROS and proteases → tissue damage; colchicine inhibits neutrophil migration and crystal phagocytosis via microtubule disruption.
- `connects-to` → **[NF-kB](../../03-molecular/nf-kb/README.md)** — MSU crystals activate NF-kB in macrophages and synoviocytes via TLR4 → IL-6, IL-8, TNF-alpha, COX-2 → synovial inflammation; NF-kB drives both acute flare cytokines and chronic tophus-associated tissue remodeling.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — xanthine oxidase converts xanthine → uric acid; serum urate >6.8 mg/dL exceeds solubility threshold → MSU crystal nucleation in joints and soft tissue → phagocytosis by neutrophils and macrophages → NLRP3 activation → acute gouty flare; allopurinol/febuxostat target XOR.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β is the central acute gout mediator: MSU crystals → NLRP3 → caspase-1 → IL-1β → neutrophil influx and arthritis; anakinra (off-label) and canakinumab (EMA approved 2013 for gout flares) target IL-1β in refractory flares unresponsive to colchicine/NSAIDs.
- `treated-by` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — NSAIDs including ibuprofen are first-line for acute gout (ACR 2020 guidelines): COX-2-driven PGE₂ amplifies NLRP3-IL-1β neutrophil recruitment to MSU crystals; 600–800 mg TDS × 7–10 days effective; contraindicated in eGFR <30.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Gout and hypertension are tightly linked: hyperuricemia independently raises blood pressure (urate impairs endothelial NO and activates the RAAS), while thiazide/loop diuretics for HTN raise serum urate and trigger gout flares — a two-way interaction that complicates treatment.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is central to gout: it excretes ~two-thirds of uric acid, so reduced urate clearance (URAT1/GLUT9 variants, CKD, diuretics) is the main cause of hyperuricemia; conversely MSU crystals damage the kidney (urate nephropathy, stones), so gout and CKD reinforce each other.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Gout is the most common inflammatory arthritis: MSU crystals deposit in cooler peripheral joints — classically the first metatarsophalangeal joint (podagra) — igniting excruciating attacks, and over years form tophi that erode bone and cartilage if urate isn't lowered.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Gout and chronic kidney disease feed each other: reduced renal urate excretion raises serum urate to cause gout, while urate crystals and inflammation injure the kidney; CKD also limits NSAID and colchicine use, so urate-lowering with allopurinol must be dose-adjusted.
- `connects-to` → **[Obesity](../obesity/README.md)** — Gout is a core feature of metabolic syndrome anchored by obesity: adiposity and insulin resistance raise serum urate by cutting renal excretion and boosting purine turnover, so weight loss lowers urate and flares; gout clusters with type 2 diabetes, hypertension and fatty liver.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Hyperuricemia and gout independently raise cardiovascular risk: urate crystals and NLRP3-driven inflammation promote endothelial dysfunction and atherosclerosis, and gout patients have excess MI and stroke—part of why gout is seen as a vascular as well as joint disease.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Gout is literally a sodium disease: when uric acid exceeds its solubility it crystallizes as monosodium urate, and these needle-shaped MSU crystals deposited in joints and tophi trigger the NLRP3-driven inflammation—dissolving them by lowering urate is the cure.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Gout and rheumatoid arthritis are both inflammatory arthritides but distinct: gout is a crystal-driven (MSU) innate attack with acute monoarticular flares, while RA is an autoantibody-driven symmetric polyarthritis—aspiration versus serology separates them.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Gout clusters with type 2 diabetes in the metabolic syndrome: insulin resistance reduces renal uric-acid excretion, raising urate, while obesity and high-purine, fructose-rich diets drive both—gout often flags an underlying cardiometabolic disorder.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol is a classic gout trigger: beer (rich in purines) and spirits raise uric acid by boosting production and blocking renal excretion, so binges precipitate acute attacks—making alcohol moderation a core part of gout prevention.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Gout signals and worsens heart disease: hyperuricemia and urate-crystal inflammation track with hypertension, coronary disease and higher cardiovascular mortality, so a gout diagnosis flags cardiovascular risk—and shared drivers like obesity link the two.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Gout has a calcium-crystal mimic, pseudogout: where gout deposits monosodium urate crystals, pseudogout (CPPD) deposits calcium pyrophosphate, causing similar acute joint inflammation—so polarized-light crystal analysis distinguishes the two arthritides.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Gout is strongly tied to cardiovascular disease: hyperuricemia and the chronic inflammation of gout independently raise the risk of hypertension, coronary disease and stroke, so gout flags cardiovascular risk beyond its joint and kidney damage.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The renal system both causes and suffers from gout: under-excretion of urate by the kidney is the main reason uric acid rises, and deposited crystals form kidney stones and urate nephropathy—so gout and kidney disease drive each other in a vicious cycle.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Tophi are the chronic granulomas of gout: persistent urate crystals provoke macrophages and fibroblasts to wall them off in firm, fibrous nodular deposits in joints and soft tissue, so fibroblast-rich tophi mark long-standing, undertreated disease.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Gout is a disease of nitrogen waste: uric acid is the nitrogen-rich end-product of purine breakdown that humans, lacking uricase, cannot degrade further, so this evolutionary loss leaves urate to crystallize in joints when it builds up.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Myeloproliferative neoplasms cause secondary gout: massive cell turnover in polycythemia vera and related disorders floods the blood with purines and urate, so gout flares can be the first clue to an underlying blood-cell overproduction.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Chronic gout deposits in the skin as tophi: long-standing high urate forms chalky subcutaneous nodules over joints and ears that can ulcerate and discharge crystals, so visible tophi mark years of untreated disease.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Gout flares can be quelled with cortisol: when NSAIDs and colchicine are unsafe—as in kidney disease—corticosteroids (oral or injected into the joint) calm the crystal-driven inflammation, a key fallback for treating an acute attack.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Chronic tophaceous gout erodes bone via osteoclasts: long-standing urate deposits activate bone-resorbing osteoclasts, carving the 'punched-out' periarticular erosions seen on X-ray that distinguish advanced gout from other arthritis.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Gout traces back to purine metabolism through adenosine: breaking down adenosine and other purines yields uric acid, so a high turnover of these nucleotides—from diet or cell breakdown—feeds the hyperuricemia that precipitates urate crystals.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut shares the job of clearing urate with the kidney: about a third of uric acid is excreted into the intestine, so gut transporters and microbes that break down urate influence blood levels—and impaired gut excretion can worsen gout.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 helps inflame the gouty joint: alongside IL-1beta, urate crystals trigger IL-6 release that amplifies the fever, pain and swelling of an acute attack, part of the cytokine cascade targeted to calm flares.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help ignite the gout flare: they take up monosodium urate crystals and, with macrophages, activate the inflammasome and prime the inflammatory response that turns crystal deposition into a sudden painful attack.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Acid urine turns gout into kidney stones: uric acid dissolves poorly when urine is acidic, so a low urinary pH lets it crystallize into stones, which is why alkalinizing the urine helps prevent them.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Chronic gout lays down fibrosis: long-standing tophi become fibrous nodules that erode joints, and persistent urate in the kidney drives interstitial scarring, the lasting damage beyond the acute flare.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells help fire the first hours of a gout attack: urate crystals trigger them to release histamine and mediators that dilate vessels and recruit neutrophils, kicking off the sudden inflammation.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Gout is confirmed by light: polarized-light microscopy of joint fluid reveals the negatively birefringent urate needles, and dual-energy CT photons map urate deposits without a tap.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Gout can spring from the marrow: myeloproliferative diseases and their rapid cell turnover flood the blood with purines that become uric acid, a secondary cause of the disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Gout can deposit in the eye: urate tophi form on the eyelids and conjunctiva and rarely inflame the sclera, an unusual but recognized site of crystal deposition.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron and polarized-light microscopy clinch the gout diagnosis: aspirated joint fluid shows needle-shaped monosodium urate crystals, negatively birefringent and packed into the tophi that the inflammasome attacks.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver makes the uric acid that crystallizes in gout: it is the main site where xanthine oxidase breaks purines down to urate, so the liver's metabolism — fueled by fructose and alcohol — sets the blood level.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Low magnesium tracks with gout: deficiency is common in the metabolic syndrome that accompanies it and is linked to higher uric acid, so magnesium status is part of the metabolic picture behind the crystals.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Treating the flare punishes the gut: colchicine causes diarrhea and the NSAIDs used for acute gout inflame the stomach into gastritis and ulcers, so the drugs that quell the joint must be balanced against the bowel.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Body fat fuels hyperuricemia: adipose tissue's inflammation and the insulin resistance of obesity cut the kidney's excretion of urate, which is why weight gain raises uric acid and weight loss helps lower it.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Gout rides with insulin resistance: the hyperinsulinemia of metabolic syndrome makes the kidney retain urate, tying the pancreatic insulin axis to the crystals — and gout flags a higher risk of type 2 diabetes.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Estrogen shields women from gout: the hormone is uricosuric, helping the kidney dump urate, so gout is uncommon before menopause and its incidence in women climbs once that protection is lost.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Rapid skin turnover feeds the urate pool: psoriasis's accelerated proliferation breaks down purines into extra uric acid, so gout is more common in psoriasis — and the two arthritides can be hard to tell apart in an inflamed joint.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Crystals also rouse the complement system: monosodium urate activates complement on its surface, generating C5a that pulls neutrophils into the joint — an arm of the acute flare working alongside the NLRP3-IL-1 pathway.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF amplifies the crystal storm: released by activated macrophages alongside IL-1β, it deepens the recruitment and activation of neutrophils that make the gout flare so exquisitely painful.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Urate injures the vessel lining: high uric acid impairs endothelial nitric-oxide and promotes inflammation, a mechanism tying gout to the hypertension and cardiovascular disease that shadow it.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The gut is gout's second drain: about a third of uric acid is excreted through the intestine via the ABCG2 transporter, so impaired gut elimination — not just the kidney — can raise urate into gout.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance fuels hyperuricemia: high insulin tells the kidney to retain urate, so the hyperinsulinemia of metabolic syndrome raises uric acid into gout — one reason gout clusters with obesity and type 2 diabetes.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — High cell turnover overproduces urate: the expanded marrow of polycythemia vera and other myeloproliferative disease floods the blood with purines, causing a secondary gout that can be the presenting clue to the hematologic disorder.
- `connects-to` → **[Stroke](../stroke/README.md)** — Hyperuricemia is an independent vascular risk: beyond its joint disease, elevated urate promotes endothelial dysfunction and is associated with a raised risk of stroke, part of gout's broader cardiovascular shadow.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Urate and the failing heart feed each other: hyperuricemia independently predicts heart failure and worsens its outcomes, while the disease and its diuretics raise urate — a bidirectional link in gout's cardiovascular burden.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A hot joint forces a critical question: acute gout closely mimics septic arthritis, which must be excluded by joint aspiration because a missed joint infection can seed sepsis, and tophi themselves can become infected.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Gouty inflammation tips toward clotting: the systemic inflammation of gout and hyperuricemia is associated with a higher risk of venous thromboembolism, adding a venous dimension to its vascular complications.
- `connects-to` → **[NASH](../nash/README.md)** — Hyperuricemia and fatty liver cluster: gout sits squarely in the metabolic syndrome, and its insulin resistance and fructose metabolism strongly associate it with non-alcoholic steatohepatitis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Recurrent disabling pain weighs on mood: the unpredictable, intensely painful flares and chronic joint damage of tophaceous gout reduce quality of life and carry an elevated rate of depression.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic inflammation and renal disease lower the count: longstanding tophaceous gout's persistent inflammation, compounded by the chronic kidney disease that so often accompanies it, can produce an anemia of chronic disease.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Tophi erode through the skin: large chronic tophi can ulcerate and discharge chalky urate, leaving open wounds over joints that are slow to heal and prone to infection.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Ulcerated tophi invite Staph: when a tophus breaks through the skin, Staphylococcus aureus readily colonizes and infects it, risking cellulitis, septic arthritis and bloodstream infection.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Chronic inflammation and immobility cost bone: longstanding gout's persistent inflammation, joint damage and reduced mobility are associated with lower bone density and a raised fracture risk.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Urate crystals trip the innate alarm: monosodium urate crystals activate the NLRP3 inflammasome to release IL-1β, the autoinflammatory burst that drives the acute gout flare and the target of IL-1 blockers.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Both the diet and the drugs hit the gut: purine- and fructose-rich food and alcohol drive hyperuricaemia, while colchicine causes diarrhoea and the NSAIDs used in flares inflame the stomach.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is woven into metabolic disease: hyperuricaemia is tightly linked to insulin resistance and the metabolic syndrome, so gout clusters with the endocrine disturbances of obesity and diabetes.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It deposits chalky lumps under the skin: tophi — subcutaneous urate crystal deposits on the ear helix, fingers and Achilles tendon — can ulcerate and discharge a white pasty material in chronic gout.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can rarely reach the spine: tophaceous urate deposits in the spine can compress nerve roots or the spinal cord, an uncommon but serious neurological complication of long-standing gout.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Sleep apnoea feeds it: obstructive sleep apnoea raises uric acid through intermittent hypoxia and nucleotide turnover, triggering nocturnal gout flares.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids treat the flare when others can't: oral or intra-articular corticosteroids relieve acute gout for patients in whom NSAIDs and colchicine are contraindicated, such as in kidney disease.
- `connects-to` → **[Quercetin](../../../03-medicine/03-food/quercetin/README.md)** — A dietary urate-lowering flavonoid: quercetin inhibits xanthine oxidase, the same enzyme blocked by allopurinol, and trials show it modestly lowers serum uric acid.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet can calm the inflammation: omega-3 fatty acids have anti-inflammatory effects studied for reducing gout flare frequency, complementing urate-lowering therapy.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — High cell turnover floods urate: myeloproliferative neoplasms like essential thrombocythaemia overproduce cells whose breakdown raises uric acid, a frequent secondary cause of gout.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Inflammatory arthritis to tell apart: gout and psoriatic arthritis both inflame the joints, psoriasis itself raises urate, and the two enter each other's differential and can coexist.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Crystals erode the bone: chronic tophaceous gout deposits urate beside joints, producing the punched-out juxta-articular bone erosions with overhanging edges characteristic of the disease.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — The kidney both makes and suffers gout: about 90% of hyperuricaemia is renal under-excretion of urate, while deposited urate crystals cause interstitial inflammation and chronic urate nephropathy that scars the glomerulus and lowers filtration.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Urate inflames the vessel wall: soluble urate and monosodium urate crystals promote endothelial dysfunction and NLRP3-driven inflammation in the arterial wall, a mechanistic link between hyperuricaemia and the atherosclerosis and hypertension that accompany gout.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Cell turnover floods the blood with urate: myelofibrosis and other myeloproliferative neoplasms massively increase purine breakdown, raising serum urate and causing secondary gout—worsened further by cytoreductive therapy that lyses cells.
- `connects-to` → **[AML](../aml/README.md)** — Tumour lysis hyperuricaemia: the rapid cell turnover of acute leukaemia and its chemotherapy floods the blood with purines and urate, triggering acute gout and urate nephropathy—prevented with allopurinol or rasburicase.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Urate and the arrhythmic heart: hyperuricaemia and gout are linked to atrial fibrillation through systemic NLRP3-driven inflammation and shared metabolic risk.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The gut excretes urate too: about a third of uric acid is cleared through the intestinal epithelium via the ABCG2 transporter, so gut dysfunction shifts the urate load onto the kidney and worsens gout.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Hyperuricaemia of high cell turnover: chronic haemolysis in sickle cell disease, like myeloproliferative disease, raises serum urate and causes secondary gout and urate nephropathy.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Tophi compress nerves: large tophaceous urate deposits can entrap peripheral nerves—classically carpal tunnel syndrome at the wrist—a mechanical complication of long-standing chronic gout.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Shared inflammasome biology: gout's anti-inflammatory colchicine was repurposed and trialled for COVID-19's hyperinflammation, the two diseases linked through NLRP3-inflammasome and IL-1β signalling.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — RAAS and urate handling: angiotensin II links hyperuricaemia to hypertension and renal urate retention, and the ARB losartan is uniquely uricosuric, lowering urate while treating blood pressure.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adiposity and urate: leptin, elevated in obesity, is associated with hyperuricaemia and gout, helping explain why excess body fat raises the risk of crystal disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Recruiting the flare: CCL2 (MCP-1) draws monocytes and macrophages to deposited urate crystals, amplifying the neutrophil-rich acute inflammation of a gout attack.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — Urate-lowering bonus: SGLT2 inhibitors increase urinary urate excretion and lower serum urate, reducing gout flares—an unexpected benefit of these diabetes and heart drugs.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Inflamed-joint hypoxia: the acutely inflamed gouty joint becomes hypoxic, stabilising HIF-1α in infiltrating cells and amplifying the inflammatory response to urate crystals.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Tophus and fibrosis: TGF-β contributes to the chronic granulomatous tophus and to the renal fibrosis of chronic urate nephropathy in long-standing gout.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Neutrophil flare and resolution: S100A8/A9 from the neutrophils flooding the gouty joint amplifies the acute flare, while aggregated neutrophil extracellular traps also drive its spontaneous resolution.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Crystal complement activation: monosodium urate crystals directly activate complement through to C5, generating chemoattractants that recruit the neutrophils igniting the acute gout attack.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory mediators: prostaglandins generated in the urate-inflamed joint drive the pain, vasodilation and swelling of an acute gout flare, the target of the NSAIDs used to treat it.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Monosodium urate crystals engage TLR2/TLR4 to provide the "signal 1" that primes the NLRP3 inflammasome, licensing the IL-1β release that drives the explosive, exquisitely painful acute gout flare.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Hyperuricemia reduces endothelial nitric-oxide bioavailability, a vascular mechanism linking gout to its strong epidemiological association with hypertension, chronic kidney disease, and cardiovascular events.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Gout clusters with the dyslipidemia and insulin resistance of metabolic syndrome, the shared physiology behind the high cardiovascular risk that accompanies chronic hyperuricemia beyond the joint disease itself.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Glucocorticoids acting through the glucocorticoid receptor are a mainstay for acute gout flares, especially when NSAIDs and colchicine are contraindicated, broadly suppressing the urate-crystal-triggered inflammation.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Gout (monosodium urate crystals) must be distinguished from pseudogout, in which calcium pyrophosphate crystals provoke a similar acute crystal arthritis—a key distinction made on polarized-light microscopy of joint fluid.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — Monosodium urate crystals and the DAMPs of crystal-induced cell injury signal through RAGE to amplify the NF-κB-driven inflammation, adding to the NLRP3-IL-1β axis that drives the intense pain of a gout flare.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4 and the IL-1 receptor (TLR4 mapped) signal through MyD88 to activate NF-κB (mapped), the adaptor relaying the crystal-triggered danger signal into the cytokine output of a gout flare.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17-producing cells help recruit the dense neutrophil infiltrate that, ingesting urate crystals, produces the acute, intensely painful joint inflammation of gout.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Gout is tightly tied to metabolic syndrome (insulin and leptin mapped), and the low adiponectin of visceral adiposity reflects the adipose-driven milieu that raises urate and sustains inflammation.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Urate crystals and xanthine-oxidase activity (already mapped) generate reactive oxygen species, and NRF2 antioxidant signaling modulates the oxidative component of the gouty inflammatory response.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 released during the gout flare signals through JAK-STAT (IL-6 already mapped) to amplify the systemic inflammatory response.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-dependent metabolic reprogramming of urate-crystal-activated macrophages supports the inflammatory cytokine output and trained-immunity features of acute gout.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is released by urate-crystal-activated macrophages, amplifying the inflammation and contributing to tophus formation in gout.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling (mTOR mapped) participates in the macrophage priming that licenses NLRP3-inflammasome activation by urate crystals in gout.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling is engaged by urate-crystal sensing, contributing to the neutrophil and macrophage activation of the acute gout flare.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response amplifying the acute and chronic inflammation of gout.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA within neutrophil extracellular traps and damaged cells around urate crystals engages cGAS-STING, amplifying the sterile inflammation of the gout flare.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling participates in the resolution of the gout flare and the fibrotic encapsulation of chronic tophi.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the macrophage oxidative-stress and metabolic responses to monosodium urate crystals in gout.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling modulates the macrophage activation accompanying the crystal-induced inflammation of gout.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β participates in the NF-κB- and NLRP3-driven inflammatory signaling of the gout flare.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, linked to purine and energy metabolism, is dysregulated in the metabolic milieu that promotes hyperuricemia and gout.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the macrophage activation of the NLRP3-driven inflammation of gout.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates NLRP3-inflammasome activation and thereby the intensity of the acute gouty inflammatory response.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the neutrophil and macrophage activation of acute gouty inflammation.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the neutrophilic inflammation of the gouty joint.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the inflammatory responses of gout.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte recruitment into the inflamed joint of gout.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the innate immune activation of the crystal-induced inflammation of gout.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven synovial angiogenesis participates in the chronic joint inflammation and tophus biology of gout.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the innate-immune gene programs of gout.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the myeloid-cell activation and inflammatory responses of gout.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the neutrophil/macrophage crystal-induced inflammation and tophus formation of gout.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Uricosuric hormone: estrogen promotes renal uric-acid excretion, which is why gout is uncommon in premenopausal women and its incidence rises after menopause, one of the clearest sex and age patterns in the disease.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiovascular risk: hyperuricaemia and gout are associated with an increased risk of myocardial infarction and cardiovascular death, and troponin elevation marks the cardiac injury of these events that complicate the disease.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — Cardiorenal link: diuretics used for heart failure raise serum urate and precipitate gout, and hyperuricaemia tracks with heart-failure severity, so the natriuretic-peptide axis connects gout to the cardiorenal syndrome.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Renal urate handling: the renin-angiotensin-aldosterone system (angiotensin II already mapped) and volume status modulate renal urate excretion, and the diuretic-induced volume contraction that activates it raises serum urate and precipitates gout.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Metabolic treatment overlap: GLP-1 receptor agonists lower body weight and, with SGLT2 inhibitors (already mapped), reduce serum urate and gout flares, linking the incretin axis to the metabolic management of hyperuricaemia.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Renal-bone axis: the chronic kidney disease that both causes and results from gout disturbs the parathyroid hormone-calcium-phosphate axis, tying urate retention to the mineral-bone derangements of renal impairment.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Uric-acid endothelial dysfunction: soluble urate impairs endothelial nitric oxide (already mapped) and raises endothelin-1, promoting the vasoconstriction and hypertension (already mapped) through which hyperuricaemia contributes to cardiovascular risk.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — RAAS activation: hyperuricaemia activates the renin-angiotensin-aldosterone system (angiotensin-II and aldosterone already mapped), a mechanism linking urate to hypertension and renal afferent-arteriolar disease.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Systemic inflammation: gout is a systemic inflammatory state, and the acute-phase fibrinogen rises with the IL-6 and IL-1 (already mapped) of flares, part of the inflammatory burden that raises cardiovascular risk.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Flare resolution: IL-4 helps switch the macrophages (already mapped) toward the M2 phenotype that resolves the acute gout flare, the anti-inflammatory arm countering the NLRP3-IL-1 (already mapped) drive.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 resolution: IL-13, with IL-4 (already mapped), supports the M2 macrophage arm that clears the crystals and resolves the inflammation of the self-limiting gout flare.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic adipokine: resistin, with leptin and the fall in adiponectin (already mapped), is a pro-inflammatory adipokine of the metabolic syndrome (insulin already mapped) that accompanies and worsens the hyperuricaemia of gout.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate crystal response: type-I interferon is a component of the innate-immune (NLRP3 already mapped) response to the monosodium urate crystals, part of the inflammatory signalling of the gout flare.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron and metabolic syndrome: hepcidin, driven by the inflammation (IL-6 already mapped), governs the iron handling whose disturbance links the iron overload to the hyperuricaemia and metabolic syndrome (insulin already mapped) of gout.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell mediator: histamine from the mast cells (already mapped) contributes to the vasodilation and the early inflammation of the acute gout flare.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Tophaceous bone erosion: the RANKL from the tophus stroma drives the osteoclastic juxta-articular bone erosion of chronic tophaceous gout.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Chronic-tophus lymphocytes: the CD4 T-helper cells infiltrate the granulomatous tophus, the adaptive component complementing the innate (NLRP3 and IL-1 already mapped) crystal inflammation of chronic gout.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 granulomatous arm: the IFN-γ of the tophus T cells is the Th1 arm of the chronic granulomatous inflammation surrounding the urate crystals in tophaceous gout.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the chronic granulomatous tophus inflammation of gout.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the crystal-driven inflammation of gout, complementing the innate (NLRP3 and IL-1 already mapped) response.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the mixed immune response of gout.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment to the urate crystals in the acute gout flare.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin flare: the bradykinin-kinin system contributes to the vasodilation, pain and vascular permeability of the acute gout flare.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the mixed immune response of gout.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive arm: the cytotoxic T cells (perforin pathway) are part of the adaptive-immune infiltrate of the chronic tophaceous inflammation of gout.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) activated on the monosodium-urate crystals of gout.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact (bradykinin already mapped) systems activated by the monosodium-urate crystals of the acute gout flare.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate arm: the NK cells (perforin pathway) are part of the innate-immune response to the monosodium-urate crystals of gout.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Tophaceous remodelling: periostin, a matricellular mediator, is part of the joint and soft-tissue remodelling around the tophi (with osteopontin already mapped) of chronic tophaceous gout.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Metabolic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) linked to the hyperuricaemia and the metabolic-syndrome comorbidity of gout.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-gout axis: TSLP, from the urate crystal-stimulated mast cells (already mapped) and synovial epithelium, primes dendritic cells (already mapped) and amplifies the Th2 dimension of the gouty inflammation beyond the canonical NLRP3 (already mapped) neutrophilic flare.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-gout axis: erythropoietin, modulated by the CKD (already mapped) comorbidity and the HIF-1α (already mapped) renal hypoxia of gout-related nephropathy, links the renal anaemia and the disordered iron handling (hepcidin already mapped) of chronic tophaceous gout.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-gout axis: melatonin, via its anti-inflammatory action on macrophages (already mapped) and mast cells (already mapped), attenuates NLRP3 (already mapped) inflammasome activation and the ROS (xanthine oxidase already mapped) dimension of the acute gouty inflammation.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-gout axis: testosterone, via androgen receptor signalling on renal tubular urate transporters (SLC22A12/URAT1 pathway) and macrophages (already mapped), modulates renal urate reabsorption and the well-established male sex predominance of gout.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin-gout axis: serotonin, released by activated platelets (already mapped) during the acute gouty attack, amplifies the periarticular vascular response, pain signalling, and the NLRP3 (already mapped) inflammasome-driven inflammatory cascade of gout.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Prolactin-gout axis: prolactin, acting on macrophage (already mapped) prolactin receptors, amplifies NLRP3 (already mapped) inflammasome priming and the IL-1β (already mapped) cytokine burst of the acute gouty inflammatory attack.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Gout oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the acute gouty inflammatory cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neutrophil-dominated cascade of gout.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Gout vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates periarticular vascular tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-driven cascade of gout.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Gout selenium: selenium, via selenoprotein antioxidant activity in macrophages (already mapped) and neutrophils (already mapped), suppresses the oxidative amplification of the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Gout iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and neutrophil (already mapped) activity; iodine deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Gout copper: copper, as cofactor of SOD1 in macrophages (already mapped) and neutrophils (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome urate cascade of gout.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Gout potassium: potassium depletion promotes macrophage (already mapped) and neutrophil (already mapped) pro-inflammatory activation; potassium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3 cascade of gout.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Gout zinc: zinc cofactors antioxidant enzymes in macrophages (already mapped) and neutrophils (already mapped); zinc deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Gout iron: iron excess drives ROS generation in macrophages (already mapped) and neutrophils (already mapped), amplifying oxidative stress; iron dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Gout phosphorus: phosphorus, as ATP in macrophages (already mapped) and neutrophils (already mapped), fuels kinase signalling; phosphorus dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Gout carbon: carbon backbone of purine rings and urate anchors xanthine-oxidase flux in macrophages (already mapped) and neutrophils (already mapped); carbon-driven metabolite accumulation amplifies the NF-κB (already mapped) and NLRP3 inflammasome cascade of gout.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Gout chloride: chloride channels regulate macrophage (already mapped) and neutrophil (already mapped) volume during urate-crystal phagocytosis; chloride dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome signalling in gout.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Gout oxygen: NADPH-oxidase generates ROS in macrophages (already mapped) and neutrophils (already mapped) during urate-crystal phagocytosis; oxygen-derived ROS amplifies NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Gout sulfur: glutathione from sulfur amino acids scavenges ROS in macrophages (already mapped) and neutrophils (already mapped) during urate-crystal phagocytosis; sulfur deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) NLRP3-inflammasome cascade of gout.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Gout pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses gout-associated immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) inflammasome cascade of gout.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Gout wnt-beta-catenin: WNT/β-catenin in macrophages (already mapped) and neutrophils (already mapped) modulates urate-crystal inflammatory resolution; wnt dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Gout il-2: IL-2 from T-helper cells (already mapped) and macrophages (already mapped) drives lymphocyte expansion; il-2 deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) inflammasome cascade of gout.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — Gout notch: NOTCH on macrophages (already mapped) and neutrophils (already mapped) modulates crystal-driven inflammation; notch dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Gout igf-1: IGF-1 from macrophages (already mapped) and synovial cells (already mapped) modulates urate-crystal metabolic response; igf-1 dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Gout fibronectin: fibronectin in macrophages (already mapped) and synovial cells (already mapped) promotes joint ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Gout activin-a: activin-A from macrophages (already mapped) and synovial cells (already mapped) promotes joint fibrosis; activin-a excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Gout cgrp: CGRP from synovial cells (already mapped) and macrophages (already mapped) modulates joint pain signalling; cgrp excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Gout calcitonin: calcitonin from synovial cells (already mapped) and macrophages (already mapped) modulates joint calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — Gout substance-p: substance-P from synovial cells (already mapped) and macrophages (already mapped) modulates joint pain tone; substance-P excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — Gout insulin-receptor: insulin receptor on macrophages (already mapped) and synovial cells (already mapped) drives metabolic tone; insulin-receptor loss amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Androgen-Receptor](../../03-molecular/androgen-receptor/README.md)** — Gout androgen-receptor: androgen receptor on macrophages (already mapped) and synovial cells (already mapped) modulates gout androgen axis; androgen-receptor loss amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Gout norepinephrine: norepinephrine from macrophages (already mapped) and synovial cells (already mapped) modulates joint stress tone; norepinephrine excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Gout adrenomedullin: adrenomedullin from macrophages (already mapped) and synovial cells (already mapped) modulates joint vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Gout bdnf: BDNF from macrophages (already mapped) and synovial cells (already mapped) modulates joint neural tone; bdnf excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Gout fgfr: FGFR from macrophages (already mapped) and synovial cells (already mapped) modulates joint repair signalling; fgfr excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Gout epinephrine: epinephrine from macrophages (already mapped) and synovial cells (already mapped) modulates joint adrenergic tone; epinephrine excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Myostatin](../../03-molecular/myostatin/README.md)** — Gout myostatin: myostatin from macrophages (already mapped) and synovial cells (already mapped) modulates joint fibrotic axis; myostatin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Gout angiopoietin: angiopoietin from macrophages (already mapped) and synovial cells (already mapped) modulates joint vascular tone; angiopoietin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Gout ghrelin: ghrelin from macrophages (already mapped) and synovial cells (already mapped) modulates joint metabolic axis; ghrelin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade of gout.

[^dalbeth-2019-gout-primer]: Dalbeth N, Choi HK, Joosten LAB, et al. Gout. *Nat Rev Dis Primers.* 2019;5(1):69. [doi:10.1038/s41572-019-0115-y](https://doi.org/10.1038/s41572-019-0115-y) · [PubMed 31558729](https://pubmed.ncbi.nlm.nih.gov/31558729/)
[^martinon-2006-nlrp3-gout]: Martinon F, Pétrilli V, Mayor A, Tardivel A, Tschopp J. Gout-associated uric acid crystals activate the NALP3 inflammasome. *Nature.* 2006;440(7081):237-241. [doi:10.1038/nature04516](https://doi.org/10.1038/nature04516) · [PubMed 16407889](https://pubmed.ncbi.nlm.nih.gov/16407889/)
[^fitzgerald-2020-acr-gout]: FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. *Arthritis Care Res (Hoboken).* 2020;72(6):744-760. [doi:10.1002/acr.24180](https://doi.org/10.1002/acr.24180) · [PubMed 32391934](https://pubmed.ncbi.nlm.nih.gov/32391934/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
