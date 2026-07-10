---
schema: human-scale-entry/v1
id: nash
name: NASH
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Metabolic liver disease from steatosis (NAFLD) through steatohepatitis (NASH) to fibrosis and HCC; driven by insulin resistance and hepatic lipid overload. TGF-beta activates stellate cells → fibrosis; semaglutide and resmetirom (THR-beta agonist) are approved treatments."
aliases: ["nonalcoholic steatohepatitis", "NAFLD", "nonalcoholic fatty liver disease", "MASLD", "MASH", "metabolic dysfunction-associated steatotic liver disease", "metabolic dysfunction-associated steatohepatitis", "hepatic steatosis"]
sources:
  - id: younossi-2016-nafld-epidemiology
    type: peer-reviewed
    cite: "Younossi ZM, Koenig AB, Abdelatif D, Fazel Y, Henry L, Wymer M. Global epidemiology of nonalcoholic fatty liver disease — meta-analytic assessment of prevalence, incidence, and outcomes. Hepatology. 2016;64(1):73-84."
    doi: "10.1002/hep.28431"
    pmid: "26707365"
    url: "https://doi.org/10.1002/hep.28431"
  - id: harrison-2024-resmetirom
    type: peer-reviewed
    cite: "Harrison SA, Bedossa P, Guy CD, et al. A phase 3, randomized, controlled trial of resmetirom in NAFLD. N Engl J Med. 2024;390(6):497-509."
    doi: "10.1056/NEJMoa2309000"
    pmid: "38324483"
    url: "https://doi.org/10.1056/NEJMoa2309000"
  - id: rinella-2023-masld-nomenclature
    type: peer-reviewed
    cite: "Rinella ME, Lazarus JV, Ratziu V, et al. A multisociety Delphi consensus statement on new fatty liver disease nomenclature. Hepatology. 2023;78(6):1966-1986."
    doi: "10.1097/HEP.0000000000000520"
    pmid: "37363821"
    url: "https://doi.org/10.1097/HEP.0000000000000520"
cross_links:
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta is the primary pro-fibrogenic signal in NASH: macrophage- and hepatocyte-derived TGF-beta → hepatic stellate cell activation → alpha-SMA and collagen I deposition → fibrosis and cirrhosis; TGF-beta also promotes hepatocyte EMT and NASH-HCC progression."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Kupffer cells and recruited monocytes drive NASH: LPS-TLR4 → NF-kB → TNF-alpha, IL-1beta, IL-6 → hepatocyte injury and stellate cell activation; M1 macrophage polarization correlates with NASH histological activity; macrophage depletion attenuates experimental NASH fibrosis."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Hepatocytes are the primary NASH target: lipid overload → ER stress, mitochondrial dysfunction, ROS → hepatocyte ballooning and lipoapoptosis; dying hepatocytes release DAMPs → Kupffer cell activation; hepatocyte SREBP-1c drives lipogenesis under insulin resistance."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Hepatic insulin resistance is the core NASH driver: impaired insulin signaling → failure to suppress hepatic glucose output and VLDL; hyperinsulinemia → SREBP-1c → lipogenesis → steatosis and lipotoxicity; GLP-1 agonists and PPAR-gamma agonists improve insulin sensitivity."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Semaglutide resolved NASH histology in 59% vs 17% placebo (Phase 2); GLP-1R activation reduces hepatic lipogenesis, liver inflammation, and oxidative stress; semaglutide ESSENCE Phase 3 NASH trial is ongoing; GLP-1R agonists are promising disease-modifying agents for NASH."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adiponectin deficiency impairs hepatic AMPK → reduced fatty acid oxidation → steatosis; adiponectin suppresses TNF-α and NF-κB in Kupffer cells → reduced hepatic inflammation; pioglitazone (PPARγ agonist) raises adiponectin, reduces NASH steatohepatitis, and slows fibrosis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Resistin (primarily monocyte/macrophage-derived in humans) activates NF-κB in Kupffer cells → TNF-α and IL-6 → NASH inflammation; resistin correlates with NASH histological severity; resistin inhibits adiponectin → impairs hepatic AMPK → steatosis and fibrosis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Hepatocyte lipotoxicity + DAMPs → Kupffer cell CCL2; elevated hepatic CCL2 → CCR2+ monocyte-derived macrophage recruitment → NLRP3 → IL-1β + TNF-α → stellate cell activation → fibrosis; cenicriviroc (CCR2/CCR5 dual antagonist) studied in CENTAUR/AURORA trials."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10 from Kupffer cells and hepatic Tregs restrains NLRP3 inflammasome activation and stellate cell activation in NASH; IL-10 KO mice develop spontaneous steatohepatitis on high-fat diet; IL-10 deficiency correlates with fibrosis stage in human NASH biopsies."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "TGF-β1 → periostin in hepatic stellate cells → integrin αvβ3 → FAK/PI3K → collagen I/III deposition → hepatic fibrosis in NASH; periostin correlates with fibrosis stage; periostin-null mice develop less hepatic fibrosis in NASH models; periostin marks activated stellate cells."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "EDA-FN is upregulated in NASH liver via TGF-β1 → activates integrin α4β7 and TLR4 on HSCs → myofibroblast differentiation → collagen I/III → hepatic fibrosis; serum EDA-FN correlates with NASH fibrosis stage; FN matrix stiffness amplifies TGF-β activation in fibrotic liver."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "NASH is the hepatic face of type 2 diabetes and metabolic syndrome: insulin resistance floods the liver with fatty acids and drives lipotoxic inflammation, so most NASH patients are diabetic or pre-diabetic, and the two accelerate each other toward cirrhosis."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity is the leading driver of NASH: excess visceral fat delivers free fatty acids and inflammatory adipokines to the liver, causing steatosis that progresses to steatohepatitis—so weight loss (diet, GLP-1 agonists, bariatric surgery) is the most effective treatment."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "NASH is now a leading cause of hepatocellular carcinoma: chronic steatohepatitis drives fibrosis and cirrhosis that can become liver cancer—and uniquely, NASH-related HCC can arise even without cirrhosis, so rising fatty-liver prevalence is reshaping HCC epidemiology."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "NASH is the inflammatory, fibrosing form of fatty liver disease: metabolic overload injures the liver, progressing from simple steatosis through steatohepatitis to cirrhosis—now a leading cause of cirrhosis and liver transplantation as obesity and diabetes rise."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Cardiovascular disease, not liver failure, is the leading killer in NASH: the same insulin resistance, dyslipidemia and inflammation that fatten the liver accelerate atherosclerosis, so most NAFLD/NASH patients die of heart disease."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "NASH and hepatitis C are converging causes of chronic liver disease: as antivirals cure HCV, NASH is overtaking it as the leading driver of cirrhosis and liver cancer—both end in fibrosis and HCC, one infectious, one metabolic."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Fibrosis stage drives the prognosis of NASH: fat plus inflammation activates hepatic fibrogenesis, and the degree of liver fibrosis—not the fat or inflammation itself—predicts progression to cirrhosis and death, so antifibrotic effect is the goal of NASH therapy."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance is the engine of NASH: it floods the liver with fatty acids and promotes fat storage and inflammation, so NASH is the hepatic face of the metabolic syndrome—why weight loss and insulin-sensitizing therapy (GLP-1, pioglitazone) treat it."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Hepatic stellate cells are NASH's fibrosis engine: activated by injured hepatocytes and macrophages, they transform into collagen-secreting myofibroblasts, scarring the liver toward cirrhosis—so these fibroblast-like cells are the target of antifibrotic drugs."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "NASH is driven partly from the gut: a dysbiotic, leaky intestine sends bacterial endotoxin and metabolites up the portal vein to inflame the fatty liver, so the gut-liver axis helps turn simple steatosis into progressive steatohepatitis."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid hormone signaling is a NASH drug target: the liver-selective THR-β agonist resmetirom boosts hepatic fat metabolism and became the first FDA-approved NASH therapy, so mimicking thyroid hormone in the liver can reverse steatosis and early fibrosis."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Cholesterol is a hidden driver of NASH: free cholesterol accumulating in hepatocytes is toxic, stressing mitochondria and activating inflammation, so lipotoxicity—not just triglyceride fat—pushes bland fatty liver toward the cell injury that defines steatohepatitis."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "SGLT2 inhibitors help fatty liver: diabetes drugs that flush glucose in urine also reduce liver fat and inflammation in MASH, so they join GLP-1 agonists among metabolic therapies repurposed for the liver disease."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "MASH is defined by what it isn't—alcohol: nonalcoholic steatohepatitis looks histologically like alcoholic liver disease, so diagnosis requires excluding heavy drinking, and the newer 'MetALD' category recognizes patients with both metabolic and alcohol drivers."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "MASH progression is driven partly by cytotoxic T cells: auto-aggressive CD8 T cells accumulate in the fatty liver, killing hepatocytes and fueling inflammation and fibrosis—and they also impair the immune surveillance that would catch emerging liver cancer."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "NASH is steatohepatitis because lipids fire the NLRP3 inflammasome: fat overload and lipotoxic species activate the inflammasome in liver cells, releasing IL-1β that turns harmless fatty liver into the inflammation and fibrosis of NASH."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "NASH often carries excess liver iron: dysmetabolic iron overload accumulates in the fatty liver, and that iron drives oxidative stress that accelerates inflammation and fibrosis—so iron status is part of assessing the disease."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NASH inflammation is tuned by NK and NKT cells: these innate lymphocytes in the liver can both kill stressed hepatocytes and shape the fibrotic response, making them double-edged players in how fatty liver progresses."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "NASH begins in the fat: overloaded, inflamed adipocytes spill free fatty acids and inflammatory adipokines into the blood, flooding the liver with the lipid and signals that ignite the steatohepatitis."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Advanced NASH enlarges the spleen: as fatty liver scars into cirrhosis, portal hypertension backs blood up into the spleen, which swells and traps platelets (hypersplenism), a sign the liver disease has decompensated."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Low oxygen aggravates NASH: pericentral liver cells sit in the most oxygen-poor zone and are first to be injured, and the intermittent hypoxia of sleep apnea—common in these patients—drives faster progression."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "NASH is increasingly staged without a biopsy: ultrasound and MRI photons measure how much fat the liver holds, while elastography reads its stiffness to gauge the fibrosis that matters most."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Most people with NASH die of the heart, not the liver: it travels with the metabolic syndrome, accelerating atherosclerosis so that cardiovascular disease, not cirrhosis, is the leading cause of death."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "When NASH decompensates into cirrhosis, the body retains sodium and water as ascites, and the dilutional low blood sodium that follows marks advanced, failing liver disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the injured liver cell of NASH: large fat droplets swell the hepatocyte, the cytoskeleton clumps into Mallory-Denk bodies, and giant megamitochondria mark the metabolic stress that distinguishes it from simple fatty liver."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Fatty liver disease quietly strains the kidney: NASH is independently linked to chronic kidney disease, the shared insulin resistance and inflammation damaging both organs in parallel beyond the usual diabetes and hypertension."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Low vitamin D shadows fatty liver: deficiency is common in NASH and correlates with more inflammation and fibrosis, reflecting the vitamin's role in insulin sensitivity and restraining the immune injury."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "NASH is staged by its collagen: activated hepatic stellate cells pour collagen into the liver, and how much they have laid down — fibrosis stage F0 to F4 — is the single strongest predictor of whether the disease progresses to cirrhosis."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Once NASH scars into cirrhosis the brain suffers: the failing liver can no longer clear ammonia, which builds up to cause hepatic encephalopathy — confusion, asterixis, and at worst coma."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils mark the 'H' in NASH: their infiltration around ballooned, fat-laden hepatocytes — forming satellitosis and Mallory-Denk bodies — is the lobular inflammation that separates simple fatty liver from true steatohepatitis."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "NASH and PCOS are two faces of insulin resistance: polycystic ovary syndrome sharply raises the risk of fatty liver and steatohepatitis in young women, so the liver and the ovary are screened together when one is found."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Diet is the cornerstone of treatment: cutting fructose and processed food while eating a high-fiber, Mediterranean pattern, with weight loss, can reverse the fat and inflammation of NASH before fibrosis sets in."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "The real killer in NASH is the artery: the same metabolic inflammation injures the endothelial lining and accelerates atherosclerosis, so cardiovascular disease — not the liver — is the leading cause of death in these patients."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammation tips fatty liver into steatohepatitis: Kupffer cells and inflamed fat pour out TNF-α, which worsens hepatocyte insulin resistance, fuels cell death, and recruits the immune attack that turns bland steatosis into NASH."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "The liver's own B cells join the assault: in NASH intrahepatic B cells expand and secrete antibody and cytokines that activate macrophages and stellate cells, pushing inflammation toward fibrosis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Fatty liver shadows the kidney: NASH independently raises the risk of chronic kidney disease through shared insulin resistance, hypertension, and inflammation, so the two metabolic-organ injuries tend to advance together."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "The liver disease kills mostly through the arteries: NASH accelerates atherosclerosis via dyslipidemia and systemic inflammation, so cardiovascular disease — not liver failure — is the leading cause of death in most patients."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "An adipose hormone turns profibrotic: leptin, high in obesity, activates hepatic stellate cells to lay down scar, an adipokine push toward fibrosis that contrasts with the protective adiponectin also released by fat."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflamed fat signals the liver: IL-6 released from expanded adipose tissue worsens hepatic insulin resistance and inflammation, helping drive simple fatty liver onward into steatohepatitis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Fat and gut signals ignite hepatic inflammation: free fatty acids and gut-derived endotoxin activate NF-κB in Kupffer cells and hepatocytes, the master switch that converts bland steatosis into the inflamed, ballooning injury of steatohepatitis."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 links the inflamed liver to cancer: IL-6-driven STAT3 activation in hepatocytes promotes survival and proliferation, a key route by which chronic NASH inflammation gives rise to hepatocellular carcinoma."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Fatty-liver disease tilts the blood toward clotting: NASH raises fibrinogen and PAI-1 and, once cirrhotic, rebalances hemostasis toward thrombosis, increasing the risk of portal vein thrombosis and venous thromboembolism."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "The fatty liver flags a higher colon-cancer risk: NASH and its metabolic milieu are associated with an increased incidence of colorectal cancer and advanced adenomas, a malignancy beyond the liver that the disease tracks with."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The fat-laden liver burdens the heart: NASH is independently linked to heart failure — especially with preserved ejection fraction — through shared insulin resistance, systemic inflammation and a cardiomyopathy of metabolic disease."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Shared metabolic excess raises uric acid: the insulin resistance and fructose metabolism of NASH drive hyperuricemia, so gout frequently accompanies fatty-liver disease as part of the metabolic syndrome cluster."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its metabolic disease reaches the brain's arteries: NASH is an independent marker of systemic atherosclerosis, and cardiovascular and cerebrovascular disease — including ischemic stroke — are leading causes of death in fatty-liver disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "A diseased liver weakens bone: NASH is associated with reduced bone mineral density through chronic inflammation, vitamin D dysregulation and disturbed hepatic-bone signaling, raising fracture risk."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Metabolic disease and mood entwine: NASH carries elevated depression, sharing the inflammation, obesity and insulin resistance of metabolic syndrome, and depression in turn worsens the lifestyle drivers of fatty liver."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It scars the body's metabolic factory: NASH progresses to cirrhosis with portal hypertension, oesophageal varices and ascites, the end-stage liver failure of a digestive organ."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "A failing fatty liver poisons the brain: as NASH cirrhosis decompensates, the liver can no longer clear ammonia and toxins, producing hepatic encephalopathy with confusion and coma."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is the liver face of metabolic disease: NASH is driven by insulin resistance and is tightly linked to type 2 diabetes, polycystic ovary syndrome and hypothyroidism across the endocrine system."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Sleep apnoea feeds it: obstructive sleep apnoea is common in NASH, and its intermittent nocturnal hypoxia independently worsens hepatic inflammation and fibrosis beyond obesity alone."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Lost muscle worsens it: sarcopenia and low muscle mass — sarcopenic obesity — independently accelerate NASH and predict more advanced fibrosis, so preserving muscle is part of management."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Innate immunity drives the inflammation: activation of Kupffer cells and the NLRP3 inflammasome turns simple fatty liver into steatohepatitis, the inflammatory step that defines NASH."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It shows on the skin: acanthosis nigricans signals the insulin resistance behind NASH, and advanced cirrhotic disease brings spider naevi and palmar erythema."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Cirrhosis backs up into the spleen: when NASH progresses to cirrhosis, portal hypertension causes congestive splenomegaly with sequestration of blood cells."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It raises kidney-disease risk: NASH independently increases the risk of chronic kidney disease through the shared insulin resistance and inflammation of metabolic syndrome."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "It targets the metabolic root: although weight loss is primary, metformin improves the insulin resistance that drives non-alcoholic steatohepatitis, often alongside treating coexisting type 2 diabetes."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet remodels the fatty liver: omega-3 fatty acids reduce hepatic triglyceride accumulation and are studied as an adjunct in non-alcoholic fatty liver disease."
  - target: 03-medicine/03-food/curcumin
    relation: connects-to
    note: "An anti-inflammatory spice is studied: curcumin from turmeric shows anti-inflammatory and lipid-lowering effects investigated for steatohepatitis, though its poor absorption limits the effect."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It plays out across the lobule: NASH shows steatosis, hepatocyte ballooning and Mallory bodies with lobular inflammation, and the pericellular 'chicken-wire' fibrosis that progresses toward cirrhosis within the hepatic lobule."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: connects-to
    note: "Cardiovascular risk dominates: most NASH patients die of cardiovascular disease, not liver failure, so statins are both safe and important here, lowering that risk despite the underlying liver disease."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Its liver cancer resists immunotherapy: NASH-driven hepatocellular carcinoma responds worse to PD-1 checkpoint blockade than viral HCC, as the impaired anti-tumour T-cell response of fatty liver blunts immunotherapy."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Its patients die of their arteries: cardiovascular disease, not liver failure, is the leading cause of death in NASH—hepatic insulin resistance, dyslipidaemia and inflammation accelerate arterial-wall atherosclerosis."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "A two-way metabolic loop with the pancreas: hepatic insulin resistance in NASH overworks the islets of Langerhans, and the resulting beta-cell strain and type 2 diabetes in turn worsen the fatty liver."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Shared metabolic-inflammatory ground: NASH and psoriasis cluster within the metabolic syndrome through systemic inflammation, and some psoriasis therapies such as methotrexate are hepatotoxic, complicating an already fatty liver."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Two hits on one liver: coexisting hepatitis B and fatty-liver disease compound hepatocyte injury, accelerating fibrosis and raising hepatocellular-carcinoma risk beyond either alone."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "A heart at risk: NAFLD/NASH independently associates with cardiac structural change—left-ventricular hypertrophy and diastolic dysfunction of the myocardium—beyond the shared metabolic risk factors."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Not only hepatocellular cancer: NASH raises the risk of intrahepatic cholangiocarcinoma as well as hepatocellular carcinoma, broadening the cancer spectrum of the cirrhotic fatty liver."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Fatty liver and atrial fibrillation: NAFLD/NASH independently raises the risk of atrial fibrillation through systemic inflammation and cardiac fibrosis, beyond the metabolic risk factors it shares with arrhythmia."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A metabolic risk amplifier: NAFLD/MAFLD is an independent risk factor for severe COVID-19, its inflammatory, insulin-resistant milieu worsening outcomes during infection."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The gut-liver axis: a leaky intestinal epithelium and dysbiosis deliver bacterial endotoxin to the liver through the portal vein, driving the inflammation that turns simple steatosis into NASH."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hepatic hypoxia: HIF-1α activated in the fatty, poorly perfused liver promotes lipogenesis, inflammation and fibrosis, helping drive the progression of NASH."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Pathological angiogenesis: VEGF-driven aberrant angiogenesis accompanies NASH fibrosis as it advances toward cirrhosis and hepatocellular carcinoma."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Stellate-cell activation: endothelin-1 contracts hepatic stellate cells and contributes to the portal hypertension and fibrosis of advancing NASH."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Fibrogenic mitogen: PDGF is the strongest proliferative signal transdifferentiating hepatic stellate cells into collagen-producing myofibroblasts, the central driver of progressive NASH fibrosis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome injury: IL-1β released downstream of NLRP3 inflammasome activation by lipotoxic hepatocytes amplifies hepatic inflammation and stellate-cell activation in the transition from steatosis to NASH."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Innate DNA sensing: leaked mitochondrial DNA from stressed hepatocytes engages the cGAS-STING pathway in liver macrophages, driving the inflammation and fibrosis that characterise NASH."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Gut-liver axis: a leaky gut delivers bacterial LPS through the portal vein to Kupffer-cell TLR4, igniting the NF-κB-driven inflammation that helps convert simple steatosis into steatohepatitis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Profibrotic target: galectin-3 from activated macrophages promotes hepatic stellate-cell activation and fibrosis in NASH, the rationale for galectin-3 inhibitors (belapectin) tested to halt progression to cirrhosis."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Hepatocyte apoptosis: caspase-mediated hepatocyte apoptosis underlies the ballooning degeneration and cytokeratin-18 release that mark NASH, the basis for pan-caspase inhibitors (emricasan) trialed in the disease."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "FGF21 analogue therapy: FGF21 acting through FGFR1c with β-Klotho improves hepatic fat handling and insulin sensitivity, the rationale for the FGF21-analogue drugs (efruxifermin, pegozafermin) that reduce liver fat and fibrosis in NASH trials."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Dysmetabolic iron overload: many NASH patients accumulate hepatic iron with raised ferritin, and the hepcidin-controlled iron loading adds oxidative stress that aggravates lipotoxic injury and fibrosis, the basis for venesection trials in the disease."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and urate stress: xanthine-oxidase activity in the steatotic liver generates reactive oxygen species and the hyperuricaemia associated with NAFLD, both contributing to the lipotoxic, pro-inflammatory milieu that drives progression to NASH."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Selective insulin resistance: hepatic insulin signalling through AKT (insulin-receptor already mapped) becomes selectively impaired in MASH, so gluconeogenesis escapes suppression while lipogenesis persists — the paradox that fuels steatosis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "Lipogenesis brake: the AMPK energy sensor (the target of the metformin already mapped, activated by adiponectin) restrains hepatic de-novo lipogenesis, and its relative inactivity in MASH permits the fat accumulation that initiates the disease."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative defence: lipotoxic reactive oxygen species in MASH engage the NRF2 antioxidant programme, and inadequate NRF2 defence allows the oxidative hepatocyte injury that drives the progression from steatosis to steatohepatitis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Lipogenesis switch: mTORC1 drives the SREBP-mediated de novo lipogenesis of hepatic steatosis, opposing the AMPK energy sensor (mapped) in the metabolic imbalance that initiates NASH."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Fibrosis effector: TGF-β signals through SMAD4 (TGF-β mapped) to activate hepatic stellate cells, the transcriptional driver of the collagen (mapped) fibrosis that defines progressive NASH."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Gut-liver axis: gut-derived endotoxin engages hepatic TLR4 (mapped) and MyD88 to NF-κB (mapped), the innate-immune signalling that converts steatosis into inflammatory steatohepatitis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Leptin and IL-6 signalling through JAK-STAT3 (STAT3 mapped) links adipose-derived and hepatic inflammation to the progression of steatohepatitis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement activation with C3 deposition in the steatotic liver contributes to the innate inflammatory drive of NASH alongside the TLR4/NLRP3 pathways already mapped."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Hepatic loss of PTEN-restrained PI3K-AKT signalling (AKT and mTOR mapped) promotes lipogenesis and steatosis, linking insulin resistance to fatty-liver disease."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the intrahepatic immune response and the inflammatory progression from steatosis to steatohepatitis in NASH."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling transduces the lipotoxic and growth-factor stimuli that drive hepatocyte stress and the proliferative progression toward hepatocellular carcinoma in NASH."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression contributes to the epigenetic dysregulation underlying the fibrotic progression and hepatocarcinogenesis of NASH."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "Hepatic FOXO1 regulates gluconeogenesis and lipid metabolism, and its dysregulation in insulin resistance drives the steatosis and lipotoxicity of NASH."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by recruited myeloid cells amplify the lobular inflammation that distinguishes NASH from simple steatosis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven cell-cycle activity contributes to the hepatocyte proliferation in the progression toward NASH-related hepatocellular carcinoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the hepatic insulin signaling and inflammatory-fibrotic pathways of non-alcoholic steatohepatitis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic CD8 T and NKT cells contribute to the hepatocyte injury and progression of non-alcoholic steatohepatitis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the hepatic stellate-cell activation driving the fibrosis of non-alcoholic steatohepatitis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of insulin, participates in the hepatic lipogenesis and insulin resistance of non-alcoholic steatohepatitis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy (lipophagy) modulates the hepatocyte lipid handling and survival whose failure contributes to non-alcoholic steatohepatitis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte recruitment amplifies the hepatic inflammation and fibrosis of non-alcoholic steatohepatitis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the hepatocyte and stellate-cell responses of non-alcoholic steatohepatitis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the hepatic-stellate-cell activation and leukocyte recruitment of non-alcoholic steatohepatitis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the hepatic inflammation and fibrogenesis of non-alcoholic steatohepatitis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the hepatic inflammation and fibrosis of NASH."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the hepatic metabolic and fibrotic gene programs of NASH."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the hepatic-stellate-cell activation and fibrosis of NASH."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Fibrogenic signalling: GAS6 activation of the AXL receptor tyrosine kinase drives hepatic stellate cell activation and the fibrosis progression of NASH, and is implicated in the transition to the hepatocellular carcinoma already mapped."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "Cardiovascular mortality: NASH is accompanied by atherogenic dyslipidaemia, and because cardiovascular disease is the leading cause of death in these patients, PCSK9-regulated LDL handling ties the fatty liver to its dominant fatal outcome."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Lipoapoptosis: lipotoxic hepatocyte death is a driver of NASH inflammation, and the balance between anti-apoptotic BCL-2 family proteins and the caspase-3 execution already mapped determines the hepatocyte apoptosis that fuels stellate-cell fibrosis."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac mortality: cardiovascular disease is the leading cause of death in NASH (PCSK9 already mapped), and troponin elevation marks the myocardial injury of the accelerated atherosclerosis that ultimately kills most of these patients."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Insulin resistance: NASH is tightly coupled to pancreatic beta-cell dysfunction and the insulin resistance (insulin already mapped) of the metabolic syndrome, and worsening glucose control accelerates the progression of the fatty liver."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex and menopause: estrogen is hepatoprotective, and its loss after menopause raises the incidence and severity of NASH in women, contributing to the sex differences in fatty liver disease and its progression."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial and portal dysfunction: as NASH progresses to cirrhosis, dysregulated nitric oxide contributes to the intrahepatic endothelial dysfunction and the splanchnic vasodilation of portal hypertension (collagen already mapped for fibrosis)."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "RAAS and fibrosis: aldosterone, part of the renin-angiotensin system, promotes hepatic stellate-cell activation and fibrosis in NASH (TGF-beta already mapped), and it also drives the hypertension of the accompanying metabolic syndrome."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins and related lipid mediators from the inflamed, fat-laden liver contribute to the inflammation of steatohepatitis (IL-6, TNF and IL-1 already mapped), part of the lipotoxic inflammatory injury of NASH."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "The metabolic driver: obesity drives the hepatic steatosis and insulin resistance (leptin, adiponectin and resistin already mapped) that underlie NASH, the liver being the hepatic manifestation of the metabolic syndrome."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Cirrhosis to cancer: NASH cirrhosis is a rapidly rising cause of hepatocellular carcinoma, and NASH-HCC can arise even without cirrhosis, driven by the chronic lipotoxic inflammation (TGF-β already mapped) of the disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Dysmetabolic iron overload: NASH disturbs iron handling (hepcidin already mapped), and the hepatic iron accumulation of the dysmetabolic iron-overload syndrome aggravates the oxidative injury and fibrosis of steatohepatitis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Profibrotic type-2 immunity: IL-4 drives the M2 macrophages (already mapped) and the profibrotic (TGF-β already mapped) type-2 response that contributes to the hepatic-stellate-cell activation and fibrosis of NASH."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Stellate-cell fibrogenesis: IL-13, with IL-4 (already mapped), is a profibrotic type-2 cytokine that activates the hepatic stellate cells to lay down the collagen (already mapped) fibrosis of NASH."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Hepatic copper and steatosis: low hepatic copper is associated with more severe steatosis and NASH, reflecting copper's role in the lipid and antioxidant metabolism of the liver (the Wilson's-disease steatosis being the differential)."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Cardiovascular risk: NASH shares the metabolic-syndrome (cholesterol and PCSK9 already mapped) drivers with the atherosclerosis, the cardiovascular disease being the leading cause of death in NASH."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Chronic-liver zinc: the zinc deficiency common in the chronic liver disease of NASH impairs the hepatic antioxidant and metabolic function."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant selenium: the antioxidant selenoprotein (GPX) defence of the liver; the selenium status modulates the oxidative injury (xanthine oxidase already mapped) of NASH."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate hepatic interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the lipotoxic and mitochondrial stress, contributes to the innate inflammation of the steatohepatitis of NASH."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 hepatic inflammation: the IFN-γ of the intrahepatic T cells (perforin already mapped) is the type-II interferon arm of the immune-mediated inflammation of NASH."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment driving the progression of NASH."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the steatohepatitis of NASH."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-mediated inflammation and fibrosis of NASH."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of NASH."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th17 (IFN-γ and IL-17 already mapped) cytokines that drive the lobular inflammation and the fibrosis of NASH."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Hepatic mast cells: the mast cells accumulate in the fibrosing liver (already mapped) and, via their mediators, promote the stellate-cell (fibroblast already mapped) activation and fibrosis of NASH."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the Kupffer-cell (macrophage already mapped) activation and the lobular inflammation of NASH."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the Kupffer-cell (macrophage already mapped) and myeloid activation of the lobular inflammation of NASH."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-driven inflammation of NASH."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Dysmetabolic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the dysmetabolic hepatic iron overload that aggravates the oxidative injury and fibrosis of NASH."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin gate: TSLP, released from injured hepatocytes and cholangiocytes (already mapped) in NASH, activates the mast cells (already mapped) and dendritic cells (already mapped) that sustain the Type-2-skewed hepatic inflammation driving fibrosis of NASH."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-oedema axis: bradykinin, generated via the kallikrein-kinin system in inflamed liver tissue, increases hepatic sinusoidal permeability and amplifies the macrophage (already mapped) and neutrophil (already mapped) recruitment of NASH."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) over-activation in the inflamed hepatic parenchyma, moderating the immune-mediated hepatocyte injury of NASH."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell effector: histamine, released by mast cells (already mapped) in the portal tract of NASH liver, activates hepatic stellate cells, amplifies the pro-inflammatory cytokine milieu (TNF-α and IL-1β already mapped) and accelerates fibrosis of NASH."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Hepato-protective cytokine: erythropoietin, acting via EPOR on hepatocytes (already mapped) and Kupffer cells (already mapped), suppresses the oxidative stress (ROS already mapped) and TGF-β-driven fibrogenic signalling, attenuating the progressive fibrosis of NASH."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian antioxidant protection: melatonin, via MT1/MT2 receptors on hepatocytes (already mapped), scavenges ROS from dysfunctional mitochondria and inhibits the NF-κB/TNF-α axis (already mapped), moderating the steatoinflammatory injury of NASH."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "NASH testosterone: androgen signalling on hepatocytes (already mapped) attenuates TGF-β (already mapped) fibrogenesis and macrophage (already mapped) lipotoxic activation; testosterone deficiency worsens the steatoinflammatory injury of NASH."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "NASH serotonin: gut-microbiome (already mapped) serotonin promotes hepatic lipogenesis via 5-HT2A receptors on hepatocytes (already mapped); 5-HT also activates macrophage (already mapped) signalling and accelerates the TGF-β (already mapped) fibrotic cascade of NASH."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "NASH prolactin: prolactin, acting via PRLR on hepatocytes (already mapped), promotes hepatic lipid synthesis; prolactin also sensitises the insulin-receptor (already mapped) pathway to the lipotoxic and macrophage (already mapped) inflammatory signals of NASH."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "NASH oxytocin: oxytocin attenuates hepatic NF-κB (already mapped) and TNF-α (already mapped) driven macrophage (already mapped) inflammation and hepatocyte (already mapped) lipotoxicity; oxytocin also suppresses TGF-β (already mapped) mediated hepatic stellate-cell fibrosis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "NASH vasopressin: vasopressin (ADH) via V1b receptor signalling promotes hepatic glycogen release and lipogenesis in hepatocytes (already mapped); vasopressin amplifies NF-κB (already mapped) and IL-6 (already mapped) driven macrophage (already mapped) inflammatory activation."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "NASH iodine: thyroid-hormone deficiency impairs lipid oxidation and amplifies NASH-driven lipotoxicity; iodine deficiency worsens NF-κB (already mapped) and TNF-α (already mapped) driven macrophage (already mapped) inflammatory cascades and TGF-β (already mapped) fibrosis."
---

# NASH

## Overview

**NASH (non-alcoholic steatohepatitis)** — now formally renamed **MASH (metabolic dysfunction-associated steatohepatitis)** in 2023 consensus nomenclature [^rinella-2023-masld-nomenclature] — is the progressive inflammatory subtype of **NAFLD/MASLD (metabolic dysfunction-associated steatotic liver disease)**. NAFLD/MASLD affects approximately **32% of adults globally** (>1.9 billion people), making it the most common chronic liver disease worldwide [^younossi-2016-nafld-epidemiology]. Of those with NAFLD, ~25% develop NASH/MASH, which carries risk of progression to cirrhosis (~15-20% over 20 years) and hepatocellular carcinoma (HCC).

**2023 nomenclature update:**
- NAFLD → **MASLD** (metabolic dysfunction-associated steatotic liver disease)
- NASH → **MASH** (metabolic dysfunction-associated steatohepatitis)
- New cardiometabolic criteria required: steatosis + ≥1 of 5 metabolic risk factors (overweight/obesity, prediabetes/T2DM, hypertension, dyslipidemia, or elevated waist circumference); replaces "non-alcoholic" (exclusion criterion) with a positive metabolic definition
- "NASH" and "NAFLD" terms remain dominant in existing literature and clinical practice; both naming systems are used below

**Disease spectrum:**
- **Simple steatosis (NAFL/MASL):** Hepatic fat ≥5% on biopsy or imaging; minimal inflammation; low risk of progression (<3% → cirrhosis over 20 years); treat underlying metabolic disease
- **NASH/MASH:** Steatosis + hepatocyte ballooning (lipoapoptosis) + lobular inflammation ± fibrosis; NAS (NAFLD Activity Score ≥5) or MASH pattern on biopsy; ~15-20% → cirrhosis; HCC risk increased 5-17× vs. simple steatosis
- **NASH cirrhosis:** Compensated → decompensated (ascites, variceal bleed, hepatic encephalopathy, hepatorenal syndrome); leading indication for liver transplantation in the US alongside alcohol-related liver disease
- **NASH-HCC:** 10-20% of NASH-HCC develops without cirrhosis (non-cirrhotic HCC); distinct biology — more often HCC in metabolically active liver without the cirrhosis-driven regeneration trigger; worse survival due to late diagnosis

**Epidemiology and risk factors:**
- **Obesity:** BMI >30 → NAFLD in ~60-80%; visceral adiposity drives free fatty acid flux to liver (via portal vein from omental fat lipolysis)
- **Type 2 diabetes:** NAFLD in 70-80% of T2DM; NASH in 20-30%; T2DM + NASH → dramatically accelerated fibrosis progression
- **Metabolic syndrome:** Dyslipidemia (elevated TG, low HDL), hypertension — all independently associated
- **Genetic modifiers:** PNPLA3 I148M (patatin-like phospholipase domain containing 3; rs738409) → most common genetic variant affecting NASH susceptibility and fibrosis severity; TM6SF2 E167K → reduced VLDL secretion → hepatic lipid accumulation; HSD17B13 splice variant → protective (associated with reduced fibrosis); MBOAT7 intronic variant → NAFLD risk

## Structure

### Pathophysiology — "Multiple Hit" model

NASH pathogenesis is driven by multiple simultaneous and sequential hits, not a simple two-hit model:

**Hit 1 — Hepatic steatosis (lipid accumulation):**
- **Insulin resistance → lipid flux:** Adipose tissue insulin resistance → unrestrained lipolysis → elevated plasma FFAs → hepatic FFA uptake via CD36 and FATP
- **De novo lipogenesis (DNL):** Hyperinsulinemia → hepatic SREBP-1c activation → fatty acid synthase (FASN), acetyl-CoA carboxylase (ACC) → palmitate and other saturated FAs; fructose (from fructose-sweetened beverages) → hepatic DNL via ChREBP → triglyceride accumulation
- **Impaired VLDL secretion:** Reduced apoB100 lipidation → failed triglyceride export from hepatocytes → lipid trapping; TM6SF2 and APOB variants
- **Dietary FFA input:** Saturated FAs from diet → direct hepatic lipotoxicity

**Hit 2 — Lipotoxic hepatocyte injury:**
- **Saturated FFAs (palmitate, stearate):** Trigger ER stress (UPR: IRE1alpha, PERK, ATF6) → CHOP → hepatocyte apoptosis; also increase ceramide and diacylglycerol (DAG) → PKCε activation → IRS-1 serine phosphorylation → further insulin resistance (lipotoxicity-insulin resistance loop)
- **Mitochondrial dysfunction:** Excess FFA → beta-oxidation saturation → incomplete oxidation → ROS, lipid peroxidation products (4-HNE, MDA) → mitochondrial DNA damage → impaired OXPHOS → energy deficit → hepatocyte injury
- **Ballooning degeneration:** Swollen pale hepatocytes with Mallory-Denk bodies (ubiquitinated K8/K18 aggregates + p62) → histological hallmark of NASH; ballooned hepatocytes release DAMPs (HMGB1, mtDNA, extracellular vesicles)

**Hit 3 — Inflammatory amplification:**
- Lipotoxic DAMPs → activate Kupffer cells via TLR4, TLR9, NLRP3 → IL-1beta, IL-6, TNF-alpha → hepatocyte injury amplification; gut microbiome-derived LPS (via leaky gut / increased intestinal permeability → portal LPS) → TLR4-driven Kupffer cell activation (gut-liver axis)
- **Recruited monocytes/macrophages:** CXCL2/CCL2 → circulating monocytes infiltrate liver → differentiate into inflammatory macrophages → amplify IL-6, TNF-alpha, IL-1beta → hepatocyte necroapoptosis → stellate cell activation
- **NLRP3 inflammasome:** Lipotoxicity → NLRP3 → caspase-1 → IL-1beta → fibrogenic and inflammatory amplification in Kupffer cells; emerging therapeutic target in NASH (selnoflast, a covalent NLRP3 inhibitor, in NASH trials)

**Hit 4 — Hepatic fibrosis (stellate cell activation):**
- Lipotoxic hepatocytes → paracrine signals (TGF-beta1, PDGF, SHH, CXCL16) → hepatic stellate cells (HSCs) activation → loss of lipid droplets → myofibroblast phenotype (alpha-SMA+) → collagen I/III/IV deposition → fibrosis
- **Fibrosis stages (NASH):** F0 (none), F1 (perisinusoidal or periportal), F2 (perisinusoidal + periportal), F3 (bridging), F4 (cirrhosis); liver-related mortality rises sharply at F3-F4
- **HSC activation pathways:** TGF-beta1 → SMAD2/3 → alpha-SMA, type I collagen gene transcription; PDGF → HSC proliferation; Hedgehog (SHH from hepatocytes) → HSC survival and fibrogenesis

## Function

### Clinical presentation

**Symptoms:** Predominantly asymptomatic until advanced fibrosis or cirrhosis; may present with right upper quadrant discomfort, fatigue, or incidentally on imaging (hepatic steatosis on US/CT/MRI)

## Pathology

### Diagnosis

**Non-invasive assessment:**
- **Liver function tests:** ALT elevated in NASH (but can be normal in cirrhosis); AST:ALT ratio >1 → advanced fibrosis (hepatic reserve depleted); GGT elevation (lipotoxicity, oxidative stress)
- **FibroScan (transient elastography):** Liver stiffness (kPa) → fibrosis staging; controlled attenuation parameter (CAP) → steatosis grade; FDA-cleared, widely used first-line assessment
- **MRI-PDFF (proton density fat fraction):** Gold standard non-invasive steatosis quantification; MR elastography (MRE) → fibrosis
- **Serum biomarkers:** FIB-4 score (age × AST / [platelets × ALT^0.5]) → fibrosis risk; NAFLD Fibrosis Score; ELF (Enhanced Liver Fibrosis) panel (P3NP, TIMP1, HA) → advanced fibrosis; PRO-C3 (type III collagen neoepitope) → fibrogenesis activity
- **Liver biopsy (gold standard):** NAS scoring: steatosis (0-3), lobular inflammation (0-3), hepatocyte ballooning (0-2); NAS ≥5 = NASH; fibrosis stage (0-4) assessed separately via Brunt/NASH CRN criteria; reserved for uncertain diagnosis, clinical trials, or pre-treatment fibrosis staging

**HCC surveillance:**
- Every 6 months ultrasound ± AFP in NASH cirrhosis; non-cirrhotic NASH-HCC surveillance less well-defined; MRI preferred over US in obese patients (poor US penetration)

### Treatment [^harrison-2024-resmetirom]

**Lifestyle modification (foundation of all NASH treatment):**
- **Weight loss:** 7-10% body weight loss → NASH resolution in ~50%; ≥10% → significant fibrosis regression; Mediterranean diet reduces hepatic fat independent of calories; structured exercise (aerobic + resistance) reduces hepatic lipid even without weight loss
- **Bariatric surgery:** Most effective intervention for morbidly obese NASH; Roux-en-Y gastric bypass or sleeve gastrectomy → 80-90% NASH resolution, significant fibrosis regression; also reduces T2DM, cardiovascular events; dedicated NASH bariatric trials ongoing

**Pharmacological — approved (2024):**

- **Resmetirom (Rezdiffra, THR-beta agonist):** FDA approved March 2024 — first NASH-specific pharmacological treatment; selective thyroid hormone receptor beta (THR-beta) agonist → liver-specific thyroid receptor activation → reduced DNL, increased beta-oxidation, reduced liver fat; MAESTRO-NASH Phase 3: 25.9% NASH resolution + ≥1 fibrosis stage improvement (vs. 9.7% placebo) at week 52; 24.2% ≥1 fibrosis improvement vs. 14.2% placebo; approved for adults with NASH/MASH + moderate-severe fibrosis (F2-F3) [^harrison-2024-resmetirom]
- **Semaglutide (Ozempic, Wegovy — GLP-1 agonist):** FDA approved for T2DM and obesity; NASH sub-study (PIONEER and ESSENCE-NASH): 59% NASH resolution at week 72 (vs. 17% placebo) but no significant fibrosis benefit in Phase 2; ESSENCE-NASH (Phase 3) in progress — largest NASH trial; semaglutide reduces body weight, hepatic DNL via GLP-1R activation, and improves insulin sensitivity; also reduces MACE in T2DM patients with established CVD (SUSTAIN-6, SELECT trials) — directly addresses the leading cause of death in NASH (cardiovascular disease)

**Pharmacological — investigational:**
- **Lanifibranor (PPAR-alpha/gamma/delta pan-agonist):** NATIVE trial (Phase 2b): significant improvement in NAS and fibrosis; Phase 3 NATIV3 ongoing
- **Obeticholic acid (OCA, FXR agonist):** REGENERATE trial: improvement in fibrosis at 18 months but no sustained benefit at 48 months; FDA declined approval due to safety (pruritus, LDL elevation) and limited efficacy; not currently approved
- **Selnoflast, DFV890 (NLRP3 inhibitors):** Phase 2 in NASH; mechanistically promising (inflammasome-fibrosis connection)
- **Combinations:** Semaglutide + resmetirom, semaglutide + ACC inhibitors — targeting multiple pathways simultaneously

## Connections

- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta is the primary pro-fibrogenic signal in NASH: macrophage- and hepatocyte-derived TGF-beta → hepatic stellate cell activation → alpha-SMA and collagen I deposition → fibrosis and cirrhosis; TGF-beta also promotes hepatocyte EMT and NASH-HCC progression.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Kupffer cells and recruited monocytes drive NASH: LPS-TLR4 → NF-kB → TNF-alpha, IL-1beta, IL-6 → hepatocyte injury and stellate cell activation; M1 macrophage polarization correlates with NASH histological activity; macrophage depletion attenuates experimental NASH fibrosis.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Hepatocytes are the primary NASH target: lipid overload → ER stress, mitochondrial dysfunction, ROS → hepatocyte ballooning and lipoapoptosis; dying hepatocytes release DAMPs → Kupffer cell activation; hepatocyte SREBP-1c drives lipogenesis under insulin resistance.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — Hepatic insulin resistance is the core NASH driver: impaired insulin signaling → failure to suppress hepatic glucose output and VLDL; hyperinsulinemia → SREBP-1c → de novo lipogenesis → steatosis and lipotoxicity; GLP-1 agonists and PPAR-gamma agonists improve insulin sensitivity.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Semaglutide resolved NASH histology in 59% vs 17% placebo (Phase 2); GLP-1R activation reduces hepatic lipogenesis, liver inflammation, and oxidative stress; semaglutide ESSENCE Phase 3 NASH trial is ongoing; GLP-1R agonists are promising disease-modifying agents for NASH.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — adiponectin deficiency impairs hepatic AMPK → reduced fatty acid oxidation → steatosis; adiponectin suppresses TNF-α and NF-κB in Kupffer cells → reduced hepatic inflammation; pioglitazone (PPARγ agonist) raises adiponectin, reduces NASH steatohepatitis, and slows fibrosis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Resistin (primarily monocyte/macrophage-derived in humans) activates NF-κB in Kupffer cells → TNF-α and IL-6 → NASH inflammation; resistin correlates with NASH histological severity; resistin inhibits adiponectin → impairs hepatic AMPK → steatosis and fibrosis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Hepatocyte lipotoxicity + DAMPs → Kupffer cell CCL2; elevated hepatic CCL2 → CCR2+ monocyte-derived macrophage recruitment → NLRP3 → IL-1β + TNF-α → stellate cell activation → fibrosis; cenicriviroc (CCR2/CCR5 dual antagonist) studied in CENTAUR/AURORA trials.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10 from Kupffer cells and hepatic Tregs restrains NLRP3 inflammasome activation and stellate cell activation in NASH; IL-10 KO mice develop spontaneous steatohepatitis on high-fat diet; IL-10 deficiency correlates with fibrosis stage in human NASH biopsies.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — TGF-β1 → periostin in hepatic stellate cells → integrin αvβ3 → FAK/PI3K → collagen I/III deposition → hepatic fibrosis in NASH; periostin correlates with fibrosis stage; periostin-null mice develop less hepatic fibrosis in NASH models; periostin marks activated stellate cells.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — EDA-FN is upregulated in NASH liver via TGF-β1 → activates integrin α4β7 and TLR4 on HSCs → myofibroblast differentiation → collagen I/III → hepatic fibrosis; serum EDA-FN correlates with NASH fibrosis stage; FN matrix stiffness amplifies TGF-β activation in fibrotic liver.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — NASH is the hepatic face of type 2 diabetes and metabolic syndrome: insulin resistance floods the liver with fatty acids and drives lipotoxic inflammation, so most NASH patients are diabetic or pre-diabetic, and the two accelerate each other toward cirrhosis.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity is the leading driver of NASH: excess visceral fat delivers free fatty acids and inflammatory adipokines to the liver, causing steatosis that progresses to steatohepatitis—so weight loss (diet, GLP-1 agonists, bariatric surgery) is the most effective treatment.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — NASH is now a leading cause of hepatocellular carcinoma: chronic steatohepatitis drives fibrosis and cirrhosis that can become liver cancer—and uniquely, NASH-related HCC can arise even without cirrhosis, so rising fatty-liver prevalence is reshaping HCC epidemiology.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — NASH is the inflammatory, fibrosing form of fatty liver disease: metabolic overload injures the liver, progressing from simple steatosis through steatohepatitis to cirrhosis—now a leading cause of cirrhosis and liver transplantation as obesity and diabetes rise.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Cardiovascular disease, not liver failure, is the leading killer in NASH: the same insulin resistance, dyslipidemia and inflammation that fatten the liver accelerate atherosclerosis, so most NAFLD/NASH patients die of heart disease.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — NASH and hepatitis C are converging causes of chronic liver disease: as antivirals cure HCV, NASH is overtaking it as the leading driver of cirrhosis and liver cancer—both end in fibrosis and HCC, one infectious, one metabolic.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Fibrosis stage drives the prognosis of NASH: fat plus inflammation activates hepatic fibrogenesis, and the degree of liver fibrosis—not the fat or inflammation itself—predicts progression to cirrhosis and death, so antifibrotic effect is the goal of NASH therapy.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance is the engine of NASH: it floods the liver with fatty acids and promotes fat storage and inflammation, so NASH is the hepatic face of the metabolic syndrome—why weight loss and insulin-sensitizing therapy (GLP-1, pioglitazone) treat it.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Hepatic stellate cells are NASH's fibrosis engine: activated by injured hepatocytes and macrophages, they transform into collagen-secreting myofibroblasts, scarring the liver toward cirrhosis—so these fibroblast-like cells are the target of antifibrotic drugs.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — NASH is driven partly from the gut: a dysbiotic, leaky intestine sends bacterial endotoxin and metabolites up the portal vein to inflame the fatty liver, so the gut-liver axis helps turn simple steatosis into progressive steatohepatitis.
- `connects-to` → **[Thyroid Hormones (T3/T4)](../../03-molecular/thyroid-hormones/README.md)** — Thyroid hormone signaling is a NASH drug target: the liver-selective THR-β agonist resmetirom boosts hepatic fat metabolism and became the first FDA-approved NASH therapy, so mimicking thyroid hormone in the liver can reverse steatosis and early fibrosis.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cholesterol is a hidden driver of NASH: free cholesterol accumulating in hepatocytes is toxic, stressing mitochondria and activating inflammation, so lipotoxicity—not just triglyceride fat—pushes bland fatty liver toward the cell injury that defines steatohepatitis.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — SGLT2 inhibitors help fatty liver: diabetes drugs that flush glucose in urine also reduce liver fat and inflammation in MASH, so they join GLP-1 agonists among metabolic therapies repurposed for the liver disease.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — MASH is defined by what it isn't—alcohol: nonalcoholic steatohepatitis looks histologically like alcoholic liver disease, so diagnosis requires excluding heavy drinking, and the newer 'MetALD' category recognizes patients with both metabolic and alcohol drivers.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — MASH progression is driven partly by cytotoxic T cells: auto-aggressive CD8 T cells accumulate in the fatty liver, killing hepatocytes and fueling inflammation and fibrosis—and they also impair the immune surveillance that would catch emerging liver cancer.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — NASH is steatohepatitis because lipids fire the NLRP3 inflammasome: fat overload and lipotoxic species activate the inflammasome in liver cells, releasing IL-1β that turns harmless fatty liver into the inflammation and fibrosis of NASH.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — NASH often carries excess liver iron: dysmetabolic iron overload accumulates in the fatty liver, and that iron drives oxidative stress that accelerates inflammation and fibrosis—so iron status is part of assessing the disease.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — NASH inflammation is tuned by NK and NKT cells: these innate lymphocytes in the liver can both kill stressed hepatocytes and shape the fibrotic response, making them double-edged players in how fatty liver progresses.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — NASH begins in the fat: overloaded, inflamed adipocytes spill free fatty acids and inflammatory adipokines into the blood, flooding the liver with the lipid and signals that ignite the steatohepatitis.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Advanced NASH enlarges the spleen: as fatty liver scars into cirrhosis, portal hypertension backs blood up into the spleen, which swells and traps platelets (hypersplenism), a sign the liver disease has decompensated.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Low oxygen aggravates NASH: pericentral liver cells sit in the most oxygen-poor zone and are first to be injured, and the intermittent hypoxia of sleep apnea—common in these patients—drives faster progression.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — NASH is increasingly staged without a biopsy: ultrasound and MRI photons measure how much fat the liver holds, while elastography reads its stiffness to gauge the fibrosis that matters most.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Most people with NASH die of the heart, not the liver: it travels with the metabolic syndrome, accelerating atherosclerosis so that cardiovascular disease, not cirrhosis, is the leading cause of death.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — When NASH decompensates into cirrhosis, the body retains sodium and water as ascites, and the dilutional low blood sodium that follows marks advanced, failing liver disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the injured liver cell of NASH: large fat droplets swell the hepatocyte, the cytoskeleton clumps into Mallory-Denk bodies, and giant megamitochondria mark the metabolic stress that distinguishes it from simple fatty liver.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Fatty liver disease quietly strains the kidney: NASH is independently linked to chronic kidney disease, the shared insulin resistance and inflammation damaging both organs in parallel beyond the usual diabetes and hypertension.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Low vitamin D shadows fatty liver: deficiency is common in NASH and correlates with more inflammation and fibrosis, reflecting the vitamin's role in insulin sensitivity and restraining the immune injury.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — NASH is staged by its collagen: activated hepatic stellate cells pour collagen into the liver, and how much they have laid down — fibrosis stage F0 to F4 — is the single strongest predictor of whether the disease progresses to cirrhosis.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Once NASH scars into cirrhosis the brain suffers: the failing liver can no longer clear ammonia, which builds up to cause hepatic encephalopathy — confusion, asterixis, and at worst coma.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils mark the 'H' in NASH: their infiltration around ballooned, fat-laden hepatocytes — forming satellitosis and Mallory-Denk bodies — is the lobular inflammation that separates simple fatty liver from true steatohepatitis.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — NASH and PCOS are two faces of insulin resistance: polycystic ovary syndrome sharply raises the risk of fatty liver and steatohepatitis in young women, so the liver and the ovary are screened together when one is found.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Diet is the cornerstone of treatment: cutting fructose and processed food while eating a high-fiber, Mediterranean pattern, with weight loss, can reverse the fat and inflammation of NASH before fibrosis sets in.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — The real killer in NASH is the artery: the same metabolic inflammation injures the endothelial lining and accelerates atherosclerosis, so cardiovascular disease — not the liver — is the leading cause of death in these patients.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammation tips fatty liver into steatohepatitis: Kupffer cells and inflamed fat pour out TNF-α, which worsens hepatocyte insulin resistance, fuels cell death, and recruits the immune attack that turns bland steatosis into NASH.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — The liver's own B cells join the assault: in NASH intrahepatic B cells expand and secrete antibody and cytokines that activate macrophages and stellate cells, pushing inflammation toward fibrosis.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Fatty liver shadows the kidney: NASH independently raises the risk of chronic kidney disease through shared insulin resistance, hypertension, and inflammation, so the two metabolic-organ injuries tend to advance together.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — The liver disease kills mostly through the arteries: NASH accelerates atherosclerosis via dyslipidemia and systemic inflammation, so cardiovascular disease — not liver failure — is the leading cause of death in most patients.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — An adipose hormone turns profibrotic: leptin, high in obesity, activates hepatic stellate cells to lay down scar, an adipokine push toward fibrosis that contrasts with the protective adiponectin also released by fat.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflamed fat signals the liver: IL-6 released from expanded adipose tissue worsens hepatic insulin resistance and inflammation, helping drive simple fatty liver onward into steatohepatitis.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Fat and gut signals ignite hepatic inflammation: free fatty acids and gut-derived endotoxin activate NF-κB in Kupffer cells and hepatocytes, the master switch that converts bland steatosis into the inflamed, ballooning injury of steatohepatitis.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 links the inflamed liver to cancer: IL-6-driven STAT3 activation in hepatocytes promotes survival and proliferation, a key route by which chronic NASH inflammation gives rise to hepatocellular carcinoma.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Fatty-liver disease tilts the blood toward clotting: NASH raises fibrinogen and PAI-1 and, once cirrhotic, rebalances hemostasis toward thrombosis, increasing the risk of portal vein thrombosis and venous thromboembolism.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — The fatty liver flags a higher colon-cancer risk: NASH and its metabolic milieu are associated with an increased incidence of colorectal cancer and advanced adenomas, a malignancy beyond the liver that the disease tracks with.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The fat-laden liver burdens the heart: NASH is independently linked to heart failure — especially with preserved ejection fraction — through shared insulin resistance, systemic inflammation and a cardiomyopathy of metabolic disease.
- `connects-to` → **[Gout](../gout/README.md)** — Shared metabolic excess raises uric acid: the insulin resistance and fructose metabolism of NASH drive hyperuricemia, so gout frequently accompanies fatty-liver disease as part of the metabolic syndrome cluster.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its metabolic disease reaches the brain's arteries: NASH is an independent marker of systemic atherosclerosis, and cardiovascular and cerebrovascular disease — including ischemic stroke — are leading causes of death in fatty-liver disease.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — A diseased liver weakens bone: NASH is associated with reduced bone mineral density through chronic inflammation, vitamin D dysregulation and disturbed hepatic-bone signaling, raising fracture risk.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Metabolic disease and mood entwine: NASH carries elevated depression, sharing the inflammation, obesity and insulin resistance of metabolic syndrome, and depression in turn worsens the lifestyle drivers of fatty liver.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It scars the body's metabolic factory: NASH progresses to cirrhosis with portal hypertension, oesophageal varices and ascites, the end-stage liver failure of a digestive organ.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — A failing fatty liver poisons the brain: as NASH cirrhosis decompensates, the liver can no longer clear ammonia and toxins, producing hepatic encephalopathy with confusion and coma.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is the liver face of metabolic disease: NASH is driven by insulin resistance and is tightly linked to type 2 diabetes, polycystic ovary syndrome and hypothyroidism across the endocrine system.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Sleep apnoea feeds it: obstructive sleep apnoea is common in NASH, and its intermittent nocturnal hypoxia independently worsens hepatic inflammation and fibrosis beyond obesity alone.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Lost muscle worsens it: sarcopenia and low muscle mass — sarcopenic obesity — independently accelerate NASH and predict more advanced fibrosis, so preserving muscle is part of management.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Innate immunity drives the inflammation: activation of Kupffer cells and the NLRP3 inflammasome turns simple fatty liver into steatohepatitis, the inflammatory step that defines NASH.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It shows on the skin: acanthosis nigricans signals the insulin resistance behind NASH, and advanced cirrhotic disease brings spider naevi and palmar erythema.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Cirrhosis backs up into the spleen: when NASH progresses to cirrhosis, portal hypertension causes congestive splenomegaly with sequestration of blood cells.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It raises kidney-disease risk: NASH independently increases the risk of chronic kidney disease through the shared insulin resistance and inflammation of metabolic syndrome.
- `connects-to` → **[Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — It targets the metabolic root: although weight loss is primary, metformin improves the insulin resistance that drives non-alcoholic steatohepatitis, often alongside treating coexisting type 2 diabetes.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet remodels the fatty liver: omega-3 fatty acids reduce hepatic triglyceride accumulation and are studied as an adjunct in non-alcoholic fatty liver disease.
- `connects-to` → **[Curcumin](../../../03-medicine/03-food/curcumin/README.md)** — An anti-inflammatory spice is studied: curcumin from turmeric shows anti-inflammatory and lipid-lowering effects investigated for steatohepatitis, though its poor absorption limits the effect.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It plays out across the lobule: NASH shows steatosis, hepatocyte ballooning and Mallory bodies with lobular inflammation, and the pericellular 'chicken-wire' fibrosis that progresses toward cirrhosis within the hepatic lobule.
- `connects-to` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — Cardiovascular risk dominates: most NASH patients die of cardiovascular disease, not liver failure, so statins are both safe and important here, lowering that risk despite the underlying liver disease.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Its liver cancer resists immunotherapy: NASH-driven hepatocellular carcinoma responds worse to PD-1 checkpoint blockade than viral HCC, as the impaired anti-tumour T-cell response of fatty liver blunts immunotherapy.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Its patients die of their arteries: cardiovascular disease, not liver failure, is the leading cause of death in NASH—hepatic insulin resistance, dyslipidaemia and inflammation accelerate arterial-wall atherosclerosis.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — A two-way metabolic loop with the pancreas: hepatic insulin resistance in NASH overworks the islets of Langerhans, and the resulting beta-cell strain and type 2 diabetes in turn worsen the fatty liver.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Shared metabolic-inflammatory ground: NASH and psoriasis cluster within the metabolic syndrome through systemic inflammation, and some psoriasis therapies such as methotrexate are hepatotoxic, complicating an already fatty liver.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Two hits on one liver: coexisting hepatitis B and fatty-liver disease compound hepatocyte injury, accelerating fibrosis and raising hepatocellular-carcinoma risk beyond either alone.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — A heart at risk: NAFLD/NASH independently associates with cardiac structural change—left-ventricular hypertrophy and diastolic dysfunction of the myocardium—beyond the shared metabolic risk factors.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Not only hepatocellular cancer: NASH raises the risk of intrahepatic cholangiocarcinoma as well as hepatocellular carcinoma, broadening the cancer spectrum of the cirrhotic fatty liver.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Fatty liver and atrial fibrillation: NAFLD/NASH independently raises the risk of atrial fibrillation through systemic inflammation and cardiac fibrosis, beyond the metabolic risk factors it shares with arrhythmia.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A metabolic risk amplifier: NAFLD/MAFLD is an independent risk factor for severe COVID-19, its inflammatory, insulin-resistant milieu worsening outcomes during infection.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The gut-liver axis: a leaky intestinal epithelium and dysbiosis deliver bacterial endotoxin to the liver through the portal vein, driving the inflammation that turns simple steatosis into NASH.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hepatic hypoxia: HIF-1α activated in the fatty, poorly perfused liver promotes lipogenesis, inflammation and fibrosis, helping drive the progression of NASH.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Pathological angiogenesis: VEGF-driven aberrant angiogenesis accompanies NASH fibrosis as it advances toward cirrhosis and hepatocellular carcinoma.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Stellate-cell activation: endothelin-1 contracts hepatic stellate cells and contributes to the portal hypertension and fibrosis of advancing NASH.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Fibrogenic mitogen: PDGF is the strongest proliferative signal transdifferentiating hepatic stellate cells into collagen-producing myofibroblasts, the central driver of progressive NASH fibrosis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammasome injury: IL-1β released downstream of NLRP3 inflammasome activation by lipotoxic hepatocytes amplifies hepatic inflammation and stellate-cell activation in the transition from steatosis to NASH.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Innate DNA sensing: leaked mitochondrial DNA from stressed hepatocytes engages the cGAS-STING pathway in liver macrophages, driving the inflammation and fibrosis that characterise NASH.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — A leaky gut delivers bacterial LPS through the portal vein to Kupffer-cell TLR4, igniting the NF-κB-driven inflammation that helps convert simple steatosis into steatohepatitis—the gut-liver axis of NASH pathogenesis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 from activated macrophages promotes hepatic stellate-cell activation and fibrosis in NASH, the rationale for galectin-3 inhibitors such as belapectin tested to halt the progression toward cirrhosis and portal hypertension.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-mediated hepatocyte apoptosis underlies the ballooning degeneration and cytokeratin-18 release that mark NASH histologically, the basis for the pan-caspase inhibitors (emricasan) trialed to slow hepatocyte loss and fibrosis.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGF21 acting through FGFR1c with β-Klotho improves hepatic fat handling and insulin sensitivity, the rationale for the FGF21-analogue drugs (efruxifermin, pegozafermin) that reduce liver fat and fibrosis in NASH trials.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Many NASH patients accumulate hepatic iron with raised ferritin, and the hepcidin-controlled iron loading adds oxidative stress that aggravates lipotoxic injury and fibrosis, the basis for venesection trials in the disease.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Xanthine-oxidase activity in the steatotic liver generates reactive oxygen species and the hyperuricemia associated with NAFLD, both contributing to the lipotoxic, pro-inflammatory milieu that drives progression to NASH.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Hepatic insulin signaling through AKT (insulin-receptor already mapped) becomes selectively impaired in MASH, so gluconeogenesis escapes suppression while lipogenesis persists—the paradox that fuels steatosis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — The AMPK energy sensor (the target of the metformin already mapped, activated by adiponectin) restrains hepatic de-novo lipogenesis, and its relative inactivity in MASH permits the fat accumulation that initiates the disease.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Lipotoxic reactive oxygen species in MASH engage the NRF2 antioxidant program, and inadequate NRF2 defense allows the oxidative hepatocyte injury that drives the progression from steatosis to steatohepatitis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTORC1 drives the SREBP-mediated de novo lipogenesis of hepatic steatosis, opposing the AMPK energy sensor (mapped) in the metabolic imbalance that initiates NASH.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β signals through SMAD4 (TGF-β mapped) to activate hepatic stellate cells, the transcriptional driver of the collagen (mapped) fibrosis that defines progressive NASH.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Gut-derived endotoxin engages hepatic TLR4 (mapped) and MyD88 to NF-κB (mapped), the innate-immune signaling that converts steatosis into inflammatory steatohepatitis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Leptin and IL-6 signaling through JAK-STAT3 (STAT3 mapped) links adipose-derived and hepatic inflammation to the progression of steatohepatitis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation with C3 deposition in the steatotic liver contributes to the innate inflammatory drive of NASH alongside the TLR4/NLRP3 pathways already mapped.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Hepatic loss of PTEN-restrained PI3K-AKT signaling (AKT and mTOR mapped) promotes lipogenesis and steatosis, linking insulin resistance to fatty-liver disease.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the intrahepatic immune response and the inflammatory progression from steatosis to steatohepatitis in NASH.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling transduces the lipotoxic and growth-factor stimuli that drive hepatocyte stress and the proliferative progression toward hepatocellular carcinoma in NASH.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression contributes to the epigenetic dysregulation underlying the fibrotic progression and hepatocarcinogenesis of NASH.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — Hepatic FOXO1 regulates gluconeogenesis and lipid metabolism, and its dysregulation in insulin resistance drives the steatosis and lipotoxicity of NASH.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by recruited myeloid cells amplify the lobular inflammation that distinguishes NASH from simple steatosis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven cell-cycle activity contributes to the hepatocyte proliferation in the progression toward NASH-related hepatocellular carcinoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the hepatic insulin signaling and inflammatory-fibrotic pathways of non-alcoholic steatohepatitis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic CD8 T and NKT cells contribute to the hepatocyte injury and progression of non-alcoholic steatohepatitis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the hepatic stellate-cell activation driving the fibrosis of non-alcoholic steatohepatitis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of insulin, participates in the hepatic lipogenesis and insulin resistance of non-alcoholic steatohepatitis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy (lipophagy) modulates the hepatocyte lipid handling and survival whose failure contributes to non-alcoholic steatohepatitis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte recruitment amplifies the hepatic inflammation and fibrosis of non-alcoholic steatohepatitis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the hepatocyte and stellate-cell responses of non-alcoholic steatohepatitis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the hepatic-stellate-cell activation and leukocyte recruitment of non-alcoholic steatohepatitis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the hepatic inflammation and fibrogenesis of non-alcoholic steatohepatitis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the hepatic inflammation and fibrosis of NASH.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the hepatic metabolic and fibrotic gene programs of NASH.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the hepatic-stellate-cell activation and fibrosis of NASH.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Fibrogenic signalling: GAS6 activation of the AXL receptor tyrosine kinase drives hepatic stellate cell activation and the fibrosis progression of NASH, and is implicated in the transition to the hepatocellular carcinoma already mapped.
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — Cardiovascular mortality: NASH is accompanied by atherogenic dyslipidaemia, and because cardiovascular disease is the leading cause of death in these patients, PCSK9-regulated LDL handling ties the fatty liver to its dominant fatal outcome.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Lipoapoptosis: lipotoxic hepatocyte death is a driver of NASH inflammation, and the balance between anti-apoptotic BCL-2 family proteins and the caspase-3 execution already mapped determines the hepatocyte apoptosis that fuels stellate-cell fibrosis.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac mortality: cardiovascular disease is the leading cause of death in NASH (PCSK9 already mapped), and troponin elevation marks the myocardial injury of the accelerated atherosclerosis that ultimately kills most of these patients.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Insulin resistance: NASH is tightly coupled to pancreatic beta-cell dysfunction and the insulin resistance (insulin already mapped) of the metabolic syndrome, and worsening glucose control accelerates the progression of the fatty liver.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex and menopause: estrogen is hepatoprotective, and its loss after menopause raises the incidence and severity of NASH in women, contributing to the sex differences in fatty liver disease and its progression.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial and portal dysfunction: as NASH progresses to cirrhosis, dysregulated nitric oxide contributes to the intrahepatic endothelial dysfunction and the splanchnic vasodilation of portal hypertension (collagen already mapped for fibrosis).
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — RAAS and fibrosis: aldosterone, part of the renin-angiotensin system, promotes hepatic stellate-cell activation and fibrosis in NASH (TGF-beta already mapped), and it also drives the hypertension of the accompanying metabolic syndrome.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins and related lipid mediators from the inflamed, fat-laden liver contribute to the inflammation of steatohepatitis (IL-6, TNF and IL-1 already mapped), part of the lipotoxic inflammatory injury of NASH.
- `connects-to` → **[Obesity](../obesity/README.md)** — The metabolic driver: obesity drives the hepatic steatosis and insulin resistance (leptin, adiponectin and resistin already mapped) that underlie NASH, the liver being the hepatic manifestation of the metabolic syndrome.
- `connects-to` → **[HCC](../hcc/README.md)** — Cirrhosis to cancer: NASH cirrhosis is a rapidly rising cause of hepatocellular carcinoma, and NASH-HCC can arise even without cirrhosis, driven by the chronic lipotoxic inflammation (TGF-β already mapped) of the disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Dysmetabolic iron overload: NASH disturbs iron handling (hepcidin already mapped), and the hepatic iron accumulation of the dysmetabolic iron-overload syndrome aggravates the oxidative injury and fibrosis of steatohepatitis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Profibrotic type-2 immunity: IL-4 drives the M2 macrophages (already mapped) and the profibrotic (TGF-β already mapped) type-2 response that contributes to the hepatic-stellate-cell activation and fibrosis of NASH.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Stellate-cell fibrogenesis: IL-13, with IL-4 (already mapped), is a profibrotic type-2 cytokine that activates the hepatic stellate cells to lay down the collagen (already mapped) fibrosis of NASH.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Hepatic copper and steatosis: low hepatic copper is associated with more severe steatosis and NASH, reflecting copper's role in the lipid and antioxidant metabolism of the liver (the Wilson's-disease steatosis being the differential).
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Cardiovascular risk: NASH shares the metabolic-syndrome (cholesterol and PCSK9 already mapped) drivers with the atherosclerosis, the cardiovascular disease being the leading cause of death in NASH.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Chronic-liver zinc: the zinc deficiency common in the chronic liver disease of NASH impairs the hepatic antioxidant and metabolic function.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant selenium: the antioxidant selenoprotein (GPX) defence of the liver; the selenium status modulates the oxidative injury (xanthine oxidase already mapped) of NASH.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate hepatic interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the lipotoxic and mitochondrial stress, contributes to the innate inflammation of the steatohepatitis of NASH.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 hepatic inflammation: the IFN-γ of the intrahepatic T cells (perforin already mapped) is the type-II interferon arm of the immune-mediated inflammation of NASH.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment driving the progression of NASH.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the steatohepatitis of NASH.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-mediated inflammation and fibrosis of NASH.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of NASH.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th17 (IFN-γ and IL-17 already mapped) cytokines that drive the lobular inflammation and the fibrosis of NASH.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Hepatic mast cells: the mast cells accumulate in the fibrosing liver (already mapped) and, via their mediators, promote the stellate-cell (fibroblast already mapped) activation and fibrosis of NASH.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the Kupffer-cell (macrophage already mapped) activation and the lobular inflammation of NASH.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the Kupffer-cell (macrophage already mapped) and myeloid activation of the lobular inflammation of NASH.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-driven inflammation of NASH.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Dysmetabolic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the dysmetabolic hepatic iron overload that aggravates the oxidative injury and fibrosis of NASH.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin gate: TSLP, released from injured hepatocytes and cholangiocytes (already mapped) in NASH, activates the mast cells (already mapped) and dendritic cells (already mapped) that sustain the Type-2-skewed hepatic inflammation driving fibrosis of NASH.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-oedema axis: bradykinin, generated via the kallikrein-kinin system in inflamed liver tissue, increases hepatic sinusoidal permeability and amplifies the macrophage (already mapped) and neutrophil (already mapped) recruitment of NASH.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) over-activation in the inflamed hepatic parenchyma, moderating the immune-mediated hepatocyte injury of NASH.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell effector: histamine, released by mast cells (already mapped) in the portal tract of NASH liver, activates hepatic stellate cells, amplifies the pro-inflammatory cytokine milieu (TNF-α and IL-1β already mapped) and accelerates fibrosis of NASH.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Hepato-protective cytokine: erythropoietin, acting via EPOR on hepatocytes (already mapped) and Kupffer cells (already mapped), suppresses the oxidative stress (ROS already mapped) and TGF-β-driven fibrogenic signalling, attenuating the progressive fibrosis of NASH.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian antioxidant protection: melatonin, via MT1/MT2 receptors on hepatocytes (already mapped), scavenges ROS from dysfunctional mitochondria and inhibits the NF-κB/TNF-α axis (already mapped), moderating the steatoinflammatory injury of NASH.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — NASH testosterone: androgen signalling on hepatocytes (already mapped) attenuates TGF-β (already mapped) fibrogenesis and macrophage (already mapped) lipotoxic activation; testosterone deficiency worsens the steatoinflammatory injury of NASH.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — NASH serotonin: gut-microbiome (already mapped) serotonin promotes hepatic lipogenesis via 5-HT2A receptors on hepatocytes (already mapped); 5-HT also activates macrophage (already mapped) signalling and accelerates the TGF-β (already mapped) fibrotic cascade of NASH.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — NASH prolactin: prolactin, acting via PRLR on hepatocytes (already mapped), promotes hepatic lipid synthesis; prolactin also sensitises the insulin-receptor (already mapped) pathway to the lipotoxic and macrophage (already mapped) inflammatory signals of NASH.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — NASH oxytocin: oxytocin attenuates hepatic NF-κB (already mapped) and TNF-α (already mapped) driven macrophage (already mapped) inflammation and hepatocyte (already mapped) lipotoxicity; oxytocin also suppresses TGF-β (already mapped) mediated hepatic stellate-cell fibrosis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — NASH vasopressin: vasopressin (ADH) via V1b receptor signalling promotes hepatic glycogen release and lipogenesis in hepatocytes (already mapped); vasopressin amplifies NF-κB (already mapped) and IL-6 (already mapped) driven macrophage (already mapped) inflammatory activation.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — NASH iodine: thyroid-hormone deficiency impairs lipid oxidation and amplifies NASH-driven lipotoxicity; iodine deficiency worsens NF-κB (already mapped) and TNF-α (already mapped) driven macrophage (already mapped) inflammatory cascades and TGF-β (already mapped) fibrosis.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^younossi-2016-nafld-epidemiology]: Younossi ZM, Koenig AB, Abdelatif D, Fazel Y, Henry L, Wymer M. Global epidemiology of nonalcoholic fatty liver disease — meta-analytic assessment of prevalence, incidence, and outcomes. *Hepatology.* 2016;64(1):73-84. [doi:10.1002/hep.28431](https://doi.org/10.1002/hep.28431) · [PubMed 26707365](https://pubmed.ncbi.nlm.nih.gov/26707365/)
[^harrison-2024-resmetirom]: Harrison SA, Bedossa P, Guy CD, et al. A phase 3, randomized, controlled trial of resmetirom in NAFLD. *N Engl J Med.* 2024;390(6):497-509. [doi:10.1056/NEJMoa2309000](https://doi.org/10.1056/NEJMoa2309000) · [PubMed 38324483](https://pubmed.ncbi.nlm.nih.gov/38324483/)
[^rinella-2023-masld-nomenclature]: Rinella ME, Lazarus JV, Ratziu V, et al. A multisociety Delphi consensus statement on new fatty liver disease nomenclature. *Hepatology.* 2023;78(6):1966-1986. [doi:10.1097/HEP.0000000000000520](https://doi.org/10.1097/HEP.0000000000000520) · [PubMed 37363821](https://pubmed.ncbi.nlm.nih.gov/37363821/)
