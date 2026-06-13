---
schema: human-scale-entry/v1
id: internet-gaming-disorder
name: Internet Gaming Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Internet gaming disorder (ICD-11 6C51; DSM-5 Section III) shares behavioral addiction neurobiology with gambling disorder: VTA-NAcc dopamine, OFC hyperactivation, D2R hypofunction, impaired inhibitory control. Prevalence 2-5% of gamers. No approved pharmacotherapy."
aliases: ["internet gaming disorder", "IGD", "gaming disorder", "video game addiction", "gaming addiction", "compulsive gaming", "problematic gaming"]
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Gaming activates VTA-NAcc dopamine via achievement and reward signals; PET shows reduced striatal D2R availability in IGD — paralleling gambling disorder and substance use disorders; dopamine cue reactivity to game stimuli resembles drug cue reactivity in fMRI."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "IGD and gambling disorder share behavioral addiction neurobiology: VTA-NAcc dopamine dysregulation, OFC hyperactivation to cues, vmPFC hypoactivation, impaired PFC-striatum inhibitory control, and D2R hypofunction on PET; both respond to CBT and motivational enhancement."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "IGD features OFC hyperactivation to game cues, vmPFC hypoactivation, reduced ventral striatum response to non-gaming rewards, and diminished ACC impulse control; structural MRI shows reduced gray matter in dlPFC and OFC — consistent with impaired top-down inhibitory control."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "IGD is associated with altered BDNF expression in prefrontal circuits; behavioral addiction models show BDNF-TrkB plasticity changes similar to substance use; BDNF Val66Met SNP has been associated with IGD vulnerability in genetic association studies."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin dysregulation contributes to impulsivity and compulsivity in IGD; 5-HT2C hypofunction reduces satiety signaling after game play; SSRIs show modest evidence for IGD with comorbid OCD or depression; impulsivity is a shared serotonin-related risk trait."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Internet gaming disorder is the behavioral mirror of substance addictions like cannabis use disorder: variable-ratio game rewards drive the same VTA-NAcc dopamine and D2-receptor hypofunction seen with drugs, with shared OFC cue-reactivity and prefrontal control deficits."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression is the most common IGD comorbidity (~50%), and most patients game largely to escape low mood, anxiety, or loneliness; this negative-reinforcement (escape) pattern predicts more severe disorder and worse outcomes, and SSRIs help mainly when depression is the driver."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Bupropion, a norepinephrine-dopamine reuptake inhibitor, reduced gaming in small controlled trials, fitting IGD's hypodopaminergic reward biology; noradrenergic tone also supports the prefrontal attention and impulse control weakened in gaming disorder."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "ADHD is one of the strongest correlates of internet gaming disorder: deficits in dopaminergic reward processing and inhibitory control predispose to compulsive gaming, the two are highly comorbid, and IGD severity tracks ADHD symptom load—stimulant treatment may reduce gaming."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Social anxiety drives internet gaming disorder: online games offer socially safe, avoidant interaction, so socially anxious people retreat into gaming, which deepens real-world avoidance in a reinforcing loop; SAD is a common IGD comorbidity and a target for combined treatment."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Internet gaming disorder and anxiety reinforce each other: gaming is short-term escape from worry, while excessive use, sleep loss and functional decline heighten anxiety; generalized anxiety disorder commonly co-occurs with IGD and shapes relapse during attempts to cut down."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Internet gaming disorder and stimulant use disorder converge on the mesolimbic dopamine reward circuit: gaming's variable rewards drive compulsive use like an addiction, as stimulants flood the nucleus accumbens with dopamine—blurring substance and behavioral addiction."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Internet gaming disorder is markedly more common in autism spectrum disorder: gaming's predictable, controllable, low-social-demand structure is especially reinforcing, so screen overuse and IGD are frequent in autistic youth and complicate management of both."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Internet gaming disorder reflects reward-circuit neuroplasticity: repeated dopaminergic reward signaling reshapes synapses in mesolimbic and prefrontal neurons, blunting reward sensitivity and impulse control much as substance addictions do—seen on functional imaging."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Internet gaming disorder and OCD share compulsivity despite different drivers: both feature repetitive, hard-to-resist behaviors engaging overlapping fronto-striatal circuits—though gaming is reward-seeking while OCD is anxiety-driven, blurring addiction and compulsion."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Internet gaming disorder contributes to obesity: prolonged sedentary screen time, disrupted sleep and mindless eating during play promote weight gain, so excessive gaming is a behavioral driver of obesity—linking a digital behavior to a metabolic disease."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Internet gaming disorder and alcohol use disorder share the brain's addiction circuitry: both hijack dopaminergic reward pathways and show tolerance, craving and withdrawal-like symptoms—evidence that behavioral and substance addictions are more alike than once thought."
sources:
  - id: kuss-2012-gaming-disorder-review
    type: peer-reviewed
    cite: "Kuss DJ, Griffiths MD. Internet gaming addiction: a systematic review of empirical research. Int J Ment Health Addict. 2012;10(2):278-296."
    doi: "10.1007/s11469-011-9318-5"
    url: "https://doi.org/10.1007/s11469-011-9318-5"
    accessed: "2026-06-08"
  - id: who-icd11-gaming-disorder
    type: clinical-guideline
    cite: "World Health Organization. ICD-11: Gaming Disorder (6C51). Geneva: WHO; 2019."
    url: "https://icd.who.int/browse/2025-01/mms/en#1448597234"
    accessed: "2026-06-08"
  - id: weinstein-2017-igm-neurobiology
    type: peer-reviewed
    cite: "Weinstein A, Livny A, Weizman A. New developments in brain research of internet and gaming disorder. Neurosci Biobehav Rev. 2017;75:314-330."
    doi: "10.1016/j.neubiorev.2017.01.040"
    pmid: "28193454"
    url: "https://doi.org/10.1016/j.neubiorev.2017.01.040"
    accessed: "2026-06-08"
---

# Internet Gaming Disorder

## Overview

**Internet Gaming Disorder (IGD)** is a proposed condition in which excessive and compulsive video game play leads to significant functional impairment across social, occupational, or educational domains. It was included in the **DSM-5 (2013) Section III** (Conditions for Further Study) and formally recognized in **ICD-11 (2019) as "Gaming Disorder" (6C51)** — placing it alongside gambling disorder as a behavioral addiction.

**Epidemiology:**
- Prevalence estimates vary widely by definition and region: **1–5% of adult gamers** (higher in Asian countries: 10–15% in some South Korean, Chinese, and Taiwanese samples)
- Adolescents are disproportionately affected: 1.7–10% of adolescent gamers depending on criteria
- Male:female ratio ~3:1 (though gender gap is narrowing with mobile gaming)
- Average age of onset: 12–20 years
- High comorbidity: depression (50%), social anxiety disorder (40%), ADHD (30%), autism spectrum disorder (20%), substance use disorders (25%)

**Cultural and regulatory context:**
- South Korea designated gaming addiction a public health crisis in 2011; operates national treatment centers
- China has regulated gaming time for minors (3 hours/week maximum since 2021)
- ICD-11 inclusion by WHO (2019) made gaming disorder a diagnosable clinical entity — driving insurance coverage and treatment funding
- DSM-5 inclusion as Section III (not fully approved) reflects ongoing debate about diagnostic criteria and cultural pathologization of leisure activity

**What distinguishes gaming disorder from heavy gaming:**
- Loss of control over gaming (not just heavy use)
- Gaming continues despite adverse consequences (failed school, lost relationships, health neglect)
- Withdrawal-like symptoms when gaming is stopped (irritability, anxiety, restlessness)
- The disorder is about **impaired control** not mere hours of play

## Structure

### ICD-11 Gaming Disorder criteria (6C51)

A pattern of persistent or recurrent gaming behavior characterized by:

| Criterion | Description |
|:---|:---|
| **Impaired control** | Inability to control frequency, intensity, duration, termination |
| **Increased priority** | Gaming takes priority over other life interests and activities |
| **Continuation despite harm** | Gaming continues or escalates despite negative consequences |
| **Duration** | Sufficient severity for ≥ 12 months (or shorter if severe) |

**DSM-5 Section III criteria (≥5 of 9 in 12 months):**

| Criterion | Domain |
|:---|:---|
| Preoccupation with gaming | Cognitive salience |
| Withdrawal symptoms when gaming not possible | Neuroadaptation |
| Tolerance — need to spend more time gaming | Neuroadaptation |
| Unsuccessful attempts to control gaming | Loss of control |
| Loss of interest in previous hobbies/entertainments | Salience |
| Continued gaming despite psychosocial problems | Harmful use |
| Deceiving family/therapist about amount of gaming | Concealment |
| Gaming to escape dysphoria or negative mood | Negative reinforcement |
| Jeopardized or lost significant relationship/job/educational opportunity | Consequences |

**Subtypes by game genre:**

| Genre | Characteristics | Risk profile |
|:---|:---|:---|
| **MMORPGs (World of Warcraft, FFXIV)** | Social structure, persistent world, guild obligations | Highest IGD risk; social reinforcement; FOMO-driven play |
| **Battle royale / FPS (Fortnite, PUBG)** | Competitive, high arousal, short-cycle reward | Adolescent males; aggression, impulsivity |
| **Mobile games / gacha** | Constant availability, loot box mechanics, monetization | Structural similarities to gambling; adolescents |
| **MOBAs (League of Legends)** | Team-based, ranked ladder, loss-aversion driven | High time investment; anger/frustration-fueled continuation |

### Assessment tools

| Tool | Items | Purpose |
|:---|:---|:---|
| **IGDS9-SF (Internet Gaming Disorder Scale - Short Form)** | 9 | DSM-5-based; most widely used research measure |
| **GAIA (Gaming Addiction Identification Test)** | 21 | ICD-11-based clinical assessment |
| **POGQ (Problematic Online Gaming Questionnaire)** | 18 | Subscales: preoccupation, overuse, immersion, social isolation |
| **CAGE-style screening** | 4 | Rapid primary care screening for gaming disorder |

## Function

### Neurobiological mechanisms of IGD

**Dopamine reward circuitry:**
- Video game play activates VTA-NAcc dopamine via unpredictable variable reward (loot boxes, leveling up, competitive wins) — **same VR schedule** that drives slot machine addiction
- PET studies with [¹¹C]raclopride show **reduced striatal D2R binding** in IGD — the same pattern found in gambling disorder, alcohol use disorder, and stimulant use disorder [^weinstein-2017-igm-neurobiology]
- Reduced D2R → less reward from non-gaming activities → compensatory gaming for adequate dopamine stimulation → behavioral trap

**Cue reactivity:**
- fMRI: game-related visual cues trigger OFC hyperactivation and amygdala activation in IGD participants — pattern virtually identical to gambling disorder and drug cue reactivity
- Cue-induced craving correlates with IGD severity and predicts relapse after treatment
- OFC hyperactivation to gaming cues (overvaluation of game rewards) + vmPFC hypoactivation (impaired top-down suppression) = the neurobiological signature of compulsive gaming

**Impaired inhibitory control:**
- dlPFC hypoactivation on Go/No-Go tasks → reduced suppression of gaming urges
- ACC dysfunction → reduced conflict monitoring and error detection → player continues despite losses/costs
- Structural MRI: reduced gray matter volume in dlPFC and OFC correlates with IGD severity (consistent with chronic dopaminergic remodeling)

**Negative reinforcement (escape motivation):**
- Most IGD patients report gaming primarily to escape depression, anxiety, loneliness, or academic stress — gaming provides **temporary relief from negative affect** but reinforces avoidance
- This escape pattern is associated with more severe IGD, higher depression comorbidity, and worse treatment outcomes
- Parallels alcohol/opioid negative reinforcement in Koob's allostatic model of addiction

### Development and risk factors

**Neurobiological risk:**
- ADHD (30% IGD comorbidity): shared dopaminergic PFC hypofunction, impulsivity, and reward sensitivity → games provide frequent, immediate reward that ADHD brain craves
- Autism spectrum disorder: predictable game rules, virtual social interaction — lowers social demand while providing stimulation; structured virtual world more navigable than social world
- Depression/social anxiety: gaming provides social interaction in low-demand format; escape from school/work stressors

**Game design mechanisms that drive IGD:**
- **Variable ratio reward schedules:** Most effective reinforcement schedule (pigeons, slots, loot boxes)
- **Social obligation/guild mechanics:** MMORPGs create social accountability — missing = letting down teammates → FOMO-driven compulsive play
- **Loss aversion exploitation:** Ranked competitive modes → intense distress at losing → emotional regulation by "one more game" → time loss
- **Loot box mechanics (gacha):** Randomized paid rewards; structural and neurobiological equivalence to slot machines; regulated as gambling in Belgium, Netherlands, UK

## Pathology

### Impact and functional impairment

**Educational and occupational:**
- Sleep displacement: late-night gaming → sleep deprivation → academic/work performance decline → more gaming to cope
- Failed academic years: well-documented in adolescent/young adult IGD cases
- Social isolation: face-to-face social skills atrophy; anxiety when gaming is not available

**Physical health:**
- Sleep disruption: circadian phase delay; reduced sleep duration; insomnia
- Sedentary behavior: obesity, cardiometabolic risk
- Musculoskeletal: repetitive strain injury, carpel tunnel; poor posture
- Ophthalmological: digital eye strain, myopia progression

### Treatment

**Psychosocial (evidence-based):**
- **CBT for IGD:** Modifies gaming-related cognitions (gaming as coping, online identity overvaluation), behavioral: structured schedules, alternative activity planning, social skills; 8-12 sessions; multiple RCTs in South Korea, China — most effective intervention
- **Motivational Enhancement Therapy (MET):** Explores ambivalence; often precedes CBT; effective for treatment-resistant or denial cases
- **Family therapy:** For adolescents; parental involvement improves outcomes; addresses family conflict that drives escape motivation
- **Abstinence vs. controlled use:** Debate mirrors alcohol treatment — total abstinence may be unrealistic for many; structured use contracts more practical for mild-moderate cases

**Pharmacological (off-label/investigational):**
- **Methylphenidate/amphetamine (ADHD comorbidity):** Strong evidence that treating ADHD dramatically reduces IGD in comorbid patients — dopaminergic normalization reduces cue reactivity
- **Bupropion (NE/DA reuptake inhibitor):** Two small Korean RCTs showed significant IGD reduction; plausible via dopaminergic mechanism
- **SSRIs:** For comorbid depression/OCD; modest IGD benefit when depression is driving escape motivation
- **No FDA/EMA-approved pharmacotherapy** for IGD as primary indication

**Digital therapeutics and emerging approaches:**
- Internet-based CBT (iCBT) shown effective in Korean and Chinese trials
- Game-based interventions that teach self-regulation skills
- "Digital detox" residential programs (South Korea, Germany): structured abstinence + CBT + social skills

## Connections

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — gaming activates VTA-NAcc dopamine via variable reward schedules (loot boxes, competitive wins, leveling) — the same mechanism as gambling and substance use; PET shows reduced striatal D2R availability in IGD — the hypodopaminergic pattern shared across addictions; cue-induced dopamine reactivity to game stimuli drives craving and relapse.

- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — IGD and gambling disorder share the core behavioral addiction neurobiology: VTA-NAcc dopamine dysregulation, OFC hyperactivation to cues, vmPFC hypoactivation, impaired PFC-striatum inhibitory control, and D2R hypofunction; both involve variable ratio reinforcement schedules; loot box mechanics in games are structurally and neurobiologically equivalent to slot machines.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — IGD features OFC hyperactivation to game cues (overvaluation of gaming rewards), vmPFC hypoactivation, reduced ventral striatum response to non-gaming rewards, and diminished ACC conflict monitoring; structural MRI shows reduced gray matter volume in dlPFC and OFC, consistent with chronic dopamine-driven reward circuit remodeling.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — IGD is associated with altered BDNF expression in prefrontal circuits, mirroring BDNF changes in substance use disorders and gambling disorder; BDNF Val66Met SNP has been associated with IGD vulnerability; BDNF-TrkB signaling in VTA-PFC circuits mediates the neuroplasticity that sustains compulsive gaming behavior.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — serotonin hypofunction contributes to impulsivity and compulsivity in IGD; 5-HT modulates impulse control in OFC-PFC circuits; SSRIs have modest evidence for IGD when driven by comorbid depression or OCD; impulsivity — a core serotonin-linked trait — is a robust predictor of IGD onset and severity.

- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Internet gaming disorder is the behavioral mirror of substance addictions like cannabis use disorder: variable-ratio game rewards drive the same VTA-NAcc dopamine and D2-receptor hypofunction seen with drugs, with shared OFC cue-reactivity and prefrontal control deficits.

- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression is the most common IGD comorbidity (~50%), and most patients game largely to escape low mood, anxiety, or loneliness; this negative-reinforcement (escape) pattern predicts more severe disorder and worse outcomes, and SSRIs help mainly when depression is the driver.

- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Bupropion, a norepinephrine-dopamine reuptake inhibitor, reduced gaming in small controlled trials, fitting IGD's hypodopaminergic reward biology; noradrenergic tone also supports the prefrontal attention and impulse control weakened in gaming disorder.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — ADHD is one of the strongest correlates of internet gaming disorder: deficits in dopaminergic reward processing and inhibitory control predispose to compulsive gaming, the two are highly comorbid, and IGD severity tracks ADHD symptom load—stimulant treatment may reduce gaming.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — Social anxiety drives internet gaming disorder: online games offer socially safe, avoidant interaction, so socially anxious people retreat into gaming, which deepens real-world avoidance in a reinforcing loop; SAD is a common IGD comorbidity and a target for combined treatment.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Internet gaming disorder and anxiety reinforce each other: gaming is short-term escape from worry, while excessive use, sleep loss and functional decline heighten anxiety; generalized anxiety disorder commonly co-occurs with IGD and shapes relapse during attempts to cut down.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Internet gaming disorder and stimulant use disorder converge on the mesolimbic dopamine reward circuit: gaming's variable rewards drive compulsive use like an addiction, as stimulants flood the nucleus accumbens with dopamine—blurring substance and behavioral addiction.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — Internet gaming disorder is markedly more common in autism spectrum disorder: gaming's predictable, controllable, low-social-demand structure is especially reinforcing, so screen overuse and IGD are frequent in autistic youth and complicate management of both.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Internet gaming disorder reflects reward-circuit neuroplasticity: repeated dopaminergic reward signaling reshapes synapses in mesolimbic and prefrontal neurons, blunting reward sensitivity and impulse control much as substance addictions do—seen on functional imaging.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Internet gaming disorder and OCD share compulsivity despite different drivers: both feature repetitive, hard-to-resist behaviors engaging overlapping fronto-striatal circuits—though gaming is reward-seeking while OCD is anxiety-driven, blurring addiction and compulsion.
- `connects-to` → **[Obesity](../obesity/README.md)** — Internet gaming disorder contributes to obesity: prolonged sedentary screen time, disrupted sleep and mindless eating during play promote weight gain, so excessive gaming is a behavioral driver of obesity—linking a digital behavior to a metabolic disease.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Internet gaming disorder and alcohol use disorder share the brain's addiction circuitry: both hijack dopaminergic reward pathways and show tolerance, craving and withdrawal-like symptoms—evidence that behavioral and substance addictions are more alike than once thought.

[^kuss-2012-gaming-disorder-review]: Kuss DJ, Griffiths MD. Internet gaming addiction: a systematic review of empirical research. *Int J Ment Health Addict.* 2012;10(2):278-296. [doi:10.1007/s11469-011-9318-5](https://doi.org/10.1007/s11469-011-9318-5)
[^who-icd11-gaming-disorder]: World Health Organization. ICD-11: Gaming Disorder (6C51). Geneva: WHO; 2019. [icd.who.int](https://icd.who.int/browse/2025-01/mms/en#1448597234)
[^weinstein-2017-igm-neurobiology]: Weinstein A, Livny A, Weizman A. New developments in brain research of internet and gaming disorder. *Neurosci Biobehav Rev.* 2017;75:314-330. [doi:10.1016/j.neubiorev.2017.01.040](https://doi.org/10.1016/j.neubiorev.2017.01.040) · [PubMed 28193454](https://pubmed.ncbi.nlm.nih.gov/28193454/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
