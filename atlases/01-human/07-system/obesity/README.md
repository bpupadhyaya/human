---
schema: human-scale-entry/v1
id: obesity
name: Obesity
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Obesity (BMI ≥30; 650M affected) is driven by genetic (FTO, MC4R), neuroendocrine (leptin resistance), gut-microbiome, and environmental factors; adipose inflammation causes metabolic syndrome; GLP-1 receptor agonists (semaglutide) achieve 15-20% weight loss."
aliases: ["obesity", "adiposity", "BMI", "metabolic syndrome", "leptin resistance", "GLP-1 agonist", "semaglutide", "tirzepatide", "adipose tissue", "central obesity"]
sources:
  - id: bluher-2019-obesity-review
    type: peer-reviewed
    cite: "Blüher M. Obesity: global epidemiology and pathogenesis. Nat Rev Endocrinol. 2019;15(5):288-298."
    doi: "10.1038/s41574-019-0176-8"
    pmid: "30814686"
    url: "https://doi.org/10.1038/s41574-019-0176-8"
    accessed: "2026-06-08"
  - id: wilding-2021-semaglutide-step1
    type: peer-reviewed
    cite: "Wilding JPH, Batterham RL, Calanna S, et al. Once-weekly semaglutide in adults with overweight or obesity. N Engl J Med. 2021;384(11):989-1002."
    doi: "10.1056/NEJMoa2032183"
    pmid: "33567185"
    url: "https://doi.org/10.1056/NEJMoa2032183"
    accessed: "2026-06-08"
  - id: backhed-2004-gut-microbiome-obesity
    type: peer-reviewed
    cite: "Bäckhed F, Ding H, Wang T, et al. The gut microbiota as an environmental factor that regulates fat storage. Proc Natl Acad Sci USA. 2004;101(44):15718-15723."
    doi: "10.1073/pnas.0407076101"
    pmid: "15505215"
    url: "https://doi.org/10.1073/pnas.0407076101"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipocyte-secreted leptin signals satiety via hypothalamic LepR/JAK2/STAT3; common obesity involves leptin resistance (elevated leptin, impaired STAT3 signaling via SOCS3 upregulation); monogenic LEP deficiency causes morbid childhood obesity treatable with metreleptin."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Ghrelin, released by gastric A-like cells during fasting, stimulates appetite via hypothalamic GHSR; ghrelin is paradoxically low in obesity but meal-suppression is blunted; GLP-1 receptor agonists (semaglutide) suppress ghrelin, contributing to appetite and weight reduction."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "GLP-1, secreted by intestinal L-cells in response to nutrients, potentiates insulin release and suppresses glucagon and appetite; GLP-1/GIP receptor agonists (semaglutide 15%, tirzepatide 22% body weight loss) are the most effective pharmacological obesity treatments available."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Chronic hyperinsulinemia in obesity drives mTORC1-mediated S6K1 → IRS-1 serine phosphorylation → insulin resistance; adipose inflammation (IL-6, TNF-α via IKKβ/NF-κB) impairs insulin signaling; type 2 diabetes develops when pancreatic β-cell compensation fails."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Dysbiosis in obesity — increased Firmicutes/Bacteroidetes ratio, reduced Akkermansia muciniphila — increases energy harvest and drives metabolic endotoxemia (LPS → TLR4 → systemic inflammation); gut microbiome transfer from obese to germ-free mice transfers adiposity phenotype."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "ARC NPY/AgRP neurons are master orexigenic drivers: NPY → Y1R/Y5R on PVN → increased food intake and reduced energy expenditure; ghrelin activates and leptin/insulin suppress ARC NPY/AgRP; NPY Leu7Pro polymorphism associates with higher BMI and metabolic syndrome risk."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "GH deficiency increases visceral adiposity and dyslipidemia, phenocopying metabolic syndrome; GH therapy reduces visceral fat ~15-20% in deficient adults; obesity-driven leptin resistance suppresses GHRH pulsatility → blunted GH amplitude; weight loss restores GH dynamics."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Visceral adiposity suppresses testosterone via aromatase upregulation and SHBG reduction; hypogonadal-obesity cycle: T deficiency worsens adiposity, which further suppresses T; 5-10% weight loss raises testosterone 2-3 nmol/L without TRT; TRT reduces fat mass ~3 kg."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid hormones set basal metabolic rate — hypothyroidism reduces BMR → weight gain; T3 drives UCP1 in BAT (thermogenesis) and mitochondrial biogenesis; TRβ agonist resmetirom reduces hepatic fat in MASH; levothyroxine normalizes TSH but does not reliably reverse obesity."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian disruption (night-shift work, social jet lag) → disrupted melatonin → leptin resistance → 40% higher obesity risk; light at night suppresses melatonin → metabolic dysregulation; MTNR1B variants modulate BMI; melatonin reduces adiposity in rodent models."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipose tissue secretes adiponectin, but obese adipocytes paradoxically produce less: visceral fat expansion → TNF-α/IL-6 → ADIPOQ suppression → adiponectin deficiency → insulin resistance and cardiovascular risk; TZDs and caloric restriction restore adiponectin."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Obesity is the dominant cause of type 2 diabetes: excess adipose tissue drives insulin resistance via free fatty acids and inflammatory adipokines, so the obesity epidemic powers the diabetes epidemic—and weight loss can put type 2 diabetes into remission."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Obesity is the leading driver of NASH: visceral fat floods the liver with free fatty acids, causing steatosis that inflames into steatohepatitis, fibrosis, and cirrhosis—the hepatic arm of the same metabolic syndrome that links obesity to diabetes and heart disease."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Adipocytes are the cellular engine of obesity: as they enlarge with triglyceride they turn dysfunctional, secreting leptin and inflammatory cytokines, less adiponectin, and recruiting macrophages—so adipose acts as an endocrine organ driving obesity's complications."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Obesity accelerates atherosclerosis and cardiovascular disease: visceral fat drives dyslipidemia, hypertension, insulin resistance and chronic inflammation that injure arteries—a central, modifiable driver of heart attack and stroke."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Obesity is the strongest modifiable risk factor for endometrial cancer: adipose tissue aromatizes androgens into estrogen, and unopposed estrogen drives endometrial proliferation, so most endometrial cancers are obesity-related—a hormone-mediated obesity cancer."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Obesity raises colorectal cancer risk: insulin/IGF-1 signaling, chronic inflammation and altered gut flora from excess adiposity promote colonic tumorigenesis, contributing to rising early-onset colorectal cancer."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Obesity engages the brain's dopamine reward system: highly palatable food drives dopamine release like other rewards, and blunted reward signaling can promote overeating to compensate—so food intake is partly an addiction-like behavior, not simple appetite."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Obesity directly damages the heart: excess volume load and fat-driven inflammation cause obesity cardiomyopathy and heart failure with preserved ejection fraction, so the heart strains under both the metabolic and mechanical burden of excess weight."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Obesity raises postmenopausal breast cancer risk: after menopause, adipose tissue becomes the main estrogen source via aromatase, so excess fat sustains estrogen signaling that drives hormone-receptor-positive breast cancer—an endocrine link between fat and cancer."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Obesity is a state of chronic inflammation run by macrophages: as fat cells enlarge and die, macrophages infiltrate adipose tissue and pour out cytokines (TNF-α, IL-6) that block insulin signaling—linking excess fat directly to insulin resistance and metabolic disease."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Obesity is a leading driver of hypertension: excess fat activates the sympathetic nervous system and renin-angiotensin axis and makes kidneys retain sodium, so weight gain raises blood pressure—and weight loss is among the most effective non-drug treatments."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Obesity overworks the pancreas: insulin resistance forces beta cells to hypersecrete insulin for years until they exhaust and fail, tipping into type 2 diabetes—and excess fat also raises the risk of pancreatitis and pancreatic cancer."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Fat is an estrogen factory that links obesity to cancer: adipose aromatase converts androgens to estrogen, so excess fat raises estrogen and drives the breast and endometrial cancers obesity promotes—especially after menopause."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol shapes where fat goes and can cause obesity: it drives visceral fat deposition and appetite, and cortisol-excess Cushing's syndrome is a secondary cause of weight gain—so refractory central obesity prompts checking the adrenal axis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Obesity is a leading cause of heart failure with preserved ejection fraction: excess weight and adipose inflammation stiffen and strain the heart, and the obese-HFpEF phenotype now responds to the GLP-1 drugs used for weight loss."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Obesity is governed by the brain's hypothalamus: it reads leptin, ghrelin, and insulin to set hunger and energy use, and when this appetite center becomes resistant to those signals, intake outruns expenditure—obesity as a disorder of central regulation."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Obesity is a low-grade inflammatory state driven by TNF: enlarged fat tissue recruits macrophages that secrete TNF-alpha, which blocks insulin signaling—the direct link from belly fat to insulin resistance and type 2 diabetes."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Obesity ties appetite to serotonin: serotonin signaling in the hypothalamus promotes satiety, which is why serotonergic drugs curb eating—and why disordered serotonin links mood, the gut, and body weight."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Obesity robs sleep of oxygen: excess neck and abdominal fat collapses the airway and loads the chest, causing obstructive sleep apnea and obesity hypoventilation, so the body repeatedly drops its oxygen overnight, straining heart and metabolism."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Obesity slowly wears out the kidneys: the metabolic load forces them to hyperfilter, and obesity-related glomerulopathy spills protein and scars the filters, a major and rising driver of chronic kidney disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Obesity sickens the endothelium: inflammatory fat signals and insulin resistance impair the vessel-lining cells that control blood flow, the early endothelial dysfunction that seeds hypertension and atherosclerosis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Body composition is read with radiation: DXA and CT photons separate dangerous visceral fat from harmless subcutaneous fat far better than the crude weight-and-height of BMI."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Overwhelmed fat turns to scar: chronically inflamed adipose tissue becomes fibrotic and stiff, losing its capacity to safely store lipid, which then spills into the liver and muscle to drive metabolic disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Obesity rewires appetite neurons: the hypothalamic neurons that sense leptin grow resistant and inflamed, so the brain misreads a fat-replete body as starving and keeps driving hunger."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows obese fat tissue under siege: adipocytes balloon with lipid until they die, and macrophages wall off the debris in 'crown-like structures,' the microscopic source of the chronic inflammation behind insulin resistance."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Excess weight crushes the breath: fat around the neck and chest collapses the airway in obstructive sleep apnea and stiffens the chest wall, blunting ventilation into the daytime drowsiness of obesity hypoventilation syndrome."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Obesity runs low on magnesium: the mineral is often depleted in metabolic syndrome, and since magnesium aids insulin signaling, its shortage feeds back to worsen the insulin resistance at the disease's core."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Fat spills into the liver: surplus calories and insulin resistance drive triglyceride into hepatocytes, making obesity the leading cause of non-alcoholic fatty liver disease that can progress through NASH to cirrhosis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Excess weight grinds the joints: the mechanical load accelerates osteoarthritis of the knees and hips, while adipokine inflammation adds to the wear, and the resulting pain and immobility make exercise — the treatment — harder."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Body fat reaches into fertility: in women obesity drives the insulin resistance and excess estrogen behind PCOS and anovulation, while in men it lowers testosterone — so weight shapes reproduction in both sexes."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid is checked in every weight workup: hypothyroidism slows metabolism and adds weight, so it is screened before blaming lifestyle, and obesity in turn nudges thyroid hormone levels — a two-way tie worth untangling."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Fiber is a quiet ally against weight: it slows gastric emptying and feeds satiety-signaling gut bacteria, so a high-fiber diet curbs intake and is a cornerstone of the dietary pattern that, with activity, treats obesity."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Weight and mood feed each other: obesity and depression each raise the risk of the other through shared inflammation, cortisol, and inactivity, and several psychiatric drugs add weight — a loop that makes treating either alone harder."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Fat is an inflammatory organ: enlarged adipocytes and their macrophages secrete IL-6 into the blood, driving the liver's C-reactive protein and the insulin resistance that links obesity to diabetes and heart disease."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Inflammation in fat starts with T cells: CD8 cytotoxic T cells infiltrate expanding adipose tissue early and recruit the macrophages that sustain the chronic low-grade inflammation of obesity."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Excess weight crystallizes in the joints: obesity raises uric acid through insulin resistance and higher turnover, so it is a leading and reversible risk factor for gout and its painful attacks."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Fat secretes a pro-inflammatory signal: resistin from adipose tissue and macrophages promotes insulin resistance and vascular inflammation, one of the adipokines through which excess fat turns into metabolic and cardiovascular disease."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Excess weight scars the kidneys: obesity hyperfilters the glomeruli and, with the diabetes and hypertension it drives, produces obesity-related glomerulopathy that progresses to chronic kidney disease."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "The weight reaches the brain's vessels: through hypertension, diabetes and atherosclerosis, obesity raises the risk of ischemic stroke, extending its cardiovascular toll beyond the heart to the cerebral circulation."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Overfed fat smolders with inflammation: free fatty acids and stressed adipocytes activate NF-κB in fat-resident macrophages, the master switch behind the chronic low-grade inflammation that links obesity to insulin resistance."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The brain stops hearing the satiety signal: leptin acts through JAK2-STAT3 in the hypothalamus to curb appetite, and obesity blunts this STAT3 signaling into leptin resistance, so high leptin no longer suppresses eating."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Excess weight thickens and slows the blood: obesity raises clotting factors and venous stasis, making it a major independent risk factor for deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Excess fat fuels a kidney cancer: obesity is a major modifiable risk factor for renal cell carcinoma, acting through insulin/IGF signaling, adipokines and chronic inflammation that promote renal tumorigenesis."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Fat is an inflammatory organ that feeds the plaques: adipose-derived TNF-α and IL-6 worsen psoriasis, so obesity raises its incidence and severity and blunts treatment response, a bidirectional inflammatory link."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Weight reshapes the airways: obesity drives a distinct, often steroid-resistant asthma phenotype through mechanical restriction of the chest and adipokine-driven airway inflammation, worsening control."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Reflux from excess weight scars toward cancer: central obesity promotes acid reflux and Barrett's esophagus, the precursor lesion behind the rising incidence of esophageal adenocarcinoma."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "It is an established pancreatic-cancer risk: obesity's chronic inflammation, hyperinsulinemia and altered adipokines raise the risk of pancreatic adenocarcinoma and worsen its outcomes."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Severe obesity can pressurize the lungs: obesity-hypoventilation and obstructive sleep apnea cause chronic hypoxia that constricts the pulmonary vasculature, contributing to pulmonary hypertension."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Adipose tissue is itself an endocrine organ: obesity drives insulin resistance, leptin and adipokine dysregulation, hypogonadism in men and polycystic ovary syndrome in women, sitting at the centre of endocrine disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Excess weight burdens the gut: obesity causes gastro-oesophageal reflux, gallstones and fatty-liver disease, and it is the leading target of bariatric surgery that reshapes the digestive tract."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Fat tissue heals badly: poorly vascularised adipose, higher wound tension and frequent diabetes make surgical-site infection and dehiscence far more common in obese patients."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Excess weight smothers breathing: obesity is the leading driver of obstructive sleep apnoea and can cause obesity hypoventilation (Pickwickian) syndrome, with daytime hypercapnia and right-heart strain."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It changes the skin in folds and friction: acanthosis nigricans, skin tags, intertrigo, hidradenitis suppurativa and venous stasis changes are common cutaneous consequences of obesity."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can raise pressure around the brain: obesity is the dominant risk factor for idiopathic intracranial hypertension (pseudotumor cerebri), causing headache, papilloedema and threatened vision."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It overworks the heart: excess weight raises cardiac output and workload, causing an obesity cardiomyopathy and atrial fibrillation, on top of the hypertension and atherosclerosis it drives."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Fat is an inflammatory organ: adipose tissue secretes inflammatory adipokines and cytokines, a chronic meta-inflammation that impairs immunity and blunts vaccine responses."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It clogs the lymphatic drainage: severe obesity impairs lymphatic function, causing obesity-related lymphoedema and, in the morbidly obese, massive localised lymphoedema."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It silently scars the kidney: obesity causes glomerular hyperfiltration and an obesity-related glomerulopathy (a secondary FSGS), an independent driver of chronic kidney disease."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "It treats the metabolic consequence: although weight loss and GLP-1 agonists are central, metformin manages the insulin resistance and type 2 diabetes that obesity drives."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "Diet quality, not just quantity, matters: obesity is associated with low magnesium status that worsens insulin resistance, part of the micronutrient picture beyond calorie excess."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "It overworks the islets: obesity-driven insulin resistance forces pancreatic islet beta cells into chronic hyperinsulinaemia, and their eventual compensatory failure is the tipping point from obesity into type 2 diabetes."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It remodels the heart muscle: obesity causes left-ventricular hypertrophy, diastolic dysfunction and fatty infiltration — an obesity cardiomyopathy that, with the raised volume load, predisposes to heart failure and atrial fibrillation."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "It now drives liver cancer: through fatty liver and steatohepatitis, obesity has become a leading cause of hepatocellular carcinoma, which can even arise before frank cirrhosis in metabolic liver disease."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "The commonest eating disorder behind it: binge-eating disorder, with recurrent loss-of-control overeating, is a major driver of weight gain and obesity, and treating it (CBT, lisdexamfetamine) aids weight control."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It hardens the arteries: obesity accelerates atherosclerosis and arterial stiffening through chronic low-grade inflammation, insulin resistance and dyslipidaemia, the vascular path to its cardiovascular disease."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "It overworks the kidney's filter: obesity causes glomerular hyperfiltration and a secondary focal segmental glomerulosclerosis—obesity-related glomerulopathy—an under-recognised cause of proteinuria and chronic kidney disease."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A leading driver of severe COVID: obesity was among the strongest predictors of severe COVID-19, through impaired ventilation, a pro-inflammatory adipose milieu and underlying endothelial dysfunction."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Midlife adiposity and the brain: midlife obesity raises the risk of later dementia, with insulin resistance, vascular injury and chronic neuroinflammation linking excess fat to Alzheimer's disease."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "An overlooked cancer link: obesity is an established risk factor for multiple myeloma and for the progression of its precursor MGUS, adding a haematologic malignancy to obesity's cancer toll."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Another obesity-linked cancer: rising body mass index raises the risk of thyroid cancer, part of obesity's broad oncogenic reach through insulin/IGF-1 signalling, sex hormones and chronic inflammation."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Fat in the liver: obesity drives triglyceride accumulation in the hepatocytes of the hepatic lobule, the steatosis that begins non-alcoholic fatty liver disease and can progress to NASH and cirrhosis."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Obesity and atrial fibrillation: excess adiposity—through atrial stretch, epicardial fat and inflammation—is a leading modifiable driver of atrial fibrillation, and weight loss can reduce its burden."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Adipose hypoxia: as fat mass outgrows its blood supply, HIF-1α activation in hypoxic adipose tissue drives the inflammation and fibrosis central to obesity's metabolic dysfunction."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Nutrient sensing: chronic overnutrition keeps mTOR signalling active in adipose and muscle, promoting fat storage and contributing to the insulin resistance of obesity."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "Energy gauge: AMPK, the cell's low-energy sensor, is blunted in obesity, reducing fat oxidation and glucose uptake—its reactivation is a key target of metformin and exercise."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Adipose macrophage recruitment: CCL2 released by stressed adipocytes draws monocytes into expanding fat, where they become the crown-like macrophages that drive obesity's chronic low-grade inflammation."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Metabolic inflammasome: excess lipids and danger signals activate the NLRP3 inflammasome in adipose macrophages, releasing IL-1β that impairs insulin signalling and links obesity to type 2 diabetes."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Receptor-level resistance: inflammatory and lipid signals impair insulin-receptor signalling in obese liver, muscle and fat, the molecular core of the insulin resistance that defines metabolic obesity."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "Appetite drive: an overactive endocannabinoid system stimulates CB1 receptors in the hypothalamus and adipose tissue to promote feeding and fat storage, the target of the CB1 antagonist rimonabant once used for obesity."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Feeding and expenditure: hypothalamic orexin integrates arousal with feeding behaviour and energy expenditure, part of the central circuitry whose dysregulation contributes to the disordered appetite control of obesity."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Lipid-induced inflammation: saturated fatty acids directly activate TLR4 on adipocytes and macrophages, igniting the NF-κB-driven metaflammation that mechanistically links obesity to insulin resistance."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Central appetite control: BDNF signalling through TrkB sits downstream of the hypothalamic melanocortin (MC4R) pathway controlling energy balance, and rare BDNF/TrkB mutations cause severe early-onset human obesity, marking it as a core appetite regulator."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Energy-expenditure signalling: FGF21 acting through FGFR1c with β-Klotho promotes fat oxidation, browning of white adipose tissue and energy expenditure, an endocrine axis being targeted by FGF21 analogues for obesity and its metabolic complications."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Adipose angiogenesis: expanding fat depots require VEGF-driven angiogenesis to vascularise, and when adipose growth outstrips its blood supply the resulting hypoxia drives the inflammation and fibrosis of dysfunctional obese adipose tissue."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Insulin resistance: insulin signalling through AKT (insulin-receptor already mapped) is progressively impaired in expanding, inflamed adipose tissue, the molecular basis of the insulin resistance linking obesity to type-2 diabetes."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Metaflammation: the NLRP3 inflammasome (already mapped) in adipose-tissue macrophages generates IL-1β, a key driver of the chronic low-grade inflammation that produces the metabolic complications of obesity."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Energy-balance therapeutics: glucagon governs hepatic glucose output and energy expenditure, and glucagon/GLP-1 dual-agonist drugs exploit this axis (alongside the GLP-1 already mapped) to drive weight loss in obesity."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Insulin-signalling defect: the insulin receptor (mapped) signals through IRS-PI3K to AKT (mapped), and blunting of this PI3K branch in overnourished tissue is the molecular core of obesity-associated insulin resistance."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Adipose inflammation: saturated fatty acids and gut-derived LPS activate adipose-tissue TLR4 (mapped) through MyD88 to NF-κB (mapped), driving the macrophage inflammation that links obesity to insulin resistance."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Glycogen and metabolism: AKT normally inhibits GSK-3β to switch on glycogen synthesis, and elevated GSK-3β activity in obesity impairs insulin action and glucose storage."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Leptin signals through the JAK2-STAT3 axis (leptin and STAT3 mapped) in hypothalamic neurons; leptin resistance at this node underlies the failure of satiety signalling in obesity."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 released by adipose-tissue macrophages drives the chronic low-grade inflammation and fibrosis of expanding fat depots in obesity."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "The adipocyte-derived complement axis (C3/adipsin) is upregulated in obesity and contributes to adipose inflammation and metabolic dysfunction."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Mitochondrial and metabolic stress in expanding adipose tissue releases cytosolic DNA that engages cGAS-STING, fuelling the metabolic inflammation of obesity."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling drives the adipose-tissue fibrosis that accompanies the dysfunctional expansion of fat in obesity."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the pro-inflammatory macrophage polarisation of obese adipose tissue, linking immunity to metabolic dysfunction."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO1 integrates insulin-PI3K-AKT signaling (AKT and PIK3CA already mapped) to control adipocyte differentiation and hepatic metabolism dysregulated in obesity."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by adipose-tissue macrophages amplify the chronic low-grade metabolic inflammation of obesity."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling contributes to adipogenesis and the inflammatory adipocyte stress response of obese adipose tissue."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic CD8 T cells accumulate in obese adipose tissue and drive the immune activation underlying obesity-associated insulin resistance."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the inflammatory and insulin-resistance signaling of obese adipose tissue."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D signaling regulates adipocyte differentiation and the metabolic-inflammatory programming of adipose tissue in obesity."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the adipocyte and hypothalamic-neuron homeostasis whose dysregulation contributes to obesity."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic programming of adipogenesis and metabolic dysfunction in obesity."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte recruitment amplifies the adipose-tissue macrophage inflammation of obesity."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the adipose-tissue immune-cell recruitment and remodeling of obesity."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the adipose inflammation and metabolic dysregulation of obesity."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33-ILC2 signaling participates in the adipose-tissue immune homeostasis and thermogenesis relevant to obesity."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the adipogenic and metabolic gene programs of obesity."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the adipose-tissue immune activation and adipocyte biology of obesity."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the adipose-tissue macrophage infiltration and metaflammation of obesity."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Central satiety: oxytocin acts in the hypothalamus to reduce food intake and is under investigation as an anti-obesity target, adding a neuroendocrine appetite brake distinct from the leptin-ghrelin axis already mapped."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "Glucosuric weight loss: SGLT2 inhibitors cause urinary excretion of glucose and thus calories, producing modest weight loss and linking a renal glucose transporter to energy balance in the treatment of obesity-related metabolic disease."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Hyperuricaemia: adiposity raises xanthine-oxidase activity and serum urate, and the resulting hyperuricaemia links obesity to gout and to the endothelial dysfunction underlying its cardiovascular risk."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac injury: obesity strains the heart (already mapped) and accelerates atherosclerosis, and troponin elevation marks the myocardial injury of the cardiovascular disease that is the leading cause of death in the obese."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Adipose renin-angiotensin: adipose tissue produces angiotensinogen and components of a local renin-angiotensin system, and the resulting angiotensin II contributes to the hypertension (already mapped) that accompanies obesity."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "Atherogenic dyslipidaemia: obesity raises triglycerides and small dense LDL, and PCSK9-regulated LDL-receptor handling contributes to the dyslipidaemia driving the accelerated atherosclerosis (already mapped) of the obese state."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Dyslipidaemia: obesity shifts cholesterol handling toward high triglycerides, low HDL and small dense LDL (PCSK9 already mapped), the atherogenic dyslipidaemia that is a core component of the metabolic syndrome."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Adipose mineralocorticoid axis: adipose tissue stimulates aldosterone release, and aldosterone acting through mineralocorticoid receptors promotes the hypertension, inflammation and fibrosis (angiotensin II already mapped) that accompany obesity."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory balance: the anti-inflammatory IL-10 counters the chronic low-grade inflammation of adipose tissue (TNF, IL-6 and IL-1 already mapped), and the imbalance toward pro-inflammatory signalling drives the insulin resistance of obesity."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Adipose M2 macrophages: IL-4 sustains the anti-inflammatory M2 macrophages (already mapped) of healthy lean adipose tissue (IL-10 already mapped), and the shift toward pro-inflammatory macrophages in obesity drives its insulin resistance."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Adipose eicosanoids: prostaglandins regulate adipogenesis and, from the inflamed adipose tissue (TNF and IL-6 already mapped), contribute to the low-grade inflammation and metabolic dysfunction of obesity."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Obesity and iron dysregulation: the chronic inflammation of obesity raises hepcidin, sequestering iron to cause a functional iron deficiency despite adequate stores, part of the disturbed metabolic milieu of the disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Adipose M2 maintenance: IL-13, with IL-4 (already mapped), maintains the anti-inflammatory M2 macrophages (already mapped) of the lean adipose tissue, and the loss of this type-2 signalling in obesity drives the inflammatory shift and insulin resistance."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil-M2 axis: IL-5 recruits the adipose eosinophils that sustain the M2 macrophages (already mapped) and metabolic health of lean fat, and their loss contributes to the adipose inflammation of obesity."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Functional iron deficiency: the obesity inflammation (IL-6 already mapped) raises hepcidin, which sequesters iron (already mapped) to cause the functional iron deficiency characteristic of obesity despite adequate stores."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Microbiome-obesity link: the gut-microbiome composition (the energy harvest, the SCFAs, the endotoxaemia — TLR4 already mapped) influences the obesity and the metabolic state."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Cardiovascular risk: obesity drives the atherosclerosis (cholesterol and PCSK9 already mapped) and the cardiovascular disease, a leading obesity complication."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Beta-cell demand: the obesity-driven insulin (already mapped) resistance raises the demand on the pancreatic β-cells, whose eventual failure causes the type 2 diabetes."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Adipose NK meta-inflammation: the adipose-tissue NK cells (perforin already mapped) and their IFN-γ drive the type-1 meta-inflammation of the obese adipose tissue (macrophages already mapped)."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Adipose Th1 inflammation: the IFN-γ of the adipose-tissue T and NK cells drives the Th1 meta-inflammation that promotes the insulin (already mapped) resistance of obesity."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the chronic adipose meta-inflammation (TNF and IL-6 already mapped) of obesity."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic adipose meta-inflammation of obesity."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune arm whose loss accompanies the pro-inflammatory shift of the obese adipose tissue."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate metabolic interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the metabolic stress, contributes to the chronic adipose meta-inflammation of obesity."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Adipose CD4 shift: the CD4 T-helper cells shift from the lean-adipose Th2/Treg toward the Th1/Th17 (IFN-γ and IL-17 already mapped) phenotype, driving the meta-inflammation of the obese adipose tissue."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Adipose mast cells: the mast cells accumulate in the obese adipose tissue and contribute to the chronic low-grade inflammation and the insulin resistance of obesity."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Adipose fibrosis: the fibroblasts/myofibroblasts drive the extracellular-matrix remodelling and fibrosis of the expanding, hypoxic (HIF-1α already mapped) adipose tissue of obesity."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the adipose-tissue inflammation and the insulin resistance of obesity."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the macrophage (already mapped) recruitment into the inflamed adipose tissue of obesity."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Dysmetabolic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the adipose-tissue and systemic iron dysregulation of obesity."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Adipose alarmin: TSLP, secreted by adipocytes (already mapped) and adipose-stromal cells under lipotoxic stress, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the Type-2-skewed adipose inflammation of obesity."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-metabolic axis: bradykinin, generated by the kallikrein-kinin system elevated in obese adipose tissue, increases insulin sensitisation via B2 receptors on adipocytes (already mapped) and endothelial cells (already mapped) and modulates the vascular tone of obesity."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) over-activation in inflamed adipose tissue, moderating the immune-driven metabolic dysfunction of obesity."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell adipose effector: histamine, released by mast cells (already mapped) in expanded adipose tissue, promotes adipocyte (already mapped) lipolysis, amplifies the pro-inflammatory cytokine milieu (TNF-α and IL-6 already mapped) and accelerates insulin resistance of obesity."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Adipokine-EPO crosstalk: erythropoietin, acting via EPOR on adipocytes (already mapped) and macrophages (already mapped), promotes fat mass reduction and improves insulin sensitivity, counteracting the adipose inflammation of obesity."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Adipose ECM remodelling: periostin, expressed by fibroblasts and adipocyte precursors in expanding adipose tissue, promotes the fibrotic extracellular matrix remodelling and adipose tissue dysfunction that amplifies the chronic inflammation of obesity."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "OB factor-h: factor H regulates the alternative complement (C3 and C5 already mapped) in adipose tissue; impaired factor H activity amplifies the adipocyte (already mapped) lipotoxic and macrophage (already mapped) inflammatory phenotype of obesity."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "OB prolactin: prolactin modulates the gut-microbiome (already mapped) composition and leptin (already mapped) sensitivity in obesity; elevated prolactin promotes adipocyte (already mapped) lipogenesis and macrophage (already mapped) adipose inflammation."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "OB vasopressin: vasopressin, via V1 receptors on adipocytes (already mapped), promotes adipose inflammation and insulin resistance; V2-receptor signalling on the kidney (already mapped) drives the fluid retention and blood-pressure elevation of the obese cardiometabolic state."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "OB selenium: selenoprotein P controls adipocyte (already mapped) lipotoxic oxidative stress and macrophage (already mapped) adipose metainflammation; selenium deficiency amplifies the NF-κB (already mapped) inflammatory cascade and worsens insulin resistance in obesity."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "OB iodine: iodine-dependent thyroid hormones regulate the basal metabolic rate and adipocyte (already mapped) lipid turnover; thyroid-hormone deficiency amplifies the NF-κB (already mapped) adipose inflammation and deepens the energy-balance dysregulation of obesity."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "OB sodium: excess dietary sodium promotes adipocyte (already mapped) fluid retention and vascular inflammation through RAAS activation; sodium-driven hypertension amplifies the NF-κB (already mapped) adipose inflammatory cascade and the cardiometabolic burden of obesity."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Obesity copper: copper, as cytochrome c oxidase cofactor in adipocytes (already mapped) and macrophages (already mapped), supports mitochondrial function; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) metabolic-inflammatory cascade of obesity."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Obesity potassium: dietary potassium regulates macrophage (already mapped) and adipocyte (already mapped) membrane potential; potassium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) adipose inflammatory cascade of obesity."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Obesity zinc: zinc, as co-factor of insulin-signalling enzymes in adipocytes (already mapped) and macrophages (already mapped), modulates fat metabolism; zinc deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) metabolic-inflammatory adipose cascade."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Obesity calcium: calcium signals regulate macrophage (already mapped) and adipocyte (already mapped) lipid metabolism; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) adipose inflammation driving the mast-cell (already mapped) cascade of obesity."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Obesity phosphorus: phosphorus-dependent ATP and signalling lipids in macrophages (already mapped) and adipocytes (already mapped) govern energy partitioning; phosphate imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) adipose metabolic-inflammatory cascade."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Obesity carbon: carbon as backbone of adipokine and NF-κB (already mapped) proteins in adipocytes (already mapped) sustains adipose signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of obesity."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Obesity chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in adipose tissue; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) adipose inflammatory cascade of obesity."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Obesity nitrogen: nitrogen in amino-acid scaffold of adipokines (already mapped) and NF-κB (already mapped) proteins in adipocytes (already mapped) sustains adipose signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of obesity."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Obesity hydrogen: hydrogen, via redox homeostasis in adipocytes (already mapped) and macrophages (already mapped), supports leptin (already mapped) signalling; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) adipose cascade of obesity."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Obesity sulfur: sulfur in cysteine residues of leptin (already mapped) and adiponectin (already mapped) in adipocytes (already mapped) sustains thiol-redox balance; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of obesity."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Obesity PD-1: PD-1 on T-cells (already mapped) in adipose tissue suppresses cytotoxic immunity; PD-1 checkpoint dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) adipose inflammatory cascade of obesity."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Obesity wnt-beta-catenin: WNT/β-catenin on adipocytes (already mapped) and macrophages (already mapped) drives adipose lipid storage; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of obesity."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Obesity rankl: RANKL from macrophages (already mapped) and adipocytes (already mapped) promotes adipose immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) adipose cascade of obesity."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Obesity il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates adipose immune surveillance; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) adipose cascade of obesity."
---

# Obesity

## Overview

**Obesity** is a chronic, relapsing metabolic disorder defined by **excess adipose tissue accumulation** sufficient to impair health, conventionally classified by body mass index (BMI):

| Classification | BMI (kg/m²) | Global prevalence |
|:---|:---|:---|
| Overweight | 25.0–29.9 | ~38% adults |
| Obesity Class I | 30.0–34.9 | ~13% adults |
| Obesity Class II | 35.0–39.9 | ~5% adults |
| Obesity Class III (severe) | ≥40 | ~2% adults |

**Epidemiology:** As of 2024, over **650 million adults** globally are obese (BMI ≥30) and over 1 billion overweight — representing a 3× increase since 1975. Obesity is projected to exceed 50% of US adults by 2030. The disorder reduces life expectancy by 3–10 years depending on severity, is the leading preventable cause of type 2 diabetes, cardiovascular disease, obstructive sleep apnea, osteoarthritis, non-alcoholic steatohepatitis (NASH), and multiple cancers [^bluher-2019-obesity-review].

Obesity is not a simple behavioral failure but a **complex neuroendocrine disorder** with strong genetic determinants (heritability ~40–70%), driven by dysregulated appetite regulation, adipokine signaling, gut-brain axis communication, and the obesogenic food environment. The revolution in understanding its biology — particularly the leptin axis (1994) and GLP-1 receptor agonist pharmacology — has transformed treatment from ineffective counseling to highly effective, mechanism-targeted pharmacotherapy.

## Structure

### Adipose tissue biology

Adipose tissue is not merely an energy depot but an active **endocrine organ** with two functionally distinct compartments:

**White adipose tissue (WAT):**
- Stores triglycerides in large unilocular lipid droplets
- Secretes **adipokines**: leptin (satiety signal), adiponectin (insulin sensitizer), resistin, visfatin, TNF-α, IL-6
- **Visceral WAT** (omental, mesenteric): metabolically harmful; directly drains into portal circulation → hepatic lipotoxicity; inflammatory adipokine secretion correlates with metabolic syndrome risk
- **Subcutaneous WAT**: metabolically more benign; leptin-rich depot that reflects overall energy status

**Brown adipose tissue (BAT):**
- Multilocular lipid droplets; rich in mitochondria expressing **UCP1** (uncoupling protein 1 / thermogenin)
- UCP1 uncouples oxidative phosphorylation → heat generation (non-shivering thermogenesis) at the expense of ATP synthesis
- Active BAT correlates with leanness; cold exposure, β3-adrenergic agonists, and FGF21 activate BAT
- BAT is a target for obesity pharmacology (thyromimetics, β3-AR agonists)

**Beige/brite adipocytes:**
- White adipocytes that acquire brown-fat-like characteristics (UCP1 expression) upon sympathetic stimulation or cold — **WAT browning**
- PRDM16 transcription factor is the master regulator of beige adipocyte differentiation
- Irisin (FNDC5 cleavage product, released by muscle during exercise) promotes WAT browning

### Hypothalamic appetite circuits

The **arcuate nucleus (ARC)** of the hypothalamus integrates peripheral satiety and hunger signals via two antagonistic neuron populations:

**ARC POMC/CART neurons (anorexigenic):**
- Respond to leptin, insulin, GLP-1, PYY → release α-MSH → melanocortin 4 receptor (MC4R) activation in paraventricular nucleus → satiety and reduced feeding
- α-MSH is the agonist of MC4R (the most common monogenic obesity gene in humans — 2–5% of severe obesity)

**ARC AgRP/NPY neurons (orexigenic):**
- Inhibited by leptin and insulin; activated by ghrelin → release NPY and AgRP (endogenous MC4R antagonist) → stimulate feeding
- These neurons drive hunger during caloric restriction; hyperactive in obesity via leptin resistance

**Melanocortin pathway mutations causing monogenic obesity:**
- **MC4R LOF** (~2–5% of severe obesity): hyperphagia, normal height, obesity
- **LEP (leptin) LOF** (<0.01%): severe hyperphagia, morbid obesity from infancy; treatable with recombinant metreleptin
- **LEPR (leptin receptor) LOF**: similar to LEP deficiency; hypogonadotropic hypogonadism in addition
- **POMC LOF**: adrenal insufficiency (loss of ACTH) + red hair (loss of MSH pigment) + early obesity

## Function

### Energy balance: the set point problem

The body defends a **body weight set point** determined by hypothalamic arcuate circuits. Caloric restriction activates multiple counter-regulatory mechanisms to restore weight:
- Leptin levels fall → AgRP neurons activate → hunger increases dramatically
- Metabolic rate decreases (reduced thyroid hormone, sympathetic tone)
- Ghrelin rises → additional hunger drive

This **adaptive thermogenesis** explains why most dietary interventions fail long-term: the body fights weight loss at the hormonal/neural level. Up to 80% of lost weight is regained within 5 years without pharmacological maintenance.

### Adipose tissue inflammation (metainflammation)

In obesity, adipocytes expand to pathological sizes → **hypoxia within the adipose depot** → macrophage infiltration (M1-polarized, pro-inflammatory):

1. **Dead adipocyte "crown-like structures":** Lipid-laden macrophage accumulations around dying adipocytes
2. **Adipokine dysregulation:** Elevated TNF-α, IL-6, MCP-1 (CCL2); reduced anti-inflammatory adiponectin
3. **Free fatty acid (FFA) spill-over:** Lipolysis in dysfunctional adipocytes → elevated circulating FFAs → ectopic lipid deposition in liver, skeletal muscle, heart, pancreas → lipotoxicity
4. **TLR4 activation by saturated FFAs and LPS (from gut dysbiosis):** NF-κB activation → chronic low-grade systemic inflammation → insulin resistance

This **metainflammation** mechanistically links obesity to type 2 diabetes, atherosclerosis, NASH, and certain cancers (via adipokine-driven inflammation and IGF-1/insulin signaling).

### Genetic architecture of common obesity

**Monogenic obesity** (<5% of severe cases): MC4R, LEP, LEPR, POMC, PCSK1, SIM1, KSR2.

**Polygenic common obesity (>95% of cases):**
- Most strongly associated common variant: **FTO (rs9939609)** — intronic SNP; actual causal mechanism involves altered transcriptional regulation of nearby **IRX3 and IRX5** genes → reduced brown adipose tissue activity and thermogenesis
- **>900 loci** identified by GWAS (2023); most enriched in CNS pathways (appetite regulation, reward) rather than adipocyte-specific pathways — confirming obesity as primarily a brain-regulated set point disorder
- Polygenic risk score (PRS) for obesity predicts risk 2–4× better than any single gene

## Pathology

### Metabolic consequences

**Metabolic syndrome** (central obesity + 2 of: elevated TG, low HDL, hypertension, elevated fasting glucose):
- Present in ~40% of obese adults
- Driven by visceral adipose inflammation, hepatic lipotoxicity, and insulin resistance

**Type 2 diabetes:**
- 80–90% of T2D patients have overweight or obesity
- Mechanism: insulin resistance → compensatory hyperinsulinemia → β-cell exhaustion → T2D; each 1 kg/m² BMI increase → ~6% higher T2D risk

**Cardiovascular disease:**
- Obesity-associated hypertension (visceral adipose → increased renin-angiotensin; insulin → sodium retention)
- Dyslipidemia (small dense LDL, elevated TG, low HDL)
- Cardiomyopathy (lipotoxicity, adipokine effects on myocardium)

**Cancer:**
- Obesity-associated cancers: endometrial (2-4×), postmenopausal breast (1.5×), colon (1.5-2×), kidney (1.5-2×), esophageal adenocarcinoma (7×), pancreatic (1.5×)
- Mechanisms: hyperinsulinemia/IGF-1 (pro-proliferative), adipose inflammation, estrogen production by adipose aromatase (endometrial/breast), altered bile acid metabolism (colorectal)

### Treatment

**Lifestyle modification:**
- Diet + physical activity: 5–10% weight loss achievable; significant metabolic benefit even without normalization of BMI; typically regained within 5 years

**Pharmacotherapy:**
| Drug | Mechanism | Weight loss | FDA approval |
|:---|:---|:---|:---|
| **Semaglutide (Wegovy)** | GLP-1 receptor agonist | ~15% (STEP 1) [^wilding-2021-semaglutide-step1] | 2021 (obesity) |
| **Tirzepatide (Zepbound)** | GLP-1 + GIP dual agonist | ~22% (SURMOUNT-1) | 2023 (obesity) |
| **Naltrexone-bupropion (Contrave)** | Opioid antagonist + dopamine/NE reuptake inhibitor | ~5-6% | 2014 |
| **Phentermine-topiramate (Qsymia)** | Amphetamine + anticonvulsant | ~8-10% | 2012 |
| **Orlistat (Xenical)** | Pancreatic lipase inhibitor | ~3-4% | 1999 |

**Bariatric surgery:**
- Roux-en-Y gastric bypass (RYGB): ~30% EWL at 5 years; T2D remission in 60–80% (precedes weight loss → involves GLP-1, bile acid, microbiome effects)
- Sleeve gastrectomy: ~25% EWL; simpler; no intestinal rerouting; standard first-line bariatric procedure
- RYGB vs. best medical therapy: surgery superior for T2D remission, CV events, and mortality (STAMPEDE, Swedish Obese Subjects study)

**Emerging treatments:**
- **CagriSema (cagrilintide + semaglutide):** ~25% weight loss in Phase 3 (REDEFINE-1)
- **Retatrutide (GLP-1/GIP/glucagon triple agonist):** ~24% at 48 weeks (Phase 2)
- **Leptin sensitizers and MC4R agonists** (setmelanotide: FDA-approved for POMC/PCSK1/LEPR deficiency)
- **Adipose tissue engineering:** Targeting UCP1 activation in WAT via β3-AR agonism, thyromimetics, or PRDM16 induction

## Connections

- `connects-to` → **[Leptin](../../../03-molecular/leptin/README.md)** — Leptin, secreted by adipocytes proportional to fat mass, signals satiety via hypothalamic LepR/JAK2/STAT3; common obesity involves leptin resistance (high leptin levels, impaired signaling) driven by SOCS3; monogenic leptin deficiency causes severe childhood obesity treatable with recombinant metreleptin.

- `connects-to` → **[Ghrelin](../../../03-molecular/ghrelin/README.md)** — Ghrelin rises during fasting and stimulates appetite via hypothalamic GHSR; ghrelin levels are paradoxically reduced in common obesity but the meal-suppression response is blunted; GLP-1 receptor agonists suppress ghrelin release, contributing to profound appetite reduction.

- `connects-to` → **[GLP-1](../../../03-molecular/glp-1/README.md)** — GLP-1, secreted by intestinal L-cells post-meal, potentiates insulin release, suppresses glucagon, and reduces appetite via hypothalamic GLP-1R; GLP-1/GIP receptor agonists (semaglutide ~15%, tirzepatide ~22% weight loss) are the most effective pharmacological obesity treatments available.

- `connects-to` → **[Insulin](../../../03-molecular/insulin/README.md)** — Chronic hyperinsulinemia in obesity drives mTORC1/S6K1 → IRS-1 serine phosphorylation → insulin resistance; adipose inflammation via IKKβ/NF-κB further impairs insulin signaling; type 2 diabetes develops when pancreatic β-cell compensation fails under sustained metabolic demand.

- `connects-to` → **[Gut Microbiome](../../gut-microbiome/README.md)** — Dysbiosis in obesity — increased Firmicutes/Bacteroidetes ratio, reduced Akkermansia muciniphila — increases energy harvest and drives metabolic endotoxemia (LPS → TLR4 → systemic inflammation); gut microbiome transfer from obese to germ-free mice transfers the adiposity phenotype.

- `connects-to` → **[NPY](../../../03-molecular/npy/README.md)** — ARC NPY/AgRP neurons are master orexigenic drivers: NPY → Y1R/Y5R on PVN → increased food intake and reduced energy expenditure; ghrelin activates and leptin/insulin suppress ARC NPY/AgRP; NPY Leu7Pro polymorphism associates with higher BMI and metabolic syndrome risk.
- `connects-to` → **[Growth Hormone](../../../03-molecular/growth-hormone/README.md)** — GH deficiency increases visceral adiposity and dyslipidemia, phenocopying metabolic syndrome; GH therapy reduces visceral fat ~15-20% in deficient adults; leptin resistance in obesity suppresses GHRH pulsatility → blunted GH amplitude; weight loss restores GH secretory dynamics.
- `connects-to` → **[Testosterone](../../../03-molecular/testosterone/README.md)** — Visceral adiposity suppresses testosterone via aromatase upregulation and SHBG reduction; hypogonadal-obesity cycle: T deficiency worsens adiposity, which further suppresses T; 5-10% weight loss raises testosterone 2-3 nmol/L without TRT; TRT reduces fat mass ~3 kg.
- `connects-to` → **[Thyroid Hormones](../../../03-molecular/thyroid-hormones/README.md)** — Thyroid hormones set basal metabolic rate — hypothyroidism reduces BMR → weight gain; T3 drives UCP1 in BAT (thermogenesis) and mitochondrial biogenesis; TRβ agonist resmetirom reduces hepatic fat in MASH; levothyroxine normalizes TSH but does not reliably reverse obesity.
- `connects-to` → **[Melatonin](../../../03-molecular/melatonin/README.md)** — Circadian disruption (night-shift work, social jet lag) → disrupted melatonin → leptin resistance → 40% higher obesity risk; light at night suppresses melatonin → metabolic dysregulation; MTNR1B variants modulate BMI; melatonin reduces adiposity in rodent models.
- `connects-to` → **[Adiponectin](../../../03-molecular/adiponectin/README.md)** — Adipose tissue secretes adiponectin, but obese adipocytes paradoxically produce less: visceral fat expansion → TNF-α/IL-6 → ADIPOQ suppression → adiponectin deficiency → insulin resistance and cardiovascular risk; TZDs and caloric restriction restore adiponectin.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Obesity is the dominant cause of type 2 diabetes: excess adipose tissue drives insulin resistance via free fatty acids and inflammatory adipokines, so the obesity epidemic powers the diabetes epidemic—and weight loss can put type 2 diabetes into remission.
- `connects-to` → **[NASH](../nash/README.md)** — Obesity is the leading driver of NASH: visceral fat floods the liver with free fatty acids, causing steatosis that inflames into steatohepatitis, fibrosis, and cirrhosis—the hepatic arm of the same metabolic syndrome that links obesity to diabetes and heart disease.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Adipocytes are the cellular engine of obesity: as they enlarge with triglyceride they turn dysfunctional, secreting leptin and inflammatory cytokines, less adiponectin, and recruiting macrophages—so adipose acts as an endocrine organ driving obesity's complications.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Obesity accelerates atherosclerosis and cardiovascular disease: visceral fat drives dyslipidemia, hypertension, insulin resistance and chronic inflammation that injure arteries—a central, modifiable driver of heart attack and stroke.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Obesity is the strongest modifiable risk factor for endometrial cancer: adipose tissue aromatizes androgens into estrogen, and unopposed estrogen drives endometrial proliferation, so most endometrial cancers are obesity-related—a hormone-mediated obesity cancer.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Obesity raises colorectal cancer risk: insulin/IGF-1 signaling, chronic inflammation and altered gut flora from excess adiposity promote colonic tumorigenesis, contributing to rising early-onset colorectal cancer.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Obesity engages the brain's dopamine reward system: highly palatable food drives dopamine release like other rewards, and blunted reward signaling can promote overeating to compensate—so food intake is partly an addiction-like behavior, not simple appetite.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Obesity directly damages the heart: excess volume load and fat-driven inflammation cause obesity cardiomyopathy and heart failure with preserved ejection fraction, so the heart strains under both the metabolic and mechanical burden of excess weight.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Obesity raises postmenopausal breast cancer risk: after menopause, adipose tissue becomes the main estrogen source via aromatase, so excess fat sustains estrogen signaling that drives hormone-receptor-positive breast cancer—an endocrine link between fat and cancer.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Obesity is a state of chronic inflammation run by macrophages: as fat cells enlarge and die, macrophages infiltrate adipose tissue and pour out cytokines (TNF-α, IL-6) that block insulin signaling—linking excess fat directly to insulin resistance and metabolic disease.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Obesity is a leading driver of hypertension: excess fat activates the sympathetic nervous system and renin-angiotensin axis and makes kidneys retain sodium, so weight gain raises blood pressure—and weight loss is among the most effective non-drug treatments.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Obesity overworks the pancreas: insulin resistance forces beta cells to hypersecrete insulin for years until they exhaust and fail, tipping into type 2 diabetes—and excess fat also raises the risk of pancreatitis and pancreatic cancer.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Fat is an estrogen factory that links obesity to cancer: adipose aromatase converts androgens to estrogen, so excess fat raises estrogen and drives the breast and endometrial cancers obesity promotes—especially after menopause.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol shapes where fat goes and can cause obesity: it drives visceral fat deposition and appetite, and cortisol-excess Cushing's syndrome is a secondary cause of weight gain—so refractory central obesity prompts checking the adrenal axis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Obesity is a leading cause of heart failure with preserved ejection fraction: excess weight and adipose inflammation stiffen and strain the heart, and the obese-HFpEF phenotype now responds to the GLP-1 drugs used for weight loss.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Obesity is governed by the brain's hypothalamus: it reads leptin, ghrelin, and insulin to set hunger and energy use, and when this appetite center becomes resistant to those signals, intake outruns expenditure—obesity as a disorder of central regulation.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Obesity is a low-grade inflammatory state driven by TNF: enlarged fat tissue recruits macrophages that secrete TNF-alpha, which blocks insulin signaling—the direct link from belly fat to insulin resistance and type 2 diabetes.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Obesity ties appetite to serotonin: serotonin signaling in the hypothalamus promotes satiety, which is why serotonergic drugs curb eating—and why disordered serotonin links mood, the gut, and body weight.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Obesity robs sleep of oxygen: excess neck and abdominal fat collapses the airway and loads the chest, causing obstructive sleep apnea and obesity hypoventilation, so the body repeatedly drops its oxygen overnight, straining heart and metabolism.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Obesity slowly wears out the kidneys: the metabolic load forces them to hyperfilter, and obesity-related glomerulopathy spills protein and scars the filters, a major and rising driver of chronic kidney disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Obesity sickens the endothelium: inflammatory fat signals and insulin resistance impair the vessel-lining cells that control blood flow, the early endothelial dysfunction that seeds hypertension and atherosclerosis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Body composition is read with radiation: DXA and CT photons separate dangerous visceral fat from harmless subcutaneous fat far better than the crude weight-and-height of BMI.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Overwhelmed fat turns to scar: chronically inflamed adipose tissue becomes fibrotic and stiff, losing its capacity to safely store lipid, which then spills into the liver and muscle to drive metabolic disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Obesity rewires appetite neurons: the hypothalamic neurons that sense leptin grow resistant and inflamed, so the brain misreads a fat-replete body as starving and keeps driving hunger.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows obese fat tissue under siege: adipocytes balloon with lipid until they die, and macrophages wall off the debris in 'crown-like structures,' the microscopic source of the chronic inflammation behind insulin resistance.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Excess weight crushes the breath: fat around the neck and chest collapses the airway in obstructive sleep apnea and stiffens the chest wall, blunting ventilation into the daytime drowsiness of obesity hypoventilation syndrome.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Obesity runs low on magnesium: the mineral is often depleted in metabolic syndrome, and since magnesium aids insulin signaling, its shortage feeds back to worsen the insulin resistance at the disease's core.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Fat spills into the liver: surplus calories and insulin resistance drive triglyceride into hepatocytes, making obesity the leading cause of non-alcoholic fatty liver disease that can progress through NASH to cirrhosis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Excess weight grinds the joints: the mechanical load accelerates osteoarthritis of the knees and hips, while adipokine inflammation adds to the wear, and the resulting pain and immobility make exercise — the treatment — harder.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Body fat reaches into fertility: in women obesity drives the insulin resistance and excess estrogen behind PCOS and anovulation, while in men it lowers testosterone — so weight shapes reproduction in both sexes.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid is checked in every weight workup: hypothyroidism slows metabolism and adds weight, so it is screened before blaming lifestyle, and obesity in turn nudges thyroid hormone levels — a two-way tie worth untangling.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Fiber is a quiet ally against weight: it slows gastric emptying and feeds satiety-signaling gut bacteria, so a high-fiber diet curbs intake and is a cornerstone of the dietary pattern that, with activity, treats obesity.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Weight and mood feed each other: obesity and depression each raise the risk of the other through shared inflammation, cortisol, and inactivity, and several psychiatric drugs add weight — a loop that makes treating either alone harder.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Fat is an inflammatory organ: enlarged adipocytes and their macrophages secrete IL-6 into the blood, driving the liver's C-reactive protein and the insulin resistance that links obesity to diabetes and heart disease.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Inflammation in fat starts with T cells: CD8 cytotoxic T cells infiltrate expanding adipose tissue early and recruit the macrophages that sustain the chronic low-grade inflammation of obesity.
- `connects-to` → **[Gout](../gout/README.md)** — Excess weight crystallizes in the joints: obesity raises uric acid through insulin resistance and higher turnover, so it is a leading and reversible risk factor for gout and its painful attacks.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Fat secretes a pro-inflammatory signal: resistin from adipose tissue and macrophages promotes insulin resistance and vascular inflammation, one of the adipokines through which excess fat turns into metabolic and cardiovascular disease.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Excess weight scars the kidneys: obesity hyperfilters the glomeruli and, with the diabetes and hypertension it drives, produces obesity-related glomerulopathy that progresses to chronic kidney disease.
- `connects-to` → **[Stroke](../stroke/README.md)** — The weight reaches the brain's vessels: through hypertension, diabetes and atherosclerosis, obesity raises the risk of ischemic stroke, extending its cardiovascular toll beyond the heart to the cerebral circulation.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Overfed fat smolders with inflammation: free fatty acids and stressed adipocytes activate NF-κB in fat-resident macrophages, the master switch behind the chronic low-grade inflammation that links obesity to insulin resistance.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The brain stops hearing the satiety signal: leptin acts through JAK2-STAT3 in the hypothalamus to curb appetite, and obesity blunts this STAT3 signaling into leptin resistance, so high leptin no longer suppresses eating.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Excess weight thickens and slows the blood: obesity raises clotting factors and venous stasis, making it a major independent risk factor for deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Excess fat fuels a kidney cancer: obesity is a major modifiable risk factor for renal cell carcinoma, acting through insulin/IGF signaling, adipokines and chronic inflammation that promote renal tumorigenesis.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Fat is an inflammatory organ that feeds the plaques: adipose-derived TNF-α and IL-6 worsen psoriasis, so obesity raises its incidence and severity and blunts treatment response, a bidirectional inflammatory link.
- `connects-to` → **[Asthma](../asthma/README.md)** — Weight reshapes the airways: obesity drives a distinct, often steroid-resistant asthma phenotype through mechanical restriction of the chest and adipokine-driven airway inflammation, worsening control.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Reflux from excess weight scars toward cancer: central obesity promotes acid reflux and Barrett's esophagus, the precursor lesion behind the rising incidence of esophageal adenocarcinoma.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — It is an established pancreatic-cancer risk: obesity's chronic inflammation, hyperinsulinemia and altered adipokines raise the risk of pancreatic adenocarcinoma and worsen its outcomes.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Severe obesity can pressurize the lungs: obesity-hypoventilation and obstructive sleep apnea cause chronic hypoxia that constricts the pulmonary vasculature, contributing to pulmonary hypertension.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Adipose tissue is itself an endocrine organ: obesity drives insulin resistance, leptin and adipokine dysregulation, hypogonadism in men and polycystic ovary syndrome in women, sitting at the centre of endocrine disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Excess weight burdens the gut: obesity causes gastro-oesophageal reflux, gallstones and fatty-liver disease, and it is the leading target of bariatric surgery that reshapes the digestive tract.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Fat tissue heals badly: poorly vascularised adipose, higher wound tension and frequent diabetes make surgical-site infection and dehiscence far more common in obese patients.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Excess weight smothers breathing: obesity is the leading driver of obstructive sleep apnoea and can cause obesity hypoventilation (Pickwickian) syndrome, with daytime hypercapnia and right-heart strain.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It changes the skin in folds and friction: acanthosis nigricans, skin tags, intertrigo, hidradenitis suppurativa and venous stasis changes are common cutaneous consequences of obesity.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can raise pressure around the brain: obesity is the dominant risk factor for idiopathic intracranial hypertension (pseudotumor cerebri), causing headache, papilloedema and threatened vision.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It overworks the heart: excess weight raises cardiac output and workload, causing an obesity cardiomyopathy and atrial fibrillation, on top of the hypertension and atherosclerosis it drives.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Fat is an inflammatory organ: adipose tissue secretes inflammatory adipokines and cytokines, a chronic meta-inflammation that impairs immunity and blunts vaccine responses.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It clogs the lymphatic drainage: severe obesity impairs lymphatic function, causing obesity-related lymphoedema and, in the morbidly obese, massive localised lymphoedema.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It silently scars the kidney: obesity causes glomerular hyperfiltration and an obesity-related glomerulopathy (a secondary FSGS), an independent driver of chronic kidney disease.
- `connects-to` → **[Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — It treats the metabolic consequence: although weight loss and GLP-1 agonists are central, metformin manages the insulin resistance and type 2 diabetes that obesity drives.
- `connects-to` → **[Dietary Magnesium](../../../03-medicine/03-food/magnesium-dietary/README.md)** — Diet quality, not just quantity, matters: obesity is associated with low magnesium status that worsens insulin resistance, part of the micronutrient picture beyond calorie excess.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — It overworks the islets: obesity-driven insulin resistance forces pancreatic islet beta cells into chronic hyperinsulinaemia, and their eventual compensatory failure is the tipping point from obesity into type 2 diabetes.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It remodels the heart muscle: obesity causes left-ventricular hypertrophy, diastolic dysfunction and fatty infiltration — an obesity cardiomyopathy that, with the raised volume load, predisposes to heart failure and atrial fibrillation.
- `connects-to` → **[HCC](../hcc/README.md)** — It now drives liver cancer: through fatty liver and steatohepatitis, obesity has become a leading cause of hepatocellular carcinoma, which can even arise before frank cirrhosis in metabolic liver disease.
- `connects-to` → **[Binge-Eating Disorder](../binge-eating-disorder/README.md)** — The commonest eating disorder behind it: binge-eating disorder, with recurrent loss-of-control overeating, is a major driver of weight gain and obesity, and treating it (CBT, lisdexamfetamine) aids weight control.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It hardens the arteries: obesity accelerates atherosclerosis and arterial stiffening through chronic low-grade inflammation, insulin resistance and dyslipidaemia, the vascular path to its cardiovascular disease.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — It overworks the kidney's filter: obesity causes glomerular hyperfiltration and a secondary focal segmental glomerulosclerosis—obesity-related glomerulopathy—an under-recognised cause of proteinuria and chronic kidney disease.
- `connects-to` → **[COVID-19](../covid-19-disease/README.md)** — A leading driver of severe COVID: obesity was among the strongest predictors of severe COVID-19, through impaired ventilation, a pro-inflammatory adipose milieu and underlying endothelial dysfunction.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Midlife adiposity and the brain: midlife obesity raises the risk of later dementia, with insulin resistance, vascular injury and chronic neuroinflammation linking excess fat to Alzheimer's disease.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — An overlooked cancer link: obesity is an established risk factor for multiple myeloma and for the progression of its precursor MGUS, adding a haematologic malignancy to obesity's cancer toll.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Another obesity-linked cancer: rising body mass index raises the risk of thyroid cancer, part of obesity's broad oncogenic reach through insulin/IGF-1 signalling, sex hormones and chronic inflammation.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Fat in the liver: obesity drives triglyceride accumulation in the hepatocytes of the hepatic lobule, the steatosis that begins non-alcoholic fatty liver disease and can progress to NASH and cirrhosis.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Obesity and atrial fibrillation: excess adiposity—through atrial stretch, epicardial fat and inflammation—is a leading modifiable driver of atrial fibrillation, and weight loss can reduce its burden.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Adipose hypoxia: as fat mass outgrows its blood supply, HIF-1α activation in hypoxic adipose tissue drives the inflammation and fibrosis central to obesity's metabolic dysfunction.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Nutrient sensing: chronic overnutrition keeps mTOR signalling active in adipose and muscle, promoting fat storage and contributing to the insulin resistance of obesity.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — Energy gauge: AMPK, the cell's low-energy sensor, is blunted in obesity, reducing fat oxidation and glucose uptake—its reactivation is a key target of metformin and exercise.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Adipose macrophage recruitment: CCL2 released by stressed adipocytes draws monocytes into expanding fat, where they become the crown-like macrophages that drive obesity's chronic low-grade inflammation.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Metabolic inflammasome: excess lipids and danger signals activate the NLRP3 inflammasome in adipose macrophages, releasing IL-1β that impairs insulin signalling and links obesity to type 2 diabetes.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — Receptor-level resistance: inflammatory and lipid signals impair insulin-receptor signalling in obese liver, muscle and fat, the molecular core of the insulin resistance that defines metabolic obesity.
- `connects-to` → **[Endocannabinoid](../../03-molecular/endocannabinoid/README.md)** — An overactive endocannabinoid system stimulates CB1 receptors in the hypothalamus and adipose tissue to promote feeding and fat storage—the target of the CB1 antagonist rimonabant, withdrawn for psychiatric effects but validating the pathway in obesity.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Hypothalamic orexin integrates arousal with feeding behavior and energy expenditure, part of the central circuitry whose dysregulation contributes to the disordered appetite control and reduced spontaneous activity of obesity.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Saturated fatty acids directly activate TLR4 on adipocytes and macrophages, igniting the NF-κB-driven "metaflammation" that mechanistically links the excess lipid of obesity to systemic insulin resistance and type 2 diabetes.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF signaling through TrkB sits downstream of the hypothalamic melanocortin (MC4R) pathway controlling energy balance, and rare BDNF/TrkB mutations cause severe early-onset human obesity, marking it as a core appetite regulator.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGF21 acting through FGFR1c with β-Klotho promotes fat oxidation, browning of white adipose tissue and energy expenditure, an endocrine axis being targeted by FGF21 analogues for obesity and its metabolic complications.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Expanding fat depots require VEGF-driven angiogenesis to vascularize, and when adipose growth outstrips its blood supply the resulting hypoxia drives the inflammation and fibrosis of dysfunctional obese adipose tissue.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Insulin signaling through AKT (insulin-receptor already mapped) is progressively impaired in expanding, inflamed adipose tissue, the molecular basis of the insulin resistance linking obesity to type-2 diabetes.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — The NLRP3 inflammasome (already mapped) in adipose-tissue macrophages generates IL-1β, a key driver of the chronic low-grade inflammation that produces the metabolic complications of obesity.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Glucagon governs hepatic glucose output and energy expenditure, and glucagon/GLP-1 dual-agonist drugs exploit this axis (alongside the GLP-1 already mapped) to drive weight loss in obesity.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — The insulin receptor (mapped) signals through IRS-PI3K to AKT (mapped), and blunting of this PI3K branch in overnourished tissue is the molecular core of obesity-associated insulin resistance.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Saturated fatty acids and gut-derived LPS activate adipose-tissue TLR4 (mapped) through MyD88 to NF-κB (mapped), driving the macrophage inflammation that links obesity to insulin resistance.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — AKT normally inhibits GSK-3β to switch on glycogen synthesis, and elevated GSK-3β activity in obesity impairs insulin action and glucose storage.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Leptin signals through the JAK2-STAT3 axis (leptin and STAT3 mapped) in hypothalamic neurons; leptin resistance at this node underlies the failure of satiety signaling in obesity.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by adipose-tissue macrophages drives the chronic low-grade inflammation and fibrosis of expanding fat depots in obesity.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — The adipocyte-derived complement axis (C3/adipsin) is upregulated in obesity and contributes to adipose inflammation and metabolic dysfunction.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Mitochondrial and metabolic stress in expanding adipose tissue releases cytosolic DNA that engages cGAS-STING, fueling the metabolic inflammation of obesity.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling drives the adipose-tissue fibrosis that accompanies the dysfunctional expansion of fat in obesity.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the pro-inflammatory macrophage polarization of obese adipose tissue, linking immunity to metabolic dysfunction.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO1 integrates insulin-PI3K-AKT signaling (AKT and PIK3CA already mapped) to control adipocyte differentiation and hepatic metabolism dysregulated in obesity.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by adipose-tissue macrophages amplify the chronic low-grade metabolic inflammation of obesity.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling contributes to adipogenesis and the inflammatory adipocyte stress response of obese adipose tissue.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic CD8 T cells accumulate in obese adipose tissue and drive the immune activation underlying obesity-associated insulin resistance.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the inflammatory and insulin-resistance signaling of obese adipose tissue.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D signaling regulates adipocyte differentiation and the metabolic-inflammatory programming of adipose tissue in obesity.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the adipocyte and hypothalamic-neuron homeostasis whose dysregulation contributes to obesity.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic programming of adipogenesis and metabolic dysfunction in obesity.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte recruitment amplifies the adipose-tissue macrophage inflammation of obesity.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the adipose-tissue immune-cell recruitment and remodeling of obesity.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the adipose inflammation and metabolic dysregulation of obesity.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33-ILC2 signaling participates in the adipose-tissue immune homeostasis and thermogenesis relevant to obesity.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the adipogenic and metabolic gene programs of obesity.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the adipose-tissue immune activation and adipocyte biology of obesity.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the adipose-tissue macrophage infiltration and metaflammation of obesity.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Central satiety: oxytocin acts in the hypothalamus to reduce food intake and is under investigation as an anti-obesity target, adding a neuroendocrine appetite brake distinct from the leptin-ghrelin axis already mapped.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — Glucosuric weight loss: SGLT2 inhibitors cause urinary excretion of glucose and thus calories, producing modest weight loss and linking a renal glucose transporter to energy balance in the treatment of obesity-related metabolic disease.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Hyperuricaemia: adiposity raises xanthine-oxidase activity and serum urate, and the resulting hyperuricaemia links obesity to gout and to the endothelial dysfunction underlying its cardiovascular risk.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac injury: obesity strains the heart (already mapped) and accelerates atherosclerosis, and troponin elevation marks the myocardial injury of the cardiovascular disease that is the leading cause of death in the obese.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Adipose renin-angiotensin: adipose tissue produces angiotensinogen and components of a local renin-angiotensin system, and the resulting angiotensin II contributes to the hypertension (already mapped) that accompanies obesity.
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — Atherogenic dyslipidaemia: obesity raises triglycerides and small dense LDL, and PCSK9-regulated LDL-receptor handling contributes to the dyslipidaemia driving the accelerated atherosclerosis (already mapped) of the obese state.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Dyslipidaemia: obesity shifts cholesterol handling toward high triglycerides, low HDL and small dense LDL (PCSK9 already mapped), the atherogenic dyslipidaemia that is a core component of the metabolic syndrome.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Adipose mineralocorticoid axis: adipose tissue stimulates aldosterone release, and aldosterone acting through mineralocorticoid receptors promotes the hypertension, inflammation and fibrosis (angiotensin II already mapped) that accompany obesity.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory balance: the anti-inflammatory IL-10 counters the chronic low-grade inflammation of adipose tissue (TNF, IL-6 and IL-1 already mapped), and the imbalance toward pro-inflammatory signalling drives the insulin resistance of obesity.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Adipose M2 macrophages: IL-4 sustains the anti-inflammatory M2 macrophages (already mapped) of healthy lean adipose tissue (IL-10 already mapped), and the shift toward pro-inflammatory macrophages in obesity drives its insulin resistance.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Adipose eicosanoids: prostaglandins regulate adipogenesis and, from the inflamed adipose tissue (TNF and IL-6 already mapped), contribute to the low-grade inflammation and metabolic dysfunction of obesity.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Obesity and iron dysregulation: the chronic inflammation of obesity raises hepcidin, sequestering iron to cause a functional iron deficiency despite adequate stores, part of the disturbed metabolic milieu of the disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Adipose M2 maintenance: IL-13, with IL-4 (already mapped), maintains the anti-inflammatory M2 macrophages (already mapped) of the lean adipose tissue, and the loss of this type-2 signalling in obesity drives the inflammatory shift and insulin resistance.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil-M2 axis: IL-5 recruits the adipose eosinophils that sustain the M2 macrophages (already mapped) and metabolic health of lean fat, and their loss contributes to the adipose inflammation of obesity.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Functional iron deficiency: the obesity inflammation (IL-6 already mapped) raises hepcidin, which sequesters iron (already mapped) to cause the functional iron deficiency characteristic of obesity despite adequate stores.
- `connects-to` → **[Gut microbiome](../gut-microbiome/README.md)** — Microbiome-obesity link: the gut-microbiome composition (the energy harvest, the SCFAs, the endotoxaemia — TLR4 already mapped) influences the obesity and the metabolic state.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Cardiovascular risk: obesity drives the atherosclerosis (cholesterol and PCSK9 already mapped) and the cardiovascular disease, a leading obesity complication.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Beta-cell demand: the obesity-driven insulin (already mapped) resistance raises the demand on the pancreatic β-cells, whose eventual failure causes the type 2 diabetes.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Adipose NK meta-inflammation: the adipose-tissue NK cells (perforin already mapped) and their IFN-γ drive the type-1 meta-inflammation of the obese adipose tissue (macrophages already mapped).
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Adipose Th1 inflammation: the IFN-γ of the adipose-tissue T and NK cells drives the Th1 meta-inflammation that promotes the insulin (already mapped) resistance of obesity.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the chronic adipose meta-inflammation (TNF and IL-6 already mapped) of obesity.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic adipose meta-inflammation of obesity.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune arm whose loss accompanies the pro-inflammatory shift of the obese adipose tissue.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate metabolic interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the metabolic stress, contributes to the chronic adipose meta-inflammation of obesity.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Adipose CD4 shift: the CD4 T-helper cells shift from the lean-adipose Th2/Treg toward the Th1/Th17 (IFN-γ and IL-17 already mapped) phenotype, driving the meta-inflammation of the obese adipose tissue.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Adipose mast cells: the mast cells accumulate in the obese adipose tissue and contribute to the chronic low-grade inflammation and the insulin resistance of obesity.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Adipose fibrosis: the fibroblasts/myofibroblasts drive the extracellular-matrix remodelling and fibrosis of the expanding, hypoxic (HIF-1α already mapped) adipose tissue of obesity.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the adipose-tissue inflammation and the insulin resistance of obesity.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the macrophage (already mapped) recruitment into the inflamed adipose tissue of obesity.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Dysmetabolic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the adipose-tissue and systemic iron dysregulation of obesity.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Adipose alarmin: TSLP, secreted by adipocytes (already mapped) and adipose-stromal cells under lipotoxic stress, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the Type-2-skewed adipose inflammation of obesity.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-metabolic axis: bradykinin, generated by the kallikrein-kinin system elevated in obese adipose tissue, increases insulin sensitisation via B2 receptors on adipocytes (already mapped) and endothelial cells (already mapped) and modulates the vascular tone of obesity.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) over-activation in inflamed adipose tissue, moderating the immune-driven metabolic dysfunction of obesity.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell adipose effector: histamine, released by mast cells (already mapped) in expanded adipose tissue, promotes adipocyte (already mapped) lipolysis, amplifies the pro-inflammatory cytokine milieu (TNF-α and IL-6 already mapped) and accelerates insulin resistance of obesity.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Adipokine-EPO crosstalk: erythropoietin, acting via EPOR on adipocytes (already mapped) and macrophages (already mapped), promotes fat mass reduction and improves insulin sensitivity, counteracting the adipose inflammation of obesity.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Adipose ECM remodelling: periostin, expressed by fibroblasts and adipocyte precursors in expanding adipose tissue, promotes the fibrotic extracellular matrix remodelling and adipose tissue dysfunction that amplifies the chronic inflammation of obesity.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — OB factor-h: factor H regulates the alternative complement (C3 and C5 already mapped) in adipose tissue; impaired factor H activity amplifies the adipocyte (already mapped) lipotoxic and macrophage (already mapped) inflammatory phenotype of obesity.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — OB prolactin: prolactin modulates the gut-microbiome (already mapped) composition and leptin (already mapped) sensitivity in obesity; elevated prolactin promotes adipocyte (already mapped) lipogenesis and macrophage (already mapped) adipose inflammation.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — OB vasopressin: vasopressin, via V1 receptors on adipocytes (already mapped), promotes adipose inflammation and insulin resistance; V2-receptor signalling on the kidney (already mapped) drives the fluid retention and blood-pressure elevation of the obese cardiometabolic state.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — OB selenium: selenoprotein P controls adipocyte (already mapped) lipotoxic oxidative stress and macrophage (already mapped) adipose metainflammation; selenium deficiency amplifies the NF-κB (already mapped) inflammatory cascade and worsens insulin resistance in obesity.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — OB iodine: iodine-dependent thyroid hormones regulate the basal metabolic rate and adipocyte (already mapped) lipid turnover; thyroid-hormone deficiency amplifies the NF-κB (already mapped) adipose inflammation and deepens the energy-balance dysregulation of obesity.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — OB sodium: excess dietary sodium promotes adipocyte (already mapped) fluid retention and vascular inflammation through RAAS activation; sodium-driven hypertension amplifies the NF-κB (already mapped) adipose inflammatory cascade and the cardiometabolic burden of obesity.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Obesity copper: copper, as cytochrome c oxidase cofactor in adipocytes (already mapped) and macrophages (already mapped), supports mitochondrial function; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) metabolic-inflammatory cascade of obesity.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Obesity potassium: dietary potassium regulates macrophage (already mapped) and adipocyte (already mapped) membrane potential; potassium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) adipose inflammatory cascade of obesity.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Obesity zinc: zinc, as co-factor of insulin-signalling enzymes in adipocytes (already mapped) and macrophages (already mapped), modulates fat metabolism; zinc deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) metabolic-inflammatory adipose cascade.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Obesity calcium: calcium signals regulate macrophage (already mapped) and adipocyte (already mapped) lipid metabolism; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) adipose inflammation driving the mast-cell (already mapped) cascade of obesity.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Obesity phosphorus: phosphorus-dependent ATP and signalling lipids in macrophages (already mapped) and adipocytes (already mapped) govern energy partitioning; phosphate imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) adipose metabolic-inflammatory cascade.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Obesity carbon: carbon as backbone of adipokine and NF-κB (already mapped) proteins in adipocytes (already mapped) sustains adipose signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of obesity.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Obesity chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in adipose tissue; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) adipose inflammatory cascade of obesity.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Obesity nitrogen: nitrogen in amino-acid scaffold of adipokines (already mapped) and NF-κB (already mapped) proteins in adipocytes (already mapped) sustains adipose signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of obesity.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Obesity hydrogen: hydrogen, via redox homeostasis in adipocytes (already mapped) and macrophages (already mapped), supports leptin (already mapped) signalling; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) adipose cascade of obesity.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Obesity sulfur: sulfur in cysteine residues of leptin (already mapped) and adiponectin (already mapped) in adipocytes (already mapped) sustains thiol-redox balance; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of obesity.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Obesity PD-1: PD-1 on T-cells (already mapped) in adipose tissue suppresses cytotoxic immunity; PD-1 checkpoint dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) adipose inflammatory cascade of obesity.
- `connects-to` → **[WNT-β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Obesity wnt-beta-catenin: WNT/β-catenin on adipocytes (already mapped) and macrophages (already mapped) drives adipose lipid storage; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of obesity.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Obesity rankl: RANKL from macrophages (already mapped) and adipocytes (already mapped) promotes adipose immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) adipose cascade of obesity.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Obesity il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates adipose immune surveillance; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) adipose cascade of obesity.

[^bluher-2019-obesity-review]: Blüher M. Obesity: global epidemiology and pathogenesis. *Nat Rev Endocrinol.* 2019;15(5):288-298. [doi:10.1038/s41574-019-0176-8](https://doi.org/10.1038/s41574-019-0176-8) · [PubMed 30814686](https://pubmed.ncbi.nlm.nih.gov/30814686/)
[^wilding-2021-semaglutide-step1]: Wilding JPH, Batterham RL, Calanna S, et al. Once-weekly semaglutide in adults with overweight or obesity. *N Engl J Med.* 2021;384(11):989-1002. [doi:10.1056/NEJMoa2032183](https://doi.org/10.1056/NEJMoa2032183) · [PubMed 33567185](https://pubmed.ncbi.nlm.nih.gov/33567185/)
[^backhed-2004-gut-microbiome-obesity]: Bäckhed F, Ding H, Wang T, et al. The gut microbiota as an environmental factor that regulates fat storage. *Proc Natl Acad Sci USA.* 2004;101(44):15718-15723. [doi:10.1073/pnas.0407076101](https://doi.org/10.1073/pnas.0407076101) · [PubMed 15505215](https://pubmed.ncbi.nlm.nih.gov/15505215/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
