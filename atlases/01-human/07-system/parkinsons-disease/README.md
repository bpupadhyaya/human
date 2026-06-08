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

[^kalia-2015-pd-review]: Kalia LV, Lang AE. Parkinson's disease. *Lancet.* 2015;386(9996):896-912. [doi:10.1016/S0140-6736(14)61393-3](https://doi.org/10.1016/S0140-6736(14)61393-3) · [PubMed 25904081](https://pubmed.ncbi.nlm.nih.gov/25904081/)
[^spillantini-1997-lewy-body]: Spillantini MG, Schmidt ML, Lee VM, Trojanowski JQ, Jakes R, Goedert M. Alpha-synuclein in Lewy bodies. *Nature.* 1997;388(6645):839-840. [doi:10.1038/42166](https://doi.org/10.1038/42166) · [PubMed 9278044](https://pubmed.ncbi.nlm.nih.gov/9278044/)
[^olanow-2009-pd-treatment]: Olanow CW, Stern MB, Sethi K. The scientific and clinical basis for the treatment of Parkinson disease. *Neurology.* 2009;72(21 Suppl 4):S1-136. [doi:10.1212/WNL.0b013e3181a1d44c](https://doi.org/10.1212/WNL.0b013e3181a1d44c) · [PubMed 19470958](https://pubmed.ncbi.nlm.nih.gov/19470958/)
