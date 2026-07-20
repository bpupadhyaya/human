---
schema: human-scale-entry/v1
id: alcohol-use-disorder
name: Alcohol Use Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Alcohol use disorder (14.5% lifetime) involves GABA-A potentiation → tolerance and withdrawal seizures (glutamate rebound), VTA-dopamine reward, and CRF-driven negative reinforcement; treatment: naltrexone, acamprosate, benzodiazepine detox, CBT, 12-step programs."
aliases: ["alcohol use disorder", "AUD", "alcoholism", "alcohol dependence", "AUDIT", "naltrexone", "acamprosate", "Wernicke-Korsakoff", "alcohol withdrawal", "CIWA"]
sources:
  - id: rehm-2017-aud-burden
    type: peer-reviewed
    cite: "Rehm J, Shield KD. Global Burden of Alcohol Use Disorders and Alcohol Liver Disease. Biomedicines. 2019;7(4):99."
    doi: "10.3390/biomedicines7040099"
    pmid: "31752397"
    url: "https://doi.org/10.3390/biomedicines7040099"
    accessed: "2026-06-08"
  - id: koob-2013-addiction-neuroscience
    type: peer-reviewed
    cite: "Koob GF, Volkow ND. Neurocircuitry of addiction. Neuropsychopharmacology. 2010;35(1):217-238."
    doi: "10.1038/npp.2009.110"
    pmid: "19710631"
    url: "https://doi.org/10.1038/npp.2009.110"
    accessed: "2026-06-08"
  - id: anton-2006-combine
    type: peer-reviewed
    cite: "Anton RF, O'Malley SS, Ciraulo DA, et al. Combined pharmacotherapies and behavioral interventions for alcohol dependence: the COMBINE study. JAMA. 2006;295(17):2003-2017."
    doi: "10.1001/jama.295.17.2003"
    pmid: "16670409"
    url: "https://doi.org/10.1001/jama.295.17.2003"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Alcohol potentiates GABA-A → sedation and tolerance; chronic use → GABA-A downregulation; abrupt cessation → GABA-A insufficiency → withdrawal seizures (6-48h) and delirium tremens (24-72h); GABRA2 (α2 subunit) polymorphisms are the strongest GWAS hit for AUD."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Alcohol inhibits NMDA receptors (NR2B) → blackouts; chronic use → compensatory NMDA upregulation; abrupt withdrawal → glutamate excitotoxicity → seizures and Wernicke-Korsakoff syndrome; acamprosate normalizes NMDA/GABA balance in protracted abstinence."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Alcohol stimulates VTA dopamine release → NAcc → euphoria and positive reinforcement; DRD2 Taq1A A1 allele → reduced D2 receptor density → compensatory drinking; naltrexone blocks opioid-mediated VTA DA release → reduces alcohol reward and craving."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Reduced serotonin in AUD → disinhibition and impulsivity; 5-HT3 receptors in NAcc amplify dopamine reward; ondansetron (5-HT3 antagonist) has modest efficacy in early-onset AUD (≤25 years); SSRIs are ineffective in AUD without comorbid depression."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Chronic alcohol reduces BDNF in NAcc and dorsomedial striatum → impairs BDNF-mediated braking on compulsive drinking; BDNF infusion into NAcc reduces ethanol preference in rodent models; abstinence partially restores BDNF; Val66Met BDNF SNP associated with AUD vulnerability."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "AUD weakens PFC-NAcc inhibitory control circuits; amygdala CRF hyperactivation drives negative reinforcement drinking; hippocampal neurogenesis is suppressed by chronic alcohol; partial brain volume recovery occurs after ≥6 months sustained abstinence."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "CRH in central amygdala/BNST mediates the negative reinforcement model of AUD: withdrawal stress → CeA CRH excess → anxiety and dysphoria → drinking to relieve distress; CRHR1 antagonists (antalarmin, verucerfont) reduce stress-induced alcohol seeking in animal models."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Alcohol stimulates β-endorphin → MOR on VTA GABAergic interneurons → disinhibition → DA surge; naltrexone (MOR/KOR antagonist) blocks this reward mechanism; OPRM1 A118G (Asn40Asp) SNP predicts superior naltrexone response — the basis for pharmacogenetic selection in AUD."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Alcohol withdrawal → NE hyperactivation → autonomic instability (tachycardia, hypertension, diaphoresis) — core CIWA-Ar items; clonidine (α2 agonist) reduces LC-NE firing during withdrawal; chronic alcohol disrupts NE synthesis and α2 autoreceptor sensitivity."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "NPY reduces voluntary alcohol intake via limbic anxiolysis; Y2R knockout mice consume 2× more alcohol; alcohol withdrawal depletes limbic NPY → anxiety → relapse; Y1R agonism in CeA reduces stress-induced alcohol-seeking; NPY is a candidate pharmacotherapy for AUD relapse."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver bears the brunt of alcohol use disorder: ethanol metabolism to acetaldehyde and a shifted NADH/NAD ratio drive steatosis → alcoholic hepatitis → fibrosis and cirrhosis; abstinence reverses early disease, but cirrhosis is the gateway to liver failure and cancer."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Alcohol use disorder is a major cause of hepatocellular carcinoma: alcoholic cirrhosis is the inflamed, regenerating background on which HCC arises, and alcohol multiplies the risk from hepatitis B/C—so HCC surveillance is essential once cirrhosis develops."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Alcohol and opioid use disorders frequently co-occur and are dangerous together: both are CNS depressants, so combined use multiplies respiratory depression and overdose death; they share reward and stress circuitry, and concurrent alcohol complicates opioid agonist therapy."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Alcohol and stimulant use disorders frequently co-occur and interact dangerously: alcohol is used to come down from stimulants, cocaine plus alcohol forms toxic cocaethylene, and both engage overlapping dopamine reward circuitry—so polysubstance use worsens outcomes."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Alcohol use disorder and depression are intertwined and bidirectional: people drink to relieve low mood, but alcohol is a depressant that deepens depression and suicide risk, and both share serotonergic and stress-axis dysregulation—so both need treating together."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Hepatocytes bear the metabolic brunt of alcohol: they oxidize ethanol via alcohol dehydrogenase and CYP2E1, generating acetaldehyde and ROS that cause fatty change, ballooning, and death—so steatosis, hepatitis, and cirrhosis trace to hepatocyte injury."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Alcohol is a direct cause of esophageal cancer: its metabolite acetaldehyde is a carcinogen that damages esophageal DNA, so heavy drinking—especially with smoking—markedly raises squamous-cell esophageal cancer risk, one of several alcohol-attributable cancers."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Alcohol is directly toxic to cardiomyocytes: chronic heavy drinking causes alcoholic cardiomyopathy, where ethanol and acetaldehyde impair contractile proteins and mitochondria, dilating the heart and causing heart failure that can partly reverse with abstinence."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Alcohol use disorder dysregulates cortisol: heavy drinking activates the HPA axis, producing a pseudo-Cushing's state with high cortisol, and withdrawal spikes it further—contributing to the anxiety, sleep disruption and relapse that mark early abstinence."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Alcohol remodels neurons toward dependence: it potentiates inhibitory GABA and blocks excitatory NMDA receptors acutely, so neurons adapt by upregulating excitation—unmasked as the tremor, seizures and delirium of withdrawal when drinking stops."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Alcohol and NASH cause overlapping fatty-liver disease: heavy drinking and metabolic syndrome both deposit fat that inflames and scars the liver, and the two are often combined—so distinguishing alcohol- from metabolism-driven steatohepatitis guides treatment."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Alcohol use disorder damages the gut-liver axis: alcohol disrupts the gut microbiome and leaks bacterial endotoxin through an inflamed barrier, and this endotoxemia drives the liver inflammation that turns heavy drinking into hepatitis and cirrhosis."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Alcohol is a leading cause of pancreatitis: it triggers premature enzyme activation that digests the pancreas, causing acute attacks and, with chronic use, permanent damage with diabetes and malabsorption—so the pancreas is among alcohol's prime organ targets."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Alcohol crosses the placenta freely: with no safe level in pregnancy, it disrupts fetal brain development, causing fetal alcohol spectrum disorders with lifelong cognitive and facial features—so alcohol use disorder in pregnancy carries permanent fetal harm."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Alcohol is an under-recognized breast cancer cause: even moderate drinking raises risk by increasing estrogen and generating DNA-damaging acetaldehyde, so alcohol is now counted among the modifiable risk factors for hormone-driven breast cancer."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Heavy drinking and thiamine loss devastate the hippocampus: Wernicke-Korsakoff syndrome and alcohol-related brain damage impair this memory hub, causing the dense amnesia and confabulation of Korsakoff's—why thiamine is given urgently in alcohol withdrawal."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Alcohol is a proven cause of colorectal cancer: its metabolite acetaldehyde damages DNA and it depletes folate, so even moderate drinking raises colorectal risk—one of several cancers (with breast and liver) alcohol drives."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Alcohol leaves a fingerprint in red cells: it is directly toxic to marrow and, with folate/B12 deficiency, enlarges red cells, so macrocytosis (high MCV) is a classic clue to chronic heavy drinking."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Heavy drinking drains the body of magnesium: alcohol makes the kidneys waste it and poor intake compounds the loss, so the resulting hypomagnesemia worsens withdrawal tremor and seizures and destabilizes the heart's rhythm."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Alcohol dependence reshapes synapses: chronic drinking shifts the balance of excitatory and inhibitory synaptic signaling, so the brain adapts to the drug—and the rebound when it is removed produces the dangerous withdrawal syndrome."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Alcohol injures the stomach directly: it inflames and erodes the gastric lining, causing gastritis and bleeding ulcers, and the vomiting of heavy use can tear the junction with the esophagus—common reasons drinkers bleed."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Heavy drinking can acidify the blood: starved and metabolizing alcohol, the body makes ketones and lactate, so alcoholic ketoacidosis drops blood pH—a dangerous acidosis that can appear even with near-normal sugar."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Alcohol weakens and destabilizes the heart: years of drinking dilate and weaken the muscle into alcoholic cardiomyopathy, while even a binge can trigger atrial fibrillation—the so-called holiday heart."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Alcohol drops the platelet count: it suppresses their production in the marrow and shortens their life, so heavy drinkers bruise and bleed easily, a count that often rebounds within days of stopping."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging reveals alcohol's toll: brain MRI shows the shrinkage and the mammillary-body changes of Wernicke's, and fMRI photons map the reward-circuit response that drives craving."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Alcohol poisons the peripheral nerves: direct toxicity and thiamine deficiency cause a painful, numbing length-dependent neuropathy, one of its most common neurological harms."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Chronic drinking depletes zinc: poor intake and gut losses lower it, contributing to the skin problems, poor wound healing and weakened immunity seen in alcohol use disorder."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows alcohol's mark on the liver cell: fat droplets swell the hepatocyte, the cytoskeleton tangles into Mallory-Denk bodies, and giant megamitochondria appear, the ultrastructure of alcoholic liver injury."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The failing liver writes on the skin: spider angiomata, palmar erythema, jaundice, and the dilated caput medusae veins are visible stigmata that betray the chronic liver damage of heavy drinking."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Drinkers run dangerously low on phosphorus: poor intake and the shifts of refeeding can crash blood phosphate, sapping the energy molecule ATP and causing the muscle weakness and rhabdomyolysis seen in alcohol use disorder."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Alcohol is directly toxic to the marrow: it enlarges red cells into macrocytosis, drops platelets, and suppresses all the blood lines, on top of the folate deficiency that compounds the anemia in heavy drinkers."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Alcohol unbalances the sex hormones: chronic use causes testicular atrophy, low testosterone, and gynecomastia in men and menstrual disruption in women — and in pregnancy it crosses the placenta to cause fetal alcohol spectrum disorder."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Drinking disarms the body's defenders: alcohol impairs neutrophil function and numbers, which is why heavy drinkers are prone to pneumonia, tuberculosis, and severe infection."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Alcohol wrecks the body's clock: it suppresses melatonin and fragments sleep, so the sedation of a nightcap gives way to rebound insomnia and vivid dreams — and withdrawal brings severe sleeplessness that drives relapse."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Drinking quietly thins the bones: alcohol directly suppresses osteoblasts and disturbs calcium and vitamin D, so chronic use causes osteoporosis and, with the falls it provokes, a high fracture risk."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Heavy drinking injures the vessel lining: alcohol harms endothelial cells and raises blood pressure, contributing to the cardiomyopathy, arrhythmia, and stroke risk that offset any benefit of light consumption."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Alcohol unmans the hormones: it suppresses testosterone production and speeds its conversion to estrogen, causing the low libido, shrunken testes, and feminization seen in chronic male drinkers."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The liver's macrophages drive alcoholic hepatitis: gut-derived endotoxin activates Kupffer cells to pour out TNF and other cytokines, the inflammatory engine that turns fatty liver into hepatitis and fibrosis."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Alcohol is a leading reversible cause of high blood pressure: intake raises it dose-dependently through sympathetic and hormonal effects, so cutting back is a frontline step that often lowers blood pressure measurably."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Alcohol inflames the brain's immune cells: ethanol and gut-derived endotoxin activate microglial TLR4, and the cytokines they release drive the neuroinflammation behind alcohol-related cognitive decline and craving."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Heavy drinking tips the brain toward bleeding: alcohol raises blood pressure and impairs clotting, sharply increasing hemorrhagic stroke risk, while binge drinking can trigger ischemic stroke through arrhythmia and surges in pressure."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Alcohol use disorder shadows bipolar disorder: it is among the commonest comorbidities, used to self-medicate mood swings yet worsening the course, raising suicide risk, and complicating diagnosis and treatment of both."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Alcohol throws the inflammation switch in liver and brain: ethanol and gut-derived endotoxin activate NF-κB in Kupffer cells and microglia, driving the alcoholic hepatitis and neuroinflammation behind much of the organ damage."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It corrodes the nervous system on many fronts: beyond intoxication, alcohol drives withdrawal seizures, thiamine-deficient Wernicke-Korsakoff encephalopathy, cerebellar degeneration and peripheral neuropathy."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Heavy drinking cripples the body's defenses: alcohol impairs neutrophil and macrophage function and, with aspiration and cirrhosis, leaves patients prone to pneumonia, spontaneous bacterial peritonitis and sepsis."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Repeated pancreatitis paves the way to cancer: heavy alcohol use is a leading cause of chronic pancreatitis, and the resulting long-standing inflammation raises the risk of pancreatic adenocarcinoma."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Chronic drinking can dilate the heart: sustained heavy alcohol use causes an alcoholic cardiomyopathy, a dilated, weakened heart that is a recognized and partly reversible cause of heart failure."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "It harms the kidney directly and through the liver: heavy alcohol drives hypertension and, in cirrhosis, hepatorenal physiology, while binge drinking can cause rhabdomyolysis — together threatening chronic kidney disease."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Heavy drinking poisons the peripheral nerves: chronic alcohol use, with its thiamine and B-vitamin deficiency, causes a length-dependent axonal neuropathy producing burning pain and numbness in the feet."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "Alcohol is a major head-and-neck carcinogen: ethanol and its metabolite acetaldehyde damage the mucosa of the mouth, throat and larynx, and combined with tobacco multiply the risk of head and neck squamous-cell cancer."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety and drinking feed each other: people drink to quell anxiety, but tolerance and withdrawal raise baseline anxiety, locking the two into a self-reinforcing cycle."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It ravages the gut from end to end: alcohol causes gastritis and Mallory-Weiss tears, acute and chronic pancreatitis, and the alcoholic hepatitis and cirrhosis with varices that define end-stage liver disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It disrupts the hormones and fuel control: chronic alcohol causes hypogonadism, a pseudo-Cushing's state and dangerous hypoglycaemia, and pancreatitis can destroy the islets into diabetes."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It disarms host defence: alcohol impairs neutrophil and lymphocyte function and ciliary clearance, leaving people with alcohol use disorder prone to pneumonia, tuberculosis and severe infection."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It disturbs the heart's rhythm and muscle: binge drinking triggers 'holiday heart' atrial fibrillation, and chronic use causes a dilated alcoholic cardiomyopathy alongside the hypertension it drives."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It wastes muscle and kills bone: acute and chronic alcoholic myopathy weaken proximal muscles, and alcohol is a leading cause of avascular necrosis of the femoral head."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Liver damage shows on the skin: spider naevi, palmar erythema and telangiectasia of alcohol-related liver disease appear on the skin, and alcohol can trigger porphyria cutanea tarda and psoriasis."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It opens the lungs to infection: alcohol impairs cough and airway defences, raising the risk of aspiration pneumonia, community-acquired pneumonia and tuberculosis, and predisposing to ARDS."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It unbalances fluids and salts: heavy drinking causes profound hypomagnesaemia and hypophosphataemia, and rhabdomyolysis or hepatorenal syndrome can precipitate acute kidney injury."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "Drinking drains magnesium: chronic alcohol use depletes body magnesium, contributing to the tremor, arrhythmia and seizures of withdrawal, so replacement is routine."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Drinking raises the risk: heavy alcohol use roughly triples the risk of active tuberculosis through impaired immunity, malnutrition and social exposure, a major driver of the global TB burden."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Trauma and drinking entwine: alcohol use disorder and PTSD frequently co-occur, as people drink to numb intrusive memories and hyperarousal, each disorder worsening the other."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Alcohol starves the bone-builders: chronic alcohol suppresses osteoblast activity and bone formation, a key mechanism behind the osteoporosis and fracture risk of alcohol use disorder."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It scars the liver lobule: chronic alcohol drives steatosis, alcoholic hepatitis and pericentral fibrosis in the hepatic lobule, progressing to cirrhosis — the classic and often fatal organ damage of alcohol use disorder."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It weakens the heart muscle: sustained heavy drinking causes a dilated alcoholic cardiomyopathy and, acutely, atrial fibrillation ('holiday heart'), adding cardiac failure to the harms of alcohol use disorder."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Alcohol is a carcinogen: it causes cancers of the mouth, throat, oesophagus, liver, colon and breast — malignancies treated with chemotherapy — making alcohol use disorder a major and preventable cancer risk."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "'Holiday heart': binge and chronic drinking trigger atrial fibrillation and other arrhythmias through the conduction system, on top of alcoholic cardiomyopathy."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Withdrawal seizures: abrupt cessation in alcohol dependence unmasks GABA-rebound hyperexcitability, causing withdrawal seizures and status epilepticus—a medical emergency."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Alcohol and urate: beer and spirits raise serum uric acid and precipitate gout attacks, a classic dietary trigger of the disease in heavy drinkers."
  - target: 01-human/07-system/hereditary-pancreatitis
    relation: connects-to
    note: "Alcohol and the pancreas: alcohol is the leading cause of chronic pancreatitis and dramatically accelerates disease in those with hereditary pancreatitis (PRSS1), compounding genetic and toxic injury."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Alcohol and dementia: heavy chronic drinking causes alcohol-related brain damage and raises later dementia risk including Alzheimer's, through thiamine deficiency, direct neurotoxicity and vascular injury."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Anaemia of drinking: alcohol causes anaemia through gastrointestinal and variceal bleeding, marrow suppression and folate deficiency—often a mix of iron-deficiency and macrocytic anaemia."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Alcoholic lung: chronic drinking impairs alveolar defence and depressed consciousness drives aspiration, raising the risk of aspiration pneumonia, lung abscess and acute respiratory distress syndrome."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Pneumococcal susceptibility: alcohol blunts neutrophil and macrophage function, making heavy drinkers prone to severe, bacteraemic pneumococcal pneumonia and invasive disease."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Impaired healing: alcohol disrupts collagen deposition, immune defence and angiogenesis, slowing wound healing and raising surgical-site infection and post-operative complication rates."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Alcoholic inflammation: gut-derived endotoxin in alcohol use disorder drives Kupffer-cell TNF-α release, a central mediator of alcoholic hepatitis and the neuroinflammation of dependence."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Hepatic and brain inflammation: IL-6 rises with chronic alcohol intake, contributing to liver injury, the acute-phase response and the neuroinflammation linked to alcohol-related cognitive decline."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: alcohol and its metabolites activate the NLRP3 inflammasome in liver and brain, releasing IL-1β to drive alcoholic liver disease and neuroinflammation."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Gut-brain endotoxin axis: alcohol increases gut permeability, letting bacterial LPS engage TLR4 on Kupffer cells and microglia, a central trigger of alcoholic liver injury and neuroinflammation."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "Reward and craving: the endocannabinoid system modulates alcohol's rewarding effects and craving through CB1 signalling in the mesolimbic circuit, an emerging therapeutic target in alcohol use disorder."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Acute intoxication and tolerance: alcohol raises extracellular adenosine, contributing to its sedative and motor-incoordinating effects, while adaptation in adenosine signalling features in tolerance and withdrawal."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Craving and arousal: hypothalamic orexin drives the cue- and stress-induced craving and the hyperarousal of alcohol withdrawal, making orexin-receptor antagonists a candidate to reduce relapse in alcohol use disorder."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Appetitive craving: ghrelin enhances the rewarding value of alcohol and promotes alcohol seeking, a gut-brain hunger signal repurposed in addiction whose blockade reduces drinking in trials."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Cholinergic reward: nicotinic acetylcholine receptors modulate alcohol's dopaminergic reward, the mechanistic basis for the nicotinic partial agonist varenicline reducing alcohol consumption in alcohol use disorder."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Anti-craving target: GLP-1 receptor agonists like semaglutide reduce alcohol craving and consumption by acting on the mesolimbic reward circuit, an emerging metabolic-pathway therapy generating strong interest for alcohol use disorder."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Alcoholic liver fibrosis: chronic alcohol activates hepatic stellate cells through TGF-β to deposit collagen, driving the progression from steatosis to the alcoholic cirrhosis that is a leading cause of death in alcohol use disorder."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Withdrawal and craving: oxytocin dampens stress and craving and can ease alcohol-withdrawal severity in studies, an endogenous social-bonding system being explored as an adjunct to reduce relapse in alcohol use disorder."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Reward plasticity: alcohol engages dopamine-driven ERK signalling in the striatal reward circuitry, the synaptic plasticity that consolidates alcohol reward and craving."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Withdrawal stress: the cortisol/CRH stress response of alcohol withdrawal (already mapped) acts through the glucocorticoid receptor, the HPA dysregulation that drives negative-affect relapse in alcohol use disorder."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative injury: alcohol metabolism generates reactive oxygen species and acetaldehyde, and the NRF2 antioxidant response defends against the oxidative damage underlying alcoholic liver disease and neurotoxicity."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Gut-liver-brain inflammation: alcohol-driven gut-barrier disruption releases microbial products that engage TLR4-MyD88-NF-κB signalling (TLR4 and NF-κB already mapped), driving the systemic and neuroinflammation that sustain alcohol use disorder."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Addiction plasticity: mTOR-dependent synaptic plasticity in the mesolimbic reward circuit consolidates the maladaptive learning and cue associations that entrench compulsive alcohol use."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophic adaptation: BDNF signalling through its TrkB receptor (NTRK) mediates the reward-circuit synaptic adaptations underlying alcohol craving and relapse vulnerability."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (mTOR mapped) participates in the reward-circuit synaptic plasticity and neuroadaptations of alcohol use disorder."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Alcohol-induced microglial and Kupffer-cell activation induces galectin-3, amplifying the neuroinflammation and hepatic injury of alcohol use disorder."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-driven JAK-STAT signalling (IL-6 mapped) transduces the systemic and neuroinflammation accompanying chronic alcohol exposure."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling in reward and stress circuits shapes the synaptic plasticity underlying dependence and relapse in alcohol use disorder."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling (JAK1/2 already mapped) transduces the systemic and neuroinflammatory tone driven by chronic alcohol exposure, including alcoholic liver disease."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic and gut-derived microbial DNA engages cGAS-STING, contributing to the TLR4-associated hepatic and neuroinflammation of alcohol use disorder."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates the neuronal and hepatic oxidative-stress handling relevant to the neuroadaptations and organ injury of alcohol use disorder."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 neuroinflammatory signaling contributes to the inflammatory tone of chronic alcohol use disorder."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the gut-derived-endotoxemia-driven myeloid inflammation linked to alcohol use disorder and alcoholic liver disease."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and oxidative-stress adaptation participates in the alcohol-associated liver and neural stress of alcohol use disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) mediates the synaptic-plasticity neuroadaptations of the reward circuit in alcohol use disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation in the reward circuit contributes to the persistent neuroadaptations and relapse vulnerability of alcohol use disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the hepatic and neuronal metabolic adaptation of alcohol use disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal and hepatic responses to the chronic ethanol exposure of alcohol use disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with alcohol use disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the NMDA-receptor and synaptic-plasticity mechanisms of the reward circuitry implicated in alcohol use disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and reward-circuit processes implicated in alcohol use disorder."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven neuroinflammation (glial activation) participates in the reward-circuit changes and neurotoxicity of alcohol use disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory responses implicated in alcohol use disorder."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with alcohol use disorder."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the microglial and neuroinflammatory processes implicated in alcohol use disorder."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences: women develop alcohol-related organ damage at lower exposures (telescoping), and estrogen with sex-based differences in alcohol metabolism contributes to this greater vulnerability in alcohol use disorder."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative metabolism: ethanol metabolism and xanthine-oxidase activity generate reactive oxygen species and uric acid, contributing to the oxidative liver injury and the hyperuricaemia and gout associated with heavy drinking."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Alcoholic cardiomyopathy: chronic heavy drinking causes a dilated cardiomyopathy, and troponin release can mark the myocardial injury of this under-recognised cardiac complication of alcohol use disorder."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Alcohol-related anaemia: heavy drinking lowers haemoglobin through a direct marrow toxicity, folate deficiency causing macrocytosis, and gastrointestinal and variceal bleeding from the associated liver disease (already mapped)."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Pseudo-Cushing and hypertension: alcohol activates the HPA and renin-angiotensin-aldosterone systems (cortisol already mapped), contributing to the hypertension and the pseudo-Cushing state seen in alcohol use disorder."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Glucose dysregulation: alcohol acutely inhibits gluconeogenesis to cause hypoglycaemia, while chronic pancreatic damage (pancreas already mapped) impairs insulin secretion, giving alcohol use disorder complex effects on glucose control."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Lipid effects: alcohol raises HDL yet also drives hypertriglyceridaemia and, in heavy use, an atherogenic dyslipidaemia (insulin already mapped), giving alcohol complex, dose-dependent effects on cholesterol and cardiovascular risk."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Electrolyte depletion: the poor intake, vomiting and renal losses of alcohol use disorder deplete potassium, and with the magnesium deficiency (already mapped) this predisposes to the arrhythmias and weakness of the malnourished drinker."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the glial neuroinflammation (TLR4 and microglia already mapped) and the alcoholic hepatitis contribute to the neuro- and hepato-inflammation of alcohol use disorder."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 anti-inflammatory arm: IL-4 polarises the microglia (already mapped) and the hepatic Kupffer cells toward an M2 phenotype, countering the TLR4-driven (already mapped) neuro- and hepato-inflammation of alcohol use disorder."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Alcohol and iron: alcohol suppresses hepcidin, promoting the intestinal iron hyperabsorption and hepatic iron loading that aggravate the oxidative (xanthine oxidase already mapped) liver injury of alcohol use disorder."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Hepatic iron overload: the hepcidin suppression (already mapped) and the direct effects of alcohol load the liver with iron (haemoglobin already mapped), the iron-catalysed oxidative stress worsening the alcoholic liver disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Profibrotic type-2 arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) and profibrotic (TGF-β already mapped) response of the alcoholic liver fibrosis in alcohol use disorder."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Hepatic stellate cells: the fibroblast-like hepatic stellate cells, activated (TGF-β and IL-13 already mapped) by the alcoholic liver injury, lay down the collagen (already mapped) fibrosis that progresses to cirrhosis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine and metabolism: alcohol alters the adipokine leptin of the appetite and craving and the metabolic (insulin already mapped) dysregulation, part of the systemic and hepatic metabolic disturbance of alcohol use disorder."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Hepatoprotective adipokine: adiponectin, with leptin (already mapped), is the hepatoprotective adipokine whose fall in the alcoholic liver disease promotes the steatosis and the fibrosis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the alcoholic steatohepatitis and the metabolic disturbance of alcohol use disorder."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Polysubstance comorbidity: alcohol and cannabis use disorders commonly co-occur (with the opioid use disorder already mapped), the shared reward-circuit (dopamine already mapped) addiction vulnerability."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the gut-derived (TLR4 already mapped) stress, drives the inflammation of the alcoholic liver (already mapped) of alcohol use disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 inflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune-mediated inflammation (IL-6 and TNF already mapped) of the alcoholic steatohepatitis of alcohol use disorder."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of alcohol use disorder."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the alcoholic liver disease of alcohol use disorder."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the gut-derived (TLR4 already mapped) inflammation of the alcoholic steatohepatitis of alcohol use disorder."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of alcohol use disorder."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the blood-brain-barrier disruption implicated in alcohol use disorder."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic arm: the cytotoxic T cells (perforin pathway) contribute both to the psychoneuroimmunology of the chronic alcohol exposure and to the hepatocyte (already mapped) injury of the alcoholic liver disease of alcohol use disorder."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astroglial neurotoxicity: the astrocytes of the brain (already mapped) are damaged by the chronic alcohol and, with the microglia (already mapped), mediate the neuroinflammation and the neurodegeneration of alcohol use disorder."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the Kupffer-cell (macrophage already mapped) activation of the alcoholic liver disease of alcohol use disorder."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the hepatic and neuroinflammatory myeloid activation of alcohol use disorder."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Alcoholic iron overload: transferrin (and its carbohydrate-deficient form, a biomarker of chronic use), the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the hepatic iron overload of alcohol use disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-gut axis: TSLP, from gut epithelium (already mapped) under the dysbiosis and the alcohol-induced barrier disruption, primes mast cells (already mapped) and dendritic cells (already mapped) and amplifies the hepatic neuroinflammation of alcohol use disorder."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-hepatic axis: bradykinin, via B1/B2 receptors on Kupffer cells (macrophage already mapped) and hepatic stellate cells, amplifies the portal inflammation and the fibrogenic activation of the alcoholic liver disease of alcohol use disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact/complement brake: the C1-esterase inhibitor regulates the classical complement (C3, C5 already mapped) and contact pathways whose activation contributes to the hepatic and neuroinflammatory injury of alcohol use disorder."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell hepatic effector: mast cells (already mapped) in the alcoholic liver stroma release histamine that amplifies the Kupffer-cell (macrophage already mapped) activation and the portal inflammatory milieu of the alcoholic liver disease of alcohol use disorder."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Alcohol-anaemia erythropoiesis: erythropoietin drives red-cell recovery from the multifactorial anaemia of alcohol use disorder; alcohol suppresses EPO production and the bone-marrow (already mapped) response, worsening the nutritional and hepatic anaemia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H limits the alternative-pathway activation (C3, C5 and C5aR1 already mapped) in the hepatic (liver already mapped) and CNS compartments, moderating the complement-driven Kupffer-cell (already mapped) activation of alcoholic liver disease."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "AUD prolactin: prolactin, via PRLR on neurons (already mapped) and microglia (already mapped), modulates HPA-axis (CRH already mapped) tone; hyperprolactinaemia amplifies the cortisol (already mapped) and dopamine (already mapped) craving cascade of alcohol use disorder."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "AUD vasopressin: vasopressin, via V1aR on neurons (already mapped) and astrocytes (already mapped), modulates HPA-axis stress; vasopressin excess amplifies the CRH (already mapped) and cortisol (already mapped) withdrawal cascade of alcohol use disorder."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "AUD selenium: selenium, as GPx in hepatocytes (already mapped) and neurons (already mapped), scavenges alcohol-induced ROS; selenium deficiency amplifies the NF-κB (already mapped) and NLRP3 (already mapped) hepatic neuroinflammatory cascade of alcohol use disorder."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "AUD iodine: iodine-dependent thyroid hormones modulate hepatic alcohol metabolism and neuronal GABA (already mapped) tone; iodine deficiency impairs thyroid regulation of the CRH (already mapped) and dopamine (already mapped) craving cascade of alcohol use disorder."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "AUD sodium: heavy alcohol use activates renin-angiotensin-aldosterone, causing sodium retention and hypertension (already mapped); sodium dysregulation amplifies the CRH (already mapped) and NF-κB (already mapped) cascade of alcohol use disorder."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "AUD copper: copper, as SOD cofactor, scavenges alcohol-induced ROS in hepatocytes (already mapped) and neurons (already mapped); copper dyshomeostasis amplifies the NF-κB (already mapped) and NLRP3 (already mapped) hepatic neuroinflammatory cascade of alcohol use disorder."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "AUD calcium: calcium regulates neuron (already mapped) excitability and dopamine (already mapped) signalling; calcium dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) hepatocyte (already mapped) liver injury in AUD."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "AUD nitrogen: nitric oxide (NO, nitrogen-derived) in macrophages (already mapped) and hepatocytes (already mapped) modulates liver inflammation; NO excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade in AUD."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "AUD chloride: chloride channels in macrophages (already mapped) and hepatocytes (already mapped) regulate intracellular pH; chloride dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and TGF-β (already mapped) fibrotic cascade in AUD."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "mitochondrial oxygen in hepatocytes (already mapped) and neurons (already mapped) sustains ATP for ethanol metabolism; hypoxia amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TGF-β (already mapped) hepatic neuroinflammatory fibrotic cascade in AUD."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "carbon, via bicarbonate in hepatocytes (already mapped) and macrophages (already mapped), maintains pH homeostasis during ethanol metabolism; carbon dioxide excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TGF-β (already mapped) fibrotic cascade in AUD."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "H2S from sulfur-amino acids in hepatocytes (already mapped) and neurons (already mapped) promotes cytoprotection; sulfur deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TGF-β (already mapped) hepatic fibrotic neuroinflammatory cascade in AUD."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "AUD PD-1: PD-1 on macrophages (already mapped) and t-cytotoxic-cell (already mapped) modulates hepatic immune homeostasis; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic neuroinflammatory cascade in AUD."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "AUD angiotensin-II: angiotensin-II in hepatocytes (already mapped) and fibroblasts (already mapped) promotes TGF-β (already mapped)-driven hepatic fibrosis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) fibrotic inflammatory cascade in AUD."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "AUD VEGF: VEGF from macrophages (already mapped) and hepatocytes (already mapped) promotes hepatic angiogenesis in alcoholic liver disease; VEGF excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and IL-6 (already mapped) fibrotic cascade in AUD."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "AUD WNT/β-catenin: WNT/β-catenin in hepatocytes (already mapped) and hepatic stellate cells modulates liver repair; WNT dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) and IL-6 (already mapped) fibrotic inflammatory cascade of alcohol use disorder."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "AUD RANKL: RANKL signalling in macrophages (already mapped) and hepatocytes (already mapped) modulates liver-immune bone axis; RANKL excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and IL-6 (already mapped) fibrotic cascade of alcohol use disorder."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "AUD SMAD4: SMAD4 in hepatocytes (already mapped) and hepatic stellate cells mediates TGF-β-driven hepatic fibrosis; SMAD4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) fibrotic inflammatory cascade of alcohol use disorder."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "AUD IL-2: IL-2 in hepatic immune cells (already mapped) and gut macrophages (already mapped) modulates alcohol-driven inflammation; IL-2 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "AUD fibronectin: fibronectin in hepatic stellate cells (already mapped) and portal endothelium (already mapped) drives liver matrix deposition; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "AUD Notch: Notch signalling in hepatocytes (already mapped) and hepatic stellate cells modulates liver zonation and injury; Notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "AUD igf-1: IGF-1 from hepatocytes (already mapped) and hepatic stellate cells (already mapped) regulates liver regeneration; IGF-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "AUD activin-a: activin-A from hepatocytes (already mapped) and macrophages (already mapped) regulates liver fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "AUD cgrp: CGRP from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "AUD calcitonin: calcitonin from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic calcium balance; calcitonin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "AUD substance-p: substance-P from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic neuroinflammation; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "AUD insulin-receptor: insulin receptor on hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic metabolic axis; insulin-receptor excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "AUD androgen-receptor: androgen receptor on hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "AUD adrenomedullin: adrenomedullin from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic vascular tone; adrenomedullin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "AUD osteopontin: osteopontin from hepatocytes (already mapped) and macrophages (already mapped) drives hepatic fibrotic remodelling; osteopontin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "AUD fgfr: FGFR on hepatocytes (already mapped) and macrophages (already mapped) regulates hepatic repair; FGFR dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "AUD epinephrine: epinephrine from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic stress tone; epinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "AUD renin: renin from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic fluid balance; renin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD."
---

# Alcohol Use Disorder

## Overview

**Alcohol use disorder (AUD)** is a chronic, relapsing brain disorder defined by loss of control over alcohol consumption despite harmful consequences. It is among the most prevalent and costly psychiatric and medical conditions worldwide, causing neurological, hepatic, cardiovascular, and psychosocial harms.

**Epidemiology:**
- Lifetime prevalence: 14.5% (US adults); 12-month prevalence ~5.3%
- ~95,000 deaths attributable to alcohol per year in the US; global burden ~3 million deaths/year
- Male-to-female ratio: 2:1 (lifetime); gap narrowing in younger cohorts
- Heritability: ~50–60%; strongly polygenic with gene-environment interactions

**DSM-5 Criteria (≥2 of 11 in 12 months):**

| Criterion | Domain |
|:---|:---|
| Drinking more/longer than intended | Loss of control |
| Persistent desire or failed efforts to cut down | Loss of control |
| Much time spent obtaining/recovering | Salience |
| Craving | Motivation |
| Failure to fulfill role obligations | Harmful use |
| Continued despite social/interpersonal problems | Harmful use |
| Giving up activities | Social withdrawal |
| Hazardous use | Risk-taking |
| Continued despite physical/psychological harm | Continued despite harm |
| Tolerance (markedly increased amounts for effect, or diminished effect) | Neuroadaptation |
| Withdrawal (withdrawal syndrome or drinking to relieve/avoid withdrawal) | Neuroadaptation |

**Severity:** Mild (2–3 criteria), Moderate (4–5), Severe (≥6)

**Screening tools:**
- **AUDIT (Alcohol Use Disorders Identification Test):** 10-item validated screen; AUDIT ≥8 = hazardous; ≥15 = likely AUD; best primary care screen
- **CAGE questionnaire:** Cut down? Annoyed? Guilty? Eye-opener? ≥2 positive → AUD screen positive
- **Biomarkers:** GGT, MCV, CDT (carbohydrate-deficient transferrin, most specific), urine EtG/EtS

## Structure

### Neurobiology of alcohol and addiction

**Koob's three-stage addiction cycle** [^koob-2013-addiction-neuroscience] describes AUD progression:

**Stage 1 — Binge/Intoxication (positive reinforcement):**
- Alcohol → VTA dopamine → nucleus accumbens (NAcc) → euphoria, reward
- GABA-A potentiation → disinhibition, anxiolysis, motor impairment
- NMDA inhibition → cognitive impairment, blackouts
- **Key circuits:** VTA → NAcc; BLA → NAcc (stimulus-reward learning)

**Stage 2 — Withdrawal/Negative Affect (negative reinforcement):**
- Chronic alcohol → GABA-A downregulation + NMDA upregulation → withdrawal state when alcohol removed
- **Amygdala CRF hyperactivation:** CRF (corticotropin-releasing factor) release in central amygdala (CeA) drives withdrawal anxiety, irritability, and dysphoria → drinking to relieve distress (negative reinforcement)
- Extended amygdala (CeA + BNST) becomes the dominant driver of drinking at this stage
- Reduced opioid/dopamine reward → anhedonia in abstinence (protracted abstinence syndrome)

**Stage 3 — Preoccupation/Anticipation (craving/relapse):**
- PFC (OFC, dlPFC, ACC) lose inhibitory control over NAcc and amygdala
- OFC hyperactivity → salience attribution to alcohol cues
- dlPFC hypofunction → impaired inhibitory control
- **Key circuits:** PFC → striatum (habit formation); PFC → amygdala (impaired regulation)

### Molecular mechanisms

**GABA-A receptor pharmacology:**
- Alcohol positive allosteric modulator at GABA-A receptors (particularly δ-subunit-containing extrasynaptic receptors and synaptic receptors with γ2 subunit)
- Acute: Cl⁻ flux increases → hyperpolarization → sedation, anxiolysis, ataxia
- Chronic: Receptor subunit composition shifts (α4/δ upregulates, α1/γ2 downregulates) → reduced GABAergic tone → tolerance → need more alcohol for same effect
- **Withdrawal:** Reduced GABA-A function + unmasked NMDA upregulation → neuronal hyperexcitability → seizures, delirium tremens

**NMDA receptor dynamics:**
- Acute: Alcohol inhibits NMDA receptors (preferentially NR2B-containing) → disrupts LTP → memory impairment, blackouts
- Chronic: Compensatory NR2B upregulation + increased expression → sensitized NMDA → withdrawal excitotoxicity
- Wernicke-Korsakoff: Thiamine (B1) deficiency → impairs Krebs cycle → insufficient ATP → glutamate excitotoxicity in mammillary bodies and medial thalamus → memory circuit destruction (Korsakoff syndrome)

**Dopamine reward:**
- Alcohol stimulates VTA dopamine via μ-opioid receptors on VTA GABAergic interneurons → disinhibition → increased DA firing → NAcc DA release
- DRD2 Taq1A polymorphism (A1 allele) → 30–40% fewer D2 receptors in striatum → reduced reward sensitivity → higher consumption to achieve reward
- Naltrexone mechanism: μ-opioid receptor blockade → prevents alcohol-induced VTA disinhibition → reduces NAcc DA surge → blunts "high"

**Endocannabinoid modulation:**
- CB1 receptors in NAcc, VTA, and amygdala modulate alcohol reward and anxiety
- Alcohol triggers endocannabinoid release (2-AG, AEA) → retrograde CB1 activation → facilitates dopamine and GABA signaling during intoxication
- CB1 antagonist rimonabant reduced drinking in trials but withdrawn for depression/suicidality

### Genetics

| Gene | Variant | Effect |
|:---|:---|:---|
| **ALDH2** | *2 (Asian populations) | Impaired acetaldehyde metabolism → flushing → strongly protective |
| **ADH1B** | *3 (rs1229984) | Rapid ethanol → acetaldehyde → reduced palatability; protective |
| **GABRA2** | Multiple SNPs | GABA-A α2 subunit; strongest GWAS hit for AUD |
| **DRD2** | Taq1A (A1 allele) | Reduced D2 density → reward deficit; AUD risk |
| **OPRM1** | A118G (Asn40Asp) | Increased opioid system activation by alcohol; predicts naltrexone response |

## Function

### Alcohol metabolism and toxicity

**Ethanol catabolism:**
1. **Ethanol → Acetaldehyde:** Alcohol dehydrogenase (ADH; liver cytosol); CYP2E1 (high alcohol load/chronic use; generates reactive oxygen species)
2. **Acetaldehyde → Acetate:** Aldehyde dehydrogenase (ALDH; mainly ALDH2 in liver mitochondria)
3. **Acetate → CO₂ + H₂O:** Peripheral tissues

**ALDH2 inhibition (disulfiram mechanism):** Blocks step 2 → acetaldehyde accumulation → flushing, nausea, palpitations, vomiting → aversive conditioning

**Hepatotoxicity cascade:**
- Acetaldehyde protein adducts → hepatocyte damage
- CYP2E1 → reactive oxygen species → oxidative stress → fatty liver → alcoholic hepatitis → cirrhosis
- LPS from gut microbiome (alcohol disrupts gut barrier) → TLR4 → Kupffer cell activation → TNF-α → hepatic inflammation

### Neurological complications

| Complication | Mechanism | Onset |
|:---|:---|:---|
| **Alcohol withdrawal seizures** | GABA-A ↓ + NMDA ↑ excitotoxicity | 6–48h after last drink |
| **Delirium tremens (DTs)** | Severe autonomic instability; 5% mortality untreated | 24–72h; peak 48h |
| **Wernicke's encephalopathy** | Thiamine deficiency → pyruvate → glutamate excitotoxicity | Acute; classic triad: confusion, ataxia, ophthalmoplegia |
| **Korsakoff syndrome** | Mammillary body + mediodorsal thalamus lesions → anterograde amnesia | Chronic; follows Wernicke's |
| **Alcoholic neuropathy** | Thiamine deficiency + direct ethanol toxicity | Insidious; distal symmetric sensorimotor |
| **Alcoholic cerebellar degeneration** | Anterior-superior vermis vulnerability; thiamine + ethanol | Progressive gait ataxia |

## Pathology

### CIWA-Ar: Alcohol Withdrawal Assessment

The **Clinical Institute Withdrawal Assessment for Alcohol — Revised (CIWA-Ar)** is the standard bedside tool (10 items: nausea, tremor, diaphoresis, anxiety, agitation, perceptual disturbances, tactile/auditory/visual disturbances, headache, orientation):
- Score 0–9: Mild; outpatient monitoring possible
- Score 10–19: Moderate; consider BZD titration
- Score ≥20: Severe; hospitalization; high DT risk

### Fetal Alcohol Spectrum Disorder (FASD)

Prenatal alcohol exposure → leading preventable cause of intellectual disability:
- **Fetal Alcohol Syndrome (FAS):** Facial dysmorphology (smooth philtrum, thin vermilion, small palpebral fissures) + growth restriction + CNS dysfunction
- Mechanism: Alcohol inhibits neuronal migration, increases apoptosis (NMDA block in neural progenitors), disrupts BDNF signaling
- No safe amount of alcohol in pregnancy established

### Treatment

**Medical Detoxification:**

| Agent | Mechanism | Notes |
|:---|:---|:---|
| **Diazepam (long-acting)** | GABA-A agonist | Standard for DT prevention; long half-life provides smooth taper |
| **Lorazepam** | GABA-A agonist | Preferred in liver disease (glucuronidation not impaired); short-acting |
| **Chlordiazepoxide** | GABA-A agonist | Long-acting; classic inpatient protocol |
| **Carbamazepine** | Na+ channel blocker | Alternative in mild-moderate withdrawal; reduces kindling; no dependency |
| **Thiamine (B1)** | Cofactor restoration | 100–500mg IV/IM BEFORE glucose in any AUD patient |
| **Gabapentin** | Calcium channel α2δ | Reduces withdrawal anxiety; useful outpatient detox adjunct |

**Relapse Prevention:**

| Medication | Mechanism | NNT | Notes |
|:---|:---|:---|:---|
| **Naltrexone** | μ-opioid antagonist | ~8–12 | Reduces craving and alcohol reward; daily or extended-release monthly injection (Vivitrol); COMBINE trial [^anton-2006-combine] support |
| **Acamprosate** | NMDA modulator + GABA-A agonist | ~12 | Normalizes glutamate/GABA balance in protracted withdrawal; best for abstinence maintenance; not in active heavy drinking |
| **Disulfiram** | ALDH inhibitor | Varies | Supervised use most effective; contraindicated with any hidden alcohol exposure; severe cardiovascular reaction possible |
| **Nalmefene** | Opioid antagonist + κ partial agonist | — | As-needed dosing before anticipated drinking; approved EU; reduces heavy drinking days |
| **Baclofen** | GABA-B agonist | — | Reduces craving and anxiety-driven drinking; approved France; extensive off-label evidence; FDA IND ongoing |
| **Gabapentin** | α2δ calcium channel | — | Reduces protracted abstinence anxiety/insomnia; widely used off-label |
| **Ondansetron** | 5-HT3 antagonist | — | Modest efficacy in early-onset AUD (onset ≤25 years); reduces genotype-specific craving |

**Psychosocial treatments:**
- **Alcoholics Anonymous (AA) / 12-step facilitation:** Peer support; spiritual framework; sustained abstinence rates correlate with meeting attendance; free and widely accessible
- **SMART Recovery:** Science-based alternative to 12-step; CBT-based; accepts harm reduction goals
- **Motivational Enhancement Therapy (MET):** Brief 4-session motivational interviewing-based; COMBINE trial component; enhances intrinsic motivation to change
- **CBT for relapse prevention:** Identifies and addresses triggers, cognitive distortions, and high-risk situations; drink refusal skills; coping with craving

**Harm reduction approaches:**
- **Controlled drinking:** Viable goal in mild-moderate AUD; reduces harm even without abstinence
- **Managed alcohol programs:** Supervised drinking in severe AUD homeless populations; reduces crisis interventions, hospitalizations, and criminalization
- **Naltrexone "as-needed":** Target-controlled dosing before drinking occasions to reduce binge episodes

## Connections

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — alcohol potentiates GABA-A → sedation and tolerance; chronic use → GABA-A downregulation; abrupt cessation → GABA-A insufficiency → withdrawal seizures (6–48h) and delirium tremens (24–72h); GABRA2 (α2 subunit) polymorphisms are the strongest GWAS association with AUD.

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — alcohol inhibits NMDA receptors (NR2B) → blackouts; chronic use → compensatory NMDA upregulation; abrupt withdrawal → glutamate excitotoxicity → seizures and Wernicke-Korsakoff syndrome; acamprosate normalizes NMDA/GABA balance in protracted abstinence to prevent relapse.

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — alcohol stimulates VTA dopamine release → NAcc → euphoria and positive reinforcement; DRD2 Taq1A A1 allele → reduced D2 receptor density → compensatory drinking; naltrexone blocks opioid-mediated VTA DA release → reduces alcohol reward and craving.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — reduced serotonin function in AUD → disinhibition and impulsivity; 5-HT3 receptors in NAcc amplify dopamine reward; ondansetron (5-HT3 antagonist) has modest efficacy in early-onset AUD (≤25 years); SSRIs are ineffective in AUD without comorbid depression.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — chronic alcohol reduces BDNF in NAcc and dorsomedial striatum → impairs BDNF-mediated braking on compulsive drinking; BDNF infusion into NAcc reduces ethanol preference in rodent models; abstinence partially restores BDNF; Val66Met BDNF SNP associated with AUD vulnerability.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — AUD weakens PFC-NAcc inhibitory control circuits; amygdala CRF hyperactivation drives negative reinforcement drinking; hippocampal neurogenesis is suppressed by chronic alcohol; partial brain volume recovery occurs after ≥6 months of sustained abstinence.

- `connects-to` → **[CRH](../../../03-molecular/crh/README.md)** — CRH in central amygdala/BNST mediates the negative reinforcement model of AUD: withdrawal stress → CeA CRH excess → anxiety and dysphoria → drinking to relieve distress; CRHR1 antagonists reduce stress-induced alcohol seeking in animal models.

- `connects-to` → **[Mu-Opioid Receptor](../../../03-molecular/mu-opioid-receptor/README.md)** — alcohol stimulates β-endorphin → MOR on VTA GABAergic interneurons → disinhibition → dopamine surge; naltrexone (MOR/KOR antagonist) blocks this reward mechanism; OPRM1 A118G (Asn40Asp) SNP predicts superior naltrexone response in AUD.

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — alcohol withdrawal → NE hyperactivation → autonomic instability (tachycardia, hypertension, diaphoresis) — core CIWA-Ar symptoms; clonidine (α2 agonist) reduces LC-NE firing during withdrawal; chronic alcohol disrupts NE autoreceptor sensitivity.

- `connects-to` → **[NPY](../../../03-molecular/npy/README.md)** — NPY reduces voluntary alcohol intake via limbic anxiolysis; Y2R knockout mice consume 2× more alcohol; alcohol withdrawal depletes limbic NPY → anxiety → relapse; Y1R agonism in CeA reduces stress-induced alcohol-seeking; NPY is a candidate pharmacotherapy for AUD relapse prevention.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver bears the brunt of alcohol use disorder: ethanol metabolism to acetaldehyde and a shifted NADH/NAD ratio drive steatosis → alcoholic hepatitis → fibrosis and cirrhosis; abstinence reverses early disease, but cirrhosis is the gateway to liver failure and cancer.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — Alcohol use disorder is a major cause of hepatocellular carcinoma: alcoholic cirrhosis is the inflamed, regenerating background on which HCC arises, and alcohol multiplies the risk from hepatitis B/C—so HCC surveillance is essential once cirrhosis develops.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Alcohol and opioid use disorders frequently co-occur and are dangerous together: both are CNS depressants, so combined use multiplies respiratory depression and overdose death; they share reward and stress circuitry, and concurrent alcohol complicates opioid agonist therapy.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Alcohol and stimulant use disorders frequently co-occur and interact dangerously: alcohol is used to come down from stimulants, cocaine plus alcohol forms toxic cocaethylene, and both engage overlapping dopamine reward circuitry—so polysubstance use worsens outcomes.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Alcohol use disorder and depression are intertwined and bidirectional: people drink to relieve low mood, but alcohol is a depressant that deepens depression and suicide risk, and both share serotonergic and stress-axis dysregulation—so both need treating together.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Hepatocytes bear the metabolic brunt of alcohol: they oxidize ethanol via alcohol dehydrogenase and CYP2E1, generating acetaldehyde and ROS that cause fatty change, ballooning, and death—so steatosis, hepatitis, and cirrhosis trace to hepatocyte injury.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Alcohol is a direct cause of esophageal cancer: its metabolite acetaldehyde is a carcinogen that damages esophageal DNA, so heavy drinking—especially with smoking—markedly raises squamous-cell esophageal cancer risk, one of several alcohol-attributable cancers.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Alcohol is directly toxic to cardiomyocytes: chronic heavy drinking causes alcoholic cardiomyopathy, where ethanol and acetaldehyde impair contractile proteins and mitochondria, dilating the heart and causing heart failure that can partly reverse with abstinence.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Alcohol use disorder dysregulates cortisol: heavy drinking activates the HPA axis, producing a pseudo-Cushing's state with high cortisol, and withdrawal spikes it further—contributing to the anxiety, sleep disruption and relapse that mark early abstinence.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Alcohol remodels neurons toward dependence: it potentiates inhibitory GABA and blocks excitatory NMDA receptors acutely, so neurons adapt by upregulating excitation—unmasked as the tremor, seizures and delirium of withdrawal when drinking stops.
- `connects-to` → **[NASH](../nash/README.md)** — Alcohol and NASH cause overlapping fatty-liver disease: heavy drinking and metabolic syndrome both deposit fat that inflames and scars the liver, and the two are often combined—so distinguishing alcohol- from metabolism-driven steatohepatitis guides treatment.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Alcohol use disorder damages the gut-liver axis: alcohol disrupts the gut microbiome and leaks bacterial endotoxin through an inflamed barrier, and this endotoxemia drives the liver inflammation that turns heavy drinking into hepatitis and cirrhosis.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Alcohol is a leading cause of pancreatitis: it triggers premature enzyme activation that digests the pancreas, causing acute attacks and, with chronic use, permanent damage with diabetes and malabsorption—so the pancreas is among alcohol's prime organ targets.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Alcohol crosses the placenta freely: with no safe level in pregnancy, it disrupts fetal brain development, causing fetal alcohol spectrum disorders with lifelong cognitive and facial features—so alcohol use disorder in pregnancy carries permanent fetal harm.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Alcohol is an under-recognized breast cancer cause: even moderate drinking raises risk by increasing estrogen and generating DNA-damaging acetaldehyde, so alcohol is now counted among the modifiable risk factors for hormone-driven breast cancer.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Heavy drinking and thiamine loss devastate the hippocampus: Wernicke-Korsakoff syndrome and alcohol-related brain damage impair this memory hub, causing the dense amnesia and confabulation of Korsakoff's—why thiamine is given urgently in alcohol withdrawal.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Alcohol is a proven cause of colorectal cancer: its metabolite acetaldehyde damages DNA and it depletes folate, so even moderate drinking raises colorectal risk—one of several cancers (with breast and liver) alcohol drives.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Alcohol leaves a fingerprint in red cells: it is directly toxic to marrow and, with folate/B12 deficiency, enlarges red cells, so macrocytosis (high MCV) is a classic clue to chronic heavy drinking.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Heavy drinking drains the body of magnesium: alcohol makes the kidneys waste it and poor intake compounds the loss, so the resulting hypomagnesemia worsens withdrawal tremor and seizures and destabilizes the heart's rhythm.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Alcohol dependence reshapes synapses: chronic drinking shifts the balance of excitatory and inhibitory synaptic signaling, so the brain adapts to the drug—and the rebound when it is removed produces the dangerous withdrawal syndrome.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Alcohol injures the stomach directly: it inflames and erodes the gastric lining, causing gastritis and bleeding ulcers, and the vomiting of heavy use can tear the junction with the esophagus—common reasons drinkers bleed.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Heavy drinking can acidify the blood: starved and metabolizing alcohol, the body makes ketones and lactate, so alcoholic ketoacidosis drops blood pH—a dangerous acidosis that can appear even with near-normal sugar.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Alcohol weakens and destabilizes the heart: years of drinking dilate and weaken the muscle into alcoholic cardiomyopathy, while even a binge can trigger atrial fibrillation—the so-called holiday heart.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Alcohol drops the platelet count: it suppresses their production in the marrow and shortens their life, so heavy drinkers bruise and bleed easily, a count that often rebounds within days of stopping.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging reveals alcohol's toll: brain MRI shows the shrinkage and the mammillary-body changes of Wernicke's, and fMRI photons map the reward-circuit response that drives craving.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Alcohol poisons the peripheral nerves: direct toxicity and thiamine deficiency cause a painful, numbing length-dependent neuropathy, one of its most common neurological harms.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Chronic drinking depletes zinc: poor intake and gut losses lower it, contributing to the skin problems, poor wound healing and weakened immunity seen in alcohol use disorder.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows alcohol's mark on the liver cell: fat droplets swell the hepatocyte, the cytoskeleton tangles into Mallory-Denk bodies, and giant megamitochondria appear, the ultrastructure of alcoholic liver injury.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The failing liver writes on the skin: spider angiomata, palmar erythema, jaundice, and the dilated caput medusae veins are visible stigmata that betray the chronic liver damage of heavy drinking.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Drinkers run dangerously low on phosphorus: poor intake and the shifts of refeeding can crash blood phosphate, sapping the energy molecule ATP and causing the muscle weakness and rhabdomyolysis seen in alcohol use disorder.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Alcohol is directly toxic to the marrow: it enlarges red cells into macrocytosis, drops platelets, and suppresses all the blood lines, on top of the folate deficiency that compounds the anemia in heavy drinkers.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Alcohol unbalances the sex hormones: chronic use causes testicular atrophy, low testosterone, and gynecomastia in men and menstrual disruption in women — and in pregnancy it crosses the placenta to cause fetal alcohol spectrum disorder.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Drinking disarms the body's defenders: alcohol impairs neutrophil function and numbers, which is why heavy drinkers are prone to pneumonia, tuberculosis, and severe infection.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Alcohol wrecks the body's clock: it suppresses melatonin and fragments sleep, so the sedation of a nightcap gives way to rebound insomnia and vivid dreams — and withdrawal brings severe sleeplessness that drives relapse.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Drinking quietly thins the bones: alcohol directly suppresses osteoblasts and disturbs calcium and vitamin D, so chronic use causes osteoporosis and, with the falls it provokes, a high fracture risk.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Heavy drinking injures the vessel lining: alcohol harms endothelial cells and raises blood pressure, contributing to the cardiomyopathy, arrhythmia, and stroke risk that offset any benefit of light consumption.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Alcohol unmans the hormones: it suppresses testosterone production and speeds its conversion to estrogen, causing the low libido, shrunken testes, and feminization seen in chronic male drinkers.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The liver's macrophages drive alcoholic hepatitis: gut-derived endotoxin activates Kupffer cells to pour out TNF and other cytokines, the inflammatory engine that turns fatty liver into hepatitis and fibrosis.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Alcohol is a leading reversible cause of high blood pressure: intake raises it dose-dependently through sympathetic and hormonal effects, so cutting back is a frontline step that often lowers blood pressure measurably.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Alcohol inflames the brain's immune cells: ethanol and gut-derived endotoxin activate microglial TLR4, and the cytokines they release drive the neuroinflammation behind alcohol-related cognitive decline and craving.
- `connects-to` → **[Stroke](../stroke/README.md)** — Heavy drinking tips the brain toward bleeding: alcohol raises blood pressure and impairs clotting, sharply increasing hemorrhagic stroke risk, while binge drinking can trigger ischemic stroke through arrhythmia and surges in pressure.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Alcohol use disorder shadows bipolar disorder: it is among the commonest comorbidities, used to self-medicate mood swings yet worsening the course, raising suicide risk, and complicating diagnosis and treatment of both.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Alcohol throws the inflammation switch in liver and brain: ethanol and gut-derived endotoxin activate NF-κB in Kupffer cells and microglia, driving the alcoholic hepatitis and neuroinflammation behind much of the organ damage.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It corrodes the nervous system on many fronts: beyond intoxication, alcohol drives withdrawal seizures, thiamine-deficient Wernicke-Korsakoff encephalopathy, cerebellar degeneration and peripheral neuropathy.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Heavy drinking cripples the body's defenses: alcohol impairs neutrophil and macrophage function and, with aspiration and cirrhosis, leaves patients prone to pneumonia, spontaneous bacterial peritonitis and sepsis.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Repeated pancreatitis paves the way to cancer: heavy alcohol use is a leading cause of chronic pancreatitis, and the resulting long-standing inflammation raises the risk of pancreatic adenocarcinoma.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Chronic drinking can dilate the heart: sustained heavy alcohol use causes an alcoholic cardiomyopathy, a dilated, weakened heart that is a recognized and partly reversible cause of heart failure.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — It harms the kidney directly and through the liver: heavy alcohol drives hypertension and, in cirrhosis, hepatorenal physiology, while binge drinking can cause rhabdomyolysis — together threatening chronic kidney disease.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Heavy drinking poisons the peripheral nerves: chronic alcohol use, with its thiamine and B-vitamin deficiency, causes a length-dependent axonal neuropathy producing burning pain and numbness in the feet.
- `connects-to` → **[Head and Neck Squamous Cell Carcinoma](../hnscc/README.md)** — Alcohol is a major head-and-neck carcinogen: ethanol and its metabolite acetaldehyde damage the mucosa of the mouth, throat and larynx, and combined with tobacco multiply the risk of head and neck squamous-cell cancer.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety and drinking feed each other: people drink to quell anxiety, but tolerance and withdrawal raise baseline anxiety, locking the two into a self-reinforcing cycle.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It ravages the gut from end to end: alcohol causes gastritis and Mallory-Weiss tears, acute and chronic pancreatitis, and the alcoholic hepatitis and cirrhosis with varices that define end-stage liver disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It disrupts the hormones and fuel control: chronic alcohol causes hypogonadism, a pseudo-Cushing's state and dangerous hypoglycaemia, and pancreatitis can destroy the islets into diabetes.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It disarms host defence: alcohol impairs neutrophil and lymphocyte function and ciliary clearance, leaving people with alcohol use disorder prone to pneumonia, tuberculosis and severe infection.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It disturbs the heart's rhythm and muscle: binge drinking triggers 'holiday heart' atrial fibrillation, and chronic use causes a dilated alcoholic cardiomyopathy alongside the hypertension it drives.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It wastes muscle and kills bone: acute and chronic alcoholic myopathy weaken proximal muscles, and alcohol is a leading cause of avascular necrosis of the femoral head.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Liver damage shows on the skin: spider naevi, palmar erythema and telangiectasia of alcohol-related liver disease appear on the skin, and alcohol can trigger porphyria cutanea tarda and psoriasis.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It opens the lungs to infection: alcohol impairs cough and airway defences, raising the risk of aspiration pneumonia, community-acquired pneumonia and tuberculosis, and predisposing to ARDS.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It unbalances fluids and salts: heavy drinking causes profound hypomagnesaemia and hypophosphataemia, and rhabdomyolysis or hepatorenal syndrome can precipitate acute kidney injury.
- `connects-to` → **[Dietary Magnesium](../../../03-medicine/03-food/magnesium-dietary/README.md)** — Drinking drains magnesium: chronic alcohol use depletes body magnesium, contributing to the tremor, arrhythmia and seizures of withdrawal, so replacement is routine.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Drinking raises the risk: heavy alcohol use roughly triples the risk of active tuberculosis through impaired immunity, malnutrition and social exposure, a major driver of the global TB burden.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Trauma and drinking entwine: alcohol use disorder and PTSD frequently co-occur, as people drink to numb intrusive memories and hyperarousal, each disorder worsening the other.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Alcohol starves the bone-builders: chronic alcohol suppresses osteoblast activity and bone formation, a key mechanism behind the osteoporosis and fracture risk of alcohol use disorder.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It scars the liver lobule: chronic alcohol drives steatosis, alcoholic hepatitis and pericentral fibrosis in the hepatic lobule, progressing to cirrhosis — the classic and often fatal organ damage of alcohol use disorder.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It weakens the heart muscle: sustained heavy drinking causes a dilated alcoholic cardiomyopathy and, acutely, atrial fibrillation ('holiday heart'), adding cardiac failure to the harms of alcohol use disorder.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Alcohol is a carcinogen: it causes cancers of the mouth, throat, oesophagus, liver, colon and breast — malignancies treated with chemotherapy — making alcohol use disorder a major and preventable cancer risk.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — 'Holiday heart': binge and chronic drinking trigger atrial fibrillation and other arrhythmias through the conduction system, on top of alcoholic cardiomyopathy.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Withdrawal seizures: abrupt cessation in alcohol dependence unmasks GABA-rebound hyperexcitability, causing withdrawal seizures and status epilepticus—a medical emergency.
- `connects-to` → **[Gout](../gout/README.md)** — Alcohol and urate: beer and spirits raise serum uric acid and precipitate gout attacks, a classic dietary trigger of the disease in heavy drinkers.
- `connects-to` → **[Hereditary Pancreatitis](../hereditary-pancreatitis/README.md)** — Alcohol and the pancreas: alcohol is the leading cause of chronic pancreatitis and dramatically accelerates disease in those with hereditary pancreatitis (PRSS1), compounding genetic and toxic injury.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Alcohol and dementia: heavy chronic drinking causes alcohol-related brain damage and raises later dementia risk including Alzheimer's, through thiamine deficiency, direct neurotoxicity and vascular injury.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Anaemia of drinking: alcohol causes anaemia through gastrointestinal and variceal bleeding, marrow suppression and folate deficiency—often a mix of iron-deficiency and macrocytic anaemia.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Alcoholic lung: chronic drinking impairs alveolar defence and depressed consciousness drives aspiration, raising the risk of aspiration pneumonia, lung abscess and acute respiratory distress syndrome.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Pneumococcal susceptibility: alcohol blunts neutrophil and macrophage function, making heavy drinkers prone to severe, bacteraemic pneumococcal pneumonia and invasive disease.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Impaired healing: alcohol disrupts collagen deposition, immune defence and angiogenesis, slowing wound healing and raising surgical-site infection and post-operative complication rates.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Alcoholic inflammation: gut-derived endotoxin in alcohol use disorder drives Kupffer-cell TNF-α release, a central mediator of alcoholic hepatitis and the neuroinflammation of dependence.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Hepatic and brain inflammation: IL-6 rises with chronic alcohol intake, contributing to liver injury, the acute-phase response and the neuroinflammation linked to alcohol-related cognitive decline.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: alcohol and its metabolites activate the NLRP3 inflammasome in liver and brain, releasing IL-1β to drive alcoholic liver disease and neuroinflammation.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Gut-brain endotoxin axis: alcohol increases gut permeability, letting bacterial LPS engage TLR4 on Kupffer cells and microglia, a central trigger of alcoholic liver injury and neuroinflammation.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — Reward and craving: the endocannabinoid system modulates alcohol's rewarding effects and craving through CB1 signalling in the mesolimbic circuit, an emerging therapeutic target in alcohol use disorder.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Acute intoxication and tolerance: alcohol raises extracellular adenosine, contributing to its sedative and motor-incoordinating effects, while adaptation in adenosine signalling features in tolerance and withdrawal.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Hypothalamic orexin drives the cue- and stress-induced craving and the hyperarousal of alcohol withdrawal, making orexin-receptor antagonists a candidate strategy to reduce relapse in alcohol use disorder.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Ghrelin enhances the rewarding value of alcohol and promotes alcohol seeking, a gut-brain hunger signal repurposed in addiction whose pharmacological blockade reduces drinking in early trials.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Nicotinic acetylcholine receptors modulate alcohol's dopaminergic reward, the mechanistic basis for the nicotinic partial agonist varenicline reducing alcohol consumption and the frequent co-occurrence of alcohol and tobacco use.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — GLP-1 receptor agonists like semaglutide reduce alcohol craving and consumption by acting on the mesolimbic reward circuit, an emerging metabolic-pathway therapy generating strong interest for alcohol use disorder.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Chronic alcohol activates hepatic stellate cells through TGF-β to deposit collagen, driving the progression from steatosis to the alcoholic cirrhosis that is a leading cause of death in alcohol use disorder.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Oxytocin dampens stress and craving and can ease alcohol-withdrawal severity in studies, an endogenous social-bonding system being explored as an adjunct to reduce relapse in alcohol use disorder.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Alcohol engages dopamine-driven ERK signaling in the striatal reward circuitry, the synaptic plasticity that consolidates alcohol reward and craving.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — The cortisol/CRH stress response of alcohol withdrawal (already mapped) acts through the glucocorticoid receptor, the HPA dysregulation that drives negative-affect relapse in alcohol use disorder.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Alcohol metabolism generates reactive oxygen species and acetaldehyde, and the NRF2 antioxidant response defends against the oxidative damage underlying alcoholic liver disease and neurotoxicity.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Alcohol-driven gut-barrier disruption releases microbial products that engage TLR4-MyD88-NF-κB signaling (TLR4 and NF-κB already mapped), driving the systemic and neuroinflammation that sustain alcohol use disorder.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-dependent synaptic plasticity in the mesolimbic reward circuit consolidates the maladaptive learning and cue associations that entrench compulsive alcohol use.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor (NTRK) mediates the reward-circuit synaptic adaptations underlying alcohol craving and relapse vulnerability.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-mTOR signaling (mTOR mapped) participates in the reward-circuit synaptic plasticity and neuroadaptations of alcohol use disorder.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Alcohol-induced microglial and Kupffer-cell activation induces galectin-3, amplifying the neuroinflammation and hepatic injury of alcohol use disorder.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine-driven JAK-STAT signaling (IL-6 mapped) transduces the systemic and neuroinflammation accompanying chronic alcohol exposure.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling in reward and stress circuits shapes the synaptic plasticity underlying dependence and relapse in alcohol use disorder.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling (JAK1/2 already mapped) transduces the systemic and neuroinflammatory tone driven by chronic alcohol exposure, including alcoholic liver disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic and gut-derived microbial DNA engages cGAS-STING, contributing to the TLR4-associated hepatic and neuroinflammation of alcohol use disorder.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates the neuronal and hepatic oxidative-stress handling relevant to the neuroadaptations and organ injury of alcohol use disorder.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 neuroinflammatory signaling contributes to the inflammatory tone of chronic alcohol use disorder.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the gut-derived-endotoxemia-driven myeloid inflammation linked to alcohol use disorder and alcoholic liver disease.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and oxidative-stress adaptation participates in the alcohol-associated liver and neural stress of alcohol use disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) mediates the synaptic-plasticity neuroadaptations of the reward circuit in alcohol use disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation in the reward circuit contributes to the persistent neuroadaptations and relapse vulnerability of alcohol use disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the hepatic and neuronal metabolic adaptation of alcohol use disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal and hepatic responses to the chronic ethanol exposure of alcohol use disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with alcohol use disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the NMDA-receptor and synaptic-plasticity mechanisms of the reward circuitry implicated in alcohol use disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and reward-circuit processes implicated in alcohol use disorder.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven neuroinflammation (glial activation) participates in the reward-circuit changes and neurotoxicity of alcohol use disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory responses implicated in alcohol use disorder.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with alcohol use disorder.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the microglial and neuroinflammatory processes implicated in alcohol use disorder.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences: women develop alcohol-related organ damage at lower exposures (telescoping), and estrogen with sex-based differences in alcohol metabolism contributes to this greater vulnerability in alcohol use disorder.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative metabolism: ethanol metabolism and xanthine-oxidase activity generate reactive oxygen species and uric acid, contributing to the oxidative liver injury and the hyperuricaemia and gout associated with heavy drinking.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Alcoholic cardiomyopathy: chronic heavy drinking causes a dilated cardiomyopathy, and troponin release can mark the myocardial injury of this under-recognised cardiac complication of alcohol use disorder.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Alcohol-related anaemia: heavy drinking lowers haemoglobin through a direct marrow toxicity, folate deficiency causing macrocytosis, and gastrointestinal and variceal bleeding from the associated liver disease (already mapped).
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Pseudo-Cushing and hypertension: alcohol activates the HPA and renin-angiotensin-aldosterone systems (cortisol already mapped), contributing to the hypertension and the pseudo-Cushing state seen in alcohol use disorder.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Glucose dysregulation: alcohol acutely inhibits gluconeogenesis to cause hypoglycaemia, while chronic pancreatic damage (pancreas already mapped) impairs insulin secretion, giving alcohol use disorder complex effects on glucose control.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Lipid effects: alcohol raises HDL yet also drives hypertriglyceridaemia and, in heavy use, an atherogenic dyslipidaemia (insulin already mapped), giving alcohol complex, dose-dependent effects on cholesterol and cardiovascular risk.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Electrolyte depletion: the poor intake, vomiting and renal losses of alcohol use disorder deplete potassium, and with the magnesium deficiency (already mapped) this predisposes to the arrhythmias and weakness of the malnourished drinker.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the glial neuroinflammation (TLR4 and microglia already mapped) and the alcoholic hepatitis contribute to the neuro- and hepato-inflammation of alcohol use disorder.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 anti-inflammatory arm: IL-4 polarises the microglia (already mapped) and the hepatic Kupffer cells toward an M2 phenotype, countering the TLR4-driven (already mapped) neuro- and hepato-inflammation of alcohol use disorder.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Alcohol and iron: alcohol suppresses hepcidin, promoting the intestinal iron hyperabsorption and hepatic iron loading that aggravate the oxidative (xanthine oxidase already mapped) liver injury of alcohol use disorder.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Hepatic iron overload: the hepcidin suppression (already mapped) and the direct effects of alcohol load the liver with iron (haemoglobin already mapped), the iron-catalysed oxidative stress worsening the alcoholic liver disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Profibrotic type-2 arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) and profibrotic (TGF-β already mapped) response of the alcoholic liver fibrosis in alcohol use disorder.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Hepatic stellate cells: the fibroblast-like hepatic stellate cells, activated (TGF-β and IL-13 already mapped) by the alcoholic liver injury, lay down the collagen (already mapped) fibrosis that progresses to cirrhosis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine and metabolism: alcohol alters the adipokine leptin of the appetite and craving and the metabolic (insulin already mapped) dysregulation, part of the systemic and hepatic metabolic disturbance of alcohol use disorder.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Hepatoprotective adipokine: adiponectin, with leptin (already mapped), is the hepatoprotective adipokine whose fall in the alcoholic liver disease promotes the steatosis and the fibrosis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the alcoholic steatohepatitis and the metabolic disturbance of alcohol use disorder.
- `connects-to` → **[Cannabis use disorder](../cannabis-use-disorder/README.md)** — Polysubstance comorbidity: alcohol and cannabis use disorders commonly co-occur (with the opioid use disorder already mapped), the shared reward-circuit (dopamine already mapped) addiction vulnerability.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the gut-derived (TLR4 already mapped) stress, drives the inflammation of the alcoholic liver (already mapped) of alcohol use disorder.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 inflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune-mediated inflammation (IL-6 and TNF already mapped) of the alcoholic steatohepatitis of alcohol use disorder.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of alcohol use disorder.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the alcoholic liver disease of alcohol use disorder.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the gut-derived (TLR4 already mapped) inflammation of the alcoholic steatohepatitis of alcohol use disorder.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of alcohol use disorder.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the blood-brain-barrier disruption implicated in alcohol use disorder.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic arm: the cytotoxic T cells (perforin pathway) contribute both to the psychoneuroimmunology of the chronic alcohol exposure and to the hepatocyte (already mapped) injury of the alcoholic liver disease of alcohol use disorder.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astroglial neurotoxicity: the astrocytes of the brain (already mapped) are damaged by the chronic alcohol and, with the microglia (already mapped), mediate the neuroinflammation and the neurodegeneration of alcohol use disorder.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the Kupffer-cell (macrophage already mapped) activation of the alcoholic liver disease of alcohol use disorder.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the hepatic and neuroinflammatory myeloid activation of alcohol use disorder.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Alcoholic iron overload: transferrin (and its carbohydrate-deficient form, a biomarker of chronic use), the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the hepatic iron overload of alcohol use disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-gut axis: TSLP, from gut epithelium (already mapped) under the dysbiosis and the alcohol-induced barrier disruption, primes mast cells (already mapped) and dendritic cells (already mapped) and amplifies the hepatic neuroinflammation of alcohol use disorder.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-hepatic axis: bradykinin, via B1/B2 receptors on Kupffer cells (macrophage already mapped) and hepatic stellate cells, amplifies the portal inflammation and the fibrogenic activation of the alcoholic liver disease of alcohol use disorder.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Contact/complement brake: the C1-esterase inhibitor regulates the classical complement (C3, C5 already mapped) and contact pathways whose activation contributes to the hepatic and neuroinflammatory injury of alcohol use disorder.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell hepatic effector: mast cells (already mapped) in the alcoholic liver stroma release histamine that amplifies the Kupffer-cell (macrophage already mapped) activation and the portal inflammatory milieu of the alcoholic liver disease of alcohol use disorder.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Alcohol-anaemia erythropoiesis: erythropoietin drives red-cell recovery from the multifactorial anaemia of alcohol use disorder; alcohol suppresses EPO production and the bone-marrow (already mapped) response, worsening the nutritional and hepatic anaemia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H limits the alternative-pathway activation (C3, C5 and C5aR1 already mapped) in the hepatic (liver already mapped) and CNS compartments, moderating the complement-driven Kupffer-cell (already mapped) activation of alcoholic liver disease.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — AUD prolactin: prolactin, via PRLR on neurons (already mapped) and microglia (already mapped), modulates HPA-axis (CRH already mapped) tone; hyperprolactinaemia amplifies the cortisol (already mapped) and dopamine (already mapped) craving cascade of alcohol use disorder.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — AUD vasopressin: vasopressin, via V1aR on neurons (already mapped) and astrocytes (already mapped), modulates HPA-axis stress; vasopressin excess amplifies the CRH (already mapped) and cortisol (already mapped) withdrawal cascade of alcohol use disorder.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — AUD selenium: selenium, as GPx in hepatocytes (already mapped) and neurons (already mapped), scavenges alcohol-induced ROS; selenium deficiency amplifies the NF-κB (already mapped) and NLRP3 (already mapped) hepatic neuroinflammatory cascade of alcohol use disorder.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-hepatic axis: iodine-dependent thyroid hormones modulate hepatic alcohol metabolism and neuronal GABA (already mapped) tone; iodine deficiency impairs thyroid regulation of the CRH (already mapped) and dopamine (already mapped) craving cascade of alcohol use disorder.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — RAAS-sodium dysregulation: heavy alcohol use activates renin-angiotensin-aldosterone, causing sodium retention and hypertension (already mapped); sodium dysregulation amplifies the CRH (already mapped) and NF-κB (already mapped) cascade of alcohol use disorder.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Hepatic antioxidant cofactor: copper, as SOD cofactor, scavenges alcohol-induced ROS in hepatocytes (already mapped) and neurons (already mapped); copper dyshomeostasis amplifies the NF-κB (already mapped) and NLRP3 (already mapped) hepatic neuroinflammatory cascade of alcohol use disorder.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — AUD calcium: calcium regulates neuron (already mapped) excitability and dopamine (already mapped) signalling; calcium dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) hepatocyte (already mapped) liver injury in AUD.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — AUD nitrogen: nitric oxide (NO, nitrogen-derived) in macrophages (already mapped) and hepatocytes (already mapped) modulates liver inflammation; NO excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade in AUD.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — AUD chloride: chloride channels in macrophages (already mapped) and hepatocytes (already mapped) regulate intracellular pH; chloride dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and TGF-β (already mapped) fibrotic cascade in AUD.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — mitochondrial oxygen in hepatocytes (already mapped) and neurons (already mapped) sustains ATP for ethanol metabolism; hypoxia amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TGF-β (already mapped) hepatic neuroinflammatory fibrotic cascade in AUD.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — carbon, via bicarbonate in hepatocytes (already mapped) and macrophages (already mapped), maintains pH homeostasis during ethanol metabolism; carbon dioxide excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TGF-β (already mapped) fibrotic cascade in AUD.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — H2S from sulfur-amino acids in hepatocytes (already mapped) and neurons (already mapped) promotes cytoprotection; sulfur deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TGF-β (already mapped) hepatic fibrotic neuroinflammatory cascade in AUD.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — AUD PD-1: PD-1 on macrophages (already mapped) and t-cytotoxic-cell (already mapped) modulates hepatic immune homeostasis; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic neuroinflammatory cascade in AUD.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — AUD angiotensin-II: angiotensin-II in hepatocytes (already mapped) and fibroblasts (already mapped) promotes TGF-β (already mapped)-driven hepatic fibrosis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) fibrotic inflammatory cascade in AUD.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — AUD VEGF: VEGF from macrophages (already mapped) and hepatocytes (already mapped) promotes hepatic angiogenesis in alcoholic liver disease; VEGF excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and IL-6 (already mapped) fibrotic cascade in AUD.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — AUD WNT/β-catenin: WNT/β-catenin in hepatocytes (already mapped) and hepatic stellate cells modulates liver repair; WNT dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) and IL-6 (already mapped) fibrotic inflammatory cascade of alcohol use disorder.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — AUD RANKL: RANKL signalling in macrophages (already mapped) and hepatocytes (already mapped) modulates liver-immune bone axis; RANKL excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and IL-6 (already mapped) fibrotic cascade of alcohol use disorder.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — AUD SMAD4: SMAD4 in hepatocytes (already mapped) and hepatic stellate cells mediates TGF-β-driven hepatic fibrosis; SMAD4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) fibrotic inflammatory cascade of alcohol use disorder.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — AUD IL-2: IL-2 in hepatic immune cells (already mapped) and gut macrophages (already mapped) modulates alcohol-driven inflammation; IL-2 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — AUD fibronectin: fibronectin in hepatic stellate cells (already mapped) and portal endothelium (already mapped) drives liver matrix deposition; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — AUD Notch: Notch signalling in hepatocytes (already mapped) and hepatic stellate cells modulates liver zonation and injury; Notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — AUD igf-1: IGF-1 from hepatocytes (already mapped) and hepatic stellate cells (already mapped) regulates liver regeneration; IGF-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — AUD activin-a: activin-A from hepatocytes (already mapped) and macrophages (already mapped) regulates liver fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — AUD cgrp: CGRP from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — AUD calcitonin: calcitonin from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic calcium balance; calcitonin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — AUD substance-p: substance-P from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic neuroinflammation; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of alcohol use disorder.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — AUD insulin-receptor: insulin receptor on hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic metabolic axis; insulin-receptor excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — AUD androgen-receptor: androgen receptor on hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — AUD adrenomedullin: adrenomedullin from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic vascular tone; adrenomedullin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — AUD osteopontin: osteopontin from hepatocytes (already mapped) and macrophages (already mapped) drives hepatic fibrotic remodelling; osteopontin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — AUD fgfr: FGFR on hepatocytes (already mapped) and macrophages (already mapped) regulates hepatic repair; FGFR dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — AUD epinephrine: epinephrine from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic stress tone; epinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — AUD renin: renin from hepatocytes (already mapped) and macrophages (already mapped) modulates hepatic fluid balance; renin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of AUD.

[^koob-2013-addiction-neuroscience]: Koob GF, Volkow ND. Neurocircuitry of addiction. *Neuropsychopharmacology.* 2010;35(1):217-238. [doi:10.1038/npp.2009.110](https://doi.org/10.1038/npp.2009.110) · [PubMed 19710631](https://pubmed.ncbi.nlm.nih.gov/19710631/)
[^anton-2006-combine]: Anton RF, O'Malley SS, Ciraulo DA, et al. Combined pharmacotherapies and behavioral interventions for alcohol dependence: the COMBINE study. *JAMA.* 2006;295(17):2003-2017. [doi:10.1001/jama.295.17.2003](https://doi.org/10.1001/jama.295.17.2003) · [PubMed 16670409](https://pubmed.ncbi.nlm.nih.gov/16670409/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
