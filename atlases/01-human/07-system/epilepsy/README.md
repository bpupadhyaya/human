---
schema: human-scale-entry/v1
id: epilepsy
name: Epilepsy
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Epilepsy (recurrent unprovoked seizures; 50M affected) comprises focal and generalized types; causes: structural, genetic (SCN1A-Dravet, KCNQ2, TSC1/2), autoimmune (anti-NMDAR), metabolic; valproate and levetiracetam are first-line; surgery and VNS for drug-refractory disease."
aliases: ["epilepsy", "seizure disorder", "Dravet syndrome", "temporal lobe epilepsy", "MTLE", "absence epilepsy", "childhood absence", "juvenile myoclonic epilepsy", "JME", "status epilepticus", "GEFS+", "West syndrome", "Lennox-Gastaut syndrome", "focal epilepsy", "generalized epilepsy"]
sources:
  - id: fisher-2017-ilae-classification
    type: peer-reviewed
    cite: "Fisher RS, Cross JH, D'Souza C, et al. Instruction manual for the ILAE 2017 operational classification of seizure types. Epilepsia. 2017;58(4):531-542."
    doi: "10.1111/epi.13671"
    pmid: "28276060"
    url: "https://doi.org/10.1111/epi.13671"
    accessed: "2026-06-08"
  - id: devinsky-2018-epilepsy-review
    type: peer-reviewed
    cite: "Devinsky O, Vezzani A, O'Brien TJ, et al. Epilepsy. Nat Rev Dis Primers. 2018;4:18024."
    doi: "10.1038/nrdp.2018.24"
    pmid: "29722352"
    url: "https://doi.org/10.1038/nrdp.2018.24"
    accessed: "2026-06-08"
  - id: engel-2012-mtle-surgery
    type: peer-reviewed
    cite: "Engel J Jr, McDermott MP, Wiebe S, et al. Early surgical therapy for drug-resistant temporal lobe epilepsy: a randomized trial. JAMA. 2012;307(9):922-930."
    doi: "10.1001/jama.2012.220"
    pmid: "22396514"
    url: "https://doi.org/10.1001/jama.2012.220"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/scn1a
    relation: connects-to
    note: "SCN1A encodes Nav1.1; de novo LOF mutations cause Dravet syndrome (SMEI) — the most severe genetic epilepsy; gain-of-function → GEFS+; Nav1.1 haploinsufficiency in GABAergic interneurons → cortical disinhibition → seizures; sodium channel blockers worsen Dravet."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "GABAergic interneurons maintain cortical inhibitory balance — the fundamental seizure brake; GABA-A receptor potentiators (benzodiazepines, phenobarbital, clobazam) and GABA-T inhibitors (valproate, vigabatrin) are the most widely used antiepileptic drugs."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR pathway gain-of-function mutations cause structural epilepsies: TSC1/TSC2 → tuberous sclerosis (seizures in 80-90% of patients); somatic PIK3CA/MTOR mutations → focal cortical dysplasia type IIb (FCDII); mTOR inhibitor everolimus reduces TSC-associated seizures by ~50%."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Epilepsy arises from focal or generalized cortical networks; MTLE involves hippocampal sclerosis; absence seizures arise from 3 Hz cortical-thalamic spike-wave; brainstem involvement explains autonomic seizure features and SUDEP; epilepsy surgery targets the epileptogenic zone."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Epilepsy risk is 2-3× elevated in AD; amyloid-driven cortical hyperexcitability precedes clinical dementia; anti-NMDAR and LGI1 autoimmune encephalitides cause encephalitis with new-onset epilepsy mimicking rapid-onset dementia; LGI1 faciobrachial seizures are pathognomonic."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Allopregnanolone (progesterone metabolite) is a potent GABA-A PAM via delta subunit extrasynaptic receptors → sedation, anxiolysis, anticonvulsant; progesterone withdrawal → allopregnanolone decline → GABA-A downregulation → seizure threshold reduction in catamenial epilepsy."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Epilepsy and migraine are comorbid disorders of cortical hyperexcitability that share genetics: gain-of-function SCN1A causes familial hemiplegic migraine while loss-of-function causes Dravet epilepsy, and valproate and topiramate treat both."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Seizures are an excitation-inhibition imbalance, and glutamate is the excitatory side: AMPA/NMDA over-activity drives synchronous bursting, and the AMPA antagonist perampanel is an antiseizure drug — the counterpart to GABA's brake."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "A seizure is hypersynchronous neuronal firing: bursting pyramidal neurons and recurrent excitatory collaterals overwhelm GABAergic interneurons → a paroxysmal depolarizing shift; most genetic epilepsies are neuronal ion-channelopathies that tip this balance."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Tuberous sclerosis is a paradigmatic genetic epilepsy: cortical tubers and TSC1/TSC2-driven mTOR overactivation cause early, often drug-resistant seizures (including infantile spasms), so mTOR inhibitors (everolimus) reduce seizures and early EEG-guided treatment is studied."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Stroke is a leading cause of acquired epilepsy in older adults: cortical infarcts and hemorrhages leave a gliotic, hyperexcitable scar that generates late-onset focal seizures months to years later; post-stroke epilepsy worsens outcomes and is managed with antiseizure medication."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes are active players in epilepsy, not bystanders: reactive astrogliosis impairs glutamate and potassium buffering and disrupts the blood-brain barrier, lowering seizure threshold; aberrant gap-junction coupling and inflammation sustain epileptogenesis."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Epilepsy and autism frequently co-occur and share biology: up to a third of autistic people have epilepsy, and both arise from disrupted excitation/inhibition balance and overlap in genes like SCN, TSC, and SHANK—often the same neurodevelopmental lesion."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Seizures are the commonest first sign of an IDH-mutant glioma: these slow-growing cortical tumors irritate neurons (partly via the oncometabolite 2-hydroxyglutarate altering glutamate), so new focal epilepsy in a young adult should prompt imaging for a low-grade glioma."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Epilepsy and depression have a bidirectional relationship: depression is the commonest psychiatric comorbidity of epilepsy and also raises the risk of developing it, shared limbic and serotonergic mechanisms link them, and depression strongly degrades quality of life."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "Brain tumors are an important cause of epilepsy: glioblastoma and other gliomas irritate surrounding cortex, so new-onset seizures in an adult mandate brain imaging—seizures are often the presenting sign of a glioma, and tumor-related epilepsy can be hard to control."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus is the seat of the commonest focal epilepsy: mesial temporal sclerosis—hippocampal scarring and neuron loss—generates temporal-lobe seizures, and surgically removing the sclerotic hippocampus can cure drug-resistant cases."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Epilepsy and schizophrenia are bidirectionally linked: temporal-lobe epilepsy can produce a schizophrenia-like psychosis, each roughly doubles the risk of the other, and they share disturbances of glutamate and GABA—so a first psychotic episode sometimes warrants EEG."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Voltage-gated sodium channels are epilepsy's central target: sodium influx fires the action potentials that, when runaway, become seizures, so many first-line drugs (phenytoin, lamotrigine) work by blocking these channels—and SCN1A mutations cause epilepsy."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Epilepsy is fundamentally a disorder of the synapse: seizures arise when synaptic excitation (glutamate) overwhelms inhibition (GABA), so the tipped excitation-inhibition balance at synapses is the common final pathway across epilepsy's many causes."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Epilepsy is a disorder of the whole nervous system's electrical stability: hypersynchronous neuronal discharges can start focally or generalize across networks, so seizures are a shared symptom of countless insults—from genetics to stroke, tumor and infection."
---

# Epilepsy

## Overview

**Epilepsy** is a chronic neurological disorder characterized by a predisposition to generate **recurrent unprovoked seizures** — the result of abnormal, excessive, or synchronous neuronal activity in the brain. The International League Against Epilepsy (ILAE) definition requires at least two unprovoked seizures occurring >24 hours apart, or one unprovoked seizure with ≥60% recurrence risk (e.g., a seizure after a stroke, cortical malformation, or certain EEG patterns) [^fisher-2017-ilae-classification].

Epilepsy affects approximately **50 million people worldwide** (~1% of the global population), making it the most common serious neurological condition after stroke and Alzheimer's disease. The annual incidence is 50-70 per 100,000 in developed countries; higher in low-income countries (120+ per 100,000) due to higher rates of birth asphyxia, infections (neurocysticercosis, cerebral malaria), and traumatic brain injury. **Drug-refractory epilepsy** — failure of two appropriately chosen antiepileptic drugs — affects ~30% of patients and represents the highest unmet need in epilepsy management [^devinsky-2018-epilepsy-review].

The biological basis of epilepsy is an imbalance between **neuronal excitation** (primarily glutamatergic, via AMPA and NMDA receptors) and **inhibition** (primarily GABAergic, via GABA-A chloride channels and GABA-B metabotropic receptors). Seizures arise when excitation transiently overwhelms inhibition in a pathologically susceptible network — due to ion channel mutations, cortical malformations, hippocampal sclerosis, autoimmune neuronal antibodies, metabolic derangements, or unknown causes.

## Structure

### ILAE 2017 seizure classification [^fisher-2017-ilae-classification]

**Focal seizures** (originate in a discrete cortical network in one hemisphere):
- **Focal aware** (formerly simple partial): Consciousness preserved; symptoms reflect the affected cortical region (motor, sensory, autonomic, psychic)
- **Focal impaired awareness** (formerly complex partial): Consciousness impaired; automatisms (lip-smacking, hand fumbling) common; most often from temporal lobe
- **Focal to bilateral tonic-clonic**: Focal seizure generalizes to involve both hemispheres → tonic-clonic convulsion; post-ictal confusion (Todd's paralysis possible if motor cortex involved)

**Generalized seizures** (involve both hemispheres from onset via cortical-subcortical networks):
- **Generalized tonic-clonic (GTC)**: Tonic phase (stiffening) → clonic phase (rhythmic jerking) → post-ictal stupor; highest injury/SUDEP risk
- **Absence (petit mal)**: 3 Hz spike-wave discharge on EEG; brief (5–30 s) staring with eye flicker; no post-ictal phase; childhood absence epilepsy (CAE) peak onset 4-8 years; often remits by puberty
- **Myoclonic**: Brief, shock-like muscle jerks; often in upper limbs; occur in juvenile myoclonic epilepsy (JME), Dravet syndrome, progressive myoclonic epilepsies
- **Atonic**: Sudden loss of muscle tone → drop attacks; associated with Lennox-Gastaut syndrome
- **Tonic, clonic**: Single-phase variants of GTC

### Epilepsy classification by etiology

| Etiology | Key examples | Mechanism | Seizure type |
|:---|:---|:---|:---|
| **Structural** | Hippocampal sclerosis (MTLE), cortical malformations (FCD), stroke, tumor | Focal cortical excitability ↑ from scarring/reorganization | Focal (±generalization) |
| **Genetic** | SCN1A (Dravet), KCNQ2 (neonatal), TSC1/2 (TSC), CDKL5, PCDH19 | Ion channel/scaffolding protein dysfunction | Focal or generalized |
| **Autoimmune** | Anti-NMDAR, anti-LGI1, anti-CASPR2, anti-GAD65 | Autoantibodies impair synaptic function | Focal (faciobrachial in LGI1), GTC |
| **Infectious** | Neurocysticercosis, cerebral malaria, HIV encephalitis | Perilesional inflammation/gliosis | Focal |
| **Metabolic** | Hypoglycemia, hyponatremia, GLUT1 deficiency, pyridoxine dependency | Altered ionic milieu or cofactor deficiency | Generalized |
| **Unknown** | ~30% of all epilepsies | Not yet identified | Focal or generalized |

### Key genetic epilepsy syndromes

| Gene | Channel/Protein | Syndrome | Key feature |
|:---|:---|:---|:---|
| **SCN1A** | Nav1.1 (GABAergic interneurons) | Dravet syndrome (SMEI) | Fever-sensitive; avoid Na-channel blockers |
| **SCN2A** | Nav1.2 (excitatory neurons) | Neonatal-onset encephalopathy | LOF early-onset; GOF late-onset; precision Na-channel therapy |
| **KCNQ2** | Kv7.2/Kv7.3 (M-current) | Neonatal epileptic encephalopathy | K+ channel LOF → neonatal seizures; carbamazepine beneficial |
| **CDKL5** | CDK-like kinase 5 | CDKL5 deficiency disorder | X-linked; spasms + severe encephalopathy; no effective treatment |
| **TSC1/TSC2** | Hamartin/Tuberin (mTOR) | Tuberous sclerosis complex | Cortical tubers + seizures (80%); everolimus reduces seizures |
| **PCDH19** | Protocadherin-19 | PCDH19 epilepsy | X-linked; affects only females; fever-sensitive clusters |
| **MECP2** | MeCP2 transcription factor | Rett syndrome | Progressive; loss of hand use; regression; after normal infancy |

### Autoimmune epilepsy

Neuronal autoantibodies cause acute encephalitis with new-onset epilepsy — often confused with viral encephalitis or new-onset psychiatric illness:

| Antibody target | Clinical syndrome | Seizure type | Treatment |
|:---|:---|:---|:---|
| **NMDA receptor (GluN1)** | Anti-NMDAR encephalitis | Complex focal, GTC; movement disorder | IVIG + methylprednisolone + rituximab |
| **LGI1** | Limbic encephalitis; faciobrachial dystonic seizures (FBDS) | FBDS (pathognomonic); complex focal | IVIG + steroids; FBDS responds dramatically |
| **CASPR2** | Morvan syndrome; limbic encephalitis | Complex focal; tonic | IVIG + steroids; thymoma association |
| **GAD65** | Stiff-person syndrome; limbic encephalitis | Complex focal; rarely GTC | Steroids; often poorly responsive |
| **AMPA receptor** | Limbic encephalitis | Complex focal | Steroids + rituximab |

Anti-NMDAR encephalitis is the most common autoimmune encephalitis (~37% of autoimmune encephalitis cases); predominantly affects young women; ovarian teratoma in ~50% of adult women; recovery possible with immunotherapy.

## Function

### Seizure initiation and spread

**Focal seizure initiation**: Abnormal synchronous burst firing (intrinsic bursting neurons + excitatory recurrent collaterals) overwhelms local inhibitory GABAergic interneurons → ictal discharge → spreads via cortical-cortical U-fibers and white matter tracts to ipsilateral, then contralateral networks.

**Absence seizure mechanism (cortical-thalamic model):**
1. Cortical focus → thalamic relay nuclei → reticular thalamic nucleus (RTN, GABAergic) → suppresses relay nuclei → synchronized 3 Hz oscillation; thalamic hyperpolarization → T-type calcium channel activation → low-threshold calcium spikes → rhythmic 3 Hz spike-wave
2. Valproate, ethosuximide, and lamotrigine inhibit T-type calcium channels → suppress absence seizures

**EEG signatures:**
- **3 Hz generalized spike-wave**: Childhood absence epilepsy, juvenile absence epilepsy
- **3-5.5 Hz polyspike-wave**: Juvenile myoclonic epilepsy (JME)
- **Hypsarrhythmia** (chaotic high-amplitude pattern): West syndrome (infantile spasms)
- **Slow spike-wave (<2.5 Hz)**: Lennox-Gastaut syndrome
- **Focal interictal epileptiform discharges (IEDs)**: Focal epilepsy; location reveals seizure focus
- **Temporal lobe theta/alpha**: Mesial temporal lobe epilepsy

### Mesial temporal lobe epilepsy (MTLE) — the most common adult focal epilepsy

**MTLE with hippocampal sclerosis (HS)** — the predominant adult focal epilepsy:
- **Pathology**: Selective loss of CA1 and CA3 hippocampal pyramidal neurons + mossy fiber sprouting (aberrant glutamatergic recurrent collaterals) → hyperexcitable hippocampus
- **Clinical features**: Aura (rising epigastric sensation, déjà vu, fear), complex partial seizures with oroalimentary automatisms, post-ictal confusion lasting minutes
- **Triggers**: Febrile seizures in early childhood (FS-HS relationship controversial), TBI, encephalitis
- **MRI findings**: T2/FLAIR hippocampal signal increase, CA1 atrophy, loss of internal structure on coronal MRI
- **Surgery**: Temporal lobectomy (anterior temporal + amygdalohippocampectomy) → 65-70% seizure-free at 2 years; superior to medical therapy in RCTs [^engel-2012-mtle-surgery]

## Pathology

### Status epilepticus (SE)

**Definition:** Seizure lasting >5 minutes (convulsive SE) or >30 minutes (non-convulsive SE) OR recurrent seizures without return to baseline.

**Emergency management (time-critical):**
1. **0–5 min**: Airway, breathing, circulation; check glucose; lorazepam (0.1 mg/kg IV, max 4 mg) or midazolam (IM/buccal/nasal) — benzodiazepine first-line
2. **5–20 min**: If benzodiazepine fails: levetiracetam (60 mg/kg IV), valproate (40 mg/kg IV), or fosphenytoin (20 mg/kg PE IV)
3. **20–40 min**: If refractory: repeat the above; anesthesia consultation
4. **>40 min (super-refractory SE)**: Midazolam or propofol infusion; ketamine (NMDA antagonist); phenobarbital; EEG monitoring

**Morbidity:** Each 10 minutes of convulsive SE increases neuronal injury; NCSE (nonconvulsive) can cause hippocampal atrophy with diagnostic delay.

### Diagnostic evaluation

**EEG:** Interictal discharges; ictal pattern; prolonged monitoring (video-EEG) for seizure capture; sleep deprivation activates discharges.

**MRI:** 3T MRI with thin-slice coronal FLAIR; MTLE shows hippocampal sclerosis; FCD appears as cortical thickening/blurring; tuberous sclerosis shows cortical tubers.

**Advanced evaluation (presurgical):**
- **FDG-PET**: Interictal hypometabolism identifies seizure focus even when MRI is negative
- **SPECT ictal/interictal subtraction (SISCOM)**: Captures hyperperfusion of ictal focus
- **SEEG (stereo-EEG)**: Invasive recording via depth electrodes for multi-lobar or deep foci
- **Wada test (IATC sodium amobarbital procedure)**: Determines dominant hemisphere for language before temporal surgery
- **fMRI language/memory lateralization**: Non-invasive Wada alternative

**Genetic testing:**
- Gene panel (50-100 epilepsy genes) for early-onset epileptic encephalopathy
- Whole exome sequencing for unexplained epilepsy in children
- **Dravet workup**: SCN1A sequencing (80% yield); if negative → PCDH19 (females), SCN1B, GABRG2
- Autoimmune workup: CSF + serum NMDAR, LGI1, CASPR2, AMPAR, GABA-B panels

### Treatment

**First-line antiepileptic drugs (AEDs):**

| Drug | Mechanism | Best for | Avoid in |
|:---|:---|:---|:---|
| **Valproate** | Na-channel, GABA-T inhibitor, T-Ca²⁺ | Broad-spectrum; generalized + focal | Pregnancy (teratogen); hepatic disease; do NOT stop abruptly |
| **Levetiracetam** | SV2A synaptic vesicle protein | Broad-spectrum; fewest interactions | Psychiatric side effects (irritability) |
| **Lamotrigine** | Na-channel (slow inactivation) | Focal + generalized; pregnancy-preferred; absence | Dravet syndrome (worsen); ramp slowly (Stevens-Johnson risk) |
| **Carbamazepine** | Na-channel | Focal epilepsy first-line; trigeminal neuralgia | Generalized/absence (worsen); HLA-B*1502 risk (Asian) → SJS |
| **Oxcarbazepine** | Na-channel | Focal; well-tolerated | Hyponatremia; Dravet |
| **Ethosuximide** | T-type Ca²⁺ channel | Absence ONLY; first-line absence | GTC (not effective) |
| **Topiramate** | Multiple (AMPA, Na, CA) | Focal; migraine prophylaxis; weight loss | Cognition ("dopamax"); renal stones |
| **Zonisamide** | Na-channel + T-Ca²⁺ | Focal + generalized; Parkinson's (adjunct) | Weight loss; renal stones |
| **Lacosamide** | Na-channel (slow inactivation) | Focal adjunct; IV available | Cardiac conduction (avoid with PR prolongation) |
| **Perampanel** | AMPA antagonist | Focal + GTC adjunct | Aggression/psychiatric; CYP450 interactions |

**Dravet-specific AEDs** (see SCN1A entry): valproate, clobazam, stiripentol, fenfluramine, cannabidiol.

**Drug-refractory epilepsy interventions:**

- **Temporal lobectomy**: For MTLE with hippocampal sclerosis; 65-70% seizure-free [^engel-2012-mtle-surgery]; memory risk on dominant side (assess with Wada/fMRI)
- **Focal cortical resection**: For FCD, tumor-related epilepsy, post-traumatic focal epilepsy
- **Corpus callosotomy**: For atonic/tonic drop attacks in Lennox-Gastaut; anterior 2/3 reduces falls without memory risk
- **VNS (vagus nerve stimulation)**: Left cervical vagus → nucleus tractus solitarius → cortical activation/inhibition; implanted stimulator; ~50% responder rate (≥50% seizure reduction); rescue magnetic stimulation available
- **RNS (responsive neurostimulation)**: Cortical-depth electrode array → closed-loop electrical stimulation on seizure detection; approved for drug-refractory focal epilepsy
- **Ketogenic diet (KD)**: High-fat (4:1 fat:carbohydrate+protein); starvation ketosis → ketone body metabolism → GABAergic mechanisms; most effective in: GLUT1 deficiency (first-line), PDH deficiency, Dravet syndrome; ~50% responder rate in drug-refractory childhood epilepsy
- **LITT (laser interstitial thermal therapy)**: MRI-guided laser ablation of hippocampus or seizure focus; minimally invasive alternative to open surgery; ~55% seizure-free for MTLE

## Connections

- `connects-to` → **[SCN1A](../../03-molecular/scn1a/README.md)** — SCN1A LOF mutations cause Dravet syndrome (most severe genetic epilepsy; Nav1.1 haploinsufficiency in GABAergic interneurons → cortical disinhibition → fever-sensitive seizures); SCN1A gain-of-function causes GEFS+; sodium channel blockers worsen Dravet; fenfluramine and cannabidiol are FDA-approved.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — cortical inhibitory balance maintained by GABAergic interneurons is the fundamental seizure brake; GABA-A receptor potentiators (benzodiazepines, phenobarbital, clobazam) and GABA-T inhibitors (valproate) are the most widely used antiepileptic drugs; GABA-A receptor subunit mutations (GABRG2, GABRA1) cause genetic generalized epilepsies.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — TSC1/TSC2 LOF → mTOR hyperactivation → cortical tubers → epilepsy in 80-90% of TSC patients; somatic PIK3CA/MTOR mutations cause focal cortical dysplasia IIb; mTOR inhibitor everolimus reduces TSC-associated seizures by ~50% (EXIST-3 trial); mTOR pathway is the major therapeutic target for structural genetic epilepsies.
- `targets` → **[Brain](../../06-organ/brain/README.md)** — epilepsy arises from focal or generalized cortical networks; hippocampal sclerosis in MTLE causes the most common adult focal epilepsy; EEG captures ictal/interictal cortical discharges; epilepsy surgery (temporal lobectomy) directly resects the epileptogenic zone.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — epilepsy risk is 2-3× elevated in AD; amyloid-driven cortical hyperexcitability precedes clinical dementia; anti-NMDAR and LGI1 autoimmune encephalitides present with epilepsy and cognitive decline, mimicking rapid-onset dementia and requiring different treatment.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Allopregnanolone (progesterone metabolite) is a potent GABA-A PAM via delta subunit extrasynaptic receptors → sedation, anxiolysis, anticonvulsant; progesterone withdrawal → allopregnanolone decline → GABA-A downregulation → seizure threshold reduction in catamenial epilepsy.
- `connects-to` → **[Migraine](../migraine/README.md)** — Epilepsy and migraine are comorbid disorders of cortical hyperexcitability that share genetics: gain-of-function SCN1A causes familial hemiplegic migraine while loss-of-function causes Dravet epilepsy, and valproate and topiramate treat both.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Seizures are an excitation-inhibition imbalance, and glutamate is the excitatory side: AMPA/NMDA over-activity drives synchronous bursting, and the AMPA antagonist perampanel is an antiseizure drug — the counterpart to GABA's brake.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — A seizure is hypersynchronous neuronal firing: bursting pyramidal neurons and recurrent excitatory collaterals overwhelm GABAergic interneurons → a paroxysmal depolarizing shift; most genetic epilepsies are neuronal ion-channelopathies that tip this balance.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Tuberous sclerosis is a paradigmatic genetic epilepsy: cortical tubers and TSC1/TSC2-driven mTOR overactivation cause early, often drug-resistant seizures (including infantile spasms), so mTOR inhibitors (everolimus) reduce seizures and early EEG-guided treatment is studied.
- `connects-to` → **[Stroke](../stroke/README.md)** — Stroke is a leading cause of acquired epilepsy in older adults: cortical infarcts and hemorrhages leave a gliotic, hyperexcitable scar that generates late-onset focal seizures months to years later; post-stroke epilepsy worsens outcomes and is managed with antiseizure medication.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes are active players in epilepsy, not bystanders: reactive astrogliosis impairs glutamate and potassium buffering and disrupts the blood-brain barrier, lowering seizure threshold; aberrant gap-junction coupling and inflammation sustain epileptogenesis.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — Epilepsy and autism frequently co-occur and share biology: up to a third of autistic people have epilepsy, and both arise from disrupted excitation/inhibition balance and overlap in genes like SCN, TSC, and SHANK—often the same neurodevelopmental lesion.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — Seizures are the commonest first sign of an IDH-mutant glioma: these slow-growing cortical tumors irritate neurons (partly via the oncometabolite 2-hydroxyglutarate altering glutamate), so new focal epilepsy in a young adult should prompt imaging for a low-grade glioma.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Epilepsy and depression have a bidirectional relationship: depression is the commonest psychiatric comorbidity of epilepsy and also raises the risk of developing it, shared limbic and serotonergic mechanisms link them, and depression strongly degrades quality of life.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — Brain tumors are an important cause of epilepsy: glioblastoma and other gliomas irritate surrounding cortex, so new-onset seizures in an adult mandate brain imaging—seizures are often the presenting sign of a glioma, and tumor-related epilepsy can be hard to control.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus is the seat of the commonest focal epilepsy: mesial temporal sclerosis—hippocampal scarring and neuron loss—generates temporal-lobe seizures, and surgically removing the sclerotic hippocampus can cure drug-resistant cases.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Epilepsy and schizophrenia are bidirectionally linked: temporal-lobe epilepsy can produce a schizophrenia-like psychosis, each roughly doubles the risk of the other, and they share disturbances of glutamate and GABA—so a first psychotic episode sometimes warrants EEG.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Voltage-gated sodium channels are epilepsy's central target: sodium influx fires the action potentials that, when runaway, become seizures, so many first-line drugs (phenytoin, lamotrigine) work by blocking these channels—and SCN1A mutations cause epilepsy.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Epilepsy is fundamentally a disorder of the synapse: seizures arise when synaptic excitation (glutamate) overwhelms inhibition (GABA), so the tipped excitation-inhibition balance at synapses is the common final pathway across epilepsy's many causes.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Epilepsy is a disorder of the whole nervous system's electrical stability: hypersynchronous neuronal discharges can start focally or generalize across networks, so seizures are a shared symptom of countless insults—from genetics to stroke, tumor and infection.

[^fisher-2017-ilae-classification]: Fisher RS, Cross JH, D'Souza C, et al. Instruction manual for the ILAE 2017 operational classification of seizure types. *Epilepsia.* 2017;58(4):531-542. [doi:10.1111/epi.13671](https://doi.org/10.1111/epi.13671) · [PubMed 28276060](https://pubmed.ncbi.nlm.nih.gov/28276060/)
[^devinsky-2018-epilepsy-review]: Devinsky O, Vezzani A, O'Brien TJ, et al. Epilepsy. *Nat Rev Dis Primers.* 2018;4:18024. [doi:10.1038/nrdp.2018.24](https://doi.org/10.1038/nrdp.2018.24) · [PubMed 29722352](https://pubmed.ncbi.nlm.nih.gov/29722352/)
[^engel-2012-mtle-surgery]: Engel J Jr, McDermott MP, Wiebe S, et al. Early surgical therapy for drug-resistant temporal lobe epilepsy: a randomized trial. *JAMA.* 2012;307(9):922-930. [doi:10.1001/jama.2012.220](https://doi.org/10.1001/jama.2012.220) · [PubMed 22396514](https://pubmed.ncbi.nlm.nih.gov/22396514/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
