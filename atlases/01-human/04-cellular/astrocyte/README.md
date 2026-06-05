---
schema: human-scale-entry/v1
id: astrocyte
name: Astrocyte
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Star-shaped glial cell; most abundant CNS cell type. Provides metabolic support (lactate shuttle), clears synaptic glutamate, buffers K⁺, maintains the blood-brain barrier via AQP4 endfeet, and forms the tripartite synapse."
aliases: ["astroglia", "fibrous astrocyte", "protoplasmic astrocyte", "reactive astrocyte", "Bergmann glia"]
sources:
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/brain
    relation: part-of
    note: "Protoplasmic astrocytes are the predominant glial cell in cortex and hippocampus, each contacting thousands of synapses; their endfeet envelop cerebral capillaries maintaining the blood-brain barrier."
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "Astrocytes support neurons via lactate supply (ANLS), glutamate recycling via GS, K⁺ spatial buffering via Kir4.1, D-serine release (NMDA co-agonist), neurotrophic factors (GDNF, BDNF), and synaptogenesis-promoting thrombospondins."
  - target: 01-human/05-tissue/synapse
    relation: modulates
    note: "Astrocytes form the third component of the tripartite synapse: take up synaptic glutamate via GLT-1/GLAST, convert to glutamine (GS), return glutamine for neurotransmitter replenishment; also release D-serine and ATP/adenosine."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Astrocytes regulate CNS K⁺ homeostasis (Kir4.1 spatial buffering), pH (bicarbonate), blood flow (Ca²⁺ waves → arteriole dilation via AA/PGE2/EET release); astrocyte dysfunction contributes to seizures, ischaemia, neurodegeneration."
---

# Astrocyte

## Overview

The astrocyte is the **most abundant cell type in the central nervous system** — star-shaped (from the Greek *astron*, star) glial cells that are indispensable partners to every neuron. Far from being passive structural scaffolding, astrocytes are **active participants in neural computation**: they form the third arm of the **tripartite synapse**, supply metabolic fuel via the astrocyte-neuron lactate shuttle, clear neurotransmitters, buffer extracellular ions, regulate cerebral blood flow, and maintain the blood-brain barrier [^alberts-mol-cell-biology].

Two major subtypes dominate the CNS: **protoplasmic astrocytes** (grey matter; highly branched, each cell contacting ~140,000 synapses) and **fibrous astrocytes** (white matter; fewer branches; envelop nodes of Ranvier). A third subtype, **Bergmann glia**, is restricted to the cerebellar cortex and guides Purkinje cell dendritogenesis. Together these cells tile the CNS in largely non-overlapping spatial domains, each astrocyte governing its own synaptic territory [^guyton-hall].

## Structure

### Morphology and markers

| Feature | Detail |
|:---|:---|
| **Soma size** | 9–25 µm diameter |
| **Shape** | Star-shaped; extensive fine processes radiating from soma |
| **Canonical marker** | GFAP (glial fibrillary acidic protein) — class III intermediate filament |
| **Additional markers** | Vimentin, nestin (immature/reactive); S100β (cytoplasmic); glutamine synthetase (GS); AQP4 (endfeet) |
| **Gap junctions** | Connexin-43 (Cx43) and Cx30 — link astrocytes into a **functional syncytium** |
| **Perivascular endfeet** | Envelop >99% of cerebral capillary surface; enriched in AQP4 (orthogonal arrays of particles, OAPs) and Kir4.1 |

### Subtypes

- **Protoplasmic** (grey matter): highly ramified, bushy processes; contact ~140,000 synapses/cell; thin perisynaptic astrocytic processes (PAPs, ~0.1–0.5 µm) penetrate deep into neuropil
- **Fibrous** (white matter): longer, less branched processes; wrap nodes of Ranvier; lower GFAP density per volume
- **Bergmann glia** (cerebellum): radial processes guide Purkinje cell dendritic arborisation; GLAST-rich; essential for cerebellar circuit formation
- **Müller glia** (retina): radial glia spanning all retinal layers; analogous astrocytic support function in the eye

## Function

### 1. Metabolic support — Astrocyte-Neuron Lactate Shuttle (ANLS)

Astrocytes are the **primary CNS glycogen reservoir** (~100 µmol glycogen/g wet brain). During neural activity:

1. Astrocyte glucose uptake (GLUT1) → **glycolysis** → pyruvate → lactate (LDHA + MCT4 export)
2. Neurons import lactate (MCT2) → pyruvate → **TCA cycle** → ATP

This shuttle provides neurons with oxidative fuel without competing for glucose. Glycogen mobilisation (glycogen phosphorylase, GP) sustains lactate output during intense firing or hypoglycaemia [^guyton-hall].

### 2. Neurotransmitter recycling — Glutamine-Glutamate/GABA Cycle

Astrocytes express **GLT-1 (EAAT2)** and **GLAST (EAAT1)** — the dominant brain glutamate transporters, responsible for >90% of synaptic glutamate clearance. Cleared glutamate undergoes amidation:

> Glutamate + NH₃ → **Glutamine** (glutamine synthetase, GS — astrocyte-specific)

Glutamine is released and taken up by neurons, which use it to regenerate glutamate (via phosphate-activated glutaminase, PAG) or GABA (GAD). GABA is recycled via GAT-3 on astrocyte membranes [^alberts-mol-cell-biology].

### 3. K⁺ Spatial Buffering

Action potentials release K⁺ into the extracellular space. Astrocytic **Kir4.1** channels absorb this K⁺ and redistribute it through the gap-junction syncytium to regions of lower K⁺ concentration (spatial buffering). This prevents extracellular K⁺ accumulation above the seizure threshold (~12 mM vs. resting ~3 mM) [^guyton-hall].

### 4. Blood-Brain Barrier Maintenance

Astrocyte endfeet signal to brain endothelial cells to:
- Upregulate and maintain **tight junction proteins** (claudin-5, occludin, ZO-1)
- Secrete **angiopoietin-1** (Tie2 → junction stabilisation), **TGF-β**, and **GDNF**
- Regulate water flux via **AQP4** (aquaporin-4), preventing oedema

### 5. Gliotransmission and Tripartite Synapse

Astrocytes detect synaptic activity via metabotropic glutamate receptors (mGluR2/3/5), P2Y receptors, and others → intracellular Ca²⁺ elevation → release of **gliotransmitters**:

| Gliotransmitter | Receptor(s) | Effect |
|:---|:---|:---|
| D-serine | NMDA NR2B subunit (co-agonist site) | Enables LTP induction |
| ATP → Adenosine | A1/A2A receptors | Synaptic depression/facilitation |
| Glutamate | mGluRs, NMDA | Slow inward currents; synchronise networks |
| GABA | GABA-A | Tonic inhibition in cerebellum, hippocampus |

### 6. Cerebrovascular Coupling

Astrocyte Ca²⁺ waves propagate to perivascular endfeet → arachidonic acid (AA) metabolised to:
- **PGE₂** (vasodilatory, EP receptors on smooth muscle)
- **EETs** (epoxyeicosatrienoic acids, vasodilatory, K⁺ channels)
- **20-HETE** (vasoconstrictive, under high activity)

This provides the cellular basis for **neurovascular coupling** — functional hyperaemia underlies the BOLD signal in fMRI [^guyton-hall].

### 7. Neurotrophic and Synaptogenic Support

Astrocytes secrete a rich cocktail of factors that shape neural circuit development and maintenance:
- **Neurotrophins**: GDNF, BDNF, NT-3, CNTF
- **Synaptogenic factors**: Thrombospondins 1/2 (induce silent synapses via α2δ-1 receptor), Hevin (NrCAM organiser), Glypicans 4 and 6 (activate AMPA receptor clustering)
- **Growth factors**: bFGF/FGF2, EGF

## Lifecycle

### Development — From Radial Glia to Astrocyte

Astrocytes are born late in neurodevelopment, after the major waves of neurogenesis:

1. **Neuroepithelial cells** (embryonic) → **Radial glial cells (RGCs)** — serve as neural stem cells AND as migratory scaffold for cortical neurons (inside-out lamination)
2. **Gliogenic switch** (~E16 in mouse, late 2nd trimester in humans): Notch/RBPJ, JAK/STAT3 (CNTF, LIF → pSTAT3), BMP2/4/SMAD signalling transition from neurogenesis to **astrogliogenesis**
3. RGCs asymmetrically divide → astrocyte daughters that progressively mature, retract radial processes, and elaborate local territorial processes
4. Postnatal maturation: astrocytes elaborate PAPs, form gap-junction networks, refine perisynaptic contacts over weeks

### Reactive Astrogliosis

Brain injury (trauma, ischaemia, infection, neurodegeneration) triggers a graded **reactive gliosis** response:
- **Mild/moderate**: ↑GFAP, ↑vimentin, process hypertrophy — neuroprotective (trophic, antioxidant, BBB repair)
- **Severe**: proliferation, migration, loss of domain organisation → formation of a **glial scar** (anisomorphic gliosis) composed of chondroitin sulfate proteoglycans (CSPGs: brevican, neurocan, versican, aggrecan) — inhibits axon regeneration [^alberts-mol-cell-biology]

Molecular switches: NF-κB (cytokine-driven reactive activation), STAT3 (scar formation), Nrf2 (antioxidant response).

## Connections

- **Part of** the brain [→ brain](../../06-organ/brain/README.md): Protoplasmic astrocytes are the predominant glial cell in cerebral cortex and hippocampus, each contacting thousands of synapses; their endfeet envelop cerebral capillaries maintaining the blood-brain barrier.
- **Modulates** neuron [→ neuron](../../04-cellular/neuron/README.md): Astrocytes support neurons via lactate supply (ANLS), glutamate recycling via GS, K⁺ spatial buffering via Kir4.1, D-serine release (NMDA co-agonist), neurotrophic factors (GDNF, BDNF), and synaptogenesis-promoting thrombospondins.
- **Modulates** synapse [→ synapse](../../05-tissue/synapse/README.md): Astrocytes form the third component of the tripartite synapse: take up synaptic glutamate via GLT-1/GLAST, convert to glutamine (GS), return glutamine for neurotransmitter replenishment; also release D-serine and ATP/adenosine.
- **Modulates** nervous system [→ nervous-system](../../07-system/nervous-system/README.md): Astrocytes regulate CNS K⁺ homeostasis (Kir4.1 spatial buffering), pH (bicarbonate), blood flow (Ca²⁺ waves → arteriole dilation via AA/PGE2/EET release); astrocyte dysfunction contributes to seizures, ischaemia, neurodegeneration.

## Pathology

| Condition | Mechanism | Key Features |
|:---|:---|:---|
| **Astrogliosis / Glial scar** | TBI, stroke, MS, SCI, ALS → reactive gliosis → CSPG-rich scar | Limits spread of damage but blocks axon regeneration; STAT3 and NF-κB drive scar phenotype |
| **Alexander disease** | Gain-of-function GFAP mutations → Rosenthal fibers (GFAP aggregates) | Megalencephalic leukoencephalopathy; infantile/juvenile forms; seizures, ataxia, spasticity |
| **Hepatic encephalopathy** | Hyperammonaemia → Alzheimer type II astrocyte transformation; cerebral oedema | Astrocyte swelling via AQP4 upregulation and glutamine accumulation (osmotic stress); impaired K⁺ buffering |
| **Neuromyelitis optica (NMO/NMOSD)** | Anti-AQP4 IgG (NMO-IgG) → complement-mediated astrocyte destruction | Inflammatory demyelinating lesions in optic nerve and spinal cord; severe attacks, distinct from MS |
| **Glioblastoma (GBM)** | Grade IV astrocytic tumour; IDH-wildtype | EGFR amplification, PTEN deletion, TERT promoter mutation; median survival ~15 months despite surgery+RT+TMZ |
| **Epilepsy** | Loss of Kir4.1 or GLT-1/GLAST → impaired K⁺ and glutamate buffering | Elevated extracellular K⁺ and glutamate → neuronal hyperexcitability → seizures |

## See Also

- [Neuron](../../04-cellular/neuron/README.md) — primary cellular partner; astrocyte-neuron metabolic and signalling interdependence
- [Synapse](../../05-tissue/synapse/README.md) — tripartite synapse: astrocyte processes are an obligatory synaptic component
- [Brain](../../06-organ/brain/README.md) — organ context; astrocytes tile the entire brain in non-overlapping territorial domains
- [Nervous System](../../07-system/nervous-system/README.md) — system-level context; astrocyte failure contributes to neurological disease across all CNS compartments
- [Macrophage](../../04-cellular/macrophage/README.md) — microglia (brain-resident macrophages) interact closely with reactive astrocytes in neuroinflammation
