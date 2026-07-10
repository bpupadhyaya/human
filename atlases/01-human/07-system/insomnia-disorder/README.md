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
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "An overactive thyroid is a hidden cause of insomnia: excess thyroid hormone speeds metabolism and arousal, causing difficulty falling and staying asleep, so checking thyroid function is part of evaluating new, unexplained chronic insomnia."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Insomnia is a disorder of hyperarousal driven by norepinephrine: an overactive noradrenergic stress system keeps the brain and body too 'switched on' to sleep, which is why insomnia overlaps anxiety and why calming arousal—not just sedation—is the goal."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Sleep and the hippocampus need each other: deep sleep consolidates hippocampal memories, so insomnia's lost sleep impairs learning and memory—and over time poor sleep is linked to hippocampal shrinkage and dementia risk."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes help build the pressure to sleep: they release adenosine during waking and drive the glymphatic flushing of brain waste during sleep, so when this glial housekeeping falters, restorative sleep suffers in insomnia."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium supports the brain's calming systems for sleep: it backs GABA signaling and restrains excitatory NMDA activity, so low magnesium can leave the mind too aroused to settle, which is why it is a common sleep supplement."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Sleep is when synapses are rebalanced: the night's slow-wave sleep prunes and renormalizes synaptic strength built up while awake, so insomnia's lost deep sleep leaves this synaptic housekeeping undone, blunting next-day learning."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Light sets the clock that insomnia fights: photons striking the retina entrain the brain's master circadian pacemaker, so evening screen and blue light suppress melatonin and push sleep later, a leading driver of modern insomnia."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Insomnia wears on the heart: short, broken sleep keeps the sympathetic nervous system and blood pressure elevated overnight, so chronic insomnia raises the long-term risk of hypertension and heart disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Sleep and waking are flipped by competing neurons: wake-promoting orexin neurons and sleep-promoting neurons toggle a switch, and insomnia reflects this circuit stuck toward arousal, unable to flip cleanly into sleep."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency steals sleep: low iron causes restless legs syndrome, whose nighttime urge to move the legs is a common, treatable cause of chronic insomnia."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Lost sleep inflames the brain: chronic insomnia activates microglia, and the impaired overnight clearance of waste that poor sleep brings is linked to a higher risk of neurodegeneration."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Insomnia keeps the stress axis switched on: the adrenal glands pour out cortisol when sleep runs short, and this hyperarousal both drives and follows the inability to sleep."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D status tracks with sleep: deficiency is linked to shorter, poorer sleep, and vitamin D receptors in the brain's sleep-regulating regions suggest the vitamin helps set the timing and depth of rest."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut and sleep talk both ways: through the gut-brain axis the intestinal microbiome shapes the serotonin and melatonin precursors that govern sleep, while poor sleep in turn disturbs the gut, a two-way loop."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium helps the brain make its sleep hormone: it is a cofactor in the pineal gland's conversion of serotonin to melatonin, so calcium availability influences the nightly melatonin surge that triggers sleep."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Reflux and insomnia feed each other: lying down lets stomach acid rise into the esophagus, and the resulting nocturnal heartburn fragments sleep — while poor sleep in turn heightens the gut's sensitivity to it."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Lost sleep unbalances blood sugar: even short-term sleep restriction worsens insulin sensitivity, straining the pancreas and helping explain why chronic insomnia tracks with a higher risk of type 2 diabetes."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hormonal tides disturb women's sleep: insomnia spikes around menstruation, in pregnancy, and especially at menopause, when falling estrogen and night-time hot flashes repeatedly break the night."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Sleep loss weakens the immune memory: poor sleep around vaccination blunts the antibody response, and chronic insomnia's immune dysregulation leaves the body less protected — one reason rest is urged around an immunization."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Broken sleep wears on the heart: chronic insomnia raises blood pressure and sympathetic tone, and is linked to a higher risk of hypertension, heart attack, and stroke over the years."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut and sleep talk both ways: the microbiome shapes serotonin and melatonin and the circadian rhythm, while sleep loss in turn shifts the flora — a gut-brain loop increasingly tied to insomnia."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Lost sleep inflames the body: insomnia and short sleep raise IL-6 and other inflammatory markers, a low-grade activation that helps explain the cardiovascular and metabolic toll of chronic poor sleep."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Sleep falls apart early in Parkinson's: insomnia and REM-sleep behavior disorder often precede the motor disease by years, and the degeneration of sleep-regulating brainstem nuclei makes broken sleep a core feature."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pain and sleeplessness feed each other: chronic neuropathic pain fragments sleep while poor sleep lowers the pain threshold, a reciprocal loop that makes treating one essential to relieving the other."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Lost sleep lights an inflammatory fire: sleep deprivation activates the NLRP3 inflammasome and raises IL-1β and IL-6, the low-grade inflammation through which chronic insomnia feeds cardiovascular and metabolic disease."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Sleeplessness wears on the brain's vessels: chronic insomnia and short sleep independently raise the risk of stroke through hypertension, inflammation and autonomic strain, beyond their toll on the heart."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Sleep tunes adaptive immunity: deep sleep supports helper T-cell function and immune memory, so chronic insomnia blunts T-cell responses and weakens vaccine protection and infection defense."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Lost sleep switches on inflammation: even partial sleep deprivation activates NF-κB in circulating immune cells, raising inflammatory cytokines — a molecular route from chronic insomnia to its cardiovascular and metabolic risk."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Sleeplessness and panic feed each other: insomnia both precedes and worsens panic disorder, with nighttime arousal and fear of nocturnal panic attacks fracturing sleep further."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Failing kidneys steal sleep: insomnia is strikingly common in chronic kidney disease, driven by restless legs, pruritus, disturbed melatonin and the rhythm disruption of dialysis, and poor sleep in turn worsens outcomes."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Sleep loss and the failing heart feed each other: orthopnea and nocturnal breathlessness fragment sleep in heart failure, while chronic insomnia's sympathetic overdrive worsens cardiac load — a two-way harm."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Poor sleep triggers the headache: insomnia and migraine are strongly bidirectional, with sleep deprivation a classic migraine trigger and the dread of nocturnal attacks fracturing sleep further."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Disrupted sleep is woven into psychosis: insomnia and fragmented sleep architecture are near-universal in schizophrenia, often heralding relapse, reflecting the same circadian and dopaminergic dysregulation that drives the illness."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Lost sleep inflames the arteries: chronic short and fragmented sleep raises blood pressure, sympathetic tone and inflammation, accelerating atherosclerosis and the cardiovascular risk tied to insomnia."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Breathlessness and nocturnal symptoms steal sleep: insomnia is highly prevalent in COPD, where cough, hypoxia and the stimulant effects of bronchodilators fragment sleep, and poor sleep worsens daytime function."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Sleep is when the body repairs: deep sleep drives growth-hormone release and immune function, so chronic insomnia and sleep loss measurably slow wound healing and tissue repair."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Sleep is governed by and governs the hormones: melatonin and the cortisol rhythm time sleep, while chronic insomnia dysregulates the HPA axis and appetite hormones, and thyrotoxicosis itself causes insomnia."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The gut and sleep disturb each other: nocturnal gastro-oesophageal reflux fragments sleep, and a bidirectional link ties insomnia to irritable bowel syndrome through the gut-brain axis."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "Sleep and attention are tightly entangled: insomnia and delayed sleep are very common in ADHD, the stimulants used to treat it can worsen sleep onset, and sleep loss in turn worsens inattention."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It often hides sleep apnoea: insomnia frequently coexists with obstructive sleep apnoea — comorbid insomnia and sleep apnoea (COMISA) — and each worsens the other and resists single treatments."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Sleeplessness amplifies pain: poor sleep lowers the pain threshold and worsens chronic musculoskeletal pain, while that pain disrupts sleep in turn, a self-reinforcing loop."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Lost sleep shows on the skin: sleep deprivation flares inflammatory skin disease and the itch of eczema disrupts sleep in return, and chronic sleep loss accelerates skin ageing."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Sleep cleans the brain: the glymphatic system clears metabolic waste, including amyloid-beta, most actively during deep sleep, so chronic insomnia may impair this nightly housekeeping."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "A full bladder breaks sleep: nocturia is a leading cause of fragmented sleep, and the kidney's circadian fall in night-time urine output is itself disturbed by poor sleep."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "Diet draws interest: magnesium supplementation has been trialled as a gentle sleep aid, with modest evidence for easing insomnia in older adults."
  - target: 03-medicine/02-traditional/ashwagandha
    relation: connects-to
    note: "A traditional herb that aids sleep: ashwagandha root extract improves sleep onset and quality in trials, acting partly by lowering cortisol, and is among the better-studied natural sleep aids."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Intrusive thoughts steal sleep: insomnia is common in OCD, where night-time rumination and compulsions delay sleep onset, and poor sleep in turn worsens obsessive symptoms."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Anticipatory worry keeps it awake: people with social anxiety frequently have insomnia, as pre-event dread and rumination raise arousal at bedtime in a self-reinforcing cycle."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Stimulants steal sleep: caffeine, nicotine and stimulant drugs delay sleep onset and fragment sleep, and stimulant use disorder both causes chronic insomnia and is sometimes driven by it as people self-medicate daytime fatigue."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "A double-edged sleep aid: many use cannabis to fall asleep, but tolerance develops and withdrawal causes rebound insomnia and vivid dreams, tying cannabis use disorder tightly to disordered sleep."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "Night-time arousal and eating intertwine: insomnia and night-eating reinforce each other, as disrupted sleep and circadian-orexin signalling drive the evening overeating of binge-eating disorder."
  - target: 01-human/07-system/internet-gaming-disorder
    relation: connects-to
    note: "Screens that steal sleep: late-night gaming arousal and blue light delay sleep onset, and insomnia and problematic gaming are tightly comorbid, each feeding the other in a vicious cycle."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Bad sleep, electrical heart risk: chronic insomnia and short sleep raise sympathetic tone, predisposing to hypertension, atrial fibrillation and other arrhythmias of the conduction system."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Opioids wreck sleep architecture: opioids suppress REM and deep sleep and worsen sleep apnoea, while withdrawal causes severe insomnia—sleep disturbance both drives and follows opioid use."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Sleep loss and seizures: sleep deprivation lowers the seizure threshold and triggers attacks in epilepsy, while seizures and antiseizure drugs fragment sleep—a bidirectional vicious cycle."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Nocturnal worsening: asthma and COPD symptoms peak overnight, fragmenting sleep, while poor sleep heightens airway inflammation—insomnia and chronic airway disease reinforce each other."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Pandemic and post-viral sleeplessness: COVID-19 sharply raised insomnia through stress and isolation ('coronasomnia'), and long-COVID neuroinflammation can leave persistent sleep disruption."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Restless legs from low iron: iron deficiency causes restless legs syndrome, a major driver of sleep-onset insomnia that often resolves once iron stores are repleted."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Menopausal sleeplessness: falling oestrogen and progesterone at menopause, with hot flushes and night sweats, are a leading cause of insomnia in midlife women."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Sleeplessness strains the heart: chronic insomnia independently raises the risk of hypertension, myocardial infarction and heart failure through sympathetic overactivity and inflammation."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Hyperarousal axis: insomnia is a disorder of hyperarousal driven by overactive CRH and HPA-axis signalling, the stress hormone keeping the brain alert when it should sleep."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Somnogenic cytokine: IL-1β is a physiological sleep regulator, and the dysregulated immune signalling of chronic insomnia disturbs the cytokine balance that normally promotes restorative sleep."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Sleep-regulatory inflammation: TNF-α normally promotes sleep, and its disruption in chronic insomnia both reflects and feeds the low-grade inflammation that raises cardiometabolic risk."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Cortical hyperarousal: elevated glutamatergic tone underlies the cortical hyperarousal central to insomnia, keeping the brain in a wake-like state and opposing the inhibitory drive that initiates sleep."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Wake drive: dopaminergic signalling promotes wakefulness and arousal, and its tone in the evening contributes to the difficulty falling asleep that characterises insomnia."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Sleep-loss metabolism: the curtailed sleep of insomnia raises ghrelin and lowers satiety signalling, driving the appetite and weight changes that link poor sleep to metabolic disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Sleep-promoting prostanoid: prostaglandin D2 is among the most potent endogenous sleep-inducing substances, acting on the basal forebrain to promote non-REM sleep, a system whose deficiency contributes to insomnia."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid sedation: the progesterone metabolite allopregnanolone is a positive GABA-A modulator with sedative effects, and falling progesterone in the luteal phase and menopause is linked to the insomnia common at those times."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "Sleep architecture: endocannabinoid signalling through CB1 receptors modulates sleep-wake regulation and slow-wave sleep, part of the circuitry whose dysregulation contributes to disturbed sleep in insomnia."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Menopausal insomnia: falling estrogen disrupts sleep architecture and thermoregulation, driving the vasomotor hot flushes and the surge in insomnia that accompany the menopausal transition, one of the commonest secondary causes of disturbed sleep in women."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid arousal: thyroid hormone excess raises metabolic rate and sympathetic arousal that fragment sleep, making hyperthyroidism a classic medical cause of insomnia that should be excluded before treating it as primary."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Circadian output: vasopressin is a key output neuropeptide of the suprachiasmatic-nucleus master clock, and its rhythmic signalling helps set the circadian timing whose misalignment underlies circadian-pattern insomnia."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Hyperarousal axis: the cortisol/CRH hyperarousal of insomnia (already mapped) acts through the glucocorticoid receptor, the HPA-axis overactivity that both causes and is worsened by chronic sleep loss."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Sleep-dependent plasticity: sleep regulates BDNF-dependent synaptic plasticity and memory consolidation, and the disrupted sleep of insomnia impairs this restorative function, linking it to the cognitive and mood symptoms of the disorder."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Synaptic restoration: sleep promotes mTOR-dependent protein synthesis that restores synaptic and cellular homeostasis, a recuperative process curtailed by the chronic sleep loss of insomnia."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Inflammatory hyperarousal: TLR4-driven neuroinflammation links the systemic low-grade inflammation of chronic sleep loss to the cortical hyperarousal that perpetuates insomnia, a bidirectional sleep-immune loop."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Sleep-dependent plasticity: BDNF signalling through its TrkB receptor (NTRK) mediates the sleep-dependent synaptic plasticity and slow-wave homeostasis that chronic insomnia degrades."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Arousal dampening: neuropeptide Y opposes CRH-driven arousal (CRH already mapped) and promotes sleep onset, and deficient NPY-mediated calming contributes to the stress-related hyperarousal of insomnia."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (mTOR mapped) participates in the synaptic and homeostatic regulation of sleep-wake states disrupted in insomnia."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 reflects the low-grade neuroinflammation linked to chronic sleep loss and insomnia."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Sleep deprivation generates oxidative stress that NRF2 antioxidant defences counter, linking insomnia to redox imbalance and its systemic consequences."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β is a core regulator of the circadian clock and of arousal-related plasticity, linking its activity to the hyperarousal of insomnia disorder."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the low-grade systemic inflammation that both results from and reinforces chronic sleep loss in insomnia disorder."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Sleep-loss-associated cellular stress can engage cGAS-STING, contributing to the neuroinflammatory consequences of chronic insomnia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress handling relevant to the hyperarousal and stress physiology of insomnia disorder."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 neuroinflammatory signaling contributes to the inflammatory tone associated with chronic insomnia disorder."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the inflammatory tone linked to the sleep-wake dysregulation of insomnia disorder."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and oxidative-stress adaptation participates in the hyperarousal neurobiology of insomnia disorder."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the low-grade peripheral inflammation associated with chronic insomnia disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the neuronal plasticity and circadian-related pathways relevant to insomnia disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the sleep-wake energy homeostasis dysregulated in insomnia disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy, which follows a circadian rhythm and is modulated by sleep, participates in the neuronal homeostasis disrupted in insomnia disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of circadian and stress genes implicated in insomnia disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the synaptic-plasticity and arousal-circuit mechanisms implicated in insomnia disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the low-grade neuroinflammation associated with insomnia disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune processes implicated in insomnia disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory processes implicated in insomnia disorder."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with insomnia disorder."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the microglial and neuroinflammatory processes implicated in insomnia disorder."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Sleep and metabolism: sleep restriction lowers leptin and raises appetite (ghrelin already mapped), linking chronic insomnia to weight gain and metabolic dysregulation in a bidirectional sleep-metabolism relationship."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Sleep homeostasis: nitric oxide in the basal forebrain and brainstem participates in the buildup of sleep pressure and the sleep-wake switch, one of the gaseous modulators of sleep regulation."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sleep-dependent secretion: testosterone release peaks during sleep, so the fragmented sleep of insomnia lowers testosterone, and low testosterone in turn worsens sleep quality, a reciprocal endocrine link."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic consequence: short and disrupted sleep in insomnia promotes insulin resistance and impaired glucose tolerance, part of the metabolic burden that links chronic insomnia to the raised risk of type 2 diabetes (already mapped)."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Neuroimmune balance: sleep loss shifts the cytokine balance, raising the pro-inflammatory IL-6 and TNF (already mapped) that IL-10 normally restrains, contributing to the low-grade inflammation associated with chronic insomnia."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: sleep deprivation increases oxidative stress, to which xanthine-oxidase-derived reactive oxygen species contribute, one mechanism proposed to link chronic insomnia to accelerated cellular ageing and cardiometabolic risk."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Cardiometabolic risk: chronic insomnia and the insulin resistance (insulin already mapped) of sleep loss shift cholesterol handling toward an atherogenic profile, part of the cardiovascular and metabolic burden associated with poor sleep."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Stress-axis mineralocorticoid arm: aldosterone acting on brain mineralocorticoid receptors, balanced against the glucocorticoid signalling (cortisol and CRH already mapped), tunes the HPA-axis hyperarousal that maintains chronic insomnia."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Sleep-metabolism link: sleep loss disturbs the appetite and incretin signalling (ghrelin and leptin already mapped), and the GLP-1 axis links the metabolic dysregulation of chronic insomnia to its appetite and weight effects."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Sleep-immune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the sleep-regulatory pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped), part of the bidirectional link between sleep and inflammation in insomnia."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), forms the type-2 response whose balance against the pro-inflammatory sleep-regulatory cytokines shapes the neuroimmune dimension of chronic insomnia."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and sleep: zinc modulates the glutamatergic (already mapped) and GABAergic (already mapped) systems and, with magnesium (already mapped), influences sleep quality, its status linked to the sleep disturbance of insomnia."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and monoamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), and disturbed copper handling affects the monoaminergic arousal system of the sleep-wake balance in insomnia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic consequence: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic (insulin already mapped) consequences of the chronic sleep loss of insomnia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin rises with sleep deprivation, part of the metabolic-inflammatory (IL-6 already mapped) consequences of the chronic sleep loss of insomnia."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Adenosine sleep pressure: the astrocytes release and regulate the adenosine (already mapped), the sleep-pressure signal accumulating during the wakefulness that is dysregulated in insomnia."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety comorbidity: generalized anxiety disorder and insomnia are highly comorbid, sharing the hyperarousal and the HPA (cortisol already mapped) dysregulation."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Metabolic consequence: the chronic sleep loss of insomnia raises the type 2 diabetes and metabolic-syndrome risk (the insulin, leptin and adiponectin already mapped dysregulation)."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate sleep-immune: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, disrupts the sleep and drives the fatigue, linking the innate immunity to the neuroinflammation of insomnia."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation (IL-1 and TNF already mapped, the sleep cytokines) associated with insomnia."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of the chronic sleep loss of insomnia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the chronic sleep loss of insomnia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of insomnia."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of insomnia."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the histamine (already mapped) and neuroinflammatory dimension implicated in the hyperarousal of insomnia."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic hyperarousal of insomnia."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Sleep-modulated NK: the NK-cell number and cytotoxicity, reduced by the sleep loss and altered by the cortisol (already mapped) rhythm, are part of the immune consequences of insomnia."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the low-grade complement activation of the systemic inflammation associated with chronic insomnia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) neuroinflammation implicated in the hyperarousal of insomnia."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the low-grade inflammation of chronic insomnia."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-hyperarousal axis: TSLP, from skin (already mapped) and gut (already mapped) epithelial barriers under the chronic stress of insomnia, primes mast cells (already mapped) and dendritic cells (already mapped) and amplifies the neuroinflammatory hyperarousal of insomnia."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-sleep axis: bradykinin, via B2R on CNS neurons (already mapped) and microglia (already mapped), modulates the neuroinflammation and the autonomic arousal contributing to the sleep-onset and sleep-maintenance difficulties of insomnia disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3 and C5 already mapped) contributing to the neuroinflammation and the complement-mediated synaptic pruning of the hyperarousal circuitry of insomnia."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Sleep-EPO axis: EPO and its receptor on neurons (already mapped) and microglia (already mapped) have neuroprotective effects; the anaemia comorbid with insomnia elevates EPO, adding a neuroendocrine dimension to the hyperarousal of insomnia."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "CNS-border matrix: periostin, from astrocytes (already mapped) and meningeal fibroblasts, remodels the neuroimmune-interface ECM and contributes to the low-grade neuroinflammation (IL-6, TNF already mapped) implicated in chronic insomnia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement gate: factor H limits alternative-pathway activation at the blood-brain barrier, restraining complement-mediated synaptic pruning and the microglial (already mapped) activation (C3 and C5 already mapped) of the hyperarousal of insomnia."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Insomnia prolactin: prolactin, sleep-entrained with melatonin (already mapped), promotes NREM slow-wave sleep via GABA (already mapped) and adenosine (already mapped) pathways; prolactin deficiency amplifies the cortisol (already mapped) HPA hyperarousal of insomnia."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Insomnia oxytocin: oxytocin, via OXTR on neurons (already mapped) and astrocytes (already mapped), reduces hypothalamic arousal and promotes sleep onset; oxytocin attenuates the cortisol (already mapped) and norepinephrine (already mapped) hyperarousal of chronic insomnia."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Insomnia selenium: selenium, as neuroprotective GPx in neurons (already mapped) and astrocytes (already mapped), scavenges neuroinflammatory (IL-6 and TNF already mapped) ROS; selenium deficiency impairs the GABA (already mapped) inhibitory tone and worsens insomnia hyperarousal."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Insomnia iodine: iodine-dependent thyroid hormones regulate neuronal (neuron already mapped) excitability and GABA (already mapped) inhibitory tone; hypothyroidism, common in insomnia, amplifies NF-κB (already mapped) and cortisol (already mapped) HPA hyperarousal."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Insomnia sodium: sodium, via voltage-gated channels on neurons (already mapped) and astrocytes (already mapped), determines action-potential firing in sleep-wake circuits; disrupted sodium from microglial (already mapped) NF-κB (already mapped) neuroinflammation worsens insomnia."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Insomnia potassium: potassium efflux activates NLRP3 inflammasome (already mapped) in microglia (already mapped); disrupted K⁺ at synapses (already mapped) and neurons (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and insomnia."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Insomnia phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and microglia (already mapped), supports synaptic energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of insomnia disorder."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Insomnia chloride: chloride, via GABA-A Cl⁻ influx in neurons (already mapped), maintains inhibitory tone; chloride dysregulation in microglia (already mapped) amplifies the NF-κB (already mapped) and IL-6 (already mapped) arousal cascade of insomnia disorder."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Insomnia sulfur: sulfur, as cysteine precursor in neurons (already mapped) and microglia (already mapped), supports GABA (already mapped) modulation; sulfur deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of insomnia."
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
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — An overactive thyroid is a hidden cause of insomnia: excess thyroid hormone speeds metabolism and arousal, causing difficulty falling and staying asleep, so checking thyroid function is part of evaluating new, unexplained chronic insomnia.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Insomnia is a disorder of hyperarousal driven by norepinephrine: an overactive noradrenergic stress system keeps the brain and body too 'switched on' to sleep, which is why insomnia overlaps anxiety and why calming arousal—not just sedation—is the goal.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Sleep and the hippocampus need each other: deep sleep consolidates hippocampal memories, so insomnia's lost sleep impairs learning and memory—and over time poor sleep is linked to hippocampal shrinkage and dementia risk.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes help build the pressure to sleep: they release adenosine during waking and drive the glymphatic flushing of brain waste during sleep, so when this glial housekeeping falters, restorative sleep suffers in insomnia.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium supports the brain's calming systems for sleep: it backs GABA signaling and restrains excitatory NMDA activity, so low magnesium can leave the mind too aroused to settle, which is why it is a common sleep supplement.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Sleep is when synapses are rebalanced: the night's slow-wave sleep prunes and renormalizes synaptic strength built up while awake, so insomnia's lost deep sleep leaves this synaptic housekeeping undone, blunting next-day learning.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Light sets the clock that insomnia fights: photons striking the retina entrain the brain's master circadian pacemaker, so evening screen and blue light suppress melatonin and push sleep later, a leading driver of modern insomnia.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Insomnia wears on the heart: short, broken sleep keeps the sympathetic nervous system and blood pressure elevated overnight, so chronic insomnia raises the long-term risk of hypertension and heart disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Sleep and waking are flipped by competing neurons: wake-promoting orexin neurons and sleep-promoting neurons toggle a switch, and insomnia reflects this circuit stuck toward arousal, unable to flip cleanly into sleep.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency steals sleep: low iron causes restless legs syndrome, whose nighttime urge to move the legs is a common, treatable cause of chronic insomnia.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Lost sleep inflames the brain: chronic insomnia activates microglia, and the impaired overnight clearance of waste that poor sleep brings is linked to a higher risk of neurodegeneration.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Insomnia keeps the stress axis switched on: the adrenal glands pour out cortisol when sleep runs short, and this hyperarousal both drives and follows the inability to sleep.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D status tracks with sleep: deficiency is linked to shorter, poorer sleep, and vitamin D receptors in the brain's sleep-regulating regions suggest the vitamin helps set the timing and depth of rest.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut and sleep talk both ways: through the gut-brain axis the intestinal microbiome shapes the serotonin and melatonin precursors that govern sleep, while poor sleep in turn disturbs the gut, a two-way loop.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium helps the brain make its sleep hormone: it is a cofactor in the pineal gland's conversion of serotonin to melatonin, so calcium availability influences the nightly melatonin surge that triggers sleep.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Reflux and insomnia feed each other: lying down lets stomach acid rise into the esophagus, and the resulting nocturnal heartburn fragments sleep — while poor sleep in turn heightens the gut's sensitivity to it.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Lost sleep unbalances blood sugar: even short-term sleep restriction worsens insulin sensitivity, straining the pancreas and helping explain why chronic insomnia tracks with a higher risk of type 2 diabetes.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hormonal tides disturb women's sleep: insomnia spikes around menstruation, in pregnancy, and especially at menopause, when falling estrogen and night-time hot flashes repeatedly break the night.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Sleep loss weakens the immune memory: poor sleep around vaccination blunts the antibody response, and chronic insomnia's immune dysregulation leaves the body less protected — one reason rest is urged around an immunization.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Broken sleep wears on the heart: chronic insomnia raises blood pressure and sympathetic tone, and is linked to a higher risk of hypertension, heart attack, and stroke over the years.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut and sleep talk both ways: the microbiome shapes serotonin and melatonin and the circadian rhythm, while sleep loss in turn shifts the flora — a gut-brain loop increasingly tied to insomnia.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Lost sleep inflames the body: insomnia and short sleep raise IL-6 and other inflammatory markers, a low-grade activation that helps explain the cardiovascular and metabolic toll of chronic poor sleep.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Sleep falls apart early in Parkinson's: insomnia and REM-sleep behavior disorder often precede the motor disease by years, and the degeneration of sleep-regulating brainstem nuclei makes broken sleep a core feature.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pain and sleeplessness feed each other: chronic neuropathic pain fragments sleep while poor sleep lowers the pain threshold, a reciprocal loop that makes treating one essential to relieving the other.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Lost sleep lights an inflammatory fire: sleep deprivation activates the NLRP3 inflammasome and raises IL-1β and IL-6, the low-grade inflammation through which chronic insomnia feeds cardiovascular and metabolic disease.
- `connects-to` → **[Stroke](../stroke/README.md)** — Sleeplessness wears on the brain's vessels: chronic insomnia and short sleep independently raise the risk of stroke through hypertension, inflammation and autonomic strain, beyond their toll on the heart.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Sleep tunes adaptive immunity: deep sleep supports helper T-cell function and immune memory, so chronic insomnia blunts T-cell responses and weakens vaccine protection and infection defense.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Lost sleep switches on inflammation: even partial sleep deprivation activates NF-κB in circulating immune cells, raising inflammatory cytokines — a molecular route from chronic insomnia to its cardiovascular and metabolic risk.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Sleeplessness and panic feed each other: insomnia both precedes and worsens panic disorder, with nighttime arousal and fear of nocturnal panic attacks fracturing sleep further.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Failing kidneys steal sleep: insomnia is strikingly common in chronic kidney disease, driven by restless legs, pruritus, disturbed melatonin and the rhythm disruption of dialysis, and poor sleep in turn worsens outcomes.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Sleep loss and the failing heart feed each other: orthopnea and nocturnal breathlessness fragment sleep in heart failure, while chronic insomnia's sympathetic overdrive worsens cardiac load — a two-way harm.
- `connects-to` → **[Migraine](../migraine/README.md)** — Poor sleep triggers the headache: insomnia and migraine are strongly bidirectional, with sleep deprivation a classic migraine trigger and the dread of nocturnal attacks fracturing sleep further.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Disrupted sleep is woven into psychosis: insomnia and fragmented sleep architecture are near-universal in schizophrenia, often heralding relapse, reflecting the same circadian and dopaminergic dysregulation that drives the illness.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Lost sleep inflames the arteries: chronic short and fragmented sleep raises blood pressure, sympathetic tone and inflammation, accelerating atherosclerosis and the cardiovascular risk tied to insomnia.
- `connects-to` → **[COPD](../copd/README.md)** — Breathlessness and nocturnal symptoms steal sleep: insomnia is highly prevalent in COPD, where cough, hypoxia and the stimulant effects of bronchodilators fragment sleep, and poor sleep worsens daytime function.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Sleep is when the body repairs: deep sleep drives growth-hormone release and immune function, so chronic insomnia and sleep loss measurably slow wound healing and tissue repair.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Sleep is governed by and governs the hormones: melatonin and the cortisol rhythm time sleep, while chronic insomnia dysregulates the HPA axis and appetite hormones, and thyrotoxicosis itself causes insomnia.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The gut and sleep disturb each other: nocturnal gastro-oesophageal reflux fragments sleep, and a bidirectional link ties insomnia to irritable bowel syndrome through the gut-brain axis.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — Sleep and attention are tightly entangled: insomnia and delayed sleep are very common in ADHD, the stimulants used to treat it can worsen sleep onset, and sleep loss in turn worsens inattention.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It often hides sleep apnoea: insomnia frequently coexists with obstructive sleep apnoea — comorbid insomnia and sleep apnoea (COMISA) — and each worsens the other and resists single treatments.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Sleeplessness amplifies pain: poor sleep lowers the pain threshold and worsens chronic musculoskeletal pain, while that pain disrupts sleep in turn, a self-reinforcing loop.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Lost sleep shows on the skin: sleep deprivation flares inflammatory skin disease and the itch of eczema disrupts sleep in return, and chronic sleep loss accelerates skin ageing.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Sleep cleans the brain: the glymphatic system clears metabolic waste, including amyloid-beta, most actively during deep sleep, so chronic insomnia may impair this nightly housekeeping.
- `connects-to` → **[Renal System](../renal-system/README.md)** — A full bladder breaks sleep: nocturia is a leading cause of fragmented sleep, and the kidney's circadian fall in night-time urine output is itself disturbed by poor sleep.
- `connects-to` → **[Dietary Magnesium](../../../03-medicine/03-food/magnesium-dietary/README.md)** — Diet draws interest: magnesium supplementation has been trialled as a gentle sleep aid, with modest evidence for easing insomnia in older adults.
- `connects-to` → **[Ashwagandha](../../../03-medicine/02-traditional/ashwagandha/README.md)** — A traditional herb that aids sleep: ashwagandha root extract improves sleep onset and quality in trials, acting partly by lowering cortisol, and is among the better-studied natural sleep aids.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Intrusive thoughts steal sleep: insomnia is common in OCD, where night-time rumination and compulsions delay sleep onset, and poor sleep in turn worsens obsessive symptoms.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — Anticipatory worry keeps it awake: people with social anxiety frequently have insomnia, as pre-event dread and rumination raise arousal at bedtime in a self-reinforcing cycle.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Stimulants steal sleep: caffeine, nicotine and stimulant drugs delay sleep onset and fragment sleep, and stimulant use disorder both causes chronic insomnia and is sometimes driven by it as people self-medicate daytime fatigue.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — A double-edged sleep aid: many use cannabis to fall asleep, but tolerance develops and withdrawal causes rebound insomnia and vivid dreams, tying cannabis use disorder tightly to disordered sleep.
- `connects-to` → **[Binge Eating Disorder](../binge-eating-disorder/README.md)** — Night-time arousal and eating intertwine: insomnia and night-eating reinforce each other, as disrupted sleep and circadian-orexin signalling drive the evening overeating of binge-eating disorder.
- `connects-to` → **[Internet Gaming Disorder](../internet-gaming-disorder/README.md)** — Screens that steal sleep: late-night gaming arousal and blue light delay sleep onset, and insomnia and problematic gaming are tightly comorbid, each feeding the other in a vicious cycle.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Bad sleep, electrical heart risk: chronic insomnia and short sleep raise sympathetic tone, predisposing to hypertension, atrial fibrillation and other arrhythmias of the conduction system.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Opioids wreck sleep architecture: opioids suppress REM and deep sleep and worsen sleep apnoea, while withdrawal causes severe insomnia—sleep disturbance both drives and follows opioid use.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Sleep loss and seizures: sleep deprivation lowers the seizure threshold and triggers attacks in epilepsy, while seizures and antiseizure drugs fragment sleep—a bidirectional vicious cycle.
- `connects-to` → **[Asthma](../asthma/README.md)** — Nocturnal worsening: asthma and COPD symptoms peak overnight, fragmenting sleep, while poor sleep heightens airway inflammation—insomnia and chronic airway disease reinforce each other.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Pandemic and post-viral sleeplessness: COVID-19 sharply raised insomnia through stress and isolation ('coronasomnia'), and long-COVID neuroinflammation can leave persistent sleep disruption.
- `connects-to` → **[Iron-Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Restless legs from low iron: iron deficiency causes restless legs syndrome, a major driver of sleep-onset insomnia that often resolves once iron stores are repleted.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Menopausal sleeplessness: falling oestrogen and progesterone at menopause, with hot flushes and night sweats, are a leading cause of insomnia in midlife women.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Sleeplessness strains the heart: chronic insomnia independently raises the risk of hypertension, myocardial infarction and heart failure through sympathetic overactivity and inflammation.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Hyperarousal axis: insomnia is a disorder of hyperarousal driven by overactive CRH and HPA-axis signalling, the stress hormone keeping the brain alert when it should sleep.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Somnogenic cytokine: IL-1β is a physiological sleep regulator, and the dysregulated immune signalling of chronic insomnia disturbs the cytokine balance that normally promotes restorative sleep.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Sleep-regulatory inflammation: TNF-α normally promotes sleep, and its disruption in chronic insomnia both reflects and feeds the low-grade inflammation that raises cardiometabolic risk.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Cortical hyperarousal: elevated glutamatergic tone underlies the cortical hyperarousal central to insomnia, keeping the brain in a wake-like state and opposing the inhibitory drive that initiates sleep.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Wake drive: dopaminergic signalling promotes wakefulness and arousal, and its tone in the evening contributes to the difficulty falling asleep that characterises insomnia.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Sleep-loss metabolism: the curtailed sleep of insomnia raises ghrelin and lowers satiety signalling, driving the appetite and weight changes that link poor sleep to metabolic disease.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Prostaglandin D2 is among the most potent endogenous sleep-inducing substances, acting on the basal forebrain to promote non-REM sleep—a sleep-promoting system whose insufficiency contributes to the difficulty achieving restorative sleep in insomnia.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — The progesterone metabolite allopregnanolone is a positive GABA-A modulator with sedative effects, and the falling progesterone of the late luteal phase and menopause is linked to the insomnia that commonly emerges at those times.
- `connects-to` → **[Endocannabinoid](../../03-molecular/endocannabinoid/README.md)** — Endocannabinoid signaling through CB1 receptors modulates sleep-wake regulation and slow-wave sleep, part of the circuitry whose dysregulation contributes to the disturbed sleep architecture of insomnia disorder.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Falling estrogen disrupts sleep architecture and thermoregulation, driving the vasomotor hot flushes and the surge in insomnia that accompany the menopausal transition, one of the commonest secondary causes of disturbed sleep in women.
- `connects-to` → **[Thyroid hormones](../../03-molecular/thyroid-hormones/README.md)** — Thyroid hormone excess raises metabolic rate and sympathetic arousal that fragment sleep, making hyperthyroidism a classic medical cause of insomnia that should be excluded before treating it as primary.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Vasopressin is a key output neuropeptide of the suprachiasmatic-nucleus master clock, and its rhythmic signaling helps set the circadian timing whose misalignment underlies circadian-pattern insomnia.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — The cortisol/CRH hyperarousal of insomnia (already mapped) acts through the glucocorticoid receptor, the HPA-axis overactivity that both causes and is worsened by chronic sleep loss.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Sleep regulates BDNF-dependent synaptic plasticity and memory consolidation, and the disrupted sleep of insomnia impairs this restorative function, linking it to the cognitive and mood symptoms of the disorder.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Sleep promotes mTOR-dependent protein synthesis that restores synaptic and cellular homeostasis, a recuperative process curtailed by the chronic sleep loss of insomnia.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4-driven neuroinflammation links the systemic low-grade inflammation of chronic sleep loss to the cortical hyperarousal that perpetuates insomnia, a bidirectional sleep-immune loop.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor (NTRK) mediates the sleep-dependent synaptic plasticity and slow-wave homeostasis that chronic insomnia degrades.
- `connects-to` → **[Neuropeptide Y](../../03-molecular/npy/README.md)** — Neuropeptide Y opposes CRH-driven arousal (CRH already mapped) and promotes sleep onset, and deficient NPY-mediated calming contributes to the stress-related hyperarousal of insomnia.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-mTOR signaling (mTOR mapped) participates in the synaptic and homeostatic regulation of sleep-wake states disrupted in insomnia.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 reflects the low-grade neuroinflammation linked to chronic sleep loss and insomnia.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Sleep deprivation generates oxidative stress that NRF2 antioxidant defenses counter, linking insomnia to redox imbalance and its systemic consequences.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β is a core regulator of the circadian clock and of arousal-related plasticity, linking its activity to the hyperarousal of insomnia disorder.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the low-grade systemic inflammation that both results from and reinforces chronic sleep loss in insomnia disorder.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Sleep-loss-associated cellular stress can engage cGAS-STING, contributing to the neuroinflammatory consequences of chronic insomnia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress handling relevant to the hyperarousal and stress physiology of insomnia disorder.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 neuroinflammatory signaling contributes to the inflammatory tone associated with chronic insomnia disorder.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the inflammatory tone linked to the sleep-wake dysregulation of insomnia disorder.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and oxidative-stress adaptation participates in the hyperarousal neurobiology of insomnia disorder.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the low-grade peripheral inflammation associated with chronic insomnia disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the neuronal plasticity and circadian-related pathways relevant to insomnia disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the sleep-wake energy homeostasis dysregulated in insomnia disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy, which follows a circadian rhythm and is modulated by sleep, participates in the neuronal homeostasis disrupted in insomnia disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of circadian and stress genes implicated in insomnia disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the synaptic-plasticity and arousal-circuit mechanisms implicated in insomnia disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the low-grade neuroinflammation associated with insomnia disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune processes implicated in insomnia disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory processes implicated in insomnia disorder.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with insomnia disorder.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the microglial and neuroinflammatory processes implicated in insomnia disorder.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Sleep and metabolism: sleep restriction lowers leptin and raises appetite (ghrelin already mapped), linking chronic insomnia to weight gain and metabolic dysregulation in a bidirectional sleep-metabolism relationship.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Sleep homeostasis: nitric oxide in the basal forebrain and brainstem participates in the buildup of sleep pressure and the sleep-wake switch, one of the gaseous modulators of sleep regulation.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sleep-dependent secretion: testosterone release peaks during sleep, so the fragmented sleep of insomnia lowers testosterone, and low testosterone in turn worsens sleep quality, a reciprocal endocrine link.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic consequence: short and disrupted sleep in insomnia promotes insulin resistance and impaired glucose tolerance, part of the metabolic burden that links chronic insomnia to the raised risk of type 2 diabetes (already mapped).
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Neuroimmune balance: sleep loss shifts the cytokine balance, raising the pro-inflammatory IL-6 and TNF (already mapped) that IL-10 normally restrains, contributing to the low-grade inflammation associated with chronic insomnia.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: sleep deprivation increases oxidative stress, to which xanthine-oxidase-derived reactive oxygen species contribute, one mechanism proposed to link chronic insomnia to accelerated cellular ageing and cardiometabolic risk.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cardiometabolic risk: chronic insomnia and the insulin resistance (insulin already mapped) of sleep loss shift cholesterol handling toward an atherogenic profile, part of the cardiovascular and metabolic burden associated with poor sleep.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Stress-axis mineralocorticoid arm: aldosterone acting on brain mineralocorticoid receptors, balanced against the glucocorticoid signalling (cortisol and CRH already mapped), tunes the HPA-axis hyperarousal that maintains chronic insomnia.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Sleep-metabolism link: sleep loss disturbs the appetite and incretin signalling (ghrelin and leptin already mapped), and the GLP-1 axis links the metabolic dysregulation of chronic insomnia to its appetite and weight effects.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Sleep-immune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the sleep-regulatory pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped), part of the bidirectional link between sleep and inflammation in insomnia.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), forms the type-2 response whose balance against the pro-inflammatory sleep-regulatory cytokines shapes the neuroimmune dimension of chronic insomnia.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and sleep: zinc modulates the glutamatergic (already mapped) and GABAergic (already mapped) systems and, with magnesium (already mapped), influences sleep quality, its status linked to the sleep disturbance of insomnia.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and monoamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), and disturbed copper handling affects the monoaminergic arousal system of the sleep-wake balance in insomnia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic consequence: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic (insulin already mapped) consequences of the chronic sleep loss of insomnia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin rises with sleep deprivation, part of the metabolic-inflammatory (IL-6 already mapped) consequences of the chronic sleep loss of insomnia.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Adenosine sleep pressure: the astrocytes release and regulate the adenosine (already mapped), the sleep-pressure signal accumulating during the wakefulness that is dysregulated in insomnia.
- `connects-to` → **[Generalized anxiety disorder](../generalized-anxiety-disorder/README.md)** — Anxiety comorbidity: generalized anxiety disorder and insomnia are highly comorbid, sharing the hyperarousal and the HPA (cortisol already mapped) dysregulation.
- `connects-to` → **[Type 2 diabetes](../type-2-diabetes/README.md)** — Metabolic consequence: the chronic sleep loss of insomnia raises the type 2 diabetes and metabolic-syndrome risk (the insulin, leptin and adiponectin already mapped dysregulation).
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate sleep-immune: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, disrupts the sleep and drives the fatigue, linking the innate immunity to the neuroinflammation of insomnia.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 arm: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation (IL-1 and TNF already mapped, the sleep cytokines) associated with insomnia.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of the chronic sleep loss of insomnia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the chronic sleep loss of insomnia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of insomnia.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of insomnia.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the histamine (already mapped) and neuroinflammatory dimension implicated in the hyperarousal of insomnia.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic hyperarousal of insomnia.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Sleep-modulated NK: the NK-cell number and cytotoxicity, reduced by the sleep loss and altered by the cortisol (already mapped) rhythm, are part of the immune consequences of insomnia.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the low-grade complement activation of the systemic inflammation associated with chronic insomnia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) neuroinflammation implicated in the hyperarousal of insomnia.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the low-grade inflammation of chronic insomnia.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-hyperarousal axis: TSLP, from skin (already mapped) and gut (already mapped) epithelial barriers under the chronic stress of insomnia, primes mast cells (already mapped) and dendritic cells (already mapped) and amplifies the neuroinflammatory hyperarousal of insomnia.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-sleep axis: bradykinin, via B2R on CNS neurons (already mapped) and microglia (already mapped), modulates the neuroinflammation and the autonomic arousal contributing to the sleep-onset and sleep-maintenance difficulties of insomnia disorder.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3 and C5 already mapped) contributing to the neuroinflammation and the complement-mediated synaptic pruning of the hyperarousal circuitry of insomnia.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Sleep-EPO axis: EPO and its receptor on neurons (already mapped) and microglia (already mapped) have neuroprotective effects; the anaemia comorbid with insomnia elevates EPO, adding a neuroendocrine dimension to the hyperarousal of insomnia.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — CNS-border matrix: periostin, from astrocytes (already mapped) and meningeal fibroblasts, remodels the neuroimmune-interface ECM and contributes to the low-grade neuroinflammation (IL-6, TNF already mapped) implicated in chronic insomnia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement gate: factor H limits alternative-pathway activation at the blood-brain barrier, restraining complement-mediated synaptic pruning and the microglial (already mapped) activation (C3 and C5 already mapped) of the hyperarousal of insomnia.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Sleep neuroendocrine: prolactin, sleep-entrained with melatonin (already mapped), promotes NREM slow-wave sleep via GABA (already mapped) and adenosine (already mapped) pathways; prolactin deficiency amplifies the cortisol (already mapped) HPA hyperarousal of insomnia.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Hypothalamic anti-arousal: oxytocin, via OXTR on neurons (already mapped) and astrocytes (already mapped), reduces hypothalamic arousal and promotes sleep onset; oxytocin attenuates the cortisol (already mapped) and norepinephrine (already mapped) hyperarousal of chronic insomnia.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Neuroprotective antioxidant: selenium, as neuroprotective GPx in neurons (already mapped) and astrocytes (already mapped), scavenges neuroinflammatory (IL-6 and TNF already mapped) ROS; selenium deficiency impairs the GABA (already mapped) inhibitory tone and worsens insomnia hyperarousal.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Insomnia iodine: iodine-dependent thyroid hormones regulate neuronal (neuron already mapped) excitability and GABA (already mapped) inhibitory tone; hypothyroidism, common in insomnia, amplifies NF-κB (already mapped) and cortisol (already mapped) HPA hyperarousal.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Insomnia sodium: sodium, via voltage-gated channels on neurons (already mapped) and astrocytes (already mapped), determines action-potential firing in sleep-wake circuits; disrupted sodium from microglial (already mapped) NF-κB (already mapped) neuroinflammation worsens insomnia.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Insomnia potassium: potassium efflux activates NLRP3 inflammasome (already mapped) in microglia (already mapped); disrupted K⁺ at synapses (already mapped) and neurons (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and insomnia.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Insomnia phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and microglia (already mapped), supports synaptic energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of insomnia disorder.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Insomnia chloride: chloride, via GABA-A Cl⁻ influx in neurons (already mapped), maintains inhibitory tone; chloride dysregulation in microglia (already mapped) amplifies the NF-κB (already mapped) and IL-6 (already mapped) arousal cascade of insomnia disorder.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Insomnia sulfur: sulfur, as cysteine precursor in neurons (already mapped) and microglia (already mapped), supports GABA (already mapped) modulation; sulfur deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of insomnia.

[^riemann-2017-insomnia-lancet]: Riemann D, Baglioni C, Bassetti C, et al. European guideline for the diagnosis and treatment of insomnia. *J Sleep Res.* 2017;26(6):675-700. [doi:10.1111/jsr.12594](https://doi.org/10.1111/jsr.12594) · [PubMed 28875581](https://pubmed.ncbi.nlm.nih.gov/28875581/)
[^trauer-2015-cbti-meta]: Trauer JM, Qian MY, Doyle JS, et al. Cognitive behavioral therapy for chronic insomnia. *Ann Intern Med.* 2015;163(3):191-204. [doi:10.7326/M14-2841](https://doi.org/10.7326/M14-2841) · [PubMed 26054060](https://pubmed.ncbi.nlm.nih.gov/26054060/)
[^herring-2012-suvorexant]: Herring WJ, Snyder E, Budd K, et al. Orexin receptor antagonism for treatment of insomnia. *Sci Transl Med.* 2012;4(129):129ra45. [doi:10.1126/scitranslmed.3003795](https://doi.org/10.1126/scitranslmed.3003795) · [PubMed 22491949](https://pubmed.ncbi.nlm.nih.gov/22491949/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
