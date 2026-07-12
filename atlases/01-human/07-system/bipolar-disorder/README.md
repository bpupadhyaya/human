---
schema: human-scale-entry/v1
id: bipolar-disorder
name: Bipolar Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Bipolar disorder (60M affected) causes episodic mania and depression; dopaminergic dysregulation and CLOCK gene variants drive mood cycles; lithium (GSK-3β inhibitor, suicide prevention) is gold-standard mood stabilizer; valproate and quetiapine are alternatives."
aliases: ["bipolar disorder", "bipolar I", "bipolar II", "manic-depressive disorder", "mania", "hypomania", "mood stabilizer", "lithium", "valproate bipolar"]
sources:
  - id: grande-2016-bipolar-review
    type: peer-reviewed
    cite: "Grande I, Berk M, Birmaher B, Vieta E. Bipolar disorder. Lancet. 2016;387(10027):1561-1572."
    doi: "10.1016/S0140-6736(15)00241-X"
    pmid: "26388529"
    url: "https://doi.org/10.1016/S0140-6736(15)00241-X"
    accessed: "2026-06-08"
  - id: geddes-2013-bipolar-treatment
    type: peer-reviewed
    cite: "Geddes JR, Miklowitz DJ. Treatment of bipolar disorder. Lancet. 2013;381(9878):1672-1682."
    doi: "10.1016/S0140-6736(13)60857-0"
    pmid: "23663953"
    url: "https://doi.org/10.1016/S0140-6736(13)60857-0"
    accessed: "2026-06-08"
  - id: cipriani-2013-lithium-suicide
    type: peer-reviewed
    cite: "Cipriani A, Hawton K, Stockton S, Geddes JR. Lithium in the prevention of suicide in mood disorders: updated systematic review and meta-analysis. BMJ. 2013;346:f3646."
    doi: "10.1136/bmj.f3646"
    pmid: "23814104"
    url: "https://doi.org/10.1136/bmj.f3646"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Lithium, the gold-standard mood stabilizer, directly inhibits GSK-3β (uncompetitive Mg²⁺ site); GSK-3β hyperactivity in bipolar drives circadian dysregulation and BDNF suppression; lithium-induced β-catenin stabilization promotes neuroprotection."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Mesolimbic dopamine hyperactivity drives manic symptoms (euphoria, impulsivity, grandiosity, decreased sleep need); antipsychotics (haloperidol, quetiapine, olanzapine) block D2 receptors and reduce acute mania; mesocortical D1 hypofunction may contribute to bipolar depression."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SSRIs can trigger manic switching in bipolar disorder — serotonergic antidepressants are generally used only with mood stabilizer cover; 5-HT2A-blocking atypical antipsychotics (quetiapine) are effective for bipolar depression without switch risk."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF Val66Met SNP is associated with 2× increased bipolar disorder risk; BDNF is reduced during depressive phases; lithium and valproate both upregulate BDNF and BCL-2, promoting hippocampal neurogenesis and neuroprotection — a common mechanism of mood stabilizers."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Valproate (VPA) potentiates GABA-A function and blocks voltage-gated Na⁺/Ca²⁺ channels in bipolar disorder; GABA deficiency in prefrontal cortex is associated with bipolar depression; benzodiazepines provide acute antimanic sedation via GABA-A agonism."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Bipolar disorder features amygdala hyperreactivity and reduced vmPFC regulation; hippocampal volume is reduced ~6% (BD-I); DLPFC shows reduced activation during working memory tasks; lithium partially reverses hippocampal atrophy with long-term use."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Bipolar disorder shares neurodevelopmental genetics with autism: risk loci including SHANK2 and the CACNA1C calcium channel span both (and schizophrenia), and BD occurs more often in autistic people — recasting it as partly a neurodevelopmental, not purely mood, disorder."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Bipolar disorder and schizophrenia share ~70% of their GWAS risk loci and a neurodevelopmental origin: BD-I mania is psychotic in ~60% of episodes, and the two lie on a continuum — a major reason the boundaries between mood and psychotic disorders are blurred."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Bipolar disorder is repeatedly misdiagnosed as major depressive disorder because depressive episodes usually come first — a 7-10 year delay — and treating that depression with an SSRI alone risks flipping into mania, so every depression should be screened for past hypomania."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "Bipolar disorder and BPD are frequently confused: both show mood instability, but bipolar episodes last days-to-weeks and are often unprovoked, while BPD shifts are rapid (hours) and reactive to interpersonal triggers—distinguishing them guides treatment choice."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep is central to bipolar disorder: sleep loss is both a warning sign and a trigger of mania, circadian disruption destabilizes mood, and restoring regular sleep (and chronotherapy) is part of treatment—while many mood stabilizers act partly by normalizing the sleep-wake cycle."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol and other substance use disorders are among the commonest bipolar comorbidities (~40%): patients drink to blunt mania or relieve depression, worsening mood cycling, impulsivity and suicide risk; integrated treatment of both improves outcomes over treating either alone."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Cannabis use disorder is tightly linked to bipolar disorder: among its commonest comorbidities, it can precipitate manic or psychotic episodes and worsens mood-episode frequency and adherence—so heavy use destabilizes bipolar illness and complicates treatment."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety disorders are highly comorbid with bipolar disorder and worsen its course: generalized anxiety predicts more mood episodes and suicidality, and complicates treatment because antidepressants for anxiety can trigger mania—so mood stabilization comes first."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Bipolar disorder involves dysfunction of neurons: disturbed ion-channel, mitochondrial, and BDNF signaling destabilizes neuronal excitability, and lithium's action via GSK-3β inhibition and neuroprotection points to a cellular basis for the illness."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "Bipolar disorder and binge eating disorder are tightly linked: BED is among the commonest eating disorders in bipolar patients, mood episodes drive impulsive eating, and weight gain is compounded by mood-stabilizer side effects—so metabolic monitoring is essential."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Bipolar disorder and PTSD frequently co-occur and worsen each other: childhood trauma raises bipolar risk, comorbid PTSD predicts more mood episodes and suicidality, and overlapping arousal and irritability blur the diagnosis—so trauma history shapes bipolar care."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "Bipolar disorder and anorexia nervosa overlap more than expected: mood instability is common in eating disorders, the two share genetic risk, and bipolar episodes can drive weight and appetite swings—so screening for an eating disorder is part of bipolar assessment."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Bipolar disorder involves glutamatergic dysfunction: abnormal excitatory signaling contributes to mood episodes, and rapid-acting ketamine (an NMDA-glutamate antagonist) can lift bipolar depression—evidence that glutamate, not just monoamines, shapes the illness."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Bipolar disorder is deeply tied to the body clock and melatonin: circadian disruption and altered melatonin rhythms can trigger mood episodes, sleep loss often precedes mania, and stabilizing sleep-wake and light exposure is a core part of management."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Bipolar disorder is a brain-wide disturbance of mood regulation: it reflects dysfunction across prefrontal-limbic networks of the nervous system rather than one region, producing the swings between mania and depression that define this highly heritable illness."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid and bipolar disorder are intertwined: hypothyroidism can mimic or trigger depression and rapid cycling, and lithium—a mainstay treatment—commonly causes hypothyroidism, so thyroid function is checked before and during mood-stabilizer therapy."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Lithium's benefit comes at a renal cost: long-term use can cause nephrogenic diabetes insipidus and slowly progressive chronic kidney disease, so kidney function and lithium levels are monitored for life—balancing the most effective mood stabilizer against renal harm."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium signaling sits at bipolar disorder's genetic core: CACNA1C, encoding a calcium channel, is among the strongest risk genes, implicating disturbed neuronal calcium handling in how mood episodes arise and why lithium acts on this system."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Bipolar disorder's mood stabilizers act on sodium and its kin: lithium is a sodium-like ion that substitutes for it in neurons, while valproate and lamotrigine block sodium channels—so monovalent-cation and ion-channel biology underlies calming the manic brain."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Bipolar disorder carries a neuroinflammatory signature in microglia: activated brain microglia and raised inflammatory markers accompany mood episodes, supporting an inflammation hypothesis and interest in anti-inflammatory adjuncts."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Mania is in part a catecholamine surge: excess norepinephrine (with dopamine) drives the energy, reduced sleep need, and racing activity of manic episodes, which is why noradrenergic stimulants can trigger mania and why dampening it helps treat it."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Bipolar disorder dysregulates the stress hormone: an overactive HPA axis raises cortisol, and the resulting stress sensitization can kindle mood episodes, while high cortisol also contributes to the cognitive and metabolic toll of the illness."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Bipolar disorder shows up in the brain's white matter: oligodendrocyte and myelin abnormalities disrupt the connections between mood-regulating regions, one of the more consistent neuroimaging findings in the disorder."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Bipolar disorder can shrink the hippocampus: recurrent episodes and high cortisol are linked to reduced hippocampal volume and impaired plasticity, a change lithium and mood stabilizers may partly protect against."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Bipolar disorder is entangled with the thyroid: an underactive thyroid can mimic or trigger depression and rapid cycling, and lithium itself often causes hypothyroidism, so thyroid function is checked and corrected throughout treatment."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Bipolar disorder involves more than neurons—astrocytes too: these glial cells recycle glutamate and support brain metabolism, and their dysfunction may unbalance the excitatory signaling that swings between mania and depression."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Bipolar disorder may be an energy disorder: studies find mitochondrial dysfunction and low brain ATP, so faltering cellular energy is a leading hypothesis for why mood and activity destabilize and why metabolism is altered."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Brain imaging shows bipolar's signature: MRI reveals white-matter abnormalities and fMRI altered amygdala-prefrontal activity, and lithium treatment even slightly increases gray-matter volume on scans."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Bipolar disorder dysregulates synaptic plasticity: lithium and mood stabilizers act on cascades like GSK-3β that remodel synapses, stabilizing the circuits that swing between mania and depression."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Bipolar drugs tax the liver: valproate and carbamazepine are metabolized there and can be hepatotoxic, so liver-function monitoring is part of long-term mood-stabilizer treatment."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy points to bipolar's energy crisis: studies find abnormal, dysfunctional mitochondria in the neurons, fueling the leading hypothesis that faulty cellular energy production underlies the swings between mania and depression."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Bipolar disorder shortens life through the heart: cardiovascular disease is its leading cause of early death, driven by chronic stress, metabolic side effects of medication, and the lifestyle toll of the illness."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium echoes lithium's calming effect: it modulates the same neuronal signaling and calcium handling, and low levels are tied to mania, so magnesium has been studied as an adjunct mood stabilizer."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "A mood stabilizer can blister the skin: lamotrigine carries a risk of Stevens-Johnson syndrome and toxic epidermal necrolysis, which is why it must be titrated up slowly and stopped at the first rash."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Treatment can inflame and unbalance the pancreas: valproate is a recognized cause of acute pancreatitis, while the antipsychotics often added drive weight gain and insulin resistance toward diabetes."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Bipolar drugs reach the reproductive tract: valproate causes polycystic ovary syndrome and, like lithium, is teratogenic — valproate with neural tube defects, lithium with the heart's Ebstein anomaly — complicating treatment in pregnancy."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Mood episodes carry an inflammatory signature: IL-6 and other cytokines rise during mania and depression, supporting a neuroinflammation model in which immune activation feeds the brain changes of bipolar disorder."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "The heart is the leading killer in bipolar disorder: chronic stress, inactivity, and the weight and metabolic effects of mood stabilizers and antipsychotics drive cardiovascular disease that shortens lifespan by over a decade."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Lithium and the gut-brain axis meet in the bowel: lithium commonly causes diarrhea that limits its dose, and the microbiome-gut-brain signaling implicated in mood adds another layer linking the gut to bipolar disorder."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Bipolar disorder and obesity feed each other: lithium, valproate, and antipsychotics drive weight gain while shared inflammation and inactivity push toward metabolic syndrome, making obesity one of its most common comorbidities and complicating drug choice."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The stress axis runs hot in mood episodes: bipolar disorder is marked by HPA-axis dysregulation, the adrenal glands oversecreting cortisol in both depression and mania, a disturbance that tracks with relapse and cognitive impairment."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Mania carries an inflammatory flush: TNF-α and other cytokines rise during acute episodes and settle with remission, part of the neuroinflammatory signature increasingly tied to bipolar disorder's course."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Body and mind share the burden: bipolar disorder carries a high rate of type 2 diabetes, driven both by the illness's metabolic biology and by the weight-gaining mood stabilizers and antipsychotics used to treat it."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The body's cannabis system sways mood: endocannabinoid signaling modulates the emotion and reward circuits disturbed in bipolar disorder, a link reflected in the high rate of cannabis use and its effect on episodes."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Peripheral immunity shifts with the mood state: altered helper T-cell profiles accompany mania and depression, extending bipolar's neuroinflammatory signature beyond the cytokines into the adaptive immune system."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Mood episodes ride a wave of inflammation: NF-κB activation drives the cytokine surges seen in mania and depression, the transcriptional engine behind bipolar's well-documented neuroinflammatory signature."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "It shortens life through the heart: bipolar disorder carries markedly elevated cardiovascular mortality, with chronic inflammation, metabolic side effects of medication and lifestyle accelerating atherosclerosis decades early."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its mainstay drug can scar the kidneys: years of lithium therapy cause nephrogenic diabetes insipidus and chronic interstitial nephritis, so long-term treatment carries a real risk of chronic kidney disease."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its cardiovascular toll reaches the brain: the accelerated atherosclerosis, metabolic syndrome and chronic inflammation of bipolar disorder raise the long-term risk of ischemic stroke beyond that of the general population."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Decades of metabolic strain wear on the heart: obesity, diabetes and the cardiometabolic effects of mood-stabilizing and antipsychotic drugs in bipolar disorder contribute to ischemic and structural heart disease and heart failure."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Mood and headache cycles intertwine: migraine is strongly comorbid with bipolar disorder, especially the bipolar II and depressive subtypes, sharing serotonergic and neuronal-excitability mechanisms."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Its mood stabilizer can flare the skin: lithium, a cornerstone of bipolar treatment, characteristically triggers or worsens psoriasis, sometimes forcing a change of therapy."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Heavy smoking scars the lungs: very high smoking rates in bipolar disorder drive chronic obstructive pulmonary disease, a major contributor to the reduced life expectancy in this population."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Mood instability and chronic pain overlap: bipolar disorder is markedly comorbid with fibromyalgia, sharing disturbances in sleep, stress reactivity and central pain and monoamine signaling."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its mainstay drug disturbs the glands: lithium commonly causes hypothyroidism and hyperparathyroidism, and thyroid dysfunction itself precipitates mood episodes, tightly linking bipolar disorder to the endocrine system."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its mood stabilisers can injure the gut and liver: valproate causes hepatotoxicity and pancreatitis, and lithium and other agents bring nausea and diarrhoea that complicate long-term treatment."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Anxiety rides alongside the mood swings: panic disorder is highly comorbid with bipolar disorder, worsening its course and complicating treatment, as antidepressants risk destabilising mood."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its mood stabiliser can damage the kidney: long-term lithium causes nephrogenic diabetes insipidus and a chronic interstitial nephritis that can slowly progress to chronic kidney disease, requiring regular monitoring."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its drugs reach the skin: lamotrigine can trigger Stevens-Johnson syndrome and toxic epidermal necrolysis, while lithium can aggravate psoriasis and acne."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Inflammation tracks its episodes: bipolar disorder is associated with raised inflammatory markers during mood episodes, supporting a neuroinflammatory component to its biology."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Both the illness and its drugs weaken bone: sedentary depressive phases and some psychotropics are linked to lower bone density and a higher fracture risk."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Heavy smoking shadows the illness: far higher smoking rates in bipolar disorder drive COPD and respiratory disease, compounding its cardiovascular mortality gap."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "Antidepressants are double-edged here: an SSRI like fluoxetine can flip a patient into mania or rapid cycling if given without a mood stabiliser, though fluoxetine-olanzapine is approved for bipolar depression."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "A latent parasite linked to mood: chronic Toxoplasma gondii infection is epidemiologically associated with bipolar disorder and higher suicide risk, possibly by altering brain dopamine."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet is studied as an adjunct: omega-3 supplementation shows modest benefit for bipolar depression in some trials, added to but not replacing mood stabilisers."
  - target: 03-medicine/02-traditional/st-johns-wort
    relation: connects-to
    note: "A herbal antidepressant that can destabilise it: St John's wort, taken for depression, can trigger mania or rapid cycling in undiagnosed bipolar disorder and interferes with mood-stabiliser metabolism."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "It raises later dementia risk: bipolar disorder is linked to a higher incidence of dementia including Alzheimer's, and intriguingly its mainstay lithium is studied as a neuroprotective agent that may lower that risk."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Stimulants and mania entangle: substance and stimulant use is highly comorbid with bipolar disorder, can precipitate or mimic manic episodes, and worsens its course and treatment response."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "White-matter wiring is disturbed: bipolar disorder shows reduced white-matter integrity and altered axonal connectivity between mood-regulating regions, part of the neuroprogression seen over repeated episodes."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Shared drugs and excitability: valproate, lamotrigine and carbamazepine are anticonvulsants that double as mood stabilisers, reflecting overlapping neuronal-excitability and kindling models of bipolar disorder and epilepsy."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Lithium taxes the kidney: long-term lithium for bipolar disorder causes chronic interstitial nephropathy and nephrogenic diabetes insipidus, slowly impairing the kidney and scarring the glomeruli over decades of use."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "A comorbid mood-anxiety overlap: bipolar disorder and obsessive-compulsive disorder co-occur often, and antidepressants for OCD can destabilise mood into mania, complicating treatment of the pair."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "A shared dopamine thread: bipolar disorder is associated with a higher later risk of Parkinson's disease, the dopaminergic surges of mania mirroring, in reverse, the dopamine loss of Parkinson's."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Mood-stabiliser cardiac effects: lithium and the antipsychotics used in bipolar disorder can disturb the cardiac conduction system—QT prolongation, bradycardia and arrhythmia—requiring ECG monitoring."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "Mood disorder in CNS disease: bipolar disorder occurs more often in multiple sclerosis, arising both from demyelinating lesions and from corticosteroid treatment, blurring primary and secondary mania."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Lithium and the parathyroids: long-term lithium therapy for bipolar disorder raises parathyroid hormone and causes hypercalcaemia, a recognised endocrine complication alongside its thyroid and kidney effects."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Mood under the pandemic: COVID-19 disrupted bipolar care and sleep-wake routines that trigger episodes, while severe infection and its neuroinflammation can precipitate mania or depression."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "The cardiovascular mortality gap: bipolar disorder roughly doubles cardiovascular death through metabolic, behavioural and treatment factors, straining the myocardium and shortening life expectancy."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory mood: IL-1β rises during mood episodes in bipolar disorder, part of the neuroinflammatory signature increasingly tied to its episodic, progressive course."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: stress and metabolic dysfunction activate the NLRP3 inflammasome in bipolar disorder, releasing IL-1β to drive the low-grade neuroinflammation linked to the illness."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Cholinergic-aminergic balance: the classic theory of bipolar disorder pits cholinergic against adrenergic tone, with cholinergic excess favouring depression and aminergic dominance favouring mania."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcium-signalling risk: the CACNA1C calcium-channel variant is the strongest genetic hit in bipolar disorder, dysregulating the calcium-calcineurin signalling that controls neuronal excitability and plasticity."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "Serotonergic vulnerability: serotonin-transporter function shapes the depressive pole of bipolar disorder and antidepressant response, though SSRIs risk triggering mania without a mood stabiliser."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Neuroplasticity signalling: mTOR-dependent synaptic plasticity is implicated in bipolar mood switching, and rapid-acting agents like ketamine act partly through this pathway."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Circadian triggering: orexin-driven sleep-wake and circadian dysregulation is central to bipolar disorder, where sleep loss reliably precipitates mania and circadian disruption tracks mood episodes."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophic plasticity: BDNF signalling through TrkB mediates the synaptic plasticity disrupted in bipolar disorder, and the neurotrophic action of lithium and valproate works partly through this BDNF-TrkB axis."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormonal mood modulation: estrogen influences monoaminergic systems, and bipolar mood episodes cluster around postpartum, perimenstrual and perimenopausal hormonal shifts, especially in rapid-cycling disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium-channel genetics: the L-type calcium channel gene CACNA1C is among the strongest and most replicated genetic risk factors for bipolar disorder, implicating dysregulated neuronal calcium signalling in the disease's pathophysiology."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Lithium signalling: lithium inhibits GSK-3β, disinhibiting Wnt/β-catenin signalling, and this pathway is one proposed route by which the prototypical mood stabiliser exerts its neuroprotective and mood-balancing effects in bipolar disorder."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic comorbidity: insulin resistance is common in bipolar disorder and associated with a more chronic, treatment-resistant course, part of the bidirectional link between metabolic dysfunction and mood that shapes long-term outcome."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Lithium target axis: the AKT-GSK3β pathway (GSK3β already mapped, the lithium target) is central to the mood-stabilising and neuroprotective signalling whose dysregulation is implicated in bipolar disorder."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Neuroplasticity signalling: neurotrophin-driven ERK-MAPK signalling, enhanced by lithium and valproate, supports the neuroplasticity and neuroprotection whose deficit is implicated in bipolar disorder."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "HPA dysregulation: altered glucocorticoid-receptor feedback (cortisol already mapped) is a consistent finding in bipolar disorder, linking HPA-axis stress physiology to the onset of mood episodes."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Stress trigger: heightened CRH-driven HPA activity (cortisol and the glucocorticoid receptor mapped) precedes and precipitates mood episodes in bipolar disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Lithium signalling node: PI3K-AKT-GSK3β-mTOR signalling (AKT, GSK-3β and mTOR mapped) is the intracellular cascade through which lithium and neurotrophins modulate the neuroplasticity disrupted in bipolar disorder."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Neuroinflammation: TLR-MyD88 signalling contributes to the low-grade neuroinflammation (IL-1β, IL-6 and TNF mapped) increasingly linked to the mood episodes of bipolar disorder."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative stress with impaired NRF2 antioxidant defence is a consistent feature of bipolar disorder, linked to its mitochondrial dysfunction."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 reflects the neuroinflammatory activation increasingly implicated in the mood episodes of bipolar disorder."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-driven JAK-STAT signalling (IL-6 mapped) transduces the systemic inflammation associated with bipolar disorder."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling (JAK1/2 already mapped) transduces the inflammatory tone implicated in the neuroprogression of bipolar disorder."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Mitochondrial dysfunction in bipolar disorder releases cytosolic DNA that can engage cGAS-STING, linking bioenergetic stress to its neuroinflammation."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the interferon-associated inflammatory component reported in mood episodes of bipolar disorder."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of the PI3K-AKT-GSK-3β axis (AKT, PIK3CA, and the lithium target GSK-3β already mapped) regulates neuronal resilience and oxidative-stress handling implicated in bipolar disorder."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to mood episodes in bipolar disorder."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked mitochondrial and metabolic dysfunction is implicated in the bioenergetic dysregulation of bipolar disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, coupled to mitochondrial energetics (mTOR already mapped), participates in the bioenergetic dysfunction implicated in bipolar disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of neuronal gene expression associated with bipolar disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy, induced by the mood stabilizer lithium, participates in the neuroprotective mechanisms relevant to bipolar disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the synaptic and neurotrophin signaling relevant to bipolar disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammatory component of bipolar disorder."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-p53 signaling participates in the cellular-resilience and neuroplasticity mechanisms modulated by mood stabilizers in bipolar disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and neuroplasticity processes implicated in bipolar disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory responses implicated in bipolar disorder."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with bipolar disorder."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neurodevelopmental gene programs implicated in bipolar disorder."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the neuromodulation and sleep-circadian processes implicated in bipolar disorder."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the microglial and neuroinflammatory processes implicated in bipolar disorder."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Purinergic mania: elevated uric acid produced by xanthine oxidase is associated with manic episodes, and the xanthine-oxidase inhibitor allopurinol has shown antimanic effects, supporting a purinergic dimension (adenosine already mapped) of bipolar disorder."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic comorbidity: bipolar disorder carries a heavy burden of obesity and metabolic syndrome, worsened by mood stabilisers and antipsychotics, and leptin dysregulation links the affective illness to its cardiometabolic morbidity."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitrosative stress: increased nitric oxide and nitrosative stress accompany mood episodes in bipolar disorder, contributing to the mitochondrial and neuronal dysfunction implicated in its pathophysiology."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Reproductive-cycle mood: mood episodes in bipolar disorder cluster around the perinatal period and menstrual cycle, implicating progesterone and its neurosteroid metabolites, alongside estrogen (already mapped), in the hormonal triggering of episodes."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Stress reactivity: central angiotensin II modulates stress responses and interacts with the HPA axis (cortisol already mapped), a neuroendocrine system implicated in the stress sensitivity that precipitates mood episodes in bipolar disorder."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response and mood regulation dysregulated in bipolar disorder."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6, TNF and IL-1 already mapped) implicated in bipolar disorder modulate the mood circuits, part of the inflammatory neuroprogression of the illness."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Lithium diabetes insipidus: chronic lithium induces resistance to vasopressin in the kidney (already mapped), causing nephrogenic diabetes insipidus with polyuria, and vasopressin also participates in the HPA stress axis dysregulated in bipolar disorder."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic syndrome: bipolar disorder and its antipsychotic and mood-stabiliser treatment promote an atherogenic dyslipidaemia (insulin and leptin already mapped), part of the metabolic syndrome that raises its cardiovascular mortality."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4 counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation reported in bipolar disorder, particularly during mood episodes."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and mood: zinc modulates the glutamatergic (already mapped) NMDA signalling, and low zinc status is reported in the depressive episodes of bipolar disorder, part of its trace-metal dimension."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and monoamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), and disturbed copper-zinc (already mapped) balance is reported in the mood episodes of bipolar disorder."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histaminergic arousal: the H1/H3 histaminergic modulation of the arousal and the sleep-wake cycle (orexin and melatonin already mapped) is disturbed in the mood episodes of bipolar disorder, and H1-active drugs affect its course."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-syndrome (insulin and cholesterol already mapped) comorbidity of bipolar disorder and its treatments."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the metabolic comorbidity of bipolar disorder."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is the type-2 immune arm of the neuroinflammation (TNF and IL-6 already mapped) implicated in bipolar disorder."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Neuronal excitability: the neuronal excitability and the ion-channel (CACNA1C calcium) dysregulation and the mitochondrial (ATP already mapped) dysfunction of the neurons underlie the mood episodes of bipolar disorder."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Metabolic comorbidity: bipolar disorder carries a high type 2 diabetes and metabolic-syndrome (insulin and cholesterol already mapped) risk, worsened by the antipsychotics (leptin and adiponectin already mapped)."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in the mood episodes of bipolar disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation associated with bipolar disorder, more prominent in the manic episodes."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of bipolar disorder."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of bipolar disorder."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension associated with bipolar disorder."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of bipolar disorder."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the type-2 (IgE already mapped) dimension implicated in bipolar disorder."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the mood episodes of bipolar disorder."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Stress-modulated NK: the NK-cell number and cytotoxicity, altered by the stress and cortisol (already mapped) reactivity, are part of the peripheral immune dysregulation of bipolar disorder."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the low-grade complement activation of the neuroinflammation implicated in bipolar disorder."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) neuroinflammation implicated in the mood episodes of bipolar disorder."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the low-grade neuroinflammation of bipolar disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-neuroinflammatory axis: TSLP, from epithelial barriers, primes mast cells (already mapped) and dendritic cells (already mapped) and amplifies the Th17 (already mapped) neuroinflammatory bias implicated in the mood episodes of bipolar disorder."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-neuroinflammatory axis: bradykinin, via B2R on CNS microglia (already mapped) and endothelium (already mapped), amplifies the BBB permeability and the neuroinflammation contributing to the mood episodes of bipolar disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3 and C5 already mapped) contributing to the synaptic pruning excess and the neuroinflammation of the mood episodes of bipolar disorder."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM remodelling in mood circuits: periostin, expressed by astrocytes (already mapped) and microglia (already mapped), modulates the perineuronal net matrix in limbic circuitry and contributes to the synaptic dysregulation underlying mood episodes of bipolar disorder."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective cytokine: erythropoietin, via EPOR on neurons (already mapped) and astrocytes (already mapped), promotes neuronal survival, limits the neurotoxic cytokine burden (TNF-α and IL-6 already mapped) and attenuates the hippocampal volume loss of bipolar disorder."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Antipsychotic-immune axis: prolactin, elevated by antipsychotic medications used in BD (dopamine already mapped), modulates T-cell (already mapped) and NK-cell (already mapped) immune function and contributes to the metabolic side-effect burden of bipolar disorder."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "BD testosterone: testosterone, via androgen receptors on neurons (already mapped), suppresses NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation; androgen deficiency amplifies the complement-C5 (already mapped)-mediated mood-circuit synaptic-pruning excess of BD."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "BD oxytocin: oxytocin, via OXTR on neurons (already mapped), modulates the dopamine (already mapped)/serotonin (already mapped) mood circuitry and neuroplasticity; oxytocin deficiency amplifies NF-κB (already mapped) neuroinflammation and BDNF (already mapped) deficit of BD."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "BD selenium: selenium, via GPx and thioredoxin reductase, protects neurons (already mapped) from oxidative injury; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory burden and the mood-episode severity of bipolar disorder."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "BD iodine: iodine-dependent thyroid hormones regulate neuronal (neuron already mapped) metabolism and hippocampal (already mapped) plasticity; hypothyroidism, common in BD, amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and mood-episode severity."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "BD potassium: potassium efflux activates NLRP3 inflammasome (already mapped) in microglia (already mapped); disrupted K⁺ and Na+ (sodium already mapped) homeostasis at synapses (already mapped) amplifies NF-κB (already mapped) and IL-1β (already mapped) neuroinflammation in BD."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "BD iron: iron is required for dopamine (already mapped) and serotonin (already mapped) synthesis; iron deficiency impairs hippocampal (already mapped) neuronal (neuron already mapped) energy and worsens the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation in BD."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "BD phosphorus: phosphorus fuels neuron (already mapped) and synapse (already mapped) ATP; phosphorus deficiency impairs dopamine (already mapped) and serotonin (already mapped) synthesis and amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation in BD."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "BD nitrogen: nitric oxide (NO, nitrogen-derived) in neurons (already mapped) and microglia (already mapped) amplifies neuroinflammation; NO excess upregulates NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) worsening serotonin (already mapped) in BD."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "BD chloride: chloride channels on neurons (already mapped) and microglia (already mapped) regulate excitability; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) and serotonin (already mapped) signalling in BD."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "BD sulfur: sulfur-containing glutathione in neurons (already mapped) and microglia (already mapped) scavenges ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) and BDNF (already mapped) dysregulation in BD."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "carbon-based organic acids in neurons (already mapped) fuel mitochondrial energy; disrupted carbon metabolism amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) and serotonin (already mapped) mood cascade in bipolar disorder."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "hydrogen ion dysregulation in brain (already mapped) amplifies mood circuit excitability; proton excess disrupts dopamine (already mapped) and serotonin (already mapped) and BDNF (already mapped) and IL-6 (already mapped) neuroinflammatory cascade in bipolar disorder."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "ROS from NADPH oxidase in neurons (already mapped) and microglia (already mapped) amplifies brain (already mapped) neuroinflammation; oxygen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade in bipolar disorder."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "BD pd-1: PD-1 on t-cytotoxic cells (already mapped) and microglia (already mapped) suppresses neuroimmune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory mood-cycling cascade in BD."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "BD glp-1: GLP-1 on neurons (already mapped) and astrocytes (already mapped) modulates synaptic energy metabolism; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory mood-cycling dysfunction in BD."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "BD vegf: VEGF from astrocytes (already mapped) and neurons (already mapped) sustains cerebrovascular supply; VEGF deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory mood dysregulation in BD."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "BD rankl: RANKL in microglia (already mapped) and astrocytes (already mapped) modulates neuroimmune skewing; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory mood-cycling cascade in BD."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "BD smad4: SMAD4 in neurons (already mapped) and astrocytes (already mapped) mediates TGF-β neuroprotection; smad4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) mood-cycling cascade in BD."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "BD il-2: IL-2 from T-helper cells (already mapped) and microglia (already mapped) modulates neuroimmune balance; IL-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory mood-cycling cascade in BD."
---

# Bipolar Disorder

## Overview

**Bipolar disorder (BD)** is a chronic, episodic mood disorder characterized by alternating periods of **mania** (or hypomania in BD-II) and **depression**, with periods of euthymia between episodes. It affects approximately **60 million people** worldwide (~1–2% lifetime prevalence) across all cultures and socioeconomic strata [^grande-2016-bipolar-review]. It ranks among the top 10 causes of global disability, with the highest years-lived-with-disability burden occurring in young adults during their most productive decades.

Bipolar disorder is often underdiagnosed — the average time from first symptom to correct diagnosis is **7–10 years**, frequently because depressive episodes present first and are mistakenly treated as unipolar depression (risking SSRI-induced manic switching). When correctly diagnosed and treated, most patients can achieve sustained mood stability, though the condition remains lifelong.

**Key clinical dimensions:**
- **BD-I**: Full manic episodes (≥7 days or requiring hospitalization), with or without depression — most severe form; associated with psychosis during mania in ~60%
- **BD-II**: Hypomanic episodes (≥4 days, no hospitalization) + major depressive episodes — often initially misdiagnosed as MDD; depression predominates; high suicide risk
- **Cyclothymia**: Subthreshold hypomanic and depressive symptoms for ≥2 years
- **BD-NOS/Other specified**: Rapid cycling (≥4 episodes/year); mixed features (simultaneous manic + depressive symptoms — highest suicide risk)

**Suicide:** BD carries the **highest suicide rate** of any psychiatric disorder — 15-fold higher than the general population; 25–50% of patients attempt suicide. Lithium is the only medication with Level 1 evidence for **suicide prevention** (Cipriani 2013) [^cipriani-2013-lithium-suicide], through mechanisms beyond mood stabilization (possibly NF-κB → neuroinflammation suppression, GSK-3β → apoptosis inhibition).

## Structure

### DSM-5 diagnostic criteria

**Manic episode** (DSM-5, required for BD-I diagnosis):
- ≥7 days (or any duration if hospitalization required or psychosis present) of persistently elevated, expansive, or irritable mood AND increased goal-directed activity/energy
- ≥3 of (DIGFAST): **D**istractibility, **I**mpulsivity/reckless behavior, **G**randiosity, **F**light of ideas, **A**ctivity increase, **S**leep decreased, **T**alkativeness/pressured speech

**Hypomanic episode** (BD-II): same symptom criteria but ≥4 days, not severe enough for hospitalization, no psychosis, and a marked functional change observable by others (not just self-reported)

**Major depressive episode**: same criteria as MDD (5/9 SIG E CAPS for ≥2 weeks)

**Specifiers relevant to treatment:**
- **Mixed features**: ≥3 symptoms of opposite polarity during current episode → highest suicide risk; lithium + quetiapine recommended; antidepressants contraindicated
- **Rapid cycling**: ≥4 distinct mood episodes/year → valproate + atypical antipsychotics; lithium less effective; rule out thyroid dysfunction and substance use
- **With psychotic features**: Typically mood-congruent (grandiosity in mania; guilt/nihilism in depression); olanzapine or aripiprazole often added
- **With anxious distress**: Very common; higher suicidality; benzodiazepines adjunctive

### Neurobiology of bipolar mood cycling

**Circadian system dysregulation:**
- **CLOCK gene** (CLOCK, ARNTL/BMAL1, PER3, CRY1/2) variants are the most consistently associated with BD across GWAS; ~50% of circadian genes are GSK-3β substrates
- GSK-3β phosphorylates CLOCK → period lengthening; PER2 → degradation; REV-ERBα → destabilization
- BD patients show reduced sleep need in mania, hypersomnia in depression, irregular sleep-wake cycles, and phase shifts — all consistent with circadian clock pathology
- Lithium lengthens circadian period (via GSK-3β inhibition) and stabilizes amplitude — likely contributing to mood stabilization

**Monoamine dysregulation:**
- **Mania:** Mesolimbic dopamine hyperactivity (D2/D3 hypersensitivity) → reward overdrive, euphoria, impulsivity, reduced sleep need; dopamine release from VTA to NAc is pathologically increased
- **Depression:** Relative hyperdopaminergic tone withdrawn; norepinephrine and serotonin deficit similar to MDD; mesocortical hypodopaminergia impairs PFC executive function
- Catecholamine hypothesis: mania = catecholamine excess; depression = catecholamine deficit (bidirectional oscillation driven by homeostatic counter-regulation and receptor downregulation/upregulation cycles)

**Intracellular signaling:**
- **GSK-3β hyperactivity**: Directly supported by postmortem studies (reduced Ser9-phosphorylated/inactivated GSK-3β in frontal cortex); lithium's clinical efficacy proportional to GSK-3β inhibition
- **IP3/DAG/PKC pathway**: Myo-inositol depletion by lithium reduces PKC-mediated signal amplification in neurons; carbamazepine similarly depletes DAG
- **Mitochondrial dysfunction**: BD shows reduced Complex I activity in postmortem brain; mitochondrial haplogroups associated with BD; N-acetylcysteine (antioxidant) shows efficacy in bipolar depression trials
- **Neuroinflammation**: TNF-α, IL-6, and CRP are elevated during mood episodes; normalized with lithium and quetiapine; shared with MDD biology but more episodic

**Genetics:**
- Heritability: ~70–80% (among highest in psychiatry)
- Twin concordance: monozygotic ~45%, dizygotic ~10%
- BD-I and schizophrenia share significant genetic overlap (GWAS; ~70% overlapping loci); BD is not merely a mood disorder — it represents a neurodevelopmental spectrum overlapping schizophrenia
- Key GWAS loci: CACNA1C (L-type Ca²⁺ channel — voltage-gated Ca²⁺ entry; convergence with migraine and schizophrenia), SHANK2 (synaptic scaffold; also autism), ANK3 (ankyrin G — Nav channel anchoring), TRANK1, and CLOCK pathway genes
- BDNF Val66Met: associated with earlier illness onset and increased depressive episodes in BD

## Function

### Manic episode biology

During acute mania, the following neurobiological cascade unfolds:

1. **Mesolimbic DA hyperactivation:** VTA → NAc dopamine surge → reward hypersensitivity → goal-directed behavior amplified → impulsivity (temporal discounting shifts toward immediate reward)
2. **NE/CORT surge:** Sympatho-adrenal activation → decreased sleep need (patients often sleep 0–2h without fatigue) → NE → LC hyperactivation → arousal
3. **Reduced vmPFC-amygdala control:** Elevated dopamine in PFC paradoxically impairs executive control (inverted U-curve of D1 receptor stimulation) → impulsivity, poor insight
4. **Circadian disruption:** CLOCK gene phase advance → sleep-wake cycle compression → positive feedback with mood elevation

### Bipolar depression biology

During bipolar depression (often longer and more disabling than mania):
- Reduced mesolimbic and mesocortical dopamine → anhedonia, psychomotor retardation, cognitive slowing
- Reduced serotonin → depressed mood, suicidality (similar to MDD)
- HPA dysregulation: unlike PTSD (hypocortisolemia) and MDD (hypercortisolemia) — BD shows mixed: elevated cortisol in acute depression but blunted diurnal rhythm; cortisol normalization correlates with mood recovery
- BDNF reduced in depressive episodes; restored with successful treatment

## Pathology

### Treatment

**Acute mania:**
- **Lithium** (serum target 0.8–1.2 mEq/L): effective for acute mania (~70% response); IV not available; takes 5–7 days for full effect; always combine with antipsychotic acutely
- **Atypical antipsychotics**: haloperidol (fastest), olanzapine, aripiprazole, risperidone, quetiapine — primary acute antimanic agents; D2 blockade rapidly reduces dopamine-driven mania within days
- **Valproate** (VPA): IV loading possible for rapid control; good for mixed features, rapid cycling, dysphoric mania; antimanic onset ~5 days; teratogenic
- **Benzodiazepines**: Lorazepam or clonazepam for behavioral control, sleep, anxiety — adjunctive; short-term only

**Bipolar depression (most challenging aspect):**
- **Quetiapine (Seroquel)**: FDA-approved for bipolar depression; 5-HT2A/D2 blockade + serotonergic modulation; 300–600 mg QD; most evidence
- **Lurasidone**: FDA-approved; good for bipolar depression with anxiety; weight-neutral
- **OFC (olanzapine-fluoxetine combination)**: FDA-approved; significant weight gain
- **Lamotrigine**: Excellent for bipolar depression prevention; slow titration required (Stevens-Johnson risk); not effective for acute mania
- **Lithium**: Effective for bipolar depression (add-on); also suicide prevention
- **Ketamine**: Emerging rapid-acting treatment for bipolar depression (IV racemic, intranasal esketamine); NMDA antagonism → rapid BDNF/mTOR-mediated synaptogenesis; mania switch risk with repeated use is low in current trials but monitoring required
- **SSRIs**: Generally avoided as monotherapy in BD — risk of manic switching; if used, always with mood stabilizer; evidence base weaker than in MDD

**Long-term maintenance (prevention of recurrence):**

| Drug | Best for | Key advantages | Key risks |
|:---|:---|:---|:---|
| **Lithium** | BD-I, suicide prevention, long-term stability | Only drug with Level 1 suicide prevention evidence; reduces BD mortality | Narrow TI (0.6–1.2 mEq/L); renal toxicity; thyroid dysfunction; teratogen; requires monitoring |
| **Valproate** | Mixed features, rapid cycling, mania prevention | Broader spectrum than lithium for cycling | Teratogenic (neural tube defects); PCOS; hepatotoxicity |
| **Lamotrigine** | Bipolar depression prevention, BD-II | No weight gain; depression focus; well-tolerated | Slow titration; Stevens-Johnson; poor acute mania efficacy |
| **Quetiapine** | Both poles; agitation | FDA-approved for all phases; sedating (useful for sleep) | Metabolic syndrome; tardive dyskinesia risk |
| **Aripiprazole** | BD-I maintenance; weight-neutral | Partial D2 agonist; low metabolic risk | Akathisia; activation can worsen agitation |
| **Long-acting injectable antipsychotics** | Non-adherence (major cause of relapse) | Bypasses daily pill adherence | Injection site reactions; metabolic effects |

**Lithium's unique properties:**
- Only mood stabilizer proven to reduce suicide attempts and completions (Cipriani 2013, meta-analysis)
- Neuroprotective: increases gray matter volume, preserves hippocampal volume, promotes neurogenesis
- Anti-inflammatory: reduces TNF-α, IL-6, NF-κB
- Telomere preservation: BD associated with accelerated telomere shortening; lithium attenuates this
- Long-term lithium users have lower rates of dementia — likely via GSK-3β → reduced tau pathology

**Psychosocial interventions (essential, evidence-based):**
- Psychoeducation: understanding prodromal symptoms, sleep as leading indicator of mood episode onset, medication adherence
- Interpersonal and Social Rhythm Therapy (IPSRT): stabilizes daily rhythms/sleep-wake cycles → reduces circadian dysregulation → fewer episodes
- Family-focused therapy: reduces high-expressed-emotion environments; reduces relapse
- Cognitive-behavioral therapy: relapse prevention, adherence, comorbid anxiety

## Connections

- `connects-to` → **[GSK-3β](../../../03-molecular/gsk-3b/README.md)** — lithium directly inhibits GSK-3β (uncompetitive Mg²⁺ site); GSK-3β hyperactivity in bipolar drives circadian dysregulation and BDNF suppression; lithium → β-catenin stabilization → neuroprotective gene expression and hippocampal neurogenesis.

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — mesolimbic dopamine hyperactivity drives manic symptoms; antipsychotics (D2 blockers) are first-line acute antimanic agents; mesocortical D1 hypofunction contributes to bipolar depression; dopamine catecholamine oscillation hypothesis explains mood cycling.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — SSRIs risk manic switching in BD and are generally avoided as monotherapy; atypical antipsychotics with 5-HT2A blockade (quetiapine) effectively treat bipolar depression without switch risk; serotonin deficit contributes to depressive phases.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — BDNF Val66Met SNP increases bipolar risk; BDNF is reduced during depressive episodes; lithium and valproate both upregulate BDNF and BCL-2, promoting neurogenesis and neuroprotection as a common mood stabilizer mechanism.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — valproate potentiates GABA-A function and blocks voltage-gated Na⁺/Ca²⁺ channels; GABA deficiency in PFC is associated with bipolar depression; benzodiazepines provide acute antimanic sedation via GABA-A agonism.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — bipolar disorder features amygdala hyperreactivity and reduced vmPFC regulation; hippocampal volume is reduced ~6% (BD-I); DLPFC shows reduced working memory activation; long-term lithium partially reverses hippocampal volume loss.

- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — Bipolar disorder shares neurodevelopmental genetics with autism: risk loci including SHANK2 and the CACNA1C calcium channel span both (and schizophrenia), and BD occurs more often in autistic people — recasting it as partly a neurodevelopmental, not purely mood, disorder.

- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Bipolar disorder and schizophrenia share ~70% of their GWAS risk loci and a neurodevelopmental origin: BD-I mania is psychotic in ~60% of episodes, and the two lie on a continuum — a major reason the boundaries between mood and psychotic disorders are blurred.

- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Bipolar disorder is repeatedly misdiagnosed as major depressive disorder because depressive episodes usually come first — a 7-10 year delay — and treating that depression with an SSRI alone risks flipping into mania, so every depression should be screened for past hypomania.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — Bipolar disorder and BPD are frequently confused: both show mood instability, but bipolar episodes last days-to-weeks and are often unprovoked, while BPD shifts are rapid (hours) and reactive to interpersonal triggers—distinguishing them guides treatment choice.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep is central to bipolar disorder: sleep loss is both a warning sign and a trigger of mania, circadian disruption destabilizes mood, and restoring regular sleep (and chronotherapy) is part of treatment—while many mood stabilizers act partly by normalizing the sleep-wake cycle.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol and other substance use disorders are among the commonest bipolar comorbidities (~40%): patients drink to blunt mania or relieve depression, worsening mood cycling, impulsivity and suicide risk; integrated treatment of both improves outcomes over treating either alone.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Cannabis use disorder is tightly linked to bipolar disorder: among its commonest comorbidities, it can precipitate manic or psychotic episodes and worsens mood-episode frequency and adherence—so heavy use destabilizes bipolar illness and complicates treatment.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety disorders are highly comorbid with bipolar disorder and worsen its course: generalized anxiety predicts more mood episodes and suicidality, and complicates treatment because antidepressants for anxiety can trigger mania—so mood stabilization comes first.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Bipolar disorder involves dysfunction of neurons: disturbed ion-channel, mitochondrial, and BDNF signaling destabilizes neuronal excitability, and lithium's action via GSK-3β inhibition and neuroprotection points to a cellular basis for the illness.
- `connects-to` → **[Binge Eating Disorder](../binge-eating-disorder/README.md)** — Bipolar disorder and binge eating disorder are tightly linked: BED is among the commonest eating disorders in bipolar patients, mood episodes drive impulsive eating, and weight gain is compounded by mood-stabilizer side effects—so metabolic monitoring is essential.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Bipolar disorder and PTSD frequently co-occur and worsen each other: childhood trauma raises bipolar risk, comorbid PTSD predicts more mood episodes and suicidality, and overlapping arousal and irritability blur the diagnosis—so trauma history shapes bipolar care.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — Bipolar disorder and anorexia nervosa overlap more than expected: mood instability is common in eating disorders, the two share genetic risk, and bipolar episodes can drive weight and appetite swings—so screening for an eating disorder is part of bipolar assessment.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Bipolar disorder involves glutamatergic dysfunction: abnormal excitatory signaling contributes to mood episodes, and rapid-acting ketamine (an NMDA-glutamate antagonist) can lift bipolar depression—evidence that glutamate, not just monoamines, shapes the illness.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Bipolar disorder is deeply tied to the body clock and melatonin: circadian disruption and altered melatonin rhythms can trigger mood episodes, sleep loss often precedes mania, and stabilizing sleep-wake and light exposure is a core part of management.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Bipolar disorder is a brain-wide disturbance of mood regulation: it reflects dysfunction across prefrontal-limbic networks of the nervous system rather than one region, producing the swings between mania and depression that define this highly heritable illness.
- `connects-to` → **[Thyroid Hormones (T3/T4)](../../03-molecular/thyroid-hormones/README.md)** — Thyroid and bipolar disorder are intertwined: hypothyroidism can mimic or trigger depression and rapid cycling, and lithium—a mainstay treatment—commonly causes hypothyroidism, so thyroid function is checked before and during mood-stabilizer therapy.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Lithium's benefit comes at a renal cost: long-term use can cause nephrogenic diabetes insipidus and slowly progressive chronic kidney disease, so kidney function and lithium levels are monitored for life—balancing the most effective mood stabilizer against renal harm.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium signaling sits at bipolar disorder's genetic core: CACNA1C, encoding a calcium channel, is among the strongest risk genes, implicating disturbed neuronal calcium handling in how mood episodes arise and why lithium acts on this system.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Bipolar disorder's mood stabilizers act on sodium and its kin: lithium is a sodium-like ion that substitutes for it in neurons, while valproate and lamotrigine block sodium channels—so monovalent-cation and ion-channel biology underlies calming the manic brain.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Bipolar disorder carries a neuroinflammatory signature in microglia: activated brain microglia and raised inflammatory markers accompany mood episodes, supporting an inflammation hypothesis and interest in anti-inflammatory adjuncts.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Mania is in part a catecholamine surge: excess norepinephrine (with dopamine) drives the energy, reduced sleep need, and racing activity of manic episodes, which is why noradrenergic stimulants can trigger mania and why dampening it helps treat it.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Bipolar disorder dysregulates the stress hormone: an overactive HPA axis raises cortisol, and the resulting stress sensitization can kindle mood episodes, while high cortisol also contributes to the cognitive and metabolic toll of the illness.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Bipolar disorder shows up in the brain's white matter: oligodendrocyte and myelin abnormalities disrupt the connections between mood-regulating regions, one of the more consistent neuroimaging findings in the disorder.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Bipolar disorder can shrink the hippocampus: recurrent episodes and high cortisol are linked to reduced hippocampal volume and impaired plasticity, a change lithium and mood stabilizers may partly protect against.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Bipolar disorder is entangled with the thyroid: an underactive thyroid can mimic or trigger depression and rapid cycling, and lithium itself often causes hypothyroidism, so thyroid function is checked and corrected throughout treatment.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Bipolar disorder involves more than neurons—astrocytes too: these glial cells recycle glutamate and support brain metabolism, and their dysfunction may unbalance the excitatory signaling that swings between mania and depression.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Bipolar disorder may be an energy disorder: studies find mitochondrial dysfunction and low brain ATP, so faltering cellular energy is a leading hypothesis for why mood and activity destabilize and why metabolism is altered.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Brain imaging shows bipolar's signature: MRI reveals white-matter abnormalities and fMRI altered amygdala-prefrontal activity, and lithium treatment even slightly increases gray-matter volume on scans.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Bipolar disorder dysregulates synaptic plasticity: lithium and mood stabilizers act on cascades like GSK-3β that remodel synapses, stabilizing the circuits that swing between mania and depression.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Bipolar drugs tax the liver: valproate and carbamazepine are metabolized there and can be hepatotoxic, so liver-function monitoring is part of long-term mood-stabilizer treatment.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy points to bipolar's energy crisis: studies find abnormal, dysfunctional mitochondria in the neurons, fueling the leading hypothesis that faulty cellular energy production underlies the swings between mania and depression.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Bipolar disorder shortens life through the heart: cardiovascular disease is its leading cause of early death, driven by chronic stress, metabolic side effects of medication, and the lifestyle toll of the illness.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium echoes lithium's calming effect: it modulates the same neuronal signaling and calcium handling, and low levels are tied to mania, so magnesium has been studied as an adjunct mood stabilizer.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — A mood stabilizer can blister the skin: lamotrigine carries a risk of Stevens-Johnson syndrome and toxic epidermal necrolysis, which is why it must be titrated up slowly and stopped at the first rash.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Treatment can inflame and unbalance the pancreas: valproate is a recognized cause of acute pancreatitis, while the antipsychotics often added drive weight gain and insulin resistance toward diabetes.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Bipolar drugs reach the reproductive tract: valproate causes polycystic ovary syndrome and, like lithium, is teratogenic — valproate with neural tube defects, lithium with the heart's Ebstein anomaly — complicating treatment in pregnancy.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Mood episodes carry an inflammatory signature: IL-6 and other cytokines rise during mania and depression, supporting a neuroinflammation model in which immune activation feeds the brain changes of bipolar disorder.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — The heart is the leading killer in bipolar disorder: chronic stress, inactivity, and the weight and metabolic effects of mood stabilizers and antipsychotics drive cardiovascular disease that shortens lifespan by over a decade.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Lithium and the gut-brain axis meet in the bowel: lithium commonly causes diarrhea that limits its dose, and the microbiome-gut-brain signaling implicated in mood adds another layer linking the gut to bipolar disorder.
- `connects-to` → **[Obesity](../obesity/README.md)** — Bipolar disorder and obesity feed each other: lithium, valproate, and antipsychotics drive weight gain while shared inflammation and inactivity push toward metabolic syndrome, making obesity one of its most common comorbidities and complicating drug choice.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The stress axis runs hot in mood episodes: bipolar disorder is marked by HPA-axis dysregulation, the adrenal glands oversecreting cortisol in both depression and mania, a disturbance that tracks with relapse and cognitive impairment.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Mania carries an inflammatory flush: TNF-α and other cytokines rise during acute episodes and settle with remission, part of the neuroinflammatory signature increasingly tied to bipolar disorder's course.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Body and mind share the burden: bipolar disorder carries a high rate of type 2 diabetes, driven both by the illness's metabolic biology and by the weight-gaining mood stabilizers and antipsychotics used to treat it.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The body's cannabis system sways mood: endocannabinoid signaling modulates the emotion and reward circuits disturbed in bipolar disorder, a link reflected in the high rate of cannabis use and its effect on episodes.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Peripheral immunity shifts with the mood state: altered helper T-cell profiles accompany mania and depression, extending bipolar's neuroinflammatory signature beyond the cytokines into the adaptive immune system.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Mood episodes ride a wave of inflammation: NF-κB activation drives the cytokine surges seen in mania and depression, the transcriptional engine behind bipolar's well-documented neuroinflammatory signature.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — It shortens life through the heart: bipolar disorder carries markedly elevated cardiovascular mortality, with chronic inflammation, metabolic side effects of medication and lifestyle accelerating atherosclerosis decades early.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its mainstay drug can scar the kidneys: years of lithium therapy cause nephrogenic diabetes insipidus and chronic interstitial nephritis, so long-term treatment carries a real risk of chronic kidney disease.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its cardiovascular toll reaches the brain: the accelerated atherosclerosis, metabolic syndrome and chronic inflammation of bipolar disorder raise the long-term risk of ischemic stroke beyond that of the general population.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Decades of metabolic strain wear on the heart: obesity, diabetes and the cardiometabolic effects of mood-stabilizing and antipsychotic drugs in bipolar disorder contribute to ischemic and structural heart disease and heart failure.
- `connects-to` → **[Migraine](../migraine/README.md)** — Mood and headache cycles intertwine: migraine is strongly comorbid with bipolar disorder, especially the bipolar II and depressive subtypes, sharing serotonergic and neuronal-excitability mechanisms.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Its mood stabilizer can flare the skin: lithium, a cornerstone of bipolar treatment, characteristically triggers or worsens psoriasis, sometimes forcing a change of therapy.
- `connects-to` → **[COPD](../copd/README.md)** — Heavy smoking scars the lungs: very high smoking rates in bipolar disorder drive chronic obstructive pulmonary disease, a major contributor to the reduced life expectancy in this population.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Mood instability and chronic pain overlap: bipolar disorder is markedly comorbid with fibromyalgia, sharing disturbances in sleep, stress reactivity and central pain and monoamine signaling.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its mainstay drug disturbs the glands: lithium commonly causes hypothyroidism and hyperparathyroidism, and thyroid dysfunction itself precipitates mood episodes, tightly linking bipolar disorder to the endocrine system.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its mood stabilisers can injure the gut and liver: valproate causes hepatotoxicity and pancreatitis, and lithium and other agents bring nausea and diarrhoea that complicate long-term treatment.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Anxiety rides alongside the mood swings: panic disorder is highly comorbid with bipolar disorder, worsening its course and complicating treatment, as antidepressants risk destabilising mood.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its mood stabiliser can damage the kidney: long-term lithium causes nephrogenic diabetes insipidus and a chronic interstitial nephritis that can slowly progress to chronic kidney disease, requiring regular monitoring.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its drugs reach the skin: lamotrigine can trigger Stevens-Johnson syndrome and toxic epidermal necrolysis, while lithium can aggravate psoriasis and acne.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Inflammation tracks its episodes: bipolar disorder is associated with raised inflammatory markers during mood episodes, supporting a neuroinflammatory component to its biology.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Both the illness and its drugs weaken bone: sedentary depressive phases and some psychotropics are linked to lower bone density and a higher fracture risk.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Heavy smoking shadows the illness: far higher smoking rates in bipolar disorder drive COPD and respiratory disease, compounding its cardiovascular mortality gap.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — Antidepressants are double-edged here: an SSRI like fluoxetine can flip a patient into mania or rapid cycling if given without a mood stabiliser, though fluoxetine-olanzapine is approved for bipolar depression.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — A latent parasite linked to mood: chronic Toxoplasma gondii infection is epidemiologically associated with bipolar disorder and higher suicide risk, possibly by altering brain dopamine.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet is studied as an adjunct: omega-3 supplementation shows modest benefit for bipolar depression in some trials, added to but not replacing mood stabilisers.
- `connects-to` → **[St John's Wort](../../../03-medicine/02-traditional/st-johns-wort/README.md)** — A herbal antidepressant that can destabilise it: St John's wort, taken for depression, can trigger mania or rapid cycling in undiagnosed bipolar disorder and interferes with mood-stabiliser metabolism.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — It raises later dementia risk: bipolar disorder is linked to a higher incidence of dementia including Alzheimer's, and intriguingly its mainstay lithium is studied as a neuroprotective agent that may lower that risk.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Stimulants and mania entangle: substance and stimulant use is highly comorbid with bipolar disorder, can precipitate or mimic manic episodes, and worsens its course and treatment response.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — White-matter wiring is disturbed: bipolar disorder shows reduced white-matter integrity and altered axonal connectivity between mood-regulating regions, part of the neuroprogression seen over repeated episodes.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Shared drugs and excitability: valproate, lamotrigine and carbamazepine are anticonvulsants that double as mood stabilisers, reflecting overlapping neuronal-excitability and kindling models of bipolar disorder and epilepsy.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Lithium taxes the kidney: long-term lithium for bipolar disorder causes chronic interstitial nephropathy and nephrogenic diabetes insipidus, slowly impairing the kidney and scarring the glomeruli over decades of use.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — A comorbid mood-anxiety overlap: bipolar disorder and obsessive-compulsive disorder co-occur often, and antidepressants for OCD can destabilise mood into mania, complicating treatment of the pair.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — A shared dopamine thread: bipolar disorder is associated with a higher later risk of Parkinson's disease, the dopaminergic surges of mania mirroring, in reverse, the dopamine loss of Parkinson's.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Mood-stabiliser cardiac effects: lithium and the antipsychotics used in bipolar disorder can disturb the cardiac conduction system—QT prolongation, bradycardia and arrhythmia—requiring ECG monitoring.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — Mood disorder in CNS disease: bipolar disorder occurs more often in multiple sclerosis, arising both from demyelinating lesions and from corticosteroid treatment, blurring primary and secondary mania.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Lithium and the parathyroids: long-term lithium therapy for bipolar disorder raises parathyroid hormone and causes hypercalcaemia, a recognised endocrine complication alongside its thyroid and kidney effects.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Mood under the pandemic: COVID-19 disrupted bipolar care and sleep-wake routines that trigger episodes, while severe infection and its neuroinflammation can precipitate mania or depression.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — The cardiovascular mortality gap: bipolar disorder roughly doubles cardiovascular death through metabolic, behavioural and treatment factors, straining the myocardium and shortening life expectancy.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory mood: IL-1β rises during mood episodes in bipolar disorder, part of the neuroinflammatory signature increasingly tied to its episodic, progressive course.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: stress and metabolic dysfunction activate the NLRP3 inflammasome in bipolar disorder, releasing IL-1β to drive the low-grade neuroinflammation linked to the illness.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Cholinergic-aminergic balance: the classic theory of bipolar disorder pits cholinergic against adrenergic tone, with cholinergic excess favouring depression and aminergic dominance favouring mania.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcium-signalling risk: the CACNA1C calcium-channel variant is the strongest genetic hit in bipolar disorder, dysregulating the calcium-calcineurin signalling that controls neuronal excitability and plasticity.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — Serotonergic vulnerability: serotonin-transporter function shapes the depressive pole of bipolar disorder and antidepressant response, though SSRIs risk triggering mania without a mood stabiliser.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Neuroplasticity signalling: mTOR-dependent synaptic plasticity is implicated in bipolar mood switching, and rapid-acting agents like ketamine act partly through this pathway.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Orexin-driven sleep-wake and circadian dysregulation is central to bipolar disorder, where sleep loss reliably precipitates mania and circadian disruption tracks mood episodes—making sleep stabilization a cornerstone of management.
- `connects-to` → **[NTRK / TrkB](../../03-molecular/ntrk/README.md)** — BDNF signaling through TrkB mediates the synaptic plasticity disrupted in bipolar disorder, and the neurotrophic action of lithium and valproate works partly through this BDNF-TrkB axis to protect neurons.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen influences monoaminergic systems, and bipolar mood episodes cluster around postpartum, perimenstrual, and perimenopausal hormonal shifts, especially in the rapid-cycling form more common in women.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — The L-type calcium channel gene CACNA1C is among the strongest and most replicated genetic risk factors for bipolar disorder, implicating dysregulated neuronal calcium signaling in the disease's pathophysiology.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Lithium inhibits GSK-3β, disinhibiting Wnt/β-catenin signaling, and this pathway is one proposed route by which the prototypical mood stabilizer exerts its neuroprotective and mood-balancing effects in bipolar disorder.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance is common in bipolar disorder and associated with a more chronic, treatment-resistant course, part of the bidirectional link between metabolic dysfunction and mood that shapes long-term outcome.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — The AKT-GSK3β pathway (GSK3β already mapped, the lithium target) is central to the mood-stabilizing and neuroprotective signaling whose dysregulation is implicated in bipolar disorder.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Neurotrophin-driven ERK-MAPK signaling, enhanced by lithium and valproate, supports the neuroplasticity and neuroprotection whose deficit is implicated in bipolar disorder.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Altered glucocorticoid-receptor feedback (cortisol already mapped) is a consistent finding in bipolar disorder, linking HPA-axis stress physiology to the onset of mood episodes.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Heightened CRH-driven HPA activity (cortisol and the glucocorticoid receptor mapped) precedes and precipitates mood episodes in bipolar disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-GSK3β-mTOR signaling (AKT, GSK-3β and mTOR mapped) is the intracellular cascade through which lithium and neurotrophins modulate the neuroplasticity disrupted in bipolar disorder.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88 signaling contributes to the low-grade neuroinflammation (IL-1β, IL-6 and TNF mapped) increasingly linked to the mood episodes of bipolar disorder.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Oxidative stress with impaired NRF2 antioxidant defense is a consistent feature of bipolar disorder, linked to its mitochondrial dysfunction.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 reflects the neuroinflammatory activation increasingly implicated in the mood episodes of bipolar disorder.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine-driven JAK-STAT signaling (IL-6 mapped) transduces the systemic inflammation associated with bipolar disorder.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling (JAK1/2 already mapped) transduces the inflammatory tone implicated in the neuroprogression of bipolar disorder.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Mitochondrial dysfunction in bipolar disorder releases cytosolic DNA that can engage cGAS-STING, linking bioenergetic stress to its neuroinflammation.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the interferon-associated inflammatory component reported in mood episodes of bipolar disorder.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of the PI3K-AKT-GSK-3β axis (AKT, PIK3CA, and the lithium target GSK-3β already mapped) regulates neuronal resilience and oxidative-stress handling implicated in bipolar disorder.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to mood episodes in bipolar disorder.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked mitochondrial and metabolic dysfunction is implicated in the bioenergetic dysregulation of bipolar disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, coupled to mitochondrial energetics (mTOR already mapped), participates in the bioenergetic dysfunction implicated in bipolar disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of neuronal gene expression associated with bipolar disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy, induced by the mood stabilizer lithium, participates in the neuroprotective mechanisms relevant to bipolar disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the synaptic and neurotrophin signaling relevant to bipolar disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammatory component of bipolar disorder.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-p53 signaling participates in the cellular-resilience and neuroplasticity mechanisms modulated by mood stabilizers in bipolar disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and neuroplasticity processes implicated in bipolar disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory responses implicated in bipolar disorder.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with bipolar disorder.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neurodevelopmental gene programs implicated in bipolar disorder.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the neuromodulation and sleep-circadian processes implicated in bipolar disorder.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the microglial and neuroinflammatory processes implicated in bipolar disorder.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Purinergic mania: elevated uric acid produced by xanthine oxidase is associated with manic episodes, and the xanthine-oxidase inhibitor allopurinol has shown antimanic effects, supporting a purinergic dimension (adenosine already mapped) of bipolar disorder.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic comorbidity: bipolar disorder carries a heavy burden of obesity and metabolic syndrome, worsened by mood stabilisers and antipsychotics, and leptin dysregulation links the affective illness to its cardiometabolic morbidity.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Nitrosative stress: increased nitric oxide and nitrosative stress accompany mood episodes in bipolar disorder, contributing to the mitochondrial and neuronal dysfunction implicated in its pathophysiology.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Reproductive-cycle mood: mood episodes in bipolar disorder cluster around the perinatal period and menstrual cycle, implicating progesterone and its neurosteroid metabolites, alongside estrogen (already mapped), in the hormonal triggering of episodes.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Stress reactivity: central angiotensin II modulates stress responses and interacts with the HPA axis (cortisol already mapped), a neuroendocrine system implicated in the stress sensitivity that precipitates mood episodes in bipolar disorder.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response and mood regulation dysregulated in bipolar disorder.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6, TNF and IL-1 already mapped) implicated in bipolar disorder modulate the mood circuits, part of the inflammatory neuroprogression of the illness.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Lithium diabetes insipidus: chronic lithium induces resistance to vasopressin in the kidney (already mapped), causing nephrogenic diabetes insipidus with polyuria, and vasopressin also participates in the HPA stress axis dysregulated in bipolar disorder.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Metabolic syndrome: bipolar disorder and its antipsychotic and mood-stabiliser treatment promote an atherogenic dyslipidaemia (insulin and leptin already mapped), part of the metabolic syndrome that raises its cardiovascular mortality.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4 counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation reported in bipolar disorder, particularly during mood episodes.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and mood: zinc modulates the glutamatergic (already mapped) NMDA signalling, and low zinc status is reported in the depressive episodes of bipolar disorder, part of its trace-metal dimension.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and monoamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), and disturbed copper-zinc (already mapped) balance is reported in the mood episodes of bipolar disorder.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histaminergic arousal: the H1/H3 histaminergic modulation of the arousal and the sleep-wake cycle (orexin and melatonin already mapped) is disturbed in the mood episodes of bipolar disorder, and H1-active drugs affect its course.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-syndrome (insulin and cholesterol already mapped) comorbidity of bipolar disorder and its treatments.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the metabolic comorbidity of bipolar disorder.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is the type-2 immune arm of the neuroinflammation (TNF and IL-6 already mapped) implicated in bipolar disorder.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Neuronal excitability: the neuronal excitability and the ion-channel (CACNA1C calcium) dysregulation and the mitochondrial (ATP already mapped) dysfunction of the neurons underlie the mood episodes of bipolar disorder.
- `connects-to` → **[Type 2 diabetes](../type-2-diabetes/README.md)** — Metabolic comorbidity: bipolar disorder carries a high type 2 diabetes and metabolic-syndrome (insulin and cholesterol already mapped) risk, worsened by the antipsychotics (leptin and adiponectin already mapped).
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in the mood episodes of bipolar disorder.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation associated with bipolar disorder, more prominent in the manic episodes.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of bipolar disorder.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of bipolar disorder.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension associated with bipolar disorder.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of bipolar disorder.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the type-2 (IgE already mapped) dimension implicated in bipolar disorder.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the mood episodes of bipolar disorder.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Stress-modulated NK: the NK-cell number and cytotoxicity, altered by the stress and cortisol (already mapped) reactivity, are part of the peripheral immune dysregulation of bipolar disorder.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the low-grade complement activation of the neuroinflammation implicated in bipolar disorder.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) neuroinflammation implicated in the mood episodes of bipolar disorder.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the low-grade neuroinflammation of bipolar disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-neuroinflammatory axis: TSLP, from epithelial barriers, primes mast cells (already mapped) and dendritic cells (already mapped) and amplifies the Th17 (already mapped) neuroinflammatory bias implicated in the mood episodes of bipolar disorder.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-neuroinflammatory axis: bradykinin, via B2R on CNS microglia (already mapped) and endothelium (already mapped), amplifies the BBB permeability and the neuroinflammation contributing to the mood episodes of bipolar disorder.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3 and C5 already mapped) contributing to the synaptic pruning excess and the neuroinflammation of the mood episodes of bipolar disorder.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM remodelling in mood circuits: periostin, expressed by astrocytes (already mapped) and microglia (already mapped), modulates the perineuronal net matrix in limbic circuitry and contributes to the synaptic dysregulation underlying mood episodes of bipolar disorder.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective cytokine: erythropoietin, via EPOR on neurons (already mapped) and astrocytes (already mapped), promotes neuronal survival, limits the neurotoxic cytokine burden (TNF-α and IL-6 already mapped) and attenuates the hippocampal volume loss of bipolar disorder.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Antipsychotic-immune axis: prolactin, elevated by antipsychotic medications used in BD (dopamine already mapped), modulates T-cell (already mapped) and NK-cell (already mapped) immune function and contributes to the metabolic side-effect burden of bipolar disorder.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen neuroinflammation suppression: testosterone, via androgen receptors on neurons, suppresses NF-κB and IL-6 neuroinflammation; androgen deficiency amplifies complement-C5-mediated mood-circuit synaptic-pruning excess of BD.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Dopamine-serotonin mood modulation: oxytocin, via OXTR on neurons, modulates the dopamine/serotonin mood circuitry and neuroplasticity; oxytocin deficiency amplifies NF-κB neuroinflammation and BDNF deficit of BD.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Neuroprotective antioxidant: selenium, via GPx and thioredoxin reductase, protects neurons from oxidative injury; selenium deficiency amplifies NF-κB and IL-6 neuroinflammatory burden and mood-episode severity of bipolar disorder.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — BD iodine: iodine-dependent thyroid hormones regulate neuronal (neuron already mapped) metabolism and hippocampal (already mapped) plasticity; hypothyroidism, common in BD, amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and mood-episode severity.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — BD potassium: potassium efflux activates NLRP3 inflammasome (already mapped) in microglia (already mapped); disrupted K⁺ and Na+ (sodium already mapped) homeostasis at synapses (already mapped) amplifies NF-κB (already mapped) and IL-1β (already mapped) neuroinflammation in BD.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — BD iron: iron is required for dopamine (already mapped) and serotonin (already mapped) synthesis; iron deficiency impairs hippocampal (already mapped) neuronal (neuron already mapped) energy and worsens the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation in BD.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — BD phosphorus: phosphorus fuels neuron (already mapped) and synapse (already mapped) ATP; phosphorus deficiency impairs dopamine (already mapped) and serotonin (already mapped) synthesis and amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation in BD.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — BD nitrogen: nitric oxide (NO, nitrogen-derived) in neurons (already mapped) and microglia (already mapped) amplifies neuroinflammation; NO excess upregulates NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) worsening serotonin (already mapped) in BD.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — BD chloride: chloride channels on neurons (already mapped) and microglia (already mapped) regulate excitability; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) and serotonin (already mapped) signalling in BD.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — BD sulfur: sulfur-containing glutathione in neurons (already mapped) and microglia (already mapped) scavenges ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) and BDNF (already mapped) dysregulation in BD.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — carbon-based organic acids in neurons (already mapped) fuel mitochondrial energy; disrupted carbon metabolism amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) and serotonin (already mapped) mood cascade in bipolar disorder.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — hydrogen ion dysregulation in brain (already mapped) amplifies mood circuit excitability; proton excess disrupts dopamine (already mapped) and serotonin (already mapped) and BDNF (already mapped) and IL-6 (already mapped) neuroinflammatory cascade in bipolar disorder.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — ROS from NADPH oxidase in neurons (already mapped) and microglia (already mapped) amplifies brain (already mapped) neuroinflammation; oxygen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade in bipolar disorder.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — BD pd-1: PD-1 on t-cytotoxic cells (already mapped) and microglia (already mapped) suppresses neuroimmune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory mood-cycling cascade in BD.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — BD glp-1: GLP-1 on neurons (already mapped) and astrocytes (already mapped) modulates synaptic energy metabolism; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory mood-cycling dysfunction in BD.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — BD vegf: VEGF from astrocytes (already mapped) and neurons (already mapped) sustains cerebrovascular supply; VEGF deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory mood dysregulation in BD.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — BD rankl: RANKL in microglia (already mapped) and astrocytes (already mapped) modulates neuroimmune skewing; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory mood-cycling cascade in BD.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — BD smad4: SMAD4 in neurons (already mapped) and astrocytes (already mapped) mediates TGF-β neuroprotection; smad4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) mood-cycling cascade in BD.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — BD il-2: IL-2 from T-helper cells (already mapped) and microglia (already mapped) modulates neuroimmune balance; IL-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory mood-cycling cascade in BD.

[^grande-2016-bipolar-review]: Grande I, Berk M, Birmaher B, Vieta E. Bipolar disorder. *Lancet.* 2016;387(10027):1561-1572. [doi:10.1016/S0140-6736(15)00241-X](https://doi.org/10.1016/S0140-6736(15)00241-X) · [PubMed 26388529](https://pubmed.ncbi.nlm.nih.gov/26388529/)
[^geddes-2013-bipolar-treatment]: Geddes JR, Miklowitz DJ. Treatment of bipolar disorder. *Lancet.* 2013;381(9878):1672-1682. [doi:10.1016/S0140-6736(13)60857-0](https://doi.org/10.1016/S0140-6736(13)60857-0) · [PubMed 23663953](https://pubmed.ncbi.nlm.nih.gov/23663953/)
[^cipriani-2013-lithium-suicide]: Cipriani A, Hawton K, Stockton S, Geddes JR. Lithium in the prevention of suicide in mood disorders: updated systematic review and meta-analysis. *BMJ.* 2013;346:f3646. [doi:10.1136/bmj.f3646](https://doi.org/10.1136/bmj.f3646) · [PubMed 23814104](https://pubmed.ncbi.nlm.nih.gov/23814104/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
