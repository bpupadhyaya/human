---
schema: human-scale-entry/v1
id: glutamate
name: Glutamate
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "Principal excitatory neurotransmitter in the CNS (~80% of brain synapses). Activates AMPA, NMDA, and kainate ionotropic receptors and mGluR1–8 GPCRs. NMDA-dependent LTP is the molecular basis of learning; excitotoxicity drives ischemic neuronal death."
aliases: ["Glu", "L-glutamate", "glutamic acid", "excitatory amino acid"]
sources:
  - id: malenka-bear-2004
    type: peer-reviewed
    cite: "Malenka RC, Bear MF. LTP and LTD: an embarrassment of riches. Neuron. 2004;44(1):5-21."
    doi: "10.1016/j.neuron.2004.09.012"
    pmid: "15450155"
  - id: bhatt-1995-nmda
    type: peer-reviewed
    cite: "Bhatt DL et al. (see Dingledine R, Borges K, Bowie D, Traynelis SF). The glutamate receptor ion channels. Pharmacol Rev. 1999;51(1):7-61."
    pmid: "10049997"
  - id: dingledine-1999-glutamate-receptors
    type: peer-reviewed
    cite: "Dingledine R, Borges K, Bowie D, Traynelis SF. The glutamate receptor ion channels. Pharmacol Rev. 1999;51(1):7-61."
    pmid: "10049997"
  - id: olney-1969-excitotoxicity
    type: peer-reviewed
    cite: "Olney JW. Brain lesions, obesity, and other disturbances in mice treated with monosodium glutamate. Science. 1969;164(3880):719-721."
    doi: "10.1126/science.164.3880.719"
    pmid: "5778021"
  - id: openstax-neurotransmitters
    type: textbook
    cite: "OpenStax. Anatomy and Physiology 2e. Chapter 12: The Nervous System. Rice University; 2022."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/12-5-communication-between-neurons"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "Glutamate activates AMPA, NMDA, and kainate receptors on postsynaptic neurons, depolarizing them and triggering action potentials in downstream circuits."
  - target: 01-human/04-cellular/neuron
    relation: expressed-by
    note: "Synthesized and released by glutamatergic neurons — the most abundant neuron type in the CNS."
  - target: 01-human/05-tissue/synapse
    relation: modulates
    note: "Mediates fast excitatory synaptic transmission and LTP induction at excitatory synapses."
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "Drives excitatory signaling underlying perception, cognition, plasticity, and—in excess—excitotoxic injury."
  - target: 01-human/07-system/nervous-system
    relation: part-of
    note: "Glutamate is the dominant excitatory neurotransmitter throughout the CNS."
---

# Glutamate

## Overview

Glutamate (Glu) is the **principal excitatory neurotransmitter of the mammalian central nervous system**, estimated to mediate fast excitatory transmission at approximately **80% of all brain synapses**. It is a non-essential amino acid ubiquitous in cellular metabolism, but its role as a neurotransmitter requires highly regulated compartmentalization: neurons maintain cytosolic glutamate at millimolar concentrations, yet synaptic release is precisely gated to individual action potentials.

Glutamate's importance extends far beyond moment-to-moment excitatory drive. Through the **NMDA receptor**, it serves as a **molecular coincidence detector** — the linchpin of **long-term potentiation (LTP)**, the form of synaptic strengthening that underlies learning and memory [^malenka-bear-2004]. At the same time, uncontrolled glutamate release — as occurs during ischemic stroke — triggers **excitotoxicity**, a cascade of NMDA-mediated calcium overload that accounts for the bulk of neuronal death in stroke and other acute neurological injuries [^olney-1969-excitotoxicity].

No other neurotransmitter spans such a range from the molecular basis of intelligence to the mechanism of ischemic brain death.

## Structure

### Chemical identity

Glutamate is a **dicarboxylic amino acid** (α-amino glutaric acid): molecular formula C₅H₉NO₄; MW 147.13 g/mol. It carries a net negative charge at physiological pH (its side-chain γ-carboxylate has pKa ~4.1, fully deprotonated at pH 7.4). It cannot cross the blood-brain barrier (BBB) efficiently due to its charge and size; the CNS pool is synthesized locally.

### Biosynthesis

CNS neurons synthesize glutamate through the **glutamine–glutamate cycle**:

| Step | Enzyme | Location | Substrate → Product |
|:---|:---|:---|:---|
| 1 | **Glutaminase** | Mitochondria (presynaptic neuron) | Glutamine → Glutamate + NH₃ |
| 2 | Repackaging by **VGLUT1/2/3** (vesicular glutamate transporters) | Synaptic vesicle membrane | Cytosolic Glu → vesicle lumen |
| 3 | After release: **astrocyte reuptake** via EAAT1/2 (GLT-1) | Perisynaptic astrocyte | Glu → Glutamine (via glutamine synthetase) → exported to neuron |

This glutamine–glutamate cycling between astrocytes and neurons is an obligate partnership — neurons cannot synthesize sufficient glutamate de novo without astrocyte-supplied glutamine.

### Receptors

Glutamate activates both **ionotropic (ligand-gated ion channels)** and **metabotropic (GPCR)** receptors [^dingledine-1999-glutamate-receptors]:

#### Ionotropic receptors

| Receptor | Subunits | Ion permeability | Key features |
|:---|:---|:---|:---|
| **AMPA** | GluA1–4 (heterotetramer) | Na⁺, K⁺ (Ca²⁺ if lacking GluA2) | Fast millisecond EPSPs; primary mediator of baseline excitatory transmission; GluA2-lacking AMPAs are Ca²⁺-permeable (important in plasticity) |
| **NMDA** | GluN1 + GluN2A–D (or GluN3) | Na⁺, K⁺, **Ca²⁺** (high permeability) | Voltage-dependent **Mg²⁺ block** at rest (coincidence detector); requires both glutamate AND glycine/D-serine co-agonist; slow kinetics (100s of ms) |
| **Kainate** | GluK1–5 | Na⁺, K⁺ | Presynaptic regulation of release; modulation of network excitability; involved in seizure activity |

#### Metabotropic receptors

| Group | Receptors | G-protein | Function |
|:---|:---|:---|:---|
| Group I | mGluR1, mGluR5 | Gαq → PLC → IP₃/DAG | Postsynaptic; enhance NMDA function; LTP/LTD modulation |
| Group II | mGluR2, mGluR3 | Gαi → ↓cAMP | Presynaptic autoreceptors; limit glutamate release (brake) |
| Group III | mGluR4, mGluR6, mGluR7, mGluR8 | Gαi → ↓cAMP | Presynaptic heteroreceptors; modulate multitransmitter release |

## Function

### Fast excitatory transmission (AMPA-mediated)

At most CNS excitatory synapses, an action potential arriving at the presynaptic terminal triggers vesicle fusion (SNARE machinery, Ca²⁺-triggered) and release of ~3,000 glutamate molecules per vesicle into the ~20 nm synaptic cleft. Cleft glutamate concentration peaks at ~1–3 mM within ~100 μs. AMPA receptors open rapidly (0.2–0.5 ms), producing a fast **excitatory postsynaptic current (EPSC)** that depolarizes the postsynaptic membrane. If the summated depolarization at the axon initial segment reaches threshold (~−55 mV), an action potential is initiated.

### Coincidence detection and LTP (NMDA-mediated)

The NMDA receptor is the brain's **molecular coincidence detector** — it requires two simultaneous conditions to conduct:

1. **Glutamate binding** (presynaptic activity)
2. **Postsynaptic depolarization** sufficient to expel the Mg²⁺ blocking the channel pore (postsynaptic activity)

When both conditions are met, Ca²⁺ flows through the NMDA channel. This Ca²⁺ influx activates **CaMKII**, which phosphorylates AMPA receptors and drives their insertion into the postsynaptic density — **LTP** [^malenka-bear-2004]. The synapse becomes more efficient for future transmission. LTP at hippocampal and cortical synapses is the cellular foundation of declarative and procedural memory.

The converse — prolonged low-level NMDA activation — drives AMPA receptor removal and **LTD** (long-term depression), which is equally essential for memory refinement and pattern separation.

## Mechanism

### The NMDA receptor voltage gating mechanism in detail

At resting membrane potential (≈ −70 mV), Mg²⁺ ions (extracellular concentration ~1 mM) enter the NMDA channel pore and become lodged, blocking current flow — even in the presence of glutamate. This block is **voltage-dependent**: as the membrane depolarizes (e.g., by AMPA-mediated EPSPs or back-propagating action potentials), the electrochemical force expelling Mg²⁺ increases. At ~−30 mV, the block is substantially relieved, and Ca²⁺ can flow.

This biophysical mechanism is the basis of **Hebbian synapse modification**: "neurons that fire together, wire together" — because only synapses that are active (glutamate present) during periods of postsynaptic depolarization (co-activation by other inputs) will undergo LTP-inducing Ca²⁺ influx. Synapses active alone, without coincident postsynaptic depolarization, do not trigger LTP.

### Excitotoxicity

In ischemia, oxygen/glucose deprivation reverses ion gradients and drives massive glutamate release from multiple sources (vesicular, transporter reversal). Sustained NMDA receptor activation → Ca²⁺ overload → activation of calpains, phospholipases, endonucleases, nitric oxide synthase → mitochondrial dysfunction → cell death. This **excitotoxic** cascade — first described by Olney [^olney-1969-excitotoxicity] — accounts for the bulk of infarct core and penumbra neuronal death in stroke and is a major therapeutic target.

## Connections

- `expressed-by` → **[neuron](../../04-cellular/neuron/README.md)** — synthesized and released by glutamatergic neurons (the most common CNS neuron type)
- `modulates` → **[synapse](../../05-tissue/synapse/README.md)** — mediates fast excitatory transmission and LTP/LTD at excitatory synapses
- `modulates` → **[brain](../../06-organ/brain/README.md)** — the primary driver of excitatory neural activity underlying all CNS computation
- `part-of` → **[nervous-system](../../07-system/nervous-system/README.md)** — foundational excitatory neurotransmitter

## Pathology

| Disease | Mechanism | Therapeutic implication |
|:---|:---|:---|
| **Ischemic stroke** | Excitotoxicity: ischemia → massive Glu release → NMDA Ca²⁺ overload → neuronal death | NMDA antagonists (memantine, ketamine) studied; tPA reperfusion limits window |
| **Epilepsy** | Excess glutamatergic excitation disrupts E/I balance → seizure propagation | Anti-seizure drugs targeting glutamate (perampanel, AMPA antagonist) |
| **Alzheimer's disease** | NMDA receptor dysfunction and excitotoxic contribution to amyloid/tau pathology | Memantine (NMDA partial antagonist) — modest symptomatic benefit |
| **Schizophrenia** | NMDA hypofunction hypothesis: reduced NMDA on GABAergic interneurons → disinhibition | NMDA-positive modulators in clinical trials |
| **ALS** | Glutamate excitotoxicity via impaired astrocytic EAAT2 (GLT-1) uptake | Riluzole (inhibits glutamate release) — extends survival |
| **TBI / neonatal HI** | Massive excitotoxic wave following impact or hypoxia | NMDA antagonists, hypothermia for neonatal HIE |

[^malenka-bear-2004]: Malenka RC, Bear MF. LTP and LTD: an embarrassment of riches. *Neuron.* 2004;44(1):5-21. [doi:10.1016/j.neuron.2004.09.012](https://doi.org/10.1016/j.neuron.2004.09.012) · [PubMed 15450155](https://pubmed.ncbi.nlm.nih.gov/15450155/)
[^bhatt-1995-nmda]: Dingledine R, Borges K, Bowie D, Traynelis SF. The glutamate receptor ion channels. *Pharmacol Rev.* 1999;51(1):7-61. [PubMed 10049997](https://pubmed.ncbi.nlm.nih.gov/10049997/)
[^dingledine-1999-glutamate-receptors]: Dingledine R, Borges K, Bowie D, Traynelis SF. The glutamate receptor ion channels. *Pharmacol Rev.* 1999;51(1):7-61. [PubMed 10049997](https://pubmed.ncbi.nlm.nih.gov/10049997/)
[^olney-1969-excitotoxicity]: Olney JW. Brain lesions, obesity, and other disturbances in mice treated with monosodium glutamate. *Science.* 1969;164(3880):719-721. [doi:10.1126/science.164.3880.719](https://doi.org/10.1126/science.164.3880.719) · [PubMed 5778021](https://pubmed.ncbi.nlm.nih.gov/5778021/)
[^openstax-neurotransmitters]: OpenStax. *Anatomy and Physiology 2e.* Chapter 12. Rice University; 2022. [openstax.org](https://openstax.org/books/anatomy-and-physiology-2e/pages/12-5-communication-between-neurons)
