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
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Stress cytokine: TNF-α is among the inflammatory markers elevated in social anxiety, reflecting how chronic social-evaluative stress feeds systemic inflammation."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Social-stress peptide: vasopressin modulates social behaviour and the stress response, and its signalling is implicated in the heightened social-threat sensitivity of social anxiety disorder."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory link: elevated IL-6 is found in social anxiety, part of the bidirectional relationship between chronic social stress and low-grade systemic inflammation."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid tone: the progesterone metabolite allopregnanolone potentiates GABA-A receptors, so fluctuations in this anxiolytic neurosteroid modulate the threat reactivity of social anxiety disorder."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Fear neuropeptide: substance P acting at NK1 receptors in the amygdala amplifies fear and stress responses, a pathway implicated in anxiety disorders including social anxiety."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Dominance and submission: testosterone shifts social approach and threat vigilance, and lower testosterone tone is linked to the submissive, avoidant behaviour characteristic of social anxiety disorder."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Social reward and rejection: the μ-opioid system mediates the pleasure of social affiliation and the pain of rejection, and blunted μ-opioid signalling is linked to the rejection sensitivity central to social anxiety disorder."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormonal modulation: estrogen tunes the serotonergic and fear-circuit systems underlying anxiety, contributing to sex differences and the perimenstrual fluctuation in symptom severity in social anxiety disorder."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Social-stress neuroinflammation: social-defeat stress raises IL-1β in fear and reward circuits, part of the neuroimmune response that links chronic social stress to the heightened threat reactivity of social anxiety."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Hyperarousal: orexin signalling that drives wakefulness and stress reactivity is implicated in anxiety, contributing to the physiological hyperarousal — racing heart, sweating, trembling — that anticipatory social fear triggers."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Amygdala fear peptide: CGRP projecting from the parabrachial nucleus into the amygdala signals threat and amplifies fear and avoidance, a neuropeptide arm of the threat circuitry overactive in social anxiety disorder."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Social-stress hormone: chronic social-defeat stress dysregulates ghrelin, which potentiates fear-memory consolidation, a gut-derived stress hormone linking the social adversity that often precedes social anxiety to its persistent fear learning."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "HPA response: anticipatory social stress activates the HPA axis (cortisol and CRH already mapped), and glucocorticoid-receptor signalling mediates the cortisol response that characterises social anxiety disorder."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: connects-to
    note: "Performance symptoms: the palpitations, tremor and blushing of social anxiety arise from catecholamine activation of β-adrenergic receptors, the target of the β-blockers already mapped for performance anxiety."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Fear-memory consolidation: amygdala ERK-MAPK signalling consolidates the fear-conditioned memories of social threat that underlie the persistence and generalisation of social anxiety disorder."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Neuroinflammatory arousal: TLR4-driven neuroinflammation links systemic and stress-induced inflammation to the cortico-amygdala hyperarousal implicated in social anxiety disorder."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Fear-extinction plasticity: BDNF signalling through its TrkB receptor (NTRK) supports the prefrontal-amygdala plasticity required for fear extinction, the deficient process underlying persistent social fear."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative stress: NRF2-regulated antioxidant defences counter the oxidative stress that accompanies chronic anxiety and HPA-axis overactivation, linking redox imbalance to the persistence of social anxiety."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "BDNF/serotonergic PI3K-AKT-mTOR signalling supports the neuroplasticity that anxiolytic treatment restores in social anxiety disorder."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 reflects the low-grade neuroinflammation associated with chronic anxiety states including social anxiety disorder."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR4-MyD88 innate signalling (TLR4 mapped) drives the neuroinflammation increasingly linked to anxiety pathophysiology."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling in limbic circuits shapes the synaptic plasticity and fear-learning balance implicated in social anxiety disorder."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the chronic inflammatory tone associated with the heightened stress reactivity of social anxiety disorder."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic mitochondrial DNA released during chronic stress can engage cGAS-STING, contributing to the neuroinflammation implicated in social anxiety disorder."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress and resilience relevant to the stress vulnerability of social anxiety disorder."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 neuroinflammatory signaling contributes to the inflammatory tone associated with social anxiety disorder."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the inflammatory tone linked to the fear and anxiety circuitry of social anxiety disorder."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and oxidative-stress adaptation participates in the neurobiology of social anxiety disorder."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the low-grade peripheral inflammation associated with social anxiety disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the neuronal plasticity of the fear circuits implicated in social anxiety disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the neurometabolic and stress-adaptation responses relevant to social anxiety disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal stress resilience and fear-circuit homeostasis implicated in social anxiety disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic (early-life-stress) programming implicated in social anxiety disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the synaptic-plasticity mechanisms of the fear and social-behavior circuitry implicated in social anxiety disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with social anxiety disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and neuroplasticity processes implicated in social anxiety disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in social anxiety disorder."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with social anxiety disorder."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the microglial and neuroinflammatory processes implicated in social anxiety disorder."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Brain renin-angiotensin: central angiotensin II modulates the HPA and sympathetic stress response, and angiotensin blockade is associated with lower anxiety, a neuroendocrine axis beyond the monoamine systems already mapped in social anxiety."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Fear circuitry: nitric oxide from neuronal nNOS modulates the amygdala and prefrontal circuits that process social threat, implicating NO signalling in the exaggerated fear response of social anxiety disorder."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Arousal and blushing: central histamine drives arousal and vigilance, systems heightened in the anticipatory anxiety, and peripheral vasomotor responses contribute to the blushing that is a hallmark somatic symptom of social anxiety."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response and threat appraisal exaggerated in social anxiety disorder."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic stress load: chronic anxiety and HPA activation (cortisol already mapped) promote insulin resistance, part of the cardiometabolic burden that can accompany long-standing social anxiety disorder."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory cytokine IL-10 counters the pro-inflammatory TNF, IL-6 and IL-1 (already mapped) reported in anxiety disorders, part of the low-grade neuroinflammation associated with chronic social anxiety."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Cardiometabolic burden: the chronic stress and insulin resistance (insulin already mapped) of long-standing social anxiety disorder shift cholesterol handling toward an atherogenic profile, part of its raised cardiovascular risk."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6, TNF and IL-1 already mapped) reported in anxiety modulate the fear and social-threat circuits implicated in social anxiety disorder."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: heightened oxidative stress, to which xanthine oxidase contributes, is reported in anxiety disorders (NRF2 already mapped), and the resulting reactive oxygen species may affect the neurons of the fear circuitry."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation reported in social anxiety disorder."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is part of the type-2 response whose balance against the pro-inflammatory signals shapes the neuroinflammatory dimension of social anxiety disorder."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and noradrenaline: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the noradrenergic arousal (beta1-adrenergic receptor already mapped) of social anxiety disorder."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Anxiolytic adipokine: leptin has anxiolytic actions in the amygdala, linking the metabolic (insulin already mapped) state to the anxiety circuits of social anxiety disorder."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory (IL-6 already mapped) comorbidity of chronic anxiety."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the neuroinflammation (TNF and IL-1 already mapped) associated with social anxiety disorder."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Neuroinflammation: the microglial activation and the neuroinflammation (TNF, IL-6 and IL-1 already mapped) are implicated in the anxiety of social anxiety disorder."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Anxiety-spectrum overlap: social anxiety disorder and panic disorder are comorbid anxiety disorders, sharing the noradrenergic and serotonergic (already mapped) dysregulation."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Anxiolytic magnesium: magnesium modulates the NMDA/glutamate (already mapped) and the HPA (cortisol already mapped) axis; low magnesium is associated with the anxiety of social anxiety disorder."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in social anxiety disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation (IL-1 and TNF already mapped) associated with social anxiety disorder."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of social anxiety disorder."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with social anxiety disorder."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of social anxiety disorder."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of social anxiety disorder."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the histamine (already mapped) and neuroinflammatory dimension implicated in social anxiety disorder."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic social-evaluative stress of social anxiety disorder."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Stress-modulated NK: the NK-cell number and cytotoxicity, altered by the chronic stress and cortisol (already mapped) reactivity, are part of the peripheral immune dysregulation of social anxiety disorder."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the low-grade complement activation of the neuroinflammation implicated in social anxiety disorder."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial neuroinflammation implicated in the fear circuitry of social anxiety disorder."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the low-grade inflammation of social anxiety disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-anxiety axis: TSLP, from gut-epithelium (gut-microbiome already mapped) and mast cells (already mapped) under the chronic social stress of social anxiety disorder, amplifies the neuroinflammatory and the Th2/mast-cell stress axis of the fear-circuit hyperactivity."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-autonomic axis: bradykinin, via B2R on CNS neurons (already mapped) and microglia (already mapped), modulates the neuroinflammation and the autonomic hyperarousal contributing to the somatic and the cardiovascular symptoms of social anxiety disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3, C5 and factor-H already mapped) contributing to the neuroinflammation and the complement-mediated fear-circuit synaptic remodelling of social anxiety disorder."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Stress EPO axis: chronic social anxiety and HPA-axis (cortisol already mapped) dysregulation alters EPO signalling; EpoR on neurons (already mapped) and microglia (already mapped) provides neuroprotection relevant to the amygdala (brain already mapped) hyperreactivity of SAD."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement gate: factor H limits alternative-pathway activation at the blood-brain barrier, restraining complement-mediated synaptic pruning and the microglial (already mapped) activation (complement C5 already mapped) of the fear-circuit hyperactivity of social anxiety disorder."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "CNS-border ECM: periostin, from astrocytes (already mapped) and meningeal fibroblasts, contributes to the perivascular ECM remodelling and the neuroinflammation (IL-6, TNF already mapped) implicated in the synaptic changes of social anxiety disorder."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "SAD prolactin: prolactin, via PRLR on neurons (already mapped) and microglia (already mapped), modulates amygdala reactivity; hyperprolactinaemia amplifies the cortisol (already mapped) and norepinephrine (already mapped) cascade of social anxiety disorder."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "SAD selenium: selenium, as neuroprotective GPx in neurons (already mapped) and microglia (already mapped), scavenges neuroinflammatory ROS; selenium deficiency impairs GABA (already mapped) tone and amplifies the amygdala hyperreactivity of social anxiety disorder."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "SAD iodine: iodine-dependent thyroid hormones modulate serotonergic (serotonin already mapped) and dopaminergic (dopamine already mapped) tone; iodine deficiency impairs cortisol (already mapped) and norepinephrine (already mapped) regulation of social anxiety disorder."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "SAD sodium: high dietary sodium activates brain renin-angiotensin (angiotensin-II already mapped) and the HPA (cortisol already mapped) axis; sodium dysregulation amplifies aldosterone (already mapped) and the norepinephrine (already mapped) cascade of social anxiety disorder."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "SAD potassium: potassium, via Kv channels on neurons (already mapped), regulates GABA (already mapped) interneuron tone; potassium dysregulation amplifies amygdala hyperreactivity and the norepinephrine (already mapped) HPA cascade of social anxiety disorder."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "SAD phosphorus: phosphorus, as ATP in neurons (already mapped) and synapses (already mapped), sustains the energetics of HPA (cortisol already mapped) and amygdala fear-circuit signalling; phosphorus deficiency impairs the neuronal resilience of social anxiety disorder."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "SAD iron: iron supports neuron (already mapped) serotonin (already mapped) and dopamine (already mapped) synthesis; iron deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and BDNF (already mapped) dysregulation in SAD."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "SAD chloride: chloride, via KCC2 in GABAergic neurons (already mapped), sets inhibitory tone; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and serotonin (already mapped) deficits in social anxiety disorder."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "SAD sulfur: hydrogen sulfide from neurons (already mapped) modulates GABAergic tone; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation, suppressing BDNF (already mapped) and serotonin (already mapped) signalling in SAD."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "SAD nitrogen: nitric oxide, generated in neurons (already mapped), modulates synaptic plasticity; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade and impairs serotonin (already mapped) signalling in SAD."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "SAD carbon: carbon, as metabolic backbone of neurons (already mapped) and macrophages (already mapped), drives synaptic energy metabolism; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) cascade of SAD."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "SAD hydrogen: hydrogen, via redox homeostasis in neurons (already mapped) and macrophages (already mapped), modulates synaptic oxidative stress; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and serotonin (already mapped) cascade of SAD."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "SAD oxygen: ROS from macrophages (already mapped) and neurons (already mapped) drives neuroinflammatory oxidative stress; oxygen-induced ROS amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) signalling cascade of SAD."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "SAD PD-1: PD-1 checkpoint signalling in T-cells (already mapped) and microglia (already mapped) modulates neuroinflammatory tone; PD-1 dysregulation amplifies serotonin (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of social anxiety disorder."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "SAD GLP-1: GLP-1 receptor signalling in neurons (already mapped) and macrophages (already mapped) modulates neurometabolic balance; GLP-1 dysregulation amplifies serotonin (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of social anxiety disorder."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "SAD VEGF: VEGF-driven angiogenesis in neurons (already mapped) and astrocytes (already mapped) modulates neuroplasticity; VEGF dysregulation amplifies serotonin (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of social anxiety disorder."
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
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Stress cytokine: TNF-α is among the inflammatory markers elevated in social anxiety, reflecting how chronic social-evaluative stress feeds systemic inflammation.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Social-stress peptide: vasopressin modulates social behaviour and the stress response, and its signalling is implicated in the heightened social-threat sensitivity of social anxiety disorder.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory link: elevated IL-6 is found in social anxiety, part of the bidirectional relationship between chronic social stress and low-grade systemic inflammation.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Neurosteroid tone: the progesterone metabolite allopregnanolone potentiates GABA-A receptors, so fluctuations in this anxiolytic neurosteroid modulate the threat reactivity of social anxiety disorder.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Fear neuropeptide: substance P acting at NK1 receptors in the amygdala amplifies fear and stress responses, a pathway implicated in anxiety disorders including social anxiety.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Dominance and submission: testosterone shifts social approach and threat vigilance, and lower testosterone tone is linked to the submissive, avoidant behaviour characteristic of social anxiety disorder.
- `connects-to` → **[μ-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — The μ-opioid system mediates the pleasure of social affiliation and the pain of rejection, and blunted μ-opioid signaling is linked to the rejection sensitivity that is central to social anxiety disorder.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen tunes the serotonergic and fear-circuit systems underlying anxiety, contributing to the sex differences and the perimenstrual fluctuation in symptom severity seen in social anxiety disorder.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Social-defeat stress raises IL-1β in fear and reward circuits, part of the neuroimmune response that links chronic social stress to the heightened threat reactivity and avoidance of social anxiety disorder.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Orexin signaling that drives wakefulness and stress reactivity is implicated in anxiety, contributing to the physiological hyperarousal—racing heart, sweating, trembling—that anticipatory social fear triggers.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — CGRP projecting from the parabrachial nucleus into the amygdala signals threat and amplifies fear and avoidance, a neuropeptide arm of the threat circuitry overactive in social anxiety disorder.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Chronic social-defeat stress dysregulates ghrelin, which potentiates fear-memory consolidation, a gut-derived stress hormone linking the social adversity that often precedes social anxiety to its persistent fear learning.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Anticipatory social stress activates the HPA axis (cortisol and CRH already mapped), and glucocorticoid-receptor signaling mediates the cortisol response that characterizes social anxiety disorder.
- `connects-to` → **[β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — The palpitations, tremor and blushing of social anxiety arise from catecholamine activation of β-adrenergic receptors, the target of the β-blockers already mapped for performance anxiety.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Amygdala ERK-MAPK signaling consolidates the fear-conditioned memories of social threat that underlie the persistence and generalization of social anxiety disorder.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4-driven neuroinflammation links systemic and stress-induced inflammation to the cortico-amygdala hyperarousal implicated in social anxiety disorder.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor (NTRK) supports the prefrontal-amygdala plasticity required for fear extinction, the deficient process underlying persistent social fear.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2-regulated antioxidant defenses counter the oxidative stress that accompanies chronic anxiety and HPA-axis overactivation, linking redox imbalance to the persistence of social anxiety.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — BDNF/serotonergic PI3K-AKT-mTOR signaling supports the neuroplasticity that anxiolytic treatment restores in social anxiety disorder.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 reflects the low-grade neuroinflammation associated with chronic anxiety states including social anxiety disorder.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4-MyD88 innate signaling (TLR4 mapped) drives the neuroinflammation increasingly linked to anxiety pathophysiology.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling in limbic circuits shapes the synaptic plasticity and fear-learning balance implicated in social anxiety disorder.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the chronic inflammatory tone associated with the heightened stress reactivity of social anxiety disorder.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic mitochondrial DNA released during chronic stress can engage cGAS-STING, contributing to the neuroinflammation implicated in social anxiety disorder.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress and resilience relevant to the stress vulnerability of social anxiety disorder.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 neuroinflammatory signaling contributes to the inflammatory tone associated with social anxiety disorder.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the inflammatory tone linked to the fear and anxiety circuitry of social anxiety disorder.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and oxidative-stress adaptation participates in the neurobiology of social anxiety disorder.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the low-grade peripheral inflammation associated with social anxiety disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the neuronal plasticity of the fear circuits implicated in social anxiety disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the neurometabolic and stress-adaptation responses relevant to social anxiety disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal stress resilience and fear-circuit homeostasis implicated in social anxiety disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic (early-life-stress) programming implicated in social anxiety disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the synaptic-plasticity mechanisms of the fear and social-behavior circuitry implicated in social anxiety disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with social anxiety disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and neuroplasticity processes implicated in social anxiety disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in social anxiety disorder.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with social anxiety disorder.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the microglial and neuroinflammatory processes implicated in social anxiety disorder.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Brain renin-angiotensin: central angiotensin II modulates the HPA and sympathetic stress response, and angiotensin blockade is associated with lower anxiety, a neuroendocrine axis beyond the monoamine systems already mapped in social anxiety.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Fear circuitry: nitric oxide from neuronal nNOS modulates the amygdala and prefrontal circuits that process social threat, implicating NO signalling in the exaggerated fear response of social anxiety disorder.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Arousal and blushing: central histamine drives arousal and vigilance, systems heightened in the anticipatory anxiety, and peripheral vasomotor responses contribute to the blushing that is a hallmark somatic symptom of social anxiety.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response and threat appraisal exaggerated in social anxiety disorder.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic stress load: chronic anxiety and HPA activation (cortisol already mapped) promote insulin resistance, part of the cardiometabolic burden that can accompany long-standing social anxiety disorder.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Neuroimmune balance: the anti-inflammatory cytokine IL-10 counters the pro-inflammatory TNF, IL-6 and IL-1 (already mapped) reported in anxiety disorders, part of the low-grade neuroinflammation associated with chronic social anxiety.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cardiometabolic burden: the chronic stress and insulin resistance (insulin already mapped) of long-standing social anxiety disorder shift cholesterol handling toward an atherogenic profile, part of its raised cardiovascular risk.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6, TNF and IL-1 already mapped) reported in anxiety modulate the fear and social-threat circuits implicated in social anxiety disorder.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: heightened oxidative stress, to which xanthine oxidase contributes, is reported in anxiety disorders (NRF2 already mapped), and the resulting reactive oxygen species may affect the neurons of the fear circuitry.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation reported in social anxiety disorder.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is part of the type-2 response whose balance against the pro-inflammatory signals shapes the neuroinflammatory dimension of social anxiety disorder.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and noradrenaline: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the noradrenergic arousal (beta1-adrenergic receptor already mapped) of social anxiety disorder.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Anxiolytic adipokine: leptin has anxiolytic actions in the amygdala, linking the metabolic (insulin already mapped) state to the anxiety circuits of social anxiety disorder.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory (IL-6 already mapped) comorbidity of chronic anxiety.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the neuroinflammation (TNF and IL-1 already mapped) associated with social anxiety disorder.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Neuroinflammation: the microglial activation and the neuroinflammation (TNF, IL-6 and IL-1 already mapped) are implicated in the anxiety of social anxiety disorder.
- `connects-to` → **[Panic disorder](../panic-disorder/README.md)** — Anxiety-spectrum overlap: social anxiety disorder and panic disorder are comorbid anxiety disorders, sharing the noradrenergic and serotonergic (already mapped) dysregulation.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Anxiolytic magnesium: magnesium modulates the NMDA/glutamate (already mapped) and the HPA (cortisol already mapped) axis; low magnesium is associated with the anxiety of social anxiety disorder.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in social anxiety disorder.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation (IL-1 and TNF already mapped) associated with social anxiety disorder.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of social anxiety disorder.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with social anxiety disorder.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of social anxiety disorder.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of social anxiety disorder.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the histamine (already mapped) and neuroinflammatory dimension implicated in social anxiety disorder.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic social-evaluative stress of social anxiety disorder.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Stress-modulated NK: the NK-cell number and cytotoxicity, altered by the chronic stress and cortisol (already mapped) reactivity, are part of the peripheral immune dysregulation of social anxiety disorder.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the low-grade complement activation of the neuroinflammation implicated in social anxiety disorder.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial neuroinflammation implicated in the fear circuitry of social anxiety disorder.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the low-grade inflammation of social anxiety disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-anxiety axis: TSLP, from gut-epithelium (gut-microbiome already mapped) and mast cells (already mapped) under the chronic social stress of social anxiety disorder, amplifies the neuroinflammatory and the Th2/mast-cell stress axis of the fear-circuit hyperactivity.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-autonomic axis: bradykinin, via B2R on CNS neurons (already mapped) and microglia (already mapped), modulates the neuroinflammation and the autonomic hyperarousal contributing to the somatic and the cardiovascular symptoms of social anxiety disorder.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3, C5 and factor-H already mapped) contributing to the neuroinflammation and the complement-mediated fear-circuit synaptic remodelling of social anxiety disorder.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Stress erythropoiesis: chronic social anxiety and HPA-axis (cortisol already mapped) dysregulation can alter erythropoietin signalling; EpoR on neurons (already mapped) and microglia (already mapped) mediates neuroprotective effects relevant to the amygdala (brain already mapped) changes of SAD.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement gate: factor H limits alternative-pathway activation at the blood-brain barrier, restraining complement-mediated synaptic pruning and the microglial (already mapped) activation (complement C5 already mapped) of the fear-circuit hyperactivity of social anxiety disorder.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — CNS-border ECM: periostin, from astrocytes (already mapped) and meningeal fibroblasts, contributes to the perivascular ECM remodelling and the neuroinflammation (IL-6, TNF already mapped) implicated in the synaptic changes of social anxiety disorder.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Amygdala reactivity modulator: prolactin, via PRLR on neurons (already mapped) and microglia (already mapped), modulates amygdala reactivity; hyperprolactinaemia amplifies the cortisol (already mapped) and norepinephrine (already mapped) cascade of social anxiety disorder.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Neuroprotective antioxidant: selenium, as neuroprotective GPx in neurons (already mapped) and microglia (already mapped), scavenges neuroinflammatory ROS; selenium deficiency impairs GABA (already mapped) tone and amplifies the amygdala hyperreactivity of social anxiety disorder.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-neurotransmitter axis: iodine-dependent thyroid hormones modulate serotonergic (serotonin already mapped) and dopaminergic (dopamine already mapped) tone; iodine deficiency impairs cortisol (already mapped) and norepinephrine (already mapped) regulation of social anxiety disorder.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — HPA-renin-angiotensin link: high dietary sodium activates brain renin-angiotensin (angiotensin-II already mapped) and the HPA (cortisol already mapped) axis; sodium dysregulation amplifies aldosterone (already mapped) and the norepinephrine (already mapped) cascade of social anxiety disorder.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — GABA interneuron tone: potassium, via Kv channels on neurons (already mapped), regulates GABA (already mapped) interneuron tone; potassium dysregulation amplifies amygdala hyperreactivity and the norepinephrine (already mapped) HPA cascade of social anxiety disorder.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Neuronal energy substrate: phosphorus, as ATP in neurons (already mapped) and synapses (already mapped), sustains the energetics of HPA (cortisol already mapped) and amygdala fear-circuit signalling; phosphorus deficiency impairs the neuronal resilience of social anxiety disorder.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — SAD iron: iron supports neuron (already mapped) serotonin (already mapped) and dopamine (already mapped) synthesis; iron deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and BDNF (already mapped) dysregulation in SAD.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — SAD chloride: chloride, via KCC2 in GABAergic neurons (already mapped), sets inhibitory tone; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and serotonin (already mapped) deficits in social anxiety disorder.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — SAD sulfur: hydrogen sulfide from neurons (already mapped) modulates GABAergic tone; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation, suppressing BDNF (already mapped) and serotonin (already mapped) signalling in SAD.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — SAD nitrogen: nitric oxide, generated in neurons (already mapped), modulates synaptic plasticity; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade and impairs serotonin (already mapped) signalling in SAD.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — SAD carbon: carbon, as metabolic backbone of neurons (already mapped) and macrophages (already mapped), drives synaptic energy metabolism; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) cascade of SAD.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — SAD hydrogen: hydrogen, via redox homeostasis in neurons (already mapped) and macrophages (already mapped), modulates synaptic oxidative stress; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and serotonin (already mapped) cascade of SAD.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — SAD oxygen: ROS from macrophages (already mapped) and neurons (already mapped) drives neuroinflammatory oxidative stress; oxygen-induced ROS amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) signalling cascade of SAD.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — SAD PD-1: PD-1 checkpoint signalling in T-cells (already mapped) and microglia (already mapped) modulates neuroinflammatory tone; PD-1 dysregulation amplifies serotonin (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of social anxiety disorder.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — SAD GLP-1: GLP-1 receptor signalling in neurons (already mapped) and macrophages (already mapped) modulates neurometabolic balance; GLP-1 dysregulation amplifies serotonin (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of social anxiety disorder.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — SAD VEGF: VEGF-driven angiogenesis in neurons (already mapped) and astrocytes (already mapped) modulates neuroplasticity; VEGF dysregulation amplifies serotonin (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of social anxiety disorder.

[^liebowitz-1987-sad-scale]: Liebowitz MR. Social phobia. *Mod Probl Pharmacopsychiatry.* 1987;22:141-173. [PubMed 2885745](https://pubmed.ncbi.nlm.nih.gov/2885745/)
[^stein-2008-sad-review]: Stein MB, Stein DJ. Social anxiety disorder. *Lancet.* 2008;371(9618):1115-1125. [doi:10.1016/S0140-6736(08)60488-2](https://doi.org/10.1016/S0140-6736(08)60488-2) · [PubMed 18374843](https://pubmed.ncbi.nlm.nih.gov/18374843/)
[^goldin-2010-mbsr-sad]: Goldin PR, Gross JJ. Effects of mindfulness-based stress reduction (MBSR) on emotion regulation in social anxiety disorder. *Emotion.* 2010;10(1):83-91. [doi:10.1037/a0018441](https://doi.org/10.1037/a0018441) · [PubMed 20141305](https://pubmed.ncbi.nlm.nih.gov/20141305/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
