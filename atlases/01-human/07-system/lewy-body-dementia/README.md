---
schema: human-scale-entry/v1
id: lewy-body-dementia
name: Lewy Body Dementia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "DLB (dementia with Lewy bodies) is the 2nd most common neurodegenerative dementia; core features: fluctuating cognition, visual hallucinations, RBD, parkinsonism; cortical alpha-synuclein Lewy body pathology; fatal neuroleptic sensitivity; rivastigmine for cognition."
aliases: ["DLB", "dementia with Lewy bodies", "Lewy body disease", "LBD", "diffuse Lewy body disease", "Lewy body dementia", "PDD", "Parkinson's disease dementia", "synucleinopathy dementia"]
sources:
  - id: mckeith-2017-dlb-criteria
    type: peer-reviewed
    cite: "McKeith IG, Boeve BF, Dickson DW, et al. Diagnosis and management of dementia with Lewy bodies: Fourth consensus report of the DLB Consortium. Neurology. 2017;89(1):88-100."
    doi: "10.1212/WNL.0000000000004058"
    pmid: "28592453"
    url: "https://doi.org/10.1212/WNL.0000000000004058"
    accessed: "2026-06-08"
  - id: spillantini-1997-lewy-body
    type: peer-reviewed
    cite: "Spillantini MG, Schmidt ML, Lee VM, Trojanowski JQ, Jakes R, Goedert M. Alpha-synuclein in Lewy bodies. Nature. 1997;388(6645):839-840."
    doi: "10.1038/42166"
    pmid: "9278044"
    url: "https://doi.org/10.1038/42166"
    accessed: "2026-06-08"
  - id: walker-2015-dlb-review
    type: peer-reviewed
    cite: "Walker Z, Possin KL, Boeve BF, Aarsland D. Lewy body dementias. Lancet. 2015;386(10004):1683-1697."
    doi: "10.1016/S0140-6736(15)00462-6"
    pmid: "26595642"
    url: "https://doi.org/10.1016/S0140-6736(15)00462-6"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "DLB and PD are both alpha-synuclein synucleinopathies; 1-year rule: dementia ≤1 year of parkinsonism → DLB; parkinsonism >1 year before dementia → PDD; SNCA pathology distribution differs — DLB has early cortical Lewy bodies while PD follows Braak brainstem→cortex staging."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "50-70% of DLB cases have concurrent Alzheimer co-pathology (Aβ plaques, tau tangles); AD and DLB share APOE4 as a risk factor; DLB with high AD co-pathology has faster cognitive decline; anti-amyloid antibodies (lecanemab) may have a role in DLB with concurrent Aβ pathology."
  - target: 01-human/03-molecular/snca
    relation: connects-to
    note: "Alpha-synuclein (SNCA) Lewy body pathology in limbic cortex and neocortex is the defining neuropathology of DLB; SNCA seed amplification assay (SAA/RT-QuIC) in CSF or skin is >90% sensitive for DLB; SNCA S129 phosphorylation marks Lewy body alpha-synuclein in DLB and PD equally."
  - target: 01-human/03-molecular/mapt
    relation: connects-to
    note: "Tau co-pathology is present in 50-70% of DLB brains; MAPT H1 haplotype is a risk factor for DLB; tau and alpha-synuclein co-aggregate via cross-seeding; DLB cases with high tau burden have faster progression and worse cognitive outcomes than pure alpha-synuclein pathology."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "DLB Lewy bodies accumulate in limbic cortex, cingulate, and occipital cortex → visual hallucinations (occipital hypometabolism); brainstem (substantia nigra) involvement causes parkinsonism; diffuse cortical cholinergic denervation (80% ChAT loss) drives cognitive fluctuations."
  - target: 01-human/03-molecular/tdp-43
    relation: connects-to
    note: "TDP-43 co-pathology in ~50% of DLB brains drives hippocampal atrophy and memory impairment independent of Lewy body burden; TDP-43 inclusions in hippocampal CA1 and entorhinal cortex accelerate cognitive decline; co-pathology predicts faster dementia progression in DLB patients."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Lewy body dementia carries the most severe cholinergic deficit — ~80% loss of cortical choline acetyltransferase, worse than Alzheimer's — driving fluctuating attention and visual hallucinations, and explaining why cholinesterase inhibitors help DLB more than AD."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Treating the parkinsonism of Lewy body dementia with dopamine agonists can unleash impulse-control disorders (gambling, hypersexuality, compulsive shopping) by over-stimulating mesolimbic reward circuits; recognizing and dose-reducing is essential."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Lewy bodies are intraneuronal inclusions of misfolded alpha-synuclein; in DLB they fill cortical and limbic neurons, and selective loss of cholinergic, dopaminergic, and noradrenergic neurons produces the dementia, parkinsonism, and dysautonomia."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep disorder is a core, often first feature of Lewy body dementia: REM sleep behavior disorder—acting out dreams from loss of REM atonia—can precede dementia by years and strongly predicts a synucleinopathy; LBD also brings fragmented sleep and daytime somnolence."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression is common and often early in Lewy body dementia: degeneration of monoaminergic brainstem nuclei (serotonin, noradrenaline) plus cognitive and motor decline drive mood symptoms that can predate the dementia, complicating the distinction from late-life depression."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Neuroinflammation accompanies Lewy body dementia: microglia activated by misfolded α-synuclein release pro-inflammatory cytokines and reactive species that amplify neuronal injury and may spread pathology; PET shows microglial activation tracking disease, a therapeutic target."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "REM sleep behavior disorder bridges Lewy body dementia and narcolepsy: RBD—acting out dreams from lost REM muscle atonia—is an early marker that often precedes Lewy body dementia by years, while narcolepsy disrupts the same REM gating from orexin loss."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes participate in Lewy body dementia's α-synuclein pathology: reactive astrocytes accumulate α-synuclein and, with microglia, drive the neuroinflammation that accompanies the spreading synucleinopathy, so glial dysfunction contributes alongside neuronal loss."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine loss links Lewy body dementia to its parkinsonism: α-synuclein degeneration of nigrostriatal dopamine neurons produces the rigidity and bradykinesia, and a DaT scan showing reduced striatal dopamine transporter helps distinguish LBD from Alzheimer's disease."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "Lewy body dementia and Huntington's are neurodegenerative movement-and-cognition disorders with distinct causes: LBD from α-synuclein (parkinsonism, hallucinations), Huntington's from a CAG repeat (chorea)—different proteins, overlapping decline."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Lewy body dementia is defined partly by psychosis that mimics schizophrenia: visual hallucinations and delusions are core features, but unlike schizophrenia they arise in older adults with parkinsonism, and antipsychotics can cause life-threatening sensitivity in LBD."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Lewy body dementia spares the hippocampus more than Alzheimer's early on: memory is relatively preserved while attention, visuospatial function and alertness fluctuate, reflecting cortical and brainstem Lewy pathology not hippocampal degeneration."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Lewy body dementia is a multisystem nervous-system synucleinopathy: alpha-synuclein deposits spread beyond cortex to autonomic and brainstem neurons, so beyond cognition it causes dysautonomia, REM sleep behavior disorder and parkinsonism—a whole-nervous-system disease."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Norepinephrine loss drives Lewy body dementia's autonomic and cognitive features: degeneration of the noradrenergic locus coeruleus contributes to orthostatic hypotension, attention fluctuations and arousal problems that distinguish LBD from Alzheimer's."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "REM sleep behavior disorder is a hallmark of Lewy body dementia: loss of normal REM atonia lets patients act out dreams, often years before dementia, and melatonin is a first-line treatment—making this sleep disturbance an early diagnostic clue."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Lewy body dementia is a failure of protein clearance: when autophagy can't degrade misfolded alpha-synuclein, it aggregates into the Lewy bodies that poison neurons, so boosting this cellular recycling system is a target shared with Parkinson's disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Lewy body dementia often starts in the gut: constipation and alpha-synuclein deposits in enteric nerves can precede cognitive and motor signs by years, echoing Parkinson's 'gut-first' route along the vagus nerve into the brain."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart helps diagnose Lewy body dementia: alpha-synuclein damages cardiac sympathetic nerves, so a MIBG scan shows reduced cardiac uptake—a marker that distinguishes Lewy body disease from Alzheimer's and other dementias."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Vivid visual hallucinations set Lewy body dementia apart: degeneration in visual-processing pathways makes well-formed hallucinations (often of people or animals) a core early feature, helping distinguish it from Alzheimer's at the bedside."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Lewy body dementia is treated partly by tuning glutamate: the NMDA-blocker memantine dampens excitotoxic glutamate signaling to modestly help cognition, complementing the cholinesterase inhibitors that target the disease's severe acetylcholine loss."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Brain iron accumulation feeds Lewy body disease: iron builds up in vulnerable neurons and catalyzes oxidative stress that promotes alpha-synuclein aggregation, linking a metal imbalance to the protein clumping at the disease's core."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Lewy body disease may begin in the gut: alpha-synuclein clumps appear in the intestinal nerves years before dementia, and constipation is a common early warning, supporting the idea that the pathology can climb the vagus nerve from gut to brain."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Lewy body dementia injures the brain's white matter: alpha-synuclein and degeneration affect oligodendrocytes and myelinated tracts, so disrupted connectivity between regions adds to the cholinergic loss behind the fluctuating cognition."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper binds alpha-synuclein directly: the protein has a copper-grabbing site, and disordered copper handling shifts synuclein toward the misfolded, aggregation-prone form, so a second metal beyond iron is tied to the Lewy body's core protein."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Lewy body dementia is a disease of failing synapses: alpha-synuclein normally works at the presynaptic terminal, and its misfolding cripples neurotransmitter release before cells die, so synaptic breakdown underlies the fluctuating cognition."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Lewy body dementia can be found in the skin: misfolded alpha-synuclein deposits in the tiny nerves of the skin, so a simple skin biopsy can now help confirm the synuclein disease behind the dementia."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Lewy body dementia starves neurons of ATP: like Parkinson's, it carries mitochondrial dysfunction that limits cellular energy, and the brain's demanding neurons falter as their power supply fails."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging helps pin down Lewy body dementia: a DaTscan's photons show the dopamine loss, and cardiac MIBG scintigraphy reveals the sympathetic denervation that helps separate it from Alzheimer's."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Lewy body dementia attacks the autonomic nerves: synuclein in the peripheral autonomic system causes orthostatic hypotension, constipation and bladder trouble, often years before the dementia appears."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Aspiration pneumonia is the common end of Lewy body dementia: as swallowing fails late in the disease, inhaled food infects the lungs, the frequent immediate cause of death."
---

# Lewy Body Dementia

## Overview

**Lewy body dementia (LBD)** encompasses two closely related synucleinopathy syndromes — **dementia with Lewy bodies (DLB)** and **Parkinson's disease dementia (PDD)** — that share the same neuropathological substrate (alpha-synuclein Lewy bodies in cortex and brainstem) but differ in the temporal relationship between dementia and parkinsonism onset. Together, the Lewy body dementias are the **second most common neurodegenerative dementia** after Alzheimer's disease, accounting for 15–20% of all dementia cases and affecting approximately **1.4 million Americans** [^walker-2015-dlb-review].

**The 1-year rule (DLB vs PDD distinction):**
- **DLB**: Dementia onset precedes parkinsonism, or dementia and parkinsonism appear within 1 year of each other
- **PDD**: Parkinson's disease diagnosed >1 year before dementia onset

This arbitrary temporal distinction reflects the same underlying pathological spectrum, and both syndromes are now grouped clinically as "Lewy body dementia" in practice, though they retain distinct diagnostic criteria (McKeith DLB Consortium criteria for DLB; MDS criteria for PDD). The shared pathomechanism — alpha-synuclein aggregation and Lewy body formation — makes DLB and PDD distinct from Alzheimer's disease (amyloid-β/tau), despite significant clinical overlap and frequent co-pathology.

Lewy body dementia is severely underdiagnosed — the mean time from symptom onset to diagnosis exceeds 1.5 years, and misdiagnosis (most often as Alzheimer's disease) leads to **potentially fatal treatment errors**, particularly iatrogenic neuroleptic sensitivity reactions.

## Structure

### Neuropathological substrate

The defining pathology of DLB is the accumulation of **alpha-synuclein Lewy bodies** in the cerebral cortex and brainstem [^spillantini-1997-lewy-body]. Unlike Parkinson's disease (where Braak staging predicts early brainstem → late cortical spread), DLB typically shows early and prominent **cortical and limbic** Lewy body pathology:

**LB distribution in DLB (McKeith pathological staging):**

| Stage | Lewy body distribution | Clinical correlation |
|:---|:---|:---|
| **Brainstem predominant** | Dorsal motor nucleus of vagus, locus coeruleus, substantia nigra | Autonomic dysfunction, parkinsonism (often absent at DLB onset) |
| **Limbic (transitional)** | Amygdala, hippocampus, entorhinal cortex, cingulate gyrus | Memory impairment, visual hallucinations |
| **Neocortical** | Temporal, parietal, frontal association cortex | Global cognitive impairment, psychiatric features, severe dementia |

Most DLB patients have **neocortical Lewy body burden at diagnosis** — explaining why cognitive impairment rather than parkinsonism is the presenting feature.

**Co-pathology:** 50–70% of DLB cases have concurrent Alzheimer co-pathology (amyloid-β plaques, tau neurofibrillary tangles), which accelerates cognitive decline and reduces response to cholinesterase inhibitors. DLB with high amyloid co-pathology may benefit from anti-amyloid antibody therapy (clinical trials ongoing).

### Neurotransmitter deficits

| Neurotransmitter | Deficit | Clinical consequence |
|:---|:---|:---|
| **Acetylcholine** | Most severe of all dementia types (80% cortical ChAT activity loss) | Cognitive fluctuations, hallucinations, memory impairment; responds to rivastigmine |
| **Dopamine** | SNpc degeneration → striatal dopamine loss | Parkinsonism (bradykinesia, rigidity, postural instability; tremor less common than PD) |
| **Norepinephrine** | Locus coeruleus degeneration | Orthostatic hypotension, REM sleep behavior disorder |
| **Serotonin** | Raphe nuclei involvement | Depression, sleep disturbance |

The profound **cholinergic deficit** in DLB — more severe than in Alzheimer's disease — explains both the cognitive fluctuations and visual hallucinations, and underlies the marked response to cholinesterase inhibitors (rivastigmine shows significant benefit in DLB, unlike the more modest effects in AD).

## Function

### Core diagnostic features (McKeith 2017 criteria) [^mckeith-2017-dlb-criteria]

**Four core clinical features (2+ required for probable DLB; 1 for possible DLB):**

1. **Fluctuating cognition**: Day-to-day or hour-to-hour oscillations in alertness and attention — "clouding" episodes lasting minutes to hours; lucid intervals followed by periods of confusion; ~80% of DLB patients; assessed by Clinician Assessment of Fluctuation (CAF) scale or Mayo Clinic Fluctuations Scale

2. **Recurrent well-formed visual hallucinations**: Typically detailed, complex, often of people or animals; present in ~70-80% of DLB patients; often non-threatening (patient may recognize them as "not real"); distinguish from Alzheimer's psychosis (which tends to be fragmented and paranoid)

3. **REM sleep behavior disorder (RBD)**: Loss of normal REM muscle atonia → patients physically act out dreams (shouting, punching, kicking); may predate dementia by years; >80% specificity for synucleinopathy; confirmed by polysomnography (PSG) with video monitoring

4. **Parkinsonism**: Bradykinesia, rigidity, and/or rest tremor; mild in most DLB (less prominent than idiopathic PD); responds partially to levodopa

**Supportive biomarkers:**
- **DAT-SPECT (DaTscan)**: Reduced dopamine transporter uptake in striatum (positive in ~80% DLB vs. ~10% AD); FDA-approved for distinguishing DLB from non-DLB dementias
- **MIBG cardiac scintigraphy**: Reduced cardiac sympathetic innervation (abnormal in ~70% DLB, ~10% AD); heart-to-mediastinum ratio <1.60 is highly specific
- **FDG-PET**: Occipital hypometabolism (visual cortex) — characteristic of DLB; distinguishes from AD (posterior parietal/temporal hypometabolism); "cingulate island sign" (preserved posterior cingulate vs. occipital loss)
- **Alpha-synuclein SAA (RT-QuIC)**: In CSF or skin biopsy; >90% sensitivity and specificity for DLB/PD; emerging as central diagnostic test
- **EEG**: Prominent slow waves, temporal sharp waves; may oscillate with fluctuating consciousness

### Clinical presentation — distinguishing DLB from Alzheimer's disease

| Feature | DLB | Alzheimer's Disease |
|:---|:---|:---|
| Memory at onset | Relatively preserved early | Prominent episodic memory loss (hippocampal) |
| Visuospatial | Severely impaired early | Impaired but less severe than DLB |
| Fluctuations | Prominent | Uncommon |
| Visual hallucinations | Spontaneous, complex, frequent | Less common; psychotic if present |
| Parkinsonism | Present in majority | Absent (late gait changes only) |
| Neuroleptic sensitivity | Fatal in ~50% | Not a major concern |
| RBD | Common | Uncommon |
| DAT-SPECT | Abnormal | Normal |
| FDG-PET | Occipital hypometabolism | Posterior parietal/temporal hypometabolism |

### Neuroleptic sensitivity — critical clinical warning

**DLB patients who receive typical or atypical antipsychotics** (especially haloperidol, risperidone, olanzapine) may develop **severe and potentially fatal neuroleptic sensitivity reactions** in ~50% of cases:
- Severe extrapyramidal rigidity, immobility
- Impaired consciousness, neuroleptic malignant syndrome-like picture
- Aspiration pneumonia, rapid functional decline
- Case fatality rate ~25-50% in affected patients

**Safe alternatives** for managing DLB psychosis:
- **Quetiapine** (relatively safe; weak D2 blockade)
- **Clozapine** (most effective; requires weekly CBC monitoring for agranulocytosis)
- **Pimavanserin** (5-HT2A inverse agonist; no dopamine blockade; FDA-approved for PD psychosis; trials in DLB ongoing)

## Pathology

### Neuropathological diagnosis

DLB diagnosis requires post-mortem demonstration of **neocortical alpha-synuclein Lewy bodies** by immunohistochemistry (anti-pSer129 SNCA antibody) in cingulate, parahippocampal, and frontal/temporal neocortex, combined with clinical features. The McKeith 2017 framework classifies neuropathological changes as:
- **High likelihood DLB**: Neocortical Lewy body pathology (with or without Alzheimer co-pathology)
- **Intermediate likelihood DLB**: Limbic Lewy body pathology
- **Low likelihood DLB**: Brainstem-predominant Lewy body pathology

Approximately 25-50% of clinically diagnosed DLB cases have significant AD co-pathology meeting neuropathological AD criteria — the "LBD-AD overlap" subtype.

### Treatment

**Cognitive symptoms:**
- **Rivastigmine (Exelon)** — the only FDA-approved treatment for PDD; also used off-label for DLB; inhibits both AChE and BChE; randomized trial (EXPRESS): 2.1-point MMSE improvement vs. placebo; cholinergic benefit reflects the profound ChAT deficit in DLB; side effects (nausea, vomiting) common with oral formulation → transdermal patch preferred
- **Donepezil** — evidence in DLB (open-label data); less RCT evidence than for AD or PDD
- **Memantine** — NMDA antagonist; modest benefit in open-label DLB studies; can worsen confusion in some patients

**Motor symptoms:**
- **Levodopa/carbidopa** — trial warranted for parkinsonism in DLB; response is less robust than in idiopathic PD (~50% respond); risk of worsening hallucinations and psychosis limits dose escalation; start low
- **Deep brain stimulation**: Limited evidence in DLB; generally avoided due to cognitive risk

**REM sleep behavior disorder:**
- **Clonazepam** (0.25–0.5 mg at bedtime): Reduces injurious dream enactment; first-line despite lack of large RCTs; not disease-modifying
- **Melatonin** (3–12 mg at bedtime): Safer than clonazepam; restores REM atonia; preferred in elderly

**Autonomic dysfunction:**
- Midodrine, droxidopa, fludrocortisone for neurogenic orthostatic hypotension
- Pyridostigmine for orthostatic hypotension (augments peripheral sympathetic tone)

**Disease-modifying therapies (investigational):**
- **Alpha-synuclein immunotherapy**: Prasinezumab (anti-SNCA mAb; Phase 2b in PD, signals in fast progressors); cinpanemab — negative Phase 2; ABBV-0805 (anti-aggregated synuclein) — Phase 2 ongoing
- **Alpha-synuclein SAA screening**: Pre-symptomatic identification of synucleinopathy enables future neuroprotective trials
- **GLP-1 agonists**: Semaglutide/liraglutide associated with lower PD risk in T2DM populations; neuroprotective mechanism investigation ongoing; Phase 2 trials in DLB planned

## Connections

- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — DLB and PD are both alpha-synuclein Lewy body diseases distinguished by the 1-year rule; SNCA pathology distribution differs — DLB has early cortical Lewy bodies while PD follows Braak staging from brainstem to cortex; motor symptoms are less prominent in DLB than idiopathic PD.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — 50-70% of DLB cases have concurrent Aβ plaques and tau tangles (AD co-pathology); both share APOE4 as a risk factor; distinguishing DLB from AD is critical due to fatal neuroleptic sensitivity; anti-amyloid antibodies may have emerging role in DLB with high amyloid burden.
- `connects-to` → **[SNCA](../../03-molecular/snca/README.md)** — cortical and limbic alpha-synuclein Lewy body pathology (SNCA S129-phosphorylated fibrils) defines DLB; alpha-synuclein SAA (RT-QuIC) in CSF or skin is >90% sensitive for DLB and emerging as the key antemortem biomarker; SNCA G51D mutation causes early-onset DLB-like syndrome.
- `connects-to` → **[MAPT](../../03-molecular/mapt/README.md)** — tau co-pathology present in 50-70% of DLB brains; MAPT H1 haplotype is a risk factor; alpha-synuclein and tau cross-seed each other; high tau burden in DLB predicts faster cognitive decline and worse prognosis.
- `targets` → **[Brain](../../06-organ/brain/README.md)** — DLB Lewy bodies accumulate in limbic cortex, parahippocampal gyrus, cingulate, and occipital cortex → visual hallucinations and cognitive fluctuations; SNpc degeneration causes parkinsonism; diffuse cholinergic denervation (80% ChAT activity loss) underlies cognitive impairment responsive to rivastigmine.
- `connects-to` → **[TDP-43](../../03-molecular/tdp-43/README.md)** — TDP-43 co-pathology in ~50% of DLB brains drives hippocampal atrophy and memory impairment independent of Lewy body burden; TDP-43 inclusions in hippocampal CA1 and entorhinal cortex accelerate cognitive decline; co-pathology predicts faster dementia progression in DLB.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Lewy body dementia carries the most severe cholinergic deficit — ~80% loss of cortical choline acetyltransferase, worse than Alzheimer's — driving fluctuating attention and visual hallucinations, and explaining why cholinesterase inhibitors help DLB more than AD.
- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — Treating the parkinsonism of Lewy body dementia with dopamine agonists can unleash impulse-control disorders (gambling, hypersexuality, compulsive shopping) by over-stimulating mesolimbic reward circuits; recognizing and dose-reducing is essential.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Lewy bodies are intraneuronal inclusions of misfolded alpha-synuclein; in DLB they fill cortical and limbic neurons, and selective loss of cholinergic, dopaminergic, and noradrenergic neurons produces the dementia, parkinsonism, and dysautonomia.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep disorder is a core, often first feature of Lewy body dementia: REM sleep behavior disorder—acting out dreams from loss of REM atonia—can precede dementia by years and strongly predicts a synucleinopathy; LBD also brings fragmented sleep and daytime somnolence.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression is common and often early in Lewy body dementia: degeneration of monoaminergic brainstem nuclei (serotonin, noradrenaline) plus cognitive and motor decline drive mood symptoms that can predate the dementia, complicating the distinction from late-life depression.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Neuroinflammation accompanies Lewy body dementia: microglia activated by misfolded α-synuclein release pro-inflammatory cytokines and reactive species that amplify neuronal injury and may spread pathology; PET shows microglial activation tracking disease, a therapeutic target.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — REM sleep behavior disorder bridges Lewy body dementia and narcolepsy: RBD—acting out dreams from lost REM muscle atonia—is an early marker that often precedes Lewy body dementia by years, while narcolepsy disrupts the same REM gating from orexin loss.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes participate in Lewy body dementia's α-synuclein pathology: reactive astrocytes accumulate α-synuclein and, with microglia, drive the neuroinflammation that accompanies the spreading synucleinopathy, so glial dysfunction contributes alongside neuronal loss.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine loss links Lewy body dementia to its parkinsonism: α-synuclein degeneration of nigrostriatal dopamine neurons produces the rigidity and bradykinesia, and a DaT scan showing reduced striatal dopamine transporter helps distinguish LBD from Alzheimer's disease.
- `connects-to` → **[Huntington Disease](../huntingtons-disease/README.md)** — Lewy body dementia and Huntington's are neurodegenerative movement-and-cognition disorders with distinct causes: LBD from α-synuclein (parkinsonism, hallucinations), Huntington's from a CAG repeat (chorea)—different proteins, overlapping decline.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Lewy body dementia is defined partly by psychosis that mimics schizophrenia: visual hallucinations and delusions are core features, but unlike schizophrenia they arise in older adults with parkinsonism, and antipsychotics can cause life-threatening sensitivity in LBD.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Lewy body dementia spares the hippocampus more than Alzheimer's early on: memory is relatively preserved while attention, visuospatial function and alertness fluctuate, reflecting cortical and brainstem Lewy pathology not hippocampal degeneration.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Lewy body dementia is a multisystem nervous-system synucleinopathy: alpha-synuclein deposits spread beyond cortex to autonomic and brainstem neurons, so beyond cognition it causes dysautonomia, REM sleep behavior disorder and parkinsonism—a whole-nervous-system disease.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Norepinephrine loss drives Lewy body dementia's autonomic and cognitive features: degeneration of the noradrenergic locus coeruleus contributes to orthostatic hypotension, attention fluctuations and arousal problems that distinguish LBD from Alzheimer's.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — REM sleep behavior disorder is a hallmark of Lewy body dementia: loss of normal REM atonia lets patients act out dreams, often years before dementia, and melatonin is a first-line treatment—making this sleep disturbance an early diagnostic clue.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Lewy body dementia is a failure of protein clearance: when autophagy can't degrade misfolded alpha-synuclein, it aggregates into the Lewy bodies that poison neurons, so boosting this cellular recycling system is a target shared with Parkinson's disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Lewy body dementia often starts in the gut: constipation and alpha-synuclein deposits in enteric nerves can precede cognitive and motor signs by years, echoing Parkinson's 'gut-first' route along the vagus nerve into the brain.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart helps diagnose Lewy body dementia: alpha-synuclein damages cardiac sympathetic nerves, so a MIBG scan shows reduced cardiac uptake—a marker that distinguishes Lewy body disease from Alzheimer's and other dementias.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Vivid visual hallucinations set Lewy body dementia apart: degeneration in visual-processing pathways makes well-formed hallucinations (often of people or animals) a core early feature, helping distinguish it from Alzheimer's at the bedside.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Lewy body dementia is treated partly by tuning glutamate: the NMDA-blocker memantine dampens excitotoxic glutamate signaling to modestly help cognition, complementing the cholinesterase inhibitors that target the disease's severe acetylcholine loss.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Brain iron accumulation feeds Lewy body disease: iron builds up in vulnerable neurons and catalyzes oxidative stress that promotes alpha-synuclein aggregation, linking a metal imbalance to the protein clumping at the disease's core.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Lewy body disease may begin in the gut: alpha-synuclein clumps appear in the intestinal nerves years before dementia, and constipation is a common early warning, supporting the idea that the pathology can climb the vagus nerve from gut to brain.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Lewy body dementia injures the brain's white matter: alpha-synuclein and degeneration affect oligodendrocytes and myelinated tracts, so disrupted connectivity between regions adds to the cholinergic loss behind the fluctuating cognition.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper binds alpha-synuclein directly: the protein has a copper-grabbing site, and disordered copper handling shifts synuclein toward the misfolded, aggregation-prone form, so a second metal beyond iron is tied to the Lewy body's core protein.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Lewy body dementia is a disease of failing synapses: alpha-synuclein normally works at the presynaptic terminal, and its misfolding cripples neurotransmitter release before cells die, so synaptic breakdown underlies the fluctuating cognition.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Lewy body dementia can be found in the skin: misfolded alpha-synuclein deposits in the tiny nerves of the skin, so a simple skin biopsy can now help confirm the synuclein disease behind the dementia.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Lewy body dementia starves neurons of ATP: like Parkinson's, it carries mitochondrial dysfunction that limits cellular energy, and the brain's demanding neurons falter as their power supply fails.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging helps pin down Lewy body dementia: a DaTscan's photons show the dopamine loss, and cardiac MIBG scintigraphy reveals the sympathetic denervation that helps separate it from Alzheimer's.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Lewy body dementia attacks the autonomic nerves: synuclein in the peripheral autonomic system causes orthostatic hypotension, constipation and bladder trouble, often years before the dementia appears.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Aspiration pneumonia is the common end of Lewy body dementia: as swallowing fails late in the disease, inhaled food infects the lungs, the frequent immediate cause of death.

[^mckeith-2017-dlb-criteria]: McKeith IG, Boeve BF, Dickson DW, et al. Diagnosis and management of dementia with Lewy bodies: Fourth consensus report of the DLB Consortium. *Neurology.* 2017;89(1):88-100. [doi:10.1212/WNL.0000000000004058](https://doi.org/10.1212/WNL.0000000000004058) · [PubMed 28592453](https://pubmed.ncbi.nlm.nih.gov/28592453/)
[^spillantini-1997-lewy-body]: Spillantini MG, Schmidt ML, Lee VM, Trojanowski JQ, Jakes R, Goedert M. Alpha-synuclein in Lewy bodies. *Nature.* 1997;388(6645):839-840. [doi:10.1038/42166](https://doi.org/10.1038/42166) · [PubMed 9278044](https://pubmed.ncbi.nlm.nih.gov/9278044/)
[^walker-2015-dlb-review]: Walker Z, Possin KL, Boeve BF, Aarsland D. Lewy body dementias. *Lancet.* 2015;386(10004):1683-1697. [doi:10.1016/S0140-6736(15)00462-6](https://doi.org/10.1016/S0140-6736(15)00462-6) · [PubMed 26595642](https://pubmed.ncbi.nlm.nih.gov/26595642/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
