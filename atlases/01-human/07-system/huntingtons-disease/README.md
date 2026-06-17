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
