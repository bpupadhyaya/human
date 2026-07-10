---
schema: human-scale-entry/v1
id: ptsd
name: PTSD
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "PTSD (7-10% lifetime risk after trauma) involves amygdala hyperreactivity, hippocampal atrophy, noradrenergic hyperarousal, and hypocortisolemia; first-line: trauma-focused CBT and SSRIs (sertraline, paroxetine); prazosin (α1 antagonist) reduces nightmares."
aliases: ["PTSD", "post-traumatic stress disorder", "trauma", "combat PTSD", "complex PTSD", "fear extinction", "prazosin PTSD", "EMDR", "prolonged exposure", "TRD PTSD"]
sources:
  - id: yehuda-2015-ptsd-review
    type: peer-reviewed
    cite: "Yehuda R, Hoge CW, McFarlane AC, et al. Post-traumatic stress disorder. Nat Rev Dis Primers. 2015;1:15057."
    doi: "10.1038/nrdp.2015.57"
    pmid: "27189040"
    url: "https://doi.org/10.1038/nrdp.2015.57"
    accessed: "2026-06-08"
  - id: foa-2019-ptsd-treatments
    type: peer-reviewed
    cite: "Foa EB, McLean CP. The efficacy of exposure therapy for anxiety and related disorders and its underlying mechanisms: the emotional processing theory. Annu Rev Clin Psychol. 2016;12:1-28."
    doi: "10.1146/annurev-clinpsy-021815-093533"
    pmid: "26928206"
    url: "https://doi.org/10.1146/annurev-clinpsy-021815-093533"
    accessed: "2026-06-08"
  - id: mitchell-2021-mdma-ptsd
    type: peer-reviewed
    cite: "Mitchell JM, Bogenschutz M, Lilienstein A, et al. MDMA-assisted therapy for severe PTSD: a randomized, double-blind, placebo-controlled phase 3 trial. Nat Med. 2021;27(6):1025-1033."
    doi: "10.1038/s41591-021-01336-3"
    url: "https://doi.org/10.1038/s41591-021-01336-3"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Locus coeruleus hyperactivation in PTSD → excess NE → amygdala hyperreactivity, hyperarousal, and intrusive re-experiencing; prazosin (α1 antagonist) reduces NE-driven nightmares; propranolol may reduce fear memory reconsolidation when given within hours of trauma."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "PTSD exhibits paradoxical hypocortisolemia — elevated CRH but enhanced GR sensitivity → excess negative feedback; low cortisol impairs fear extinction; hydrocortisone given within hours of trauma shows prophylactic benefit in some randomized trials."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Reduced hippocampal BDNF in PTSD mirrors findings in MDD; chronic stress → glucocorticoid-mediated BDNF suppression → hippocampal volume loss (~8% in chronic PTSD); SSRIs normalize BDNF and partially restore hippocampal volume with sustained treatment."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "NMDA receptor-mediated processes underlie fear memory consolidation and extinction in amygdala and vmPFC; D-cycloserine (partial NMDA agonist) enhances extinction in CBT; ketamine reduces PTSD symptoms via rapid BDNF/mTOR signaling and disrupted fear memory reconsolidation."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "PTSD features amygdala hyperreactivity and reduced vmPFC control over fear responses; hippocampal volume is reduced ~8%; anterior cingulate shows reduced activation; normalization of amygdala-vmPFC connectivity predicts treatment response on fMRI."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Oxytocin facilitates fear extinction in the amygdala via OTR on CeA neurons; chronic stress reduces OT signaling; intranasal oxytocin is under investigation as an adjunct to exposure therapy to enhance extinction memory consolidation in PTSD."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SSRIs (sertraline, paroxetine) are FDA-approved for PTSD; serotonin modulates fear extinction in vmPFC; serotonin dysregulation contributes to PTSD hyperarousal, emotional numbing, and sleep disturbance; SNRIs (venlafaxine) also used for PTSD with good evidence."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "PTSD shows CSF CRH excess, elevated ACTH, and paradoxically low cortisol (enhanced glucocorticoid feedback); CRH hyperdrive in amygdala/BNST drives hyperarousal and re-experiencing; CRHR1 antagonists are a proposed pharmacotherapy pending adequate clinical trials."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "PTSD shows dissociated HPA: normal or elevated ACTH responses to CRH but low basal cortisol — due to GR hypersensitivity (enhanced negative feedback); contrasts with MDD (high ACTH + high cortisol + GR resistance); enhanced DST suppression (<0.5 µg/dL) is the PTSD biomarker."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Amygdala and CSF NPY are reduced in PTSD; Y1R-mediated anxiolysis is impaired; plasma NPY correlates with stress resilience in veterans; glucocorticoid excess in chronic stress depletes amygdala NPY; NPY Y1R agonists are under investigation as PTSD pharmacotherapy."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "CSF vasopressin is elevated in PTSD; AVP-CRH synergy at corticotroph V1bR potentiates ACTH when CRH receptors desensitise; elevated AVP sustains HPA hyperactivation; V1bR antagonists show anxiolytic effects and are a proposed PTSD pharmacotherapy."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "PTSD and major depression are highly comorbid and share neurobiology: HPA-axis and monoaminergic dysregulation, hippocampal changes, and overlapping symptoms link them, about half of PTSD patients also meet criteria for depression, and SSRIs treat both."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus is central to PTSD: reduced hippocampal volume impairs contextualizing fear memories, so trauma cues are not recognized as past, and the hippocampus fails to restrain an overactive amygdala—a core circuit abnormality targeted by trauma-focused therapy."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "PTSD and alcohol use disorder form a vicious cycle: many drink to blunt hyperarousal and intrusive memories, but alcohol fragments sleep and worsens PTSD, and the two strongly co-occur—so integrated treatment of both outperforms addressing either alone."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "PTSD and panic disorder share a hyperactive fear response but differ in trigger: both feature surges of autonomic arousal, but panic attacks come 'out of the blue' while PTSD's are cued by trauma reminders—and panic commonly complicates PTSD."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "PTSD and bipolar disorder frequently co-occur and worsen each other: trauma raises bipolar risk, comorbid PTSD predicts more mood episodes and suicidality, and overlapping irritability and arousal can blur diagnosis—so screening for trauma is part of bipolar assessment."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "PTSD and fibromyalgia are tightly linked through chronic stress: trauma and HPA-axis dysregulation promote central sensitization, so fibromyalgia is far more common in PTSD—evidence that psychological trauma can manifest as bodily pain."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "PTSD reflects a tipped excitatory-inhibitory balance: deficient GABAergic inhibition leaves fear circuits hyperexcitable, underlying hyperarousal and intrusive memories, which is why benzodiazepines that boost GABA paradoxically tend to worsen long-term PTSD."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep disturbance is a core feature of PTSD, not just a symptom: nightmares and insomnia are diagnostic criteria and can precede and perpetuate the disorder, and treating the insomnia (e.g., with prazosin or CBT-I) improves overall PTSD outcomes."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "PTSD and cannabis use disorder feed each other: many with PTSD use cannabis to dampen hyperarousal and insomnia, but tolerance and withdrawal worsen the symptoms it masks, so this common self-treatment readily slides into dependence."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The endocannabinoid system governs fear extinction central to PTSD: cannabinoid signaling helps the brain unlearn trauma cues, and deficits may lock in fear—so this pathway underlies why cannabis is sought for PTSD nightmares and why it is a drug-development target."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Adrenaline burns trauma into memory: the epinephrine surge during a terrifying event strengthens memory consolidation, helping explain PTSD's intrusive recollections—and why beta-blockers like propranolol have been tested to blunt or weaken fear memories."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "PTSD and borderline personality disorder share a traumatic root: childhood trauma drives both, and complex PTSD overlaps BPD's emotional dysregulation and unstable relationships—so the two frequently co-occur and can be hard to disentangle clinically."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "PTSD dysregulates the adrenal stress axis: chronic trauma alters HPA-axis output so the adrenal gland's cortisol response is blunted and abnormal, leaving the noradrenergic alarm system unrestrained—part of the biology behind hypervigilance and flashbacks."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Trauma leaves an inflammatory mark via microglia: PTSD is linked to activated brain microglia and neuroinflammation that may damage the hippocampus and prefrontal cortex, connecting psychological trauma to measurable brain changes."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine ties PTSD to reward and to its therapies: trauma blunts reward-related dopamine signaling (contributing to numbing and anhedonia), and dopamine is part of why MDMA-assisted therapy is being studied to help process traumatic memories."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "PTSD strikes women about twice as often, and estrogen is part of why: the hormone shapes fear extinction, so low-estrogen phases impair the unlearning of fear—helping explain sex differences in risk and the timing of intrusive symptoms."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "PTSD wrecks sleep, and melatonin is enlisted to mend it: nightmares and insomnia are core symptoms tied to disrupted circadian and REM regulation, so melatonin and sleep-targeted therapy are used alongside trauma treatment."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "PTSD's fear circuits depend on astrocytes: these glial cells regulate glutamate in the amygdala and hippocampus that encode and extinguish fear, so astrocyte dysfunction can lock in the traumatic memory that drives the disorder."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "PTSD is hard on the heart: chronic hyperarousal keeps stress hormones and blood pressure high and stokes inflammation, and survivors carry a markedly raised risk of heart attack and cardiovascular disease, making PTSD a cardiac risk factor."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Traumatic memories are cemented by calcium: fear learning in the amygdala relies on calcium flooding through NMDA receptors to strengthen synapses, the molecular step that locks a terrifying event into a lasting, intrusive memory."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "PTSD lives in overstrengthened synapses: trauma potentiates the amygdala's fear synapses while weakening the prefrontal control over them, and therapy works by reconsolidating or extinguishing these synaptic memories."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Brain imaging maps PTSD: fMRI photons reveal an overactive amygdala and underactive prefrontal cortex, alongside a smaller hippocampus, the neural signature of trauma's lasting grip."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "PTSD is written in neurons: amygdala fear neurons overfire while the hippocampal and prefrontal neurons that should place the fear in context and dampen it are impaired, so danger feels ever-present."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "PTSD's stress axis is paradoxically hypersensitive: more sensitive glucocorticoid receptors enhance cortisol's negative feedback, so cortisol runs low even as the system overreacts to reminders of trauma."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Trauma may reshape the brain's wiring insulation: chronic stress alters oligodendrocytes and myelination in the fear-circuit tracts, and the resulting white-matter changes are seen on imaging in PTSD."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "PTSD speaks to the gut: it is tightly comorbid with irritable bowel syndrome, the trauma-primed stress axis and altered gut-brain signaling disturbing motility and sensation in the bowel."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Chronic stress burns through magnesium: the sustained HPA activation of PTSD depletes the mineral, and because magnesium restrains both the stress axis and the NMDA receptors of fear, its loss can deepen the hyperarousal."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "PTSD smolders with inflammation: chronic stress raises CRP and inflammatory cytokines and dysregulates immune cells, helping explain the higher rates of autoimmune and cardiovascular disease and a kind of accelerated aging in sufferers."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Trauma settles in the gut: through the brain-gut axis PTSD drives functional dyspepsia, nausea, and irritable bowel, and the stomach's churning becomes a somatic echo of the hypervigilant nervous system."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Chronic stress turns down the sex hormones: sustained cortisol from PTSD suppresses the HPG axis, lowering testosterone and contributing to the reduced libido, fatigue, and low mood that often accompany the disorder."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Trauma leaves an inflammatory, autoimmune mark: PTSD raises circulating inflammatory markers and autoantibodies and is linked to a higher risk of autoimmune diseases, a body-wide signature of chronically dysregulated stress and immunity."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "PTSD is hard on the heart and vessels: years of sympathetic and cortisol overdrive raise blood pressure and accelerate atherosclerosis, giving these patients a substantially higher rate of heart attack and cardiovascular death."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "PTSD and reproduction intertwine: sexual trauma is a major cause, the disorder disrupts sexual function and intimacy, and it strikes women about twice as often, with symptoms shifting across the menstrual cycle and the perinatal period."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Trauma leaves an inflammatory signature: PTSD runs with elevated IL-6 and other inflammatory markers, a low-grade immune activation thought to link the disorder to its heart and metabolic complications and even to influence fear circuitry."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The traumatized brain talks to the gut and back: PTSD is marked by an altered microbiome, and through the microbiome-gut-brain axis these shifts may shape stress reactivity, inflammation, and the disorder's resilience or severity."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "PTSD and chronic pain feed each other: they co-occur strikingly often, sharing central sensitization and stress circuitry, so trauma amplifies neuropathic pain while persistent pain keeps the traumatic memory alive."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Chronic alarm raises the pressure: the sustained sympathetic and HPA-axis overdrive of PTSD keeps blood pressure elevated, a major route by which trauma translates into long-term cardiovascular disease."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Stress hormones disturb metabolism: chronically high cortisol with poor sleep and lifestyle disruption raises the risk of insulin resistance and type 2 diabetes among people with PTSD."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "It overlaps the broader anxiety spectrum: PTSD shares fear-circuit dysregulation and frequently co-occurs with generalized anxiety disorder, the two amplifying each other's worry and hypervigilance."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic stress smolders as inflammation: PTSD shows elevated NF-κB activity in immune cells, a stress-driven inflammatory signal that helps explain its raised risk of cardiovascular and metabolic disease."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is a disorder of the brain's fear circuitry: PTSD reflects dysregulation across the amygdala, hippocampus and prefrontal cortex of the nervous system, the network that normally extinguishes fear after a threat passes."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Trauma drives self-medication with opioids: PTSD is strongly comorbid with opioid use disorder, as sufferers turn to opioids to blunt hyperarousal and intrusive memories, deepening the addiction."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Chronic stress reshapes the body: sustained cortisol, disrupted sleep and emotional eating in PTSD promote weight gain and central adiposity, contributing to a high rate of obesity and metabolic syndrome."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Relentless stress wears on the vessels: PTSD's chronic sympathetic and HPA-axis activation raises blood pressure and inflammation, and epidemiologic studies link it to a higher long-term risk of ischemic stroke."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The stressed heart can fail over time: chronic catecholamine surges, hypertension and inflammation in PTSD accelerate cardiovascular disease, and the disorder is associated with an increased incidence of heart failure."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Chronic stress inflames the arteries: the sustained sympathetic arousal, cortisol dysregulation and systemic inflammation of PTSD accelerate atherosclerosis, underlying its raised cardiovascular risk."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Trauma can prime autoimmunity: PTSD is associated with a higher incidence of autoimmune diseases such as rheumatoid arthritis, thought to reflect chronic stress-driven immune dysregulation."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Lasting stress wears on the aging brain: PTSD is linked to a higher risk of dementia, with chronic cortisol exposure and hippocampal injury contributing to later Alzheimer-type cognitive decline."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Trauma is felt in the gut: PTSD strongly co-occurs with irritable bowel syndrome and functional GI disorders, with the dysregulated gut-brain axis and autonomic arousal driving abdominal pain and altered bowel habit."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Trauma can tip into psychosis: severe and childhood trauma is a recognised risk factor for schizophrenia, and PTSD with psychotic features overlaps with it, the two frequently co-occurring."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Two anxiety-spectrum disorders intertwine: PTSD and OCD frequently coexist, with trauma sometimes precipitating obsessive-compulsive symptoms and the intrusive thoughts of each reinforcing the other."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It carries a distinctive hormone signature: PTSD is marked by low basal cortisol with enhanced glucocorticoid negative feedback — dexamethasone hypersuppression — unlike most chronic-stress states."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Fear seizes the breath: flashbacks and panic in PTSD trigger hyperventilation and breathlessness, and the disorder is associated with higher rates of asthma and respiratory symptoms."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Constant hyperarousal tenses the body: the sustained muscle tension of PTSD's hypervigilance contributes to chronic neck, back and widespread musculoskeletal pain."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Trauma surfaces on the skin: chronic stress flares psoriasis and eczema, triggers stress-related alopecia and urticaria, and trauma-related behaviours can mark the skin."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It raises kidney-disease risk: PTSD-associated hypertension, metabolic syndrome and chronic stress are linked to a higher risk of chronic kidney disease, well documented in veterans."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "SSRIs are first-line medication: serotonergic antidepressants such as the SSRIs are the first-line pharmacotherapy for PTSD, used alongside trauma-focused psychotherapy."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "They blunt the adrenergic surge: beta-blockers like propranolol, and the related alpha-blocker prazosin, reduce the hyperarousal and nightmares of PTSD by dampening noradrenergic overactivity."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet is studied for resilience: omega-3 supplementation has been trialled to prevent or ease PTSD after trauma, though the evidence remains modest and uncertain."
  - target: 03-medicine/02-traditional/ashwagandha
    relation: connects-to
    note: "Traditional calm is sought: adaptogens such as ashwagandha are used for the chronic stress and poor sleep of PTSD, complementing trauma-focused therapy and SSRIs."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Overlapping fear and avoidance: PTSD and social anxiety disorder share hyperarousal, avoidance and exaggerated threat appraisal, frequently co-occur, and trauma can precipitate or worsen social anxiety."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Self-medication and comorbidity: stimulant and other substance use is common in PTSD as patients try to numb or override hyperarousal, and the disorders worsen each other's course and treatment."
  - target: 03-medicine/02-traditional/st-johns-wort
    relation: connects-to
    note: "A herbal serotonergic adjunct: St John's wort, raising serotonin like the SSRIs that are first-line for PTSD, is used by some for the comorbid depression, though evidence is limited and drug interactions are a concern."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Disordered REM connects them: PTSD fragments REM sleep with nightmares and hyperarousal, overlapping the disrupted REM regulation and daytime sleepiness of narcolepsy, and the two are comorbid."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Stress and headache feed each other: PTSD and migraine are strongly comorbid, sharing stress-axis and serotonergic dysregulation and central sensitisation, so each worsens the other's course."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "The heart pays for chronic stress: sustained catecholamine and cortisol surges in PTSD raise cardiovascular risk, and acute severe stress can stun the myocardium as Takotsubo (stress) cardiomyopathy."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Trauma and autoimmunity: PTSD is associated with a higher later incidence of autoimmune diseases such as lupus, the chronic stress and inflammation dysregulating immune tolerance."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A pandemic mental-health toll: COVID-19 survivors—especially after ICU care—and frontline workers show high rates of PTSD, the life-threatening illness and isolation acting as traumatic stressors."
  - target: 01-human/07-system/bulimia-nervosa
    relation: connects-to
    note: "Trauma and disordered eating: childhood trauma and PTSD strongly predispose to bulimia and binge-eating, the bingeing and purging serving as affect regulation for trauma-driven distress."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Autonomic toll: PTSD's chronic sympathetic overdrive reduces heart-rate variability and raises arrhythmia and sudden-cardiac-death risk, the conduction-system consequence of a perpetually activated stress response."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Trauma and seizures: psychogenic nonepileptic seizures are strongly tied to trauma and PTSD and are the key differential of epilepsy, while PTSD and epilepsy are also bidirectionally associated."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The gut-brain axis in trauma: PTSD alters the microbiome and intestinal barrier, the epithelium mediating stress-related GI symptoms and low-grade inflammation that feed back to the traumatised brain."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neuroinflammation: elevated IL-1β from activated microglia is linked to the fear-circuit dysfunction and memory consolidation abnormalities of PTSD."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory signature: raised TNF-α is among the peripheral inflammatory markers consistently found in PTSD, tying chronic stress to systemic low-grade inflammation."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Stress inflammasome: chronic stress activates the NLRP3 inflammasome, and its IL-1β output is increasingly implicated in the neuroinflammatory component of PTSD."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "Treatment and gene-environment risk: SSRIs blocking the serotonin transporter are first-line for PTSD, and the 5-HTTLPR transporter polymorphism is among the most studied gene-by-trauma interactions in the disorder."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: connects-to
    note: "Fear-memory reconsolidation: noradrenaline acting on β-adrenergic receptors strengthens traumatic memory consolidation, the rationale for propranolol to blunt reconsolidation and the hyperarousal of PTSD."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Neuroinflammatory recruitment: elevated CCL2 in PTSD recruits monocytes that traffic to the brain, contributing to the microglial activation and inflammation linked to its stress-related neuropathology."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Peritraumatic protection: opioid analgesia given soon after trauma lowers later PTSD risk, and endogenous opioid signalling shapes fear extinction — implicating the μ-opioid system in the consolidation of traumatic memory."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid deficit: reduced allopregnanolone, a progesterone metabolite and positive GABA-A modulator, is found in PTSD, weakening the inhibitory tone that normally restrains the fear and arousal circuits."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Stress tachykinin: substance P is elevated in PTSD and acts on NK1 receptors in the amygdala to heighten anxiety and the stress response, a neuropeptide arm of the disorder's hyperarousal."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Hyperarousal and nightmares: elevated orexin signalling drives the chronic hyperarousal, fragmented sleep and nightmares of PTSD, the wake-promoting system whose overactivity underlies the disorder's prominent sleep disturbance."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Fear-memory consolidation: ghrelin enhances fear learning and the persistence of traumatic memories, a stress-responsive hormone that potentiates amygdala fear circuits and is implicated in the over-consolidated fear memory at the core of PTSD."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Autonomic startle: cholinergic signalling contributes to the exaggerated startle response and autonomic hyperreactivity of PTSD, the parasympathetic-sympathetic imbalance that accompanies the noradrenergic hyperarousal."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Fear-memory consolidation: ERK-MAPK signalling in the amygdala consolidates and reconsolidates fear memories, the molecular substrate of the intrusive traumatic-memory persistence and reactivity central to PTSD."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Reconsolidation and extinction: synaptic mTOR-dependent protein synthesis underlies the reconsolidation and extinction of fear memory, a plasticity mechanism of interest for memory-targeted PTSD treatments."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Stress neuroinflammation: innate-immune TLR4 signalling links chronic traumatic stress to the neuroinflammation (IL-1β, IL-6 and TNF-α already mapped) increasingly implicated in the pathophysiology of PTSD."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Fear-memory consolidation: PI3K-AKT signalling (with mTOR and ERK1/2 mapped) relays the BDNF-driven (mapped) synaptic plasticity that consolidates the traumatic fear memories of PTSD."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Extinction and reconsolidation: GSK-3β regulates fear-memory reconsolidation and extinction, the processes disrupted in PTSD and modulated by mood-stabiliser therapy."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microglial relay: TLR4 (mapped) signals through MyD88 to drive the microglial neuroinflammation (IL-1β, IL-6 and TNF mapped) increasingly linked to PTSD risk and severity."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-driven JAK-STAT signalling (IL-6 mapped) transduces the peripheral and central inflammatory milieu associated with PTSD symptom severity."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement-mediated synaptic pruning (C3 tagging) in fear-circuit regions is implicated in the aberrant remodelling that underlies PTSD memory pathology."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 is induced during stress-driven neuroinflammation, amplifying the reactive microglial state linked to PTSD."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "BDNF-TrkB (NTRK) signalling (BDNF already mapped) drives the hippocampal and amygdalar plasticity underlying fear conditioning and extinction in PTSD."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the chronic inflammatory tone associated with the stress-driven neuroinflammation of PTSD."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic mitochondrial DNA released during chronic stress can engage cGAS-STING, contributing to the neuroinflammation implicated in PTSD."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 neuroinflammatory signaling contributes to the chronic low-grade inflammation reported in PTSD."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to the stress physiology of PTSD."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of stress and PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress and resilience relevant to the fear-circuit plasticity of PTSD."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and mitochondrial stress responses contribute to the neurobiology of post-traumatic stress disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the neuronal plasticity of the fear-memory circuits altered in post-traumatic stress disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK metabolic signaling participates in the neuronal energetic and stress-adaptation responses relevant to post-traumatic stress disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic (traumatic-memory and FKBP5-linked) programming implicated in post-traumatic stress disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal stress responses and fear-memory circuits implicated in post-traumatic stress disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the synaptic plasticity of the fear-memory consolidation of post-traumatic stress disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with post-traumatic stress disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and hippocampal-plasticity processes implicated in post-traumatic stress disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in post-traumatic stress disorder."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with post-traumatic stress disorder."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic (trauma-related) programming implicated in post-traumatic stress disorder."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the fear-memory-related synaptic plasticity and neuroimmune activation of post-traumatic stress disorder."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Brain renin-angiotensin: central angiotensin II modulates fear consolidation and the stress response, and angiotensin-receptor blockers such as losartan are associated with reduced PTSD symptoms, a neuroendocrine target beyond the monoamine and HPA systems already mapped."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Fear-memory plasticity: nitric oxide from neuronal nNOS is required for the synaptic plasticity of fear conditioning in the amygdala, implicating NO signalling in the formation of the intrusive traumatic memories of PTSD."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Arousal regulation: central histaminergic neurotransmission drives wakefulness and arousal, systems pathologically heightened in the hypervigilance, exaggerated startle and sleep disturbance of post-traumatic stress disorder."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response and fear memory dysregulated in post-traumatic stress disorder."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic dysregulation: chronic stress in PTSD promotes insulin resistance and the metabolic syndrome (cortisol already mapped), part of the cardiometabolic burden that raises long-term physical illness in affected patients."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiovascular risk: the sustained sympathetic activation (norepinephrine already mapped) of PTSD raises the risk of coronary disease and myocardial infarction, and troponin elevation marks the cardiac injury of these excess cardiovascular events."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Cardiometabolic dyslipidaemia: the chronic stress and insulin resistance (insulin already mapped) of PTSD shift cholesterol handling toward an atherogenic profile, part of the cardiometabolic burden that raises its long-term cardiovascular risk."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6, TNF and IL-1 already mapped) reported in PTSD modulate the fear and stress circuits, part of the immune-inflammatory dimension of the disorder."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory balance: the anti-inflammatory IL-10 counters the chronic low-grade inflammation (IL-6, TNF and IL-1 already mapped) of PTSD, and the imbalance toward pro-inflammatory signalling is part of its cardiometabolic and neuropsychiatric burden."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation reported in PTSD."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and noradrenaline: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the noradrenergic hyperarousal central to PTSD."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and fear memory: zinc modulates the glutamatergic (already mapped) NMDA signalling of the fear-memory circuits, and low zinc status is associated with the mood and anxiety symptoms that accompany PTSD."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation (TNF, IL-6 and IL-1 already mapped) implicated in PTSD."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "Trauma-spectrum overlap: borderline personality disorder is strongly linked to childhood trauma and overlaps with complex PTSD, the two sharing the HPA-axis (cortisol and CRH already mapped) dysregulation and affective instability."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety comorbidity: generalized anxiety disorder commonly co-occurs with PTSD, part of the anxious-hyperarousal (noradrenaline already mapped) symptom burden that accompanies the trauma disorder."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic-inflammatory adipokine: leptin is the adipokine of the metabolic-inflammatory milieu; PTSD is associated with the metabolic dysregulation (insulin already mapped) and the adipokine changes."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory milieu of PTSD."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the metabolic-inflammatory (IL-6 and TNF already mapped) dimension of PTSD."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-1 and TNF already mapped) implicated in PTSD."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation associated with the chronic stress of PTSD."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of PTSD."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with the chronic stress of PTSD."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension associated with PTSD."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the stress-related immune dysregulation of PTSD."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the stress-reactive (histamine already mapped) dimension of PTSD."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic stress of PTSD."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Stress-modulated NK: the NK-cell number and cytotoxicity, altered by the chronic stress and cortisol (already mapped) reactivity, are part of the peripheral immune dysregulation of PTSD."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the low-grade complement activation of the chronic-stress neuroinflammation implicated in PTSD."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) neuroinflammation implicated in PTSD."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the chronic-stress neuroinflammation of PTSD."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuro-immune alarmin: TSLP, released by skin (already mapped) and gut-epithelial (already mapped) barriers under chronic stress, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the systemic low-grade immune activation of PTSD."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin stress-response axis: bradykinin, generated by the kallikrein-kinin system activated by trauma-related inflammation, augments blood-brain-barrier permeability and amplifies the microglial (already mapped) neuroinflammation of PTSD."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) activation in the stress-sensitised CNS environment, moderating neuroinflammation of PTSD."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM remodelling in the fear-memory circuit: periostin, expressed by astrocytes (already mapped) and microglia (already mapped) in the amygdala and hippocampus, modulates the extracellular matrix perineuronal nets that consolidate the maladaptive fear memories of PTSD."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuro-protective cytokine: erythropoietin, via EPOR on hippocampal neurons and astrocytes (already mapped), promotes neurogenesis and limits the HPA-axis-driven (cortisol already mapped) hippocampal volume loss and the neuroinflammatory burden of PTSD."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Stress-endocrine coupling: prolactin, elevated after acute trauma and stress (HPA-axis already mapped), modulates the T-cell (already mapped) and NK-cell (already mapped) immune function and contributes to the female-predominant vulnerability to PTSD."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "PTSD factor-h: factor H limits alternative complement (C5 already mapped) in the neuroinflamed brain (already mapped); impaired factor H amplifies microglial (already mapped) and astrocyte (already mapped) complement-driven hippocampal (already mapped) damage of PTSD."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "PTSD transferrin: transferrin supports brain (already mapped) iron homeostasis and dopamine (already mapped) synthesis; iron dyshomeostasis amplifies hippocampal (already mapped) neurodegeneration and cortisol (already mapped) HPA-axis disruption of PTSD."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "PTSD iron: iron supports brain (already mapped) myelination and dopamine (already mapped) synthesis; iron deficiency amplifies hippocampal (already mapped) neurodegeneration and cortisol (already mapped) HPA-axis dysregulation in PTSD."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "PTSD selenium: selenoprotein P reduces hippocampal (already mapped) neuron (already mapped) oxidative stress and microglial activation; selenium deficiency amplifies the NF-κB (already mapped) neuroinflammation and the cortisol (already mapped) HPA-axis dysregulation of PTSD."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "PTSD iodine: iodine-dependent thyroid hormones regulate hippocampal (already mapped) neurogenesis and cortisol (already mapped) HPA-axis homeostasis; thyroid-hormone deficiency amplifies the NF-κB (already mapped) neuroinflammation and worsens trauma memory consolidation in PTSD."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "PTSD sodium: sodium regulates GABAergic (already mapped) and glutamatergic (already mapped) neurotransmission in hippocampal (already mapped) fear circuits; sodium-driven aldosterone (already mapped) excess amplifies the NF-κB (already mapped) neuroinflammation of PTSD."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "PTSD potassium: potassium, via Kv7/HCN channels in neurons (already mapped) and astrocytes (already mapped), regulates fear-circuit excitability; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of PTSD."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "PTSD phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and microglia (already mapped), supports synaptic plasticity and memory consolidation; phosphorus deficiency amplifies the NF-κB (already mapped) and cortisol (already mapped) HPA-axis cascade of PTSD."
---

# PTSD

## Overview

**Post-traumatic stress disorder (PTSD)** is a trauma- and stressor-related psychiatric condition that develops in a subset of individuals following exposure to actual or threatened death, serious injury, or sexual violence. It affects approximately **7–10% of individuals** who experience qualifying traumatic events over their lifetimes — with higher rates in certain exposed groups (veterans: 15–30%; sexual assault survivors: 30–50%; disaster workers: 10–20%). Globally, an estimated 3.9–5.6% of adults have lifetime PTSD, with women affected at 2× the rate of men.

**DSM-5 PTSD** (requires exposure to trauma + symptoms from all 4 clusters ≥1 month):

**Criterion A (Trauma):** Exposure to death, serious injury, or sexual violence (direct, witnessed, learned about, or repeated first-responder exposure)

**4 Symptom clusters:**

| Cluster | Examples | Neural correlate |
|:---|:---|:---|
| **B — Intrusion** | Flashbacks, nightmares, psychological/physiological distress to cues | Amygdala hyperreactivity; context-independent fear retrieval |
| **C — Avoidance** | Avoiding trauma-related thoughts, feelings, places, people | vmPFC failure to suppress amygdala; anhedonia |
| **D — Negative cognitions/mood** | Persistent negative beliefs, distorted blame, emotional numbing, dissociation | Hippocampal memory encoding failure; PFC hypofunction |
| **E — Hyperarousal** | Hypervigilance, exaggerated startle, irritability, sleep disturbance, reckless behavior | Locus coeruleus-NE hyperactivation; amygdala sensitization |

**Complex PTSD (ICD-11):** Includes three additional domains — emotional dysregulation, negative self-concept, and relationship disturbances — typical of prolonged childhood trauma (complex developmental trauma).

## Structure

### Neurobiology of fear circuits

PTSD represents a pathological state of the **amygdala-hippocampus-prefrontal fear circuit**:

**Basolateral amygdala (BLA):**
- Core site of **fear memory acquisition and storage** — Pavlovian fear conditioning occurs here: CS (conditioned stimulus, e.g., sound) + US (unconditioned stimulus, shock) → CS-US association encoded via CaMKII/CREB-dependent plasticity
- In PTSD: heightened BLA activity, reduced threshold for fear acquisition, overgeneralization of conditioned fear to non-threatening cues (conceptually similar to gun exposure → freeze in a patient with combat PTSD)
- BLA → downstream nuclei: central amygdala (CeA) → fear expression (freezing, HR increase, cortisol); basal amygdala → vHPC → avoidance behavior

**Ventromedial prefrontal cortex (vmPFC, includes infralimbic cortex):**
- Source of **fear extinction** — vmPFC neurons send GABAergic projections to amygdala intercalated cells (ITC) → inhibit CeA → safety signal; extinction learning is vmPFC-dependent
- In PTSD: reduced vmPFC volume and activation → inadequate suppression of BLA → persistence of conditioned fear → failure of extinction → PTSD maintenance
- Target of MDMA-assisted therapy: MDMA restores vmPFC control over amygdala

**Hippocampus:**
- Essential for **contextual fear discrimination** — allows fear response to be appropriately limited to the original danger context (not generalized)
- In PTSD: hippocampal volume reduced ~8% (bilateral; predominantly CA3 and dentate gyrus); impaired contextual encoding → fear triggered in "safe" contexts
- Mechanism: chronic stress → glucocorticoid excess → reduced BDNF → CA3 dendritic retraction; SSRI treatment partially restores hippocampal volume over 6–12 months

**Locus coeruleus (LC):**
- Source of CNS norepinephrine; projects widely to cortex, amygdala, hippocampus, spinal cord
- In PTSD: hyperactivated LC → elevated tonic and phasic NE → chronic hyperarousal, exaggerated startle, sleep disruption
- Target of prazosin (α1 antagonist, reduces nightmares) and clonidine (α2 agonist, reduces LC firing)

## Function

### HPA axis in PTSD: the cortisol paradox

Unlike MDD (which features **hypercortisolemia**), PTSD — particularly chronic PTSD — paradoxically shows **hypocortisolemia** [^yehuda-2015-ptsd-review]:

- **Acute trauma response:** Cortisol surge (normal) → should suppress traumatic memory consolidation and aid resolution
- **Chronic PTSD:** Cortisol levels are often **below normal**, combined with:
  - Enhanced negative feedback sensitivity (lower dexamethasone dose required for cortisol suppression)
  - Upregulated glucocorticoid receptors on lymphocytes
  - Elevated CRH in CSF despite low cortisol

**Mechanistic interpretation:**
- Enhanced GR sensitivity → more powerful negative feedback → greater cortisol suppression
- Low cortisol in PTSD impairs extinction: cortisol normally facilitates extinction memory consolidation; without it, fear memories cannot be adequately resolved
- Yehuda's model: PTSD is not an excess of cortisol but a dysregulation — the normal post-trauma cortisol surge fails to suppress trauma memory → persistent fear encoding

**Implications:** Hydrocortisone given acutely (within hours of trauma) in ICU patients or combat settings reduces PTSD incidence in some RCTs — by rescuing the normal cortisol surge needed for memory resolution.

### Noradrenergic system

The **norepinephrine hyperactivation model of PTSD** explains hyperarousal symptoms:
- LC hyperactivation → elevated NE → increased amygdala reactivity (BLA has dense α1-NE receptors → NE enhances fear memory acquisition and intrusive retrieval)
- Sleep disruption: NE during REM sleep normally decreases → in PTSD, high NE during REM → nightmares
- Startle: NE lowers the sensory threshold for CeA-mediated startle
- Exaggerated cardiovascular response to trauma reminders: sympathetic surge

**Pharmacological targets:**
- **Prazosin (α1 antagonist):** Reduces nightmares and overall PTSD severity in multiple RCTs; blocks NE signaling in amygdala and brainstem circuits during sleep
- **Propranolol (β-blocker):** May reduce fear memory reconsolidation when given within 1–6 hours of reactivating a trauma memory (controversial; reconsolidation blockade hypothesis)
- **Clonidine (α2 agonist):** Reduces LC firing → decreases NE release → reduces hyperarousal; used in children with PTSD/complex PTSD

## Pathology

### Trauma characteristics and risk factors

Not all trauma leads to PTSD. Risk and resilience factors include:

**Risk factors:**
- Trauma type: interpersonal violence (sexual assault, combat) > accidents > natural disasters
- Peritraumatic dissociation (strongest predictor of PTSD development)
- Prior trauma (especially childhood adversity — sensitizes amygdala and HPA axis)
- Genetic factors: heritability ~40%; Val66Met BDNF, FKBP5 (GR co-chaperone variants alter cortisol sensitivity), RELN (reelin)
- Female sex; poverty; lack of social support

**Resilience factors:**
- Strong social support (most protective modifiable factor)
- Prior mastery experiences; sense of agency
- High BDNF (exercise, social engagement)
- Rapid cortisol normalization after trauma (adequate glucocorticoid response)

### Treatment

**First-line evidence-based treatments:**

**Trauma-focused psychotherapy (superior to pharmacotherapy in most trials):**
- **Prolonged Exposure (PE):** Imaginal and in vivo exposure to trauma memories and avoided situations; disrupts conditioned fear through extinction learning; 50-60% remission [^foa-2019-ptsd-treatments]
- **Cognitive Processing Therapy (CPT):** Modifies maladaptive cognitions about trauma (stuck points); equivalent to PE; used widely in VA system
- **EMDR (Eye Movement Desensitization and Reprocessing):** Bilateral sensory stimulation during trauma memory processing; equivalent efficacy to PE/CPT; mechanism debated (eye movements may be inert — exposure component may drive benefit)

**Pharmacotherapy:**
- **SSRIs (sertraline, paroxetine):** FDA-approved for PTSD; moderate efficacy (~30-40% response); normalize serotonin and BDNF; useful for comorbid depression/anxiety
- **Venlafaxine (SNRI):** Off-label but evidence-based; addresses NE hyperarousal component
- **Prazosin (α1 antagonist):** For nightmares and sleep disruption; addresses NE-driven dream pathology
- **Benzodiazepines:** NOT recommended in PTSD — impair fear extinction learning (GABA-A-mediated amnesia blocks extinction consolidation); worsen long-term course despite short-term symptom reduction

**Novel/Emerging:**

**MDMA-assisted therapy:**
- Phase 3 trial (Mitchell et al., Nat Med 2021) [^mitchell-2021-mdma-ptsd]: MDMA-assisted therapy → 67% no longer met PTSD criteria vs. 32% placebo at 18-week endpoint; large effect size (d=0.9)
- Mechanism: MDMA releases serotonin, oxytocin, and NE → dampens amygdala reactivity while enabling emotional processing within therapy session; facilitates "therapeutic window" — processing trauma without overwhelming anxiety; may restore vmPFC-amygdala connectivity
- FDA Advisory Committee rejected approval (2024) on manufacturing and data integrity grounds; Phase 3b trial ongoing; widely available in clinical settings outside the US (Australia approved 2023)

**Stellate ganglion block:**
- Single injection of local anesthetic into cervical sympathetic ganglion; appears to reduce LC-sympathetic outflow; ~50-60% responder rate in RCTs for combat PTSD; mechanism may involve NGF-driven sympathetic hyperinnervation of LC

**Cannabis and cannabinoids:**
- Endocannabinoid system (CB1 receptors in amygdala and hippocampus) regulates fear extinction; THC reduces nightmare severity; synthetic nabilone approved in Canada for PTSD nightmares; clinical use outpacing evidence base

## Connections

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — locus coeruleus hyperactivation in PTSD drives excess NE → amygdala hyperreactivity, hyperarousal, and intrusive re-experiencing; prazosin (α1 antagonist) reduces NE-driven nightmares; propranolol given acutely after trauma may reduce fear memory reconsolidation.

- `connects-to` → **[Cortisol](../../../03-molecular/cortisol/README.md)** — PTSD exhibits paradoxical hypocortisolemia with enhanced GR sensitivity → excess negative feedback; low cortisol impairs fear extinction; hydrocortisone given within hours of trauma shows prophylactic benefit; opposite HPA profile from MDD despite clinical overlap.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — chronic stress-induced glucocorticoid BDNF suppression causes hippocampal volume loss (~8%) in PTSD; reduced BDNF impairs contextual fear discrimination; SSRIs normalize hippocampal BDNF and partially restore volume; Val66Met SNP increases PTSD risk.

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — NMDA receptors mediate fear memory consolidation and extinction in amygdala and vmPFC; D-cycloserine (partial NMDA agonist) enhances extinction learning in prolonged exposure therapy; ketamine reduces PTSD symptoms via BDNF/mTOR-mediated synaptic remodeling.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — PTSD features BLA hyperreactivity, reduced vmPFC-amygdala suppression, ~8% hippocampal volume reduction, and reduced anterior cingulate activation; normalization of amygdala-vmPFC functional connectivity is a biomarker of treatment response on task-based fMRI.

- `connects-to` → **[Oxytocin](../../../03-molecular/oxytocin/README.md)** — oxytocin facilitates fear extinction in the amygdala via OTR on CeA neurons; chronic stress reduces OT signaling; intranasal oxytocin is under investigation as an adjunct to exposure therapy to enhance extinction memory consolidation.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — SSRIs (sertraline, paroxetine) are FDA-approved for PTSD; serotonin modulates fear extinction in vmPFC; serotonin dysregulation contributes to hyperarousal, emotional numbing, and sleep disturbance; SNRIs (venlafaxine) are also evidence-based for PTSD symptom reduction.

- `connects-to` → **[CRH](../../../03-molecular/crh/README.md)** — PTSD shows CSF CRH excess, elevated ACTH, and paradoxically low cortisol (enhanced glucocorticoid feedback); CRH hyperdrive in amygdala/BNST drives hyperarousal and re-experiencing; CRHR1 antagonists are a proposed pharmacotherapy pending adequate clinical trials.

- `connects-to` → **[ACTH](../../../03-molecular/acth/README.md)** — PTSD exhibits a dissociated HPA pattern: normal or elevated ACTH responses to CRH challenge but chronically low basal cortisol, explained by GR hypersensitivity (enhanced negative feedback) rather than pituitary hypofunction; enhanced DST suppression (<0.5 µg/dL) is a biological signature of PTSD that distinguishes it from MDD.

- `connects-to` → **[NPY](../../../03-molecular/npy/README.md)** — amygdala and CSF NPY are reduced in PTSD; Y1R-mediated anxiolysis is impaired; plasma NPY correlates with stress resilience in veterans; glucocorticoid excess in chronic stress depletes amygdala NPY; NPY Y1R agonists are under investigation as PTSD pharmacotherapy.
- `connects-to` → **[Vasopressin](../../../03-molecular/vasopressin/README.md)** — CSF vasopressin is elevated in PTSD; AVP-CRH synergy at corticotroph V1bR potentiates ACTH when CRH receptors desensitise; elevated AVP sustains HPA hyperactivation; V1bR antagonists show anxiolytic effects and are a proposed PTSD pharmacotherapy.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — PTSD and major depression are highly comorbid and share neurobiology: HPA-axis and monoaminergic dysregulation, hippocampal changes, and overlapping symptoms link them, about half of PTSD patients also meet criteria for depression, and SSRIs treat both.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus is central to PTSD: reduced hippocampal volume impairs contextualizing fear memories, so trauma cues are not recognized as past, and the hippocampus fails to restrain an overactive amygdala—a core circuit abnormality targeted by trauma-focused therapy.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — PTSD and alcohol use disorder form a vicious cycle: many drink to blunt hyperarousal and intrusive memories, but alcohol fragments sleep and worsens PTSD, and the two strongly co-occur—so integrated treatment of both outperforms addressing either alone.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — PTSD and panic disorder share a hyperactive fear response but differ in trigger: both feature surges of autonomic arousal, but panic attacks come 'out of the blue' while PTSD's are cued by trauma reminders—and panic commonly complicates PTSD.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — PTSD and bipolar disorder frequently co-occur and worsen each other: trauma raises bipolar risk, comorbid PTSD predicts more mood episodes and suicidality, and overlapping irritability and arousal can blur diagnosis—so screening for trauma is part of bipolar assessment.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — PTSD and fibromyalgia are tightly linked through chronic stress: trauma and HPA-axis dysregulation promote central sensitization, so fibromyalgia is far more common in PTSD—evidence that psychological trauma can manifest as bodily pain.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — PTSD reflects a tipped excitatory-inhibitory balance: deficient GABAergic inhibition leaves fear circuits hyperexcitable, underlying hyperarousal and intrusive memories, which is why benzodiazepines that boost GABA paradoxically tend to worsen long-term PTSD.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep disturbance is a core feature of PTSD, not just a symptom: nightmares and insomnia are diagnostic criteria and can precede and perpetuate the disorder, and treating the insomnia (e.g., with prazosin or CBT-I) improves overall PTSD outcomes.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — PTSD and cannabis use disorder feed each other: many with PTSD use cannabis to dampen hyperarousal and insomnia, but tolerance and withdrawal worsen the symptoms it masks, so this common self-treatment readily slides into dependence.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The endocannabinoid system governs fear extinction central to PTSD: cannabinoid signaling helps the brain unlearn trauma cues, and deficits may lock in fear—so this pathway underlies why cannabis is sought for PTSD nightmares and why it is a drug-development target.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Adrenaline burns trauma into memory: the epinephrine surge during a terrifying event strengthens memory consolidation, helping explain PTSD's intrusive recollections—and why beta-blockers like propranolol have been tested to blunt or weaken fear memories.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — PTSD and borderline personality disorder share a traumatic root: childhood trauma drives both, and complex PTSD overlaps BPD's emotional dysregulation and unstable relationships—so the two frequently co-occur and can be hard to disentangle clinically.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — PTSD dysregulates the adrenal stress axis: chronic trauma alters HPA-axis output so the adrenal gland's cortisol response is blunted and abnormal, leaving the noradrenergic alarm system unrestrained—part of the biology behind hypervigilance and flashbacks.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Trauma leaves an inflammatory mark via microglia: PTSD is linked to activated brain microglia and neuroinflammation that may damage the hippocampus and prefrontal cortex, connecting psychological trauma to measurable brain changes.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine ties PTSD to reward and to its therapies: trauma blunts reward-related dopamine signaling (contributing to numbing and anhedonia), and dopamine is part of why MDMA-assisted therapy is being studied to help process traumatic memories.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — PTSD strikes women about twice as often, and estrogen is part of why: the hormone shapes fear extinction, so low-estrogen phases impair the unlearning of fear—helping explain sex differences in risk and the timing of intrusive symptoms.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — PTSD wrecks sleep, and melatonin is enlisted to mend it: nightmares and insomnia are core symptoms tied to disrupted circadian and REM regulation, so melatonin and sleep-targeted therapy are used alongside trauma treatment.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — PTSD's fear circuits depend on astrocytes: these glial cells regulate glutamate in the amygdala and hippocampus that encode and extinguish fear, so astrocyte dysfunction can lock in the traumatic memory that drives the disorder.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — PTSD is hard on the heart: chronic hyperarousal keeps stress hormones and blood pressure high and stokes inflammation, and survivors carry a markedly raised risk of heart attack and cardiovascular disease, making PTSD a cardiac risk factor.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Traumatic memories are cemented by calcium: fear learning in the amygdala relies on calcium flooding through NMDA receptors to strengthen synapses, the molecular step that locks a terrifying event into a lasting, intrusive memory.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — PTSD lives in overstrengthened synapses: trauma potentiates the amygdala's fear synapses while weakening the prefrontal control over them, and therapy works by reconsolidating or extinguishing these synaptic memories.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Brain imaging maps PTSD: fMRI photons reveal an overactive amygdala and underactive prefrontal cortex, alongside a smaller hippocampus, the neural signature of trauma's lasting grip.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — PTSD is written in neurons: amygdala fear neurons overfire while the hippocampal and prefrontal neurons that should place the fear in context and dampen it are impaired, so danger feels ever-present.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — PTSD's stress axis is paradoxically hypersensitive: more sensitive glucocorticoid receptors enhance cortisol's negative feedback, so cortisol runs low even as the system overreacts to reminders of trauma.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Trauma may reshape the brain's wiring insulation: chronic stress alters oligodendrocytes and myelination in the fear-circuit tracts, and the resulting white-matter changes are seen on imaging in PTSD.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — PTSD speaks to the gut: it is tightly comorbid with irritable bowel syndrome, the trauma-primed stress axis and altered gut-brain signaling disturbing motility and sensation in the bowel.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Chronic stress burns through magnesium: the sustained HPA activation of PTSD depletes the mineral, and because magnesium restrains both the stress axis and the NMDA receptors of fear, its loss can deepen the hyperarousal.
- `connects-to` → **[Immune System](../immune-system/README.md)** — PTSD smolders with inflammation: chronic stress raises CRP and inflammatory cytokines and dysregulates immune cells, helping explain the higher rates of autoimmune and cardiovascular disease and a kind of accelerated aging in sufferers.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Trauma settles in the gut: through the brain-gut axis PTSD drives functional dyspepsia, nausea, and irritable bowel, and the stomach's churning becomes a somatic echo of the hypervigilant nervous system.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Chronic stress turns down the sex hormones: sustained cortisol from PTSD suppresses the HPG axis, lowering testosterone and contributing to the reduced libido, fatigue, and low mood that often accompany the disorder.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Trauma leaves an inflammatory, autoimmune mark: PTSD raises circulating inflammatory markers and autoantibodies and is linked to a higher risk of autoimmune diseases, a body-wide signature of chronically dysregulated stress and immunity.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — PTSD is hard on the heart and vessels: years of sympathetic and cortisol overdrive raise blood pressure and accelerate atherosclerosis, giving these patients a substantially higher rate of heart attack and cardiovascular death.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — PTSD and reproduction intertwine: sexual trauma is a major cause, the disorder disrupts sexual function and intimacy, and it strikes women about twice as often, with symptoms shifting across the menstrual cycle and the perinatal period.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Trauma leaves an inflammatory signature: PTSD runs with elevated IL-6 and other inflammatory markers, a low-grade immune activation thought to link the disorder to its heart and metabolic complications and even to influence fear circuitry.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The traumatized brain talks to the gut and back: PTSD is marked by an altered microbiome, and through the microbiome-gut-brain axis these shifts may shape stress reactivity, inflammation, and the disorder's resilience or severity.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — PTSD and chronic pain feed each other: they co-occur strikingly often, sharing central sensitization and stress circuitry, so trauma amplifies neuropathic pain while persistent pain keeps the traumatic memory alive.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Chronic alarm raises the pressure: the sustained sympathetic and HPA-axis overdrive of PTSD keeps blood pressure elevated, a major route by which trauma translates into long-term cardiovascular disease.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Stress hormones disturb metabolism: chronically high cortisol with poor sleep and lifestyle disruption raises the risk of insulin resistance and type 2 diabetes among people with PTSD.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — It overlaps the broader anxiety spectrum: PTSD shares fear-circuit dysregulation and frequently co-occurs with generalized anxiety disorder, the two amplifying each other's worry and hypervigilance.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic stress smolders as inflammation: PTSD shows elevated NF-κB activity in immune cells, a stress-driven inflammatory signal that helps explain its raised risk of cardiovascular and metabolic disease.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is a disorder of the brain's fear circuitry: PTSD reflects dysregulation across the amygdala, hippocampus and prefrontal cortex of the nervous system, the network that normally extinguishes fear after a threat passes.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Trauma drives self-medication with opioids: PTSD is strongly comorbid with opioid use disorder, as sufferers turn to opioids to blunt hyperarousal and intrusive memories, deepening the addiction.
- `connects-to` → **[Obesity](../obesity/README.md)** — Chronic stress reshapes the body: sustained cortisol, disrupted sleep and emotional eating in PTSD promote weight gain and central adiposity, contributing to a high rate of obesity and metabolic syndrome.
- `connects-to` → **[Stroke](../stroke/README.md)** — Relentless stress wears on the vessels: PTSD's chronic sympathetic and HPA-axis activation raises blood pressure and inflammation, and epidemiologic studies link it to a higher long-term risk of ischemic stroke.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The stressed heart can fail over time: chronic catecholamine surges, hypertension and inflammation in PTSD accelerate cardiovascular disease, and the disorder is associated with an increased incidence of heart failure.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Chronic stress inflames the arteries: the sustained sympathetic arousal, cortisol dysregulation and systemic inflammation of PTSD accelerate atherosclerosis, underlying its raised cardiovascular risk.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Trauma can prime autoimmunity: PTSD is associated with a higher incidence of autoimmune diseases such as rheumatoid arthritis, thought to reflect chronic stress-driven immune dysregulation.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Lasting stress wears on the aging brain: PTSD is linked to a higher risk of dementia, with chronic cortisol exposure and hippocampal injury contributing to later Alzheimer-type cognitive decline.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Trauma is felt in the gut: PTSD strongly co-occurs with irritable bowel syndrome and functional GI disorders, with the dysregulated gut-brain axis and autonomic arousal driving abdominal pain and altered bowel habit.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Trauma can tip into psychosis: severe and childhood trauma is a recognised risk factor for schizophrenia, and PTSD with psychotic features overlaps with it, the two frequently co-occurring.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Two anxiety-spectrum disorders intertwine: PTSD and OCD frequently coexist, with trauma sometimes precipitating obsessive-compulsive symptoms and the intrusive thoughts of each reinforcing the other.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It carries a distinctive hormone signature: PTSD is marked by low basal cortisol with enhanced glucocorticoid negative feedback — dexamethasone hypersuppression — unlike most chronic-stress states.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Fear seizes the breath: flashbacks and panic in PTSD trigger hyperventilation and breathlessness, and the disorder is associated with higher rates of asthma and respiratory symptoms.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Constant hyperarousal tenses the body: the sustained muscle tension of PTSD's hypervigilance contributes to chronic neck, back and widespread musculoskeletal pain.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Trauma surfaces on the skin: chronic stress flares psoriasis and eczema, triggers stress-related alopecia and urticaria, and trauma-related behaviours can mark the skin.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It raises kidney-disease risk: PTSD-associated hypertension, metabolic syndrome and chronic stress are linked to a higher risk of chronic kidney disease, well documented in veterans.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — SSRIs are first-line medication: serotonergic antidepressants such as the SSRIs are the first-line pharmacotherapy for PTSD, used alongside trauma-focused psychotherapy.
- `connects-to` → **[Beta-Blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — They blunt the adrenergic surge: beta-blockers like propranolol, and the related alpha-blocker prazosin, reduce the hyperarousal and nightmares of PTSD by dampening noradrenergic overactivity.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet is studied for resilience: omega-3 supplementation has been trialled to prevent or ease PTSD after trauma, though the evidence remains modest and uncertain.
- `connects-to` → **[Ashwagandha](../../../03-medicine/02-traditional/ashwagandha/README.md)** — Traditional calm is sought: adaptogens such as ashwagandha are used for the chronic stress and poor sleep of PTSD, complementing trauma-focused therapy and SSRIs.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — Overlapping fear and avoidance: PTSD and social anxiety disorder share hyperarousal, avoidance and exaggerated threat appraisal, frequently co-occur, and trauma can precipitate or worsen social anxiety.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Self-medication and comorbidity: stimulant and other substance use is common in PTSD as patients try to numb or override hyperarousal, and the disorders worsen each other's course and treatment.
- `connects-to` → **[St John's Wort](../../../03-medicine/02-traditional/st-johns-wort/README.md)** — A herbal serotonergic adjunct: St John's wort, raising serotonin like the SSRIs that are first-line for PTSD, is used by some for the comorbid depression, though evidence is limited and drug interactions are a concern.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Disordered REM connects them: PTSD fragments REM sleep with nightmares and hyperarousal, overlapping the disrupted REM regulation and daytime sleepiness of narcolepsy, and the two are comorbid.
- `connects-to` → **[Migraine](../migraine/README.md)** — Stress and headache feed each other: PTSD and migraine are strongly comorbid, sharing stress-axis and serotonergic dysregulation and central sensitisation, so each worsens the other's course.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — The heart pays for chronic stress: sustained catecholamine and cortisol surges in PTSD raise cardiovascular risk, and acute severe stress can stun the myocardium as Takotsubo (stress) cardiomyopathy.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Trauma and autoimmunity: PTSD is associated with a higher later incidence of autoimmune diseases such as lupus, the chronic stress and inflammation dysregulating immune tolerance.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A pandemic mental-health toll: COVID-19 survivors—especially after ICU care—and frontline workers show high rates of PTSD, the life-threatening illness and isolation acting as traumatic stressors.
- `connects-to` → **[Bulimia Nervosa](../bulimia-nervosa/README.md)** — Trauma and disordered eating: childhood trauma and PTSD strongly predispose to bulimia and binge-eating, the bingeing and purging serving as affect regulation for trauma-driven distress.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Autonomic toll: PTSD's chronic sympathetic overdrive reduces heart-rate variability and raises arrhythmia and sudden-cardiac-death risk, the conduction-system consequence of a perpetually activated stress response.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Trauma and seizures: psychogenic nonepileptic seizures are strongly tied to trauma and PTSD and are the key differential of epilepsy, while PTSD and epilepsy are also bidirectionally associated.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The gut-brain axis in trauma: PTSD alters the microbiome and intestinal barrier, the epithelium mediating stress-related GI symptoms and low-grade inflammation that feed back to the traumatised brain.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Neuroinflammation: elevated IL-1β from activated microglia is linked to the fear-circuit dysfunction and memory consolidation abnormalities of PTSD.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory signature: raised TNF-α is among the peripheral inflammatory markers consistently found in PTSD, tying chronic stress to systemic low-grade inflammation.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Stress inflammasome: chronic stress activates the NLRP3 inflammasome, and its IL-1β output is increasingly implicated in the neuroinflammatory component of PTSD.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — Treatment and gene-environment risk: SSRIs blocking the serotonin transporter are first-line for PTSD, and the 5-HTTLPR transporter polymorphism is among the most studied gene-by-trauma interactions in the disorder.
- `connects-to` → **[β1-Adrenergic Receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — Fear-memory reconsolidation: noradrenaline acting on β-adrenergic receptors strengthens traumatic memory consolidation, the rationale for propranolol to blunt reconsolidation and the hyperarousal of PTSD.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Neuroinflammatory recruitment: elevated CCL2 in PTSD recruits monocytes that traffic to the brain, contributing to the microglial activation and inflammation linked to its stress-related neuropathology.
- `connects-to` → **[μ-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Opioid analgesia given soon after trauma lowers later PTSD risk, and endogenous opioid signaling shapes fear extinction—implicating the μ-opioid system in the consolidation of traumatic memory and in resilience.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Reduced allopregnanolone, a progesterone metabolite and positive GABA-A modulator, is found in PTSD, weakening the inhibitory tone that normally restrains the fear and arousal circuits and offering a neurosteroid treatment target.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Substance P is elevated in PTSD and acts on NK1 receptors in the amygdala to heighten anxiety and the stress response, a neuropeptide arm of the hyperarousal that complements the noradrenergic surge.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Elevated orexin signaling drives the chronic hyperarousal, fragmented sleep and nightmares of PTSD, the wake-promoting system whose overactivity underlies the disorder's prominent sleep disturbance.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Ghrelin enhances fear learning and the persistence of traumatic memories, a stress-responsive hormone that potentiates amygdala fear circuits and is implicated in the over-consolidated fear memory at the core of PTSD.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Cholinergic signaling contributes to the exaggerated startle response and autonomic hyperreactivity of PTSD, the parasympathetic-sympathetic imbalance that accompanies the noradrenergic hyperarousal.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling in the amygdala consolidates and reconsolidates fear memories, the molecular substrate of the intrusive traumatic-memory persistence and reactivity central to PTSD.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Synaptic mTOR-dependent protein synthesis underlies the reconsolidation and extinction of fear memory, a plasticity mechanism of interest for memory-targeted PTSD treatments.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Innate-immune TLR4 signaling links chronic traumatic stress to the neuroinflammation (IL-1β, IL-6 and TNF-α already mapped) increasingly implicated in the pathophysiology of PTSD.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling (with mTOR and ERK1/2 mapped) relays the BDNF-driven (mapped) synaptic plasticity that consolidates the traumatic fear memories of PTSD.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates fear-memory reconsolidation and extinction, the processes disrupted in PTSD and modulated by mood-stabilizer therapy.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4 (mapped) signals through MyD88 to drive the microglial neuroinflammation (IL-1β, IL-6 and TNF mapped) increasingly linked to PTSD risk and severity.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine-driven JAK-STAT signaling (IL-6 mapped) transduces the peripheral and central inflammatory milieu associated with PTSD symptom severity.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement-mediated synaptic pruning (C3 tagging) in fear-circuit regions is implicated in the aberrant remodeling that underlies PTSD memory pathology.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 is induced during stress-driven neuroinflammation, amplifying the reactive microglial state linked to PTSD.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF-TrkB (NTRK) signaling (BDNF already mapped) drives the hippocampal and amygdalar plasticity underlying fear conditioning and extinction in PTSD.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the chronic inflammatory tone associated with the stress-driven neuroinflammation of PTSD.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic mitochondrial DNA released during chronic stress can engage cGAS-STING, contributing to the neuroinflammation implicated in PTSD.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 neuroinflammatory signaling contributes to the chronic low-grade inflammation reported in PTSD.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to the stress physiology of PTSD.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of stress and PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress and resilience relevant to the fear-circuit plasticity of PTSD.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and mitochondrial stress responses contribute to the neurobiology of post-traumatic stress disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the neuronal plasticity of the fear-memory circuits altered in post-traumatic stress disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK metabolic signaling participates in the neuronal energetic and stress-adaptation responses relevant to post-traumatic stress disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic (traumatic-memory and FKBP5-linked) programming implicated in post-traumatic stress disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal stress responses and fear-memory circuits implicated in post-traumatic stress disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the synaptic plasticity of the fear-memory consolidation of post-traumatic stress disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with post-traumatic stress disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and hippocampal-plasticity processes implicated in post-traumatic stress disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in post-traumatic stress disorder.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with post-traumatic stress disorder.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic (trauma-related) programming implicated in post-traumatic stress disorder.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the fear-memory-related synaptic plasticity and neuroimmune activation of post-traumatic stress disorder.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Brain renin-angiotensin: central angiotensin II modulates fear consolidation and the stress response, and angiotensin-receptor blockers such as losartan are associated with reduced PTSD symptoms, a neuroendocrine target beyond the monoamine and HPA systems already mapped.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Fear-memory plasticity: nitric oxide from neuronal nNOS is required for the synaptic plasticity of fear conditioning in the amygdala, implicating NO signalling in the formation of the intrusive traumatic memories of PTSD.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Arousal regulation: central histaminergic neurotransmission drives wakefulness and arousal, systems pathologically heightened in the hypervigilance, exaggerated startle and sleep disturbance of post-traumatic stress disorder.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response and fear memory dysregulated in post-traumatic stress disorder.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic dysregulation: chronic stress in PTSD promotes insulin resistance and the metabolic syndrome (cortisol already mapped), part of the cardiometabolic burden that raises long-term physical illness in affected patients.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiovascular risk: the sustained sympathetic activation (norepinephrine already mapped) of PTSD raises the risk of coronary disease and myocardial infarction, and troponin elevation marks the cardiac injury of these excess cardiovascular events.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cardiometabolic dyslipidaemia: the chronic stress and insulin resistance (insulin already mapped) of PTSD shift cholesterol handling toward an atherogenic profile, part of the cardiometabolic burden that raises its long-term cardiovascular risk.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6, TNF and IL-1 already mapped) reported in PTSD modulate the fear and stress circuits, part of the immune-inflammatory dimension of the disorder.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory balance: the anti-inflammatory IL-10 counters the chronic low-grade inflammation (IL-6, TNF and IL-1 already mapped) of PTSD, and the imbalance toward pro-inflammatory signalling is part of its cardiometabolic and neuropsychiatric burden.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation reported in PTSD.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and noradrenaline: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the noradrenergic hyperarousal central to PTSD.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and fear memory: zinc modulates the glutamatergic (already mapped) NMDA signalling of the fear-memory circuits, and low zinc status is associated with the mood and anxiety symptoms that accompany PTSD.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation (TNF, IL-6 and IL-1 already mapped) implicated in PTSD.
- `connects-to` → **[Borderline personality disorder](../borderline-personality-disorder/README.md)** — Trauma-spectrum overlap: borderline personality disorder is strongly linked to childhood trauma and overlaps with complex PTSD, the two sharing the HPA-axis (cortisol and CRH already mapped) dysregulation and affective instability.
- `connects-to` → **[Generalized anxiety disorder](../generalized-anxiety-disorder/README.md)** — Anxiety comorbidity: generalized anxiety disorder commonly co-occurs with PTSD, part of the anxious-hyperarousal (noradrenaline already mapped) symptom burden that accompanies the trauma disorder.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic-inflammatory adipokine: leptin is the adipokine of the metabolic-inflammatory milieu; PTSD is associated with the metabolic dysregulation (insulin already mapped) and the adipokine changes.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory milieu of PTSD.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the metabolic-inflammatory (IL-6 and TNF already mapped) dimension of PTSD.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-1 and TNF already mapped) implicated in PTSD.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation associated with the chronic stress of PTSD.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of PTSD.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with the chronic stress of PTSD.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension associated with PTSD.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the stress-related immune dysregulation of PTSD.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the stress-reactive (histamine already mapped) dimension of PTSD.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic stress of PTSD.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Stress-modulated NK: the NK-cell number and cytotoxicity, altered by the chronic stress and cortisol (already mapped) reactivity, are part of the peripheral immune dysregulation of PTSD.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the low-grade complement activation of the chronic-stress neuroinflammation implicated in PTSD.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) neuroinflammation implicated in PTSD.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the chronic-stress neuroinflammation of PTSD.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuro-immune alarmin: TSLP, released by skin (already mapped) and gut-epithelial (already mapped) barriers under chronic stress, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the systemic low-grade immune activation of PTSD.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin stress-response axis: bradykinin, generated by the kallikrein-kinin system activated by trauma-related inflammation, augments blood-brain-barrier permeability and amplifies the microglial (already mapped) neuroinflammation of PTSD.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) activation in the stress-sensitised CNS environment, moderating neuroinflammation of PTSD.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM remodelling in the fear-memory circuit: periostin, expressed by astrocytes (already mapped) and microglia (already mapped) in the amygdala and hippocampus, modulates the extracellular matrix perineuronal nets that consolidate the maladaptive fear memories of PTSD.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuro-protective cytokine: erythropoietin, via EPOR on hippocampal neurons and astrocytes (already mapped), promotes neurogenesis and limits the HPA-axis-driven (cortisol already mapped) hippocampal volume loss and the neuroinflammatory burden of PTSD.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Stress-endocrine coupling: prolactin, elevated after acute trauma and stress (HPA-axis already mapped), modulates the T-cell (already mapped) and NK-cell (already mapped) immune function and contributes to the female-predominant vulnerability to PTSD.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — PTSD factor-h: factor H limits alternative complement (C5 already mapped) in the neuroinflamed brain (already mapped); impaired factor H amplifies microglial (already mapped) and astrocyte (already mapped) complement-driven hippocampal (already mapped) damage of PTSD.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — PTSD transferrin: transferrin supports brain (already mapped) iron homeostasis and dopamine (already mapped) synthesis; iron dyshomeostasis amplifies hippocampal (already mapped) neurodegeneration and cortisol (already mapped) HPA-axis disruption of PTSD.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — PTSD iron: iron supports brain (already mapped) myelination and dopamine (already mapped) synthesis; iron deficiency amplifies hippocampal (already mapped) neurodegeneration and cortisol (already mapped) HPA-axis dysregulation in PTSD.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — PTSD selenium: selenoprotein P reduces hippocampal (already mapped) neuron (already mapped) oxidative stress and microglial activation; selenium deficiency amplifies the NF-κB (already mapped) neuroinflammation and the cortisol (already mapped) HPA-axis dysregulation of PTSD.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — PTSD iodine: iodine-dependent thyroid hormones regulate hippocampal (already mapped) neurogenesis and cortisol (already mapped) HPA-axis homeostasis; thyroid-hormone deficiency amplifies the NF-κB (already mapped) neuroinflammation and worsens trauma memory consolidation in PTSD.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — PTSD sodium: sodium regulates GABAergic (already mapped) and glutamatergic (already mapped) neurotransmission in hippocampal (already mapped) fear circuits; sodium-driven aldosterone (already mapped) excess amplifies the NF-κB (already mapped) neuroinflammation of PTSD.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — PTSD potassium: potassium, via Kv7/HCN channels in neurons (already mapped) and astrocytes (already mapped), regulates fear-circuit excitability; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of PTSD.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — PTSD phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and microglia (already mapped), supports synaptic plasticity and memory consolidation; phosphorus deficiency amplifies the NF-κB (already mapped) and cortisol (already mapped) HPA-axis cascade of PTSD.

[^yehuda-2015-ptsd-review]: Yehuda R, Hoge CW, McFarlane AC, et al. Post-traumatic stress disorder. *Nat Rev Dis Primers.* 2015;1:15057. [doi:10.1038/nrdp.2015.57](https://doi.org/10.1038/nrdp.2015.57) · [PubMed 27189040](https://pubmed.ncbi.nlm.nih.gov/27189040/)
[^foa-2019-ptsd-treatments]: Foa EB, McLean CP. The efficacy of exposure therapy for anxiety and related disorders. *Annu Rev Clin Psychol.* 2016;12:1-28. [doi:10.1146/annurev-clinpsy-021815-093533](https://doi.org/10.1146/annurev-clinpsy-021815-093533) · [PubMed 26928206](https://pubmed.ncbi.nlm.nih.gov/26928206/)
[^mitchell-2021-mdma-ptsd]: Mitchell JM, Bogenschutz M, Lilienstein A, et al. MDMA-assisted therapy for severe PTSD: a randomized, double-blind, placebo-controlled phase 3 trial. *Nat Med.* 2021;27(6):1025-1033. [doi:10.1038/s41591-021-01336-3](https://doi.org/10.1038/s41591-021-01336-3)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
