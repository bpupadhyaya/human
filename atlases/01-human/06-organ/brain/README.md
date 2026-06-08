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
