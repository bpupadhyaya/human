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
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Social and generalized anxiety disorders overlap (~35-45% comorbid) but differ in scope: social anxiety is fear of scrutiny in specific situations, while GAD is broad, multi-domain worry — and only social anxiety shows a striatal dopamine deficit."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression complicates over half of social anxiety disorder and usually follows it: years of social avoidance and isolation breed hopelessness, so SAD-driven loss of relationships is a route into MDD; treating the social anxiety early can head off the depression."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol is the classic self-medication for social anxiety — it acutely blunts amygdala social-threat reactivity — so 20-25% of people with social anxiety disorder develop an alcohol use disorder, a reinforcing trap where drinking eases anxiety while worsening its course."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Social anxiety and panic disorder are distinct but overlapping: social anxiety fears scrutiny and humiliation, while panic disorder centers on unexpected autonomic attacks and fear of them; situationally-bound panic can occur within social anxiety, and both respond to SSRIs."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Social anxiety is very common in autism and hard to disentangle: autistic social difficulty is a skills/processing difference while social anxiety is fear of negative evaluation, yet they co-occur and reinforce avoidance; recognizing both shapes treatment focus."
  - target: 01-human/07-system/internet-gaming-disorder
    relation: connects-to
    note: "Social anxiety predisposes to internet gaming disorder: online games offer socially safe, avoidant interaction, so socially anxious people retreat into gaming, which deepens real-world avoidance in a loop; addressing social anxiety is part of treating problematic gaming."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Social anxiety disorder and PTSD both center on fear and avoidance but of different triggers: SAD fears scrutiny in social situations, while PTSD fears trauma reminders—both involve amygdala hyperreactivity and respond to SSRIs and exposure-based therapy."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Social anxiety disorder and OCD overlap in anxious avoidance but differ in driver: SAD avoids feared social judgment, while OCD performs compulsions to neutralize obsessions—both are highly comorbid and share SSRI responsiveness and CBT."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Social anxiety disorder reflects an overactive fear circuit in neurons: a hyperreactive amygdala and weak prefrontal regulation amplify the threat response to social cues, the same neuronal imbalance behind other anxiety disorders, which SSRIs and exposure therapy recalibrate."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol marks the stress biology of social anxiety: anticipating social scrutiny activates the HPA axis and raises cortisol, and the exaggerated physiological arousal—blushing, sweating, racing heart—both reflects and reinforces the fear of negative evaluation."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Social anxiety and insomnia feed each other: anticipatory worry about social events delays sleep, and resulting fatigue worsens next-day social performance and avoidance—so poor sleep amplifies the anxiety that caused it, a self-perpetuating loop."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "Social anxiety often precedes eating disorders: fear of eating or being watched in public can drive the food avoidance and body scrutiny seen in anorexia nervosa, and the two frequently coexist—social evaluation fears feeding restrictive behavior."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "The serotonin transporter is social anxiety disorder's key drug target: SSRIs blocking it are first-line treatment, and transporter-gene variation is linked to anxious temperament—connecting the disorder's heritable shyness to serotonergic signaling."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Social anxiety disorder reflects an overactive fear network in the nervous system: a hyperreactive amygdala and weak prefrontal regulation exaggerate threat from social scrutiny, so it is a circuit-level disorder treated by retraining those responses."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Social anxiety disorder and cannabis use disorder are tightly linked: people use cannabis to ease social fear, but heavy use and withdrawal can heighten anxiety and paranoia, so this common self-medication readily slides into dependence."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Social anxiety's physical symptoms are an adrenaline surge: epinephrine drives the racing heart, blushing, sweating, and trembling of feared social moments, which is why beta-blockers like propranolol that blunt adrenaline help with performance anxiety."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF links social anxiety to brain plasticity: this neurotrophin shapes the fear circuits that learn and unlearn social threat, and SSRIs that raise BDNF slowly remodel them—part of why exposure therapy and medication take weeks to rewire avoidance."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus stores social anxiety's fear context: by encoding where and with whom bad social experiences happened, it helps generalize fear to new situations, so this memory hub feeds the anticipatory dread central to the disorder."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Performance social anxiety is treated through the heart: propranolol, a beta-blocker, blunts the racing heart and tremor of stage fright by blocking adrenaline's cardiac effects—calming the physical symptoms that feed the fear without sedation."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Caffeine worsens social anxiety by blocking adenosine: removing adenosine's calming brake heightens arousal and palpitations that mimic and amplify anxious feelings, so caffeine can trigger or intensify social fear in susceptible people."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Social anxiety has a neuroinflammatory thread in microglia: chronic stress activates brain microglia whose cytokines alter the fear and reward circuits, linking immune activation to the persistence of social anxiety."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Social anxiety's physical dread comes from the adrenal glands: anticipating scrutiny triggers an adrenaline and cortisol surge that causes the blushing, sweating, trembling and pounding heart, the body's alarm misfiring in ordinary social moments."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Social anxiety is learned and stored in synapses: fear conditioning strengthens connections in the brain's threat circuits, so social cues come to trigger alarm—plasticity that therapy and SSRIs gradually help reshape."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium helps calm the socially anxious brain: it supports GABA inhibition and restrains excitatory NMDA signaling, so low magnesium can lower the threshold for the over-arousal that fuels anxiety in feared situations."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Social anxiety is written on the skin as blushing: a sympathetic surge floods facial blood vessels, and the visible flush—being seen to react—becomes a feared symptom that feeds the anxiety in a self-reinforcing loop."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Social anxiety's fear memories rely on calcium: calcium entering threat-circuit neurons strengthens the synapses that tag social cues as dangerous, the molecular step that cements conditioned social fear."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes help tune the socially anxious brain: by clearing and recycling glutamate in the amygdala and prefrontal circuits, they shape the excitation-inhibition balance whose tilt toward arousal underlies the disorder."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "fMRI photons capture social anxiety's brain: the amygdala overreacts to faces and signs of judgment while prefrontal regulation lags, the neural basis of the fear of scrutiny."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Social anxiety hits the breath: in feared situations hyperventilation and a tight chest are common physical symptoms, the body's alarm response misfiring in front of others."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Social anxiety's visible signs travel autonomic nerves: sympathetic peripheral nerves drive the sweating, trembling and blushing that betray the fear and feed the cycle of self-consciousness."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc helps temper anxious circuits: it modulates the GABA and glutamate balance that calms the brain, and low zinc is reported in anxiety, making it a studied nutritional adjunct to therapy."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Dread settles in the stomach: anticipating a social ordeal floods the gut with stress signals, producing the nausea and 'butterflies' that are among social anxiety's most dreaded physical symptoms."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D shadows the socially anxious: deficiency is associated with greater anxiety, and the vitamin's receptors in mood-regulating brain regions suggest it helps set the threshold for the fear that social situations trigger."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "The dreaded blush and sweat are cholinergic: eccrine sweat glands are driven by acetylcholine, so the visible sweating of social anxiety is a sympathetic-cholinergic response — and the fear of showing it feeds the cycle."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Anticipatory dread steals sleep: social anxiety commonly brings insomnia and a disturbed circadian rhythm with altered melatonin, the lost rest sharpening the next day's self-consciousness."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Treatment and hormones touch intimacy: the SSRIs that treat social anxiety often dull libido and delay orgasm, while the disorder itself can make dating and sexual relationships fraught with avoidance."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The endocannabinoid system tunes social fear: it governs fear extinction and social reward, and cannabidiol (CBD), which raises endocannabinoid tone, has shown promise at easing the anxiety of public speaking."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Sociability has a microbial dimension: germ-free animals are socially abnormal and gut flora shape the circuits of social behavior and anxiety, so the microbiome-gut-brain axis is studied as a lever on social anxiety."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Anxiety and the bowel feed back: social anxiety overlaps heavily with irritable bowel syndrome, and the fear of urgent, embarrassing GI symptoms in public can itself deepen the avoidance at the disorder's core."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "The stress axis fires at the thought of judgment: CRH launches the HPA cascade, and an over-reactive CRH-cortisol response underlies the racing heart and dread that social situations trigger in the disorder."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "An overactive thyroid can masquerade as social anxiety: hyperthyroidism brings tremor, palpitations, sweating, and nervousness that mimic and worsen it, so thyroid function is checked when anxiety appears or flares."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Anxiety shadows mood disorder: social anxiety co-occurs with bipolar disorder far more than chance, often preceding it, and the comorbidity worsens the course and complicates treatment of both."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate sets the fear circuit's gain: excess excitatory signaling in the amygdala and prefrontal cortex sustains the threat over-appraisal of social anxiety, and glutamate-modulating agents like d-cycloserine are studied to speed exposure therapy."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Stimulants and social anxiety pull in both directions: caffeine and stimulant drugs provoke the palpitations and jitteriness that ignite social fear, yet some sufferers misuse substances to self-medicate, raising addiction risk."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "A visible skin disease breeds social fear: the stigma of psoriasis plaques drives marked social anxiety and avoidance, one of the clearest examples of how a chronic dermatologic condition shapes mental health."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic social stress leaves an inflammatory trace: the sustained arousal of social anxiety activates NF-κB-driven cytokine signaling, a low-grade inflammation increasingly tied to the disorder's persistence and its physical-health toll."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Social fear shadows psychosis: social anxiety is common in schizophrenia, overlapping its negative symptoms and social withdrawal and sometimes appearing in the prodrome before frank psychosis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Standing fear strains the heart over time: the repeated sympathetic surges of social anxiety raise heart rate and blood pressure, and chronic anxiety is linked to higher long-term cardiovascular risk."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Avoidance and comfort eating add weight: the social withdrawal and reduced activity of social anxiety, plus stress-driven eating, contribute to obesity, compounding the disorder's physical-health burden."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "Shame can drive secret eating: social anxiety frequently co-occurs with binge eating disorder, where fear of judgment fuels solitary, distressing binges that deepen isolation."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Anxiety and chronic pain travel together: social anxiety is over-represented in fibromyalgia, the shared central stress-and-pain processing amplifying both the bodily pain and the social fear."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Breathlessness and social fear intertwine: social anxiety is elevated in asthma, where visible symptoms and inhaler use in public, plus the panic of air hunger, reinforce avoidance and worse control."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Performance stress spikes the pressure: the intense sympathetic surges of feared social situations, on a background of chronic stress arousal, contribute over time to hypertension."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Chronic stress and avoidance tilt toward diabetes: sustained cortisol arousal, comfort eating and the inactivity of social avoidance contribute to the insulin resistance behind type 2 diabetes."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its fears show on the skin: blushing and facial flushing are core feared symptoms of social anxiety, and visible sweating from hyperhidrosis both triggers and is dreaded in social situations."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Anxiety speaks through the gut: social anxiety drives the 'nervous stomach' of cramps, nausea and urgency, and is comorbid with irritable bowel syndrome through the gut-brain axis."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "They frequently co-occur: social anxiety is common in ADHD, where social difficulties and rejection sensitivity feed the fear of judgement, complicating diagnosis and treatment."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Social-evaluative fear spikes cortisol: social anxiety disorder shows an exaggerated HPA-axis cortisol response to scrutiny, and beta-blockers blunt the adrenergic tremor and palpitations of performance anxiety."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Anticipation tenses the body: dreaded social situations bring muscle tension, trembling and tension headaches that themselves heighten self-consciousness."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Fear quickens the breath: social anxiety provokes hyperventilation, breathlessness and a choking sensation during feared encounters, somatic symptoms that can escalate to panic."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "First-line treatment is an SSRI: antidepressants like fluoxetine, alongside cognitive behavioural therapy, are the mainstay for generalised social anxiety disorder."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "A heart drug calms performance nerves: beta-blockers like propranolol blunt the tremor, palpitations and sweating of performance anxiety when taken before a feared event."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Chronic social stress inflames the body: sustained anxiety dysregulates cortisol and raises inflammatory markers, a stress-immune link shared across the anxiety disorders."
  - target: 03-medicine/02-traditional/ashwagandha
    relation: connects-to
    note: "A traditional calm for nerves: ashwagandha and similar adaptogens are used to ease anxiety and lower cortisol, a complementary option alongside the SSRIs that treat social anxiety disorder."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet offers a modest adjunct: omega-3 supplementation shows small anxiety-reducing effects in trials, used alongside but not instead of established treatment for social anxiety."
  - target: 01-human/07-system/bulimia-nervosa
    relation: connects-to
    note: "Fear of judgement links them: social anxiety disorder commonly precedes and coexists with bulimia nervosa, where intense fear of negative evaluation feeds disordered eating and shame."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "Rejection sensitivity in common: social anxiety disorder and borderline personality disorder both centre on intense fear of rejection and negative evaluation, frequently coexist, and amplify each other's interpersonal distress."
  - target: 03-medicine/02-traditional/st-johns-wort
    relation: connects-to
    note: "A herbal serotonergic option: St John's wort raises serotonin like the SSRIs that are first-line for social anxiety, and is used by some for milder symptoms, though evidence is limited and interactions are common."
  - target: 03-medicine/02-traditional/panax-ginseng
    relation: connects-to
    note: "An adaptogen tried for anxiety: like ashwagandha, Panax ginseng is among the traditional remedies used for the chronic stress and arousal of social anxiety, complementing rather than replacing established therapy."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "The racing, pounding heart: social anxiety's autonomic surge drives palpitations, tachycardia and tremor through the conduction system, and beta-blockers blunt these symptoms for performance anxiety."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "The resilience neuropeptide: NPY dampens amygdala threat reactivity and the stress response, and low NPY tone is linked to the heightened social-threat sensitivity that underlies social anxiety."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Reward pursued in private: social anxiety can predispose to solitary behavioural addictions like gambling, undertaken to avoid social exposure and relieve anticipatory distress."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Self-medicating distress: social anxiety disorder raises the risk of substance use disorders including opioids, used to blunt anticipatory dread and the physical symptoms of social fear."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Anxiety and headache: social anxiety disorder is comorbid with migraine, the two sharing serotonergic dysregulation and a stress-reactive nervous system that lowers the threshold for both."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Isolation and reintegration fear: the COVID-19 pandemic worsened social anxiety, with prolonged isolation and later re-entry into social settings intensifying anticipatory distress."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Gut-brain axis: social anxiety overlaps with irritable bowel syndrome, and signalling across the intestinal epithelium and microbiome shapes the stress and fear circuits that drive it."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Visible skin and avoidance: chronic, visible eczema—like psoriasis—drives appearance-related distress, embarrassment and social withdrawal that feed and worsen social anxiety."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Visible motor symptoms: Parkinson's tremor, reduced facial expression and gait changes commonly provoke social anxiety and withdrawal, which are core non-motor features of the disease."
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

- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Social and generalized anxiety disorders overlap (~35-45% comorbid) but differ in scope: social anxiety is fear of scrutiny in specific situations, while GAD is broad, multi-domain worry — and only social anxiety shows a striatal dopamine deficit.

- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression complicates over half of social anxiety disorder and usually follows it: years of social avoidance and isolation breed hopelessness, so SAD-driven loss of relationships is a route into MDD; treating the social anxiety early can head off the depression.

- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol is the classic self-medication for social anxiety — it acutely blunts amygdala social-threat reactivity — so 20-25% of people with social anxiety disorder develop an alcohol use disorder, a reinforcing trap where drinking eases anxiety while worsening its course.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Social anxiety and panic disorder are distinct but overlapping: social anxiety fears scrutiny and humiliation, while panic disorder centers on unexpected autonomic attacks and fear of them; situationally-bound panic can occur within social anxiety, and both respond to SSRIs.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — Social anxiety is very common in autism and hard to disentangle: autistic social difficulty is a skills/processing difference while social anxiety is fear of negative evaluation, yet they co-occur and reinforce avoidance; recognizing both shapes treatment focus.
- `connects-to` → **[Internet Gaming Disorder](../internet-gaming-disorder/README.md)** — Social anxiety predisposes to internet gaming disorder: online games offer socially safe, avoidant interaction, so socially anxious people retreat into gaming, which deepens real-world avoidance in a loop; addressing social anxiety is part of treating problematic gaming.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Social anxiety disorder and PTSD both center on fear and avoidance but of different triggers: SAD fears scrutiny in social situations, while PTSD fears trauma reminders—both involve amygdala hyperreactivity and respond to SSRIs and exposure-based therapy.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Social anxiety disorder and OCD overlap in anxious avoidance but differ in driver: SAD avoids feared social judgment, while OCD performs compulsions to neutralize obsessions—both are highly comorbid and share SSRI responsiveness and CBT.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Social anxiety disorder reflects an overactive fear circuit in neurons: a hyperreactive amygdala and weak prefrontal regulation amplify the threat response to social cues, the same neuronal imbalance behind other anxiety disorders, which SSRIs and exposure therapy recalibrate.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol marks the stress biology of social anxiety: anticipating social scrutiny activates the HPA axis and raises cortisol, and the exaggerated physiological arousal—blushing, sweating, racing heart—both reflects and reinforces the fear of negative evaluation.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Social anxiety and insomnia feed each other: anticipatory worry about social events delays sleep, and resulting fatigue worsens next-day social performance and avoidance—so poor sleep amplifies the anxiety that caused it, a self-perpetuating loop.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — Social anxiety often precedes eating disorders: fear of eating or being watched in public can drive the food avoidance and body scrutiny seen in anorexia nervosa, and the two frequently coexist—social evaluation fears feeding restrictive behavior.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — The serotonin transporter is social anxiety disorder's key drug target: SSRIs blocking it are first-line treatment, and transporter-gene variation is linked to anxious temperament—connecting the disorder's heritable shyness to serotonergic signaling.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Social anxiety disorder reflects an overactive fear network in the nervous system: a hyperreactive amygdala and weak prefrontal regulation exaggerate threat from social scrutiny, so it is a circuit-level disorder treated by retraining those responses.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Social anxiety disorder and cannabis use disorder are tightly linked: people use cannabis to ease social fear, but heavy use and withdrawal can heighten anxiety and paranoia, so this common self-medication readily slides into dependence.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Social anxiety's physical symptoms are an adrenaline surge: epinephrine drives the racing heart, blushing, sweating, and trembling of feared social moments, which is why beta-blockers like propranolol that blunt adrenaline help with performance anxiety.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF links social anxiety to brain plasticity: this neurotrophin shapes the fear circuits that learn and unlearn social threat, and SSRIs that raise BDNF slowly remodel them—part of why exposure therapy and medication take weeks to rewire avoidance.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus stores social anxiety's fear context: by encoding where and with whom bad social experiences happened, it helps generalize fear to new situations, so this memory hub feeds the anticipatory dread central to the disorder.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Performance social anxiety is treated through the heart: propranolol, a beta-blocker, blunts the racing heart and tremor of stage fright by blocking adrenaline's cardiac effects—calming the physical symptoms that feed the fear without sedation.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Caffeine worsens social anxiety by blocking adenosine: removing adenosine's calming brake heightens arousal and palpitations that mimic and amplify anxious feelings, so caffeine can trigger or intensify social fear in susceptible people.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Social anxiety has a neuroinflammatory thread in microglia: chronic stress activates brain microglia whose cytokines alter the fear and reward circuits, linking immune activation to the persistence of social anxiety.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Social anxiety's physical dread comes from the adrenal glands: anticipating scrutiny triggers an adrenaline and cortisol surge that causes the blushing, sweating, trembling and pounding heart, the body's alarm misfiring in ordinary social moments.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Social anxiety is learned and stored in synapses: fear conditioning strengthens connections in the brain's threat circuits, so social cues come to trigger alarm—plasticity that therapy and SSRIs gradually help reshape.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium helps calm the socially anxious brain: it supports GABA inhibition and restrains excitatory NMDA signaling, so low magnesium can lower the threshold for the over-arousal that fuels anxiety in feared situations.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Social anxiety is written on the skin as blushing: a sympathetic surge floods facial blood vessels, and the visible flush—being seen to react—becomes a feared symptom that feeds the anxiety in a self-reinforcing loop.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Social anxiety's fear memories rely on calcium: calcium entering threat-circuit neurons strengthens the synapses that tag social cues as dangerous, the molecular step that cements conditioned social fear.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes help tune the socially anxious brain: by clearing and recycling glutamate in the amygdala and prefrontal circuits, they shape the excitation-inhibition balance whose tilt toward arousal underlies the disorder.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — fMRI photons capture social anxiety's brain: the amygdala overreacts to faces and signs of judgment while prefrontal regulation lags, the neural basis of the fear of scrutiny.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Social anxiety hits the breath: in feared situations hyperventilation and a tight chest are common physical symptoms, the body's alarm response misfiring in front of others.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Social anxiety's visible signs travel autonomic nerves: sympathetic peripheral nerves drive the sweating, trembling and blushing that betray the fear and feed the cycle of self-consciousness.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc helps temper anxious circuits: it modulates the GABA and glutamate balance that calms the brain, and low zinc is reported in anxiety, making it a studied nutritional adjunct to therapy.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Dread settles in the stomach: anticipating a social ordeal floods the gut with stress signals, producing the nausea and 'butterflies' that are among social anxiety's most dreaded physical symptoms.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D shadows the socially anxious: deficiency is associated with greater anxiety, and the vitamin's receptors in mood-regulating brain regions suggest it helps set the threshold for the fear that social situations trigger.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — The dreaded blush and sweat are cholinergic: eccrine sweat glands are driven by acetylcholine, so the visible sweating of social anxiety is a sympathetic-cholinergic response — and the fear of showing it feeds the cycle.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Anticipatory dread steals sleep: social anxiety commonly brings insomnia and a disturbed circadian rhythm with altered melatonin, the lost rest sharpening the next day's self-consciousness.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Treatment and hormones touch intimacy: the SSRIs that treat social anxiety often dull libido and delay orgasm, while the disorder itself can make dating and sexual relationships fraught with avoidance.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The endocannabinoid system tunes social fear: it governs fear extinction and social reward, and cannabidiol (CBD), which raises endocannabinoid tone, has shown promise at easing the anxiety of public speaking.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Sociability has a microbial dimension: germ-free animals are socially abnormal and gut flora shape the circuits of social behavior and anxiety, so the microbiome-gut-brain axis is studied as a lever on social anxiety.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Anxiety and the bowel feed back: social anxiety overlaps heavily with irritable bowel syndrome, and the fear of urgent, embarrassing GI symptoms in public can itself deepen the avoidance at the disorder's core.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — The stress axis fires at the thought of judgment: CRH launches the HPA cascade, and an over-reactive CRH-cortisol response underlies the racing heart and dread that social situations trigger in the disorder.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — An overactive thyroid can masquerade as social anxiety: hyperthyroidism brings tremor, palpitations, sweating, and nervousness that mimic and worsen it, so thyroid function is checked when anxiety appears or flares.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Anxiety shadows mood disorder: social anxiety co-occurs with bipolar disorder far more than chance, often preceding it, and the comorbidity worsens the course and complicates treatment of both.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Glutamate sets the fear circuit's gain: excess excitatory signaling in the amygdala and prefrontal cortex sustains the threat over-appraisal of social anxiety, and glutamate-modulating agents like d-cycloserine are studied to speed exposure therapy.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Stimulants and social anxiety pull in both directions: caffeine and stimulant drugs provoke the palpitations and jitteriness that ignite social fear, yet some sufferers misuse substances to self-medicate, raising addiction risk.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — A visible skin disease breeds social fear: the stigma of psoriasis plaques drives marked social anxiety and avoidance, one of the clearest examples of how a chronic dermatologic condition shapes mental health.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic social stress leaves an inflammatory trace: the sustained arousal of social anxiety activates NF-κB-driven cytokine signaling, a low-grade inflammation increasingly tied to the disorder's persistence and its physical-health toll.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Social fear shadows psychosis: social anxiety is common in schizophrenia, overlapping its negative symptoms and social withdrawal and sometimes appearing in the prodrome before frank psychosis.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Standing fear strains the heart over time: the repeated sympathetic surges of social anxiety raise heart rate and blood pressure, and chronic anxiety is linked to higher long-term cardiovascular risk.
- `connects-to` → **[Obesity](../obesity/README.md)** — Avoidance and comfort eating add weight: the social withdrawal and reduced activity of social anxiety, plus stress-driven eating, contribute to obesity, compounding the disorder's physical-health burden.
- `connects-to` → **[Binge Eating Disorder](../binge-eating-disorder/README.md)** — Shame can drive secret eating: social anxiety frequently co-occurs with binge eating disorder, where fear of judgment fuels solitary, distressing binges that deepen isolation.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Anxiety and chronic pain travel together: social anxiety is over-represented in fibromyalgia, the shared central stress-and-pain processing amplifying both the bodily pain and the social fear.
- `connects-to` → **[Asthma](../asthma/README.md)** — Breathlessness and social fear intertwine: social anxiety is elevated in asthma, where visible symptoms and inhaler use in public, plus the panic of air hunger, reinforce avoidance and worse control.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Performance stress spikes the pressure: the intense sympathetic surges of feared social situations, on a background of chronic stress arousal, contribute over time to hypertension.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Chronic stress and avoidance tilt toward diabetes: sustained cortisol arousal, comfort eating and the inactivity of social avoidance contribute to the insulin resistance behind type 2 diabetes.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its fears show on the skin: blushing and facial flushing are core feared symptoms of social anxiety, and visible sweating from hyperhidrosis both triggers and is dreaded in social situations.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Anxiety speaks through the gut: social anxiety drives the 'nervous stomach' of cramps, nausea and urgency, and is comorbid with irritable bowel syndrome through the gut-brain axis.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — They frequently co-occur: social anxiety is common in ADHD, where social difficulties and rejection sensitivity feed the fear of judgement, complicating diagnosis and treatment.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Social-evaluative fear spikes cortisol: social anxiety disorder shows an exaggerated HPA-axis cortisol response to scrutiny, and beta-blockers blunt the adrenergic tremor and palpitations of performance anxiety.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Anticipation tenses the body: dreaded social situations bring muscle tension, trembling and tension headaches that themselves heighten self-consciousness.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Fear quickens the breath: social anxiety provokes hyperventilation, breathlessness and a choking sensation during feared encounters, somatic symptoms that can escalate to panic.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — First-line treatment is an SSRI: antidepressants like fluoxetine, alongside cognitive behavioural therapy, are the mainstay for generalised social anxiety disorder.
- `connects-to` → **[Beta-blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — A heart drug calms performance nerves: beta-blockers like propranolol blunt the tremor, palpitations and sweating of performance anxiety when taken before a feared event.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Chronic social stress inflames the body: sustained anxiety dysregulates cortisol and raises inflammatory markers, a stress-immune link shared across the anxiety disorders.
- `connects-to` → **[Ashwagandha](../../../03-medicine/02-traditional/ashwagandha/README.md)** — A traditional calm for nerves: ashwagandha and similar adaptogens are used to ease anxiety and lower cortisol, a complementary option alongside the SSRIs that treat social anxiety disorder.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet offers a modest adjunct: omega-3 supplementation shows small anxiety-reducing effects in trials, used alongside but not instead of established treatment for social anxiety.
- `connects-to` → **[Bulimia Nervosa](../bulimia-nervosa/README.md)** — Fear of judgement links them: social anxiety disorder commonly precedes and coexists with bulimia nervosa, where intense fear of negative evaluation feeds disordered eating and shame.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — Rejection sensitivity in common: social anxiety disorder and borderline personality disorder both centre on intense fear of rejection and negative evaluation, frequently coexist, and amplify each other's interpersonal distress.
- `connects-to` → **[St John's Wort](../../../03-medicine/02-traditional/st-johns-wort/README.md)** — A herbal serotonergic option: St John's wort raises serotonin like the SSRIs that are first-line for social anxiety, and is used by some for milder symptoms, though evidence is limited and interactions are common.
- `connects-to` → **[Panax Ginseng](../../../03-medicine/02-traditional/panax-ginseng/README.md)** — An adaptogen tried for anxiety: like ashwagandha, Panax ginseng is among the traditional remedies used for the chronic stress and arousal of social anxiety, complementing rather than replacing established therapy.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — The racing, pounding heart: social anxiety's autonomic surge drives palpitations, tachycardia and tremor through the conduction system, and beta-blockers blunt these symptoms for performance anxiety.
- `connects-to` → **[NPY](../../03-molecular/npy/README.md)** — The resilience neuropeptide: NPY dampens amygdala threat reactivity and the stress response, and low NPY tone is linked to the heightened social-threat sensitivity that underlies social anxiety.
- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — Reward pursued in private: social anxiety can predispose to solitary behavioural addictions like gambling, undertaken to avoid social exposure and relieve anticipatory distress.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Self-medicating distress: social anxiety disorder raises the risk of substance use disorders including opioids, used to blunt anticipatory dread and the physical symptoms of social fear.
- `connects-to` → **[Migraine](../migraine/README.md)** — Anxiety and headache: social anxiety disorder is comorbid with migraine, the two sharing serotonergic dysregulation and a stress-reactive nervous system that lowers the threshold for both.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Isolation and reintegration fear: the COVID-19 pandemic worsened social anxiety, with prolonged isolation and later re-entry into social settings intensifying anticipatory distress.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Gut-brain axis: social anxiety overlaps with irritable bowel syndrome, and signalling across the intestinal epithelium and microbiome shapes the stress and fear circuits that drive it.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Visible skin and avoidance: chronic, visible eczema—like psoriasis—drives appearance-related distress, embarrassment and social withdrawal that feed and worsen social anxiety.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Visible motor symptoms: Parkinson's tremor, reduced facial expression and gait changes commonly provoke social anxiety and withdrawal, which are core non-motor features of the disease.

[^liebowitz-1987-sad-scale]: Liebowitz MR. Social phobia. *Mod Probl Pharmacopsychiatry.* 1987;22:141-173. [PubMed 2885745](https://pubmed.ncbi.nlm.nih.gov/2885745/)
[^stein-2008-sad-review]: Stein MB, Stein DJ. Social anxiety disorder. *Lancet.* 2008;371(9618):1115-1125. [doi:10.1016/S0140-6736(08)60488-2](https://doi.org/10.1016/S0140-6736(08)60488-2) · [PubMed 18374843](https://pubmed.ncbi.nlm.nih.gov/18374843/)
[^goldin-2010-mbsr-sad]: Goldin PR, Gross JJ. Effects of mindfulness-based stress reduction (MBSR) on emotion regulation in social anxiety disorder. *Emotion.* 2010;10(1):83-91. [doi:10.1037/a0018441](https://doi.org/10.1037/a0018441) · [PubMed 20141305](https://pubmed.ncbi.nlm.nih.gov/20141305/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
