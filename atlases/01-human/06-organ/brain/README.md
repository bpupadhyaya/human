---
schema: human-scale-entry/v1
id: brain
name: Brain
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-04
summary: "The ~1.4 kg central organ of the nervous system: site of cognition, perception, memory, emotion, and motor control. Contains ~86 billion neurons in 4 cortical lobes, subcortical nuclei, cerebellum, and brainstem. Protected by skull, meninges, and the blood-brain barrier."
aliases: ["encephalon", "cerebrum", "cerebral cortex", "human brain"]
sources:
  - id: kandel-principles-brain
    type: textbook
    cite: "Kandel ER, Koester JD, Mack SH, Siegelbaum SA. Principles of Neural Science. 6th ed. McGraw-Hill; 2021."
    url: "https://www.mhprofessional.com/principles-of-neural-science-sixth-edition-9781259642234-usa"
    accessed: "2026-06-04"
  - id: azevedo-2009-brain-cells
    type: peer-reviewed
    cite: "Azevedo FA, Carvalho LR, Grinberg LT, et al. Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. J Comp Neurol. 2009;513(5):532-541."
    doi: "10.1002/cne.21974"
    pmid: "19226510"
  - id: openstax-brain-ch13
    type: textbook
    cite: "OpenStax. Anatomy and Physiology 2e. Chapter 13: Anatomy of the Nervous System. Rice University; 2022."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/13-1-the-embryologic-perspective"
    accessed: "2026-06-04"
  - id: herculano-houzel-2009-human-brain
    type: peer-reviewed
    cite: "Herculano-Houzel S. The human brain in numbers: a linearly scaled-up primate brain. Front Hum Neurosci. 2009;3:31."
    doi: "10.3389/neuro.09.031.2009"
    pmid: "19915731"
cross_links:
  - target: 01-human/05-tissue/synapse
    relation: contains
    note: "The brain contains an estimated 100–500 trillion synapses — the functional junctions of its neural circuits."
  - target: 01-human/04-cellular/neuron
    relation: contains
    note: "The brain contains ~86 billion neurons distributed across cortical and subcortical structures."
  - target: 01-human/07-system/nervous-system
    relation: part-of
    note: "The brain is the principal organ of the central nervous system."
  - target: 01-human/03-molecular/dopamine
    relation: modulated-by
    note: "Dopamine regulates reward, motor control, cognition, and pituitary function via mesolimbic, mesocortical, nigrostriatal, and tuberoinfundibular pathways."
  - target: 01-human/03-molecular/glutamate
    relation: modulated-by
    note: "Glutamate drives the excitatory activity underlying perception, cognition, and memory at ~80% of brain synapses."
  - target: 01-human/03-molecular/gaba
    relation: modulated-by
    note: "GABA provides inhibitory control that maintains E/I balance, network oscillations, and circuit stability throughout the brain."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "The brain requires ~20% of resting cardiac output; cerebrovascular autoregulation and the baroreceptor reflex link brain and cardiovascular system."
  - target: 02-pathogen/05-prions/prion-protein
    relation: damaged-by
    evidence: kandel-principles-brain
    note: "PrPSc accumulation in brain parenchyma causes spongiform vacuolation, astrogliosis, and neuronal loss; CJD destroys cortex, thalamus, and cerebellum progressively"
  - target: 01-human/05-tissue/hippocampus
    relation: composed-of
    note: "Composed Of by Hippocampus."
  - target: 01-human/04-cellular/microglia
    relation: composed-of
    note: "Composed Of by Microglia."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: composed-of
    note: "Composed Of by Oligodendrocyte."
  - target: 01-human/04-cellular/astrocyte
    relation: composed-of
    note: "Composed Of by Astrocyte."
  - target: 02-pathogen/01-viruses/rabies-virus
    relation: damaged-by
    note: "Damaged by Rabies Virus (RABV)."
  - target: 02-pathogen/01-viruses/zika-virus
    relation: damaged-by
    note: "Damaged by Zika Virus (ZIKV)."
  - target: 02-pathogen/03-fungi/cryptococcus-neoformans
    relation: damaged-by
    note: "Damaged by Cryptococcus neoformans."
  - target: 02-pathogen/04-parasites/trypanosoma-brucei
    relation: damaged-by
    note: "Damaged by Trypanosoma brucei."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: damaged-by
    note: "Damaged by Toxoplasma gondii."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: damaged-by
    note: "Damaged by Neisseria meningitidis."
  - target: 02-pathogen/02-bacteria/listeria-monocytogenes
    relation: damaged-by
    note: "Damaged by Listeria monocytogenes."
  - target: 03-medicine/02-traditional/ginkgo-biloba
    relation: modulated-by
    note: "Modulated by Ginkgo biloba (EGb 761)."
  - target: 03-medicine/02-traditional/st-johns-wort
    relation: modulated-by
    note: "Modulated by St. John's Wort (Hypericum perforatum)."
  - target: 01-human/07-system/migraine
    relation: target-of
    note: "Migraine involves cortical spreading depression (CSD) as the aura generator in occipital cortex; hypothalamus drives prodromal symptoms; pain localizes to TNC and thalamus; PET identifies a brainstem migraine generator in dorsal raphe and PAG."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "ALS selectively degenerates upper motor neurons (primary motor cortex Betz cells) and their corticospinal projections; motor cortex hyperexcitability is an early feature; TDP-43 inclusions appear in motor cortex neurons in >97% of ALS; motor cortex atrophy is detectable by MRI."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "HD selectively atrophies striatum (caudate + putamen) detectable by MRI 15+ years pre-onset; cortical layer V and thalamic neurons also degenerate; lateral ventricle enlargement mirrors striatal atrophy and tracks disease progression by UHDRS total functional capacity."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "OCD is a CSTC circuit disorder: OFC/ACC hyperactivity drives excessive error detection; caudate hyperactivity disinhibits thalamocortical drive back to OFC → repetitive compulsions; SSRIs and ERP both normalize caudate hypermetabolism on PET, converging on the same circuit."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "ADHD involves PFC, anterior cingulate, and striatal circuit dysfunction; MRI shows ~3-5% smaller brain volume with 2-5 year maturation delay; default mode network fails to deactivate during tasks → attention lapses; PFC gray matter thinning correlates with ADHD severity."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "GAD involves amygdala hyperreactivity, vmPFC hypoactivity, and hippocampal volume reduction; fMRI shows increased amygdala-insula connectivity and failure of vmPFC to suppress amygdala fear responses; SSRIs and CBT both normalize amygdala reactivity on fMRI."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Panic disorder features BLA hyperreactivity to interoceptive and CO2 stimuli, insula hyperactivation, reduced vmPFC control over amygdala, and LC-NE dysregulation; CBT with interoceptive exposure normalizes amygdala-insula reactivity on fMRI over weeks."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "SAD features BLA hyperreactivity to social threat cues and reduced amygdala habituation; striatal hypoactivation during social reward; reduced vmPFC-amygdala inhibition; CBT with behavioral experiments normalizes amygdala-vmPFC connectivity on task-based fMRI."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "AUD weakens PFC-NAcc inhibitory control circuits; amygdala CRF hyperactivation drives negative reinforcement drinking; hippocampal neurogenesis is suppressed by chronic alcohol; partial brain volume recovery occurs after ≥6 months of sustained abstinence."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "OUD remodels VTA-NAcc reward circuits (MOR disinhibition), LC (NE rebound withdrawal), PFC control circuits (craving-driven approach), and amygdala (conditioned fear of withdrawal); buprenorphine and naltrexone normalize these circuit abnormalities over months of treatment."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Insomnia involves VLPO failure to silence arousal centers (LC, TMN, raphe, orexin neurons) — the flip-flop switch remains unstable; cortical hyperarousal at sleep onset on EEG (elevated beta power) is the core mechanism; CBT-I normalizes sleep-wake homeostasis."
  - target: 01-human/03-molecular/orexin
    relation: contains
    note: "Orexin neurons are confined to the lateral hypothalamus and project to LC, TMN, raphe, basal forebrain, and VTA; loss of ~70,000 orexin neurons in narcolepsy type 1 is the most precisely characterized lesion underlying a primary sleep disorder."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "AN shows gray matter reduction in OFC, insular cortex, and cingulate; fMRI reveals altered insula processing of food cues and reduced striatal reward responses; OFC hyperactivation drives cognitive rigidity; much gray matter recovers with weight restoration over 1-2 years."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "BPD features amygdala hyperreactivity to social threat and rejection cues, reduced vmPFC-amygdala inhibitory connectivity, and impaired PFC regulation; effective DBT treatment normalizes amygdala reactivity and increases PFC activation on fMRI over 12 months of treatment."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "MOR expressed in PAG (descending analgesia), VTA (euphoria via DA disinhibition), LC (arousal/withdrawal), NAcc (reinforcement), amygdala (aversion), and pre-Bötzinger complex (respiratory rhythm depression); MOR distribution explains opioids' broad opposing CNS effects."
  - target: 01-human/07-system/bulimia-nervosa
    relation: connects-to
    note: "BN involves insula dysfunction (impaired interoceptive satiety signaling), reduced ventral PFC inhibitory control, striatal reward dysregulation, and ACC conflict monitoring deficits; CBT-BN and fluoxetine both normalize PFC-striatal connectivity on fMRI."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Stimulant use disorders remodel VTA-NAcc circuits (ΔFosB, D2R loss), PFC (gray matter thinning, ↓ inhibitory control), and amygdala (cue craving); PET shows reduced DAT and D2R; meth causes DAT terminal destruction detectable on dopamine transporter imaging."
  - target: 01-human/03-molecular/adenosine
    relation: modulated-by
    note: "Basal forebrain adenosine accumulates during waking → builds sleep pressure via A1R/A2AR on arousal neurons; caffeine (A1R/A2AR antagonist) blocks this pressure; adenosine A1R also mediates neuroprotection during ischemia by suppressing excitotoxic glutamate release."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "PTSD remodels the amygdala-vmPFC-hippocampus fear circuit: BLA hyperactivation, vmPFC extinction failure, hippocampal volume loss (~8%); PET/fMRI shows ↑ amygdala and ↓ mPFC activation to trauma cues; prolonged exposure therapy normalizes amygdala-vmPFC connectivity."
  - target: 01-human/03-molecular/crh
    relation: modulated-by
    note: "CRH neurons in central amygdala (CeA) and BNST coordinate fear expression and anticipatory anxiety independent of the HPA axis; BNST CRH mediates sustained anxiety; hippocampal GR provides slow negative feedback on PVN CRH synthesis; disruption underlies PTSD and AUD."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "CB1R is among the most abundant brain GPCRs — densest in basal ganglia, cerebellum, hippocampus, and cortex; retrograde 2-AG/AEA mediates DSI/DSE synaptic plasticity; hippocampal CB1R enables fear extinction LTD; chronic THC-driven CB1R downregulation is measurable by PET."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Chronic heavy cannabis use reduces hippocampal and amygdala gray matter; PFC thinning correlates with cognitive impairment; CB1R downregulation on PET persists 4+ weeks after abstinence; adolescent-onset use causes greater structural brain changes than adult onset."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Gambling disorder features OFC hyperactivation, vmPFC hypoactivation, reduced ventral striatum response to wins, and diminished ACC conflict monitoring; impaired PFC-striatum inhibitory control distinguishes disordered from recreational gambling."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "FM involves thalamic hypersensitivity, ACC and insula hyperactivation to pain (fMRI), and altered DMN connectivity; MRS shows elevated insula glutamate; gray matter reductions in dlPFC and ACC correlate with chronicity; changes partially reverse with effective treatment."
  - target: 01-human/07-system/internet-gaming-disorder
    relation: connects-to
    note: "IGD features OFC hyperactivation to game cues, vmPFC hypoactivation, reduced ventral striatum response to non-gaming rewards, and diminished ACC impulse control; structural MRI shows reduced dlPFC gray matter — consistent with impaired top-down inhibitory control."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "SP is expressed in dorsal horn C-fiber terminals (pain), amygdala (fear/stress), raphe nuclei (co-release with 5-HT), and brainstem vagal circuits; NK1R spans pain, vomiting, and emotion circuits; NK1R internalization marks C-fiber nociceptive activation histologically."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "BED features OFC hyperactivation to food cues (paralleling drug cue reactivity), impaired vmPFC inhibitory control over binge impulses, insula hyperactivation during food craving, and dorsal striatum hypoactivation reflecting habitual eating."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Neuropathic pain involves thalamic sensitization, ACC/insula hyperactivation, and somatosensory cortex reorganization; chronic pain reduces gray matter in ACC and dlPFC; CNS changes explain pain persistence despite peripheral healing and maladaptive neuroplasticity."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "NT1 selectively destroys lateral hypothalamic orexin neurons, destabilizing the VLPO-arousal flip-flop switch; TMN histamine, LC norepinephrine, and raphe serotonin projections are all under-driven; pontine REM-on/off circuit dysregulation underlies cataplexy."
  - target: 01-human/03-molecular/melatonin
    relation: modulated-by
    note: "Pineal melatonin is regulated by SCN via RHT → SCG → NE → β1 → AANAT; MT2 on SCN neurons mediates circadian phase shifts; melanopsin ipRGC input suppresses SCN-driven melatonin — the molecular basis of light-hygiene recommendations."
  - target: 01-human/03-molecular/acth
    relation: secretes
    note: "Anterior pituitary corticotrophs produce ACTH from POMC via PC1/3 cleavage; SCN → PVN CRH pulsatility drives ACTH circadian rhythm with morning peak; hypothalamic POMC neurons (arcuate nucleus) produce α-MSH acting on MC4R to regulate appetite — a parallel POMC-derived system."
  - target: 01-human/03-molecular/npy
    relation: contains
    note: "NPY is the most abundant CNS neuropeptide; ARC NPY/AgRP neurons drive hunger via Y1R/Y5R on PVN; CeA NPY-Y1R circuits are anxiolytic; hippocampal NPY interneurons suppress mossy fiber bursting and set seizure threshold; LC NPY-Y2R attenuates NE stress hyperactivation."
---

# Brain

## Overview

The human brain is the **most complex biological organ known to science** — a ~1.4 kg (3.1 lb) structure that serves as the seat of all conscious experience, cognition, memory, emotion, language, and voluntary movement. It is also the master regulatory organ for visceral function, endocrine secretion, and behavioral state. Despite representing only ~2% of body weight, the brain consumes approximately **20% of the body's resting metabolic energy** — almost entirely in the form of glucose and oxygen delivered by continuous blood flow (~750 mL/min).

The brain contains approximately **86 billion neurons** [^azevedo-2009-brain-cells] — a number essentially equal to the ~85 billion non-neuronal cells (predominantly glia: astrocytes, oligodendrocytes, microglia). Each neuron makes, on average, ~7,000 synaptic connections, yielding a total synaptic count estimated at 100–500 trillion. This connectivity underlies the brain's extraordinary information-processing capacity — and the intricacy of the disorders that result when it is disrupted.

The brain's critical importance is reflected in its multiple layers of protection: a rigid bony skull, three meningeal layers (dura, arachnoid, pia), cerebrospinal fluid (CSF) cushioning, and the **blood-brain barrier (BBB)** — a specialized endothelial tight-junction barrier that selectively controls which molecules enter the CNS parenchyma.

## Structure

### Major anatomical divisions

| Division | Key structures | Core functions |
|:---|:---|:---|
| **Cerebral cortex** | Frontal, parietal, temporal, occipital lobes; 6 cortical layers; ~2–4 mm thick; ~145,000 mm² surface area (highly folded) | Higher cognition, sensory perception, voluntary motor control, language, executive function |
| **Frontal lobe** | Primary motor cortex (M1), premotor, supplementary motor; prefrontal cortex (PFC); Broca's area | Motor planning and execution; executive function, working memory, decision-making; speech production |
| **Parietal lobe** | Primary somatosensory cortex (S1); posterior parietal cortex | Somatosensory processing; spatial orientation; sensorimotor integration |
| **Temporal lobe** | Primary auditory cortex; Wernicke's area; fusiform gyrus; entorhinal cortex | Auditory processing; language comprehension; face/object recognition; memory encoding (via hippocampus) |
| **Occipital lobe** | Primary visual cortex (V1); extrastriate areas V2–V5 (MT/V5 for motion; V4 for color) | Visual perception and processing |
| **Basal ganglia** | Striatum (caudate + putamen), globus pallidus, subthalamic nucleus, substantia nigra | Motor program selection, habit formation, reward-based learning; direct and indirect pathways |
| **Hippocampus** | CA1, CA3, dentate gyrus, subiculum (medial temporal lobe) | Episodic memory encoding (declarative), spatial navigation, pattern completion and separation |
| **Amygdala** | Basolateral, central, medial nuclei | Fear conditioning, emotional memory, threat appraisal, social cognition |
| **Thalamus** | Lateral geniculate (vision), medial geniculate (audition), VPL/VPM (somatosensory), mediodorsal (PFC relay), pulvinar | Sensory relay and gating to cortex; corticothalamic loops for attention and consciousness |
| **Hypothalamus** | Arcuate, paraventricular, suprachiasmatic, lateral hypothalamic nuclei | Homeostasis (temperature, hunger, thirst, sleep-wake); endocrine axis control (HPA, HPT, HPG); circadian rhythm |
| **Cerebellum** | Cortex (Purkinje cells, granule cells), deep cerebellar nuclei | Motor coordination, balance, timing, procedural learning; emerging evidence for cognitive roles |
| **Brainstem** | Midbrain (VTA, SNc, superior colliculus); pons (locus coeruleus, raphe); medulla (cardiovascular/respiratory centers) | Arousal; monoaminergic nuclei (DA, NE, 5-HT); vital reflex control (breathing, HR, BP) |

### Gray matter vs. white matter

- **Gray matter**: Contains neuronal cell bodies, dendrites, synapses, and unmyelinated axons. Found in cortex, basal ganglia, thalamus, and cerebellar cortex. Site of local computation.
- **White matter**: Dense tracts of myelinated axons connecting gray matter regions. Major tracts: corpus callosum (interhemispheric), internal capsule (corticospinal/thalamocortical), arcuate fasciculus (language), uncinate fasciculus (temporal-frontal). White matter constitutes ~60% of brain volume.

### Blood supply and the blood-brain barrier

The brain receives arterial blood via the **internal carotid arteries** (anterior circulation) and **vertebral arteries** (posterior circulation), joined at the **Circle of Willis**. Cerebrovascular autoregulation maintains constant cerebral blood flow (CBF ~50 mL/100 g/min) across a wide range of arterial blood pressures (MAP 60–160 mmHg).

The **blood-brain barrier (BBB)** consists of specialized endothelial cells with tight junctions (claudins, occludins), surrounded by pericytes and astrocytic endfeet. The BBB restricts passage of polar molecules, charged species, and most large proteins while permitting lipid-soluble molecules and those with specific transporters. It is a major obstacle to CNS drug delivery — most therapeutic molecules do not cross the BBB.

## Function

### Cognition and consciousness

The **prefrontal cortex** orchestrates executive functions: working memory, planning, cognitive flexibility, impulse control, and decision-making under uncertainty. The **default mode network** (medial PFC, posterior cingulate, angular gyrus) is active during mind-wandering, self-referential thought, and episodic memory retrieval.

Consciousness requires the **thalamocortical system**: continuous, synchronized activity between thalamus and widespread cortical areas. Disruption of this system — by anesthesia, sleep, seizure, or structural damage — impairs consciousness.

### Memory systems

| Memory type | Neural substrate | Mechanism |
|:---|:---|:---|
| **Episodic (declarative)** | Hippocampus → entorhinal cortex → neocortex | LTP-based encoding; hippocampal-dependent initially; systems consolidation to cortex over weeks |
| **Semantic** | Anterior temporal lobe, neocortex | Distributed cortical representations |
| **Procedural/motor** | Basal ganglia (habit), cerebellum (motor sequence) | Dopaminergic reward learning; cerebellar error correction |
| **Fear/emotional** | Amygdala (BLA) → hippocampus | Pavlovian fear conditioning; emotional modulation of hippocampal encoding |
| **Working memory** | Dorsolateral PFC | Persistent activity in layer III pyramidal neuron circuits; DA D1 optimization |

### Motor control

The corticospinal tract carries voluntary motor commands from M1 (layer V Betz cells) down through internal capsule → brainstem → spinal cord → lower motor neurons → muscle. The **basal ganglia** select and gate motor programs (via direct and indirect pathways, modulated by dopamine from SNc). The **cerebellum** computes prediction errors and fine-tunes motor execution.

## Connections

- `contains` → **[synapse](../../05-tissue/synapse/README.md)** — ~100–500 trillion synaptic junctions form the brain's connectivity
- `contains` → **[neuron](../../04-cellular/neuron/README.md)** — ~86 billion neurons are the computing cells of the brain
- `part-of` → **[nervous-system](../../07-system/nervous-system/README.md)** — the brain is the principal CNS organ
- `modulated-by` → **[dopamine](../../03-molecular/dopamine/README.md)** — dopamine shapes reward, motor, cognitive, and endocrine circuits
- `modulated-by` → **[glutamate](../../03-molecular/glutamate/README.md)** — glutamate provides the dominant excitatory drive across all brain circuits
- `modulated-by` → **[gaba](../../03-molecular/gaba/README.md)** — GABA provides circuit-stabilizing inhibition
- `connects-to` → **[cardiovascular-system](../../07-system/cardiovascular-system/README.md)** — the brain consumes ~20% of cardiac output; autoregulation and baroreceptor reflex link the two systems
- `targeted-by` → **[Migraine](../../07-system/migraine/README.md)** — migraine involves cortical spreading depression (CSD) as the aura generator in occipital cortex; hypothalamus drives prodromal symptoms; pain localizes to TNC and thalamus; PET identifies a brainstem migraine generator in dorsal raphe and PAG.
- `connects-to` → **[ALS](../../07-system/als/README.md)** — ALS selectively degenerates upper motor neurons (primary motor cortex Betz cells) and their corticospinal projections; motor cortex hyperexcitability is an early feature; TDP-43 inclusions appear in motor cortex neurons in >97% of ALS; motor cortex atrophy is detectable by MRI.
- `connects-to` → **[Huntington Disease](../../07-system/huntingtons-disease/README.md)** — HD selectively atrophies striatum (caudate + putamen) detectable by MRI 15+ years pre-onset; cortical layer V and thalamic neurons also degenerate; lateral ventricle enlargement mirrors striatal atrophy and tracks disease progression by UHDRS-TFC.
- `connects-to` → **[Obsessive-Compulsive Disorder](../../07-system/obsessive-compulsive-disorder/README.md)** — OCD is a CSTC circuit disorder: OFC/ACC hyperactivity drives excessive error detection; caudate nucleus hyperactivity disinhibits thalamocortical drive back to OFC → repetitive compulsive behaviors; SSRIs and ERP both normalize caudate hypermetabolism on PET.
- `connects-to` → **[ADHD](../../07-system/attention-deficit-hyperactivity-disorder/README.md)** — ADHD involves PFC, anterior cingulate, and striatal circuit dysfunction; MRI shows ~3-5% smaller total brain volume with 2-5 year cortical maturation delay; default mode network fails to deactivate during tasks → attention lapses; PFC gray matter thinning correlates with ADHD severity.
- `connects-to` → **[Generalized Anxiety Disorder](../../07-system/generalized-anxiety-disorder/README.md)** — GAD involves amygdala hyperreactivity, vmPFC hypoactivity, and hippocampal volume reduction (~5-8%); fMRI shows increased amygdala-insula connectivity and failure of vmPFC to suppress amygdala fear responses; SSRIs and CBT both normalize amygdala reactivity.
- `connects-to` → **[Panic Disorder](../../07-system/panic-disorder/README.md)** — panic disorder features BLA hyperreactivity to interoceptive and CO2 stimuli, insula hyperactivation, reduced vmPFC control over amygdala, and LC-NE dysregulation; CBT with interoceptive exposure normalizes amygdala-insula reactivity on fMRI over 12+ weeks.
- `connects-to` → **[Social Anxiety Disorder](../../07-system/social-anxiety-disorder/README.md)** — SAD features BLA hyperreactivity to social threat cues and reduced amygdala habituation to repeated faces; striatal hypoactivation during social reward; reduced vmPFC-amygdala inhibition; CBT normalizes amygdala-vmPFC connectivity on task-based fMRI.
- `connects-to` → **[Alcohol Use Disorder](../../07-system/alcohol-use-disorder/README.md)** — AUD weakens PFC-NAcc inhibitory control circuits; amygdala CRF hyperactivation drives negative reinforcement drinking; hippocampal neurogenesis is suppressed by chronic alcohol; partial brain volume recovery occurs after ≥6 months of sustained abstinence.
- `connects-to` → **[Opioid Use Disorder](../../07-system/opioid-use-disorder/README.md)** — OUD remodels VTA-NAcc reward circuits (MOR disinhibition), LC (NE rebound withdrawal), PFC control circuits (craving-driven approach behavior), and amygdala (conditioned fear of withdrawal); buprenorphine and naltrexone normalize these abnormalities over months of treatment.
- `connects-to` → **[Insomnia Disorder](../../07-system/insomnia-disorder/README.md)** — insomnia involves VLPO failure to silence arousal centers (LC, TMN, raphe, orexin neurons) — the flip-flop switch remains unstable; cortical hyperarousal at sleep onset (elevated EEG beta power) is the core mechanism; CBT-I normalizes sleep-wake homeostasis.
- `contains` → **[Orexin](../../03-molecular/orexin/README.md)** — orexin neurons are confined to the lateral hypothalamus and project broadly to LC, TMN, raphe, basal forebrain, and VTA; loss of ~70,000 orexin neurons in narcolepsy type 1 is the most precisely characterized lesion in a primary sleep disorder.
- `connects-to` → **[Anorexia Nervosa](../../07-system/anorexia-nervosa/README.md)** — AN shows gray matter reduction in OFC, insular cortex, and cingulate; fMRI reveals altered insula processing of food cues and reduced striatal reward responses; OFC hyperactivation drives cognitive rigidity; much gray matter recovers with weight restoration over 1-2 years.
- `connects-to` → **[Borderline Personality Disorder](../../07-system/borderline-personality-disorder/README.md)** — BPD features amygdala hyperreactivity to social threat and rejection cues, reduced vmPFC-amygdala inhibitory connectivity, and impaired PFC regulation; effective DBT treatment normalizes amygdala reactivity and increases PFC activation on fMRI over 12 months.
- `connects-to` → **[Mu-Opioid Receptor](../../03-molecular/mu-opioid-receptor/README.md)** — MOR expressed in PAG (descending analgesia), VTA (euphoria via DA disinhibition), LC (arousal/withdrawal), NAcc (reinforcement), amygdala (aversion), and pre-Bötzinger complex (respiratory depression); MOR distribution explains opioids' broad opposing CNS effects.
- `connects-to` → **[Bulimia Nervosa](../../07-system/bulimia-nervosa/README.md)** — BN involves insula dysfunction (impaired interoceptive satiety signaling), reduced ventral PFC inhibitory control, striatal D3R/D2R reward dysregulation, and ACC conflict monitoring deficits; CBT-BN and fluoxetine both normalize PFC-striatal connectivity on fMRI.
- `connects-to` → **[Stimulant Use Disorder](../../07-system/stimulant-use-disorder/README.md)** — stimulant use disorders remodel VTA-NAcc circuits (ΔFosB, D2R loss), PFC (gray matter thinning, ↓ inhibitory control), and amygdala (cue-conditioned craving); PET shows reduced DAT and D2R in striatum; meth causes DAT terminal destruction detectable on dopamine transporter imaging.
- `modulated-by` → **[Adenosine](../../03-molecular/adenosine/README.md)** — basal forebrain adenosine accumulates during waking → builds homeostatic sleep pressure via A1R/A2AR on arousal-promoting neurons; caffeine blocks this pressure; A1R also mediates neuroprotection during ischemia by suppressing excitotoxic glutamate release.

- `connects-to` → **[PTSD](../../07-system/ptsd/README.md)** — PTSD remodels the amygdala-vmPFC-hippocampus fear circuit: BLA hyperactivation, vmPFC extinction failure, and hippocampal volume loss (~8%); PET/fMRI shows ↑ amygdala and ↓ mPFC activation to trauma cues; prolonged exposure therapy normalizes amygdala-vmPFC functional connectivity.

- `modulated-by` → **[CRH](../../03-molecular/crh/README.md)** — CRH neurons in CeA and BNST coordinate fear expression and sustained anticipatory anxiety independent of HPA axis cortisol; BNST CRH mediates contextual anxiety; hippocampal glucocorticoid receptors provide slow negative feedback on PVN CRH synthesis; disruption underlies PTSD and AUD.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — CB1R is among the most abundant GPCRs in the brain, densest in basal ganglia, cerebellum, hippocampus, and cortex; retrograde 2-AG/AEA endocannabinoid signaling mediates DSI/DSE synaptic plasticity; hippocampal CB1R enables fear extinction LTD; chronic THC causes CB1R downregulation measurable by PET.
- `connects-to` → **[Cannabis Use Disorder](../../07-system/cannabis-use-disorder/README.md)** — chronic heavy cannabis use reduces hippocampal and amygdala gray matter volume; PFC thinning correlates with cognitive impairment; CB1R downregulation on PET persists 4+ weeks post-abstinence; adolescent-onset use causes greater structural brain changes than adult onset.
- `connects-to` → **[Gambling Disorder](../../07-system/gambling-disorder/README.md)** — gambling disorder features OFC hyperactivation (overvaluation of rewards), vmPFC hypoactivation, reduced ventral striatum response to wins, and diminished ACC conflict monitoring; impaired PFC-striatum inhibitory control is the neurobiological signature distinguishing disordered from recreational gambling.
- `connects-to` → **[Fibromyalgia](../../07-system/fibromyalgia/README.md)** — FM involves thalamic hypersensitivity, ACC and posterior insula hyperactivation to pain stimuli (fMRI), and altered default mode network connectivity; MRS shows elevated glutamate in posterior insula correlating with pain severity; gray matter reductions in dlPFC and ACC correlate with chronicity and partially reverse with effective treatment.
- `connects-to` → **[Internet Gaming Disorder](../../07-system/internet-gaming-disorder/README.md)** — IGD features OFC hyperactivation to game cues, vmPFC hypoactivation, reduced ventral striatum response to non-gaming rewards, and diminished ACC impulse control; structural MRI shows reduced gray matter in dlPFC and OFC — consistent with chronic dopamine-driven reward circuit remodeling.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — SP is expressed in spinal dorsal horn (pain transmission from C-fibers), amygdala (fear/stress), raphe nuclei (co-release with 5-HT), striatum, and brainstem vagal circuits; NK1R is widely distributed in pain, emotion, and vomiting circuits; NK1R internalization is a validated histological marker of C-fiber nociceptive activation.
- `connects-to` → **[Binge Eating Disorder](../../07-system/binge-eating-disorder/README.md)** — BED features OFC hyperactivation to food cues (paralleling drug cue reactivity in SUD), impaired vmPFC inhibitory control over binge impulses, insula hyperactivation during food craving, and dorsal striatum hypoactivation reflecting a shift from goal-directed to habitual eating patterns.
- `connects-to` → **[Neuropathic Pain](../../07-system/neuropathic-pain/README.md)** — neuropathic pain involves thalamic sensitization, ACC and insular hyperactivation to pain stimuli, and somatosensory cortex reorganization; chronic neuropathic pain is associated with gray matter reduction in ACC and dlPFC; central changes explain why pain persists after peripheral healing and why maladaptive neuroplasticity becomes the dominant driver.
- `connects-to` → **[Narcolepsy](../../07-system/narcolepsy/README.md)** — NT1 selectively destroys lateral hypothalamic orexin neurons, destabilizing the VLPO–arousal flip-flop; under-driven TMN, LC, and raphe projections reduce histamine, NE, and 5-HT arousal tone; pontine REM-on/off circuit dysregulation underlies cataplexy; amygdala hypersensitivity mediates emotion-triggered cataplexy attacks.
- `modulated-by` → **[Melatonin](../../03-molecular/melatonin/README.md)** — the pineal gland (brain appendage) secretes melatonin under SCN circadian control via the retinohypothalamic tract → superior cervical ganglion → NE → β1-AR → AANAT; SCN MT2 receptors mediate melatonin-driven circadian phase shifts; melanopsin ipRGC blue-light input suppresses SCN-driven melatonin — the molecular basis of light-hygiene recommendations for sleep.
- `secretes` → **[ACTH](../../03-molecular/acth/README.md)** — anterior pituitary corticotrophs (derived from POMC by PC1/3 cleavage) release ACTH whose circadian rhythm is driven by SCN → PVN CRH pulsatility; simultaneously, hypothalamic arcuate nucleus POMC neurons produce α-MSH acting on MC4R → appetite suppression and energy balance — a parallel POMC-derived neuroendocrine system originating in the brain.
- `contains` → **[NPY](../../03-molecular/npy/README.md)** — NPY is the most abundant CNS neuropeptide; ARC NPY/AgRP neurons drive hunger via Y1R/Y5R on PVN; CeA NPY-Y1R circuits are anxiolytic; hippocampal NPY interneurons suppress mossy fiber bursting and set seizure threshold; LC NPY-Y2R attenuates NE stress hyperactivation.

## Pathology

| Disease | Core mechanism | Prevalence / Burden |
|:---|:---|:---|
| **Stroke** | Ischemic (~87%): embolic or thrombotic occlusion → excitotoxic infarction; Hemorrhagic (~13%): vessel rupture | #2 cause of death globally; ~15 million cases/year |
| **Alzheimer's disease** | Amyloid-β plaque deposition, tau neurofibrillary tangles → synaptic loss → neurodegeneration; hippocampus first | ~50 million affected globally; leading cause of dementia |
| **Parkinson's disease** | Selective loss of SNc dopaminergic neurons → striatal dopamine depletion → motor circuit dysfunction | ~10 million globally; tremor, rigidity, bradykinesia |
| **Epilepsy** | E/I imbalance → seizure generation and propagation (can be focal or generalized) | ~50 million globally; 30% drug-resistant |
| **Glioblastoma (GBM)** | Grade IV astrocytoma; diffusely infiltrating; IDH-wildtype; median survival ~15 months even with treatment | ~3/100,000/year; most lethal primary brain tumor |
| **Depression** | Monoamine/glutamate/neuroinflammation hypothesis; PFC hypoactivity, amygdala hyperactivity | ~280 million globally; leading disability cause |
| **Schizophrenia** | NMDA hypofunction + dopamine dysregulation; PV interneuron loss → gamma synchrony deficits | ~24 million globally; 0.3–0.7% lifetime prevalence |
| **Traumatic brain injury (TBI)** | Mechanical disruption → excitotoxicity, inflammation, axonal shear injury | ~70 million/year globally; #1 cause of disability in young adults |

[^kandel-principles-brain]: Kandel ER, Koester JD, Mack SH, Siegelbaum SA. *Principles of Neural Science.* 6th ed. McGraw-Hill; 2021.
[^azevedo-2009-brain-cells]: Azevedo FA, Carvalho LR, Grinberg LT, et al. Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. *J Comp Neurol.* 2009;513(5):532-541. [doi:10.1002/cne.21974](https://doi.org/10.1002/cne.21974) · [PubMed 19226510](https://pubmed.ncbi.nlm.nih.gov/19226510/)
[^openstax-brain-ch13]: OpenStax. *Anatomy and Physiology 2e.* Chapter 13. Rice University; 2022. [openstax.org](https://openstax.org/books/anatomy-and-physiology-2e/pages/13-1-the-embryologic-perspective)
[^herculano-houzel-2009-human-brain]: Herculano-Houzel S. The human brain in numbers: a linearly scaled-up primate brain. *Front Hum Neurosci.* 2009;3:31. [doi:10.3389/neuro.09.031.2009](https://doi.org/10.3389/neuro.09.031.2009) · [PubMed 19915731](https://pubmed.ncbi.nlm.nih.gov/19915731/)
