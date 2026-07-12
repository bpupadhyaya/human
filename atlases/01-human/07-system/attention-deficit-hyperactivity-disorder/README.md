---
schema: human-scale-entry/v1
id: attention-deficit-hyperactivity-disorder
name: Attention-Deficit/Hyperactivity Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "ADHD (5-10% prevalence; 4:1 male:female) is driven by prefrontal cortex dopamine/norepinephrine deficiency impairing executive function; stimulants (methylphenidate, amphetamines) are first-line; 60-70% of childhood ADHD persists into adulthood."
aliases: ["ADHD", "attention deficit hyperactivity disorder", "ADD", "attention deficit disorder", "hyperactivity disorder", "ADHD inattentive type", "ADHD combined type"]
sources:
  - id: faraone-2021-adhd-primer
    type: peer-reviewed
    cite: "Faraone SV, Banaschewski T, Coghill D, et al. The World Federation of ADHD International Consensus Statement: 208 Evidence-based conclusions about the disorder. Neurosci Biobehav Rev. 2021;128:789-818."
    doi: "10.1016/j.neubiorev.2021.01.022"
    pmid: "33549739"
    url: "https://doi.org/10.1016/j.neubiorev.2021.01.022"
    accessed: "2026-06-08"
  - id: arnsten-2009-adhd-neuroscience
    type: peer-reviewed
    cite: "Arnsten AF. Toward a new understanding of attention-deficit hyperactivity disorder pathophysiology: an important role for prefrontal cortex dysfunction. CNS Drugs. 2009;23(Suppl 1):33-41."
    doi: "10.2165/00023210-200923000-00005"
    pmid: "19621976"
    url: "https://doi.org/10.2165/00023210-200923000-00005"
    accessed: "2026-06-08"
  - id: biederman-2005-adhd-adults
    type: peer-reviewed
    cite: "Biederman J, Faraone SV. Attention-deficit hyperactivity disorder. Lancet. 2005;366(9481):237-248."
    doi: "10.1016/S0140-6736(05)66915-2"
    pmid: "16023516"
    url: "https://doi.org/10.1016/S0140-6736(05)66915-2"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "ADHD involves hypofunctional PFC dopamine D1 receptor signaling impairing working memory and executive control; methylphenidate and amphetamines increase synaptic dopamine/NE; COMT Val158Met SNP (rapid dopamine catabolism) increases ADHD risk and alters stimulant response."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "NE α2A-receptor signaling in PFC strengthens layer III pyramidal neuron connectivity underlying working memory; atomoxetine (selective NE reuptake inhibitor) and guanfacine/clonidine (α2A agonists) treat ADHD by restoring NE-PFC function without dopamine-reward effects."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "ADHD involves PFC, anterior cingulate cortex, striatum, and cerebellum circuit dysfunction; MRI shows ~3% smaller total brain volume; PFC gray matter thinning delays 2-5 years relative to controls; default mode network fails to deactivate during tasks → attention lapses."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF Val66Met SNP is over-represented in ADHD; BDNF supports PFC dopaminergic circuit maturation; stimulant treatment increases BDNF expression in PFC; exercise (which raises BDNF) reduces ADHD symptom severity in children and improves executive function outcomes."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "PFC layer III pyramidal neurons are the core ADHD substrate; they express DA D1 and NE α2A receptors maintaining persistent firing for working memory; D1 → cAMP → HCN/K⁺ channel closure → strengthened circuit; catecholamine deficiency → HCN open → signal noise → inattention."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "ADHD and ASD co-occur in 20-50% of cases; DSM-5 (2013) allows dual diagnosis; both share genetic architecture (CNVs at 16p13.11, 1q21.1; FOXP2, SHANK3) and PFC-striatal circuit dysfunction; methylphenidate has lower efficacy and more side effects in ASD+ADHD vs ADHD alone."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Hippocampus is ~3-4% smaller in ADHD (meta-analysis); working memory deficits partly reflect hippocampal-PFC circuit dysfunction; stimulants normalize hippocampal-PFC connectivity on fMRI; episodic memory impairment is an underrecognized domain affecting academic performance."
  - target: 01-human/07-system/bulimia-nervosa
    relation: connects-to
    note: "ADHD and bulimia nervosa are linked by impulsivity and reward dysregulation: childhood ADHD roughly doubles later bulimia risk, with shared deficits in prefrontal inhibitory control and dopaminergic reward driving both loss-of-control eating and impulsive behavior."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "ADHD and stimulant use disorder share a dopaminergic core: untreated ADHD raises later substance-use risk, yet properly prescribed stimulants lower it; still, the same drugs carry misuse and diversion potential, so prescribing balances benefit against addiction risk."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "ADHD and bipolar disorder overlap and are easily confused: both feature distractibility, impulsivity, and high energy, but ADHD is chronic and trait-like while bipolar elevation is episodic; they co-occur, and stimulants are used cautiously in bipolar ADHD to avoid mania."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "ADHD strongly predisposes to gambling disorder: deficient dopaminergic reward processing and impaired impulse control drive risky, poorly-checked betting, the two are highly comorbid, and gambling severity tracks ADHD symptom load—so impulsivity is a shared treatment target."
  - target: 01-human/07-system/internet-gaming-disorder
    relation: connects-to
    note: "ADHD is one of the strongest correlates of internet gaming disorder: deficits in dopaminergic reward and inhibition predispose to compulsive gaming, the two are highly comorbid bidirectionally, and IGD severity tracks ADHD symptom load—stimulant treatment can reduce gaming."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "ADHD is strongly linked to binge eating disorder: deficient dopaminergic reward and impulse control predispose to impulsive overeating, the two are highly comorbid, and lisdexamfetamine—an ADHD stimulant—is the only FDA-approved BED drug, dampening the reward salience of food."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "ADHD and depression frequently co-occur and can be hard to separate: untreated ADHD's chronic underachievement and rejection feed depression, the disorders share dopaminergic and executive-function deficits, and stimulant plus antidepressant strategies are often combined."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety disorders are among the commonest ADHD comorbidities: the strain of inattention and disorganization breeds chronic worry, and the two can mask each other—stimulants may worsen anxiety while untreated ADHD fuels it—so treatment must balance both."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "ADHD substantially raises the risk of alcohol and other substance use disorders: impulsivity and reward dysregulation drive earlier, heavier use, and self-medication is common—so treating ADHD can lower, not raise, the long-term addiction risk."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "ADHD and insomnia are deeply linked: delayed sleep phase, bedtime restlessness and racing thoughts are common in ADHD, and stimulant treatment can worsen sleep onset—while the resulting sleep loss mimics and amplifies inattention, blurring cause and effect."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "ADHD raises the risk of cannabis use disorder: impulsivity and self-medication for restlessness drive earlier, heavier use, yet cannabis worsens attention and motivation—so the disorder and the drug reinforce each other, complicating diagnosis and treatment."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate signaling is implicated in ADHD beyond dopamine: imbalances in glutamate—the brain's main excitatory transmitter—affect the prefrontal circuits governing attention and impulse control, and are a target of interest for non-stimulant ADHD therapies."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Beyond dopamine and norepinephrine, serotonin modulates ADHD: serotonergic tone influences the impulsivity and emotional dysregulation of the disorder, and serotonin-acting drugs are used for comorbid mood and anxiety symptoms common in ADHD."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "ADHD is a neurodevelopmental disorder of the nervous system's executive networks: delayed maturation and altered connectivity in prefrontal-striatal circuits impair attention and impulse control, so it reflects how the brain regulates behavior, not a lack of effort."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Iron deficiency is linked to ADHD symptoms: iron is a cofactor for dopamine synthesis, and low ferritin is associated with worse inattention and restless sleep, so checking and correcting iron can be part of evaluating a child with ADHD."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "ADHD commonly comes with disrupted sleep: delayed melatonin release shifts the body clock later, causing trouble falling asleep that worsens daytime inattention, so melatonin and sleep treatment are part of comprehensive ADHD care."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "ADHD risk is partly set before birth via the placenta: maternal smoking, alcohol, stress, and placental insufficiency that limit fetal brain growth raise the child's ADHD risk—so prenatal environment shapes this neurodevelopmental disorder."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "ADHD and OCD share frontostriatal circuitry yet pull oppositely: ADHD is impulsive and under-controlled while OCD is over-controlled, so they can co-occur and complicate each other—and stimulants for ADHD may aggravate obsessions."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "ADHD reaches beyond neurons to astrocytes: these glial cells help clear and recycle dopamine and glutamate at synapses, so astrocyte dysfunction can blunt the prefrontal signaling that stimulant medications work to restore."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "ADHD and epilepsy travel together: children with epilepsy have far higher ADHD rates and vice versa, sharing disrupted attention networks—and stimulant treatment is generally safe and helpful rather than seizure-provoking in well-controlled epilepsy."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "ADHD predisposes to obesity: impulsivity and dopamine-driven reward seeking promote dysregulated, binge-style eating, so untreated attention-deficit symptoms are a risk factor for weight gain and disordered eating."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron is the quiet partner of dopamine in ADHD: it is a cofactor for the enzyme that makes dopamine, so low iron stores (even without anemia) are linked to worse symptoms, and supplementation is studied in deficient children."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "ADHD is a disorder of the dopamine synapse: signaling across reward and attention synapses is dysregulated, and stimulant medicines work by raising dopamine and norepinephrine in this synaptic gap to sharpen focus."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia may shape the ADHD brain: prenatal inflammation and microglial pruning of synapses influence the development of attention circuits, an emerging neuroimmune angle on why early-life stress raises ADHD risk."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "ADHD is linked to low zinc: the mineral helps regulate dopamine signaling, so deficiency is associated with more severe symptoms, and zinc status is studied as a modifier of the disorder and its treatment."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid shapes attention: its hormones guide brain development and arousal, so thyroid dysfunction can produce inattention and hyperactivity that mimic ADHD, which is why thyroid problems are screened for."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "ADHD treatment must watch the heart: the stimulant medicines that sharpen focus also raise heart rate and blood pressure, so cardiac history and monitoring guide their safe use."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Brain imaging shows ADHD's delayed wiring: MRI photons reveal slower cortical maturation and altered connectivity, and fMRI maps underactivity in the attention and reward networks."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "ADHD involves delayed white matter: the oligodendrocytes that myelinate the connections between attention regions mature slowly, slowing the brain's information highways."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut may sway ADHD: emerging work ties the intestinal microbiome to attention and behavior through the gut-brain axis, hinting the bowel's microbes influence symptoms."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium runs low in many with ADHD: the mineral supports the neurotransmitter balance behind focus and calm, and deficiency is associated with worse symptoms, making it a studied nutritional adjunct."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D in early life may shape ADHD risk: low maternal and childhood levels are linked to higher rates of the disorder, fitting the vitamin's role in the developing brain."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "ADHD and the itchy skin travel together: it is notably comorbid with atopic dermatitis, the sleep-wrecking itch and shared inflammatory and neurodevelopmental threads linking the gut, skin, and attention."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The stimulant treatments curb the appetite: methylphenidate and amphetamines blunt hunger and can cause nausea and stomach upset, so children's intake and weight are watched closely during therapy."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Stimulants can nudge growth off course: by suppressing appetite they may modestly slow height and weight gain in children, prompting drug holidays and growth monitoring during long-term treatment."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Estrogen tunes the ADHD brain: because the hormone modulates dopamine, many women find symptoms swing across the menstrual cycle and worsen as estrogen falls in the perimenopause, shaping how treatment is timed."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "The stimulant medicines lean on the heart: methylphenidate and amphetamines modestly raise heart rate and blood pressure, so cardiovascular history is screened before starting and the vitals are monitored during treatment."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The endocannabinoid system touches attention and reward: it modulates the dopamine circuits implicated in ADHD, part of why cannabis is commonly used — and misused — by those with the disorder seeking relief."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Low iron shows in the red cells and the focus: iron-deficiency, with its small, pale erythrocytes and low ferritin, is more common in ADHD and worsens symptoms, so iron status is checked and repleted as an adjunct."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Attention needs the brain's brakes too: reduced GABAergic inhibition tips the excitation-inhibition balance in ADHD, contributing to the impulsivity and distractibility that stimulant and other therapies try to rein in."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut may shape attention: altered microbiome composition is reported in ADHD, and through the microbiome-gut-brain axis it can influence the dopamine and stress signaling tied to the disorder."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Sleepiness and inattention overlap: ADHD and narcolepsy frequently co-occur and share a hypoarousal that both respond to stimulants, so daytime sleepiness in ADHD prompts a look for an underlying sleep disorder."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid imbalance mimics ADHD: both hyper- and hypothyroidism produce inattention, restlessness, or sluggishness, and rare resistance to thyroid hormone is strongly linked to ADHD — so thyroid function is checked when the picture is atypical."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The stress axis runs differently in ADHD: a blunted or dysregulated adrenal cortisol response is reported, part of the altered arousal regulation that underlies the disorder and its links to stress and sleep."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Attention and headache travel together: ADHD and migraine are comorbid more than chance, sharing dopaminergic and arousal dysregulation, so each is more common in people who have the other."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "An inflammatory thread runs through it: emerging evidence links ADHD to low-grade neuroinflammation with NF-κB-driven cytokine signaling, part of why maternal immune activation and inflammation raise the risk."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Impulsivity raises the stakes of every drug: untreated ADHD strongly predisposes to substance use disorders including opioids, the impulsivity and reward dysregulation driving earlier, heavier use and addiction."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "Impulsivity and emotional dysregulation overlap: ADHD and borderline personality disorder co-occur often and share traits of impulsivity and affective instability, blurring the line between the two."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Impulsive eating and obesity raise the metabolic stakes: ADHD's impulsivity and reward dysregulation drive disordered eating and obesity, translating over time into a higher risk of type 2 diabetes."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Years of social missteps breed fear: the inattention and impulsivity of ADHD cause repeated social difficulties that can foster social anxiety, a common comorbidity that compounds functional impairment."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Its stimulant treatment nudges up the pressure: the methylphenidate and amphetamine medications for ADHD raise heart rate and blood pressure, so cardiovascular monitoring is part of long-term treatment."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Impulsivity and inattention court injury: ADHD carries markedly higher rates of accidents, falls and burns, producing wounds and fractures more often than in the general population."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "It travels with atopic and respiratory disease: ADHD is comorbid with asthma at elevated rates, the two sharing inflammatory and neurodevelopmental links and complicating each other's management."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Trauma and attention deficits intertwine: ADHD and PTSD frequently co-occur, sharing impulsivity and arousal dysregulation, and childhood ADHD raises vulnerability to traumatic events."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its stimulant treatment touches growth: appetite-suppressing stimulants can modestly slow height and weight gain in children with ADHD, prompting growth monitoring, and they raise heart rate and blood pressure."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Stimulants curb appetite and upset the gut: the medications for ADHD commonly cause appetite suppression with weight loss, nausea and abdominal pain, complicating nutrition in growing children."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Anxiety rides alongside it: panic and anxiety disorders are frequently comorbid with ADHD, and the stimulants used to treat it can provoke or worsen panic attacks, complicating management."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It often comes with bedwetting: nocturnal enuresis and daytime urinary incontinence are markedly more common in children with ADHD, reflecting shared maturational and attentional factors."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It clusters with allergy and autoimmunity: ADHD is associated with atopic and allergic conditions and shows links to immune dysregulation and low-grade inflammation."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It touches the skin: ADHD co-occurs with atopic dermatitis and with chronic skin-picking, and stimulant-related formication can drive scratching and excoriation."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It travels with allergy and bad sleep: ADHD frequently coexists with asthma and allergic disease, and obstructive sleep apnoea can mimic or worsen the inattention and hyperactivity."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet offers a small lever: omega-3 supplementation shows modest benefit for ADHD symptoms in trials, a complement rather than a substitute for established treatment."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Trace minerals draw interest: low zinc and iron status are associated with ADHD, and supplementation may help when deficiency is present, though it is not a primary therapy."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "A genetic cause of the attention phenotype: around half of children with neurofibromatosis type 1 meet criteria for ADHD, making it one of the strongest single-gene contributors to the disorder."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Inattention and chronic pain overlap: ADHD is markedly more common in fibromyalgia, the two sharing dopaminergic dysregulation, poor sleep and difficulties with attention and pain processing."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Shared neurodevelopmental roots: ADHD and schizophrenia overlap in genetic risk and dopaminergic dysfunction, and childhood ADHD is associated with a modestly raised later risk of psychosis."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Its wiring is subtly altered: ADHD shows differences in white-matter microstructure and axonal connectivity across fronto-striatal and cerebellar networks, the structural correlate of its attention and impulse-control difficulties."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "A shared dopamine thread: ADHD and Parkinson's both centre on dopamine dysregulation — one treated by boosting dopamine with stimulants, the other by replacing it — and ADHD is linked to a modestly higher later risk of Parkinson's."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Its stimulants touch the heart's rhythm: methylphenidate and amphetamines raise heart rate and blood pressure and can affect cardiac conduction, so cardiac history is screened before starting stimulant treatment for ADHD."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Arousal and vigilance: orexin from the hypothalamus sustains wakefulness and attention, and the sleep-wake instability common in ADHD—and its overlap with narcolepsy—implicates this arousal system."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "The wakefulness amine: brain histamine acting through H3 receptors regulates attention and arousal, and H3-modulating drugs are studied in ADHD and narcolepsy."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "Impulse control and eating: ADHD raises the risk of disordered eating across the spectrum, and stimulant-driven appetite suppression complicates its overlap with anorexia nervosa."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "ADHD in genetic syndromes: tuberous sclerosis, like neurofibromatosis type 1, carries very high rates of ADHD, linking single-gene neurodevelopmental disorders to attention dysfunction."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "A later dementia link: adult ADHD is associated with a higher later risk of dementia including Alzheimer's, possibly through shared catecholaminergic vulnerability and accumulated lifestyle risk."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Attention after the pandemic: COVID-19 disruption worsened ADHD symptoms and access to care, and long-COVID 'brain fog' can mimic or aggravate attention deficits."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Atopy and attention: atopic dermatitis is epidemiologically associated with ADHD, plausibly through chronic inflammation and the sleep disruption that relentless itch causes in childhood."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Cholinergic attention: acetylcholine modulates arousal and selective attention, and nicotinic signalling is implicated in ADHD—reflected in high smoking rates and trials of nicotinic agonists."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Caffeine and arousal: blocking adenosine receptors with caffeine—often self-administered in ADHD—disinhibits dopamine signalling and boosts alertness, loosely mirroring stimulant medication."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Blunted stress axis: ADHD is associated with a dysregulated, often blunted cortisol response, reflecting altered HPA-axis function that may relate to its arousal and emotional-regulation difficulties."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Neuroinflammation link: elevated IL-6, including maternal IL-6 in pregnancy, is associated with ADHD risk, part of the emerging inflammatory contribution to neurodevelopment."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory association: raised TNF-α is reported in ADHD, consistent with the low-grade inflammation increasingly linked to neurodevelopmental and attentional disorders."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "Impulsivity and comorbidity: serotonin-transporter function shapes the impulsivity of ADHD and its frequent comorbid anxiety and depression, intersecting with the dopamine-noradrenaline circuits stimulants target."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Neurodevelopmental growth: IGF-1 supports the brain maturation that is delayed in ADHD, fitting the model of the disorder as a maturational lag in prefrontal network development."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Prenatal androgen influence: prenatal testosterone exposure is implicated in the marked male predominance of ADHD and in shaping the developing attention and impulse-control circuits."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormonal symptom fluctuation: estrogen enhances dopaminergic tone, so ADHD symptoms in women fluctuate across the menstrual cycle and often worsen in the low-estrogen perimenopausal years, affecting treatment response."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophin development: BDNF signalling through TrkB shapes the prefrontal circuit maturation implicated in ADHD, linking neurotrophin signalling to the delayed cortical development underlying the disorder."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Neuroinflammation link: elevated inflammatory chemokines such as CCL2 are increasingly associated with ADHD, consistent with the maternal-immune-activation and inflammation contributions to its neurodevelopmental risk."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron-dopamine link: iron is a cofactor for tyrosine hydroxylase in dopamine synthesis, and low iron stores (ferritin) are associated with ADHD severity and restless legs, a basis for checking and replacing iron in affected children."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Cross-disorder genetics: calcium-channel genes such as CACNA1C are shared risk loci across ADHD and other psychiatric disorders, implicating dysregulated neuronal calcium signalling in the activity-dependent synaptic processes underlying attention."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitrergic signalling: neuronal nitric-oxide synthase shapes dopaminergic and glutamatergic transmission in the prefrontal circuits governing attention, and nNOS gene variants have been associated with ADHD and impulsivity."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Stress reactivity: HPA-axis dysregulation (cortisol already mapped) and altered glucocorticoid-receptor signalling are implicated in ADHD, linking stress reactivity to its inattention and emotional dysregulation."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Dopamine signalling: dopamine D2-receptor signalling through the AKT-GSK3β axis modulates the striatal dopamine circuitry central to ADHD and to the action of its dopaminergic stimulant treatments."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Circuit plasticity: dopamine- and BDNF-driven ERK signalling supports the prefrontal-striatal synaptic plasticity whose disruption contributes to the attentional and executive deficits of ADHD."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Neuroinflammatory contribution: TLR4-driven neuroinflammation is increasingly implicated in ADHD, linking immune activation and maternal-immune-activation risk to the catecholaminergic dysfunction of the disorder."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Neurodevelopmental plasticity: mTOR-dependent synaptic plasticity shapes the prefrontal-striatal circuit development whose alterations underlie the executive-function deficits of ADHD."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative stress: NRF2-regulated antioxidant defences counter the oxidative stress reported in ADHD, a redox component of its neurodevelopmental pathophysiology."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "BDNF/neurotrophin PI3K-AKT-mTOR signalling (mTOR, GSK-3β and ERK mapped) supports the neurodevelopmental processes implicated in ADHD."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN regulation of the PI3K-AKT-mTOR axis influences neuronal connectivity and is implicated in neurodevelopmental phenotypes overlapping ADHD."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 reflects the low-grade neuroinflammation increasingly associated with ADHD."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the low-grade inflammatory tone linked to the neurodevelopmental dysregulation of ADHD."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the innate neuroinflammation implicated in the neurodevelopmental component of ADHD."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling transduces the maternal-immune-activation interferon exposure epidemiologically linked to ADHD."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of the PTEN-PI3K-AKT axis (PTEN and AKT already mapped) regulates the neuronal plasticity and oxidative-stress handling relevant to the neurodevelopmental circuitry of ADHD."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the low-grade inflammatory tone associated with ADHD."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to ADHD."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and oxidative-stress adaptation participates in the neurodevelopmental neurobiology of attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the neuronal plasticity of the fronto-striatal circuits implicated in attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of neurodevelopmental gene expression implicated in attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the neurometabolic mechanisms relevant to attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal and synaptic homeostasis implicated in attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the catecholamine-receptor and synaptic signaling implicated in attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuronal migration and neurodevelopmental processes implicated in attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven neuroinflammation participates in the immune-related mechanisms implicated in attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the microglial synaptic remodeling and neuroinflammatory processes implicated in attention-deficit hyperactivity disorder."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Social cognition: oxytocin shapes the social-cognitive and reward circuits implicated in the interpersonal difficulties of ADHD, and is being explored as an adjunct to address social deficits beyond the core dopaminergic symptoms."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Brain renin-angiotensin: central angiotensin II modulates dopaminergic transmission and stress reactivity, a neuroendocrine axis distinct from the catecholamine systems (dopamine already mapped) targeted by stimulants in ADHD."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Hormonal fluctuation: ADHD symptoms in women often worsen when progesterone-derived neurosteroids fall across the menstrual cycle, part of the reproductive-hormone influence (estrogen already mapped) on the disorder's expression."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress reactivity and arousal systems dysregulated alongside the catecholamine deficits of ADHD."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic association: ADHD is associated with higher rates of obesity and insulin resistance, linked partly to impulsive eating and shared dopaminergic (already mapped) reward pathways, a metabolic dimension of the disorder."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory cytokine IL-10 counters the elevated IL-6 and TNF (already mapped) reported in ADHD, part of the low-grade neuroinflammation implicated in a subset of the disorder."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and impulsive eating: ADHD is associated with obesity and disordered eating, and the adipokine leptin, with the shared dopaminergic (already mapped) reward pathways, links the disorder to its metabolic comorbidity (insulin already mapped)."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic dyslipidaemia: the obesity and metabolic dysregulation (insulin already mapped) more common in ADHD shift cholesterol handling toward an atherogenic profile, part of the cardiometabolic dimension of the disorder."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6, TNF and IL-1 already mapped) implicated in a subset of ADHD modulate the fronto-striatal circuits (dopamine already mapped) of the disorder."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation implicated in a subset of ADHD."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is part of the type-2 response whose balance against the pro-inflammatory signals shapes the neuroinflammatory dimension of ADHD."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and catecholamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), and disturbed copper-zinc (already mapped) balance is reported in ADHD."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic (insulin already mapped) comorbidity reported in ADHD."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the metabolic-inflammatory dimension associated with ADHD."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron-regulatory hormone: hepcidin governs the iron (transferrin and iron already mapped) handling whose disturbance underlies the low-iron state associated with ADHD, affecting the dopamine (already mapped) synthesis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Dopaminergic circuits: the prefrontal-striatal dopaminergic and noradrenergic (already mapped) neurons and their synaptic signalling underlie ADHD, the stimulant (methylphenidate) target."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc cofactor: zinc (a cofactor for the dopamine — already mapped — metabolism and the melatonin — already mapped — pathway) is often low in ADHD, and the supplementation is studied as an adjunct."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Substance-use link: ADHD raises the risk of the (stimulant and other) substance use disorder, and the properly treated stimulant medication modifies that risk."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in the neurodevelopment of ADHD."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation (IL-1 and TNF already mapped) associated with ADHD."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of ADHD."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation and the atopy comorbidity associated with ADHD."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension associated with ADHD."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/atopy arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension and the atopy comorbidity associated with ADHD."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the histamine (already mapped) and neuroinflammatory dimension implicated in ADHD."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune dimension of the neuroinflammatory interaction associated with ADHD."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate immune arm: the NK cells (perforin pathway) are part of the peripheral innate-immune dimension of the immune dysregulation reported in ADHD."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the low-grade complement activation of the neuroinflammation implicated in ADHD."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial neuroinflammation implicated in the neurodevelopmental dimension of ADHD."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the neuroinflammation reported in ADHD."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-neuroimmune axis: TSLP, from barrier epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the neuroinflammatory dimension of ADHD."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-neuroinflammation axis: bradykinin, via B1/B2 receptors on microglia (already mapped) and brain endothelium, amplifies the blood-brain-barrier disruption and the neuroinflammatory milieu of ADHD."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective cytokine: erythropoietin, via the EPOR on neurons and microglia (already mapped), modulates the neuronal survival and the neuroinflammatory dimension of the neurodevelopmental disorder of ADHD."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C3/C5 already mapped) whose activation contributes to the neuroinflammatory signalling and synaptic pruning of the neurodevelopmental disorder of ADHD."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Alternative complement regulation: factor H regulates the alternative complement pathway (C3/C5 already mapped) whose dysregulation amplifies the microglial neuroinflammation and synaptic pruning of the neurodevelopmental dimension of ADHD."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Neuroendocrine-immune axis: prolactin, via PRL receptors on microglia (already mapped) and T cells (already mapped), modulates the neuroinflammatory cytokine milieu (dopamine already mapped) of the neurodevelopmental disorder of ADHD."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "ADHD vasopressin: vasopressin, via V1aR on neurons (already mapped) and microglia (already mapped), modulates social-memory and HPA-axis stress; vasopressin dysregulation amplifies the dopamine (already mapped) and norepinephrine (already mapped) executive-dysfunction of ADHD."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "ADHD selenium: selenium, as neuroprotective GPx in neurons (already mapped) and microglia (already mapped), scavenges neuroinflammatory ROS; selenium deficiency impairs the dopamine (already mapped) and norepinephrine (already mapped) neurotransmitter regulation of ADHD."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "ADHD iodine: iodine-dependent thyroid hormones modulate dopaminergic (dopamine already mapped) and noradrenergic (norepinephrine already mapped) tone; iodine deficiency impairs the prefrontal cortex (neurons already mapped) executive function and the attention regulation of ADHD."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "ADHD sodium: high dietary sodium amplifies neuroinflammation in neurons (already mapped) and microglia (already mapped); sodium dysregulation amplifies NF-κB (already mapped) and worsens the dopamine (already mapped) and norepinephrine (already mapped) dysfunction of ADHD."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "ADHD potassium: potassium, via Kv channels on neurons (already mapped), regulates GABAergic interneuron tone; potassium dysregulation amplifies neural excitability and the dopamine (already mapped) and norepinephrine (already mapped) executive-dysfunction cascade of ADHD."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "ADHD phosphorus: phosphorus, as ATP in neurons (already mapped) and astrocytes (already mapped), sustains dopaminergic (dopamine already mapped) neurotransmission; phosphorus deficiency impairs norepinephrine (already mapped) signalling and the prefrontal resilience of ADHD."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "ADHD nitrogen: nitric oxide (NO, nitrogen-derived) in neurons (already mapped) and microglia (already mapped) regulates dopamine (already mapped) neurotransmission; NO dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in ADHD."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "ADHD chloride: chloride channels on neurons (already mapped) and microglia (already mapped) regulate membrane excitability; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) signalling cascade in ADHD."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "ADHD sulfur: sulfur-containing glutathione in neurons (already mapped) and microglia (already mapped) scavenges ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) dysregulation in ADHD."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "carbon-based lipid mediators in neurons (already mapped) support synaptic signalling; disrupted carbon metabolism amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) and BDNF (already mapped) neurodevelopmental dysregulation in ADHD."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "hydrogen ion dysregulation in brain (already mapped) amplifies neurotransmission; proton excess disrupts dopamine (already mapped) and norepinephrine (already mapped) and BDNF (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) neuronal cascade in ADHD."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "ROS from NADPH oxidase in neurons (already mapped) and brain (already mapped) microglia impairs prefrontal circuit function; oxygen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) and BDNF (already mapped) cascade in ADHD."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "ADHD pd-1: PD-1 on t-cytotoxic cells (already mapped) and microglia (already mapped) suppresses neuroimmune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory dopaminergic disruption in ADHD."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "ADHD glp-1: GLP-1 on neurons (already mapped) and astrocytes (already mapped) modulates synaptic energy metabolism; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory dopamine-circuit dysfunction in ADHD."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "ADHD vegf: VEGF from astrocytes (already mapped) and neurons (already mapped) sustains cerebrovascular supply; VEGF deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory dopamine (already mapped) deficit in ADHD."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "ADHD wnt-beta-catenin: WNT/β-catenin on neurons (already mapped) and astrocytes (already mapped) regulates plasticity; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) dopamine-circuit dysfunction in ADHD."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "ADHD rankl: RANKL in microglia (already mapped) and astrocytes (already mapped) modulates neuroinflammatory skewing; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) dopamine-circuit dysfunction in ADHD."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "ADHD smad4: SMAD4 in neurons (already mapped) and astrocytes (already mapped) mediates TGF-β neuroprotection; smad4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) dopamine-circuit dysfunction in ADHD."
---

# Attention-Deficit/Hyperactivity Disorder

## Overview

**Attention-deficit/hyperactivity disorder (ADHD)** is one of the most common neurodevelopmental disorders, affecting approximately **5-10% of children** and **2.5-5% of adults** worldwide — roughly 366 million adults globally [^faraone-2021-adhd-primer]. It is characterized by persistent, developmentally inappropriate inattention, hyperactivity, and impulsivity that impairs functioning across multiple settings (home, school, work). ADHD is the most heritable common psychiatric disorder (~75–80% heritability in twin studies) and is defined by a complex polygenetic architecture.

**ADHD is not a deficit of attention per se** — it is more accurately understood as a **deficit in executive regulation of attention**: the ability to direct, sustain, and shift attention according to goals rather than immediate stimuli. Crucially, ADHD individuals can hyperfocus intensely on high-interest activities while being unable to sustain attention on low-interest tasks — reflecting motivational rather than attentional capacity differences [^arnsten-2009-adhd-neuroscience].

ADHD persists into adulthood in approximately **60-70%** of childhood cases (though symptoms may shift from overt hyperactivity to inner restlessness and disorganization). Adult ADHD is associated with markedly elevated rates of underemployment, relationship instability, accidental injury, substance use disorders (~25% comorbidity), and a 13-year reduction in life expectancy in the most severely affected.

**DSM-5 ADHD subtypes:**
- **Combined presentation (ADHD-C):** ≥6 inattentive + ≥6 hyperactive-impulsive symptoms; ~50-70% of cases
- **Predominantly Inattentive (ADHD-PI, "ADD"):** ≥6 inattentive symptoms; ~20-30%; under-diagnosed, especially in females
- **Predominantly Hyperactive-Impulsive (ADHD-PH):** ≥6 hyperactive-impulsive symptoms; ~5-15%; most common presentation in preschool children

## Structure

### Neurobiological basis: PFC catecholamine deficit [^arnsten-2009-adhd-neuroscience]

The dominant neurobiological model of ADHD centers on **prefrontal cortex (PFC) dysfunction driven by dopamine (DA) and norepinephrine (NE) deficiency**:

**PFC and executive function:**
The PFC (dorsolateral PFC, anterior cingulate cortex, orbital PFC) is the neural substrate of executive function: working memory, response inhibition, attentional control, and decision-making. PFC layer III pyramidal neurons maintain persistent firing representing task-relevant information ("working memory"). This persistent activity requires optimal DA D1 and NE α2A receptor stimulation:

| Signal | Receptor | Effect at optimal level | Effect at deficit |
|:---|:---|:---|:---|
| **Dopamine** | D1 (Gs/cAMP) → closes HCN/K⁺ channels | Strengthens task-relevant PFC column connectivity | Weakens signal; distraction prevails |
| **Norepinephrine** | α2A (Gi/cAMP↓) → HCN channel closure | Strengthens working memory networks | NE deficiency → HCN channels open → signal noise |

**"Inverted-U" tuning:** Both DA and NE PFC effects follow an inverted-U concentration curve — too little OR too much impairs PFC function. Stimulants optimize catecholamines by increasing synaptic levels from sub-optimal to optimal (rather than simply "adding more").

**Striatal dopamine and reward:** Mesolimbic (VTA→striatum) dopamine is also affected — reduced dopamine release to non-immediate rewards reduces motivation for deferred outcomes, contributing to impulsivity and procrastination. This is distinct from the PFC catecholamine deficit driving inattention.

### Neural circuit abnormalities (neuroimaging)

MRI studies in ADHD (pooled N > 10,000) reveal:
- **Total brain volume:** ~3-5% smaller than non-ADHD controls; delay of ~2-5 years in cortical maturation; volume difference normalizes partially with age
- **PFC gray matter:** Dorsolateral and anterior cingulate PFC thinning correlates with ADHD severity; right-predominant
- **Caudate nucleus:** Smaller; normalizes with stimulant treatment (suggesting medication normalizes volume)
- **Cerebellum:** 3-5% smaller; contributes to timing and motor control deficits
- **Default mode network (DMN):** Fails to deactivate during tasks → competes with task-positive networks → internal thoughts interrupt goal-directed behavior ("mind wandering")
- **White matter:** Reduced fractional anisotropy (FA) in frontostriatal and frontoparietal tracts

## Function

### DSM-5 symptom criteria

**Inattention (≥6 of 9 for ≥6 months, not explained by developmental level):**
- Often fails to give close attention to details; careless mistakes
- Difficulty sustaining attention in tasks or play
- Does not seem to listen when spoken to directly
- Does not follow through on instructions; fails to finish tasks
- Difficulty organizing tasks; poor time management
- Avoids, dislikes, or reluctantly engages tasks requiring sustained mental effort
- Often loses things necessary for tasks
- Easily distracted by extraneous stimuli
- Often forgetful in daily activities

**Hyperactivity-Impulsivity (≥6 of 9 symptoms for ≥6 months):**
- Often fidgets or squirms; leaves seat when expected to remain seated
- Runs/climbs when inappropriate (in adults: feelings of restlessness)
- Unable to engage in leisure activities quietly
- "On the go," "driven by a motor"
- Often talks excessively; blurts out answers; difficulty waiting turn
- Often interrupts or intrudes on others

**Diagnostic requirements:** Symptoms present before age 12; present in ≥2 settings; impair social, academic, or occupational function; not exclusively during psychosis or another disorder.

### ADHD in females

ADHD is diagnosed ~4:1 male:female in children, narrowing to ~2:1 in adults. Female under-diagnosis is a recognized systemic bias:
- Females more often present with inattentive (not hyperactive) subtype — less disruptive, less likely to trigger referral
- Females develop more effective compensatory strategies masking impairment
- Comorbid anxiety and depression (more common in females with ADHD) are often treated without the underlying ADHD being identified
- Female ADHD symptoms often worsen with hormonal fluctuations (premenstrual, peripartum, menopause) due to estrogen-dopamine interaction

### Comorbidities

| Comorbidity | Frequency | Notes |
|:---|:---|:---|
| Anxiety disorders | ~50% | Can co-exist with ADHD; distinguish from ADHD-driven "worry about consequences of inattention" |
| Major depressive disorder | ~35% | Often secondary to ADHD-related failures; treat ADHD first |
| Oppositional defiant disorder (ODD) | ~60% in children | Treat with ADHD medications + behavioral therapy |
| Learning disabilities | ~45% | Distinct from ADHD; reading disorder (dyslexia) most common |
| Substance use disorders | ~25% | ADHD is a major risk factor; treatment with stimulants reduces SUD risk |
| Autism spectrum disorder | ~20-50% | Significant overlap; both can co-exist per DSM-5 (allowed since 2013) |
| Tic disorder/Tourette | ~10-20% | Stimulants rarely worsen tics contrary to previous concern |
| Sleep disorders | ~75% | Delayed sleep phase (DSPS) very common; poor sleep worsens ADHD |

## Pathology

### Genetics

ADHD heritability: **75-80%** (twin studies), making it the most heritable common psychiatric disorder.

**Candidate gene associations (before GWAS):**
- **DAT1/SLC6A3:** Dopamine transporter; 10-repeat VNTR in 3'UTR associated with ADHD; methylphenidate is a DAT inhibitor
- **DRD4 7-repeat:** D4 receptor exon III 7-repeat allele; associated with ADHD, novelty-seeking; encodes reduced-sensitivity receptor
- **DRD5:** D5 receptor microsatellite polymorphism; meta-analytic association
- **COMT Val158Met:** Met allele → slower dopamine catabolism → higher PFC DA; Val allele → faster catabolism → lower PFC DA → ADHD risk; affects stimulant response
- **SNAP25:** Synaptosomal-associated protein 25; presynaptic DA release

**GWAS (2019, iPSYCH/deCODE, N > 55,000):** 12 genome-wide significant loci identified; genes implicated in neuronal development (FOXP2, STK39) and DA/NE signaling; SNP heritability ~22%; most loci are shared with educational attainment, executive function, and other psychiatric disorders.

**Copy number variants (CNVs):** 16p13.11 duplications, 1q21.1 deletions, and chromosomal regions overlapping with ASD and schizophrenia — ADHD shares genetic architecture with multiple neurodevelopmental conditions.

### Diagnosis and assessment

ADHD is a clinical diagnosis requiring [^biederman-2005-adhd-adults]:
1. Comprehensive history (parent/teacher/self-report rating scales)
2. **Rating scales:** Conners 3, ADHD Rating Scale-5 (ADHD-RS-5), Adult ADHD Self-Report Scale (ASRS)
3. Cognitive testing (not required but informative): TOVA, CPT (sustained attention); BRIEF-2 (executive function)
4. Neuroimaging and EEG: NOT diagnostic (no biomarker distinguishes ADHD from controls at individual level)
5. Rule out: thyroid dysfunction, sleep apnea, vision/hearing deficits, mood disorders, substance use

**EEG:** Elevated theta/alpha power and reduced beta power at frontal electrodes are group-level findings but not diagnostic. Theta/beta ratio: FDA cleared as adjunctive tool but insufficient alone for diagnosis.

### Treatment

**Stimulant medications — first-line:**

| Drug class | Mechanism | Examples | Onset/Duration |
|:---|:---|:---|:---|
| **Methylphenidate (MPH)** | Blocks DAT and NET reuptake | Ritalin (IR), Concerta (OROS), Jornay PM (delayed-release), Daytrana (patch) | IR: 4h; ER: 8-12h |
| **Amphetamine** | Blocks DAT/NET + reverses transporter (active DA/NE release) | Adderall XR, Vyvanse (lisdexamfetamine, prodrug), Dexedrine | IR: 4-6h; XR: 10-14h |

- Response rate: ~70-80% for any stimulant; if one stimulant class fails, try the other
- Effect sizes: Cohen's d ~0.8-1.0 for core ADHD symptoms (one of the highest in psychiatry)
- Safety: Modest appetite suppression (most children stay within normal growth curves), heart rate/BP increase (~3-5 bpm/1-2 mmHg average); cardiovascular screening required
- Lisdexamfetamine (Vyvanse): prodrug converted to d-amphetamine by red blood cell enzymes → lower abuse potential; FDA-approved for ADHD and binge eating disorder

**Non-stimulant medications — second-line:**

| Drug | Mechanism | Use case |
|:---|:---|:---|
| **Atomoxetine (Strattera)** | Selective NE reuptake inhibitor | Stimulant intolerance, active substance use disorder, tic disorder |
| **Guanfacine ER (Intuniv)** | α2A agonist | Combined with stimulants for incomplete response; especially for hyperactivity/impulsivity |
| **Clonidine ER (Kapvay)** | α2A/α2B/α2C agonist | Similar to guanfacine; also treats sleep-onset insomnia in ADHD |
| **Viloxazine ER (Qelbree)** | NE reuptake inhibitor + 5-HT2B antagonist | Newer FDA-approved non-stimulant; faster onset than atomoxetine |
| **Bupropion** | DA/NE reuptake inhibitor | Off-label; useful if comorbid depression; lower effect size than stimulants |

**Behavioral interventions:**
- **Children:** Behavioral parent training (BPT) is evidence-based; organizational skills training; school accommodations (extended time, preferential seating, reduced-distraction environment)
- **Adults:** CBT for ADHD (CBT-ADHD) addresses maladaptive beliefs, time management deficits, emotional dysregulation; combined with medication superior to either alone
- **Exercise:** Acute aerobic exercise (20-30 min) produces ~24-hour reduction in ADHD symptoms; chronic exercise raises BDNF, increases catecholamine release, and improves executive function — recommended as adjunct

## Connections

- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — ADHD involves hypofunctional PFC D1 receptor signaling impairing working memory; methylphenidate and amphetamines increase synaptic dopamine; COMT Val158Met SNP (rapid catabolism) increases ADHD risk; striatal dopamine deficiency reduces reward motivation and drives impulsivity.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — NE α2A-receptor signaling in PFC strengthens layer III pyramidal neuron connectivity underlying working memory; atomoxetine (selective NE reuptake inhibitor) and guanfacine/clonidine (α2A agonists) treat ADHD by restoring NE-PFC function without dopamine-reward circuit effects.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — ADHD involves PFC, anterior cingulate, and striatal circuit dysfunction; MRI shows ~3-5% smaller total brain volume with 2-5 year cortical maturation delay; default mode network fails to deactivate during tasks → attention lapses; PFC gray matter thinning correlates with ADHD severity.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF Val66Met SNP is over-represented in ADHD; BDNF supports PFC dopaminergic circuit maturation; stimulant treatment increases BDNF in PFC; aerobic exercise, which robustly raises BDNF, reduces ADHD symptom severity and improves executive function outcomes.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — PFC layer III pyramidal neurons are the core ADHD substrate; they express DA D1 and NE α2A receptors maintaining persistent firing for working memory; D1 → cAMP → HCN/K⁺ channel closure → strengthened circuit; catecholamine deficiency → HCN open → signal noise → inattention.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — ADHD and ASD co-occur in 20-50% of cases; DSM-5 (2013) allows dual diagnosis; both share genetic architecture (CNVs at 16p13.11, 1q21.1; FOXP2, SHANK3) and PFC-striatal circuit dysfunction; methylphenidate has lower efficacy and more side effects in ASD+ADHD vs ADHD alone.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — hippocampus is ~3-4% smaller in ADHD (meta-analysis); working memory deficits partly reflect hippocampal-PFC circuit dysfunction; stimulants normalize hippocampal-PFC connectivity on fMRI; episodic memory impairment is an underrecognized domain affecting academic performance.
- `connects-to` → **[Bulimia Nervosa](../bulimia-nervosa/README.md)** — ADHD and bulimia nervosa are linked by impulsivity and reward dysregulation: childhood ADHD roughly doubles later bulimia risk, with shared deficits in prefrontal inhibitory control and dopaminergic reward driving both loss-of-control eating and impulsive behavior.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — ADHD and stimulant use disorder share a dopaminergic core: untreated ADHD raises later substance-use risk, yet properly prescribed stimulants lower it; still, the same drugs carry misuse and diversion potential, so prescribing balances benefit against addiction risk.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — ADHD and bipolar disorder overlap and are easily confused: both feature distractibility, impulsivity, and high energy, but ADHD is chronic and trait-like while bipolar elevation is episodic; they co-occur, and stimulants are used cautiously in bipolar ADHD to avoid mania.
- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — ADHD strongly predisposes to gambling disorder: deficient dopaminergic reward processing and impaired impulse control drive risky, poorly-checked betting, the two are highly comorbid, and gambling severity tracks ADHD symptom load—so impulsivity is a shared treatment target.
- `connects-to` → **[Internet Gaming Disorder](../internet-gaming-disorder/README.md)** — ADHD is one of the strongest correlates of internet gaming disorder: deficits in dopaminergic reward and inhibition predispose to compulsive gaming, the two are highly comorbid bidirectionally, and IGD severity tracks ADHD symptom load—stimulant treatment can reduce gaming.
- `connects-to` → **[Binge Eating Disorder](../binge-eating-disorder/README.md)** — ADHD is strongly linked to binge eating disorder: deficient dopaminergic reward and impulse control predispose to impulsive overeating, the two are highly comorbid, and lisdexamfetamine—an ADHD stimulant—is the only FDA-approved BED drug, dampening the reward salience of food.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — ADHD and depression frequently co-occur and can be hard to separate: untreated ADHD's chronic underachievement and rejection feed depression, the disorders share dopaminergic and executive-function deficits, and stimulant plus antidepressant strategies are often combined.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety disorders are among the commonest ADHD comorbidities: the strain of inattention and disorganization breeds chronic worry, and the two can mask each other—stimulants may worsen anxiety while untreated ADHD fuels it—so treatment must balance both.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — ADHD substantially raises the risk of alcohol and other substance use disorders: impulsivity and reward dysregulation drive earlier, heavier use, and self-medication is common—so treating ADHD can lower, not raise, the long-term addiction risk.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — ADHD and insomnia are deeply linked: delayed sleep phase, bedtime restlessness and racing thoughts are common in ADHD, and stimulant treatment can worsen sleep onset—while the resulting sleep loss mimics and amplifies inattention, blurring cause and effect.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — ADHD raises the risk of cannabis use disorder: impulsivity and self-medication for restlessness drive earlier, heavier use, yet cannabis worsens attention and motivation—so the disorder and the drug reinforce each other, complicating diagnosis and treatment.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Glutamate signaling is implicated in ADHD beyond dopamine: imbalances in glutamate—the brain's main excitatory transmitter—affect the prefrontal circuits governing attention and impulse control, and are a target of interest for non-stimulant ADHD therapies.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Beyond dopamine and norepinephrine, serotonin modulates ADHD: serotonergic tone influences the impulsivity and emotional dysregulation of the disorder, and serotonin-acting drugs are used for comorbid mood and anxiety symptoms common in ADHD.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — ADHD is a neurodevelopmental disorder of the nervous system's executive networks: delayed maturation and altered connectivity in prefrontal-striatal circuits impair attention and impulse control, so it reflects how the brain regulates behavior, not a lack of effort.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Iron deficiency is linked to ADHD symptoms: iron is a cofactor for dopamine synthesis, and low ferritin is associated with worse inattention and restless sleep, so checking and correcting iron can be part of evaluating a child with ADHD.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — ADHD commonly comes with disrupted sleep: delayed melatonin release shifts the body clock later, causing trouble falling asleep that worsens daytime inattention, so melatonin and sleep treatment are part of comprehensive ADHD care.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — ADHD risk is partly set before birth via the placenta: maternal smoking, alcohol, stress, and placental insufficiency that limit fetal brain growth raise the child's ADHD risk—so prenatal environment shapes this neurodevelopmental disorder.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — ADHD and OCD share frontostriatal circuitry yet pull oppositely: ADHD is impulsive and under-controlled while OCD is over-controlled, so they can co-occur and complicate each other—and stimulants for ADHD may aggravate obsessions.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — ADHD reaches beyond neurons to astrocytes: these glial cells help clear and recycle dopamine and glutamate at synapses, so astrocyte dysfunction can blunt the prefrontal signaling that stimulant medications work to restore.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — ADHD and epilepsy travel together: children with epilepsy have far higher ADHD rates and vice versa, sharing disrupted attention networks—and stimulant treatment is generally safe and helpful rather than seizure-provoking in well-controlled epilepsy.
- `connects-to` → **[Obesity](../obesity/README.md)** — ADHD predisposes to obesity: impulsivity and dopamine-driven reward seeking promote dysregulated, binge-style eating, so untreated attention-deficit symptoms are a risk factor for weight gain and disordered eating.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron is the quiet partner of dopamine in ADHD: it is a cofactor for the enzyme that makes dopamine, so low iron stores (even without anemia) are linked to worse symptoms, and supplementation is studied in deficient children.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — ADHD is a disorder of the dopamine synapse: signaling across reward and attention synapses is dysregulated, and stimulant medicines work by raising dopamine and norepinephrine in this synaptic gap to sharpen focus.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia may shape the ADHD brain: prenatal inflammation and microglial pruning of synapses influence the development of attention circuits, an emerging neuroimmune angle on why early-life stress raises ADHD risk.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — ADHD is linked to low zinc: the mineral helps regulate dopamine signaling, so deficiency is associated with more severe symptoms, and zinc status is studied as a modifier of the disorder and its treatment.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid shapes attention: its hormones guide brain development and arousal, so thyroid dysfunction can produce inattention and hyperactivity that mimic ADHD, which is why thyroid problems are screened for.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — ADHD treatment must watch the heart: the stimulant medicines that sharpen focus also raise heart rate and blood pressure, so cardiac history and monitoring guide their safe use.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Brain imaging shows ADHD's delayed wiring: MRI photons reveal slower cortical maturation and altered connectivity, and fMRI maps underactivity in the attention and reward networks.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — ADHD involves delayed white matter: the oligodendrocytes that myelinate the connections between attention regions mature slowly, slowing the brain's information highways.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut may sway ADHD: emerging work ties the intestinal microbiome to attention and behavior through the gut-brain axis, hinting the bowel's microbes influence symptoms.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium runs low in many with ADHD: the mineral supports the neurotransmitter balance behind focus and calm, and deficiency is associated with worse symptoms, making it a studied nutritional adjunct.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D in early life may shape ADHD risk: low maternal and childhood levels are linked to higher rates of the disorder, fitting the vitamin's role in the developing brain.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — ADHD and the itchy skin travel together: it is notably comorbid with atopic dermatitis, the sleep-wrecking itch and shared inflammatory and neurodevelopmental threads linking the gut, skin, and attention.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The stimulant treatments curb the appetite: methylphenidate and amphetamines blunt hunger and can cause nausea and stomach upset, so children's intake and weight are watched closely during therapy.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Stimulants can nudge growth off course: by suppressing appetite they may modestly slow height and weight gain in children, prompting drug holidays and growth monitoring during long-term treatment.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Estrogen tunes the ADHD brain: because the hormone modulates dopamine, many women find symptoms swing across the menstrual cycle and worsen as estrogen falls in the perimenopause, shaping how treatment is timed.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — The stimulant medicines lean on the heart: methylphenidate and amphetamines modestly raise heart rate and blood pressure, so cardiovascular history is screened before starting and the vitals are monitored during treatment.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The endocannabinoid system touches attention and reward: it modulates the dopamine circuits implicated in ADHD, part of why cannabis is commonly used — and misused — by those with the disorder seeking relief.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Low iron shows in the red cells and the focus: iron-deficiency, with its small, pale erythrocytes and low ferritin, is more common in ADHD and worsens symptoms, so iron status is checked and repleted as an adjunct.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Attention needs the brain's brakes too: reduced GABAergic inhibition tips the excitation-inhibition balance in ADHD, contributing to the impulsivity and distractibility that stimulant and other therapies try to rein in.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut may shape attention: altered microbiome composition is reported in ADHD, and through the microbiome-gut-brain axis it can influence the dopamine and stress signaling tied to the disorder.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Sleepiness and inattention overlap: ADHD and narcolepsy frequently co-occur and share a hypoarousal that both respond to stimulants, so daytime sleepiness in ADHD prompts a look for an underlying sleep disorder.
- `connects-to` → **[Thyroid Hormones (T3/T4)](../../03-molecular/thyroid-hormones/README.md)** — Thyroid imbalance mimics ADHD: both hyper- and hypothyroidism produce inattention, restlessness, or sluggishness, and rare resistance to thyroid hormone is strongly linked to ADHD — so thyroid function is checked when the picture is atypical.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The stress axis runs differently in ADHD: a blunted or dysregulated adrenal cortisol response is reported, part of the altered arousal regulation that underlies the disorder and its links to stress and sleep.
- `connects-to` → **[Migraine](../migraine/README.md)** — Attention and headache travel together: ADHD and migraine are comorbid more than chance, sharing dopaminergic and arousal dysregulation, so each is more common in people who have the other.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — An inflammatory thread runs through it: emerging evidence links ADHD to low-grade neuroinflammation with NF-κB-driven cytokine signaling, part of why maternal immune activation and inflammation raise the risk.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Impulsivity raises the stakes of every drug: untreated ADHD strongly predisposes to substance use disorders including opioids, the impulsivity and reward dysregulation driving earlier, heavier use and addiction.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — Impulsivity and emotional dysregulation overlap: ADHD and borderline personality disorder co-occur often and share traits of impulsivity and affective instability, blurring the line between the two.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Impulsive eating and obesity raise the metabolic stakes: ADHD's impulsivity and reward dysregulation drive disordered eating and obesity, translating over time into a higher risk of type 2 diabetes.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — Years of social missteps breed fear: the inattention and impulsivity of ADHD cause repeated social difficulties that can foster social anxiety, a common comorbidity that compounds functional impairment.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Its stimulant treatment nudges up the pressure: the methylphenidate and amphetamine medications for ADHD raise heart rate and blood pressure, so cardiovascular monitoring is part of long-term treatment.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Impulsivity and inattention court injury: ADHD carries markedly higher rates of accidents, falls and burns, producing wounds and fractures more often than in the general population.
- `connects-to` → **[Asthma](../asthma/README.md)** — It travels with atopic and respiratory disease: ADHD is comorbid with asthma at elevated rates, the two sharing inflammatory and neurodevelopmental links and complicating each other's management.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Trauma and attention deficits intertwine: ADHD and PTSD frequently co-occur, sharing impulsivity and arousal dysregulation, and childhood ADHD raises vulnerability to traumatic events.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its stimulant treatment touches growth: appetite-suppressing stimulants can modestly slow height and weight gain in children with ADHD, prompting growth monitoring, and they raise heart rate and blood pressure.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Stimulants curb appetite and upset the gut: the medications for ADHD commonly cause appetite suppression with weight loss, nausea and abdominal pain, complicating nutrition in growing children.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Anxiety rides alongside it: panic and anxiety disorders are frequently comorbid with ADHD, and the stimulants used to treat it can provoke or worsen panic attacks, complicating management.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It often comes with bedwetting: nocturnal enuresis and daytime urinary incontinence are markedly more common in children with ADHD, reflecting shared maturational and attentional factors.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It clusters with allergy and autoimmunity: ADHD is associated with atopic and allergic conditions and shows links to immune dysregulation and low-grade inflammation.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It touches the skin: ADHD co-occurs with atopic dermatitis and with chronic skin-picking, and stimulant-related formication can drive scratching and excoriation.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It travels with allergy and bad sleep: ADHD frequently coexists with asthma and allergic disease, and obstructive sleep apnoea can mimic or worsen the inattention and hyperactivity.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet offers a small lever: omega-3 supplementation shows modest benefit for ADHD symptoms in trials, a complement rather than a substitute for established treatment.
- `connects-to` → **[Dietary Zinc](../../../03-medicine/03-food/zinc-dietary/README.md)** — Trace minerals draw interest: low zinc and iron status are associated with ADHD, and supplementation may help when deficiency is present, though it is not a primary therapy.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — A genetic cause of the attention phenotype: around half of children with neurofibromatosis type 1 meet criteria for ADHD, making it one of the strongest single-gene contributors to the disorder.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Inattention and chronic pain overlap: ADHD is markedly more common in fibromyalgia, the two sharing dopaminergic dysregulation, poor sleep and difficulties with attention and pain processing.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Shared neurodevelopmental roots: ADHD and schizophrenia overlap in genetic risk and dopaminergic dysfunction, and childhood ADHD is associated with a modestly raised later risk of psychosis.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Its wiring is subtly altered: ADHD shows differences in white-matter microstructure and axonal connectivity across fronto-striatal and cerebellar networks, the structural correlate of its attention and impulse-control difficulties.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — A shared dopamine thread: ADHD and Parkinson's both centre on dopamine dysregulation — one treated by boosting dopamine with stimulants, the other by replacing it — and ADHD is linked to a modestly higher later risk of Parkinson's.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Its stimulants touch the heart's rhythm: methylphenidate and amphetamines raise heart rate and blood pressure and can affect cardiac conduction, so cardiac history is screened before starting stimulant treatment for ADHD.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Arousal and vigilance: orexin from the hypothalamus sustains wakefulness and attention, and the sleep-wake instability common in ADHD—and its overlap with narcolepsy—implicates this arousal system.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — The wakefulness amine: brain histamine acting through H3 receptors regulates attention and arousal, and H3-modulating drugs are studied in ADHD and narcolepsy.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — Impulse control and eating: ADHD raises the risk of disordered eating across the spectrum, and stimulant-driven appetite suppression complicates its overlap with anorexia nervosa.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — ADHD in genetic syndromes: tuberous sclerosis, like neurofibromatosis type 1, carries very high rates of ADHD, linking single-gene neurodevelopmental disorders to attention dysfunction.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — A later dementia link: adult ADHD is associated with a higher later risk of dementia including Alzheimer's, possibly through shared catecholaminergic vulnerability and accumulated lifestyle risk.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Attention after the pandemic: COVID-19 disruption worsened ADHD symptoms and access to care, and long-COVID 'brain fog' can mimic or aggravate attention deficits.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Atopy and attention: atopic dermatitis is epidemiologically associated with ADHD, plausibly through chronic inflammation and the sleep disruption that relentless itch causes in childhood.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Cholinergic attention: acetylcholine modulates arousal and selective attention, and nicotinic signalling is implicated in ADHD—reflected in high smoking rates and trials of nicotinic agonists.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Caffeine and arousal: blocking adenosine receptors with caffeine—often self-administered in ADHD—disinhibits dopamine signalling and boosts alertness, loosely mirroring stimulant medication.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Blunted stress axis: ADHD is associated with a dysregulated, often blunted cortisol response, reflecting altered HPA-axis function that may relate to its arousal and emotional-regulation difficulties.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Neuroinflammation link: elevated IL-6, including maternal IL-6 in pregnancy, is associated with ADHD risk, part of the emerging inflammatory contribution to neurodevelopment.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory association: raised TNF-α is reported in ADHD, consistent with the low-grade inflammation increasingly linked to neurodevelopmental and attentional disorders.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — Impulsivity and comorbidity: serotonin-transporter function shapes the impulsivity of ADHD and its frequent comorbid anxiety and depression, intersecting with the dopamine-noradrenaline circuits stimulants target.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Neurodevelopmental growth: IGF-1 supports the brain maturation that is delayed in ADHD, fitting the model of the disorder as a maturational lag in prefrontal network development.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Prenatal androgen influence: prenatal testosterone exposure is implicated in the marked male predominance of ADHD and in shaping the developing attention and impulse-control circuits.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen enhances dopaminergic tone, so ADHD symptoms in women fluctuate across the menstrual cycle and often worsen in the low-estrogen perimenopausal years—a frequently overlooked influence on diagnosis and treatment response.
- `connects-to` → **[NTRK / TrkB](../../03-molecular/ntrk/README.md)** — BDNF signaling through TrkB shapes the prefrontal circuit maturation implicated in ADHD, linking neurotrophin signaling to the delayed cortical development that underlies the disorder's maturational-lag model.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Elevated inflammatory chemokines such as CCL2 are increasingly associated with ADHD, consistent with the maternal-immune-activation and inflammation contributions to its neurodevelopmental risk profile.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron is a cofactor for tyrosine hydroxylase in dopamine synthesis, and low iron stores (ferritin) are associated with ADHD severity and restless legs, a basis for checking and replacing iron in affected children.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium-channel genes such as CACNA1C are shared risk loci across ADHD and other psychiatric disorders, implicating dysregulated neuronal calcium signaling in the activity-dependent synaptic processes underlying attention.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Neuronal nitric-oxide synthase shapes dopaminergic and glutamatergic transmission in the prefrontal circuits governing attention, and nNOS gene variants have been associated with ADHD and impulsivity.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — HPA-axis dysregulation (cortisol already mapped) and altered glucocorticoid-receptor signaling are implicated in ADHD, linking stress reactivity to its inattention and emotional dysregulation.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — Dopamine D2-receptor signaling through the AKT-GSK3β axis modulates the striatal dopamine circuitry central to ADHD and to the action of its dopaminergic stimulant treatments.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Dopamine- and BDNF-driven ERK signaling supports the prefrontal-striatal synaptic plasticity whose disruption contributes to the attentional and executive deficits of ADHD.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4-driven neuroinflammation is increasingly implicated in ADHD, linking immune activation and maternal-immune-activation risk to the catecholaminergic dysfunction of the disorder.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-dependent synaptic plasticity shapes the prefrontal-striatal circuit development whose alterations underlie the executive-function deficits of ADHD.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2-regulated antioxidant defenses counter the oxidative stress reported in ADHD, a redox component of its neurodevelopmental pathophysiology.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — BDNF/neurotrophin PI3K-AKT-mTOR signaling (mTOR, GSK-3β and ERK mapped) supports the neurodevelopmental processes implicated in ADHD.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN regulation of the PI3K-AKT-mTOR axis influences neuronal connectivity and is implicated in neurodevelopmental phenotypes overlapping ADHD.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 reflects the low-grade neuroinflammation increasingly associated with ADHD.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the low-grade inflammatory tone linked to the neurodevelopmental dysregulation of ADHD.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the innate neuroinflammation implicated in the neurodevelopmental component of ADHD.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling transduces the maternal-immune-activation interferon exposure epidemiologically linked to ADHD.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of the PTEN-PI3K-AKT axis (PTEN and AKT already mapped) regulates the neuronal plasticity and oxidative-stress handling relevant to the neurodevelopmental circuitry of ADHD.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the low-grade inflammatory tone associated with ADHD.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to ADHD.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and oxidative-stress adaptation participates in the neurodevelopmental neurobiology of attention-deficit hyperactivity disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the neuronal plasticity of the fronto-striatal circuits implicated in attention-deficit hyperactivity disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of neurodevelopmental gene expression implicated in attention-deficit hyperactivity disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the neurometabolic mechanisms relevant to attention-deficit hyperactivity disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal and synaptic homeostasis implicated in attention-deficit hyperactivity disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the catecholamine-receptor and synaptic signaling implicated in attention-deficit hyperactivity disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with attention-deficit hyperactivity disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuronal migration and neurodevelopmental processes implicated in attention-deficit hyperactivity disorder.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven neuroinflammation participates in the immune-related mechanisms implicated in attention-deficit hyperactivity disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in attention-deficit hyperactivity disorder.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with attention-deficit hyperactivity disorder.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the microglial synaptic remodeling and neuroinflammatory processes implicated in attention-deficit hyperactivity disorder.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Social cognition: oxytocin shapes the social-cognitive and reward circuits implicated in the interpersonal difficulties of ADHD, and is being explored as an adjunct to address social deficits beyond the core dopaminergic symptoms.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Brain renin-angiotensin: central angiotensin II modulates dopaminergic transmission and stress reactivity, a neuroendocrine axis distinct from the catecholamine systems (dopamine already mapped) targeted by stimulants in ADHD.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Hormonal fluctuation: ADHD symptoms in women often worsen when progesterone-derived neurosteroids fall across the menstrual cycle, part of the reproductive-hormone influence (estrogen already mapped) on the disorder's expression.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress reactivity and arousal systems dysregulated alongside the catecholamine deficits of ADHD.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic association: ADHD is associated with higher rates of obesity and insulin resistance, linked partly to impulsive eating and shared dopaminergic (already mapped) reward pathways, a metabolic dimension of the disorder.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Neuroimmune balance: the anti-inflammatory cytokine IL-10 counters the elevated IL-6 and TNF (already mapped) reported in ADHD, part of the low-grade neuroinflammation implicated in a subset of the disorder.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and impulsive eating: ADHD is associated with obesity and disordered eating, and the adipokine leptin, with the shared dopaminergic (already mapped) reward pathways, links the disorder to its metabolic comorbidity (insulin already mapped).
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Metabolic dyslipidaemia: the obesity and metabolic dysregulation (insulin already mapped) more common in ADHD shift cholesterol handling toward an atherogenic profile, part of the cardiometabolic dimension of the disorder.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6, TNF and IL-1 already mapped) implicated in a subset of ADHD modulate the fronto-striatal circuits (dopamine already mapped) of the disorder.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation implicated in a subset of ADHD.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is part of the type-2 response whose balance against the pro-inflammatory signals shapes the neuroinflammatory dimension of ADHD.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and catecholamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), and disturbed copper-zinc (already mapped) balance is reported in ADHD.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic (insulin already mapped) comorbidity reported in ADHD.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the metabolic-inflammatory dimension associated with ADHD.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron-regulatory hormone: hepcidin governs the iron (transferrin and iron already mapped) handling whose disturbance underlies the low-iron state associated with ADHD, affecting the dopamine (already mapped) synthesis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Dopaminergic circuits: the prefrontal-striatal dopaminergic and noradrenergic (already mapped) neurons and their synaptic signalling underlie ADHD, the stimulant (methylphenidate) target.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc cofactor: zinc (a cofactor for the dopamine — already mapped — metabolism and the melatonin — already mapped — pathway) is often low in ADHD, and the supplementation is studied as an adjunct.
- `connects-to` → **[Stimulant use disorder](../stimulant-use-disorder/README.md)** — Substance-use link: ADHD raises the risk of the (stimulant and other) substance use disorder, and the properly treated stimulant medication modifies that risk.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in the neurodevelopment of ADHD.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation (IL-1 and TNF already mapped) associated with ADHD.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of ADHD.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation and the atopy comorbidity associated with ADHD.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension associated with ADHD.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/atopy arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension and the atopy comorbidity associated with ADHD.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the histamine (already mapped) and neuroinflammatory dimension implicated in ADHD.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune dimension of the neuroinflammatory interaction associated with ADHD.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate immune arm: the NK cells (perforin pathway) are part of the peripheral innate-immune dimension of the immune dysregulation reported in ADHD.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the low-grade complement activation of the neuroinflammation implicated in ADHD.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial neuroinflammation implicated in the neurodevelopmental dimension of ADHD.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the neuroinflammation reported in ADHD.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-neuroimmune axis: TSLP, from barrier epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the neuroinflammatory dimension of ADHD.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-neuroinflammation axis: bradykinin, via B1/B2 receptors on microglia (already mapped) and brain endothelium, amplifies the blood-brain-barrier disruption and the neuroinflammatory milieu of ADHD.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective cytokine: erythropoietin, via the EPOR on neurons and microglia (already mapped), modulates the neuronal survival and the neuroinflammatory dimension of the neurodevelopmental disorder of ADHD.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C3/C5 already mapped) whose activation contributes to the neuroinflammatory signalling and synaptic pruning of the neurodevelopmental disorder of ADHD.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Alternative complement regulation: factor H regulates the alternative complement pathway (C3/C5 already mapped) whose dysregulation amplifies the microglial neuroinflammation and synaptic pruning of the neurodevelopmental dimension of ADHD.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Neuroendocrine-immune axis: prolactin, via PRL receptors on microglia (already mapped) and T cells (already mapped), modulates the neuroinflammatory cytokine milieu (dopamine already mapped) of the neurodevelopmental disorder of ADHD.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — ADHD vasopressin: vasopressin, via V1aR on neurons (already mapped) and microglia (already mapped), modulates social-memory and HPA-axis stress; vasopressin dysregulation amplifies the dopamine (already mapped) and norepinephrine (already mapped) executive-dysfunction of ADHD.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — ADHD selenium: selenium, as neuroprotective GPx in neurons (already mapped) and microglia (already mapped), scavenges neuroinflammatory ROS; selenium deficiency impairs the dopamine (already mapped) and norepinephrine (already mapped) neurotransmitter regulation of ADHD.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — ADHD iodine: iodine-dependent thyroid hormones modulate dopaminergic (dopamine already mapped) and noradrenergic (norepinephrine already mapped) tone; iodine deficiency impairs the prefrontal cortex (neurons already mapped) executive function and the attention regulation of ADHD.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — ADHD sodium: high dietary sodium amplifies neuroinflammation in neurons (already mapped) and microglia (already mapped); sodium dysregulation amplifies NF-κB (already mapped) and worsens the dopamine (already mapped) and norepinephrine (already mapped) dysfunction of ADHD.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — ADHD potassium: potassium, via Kv channels on neurons (already mapped), regulates GABAergic interneuron tone; potassium dysregulation amplifies neural excitability and the dopamine (already mapped) and norepinephrine (already mapped) executive-dysfunction cascade of ADHD.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — ADHD phosphorus: phosphorus, as ATP in neurons (already mapped) and astrocytes (already mapped), sustains dopaminergic (dopamine already mapped) neurotransmission; phosphorus deficiency impairs norepinephrine (already mapped) signalling and the prefrontal resilience of ADHD.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — ADHD nitrogen: nitric oxide (NO, nitrogen-derived) in neurons (already mapped) and microglia (already mapped) regulates dopamine (already mapped) neurotransmission; NO dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in ADHD.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — ADHD chloride: chloride channels on neurons (already mapped) and microglia (already mapped) regulate membrane excitability; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) signalling cascade in ADHD.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — ADHD sulfur: sulfur-containing glutathione in neurons (already mapped) and microglia (already mapped) scavenges ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) dysregulation in ADHD.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — carbon-based lipid mediators in neurons (already mapped) support synaptic signalling; disrupted carbon metabolism amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) and BDNF (already mapped) neurodevelopmental dysregulation in ADHD.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — hydrogen ion dysregulation in brain (already mapped) amplifies neurotransmission; proton excess disrupts dopamine (already mapped) and norepinephrine (already mapped) and BDNF (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) neuronal cascade in ADHD.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — ROS from NADPH oxidase in neurons (already mapped) and brain (already mapped) microglia impairs prefrontal circuit function; oxygen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) and BDNF (already mapped) cascade in ADHD.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — ADHD pd-1: PD-1 on t-cytotoxic cells (already mapped) and microglia (already mapped) suppresses neuroimmune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory dopaminergic disruption in ADHD.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — ADHD glp-1: GLP-1 on neurons (already mapped) and astrocytes (already mapped) modulates synaptic energy metabolism; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory dopamine-circuit dysfunction in ADHD.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — ADHD vegf: VEGF from astrocytes (already mapped) and neurons (already mapped) sustains cerebrovascular supply; VEGF deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory dopamine (already mapped) deficit in ADHD.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — ADHD wnt-beta-catenin: WNT/β-catenin on neurons (already mapped) and astrocytes (already mapped) regulates plasticity; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) dopamine-circuit dysfunction in ADHD.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — ADHD rankl: RANKL in microglia (already mapped) and astrocytes (already mapped) modulates neuroinflammatory skewing; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) dopamine-circuit dysfunction in ADHD.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — ADHD smad4: SMAD4 in neurons (already mapped) and astrocytes (already mapped) mediates TGF-β neuroprotection; smad4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) dopamine-circuit dysfunction in ADHD.

[^faraone-2021-adhd-primer]: Faraone SV, Banaschewski T, Coghill D, et al. The World Federation of ADHD International Consensus Statement: 208 Evidence-based conclusions about the disorder. *Neurosci Biobehav Rev.* 2021;128:789-818. [doi:10.1016/j.neubiorev.2021.01.022](https://doi.org/10.1016/j.neubiorev.2021.01.022) · [PubMed 33549739](https://pubmed.ncbi.nlm.nih.gov/33549739/)
[^arnsten-2009-adhd-neuroscience]: Arnsten AF. Toward a new understanding of ADHD pathophysiology: an important role for prefrontal cortex dysfunction. *CNS Drugs.* 2009;23(Suppl 1):33-41. [doi:10.2165/00023210-200923000-00005](https://doi.org/10.2165/00023210-200923000-00005) · [PubMed 19621976](https://pubmed.ncbi.nlm.nih.gov/19621976/)
[^biederman-2005-adhd-adults]: Biederman J, Faraone SV. Attention-deficit hyperactivity disorder. *Lancet.* 2005;366(9481):237-248. [doi:10.1016/S0140-6736(05)66915-2](https://doi.org/10.1016/S0140-6736(05)66915-2) · [PubMed 16023516](https://pubmed.ncbi.nlm.nih.gov/16023516/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
