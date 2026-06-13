---
schema: human-scale-entry/v1
id: cannabis-use-disorder
name: Cannabis Use Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Cannabis use disorder (~9% of users) results from THC-driven CB1R desensitization/downregulation; withdrawal: anxiety, irritability, insomnia, appetite loss. Prevalence rising with legalization. No FDA-approved pharmacotherapy; CBT and motivational enhancement are first-line."
aliases: ["cannabis use disorder", "CUD", "marijuana use disorder", "cannabis dependence", "THC dependence", "cannabis withdrawal", "marijuana addiction"]
cross_links:
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "Repeated THC → CB1R desensitization (GRK3/β-arrestin) and downregulation → reduced endocannabinoid tone → tolerance; withdrawal reflects endocannabinoid deficiency: anxiety, irritability, insomnia, appetite loss; CB1R recovery requires 2-4 weeks abstinence."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "THC → CB1R on VTA interneurons → DA disinhibition → NAcc dopamine surge; chronic use → D2R downregulation and blunted NAcc response to natural rewards; PET shows reduced striatal dopamine in chronic cannabis users — mirroring other substance use disorders."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "CB1R on GABAergic interneurons mediates THC's disinhibitory effects; chronic THC → CB1R internalization → altered E/I balance; PFC GABA deficits correlate with impaired inhibitory control; MRS shows reduced GABA in cannabis-dependent users."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Chronic THC reduces hippocampal BDNF in adolescent models, impairing synaptic plasticity; adolescent cannabis use is associated with greater BDNF-related hippocampal vulnerability; abstinence partially restores BDNF-dependent plasticity over weeks to months."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Chronic heavy cannabis use reduces hippocampal and amygdala gray matter; PFC thinning correlates with cognitive impairment; CB1R downregulation on PET persists 4+ weeks after abstinence; adolescent-onset use causes greater structural brain changes than adult onset."
  - target: 01-human/07-system/internet-gaming-disorder
    relation: connects-to
    note: "Cannabis use disorder and internet gaming disorder are the substance and behavioral ends of one addiction spectrum: both converge on VTA-NAcc dopamine surges, D2-receptor downregulation, and weakened prefrontal control, and both lack approved drugs — treated instead with CBT."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Heavy, high-THC, low-CBD cannabis use is a robust risk factor for psychosis and schizophrenia, plausibly by disrupting cortical dopamine signaling; COMT Val158Met moderates vulnerability, and ~10-15% of first-episode psychosis is cannabis-attributable in high-use regions."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Smoked cannabis irritates the airways like tobacco smoke, causing chronic bronchitis (cough, sputum, wheeze) from combustion toxicants rather than the airflow obstruction of COPD; vaporization at lower temperatures or non-smoked routes reduces this airway toxicant exposure."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Cannabis and alcohol are the two most co-used substances: both engage the mesolimbic dopamine reward pathway and GABAergic signalling, frequently co-occur, and concurrent use compounds cognitive and motor impairment; both follow a craving-tolerance-withdrawal course."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Cannabis and opioid use disorders share dopaminergic reward circuitry and a craving-tolerance-withdrawal course; the endocannabinoid and opioid systems interact, fueling debate over whether cannabis substitutes for or precedes opioid use, with mixed evidence on overdose."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Cannabis and anxiety have a bidirectional link: people use cannabis to self-medicate anxiety, yet heavy use and withdrawal can worsen it, and high-THC/low-CBD products are most anxiogenic; CB1 signalling modulates amygdala fear circuits underlying generalized anxiety disorder."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Cannabis and stimulant use disorders commonly co-occur and share a mesolimbic dopamine reward pathway but differ in course: cannabis withdrawal is mild and protracted while stimulants produce intense crash and craving—polysubstance use worsens prognosis."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Cannabis use disorder is tightly linked to bipolar disorder: among its commonest comorbidities, it can precipitate manic or psychotic episodes and worsens mood-episode frequency—so heavy use in a young person with mood instability warrants caution."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Cannabis acts on CB1 receptors densest on neurons: THC mimics endocannabinoids that normally tune synaptic release, so chronic exposure downregulates CB1 signaling—especially harmful in the adolescent brain, where it can durably alter neural circuit maturation."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Cannabis can trigger panic attacks: high-THC use, especially in the inexperienced, provokes acute anxiety, paranoia and panic, and chronic use is associated with anxiety disorders—so cannabis is both a cause and a sometimes self-medicated comorbidity of panic."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Cannabis use disorder and depression are bidirectionally linked: heavy cannabis use is associated with higher rates of depression, while some use cannabis to self-medicate low mood—a relationship where cause and consequence are hard to separate."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "PTSD and cannabis use disorder are closely intertwined: many with PTSD use cannabis to blunt hyperarousal and insomnia, raising the risk of dependence, while withdrawal can worsen the symptoms it masks—so cannabis is a common but double-edged self-treatment in PTSD."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Cannabis stresses the heart and vessels: THC raises heart rate and blood pressure acutely and is linked to myocardial infarction, arrhythmia and cannabis arteritis, so heavy use carries real cardiovascular risk despite cannabis's benign reputation."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Cannabis and sleep have a two-edged relationship: it may shorten sleep latency acutely but suppresses REM and, on withdrawal, causes rebound insomnia and vivid dreams—so dependence and disturbed sleep reinforce each other in cannabis use disorder."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Cannabis perturbs glutamate signaling in ways tied to psychosis: THC's action on CB1 receptors modulates glutamate release in cortical and limbic circuits, and this disruption helps explain why heavy adolescent use raises schizophrenia risk."
sources:
  - id: hasin-2015-cannabis-disorder
    type: peer-reviewed
    cite: "Hasin DS, Saha TD, Kerridge BT, et al. Prevalence of marijuana use disorders in the United States between 2001-2002 and 2012-2013. JAMA Psychiatry. 2015;72(12):1235-1242."
    doi: "10.1001/jamapsychiatry.2015.1858"
    pmid: "26502112"
    url: "https://doi.org/10.1001/jamapsychiatry.2015.1858"
  - id: budney-2004-cannabis-withdrawal
    type: peer-reviewed
    cite: "Budney AJ, Moore BA, Vandrey RG, Hughes JR. The time course and significance of cannabis withdrawal. J Abnorm Psychol. 2003;112(3):393-402."
    doi: "10.1037/0021-843X.112.3.393"
    pmid: "12943018"
    url: "https://doi.org/10.1037/0021-843X.112.3.393"
---

# Cannabis Use Disorder

## Overview

**Cannabis Use Disorder (CUD)** is a DSM-5 substance use disorder characterized by problematic use of cannabis (marijuana, hashish, or synthetic cannabinoids) leading to clinically significant impairment or distress. It is the most prevalent illicit substance use disorder globally, driven by widespread cannabis use and increasing potency of commercial preparations (THC content of retail cannabis rose from ~4% in 1995 to >15–20% in 2020 in regulated markets).

**Epidemiology:**
- CUD affects approximately **9% of lifetime cannabis users** (conditional risk); rising with higher-potency cannabis exposure
- 12-month prevalence in US adults: ~1.5% (rising with legalization); ~22 million Americans past-month users
- Rates higher in daily/near-daily users: ~35–50% develop CUD
- Adolescent users have 4× the risk of developing CUD compared to adult initiators
- Male:female ratio ~2:1; declining gap in younger cohorts
- Comorbidity: psychotic disorders (3-fold elevated CUD prevalence), depression (3×), anxiety disorders (2×), other SUDs

**Policy context:** As of 2025, cannabis is legal in 24 US states + DC for recreational use; cannabis use disorder diagnosis is unaffected by legality — frequency, quantity, and control impairment determine diagnosis. Legalization has been associated with increased treatment presentations for CUD.

**Key pharmacological background:** THC (Δ9-tetrahydrocannabinol) is the primary psychoactive cannabinoid; it acts as a **partial agonist at CB1R and CB2R**. CBD (cannabidiol) is non-psychoactive, does not bind CB1R appreciably, and modulates TRPV1, GPR55, 5-HT1A, and has anticonvulsant, anxiolytic, and anti-inflammatory properties.

## Structure

### DSM-5 Criteria (≥2 of 11 in 12 months)

| Criterion | Domain |
|:---|:---|
| Larger amounts or longer period than intended | Loss of control |
| Unsuccessful efforts to cut down | Loss of control |
| Much time spent using/recovering | Salience |
| Craving | Motivation |
| Role obligations failure | Harmful use |
| Continued despite social problems | Harmful use |
| Giving up activities | Social withdrawal |
| Hazardous use (e.g., driving high) | Risk-taking |
| Continued despite psychological/physical harm | Persistence despite harm |
| Tolerance | Neuroadaptation |
| Withdrawal | Neuroadaptation |

**Severity:** Mild (2-3), Moderate (4-5), Severe (≥6)

**Cannabis Withdrawal Syndrome (DSM-5, included 2013):**
Develops within 24-72 hours of heavy use cessation; peaks at days 2-4; resolves over 1-2 weeks [^budney-2004-cannabis-withdrawal]:
- Irritability, anger, aggressiveness
- Nervousness/anxiety
- Sleep difficulty (insomnia, vivid/disturbing dreams)
- Decreased appetite/weight loss
- Restlessness
- Depressed mood
- Physical symptoms: abdominal pain, sweating, shakiness, headache

### Potency and Harm Profile

| Product | Typical THC% | CUD risk | Acute harm |
|:---|:---|:---|:---|
| Traditional herbal (flower) | 10–20% | Moderate | Anxiety, paranoia |
| Concentrates (wax, shatter, dabs) | 60–90% | High | Psychosis risk ↑ |
| High-THC flower ("craft") | 25–35% | High | Anxiety, dependence |
| CBD-dominant product | <0.3% THC | Low | Minimal |
| Edibles | Variable; delayed onset | Moderate-high (dosing errors) | Acute toxicity risk |

## Function

### Neurobiology of THC Reward and Dependence

**Acute THC effects on reward circuits:**
1. THC → CB1R (partial agonist) on VTA GABAergic interneurons → DSI → disinhibition of VTA DA neurons → ↑ NAcc DA release → euphoria and positive reinforcement
2. THC → CB1R on cortical glutamatergic inputs to VTA → reduced glutamate → further modulation of DA firing
3. THC → hippocampal CB1R → impaired memory encoding (temporary episodic memory disruption)
4. THC → cerebellar CB1R → impaired motor coordination, timing

**Chronic THC neuroadaptation:**
1. **CB1R desensitization:** GRK3 phosphorylates CB1R → β-arrestin 2 recruitment → internalization; reduces surface CB1R density → tolerance
2. **CB1R downregulation:** Reduced CB1R mRNA and protein in heavy users; measurable by PET radioligand imaging (↓ [¹¹C]OMAR binding)
3. **Dopamine deficits:** ↓ D2R and ↓ DAT; reduced NAcc DA release to non-cannabis rewards → blunted hedonic response → motivational deficits
4. **PFC-mediated inhibitory control failure:** CB1R downregulation + reduced GABA → impaired PFC E/I balance → difficulty stopping cannabis use

### Psychosis Risk

Heavy cannabis use, especially high-THC/low-CBD varieties, is associated with increased psychosis risk:
- Odds ratio for psychotic disorder with any cannabis use: ~1.4; heavy use: ~3.4; high-potency daily use: ~5×
- Mechanism: Excess CB1R activation in PFC → disrupted PFC-controlled dopamine signaling → reduced cortical DA; subcortical DA excess → positive symptoms
- COMT Val158Met genotype moderates cannabis-psychosis link (Val carriers more vulnerable)
- 10–15% of first-episode psychosis cases attributable to cannabis in high-prevalence areas (Netherlands data)

### Cognitive Effects

Chronic cannabis use impairs:
- Episodic memory: hippocampal CB1R-mediated; significant with daily use; improves with abstinence (months) but may not fully normalize with very early onset
- Attention and processing speed: dose-dependent impairment; PFC-driven
- Executive function: inhibitory control, planning — associated with PFC gray matter thinning on MRI
- Psychomotor speed: relevant for driving impairment (THC-impaired driving doubles accident risk)

## Pathology

### Medical Complications

| System | Complication | Mechanism |
|:---|:---|:---|
| Pulmonary | Chronic bronchitis, cannabinoid hyperemesis syndrome | Smoke irritants; CB1R in hypothalamus/vagus |
| Cardiovascular | Tachycardia (acute), rare MI/stroke in young | Sympathomimetic; CB1R cardiovascular effects |
| Psychiatric | Psychosis, depression, anxiety, exacerbation of bipolar | Dopamine disruption; CB1R-mediated |
| Neurodevelopmental | IQ reduction (ongoing debate), gray matter loss | Adolescent CNS exposure to THC |
| Reproductive | Reduced sperm motility, altered menstrual cycle | CB1R in reproductive system |
| Fetal | Low birth weight, NICU admission | Placental CB1R; THC crosses placenta |

### Cannabinoid Hyperemesis Syndrome (CHS)

Paradoxical syndrome in heavy long-term users: cyclic vomiting relieved by hot baths; mechanism involves TRPV1 desensitization reversal and CB1R-mediated hypothalamic temperature dysregulation; resolved by cannabis cessation; hot showers provide acute symptom relief; topical capsaicin cream (TRPV1 activation) reduces vomiting episodes.

### Treatment

**No FDA-approved pharmacotherapy for CUD.** [^hasin-2015-cannabis-disorder]

**Psychosocial treatments (evidence-based):**
- **Motivational Enhancement Therapy (MET):** 2-4 sessions; explores ambivalence; most studied for CUD; efficacy improves when combined with CBT
- **CBT (Cognitive Behavioral Therapy):** Coping skills, trigger management, relapse prevention; 6-12 sessions; improves abstinence rates
- **Contingency Management (CM):** Voucher-based incentives for negative urine screens; most effective for verified abstinence; works best when added to MET/CBT

**Pharmacological trials (off-label/investigational):**
- **Gabapentin:** Reduced withdrawal symptoms and cannabis use in a small RCT; VGCC α2δ mechanism reduces anxiety/sleep disturbance
- **N-acetylcysteine (NAC):** Glutamate modulator; reduced cannabis use in adolescents in one RCT; failed in adults; ongoing trials
- **Nabiximols (THC:CBD 1:1):** Reduced withdrawal severity; "cannabis agonist" replacement therapy concept; available in some countries
- **CBD:** Reduces cue-induced craving and anxiety; ongoing trials for CUD; mechanism includes 5-HT1A, TRPV1, GPR55

**Harm reduction:**
- Switching from high-THC to lower-THC or CBD-dominant products
- Avoiding smoking; vaporization at lower temperatures reduces combustion toxicants
- Setting use limits; avoiding morning/daily use patterns
- Not driving while impaired

## Connections

- `connects-to` → **[Endocannabinoid System](../../../03-molecular/endocannabinoid/README.md)** — repeated THC exposure → CB1R desensitization (GRK3/β-arrestin) and downregulation → reduced endocannabinoid tone → tolerance; withdrawal reflects rebound endocannabinoid deficiency: anxiety, irritability, insomnia, appetite loss; CB1R recovery requires 2-4 weeks of abstinence.

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — THC → CB1R on VTA interneurons → DA disinhibition → NAcc dopamine surge; chronic use → D2R downregulation and blunted NAcc response to natural rewards; PET shows reduced striatal dopamine in chronic users — pattern shared with other substance use disorders.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — CB1R on GABAergic interneurons mediates THC's disinhibitory effects; chronic THC → CB1R internalization on GABA terminals → altered E/I balance; GABA deficits in PFC with chronic use correlate with impaired inhibitory control in CUD.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — chronic THC exposure reduces hippocampal BDNF in adolescent models, impairing synaptic plasticity; adolescent cannabis use is associated with greater BDNF-related hippocampal vulnerability; abstinence partially restores BDNF-dependent plasticity over weeks to months.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — chronic heavy cannabis use reduces hippocampal and amygdala gray matter volume; PFC thinning correlates with cognitive impairment; CB1R downregulation measurable by PET persists 4+ weeks after abstinence; adolescent-onset use associated with greater structural brain changes than adult onset.

- `connects-to` → **[Internet Gaming Disorder](../internet-gaming-disorder/README.md)** — Cannabis use disorder and internet gaming disorder are the substance and behavioral ends of one addiction spectrum: both converge on VTA-NAcc dopamine surges, D2-receptor downregulation, and weakened prefrontal control, and both lack approved drugs — treated instead with CBT.

- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Heavy, high-THC, low-CBD cannabis use is a robust risk factor for psychosis and schizophrenia, plausibly by disrupting cortical dopamine signaling; COMT Val158Met moderates vulnerability, and ~10-15% of first-episode psychosis is cannabis-attributable in high-use regions.

- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Smoked cannabis irritates the airways like tobacco smoke, causing chronic bronchitis (cough, sputum, wheeze) from combustion toxicants rather than the airflow obstruction of COPD; vaporization at lower temperatures or non-smoked routes reduces this airway toxicant exposure.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Cannabis and alcohol are the two most co-used substances: both engage the mesolimbic dopamine reward pathway and GABAergic signalling, frequently co-occur, and concurrent use compounds cognitive and motor impairment; both follow a craving-tolerance-withdrawal course.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Cannabis and opioid use disorders share dopaminergic reward circuitry and a craving-tolerance-withdrawal course; the endocannabinoid and opioid systems interact, fueling debate over whether cannabis substitutes for or precedes opioid use, with mixed evidence on overdose.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Cannabis and anxiety have a bidirectional link: people use cannabis to self-medicate anxiety, yet heavy use and withdrawal can worsen it, and high-THC/low-CBD products are most anxiogenic; CB1 signalling modulates amygdala fear circuits underlying generalized anxiety disorder.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Cannabis and stimulant use disorders commonly co-occur and share a mesolimbic dopamine reward pathway but differ in course: cannabis withdrawal is mild and protracted while stimulants produce intense crash and craving—polysubstance use worsens prognosis.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Cannabis use disorder is tightly linked to bipolar disorder: among its commonest comorbidities, it can precipitate manic or psychotic episodes and worsens mood-episode frequency—so heavy use in a young person with mood instability warrants caution.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Cannabis acts on CB1 receptors densest on neurons: THC mimics endocannabinoids that normally tune synaptic release, so chronic exposure downregulates CB1 signaling—especially harmful in the adolescent brain, where it can durably alter neural circuit maturation.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Cannabis can trigger panic attacks: high-THC use, especially in the inexperienced, provokes acute anxiety, paranoia and panic, and chronic use is associated with anxiety disorders—so cannabis is both a cause and a sometimes self-medicated comorbidity of panic.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Cannabis use disorder and depression are bidirectionally linked: heavy cannabis use is associated with higher rates of depression, while some use cannabis to self-medicate low mood—a relationship where cause and consequence are hard to separate.
- `connects-to` → **[PTSD](../ptsd/README.md)** — PTSD and cannabis use disorder are closely intertwined: many with PTSD use cannabis to blunt hyperarousal and insomnia, raising the risk of dependence, while withdrawal can worsen the symptoms it masks—so cannabis is a common but double-edged self-treatment in PTSD.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Cannabis stresses the heart and vessels: THC raises heart rate and blood pressure acutely and is linked to myocardial infarction, arrhythmia and cannabis arteritis, so heavy use carries real cardiovascular risk despite cannabis's benign reputation.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Cannabis and sleep have a two-edged relationship: it may shorten sleep latency acutely but suppresses REM and, on withdrawal, causes rebound insomnia and vivid dreams—so dependence and disturbed sleep reinforce each other in cannabis use disorder.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Cannabis perturbs glutamate signaling in ways tied to psychosis: THC's action on CB1 receptors modulates glutamate release in cortical and limbic circuits, and this disruption helps explain why heavy adolescent use raises schizophrenia risk.

[^hasin-2015-cannabis-disorder]: Hasin DS, Saha TD, Kerridge BT, et al. Prevalence of marijuana use disorders in the United States between 2001-2002 and 2012-2013. *JAMA Psychiatry.* 2015;72(12):1235-1242. [doi:10.1001/jamapsychiatry.2015.1858](https://doi.org/10.1001/jamapsychiatry.2015.1858) · [PubMed 26502112](https://pubmed.ncbi.nlm.nih.gov/26502112/)
[^budney-2004-cannabis-withdrawal]: Budney AJ, Moore BA, Vandrey RG, Hughes JR. The time course and significance of cannabis withdrawal. *J Abnorm Psychol.* 2003;112(3):393-402. [doi:10.1037/0021-843X.112.3.393](https://doi.org/10.1037/0021-843X.112.3.393) · [PubMed 12943018](https://pubmed.ncbi.nlm.nih.gov/12943018/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
