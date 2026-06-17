---
schema: human-scale-entry/v1
id: autism-spectrum-disorder
name: Autism Spectrum Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "ASD (1-2% prevalence; 4:1 male bias) causes social communication deficits and restricted repetitive behaviors; E/I imbalance and synaptic scaffold mutations (SHANK3, NLGN3/4) are core mechanisms; ABA therapy is evidence-based; no pharmacotherapy is approved for core symptoms."
aliases: ["autism spectrum disorder", "ASD", "autism", "Asperger syndrome", "autistic disorder", "pervasive developmental disorder", "SHANK3", "NLGN3", "Fragile X", "Rett syndrome"]
sources:
  - id: maenner-2023-asd-prevalence
    type: peer-reviewed
    cite: "Maenner MJ, Warren Z, Williams AR, et al. Prevalence and characteristics of autism spectrum disorder among children aged 8 years — Autism and Developmental Disabilities Monitoring Network, 11 Sites, United States, 2020. MMWR Surveill Summ. 2023;72(2):1-14."
    doi: "10.15585/mmwr.ss7202a1"
    pmid: "36952216"
    url: "https://doi.org/10.15585/mmwr.ss7202a1"
    accessed: "2026-06-08"
  - id: lord-2020-asd-review
    type: peer-reviewed
    cite: "Lord C, Elsabbagh M, Baird G, Veenstra-Vanderweele J. Autism spectrum disorder. Lancet. 2018;392(10146):508-520."
    doi: "10.1016/S0140-6736(18)31129-2"
    pmid: "30078460"
    url: "https://doi.org/10.1016/S0140-6736(18)31129-2"
    accessed: "2026-06-08"
  - id: sanders-2012-asd-exome
    type: peer-reviewed
    cite: "Sanders SJ, Murtha MT, Gupta AR, et al. De novo mutations revealed by whole-exome sequencing are strongly associated with autism. Nature. 2012;485(7397):237-241."
    doi: "10.1038/nature10945"
    pmid: "22495306"
    url: "https://doi.org/10.1038/nature10945"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Oxytocin is reduced in subsets of ASD; OXTR methylation reduces receptor expression; intranasal OT modestly improves eye contact and social reciprocity in some RCTs; OT interventions remain experimental pending responder biomarker identification."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "E/I imbalance toward excess excitation is a core ASD mechanism; SHANK3 and NLGN3 mutations disrupt postsynaptic NMDA/AMPA scaffolding; mGluR5 hyperactivation in Fragile X drives excess dendritic protein synthesis; mGluR5 antagonists failed Phase 2 trials in FXS."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Reduced GABAergic inhibition contributes to E/I imbalance in ASD; GABA-A subunit mutations (GABRA1, GABRB3) are associated with ASD; GABA deficiency in ASD cortex may underlie sensory hypersensitivity; GABAergic circuit maturation delays are proposed as ASD endophenotype."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Syndromic ASD via mTOR hyperactivation: tuberous sclerosis (TSC1/2 LOF → mTORC1), PTEN hamartoma tumors (PTEN LOF); mTOR excess drives synaptic protein overproduction; everolimus reduces ASD severity and seizure burden in TSC; 25-35% of TSC patients have ASD."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "ASD features amygdala hyperreactivity to faces, atypical gaze via STS, reduced default mode network connectivity, and early cortical overgrowth followed by reduced long-range connectivity; atypical lateralization and local-over-global processing are consistent findings."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "AVPR1A promoter microsatellites (RS1, RS3) associate with ASD social behavior; V1aR in lateral septum mediates social recognition memory; V1aR-KO mice show impaired social memory; intranasal vasopressin is in Phase 2 trials for ASD social communication deficits."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Autism is in large part a disorder of the synapse: de novo mutations in scaffold proteins that organize the postsynaptic density tip neurons toward an excitation-inhibition imbalance, and ASD brains show early cortical neuron overgrowth then reduced long-range connectivity."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Autism and epilepsy frequently co-occur (roughly 20-30%), both reflecting cortical excitation-inhibition imbalance and often the same genes — SCN, GABA-receptor, and mTOR-pathway mutations cause both; shared E/I biology makes epilepsy one of ASD's key medical comorbidities."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Autism, bipolar disorder, and schizophrenia sit on an overlapping neurodevelopmental and genetic continuum: risk loci such as SHANK2 and the CACNA1C calcium channel are shared across all three, and bipolar disorder is a notable comorbidity in autistic people."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "Autism and ADHD are the most common neurodevelopmental comorbidity pair, co-occurring in 30-60%: they share heritability and executive-function and reward differences, DSM-5 now permits dual diagnosis, and ADHD inattention/impulsivity often complicate autistic presentations."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Tuberous sclerosis is a leading single-gene cause of syndromic autism: loss of TSC1/TSC2 disinhibits mTOR, producing cortical tubers, epilepsy and autism in up to half of patients; this links autism to the mTOR synaptic pathway and motivates mTOR-inhibitor trials."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Autism is increasingly understood as a synaptopathy: many risk genes (SHANK, neurexin/neuroligin, mTOR regulators) converge on synapse formation, pruning and the excitation/inhibition balance, so altered synaptic signaling underlies the social and sensory phenotype."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Autism and schizophrenia share neurodevelopmental origins and genetics: overlapping copy-number variants (22q11, 16p11) and synaptic genes underlie both, on a continuum of early brain miswiring—though autism presents in childhood and schizophrenia in late adolescence."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Autism and OCD share repetitive behavior but differ in drive: autistic repetitive behaviors are self-soothing and not unwanted, while OCD compulsions relieve ego-dystonic obsessions—yet the two co-occur, so telling comforting routine from distressing ritual guides care."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia are implicated in autism's altered brain wiring: as the synaptic pruners of development, dysregulated microglia may leave excess or aberrant synapses, and signs of neuroinflammation in autistic brains point to immune-neural crosstalk in early circuit formation."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Autism is linked to the gut-brain axis: many autistic people have GI symptoms and altered gut microbiomes, and microbial metabolites may influence behavior and neurodevelopment—an area of intense (if still unproven) research into diet and microbiome interventions."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes contribute to autism's altered brain wiring: beyond neurons, dysfunctional astrocytes disturb synapse formation, glutamate handling and neuroinflammation, supporting a view of autism as a disorder of brain connectivity."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Autism and anxiety disorders very frequently co-occur: a large share of autistic people have generalized anxiety, which intensifies sensory sensitivities and rigidity—so screening for and treating anxiety is central to autism care."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Elevated blood serotonin is autism's oldest biomarker: about a quarter of children with autism have platelet hyperserotonemia, and serotonin's role in early brain wiring links this neurotransmitter to the disorder's developmental origins, though its meaning stays unclear."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine circuits are implicated in autism's core features: altered mesolimbic dopamine signaling may underlie differences in social motivation and repetitive behaviors, and dopamine-blocking antipsychotics are the main drugs approved for autism-associated irritability."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Autism is a neurodevelopmental condition of the whole nervous system: altered synapse formation and excitation-inhibition balance during early brain development shape lifelong differences in perception, communication and behavior across many brain networks."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune system is woven into autism's origins: maternal infection and immune activation in pregnancy raise risk, and many autistic children show ongoing neuroinflammation with activated microglia—so immune signaling shapes the developing social brain."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF ties autism to synaptic wiring: this neurotrophin guides how synapses form and prune, and altered BDNF levels are reported in autism, fitting a model where mis-tuned synaptic growth—too many or too few connections—underlies the atypical brain development."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus is altered in autism: differences in its size and connectivity accompany the memory and spatial-learning quirks seen in the condition, and as a region of lifelong neurogenesis it links autism to how experience reshapes the developing brain."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Prenatal testosterone may bias autism risk: elevated fetal androgen exposure is one proposed factor behind the ~4:1 male predominance and the 'extreme male brain' theory, linking sex hormones in the womb to later neurodevelopment."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "The placenta is a route to autism risk: maternal immune activation, infection and exposures (like valproate) acting through the placenta during pregnancy raise ASD likelihood, pointing to a prenatal origin for much of the condition."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc helps build the synapses disrupted in autism: SHANK scaffold proteins—mutated in some autism—are zinc-dependent, and zinc concentrates at synapses, so disturbed zinc signaling is one link between trace-metal biology and synaptic ASD genes."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Autism reshapes the brain's wiring insulation: studies find altered myelin and oligodendrocyte differences underlying the atypical long- and short-range connectivity, so white-matter changes accompany the synaptic biology of ASD."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Maternal IL-6 links infection to autism risk: when the mother's immune system activates in pregnancy, IL-6 crossing to the fetal brain perturbs development in animal models, a leading mechanism behind the maternal-immune-activation hypothesis of ASD."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium tunes the glutamate signaling disturbed in autism: it blocks the NMDA receptor at rest, so altered magnesium handling can shift the excitation-inhibition balance that many ASD genes already push toward over-excitation."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Autism converges on calcium signaling: several of the strongest risk genes encode calcium channels (like CACNA1C) or calcium-handling proteins, so altered calcium flow into neurons is a recurring thread through the disorder's genetics."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Autism reaches into the gut: GI symptoms are far more common in ASD, and through the gut-brain axis the large intestine's microbes and signals can influence behavior, tying digestive health to the condition."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Autism often runs short on ATP: a subset of children show mitochondrial dysfunction that limits the cell's energy currency, and the brain's high energy demand may make developing neurons especially sensitive to this shortfall."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Brain imaging probes autism: MRI shows early brain overgrowth and altered connectivity, and fMRI photons map how differently social and sensory networks light up, sought as objective markers."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency is common in autism: restrictive eating lowers stores, and because iron is needed to make dopamine, low iron may worsen attention, sleep and restless behaviors."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Autism shows in the eyes: reduced eye contact and atypical gaze are early signs, and eye-tracking is studied as an objective measure of the social differences that define the condition."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy hints at autism's altered wiring: studies find changes in dendritic spine density and synapse structure, the fine connections between neurons that mTOR and other autism genes help build and prune."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D in pregnancy may shape the risk: low maternal vitamin D during fetal brain development is associated with a higher chance of autism, fitting the vitamin's role in neurodevelopment and immune regulation."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Autism and the heart often travel together: children with congenital heart disease have elevated rates of autism, the shared early developmental disruption and surgical-stress exposure linking the two conditions."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Sleep is a near-universal struggle in autism: disrupted melatonin rhythms leave many autistic children unable to fall or stay asleep, and melatonin is the first-line treatment, easing both the insomnia and the daytime behavior it worsens."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The gut is a frequent trouble spot: autistic children have high rates of reflux, constipation, and selective eating, the GI symptoms feeding into the gut-brain axis already implicated in the condition."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The mother's thyroid shapes the risk: adequate maternal thyroid hormone is critical for fetal brain development, and maternal hypothyroxinemia in pregnancy is a recognized risk factor for autism in the child."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "A mother's antibodies can target the fetal brain: in maternal-autoantibody-related autism, IgG against fetal brain proteins crosses the placenta and disturbs neurodevelopment, one immune route into the condition's many causes."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune genes sit among the risk loci: MHC/HLA variants and maternal immune activation in pregnancy are tied to autism, linking the brain's wiring to the same antigen-presenting machinery that runs immunity."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Much of the risk is set before birth: advanced parental age, prenatal valproate, and maternal immune activation shape autism risk, and the striking male predominance points to sex-hormone influences on the developing brain."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Maternal IL-17A is a molecular bridge from infection to autism: in maternal immune activation models, this Th17 cytokine crosses into the fetal brain and alters cortical development, producing autism-like behavior in the offspring."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Brain mast cells may stoke the neuroinflammation: they sit near the blood-brain barrier and release mediators that activate microglia, and the high rate of allergy and mast-cell activation in autism hints at a role in some cases."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "A single-gene road to autism: neurofibromatosis type 1 carries a high rate of autism features, one of the RAS-MAPK 'RASopathies' that, like tuberous sclerosis, show how one mutation can derail the social brain."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The body's cannabis system tunes the social brain: endocannabinoid signaling shapes the synaptic plasticity and reward responses to social cues, and its dysregulation in autism is the rationale behind cannabidiol trials for the condition."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "An immune imbalance shadows it: reduced regulatory T cells and a tilt toward inflammation accompany autism, fitting the maternal-immune-activation models in which prenatal inflammation reshapes brain development."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep rarely comes easy: insomnia and disrupted sleep architecture are strikingly common in autism, tied to altered melatonin rhythms, and poor sleep in turn worsens daytime behavior and core symptoms."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Neuroinflammation runs through NF-κB: maternal immune activation and microglial activation in autism converge on NF-κB-driven cytokine signaling, part of the inflammatory thread woven through its neurodevelopment."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "One gene ties autism to overgrowth: PTEN mutations cause a macrocephaly-autism syndrome, and because PTEN restrains the mTOR pathway, its loss drives the synaptic overgrowth linking this monogenic cause to the broader spectrum."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The gut speaks loudly in autism: constipation, diarrhea and abdominal pain are far more common than in peers, a GI burden tied to the gut-brain axis and to the altered microbiome that accompanies the condition."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Social difficulty breeds social fear: social anxiety is among the most common comorbidities in autism, as repeated misread interactions and rejection foster intense anticipatory fear of social situations."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Isolation and burnout darken mood: depression is markedly elevated in autistic people, driven by loneliness, the exhaustion of masking, and the cumulative toll of navigating an unaccommodating world."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Several forces tip toward weight gain: restricted food preferences, reduced physical activity, and the appetite-stimulating antipsychotics often prescribed in autism combine to raise the rate of obesity."
---

# Autism Spectrum Disorder

## Overview

**Autism spectrum disorder (ASD)** is a neurodevelopmental condition characterized by deficits in **social communication and interaction** combined with **restricted, repetitive behaviors and sensory differences**, with symptoms present from early childhood. ASD is not a single disease but a spectrum of heterogeneous conditions sharing these core features — ranging from individuals with profound intellectual disability and minimal speech to those with high cognitive ability and typical language (previously termed "Asperger syndrome" in DSM-IV; now unified under ASD in DSM-5).

ASD affects approximately **1 in 44 children** in the US (2020 CDC data) — about 2% of the population [^maenner-2023-asd-prevalence] — making it one of the most prevalent neurodevelopmental conditions. The **4:1 male predominance** is genuine but the female "camouflage" phenomenon (better social masking) contributes to under-diagnosis in girls; true sex ratio may be closer to 3:1. Sibling recurrence risk is 10–20×, and monozygotic twin concordance is ~70–90%, confirming strong heritability.

The dramatic rise in ASD prevalence from ~0.05% in the 1970s to ~2% today primarily reflects **expanded diagnostic criteria** (DSM-III → DSM-5 broadening), greater awareness, and diagnostic substitution (children previously labeled with intellectual disability or language delay). True biological incidence increase may also contribute to a modest degree (advanced paternal age, prenatal environmental factors).

## Structure

### DSM-5 criteria

**Criterion A — Persistent deficits in social communication and social interaction** across multiple contexts (all three required):
1. Deficits in social-emotional reciprocity (reduced social initiation, failure to respond to social bids, absent back-and-forth conversation)
2. Deficits in nonverbal communicative behaviors (poor eye contact, reduced facial expression, atypical gesturing, absent joint attention)
3. Deficits in developing, maintaining, and understanding relationships (difficulty with make-believe play, preference for rules over flexible social interaction, absent interest in peers)

**Criterion B — Restricted, repetitive behaviors** (≥2 of 4):
1. Stereotyped/repetitive motor movements, use of objects, or speech (echolalia, hand flapping, lining up objects)
2. Insistence on sameness, inflexible adherence to routines, ritualized patterns
3. Restricted, fixated interests that are abnormal in intensity or focus
4. Hyper- or hyporeactivity to sensory input (indifference to pain/temperature, adverse response to specific sounds/textures, visual fascination)

**Severity levels (1–3):** Based on amount of support required for social communication and restricted/repetitive behaviors; Level 3 ("requiring very substantial support") is most severe.

**Specifiers:** With/without intellectual impairment; with/without language impairment; associated with genetic/medical condition; associated with catatonia.

### Syndromic vs. idiopathic ASD

**Syndromic ASD** (~25% of cases): ASD features secondary to a known genetic disorder:

| Syndrome | Gene/Locus | Mechanism | ASD Prevalence |
|:---|:---|:---|:---|
| **Fragile X syndrome** | FMR1 (CGG triplet repeat expansion, >200 repeats → methylation → silencing) | Loss of FMRP → excess mGluR5-driven dendritic protein synthesis | 30% of FXS males |
| **Tuberous sclerosis complex (TSC)** | TSC1/TSC2 LOF → mTORC1 hyperactivation | Cortical tubers, heterotopia; synaptic protein excess | 25–50% of TSC |
| **Rett syndrome** | MECP2 LOF (X-linked, almost exclusively females) | Impaired neuronal gene silencing; progressive neurodegeneration | ~75% of Rett |
| **Angelman syndrome** | UBE3A loss (maternal 15q11-q13 imprinting) | Reduced ubiquitin E3 ligase → synaptic protein accumulation | ~50% of AS |
| **PTEN hamartoma** | PTEN LOF → mTOR hyperactivation | Macrocephaly, intellectual disability | ~20% of macrocephalic ASD |
| **22q11.2 deletion** | TBX1, DGCR8, others | Haploinsufficiency of multiple neurodevelopmental genes | ~50% of 22q11.2DS |

**Idiopathic ASD** (~75%): Complex genetic architecture:
- Heritability: ~70–90% (twin studies); polygenic risk from hundreds of common variants + rare de novo mutations
- **De novo mutations**: Among the strongest ASD risk factors; detected in ~10–15% of sporadic ASD vs. <1% of controls [^sanders-2012-asd-exome]; enriched in genes encoding synaptic proteins
- Key ASD gene categories: **Synaptic scaffold proteins** (SHANK1/2/3, NRXN1, NLGN3/4X), **chromatin regulators** (CHD8 — most commonly mutated ASD gene; ARID1B; KDM5C), **RNA processing** (FMR1, CNTNAP2), **mTOR pathway** (TSC1/2, PTEN)
- Major CNVs: 16p11.2 deletion (most common ASD CNV; also found in schizophrenia); 15q11-q13 duplication; 1q21.1 deletion/duplication

### Neurobiology of ASD

**Excitation-inhibition (E/I) imbalance hypothesis:**
The dominant neurobiological framework proposes that ASD reflects excess cortical excitation relative to inhibition — or, in some cases, altered E/I balance in specific circuits:
- SHANK3, NLGN3, NRXN1 mutations → impaired postsynaptic density organization → reduced NMDA receptor clustering → compensatory AMPA receptor upregulation → E/I shift
- Parvalbumin (PV) interneuron deficits observed in postmortem ASD cortex → reduced GABAergic inhibitory tone → sensory hypersensitivity
- However, the direction of E/I imbalance is circuit-specific: some circuits show hyperexcitability; others (especially PFC) may show hypoexcitability

**Synaptic scaffold proteins:**
- **SHANK proteins** (SHANK1/2/3) are master scaffolds at the postsynaptic density (PSD), anchoring NMDA receptors, AMPA receptors, mGluRs, and Homer proteins. SHANK3 haploinsufficiency causes ASD with severe social deficits in mice and humans (Phelan-McDermid syndrome — 22q13.3 deletion)
- **Neuroligins** (NLGN3/4X): trans-synaptic adhesion molecules that organize the PSD by binding presynaptic neurexins. NLGN3 R451C knock-in mice show enhanced inhibitory transmission (paradoxical) + social deficits. NLGN4X LOF associated with ASD + intellectual disability
- **Neurexins** (NRXN1–3): presynaptic organizers that match NLGN across the synaptic cleft; deletions are among the highest-penetrance ASD CNVs

**Cortical development:**
- ASD brains show **cortical overgrowth** at 12–24 months (expanded total brain volume, especially frontal lobe) followed by **reduced long-range white matter connectivity** in adolescence
- Transient cortical overgrowth: driven by excess early neurogenesis (Marchetto 2017; organoid models show ASD iPSC-derived cortical organoids produce excess neurons via premature cell cycle exit)
- **Local-over-global processing** bias: ASD cognition shows superior detection of local features (Embedded Figures Test, block design) with reduced global gestalt processing — consistent with restricted local cortical connectivity

## Function

### Social brain network in ASD

The neural basis of ASD social deficits involves dysfunction of the **social brain network**:

| Region | Function in neurotypicals | ASD alteration |
|:---|:---|:---|
| **Amygdala** | Encodes social salience; gaze direction; emotional facial expression | Hyperreactive to faces; rapid habituation failure; inverse correlation with clinical severity |
| **Superior temporal sulcus (STS)** | Biological motion; voice recognition; joint attention | Reduced activation to social stimuli; atypical functional connectivity with amygdala |
| **Fusiform face area (FFA)** | Expert face recognition | Hypoactivation in ASD; atypical processing of eyes |
| **Inferior frontal gyrus / Broca's area** | Mirror neuron system; language; imitation | Reduced activation during observation of intentional actions |
| **mPFC / vmPFC** | Theory of Mind; mentalizing; social reward | Reduced activation during false belief tasks; impaired mentalizing network |
| **Anterior insula** | Interoception; social pain; empathy | Atypical activation; altered interoceptive awareness |

**Default mode network (DMN) in ASD:** Neurotypical brains show DMN suppression during attention-demanding tasks. ASD shows reduced task-induced DMN suppression AND reduced resting-state connectivity within the DMN — reflected in disrupted self-referential processing and mentalizing.

**Theory of Mind:** The capacity to attribute mental states to others ("mentalizing") is consistently reduced in ASD across ToM tasks (Sally-Anne false belief, Faux Pas test, Reading the Mind in the Eyes). The neural substrate is the mentalizing network (mPFC, TPJ, posterior STS), which shows reduced activation in ASD during implicit social inference tasks.

## Pathology

### Risk factors and diagnosis

**Prenatal/postnatal risk factors:**
- Advanced paternal age (>40 years) — de novo mutation rate increases 2-fold
- Advanced maternal age (>35) — independent of paternal age
- Prenatal exposure to valproate (ASD risk 10–15× in offspring of mothers treated for epilepsy in pregnancy)
- Preterm birth (<26 weeks): ~20-fold elevated ASD risk
- Maternal immune activation during pregnancy (gestational inflammation) — maternal cytokines cross placenta; preclinical evidence strong, human epidemiology mixed
- NO convincing evidence for childhood vaccination (MMR) — multiple large RCTs and cohort studies have comprehensively excluded this hypothesis

**Diagnostic tools:**
- **ADOS-2** (Autism Diagnostic Observation Schedule, 2nd edition): gold-standard observational assessment; standardized activities that elicit social, communicative, and play behaviors
- **ADI-R** (Autism Diagnostic Interview-Revised): caregiver interview covering early development and current symptoms
- **CARS-2** and **Childhood Autism Rating Scale** for dimensional severity rating
- First symptoms typically apparent before age 3; median age of diagnosis in US is ~4 years (later in girls and less affected individuals)

### Treatment and management

**Behavioral/educational interventions:**
- **Applied Behavior Analysis (ABA)**: Most evidence-based intervention; intensive (20–40 h/week) behavioral modification using positive reinforcement; greatest gains in adaptive behavior, language, and cognition when started early (before age 5); Level 1 evidence for improving functional outcomes
- **Speech-language therapy**: Augmentative and alternative communication (AAC) for minimally verbal individuals; social pragmatics training for verbal ASD
- **Occupational therapy**: Sensory integration; fine motor skills; activities of daily living
- **Social skills groups**: Evidence-based for adolescents/adults with higher-functioning ASD; PEERS program (Program for the Education and Enrichment of Relational Skills) has robust RCT evidence
- **Pivotal Response Treatment (PRT)**: Naturalistic ABA-based approach; targets "pivotal" behaviors (motivation, initiation) that have broad developmental impact

**Pharmacotherapy (note: no drug approved for ASD's core social/communication symptoms):**

| Drug | Target | Indication in ASD | Evidence |
|:---|:---|:---|:---|
| Risperidone | D2/5-HT2A antagonist | Irritability, aggression, self-injurious behavior | FDA-approved (6–17 years) |
| Aripiprazole | D2 partial agonist | Irritability | FDA-approved (6–17 years) |
| SSRIs (fluoxetine, sertraline) | SERT inhibitor | Repetitive behaviors, anxiety, OCD features | Mixed evidence; generally modest benefit |
| Melatonin | MT1/MT2 agonist | Sleep disturbances (common in 50–80% of ASD) | Consistent evidence for sleep onset |
| Oxytocin (intranasal) | OTR agonist | Social communication | Phase 2 evidence mixed; not FDA-approved |
| Everolimus | mTORC1 inhibitor | Seizures + ASD in TSC | Reduces TSC seizures; modest ASD effects |
| Bumetanide | NKCC1 blocker (chloride co-transporter) | E/I balance correction (GABA depolarizing → hyperpolarizing shift) | Phase 2 evidence; not approved; EU phase 3 failed 2021 |

**Emerging/research therapies:**
- **CRISPR correction** of SHANK3 mutations in iPSC-derived neurons (preclinical)
- **Gene therapy for Rett syndrome:** MECP2 gene replacement via AAV9 (Phase 1/2 REVEAL trial: significant improvement in Rett symptoms)
- **mGluR5 modulators:** Arbaclofen (GABA-B agonist) for social deficit in Fragile X — failed Phase 3 but responders with certain genotypes identified
- **IGF-1 (mecasermin)** for Phelan-McDermid (SHANK3 deletion): Phase 2 showed improved socialization and expressive language; Phase 3 ongoing

## Connections

- `connects-to` → **[Oxytocin](../../../03-molecular/oxytocin/README.md)** — oxytocin is reduced in subsets of ASD; OXTR methylation reduces receptor expression; intranasal OT modestly improves eye contact and social reciprocity in some RCTs; OT interventions remain experimental pending responder biomarker identification (OXTR genotype, baseline OT level).

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — E/I imbalance toward excess excitation is a core ASD mechanism; SHANK3 and NLGN3 mutations disrupt postsynaptic NMDA/AMPA scaffolding; mGluR5 hyperactivation in Fragile X syndrome drives excess dendritic protein synthesis; mGluR5 antagonists failed Phase 2 trials in FXS.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — reduced GABAergic inhibition contributes to cortical E/I imbalance in ASD; GABA-A subunit mutations (GABRA1, GABRB3) are associated with ASD; PV interneuron deficits in ASD cortex reduce GABAergic tone and contribute to sensory hypersensitivity.

- `connects-to` → **[mTOR](../../../03-molecular/mtor/README.md)** — syndromic ASD via mTOR hyperactivation: tuberous sclerosis (TSC1/2 LOF), PTEN hamartoma (PTEN LOF); excess mTOR drives synaptic protein overproduction; everolimus reduces ASD severity and seizure burden in TSC patients.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — ASD features amygdala hyperreactivity to faces, atypical gaze processing via STS, reduced DMN connectivity, early cortical overgrowth followed by reduced long-range white matter connectivity, and consistent local-over-global processing bias.
- `connects-to` → **[Vasopressin](../../../03-molecular/vasopressin/README.md)** — AVPR1A promoter microsatellites (RS1, RS3) associate with ASD social behavior; V1aR in lateral septum mediates social recognition memory; V1aR-KO mice show impaired social memory; intranasal vasopressin is in Phase 2 trials for ASD social communication deficits.

- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Autism is in large part a disorder of the synapse: de novo mutations in scaffold proteins that organize the postsynaptic density tip neurons toward an excitation-inhibition imbalance, and ASD brains show early cortical neuron overgrowth then reduced long-range connectivity.

- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Autism and epilepsy frequently co-occur (roughly 20-30%), both reflecting cortical excitation-inhibition imbalance and often the same genes — SCN, GABA-receptor, and mTOR-pathway mutations cause both; shared E/I biology makes epilepsy one of ASD's key medical comorbidities.

- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Autism, bipolar disorder, and schizophrenia sit on an overlapping neurodevelopmental and genetic continuum: risk loci such as SHANK2 and the CACNA1C calcium channel are shared across all three, and bipolar disorder is a notable comorbidity in autistic people.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — Autism and ADHD are the most common neurodevelopmental comorbidity pair, co-occurring in 30-60%: they share heritability and executive-function and reward differences, DSM-5 now permits dual diagnosis, and ADHD inattention/impulsivity often complicate autistic presentations.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Tuberous sclerosis is a leading single-gene cause of syndromic autism: loss of TSC1/TSC2 disinhibits mTOR, producing cortical tubers, epilepsy and autism in up to half of patients; this links autism to the mTOR synaptic pathway and motivates mTOR-inhibitor trials.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Autism is increasingly understood as a synaptopathy: many risk genes (SHANK, neurexin/neuroligin, mTOR regulators) converge on synapse formation, pruning and the excitation/inhibition balance, so altered synaptic signaling underlies the social and sensory phenotype.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Autism and schizophrenia share neurodevelopmental origins and genetics: overlapping copy-number variants (22q11, 16p11) and synaptic genes underlie both, on a continuum of early brain miswiring—though autism presents in childhood and schizophrenia in late adolescence.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Autism and OCD share repetitive behavior but differ in drive: autistic repetitive behaviors are self-soothing and not unwanted, while OCD compulsions relieve ego-dystonic obsessions—yet the two co-occur, so telling comforting routine from distressing ritual guides care.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia are implicated in autism's altered brain wiring: as the synaptic pruners of development, dysregulated microglia may leave excess or aberrant synapses, and signs of neuroinflammation in autistic brains point to immune-neural crosstalk in early circuit formation.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Autism is linked to the gut-brain axis: many autistic people have GI symptoms and altered gut microbiomes, and microbial metabolites may influence behavior and neurodevelopment—an area of intense (if still unproven) research into diet and microbiome interventions.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes contribute to autism's altered brain wiring: beyond neurons, dysfunctional astrocytes disturb synapse formation, glutamate handling and neuroinflammation, supporting a view of autism as a disorder of brain connectivity.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Autism and anxiety disorders very frequently co-occur: a large share of autistic people have generalized anxiety, which intensifies sensory sensitivities and rigidity—so screening for and treating anxiety is central to autism care.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Elevated blood serotonin is autism's oldest biomarker: about a quarter of children with autism have platelet hyperserotonemia, and serotonin's role in early brain wiring links this neurotransmitter to the disorder's developmental origins, though its meaning stays unclear.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine circuits are implicated in autism's core features: altered mesolimbic dopamine signaling may underlie differences in social motivation and repetitive behaviors, and dopamine-blocking antipsychotics are the main drugs approved for autism-associated irritability.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Autism is a neurodevelopmental condition of the whole nervous system: altered synapse formation and excitation-inhibition balance during early brain development shape lifelong differences in perception, communication and behavior across many brain networks.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune system is woven into autism's origins: maternal infection and immune activation in pregnancy raise risk, and many autistic children show ongoing neuroinflammation with activated microglia—so immune signaling shapes the developing social brain.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF ties autism to synaptic wiring: this neurotrophin guides how synapses form and prune, and altered BDNF levels are reported in autism, fitting a model where mis-tuned synaptic growth—too many or too few connections—underlies the atypical brain development.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus is altered in autism: differences in its size and connectivity accompany the memory and spatial-learning quirks seen in the condition, and as a region of lifelong neurogenesis it links autism to how experience reshapes the developing brain.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Prenatal testosterone may bias autism risk: elevated fetal androgen exposure is one proposed factor behind the ~4:1 male predominance and the 'extreme male brain' theory, linking sex hormones in the womb to later neurodevelopment.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — The placenta is a route to autism risk: maternal immune activation, infection and exposures (like valproate) acting through the placenta during pregnancy raise ASD likelihood, pointing to a prenatal origin for much of the condition.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc helps build the synapses disrupted in autism: SHANK scaffold proteins—mutated in some autism—are zinc-dependent, and zinc concentrates at synapses, so disturbed zinc signaling is one link between trace-metal biology and synaptic ASD genes.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Autism reshapes the brain's wiring insulation: studies find altered myelin and oligodendrocyte differences underlying the atypical long- and short-range connectivity, so white-matter changes accompany the synaptic biology of ASD.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Maternal IL-6 links infection to autism risk: when the mother's immune system activates in pregnancy, IL-6 crossing to the fetal brain perturbs development in animal models, a leading mechanism behind the maternal-immune-activation hypothesis of ASD.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium tunes the glutamate signaling disturbed in autism: it blocks the NMDA receptor at rest, so altered magnesium handling can shift the excitation-inhibition balance that many ASD genes already push toward over-excitation.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Autism converges on calcium signaling: several of the strongest risk genes encode calcium channels (like CACNA1C) or calcium-handling proteins, so altered calcium flow into neurons is a recurring thread through the disorder's genetics.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Autism reaches into the gut: GI symptoms are far more common in ASD, and through the gut-brain axis the large intestine's microbes and signals can influence behavior, tying digestive health to the condition.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Autism often runs short on ATP: a subset of children show mitochondrial dysfunction that limits the cell's energy currency, and the brain's high energy demand may make developing neurons especially sensitive to this shortfall.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Brain imaging probes autism: MRI shows early brain overgrowth and altered connectivity, and fMRI photons map how differently social and sensory networks light up, sought as objective markers.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency is common in autism: restrictive eating lowers stores, and because iron is needed to make dopamine, low iron may worsen attention, sleep and restless behaviors.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Autism shows in the eyes: reduced eye contact and atypical gaze are early signs, and eye-tracking is studied as an objective measure of the social differences that define the condition.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy hints at autism's altered wiring: studies find changes in dendritic spine density and synapse structure, the fine connections between neurons that mTOR and other autism genes help build and prune.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D in pregnancy may shape the risk: low maternal vitamin D during fetal brain development is associated with a higher chance of autism, fitting the vitamin's role in neurodevelopment and immune regulation.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Autism and the heart often travel together: children with congenital heart disease have elevated rates of autism, the shared early developmental disruption and surgical-stress exposure linking the two conditions.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Sleep is a near-universal struggle in autism: disrupted melatonin rhythms leave many autistic children unable to fall or stay asleep, and melatonin is the first-line treatment, easing both the insomnia and the daytime behavior it worsens.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The gut is a frequent trouble spot: autistic children have high rates of reflux, constipation, and selective eating, the GI symptoms feeding into the gut-brain axis already implicated in the condition.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The mother's thyroid shapes the risk: adequate maternal thyroid hormone is critical for fetal brain development, and maternal hypothyroxinemia in pregnancy is a recognized risk factor for autism in the child.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — A mother's antibodies can target the fetal brain: in maternal-autoantibody-related autism, IgG against fetal brain proteins crosses the placenta and disturbs neurodevelopment, one immune route into the condition's many causes.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Immune genes sit among the risk loci: MHC/HLA variants and maternal immune activation in pregnancy are tied to autism, linking the brain's wiring to the same antigen-presenting machinery that runs immunity.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Much of the risk is set before birth: advanced parental age, prenatal valproate, and maternal immune activation shape autism risk, and the striking male predominance points to sex-hormone influences on the developing brain.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Maternal IL-17A is a molecular bridge from infection to autism: in maternal immune activation models, this Th17 cytokine crosses into the fetal brain and alters cortical development, producing autism-like behavior in the offspring.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Brain mast cells may stoke the neuroinflammation: they sit near the blood-brain barrier and release mediators that activate microglia, and the high rate of allergy and mast-cell activation in autism hints at a role in some cases.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — A single-gene road to autism: neurofibromatosis type 1 carries a high rate of autism features, one of the RAS-MAPK 'RASopathies' that, like tuberous sclerosis, show how one mutation can derail the social brain.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The body's cannabis system tunes the social brain: endocannabinoid signaling shapes the synaptic plasticity and reward responses to social cues, and its dysregulation in autism is the rationale behind cannabidiol trials for the condition.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — An immune imbalance shadows it: reduced regulatory T cells and a tilt toward inflammation accompany autism, fitting the maternal-immune-activation models in which prenatal inflammation reshapes brain development.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep rarely comes easy: insomnia and disrupted sleep architecture are strikingly common in autism, tied to altered melatonin rhythms, and poor sleep in turn worsens daytime behavior and core symptoms.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Neuroinflammation runs through NF-κB: maternal immune activation and microglial activation in autism converge on NF-κB-driven cytokine signaling, part of the inflammatory thread woven through its neurodevelopment.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — One gene ties autism to overgrowth: PTEN mutations cause a macrocephaly-autism syndrome, and because PTEN restrains the mTOR pathway, its loss drives the synaptic overgrowth linking this monogenic cause to the broader spectrum.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The gut speaks loudly in autism: constipation, diarrhea and abdominal pain are far more common than in peers, a GI burden tied to the gut-brain axis and to the altered microbiome that accompanies the condition.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — Social difficulty breeds social fear: social anxiety is among the most common comorbidities in autism, as repeated misread interactions and rejection foster intense anticipatory fear of social situations.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Isolation and burnout darken mood: depression is markedly elevated in autistic people, driven by loneliness, the exhaustion of masking, and the cumulative toll of navigating an unaccommodating world.
- `connects-to` → **[Obesity](../obesity/README.md)** — Several forces tip toward weight gain: restricted food preferences, reduced physical activity, and the appetite-stimulating antipsychotics often prescribed in autism combine to raise the rate of obesity.

[^maenner-2023-asd-prevalence]: Maenner MJ, Warren Z, Williams AR, et al. Prevalence and characteristics of autism spectrum disorder among children aged 8 years — ADDM Network, 2020. *MMWR Surveill Summ.* 2023;72(2):1-14. [doi:10.15585/mmwr.ss7202a1](https://doi.org/10.15585/mmwr.ss7202a1) · [PubMed 36952216](https://pubmed.ncbi.nlm.nih.gov/36952216/)
[^lord-2020-asd-review]: Lord C, Elsabbagh M, Baird G, Veenstra-Vanderweele J. Autism spectrum disorder. *Lancet.* 2018;392(10146):508-520. [doi:10.1016/S0140-6736(18)31129-2](https://doi.org/10.1016/S0140-6736(18)31129-2) · [PubMed 30078460](https://pubmed.ncbi.nlm.nih.gov/30078460/)
[^sanders-2012-asd-exome]: Sanders SJ, Murtha MT, Gupta AR, et al. De novo mutations revealed by whole-exome sequencing are strongly associated with autism. *Nature.* 2012;485(7397):237-241. [doi:10.1038/nature10945](https://doi.org/10.1038/nature10945) · [PubMed 22495306](https://pubmed.ncbi.nlm.nih.gov/22495306/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
