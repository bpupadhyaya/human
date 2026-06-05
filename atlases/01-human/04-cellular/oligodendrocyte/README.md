---
schema: human-scale-entry/v1
id: oligodendrocyte
name: Oligodendrocyte
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "CNS myelin-forming glia; one cell myelinates 15–40 axon segments, boosting conduction from ~0.5 to ≥70 m/s via saltatory conduction. OPCs (NG2+PDGFRα+) persist as adult progenitors. MCT1-derived lactate provides metabolic support to axons independent of insulation."
aliases: ["OL", "myelinating glia", "CNS myelin-forming cell", "OPC", "oligodendrocyte precursor cell"]
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
    note: "Oligodendrocytes form myelin sheaths across all CNS white matter tracts; corpus callosum, corona radiata, cerebellar peduncles, and optic nerves have the highest OL density; OL loss disrupts saltatory conduction throughout the CNS."
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "Oligodendrocytes myelinate 15–40 axon segments each (saltatory conduction → ≥70 m/s); provide metabolic lactate via MCT1→axonal MCT2; axonal glutamate activates OPC NMDA receptors → mTOR → MBP translation."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "White matter integrity (OL myelination) determines conduction velocity, neural synchrony, and cognition; demyelination (MS, MOGAD, PML) causes conduction block, sensory/motor deficits; OPC remyelination partially restores function."
  - target: 01-human/05-tissue/synapse
    relation: modulates
    note: "Myelinated axons propagate action potentials rapidly to synaptic terminals; OL metabolic support via MCT1-derived lactate sustains high-frequency firing; demyelination disrupts temporal precision of synaptic transmission."
---

# Oligodendrocyte

## Overview

Oligodendrocytes are the myelin-forming glial cells of the central nervous system. Unlike Schwann cells (PNS myelinating glia — one Schwann cell per one axon segment), a single oligodendrocyte extends processes to myelinate 15–40 distinct axon internodal segments, each segment spanning 100–1500 µm in length and wrapped by approximately 150 compacted membrane layers [^alberts-mol-cell-biology]. This architecture is highly efficient — a single oligodendrocyte can insulate hundreds of metres of axonal surface area in total.

The functional consequence of myelin is profound: unmyelinated axons conduct action potentials at ~0.5–2 m/s via continuous propagation; myelinated axons conduct via saltatory conduction (action potentials jump between nodes of Ranvier where voltage-gated Na+ channels cluster) at speeds of ≥70 m/s for large-diameter fibres [^guyton-hall]. Myelination is therefore not merely insulation — it is a conduction velocity amplifier that makes the rapid sensorimotor integration, language, and cognitive functions of the large mammalian brain possible.

Two functionally and molecularly distinct populations of oligodendrocyte-lineage cells exist in the adult CNS:

1. **Oligodendrocyte precursor cells (OPCs)** — NG2+ PDGFRα+ OLIG2+ cycling or quiescent progenitors distributed throughout grey and white matter (~5% of all CNS cells in adults). OPCs are the source of new oligodendrocytes for limited adult myelination and remyelination.
2. **Mature oligodendrocytes (MO)** — CC1+ MBP+ PLP1+ MOG+ MAG+ terminally differentiated, post-mitotic myelin-forming cells.

Oligodendrocytes are derived from the ventral ventricular zone (neuroepithelium) via three waves of specification in the mouse (E12.5 from the medial ganglionic eminence, E15.5 from the lateral and caudal ganglionic eminences, and postnatally from the cortex) — all sharing the OLIG2 → NKX2.2 → MBP/PLP differentiation pathway [^alberts-mol-cell-biology].

## Structure

### OPC (Oligodendrocyte Precursor Cell)

**Morphology.** Bipolar or stellate cell body (8–15 µm) bearing 2–6 processes; NG2 (CSPG4) proteoglycan coat visible as a pericellular matrix; PDGFRα (PDGFR-alpha) on surface; responds to PDGF-AA (main proliferative signal) and NT-3, CNTF, IGF-1 (survival/differentiation signals).

**State.** OPCs cycle slowly (weeks–months) or are quiescent; proliferate robustly after demyelinating injury (driven by PDGF-AA, FGF2, EGF); remain undifferentiated in the presence of inhibitory signals — LINGO-1 (leucine-rich repeat and Ig domain-containing Nogo receptor-interacting protein 1), Nogo-A (RTN4 — expressed on myelin and neurons), chondroitin sulphate proteoglycans (CSPGs — upregulated in the glial scar after injury), PSA-NCAM (polysialylated neural cell adhesion molecule on immature axons) [^alberts-mol-cell-biology].

**Electric properties.** OPCs express functional AMPA and NMDA receptors (GluN2C/D-containing NMDARs at glutamatergic synapses) — active neurons release glutamate that depolarises OPCs → Ca²⁺ influx → mTOR → MBP (myelin basic protein) translation. This activity-dependent myelination couples circuit activity to white matter architecture.

### Mature Oligodendrocyte

**Morphology.** Larger cell body (15–20 µm) with multiple processes that broaden into flat myelin membrane sheets wrapping around axons. The processes elongate to axons (up to 200–300 µm away), spiral ~150 times around the internode, and compact into myelin.

**Myelin ultrastructure.**
- **Composition:** ~70% lipid / ~30% protein (highest lipid content of any biological membrane)
  - Lipids: cholesterol (~25 mol%), galactocerebroside/GalC (~20%), sulfatide (~5%), plasmalogen phospholipids, sphingomyelin
  - Proteins: MBP (myelin basic protein — ~30% of total; positively charged, bridges adjacent cytoplasmic leaflets via electrostatic interactions → compacts the major dense line), PLP1/DM20 (proteolipid protein — ~50% of total; most abundant CNS myelin protein; 4-pass transmembrane; stabilises extracellular intraperiod line), MOG (myelin oligodendrocyte glycoprotein — ~0.01–0.05%; outermost lamella; target of anti-MOG IgG in MOGAD), MAG (myelin-associated glycoprotein — inner periaxonal space; mediates axon-OL contact; inhibits axon regeneration via NgR1), MOBP (myelin-associated oligodendrocyte basic protein), CNP (2',3'-cyclic nucleotide 3'-phosphodiesterase — non-compact regions)

- **X-ray diffraction periodicity:** major dense line (cytoplasmic faces) ~2.9 nm; intraperiod line (extracellular faces) ~3.9 nm; total myelin period ~11.9 nm (measured in situ)

### Node of Ranvier

The node is the unmyelinated gap (1–2 µm) between adjacent internodes where action potential regeneration occurs [^guyton-hall]:
- **Node:** Nav1.6 (predominant in mature nodes), Nav1.1; AnkyrinG + βIV-spectrin scaffold anchors channels; NrCAM, contactin, neurofascin-186 (axonal)
- **Paranode:** Caspr1 (contactin-associated protein) + contactin on axon → neurofascin-155 on myelin paranodal loops — high-resistance junctions that prevent current spread across the internode (critical for saltatory conduction efficiency)
- **Juxtaparanode:** Kv1.1/1.2 (KCNA1/2 — low-threshold K+ channels; maintain repolarisation; mutated in neuromyotonia); Caspr2 + TAG-1
- **Internode:** Kv1 channels under compact myelin (normally inaccessible — become exposed and pathological after demyelination, causing conduction failure)

## Function

### Myelination and Saltatory Conduction

The primary function of oligodendrocytes is to form compact myelin, enabling saltatory conduction [^guyton-hall]. Key parameters:

| Axon type | Diameter | Conduction velocity | Myelinated? |
|:---|:---|:---|:---|
| Aα (motor, proprioception) | 13–20 µm | 70–120 m/s | Yes |
| Aβ (tactile) | 6–12 µm | 33–75 m/s | Yes |
| Aδ (pain, temperature) | 1–5 µm | 3–30 m/s | Lightly |
| C fibres (pain, autonomic) | 0.2–1.5 µm | 0.5–2 m/s | No |

The capacitance of the axonal membrane is reduced ~100-fold by myelin wrapping, dramatically reducing the charging current needed per unit length. The net effect: conduction velocity scales with axon diameter in myelinated fibres (velocity ≈ 6× diameter [µm] m/s) vs. diameter^0.5 for unmyelinated fibres.

### Activity-Dependent Myelination

New myelination in the adult CNS (primarily of previously unmyelinated or partially myelinated axons) is driven by neuronal activity [^alberts-mol-cell-biology]:
1. Active axons release glutamate from vesicles at axo-OPC synapses → activates NMDA and AMPA receptors on OPC → Ca²⁺ → Akt/mTOR → increased MBP and PLP translation → myelin synthesis
2. ATP release from active axons → P2Y1 receptor on OPCs → Ca²⁺ → promotes OPC differentiation
3. Active axons release BDNF and LIF → OPC differentiation signals

This activity-dependence of myelination is a mechanism by which learning and experience reshape white matter — a biological basis for white matter changes observed in trained musicians, bilinguals, and following motor skill acquisition (detected by MRI diffusion tensor imaging changes in fractional anisotropy).

### Metabolic Support of Axons (MCT1 Shuttle)

Beyond insulation, oligodendrocytes provide critical metabolic support to ensheathed axons via the monocarboxylate transporter 1 (MCT1) expressed in compact myelin [^alberts-mol-cell-biology]:

- Oligodendrocytes import glucose and generate lactate via aerobic glycolysis → export lactate via MCT1 in compact myelin → lactate enters the periaxonal space → taken up by axons via MCT2 → oxidative phosphorylation in axonal mitochondria → ATP for ion pump function (Na+/K+-ATPase) during sustained high-frequency firing

This is analogous to the astrocyte-neuron lactate shuttle, but delivered directly through the myelin sheath. Critically, heterozygous deletion of *MCT1* specifically in oligodendrocytes (without causing demyelination) causes axonal degeneration in mice — demonstrating that metabolic support is an OL function independent of myelin insulation and that its loss is sufficient to cause neurodegeneration.

## Lifecycle

**Specification.** Ventral progenitors in the ventricular zone co-express OLIG2 + NKX2.2 → committed OPC identity. In the spinal cord, the majority arise from the pMN domain (motor neuron progenitor domain) that also generates motor neurons — timed by Ngn2 (neuronal) vs. OLIG2/NKX2.2 (OL) fate switch. In the brain, sequential waves from MGE, LGE, and cortical VZ generate the full adult OL population [^alberts-mol-cell-biology].

**OPC proliferation and migration.** OPCs proliferate in response to PDGF-AA (PDGFR-α), FGF2, and EGF; migrate along axon tracts guided by semaphorin and netrin gradients; populate both white and grey matter. In the adult CNS, OPCs remain the only mitotically active cell type under homeostatic conditions.

**Differentiation into mature OL.** When OPC contacts a myelination-competent axon: LINGO-1, PSA-NCAM, and CSPG inhibitory signals must be overcome or cleared → Akt/mTOR activation (key signalling node for myelin protein synthesis) → process extension → membrane wrapping → compaction (exclusion of cytoplasm between membrane leaflets mediated by MBP electrostatic interactions and ZO-1/14-3-3 from non-compact regions). Required transcription factors: YY1 (represses OPC identity genes), ZEB2, myelin regulatory factor (MYRF — master OL differentiation TF, cleaves itself from ER membrane → nucleus → drives MBP, PLP, MOG transcription) [^alberts-mol-cell-biology].

**Maturation and maintenance.** Mature oligodendrocytes are post-mitotic and long-lived (years); they do not regenerate from themselves. New OLs arise only from OPC differentiation. Thyroid hormone (T3) is a potent pro-myelination signal (promotes OPC differentiation and myelin protein synthesis); its deficiency in neonates → cretinism (hypomyelination → intellectual disability). Vitamin D and retinoic acid also regulate OPC differentiation.

**Adult remyelination.** After demyelinating injury, resident OPCs proliferate (within days), migrate to the lesion (weeks), and differentiate into new myelinating OLs (weeks–months). Remyelinated internodes are shorter and thinner than original. In MS chronic lesions, OPCs are often present but fail to differentiate — "remyelination failure" — due to persistence of inhibitory signals (LINGO-1, CSPG, Semaphorin 3A, PSANCAM) and loss of pro-differentiation signals (absent BDNF, IGF-1 from inflammatory microenvironment). Therapeutic targets include anti-LINGO-1 (opicinumab), clemastine (muscarinic M1/M3 receptor antagonist → promotes OPC differentiation), and bexarotene (RXR agonist) [^guyton-hall].

## Connections

- **Part of:** [brain](../../06-organ/brain/README.md) — form myelin sheaths across all CNS white matter; corpus callosum, corona radiata, and optic nerves have highest OL density.
- **Modulates:** [neuron](../neuron/README.md) — saltatory conduction (≥70 m/s); MCT1 lactate → MCT2 axon metabolic support; activity-dependent myelination via OPC NMDA receptors → mTOR → MBP synthesis.
- **Modulates:** [nervous-system](../../07-system/nervous-system/README.md) — white matter integrity determines conduction velocity and cognitive function; demyelination (MS, MOGAD, PML) causes conduction block; OPC remyelination partially restores function.
- **Modulates:** [synapse](../../05-tissue/synapse/README.md) — myelination enables rapid propagation of action potentials to terminals; MCT1 lactate sustains high-frequency axonal firing; demyelination disrupts temporal precision and neural computation.

## Pathology

### Multiple Sclerosis (MS)

MS is the paradigmatic demyelinating disease — CNS-infiltrating CD4+ Th1/Th17 cells (recognising myelin peptides in the context of HLA-DRB1*15:01), CD8+ cytotoxic T cells, B cells, and macrophages destroy oligodendrocytes and myelin [^guyton-hall]. Acute lesions show oligodendrocyte apoptosis (TRAIL, perforin/granzyme, Fas-FasL) + complement-mediated myelin destruction. Axons are relatively preserved early but undergo progressive degeneration in chronic disease (Wallerian degeneration) — the substrate of irreversible disability.

Disease-modifying therapies target the adaptive immune infiltrate:
- **Natalizumab** (anti-α4-integrin/VLA-4 antibody) — blocks T cell and monocyte transmigration across BBB
- **Ocrelizumab / Ofatumumab** (anti-CD20) — depletes B cells (both mature and memory; not plasma cells)
- **Siponimod / Ozanimod** (S1PR1/5 modulators) — trap lymphocytes in secondary lymphoid organs, reducing CNS entry
- **Cladribine / Alemtuzumab** — lymphocyte depletion with immune reconstitution
OPC remyelination is limited in chronic MS due to inhibitory microenvironment and OPC senescence.

### MOGAD (MOG Antibody Disease)

Anti-MOG IgG1 antibodies target the outermost myelin lamella (MOG is expressed exclusively on the external surface) → complement activation (MOG is a complement activator) + ADCC → oligodendrocyte and myelin destruction. MOGAD presents as ADEM (acute disseminated encephalomyelitis), bilateral optic neuritis, or transverse myelitis — distinguished from MS by bilateral optic involvement, absence of OCBs, and good response to steroids and rituximab [^alberts-mol-cell-biology].

### Progressive Multifocal Leukoencephalopathy (PML)

JC virus (John Cunningham polyomavirus) specifically infects OPCs and mature oligodendrocytes (using serotonin receptor 5HT2A as entry receptor and agnoprotein for nuclear egress) → OL lysis → widespread demyelination → severe white matter destruction → death or profound disability. Occurs in immunosuppressed individuals (natalizumab [1:1000], rituximab, HIV/AIDS, organ transplant). No antiviral therapy; treatment is restoration of immune function (IRIS can paradoxically worsen initial outcome) [^guyton-hall].

### Pelizaeus-Merzbacher Disease (PMD)

X-linked recessive *PLP1* mutations (duplications, point mutations, or deletions of proteolipid protein 1 — the most abundant CNS myelin protein) → hypomyelination and dysmyelination → nystagmus (onset: infancy), hypotonia → cerebellar ataxia, dysarthria, progressive spastic quadriplegia. The most common point mutation (A242V) causes ER retention of PLP1 → oligodendrocyte ER stress → UPR → apoptosis. Severe form is fatal in early adulthood; milder SPG2 allelic variant (spastic paraplegia type 2) has longer survival [^alberts-mol-cell-biology].

### Vanishing White Matter Disease

Autosomal recessive mutations in *EIF2B1–5* (subunits of eukaryotic initiation factor 2B — a GEF that recycles eIF2-GDP to eIF2-GTP, required for translation initiation) → ER stress → constitutive ISR (integrated stress response) activation → astrocyte dysfunction → secondary OL dysfunction and white matter vanishing (visible on MRI as fluid-filled white matter replacing normal signal). Precipitated/worsened by febrile illness, head trauma, and fright (stress → ↑eIF2α-P → worsens already-impaired eIF2B function) [^guyton-hall].

## See Also

- [neuron](../neuron/README.md)
- [microglia](../microglia/README.md)
- [brain](../../06-organ/brain/README.md)
- [synapse](../../05-tissue/synapse/README.md)
- [nervous-system](../../07-system/nervous-system/README.md)
- [immune-system](../../07-system/immune-system/README.md)
- [atp](../../03-molecular/atp/README.md)

---

> **AI co-maintenance notice:** This entry is maintained with AI assistance. Content reflects standard textbook and peer-reviewed sources as cited; verify critical details against primary literature before clinical or research application.

[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022. [NCBI Bookshelf →](https://www.ncbi.nlm.nih.gov/books/NBK26880/)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [Publisher →](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
