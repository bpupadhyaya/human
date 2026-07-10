---
schema: human-scale-entry/v1
id: major-depressive-disorder
name: Major Depressive Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Major depressive disorder (280M affected) involves serotonergic/noradrenergic deficit, HPA dysregulation, neuroinflammation, and reduced BDNF neuroplasticity; SSRIs/SNRIs are first-line; ketamine (IV racemic or nasal esketamine) is the fastest-acting approved antidepressant."
aliases: ["major depressive disorder", "MDD", "depression", "unipolar depression", "TRD", "treatment-resistant depression", "antidepressant", "SSRI", "SNRI", "ketamine depression", "esketamine"]
sources:
  - id: cipriani-2018-antidepressants-meta
    type: peer-reviewed
    cite: "Cipriani A, Furukawa TA, Salanti G, et al. Comparative efficacy and acceptability of 21 antidepressant drugs for the acute treatment of adults with major depressive disorder: a systematic review and network meta-analysis. Lancet. 2018;391(10128):1357-1366."
    doi: "10.1016/S0140-6736(17)32802-7"
    pmid: "29477251"
    url: "https://doi.org/10.1016/S0140-6736(17)32802-7"
    accessed: "2026-06-08"
  - id: zarate-2006-ketamine-rapid
    type: peer-reviewed
    cite: "Zarate CA Jr, Singh JB, Carlson PJ, et al. A randomized trial of an N-methyl-D-aspartate antagonist in treatment-resistant major depression. Arch Gen Psychiatry. 2006;63(8):856-864."
    doi: "10.1001/archpsyc.63.8.856"
    pmid: "16894061"
    url: "https://doi.org/10.1001/archpsyc.63.8.856"
    accessed: "2026-06-08"
  - id: duman-2012-bdnf-depression
    type: peer-reviewed
    cite: "Duman RS, Aghajanian GK. Synaptic dysfunction in depression: potential therapeutic targets. Science. 2012;338(6103):68-72."
    doi: "10.1126/science.1222939"
    pmid: "23042884"
    url: "https://doi.org/10.1126/science.1222939"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Reduced serotonergic neurotransmission is central to MDD; SSRIs (fluoxetine, sertraline, escitalopram) are first-line antidepressants; tryptophan depletion triggers depressive relapse in remitted MDD; 5-HT1A autoreceptor desensitization is required for delayed SSRI onset."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "SNRIs (venlafaxine, duloxetine) and TCAs raise synaptic NE via NET blockade; NE deficit underlies psychomotor retardation; mirtazapine (α2 antagonist) raises NE and 5-HT by blocking autoreceptors; melancholic MDD preferentially responds to NE-targeting antidepressants."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "HPA hyperactivation in MDD — elevated CRH, cortisol, blunted dexamethasone suppression — causes hippocampal atrophy via GR-mediated BDNF suppression; normalizing cortisol (mifepristone, CRH antagonists) correlates with antidepressant response; cortisol predicts remission."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "CRH hyperdrive from PVN and CeA drives HPA hyperactivation in MDD; elevated CSF CRH and blunted DST are the most replicated biomarkers; CRHR1 antagonists reduce depressive symptoms in trials; CRH excess causes hippocampal BDNF suppression and dendritic atrophy."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF deficiency is central to the neuroplasticity hypothesis of MDD: stress reduces hippocampal BDNF; antidepressants (SSRIs, MAOIs, ketamine) normalize BDNF; BDNF Val66Met SNP impairs activity-dependent secretion and increases MDD vulnerability to stress."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "MDD involves reduced hippocampal volume (~2% per episode), reduced DLPFC gray matter, and hyperactive amygdala; functional dysconnectivity between DLPFC and limbic regions; subgenual cingulate (Area 25) hyperactivity is normalized by DBS and antidepressants."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "MDD features ACTH hypersecretion from CRH-driven corticotroph excess → hypercortisolemia; DST nonsuppression reflects HPA hyperdrive; blunted ACTH response to exogenous CRH indicates corticotroph downregulation; ACTH/cortisol normalisation with antidepressants predicts remission."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Antipsychotic-induced hyperprolactinemia causes sexual dysfunction and anhedonia driving non-adherence; postpartum prolactin dynamics may modulate MDD vulnerability; cabergoline (D2 agonist) has shown adjunctive antidepressant effects in small trials."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Male hypogonadism (T <300 ng/dL) predicts MDD risk; testosterone deficiency causes fatigue, anhedonia, and low libido indistinguishable from MDD; TRT has adjunctive antidepressant efficacy in hypogonadal men; SSRI-treated men with residual anhedonia benefit from TRT augmentation."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Perimenopausal estrogen fluctuations trigger or worsen MDD; transdermal estradiol (100 mcg/day patch) has antidepressant efficacy in perimenopausal women; PMDD involves abnormal CNS sensitivity to allopregnanolone (progesterone metabolite) fluctuations, not estrogen deficiency."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Hypothyroidism causes reversible depressive syndrome indistinguishable from MDD; TSH >10 mIU/L is a diagnostic exclusion for MDD; subclinical hypothyroidism accounts for ~10% of refractory MDD; T3 (25-50 mcg/day) augments antidepressant response in treatment-resistant depression."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Luteal allopregnanolone fluctuations drive PMDD and PPD; declining P4 post-delivery triggers PPD; brexanolone (IV allopregnanolone) and zuranolone (oral) treat PPD; PMDD responds to SSRIs, combined OCP, or GnRH agonist; progesterone withdrawal worsens anxiety."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Seasonal affective disorder (winter depression) involves delayed circadian phase and abnormal melatonin timing; agomelatine (MT1/MT2 agonist + 5-HT2C antagonist) is an approved antidepressant with circadian phase-advancing effects; light therapy resets SCN/melatonin phase in SAD."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "AVP is elevated in PVN and CSF of depressed patients; V1bR co-drives HPA hyperactivation with CRH → excess ACTH and cortisol; V1b antagonist SSR149415 showed antidepressant effects in Phase 2; SSRIs normalise hypersecretion of both CRH and AVP."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Leptin falls during caloric restriction → ↓POMC → ↓α-MSH → ↓melanocortin tone; hyperleptinemia (obesity) associates with depressive symptoms; LEPR polymorphisms associate with MDD risk; leptin restores BDNF and reverses anhedonia in diet-induced obesity rodent models."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: treated-by
    note: "Fluoxetine is first-line SSRI for MDD (Cipriani 2018 21-drug meta-analysis); onset 4–6 weeks via SERT inhibition → 5-HT desensitization → BDNF/TrkB synaptic plasticity; only SSRI approved for pediatric MDD (age ≥8); effective for acute and maintenance treatment."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Depression shrinks the hippocampus: chronic stress and high cortisol impair hippocampal neurogenesis and reduce its volume, contributing to mood symptoms—and antidepressants that restore neurogenesis help reverse it, linking stress hormones to brain structure."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Depression involves more than neurotransmitter levels at the neuron: impaired synaptic plasticity, dendritic loss and reduced BDNF-driven connectivity underlie it, which is why rapid agents like ketamine that regrow synapses lift mood faster than monoamine drugs."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation links the immune system to depression: raised IL-6 and other cytokines accompany many depressions, can cause sickness-behavior low mood, and predict poorer antidepressant response—a subtype where anti-inflammatory strategies are studied."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Depression is increasingly seen as a glutamatergic disorder: stress alters glutamate signaling and synaptic plasticity, and the rapid antidepressant ketamine acts on NMDA glutamate receptors—evidence that the monoamine model alone is incomplete."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Depression is linked to the gut-brain axis: the microbiome shapes neurotransmitter and inflammatory signaling reaching the brain via the vagus nerve, and dysbiosis is associated with depression—so the gut is an emerging target beyond the brain itself."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Depression and insomnia are tightly bidirectional: sleep disturbance is a core symptom and often the first sign, and persistent insomnia independently predicts and worsens depression—so treating sleep is integral to treating the mood disorder."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Depression has a neuroinflammatory arm in microglia: activated brain microglia release cytokines that lower serotonin precursors and impair neuroplasticity, linking the immune system to mood and helping explain why inflammation predicts poorer antidepressant response."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Distinguishing depression from bipolar disorder is critical: a depressive episode may be the first sign of bipolar illness, and giving an antidepressant alone can trigger mania—so screening for past hypomania guides whether mood stabilizers are needed."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Anhedonia in depression points to dopamine: beyond serotonin, blunted dopamine reward signaling underlies the loss of pleasure and motivation, which is why some antidepressants and adjuncts target dopamine to relieve symptoms that SSRIs miss."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Depression isn't only low serotonin—it's also low GABA: deficient inhibitory GABA signaling is found in depressed brains, and neurosteroid drugs (brexanolone, zuranolone) that boost GABA receptors rapidly lift mood, especially in postpartum depression."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Depression shows a loss of astrocytes: postmortem brains reveal reduced astrocyte density in mood-regulating regions, impairing the glutamate clearance and neuron support these glial cells provide—a structural face of the illness beyond neurotransmitters."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Oxytocin ties depression to broken social bonds: low signaling of this bonding hormone is linked to the social withdrawal and loss of connection in depression, and it is studied as a route to ease the isolation that deepens the illness."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium influences the depressed brain: it blocks the NMDA receptor and supports neuroplasticity, so low magnesium is linked to depression and supplementation is studied as an adjunct, echoing ketamine's glutamate-targeting action."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Depression is increasingly seen as a synaptic disease: chronic stress prunes synapses in mood circuits, and fast-acting antidepressants like ketamine work by rapidly regrowing them, shifting focus from neurotransmitter levels to synaptic repair."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Depression keeps the adrenal glands overworked: an overactive HPA axis drives them to pour out cortisol, and this sustained stress-hormone excess feeds the cognitive, metabolic and mood disturbances of the illness."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Light is medicine for some depression: bright-light therapy delivers photons that reset the body clock and lift seasonal affective disorder, which short, dim winter days can trigger."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Depression is linked to low zinc: the mineral supports BDNF and tempers NMDA signaling, so deficiency is associated with depressive symptoms and zinc is studied as an add-on to antidepressants."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Depression talks with the gut: through the gut-brain axis, the large intestine's microbes and the serotonin made there influence mood, a two-way link tying digestive health to depression."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Low iron can mimic and worsen depression: iron deficiency causes the fatigue, poor concentration and low mood that overlap with MDD, so iron is checked in the workup of new depression."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Depression alters white matter: oligodendrocyte and myelin abnormalities appear in the mood-circuit tracts, part of the connectivity changes seen on imaging in chronic MDD."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Depression and heart disease feed each other: MDD raises the risk of heart attacks and worsens survival after one, through stress hormones, inflammation and the behaviors it shapes."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Depression may thin the brain's connections: studies find reduced dendritic spines and synapses in mood-regulating regions, and the rapid antidepressant effect of ketamine is thought to work by regrowing them."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D shadows the depressed mind: deficiency is consistently associated with depression, and the vitamin's receptors throughout the brain's mood circuits suggest a role in the seasonal and chronic forms of the illness."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Depression unsettles the stomach: appetite swings up or down, nausea and 'butterflies' are common somatic complaints, and the gut-brain serotonin axis ties mood tightly to digestion."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid impersonates depression: hypothyroidism produces low mood, fatigue, and slowed thinking that lift with hormone replacement, so thyroid function is checked in every depression workup and added as augmentation when standard antidepressants fall short."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Depression has an inflammatory face: raised TNF-α and related cytokines appear in depressed patients, can themselves induce low mood as sickness behavior, and mark the subgroup whose illness may respond to anti-inflammatory strategies."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Depression and obesity feed each other: each roughly doubles the risk of the other through shared inflammation, cortisol, and inactivity, and several antidepressants add weight — a metabolic-mood loop that complicates treating either alone."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Depression tracks the reproductive hormones: it surges around the premenstrual phase, after childbirth, and through the menopause transition, the timing that ties mood to estrogen and progesterone shifts and shapes perinatal screening and treatment."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammation may help drive depression: stress activates the NLRP3 inflammasome in microglia to release IL-1β and IL-6, and this neuroinflammation is one explanation for the depressive symptoms seen in inflammatory illness and a target for novel therapies."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Depression makes platelets sticky: their serotonin handling overlaps the brain's, and in depression platelets become hyperreactive — a link to the raised heart-attack and stroke risk, partly offset by SSRIs that blunt platelet aggregation."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "An older neurochemical theory still holds: depression may reflect a cholinergic-adrenergic imbalance with acetylcholine signaling tipped too high, which is why the anticholinergic drug scopolamine can lift mood rapidly in some patients."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Adaptive immunity joins the inflammatory story: shifts toward Th17 helper T cells and altered T-cell profiles accompany depression, extending the inflammation hypothesis beyond microglia and cytokines into the body's broader immune response."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Damaged vessels can darken mood: cerebrovascular disease and stroke produce 'vascular depression', with post-stroke depression striking a large share of survivors and worsening their recovery — depression here a consequence of brain injury, not only a risk factor for it."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Depression and diabetes feed each other: depression raises diabetes risk through inactivity, cortisol, and inflammation, while the burden of diabetes deepens depression — a bidirectional loop that worsens control and outcomes in both."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety is depression's constant companion: generalized anxiety disorder co-occurs with major depression in a large share of patients, the mixed anxiety-depression that shares serotonergic biology and responds to overlapping treatments."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Trauma sets the stage for depression: PTSD greatly raises the risk of comorbid major depression, the two sharing HPA-axis dysregulation and overlapping symptoms that complicate diagnosis and worsen prognosis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Depression smolders with inflammation through NF-κB: psychological stress activates NF-κB-driven cytokine signaling, the inflammatory hypothesis of depression that links it to its raised cardiovascular and metabolic risk."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "A mood disorder that hardens the arteries: depression is an independent risk factor for and consequence of cardiovascular disease, its inflammation, autonomic strain and behavioral effects accelerating atherosclerosis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Low mood tips the blood toward clots: depression is associated with a higher risk of venous thromboembolism, through inflammation, platelet activation and the inactivity that accompanies severe episodes."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Depression and the failing heart feed each other: depression is common in heart failure and independently predicts hospitalization and death, sharing inflammation and autonomic dysregulation, and worsening self-care."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "It is the commonest psychiatric burden of kidney failure: depression is highly prevalent in chronic kidney disease and on dialysis, driven by the illness burden and uremic effects, and it worsens adherence and survival."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Drinking and depression entangle: alcohol use disorder and major depression frequently co-occur, each worsening the other — alcohol used to self-medicate low mood while deepening it, complicating treatment of both."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Low mood quietly thins the bones: depression is associated with reduced bone density through cortisol, inflammation and inactivity, and the SSRIs used to treat it independently lower bone mass and raise fracture risk."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Depression foreshadows and accelerates dementia: late-life depression is both a risk factor for and an early sign of Alzheimer's, sharing inflammatory, vascular and hippocampal changes."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Mood and central pain amplify each other: depression is highly comorbid with fibromyalgia, the two sharing serotonergic and stress-system dysregulation that heightens both low mood and pain sensitivity."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is a disorder of brain circuits and chemistry: depression reflects dysregulation of monoaminergic transmission and limbic-prefrontal networks, with hippocampal and neuroplastic changes underpinning it."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones drive and mimic it: depression features HPA-axis overactivity with high cortisol, and thyroid disease and other endocrine disorders both cause and worsen depressive symptoms."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Inflammation feeds low mood: raised inflammatory cytokines are found in depression and can induce it (sickness behaviour), the basis of the inflammatory hypothesis of mood disorder."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It reaches the gut both ways: appetite and weight change are core symptoms, the gut-brain axis ties it to functional GI disorders, and SSRIs impair platelet serotonin to raise gastrointestinal bleeding risk."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Low mood is felt in the body: depression frequently presents with unexplained muscle and back pain, and is bidirectionally linked with chronic musculoskeletal pain that deepens it."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its drugs can unbalance sodium: SSRIs can cause hyponatraemia from SIADH, particularly in older patients, requiring monitoring after starting treatment."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Heart and mood are bound together: depression worsens outcomes after myocardial infarction and independently raises cardiovascular risk through inflammation, autonomic and behavioural pathways."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It travels with breathing disease: depression is common in COPD and asthma, worsening symptom burden and adherence, and breathlessness itself feeds low mood."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin and mind interact: depression accompanies chronic skin disease such as psoriasis and acne, and the distress of visible disease deepens low mood in turn."
  - target: 03-medicine/02-traditional/st-johns-wort
    relation: connects-to
    note: "A herbal antidepressant: St John's wort is effective for mild-to-moderate depression in trials, acting on monoamines, but it dangerously induces drug-metabolising enzymes and risks serotonin syndrome with SSRIs."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet offers a modest adjunct: omega-3 (EPA-rich) supplementation has small antidepressant effects in trials, used alongside but not instead of established therapy for major depression."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "A latent parasite linked to mood: chronic Toxoplasma gondii infection is epidemiologically associated with major depression and suicidal behaviour, possibly through neuroinflammation and altered dopamine."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Depression shadows the dopamine loss: major depression is a common prodrome and comorbidity of Parkinson's disease, sharing degeneration of monoaminergic dopamine, serotonin and noradrenaline systems, so mood symptoms can precede the tremor by years."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "A two-way street with seizures: depression and epilepsy are bidirectionally linked—each roughly doubles the risk of the other—through shared GABA/glutamate imbalance, HPA-axis overactivity and neuroinflammation, and some antidepressant and antiseizure drugs cross over."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Pain and mood travel together: major depression and migraine are strongly comorbid and bidirectional, sharing serotonergic dysfunction and central sensitisation, so each worsens the other's course and some drugs like amitriptyline and SNRIs treat both."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "The heart-depression link: depression worsens survival after myocardial infarction and is itself a cardiovascular risk factor, while antidepressants—especially tricyclics—affect the QT interval and cardiac conduction."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Inflammation and mood: chronic inflammatory diseases like rheumatoid arthritis carry high rates of depression, and cytokines (IL-6, TNF) drive the sickness behaviour behind the inflammatory hypothesis of depression."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The gut-brain axis: the intestinal epithelium and its microbiome signal to the brain via the vagus and immune and metabolic pathways, a route increasingly implicated in depression."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Depression within psychosis: major depressive symptoms are common in schizophrenia and define schizoaffective disorder, with shared neurotransmitter and inflammatory biology and a markedly raised suicide risk across both."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Post-viral depression: SARS-CoV-2 infection and the chronic neuroinflammation of long COVID raise rates of new-onset depression, while the pandemic itself drove a global surge in depressive illness."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Inflammation feeds mood: depression is strikingly common in inflammatory bowel disease, a bidirectional link through systemic cytokines, the gut microbiome and the gut-brain axis that worsens both conditions."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory hypothesis: IL-1β and the inflammasome drive the neuroinflammation increasingly implicated in depression, joining IL-6 and TNF-α in the cytokine signature of low mood."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Stress neuropeptide: substance P and its NK1 receptor regulate mood and stress responses, an early antidepressant target that, though clinically disappointing, illuminated depression biology."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Resilience signal: neuropeptide Y has anti-stress, antidepressant-like effects, and low NPY levels are associated with depression and impaired stress resilience."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "SSRI target: the serotonin transporter is blocked by the SSRIs that are first-line for depression, and its gene variants modulate stress-related depression risk."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "HPA dysregulation: impaired glucocorticoid-receptor feedback underlies the cortisol hypersecretion of melancholic depression, a core stress-axis abnormality of the disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Inflammatory depression: IFN-γ and interferon therapy can precipitate depression by diverting tryptophan from serotonin toward neurotoxic kynurenines, part of the cytokine model of MDD."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Rapid antidepressant target: ketamine's fast antidepressant action depends on mTOR-driven synaptogenesis in the prefrontal cortex, reversing the synaptic loss seen in depression."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "Mood and stress buffering: endocannabinoid CB1 signalling regulates stress reactivity and emotional tone, and deficient endocannabinoid tone is implicated in the anhedonia and stress sensitivity of depression."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Neuroinflammatory trafficking: CCL2 recruits monocytes to the brain in depression, part of the low-grade neuroinflammation increasingly tied to the disorder's pathophysiology."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Synaptogenic mechanism: BDNF signalling through its TrkB receptor mediates the rapid synaptogenesis that underlies ketamine's fast antidepressant effect, the neurotrophin axis whose impairment characterises depression."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Reward and anhedonia: the endogenous μ-opioid system mediates social reward and its loss contributes to anhedonia, the rationale for low-dose buprenorphine in treatment-resistant depression."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Neuroinflammatory hypothesis: microglial TLR4-driven innate immune activation is a key strand of the inflammatory hypothesis of depression, linking chronic stress and infection to the disorder's neuroinflammation."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Arousal and anhedonia: orexin signalling that governs wakefulness, reward and motivation is dysregulated in depression, contributing to the disturbed sleep, fatigue and anhedonia that are core symptoms beyond low mood."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Stress hormone: ghrelin rises with chronic stress and has antidepressant-like central effects, a gut-derived hormone linking appetite, the stress response and mood in the metabolic-psychiatric overlap of depression."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: markers of oxidative stress, partly from xanthine-oxidase activity, are raised in depression, the redox imbalance that — with neuroinflammation — is increasingly implicated in the neurobiology of the disorder."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Mood and neuroplasticity: GSK-3β is a convergence node for mood regulation and synaptic plasticity, inhibited by lithium and modulated downstream of the serotonergic and BDNF signalling implicated in depression."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory deficit: a relative shortfall of regulatory IL-10 against the raised pro-inflammatory cytokines (IL-6, IL-1β and TNF mapped) is part of the neuroinflammatory hypothesis of depression."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Synaptic pruning: complement-mediated microglial pruning of synapses contributes to the loss of prefrontal and hippocampal connectivity implicated in the pathophysiology of depression."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Inflammatory depression: TLR4-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped) transduces the inflammatory state increasingly implicated in the pathophysiology and treatment resistance of major depression."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative neurobiology: NRF2-regulated antioxidant defence counters the oxidative stress (xanthine-oxidase already mapped) associated with major depression, a redox component of its neurobiology."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Neuroplasticity: ERK-MAPK signalling downstream of BDNF-TrkB (both already mapped) mediates the synaptic plasticity whose impairment underlies depression and whose restoration accompanies antidepressant response."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (mTOR and GSK-3β mapped) downstream of BDNF mediates the rapid synaptogenic antidepressant action of ketamine and the neuroplasticity deficits of major depression."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 reflects the neuroinflammatory activation increasingly implicated in major depressive disorder."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-driven JAK-STAT signalling (IL-6 mapped) transduces the systemic inflammation associated with major depressive disorder and its treatment resistance."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling (JAK1/2 already mapped) transduces the neuroinflammatory tone implicated in the pathophysiology and treatment resistance of major depressive disorder."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic mitochondrial DNA released during chronic stress engages cGAS-STING, contributing to the neuroinflammation of major depressive disorder."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling underlies the depression induced by type-I-interferon therapy, linking interferon signalling to the inflammatory subtype of major depressive disorder."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT and GSK-3β signaling (AKT and GSK-3β already mapped) regulates the neuronal resilience and oxidative-stress handling implicated in major depressive disorder."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to major depressive disorder."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and mitochondrial stress responses contribute to the neuroplasticity changes of major depressive disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of BDNF-TrkB (BDNF and NTRK already mapped), supports the neuroplasticity compromised in major depressive disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling participates in the metabolic and neuroinflammatory dysregulation of major depressive disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates neuronal resilience and the stress responses implicated in major depressive disorder, a candidate antidepressant mechanism."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (FYN) kinase signaling participates in the NMDA-receptor and synaptic-plasticity mechanisms implicated in major depressive disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with major depressive disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic (early-life-stress) programming implicated in major depressive disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and neuroplasticity processes implicated in major depressive disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in major depressive disorder."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with major depressive disorder."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the stress-responsive neuronal gene programs of major depressive disorder."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the sleep-wake and neuromodulatory processes implicated in major depressive disorder."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microglial activation and neuroinflammation implicated in major depressive disorder."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Brain renin-angiotensin: central angiotensin II modulates stress reactivity and neuroinflammation, and angiotensin-blocking antihypertensives have been associated with lower depression risk, implicating the brain RAS in mood regulation."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic depression: insulin resistance and depression are bidirectionally linked, sharing inflammatory and HPA-axis (cortisol already mapped) pathways, and impaired brain insulin signalling is implicated in the metabolic subtype of major depressive disorder."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid receptors: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response, and their dysregulation is implicated in the HPA-axis abnormalities of depression."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Neurogenesis: VEGF supports the hippocampal neurogenesis and angiogenesis (BDNF already mapped) that antidepressants promote, a vascular-neurotrophic mechanism implicated in recovery from depression and in the reduced hippocampal volume seen in the illness."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammation: prostaglandins from activated microglia (already mapped) contribute to the neuroinflammatory dimension of depression, and anti-inflammatory agents that block their synthesis are studied as adjuncts in the inflammatory subtype."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitrergic mood signalling: nitric oxide from neuronal nitric oxide synthase modulates monoamine (serotonin already mapped) and glutamatergic transmission, and dysregulated NO-cGMP signalling is implicated in the neurobiology of depression."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Lipids and mood: cholesterol is essential to neuronal membranes and synaptic function, and both the metabolic-syndrome dyslipidaemia comorbid with depression and the associations of very low cholesterol with suicidality link lipids to mood."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron and monoamines: iron is a cofactor for the enzymes making dopamine and serotonin (already mapped), and iron deficiency is associated with the fatigue and low mood of depression, sometimes improving with repletion."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Unipolar-bipolar distinction: distinguishing unipolar major depression from the depressive episodes of bipolar disorder is critical, as antidepressants can precipitate mania, and the two share overlapping mood neurobiology (BDNF and glutamate already mapped)."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Microglial polarisation: IL-4 polarises the microglia (already mapped) toward an anti-inflammatory M2 phenotype (IL-10 already mapped), the balance against the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) shaping the neuroinflammatory subset of depression."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is part of the type-2 arm whose balance against the pro-inflammatory signals shapes the neuroinflammatory dimension of major depression."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and monoamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), and disturbed copper-zinc (already mapped) balance is reported in major depression."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon-induced depression: interferon-α therapy is a classic cause of depression, and the type-I interferon neuroinflammatory (IFN-γ already mapped) signalling is implicated in the pathophysiology of major depression."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic-inflammatory adipokine: adiponectin, with leptin (already mapped), links the obesity and metabolic syndrome (insulin already mapped) to the inflammatory dimension of major depression."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the metabolic-inflammatory (IL-6 already mapped) link to major depression."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Anxiety comorbidity: major depression and social anxiety disorder are highly comorbid, sharing the serotonergic (already mapped) dysregulation and the SSRI treatment."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Panic comorbidity: major depression and panic disorder are comorbid, sharing the serotonergic and noradrenergic (already mapped) dysregulation."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Substance-use comorbidity: major depression is highly comorbid with opioid use disorder (the self-medication, the shared reward — dopamine already mapped — and stress — cortisol already mapped — dysregulation)."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the neuroinflammation (IL-6 and TNF already mapped) implicated in major depressive disorder."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of major depressive disorder."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with major depressive disorder."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation associated with major depressive disorder."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive neuroinflammation: the cytotoxic T cells (perforin pathway) of the CNS-border compartments are part of the adaptive-immune contribution to the neuroinflammation of major depressive disorder."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the type-2 (IgE already mapped) dimension of major depressive disorder."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Stress-modulated NK: the NK-cell number and cytotoxicity, altered by the chronic stress and cortisol (already mapped) reactivity, are part of the peripheral immune dysregulation of major depressive disorder."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) activation and the complement-mediated synapse loss implicated in major depressive disorder."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the neuroinflammation of major depressive disorder."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Neuroinflammatory mediator: histamine (released by brain mast cells and tuberomammillary nucleus neurons) signals through H1/H3 receptors to modulate the HPA axis dysregulation and the norepinephrine-serotonin (already mapped) imbalance of major depressive disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuroimmune alarmin: elevated peripheral TSLP from atopic/allergic comorbidities (mast cells already mapped) activates dendritic cells and drives the neuroinflammatory IL-6/TNF-α (already mapped) cytokine cascade that mediates the depression-allergy comorbidity in MDD."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Neuroinflammation amplifier: bradykinin activates central B2 receptors, amplifying the NF-kB (already mapped) neuroinflammation and norepinephrine (already mapped) release that characterise the stress-induced neuroinflammatory phenotype of major depressive disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Neurocomplement brake: C1-INH controls the classical complement pathway (C3 and C5aR1 already mapped) at the blood-brain barrier and in the choroid plexus, limiting the complement-mediated synaptic pruning and the neuroimmune inflammation of major depressive disorder."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective EPO: erythropoietin, via EPOR on neurons (already mapped) and microglia (already mapped), activates the JAK2/STAT3 (JAK1/2 already mapped) anti-apoptotic pathway and reduces the neuroinflammatory IL-6 (already mapped) burden of major depressive disorder."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Astrocyte ECM remodelling: periostin, expressed by reactive astrocytes (already mapped) in the neuroinflamed brain (already mapped) of MDD, promotes the extracellular matrix changes that accompany glial morphology shifts and synaptic (already mapped) remodelling in depression."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenoprotein antidepressant: selenium, via neuronal and microglial (both already mapped) selenoproteins (GPx/TrxR), quenches the reactive oxygen species and neuroinflammatory IL-6 (already mapped) burden underlying the oxidative-stress phenotype of major depressive disorder."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Neurocomplement factor H: factor H, the key complement regulator (C3 and C5aR1 already mapped), controls complement-mediated synaptic pruning and microglial (already mapped) activation in the MDD brain, limiting the neuroimmune cascade at the blood-brain barrier."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement C5: complement C5, cleaved to C5a (C5aR1 already mapped) and MAC, drives neuroinflammatory astrocytic (already mapped) activation and C1q-mediated synaptic pruning linking inflammatory MDD to hippocampal grey-matter loss and cognitive impairment."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "MDD iodine HPT axis: iodine, as the essential substrate for thyroid hormone (already mapped) biosynthesis, supports the HPT axis; iodine insufficiency deepens the neuroimmune NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory burden of major depressive disorder."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "MDD sodium neuroimmune: sodium, at supraphysiological levels, activates microglial (already mapped) NF-κB (already mapped) and IL-6 (already mapped) signalling toward a pro-inflammatory macrophage (already mapped) state, amplifying the neuroinflammatory burden of MDD."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "MDD potassium neuronal: potassium maintains synaptic (already mapped) resting potential and BDNF (already mapped) signalling; potassium dyshomeostasis in the MDD hippocampus (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation in MDD."
---

# Major Depressive Disorder

## Overview

**Major depressive disorder (MDD)** is a common, recurrent, and potentially life-threatening psychiatric condition characterized by sustained depressed mood and/or anhedonia, representing the leading cause of disability worldwide. It affects approximately **280 million people globally** (~5% of the population), with a lifetime prevalence of 15–20% in high-income countries. Women are affected approximately twice as often as men. MDD is a top 5 cause of global disease burden by disability-adjusted life years (DALYs), ahead of ischemic heart disease and stroke in many countries.

**DSM-5 diagnostic criteria** require ≥5 of the following symptoms present ≥2 weeks (with at least one being depressed mood or anhedonia):
1. Depressed mood (nearly every day)
2. **Anhedonia** (loss of interest or pleasure — the most reliable diagnostic marker)
3. Significant weight change or appetite disturbance
4. Insomnia or hypersomnia
5. Psychomotor agitation or retardation (observable by others)
6. Fatigue or loss of energy
7. Feelings of worthlessness or excessive guilt
8. Difficulty concentrating or indecisiveness
9. Recurrent thoughts of death or suicidal ideation

MDD is distinct from **bereavement**, **bipolar depression** (which requires prior manic/hypomanic episode), **persistent depressive disorder** (dysthymia, ≥2 years of milder depression), and **secondary depression** (hypothyroidism, Cushing's, interferon therapy, corticosteroids).

## Structure

### Neuroanatomy of depression

Neuroimaging and postmortem studies consistently identify structural and functional abnormalities across a depression-specific circuit:

**Subgenual anterior cingulate cortex (sgACC, Brodmann Area 25):**
- Most consistently hyperactivated region in acute depression; increased metabolism on PET correlates with depression severity
- Deep brain stimulation (DBS) of white matter tracts adjacent to Area 25 (subcallosal cingulate tract) produces rapid remission in treatment-resistant MDD (~60% response at 1 year — Kennedy et al., NEJM Evidence 2022)
- Projects to brainstem monoamine nuclei (raphe, locus coeruleus) and hypothalamus; hyperactivation suppresses monoaminergic output and dysregulates HPA axis

**Hippocampus:**
- Volume reduced 2–5% in first-episode MDD; further atrophy (~0.5-1% per episode) with recurrent episodes — reversible with sustained antidepressant treatment
- Loss of CA1 and dentate gyrus pyramidal neurons; reduced subgranular zone neurogenesis
- Mechanism: glucocorticoid excess → GR-mediated BDNF suppression → loss of trophic support → dendritic atrophy and neuronal apoptosis

**Dorsolateral prefrontal cortex (DLPFC):**
- Reduced volume and metabolic activity (hypofrontality) correlates with cognitive symptoms (concentration, decision-making)
- Target of repetitive transcranial magnetic stimulation (rTMS; FDA-cleared for MDD)
- Reduced DLPFC activity → impaired top-down regulation of limbic hyperreactivity

**Amygdala:**
- Hyperactivated (increased metabolism; exaggerated to emotional stimuli); enlarged in first-episode MDD vs. controls
- Hyperactive amygdala → exaggerated negative emotional processing, increased stress reactivity, fear generalization → rumination

**Default Mode Network (DMN):**
- Increased DMN activity and connectivity during MDD → maladaptive self-referential processing (rumination, negative self-focus)
- Psilocybin and ketamine rapidly disrupt DMN hyperconnectivity → correlated with antidepressant response

## Function

### Monoamine hypothesis

The classical **monoamine deficiency hypothesis** (Schildkraut 1965) proposed that MDD arises from insufficient monoamine (serotonin, norepinephrine, dopamine) neurotransmission. Evidence:
- All effective conventional antidepressants increase monoamine availability (SSRI → 5-HT; SNRI → 5-HT + NE; TCAs → 5-HT + NE + DA; MAOIs → all monoamines)
- Tryptophan depletion (reduces brain 5-HT) causes relapse in SSRI-remitted patients
- Catecholamine depletion (alpha-methyl-para-tyrosine → reduces NE/DA) triggers depression in remitted patients treated with NE-preferring antidepressants

**Limitations:** The monoamine hypothesis alone is insufficient:
- Monoamine increase occurs within hours of antidepressant administration, but clinical benefit requires 2–4 weeks → downstream synaptic remodeling (BDNF-neuroplasticity) is required
- ~30% of patients do not respond to monoamine-targeting antidepressants (treatment-resistant depression)
- Tianeptine (a serotonin reuptake enhancer, not blocker) is an effective antidepressant → simple monoamine increase is not sufficient

### Neuroplasticity hypothesis (BDNF hypothesis)

Duman and Aghajanian (2012) [^duman-2012-bdnf-depression] proposed that MDD results from impaired synaptic plasticity — specifically from reduced BDNF-TrkB signaling in hippocampus and prefrontal cortex:

- **Chronic stress** → elevated cortisol → GR-mediated suppression of BDNF promoters → reduced BDNF in hippocampus → dendritic retraction, reduced LTP, impaired neurogenesis → depression-like phenotype (in rodent models)
- **Antidepressants** → ultimately increase BDNF regardless of primary mechanism (SSRI → 5-HT → CREB → BDNF; ketamine → AMPA stimulation → BDNF release; ECT → seizure → massive BDNF induction)
- Intra-hippocampal BDNF infusion produces antidepressant-like effects; dominant-negative TrkB blocks antidepressant response in rodents

### HPA axis dysregulation

In ~50% of MDD patients (especially severe/melancholic depression):
- **Elevated CRH** in CSF (excess hypothalamic drive)
- **Elevated basal cortisol** and flattened diurnal variation
- **Blunted dexamethasone suppression test (DST):** Failure to suppress cortisol after 1 mg dexamethasone (a GR agonist) indicates hypercortisolemia and HPA axis escape
- **Mechanism:** Reduced hippocampal GR expression (due to early-life stress and BDNF loss) → impaired negative feedback → HPA hyperactivity → more cortisol → more BDNF suppression → further hippocampal atrophy (vicious cycle)

Normalization of HPA axis (return of DST suppression) predicts remission better than symptom rating scales.

### Neuroinflammation

Approximately 30–40% of MDD patients have elevated inflammatory markers:
- **Elevated IL-6, TNF-α, CRP** in blood correlate with depression severity
- **IDO pathway activation:** Inflammatory cytokines induce indoleamine 2,3-dioxygenase (IDO) → converts tryptophan to kynurenine instead of serotonin → depletes serotonin and produces glutamate (quinolinic acid) → excitotoxic → NMDA receptor-mediated hippocampal injury
- **Microglia activation:** Translocator protein (TSPO) PET shows increased microglial activation in MDD vs. controls
- Anti-inflammatory antidepressants (celecoxib adjunct, infliximab for high-CRP patients) show efficacy in inflammatory subtype MDD

## Pathology

### Subtypes

| Subtype | Characteristics | Treatment implication |
|:---|:---|:---|
| **Melancholic depression** | Diurnal variation (worse AM), loss of reactivity, psychomotor retardation, marked anhedonia | TCAs or high-dose SSRIs; ECT for severe; ketamine; NE-targeted drugs (SNRIs, desipramine) |
| **Atypical depression** | Mood reactivity preserved; hypersomnia, hyperphagia, leaden paralysis, rejection sensitivity | MAOIs historically most effective; SSRIs effective; avoid TCAs |
| **Psychotic depression** | Delusions or hallucinations co-occurring with depression | Antidepressant + antipsychotic; ECT is first-line for psychotic depression |
| **Postpartum depression (PPD)** | Within 4 weeks post-delivery; associated with allopregnanolone withdrawal | Brexanolone (GABA-A neurosteroid) — FDA 2019; SSRIs safe in breastfeeding |
| **Seasonal affective disorder (SAD)** | Winter depression; hypersomnia, hyperphagia, carbohydrate craving | Light therapy (10,000 lux, 30 min AM); bupropion XL preventive |
| **Treatment-resistant depression (TRD)** | Failure of ≥2 adequate antidepressant trials | Augmentation (lithium, atypical antipsychotic, thyroid), ketamine/esketamine, ECT, DBS, psilocybin |

### Antidepressant pharmacology [^cipriani-2018-antidepressants-meta]

**First-line treatments — SSRIs and SNRIs:**

| Drug | Class | Mechanism | Notes |
|:---|:---|:---|:---|
| Escitalopram | SSRI | Most selective SERT inhibitor | Best efficacy/tolerability ratio in Cipriani 2018 meta-analysis |
| Sertraline | SSRI | SERT + weak DAT inhibition | Preferred in cardiac patients; most studied |
| Fluoxetine | SSRI | SERT; long half-life (2–6 days) | Low discontinuation syndrome risk; Prozac |
| Venlafaxine | SNRI | SERT >> NET at low doses; SERT + NET at higher doses | Better efficacy than SSRIs in severe depression |
| Duloxetine | SNRI | SERT + NET (more balanced than venlafaxine) | Also FDA-approved for chronic pain, diabetic neuropathy |
| Mirtazapine | Tetracyclic | α2 antagonist + 5-HT2A/C antagonist | No sexual side effects; sedating; weight gain; effective |

**Fast-acting antidepressants:**

**Ketamine/esketamine:**
- IV ketamine (0.5 mg/kg over 40 min): antidepressant effect within 2–4 hours; 70% response in treatment-resistant MDD (vs. ~30% for conventional antidepressants) [^zarate-2006-ketamine-rapid]
- Mechanism: NMDA receptor block → disinhibition of pyramidal neurons → AMPA stimulation → BDNF release → TrkB → mTOR → rapid synaptogenesis
- Esketamine (Spravato, nasal spray): FDA-approved 2019 for TRD and MDD with acute suicidal ideation; 56 mg or 84 mg twice weekly → weekly → biweekly
- Limitations: dissociation, transient BP increase, abuse potential; administered in supervised medical setting

**Brexanolone (Zulresso):**
- IV GABA-A neurosteroid agonist (synthetic allopregnanolone); FDA-approved 2019 for postpartum depression
- 60-hour IV infusion; ~70% remission vs. ~30% placebo; rapid effect (24–48h)
- Mechanistic implication: allopregnanolone withdrawal postpartum is a key trigger for PPD

**Psilocybin:**
- Two-dose psilocybin therapy (25 mg) produced sustained antidepressant effect at 12 weeks (Compass Pathways COMP360 Phase 2, 2022): 29% remission vs. 8% placebo at 3 weeks
- Mechanism: 5-HT2A agonism in PFC → disruption of DMN → enhanced cognitive flexibility; BDNF increase; neuroplasticity
- FDA Breakthrough Therapy designation for TRD; Phase 3 trials ongoing

**ECT and Neuromodulation:**
- **ECT (electroconvulsive therapy):** Most effective treatment for severe/refractory MDD (80% response); mechanism: generalized tonic-clonic seizure → massive monoamine and BDNF release → hippocampal neurogenesis; retrograde amnesia is primary side effect
- **rTMS (repetitive TMS):** 10 Hz stimulation of left DLPFC; FDA-cleared; ~40-50% response in TRD; Deep TMS (H-coil) reaches sgACC
- **DBS:** Subcallosal cingulate tract stimulation; 60% response in severe TRD at 1 year; investigational

### Risk and protective factors

**Genetic:** Heritability ~37% (lower than schizophrenia or bipolar); polygenic; GWAS identified >100 loci; 5-HTTLPR (SLC6A4 promoter) × stress interaction; BDNF Val66Met

**Environmental risk factors:** Early-life adversity (childhood abuse/neglect — 3× increased risk), chronic stress, socioeconomic factors, social isolation, chronic medical illness (cardiovascular, chronic pain)

**Protective factors:** Social support, aerobic exercise (reduces MDD risk by 25–35%), adequate sleep, omega-3 fatty acids, mindfulness, purpose/meaning

## Connections

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — reduced serotonergic neurotransmission is central to MDD; SSRIs are first-line antidepressants; tryptophan depletion triggers depressive relapse in remitted patients; 5-HT1A autoreceptor desensitization determines the delayed therapeutic onset of SSRIs.

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — NE deficit underlies psychomotor retardation and concentration difficulty in MDD; SNRIs (venlafaxine, duloxetine) block NET to raise synaptic NE; mirtazapine (α2 antagonist) increases NE and 5-HT by blocking autoreceptors; melancholic depression preferentially responds to NE-targeting drugs.

- `connects-to` → **[Cortisol](../../../03-molecular/cortisol/README.md)** — HPA axis hyperactivation in MDD — elevated CRH, cortisol, and blunted dexamethasone suppression — causes hippocampal atrophy via GR-mediated BDNF suppression; cortisol normalization predicts antidepressant response; mifepristone and CRH receptor antagonists are experimental antidepressants.

- `connects-to` → **[CRH](../../../03-molecular/crh/README.md)** — CRH hyperdrive from PVN and CeA drives the HPA hyperactivation of MDD; elevated CSF CRH and blunted dexamethasone suppression are the most replicated biological findings in MDD; CRHR1 antagonists and mifepristone (GR antagonist) show antidepressant activity; CRH excess drives hippocampal BDNF suppression and dendritic retraction.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — BDNF deficiency is central to the neuroplasticity hypothesis of MDD; stress reduces hippocampal BDNF via glucocorticoid-mediated CREB repression; all effective antidepressants (SSRIs, MAOIs, ketamine, ECT) ultimately normalize BDNF; Val66Met SNP increases MDD vulnerability.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — MDD involves reduced hippocampal volume (~2% per episode), DLPFC hypofrontality, hyperactive amygdala, and sgACC (Area 25) hyperactivation; functional DLPFC–limbic dysconnectivity; sgACC DBS produces rapid remission in severe TRD by normalizing Area 25 hypermetabolism.

- `connects-to` → **[ACTH](../../../03-molecular/acth/README.md)** — MDD shows HPA hyperdrive: CRH excess → ACTH hypersecretion → hypercortisolemia; paradoxically, the CRH stimulation test reveals blunted ACTH response (indicating corticotroph downregulation from chronic CRH excess); normalization of the ACTH/cortisol rhythm with antidepressant treatment reliably predicts and follows clinical remission.

- `connects-to` → **[Prolactin](../../../03-molecular/prolactin/README.md)** — antipsychotic-induced hyperprolactinemia causes sexual dysfunction and anhedonia driving non-adherence; postpartum prolactin dynamics (peaking at delivery then falling) may modulate MDD vulnerability via dopaminergic systems; cabergoline has shown adjunctive antidepressant effects in small trials.

- `connects-to` → **[Testosterone](../../../03-molecular/testosterone/README.md)** — Male hypogonadism (T <300 ng/dL) predicts MDD risk; testosterone deficiency causes fatigue, anhedonia, and low libido indistinguishable from MDD; TRT has adjunctive antidepressant efficacy in hypogonadal men; SSRI-treated men with residual anhedonia benefit from TRT augmentation.

- `connects-to` → **[Estrogen](../../../03-molecular/estrogen/README.md)** — Perimenopausal estrogen fluctuations trigger or worsen MDD; transdermal estradiol (100 mcg/day patch) has antidepressant efficacy in perimenopausal women; PMDD involves abnormal CNS sensitivity to allopregnanolone (progesterone metabolite) fluctuations, not estrogen deficiency.

- `connects-to` → **[Thyroid Hormones](../../../03-molecular/thyroid-hormones/README.md)** — Hypothyroidism causes reversible depressive syndrome indistinguishable from MDD; TSH >10 mIU/L is a diagnostic exclusion for MDD; subclinical hypothyroidism accounts for ~10% of refractory MDD; T3 (25-50 mcg/day) augments antidepressant response in treatment-resistant depression.

- `connects-to` → **[Progesterone](../../../03-molecular/progesterone/README.md)** — Luteal allopregnanolone fluctuations drive PMDD and PPD; declining P4 post-delivery triggers PPD; brexanolone (IV allopregnanolone) and zuranolone (oral) treat PPD; PMDD responds to SSRIs, combined OCP, or GnRH agonist; progesterone withdrawal worsens anxiety.

- `connects-to` → **[Melatonin](../../../03-molecular/melatonin/README.md)** — Seasonal affective disorder (winter depression) involves delayed circadian phase and abnormal melatonin timing; agomelatine (MT1/MT2 agonist + 5-HT2C antagonist) is an approved antidepressant with circadian phase-advancing effects; light therapy resets SCN/melatonin phase in SAD.
- `connects-to` → **[Vasopressin](../../../03-molecular/vasopressin/README.md)** — AVP is elevated in PVN and CSF of depressed patients; V1bR co-drives HPA hyperactivation with CRH → excess ACTH and cortisol; V1b antagonist SSR149415 showed antidepressant effects in Phase 2; SSRIs normalise hypersecretion of both CRH and AVP.
- `connects-to` → **[Leptin](../../../03-molecular/leptin/README.md)** — leptin falls during caloric restriction → ↓POMC → ↓α-MSH → ↓melanocortin tone; hyperleptinemia (obesity) associates with depressive symptoms; LEPR polymorphisms associate with MDD risk; leptin restores BDNF and reverses anhedonia in diet-induced obesity rodent models.
- `treated-by` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — first-line SSRI for MDD (Cipriani 2018 21-drug meta-analysis); onset 4–6 weeks via SERT inhibition → 5-HT desensitization → BDNF/TrkB synaptic plasticity; only SSRI approved for pediatric MDD (age ≥8); effective for acute and maintenance treatment.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Depression shrinks the hippocampus: chronic stress and high cortisol impair hippocampal neurogenesis and reduce its volume, contributing to mood symptoms—and antidepressants that restore neurogenesis help reverse it, linking stress hormones to brain structure.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Depression involves more than neurotransmitter levels at the neuron: impaired synaptic plasticity, dendritic loss and reduced BDNF-driven connectivity underlie it, which is why rapid agents like ketamine that regrow synapses lift mood faster than monoamine drugs.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation links the immune system to depression: raised IL-6 and other cytokines accompany many depressions, can cause sickness-behavior low mood, and predict poorer antidepressant response—a subtype where anti-inflammatory strategies are studied.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Depression is increasingly seen as a glutamatergic disorder: stress alters glutamate signaling and synaptic plasticity, and the rapid antidepressant ketamine acts on NMDA glutamate receptors—evidence that the monoamine model alone is incomplete.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Depression is linked to the gut-brain axis: the microbiome shapes neurotransmitter and inflammatory signaling reaching the brain via the vagus nerve, and dysbiosis is associated with depression—so the gut is an emerging target beyond the brain itself.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Depression and insomnia are tightly bidirectional: sleep disturbance is a core symptom and often the first sign, and persistent insomnia independently predicts and worsens depression—so treating sleep is integral to treating the mood disorder.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Depression has a neuroinflammatory arm in microglia: activated brain microglia release cytokines that lower serotonin precursors and impair neuroplasticity, linking the immune system to mood and helping explain why inflammation predicts poorer antidepressant response.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Distinguishing depression from bipolar disorder is critical: a depressive episode may be the first sign of bipolar illness, and giving an antidepressant alone can trigger mania—so screening for past hypomania guides whether mood stabilizers are needed.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Anhedonia in depression points to dopamine: beyond serotonin, blunted dopamine reward signaling underlies the loss of pleasure and motivation, which is why some antidepressants and adjuncts target dopamine to relieve symptoms that SSRIs miss.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Depression isn't only low serotonin—it's also low GABA: deficient inhibitory GABA signaling is found in depressed brains, and neurosteroid drugs (brexanolone, zuranolone) that boost GABA receptors rapidly lift mood, especially in postpartum depression.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Depression shows a loss of astrocytes: postmortem brains reveal reduced astrocyte density in mood-regulating regions, impairing the glutamate clearance and neuron support these glial cells provide—a structural face of the illness beyond neurotransmitters.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Oxytocin ties depression to broken social bonds: low signaling of this bonding hormone is linked to the social withdrawal and loss of connection in depression, and it is studied as a route to ease the isolation that deepens the illness.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium influences the depressed brain: it blocks the NMDA receptor and supports neuroplasticity, so low magnesium is linked to depression and supplementation is studied as an adjunct, echoing ketamine's glutamate-targeting action.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Depression is increasingly seen as a synaptic disease: chronic stress prunes synapses in mood circuits, and fast-acting antidepressants like ketamine work by rapidly regrowing them, shifting focus from neurotransmitter levels to synaptic repair.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Depression keeps the adrenal glands overworked: an overactive HPA axis drives them to pour out cortisol, and this sustained stress-hormone excess feeds the cognitive, metabolic and mood disturbances of the illness.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Light is medicine for some depression: bright-light therapy delivers photons that reset the body clock and lift seasonal affective disorder, which short, dim winter days can trigger.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Depression is linked to low zinc: the mineral supports BDNF and tempers NMDA signaling, so deficiency is associated with depressive symptoms and zinc is studied as an add-on to antidepressants.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Depression talks with the gut: through the gut-brain axis, the large intestine's microbes and the serotonin made there influence mood, a two-way link tying digestive health to depression.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Low iron can mimic and worsen depression: iron deficiency causes the fatigue, poor concentration and low mood that overlap with MDD, so iron is checked in the workup of new depression.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Depression alters white matter: oligodendrocyte and myelin abnormalities appear in the mood-circuit tracts, part of the connectivity changes seen on imaging in chronic MDD.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Depression and heart disease feed each other: MDD raises the risk of heart attacks and worsens survival after one, through stress hormones, inflammation and the behaviors it shapes.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Depression may thin the brain's connections: studies find reduced dendritic spines and synapses in mood-regulating regions, and the rapid antidepressant effect of ketamine is thought to work by regrowing them.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D shadows the depressed mind: deficiency is consistently associated with depression, and the vitamin's receptors throughout the brain's mood circuits suggest a role in the seasonal and chronic forms of the illness.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Depression unsettles the stomach: appetite swings up or down, nausea and 'butterflies' are common somatic complaints, and the gut-brain serotonin axis ties mood tightly to digestion.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid impersonates depression: hypothyroidism produces low mood, fatigue, and slowed thinking that lift with hormone replacement, so thyroid function is checked in every depression workup and added as augmentation when standard antidepressants fall short.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Depression has an inflammatory face: raised TNF-α and related cytokines appear in depressed patients, can themselves induce low mood as sickness behavior, and mark the subgroup whose illness may respond to anti-inflammatory strategies.
- `connects-to` → **[Obesity](../obesity/README.md)** — Depression and obesity feed each other: each roughly doubles the risk of the other through shared inflammation, cortisol, and inactivity, and several antidepressants add weight — a metabolic-mood loop that complicates treating either alone.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Depression tracks the reproductive hormones: it surges around the premenstrual phase, after childbirth, and through the menopause transition, the timing that ties mood to estrogen and progesterone shifts and shapes perinatal screening and treatment.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammation may help drive depression: stress activates the NLRP3 inflammasome in microglia to release IL-1β and IL-6, and this neuroinflammation is one explanation for the depressive symptoms seen in inflammatory illness and a target for novel therapies.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Depression makes platelets sticky: their serotonin handling overlaps the brain's, and in depression platelets become hyperreactive — a link to the raised heart-attack and stroke risk, partly offset by SSRIs that blunt platelet aggregation.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — An older neurochemical theory still holds: depression may reflect a cholinergic-adrenergic imbalance with acetylcholine signaling tipped too high, which is why the anticholinergic drug scopolamine can lift mood rapidly in some patients.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Adaptive immunity joins the inflammatory story: shifts toward Th17 helper T cells and altered T-cell profiles accompany depression, extending the inflammation hypothesis beyond microglia and cytokines into the body's broader immune response.
- `connects-to` → **[Stroke](../stroke/README.md)** — Damaged vessels can darken mood: cerebrovascular disease and stroke produce 'vascular depression', with post-stroke depression striking a large share of survivors and worsening their recovery — depression here a consequence of brain injury, not only a risk factor for it.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Depression and diabetes feed each other: depression raises diabetes risk through inactivity, cortisol, and inflammation, while the burden of diabetes deepens depression — a bidirectional loop that worsens control and outcomes in both.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety is depression's constant companion: generalized anxiety disorder co-occurs with major depression in a large share of patients, the mixed anxiety-depression that shares serotonergic biology and responds to overlapping treatments.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Trauma sets the stage for depression: PTSD greatly raises the risk of comorbid major depression, the two sharing HPA-axis dysregulation and overlapping symptoms that complicate diagnosis and worsen prognosis.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Depression smolders with inflammation through NF-κB: psychological stress activates NF-κB-driven cytokine signaling, the inflammatory hypothesis of depression that links it to its raised cardiovascular and metabolic risk.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — A mood disorder that hardens the arteries: depression is an independent risk factor for and consequence of cardiovascular disease, its inflammation, autonomic strain and behavioral effects accelerating atherosclerosis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Low mood tips the blood toward clots: depression is associated with a higher risk of venous thromboembolism, through inflammation, platelet activation and the inactivity that accompanies severe episodes.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Depression and the failing heart feed each other: depression is common in heart failure and independently predicts hospitalization and death, sharing inflammation and autonomic dysregulation, and worsening self-care.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — It is the commonest psychiatric burden of kidney failure: depression is highly prevalent in chronic kidney disease and on dialysis, driven by the illness burden and uremic effects, and it worsens adherence and survival.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Drinking and depression entangle: alcohol use disorder and major depression frequently co-occur, each worsening the other — alcohol used to self-medicate low mood while deepening it, complicating treatment of both.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Low mood quietly thins the bones: depression is associated with reduced bone density through cortisol, inflammation and inactivity, and the SSRIs used to treat it independently lower bone mass and raise fracture risk.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Depression foreshadows and accelerates dementia: late-life depression is both a risk factor for and an early sign of Alzheimer's, sharing inflammatory, vascular and hippocampal changes.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Mood and central pain amplify each other: depression is highly comorbid with fibromyalgia, the two sharing serotonergic and stress-system dysregulation that heightens both low mood and pain sensitivity.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is a disorder of brain circuits and chemistry: depression reflects dysregulation of monoaminergic transmission and limbic-prefrontal networks, with hippocampal and neuroplastic changes underpinning it.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones drive and mimic it: depression features HPA-axis overactivity with high cortisol, and thyroid disease and other endocrine disorders both cause and worsen depressive symptoms.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Inflammation feeds low mood: raised inflammatory cytokines are found in depression and can induce it (sickness behaviour), the basis of the inflammatory hypothesis of mood disorder.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It reaches the gut both ways: appetite and weight change are core symptoms, the gut-brain axis ties it to functional GI disorders, and SSRIs impair platelet serotonin to raise gastrointestinal bleeding risk.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Low mood is felt in the body: depression frequently presents with unexplained muscle and back pain, and is bidirectionally linked with chronic musculoskeletal pain that deepens it.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its drugs can unbalance sodium: SSRIs can cause hyponatraemia from SIADH, particularly in older patients, requiring monitoring after starting treatment.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Heart and mood are bound together: depression worsens outcomes after myocardial infarction and independently raises cardiovascular risk through inflammation, autonomic and behavioural pathways.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It travels with breathing disease: depression is common in COPD and asthma, worsening symptom burden and adherence, and breathlessness itself feeds low mood.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin and mind interact: depression accompanies chronic skin disease such as psoriasis and acne, and the distress of visible disease deepens low mood in turn.
- `connects-to` → **[St John's Wort](../../../03-medicine/02-traditional/st-johns-wort/README.md)** — A herbal antidepressant: St John's wort is effective for mild-to-moderate depression in trials, acting on monoamines, but it dangerously induces drug-metabolising enzymes and risks serotonin syndrome with SSRIs.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet offers a modest adjunct: omega-3 (EPA-rich) supplementation has small antidepressant effects in trials, used alongside but not instead of established therapy for major depression.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — A latent parasite linked to mood: chronic Toxoplasma gondii infection is epidemiologically associated with major depression and suicidal behaviour, possibly through neuroinflammation and altered dopamine.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Depression shadows the dopamine loss: major depression is a common prodrome and comorbidity of Parkinson's disease, sharing degeneration of monoaminergic dopamine, serotonin and noradrenaline systems, so mood symptoms can precede the tremor by years.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — A two-way street with seizures: depression and epilepsy are bidirectionally linked—each roughly doubles the risk of the other—through shared GABA/glutamate imbalance, HPA-axis overactivity and neuroinflammation, and some antidepressant and antiseizure drugs cross over.
- `connects-to` → **[Migraine](../migraine/README.md)** — Pain and mood travel together: major depression and migraine are strongly comorbid and bidirectional, sharing serotonergic dysfunction and central sensitisation, so each worsens the other's course and some drugs like amitriptyline and SNRIs treat both.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — The heart-depression link: depression worsens survival after myocardial infarction and is itself a cardiovascular risk factor, while antidepressants—especially tricyclics—affect the QT interval and cardiac conduction.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Inflammation and mood: chronic inflammatory diseases like rheumatoid arthritis carry high rates of depression, and cytokines (IL-6, TNF) drive the sickness behaviour behind the inflammatory hypothesis of depression.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The gut-brain axis: the intestinal epithelium and its microbiome signal to the brain via the vagus and immune and metabolic pathways, a route increasingly implicated in depression.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Depression within psychosis: major depressive symptoms are common in schizophrenia and define schizoaffective disorder, with shared neurotransmitter and inflammatory biology and a markedly raised suicide risk across both.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Post-viral depression: SARS-CoV-2 infection and the chronic neuroinflammation of long COVID raise rates of new-onset depression, while the pandemic itself drove a global surge in depressive illness.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Inflammation feeds mood: depression is strikingly common in inflammatory bowel disease, a bidirectional link through systemic cytokines, the gut microbiome and the gut-brain axis that worsens both conditions.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory hypothesis: IL-1β and the inflammasome drive the neuroinflammation increasingly implicated in depression, joining IL-6 and TNF-α in the cytokine signature of low mood.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Stress neuropeptide: substance P and its NK1 receptor regulate mood and stress responses, an early antidepressant target that, though clinically disappointing, illuminated depression biology.
- `connects-to` → **[NPY](../../03-molecular/npy/README.md)** — Resilience signal: neuropeptide Y has anti-stress, antidepressant-like effects, and low NPY levels are associated with depression and impaired stress resilience.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — SSRI target: the serotonin transporter is blocked by the SSRIs that are first-line for depression, and its gene variants modulate stress-related depression risk.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — HPA dysregulation: impaired glucocorticoid-receptor feedback underlies the cortisol hypersecretion of melancholic depression, a core stress-axis abnormality of the disorder.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Inflammatory depression: IFN-γ and interferon therapy can precipitate depression by diverting tryptophan from serotonin toward neurotoxic kynurenines, part of the cytokine model of MDD.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Rapid antidepressant target: ketamine's fast antidepressant action depends on mTOR-driven synaptogenesis in the prefrontal cortex, reversing the synaptic loss seen in depression.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — Mood and stress buffering: endocannabinoid CB1 signalling regulates stress reactivity and emotional tone, and deficient endocannabinoid tone is implicated in the anhedonia and stress sensitivity of depression.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Neuroinflammatory trafficking: CCL2 recruits monocytes to the brain in depression, part of the low-grade neuroinflammation increasingly tied to the disorder's pathophysiology.
- `connects-to` → **[NTRK / TrkB](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor mediates the rapid synaptogenesis that underlies ketamine's fast antidepressant effect, the neurotrophin axis whose impairment is a core feature of the neurobiology of depression.
- `connects-to` → **[μ-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — The endogenous μ-opioid system mediates social reward and connection, and its dysfunction contributes to anhedonia—the rationale for low-dose buprenorphine and related opioid-modulating agents in treatment-resistant depression.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Microglial TLR4-driven innate immune activation is a key strand of the inflammatory hypothesis of depression, linking chronic stress, infection, and a leaky gut to the neuroinflammation found in a subset of depressed patients.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Orexin signaling that governs wakefulness, reward and motivation is dysregulated in depression, contributing to the disturbed sleep, fatigue and anhedonia that are core symptoms beyond low mood.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Ghrelin rises with chronic stress and has antidepressant-like central effects, a gut-derived hormone linking appetite, the stress response and mood in the metabolic-psychiatric overlap of depression.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Markers of oxidative stress, partly from xanthine-oxidase activity, are raised in depression, the redox imbalance that—with neuroinflammation—is increasingly implicated in the neurobiology of the disorder.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β is a convergence node for mood regulation and synaptic plasticity, inhibited by lithium and modulated downstream of the serotonergic and BDNF signaling implicated in depression.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — A relative shortfall of regulatory IL-10 against the raised pro-inflammatory cytokines (IL-6, IL-1β and TNF mapped) is part of the neuroinflammatory hypothesis of depression.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement-mediated microglial pruning of synapses contributes to the loss of prefrontal and hippocampal connectivity implicated in the pathophysiology of depression.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped) transduces the inflammatory state increasingly implicated in the pathophysiology and treatment resistance of major depression.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2-regulated antioxidant defense counters the oxidative stress (xanthine-oxidase already mapped) associated with major depression, a redox component of its neurobiology.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of BDNF-TrkB (both already mapped) mediates the synaptic plasticity whose impairment underlies depression and whose restoration accompanies antidepressant response.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-mTOR signaling (mTOR and GSK-3β mapped) downstream of BDNF mediates the rapid synaptogenic antidepressant action of ketamine and the neuroplasticity deficits of major depression.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 reflects the neuroinflammatory activation increasingly implicated in major depressive disorder.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine-driven JAK-STAT signaling (IL-6 mapped) transduces the systemic inflammation associated with major depressive disorder and its treatment resistance.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling (JAK1/2 already mapped) transduces the neuroinflammatory tone implicated in the pathophysiology and treatment resistance of major depressive disorder.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic mitochondrial DNA released during chronic stress engages cGAS-STING, contributing to the neuroinflammation of major depressive disorder.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling underlies the depression induced by type-I-interferon therapy, linking interferon signaling to the inflammatory subtype of major depressive disorder.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT and GSK-3β signaling (AKT and GSK-3β already mapped) regulates the neuronal resilience and oxidative-stress handling implicated in major depressive disorder.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to major depressive disorder.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and mitochondrial stress responses contribute to the neuroplasticity changes of major depressive disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of BDNF-TrkB (BDNF and NTRK already mapped), supports the neuroplasticity compromised in major depressive disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling participates in the metabolic and neuroinflammatory dysregulation of major depressive disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates neuronal resilience and the stress responses implicated in major depressive disorder, a candidate antidepressant mechanism.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (FYN) kinase signaling participates in the NMDA-receptor and synaptic-plasticity mechanisms implicated in major depressive disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with major depressive disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic (early-life-stress) programming implicated in major depressive disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and neuroplasticity processes implicated in major depressive disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in major depressive disorder.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with major depressive disorder.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the stress-responsive neuronal gene programs of major depressive disorder.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the sleep-wake and neuromodulatory processes implicated in major depressive disorder.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microglial activation and neuroinflammation implicated in major depressive disorder.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Brain renin-angiotensin: central angiotensin II modulates stress reactivity and neuroinflammation, and angiotensin-blocking antihypertensives have been associated with lower depression risk, implicating the brain RAS in mood regulation.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic depression: insulin resistance and depression are bidirectionally linked, sharing inflammatory and HPA-axis (cortisol already mapped) pathways, and impaired brain insulin signalling is implicated in the metabolic subtype of major depressive disorder.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid receptors: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response, and their dysregulation is implicated in the HPA-axis abnormalities of depression.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Neurogenesis: VEGF supports the hippocampal neurogenesis and angiogenesis (BDNF already mapped) that antidepressants promote, a vascular-neurotrophic mechanism implicated in recovery from depression and in the reduced hippocampal volume seen in the illness.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammation: prostaglandins from activated microglia (already mapped) contribute to the neuroinflammatory dimension of depression, and anti-inflammatory agents that block their synthesis are studied as adjuncts in the inflammatory subtype.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Nitrergic mood signalling: nitric oxide from neuronal nitric oxide synthase modulates monoamine (serotonin already mapped) and glutamatergic transmission, and dysregulated NO-cGMP signalling is implicated in the neurobiology of depression.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Lipids and mood: cholesterol is essential to neuronal membranes and synaptic function, and both the metabolic-syndrome dyslipidaemia comorbid with depression and the associations of very low cholesterol with suicidality link lipids to mood.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron and monoamines: iron is a cofactor for the enzymes making dopamine and serotonin (already mapped), and iron deficiency is associated with the fatigue and low mood of depression, sometimes improving with repletion.
- `connects-to` → **[Bipolar disorder](../bipolar-disorder/README.md)** — Unipolar-bipolar distinction: distinguishing unipolar major depression from the depressive episodes of bipolar disorder is critical, as antidepressants can precipitate mania, and the two share overlapping mood neurobiology (BDNF and glutamate already mapped).
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Microglial polarisation: IL-4 polarises the microglia (already mapped) toward an anti-inflammatory M2 phenotype (IL-10 already mapped), the balance against the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) shaping the neuroinflammatory subset of depression.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is part of the type-2 arm whose balance against the pro-inflammatory signals shapes the neuroinflammatory dimension of major depression.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and monoamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), and disturbed copper-zinc (already mapped) balance is reported in major depression.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon-induced depression: interferon-α therapy is a classic cause of depression, and the type-I interferon neuroinflammatory (IFN-γ already mapped) signalling is implicated in the pathophysiology of major depression.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic-inflammatory adipokine: adiponectin, with leptin (already mapped), links the obesity and metabolic syndrome (insulin already mapped) to the inflammatory dimension of major depression.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the metabolic-inflammatory (IL-6 already mapped) link to major depression.
- `connects-to` → **[Social anxiety disorder](../social-anxiety-disorder/README.md)** — Anxiety comorbidity: major depression and social anxiety disorder are highly comorbid, sharing the serotonergic (already mapped) dysregulation and the SSRI treatment.
- `connects-to` → **[Panic disorder](../panic-disorder/README.md)** — Panic comorbidity: major depression and panic disorder are comorbid, sharing the serotonergic and noradrenergic (already mapped) dysregulation.
- `connects-to` → **[Opioid use disorder](../opioid-use-disorder/README.md)** — Substance-use comorbidity: major depression is highly comorbid with opioid use disorder (the self-medication, the shared reward — dopamine already mapped — and stress — cortisol already mapped — dysregulation).
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the neuroinflammation (IL-6 and TNF already mapped) implicated in major depressive disorder.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of major depressive disorder.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with major depressive disorder.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation associated with major depressive disorder.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive neuroinflammation: the cytotoxic T cells (perforin pathway) of the CNS-border compartments are part of the adaptive-immune contribution to the neuroinflammation of major depressive disorder.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the type-2 (IgE already mapped) dimension of major depressive disorder.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Stress-modulated NK: the NK-cell number and cytotoxicity, altered by the chronic stress and cortisol (already mapped) reactivity, are part of the peripheral immune dysregulation of major depressive disorder.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) activation and the complement-mediated synapse loss implicated in major depressive disorder.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the neuroinflammation of major depressive disorder.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Neuroinflammatory mediator: histamine (released by brain mast cells and tuberomammillary nucleus neurons) signals through H1/H3 receptors to modulate the HPA axis dysregulation and the norepinephrine-serotonin (already mapped) imbalance of major depressive disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuroimmune alarmin: elevated peripheral TSLP from atopic/allergic comorbidities (mast cells already mapped) activates dendritic cells and drives the neuroinflammatory IL-6/TNF-α (already mapped) cytokine cascade that mediates the depression-allergy comorbidity in MDD.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Neuroinflammation amplifier: bradykinin activates central B2 receptors, amplifying the NF-κB (already mapped) neuroinflammation and norepinephrine (already mapped) release that characterise the stress-induced neuroinflammatory phenotype of major depressive disorder.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Neurocomplement brake: C1-INH controls the classical complement pathway (C3 and C5aR1 already mapped) at the blood-brain barrier and in the choroid plexus, limiting the complement-mediated synaptic pruning and the neuroimmune inflammation of major depressive disorder.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective EPO: erythropoietin, via EPOR on neurons (already mapped) and microglia (already mapped), activates the JAK2/STAT3 (JAK1/2 already mapped) anti-apoptotic pathway and reduces the neuroinflammatory IL-6 (already mapped) burden of major depressive disorder.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Astrocyte ECM remodelling: periostin, expressed by reactive astrocytes (already mapped) in the neuroinflamed brain (already mapped) of MDD, promotes the extracellular matrix changes that accompany glial morphology shifts and synaptic (already mapped) remodelling in depression.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenoprotein antidepressant: selenium, via neuronal and microglial (both already mapped) selenoproteins (GPx/TrxR), quenches the reactive oxygen species and neuroinflammatory IL-6 (already mapped) burden underlying the oxidative-stress phenotype of major depressive disorder.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Neurocomplement factor H: factor H, the key complement regulator (C3 and C5aR1 already mapped), controls complement-mediated synaptic pruning and microglial (already mapped) activation in the MDD brain, limiting the neuroimmune cascade at the blood-brain barrier.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement C5: complement C5, cleaved to C5a (C5aR1 already mapped) and MAC, drives neuroinflammatory astrocytic (already mapped) activation and C1q-mediated synaptic pruning linking inflammatory MDD to hippocampal grey-matter loss and cognitive impairment.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — MDD iodine HPT axis: iodine, as the essential substrate for thyroid hormone (already mapped) biosynthesis, supports the HPT axis; iodine insufficiency deepens the neuroimmune NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory burden of major depressive disorder.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — MDD sodium neuroimmune: sodium, at supraphysiological levels, activates microglial (already mapped) NF-κB (already mapped) and IL-6 (already mapped) signalling toward a pro-inflammatory macrophage (already mapped) state, amplifying the neuroinflammatory burden of MDD.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — MDD potassium neuronal: potassium maintains synaptic (already mapped) resting potential and BDNF (already mapped) signalling; potassium dyshomeostasis in the MDD hippocampus (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation in MDD.

[^cipriani-2018-antidepressants-meta]: Cipriani A, Furukawa TA, Salanti G, et al. Comparative efficacy and acceptability of 21 antidepressant drugs for acute treatment of adults with major depressive disorder. *Lancet.* 2018;391(10128):1357-1366. [doi:10.1016/S0140-6736(17)32802-7](https://doi.org/10.1016/S0140-6736(17)32802-7) · [PubMed 29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/)
[^zarate-2006-ketamine-rapid]: Zarate CA Jr, Singh JB, Carlson PJ, et al. A randomized trial of an N-methyl-D-aspartate antagonist in treatment-resistant major depression. *Arch Gen Psychiatry.* 2006;63(8):856-864. [doi:10.1001/archpsyc.63.8.856](https://doi.org/10.1001/archpsyc.63.8.856) · [PubMed 16894061](https://pubmed.ncbi.nlm.nih.gov/16894061/)
[^duman-2012-bdnf-depression]: Duman RS, Aghajanian GK. Synaptic dysfunction in depression: potential therapeutic targets. *Science.* 2012;338(6103):68-72. [doi:10.1126/science.1222939](https://doi.org/10.1126/science.1222939) · [PubMed 23042884](https://pubmed.ncbi.nlm.nih.gov/23042884/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
