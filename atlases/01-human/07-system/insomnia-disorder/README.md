---
schema: human-scale-entry/v1
id: insomnia-disorder
name: Insomnia Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Insomnia disorder (10-30% chronic) involves VLPO failure to suppress arousal centers and cortical hyperarousal; first-line: CBT-I (sleep restriction, stimulus control, cognitive restructuring); pharmacotherapy: DORAs (suvorexant, lemborexant), Z-drugs, low-dose doxepin."
aliases: ["insomnia disorder", "insomnia", "chronic insomnia", "sleep-onset insomnia", "sleep-maintenance insomnia", "CBT-I", "suvorexant", "DORA", "ISI", "ISQ", "Insomnia Severity Index", "sleep restriction"]
sources:
  - id: riemann-2017-insomnia-lancet
    type: peer-reviewed
    cite: "Riemann D, Baglioni C, Bassetti C, et al. European guideline for the diagnosis and treatment of insomnia. J Sleep Res. 2017;26(6):675-700."
    doi: "10.1111/jsr.12594"
    pmid: "28875581"
    url: "https://doi.org/10.1111/jsr.12594"
    accessed: "2026-06-08"
  - id: trauer-2015-cbti-meta
    type: peer-reviewed
    cite: "Trauer JM, Qian MY, Doyle JS, Rajaratnam SM, Cunnington D. Cognitive behavioral therapy for chronic insomnia: a systematic review and meta-analysis. Ann Intern Med. 2015;163(3):191-204."
    doi: "10.7326/M14-2841"
    pmid: "26054060"
    url: "https://doi.org/10.7326/M14-2841"
    accessed: "2026-06-08"
  - id: herring-2012-suvorexant
    type: peer-reviewed
    cite: "Herring WJ, Snyder E, Budd K, et al. Orexin receptor antagonism for treatment of insomnia. Sci Transl Med. 2012;4(129):129ra45."
    doi: "10.1126/scitranslmed.3003795"
    pmid: "22491949"
    url: "https://doi.org/10.1126/scitranslmed.3003795"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Orexin neurons in lateral hypothalamus maintain wakefulness by driving LC, TMN, raphe, and basal forebrain; in insomnia, orexin system may be hyperactive; DORAs (suvorexant, lemborexant, daridorexant) block OX1R/OX2R to reduce wake-promoting drive and facilitate sleep."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Z-drugs (zolpidem, zaleplon, eszopiclone) and benzodiazepines are GABA-A positive allosteric modulators highly effective for insomnia but carry tolerance, rebound insomnia, and dependency risks; CBT-I is preferred precisely because it does not require GABA-A modulation."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Trazodone (5-HT2A antagonist + α1/H1 blocker) is the most commonly prescribed off-label insomnia medication; 5-HT2A receptor blockade shifts sleep architecture toward slow-wave sleep; raphe serotonin promotes wakefulness during day and transitions to sleep-onset at night."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "H1 receptors on cortical neurons maintain arousal via TMN projections; low-dose doxepin (3-6mg) is FDA-approved for sleep-maintenance insomnia via H1 blockade; OTC diphenhydramine blocks H1 but causes next-day grogginess and anticholinergic side effects in elderly."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Insomnia involves VLPO failure to fully silence arousal centers (LC, TMN, raphe, orexin neurons) — the flip-flop switch remains unstable; cortical hyperarousal at sleep onset is the core mechanism; CBT-I normalizes sleep homeostasis without pharmacological GABA-A modulation."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine builds homeostatic sleep pressure (process S) during waking via A1R/A2AR on arousal neurons; caffeine (A1R/A2AR antagonist) promotes wakefulness by blocking this pressure — poor caffeine timing is a major behavioral contributor to insomnia onset and maintenance."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Chronic insomnia features HPA hyperarousal — elevated 24h urinary cortisol, blunted diurnal decline, and high evening cortisol; elevated cortisol at sleep onset opposes the core temperature drop required for sleep; CBT-I normalizes HPA hyperarousal in treatment responders."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin MT1 activation reduces SCN firing → sleep onset; MT2 mediates phase shifts; ramelteon (MT1/MT2 agonist, FDA 2005) treats insomnia with no abuse potential; exogenous melatonin (0.5–3 mg) at DLMO is effective for circadian-phase insomnia variants."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "SWS disruption in insomnia suppresses GH (70-80% of daily GH occurs in the first SWS episode); chronic insomnia → reduced GH output; treating sleep disorders with CBT-I or pharmacotherapy may partially restore GH secretory dynamics."
  - target: 01-human/07-system/lewy-body-dementia
    relation: connects-to
    note: "REM sleep behavior disorder—dream-enactment from lost REM atonia—is a powerful early marker of Lewy body dementia and other synucleinopathies, often preceding them by years; LBD also fragments sleep with daytime sleepiness, so these complaints warrant neuro evaluation."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Insomnia and depression are deeply intertwined and bidirectional: insomnia is both a symptom and an independent risk factor for new and recurrent depression, the two share monoaminergic and HPA-axis dysregulation, and treating insomnia (CBT-I) improves depression outcomes."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Insomnia and generalized anxiety reinforce each other: anxious hyperarousal and rumination make sleep hard, while the resulting sleep loss heightens next-day anxiety; both share elevated cortisol and noradrenergic tone, and CBT-I plus anxiety treatment address the loop."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Insomnia and narcolepsy are opposite faces of sleep-wake regulation: insomnia is inability to sleep from a hyperaroused, orexin-active state, while narcolepsy is sleepiness from orexin loss—the orexin system that keeps insomniacs awake fails in narcolepsy."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Insomnia is a core and often presenting symptom of PTSD: hyperarousal and trauma nightmares fragment sleep, persistent insomnia predicts and perpetuates PTSD, and treating the sleep disturbance (CBT-I, prazosin for nightmares) improves overall PTSD outcomes."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Sleep is tightly bound to bipolar disorder: insomnia and a reduced need for sleep often herald or trigger mania, while hypersomnia accompanies depression, and stabilizing sleep and circadian rhythm is central to preventing mood episodes."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Insomnia and fibromyalgia are tightly intertwined: non-restorative sleep worsens pain perception and central sensitization, while chronic pain fragments sleep—so poor sleep both results from and amplifies fibromyalgia, making sleep a core treatment target."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Insomnia and short sleep promote obesity: sleep loss raises ghrelin and lowers leptin, increasing appetite, while disrupting glucose metabolism—so chronic insomnia is a modifiable contributor to weight gain and metabolic syndrome, and obesity in turn worsens sleep."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Insomnia and Alzheimer's disease share a bidirectional link through sleep's role in brain clearance: deep sleep clears amyloid-β via the glymphatic system, so poor sleep may promote amyloid accumulation, while Alzheimer's pathology itself disrupts sleep."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Insomnia is a disorder of the nervous system's arousal regulation: it reflects hyperarousal—the brain failing to disengage its wake-promoting circuits—so it is less a lack of sleep drive than an inability to switch off, the rationale behind cognitive behavioral therapy."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Insomnia and type 2 diabetes feed each other: short, fragmented sleep raises cortisol and impairs glucose tolerance and insulin sensitivity, so chronic insomnia independently raises diabetes risk—and nocturnal symptoms of diabetes in turn disrupt sleep."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol is a common but counterproductive self-treatment for insomnia: it speeds sleep onset yet fragments the second half of the night and suppresses REM, and tolerance fuels escalating use—so insomnia both drives and worsens alcohol use disorder."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Acetylcholine helps run the sleep-wake switch: high cholinergic activity drives REM sleep and wakefulness while it falls in deep sleep, so the balance between acetylcholine and sleep-promoting signals shapes sleep architecture disrupted in insomnia."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Chronic insomnia raises blood pressure: short, fragmented sleep keeps the stress system and sympathetic tone elevated overnight, so persistent insomnia is an independent risk factor for hypertension and cardiovascular disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Sleep and immunity are deeply linked: deep sleep supports immune memory and infection defense, so the chronic sleep loss of insomnia raises inflammation and blunts vaccine responses—part of why poor sleep tracks with worse health overall."
---

# Insomnia Disorder

## Overview

**Insomnia disorder** is characterized by dissatisfaction with sleep quantity or quality, with difficulty initiating sleep, maintaining sleep, or early morning awakening with inability to return to sleep — occurring ≥3 nights/week for ≥3 months, causing clinically significant distress or functional impairment, despite adequate opportunity for sleep.

**Epidemiology:**
- Chronic insomnia prevalence: 10–30% of general population; occasional insomnia: 40–60%
- Female-to-male ratio: 1.4:1 to 2:1; risk increases with age (50-60% of older adults)
- Strong comorbidity with MDD (40%), anxiety disorders (35–45%), chronic pain (50%), COPD (40-50%)
- Economic burden: $92–107 billion/year in US (workplace absenteeism, accidents, healthcare utilization)
- Paradox: people with insomnia typically spend MORE time in bed, which perpetuates the disorder

**DSM-5 / ICSD-3 Criteria:**
1. Difficulty initiating sleep, maintaining sleep, or early awakening
2. Occurs ≥3 nights/week for ≥3 months
3. Causes significant distress or functional impairment (fatigue, mood, cognition, performance)
4. Occurs despite adequate sleep opportunity and circumstances
5. Not better explained by another sleep disorder, substance, or medical/mental disorder

**Assessment — ISI (Insomnia Severity Index):** 7-item validated scale (0–28); mild: 8–14; moderate: 15–21; severe: 22–28; widely used in clinical trials and primary care.

**Sleep diary:** 2-week prospective record of bedtime, rise time, sleep latency, number/duration of awakenings, subjective quality → essential for sleep restriction therapy dosing.

**Actigraphy:** Wrist-worn movement detection; 7–14 day recording; identifies rest-activity cycles; useful when diary unreliable.

**Polysomnography (PSG):** Not routinely indicated for insomnia diagnosis; PSG shows extended sleep latency, reduced sleep efficiency, increased arousal index — but is not required for diagnosis.

## Structure

### Neurobiology of sleep-wake regulation

**VLPO and the flip-flop switch:**

The **ventrolateral preoptic area (VLPO)** of the anterior hypothalamus is the primary sleep-promoting nucleus:
- VLPO neurons are **GABAergic and galaninergic** → project to and inhibit all major arousal centers: LC (NE), TMN (histamine), raphe (5-HT), LDT/PPT (acetylcholine), and lateral hypothalamic orexin neurons
- During wake: Arousal centers inhibit VLPO (via NE, 5-HT, histamine) + orexin neurons reinforce all arousal centers → stable wakefulness
- During sleep: VLPO becomes active → inhibits all arousal centers simultaneously → stable sleep
- **Bistability ("flip-flop"):** Because VLPO inhibits arousal centers and arousal centers inhibit VLPO, the system is all-or-nothing — either fully awake or fully asleep; **orexin stabilizes the switch** toward wakefulness by reinforcing all arousal centers simultaneously

**In insomnia:** The flip-flop switch becomes unstable — VLPO activation is insufficient or delayed, arousal center activity is excessive, or orexin system is hyperactive → failure to fully commit to sleep → frequent nocturnal awakenings.

**Homeostatic sleep pressure (Process S):**
- **Adenosine** accumulates in the basal forebrain during wakefulness → inhibits wake-promoting neurons via A1 receptors → promotes sleep; cleared during sleep
- Caffeine acts by blocking adenosine A1/A2A receptors → blocks sleepiness signal
- Sleep deprivation → adenosine surplus → rebound sleepiness ("sleep debt")
- In chronic insomnia: adenosine homeostasis may be normal, but arousal circuits override the sleep signal

**Hyperarousal model:**
- **Physiological:** Elevated 24-hour cortisol, elevated body temperature at sleep onset (normal sleep requires core temperature drop), elevated HR, elevated ACTH
- **Cognitive:** Racing thoughts, rumination about sleep, performance anxiety about falling asleep
- **Cortical:** EEG shows elevated beta power (high-frequency cortical activity) during NREM sleep — "wake intrusion"; fMRI shows reduced deactivation of the default mode network at sleep onset

**3P Model (Spielman):**
1. **Predisposing factors:** Anxious temperament, trait worry, family history, female sex, chronic stress reactivity
2. **Precipitating factors:** Life stressors, medical illness, bereavement, jet lag, shift work
3. **Perpetuating factors:** Time-in-bed extension (spending 10 hours in bed "to catch up"), daytime napping, caffeine use, maladaptive beliefs ("I need 8 hours or I can't function"), conditioned arousal to the bedroom

CBT-I directly targets perpetuating factors.

## Function

### Sleep stages and insomnia effects

**Normal sleep architecture:**
- Sleep cycles: 90-min periods cycling through NREM stages 1-3 and REM
- N3 (slow-wave sleep, SWS): most restorative; growth hormone release; immune function; memory consolidation
- REM: emotional processing; dreaming; motor system consolidation

**Insomnia disruption:**
- Reduced sleep efficiency (time asleep/time in bed < 85%)
- Prolonged sleep onset latency (SOL > 20-30 min)
- Increased wake after sleep onset (WASO > 30 min)
- Reduced N3 slow-wave sleep (benzodiazepines worsen this; DORAs preserve N3; CBT-I can increase N3)
- Increased N1 transitional sleep (light, non-restorative)

**Impact on daytime function:**
- Cognitive impairment: sustained attention, working memory, psychomotor vigilance (simulated driving performance worsens)
- Metabolic: chronic partial sleep restriction → insulin resistance, increased ghrelin, decreased leptin → obesity risk
- Cardiovascular: insomnia × short sleep duration (< 6h PSG-confirmed) → 3.5× increased hypertension risk
- Psychiatric: bidirectional — insomnia increases depression risk (relative risk 2.2× for MDD); depression worsens insomnia

## Pathology

### Insomnia variants

| Type | Characteristics |
|:---|:---|
| **Sleep-onset insomnia** | >30 min to fall asleep; common in anxiety, delayed sleep phase syndrome |
| **Sleep-maintenance insomnia** | Frequent nocturnal awakenings; common in older adults, pain, depression |
| **Early morning awakening** | Waking ≥2h before desired time; common in MDD (earliest to improve with antidepressants) |
| **Short-sleep insomnia** | PSG-confirmed short TST + subjective insomnia; highest medical risk (HTN, T2DM, mortality) |
| **Paradoxical insomnia** | Subjective insomnia with near-normal PSG; EEG shows beta frequency activity suggesting cortical hyperarousal during sleep |
| **Comorbid insomnia** | With MDD, anxiety, chronic pain, COPD, menopause — requires addressing both conditions |

### Treatment

**CBT-I (Cognitive Behavioral Therapy for Insomnia):**
- Meta-analysis: CBT-I improves sleep efficiency ~10%, reduces SOL by 19 min, reduces WASO by 26 min; effects maintained at 12-month follow-up; superior to pharmacotherapy at follow-up [^trauer-2015-cbti-meta]
- First-line per ACP (2016), AASM, European guideline (2017)
- **Components:**
  - **Sleep restriction therapy (SRT):** Restrict time-in-bed to actual sleep time (minimum 5.5h); creates initial sleep deprivation → increases homeostatic sleep pressure → consolidates sleep; gradually extend as efficiency improves; most powerful CBT-I component
  - **Stimulus control:** Bedroom = sleep/sex only; get out of bed if awake >20 min; consistent rise time regardless of sleep; no daytime napping → rebuilds conditioned arousal between bed and sleepiness
  - **Relaxation techniques:** Progressive muscle relaxation, diaphragmatic breathing, body scan meditation → reduce somatic hyperarousal at bedtime
  - **Cognitive restructuring:** Challenge catastrophic beliefs ("I'll die if I don't sleep 8 hours", "I can never function on this little sleep") → reduce cognitive arousal
  - **Sleep hygiene education:** Caffeine cutoff 6h before bed, consistent schedule, cool bedroom (~18-20°C), dim light 1h before bed, exercise (morning/afternoon)
- **Digital CBT-I (dCBT-I):** Sleepio (UK NHS approved), Somryst (FDA De Novo approved 2020) — app-based CBT-I; equivalent to therapist-delivered for mild-moderate insomnia; addresses access and cost barriers

**Pharmacotherapy:**

| Medication | Class | Mechanism | Notes |
|:---|:---|:---|:---|
| Suvorexant (Belsomra) | DORA | OX1R+OX2R antagonist | FDA 2014; 10-20mg; onset + maintenance; no dependence; preferred in elderly |
| Lemborexant (Dayvigo) | DORA | OX1R+OX2R antagonist | FDA 2019; 5-10mg; fall prevention advantage; faster offset than suvorexant |
| Daridorexant (Quviviq) | DORA | OX1R+OX2R antagonist | FDA 2022; 25-50mg; daytime functioning improvement endpoint |
| Zolpidem (Ambien) | Z-drug | α1-GABA-A PAM | FDA; 5-10mg; onset; rebound risk; impaired driving next morning (women 5mg) |
| Eszopiclone (Lunesta) | Z-drug | GABA-A PAM | FDA; 1-3mg; both onset and maintenance; bitter taste side effect |
| Zaleplon (Sonata) | Z-drug | α1-GABA-A PAM | FDA; 5-10mg; very short half-life; middle-of-night dosing possible |
| Ramelteon (Rozerem) | MT agonist | MT1+MT2 receptor agonist | FDA; sleep onset only; very safe; no dependency; minimal efficacy for maintenance |
| Low-dose doxepin (3-6mg) | TCA | H1 antagonist | FDA; maintenance insomnia; particularly for early morning awakening in elderly |
| Trazodone 25-150mg | SARI | 5-HT2A antagonist | Off-label; widely used; maintenance; sedating; priapism rare |
| Melatonin 0.5-5mg | Hormone | MT1/MT2 agonist | OTC; weak evidence for insomnia; better for circadian phase disorders |
| Diphenhydramine | Antihistamine | H1 antagonist | OTC; rapid tolerance; next-day sedation; avoid in elderly (BEERS) |
| Benzodiazepines | BZD | GABA-A PAM | Short-term only; temazepam, triazolam; significant dependence/cognitive risks |

**Cautions in elderly:**
- Benzodiazepines and Z-drugs: falls risk, cognitive impairment, fractures — BEERS criteria "avoid"
- DORAs: preferred (no fall risk increase); lemborexant showed superior fall outcomes vs. zolpidem in elderly
- Ramelteon: safest option; low-dose doxepin: good evidence

## Connections

- `connects-to` → **[Orexin](../../../03-molecular/orexin/README.md)** — orexin neurons in lateral hypothalamus maintain wakefulness by driving LC, TMN, raphe, and basal forebrain; in insomnia, orexin system may be hyperactive; DORAs (suvorexant, lemborexant, daridorexant) block OX1R/OX2R to reduce wake-promoting drive and facilitate sleep.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — Z-drugs (zolpidem, zaleplon, eszopiclone) and benzodiazepines are GABA-A positive allosteric modulators highly effective for insomnia but carry tolerance, rebound insomnia, and dependency risks; CBT-I is preferred because it normalizes sleep without GABA-A pharmacology.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — trazodone (5-HT2A antagonist + α1/H1 blockade) is the most commonly prescribed off-label insomnia medication; 5-HT2A blockade shifts sleep architecture toward slow-wave sleep; raphe serotonin promotes wakefulness during day and transitions to sleep-onset at night.

- `connects-to` → **[Histamine](../../../03-molecular/histamine/README.md)** — histamine H1 receptors on cortical neurons maintain arousal via TMN projections; low-dose doxepin (3-6mg) is FDA-approved for sleep-maintenance insomnia via selective H1 blockade; OTC diphenhydramine blocks H1 but causes next-day sedation and anticholinergic effects in elderly.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — insomnia involves VLPO failure to fully silence arousal centers (LC, TMN, raphe, orexin neurons), with the flip-flop switch remaining unstable; cortical hyperarousal at sleep onset is the core mechanism; CBT-I normalizes sleep-wake homeostasis by targeting perpetuating behavioral factors.

- `connects-to` → **[Adenosine](../../../03-molecular/adenosine/README.md)** — adenosine builds homeostatic sleep pressure (process S) during waking via A1R/A2AR on arousal neurons; caffeine (A1R/A2AR antagonist) promotes wakefulness by blocking this pressure — poor caffeine timing is a major behavioral contributor to insomnia onset and maintenance.

- `connects-to` → **[Cortisol](../../../03-molecular/cortisol/README.md)** — chronic insomnia features HPA hyperarousal: elevated 24h urinary cortisol, blunted diurnal cortisol decline, and elevated evening cortisol; high cortisol at sleep onset opposes the core body temperature drop required for sleep initiation; HPA hyperarousal normalizes with successful CBT-I treatment, validating it as a biomarker of therapeutic response.

- `connects-to` → **[Melatonin](../../../03-molecular/melatonin/README.md)** — melatonin MT1 activation reduces SCN firing and lowers the arousal threshold at sleep onset; MT2 receptors mediate circadian phase shifts; ramelteon (MT1/MT2 agonist, FDA-approved 2005) is effective for sleep-onset insomnia with no abuse potential or dependence risk; exogenous melatonin (0.5–3 mg timed at DLMO) addresses circadian-phase insomnia variants (DSPD, jet lag).
- `connects-to` → **[Growth Hormone](../../../03-molecular/growth-hormone/README.md)** — SWS disruption in insomnia suppresses GH (70-80% of daily GH occurs in the first SWS episode within 1 hour of sleep onset); chronic insomnia → reduced GH output; treating sleep disorders with CBT-I or pharmacotherapy may partially restore GH secretory dynamics.
- `connects-to` → **[Lewy Body Dementia](../lewy-body-dementia/README.md)** — REM sleep behavior disorder—dream-enactment from lost REM atonia—is a powerful early marker of Lewy body dementia and other synucleinopathies, often preceding them by years; LBD also fragments sleep with daytime sleepiness, so these complaints warrant neuro evaluation.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Insomnia and depression are deeply intertwined and bidirectional: insomnia is both a symptom and an independent risk factor for new and recurrent depression, the two share monoaminergic and HPA-axis dysregulation, and treating insomnia (CBT-I) improves depression outcomes.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Insomnia and generalized anxiety reinforce each other: anxious hyperarousal and rumination make sleep hard, while the resulting sleep loss heightens next-day anxiety; both share elevated cortisol and noradrenergic tone, and CBT-I plus anxiety treatment address the loop.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Insomnia and narcolepsy are opposite faces of sleep-wake regulation: insomnia is inability to sleep from a hyperaroused, orexin-active state, while narcolepsy is sleepiness from orexin loss—the orexin system that keeps insomniacs awake fails in narcolepsy.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Insomnia is a core and often presenting symptom of PTSD: hyperarousal and trauma nightmares fragment sleep, persistent insomnia predicts and perpetuates PTSD, and treating the sleep disturbance (CBT-I, prazosin for nightmares) improves overall PTSD outcomes.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Sleep is tightly bound to bipolar disorder: insomnia and a reduced need for sleep often herald or trigger mania, while hypersomnia accompanies depression, and stabilizing sleep and circadian rhythm is central to preventing mood episodes.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Insomnia and fibromyalgia are tightly intertwined: non-restorative sleep worsens pain perception and central sensitization, while chronic pain fragments sleep—so poor sleep both results from and amplifies fibromyalgia, making sleep a core treatment target.
- `connects-to` → **[Obesity](../obesity/README.md)** — Insomnia and short sleep promote obesity: sleep loss raises ghrelin and lowers leptin, increasing appetite, while disrupting glucose metabolism—so chronic insomnia is a modifiable contributor to weight gain and metabolic syndrome, and obesity in turn worsens sleep.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Insomnia and Alzheimer's disease share a bidirectional link through sleep's role in brain clearance: deep sleep clears amyloid-β via the glymphatic system, so poor sleep may promote amyloid accumulation, while Alzheimer's pathology itself disrupts sleep.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Insomnia is a disorder of the nervous system's arousal regulation: it reflects hyperarousal—the brain failing to disengage its wake-promoting circuits—so it is less a lack of sleep drive than an inability to switch off, the rationale behind cognitive behavioral therapy.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Insomnia and type 2 diabetes feed each other: short, fragmented sleep raises cortisol and impairs glucose tolerance and insulin sensitivity, so chronic insomnia independently raises diabetes risk—and nocturnal symptoms of diabetes in turn disrupt sleep.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol is a common but counterproductive self-treatment for insomnia: it speeds sleep onset yet fragments the second half of the night and suppresses REM, and tolerance fuels escalating use—so insomnia both drives and worsens alcohol use disorder.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Acetylcholine helps run the sleep-wake switch: high cholinergic activity drives REM sleep and wakefulness while it falls in deep sleep, so the balance between acetylcholine and sleep-promoting signals shapes sleep architecture disrupted in insomnia.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Chronic insomnia raises blood pressure: short, fragmented sleep keeps the stress system and sympathetic tone elevated overnight, so persistent insomnia is an independent risk factor for hypertension and cardiovascular disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Sleep and immunity are deeply linked: deep sleep supports immune memory and infection defense, so the chronic sleep loss of insomnia raises inflammation and blunts vaccine responses—part of why poor sleep tracks with worse health overall.

[^riemann-2017-insomnia-lancet]: Riemann D, Baglioni C, Bassetti C, et al. European guideline for the diagnosis and treatment of insomnia. *J Sleep Res.* 2017;26(6):675-700. [doi:10.1111/jsr.12594](https://doi.org/10.1111/jsr.12594) · [PubMed 28875581](https://pubmed.ncbi.nlm.nih.gov/28875581/)
[^trauer-2015-cbti-meta]: Trauer JM, Qian MY, Doyle JS, et al. Cognitive behavioral therapy for chronic insomnia. *Ann Intern Med.* 2015;163(3):191-204. [doi:10.7326/M14-2841](https://doi.org/10.7326/M14-2841) · [PubMed 26054060](https://pubmed.ncbi.nlm.nih.gov/26054060/)
[^herring-2012-suvorexant]: Herring WJ, Snyder E, Budd K, et al. Orexin receptor antagonism for treatment of insomnia. *Sci Transl Med.* 2012;4(129):129ra45. [doi:10.1126/scitranslmed.3003795](https://doi.org/10.1126/scitranslmed.3003795) · [PubMed 22491949](https://pubmed.ncbi.nlm.nih.gov/22491949/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
