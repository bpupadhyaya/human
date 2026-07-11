---
schema: human-scale-entry/v1
id: schizophrenia
name: Schizophrenia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Schizophrenia (1% lifetime risk) is a severe psychotic disorder with positive symptoms (hallucinations, delusions), negative symptoms (avolition, flat affect), and cognitive deficits; mesolimbic dopamine D2 hyperactivity drives psychosis; all antipsychotics block D2 receptors."
aliases: ["schizophrenia", "psychosis", "positive symptoms", "negative symptoms", "dopamine hypothesis", "NMDA hypofunction", "antipsychotic", "clozapine", "haloperidol", "schizophrenia spectrum"]
sources:
  - id: howes-2009-dopamine-hypothesis
    type: peer-reviewed
    cite: "Howes OD, Kapur S. The dopamine hypothesis of schizophrenia: version III—the final common pathway. Schizophr Bull. 2009;35(3):549-562."
    doi: "10.1093/schbul/sbp006"
    pmid: "19325164"
    url: "https://doi.org/10.1093/schbul/sbp006"
    accessed: "2026-06-08"
  - id: moghaddam-2012-glutamate
    type: peer-reviewed
    cite: "Moghaddam B, Javitt D. From revolution to evolution: the glutamate hypothesis of schizophrenia and its implication for treatment. Neuropsychopharmacology. 2012;37(1):4-15."
    doi: "10.1038/npp.2011.181"
    pmid: "21956446"
    url: "https://doi.org/10.1038/npp.2011.181"
    accessed: "2026-06-08"
  - id: leucht-2013-antipsychotics-meta
    type: peer-reviewed
    cite: "Leucht S, Cipriani A, Spineli L, et al. Comparative efficacy and tolerability of 15 antipsychotic drugs in schizophrenia: a multiple-treatments meta-analysis. Lancet. 2013;382(9896):951-962."
    doi: "10.1016/S0140-6736(13)60733-3"
    pmid: "23810019"
    url: "https://doi.org/10.1016/S0140-6736(13)60733-3"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Mesolimbic D2 hyperactivity drives positive symptoms (hallucinations, delusions); mesocortical D1 hypofunction in PFC drives negative and cognitive symptoms; all antipsychotics achieve therapeutic effect via D2 blockade (60-80% receptor occupancy threshold)."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "NMDA receptor hypofunction in PFC parvalbumin interneurons underlies cognitive and negative symptoms; ketamine (NMDA antagonist) reproduces full schizophrenia phenotype; glycine-site NMDA co-agonists and AMPA potentiators are experimental treatments."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Parvalbumin interneuron hypofunction in PFC — reduced GAD67, impaired GABA synthesis — causes deficient gamma oscillations that underlie working memory deficits; GABAergic interneuron loss may be primary, upstream of dopamine and glutamate dysregulation."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "5-HT2A blockade in PFC by atypical antipsychotics (clozapine, olanzapine, risperidone) enhances dopaminergic output; 5-HT2A agonism by hallucinogens (LSD, psilocybin) models positive symptoms; serotonin-dopamine interaction shapes atypical antipsychotic efficacy."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Schizophrenia involves enlarged ventricles, reduced gray matter in DLPFC, superior temporal gyrus, and hippocampus; functional dysconnectivity between PFC and temporal/limbic regions on fMRI; PV interneuron density is reduced in DLPFC and hippocampus post-mortem."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Antipsychotic D2 blockade at the pituitary tuberoinfundibular pathway removes TIDA inhibition → hyperprolactinemia; risperidone/haloperidol cause greatest elevation; galactorrhea, sexual dysfunction, and bone loss are key non-adherence drivers in schizophrenia."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "H1R inverse agonists (clozapine, olanzapine, quetiapine) drive antipsychotic weight gain and sedation; H3R heteroreceptors on DA/5-HT terminals modulate monoamine release; histaminergic TMN arousal neurons are implicated in arousal deficit and cognitive symptoms in schizophrenia."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Schizophrenia's cellular lesion centers on the parvalbumin fast-spiking GABAergic interneuron of the prefrontal cortex and hippocampus: reduced GAD67 and impaired firing degrade the gamma oscillations behind working memory — upstream of the dopamine and glutamate abnormalities."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Schizophrenia and bipolar disorder overlap genetically and clinically: they share risk variants (CACNA1C) and the schizoaffective category, and both feature psychosis — but schizophrenia is dominated by chronic negative/cognitive deficits, bipolar by episodic mood elevation."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus is a key schizophrenia node: reduced in volume with fewer parvalbumin interneurons, and an overactive anterior hippocampus may drive aberrant dopamine release via the subiculum-VTA pathway — linking memory deficits to the dopamine dysregulation behind psychosis."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia are central to a leading schizophrenia hypothesis: complement-C4-tagged synapses are over-pruned by microglia in adolescence, and the strongest common genetic risk maps to the C4 locus—excess synaptic elimination may underlie the disorder's grey-matter loss."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Schizophrenia and autism share neurodevelopmental roots and genetics: overlapping copy-number variants (22q11, 16p11) and synaptic genes underlie both, sitting on a continuum of early brain miswiring—though autism presents in childhood and schizophrenia later."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes contribute to the glutamate dysfunction of schizophrenia: by clearing synaptic glutamate and supplying the NMDA co-agonist D-serine, astrocyte dysfunction can impair NMDA-receptor signaling—the basis of the glutamatergic hypothesis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Schizophrenia and depression overlap and can be hard to separate: depression often complicates schizophrenia and raises suicide risk, and the two share genetic and neurochemical substrates—so mood symptoms are assessed throughout the illness."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Schizophrenia and epilepsy are bidirectionally linked: each roughly doubles the risk of the other, temporal-lobe epilepsy can produce schizophrenia-like psychosis, and they share glutamate and GABA disturbances—genuinely overlapping disorders."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Schizophrenia involves oligodendrocyte and white-matter abnormalities, not just neurons: fewer oligodendrocytes and disrupted myelination impair long-range connectivity, supporting a 'dysconnectivity' model where faulty wiring underlies the illness."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF deficits link schizophrenia to disrupted neurodevelopment: reduced brain-derived neurotrophic factor impairs synaptic plasticity and cortical circuit maturation, fitting the neurodevelopmental model in which schizophrenia's roots predate its psychotic onset by years."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Cannabis use can precipitate and worsen schizophrenia: heavy adolescent use raises the risk of developing psychosis and triggers relapse in patients, since THC perturbs the dopamine and endocannabinoid systems—so cannabis avoidance is part of schizophrenia management."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Acetylcholine is an emerging schizophrenia target beyond dopamine: muscarinic agonists (xanomeline) improve psychosis without blocking dopamine, so the cholinergic system shapes symptoms—a shift from the dopamine-only model of antipsychotic action."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Schizophrenia is increasingly seen as a synaptic disorder: excessive synaptic pruning in adolescence—linked to complement (C4) and microglia—thins prefrontal connectivity, so it is conceived as a disease of disrupted synapses, not just dopamine."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune system is implicated in schizophrenia: a complement-C4 risk variant drives excessive microglial synaptic pruning, and maternal infection raises offspring risk, so neuroinflammation and immune-mediated synapse loss feature in current models of the disease."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Schizophrenia shortens life mainly through cardiovascular disease: antipsychotic-related weight gain and metabolic syndrome, plus smoking and poor access to care, cause excess heart disease—so patients die 15-20 years early, largely of cardiovascular causes."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Schizophrenia may involve excessive synaptic pruning via complement: the strongest common-variant risk lies in complement C4, which tags synapses through C3 for microglial removal, so over-pruning in adolescence could thin the cortical connections seen in the disease."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Prenatal and placental factors raise schizophrenia risk: maternal infection, malnutrition and obstetric complications acting through the placenta interact with genetic risk, supporting a neurodevelopmental origin set in motion before birth."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut-brain axis is implicated in schizophrenia: altered gut microbiota and intestinal inflammation can influence neurotransmitters and immune signaling reaching the brain, an emerging factor beyond the classic dopamine and glutamate models."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Schizophrenia's strongest genetic hits include a calcium channel: CACNA1C and other voltage-gated calcium channel genes top the risk lists, so disturbed calcium signaling in neurons—shared with bipolar disorder—is a core piece of its biology."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Maternal IL-6 links infection to schizophrenia: prenatal immune activation, signaled through IL-6, perturbs fetal brain development and raises later risk—evidence that inflammation in pregnancy is one road into the disorder."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Stress and cortisol shape schizophrenia's onset: an overactive HPA axis and high cortisol mark the prodrome and can precipitate first psychosis in vulnerable people, the hormonal arm of the stress-diathesis model."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium touches schizophrenia's glutamate problem: it gates the NMDA receptor, central to the glutamate-hypofunction theory of the illness, so disturbed magnesium handling can shift the excitation-inhibition balance behind psychosis."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Stress and the adrenal glands shape schizophrenia: an overactive HPA axis drives the adrenals to pour out cortisol, and this stress-hormone surge marks the prodrome and can tip vulnerable people into first psychosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "A gut-brain axis is emerging in schizophrenia: an altered intestinal microbiome and gut inflammation may influence neurotransmitters and immune signals reaching the brain, linking the large intestine to psychotic illness."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Schizophrenia disturbs synaptic zinc: this trace metal tunes the NMDA glutamate receptors at the core of the disease's signaling, so zinc dysregulation is studied in its synaptic and cognitive deficits."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Schizophrenia's deadliest complication is the heart: antipsychotics prolong the QT and drive metabolic syndrome, and patients die of cardiovascular disease years early—the leading cause of their shortened lifespan."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Antipsychotics fatten the adipocytes: the drugs that quiet psychosis also drive weight gain and fat accumulation, fueling the metabolic syndrome and diabetes that burden treated schizophrenia."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons reveal the schizophrenic brain's structure and chemistry: MRI shows enlarged ventricles and thinned gray matter, while PET tracers map the striatal dopamine excess that antipsychotics aim to dampen."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye carries a schizophrenia signature: smooth-pursuit eye movements are jerky and broken in patients and their unaffected relatives, a heritable endophenotype that points to the brain-wiring deficits behind the illness."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D in the womb shapes later risk: low maternal vitamin D during fetal brain development is an established schizophrenia risk factor, helping explain the disease's links to winter births and higher latitudes."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The most effective drug demands blood counts: clozapine, reserved for treatment-resistant schizophrenia, can wipe out neutrophils into a life-threatening agranulocytosis, so patients undergo mandatory regular neutrophil monitoring to use it safely."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Antipsychotics tax the metabolic organs: second-generation agents like olanzapine and clozapine drive weight gain and insulin resistance, straining the pancreas toward the diabetes and metabolic syndrome that shorten lives in schizophrenia."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Many antipsychotics tug at the heart's potassium gate: by blocking the hERG potassium channel they prolong the QT interval, a delayed repolarization that in susceptible patients can tip into the dangerous arrhythmia torsades de pointes."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "A treatable mimic hides among the cases: anti-NMDA-receptor encephalitis produces psychosis indistinguishable from schizophrenia, its autoantibodies against the NMDA receptor a reason to test, since immunotherapy can reverse what looks like a primary psychotic break."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "A brain parasite shadows the risk: chronic Toxoplasma gondii infection, which encysts in the brain and nudges dopamine, is consistently associated with a modestly higher rate of schizophrenia, one strand of the disease's infection-and-immune hypothesis."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The drugs reach into reproduction: by blocking dopamine, many antipsychotics lift prolactin into galactorrhea, amenorrhea, and sexual dysfunction, side effects that erode adherence and reproductive health in schizophrenia."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Schizophrenia and insulin resistance are entangled: antipsychotics blunt insulin sensitivity and drive weight gain, and even drug-naive patients show glucose dysregulation, so the metabolic syndrome that shortens lives in schizophrenia is partly built into the illness."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "One antipsychotic can inflame the heart muscle: clozapine, the most effective drug for resistant schizophrenia, can cause myocarditis and cardiomyopathy by injuring cardiomyocytes, so cardiac monitoring is mandatory when it is started."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Treatment commonly brings weight gain: many antipsychotics, especially olanzapine and clozapine, drive substantial obesity through appetite and metabolic effects, a major reason for the metabolic syndrome and shortened life expectancy in schizophrenia."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "The sugar disease often follows: schizophrenia carries a raised risk of type 2 diabetes both from antipsychotics that directly impair insulin signaling — sometimes within weeks, beyond their weight effect — and from an intrinsic predisposition shared with the illness."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "An immune signature runs alongside: shifts in helper T-cell subsets and raised inflammatory cytokines appear in schizophrenia, supporting a neuroinflammatory contribution that complements the microglial pruning and complement findings."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "The body clock is unsettled: melatonin rhythms are blunted and sleep-wake cycles disrupted in schizophrenia, both as a feature of the illness and a target, with melatonin used to ease the insomnia and metabolic effects of treatment."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Neuroinflammation has an inflammasome arm: NLRP3-driven IL-1β release is implicated in the microglial activation and developmental disruption proposed in schizophrenia, complementing the complement-mediated synaptic pruning findings."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Substance use runs high: alcohol use disorder is markedly more common in schizophrenia, used to self-medicate symptoms yet worsening psychosis, adherence, and the metabolic and cardiovascular toll of the illness."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "The mortality gap reaches the brain: metabolic syndrome, antipsychotic effects, and smoking give schizophrenia a raised stroke risk, part of the cardiovascular disease that shortens life expectancy by 15-20 years."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The antipsychotics themselves clot the veins: most antipsychotic drugs independently raise venous thromboembolism risk, compounded by sedation, immobility and obesity, so DVT and pulmonary embolism are a recognized treatment hazard."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Blocking dopamine mimics the disease: D2-antagonist antipsychotics induce a drug-induced parkinsonism — bradykinesia, rigidity and tremor — that can be hard to distinguish from idiopathic Parkinson's, the pharmacologic mirror of its dopamine deficit."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Clozapine can strip the neutrophils: the agranulocytosis caused by clozapine, the drug reserved for resistant schizophrenia, removes the front-line defense against bacteria and can precipitate life-threatening sepsis, mandating blood-count monitoring."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its antipsychotics and metabolic burden weaken the heart: clozapine can cause myocarditis and cardiomyopathy, and the diabetes, obesity and dyslipidemia driven by antipsychotics accelerate the cardiac disease that shortens schizophrenia lifespans."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Very high smoking rates scar the lungs: people with schizophrenia smoke heavily, and the resulting chronic obstructive pulmonary disease is a major contributor to their markedly reduced life expectancy."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Prolactin-raising drugs thin the bones: many antipsychotics block dopamine to raise prolactin, suppressing sex hormones, and the resulting hypogonadism — with inactivity and smoking — accelerates bone loss toward osteoporosis."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Obsessions commonly accompany psychosis: a substantial minority with schizophrenia have comorbid obsessive-compulsive symptoms (schizo-obsessive presentations), and some antipsychotics can themselves provoke them."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Clozapine can paralyse the gut: the most effective antipsychotic causes severe gastrointestinal hypomotility, with constipation that can progress to ileus, obstruction and life-threatening bowel complications."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety pervades the illness: prominent anxiety and worry accompany the prodrome, active psychosis and insight into schizophrenia, frequently meeting criteria for a comorbid generalized anxiety disorder."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is fundamentally a brain disorder: schizophrenia involves dopaminergic and glutamatergic dysregulation, neurodevelopmental grey-matter changes and disrupted connectivity, the neurobiology underlying psychosis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its drugs flood the body with prolactin: dopamine-blocking antipsychotics raise prolactin, causing galactorrhoea, amenorrhoea and hypogonadism, and they drive the metabolic syndrome of weight gain and diabetes."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Very heavy smoking scars the lungs: people with schizophrenia smoke at extremely high rates, giving high COPD and pneumonia burdens, and clozapine can rarely cause respiratory depression."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Water and muscle breakdown threaten the kidney: psychogenic polydipsia causes water intoxication with hyponatraemia, and neuroleptic malignant syndrome with rhabdomyolysis can cause acute kidney injury."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Antipsychotics act on muscle and movement: they cause acute dystonia, drug-induced parkinsonism and tardive dyskinesia, and neuroleptic malignant syndrome brings life-threatening muscle rigidity."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Drugs and self-neglect mark the skin: chlorpromazine causes photosensitivity and slate-grey pigmentation, and the self-neglect of severe illness contributes to skin and dental problems."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: connects-to
    note: "Maternal infection raises the risk: prenatal exposure to influenza and other infections is linked to higher schizophrenia risk through maternal immune activation affecting fetal brain development."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet is studied in early psychosis: omega-3 supplementation has been trialled to delay transition in those at high clinical risk of psychosis, with mixed results."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "Antidepressants augment treatment: SSRIs like fluoxetine are added to antipsychotics for the depressive and negative symptoms that often accompany schizophrenia."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "It curbs antipsychotic metabolic harm: second-generation antipsychotics cause weight gain, insulin resistance and dyslipidaemia, and metformin is added to blunt the drug-induced metabolic syndrome that widens the cardiovascular mortality gap in schizophrenia."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Trauma feeds psychosis risk: childhood adversity and trauma raise the risk of later schizophrenia, and PTSD itself can present with psychotic features, blurring the boundary between trauma-related and primary psychotic illness."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "A psychotic-symptom differential: borderline personality disorder produces transient stress-related paranoia and dissociation that can mimic schizophrenia, distinguished by the persistence, negative symptoms and course of true psychosis."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep falls apart in psychosis: schizophrenia disrupts sleep architecture—reduced slow-wave sleep and sleep spindles—and insomnia often heralds relapse, with the two sharing dopaminergic and circadian dysregulation."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "Psychosis from the striatum: Huntington's disease frequently produces psychotic symptoms, and its striatal dopamine dysregulation echoes the dopamine hypothesis of schizophrenia—one a degenerative, one a developmental disorder of the same circuits."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Late-life psychosis and shared mechanisms: psychotic features arise in Alzheimer's dementia, and schizophrenia and Alzheimer's share synaptic loss, microglial and complement-driven pruning and neuroinflammation despite their different ages of onset."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Antipsychotics and sudden death: many antipsychotics prolong the QT interval, and schizophrenia carries an elevated risk of sudden cardiac death through arrhythmia and the conduction system."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Clozapine myocarditis: clozapine—the most effective drug for treatment-resistant schizophrenia—can cause an acute myocarditis and cardiomyopathy of the myocardium, monitored closely in the first weeks of treatment."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Hyperprolactinaemia and breast cancer: dopamine-blocking antipsychotics raise prolactin, and sustained hyperprolactinaemia is associated with a modest increase in breast cancer risk in long-treated patients."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Infection and psychosis: maternal infection in pregnancy raises schizophrenia risk (as with influenza and toxoplasma), and severe COVID-19 with its neuroinflammation can precipitate new psychosis, while the pandemic worsened outcomes for patients."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "A psychosis mimic: the vivid hypnagogic hallucinations and REM intrusions of narcolepsy can resemble psychosis, and the two intersect through dopaminergic and thalamic circuits and the drugs that modulate them."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Smoking's toll: very high smoking rates in schizophrenia—partly self-medicating cognitive and sensory-gating deficits with nicotine—drive excess lung cancer and COPD, contributing to the large mortality gap."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "Cannabinoid risk axis: endocannabinoid signalling is dysregulated in schizophrenia, and cannabis use through CB1-receptor agonism is a robust environmental risk factor for psychosis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Social cognition: oxytocin modulates the social cognition and trust deficits central to schizophrenia, and has been explored as an adjunct to antipsychotics."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Neuroinflammation: raised TNF-α and other inflammatory cytokines, with microglial activation, are increasingly implicated in the neurodevelopmental pathology of schizophrenia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Maternal immune activation: IL-1β is a key cytokine of the maternal immune activation linked to schizophrenia risk, and features in the neuroinflammation of the disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Immune dysregulation: altered IFN-γ signalling is part of the immune dysregulation increasingly tied to schizophrenia, linking infection and inflammation to its neurodevelopment."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Noradrenergic arousal: noradrenergic dysregulation contributes to the arousal, attention and stress-response abnormalities seen in schizophrenia alongside the dopamine hypothesis."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitrergic signalling: the schizophrenia risk gene NOS1AP regulates neuronal nitric-oxide synthase, tying NO signalling at the NMDA-receptor synapse to the glutamatergic dysfunction implicated in the disorder."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "DISC1-GSK3 axis: dopamine D2 and DISC1 signalling converge on GSK-3β, a kinase governing neurodevelopment and synaptic plasticity whose dysregulation is implicated in schizophrenia and is inhibited by mood stabilisers."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Maternal immune activation: prenatal type-I-interferon responses to infection raise schizophrenia risk, a key strand of the neurodevelopmental immune hypothesis linking gestational inflammation to later psychosis."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Strongest risk locus: the MHC region on chromosome 6 holds schizophrenia's largest genetic signal, driven largely by complement C4 alleles that increase synaptic pruning — tying the immune-gene locus to the loss of cortical synapses seen in the disease."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Purinergic modulation: the adenosine hypothesis holds that deficient adenosine signalling disinhibits dopamine and glutamate transmission, and adenosine A2A receptors that heteromerise with dopamine D2 receptors are an emerging antipsychotic target."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Synaptic-signalling risk gene: the calcineurin subunit gene PPP3CC is associated with schizophrenia, and calcineurin-knockout mice show schizophrenia-like deficits — implicating this NMDA-coupled phosphatase in the synaptic dysfunction of psychosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "AKT-GSK3β axis: AKT1 is a schizophrenia-susceptibility gene, and dopamine-D2-receptor signalling through the AKT-GSK3β pathway (GSK3β already mapped) is a core node at which antipsychotics and lithium act on the disorder."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Neurodevelopmental synapse: mTOR signalling regulates the activity-dependent protein synthesis and dendritic-spine maturation that are disrupted in schizophrenia, tying its neurodevelopmental origins to synaptic dysfunction."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Metabolic comorbidity: antipsychotics cause weight gain and the metabolic syndrome already mapped here (obesity, type-2 diabetes, metformin), and GLP-1 receptor agonists are increasingly used to counter this iatrogenic metabolic burden."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "AKT1 signalling: AKT1 (mapped) is a schizophrenia-risk gene, and the PI3K-AKT-GSK3β-mTOR axis (AKT, GSK-3β and mTOR already mapped) relays dopamine and neurotrophin signals implicated in the disorder."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "HPA stress reactivity: heightened CRH-driven HPA-axis activity (cortisol mapped) is associated with the onset and relapse of psychosis, linking stress to the dopaminergic dysregulation of schizophrenia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Neurodevelopmental MAPK: neuregulin-ErbB and BDNF-TrkB signalling converge on MAPK-ERK, a pathway implicated in the synaptic and neurodevelopmental abnormalities of schizophrenia."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurodevelopmental plasticity: BDNF signalling through its TrkB receptor (NTRK) supports the cortical neurodevelopment and synaptic plasticity whose disruption is central to schizophrenia."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Maternal-immune-activation link: TLR4-driven microglial neuroinflammation, linked to maternal immune activation and prenatal infection, contributes to the neurodevelopmental origins of schizophrenia."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Redox dysregulation: NRF2-regulated antioxidant defence counters the oxidative stress increasingly implicated in the parvalbumin-interneuron dysfunction of schizophrenia."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 reflects the aberrant microglial synaptic pruning increasingly implicated in the neurodevelopmental pathogenesis of schizophrenia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-driven JAK-STAT signalling (IL-6 mapped) transduces the maternal-immune-activation and chronic inflammation linked to schizophrenia risk."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN regulation of the PI3K-AKT-GSK-3β axis (AKT and GSK-3β mapped) shapes the neurodevelopmental signalling implicated in schizophrenia."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the neuroinflammatory tone implicated in the neurodevelopmental pathophysiology of schizophrenia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the maternal-immune-activation and innate neuroinflammation implicated in schizophrenia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling (type-I interferon already mapped) transduces the maternal-immune-activation interferon exposure epidemiologically linked to schizophrenia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates neuronal metabolism and oxidative-stress handling implicated in schizophrenia."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked mitochondrial and metabolic dysfunction contributes to the neurodevelopmental pathology of schizophrenia."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the innate immune activation and microglial priming associated with schizophrenia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic and neurodevelopmental dysregulation implicated in schizophrenia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling participates in the metabolic and neuroinflammatory disturbances of schizophrenia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the synaptic pruning and neuronal homeostasis implicated in schizophrenia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (FYN) kinase signaling participates in the NMDA-receptor and synaptic-plasticity mechanisms implicated in schizophrenia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the microglial activation and neuroinflammation implicated in schizophrenia."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement signaling, alongside complement-mediated synaptic pruning (complement-C3 already mapped), participates in the synaptic pathology of schizophrenia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neurodevelopmental interneuron migration and neuroimmune interactions implicated in schizophrenia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in schizophrenia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the maternal-immune-activation and neuroinflammatory processes implicated in schizophrenia."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen-protection hypothesis: estrogen modulates dopaminergic transmission, women show later onset and a second incidence peak at menopause, and estrogen adjuncts improve symptoms, a neuroendocrine dimension of schizophrenia beyond the neurotransmitter models."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Antipsychotic metabolic syndrome: second-generation antipsychotics disrupt leptin signalling and drive the weight gain, dyslipidaemia and diabetes that dominate the physical-health morbidity and shortened lifespan of schizophrenia."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: schizophrenia is associated with impaired antioxidant defence and raised oxidative markers, and xanthine-oxidase-derived reactive oxygen species and purine dysregulation contribute to the redox imbalance implicated in its neuropathology."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Brain renin-angiotensin: central angiotensin II modulates dopamine transmission, neuroinflammation and stress reactivity, and angiotensin-blocking drugs are being investigated as adjuncts, implicating the brain RAS beyond the classical neurotransmitters already mapped."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroids: progesterone-derived allopregnanolone modulates GABA-A signalling (GABA already mapped), and fluctuations across the reproductive cycle influence psychosis, part of the neurosteroid and sex-hormone contribution to schizophrenia (estrogen already mapped)."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Developmental iron: iron is a cofactor for dopamine synthesis, and prenatal iron deficiency is an epidemiological risk factor for schizophrenia, linking early-life micronutrient status to the neurodevelopmental origins of the disorder."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammation: prostaglandins from the low-grade neuroinflammation (IL-6 and IL-1 already mapped) and maternal infection implicated in schizophrenia modulate the developing brain, and anti-inflammatory agents are studied as adjuncts."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Clozapine myocarditis: clozapine, the most effective antipsychotic for treatment-resistant schizophrenia, can cause myocarditis and cardiomyopathy, and troponin elevation is monitored to detect this serious adverse effect early."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Neurovascular development: VEGF supports the cerebral angiogenesis and neurotrophic signalling (BDNF already mapped) implicated in the neurodevelopmental abnormalities of schizophrenia, part of its altered brain-vascular biology."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Antipsychotic dyslipidaemia: the second-generation antipsychotics raise cholesterol and drive the metabolic syndrome (insulin and leptin already mapped), a major contributor to the cardiovascular mortality that shortens life in schizophrenia."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-10 counters the microglial pro-inflammatory cytokines (TNF, IL-6 and IL-1 already mapped) implicated in schizophrenia, part of the neuroinflammatory dimension of the disorder."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and psychosis: copper is a cofactor in dopamine metabolism (dopamine already mapped), and disordered copper handling, as in Wilson's disease, can produce a psychosis that mimics schizophrenia, linking the trace metal to the disorder."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Microglial polarisation: IL-4 polarises the microglia (already mapped) toward an anti-inflammatory M2 phenotype (IL-10 already mapped), the balance against the neuroinflammation (TNF, IL-6 and IL-1 already mapped) implicated in schizophrenia."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is part of the type-2 arm whose balance against the pro-inflammatory signals shapes the neuroinflammatory dimension of schizophrenia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic adipokine: resistin, with leptin (already mapped), is part of the adipokine milieu of the metabolic syndrome (insulin and cholesterol already mapped) worsened by the antipsychotics and the disease in schizophrenia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin and resistin (already mapped), completes the adipokine axis of the metabolic syndrome (insulin and cholesterol already mapped) worsened by the antipsychotics in schizophrenia."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "NMDA modulation: magnesium blocks the NMDA receptor (glutamate already mapped), and magnesium dysregulation is implicated in the NMDA-hypofunction model of schizophrenia."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Synaptic zinc: the synaptic zinc that modulates the glutamate (already mapped) and NMDA signalling is disturbed in schizophrenia, part of the trace-metal dimension of the disorder."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 neuroinflammation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in schizophrenia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 neuroinflammation: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension implicated in schizophrenia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 immune arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with schizophrenia."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive neuroinflammation: the cytotoxic T cells (perforin already mapped) of the CNS-border compartments are part of the adaptive-immune contribution to the neuroinflammation implicated in schizophrenia."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells of the meningeal/CNS-border immune compartments present antigen (MHC already mapped) to the T cells (already mapped) of the neuroinflammation implicated in schizophrenia."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation associated with schizophrenia."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the type-2 (IgE already mapped) dimension implicated in schizophrenia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) synaptic pruning implicated in schizophrenia."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Peripheral innate arm: the NK cells (perforin pathway) are part of the peripheral innate-immune dysregulation associated with schizophrenia."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway (C1q–C4–C3, with C3, C5 and C5aR1 already mapped) that drives the microglial (already mapped) synaptic pruning implicated in schizophrenia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-mediated synaptic pruning of schizophrenia."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells: the regulatory T cells, reduced in the peripheral immune dysregulation of schizophrenia, normally restrain the neuroinflammation implicated in the disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuroimmune alarmin: TSLP levels reflect the type-2 and mast-cell activation implicated in the maternal immune-activation hypothesis of schizophrenia, and the comorbid allergic/atopic conditions that frequently accompany the disorder."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "BBB neuroinflammation: bradykinin, elevated in the CSF and plasma of schizophrenia patients, increases blood-brain barrier permeability and contributes to the microglial (already mapped) neuroinflammation and complement (already mapped) activation."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective EPO: erythropoietin exerts neuroprotective effects on schizophrenia-relevant circuits via EPOR on neurons and glia; clinical trials of EPO have targeted the cognitive deficits and white-matter pathology of the disorder."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM neuroinflammatory matrix: periostin is elevated in schizophrenia brain tissue; it modulates integrin signalling on astrocytes and microglia, contributing to the synaptic remodelling and neuroinflammatory milieu of the disorder."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen dysregulation: testosterone levels are reduced in male schizophrenia patients and inversely correlate with positive-symptom severity; androgen receptor signalling on dopaminergic neurons modulates D2 receptor density and antipsychotic sensitivity."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Brain iron transport: transferrin-mediated iron delivery is impaired in schizophrenia; prenatal iron deficiency (a risk factor) disrupts monoaminergic maturation, and CSF transferrin levels correlate with cognitive impairment in affected patients."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Sz vasopressin: vasopressin via V1aR and V1bR in limbic circuits (already mapped) and hypothalamus modulates the oxytocin (already mapped)-social-cognition axis and antipsychotic-responsive positive symptoms, with CSF vasopressin inversely correlating with schizophrenia severity."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Sz selenium: selenium deficiency amplifies the oxidative stress (xanthine-oxidase and nfe2l2 already mapped) in schizophrenia brain tissue; selenoproteins (GPx1, GPx4) protect dopaminergic (already mapped) and glutamatergic (already mapped) neurons from lipid peroxidation."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Sz iodine: iodine regulates neurodevelopment disrupted in schizophrenia through thyroid-hormone-mediated cortical myelination; maternal iodine deficiency impairs monoaminergic maturation (dopamine already mapped) and increases schizophrenia risk via prenatal hypothyroidism."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sz sodium: sodium-channel-mediated interneuron firing governs dopaminergic (already mapped) and glutamatergic (already mapped) neurotransmission; sodium dysregulation amplifies cortical hypofrontality and the positive-symptom burden of schizophrenia."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Sz phosphorus: phosphorus as ATP fuels PI3K/AKT (already mapped) signalling and synaptic vesicle cycling underlying dopamine (already mapped) and glutamate (already mapped) neurotransmission; membrane phospholipid abnormalities are a replicated schizophrenia biomarker."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Sz sulfur: hyperhomocysteinaemia — a schizophrenia risk biomarker — impairs glutamatergic (already mapped) NMDAR function and dopamine (already mapped) metabolism, amplifying the oxidative stress (xanthine-oxidase already mapped) of schizophrenia."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Sz chloride: KCC2/NKCC1 chloride dysregulation shifts GABA (already mapped) from inhibitory to excitatory; chloride imbalance amplifies glutamate (already mapped) excitotoxicity and IL-6 (already mapped) neuroinflammation in neurons (already mapped) of schizophrenia."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Sz nitrogen: nitric oxide modulates dopamine (already mapped) and glutamate (already mapped) neurotransmission; NOS dysfunction in neurons (already mapped) and microglia (already mapped) amplifies IL-6 (already mapped) and mTOR (already mapped) cascade of schizophrenia."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Sz carbon: glycine and serine carbon scaffolds act as NMDA co-agonists modulating glutamate (already mapped); one-carbon metabolism deficits amplify BDNF (already mapped) signalling and IL-6 (already mapped) neuroinflammation in neurons (already mapped) of schizophrenia."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Sz oxygen: ROS from neurons (already mapped) and macrophages (already mapped) drives neuroinflammatory oxidative stress; oxygen-induced ROS amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade and worsens glutamate (already mapped) receptor damage in schizophrenia."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Sz hydrogen: hydrogen bonds stabilise neurotransmitter-receptor complexes in neurons (already mapped); oxidative hydrogen peroxide from macrophages (already mapped) drives NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of schizophrenia."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Sz NF-κB: NF-κB drives IL-6 (already mapped) and IL-1β (already mapped) transcription in macrophages (already mapped); sustained NF-κB activation amplifies dopamine (already mapped) dysregulation and suppresses BDNF (already mapped) neurotrophic signalling in schizophrenia."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Sz PD-1: PD-1 checkpoint on macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates neuroinflammatory immune surveillance; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of schizophrenia."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Sz Wnt/β-catenin: Wnt/β-catenin signalling in neurons (already mapped) and macrophages (already mapped) supports synaptic plasticity; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) cascade of schizophrenia."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Sz RANKL: RANKL signalling in macrophages (already mapped) and neurons (already mapped) modulates neuroinflammatory bone-immune crosstalk; RANKL dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) cascade of schizophrenia."
---

# Schizophrenia

## Overview

**Schizophrenia** is a severe, chronic psychiatric disorder defined by episodic psychosis (hallucinations, delusions) with persistent functional impairment arising from positive, negative, and cognitive symptom domains. It affects approximately **1% of the global population** across all cultures and socioeconomic strata — roughly 24 million people worldwide — and ranks among the most disabling medical conditions, typically emerging in late adolescence to early adulthood (peak onset: males 18–25 years; females 25–35 years, with a second peak at menopause). The illness carries enormous personal, familial, and economic burden: 40–50% of people with schizophrenia attempt suicide, and lifetime mortality is 2–3× the general population.

**DSM-5 diagnostic criteria** require ≥2 of the following symptoms (≥1 month, ≥1 must be from 1–3):
1. Delusions
2. Hallucinations
3. Disorganized speech
4. Grossly disorganized or catatonic behavior
5. Negative symptoms

Plus ≥6 months of social/occupational dysfunction not attributable to substances or medical conditions.

**Three symptom domains** that drive different pathophysiological and treatment implications:

| Domain | Examples | Neural substrate | Treatment response |
|:---|:---|:---|:---|
| **Positive** | Auditory hallucinations, persecutory delusions, thought disorder | Mesolimbic dopamine D2 hyperactivity | Good (antipsychotics) |
| **Negative** | Avolition, alogia, anhedonia, asociality, flat affect (5 A's) | Mesocortical D1 hypofunction; PFC GABAergic deficit | Poor (antipsychotics largely ineffective) |
| **Cognitive** | Working memory, processing speed, verbal learning deficits | DLPFC PV interneuron deficit; NMDA hypofunction | Untreated by current antipsychotics |

## Structure

### Neuroanatomical abnormalities

Structural neuroimaging (MRI) and postmortem studies consistently identify:

**Gray matter reductions:**
- **Dorsolateral prefrontal cortex (DLPFC):** Reduced volume, impaired activation during working memory tasks (hypofrontality on PET/fMRI); correlates with cognitive deficits and negative symptoms
- **Superior temporal gyrus (STG):** Planum temporale reduction (auditory association cortex); correlates with severity of auditory hallucinations
- **Hippocampus and parahippocampal gyrus:** Reduced volume; impaired pattern separation and memory encoding
- **Anterior cingulate cortex:** Reduced volume; correlates with avolition and poor error monitoring

**Structural changes:**
- **Enlarged lateral ventricles:** 5–10% greater volume than controls on average; present in first-episode, drug-naive patients
- **Reduced white matter integrity:** Uncinate fasciculus (PFC–amygdala), arcuate fasciculus (language), cingulum (PFC–hippocampus) on DTI

### Cellular pathology

**Parvalbumin (PV) interneuron deficit:**
- Postmortem DLPFC and hippocampus: reduced PV+ cell density, reduced GAD67 (GABA synthetic enzyme) expression
- PV+ chandelier and basket cells provide perisomatic inhibition to pyramidal neurons and generate high-frequency gamma oscillations (30–80 Hz)
- Loss of PV interneurons → impaired gamma synchrony → working memory deficit (measurable by EEG/MEG in schizophrenia patients and unaffected relatives)

**Synaptic pruning hypothesis:**
- Schizophrenia onset coincides with adolescent synaptic pruning (complement-mediated elimination of weaker synapses via C4A/C4B)
- GWAS identified the **C4A gene** (complement component 4A) as a major schizophrenia risk locus (Sekar et al., 2016); elevated C4A → excess synapse elimination in PFC during pruning → loss of PV interneurons and thalamo-cortical connections

## Function

### The dopamine hypothesis (Version III)

The **mesolimbic/mesocortical dopamine hypothesis** remains the best-supported pathophysiological framework [^howes-2009-dopamine-hypothesis]:

**Evidence from neuroimaging:**
- **[¹⁸F]-DOPA PET:** Measures presynaptic dopamine synthesis capacity; elevated by ~12% in striatum of schizophrenia patients vs. controls; high at first episode before antipsychotic treatment
- **[¹¹C]-raclopride displacement:** Amphetamine displaces more D2 receptor binding in schizophrenia → elevated dopamine release capacity in striatum
- **[¹¹C]-PHNO PET:** Elevated D2/D3 receptor density in caudate/putamen (extrasynaptic D2) correlates with positive symptom severity

**Mesolimbic pathway (VTA → nucleus accumbens, striatum):**
- Tonic dopamine release normally signals reward and salience
- D2 hyperactivation → aberrant salience attribution → neutral stimuli acquire exaggerated personal significance → delusions and hallucinations (Kapur's salience dysregulation theory)

**Mesocortical pathway (VTA → PFC):**
- D1 receptor activation at PFC pyramidal cells supports working memory maintenance (inverted-U: optimal D1 tone required)
- PFC dopamine hypofunction in schizophrenia → working memory deficit, negative symptoms
- Creates a paradox: striatal D2 excess while cortical D1 is deficient

**Antipsychotic mechanism:**
All approved antipsychotics occupy D2 receptors. Clinical response requires **60–80% D2 occupancy** in striatum (PET studies); >80% occupancy → extrapyramidal side effects (EPS). Fast D2 dissociation (aripiprazole, clozapine) reduces EPS risk.

### Glutamate/NMDA receptor hypofunction hypothesis

The glutamate hypothesis arose from the observation that **PCP (phencyclidine)** and **ketamine** (NMDA receptor antagonists) reproduce all three symptom domains (positive, negative, cognitive) in healthy volunteers — an effect not achievable with amphetamine (which only induces positive symptoms) [^moghaddam-2012-glutamate]:

**Circuit mechanism:**
1. PV+ interneurons in PFC express high levels of NMDA receptors (GluN2B-containing)
2. NMDA hypofunction → PV interneuron silencing → reduced GABA release → disinhibition of pyramidal glutamate neurons
3. Excess glutamate in PFC → downstream excess subcortical dopamine release (via nucleus accumbens)
4. Glutamate–dopamine interaction: NMDA hypofunction → both cortical glutamate excess (causing cognitive/negative symptoms) and subcortical dopamine excess (causing positive symptoms)

**Biomarker evidence:**
- CSF glutamate elevated in antipsychotic-naive schizophrenia
- Magnetic resonance spectroscopy (MRS): elevated glutamate in basal ganglia; reduced glutamate in PFC in chronic schizophrenia
- Glutamate hypothesis explains why ketamine models the complete syndrome while amphetamine models only positive symptoms

### Genetic architecture

Schizophrenia has high heritability (~79%) but complex polygenic architecture with no single causal gene:

**Copy number variants (CNVs — large rare variants):**
- **22q11.2 deletion (DiGeorge/velocardiofacial syndrome):** ~1/2000 births; 25–30% develop schizophrenia by adulthood; the highest schizophrenia risk factor known
- **1q21.1, 15q11.2, 15q13.3, 16p11.2:** Associated CNVs with 2–10× increased risk

**GWAS common variants (>260 loci):**
- **C4A/C4B** (complement; synaptic pruning) — most biologically interpretable GWAS signal
- **CACNA1C** (L-type Ca²⁺ channel; also bipolar disorder)
- **COMT** (catechol-O-methyltransferase; dopamine catabolism in PFC)
- **DISC1** (disrupted in schizophrenia 1; rare family with translocation)
- **NRG1** (neuregulin 1; ErbB4 signaling in PV interneurons)
- **DTNBP1** (dysbindin; presynaptic vesicle protein)

**De novo coding mutations** (whole-exome sequencing): SETD1A (histone methyltransferase), SYNGAP1 (synaptic RasGAP), NRXN1 (neurexin; synaptic scaffolding) — rare but high penetrance.

Notably, schizophrenia shares genetic loci with bipolar disorder, ASD, ADHD, major depression, and epilepsy (the **psychiatric cross-disorder overlap** — these conditions share common polygenic risk).

## Pathology

### Clinical course

**Phases:**
1. **Prodrome** (months to years): Social withdrawal, declining function, attenuated psychosis; anxiety, depression; high-risk state for conversion to full psychosis (~30–40% convert in 2 years)
2. **First episode psychosis (FEP):** Acute psychotic break; best prognosis if treated early (DUP — duration of untreated psychosis is the strongest modifiable prognostic factor)
3. **Chronic relapsing-remitting course** (most patients): Positive symptoms respond to antipsychotics; negative/cognitive symptoms persist
4. **Treatment-resistant schizophrenia (TRS):** ~30% do not respond to ≥2 adequate antipsychotic trials; defined by failure to achieve ≥20% symptom reduction

### Comorbidities

- **Substance use disorders:** 50% lifetime; cannabis (particularly high-THC) precipitates psychosis and worsens course (CB1 receptor agonism amplifies dopamine release in striatum)
- **Metabolic syndrome:** 2–3× elevated risk (antipsychotic side effects: weight gain, dyslipidemia, T2D)
- **Cardiovascular disease:** Leading cause of premature death (smoking prevalence 60-80%; antipsychotic metabolic effects)
- **Suicide:** 5–10% completed suicide lifetime (40–50% attempt); clozapine is the only antipsychotic proven to reduce suicidality

### Antipsychotic treatment [^leucht-2013-antipsychotics-meta]

**First-generation (typical) antipsychotics — D2 blockers:**
- Haloperidol, chlorpromazine, fluphenazine
- Highly effective for positive symptoms; ~70% response
- High EPS risk: acute dystonia, akathisia, parkinsonism, tardive dyskinesia (TD; irreversible in ~25% of chronic users)
- Depot formulations (haloperidol decanoate) for adherence

**Second-generation (atypical) antipsychotics — D2 + 5-HT2A antagonists:**

| Drug | D2 Ki | 5-HT2A Ki | Key features |
|:---|:---|:---|:---|
| **Clozapine** | Low affinity (fast off-rate) | Very high | Gold standard for TRS; reduces suicidality; risk: agranulocytosis (1–2%, mandatory ANC monitoring), weight gain, seizures, myocarditis |
| **Olanzapine** | Moderate | High | High efficacy; major metabolic risk (weight gain 4–8 kg/year) |
| **Quetiapine** | Low | High | Sedating; used for comorbid anxiety/sleep; antimaniac effect |
| **Risperidone** | High | High | Effective; EPS at higher doses; hyperprolactinemia |
| **Aripiprazole** | D2 partial agonist | 5-HT2A antagonist | Weight-neutral; activating; reduced EPS |
| **Ziprasidone** | Moderate | High | Low metabolic risk; QTc prolongation risk |

**Novel mechanism — muscarinic antipsychotic (2024):**
- **Xanomeline-trospium (KarXT/Cobenfy, Bristol-Myers Squibb):** FDA-approved September 2024 — first antipsychotic without D2 blockade
- Mechanism: Xanomeline is a muscarinic M1/M4 receptor agonist; M1 activation in PFC improves cognition; M4 activation in striatum reduces dopamine release; trospium (peripheral muscarinic antagonist) limits GI side effects
- EMERGENT-4 trial: significantly reduced PANSS total score vs. placebo; no EPS, no weight gain; represents a new era in schizophrenia treatment

### Early intervention

**First-episode psychosis (FEP) programs:**
- Coordinated specialty care (CSC) combining low-dose antipsychotic, family education, individual therapy, supported education/employment
- RAISE study (2015): CSC significantly superior to standard care for symptoms, quality of life, employment
- Duration of untreated psychosis (DUP) reduction: every week of delay in treatment worsens long-term prognosis

## Connections

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — Mesolimbic D2 hyperactivity drives positive symptoms (hallucinations, delusions); mesocortical D1 hypofunction in PFC drives negative and cognitive symptoms; all antipsychotics achieve therapeutic effect via D2 blockade (60-80% receptor occupancy threshold).

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — NMDA receptor hypofunction in PFC parvalbumin interneurons underlies cognitive and negative symptoms; ketamine (NMDA antagonist) reproduces the full schizophrenia phenotype; glycine-site NMDA co-agonists and AMPA potentiators are experimental treatments.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — Parvalbumin interneuron hypofunction in PFC — reduced GAD67, impaired GABA synthesis — causes deficient gamma oscillations that underlie working memory deficits; GABAergic interneuron loss may be primary, upstream of dopamine and glutamate dysregulation.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — 5-HT2A blockade in PFC by atypical antipsychotics (clozapine, olanzapine, risperidone) enhances dopaminergic output; 5-HT2A agonism by hallucinogens (LSD, psilocybin) models positive symptoms; serotonin-dopamine interaction shapes atypical antipsychotic efficacy.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — Schizophrenia involves enlarged ventricles, reduced gray matter in DLPFC, superior temporal gyrus, and hippocampus; functional dysconnectivity between PFC and temporal/limbic regions on fMRI; PV interneuron density is reduced in DLPFC and hippocampus post-mortem.

- `connects-to` → **[Prolactin](../../../03-molecular/prolactin/README.md)** — antipsychotic D2 blockade at the pituitary tuberoinfundibular pathway removes TIDA inhibition → hyperprolactinemia; risperidone causes greatest elevation (45-100 ng/mL); galactorrhea, sexual dysfunction, and osteoporosis are key drivers of medication non-adherence in schizophrenia.
- `connects-to` → **[Histamine](../../../03-molecular/histamine/README.md)** — H1R inverse agonists (clozapine, olanzapine, quetiapine) drive antipsychotic weight gain and sedation; H3R heteroreceptors on DA/5-HT terminals modulate monoamine release; histaminergic TMN arousal neurons are implicated in arousal deficit and cognitive symptoms in schizophrenia.

- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Schizophrenia's cellular lesion centers on the parvalbumin fast-spiking GABAergic interneuron of the prefrontal cortex and hippocampus: reduced GAD67 and impaired firing degrade the gamma oscillations behind working memory — upstream of the dopamine and glutamate abnormalities.

- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Schizophrenia and bipolar disorder overlap genetically and clinically: they share risk variants (CACNA1C) and the schizoaffective category, and both feature psychosis — but schizophrenia is dominated by chronic negative/cognitive deficits, bipolar by episodic mood elevation.

- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus is a key schizophrenia node: reduced in volume with fewer parvalbumin interneurons, and an overactive anterior hippocampus may drive aberrant dopamine release via the subiculum-VTA pathway — linking memory deficits to the dopamine dysregulation behind psychosis.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia are central to a leading schizophrenia hypothesis: complement-C4-tagged synapses are over-pruned by microglia in adolescence, and the strongest common genetic risk maps to the C4 locus—excess synaptic elimination may underlie the disorder's grey-matter loss.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — Schizophrenia and autism share neurodevelopmental roots and genetics: overlapping copy-number variants (22q11, 16p11) and synaptic genes underlie both, sitting on a continuum of early brain miswiring—though autism presents in childhood and schizophrenia later.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes contribute to the glutamate dysfunction of schizophrenia: by clearing synaptic glutamate and supplying the NMDA co-agonist D-serine, astrocyte dysfunction can impair NMDA-receptor signaling—the basis of the glutamatergic hypothesis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Schizophrenia and depression overlap and can be hard to separate: depression often complicates schizophrenia and raises suicide risk, and the two share genetic and neurochemical substrates—so mood symptoms are assessed throughout the illness.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Schizophrenia and epilepsy are bidirectionally linked: each roughly doubles the risk of the other, temporal-lobe epilepsy can produce schizophrenia-like psychosis, and they share glutamate and GABA disturbances—genuinely overlapping disorders.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Schizophrenia involves oligodendrocyte and white-matter abnormalities, not just neurons: fewer oligodendrocytes and disrupted myelination impair long-range connectivity, supporting a 'dysconnectivity' model where faulty wiring underlies the illness.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF deficits link schizophrenia to disrupted neurodevelopment: reduced brain-derived neurotrophic factor impairs synaptic plasticity and cortical circuit maturation, fitting the neurodevelopmental model in which schizophrenia's roots predate its psychotic onset by years.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Cannabis use can precipitate and worsen schizophrenia: heavy adolescent use raises the risk of developing psychosis and triggers relapse in patients, since THC perturbs the dopamine and endocannabinoid systems—so cannabis avoidance is part of schizophrenia management.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Acetylcholine is an emerging schizophrenia target beyond dopamine: muscarinic agonists (xanomeline) improve psychosis without blocking dopamine, so the cholinergic system shapes symptoms—a shift from the dopamine-only model of antipsychotic action.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Schizophrenia is increasingly seen as a synaptic disorder: excessive synaptic pruning in adolescence—linked to complement (C4) and microglia—thins prefrontal connectivity, so it is conceived as a disease of disrupted synapses, not just dopamine.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune system is implicated in schizophrenia: a complement-C4 risk variant drives excessive microglial synaptic pruning, and maternal infection raises offspring risk, so neuroinflammation and immune-mediated synapse loss feature in current models of the disease.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Schizophrenia shortens life mainly through cardiovascular disease: antipsychotic-related weight gain and metabolic syndrome, plus smoking and poor access to care, cause excess heart disease—so patients die 15-20 years early, largely of cardiovascular causes.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Schizophrenia may involve excessive synaptic pruning via complement: the strongest common-variant risk lies in complement C4, which tags synapses through C3 for microglial removal, so over-pruning in adolescence could thin the cortical connections seen in the disease.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Prenatal and placental factors raise schizophrenia risk: maternal infection, malnutrition and obstetric complications acting through the placenta interact with genetic risk, supporting a neurodevelopmental origin set in motion before birth.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut-brain axis is implicated in schizophrenia: altered gut microbiota and intestinal inflammation can influence neurotransmitters and immune signaling reaching the brain, an emerging factor beyond the classic dopamine and glutamate models.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Schizophrenia's strongest genetic hits include a calcium channel: CACNA1C and other voltage-gated calcium channel genes top the risk lists, so disturbed calcium signaling in neurons—shared with bipolar disorder—is a core piece of its biology.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Maternal IL-6 links infection to schizophrenia: prenatal immune activation, signaled through IL-6, perturbs fetal brain development and raises later risk—evidence that inflammation in pregnancy is one road into the disorder.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Stress and cortisol shape schizophrenia's onset: an overactive HPA axis and high cortisol mark the prodrome and can precipitate first psychosis in vulnerable people, the hormonal arm of the stress-diathesis model.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium touches schizophrenia's glutamate problem: it gates the NMDA receptor, central to the glutamate-hypofunction theory of the illness, so disturbed magnesium handling can shift the excitation-inhibition balance behind psychosis.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Stress and the adrenal glands shape schizophrenia: an overactive HPA axis drives the adrenals to pour out cortisol, and this stress-hormone surge marks the prodrome and can tip vulnerable people into first psychosis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — A gut-brain axis is emerging in schizophrenia: an altered intestinal microbiome and gut inflammation may influence neurotransmitters and immune signals reaching the brain, linking the large intestine to psychotic illness.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Schizophrenia disturbs synaptic zinc: this trace metal tunes the NMDA glutamate receptors at the core of the disease's signaling, so zinc dysregulation is studied in its synaptic and cognitive deficits.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Schizophrenia's deadliest complication is the heart: antipsychotics prolong the QT and drive metabolic syndrome, and patients die of cardiovascular disease years early—the leading cause of their shortened lifespan.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Antipsychotics fatten the adipocytes: the drugs that quiet psychosis also drive weight gain and fat accumulation, fueling the metabolic syndrome and diabetes that burden treated schizophrenia.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons reveal the schizophrenic brain's structure and chemistry: MRI shows enlarged ventricles and thinned gray matter, while PET tracers map the striatal dopamine excess that antipsychotics aim to dampen.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye carries a schizophrenia signature: smooth-pursuit eye movements are jerky and broken in patients and their unaffected relatives, a heritable endophenotype that points to the brain-wiring deficits behind the illness.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D in the womb shapes later risk: low maternal vitamin D during fetal brain development is an established schizophrenia risk factor, helping explain the disease's links to winter births and higher latitudes.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The most effective drug demands blood counts: clozapine, reserved for treatment-resistant schizophrenia, can wipe out neutrophils into a life-threatening agranulocytosis, so patients undergo mandatory regular neutrophil monitoring to use it safely.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Antipsychotics tax the metabolic organs: second-generation agents like olanzapine and clozapine drive weight gain and insulin resistance, straining the pancreas toward the diabetes and metabolic syndrome that shorten lives in schizophrenia.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Many antipsychotics tug at the heart's potassium gate: by blocking the hERG potassium channel they prolong the QT interval, a delayed repolarization that in susceptible patients can tip into the dangerous arrhythmia torsades de pointes.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — A treatable mimic hides among the cases: anti-NMDA-receptor encephalitis produces psychosis indistinguishable from schizophrenia, its autoantibodies against the NMDA receptor a reason to test, since immunotherapy can reverse what looks like a primary psychotic break.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — A brain parasite shadows the risk: chronic Toxoplasma gondii infection, which encysts in the brain and nudges dopamine, is consistently associated with a modestly higher rate of schizophrenia, one strand of the disease's infection-and-immune hypothesis.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The drugs reach into reproduction: by blocking dopamine, many antipsychotics lift prolactin into galactorrhea, amenorrhea, and sexual dysfunction, side effects that erode adherence and reproductive health in schizophrenia.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Schizophrenia and insulin resistance are entangled: antipsychotics blunt insulin sensitivity and drive weight gain, and even drug-naive patients show glucose dysregulation, so the metabolic syndrome that shortens lives in schizophrenia is partly built into the illness.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — One antipsychotic can inflame the heart muscle: clozapine, the most effective drug for resistant schizophrenia, can cause myocarditis and cardiomyopathy by injuring cardiomyocytes, so cardiac monitoring is mandatory when it is started.
- `connects-to` → **[Obesity](../obesity/README.md)** — Treatment commonly brings weight gain: many antipsychotics, especially olanzapine and clozapine, drive substantial obesity through appetite and metabolic effects, a major reason for the metabolic syndrome and shortened life expectancy in schizophrenia.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — The sugar disease often follows: schizophrenia carries a raised risk of type 2 diabetes both from antipsychotics that directly impair insulin signaling — sometimes within weeks, beyond their weight effect — and from an intrinsic predisposition shared with the illness.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — An immune signature runs alongside: shifts in helper T-cell subsets and raised inflammatory cytokines appear in schizophrenia, supporting a neuroinflammatory contribution that complements the microglial pruning and complement findings.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — The body clock is unsettled: melatonin rhythms are blunted and sleep-wake cycles disrupted in schizophrenia, both as a feature of the illness and a target, with melatonin used to ease the insomnia and metabolic effects of treatment.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Neuroinflammation has an inflammasome arm: NLRP3-driven IL-1β release is implicated in the microglial activation and developmental disruption proposed in schizophrenia, complementing the complement-mediated synaptic pruning findings.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Substance use runs high: alcohol use disorder is markedly more common in schizophrenia, used to self-medicate symptoms yet worsening psychosis, adherence, and the metabolic and cardiovascular toll of the illness.
- `connects-to` → **[Stroke](../stroke/README.md)** — The mortality gap reaches the brain: metabolic syndrome, antipsychotic effects, and smoking give schizophrenia a raised stroke risk, part of the cardiovascular disease that shortens life expectancy by 15-20 years.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The antipsychotics themselves clot the veins: most antipsychotic drugs independently raise venous thromboembolism risk, compounded by sedation, immobility and obesity, so DVT and pulmonary embolism are a recognized treatment hazard.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Blocking dopamine mimics the disease: D2-antagonist antipsychotics induce a drug-induced parkinsonism — bradykinesia, rigidity and tremor — that can be hard to distinguish from idiopathic Parkinson's, the pharmacologic mirror of its dopamine deficit.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Clozapine can strip the neutrophils: the agranulocytosis caused by clozapine, the drug reserved for resistant schizophrenia, removes the front-line defense against bacteria and can precipitate life-threatening sepsis, mandating blood-count monitoring.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its antipsychotics and metabolic burden weaken the heart: clozapine can cause myocarditis and cardiomyopathy, and the diabetes, obesity and dyslipidemia driven by antipsychotics accelerate the cardiac disease that shortens schizophrenia lifespans.
- `connects-to` → **[COPD](../copd/README.md)** — Very high smoking rates scar the lungs: people with schizophrenia smoke heavily, and the resulting chronic obstructive pulmonary disease is a major contributor to their markedly reduced life expectancy.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Prolactin-raising drugs thin the bones: many antipsychotics block dopamine to raise prolactin, suppressing sex hormones, and the resulting hypogonadism — with inactivity and smoking — accelerates bone loss toward osteoporosis.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Obsessions commonly accompany psychosis: a substantial minority with schizophrenia have comorbid obsessive-compulsive symptoms (schizo-obsessive presentations), and some antipsychotics can themselves provoke them.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Clozapine can paralyse the gut: the most effective antipsychotic causes severe gastrointestinal hypomotility, with constipation that can progress to ileus, obstruction and life-threatening bowel complications.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety pervades the illness: prominent anxiety and worry accompany the prodrome, active psychosis and insight into schizophrenia, frequently meeting criteria for a comorbid generalized anxiety disorder.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is fundamentally a brain disorder: schizophrenia involves dopaminergic and glutamatergic dysregulation, neurodevelopmental grey-matter changes and disrupted connectivity, the neurobiology underlying psychosis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its drugs flood the body with prolactin: dopamine-blocking antipsychotics raise prolactin, causing galactorrhoea, amenorrhoea and hypogonadism, and they drive the metabolic syndrome of weight gain and diabetes.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Very heavy smoking scars the lungs: people with schizophrenia smoke at extremely high rates, giving high COPD and pneumonia burdens, and clozapine can rarely cause respiratory depression.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Water and muscle breakdown threaten the kidney: psychogenic polydipsia causes water intoxication with hyponatraemia, and neuroleptic malignant syndrome with rhabdomyolysis can cause acute kidney injury.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Antipsychotics act on muscle and movement: they cause acute dystonia, drug-induced parkinsonism and tardive dyskinesia, and neuroleptic malignant syndrome brings life-threatening muscle rigidity.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Drugs and self-neglect mark the skin: chlorpromazine causes photosensitivity and slate-grey pigmentation, and the self-neglect of severe illness contributes to skin and dental problems.
- `connects-to` → **[Influenza A](../../../02-pathogen/01-viruses/influenza-a/README.md)** — Maternal infection raises the risk: prenatal exposure to influenza and other infections is linked to higher schizophrenia risk through maternal immune activation affecting fetal brain development.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet is studied in early psychosis: omega-3 supplementation has been trialled to delay transition in those at high clinical risk of psychosis, with mixed results.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — Antidepressants augment treatment: SSRIs like fluoxetine are added to antipsychotics for the depressive and negative symptoms that often accompany schizophrenia.
- `connects-to` → **[Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — It curbs antipsychotic metabolic harm: second-generation antipsychotics cause weight gain, insulin resistance and dyslipidaemia, and metformin is added to blunt the drug-induced metabolic syndrome that widens the cardiovascular mortality gap in schizophrenia.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Trauma feeds psychosis risk: childhood adversity and trauma raise the risk of later schizophrenia, and PTSD itself can present with psychotic features, blurring the boundary between trauma-related and primary psychotic illness.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — A psychotic-symptom differential: borderline personality disorder produces transient stress-related paranoia and dissociation that can mimic schizophrenia, distinguished by the persistence, negative symptoms and course of true psychosis.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep falls apart in psychosis: schizophrenia disrupts sleep architecture—reduced slow-wave sleep and sleep spindles—and insomnia often heralds relapse, with the two sharing dopaminergic and circadian dysregulation.
- `connects-to` → **[Huntington's Disease](../huntingtons-disease/README.md)** — Psychosis from the striatum: Huntington's disease frequently produces psychotic symptoms, and its striatal dopamine dysregulation echoes the dopamine hypothesis of schizophrenia—one a degenerative, one a developmental disorder of the same circuits.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Late-life psychosis and shared mechanisms: psychotic features arise in Alzheimer's dementia, and schizophrenia and Alzheimer's share synaptic loss, microglial and complement-driven pruning and neuroinflammation despite their different ages of onset.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Antipsychotics and sudden death: many antipsychotics prolong the QT interval, and schizophrenia carries an elevated risk of sudden cardiac death through arrhythmia and the conduction system.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Clozapine myocarditis: clozapine—the most effective drug for treatment-resistant schizophrenia—can cause an acute myocarditis and cardiomyopathy of the myocardium, monitored closely in the first weeks of treatment.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Hyperprolactinaemia and breast cancer: dopamine-blocking antipsychotics raise prolactin, and sustained hyperprolactinaemia is associated with a modest increase in breast cancer risk in long-treated patients.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Infection and psychosis: maternal infection in pregnancy raises schizophrenia risk (as with influenza and toxoplasma), and severe COVID-19 with its neuroinflammation can precipitate new psychosis, while the pandemic worsened outcomes for patients.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — A psychosis mimic: the vivid hypnagogic hallucinations and REM intrusions of narcolepsy can resemble psychosis, and the two intersect through dopaminergic and thalamic circuits and the drugs that modulate them.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Smoking's toll: very high smoking rates in schizophrenia—partly self-medicating cognitive and sensory-gating deficits with nicotine—drive excess lung cancer and COPD, contributing to the large mortality gap.
- `connects-to` → **[Endocannabinoid](../../03-molecular/endocannabinoid/README.md)** — Cannabinoid risk axis: endocannabinoid signalling is dysregulated in schizophrenia, and cannabis use through CB1-receptor agonism is a robust environmental risk factor for psychosis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Social cognition: oxytocin modulates the social cognition and trust deficits central to schizophrenia, and has been explored as an adjunct to antipsychotics.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Neuroinflammation: raised TNF-α and other inflammatory cytokines, with microglial activation, are increasingly implicated in the neurodevelopmental pathology of schizophrenia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Maternal immune activation: IL-1β is a key cytokine of the maternal immune activation linked to schizophrenia risk, and features in the neuroinflammation of the disorder.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Immune dysregulation: altered IFN-γ signalling is part of the immune dysregulation increasingly tied to schizophrenia, linking infection and inflammation to its neurodevelopment.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Noradrenergic arousal: noradrenergic dysregulation contributes to the arousal, attention and stress-response abnormalities seen in schizophrenia alongside the dopamine hypothesis.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — The schizophrenia risk gene NOS1AP regulates neuronal nitric-oxide synthase, tying NO signaling at the NMDA-receptor synapse to the glutamatergic dysfunction implicated in the disorder—a molecular bridge between a genetic locus and the NMDA-hypofunction model.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — Dopamine D2 and DISC1 signaling converge on GSK-3β, a kinase governing neurodevelopment and synaptic plasticity whose dysregulation is implicated in schizophrenia and which is inhibited by lithium and other mood stabilizers.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Prenatal type-I-interferon responses to maternal infection raise schizophrenia risk, a key strand of the neurodevelopmental immune hypothesis linking gestational inflammation to psychosis emerging decades later.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — The MHC region on chromosome 6 holds schizophrenia's largest genetic signal, driven largely by complement C4 alleles that increase synaptic pruning—tying the immune-gene locus to the loss of cortical synapses seen in the disease.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — The adenosine hypothesis holds that deficient adenosine signaling disinhibits dopamine and glutamate transmission, and adenosine A2A receptors that heteromerize with dopamine D2 receptors are an emerging antipsychotic target.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — The calcineurin subunit gene PPP3CC is associated with schizophrenia, and calcineurin-knockout mice show schizophrenia-like deficits—implicating this NMDA-coupled phosphatase in the synaptic dysfunction of psychosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — AKT1 is a schizophrenia-susceptibility gene, and dopamine-D2-receptor signaling through the AKT-GSK3β pathway (GSK3β already mapped) is a core node at which antipsychotics and lithium act on the disorder.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling regulates the activity-dependent protein synthesis and dendritic-spine maturation that are disrupted in schizophrenia, tying its neurodevelopmental origins to synaptic dysfunction.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Antipsychotics cause weight gain and the metabolic syndrome already mapped here (obesity, type-2 diabetes, metformin), and GLP-1 receptor agonists are increasingly used to counter this iatrogenic metabolic burden.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — AKT1 (mapped) is a schizophrenia-risk gene, and the PI3K-AKT-GSK3β-mTOR axis (AKT, GSK-3β and mTOR already mapped) relays dopamine and neurotrophin signals implicated in the disorder.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Heightened CRH-driven HPA-axis activity (cortisol mapped) is associated with the onset and relapse of psychosis, linking stress to the dopaminergic dysregulation of schizophrenia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Neuregulin-ErbB and BDNF-TrkB signaling converge on MAPK-ERK, a pathway implicated in the synaptic and neurodevelopmental abnormalities of schizophrenia.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor (NTRK) supports the cortical neurodevelopment and synaptic plasticity whose disruption is central to schizophrenia.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4-driven microglial neuroinflammation, linked to maternal immune activation and prenatal infection, contributes to the neurodevelopmental origins of schizophrenia.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2-regulated antioxidant defense counters the oxidative stress increasingly implicated in the parvalbumin-interneuron dysfunction of schizophrenia.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 reflects the aberrant microglial synaptic pruning increasingly implicated in the neurodevelopmental pathogenesis of schizophrenia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine-driven JAK-STAT signaling (IL-6 mapped) transduces the maternal-immune-activation and chronic inflammation linked to schizophrenia risk.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN regulation of the PI3K-AKT-GSK-3β axis (AKT and GSK-3β mapped) shapes the neurodevelopmental signaling implicated in schizophrenia.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the neuroinflammatory tone implicated in the neurodevelopmental pathophysiology of schizophrenia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the maternal-immune-activation and innate neuroinflammation implicated in schizophrenia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling (type-I interferon already mapped) transduces the maternal-immune-activation interferon exposure epidemiologically linked to schizophrenia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates neuronal metabolism and oxidative-stress handling implicated in schizophrenia.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked mitochondrial and metabolic dysfunction contributes to the neurodevelopmental pathology of schizophrenia.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the innate immune activation and microglial priming associated with schizophrenia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic and neurodevelopmental dysregulation implicated in schizophrenia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling participates in the metabolic and neuroinflammatory disturbances of schizophrenia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the synaptic pruning and neuronal homeostasis implicated in schizophrenia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (FYN) kinase signaling participates in the NMDA-receptor and synaptic-plasticity mechanisms implicated in schizophrenia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the microglial activation and neuroinflammation implicated in schizophrenia.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement signaling, alongside complement-mediated synaptic pruning (complement-C3 already mapped), participates in the synaptic pathology of schizophrenia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neurodevelopmental interneuron migration and neuroimmune interactions implicated in schizophrenia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in schizophrenia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the maternal-immune-activation and neuroinflammatory processes implicated in schizophrenia.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen-protection hypothesis: estrogen modulates dopaminergic transmission, women show later onset and a second incidence peak at menopause, and estrogen adjuncts improve symptoms, a neuroendocrine dimension of schizophrenia beyond the neurotransmitter models.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Antipsychotic metabolic syndrome: second-generation antipsychotics disrupt leptin signalling and drive the weight gain, dyslipidaemia and diabetes that dominate the physical-health morbidity and shortened lifespan of schizophrenia.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: schizophrenia is associated with impaired antioxidant defence and raised oxidative markers, and xanthine-oxidase-derived reactive oxygen species and purine dysregulation contribute to the redox imbalance implicated in its neuropathology.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Brain renin-angiotensin: central angiotensin II modulates dopamine transmission, neuroinflammation and stress reactivity, and angiotensin-blocking drugs are being investigated as adjuncts, implicating the brain RAS beyond the classical neurotransmitters already mapped.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Neurosteroids: progesterone-derived allopregnanolone modulates GABA-A signalling (GABA already mapped), and fluctuations across the reproductive cycle influence psychosis, part of the neurosteroid and sex-hormone contribution to schizophrenia (estrogen already mapped).
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Developmental iron: iron is a cofactor for dopamine synthesis, and prenatal iron deficiency is an epidemiological risk factor for schizophrenia, linking early-life micronutrient status to the neurodevelopmental origins of the disorder.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammation: prostaglandins from the low-grade neuroinflammation (IL-6 and IL-1 already mapped) and maternal infection implicated in schizophrenia modulate the developing brain, and anti-inflammatory agents are studied as adjuncts.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Clozapine myocarditis: clozapine, the most effective antipsychotic for treatment-resistant schizophrenia, can cause myocarditis and cardiomyopathy, and troponin elevation is monitored to detect this serious adverse effect early.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Neurovascular development: VEGF supports the cerebral angiogenesis and neurotrophic signalling (BDNF already mapped) implicated in the neurodevelopmental abnormalities of schizophrenia, part of its altered brain-vascular biology.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Antipsychotic dyslipidaemia: the second-generation antipsychotics raise cholesterol and drive the metabolic syndrome (insulin and leptin already mapped), a major contributor to the cardiovascular mortality that shortens life in schizophrenia.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Neuroimmune balance: the anti-inflammatory IL-10 counters the microglial pro-inflammatory cytokines (TNF, IL-6 and IL-1 already mapped) implicated in schizophrenia, part of the neuroinflammatory dimension of the disorder.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and psychosis: copper is a cofactor in dopamine metabolism (dopamine already mapped), and disordered copper handling, as in Wilson's disease, can produce a psychosis that mimics schizophrenia, linking the trace metal to the disorder.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Microglial polarisation: IL-4 polarises the microglia (already mapped) toward an anti-inflammatory M2 phenotype (IL-10 already mapped), the balance against the neuroinflammation (TNF, IL-6 and IL-1 already mapped) implicated in schizophrenia.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), is part of the type-2 arm whose balance against the pro-inflammatory signals shapes the neuroinflammatory dimension of schizophrenia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic adipokine: resistin, with leptin (already mapped), is part of the adipokine milieu of the metabolic syndrome (insulin and cholesterol already mapped) worsened by the antipsychotics and the disease in schizophrenia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin and resistin (already mapped), completes the adipokine axis of the metabolic syndrome (insulin and cholesterol already mapped) worsened by the antipsychotics in schizophrenia.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — NMDA modulation: magnesium blocks the NMDA receptor (glutamate already mapped), and magnesium dysregulation is implicated in the NMDA-hypofunction model of schizophrenia.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Synaptic zinc: the synaptic zinc that modulates the glutamate (already mapped) and NMDA signalling is disturbed in schizophrenia, part of the trace-metal dimension of the disorder.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 neuroinflammation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in schizophrenia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 neuroinflammation: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension implicated in schizophrenia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 immune arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with schizophrenia.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive neuroinflammation: the cytotoxic T cells (perforin already mapped) of the CNS-border compartments are part of the adaptive-immune contribution to the neuroinflammation implicated in schizophrenia.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells of the meningeal/CNS-border immune compartments present antigen (MHC already mapped) to the T cells (already mapped) of the neuroinflammation implicated in schizophrenia.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation associated with schizophrenia.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the type-2 (IgE already mapped) dimension implicated in schizophrenia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) synaptic pruning implicated in schizophrenia.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Peripheral innate arm: the NK cells (perforin pathway) are part of the peripheral innate-immune dysregulation associated with schizophrenia.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway (C1q–C4–C3, with C3, C5 and C5aR1 already mapped) that drives the microglial (already mapped) synaptic pruning implicated in schizophrenia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-mediated synaptic pruning of schizophrenia.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells: the regulatory T cells, reduced in the peripheral immune dysregulation of schizophrenia, normally restrain the neuroinflammation implicated in the disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuroimmune alarmin: TSLP levels reflect the type-2 and mast-cell activation implicated in the maternal immune-activation hypothesis of schizophrenia, and the comorbid allergic/atopic conditions that frequently accompany the disorder.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — BBB neuroinflammation: bradykinin, elevated in the CSF and plasma of schizophrenia patients, increases blood-brain barrier permeability and contributes to the microglial (already mapped) neuroinflammation and complement (already mapped) activation.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective EPO: erythropoietin exerts neuroprotective effects on schizophrenia-relevant circuits via EPOR on neurons and glia; clinical trials of EPO have targeted the cognitive deficits and white-matter pathology of the disorder.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM neuroinflammatory matrix: periostin is elevated in schizophrenia brain tissue; it modulates integrin signalling on astrocytes and microglia, contributing to the synaptic remodelling and neuroinflammatory milieu of the disorder.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen dysregulation: testosterone levels are reduced in male schizophrenia patients and inversely correlate with positive-symptom severity; androgen receptor signalling on dopaminergic neurons modulates D2 receptor density and antipsychotic sensitivity.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Brain iron transport: transferrin-mediated iron delivery is impaired in schizophrenia; prenatal iron deficiency (a risk factor) disrupts monoaminergic maturation, and CSF transferrin levels correlate with cognitive impairment in affected patients.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Sz vasopressin: vasopressin via V1aR and V1bR in limbic circuits (already mapped) and hypothalamus modulates the oxytocin (already mapped)-social-cognition axis and antipsychotic-responsive positive symptoms, with CSF vasopressin inversely correlating with schizophrenia severity.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Sz selenium: selenium deficiency amplifies the oxidative stress (xanthine-oxidase and nfe2l2 already mapped) in schizophrenia brain tissue; selenoproteins (GPx1, GPx4) protect dopaminergic (already mapped) and glutamatergic (already mapped) neurons from lipid peroxidation.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Sz iodine: iodine regulates neurodevelopment disrupted in schizophrenia through thyroid-hormone-mediated cortical myelination; maternal iodine deficiency impairs monoaminergic maturation (dopamine already mapped) and increases schizophrenia risk via prenatal hypothyroidism.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sz sodium: sodium-channel-mediated interneuron firing governs dopaminergic (already mapped) and glutamatergic (already mapped) neurotransmission; sodium dysregulation amplifies cortical hypofrontality and the positive-symptom burden of schizophrenia.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Sz phosphorus: phosphorus as ATP fuels PI3K/AKT (already mapped) signalling and synaptic vesicle cycling underlying dopamine (already mapped) and glutamate (already mapped) neurotransmission; membrane phospholipid abnormalities are a replicated schizophrenia biomarker.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Sz sulfur: hyperhomocysteinaemia — a schizophrenia risk biomarker — impairs glutamatergic (already mapped) NMDAR function and dopamine (already mapped) metabolism, amplifying the oxidative stress (xanthine-oxidase already mapped) of schizophrenia.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Sz chloride: KCC2/NKCC1 chloride dysregulation shifts GABA (already mapped) from inhibitory to excitatory; chloride imbalance amplifies glutamate (already mapped) excitotoxicity and IL-6 (already mapped) neuroinflammation in neurons (already mapped) of schizophrenia.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Sz nitrogen: nitric oxide modulates dopamine (already mapped) and glutamate (already mapped) neurotransmission; NOS dysfunction in neurons (already mapped) and microglia (already mapped) amplifies IL-6 (already mapped) and mTOR (already mapped) cascade of schizophrenia.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Sz carbon: glycine and serine carbon scaffolds act as NMDA co-agonists modulating glutamate (already mapped); one-carbon metabolism deficits amplify BDNF (already mapped) signalling and IL-6 (already mapped) neuroinflammation in neurons (already mapped) of schizophrenia.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Sz oxygen: ROS from neurons (already mapped) and macrophages (already mapped) drives neuroinflammatory oxidative stress; oxygen-induced ROS amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade and worsens glutamate (already mapped) receptor damage in schizophrenia.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Sz hydrogen: hydrogen bonds stabilise neurotransmitter-receptor complexes in neurons (already mapped); oxidative hydrogen peroxide from macrophages (already mapped) drives NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of schizophrenia.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Sz NF-κB: NF-κB drives IL-6 (already mapped) and IL-1β (already mapped) transcription in macrophages (already mapped); sustained NF-κB activation amplifies dopamine (already mapped) dysregulation and suppresses BDNF (already mapped) neurotrophic signalling in schizophrenia.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Sz PD-1: PD-1 checkpoint on macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates neuroinflammatory immune surveillance; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of schizophrenia.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Sz Wnt/β-catenin: Wnt/β-catenin signalling in neurons (already mapped) and macrophages (already mapped) supports synaptic plasticity; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) cascade of schizophrenia.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Sz RANKL: RANKL signalling in macrophages (already mapped) and neurons (already mapped) modulates neuroinflammatory bone-immune crosstalk; RANKL dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and dopamine (already mapped) cascade of schizophrenia.

[^howes-2009-dopamine-hypothesis]: Howes OD, Kapur S. The dopamine hypothesis of schizophrenia: version III—the final common pathway. *Schizophr Bull.* 2009;35(3):549-562. [doi:10.1093/schbul/sbp006](https://doi.org/10.1093/schbul/sbp006) · [PubMed 19325164](https://pubmed.ncbi.nlm.nih.gov/19325164/)
[^moghaddam-2012-glutamate]: Moghaddam B, Javitt D. From revolution to evolution: the glutamate hypothesis of schizophrenia and its implication for treatment. *Neuropsychopharmacology.* 2012;37(1):4-15. [doi:10.1038/npp.2011.181](https://doi.org/10.1038/npp.2011.181) · [PubMed 21956446](https://pubmed.ncbi.nlm.nih.gov/21956446/)
[^leucht-2013-antipsychotics-meta]: Leucht S, Cipriani A, Spineli L, et al. Comparative efficacy and tolerability of 15 antipsychotic drugs in schizophrenia: a multiple-treatments meta-analysis. *Lancet.* 2013;382(9896):951-962. [doi:10.1016/S0140-6736(13)60733-3](https://doi.org/10.1016/S0140-6736(13)60733-3) · [PubMed 23810019](https://pubmed.ncbi.nlm.nih.gov/23810019/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
