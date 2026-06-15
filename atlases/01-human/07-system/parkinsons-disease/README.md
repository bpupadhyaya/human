---
schema: human-scale-entry/v1
id: parkinsons-disease
name: Parkinson's Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Neurodegenerative disease from dopaminergic neuron loss in the substantia nigra; alpha-synuclein Lewy bodies are the pathological hallmark. Cardinal features: bradykinesia, rigidity, resting tremor. Levodopa/carbidopa is mainstay therapy; no disease-modifying therapy approved."
aliases: ["PD", "Parkinson disease", "paralysis agitans", "idiopathic Parkinson's"]
sources:
  - id: kalia-2015-pd-review
    type: peer-reviewed
    cite: "Kalia LV, Lang AE. Parkinson's disease. Lancet. 2015;386(9996):896-912."
    doi: "10.1016/S0140-6736(14)61393-3"
    pmid: "25904081"
    url: "https://doi.org/10.1016/S0140-6736(14)61393-3"
  - id: spillantini-1997-lewy-body
    type: peer-reviewed
    cite: "Spillantini MG, Schmidt ML, Lee VM, Trojanowski JQ, Jakes R, Goedert M. Alpha-synuclein in Lewy bodies. Nature. 1997;388(6645):839-840."
    doi: "10.1038/42166"
    pmid: "9278044"
    url: "https://doi.org/10.1038/42166"
  - id: olanow-2009-pd-treatment
    type: peer-reviewed
    cite: "Olanow CW, Stern MB, Sethi K. The scientific and clinical basis for the treatment of Parkinson disease. Neurology. 2009;72(21 Suppl 4):S1-136."
    doi: "10.1212/WNL.0b013e3181a1d44c"
    pmid: "19470958"
    url: "https://doi.org/10.1212/WNL.0b013e3181a1d44c"
cross_links:
  - target: 01-human/06-organ/brain
    relation: targets
    note: "PD destroys dopaminergic neurons in the substantia nigra pars compacta → depletes striatal dopamine → disrupts basal ganglia circuitry; Lewy bodies spread via Braak staging from brainstem to limbic and neocortex."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Alpha-synuclein aggregates activate microglia via TLR2/4 and NLRP3 inflammasome → IL-1β and TNF-alpha → dopaminergic neuron death; neuroinflammation amplifies degeneration and correlates with disease progression."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Alpha-synuclein is degraded by autophagy (macroautophagy and CMA); mutant SNCA and LRRK2 impair autophagy flux → aggregate accumulation; TFEB activation and rapamycin reduce synuclein pathology in preclinical models."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Both are age-related neurodegenerative diseases with prion-like protein aggregation (tau/Abeta in AD; alpha-synuclein in PD); Lewy body dementia overlaps both; shared pathomechanisms include mitochondrial dysfunction, autophagy failure, and neuroinflammation."
  - target: 01-human/03-molecular/snca
    relation: connects-to
    note: "SNCA missense mutations (A53T, A30P, E46K) and gene duplication/triplication cause familial PD; misfolded alpha-synuclein fibrils are the main component of Lewy bodies; SNCA propagates via synaptic connections following Braak staging from brainstem to neocortex."
  - target: 01-human/03-molecular/lrrk2
    relation: connects-to
    note: "LRRK2 G2019S (~1-2% of sporadic PD, ~40% penetrance by age 80) is the most common pathogenic variant causing familial PD; LRRK2 kinase hyperactivation → Rab GTPase hyperphosphorylation → vesicle trafficking defects and α-synuclein aggregation in dopaminergic neurons."
  - target: 01-human/03-molecular/mapt
    relation: connects-to
    note: "MAPT H1 haplotype (common in Europeans) is a risk factor for PD and PSP; tau co-aggregates with alpha-synuclein in Lewy body dementia and some PD brains; MAPT LOF mutations cause FTLD-MAPT; tau and SNCA pathology converge on mitochondrial dysfunction and autophagy impairment."
  - target: 01-human/07-system/lewy-body-dementia
    relation: connects-to
    note: "DLB and PD are both alpha-synuclein synucleinopathies: the 1-year rule distinguishes DLB (dementia onset ≤1 year of parkinsonism) from PDD (parkinsonism >1 year before dementia); DLB features early cortical Lewy bodies while PD follows Braak brainstem→cortex staging."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Parkinson's is defined by dopamine loss: degeneration of substantia nigra pars compacta neurons depletes striatal dopamine → bradykinesia, rigidity and tremor once ~60-80% is gone; levodopa, dopamine agonists and MAO-B/COMT inhibitors restore dopaminergic tone."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Parkinson's is a neurodegeneration of specific neurons: α-synuclein-laden Lewy bodies accumulate in dopaminergic substantia nigra neurons, driving mitochondrial and autophagy failure and selective death; the vulnerability of these pacemaking neurons explains the motor syndrome."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pain is a common, underrecognized non-motor feature of Parkinson's: beyond musculoskeletal and dystonic pain, central pain arises from altered nociceptive processing in dopaminergic pathways; some PD pain fluctuates with 'off' periods and eases with dopaminergic therapy."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression is one of the commonest non-motor features of Parkinson's, often preceding motor symptoms: degeneration of dopaminergic, serotonergic, and noradrenergic systems—not just illness burden—drives it, so PD depression is intrinsic to the neurodegeneration."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Parkinson's may begin in the gut: α-synuclein pathology appears in the enteric nervous system years before the brain (preceded by constipation), and an altered gut microbiome is implicated, supporting Braak's hypothesis that disease ascends the vagus from gut to brainstem."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "Parkinson's and Huntington's are movement disorders at opposite poles: PD is hypokinetic from dopamine loss, causing bradykinesia and rigidity, while Huntington's is hyperkinetic from striatal degeneration, causing chorea—mirror images of basal-ganglia dysfunction."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Parkinson's disease and schizophrenia are dopamine opposites: PD comes from too little striatal dopamine, while psychosis involves too much dopamine signaling—so antipsychotics cause parkinsonism and PD drugs can cause psychosis."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Parkinson's disease and narcolepsy both disrupt sleep-wake regulation: PD patients commonly have REM-sleep behavior disorder years before motor symptoms, plus excessive daytime sleepiness, reflecting degeneration of brainstem sleep nuclei—an early PD warning sign."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes participate in Parkinson's neurodegeneration: reactive astrocytes can clear or spread α-synuclein, lose support of dopaminergic neurons, and amplify neuroinflammation with microglia—so glia, not just dying neurons, shape progression."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Parkinson's is not just a dopamine disease: degeneration of noradrenergic locus coeruleus neurons depletes norepinephrine, driving the autonomic failure, orthostatic hypotension and cognitive and mood symptoms that levodopa cannot fix."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin neurons degenerate in Parkinson's too: their loss contributes to the depression, anxiety and sleep disturbance that often precede motor signs, and serotonergic terminals also aberrantly process levodopa, contributing to dyskinesias."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Parkinson's is a disorder of the whole nervous system: though defined by nigral dopamine loss and tremor, alpha-synuclein pathology spreads from gut and brainstem to cortex, explaining the autonomic, sleep, sensory and cognitive features beyond movement."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Parkinson's is a dopamine-acetylcholine imbalance: as dopamine falls, relatively unopposed cholinergic activity in the striatum worsens tremor, so anticholinergic drugs help—while loss of cholinergic neurons elsewhere contributes to the dementia of advanced disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron accumulates in the Parkinson's brain: the substantia nigra loads with iron that can catalyze oxidative damage and ferroptosis of dopamine neurons, so brain iron is both a disease marker on MRI and a candidate target for protective therapy."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Parkinson's often begins in the gut: constipation can precede tremor by years, and misfolded alpha-synuclein appears in enteric nerves early—fuelling the 'gut-first' hypothesis that the disease may ascend the vagus nerve from gut to brain."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Parkinson's disrupts the basal ganglia's glutamate balance: losing dopamine lets the subthalamic nucleus fire excess glutamate onto output nuclei, driving the movement slowing—so the NMDA-blocker amantadine and deep-brain stimulation of this glutamatergic hub help."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Parkinson's has an autoimmune flavor: T-helper cells that recognize alpha-synuclein peptides infiltrate the brain and may accelerate dopaminergic neuron loss, linking the adaptive immune system to a classic neurodegenerative disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Parkinson's denervates the heart early: loss of sympathetic nerves to the heart (seen on MIBG imaging) is a characteristic, early sign reflecting that alpha-synuclein pathology spreads through the autonomic nervous system beyond the brain."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Parkinson's dopamine neurons are vulnerable because of calcium: the substantia nigra cells are autonomous pacemakers that fire using calcium channels, and that constant calcium load stresses mitochondria—why calcium-channel blockers are tested to protect them."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Parkinson's is partly an energy failure: mitochondrial complex-I defects and failed mitophagy starve dopamine neurons of ATP, and the toxin MPTP that causes parkinsonism works exactly by poisoning this energy supply."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Parkinson's has an autoimmune streak involving regulatory T cells: T cells that recognize alpha-synuclein appear in patients, and a shortage of restraining Tregs may let this immune attack add to the neurodegeneration."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Parkinson's may begin at the synapse: alpha-synuclein normally works at presynaptic terminals, and its misfolding cripples dopamine release and synaptic function long before neurons die—so the disease is in part a failure of synapses, not just cells."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Parkinson's may start in the gut: alpha-synuclein clumps appear in the large intestine's nerves years early, constipation is among the first symptoms, and the pathology may climb the vagus nerve from bowel to brain."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Parkinson's smolders with TNF-α: activated microglia pour out this cytokine in the affected brain, and the chronic neuroinflammation it drives is thought to accelerate the loss of dopamine neurons."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Parkinson's can be imaged: a DaTscan uses radioactive photons to show the depleted dopamine terminals in the striatum, separating true Parkinson's from tremor that merely mimics it."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Parkinson's leaves traces in the skin: alpha-synuclein deposits can be found in skin nerve biopsies as an emerging diagnostic test, and seborrheic dermatitis is a common early sign."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Where alpha-synuclein lodges decides the disease: when it accumulates in oligodendrocytes rather than neurons, the result is multiple system atrophy, a faster Parkinson-plus disorder."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals Parkinson's defining lesion: the Lewy body, a dense core of tangled alpha-synuclein filaments inside the dying dopamine neuron, surrounded by the swollen, failing mitochondria that mark its energy crisis."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Parkinson's shows in the eyes: blinking slows to a stare, eye movements grow jerky, and dopamine loss thins the retina — a change now studied as an early imaging biomarker of the disease in the brain."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper handling falters in the Parkinson's brain: the metal normally helps antioxidant defenses, and its disturbed balance in the substantia nigra adds to the oxidative stress, alongside iron, that kills the dopamine neurons."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Parkinson's slows the stomach: gastroparesis delays emptying so erratically that levodopa absorption becomes unpredictable, causing the on-off motor swings, while the delayed transit is part of the gut dysfunction that may even precede the tremor."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Sleep breaks down early in Parkinson's: REM sleep behavior disorder — acting out dreams — is a striking prodrome that can precede the disease by years, and disrupted melatonin and circadian rhythm worsen the fragmented nights."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Autonomic failure reaches the body's smooth muscle: the disease's loss of autonomic control slows gut and bladder smooth muscle into constipation and urinary trouble, and weakens vascular tone into the orthostatic hypotension that causes falls."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Clearing the rogue protein is the new hope: monoclonal antibodies against aggregated alpha-synuclein are in trials to slow Parkinson's, aiming to mop up the misfolded protein before it spreads neuron to neuron."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Parkinson's is a disease of basal-ganglia GABA circuits: losing dopamine unbalances the GABAergic direct and indirect pathways, over-inhibiting movement — and that same GABA output is what deep-brain stimulation and pallidotomy retune."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Dopamine treatment can unleash compulsions: dopamine-agonist drugs trigger impulse-control disorders including hypersexuality, while autonomic disease causes erectile and sexual dysfunction — and estrogen's neuroprotection may explain why men are affected more."
---

# Parkinson's Disease

## Overview

**Parkinson's disease (PD)** is the **second most common neurodegenerative disease** after Alzheimer's, affecting approximately **10 million people worldwide** (~1 million in the US). It is defined by the selective loss of **dopaminergic neurons in the substantia nigra pars compacta (SNpc)** and the accumulation of **alpha-synuclein-containing Lewy bodies** in surviving neurons. The clinical hallmarks are the motor triad of **bradykinesia** (required for diagnosis), **muscular rigidity**, and **resting tremor**, with postural instability emerging later [^kalia-2015-pd-review].

PD is primarily a disease of aging (mean onset ~60 years), but **~10–15% of cases are early-onset (<50 years)**, often with a genetic cause. Lifetime risk is ~2% for men, ~1.3% for women. Incidence is increasing globally as populations age.

**Pathological staging (Braak staging of PD):**
- **Stage 1-2 (presymptomatic):** Alpha-synuclein pathology in olfactory bulb and dorsal motor nucleus of vagus nerve (explains anosmia and autonomic dysfunction years before motor symptoms)
- **Stage 3-4 (symptomatic):** SNpc degeneration → dopamine depletion → motor symptoms emerge (when >50-60% of SNpc neurons are lost)
- **Stage 5-6 (advanced):** Spread to limbic cortex and neocortex → dementia (Parkinson's disease dementia, PDD) in ~80% over 20 years

**Genetics:**
- **Familial PD (~10-15%):** Autosomal dominant: *SNCA* (alpha-synuclein, A53T/A30P/E46K triplication) → toxic aggregation; *LRRK2* G2019S (most common genetic PD, ~1-2% sporadic, ~13% Ashkenazi Jewish) → kinase overactivation; autosomal recessive: *PRKN* (Parkin), *PINK1*, *DJ-1* → mitochondrial quality control failure
- **Sporadic PD (>85%):** Complex polygenic; *GBA* variants (glucocerebrosidase, ~5-10% of PD) are the most common genetic risk factor; GWAS identified >90 risk loci

## Structure

### Dopaminergic circuit

**Nigrostriatal pathway:** SNpc dopaminergic axons project to the **striatum (caudate + putamen)** → regulate the basal ganglia motor loop:
- **Direct pathway (D1 receptors):** Striatum → inhibits GPi/SNpr → disinhibits thalamus → facilitates cortical motor activation ("GO")
- **Indirect pathway (D2 receptors):** Striatum → inhibits GPe → releases STN inhibition → activates GPi/SNpr → inhibits thalamus → suppresses cortical activation ("STOP")
- **PD effect:** Dopamine loss → weakened direct pathway, overactive indirect pathway → thalamic suppression → bradykinesia and rigidity; STN becomes hyperactive → target for deep brain stimulation (DBS)

**Other affected pathways:**
- **Mesolimbic/mesocortical (VTA → limbic/frontal cortex):** Dopamine loss → depression, apathy, and cognitive impairment in advanced PD
- **Noradrenergic (locus coeruleus):** Early degeneration → orthostatic hypotension, mood disorders, gait freezing
- **Serotonergic (raphe nuclei):** Depression in ~40% of PD
- **Enteric nervous system:** Alpha-synuclein in myenteric plexus → constipation (often precedes motor symptoms by years; supports "gut-first" PD hypothesis)

### Alpha-synuclein and Lewy body pathology [^spillantini-1997-lewy-body]

**Alpha-synuclein (SNCA, 140 aa):** Presynaptic protein; normally regulates synaptic vesicle trafficking and neurotransmitter release. Intrinsically disordered → forms amphipathic helical structure on membranes.

**Aggregation cascade:**
1. Misfolded alpha-synuclein monomers → soluble oligomers (most neurotoxic, disrupt membranes and mitochondria) → protofibrils → insoluble amyloid fibrils
2. Fibrils compact with ubiquitin, neurofilaments, and chaperones → **Lewy bodies** (spherical, eosinophilic, ~5-25 μm, cytoplasmic inclusions)
3. Lewy bodies spread between connected neurons in a prion-like manner (trans-synaptic transmission of alpha-synuclein seeds → Braak staging)

**Triggers of aggregation:**
- Genetic: SNCA A53T/duplication/triplication → concentration-dependent aggregation
- Environmental: Pesticides (rotenone, paraquat) → mitochondrial complex I inhibition → oxidative stress → synuclein misfolding
- Post-translational: Phospho-Ser129 (90% of aggregated synuclein is phosphorylated); nitrosylation, ubiquitination

**Degradation failure:**
- Normal: Alpha-synuclein cleared by UPS (ubiquitin-proteasome system) and chaperone-mediated autophagy (CMA, via LAMP-2A)
- PD: Mutant/oligomeric synuclein blocks LAMP-2A → impairs CMA → accumulates; LRRK2 G2019S phosphorylates beclin-1 → impairs macroautophagy

## Function

### Clinical presentation [^kalia-2015-pd-review]

**Motor features (cardinal triad):**
- **Bradykinesia (required for diagnosis):** Slowness and decrement in amplitude of repetitive movements (finger tapping, foot stomping); micrographia; masked facies (hypomimia); hypophonia
- **Rigidity:** Lead-pipe or cogwheel (tremor superimposed) resistance throughout range of motion; paratonia; Froment's maneuver (contralateral activation enhances rigidity)
- **Resting tremor (4-6 Hz):** Pill-rolling; suppressed with voluntary movement; worsened by stress; asymmetric onset; may be absent (akinetic-rigid variant)
- **Postural instability:** Pull test → retropulsion; gait freezing (festination); falls are leading cause of morbidity/mortality in advanced PD

**Non-motor features (often precede motor by years):**
- **Prodromal:** Anosmia (~90% at diagnosis), REM sleep behavior disorder (RBD — acts out dreams, high specificity for synucleinopathy), constipation, depression
- **Autonomic:** Orthostatic hypotension (↑ fall risk); urinary urgency/retention; sweating abnormalities; sexual dysfunction; gastroparesis
- **Neuropsychiatric:** Depression (~40%), anxiety (~40%), impulse control disorders (dopamine agonists → gambling, hypersexuality), psychosis (hallucinations with levodopa — treat with clozapine or pimavanserin)
- **Cognitive:** Mild cognitive impairment (MCI) at diagnosis in ~25%; PD dementia in ~80% at 20 years; earlier dementia with Lewy body disease (DLB) if dementia precedes motor features

**Diagnostic criteria (MDS Clinical Criteria, 2015):**
- Definite PD: Parkinsonism (bradykinesia + rigidity and/or tremor) + no exclusion criteria + ≥2 supportive features + no red flags
- Supportive features: Unilateral onset, rest tremor, levodopa response, levodopa-induced dyskinesia, olfactory loss, cardiac sympathetic denervation on MIBG scintigraphy
- Red flags: Falls early, bulbar dysfunction early, autonomic failure preceding motor, limited levodopa response → suggest atypical parkinsonism (MSA, PSP, CBD, DLB)

### Differential diagnosis: atypical parkinsonism

| Feature | PD | MSA | PSP | CBD |
|:---|:---|:---|:---|:---|
| Symmetry | Asymmetric | Symmetric | Symmetric | Asymmetric |
| Tremor | Rest tremor | Rare | Rare | Rare |
| Levodopa response | Excellent | Poor | Poor | Poor |
| Falls | Late | Early | Very early | Moderate |
| Eye movement | Normal | Normal | Vertical gaze palsy | Abnormal |
| Autonomic | Mild-moderate | Severe early | Mild | Mild |

## Pathology

### Diagnosis

**Clinical (gold standard):** MDS criteria; DAT-SPECT (DaTscan) — confirms dopaminergic deficit in striatum; 90% specificity for nigrostriatal degeneration vs. essential tremor.

**Biomarkers (emerging):**
- **CSF/blood alpha-synuclein:** Seed amplification assay (SAA/RT-QuIC) — >90% sensitivity/specificity for PD/DLB vs. healthy controls; FDA breakthrough designation
- **Skin biopsy:** Phospho-synuclein in dermal nerve fibers — non-invasive biomarker
- **GBA activity:** Plasma glucocerebrosidase activity predicts GBA-PD and severity
- **MRI:** Substantia nigra hyperechogenicity (transcranial ultrasound); neuromelanin-sensitive MRI; iron accumulation on SWI in SNpc

### Treatment [^olanow-2009-pd-treatment]

**Dopaminergic replacement:**

*Levodopa/carbidopa (Sinemet) — gold standard:*
- Levodopa: Dopamine precursor; crosses blood-brain barrier; metabolized to dopamine in striatum
- Carbidopa: Peripheral DOPA decarboxylase inhibitor → prevents peripheral conversion → reduces nausea, allows lower levodopa dose
- **Initial motor response:** ~90% improvement in motor symptoms; most effective treatment
- **Motor complications (after 5-10 years):**
  - *Wearing off:* Shortened motor response duration (correlates with shrinking levodopa half-life as PD progresses) → treat with COMT inhibitors (entacapone) or MAO-B inhibitors (rasagiline), or controlled-release formulations
  - *Dyskinesia:* Involuntary choreiform movements at peak dose; treat by reducing levodopa dose, adding amantadine (NMDA antagonist)
  - *ON-OFF fluctuations:* Unpredictable motor response → continuous dopaminergic stimulation via levodopa-carbidopa intestinal gel (LCIG, Duopa) or subcutaneous levodopa (ND0612)

*Dopamine agonists (pramipexole, ropinirole, rotigotine patch):*
- Directly stimulate D2/D3 receptors; longer half-life → fewer motor fluctuations
- First-line for younger patients (<60) to delay levodopa motor complications
- Side effects: Impulse control disorders (gambling, hypersexuality, binge eating) in ~15-20%; daytime somnolence; hallucinations in elderly

*MAO-B inhibitors (selegiline, rasagiline, safinamide):*
- Inhibit monoamine oxidase B → reduce dopamine catabolism; mild symptomatic benefit and possible neuroprotective effect (ADAGIO trial: rasagiline 1 mg/day — modest but persistent benefit)

*COMT inhibitors (entacapone, opicapone, tolcapone):*
- Block catechol-O-methyltransferase → reduce peripheral and central levodopa metabolism → extend levodopa effect and reduce wearing off

**Deep brain stimulation (DBS):**
- Bilateral subthalamic nucleus (STN) or globus pallidus internus (GPi) DBS → reduce motor fluctuations and dyskinesias by ~50-60%
- Indication: Advanced PD with motor complications refractory to medication; requires >4 years levodopa benefit; contraindicated with severe dementia or active psychiatric illness
- **STN DBS** → allows levodopa reduction (reduces dyskinesia); **GPi DBS** → more directly reduces dyskinesia without levodopa reduction; Vim DBS for tremor-predominant PD
- Adaptive DBS (closed-loop): Neural signal-triggered stimulation → individualized and more effective

**Disease-modifying therapies (investigational):**
- **Alpha-synuclein immunotherapy:** Anti-synuclein antibodies (prasinezumab Phase IIb → negative on primary endpoint but signal in fast progressors; cinpanemab — negative)
- **LRRK2 kinase inhibitors (DNL201, BIIB094):** Reduce LRRK2 phosphorylation targets; Phase 2 ongoing in LRRK2-PD; also tested in sporadic PD (LRRK2 is activated in sporadic PD under inflammatory conditions)
- **GBA-targeting:** Ambroxol (chaperone → enhances GBA folding, Phase 2 ongoing); gene therapy (AAV-GBA intrathecal injection)
- **GLP-1 agonists (semaglutide, liraglutide):** Retrospective data: GLP-1 agonist use in T2DM associated with lower PD risk; Phase 2 trials ongoing based on neuroprotective mechanism (AMPK activation, neuroinflammation reduction)
- **Iron chelation:** Deferiprone (Phase 3 FAIR-PARK-II) — negative on primary endpoint; dopaminergic neuron iron overload drives oxidative stress in SNpc

**Symptomatic non-dopaminergic:**
- Rivastigmine (ChEI) for PD dementia
- Pimavanserin (5-HT2A inverse agonist) for PD psychosis — does not worsen motor symptoms
- Clonazepam for REM sleep behavior disorder
- Fludrocortisone/droxidopa for neurogenic orthostatic hypotension
- Exercise: Aerobic exercise (treadmill, cycling) → BDNF upregulation → neuroprotective in animal models; improves gait, balance, cognition in clinical trials (ParkProTreK)

## Connections

- `targets` → **[Brain](../../06-organ/brain/README.md)** — PD selectively destroys dopaminergic neurons in the substantia nigra pars compacta, disrupting basal ganglia motor circuitry; alpha-synuclein Lewy body pathology spreads via Braak staging from brainstem to neocortex.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — alpha-synuclein aggregates activate microglia via TLR2/4 and NLRP3 inflammasome, driving IL-1β-mediated dopaminergic neuron death; chronic neuroinflammation amplifies degeneration throughout disease course.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — alpha-synuclein is cleared by CMA and macroautophagy; LRRK2 and mutant SNCA impair autophagy flux, promoting aggregate accumulation; TFEB activation and rapamycin reduce synuclein pathology in preclinical PD models.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — both are age-related neurodegenerative diseases with prion-like protein spreading (tau/Aβ in AD; alpha-synuclein in PD); shared pathomechanisms include mitochondrial dysfunction, autophagy failure, and neuroinflammation; Lewy body dementia bridges both.
- `connects-to` → **[SNCA](../../03-molecular/snca/README.md)** — SNCA missense mutations (A53T, A30P, E46K) and gene duplication/triplication cause familial PD; misfolded alpha-synuclein fibrils are the main component of Lewy bodies; SNCA propagates via synaptic connections following Braak staging from brainstem to neocortex.
- `connects-to` → **[LRRK2](../../03-molecular/lrrk2/README.md)** — LRRK2 G2019S (~1-2% of sporadic PD, ~40% penetrance by age 80) is the most common pathogenic variant causing familial PD; LRRK2 kinase hyperactivation → Rab GTPase hyperphosphorylation → vesicle trafficking defects and α-synuclein aggregation in dopaminergic neurons.
- `connects-to` → **[MAPT](../../03-molecular/mapt/README.md)** — MAPT H1 haplotype (common in Europeans) is a risk factor for PD and PSP; tau co-aggregates with alpha-synuclein in Lewy body dementia and some PD brains; MAPT LOF mutations cause FTLD-MAPT; tau and SNCA pathology converge on mitochondrial dysfunction and autophagy impairment.
- `connects-to` → **[Lewy Body Dementia](../lewy-body-dementia/README.md)** — DLB and PD are both alpha-synuclein synucleinopathies distinguished by the 1-year rule; DLB features early cortical Lewy bodies while PD follows Braak brainstem→cortex staging; PDD (Parkinson's disease dementia) occurs in ~80% of PD at 20 years and shares DLB's cholinergic deficit and rivastigmine responsiveness.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Parkinson's is defined by dopamine loss: degeneration of substantia nigra pars compacta neurons depletes striatal dopamine → bradykinesia, rigidity and tremor once ~60-80% is gone; levodopa, dopamine agonists and MAO-B/COMT inhibitors restore dopaminergic tone.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Parkinson's is a neurodegeneration of specific neurons: α-synuclein-laden Lewy bodies accumulate in dopaminergic substantia nigra neurons, driving mitochondrial and autophagy failure and selective death; the vulnerability of these pacemaking neurons explains the motor syndrome.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pain is a common, underrecognized non-motor feature of Parkinson's: beyond musculoskeletal and dystonic pain, central pain arises from altered nociceptive processing in dopaminergic pathways; some PD pain fluctuates with 'off' periods and eases with dopaminergic therapy.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression is one of the commonest non-motor features of Parkinson's, often preceding motor symptoms: degeneration of dopaminergic, serotonergic, and noradrenergic systems—not just illness burden—drives it, so PD depression is intrinsic to the neurodegeneration.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Parkinson's may begin in the gut: α-synuclein pathology appears in the enteric nervous system years before the brain (preceded by constipation), and an altered gut microbiome is implicated, supporting Braak's hypothesis that disease ascends the vagus from gut to brainstem.
- `connects-to` → **[Huntington Disease](../huntingtons-disease/README.md)** — Parkinson's and Huntington's are movement disorders at opposite poles: PD is hypokinetic from dopamine loss, causing bradykinesia and rigidity, while Huntington's is hyperkinetic from striatal degeneration, causing chorea—mirror images of basal-ganglia dysfunction.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Parkinson's disease and schizophrenia are dopamine opposites: PD comes from too little striatal dopamine, while psychosis involves too much dopamine signaling—so antipsychotics cause parkinsonism and PD drugs can cause psychosis.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Parkinson's disease and narcolepsy both disrupt sleep-wake regulation: PD patients commonly have REM-sleep behavior disorder years before motor symptoms, plus excessive daytime sleepiness, reflecting degeneration of brainstem sleep nuclei—an early PD warning sign.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes participate in Parkinson's neurodegeneration: reactive astrocytes can clear or spread α-synuclein, lose support of dopaminergic neurons, and amplify neuroinflammation with microglia—so glia, not just dying neurons, shape progression.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Parkinson's is not just a dopamine disease: degeneration of noradrenergic locus coeruleus neurons depletes norepinephrine, driving the autonomic failure, orthostatic hypotension and cognitive and mood symptoms that levodopa cannot fix.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin neurons degenerate in Parkinson's too: their loss contributes to the depression, anxiety and sleep disturbance that often precede motor signs, and serotonergic terminals also aberrantly process levodopa, contributing to dyskinesias.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Parkinson's is a disorder of the whole nervous system: though defined by nigral dopamine loss and tremor, alpha-synuclein pathology spreads from gut and brainstem to cortex, explaining the autonomic, sleep, sensory and cognitive features beyond movement.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Parkinson's is a dopamine-acetylcholine imbalance: as dopamine falls, relatively unopposed cholinergic activity in the striatum worsens tremor, so anticholinergic drugs help—while loss of cholinergic neurons elsewhere contributes to the dementia of advanced disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron accumulates in the Parkinson's brain: the substantia nigra loads with iron that can catalyze oxidative damage and ferroptosis of dopamine neurons, so brain iron is both a disease marker on MRI and a candidate target for protective therapy.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Parkinson's often begins in the gut: constipation can precede tremor by years, and misfolded alpha-synuclein appears in enteric nerves early—fuelling the 'gut-first' hypothesis that the disease may ascend the vagus nerve from gut to brain.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Parkinson's disrupts the basal ganglia's glutamate balance: losing dopamine lets the subthalamic nucleus fire excess glutamate onto output nuclei, driving the movement slowing—so the NMDA-blocker amantadine and deep-brain stimulation of this glutamatergic hub help.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Parkinson's has an autoimmune flavor: T-helper cells that recognize alpha-synuclein peptides infiltrate the brain and may accelerate dopaminergic neuron loss, linking the adaptive immune system to a classic neurodegenerative disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Parkinson's denervates the heart early: loss of sympathetic nerves to the heart (seen on MIBG imaging) is a characteristic, early sign reflecting that alpha-synuclein pathology spreads through the autonomic nervous system beyond the brain.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Parkinson's dopamine neurons are vulnerable because of calcium: the substantia nigra cells are autonomous pacemakers that fire using calcium channels, and that constant calcium load stresses mitochondria—why calcium-channel blockers are tested to protect them.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Parkinson's is partly an energy failure: mitochondrial complex-I defects and failed mitophagy starve dopamine neurons of ATP, and the toxin MPTP that causes parkinsonism works exactly by poisoning this energy supply.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Parkinson's has an autoimmune streak involving regulatory T cells: T cells that recognize alpha-synuclein appear in patients, and a shortage of restraining Tregs may let this immune attack add to the neurodegeneration.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Parkinson's may begin at the synapse: alpha-synuclein normally works at presynaptic terminals, and its misfolding cripples dopamine release and synaptic function long before neurons die—so the disease is in part a failure of synapses, not just cells.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Parkinson's may start in the gut: alpha-synuclein clumps appear in the large intestine's nerves years early, constipation is among the first symptoms, and the pathology may climb the vagus nerve from bowel to brain.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Parkinson's smolders with TNF-α: activated microglia pour out this cytokine in the affected brain, and the chronic neuroinflammation it drives is thought to accelerate the loss of dopamine neurons.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Parkinson's can be imaged: a DaTscan uses radioactive photons to show the depleted dopamine terminals in the striatum, separating true Parkinson's from tremor that merely mimics it.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Parkinson's leaves traces in the skin: alpha-synuclein deposits can be found in skin nerve biopsies as an emerging diagnostic test, and seborrheic dermatitis is a common early sign.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Where alpha-synuclein lodges decides the disease: when it accumulates in oligodendrocytes rather than neurons, the result is multiple system atrophy, a faster Parkinson-plus disorder.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals Parkinson's defining lesion: the Lewy body, a dense core of tangled alpha-synuclein filaments inside the dying dopamine neuron, surrounded by the swollen, failing mitochondria that mark its energy crisis.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Parkinson's shows in the eyes: blinking slows to a stare, eye movements grow jerky, and dopamine loss thins the retina — a change now studied as an early imaging biomarker of the disease in the brain.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper handling falters in the Parkinson's brain: the metal normally helps antioxidant defenses, and its disturbed balance in the substantia nigra adds to the oxidative stress, alongside iron, that kills the dopamine neurons.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Parkinson's slows the stomach: gastroparesis delays emptying so erratically that levodopa absorption becomes unpredictable, causing the on-off motor swings, while the delayed transit is part of the gut dysfunction that may even precede the tremor.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Sleep breaks down early in Parkinson's: REM sleep behavior disorder — acting out dreams — is a striking prodrome that can precede the disease by years, and disrupted melatonin and circadian rhythm worsen the fragmented nights.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Autonomic failure reaches the body's smooth muscle: the disease's loss of autonomic control slows gut and bladder smooth muscle into constipation and urinary trouble, and weakens vascular tone into the orthostatic hypotension that causes falls.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Clearing the rogue protein is the new hope: monoclonal antibodies against aggregated alpha-synuclein are in trials to slow Parkinson's, aiming to mop up the misfolded protein before it spreads neuron to neuron.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Parkinson's is a disease of basal-ganglia GABA circuits: losing dopamine unbalances the GABAergic direct and indirect pathways, over-inhibiting movement — and that same GABA output is what deep-brain stimulation and pallidotomy retune.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Dopamine treatment can unleash compulsions: dopamine-agonist drugs trigger impulse-control disorders including hypersexuality, while autonomic disease causes erectile and sexual dysfunction — and estrogen's neuroprotection may explain why men are affected more.

[^kalia-2015-pd-review]: Kalia LV, Lang AE. Parkinson's disease. *Lancet.* 2015;386(9996):896-912. [doi:10.1016/S0140-6736(14)61393-3](https://doi.org/10.1016/S0140-6736(14)61393-3) · [PubMed 25904081](https://pubmed.ncbi.nlm.nih.gov/25904081/)
[^spillantini-1997-lewy-body]: Spillantini MG, Schmidt ML, Lee VM, Trojanowski JQ, Jakes R, Goedert M. Alpha-synuclein in Lewy bodies. *Nature.* 1997;388(6645):839-840. [doi:10.1038/42166](https://doi.org/10.1038/42166) · [PubMed 9278044](https://pubmed.ncbi.nlm.nih.gov/9278044/)
[^olanow-2009-pd-treatment]: Olanow CW, Stern MB, Sethi K. The scientific and clinical basis for the treatment of Parkinson disease. *Neurology.* 2009;72(21 Suppl 4):S1-136. [doi:10.1212/WNL.0b013e3181a1d44c](https://doi.org/10.1212/WNL.0b013e3181a1d44c) · [PubMed 19470958](https://pubmed.ncbi.nlm.nih.gov/19470958/)
