---
schema: human-scale-entry/v1
id: atherosclerosis
name: Atherosclerosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic arterial intimal disease driven by LDL oxidation, macrophage foam cell formation, and smooth muscle migration; vulnerable plaque rupture causes MI and stroke. Statins, PCSK9 inhibitors, and anti-inflammatory therapies (colchicine) are evidence-based interventions."
aliases: ["arteriosclerosis", "coronary artery disease", "CAD", "ASCVD", "atherosclerotic cardiovascular disease"]
sources:
  - id: ross-1999-atherosclerosis-review
    type: peer-reviewed
    cite: "Ross R. Atherosclerosis — an inflammatory disease. N Engl J Med. 1999;340(2):115-126."
    doi: "10.1056/NEJM199901143400207"
    pmid: "9887164"
    url: "https://doi.org/10.1056/NEJM199901143400207"
  - id: ridker-2017-cantos
    type: peer-reviewed
    cite: "Ridker PM, Everett BM, Thuren T, et al. Antiinflammatory Therapy with Canakinumab for Atherosclerotic Disease. N Engl J Med. 2017;377(12):1119-1131."
    doi: "10.1056/NEJMoa1707914"
    pmid: "28845751"
    url: "https://doi.org/10.1056/NEJMoa1707914"
  - id: sabatine-2017-pcsk9
    type: peer-reviewed
    cite: "Sabatine MS, Giugliano RP, Keech AC, et al. Evolocumab and Clinical Outcomes in Patients with Cardiovascular Disease. N Engl J Med. 2017;376(18):1713-1722."
    doi: "10.1056/NEJMoa1615664"
    pmid: "28304224"
    url: "https://doi.org/10.1056/NEJMoa1615664"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: targets
    note: "Atherosclerosis is the primary cause of coronary artery disease, peripheral arterial disease, and ischemic stroke; plaque build-up reduces luminal diameter, limits perfusion during demand, and ruptures to trigger acute thrombosis — the mechanism of most MIs and ischemic strokes."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "LDL-C is the causal driver of atherosclerosis; apoB-containing lipoproteins (LDL, Lp(a), VLDL remnants) accumulate in the arterial intima → oxidation → foam cell formation; each 1 mmol/L LDL reduction → 22% CVD event reduction (Cholesterol Treatment Trialists 2010)."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "eNOS-derived NO maintains vascular homeostasis; LDL oxidation and hypertension reduce NO via oxidative stress → endothelial dysfunction, the earliest atherosclerotic lesion; statins, exercise, and ACE inhibitors partially restore eNOS activity and plaque stability."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are the defining plaque component; monocytes take up oxLDL via SR-A/CD36 → foam cells; M1-polarized macrophages produce MMP-9/12 → fibrous cap thinning and rupture; TREM2+ macrophages promote lipid export and plaque resolution."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "PCSK9 inhibitors (evolocumab, alirocumab) reduce LDL-C by 50-60% add-on to statins; FOURIER trial (evolocumab): 15% RRR in MACE at ~26 months; ODYSSEY OUTCOMES (alirocumab): 15% RRR with mortality reduction; PCSK9 inhibition is standard-of-care for high-risk atherosclerotic CVD."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2 from endothelium/macrophages → CCR2 on monocytes → subendothelial monocyte recruitment → foam cell formation → atherosclerotic plaque; CCL2/CCR2 knockout reduces plaque 40-60% in ApoE-/- mice; serum CCL2 correlates with MACE risk in MRFIT and EPIC-Norfolk cohorts."
  - target: 01-human/07-system/familial-hypercholesterolemia
    relation: connects-to
    note: "FH accelerates atherosclerosis; HeFH untreated: 20× higher CVD risk; coronary atherosclerosis, tendon xanthomas, and xanthelasma are hallmarks; cumulative LDL-C burden predicts events; early statin initiation reduces atherosclerotic events in HeFH."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "FN accumulates in the arterial intima early in atherosclerosis; EDA-FN activates TLR4 on SMCs and macrophages → NF-κB → inflammation; FN-integrin α5β1 promotes SMC migration from media to intima; plaque FN cross-links collagen → fibrous cap stability; plasma FN falls in acute MI."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: treated-by
    note: "Aspirin 75-100 mg/day is a cornerstone of secondary prevention in atherosclerotic CVD; irreversible platelet COX-1 acetylation blocks TXA₂ → prevents arterial thrombosis at ruptured plaques; ATC meta-analysis: 22% proportional reduction in serious vascular events."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Cholesterol (C₂₇H₄₆O) and fatty acid carbon accumulate in arterial macrophages forming foam cells; oxidised LDL carbon adducts trigger inflammatory NF-κB signalling; statins inhibit HMG-CoA reductase, reducing hepatic cholesterol carbon synthesis."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Atherosclerosis begins at the endothelial cell: disturbed flow, LDL, smoking and hyperglycemia injure it, so it loses nitric-oxide protection and expresses adhesion molecules that recruit monocytes and let LDL enter the intima—the initiating step of plaque."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Coronary atherosclerosis is the dominant cause of heart disease: plaque narrowing produces angina and ischemia, while rupture of a vulnerable plaque triggers thrombosis → myocardial infarction; LDL lowering, antiplatelets and revascularization aim to stabilize coronary plaque."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Atherosclerosis is a leading cause of ischemic stroke: carotid and intracranial plaques narrow vessels and, when they rupture, throw emboli or thrombose to occlude cerebral arteries → infarction; carotid imaging, statins, antiplatelets and endarterectomy target this mechanism."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes powerfully accelerates atherosclerosis: hyperglycemia, insulin resistance, and diabetic dyslipidemia injure the endothelium and inflame plaques, so cardiovascular disease is the top killer in diabetes—hence aggressive lipid and BP control."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Hypertension drives atherosclerosis through mechanical and inflammatory injury: high pressure damages the endothelium, especially at branch points, accelerating plaque formation and rupture—so BP control is among the best ways to prevent its heart attacks and strokes."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Vascular smooth muscle cells shape atherosclerotic plaques both ways: they migrate into the intima to form the fibrous cap that stabilizes a plaque, but also take up lipid to become foam cells—so their behavior decides whether a plaque stays stable or ruptures."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets turn a plaque into a heart attack: when an atherosclerotic cap ruptures, the exposed lipid core triggers platelet adhesion and aggregation forming the occlusive thrombus—so antiplatelet drugs like aspirin help prevent myocardial infarction and stroke."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 links inflammation to atherosclerosis: plaque macrophages release IL-6 that drives CRP and fuels lesion progression, and trials lowering inflammation (canakinumab, colchicine) cut cardiovascular events—showing atherosclerosis is inflammatory, not just lipid."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity accelerates atherosclerosis: excess visceral fat drives insulin resistance, dyslipidemia, hypertension and chronic inflammation that together damage arteries, so obesity is a central, modifiable hub feeding the major atherosclerotic risk factors."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium marks and stiffens atherosclerotic arteries: chronic plaque inflammation drives calcium deposition that hardens vessel walls, and a CT coronary-calcium score quantifies this buildup to gauge cardiovascular risk."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells make atherosclerosis an inflammatory disease: Th1 cells in the plaque secrete cytokines that activate macrophages and destabilize the fibrous cap, so immune activity—not just lipid—governs whether a plaque stays quiet or ruptures."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Chronic kidney disease accelerates atherosclerosis: uremia, phosphate retention and inflammation promote vascular calcification and plaque, so cardiovascular disease—not kidney failure—is the leading cause of death in CKD."
  - target: 01-human/03-molecular/apoe
    relation: connects-to
    note: "APOE shapes atherosclerosis risk: this lipid-carrier protein clears cholesterol-rich particles, and the common APOE4 variant raises LDL and cardiovascular (and Alzheimer's) risk, so APOE genotype is a built-in modifier of how fast plaque builds."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome fuels atherosclerosis: gut bacteria convert dietary choline and carnitine into TMAO, a metabolite that promotes plaque and clotting, so what microbes make from red meat and eggs feeds the arterial disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils inflame the atherosclerotic plaque: they release NETs and enzymes that recruit more inflammation and destabilize the fibrous cap, so beyond macrophages, neutrophil-driven inflammation helps turn a stable plaque into a rupture-prone one."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "An atherosclerotic plaque lives or dies by its collagen cap: smooth muscle lays down a collagen-rich fibrous cap that, when thick, keeps the plaque stable, but when thinned by inflammation it ruptures—triggering the clot of a heart attack or stroke."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Atherosclerosis is an immune disease involving cytotoxic T cells: CD8 T cells infiltrate plaques and can kill the cells that stabilize them, adding adaptive immunity to the macrophage-driven inflammation behind plaque progression."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Intraplaque hemorrhage accelerates atherosclerosis: leaky new vessels bleed red cells into the plaque, dumping cholesterol-rich membranes and iron that enlarge the lipid core and destabilize it—turning a quiet plaque into a dangerous one."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Atherosclerosis is dangerous because it cuts off oxygen: narrowed arteries throttle blood flow so tissue demand outstrips supply, causing the angina, claudication and—on plaque rupture—the infarction that kills oxygen-starved muscle."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Atherosclerosis turns deadly when thrombin fires: a ruptured plaque exposes tissue that triggers the clotting cascade, and thrombin builds the clot that abruptly blocks the artery—the final step to heart attack and stroke."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Atherosclerosis attacks the kidney's arteries: narrowing of the renal artery (renovascular disease) lowers kidney blood flow, driving resistant hypertension and progressive kidney damage, so the disease is both a cause and a victim of vascular aging."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Atherosclerosis lives or dies by its fibrous cap: smooth-muscle cells lay down collagen to wall off the fatty core, and when this fibrous scar thins and ruptures, the exposed core triggers the clot behind heart attacks."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Atherosclerosis chokes the brain's arteries: plaque in the carotid and cerebral vessels throws clots or narrows flow, causing ischemic strokes and contributing to vascular cognitive decline."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Atherosclerotic plaques summon VEGF to grow vessels: as a plaque thickens it turns hypoxic and releases VEGF, sprouting fragile microvessels that bleed into the plaque and destabilize it, raising rupture risk."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Atherosclerosis is scored by imaging: a CT coronary calcium scan in X-ray photons quantifies plaque burden to predict risk, and angiography maps the narrowings that threaten flow."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The plaque's foam cells come from the marrow: it supplies the monocytes that invade the artery wall, and age-related clonal mutations in marrow cells (clonal hematopoiesis) independently accelerate atherosclerosis."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver sets the stage for atherosclerosis: it makes and clears LDL cholesterol, so it is where statins act to lower the lipid that builds the plaque."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the plaque's anatomy: lipid-stuffed foam cells, needle-like cholesterol clefts, and a soft necrotic core capped by fibrous tissue — the unstable structure whose rupture triggers heart attacks and strokes."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper helps turn cholesterol toxic: as a redox-active metal it catalyzes the oxidation of LDL, and it is oxidized LDL that macrophages gorge on to become the foam cells at the heart of the plaque."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Atherosclerosis can starve the gut: when it narrows the mesenteric arteries, eating brings on the cramping 'intestinal angina,' and a sudden clot there can cause catastrophic bowel infarction."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Atherosclerosis of the neck and brain arteries threatens neurons: carotid plaque throws emboli that cause stroke and TIA, while diffuse small-vessel disease starves neurons into vascular cognitive impairment."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Erectile dysfunction is atherosclerosis's early warning: the small penile arteries clog before the larger coronaries, so new ED in a man is often the first sign of systemic disease and prompts cardiac assessment."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Narrowed leg arteries cramp the muscles: peripheral artery disease starves the calf and thigh muscles of blood, causing the claudication pain that comes on with walking and, when severe, threatens the limb."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Atherosclerosis is now treated as inflammation: the anti-IL-1β antibody canakinumab cut cardiovascular events in the CANTOS trial, proving the plaque's inflammatory drive, while oxidized-LDL autoantibodies mark the immune response within it."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Visceral fat fuels the plaque: enlarged adipocytes pour out inflammatory adipokines and free fatty acids that worsen dyslipidemia and insulin resistance, tying central obesity directly to accelerated atherosclerosis."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Diet is frontline prevention: soluble fiber lowers LDL by binding bile acids, and a high-fiber, Mediterranean pattern that cuts saturated fat measurably slows atherosclerosis alongside statins."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Fibrinogen is the clot that finishes the plaque: this acute-phase protein is both a marker of vascular inflammation and the substrate that, on a ruptured plaque, forms the occlusive thrombus of heart attack and stroke."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells are the plaque's brake: they dampen the inflammatory attack on the artery wall, so when their atheroprotective control fails, the lesion grows more inflamed and unstable."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Chronic inflammation anywhere ages the arteries: rheumatoid arthritis accelerates atherosclerosis through its systemic inflammatory load, giving patients excess heart attacks and the cardiovascular death that shortens their lives."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Cholesterol crystals ignite the plaque's inflammasome: ingested by lesion macrophages they activate NLRP3 to release IL-1β, the upstream step CANTOS validated by cutting events with IL-1β blockade — proof inflammation, not just lipid, drives atherosclerosis."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Skin inflammation reaches the arteries: psoriasis carries excess cardiovascular risk, its systemic Th17/IL-17 inflammation accelerating atherosclerosis, so plaque psoriasis is now treated as a vascular risk factor too."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Lupus ages arteries decades early: chronic immune-complex inflammation and steroid exposure drive premature, accelerated atherosclerosis, making cardiovascular disease a leading cause of late death in systemic lupus."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is the inflammatory switch in the artery wall: activated by oxidized LDL and disturbed flow in endothelium and macrophages, it drives the adhesion molecules and cytokines that recruit immune cells and build the plaque."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 shapes the plaque's macrophages: IL-6-driven STAT3 signaling tunes the inflammatory macrophage response within the lesion, contributing to the chronic inflammation that destabilizes atherosclerotic plaque."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Arterial and venous clots share a soil: although atherosclerosis is an arterial disease, it shares risk factors and systemic inflammation with venous thromboembolism, and the two cluster together more than chance."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Clogged coronaries weaken the pump: atherosclerosis of the coronary arteries causes myocardial infarction and chronic ischemia, the leading cause of the ischemic cardiomyopathy that drives heart failure."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Starved limbs cannot heal: atherosclerotic peripheral arterial disease cuts blood flow to the legs, producing ischemic ulcers that resist healing and, in critical limb ischemia, progress to gangrene and amputation."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Hardened brain vessels darken mood: cerebral small-vessel atherosclerosis underlies the 'vascular depression' of later life, a late-onset, often treatment-resistant depression tied to ischemic white-matter injury."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Diseased brain vessels erode the mind: cerebral atherosclerosis causes vascular dementia and lowers the threshold for Alzheimer's, the two often coexisting as the mixed dementia of later life."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Blocked leg arteries starve the skin: peripheral arterial disease from atherosclerosis deprives the limbs of blood, causing ischemic ulcers and gangrene that cannot heal without restored flow."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Small-vessel disease can mimic parkinsonism: cumulative atherosclerotic infarcts in the basal ganglia produce vascular parkinsonism, a gait-predominant syndrome overlapping with Parkinson's disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It starves the bowel of blood: atherosclerosis of the mesenteric arteries causes chronic intestinal angina with post-meal pain and weight loss, and acute occlusion brings catastrophic bowel infarction."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It throttles the kidney's blood supply: atherosclerotic renal artery stenosis causes renovascular hypertension and ischaemic nephropathy, and showers of cholesterol emboli can injure the kidneys."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Chronic limb ischaemia marks the skin: atherosclerotic peripheral arterial disease leaves the legs with hair loss, shiny atrophic cool skin and thickened nails, the trophic changes of poor perfusion."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is fundamentally an inflammatory disease: macrophage foam cells, the NLRP3 inflammasome and IL-1β drive plaque growth and rupture, now targeted by anti-inflammatory colchicine and canakinumab."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It hardens the arteries to the brain: carotid and intracranial atherosclerosis cause transient ischaemic attacks and contribute to vascular cognitive impairment beyond overt stroke."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is the vascular endpoint of metabolic disease: diabetes, dyslipidaemia and the metabolic syndrome accelerate plaque formation, tying atherosclerosis tightly to endocrine dysfunction."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: connects-to
    note: "The defining therapy: statins lower LDL and stabilise plaque, the cornerstone of preventing the heart attacks and strokes that atherosclerosis causes."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The artery wall has its own drainage: lymphatic vessels clear cholesterol from the arterial wall in reverse cholesterol transport, and impaired lymphatic function promotes plaque growth."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It shares its biggest cause with lung disease: smoking drives both atherosclerosis and COPD, and the hypoxia of chronic lung disease and sleep apnoea further accelerates arterial plaque."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "They protect the vessel wall: ACE inhibitors lower blood pressure and improve endothelial function, slowing atherosclerosis and reducing cardiovascular events beyond their pressure effect."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Infection may inflame the plaque: cytomegalovirus and other herpesviruses are found in atherosclerotic lesions and are proposed to add to the chronic inflammation that drives plaque growth."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "A fish-oil drug cuts events: high-dose icosapent ethyl (purified EPA) reduced cardiovascular events in high-risk patients, one diet-derived therapy with proven benefit in atherosclerosis."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Antibody and RNA drugs slash LDL: PCSK9-inhibitor antibodies (evolocumab) and the siRNA inclisiran drive LDL far below what statins achieve, while anti-inflammatory approaches target the residual inflammatory risk of atherosclerosis."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It is a disease of the artery wall: atherosclerosis builds within the intima — LDL retention, foam-cell-laden macrophages, a smooth-muscle fibrous cap over a lipid-necrotic core — that can rupture and thrombose the vessel."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It starves the heart muscle: coronary atherosclerosis is the cause of myocardial infarction, where plaque rupture and thrombosis occlude an artery and infarct the myocardium — the leading cause of death worldwide."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Urate and inflamed arteries: hyperuricaemia and gout are independently associated with atherosclerosis and cardiovascular events, sharing the NLRP3-inflammasome-driven inflammation that destabilises plaque."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Ischaemic nephropathy: atherosclerosis of the renal arteries and intrarenal vessels starves the glomerulus, causing renovascular hypertension and ischaemic chronic kidney disease."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Ischaemia and arrhythmia: coronary atherosclerosis starves the conduction system, and infarction scars it, causing the heart block and ventricular arrhythmias of ischaemic heart disease."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Accelerated arterial disease: HIV/AIDS speeds atherosclerosis through chronic immune activation, inflammation and antiretroviral metabolic effects, making cardiovascular disease a leading cause of death in treated HIV."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Inflammation injures arteries: chronic inflammatory diseases like inflammatory bowel disease accelerate atherosclerosis, the systemic inflammation damaging the arterial wall beyond traditional risk factors."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Infection that ruptures plaques: COVID-19's hyperinflammatory, prothrombotic state can rupture atherosclerotic plaques and trigger heart attacks and strokes, with lasting cardiovascular risk after recovery."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Fatty liver and arteries: NASH and atherosclerosis share insulin resistance, atherogenic dyslipidaemia and systemic inflammation, and NASH is an independent risk factor for cardiovascular disease."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Accelerated disease: type 1 diabetes dramatically accelerates atherosclerosis through chronic hyperglycaemia, glycation and endothelial injury, making cardiovascular disease its leading cause of death."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Endothelial vasoconstrictor: endothelin-1 from dysfunctional endothelium drives vasoconstriction, smooth-muscle proliferation and inflammation that promote atherosclerotic plaque growth."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammation hypothesis confirmed: IL-1β drives plaque inflammation, and the CANTOS trial showed that blocking it with canakinumab cuts cardiovascular events—proving inflammation as a causal, treatable driver of atherosclerosis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Endothelial activation: TNF-α upregulates adhesion molecules and CCL2 on the endothelium, recruiting the monocytes that become the foam cells of the atherosclerotic plaque."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Plaque hypoxia: the thickening, metabolically active plaque outgrows its oxygen supply, stabilising HIF-1α to drive the intraplaque angiogenesis and inflammation that destabilise it."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "OxLDL sensing: TLR4 on plaque macrophages recognises oxidised LDL and other danger signals, igniting the NF-κB inflammation that converts lipid uptake into the chronic immune disease of atherosclerosis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Myeloid alarmin: S100A8/A9 from activated plaque neutrophils and monocytes amplifies vascular inflammation and circulates as a biomarker predicting atherosclerotic cardiovascular events."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 plaque immunity: IFN-γ from plaque T cells activates macrophages and suppresses smooth-muscle collagen synthesis, thinning the fibrous cap and predisposing the plaque to rupture."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "AGE/oxLDL signalling: RAGE on endothelium and macrophages senses advanced glycation end-products and oxidised LDL, amplifying NF-κB-driven plaque inflammation and explaining the accelerated atherosclerosis of diabetes."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Necrotic-core formation: caspase-3-mediated apoptosis of plaque macrophages and smooth-muscle cells, when clearance fails, builds the lipid-rich necrotic core that makes an atherosclerotic plaque unstable and rupture-prone."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Rupture thrombosis: when an atherosclerotic plaque ruptures, exposed subendothelium and released von Willebrand factor mediate the platelet adhesion that nucleates the occlusive thrombus of myocardial infarction and stroke."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Plaque calcification: advanced atherosclerotic plaques calcify as smooth-muscle cells transdifferentiate toward an osteoblast-like phenotype, the calcium deposition measured by coronary-artery-calcium scoring to quantify plaque burden and refine cardiovascular risk."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "LDL oxidation: xanthine-oxidase-derived reactive oxygen species oxidise LDL trapped in the arterial wall, and it is this oxidised LDL — not native LDL — that macrophages devour to become the foam cells at the heart of the plaque."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Foam-cell marker: galectin-3 is highly expressed by the lipid-laden macrophages of the atherosclerotic plaque, promoting their inflammatory activation and serving as a circulating biomarker of plaque burden and cardiovascular risk."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Neointima formation: PDGF from platelets and plaque cells drives migration and proliferation of vascular smooth-muscle cells (already mapped) from media to intima, building the fibrous cap and stenotic neointima of atherosclerosis."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Cap stability: TGF-β regulates collagen synthesis and the stability of the atherosclerotic fibrous cap, opposing the inflammatory forces (IL-1β already mapped) that thin the cap toward rupture."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Plaque neovascularisation: angiopoietin-driven angiogenesis produces the fragile intraplaque neovessels that haemorrhage and destabilise advanced atherosclerotic plaques, precipitating acute events."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate plaque inflammation: TLR4 sensing of oxidised LDL signals through MyD88 to NF-κB (both already mapped), igniting the sterile innate inflammation that converts lipid deposition into progressive atherosclerotic plaque."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Vascular oxidant defence: NRF2 antioxidant signalling counters the oxidative modification of LDL and the vascular oxidative stress central to atherogenesis and endothelial injury."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Endothelial protection: the PI3K-AKT-eNOS axis maintains endothelial nitric-oxide production (NO already mapped), and its impairment promotes the endothelial dysfunction that initiates atherosclerosis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Oxidized-LDL and PDGF-driven ERK-MAPK signalling (PDGF mapped) promotes the smooth-muscle proliferation and migration that build the atherosclerotic plaque."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR regulation of macrophage autophagy and efferocytosis governs dead-cell clearance and the necrotic-core expansion of atherosclerotic plaques."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IFN-γ and IL-6 signalling through JAK-STAT (both mapped) drives the chronic vascular inflammation central to atherogenesis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cholesterol-crystal and mitochondrial DNA engagement of cGAS-STING amplifies the sterile inflammation of the atherosclerotic plaque."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) governs the smooth-muscle and fibrous-cap responses that determine plaque stability in atherosclerosis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ-STAT1 signalling drives the macrophage activation and antigen presentation that propagate the chronic immune response of atherosclerosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the endothelial and macrophage oxidative-stress and lipid-handling responses relevant to atherosclerotic plaque biology."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic CD8 and NK activity contributes to the plaque instability and necrotic-core formation of atherosclerosis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven vascular smooth-muscle-cell proliferation contributes to the intimal hyperplasia of the atherosclerotic plaque."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the macrophage inflammatory and foam-cell signaling within the atherosclerotic plaque."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the endothelial activation and macrophage survival of the atherosclerotic lesion."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, a regulator of vascular lipid metabolism and inflammation, is atheroprotective and its dysregulation promotes atherosclerosis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy (including macrophage lipophagy) modulates the foam-cell formation and plaque stability of atherosclerosis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the endothelial activation and vascular-smooth-muscle responses of atherosclerosis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte recruitment into the arterial wall drives the inflammation of atherosclerosis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation (including clonal hematopoiesis) participates in the vascular inflammation and atherogenesis of atherosclerosis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the smooth-muscle-cell and leukocyte dynamics of atherosclerotic plaques."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the vascular inflammation and plaque immunobiology of atherosclerosis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the vascular inflammation and plaque instability of atherosclerosis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory and lipid-driven vascular injury of atherosclerosis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the macrophage and vascular-cell gene programs of atherosclerosis."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Adaptive plaque immunity: atherosclerosis has an adaptive immune component, with MHC class II presentation of oxidised-LDL and ApoB peptides to T cells shaping the inflammation of the plaque, a target of experimental atherosclerosis vaccines."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Plaque rupture: rupture of an atherosclerotic plaque triggers coronary thrombosis and myocardial infarction, and troponin release marks the resulting myocardial injury, the acute clinical endpoint of the disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and inflammation: obesity accelerates atherosclerosis, and the adipokine leptin promotes endothelial dysfunction, macrophage foam-cell formation and vascular inflammation, linking metabolic syndrome to plaque progression."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Atheroprotective cytokine: the anti-inflammatory cytokine IL-10 restrains plaque inflammation and stabilises lesions, so the balance between it and the pro-inflammatory IL-1 and TNF (already mapped) shapes plaque progression and rupture risk."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex protection: estrogen improves endothelial function and lipid profiles, and its premenopausal presence delays atherosclerosis in women, contributing to the sex and age differences in cardiovascular risk."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Plaque destabilisation: mast cells in the atherosclerotic plaque release proteases and histamine that degrade the fibrous cap (collagen already mapped) and promote intraplaque haemorrhage, contributing to the rupture behind acute events."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane and inflammation: the prostaglandin balance shifts toward the prothrombotic thromboxane on the atherosclerotic plaque, part of why low-dose aspirin is used, while inflammatory prostaglandins (IL-6 and IL-1 already mapped) drive the lesion."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Protective adipokine: adiponectin is anti-inflammatory and anti-atherogenic, and its fall in obesity and the metabolic syndrome (leptin already mapped) removes a brake on the vascular inflammation that drives atherosclerosis."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance: insulin resistance and hyperinsulinaemia promote endothelial dysfunction (nitric oxide already mapped) and the atherogenic dyslipidaemia (cholesterol already mapped), accelerating the atherosclerosis of the metabolic syndrome and diabetes."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Macrophage polarisation: IL-4 polarises the plaque macrophages (already mapped) toward an M2 phenotype (IL-10 already mapped), and the balance between the inflammatory and resolving macrophages shapes the stability of the atherosclerotic lesion."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Pro-atherogenic adipokine: resistin, with leptin (already mapped) and the fall in adiponectin (already mapped), is a pro-inflammatory adipokine that promotes the endothelial dysfunction and vascular inflammation of atherosclerosis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Plaque iron handling: the hepcidin-regulated iron handling of the plaque macrophages (already mapped) influences the oxidative stress (xanthine oxidase already mapped) of the lesion, the basis of the iron hypothesis of atherosclerosis."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "LDL oxidation: iron catalyses the oxidation of the LDL (cholesterol already mapped) that generates the oxidised LDL taken up by the foam-cell macrophages (already mapped), the iron hypothesis (hepcidin already mapped) of atherogenesis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 plaque arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the plaque inflammation, a potentially plaque-stabilising phenotype in atherosclerosis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and endothelial protection: zinc is an antioxidant and endothelial-protective trace metal, and its deficiency promotes the oxidative stress and endothelial dysfunction (nitric oxide already mapped) of atherosclerosis."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Coronary disease: the coronary atherosclerosis causes the angina and the myocardial infarction (troponin already mapped) of the heart, the leading cause of death."
  - target: 01-human/07-system/familial-hypercholesterolemia
    relation: connects-to
    note: "Monogenic driver: familial hypercholesterolaemia (LDL and PCSK9 already mapped) causes the premature, severe atherosclerosis, the extreme of the cholesterol-driven disease."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Atherothrombosis: the platelets aggregate on the ruptured plaque (VWF and thrombin already mapped) to form the occlusive thrombus, the atherothrombotic MI and stroke."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 plaque polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the plaque inflammation that destabilises the atherosclerotic lesion."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate plaque interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the cholesterol-crystal and cellular stress, amplifies the macrophage (already mapped) inflammation of the atheroma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension modulating the Th1-driven atherosclerotic inflammation."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of the atherosclerotic plaque."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Mast-cell arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), arms the plaque mast cells whose degranulation destabilises the atheroma."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Plaque antigen presentation: the dendritic cells present the oxidised-LDL and other plaque antigens (MHC already mapped), shaping the adaptive T-cell response of the atheroma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the monocyte and mast-cell (already mapped) recruitment into the atherosclerotic plaque."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) on the oxidised LDL contribute to the plaque inflammation and the membrane-attack-complex injury of atherosclerosis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) on the oxidised LDL, and its variants are linked to the risk of atherosclerosis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the oxidised LDL and C-reactive protein in the atherosclerotic plaque."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Plaque matricellular: osteopontin, produced by the foam-cell macrophages (already mapped) and smooth-muscle cells (already mapped), is a matricellular mediator of the plaque inflammation and the vascular calcification of atherosclerosis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Plaque iron: transferrin, the iron carrier, reflects the disordered iron handling and the intraplaque-haemorrhage iron that aggravates the oxidative injury of the atherosclerotic plaque."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-plaque axis: TSLP, from activated endothelium (already mapped) and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/eosinophil plaque inflammation and the vulnerable-plaque formation of atherosclerosis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-vascular axis: bradykinin, via B2 receptors on arterial endothelium (already mapped), releases NO and prostacyclin and modulates the vasotension and endothelial dysfunction of the atherosclerotic risk dimension of atherosclerosis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Vascular erythropoietin: erythropoietin, via the EPOR on endothelial cells (already mapped) and smooth-muscle cells (already mapped), exerts cardioprotective and anti-inflammatory effects that modulate the vascular damage of atherosclerosis."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell plaque: histamine, from mast cells in the atherosclerotic plaque (already mapped), degrades the fibrous cap (collagen already mapped) and amplifies the intraplaque inflammation and vulnerable-plaque formation of atherosclerosis."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Antioxidant-plaque axis: melatonin, via MT1/MT2 receptors and its radical-scavenging activity, reduces the oxidised-LDL (LDL already mapped) load and the endothelial dysfunction that drive the progression of atherosclerosis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone vascular axis: testosterone, via androgen receptors on endothelium (already mapped) and smooth-muscle cells (already mapped), modulates the lipid profile (LDL and HDL already mapped) and vascular tone of atherosclerosis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Atherosclerosis serotonin: serotonin, via 5-HT receptors on platelets (already mapped) and smooth-muscle cells (already mapped), amplifies vasoconstriction; serotonin worsens the nitric-oxide (already mapped) and NF-κB (already mapped) atherogenic cascade of atherosclerosis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Atherosclerosis prolactin: prolactin, via PRLR on endothelium (already mapped) and macrophages (already mapped), promotes foam-cell formation; hyperprolactinaemia amplifies the NF-κB (already mapped) and NLRP3 (already mapped) atherogenic inflammatory cascade of atherosclerosis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Atherosclerosis oxytocin: oxytocin, via OXTR on endothelium (already mapped) and macrophages (already mapped), attenuates atherogenic inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and NLRP3 (already mapped) inflammatory plaque cascade of atherosclerosis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Atherosclerosis vasopressin: vasopressin, via V1aR on smooth-muscle cells (already mapped) and endothelium (already mapped), promotes vasoconstriction; vasopressin dysregulation amplifies the NF-κB (already mapped) and NLRP3 (already mapped) plaque cascade of atherosclerosis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Atherosclerosis selenium: selenium, as GPx in endothelial cells (already mapped) and macrophages (already mapped), scavenges atherogenic ROS; selenium deficiency amplifies the NF-κB (already mapped) and NLRP3 (already mapped) inflammatory plaque cascade of atherosclerosis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Atherosclerosis iodine: iodine-dependent thyroid hormones modulate cholesterol (already mapped) homeostasis and endothelial (already mapped) function; iodine deficiency amplifies the NF-κB (already mapped) and NLRP3 (already mapped) atherogenic plaque cascade of atherosclerosis."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Atherosclerosis sodium: excess dietary sodium drives endothelial-cell (already mapped) inflammation; sodium amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) atherogenic plaque and thrombin (already mapped) cascade."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Atherosclerosis potassium: potassium regulates endothelial-cell (already mapped) membrane function; potassium dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) atherogenic cascade in atherosclerosis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Atherosclerosis magnesium: magnesium stabilises endothelial-cell (already mapped) function and attenuates platelet (already mapped) aggregation; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and fibrinogen (already mapped) atherogenic cascade."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "chloride channels on macrophages (already mapped) and smooth-muscle cells (already mapped) regulate intracellular pH; chloride dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) atherogenic plaque cascade in atherosclerosis."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "H2S from sulfur-amino acids in macrophages (already mapped) and smooth-muscle cells (already mapped) scavenges ROS; sulfur deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) atherogenic plaque cascade in atherosclerosis."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "nitric oxide from iNOS in macrophages (already mapped) and smooth-muscle cells (already mapped) modulates vascular tone; nitrogen excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) atherogenic plaque cascade in atherosclerosis."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Athero hydrogen: hydrogen via ROS balance in macrophages (already mapped) and endothelial cells (already mapped) modulates plaque oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) cascade in atherosclerosis."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Athero phosphorus: phosphorus-driven ATP in smooth-muscle cells (already mapped) and endothelial cells (already mapped) sustains vascular homeostasis; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) in atherosclerosis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Athero pd-1: PD-1 on t-cytotoxic cells (already mapped) and regulatory T cells (already mapped) restrains plaque inflammation; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) atheroinflammatory plaque destabilisation."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Athero glp-1: GLP-1 on macrophages (already mapped) and endothelial cells (already mapped) attenuates vascular skewing; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) atheroinflammatory plaque cascade in atherosclerosis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Athero angiotensin-ii: angiotensin II on smooth-muscle cells (already mapped) and endothelial cells (already mapped) promotes remodelling; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) athero cascade in atherosclerosis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Athero wnt-beta-catenin: WNT/β-catenin on smooth-muscle cells (already mapped) and endothelial cells (already mapped) regulates homeostasis; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) in atherosclerosis."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Athero rankl: RANKL in macrophages (already mapped) and smooth-muscle cells (already mapped) modulates plaque bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Athero il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates plaque immune surveillance; il-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Athero notch: NOTCH on smooth-muscle cells (already mapped) and endothelial cells (already mapped) regulates vascular cell fate; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Athero igf-1: IGF-1 from macrophages (already mapped) and smooth-muscle cells (already mapped) promotes plaque growth; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Athero activin-a: activin-A from macrophages (already mapped) and smooth-muscle cells (already mapped) regulates plaque fibro-inflammatory balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Athero cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade."
---

# Atherosclerosis

## Overview

**Atherosclerosis** is a **chronic inflammatory disease of the arterial intima** characterized by progressive accumulation of lipids, immune cells, smooth muscle cells, and extracellular matrix components forming **atherosclerotic plaques (atheromas)** within the arterial wall. First recognized as an inflammatory disease by Russell Ross in 1999 [^ross-1999-atherosclerosis-review], atherosclerosis is the underlying pathology of **coronary artery disease (CAD), ischemic stroke, and peripheral arterial disease (PAD)** — collectively **atherosclerotic cardiovascular disease (ASCVD)** — the **leading cause of death globally** (~18 million deaths/year, WHO 2019).

The process begins in childhood with **fatty streaks** and progresses silently over decades. Clinically manifest disease (ACS, stable angina, TIA, stroke) typically appears in the 4th-7th decade of life. **Acute plaque rupture or erosion** triggers thrombus formation → abrupt vessel occlusion → myocardial infarction or ischemic stroke.

**Risk factors (established):**
- **Modifiable:** Hyperlipidemia (LDL-C, Lp(a)), hypertension, diabetes mellitus (T2DM > T1DM), smoking, obesity, physical inactivity, chronic inflammation (RA, psoriasis, SLE), air pollution, psychosocial stress
- **Non-modifiable:** Age (men >45, women >55), male sex, family history of premature ASCVD (<55 men, <65 women), genetic hypercholesterolemia (FH)
- **Novel risk enhancers:** hs-CRP ≥2.0 mg/L, coronary artery calcium (CAC) score ≥100, Lp(a) ≥50 mg/dL (≥125 nmol/L), ABI <0.9 (peripheral arterial disease), chronic kidney disease

**Atherosclerosis pathological stages:**
1. **Endothelial dysfunction:** LDL entry, oxidative stress, reduced NO → earliest event; no structural change; reversible
2. **Fatty streak:** Foam cells (macrophage-derived); first visible lesion; present in most adults by age 20; can regress
3. **Plaque (atheroma):** Necrotic core (lipid, dead foam cells, cholesterol crystals), fibrous cap (smooth muscle, collagen), inflammatory infiltrate; decades of progression
4. **Vulnerable (unstable) plaque:** Thin fibrous cap, large necrotic core, rich macrophage infiltrate → prone to rupture → ACS
5. **Plaque rupture/erosion → thrombus:** ACS, MI, ischemic stroke

## Structure

### Plaque anatomy [^ross-1999-atherosclerosis-review]

**Intimal layers (site of atherosclerosis):**
- **Endothelium:** Normally anti-atherogenic (NO production, LDL barrier, PAI-1 low); dysfunction = first step; risk factors → endothelial oxidative stress → ICAM-1, VCAM-1, E-selectin upregulation → monocyte adhesion and transmigration
- **Subendothelial space (intima):** LDL retention via proteoglycans (biglycan, decorin) → oxidative modification (oxLDL, minimally modified LDL) → pattern recognition by SR-A, CD36 on macrophages
- **Internal elastic lamina:** SMC migration from media to intima depends on MMP-mediated IEL remodeling

**Plaque components:**
- **Necrotic core:** Accumulated lipid (free cholesterol, cholesterol esters), dead foam cell remnants, cholesterol crystals (NLRP3 inflammasome activation), calcium deposits; correlates with rupture risk
- **Fibrous cap:** Dense collagen (types I and III) produced by intimal smooth muscle cells; VSMC apoptosis (from ROS, macrophage cytotoxicity) → cap thinning; cap thickness <65 μm defines thin-cap fibroatheroma (TCFA) — the vulnerable plaque phenotype
- **Shoulder region:** Junction of fibrous cap and plaque body; highest inflammatory cell density; site of cap rupture
- **Macrophage infiltrate (foam cells):** Accumulated oxLDL via SR-A/CD36 → lipid-laden foam cells; produce MMP-2/9/12 → fibrous cap degradation; produce TNF-alpha, IL-1beta, IL-6 → local and systemic inflammation
- **Neovascularization:** Intraplaque angiogenesis (VEGF-driven) → fragile intraplaque vessels → intraplaque hemorrhage → rapid plaque expansion

### Lipoprotein pathophysiology

**LDL (low-density lipoprotein):**
- ApoB-100 particle carrying cholesterol; enters intima by transcytosis (endothelial LDLR-independent) → trapped by proteoglycans → oxidized by 12-LOX, 15-LOX, MPO → oxLDL → SR-A/CD36-mediated uptake → foam cells (LDLR-pathway is cholesterol-regulated; scavenger receptors are not → unrestricted foam cell formation)
- **PCSK9 (proprotein convertase subtilisin/kexin type 9):** Binds LDL receptor on hepatocytes → lysosomal LDLR degradation → less hepatic LDL uptake → elevated plasma LDL; gain-of-function PCSK9 mutations → severe hypercholesterolemia; loss-of-function PCSK9 mutations (rare, West Africans) → very low LDL → near-zero lifetime ASCVD risk
- **Lp(a) (lipoprotein a):** LDL-like particle with additional apo(a) protein linked via disulfide bond to apoB; pro-atherogenic (intimal accumulation) and pro-thrombotic (plasminogen homology → antifibrinolytic); genetic (KRINGLE domain size determines levels); elevated in ~20% of population; pelacarsen (antisense oligonucleotide, Phase 3) and olpasiran (siRNA) reduce Lp(a) >90%

## Function

### Inflammatory mechanism of atherosclerosis

**Inflammatory cascade:**

1. **Endothelial activation:** Risk factors → ROS → NFkB → VCAM-1, ICAM-1 → monocyte (CCR2+) binding via MCP-1 (CCL2) → transmigration into intima → differentiation to macrophages
2. **Foam cell formation:** Macrophages engulf oxLDL → lipid overload → foam cell; foam cells release MMP-9/12 → fibrous cap thinning; secrete IL-1beta, TNF-alpha → amplify local inflammation
3. **Adaptive immune response:** Oxidized LDL is immunogenic → CD4+ Th1 cells produce IFN-gamma → macrophage activation; Th17 cells → plaque progression; Tregs → atheroprotective (suppress Th1/Th17 responses)
4. **NLRP3 inflammasome activation:** Cholesterol crystals → NLRP3 → IL-1beta release → systemic and local pro-atherogenic inflammation (basis for IL-1beta blockade therapy)
5. **SMC migration:** Macrophage-derived PDGF → SMC migration from media to intima → fibrous cap formation (protective initially); VSMC apoptosis → cap thinning → vulnerability
6. **Calcification:** Dead foam cells → calcium phosphate deposits; coronary artery calcium (CAC) score by CT quantifies burden

### Vulnerable plaque and acute coronary syndromes

**Plaque vulnerability (TCFA criteria):**
- Cap thickness <65 μm (ruptured plaques typically <23 μm)
- Large necrotic core >40% plaque volume
- Dense macrophage infiltrate in shoulder region
- Intraplaque neovascularization (hemorrhage risk)

**Rupture triggers:**
- Physical exertion, circadian catecholamine surge (morning peak of MIs)
- Systemic inflammation (CRP spike, acute infection)
- MMP-mediated cap degradation (macrophage-derived MMP-9, -12)

**Plaque erosion (~30% of ACS):** Endothelial denudation without plaque rupture → thrombus on intact fibrous cap; more common in younger women, smokers, hypertriglyceridemia; treated with aspirin ± P2Y12 inhibition + statin (less benefit from PCI in some cases)

## Pathology

### Diagnosis

**Functional (ischemia detection):**
- Exercise stress test (ECG ± imaging): Detect flow-limiting stenosis (>70% luminal narrowing)
- Stress echo, nuclear perfusion (SPECT, PET), cardiac MRI: Detect perfusion defects and wall motion abnormalities
- Coronary CT angiography (CCTA): Non-invasive coronary anatomy; detects stenosis and plaque burden; FFRCT (fractional flow reserve by CT) assesses physiological significance

**Anatomical (plaque characterization):**
- **Coronary artery calcium (CAC) score (non-contrast CT):** Most powerful predictor for event risk beyond Framingham score; CAC=0 → very low 10-year risk (statin downgrade candidate); CAC ≥100 → high risk (statin initiation regardless of clinical risk)
- **Intravascular ultrasound (IVUS):** Plaque burden, volume, and echogenicity in cath lab
- **OCT (optical coherence tomography):** High-resolution intravascular; identifies TCFA, fibrous cap thickness, and erosion vs. rupture

### Treatment [^ridker-2017-cantos] [^sabatine-2017-pcsk9]

**Lipid-lowering — primary and secondary prevention:**

*Statins (HMG-CoA reductase inhibitors):*
- Inhibit cholesterol synthesis → hepatic LDLR upregulation → LDL clearance; reduces LDL 30-55% (dose-dependent); high-intensity: atorvastatin 40-80 mg, rosuvastatin 20-40 mg
- **PROVE-IT, TNT, JUPITER, FOURIER (CTT meta-analysis):** Each 1 mmol/L LDL reduction → 22% RRR in major ASCVD events; NNT ~5 for high-risk secondary prevention over 5 years
- **Pleiotropic effects:** Reduce CRP, improve endothelial function, stabilize plaque (↑ fibrous cap thickness via SMC stimulation and MMP suppression); independent of LDL lowering
- **Safety:** Myopathy (1-3%, usually mild); rhabdomyolysis (<0.01%); monitor CK if symptomatic; DM risk increased ~10-12% with high-dose statins (NNT 200 for diabetes vs. NNT 5 for CV event prevention — net benefit)

*PCSK9 inhibitors:*
- **Evolocumab (Repatha, anti-PCSK9 mAb):** SC biweekly or monthly; reduces LDL 60% added to statin; FOURIER trial: evolocumab vs. placebo in statin-treated ASCVD → 15% RRR in composite MACE (MI, stroke, CV death) over 2.2 years; LDL to ~30 mg/dL achievable [^sabatine-2017-pcsk9]
- **Alirocumab (Praluent):** Similar mechanism; ODYSSEY Outcomes: 15% RRR in post-ACS patients; reduces Lp(a) ~25-30%
- **Inclisiran (LEQVIO, anti-PCSK9 siRNA):** SC injection twice/year; reduces LDL ~50% vs. placebo; ORION-10/11 trials; approved for ASCVD and FH; CVOT ongoing (ORION-4)

*Other lipid agents:*
- **Ezetimibe:** Inhibits NPC1L1 → reduced cholesterol absorption; LDL -20%; IMPROVE-IT: ezetimibe+simvastatin vs. simvastatin alone → 6.4% RRR in MACE post-ACS (modest but additive)
- **Bempedoic acid (Nexletol):** ACL inhibitor → reduces hepatic cholesterol synthesis upstream of HMG-CoA reductase; doesn't cause myopathy (not expressed in skeletal muscle); CLEAR Outcomes: 13% RRR in primary endpoint vs placebo; add-on to statins or statin-intolerant patients

**Anti-inflammatory — targeting residual inflammatory risk:**
- **Colchicine (LoDoCo2, COLCOT):** Anti-inflammatory (inhibits tubulin polymerization → inflammasome and neutrophil activation reduction); 0.5 mg daily; 31% RRR in MACE in post-ACS (COLCOT); 23% RRR in stable CAD (LoDoCo2); FDA approved for ASCVD risk reduction
- **Canakinumab (anti-IL-1beta mAb):** CANTOS trial: 150 mg SC quarterly; 15% RRR in MACE in post-MI patients with elevated hs-CRP (≥2 mg/L); confirmed inflammatory hypothesis of atherosclerosis [^ridker-2017-cantos]; not approved for CV indication due to infection mortality risk; paved way for colchicine

**Antiplatelet and antithrombotic:**
- **Aspirin (75-100 mg):** Irreversibly inhibits COX-1 → TXA2 → platelet activation; secondary prevention (established ASCVD): clear benefit; primary prevention: benefit-risk unfavorable in low-to-moderate risk (ARRIVE, ASPREE, ASCEND) — bleeding offsets CV benefit
- **P2Y12 inhibitors:** Clopidogrel, ticagrelor, prasugrel → ADP receptor blockade → antiplatelet; dual antiplatelet therapy (DAPT) post-ACS or PCI for 1-12 months
- **Rivaroxaban 2.5 mg BID + aspirin (COMPASS):** For PAD and CAD without recent ACS; 24% RRR in MACE vs. aspirin alone; FDA approved for ASCVD

## Connections

- `targets` → **[Cardiovascular System](../cardiovascular-system/README.md)** — atherosclerosis is the primary driver of coronary artery disease, ischemic stroke, and peripheral arterial disease; plaque rupture triggers acute thrombosis causing MI and stroke; statins and PCSK9 inhibitors reduce LDL and MACE by 15-50% depending on baseline risk.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — LDL-C is the causal driver of atherosclerosis; apoB-containing lipoproteins accumulate in the arterial intima, undergo oxidation, and are engulfed by macrophages → foam cell formation; each 1 mmol/L LDL reduction yields ~22% relative MACE reduction.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — eNOS-derived NO maintains vascular homeostasis; risk factors reduce NO bioavailability via oxidative stress → endothelial dysfunction, the earliest atherosclerotic lesion; statins, exercise, and ACE inhibitors partially restore eNOS activity and plaque stability.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — macrophages are the defining cellular component of atheromas; monocyte-derived macrophages ingest oxLDL via scavenger receptors → foam cells; M1-polarized macrophages produce MMP-9/12 → cap thinning and plaque rupture; anti-inflammatory therapies (colchicine, canakinumab) target macrophage-driven inflammation.
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — PCSK9 inhibitors (evolocumab, alirocumab) reduce LDL-C by 50-60% add-on to statins; FOURIER trial (evolocumab): 15% RRR in MACE at ~26 months; ODYSSEY OUTCOMES (alirocumab): 15% RRR with mortality reduction; PCSK9 inhibition is standard-of-care for high-risk atherosclerotic CVD.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 from endothelium/macrophages → CCR2 on monocytes → subendothelial monocyte recruitment → foam cell formation → atherosclerotic plaque; CCL2/CCR2 knockout reduces plaque 40-60% in ApoE-/- mice; serum CCL2 correlates with MACE risk in MRFIT and EPIC-Norfolk cohorts.
- `connects-to` → **[Familial Hypercholesterolemia](../familial-hypercholesterolemia/README.md)** — FH accelerates atherosclerosis; HeFH untreated: 20× higher CVD risk; coronary atherosclerosis, tendon xanthomas, and xanthelasma are hallmarks; cumulative LDL-C burden predicts events; early statin initiation reduces atherosclerotic events in HeFH.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — FN accumulates in the arterial intima early in atherosclerosis; EDA-FN activates TLR4 on SMCs and macrophages → NF-κB → inflammation; FN-integrin α5β1 promotes SMC migration from media to intima; plaque FN cross-links collagen → fibrous cap stability; plasma FN falls in acute MI.
- `treated-by` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — aspirin 75-100 mg/day is a cornerstone of secondary prevention in atherosclerotic CVD; irreversible platelet COX-1 acetylation blocks TXA₂ → prevents plaque-rupture-triggered arterial thrombosis; ATC meta-analysis: 22% proportional reduction in serious vascular events.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Cholesterol (C₂₇H₄₆O) and fatty acid carbon accumulate in arterial macrophages forming foam cells; oxidised LDL carbon adducts trigger inflammatory NF-κB signalling; statins inhibit HMG-CoA reductase, reducing hepatic cholesterol carbon synthesis.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Atherosclerosis begins at the endothelial cell: disturbed flow, LDL, smoking and hyperglycemia injure it, so it loses nitric-oxide protection and expresses adhesion molecules that recruit monocytes and let LDL enter the intima—the initiating step of plaque.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Coronary atherosclerosis is the dominant cause of heart disease: plaque narrowing produces angina and ischemia, while rupture of a vulnerable plaque triggers thrombosis → myocardial infarction; LDL lowering, antiplatelets and revascularization aim to stabilize coronary plaque.
- `connects-to` → **[Stroke](../stroke/README.md)** — Atherosclerosis is a leading cause of ischemic stroke: carotid and intracranial plaques narrow vessels and, when they rupture, throw emboli or thrombose to occlude cerebral arteries → infarction; carotid imaging, statins, antiplatelets and endarterectomy target this mechanism.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes powerfully accelerates atherosclerosis: hyperglycemia, insulin resistance, and diabetic dyslipidemia injure the endothelium and inflame plaques, so cardiovascular disease is the top killer in diabetes—hence aggressive lipid and BP control.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Hypertension drives atherosclerosis through mechanical and inflammatory injury: high pressure damages the endothelium, especially at branch points, accelerating plaque formation and rupture—so BP control is among the best ways to prevent its heart attacks and strokes.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Vascular smooth muscle cells shape atherosclerotic plaques both ways: they migrate into the intima to form the fibrous cap that stabilizes a plaque, but also take up lipid to become foam cells—so their behavior decides whether a plaque stays stable or ruptures.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets turn a plaque into a heart attack: when an atherosclerotic cap ruptures, the exposed lipid core triggers platelet adhesion and aggregation forming the occlusive thrombus—so antiplatelet drugs like aspirin help prevent myocardial infarction and stroke.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 links inflammation to atherosclerosis: plaque macrophages release IL-6 that drives CRP and fuels lesion progression, and trials lowering inflammation (canakinumab, colchicine) cut cardiovascular events—showing atherosclerosis is inflammatory, not just lipid.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity accelerates atherosclerosis: excess visceral fat drives insulin resistance, dyslipidemia, hypertension and chronic inflammation that together damage arteries, so obesity is a central, modifiable hub feeding the major atherosclerotic risk factors.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium marks and stiffens atherosclerotic arteries: chronic plaque inflammation drives calcium deposition that hardens vessel walls, and a CT coronary-calcium score quantifies this buildup to gauge cardiovascular risk.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells make atherosclerosis an inflammatory disease: Th1 cells in the plaque secrete cytokines that activate macrophages and destabilize the fibrous cap, so immune activity—not just lipid—governs whether a plaque stays quiet or ruptures.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Chronic kidney disease accelerates atherosclerosis: uremia, phosphate retention and inflammation promote vascular calcification and plaque, so cardiovascular disease—not kidney failure—is the leading cause of death in CKD.
- `connects-to` → **[APOE](../../03-molecular/apoe/README.md)** — APOE shapes atherosclerosis risk: this lipid-carrier protein clears cholesterol-rich particles, and the common APOE4 variant raises LDL and cardiovascular (and Alzheimer's) risk, so APOE genotype is a built-in modifier of how fast plaque builds.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome fuels atherosclerosis: gut bacteria convert dietary choline and carnitine into TMAO, a metabolite that promotes plaque and clotting, so what microbes make from red meat and eggs feeds the arterial disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils inflame the atherosclerotic plaque: they release NETs and enzymes that recruit more inflammation and destabilize the fibrous cap, so beyond macrophages, neutrophil-driven inflammation helps turn a stable plaque into a rupture-prone one.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — An atherosclerotic plaque lives or dies by its collagen cap: smooth muscle lays down a collagen-rich fibrous cap that, when thick, keeps the plaque stable, but when thinned by inflammation it ruptures—triggering the clot of a heart attack or stroke.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Atherosclerosis is an immune disease involving cytotoxic T cells: CD8 T cells infiltrate plaques and can kill the cells that stabilize them, adding adaptive immunity to the macrophage-driven inflammation behind plaque progression.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Intraplaque hemorrhage accelerates atherosclerosis: leaky new vessels bleed red cells into the plaque, dumping cholesterol-rich membranes and iron that enlarge the lipid core and destabilize it—turning a quiet plaque into a dangerous one.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Atherosclerosis is dangerous because it cuts off oxygen: narrowed arteries throttle blood flow so tissue demand outstrips supply, causing the angina, claudication and—on plaque rupture—the infarction that kills oxygen-starved muscle.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Atherosclerosis turns deadly when thrombin fires: a ruptured plaque exposes tissue that triggers the clotting cascade, and thrombin builds the clot that abruptly blocks the artery—the final step to heart attack and stroke.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Atherosclerosis attacks the kidney's arteries: narrowing of the renal artery (renovascular disease) lowers kidney blood flow, driving resistant hypertension and progressive kidney damage, so the disease is both a cause and a victim of vascular aging.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Atherosclerosis lives or dies by its fibrous cap: smooth-muscle cells lay down collagen to wall off the fatty core, and when this fibrous scar thins and ruptures, the exposed core triggers the clot behind heart attacks.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Atherosclerosis chokes the brain's arteries: plaque in the carotid and cerebral vessels throws clots or narrows flow, causing ischemic strokes and contributing to vascular cognitive decline.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Atherosclerotic plaques summon VEGF to grow vessels: as a plaque thickens it turns hypoxic and releases VEGF, sprouting fragile microvessels that bleed into the plaque and destabilize it, raising rupture risk.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Atherosclerosis is scored by imaging: a CT coronary calcium scan in X-ray photons quantifies plaque burden to predict risk, and angiography maps the narrowings that threaten flow.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — The plaque's foam cells come from the marrow: it supplies the monocytes that invade the artery wall, and age-related clonal mutations in marrow cells (clonal hematopoiesis) independently accelerate atherosclerosis.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver sets the stage for atherosclerosis: it makes and clears LDL cholesterol, so it is where statins act to lower the lipid that builds the plaque.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the plaque's anatomy: lipid-stuffed foam cells, needle-like cholesterol clefts, and a soft necrotic core capped by fibrous tissue — the unstable structure whose rupture triggers heart attacks and strokes.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper helps turn cholesterol toxic: as a redox-active metal it catalyzes the oxidation of LDL, and it is oxidized LDL that macrophages gorge on to become the foam cells at the heart of the plaque.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Atherosclerosis can starve the gut: when it narrows the mesenteric arteries, eating brings on the cramping 'intestinal angina,' and a sudden clot there can cause catastrophic bowel infarction.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Atherosclerosis of the neck and brain arteries threatens neurons: carotid plaque throws emboli that cause stroke and TIA, while diffuse small-vessel disease starves neurons into vascular cognitive impairment.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Erectile dysfunction is atherosclerosis's early warning: the small penile arteries clog before the larger coronaries, so new ED in a man is often the first sign of systemic disease and prompts cardiac assessment.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Narrowed leg arteries cramp the muscles: peripheral artery disease starves the calf and thigh muscles of blood, causing the claudication pain that comes on with walking and, when severe, threatens the limb.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Atherosclerosis is now treated as inflammation: the anti-IL-1β antibody canakinumab cut cardiovascular events in the CANTOS trial, proving the plaque's inflammatory drive, while oxidized-LDL autoantibodies mark the immune response within it.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Visceral fat fuels the plaque: enlarged adipocytes pour out inflammatory adipokines and free fatty acids that worsen dyslipidemia and insulin resistance, tying central obesity directly to accelerated atherosclerosis.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Diet is frontline prevention: soluble fiber lowers LDL by binding bile acids, and a high-fiber, Mediterranean pattern that cuts saturated fat measurably slows atherosclerosis alongside statins.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Fibrinogen is the clot that finishes the plaque: this acute-phase protein is both a marker of vascular inflammation and the substrate that, on a ruptured plaque, forms the occlusive thrombus of heart attack and stroke.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells are the plaque's brake: they dampen the inflammatory attack on the artery wall, so when their atheroprotective control fails, the lesion grows more inflamed and unstable.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Chronic inflammation anywhere ages the arteries: rheumatoid arthritis accelerates atherosclerosis through its systemic inflammatory load, giving patients excess heart attacks and the cardiovascular death that shortens their lives.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Cholesterol crystals ignite the plaque's inflammasome: ingested by lesion macrophages they activate NLRP3 to release IL-1β, the upstream step CANTOS validated by cutting events with IL-1β blockade — proof inflammation, not just lipid, drives atherosclerosis.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Skin inflammation reaches the arteries: psoriasis carries excess cardiovascular risk, its systemic Th17/IL-17 inflammation accelerating atherosclerosis, so plaque psoriasis is now treated as a vascular risk factor too.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Lupus ages arteries decades early: chronic immune-complex inflammation and steroid exposure drive premature, accelerated atherosclerosis, making cardiovascular disease a leading cause of late death in systemic lupus.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is the inflammatory switch in the artery wall: activated by oxidized LDL and disturbed flow in endothelium and macrophages, it drives the adhesion molecules and cytokines that recruit immune cells and build the plaque.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 shapes the plaque's macrophages: IL-6-driven STAT3 signaling tunes the inflammatory macrophage response within the lesion, contributing to the chronic inflammation that destabilizes atherosclerotic plaque.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Arterial and venous clots share a soil: although atherosclerosis is an arterial disease, it shares risk factors and systemic inflammation with venous thromboembolism, and the two cluster together more than chance.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Clogged coronaries weaken the pump: atherosclerosis of the coronary arteries causes myocardial infarction and chronic ischemia, the leading cause of the ischemic cardiomyopathy that drives heart failure.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Starved limbs cannot heal: atherosclerotic peripheral arterial disease cuts blood flow to the legs, producing ischemic ulcers that resist healing and, in critical limb ischemia, progress to gangrene and amputation.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Hardened brain vessels darken mood: cerebral small-vessel atherosclerosis underlies the 'vascular depression' of later life, a late-onset, often treatment-resistant depression tied to ischemic white-matter injury.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Diseased brain vessels erode the mind: cerebral atherosclerosis causes vascular dementia and lowers the threshold for Alzheimer's, the two often coexisting as the mixed dementia of later life.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Blocked leg arteries starve the skin: peripheral arterial disease from atherosclerosis deprives the limbs of blood, causing ischemic ulcers and gangrene that cannot heal without restored flow.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Small-vessel disease can mimic parkinsonism: cumulative atherosclerotic infarcts in the basal ganglia produce vascular parkinsonism, a gait-predominant syndrome overlapping with Parkinson's disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It starves the bowel of blood: atherosclerosis of the mesenteric arteries causes chronic intestinal angina with post-meal pain and weight loss, and acute occlusion brings catastrophic bowel infarction.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It throttles the kidney's blood supply: atherosclerotic renal artery stenosis causes renovascular hypertension and ischaemic nephropathy, and showers of cholesterol emboli can injure the kidneys.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Chronic limb ischaemia marks the skin: atherosclerotic peripheral arterial disease leaves the legs with hair loss, shiny atrophic cool skin and thickened nails, the trophic changes of poor perfusion.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is fundamentally an inflammatory disease: macrophage foam cells, the NLRP3 inflammasome and IL-1β drive plaque growth and rupture, now targeted by anti-inflammatory colchicine and canakinumab.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It hardens the arteries to the brain: carotid and intracranial atherosclerosis cause transient ischaemic attacks and contribute to vascular cognitive impairment beyond overt stroke.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is the vascular endpoint of metabolic disease: diabetes, dyslipidaemia and the metabolic syndrome accelerate plaque formation, tying atherosclerosis tightly to endocrine dysfunction.
- `connects-to` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — The defining therapy: statins lower LDL and stabilise plaque, the cornerstone of preventing the heart attacks and strokes that atherosclerosis causes.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The artery wall has its own drainage: lymphatic vessels clear cholesterol from the arterial wall in reverse cholesterol transport, and impaired lymphatic function promotes plaque growth.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It shares its biggest cause with lung disease: smoking drives both atherosclerosis and COPD, and the hypoxia of chronic lung disease and sleep apnoea further accelerates arterial plaque.
- `connects-to` → **[ACE Inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — They protect the vessel wall: ACE inhibitors lower blood pressure and improve endothelial function, slowing atherosclerosis and reducing cardiovascular events beyond their pressure effect.
- `connects-to` → **[Herpesvirus](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Infection may inflame the plaque: cytomegalovirus and other herpesviruses are found in atherosclerotic lesions and are proposed to add to the chronic inflammation that drives plaque growth.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — A fish-oil drug cuts events: high-dose icosapent ethyl (purified EPA) reduced cardiovascular events in high-risk patients, one diet-derived therapy with proven benefit in atherosclerosis.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Antibody and RNA drugs slash LDL: PCSK9-inhibitor antibodies (evolocumab) and the siRNA inclisiran drive LDL far below what statins achieve, while anti-inflammatory approaches target the residual inflammatory risk of atherosclerosis.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It is a disease of the artery wall: atherosclerosis builds within the intima — LDL retention, foam-cell-laden macrophages, a smooth-muscle fibrous cap over a lipid-necrotic core — that can rupture and thrombose the vessel.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It starves the heart muscle: coronary atherosclerosis is the cause of myocardial infarction, where plaque rupture and thrombosis occlude an artery and infarct the myocardium — the leading cause of death worldwide.
- `connects-to` → **[Gout](../gout/README.md)** — Urate and inflamed arteries: hyperuricaemia and gout are independently associated with atherosclerosis and cardiovascular events, sharing the NLRP3-inflammasome-driven inflammation that destabilises plaque.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Ischaemic nephropathy: atherosclerosis of the renal arteries and intrarenal vessels starves the glomerulus, causing renovascular hypertension and ischaemic chronic kidney disease.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Ischaemia and arrhythmia: coronary atherosclerosis starves the conduction system, and infarction scars it, causing the heart block and ventricular arrhythmias of ischaemic heart disease.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Accelerated arterial disease: HIV/AIDS speeds atherosclerosis through chronic immune activation, inflammation and antiretroviral metabolic effects, making cardiovascular disease a leading cause of death in treated HIV.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Inflammation injures arteries: chronic inflammatory diseases like inflammatory bowel disease accelerate atherosclerosis, the systemic inflammation damaging the arterial wall beyond traditional risk factors.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Infection that ruptures plaques: COVID-19's hyperinflammatory, prothrombotic state can rupture atherosclerotic plaques and trigger heart attacks and strokes, with lasting cardiovascular risk after recovery.
- `connects-to` → **[NASH](../nash/README.md)** — Fatty liver and arteries: NASH and atherosclerosis share insulin resistance, atherogenic dyslipidaemia and systemic inflammation, and NASH is an independent risk factor for cardiovascular disease.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Accelerated disease: type 1 diabetes dramatically accelerates atherosclerosis through chronic hyperglycaemia, glycation and endothelial injury, making cardiovascular disease its leading cause of death.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelial vasoconstrictor: endothelin-1 from dysfunctional endothelium drives vasoconstriction, smooth-muscle proliferation and inflammation that promote atherosclerotic plaque growth.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammation hypothesis confirmed: IL-1β drives plaque inflammation, and the CANTOS trial showed that blocking it with canakinumab cuts cardiovascular events—proving inflammation as a causal, treatable driver of atherosclerosis.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Endothelial activation: TNF-α upregulates adhesion molecules and CCL2 on the endothelium, recruiting the monocytes that become the foam cells of the atherosclerotic plaque.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Plaque hypoxia: the thickening, metabolically active plaque outgrows its oxygen supply, stabilising HIF-1α to drive the intraplaque angiogenesis and inflammation that destabilise it.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — OxLDL sensing: TLR4 on plaque macrophages recognises oxidised LDL and other danger signals, igniting the NF-κB inflammation that converts lipid uptake into the chronic immune disease of atherosclerosis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Myeloid alarmin: S100A8/A9 from activated plaque neutrophils and monocytes amplifies vascular inflammation and circulates as a biomarker predicting atherosclerotic cardiovascular events.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 plaque immunity: IFN-γ from plaque T cells activates macrophages and suppresses smooth-muscle collagen synthesis, thinning the fibrous cap and predisposing the plaque to rupture.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — RAGE on endothelium and macrophages senses advanced glycation end-products and oxidized LDL, amplifying the NF-κB-driven plaque inflammation that explains the accelerated, diffuse atherosclerosis of diabetes mellitus.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3-mediated apoptosis of plaque macrophages and smooth-muscle cells, when efferocytic clearance fails, builds the lipid-rich necrotic core that makes an atherosclerotic plaque unstable and prone to rupture.
- `connects-to` → **[von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — When an atherosclerotic plaque ruptures, exposed subendothelium and released von Willebrand factor mediate the platelet adhesion that nucleates the occlusive thrombus of myocardial infarction and ischemic stroke.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Advanced atherosclerotic plaques calcify as smooth-muscle cells transdifferentiate toward an osteoblast-like phenotype, the calcium deposition measured by coronary-artery-calcium scoring to quantify plaque burden and refine cardiovascular risk.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Xanthine-oxidase-derived reactive oxygen species oxidize LDL trapped in the arterial wall, and it is this oxidized LDL—not native LDL—that macrophages devour to become the foam cells at the heart of the plaque.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is highly expressed by the lipid-laden macrophages of the atherosclerotic plaque, promoting their inflammatory activation and serving as a circulating biomarker of plaque burden and cardiovascular risk.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF from platelets and plaque cells drives migration and proliferation of vascular smooth-muscle cells (already mapped) from media to intima, building the fibrous cap and stenotic neointima of atherosclerosis.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β regulates collagen synthesis and the stability of the atherosclerotic fibrous cap, opposing the inflammatory forces (IL-1β already mapped) that thin the cap toward rupture.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Angiopoietin-driven angiogenesis produces the fragile intraplaque neovessels that hemorrhage and destabilize advanced atherosclerotic plaques, precipitating acute events.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4 sensing of oxidized LDL signals through MyD88 to NF-κB (both already mapped), igniting the sterile innate inflammation that converts lipid deposition into progressive atherosclerotic plaque.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling counters the oxidative modification of LDL and the vascular oxidative stress central to atherogenesis and endothelial injury.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — The PI3K-AKT-eNOS axis maintains endothelial nitric-oxide production (NO already mapped), and its impairment promotes the endothelial dysfunction that initiates atherosclerosis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Oxidized-LDL and PDGF-driven ERK-MAPK signaling (PDGF mapped) promotes the smooth-muscle proliferation and migration that build the atherosclerotic plaque.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR regulation of macrophage autophagy and efferocytosis governs dead-cell clearance and the necrotic-core expansion of atherosclerotic plaques.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IFN-γ and IL-6 signaling through JAK-STAT (both mapped) drives the chronic vascular inflammation central to atherogenesis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cholesterol-crystal and mitochondrial DNA engagement of cGAS-STING amplifies the sterile inflammation of the atherosclerotic plaque.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) governs the smooth-muscle and fibrous-cap responses that determine plaque stability in atherosclerosis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ-STAT1 signaling drives the macrophage activation and antigen presentation that propagate the chronic immune response of atherosclerosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the endothelial and macrophage oxidative-stress and lipid-handling responses relevant to atherosclerotic plaque biology.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic CD8 and NK activity contributes to the plaque instability and necrotic-core formation of atherosclerosis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven vascular smooth-muscle-cell proliferation contributes to the intimal hyperplasia of the atherosclerotic plaque.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the macrophage inflammatory and foam-cell signaling within the atherosclerotic plaque.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the endothelial activation and macrophage survival of the atherosclerotic lesion.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, a regulator of vascular lipid metabolism and inflammation, is atheroprotective and its dysregulation promotes atherosclerosis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy (including macrophage lipophagy) modulates the foam-cell formation and plaque stability of atherosclerosis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the endothelial activation and vascular-smooth-muscle responses of atherosclerosis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte recruitment into the arterial wall drives the inflammation of atherosclerosis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation (including clonal hematopoiesis) participates in the vascular inflammation and atherogenesis of atherosclerosis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the smooth-muscle-cell and leukocyte dynamics of atherosclerotic plaques.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the vascular inflammation and plaque immunobiology of atherosclerosis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the vascular inflammation and plaque instability of atherosclerosis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory and lipid-driven vascular injury of atherosclerosis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the macrophage and vascular-cell gene programs of atherosclerosis.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Adaptive plaque immunity: atherosclerosis has an adaptive immune component, with MHC class II presentation of oxidised-LDL and ApoB peptides to T cells shaping the inflammation of the plaque, a target of experimental atherosclerosis vaccines.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Plaque rupture: rupture of an atherosclerotic plaque triggers coronary thrombosis and myocardial infarction, and troponin release marks the resulting myocardial injury, the acute clinical endpoint of the disease.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and inflammation: obesity accelerates atherosclerosis, and the adipokine leptin promotes endothelial dysfunction, macrophage foam-cell formation and vascular inflammation, linking metabolic syndrome to plaque progression.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Atheroprotective cytokine: the anti-inflammatory cytokine IL-10 restrains plaque inflammation and stabilises lesions, so the balance between it and the pro-inflammatory IL-1 and TNF (already mapped) shapes plaque progression and rupture risk.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex protection: estrogen improves endothelial function and lipid profiles, and its premenopausal presence delays atherosclerosis in women, contributing to the sex and age differences in cardiovascular risk.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Plaque destabilisation: mast cells in the atherosclerotic plaque release proteases and histamine that degrade the fibrous cap (collagen already mapped) and promote intraplaque haemorrhage, contributing to the rupture behind acute events.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Thromboxane and inflammation: the prostaglandin balance shifts toward the prothrombotic thromboxane on the atherosclerotic plaque, part of why low-dose aspirin is used, while inflammatory prostaglandins (IL-6 and IL-1 already mapped) drive the lesion.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Protective adipokine: adiponectin is anti-inflammatory and anti-atherogenic, and its fall in obesity and the metabolic syndrome (leptin already mapped) removes a brake on the vascular inflammation that drives atherosclerosis.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance: insulin resistance and hyperinsulinaemia promote endothelial dysfunction (nitric oxide already mapped) and the atherogenic dyslipidaemia (cholesterol already mapped), accelerating the atherosclerosis of the metabolic syndrome and diabetes.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Macrophage polarisation: IL-4 polarises the plaque macrophages (already mapped) toward an M2 phenotype (IL-10 already mapped), and the balance between the inflammatory and resolving macrophages shapes the stability of the atherosclerotic lesion.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Pro-atherogenic adipokine: resistin, with leptin (already mapped) and the fall in adiponectin (already mapped), is a pro-inflammatory adipokine that promotes the endothelial dysfunction and vascular inflammation of atherosclerosis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Plaque iron handling: the hepcidin-regulated iron handling of the plaque macrophages (already mapped) influences the oxidative stress (xanthine oxidase already mapped) of the lesion, the basis of the iron hypothesis of atherosclerosis.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — LDL oxidation: iron catalyses the oxidation of the LDL (cholesterol already mapped) that generates the oxidised LDL taken up by the foam-cell macrophages (already mapped), the iron hypothesis (hepcidin already mapped) of atherogenesis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 plaque arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the plaque inflammation, a potentially plaque-stabilising phenotype in atherosclerosis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and endothelial protection: zinc is an antioxidant and endothelial-protective trace metal, and its deficiency promotes the oxidative stress and endothelial dysfunction (nitric oxide already mapped) of atherosclerosis.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Coronary disease: the coronary atherosclerosis causes the angina and the myocardial infarction (troponin already mapped) of the heart, the leading cause of death.
- `connects-to` → **[Familial hypercholesterolemia](../familial-hypercholesterolemia/README.md)** — Monogenic driver: familial hypercholesterolaemia (LDL and PCSK9 already mapped) causes the premature, severe atherosclerosis, the extreme of the cholesterol-driven disease.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Atherothrombosis: the platelets aggregate on the ruptured plaque (VWF and thrombin already mapped) to form the occlusive thrombus, the atherothrombotic MI and stroke.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 plaque polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the plaque inflammation that destabilises the atherosclerotic lesion.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate plaque interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the cholesterol-crystal and cellular stress, amplifies the macrophage (already mapped) inflammation of the atheroma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension modulating the Th1-driven atherosclerotic inflammation.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of the atherosclerotic plaque.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Mast-cell arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), arms the plaque mast cells whose degranulation destabilises the atheroma.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Plaque antigen presentation: the dendritic cells present the oxidised-LDL and other plaque antigens (MHC already mapped), shaping the adaptive T-cell response of the atheroma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the monocyte and mast-cell (already mapped) recruitment into the atherosclerotic plaque.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) on the oxidised LDL contribute to the plaque inflammation and the membrane-attack-complex injury of atherosclerosis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) on the oxidised LDL, and its variants are linked to the risk of atherosclerosis.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the oxidised LDL and C-reactive protein in the atherosclerotic plaque.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Plaque matricellular: osteopontin, produced by the foam-cell macrophages (already mapped) and smooth-muscle cells (already mapped), is a matricellular mediator of the plaque inflammation and the vascular calcification of atherosclerosis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Plaque iron: transferrin, the iron carrier, reflects the disordered iron handling and the intraplaque-haemorrhage iron that aggravates the oxidative injury of the atherosclerotic plaque.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-plaque axis: TSLP, from activated endothelium (already mapped) and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/eosinophil plaque inflammation and the vulnerable-plaque formation of atherosclerosis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-vascular axis: bradykinin, via B2 receptors on arterial endothelium (already mapped), releases NO and prostacyclin and modulates the vasotension and endothelial dysfunction of the atherosclerotic risk dimension of atherosclerosis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Vascular erythropoietin: erythropoietin, via the EPOR on endothelial cells (already mapped) and smooth-muscle cells (already mapped), exerts cardioprotective and anti-inflammatory effects that modulate the vascular damage of atherosclerosis.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell plaque: histamine, from mast cells in the atherosclerotic plaque (already mapped), degrades the fibrous cap (collagen already mapped) and amplifies the intraplaque inflammation and vulnerable-plaque formation of atherosclerosis.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Antioxidant-plaque axis: melatonin, via MT1/MT2 receptors and its radical-scavenging activity, reduces the oxidised-LDL (LDL already mapped) load and the endothelial dysfunction that drive the progression of atherosclerosis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex-hormone vascular axis: testosterone, via androgen receptors on endothelium (already mapped) and smooth-muscle cells (already mapped), modulates the lipid profile (LDL and HDL already mapped) and vascular tone of atherosclerosis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Atherosclerosis serotonin: serotonin, via 5-HT receptors on platelets (already mapped) and smooth-muscle cells (already mapped), amplifies vasoconstriction; serotonin worsens the nitric-oxide (already mapped) and NF-κB (already mapped) atherogenic cascade of atherosclerosis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Atherosclerosis prolactin: prolactin, via PRLR on endothelium (already mapped) and macrophages (already mapped), promotes foam-cell formation; hyperprolactinaemia amplifies the NF-κB (already mapped) and NLRP3 (already mapped) atherogenic inflammatory cascade of atherosclerosis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Atherosclerosis oxytocin: oxytocin, via OXTR on endothelium (already mapped) and macrophages (already mapped), attenuates atherogenic inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and NLRP3 (already mapped) inflammatory plaque cascade of atherosclerosis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Atherosclerosis vasopressin: vasopressin, via V1aR on smooth-muscle cells (already mapped) and endothelium (already mapped), promotes vasoconstriction; vasopressin dysregulation amplifies the NF-κB (already mapped) and NLRP3 (already mapped) plaque cascade of atherosclerosis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Atherosclerosis selenium: selenium, as GPx in endothelial cells (already mapped) and macrophages (already mapped), scavenges atherogenic ROS; selenium deficiency amplifies the NF-κB (already mapped) and NLRP3 (already mapped) inflammatory plaque cascade of atherosclerosis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Atherosclerosis iodine: iodine-dependent thyroid hormones modulate cholesterol (already mapped) homeostasis and endothelial (already mapped) function; iodine deficiency amplifies the NF-κB (already mapped) and NLRP3 (already mapped) atherogenic plaque cascade of atherosclerosis.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Atherosclerosis sodium: excess dietary sodium drives endothelial-cell (already mapped) inflammation; sodium amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) atherogenic plaque and thrombin (already mapped) cascade.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Atherosclerosis potassium: potassium regulates endothelial-cell (already mapped) membrane function; potassium dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) atherogenic cascade in atherosclerosis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Atherosclerosis magnesium: magnesium stabilises endothelial-cell (already mapped) function and attenuates platelet (already mapped) aggregation; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and fibrinogen (already mapped) atherogenic cascade.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — chloride channels on macrophages (already mapped) and smooth-muscle cells (already mapped) regulate intracellular pH; chloride dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) atherogenic plaque cascade in atherosclerosis.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — H2S from sulfur-amino acids in macrophages (already mapped) and smooth-muscle cells (already mapped) scavenges ROS; sulfur deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) atherogenic plaque cascade in atherosclerosis.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — nitric oxide from iNOS in macrophages (already mapped) and smooth-muscle cells (already mapped) modulates vascular tone; nitrogen excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) atherogenic plaque cascade in atherosclerosis.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Athero hydrogen: hydrogen via ROS balance in macrophages (already mapped) and endothelial cells (already mapped) modulates plaque oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) cascade in atherosclerosis.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Athero phosphorus: phosphorus-driven ATP in smooth-muscle cells (already mapped) and endothelial cells (already mapped) sustains vascular homeostasis; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) in atherosclerosis.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Athero pd-1: PD-1 on t-cytotoxic cells (already mapped) and regulatory T cells (already mapped) restrains plaque inflammation; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) atheroinflammatory plaque destabilisation.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Athero glp-1: GLP-1 on macrophages (already mapped) and endothelial cells (already mapped) attenuates vascular skewing; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) atheroinflammatory plaque cascade in atherosclerosis.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Athero angiotensin-ii: angiotensin II on smooth-muscle cells (already mapped) and endothelial cells (already mapped) promotes remodelling; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) athero cascade in atherosclerosis.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Athero wnt-beta-catenin: WNT/β-catenin on smooth-muscle cells (already mapped) and endothelial cells (already mapped) regulates homeostasis; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) in atherosclerosis.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Athero rankl: RANKL in macrophages (already mapped) and smooth-muscle cells (already mapped) modulates plaque bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Athero il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates plaque immune surveillance; il-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — Athero notch: NOTCH on smooth-muscle cells (already mapped) and endothelial cells (already mapped) regulates vascular cell fate; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Athero igf-1: IGF-1 from macrophages (already mapped) and smooth-muscle cells (already mapped) promotes plaque growth; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Athero activin-a: activin-A from macrophages (already mapped) and smooth-muscle cells (already mapped) regulates plaque fibro-inflammatory balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Athero cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) atherosclerotic cascade.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^ross-1999-atherosclerosis-review]: Ross R. Atherosclerosis — an inflammatory disease. *N Engl J Med.* 1999;340(2):115-126. [doi:10.1056/NEJM199901143400207](https://doi.org/10.1056/NEJM199901143400207) · [PubMed 9887164](https://pubmed.ncbi.nlm.nih.gov/9887164/)
[^ridker-2017-cantos]: Ridker PM, Everett BM, Thuren T, et al. Antiinflammatory Therapy with Canakinumab for Atherosclerotic Disease. *N Engl J Med.* 2017;377(12):1119-1131. [doi:10.1056/NEJMoa1707914](https://doi.org/10.1056/NEJMoa1707914) · [PubMed 28845751](https://pubmed.ncbi.nlm.nih.gov/28845751/)
[^sabatine-2017-pcsk9]: Sabatine MS, Giugliano RP, Keech AC, et al. Evolocumab and Clinical Outcomes in Patients with Cardiovascular Disease. *N Engl J Med.* 2017;376(18):1713-1722. [doi:10.1056/NEJMoa1615664](https://doi.org/10.1056/NEJMoa1615664) · [PubMed 28304224](https://pubmed.ncbi.nlm.nih.gov/28304224/)
