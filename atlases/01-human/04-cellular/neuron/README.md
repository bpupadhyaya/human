---
schema: human-scale-entry/v1
id: neuron
name: Neuron
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-04
summary: "The electrically excitable cell that is the functional unit of the nervous system. ~86 billion in the adult human brain. Core morphology: soma, dendrites, axon, terminals. Propagates action potentials; integrates synaptic inputs to produce patterned output."
aliases: ["nerve cell", "neural cell", "dopaminergic neuron", "glutamatergic neuron", "GABAergic neuron", "interneuron", "motor neuron", "sensory neuron"]
sources:
  - id: azevedo-2009-neuron-count
    type: peer-reviewed
    cite: "Azevedo FA, Carvalho LR, Grinberg LT, et al. Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. J Comp Neurol. 2009;513(5):532-541."
    doi: "10.1002/cne.21974"
    pmid: "19226510"
  - id: kandel-principles
    type: textbook
    cite: "Kandel ER, Koester JD, Mack SH, Siegelbaum SA. Principles of Neural Science. 6th ed. McGraw-Hill; 2021."
    url: "https://www.mhprofessional.com/principles-of-neural-science-sixth-edition-9781259642234-usa"
    accessed: "2026-06-04"
  - id: bhatt-openstax-anatomy
    type: textbook
    cite: "OpenStax. Anatomy and Physiology 2e. Chapter 12: Introduction to the Nervous System. Rice University; 2022."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/12-1-basic-structure-and-function-of-the-nervous-system"
    accessed: "2026-06-04"
  - id: bhatt-hodgkin-huxley
    type: peer-reviewed
    cite: "Hodgkin AL, Huxley AF. A quantitative description of membrane current and its application to conduction and excitation in nerve. J Physiol. 1952;117(4):500-544."
    doi: "10.1113/jphysiol.1952.sp004764"
    pmid: "12991237"
cross_links:
  - target: 01-human/05-tissue/synapse
    relation: part-of
    note: "Neurons form the pre- and postsynaptic elements of synapses — synapses cannot exist without neurons."
  - target: 01-human/06-organ/brain
    relation: part-of
    note: "Neurons are the primary computational cells of the brain."
  - target: 01-human/07-system/nervous-system
    relation: part-of
    note: "Neurons are the fundamental cellular unit of the entire nervous system."
  - target: 01-human/03-molecular/dopamine
    relation: expresses
    note: "Dopaminergic neurons synthesize and release dopamine via tyrosine hydroxylase and DOPA decarboxylase."
  - target: 01-human/03-molecular/glutamate
    relation: expresses
    note: "Glutamatergic neurons — the most abundant class — synthesize and release glutamate."
  - target: 01-human/03-molecular/gaba
    relation: expresses
    note: "GABAergic interneurons synthesize GABA via GAD65/GAD67 and release it at inhibitory synapses."
  - target: 01-human/03-molecular/dopamine
    relation: modulated-by
    note: "Dopamine modulates neuronal excitability, plasticity, and firing patterns via D1–D5 receptors on neuron dendrites and soma."
  - target: 01-human/03-molecular/glutamate
    relation: modulated-by
    note: "Glutamate activates AMPA and NMDA receptors on neuronal dendrites, providing the primary excitatory drive and triggering LTP."
  - target: 01-human/03-molecular/gaba
    relation: modulated-by
    note: "GABA activates GABA-A and GABA-B receptors on neuronal soma and dendrites, providing inhibitory control."
  - target: 01-human/03-molecular/serotonin
    relation: expresses
    note: "Serotonergic neurons in the dorsal and median raphe nuclei synthesize 5-HT via TPH2 + AADC and project broadly to limbic, prefrontal, and cerebellar targets; raphe neurons provide ~5% of total body serotonin."
  - target: 01-human/02-atomic/sodium
    relation: modulated-by
    evidence: bhatt-hodgkin-huxley
    note: "Nav1.x channels generate the depolarising INa upstroke of neuronal action potentials; Na⁺/K⁺-ATPase restores gradient, consuming ~20–30% of neuronal ATP."
  - target: 01-human/02-atomic/potassium
    relation: modulated-by
    evidence: bhatt-hodgkin-huxley
    note: "Kv channels repolarise neuronal APs; Kir2.x maintains resting potential at ~−70 mV; hypokalaemia prolongs AP duration and predisposes to seizures."
  - target: 02-pathogen/05-prions/prion-protein
    relation: damaged-by
    evidence: kandel-principles
    note: "PrPSc templated misfolding accumulates as amyloid plaques in neural tissue, causing spongiform vacuolation, synaptic loss, and neuronal death in CJD/prion diseases."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: modulated-by
    evidence: kandel-principles
    note: "SERT (SLC6A4) on presynaptic serotonergic neurons reuptakes 5-HT from the synapse; SSRI blockade increases synaptic 5-HT, sustaining 5-HT1A/5-HT2A receptor activation and mediating antidepressant action."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: contains
    evidence: kandel-principles
    note: "SERT is an integral membrane protein of serotonergic neuron presynaptic terminals; it localises to lipid raft microdomains adjacent to the active zone and is regulated by PKC-mediated Thr616 phosphorylation and internalisation."
  - target: 02-pathogen/02-bacteria/clostridium-tetani
    relation: damaged-by
    evidence: kandel-principles
    note: "Tetanospasmin (TeNT) undergoes retrograde axonal transport to inhibitory interneurons, where VAMP-2 cleavage blocks GABA/glycine release, removing inhibitory control of α-motor neurons and causing spastic paralysis."
---

# Neuron

## Overview

The neuron is the **fundamental cellular unit of the nervous system** — an electrically excitable cell specialized to receive, integrate, and transmit information encoded as electrochemical signals. The adult human brain contains approximately **86 billion neurons** [^azevedo-2009-neuron-count], together forming roughly **100–500 trillion synaptic connections** — the most complex information-processing structure known to biology.

Each neuron is both a **computational unit** (integrating hundreds to thousands of simultaneous synaptic inputs) and a **communication node** (sending signals, via action potentials, over axons ranging from millimeters to over a meter in length). The precision and speed of this information transfer — action potentials propagating at 0.5 m/s (unmyelinated) to 120 m/s (heavily myelinated) — underlie all of nervous-system function: from the spinal reflex arc to the construction of conscious experience.

Neurons come in extraordinary variety — over 1,000 morphologically and molecularly distinct cell types have been identified in the mouse brain alone, and human diversity is likely greater. Yet all neurons share the same fundamental architecture and electrical excitability mechanism, first described quantitatively by Hodgkin and Huxley in 1952 [^bhatt-hodgkin-huxley] — work that earned the 1963 Nobel Prize in Physiology or Medicine.

## Structure

### Core morphological components

| Compartment | Description | Function |
|:---|:---|:---|
| **Soma (cell body)** | 5–100 μm diameter; contains nucleus, rough ER (Nissl bodies), mitochondria, Golgi | Site of protein synthesis, metabolic support; integrates distal dendritic inputs |
| **Dendrites** | Arborizing processes extending from soma; can span hundreds of micrometers; surface studded with dendritic spines (excitatory synapses) | **Input** compartment — receive and integrate synaptic signals; passive and active signal propagation toward soma |
| **Axon** | Single long process (up to 1 m in motor neurons); arises from the **axon initial segment (AIS)** | **Output** compartment — conducts action potentials from AIS to terminals; AIS is the spike initiation zone (highest density of Nav channels) |
| **Myelin sheath** | Oligodendrocyte (CNS) or Schwann cell (PNS) wraps; interrupted at **nodes of Ranvier** | Increases conduction velocity (saltatory conduction); reduces metabolic cost |
| **Axon terminals (boutons)** | Presynaptic endings containing synaptic vesicles, active zone scaffold, voltage-gated Ca²⁺ channels | Vesicle exocytosis → neurotransmitter release into synaptic cleft |
| **Dendritic spines** | Tiny mushroom-shaped protrusions on dendrites (~0.2–2 μm diameter) | Compartmentalize calcium and signaling for individual excitatory synapses; substrate of structural plasticity |

### Neuronal diversity

Neurons are classified by morphology, connectivity, and neurotransmitter identity:

**By morphology:**
- **Multipolar** — most CNS neurons; multiple dendrites, single axon (e.g., pyramidal cells, Purkinje cells)
- **Bipolar** — one dendrite + one axon (retinal ganglion cells, olfactory sensory neurons)
- **Unipolar/pseudounipolar** — single process bifurcating into peripheral and central branches (dorsal root ganglion cells)

**By function:**
- **Sensory (afferent) neurons** — transduce environmental stimuli → CNS
- **Motor (efferent) neurons** — CNS → muscle/gland output
- **Interneurons** — local circuit integration; ~99% of all CNS neurons

**By neurotransmitter:**
- **Glutamatergic** — excitatory; ~80% of cortical neurons; express VGLUT1/2
- **GABAergic** — inhibitory; ~20% of cortical neurons; express GAD65/67
- **Dopaminergic** — VTA, SNc, arcuate; express tyrosine hydroxylase (TH)
- **Serotonergic** — raphe nuclei; express tryptophan hydroxylase
- **Cholinergic** — basal forebrain, brainstem; express ChAT
- **Noradrenergic** — locus coeruleus; express TH + DBH

## Function

### Electrochemical signaling

Neurons maintain a **resting membrane potential** of approximately −70 mV (inside negative relative to outside), sustained by the Na⁺/K⁺-ATPase pump (3 Na⁺ out per 2 K⁺ in) and selective resting conductances (primarily K⁺ through Kir channels).

**Graded potentials** — receptor potentials in sensory neurons, synaptic potentials in interneurons and motor neurons — depolarize or hyperpolarize the membrane in proportion to stimulus intensity. These decay passively with distance but summate in space (spatial summation) and time (temporal summation) at the soma and AIS.

**Action potentials** — when the summed depolarization reaches threshold (~−55 mV) at the AIS, voltage-gated Na⁺ channels (Nav1.6 at the AIS) open in a regenerative cascade: Na⁺ influx → depolarization → more Nav open → spike peak at ~+40 mV. Rapid Nav inactivation and delayed K⁺ channel (Kv) opening repolarize the membrane, producing the characteristic ~1 ms action potential waveform. The action potential propagates without decrement down the axon [^bhatt-hodgkin-huxley].

**Saltatory conduction** — in myelinated axons, action potential currents "jump" between exposed nodes of Ranvier (spaced ~1–2 mm), greatly increasing conduction velocity (10–120 m/s) while reducing energy expenditure per conducted impulse.

### Synaptic integration

A typical cortical pyramidal neuron receives ~10,000 synaptic inputs on its dendrites. These inputs activate ligand-gated channels (glutamatergic EPSPs, GABAergic IPSPs) and modulate the neuron's excitability. The neuron computes a **weighted, time-varying sum** of these inputs, incorporating dendritic active conductances (voltage-gated Na⁺, Ca²⁺, K⁺) that can amplify or suppress distal inputs. The output is a stream of action potentials whose **firing rate** and **timing** encode the neuron's assessment of its inputs.

## Lifecycle

### Neurogenesis and migration

Most neurons are born during **embryonic and early postnatal neurogenesis**, in the ventricular and subventricular zones of the developing brain. Radial glial cells serve as neural stem cells; postmitotic neurons migrate along radial glial scaffolds to their final positions (inside-out lamination of the cortex). **Adult neurogenesis** — the production of new neurons from neural stem cells in the adult brain — is well-established in the hippocampal dentate gyrus (granule cells) and olfactory bulb in rodents; its extent in adult humans is actively debated.

### Differentiation and connectivity

After migration, neurons extend axons and dendrites guided by molecular cues (netrins, semaphorins, ephrins). Synaptic connections form between axon terminals and target dendrites/somas, initially in excess — approximately twice as many synapses form as are retained in the adult. **Synaptic pruning** (activity-dependent elimination via complement proteins, microglia) eliminates weak/inappropriate connections. The final wiring pattern is shaped by both genetic programs and experience-dependent activity.

### Maintenance and plasticity

Unlike most somatic cells, the majority of neurons in the adult brain are **post-mitotic** and long-lived — many persist for the lifetime of the organism. They require continuous metabolic support (oxygen, glucose — neurons have minimal glycogen stores and no fat reserves), trophic support (NGF, BDNF, NT-3), and active cytoskeletal maintenance for the integrity of their long axons (axonal transport via kinesin and dynein motors at 0.3–400 mm/day).

Structural **synaptic plasticity** — growth and retraction of dendritic spines, formation and elimination of synaptic contacts — persists throughout life as the cellular substrate of learning, memory, and recovery from injury.

### Neuronal death and degeneration

Neurons that lose trophic support undergo **apoptosis** (programmed cell death) — a major mechanism of developmental circuit refinement (Bcl-2 family / caspase pathway). In disease, neurons die by:
- **Excitotoxicity** (NMDA Ca²⁺ overload in stroke, TBI)
- **Apoptosis** (neurodegenerative disease — Parkinson's, Huntington's)
- **Necrosis** (acute hypoxia/ischemia)
- **Aggregation-induced toxicity** (amyloid, alpha-synuclein, tau in AD/PD)

Notably, the adult CNS has very limited regenerative capacity after neuronal death: lost neurons are generally not replaced, unlike peripheral nervous system axons (which can regenerate along Schwann cell scaffolds).

## Connections

- `part-of` → **[synapse](../../05-tissue/synapse/README.md)** — neurons form the pre- and postsynaptic elements of every synapse
- `part-of` → **[brain](../../06-organ/brain/README.md)** — neurons are the primary computational cells of the brain
- `part-of` → **[nervous-system](../../07-system/nervous-system/README.md)** — foundational cell type of all nervous system divisions
- `expresses` → **[dopamine](../../03-molecular/dopamine/README.md)** — dopaminergic neurons synthesize and release dopamine
- `expresses` → **[glutamate](../../03-molecular/glutamate/README.md)** — glutamatergic neurons release glutamate at excitatory synapses
- `expresses` → **[gaba](../../03-molecular/gaba/README.md)** — GABAergic interneurons synthesize and release GABA
- `modulated-by` → **[dopamine](../../03-molecular/dopamine/README.md)** — DA modulates neuronal excitability and plasticity via D1–D5 receptors
- `modulated-by` → **[glutamate](../../03-molecular/glutamate/README.md)** — Glu excites neurons through AMPA and NMDA receptors
- `modulated-by` → **[gaba](../../03-molecular/gaba/README.md)** — GABA inhibits neurons through GABA-A/B receptors

[^azevedo-2009-neuron-count]: Azevedo FA, Carvalho LR, Grinberg LT, et al. Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. *J Comp Neurol.* 2009;513(5):532-541. [doi:10.1002/cne.21974](https://doi.org/10.1002/cne.21974) · [PubMed 19226510](https://pubmed.ncbi.nlm.nih.gov/19226510/)
[^kandel-principles]: Kandel ER, Koester JD, Mack SH, Siegelbaum SA. *Principles of Neural Science.* 6th ed. McGraw-Hill; 2021.
[^bhatt-openstax-anatomy]: OpenStax. *Anatomy and Physiology 2e.* Chapter 12. Rice University; 2022. [openstax.org](https://openstax.org/books/anatomy-and-physiology-2e/pages/12-1-basic-structure-and-function-of-the-nervous-system)
[^bhatt-hodgkin-huxley]: Hodgkin AL, Huxley AF. A quantitative description of membrane current and its application to conduction and excitation in nerve. *J Physiol.* 1952;117(4):500-544. [doi:10.1113/jphysiol.1952.sp004764](https://doi.org/10.1113/jphysiol.1952.sp004764) · [PubMed 12991237](https://pubmed.ncbi.nlm.nih.gov/12991237/)
