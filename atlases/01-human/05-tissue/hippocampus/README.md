---
schema: human-scale-entry/v1
id: hippocampus
name: Hippocampus
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-05
summary: "Bilateral archicortical structure in the medial temporal lobe, critical for episodic memory encoding, spatial navigation, and emotional memory. Contains CA1–CA4 pyramidal neurons and dentate gyrus granule cells forming the trisynaptic entorhinal-hippocampal circuit."
aliases: ["hippocampal formation", "cornu ammonis", "CA1-CA4", "dentate gyrus", "entorhinal-hippocampal circuit"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/brain
    relation: part-of
    note: "Hippocampus is a bilateral archicortical structure in the medial temporal lobe; CA1/CA3 pyramidal neurons and dentate gyrus granule cells form the trisynaptic circuit for declarative memory encoding and spatial navigation."
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "CA1 pyramidal neurons exhibit LTP at Schaffer collateral synapses via NMDAR-dependent Ca²⁺/CaMKII → AMPAR insertion; place cells encode spatial location; dentate gyrus neurogenesis contributes to pattern separation and episodic memory."
  - target: 01-human/03-molecular/glutamate
    relation: modulates
    note: "Schaffer collateral and perforant path synapses are glutamatergic (AMPAR+NMDAR); NMDAR is the coincidence detector for LTP; excitotoxic glutamate release in ischaemia selectively kills CA1 pyramidal neurons (Sommer sector)."
  - target: 01-human/03-molecular/cortisol
    relation: modulates
    note: "Hippocampus expresses high GR and MR levels; acute cortisol → ↑synaptic plasticity; chronic cortisol → ↓BDNF, ↓neurogenesis, CA3 dendritic atrophy, hippocampal volume reduction — basis of stress-induced depression and PTSD."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF/TrkB drives L-LTP and dentate gyrus neurogenesis; antidepressants ↑BDNF/CREB → neurogenesis required for antidepressant efficacy (Santarelli 2003); chronic cortisol ↓BDNF → hippocampal atrophy in depression/PTSD; ketamine → rapid BDNF release → rapid antidepressant action."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin (5-HT1A/5-HT4) modulates hippocampal neuroplasticity; 5-HT1A in DG granule cells and CA1 pyramidal neurons; SSRIs ↑5-HT → ↑BDNF/TrkB → ↑SGZ neurogenesis → antidepressant effect delayed 2-4 weeks; 5-HT depletion impairs pattern separation and memory consolidation."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Hippocampus and entorhinal cortex are earliest sites of NFT deposition (Braak I-II) and Aβ synaptic failure; hippocampal MRI atrophy is the earliest AD biomarker; CA1 Sommer sector is selectively vulnerable; lecanemab (anti-Aβ) slows hippocampal atrophy and memory decline."
---

# Hippocampus

## Overview

The hippocampus is a paired, seahorse-shaped archicortical (three-layered paleocortex) structure located in the medial temporal lobe of each cerebral hemisphere, forming a prominent elevation on the floor of the inferior horn of the lateral ventricle. Approximately 3–4 cm long in humans, it is bilaterally symmetric and connected to the overlying cortex and subcortical structures via the fornix, a white matter arch projecting to the mammillary bodies, septal nuclei, and hypothalamus. Together with the dentate gyrus, subiculum, presubiculum, parasubiculum, and entorhinal cortex, it forms the hippocampal formation — the primary limbic structure for declarative (explicit) memory encoding, spatial navigation, and emotional memory modulation.[^guyton-hall]

The critical importance of the hippocampus in human memory was established by the case of H.M. (Henry Molaison, 1953): bilateral hippocampal resection for intractable epilepsy produced profound anterograde amnesia (inability to form new declarative memories) while largely preserving procedural memory, intelligence, and remote memories — dissociating hippocampus-dependent from hippocampus-independent memory systems. John O'Keefe's 1971 discovery of hippocampal place cells (Nobel Prize 2014, shared with Edvard and May-Britt Moser for grid cells in entorhinal cortex) established the hippocampus as the neural substrate of the mammalian cognitive map.[^alberts-mol-cell-biology]

## Structure

**Subfields and cytoarchitecture.** The hippocampus proper (cornu ammonis, CA) is divided into CA1, CA2, CA3, and CA4 subfields based on pyramidal cell size, connectivity, and gene expression:

| Subfield | Pyramidal neuron size | Key inputs | Key outputs | Distinct features |
|----------|----------------------|------------|-------------|-------------------|
| CA1 | Medium, densely packed | Schaffer collaterals (CA3), TA path (EC layer III) | Subiculum, EC layer V, prefrontal cortex | LTP model synapse; most vulnerable to ischaemia; "Sommer sector" |
| CA2 | Large, densely packed | Mossy fibres (DG), TA path, lateral entorhinal cortex | CA1, CA3 | Social memory; relatively ischaemia-resistant; RGS14-enriched |
| CA3 | Large, loosely packed | Mossy fibres (DG), perforant path (EC layer II) | Schaffer collaterals → CA1; commissural fibres | Autoassociative recurrent network; pattern completion; epilepsy-prone |
| CA4 (hilar region) | Mossy cells, interneurons | DG granule cell axons | DG (feedback) | Mossy cell loss → temporal lobe epilepsy after SE |

**Dentate gyrus (DG).** A C-shaped trilaminar cortex wrapping around CA3; granule cells (~10 µm, ~1.2 million per human hippocampus) are compact and sparsely firing, performing pattern separation (orthogonalising similar inputs). DG receives the main cortical input via the perforant path (EC layer II → molecular layer of DG) and projects via mossy fibre axons (~6–12 µm diameter) to CA3 thorny excrescence synapses (giant boutons, ~4 µm, multiple active zones → powerful, conditional detonator synapses). The DG subgranular zone (SGZ) is one of two regions in the adult brain supporting neurogenesis.[^alberts-mol-cell-biology]

**Trisynaptic circuit (entorhinal-hippocampal loop).**
1. *Perforant path* (synapse 1): Entorhinal cortex (EC) layer II stellate cells → DG granule cell dendrites in molecular layer; medial perforant path (MEC→DG, spatial/grid-cell input) and lateral perforant path (LEC→DG, non-spatial/object input).
2. *Mossy fibres* (synapse 2): DG granule cell axons → CA3 pyramidal dendrites (proximal, thorny excrescences); also contain GluR2-lacking AMPAR (Ca²⁺-permeable) and kainate receptors (GluK2/GluK5); conditional gating (low stimulation → GABA interneuron inhibition dominant; high stimulation → detonator excitation).
3. *Schaffer collaterals* (synapse 3): CA3 pyramidal axon collaterals → CA1 pyramidal dendrites (stratum radiatum); AMPAR (fast EPSPs) + NMDAR (Mg²⁺-gated, coincidence detector); the canonical site of LTP induction.

**Temporo-ammonic (TA) pathway.** EC layer III → CA1 apical dendrites (stratum lacunosum-moleculare); provides direct cortical input to CA1, bypassing DG/CA3; particularly active during sleep (sharp wave-ripples) for memory consolidation and during pattern completion.

**Interneuron network.** Approximately 15–20% of hippocampal neurons are GABAergic interneurons, classified by molecular marker, morphology, and target cell compartment:
- *PV⁺ basket cells*: target soma/proximal dendrites → synchronise pyramidal cell firing → γ oscillations; fast-spiking, VGCC-dense.
- *PV⁺ chandelier (axo-axonic) cells*: target axon initial segment → precise spike timing control.
- *CCK⁺ basket cells*: CB1R-expressing → endocannabinoid-mediated retrograde suppression of GABA release (DSI).
- *SOM⁺ bistratified cells and OLM (oriens-lacunosum-moleculare) cells*: target dendrites → θ-resonant, gate perforant vs Schaffer path inputs.
- *NPY⁺ Ivy cells*: slow, persistent inhibition; coupled to sharp-wave ripples.

## Function

**Memory encoding — episodic and declarative memory.** The hippocampus binds spatially and temporally separate elements of experience (what, where, when) into coherent episodic memories by rapid indexing of neocortical representations. This "complementary learning systems" framework (O'Reilly & McClelland, 1994) posits: hippocampus performs fast, one-shot learning of specific episodes (high plasticity, interference-prone) while neocortex extracts slow statistical regularities (semantic knowledge, stable). The index theory (Teyler & DiScenna) proposes that the hippocampus stores pointers to neocortical patterns rather than the patterns themselves.[^guyton-hall]

**Spatial navigation and cognitive map.** Place cells (CA1/CA3 pyramidal neurons, O'Keefe 1971) fire selectively when the animal is at a specific location in an environment ("place field," 0.5–5 m in humans). Place cell assemblies collectively represent the animal's position as a population code. Grid cells (EC layer II/III, Mosers 2005) fire at multiple locations arranged in a hexagonal lattice — providing a metric coordinate system. Head-direction cells (presubiculum, anterior thalamus) encode heading angle. These three cell types form an integrated navigation system. In humans, hippocampal place cells have been recorded during virtual reality navigation (Ekstrom et al., 2003 — intracranial EEG) and in spatial planning tasks.[^alberts-mol-cell-biology]

**Long-term potentiation (LTP) — cellular mechanism of memory.**
- *Induction* (Bliss & Lømo, 1973): High-frequency stimulation (HFS, 100 Hz, 1 s) of Schaffer collaterals → burst of glutamate → AMPAR-mediated depolarisation → NMDAR Mg²⁺ block relieved → Ca²⁺ influx through NMDAR.
- *Expression* (early LTP, E-LTP, ≤1 h): Ca²⁺ → CaMKII autophosphorylation (T286) → constitutive activation → GluA1 Ser831 phosphorylation → AMPAR conductance ↑; Rab11/NSF-dependent AMPAR exocytosis → ↑synaptic AMPAR number (silent synapse recruitment).
- *Consolidation* (late LTP, L-LTP, >1 h): PKA → CREB (Ser133) → transcription of Arc (AMPAR endocytosis regulation), BDNF (→TrkB→MAPK/ERK→new protein synthesis), CPEB → local dendritic mRNA translation; spine growth (stable structural LTP).[^guyton-hall]

**Long-term depression (LTD).**
- Low-frequency stimulation (LFS, 1 Hz, 900 pulses) → moderate Ca²⁺ via NMDAR (lower peak than LTP) → preferential activation of protein phosphatases (PP1, PP2B/calcineurin) → GluA2 Ser880 dephosphorylation → GRIP displacement → GluA2-dependent AMPAR endocytosis → ↓synaptic strength.
- mGluR-LTD (type I mGluR, Gq → IP₃/DAG; prominent in CA1 stratum oriens): Dependent on local dendritic protein synthesis (CPEB, FMRP); dysregulated in Fragile X syndrome (excess mGluR-LTD due to ↑AMPAR endocytosis → cognitive impairment).

**Hippocampal oscillations.**
- *θ oscillations* (4–8 Hz): During active locomotion and REM sleep; driven by medial septal GABAergic/cholinergic pacemaker + entorhinal cortex input + CA1 OLM interneurons. θ phase-gates synaptic plasticity: LTP preferential at θ peak, LTD at θ trough (θ phase-code for memory encoding). ACh from medial septum (via fornix) → M1/M3 on pyramidal neurons and M2 on interneurons → enhances θ power.
- *γ oscillations* (30–100 Hz): Nested within θ; generated by PV⁺ basket cell networks (pyramidal-interneuron gamma, PING); bind together neural ensembles encoding separate features of a memory; disrupted in schizophrenia (↓PV⁺ cells, ↓NMDAR on interneurons → ↓γ → disorganised memory binding).[^alberts-mol-cell-biology]
- *Sharp wave-ripples* (SWRs, 80–200 Hz): During slow-wave sleep and quiet wakefulness; originate from CA3 synchronous bursts → CA1 (Schaffer collaterals) → CA1 ripples (PV⁺ basket cell oscillations); replay of recent experiences in compressed, accelerated form → hippocampal-to-neocortical memory transfer → systems consolidation (declarative memory stabilisation).

**Adult neurogenesis in the dentate gyrus.**
- Neural stem cells in the SGZ (type 1 radial glia-like cells: Sox2⁺, GFAP⁺, nestin⁺) → asymmetric division → type 2 intermediate progenitors (DCX⁺) → newborn granule cells (Prox1⁺) → integrate into trisynaptic circuit within 4–6 weeks; undergo period of increased plasticity (4–6 weeks post-mitosis) during which NMDAR-dependent LTP thresholds are lower than mature granule cells.
- Function: Pattern separation (new neurons provide orthogonal representations for similar inputs), temporal encoding (neurogenesis rate may code elapsed time in episodic memories).
- Regulation: Enhanced by aerobic exercise (↑VEGF, ↑BDNF), enriched environment, learning; suppressed by chronic stress (↑glucocorticoids → ↓SGZ proliferation, ↑apoptosis), ageing, alcohol, irradiation, depression.[^guyton-hall]

## Connections

- `part-of` → **[Brain](../../06-organ/brain/README.md)** — Hippocampus is a bilateral archicortical structure in the medial temporal lobe; CA1/CA3 pyramidal neurons and dentate gyrus granule cells form the trisynaptic circuit for declarative memory encoding and spatial navigation.
- `modulates` → **[Neuron](../../04-cellular/neuron/README.md)** — CA1 pyramidal neurons exhibit LTP at Schaffer collateral synapses via NMDAR-dependent Ca²⁺/CaMKII → AMPAR insertion; place cells encode spatial location; dentate gyrus neurogenesis contributes to pattern separation and episodic memory.
- `modulates` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Schaffer collateral and perforant path synapses are glutamatergic (AMPAR+NMDAR); NMDAR is the coincidence detector for LTP; excitotoxic glutamate release in ischaemia selectively kills CA1 pyramidal neurons (Sommer sector).
- `modulates` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Hippocampus expresses high GR and MR levels; acute cortisol → ↑synaptic plasticity; chronic cortisol → ↓BDNF, ↓neurogenesis, CA3 dendritic atrophy, hippocampal volume reduction — basis of stress-induced depression and PTSD.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF/TrkB drives L-LTP and dentate gyrus neurogenesis; antidepressants ↑BDNF/CREB → neurogenesis required for antidepressant efficacy (Santarelli 2003); chronic cortisol ↓BDNF → hippocampal atrophy in depression/PTSD; ketamine → rapid BDNF release → rapid antidepressant action.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin (5-HT1A/5-HT4) modulates hippocampal neuroplasticity; 5-HT1A in DG granule cells and CA1 pyramidal neurons; SSRIs ↑5-HT → ↑BDNF/TrkB → ↑SGZ neurogenesis → antidepressant effect delayed 2-4 weeks; 5-HT depletion impairs pattern separation and memory consolidation.
- `connects-to` → **[Alzheimer's Disease](../../07-system/alzheimers-disease/README.md)** — Hippocampus and entorhinal cortex are earliest sites of NFT deposition (Braak I-II) and Aβ synaptic failure; hippocampal MRI atrophy is the earliest AD biomarker; CA1 Sommer sector is selectively vulnerable; lecanemab (anti-Aβ) slows hippocampal atrophy and memory decline.

## Pathology

**Alzheimer's disease (AD).** The hippocampus and its afferent entorhinal cortex are the earliest sites of neurofibrillary tangle (NFT) deposition (hyperphosphorylated tau, Braak stages I–II → III–IV → V–VI) and secondary neuronal loss. Amyloid-β plaques (Aβ₁₋₄₂ oligomers → soluble oligomers → fibrils → plaques) impair synaptic plasticity, activate microglia (TREM2-dependent) → neuroinflammation → spread of tau pathology. Clinically: hippocampal atrophy on MRI (entorhinal + CA1) → declarative memory loss (anterograde amnesia) precedes other cognitive domains by years. Biomarkers: CSF Aβ₁₋₄₂↓, tau/p-tau↑; amyloid PET (florbetapir); tau PET. DMT: lecanemab, donanemab (anti-Aβ monoclonal antibodies → slow progression); symptomatic: acetylcholinesterase inhibitors (donepezil, rivastigmine — augment cholinergic tone) + memantine (NMDAR partial antagonist).[^guyton-hall]

**Hippocampal sclerosis and temporal lobe epilepsy (TLE).** Selective neuronal loss in CA1 (Sommer sector), CA3, and hilar neurons (mossy cells and PV⁺ interneurons) following prolonged febrile seizures in childhood or status epilepticus → reactive gliosis → hippocampal sclerosis. Loss of inhibitory interneurons → reduced feed-forward inhibition → CA3 recurrent circuit hyperexcitability → spontaneous temporal lobe seizures. TLE is the commonest cause of medically intractable epilepsy. Surgical resection (temporal lobectomy / selective amygdalohippocampectomy) → ~60–70% seizure-free at 2 years; MRI volumetry and EEG concordance required for localisation.[^alberts-mol-cell-biology]

**Depression and hippocampal atrophy.** Recurrent major depressive disorder (MDD) is associated with hippocampal volume reduction (~8–19% in severe/chronic cases) — driven by glucocorticoid-mediated suppression of BDNF (→↓TrkB→↓CREB signalling) and adult neurogenesis. The "neurogenesis hypothesis of depression" (Santarelli et al., 2003): SSRI antidepressants require hippocampal neurogenesis to exert behavioural efficacy in animal models. Aerobic exercise (↑BDNF, ↑IGF-1 → ↑SGZ proliferation) partly reverses hippocampal atrophy. Ketamine (NMDAR antagonist → rapid AMPAR-mediated synaptic potentiation, BDNF release → antidepressant within hours, vs 2–4 weeks for SSRIs).

**PTSD.** Hippocampal volume reduction (bilateral, ~6–8%) in PTSD compared to trauma-exposed non-PTSD controls — predisposing factor rather than purely a consequence. Impaired hippocampal contextual memory → failure to discriminate safe from dangerous contexts → generalised fear (conditioned fear without context discrimination). Impaired extinction of conditioned fear (vmPFC-hippocampus circuit dysfunction). Treatment: trauma-focused CBT, EMDR; MDMA-assisted psychotherapy (Phase 3); propranolol reconsolidation interference; stellate ganglion block (experimental).[^guyton-hall]

**Limbic encephalitis.** Autoimmune encephalitis targeting hippocampal and limbic structures:
- Anti-NMDAR encephalitis (NR1 subunit IgG, often paraneoplastic — ovarian teratoma in young women): acute psychosis, stereotypies, seizures, autonomic instability, coma; 80% recovery with immunotherapy (steroids, IVIG, rituximab) + tumour removal.
- Anti-LGI1 (leucine-rich glioma-inactivated protein 1): faciobrachial dystonic seizures, hyponatraemia, hippocampal atrophy.
- Anti-CASPR2, anti-AMPAR, anti-GABA-B: each with distinct clinical phenotypes.
All forms: ↑CSF protein, limbic hyperintensity on FLAIR MRI (hippocampus/amygdala), EEG slow waves → urgent immunotherapy.[^alberts-mol-cell-biology]

## See Also

- [brain](../../06-organ/brain/README.md) — organ context; hippocampus as medial temporal lobe component
- [neuron](../../04-cellular/neuron/README.md) — principal cell type executing synaptic plasticity and place coding
- [glutamate](../../03-molecular/glutamate/README.md) — primary excitatory neurotransmitter at hippocampal synapses
- [gaba](../../03-molecular/gaba/README.md) — interneuron-mediated inhibition coordinating hippocampal oscillations
- [cortisol](../../03-molecular/cortisol/README.md) — stress hormone mediating hippocampal atrophy and neurogenesis suppression
- [serotonin](../../03-molecular/serotonin/README.md) — antidepressant-mediated hippocampal neurogenesis and plasticity
- [nervous-system](../../07-system/nervous-system/README.md) — systems context for hippocampal limbic function

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
