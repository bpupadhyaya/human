---
schema: human-scale-entry/v1
id: axonal-transport
name: Axonal Transport
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-06
summary: "Bidirectional movement of cargoes along axonal microtubule tracks; kinesin drives anterograde delivery (synaptic vesicles, mitochondria) and dynein drives retrograde return (trophic signals, damaged organelles). Disrupted in Alzheimer's, ALS, and Huntington's."
aliases: ["axoplasmic transport", "fast axonal transport", "slow axonal transport"]
sources:
  - id: hirokawa-2009-kinesin
    type: peer-reviewed
    cite: "Hirokawa N, Noda Y, Tanaka Y, Niwa S. Kinesin superfamily motor proteins and intracellular transport. Nat Rev Mol Cell Biol. 2009;10(10):682-696."
    doi: "10.1038/nrm2774"
    pmid: "19773780"
    url: "https://doi.org/10.1038/nrm2774"
  - id: maday-2014-axonal-transport
    type: peer-reviewed
    cite: "Maday S, Twelvetrees AE, Moughamian AJ, Holzbaur EL. Axonal transport: cargo-specific mechanisms of motility and regulation. Neuron. 2014;84(2):292-309."
    doi: "10.1016/j.neuron.2014.10.019"
    pmid: "25374356"
    url: "https://doi.org/10.1016/j.neuron.2014.10.019"
  - id: millecamps-2013-neurodegeneration
    type: peer-reviewed
    cite: "Millecamps S, Julien JP. Axonal transport deficits and neurodegenerative diseases. Nat Rev Neurosci. 2013;14(3):161-176."
    doi: "10.1038/nrn3380"
    pmid: "23361386"
    url: "https://doi.org/10.1038/nrn3380"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: part-of
    note: "Axonal transport is a fundamental process of every neuron; motor neurons with meter-long axons (sciatic nerve) depend on rapid anterograde transport to supply synaptic terminals with vesicles and retrograde transport to deliver trophic signals (BDNF-TrkB endosomes) to the soma."
  - target: 01-human/03-molecular/snare-complex
    relation: connects-to
    note: "Synaptic vesicle precursors and SNARE cargo are delivered to terminals by anterograde fast axonal transport (kinesin-3/KIF1A); SNARE proteins cannot diffuse from the soma and depend entirely on transport for distal replenishment."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Axonal transport maintains the presynaptic terminal by continuously supplying synaptic vesicle proteins, mitochondria, and lipid membranes; retrograde transport clears autophagosomes containing damaged organelles back to the soma for lysosomal degradation."
---

# Axonal Transport

## Overview

**Axonal transport** is the active, motor-protein-driven movement of organelles, vesicles, proteins, and RNA along the length of the axon — the uniquely elongated process of neurons that can extend over a meter in large mammals. Because the neuronal soma is the primary site of protein synthesis and organelle biogenesis, and yet the synaptic terminal (often located far away) demands continuous renewal of synaptic vesicles, mitochondria, and membrane components, neurons have evolved a specialized logistics system driven by cytoskeletal motor proteins.

The fundamental architecture is a **bidirectional highway** along **microtubule tracks** (uniformly oriented in axons: plus-ends distal in axons, enabling directionality):
- **Anterograde transport:** Soma → axon → terminal; powered by **kinesin** motors (KIF family)
- **Retrograde transport:** Terminal → axon → soma; powered by **cytoplasmic dynein** (with dynactin complex)

Disruption of axonal transport is now recognized as a **central early event** in multiple neurodegenerative diseases — often preceding overt neuronal death by years — and represents a promising therapeutic target [^millecamps-2013-neurodegeneration].

## Structure

### Microtubule tracks

Axonal microtubules are long (up to hundreds of μm), uniformly polar (plus-end distal), and densely packed (~100/μm² in large axons). They are stabilized by:
- **Tau protein:** Microtubule-associated protein that bridges adjacent MTs and regulates motor binding; hyperphosphorylated tau (as in Alzheimer's disease and frontotemporal dementia) dissociates from MTs, forms neurofibrillary tangles, and disrupts axonal transport
- **MAPs (microtubule-associated proteins):** MAP1B, MAP2 (excluded from axons), and others modulate MT dynamics, spacing, and post-translational modifications (acetylation, detyrosination) that create a "tubulin code" recognized by specific motor adaptors

### Kinesin motors (anterograde)

The **kinesin superfamily (KIF proteins)** comprises 45 members in humans [^hirokawa-2009-kinesin]:

| Kinesin | Primary cargoes | Speed |
|:---|:---|:---|
| KIF5A/B/C (conventional kinesin-1) | Mitochondria, APP vesicles, mRNA, neurofilaments | ~1 μm/s |
| KIF1A/B (kinesin-3) | Synaptic vesicle precursors, dense-core vesicles | ~1.5 μm/s |
| KIF2A/B (kinesin-13) | MT dynamics regulation (depolymerizing) | — |
| KIF17 (kinesin-2) | NMDA receptor vesicles | ~0.75 μm/s |

Kinesins are processive dimers; each ATPase head hydrolyzes one ATP per 8 nm step along the MT; a single kinesin generates ~5–7 pN of force.

**Adaptor proteins** link motor complexes to specific cargoes: TRAK1/2 (mitochondria ↔ KIF5), DENN/MADD (synaptic vesicles ↔ KIF1A), JIP1/3 (APP vesicles ↔ KIF5 and dynein). These adaptors often respond to local Ca²⁺ or phosphorylation signals to regulate transport at specific locations (e.g., stopping mitochondria at high-activity synapses).

### Dynein motor (retrograde)

**Cytoplasmic dynein-1** is the sole retrograde motor complex [^maday-2014-axonal-transport]:
- **Core complex:** Two heavy chains (DHC1; ATPase motors), two intermediate chains (DIC), light intermediate chains, light chains
- **Dynactin:** Essential activating cofactor complex (Arp1 filament + p150^glued^); increases processivity from ~1 μm to >100 μm; mutations in dynactin (DCTN1) cause motor neuron disease
- **Cargo adaptors:** BICD2 (Golgi/nucleus), Hook1/3 (endosomes), RILP (late endosomes/lysosomes); each adaptor activates dynein by releasing autoinhibited conformations

Dynein moves at ~0.5–1 μm/s toward the MT minus-end (soma); the dynein-dynactin-adaptor complex generates ~1 pN of force per dynein head.

### Transport categories

**Fast axonal transport (FAT):** 200–400 mm/day (2–4 μm/s); moves membrane-bound organelles:
- Anterograde FAT: Synaptic vesicle precursors, mitochondria, APP vesicles, dense-core vesicles
- Retrograde FAT: Signaling endosomes (BDNF-TrkB), autophagosomes, multivesicular bodies, recycled membrane

**Slow axonal transport (SAT):** 0.1–10 mm/day; moves cytoskeletal components and soluble proteins:
- SCa (slow component a): Neurofilaments, tubulin; ~0.1–1 mm/day
- SCb (slow component b): Actin, glycolytic enzymes, clathrin, calmodulin; ~2–10 mm/day
- SAT uses the same kinesin/dynein motors but cargo moves in short, infrequent bursts — net movement is slow but peak velocities during bursts equal FAT

## Function

**Anterograde supply:** Every presynaptic terminal is maintained exclusively by anterograde transport from the soma — synaptic vesicle proteins (synapsin, synaptotagmin, synaptobrevin), neurotransmitter-synthesizing enzymes, lipid membranes, and mitochondria must travel the full axon length. For a 1-meter motor neuron axon (e.g., tibial nerve), refilling the terminal after sustained activity takes hours.

**Retrograde signaling:** Signaling endosomes carry neurotrophic factor-receptor complexes (BDNF-TrkB, NGF-TrkA) retrogradely from axon terminals to the soma, where they activate transcription factors (CREB) that regulate neuronal survival, differentiation, and synaptic plasticity. This retrograde trophic signal is critical during development and is degraded in neurodegenerative disease.

**Quality control:** Damaged organelles and protein aggregates are packaged into autophagosomes at the distal axon and transported retrogradely to the soma/lysosome for degradation. Failure of this clearance mechanism contributes to aggregate accumulation in neurodegeneration.

**Pathogen exploitation:** Several neurotropic pathogens exploit retrograde axonal transport:
- **Herpes simplex / VZV:** Capsids reach DRG soma via dynein for latent infection establishment; reactivated virions travel anterograde to skin epithelium
- **Tetanus toxin:** Endocytosed at NMJ → retrograde transport to spinal cord → trans-synaptic spread → VAMP2 cleavage → disinhibition → tetanic spasm
- **Rabies virus:** Retrograde transport from peripheral nerve terminal to CNS

**Disease mechanisms [^millecamps-2013-neurodegeneration]:**
- **Alzheimer's disease:** Hyperphosphorylated tau detaches from MTs → MT destabilization → FAT impairment; APP cleavage products (Aβ) produced in excess in transported APP vesicles at synapses; amyloid precursor protein transport disruption → synaptic failure
- **ALS:** Mutations in SOD1, FUS, TDP-43, C9orf72 → impaired retrograde signaling, dynein/dynactin dysfunction, neurofilament aggregates blocking transport; KIF5A mutations cause familial ALS (fALS)
- **Huntington's disease:** PolyQ-expanded huntingtin impairs HAP1-mediated BDNF vesicle transport → cortical → striatal trophic support failure → striatal neuron death

## Connections

- `part-of` → **[Neuron](../../04-cellular/neuron/README.md)** — axonal transport is a fundamental ongoing process within every neuron; disruption is incompatible with long-term axonal and synaptic maintenance.
- `connects-to` → **[SNARE Complex](../../03-molecular/snare-complex/README.md)** — SNARE protein cargoes (synaptobrevin, SNAP-25, syntaxin) and their synaptic vesicle precursors are delivered to presynaptic terminals exclusively by KIF1A-driven anterograde fast axonal transport.
- `connects-to` → **[Synapse](../synapse/README.md)** — axonal transport maintains the presynaptic terminal by supplying synaptic vesicle components, mitochondria, and membrane, and clears damaged organelles via retrograde autophagosomes.

[^hirokawa-2009-kinesin]: Hirokawa N, Noda Y, Tanaka Y, Niwa S. Kinesin superfamily motor proteins and intracellular transport. *Nat Rev Mol Cell Biol.* 2009;10(10):682-696. [doi:10.1038/nrm2774](https://doi.org/10.1038/nrm2774) · [PubMed 19773780](https://pubmed.ncbi.nlm.nih.gov/19773780/)
[^maday-2014-axonal-transport]: Maday S, Twelvetrees AE, Moughamian AJ, Holzbaur EL. Axonal transport: cargo-specific mechanisms of motility and regulation. *Neuron.* 2014;84(2):292-309. [doi:10.1016/j.neuron.2014.10.019](https://doi.org/10.1016/j.neuron.2014.10.019) · [PubMed 25374356](https://pubmed.ncbi.nlm.nih.gov/25374356/)
[^millecamps-2013-neurodegeneration]: Millecamps S, Julien JP. Axonal transport deficits and neurodegenerative diseases. *Nat Rev Neurosci.* 2013;14(3):161-176. [doi:10.1038/nrn3380](https://doi.org/10.1038/nrn3380) · [PubMed 23361386](https://pubmed.ncbi.nlm.nih.gov/23361386/)
