---
schema: human-scale-entry/v1
id: type-1-diabetes
name: Type 1 Diabetes
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Autoimmune destruction of pancreatic beta cells → absolute insulin deficiency; CD8+ and CD4+ Th1 cells target GAD65, IA-2, and insulin antigens. Staged by autoantibody seropositivity; teplizumab (anti-CD3) delays clinical onset; managed with insulin replacement."
aliases: ["T1D", "type 1 diabetes mellitus", "T1DM", "juvenile diabetes", "insulin-dependent diabetes mellitus", "IDDM", "autoimmune diabetes"]
sources:
  - id: atkinson-2014-t1d-lancet
    type: peer-reviewed
    cite: "Atkinson MA, Eisenbarth GS, Michels AW. Type 1 diabetes. Lancet. 2014;383(9911):69-82."
    doi: "10.1016/S0140-6736(13)60591-7"
    pmid: "23890997"
    url: "https://doi.org/10.1016/S0140-6736(13)60591-7"
  - id: herold-2019-teplizumab-t1d
    type: peer-reviewed
    cite: "Herold KC, Bundy BN, Long SA, et al. An anti-CD3 antibody, teplizumab, in relatives at risk for type 1 diabetes. N Engl J Med. 2019;381(7):603-613."
    doi: "10.1056/NEJMoa1905155"
    pmid: "31180675"
    url: "https://doi.org/10.1056/NEJMoa1905155"
  - id: insel-2015-t1d-staging
    type: peer-reviewed
    cite: "Insel RA, Dunne JL, Atkinson MA, et al. Staging presymptomatic type 1 diabetes: a scientific statement of JDRF, the Endocrine Society, and the American Diabetes Association. Diabetes Care. 2015;38(10):1964-1974."
    doi: "10.2337/dc15-1419"
    pmid: "26404926"
    url: "https://doi.org/10.2337/dc15-1419"
cross_links:
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CD8+ CTLs are the primary beta cell destroyers in T1D: autoreactive CTLs recognize HLA-A2-restricted GAD65, IGRP, and insulin peptides → perforin/granzyme and Fas-FasL → beta cell apoptosis; islet CTL infiltration (insulitis) precedes clinical T1D onset by years."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4+ Th1 cells coordinate T1D autoimmunity: HLA-DQ8/DQ2-restricted presentation of beta cell antigens → IFN-gamma, IL-2 → CTL priming and macrophage activation; Treg insufficiency allows unchecked Th1 expansion; teplizumab (anti-CD3) shifts Th1/Treg balance."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Treg insufficiency is a core T1D mechanism: FOXP3+ Tregs normally suppress autoreactive T cells in pancreatic lymph nodes and islets; NOD mice have Treg functional defects; low-dose IL-2 therapy expands Tregs → ongoing clinical trials to delay T1D progression."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells act as APCs for beta cell antigens and produce autoantibodies (anti-GAD65, anti-IA-2, anti-ZnT8, anti-insulin) used for T1D staging (Stage 1: ≥2 Ab, normoglycemia; Stage 2: ≥2 Ab, dysglycemia); rituximab transiently preserves C-peptide in new-onset T1D."
  - target: 01-human/03-molecular/insulin
    relation: treated-by
    note: "T1D results from autoimmune β-cell destruction → absolute insulin deficiency; CD8+ CTLs target GAD65, IGRP, and insulin peptides → apoptosis; lifelong insulin replacement (MDI or pump) is required; DCCT trial showed intensive insulin therapy halves long-term complications."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Type 1 diabetes is an organ-specific autoimmune attack on the insulin-producing beta cells of the pancreatic islets; T-cell insulitis silently destroys ~80% of beta-cell mass before hyperglycemia appears, leaving absolute insulin deficiency while the exocrine pancreas is spared."
  - target: 02-pathogen/01-viruses/coxsackievirus-b
    relation: connects-to
    note: "Enteroviruses, especially Coxsackievirus B, are the leading environmental trigger of type 1 diabetes: CVB infects beta cells via the CAR receptor and its 2C protein shares homology with GAD65, and enteroviral RNA is found in islets at diagnosis — motivating CVB vaccine trials."
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Chronic hyperglycemia from type 1 diabetes drives microvascular complications — virtually all T1D patients develop diabetic retinopathy after 20 years — so the DCCT showed that intensive insulin control cuts retinopathy onset 76%; eye screening starts 5 years after diagnosis."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "T1D and T2D share chronic hyperglycemia and vascular complications but differ in cause: T1D is autoimmune β-cell loss needing insulin, T2D is insulin resistance with relative deficiency; the line blurs with obesity-linked T1D and adult-onset autoimmune diabetes (LADA)."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Type 1 diabetes is strongly HLA-linked: MHC class II alleles HLA-DR3-DQ2 and DR4-DQ8 confer the greatest genetic risk by presenting islet autoantigens (insulin, GAD65) to autoreactive CD4+ T cells, while DQ6 is protective; HLA typing predicts risk in relatives."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Diabetic kidney disease is a leading T1D complication and a top cause of end-stage renal disease: chronic hyperglycemia → glomerular hyperfiltration, mesangial expansion and albuminuria → declining GFR; DCCT/EDIC showed tight glucose control plus RAAS blockade slows progression."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Type 1 diabetes is a leading cause of neuropathic pain through diabetic peripheral neuropathy: decades of hyperglycemia damage distal nerves via polyol, AGE, and microvascular mechanisms, causing burning stocking-glove pain—so early glycemic control is key prevention."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Type 1 diabetes impairs wound healing and underlies the diabetic foot: hyperglycemia, neuropathy (lost protective sensation), and microvascular disease stall healing and breed infection, so foot ulcers in long-standing T1D are a major cause of non-traumatic amputation."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells initiate the autoimmunity of type 1 diabetes: they capture islet antigens and present them to autoreactive T cells in pancreatic lymph nodes, breaking tolerance and launching the cytotoxic attack on β-cells—so DCs are a target for tolerance therapies."
  - target: 01-human/07-system/pemphigus-vulgaris
    relation: connects-to
    note: "Type 1 diabetes and pemphigus vulgaris are both HLA-linked autoimmune diseases: T1DM is T-cell-mediated destruction of pancreatic β-cells, while pemphigus is antibody-mediated against desmoglein in skin—two ends of the autoimmune spectrum that cluster in patients."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Type 1 diabetes and narcolepsy type 1 are both autoimmune diseases that destroy an irreplaceable cell population: T1DM the insulin-producing β-cells, narcolepsy the hypothalamic orexin neurons—each HLA-associated and likely T-cell-mediated, leaving a permanent deficit."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Type 1 diabetes accelerates atherosclerosis, the leading cause of death in T1DM: lifelong hyperglycemia injures the endothelium and worsens lipids, so even well-controlled patients face premature cardiovascular disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Type 1 diabetes is fundamentally an autoimmune disease: a breakdown of self-tolerance lets the immune system destroy insulin-producing beta cells, so it clusters with other autoimmune disorders and is now a target for immune-modulating prevention like teplizumab."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Type 1 diabetes deranges glucagon as well as insulin: as islets are destroyed, alpha cells lose normal glucose-sensing and fail to release glucagon during hypoglycemia, removing a key safety brake—so insulin treatment carries serious risk of severe lows."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Type 1 diabetes is the endocrine system's prototypic insulin-deficiency disease: autoimmune loss of pancreatic islet hormone output disrupts glucose homeostasis and often coexists with autoimmune thyroid and adrenal disease in polyglandular syndromes."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome may shape type 1 diabetes risk: early-life dysbiosis and a leaky gut can skew immune development and are linked to islet autoimmunity, so microbial exposures help explain why T1D incidence is rising faster than genetics alone can."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D is tied to type 1 diabetes risk: it modulates the immune system and regulatory T cells, and low early-life vitamin D status is associated with more islet autoimmunity—so deficiency is a candidate environmental trigger of this autoimmune disease."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Adrenaline is the backup against hypoglycemia in type 1 diabetes: when insulin overshoots, epinephrine should raise glucose and trigger warning symptoms, but in long-standing T1D this response blunts—causing dangerous hypoglycemia unawareness."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Type 1 diabetes travels with thyroid autoimmunity: it clusters in autoimmune polyglandular syndromes with Hashimoto's and Graves' disease, so patients are screened for thyroid antibodies and TSH—one autoimmune endocrine failure predicts another."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Diabetic ketoacidosis is a potassium trap: acidosis masks a severe total-body potassium deficit by shifting K+ out of cells, so giving insulin drives potassium back in and can cause dangerous hypokalemia—why DKA care obsessively tracks potassium."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol is type 1 diabetes's counter-hormone and a fellow autoimmune target: it raises glucose opposing insulin (driving hypoglycemia-rebound), and autoimmune adrenal failure (Addison's) can join T1D in polyglandular syndrome."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Type 1 diabetes attacks a zinc transporter: ZnT8, which loads zinc into insulin granules, is a major autoantigen—anti-ZnT8 antibodies help diagnose it—and zinc is needed to crystallize and store the very insulin the disease destroys."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type 1 diabetes carries a type I interferon signature: viral triggers (like coxsackievirus) and IFN make beta cells display more antigen and self-destruct, so interferon is a bridge from infection to the autoimmune attack on the islets."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Type 1 diabetes begins as insulitis led by macrophages: these innate cells are among the first to invade the islets, presenting beta-cell antigens and secreting toxic mediators that recruit the T cells which finish the destruction."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Type 1 diabetes can flood the blood with hydrogen ions: without insulin the body burns fat into acidic ketones, and the resulting diabetic ketoacidosis drops blood pH into a dangerous acidosis—the classic emergency that often reveals the disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Type 1 diabetes unleashes the liver: lacking insulin's brake, it overproduces glucose and converts incoming fatty acids into the ketone bodies of ketoacidosis, so the liver drives both the high blood sugar and the acid crisis."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Insulin loss in type 1 diabetes sets fat cells loose: unrestrained lipolysis pours free fatty acids out of adipocytes, supplying the liver with the raw material it turns into the ketones that cause ketoacidosis."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Years of high glucose in type 1 diabetes damage peripheral nerves, causing the numb, painful 'stocking-glove' neuropathy that threatens the feet with unnoticed injury and ulcers."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Type 1 diabetes demands regular eye screening: retinal photographs in visible-light photons catch the diabetic retinopathy that years of glucose swings inflict on the retina, before vision is lost."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Type 1 diabetes is a leading cause of kidney failure: decades of high glucose scar the glomeruli into diabetic nephropathy, which urine-protein screening catches early enough to slow."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the islet under attack: beta cells packed with insulin secretory granules sit besieged by infiltrating T cells in insulitis, the autoimmune assault that wipes out the body's only source of insulin."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The red cell keeps the diabetic's long-term score: glucose binds irreversibly to hemoglobin over the erythrocyte's lifespan, so the HbA1c reflects months of average sugar and guides how tightly the insulin is dosed."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Diabetic ketoacidosis is also a sodium crisis: sky-high glucose pulls water into the blood and lowers the measured sodium, while the osmotic diuresis drains salt and water — making careful sodium and fluid replacement central to treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Type 1 diabetes leaves an autoantibody trail: antibodies against GAD65, IA-2, ZnT8, and insulin appear before symptoms, marking the autoimmune attack on the islets and letting at-risk children be identified years ahead."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Control is read off the hemoglobin: glucose glycates the red-cell protein into HbA1c, whose level averages months of blood sugar and guides how tightly the insulin regimen is run to stave off complications."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye is an early casualty: years of high glucose damage the retina's microvessels into diabetic retinopathy, the leading cause of blindness in working-age adults, so regular retinal screening is built into care."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Autoimmunity rarely travels alone: type 1 diabetes clusters with other autoimmune endocrine disease, and Addison's disease — autoimmune destruction of the adrenal gland — joins it in the polyglandular syndromes that demand vigilance."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy demands near-perfect control: high glucose around conception raises congenital malformation and miscarriage risk and later causes macrosomia, so type 1 diabetics tighten their insulin and monitoring before and through pregnancy."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Glucose injures the vessel lining throughout: damaged endothelial cells underlie both the microvascular complications in eye, kidney, and nerve and the accelerated atherosclerosis that makes heart disease the long-term killer in type 1 diabetes."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Type 1 diabetes is partly an IL-2 problem: weak IL-2 signaling starves the regulatory T cells that should restrain islet autoimmunity, so low-dose IL-2 to expand Tregs is a leading strategy to halt beta-cell destruction."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells join the islet assault: they infiltrate the inflamed pancreatic islets and help kill insulin-making beta cells, adding an innate arm to the T-cell-driven autoimmunity of type 1 diabetes."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The gut helps set off islet autoimmunity: a leaky small-bowel barrier and dietary antigens prime the immune system, and the strong overlap with celiac disease ties intestinal immunity to the onset of type 1 diabetes."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Innate inflammation joins the islet attack: NLRP3 inflammasome activation in islet-infiltrating immune cells releases IL-1β that is directly toxic to beta cells, an innate arm layered on the T-cell-driven autoimmunity."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The earliest invaders may be neutrophils: neutrophils and their NETs infiltrate the islets early in the disease, an innate trigger thought to help initiate the autoimmune insulitis before T cells finish the job."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "A dangerous way to control weight: some young people with type 1 diabetes deliberately skip insulin to lose weight ('diabulimia'), a disordered-eating behavior that overlaps anorexia and drives repeated ketoacidosis and early complications."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Cytokines kill the beta cell through NF-κB: IL-1β, TNF and interferon from infiltrating immune cells activate NF-κB inside islet beta cells, driving the stress and apoptosis that destroys insulin production in type 1 diabetes."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Ketoacidosis turns the blood prothrombotic: the dehydration, inflammation and endothelial injury of diabetic ketoacidosis sharply raise clot risk, so venous thromboembolism is a recognized hazard of severe decompensation."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Infection and diabetes feed each other dangerously: hyperglycemia blunts immune defense while infection commonly precipitates ketoacidosis, so serious infection and sepsis are both a trigger and a threat in type 1 diabetes."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Sugar-rich tissue invites the yeast: glucose in blood and urine plus impaired immunity favor Candida overgrowth, so recurrent vulvovaginal, oral and skin-fold candidiasis often flags poor glycemic control."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Decades of high sugar damage the arteries: type 1 diabetes accelerates atherosclerosis from a young age, and the resulting large-vessel disease raises the lifetime risk of ischemic stroke."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "The relentless self-management weighs on mood: the lifelong burden of carbohydrate counting, injections and fear of hypoglycemia gives type 1 diabetes a high rate of depression and diabetes distress."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Decades of glucose injury weaken the heart: type 1 diabetes accelerates coronary disease and causes a diabetic cardiomyopathy through microvascular damage and metabolic stress, routes toward heart failure over a lifetime."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "It builds a more fragile skeleton: insulin's loss removes a bone-anabolic signal, so type 1 diabetes is associated with lower bone mineral density and a markedly elevated fracture risk."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Ketoacidosis and high glucose invite invasive mold: poorly controlled type 1 diabetes, especially in ketoacidosis, impairs neutrophil function and predisposes to invasive fungal infections such as aspergillosis and mucormycosis."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Autoimmunity and neuropathy hit the gut: type 1 diabetes co-occurs with coeliac disease and autoimmune gastritis, and longstanding autonomic neuropathy causes gastroparesis with erratic glucose control."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It marks the skin in characteristic ways: type 1 diabetes causes necrobiosis lipoidica, repeated-injection lipohypertrophy and diabetic dermopathy, and the autoimmune diathesis brings vitiligo."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Relentless self-management and hypo-fear breed worry: the constant glucose monitoring, dosing decisions and dread of hypoglycaemia in type 1 diabetes generate diabetes distress and chronic anxiety."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Glucose extremes endanger the brain: severe hypoglycaemia causes seizures and coma, diabetic ketoacidosis can cause cerebral oedema in children, and long-standing disease brings peripheral and autonomic neuropathy."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It stiffens joints and breaks down the foot: type 1 diabetes causes diabetic cheiroarthropathy with limited joint mobility, frozen shoulder, and Charcot neuroarthropathy that destroys the foot's architecture."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Autonomic nerve damage misruns the heart: cardiac autonomic neuropathy in type 1 diabetes causes resting tachycardia, blunted heart-rate variability and silent myocardial ischaemia that masks heart attacks."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Acidosis drives deep breathing: diabetic ketoacidosis causes the deep, laboured Kussmaul breathing that blows off CO2, and diabetes mildly reduces lung function and raises pneumonia risk."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "It weakens defences against TB: diabetes impairs cell-mediated immunity and roughly triples the risk of active tuberculosis, worsening its course and treatment outcomes."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "It invites skin and foot infection: impaired immunity and peripheral neuropathy predispose type 1 diabetes to staphylococcal skin abscesses and diabetic-foot infections."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Autoimmunity is born in a lymph node: the pancreatic (peri-islet) lymph nodes are where dendritic cells first present beta-cell antigens to autoreactive T cells, making regional lymphatics the cradle of type 1 diabetes."
  - target: 02-pathogen/01-viruses/rotavirus
    relation: connects-to
    note: "A childhood virus under suspicion: enteric infections including rotavirus are studied as triggers of islet autoimmunity through molecular mimicry, and rotavirus vaccination has been linked to lower type 1 diabetes incidence."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Cancer immunotherapy can cause it: PD-1/PD-L1 checkpoint inhibitors trigger a rapid autoimmune type 1 diabetes as an immune-related adverse event, often presenting with abrupt ketoacidosis and low C-peptide."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "It destroys the insulin source: type 1 diabetes is autoimmune T-cell destruction of the insulin-producing beta cells of the pancreatic islets, leaving absolute insulin deficiency once most islet mass is lost."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Immunotherapy can delay onset: the anti-CD3 antibody teplizumab postpones progression to clinical type 1 diabetes in at-risk individuals by blunting the autoreactive T cells, the first disease-modifying therapy for the condition."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "It scars the kidney filter too: like type 2 diabetes, chronic hyperglycaemia in type 1 thickens the glomerular basement membrane and expands the mesangium, causing the diabetic nephropathy that is a major long-term complication."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Macrovascular disease shortens it: type 1 diabetes accelerates atherosclerosis and arterial stiffening, so cardiovascular disease is the leading cause of death in long-standing T1D despite good glucose control."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Its autoantibodies signal the autoimmunity: type 1 diabetes is a T-cell attack on beta cells, but islet autoantibodies (anti-GAD, anti-IA2) made with germinal-centre B-cell help mark the loss of tolerance and predict onset."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "It can be precipitated by infection: COVID-19 and other viral infections are linked to new-onset type 1 diabetes, with viral injury and molecular mimicry implicated in triggering islet autoimmunity in susceptible children."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Shared autoimmune ground: type 1 diabetes and psoriasis cluster together, the two sharing immune-regulatory susceptibility loci that tilt toward autoimmunity across organs."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "A different route to insulin lack: cystic-fibrosis-related diabetes arises from progressive pancreatic destruction, a hybrid of the insulin deficiency of type 1 and resistance—the commonest CF comorbidity in adults."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Diabetic cardiomyopathy from youth: lifelong type 1 diabetes stiffens and scars the myocardium through AGE deposition and microvascular disease, raising heart-failure risk independent of coronary disease."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Fragile bones from diagnosis: unlike type 2 diabetes, type 1 lowers bone density and impairs bone quality from a young age, and Charcot neuroarthropathy destroys the foot's cortical bone in those with neuropathy."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Electrolytes and the heart: diabetic ketoacidosis and its treatment swing potassium between hyper- and hypokalaemia, destabilising the cardiac conduction system, while autonomic neuropathy raises arrhythmia and sudden-death risk."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Polyautoimmunity: type 1 diabetes clusters with other autoimmune diseases—thyroid, coeliac and rheumatoid arthritis—through shared HLA and immune-susceptibility loci, so one autoimmune diagnosis raises the odds of another."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 attack: IFN-γ from autoreactive T-helper cells upregulates islet MHC and recruits cytotoxic cells, central to the immune destruction of insulin-producing beta cells."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Beta-cell toxicity: IL-1β secreted by islet-infiltrating macrophages directly impairs and kills beta cells, a key inflammatory mediator of the islet destruction in type 1 diabetes."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic killing: autoreactive CD8 T cells use perforin and granzyme to lyse beta cells, the final cytotoxic step that destroys the islets in type 1 diabetes."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Tolerance checkpoint and risk gene: CTLA-4 polymorphisms predispose to type 1 diabetes by weakening T-cell restraint, and CTLA4-Ig (abatacept) slows beta-cell loss in early disease."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Peripheral tolerance: PD-1 restrains autoreactive T cells against beta cells, and checkpoint-inhibitor cancer therapy that blocks it can precipitate fulminant autoimmune type 1 diabetes."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 islet inflammation: IL-17A-producing T cells infiltrate the islets and amplify the inflammatory beta-cell injury that accompanies the dominant cytotoxic response in type 1 diabetes."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "B-cell antigen presentation: B cells present islet autoantigens and produce autoantibodies in type 1 diabetes, and anti-CD20 (rituximab) delays beta-cell decline in new-onset disease — evidence B cells help drive the T-cell attack."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Cytokine beta-cell injury: TNF-α contributes to islet inflammation and beta-cell dysfunction, and the anti-TNF agent golimumab preserves endogenous insulin production in newly diagnosed type 1 diabetes."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Beta-cell apoptosis: caspase-3-mediated apoptosis is the final death pathway through which cytokine and cytotoxic-T-cell attack destroy insulin-producing beta cells in type 1 diabetes."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-signalling preservation: interferon and cytokine signals stressing beta cells run through JAK-STAT, and the JAK inhibitor baricitinib has been shown to preserve residual beta-cell function in new-onset type 1 diabetes, a disease-modifying strategy."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Islet GABA: beta cells co-secrete GABA, which acts in a paracrine loop to promote beta-cell survival and regeneration and to dampen islet inflammation, an endogenous protective signalling axis explored as a type 1 diabetes therapy."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell autoimmunity: although T-cell-mediated, type 1 diabetes depends on autoreactive B cells presenting islet antigens and making islet autoantibodies, the BAFF-supported B-cell arm targeted by the anti-CD20 therapy that can slow progression."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "Viral trigger sensing: enteroviral infection of islet β-cells (Coxsackie B already mapped) activates RIG-I-like sensing and a type-I interferon response that helps trigger the autoimmune destruction of type 1 diabetes."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "β-cell sensitisation: interferon signalling through STAT1 in β-cells upregulates MHC and pro-apoptotic genes, sensitising them to the autoimmune CD8 T-cell attack (perforin already mapped) that destroys them in type 1 diabetes."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis threshold: the balance of anti-apoptotic BCL-2 against cytokine- and CTL-driven pro-apoptotic signals sets the threshold for the β-cell apoptosis (caspase-3 already mapped) that depletes insulin-producing cells."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Viral/innate trigger: enteroviral and TLR signalling through MyD88 in islets and innate cells contributes to initiating the autoimmune attack on β-cells in type 1 diabetes."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Nucleic-acid sensing: cytosolic sensing of viral and self nucleic acids via cGAS-STING drives the type-I interferon (mapped) response implicated in triggering islet autoimmunity."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 induction: IL-12 drives the Th1/IFN-γ response (IFN-γ mapped) that directs the cytotoxic CD8 T-cell destruction of insulin-producing β-cells."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "β-cell PI3K-AKT signalling promotes insulin secretion and β-cell survival, and its failure under cytokine attack contributes to the β-cell apoptosis of type 1 diabetes."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β-dependent regulatory T-cell tolerance restrains islet autoimmunity, and its insufficiency permits the autoreactive destruction of β-cells."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10 is a key regulatory cytokine limiting islet inflammation; deficient IL-10-mediated control contributes to progression of type 1 diabetes."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates the macrophage and dendritic-cell inflammation within the insulitis that destroys pancreatic β-cells in type 1 diabetes."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling shapes the pathogenic Th17 response and inflammatory milieu of the islet autoimmunity of type 1 diabetes."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) governs the regulatory-T-cell control that, when insufficient, permits the islet autoimmunity of type 1 diabetes."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates β-cell survival and the T-cell tolerance whose breakdown drives the autoimmune β-cell destruction of type 1 diabetes."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by infiltrating myeloid cells amplify the insulitis of type 1 diabetes."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling participates in the cytokine-driven β-cell stress and the T-cell activation of the islet autoimmunity of type 1 diabetes."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven β-cell inflammatory stress and the autoreactive lymphocyte signaling of type 1 diabetes."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and hypoxic stress responses shape the β-cell vulnerability and islet inflammation of type 1 diabetes."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs both β-cell survival and the autoreactive lymphocyte activation of type 1 diabetes."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LCK) kinase signaling downstream of the T-cell receptor drives the autoreactive T-cell activation destroying β-cells in type 1 diabetes."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the β-cell survival under the immune and ER stress of type 1 diabetes."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the autoreactive immune response in type 1 diabetes."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the autoreactive T-cell and β-cell metabolism of type 1 diabetes."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the islets contributes to the insulitis of type 1 diabetes."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the islet leukocyte trafficking and β-cell interactions of type 1 diabetes."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the islet immune microenvironment of type 1 diabetes."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the immune-mediated islet inflammation of type 1 diabetes."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the autoreactive T-cell activation driving the β-cell destruction of type 1 diabetes."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Beta-cell exocytosis: calcium influx triggers the exocytosis of insulin granules from beta cells, the secretory step progressively lost as autoimmune destruction eliminates the beta-cell mass in type 1 diabetes."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Islet autoantibodies: IgG autoantibodies against insulin, GAD65, IA-2 and ZnT8 appear years before symptoms and are the basis for presymptomatic staging and screening of type 1 diabetes."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "GAD65 autoantigen: glutamic acid decarboxylase, which converts glutamate to GABA (already mapped) in beta cells, is a principal type 1 diabetes autoantigen, so the glutamate-GAD axis is central to the islet autoimmunity."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Diabetic ketoacidosis: absolute insulin deficiency drives lipolysis and ketogenesis, and the accumulating ketoacids release protons that cause the metabolic acidosis of diabetic ketoacidosis, a life-threatening presentation of type 1 diabetes."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Cerebral oedema: cerebral oedema is the most feared complication of diabetic ketoacidosis in children, a swelling of the brain during treatment that remains a leading cause of death and disability in paediatric type 1 diabetes."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th1/Th2 balance: a shift away from IL-4-driven type-2 responses toward the Th1 cytokines (IFN-gamma/IL-12 already mapped) favours the destructive islet autoimmunity, so the Th1/Th2 balance shapes progression to type 1 diabetes."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative beta-cell injury: reactive oxygen species, to which xanthine oxidase contributes, contribute to beta-cell destruction (perforin and NLRP3 already mapped) in type 1 diabetes, and oxidative stress also adds to the burden of diabetic ketoacidosis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Proliferative retinopathy: chronic hyperglycaemia in type 1 diabetes drives VEGF-mediated retinal neovascularisation, the proliferative diabetic retinopathy (eye already mapped) that threatens vision and is treated with anti-VEGF therapy."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Microvascular dysfunction: impaired endothelial nitric oxide from chronic hyperglycaemia contributes to the endothelial and microvascular dysfunction underlying the nephropathy (kidney already mapped) and retinopathy of type 1 diabetes."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Incretin adjunct: GLP-1 suppresses the counter-regulatory glucagon (already mapped) and slows gastric emptying, and incretin-based agents are being studied as adjuncts to insulin in type 1 diabetes."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Th1/Th2 balance: IL-13, with IL-4 (already mapped), forms the type-2 arm whose balance against the Th1 response (IFN-γ already mapped) shapes the autoimmune destruction of the β-cells in type 1 diabetes."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Islet inflammation: prostaglandins from the insulitis (IL-1 already mapped) contribute to the inflammatory β-cell injury of type 1 diabetes, part of the eicosanoid dimension of the autoimmune attack on the islets."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine dysregulation: leptin, low in the insulin-deficient (already mapped) state, contributes to the metabolic dysregulation of type 1 diabetes, interacting with insulin and amylin in the islet-adipose axis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Hypomagnesaemia: the hypomagnesaemia common in diabetes worsens the insulin (already mapped) action and is associated with the microvascular complications of type 1 diabetes."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine axis: adiponectin, with leptin (already mapped), is altered in type 1 diabetes, part of the adipokine dimension of its metabolic and cardiovascular-risk profile."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipokine of the metabolic-cardiovascular-risk profile of type 1 diabetes."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Islet macrophages: the islet-resident macrophages present the β-cell antigens and, with the innate (IL-1β and type-I interferon already mapped) signals, initiate and amplify the insulitis of type 1 diabetes."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Inflammation iron regulation: the chronic autoimmune inflammation (IL-6 and IL-1 already mapped) of type 1 diabetes raises the hepcidin, contributing to the iron dysregulation and the anaemia of chronic disease."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the autoimmune insulitis, complementing the dominant Th1 (IFN-γ and IL-12 already mapped) β-cell attack of type 1 diabetes."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the broader immune dysregulation of type 1 diabetes."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension and the atopic comorbidity reported in type 1 diabetes."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Islet-autoantibody source: the plasma cells secrete the islet autoantibodies (anti-GAD, IA-2, ZnT8; immunoglobulin already mapped) that mark the autoimmunity of type 1 diabetes."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Islet inflammation: IL-6 contributes to the insulitis and the β-cell inflammation of type 1 diabetes, a target explored (with the anti-CD3 already mapped) to preserve β-cell function."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Islet mast cells: the mast cells infiltrate the inflamed islets and contribute to the innate inflammatory milieu of the insulitis of type 1 diabetes."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Islet complement: the complement C5 and its activation (with C3 already mapped) contribute to the innate inflammatory injury of the insulitis of type 1 diabetes."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement to the myeloid recruitment into the inflamed islets of type 1 diabetes."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Autoimmune micronutrient: selenium, a selenoprotein antioxidant cofactor, is part of the micronutrient dimension (with vitamin D already mapped) of the autoimmune susceptibility and the oxidative β-cell stress of type 1 diabetes."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement activation in the inflamed islets of type 1 diabetes."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated in the islet autoimmunity of type 1 diabetes, and C1-INH has been explored as an islet-protective therapy."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "β-cell iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) implicated in the oxidative β-cell stress of type 1 diabetes."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-DC axis: TSLP, released from gut-epithelial (gut-microbiome already mapped) and skin (already mapped) barriers, activates mast cells (already mapped) and dendritic cells (already mapped), shaping the Th2/Th1 immune balance in the islet autoimmunity of type 1 diabetes."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-islet axis: bradykinin, generated in the inflamed pancreas (already mapped) by the kallikrein-kinin system, amplifies the macrophage (already mapped) and T-cell (already mapped) islet infiltration and augments endothelial permeability in the insulitis of type 1 diabetes."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoiesis support: erythropoietin counteracts the anaemia of chronic disease driven by the renal (already mapped) and inflammatory complications and the hepcidin (already mapped) dysregulation of advanced type 1 diabetes."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell islet effector: histamine, released by mast cells (already mapped) in the pancreatic islets, promotes vascular permeability and amplifies the cytokine cascade (IFN-γ and TNF-α already mapped) driving beta-cell destruction of type 1 diabetes."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Islet ECM remodelling: periostin, expressed by pancreatic stellate cells (already mapped) and fibroblasts under TGF-β (already mapped), promotes the peri-islet fibrotic remodelling that impairs beta-cell survival and insulin secretion in type 1 diabetes."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian beta-cell protection: melatonin, via MT1/MT2 receptors on pancreatic beta cells (already mapped), modulates insulin secretion rhythm and suppresses the oxidative stress (ROS already mapped) driving the autoimmune beta-cell destruction of type 1 diabetes."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "T1D testosterone: testosterone, via androgen receptors on pancreatic beta cells, attenuates T-helper-cell (already mapped) and B-cell (already mapped) autoreactivity; androgen deficiency worsens the TNF-α (already mapped) and macrophage (already mapped) insulitis in T1D."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "T1D serotonin: serotonin, synthesised by pancreatic (pancreas already mapped) beta cells, primes insulin (already mapped) secretion and islet mass; 5-HT also modulates T-helper-cell (already mapped) and macrophage (already mapped) autoreactive insulitis of type 1 diabetes."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "T1D prolactin: prolactin, via PRLR on pancreatic (pancreas already mapped) beta cells, promotes beta-cell survival and insulin (already mapped) secretion; prolactin modulates regulatory T-cell (already mapped) and macrophage (already mapped) immune protection against insulitis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "T1D oxytocin: oxytocin, via OXTR on pancreatic beta cells (pancreas already mapped) and regulatory T-cells (already mapped), suppresses the NF-κB (already mapped) insulitis-driving macrophage (already mapped) and T-helper-cell (already mapped) autoreactivity in type 1 diabetes."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "T1D vasopressin: vasopressin, via V1b receptors on beta cells (pancreas already mapped), modulates insulin (already mapped) secretion; vasopressin amplifies the adrenal (cortisol already mapped) stress axis and worsens NF-κB (already mapped) autoimmune insulitis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "T1D iodine: iodine-dependent thyroid hormones regulate beta-cell (pancreas already mapped) function and insulin (already mapped) secretion; hypothyroidism co-occurs with T1D via shared autoimmune mechanisms and amplifies NF-κB (already mapped) inflammatory insulitis."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "T1D iron: iron supports macrophage (already mapped) and T-helper-cell (already mapped) differentiation; iron deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) beta-cell destruction in T1D."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "T1D copper: copper, via ceruloplasmin and SOD in macrophages (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TNF-α (already mapped) driven autoimmune beta-cell destruction and IL-6 (already mapped) cascade in T1D."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "T1D phosphorus: phosphorus, as ATP donor for beta-cell function and mTOR (already mapped) in macrophages (already mapped), supports immunoregulation; phosphorus deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) autoimmune insulitis in T1D."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "T1D chloride: chloride, via CFTR in pancreatic beta cells (pancreas already mapped) and macrophages (already mapped), modulates insulin (already mapped) secretion; chloride imbalance amplifies NF-κB (already mapped) and NLRP3 (already mapped) beta-cell destruction in T1D."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "T1D sulfur: glutathione from sulfur-amino acids in macrophages (already mapped) and T-helper-cell (already mapped) quenches ROS; sulfur deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) autoimmune insulitis of T1D."
---

# Type 1 Diabetes

## Overview

**Type 1 diabetes (T1D)** is a **chronic autoimmune disease** in which T lymphocyte-mediated destruction of **insulin-producing pancreatic beta cells** in the islets of Langerhans leads to **absolute insulin deficiency**, requiring lifelong insulin replacement for survival [^atkinson-2014-t1d-lancet]. T1D accounts for ~5-10% of all diabetes (type 2 diabetes accounts for 90-95%) but is the predominant form in children and young adults, with peak incidence at 4-6 years and 10-14 years. The global incidence is rising ~3-4% per year, particularly in young children, with highest rates in Finland, Sardinia, and northern European countries (~60 per 100,000 per year).

**Key distinctions from Type 2 Diabetes:**
| Feature | T1D | T2D |
|---|---|---|
| Pathogenesis | Autoimmune beta cell destruction | Insulin resistance + relative beta cell failure |
| Insulin secretion | Near-zero (absolute deficiency) | Reduced but not absent (especially early) |
| Onset | Classically pediatric/young adult; 40% diagnosed >30 | Adult-onset; increasing in children |
| Body habitus | Any (classically non-obese) | Associated with obesity |
| Autoantibodies | Present (GAD65, IA-2, ZnT8, insulin) | Absent |
| Treatment | Insulin required from diagnosis | Lifestyle → oral agents → injectable/insulin |
| Ketoacidosis | Common at diagnosis; recurrent risk | Uncommon |

**Latent autoimmune diabetes in adults (LADA / Type 1.5):**
- Slowly progressive autoimmune diabetes presenting in adults (often >30 years); initially resembles T2D but GADA (anti-GAD65) positive; C-peptide declines over 1-5 years → insulin-dependence; accounts for ~2-12% of adult-onset diabetes; frequently misdiagnosed as T2D

**DKA (diabetic ketoacidosis) at T1D onset:**
- Absolute insulin deficiency → glucagon-dominant state → hepatic gluconeogenesis, glycogenolysis → hyperglycemia; concurrent lipolysis → FFAs → hepatic beta-oxidation → acetyl-CoA excess → ketone body synthesis (beta-hydroxybutyrate, acetoacetate) → metabolic acidosis; DKA mortality <1% in modern care; hallmark: high anion gap metabolic acidosis + hyperglycemia + ketonemia/ketonuria

## Structure

### Immunopathogenesis — T1D as autoimmune insulitis [^atkinson-2014-t1d-lancet]

**Genetic susceptibility:**
- **HLA (40-50% of T1D heritability):**
  - **HLA-DR3-DQ2 (DQB1*02:01/DQA1*05:01) and HLA-DR4-DQ8 (DQB1*03:02/DQA1*03:01):** Highest risk haplotypes (~10-15× increased T1D risk); DR3-DQ2/DR4-DQ8 heterozygotes have highest risk (~1 in 20 chance by age 15 in relatives); HLA controls antigen presentation of beta cell peptides to T cells
  - **HLA-DR15-DQ6 (DQB1*06:02):** Protective — dominant protection even in DQ8/DQ2 carriers
  - Mechanism: DQ8 molecule fails to efficiently tolerize autoreactive T cells to proinsulin and GAD65 peptides during thymic selection → escape of autoreactive repertoire into periphery
- **Non-HLA genes (50-60% of heritability):**
  - **INS VNTR (insulin gene promoter):** Short VNTR → reduced thymic insulin expression → impaired central tolerance to insulin → autoreactive T cells escape; long VNTR → more thymic insulin → better tolerance
  - **PTPN22 (protein tyrosine phosphatase N22, R620W variant):** Gain-of-function → increased T cell receptor signaling threshold → impaired negative selection; also risk factor for RA, SLE, Graves' disease
  - **IL2RA (CD25):** IL-2 signaling → Treg function; multiple T1D risk variants in IL2RA and IL2 gene regions
  - **CTLA4, PTPN2, IFIH1 (MDA5):** T cell co-stimulation, innate viral sensing → modulate T1D risk

**Environmental triggers:**
- **Enteroviruses (Coxsackievirus B):** Molecular mimicry (CB virus protein 2C shares sequence homology with GAD65); direct beta cell infection (CB virus receptor CAR expressed on beta cells); insulitis observed at CB virus-positive T1D diagnosis; CB virus exposure correlates with T1D incidence in longitudinal studies
- **Gut microbiome:** Reduced microbial diversity and specific dysbiosis patterns precede T1D in high-risk children (TEDDY/DIPP studies); loss of Lactobacillus → impaired SCFAs → impaired Treg differentiation → autoimmunity; germ-free NOD mice develop accelerated T1D
- **Vitamin D deficiency:** Inverse correlation with T1D incidence (northern latitudes, lower UV); vitamin D receptor expressed on Tregs → Treg maintenance; supplementation trials in high-risk children ongoing

**Insulitis (islet lymphocytic infiltrate):**
- Pathologically: CD8+ T cells (dominant), CD4+ T cells, macrophages, B cells infiltrate islets → "insulitis"; occurs years before clinical diagnosis
- CD8+ CTLs recognizing HLA-A2-restricted epitopes of IGRP (islet-specific glucose-6-phosphatase catalytic subunit-related protein), preproinsulin, GAD65, and IA-2 → perforin/granzyme B → beta cell apoptosis
- Progressive beta cell destruction: ~80% of beta cell mass lost before overt hyperglycemia (residual mass maintains near-normal glucose until critical threshold lost)

## Function

### Clinical presentation

**Classic triad at T1D diagnosis (DKA or polyuria/polydipsia):**
- **Polyuria, polydipsia, nocturia:** Hyperglycemia → glycosuria → osmotic diuresis → water loss → polydipsia
- **Weight loss:** Absolute insulin deficiency → catabolic state → muscle wasting, fat lipolysis
- **Fatigue:** Cellular glucose deprivation despite hyperglycemia (glucose cannot enter cells without insulin)
- **DKA (30-40% of new diagnoses):** Vomiting, abdominal pain, Kussmaul respirations (deep rapid breathing → compensating metabolic acidosis), fruity breath (acetone), altered consciousness at severe stage
- **Honeymoon period:** In first months post-diagnosis, residual beta cells recover temporarily (DKA stress resolved, inflammation subsides) → reduced insulin requirements (exogenous insulin suppresses autoimmune beta cell death); lasts weeks to months; eventually immune destruction resumes

**Chronic complications (shared with T2D, accelerated by glucose variability):**
- **Microvascular:** Diabetic retinopathy (leading cause of blindness, working-age adults), nephropathy (leading cause of ESRD in developed countries), neuropathy (peripheral > autonomic)
- **Macrovascular:** Cardiovascular disease accelerated 2-4× vs. age-matched controls; stroke; peripheral arterial disease
- **Hypoglycemia unawareness:** Loss of autonomic warning symptoms (sweating, tremor) from recurrent hypoglycemia → dangerous hypoglycemia risk; impaired hypoglycemia-associated autonomic failure (HAAF)

## Pathology

### Staging and screening [^insel-2015-t1d-staging]

**Three-stage T1D model (JDRF/ADA/Endocrine Society, 2015):**
- **Stage 1:** Multiple positive autoantibodies (≥2), normoglycemia, no symptoms — active autoimmunity, beta cell destruction underway; risk of progression to clinical T1D: ~75% at 10 years
- **Stage 2:** Multiple positive autoantibodies + dysglycemia (impaired fasting glucose or IGT, or HbA1c 5.7-6.4%) — 70-80% progress to clinical T1D within 5 years
- **Stage 3:** Clinical T1D (symptomatic hyperglycemia meeting diabetes diagnostic criteria)

**Autoantibody screening:**
- Autoantibodies: anti-GAD65 (most common, 75-80%), anti-IA-2/ICA512 (60-75%), anti-ZnT8 (60-70%), anti-insulin (most specific in young children <5 years, disappears with insulin therapy)
- Recommended screening in first-degree relatives and general population high-risk individuals (HLA-DR3/DR4); NIDDK Autoimmunity Screening for Kids (ASK) trial; commercial screening programs (TrialNet)

### Treatment

**Insulin therapy (all T1D patients require insulin):**
- **Multiple daily injections (MDI):** Basal insulin (glargine, detemir, degludec → once or twice daily) + bolus insulin (aspart, lispro, glulisine → with meals); "basal-bolus" regimen mimics physiological insulin; carbohydrate counting required for accurate bolus dosing
- **Continuous subcutaneous insulin infusion (CSII, insulin pump):** Delivers basal rate + bolus via subcutaneous catheter; allows variable basal rates (e.g., lower overnight, higher dawn phenomenon); hybrid closed-loop systems (Control-IQ, Omnipod 5, MiniMed 780G) combine pump + CGM + algorithm for semi-automated insulin delivery
- **Continuous glucose monitoring (CGM):** Real-time glucose readings (every 1-5 min); Dexcom G7 (10-day sensor), Libre 3 (14-day); factory calibrated; dramatically reduces HbA1c variability, hypoglycemia, DKA; time-in-range (70-180 mg/dL) is the key therapeutic target (>70% TIR associated with reduced complications)

**Disease-modifying therapy:**
- **Teplizumab (Tzield, anti-CD3 Fc-modified humanized antibody):** FDA approved 2022 for delaying Stage 3 T1D in Stage 2 (≥8 years old) — first approved T1D prevention therapy; anti-CD3 → T cell exhaustion and Treg expansion → slows beta cell destruction; median delay of clinical onset: 3 years in Stage 2 patients (TrialNet 2019 NEJM trial: 48 vs. 24 months median before Stage 3) [^herold-2019-teplizumab-t1d]; 14-day IV course; adverse effects: rash, cytokine release, transient EBV reactivation
- **Abatacept (CTLA-4 Ig):** T cell co-stimulation blockade (CD80/86-CD28 blockade) → reduced T cell priming; TrialNet trial: slows C-peptide decline in new-onset T1D at 2 years but effect wanes
- **Rituximab (anti-CD20):** B cell depletion → reduces antigen presentation and autoantibodies; C-peptide preservation at 1 year in new-onset T1D; no sustained long-term benefit

**Emerging and investigational:**
- **Low-dose IL-2:** Selectively expands Tregs (IL-2R high on Tregs); Phase 2 trials in new-onset T1D (DIPIT, ACT1ON)
- **Stem cell-derived islets (VX-880, Vertex):** SC-islets transplanted into portal vein → insulin production; early trials show insulin independence in severe T1D; requires immunosuppression
- **Encapsulated islets (ViaCyte, CRISPR-edited "immune invisible" beta cells):** Avoids immunosuppression requirement
- **Closed-loop insulin delivery + immunotherapy combinations:** Future frontier to both replace and protect beta cell function

## Connections

- `connects-to` → **[T Cytotoxic Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CD8+ CTLs are the primary beta cell destroyers in T1D: autoreactive CTLs recognize HLA-A2-restricted GAD65, IGRP, and insulin peptides → perforin/granzyme and Fas-FasL → beta cell apoptosis; islet CTL infiltration (insulitis) precedes clinical onset by years.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — CD4+ Th1 cells coordinate T1D autoimmunity: HLA-DQ8/DQ2-restricted beta cell antigen presentation → IFN-gamma, IL-2 → CTL priming and macrophage activation; Treg insufficiency allows unchecked Th1 expansion; teplizumab shifts Th1/Treg balance.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Treg insufficiency is a core T1D mechanism: FOXP3+ Tregs suppress autoreactive T cells in pancreatic lymph nodes and islets; NOD mice have Treg functional defects; low-dose IL-2 expands Tregs → ongoing clinical trials to delay T1D progression.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells act as APCs for beta cell antigens and produce autoantibodies (anti-GAD65, anti-IA-2, anti-ZnT8, anti-insulin) used for T1D staging (Stage 1: ≥2 Ab, normoglycemia; Stage 2: ≥2 Ab, dysglycemia); rituximab transiently preserves C-peptide in new-onset T1D.
- `treated-by` → **[Insulin](../../03-molecular/insulin/README.md)** — T1D results from autoimmune β-cell destruction → absolute insulin deficiency; CD8+ CTLs target GAD65, IGRP, and insulin peptides → apoptosis; lifelong insulin replacement (MDI or pump) is required; DCCT trial showed intensive insulin therapy halves long-term complications.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Type 1 diabetes is an organ-specific autoimmune attack on the insulin-producing beta cells of the pancreatic islets; T-cell insulitis silently destroys ~80% of beta-cell mass before hyperglycemia appears, leaving absolute insulin deficiency while the exocrine pancreas is spared.
- `connects-to` → **[Coxsackievirus B](../../../02-pathogen/01-viruses/coxsackievirus-b/README.md)** — Enteroviruses, especially Coxsackievirus B, are the leading environmental trigger of type 1 diabetes: CVB infects beta cells via the CAR receptor and its 2C protein shares homology with GAD65, and enteroviral RNA is found in islets at diagnosis — motivating CVB vaccine trials.
- `connects-to` → **[Diabetic Retinopathy](../diabetic-retinopathy/README.md)** — Chronic hyperglycemia from type 1 diabetes drives microvascular complications — virtually all T1D patients develop diabetic retinopathy after 20 years — so the DCCT showed that intensive insulin control cuts retinopathy onset 76%; eye screening starts 5 years after diagnosis.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — T1D and T2D share chronic hyperglycemia and vascular complications but differ in cause: T1D is autoimmune β-cell loss needing insulin, T2D is insulin resistance with relative deficiency; the line blurs with obesity-linked T1D and adult-onset autoimmune diabetes (LADA).
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Type 1 diabetes is strongly HLA-linked: MHC class II alleles HLA-DR3-DQ2 and DR4-DQ8 confer the greatest genetic risk by presenting islet autoantigens (insulin, GAD65) to autoreactive CD4+ T cells, while DQ6 is protective; HLA typing predicts risk in relatives.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Diabetic kidney disease is a leading T1D complication and a top cause of end-stage renal disease: chronic hyperglycemia → glomerular hyperfiltration, mesangial expansion and albuminuria → declining GFR; DCCT/EDIC showed tight glucose control plus RAAS blockade slows progression.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Type 1 diabetes is a leading cause of neuropathic pain through diabetic peripheral neuropathy: decades of hyperglycemia damage distal nerves via polyol, AGE, and microvascular mechanisms, causing burning stocking-glove pain—so early glycemic control is key prevention.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Type 1 diabetes impairs wound healing and underlies the diabetic foot: hyperglycemia, neuropathy (lost protective sensation), and microvascular disease stall healing and breed infection, so foot ulcers in long-standing T1D are a major cause of non-traumatic amputation.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells initiate the autoimmunity of type 1 diabetes: they capture islet antigens and present them to autoreactive T cells in pancreatic lymph nodes, breaking tolerance and launching the cytotoxic attack on β-cells—so DCs are a target for tolerance therapies.
- `connects-to` → **[Pemphigus Vulgaris](../pemphigus-vulgaris/README.md)** — Type 1 diabetes and pemphigus vulgaris are both HLA-linked autoimmune diseases: T1DM is T-cell-mediated destruction of pancreatic β-cells, while pemphigus is antibody-mediated against desmoglein in skin—two ends of the autoimmune spectrum that cluster in patients.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Type 1 diabetes and narcolepsy type 1 are both autoimmune diseases that destroy an irreplaceable cell population: T1DM the insulin-producing β-cells, narcolepsy the hypothalamic orexin neurons—each HLA-associated and likely T-cell-mediated, leaving a permanent deficit.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Type 1 diabetes accelerates atherosclerosis, the leading cause of death in T1DM: lifelong hyperglycemia injures the endothelium and worsens lipids, so even well-controlled patients face premature cardiovascular disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Type 1 diabetes is fundamentally an autoimmune disease: a breakdown of self-tolerance lets the immune system destroy insulin-producing beta cells, so it clusters with other autoimmune disorders and is now a target for immune-modulating prevention like teplizumab.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Type 1 diabetes deranges glucagon as well as insulin: as islets are destroyed, alpha cells lose normal glucose-sensing and fail to release glucagon during hypoglycemia, removing a key safety brake—so insulin treatment carries serious risk of severe lows.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Type 1 diabetes is the endocrine system's prototypic insulin-deficiency disease: autoimmune loss of pancreatic islet hormone output disrupts glucose homeostasis and often coexists with autoimmune thyroid and adrenal disease in polyglandular syndromes.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome may shape type 1 diabetes risk: early-life dysbiosis and a leaky gut can skew immune development and are linked to islet autoimmunity, so microbial exposures help explain why T1D incidence is rising faster than genetics alone can.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D is tied to type 1 diabetes risk: it modulates the immune system and regulatory T cells, and low early-life vitamin D status is associated with more islet autoimmunity—so deficiency is a candidate environmental trigger of this autoimmune disease.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Adrenaline is the backup against hypoglycemia in type 1 diabetes: when insulin overshoots, epinephrine should raise glucose and trigger warning symptoms, but in long-standing T1D this response blunts—causing dangerous hypoglycemia unawareness.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Type 1 diabetes travels with thyroid autoimmunity: it clusters in autoimmune polyglandular syndromes with Hashimoto's and Graves' disease, so patients are screened for thyroid antibodies and TSH—one autoimmune endocrine failure predicts another.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Diabetic ketoacidosis is a potassium trap: acidosis masks a severe total-body potassium deficit by shifting K+ out of cells, so giving insulin drives potassium back in and can cause dangerous hypokalemia—why DKA care obsessively tracks potassium.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol is type 1 diabetes's counter-hormone and a fellow autoimmune target: it raises glucose opposing insulin (driving hypoglycemia-rebound), and autoimmune adrenal failure (Addison's) can join T1D in polyglandular syndrome.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Type 1 diabetes attacks a zinc transporter: ZnT8, which loads zinc into insulin granules, is a major autoantigen—anti-ZnT8 antibodies help diagnose it—and zinc is needed to crystallize and store the very insulin the disease destroys.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type 1 diabetes carries a type I interferon signature: viral triggers (like coxsackievirus) and IFN make beta cells display more antigen and self-destruct, so interferon is a bridge from infection to the autoimmune attack on the islets.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Type 1 diabetes begins as insulitis led by macrophages: these innate cells are among the first to invade the islets, presenting beta-cell antigens and secreting toxic mediators that recruit the T cells which finish the destruction.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Type 1 diabetes can flood the blood with hydrogen ions: without insulin the body burns fat into acidic ketones, and the resulting diabetic ketoacidosis drops blood pH into a dangerous acidosis—the classic emergency that often reveals the disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Type 1 diabetes unleashes the liver: lacking insulin's brake, it overproduces glucose and converts incoming fatty acids into the ketone bodies of ketoacidosis, so the liver drives both the high blood sugar and the acid crisis.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Insulin loss in type 1 diabetes sets fat cells loose: unrestrained lipolysis pours free fatty acids out of adipocytes, supplying the liver with the raw material it turns into the ketones that cause ketoacidosis.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Years of high glucose in type 1 diabetes damage peripheral nerves, causing the numb, painful 'stocking-glove' neuropathy that threatens the feet with unnoticed injury and ulcers.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Type 1 diabetes demands regular eye screening: retinal photographs in visible-light photons catch the diabetic retinopathy that years of glucose swings inflict on the retina, before vision is lost.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Type 1 diabetes is a leading cause of kidney failure: decades of high glucose scar the glomeruli into diabetic nephropathy, which urine-protein screening catches early enough to slow.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the islet under attack: beta cells packed with insulin secretory granules sit besieged by infiltrating T cells in insulitis, the autoimmune assault that wipes out the body's only source of insulin.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The red cell keeps the diabetic's long-term score: glucose binds irreversibly to hemoglobin over the erythrocyte's lifespan, so the HbA1c reflects months of average sugar and guides how tightly the insulin is dosed.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Diabetic ketoacidosis is also a sodium crisis: sky-high glucose pulls water into the blood and lowers the measured sodium, while the osmotic diuresis drains salt and water — making careful sodium and fluid replacement central to treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Type 1 diabetes leaves an autoantibody trail: antibodies against GAD65, IA-2, ZnT8, and insulin appear before symptoms, marking the autoimmune attack on the islets and letting at-risk children be identified years ahead.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Control is read off the hemoglobin: glucose glycates the red-cell protein into HbA1c, whose level averages months of blood sugar and guides how tightly the insulin regimen is run to stave off complications.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye is an early casualty: years of high glucose damage the retina's microvessels into diabetic retinopathy, the leading cause of blindness in working-age adults, so regular retinal screening is built into care.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Autoimmunity rarely travels alone: type 1 diabetes clusters with other autoimmune endocrine disease, and Addison's disease — autoimmune destruction of the adrenal gland — joins it in the polyglandular syndromes that demand vigilance.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy demands near-perfect control: high glucose around conception raises congenital malformation and miscarriage risk and later causes macrosomia, so type 1 diabetics tighten their insulin and monitoring before and through pregnancy.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Glucose injures the vessel lining throughout: damaged endothelial cells underlie both the microvascular complications in eye, kidney, and nerve and the accelerated atherosclerosis that makes heart disease the long-term killer in type 1 diabetes.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Type 1 diabetes is partly an IL-2 problem: weak IL-2 signaling starves the regulatory T cells that should restrain islet autoimmunity, so low-dose IL-2 to expand Tregs is a leading strategy to halt beta-cell destruction.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells join the islet assault: they infiltrate the inflamed pancreatic islets and help kill insulin-making beta cells, adding an innate arm to the T-cell-driven autoimmunity of type 1 diabetes.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The gut helps set off islet autoimmunity: a leaky small-bowel barrier and dietary antigens prime the immune system, and the strong overlap with celiac disease ties intestinal immunity to the onset of type 1 diabetes.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Innate inflammation joins the islet attack: NLRP3 inflammasome activation in islet-infiltrating immune cells releases IL-1β that is directly toxic to beta cells, an innate arm layered on the T-cell-driven autoimmunity.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The earliest invaders may be neutrophils: neutrophils and their NETs infiltrate the islets early in the disease, an innate trigger thought to help initiate the autoimmune insulitis before T cells finish the job.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — A dangerous way to control weight: some young people with type 1 diabetes deliberately skip insulin to lose weight ('diabulimia'), a disordered-eating behavior that overlaps anorexia and drives repeated ketoacidosis and early complications.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Cytokines kill the beta cell through NF-κB: IL-1β, TNF and interferon from infiltrating immune cells activate NF-κB inside islet beta cells, driving the stress and apoptosis that destroys insulin production in type 1 diabetes.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Ketoacidosis turns the blood prothrombotic: the dehydration, inflammation and endothelial injury of diabetic ketoacidosis sharply raise clot risk, so venous thromboembolism is a recognized hazard of severe decompensation.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Infection and diabetes feed each other dangerously: hyperglycemia blunts immune defense while infection commonly precipitates ketoacidosis, so serious infection and sepsis are both a trigger and a threat in type 1 diabetes.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Sugar-rich tissue invites the yeast: glucose in blood and urine plus impaired immunity favor Candida overgrowth, so recurrent vulvovaginal, oral and skin-fold candidiasis often flags poor glycemic control.
- `connects-to` → **[Stroke](../stroke/README.md)** — Decades of high sugar damage the arteries: type 1 diabetes accelerates atherosclerosis from a young age, and the resulting large-vessel disease raises the lifetime risk of ischemic stroke.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — The relentless self-management weighs on mood: the lifelong burden of carbohydrate counting, injections and fear of hypoglycemia gives type 1 diabetes a high rate of depression and diabetes distress.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Decades of glucose injury weaken the heart: type 1 diabetes accelerates coronary disease and causes a diabetic cardiomyopathy through microvascular damage and metabolic stress, routes toward heart failure over a lifetime.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — It builds a more fragile skeleton: insulin's loss removes a bone-anabolic signal, so type 1 diabetes is associated with lower bone mineral density and a markedly elevated fracture risk.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Ketoacidosis and high glucose invite invasive mold: poorly controlled type 1 diabetes, especially in ketoacidosis, impairs neutrophil function and predisposes to invasive fungal infections such as aspergillosis and mucormycosis.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Autoimmunity and neuropathy hit the gut: type 1 diabetes co-occurs with coeliac disease and autoimmune gastritis, and longstanding autonomic neuropathy causes gastroparesis with erratic glucose control.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It marks the skin in characteristic ways: type 1 diabetes causes necrobiosis lipoidica, repeated-injection lipohypertrophy and diabetic dermopathy, and the autoimmune diathesis brings vitiligo.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Relentless self-management and hypo-fear breed worry: the constant glucose monitoring, dosing decisions and dread of hypoglycaemia in type 1 diabetes generate diabetes distress and chronic anxiety.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Glucose extremes endanger the brain: severe hypoglycaemia causes seizures and coma, diabetic ketoacidosis can cause cerebral oedema in children, and long-standing disease brings peripheral and autonomic neuropathy.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It stiffens joints and breaks down the foot: type 1 diabetes causes diabetic cheiroarthropathy with limited joint mobility, frozen shoulder, and Charcot neuroarthropathy that destroys the foot's architecture.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Autonomic nerve damage misruns the heart: cardiac autonomic neuropathy in type 1 diabetes causes resting tachycardia, blunted heart-rate variability and silent myocardial ischaemia that masks heart attacks.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Acidosis drives deep breathing: diabetic ketoacidosis causes the deep, laboured Kussmaul breathing that blows off CO2, and diabetes mildly reduces lung function and raises pneumonia risk.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — It weakens defences against TB: diabetes impairs cell-mediated immunity and roughly triples the risk of active tuberculosis, worsening its course and treatment outcomes.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — It invites skin and foot infection: impaired immunity and peripheral neuropathy predispose type 1 diabetes to staphylococcal skin abscesses and diabetic-foot infections.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Autoimmunity is born in a lymph node: the pancreatic (peri-islet) lymph nodes are where dendritic cells first present beta-cell antigens to autoreactive T cells, making regional lymphatics the cradle of type 1 diabetes.
- `connects-to` → **[Rotavirus](../../../02-pathogen/01-viruses/rotavirus/README.md)** — A childhood virus under suspicion: enteric infections including rotavirus are studied as triggers of islet autoimmunity through molecular mimicry, and rotavirus vaccination has been linked to lower type 1 diabetes incidence.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Cancer immunotherapy can cause it: PD-1/PD-L1 checkpoint inhibitors trigger a rapid autoimmune type 1 diabetes as an immune-related adverse event, often presenting with abrupt ketoacidosis and low C-peptide.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — It destroys the insulin source: type 1 diabetes is autoimmune T-cell destruction of the insulin-producing beta cells of the pancreatic islets, leaving absolute insulin deficiency once most islet mass is lost.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Immunotherapy can delay onset: the anti-CD3 antibody teplizumab postpones progression to clinical type 1 diabetes in at-risk individuals by blunting the autoreactive T cells, the first disease-modifying therapy for the condition.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — It scars the kidney filter too: like type 2 diabetes, chronic hyperglycaemia in type 1 thickens the glomerular basement membrane and expands the mesangium, causing the diabetic nephropathy that is a major long-term complication.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Macrovascular disease shortens it: type 1 diabetes accelerates atherosclerosis and arterial stiffening, so cardiovascular disease is the leading cause of death in long-standing T1D despite good glucose control.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Its autoantibodies signal the autoimmunity: type 1 diabetes is a T-cell attack on beta cells, but islet autoantibodies (anti-GAD, anti-IA2) made with germinal-centre B-cell help mark the loss of tolerance and predict onset.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — It can be precipitated by infection: COVID-19 and other viral infections are linked to new-onset type 1 diabetes, with viral injury and molecular mimicry implicated in triggering islet autoimmunity in susceptible children.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Shared autoimmune ground: type 1 diabetes and psoriasis cluster together, the two sharing immune-regulatory susceptibility loci that tilt toward autoimmunity across organs.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — A different route to insulin lack: cystic-fibrosis-related diabetes arises from progressive pancreatic destruction, a hybrid of the insulin deficiency of type 1 and resistance—the commonest CF comorbidity in adults.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Diabetic cardiomyopathy from youth: lifelong type 1 diabetes stiffens and scars the myocardium through AGE deposition and microvascular disease, raising heart-failure risk independent of coronary disease.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Fragile bones from diagnosis: unlike type 2 diabetes, type 1 lowers bone density and impairs bone quality from a young age, and Charcot neuroarthropathy destroys the foot's cortical bone in those with neuropathy.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Electrolytes and the heart: diabetic ketoacidosis and its treatment swing potassium between hyper- and hypokalaemia, destabilising the cardiac conduction system, while autonomic neuropathy raises arrhythmia and sudden-death risk.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Polyautoimmunity: type 1 diabetes clusters with other autoimmune diseases—thyroid, coeliac and rheumatoid arthritis—through shared HLA and immune-susceptibility loci, so one autoimmune diagnosis raises the odds of another.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 attack: IFN-γ from autoreactive T-helper cells upregulates islet MHC and recruits cytotoxic cells, central to the immune destruction of insulin-producing beta cells.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Beta-cell toxicity: IL-1β secreted by islet-infiltrating macrophages directly impairs and kills beta cells, a key inflammatory mediator of the islet destruction in type 1 diabetes.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic killing: autoreactive CD8 T cells use perforin and granzyme to lyse beta cells, the final cytotoxic step that destroys the islets in type 1 diabetes.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Tolerance checkpoint and risk gene: CTLA-4 polymorphisms predispose to type 1 diabetes by weakening T-cell restraint, and CTLA4-Ig (abatacept) slows beta-cell loss in early disease.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Peripheral tolerance: PD-1 restrains autoreactive T cells against beta cells, and checkpoint-inhibitor cancer therapy that blocks it can precipitate fulminant autoimmune type 1 diabetes.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 islet inflammation: IL-17A-producing T cells infiltrate the islets and amplify the inflammatory beta-cell injury that accompanies the dominant cytotoxic response in type 1 diabetes.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — B cells present islet autoantigens and produce autoantibodies in type 1 diabetes, and anti-CD20 (rituximab) delays beta-cell decline in new-onset disease—evidence that B cells, not only T cells, help drive the autoimmune attack.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α contributes to islet inflammation and beta-cell dysfunction, and the anti-TNF agent golimumab preserves endogenous insulin production in newly diagnosed type 1 diabetes—a disease-modifying cytokine target.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3-mediated apoptosis is the final common death pathway through which cytokine signaling and cytotoxic-T-cell attack destroy the insulin-producing beta cells, the cellular endpoint of type 1 diabetes.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Interferon and cytokine signals stressing beta cells run through JAK-STAT, and the JAK inhibitor baricitinib has been shown to preserve residual beta-cell function in new-onset type 1 diabetes, a disease-modifying strategy.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Beta cells co-secrete GABA, which acts in a paracrine loop to promote beta-cell survival and regeneration and to dampen islet inflammation, an endogenous protective signaling axis explored as a type 1 diabetes therapy.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — Although T-cell-mediated, type 1 diabetes depends on autoreactive B cells presenting islet antigens and making islet autoantibodies, the BAFF-supported B-cell arm targeted by the anti-CD20 therapy that can slow progression.
- `connects-to` → **[RIG-I](../../03-molecular/rig-i/README.md)** — Enteroviral infection of islet β-cells (Coxsackie B already mapped) activates RIG-I-like sensing and a type-I interferon response that helps trigger the autoimmune destruction of type 1 diabetes.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — Interferon signaling through STAT1 in β-cells upregulates MHC and pro-apoptotic genes, sensitizing them to the autoimmune CD8 T-cell attack (perforin already mapped) that destroys them in type 1 diabetes.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — The balance of anti-apoptotic BCL-2 against cytokine- and CTL-driven pro-apoptotic signals sets the threshold for the β-cell apoptosis (caspase-3 already mapped) that depletes insulin-producing cells.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Enteroviral and TLR signaling through MyD88 in islets and innate cells contributes to initiating the autoimmune attack on β-cells in type 1 diabetes.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic sensing of viral and self nucleic acids via cGAS-STING drives the type-I interferon (mapped) response implicated in triggering islet autoimmunity.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 drives the Th1/IFN-γ response (IFN-γ mapped) that directs the cytotoxic CD8 T-cell destruction of insulin-producing β-cells.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — β-cell PI3K-AKT signaling promotes insulin secretion and β-cell survival, and its failure under cytokine attack contributes to the β-cell apoptosis of type 1 diabetes.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β-dependent regulatory T-cell tolerance restrains islet autoimmunity, and its insufficiency permits the autoreactive destruction of β-cells.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10 is a key regulatory cytokine limiting islet inflammation; deficient IL-10-mediated control contributes to progression of type 1 diabetes.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates the macrophage and dendritic-cell inflammation within the insulitis that destroys pancreatic β-cells in type 1 diabetes.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling shapes the pathogenic Th17 response and inflammatory milieu of the islet autoimmunity of type 1 diabetes.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) governs the regulatory-T-cell control that, when insufficient, permits the islet autoimmunity of type 1 diabetes.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates β-cell survival and the T-cell tolerance whose breakdown drives the autoimmune β-cell destruction of type 1 diabetes.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by infiltrating myeloid cells amplify the insulitis of type 1 diabetes.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling participates in the cytokine-driven β-cell stress and the T-cell activation of the islet autoimmunity of type 1 diabetes.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven β-cell inflammatory stress and the autoreactive lymphocyte signaling of type 1 diabetes.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and hypoxic stress responses shape the β-cell vulnerability and islet inflammation of type 1 diabetes.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs both β-cell survival and the autoreactive lymphocyte activation of type 1 diabetes.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LCK) kinase signaling downstream of the T-cell receptor drives the autoreactive T-cell activation destroying β-cells in type 1 diabetes.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the β-cell survival under the immune and ER stress of type 1 diabetes.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the autoreactive immune response in type 1 diabetes.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the autoreactive T-cell and β-cell metabolism of type 1 diabetes.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the islets contributes to the insulitis of type 1 diabetes.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the islet leukocyte trafficking and β-cell interactions of type 1 diabetes.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the islet immune microenvironment of type 1 diabetes.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the immune-mediated islet inflammation of type 1 diabetes.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the autoreactive T-cell activation driving the β-cell destruction of type 1 diabetes.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Beta-cell exocytosis: calcium influx triggers the exocytosis of insulin granules from beta cells, the secretory step progressively lost as autoimmune destruction eliminates the beta-cell mass in type 1 diabetes.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Islet autoantibodies: IgG autoantibodies against insulin, GAD65, IA-2 and ZnT8 appear years before symptoms and are the basis for presymptomatic staging and screening of type 1 diabetes.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — GAD65 autoantigen: glutamic acid decarboxylase, which converts glutamate to GABA (already mapped) in beta cells, is a principal type 1 diabetes autoantigen, so the glutamate-GAD axis is central to the islet autoimmunity.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Diabetic ketoacidosis: absolute insulin deficiency drives lipolysis and ketogenesis, and the accumulating ketoacids release protons that cause the metabolic acidosis of diabetic ketoacidosis, a life-threatening presentation of type 1 diabetes.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Cerebral oedema: cerebral oedema is the most feared complication of diabetic ketoacidosis in children, a swelling of the brain during treatment that remains a leading cause of death and disability in paediatric type 1 diabetes.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th1/Th2 balance: a shift away from IL-4-driven type-2 responses toward the Th1 cytokines (IFN-gamma/IL-12 already mapped) favours the destructive islet autoimmunity, so the Th1/Th2 balance shapes progression to type 1 diabetes.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative beta-cell injury: reactive oxygen species, to which xanthine oxidase contributes, contribute to beta-cell destruction (perforin and NLRP3 already mapped) in type 1 diabetes, and oxidative stress also adds to the burden of diabetic ketoacidosis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Proliferative retinopathy: chronic hyperglycaemia in type 1 diabetes drives VEGF-mediated retinal neovascularisation, the proliferative diabetic retinopathy (eye already mapped) that threatens vision and is treated with anti-VEGF therapy.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Microvascular dysfunction: impaired endothelial nitric oxide from chronic hyperglycaemia contributes to the endothelial and microvascular dysfunction underlying the nephropathy (kidney already mapped) and retinopathy of type 1 diabetes.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Incretin adjunct: GLP-1 suppresses the counter-regulatory glucagon (already mapped) and slows gastric emptying, and incretin-based agents are being studied as adjuncts to insulin in type 1 diabetes.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Th1/Th2 balance: IL-13, with IL-4 (already mapped), forms the type-2 arm whose balance against the Th1 response (IFN-γ already mapped) shapes the autoimmune destruction of the β-cells in type 1 diabetes.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Islet inflammation: prostaglandins from the insulitis (IL-1 already mapped) contribute to the inflammatory β-cell injury of type 1 diabetes, part of the eicosanoid dimension of the autoimmune attack on the islets.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine dysregulation: leptin, low in the insulin-deficient (already mapped) state, contributes to the metabolic dysregulation of type 1 diabetes, interacting with insulin and amylin in the islet-adipose axis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Hypomagnesaemia: the hypomagnesaemia common in diabetes worsens the insulin (already mapped) action and is associated with the microvascular complications of type 1 diabetes.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine axis: adiponectin, with leptin (already mapped), is altered in type 1 diabetes, part of the adipokine dimension of its metabolic and cardiovascular-risk profile.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipokine of the metabolic-cardiovascular-risk profile of type 1 diabetes.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Islet macrophages: the islet-resident macrophages present the β-cell antigens and, with the innate (IL-1β and type-I interferon already mapped) signals, initiate and amplify the insulitis of type 1 diabetes.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Inflammation iron regulation: the chronic autoimmune inflammation (IL-6 and IL-1 already mapped) of type 1 diabetes raises the hepcidin, contributing to the iron dysregulation and the anaemia of chronic disease.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the autoimmune insulitis, complementing the dominant Th1 (IFN-γ and IL-12 already mapped) β-cell attack of type 1 diabetes.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the broader immune dysregulation of type 1 diabetes.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension and the atopic comorbidity reported in type 1 diabetes.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Islet-autoantibody source: the plasma cells secrete the islet autoantibodies (anti-GAD, IA-2, ZnT8; immunoglobulin already mapped) that mark the autoimmunity of type 1 diabetes.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Islet inflammation: IL-6 contributes to the insulitis and the β-cell inflammation of type 1 diabetes, a target explored (with the anti-CD3 already mapped) to preserve β-cell function.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Islet mast cells: the mast cells infiltrate the inflamed islets and contribute to the innate inflammatory milieu of the insulitis of type 1 diabetes.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Islet complement: the complement C5 and its activation (with C3 already mapped) contribute to the innate inflammatory injury of the insulitis of type 1 diabetes.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement to the myeloid recruitment into the inflamed islets of type 1 diabetes.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Autoimmune micronutrient: selenium, a selenoprotein antioxidant cofactor, is part of the micronutrient dimension (with vitamin D already mapped) of the autoimmune susceptibility and the oxidative β-cell stress of type 1 diabetes.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement activation in the inflamed islets of type 1 diabetes.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated in the islet autoimmunity of type 1 diabetes, and C1-INH has been explored as an islet-protective therapy.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — β-cell iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) implicated in the oxidative β-cell stress of type 1 diabetes.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-DC axis: TSLP, released from gut-epithelial (gut-microbiome already mapped) and skin (already mapped) barriers, activates mast cells (already mapped) and dendritic cells (already mapped), shaping the Th2/Th1 immune balance in the islet autoimmunity of type 1 diabetes.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-islet axis: bradykinin, generated in the inflamed pancreas (already mapped) by the kallikrein-kinin system, amplifies the macrophage (already mapped) and T-cell (already mapped) islet infiltration and augments endothelial permeability in the insulitis of type 1 diabetes.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoiesis support: erythropoietin counteracts the anaemia of chronic disease driven by the renal (already mapped) and inflammatory complications and the hepcidin (already mapped) dysregulation of advanced type 1 diabetes.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell islet effector: histamine, released by mast cells (already mapped) in the pancreatic islets under inflammatory stimuli, promotes the vascular permeability and amplifies the cytokine (IFN-γ and TNF-α already mapped) cascade driving the beta-cell destruction of type 1 diabetes.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Islet ECM remodelling: periostin, expressed by pancreatic stellate cells (already mapped) and fibroblasts under TGF-β (already mapped), promotes the peri-islet fibrotic remodelling that impairs beta-cell survival and insulin secretion in type 1 diabetes.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian beta-cell protection: melatonin, via MT1/MT2 receptors on pancreatic beta cells (already mapped), modulates insulin secretion rhythm and suppresses the oxidative stress (ROS already mapped) driving the autoimmune beta-cell destruction of type 1 diabetes.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — T1D testosterone: testosterone, via androgen receptors on pancreatic beta cells, attenuates T-helper-cell (already mapped) and B-cell (already mapped) autoreactivity; androgen deficiency worsens the TNF-α (already mapped) and macrophage (already mapped) insulitis in T1D.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — T1D serotonin: serotonin, synthesised by pancreatic (pancreas already mapped) beta cells, primes insulin (already mapped) secretion and islet mass; 5-HT also modulates T-helper-cell (already mapped) and macrophage (already mapped) autoreactive insulitis of type 1 diabetes.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — T1D prolactin: prolactin, via PRLR on pancreatic (pancreas already mapped) beta cells, promotes beta-cell survival and insulin (already mapped) secretion; prolactin modulates regulatory T-cell (already mapped) and macrophage (already mapped) immune protection against insulitis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — T1D oxytocin: oxytocin, via OXTR on pancreatic beta cells (pancreas already mapped) and regulatory T-cells (already mapped), suppresses the NF-κB (already mapped) insulitis-driving macrophage (already mapped) and T-helper-cell (already mapped) autoreactivity in type 1 diabetes.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — T1D vasopressin: vasopressin, via V1b receptors on beta cells (pancreas already mapped), modulates insulin (already mapped) secretion; vasopressin amplifies the adrenal (cortisol already mapped) stress axis and worsens NF-κB (already mapped) autoimmune insulitis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — T1D iodine: iodine-dependent thyroid hormones regulate beta-cell (pancreas already mapped) function and insulin (already mapped) secretion; hypothyroidism co-occurs with T1D via shared autoimmune mechanisms and amplifies NF-κB (already mapped) inflammatory insulitis.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — T1D iron: iron supports macrophage (already mapped) and T-helper-cell (already mapped) differentiation; iron deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) beta-cell destruction in T1D.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — T1D copper: copper, via ceruloplasmin and SOD in macrophages (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TNF-α (already mapped) driven autoimmune beta-cell destruction and IL-6 (already mapped) cascade in T1D.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — T1D phosphorus: phosphorus, as ATP donor for beta-cell function and mTOR (already mapped) in macrophages (already mapped), supports immunoregulation; phosphorus deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) autoimmune insulitis in T1D.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — T1D chloride: chloride, via CFTR in pancreatic beta cells (pancreas already mapped) and macrophages (already mapped), modulates insulin (already mapped) secretion; chloride imbalance amplifies NF-κB (already mapped) and NLRP3 (already mapped) beta-cell destruction in T1D.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — T1D sulfur: glutathione from sulfur-amino acids in macrophages (already mapped) and T-helper-cell (already mapped) quenches ROS; sulfur deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-6 (already mapped) autoimmune insulitis of T1D.

[^atkinson-2014-t1d-lancet]: Atkinson MA, Eisenbarth GS, Michels AW. Type 1 diabetes. *Lancet.* 2014;383(9911):69-82. [doi:10.1016/S0140-6736(13)60591-7](https://doi.org/10.1016/S0140-6736(13)60591-7) · [PubMed 23890997](https://pubmed.ncbi.nlm.nih.gov/23890997/)
[^herold-2019-teplizumab-t1d]: Herold KC, Bundy BN, Long SA, et al. An anti-CD3 antibody, teplizumab, in relatives at risk for type 1 diabetes. *N Engl J Med.* 2019;381(7):603-613. [doi:10.1056/NEJMoa1905155](https://doi.org/10.1056/NEJMoa1905155) · [PubMed 31180675](https://pubmed.ncbi.nlm.nih.gov/31180675/)
[^insel-2015-t1d-staging]: Insel RA, Dunne JL, Atkinson MA, et al. Staging presymptomatic type 1 diabetes. *Diabetes Care.* 2015;38(10):1964-1974. [doi:10.2337/dc15-1419](https://doi.org/10.2337/dc15-1419) · [PubMed 26404926](https://pubmed.ncbi.nlm.nih.gov/26404926/)
