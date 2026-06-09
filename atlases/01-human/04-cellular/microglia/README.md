---
schema: human-scale-entry/v1
id: microglia
name: Microglia
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "CNS-resident macrophages (~5–20% of CNS cells) of haematopoietic (myeloid) origin — unique among glia. Yolk-sac progenitors seed the CNS before BBB formation; maintained by self-renewal (CSF1R/IL-34). Survey ~1000 µm³/min; prune synapses; clear Aβ; drive neuroinflammation."
aliases: ["CNS-resident macrophage", "brain macrophage", "microglial cell", "ramified microglia", "activated microglia"]
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
    note: "Microglia are the CNS-resident macrophages (5–20% of cells); yolk-sac origin, maintained by self-renewal via CSF1R/IL-34; ramified microglia survey ~1000 µm³/min; become amoeboid on activation."
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "Microglia prune synapses (C1q/C3-tagged via CR3); supply BDNF/IGF-1 in homeostasis; activated microglia (TNF-α, IL-1β, ROS, iNOS-NO) damage neurons in AD, PD, TBI; TREM2-driven DAM phagocytose Aβ."
  - target: 01-human/05-tissue/synapse
    relation: modulates
    note: "Microglial processes contact synapses at ~1000 µm³/min; complement-mediated synaptic pruning (C1q tags inactive synapses, CR3 on microglia drives engulfment) is critical for circuit refinement in CNS development."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Microglial NLRP3 inflammasome (Aβ, ATP, α-synuclein, uric acid) → caspase-1 → IL-1β/IL-18 → neuroinflammatory cascade; chronic neuroinflammation underlies ALS, AD, PD, TBI, and MS disease progression."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Spinal microglia are activated by nerve injury via P2X4R/P2X7R → BDNF release → neuronal TrkB → KCC2 downregulation → GABA becomes depolarizing → allodynia; microglial p38 MAPK drives BDNF secretion; minocycline attenuates neuropathic pain in rodent models."
  - target: 01-human/03-molecular/bdnf
    relation: modulates
    note: "Activated spinal microglia release BDNF via P2X4R-p38 MAPK after nerve injury; microglial BDNF acts on neuronal TrkB → KCC2 downregulation → GABA depolarizing → allodynia; microglia also express TrkB and are BDNF targets in homeostasis."
---

# Microglia

## Overview

Microglia are the resident macrophages of the central nervous system, constituting approximately 5–20% of all CNS cells depending on region — with higher densities in the substantia nigra, hippocampus, and basal ganglia compared with white matter [^alberts-mol-cell-biology]. They are unique among CNS glial cells in their haematopoietic (myeloid) rather than neuroectodermal origin, and unique among macrophage populations in their embryonic seeding and lifelong self-renewal without monocyte replacement under homeostatic conditions.

Unlike astrocytes, oligodendrocytes, and ependymal cells (all neuroectoderm-derived), microglia descend from primitive macrophage precursors of the embryonic yolk sac. In the mouse, these progenitors (E9.5) colonise the developing CNS before blood-brain barrier (BBB) formation and before definitive haematopoiesis begins in the bone marrow, establishing the long-lived parenchymal microglial pool. The equivalent process occurs in the first trimester of human development.

Homeostatic microglia display a characteristic ramified morphology: a small cell body bearing numerous thin, highly branched processes that extend and retract continuously, surveying approximately 1000 µm³ of parenchyma per minute and making transient contact with synapses, blood vessels, and neuronal soma [^guyton-hall]. Upon detection of injury, infection, or cellular stress, microglia rapidly retract processes, assume an amoeboid morphology, and adopt effector programs ranging from phagocytosis to neuroinflammatory cytokine secretion.

## Structure

**Homeostatic morphology.** Small soma (5–10 µm diameter) bearing 4–6 primary processes that branch extensively into secondary and tertiary processes spanning up to 50–75 µm. The cytoplasm is sparse; the nucleus is large relative to cell body size. Each microglial cell surveys a non-overlapping territorial domain of ~30,000–50,000 µm³; the entire brain parenchyma is tiled by these domains.

**Activated morphology.** Progressive process retraction accompanied by soma enlargement → hypertrophic (partially retracted, thickened processes) → amoeboid (large soma, few or no processes, mobile). Amoeboid microglia accumulate at sites of injury, infection, or amyloid plaque deposition.

**Unique transcriptome.** Microglia express a signature gene set that distinguishes them from all other CNS cells and from peripheral macrophages: *P2RY12* (purinergic receptor for ADP/ATP), *TMEM119* (homeostatic marker), *TREM2* (triggering receptor on myeloid cells 2 — recognises lipids, myelin, phosphatidylserine), *SALL1* (microglial identity TF, maintained by CNS environment), *Iba1/AIF1* (ionised calcium-binding adaptor molecule 1 — cytoskeletal, standard histological marker), and *CX3CR1* (fractalkine receptor — binds CX3CL1 constitutively expressed on neurons, maintaining microglial quiescence) [^alberts-mol-cell-biology].

**Key surface receptors.** TLR1–9 (pattern recognition); TREM2 + DAP12 (signalling complex); CSF1R (M-CSF and IL-34 receptor — survival/proliferation signal); P2RY12 (purinergic — ATP gradient sensing → injury chemotaxis); CR3/CD11b (complement receptor 3 — phagocytosis of C3b-opsonised targets including synapses); CX3CR1 (fractalkine — neuron-microglia communication); CLEC7A (dectin-1 — fungal β-glucan, activated state); MHC-II (low in homeostasis, upregulated on activation).

## Function

### 1. Homeostatic Surveillance

In the healthy CNS, ramified microglia perform continuous, rapid, non-directed surveillance of the parenchyma [^guyton-hall]. This is not passive — process motility is driven by P2RY12 (purinergic receptor detecting extracellular ATP/ADP released from stressed or damaged cells, creating a chemotactic gradient) and CX3CR1 (fractalkine receptor keeping microglia in a surveillant, non-inflammatory state via constitutive neuronal CX3CL1 signalling). Surveillance rate: ~1000 µm³/min per cell, meaning the entire brain parenchyma is sampled approximately every few hours [^alberts-mol-cell-biology].

### 2. Synaptic Pruning

One of the most important developmental and homeostatic functions of microglia is the elimination of surplus synapses — a process essential for the refinement of neural circuits during development and implicated in synaptic loss in disease [^alberts-mol-cell-biology].

The complement cascade is the key molecular mediator: less-active or supernumerary synapses are tagged with C1q and C3 cleavage product C3b by the classical complement pathway. Microglia express complement receptor CR3 (CD11b/CD18), which binds C3b-opsonised presynaptic terminals and drives their engulfment by phagocytosis. This process is best characterised in the retinogeniculate projection (elimination of retinal ganglion cell axon synapses on lateral geniculate nucleus neurons) and hippocampal synaptic pruning. In Alzheimer's disease, aberrant reactivation of developmental synaptic pruning — driven by soluble Aβ oligomers triggering complement tagging of synapses — is thought to underlie early synaptic loss and cognitive decline.

### 3. Phagocytosis

Microglia phagocytose diverse cargoes [^guyton-hall]:
- Apoptotic neurons and cellular debris (via phosphatidylserine recognition by TREM2, MERTK, AXL)
- Myelin debris following axonal injury (critical for initiating remyelination; myelin fragments are recognised by TREM2)
- Amyloid-β plaques and fibrils (limited capacity; TREM2 R47H variant impairs this function)
- Pathogens (bacteria, fungi, viruses — via TLRs, CLEC7A, FcγRs)
- Glutamate-releasing synaptic vesicles (via LRP1)

Phagocytic efficiency is regulated by TREM2: TREM2 ligation by lipids, phosphatidylserine (on apoptotic cells), or Aβ-bound ApoE → DAP12 → Syk → PI3K → Akt → enhanced phagocytic cup formation, phagosome maturation, and lysosomal degradation.

### 4. Neuroinflammatory Activation

TLR/NLR/STING stimulation by PAMPs (LPS, viral RNA/DNA) or DAMPs (Aβ, α-synuclein aggregates, misfolded tau, HMGB1, ATP) activates microglia to a pro-inflammatory effector state [^alberts-mol-cell-biology]:

- **TLR4 → MyD88 → IRAK4 → TRAF6 → NF-κB** → TNF-α, IL-1β, IL-6, IL-12, CCL2, CXCL10
- **NLRP3 inflammasome** — assembled by MSU crystals, Aβ fibrils, silica, ATP (via P2X7) → caspase-1 → IL-1β and IL-18 maturation and secretion → pyroptosis (gasdermin D pore formation → cell death + IL-1β/IL-18 release)
- **iNOS (NOS2)** → NO production (reactive nitrogen species) → peroxynitrite (ONOO⁻) with superoxide → neuronal protein nitration, mitochondrial damage
- **NADPH oxidase (NOX2)** → superoxide → H₂O₂ → oxidative stress → lipid peroxidation in neuronal membranes

These responses are beneficial acutely (pathogen clearance) but chronically activated microglia (as in AD, PD, TBI) sustain a neuroinflammatory milieu that exacerbates neuronal damage and drives disease progression [^guyton-hall].

### 5. Neuroprotective Functions (Homeostatic/M2-like Microglia)

Not all microglial activation is deleterious. Homeostatic microglia and IL-4/IL-13-stimulated microglia adopt neuroprotective programs [^alberts-mol-cell-biology]:
- Secretion of neurotrophic factors: BDNF (brain-derived neurotrophic factor — supports synaptic plasticity and neuronal survival), IGF-1 (insulin-like growth factor 1 — neuroprotection, remyelination), NT-3
- Anti-inflammatory cytokines: IL-10 (suppresses TNF-α and IL-1β production), TGF-β1 (maintains microglial homeostatic phenotype via Smad2/3)
- Myelin debris clearance: essential prerequisite for remyelination by OPCs in MS and other demyelinating conditions; M2-like microglia express higher TREM2 and MerTK, promoting lipid phagocytosis

### 6. TREM2-APOE-DAM Axis (Alzheimer's Disease)

In Alzheimer's disease, microglia undergo a stereotyped transcriptional transition from homeostatic microglia (HM) to disease-associated microglia (DAM) [^alberts-mol-cell-biology]:

**Stage 1 DAM (TREM2-independent):** Downregulation of homeostatic genes (*P2RY12*, *TMEM119*, *CX3CR1*, *SALL1*); upregulation of *TYROBP/DAP12*, *ApoE*, *B2m*. This stage occurs in response to sensing amyloid pathology and does not require TREM2.

**Stage 2 DAM (TREM2-dependent):** TREM2 engagement by ApoE-lipid complexes or Aβ triggers Syk → PI3K → mTOR; upregulation of *CST7* (cystatin F), *LPL* (lipoprotein lipase — lipid metabolism), *SPP1* (osteopontin), *CLEC7A* (dectin-1), *ITGAX* (CD11c), *Cst3*, *APOE*. DAM cells cluster around amyloid plaques and attempt phagocytic clearance — but their capacity is overwhelmed in established AD.

AD GWAS risk genes are strongly enriched in microglia: *TREM2* (R47H → 3× AD risk), *CLU*, *CR1*, *BIN1*, *PICALM*, *MS4A cluster*, *ABCA7*, *PLCG2*, *ABI3* — all expressed in microglia and implicated in phagocytosis, lipid metabolism, or endolysosomal trafficking.

## Lifecycle

**Embryonic origin.** Primitive macrophage progenitors arise in the yolk sac at E8.5 (mouse equivalent) and migrate to the developing CNS during E9.5–E12.5, before BBB closure and before definitive bone-marrow haematopoiesis. These precursors express Runx1, PU.1 (SPI1), and C-kit at early stages; transitional cells express CX3CR1 as they enter the brain parenchyma [^alberts-mol-cell-biology].

**Maturation.** From E13 through postnatal day 3 (mouse), immature microglia differentiate into ramified adult microglia under the influence of CNS-derived factors: TGF-β1 (from astrocytes and microglia themselves — maintains SALL1 expression and homeostatic identity), IL-34 and M-CSF (CSF1R ligands), and colony-stimulating factor 1. Key transcription factors: IRF8, PU.1, SALL1 (unique to microglia vs. peripheral macrophages — maintained by the CNS environment; SALL1 deletion converts microglia toward peripheral macrophage-like identity).

**Maintenance.** Adult microglia are maintained predominantly by local self-renewal — detected by EdU/BrdU incorporation in Ki67+ microglia. Half-life is estimated at several months in the mouse. Under homeostatic conditions, circulating monocytes do NOT substantially contribute to the resident microglial pool — a key distinction from most other tissue macrophage populations [^guyton-hall].

**Response to injury/systemic inflammation.** After TBI, stroke, or severe systemic infection, bone-marrow-derived Ly6C-hi classical monocytes can enter the CNS via disrupted BBB and transiently adopt microglial-like phenotypes. However, they do not durably engraft as long-lived microglia under most circumstances; after resolution, the microglial pool is re-established from surviving resident microglia by proliferation.

**Experimental depletion and repopulation.** CSF1R inhibitors (PLX5622, PLX3397) deplete >95% of microglia within 1–2 weeks in rodents; upon drug withdrawal, microglia rapidly repopulate from residual progenitors within 7–14 days — a model system revealing microglial function in disease contexts.

## Connections

- `part-of` → **[Brain](../../06-organ/brain/README.md)** — microglia are CNS-resident macrophages (5–20% of cells); maintained by self-renewal via CSF1R/IL-34; surveillance rate ~1000 µm³/min; amoeboid on activation.
- `modulates` → **[Neuron](../neuron/README.md)** — synaptic pruning (C1q/C3-tagged synapses via CR3); BDNF/IGF-1 support in homeostasis; TNF-α, IL-1β, ROS, iNOS-NO → neuronal damage in AD, PD, TBI; TREM2-driven DAM phagocytose Aβ.
- `modulates` → **[Synapse](../../05-tissue/synapse/README.md)** — complement-mediated pruning (C1q/C3 tag inactive synapses → CR3 on microglia → engulfment); critical for circuit refinement in CNS development; aberrant pruning underlies early synaptic loss in AD.
- `modulates` → **[Nervous System](../../07-system/nervous-system/README.md)** — NLRP3 inflammasome → caspase-1 → IL-1β/IL-18 → neuroinflammatory cascade; chronic neuroinflammation underlies AD, PD, ALS, TBI, and MS disease progression.
- `connects-to` → **[Neuropathic Pain](../../07-system/neuropathic-pain/README.md)** — spinal microglia activated by nerve injury via P2X4R → BDNF release → neuronal TrkB → KCC2 downregulation → GABA becomes depolarizing → allodynia; microglial p38 MAPK drives BDNF secretion; minocycline attenuates neuropathic pain in rodent models.
- `modulates` → **[BDNF](../../03-molecular/bdnf/README.md)** — activated spinal microglia release BDNF via P2X4R-p38 MAPK after nerve injury; microglial BDNF acts on neuronal TrkB → KCC2 downregulation → GABA depolarizing → allodynia; microglia also express TrkB and are BDNF targets in homeostasis.

## Pathology

### Alzheimer's Disease

TREM2 loss-of-function variants (R47H: ~3× risk; R62H: ~1.7× risk) impair microglial lipid sensing, phagocytosis, and DAM transition → failure of amyloid plaque containment → unchecked Aβ spread and accelerated tau propagation. NLRP3 inflammasome activation by Aβ fibrils and oligomers → caspase-1 → IL-1β/IL-18 → complement-mediated synaptic pruning → dendritic spine loss and cognitive decline. Microglia around plaques in AD brains are dystrophic, with fragmented processes and impaired phagocytic capacity [^alberts-mol-cell-biology].

### Parkinson's Disease

α-Synuclein aggregates (released from degenerating dopaminergic neurons of the substantia nigra) are recognised by microglial TREM2, TLR1/2/4, and CD36 → NF-κB → TNF-α, IL-1β → dopaminergic neuron injury in a feedforward loop. NLRP3 inflammasome in microglia, activated by α-synuclein fibrils, drives caspase-1-mediated IL-1β secretion and pyroptosis. LRRK2 (leucine-rich repeat kinase 2 — most common familial PD mutation) is highly expressed in microglia; gain-of-function mutations → increased TLR4-driven inflammatory signalling [^guyton-hall].

### Multiple Sclerosis

Activated microglia and infiltrating macrophages are present at active MS lesion borders (shadow plaques, active/smouldering plaques). They produce TNF-α, IL-1β, NO, and reactive oxygen species → oligodendrocyte death and demyelination. Conversely, M2-like microglia and foamy macrophages that have phagocytosed myelin debris are essential for remyelination — clearing the inhibitory myelin debris that blocks OPC differentiation. The balance between inflammatory and phagocytic (lipid-processing) microglial states determines lesion progression vs. repair.

### ALS (Amyotrophic Lateral Sclerosis)

TDP-43 and C9orf72 dipeptide repeat aggregates from degenerating motor neurons activate microglia via cGAS/STING and NF-κB → sustained TNF-α and IL-6 production → motor neuron injury. Microglia in ALS spinal cord are chronically activated; SOD1-G93A mouse model shows that microglial NF-κB activation accelerates disease progression — selective NF-κB deletion in myeloid cells delays onset and extends survival [^alberts-mol-cell-biology].

### Nasu-Hakola Disease (PLOSL)

Loss-of-function mutations in either *TREM2* or *TYROBP* (DAP12) cause polycystic lipomembranous osteodysplasia with sclerosing leukoencephalopathy (PLOSL) — a rare autosomal-recessive disease characterised by early-onset progressive dementia and bone cysts. Demonstrates that TREM2-DAP12 signalling is essential for microglial homeostatic function in the CNS and for osteoclast function in bone (osteoclasts are also TREM2+), linking microglial biology to skeletal disease [^guyton-hall].

[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022. [NCBI Bookshelf →](https://www.ncbi.nlm.nih.gov/books/NBK26880/)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [Publisher →](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
