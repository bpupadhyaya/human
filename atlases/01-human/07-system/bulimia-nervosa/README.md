---
schema: human-scale-entry/v1
id: bulimia-nervosa
name: Bulimia Nervosa
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Eating disorder characterized by binge eating + compensatory behaviors (purging, fasting, exercise) ≥1/week × 3 months at normal weight. Serotonin hypofunction drives impulsivity; fluoxetine 60 mg is FDA-approved. CBT-BN is first-line treatment."
aliases: ["BN", "bulimia", "binge-purge disorder", "purging disorder"]
sources:
  - id: fairburn-2008-cbt-eating-disorders
    type: textbook
    cite: "Fairburn CG. Cognitive Behavior Therapy and Eating Disorders. Guilford Press; 2008."
    url: "https://www.guilford.com/books/Cognitive-Behavior-Therapy-and-Eating-Disorders/Fairburn/9781593857097"
    accessed: "2026-06-08"
  - id: kaye-2008-bn-neurobiology
    type: peer-reviewed
    cite: "Kaye WH, Fudge JL, Paulus M. New insights into symptoms and neurocircuit function of anorexia nervosa. Nat Rev Neurosci. 2009;10(8):573-584."
    doi: "10.1038/nrn2682"
    pmid: "19603056"
  - id: hadigan-1995-fluoxetine-bn
    type: peer-reviewed
    cite: "Fluoxetine in the treatment of bulimia nervosa. A multicenter, placebo-controlled, double-blind trial. Fluoxetine Bulimia Nervosa Collaborative Study Group. Arch Gen Psychiatry. 1992;49(2):139-47."
    pmid: "1550466"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin hypofunction in prefrontal-limbic circuits drives impulse control failure and binge episodes in BN; 5-HT2C activation reduces food intake; fluoxetine 60 mg (FDA-approved, the highest approved SSRI dose for any indication) reduces binge/purge frequency ~50%."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dysregulated striatal dopamine drives binge reinforcement in BN; D3R in NAcc; PET shows ↑DA release during food cue exposure; altered reward prediction error signaling contributes to loss-of-control eating; dopamine mediates the negative reinforcement of purging."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Ghrelin (hunger hormone) is elevated in BN during restriction phases → amplifies binge trigger; ghrelin rises fail to suppress normally after binge eating in BN; ghrelin-NPY axis drives hyperphagia in restriction-binge cycles; ghrelin receptor antagonism is under investigation."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "BN involves insula dysfunction (impaired satiety signaling), reduced PFC inhibitory control over limbic reward circuits, ACC conflict monitoring deficits, and striatal reward hyperreactivity to food cues; CBT-BN normalizes PFC-striatal connectivity on fMRI."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "BN and AN share dietary-restraint → binge/compensatory pathophysiology with body-image distortion; BMI distinguishes (normal in BN, low in AN); ~25% AN patients later develop BN; DSM-5 criterion E excludes BN if AN active; AN carries higher mortality (SMR 5-10x vs 1.5-2x)."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Leptin signals adipose energy stores to hypothalamus; binge-purge cycles blunt leptin fluctuation → impaired satiety sensing; purging reduces leptin acutely despite adequate caloric load; leptin-NPY arcuate axis dysregulation in BN impairs hunger-fullness signaling."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "HPA dysregulation in BN → elevated cortisol during restriction/binge; stress cortisol drives emotional eating and binge triggers; cortisol elevates ghrelin and suppresses leptin → amplifies hunger drives; purging transiently reduces cortisol, reinforcing the cycle."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "Bulimia nervosa and ADHD share impulsivity and reward-circuit dysfunction: childhood ADHD roughly doubles later bulimia risk, with weak prefrontal inhibitory control and dysregulated striatal dopamine underlying both binge eating and impulsive behavior."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "Bulimia nervosa and binge-eating disorder both feature recurrent loss-of-control binges but differ in the aftermath: BN includes compensatory purging (vomiting, laxatives, exercise) keeping weight near-normal, while BED has binges without purging and trends toward obesity."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "Bulimia nervosa and borderline personality disorder frequently co-occur (~25-30%), sharing impulsivity, affect dysregulation, and self-harm; binge-purge cycles can serve the same emotion-regulation role as BPD impulsivity, and dialectical behavior therapy helps both."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression is among the commonest bulimia comorbidities: shared serotonergic dysfunction underlies both, the shame of binge-purge cycles deepens low mood, and SSRIs (fluoxetine is the only FDA-approved bulimia drug) treat both—though purging can undermine medication absorption."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Purging makes bulimia dangerous to the heart: self-induced vomiting and laxative abuse waste potassium → hypokalemia that prolongs QT and triggers fatal arrhythmia, the leading cause of sudden death in bulimia; ipecac abuse adds a direct cardiomyopathy."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Bulimia and substance use disorders, especially alcohol, frequently co-occur: shared impulsivity and reward-system dysregulation link binge eating and binge drinking, and the combination worsens medical risk and self-harm; integrated treatment of both beats treating either alone."
---

# Bulimia Nervosa

## Overview

Bulimia nervosa (BN) is an eating disorder defined by recurrent episodes of **binge eating** followed by **compensatory behaviors** designed to prevent weight gain. Unlike anorexia nervosa, patients with BN typically maintain a normal or above-average body weight — a feature that both delays recognition and distinguishes its pathophysiology. The disorder is characterized by a profound disruption of the normal capacity to regulate eating, driven by neurobiological dysregulation of serotonin-mediated impulse control, dopamine reward circuits, and interoceptive signaling of hunger and satiety [^kaye-2008-bn-neurobiology].

The defining features — binge eating and purging — create a vicious cycle: restrictive dieting increases hunger drives and erodes inhibitory control → uncontrolled binge → guilt/shame → purging to restore perceived control → further restriction → next binge. This restriction-binge-purge cycle is perpetuated by serotonin hypofunction, dopaminergic reward dysregulation, and the reinforcing properties of purging (rapid reduction in anxiety).

Bulimia nervosa carries significant medical morbidity (electrolyte imbalances, dental erosion, esophageal complications) and high psychiatric comorbidity (depression, anxiety, substance use), though mortality is lower than anorexia nervosa. The only FDA-approved pharmacotherapy is **fluoxetine 60 mg** — notably the highest approved SSRI dose for any psychiatric indication — based on large multicenter RCTs [^hadigan-1995-fluoxetine-bn].

## Overview

### Epidemiology

| Parameter | Value |
|:---|:---|
| **Lifetime prevalence (women)** | 1–2% |
| **Lifetime prevalence (men)** | 0.1–0.5% |
| **Age of onset** | Typically late adolescence/early adulthood (16–24 years) — later than AN |
| **Body weight** | Normal or above-average BMI (unlike AN); BMI typically 18.5–25 |
| **Mortality (SMR)** | ~1.5–2× general population (lower than AN SMR 5–10×) |
| **Sex ratio** | ~10:1 female:male |
| **Racial/ethnic factors** | Less commonly diagnosed in non-white groups due to recognition bias; prevalence appears more equal |

## Structure

### DSM-5 Diagnostic Criteria

All of the following must be met:

**A. Recurrent binge eating episodes:**
- Eating a larger amount of food in a discrete period than most would eat
- Sense of **loss of control** over eating during the episode

**B. Recurrent inappropriate compensatory behaviors:**
- **Purging type:** Self-induced vomiting, misuse of laxatives/diuretics/enemas
- **Non-purging type:** Excessive exercise, fasting (without regular purging)

**C. Frequency/duration:** Behaviors occur at least **once per week for 3 months**

**D. Self-evaluation** is unduly influenced by body shape and weight

**E. Not occurring exclusively during episodes of anorexia nervosa**

### Severity Specifiers (based on purging frequency/week)

| Severity | Compensatory behaviors/week |
|:---|:---|
| Mild | 1–3 |
| Moderate | 4–7 |
| Severe | 8–13 |
| Extreme | ≥14 |

## Function

### Neurobiological Mechanisms

**Serotonin hypofunction (primary driver):**

- 5-HT2C receptors in the hypothalamic arcuate nucleus mediate satiety signaling; reduced 5-HT2C signaling → impaired satiety → prolonged eating
- 5-HT in PFC mediates impulse control; serotonin deficiency → ↓inhibitory control over eating impulses → binge vulnerability
- Kaye and colleagues documented chronically reduced CSF 5-HIAA in both acute and recovered BN patients — suggesting trait hyposerotonergic state, not simply starvation-related tryptophan depletion
- 5-HT3R in the nucleus accumbens amplifies dopamine release during binge eating, contributing to binge reinforcement
- Fluoxetine 60 mg (vs. 20 mg for depression) raises synaptic 5-HT substantially above the threshold needed for impulse control normalization in BN

**Dopamine reward circuit dysregulation:**

- Striatal D3R on NAcc neurons; food cues trigger exaggerated DA release → heightened incentive salience of food
- PET studies show increased striatal DA release in BN during food cue exposure (analogous to substance use disorder cue reactivity)
- Reduced D2R availability in dorsal striatum → impaired goal-directed control over eating behavior
- Binge eating and purging both activate the mesolimbic DA system, though through different mechanisms:
  - **Binge:** Large caloric load → massive opioid + DA surge
  - **Purging:** Anxiety relief → negative reinforcement via DA normalization

**Insula-interoceptive circuit failure:**

- The insular cortex integrates interoceptive signals (hunger, satiety, nausea, disgust) with emotional valence
- BN patients show altered insula activation during hunger/satiety signaling — impairing recognition of fullness during binges
- Failure of normal satiety detection (mediated by CCK, GLP-1, ghrelin suppression) prevents timely binge termination
- Insula hyperactivation to food cues and hypoactivation during actual eating creates a paradoxical satiety failure

**Prefrontal inhibitory failure:**

- Right ventral PFC mediates inhibitory control over impulses; reduced gray matter in VLPFC in BN
- Reduced top-down PFC regulation of amygdala (food-related fear/desire) and striatum (reward drive)
- This parallels substance use disorder: the ratio of bottom-up reward drive to top-down inhibitory control is shifted toward drive

### Ghrelin and the Restriction-Binge Cycle

- **Restriction phase:** Caloric restriction → ↑ fasting ghrelin → ↑ NPY/AgRP → ↑ hunger and appetite → cravings amplified
- **Pre-binge:** Ghrelin remains elevated (fails to suppress with normal pre-meal cues in BN)
- **Binge:** Caloric intake rapidly suppresses ghrelin, but post-binge satiety signals (CCK, PYY, GLP-1) are less effective in BN, allowing binge continuation
- **Post-purge:** Ghrelin rises again rapidly after purging — driving next restriction/binge cycle

### Medical Complications

| System | Complication | Mechanism |
|:---|:---|:---|
| **Oral** | Dental erosion (perimylolysis), enamel loss on lingual surface | Gastric acid from chronic vomiting |
| **Salivary** | Parotid hypertrophy (sialoadenosis), elevated amylase | Chronic repetitive mechanical stimulation |
| **GI** | Esophagitis, Barrett's esophagus, Mallory-Weiss tears, constipation, rectal prolapse | Acid reflux; laxative abuse; excessive straining |
| **Metabolic** | Hypokalemia, hypochloremia, metabolic alkalosis (from purging); hyponatremia (from laxative/water overload) | Ion loss from vomiting/laxatives |
| **Cardiac** | QTc prolongation (from hypokalemia), arrhythmias; cardiomyopathy from emetine (ipecac) | Electrolyte disturbances |
| **Endocrine** | Irregular menses, mild cortisol elevation, reduced leptin fluctuation | Binge-purge disruption of energy balance signals |
| **Musculoskeletal** | Russell's sign (dorsal MCP calluses from vomiting induction) | Trauma from teeth on hand |

## Pathology

### Comorbidities

| Comorbidity | Prevalence in BN | Notes |
|:---|:---|:---|
| Major depressive disorder | ~75% | Often secondary to shame and binge-purge cycles |
| Anxiety disorders | ~60–75% | GAD, social anxiety; anxiety frequently precedes binge |
| Substance use disorder | ~30% | Alcohol > stimulants; dopamine overlap |
| Borderline personality disorder | ~25% | Emotional dysregulation, impulsivity overlap |
| Trauma/PTSD | ~30–50% | Childhood trauma is major risk factor |
| Self-harm | ~30% | Impulsivity trait |

### Medical Laboratory Findings

- ↓ K⁺ (hypokalemia) from purging → QTc prolongation on ECG
- ↓ Cl⁻, ↑ HCO₃⁻ (metabolic alkalosis) from vomiting
- ↑ Serum amylase (parotid, not pancreatic isotype)
- Normal BMI/weight — unlike AN
- Normal CBC (unless nutritional compromise)

## Connections

- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — serotonin hypofunction in prefrontal-limbic circuits drives impulse control failure and binge episodes in BN; reduced 5-HT2C satiety signaling; fluoxetine 60 mg (FDA-approved, highest approved SSRI dose for any indication) reduces binge/purge frequency ~50% and is first-line pharmacotherapy.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — dysregulated striatal dopamine reward drives binge-eating reinforcement via NAcc D3R; PET shows ↑ striatal DA release during food cue exposure in BN; altered reward prediction error signaling and impaired D2R-mediated inhibitory control contribute to loss-of-control eating.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — ghrelin is elevated in BN during restriction phases, amplifying hunger drives that trigger binges; post-meal ghrelin suppression is impaired in BN; the ghrelin-NPY axis is central to restriction-binge cycling; ghrelin receptor antagonism is under investigation as adjunct therapy.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — BN involves insula dysfunction (impaired interoceptive satiety signaling), reduced ventral PFC inhibitory control, striatal D3R/D2R reward dysregulation, and ACC conflict monitoring deficits; CBT-BN and fluoxetine both normalize PFC-striatal connectivity on fMRI.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — BN and AN share dietary-restraint → binge/compensatory pathophysiology with body-image distortion; BMI distinguishes (normal in BN, low in AN); ~25% AN patients later develop BN; DSM-5 criterion E excludes BN if AN active; AN carries higher mortality (SMR 5-10x vs 1.5-2x).
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — leptin signals adipose energy stores to hypothalamus; binge-purge cycles blunt leptin fluctuation → impaired satiety sensing; purging reduces leptin acutely despite adequate caloric load; leptin-NPY arcuate axis dysregulation in BN impairs hunger-fullness signaling.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — HPA dysregulation in BN → elevated cortisol during restriction/binge; stress cortisol drives emotional eating and binge triggers; cortisol elevates ghrelin and suppresses leptin → amplifies hunger drives; purging transiently reduces cortisol, reinforcing the cycle.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — Bulimia nervosa and ADHD share impulsivity and reward-circuit dysfunction: childhood ADHD roughly doubles later bulimia risk, with weak prefrontal inhibitory control and dysregulated striatal dopamine underlying both binge eating and impulsive behavior.
- `connects-to` → **[Binge Eating Disorder](../binge-eating-disorder/README.md)** — Bulimia nervosa and binge-eating disorder both feature recurrent loss-of-control binges but differ in the aftermath: BN includes compensatory purging (vomiting, laxatives, exercise) keeping weight near-normal, while BED has binges without purging and trends toward obesity.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — Bulimia nervosa and borderline personality disorder frequently co-occur (~25-30%), sharing impulsivity, affect dysregulation, and self-harm; binge-purge cycles can serve the same emotion-regulation role as BPD impulsivity, and dialectical behavior therapy helps both.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression is among the commonest bulimia comorbidities: shared serotonergic dysfunction underlies both, the shame of binge-purge cycles deepens low mood, and SSRIs (fluoxetine is the only FDA-approved bulimia drug) treat both—though purging can undermine medication absorption.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Purging makes bulimia dangerous to the heart: self-induced vomiting and laxative abuse waste potassium → hypokalemia that prolongs QT and triggers fatal arrhythmia, the leading cause of sudden death in bulimia; ipecac abuse adds a direct cardiomyopathy.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Bulimia and substance use disorders, especially alcohol, frequently co-occur: shared impulsivity and reward-system dysregulation link binge eating and binge drinking, and the combination worsens medical risk and self-harm; integrated treatment of both beats treating either alone.

## Treatment

### Psychological Interventions

**CBT-BN (Cognitive Behavioral Therapy for Bulimia Nervosa):**
- First-line treatment with strongest evidence base
- Fairburn's enhanced CBT (CBT-E): 20 sessions; targets the vicious cycle of dietary restraint → binge → purge → shame
- Core techniques: dietary monitoring/normalization, challenging dietary rules and food fears, addressing perfectionism and low self-esteem
- Response: ~50% of patients achieve abstinence from binge/purge; ~30–40% full remission
- Binge/purge reduction by ~90% in responders

**Interpersonal Psychotherapy (IPT):**
- Equivalent efficacy to CBT-BN at 1-year follow-up; targets interpersonal deficits that drive emotional eating
- Slower initial response than CBT-BN; preferred when interpersonal stressors are dominant

**DBT-based approaches:**
- Dialectical Behavior Therapy skills (particularly distress tolerance, emotion regulation) effective for emotional eating and impulsive purging
- Especially useful with comorbid BPD or self-harm

### Pharmacotherapy

| Agent | Evidence | Dose | FDA-approved |
|:---|:---|:---|:---|
| **Fluoxetine** | Strong (multicenter RCT; ~50% reduction in binge/purge) | **60 mg/day** (note: 3× standard antidepressant dose) | **Yes** — BN only eating disorder with FDA pharmacotherapy |
| Sertraline | Moderate evidence | 100–200 mg | No |
| Topiramate | Moderate (reduces binge/purge but cognitive SE profile limits use) | 100–200 mg | No |
| Naltrexone | Modest evidence for binge reduction (opioid system in binge reinforcement) | 50 mg | No |
| Bupropion | Contraindicated in BN — increased seizure risk from electrolyte imbalances | — | Contraindicated |

**Key principle:** CBT-BN + fluoxetine > either alone; combination is the evidence-based optimum.

### Self-Monitoring and Stepping Down

- Guided self-help CBT (book or app-based) is effective for mild-moderate BN; step up to therapist-led CBT-BN for moderate-severe
- Dietitian involvement for meal planning and nutrition normalization
- Medical monitoring (electrolytes, ECG if hypokalemia) as needed
- Dental care (remineralization, pH management) to slow enamel erosion

[^fairburn-2008-cbt-eating-disorders]: Fairburn CG. *Cognitive Behavior Therapy and Eating Disorders.* Guilford Press; 2008.
[^kaye-2008-bn-neurobiology]: Kaye WH, Fudge JL, Paulus M. New insights into symptoms and neurocircuit function of anorexia nervosa. *Nat Rev Neurosci.* 2009;10(8):573-584. [doi:10.1038/nrn2682](https://doi.org/10.1038/nrn2682) · [PubMed 19603056](https://pubmed.ncbi.nlm.nih.gov/19603056/)
[^hadigan-1995-fluoxetine-bn]: Fluoxetine Bulimia Nervosa Collaborative Study Group. Fluoxetine in the treatment of bulimia nervosa. *Arch Gen Psychiatry.* 1992;49(2):139-47. [PubMed 1550466](https://pubmed.ncbi.nlm.nih.gov/1550466/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
