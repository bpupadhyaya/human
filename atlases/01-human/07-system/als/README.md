---
schema: human-scale-entry/v1
id: als
name: ALS
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "ALS (30k US; 200k global) is a fatal motor neuron disease with progressive degeneration of upper and lower motor neurons; TDP-43 inclusions are the pathological hallmark in >97%; riluzole and edaravone extend survival modestly; tofersen (SOD1 ASO) is approved for familial ALS."
aliases: ["ALS", "amyotrophic lateral sclerosis", "Lou Gehrig's disease", "motor neuron disease", "MND", "SOD1 ALS", "TDP-43 ALS", "C9orf72 ALS", "FALS", "SALS"]
sources:
  - id: brown-2017-als-review
    type: peer-reviewed
    cite: "Brown RH, Al-Chalabi A. Amyotrophic lateral sclerosis. N Engl J Med. 2017;377(2):162-172."
    doi: "10.1056/NEJMra1603471"
    pmid: "28700839"
    url: "https://doi.org/10.1056/NEJMra1603471"
    accessed: "2026-06-08"
  - id: edaravone-als-2017
    type: peer-reviewed
    cite: "Writing Group on behalf of the Edaravone ALS 19 Study Group. Safety and efficacy of edaravone in well defined patients with amyotrophic lateral sclerosis: a randomised, double-blind, placebo-controlled trial. Lancet Neurol. 2017;16(7):505-512."
    doi: "10.1016/S1474-4422(17)30115-1"
    pmid: "28522180"
    url: "https://doi.org/10.1016/S1474-4422(17)30115-1"
    accessed: "2026-06-08"
  - id: miller-2023-tofersen-als
    type: peer-reviewed
    cite: "Miller TM, Cudkowicz ME, Genge A, et al. Trial of Antisense Oligonucleotide Tofersen for SOD1 ALS. N Engl J Med. 2022;387(12):1099-1110."
    doi: "10.1056/NEJMoa2204705"
    pmid: "36129998"
    url: "https://doi.org/10.1056/NEJMoa2204705"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/tdp-43
    relation: connects-to
    note: "TDP-43 cytoplasmic inclusions are the pathological hallmark of >97% of ALS; TARDBP mutations cause ~4% of familial ALS; nuclear TDP-43 loss disrupts splicing of STMN2 and UNC13A, driving axonal degeneration and synaptic failure in motor neurons."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate excitotoxicity via impaired astrocytic EAAT2 (GLT-1) uptake is a core ALS mechanism; riluzole (approved 1995) inhibits glutamate release and blocks persistent Na⁺ channels; AMPA receptor calcium permeability is increased in ALS spinal motor neurons."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Impaired autophagy (linked to mTOR hyperactivation and ULK1 dysfunction) contributes to TDP-43 and SOD1 aggregate accumulation in ALS; rapamycin reduces aggregate burden in ALS mouse models; p62/SQSTM1 (autophagy receptor) is a consistent component of ALS inclusions."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "ALS targets upper motor neurons in the primary motor cortex (Betz cells in layer V) and lower motor neurons in brainstem and spinal cord anterior horn; cortical hyperexcitability precedes clinical onset; cognitive and behavioral changes occur in ~50% (ALS-FTD continuum)."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "ALS reactive astrocytes lose EAAT2 → amplify glutamate excitotoxicity; ALS astrocytes kill co-cultured motor neurons in vitro; astrocyte-specific SOD1 removal prolongs mouse survival; non-cell-autonomous neurodegeneration via astrocytes is a core ALS mechanism."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "M1 microglia in ALS spinal cord release TNF-α, IL-1β, and NO → neurotoxic; NF-κB suppression in microglia prolongs SOD1 mouse survival; microglia transition from protective M2 to damaging M1 as ALS progresses; peripheral monocyte infiltration amplifies neuroinflammation."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "ALS causes dying-back axonopathy of peripheral motor nerves; neurofilament accumulation blocks axonal transport; EMG shows denervation (fibrillations, PSWs, giant units) in ≥3 body regions; peripheral motor nerve loss produces fasciculations, atrophy, and areflexia (LMN signs)."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "ALS is a motor neuron disease: it selectively kills the upper motor neurons of the cortex and the lower motor neurons of the brainstem and spinal cord, sparing most others; their extreme length and calcium-permeable AMPA receptors make these neurons uniquely vulnerable."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "ALS and CIDP both cause progressive weakness but at different sites: ALS is irreversible degeneration of the motor neuron itself, whereas CIDP is immune demyelination of the peripheral nerve — treatable and often reversible — so distinguishing them is critical."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "ALS shares the TDP-43 proteinopathy that also marks frontotemporal dementia and a subset of Alzheimer's: ~50% of ALS patients show cognitive change, C9orf72 expansion causes both ALS and FTD, and cytoplasmic TDP-43 aggregates link these diseases mechanistically."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: connects-to
    note: "ALS dismantles the neuromuscular junction early: as motor neurons degenerate, their axons die back and synapses retract from muscle endplates (denervation), causing fasciculations, weakness and wasting—this 'dying-back' NMJ loss may precede cell-body death."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "ALS devastates the musculoskeletal system through denervation: loss of upper and lower motor neurons produces progressive muscle weakness, wasting, spasticity and ultimately paralysis, while sparing sensation; the relentless decline in muscle function defines the disability."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Respiratory failure is the usual cause of death in ALS: degeneration of the motor neurons driving the diaphragm and accessory muscles progressively weakens ventilation, so non-invasive ventilation prolongs survival and forced vital capacity is a key prognostic and trial endpoint."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "ALS and myasthenia gravis cause weakness at opposite ends of the motor unit: ALS degenerates the motor neuron (upper and lower signs, fasciculations), while myasthenia blocks the neuromuscular junction (fatigable, treatable)—a prognosis-changing distinction."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "ALS and Parkinson's are neurodegenerations of protein misfolding hitting different neurons: ALS kills motor neurons (TDP-43), Parkinson's kills dopaminergic neurons (α-synuclein)—and ALS-parkinsonism-dementia overlaps hint at shared proteostasis failure."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Oligodendrocytes contribute to motor neuron death in ALS: beyond myelination they metabolically support axons, and dysfunctional ALS oligodendrocytes fail to supply lactate and degenerate—so glial, not just neuronal, failure drives the disease."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "ALS severs the acetylcholine signal to muscle: as motor neurons die, the terminals that release acetylcholine at the neuromuscular junction degenerate, so muscles lose stimulation and waste—unlike myasthenia gravis, where the receptor not the nerve is blocked."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Respiratory failure is how ALS kills: progressive weakness of the diaphragm and chest muscles cripples the lungs' bellows, causing hypoventilation, CO2 retention and eventual failure—so non-invasive ventilation is a mainstay that extends survival in ALS."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "ALS and multiple sclerosis both cause motor weakness but differ fundamentally: ALS is degenerative death of motor neurons, while MS is autoimmune demyelination with sensory and visual features—so ALS spares sensation and progresses without the relapses of MS."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper links the first ALS gene to oxidative stress: SOD1 is a copper-zinc superoxide dismutase, and many familial ALS mutations make the misfolded enzyme mishandle copper and generate toxic free radicals—so metal-dependent oxidative injury helps kill motor neurons."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "ALS is a relentless disease of the motor nervous system: it kills both upper motor neurons in the cortex and lower motor neurons in the brainstem and cord, so spasticity and wasting advance together until respiratory muscles fail."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Neuroinflammation drives ALS progression: activated microglia and astrocytes plus infiltrating immune cells turn from protective to toxic around dying motor neurons, so the immune system shapes how fast the disease advances—a target for emerging therapies."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "ALS is increasingly seen as a disease of failed protein clearance: motor neurons can't autophagy-degrade misfolded TDP-43 and SOD1, so toxic aggregates accumulate—linking many ALS genes (and the overlap with frontotemporal dementia) to a common disposal defect."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "ALS's SOD1 enzyme is a copper-zinc protein, and zinc is structural to it: mutations that disturb metal binding destabilize SOD1 into toxic aggregates, so the zinc (and copper) chemistry of this antioxidant enzyme sits at the heart of inherited ALS."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome is an emerging factor in ALS: altered gut flora and their metabolites may influence neuroinflammation and disease progression along the gut-brain axis, so the microbiome is being explored as a modifier of this relentless motor-neuron disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "ALS motor neurons die from calcium-driven excitotoxicity: excess glutamate floods them with calcium, and their unusually low calcium-buffering makes them especially vulnerable—the rationale for the glutamate-blunting drug riluzole."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells slow ALS: they restrain the harmful neuroinflammation of microglia, and patients with more functional Tregs progress slower—so expanding Tregs is an experimental therapy for this relentless motor neuron disease."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "ALS overlaps frontotemporal dementia in the hippocampus and cortex: TDP-43 pathology spreads beyond motor neurons to memory and behavior regions, so up to half of ALS patients develop cognitive change—uniting two diseases on one molecular spectrum."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Motor neurons in ALS run out of ATP: failing mitochondria cannot meet the huge energy demand of cells with metre-long axons, so the energy shortfall cripples transport and ion pumping and helps drive the neurons' death."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells infiltrate the dying motor regions in ALS: adaptive immunity adds to microglial inflammation, and the balance between these CD8 cells and protective regulatory T cells helps set how fast the disease advances."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "ALS motor neurons fire too easily through persistent sodium currents: this hyperexcitability stresses the cells and contributes to their loss, and it is partly why riluzole—which curbs sodium currents and glutamate—modestly slows the disease."
---

# ALS

## Overview

**Amyotrophic lateral sclerosis (ALS)**, also known as **Lou Gehrig's disease** or motor neuron disease (MND), is a progressive, invariably fatal neurodegenerative disease that selectively destroys **upper motor neurons (UMN)** in the primary motor cortex and **lower motor neurons (LMN)** in the brainstem and spinal cord anterior horn. The result is progressive paralysis of voluntary muscles — including limb muscles, bulbar muscles (swallowing, speech), and ultimately respiratory muscles — leading to death typically from respiratory failure within **2–5 years** of onset in most patients (10–15% survive >10 years; Stephen Hawking lived 55 years — an extraordinary outlier).

**Epidemiology [^brown-2017-als-review]:**
- Prevalence: ~30,000 in the US; ~200,000 globally
- Incidence: 2–3 per 100,000 per year (Western populations); lifetime risk ~1 in 300–400
- Peak onset: age 55–75 years; male:female ~1.3–1.5:1
- Genetics: ~10–15% familial (≥1 affected first-degree relative); 85–90% sporadic
- Prognosis: median survival ~2–3 years from symptom onset; ~50% die within 30 months; bulbar-onset worse than limb-onset

**ALS-FTD continuum:** ALS and frontotemporal dementia (FTD) are now recognized as ends of a disease spectrum. ~50% of ALS patients have some cognitive/behavioral changes; ~5–15% meet criteria for full FTD. C9orf72 repeat expansion is the most common cause of both ALS and ALS-FTD.

## Structure

### Upper and lower motor neuron signs

ALS diagnosis requires evidence of **both UMN and LMN degeneration** across ≥2 body regions (El Escorial revised criteria; Gold Coast criteria 2020):

| Finding | UMN dysfunction | LMN dysfunction |
|:---|:---|:---|
| **Reflexes** | Hyperreflexia (brisk DTRs) | Hyporeflexia/areflexia |
| **Muscle tone** | Spasticity | Flaccidity |
| **Pathological signs** | Babinski sign, Hoffman's sign, jaw jerk | Absent |
| **Muscle bulk** | Preserved early | Atrophy (denervation) |
| **Fasciculations** | Absent | Present (spontaneous motor unit discharges) |
| **EMG** | Central conduction delay | Fibrillations, positive sharp waves, giant motor units |

**Clinical phenotypes:**
- **Classic limb-onset ALS:** Asymmetric limb weakness (arm or leg); spreads to other limbs and bulbar muscles; accounts for ~70% of cases
- **Bulbar-onset ALS:** Dysarthria, dysphagia first; accounts for ~25%; faster progression; more common in women and older patients
- **Respiratory-onset ALS:** Dyspnea, orthopnea without limb involvement initially; rare (~3%); very rapid progression
- **Flail arm syndrome (brachial amyotrophic diplegia):** Bilateral arm weakness with LMN predominance; slower progression
- **Primary lateral sclerosis (PLS):** Pure UMN presentation >4 years without LMN signs — favorable prognosis; some eventually develop LMN signs (ALS)
- **Progressive muscular atrophy (PMA):** Pure LMN presentation; TDP-43 inclusions found at autopsy — ALS variant

### Genetics of ALS

| Gene | Mutation type | % familial ALS | % sporadic ALS | Protein function |
|:---|:---|:---|:---|:---|
| **C9orf72** | GGGGCC hexanucleotide repeat expansion (>30 copies; normal <10) | 40% | 5–10% | Nuclear export factor; RNA granule regulation; autophagy |
| **SOD1** | Missense (>180 mutations; A4V most common/lethal in North America) | 20% | 1–2% | Cu-Zn superoxide dismutase (toxic gain-of-function, not LOF) |
| **TARDBP** | Missense (>50 mutations in glycine-rich CTD) | 4% | <1% | RNA-binding protein TDP-43 |
| **FUS** | Missense (NLS mutations most severe; juvenile-onset FUS-ALS) | 4–5% | <1% | RNA-binding protein; similar to TDP-43 |
| **TBK1** | LOF (haploinsufficiency) | 4% | <1% | Tank-binding kinase 1; autophagy and NF-κB signaling |
| **NEK1** | LOF | 3% | ~1% | NIMA-related kinase; DNA damage response |
| **CHCHD10** | Missense | 2% | <1% | Mitochondrial inner membrane protein |
| **UBQLN2** | Missense (X-linked) | ~2% | <1% | Ubiquilin-2; ubiquitin-proteasome pathway |
| **OPTN** | Missense/deletion | 2% | <1% | Optineurin; autophagy receptor; NF-κB signaling |

**C9orf72 mechanism:** The GGGGCC expansion causes toxicity via three mechanisms:
1. **RNA foci:** Repeat-containing RNA forms nuclear foci that sequester RNA-binding proteins (hnRNP A3, Pur-α) → loss of normal RBP function
2. **Dipeptide repeat proteins (DPRs):** Repeat-associated non-ATG (RAN) translation produces 5 DPR species (poly-GA, poly-GR, poly-PR, poly-GP, poly-PA); poly-GR and poly-PR are highly toxic — disrupt nucleocytoplasmic transport, stress granule dynamics, and ribosome function
3. **C9orf72 haploinsufficiency:** C9orf72 protein regulates autophagy and lysosomal function; reduced levels impair autophagy of TDP-43/FUS aggregates

### Pathology

**TDP-43 proteinopathy:** >97% of all ALS cases (sporadic and familial, with the notable exception of SOD1-ALS and FUS-ALS which have distinct inclusions) show:
- Nuclear clearance of TDP-43 from affected neurons
- Cytoplasmic inclusions of ubiquitinated, phosphorylated, C-terminally cleaved TDP-43
- Loss of nuclear TDP-43 RNA processing function → cryptic exon inclusion in STMN2 and UNC13A → axon regeneration failure and synaptic deficiency

**SOD1 ALS:** A unique subtype — SOD1 inclusions rather than TDP-43; different cell biology; unique vulnerability of fast-fatigable motor neurons; tofersen (SOD1 ASO) is the first approved targeted therapy for any ALS genetic variant.

## Function

### Motor neuron vulnerability mechanisms

Why are motor neurons uniquely vulnerable in ALS? Multiple converging factors:

**Glutamate excitotoxicity:**
- Astrocytic glutamate uptake transporter EAAT2 (GLT-1) is selectively reduced in ALS spinal cord → elevated synaptic glutamate → persistent NMDA/AMPA receptor activation → intracellular Ca²⁺ overload
- ALS motor neurons express higher levels of **Ca²⁺-permeable AMPA receptors** (lower GluA2 levels → more Ca²⁺-permeable AMPARs) than typical CNS neurons — increasing vulnerability to Ca²⁺ toxicity
- Ca²⁺ overload → mitochondrial dysfunction → ROS production → protein aggregation amplification → cell death

**Axonal transport failure:**
- Motor neuron axons are among the longest in the body (>1 meter for lumbar motor neurons) → axonal transport is critically important and energetically costly
- Dynein/kinesin motor complex dysfunction in ALS → impaired retrograde transport of neurotropic signals (BDNF, GDNF) and organelles → failure of energy supply to distal axon
- Neurofilament accumulation in cell bodies and axons (a feature of ALS) → axonal transport blockade → "dying-back" axonopathy

**Neuroinflammation:**
- Microglial activation and astrocyte reactivity are prominent in ALS spinal cord
- Reactive astrocytes lose EAAT2 expression → amplify excitotoxicity
- M1 microglia release TNF-α, IL-1β, NO → neurotoxic
- Neuroinflammation propagates disease progression (not just secondary epiphenomenon — NF-κB suppression in microglia prolongs survival in SOD1 mice)

**Mitochondrial dysfunction:**
- Mitochondrial morphology is disrupted in ALS motor neurons
- SOD1 mutation → mitochondrial mislocalization in motor neurons → impaired ATP production at nodes of Ranvier → action potential failure
- TDP-43 regulates mitochondrial RNA → TDP-43 pathology disrupts mitochondrial function

## Pathology

### Diagnosis

ALS diagnosis is **clinical** — no single definitive biomarker test (though NfL is increasingly used):

**Revised El Escorial / Gold Coast criteria (2020):**
- Gold Coast criteria simplified: clinical signs of LMN degeneration + evidence of progressive spread (additional regions or EMG evidence in asymptomatic regions)
- EMG remains essential: shows active denervation (fibrillations, PSWs) in ≥3 regions (bulbar, cervical, thoracic, lumbar) to establish LMN disease broadly

**Biomarkers:**
- **Neurofilament light chain (NfL):** Elevated in CSF and blood; correlated with disease progression rate; reduces with tofersen treatment (SOD1-ALS) proportional to clinical benefit; increasingly used as trial endpoint and prognostic marker
- **pNfH (phosphorylated neurofilament heavy chain):** Similar to NfL; ALS-specific elevations
- **TDP-43 in CSF:** Elevated in ~50% of ALS patients but less sensitive than NfL
- **Genetic testing:** Strongly recommended for all ALS patients; C9orf72 repeat expansion PCR; NGS panel for SOD1, TARDBP, FUS, and other genes — affects prognosis and treatment (tofersen for SOD1-ALS)

### Treatment

**Approved disease-modifying therapies:**

| Drug | Mechanism | Approval | Benefit |
|:---|:---|:---|:---|
| **Riluzole** | Glutamate release inhibitor; persistent Na⁺ channel blocker → reduces motor neuron excitability | FDA 1995 | ~3-month median survival extension; modestly slows decline |
| **Edaravone** | Free radical scavenger (oxidative stress reduction) | FDA 2017 (selected patients); Japan/Canada/Korea earlier | ~33% slower functional decline in selected subgroup [^edaravone-als-2017] |
| **Tofersen (Qalsody)** | SOD1-targeting antisense oligonucleotide → reduces SOD1 protein | FDA 2023 (accelerated approval; SOD1-ALS only) | Reduces NfL; slows decline in faster-progressing SOD1-ALS; some functional benefit [^miller-2023-tofersen-als] |
| **AMX0035 (Relyvrio)** | Sodium phenylbutyrate + taurursodiol → reduces ER stress + mitochondrial apoptosis | FDA 2022 (accelerated; withdrawn 2024 after confirmatory trial failed) | Initial trial showed survival benefit; failed Phase 3 PHOENIX trial |

**Symptomatic/supportive management (essential):**
- **Non-invasive ventilation (NIV/BiPAP):** Standard of care for respiratory compromise; extends survival ~7 months in median and >12 months in some patients; comfort and quality of life
- **PEG tube:** Percutaneous gastrostomy when swallowing impaired (bulbar dysfunction); maintains nutrition and weight; recommended before FVC <50%
- **Communication augmentative/alternative technology (AAC):** Text-to-speech, eye-gaze devices — life-changing for quality of life
- **Multidisciplinary ALS clinic:** Consistent evidence that multidisciplinary care (neurology, respiratory therapy, PT, OT, speech, social work, palliative care) extends survival and improves quality of life
- **Riluzole + baclofen:** Baclofen reduces spasticity
- **Mexiletine:** For muscle cramps (sodium channel stabilizer)

**Emerging therapies:**
- **C9orf72-targeting ASOs:** BIIB078 (antisense targeting C9orf72 repeat-containing RNA) — Phase 1/2; AB-105 (RAN translation inhibitor)
- **STMN2-restoring ASO (UMass/Clene):** Corrects cryptic exon to restore stathmin-2; Phase 1/2 ongoing (TDP-43 ALS strategy — applicable to >97% of cases)
- **Stem cell approaches:** NurOwn (MSC-NTF) — failed Phase 3 2023; AstroRx (healthy astrocyte transplant) — Phase 1
- **Gene therapy:** AAV-SOD1 silencing; intrathecal delivery; ongoing trials

## Connections

- `connects-to` → **[TDP-43](../../../03-molecular/tdp-43/README.md)** — TDP-43 cytoplasmic inclusions are the pathological hallmark of >97% of ALS; TARDBP mutations cause ~4% of familial ALS; nuclear TDP-43 loss disrupts STMN2 and UNC13A splicing, causing axonal degeneration and synaptic failure.

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — glutamate excitotoxicity via impaired astrocytic EAAT2 uptake is a core ALS mechanism; riluzole inhibits glutamate release; ALS motor neurons express Ca²⁺-permeable AMPA receptors (low GluA2) increasing vulnerability; NMDA Ca²⁺ overload drives mitochondrial failure.

- `connects-to` → **[mTOR](../../../03-molecular/mtor/README.md)** — impaired autophagy contributes to TDP-43 and SOD1 aggregate accumulation; rapamycin reduces aggregate burden in ALS mouse models; p62/SQSTM1 and optineurin (autophagy receptors) are consistent components of ALS inclusions, indicating failed selective autophagy.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — ALS targets upper motor neurons (Betz cells, layer V primary motor cortex) and lower motor neurons (brainstem/spinal anterior horn); cortical hyperexcitability and reduced cortical inhibition precede clinical onset; cognitive/behavioral changes occur in ~50% (ALS-FTD spectrum).
- `connects-to` → **[Astrocyte](../../../04-cellular/astrocyte/README.md)** — ALS reactive astrocytes lose EAAT2 → amplify glutamate excitotoxicity; ALS astrocytes kill co-cultured motor neurons in vitro; astrocyte-specific SOD1 removal prolongs mouse survival; non-cell-autonomous neurodegeneration via astrocytes is a core ALS mechanism.
- `connects-to` → **[Microglia](../../../04-cellular/microglia/README.md)** — M1 microglia in ALS spinal cord release TNF-α, IL-1β, and NO → neurotoxic; NF-κB suppression in microglia prolongs SOD1 mouse survival; microglia transition from protective M2 to damaging M1 as ALS progresses; peripheral monocyte infiltration amplifies neuroinflammation.
- `connects-to` → **[Peripheral Nerve](../../../05-tissue/peripheral-nerve/README.md)** — ALS causes dying-back axonopathy of peripheral motor nerves; neurofilament accumulation blocks axonal transport; EMG shows denervation (fibrillations, PSWs, giant units) in ≥3 body regions; peripheral motor nerve loss produces fasciculations, atrophy, and areflexia (LMN signs).

- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — ALS is a motor neuron disease: it selectively kills the upper motor neurons of the cortex and the lower motor neurons of the brainstem and spinal cord, sparing most others; their extreme length and calcium-permeable AMPA receptors make these neurons uniquely vulnerable.

- `connects-to` → **[CIDP](../cidp/README.md)** — ALS and CIDP both cause progressive weakness but at different sites: ALS is irreversible degeneration of the motor neuron itself, whereas CIDP is immune demyelination of the peripheral nerve — treatable and often reversible — so distinguishing them is critical.

- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — ALS shares the TDP-43 proteinopathy that also marks frontotemporal dementia and a subset of Alzheimer's: ~50% of ALS patients show cognitive change, C9orf72 expansion causes both ALS and FTD, and cytoplasmic TDP-43 aggregates link these diseases mechanistically.
- `connects-to` → **[Neuromuscular Junction](../../05-tissue/neuromuscular-junction/README.md)** — ALS dismantles the neuromuscular junction early: as motor neurons degenerate, their axons die back and synapses retract from muscle endplates (denervation), causing fasciculations, weakness and wasting—this 'dying-back' NMJ loss may precede cell-body death.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — ALS devastates the musculoskeletal system through denervation: loss of upper and lower motor neurons produces progressive muscle weakness, wasting, spasticity and ultimately paralysis, while sparing sensation; the relentless decline in muscle function defines the disability.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Respiratory failure is the usual cause of death in ALS: degeneration of the motor neurons driving the diaphragm and accessory muscles progressively weakens ventilation, so non-invasive ventilation prolongs survival and forced vital capacity is a key prognostic and trial endpoint.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — ALS and myasthenia gravis cause weakness at opposite ends of the motor unit: ALS degenerates the motor neuron (upper and lower signs, fasciculations), while myasthenia blocks the neuromuscular junction (fatigable, treatable)—a prognosis-changing distinction.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — ALS and Parkinson's are neurodegenerations of protein misfolding hitting different neurons: ALS kills motor neurons (TDP-43), Parkinson's kills dopaminergic neurons (α-synuclein)—and ALS-parkinsonism-dementia overlaps hint at shared proteostasis failure.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Oligodendrocytes contribute to motor neuron death in ALS: beyond myelination they metabolically support axons, and dysfunctional ALS oligodendrocytes fail to supply lactate and degenerate—so glial, not just neuronal, failure drives the disease.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — ALS severs the acetylcholine signal to muscle: as motor neurons die, the terminals that release acetylcholine at the neuromuscular junction degenerate, so muscles lose stimulation and waste—unlike myasthenia gravis, where the receptor not the nerve is blocked.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Respiratory failure is how ALS kills: progressive weakness of the diaphragm and chest muscles cripples the lungs' bellows, causing hypoventilation, CO2 retention and eventual failure—so non-invasive ventilation is a mainstay that extends survival in ALS.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — ALS and multiple sclerosis both cause motor weakness but differ fundamentally: ALS is degenerative death of motor neurons, while MS is autoimmune demyelination with sensory and visual features—so ALS spares sensation and progresses without the relapses of MS.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper links the first ALS gene to oxidative stress: SOD1 is a copper-zinc superoxide dismutase, and many familial ALS mutations make the misfolded enzyme mishandle copper and generate toxic free radicals—so metal-dependent oxidative injury helps kill motor neurons.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — ALS is a relentless disease of the motor nervous system: it kills both upper motor neurons in the cortex and lower motor neurons in the brainstem and cord, so spasticity and wasting advance together until respiratory muscles fail.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Neuroinflammation drives ALS progression: activated microglia and astrocytes plus infiltrating immune cells turn from protective to toxic around dying motor neurons, so the immune system shapes how fast the disease advances—a target for emerging therapies.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — ALS is increasingly seen as a disease of failed protein clearance: motor neurons can't autophagy-degrade misfolded TDP-43 and SOD1, so toxic aggregates accumulate—linking many ALS genes (and the overlap with frontotemporal dementia) to a common disposal defect.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — ALS's SOD1 enzyme is a copper-zinc protein, and zinc is structural to it: mutations that disturb metal binding destabilize SOD1 into toxic aggregates, so the zinc (and copper) chemistry of this antioxidant enzyme sits at the heart of inherited ALS.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome is an emerging factor in ALS: altered gut flora and their metabolites may influence neuroinflammation and disease progression along the gut-brain axis, so the microbiome is being explored as a modifier of this relentless motor-neuron disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — ALS motor neurons die from calcium-driven excitotoxicity: excess glutamate floods them with calcium, and their unusually low calcium-buffering makes them especially vulnerable—the rationale for the glutamate-blunting drug riluzole.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells slow ALS: they restrain the harmful neuroinflammation of microglia, and patients with more functional Tregs progress slower—so expanding Tregs is an experimental therapy for this relentless motor neuron disease.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — ALS overlaps frontotemporal dementia in the hippocampus and cortex: TDP-43 pathology spreads beyond motor neurons to memory and behavior regions, so up to half of ALS patients develop cognitive change—uniting two diseases on one molecular spectrum.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Motor neurons in ALS run out of ATP: failing mitochondria cannot meet the huge energy demand of cells with metre-long axons, so the energy shortfall cripples transport and ion pumping and helps drive the neurons' death.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells infiltrate the dying motor regions in ALS: adaptive immunity adds to microglial inflammation, and the balance between these CD8 cells and protective regulatory T cells helps set how fast the disease advances.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — ALS motor neurons fire too easily through persistent sodium currents: this hyperexcitability stresses the cells and contributes to their loss, and it is partly why riluzole—which curbs sodium currents and glutamate—modestly slows the disease.

[^brown-2017-als-review]: Brown RH, Al-Chalabi A. Amyotrophic lateral sclerosis. *N Engl J Med.* 2017;377(2):162-172. [doi:10.1056/NEJMra1603471](https://doi.org/10.1056/NEJMra1603471) · [PubMed 28700839](https://pubmed.ncbi.nlm.nih.gov/28700839/)
[^edaravone-als-2017]: Writing Group, Edaravone ALS 19 Study Group. Safety and efficacy of edaravone in well defined patients with amyotrophic lateral sclerosis. *Lancet Neurol.* 2017;16(7):505-512. [doi:10.1016/S1474-4422(17)30115-1](https://doi.org/10.1016/S1474-4422(17)30115-1) · [PubMed 28522180](https://pubmed.ncbi.nlm.nih.gov/28522180/)
[^miller-2023-tofersen-als]: Miller TM, Cudkowicz ME, Genge A, et al. Trial of Antisense Oligonucleotide Tofersen for SOD1 ALS. *N Engl J Med.* 2022;387(12):1099-1110. [doi:10.1056/NEJMoa2204705](https://doi.org/10.1056/NEJMoa2204705) · [PubMed 36129998](https://pubmed.ncbi.nlm.nih.gov/36129998/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
