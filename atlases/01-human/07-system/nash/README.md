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

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^younossi-2016-nafld-epidemiology]: Younossi ZM, Koenig AB, Abdelatif D, Fazel Y, Henry L, Wymer M. Global epidemiology of nonalcoholic fatty liver disease — meta-analytic assessment of prevalence, incidence, and outcomes. *Hepatology.* 2016;64(1):73-84. [doi:10.1002/hep.28431](https://doi.org/10.1002/hep.28431) · [PubMed 26707365](https://pubmed.ncbi.nlm.nih.gov/26707365/)
[^harrison-2024-resmetirom]: Harrison SA, Bedossa P, Guy CD, et al. A phase 3, randomized, controlled trial of resmetirom in NAFLD. *N Engl J Med.* 2024;390(6):497-509. [doi:10.1056/NEJMoa2309000](https://doi.org/10.1056/NEJMoa2309000) · [PubMed 38324483](https://pubmed.ncbi.nlm.nih.gov/38324483/)
[^rinella-2023-masld-nomenclature]: Rinella ME, Lazarus JV, Ratziu V, et al. A multisociety Delphi consensus statement on new fatty liver disease nomenclature. *Hepatology.* 2023;78(6):1966-1986. [doi:10.1097/HEP.0000000000000520](https://doi.org/10.1097/HEP.0000000000000520) · [PubMed 37363821](https://pubmed.ncbi.nlm.nih.gov/37363821/)
