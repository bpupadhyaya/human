---
schema: human-scale-entry/v1
id: parkinsons-disease
name: Parkinson's Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Neurodegenerative disease from dopaminergic neuron loss in the substantia nigra; alpha-synuclein Lewy bodies are the pathological hallmark. Cardinal features: bradykinesia, rigidity, resting tremor. Levodopa/carbidopa is mainstay therapy; no disease-modifying therapy approved."
aliases: ["PD", "Parkinson disease", "paralysis agitans", "idiopathic Parkinson's"]
sources:
  - id: kalia-2015-pd-review
    type: peer-reviewed
    cite: "Kalia LV, Lang AE. Parkinson's disease. Lancet. 2015;386(9996):896-912."
    doi: "10.1016/S0140-6736(14)61393-3"
    pmid: "25904081"
    url: "https://doi.org/10.1016/S0140-6736(14)61393-3"
  - id: spillantini-1997-lewy-body
    type: peer-reviewed
    cite: "Spillantini MG, Schmidt ML, Lee VM, Trojanowski JQ, Jakes R, Goedert M. Alpha-synuclein in Lewy bodies. Nature. 1997;388(6645):839-840."
    doi: "10.1038/42166"
    pmid: "9278044"
    url: "https://doi.org/10.1038/42166"
  - id: olanow-2009-pd-treatment
    type: peer-reviewed
    cite: "Olanow CW, Stern MB, Sethi K. The scientific and clinical basis for the treatment of Parkinson disease. Neurology. 2009;72(21 Suppl 4):S1-136."
    doi: "10.1212/WNL.0b013e3181a1d44c"
    pmid: "19470958"
    url: "https://doi.org/10.1212/WNL.0b013e3181a1d44c"
cross_links:
  - target: 01-human/06-organ/brain
    relation: targets
    note: "PD destroys dopaminergic neurons in the substantia nigra pars compacta → depletes striatal dopamine → disrupts basal ganglia circuitry; Lewy bodies spread via Braak staging from brainstem to limbic and neocortex."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Alpha-synuclein aggregates activate microglia via TLR2/4 and NLRP3 inflammasome → IL-1β and TNF-alpha → dopaminergic neuron death; neuroinflammation amplifies degeneration and correlates with disease progression."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Alpha-synuclein is degraded by autophagy (macroautophagy and CMA); mutant SNCA and LRRK2 impair autophagy flux → aggregate accumulation; TFEB activation and rapamycin reduce synuclein pathology in preclinical models."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Both are age-related neurodegenerative diseases with prion-like protein aggregation (tau/Abeta in AD; alpha-synuclein in PD); Lewy body dementia overlaps both; shared pathomechanisms include mitochondrial dysfunction, autophagy failure, and neuroinflammation."
  - target: 01-human/03-molecular/snca
    relation: connects-to
    note: "SNCA missense mutations (A53T, A30P, E46K) and gene duplication/triplication cause familial PD; misfolded alpha-synuclein fibrils are the main component of Lewy bodies; SNCA propagates via synaptic connections following Braak staging from brainstem to neocortex."
  - target: 01-human/03-molecular/lrrk2
    relation: connects-to
    note: "LRRK2 G2019S (~1-2% of sporadic PD, ~40% penetrance by age 80) is the most common pathogenic variant causing familial PD; LRRK2 kinase hyperactivation → Rab GTPase hyperphosphorylation → vesicle trafficking defects and α-synuclein aggregation in dopaminergic neurons."
  - target: 01-human/03-molecular/mapt
    relation: connects-to
    note: "MAPT H1 haplotype (common in Europeans) is a risk factor for PD and PSP; tau co-aggregates with alpha-synuclein in Lewy body dementia and some PD brains; MAPT LOF mutations cause FTLD-MAPT; tau and SNCA pathology converge on mitochondrial dysfunction and autophagy impairment."
  - target: 01-human/07-system/lewy-body-dementia
    relation: connects-to
    note: "DLB and PD are both alpha-synuclein synucleinopathies: the 1-year rule distinguishes DLB (dementia onset ≤1 year of parkinsonism) from PDD (parkinsonism >1 year before dementia); DLB features early cortical Lewy bodies while PD follows Braak brainstem→cortex staging."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Parkinson's is defined by dopamine loss: degeneration of substantia nigra pars compacta neurons depletes striatal dopamine → bradykinesia, rigidity and tremor once ~60-80% is gone; levodopa, dopamine agonists and MAO-B/COMT inhibitors restore dopaminergic tone."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Parkinson's is a neurodegeneration of specific neurons: α-synuclein-laden Lewy bodies accumulate in dopaminergic substantia nigra neurons, driving mitochondrial and autophagy failure and selective death; the vulnerability of these pacemaking neurons explains the motor syndrome."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pain is a common, underrecognized non-motor feature of Parkinson's: beyond musculoskeletal and dystonic pain, central pain arises from altered nociceptive processing in dopaminergic pathways; some PD pain fluctuates with 'off' periods and eases with dopaminergic therapy."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression is one of the commonest non-motor features of Parkinson's, often preceding motor symptoms: degeneration of dopaminergic, serotonergic, and noradrenergic systems—not just illness burden—drives it, so PD depression is intrinsic to the neurodegeneration."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Parkinson's may begin in the gut: α-synuclein pathology appears in the enteric nervous system years before the brain (preceded by constipation), and an altered gut microbiome is implicated, supporting Braak's hypothesis that disease ascends the vagus from gut to brainstem."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "Parkinson's and Huntington's are movement disorders at opposite poles: PD is hypokinetic from dopamine loss, causing bradykinesia and rigidity, while Huntington's is hyperkinetic from striatal degeneration, causing chorea—mirror images of basal-ganglia dysfunction."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Parkinson's disease and schizophrenia are dopamine opposites: PD comes from too little striatal dopamine, while psychosis involves too much dopamine signaling—so antipsychotics cause parkinsonism and PD drugs can cause psychosis."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Parkinson's disease and narcolepsy both disrupt sleep-wake regulation: PD patients commonly have REM-sleep behavior disorder years before motor symptoms, plus excessive daytime sleepiness, reflecting degeneration of brainstem sleep nuclei—an early PD warning sign."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes participate in Parkinson's neurodegeneration: reactive astrocytes can clear or spread α-synuclein, lose support of dopaminergic neurons, and amplify neuroinflammation with microglia—so glia, not just dying neurons, shape progression."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Parkinson's is not just a dopamine disease: degeneration of noradrenergic locus coeruleus neurons depletes norepinephrine, driving the autonomic failure, orthostatic hypotension and cognitive and mood symptoms that levodopa cannot fix."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin neurons degenerate in Parkinson's too: their loss contributes to the depression, anxiety and sleep disturbance that often precede motor signs, and serotonergic terminals also aberrantly process levodopa, contributing to dyskinesias."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Parkinson's is a disorder of the whole nervous system: though defined by nigral dopamine loss and tremor, alpha-synuclein pathology spreads from gut and brainstem to cortex, explaining the autonomic, sleep, sensory and cognitive features beyond movement."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Parkinson's is a dopamine-acetylcholine imbalance: as dopamine falls, relatively unopposed cholinergic activity in the striatum worsens tremor, so anticholinergic drugs help—while loss of cholinergic neurons elsewhere contributes to the dementia of advanced disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron accumulates in the Parkinson's brain: the substantia nigra loads with iron that can catalyze oxidative damage and ferroptosis of dopamine neurons, so brain iron is both a disease marker on MRI and a candidate target for protective therapy."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Parkinson's often begins in the gut: constipation can precede tremor by years, and misfolded alpha-synuclein appears in enteric nerves early—fuelling the 'gut-first' hypothesis that the disease may ascend the vagus nerve from gut to brain."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Parkinson's disrupts the basal ganglia's glutamate balance: losing dopamine lets the subthalamic nucleus fire excess glutamate onto output nuclei, driving the movement slowing—so the NMDA-blocker amantadine and deep-brain stimulation of this glutamatergic hub help."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Parkinson's has an autoimmune flavor: T-helper cells that recognize alpha-synuclein peptides infiltrate the brain and may accelerate dopaminergic neuron loss, linking the adaptive immune system to a classic neurodegenerative disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Parkinson's denervates the heart early: loss of sympathetic nerves to the heart (seen on MIBG imaging) is a characteristic, early sign reflecting that alpha-synuclein pathology spreads through the autonomic nervous system beyond the brain."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Parkinson's dopamine neurons are vulnerable because of calcium: the substantia nigra cells are autonomous pacemakers that fire using calcium channels, and that constant calcium load stresses mitochondria—why calcium-channel blockers are tested to protect them."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Parkinson's is partly an energy failure: mitochondrial complex-I defects and failed mitophagy starve dopamine neurons of ATP, and the toxin MPTP that causes parkinsonism works exactly by poisoning this energy supply."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Parkinson's has an autoimmune streak involving regulatory T cells: T cells that recognize alpha-synuclein appear in patients, and a shortage of restraining Tregs may let this immune attack add to the neurodegeneration."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Parkinson's may begin at the synapse: alpha-synuclein normally works at presynaptic terminals, and its misfolding cripples dopamine release and synaptic function long before neurons die—so the disease is in part a failure of synapses, not just cells."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Parkinson's may start in the gut: alpha-synuclein clumps appear in the large intestine's nerves years early, constipation is among the first symptoms, and the pathology may climb the vagus nerve from bowel to brain."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Parkinson's smolders with TNF-α: activated microglia pour out this cytokine in the affected brain, and the chronic neuroinflammation it drives is thought to accelerate the loss of dopamine neurons."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Parkinson's can be imaged: a DaTscan uses radioactive photons to show the depleted dopamine terminals in the striatum, separating true Parkinson's from tremor that merely mimics it."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Parkinson's leaves traces in the skin: alpha-synuclein deposits can be found in skin nerve biopsies as an emerging diagnostic test, and seborrheic dermatitis is a common early sign."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Where alpha-synuclein lodges decides the disease: when it accumulates in oligodendrocytes rather than neurons, the result is multiple system atrophy, a faster Parkinson-plus disorder."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals Parkinson's defining lesion: the Lewy body, a dense core of tangled alpha-synuclein filaments inside the dying dopamine neuron, surrounded by the swollen, failing mitochondria that mark its energy crisis."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Parkinson's shows in the eyes: blinking slows to a stare, eye movements grow jerky, and dopamine loss thins the retina — a change now studied as an early imaging biomarker of the disease in the brain."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper handling falters in the Parkinson's brain: the metal normally helps antioxidant defenses, and its disturbed balance in the substantia nigra adds to the oxidative stress, alongside iron, that kills the dopamine neurons."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Parkinson's slows the stomach: gastroparesis delays emptying so erratically that levodopa absorption becomes unpredictable, causing the on-off motor swings, while the delayed transit is part of the gut dysfunction that may even precede the tremor."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Sleep breaks down early in Parkinson's: REM sleep behavior disorder — acting out dreams — is a striking prodrome that can precede the disease by years, and disrupted melatonin and circadian rhythm worsen the fragmented nights."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Autonomic failure reaches the body's smooth muscle: the disease's loss of autonomic control slows gut and bladder smooth muscle into constipation and urinary trouble, and weakens vascular tone into the orthostatic hypotension that causes falls."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Clearing the rogue protein is the new hope: monoclonal antibodies against aggregated alpha-synuclein are in trials to slow Parkinson's, aiming to mop up the misfolded protein before it spreads neuron to neuron."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Parkinson's is a disease of basal-ganglia GABA circuits: losing dopamine unbalances the GABAergic direct and indirect pathways, over-inhibiting movement — and that same GABA output is what deep-brain stimulation and pallidotomy retune."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Dopamine treatment can unleash compulsions: dopamine-agonist drugs trigger impulse-control disorders including hypersexuality, while autonomic disease causes erectile and sexual dysfunction — and estrogen's neuroprotection may explain why men are affected more."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Parkinson's and melanoma travel together: people with one carry a higher risk of the other, a bidirectional link rooted in shared pigment and α-synuclein biology rather than in levodopa, prompting skin surveillance in patients."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Parkinson's reaches beyond the brain into peripheral nerves: α-synuclein deposits in autonomic fibers of the skin and gut — now sampled by biopsy to diagnose it — and the resulting autonomic neuropathy causes orthostatic drops in blood pressure."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "The immune system joins the attack on dopamine neurons: cytotoxic T cells that recognize α-synuclein fragments infiltrate the substantia nigra, an adaptive autoimmune assault that helps drive the neuronal loss of Parkinson's."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Microglia inflame the dying nigra: α-synuclein aggregates activate the NLRP3 inflammasome in microglia to release IL-1β, a self-amplifying neuroinflammation that accelerates dopamine-neuron loss and is a leading drug target in Parkinson's."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Disordered insulin signaling speeds it: type 2 diabetes and brain insulin resistance raise Parkinson's risk and quicken its progression, which is why GLP-1 diabetes drugs are now being trialed to slow the neurodegeneration."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate cells help clear the toxic protein: natural killer cells scavenge α-synuclein aggregates and modulate the neuroinflammation, an innate-immune arm of Parkinson's that complements the cytotoxic T-cell attack."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Microglia inflame the dying neurons through NF-κB: α-synuclein activates NF-κB in microglia, which prime the NLRP3 inflammasome and pour out cytokines that accelerate the loss of dopaminergic neurons."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep falls apart early and often: insomnia, fragmented sleep and REM sleep behavior disorder are cardinal non-motor features of Parkinson's, sometimes preceding the tremor by years as the disease invades sleep-regulating nuclei."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Swallowing fails and the lungs pay: advancing Parkinson's brings dysphagia and aspiration, so aspiration pneumonia and the sepsis it triggers are the leading cause of death in the disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Falls meet fragile bones: postural instability and freezing make falls frequent in Parkinson's, while immobility and low vitamin D thin the bones, so osteoporotic hip and wrist fractures are a major source of disability."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety is a core non-motor feature: persistent worry and 'off'-period anxiety are common in Parkinson's, arising from the same degeneration of dopaminergic, noradrenergic and serotonergic systems that drives the motor disease."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Renal function shapes its treatment and risk: chronic kidney disease shares vascular and oxidative mechanisms epidemiologically linked to Parkinson's, and impaired clearance alters dosing of the drugs used to manage it."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Its dysphagia lets food reach the lungs: impaired swallowing in Parkinson's causes silent aspiration, and the resulting aspiration pneumonia — often pneumococcal — is the leading cause of death in advanced disease."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Progressive immobility clots the veins: the bradykinesia, rigidity and falls of advanced Parkinson's reduce mobility, and the resulting venous stasis raises the risk of deep vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "It shares the vascular terrain: Parkinson's overlaps with cerebrovascular disease through vascular parkinsonism, and the reduced mobility and autonomic dysfunction of advanced disease compound stroke risk."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Its dopamine drugs unleash compulsions: dopamine-agonist therapy for Parkinson's classically triggers impulse-control disorders — pathological gambling, hypersexuality and compulsive shopping — that resolve when the drug is reduced."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Rigidity and falls batter the skeleton: the bradykinesia, postural instability and stooped camptocormic posture of Parkinson's cause frequent falls and fractures, contractures and chronic musculoskeletal pain."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Autonomic failure unsettles the bladder: Parkinson's disrupts autonomic control of the bladder, causing urinary urgency, frequency and nocturia, with retention and recurrent infection in advanced disease."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Autonomic failure drops the blood pressure: Parkinson's causes orthostatic hypotension — a major non-motor feature worsened by levodopa — leading to dizziness, syncope and falls on standing."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It shows on the skin: seborrhoeic dermatitis with a greasy, scaly face and excess sweating are classic dermatological features of Parkinson's, reflecting its autonomic and sebaceous dysregulation."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Swallowing failure floods the lungs: dysphagia leads to aspiration pneumonia — a leading cause of death in Parkinson's — while rigidity of the chest wall restricts breathing."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Brain inflammation drives it: microglial neuroinflammation and the immune-regulating LRRK2 gene implicate the immune system in the onset and progression of Parkinson's disease."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Failing waste clearance lets protein build up: impaired glymphatic and meningeal-lymphatic clearance of alpha-synuclein is increasingly implicated in the neurodegeneration of Parkinson's."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is tied to metabolism: Parkinson's causes unexplained weight loss and is bidirectionally linked with type 2 diabetes, sharing mitochondrial and insulin-signalling pathways."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "A gut bug that blocks the drug: Helicobacter pylori infection impairs levodopa absorption and is epidemiologically linked to Parkinson's, so eradication can improve motor control."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: connects-to
    note: "A historical post-infectious link: the encephalitis lethargica that followed the 1918 influenza pandemic caused a striking post-encephalitic parkinsonism, fuelling interest in infectious triggers."
  - target: 03-medicine/02-traditional/ginkgo-biloba
    relation: connects-to
    note: "Traditional neuroprotectants are explored: antioxidant herbs such as ginkgo biloba are studied for neurodegeneration, though none substitute for dopaminergic therapy in Parkinson's."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Aggregates clog the axon: α-synuclein oligomers impair axonal transport in nigrostriatal neurons, contributing to the dying-back degeneration that strips dopamine terminals from the striatum before cell bodies die."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It denervates the heart: Parkinson's causes cardiac sympathetic denervation, so reduced MIBG uptake in the myocardium is an early biomarker distinguishing it from atypical parkinsonism, and contributes to orthostatic hypotension."
  - target: 03-medicine/02-traditional/panax-ginseng
    relation: connects-to
    note: "Ginsenosides are studied for neuroprotection: Panax ginseng shows dopaminergic-neuron-protective effects in Parkinson's models, joining ginkgo among traditional remedies explored as adjuncts, though none replace levodopa."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "It may begin in the gut: α-synuclein pathology can start in the enteric nervous system of the intestinal wall and ascend the vagus to the brain (Braak's gut-first hypothesis), and constipation precedes the tremor by years."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Dementia comes with time: most people with Parkinson's eventually develop cognitive decline as α-synuclein and Lewy pathology spread to the hippocampus and cortex, blurring the line with Lewy body dementia."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Infections can trigger parkinsonism: as influenza once left post-encephalitic parkinsonism, viral infections including COVID-19 are reported to precipitate or unmask Parkinson's, supporting a role for neuroinflammation in its onset."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Vascular parkinsonism: small-vessel disease of the brain's arterial walls can mimic Parkinson's with a lower-body, gait-predominant parkinsonism that responds poorly to levodopa, a key differential."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "Neurodegeneration's shared themes: Parkinson's and ALS are both age-related neurodegenerations driven by protein misfolding and aggregation, with rare overlap syndromes and the Guam ALS-parkinsonism-dementia complex linking them."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "A shared dopamine thread: bipolar disorder is associated with a higher later risk of Parkinson's disease, and the dopaminergic dysregulation of mania mirrors, in reverse, the dopamine loss of Parkinson's."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Aspiration ends it: dysphagia in advanced Parkinson's leads to aspiration pneumonia, seeding the alveoli with oral flora—the leading cause of death in the disease."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "Drug-induced valve disease: ergot-derived dopamine agonists (pergolide, cabergoline) stimulate 5-HT2B receptors to fibrose the heart valves and endocardium, the reason these agonists are now largely avoided."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Pain in Parkinson's: chronic pain is a common non-motor symptom of Parkinson's with central-sensitisation features that overlap fibromyalgia, beyond the rigidity and dystonia of the motor disease."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neuroinflammation: IL-1β released by activated microglia around degenerating dopaminergic neurons amplifies the inflammatory cascade that drives nigral cell loss in Parkinson's."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory marker: elevated IL-6 in CSF and blood tracks neuroinflammation and disease progression in Parkinson's, part of the cytokine milieu fuelling neurodegeneration."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Impaired clearance: mTOR overactivity suppresses the autophagy/mitophagy needed to clear α-synuclein and damaged mitochondria, and its inhibition is neuroprotective in Parkinson's models."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Microglial recruitment: CCL2 released in the inflamed substantia nigra draws monocytes and amplifies the microglial activation that contributes to dopaminergic neurodegeneration in Parkinson's."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Adaptive autoimmunity: IFN-γ from T cells recognising α-synuclein epitopes infiltrates the Parkinson's brain, evidence that an adaptive immune attack on dopaminergic neurons contributes to the disease."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Neuroprotective repurposing: GLP-1 receptor agonists developed for diabetes show neuroprotective signals in Parkinson's trials, reflecting a metabolic-neurodegeneration link and brain insulin signalling."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "α-Synuclein sensing: aggregated α-synuclein released from dying neurons activates microglial TLR4, triggering the chronic neuroinflammation that propagates dopaminergic neurodegeneration in Parkinson's disease."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Nigral iron and ferroptosis: iron accumulates in the substantia nigra of Parkinson's disease, and dysregulated ferroportin-controlled iron export sensitises dopaminergic neurons to ferroptotic, oxidative cell death."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Mitochondrial-DNA sensing: failed PINK1/Parkin mitophagy lets damaged mitochondria leak DNA that activates cGAS-STING, driving the type-I-interferon neuroinflammation now implicated in Parkinson's neurodegeneration."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Pacemaking calcium stress: substantia-nigra dopaminergic neurons use L-type Cav1.3 calcium channels for autonomous pacemaking, and the resulting chronic calcium load stresses mitochondria — a selective vulnerability that motivated the isradipine trials in Parkinson's."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Urate and oxidative stress: xanthine oxidase produces urate, and higher urate levels are associated with lower Parkinson's risk and slower progression, suggesting that antioxidant urate partly offsets the oxidative stress damaging dopaminergic neurons."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Lost trophic support: BDNF normally sustains the survival of substantia-nigra dopaminergic neurons, and its reduction in Parkinson's removes a key neurotrophic support, contributing to the progressive degeneration of the nigrostriatal pathway."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative defence: substantia-nigra dopaminergic neurons face intense oxidative stress, and the NRF2 antioxidant response is a key defence whose decline permits the oxidative and mitochondrial damage driving Parkinson's neurodegeneration."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Neuronal apoptosis: caspase-3-mediated apoptosis executes the loss of nigral dopaminergic neurons in Parkinson's, downstream of the mitochondrial dysfunction and α-synuclein toxicity already mapped."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement neuroinflammation: microglial complement C3 tags synapses and neurons for elimination in Parkinson's, an arm of the neuroinflammation (with the NLRP3 inflammasome already mapped) that propagates neurodegeneration."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "Mitophagy and energy: AMPK senses the bioenergetic failure of Parkinson's (ATP mapped) and, opposing mTOR (mapped), promotes the autophagy/mitophagy (autophagy mapped) that clears the damaged mitochondria central to dopaminergic neuron death."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Tau and apoptosis: GSK-3β phosphorylates tau (MAPT mapped) and promotes neuronal apoptosis, a convergence node linking the genetic and degenerative threads of Parkinson's disease."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "α-synuclein-driven microglia: TLR4 (mapped) sensing of aggregated α-synuclein (SNCA mapped) signals through MyD88 to activate microglia, driving the neuroinflammation that propagates Parkinson's neurodegeneration."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling (GSK-3β and mTOR mapped) maintains dopaminergic-neuron survival, and its failure promotes the apoptotic loss characteristic of Parkinson's disease."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IFN-γ/cytokine-driven JAK-STAT signalling (IFN-γ mapped) sustains the reactive microgliosis that propagates dopaminergic neuroinflammation in Parkinson's disease."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 is induced by α-synuclein (SNCA mapped) and amplifies the neuroinflammatory response driving dopaminergic neurodegeneration."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling drives the interferon-responsive microglial activation that contributes to the neuroinflammation of Parkinson's disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK-STAT3 signalling (JAK1/2 already mapped) in microglia and astrocytes sustains the reactive gliosis accompanying dopaminergic neurodegeneration in Parkinson's disease."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN, the phosphatase that restrains PI3K-AKT survival signalling (and the namesake of PINK1's pathway), modulates the mitochondrial quality control and neuronal survival relevant to Parkinson's disease."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the autophagy and oxidative-stress defense of dopaminergic neurons, programs that fail in Parkinson's disease."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation contributing to dopaminergic degeneration in Parkinson's disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling participates in dopaminergic neuron stress and in the L-DOPA-induced dyskinesia associated with Parkinson's disease therapy."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α couples the mitochondrial dysfunction and oxidative stress of dopaminergic neurons to metabolic adaptation in Parkinson's disease."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the neuronal survival pathways whose failure contributes to dopaminergic degeneration in Parkinson's disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic CD8 T cells infiltrate the substantia nigra and contribute to the neurodegeneration of Parkinson's disease."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation, including SNCA regulation, implicated in Parkinson's disease."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the microglial activation and neuroinflammation of Parkinson's disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte and microglial recruitment amplifies the neuroinflammation of Parkinson's disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the microglial and immune-cell responses of the neuroinflammation of Parkinson's disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling from infiltrating T cells participates in the neuroinflammation and dopaminergic neurodegeneration of Parkinson's disease."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and astrocyte neuroinflammatory responses of Parkinson's disease."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neuronal and neuroinflammatory gene programs of Parkinson's disease."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the microglial activation and neuronal calcium dysregulation of Parkinson's disease."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (A2A receptor) signaling participates in the basal-ganglia motor circuitry and neuroinflammation of Parkinson's disease."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences: Parkinson's disease is more common in men, and estrogen exerts neuroprotective effects on dopaminergic neurons, contributing to the later onset and milder early course seen in women."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Brain renin-angiotensin: a local renin-angiotensin system in the substantia nigra amplifies microglial oxidative stress and neuroinflammation, and angiotensin-receptor blockade is neuroprotective in models, a target beyond dopamine replacement."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance: brain insulin resistance is common in Parkinson's disease and impairs neuronal energetics and survival, the rationale behind repurposing GLP-1 agonists (already mapped) as disease-modifying candidates."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Adaptive autoimmunity: alpha-synuclein-specific T cells recognised through IL-2-driven expansion are found in Parkinson's disease, implicating an adaptive immune response against the aggregating protein (already mapped) in dopaminergic neuron loss."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid protection: progesterone and its neurosteroid metabolites are neuroprotective, and together with estrogen (already mapped) may contribute to the lower incidence and later onset of Parkinson's disease in women."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Microglial polarisation: IL-4 shifts microglia (already mapped) toward a reparative, anti-inflammatory phenotype, and boosting this arm against the pro-inflammatory TNF/IL-1 response is a neuroprotective strategy explored in Parkinson's disease."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory neuroprotection: IL-10, with IL-4 (already mapped), opposes the microglial pro-inflammatory response (TNF, IL-1 and IL-6 already mapped) driving dopaminergic neuron loss, and boosting this arm is a neuroprotective strategy in Parkinson's disease."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Enteric origin: alpha-synuclein pathology (already mapped) may begin in the enteric nervous system, and the small intestine, like the large intestine (already mapped), is affected early, with altered motility and the prodromal gut symptoms of Parkinson's disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the activated microglia (already mapped) contribute to the neuroinflammation that drives dopaminergic neuron loss, and the cyclooxygenase pathway has been studied as a neuroprotective target in Parkinson's disease."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitrosative stress: nitric oxide from the activated microglia (already mapped) forms peroxynitrite that nitrosylates proteins and adds to the oxidative injury (ferroportin-linked iron already mapped) killing the dopaminergic neurons of Parkinson's disease."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc dyshomeostasis: disturbed zinc handling in the substantia nigra, alongside the iron (already mapped) and copper accumulation, contributes to the metal-catalysed oxidative stress that damages the dopaminergic neurons of Parkinson's disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium neuroprotection: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity on the vulnerable nigral neurons, a proposed neuroprotective factor in Parkinson's disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation (NLRP3, TNF and IL-1 already mapped) that drives the dopaminergic loss of Parkinson's disease."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron regulation: hepcidin governs the iron (already mapped) handling whose dysregulation contributes to the nigral iron accumulation (ferroportin already mapped) and the metal-catalysed oxidative stress of Parkinson's disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine neuroprotection: the adipokine leptin has neurotrophic and neuroprotective actions on the dopaminergic neurons, and the metabolic dysregulation (insulin already mapped) it reflects is linked to Parkinson's-disease risk."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Neuroprotective adipokine: adiponectin, with leptin (already mapped), has neuroprotective and metabolic (insulin already mapped) actions linked to Parkinson's-disease risk and the metabolic milieu."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the neuroinflammation (TNF and IL-6 already mapped) and metabolic milieu of Parkinson's disease."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Mitochondrial-DNA interferon: the cGAS-STING (already mapped) sensing of the mitochondrial DNA from the failing mitophagy (autophagy already mapped) drives the type-I interferon neuroinflammation of Parkinson's disease."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the T-cell-mediated neuroinflammation that accelerates the dopaminergic neuron (already mapped) loss of Parkinson's disease."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 immune arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the peripheral immune dysregulation associated with Parkinson's disease."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 neuroinflammation: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory response implicated in Parkinson's disease."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Anti-α-synuclein humoral arm: the B cells produce the anti-α-synuclein (SNCA already mapped) antibodies of the emerging adaptive-immune contribution to Parkinson's disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell neuroinflammation: the mast cells of the brain and the gut (already mapped) contribute to the neuroinflammation and the gut-brain axis of Parkinson's disease."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the peripheral immune dysregulation of Parkinson's disease."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Nigral iron: transferrin, the iron carrier, is central to the iron accumulation in the substantia nigra that, with the disordered ferroportin and hepcidin (already mapped), drives the oxidative stress and ferroptosis of the dopaminergic neurons of Parkinson's disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells of the CNS-border and peripheral compartments present the alpha-synuclein (already mapped) epitopes to the T cells (already mapped), priming the adaptive autoimmunity implicated in Parkinson's disease."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the microglial (already mapped) neuroinflammation of Parkinson's disease."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the complement-driven microglial neuroinflammation of Parkinson's disease."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the neuroinflammation of Parkinson's disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Border-associated macrophages: the CNS-border and infiltrating macrophages contribute to the clearance of the alpha-synuclein (already mapped) and the neuroinflammation of Parkinson's disease."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuroinflammatory alarmin: TSLP, released from enteric epithelium (gut-microbiome already mapped) and skin (already mapped) during gut dysbiosis, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the gut-to-brain axis of Parkinson's disease."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-oedema axis: bradykinin, generated by the kallikrein-kinin system activated by neuroinflammation, augments blood-brain-barrier permeability and amplifies the microglial (already mapped) and macrophage (already mapped) recruitment of Parkinson's disease."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective cytokine: erythropoietin, acting via EPOR on dopaminergic neurons (already mapped) and astrocytes (already mapped), promotes neuronal survival and limits the oxidative and neuroinflammatory degeneration of Parkinson's disease."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Nigro-striatal mast-cell effector: histamine, released by mast cells in the substantia nigra, promotes dopaminergic neurotoxicity via H1/H4 receptors on microglia (already mapped) and amplifies the neuroinflammatory milieu (TNF-α and IL-1β already mapped) of Parkinson's disease."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM remodelling in the nigro-striatal pathway: periostin, expressed by astrocytes (already mapped) in the substantia nigra under neuroinflammation, modulates the extracellular matrix scaffold and Lewy body (alpha-synuclein already mapped) deposition in Parkinson's disease."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits the classical complement (C3 and C5 already mapped) and bradykinin (already mapped) activation in the inflamed substantia nigra, moderating the complement-driven dopaminergic neurodegeneration of Parkinson's disease."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "PD testosterone: testosterone attenuates SNCA (already mapped) aggregation and microglial (already mapped) neuroinflammation in the substantia nigra; androgen deficiency accelerates the dopaminergic neuron (already mapped) loss of Parkinson's disease."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "PD oxytocin: oxytocin receptors on astrocytes (already mapped) and dopaminergic neurons (already mapped) attenuate SNCA (already mapped) aggregation; oxytocin also modulates the dopamine (already mapped) and serotonin (already mapped) circuits of Parkinson's disease."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "PD vasopressin: vasopressin V1A receptors on dopaminergic neurons (already mapped) modulate striatal activity and dopamine (already mapped) release; vasopressin deficiency amplifies the neuroinflammatory and autonomic (brain already mapped) dysfunction of Parkinson's disease."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "PD prolactin: prolactin modulates dopaminergic (already mapped) neuron survival and microglial (already mapped) neuroinflammation in the substantia nigra; prolactin interacts with SNCA (already mapped) aggregation and the NF-κB (already mapped) cascade of Parkinson's disease."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "PD selenium: selenoprotein P reduces the oxidative stress driving SNCA (already mapped) aggregation and dopaminergic (already mapped) neurodegeneration; selenium deficiency amplifies the NF-κB (already mapped) neuroinflammation and accelerates Parkinson's disease progression."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "PD iodine: iodine-dependent thyroid hormones sustain dopaminergic (already mapped) neuron energy metabolism in the substantia nigra; thyroid-hormone deficiency amplifies the NF-κB (already mapped) cascade and worsens SNCA (already mapped) aggregation in Parkinson's disease."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "PD sodium: excess sodium promotes microglia (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and TNF-α (already mapped) skewing amplifies the neuroinflammatory cascade of Parkinson's disease."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "PD potassium: potassium regulates neuron (already mapped) and microglia (already mapped) membrane excitability; potassium dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade and dopaminergic degeneration of Parkinson's disease."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "PD phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and microglia (already mapped), maintains dopaminergic neuron energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of Parkinson's disease."
---

# Parkinson's Disease

## Overview

**Parkinson's disease (PD)** is the **second most common neurodegenerative disease** after Alzheimer's, affecting approximately **10 million people worldwide** (~1 million in the US). It is defined by the selective loss of **dopaminergic neurons in the substantia nigra pars compacta (SNpc)** and the accumulation of **alpha-synuclein-containing Lewy bodies** in surviving neurons. The clinical hallmarks are the motor triad of **bradykinesia** (required for diagnosis), **muscular rigidity**, and **resting tremor**, with postural instability emerging later [^kalia-2015-pd-review].

PD is primarily a disease of aging (mean onset ~60 years), but **~10–15% of cases are early-onset (<50 years)**, often with a genetic cause. Lifetime risk is ~2% for men, ~1.3% for women. Incidence is increasing globally as populations age.

**Pathological staging (Braak staging of PD):**
- **Stage 1-2 (presymptomatic):** Alpha-synuclein pathology in olfactory bulb and dorsal motor nucleus of vagus nerve (explains anosmia and autonomic dysfunction years before motor symptoms)
- **Stage 3-4 (symptomatic):** SNpc degeneration → dopamine depletion → motor symptoms emerge (when >50-60% of SNpc neurons are lost)
- **Stage 5-6 (advanced):** Spread to limbic cortex and neocortex → dementia (Parkinson's disease dementia, PDD) in ~80% over 20 years

**Genetics:**
- **Familial PD (~10-15%):** Autosomal dominant: *SNCA* (alpha-synuclein, A53T/A30P/E46K triplication) → toxic aggregation; *LRRK2* G2019S (most common genetic PD, ~1-2% sporadic, ~13% Ashkenazi Jewish) → kinase overactivation; autosomal recessive: *PRKN* (Parkin), *PINK1*, *DJ-1* → mitochondrial quality control failure
- **Sporadic PD (>85%):** Complex polygenic; *GBA* variants (glucocerebrosidase, ~5-10% of PD) are the most common genetic risk factor; GWAS identified >90 risk loci

## Structure

### Dopaminergic circuit

**Nigrostriatal pathway:** SNpc dopaminergic axons project to the **striatum (caudate + putamen)** → regulate the basal ganglia motor loop:
- **Direct pathway (D1 receptors):** Striatum → inhibits GPi/SNpr → disinhibits thalamus → facilitates cortical motor activation ("GO")
- **Indirect pathway (D2 receptors):** Striatum → inhibits GPe → releases STN inhibition → activates GPi/SNpr → inhibits thalamus → suppresses cortical activation ("STOP")
- **PD effect:** Dopamine loss → weakened direct pathway, overactive indirect pathway → thalamic suppression → bradykinesia and rigidity; STN becomes hyperactive → target for deep brain stimulation (DBS)

**Other affected pathways:**
- **Mesolimbic/mesocortical (VTA → limbic/frontal cortex):** Dopamine loss → depression, apathy, and cognitive impairment in advanced PD
- **Noradrenergic (locus coeruleus):** Early degeneration → orthostatic hypotension, mood disorders, gait freezing
- **Serotonergic (raphe nuclei):** Depression in ~40% of PD
- **Enteric nervous system:** Alpha-synuclein in myenteric plexus → constipation (often precedes motor symptoms by years; supports "gut-first" PD hypothesis)

### Alpha-synuclein and Lewy body pathology [^spillantini-1997-lewy-body]

**Alpha-synuclein (SNCA, 140 aa):** Presynaptic protein; normally regulates synaptic vesicle trafficking and neurotransmitter release. Intrinsically disordered → forms amphipathic helical structure on membranes.

**Aggregation cascade:**
1. Misfolded alpha-synuclein monomers → soluble oligomers (most neurotoxic, disrupt membranes and mitochondria) → protofibrils → insoluble amyloid fibrils
2. Fibrils compact with ubiquitin, neurofilaments, and chaperones → **Lewy bodies** (spherical, eosinophilic, ~5-25 μm, cytoplasmic inclusions)
3. Lewy bodies spread between connected neurons in a prion-like manner (trans-synaptic transmission of alpha-synuclein seeds → Braak staging)

**Triggers of aggregation:**
- Genetic: SNCA A53T/duplication/triplication → concentration-dependent aggregation
- Environmental: Pesticides (rotenone, paraquat) → mitochondrial complex I inhibition → oxidative stress → synuclein misfolding
- Post-translational: Phospho-Ser129 (90% of aggregated synuclein is phosphorylated); nitrosylation, ubiquitination

**Degradation failure:**
- Normal: Alpha-synuclein cleared by UPS (ubiquitin-proteasome system) and chaperone-mediated autophagy (CMA, via LAMP-2A)
- PD: Mutant/oligomeric synuclein blocks LAMP-2A → impairs CMA → accumulates; LRRK2 G2019S phosphorylates beclin-1 → impairs macroautophagy

## Function

### Clinical presentation [^kalia-2015-pd-review]

**Motor features (cardinal triad):**
- **Bradykinesia (required for diagnosis):** Slowness and decrement in amplitude of repetitive movements (finger tapping, foot stomping); micrographia; masked facies (hypomimia); hypophonia
- **Rigidity:** Lead-pipe or cogwheel (tremor superimposed) resistance throughout range of motion; paratonia; Froment's maneuver (contralateral activation enhances rigidity)
- **Resting tremor (4-6 Hz):** Pill-rolling; suppressed with voluntary movement; worsened by stress; asymmetric onset; may be absent (akinetic-rigid variant)
- **Postural instability:** Pull test → retropulsion; gait freezing (festination); falls are leading cause of morbidity/mortality in advanced PD

**Non-motor features (often precede motor by years):**
- **Prodromal:** Anosmia (~90% at diagnosis), REM sleep behavior disorder (RBD — acts out dreams, high specificity for synucleinopathy), constipation, depression
- **Autonomic:** Orthostatic hypotension (↑ fall risk); urinary urgency/retention; sweating abnormalities; sexual dysfunction; gastroparesis
- **Neuropsychiatric:** Depression (~40%), anxiety (~40%), impulse control disorders (dopamine agonists → gambling, hypersexuality), psychosis (hallucinations with levodopa — treat with clozapine or pimavanserin)
- **Cognitive:** Mild cognitive impairment (MCI) at diagnosis in ~25%; PD dementia in ~80% at 20 years; earlier dementia with Lewy body disease (DLB) if dementia precedes motor features

**Diagnostic criteria (MDS Clinical Criteria, 2015):**
- Definite PD: Parkinsonism (bradykinesia + rigidity and/or tremor) + no exclusion criteria + ≥2 supportive features + no red flags
- Supportive features: Unilateral onset, rest tremor, levodopa response, levodopa-induced dyskinesia, olfactory loss, cardiac sympathetic denervation on MIBG scintigraphy
- Red flags: Falls early, bulbar dysfunction early, autonomic failure preceding motor, limited levodopa response → suggest atypical parkinsonism (MSA, PSP, CBD, DLB)

### Differential diagnosis: atypical parkinsonism

| Feature | PD | MSA | PSP | CBD |
|:---|:---|:---|:---|:---|
| Symmetry | Asymmetric | Symmetric | Symmetric | Asymmetric |
| Tremor | Rest tremor | Rare | Rare | Rare |
| Levodopa response | Excellent | Poor | Poor | Poor |
| Falls | Late | Early | Very early | Moderate |
| Eye movement | Normal | Normal | Vertical gaze palsy | Abnormal |
| Autonomic | Mild-moderate | Severe early | Mild | Mild |

## Pathology

### Diagnosis

**Clinical (gold standard):** MDS criteria; DAT-SPECT (DaTscan) — confirms dopaminergic deficit in striatum; 90% specificity for nigrostriatal degeneration vs. essential tremor.

**Biomarkers (emerging):**
- **CSF/blood alpha-synuclein:** Seed amplification assay (SAA/RT-QuIC) — >90% sensitivity/specificity for PD/DLB vs. healthy controls; FDA breakthrough designation
- **Skin biopsy:** Phospho-synuclein in dermal nerve fibers — non-invasive biomarker
- **GBA activity:** Plasma glucocerebrosidase activity predicts GBA-PD and severity
- **MRI:** Substantia nigra hyperechogenicity (transcranial ultrasound); neuromelanin-sensitive MRI; iron accumulation on SWI in SNpc

### Treatment [^olanow-2009-pd-treatment]

**Dopaminergic replacement:**

*Levodopa/carbidopa (Sinemet) — gold standard:*
- Levodopa: Dopamine precursor; crosses blood-brain barrier; metabolized to dopamine in striatum
- Carbidopa: Peripheral DOPA decarboxylase inhibitor → prevents peripheral conversion → reduces nausea, allows lower levodopa dose
- **Initial motor response:** ~90% improvement in motor symptoms; most effective treatment
- **Motor complications (after 5-10 years):**
  - *Wearing off:* Shortened motor response duration (correlates with shrinking levodopa half-life as PD progresses) → treat with COMT inhibitors (entacapone) or MAO-B inhibitors (rasagiline), or controlled-release formulations
  - *Dyskinesia:* Involuntary choreiform movements at peak dose; treat by reducing levodopa dose, adding amantadine (NMDA antagonist)
  - *ON-OFF fluctuations:* Unpredictable motor response → continuous dopaminergic stimulation via levodopa-carbidopa intestinal gel (LCIG, Duopa) or subcutaneous levodopa (ND0612)

*Dopamine agonists (pramipexole, ropinirole, rotigotine patch):*
- Directly stimulate D2/D3 receptors; longer half-life → fewer motor fluctuations
- First-line for younger patients (<60) to delay levodopa motor complications
- Side effects: Impulse control disorders (gambling, hypersexuality, binge eating) in ~15-20%; daytime somnolence; hallucinations in elderly

*MAO-B inhibitors (selegiline, rasagiline, safinamide):*
- Inhibit monoamine oxidase B → reduce dopamine catabolism; mild symptomatic benefit and possible neuroprotective effect (ADAGIO trial: rasagiline 1 mg/day — modest but persistent benefit)

*COMT inhibitors (entacapone, opicapone, tolcapone):*
- Block catechol-O-methyltransferase → reduce peripheral and central levodopa metabolism → extend levodopa effect and reduce wearing off

**Deep brain stimulation (DBS):**
- Bilateral subthalamic nucleus (STN) or globus pallidus internus (GPi) DBS → reduce motor fluctuations and dyskinesias by ~50-60%
- Indication: Advanced PD with motor complications refractory to medication; requires >4 years levodopa benefit; contraindicated with severe dementia or active psychiatric illness
- **STN DBS** → allows levodopa reduction (reduces dyskinesia); **GPi DBS** → more directly reduces dyskinesia without levodopa reduction; Vim DBS for tremor-predominant PD
- Adaptive DBS (closed-loop): Neural signal-triggered stimulation → individualized and more effective

**Disease-modifying therapies (investigational):**
- **Alpha-synuclein immunotherapy:** Anti-synuclein antibodies (prasinezumab Phase IIb → negative on primary endpoint but signal in fast progressors; cinpanemab — negative)
- **LRRK2 kinase inhibitors (DNL201, BIIB094):** Reduce LRRK2 phosphorylation targets; Phase 2 ongoing in LRRK2-PD; also tested in sporadic PD (LRRK2 is activated in sporadic PD under inflammatory conditions)
- **GBA-targeting:** Ambroxol (chaperone → enhances GBA folding, Phase 2 ongoing); gene therapy (AAV-GBA intrathecal injection)
- **GLP-1 agonists (semaglutide, liraglutide):** Retrospective data: GLP-1 agonist use in T2DM associated with lower PD risk; Phase 2 trials ongoing based on neuroprotective mechanism (AMPK activation, neuroinflammation reduction)
- **Iron chelation:** Deferiprone (Phase 3 FAIR-PARK-II) — negative on primary endpoint; dopaminergic neuron iron overload drives oxidative stress in SNpc

**Symptomatic non-dopaminergic:**
- Rivastigmine (ChEI) for PD dementia
- Pimavanserin (5-HT2A inverse agonist) for PD psychosis — does not worsen motor symptoms
- Clonazepam for REM sleep behavior disorder
- Fludrocortisone/droxidopa for neurogenic orthostatic hypotension
- Exercise: Aerobic exercise (treadmill, cycling) → BDNF upregulation → neuroprotective in animal models; improves gait, balance, cognition in clinical trials (ParkProTreK)

## Connections

- `targets` → **[Brain](../../06-organ/brain/README.md)** — PD selectively destroys dopaminergic neurons in the substantia nigra pars compacta, disrupting basal ganglia motor circuitry; alpha-synuclein Lewy body pathology spreads via Braak staging from brainstem to neocortex.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — alpha-synuclein aggregates activate microglia via TLR2/4 and NLRP3 inflammasome, driving IL-1β-mediated dopaminergic neuron death; chronic neuroinflammation amplifies degeneration throughout disease course.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — alpha-synuclein is cleared by CMA and macroautophagy; LRRK2 and mutant SNCA impair autophagy flux, promoting aggregate accumulation; TFEB activation and rapamycin reduce synuclein pathology in preclinical PD models.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — both are age-related neurodegenerative diseases with prion-like protein spreading (tau/Aβ in AD; alpha-synuclein in PD); shared pathomechanisms include mitochondrial dysfunction, autophagy failure, and neuroinflammation; Lewy body dementia bridges both.
- `connects-to` → **[SNCA](../../03-molecular/snca/README.md)** — SNCA missense mutations (A53T, A30P, E46K) and gene duplication/triplication cause familial PD; misfolded alpha-synuclein fibrils are the main component of Lewy bodies; SNCA propagates via synaptic connections following Braak staging from brainstem to neocortex.
- `connects-to` → **[LRRK2](../../03-molecular/lrrk2/README.md)** — LRRK2 G2019S (~1-2% of sporadic PD, ~40% penetrance by age 80) is the most common pathogenic variant causing familial PD; LRRK2 kinase hyperactivation → Rab GTPase hyperphosphorylation → vesicle trafficking defects and α-synuclein aggregation in dopaminergic neurons.
- `connects-to` → **[MAPT](../../03-molecular/mapt/README.md)** — MAPT H1 haplotype (common in Europeans) is a risk factor for PD and PSP; tau co-aggregates with alpha-synuclein in Lewy body dementia and some PD brains; MAPT LOF mutations cause FTLD-MAPT; tau and SNCA pathology converge on mitochondrial dysfunction and autophagy impairment.
- `connects-to` → **[Lewy Body Dementia](../lewy-body-dementia/README.md)** — DLB and PD are both alpha-synuclein synucleinopathies distinguished by the 1-year rule; DLB features early cortical Lewy bodies while PD follows Braak brainstem→cortex staging; PDD (Parkinson's disease dementia) occurs in ~80% of PD at 20 years and shares DLB's cholinergic deficit and rivastigmine responsiveness.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Parkinson's is defined by dopamine loss: degeneration of substantia nigra pars compacta neurons depletes striatal dopamine → bradykinesia, rigidity and tremor once ~60-80% is gone; levodopa, dopamine agonists and MAO-B/COMT inhibitors restore dopaminergic tone.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Parkinson's is a neurodegeneration of specific neurons: α-synuclein-laden Lewy bodies accumulate in dopaminergic substantia nigra neurons, driving mitochondrial and autophagy failure and selective death; the vulnerability of these pacemaking neurons explains the motor syndrome.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pain is a common, underrecognized non-motor feature of Parkinson's: beyond musculoskeletal and dystonic pain, central pain arises from altered nociceptive processing in dopaminergic pathways; some PD pain fluctuates with 'off' periods and eases with dopaminergic therapy.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression is one of the commonest non-motor features of Parkinson's, often preceding motor symptoms: degeneration of dopaminergic, serotonergic, and noradrenergic systems—not just illness burden—drives it, so PD depression is intrinsic to the neurodegeneration.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Parkinson's may begin in the gut: α-synuclein pathology appears in the enteric nervous system years before the brain (preceded by constipation), and an altered gut microbiome is implicated, supporting Braak's hypothesis that disease ascends the vagus from gut to brainstem.
- `connects-to` → **[Huntington Disease](../huntingtons-disease/README.md)** — Parkinson's and Huntington's are movement disorders at opposite poles: PD is hypokinetic from dopamine loss, causing bradykinesia and rigidity, while Huntington's is hyperkinetic from striatal degeneration, causing chorea—mirror images of basal-ganglia dysfunction.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Parkinson's disease and schizophrenia are dopamine opposites: PD comes from too little striatal dopamine, while psychosis involves too much dopamine signaling—so antipsychotics cause parkinsonism and PD drugs can cause psychosis.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Parkinson's disease and narcolepsy both disrupt sleep-wake regulation: PD patients commonly have REM-sleep behavior disorder years before motor symptoms, plus excessive daytime sleepiness, reflecting degeneration of brainstem sleep nuclei—an early PD warning sign.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes participate in Parkinson's neurodegeneration: reactive astrocytes can clear or spread α-synuclein, lose support of dopaminergic neurons, and amplify neuroinflammation with microglia—so glia, not just dying neurons, shape progression.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Parkinson's is not just a dopamine disease: degeneration of noradrenergic locus coeruleus neurons depletes norepinephrine, driving the autonomic failure, orthostatic hypotension and cognitive and mood symptoms that levodopa cannot fix.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin neurons degenerate in Parkinson's too: their loss contributes to the depression, anxiety and sleep disturbance that often precede motor signs, and serotonergic terminals also aberrantly process levodopa, contributing to dyskinesias.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Parkinson's is a disorder of the whole nervous system: though defined by nigral dopamine loss and tremor, alpha-synuclein pathology spreads from gut and brainstem to cortex, explaining the autonomic, sleep, sensory and cognitive features beyond movement.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Parkinson's is a dopamine-acetylcholine imbalance: as dopamine falls, relatively unopposed cholinergic activity in the striatum worsens tremor, so anticholinergic drugs help—while loss of cholinergic neurons elsewhere contributes to the dementia of advanced disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron accumulates in the Parkinson's brain: the substantia nigra loads with iron that can catalyze oxidative damage and ferroptosis of dopamine neurons, so brain iron is both a disease marker on MRI and a candidate target for protective therapy.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Parkinson's often begins in the gut: constipation can precede tremor by years, and misfolded alpha-synuclein appears in enteric nerves early—fuelling the 'gut-first' hypothesis that the disease may ascend the vagus nerve from gut to brain.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Parkinson's disrupts the basal ganglia's glutamate balance: losing dopamine lets the subthalamic nucleus fire excess glutamate onto output nuclei, driving the movement slowing—so the NMDA-blocker amantadine and deep-brain stimulation of this glutamatergic hub help.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Parkinson's has an autoimmune flavor: T-helper cells that recognize alpha-synuclein peptides infiltrate the brain and may accelerate dopaminergic neuron loss, linking the adaptive immune system to a classic neurodegenerative disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Parkinson's denervates the heart early: loss of sympathetic nerves to the heart (seen on MIBG imaging) is a characteristic, early sign reflecting that alpha-synuclein pathology spreads through the autonomic nervous system beyond the brain.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Parkinson's dopamine neurons are vulnerable because of calcium: the substantia nigra cells are autonomous pacemakers that fire using calcium channels, and that constant calcium load stresses mitochondria—why calcium-channel blockers are tested to protect them.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Parkinson's is partly an energy failure: mitochondrial complex-I defects and failed mitophagy starve dopamine neurons of ATP, and the toxin MPTP that causes parkinsonism works exactly by poisoning this energy supply.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Parkinson's has an autoimmune streak involving regulatory T cells: T cells that recognize alpha-synuclein appear in patients, and a shortage of restraining Tregs may let this immune attack add to the neurodegeneration.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Parkinson's may begin at the synapse: alpha-synuclein normally works at presynaptic terminals, and its misfolding cripples dopamine release and synaptic function long before neurons die—so the disease is in part a failure of synapses, not just cells.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Parkinson's may start in the gut: alpha-synuclein clumps appear in the large intestine's nerves years early, constipation is among the first symptoms, and the pathology may climb the vagus nerve from bowel to brain.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Parkinson's smolders with TNF-α: activated microglia pour out this cytokine in the affected brain, and the chronic neuroinflammation it drives is thought to accelerate the loss of dopamine neurons.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Parkinson's can be imaged: a DaTscan uses radioactive photons to show the depleted dopamine terminals in the striatum, separating true Parkinson's from tremor that merely mimics it.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Parkinson's leaves traces in the skin: alpha-synuclein deposits can be found in skin nerve biopsies as an emerging diagnostic test, and seborrheic dermatitis is a common early sign.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Where alpha-synuclein lodges decides the disease: when it accumulates in oligodendrocytes rather than neurons, the result is multiple system atrophy, a faster Parkinson-plus disorder.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals Parkinson's defining lesion: the Lewy body, a dense core of tangled alpha-synuclein filaments inside the dying dopamine neuron, surrounded by the swollen, failing mitochondria that mark its energy crisis.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Parkinson's shows in the eyes: blinking slows to a stare, eye movements grow jerky, and dopamine loss thins the retina — a change now studied as an early imaging biomarker of the disease in the brain.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper handling falters in the Parkinson's brain: the metal normally helps antioxidant defenses, and its disturbed balance in the substantia nigra adds to the oxidative stress, alongside iron, that kills the dopamine neurons.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Parkinson's slows the stomach: gastroparesis delays emptying so erratically that levodopa absorption becomes unpredictable, causing the on-off motor swings, while the delayed transit is part of the gut dysfunction that may even precede the tremor.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Sleep breaks down early in Parkinson's: REM sleep behavior disorder — acting out dreams — is a striking prodrome that can precede the disease by years, and disrupted melatonin and circadian rhythm worsen the fragmented nights.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Autonomic failure reaches the body's smooth muscle: the disease's loss of autonomic control slows gut and bladder smooth muscle into constipation and urinary trouble, and weakens vascular tone into the orthostatic hypotension that causes falls.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Clearing the rogue protein is the new hope: monoclonal antibodies against aggregated alpha-synuclein are in trials to slow Parkinson's, aiming to mop up the misfolded protein before it spreads neuron to neuron.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Parkinson's is a disease of basal-ganglia GABA circuits: losing dopamine unbalances the GABAergic direct and indirect pathways, over-inhibiting movement — and that same GABA output is what deep-brain stimulation and pallidotomy retune.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Dopamine treatment can unleash compulsions: dopamine-agonist drugs trigger impulse-control disorders including hypersexuality, while autonomic disease causes erectile and sexual dysfunction — and estrogen's neuroprotection may explain why men are affected more.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Parkinson's and melanoma travel together: people with one carry a higher risk of the other, a bidirectional link rooted in shared pigment and α-synuclein biology rather than in levodopa, prompting skin surveillance in patients.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Parkinson's reaches beyond the brain into peripheral nerves: α-synuclein deposits in autonomic fibers of the skin and gut — now sampled by biopsy to diagnose it — and the resulting autonomic neuropathy causes orthostatic drops in blood pressure.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — The immune system joins the attack on dopamine neurons: cytotoxic T cells that recognize α-synuclein fragments infiltrate the substantia nigra, an adaptive autoimmune assault that helps drive the neuronal loss of Parkinson's.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Microglia inflame the dying nigra: α-synuclein aggregates activate the NLRP3 inflammasome in microglia to release IL-1β, a self-amplifying neuroinflammation that accelerates dopamine-neuron loss and is a leading drug target in Parkinson's.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Disordered insulin signaling speeds it: type 2 diabetes and brain insulin resistance raise Parkinson's risk and quicken its progression, which is why GLP-1 diabetes drugs are now being trialed to slow the neurodegeneration.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Innate cells help clear the toxic protein: natural killer cells scavenge α-synuclein aggregates and modulate the neuroinflammation, an innate-immune arm of Parkinson's that complements the cytotoxic T-cell attack.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Microglia inflame the dying neurons through NF-κB: α-synuclein activates NF-κB in microglia, which prime the NLRP3 inflammasome and pour out cytokines that accelerate the loss of dopaminergic neurons.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep falls apart early and often: insomnia, fragmented sleep and REM sleep behavior disorder are cardinal non-motor features of Parkinson's, sometimes preceding the tremor by years as the disease invades sleep-regulating nuclei.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Swallowing fails and the lungs pay: advancing Parkinson's brings dysphagia and aspiration, so aspiration pneumonia and the sepsis it triggers are the leading cause of death in the disease.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Falls meet fragile bones: postural instability and freezing make falls frequent in Parkinson's, while immobility and low vitamin D thin the bones, so osteoporotic hip and wrist fractures are a major source of disability.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety is a core non-motor feature: persistent worry and 'off'-period anxiety are common in Parkinson's, arising from the same degeneration of dopaminergic, noradrenergic and serotonergic systems that drives the motor disease.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Renal function shapes its treatment and risk: chronic kidney disease shares vascular and oxidative mechanisms epidemiologically linked to Parkinson's, and impaired clearance alters dosing of the drugs used to manage it.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Its dysphagia lets food reach the lungs: impaired swallowing in Parkinson's causes silent aspiration, and the resulting aspiration pneumonia — often pneumococcal — is the leading cause of death in advanced disease.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Progressive immobility clots the veins: the bradykinesia, rigidity and falls of advanced Parkinson's reduce mobility, and the resulting venous stasis raises the risk of deep vein thrombosis and pulmonary embolism.
- `connects-to` → **[Stroke](../stroke/README.md)** — It shares the vascular terrain: Parkinson's overlaps with cerebrovascular disease through vascular parkinsonism, and the reduced mobility and autonomic dysfunction of advanced disease compound stroke risk.
- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — Its dopamine drugs unleash compulsions: dopamine-agonist therapy for Parkinson's classically triggers impulse-control disorders — pathological gambling, hypersexuality and compulsive shopping — that resolve when the drug is reduced.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Rigidity and falls batter the skeleton: the bradykinesia, postural instability and stooped camptocormic posture of Parkinson's cause frequent falls and fractures, contractures and chronic musculoskeletal pain.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Autonomic failure unsettles the bladder: Parkinson's disrupts autonomic control of the bladder, causing urinary urgency, frequency and nocturia, with retention and recurrent infection in advanced disease.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Autonomic failure drops the blood pressure: Parkinson's causes orthostatic hypotension — a major non-motor feature worsened by levodopa — leading to dizziness, syncope and falls on standing.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It shows on the skin: seborrhoeic dermatitis with a greasy, scaly face and excess sweating are classic dermatological features of Parkinson's, reflecting its autonomic and sebaceous dysregulation.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Swallowing failure floods the lungs: dysphagia leads to aspiration pneumonia — a leading cause of death in Parkinson's — while rigidity of the chest wall restricts breathing.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Brain inflammation drives it: microglial neuroinflammation and the immune-regulating LRRK2 gene implicate the immune system in the onset and progression of Parkinson's disease.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Failing waste clearance lets protein build up: impaired glymphatic and meningeal-lymphatic clearance of alpha-synuclein is increasingly implicated in the neurodegeneration of Parkinson's.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is tied to metabolism: Parkinson's causes unexplained weight loss and is bidirectionally linked with type 2 diabetes, sharing mitochondrial and insulin-signalling pathways.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — A gut bug that blocks the drug: Helicobacter pylori infection impairs levodopa absorption and is epidemiologically linked to Parkinson's, so eradication can improve motor control.
- `connects-to` → **[Influenza A](../../../02-pathogen/01-viruses/influenza-a/README.md)** — A historical post-infectious link: the encephalitis lethargica that followed the 1918 influenza pandemic caused a striking post-encephalitic parkinsonism, fuelling interest in infectious triggers.
- `connects-to` → **[Ginkgo Biloba](../../../03-medicine/02-traditional/ginkgo-biloba/README.md)** — Traditional neuroprotectants are explored: antioxidant herbs such as ginkgo biloba are studied for neurodegeneration, though none substitute for dopaminergic therapy in Parkinson's.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Aggregates clog the axon: α-synuclein oligomers impair axonal transport in nigrostriatal neurons, contributing to the dying-back degeneration that strips dopamine terminals from the striatum before cell bodies die.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It denervates the heart: Parkinson's causes cardiac sympathetic denervation, so reduced MIBG uptake in the myocardium is an early biomarker distinguishing it from atypical parkinsonism, and contributes to orthostatic hypotension.
- `connects-to` → **[Panax Ginseng](../../../03-medicine/02-traditional/panax-ginseng/README.md)** — Ginsenosides are studied for neuroprotection: Panax ginseng shows dopaminergic-neuron-protective effects in Parkinson's models, joining ginkgo among traditional remedies explored as adjuncts, though none replace levodopa.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — It may begin in the gut: α-synuclein pathology can start in the enteric nervous system of the intestinal wall and ascend the vagus to the brain (Braak's gut-first hypothesis), and constipation precedes the tremor by years.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Dementia comes with time: most people with Parkinson's eventually develop cognitive decline as α-synuclein and Lewy pathology spread to the hippocampus and cortex, blurring the line with Lewy body dementia.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Infections can trigger parkinsonism: as influenza once left post-encephalitic parkinsonism, viral infections including COVID-19 are reported to precipitate or unmask Parkinson's, supporting a role for neuroinflammation in its onset.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Vascular parkinsonism: small-vessel disease of the brain's arterial walls can mimic Parkinson's with a lower-body, gait-predominant parkinsonism that responds poorly to levodopa, a key differential.
- `connects-to` → **[ALS](../als/README.md)** — Neurodegeneration's shared themes: Parkinson's and ALS are both age-related neurodegenerations driven by protein misfolding and aggregation, with rare overlap syndromes and the Guam ALS-parkinsonism-dementia complex linking them.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — A shared dopamine thread: bipolar disorder is associated with a higher later risk of Parkinson's disease, and the dopaminergic dysregulation of mania mirrors, in reverse, the dopamine loss of Parkinson's.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Aspiration ends it: dysphagia in advanced Parkinson's leads to aspiration pneumonia, seeding the alveoli with oral flora—the leading cause of death in the disease.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — Drug-induced valve disease: ergot-derived dopamine agonists (pergolide, cabergoline) stimulate 5-HT2B receptors to fibrose the heart valves and endocardium, the reason these agonists are now largely avoided.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Pain in Parkinson's: chronic pain is a common non-motor symptom of Parkinson's with central-sensitisation features that overlap fibromyalgia, beyond the rigidity and dystonia of the motor disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Neuroinflammation: IL-1β released by activated microglia around degenerating dopaminergic neurons amplifies the inflammatory cascade that drives nigral cell loss in Parkinson's.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory marker: elevated IL-6 in CSF and blood tracks neuroinflammation and disease progression in Parkinson's, part of the cytokine milieu fuelling neurodegeneration.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Impaired clearance: mTOR overactivity suppresses the autophagy/mitophagy needed to clear α-synuclein and damaged mitochondria, and its inhibition is neuroprotective in Parkinson's models.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Microglial recruitment: CCL2 released in the inflamed substantia nigra draws monocytes and amplifies the microglial activation that contributes to dopaminergic neurodegeneration in Parkinson's.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Adaptive autoimmunity: IFN-γ from T cells recognising α-synuclein epitopes infiltrates the Parkinson's brain, evidence that an adaptive immune attack on dopaminergic neurons contributes to the disease.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Neuroprotective repurposing: GLP-1 receptor agonists developed for diabetes show neuroprotective signals in Parkinson's trials, reflecting a metabolic-neurodegeneration link and brain insulin signalling.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Aggregated α-synuclein released from dying neurons activates microglial TLR4, triggering the chronic neuroinflammation that propagates dopaminergic neurodegeneration—linking the disease's defining protein to its inflammatory engine.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Iron accumulates in the substantia nigra of Parkinson's disease, and dysregulated ferroportin-controlled iron export sensitizes dopaminergic neurons to ferroptotic, oxidative cell death—the rationale for iron-chelation trials.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Failed PINK1/Parkin mitophagy lets damaged mitochondria leak DNA that activates cGAS-STING, driving the type-I-interferon neuroinflammation now implicated in the neurodegeneration of both familial and sporadic Parkinson's.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Substantia-nigra dopaminergic neurons use L-type Cav1.3 calcium channels for autonomous pacemaking, and the resulting chronic calcium load stresses mitochondria—a selective vulnerability that motivated the isradipine trials in Parkinson's.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Xanthine oxidase produces urate, and higher urate levels are associated with lower Parkinson's risk and slower progression, suggesting that antioxidant urate partly offsets the oxidative stress damaging dopaminergic neurons.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF normally sustains the survival of substantia-nigra dopaminergic neurons, and its reduction in Parkinson's removes a key neurotrophic support, contributing to the progressive degeneration of the nigrostriatal pathway.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Substantia-nigra dopaminergic neurons face intense oxidative stress, and the NRF2 antioxidant response is a key defense whose decline permits the oxidative and mitochondrial damage driving Parkinson's neurodegeneration.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3-mediated apoptosis executes the loss of nigral dopaminergic neurons in Parkinson's, downstream of the mitochondrial dysfunction and α-synuclein toxicity already mapped.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Microglial complement C3 tags synapses and neurons for elimination in Parkinson's, an arm of the neuroinflammation (with the NLRP3 inflammasome already mapped) that propagates neurodegeneration.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK senses the bioenergetic failure of Parkinson's (ATP mapped) and, opposing mTOR (mapped), promotes the autophagy/mitophagy (autophagy mapped) that clears the damaged mitochondria central to dopaminergic neuron death.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β phosphorylates tau (MAPT mapped) and promotes neuronal apoptosis, a convergence node linking the genetic and degenerative threads of Parkinson's disease.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4 (mapped) sensing of aggregated α-synuclein (SNCA mapped) signals through MyD88 to activate microglia, driving the neuroinflammation that propagates Parkinson's neurodegeneration.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling (GSK-3β and mTOR mapped) maintains dopaminergic-neuron survival, and its failure promotes the apoptotic loss characteristic of Parkinson's disease.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IFN-γ/cytokine-driven JAK-STAT signaling (IFN-γ mapped) sustains the reactive microgliosis that propagates dopaminergic neuroinflammation in Parkinson's disease.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 is induced by α-synuclein (SNCA mapped) and amplifies the neuroinflammatory response driving dopaminergic neurodegeneration.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling drives the interferon-responsive microglial activation that contributes to the neuroinflammation of Parkinson's disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — JAK-STAT3 signaling (JAK1/2 already mapped) in microglia and astrocytes sustains the reactive gliosis accompanying dopaminergic neurodegeneration in Parkinson's disease.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN, the phosphatase that restrains PI3K-AKT survival signaling (and the namesake of PINK1's pathway), modulates the mitochondrial quality control and neuronal survival relevant to Parkinson's disease.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the autophagy and oxidative-stress defense of dopaminergic neurons, programs that fail in Parkinson's disease.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation contributing to dopaminergic degeneration in Parkinson's disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling participates in dopaminergic neuron stress and in the L-DOPA-induced dyskinesia associated with Parkinson's disease therapy.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α couples the mitochondrial dysfunction and oxidative stress of dopaminergic neurons to metabolic adaptation in Parkinson's disease.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the neuronal survival pathways whose failure contributes to dopaminergic degeneration in Parkinson's disease.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic CD8 T cells infiltrate the substantia nigra and contribute to the neurodegeneration of Parkinson's disease.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation, including SNCA regulation, implicated in Parkinson's disease.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the microglial activation and neuroinflammation of Parkinson's disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte and microglial recruitment amplifies the neuroinflammation of Parkinson's disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the microglial and immune-cell responses of the neuroinflammation of Parkinson's disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling from infiltrating T cells participates in the neuroinflammation and dopaminergic neurodegeneration of Parkinson's disease.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and astrocyte neuroinflammatory responses of Parkinson's disease.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neuronal and neuroinflammatory gene programs of Parkinson's disease.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the microglial activation and neuronal calcium dysregulation of Parkinson's disease.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (A2A receptor) signaling participates in the basal-ganglia motor circuitry and neuroinflammation of Parkinson's disease.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences: Parkinson's disease is more common in men, and estrogen exerts neuroprotective effects on dopaminergic neurons, contributing to the later onset and milder early course seen in women.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Brain renin-angiotensin: a local renin-angiotensin system in the substantia nigra amplifies microglial oxidative stress and neuroinflammation, and angiotensin-receptor blockade is neuroprotective in models, a target beyond dopamine replacement.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance: brain insulin resistance is common in Parkinson's disease and impairs neuronal energetics and survival, the rationale behind repurposing GLP-1 agonists (already mapped) as disease-modifying candidates.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Adaptive autoimmunity: alpha-synuclein-specific T cells recognised through IL-2-driven expansion are found in Parkinson's disease, implicating an adaptive immune response against the aggregating protein (already mapped) in dopaminergic neuron loss.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Neurosteroid protection: progesterone and its neurosteroid metabolites are neuroprotective, and together with estrogen (already mapped) may contribute to the lower incidence and later onset of Parkinson's disease in women.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Microglial polarisation: IL-4 shifts microglia (already mapped) toward a reparative, anti-inflammatory phenotype, and boosting this arm against the pro-inflammatory TNF/IL-1 response is a neuroprotective strategy explored in Parkinson's disease.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory neuroprotection: IL-10, with IL-4 (already mapped), opposes the microglial pro-inflammatory response (TNF, IL-1 and IL-6 already mapped) driving dopaminergic neuron loss, and boosting this arm is a neuroprotective strategy in Parkinson's disease.
- `connects-to` → **[Small intestine](../../06-organ/small-intestine/README.md)** — Enteric origin: alpha-synuclein pathology (already mapped) may begin in the enteric nervous system, and the small intestine, like the large intestine (already mapped), is affected early, with altered motility and the prodromal gut symptoms of Parkinson's disease.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the activated microglia (already mapped) contribute to the neuroinflammation that drives dopaminergic neuron loss, and the cyclooxygenase pathway has been studied as a neuroprotective target in Parkinson's disease.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Nitrosative stress: nitric oxide from the activated microglia (already mapped) forms peroxynitrite that nitrosylates proteins and adds to the oxidative injury (ferroportin-linked iron already mapped) killing the dopaminergic neurons of Parkinson's disease.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc dyshomeostasis: disturbed zinc handling in the substantia nigra, alongside the iron (already mapped) and copper accumulation, contributes to the metal-catalysed oxidative stress that damages the dopaminergic neurons of Parkinson's disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium neuroprotection: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity on the vulnerable nigral neurons, a proposed neuroprotective factor in Parkinson's disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation (NLRP3, TNF and IL-1 already mapped) that drives the dopaminergic loss of Parkinson's disease.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron regulation: hepcidin governs the iron (already mapped) handling whose dysregulation contributes to the nigral iron accumulation (ferroportin already mapped) and the metal-catalysed oxidative stress of Parkinson's disease.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine neuroprotection: the adipokine leptin has neurotrophic and neuroprotective actions on the dopaminergic neurons, and the metabolic dysregulation (insulin already mapped) it reflects is linked to Parkinson's-disease risk.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Neuroprotective adipokine: adiponectin, with leptin (already mapped), has neuroprotective and metabolic (insulin already mapped) actions linked to Parkinson's-disease risk and the metabolic milieu.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the neuroinflammation (TNF and IL-6 already mapped) and metabolic milieu of Parkinson's disease.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Mitochondrial-DNA interferon: the cGAS-STING (already mapped) sensing of the mitochondrial DNA from the failing mitophagy (autophagy already mapped) drives the type-I interferon neuroinflammation of Parkinson's disease.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the T-cell-mediated neuroinflammation that accelerates the dopaminergic neuron (already mapped) loss of Parkinson's disease.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 immune arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the peripheral immune dysregulation associated with Parkinson's disease.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 neuroinflammation: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory response implicated in Parkinson's disease.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Anti-α-synuclein humoral arm: the B cells produce the anti-α-synuclein (SNCA already mapped) antibodies of the emerging adaptive-immune contribution to Parkinson's disease.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell neuroinflammation: the mast cells of the brain and the gut (already mapped) contribute to the neuroinflammation and the gut-brain axis of Parkinson's disease.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the peripheral immune dysregulation of Parkinson's disease.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Nigral iron: transferrin, the iron carrier, is central to the iron accumulation in the substantia nigra that, with the disordered ferroportin and hepcidin (already mapped), drives the oxidative stress and ferroptosis of the dopaminergic neurons of Parkinson's disease.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells of the CNS-border and peripheral compartments present the alpha-synuclein (already mapped) epitopes to the T cells (already mapped), priming the adaptive autoimmunity implicated in Parkinson's disease.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the microglial (already mapped) neuroinflammation of Parkinson's disease.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the complement-driven microglial neuroinflammation of Parkinson's disease.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the neuroinflammation of Parkinson's disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Border-associated macrophages: the CNS-border and infiltrating macrophages contribute to the clearance of the alpha-synuclein (already mapped) and the neuroinflammation of Parkinson's disease.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuroinflammatory alarmin: TSLP, released from enteric epithelium (gut-microbiome already mapped) and skin (already mapped) during gut dysbiosis, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the gut-to-brain axis of Parkinson's disease.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-oedema axis: bradykinin, generated by the kallikrein-kinin system activated by neuroinflammation, augments blood-brain-barrier permeability and amplifies the microglial (already mapped) and macrophage (already mapped) recruitment of Parkinson's disease.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective cytokine: erythropoietin, acting via EPOR on dopaminergic neurons (already mapped) and astrocytes (already mapped), promotes neuronal survival and limits the oxidative and neuroinflammatory degeneration of Parkinson's disease.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Striatal mast-cell effector: histamine, released by mast cells in the substantia nigra and striatum, promotes dopaminergic neurotoxicity via H1/H4 receptors on microglia (already mapped) and amplifies the neuroinflammatory milieu (TNF-α and IL-1β already mapped) of Parkinson's disease.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM remodelling in the nigro-striatal pathway: periostin, expressed by astrocytes (already mapped) in the substantia nigra under neuroinflammation, modulates the extracellular matrix scaffold and Lewy body (alpha-synuclein already mapped) deposition in Parkinson's disease.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits the classical complement (C3 and C5 already mapped) and bradykinin (already mapped) activation in the inflamed substantia nigra, moderating the complement-driven dopaminergic neurodegeneration of Parkinson's disease.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — PD testosterone: testosterone attenuates SNCA (already mapped) aggregation and microglial (already mapped) neuroinflammation in the substantia nigra; androgen deficiency accelerates the dopaminergic neuron (already mapped) loss of Parkinson's disease.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — PD oxytocin: oxytocin receptors on astrocytes (already mapped) and dopaminergic neurons (already mapped) attenuate SNCA (already mapped) aggregation; oxytocin also modulates the dopamine (already mapped) and serotonin (already mapped) circuits of Parkinson's disease.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — PD vasopressin: vasopressin V1A receptors on dopaminergic neurons (already mapped) modulate striatal activity and dopamine (already mapped) release; vasopressin deficiency amplifies the neuroinflammatory and autonomic (brain already mapped) dysfunction of Parkinson's disease.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — PD prolactin: prolactin modulates dopaminergic (already mapped) neuron survival and microglial (already mapped) neuroinflammation in the substantia nigra; prolactin interacts with SNCA (already mapped) aggregation and the NF-κB (already mapped) cascade of Parkinson's disease.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — PD selenium: selenoprotein P reduces the oxidative stress driving SNCA (already mapped) aggregation and dopaminergic (already mapped) neurodegeneration; selenium deficiency amplifies the NF-κB (already mapped) neuroinflammation and accelerates Parkinson's disease progression.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — PD iodine: iodine-dependent thyroid hormones sustain dopaminergic (already mapped) neuron energy metabolism in the substantia nigra; thyroid-hormone deficiency amplifies the NF-κB (already mapped) cascade and worsens SNCA (already mapped) aggregation in Parkinson's disease.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — PD sodium: excess sodium promotes microglia (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and TNF-α (already mapped) skewing amplifies the neuroinflammatory cascade of Parkinson's disease.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — PD potassium: potassium regulates neuron (already mapped) and microglia (already mapped) membrane excitability; potassium dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade and dopaminergic degeneration of Parkinson's disease.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — PD phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and microglia (already mapped), maintains dopaminergic neuron energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of Parkinson's disease.

[^kalia-2015-pd-review]: Kalia LV, Lang AE. Parkinson's disease. *Lancet.* 2015;386(9996):896-912. [doi:10.1016/S0140-6736(14)61393-3](https://doi.org/10.1016/S0140-6736(14)61393-3) · [PubMed 25904081](https://pubmed.ncbi.nlm.nih.gov/25904081/)
[^spillantini-1997-lewy-body]: Spillantini MG, Schmidt ML, Lee VM, Trojanowski JQ, Jakes R, Goedert M. Alpha-synuclein in Lewy bodies. *Nature.* 1997;388(6645):839-840. [doi:10.1038/42166](https://doi.org/10.1038/42166) · [PubMed 9278044](https://pubmed.ncbi.nlm.nih.gov/9278044/)
[^olanow-2009-pd-treatment]: Olanow CW, Stern MB, Sethi K. The scientific and clinical basis for the treatment of Parkinson disease. *Neurology.* 2009;72(21 Suppl 4):S1-136. [doi:10.1212/WNL.0b013e3181a1d44c](https://doi.org/10.1212/WNL.0b013e3181a1d44c) · [PubMed 19470958](https://pubmed.ncbi.nlm.nih.gov/19470958/)
