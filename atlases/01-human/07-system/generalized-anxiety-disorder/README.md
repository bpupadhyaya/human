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
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid disease can masquerade as anxiety: an overactive thyroid causes palpitations, tremor, sweating, and restlessness indistinguishable from GAD, so thyroid hormones are checked before settling on a psychiatric diagnosis—a treatable mimic not to miss."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Anxiety and the gut talk constantly in GAD: worry triggers nausea, cramping, and bowel changes, and irritable bowel syndrome frequently coexists, so the gut-brain axis makes digestive symptoms a core, distressing feature of generalized anxiety."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus links stress to anxiety: chronic cortisol in GAD can shrink and impair it, weakening the brake it normally puts on the stress response, so a stress-damaged hippocampus may help lock worry into a self-sustaining loop."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Anxiety can be a thyroid problem in disguise: an overactive thyroid causes palpitations, tremor, restlessness and worry that mimic generalized anxiety, so checking thyroid function is essential before treating—and correcting it can resolve the symptoms."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Caffeine fuels anxiety by blocking adenosine: adenosine normally promotes calm and sleepiness, so caffeine's blockade heightens arousal and can trigger or worsen generalized anxiety—why cutting caffeine is first-line advice."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Generalized anxiety has a neuroinflammatory side in microglia: chronic stress activates brain microglia that release cytokines altering mood circuits, linking the immune system to persistent worry and the overlap of anxiety with inflammatory illness."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Generalized anxiety keeps the adrenal glands switched on: chronic worry drives the HPA axis to make the adrenals pour out cortisol, and this sustained stress-hormone output underlies the fatigue, tension and health toll of long-term anxiety."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Low magnesium can heighten anxiety: the mineral normally restrains the NMDA receptor and supports GABA, so deficiency tips the brain toward excitation, which is why magnesium status is studied in relation to anxiety symptoms."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The endocannabinoid system helps set the brain's anxiety thermostat: it dampens stress circuits and fear responses, so when this tone falls anxiety rises, making the system a target behind why cannabis can both calm and worsen worry."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Anxiety is tuned at the synapse: the balance of excitatory glutamate and inhibitory GABA across amygdala and prefrontal synapses sets how strongly threat signals fire, and shifting that synaptic balance toward excitation drives chronic worry."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Anxiety speaks through the gut: the gut-brain axis ties worry to the large intestine, so anxiety triggers cramping and changed bowel habits, and a troubled gut signals back to heighten anxiety—the loop behind anxiety's overlap with IBS."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Generalized anxiety reflects over-firing neurons: hyperexcitable cells in the amygdala and worry circuits respond too readily to threat while calming inputs lag, the cellular imbalance that medications and therapy work to settle."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Anxiety shows on fMRI: photons map an overactive amygdala and weak prefrontal control, the brain pattern of an exaggerated threat response that underlies generalized anxiety."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes tune the anxiety circuit's glutamate, and their dysfunction is implicated in the over-excitable fear networks of generalized anxiety, extending the disorder beyond neurons alone."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Anxiety quickens the breath: hyperventilation and air hunger are core physical symptoms, and the low CO2 that results causes the tingling and lightheadedness of an anxiety attack."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc helps keep anxiety in check: it modulates the GABA and glutamate balance of the calming circuits, and low zinc is reported in anxiety disorders, with supplementation studied as an adjunct to standard treatment."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Anxiety churns the stomach: the gut-brain axis turns worry into nausea, 'butterflies,' and functional dyspepsia, so abdominal distress is one of the most common bodily complaints of generalized anxiety."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D shadows the anxious mind: deficiency is associated with higher anxiety, and the vitamin's receptors throughout mood-regulating brain regions suggest it helps tune the circuits that worry overactivates."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Worry steals sleep through the clock: GAD's racing mind delays sleep onset and blunts melatonin, and the resulting insomnia loops back to sharpen the next day's anxiety — a cycle melatonin and sleep hygiene aim to break."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Anxiety shows on the skin: the autonomic surge brings sweating, flushing, and goosebumps, and chronic stress flares skin conditions like eczema and hives through the brain-skin axis."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Sex hormones color the worry: GAD is about twice as common in women, and anxiety often intensifies premenstrually, in the postpartum, and around menopause as estrogen and progesterone swing."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Chronic worry leaves an inflammatory trace: GAD is associated with raised IL-6 and other inflammatory markers, fitting a model in which sustained stress-axis activation primes low-grade inflammation that acts back on the anxious brain."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The body's smooth muscle carries the tension: chronic anxiety clenches gut and airway smooth muscle into the cramping, bloating, and chest tightness of GAD's somatic symptoms, the physical face of relentless worry."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Sustained anxiety hardens the arteries: the chronic sympathetic and cortisol drive of GAD raises blood pressure and inflammation that accelerate atherosclerosis, contributing to its long-term cardiovascular risk."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Chronic worry erodes neuroplasticity: GAD is marked by lower BDNF, weakening the synaptic remodeling that lets the brain adapt, and treatments that raise BDNF parallel recovery from anxiety."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stress reaches the mast cell: brain and gut mast cells carry receptors for the stress peptide CRH, releasing mediators that may link anxiety to its headaches, flushing, and the visceral hypersensitivity of an anxious gut."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Worry leaves a metabolic mark: the chronic cortisol of GAD promotes insulin resistance and central fat, and anxiety and type 2 diabetes each raise the risk of the other in a two-way link."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Chronic stress inflames the brain: NLRP3 inflammasome activation in microglia releases IL-1β that disturbs the mood and fear circuits, part of the neuroinflammation increasingly tied to anxiety disorders."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "A calming hormone opposes the worry: oxytocin dampens amygdala fear responses and buffers stress, the anxiolytic, social-bonding signal whose deficiency may leave the threat circuits of GAD unchecked."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Sustained alarm raises the pressure: the chronic sympathetic and cortisol drive of GAD keeps blood pressure elevated, one route by which long-term anxiety translates into cardiovascular disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic worry leaves an inflammatory mark: persistent stress in GAD activates NF-κB-driven cytokine signaling, the neuroinflammatory thread linking anxiety to its raised cardiovascular and metabolic risk."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is a disorder of the brain's threat circuitry: GAD reflects an overactive amygdala-driven fear network with weak prefrontal restraint, dysregulation of the nervous system's normal worry-and-safety balance."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "People reach for cannabis to quiet the worry: GAD frequently co-occurs with cannabis use disorder, as users self-medicate anxiety even though heavy use and withdrawal can ultimately worsen it."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Chronic worry strains the heart: the sustained sympathetic activation of GAD raises heart rate and blood pressure and is associated with worse cardiac outcomes, contributing over time to heart failure risk."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Anxiety tracks with cerebrovascular risk: the chronic stress, hypertension and inflammation of long-standing GAD are linked epidemiologically to a higher long-term risk of stroke."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Stress reshapes appetite and activity: cortisol-driven cravings, comfort eating and reduced activity in GAD, compounded by some anxiolytic medications, contribute to weight gain and obesity."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Breathlessness and anxiety amplify each other: GAD is highly comorbid with COPD, where air hunger triggers panic and chronic worry, and anxiety in turn worsens dyspnea and disability."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Chronic worry may wear on the aging brain: sustained cortisol elevation and the long-term sedatives used for GAD are associated with an increased risk of later cognitive decline and dementia."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Stress hormones and sedative falls cost bone: chronic cortisol elevation in GAD lowers bone density, while the benzodiazepines often used raise fall and fracture risk on already fragile bone."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones both mimic and drive it: thyrotoxicosis, phaeochromocytoma and cortisol dysregulation produce anxiety identical to GAD, and chronic worry itself dysregulates the HPA stress axis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chronic worry presses on the heart: GAD causes palpitations and sustained sympathetic arousal, and is independently associated with raised blood pressure and cardiovascular events including takotsubo cardiomyopathy."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "They frequently travel together: anxiety disorders are highly comorbid with ADHD, where inattention and the strain of coping fuel worry, and stimulant treatment can itself heighten anxiety."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Worry lives in the muscles: persistent muscle tension, aches and tension headaches are core somatic features of generalized anxiety disorder, often the symptoms that bring people to the doctor."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Chronic worry unsettles immunity: sustained anxiety dysregulates cortisol and raises inflammatory markers, blunting immune function over time."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Anxiety surfaces on the skin: stress aggravates eczema, psoriasis and itch and drives sweating, and skin-picking or hair-pulling behaviours can accompany chronic anxiety."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Breathing carries the symptoms: anxiety drives hyperventilation, breathlessness and chest tightness, and a vicious circle ties it tightly to asthma and breathing disorders."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "First-line treatment is an antidepressant: SSRIs like fluoxetine are the mainstay for generalized anxiety disorder, preferred over benzodiazepines for long-term control."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "Diet draws interest: low magnesium status has been linked to anxiety and supplementation trialled as an adjunct, though the evidence remains modest."
  - target: 03-medicine/02-traditional/ashwagandha
    relation: connects-to
    note: "A traditional anxiolytic with evidence: ashwagandha, an adaptogenic herb, reduces anxiety and cortisol in trials and is among the better-supported complementary treatments for generalized anxiety."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet offers a modest adjunct: omega-3 supplementation shows small anxiolytic effects in some trials, used alongside but not instead of first-line therapy for generalized anxiety."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "The gut and worry feed each other: anxiety is far more common in inflammatory bowel disease, and through the gut-brain axis disease flares and chronic worry each worsen the other."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "They blunt the body's anxiety: beta-blockers like propranolol damp the adrenergic physical symptoms of anxiety — racing heart, tremor, sweating — useful for performance and situational anxiety though they do not treat the underlying worry."
  - target: 03-medicine/02-traditional/st-johns-wort
    relation: connects-to
    note: "A herbal serotonergic option: St John's wort, which raises serotonin like the SSRIs used for anxiety, is taken by some for mild anxiety and depression, though efficacy is uncertain and it interacts with many drugs."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "Chronic anxiety amid instability: generalized anxiety is a frequent comorbidity of borderline personality disorder, sharing emotional dysregulation and an exaggerated threat response that compound each other."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "The brain's anti-anxiety neuropeptide: NPY buffers the stress response and amygdala reactivity, and low NPY tone tracks with anxiety vulnerability and poor resilience—an endogenous counterweight to the CRH-driven stress underlying GAD."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Anxiety and compulsive reward feed each other: people with GAD may gamble to escape anxious distress, and mounting losses deepen worry—a bidirectional loop between anxiety and behavioural addiction."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Why anxiety feels like the heart: GAD's autonomic arousal drives palpitations, sinus tachycardia and ectopy through the conduction system, the somatic symptom that brings many anxious patients to cardiology and the rationale for beta-blockade."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "The commonest psychiatric comorbidity of seizures: anxiety is the most frequent psychiatric companion of epilepsy, bidirectionally linked through shared GABAergic dysfunction and the stress of unpredictable seizures."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Anxiety amplifies pain: generalized anxiety disorder commonly coexists with chronic and neuropathic pain, each worsening the other through shared serotonergic-noradrenergic pathways that SNRIs like duloxetine target in both."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A pandemic of anxiety: COVID-19 sharply raised rates of generalized anxiety through health fears, isolation and bereavement, and post-COVID neuroinflammation may directly worsen anxiety symptoms."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "The organic anxiety mimic: a catecholamine-secreting phaeochromocytoma causes paroxysmal anxiety, palpitations and sweating that imitate generalized anxiety, a can't-miss endocrine cause to exclude in atypical cases."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The gut-brain axis: generalized anxiety overlaps heavily with irritable bowel syndrome, with the intestinal epithelium and microbiome signalling to anxiety circuits via the vagus and immune pathways."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Anxiety and the heart muscle: chronic anxiety raises cardiovascular risk, and acute extreme stress can precipitate Takotsubo (stress) cardiomyopathy, transiently stunning the myocardium."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory anxiety: IL-1β from activated microglia is implicated in the neuroinflammation increasingly linked to anxiety, with chronic stress raising this innate cytokine."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Stress cytokine: elevated TNF-α is among the inflammatory markers found in generalised anxiety, part of the bidirectional link between chronic stress and systemic inflammation."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Threat and reward: dopaminergic signalling shapes the uncertainty and threat appraisal that drive anxiety, and its dysregulation contributes to the avoidance and anticipatory worry of GAD."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid anxiolysis: the progesterone metabolite allopregnanolone is a positive GABA-A modulator, so its fluctuations shape anxiety and underlie the neurosteroid drugs developed for anxiety and depression."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Stress-axis amplifier: vasopressin synergises with CRH to drive the HPA-axis hyperactivity of generalised anxiety, sustaining the heightened stress reactivity central to the disorder."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Neuroinflammatory link: CCL2 recruits monocytes to the brain and is among the chemokines tied to the low-grade neuroinflammation increasingly implicated in chronic anxiety."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormonal modulation: estrogen tunes serotonergic and GABAergic tone, and anxiety in women often worsens during the perimenstrual and perimenopausal low-estrogen windows, implicating ovarian hormones in generalised anxiety."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Tachykinin fear circuit: substance P acting on NK1 receptors in the amygdala drives anxiety and the stress response, the rationale behind NK1-antagonist anxiolytics tested for generalised anxiety disorder."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histaminergic arousal: central H1 histamine signalling drives the wakeful arousal that anxiety heightens, which is why the H1 antihistamine hydroxyzine is an established non-addictive anxiolytic for the disorder."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Anxiogenic neuropeptide: CGRP released from the parabrachial nucleus into the amygdala signals threat and heightens anxiety, a neuropeptide arm of the fear circuitry implicated in generalized anxiety and its comorbidity with migraine."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Hyperarousal: orexin signalling that drives wakefulness and stress responses is elevated in anxiety, contributing to the persistent hyperarousal, tension and disturbed sleep that characterise generalized anxiety disorder."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Autonomic anxiety: cholinergic signalling shapes the autonomic and arousal responses of anxiety, and an imbalance between cholinergic and adrenergic tone contributes to the somatic symptoms — restlessness, palpitations — of generalized anxiety disorder."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "HPA dysregulation: chronic worry sustains HPA-axis activation, and altered glucocorticoid-receptor feedback (cortisol and CRH already mapped) underlies the dysregulated stress response of generalized anxiety disorder."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Neuroinflammation balance: the low-grade neuroinflammation of GAD (IL-1β, IL-6 and TNF-α already mapped) is counter-balanced by regulatory IL-10, whose relative deficiency tracks with anxiety severity."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Fear-circuit plasticity: synaptic mTOR-dependent plasticity in the prefrontal-amygdala fear circuitry is implicated in anxiety and in the rapid anxiolytic action of glutamatergic agents."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Neuroinflammatory anxiety: TLR4 innate-immune signalling links peripheral inflammation and psychological stress to the central neuroinflammation increasingly implicated in the pathophysiology of anxiety disorders."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophic plasticity: BDNF acts through its TrkB receptor (NTRK) to drive the hippocampal and prefrontal neuroplasticity whose deficit underlies chronic anxiety and whose restoration accompanies anxiolytic response."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative stress: NRF2-regulated antioxidant defences counter the oxidative stress that accompanies chronic anxiety and sustained HPA-axis overactivation, a link between redox imbalance and mood."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "BDNF/neurotrophin and serotonergic PI3K-AKT-mTOR signalling (mTOR mapped) supports the neuroplasticity that anxiolytic and antidepressant treatment restores in generalized anxiety disorder."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR4-MyD88 innate signalling (TLR4 mapped) drives the low-grade neuroinflammation increasingly linked to the pathophysiology of generalized anxiety disorder."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 reflects the neuroinflammatory activation associated with chronic anxiety and sustained stress."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling in limbic circuits shapes the synaptic plasticity and emotional-regulation balance implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the chronic inflammatory tone associated with the sustained stress of generalized anxiety disorder."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic mitochondrial DNA released during chronic stress can engage cGAS-STING, contributing to the neuroinflammation implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress and resilience relevant to the stress vulnerability of generalized anxiety disorder."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 neuroinflammatory signaling contributes to the inflammatory tone associated with generalized anxiety disorder."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the inflammatory tone linked to the mood and anxiety circuitry of generalized anxiety disorder."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and oxidative-stress adaptation participates in the neurobiology of generalized anxiety disorder."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the low-grade peripheral inflammation associated with generalized anxiety disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the neuronal plasticity of the fear and worry circuits implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the neurometabolic and stress-adaptation responses relevant to generalized anxiety disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal stress resilience and fear-circuit homeostasis implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic (early-life-stress) programming implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the synaptic-plasticity mechanisms of the fear and anxiety circuitry implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with generalized anxiety disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and neuroplasticity processes implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with generalized anxiety disorder."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the microglial and neuroinflammatory processes implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: connects-to
    note: "Somatic symptoms: the palpitations, tremor and tachycardia of anxiety are peripheral beta-adrenergic effects, which is why beta-blockers relieve the somatic manifestations of generalized anxiety even without acting on the core worry."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Brain renin-angiotensin: central angiotensin II modulates the HPA and sympathetic stress response, and angiotensin-receptor blockade is associated with reduced anxiety, a neuroendocrine axis beyond the monoamine and GABA systems already mapped."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Fear circuitry: nitric oxide from neuronal nNOS modulates the amygdala and hippocampal circuits that generate anxiety, implicating NO signalling in the regulation of anxiety-like states."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response and threat appraisal dysregulated in generalized anxiety disorder."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic stress load: chronic anxiety and HPA activation (cortisol already mapped) promote insulin resistance and metabolic dysregulation, part of the cardiometabolic burden that accompanies long-standing generalized anxiety disorder."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex differences: generalized anxiety disorder is roughly twice as common in women, and androgens, which have anxiolytic effects, alongside estrogen and progesterone (already mapped) are implicated in these sex differences in vulnerability."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6, TNF and IL-1 already mapped) reported in anxiety modulate the fear and stress circuits, part of the immune-inflammatory dimension of generalized anxiety disorder."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Cardiometabolic burden: the chronic HPA activation and insulin resistance (insulin already mapped) of long-standing generalized anxiety disorder shift cholesterol handling toward an atherogenic profile, part of its raised cardiovascular risk."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: heightened oxidative stress, to which xanthine oxidase contributes, is reported in anxiety disorders (NRF2 already mapped), and the resulting reactive oxygen species may affect the neurons of the fear and worry circuits."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation reported in generalized anxiety disorder."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is part of the type-2 immune response whose balance against the pro-inflammatory signals shapes the neuroinflammatory dimension of generalized anxiety disorder."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and noradrenaline: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the noradrenergic arousal central to generalized anxiety disorder."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Anxiolytic adipokine: leptin has anxiolytic actions in the amygdala and hippocampus, linking the metabolic (insulin already mapped) state to the anxiety circuits of generalized anxiety disorder."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory (IL-6 already mapped) comorbidity of chronic anxiety."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the neuroinflammation (TNF and IL-1 already mapped) associated with generalized anxiety disorder."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Neuroinflammation: the microglial activation and the neuroinflammation (TNF, IL-6 and IL-1 already mapped) are implicated in the chronic stress and the anxiety of generalized anxiety disorder."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Anxiety-spectrum overlap: generalized anxiety disorder and panic disorder are highly comorbid anxiety disorders, sharing the serotonergic and noradrenergic (already mapped) dysregulation."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Anxiolytic zinc: zinc modulates the glutamate/NMDA (already mapped) signalling and has an anxiolytic role; low zinc is associated with the anxiety of generalized anxiety disorder."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation (IL-1 and TNF already mapped) associated with generalized anxiety disorder."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of generalized anxiety disorder."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with generalized anxiety disorder."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of generalized anxiety disorder."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of generalized anxiety disorder."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic worry and hyperarousal of generalized anxiety disorder."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Stress-modulated NK: the NK-cell number and cytotoxicity, altered by the chronic stress and cortisol (already mapped) reactivity, are part of the peripheral immune dysregulation of generalized anxiety disorder."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the innate inflammatory dimension of the neuroimmune interaction in generalized anxiety disorder."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are part of the low-grade complement activation of the neuroinflammation implicated in generalized anxiety disorder."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the neuroinflammation implicated in generalized anxiety disorder."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the low-grade inflammation of generalized anxiety disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-anxiety axis: TSLP, from gut-epithelium (gut-microbiome already mapped) and mast cells (already mapped), amplifies the neuroinflammatory and the Th2/mast-cell stress axis implicated in the HPA-axis (cortisol already mapped) dysregulation of generalized anxiety disorder."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-autonomic axis: bradykinin, via B2R on CNS neurons (already mapped) and microglia (already mapped), modulates the neuroinflammation and the autonomic hyperarousal contributing to the somatic symptoms of generalized anxiety disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3, C5 and factor-H already mapped) contributing to the neuroinflammation and the complement-mediated synaptic pruning of generalized anxiety disorder."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Stress erythropoiesis: chronic anxiety and HPA-axis (cortisol already mapped) dysregulation can alter erythropoietin signalling; EpoR on neurons (already mapped) also mediates neuroprotective effects relevant to the hippocampal (already mapped) changes of GAD."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Neuroimmune matrix: periostin, from astrocytes (already mapped) and the CNS extracellular matrix, contributes to the glial remodelling and the neuroinflammation (IL-6, TNF, IL-1 already mapped) implicated in the synaptic changes of GAD."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Stress neuroendocrine probe: prolactin reflects serotonergic (already mapped) and dopaminergic tone — challenge tests use its release as a monoamine readout — and its dysregulation under chronic stress links the HPA-serotonin axis to GAD."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "GAD selenium: selenium, as neuroprotective GPx in neurons (already mapped) and microglia (already mapped), scavenges neuroinflammatory (IL-6 and TNF already mapped) ROS; selenium deficiency impairs GABAergic (GABA already mapped) inhibitory tone and exacerbates GAD."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "GAD iodine: iodine-dependent thyroid hormones modulate GABAergic (GABA already mapped) and serotonergic (serotonin already mapped) neurotransmission in neurons (already mapped); iodine deficiency impairs HPA (cortisol already mapped) axis regulation and exacerbates GAD."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "GAD sodium: sodium, via voltage-gated Na⁺ channels on neurons (already mapped) and astrocytes (already mapped), sets the action-potential threshold; sodium channel dysfunction amplifies the glutamate (already mapped) excitatory–GABA (already mapped) inhibitory imbalance of GAD."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "GAD potassium: potassium, via K⁺ channels on neurons (already mapped), sets GABAergic (GABA already mapped) inhibitory potential; potassium dysregulation amplifies the glutamate (already mapped) excitatory imbalance and NLRP3 (already mapped) cascade of GAD."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "GAD phosphorus: phosphorus, as ATP backbone in neurons (already mapped), fuels the Na⁺/K⁺-ATPase maintaining GABA (already mapped) inhibitory tone; phosphorus deficiency impairs neuronal energetics and amplifies the glutamate (already mapped) excitatory cascade of GAD."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "GAD iron: iron, as cofactor of monoamine-oxidase in neurons (already mapped), supports dopamine (already mapped) and serotonin (already mapped) synthesis; iron deficiency amplifies the HPA (cortisol already mapped) and norepinephrine (already mapped) anxiety cascade of GAD."
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
- `connects-to` → **[Thyroid Hormones (T3/T4)](../../03-molecular/thyroid-hormones/README.md)** — Thyroid disease can masquerade as anxiety: an overactive thyroid causes palpitations, tremor, sweating, and restlessness indistinguishable from GAD, so thyroid hormones are checked before settling on a psychiatric diagnosis—a treatable mimic not to miss.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Anxiety and the gut talk constantly in GAD: worry triggers nausea, cramping, and bowel changes, and irritable bowel syndrome frequently coexists, so the gut-brain axis makes digestive symptoms a core, distressing feature of generalized anxiety.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus links stress to anxiety: chronic cortisol in GAD can shrink and impair it, weakening the brake it normally puts on the stress response, so a stress-damaged hippocampus may help lock worry into a self-sustaining loop.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Anxiety can be a thyroid problem in disguise: an overactive thyroid causes palpitations, tremor, restlessness and worry that mimic generalized anxiety, so checking thyroid function is essential before treating—and correcting it can resolve the symptoms.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Caffeine fuels anxiety by blocking adenosine: adenosine normally promotes calm and sleepiness, so caffeine's blockade heightens arousal and can trigger or worsen generalized anxiety—why cutting caffeine is first-line advice.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Generalized anxiety has a neuroinflammatory side in microglia: chronic stress activates brain microglia that release cytokines altering mood circuits, linking the immune system to persistent worry and the overlap of anxiety with inflammatory illness.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Generalized anxiety keeps the adrenal glands switched on: chronic worry drives the HPA axis to make the adrenals pour out cortisol, and this sustained stress-hormone output underlies the fatigue, tension and health toll of long-term anxiety.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Low magnesium can heighten anxiety: the mineral normally restrains the NMDA receptor and supports GABA, so deficiency tips the brain toward excitation, which is why magnesium status is studied in relation to anxiety symptoms.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The endocannabinoid system helps set the brain's anxiety thermostat: it dampens stress circuits and fear responses, so when this tone falls anxiety rises, making the system a target behind why cannabis can both calm and worsen worry.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Anxiety is tuned at the synapse: the balance of excitatory glutamate and inhibitory GABA across amygdala and prefrontal synapses sets how strongly threat signals fire, and shifting that synaptic balance toward excitation drives chronic worry.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Anxiety speaks through the gut: the gut-brain axis ties worry to the large intestine, so anxiety triggers cramping and changed bowel habits, and a troubled gut signals back to heighten anxiety—the loop behind anxiety's overlap with IBS.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Generalized anxiety reflects over-firing neurons: hyperexcitable cells in the amygdala and worry circuits respond too readily to threat while calming inputs lag, the cellular imbalance that medications and therapy work to settle.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Anxiety shows on fMRI: photons map an overactive amygdala and weak prefrontal control, the brain pattern of an exaggerated threat response that underlies generalized anxiety.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes tune the anxiety circuit's glutamate, and their dysfunction is implicated in the over-excitable fear networks of generalized anxiety, extending the disorder beyond neurons alone.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Anxiety quickens the breath: hyperventilation and air hunger are core physical symptoms, and the low CO2 that results causes the tingling and lightheadedness of an anxiety attack.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc helps keep anxiety in check: it modulates the GABA and glutamate balance of the calming circuits, and low zinc is reported in anxiety disorders, with supplementation studied as an adjunct to standard treatment.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Anxiety churns the stomach: the gut-brain axis turns worry into nausea, 'butterflies,' and functional dyspepsia, so abdominal distress is one of the most common bodily complaints of generalized anxiety.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D shadows the anxious mind: deficiency is associated with higher anxiety, and the vitamin's receptors throughout mood-regulating brain regions suggest it helps tune the circuits that worry overactivates.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Worry steals sleep through the clock: GAD's racing mind delays sleep onset and blunts melatonin, and the resulting insomnia loops back to sharpen the next day's anxiety — a cycle melatonin and sleep hygiene aim to break.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Anxiety shows on the skin: the autonomic surge brings sweating, flushing, and goosebumps, and chronic stress flares skin conditions like eczema and hives through the brain-skin axis.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Sex hormones color the worry: GAD is about twice as common in women, and anxiety often intensifies premenstrually, in the postpartum, and around menopause as estrogen and progesterone swing.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Chronic worry leaves an inflammatory trace: GAD is associated with raised IL-6 and other inflammatory markers, fitting a model in which sustained stress-axis activation primes low-grade inflammation that acts back on the anxious brain.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The body's smooth muscle carries the tension: chronic anxiety clenches gut and airway smooth muscle into the cramping, bloating, and chest tightness of GAD's somatic symptoms, the physical face of relentless worry.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Sustained anxiety hardens the arteries: the chronic sympathetic and cortisol drive of GAD raises blood pressure and inflammation that accelerate atherosclerosis, contributing to its long-term cardiovascular risk.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Chronic worry erodes neuroplasticity: GAD is marked by lower BDNF, weakening the synaptic remodeling that lets the brain adapt, and treatments that raise BDNF parallel recovery from anxiety.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Stress reaches the mast cell: brain and gut mast cells carry receptors for the stress peptide CRH, releasing mediators that may link anxiety to its headaches, flushing, and the visceral hypersensitivity of an anxious gut.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Worry leaves a metabolic mark: the chronic cortisol of GAD promotes insulin resistance and central fat, and anxiety and type 2 diabetes each raise the risk of the other in a two-way link.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Chronic stress inflames the brain: NLRP3 inflammasome activation in microglia releases IL-1β that disturbs the mood and fear circuits, part of the neuroinflammation increasingly tied to anxiety disorders.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — A calming hormone opposes the worry: oxytocin dampens amygdala fear responses and buffers stress, the anxiolytic, social-bonding signal whose deficiency may leave the threat circuits of GAD unchecked.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Sustained alarm raises the pressure: the chronic sympathetic and cortisol drive of GAD keeps blood pressure elevated, one route by which long-term anxiety translates into cardiovascular disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic worry leaves an inflammatory mark: persistent stress in GAD activates NF-κB-driven cytokine signaling, the neuroinflammatory thread linking anxiety to its raised cardiovascular and metabolic risk.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is a disorder of the brain's threat circuitry: GAD reflects an overactive amygdala-driven fear network with weak prefrontal restraint, dysregulation of the nervous system's normal worry-and-safety balance.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — People reach for cannabis to quiet the worry: GAD frequently co-occurs with cannabis use disorder, as users self-medicate anxiety even though heavy use and withdrawal can ultimately worsen it.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Chronic worry strains the heart: the sustained sympathetic activation of GAD raises heart rate and blood pressure and is associated with worse cardiac outcomes, contributing over time to heart failure risk.
- `connects-to` → **[Stroke](../stroke/README.md)** — Anxiety tracks with cerebrovascular risk: the chronic stress, hypertension and inflammation of long-standing GAD are linked epidemiologically to a higher long-term risk of stroke.
- `connects-to` → **[Obesity](../obesity/README.md)** — Stress reshapes appetite and activity: cortisol-driven cravings, comfort eating and reduced activity in GAD, compounded by some anxiolytic medications, contribute to weight gain and obesity.
- `connects-to` → **[COPD](../copd/README.md)** — Breathlessness and anxiety amplify each other: GAD is highly comorbid with COPD, where air hunger triggers panic and chronic worry, and anxiety in turn worsens dyspnea and disability.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Chronic worry may wear on the aging brain: sustained cortisol elevation and the long-term sedatives used for GAD are associated with an increased risk of later cognitive decline and dementia.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Stress hormones and sedative falls cost bone: chronic cortisol elevation in GAD lowers bone density, while the benzodiazepines often used raise fall and fracture risk on already fragile bone.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones both mimic and drive it: thyrotoxicosis, phaeochromocytoma and cortisol dysregulation produce anxiety identical to GAD, and chronic worry itself dysregulates the HPA stress axis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Chronic worry presses on the heart: GAD causes palpitations and sustained sympathetic arousal, and is independently associated with raised blood pressure and cardiovascular events including takotsubo cardiomyopathy.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — They frequently travel together: anxiety disorders are highly comorbid with ADHD, where inattention and the strain of coping fuel worry, and stimulant treatment can itself heighten anxiety.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Worry lives in the muscles: persistent muscle tension, aches and tension headaches are core somatic features of generalized anxiety disorder, often the symptoms that bring people to the doctor.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Chronic worry unsettles immunity: sustained anxiety dysregulates cortisol and raises inflammatory markers, blunting immune function over time.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Anxiety surfaces on the skin: stress aggravates eczema, psoriasis and itch and drives sweating, and skin-picking or hair-pulling behaviours can accompany chronic anxiety.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Breathing carries the symptoms: anxiety drives hyperventilation, breathlessness and chest tightness, and a vicious circle ties it tightly to asthma and breathing disorders.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — First-line treatment is an antidepressant: SSRIs like fluoxetine are the mainstay for generalized anxiety disorder, preferred over benzodiazepines for long-term control.
- `connects-to` → **[Dietary Magnesium](../../../03-medicine/03-food/magnesium-dietary/README.md)** — Diet draws interest: low magnesium status has been linked to anxiety and supplementation trialled as an adjunct, though the evidence remains modest.
- `connects-to` → **[Ashwagandha](../../../03-medicine/02-traditional/ashwagandha/README.md)** — A traditional anxiolytic with evidence: ashwagandha, an adaptogenic herb, reduces anxiety and cortisol in trials and is among the better-supported complementary treatments for generalized anxiety.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet offers a modest adjunct: omega-3 supplementation shows small anxiolytic effects in some trials, used alongside but not instead of first-line therapy for generalized anxiety.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — The gut and worry feed each other: anxiety is far more common in inflammatory bowel disease, and through the gut-brain axis disease flares and chronic worry each worsen the other.
- `connects-to` → **[Beta-blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — They blunt the body's anxiety: beta-blockers like propranolol damp the adrenergic physical symptoms of anxiety — racing heart, tremor, sweating — useful for performance and situational anxiety though they do not treat the underlying worry.
- `connects-to` → **[St John's Wort](../../../03-medicine/02-traditional/st-johns-wort/README.md)** — A herbal serotonergic option: St John's wort, which raises serotonin like the SSRIs used for anxiety, is taken by some for mild anxiety and depression, though efficacy is uncertain and it interacts with many drugs.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — Chronic anxiety amid instability: generalized anxiety is a frequent comorbidity of borderline personality disorder, sharing emotional dysregulation and an exaggerated threat response that compound each other.
- `connects-to` → **[NPY](../../03-molecular/npy/README.md)** — The brain's anti-anxiety neuropeptide: NPY buffers the stress response and amygdala reactivity, and low NPY tone tracks with anxiety vulnerability and poor resilience—an endogenous counterweight to the CRH-driven stress underlying GAD.
- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — Anxiety and compulsive reward feed each other: people with GAD may gamble to escape anxious distress, and mounting losses deepen worry—a bidirectional loop between anxiety and behavioural addiction.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Why anxiety feels like the heart: GAD's autonomic arousal drives palpitations, sinus tachycardia and ectopy through the conduction system, the somatic symptom that brings many anxious patients to cardiology and the rationale for beta-blockade.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — The commonest psychiatric comorbidity of seizures: anxiety is the most frequent psychiatric companion of epilepsy, bidirectionally linked through shared GABAergic dysfunction and the stress of unpredictable seizures.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Anxiety amplifies pain: generalized anxiety disorder commonly coexists with chronic and neuropathic pain, each worsening the other through shared serotonergic-noradrenergic pathways that SNRIs like duloxetine target in both.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A pandemic of anxiety: COVID-19 sharply raised rates of generalized anxiety through health fears, isolation and bereavement, and post-COVID neuroinflammation may directly worsen anxiety symptoms.
- `connects-to` → **[Pheochromocytoma & Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — The organic anxiety mimic: a catecholamine-secreting phaeochromocytoma causes paroxysmal anxiety, palpitations and sweating that imitate generalized anxiety, a can't-miss endocrine cause to exclude in atypical cases.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The gut-brain axis: generalized anxiety overlaps heavily with irritable bowel syndrome, with the intestinal epithelium and microbiome signalling to anxiety circuits via the vagus and immune pathways.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Anxiety and the heart muscle: chronic anxiety raises cardiovascular risk, and acute extreme stress can precipitate Takotsubo (stress) cardiomyopathy, transiently stunning the myocardium.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory anxiety: IL-1β from activated microglia is implicated in the neuroinflammation increasingly linked to anxiety, with chronic stress raising this innate cytokine.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Stress cytokine: elevated TNF-α is among the inflammatory markers found in generalised anxiety, part of the bidirectional link between chronic stress and systemic inflammation.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Threat and reward: dopaminergic signalling shapes the uncertainty and threat appraisal that drive anxiety, and its dysregulation contributes to the avoidance and anticipatory worry of GAD.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Neurosteroid anxiolysis: the progesterone metabolite allopregnanolone is a positive GABA-A modulator, so its fluctuations shape anxiety and underlie the neurosteroid drugs developed for anxiety and depression.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Stress-axis amplifier: vasopressin synergises with CRH to drive the HPA-axis hyperactivity of generalised anxiety, sustaining the heightened stress reactivity central to the disorder.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Neuroinflammatory link: CCL2 recruits monocytes to the brain and is among the chemokines tied to the low-grade neuroinflammation increasingly implicated in chronic anxiety.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen tunes serotonergic and GABAergic tone, and anxiety in women often worsens during the perimenstrual and perimenopausal low-estrogen windows, implicating ovarian hormones in the course of generalized anxiety disorder.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Substance P acting on NK1 receptors in the amygdala drives anxiety and the stress response, the rationale behind the NK1-antagonist anxiolytics tested (with mixed results) for generalized anxiety disorder.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Central H1 histamine signaling drives the wakeful arousal that anxiety heightens, which is why the H1 antihistamine hydroxyzine is an established non-addictive anxiolytic option for generalized anxiety disorder.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — CGRP released from the parabrachial nucleus into the amygdala signals threat and heightens anxiety, a neuropeptide arm of the fear circuitry implicated in generalized anxiety and its comorbidity with migraine.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Orexin signaling that drives wakefulness and stress responses is elevated in anxiety, contributing to the persistent hyperarousal, tension and disturbed sleep that characterize generalized anxiety disorder.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Cholinergic signaling shapes the autonomic and arousal responses of anxiety, and an imbalance between cholinergic and adrenergic tone contributes to the somatic symptoms—restlessness, palpitations—of generalized anxiety disorder.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Chronic worry sustains HPA-axis activation, and altered glucocorticoid-receptor feedback (cortisol and CRH already mapped) underlies the dysregulated stress response of generalized anxiety disorder.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — The low-grade neuroinflammation of GAD (IL-1β, IL-6 and TNF-α already mapped) is counter-balanced by regulatory IL-10, whose relative deficiency tracks with anxiety severity.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Synaptic mTOR-dependent plasticity in the prefrontal-amygdala fear circuitry is implicated in anxiety and in the rapid anxiolytic action of glutamatergic agents.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 innate-immune signaling links peripheral inflammation and psychological stress to the central neuroinflammation increasingly implicated in the pathophysiology of anxiety disorders.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF acts through its TrkB receptor (NTRK) to drive the hippocampal and prefrontal neuroplasticity whose deficit underlies chronic anxiety and whose restoration accompanies anxiolytic response.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2-regulated antioxidant defenses counter the oxidative stress that accompanies chronic anxiety and sustained HPA-axis overactivation, a link between redox imbalance and mood.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — BDNF/neurotrophin and serotonergic PI3K-AKT-mTOR signaling (mTOR mapped) supports the neuroplasticity that anxiolytic and antidepressant treatment restores in generalized anxiety disorder.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4-MyD88 innate signaling (TLR4 mapped) drives the low-grade neuroinflammation increasingly linked to the pathophysiology of generalized anxiety disorder.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 reflects the neuroinflammatory activation associated with chronic anxiety and sustained stress.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling in limbic circuits shapes the synaptic plasticity and emotional-regulation balance implicated in generalized anxiety disorder.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the chronic inflammatory tone associated with the sustained stress of generalized anxiety disorder.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic mitochondrial DNA released during chronic stress can engage cGAS-STING, contributing to the neuroinflammation implicated in generalized anxiety disorder.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress and resilience relevant to the stress vulnerability of generalized anxiety disorder.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 neuroinflammatory signaling contributes to the inflammatory tone associated with generalized anxiety disorder.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the inflammatory tone linked to the mood and anxiety circuitry of generalized anxiety disorder.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and oxidative-stress adaptation participates in the neurobiology of generalized anxiety disorder.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the low-grade peripheral inflammation associated with generalized anxiety disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the neuronal plasticity of the fear and worry circuits implicated in generalized anxiety disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the neurometabolic and stress-adaptation responses relevant to generalized anxiety disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal stress resilience and fear-circuit homeostasis implicated in generalized anxiety disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic (early-life-stress) programming implicated in generalized anxiety disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the synaptic-plasticity mechanisms of the fear and anxiety circuitry implicated in generalized anxiety disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with generalized anxiety disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and neuroplasticity processes implicated in generalized anxiety disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in generalized anxiety disorder.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with generalized anxiety disorder.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the microglial and neuroinflammatory processes implicated in generalized anxiety disorder.
- `connects-to` → **[Beta-1 adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — Somatic symptoms: the palpitations, tremor and tachycardia of anxiety are peripheral beta-adrenergic effects, which is why beta-blockers relieve the somatic manifestations of generalized anxiety even without acting on the core worry.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Brain renin-angiotensin: central angiotensin II modulates the HPA and sympathetic stress response, and angiotensin-receptor blockade is associated with reduced anxiety, a neuroendocrine axis beyond the monoamine and GABA systems already mapped.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Fear circuitry: nitric oxide from neuronal nNOS modulates the amygdala and hippocampal circuits that generate anxiety, implicating NO signalling in the regulation of anxiety-like states.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response and threat appraisal dysregulated in generalized anxiety disorder.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic stress load: chronic anxiety and HPA activation (cortisol already mapped) promote insulin resistance and metabolic dysregulation, part of the cardiometabolic burden that accompanies long-standing generalized anxiety disorder.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex differences: generalized anxiety disorder is roughly twice as common in women, and androgens, which have anxiolytic effects, alongside estrogen and progesterone (already mapped) are implicated in these sex differences in vulnerability.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6, TNF and IL-1 already mapped) reported in anxiety modulate the fear and stress circuits, part of the immune-inflammatory dimension of generalized anxiety disorder.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cardiometabolic burden: the chronic HPA activation and insulin resistance (insulin already mapped) of long-standing generalized anxiety disorder shift cholesterol handling toward an atherogenic profile, part of its raised cardiovascular risk.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: heightened oxidative stress, to which xanthine oxidase contributes, is reported in anxiety disorders (NRF2 already mapped), and the resulting reactive oxygen species may affect the neurons of the fear and worry circuits.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation reported in generalized anxiety disorder.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is part of the type-2 immune response whose balance against the pro-inflammatory signals shapes the neuroinflammatory dimension of generalized anxiety disorder.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and noradrenaline: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the noradrenergic arousal central to generalized anxiety disorder.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Anxiolytic adipokine: leptin has anxiolytic actions in the amygdala and hippocampus, linking the metabolic (insulin already mapped) state to the anxiety circuits of generalized anxiety disorder.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory (IL-6 already mapped) comorbidity of chronic anxiety.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the neuroinflammation (TNF and IL-1 already mapped) associated with generalized anxiety disorder.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Neuroinflammation: the microglial activation and the neuroinflammation (TNF, IL-6 and IL-1 already mapped) are implicated in the chronic stress and the anxiety of generalized anxiety disorder.
- `connects-to` → **[Panic disorder](../panic-disorder/README.md)** — Anxiety-spectrum overlap: generalized anxiety disorder and panic disorder are highly comorbid anxiety disorders, sharing the serotonergic and noradrenergic (already mapped) dysregulation.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Anxiolytic zinc: zinc modulates the glutamate/NMDA (already mapped) signalling and has an anxiolytic role; low zinc is associated with the anxiety of generalized anxiety disorder.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in generalized anxiety disorder.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation (IL-1 and TNF already mapped) associated with generalized anxiety disorder.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of generalized anxiety disorder.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with generalized anxiety disorder.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of generalized anxiety disorder.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of generalized anxiety disorder.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic worry and hyperarousal of generalized anxiety disorder.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Stress-modulated NK: the NK-cell number and cytotoxicity, altered by the chronic stress and cortisol (already mapped) reactivity, are part of the peripheral immune dysregulation of generalized anxiety disorder.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the innate inflammatory dimension of the neuroimmune interaction in generalized anxiety disorder.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are part of the low-grade complement activation of the neuroinflammation implicated in generalized anxiety disorder.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the neuroinflammation implicated in generalized anxiety disorder.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the low-grade inflammation of generalized anxiety disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-anxiety axis: TSLP, from gut-epithelium (gut-microbiome already mapped) and mast cells (already mapped), amplifies the neuroinflammatory and the Th2/mast-cell stress axis implicated in the HPA-axis (cortisol already mapped) dysregulation of generalized anxiety disorder.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-autonomic axis: bradykinin, via B2R on CNS neurons (already mapped) and microglia (already mapped), modulates the neuroinflammation and the autonomic hyperarousal contributing to the somatic symptoms of generalized anxiety disorder.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3, C5 and factor-H already mapped) contributing to the neuroinflammation and the complement-mediated synaptic pruning of generalized anxiety disorder.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Stress erythropoiesis: chronic anxiety and HPA-axis (cortisol already mapped) dysregulation can alter erythropoietin signalling; EpoR on neurons (already mapped) also mediates neuroprotective effects relevant to the hippocampal (already mapped) changes of GAD.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Neuroimmune matrix: periostin, from astrocytes (already mapped) and the CNS extracellular matrix, contributes to the glial remodelling and the neuroinflammation (IL-6, TNF, IL-1 already mapped) implicated in the synaptic changes of GAD.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Stress neuroendocrine probe: prolactin reflects serotonergic (already mapped) and dopaminergic tone — challenge tests use its release as a monoamine readout — and its dysregulation under chronic stress links the HPA-serotonin axis to GAD.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Neuroprotective antioxidant: selenium, as neuroprotective GPx in neurons (already mapped) and microglia (already mapped), scavenges neuroinflammatory (IL-6 and TNF already mapped) ROS; selenium deficiency impairs GABAergic (GABA already mapped) inhibitory tone and exacerbates GAD.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-neuroendocrine axis: iodine-dependent thyroid hormones modulate GABAergic (GABA already mapped) and serotonergic (serotonin already mapped) neurotransmission in neurons (already mapped); iodine deficiency impairs HPA (cortisol already mapped) axis regulation and exacerbates GAD.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Neuronal excitability: sodium, via voltage-gated Na⁺ channels on neurons (already mapped) and astrocytes (already mapped), sets the action-potential threshold; sodium channel dysfunction amplifies the glutamate (already mapped) excitatory–GABA (already mapped) inhibitory imbalance of GAD.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — GABAergic inhibitory tone: potassium, via K⁺ channels on neurons (already mapped), sets GABAergic (GABA already mapped) inhibitory potential; potassium dysregulation amplifies the glutamate (already mapped) excitatory imbalance and NLRP3 (already mapped) cascade of GAD.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Neuronal ATP energetics: phosphorus, as ATP backbone in neurons (already mapped), fuels the Na⁺/K⁺-ATPase maintaining GABA (already mapped) inhibitory tone; phosphorus deficiency impairs neuronal energetics and amplifies the glutamate (already mapped) excitatory cascade of GAD.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Monoamine synthesis cofactor: iron, as cofactor of monoamine-oxidase in neurons (already mapped), supports dopamine (already mapped) and serotonin (already mapped) synthesis; iron deficiency amplifies the HPA (cortisol already mapped) and norepinephrine (already mapped) anxiety cascade of GAD.

[^kessler-2005-gad-prevalence]: Kessler RC, Berglund P, Demler O, et al. Lifetime prevalence and age-of-onset distributions of DSM-IV disorders in the NCS Replication. *Arch Gen Psychiatry.* 2005;62(6):593-602. [doi:10.1001/archpsyc.62.6.593](https://doi.org/10.1001/archpsyc.62.6.593) · [PubMed 15939837](https://pubmed.ncbi.nlm.nih.gov/15939837/)
[^bandelow-2015-anxiety-biology]: Bandelow B, Michaelis S. Epidemiology of anxiety disorders in the 21st century. *Dialogues Clin Neurosci.* 2015;17(3):327-335. [doi:10.31887/DCNS.2015.17.3/bbandelow](https://doi.org/10.31887/DCNS.2015.17.3/bbandelow) · [PubMed 26487812](https://pubmed.ncbi.nlm.nih.gov/26487812/)
[^baldwin-2014-gad-treatment]: Baldwin DS, Anderson IM, Nutt DJ, et al. Evidence-based pharmacological treatment of anxiety disorders. *J Psychopharmacol.* 2014;28(5):403-439. [doi:10.1177/0269881114525674](https://doi.org/10.1177/0269881114525674) · [PubMed 24713617](https://pubmed.ncbi.nlm.nih.gov/24713617/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
