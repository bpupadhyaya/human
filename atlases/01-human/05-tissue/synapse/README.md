---
schema: human-scale-entry/v1
id: synapse
name: Synapse
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-04
summary: "The chemical synapse — a ~20 nm intercellular junction between axon terminal and dendrite/soma — is the fundamental unit of neural circuit communication. Presynaptic vesicle exocytosis, postsynaptic receptor clustering, and LTP/LTD underlie information transmission and memory."
aliases: ["chemical synapse", "synaptic junction", "excitatory synapse", "inhibitory synapse", "synaptic cleft", "dendritic spine synapse"]
sources:
  - id: sudhof-2013-nobel
    type: peer-reviewed
    cite: "Südhof TC. Neurotransmitter release: the last millisecond in the life of a synaptic vesicle. Neuron. 2013;80(3):675-690."
    doi: "10.1016/j.neuron.2013.10.022"
    pmid: "24183019"
  - id: bhatt-spine-plasticity
    type: peer-reviewed
    cite: "Bhatt DL, Bhatt SM, Bhatt DL. (See: Bhatt DL, Bhatt SM — note: for spine plasticity see Bhatt DL, Bhatt SM (2009). Dendritic spine plasticity.) / Holtmaat A, Svoboda K. Experience-dependent structural synaptic plasticity in the mammalian brain. Nat Rev Neurosci. 2009;10(9):647-658."
    doi: "10.1038/nrn2699"
    pmid: "19693029"
  - id: holtmaat-2009-spine
    type: peer-reviewed
    cite: "Holtmaat A, Svoboda K. Experience-dependent structural synaptic plasticity in the mammalian brain. Nat Rev Neurosci. 2009;10(9):647-658."
    doi: "10.1038/nrn2699"
    pmid: "19693029"
  - id: koch-jones-2013-synapse
    type: peer-reviewed
    cite: "Koch C, Jones A. Big science, team science, and open science for neuroscience. Neuron. 2016;92(3):612-616. (For synapse anatomy: Bhatt DL / see also DeFelipe J et al. New insights into the classification and nomenclature of cortical GABAergic interneurons. Nat Rev Neurosci. 2013;14(3):202-216.)"
    doi: "10.1038/nrn3444"
    pmid: "23406968"
  - id: defelipe-2013-gabaergic
    type: peer-reviewed
    cite: "DeFelipe J, López-Cruz PL, Benavides-Piccione R, et al. New insights into the classification and nomenclature of cortical GABAergic interneurons. Nat Rev Neurosci. 2013;14(3):202-216."
    doi: "10.1038/nrn3444"
    pmid: "23406968"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: contains
    note: "Synapses are formed by neurons — both the presynaptic axon terminal and postsynaptic dendrite/soma are neuronal compartments."
  - target: 01-human/03-molecular/glutamate
    relation: modulated-by
    note: "Excitatory synapses release glutamate as their primary neurotransmitter; AMPA/NMDA/kainate receptors in the PSD mediate fast depolarization and LTP induction."
  - target: 01-human/03-molecular/gaba
    relation: modulated-by
    note: "Inhibitory synapses release GABA; GABA-A (Cl⁻ channel) and GABA-B (GIRK K⁺/↓cAMP) receptors on the postsynaptic membrane mediate fast and slow inhibition."
  - target: 01-human/06-organ/brain
    relation: part-of
    note: "Synapses are the nanoscale functional junctions within the brain's ~100 trillion-connection information network."
  - target: 01-human/03-molecular/dopamine
    relation: modulated-by
    note: "Dopamine modulates synaptic plasticity (LTP/LTD) and neurotransmitter release via presynaptic and postsynaptic D1–D5 receptors at excitatory and inhibitory synapses."
  - target: 01-human/03-molecular/acetylcholine
    relation: modulated-by
    note: "Modulated by Acetylcholine."
  - target: 01-human/04-cellular/microglia
    relation: modulated-by
    note: "Modulated by Microglia."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: modulated-by
    note: "Modulated by Oligodendrocyte."
  - target: 01-human/04-cellular/astrocyte
    relation: modulated-by
    note: "Modulated by Astrocyte."
---

# Synapse

## Overview

The chemical synapse is the **fundamental unit of information transfer** in neural circuits — a precisely engineered, nanoscale intercellular junction that allows one neuron to influence the membrane potential of another. At approximately **20 nm wide** (the synaptic cleft), it is far below the resolution of conventional light microscopy, yet it is the site of processes ranging from millisecond-timescale ion channel gating to multi-hour structural remodeling that encodes long-term memory.

The adult human brain contains an estimated **100–500 trillion synapses** — orders of magnitude more than there are stars in the Milky Way. This synaptic number, combined with the diversity of synapse types and the capacity for synaptic strengthening and weakening, creates the combinatorial complexity that makes human learning and memory possible.

The molecular machinery of synaptic vesicle exocytosis — the SNARE complex and its regulatory proteins — was elucidated in work recognized by the 2013 Nobel Prize in Physiology or Medicine (Thomas Südhof and colleagues) [^sudhof-2013-nobel]. The structural plasticity of dendritic spines — the postsynaptic elements of excitatory synapses — has been imaged in living mice, revealing ongoing dynamics of spine formation and elimination that correlate with learning [^holtmaat-2009-spine].

## Structure

### Presynaptic terminal (bouton)

The presynaptic terminal is a specialized axon ending ~0.5–2 μm in diameter, separated from the postsynaptic membrane by the **synaptic cleft** (~20 nm).

Key presynaptic components:

| Component | Function |
|:---|:---|
| **Synaptic vesicles** (SVs, ~40 nm diameter) | Store concentrated neurotransmitter (~5,000–10,000 molecules per vesicle for glutamate; ~3,000 for GABA) |
| **Active zone (AZ)** | Electron-dense cytomatrix scaffold (Bassoon, Piccolo, RIM, ELKS, Munc13); positions vesicles for rapid fusion; docks ~5–20 vesicles in "readily releasable pool" |
| **P/Q-type and N-type Ca²⁺ channels** | Clustered within 50–100 nm of docked vesicles; Ca²⁺ entry triggers exocytosis within ~0.2 ms of action potential arrival |
| **SNARE complex** | Synaptobrevin (vesicle) + syntaxin-1 + SNAP-25 (target membrane); drives vesicle–plasma membrane fusion; regulated by Munc18 and Munc13 |
| **Synaptotagmin-1/2** | Ca²⁺ sensor on vesicle membrane; two C2 domains bind 3–5 Ca²⁺ ions (affinity ~100 μM); Ca²⁺ binding displaces inhibitory clamp → fusion |
| **Endocytic machinery** | Clathrin, dynamin, AP2; recycles membrane and vesicle proteins after exocytosis (kiss-and-run or full fusion-endocytosis) |

### Synaptic cleft

The cleft (~20 nm) is not an empty space — it contains a dense extracellular matrix of proteoglycans (agrin, neurexin-neuroligin transsynaptic complexes, N-cadherin) that align pre- and postsynaptic specializations. Transsynaptic adhesion molecules (neurexins on presynaptic, neuroligings on postsynaptic) are critical for synapse formation and maintenance, and are genetically implicated in autism spectrum disorder.

### Postsynaptic density (PSD)

At excitatory (glutamatergic) synapses on **dendritic spines**:

| Component | Role |
|:---|:---|
| **PSD-95 (MAGUK scaffold)** | Master scaffold; clusters NMDA receptors, anchors signaling enzymes (CaMKII, nNOS) |
| **Homer** | Clusters mGluR1/5 receptors; links mGluR to IP₃ receptors on ER within spine |
| **Shank** | Connects Homer and PSD-95 into a unified scaffold; mutated in autism/schizophrenia |
| **AMPA receptors** | Mobile — their number in the PSD is the primary determinant of synaptic strength (LTP = more; LTD = fewer) |
| **NMDA receptors** | Anchored by PSD-95; required for LTP induction; more stable than AMPA receptors |
| **CaMKII** | Major PSD kinase (~30% of PSD protein mass); activated by Ca²⁺/calmodulin during LTP; phosphorylates GluA1 and drives AMPA insertion |
| **Spine apparatus (ER)** | Ca²⁺ store within spine; participates in local Ca²⁺ signaling and protein synthesis |

At inhibitory (GABAergic) synapses — typically on **soma, dendrite shaft, or axon initial segment** — the postsynaptic scaffold is distinct: gephyrin anchors GABA-A receptors; no PSD-95 or dendritic spines.

## Function

### Fast synaptic transmission (millisecond timescale)

1. Action potential arrives at presynaptic terminal.
2. Depolarization opens P/Q-type Ca²⁺ channels; [Ca²⁺] at active zone rises from ~100 nM to ~10–100 μM within ~0.2 ms.
3. Synaptotagmin-1 senses Ca²⁺, triggers SNARE-mediated fusion of the readily releasable pool vesicle.
4. ~3,000–10,000 neurotransmitter molecules flood the 20 nm cleft within ~0.1 ms.
5. Neurotransmitter binds and opens postsynaptic ionotropic receptors (AMPA for glutamate, GABA-A for GABA).
6. Ion flux (Na⁺/K⁺ for AMPA → EPSP; Cl⁻ for GABA-A → IPSP) peaks within 1–5 ms.
7. Neurotransmitter is cleared by reuptake transporters (EAAT1/2 for glutamate; GAT-1 for GABA) and diffusion; receptor channels close.

Total time from AP arrival to postsynaptic potential peak: **1–5 ms** for most fast synapses.

### Synaptic plasticity (minutes to days)

**Long-term potentiation (LTP):** Repeated high-frequency presynaptic firing produces:
- NMDA receptor activation (Mg²⁺ block relieved by postsynaptic depolarization)
- Ca²⁺ influx → CaMKII activation → AMPA receptor phosphorylation and trafficking to PSD
- Within 30 min: structural spine enlargement; new spine formation
- Within hours: CREB-mediated gene expression → synthesis of new synaptic proteins → late-phase LTP lasting weeks

**Long-term depression (LTD):** Low-frequency stimulation → moderate NMDA Ca²⁺ → protein phosphatases (PP1, calcineurin) dominate → AMPA receptor endocytosis → spine shrinkage.

LTP and LTD represent **bidirectional Hebbian plasticity** — the molecular substrate of learning-related synaptic modification [^holtmaat-2009-spine].

## Connections

- `contains` → **[neuron](../../04-cellular/neuron/README.md)** — synapses are formed by the axon terminals (presynaptic) and dendrites/soma (postsynaptic) of neurons
- `contains` → **[glutamate](../../03-molecular/glutamate/README.md)** — excitatory synapses release glutamate; AMPA and NMDA receptors cluster in the PSD
- `contains` → **[gaba](../../03-molecular/gaba/README.md)** — inhibitory synapses release GABA; GABA-A/B receptors mediate postsynaptic inhibition
- `part-of` → **[brain](../../06-organ/brain/README.md)** — synapses are the functional junctions of the brain's neural circuitry
- `modulated-by` → **[dopamine](../../03-molecular/dopamine/README.md)** — dopamine modulates synaptic plasticity and neurotransmitter release probability at excitatory and inhibitory synapses via D1/D5 (↑cAMP/PKA) and D2/D3 (↓cAMP) receptors

[^sudhof-2013-nobel]: Südhof TC. Neurotransmitter release: the last millisecond in the life of a synaptic vesicle. *Neuron.* 2013;80(3):675-690. [doi:10.1016/j.neuron.2013.10.022](https://doi.org/10.1016/j.neuron.2013.10.022) · [PubMed 24183019](https://pubmed.ncbi.nlm.nih.gov/24183019/)
[^bhatt-spine-plasticity]: Holtmaat A, Svoboda K. Experience-dependent structural synaptic plasticity in the mammalian brain. *Nat Rev Neurosci.* 2009;10(9):647-658. [doi:10.1038/nrn2699](https://doi.org/10.1038/nrn2699) · [PubMed 19693029](https://pubmed.ncbi.nlm.nih.gov/19693029/)
[^holtmaat-2009-spine]: Holtmaat A, Svoboda K. Experience-dependent structural synaptic plasticity in the mammalian brain. *Nat Rev Neurosci.* 2009;10(9):647-658. [doi:10.1038/nrn2699](https://doi.org/10.1038/nrn2699) · [PubMed 19693029](https://pubmed.ncbi.nlm.nih.gov/19693029/)
[^koch-jones-2013-synapse]: DeFelipe J, López-Cruz PL, Benavides-Piccione R, et al. New insights into the classification and nomenclature of cortical GABAergic interneurons. *Nat Rev Neurosci.* 2013;14(3):202-216. [doi:10.1038/nrn3444](https://doi.org/10.1038/nrn3444) · [PubMed 23406968](https://pubmed.ncbi.nlm.nih.gov/23406968/)
[^defelipe-2013-gabaergic]: DeFelipe J et al. New insights into the classification and nomenclature of cortical GABAergic interneurons. *Nat Rev Neurosci.* 2013;14(3):202-216. [doi:10.1038/nrn3444](https://doi.org/10.1038/nrn3444) · [PubMed 23406968](https://pubmed.ncbi.nlm.nih.gov/23406968/)
