---
schema: human-scale-entry/v1
id: social-anxiety-disorder
name: Social Anxiety Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Social anxiety disorder (12% lifetime) involves amygdala hyperreactivity to social threat and striatal dopamine deficit impairing social reward; first-line: SSRIs/SNRIs + CBT with social exposure; β-blockers for performance-only type; MAOIs for severe refractory cases."
aliases: ["social anxiety disorder", "social phobia", "SAD", "performance anxiety", "LSAS", "Liebowitz Social Anxiety Scale", "social fear", "public speaking anxiety"]
sources:
  - id: liebowitz-1987-sad-scale
    type: peer-reviewed
    cite: "Liebowitz MR. Social phobia. Mod Probl Pharmacopsychiatry. 1987;22:141-173."
    pmid: "2885745"
  - id: stein-2008-sad-review
    type: peer-reviewed
    cite: "Stein MB, Stein DJ. Social anxiety disorder. Lancet. 2008;371(9618):1115-1125."
    doi: "10.1016/S0140-6736(08)60488-2"
    pmid: "18374843"
    url: "https://doi.org/10.1016/S0140-6736(08)60488-2"
    accessed: "2026-06-08"
  - id: goldin-2010-mbsr-sad
    type: peer-reviewed
    cite: "Goldin PR, Gross JJ. Effects of mindfulness-based stress reduction (MBSR) on emotion regulation in social anxiety disorder. Emotion. 2010;10(1):83-91."
    doi: "10.1037/a0018441"
    pmid: "20141305"
    url: "https://doi.org/10.1037/a0018441"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Reduced SERT binding in amygdala and striatum in SAD; SSRIs (paroxetine, sertraline FDA-approved; escitalopram, venlafaxine XR evidence-based) are first-line pharmacotherapy; serotonergic modulation of amygdala reduces social threat hyperreactivity and improves social function."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Reduced D2 binding in striatum in SAD (SPECT) → impaired social reward processing and anhedonia; dopaminergic deficits distinguish SAD from other anxiety disorders; blunted approach motivation reinforces avoidance; MAOIs highly effective possibly via dopamine disinhibition."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Adrenergic surge in social situations causes blushing, tremor, and sweating; propranolol (β1 antagonist) reduces somatic performance anxiety; NE amplifies amygdala reactivity to social threat; venlafaxine XR (SNRI) addresses both NE hyperarousal and serotonin dysregulation."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Benzodiazepines (clonazepam) are effective for SAD but dependency concerns limit use; GABAergic deficits in limbic circuits may impair amygdala threat dampening in social situations; pregabalin and gabapentin show evidence for SAD as alternative GABAergic treatments."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "SAD features BLA hyperreactivity to social threat cues (angry/contemptuous faces); reduced amygdala habituation; reduced vmPFC-amygdala inhibition; striatal hypoactivation during social reward; CBT normalizes amygdala-vmPFC functional connectivity on fMRI."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Reduced OTR in BLA in SAD decreases OT-mediated social threat dampening; low OT tone associates with gaze avoidance and social approach deficits; intranasal OT (24 IU) enhances social salience and attention to eyes and is in Phase 2 trials as CBT augmentation for SAD."
---

# Social Anxiety Disorder

## Overview

**Social anxiety disorder (SAD)**, formerly social phobia, is characterized by intense, persistent fear of social situations where one may be scrutinized, embarrassed, or judged negatively. It is the **most common anxiety disorder** by lifetime prevalence in the US and one of the most common psychiatric conditions globally.

**Epidemiology:**
- Lifetime prevalence: ~12.1% (US); 7–13% globally; 12-month prevalence ~7.1%
- Female-to-male ratio: 1.4:1 (less pronounced than other anxiety disorders); males more likely to seek treatment
- Onset: typically adolescence (13–17 years); strongly linked to behavioral inhibition temperament in childhood
- Course: chronic if untreated (median duration 25+ years); spontaneous remission rare (<20% at 12 years)
- High comorbidity: MDD (>50% lifetime); AUD (self-medication 20-25%); other anxiety disorders

**DSM-5 Criteria:**
1. Marked fear/anxiety about social situations where one may be scrutinized
2. Fear of acting in ways that will be humiliating or embarrassing, or showing anxiety symptoms
3. Social situations almost always provoke fear/anxiety
4. Social situations avoided or endured with intense distress
5. Fear out of proportion to actual threat posed by situation
6. Duration ≥6 months
7. Significant distress or functional impairment
8. Not due to substances, medical conditions, or another mental disorder

**Performance-only specifier:** Fear limited to performing or speaking in public; distinct neural profile (more anterior temporal activation, less vmPFC suppression failure); responds to propranolol.

**Assessment — LSAS (Liebowitz Social Anxiety Scale)** [^liebowitz-1987-sad-scale]: 24-item scale rating fear and avoidance across social interaction and performance situations; LSAS ≥60 indicates moderate SAD; ≥ 90 very severe; widely used in clinical trials.

## Structure

### Neuroanatomy of social fear

**Amygdala hyperreactivity:**
- fMRI studies consistently show exaggerated BOLD signal in BLA in response to angry, contemptuous, or neutral faces in SAD patients vs. controls [^stein-2008-sad-review]
- **Reduced habituation:** Normal amygdala response to repeated neutral faces decreases (habituation); in SAD, amygdala remains hyperactivated to faces over repeated exposure — the abnormal lack of habituation is a key biomarker
- Faces presented outside conscious awareness (subliminal) still activate amygdala in SAD — suggests automatic (not effortful) threat processing

**Prefrontal-amygdala imbalance:**
- vmPFC sends GABAergic projections to amygdala intercalated cells → dampens CeA output → safety signal
- In SAD: reduced vmPFC activation during social challenge → inadequate amygdala suppression → persistent threat appraisal
- Successful CBT treatment restores vmPFC → amygdala suppression on fMRI

**Striatal dopamine deficit:**
- SPECT imaging: reduced **D2 receptor binding** in caudate and putamen in SAD vs. controls — a distinctive finding not seen in GAD or panic disorder
- Reduced dopamine synthesis in social reward circuits (VTA → striatum) → social situations less inherently rewarding → anhedonia → avoidance is reinforced
- **Dopaminergic social reward learning** impaired — patients with SAD fail to update expectations toward positive social outcomes → negative social prediction errors dominate
- This may explain the striking efficacy of MAOIs (phenelzine) in SAD — MAOIs increase dopamine (and serotonin, NE) by blocking monoamine oxidase

**Serotonin system:**
- Reduced serotonin transporter (SERT/SLC6A4) binding in amygdala and striatum on SPECT
- Reduced 5-HT1A autoreceptors in raphe nuclei
- SSRIs are first-line treatment — normalize SERT binding with sustained treatment
- Serotonin modulates amygdala reactivity to social threat and approach/avoidance balance

### Self-focused attention model

David Clark and Adrian Wells' cognitive model explains SAD maintenance through self-focused processing:

1. **Social situation triggers threat perception**
2. **Attention shifts inward:** Patient monitors own perceived inadequacy (blushing, shaking, saying something stupid) rather than processing social cues from others
3. **Safety behaviors:** Avoiding eye contact, over-preparing, speaking briefly, avoiding speaking at all → prevents disconfirmation of feared social catastrophe
4. **Post-event processing:** Rumination after social events — replaying perceived failures → negative self-appraisal → maintenance of fear
5. **Social performance worsens** due to attention being consumed by self-monitoring rather than engaging with the situation

CBT targets each step: eliminating safety behaviors, shifting attention outward, cognitive restructuring of core beliefs ("I am fundamentally inadequate in social situations").

## Function

### Behavioral inhibition and neurodevelopment

- **Behavioral inhibition (BI):** Temperamental trait identified in infancy/toddlerhood — fearful, avoidant, shy with novelty; strongest temperamental predictor of SAD (odds ratio ~5-7)
- BI is mediated by amygdala hypersensitivity and reduced vmPFC regulation; familial heritability ~50%
- Adverse childhood experiences (peer victimization, embarrassing public events, parental overprotection) interact with BI to convert temperament into disorder
- Neuroimaging: adolescents with BI show structural and functional amygdala-vmPFC differences even before meeting SAD criteria

### Social reward and dopamine

The unique **dopaminergic social reward deficit** in SAD has clinical implications:
- SAD patients show blunted anticipatory pleasure for social events (anhedonia) even when they "know" an event will be positive
- Reduced dopamine → reduced approach motivation → avoidance reinforced by escape from anxiety (negative reinforcement) rather than choice
- This helps explain why CBT "behavioral experiments" (approach without avoidance) are especially difficult for SAD patients — they must act against both anxiety and reduced reward motivation simultaneously

## Pathology

### Comorbidity patterns

| Comorbidity | Prevalence in SAD | Notes |
|:---|:---|:---|
| **Major Depressive Disorder** | ~50% lifetime | SAD typically precedes MDD; social isolation → depression |
| **Alcohol Use Disorder** | ~20–25% | Self-medication; alcohol reduces social anxiety acutely |
| **GAD** | ~35–45% | Overlapping worry; distinguish by focus (social vs. general) |
| **Other anxiety disorders** | ~40% | Specific phobia, panic disorder |
| **Body Dysmorphic Disorder** | ~10–20% | Overlapping shame/social avoidance; treatment similar |

### Treatment

**Cognitive-Behavioral Therapy:**
- **Efficacy:** 56–76% response rate; equivalent to pharmacotherapy short-term; superior long-term; MBSR shows equivalent results in RCTs for SAD [^goldin-2010-mbsr-sad]
- **Clark's CBT model components:**
  - Psychoeducation: the self-focused attention model
  - Video feedback: watching yourself on video to correct distorted self-image
  - Behavioral experiments: entering feared situations without safety behaviors
  - Cognitive restructuring: challenging core beliefs ("I am boring/stupid/blushing visibly")
  - Social skills training (when genuine deficit exists, not just distorted appraisal)
- **Mindfulness-based approaches:** MBSR reduces SAD severity; shifts attention from self-monitoring to outward engagement

**Pharmacotherapy:**

| Medication | Class | Notes |
|:---|:---|:---|
| Paroxetine | SSRI | FDA-approved for SAD; also reduces anticipatory anxiety |
| Sertraline | SSRI | FDA-approved; well-tolerated; flexible dosing |
| Venlafaxine XR | SNRI | FDA-approved; addresses both serotonin and NE components |
| Escitalopram | SSRI | Off-label; strong evidence; good tolerability |
| Phenelzine | MAOI | Most effective pharmacotherapy (~75% response); limited by dietary restrictions, orthostasis; reserved for SSRI-refractory cases |
| Clonazepam | BZD | Effective; short-term only; dependency risk |
| Propranolol | β-blocker | Performance anxiety only; not generalized SAD; reduces tremor, blushing, HR |
| Pregabalin | Calcium channel α2δ | Evidence in RCTs; option for SSRI non-responders |

**D-cycloserine augmentation:**
- Partial NMDA agonist given before exposure sessions → enhances extinction consolidation → faster response to CBT; RCTs show benefit when given to augment specific exposure trials (not daily)

## Connections

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — reduced SERT binding in amygdala and striatum in SAD; SSRIs (paroxetine, sertraline FDA-approved; escitalopram and venlafaxine XR evidence-based) are first-line; serotonergic modulation of amygdala reduces social threat hyperreactivity and improves approach behavior.

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — reduced D2 binding in striatum in SAD (SPECT) → impaired social reward processing and social anhedonia; dopaminergic deficits distinguish SAD from other anxiety disorders; blunted approach motivation reinforces avoidance; MAOIs are highly effective possibly via dopamine disinhibition.

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — adrenergic surge in social situations causes blushing, tremor, and sweating; propranolol (β1 antagonist) reduces somatic performance anxiety; NE amplifies amygdala reactivity to social threat; venlafaxine XR (SNRI) addresses both NE hyperarousal and serotonin dysregulation.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — benzodiazepines (clonazepam) are effective for SAD but dependency concerns limit use; GABAergic deficits in limbic circuits may impair amygdala threat dampening; pregabalin and gabapentin show evidence for SAD as alternative GABAergic treatments.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — SAD features BLA hyperreactivity to social threat cues and reduced amygdala habituation; striatal hypoactivation during social reward; reduced vmPFC-amygdala inhibition; CBT with behavioral experiments normalizes amygdala-vmPFC connectivity on task-based fMRI.

- `connects-to` → **[Oxytocin](../../../03-molecular/oxytocin/README.md)** — reduced OTR expression in the BLA and CeA in SAD diminishes OT-mediated dampening of amygdala social threat responses; low endogenous OT associates with gaze avoidance, reduced eye contact, and social approach motivation deficits; intranasal OT (24 IU) enhances social salience, attention to eye regions, and reduces skin conductance to angry faces; in Phase 2 trials as CBT augmentation.

[^liebowitz-1987-sad-scale]: Liebowitz MR. Social phobia. *Mod Probl Pharmacopsychiatry.* 1987;22:141-173. [PubMed 2885745](https://pubmed.ncbi.nlm.nih.gov/2885745/)
[^stein-2008-sad-review]: Stein MB, Stein DJ. Social anxiety disorder. *Lancet.* 2008;371(9618):1115-1125. [doi:10.1016/S0140-6736(08)60488-2](https://doi.org/10.1016/S0140-6736(08)60488-2) · [PubMed 18374843](https://pubmed.ncbi.nlm.nih.gov/18374843/)
[^goldin-2010-mbsr-sad]: Goldin PR, Gross JJ. Effects of mindfulness-based stress reduction (MBSR) on emotion regulation in social anxiety disorder. *Emotion.* 2010;10(1):83-91. [doi:10.1037/a0018441](https://doi.org/10.1037/a0018441) · [PubMed 20141305](https://pubmed.ncbi.nlm.nih.gov/20141305/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
