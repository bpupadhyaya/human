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

[^koob-2013-addiction-neuroscience]: Koob GF, Volkow ND. Neurocircuitry of addiction. *Neuropsychopharmacology.* 2010;35(1):217-238. [doi:10.1038/npp.2009.110](https://doi.org/10.1038/npp.2009.110) · [PubMed 19710631](https://pubmed.ncbi.nlm.nih.gov/19710631/)
[^anton-2006-combine]: Anton RF, O'Malley SS, Ciraulo DA, et al. Combined pharmacotherapies and behavioral interventions for alcohol dependence: the COMBINE study. *JAMA.* 2006;295(17):2003-2017. [doi:10.1001/jama.295.17.2003](https://doi.org/10.1001/jama.295.17.2003) · [PubMed 16670409](https://pubmed.ncbi.nlm.nih.gov/16670409/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
