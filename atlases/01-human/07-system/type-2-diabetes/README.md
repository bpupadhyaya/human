---
schema: human-scale-entry/v1
id: type-2-diabetes
name: Type 2 Diabetes
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic metabolic disease from progressive insulin resistance and β-cell failure. Driven by obesity and inactivity. First-line: metformin (AMPK activation); GLP-1 agonists and SGLT2 inhibitors provide cardiovascular and renal benefit beyond glycemic control."
aliases: ["T2DM", "type 2 diabetes mellitus", "non-insulin-dependent diabetes", "NIDDM", "adult-onset diabetes"]
sources:
  - id: defronzo-2009-t2dm
    type: peer-reviewed
    cite: "DeFronzo RA. Banting Lecture. From the triumvirate to the ominous octet: a new paradigm for the treatment of type 2 diabetes mellitus. Diabetes. 2009;58(4):773-795."
    doi: "10.2337/db09-9028"
    pmid: "19336687"
    url: "https://doi.org/10.2337/db09-9028"
  - id: zinman-2015-empareg
    type: peer-reviewed
    cite: "Zinman B, Wanner C, Lachin JM, et al. Empagliflozin, Cardiovascular Outcomes, and Mortality in Type 2 Diabetes. N Engl J Med. 2015;373(22):2117-2128."
    doi: "10.1056/NEJMoa1504720"
    pmid: "26378978"
    url: "https://doi.org/10.1056/NEJMoa1504720"
  - id: marwick-2018-t2dm-cv
    type: peer-reviewed
    cite: "Marwick TH, Ritchie R, Shaw JE, Kaye D. Implications of Underlying Mechanisms for the Recognition and Management of Diabetic Cardiomyopathy. J Am Coll Cardiol. 2018;71(3):339-351."
    doi: "10.1016/j.jacc.2017.11.019"
    pmid: "29348028"
    url: "https://doi.org/10.1016/j.jacc.2017.11.019"
cross_links:
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "T2DM is a disease of insulin signaling failure: IRS-1 Ser307 phosphorylation (by JNK/IKKβ) uncouples PI3K → impaired glucose uptake; progressive β-cell glucotoxicity reduces insulin secretion; therapies must address both peripheral resistance and secretory failure."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "Metformin (first-line T2DM therapy) activates AMPK via complex I inhibition → AMPK phosphorylates ACC and activates GLUT4 trafficking; AMPK also inhibits mTORC1 → reduced hepatic glucose output; loss of AMPK activity in obesity and insulin resistance contributes to hyperglycemia."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Diabetes is the leading cause of CKD globally (~40% of CKD); hyperglycemia drives mesangial expansion, podocyte injury, and GBM thickening → diabetic nephropathy; SGLT2 inhibitors provide renoprotection independent of glycemic control (CREDENCE, DAPA-CKD trials)."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "T2DM and hypertension co-occur in >70% of patients via shared insulin resistance and RAAS activation; combined hyperglycemia and hypertension accelerate CVD, retinopathy, and nephropathy; preferred antihypertensives in T2DM are ACEi or ARB (renoprotective)."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "GLP-1R agonists (semaglutide, liraglutide, dulaglutide) reduce HbA1c 1-1.5% and weight 5-15%; glucose-dependent insulin secretion avoids hypoglycemia; SUSTAIN-6 (semaglutide) and LEADER (liraglutide) showed CV risk reduction in T2D with established cardiovascular disease."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "EMPA-REG OUTCOME (empagliflozin, T2D + CVD): 14% MACE reduction, 35% CV death reduction, 35% HHF reduction; SGLT2 inhibitors reduce HbA1c ~0.7-1.0% with glucose-dependent mechanism avoiding hypoglycemia; first-line therapy in T2D with established ASCVD or heart failure."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Hyperglycemia → excess AGE formation → RAGE on endothelium and macrophages → NF-κB → VCAM-1, ICAM-1, MCP-1 → diabetic micro- and macroangiopathy; soluble RAGE (sRAGE, a decoy) is inversely associated with T2D complications; RAGE also mediates AGE-driven β-cell dysfunction."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Ghrelin opposes insulin: GHSR1a in pancreatic β cells → reduced insulin secretion; obese T2DM patients have blunted ghrelin suppression after meals; GLP-1 receptor agonists suppress ghrelin surges — contributing to satiety; anamorelin (GHSR1a agonist) treats cancer cachexia."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "GH is counter-regulatory: raises plasma glucose via hepatic output and peripheral insulin resistance (GHR/STAT5 → IRS-1 serine phosphorylation); acromegaly causes T2DM in 25-40%; declining GH/IGF-1 with aging contributes to metabolic inflexibility and abdominal adiposity."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "MTNR1B rs10830963 impairs beta-cell MT2 inhibition of insulin → elevated fasting glucose → T2DM risk; melatonin suppresses nocturnal insulin secretion; high-dose melatonin reduces insulin sensitivity in susceptible individuals; MT2 agonists under investigation for T2DM."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Leptin resistance in obesity links to T2DM: SOCS3 impairs IRS-1 → convergent blunting of leptin and insulin signalling; hyperleptinemia independently predicts T2DM onset; metformin reduces leptin; bariatric surgery lowers leptin and improves insulin sensitivity."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "T2DM → elevated sclerostin via AGE accumulation in osteocyte lacuno-canalicular network; contributes to impaired bone quality despite normal BMD; diabetic patients have higher fracture risk at any given BMD due to sclerostin-mediated osteoblast suppression."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Obese adipocyte CCL2 → CCR2+ monocyte recruitment → adipose tissue macrophage (ATM) infiltration → M1 polarization → TNF-α + IL-6 → hepatic and skeletal muscle insulin resistance; crown-like structures (ATM clusters around dead adipocytes) predict T2DM independently of BMI."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity is the dominant driver of type 2 diabetes: excess, dysfunctional adipose tissue releases free fatty acids and inflammatory cytokines causing insulin resistance, overworking β-cells until they fail—so weight loss can prevent or even remit T2DM."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Type 2 diabetes powerfully accelerates atherosclerosis: hyperglycemia, dyslipidemia and insulin resistance injure the endothelium and inflame plaques, so cardiovascular disease is the leading cause of death in diabetics—driving aggressive risk-factor control."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "The adipocyte sits at the heart of type 2 diabetes: enlarged, stressed fat cells become insulin-resistant and secrete adipokines and free fatty acids that spread resistance to muscle and liver—adipose tissue as an endocrine driver, not just a fat store."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Type 2 diabetes is a bihormonal disease, not just insulin failure: alpha cells oversecrete glucagon while beta cells under-secrete insulin, so unchecked glucagon drives hepatic glucose output—why GLP-1 and amylin-based drugs that suppress glucagon help control it."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Type 2 diabetes ends in pancreatic beta-cell failure: insulin resistance first forces beta cells to overwork, but they progressively exhaust and die, so the pancreas's declining insulin output—not just resistance—drives the need for insulin therapy over time."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Type 2 diabetes roughly doubles stroke risk: chronic hyperglycemia accelerates atherosclerosis and small-vessel disease while high glucose worsens stroke outcome, so glycemic and vascular risk-factor control is central to preventing the cerebrovascular toll of diabetes."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Type 2 diabetes is a leading cause of blindness via retinopathy: chronic hyperglycemia damages retinal microvessels, causing leakage, ischemia, and neovascularization—so annual retinal screening and tight glucose and blood-pressure control protect vision."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Diabetic peripheral neuropathy is among type 2 diabetes' most common complications: hyperglycemia and microvascular injury damage long nerves, causing stocking-glove numbness and pain that underlie foot ulcers and amputations—so foot care is central to management."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Type 2 diabetes and the liver are tightly linked through fatty liver disease: insulin resistance drives hepatic fat accumulation (MASLD/MASH), which worsens glucose control and can progress to cirrhosis—so the diabetic liver is both cause and casualty of the disease."
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Type 2 diabetes is the leading cause of diabetic retinopathy: chronic hyperglycemia damages retinal microvessels, causing the leading preventable blindness in working-age adults—so glucose and blood-pressure control plus eye screening protect vision."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Type 2 diabetes drives heart failure independently: hyperglycemia and insulin resistance stiffen and weaken the myocardium (diabetic cardiomyopathy), and SGLT2 inhibitors—first diabetes drugs—now treat heart failure even in non-diabetics."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Type 2 diabetes is fueled by adipose inflammation via TNF-alpha: enlarged fat tissue releases TNF-alpha and other cytokines that impair insulin signaling, linking obesity's chronic low-grade inflammation directly to insulin resistance."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium deficiency feeds type 2 diabetes: low magnesium worsens insulin resistance and is common in poorly controlled diabetes (and worsened by it), so correcting it modestly improves glucose control—a two-way street between the mineral and the disease."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome shapes type 2 diabetes: dysbiosis fuels low-grade inflammation and insulin resistance, and metformin partly works by reshaping gut bacteria—so what lives in the intestine influences blood sugar."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol drives the diabetes of stress and steroids: the hormone raises blood glucose by spurring the liver and blunting insulin, so chronic stress, Cushing's, and steroid therapy can unmask or worsen type 2 diabetes."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Insulin is packaged with zinc: beta cells store the hormone as zinc-coordinated crystals, and the zinc transporter ZnT8 is both a diabetes-risk gene and an autoantibody target, tying trace-metal handling to the disease."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Type 2 diabetes is the leading cause of kidney failure: years of high glucose scar the glomeruli (diabetic nephropathy), so protecting the kidney with SGLT2 inhibitors and blood-pressure control is central to long-term care."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages link fat to insulin resistance in type 2 diabetes: inflamed adipose tissue recruits macrophages whose cytokines blunt insulin signaling, so this immune-metabolic crosstalk helps turn obesity into diabetes."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Type 2 diabetes is at its core a cardiovascular disease: it doubles the risk of heart attack and heart failure, which remain the leading cause of death, so modern care prizes drugs that protect the heart, not just lower glucose."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "High glucose injures the endothelial cells lining blood vessels: this endothelial dysfunction is the shared root of diabetes's micro- and macrovascular complications, from retinopathy and nephropathy to accelerated atherosclerosis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Insulin drives potassium into cells, so diabetes is also a potassium story: emergencies like ketoacidosis hide a whole-body deficit, and giving insulin can crash serum potassium dangerously low unless it is replaced."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The red cell keeps diabetes's three-month diary: glucose sticks irreversibly to hemoglobin over the erythrocyte's lifespan, so the HbA1c reflects average blood sugar and has become the central test for diagnosing and tracking the disease."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Diabetes is written on the skin: the velvety darkening of acanthosis nigricans flags the insulin resistance, while poor circulation and nerve loss turn minor foot wounds into the slow-healing ulcers that threaten amputation."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons screen for diabetes's silent damage: retinal photography and OCT catch the eye disease before vision is lost, the workhorse imaging of the annual checks that protect organs the high sugar attacks unnoticed."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Diabetes leaves its mark on hemoglobin: glucose sticks irreversibly to the protein, and the fraction so glycated — HbA1c — averages three months of blood sugar, becoming the single number that diagnoses diabetes and steers its treatment."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "The microvascular damage shows under the electron microscope: chronic high sugar thickens the capillary basement membranes throughout the body, the ultrastructural change underlying the kidney, eye, and nerve damage of diabetes."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Diabetes unsettles the bowel: autonomic neuropathy and altered gut microbiome disturb colonic motility, producing the alternating constipation and diabetic diarrhea that trouble many with long-standing disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Sugar slowly poisons the nerves: chronic hyperglycemia injures the longest neurons first, dying back from the toes in the stocking-glove numbness, burning pain, and lost sensation of diabetic peripheral neuropathy."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "What's absent helps define it: type 2 diabetes is not autoimmune, so the islet autoantibodies of type 1 are missing, and finding GAD antibodies in an adult labeled type 2 instead reveals latent autoimmune diabetes (LADA)."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Diabetes cripples repair: poor circulation, neuropathy, and high glucose stalling immune cells turn minor foot injuries into chronic non-healing ulcers, the leading path to the amputations that shadow the disease."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Diabetes and fatty liver feed each other: insulin resistance drives fat into the liver, and the resulting NASH worsens glucose control while progressing toward cirrhosis — a metabolic pairing that GLP-1 and related drugs now target together."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "High sugar shears the kidney's filter cells: chronic hyperglycemia and glomerular hyperfiltration injure the podocytes, and as these hard-to-replace cells detach, albumin leaks into the urine — the first sign of diabetic kidney disease."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Diabetes reaches reproductive health: vascular and nerve damage cause erectile dysfunction in men, insulin resistance underlies the PCOS often preceding it in women, and poorly controlled glucose in pregnancy harms the fetus."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "The liver pumps out sugar it shouldn't: insulin-resistant hepatocytes keep running gluconeogenesis even when glucose is already high, so excess hepatic glucose output drives the fasting hyperglycemia that metformin works to restrain."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation links fat to insulin resistance: IL-6 and other cytokines released by enlarged, stressed adipose tissue interfere with insulin signaling in muscle and liver, part of the low-grade inflammation that ties obesity to type 2 diabetes."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "It reaches the aging brain: insulin resistance and chronic hyperglycemia raise the risk of dementia, including Alzheimer's, so strongly that the disease is sometimes called 'type 3 diabetes' for the brain's own faltering insulin signaling."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is the inflammatory hub of insulin resistance: free fatty acids and cytokines activate NF-κB in liver, fat and muscle, blunting insulin signaling — the mechanism behind the chronic low-grade inflammation that drives type 2 diabetes."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "High sugar tips the blood toward clotting: type 2 diabetes raises fibrinogen and platelet reactivity and impairs fibrinolysis, contributing to a prothrombotic state that modestly increases deep-vein thrombosis and pulmonary embolism risk."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "It blunts defenses and worsens infection: hyperglycemia impairs neutrophil function and wound healing, making people with diabetes more prone to severe infections and to sepsis when those infections take hold."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "The link runs both ways: long-standing type 2 diabetes modestly raises pancreatic cancer risk, while new-onset diabetes in an older adult can be the first sign of an occult pancreatic tumor destroying islet function."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Sugar feeds the yeast: glucose-rich tissues and impaired immunity in diabetes favor Candida overgrowth, causing the recurrent vulvovaginal, oral and skin-fold candidiasis that often flags poor glycemic control."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "It is a major global TB risk factor: diabetes roughly triples the risk of progressing to active tuberculosis and worsens its outcomes, a converging epidemic as type 2 diabetes spreads through TB-endemic regions."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Diabetes and depression feed each other: living with the disease and its complications raises depression risk, and depression in turn worsens glycemic control and self-care, a well-documented bidirectional loop."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "It weakens bone quality despite normal density: type 2 diabetes raises fracture risk through poor bone quality and falls, and the thiazolidinediones used to treat it accelerate bone loss."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "High glucose blunts the defenses against mold: the impaired neutrophil function and immune dysregulation of poorly controlled diabetes raise susceptibility to invasive fungal infection, including pulmonary aspergillosis."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Chronic hyperglycaemia damages the nerves: distal symmetric diabetic polyneuropathy is among the commonest causes of neuropathic pain, with burning feet, numbness and the risk of unfelt foot injury."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Autonomic neuropathy slows the gut: long-standing type 2 diabetes can cause gastroparesis with nausea, bloating and erratic glucose control, plus diabetic diarrhoea and constipation from enteric nerve damage."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A demanding chronic disease breeds worry: the relentless self-management, fear of hypoglycaemia and dread of complications in type 2 diabetes generate diabetes distress and chronic anxiety alongside depression."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is the archetypal endocrine disorder: insulin resistance with progressive beta-cell failure dysregulates the body's central metabolic hormone, deranging glucose, lipid and counter-regulatory hormone signalling throughout the system."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It marks the skin in many ways: acanthosis nigricans signals insulin resistance, while diabetic dermopathy, necrobiosis lipoidica and neuropathic-ischaemic foot ulcers track the vascular and nerve damage of type 2 diabetes."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Hyperglycaemia blunts host defence: high glucose impairs neutrophil function and complement, so type 2 diabetes raises susceptibility to skin, urinary, foot and respiratory infections and worsens their severity."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It is a cardiovascular risk-equivalent: type 2 diabetes drives a specific diabetic cardiomyopathy and, through autonomic neuropathy, can cause silent myocardial infarction."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It damages nerves widely: diabetic peripheral and autonomic neuropathy cause foot ulcers, gastroparesis and postural hypotension, and the disease accelerates cognitive decline."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It stiffens hands and joints: type 2 diabetes causes diabetic cheiroarthropathy, frozen shoulder, Dupuytren's contracture and Charcot neuroarthropathy of the foot."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "First-line lowers the glucose: metformin reduces hepatic glucose output and improves insulin sensitivity, the foundation drug for type 2 diabetes with cardiovascular benefit."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It is the leading cause of kidney failure: diabetic nephropathy from chronic hyperglycaemia damages the glomeruli, the commonest cause of end-stage renal disease worldwide."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It shadows the lungs: type 2 diabetes is strongly associated with obstructive sleep apnoea and raises the risk of pneumonia and tuberculosis through impaired immunity."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: connects-to
    note: "A cardiovascular risk equivalent: type 2 diabetes accelerates atherosclerosis so much that most patients over 40 are offered a statin for primary prevention, lipid-lowering being as central to outcomes as glucose control."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "It scars the filtering unit: chronic hyperglycaemia thickens the glomerular basement membrane and expands the mesangium, producing the Kimmelstiel-Wilson nodules and hyperfiltration that precede the proteinuria of diabetic nephropathy."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Two diseases, one hyperglycaemia: type 2 diabetes arises from insulin resistance with relative insulin deficiency, whereas type 1 is autoimmune destruction of beta cells causing absolute deficiency — distinct causes converging on high glucose and shared complications."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "The beta cell finally fails: type 2 diabetes begins with insulin resistance but progresses as the islets of Langerhans exhaust and lose beta cells—with islet amyloid (IAPP) deposition—so insulin output falls and hyperglycaemia worsens."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It hardens the arteries: type 2 diabetes accelerates atherosclerosis and stiffens the arterial wall through hyperglycaemia, AGEs and dyslipidaemia, making macrovascular disease—heart attack and stroke—the leading cause of diabetic death."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Insulin resistance raises urate: type 2 diabetes and gout cluster within the metabolic syndrome, as hyperinsulinaemia reduces renal uric-acid excretion and shared obesity drives both."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Insulin and oestrogen drive it: type 2 diabetes and its obesity raise endometrial cancer risk markedly, as hyperinsulinaemia and adipose-derived oestrogen both stimulate endometrial proliferation."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Diabetic cardiomyopathy: glucotoxicity and AGE deposition stiffen the myocardium and cause heart failure with preserved ejection fraction, independent of coronary disease or hypertension."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "The diabetic bone paradox: despite normal or high bone density, type 2 diabetes degrades cortical bone microarchitecture and collagen through AGE cross-linking, paradoxically raising fracture risk."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A two-way danger: type 2 diabetes is a leading risk factor for severe COVID-19 and death, and SARS-CoV-2 can in turn trigger new-onset diabetes and severe hyperglycaemic crises."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "From fatty liver to cancer: type 2 diabetes and its associated NASH markedly raise the risk of hepatocellular carcinoma, now a leading cause of liver cancer in high-income countries even without cirrhosis."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Hyperinsulinaemia and the colon: type 2 diabetes raises colorectal cancer risk and worsens its outcomes through insulin/IGF-1 signalling, while metformin appears to reduce that risk."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Insulin-sensitising adipokine: adiponectin falls as adipose tissue expands, and its decline drives the insulin resistance underlying type 2 diabetes."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Pro-resistance adipokine: resistin from adipose tissue and macrophages promotes insulin resistance and chronic inflammation, contributing to type 2 diabetes."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vascular complications: endothelin-1-driven vasoconstriction and endothelial dysfunction mediate much of the micro- and macrovascular damage of type 2 diabetes."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Islet inflammation: islet amyloid and glucotoxicity activate IL-1β, which damages beta cells—the rationale for IL-1 blockade trials in type 2 diabetes."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Metabolic inflammasome: the NLRP3 inflammasome, activated by excess glucose, lipids and islet amyloid, matures the IL-1β that drives the beta-cell dysfunction of type 2 diabetes."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Adipose hypoxia: as fat mass expands beyond its blood supply, HIF-1α stabilised in hypoxic adipose tissue drives the inflammation underlying insulin resistance in type 2 diabetes."
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "Hepatic glucose output: insulin normally inactivates FOXO1 to switch off gluconeogenesis, so the insulin resistance of type 2 diabetes leaves FOXO1 active in the liver, driving the inappropriate fasting glucose production behind morning hyperglycaemia."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Insulin-resistance mediator: galectin-3 secreted by adipose-tissue macrophages binds the insulin receptor and impairs its signalling, a direct molecular link between the chronic inflammation of obesity and systemic insulin resistance."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: hyperglycaemia and insulin resistance reduce endothelial nitric-oxide bioavailability, the early vascular lesion that underlies the macro- and microvascular complications of type 2 diabetes."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Receptor-level resistance: in type 2 diabetes the insulin receptor and its downstream IRS-PI3K-AKT cascade respond poorly to insulin, the molecular signalling defect of insulin resistance that forces compensatory hyperinsulinaemia until β-cells fail."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Diabetic retinopathy: chronic hyperglycaemia drives retinal ischaemia and VEGF release, fuelling the pathological neovascularisation of proliferative diabetic retinopathy — the leading cause of working-age blindness and the target of intravitreal anti-VEGF therapy."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Diabetic nephropathy: high glucose induces TGF-β in the glomerulus, driving the mesangial-matrix expansion and basement-membrane thickening that produce diabetic kidney disease, the commonest cause of end-stage renal failure."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Core of insulin resistance: insulin signals through the insulin-receptor-PI3K-AKT axis (insulin-receptor and FOXO1 already mapped) to drive glucose uptake and suppress hepatic gluconeogenesis, and impaired AKT signalling is the molecular heart of insulin resistance."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Nutrient-overload feedback: chronic nutrient excess activates mTORC1-S6K, which feeds back to inhibit insulin-receptor-substrate signalling, a mechanism coupling overnutrition and obesity to the insulin resistance of type 2 diabetes."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "Diabetic dyslipidaemia: the atherogenic dyslipidaemia of type 2 diabetes amplifies cardiovascular risk, and PCSK9 (which raises LDL) is targeted alongside the statins already mapped to lower that risk in these high-risk patients."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Metabolic insulin arm: the insulin receptor (mapped) signals through IRS to PI3K and AKT (mapped); blunting of this PI3K branch is the molecular core of insulin resistance in type 2 diabetes."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Glycogen control: insulin-activated AKT (mapped) inhibits GSK-3β to switch on glycogen synthase; elevated GSK-3β activity in type 2 diabetes impairs glycogen storage and insulin signalling."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Selective insulin resistance: while the PI3K metabolic arm is blunted, insulin's MAPK-ERK mitogenic arm remains active in type 2 diabetes, a selectivity that drives the vascular and proliferative complications."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Lipotoxic inflammation: TLR4 sensing of saturated free fatty acids drives the lipotoxic metabolic inflammation that links obesity to the insulin resistance of type 2 diabetes."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate metabolic inflammation: TLR-MyD88-NF-κB signalling (NF-κB and NLRP3 already mapped) transduces nutrient-excess and lipotoxic signals into the chronic metabolic inflammation underlying type 2 diabetes."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Glucotoxic oxidative defence: NRF2 antioxidant defence counters the glucotoxic oxidative stress that damages β-cells and impairs insulin signalling in type 2 diabetes."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Pro-inflammatory IL-6-STAT3 signalling in adipose tissue and liver contributes to the chronic low-grade inflammation that drives insulin resistance in type 2 diabetes."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Mitochondrial and metabolic stress releases cytosolic DNA that engages cGAS-STING, fuelling the metabolic inflammation of adipose tissue in type 2 diabetes."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the islet and renal fibrosis that accompanies β-cell failure and diabetic nephropathy in type 2 diabetes."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2 signaling downstream of IL-6 and other cytokines (IL-6 mapped) propagates the inflammatory insulin resistance of adipose and liver in type 2 diabetes."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling contributes to islet inflammation and β-cell stress in the metabolic-immune milieu of type 2 diabetes."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Calprotectin (S100A8/A9) released by myeloid cells amplifies the chronic low-grade adipose-tissue inflammation that drives insulin resistance in type 2 diabetes."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors (distinct from FOXO1 already mapped) integrate insulin-PI3K-AKT signaling to regulate hepatic gluconeogenesis and β-cell stress responses in type 2 diabetes."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the inflammatory insulin-resistance signaling of adipose and hepatic tissue in type 2 diabetes."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic CD8 T cells contribute to the adipose-tissue immune activation that drives insulin resistance in type 2 diabetes."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the pancreatic β-cell survival and insulin-target-tissue homeostasis whose failure contributes to type 2 diabetes."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic (metabolic-memory) programming of type 2 diabetes."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven chemokine signaling recruits macrophages into adipose tissue, amplifying the inflammation that drives insulin resistance in type 2 diabetes."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the islet-cell and immune-cell interactions of type 2 diabetes."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 and the complement system participate in the metabolic inflammation and insulin resistance of type 2 diabetes."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A-p16 senescence signaling (a genome-wide-association-study locus for type 2 diabetes) participates in the β-cell senescence and dysfunction of type 2 diabetes."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the adipose-tissue immune regulation and metaflammation of type 2 diabetes."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the chronic inflammation of type 2 diabetes."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the metabolic gene programs relevant to type 2 diabetes."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Beta-cell secretion: after glucose closes the KATP channel and depolarises the beta cell, calcium influx triggers the exocytosis of insulin granules, the final step of secretion whose progressive failure underlies the beta-cell dysfunction of type 2 diabetes."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Male hypogonadism: low testosterone is bidirectionally linked with type 2 diabetes in men, as visceral adiposity and insulin resistance suppress testosterone while the resulting hypogonadism further worsens metabolic control and body composition."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Hyperuricaemia and oxidative stress: xanthine oxidase generates uric acid and reactive oxygen species, and the hyperuricaemia clustering with metabolic syndrome contributes to the insulin resistance and endothelial dysfunction of type 2 diabetes."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Silent myocardial infarction: type 2 diabetes accelerates coronary disease (atherosclerosis already mapped) and blunts anginal warning through autonomic neuropathy, so myocardial infarction is often silent, and troponin marks the cardiac injury when it occurs."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Neuropathic pain: painful diabetic peripheral neuropathy (peripheral nerve already mapped) is a major burden, and when other agents fail it is treated with opioids acting at the mu-opioid receptor, at the cost of dependence risk."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopaminergic glucose control: central dopaminergic tone influences glucose metabolism, and the dopamine agonist bromocriptine, given as a morning quick-release formulation, is an approved glucose-lowering therapy for type 2 diabetes."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Atherogenic dyslipidaemia: type 2 diabetes shifts cholesterol handling toward high triglycerides, low HDL and small dense LDL (PCSK9 already mapped), the dyslipidaemia driving much of its accelerated cardiovascular risk."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory balance: the anti-inflammatory IL-10 counters the chronic low-grade inflammation (TNF, IL-6 and IL-1 already mapped) of adipose tissue in type 2 diabetes, and the imbalance contributes to the insulin resistance."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Cardiorenal RAAS: aldosterone drives the fibrosis and inflammation of diabetic kidney disease (angiotensin and endothelin already mapped), and mineralocorticoid-receptor antagonists such as finerenone slow the progression of diabetic nephropathy."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "SGLT2 and cardiorenal benefit: the SGLT2 inhibitors (SGLT2 already mapped) block renal sodium-glucose cotransport, and the resulting natriuresis and tubuloglomerular feedback underlie the cardiovascular and renal protection they confer in type 2 diabetes."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Adipose M2 macrophages: IL-4 sustains the anti-inflammatory M2 macrophages of healthy adipose tissue (IL-10 already mapped), and the shift away from this state toward pro-inflammatory macrophages (TNF already mapped) drives the insulin resistance of type 2 diabetes."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Peripheral metabolic serotonin: gut-derived peripheral serotonin regulates pancreatic β-cell mass and adipose and hepatic metabolism, part of the neuroendocrine control of the energy balance disturbed in type 2 diabetes."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Adipose M2 maintenance: IL-13, with IL-4 (already mapped), sustains the anti-inflammatory M2 macrophages of healthy adipose tissue, and the loss of this type-2 signalling drives the inflammation and insulin resistance of type 2 diabetes."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Insulin secretion trigger: the calcium influx into the β-cell triggers the exocytosis of the insulin (already mapped) granules, the calcium signalling of the glucose-stimulated insulin secretion that fails in type 2 diabetes."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "KATP channel: the ATP-sensitive potassium channel of the β-cell closes on glucose rise to depolarise the cell and trigger insulin (already mapped) release, the target of the sulfonylureas used in type 2 diabetes."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron and insulin resistance: hepcidin, the iron-regulatory hormone; the iron overload (the ferritin, an IL-6-driven already-mapped marker) is associated with the insulin (already mapped) resistance of type 2 diabetes."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenoprotein-P hepatokine: selenium's selenoprotein-P (SELENOP), secreted by the liver (already mapped), acts as a hepatokine that impairs the insulin (already mapped) signalling, linking the selenium status to type 2 diabetes."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Central energy control: the brain's hypothalamic appetite and energy regulation (leptin, ghrelin and insulin already mapped) is central to type 2 diabetes, which also raises the risk of vascular dementia and cognitive decline."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the chronic metabolic inflammation (IL-6 and TNF already mapped) of the insulin resistance of type 2 diabetes."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate metabolic inflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the metabolic stress, contributes to the chronic low-grade inflammation (IL-6 and TNF already mapped) of the insulin resistance of type 2 diabetes."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Adipose Th1 inflammation: the IFN-γ of the adipose-tissue T cells (with the macrophages already mapped) drives the Th1 inflammation that promotes the insulin (already mapped) resistance of type 2 diabetes."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm whose loss (the reduced adipose eosinophils/ILC2s) permits the pro-inflammatory insulin resistance of type 2 diabetes."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic low-grade inflammation of the insulin resistance of type 2 diabetes."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the adipose immune milieu of type 2 diabetes."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Adipose CD4 arm: the CD4 T-helper cells shift toward the Th1/Th17 (IFN-γ and IL-17 already mapped) phenotype in the inflamed adipose tissue, driving the insulin resistance of type 2 diabetes."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adipose CD8 initiator: the CD8 T cells (perforin already mapped) infiltrate the adipose tissue early and recruit and activate the macrophages (already mapped) that drive the insulin resistance of type 2 diabetes."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Adipose mast cells: the mast cells accumulate in the inflamed adipose tissue and contribute to the chronic low-grade inflammation and the insulin resistance of type 2 diabetes."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Adipose B cells: the B cells accumulate in the inflamed adipose tissue and, through pathogenic antibodies and cytokines, promote the insulin resistance of type 2 diabetes."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Adipose antigen presentation: the dendritic cells of the inflamed adipose tissue present antigen to the T cells (already mapped) and sustain the chronic low-grade inflammation of type 2 diabetes."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the macrophage (already mapped) recruitment into the inflamed adipose tissue of type 2 diabetes."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Adipose alarmin: TSLP released from the hypertrophic adipocytes (already mapped) and the inflamed adipose tissue of type 2 diabetes activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the chronic low-grade inflammation."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-kallikrein axis: bradykinin, generated by tissue kallikrein activation in the insulin-resistant adipose and skeletal-muscle tissue of type 2 diabetes, potentiates insulin signalling through its B2R receptor and modulates vascular tone in the diabetic vasculopathy."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-insulin crosstalk: erythropoietin, via the JAK-STAT (already mapped) and PI3K-AKT (already mapped) pathways, modulates insulin sensitivity and β-cell survival, and EPO deficiency contributes to the anaemia of the CKD (already mapped) complication of type 2 diabetes."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact-complement regulation: C1-esterase inhibitor restrains the classical complement C1 (with C3/C5aR1 already mapped) and the kallikrein-kinin system (bradykinin already mapped) activated in the inflamed adipose tissue and vasculopathy of type 2 diabetes."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Adipose mast-cell effector: histamine released by mast cells (already mapped) in the inflamed adipose tissue of T2D amplifies insulin resistance through H1R on adipocytes, driving the vicious cycle of adipose inflammation and metabolic dysfunction."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Adipose fibrosis scaffold: periostin, downstream of TGF-β (already mapped) signalling in the inflamed adipose tissue, promotes the peri-adipocyte fibrosis that impairs adipose expandability and worsens insulin resistance in type 2 diabetes."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "T2D prolactin: prolactin acts as a pancreatic (already mapped) beta-cell survival factor; gestational hyperprolactinaemia promotes beta-cell mass expansion, while elevated prolactin in T2D amplifies insulin resistance and worsens the metabolic dysfunction."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "T2D oxytocin: oxytocin receptors on pancreatic (already mapped) beta-cells modulate insulin (already mapped) secretion in type 2 diabetes; intranasal oxytocin reduces food intake and adiponectin/leptin (already mapped) adipose inflammation, worsening insulin resistance."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "T2D vasopressin: vasopressin (ADH) drives hepatic (already mapped) glucose production via V1b receptor on pancreatic (already mapped) alpha-cells; elevated copeptin predicts T2D risk, and AVP-driven osmotic signalling amplifies the AMPK (already mapped) pathway dysfunction."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "T2D iodine: iodine-dependent thyroid hormones regulate insulin (already mapped) sensitivity and AMPK (already mapped) signalling in type 2 diabetes; hypothyroidism worsens hepatic (already mapped) glucose output and NF-κB (already mapped)-driven adipose inflammation in T2D."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "T2D copper: copper-dependent superoxide dismutase (SOD) combats oxidative stress driving NF-κB (already mapped)-mediated beta-cell (already mapped) damage and insulin (already mapped) resistance in type 2 diabetes; copper dysregulation worsens T2D vascular complications."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "T2D phosphorus: phosphorus is essential for ATP-mediated insulin (already mapped) signalling and AMPK (already mapped) activation in T2D; hyperphosphaturia accelerates CKD (already mapped) progression and FGF-23/phosphate dysregulation amplifies cardiovascular risk in diabetes."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "T2D iron: iron overload promotes hepatocyte (already mapped) and macrophage (already mapped) oxidative stress; iron-induced NF-κB (already mapped) and IL-6 (already mapped) amplify adipocyte (already mapped) inflammation and insulin (already mapped) resistance cascade of T2D."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "T2D chloride: chloride, via CFTR in pancreatic and hepatocyte (already mapped) cells, regulates insulin (already mapped) secretion; chloride dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of type 2 diabetes."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "T2D sulfur: glutathione buffers oxidative stress from NF-κB (already mapped) and AMPK (already mapped) in macrophages (already mapped) and hepatocytes (already mapped); hyperhomocysteinaemia amplifies insulin (already mapped) resistance and IL-6 (already mapped) cascade of T2D."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "T2D nitrogen: nitric oxide from eNOS in endothelial-cell (already mapped) and macrophages (already mapped) preserves insulin (already mapped) sensitivity; nitrogen deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) vascular insulin resistance of T2D."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "T2D oxygen: mitochondrial oxygen consumption in hepatocytes (already mapped) and adipocytes (already mapped) drives ATP for insulin (already mapped) signalling; hypoxia amplifies NF-κB (already mapped) and IL-6 (already mapped) adipose inflammation and insulin resistance of T2D."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "T2D carbon: CO2 in bicarbonate buffering of hepatocytes (already mapped) and macrophages (already mapped) regulates pH for insulin (already mapped) secretion; carbon-metabolite excess amplifies NF-κB (already mapped) and AMPK (already mapped) insulin resistance of T2D."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "T2D PD-1: PD-1 on macrophages (already mapped) and T-helper-cell (already mapped) modulates adipose immune homeostasis; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and GLP-1 (already mapped) resistance cascade of T2D."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "T2D angiotensin-II: angiotensin-II in hepatocytes (already mapped) and adipocytes (already mapped) promotes insulin resistance via RAAS; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of T2D."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "T2D Wnt/β-catenin: Wnt signalling in hepatocytes (already mapped) and adipocytes (already mapped) regulates glucose metabolism; Wnt dysregulation amplifies NF-κB (already mapped) and AMPK (already mapped) and GLP-1 (already mapped) resistance cascade of T2D."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "T2D hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and adipocytes (already mapped), quenches metabolic ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and insulin (already mapped) cascade of type 2 diabetes."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "T2D RANKL: RANKL signalling in macrophages (already mapped) and adipocytes (already mapped) modulates metabolic bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and insulin (already mapped) cascade of type 2 diabetes."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T2D IL-2: IL-2 signalling in T-cells (already mapped) and macrophages (already mapped) modulates immune tolerance; IL-2 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and insulin (already mapped) cascade of type 2 diabetes."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "T2D Fibronectin: Fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds adipose ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "T2D NOTCH: NOTCH on hepatocytes (already mapped) and macrophages (already mapped) regulates adipose metabolic tone; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "T2D IGF-1: IGF-1 from hepatocytes (already mapped) and macrophages (already mapped) promotes insulin sensitivity; IGF-1 loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "T2D activin-a: activin-A from hepatocytes (already mapped) and macrophages (already mapped) regulates adipose immune-fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "T2D cgrp: CGRP from hepatocytes (already mapped) and macrophages (already mapped) modulates adipose neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "T2D calcitonin: calcitonin from hepatocytes (already mapped) and macrophages (already mapped) modulates adipose calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "T2D substance-p: substance-P from hepatocytes (already mapped) and macrophages (already mapped) modulates adipose neuroimmune tone; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "T2D androgen-receptor: androgen receptor on hepatocytes (already mapped) and macrophages (already mapped) modulates T2D hormonal metabolism; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of T2D."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "T2D norepinephrine: norepinephrine from macrophages (already mapped) and hepatocytes (already mapped) amplifies T2D sympathoadrenal stress; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of T2D."
---

# Type 2 Diabetes

## Overview

**Type 2 diabetes mellitus (T2DM)** is a chronic metabolic disease characterized by **hyperglycemia resulting from progressive insulin resistance in peripheral tissues (skeletal muscle, adipose, liver) combined with relative insulin secretory failure** from pancreatic β-cells — the so-called "ominous octet" of pathological defects described by DeFronzo [^defronzo-2009-t2dm]. Unlike type 1 diabetes (autoimmune β-cell destruction → absolute insulin deficiency), T2DM involves a gradual decline from compensated insulin resistance (elevated insulin, normal glucose) → impaired fasting glucose/glucose intolerance → overt T2DM as β-cell compensation fails.

**Global burden:** 537 million people worldwide with T2DM in 2021 (IDF Diabetes Atlas); projected 643 million by 2030; responsible for ~6.7 million deaths/year; a major driver of cardiovascular disease (3-4× increased risk of MI and stroke), chronic kidney disease (leading cause globally), blindness (diabetic retinopathy), and lower limb amputations.

**Pathophysiology triad:**
1. **Insulin resistance:** Muscle and adipose fail to take up glucose in response to insulin → postprandial hyperglycemia; liver fails to suppress gluconeogenesis → fasting hyperglycemia
2. **β-cell dysfunction:** Progressive: hyperinsulinemia → ER stress → lipotoxicity → glucotoxicity → β-cell apoptosis → insulin secretory capacity falls ~50% by T2DM diagnosis and continues declining
3. **Adipocyte dysfunction:** Visceral adiposity → ectopic fat deposition in liver and muscle → lipotoxicity → insulin resistance; adipokine imbalance (↑ TNF-α, IL-6, resistin; ↓ adiponectin)

**Risk factors:** Obesity (BMI >30), physical inactivity, family history (heritability ~40-70%), age >45, hypertension, dyslipidemia, gestational diabetes, polycystic ovary syndrome, certain medications (glucocorticoids, antipsychotics), sleep apnea.

**Genetic architecture:** Highly polygenic (>400 susceptibility loci identified by GWAS); individual SNPs confer modest risk; major loci: TCF7L2 (Wnt/β-catenin → β-cell development), SLC30A8 (ZnT8, β-cell zinc transporter), PPARG (adipogenesis), KCNJ11 (K_ATP channel → insulin secretion).

## Structure

### The DeFronzo "Ominous Octet" — organ-level contributions [^defronzo-2009-t2dm]

Eight organs/tissues contribute to T2DM pathophysiology:
1. **Skeletal muscle (75% of insulin-stimulated glucose disposal):** Impaired GLUT4 translocation → reduced glucose uptake → postprandial hyperglycemia
2. **Liver:** Failure of insulin to suppress gluconeogenesis → fasting hyperglycemia; elevated hepatic glucose output even with hyperinsulinemia (hepatic insulin resistance)
3. **Pancreatic β-cells:** Progressive secretory failure; initially compensatory hypersecretion → burnout from glucotoxicity and lipotoxicity → reduced first-phase insulin release → hyperglycemia
4. **Pancreatic α-cells:** Hyperglucagonemia (α-cells are relatively insulin-resistant in T2DM) → excess hepatic glucose production; GLP-1 agonists suppress glucagon; GIP+GLP-1 dual agonists target both
5. **Adipocytes:** Increased lipolysis → elevated free fatty acids (FFA) → liver (hepatic steatosis, gluconeogenesis), muscle (insulin resistance via ceramide and diacylglycerol), β-cells (lipotoxicity)
6. **Brain:** Central insulin resistance → altered satiety; GLP-1 receptor agonists act centrally to reduce appetite and weight
7. **Kidney:** Increased tubular glucose reabsorption (SGLT2 upregulation in diabetic kidney → exacerbates hyperglycemia); SGLT2 inhibitors exploit this
8. **Gut:** Reduced GLP-1 secretion from L-cells (impaired incretin effect accounts for 50% of postprandial glucose rise); GLP-1 agonists restore this deficit

### Molecular basis of insulin resistance

**Adipokine-driven inflammation:**
- Visceral fat → TNF-α, IL-6, resistin secretion + reduced adiponectin → systemic low-grade inflammation
- TNF-α → IKKβ → IRS-1 Ser307 phosphorylation → IRS-1 degradation → PI3K uncoupled from insulin receptor → Akt not activated → GLUT4 not translocated

**JNK pathway:**
- Saturated fatty acids (palmitate) → ceramide synthesis → ceramide activates PP2A → dephosphorylates Akt → insulin resistance; also via ER stress → IRE1→JNK → IRS-1 Ser307 phosphorylation

**Mitochondrial dysfunction:**
- Reduced mitochondrial biogenesis (reduced PGC-1α in T2DM muscle) → impaired fatty acid oxidation → intramyocellular lipid accumulation (IMCL) → DAG → PKCθ → IRS-1 Ser phosphorylation → insulin resistance

## Function

### Chronic complications: the ABCDE of T2DM

**Microvascular complications (from hyperglycemia):**
- **Diabetic retinopathy:** Pericyte loss → acellular capillaries → microaneurysms → neovascularization (VEGF-driven) → tractional retinal detachment; leading cause of new blindness in working-age adults
- **Diabetic nephropathy:** GBM thickening, mesangial expansion, podocyte injury → proteinuria → progressive CKD → ESRD; GFR declines ~4-10 mL/min/year in proteinuric T2DM
- **Diabetic neuropathy:** Schwann cell dysfunction, axonal degeneration → painful peripheral neuropathy, autonomic neuropathy (gastroparesis, orthostatic hypotension, neurogenic bladder), Charcot foot

**Macrovascular complications (from insulin resistance + dyslipidemia + hypertension):**
- 2-4× increased cardiovascular mortality; atherosclerosis accelerated by endothelial dysfunction (reduced eNOS), foam cell formation, advanced glycation end-products (AGEs → RAGE → NF-κB → inflammation)
- Diabetic cardiomyopathy: impaired cardiac energetics (shift to fatty acid oxidation → reduced efficiency), myocardial fibrosis, diastolic dysfunction [^marwick-2018-t2dm-cv]

### Diagnostic criteria (ADA 2024)

| Test | Diabetes | Pre-diabetes | Normal |
|:---|:---|:---|:---|
| Fasting plasma glucose | ≥126 mg/dL | 100-125 mg/dL | <100 mg/dL |
| 2-hour OGTT | ≥200 mg/dL | 140-199 mg/dL | <140 mg/dL |
| HbA1c | ≥6.5% | 5.7-6.4% | <5.7% |
| Random glucose | ≥200 + symptoms | — | — |

## Pathology

### Cardiovascular-renal metabolic syndrome: the T2DM complication nexus

T2DM, CKD, heart failure, and obesity form the **cardiorenal metabolic (CRM) syndrome** — each condition worsens the others:
- T2DM → diabetic nephropathy → CKD → hypertension → cardiovascular disease
- Heart failure → reduced renal perfusion → cardiorenal syndrome → worsened glycemic control
- Obesity → visceral adiposity → insulin resistance → T2DM → all complications

### Pharmacological management

**Glycemic targets:**
- HbA1c <7.0% (most patients); <6.5% in young, low hypoglycemia risk; <8.0% in elderly/complex
- ADA 2024: Time-in-range (TIR) ≥70% on CGM for adults

**Drug classes (stepwise intensification):**

**Metformin (1st line):**
- Mechanism: AMPK activation (via Complex I inhibition → ATP→AMP rise → AMPK) → hepatic gluconeogenesis suppression (phosphorylates CREB coactivator TORC2) + sensitizes peripheral tissues; also independent of AMPK via direct phosphoglucose isomerase inhibition
- Benefits: neutral/weight loss, low hypoglycemia risk, CV-neutral (UKPDS long-term data), reduced cancer risk (meta-analyses), $4/month
- Limitation: GI intolerance, contraindicated eGFR <30

**GLP-1 receptor agonists (2nd line, cardioprotective):**
- Liraglutide, semaglutide, dulaglutide — GLP-1 mimetics; bind GLP-1R on β-cells → cAMP → PKA → KATP channel closure → insulin secretion (glucose-dependent, no hypoglycemia); also: suppress glucagon, slow gastric emptying, central satiety (weight loss 3-15%)
- **CV outcomes:** LEADER (liraglutide), SUSTAIN-6 (semaglutide), REWIND (dulaglutide) — significant MACE reduction in high-CV-risk T2DM; primary prevention CV benefit: SELECT trial (semaglutide 2.4 mg in obesity, regardless of T2DM)
- Oral semaglutide: first oral GLP-1 agonist (Rybelsus); PIONEER-6: non-inferior to IV

**SGLT2 inhibitors (2nd/3rd line, cardiorenal protective):**
- Empagliflozin, dapagliflozin, canagliflozin — block SGLT2 in proximal tubule → ~60-80 g glucose/day excreted in urine → HbA1c ↓0.7-1.0%; also: osmotic diuresis → BP reduction, weight loss (~2-3 kg)
- **Cardiovascular:** EMPA-REG OUTCOME (empagliflozin): 38% reduction in CV death, 35% reduction in heart failure hospitalization vs placebo in established CVD [^zinman-2015-empareg]; mechanisms beyond glycemic: reduced preload/afterload, improved cardiac energetics, reduced uric acid
- **Renal:** CREDENCE (canagliflozin), DAPA-CKD (dapagliflozin): ~30-40% reduction in renal composite (eGFR decline, ESRD, renal death) — now approved for CKD independent of T2DM; tubuloglomerular feedback mechanism (SGLT2 inhibition → increased NaCl at macula densa → afferent arteriole constriction → reduced glomerular hyperfiltration → long-term nephroprotection)

**Additional agents:**
- **DPP-4 inhibitors (sitagliptin, saxagliptin):** Block GLP-1/GIP degradation → modestly increase endogenous incretin levels; CV-neutral; well tolerated; lower HbA1c-lowering than GLP-1 agonists
- **TZDs (pioglitazone):** PPARγ agonist → insulin sensitization; reduces CV events in insulin-resistant patients (PROactive); weight gain, heart failure risk limits use
- **Sulfonylureas (glipizide, glyburide):** Stimulate insulin secretion (close K_ATP channels); low cost but hypoglycemia risk, weight gain, lose efficacy as β-cells fail
- **Basal insulin (glargine, detemir, degludec):** When oral/non-insulin injectable agents insufficient; added at bedtime; titrate to fasting glucose <130 mg/dL

## Connections

- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — T2DM is fundamentally a disease of insulin signaling failure; peripheral insulin resistance (IRS-1 Ser307 phosphorylation) prevents glucose uptake; progressive β-cell burnout reduces insulin secretion; both arms must be addressed therapeutically.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — metformin activates AMPK via Complex I inhibition → suppresses hepatic gluconeogenesis and activates GLUT4; AMPK activity is impaired in insulin-resistant states; AMPK is a major target for T2DM drug development.
- `connects-to` → **[CKD](../ckd/README.md)** — diabetes is the leading cause of CKD globally; hyperglycemia drives diabetic nephropathy; SGLT2 inhibitors provide renoprotection beyond glycemic control.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — T2DM and hypertension co-occur in >70% of patients through shared insulin resistance and RAAS activation; combined hyperglycemia and hypertension accelerate CVD, retinopathy, and nephropathy.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — GLP-1R agonists (semaglutide, liraglutide, dulaglutide) reduce HbA1c 1-1.5% and weight 5-15%; glucose-dependent insulin secretion avoids hypoglycemia; SUSTAIN-6 (semaglutide) and LEADER (liraglutide) showed CV risk reduction in T2D with established cardiovascular disease.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — EMPA-REG OUTCOME (empagliflozin, T2D + CVD): 14% MACE reduction, 35% CV death reduction, 35% HHF reduction; SGLT2 inhibitors reduce HbA1c ~0.7-1.0% with glucose-dependent mechanism avoiding hypoglycemia; first-line therapy in T2D with established ASCVD or heart failure.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — Hyperglycemia → excess AGE formation → RAGE on endothelium and macrophages → NF-κB → VCAM-1, ICAM-1, MCP-1 → diabetic micro- and macroangiopathy; soluble RAGE (sRAGE, a decoy) is inversely associated with T2D complications; RAGE also mediates AGE-driven β-cell dysfunction.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — GH is counter-regulatory: raises plasma glucose via hepatic output and peripheral insulin resistance (GHR/STAT5 → IRS-1 serine phosphorylation); acromegaly causes T2DM in 25-40% of cases; exogenous GH raises insulin requirements; declining GH/IGF-1 with aging contributes to metabolic inflexibility.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — MTNR1B rs10830963 impairs beta-cell MT2 inhibition of insulin → elevated fasting glucose → T2DM risk; melatonin suppresses nocturnal insulin secretion; high-dose melatonin reduces insulin sensitivity in susceptible individuals; MT2 agonists under investigation for T2DM.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — leptin resistance in obesity links to T2DM: SOCS3 impairs IRS-1 → convergent blunting of leptin and insulin signalling; hyperleptinemia independently predicts T2DM onset; metformin reduces leptin; bariatric surgery lowers leptin and improves insulin sensitivity.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — T2DM elevates sclerostin via AGE accumulation in the osteocyte lacuno-canalicular network; sclerostin-mediated osteoblast suppression impairs bone quality despite normal BMD, leading to higher fracture risk at any given BMD; a mechanistic link between hyperglycemia and diabetic bone fragility.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Obese adipocyte CCL2 → CCR2+ monocyte recruitment → adipose tissue macrophage (ATM) infiltration → M1 polarization → TNF-α + IL-6 → hepatic and skeletal muscle insulin resistance; crown-like structures (ATM clusters around dead adipocytes) predict T2DM independently of BMI.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity is the dominant driver of type 2 diabetes: excess, dysfunctional adipose tissue releases free fatty acids and inflammatory cytokines causing insulin resistance, overworking β-cells until they fail—so weight loss can prevent or even remit T2DM.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Type 2 diabetes powerfully accelerates atherosclerosis: hyperglycemia, dyslipidemia and insulin resistance injure the endothelium and inflame plaques, so cardiovascular disease is the leading cause of death in diabetics—driving aggressive risk-factor control.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — The adipocyte sits at the heart of type 2 diabetes: enlarged, stressed fat cells become insulin-resistant and secrete adipokines and free fatty acids that spread resistance to muscle and liver—adipose tissue as an endocrine driver, not just a fat store.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Type 2 diabetes is a bihormonal disease, not just insulin failure: alpha cells oversecrete glucagon while beta cells under-secrete insulin, so unchecked glucagon drives hepatic glucose output—why GLP-1 and amylin-based drugs that suppress glucagon help control it.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Type 2 diabetes ends in pancreatic beta-cell failure: insulin resistance first forces beta cells to overwork, but they progressively exhaust and die, so the pancreas's declining insulin output—not just resistance—drives the need for insulin therapy over time.
- `connects-to` → **[Stroke](../stroke/README.md)** — Type 2 diabetes roughly doubles stroke risk: chronic hyperglycemia accelerates atherosclerosis and small-vessel disease while high glucose worsens stroke outcome, so glycemic and vascular risk-factor control is central to preventing the cerebrovascular toll of diabetes.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Type 2 diabetes is a leading cause of blindness via retinopathy: chronic hyperglycemia damages retinal microvessels, causing leakage, ischemia, and neovascularization—so annual retinal screening and tight glucose and blood-pressure control protect vision.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Diabetic peripheral neuropathy is among type 2 diabetes' most common complications: hyperglycemia and microvascular injury damage long nerves, causing stocking-glove numbness and pain that underlie foot ulcers and amputations—so foot care is central to management.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Type 2 diabetes and the liver are tightly linked through fatty liver disease: insulin resistance drives hepatic fat accumulation (MASLD/MASH), which worsens glucose control and can progress to cirrhosis—so the diabetic liver is both cause and casualty of the disease.
- `connects-to` → **[Diabetic Retinopathy](../diabetic-retinopathy/README.md)** — Type 2 diabetes is the leading cause of diabetic retinopathy: chronic hyperglycemia damages retinal microvessels, causing the leading preventable blindness in working-age adults—so glucose and blood-pressure control plus eye screening protect vision.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Type 2 diabetes drives heart failure independently: hyperglycemia and insulin resistance stiffen and weaken the myocardium (diabetic cardiomyopathy), and SGLT2 inhibitors—first diabetes drugs—now treat heart failure even in non-diabetics.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Type 2 diabetes is fueled by adipose inflammation via TNF-alpha: enlarged fat tissue releases TNF-alpha and other cytokines that impair insulin signaling, linking obesity's chronic low-grade inflammation directly to insulin resistance.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium deficiency feeds type 2 diabetes: low magnesium worsens insulin resistance and is common in poorly controlled diabetes (and worsened by it), so correcting it modestly improves glucose control—a two-way street between the mineral and the disease.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome shapes type 2 diabetes: dysbiosis fuels low-grade inflammation and insulin resistance, and metformin partly works by reshaping gut bacteria—so what lives in the intestine influences blood sugar.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol drives the diabetes of stress and steroids: the hormone raises blood glucose by spurring the liver and blunting insulin, so chronic stress, Cushing's, and steroid therapy can unmask or worsen type 2 diabetes.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Insulin is packaged with zinc: beta cells store the hormone as zinc-coordinated crystals, and the zinc transporter ZnT8 is both a diabetes-risk gene and an autoantibody target, tying trace-metal handling to the disease.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Type 2 diabetes is the leading cause of kidney failure: years of high glucose scar the glomeruli (diabetic nephropathy), so protecting the kidney with SGLT2 inhibitors and blood-pressure control is central to long-term care.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages link fat to insulin resistance in type 2 diabetes: inflamed adipose tissue recruits macrophages whose cytokines blunt insulin signaling, so this immune-metabolic crosstalk helps turn obesity into diabetes.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Type 2 diabetes is at its core a cardiovascular disease: it doubles the risk of heart attack and heart failure, which remain the leading cause of death, so modern care prizes drugs that protect the heart, not just lower glucose.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — High glucose injures the endothelial cells lining blood vessels: this endothelial dysfunction is the shared root of diabetes's micro- and macrovascular complications, from retinopathy and nephropathy to accelerated atherosclerosis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Insulin drives potassium into cells, so diabetes is also a potassium story: emergencies like ketoacidosis hide a whole-body deficit, and giving insulin can crash serum potassium dangerously low unless it is replaced.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The red cell keeps diabetes's three-month diary: glucose sticks irreversibly to hemoglobin over the erythrocyte's lifespan, so the HbA1c reflects average blood sugar and has become the central test for diagnosing and tracking the disease.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Diabetes is written on the skin: the velvety darkening of acanthosis nigricans flags the insulin resistance, while poor circulation and nerve loss turn minor foot wounds into the slow-healing ulcers that threaten amputation.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons screen for diabetes's silent damage: retinal photography and OCT catch the eye disease before vision is lost, the workhorse imaging of the annual checks that protect organs the high sugar attacks unnoticed.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Diabetes leaves its mark on hemoglobin: glucose sticks irreversibly to the protein, and the fraction so glycated — HbA1c — averages three months of blood sugar, becoming the single number that diagnoses diabetes and steers its treatment.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — The microvascular damage shows under the electron microscope: chronic high sugar thickens the capillary basement membranes throughout the body, the ultrastructural change underlying the kidney, eye, and nerve damage of diabetes.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Diabetes unsettles the bowel: autonomic neuropathy and altered gut microbiome disturb colonic motility, producing the alternating constipation and diabetic diarrhea that trouble many with long-standing disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Sugar slowly poisons the nerves: chronic hyperglycemia injures the longest neurons first, dying back from the toes in the stocking-glove numbness, burning pain, and lost sensation of diabetic peripheral neuropathy.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — What's absent helps define it: type 2 diabetes is not autoimmune, so the islet autoantibodies of type 1 are missing, and finding GAD antibodies in an adult labeled type 2 instead reveals latent autoimmune diabetes (LADA).
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Diabetes cripples repair: poor circulation, neuropathy, and high glucose stalling immune cells turn minor foot injuries into chronic non-healing ulcers, the leading path to the amputations that shadow the disease.
- `connects-to` → **[NASH](../nash/README.md)** — Diabetes and fatty liver feed each other: insulin resistance drives fat into the liver, and the resulting NASH worsens glucose control while progressing toward cirrhosis — a metabolic pairing that GLP-1 and related drugs now target together.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — High sugar shears the kidney's filter cells: chronic hyperglycemia and glomerular hyperfiltration injure the podocytes, and as these hard-to-replace cells detach, albumin leaks into the urine — the first sign of diabetic kidney disease.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Diabetes reaches reproductive health: vascular and nerve damage cause erectile dysfunction in men, insulin resistance underlies the PCOS often preceding it in women, and poorly controlled glucose in pregnancy harms the fetus.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — The liver pumps out sugar it shouldn't: insulin-resistant hepatocytes keep running gluconeogenesis even when glucose is already high, so excess hepatic glucose output drives the fasting hyperglycemia that metformin works to restrain.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation links fat to insulin resistance: IL-6 and other cytokines released by enlarged, stressed adipose tissue interfere with insulin signaling in muscle and liver, part of the low-grade inflammation that ties obesity to type 2 diabetes.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — It reaches the aging brain: insulin resistance and chronic hyperglycemia raise the risk of dementia, including Alzheimer's, so strongly that the disease is sometimes called 'type 3 diabetes' for the brain's own faltering insulin signaling.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is the inflammatory hub of insulin resistance: free fatty acids and cytokines activate NF-κB in liver, fat and muscle, blunting insulin signaling — the mechanism behind the chronic low-grade inflammation that drives type 2 diabetes.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — High sugar tips the blood toward clotting: type 2 diabetes raises fibrinogen and platelet reactivity and impairs fibrinolysis, contributing to a prothrombotic state that modestly increases deep-vein thrombosis and pulmonary embolism risk.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — It blunts defenses and worsens infection: hyperglycemia impairs neutrophil function and wound healing, making people with diabetes more prone to severe infections and to sepsis when those infections take hold.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — The link runs both ways: long-standing type 2 diabetes modestly raises pancreatic cancer risk, while new-onset diabetes in an older adult can be the first sign of an occult pancreatic tumor destroying islet function.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Sugar feeds the yeast: glucose-rich tissues and impaired immunity in diabetes favor Candida overgrowth, causing the recurrent vulvovaginal, oral and skin-fold candidiasis that often flags poor glycemic control.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — It is a major global TB risk factor: diabetes roughly triples the risk of progressing to active tuberculosis and worsens its outcomes, a converging epidemic as type 2 diabetes spreads through TB-endemic regions.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Diabetes and depression feed each other: living with the disease and its complications raises depression risk, and depression in turn worsens glycemic control and self-care, a well-documented bidirectional loop.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — It weakens bone quality despite normal density: type 2 diabetes raises fracture risk through poor bone quality and falls, and the thiazolidinediones used to treat it accelerate bone loss.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — High glucose blunts the defenses against mold: the impaired neutrophil function and immune dysregulation of poorly controlled diabetes raise susceptibility to invasive fungal infection, including pulmonary aspergillosis.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Chronic hyperglycaemia damages the nerves: distal symmetric diabetic polyneuropathy is among the commonest causes of neuropathic pain, with burning feet, numbness and the risk of unfelt foot injury.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Autonomic neuropathy slows the gut: long-standing type 2 diabetes can cause gastroparesis with nausea, bloating and erratic glucose control, plus diabetic diarrhoea and constipation from enteric nerve damage.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A demanding chronic disease breeds worry: the relentless self-management, fear of hypoglycaemia and dread of complications in type 2 diabetes generate diabetes distress and chronic anxiety alongside depression.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is the archetypal endocrine disorder: insulin resistance with progressive beta-cell failure dysregulates the body's central metabolic hormone, deranging glucose, lipid and counter-regulatory hormone signalling throughout the system.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It marks the skin in many ways: acanthosis nigricans signals insulin resistance, while diabetic dermopathy, necrobiosis lipoidica and neuropathic-ischaemic foot ulcers track the vascular and nerve damage of type 2 diabetes.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Hyperglycaemia blunts host defence: high glucose impairs neutrophil function and complement, so type 2 diabetes raises susceptibility to skin, urinary, foot and respiratory infections and worsens their severity.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It is a cardiovascular risk-equivalent: type 2 diabetes drives a specific diabetic cardiomyopathy and, through autonomic neuropathy, can cause silent myocardial infarction.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It damages nerves widely: diabetic peripheral and autonomic neuropathy cause foot ulcers, gastroparesis and postural hypotension, and the disease accelerates cognitive decline.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It stiffens hands and joints: type 2 diabetes causes diabetic cheiroarthropathy, frozen shoulder, Dupuytren's contracture and Charcot neuroarthropathy of the foot.
- `connects-to` → **[Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — First-line lowers the glucose: metformin reduces hepatic glucose output and improves insulin sensitivity, the foundation drug for type 2 diabetes with cardiovascular benefit.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It is the leading cause of kidney failure: diabetic nephropathy from chronic hyperglycaemia damages the glomeruli, the commonest cause of end-stage renal disease worldwide.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It shadows the lungs: type 2 diabetes is strongly associated with obstructive sleep apnoea and raises the risk of pneumonia and tuberculosis through impaired immunity.
- `connects-to` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — A cardiovascular risk equivalent: type 2 diabetes accelerates atherosclerosis so much that most patients over 40 are offered a statin for primary prevention, lipid-lowering being as central to outcomes as glucose control.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — It scars the filtering unit: chronic hyperglycaemia thickens the glomerular basement membrane and expands the mesangium, producing the Kimmelstiel-Wilson nodules and hyperfiltration that precede the proteinuria of diabetic nephropathy.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Two diseases, one hyperglycaemia: type 2 diabetes arises from insulin resistance with relative insulin deficiency, whereas type 1 is autoimmune destruction of beta cells causing absolute deficiency — distinct causes converging on high glucose and shared complications.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — The beta cell finally fails: type 2 diabetes begins with insulin resistance but progresses as the islets of Langerhans exhaust and lose beta cells—with islet amyloid (IAPP) deposition—so insulin output falls and hyperglycaemia worsens.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It hardens the arteries: type 2 diabetes accelerates atherosclerosis and stiffens the arterial wall through hyperglycaemia, AGEs and dyslipidaemia, making macrovascular disease—heart attack and stroke—the leading cause of diabetic death.
- `connects-to` → **[Gout](../gout/README.md)** — Insulin resistance raises urate: type 2 diabetes and gout cluster within the metabolic syndrome, as hyperinsulinaemia reduces renal uric-acid excretion and shared obesity drives both.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Insulin and oestrogen drive it: type 2 diabetes and its obesity raise endometrial cancer risk markedly, as hyperinsulinaemia and adipose-derived oestrogen both stimulate endometrial proliferation.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Diabetic cardiomyopathy: glucotoxicity and AGE deposition stiffen the myocardium and cause heart failure with preserved ejection fraction, independent of coronary disease or hypertension.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — The diabetic bone paradox: despite normal or high bone density, type 2 diabetes degrades cortical bone microarchitecture and collagen through AGE cross-linking, paradoxically raising fracture risk.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A two-way danger: type 2 diabetes is a leading risk factor for severe COVID-19 and death, and SARS-CoV-2 can in turn trigger new-onset diabetes and severe hyperglycaemic crises.
- `connects-to` → **[HCC](../hcc/README.md)** — From fatty liver to cancer: type 2 diabetes and its associated NASH markedly raise the risk of hepatocellular carcinoma, now a leading cause of liver cancer in high-income countries even without cirrhosis.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Hyperinsulinaemia and the colon: type 2 diabetes raises colorectal cancer risk and worsens its outcomes through insulin/IGF-1 signalling, while metformin appears to reduce that risk.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Insulin-sensitising adipokine: adiponectin falls as adipose tissue expands, and its decline drives the insulin resistance underlying type 2 diabetes.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Pro-resistance adipokine: resistin from adipose tissue and macrophages promotes insulin resistance and chronic inflammation, contributing to type 2 diabetes.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vascular complications: endothelin-1-driven vasoconstriction and endothelial dysfunction mediate much of the micro- and macrovascular damage of type 2 diabetes.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Islet inflammation: islet amyloid and glucotoxicity activate IL-1β, which damages beta cells—the rationale for IL-1 blockade trials in type 2 diabetes.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Metabolic inflammasome: the NLRP3 inflammasome, activated by excess glucose, lipids and islet amyloid, matures the IL-1β that drives the beta-cell dysfunction of type 2 diabetes.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Adipose hypoxia: as fat mass expands beyond its blood supply, HIF-1α stabilised in hypoxic adipose tissue drives the inflammation underlying insulin resistance in type 2 diabetes.
- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — Insulin normally inactivates FOXO1 to switch off gluconeogenesis, so the insulin resistance of type 2 diabetes leaves FOXO1 active in the liver—driving the inappropriate fasting glucose output behind the morning hyperglycemia that metformin targets.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 secreted by adipose-tissue macrophages binds the insulin receptor and impairs its signaling—a direct molecular link between the chronic low-grade inflammation of obesity and the systemic insulin resistance that defines type 2 diabetes.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Hyperglycemia and insulin resistance reduce endothelial nitric-oxide bioavailability, the early vascular lesion that underlies both the macrovascular (coronary, stroke) and microvascular (retinopathy, nephropathy) complications of type 2 diabetes.
- `connects-to` → **[Insulin receptor](../../03-molecular/insulin-receptor/README.md)** — In type 2 diabetes the insulin receptor and its downstream IRS-PI3K-AKT cascade respond poorly to insulin, the molecular signaling defect of insulin resistance that forces compensatory hyperinsulinemia until β-cells fail.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Chronic hyperglycemia drives retinal ischemia and VEGF release, fueling the pathological neovascularization of proliferative diabetic retinopathy—the leading cause of working-age blindness and the target of intravitreal anti-VEGF therapy.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — High glucose induces TGF-β in the glomerulus, driving the mesangial-matrix expansion and basement-membrane thickening that produce diabetic kidney disease, the commonest cause of end-stage renal failure.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Insulin signals through the insulin-receptor-PI3K-AKT axis (insulin-receptor and FOXO1 already mapped) to drive glucose uptake and suppress hepatic gluconeogenesis, and impaired AKT signaling is the molecular heart of insulin resistance.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Chronic nutrient excess activates mTORC1-S6K, which feeds back to inhibit insulin-receptor-substrate signaling, a mechanism coupling overnutrition and obesity to the insulin resistance of type 2 diabetes.
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — The atherogenic dyslipidemia of type 2 diabetes amplifies cardiovascular risk, and PCSK9 (which raises LDL) is targeted alongside the statins already mapped to lower that risk in these high-risk patients.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — The insulin receptor (mapped) signals through IRS to PI3K and AKT (mapped); blunting of this PI3K branch is the molecular core of insulin resistance in type 2 diabetes.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — Insulin-activated AKT (mapped) inhibits GSK-3β to switch on glycogen synthase; elevated GSK-3β activity in type 2 diabetes impairs glycogen storage and insulin signaling.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — While the PI3K metabolic arm is blunted, insulin's MAPK-ERK mitogenic arm remains active in type 2 diabetes, a selectivity that drives the vascular and proliferative complications.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of saturated free fatty acids drives the lipotoxic metabolic inflammation that links obesity to the insulin resistance of type 2 diabetes.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB signaling (NF-κB and NLRP3 already mapped) transduces nutrient-excess and lipotoxic signals into the chronic metabolic inflammation underlying type 2 diabetes.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant defense counters the glucotoxic oxidative stress that damages β-cells and impairs insulin signaling in type 2 diabetes.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Pro-inflammatory IL-6-STAT3 signaling in adipose tissue and liver contributes to the chronic low-grade inflammation that drives insulin resistance in type 2 diabetes.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Mitochondrial and metabolic stress releases cytosolic DNA that engages cGAS-STING, fueling the metabolic inflammation of adipose tissue in type 2 diabetes.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the islet and renal fibrosis that accompanies β-cell failure and diabetic nephropathy in type 2 diabetes.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2 signaling downstream of IL-6 and other cytokines (IL-6 mapped) propagates the inflammatory insulin resistance of adipose and liver in type 2 diabetes.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling contributes to islet inflammation and β-cell stress in the metabolic-immune milieu of type 2 diabetes.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Calprotectin (S100A8/A9) released by myeloid cells amplifies the chronic low-grade adipose-tissue inflammation that drives insulin resistance in type 2 diabetes.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors (distinct from FOXO1 already mapped) integrate insulin-PI3K-AKT signaling to regulate hepatic gluconeogenesis and β-cell stress responses in type 2 diabetes.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the inflammatory insulin-resistance signaling of adipose and hepatic tissue in type 2 diabetes.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic CD8 T cells contribute to the adipose-tissue immune activation that drives insulin resistance in type 2 diabetes.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the pancreatic β-cell survival and insulin-target-tissue homeostasis whose failure contributes to type 2 diabetes.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic (metabolic-memory) programming of type 2 diabetes.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven chemokine signaling recruits macrophages into adipose tissue, amplifying the inflammation that drives insulin resistance in type 2 diabetes.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the islet-cell and immune-cell interactions of type 2 diabetes.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 and the complement system participate in the metabolic inflammation and insulin resistance of type 2 diabetes.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A-p16 senescence signaling (a genome-wide-association-study locus for type 2 diabetes) participates in the β-cell senescence and dysfunction of type 2 diabetes.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the adipose-tissue immune regulation and metaflammation of type 2 diabetes.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the chronic inflammation of type 2 diabetes.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the metabolic gene programs relevant to type 2 diabetes.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Beta-cell secretion: after glucose closes the KATP channel and depolarises the beta cell, calcium influx triggers the exocytosis of insulin granules, the final step of secretion whose progressive failure underlies the beta-cell dysfunction of type 2 diabetes.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Male hypogonadism: low testosterone is bidirectionally linked with type 2 diabetes in men, as visceral adiposity and insulin resistance suppress testosterone while the resulting hypogonadism further worsens metabolic control and body composition.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Hyperuricaemia and oxidative stress: xanthine oxidase generates uric acid and reactive oxygen species, and the hyperuricaemia clustering with metabolic syndrome contributes to the insulin resistance and endothelial dysfunction of type 2 diabetes.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Silent myocardial infarction: type 2 diabetes accelerates coronary disease (atherosclerosis already mapped) and blunts anginal warning through autonomic neuropathy, so myocardial infarction is often silent, and troponin marks the cardiac injury when it occurs.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Neuropathic pain: painful diabetic peripheral neuropathy (peripheral nerve already mapped) is a major burden, and when other agents fail it is treated with opioids acting at the mu-opioid receptor, at the cost of dependence risk.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopaminergic glucose control: central dopaminergic tone influences glucose metabolism, and the dopamine agonist bromocriptine, given as a morning quick-release formulation, is an approved glucose-lowering therapy for type 2 diabetes.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Atherogenic dyslipidaemia: type 2 diabetes shifts cholesterol handling toward high triglycerides, low HDL and small dense LDL (PCSK9 already mapped), the dyslipidaemia driving much of its accelerated cardiovascular risk.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory balance: the anti-inflammatory IL-10 counters the chronic low-grade inflammation (TNF, IL-6 and IL-1 already mapped) of adipose tissue in type 2 diabetes, and the imbalance contributes to the insulin resistance.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Cardiorenal RAAS: aldosterone drives the fibrosis and inflammation of diabetic kidney disease (angiotensin and endothelin already mapped), and mineralocorticoid-receptor antagonists such as finerenone slow the progression of diabetic nephropathy.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — SGLT2 and cardiorenal benefit: the SGLT2 inhibitors (SGLT2 already mapped) block renal sodium-glucose cotransport, and the resulting natriuresis and tubuloglomerular feedback underlie the cardiovascular and renal protection they confer in type 2 diabetes.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Adipose M2 macrophages: IL-4 sustains the anti-inflammatory M2 macrophages of healthy adipose tissue (IL-10 already mapped), and the shift away from this state toward pro-inflammatory macrophages (TNF already mapped) drives the insulin resistance of type 2 diabetes.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Peripheral metabolic serotonin: gut-derived peripheral serotonin regulates pancreatic β-cell mass and adipose and hepatic metabolism, part of the neuroendocrine control of the energy balance disturbed in type 2 diabetes.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Adipose M2 maintenance: IL-13, with IL-4 (already mapped), sustains the anti-inflammatory M2 macrophages of healthy adipose tissue, and the loss of this type-2 signalling drives the inflammation and insulin resistance of type 2 diabetes.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Insulin secretion trigger: the calcium influx into the β-cell triggers the exocytosis of the insulin (already mapped) granules, the calcium signalling of the glucose-stimulated insulin secretion that fails in type 2 diabetes.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — KATP channel: the ATP-sensitive potassium channel of the β-cell closes on glucose rise to depolarise the cell and trigger insulin (already mapped) release, the target of the sulfonylureas used in type 2 diabetes.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron and insulin resistance: hepcidin, the iron-regulatory hormone; the iron overload (the ferritin, an IL-6-driven already-mapped marker) is associated with the insulin (already mapped) resistance of type 2 diabetes.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenoprotein-P hepatokine: selenium's selenoprotein-P (SELENOP), secreted by the liver (already mapped), acts as a hepatokine that impairs the insulin (already mapped) signalling, linking the selenium status to type 2 diabetes.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Central energy control: the brain's hypothalamic appetite and energy regulation (leptin, ghrelin and insulin already mapped) is central to type 2 diabetes, which also raises the risk of vascular dementia and cognitive decline.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the chronic metabolic inflammation (IL-6 and TNF already mapped) of the insulin resistance of type 2 diabetes.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate metabolic inflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the metabolic stress, contributes to the chronic low-grade inflammation (IL-6 and TNF already mapped) of the insulin resistance of type 2 diabetes.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Adipose Th1 inflammation: the IFN-γ of the adipose-tissue T cells (with the macrophages already mapped) drives the Th1 inflammation that promotes the insulin (already mapped) resistance of type 2 diabetes.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm whose loss (the reduced adipose eosinophils/ILC2s) permits the pro-inflammatory insulin resistance of type 2 diabetes.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic low-grade inflammation of the insulin resistance of type 2 diabetes.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the adipose immune milieu of type 2 diabetes.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Adipose CD4 arm: the CD4 T-helper cells shift toward the Th1/Th17 (IFN-γ and IL-17 already mapped) phenotype in the inflamed adipose tissue, driving the insulin resistance of type 2 diabetes.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adipose CD8 initiator: the CD8 T cells (perforin already mapped) infiltrate the adipose tissue early and recruit and activate the macrophages (already mapped) that drive the insulin resistance of type 2 diabetes.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Adipose mast cells: the mast cells accumulate in the inflamed adipose tissue and contribute to the chronic low-grade inflammation and the insulin resistance of type 2 diabetes.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Adipose B cells: the B cells accumulate in the inflamed adipose tissue and, through pathogenic antibodies and cytokines, promote the insulin resistance of type 2 diabetes.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Adipose antigen presentation: the dendritic cells of the inflamed adipose tissue present antigen to the T cells (already mapped) and sustain the chronic low-grade inflammation of type 2 diabetes.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the macrophage (already mapped) recruitment into the inflamed adipose tissue of type 2 diabetes.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Adipose alarmin: TSLP released from the hypertrophic adipocytes (already mapped) and the inflamed adipose tissue of type 2 diabetes activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the chronic low-grade inflammation.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-kallikrein axis: bradykinin, generated by tissue kallikrein activation in the insulin-resistant adipose and skeletal-muscle tissue of type 2 diabetes, potentiates insulin signalling through its B2R receptor and modulates vascular tone in the diabetic vasculopathy.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-insulin crosstalk: erythropoietin, via the JAK-STAT (already mapped) and PI3K-AKT (already mapped) pathways, modulates insulin sensitivity and β-cell survival, and EPO deficiency contributes to the anaemia of the CKD (already mapped) complication of type 2 diabetes.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Contact-complement regulation: C1-esterase inhibitor restrains the classical complement C1 (with C3/C5aR1 already mapped) and the kallikrein-kinin system (bradykinin already mapped) activated in the inflamed adipose tissue and vasculopathy of type 2 diabetes.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Adipose mast-cell effector: histamine released by mast cells (already mapped) in the inflamed adipose tissue of T2D amplifies insulin resistance through H1R on adipocytes, driving the vicious cycle of adipose inflammation and metabolic dysfunction.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Adipose fibrosis scaffold: periostin, downstream of TGF-β (already mapped) signalling in the inflamed adipose tissue, promotes the peri-adipocyte fibrosis that impairs adipose expandability and worsens insulin resistance in type 2 diabetes.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — T2D prolactin: prolactin acts as a pancreatic (already mapped) beta-cell survival factor; gestational hyperprolactinaemia promotes beta-cell mass expansion, while elevated prolactin in T2D amplifies insulin resistance and worsens the metabolic dysfunction.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — T2D oxytocin: oxytocin receptors on pancreatic (already mapped) beta-cells modulate insulin (already mapped) secretion in type 2 diabetes; intranasal oxytocin reduces food intake and adiponectin/leptin (already mapped) adipose inflammation, worsening insulin resistance.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — T2D vasopressin: vasopressin (ADH) drives hepatic (already mapped) glucose production via V1b receptor on pancreatic (already mapped) alpha-cells; elevated copeptin predicts T2D risk, and AVP-driven osmotic signalling amplifies the AMPK (already mapped) pathway dysfunction.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — T2D iodine: iodine-dependent thyroid hormones regulate insulin (already mapped) sensitivity and AMPK (already mapped) signalling in type 2 diabetes; hypothyroidism worsens hepatic (already mapped) glucose output and NF-κB (already mapped)-driven adipose inflammation in T2D.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — T2D copper: copper-dependent superoxide dismutase (SOD) combats oxidative stress driving NF-κB (already mapped)-mediated beta-cell (already mapped) damage and insulin (already mapped) resistance in type 2 diabetes; copper dysregulation worsens T2D vascular complications.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — T2D phosphorus: phosphorus is essential for ATP-mediated insulin (already mapped) signalling and AMPK (already mapped) activation in T2D; hyperphosphaturia accelerates CKD (already mapped) progression and FGF-23/phosphate dysregulation amplifies cardiovascular risk in diabetes.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — T2D iron: iron overload promotes hepatocyte (already mapped) and macrophage (already mapped) oxidative stress; iron-induced NF-κB (already mapped) and IL-6 (already mapped) amplify adipocyte (already mapped) inflammation and insulin (already mapped) resistance cascade of T2D.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — T2D chloride: chloride, via CFTR in pancreatic and hepatocyte (already mapped) cells, regulates insulin (already mapped) secretion; chloride dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of type 2 diabetes.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — T2D sulfur: glutathione buffers oxidative stress from NF-κB (already mapped) and AMPK (already mapped) in macrophages (already mapped) and hepatocytes (already mapped); hyperhomocysteinaemia amplifies insulin (already mapped) resistance and IL-6 (already mapped) cascade of T2D.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — T2D nitrogen: nitric oxide from eNOS in endothelial-cell (already mapped) and macrophages (already mapped) preserves insulin (already mapped) sensitivity; nitrogen deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) vascular insulin resistance of T2D.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — T2D oxygen: mitochondrial oxygen consumption in hepatocytes (already mapped) and adipocytes (already mapped) drives ATP for insulin (already mapped) signalling; hypoxia amplifies NF-κB (already mapped) and IL-6 (already mapped) adipose inflammation and insulin resistance of T2D.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — T2D carbon: CO2 in bicarbonate buffering of hepatocytes (already mapped) and macrophages (already mapped) regulates pH for insulin (already mapped) secretion; carbon-metabolite excess amplifies NF-κB (already mapped) and AMPK (already mapped) insulin resistance of T2D.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — T2D PD-1: PD-1 on macrophages (already mapped) and T-helper-cell (already mapped) modulates adipose immune homeostasis; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and GLP-1 (already mapped) resistance cascade of T2D.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — T2D angiotensin-II: angiotensin-II in hepatocytes (already mapped) and adipocytes (already mapped) promotes insulin resistance via RAAS; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of T2D.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — T2D Wnt/β-catenin: Wnt signalling in hepatocytes (already mapped) and adipocytes (already mapped) regulates glucose metabolism; Wnt dysregulation amplifies NF-κB (already mapped) and AMPK (already mapped) and GLP-1 (already mapped) resistance cascade of T2D.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — T2D hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and adipocytes (already mapped), quenches metabolic ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and insulin (already mapped) cascade of type 2 diabetes.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — T2D RANKL: RANKL signalling in macrophages (already mapped) and adipocytes (already mapped) modulates metabolic bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and insulin (already mapped) cascade of type 2 diabetes.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T2D IL-2: IL-2 signalling in T-cells (already mapped) and macrophages (already mapped) modulates immune tolerance; IL-2 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and insulin (already mapped) cascade of type 2 diabetes.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — T2D Fibronectin: Fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds adipose ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — T2D NOTCH: NOTCH on hepatocytes (already mapped) and macrophages (already mapped) regulates adipose metabolic tone; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — T2D IGF-1: IGF-1 from hepatocytes (already mapped) and macrophages (already mapped) promotes insulin sensitivity; IGF-1 loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — T2D activin-a: activin-A from hepatocytes (already mapped) and macrophages (already mapped) regulates adipose immune-fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — T2D cgrp: CGRP from hepatocytes (already mapped) and macrophages (already mapped) modulates adipose neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — T2D calcitonin: calcitonin from hepatocytes (already mapped) and macrophages (already mapped) modulates adipose calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — T2D substance-p: substance-P from hepatocytes (already mapped) and macrophages (already mapped) modulates adipose neuroimmune tone; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of type 2 diabetes.
- `connects-to` → **[Androgen-Receptor](../../03-molecular/androgen-receptor/README.md)** — T2D androgen-receptor: androgen receptor on hepatocytes (already mapped) and macrophages (already mapped) modulates T2D hormonal metabolism; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of T2D.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — T2D norepinephrine: norepinephrine from macrophages (already mapped) and hepatocytes (already mapped) amplifies T2D sympathoadrenal stress; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) metabolic cascade of T2D.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^defronzo-2009-t2dm]: DeFronzo RA. Banting Lecture. From the triumvirate to the ominous octet: a new paradigm for the treatment of type 2 diabetes mellitus. *Diabetes.* 2009;58(4):773-795. [doi:10.2337/db09-9028](https://doi.org/10.2337/db09-9028) · [PubMed 19336687](https://pubmed.ncbi.nlm.nih.gov/19336687/)
[^zinman-2015-empareg]: Zinman B, Wanner C, Lachin JM, et al. Empagliflozin, Cardiovascular Outcomes, and Mortality in Type 2 Diabetes. *N Engl J Med.* 2015;373(22):2117-2128. [doi:10.1056/NEJMoa1504720](https://doi.org/10.1056/NEJMoa1504720) · [PubMed 26378978](https://pubmed.ncbi.nlm.nih.gov/26378978/)
[^marwick-2018-t2dm-cv]: Marwick TH, Ritchie R, Shaw JE, Kaye D. Implications of Underlying Mechanisms for the Recognition and Management of Diabetic Cardiomyopathy. *J Am Coll Cardiol.* 2018;71(3):339-351. [doi:10.1016/j.jacc.2017.11.019](https://doi.org/10.1016/j.jacc.2017.11.019) · [PubMed 29348028](https://pubmed.ncbi.nlm.nih.gov/29348028/)
