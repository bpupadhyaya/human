---
schema: human-scale-entry/v1
id: huntingtons-disease
name: Huntington Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Huntington disease is caused by HTT CAG repeat expansion (≥36 copies); autosomal dominant; choreoathetosis, cognitive decline, and psychiatric disturbance onset in the 4th-5th decade; disease-modifying HTT-lowering therapies (ASOs, siRNA) are in Phase 3 clinical trials."
aliases: ["Huntington disease", "HD", "Huntington's disease", "HTT CAG expansion", "huntingtin disease", "chorea HD", "polyQ neurodegeneration", "HD neurodegeneration", "CAG repeat disease", "HTT repeat expansion"]
cross_links:
  - target: 01-human/03-molecular/htt
    relation: connects-to
    note: "HTT CAG repeat ≥36 → polyglutamine mHTT aggregation → impaired proteostasis, mitochondrial dysfunction, and transcriptional dysregulation in striatal MSNs; caudate/putamen atrophy is the hallmark; juvenile HD (>60 CAG) presents with rigidity and seizures rather than chorea."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Mutant huntingtin (mHTT) sequesters p62/SQSTM1 and impairs autophagosome formation → defective selective autophagy → mHTT aggregate accumulation → neuronal proteotoxicity; mTOR inhibitors (rapamycin) and autophagy enhancers reduce mHTT burden in HD mouse models."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "mHTT causes preferential degeneration of striatal MSNs expressing D1 and D2 dopamine receptors; early loss of indirect pathway MSNs (D2) → dopamine pathway imbalance → chorea; tetrabenazine (VMAT2 inhibitor) depletes presynaptic dopamine → suppresses choreiform movements."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "mHTT aggregates activate caspase-3 and caspase-9 in striatal MSNs via mitochondrial pathway; mHTT N-terminal fragments (calpain-cleaved) amplify caspase activation; caspase-3 inhibition with z-DEVD-fmk is neuroprotective in HD mouse models, supporting apoptosis as a driver."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "mHTT disrupts HTT's cytoplasmic REST/NRSF sequestration → nuclear REST represses BDNF transcription; mHTT also impairs HAP1-mediated BDNF vesicle transport from cortex to striatum → MSN trophic deprivation; BDNF/TrkB restoration is a key HD therapeutic goal."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Striatal MSNs receive massive glutamatergic input from cortex; mHTT sensitizes MSNs to NMDA receptor excitotoxicity via NR2B (GluN2B) dysregulation; riluzole and memantine reduce excitotoxic MSN death in HD models; E/I imbalance contributes to early HD cognitive symptoms."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "HD selectively atrophies striatum (caudate + putamen) detectable by MRI 15+ years pre-onset; cortical layer V and thalamic neurons also degenerate; lateral ventricle enlargement mirrors striatal volume loss and tracks disease progression by UHDRS total functional capacity."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Huntington's disease kills a specific neuron: the GABAergic medium spiny neurons of the striatum, especially indirect-pathway (D2) MSNs whose loss disinhibits movement and causes chorea; mutant huntingtin starves them of BDNF and sensitizes them to glutamate excitotoxicity."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Neuroinflammation is an early feature of Huntington's disease: microglia activate in the striatum and cortex years before symptoms (on PET), and mutant huntingtin acts cell-autonomously inside microglia to make them hyper-reactive — adding inflammation to the neurodegeneration."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Huntington's disease is an autosomal-dominant neurodegenerative disease of the CNS: a CAG-repeat expansion in HTT makes a toxic polyglutamine protein that destroys the striatum and cortex, causing chorea, cognitive decline, and psychiatric disturbance over 15-20 years."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes contribute to Huntington's disease: mutant huntingtin in astrocytes impairs glutamate uptake (lower EAAT2) and potassium buffering, raising excitotoxicity on vulnerable striatal neurons and cutting neurotrophic support—amplifying the neuronal loss."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Huntington's and Parkinson's are contrasting basal-ganglia disorders: HD is a CAG-repeat disease causing chorea from striatal indirect-pathway neuron loss, while PD causes hypokinesia from dopaminergic loss—dopamine-blockers ease HD chorea but cause parkinsonism."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Psychiatric illness is intrinsic to Huntington's, not just reactive: depression is very common and suicide risk markedly elevated, often preceding motor onset, reflecting degeneration of frontostriatal mood circuits; treating it is central to HD care given the high suicide rate."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Huntington's and Alzheimer's are both neurodegenerative proteinopathies: Huntington's is a dominant CAG-repeat expansion striking striatal neurons, while Alzheimer's is mostly sporadic amyloid-β and tau pathology of the cortex—monogenic chorea versus complex dementia."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Huntington's disease is fundamentally a loss of GABAergic neurons: the striatal medium spiny neurons that degenerate are the brain's main inhibitory (GABA) output, so their loss disinhibits motor circuits, producing the involuntary chorea that defines the disease."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Huntington's often presents with psychiatric symptoms before chorea: depression, irritability and psychosis resembling schizophrenia can precede motor signs by years, reflecting striatal-prefrontal disruption—a movement disorder first masquerading as mental illness."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "Huntington's and ALS are both fatal neurodegenerations but mechanistically distinct: HD is a CAG-repeat polyglutamine disease killing striatal neurons, while ALS destroys motor neurons via TDP-43—both show how a single protein's misfolding dooms specific neurons."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Huntington's disease damages the heart, not just the brain: mutant huntingtin and autonomic dysfunction cause cardiomyopathy and arrhythmias, making cardiac disease a leading cause of death in HD—evidence the CAG-repeat defect harms tissues beyond the striatum."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Depression in Huntington's reflects serotonergic disruption: mood disorder and suicide risk often precede the movement disorder, driven partly by altered serotonin signaling, so SSRIs are widely used—psychiatric care is as central to HD management as treating chorea."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Huntington's disease also strikes striatal acetylcholine: loss of cholinergic interneurons in the caudate and putamen disturbs the balance with dopamine and GABA, contributing to the movement and cognitive disorder beyond the classic medium spiny neuron loss."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Huntington's shows genetic anticipation through the reproductive system: the CAG repeat expands further during sperm formation, so paternally transmitted disease tends to start earlier and more severely in each generation—a hallmark of trinucleotide-repeat inheritance."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Huntington's disease harms the heart and metabolism: mutant huntingtin and autonomic dysfunction cause cardiomyopathy and a hypermetabolic, wasting state, so cardiovascular disease and weight loss are major non-neurological contributors to death in HD."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Huntington's disease causes relentless weight loss through the gut: chorea burns energy while swallowing difficulty and gut dysfunction limit intake, so progressive cachexia and aspiration are major problems despite a normal or increased appetite."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Huntington's disease begins at the synapse: mutant huntingtin disrupts synaptic signaling and BDNF transport long before neurons die, so striatal synapse loss—not just cell death—drives the early movement and cognitive decline."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium-driven excitotoxicity kills neurons in Huntington's: overactive NMDA receptors flood striatal neurons with calcium, triggering the cascades that destroy them, so disturbed calcium handling links glutamate signaling to the disease's selective neuronal loss."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Huntington's starves neurons of ATP: mutant huntingtin cripples mitochondria, so striatal neurons can't generate enough energy and the whole body burns through calories—explaining both neurodegeneration and the relentless weight loss of the disease."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Huntington's damages oligodendrocytes and white matter: mutant huntingtin disrupts the genes these cells use to myelinate axons, so white-matter loss appears even before obvious neuron death—an early structural marker of the disease."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Huntington's disrupts the brain's own cholesterol: mutant huntingtin suppresses cholesterol synthesis that neurons need for synapses and myelin, so falling brain cholesterol contributes to the synaptic failure underlying symptoms."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron piles up in the Huntington's brain: the degenerating basal ganglia accumulate iron that catalyzes oxidative stress, adding a metal-driven injury to the toxic effects of the mutant huntingtin protein."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Huntington's wastes the body despite eating: gut dysmotility and a hypermetabolic state cause relentless weight loss, so the large intestine and digestion are part of the systemic toll beyond the movement and mood symptoms."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Microglia inflame the Huntington's brain through NF-kB: mutant huntingtin activates this inflammatory switch in the brain's immune cells, and the resulting cytokine release adds neuroinflammation to the neuronal degeneration."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Huntington's reaches the pancreas: the disease is linked to diabetes and impaired insulin output, as mutant huntingtin disturbs pancreatic islet cells alongside its toll on the brain."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Huntington's burns through fat: a hypermetabolic state and altered adipocytes drive the relentless weight loss that marks the disease, so patients need far more calories than expected."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Huntington's brain smolders with TNF-α: activated microglia release this cytokine, and the chronic neuroinflammation it drives compounds the degeneration of the vulnerable striatal neurons."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Huntington's shows on MRI: the photons reveal the shrunken caudate and putamen that flatten the ventricle's edge, a structural marker that tracks the disease as it advances."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Huntington's reaches beyond the striatum into the hippocampus: its degeneration contributes to the memory and learning deficits that accompany the movement disorder."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Huntington's disrupts the immune system too: mutant huntingtin in immune cells makes monocytes and T cells hyperreactive, adding peripheral inflammation to the neurodegeneration."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals Huntington's protein clumps: the expanded-glutamine huntingtin aggregates into dense intranuclear inclusions inside striatal neurons, the misfolded-protein lesion that marks the disease's relentless cell death."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eyes betray Huntington's early: slowed and broken saccadic eye movements appear before the chorea is obvious, an early, measurable sign clinicians use to track the disease's onset and progression."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Huntington's most often ends through the lungs: as the disease destroys the control of swallowing, aspiration pneumonia becomes the leading cause of death, the same final pathway as other late neurodegenerations."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Huntington's starves the body despite eating: a hypermetabolic state plus the difficulty getting food down causes relentless weight loss, so high-calorie feeding and eventually a gastrostomy become part of care."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "The disease scrambles the body clock: degeneration of the brain's circadian centers blunts melatonin and fragments sleep, with insomnia and reversed day-night rhythms appearing even before the chorea."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Huntington's writes itself on movement: the writhing chorea gives way over years to rigidity and dystonia, and the constant motion plus poor intake wastes muscle, driving the falls and disability that define its course."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Metals pile up in the dying striatum: Huntington's brains accumulate copper and iron in the degenerating basal ganglia, where the redox-active metal binds mutant huntingtin and fuels the oxidative stress that helps kill the neurons."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Huntington's disturbs the gonadal axis: mutant huntingtin damages the hypothalamus and testes, lowering testosterone and shrinking the gonads — one of the peripheral endocrine signs that the disease reaches well beyond the brain."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "The psychiatric face can come first: years before the chorea, Huntington's brings obsessive, perseverative and compulsive behaviors along with irritability and apathy, reflecting the early breakdown of the striatal-frontal circuits that govern flexible behavior."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Huntington's deranges metabolism too: mutant huntingtin impairs pancreatic beta cells and energy handling, so diabetes is more common even as relentless weight loss strips the body — a peripheral metabolic face of the disease."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Clearing the aggregates runs through mTOR: the protein's signaling restrains autophagy, so mTOR inhibitors like rapamycin are studied to boost the disposal of toxic mutant huntingtin."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The mutation reaches the immune cells: macrophages and monocytes carrying mutant huntingtin are hyperreactive and pour out extra cytokines, a peripheral immune activation that parallels the brain's microglial inflammation."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement tags the doomed synapses: C1q and C3 mark striatal synapses for microglial pruning in Huntington's, an over-active version of developmental synapse elimination that contributes to the early circuit loss."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Huntington's wrecks the body clock: degeneration of hypothalamic circadian centers and falling melatonin fragment sleep into severe insomnia and day-night reversal, often years before the chorea, worsening cognition and mood."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Aspiration is how Huntington's kills: as the disease destroys swallowing control, food and saliva enter the lungs, and the resulting aspiration pneumonia and sepsis are the leading cause of death."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Mutant huntingtin inflames the brain: it activates microglia and the NLRP3 inflammasome, releasing IL-1β that adds a neuroinflammatory accelerant to the striatal neuron loss of Huntington's."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Mood swings can precede the chorea: Huntington's psychiatric prodrome includes irritability, mania and depression resembling bipolar disorder, reflecting the disease's early reach into mood-regulating circuits."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The mutant protein also harms the heart: huntingtin is expressed in cardiomyocytes, and Huntington's carries a cardiomyopathy and autonomic dysfunction that make cardiac disease a major non-neurological cause of death."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its cardiomyopathy can fail the heart: mutant huntingtin's direct cardiac toxicity and autonomic dysfunction predispose to a cardiomyopathy and heart failure, a leading non-neurological cause of death in Huntington's."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Wasting and falls fracture fragile bones: the relentless weight loss, immobility and frequent falls of advancing Huntington's leave low bone density and a high risk of osteoporotic fracture."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety is part of its psychiatric face: marked anxiety, often preceding the motor signs, is common in Huntington's, arising from the same striatal-cortical degeneration that drives its mood and behavioral changes."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Chorea and dysphagia send food to the lungs: progressive swallowing failure in Huntington's causes aspiration, and the resulting pneumonia — often pneumococcal — is the leading cause of death."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Involuntary movement and late immobility break the skin: chorea causes repeated minor trauma, and the bedbound, malnourished end stage of Huntington's predisposes to pressure ulcers that heal poorly."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "It can ignite seizures: epilepsy is a recognized feature, especially of juvenile Huntington's disease, reflecting the cortical involvement of its neurodegeneration."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Swallowing failure floods the lungs: progressive dysphagia and chorea of the swallowing muscles in Huntington's cause aspiration, and aspiration pneumonia is the leading cause of death."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It burns weight despite eating: Huntington's causes profound weight loss through a hypermetabolic state and hypothalamic dysfunction that also disrupts circadian and metabolic hormones."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut-brain axis is disturbed: Huntington's disease is associated with gut dysbiosis that, through the gut-brain axis, may contribute to its weight loss and the progression of its symptoms."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "The mutant protein also harms the heart: huntingtin is expressed in cardiac muscle, contributing to cardiomyopathy and autonomic dysfunction, with heart disease a leading cause of death in Huntington's."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It hyperactivates the immune system: mutant huntingtin in immune cells causes peripheral immune hyperactivation and neuroinflammation thought to contribute to disease progression."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It loses bladder control: advancing Huntington's brings neurogenic bladder with urinary urgency and incontinence and a raised risk of urinary infection."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "Psychiatric symptoms need treatment: SSRIs like fluoxetine are widely used for the depression, anxiety and obsessive-compulsive features that often precede and accompany Huntington's chorea."
  - target: 01-human/07-system/lewy-body-dementia
    relation: connects-to
    note: "A fellow movement-and-mind neurodegeneration: like Lewy body dementia, Huntington's disease couples a movement disorder with progressive cognitive and psychiatric decline, though through a different pathology."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "End-stage immobility breaks the skin: in advanced Huntington's disease, rigidity, immobility and poor nutrition make pressure ulcers a major complication of care."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Stress hormones run high: Huntington's disease disrupts the hypothalamic-pituitary-adrenal axis, raising cortisol and contributing to its weight loss, mood disturbance and metabolic decline."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Dysphagia invites pneumonia: as Huntington's disease impairs swallowing, aspiration of oral bacteria including Staphylococcus aureus causes the pneumonia that is a leading cause of death."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Sleep falls apart through orexin loss: Huntington's disease damages hypothalamic orexin neurons, producing the fragmented sleep and daytime sleepiness it shares with narcolepsy."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Mutant huntingtin jams the cell's transport: expanded huntingtin disrupts microtubule-based axonal transport, starving neurons of BDNF and mitochondria delivered along the axon—a core driver of the striatal neuron death behind Huntington's chorea."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It is not only a brain disease: huntingtin is expressed in the heart, and Huntington's disease carries a peripheral cardiomyopathy with autonomic dysfunction, so cardiac causes rank among its leading deaths alongside aspiration pneumonia."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "Opposite roads to wasting: Huntington's disease causes relentless weight loss from a hypermetabolic state despite preserved or increased appetite, the mirror image of anorexia nervosa, where psychological appetite suppression drives the weight loss."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Arrhythmia and sudden death: beyond cardiomyopathy, Huntington's autonomic failure prolongs the QT interval and disturbs cardiac rhythm, contributing to the sudden cardiac deaths that punctuate the disease."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Wasting thins the skeleton: HD's hypermetabolic, chorea-driven catabolism causes progressive weight loss and reduced bone density, raising fracture risk in a population already prone to falls."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Gut involvement: mutant huntingtin is expressed in the gut, where enteric dysfunction and altered intestinal epithelium contribute to the weight loss and gut-brain disturbances of HD."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Aspiration ends it: dysphagia from advanced Huntington's leads to aspiration pneumonia, seeding the alveoli with oral flora—the leading cause of death in the disease."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Chorea has many causes: beyond Huntington's, chorea arises in lupus and antiphospholipid syndrome (autoimmune chorea), a treatable mimic to exclude before attributing new chorea to HD."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Acquired chorea: a stroke in the subthalamic nucleus or basal ganglia causes hemiballismus and chorea, an acquired movement disorder that mimics the inherited chorea of Huntington's."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "Repeat-expansion modifier: DNA mismatch-repair genes such as MLH1 and MSH3 drive somatic CAG-repeat expansion in striatal neurons, a leading genetic modifier of Huntington's age of onset."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Failing antioxidant defence: impaired NRF2 (NFE2L2) signalling contributes to the oxidative stress and mitochondrial dysfunction that drive neuronal death in Huntington's disease."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Apoptotic activation: mutant huntingtin interacts with and activates p53, promoting the mitochondrial dysfunction and neuronal apoptosis central to Huntington's neurodegeneration."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory progression: elevated IL-6 appears years before symptom onset in Huntington's disease, part of the systemic and central inflammation tracking with its course."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Microglial cytokine: IL-1β from microglia activated by mutant huntingtin amplifies the neuroinflammation that contributes to striatal neuronal loss in Huntington's disease."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Noradrenergic disruption: degeneration of brainstem noradrenergic neurons in Huntington's disease alters norepinephrine signalling, contributing to its mood and autonomic symptoms."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Neuroinflammatory recruitment: CCL2 is elevated in Huntington's disease and recruits monocytes and activates microglia, contributing to the neuroinflammation that accompanies striatal degeneration."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA-sensing inflammation: mitochondrial dysfunction in Huntington's disease releases DNA that activates cGAS-STING, an emerging driver of the chronic neuroinflammatory response to mutant huntingtin."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Neurotrophic support: IGF-1 signalling is dysregulated in Huntington's disease and supports neuronal survival, an axis explored for neuroprotection alongside the loss of BDNF support to the striatum."
  - target: 01-human/03-molecular/msh2
    relation: connects-to
    note: "Somatic CAG expansion: DNA mismatch-repair genes including MSH2 (with MSH3 and MLH1) drive the somatic expansion of the CAG repeat in neurons, the modifier process that GWAS show governs the age of onset of Huntington's disease."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "BDNF-TrkB starvation: mutant huntingtin impairs the cortical production and axonal transport of BDNF to the striatum, depriving striatal neurons of the TrkB-mediated trophic support whose loss drives their selective death."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Microglial neuroinflammation: mutant huntingtin and DAMPs activate microglial TLR4, driving the neuroinflammation that accompanies and accelerates the striatal neurodegeneration of Huntington's disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Excitotoxic calcium: mutant huntingtin sensitises striatal NMDA receptors and disrupts mitochondrial calcium handling, so glutamate excitotoxicity floods medium spiny neurons with calcium — a central mechanism of their selective vulnerability in Huntington's."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial driver: galectin-3 released by activated microglia in the Huntington's striatum amplifies the neuroinflammatory response, a microglial signal increasingly implicated as a driver of the neurodegeneration alongside the cell-autonomous huntingtin toxicity."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: mitochondrial dysfunction and xanthine-oxidase-derived reactive oxygen species add an oxidative burden to the striatal neurons in Huntington's, compounding the energy failure that the NRF2 antioxidant response struggles to offset."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Pro-survival phosphorylation: IGF-1 and BDNF (both mapped) signal through PI3K-AKT, and AKT phosphorylates huntingtin at serine-421 to reduce its toxicity — a neuroprotective axis that is impaired in Huntington's disease."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "Energy sensing: the bioenergetic failure of Huntington's (ATP already mapped) activates AMPK, which both reflects the energy deficit and promotes the autophagic clearance (autophagy mapped) of mutant huntingtin aggregates."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Mitochondrial apoptosis: a shift in the BCL-2 family balance toward apoptosis engages the mitochondrial caspase pathway (caspase-3 mapped) that drives the death of striatal medium spiny neurons in Huntington's."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microglial neuroinflammation: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped) in microglia drives the neuroinflammation that accelerates striatal neurodegeneration in Huntington's disease."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine inflammation: IL-6 and interferon signalling through JAK-STAT (IL-6 already mapped) contributes to the central and peripheral inflammation characteristic of Huntington's disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Neurotrophic survival: ERK-MAPK signalling engaged downstream of BDNF-TrkB (both already mapped) is a pro-survival pathway whose impairment contributes to the vulnerability of striatal medium spiny neurons in Huntington's disease."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β dysregulation, downstream of impaired BDNF/AKT signalling (BDNF and AKT mapped), contributes to the neuronal dysfunction and death of Huntington's disease."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN regulation of the PI3K-AKT-mTOR axis (AKT and mTOR mapped) influences the autophagic clearance of mutant huntingtin and neuronal survival in Huntington's disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3-driven reactive astrogliosis is part of the neuroinflammatory response to striatal degeneration in Huntington's disease."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling (cGAS-STING already mapped) drives the interferon-responsive microglial activation of the neuroinflammation in Huntington's disease."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors (notably FOXO3) promote the autophagy and proteostasis that clear mutant huntingtin, a neuroprotective axis in Huntington's disease."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the neuroprotective-versus-inflammatory glial balance in the striatal degeneration of Huntington's disease."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation of Huntington's disease."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and mitochondrial stress responses contribute to the striatal neurodegeneration of Huntington's disease."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Aberrant CDK4/6-driven cell-cycle re-entry of post-mitotic neurons contributes to the neuronal death of Huntington's disease."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the neuronal survival pathways compromised in Huntington's disease."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of gene expression in Huntington's disease."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-p53 signaling (p53 already mapped) participates in the neuronal apoptosis of Huntington's disease."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (FYN) kinase signaling participates in the NMDA-receptor-mediated excitotoxicity and synaptic dysfunction of Huntington's disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven microglial and monocyte recruitment contributes to the neuroinflammation of Huntington's disease."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-linked calcium signaling participates in the excitotoxic neuronal dysfunction of Huntington's disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the microglial and neuroinflammatory responses of Huntington's disease."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses of Huntington's disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation of Huntington's disease."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of the neuronal gene programs of Huntington's disease."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (A2A receptor) signaling participates in the striatal-neuron dysfunction and neuroinflammation of Huntington's disease."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microglial activation and neuroinflammation of Huntington's disease."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Hypermetabolic weight loss: despite adequate intake, Huntington's disease causes progressive weight loss from a hypermetabolic state with impaired insulin signalling and mitochondrial energy failure (ATP already mapped), a metabolic feature tracking disease severity."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Energy dysregulation: falling fat stores and altered leptin signalling accompany the relentless weight loss of Huntington's disease, reflecting hypothalamic involvement and the systemic metabolic disturbance beyond the movement disorder."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Neuroinflammation: MHC class II is upregulated on activated microglia (already mapped) in the Huntington striatum, marking the neuroinflammatory response that accompanies and may accelerate the degeneration of medium spiny neurons."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac involvement: mutant huntingtin is expressed in the heart, and Huntington's disease carries a cardiomyopathy and autonomic dysfunction, with troponin elevation marking the myocardial injury that contributes to its cardiovascular mortality."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Excitotoxic injury: nitric oxide from neuronal nitric oxide synthase, driven by the glutamate excitotoxicity (already mapped), contributes with reactive oxygen species (xanthine oxidase already mapped) to the oxidative and nitrosative damage of the striatal neurons."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Metabolic wasting: the relentless weight loss of Huntington's disease reflects hypothalamic and metabolic dysfunction (insulin and leptin already mapped), and GLP-1-based agents are studied for the disturbed energy and glucose handling."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the activated microglia (already mapped) and the cyclooxygenase pathway contribute to the neuroinflammation (TNF, IL-6 and IL-1 already mapped) that accelerates the striatal neurodegeneration of Huntington's disease."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory counterweight: the anti-inflammatory IL-10 opposes the microglial pro-inflammatory response (TNF, IL-6 and IL-1 already mapped) driving the neurodegeneration, part of the neuroimmune balance in Huntington's disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "NMDA neuroprotection: magnesium blocks the NMDA receptor of the glutamate excitotoxicity (already mapped) that kills the striatal neurons, and its modulation is of interest for the excitotoxic injury of Huntington's disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Microglial polarisation: IL-4 polarises the microglia (already mapped) toward an anti-inflammatory M2 phenotype (IL-10 already mapped), the balance against the pro-inflammatory activation shaping the neuroinflammation of Huntington's disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglial arm whose balance against the pro-inflammatory signals (TNF, IL-1 and IL-6 already mapped) shapes the neurodegeneration of Huntington's disease."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Synaptic zinc: zinc modulates the glutamatergic (already mapped) synapses of the striatum, and the zinc dyshomeostasis of Huntington's disease contributes, with iron and copper (already mapped), to the metal-linked excitotoxic neurodegeneration."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Weight-loss adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the weight loss and metabolic (insulin already mapped) disturbance that are features of Huntington's disease."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "cGAS-STING neuroinflammation: type-I interferon, downstream of the cGAS-STING (already mapped) pathway activated by the mutant huntingtin (already mapped), drives the innate-immune neuroinflammation of Huntington's disease."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Hypermetabolism adipokine: resistin, with leptin and adiponectin (already mapped), is part of the adipokine milieu of the weight loss and hypermetabolism of Huntington's disease."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the infiltrating T cells (with the type-I interferon already mapped) is the type-II interferon arm of the peripheral-immune activation and neuroinflammation of Huntington's disease."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response of the systemic-immune activation accompanying the neurodegeneration of Huntington's disease."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive neuroinflammation: the cytotoxic T cells (perforin already mapped) infiltrate the neuroinflamed Huntington brain, the adaptive-immune component of the neurodegeneration."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the peripheral-immune dysregulation of Huntington's disease."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the peripheral-immune activation and neuroinflammation of Huntington's disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells of the peripheral and CNS-border immune compartments present antigen to the T cells (already mapped) of the neuroinflammation of Huntington's disease."
sources:
  - id: gusella-1983-htt-locus
    type: peer-reviewed
    cite: "Gusella JF, Wexler NS, Conneally PM, et al. A polymorphic DNA marker genetically linked to Huntington's disease. Nature. 1983;306(5940):234-238."
    doi: "10.1038/306234a0"
    pmid: "6316146"
    url: "https://doi.org/10.1038/306234a0"
  - id: macdonald-1993-htt-gene
    type: peer-reviewed
    cite: "The Huntington's Disease Collaborative Research Group. A novel gene containing a trinucleotide repeat that is expanded and unstable on Huntington's disease chromosomes. Cell. 1993;72(6):971-983."
    doi: "10.1016/0092-8674(93)90585-E"
    pmid: "8458085"
    url: "https://doi.org/10.1016/0092-8674(93)90585-E"
---

# Huntington Disease

## Overview

Huntington disease (HD) is an autosomal dominant neurodegenerative disorder caused by CAG trinucleotide repeat expansion (≥36 repeats) in exon 1 of the HTT gene on chromosome 4p16.3. Prevalence is ~5–10 per 100,000 in populations of European ancestry; lower in Asian and African populations. Repeat length is the primary determinant of age of onset: 36–39 repeats → reduced penetrance (onset often >60 years); 40–55 repeats → classic adult HD (mean onset ~40 years); >60 repeats → juvenile HD (onset <20 years). HD is uniformly progressive and fatal, with death typically 15–20 years after motor onset. No disease-modifying therapy is currently approved, but several HTT-lowering strategies are in late-phase trials.

## Structure

HD pathology centers on preferential degeneration of striatal medium spiny neurons (MSNs), which constitute ~95% of striatal neurons. The indirect pathway MSNs (D2 receptor-expressing, enkephalinergic, projecting to globus pallidus externa) are lost early, disinhibiting the subthalamic nucleus and producing hyperkinesia (chorea). Direct pathway MSNs (D1, substance P, projecting to GPi/SNr) are lost later, causing rigidity and bradykinesia in advanced disease. Cortical neurons (layer V pyramidal cells) also degenerate, contributing to cognitive and psychiatric features. Caudate and putamen atrophy is the neuroimaging hallmark; ventricular enlargement (especially lateral horns) is proportional to striatal volume loss and correlates with disease stage.

## Function

HD disrupts multiple neural circuit functions:
- **Motor control**: Cortico-striato-thalamo-cortical loops are disrupted; early indirect pathway loss → chorea; late direct pathway loss → rigidity/dystonia.
- **Cognition**: Executive dysfunction (frontal-striatal), working memory loss, and slowed processing precede motor onset by years; dementia is universal in late HD.
- **Psychiatry**: Depression (prevalence ~40%), irritability, apathy, OCD-like behaviors, and psychosis occur throughout the disease course; psychiatric symptoms often predate motor diagnosis.
- **Autonomic/systemic**: Weight loss is common (despite adequate intake) due to hypothalamic involvement and elevated metabolic rate; sleep disturbances (REM sleep behavior disorder, circadian disruption) are prominent.

## Pathology

**Genetics**: Juvenile HD (>60 CAG) presents with akinetic-rigid syndrome, seizures, and rapid progression rather than chorea. New mutations (>36 CAG de novo) arise primarily from paternal transmission of intermediate alleles (27–35 repeats); somatic instability in striatum amplifies repeat length beyond the germline count, explaining tissue-specific vulnerability.

**Neuropathology**: Intranuclear inclusions (NIIs) containing mHTT exon-1 fragments are present in neurons; paradoxically, neurons with inclusions may survive longer than inclusion-free neurons — soluble oligomeric mHTT is the primary toxic species. MSN loss follows a dorsomedial → ventrolateral gradient in caudate; putamen loss parallels caudate. Vonsattel grade 0–4 grading system (grade 0 = no visible atrophy but microscopically abnormal; grade 4 = severe global striatal loss).

**Diagnosis**: Clinical diagnosis requires motor signs + positive genetic test (≥36 CAG repeats). Predictive genetic testing is available for at-risk individuals (with mandatory pre- and post-test counseling per HDSA/EHN guidelines). Plasma neurofilament light (NfL) is an emerging biomarker: NfL rises 15+ years before expected motor onset in CAG expansion carriers and tracks disease progression.

**Treatment**:
- Chorea: Tetrabenazine (VMAT2 inhibitor, FDA 2008), deutetrabenazine (FDA 2017), valbenazine (FDA 2023) reduce chorea without altering disease course.
- Psychiatric: Standard antidepressants, antipsychotics (olanzapine, quetiapine for irritability/psychosis); avoid typical antipsychotics (worsen rigidity).
- HTT-lowering (investigational): Tominersen (intrathecal ASO targeting HTT mRNA) showed dose-dependent CSF HTT reduction but unexpected clinical worsening in the 2021 Phase 3 GENERATION HD1 trial (120 mg every 8 weeks cohort); lower-dose regimens under re-evaluation. WVE-003 (allele-selective ASO targeting SNP rs362307 on mHTT allele) and siRNA approaches (RG6042, ARB-1001) in Phase 1/2. AAV5-miHTT gene therapy (uniQure) in Phase 1/2.

## Connections

- `connects-to` → **[HTT](../../03-molecular/htt/README.md)** — HTT CAG repeat ≥36 → polyglutamine mHTT aggregation → impaired proteostasis, mitochondrial dysfunction, and transcriptional dysregulation in striatal MSNs; caudate/putamen atrophy is the hallmark; juvenile HD (>60 CAG) presents with rigidity and seizures rather than chorea.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — mutant huntingtin sequesters p62/SQSTM1 and impairs autophagosome formation → defective selective autophagy → mHTT accumulation → neuronal proteotoxicity; mTOR inhibitors and autophagy enhancers reduce mHTT burden in HD mouse models.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — mHTT causes preferential degeneration of striatal MSNs expressing D1 and D2 dopamine receptors; indirect pathway MSN (D2) loss → chorea; tetrabenazine (VMAT2 inhibitor) depletes presynaptic dopamine to suppress choreiform movements; approved FDA 2008.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — mHTT aggregates activate caspase-3 and caspase-9 in striatal MSNs via mitochondrial pathway; calpain-cleaved mHTT N-terminal fragments amplify caspase activation; caspase-3 inhibition is neuroprotective in HD mouse models.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — mHTT disrupts REST/NRSF cytoplasmic sequestration → nuclear REST represses BDNF transcription; mHTT also impairs HAP1-mediated BDNF vesicle transport from cortex to striatum → MSN trophic deprivation; BDNF/TrkB signaling restoration is a key therapeutic goal.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — striatal MSNs receive massive glutamatergic input from cortex; mHTT sensitizes MSNs to NMDA excitotoxicity via NR2B dysregulation; riluzole and memantine reduce excitotoxic MSN death in HD models; E/I imbalance contributes to early cognitive symptoms.
- `targets` → **[Brain](../../06-organ/brain/README.md)** — HD selectively atrophies striatum (caudate + putamen) detectable by MRI 15+ years pre-onset; cortical layer V and thalamic neurons also degenerate; lateral ventricle enlargement mirrors striatal atrophy and tracks disease progression by UHDRS-TFC.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Huntington's disease kills a specific neuron: the GABAergic medium spiny neurons of the striatum, especially indirect-pathway (D2) MSNs whose loss disinhibits movement and causes chorea; mutant huntingtin starves them of BDNF and sensitizes them to glutamate excitotoxicity.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Neuroinflammation is an early feature of Huntington's disease: microglia activate in the striatum and cortex years before symptoms (on PET), and mutant huntingtin acts cell-autonomously inside microglia to make them hyper-reactive — adding inflammation to the neurodegeneration.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Huntington's disease is an autosomal-dominant neurodegenerative disease of the CNS: a CAG-repeat expansion in HTT makes a toxic polyglutamine protein that destroys the striatum and cortex, causing chorea, cognitive decline, and psychiatric disturbance over 15-20 years.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes contribute to Huntington's disease: mutant huntingtin in astrocytes impairs glutamate uptake (lower EAAT2) and potassium buffering, raising excitotoxicity on vulnerable striatal neurons and cutting neurotrophic support—amplifying the neuronal loss.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Huntington's and Parkinson's are contrasting basal-ganglia disorders: HD is a CAG-repeat disease causing chorea from striatal indirect-pathway neuron loss, while PD causes hypokinesia from dopaminergic loss—dopamine-blockers ease HD chorea but cause parkinsonism.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Psychiatric illness is intrinsic to Huntington's, not just reactive: depression is very common and suicide risk markedly elevated, often preceding motor onset, reflecting degeneration of frontostriatal mood circuits; treating it is central to HD care given the high suicide rate.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Huntington's and Alzheimer's are both neurodegenerative proteinopathies: Huntington's is a dominant CAG-repeat expansion striking striatal neurons, while Alzheimer's is mostly sporadic amyloid-β and tau pathology of the cortex—monogenic chorea versus complex dementia.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Huntington's disease is fundamentally a loss of GABAergic neurons: the striatal medium spiny neurons that degenerate are the brain's main inhibitory (GABA) output, so their loss disinhibits motor circuits, producing the involuntary chorea that defines the disease.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Huntington's often presents with psychiatric symptoms before chorea: depression, irritability and psychosis resembling schizophrenia can precede motor signs by years, reflecting striatal-prefrontal disruption—a movement disorder first masquerading as mental illness.
- `connects-to` → **[ALS](../als/README.md)** — Huntington's and ALS are both fatal neurodegenerations but mechanistically distinct: HD is a CAG-repeat polyglutamine disease killing striatal neurons, while ALS destroys motor neurons via TDP-43—both show how a single protein's misfolding dooms specific neurons.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Huntington's disease damages the heart, not just the brain: mutant huntingtin and autonomic dysfunction cause cardiomyopathy and arrhythmias, making cardiac disease a leading cause of death in HD—evidence the CAG-repeat defect harms tissues beyond the striatum.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Depression in Huntington's reflects serotonergic disruption: mood disorder and suicide risk often precede the movement disorder, driven partly by altered serotonin signaling, so SSRIs are widely used—psychiatric care is as central to HD management as treating chorea.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Huntington's disease also strikes striatal acetylcholine: loss of cholinergic interneurons in the caudate and putamen disturbs the balance with dopamine and GABA, contributing to the movement and cognitive disorder beyond the classic medium spiny neuron loss.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Huntington's shows genetic anticipation through the reproductive system: the CAG repeat expands further during sperm formation, so paternally transmitted disease tends to start earlier and more severely in each generation—a hallmark of trinucleotide-repeat inheritance.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Huntington's disease harms the heart and metabolism: mutant huntingtin and autonomic dysfunction cause cardiomyopathy and a hypermetabolic, wasting state, so cardiovascular disease and weight loss are major non-neurological contributors to death in HD.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Huntington's disease causes relentless weight loss through the gut: chorea burns energy while swallowing difficulty and gut dysfunction limit intake, so progressive cachexia and aspiration are major problems despite a normal or increased appetite.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Huntington's disease begins at the synapse: mutant huntingtin disrupts synaptic signaling and BDNF transport long before neurons die, so striatal synapse loss—not just cell death—drives the early movement and cognitive decline.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium-driven excitotoxicity kills neurons in Huntington's: overactive NMDA receptors flood striatal neurons with calcium, triggering the cascades that destroy them, so disturbed calcium handling links glutamate signaling to the disease's selective neuronal loss.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Huntington's starves neurons of ATP: mutant huntingtin cripples mitochondria, so striatal neurons can't generate enough energy and the whole body burns through calories—explaining both neurodegeneration and the relentless weight loss of the disease.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Huntington's damages oligodendrocytes and white matter: mutant huntingtin disrupts the genes these cells use to myelinate axons, so white-matter loss appears even before obvious neuron death—an early structural marker of the disease.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Huntington's disrupts the brain's own cholesterol: mutant huntingtin suppresses cholesterol synthesis that neurons need for synapses and myelin, so falling brain cholesterol contributes to the synaptic failure underlying symptoms.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron piles up in the Huntington's brain: the degenerating basal ganglia accumulate iron that catalyzes oxidative stress, adding a metal-driven injury to the toxic effects of the mutant huntingtin protein.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Huntington's wastes the body despite eating: gut dysmotility and a hypermetabolic state cause relentless weight loss, so the large intestine and digestion are part of the systemic toll beyond the movement and mood symptoms.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Microglia inflame the Huntington's brain through NF-kB: mutant huntingtin activates this inflammatory switch in the brain's immune cells, and the resulting cytokine release adds neuroinflammation to the neuronal degeneration.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Huntington's reaches the pancreas: the disease is linked to diabetes and impaired insulin output, as mutant huntingtin disturbs pancreatic islet cells alongside its toll on the brain.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Huntington's burns through fat: a hypermetabolic state and altered adipocytes drive the relentless weight loss that marks the disease, so patients need far more calories than expected.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Huntington's brain smolders with TNF-α: activated microglia release this cytokine, and the chronic neuroinflammation it drives compounds the degeneration of the vulnerable striatal neurons.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Huntington's shows on MRI: the photons reveal the shrunken caudate and putamen that flatten the ventricle's edge, a structural marker that tracks the disease as it advances.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Huntington's reaches beyond the striatum into the hippocampus: its degeneration contributes to the memory and learning deficits that accompany the movement disorder.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Huntington's disrupts the immune system too: mutant huntingtin in immune cells makes monocytes and T cells hyperreactive, adding peripheral inflammation to the neurodegeneration.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals Huntington's protein clumps: the expanded-glutamine huntingtin aggregates into dense intranuclear inclusions inside striatal neurons, the misfolded-protein lesion that marks the disease's relentless cell death.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eyes betray Huntington's early: slowed and broken saccadic eye movements appear before the chorea is obvious, an early, measurable sign clinicians use to track the disease's onset and progression.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Huntington's most often ends through the lungs: as the disease destroys the control of swallowing, aspiration pneumonia becomes the leading cause of death, the same final pathway as other late neurodegenerations.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Huntington's starves the body despite eating: a hypermetabolic state plus the difficulty getting food down causes relentless weight loss, so high-calorie feeding and eventually a gastrostomy become part of care.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — The disease scrambles the body clock: degeneration of the brain's circadian centers blunts melatonin and fragments sleep, with insomnia and reversed day-night rhythms appearing even before the chorea.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Huntington's writes itself on movement: the writhing chorea gives way over years to rigidity and dystonia, and the constant motion plus poor intake wastes muscle, driving the falls and disability that define its course.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Metals pile up in the dying striatum: Huntington's brains accumulate copper and iron in the degenerating basal ganglia, where the redox-active metal binds mutant huntingtin and fuels the oxidative stress that helps kill the neurons.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Huntington's disturbs the gonadal axis: mutant huntingtin damages the hypothalamus and testes, lowering testosterone and shrinking the gonads — one of the peripheral endocrine signs that the disease reaches well beyond the brain.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — The psychiatric face can come first: years before the chorea, Huntington's brings obsessive, perseverative and compulsive behaviors along with irritability and apathy, reflecting the early breakdown of the striatal-frontal circuits that govern flexible behavior.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Huntington's deranges metabolism too: mutant huntingtin impairs pancreatic beta cells and energy handling, so diabetes is more common even as relentless weight loss strips the body — a peripheral metabolic face of the disease.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Clearing the aggregates runs through mTOR: the protein's signaling restrains autophagy, so mTOR inhibitors like rapamycin are studied to boost the disposal of toxic mutant huntingtin.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The mutation reaches the immune cells: macrophages and monocytes carrying mutant huntingtin are hyperreactive and pour out extra cytokines, a peripheral immune activation that parallels the brain's microglial inflammation.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement tags the doomed synapses: C1q and C3 mark striatal synapses for microglial pruning in Huntington's, an over-active version of developmental synapse elimination that contributes to the early circuit loss.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Huntington's wrecks the body clock: degeneration of hypothalamic circadian centers and falling melatonin fragment sleep into severe insomnia and day-night reversal, often years before the chorea, worsening cognition and mood.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Aspiration is how Huntington's kills: as the disease destroys swallowing control, food and saliva enter the lungs, and the resulting aspiration pneumonia and sepsis are the leading cause of death.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Mutant huntingtin inflames the brain: it activates microglia and the NLRP3 inflammasome, releasing IL-1β that adds a neuroinflammatory accelerant to the striatal neuron loss of Huntington's.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Mood swings can precede the chorea: Huntington's psychiatric prodrome includes irritability, mania and depression resembling bipolar disorder, reflecting the disease's early reach into mood-regulating circuits.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The mutant protein also harms the heart: huntingtin is expressed in cardiomyocytes, and Huntington's carries a cardiomyopathy and autonomic dysfunction that make cardiac disease a major non-neurological cause of death.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its cardiomyopathy can fail the heart: mutant huntingtin's direct cardiac toxicity and autonomic dysfunction predispose to a cardiomyopathy and heart failure, a leading non-neurological cause of death in Huntington's.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Wasting and falls fracture fragile bones: the relentless weight loss, immobility and frequent falls of advancing Huntington's leave low bone density and a high risk of osteoporotic fracture.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety is part of its psychiatric face: marked anxiety, often preceding the motor signs, is common in Huntington's, arising from the same striatal-cortical degeneration that drives its mood and behavioral changes.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Chorea and dysphagia send food to the lungs: progressive swallowing failure in Huntington's causes aspiration, and the resulting pneumonia — often pneumococcal — is the leading cause of death.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Involuntary movement and late immobility break the skin: chorea causes repeated minor trauma, and the bedbound, malnourished end stage of Huntington's predisposes to pressure ulcers that heal poorly.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — It can ignite seizures: epilepsy is a recognized feature, especially of juvenile Huntington's disease, reflecting the cortical involvement of its neurodegeneration.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Swallowing failure floods the lungs: progressive dysphagia and chorea of the swallowing muscles in Huntington's cause aspiration, and aspiration pneumonia is the leading cause of death.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It burns weight despite eating: Huntington's causes profound weight loss through a hypermetabolic state and hypothalamic dysfunction that also disrupts circadian and metabolic hormones.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut-brain axis is disturbed: Huntington's disease is associated with gut dysbiosis that, through the gut-brain axis, may contribute to its weight loss and the progression of its symptoms.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — The mutant protein also harms the heart: huntingtin is expressed in cardiac muscle, contributing to cardiomyopathy and autonomic dysfunction, with heart disease a leading cause of death in Huntington's.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It hyperactivates the immune system: mutant huntingtin in immune cells causes peripheral immune hyperactivation and neuroinflammation thought to contribute to disease progression.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It loses bladder control: advancing Huntington's brings neurogenic bladder with urinary urgency and incontinence and a raised risk of urinary infection.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — Psychiatric symptoms need treatment: SSRIs like fluoxetine are widely used for the depression, anxiety and obsessive-compulsive features that often precede and accompany Huntington's chorea.
- `connects-to` → **[Lewy Body Dementia](../lewy-body-dementia/README.md)** — A fellow movement-and-mind neurodegeneration: like Lewy body dementia, Huntington's disease couples a movement disorder with progressive cognitive and psychiatric decline, though through a different pathology.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — End-stage immobility breaks the skin: in advanced Huntington's disease, rigidity, immobility and poor nutrition make pressure ulcers a major complication of care.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Stress hormones run high: Huntington's disease disrupts the hypothalamic-pituitary-adrenal axis, raising cortisol and contributing to its weight loss, mood disturbance and metabolic decline.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Dysphagia invites pneumonia: as Huntington's disease impairs swallowing, aspiration of oral bacteria including Staphylococcus aureus causes the pneumonia that is a leading cause of death.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Sleep falls apart through orexin loss: Huntington's disease damages hypothalamic orexin neurons, producing the fragmented sleep and daytime sleepiness it shares with narcolepsy.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Mutant huntingtin jams the cell's transport: expanded huntingtin disrupts microtubule-based axonal transport, starving neurons of BDNF and mitochondria delivered along the axon—a core driver of the striatal neuron death behind Huntington's chorea.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It is not only a brain disease: huntingtin is expressed in the heart, and Huntington's disease carries a peripheral cardiomyopathy with autonomic dysfunction, so cardiac causes rank among its leading deaths alongside aspiration pneumonia.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — Opposite roads to wasting: Huntington's disease causes relentless weight loss from a hypermetabolic state despite preserved or increased appetite, the mirror image of anorexia nervosa, where psychological appetite suppression drives the weight loss.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Arrhythmia and sudden death: beyond cardiomyopathy, Huntington's autonomic failure prolongs the QT interval and disturbs cardiac rhythm, contributing to the sudden cardiac deaths that punctuate the disease.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Wasting thins the skeleton: HD's hypermetabolic, chorea-driven catabolism causes progressive weight loss and reduced bone density, raising fracture risk in a population already prone to falls.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Gut involvement: mutant huntingtin is expressed in the gut, where enteric dysfunction and altered intestinal epithelium contribute to the weight loss and gut-brain disturbances of HD.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Aspiration ends it: dysphagia from advanced Huntington's leads to aspiration pneumonia, seeding the alveoli with oral flora—the leading cause of death in the disease.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Chorea has many causes: beyond Huntington's, chorea arises in lupus and antiphospholipid syndrome (autoimmune chorea), a treatable mimic to exclude before attributing new chorea to HD.
- `connects-to` → **[Stroke](../stroke/README.md)** — Acquired chorea: a stroke in the subthalamic nucleus or basal ganglia causes hemiballismus and chorea, an acquired movement disorder that mimics the inherited chorea of Huntington's.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — Repeat-expansion modifier: DNA mismatch-repair genes such as MLH1 and MSH3 drive somatic CAG-repeat expansion in striatal neurons, a leading genetic modifier of Huntington's age of onset.
- `connects-to` → **[NFE2L2](../../03-molecular/nfe2l2/README.md)** — Failing antioxidant defence: impaired NRF2 (NFE2L2) signalling contributes to the oxidative stress and mitochondrial dysfunction that drive neuronal death in Huntington's disease.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Apoptotic activation: mutant huntingtin interacts with and activates p53, promoting the mitochondrial dysfunction and neuronal apoptosis central to Huntington's neurodegeneration.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory progression: elevated IL-6 appears years before symptom onset in Huntington's disease, part of the systemic and central inflammation tracking with its course.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Microglial cytokine: IL-1β from microglia activated by mutant huntingtin amplifies the neuroinflammation that contributes to striatal neuronal loss in Huntington's disease.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Noradrenergic disruption: degeneration of brainstem noradrenergic neurons in Huntington's disease alters norepinephrine signalling, contributing to its mood and autonomic symptoms.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Neuroinflammatory recruitment: CCL2 is elevated in Huntington's disease and recruits monocytes and activates microglia, contributing to the neuroinflammation that accompanies striatal degeneration.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA-sensing inflammation: mitochondrial dysfunction in Huntington's disease releases DNA that activates cGAS-STING, an emerging driver of the chronic neuroinflammatory response to mutant huntingtin.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Neurotrophic support: IGF-1 signalling is dysregulated in Huntington's disease and supports neuronal survival, an axis explored for neuroprotection alongside the loss of BDNF support to the striatum.
- `connects-to` → **[MSH2](../../03-molecular/msh2/README.md)** — DNA mismatch-repair genes including MSH2 (with MSH3 and MLH1) drive the somatic expansion of the CAG repeat within neurons, the modifier process that genome-wide studies show governs the age of onset of Huntington's disease.
- `connects-to` → **[NTRK / TrkB](../../03-molecular/ntrk/README.md)** — Mutant huntingtin impairs the cortical production and axonal transport of BDNF to the striatum, depriving striatal neurons of the TrkB-mediated trophic support whose loss drives their selective vulnerability and death.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Mutant huntingtin and released DAMPs activate microglial TLR4, driving the neuroinflammation that accompanies and accelerates the striatal neurodegeneration underlying the movement, cognitive, and psychiatric decline of Huntington's disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Mutant huntingtin sensitizes striatal NMDA receptors and disrupts mitochondrial calcium handling, so glutamate excitotoxicity floods medium spiny neurons with calcium—a central mechanism of their selective vulnerability in Huntington's.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by activated microglia in the Huntington's striatum amplifies the neuroinflammatory response, a microglial signal increasingly implicated as a driver of the neurodegeneration alongside the cell-autonomous huntingtin toxicity.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Mitochondrial dysfunction and xanthine-oxidase-derived reactive oxygen species add an oxidative burden to the striatal neurons in Huntington's, compounding the energy failure that the NRF2 antioxidant response struggles to offset.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — IGF-1 and BDNF (both mapped) signal through PI3K-AKT, and AKT phosphorylates huntingtin at serine-421 to reduce its toxicity—a neuroprotective axis that is impaired in Huntington's disease.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — The bioenergetic failure of Huntington's (ATP already mapped) activates AMPK, which both reflects the energy deficit and promotes the autophagic clearance (autophagy mapped) of mutant huntingtin aggregates.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — A shift in the BCL-2 family balance toward apoptosis engages the mitochondrial caspase pathway (caspase-3 mapped) that drives the death of striatal medium spiny neurons in Huntington's.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped) in microglia drives the neuroinflammation that accelerates striatal neurodegeneration in Huntington's disease.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 and interferon signaling through JAK-STAT (IL-6 already mapped) contributes to the central and peripheral inflammation characteristic of Huntington's disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling engaged downstream of BDNF-TrkB (both already mapped) is a pro-survival pathway whose impairment contributes to the vulnerability of striatal medium spiny neurons in Huntington's disease.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β dysregulation, downstream of impaired BDNF/AKT signaling (BDNF and AKT mapped), contributes to the neuronal dysfunction and death of Huntington's disease.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN regulation of the PI3K-AKT-mTOR axis (AKT and mTOR mapped) influences the autophagic clearance of mutant huntingtin and neuronal survival in Huntington's disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3-driven reactive astrogliosis is part of the neuroinflammatory response to striatal degeneration in Huntington's disease.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling (cGAS-STING already mapped) drives the interferon-responsive microglial activation of the neuroinflammation in Huntington's disease.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors (notably FOXO3) promote the autophagy and proteostasis that clear mutant huntingtin, a neuroprotective axis in Huntington's disease.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the neuroprotective-versus-inflammatory glial balance in the striatal degeneration of Huntington's disease.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation of Huntington's disease.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and mitochondrial stress responses contribute to the striatal neurodegeneration of Huntington's disease.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Aberrant CDK4/6-driven cell-cycle re-entry of post-mitotic neurons contributes to the neuronal death of Huntington's disease.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the neuronal survival pathways compromised in Huntington's disease.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of gene expression in Huntington's disease.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-p53 signaling (p53 already mapped) participates in the neuronal apoptosis of Huntington's disease.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (FYN) kinase signaling participates in the NMDA-receptor-mediated excitotoxicity and synaptic dysfunction of Huntington's disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven microglial and monocyte recruitment contributes to the neuroinflammation of Huntington's disease.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-linked calcium signaling participates in the excitotoxic neuronal dysfunction of Huntington's disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the microglial and neuroinflammatory responses of Huntington's disease.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses of Huntington's disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation of Huntington's disease.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of the neuronal gene programs of Huntington's disease.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (A2A receptor) signaling participates in the striatal-neuron dysfunction and neuroinflammation of Huntington's disease.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microglial activation and neuroinflammation of Huntington's disease.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Hypermetabolic weight loss: despite adequate intake, Huntington's disease causes progressive weight loss from a hypermetabolic state with impaired insulin signalling and mitochondrial energy failure (ATP already mapped), a metabolic feature tracking disease severity.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Energy dysregulation: falling fat stores and altered leptin signalling accompany the relentless weight loss of Huntington's disease, reflecting hypothalamic involvement and the systemic metabolic disturbance beyond the movement disorder.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Neuroinflammation: MHC class II is upregulated on activated microglia (already mapped) in the Huntington striatum, marking the neuroinflammatory response that accompanies and may accelerate the degeneration of medium spiny neurons.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac involvement: mutant huntingtin is expressed in the heart, and Huntington's disease carries a cardiomyopathy and autonomic dysfunction, with troponin elevation marking the myocardial injury that contributes to its cardiovascular mortality.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Excitotoxic injury: nitric oxide from neuronal nitric oxide synthase, driven by the glutamate excitotoxicity (already mapped), contributes with reactive oxygen species (xanthine oxidase already mapped) to the oxidative and nitrosative damage of the striatal neurons.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Metabolic wasting: the relentless weight loss of Huntington's disease reflects hypothalamic and metabolic dysfunction (insulin and leptin already mapped), and GLP-1-based agents are studied for the disturbed energy and glucose handling.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the activated microglia (already mapped) and the cyclooxygenase pathway contribute to the neuroinflammation (TNF, IL-6 and IL-1 already mapped) that accelerates the striatal neurodegeneration of Huntington's disease.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory counterweight: the anti-inflammatory IL-10 opposes the microglial pro-inflammatory response (TNF, IL-6 and IL-1 already mapped) driving the neurodegeneration, part of the neuroimmune balance in Huntington's disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — NMDA neuroprotection: magnesium blocks the NMDA receptor of the glutamate excitotoxicity (already mapped) that kills the striatal neurons, and its modulation is of interest for the excitotoxic injury of Huntington's disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Microglial polarisation: IL-4 polarises the microglia (already mapped) toward an anti-inflammatory M2 phenotype (IL-10 already mapped), the balance against the pro-inflammatory activation shaping the neuroinflammation of Huntington's disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglial arm whose balance against the pro-inflammatory signals (TNF, IL-1 and IL-6 already mapped) shapes the neurodegeneration of Huntington's disease.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Synaptic zinc: zinc modulates the glutamatergic (already mapped) synapses of the striatum, and the zinc dyshomeostasis of Huntington's disease contributes, with iron and copper (already mapped), to the metal-linked excitotoxic neurodegeneration.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Weight-loss adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the weight loss and metabolic (insulin already mapped) disturbance that are features of Huntington's disease.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — cGAS-STING neuroinflammation: type-I interferon, downstream of the cGAS-STING (already mapped) pathway activated by the mutant huntingtin (already mapped), drives the innate-immune neuroinflammation of Huntington's disease.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Hypermetabolism adipokine: resistin, with leptin and adiponectin (already mapped), is part of the adipokine milieu of the weight loss and hypermetabolism of Huntington's disease.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the infiltrating T cells (with the type-I interferon already mapped) is the type-II interferon arm of the peripheral-immune activation and neuroinflammation of Huntington's disease.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response of the systemic-immune activation accompanying the neurodegeneration of Huntington's disease.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive neuroinflammation: the cytotoxic T cells (perforin already mapped) infiltrate the neuroinflamed Huntington brain, the adaptive-immune component of the neurodegeneration.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the peripheral-immune dysregulation of Huntington's disease.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the peripheral-immune activation and neuroinflammation of Huntington's disease.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells of the peripheral and CNS-border immune compartments present antigen to the T cells (already mapped) of the neuroinflammation of Huntington's disease.
