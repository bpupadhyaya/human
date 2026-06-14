---
schema: human-scale-entry/v1
id: schizophrenia
name: Schizophrenia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Schizophrenia (1% lifetime risk) is a severe psychotic disorder with positive symptoms (hallucinations, delusions), negative symptoms (avolition, flat affect), and cognitive deficits; mesolimbic dopamine D2 hyperactivity drives psychosis; all antipsychotics block D2 receptors."
aliases: ["schizophrenia", "psychosis", "positive symptoms", "negative symptoms", "dopamine hypothesis", "NMDA hypofunction", "antipsychotic", "clozapine", "haloperidol", "schizophrenia spectrum"]
sources:
  - id: howes-2009-dopamine-hypothesis
    type: peer-reviewed
    cite: "Howes OD, Kapur S. The dopamine hypothesis of schizophrenia: version III—the final common pathway. Schizophr Bull. 2009;35(3):549-562."
    doi: "10.1093/schbul/sbp006"
    pmid: "19325164"
    url: "https://doi.org/10.1093/schbul/sbp006"
    accessed: "2026-06-08"
  - id: moghaddam-2012-glutamate
    type: peer-reviewed
    cite: "Moghaddam B, Javitt D. From revolution to evolution: the glutamate hypothesis of schizophrenia and its implication for treatment. Neuropsychopharmacology. 2012;37(1):4-15."
    doi: "10.1038/npp.2011.181"
    pmid: "21956446"
    url: "https://doi.org/10.1038/npp.2011.181"
    accessed: "2026-06-08"
  - id: leucht-2013-antipsychotics-meta
    type: peer-reviewed
    cite: "Leucht S, Cipriani A, Spineli L, et al. Comparative efficacy and tolerability of 15 antipsychotic drugs in schizophrenia: a multiple-treatments meta-analysis. Lancet. 2013;382(9896):951-962."
    doi: "10.1016/S0140-6736(13)60733-3"
    pmid: "23810019"
    url: "https://doi.org/10.1016/S0140-6736(13)60733-3"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Mesolimbic D2 hyperactivity drives positive symptoms (hallucinations, delusions); mesocortical D1 hypofunction in PFC drives negative and cognitive symptoms; all antipsychotics achieve therapeutic effect via D2 blockade (60-80% receptor occupancy threshold)."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "NMDA receptor hypofunction in PFC parvalbumin interneurons underlies cognitive and negative symptoms; ketamine (NMDA antagonist) reproduces full schizophrenia phenotype; glycine-site NMDA co-agonists and AMPA potentiators are experimental treatments."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Parvalbumin interneuron hypofunction in PFC — reduced GAD67, impaired GABA synthesis — causes deficient gamma oscillations that underlie working memory deficits; GABAergic interneuron loss may be primary, upstream of dopamine and glutamate dysregulation."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "5-HT2A blockade in PFC by atypical antipsychotics (clozapine, olanzapine, risperidone) enhances dopaminergic output; 5-HT2A agonism by hallucinogens (LSD, psilocybin) models positive symptoms; serotonin-dopamine interaction shapes atypical antipsychotic efficacy."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Schizophrenia involves enlarged ventricles, reduced gray matter in DLPFC, superior temporal gyrus, and hippocampus; functional dysconnectivity between PFC and temporal/limbic regions on fMRI; PV interneuron density is reduced in DLPFC and hippocampus post-mortem."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Antipsychotic D2 blockade at the pituitary tuberoinfundibular pathway removes TIDA inhibition → hyperprolactinemia; risperidone/haloperidol cause greatest elevation; galactorrhea, sexual dysfunction, and bone loss are key non-adherence drivers in schizophrenia."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "H1R inverse agonists (clozapine, olanzapine, quetiapine) drive antipsychotic weight gain and sedation; H3R heteroreceptors on DA/5-HT terminals modulate monoamine release; histaminergic TMN arousal neurons are implicated in arousal deficit and cognitive symptoms in schizophrenia."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Schizophrenia's cellular lesion centers on the parvalbumin fast-spiking GABAergic interneuron of the prefrontal cortex and hippocampus: reduced GAD67 and impaired firing degrade the gamma oscillations behind working memory — upstream of the dopamine and glutamate abnormalities."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Schizophrenia and bipolar disorder overlap genetically and clinically: they share risk variants (CACNA1C) and the schizoaffective category, and both feature psychosis — but schizophrenia is dominated by chronic negative/cognitive deficits, bipolar by episodic mood elevation."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus is a key schizophrenia node: reduced in volume with fewer parvalbumin interneurons, and an overactive anterior hippocampus may drive aberrant dopamine release via the subiculum-VTA pathway — linking memory deficits to the dopamine dysregulation behind psychosis."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia are central to a leading schizophrenia hypothesis: complement-C4-tagged synapses are over-pruned by microglia in adolescence, and the strongest common genetic risk maps to the C4 locus—excess synaptic elimination may underlie the disorder's grey-matter loss."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Schizophrenia and autism share neurodevelopmental roots and genetics: overlapping copy-number variants (22q11, 16p11) and synaptic genes underlie both, sitting on a continuum of early brain miswiring—though autism presents in childhood and schizophrenia later."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes contribute to the glutamate dysfunction of schizophrenia: by clearing synaptic glutamate and supplying the NMDA co-agonist D-serine, astrocyte dysfunction can impair NMDA-receptor signaling—the basis of the glutamatergic hypothesis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Schizophrenia and depression overlap and can be hard to separate: depression often complicates schizophrenia and raises suicide risk, and the two share genetic and neurochemical substrates—so mood symptoms are assessed throughout the illness."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Schizophrenia and epilepsy are bidirectionally linked: each roughly doubles the risk of the other, temporal-lobe epilepsy can produce schizophrenia-like psychosis, and they share glutamate and GABA disturbances—genuinely overlapping disorders."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Schizophrenia involves oligodendrocyte and white-matter abnormalities, not just neurons: fewer oligodendrocytes and disrupted myelination impair long-range connectivity, supporting a 'dysconnectivity' model where faulty wiring underlies the illness."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF deficits link schizophrenia to disrupted neurodevelopment: reduced brain-derived neurotrophic factor impairs synaptic plasticity and cortical circuit maturation, fitting the neurodevelopmental model in which schizophrenia's roots predate its psychotic onset by years."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Cannabis use can precipitate and worsen schizophrenia: heavy adolescent use raises the risk of developing psychosis and triggers relapse in patients, since THC perturbs the dopamine and endocannabinoid systems—so cannabis avoidance is part of schizophrenia management."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Acetylcholine is an emerging schizophrenia target beyond dopamine: muscarinic agonists (xanomeline) improve psychosis without blocking dopamine, so the cholinergic system shapes symptoms—a shift from the dopamine-only model of antipsychotic action."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Schizophrenia is increasingly seen as a synaptic disorder: excessive synaptic pruning in adolescence—linked to complement (C4) and microglia—thins prefrontal connectivity, so it is conceived as a disease of disrupted synapses, not just dopamine."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune system is implicated in schizophrenia: a complement-C4 risk variant drives excessive microglial synaptic pruning, and maternal infection raises offspring risk, so neuroinflammation and immune-mediated synapse loss feature in current models of the disease."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Schizophrenia shortens life mainly through cardiovascular disease: antipsychotic-related weight gain and metabolic syndrome, plus smoking and poor access to care, cause excess heart disease—so patients die 15-20 years early, largely of cardiovascular causes."
---

# Schizophrenia

## Overview

**Schizophrenia** is a severe, chronic psychiatric disorder defined by episodic psychosis (hallucinations, delusions) with persistent functional impairment arising from positive, negative, and cognitive symptom domains. It affects approximately **1% of the global population** across all cultures and socioeconomic strata — roughly 24 million people worldwide — and ranks among the most disabling medical conditions, typically emerging in late adolescence to early adulthood (peak onset: males 18–25 years; females 25–35 years, with a second peak at menopause). The illness carries enormous personal, familial, and economic burden: 40–50% of people with schizophrenia attempt suicide, and lifetime mortality is 2–3× the general population.

**DSM-5 diagnostic criteria** require ≥2 of the following symptoms (≥1 month, ≥1 must be from 1–3):
1. Delusions
2. Hallucinations
3. Disorganized speech
4. Grossly disorganized or catatonic behavior
5. Negative symptoms

Plus ≥6 months of social/occupational dysfunction not attributable to substances or medical conditions.

**Three symptom domains** that drive different pathophysiological and treatment implications:

| Domain | Examples | Neural substrate | Treatment response |
|:---|:---|:---|:---|
| **Positive** | Auditory hallucinations, persecutory delusions, thought disorder | Mesolimbic dopamine D2 hyperactivity | Good (antipsychotics) |
| **Negative** | Avolition, alogia, anhedonia, asociality, flat affect (5 A's) | Mesocortical D1 hypofunction; PFC GABAergic deficit | Poor (antipsychotics largely ineffective) |
| **Cognitive** | Working memory, processing speed, verbal learning deficits | DLPFC PV interneuron deficit; NMDA hypofunction | Untreated by current antipsychotics |

## Structure

### Neuroanatomical abnormalities

Structural neuroimaging (MRI) and postmortem studies consistently identify:

**Gray matter reductions:**
- **Dorsolateral prefrontal cortex (DLPFC):** Reduced volume, impaired activation during working memory tasks (hypofrontality on PET/fMRI); correlates with cognitive deficits and negative symptoms
- **Superior temporal gyrus (STG):** Planum temporale reduction (auditory association cortex); correlates with severity of auditory hallucinations
- **Hippocampus and parahippocampal gyrus:** Reduced volume; impaired pattern separation and memory encoding
- **Anterior cingulate cortex:** Reduced volume; correlates with avolition and poor error monitoring

**Structural changes:**
- **Enlarged lateral ventricles:** 5–10% greater volume than controls on average; present in first-episode, drug-naive patients
- **Reduced white matter integrity:** Uncinate fasciculus (PFC–amygdala), arcuate fasciculus (language), cingulum (PFC–hippocampus) on DTI

### Cellular pathology

**Parvalbumin (PV) interneuron deficit:**
- Postmortem DLPFC and hippocampus: reduced PV+ cell density, reduced GAD67 (GABA synthetic enzyme) expression
- PV+ chandelier and basket cells provide perisomatic inhibition to pyramidal neurons and generate high-frequency gamma oscillations (30–80 Hz)
- Loss of PV interneurons → impaired gamma synchrony → working memory deficit (measurable by EEG/MEG in schizophrenia patients and unaffected relatives)

**Synaptic pruning hypothesis:**
- Schizophrenia onset coincides with adolescent synaptic pruning (complement-mediated elimination of weaker synapses via C4A/C4B)
- GWAS identified the **C4A gene** (complement component 4A) as a major schizophrenia risk locus (Sekar et al., 2016); elevated C4A → excess synapse elimination in PFC during pruning → loss of PV interneurons and thalamo-cortical connections

## Function

### The dopamine hypothesis (Version III)

The **mesolimbic/mesocortical dopamine hypothesis** remains the best-supported pathophysiological framework [^howes-2009-dopamine-hypothesis]:

**Evidence from neuroimaging:**
- **[¹⁸F]-DOPA PET:** Measures presynaptic dopamine synthesis capacity; elevated by ~12% in striatum of schizophrenia patients vs. controls; high at first episode before antipsychotic treatment
- **[¹¹C]-raclopride displacement:** Amphetamine displaces more D2 receptor binding in schizophrenia → elevated dopamine release capacity in striatum
- **[¹¹C]-PHNO PET:** Elevated D2/D3 receptor density in caudate/putamen (extrasynaptic D2) correlates with positive symptom severity

**Mesolimbic pathway (VTA → nucleus accumbens, striatum):**
- Tonic dopamine release normally signals reward and salience
- D2 hyperactivation → aberrant salience attribution → neutral stimuli acquire exaggerated personal significance → delusions and hallucinations (Kapur's salience dysregulation theory)

**Mesocortical pathway (VTA → PFC):**
- D1 receptor activation at PFC pyramidal cells supports working memory maintenance (inverted-U: optimal D1 tone required)
- PFC dopamine hypofunction in schizophrenia → working memory deficit, negative symptoms
- Creates a paradox: striatal D2 excess while cortical D1 is deficient

**Antipsychotic mechanism:**
All approved antipsychotics occupy D2 receptors. Clinical response requires **60–80% D2 occupancy** in striatum (PET studies); >80% occupancy → extrapyramidal side effects (EPS). Fast D2 dissociation (aripiprazole, clozapine) reduces EPS risk.

### Glutamate/NMDA receptor hypofunction hypothesis

The glutamate hypothesis arose from the observation that **PCP (phencyclidine)** and **ketamine** (NMDA receptor antagonists) reproduce all three symptom domains (positive, negative, cognitive) in healthy volunteers — an effect not achievable with amphetamine (which only induces positive symptoms) [^moghaddam-2012-glutamate]:

**Circuit mechanism:**
1. PV+ interneurons in PFC express high levels of NMDA receptors (GluN2B-containing)
2. NMDA hypofunction → PV interneuron silencing → reduced GABA release → disinhibition of pyramidal glutamate neurons
3. Excess glutamate in PFC → downstream excess subcortical dopamine release (via nucleus accumbens)
4. Glutamate–dopamine interaction: NMDA hypofunction → both cortical glutamate excess (causing cognitive/negative symptoms) and subcortical dopamine excess (causing positive symptoms)

**Biomarker evidence:**
- CSF glutamate elevated in antipsychotic-naive schizophrenia
- Magnetic resonance spectroscopy (MRS): elevated glutamate in basal ganglia; reduced glutamate in PFC in chronic schizophrenia
- Glutamate hypothesis explains why ketamine models the complete syndrome while amphetamine models only positive symptoms

### Genetic architecture

Schizophrenia has high heritability (~79%) but complex polygenic architecture with no single causal gene:

**Copy number variants (CNVs — large rare variants):**
- **22q11.2 deletion (DiGeorge/velocardiofacial syndrome):** ~1/2000 births; 25–30% develop schizophrenia by adulthood; the highest schizophrenia risk factor known
- **1q21.1, 15q11.2, 15q13.3, 16p11.2:** Associated CNVs with 2–10× increased risk

**GWAS common variants (>260 loci):**
- **C4A/C4B** (complement; synaptic pruning) — most biologically interpretable GWAS signal
- **CACNA1C** (L-type Ca²⁺ channel; also bipolar disorder)
- **COMT** (catechol-O-methyltransferase; dopamine catabolism in PFC)
- **DISC1** (disrupted in schizophrenia 1; rare family with translocation)
- **NRG1** (neuregulin 1; ErbB4 signaling in PV interneurons)
- **DTNBP1** (dysbindin; presynaptic vesicle protein)

**De novo coding mutations** (whole-exome sequencing): SETD1A (histone methyltransferase), SYNGAP1 (synaptic RasGAP), NRXN1 (neurexin; synaptic scaffolding) — rare but high penetrance.

Notably, schizophrenia shares genetic loci with bipolar disorder, ASD, ADHD, major depression, and epilepsy (the **psychiatric cross-disorder overlap** — these conditions share common polygenic risk).

## Pathology

### Clinical course

**Phases:**
1. **Prodrome** (months to years): Social withdrawal, declining function, attenuated psychosis; anxiety, depression; high-risk state for conversion to full psychosis (~30–40% convert in 2 years)
2. **First episode psychosis (FEP):** Acute psychotic break; best prognosis if treated early (DUP — duration of untreated psychosis is the strongest modifiable prognostic factor)
3. **Chronic relapsing-remitting course** (most patients): Positive symptoms respond to antipsychotics; negative/cognitive symptoms persist
4. **Treatment-resistant schizophrenia (TRS):** ~30% do not respond to ≥2 adequate antipsychotic trials; defined by failure to achieve ≥20% symptom reduction

### Comorbidities

- **Substance use disorders:** 50% lifetime; cannabis (particularly high-THC) precipitates psychosis and worsens course (CB1 receptor agonism amplifies dopamine release in striatum)
- **Metabolic syndrome:** 2–3× elevated risk (antipsychotic side effects: weight gain, dyslipidemia, T2D)
- **Cardiovascular disease:** Leading cause of premature death (smoking prevalence 60-80%; antipsychotic metabolic effects)
- **Suicide:** 5–10% completed suicide lifetime (40–50% attempt); clozapine is the only antipsychotic proven to reduce suicidality

### Antipsychotic treatment [^leucht-2013-antipsychotics-meta]

**First-generation (typical) antipsychotics — D2 blockers:**
- Haloperidol, chlorpromazine, fluphenazine
- Highly effective for positive symptoms; ~70% response
- High EPS risk: acute dystonia, akathisia, parkinsonism, tardive dyskinesia (TD; irreversible in ~25% of chronic users)
- Depot formulations (haloperidol decanoate) for adherence

**Second-generation (atypical) antipsychotics — D2 + 5-HT2A antagonists:**

| Drug | D2 Ki | 5-HT2A Ki | Key features |
|:---|:---|:---|:---|
| **Clozapine** | Low affinity (fast off-rate) | Very high | Gold standard for TRS; reduces suicidality; risk: agranulocytosis (1–2%, mandatory ANC monitoring), weight gain, seizures, myocarditis |
| **Olanzapine** | Moderate | High | High efficacy; major metabolic risk (weight gain 4–8 kg/year) |
| **Quetiapine** | Low | High | Sedating; used for comorbid anxiety/sleep; antimaniac effect |
| **Risperidone** | High | High | Effective; EPS at higher doses; hyperprolactinemia |
| **Aripiprazole** | D2 partial agonist | 5-HT2A antagonist | Weight-neutral; activating; reduced EPS |
| **Ziprasidone** | Moderate | High | Low metabolic risk; QTc prolongation risk |

**Novel mechanism — muscarinic antipsychotic (2024):**
- **Xanomeline-trospium (KarXT/Cobenfy, Bristol-Myers Squibb):** FDA-approved September 2024 — first antipsychotic without D2 blockade
- Mechanism: Xanomeline is a muscarinic M1/M4 receptor agonist; M1 activation in PFC improves cognition; M4 activation in striatum reduces dopamine release; trospium (peripheral muscarinic antagonist) limits GI side effects
- EMERGENT-4 trial: significantly reduced PANSS total score vs. placebo; no EPS, no weight gain; represents a new era in schizophrenia treatment

### Early intervention

**First-episode psychosis (FEP) programs:**
- Coordinated specialty care (CSC) combining low-dose antipsychotic, family education, individual therapy, supported education/employment
- RAISE study (2015): CSC significantly superior to standard care for symptoms, quality of life, employment
- Duration of untreated psychosis (DUP) reduction: every week of delay in treatment worsens long-term prognosis

## Connections

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — Mesolimbic D2 hyperactivity drives positive symptoms (hallucinations, delusions); mesocortical D1 hypofunction in PFC drives negative and cognitive symptoms; all antipsychotics achieve therapeutic effect via D2 blockade (60-80% receptor occupancy threshold).

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — NMDA receptor hypofunction in PFC parvalbumin interneurons underlies cognitive and negative symptoms; ketamine (NMDA antagonist) reproduces the full schizophrenia phenotype; glycine-site NMDA co-agonists and AMPA potentiators are experimental treatments.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — Parvalbumin interneuron hypofunction in PFC — reduced GAD67, impaired GABA synthesis — causes deficient gamma oscillations that underlie working memory deficits; GABAergic interneuron loss may be primary, upstream of dopamine and glutamate dysregulation.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — 5-HT2A blockade in PFC by atypical antipsychotics (clozapine, olanzapine, risperidone) enhances dopaminergic output; 5-HT2A agonism by hallucinogens (LSD, psilocybin) models positive symptoms; serotonin-dopamine interaction shapes atypical antipsychotic efficacy.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — Schizophrenia involves enlarged ventricles, reduced gray matter in DLPFC, superior temporal gyrus, and hippocampus; functional dysconnectivity between PFC and temporal/limbic regions on fMRI; PV interneuron density is reduced in DLPFC and hippocampus post-mortem.

- `connects-to` → **[Prolactin](../../../03-molecular/prolactin/README.md)** — antipsychotic D2 blockade at the pituitary tuberoinfundibular pathway removes TIDA inhibition → hyperprolactinemia; risperidone causes greatest elevation (45-100 ng/mL); galactorrhea, sexual dysfunction, and osteoporosis are key drivers of medication non-adherence in schizophrenia.
- `connects-to` → **[Histamine](../../../03-molecular/histamine/README.md)** — H1R inverse agonists (clozapine, olanzapine, quetiapine) drive antipsychotic weight gain and sedation; H3R heteroreceptors on DA/5-HT terminals modulate monoamine release; histaminergic TMN arousal neurons are implicated in arousal deficit and cognitive symptoms in schizophrenia.

- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Schizophrenia's cellular lesion centers on the parvalbumin fast-spiking GABAergic interneuron of the prefrontal cortex and hippocampus: reduced GAD67 and impaired firing degrade the gamma oscillations behind working memory — upstream of the dopamine and glutamate abnormalities.

- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Schizophrenia and bipolar disorder overlap genetically and clinically: they share risk variants (CACNA1C) and the schizoaffective category, and both feature psychosis — but schizophrenia is dominated by chronic negative/cognitive deficits, bipolar by episodic mood elevation.

- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus is a key schizophrenia node: reduced in volume with fewer parvalbumin interneurons, and an overactive anterior hippocampus may drive aberrant dopamine release via the subiculum-VTA pathway — linking memory deficits to the dopamine dysregulation behind psychosis.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia are central to a leading schizophrenia hypothesis: complement-C4-tagged synapses are over-pruned by microglia in adolescence, and the strongest common genetic risk maps to the C4 locus—excess synaptic elimination may underlie the disorder's grey-matter loss.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — Schizophrenia and autism share neurodevelopmental roots and genetics: overlapping copy-number variants (22q11, 16p11) and synaptic genes underlie both, sitting on a continuum of early brain miswiring—though autism presents in childhood and schizophrenia later.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes contribute to the glutamate dysfunction of schizophrenia: by clearing synaptic glutamate and supplying the NMDA co-agonist D-serine, astrocyte dysfunction can impair NMDA-receptor signaling—the basis of the glutamatergic hypothesis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Schizophrenia and depression overlap and can be hard to separate: depression often complicates schizophrenia and raises suicide risk, and the two share genetic and neurochemical substrates—so mood symptoms are assessed throughout the illness.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Schizophrenia and epilepsy are bidirectionally linked: each roughly doubles the risk of the other, temporal-lobe epilepsy can produce schizophrenia-like psychosis, and they share glutamate and GABA disturbances—genuinely overlapping disorders.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Schizophrenia involves oligodendrocyte and white-matter abnormalities, not just neurons: fewer oligodendrocytes and disrupted myelination impair long-range connectivity, supporting a 'dysconnectivity' model where faulty wiring underlies the illness.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF deficits link schizophrenia to disrupted neurodevelopment: reduced brain-derived neurotrophic factor impairs synaptic plasticity and cortical circuit maturation, fitting the neurodevelopmental model in which schizophrenia's roots predate its psychotic onset by years.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Cannabis use can precipitate and worsen schizophrenia: heavy adolescent use raises the risk of developing psychosis and triggers relapse in patients, since THC perturbs the dopamine and endocannabinoid systems—so cannabis avoidance is part of schizophrenia management.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Acetylcholine is an emerging schizophrenia target beyond dopamine: muscarinic agonists (xanomeline) improve psychosis without blocking dopamine, so the cholinergic system shapes symptoms—a shift from the dopamine-only model of antipsychotic action.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Schizophrenia is increasingly seen as a synaptic disorder: excessive synaptic pruning in adolescence—linked to complement (C4) and microglia—thins prefrontal connectivity, so it is conceived as a disease of disrupted synapses, not just dopamine.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune system is implicated in schizophrenia: a complement-C4 risk variant drives excessive microglial synaptic pruning, and maternal infection raises offspring risk, so neuroinflammation and immune-mediated synapse loss feature in current models of the disease.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Schizophrenia shortens life mainly through cardiovascular disease: antipsychotic-related weight gain and metabolic syndrome, plus smoking and poor access to care, cause excess heart disease—so patients die 15-20 years early, largely of cardiovascular causes.

[^howes-2009-dopamine-hypothesis]: Howes OD, Kapur S. The dopamine hypothesis of schizophrenia: version III—the final common pathway. *Schizophr Bull.* 2009;35(3):549-562. [doi:10.1093/schbul/sbp006](https://doi.org/10.1093/schbul/sbp006) · [PubMed 19325164](https://pubmed.ncbi.nlm.nih.gov/19325164/)
[^moghaddam-2012-glutamate]: Moghaddam B, Javitt D. From revolution to evolution: the glutamate hypothesis of schizophrenia and its implication for treatment. *Neuropsychopharmacology.* 2012;37(1):4-15. [doi:10.1038/npp.2011.181](https://doi.org/10.1038/npp.2011.181) · [PubMed 21956446](https://pubmed.ncbi.nlm.nih.gov/21956446/)
[^leucht-2013-antipsychotics-meta]: Leucht S, Cipriani A, Spineli L, et al. Comparative efficacy and tolerability of 15 antipsychotic drugs in schizophrenia: a multiple-treatments meta-analysis. *Lancet.* 2013;382(9896):951-962. [doi:10.1016/S0140-6736(13)60733-3](https://doi.org/10.1016/S0140-6736(13)60733-3) · [PubMed 23810019](https://pubmed.ncbi.nlm.nih.gov/23810019/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
