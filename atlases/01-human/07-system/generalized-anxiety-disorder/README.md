---
schema: human-scale-entry/v1
id: generalized-anxiety-disorder
name: Generalized Anxiety Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "GAD (6% lifetime prevalence) is defined by 6+ months of excessive, uncontrollable worry; driven by HPA axis dysregulation, noradrenergic hyperactivity, and GABAergic deficit; SSRIs/SNRIs and duloxetine are first-line; buspirone and pregabalin are alternatives."
aliases: ["GAD", "generalized anxiety disorder", "anxiety neurosis", "chronic anxiety", "free-floating anxiety", "worry disorder"]
sources:
  - id: kessler-2005-gad-prevalence
    type: peer-reviewed
    cite: "Kessler RC, Berglund P, Demler O, et al. Lifetime prevalence and age-of-onset distributions of DSM-IV disorders in the National Comorbidity Survey Replication. Arch Gen Psychiatry. 2005;62(6):593-602."
    doi: "10.1001/archpsyc.62.6.593"
    pmid: "15939837"
    url: "https://doi.org/10.1001/archpsyc.62.6.593"
    accessed: "2026-06-08"
  - id: bandelow-2015-anxiety-biology
    type: peer-reviewed
    cite: "Bandelow B, Michaelis S. Epidemiology of anxiety disorders in the 21st century. Dialogues Clin Neurosci. 2015;17(3):327-335."
    doi: "10.31887/DCNS.2015.17.3/bbandelow"
    pmid: "26487812"
    url: "https://doi.org/10.31887/DCNS.2015.17.3/bbandelow"
    accessed: "2026-06-08"
  - id: baldwin-2014-gad-treatment
    type: peer-reviewed
    cite: "Baldwin DS, Anderson IM, Nutt DJ, et al. Evidence-based pharmacological treatment of anxiety disorders, post-traumatic stress and obsessive-compulsive disorder: a revision of the 2005 guidelines from the British Association for Psychopharmacology. J Psychopharmacol. 2014;28(5):403-439."
    doi: "10.1177/0269881114525674"
    pmid: "24713617"
    url: "https://doi.org/10.1177/0269881114525674"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SSRIs (escitalopram, sertraline) and SNRIs (venlafaxine, duloxetine) are first-line GAD pharmacotherapy; 5-HT1A receptor partial agonist buspirone is second-line; serotonergic deficiency in amygdala-PFC circuits contributes to hypervigilance and excessive worry."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Locus coeruleus NE hyperactivity drives sympathetic arousal, hypervigilance, and somatic anxiety symptoms in GAD; SNRIs (duloxetine, venlafaxine) treat GAD via dual NE + 5-HT reuptake inhibition; propranolol reduces peripheral β-adrenergic symptoms of anxiety."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "GABAergic deficit in amygdala, hippocampus, and PFC reduces inhibitory tone on the fear circuit → pathological worry; benzodiazepines (positive GABA-A allosteric modulators) provide rapid relief; pregabalin (α2δ VGCC subunit ligand) reduces glutamate/GABA imbalance."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Excessive amygdala glutamatergic activity drives hypervigilance and threat anticipation in GAD; pregabalin reduces glutamate release via α2δ VGCC subunit blockade; ketamine's anti-anxiety effect involves rapid normalization of PFC glutamate transmission."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "HPA axis hyperactivation in GAD → elevated cortisol → hippocampal volume reduction and impaired extinction of conditioned fear; cortisol feedback sensitization perpetuates chronic worry; morning cortisol is elevated in GAD and normalizes with SSRI treatment."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "GAD involves amygdala hyperreactivity, PFC hypoactivity (impaired worry regulation), and reduced hippocampal volume; fMRI shows increased amygdala-insula connectivity and failure of ventromedial PFC to suppress amygdala fear responses during worry provocation."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Generalized and social anxiety disorders share amygdala hyperreactivity and serotonergic biology but differ in focus: GAD is diffuse, future-oriented worry across many life domains, whereas social anxiety is fear of being judged in specific social situations."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "GAD has the highest depression comorbidity of any anxiety disorder (~67% lifetime), reflecting shared monoamine, HPA-axis, and amygdala-PFC substrates; the two are typically treated together with the same SSRIs/SNRIs, and duloxetine covers both plus comorbid pain."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Generalized anxiety and panic disorder are distinct anxiety syndromes: GAD is sustained, free-floating worry with muscle tension, whereas panic disorder is discrete attacks of intense fear with autonomic surge and situational avoidance."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Insomnia and GAD are tightly intertwined: ruminative worry and hyperarousal make sleep hard, and the sleep loss worsens anxiety next day—a bidirectional loop; both share heightened cortisol/noradrenergic tone, and CBT-I plus anxiety treatment help each."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "GAD and PTSD are overlapping stress disorders with shared hypervigilance, sleep disturbance and amygdala-prefrontal dysregulation, but differ in trigger: PTSD follows a defining trauma with re-experiencing and avoidance, while GAD is free-floating worry; they frequently co-occur."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Generalized anxiety drives and mimics cardiac disease: chronic sympathetic/HPA activation raises heart rate and blood pressure with higher cardiovascular risk, while palpitations and chest tightness send anxious patients to cardiology—telling GAD from heart disease matters."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "GAD and OCD are anxiety-related disorders that often co-occur but differ in form: GAD is diffuse, free-floating worry about everyday matters, while OCD's anxiety is tied to intrusive obsessions relieved by compulsions—both respond to SSRIs and CBT."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Generalized anxiety frequently coexists with bipolar disorder and complicates it: anxiety worsens the course and suicidality, and antidepressants for it can destabilize mood or trigger mania—so anxiety in a bipolar patient is managed cautiously after mood stabilization."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Generalized anxiety and alcohol use disorder form a self-medication cycle: people drink to quiet chronic worry, but alcohol and its withdrawal rebound into worse anxiety, deepening both conditions—so the two strongly co-occur and need concurrent treatment."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Generalized anxiety and fibromyalgia commonly overlap through central sensitization: chronic anxiety and HPA-axis dysregulation amplify pain processing, so anxiety is far more common in fibromyalgia and worsens its pain and fatigue."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Anxiety and asthma form a vicious cycle: breathlessness triggers anxiety and anxiety worsens perceived dyspnea, so anxiety disorders are common in asthma and degrade control—distinguishing a panic attack from bronchospasm matters clinically."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Generalized anxiety and migraine are strongly comorbid: they share serotonergic and stress-pathway biology, anxiety lowers the threshold for migraine attacks, and chronic migraine fuels anxiety—so treating one (e.g. with SNRIs) often helps the other."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Generalized anxiety disorder is rooted in an overactive stress axis: corticotropin-releasing hormone drives the HPA response, and chronically elevated CRH signaling keeps the brain in a state of vigilance and worry that characterizes the disorder."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "The serotonin transporter is GAD's main drug target: SSRIs and SNRIs block it to raise synaptic serotonin, and a common transporter-gene variant (5-HTTLPR) is linked to anxiety-prone temperament—tying the disorder's biology to its first-line treatment."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Generalized anxiety disorder is increasingly linked to the gut-brain axis: the gut microbiome modulates stress hormones and neurotransmitters via the vagus nerve, and dysbiosis is associated with heightened anxiety—an emerging target beyond brain-centered models."
---

# Generalized Anxiety Disorder

## Overview

**Generalized anxiety disorder (GAD)** is a chronic anxiety disorder characterized by **excessive, uncontrollable worry** about multiple life domains (health, finances, relationships, performance) for ≥6 months, accompanied by somatic symptoms (muscle tension, fatigue, restlessness, insomnia, irritability, difficulty concentrating). GAD is among the most prevalent mental health conditions globally, with a **lifetime prevalence of ~5-6%** and a 12-month prevalence of ~2-3% [^kessler-2005-gad-prevalence].

Unlike fear (a response to an immediate threat), anxiety in GAD is **anticipatory, diffuse, and future-oriented** — focused on potential threats that may never materialize. This distinction has important neurobiological implications: fear engages the basolateral amygdala (BLA) responding to cues; anxiety engages the bed nucleus of the stria terminalis (BNST) and anterior cingulate cortex (ACC) in sustained vigilance states.

GAD has a **2:1 female:male prevalence** and typically begins in early adulthood (median onset ~30 years), though a bimodal distribution includes childhood-onset cases. The course is chronic and waxing-waning, with fewer than one-third achieving sustained remission without treatment [^bandelow-2015-anxiety-biology]. GAD has the highest rate of comorbidity with major depressive disorder (~67% lifetime comorbidity) of all anxiety disorders — reflecting shared neurobiological substrates (monoaminergic systems, HPA axis, amygdala-PFC circuits).

**Distinction from other anxiety disorders:**
- GAD: pervasive worry across multiple domains; future-oriented; somatic tension; no avoidance of specific stimuli
- Panic disorder: episodic intense fear (panic attacks), not sustained worry; typically involves situational avoidance
- Social anxiety disorder: specific to social evaluation; discrete situational triggers; performance-focused
- PTSD: worry anchored to a specific traumatic event; intrusive memories and hyperarousal; avoidance of trauma cues
- OCD: ego-dystonic obsessions followed by compulsive rituals; distinct CSTC circuit pathology

## Structure

### Neurobiology of anxiety [^bandelow-2015-anxiety-biology]

**Fear circuit (immediate threat — normal fear):**
Sensory input → thalamus → BLA (basolateral amygdala) → CeA (central amygdala) → brainstem effectors → sympathetic arousal, freezing, flight/fight

**Anxiety circuit (sustained anticipatory anxiety — GAD):**
PFC (worry generation) → BNST (sustained vigilance) → hypothalamus (HPA activation) → hippocampus (contextual modulation) → BLA (threat appraisal) → CeA output → sustained arousal state

**PFC-amygdala balance:**
The **ventromedial PFC (vmPFC)** normally provides "top-down" inhibitory regulation of amygdala reactivity — suppressing fear responses after threat appraisal. In GAD:
- vmPFC activity is reduced → impaired inhibition of amygdala responses
- Amygdala reactivity is increased → heightened threat detection and arousal
- ACC (anterior cingulate cortex) is hyperactive → sustained worry loops
- Insula hyperactivation → heightened interoception and somatic symptom awareness

**HPA axis:**
Chronic stress → elevated CRH (corticotropin-releasing hormone) from PVN → ACTH from anterior pituitary → cortisol from adrenal cortex → HPA feedback sensitization in GAD. Elevated cortisol → hippocampal volume reduction (GR-mediated excitotoxicity) → impaired contextual fear extinction → perpetuates anxiety. Morning plasma cortisol is elevated in GAD and normalizes with effective SSRI treatment.

### The role of GABA and glutamate

**GABAergic deficit:** MRS (magnetic resonance spectroscopy) studies document reduced GABA in the occipital cortex, PFC, and insula of GAD patients. Reduced GABAergic inhibitory tone in amygdala and hippocampal circuits allows excitatory circuits to dominate → excessive threat detection and anxiety maintenance.

**Glutamatergic excess:** Elevated glutamate in the anterior cingulate cortex and amygdala (MRS) contributes to rumination and hypervigilance. Pregabalin works by reducing the α2δ subunit of voltage-gated calcium channels → reduced glutamate and substance P release at anxiety-related synapses.

## Function

### DSM-5 diagnostic criteria

**A.** Excessive anxiety and worry (apprehensive expectation) about multiple events or activities, occurring more days than not for ≥6 months
**B.** Difficulty controlling the worry
**C.** At least three of the following (one for children):
1. **Restlessness** or feeling keyed up/on edge
2. Being easily **fatigued**
3. Difficulty **concentrating** or mind going blank
4. **Irritability**
5. **Muscle tension**
6. **Sleep disturbance** (difficulty falling/staying asleep, or restless unsatisfying sleep)

**D.** Significant distress or functional impairment
**E.** Not attributable to substances or medical condition
**F.** Not better explained by another anxiety disorder

**Assessment tools:** GAD-7 (7-item validated scale; score 5-9 = mild, 10-14 = moderate, 15-21 = severe; ≥10 = probable GAD requiring assessment); Penn State Worry Questionnaire (PSWQ); Hamilton Anxiety Rating Scale (HAM-A).

### Somatic presentations

GAD frequently presents to primary care with predominantly somatic complaints:
- **Muscle tension:** Headaches (tension-type), neck/shoulder tightness, jaw clenching (TMJ dysfunction)
- **Cardiovascular:** Palpitations, atypical chest discomfort (heightened cardiac awareness without structural disease)
- **Gastrointestinal:** IBS overlap (~40% of IBS patients have GAD); nausea, bloating, urgency
- **Sleep:** Initial insomnia (difficulty falling asleep due to racing thoughts) and early morning awakening
- **Fatigue:** Chronic fatigue from sustained sympathetic arousal and sleep disruption
- **Cognitive:** "Mental blanks," poor concentration, indecisiveness

**GAD and medical illness:** GAD is 3-4× more prevalent in patients with chronic medical conditions (diabetes, CHD, COPD). The relationship is bidirectional: GAD worsens illness outcomes (poor adherence, amplified pain, impaired sleep), and illness exacerbates anxiety.

### Comorbidities

| Comorbidity | Frequency | Notes |
|:---|:---|:---|
| Major depressive disorder | ~67% lifetime | Highest MDD co-occurrence of all anxiety disorders; treat both simultaneously |
| Other anxiety disorders (panic, social anxiety, specific phobia) | ~50% | Distinct phenomenology and treatment response despite shared biology |
| PTSD | ~20% | Trauma history amplifies GAD risk; PTSD may precede GAD |
| Substance use disorder (alcohol, benzodiazepines) | ~25% | Self-medication of anxiety; complicates treatment |
| Pain disorders (fibromyalgia, IBS, migraine) | ~30-40% | Central sensitization shared mechanism; serotonin-NE axis involvement |
| Insomnia | ~75% | Bidirectional; poor sleep worsens anxiety; CBT-I as adjunct |

## Pathology

### Genetics and biomarkers

GAD heritability: **30-40%** (twin studies) — lower than mood disorders or schizophrenia, suggesting greater environmental contribution. Shared genetic variance with MDD and neuroticism. GWAS: limited findings; RBFOX1 (RNA-binding protein) and chromosomal regions overlapping with depression and other anxiety disorders have been implicated.

**Neuroimaging biomarkers:**
- Amygdala volume: smaller in GAD; resting-state hyperconnectivity between amygdala and ACC
- vmPFC gray matter: reduced thickness correlates with anxiety severity
- Hippocampal volume: reduced (~5-8%) compared to healthy controls, consistent with chronic HPA axis stress exposure

**Biological markers:** Elevated morning cortisol; reduced benzodiazepine receptor density (lower SPECT signal) in prefrontal cortex; elevated CRH in CSF. None are diagnostic biomarkers; they are research tools.

### Treatment [^baldwin-2014-gad-treatment]

**First-line — SSRIs and SNRIs:**

| Drug | Class | Starting dose | Target dose | Notes |
|:---|:---|:---|:---|:---|
| **Escitalopram** | SSRI | 5 mg | 10-20 mg | Best-tolerated SSRI; first-line for GAD + MDD comorbidity |
| **Sertraline** | SSRI | 25-50 mg | 50-200 mg | Well-tolerated; broad anxiety efficacy; once-daily |
| **Paroxetine CR** | SSRI | 12.5 mg | 25-62.5 mg | Anti-anxiety potency; anticholinergic side effects; discontinuation syndrome |
| **Venlafaxine XR** | SNRI | 37.5-75 mg | 75-225 mg | Dual NE/5-HT; evidence for dose-response in GAD; BP monitoring needed |
| **Duloxetine** | SNRI | 30 mg | 60-120 mg | FDA-approved for GAD; also targets pain comorbidity; nausea common initially |

Allow **4-8 weeks** for onset of anxiolytic effect. Continue treatment ≥12 months after remission to prevent relapse.

**Second-line:**

| Drug | Mechanism | Notes |
|:---|:---|:---|
| **Buspirone** | 5-HT1A partial agonist | Non-addictive; onset 2-4 weeks; less effective if prior benzodiazepine use; no cross-tolerance |
| **Pregabalin** | α2δ VGCC subunit ligand | Reduces glutamate/substance P release; onset 1-2 weeks; evidence for GAD; weight gain; potential abuse liability |
| **TCAs (imipramine)** | NE + SERT block | Effective but poorly tolerated; anticholinergic side effects; overdose risk |
| **Hydroxyzine** | H1 antihistamine | Rapid anxiolytic (within 30 min); useful for acute or situational anxiety; sedating |
| **Quetiapine XR** | D2/5-HT2A antagonist | Off-label; effective in treatment-resistant GAD; metabolic side effects limit use |

**Benzodiazepines (short-term/adjunctive only):**
- Effective for rapid relief (diazepam, lorazepam, clonazepam) but NOT recommended as first-line or long-term due to dependence, cognitive impairment, fall risk in elderly, and rebound anxiety
- Appropriate uses: initial weeks while SSRI/SNRI is titrated; acute exacerbations; procedural anxiety
- Taper gradually (10% reduction per week) to avoid withdrawal seizures in long-term users

**First-line — Psychotherapy:**
**CBT (cognitive-behavioral therapy)** for GAD:
- Cognitive restructuring (challenging catastrophic predictions)
- Worry exposure (controlled engagement with worry topics → habituation)
- Relaxation training (progressive muscle relaxation, diaphragmatic breathing)
- Response rate: ~60-65% (similar to pharmacotherapy); effect persists after termination (unlike medication)
- Combined CBT + medication superior to either alone in treatment-resistant cases

**Mindfulness-Based Stress Reduction (MBSR):** Strong evidence for GAD; 8-week group intervention; reduces amygdala reactivity and improves vmPFC regulation on fMRI; durable effects at 1-year follow-up.

## Connections

- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — SSRIs (escitalopram, sertraline) and buspirone (5-HT1A partial agonist) are first-line GAD treatments; serotonergic deficiency in amygdala-PFC circuits contributes to hypervigilance and excessive worry; 4-8 week response latency reflects serotonergic neuroplasticity.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — locus coeruleus NE hyperactivity drives sympathetic arousal and somatic anxiety symptoms in GAD; SNRIs (duloxetine, venlafaxine) provide dual NE + serotonin reuptake inhibition; propranolol reduces peripheral β-adrenergic manifestations of anxiety (palpitations, tremor).
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — reduced GABAergic inhibitory tone in amygdala, hippocampus, and PFC allows excitatory anxiety circuits to dominate in GAD; benzodiazepines provide rapid symptom relief via GABA-A allosteric potentiation; pregabalin reduces glutamate/substance P release via α2δ blockade.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — excessive amygdala glutamatergic activity drives hypervigilance and threat anticipation in GAD; pregabalin reduces glutamate release via α2δ VGCC subunit blockade; NMDA receptor involvement in fear extinction underlies D-cycloserine augmentation strategies.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — HPA axis hyperactivation in GAD → elevated cortisol → hippocampal volume reduction and impaired extinction of conditioned fear; morning cortisol is elevated in GAD and normalizes with SSRI treatment; chronic cortisol elevation perpetuates amygdala sensitization.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — GAD involves amygdala hyperreactivity, vmPFC hypoactivity, and hippocampal volume reduction; fMRI shows increased amygdala-insula connectivity and failure of vmPFC to suppress amygdala fear responses; effective treatment (SSRIs or CBT) normalizes amygdala reactivity.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — Generalized and social anxiety disorders share amygdala hyperreactivity and serotonergic biology but differ in focus: GAD is diffuse, future-oriented worry across many life domains, whereas social anxiety is fear of being judged in specific social situations.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — GAD has the highest depression comorbidity of any anxiety disorder (~67% lifetime), reflecting shared monoamine, HPA-axis, and amygdala-PFC substrates; the two are typically treated together with the same SSRIs/SNRIs, and duloxetine covers both plus comorbid pain.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Generalized anxiety and panic disorder are distinct anxiety syndromes: GAD is sustained, free-floating worry with muscle tension, whereas panic disorder is discrete attacks of intense fear with autonomic surge and situational avoidance.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Insomnia and GAD are tightly intertwined: ruminative worry and hyperarousal make sleep hard, and the sleep loss worsens anxiety next day—a bidirectional loop; both share heightened cortisol/noradrenergic tone, and CBT-I plus anxiety treatment help each.
- `connects-to` → **[PTSD](../ptsd/README.md)** — GAD and PTSD are overlapping stress disorders with shared hypervigilance, sleep disturbance and amygdala-prefrontal dysregulation, but differ in trigger: PTSD follows a defining trauma with re-experiencing and avoidance, while GAD is free-floating worry; they frequently co-occur.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Generalized anxiety drives and mimics cardiac disease: chronic sympathetic/HPA activation raises heart rate and blood pressure with higher cardiovascular risk, while palpitations and chest tightness send anxious patients to cardiology—telling GAD from heart disease matters.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — GAD and OCD are anxiety-related disorders that often co-occur but differ in form: GAD is diffuse, free-floating worry about everyday matters, while OCD's anxiety is tied to intrusive obsessions relieved by compulsions—both respond to SSRIs and CBT.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Generalized anxiety frequently coexists with bipolar disorder and complicates it: anxiety worsens the course and suicidality, and antidepressants for it can destabilize mood or trigger mania—so anxiety in a bipolar patient is managed cautiously after mood stabilization.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Generalized anxiety and alcohol use disorder form a self-medication cycle: people drink to quiet chronic worry, but alcohol and its withdrawal rebound into worse anxiety, deepening both conditions—so the two strongly co-occur and need concurrent treatment.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Generalized anxiety and fibromyalgia commonly overlap through central sensitization: chronic anxiety and HPA-axis dysregulation amplify pain processing, so anxiety is far more common in fibromyalgia and worsens its pain and fatigue.
- `connects-to` → **[Asthma](../asthma/README.md)** — Anxiety and asthma form a vicious cycle: breathlessness triggers anxiety and anxiety worsens perceived dyspnea, so anxiety disorders are common in asthma and degrade control—distinguishing a panic attack from bronchospasm matters clinically.
- `connects-to` → **[Migraine](../migraine/README.md)** — Generalized anxiety and migraine are strongly comorbid: they share serotonergic and stress-pathway biology, anxiety lowers the threshold for migraine attacks, and chronic migraine fuels anxiety—so treating one (e.g. with SNRIs) often helps the other.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Generalized anxiety disorder is rooted in an overactive stress axis: corticotropin-releasing hormone drives the HPA response, and chronically elevated CRH signaling keeps the brain in a state of vigilance and worry that characterizes the disorder.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — The serotonin transporter is GAD's main drug target: SSRIs and SNRIs block it to raise synaptic serotonin, and a common transporter-gene variant (5-HTTLPR) is linked to anxiety-prone temperament—tying the disorder's biology to its first-line treatment.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Generalized anxiety disorder is increasingly linked to the gut-brain axis: the gut microbiome modulates stress hormones and neurotransmitters via the vagus nerve, and dysbiosis is associated with heightened anxiety—an emerging target beyond brain-centered models.

[^kessler-2005-gad-prevalence]: Kessler RC, Berglund P, Demler O, et al. Lifetime prevalence and age-of-onset distributions of DSM-IV disorders in the NCS Replication. *Arch Gen Psychiatry.* 2005;62(6):593-602. [doi:10.1001/archpsyc.62.6.593](https://doi.org/10.1001/archpsyc.62.6.593) · [PubMed 15939837](https://pubmed.ncbi.nlm.nih.gov/15939837/)
[^bandelow-2015-anxiety-biology]: Bandelow B, Michaelis S. Epidemiology of anxiety disorders in the 21st century. *Dialogues Clin Neurosci.* 2015;17(3):327-335. [doi:10.31887/DCNS.2015.17.3/bbandelow](https://doi.org/10.31887/DCNS.2015.17.3/bbandelow) · [PubMed 26487812](https://pubmed.ncbi.nlm.nih.gov/26487812/)
[^baldwin-2014-gad-treatment]: Baldwin DS, Anderson IM, Nutt DJ, et al. Evidence-based pharmacological treatment of anxiety disorders. *J Psychopharmacol.* 2014;28(5):403-439. [doi:10.1177/0269881114525674](https://doi.org/10.1177/0269881114525674) · [PubMed 24713617](https://pubmed.ncbi.nlm.nih.gov/24713617/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
