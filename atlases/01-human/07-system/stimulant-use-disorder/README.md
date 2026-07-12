---
schema: human-scale-entry/v1
id: stimulant-use-disorder
name: Stimulant Use Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Cocaine and amphetamine misuse causing pathological dopamine surges (DAT block/reversal). VTA-NAcc remodeling via ΔFosB accumulation; D2R downregulation; hypodopaminergic withdrawal state. No FDA-approved pharmacotherapy; contingency management has strongest evidence."
aliases: ["cocaine use disorder", "cocaine addiction", "methamphetamine use disorder", "stimulant addiction", "amphetamine use disorder"]
sources:
  - id: volkow-2007-cocaine-dopamine
    type: peer-reviewed
    cite: "Volkow ND, Wang GJ, Fowler JS, Telang F. Overlapping neuronal circuits in addiction and obesity: evidence of systems pathology. Philos Trans R Soc Lond B Biol Sci. 2008;363(1507):3191-200."
    doi: "10.1098/rstb.2008.0107"
    pmid: "18640918"
  - id: robinson-berridge-2003-incentive-salience
    type: peer-reviewed
    cite: "Robinson TE, Berridge KC. Addiction. Annu Rev Psychol. 2003;54:25-53."
    doi: "10.1146/annurev.psych.54.101601.145237"
    pmid: "12185211"
  - id: pettinati-2011-contingency-management
    type: peer-reviewed
    cite: "Prendergast M, Podus D, Finney J, Greenwell L, Roll J. Contingency management for treatment of substance use disorders: a meta-analysis. Addiction. 2006;101(11):1546-60."
    doi: "10.1111/j.1360-0443.2006.01581.x"
    pmid: "17034434"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Cocaine blocks DAT/NET/SERT → acute DA surge in NAcc (euphoria); amphetamines reverse DAT via TAAR1/PKC → massive cytoplasmic DA release; chronic use → D2R downregulation and ΔFosB accumulation → hypodopaminergic withdrawal state and anhedonia."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Cocaine/amphetamines block or reverse NET → acute NE surge → tachycardia, hypertension, mydriasis; PFC NE elevation → arousal and attention; chronic stimulant NE dysregulation contributes to anxiety, agitation, and withdrawal dysphoria."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Cocaine blocks SERT → ↑ synaptic 5-HT in limbic circuits; MDMA reverses SERT → massive 5-HT/DA release → empathogenic effects; chronic MDMA causes SERT downregulation and serotonergic neurotoxicity; 5-HT dysregulation modulates relapse vulnerability."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Repeated stimulant use → ΔFosB accumulation in NAcc → altered BDNF expression; BDNF in VTA sensitizes stimulant reward; withdrawal-phase BDNF changes contribute to depression and craving; BDNF/TrkB signaling is a target in relapse prevention research."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Chronic stimulant use disrupts glutamate homeostasis in NAcc via reduced system Xc activity; drug cues trigger PFC→NAcc glutamate surges → craving; N-acetylcysteine restores system Xc and reduces cue-induced craving; mGluR2/3 agonists are in clinical trials."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Stimulant use disorders remodel VTA-NAcc circuits (ΔFosB, D2R loss), PFC (gray matter thinning, ↓ inhibitory control), and amygdala (cue craving); PET shows reduced DAT and D2R in striatum; meth causes DAT terminal destruction detectable on transporter imaging."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Cocaine is directly cardiotoxic: by blocking norepinephrine reuptake and triggering α1-adrenergic coronary vasospasm it can cause myocardial infarction even in young people, plus arrhythmia and aortic dissection — cocaine chest pain is a leading drug-related ED visit."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Stimulant and opioid use disorders engage the same VTA-NAcc dopamine reward system from opposite ends, and the two increasingly overlap: 'speedball' co-use and fentanyl-adulterated cocaine/meth now drive tens of thousands of stimulant-involved overdose deaths a year."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Heavy methamphetamine or cocaine use can produce a psychosis clinically indistinguishable from schizophrenia, reflecting shared excess striatal dopamine; the paranoid delusions and hallucinations may persist for weeks after the drug stops and are treated with antipsychotics."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Stimulants are a major cause of stroke in the young: cocaine and methamphetamine drive surges in blood pressure, vasospasm and vasculitis-like arteriopathy → ischemic and hemorrhagic stroke (and MI), often within hours of use; chronic meth also accelerates small-vessel disease."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Stimulant use disorder fuels HIV transmission: methamphetamine drives high-risk sexual behavior and, when injected, needle sharing; it also worsens antiretroviral adherence and accelerates neurocognitive decline, making integrated addiction and HIV care essential."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Stimulant and alcohol use disorders commonly co-occur, and the combination is uniquely toxic: co-use of cocaine and alcohol forms cocaethylene, a longer-acting metabolite that heightens cardiac and hepatic toxicity and sudden-death risk; alcohol is often used to 'come down'."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Stimulant and cannabis use disorders often co-occur but differ pharmacologically: stimulants flood the synapse with dopamine for an intense high and crash, while cannabis acts on CB1 receptors with milder reward—using both compounds psychiatric and cardiovascular risk."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Stimulant use disorder and bipolar disorder are tightly linked and hard to disentangle: stimulant intoxication mimics mania and withdrawal mimics depression, while bipolar patients are prone to stimulant misuse—so each can trigger or mask the other."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Stimulants are directly cardiotoxic to cardiomyocytes: cocaine and methamphetamine drive catecholamine excess, vasospasm, and tachycardia that cause infarction, arrhythmia, and dilated cardiomyopathy—making cardiac disease a leading cause of death in stimulant users."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Stimulant use disorder and depression are bound by the crash: dopamine depletion after a binge produces profound dysphoria, anhedonia and fatigue that mimics and can trigger major depression, so withdrawal-driven low mood fuels relapse to restore the lost reward signal."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Stimulants are vascular poisons beyond the heart: cocaine and amphetamines cause surges in blood pressure and vasospasm that drive aortic dissection, hypertensive emergency and ischemic stroke, so the cardiovascular system bears acute catastrophic risk with every binge."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Stimulants wreck sleep: by flooding dopamine and norepinephrine they suppress sleep during binges, and the rebound crash brings hypersomnia then chronic insomnia—and the sleep deprivation worsens cravings, mood and psychosis risk in stimulant use disorder."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Stimulants directly remodel neurons: cocaine and amphetamines flood synapses with dopamine, and chronic use prunes and reshapes dendritic spines in reward circuits—structural neuroadaptations underlying the entrenched craving of stimulant use disorder."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "Stimulant use disorder has a complicated tie to ADHD: prescription stimulants effectively treat ADHD and properly used rarely cause addiction, yet diversion and misuse of these same drugs is a route into stimulant use disorder—so prescribing balances benefit and risk."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Stimulant use disorder is a chronic disorder of the nervous system's reward and control circuits: repeated dopamine surges blunt the reward system and weaken prefrontal control, so craving and relapse persist long after the drug clears—addiction as brain disease."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Stimulant use shows on the skin: methamphetamine causes formication—the sensation of 'bugs' crawling—driving compulsive picking and sores, while injection leaves track marks and abscesses, so skin findings are visible clues to stimulant use disorder."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Stimulants in pregnancy damage the placenta: cocaine and methamphetamine constrict placental vessels, raising the risk of abruption, growth restriction, and preterm birth—so stimulant use disorder in pregnancy threatens the fetus through impaired placental blood flow."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Stimulants can manufacture panic: the surge of dopamine and noradrenaline races the heart and floods the body with fight-or-flight signals, triggering panic attacks during intoxication and withdrawal—so stimulant use both mimics and worsens panic disorder."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Stimulants can wreck the kidneys: cocaine and methamphetamine cause vasoconstriction, severe hypertension and rhabdomyolysis, so acute kidney injury and, over time, chronic kidney disease are recognized harms of heavy stimulant use."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Methamphetamine inflames the brain via microglia: it activates microglia whose toxic mediators damage dopamine neurons, contributing to the lasting cognitive and movement problems seen after heavy use—neurotoxicity beyond addiction."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Stimulants drive dangerous spikes in blood pressure: cocaine and amphetamines surge catecholamines to cause acute hypertension that triggers heart attacks, strokes and aortic dissection—the cardiovascular emergencies that make stimulant toxicity lethal."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Stimulant addiction is etched into synapses: cocaine and amphetamines flood the reward pathway with dopamine, and repeated surges strengthen and remodel synaptic connections, the lasting plasticity that drives craving and relapse."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Stimulants attack the blood vessel lining: cocaine and amphetamines constrict and injure the endothelium and accelerate clotting and plaque, causing the vasospasm behind stimulant heart attacks and strokes even in young users."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Smoked stimulants injure the lungs: inhaling crack cocaine or methamphetamine causes 'crack lung'—bleeding, inflammation and fluid in the air sacs—plus pulmonary hypertension, so the route of use brings its own respiratory harm."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Stimulant overdose can spill potassium: severe hyperthermia and muscle breakdown (rhabdomyolysis) from cocaine or methamphetamine release potassium into the blood, risking dangerous hyperkalemia and fatal arrhythmias."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Cocaine can infarct the bowel: its intense vasoconstriction throttles the gut's blood supply, causing mesenteric ischemia and bowel infarction—a surgical emergency that can follow a binge even in the young."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Stimulants make platelets clot: cocaine and amphetamines activate platelets and promote thrombosis, helping spawn the heart attacks and strokes that strike stimulant users without underlying disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging reveals stimulants' harm: fMRI photons show the hyperactivated reward circuit, and CT of the head catches the strokes and brain hemorrhages that cocaine and amphetamines can trigger."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "MDMA can fatally drop sodium: the drug spurs excess water-drinking and ADH release, so dilutional hyponatremia causes the cerebral edema and seizures behind some ecstasy deaths."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Stimulants flood the sympathetic nerves: as sympathomimetics they drive the racing heart, dilated pupils and sweating, the autonomic storm of intoxication carried along peripheral nerves."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows stimulant-damaged heart muscle: the catecholamine surge from cocaine or methamphetamine forces the fibers into the wavy, hypercontracted bands of contraction-band necrosis, the microscopic mark of a drug-stressed heart."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Stimulants can scorch the liver: cocaine and MDMA cause hepatotoxicity, and the extreme hyperthermia of overdose can cook the liver into fulminant failure, a sometimes fatal complication of intoxication."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Stimulant binges deplete magnesium: poor intake and the drug's metabolic stress drain it, and the resulting low magnesium worsens the arrhythmias and vasospasm — so magnesium is given to settle a stimulant-stressed heart."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Stimulants shut down appetite and starve the gut: they suppress hunger into marked weight loss, while cocaine's vasoconstriction can choke the mesenteric and gastric vessels into ischemia and ulceration."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Stimulants drive risky sexuality: by spiking dopamine they fuel hypersexual, impulsive behavior that raises HIV and STI risk, while in pregnancy they constrict the placental vessels and harm the fetus."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Tainted cocaine can wipe out the neutrophils: levamisole, a common adulterant, causes a severe agranulocytosis and a retiform purpura vasculitis, so an unexplained crashing neutrophil count points to contaminated supply."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Stimulants clamp the arteries shut: by flooding vascular smooth muscle with catecholamines they cause intense vasospasm, the mechanism behind cocaine's heart attacks, strokes, gut ischemia, and the necrosis of the nasal septum."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "They counterfeit the body's own alarm: cocaine and amphetamines flood synapses and the circulation with catecholamines, producing the racing heart, hypertension, dilated pupils, and hyperthermia of the sympathomimetic toxidrome."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Even the pancreas can infarct: stimulant-driven vasoconstriction can cut its blood supply into ischemic pancreatitis, one of the less-known visceral injuries of the vasospasm these drugs unleash."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "Stimulants drive the spread of HIV: injection and the hypersexual, disinhibited behavior of methamphetamine and cocaine raise transmission risk, so stimulant use disorder is a major engine of new HIV infection."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Stimulants age the arteries fast: repeated catecholamine surges, hypertension, and vascular inflammation accelerate atherosclerosis, so chronic cocaine and amphetamine use brings premature coronary disease and stroke."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Addictions cluster around the reward circuit: stimulant use disorder frequently co-occurs with gambling and other behavioral addictions, sharing the dopamine-driven impulsivity that the drugs directly amplify."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Stimulants scar the brain's support cells: methamphetamine and cocaine provoke reactive astrogliosis and disrupt the blood-brain barrier astrocytes help maintain, contributing to the neurotoxicity and cognitive decline of chronic use."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Addiction has a neuroinflammatory engine: stimulants activate microglial TLR4 and the NLRP3 inflammasome, and the IL-1β released reinforces drug-seeking and the neurotoxicity behind stimulant brain injury."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Injection stimulant use spreads hepatitis C: shared needles and the binge-injection pattern of methamphetamine and cocaine make stimulant use disorder a major route of HCV transmission, alongside HIV."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Stimulants inflame the brain through NF-κB: cocaine and methamphetamine activate microglial NF-κB signaling, driving the cytokine output and neurotoxicity that underlie addiction-related brain injury."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "The needle can seed a fungus: injection stimulant use causes Candida bloodstream infection that lodges in the eyes and heart valves, the candidemia and endocarditis shared with other injection drug use."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Stimulants grind down the kidneys: cocaine and methamphetamine cause vasoconstriction, malignant hypertension and rhabdomyolysis-driven acute kidney injury that can accumulate into chronic kidney disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Stimulants wear out the heart: chronic cocaine and methamphetamine cause a toxic cardiomyopathy through catecholamine excess, tachycardia and ischemia, a leading cause of heart failure in young users."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Methamphetamine scars the lung's vessels: it is an established cause of pulmonary arterial hypertension, producing a severe drug-induced form indistinguishable from the idiopathic disease."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Injection breaches the body's barriers: non-sterile injection stimulant use seeds the blood and heart valves with bacteria, so endocarditis, abscesses and bloodstream infection can progress to sepsis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "It tears at the skin and starves it of blood: methamphetamine drives compulsive skin-picking sores and, with injection abscesses and vasoconstriction, leaves chronic wounds slow to heal in often malnourished users."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Injection opens a door for Staph: non-sterile injection of stimulants inoculates Staphylococcus aureus into skin and bloodstream, causing abscesses, cellulitis and endocarditis."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Trauma and stimulant use reinforce each other: PTSD is highly comorbid with stimulant use disorder, with stimulants used to counter numbing and hyperarousal even as use worsens the trauma symptoms."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Stimulants scar the skin and mouth: methamphetamine causes formication with compulsive skin-picking ('meth sores') and rampant 'meth mouth' dental decay, and cocaine perforates the nasal septum."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Cocaine starves the bowel of blood: its intense vasoconstriction causes mesenteric ischaemia and bowel infarction, and stimulant-driven appetite suppression leads to marked weight loss and malnutrition."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Overdose can dissolve muscle: stimulant-induced hyperthermia, agitation and seizures cause rhabdomyolysis, releasing myoglobin that can precipitate acute kidney injury."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Inhaled stimulants scar the lungs: smoking crack cocaine or methamphetamine causes 'crack lung' — acute eosinophilic pneumonitis and alveolar haemorrhage — and barotrauma with pneumothorax."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "They drive sympathetic overdrive: stimulants suppress appetite and cause weight loss, and overdose brings hyperthermia and a hypermetabolic, adrenergic storm resembling thyroid excess."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Cocaine attacks the kidney directly: it causes renal infarction and malignant hypertension with acute kidney injury, distinct from the rhabdomyolysis that also threatens renal function."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "An adulterant cripples the marrow: cocaine is widely cut with levamisole, which can cause severe agranulocytosis and an ANCA-associated vasculitis, while stimulant use broadly impairs host defence."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Injecting and risky sex spread blood-borne virus: stimulant use disorder transmits hepatitis B alongside hepatitis C and HIV, through shared needles and disinhibited behaviour."
  - target: 02-pathogen/02-bacteria/clostridium-tetani
    relation: connects-to
    note: "Contaminated injection seeds soil spores: injecting stimulants risks tetanus and wound botulism from Clostridium, especially with subcutaneous 'skin-popping'."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Stress fuels the crash and craving: corticotropin-releasing hormone and HPA-axis activation drive the dysphoric withdrawal and relapse that follow stimulant binges."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Methamphetamine scars dopamine neurons: chronic methamphetamine is toxic to striatal dopaminergic terminals and is linked to a higher later risk of Parkinson's disease."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "It lowers the seizure threshold: cocaine and amphetamines provoke seizures acutely through massive monoamine release and cerebral vasospasm, a common reason for stimulant-related emergencies."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It poisons the heart muscle: cocaine and methamphetamine cause myocardial infarction through coronary vasospasm and thrombosis, plus a dilated cardiomyopathy and arrhythmias — cardiac disease is a leading cause of stimulant death."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It ravages the arteries: stimulants cause vasospasm, hypertensive surges, accelerated atherosclerosis and aortic dissection, driving the strokes and vascular catastrophes seen with cocaine and amphetamine use."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "Stimulants serve weight control: their potent appetite suppression is exploited in eating disorders, where stimulant and appetite-suppressant misuse overlaps with anorexia nervosa and drives stimulant use disorder."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Stimulant sudden death: cocaine and methamphetamine block cardiac sodium and potassium channels and flood the heart with catecholamines, causing the arrhythmias and QRS/QT changes behind sudden cardiac death."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "Injection endocarditis: intravenous stimulant use seeds the endocardium and heart valves with skin bacteria, causing right-sided infective endocarditis and septic emboli to the lungs."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "'Crack lung': inhaled cocaine causes acute lung injury within hours—alveolar haemorrhage, oedema and eosinophilic pneumonitis flooding the gas-exchange surface."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Needle-borne infection: injection stimulant use spreads hepatitis B alongside hepatitis C and HIV through shared needles, adding chronic liver disease to the harms of stimulant use."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Kidney injury: stimulants cause acute kidney injury through rhabdomyolysis, intense vasoconstriction and malignant hypertension, damaging the glomerulus and renal tubules."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Clots from injecting: injection stimulant use causes thrombophlebitis and deep-vein thrombosis at injection sites, and the prothrombotic, vasoconstrictive drug effects raise venous thromboembolism risk."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Levamisole vasculitis: cocaine adulterated with levamisole triggers an ANCA-associated vasculitis with retiform purpura, agranulocytosis and a lupus-like syndrome, a distinctive drug-induced disease."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Mesenteric ischaemia: cocaine's intense vasoconstriction can starve the gut of blood, causing intestinal ischaemia and infarction that destroys the intestinal epithelium and bowel wall."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Stimulant rhabdomyolysis: cocaine and methamphetamine cause muscle breakdown through hyperthermia, vasoconstriction and seizures, releasing myoglobin that can precipitate acute kidney injury."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vasoconstrictor surge: cocaine and methamphetamine raise endothelin-1 and sympathetic tone, the intense vasoconstriction behind their strokes, myocardial infarctions and mesenteric ischaemia."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Glial neuroinflammation: stimulants activate microglia to release TNF-α, neuroinflammation that contributes to the neurotoxicity and cognitive deficits of chronic stimulant use."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory signalling: chronic stimulant use raises IL-6, part of the immune activation and vascular inflammation that accompany dependence and its cardiovascular harms."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "Reverse transport: amphetamines and MDMA hijack the serotonin transporter to run it in reverse, dumping monoamines into the synapse — the molecular mechanism of the rush and the serotonergic toxicity of stimulants."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: cocaine impairs nitric-oxide signalling and provokes coronary vasospasm, a key mechanism of the myocardial infarction and stroke that complicate stimulant use."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Purinergic reward modulation: adenosine A2A receptors antagonise dopamine D2 signalling in the striatum, a brake on stimulant reward that caffeine and other stimulants engage to amplify dopaminergic drive."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Craving and arousal: hypothalamic orexin drives the arousal and cue-induced craving central to stimulant use disorder, making orexin-receptor antagonists a candidate to reduce relapse and drug-seeking."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Reward-plasticity node: dopamine D2-receptor signalling converges on GSK-3β, a kinase mediating the synaptic plasticity of stimulant reward and sensitisation that underlies the compulsive use of cocaine and amphetamines."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Neuroinflammatory neurotoxicity: methamphetamine and cocaine activate microglial TLR4, driving the neuroinflammation that contributes both to reward potentiation and to the dopaminergic neurotoxicity of chronic stimulant use."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Anti-craving target: GLP-1 receptor agonists reduce the dopaminergic reward response to cocaine and methamphetamine in models, an emerging metabolic-pathway approach to dampening craving and relapse in stimulant use disorder."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Dopaminergic neurotoxicity: methamphetamine drives caspase-3-mediated apoptosis of dopaminergic neurons and terminals, the cell death behind the lasting cognitive and motor deficits and Parkinson's-disease risk of chronic heavy use."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiotoxicity: cocaine causes coronary vasospasm, accelerated atherosclerosis and direct myocardial injury, producing the troponin-positive myocardial infarction and cardiomyopathy that make stimulant use a major cardiovascular hazard."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Reward plasticity: cocaine and amphetamine drive dopamine-induced ERK activation in the striatum, the molecular trigger of the synaptic plasticity that consolidates stimulant reward and craving."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Sensitisation signalling: stimulant action on dopamine D2 receptors signals through the AKT-GSK3β axis (GSK3β already mapped), a pathway shaping the reward and behavioural sensitisation of stimulant use disorder."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Stress and relapse: HPA-axis stress signalling through the glucocorticoid receptor (CRH already mapped) drives the stress-induced craving and relapse of stimulant use disorder."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Glial neuroinflammation: stimulants activate microglial TLR4 signalling through MyD88 to NF-κB (TLR4 and NF-κB already mapped), driving the neuroinflammation that contributes to the neurotoxicity and reward dysregulation of stimulant use disorder."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Addiction plasticity: mTOR-dependent synaptic plasticity in the mesolimbic reward circuit consolidates the maladaptive learning and drug-cue associations that entrench compulsive stimulant use."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophic remodelling: BDNF signalling through its TrkB receptor (NTRK) mediates the reward-circuit synaptic remodelling underlying stimulant craving and the persistence of relapse vulnerability."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN regulation of the PI3K-AKT-mTOR axis (AKT, mTOR and GSK-3β mapped) shapes the reward-circuit synaptic plasticity underlying stimulant addiction."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Stimulant-induced microglial activation induces galectin-3, amplifying the neuroinflammation linked to stimulant neurotoxicity and addiction."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-driven JAK-STAT signalling (IL-6 mapped) transduces the neuroinflammatory milieu accompanying chronic stimulant exposure."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling (JAK1/2 already mapped) transduces the neuroinflammatory tone implicated in the reward dysregulation of stimulant use disorder."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA released by stimulant-induced glial and neuronal stress can engage cGAS-STING, contributing to the neuroinflammation of stimulant use disorder."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the interferon-associated microglial activation reported with chronic stimulant exposure."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of the PTEN-PI3K-AKT axis (PTEN and AKT already mapped) regulates the neuronal plasticity and oxidative-stress handling relevant to the reward neuroadaptations of stimulant use disorder."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to chronic stimulant use disorder."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α responses to stimulant-associated vasoconstrictive and metabolic stress contribute to the neurovascular injury of stimulant use disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) mediates the synaptic-plasticity neuroadaptations of the reward circuit in stimulant use disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK metabolic signaling participates in the neuronal energetic and oxidative stress of chronic stimulant exposure in stimulant use disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation in the reward circuit contributes to the persistent neuroadaptations and relapse vulnerability of stimulant use disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal and reward-circuit homeostasis implicated in stimulant use disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the dopamine-transporter regulation and synaptic plasticity of stimulant use disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with stimulant use disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and reward-circuit processes implicated in stimulant use disorder."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven neuroinflammation participates in the glial activation and reward-circuit changes of stimulant use disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory responses implicated in stimulant use disorder."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with stimulant use disorder."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the microglial and neuroinflammatory processes implicated in stimulant use disorder."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the reward-circuit gene programs implicated in stimulant use disorder."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences: estrogen amplifies the dopaminergic response to stimulants, and women show a faster progression to dependence (telescoping) and menstrual-cycle variation in cocaine craving, implicating sex hormones in stimulant use disorder."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Social reward: oxytocin modulates the social bonding and reward circuits disrupted by chronic stimulant use, and is under investigation as a treatment to reduce craving and stress-induced relapse."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Polysubstance overlap: stimulant use disorder increasingly co-occurs with opioid use, and mu-opioid signalling interacts with the dopaminergic reward system (dopamine already mapped), a combination behind rising stimulant-opioid overdose deaths."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response driving the craving and stress-induced relapse of stimulant use disorder."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic dysregulation: chronic stimulant use disturbs appetite, weight and glucose handling, and the resulting insulin and metabolic dysregulation add to the cardiometabolic harm of the disorder."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Neuroinflammatory balance: the anti-inflammatory cytokine IL-10 counters the TLR4-driven TNF and IL-1 (already mapped) that stimulants provoke in glia, part of the neuroinflammation implicated in stimulant neurotoxicity and dependence."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the glial neuroinflammation (IL-6, TNF and IL-1 already mapped) that stimulants provoke modulate the reward and stress circuits, part of the neurotoxicity of stimulant use disorder."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative neurotoxicity: stimulants generate oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species (NLRP3 already mapped) drive the dopaminergic neurotoxicity and cardiovascular injury of the disorder."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Cardiometabolic harm: chronic stimulant use disturbs metabolism and, with the sympathetic strain (norepinephrine already mapped) on the vasculature, contributes to the atherogenic dyslipidaemia adding to the cardiovascular harm of the disorder."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the microglial (already mapped) pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the neuroinflammation driving stimulant neurotoxicity."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and dopamine signalling: zinc modulates the dopamine transporter (dopamine already mapped) and NMDA signalling, and disturbed zinc status is linked to the reward and mood dysregulation of stimulant use disorder."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and catecholamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the catecholamine reward and toxicity of stimulant use disorder."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Neuroimmune balance: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation (TLR4, TNF and IL-1 already mapped) of the methamphetamine neurotoxicity of stimulant use disorder."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine and reward: leptin modulates the reward (dopamine already mapped) circuitry and the appetite suppression of the stimulants, part of the metabolic-reward crosstalk of stimulant use disorder."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic-cardiovascular adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic and cardiovascular (cholesterol already mapped) toxicity of stimulant use disorder."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic-cardiovascular (cholesterol already mapped) toxicity of stimulant use disorder."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Dopaminergic neurotoxicity: the methamphetamine damages the dopaminergic (already mapped) and serotonergic neurons (the terminal loss), the neurotoxicity of stimulant use disorder."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Polysubstance comorbidity: the stimulant and opioid use disorders commonly co-occur (the 'speedball', the stimulant-adulterated opioid supply), the shared reward-circuit (dopamine already mapped) vulnerability."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, contributes to the glial (microglia already mapped) neuroinflammation and the dopaminergic neurotoxicity of stimulant use disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune-inflammatory dimension (TNF and IL-1 already mapped) of chronic stimulant use."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of stimulant use disorder."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of chronic stimulant use."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of stimulant use disorder."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of stimulant use disorder."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the blood-brain-barrier disruption implicated in stimulant use disorder."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic stimulant exposure of stimulant use disorder."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Stimulant-modulated NK: the NK-cell number and cytotoxicity, altered by the chronic stimulant exposure and the stress reactivity, are part of the peripheral immune dysregulation of stimulant use disorder."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the complement activation of the neuroinflammation implicated in stimulant use disorder."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) neuroinflammation of the reward-circuit dimension of stimulant use disorder."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the neuroinflammation of stimulant use disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-neuroimmune axis: TSLP, from barrier epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the neuroinflammatory dimension of stimulant use disorder."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-neuroinflammation axis: bradykinin, via B1/B2 receptors on microglia (already mapped) and endothelium, amplifies the blood-brain-barrier disruption and the neuroinflammation of stimulant use disorder."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective cytokine: erythropoietin, via the EPOR on neurons and microglia (already mapped), reduces oxidative stress and apoptosis in the neuroinflammatory dimension of stimulant use disorder."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-reward axis: histamine, from tuberomammillary-nucleus (brain already mapped) neurons and mast cells (already mapped), modulates the dopaminergic (dopamine already mapped) reward circuitry and the sleep-wake dysregulation of stimulant use disorder."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-reward axis: stimulant use disrupts melatonin secretion and circadian rhythm; melatonin dysregulation perpetuates the insomnia (already mapped) and the dopaminergic (dopamine already mapped) reward-clock coupling of stimulant use disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement-contact brake: C1-esterase inhibitor regulates the classical-complement and contact-system (bradykinin already mapped) activation contributing to the neuroinflammation and the microglial (already mapped) TLR4-driven neuroinflammation of stimulant use disorder."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "SUD testosterone: testosterone, via androgen receptors on neurons (already mapped) and microglia (already mapped), modulates dopaminergic reward; testosterone deficiency amplifies the CRH (already mapped) and norepinephrine (already mapped) cascade of stimulant use disorder."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "SUD prolactin: prolactin, via PRLR on neurons (already mapped) and microglia (already mapped), modulates dopaminergic reward; hyperprolactinaemia amplifies the CRH (already mapped) and norepinephrine (already mapped) cascade of stimulant use disorder."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "SUD vasopressin: vasopressin, via V1aR on neurons (already mapped) and microglia (already mapped), modulates HPA-axis (CRH already mapped) tone; vasopressin dysregulation amplifies norepinephrine (already mapped) and NLRP3 (already mapped) cascade of stimulant use disorder."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "SUD selenium: selenium, as GPx in neurons (already mapped) and microglia (already mapped), scavenges dopaminergic (dopamine already mapped) neuroinflammatory ROS; selenium deficiency amplifies the CRH (already mapped) and NLRP3 (already mapped) cascade of stimulant use disorder."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "SUD iodine: iodine-dependent thyroid hormones modulate dopaminergic (dopamine already mapped) and serotonergic (serotonin already mapped) tone; iodine deficiency impairs thyroid-mediated regulation of the CRH (already mapped) stress axis of stimulant use disorder."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "SUD phosphorus: phosphorus, as ATP in neurons (already mapped) and synapses (already mapped), sustains dopaminergic (dopamine already mapped) vesicle release; phosphorus deficiency amplifies the NLRP3 (already mapped) neuroinflammation of stimulant use disorder."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "SUD iron: iron supports neuron (already mapped) dopamine (already mapped) and serotonin (already mapped) synthesis; iron deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and BDNF (already mapped) dysregulation in stimulant use disorder."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "SUD calcium: calcium gates neuron (already mapped) dopamine (already mapped) release via vesicular exocytosis; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and BDNF (already mapped) suppression in stimulant use disorder."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "SUD chloride: chloride, via KCC2 in GABAergic neurons (already mapped), sets inhibitory tone; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and serotonin (already mapped) signalling deficits in stimulant use disorder."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "SUD sulfur: hydrogen sulfide from neurons (already mapped) modulates dopamine (already mapped) signalling; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) suppression in stimulant use disorder."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "SUD carbon: carbon, as metabolic backbone of dopamine (already mapped) and BDNF (already mapped) in neurons (already mapped), drives synaptic energy metabolism; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of stimulant use disorder."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "SUD hydrogen: hydrogen, via redox homeostasis in neurons (already mapped) and macrophages (already mapped), modulates dopamine (already mapped) oxidative stress; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of stimulant use disorder."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "SUD nitrogen: nitric oxide from neurons (already mapped) modulates dopamine (already mapped) signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and serotonin (already mapped) cascade of stimulant use disorder."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "SUD oxygen: reactive oxygen species in neurons (already mapped) and macrophages (already mapped) drive oxidative neuronal damage; oxygen imbalance amplifies dopamine (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of stimulant use disorder."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "SUD PD-1: PD-1 checkpoint signalling in T-cells (already mapped) and microglia (already mapped) modulates neuroinflammatory tone; PD-1 dysregulation amplifies dopamine (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of stimulant use disorder."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "SUD angiotensin-II: angiotensin-II signalling in neurons (already mapped) and macrophages (already mapped) promotes inflammation; angiotensin-II excess amplifies dopamine (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of stimulant use disorder."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "SUD wnt-beta-catenin: WNT/β-catenin on neurons (already mapped) and astrocytes (already mapped) regulates reward circuit plasticity; wnt-beta-catenin loss amplifies nf-kb (already mapped) and dopamine (already mapped) and crh (already mapped) cascade of SUD."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "SUD rankl: RANKL from macrophages (already mapped) and astrocytes (already mapped) promotes neuroinflammatory immune activation; rankl excess amplifies nf-kb (already mapped) and dopamine (already mapped) and crh (already mapped) cascade of SUD."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "SUD smad4: SMAD4 in neurons (already mapped) and astrocytes (already mapped) transduces TGF-β signals; smad4 loss amplifies nf-kb (already mapped) and dopamine (already mapped) and crh (already mapped) cascade of SUD."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "SUD il-2: IL-2 from T-cells (already mapped) and microglia (already mapped) regulates neuroinflammatory surveillance in stimulant circuits; il-2 dysregulation amplifies nf-kb (already mapped) and dopamine (already mapped) and crh (already mapped) cascade of SUD."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "SUD vegf: VEGF from macrophages (already mapped) and astrocytes (already mapped) drives neuroinflammatory angiogenesis in stimulant use disorder; vegf dysregulation amplifies nf-kb (already mapped) and dopamine (already mapped) and crh (already mapped) cascade of SUD."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "SUD fibronectin: fibronectin in neurons (already mapped) and astrocytes (already mapped) promotes CNS ECM remodelling in stimulant circuits; fibronectin excess amplifies nf-kb (already mapped) and dopamine (already mapped) and crh (already mapped) cascade of SUD."
---

# Stimulant Use Disorder

## Overview

Stimulant use disorder encompasses the pathological use of psychostimulants — primarily **cocaine** (plant-derived alkaloid from Erythroxylum coca) and **amphetamines** (synthetic amines: d-amphetamine, methamphetamine, MDMA) — characterized by compulsive drug-seeking, loss of control, and continuation despite adverse consequences. Despite shared clinical features, cocaine and amphetamine have distinct molecular mechanisms: cocaine is a **monoamine transporter reuptake inhibitor** (blocking DAT, NET, and SERT), while amphetamines are **monoamine releasers** (reversing DAT/NET via intracellular mechanisms) [^robinson-berridge-2003-incentive-salience].

Both produce pathological surges of dopamine in the nucleus accumbens that are far in excess of any natural reward — estimated at 3–5× the DA release from sex, food, or social reward in preclinical models. This supraphysiological DA flooding drives the reward learning and neural remodeling that constitutes addiction.

The public health burden is substantial: approximately **5 million Americans** had cocaine use disorder and **2.5 million** had methamphetamine use disorder in recent National Survey on Drug Use and Health estimates. The methamphetamine epidemic has intensified dramatically with illicitly manufactured supply. Despite decades of research, **no FDA-approved pharmacotherapy** exists for stimulant use disorders; **contingency management** (voucher-based behavioral reinforcement) has the strongest evidence base [^pettinati-2011-contingency-management].

## Structure

### Pharmacology: Cocaine vs. Amphetamine Mechanisms

| Feature | Cocaine | Amphetamine / Methamphetamine |
|:---|:---|:---|
| **Primary mechanism** | DAT/NET/SERT competitive reuptake inhibitor | DAT/NET reversal (efflux via TAAR1 + PKC-DAT phosphorylation) |
| **DA source** | Prevents reuptake → synaptic accumulation | Reverses DAT → cytoplasmic DA effluxed regardless of vesicle release |
| **Onset** | Rapid (IV/smoked: seconds; intranasal: minutes) | Rapid (IV/smoked: seconds; oral: 30–60 min) |
| **Duration** | Short (45–90 min; intense "high") | Long (8–12+ h for methamphetamine) |
| **NE effects** | NET block → NE surge → ↑BP, ↑HR | NET reversal → NE efflux → ↑BP, ↑HR, ↑arousal |
| **SERT effects** | SERT block → ↑ synaptic 5-HT | Moderate 5-HT reversal (less than DA/NE) |
| **Local anesthetic** | Yes (Na⁺ channel block; used in ENT surgery) | No |
| **Neurotoxicity** | Primarily vascular (stroke, vasospasm) | Direct dopaminergic/serotonergic neurotoxicity (oxidative stress) |
| **MDMA distinction** | — | MDMA: primarily SERT reversal → massive 5-HT release; also DAT reversal |

### Key Molecular Targets

**Dopamine transporter (DAT/SLC6A3):**
- Cocaine binds to the outward-facing conformation of DAT → competitive blockade → DA accumulates in synapse
- Amphetamine enters neurons via DAT → activates TAAR1 (intracellular receptor) → Gβγ → PKC → phosphorylates DAT Ser7 → DAT internalization and reversal → DA efflux independent of vesicle release
- With repeated cocaine: DAT expression initially upregulates (tolerance attempt); with meth: DAT is internalized and neurotoxic oxidative damage reduces DAT permanently

**ΔFosB accumulation:**
- Repeated stimulant administration → acute FosB (bZIP transcription factor) → truncated isoform ΔFosB accumulates (highly stable; half-life weeks)
- ΔFosB in NAcc → altered transcription: ↑CyclinD3, ↑GluR2 → sensitized reward circuit
- ΔFosB is the molecular "switch" converting recreational use into compulsive addiction; ΔFosB levels predict the degree of behavioral sensitization

## Function

### Acute Effects: Dopamine Storm

**Mesolimbic circuit:**
- Normal eating/sex: NAcc dopamine increases ~100–150% above baseline
- Cocaine (0.5 mg/kg IV): NAcc DA increases ~300–400% above baseline
- Peak plasma DA in NAcc during stimulant high is far outside the range of any natural reward — producing an artificial "superstimulus" that drives powerful associative learning

**Incentive salience hijacking (Robinson-Berridge model) [^robinson-berridge-2003-incentive-salience]:**
- Liking (hedonic pleasure): mediated by opioid/endocannabinoid systems in NAcc hot zones
- Wanting (incentive salience): mediated by mesolimbic DA
- With repeated stimulant use: sensitized DA system → ↑"wanting" (craving) even as "liking" (hedonic pleasure) decreases (hedonic tolerance)
- This dissociation explains compulsive drug-seeking despite diminishing pleasure

**Peripheral sympathomimetic effects (acute):**
- NE surge → ↑ heart rate, ↑ blood pressure, mydriasis, hyperthermia
- Cocaine additional effects: local anesthetic (membrane-stabilizing), coronary vasospasm (risk of MI even in young patients without coronary artery disease)
- Hypertensive crisis risk with MAOIs (contraindicated combination)

### Chronic Effects: Neuroplasticity and Hypodopaminergic State

With repeated use, compensatory downregulation shifts the brain toward a **hypodopaminergic state** during abstinence:

| Change | Mechanism | Consequence |
|:---|:---|:---|
| **↓ D2R in striatum** | Receptor downregulation in response to chronic DA excess | Anhedonia, inability to feel reward from natural stimuli; drives continued drug seeking |
| **↓ DAT availability** | Meth: oxidative damage to dopaminergic terminals; cocaine: compensation then depletion | Reduced capacity for normal DA cycling; persists months-years |
| **ΔFosB accumulation** | Stable truncated FosB isoform in NAcc | Sensitized response to drug and drug cues; drives craving |
| **Glutamate dysregulation** | ↓ System Xc activity in NAcc → ↓ extrasynaptic glutamate → loss of mGluR2/3 autoreceptor tone | Cue-triggered PFC→NAcc glutamate surge → craving/relapse |
| **PFC gray matter loss** | Chronic stimulant-induced inflammation, oxidative stress | ↓ Inhibitory control over drug seeking; impaired decision-making |
| **Amygdala sensitization** | Drug-cue conditioning → fear/craving overlap | Intense cue-triggered craving; high relapse risk in cue-rich environments |

### Methamphetamine Neurotoxicity

Unlike cocaine, methamphetamine causes **direct neurotoxic damage** to dopaminergic and serotonergic terminals:
- METH entry into neurons → reverses VMAT2 → DA released from vesicles into cytoplasm → oxidation → hydroxyl radical formation → protein carbonylation, lipid peroxidation
- Terminal damage: striatal DAT density reduced 50–80% in long-term users (PET imaging)
- Serotonergic terminals damaged by oxidative 5-HT metabolism (less severe than DA)
- Microglial activation in striatum and PFC → neuroinflammation → further neuronal loss
- Partial recovery of DAT with prolonged abstinence (12+ months) possible but often incomplete

## Pathology

### Clinical Presentation

**Intoxication:**
- Euphoria, increased energy, decreased appetite, hyperthermia, tachycardia, hypertension, mydriasis, insomnia
- Cocaine: intense but brief high (45–90 min); "binge" pattern driven by short duration
- Meth: prolonged (8–12 h) high; binge-crash cycles lasting days ("tweaking")
- Severe: paranoid psychosis (especially with meth — can be clinically indistinguishable from schizophrenia), hallucinations, violent behavior, hyperthermia, cardiac arrhythmia

**Cocaine cardiac complications:**
- Coronary vasospasm → MI in young adults (mechanism: α1-adrenergic + reduced endothelial NO)
- Aortic dissection (hypertensive crisis)
- QTc prolongation → ventricular arrhythmias
- Cocaine-associated chest pain is the leading cause of drug-related ED visits in adults

**Withdrawal:**
- Dysphoric "crash": profound anhedonia, fatigue, hypersomnia, depression (hours to days)
- No physical withdrawal syndrome (unlike opioids or alcohol) — psychological withdrawal
- Craving peaks at 1–3 days, subsides but persists for months; cue-triggered craving can persist years

**Stimulant-induced psychosis:**
- High-dose meth (or cocaine) → transient psychosis with auditory/visual/tactile hallucinations, paranoid delusions
- Can persist weeks after cessation in some patients
- Clinically difficult to distinguish from primary schizophrenia without history; treated with antipsychotics

### Epidemiology and Comorbidities

| Feature | Value |
|:---|:---|
| **US cocaine use disorder** | ~5 million (2022 NSDUH) |
| **US meth use disorder** | ~2.5 million |
| **HIV risk** | ↑ 3–5× (IV use + risky sexual behavior on meth) |
| **HCV risk** | ↑ (IV use) |
| **Comorbid MDD** | ~50–60% |
| **Comorbid anxiety** | ~40–50% |
| **Comorbid AUD** | ~30–40% |
| **Comorbid ASPD** | ~30% |
| **Overdose deaths** | Stimulants cause ~30,000 deaths/year in US (often combined with fentanyl) |

## Connections

- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — cocaine blocks DAT/NET/SERT → DA accumulates in NAcc synapse; amphetamines reverse DAT → massive cytoplasmic DA efflux; chronic use → D2R downregulation, ΔFosB accumulation, and hypodopaminergic withdrawal state; PET shows ↓ striatal D2R availability predicts poor treatment outcomes.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — stimulants block or reverse NET → acute NE surge → tachycardia, hypertension, ↑ arousal; cocaine coronary vasospasm mediated partly by α1-NE stimulation; chronic NE dysregulation contributes to anxiety, agitation, and withdrawal dysphoria in stimulant use disorder.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — cocaine blocks SERT → ↑ synaptic 5-HT in limbic circuits; MDMA reverses SERT → massive 5-HT release → empathogenic effects; chronic MDMA causes serotonergic neurotoxicity (SERT downregulation); serotonergic modulation influences relapse vulnerability in stimulant use disorder.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — repeated cocaine/amphetamine drives ΔFosB accumulation in NAcc → altered BDNF/TrkB expression; BDNF in VTA sensitizes stimulant reward; withdrawal-phase BDNF changes contribute to depression and craving; BDNF dysregulation is a therapeutic target for relapse prevention.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — chronic stimulant use disrupts glutamate homeostasis in NAcc via reduced system Xc activity; drug cues trigger PFC→NAcc glutamate surges that drive craving; N-acetylcysteine (restores system Xc) and mGluR2/3 agonists (reduce prefrontal glutamate release) are in clinical trials for stimulant relapse prevention.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — stimulant use disorders remodel VTA-NAcc circuits (ΔFosB, D2R loss), PFC (gray matter thinning, impaired inhibitory control), amygdala (cue-conditioned craving), and LC-NE arousal circuits; PET shows reduced DAT and D2R in striatum of chronic users; meth causes DAT terminal destruction detectable by TRODAT/FP-CIT imaging.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Cocaine is directly cardiotoxic: by blocking norepinephrine reuptake and triggering α1-adrenergic coronary vasospasm it can cause myocardial infarction even in young people, plus arrhythmia and aortic dissection — cocaine chest pain is a leading drug-related ED visit.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Stimulant and opioid use disorders engage the same VTA-NAcc dopamine reward system from opposite ends, and the two increasingly overlap: 'speedball' co-use and fentanyl-adulterated cocaine/meth now drive tens of thousands of stimulant-involved overdose deaths a year.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Heavy methamphetamine or cocaine use can produce a psychosis clinically indistinguishable from schizophrenia, reflecting shared excess striatal dopamine; the paranoid delusions and hallucinations may persist for weeks after the drug stops and are treated with antipsychotics.
- `connects-to` → **[Stroke](../stroke/README.md)** — Stimulants are a major cause of stroke in the young: cocaine and methamphetamine drive surges in blood pressure, vasospasm and vasculitis-like arteriopathy → ischemic and hemorrhagic stroke (and MI), often within hours of use; chronic meth also accelerates small-vessel disease.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Stimulant use disorder fuels HIV transmission: methamphetamine drives high-risk sexual behavior and, when injected, needle sharing; it also worsens antiretroviral adherence and accelerates neurocognitive decline, making integrated addiction and HIV care essential.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Stimulant and alcohol use disorders commonly co-occur, and the combination is uniquely toxic: co-use of cocaine and alcohol forms cocaethylene, a longer-acting metabolite that heightens cardiac and hepatic toxicity and sudden-death risk; alcohol is often used to 'come down'.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Stimulant and cannabis use disorders often co-occur but differ pharmacologically: stimulants flood the synapse with dopamine for an intense high and crash, while cannabis acts on CB1 receptors with milder reward—using both compounds psychiatric and cardiovascular risk.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Stimulant use disorder and bipolar disorder are tightly linked and hard to disentangle: stimulant intoxication mimics mania and withdrawal mimics depression, while bipolar patients are prone to stimulant misuse—so each can trigger or mask the other.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Stimulants are directly cardiotoxic to cardiomyocytes: cocaine and methamphetamine drive catecholamine excess, vasospasm, and tachycardia that cause infarction, arrhythmia, and dilated cardiomyopathy—making cardiac disease a leading cause of death in stimulant users.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Stimulant use disorder and depression are bound by the crash: dopamine depletion after a binge produces profound dysphoria, anhedonia and fatigue that mimics and can trigger major depression, so withdrawal-driven low mood fuels relapse to restore the lost reward signal.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Stimulants are vascular poisons beyond the heart: cocaine and amphetamines cause surges in blood pressure and vasospasm that drive aortic dissection, hypertensive emergency and ischemic stroke, so the cardiovascular system bears acute catastrophic risk with every binge.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Stimulants wreck sleep: by flooding dopamine and norepinephrine they suppress sleep during binges, and the rebound crash brings hypersomnia then chronic insomnia—and the sleep deprivation worsens cravings, mood and psychosis risk in stimulant use disorder.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Stimulants directly remodel neurons: cocaine and amphetamines flood synapses with dopamine, and chronic use prunes and reshapes dendritic spines in reward circuits—structural neuroadaptations underlying the entrenched craving of stimulant use disorder.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — Stimulant use disorder has a complicated tie to ADHD: prescription stimulants effectively treat ADHD and properly used rarely cause addiction, yet diversion and misuse of these same drugs is a route into stimulant use disorder—so prescribing balances benefit and risk.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Stimulant use disorder is a chronic disorder of the nervous system's reward and control circuits: repeated dopamine surges blunt the reward system and weaken prefrontal control, so craving and relapse persist long after the drug clears—addiction as brain disease.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Stimulant use shows on the skin: methamphetamine causes formication—the sensation of 'bugs' crawling—driving compulsive picking and sores, while injection leaves track marks and abscesses, so skin findings are visible clues to stimulant use disorder.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Stimulants in pregnancy damage the placenta: cocaine and methamphetamine constrict placental vessels, raising the risk of abruption, growth restriction, and preterm birth—so stimulant use disorder in pregnancy threatens the fetus through impaired placental blood flow.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Stimulants can manufacture panic: the surge of dopamine and noradrenaline races the heart and floods the body with fight-or-flight signals, triggering panic attacks during intoxication and withdrawal—so stimulant use both mimics and worsens panic disorder.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Stimulants can wreck the kidneys: cocaine and methamphetamine cause vasoconstriction, severe hypertension and rhabdomyolysis, so acute kidney injury and, over time, chronic kidney disease are recognized harms of heavy stimulant use.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Methamphetamine inflames the brain via microglia: it activates microglia whose toxic mediators damage dopamine neurons, contributing to the lasting cognitive and movement problems seen after heavy use—neurotoxicity beyond addiction.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Stimulants drive dangerous spikes in blood pressure: cocaine and amphetamines surge catecholamines to cause acute hypertension that triggers heart attacks, strokes and aortic dissection—the cardiovascular emergencies that make stimulant toxicity lethal.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Stimulant addiction is etched into synapses: cocaine and amphetamines flood the reward pathway with dopamine, and repeated surges strengthen and remodel synaptic connections, the lasting plasticity that drives craving and relapse.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Stimulants attack the blood vessel lining: cocaine and amphetamines constrict and injure the endothelium and accelerate clotting and plaque, causing the vasospasm behind stimulant heart attacks and strokes even in young users.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Smoked stimulants injure the lungs: inhaling crack cocaine or methamphetamine causes 'crack lung'—bleeding, inflammation and fluid in the air sacs—plus pulmonary hypertension, so the route of use brings its own respiratory harm.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Stimulant overdose can spill potassium: severe hyperthermia and muscle breakdown (rhabdomyolysis) from cocaine or methamphetamine release potassium into the blood, risking dangerous hyperkalemia and fatal arrhythmias.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Cocaine can infarct the bowel: its intense vasoconstriction throttles the gut's blood supply, causing mesenteric ischemia and bowel infarction—a surgical emergency that can follow a binge even in the young.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Stimulants make platelets clot: cocaine and amphetamines activate platelets and promote thrombosis, helping spawn the heart attacks and strokes that strike stimulant users without underlying disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging reveals stimulants' harm: fMRI photons show the hyperactivated reward circuit, and CT of the head catches the strokes and brain hemorrhages that cocaine and amphetamines can trigger.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — MDMA can fatally drop sodium: the drug spurs excess water-drinking and ADH release, so dilutional hyponatremia causes the cerebral edema and seizures behind some ecstasy deaths.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Stimulants flood the sympathetic nerves: as sympathomimetics they drive the racing heart, dilated pupils and sweating, the autonomic storm of intoxication carried along peripheral nerves.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows stimulant-damaged heart muscle: the catecholamine surge from cocaine or methamphetamine forces the fibers into the wavy, hypercontracted bands of contraction-band necrosis, the microscopic mark of a drug-stressed heart.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Stimulants can scorch the liver: cocaine and MDMA cause hepatotoxicity, and the extreme hyperthermia of overdose can cook the liver into fulminant failure, a sometimes fatal complication of intoxication.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Stimulant binges deplete magnesium: poor intake and the drug's metabolic stress drain it, and the resulting low magnesium worsens the arrhythmias and vasospasm — so magnesium is given to settle a stimulant-stressed heart.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Stimulants shut down appetite and starve the gut: they suppress hunger into marked weight loss, while cocaine's vasoconstriction can choke the mesenteric and gastric vessels into ischemia and ulceration.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Stimulants drive risky sexuality: by spiking dopamine they fuel hypersexual, impulsive behavior that raises HIV and STI risk, while in pregnancy they constrict the placental vessels and harm the fetus.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Tainted cocaine can wipe out the neutrophils: levamisole, a common adulterant, causes a severe agranulocytosis and a retiform purpura vasculitis, so an unexplained crashing neutrophil count points to contaminated supply.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Stimulants clamp the arteries shut: by flooding vascular smooth muscle with catecholamines they cause intense vasospasm, the mechanism behind cocaine's heart attacks, strokes, gut ischemia, and the necrosis of the nasal septum.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — They counterfeit the body's own alarm: cocaine and amphetamines flood synapses and the circulation with catecholamines, producing the racing heart, hypertension, dilated pupils, and hyperthermia of the sympathomimetic toxidrome.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Even the pancreas can infarct: stimulant-driven vasoconstriction can cut its blood supply into ischemic pancreatitis, one of the less-known visceral injuries of the vasospasm these drugs unleash.
- `connects-to` → **[HIV](../hiv/README.md)** — Stimulants drive the spread of HIV: injection and the hypersexual, disinhibited behavior of methamphetamine and cocaine raise transmission risk, so stimulant use disorder is a major engine of new HIV infection.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Stimulants age the arteries fast: repeated catecholamine surges, hypertension, and vascular inflammation accelerate atherosclerosis, so chronic cocaine and amphetamine use brings premature coronary disease and stroke.
- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — Addictions cluster around the reward circuit: stimulant use disorder frequently co-occurs with gambling and other behavioral addictions, sharing the dopamine-driven impulsivity that the drugs directly amplify.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Stimulants scar the brain's support cells: methamphetamine and cocaine provoke reactive astrogliosis and disrupt the blood-brain barrier astrocytes help maintain, contributing to the neurotoxicity and cognitive decline of chronic use.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Addiction has a neuroinflammatory engine: stimulants activate microglial TLR4 and the NLRP3 inflammasome, and the IL-1β released reinforces drug-seeking and the neurotoxicity behind stimulant brain injury.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Injection stimulant use spreads hepatitis C: shared needles and the binge-injection pattern of methamphetamine and cocaine make stimulant use disorder a major route of HCV transmission, alongside HIV.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Stimulants inflame the brain through NF-κB: cocaine and methamphetamine activate microglial NF-κB signaling, driving the cytokine output and neurotoxicity that underlie addiction-related brain injury.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — The needle can seed a fungus: injection stimulant use causes Candida bloodstream infection that lodges in the eyes and heart valves, the candidemia and endocarditis shared with other injection drug use.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Stimulants grind down the kidneys: cocaine and methamphetamine cause vasoconstriction, malignant hypertension and rhabdomyolysis-driven acute kidney injury that can accumulate into chronic kidney disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Stimulants wear out the heart: chronic cocaine and methamphetamine cause a toxic cardiomyopathy through catecholamine excess, tachycardia and ischemia, a leading cause of heart failure in young users.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Methamphetamine scars the lung's vessels: it is an established cause of pulmonary arterial hypertension, producing a severe drug-induced form indistinguishable from the idiopathic disease.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Injection breaches the body's barriers: non-sterile injection stimulant use seeds the blood and heart valves with bacteria, so endocarditis, abscesses and bloodstream infection can progress to sepsis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — It tears at the skin and starves it of blood: methamphetamine drives compulsive skin-picking sores and, with injection abscesses and vasoconstriction, leaves chronic wounds slow to heal in often malnourished users.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Injection opens a door for Staph: non-sterile injection of stimulants inoculates Staphylococcus aureus into skin and bloodstream, causing abscesses, cellulitis and endocarditis.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Trauma and stimulant use reinforce each other: PTSD is highly comorbid with stimulant use disorder, with stimulants used to counter numbing and hyperarousal even as use worsens the trauma symptoms.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Stimulants scar the skin and mouth: methamphetamine causes formication with compulsive skin-picking ('meth sores') and rampant 'meth mouth' dental decay, and cocaine perforates the nasal septum.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Cocaine starves the bowel of blood: its intense vasoconstriction causes mesenteric ischaemia and bowel infarction, and stimulant-driven appetite suppression leads to marked weight loss and malnutrition.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Overdose can dissolve muscle: stimulant-induced hyperthermia, agitation and seizures cause rhabdomyolysis, releasing myoglobin that can precipitate acute kidney injury.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Inhaled stimulants scar the lungs: smoking crack cocaine or methamphetamine causes 'crack lung' — acute eosinophilic pneumonitis and alveolar haemorrhage — and barotrauma with pneumothorax.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — They drive sympathetic overdrive: stimulants suppress appetite and cause weight loss, and overdose brings hyperthermia and a hypermetabolic, adrenergic storm resembling thyroid excess.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Cocaine attacks the kidney directly: it causes renal infarction and malignant hypertension with acute kidney injury, distinct from the rhabdomyolysis that also threatens renal function.
- `connects-to` → **[Immune System](../immune-system/README.md)** — An adulterant cripples the marrow: cocaine is widely cut with levamisole, which can cause severe agranulocytosis and an ANCA-associated vasculitis, while stimulant use broadly impairs host defence.
- `connects-to` → **[Hepatitis B virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Injecting and risky sex spread blood-borne virus: stimulant use disorder transmits hepatitis B alongside hepatitis C and HIV, through shared needles and disinhibited behaviour.
- `connects-to` → **[Clostridium tetani](../../../02-pathogen/02-bacteria/clostridium-tetani/README.md)** — Contaminated injection seeds soil spores: injecting stimulants risks tetanus and wound botulism from Clostridium, especially with subcutaneous 'skin-popping'.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Stress fuels the crash and craving: corticotropin-releasing hormone and HPA-axis activation drive the dysphoric withdrawal and relapse that follow stimulant binges.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Methamphetamine scars dopamine neurons: chronic methamphetamine is toxic to striatal dopaminergic terminals and is linked to a higher later risk of Parkinson's disease.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — It lowers the seizure threshold: cocaine and amphetamines provoke seizures acutely through massive monoamine release and cerebral vasospasm, a common reason for stimulant-related emergencies.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It poisons the heart muscle: cocaine and methamphetamine cause myocardial infarction through coronary vasospasm and thrombosis, plus a dilated cardiomyopathy and arrhythmias — cardiac disease is a leading cause of stimulant death.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It ravages the arteries: stimulants cause vasospasm, hypertensive surges, accelerated atherosclerosis and aortic dissection, driving the strokes and vascular catastrophes seen with cocaine and amphetamine use.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — Stimulants serve weight control: their potent appetite suppression is exploited in eating disorders, where stimulant and appetite-suppressant misuse overlaps with anorexia nervosa and drives stimulant use disorder.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Stimulant sudden death: cocaine and methamphetamine block cardiac sodium and potassium channels and flood the heart with catecholamines, causing the arrhythmias and QRS/QT changes behind sudden cardiac death.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — Injection endocarditis: intravenous stimulant use seeds the endocardium and heart valves with skin bacteria, causing right-sided infective endocarditis and septic emboli to the lungs.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — 'Crack lung': inhaled cocaine causes acute lung injury within hours—alveolar haemorrhage, oedema and eosinophilic pneumonitis flooding the gas-exchange surface.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Needle-borne infection: injection stimulant use spreads hepatitis B alongside hepatitis C and HIV through shared needles, adding chronic liver disease to the harms of stimulant use.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Kidney injury: stimulants cause acute kidney injury through rhabdomyolysis, intense vasoconstriction and malignant hypertension, damaging the glomerulus and renal tubules.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Clots from injecting: injection stimulant use causes thrombophlebitis and deep-vein thrombosis at injection sites, and the prothrombotic, vasoconstrictive drug effects raise venous thromboembolism risk.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Levamisole vasculitis: cocaine adulterated with levamisole triggers an ANCA-associated vasculitis with retiform purpura, agranulocytosis and a lupus-like syndrome, a distinctive drug-induced disease.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Mesenteric ischaemia: cocaine's intense vasoconstriction can starve the gut of blood, causing intestinal ischaemia and infarction that destroys the intestinal epithelium and bowel wall.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Stimulant rhabdomyolysis: cocaine and methamphetamine cause muscle breakdown through hyperthermia, vasoconstriction and seizures, releasing myoglobin that can precipitate acute kidney injury.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vasoconstrictor surge: cocaine and methamphetamine raise endothelin-1 and sympathetic tone, the intense vasoconstriction behind their strokes, myocardial infarctions and mesenteric ischaemia.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Glial neuroinflammation: stimulants activate microglia to release TNF-α, neuroinflammation that contributes to the neurotoxicity and cognitive deficits of chronic stimulant use.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory signalling: chronic stimulant use raises IL-6, part of the immune activation and vascular inflammation that accompany dependence and its cardiovascular harms.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — Reverse transport: amphetamines and MDMA hijack the serotonin transporter to run it in reverse, dumping monoamines into the synapse — the molecular mechanism of the rush and the serotonergic toxicity of stimulants.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial dysfunction: cocaine impairs nitric-oxide signalling and provokes coronary vasospasm, a key mechanism of the myocardial infarction and stroke that complicate stimulant use.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Purinergic reward modulation: adenosine A2A receptors antagonise dopamine D2 signalling in the striatum, a brake on stimulant reward that caffeine and other stimulants engage to amplify dopaminergic drive.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Hypothalamic orexin drives the arousal and cue-induced craving central to stimulant use disorder, making orexin-receptor antagonists a candidate strategy to reduce relapse and drug-seeking behavior.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — Dopamine D2-receptor signaling converges on GSK-3β, a kinase mediating the synaptic plasticity of stimulant reward and sensitization that underlies the compulsive use of cocaine and amphetamines.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Methamphetamine and cocaine activate microglial TLR4, driving the neuroinflammation that contributes both to reward potentiation and to the dopaminergic neurotoxicity of chronic stimulant use.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — GLP-1 receptor agonists reduce the dopaminergic reward response to cocaine and methamphetamine in models, an emerging metabolic-pathway approach to dampening craving and relapse in stimulant use disorder.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Methamphetamine drives caspase-3-mediated apoptosis of dopaminergic neurons and terminals, the cell death behind the lasting cognitive and motor deficits and Parkinson's-disease risk of chronic heavy use.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cocaine causes coronary vasospasm, accelerated atherosclerosis and direct myocardial injury, producing the troponin-positive myocardial infarction and cardiomyopathy that make stimulant use a major cardiovascular hazard.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Cocaine and amphetamine drive dopamine-induced ERK activation in the striatum, the molecular trigger of the synaptic plasticity that consolidates stimulant reward and craving.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Stimulant action on dopamine D2 receptors signals through the AKT-GSK3β axis (GSK3β already mapped), a pathway shaping the reward and behavioral sensitization of stimulant use disorder.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — HPA-axis stress signaling through the glucocorticoid receptor (CRH already mapped) drives the stress-induced craving and relapse of stimulant use disorder.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Stimulants activate microglial TLR4 signaling through MyD88 to NF-κB (TLR4 and NF-κB already mapped), driving the neuroinflammation that contributes to the neurotoxicity and reward dysregulation of stimulant use disorder.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-dependent synaptic plasticity in the mesolimbic reward circuit consolidates the maladaptive learning and drug-cue associations that entrench compulsive stimulant use.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor (NTRK) mediates the reward-circuit synaptic remodeling underlying stimulant craving and the persistence of relapse vulnerability.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN regulation of the PI3K-AKT-mTOR axis (AKT, mTOR and GSK-3β mapped) shapes the reward-circuit synaptic plasticity underlying stimulant addiction.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Stimulant-induced microglial activation induces galectin-3, amplifying the neuroinflammation linked to stimulant neurotoxicity and addiction.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine-driven JAK-STAT signaling (IL-6 mapped) transduces the neuroinflammatory milieu accompanying chronic stimulant exposure.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling (JAK1/2 already mapped) transduces the neuroinflammatory tone implicated in the reward dysregulation of stimulant use disorder.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA released by stimulant-induced glial and neuronal stress can engage cGAS-STING, contributing to the neuroinflammation of stimulant use disorder.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the interferon-associated microglial activation reported with chronic stimulant exposure.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of the PTEN-PI3K-AKT axis (PTEN and AKT already mapped) regulates the neuronal plasticity and oxidative-stress handling relevant to the reward neuroadaptations of stimulant use disorder.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to chronic stimulant use disorder.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α responses to stimulant-associated vasoconstrictive and metabolic stress contribute to the neurovascular injury of stimulant use disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) mediates the synaptic-plasticity neuroadaptations of the reward circuit in stimulant use disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK metabolic signaling participates in the neuronal energetic and oxidative stress of chronic stimulant exposure in stimulant use disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation in the reward circuit contributes to the persistent neuroadaptations and relapse vulnerability of stimulant use disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal and reward-circuit homeostasis implicated in stimulant use disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the dopamine-transporter regulation and synaptic plasticity of stimulant use disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with stimulant use disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and reward-circuit processes implicated in stimulant use disorder.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven neuroinflammation participates in the glial activation and reward-circuit changes of stimulant use disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory responses implicated in stimulant use disorder.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with stimulant use disorder.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the microglial and neuroinflammatory processes implicated in stimulant use disorder.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the reward-circuit gene programs implicated in stimulant use disorder.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences: estrogen amplifies the dopaminergic response to stimulants, and women show a faster progression to dependence (telescoping) and menstrual-cycle variation in cocaine craving, implicating sex hormones in stimulant use disorder.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Social reward: oxytocin modulates the social bonding and reward circuits disrupted by chronic stimulant use, and is under investigation as a treatment to reduce craving and stress-induced relapse.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Polysubstance overlap: stimulant use disorder increasingly co-occurs with opioid use, and mu-opioid signalling interacts with the dopaminergic reward system (dopamine already mapped), a combination behind rising stimulant-opioid overdose deaths.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response driving the craving and stress-induced relapse of stimulant use disorder.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic dysregulation: chronic stimulant use disturbs appetite, weight and glucose handling, and the resulting insulin and metabolic dysregulation add to the cardiometabolic harm of the disorder.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Neuroinflammatory balance: the anti-inflammatory cytokine IL-10 counters the TLR4-driven TNF and IL-1 (already mapped) that stimulants provoke in glia, part of the neuroinflammation implicated in stimulant neurotoxicity and dependence.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the glial neuroinflammation (IL-6, TNF and IL-1 already mapped) that stimulants provoke modulate the reward and stress circuits, part of the neurotoxicity of stimulant use disorder.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative neurotoxicity: stimulants generate oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species (NLRP3 already mapped) drive the dopaminergic neurotoxicity and cardiovascular injury of the disorder.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cardiometabolic harm: chronic stimulant use disturbs metabolism and, with the sympathetic strain (norepinephrine already mapped) on the vasculature, contributes to the atherogenic dyslipidaemia adding to the cardiovascular harm of the disorder.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the microglial (already mapped) pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the neuroinflammation driving stimulant neurotoxicity.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and dopamine signalling: zinc modulates the dopamine transporter (dopamine already mapped) and NMDA signalling, and disturbed zinc status is linked to the reward and mood dysregulation of stimulant use disorder.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and catecholamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the catecholamine reward and toxicity of stimulant use disorder.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Neuroimmune balance: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation (TLR4, TNF and IL-1 already mapped) of the methamphetamine neurotoxicity of stimulant use disorder.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine and reward: leptin modulates the reward (dopamine already mapped) circuitry and the appetite suppression of the stimulants, part of the metabolic-reward crosstalk of stimulant use disorder.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic-cardiovascular adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic and cardiovascular (cholesterol already mapped) toxicity of stimulant use disorder.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic-cardiovascular (cholesterol already mapped) toxicity of stimulant use disorder.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Dopaminergic neurotoxicity: the methamphetamine damages the dopaminergic (already mapped) and serotonergic neurons (the terminal loss), the neurotoxicity of stimulant use disorder.
- `connects-to` → **[Opioid use disorder](../opioid-use-disorder/README.md)** — Polysubstance comorbidity: the stimulant and opioid use disorders commonly co-occur (the 'speedball', the stimulant-adulterated opioid supply), the shared reward-circuit (dopamine already mapped) vulnerability.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, contributes to the glial (microglia already mapped) neuroinflammation and the dopaminergic neurotoxicity of stimulant use disorder.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune-inflammatory dimension (TNF and IL-1 already mapped) of chronic stimulant use.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of stimulant use disorder.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of chronic stimulant use.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of stimulant use disorder.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of stimulant use disorder.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the blood-brain-barrier disruption implicated in stimulant use disorder.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic stimulant exposure of stimulant use disorder.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Stimulant-modulated NK: the NK-cell number and cytotoxicity, altered by the chronic stimulant exposure and the stress reactivity, are part of the peripheral immune dysregulation of stimulant use disorder.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the complement activation of the neuroinflammation implicated in stimulant use disorder.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) neuroinflammation of the reward-circuit dimension of stimulant use disorder.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the neuroinflammation of stimulant use disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-neuroimmune axis: TSLP, from barrier epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the neuroinflammatory dimension of stimulant use disorder.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-neuroinflammation axis: bradykinin, via B1/B2 receptors on microglia (already mapped) and endothelium, amplifies the blood-brain-barrier disruption and the neuroinflammation of stimulant use disorder.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective cytokine: erythropoietin, via the EPOR on neurons and microglia (already mapped), reduces oxidative stress and apoptosis in the neuroinflammatory dimension of stimulant use disorder.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-reward axis: histamine, from tuberomammillary-nucleus (brain already mapped) neurons and mast cells (already mapped), modulates the dopaminergic (dopamine already mapped) reward circuitry and the sleep-wake dysregulation of stimulant use disorder.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-reward axis: stimulant use profoundly disrupts the circadian rhythm and melatonin secretion; melatonin dysregulation perpetuates the insomnia-sleep fragmentation (already mapped) and the dopaminergic (dopamine already mapped) reward-clock coupling of stimulant use disorder.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement-contact brake: C1-esterase inhibitor regulates the classical-complement and contact-system (bradykinin already mapped) activation contributing to the neuroinflammation and the microglial (already mapped) TLR4-driven neuroinflammation of stimulant use disorder.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — SUD testosterone: testosterone, via androgen receptors on neurons (already mapped) and microglia (already mapped), modulates dopaminergic reward; testosterone deficiency amplifies the CRH (already mapped) and norepinephrine (already mapped) cascade of stimulant use disorder.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — SUD prolactin: prolactin, via PRLR on neurons (already mapped) and microglia (already mapped), modulates dopaminergic reward; hyperprolactinaemia amplifies the CRH (already mapped) and norepinephrine (already mapped) cascade of stimulant use disorder.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — SUD vasopressin: vasopressin, via V1aR on neurons (already mapped) and microglia (already mapped), modulates HPA-axis (CRH already mapped) tone; vasopressin dysregulation amplifies norepinephrine (already mapped) and NLRP3 (already mapped) cascade of stimulant use disorder.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Dopaminergic ROS scavenger: selenium, as GPx in neurons (already mapped) and microglia (already mapped), scavenges dopaminergic (dopamine already mapped) neuroinflammatory ROS; selenium deficiency amplifies the CRH (already mapped) and NLRP3 (already mapped) cascade of stimulant use disorder.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-reward axis: iodine-dependent thyroid hormones modulate dopaminergic (dopamine already mapped) and serotonergic (serotonin already mapped) tone; iodine deficiency impairs thyroid-mediated regulation of the CRH (already mapped) stress axis of stimulant use disorder.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Synaptic energy substrate: phosphorus, as ATP in neurons (already mapped) and synapses (already mapped), sustains dopaminergic (dopamine already mapped) vesicle release; phosphorus deficiency amplifies the NLRP3 (already mapped) neuroinflammation of stimulant use disorder.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — SUD iron: iron supports neuron (already mapped) dopamine (already mapped) and serotonin (already mapped) synthesis; iron deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and BDNF (already mapped) dysregulation in stimulant use disorder.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — SUD calcium: calcium gates neuron (already mapped) dopamine (already mapped) release via vesicular exocytosis; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and BDNF (already mapped) suppression in stimulant use disorder.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — SUD chloride: chloride, via KCC2 in GABAergic neurons (already mapped), sets inhibitory tone; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and serotonin (already mapped) signalling deficits in stimulant use disorder.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — SUD sulfur: hydrogen sulfide from neurons (already mapped) modulates dopamine (already mapped) signalling; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) suppression in stimulant use disorder.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — SUD carbon: carbon, as metabolic backbone of dopamine (already mapped) and BDNF (already mapped) in neurons (already mapped), drives synaptic energy metabolism; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of stimulant use disorder.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — SUD hydrogen: hydrogen, via redox homeostasis in neurons (already mapped) and macrophages (already mapped), modulates dopamine (already mapped) oxidative stress; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of stimulant use disorder.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — SUD nitrogen: nitric oxide from neurons (already mapped) modulates dopamine (already mapped) signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and serotonin (already mapped) cascade of stimulant use disorder.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — SUD oxygen: reactive oxygen species in neurons (already mapped) and macrophages (already mapped) drive oxidative neuronal damage; oxygen imbalance amplifies dopamine (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of stimulant use disorder.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — SUD PD-1: PD-1 checkpoint signalling in T-cells (already mapped) and microglia (already mapped) modulates neuroinflammatory tone; PD-1 dysregulation amplifies dopamine (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of stimulant use disorder.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — SUD angiotensin-II: angiotensin-II signalling in neurons (already mapped) and macrophages (already mapped) promotes inflammation; angiotensin-II excess amplifies dopamine (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of stimulant use disorder.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — SUD wnt-beta-catenin: WNT/β-catenin on neurons (already mapped) and astrocytes (already mapped) regulates reward circuit plasticity; wnt-beta-catenin loss amplifies NF-κB (already mapped) and Dopamine (already mapped) and CRH (already mapped) cascade of SUD.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — SUD rankl: RANKL from macrophages (already mapped) and astrocytes (already mapped) promotes neuroinflammatory immune activation; rankl excess amplifies NF-κB (already mapped) and Dopamine (already mapped) and CRH (already mapped) cascade of SUD.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — SUD smad4: SMAD4 in neurons (already mapped) and astrocytes (already mapped) transduces TGF-β signals; smad4 loss amplifies NF-κB (already mapped) and Dopamine (already mapped) and CRH (already mapped) cascade of SUD.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — SUD il-2: IL-2 from T-cells (already mapped) and microglia (already mapped) regulates neuroinflammatory surveillance in stimulant circuits; il-2 dysregulation amplifies NF-κB (already mapped) and Dopamine (already mapped) and CRH (already mapped) cascade of SUD.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — SUD vegf: VEGF from macrophages (already mapped) and astrocytes (already mapped) drives neuroinflammatory angiogenesis in stimulant use disorder; vegf dysregulation amplifies NF-κB (already mapped) and Dopamine (already mapped) and CRH (already mapped) cascade of SUD.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — SUD fibronectin: fibronectin in neurons (already mapped) and astrocytes (already mapped) promotes CNS ECM remodelling in stimulant circuits; fibronectin excess amplifies NF-κB (already mapped) and Dopamine (already mapped) and CRH (already mapped) cascade of SUD.

## Treatment

### Evidence-Based Interventions

**No FDA-approved pharmacotherapy exists** for cocaine or methamphetamine use disorder (2024). This is in contrast to opioid (buprenorphine, methadone, naltrexone) and alcohol (naltrexone, acamprosate, disulfiram) use disorders.

| Intervention | Evidence | Mechanism |
|:---|:---|:---|
| **Contingency management (CM)** | Strongest evidence (meta-analysis: large ES) | Voucher/prize for drug-negative urine → positive reinforcement competes with drug reward |
| **CBT for SUD** | Moderate evidence; best for relapse prevention | Identifies triggers; coping skills; craving management |
| **Motivational interviewing** | Moderate evidence; best for engagement | Ambivalence resolution; builds intrinsic motivation |
| **Bupropion** | Modest evidence for meth (not cocaine) | DAT/NET inhibitor; may partially replace meth reward and reduce craving |
| **Modafinil** | Modest evidence for cocaine (inconsistent) | Non-stimulant DA/NE modulator; reduces cocaine subjective effects |
| **N-acetylcysteine** | Emerging evidence | Restores system Xc glutamate homeostasis → reduces cue-induced craving |
| **Naltrexone** | Weak evidence for cocaine | Opioid component of cocaine reinforcement |
| **Topiramate** | Modest evidence for cocaine | GABA-A agonist/AMPA antagonist; reduces craving |
| **Disulfiram** | Some evidence for cocaine | May inhibit DA-β-hydroxylase → ↑ DA → aversive cocaine reactions |

**Contingency management (CM)** is the most evidence-based non-pharmacological intervention: drug-negative urine screens earn escalating vouchers redeemable for goods/services. Meta-analyses show the largest effect sizes of any SUD treatment for cocaine (~d = 0.58). The PACT Act (2023) removed regulatory barriers to implementing CM in federally-funded clinics in the US.

### Harm Reduction

- Fentanyl test strips: critical due to stimulant supplies contaminated with fentanyl (many meth and cocaine overdose deaths involve polysubstance involvement with fentanyl)
- Naloxone distribution for stimulant users at risk of opioid co-exposure
- HIV prevention: PrEP for meth users engaging in high-risk sexual behavior; needle programs for IV users
- Wound care (skin-popping in meth users): serious wound infections, necrotizing fasciitis
- Cardiovascular monitoring: ECG, cardiac biomarkers if chest pain

[^volkow-2007-cocaine-dopamine]: Volkow ND, Wang GJ, Fowler JS, Telang F. Overlapping neuronal circuits in addiction and obesity: evidence of systems pathology. *Philos Trans R Soc Lond B Biol Sci.* 2008;363(1507):3191-200. [doi:10.1098/rstb.2008.0107](https://doi.org/10.1098/rstb.2008.0107) · [PubMed 18640918](https://pubmed.ncbi.nlm.nih.gov/18640918/)
[^robinson-berridge-2003-incentive-salience]: Robinson TE, Berridge KC. Addiction. *Annu Rev Psychol.* 2003;54:25-53. [doi:10.1146/annurev.psych.54.101601.145237](https://doi.org/10.1146/annurev.psych.54.101601.145237) · [PubMed 12185211](https://pubmed.ncbi.nlm.nih.gov/12185211/)
[^pettinati-2011-contingency-management]: Prendergast M, Podus D, Finney J, Greenwell L, Roll J. Contingency management for treatment of substance use disorders: a meta-analysis. *Addiction.* 2006;101(11):1546-60. [doi:10.1111/j.1360-0443.2006.01581.x](https://doi.org/10.1111/j.1360-0443.2006.01581.x) · [PubMed 17034434](https://pubmed.ncbi.nlm.nih.gov/17034434/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
