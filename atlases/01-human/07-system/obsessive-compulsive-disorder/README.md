---
schema: human-scale-entry/v1
id: obsessive-compulsive-disorder
name: Obsessive-Compulsive Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "OCD (2-3% lifetime prevalence) is driven by cortico-striato-thalamo-cortical circuit hyperactivity; SSRIs at high doses are first-line; CBT with ERP achieves remission in ~60%; glutamatergic and dopaminergic dysregulation underlie treatment-resistant OCD."
aliases: ["OCD", "obsessive compulsive disorder", "obsessive-compulsive", "OCD spectrum", "CSTC circuit", "contamination OCD", "checking OCD", "hoarding disorder"]
sources:
  - id: abramowitz-2009-ocd-review
    type: peer-reviewed
    cite: "Abramowitz JS, Taylor S, McKay D. Obsessive-compulsive disorder. Lancet. 2009;374(9688):491-499."
    doi: "10.1016/S0140-6736(09)60240-3"
    pmid: "19665647"
    url: "https://doi.org/10.1016/S0140-6736(09)60240-3"
    accessed: "2026-06-08"
  - id: chamberlain-2008-ocd-neuroscience
    type: peer-reviewed
    cite: "Chamberlain SR, Menzies L, Hampshire A, et al. Orbitofrontal dysfunction in patients with obsessive-compulsive disorder and their unaffected relatives. Science. 2008;321(5887):421-422."
    doi: "10.1126/science.1154433"
    pmid: "18635808"
    url: "https://doi.org/10.1126/science.1154433"
    accessed: "2026-06-08"
  - id: pittenger-2017-ocd-glutamate
    type: peer-reviewed
    cite: "Pittenger C. Glutamate and anxiety disorders. Curr Top Behav Neurosci. 2015;23:145-168."
    doi: "10.1007/7854_2014_295"
    pmid: "25091538"
    url: "https://doi.org/10.1007/7854_2014_295"
    accessed: "2026-06-08"
  - id: soomro-2008-ssri-ocd
    type: peer-reviewed
    cite: "Soomro GM, Altman D, Rajagopal S, Oakley-Browne M. Selective serotonin re-uptake inhibitors (SSRIs) versus placebo for obsessive compulsive disorder (OCD). Cochrane Database Syst Rev. 2008;(1):CD001765."
    doi: "10.1002/14651858.CD001765.pub3"
    pmid: "18253995"
    url: "https://doi.org/10.1002/14651858.CD001765.pub3"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SSRIs at high doses (fluoxetine 40-80 mg, fluvoxamine, sertraline) are first-line OCD treatment; serotonin modulates cortico-striatal signaling; SSRI response in OCD requires 8-12 weeks at maximal doses; serotonergic augmentation of CBT improves outcomes."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine in ventral striatum and OFC drives reward learning and habit formation; CSTC circuit dopamine dysregulation contributes to compulsive behaviors; atypical antipsychotic augmentation (risperidone, aripiprazole) of SSRIs benefits treatment-resistant OCD via D2 blockade."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamatergic hyperactivity in OFC-striatum projections drives compulsive symptom circuits; riluzole (glutamate release inhibitor) and memantine reduce OCD symptoms in randomized trials; ketamine produces rapid anti-OCD effects in treatment-resistant cases."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Reduced GABAergic inhibitory tone in OFC and striatum contributes to CSTC hyperactivity in OCD; benzodiazepines provide short-term symptom relief; inositol (indirect GABA modulator) and D-cycloserine (NMDA partial agonist) augment ERP therapy outcomes."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "OCD is a CSTC circuit disorder: OFC and ACC hyperactivity → excessive error detection; caudate nucleus fail to suppress OFC-thalamus loop → repetitive behaviors; SSRI treatment and ERP both normalize caudate hypermetabolism on PET imaging."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Major depression is the most common comorbidity of OCD (~65% lifetime), usually arising secondary to the burden of obsessions and compulsions; the two share serotonergic dysfunction and both respond to SSRIs, though OCD needs higher doses and 8-12 weeks to respond."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "OCD is distinguished from generalized anxiety disorder by the form of the thoughts: OCD obsessions are intrusive, ego-dystonic, and trigger stereotyped compulsions, whereas GAD worry is about realistic everyday concerns, ego-syntonic, and not ritualized."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "PANDAS links Group A Streptococcus to abrupt-onset pediatric OCD: anti-streptococcal antibodies cross-react with basal-ganglia neurons to inflame the CSTC circuit, producing sudden obsessions and tics that may respond to antibiotics and immunotherapy."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "OCD and BPD both involve distressing, hard-to-control inner experience but differ in form: OCD is ego-dystonic intrusive thoughts and compulsions, BPD is emotional instability, impulsivity and unstable relationships; they can co-occur, with ERP/CBT central to OCD and DBT to BPD."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "OCD and autism overlap substantially: both feature repetitive behaviors and need for sameness, OCD is markedly more prevalent in autistic people, and distinguishing ego-dystonic compulsions from autistic routines (often not distressing in themselves) is a key clinical challenge."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "OCD and anorexia nervosa are closely linked: they share perfectionism, intrusive thoughts and ritualized behavior, frequently co-occur, and high premorbid OCD traits predict anorexia; orbitofrontal-striatal circuitry features in both, though anorexia's rituals center on food."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "OCD and panic disorder are anxiety-spectrum disorders that often co-occur but differ: OCD's anxiety is driven by intrusive obsessions relieved by compulsions, while panic is sudden autonomic surges of fear—both share SSRI responsiveness and exposure-based therapy."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "OCD and schizophrenia intersect in schizo-obsessive presentations: OC symptoms are common in schizophrenia and can worsen on antipsychotics like clozapine, and both involve glutamate and dopamine dysregulation—so telling obsessions from delusions guides care."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "OCD arises from dysfunction in cortico-striato-thalamo-cortical neurons: overactive loops through the orbitofrontal cortex, caudate, and thalamus generate the repetitive obsessions and compulsions, which is why SSRIs and, in refractory cases, deep brain stimulation can help."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "OCD and PTSD both feature intrusive, distressing thoughts but differ in origin: OCD's obsessions are recognized as one's own and neutralized by compulsions, while PTSD's intrusions are trauma memories—overlapping phenomenology with different roots."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "OCD and bipolar disorder frequently co-occur and complicate each other: comorbid OCD worsens bipolar outcomes, and SSRIs used for OCD can trigger mania in bipolar patients—so screening for bipolarity is essential before treating OCD pharmacologically."
  - target: 01-human/07-system/internet-gaming-disorder
    relation: connects-to
    note: "OCD and internet gaming disorder both involve compulsive, hard-to-resist behaviors engaging fronto-striatal circuits: OCD's compulsions relieve anxiety while gaming is reward-driven, but both show the loss of behavioral control that blurs compulsion and addiction."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "OCD involves a dysregulated stress axis: HPA-axis and cortisol abnormalities accompany the disorder, and stress worsens obsessions and compulsions—so the stress system interacts with the cortico-striatal circuits that drive the repetitive, intrusive symptoms."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "OCD sits within the anxiety-related spectrum alongside social anxiety: both involve excessive fear-driven avoidance and respond to SSRIs and exposure therapy, though OCD's hallmark is intrusive obsessions and ritualized compulsions rather than social fear."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "OCD shows altered cortico-striatal-limbic circuitry including the hippocampus: imaging reveals overactive orbitofrontal-striatal loops with hippocampal and memory-circuit changes, so OCD maps to specific brain-circuit dysfunction that medication and CBT recalibrate."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF links OCD to faulty brain wiring: this neuroplasticity factor shapes the cortico-striatal circuits that misfire in OCD, and BDNF gene variants are among its genetic risk factors—helping explain why SSRIs, which raise BDNF, slowly remodel the disorder."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "OCD and ADHD frequently co-occur yet pull in opposite directions: both involve frontostriatal dysfunction, but OCD is over-controlled and ADHD impulsive, so stimulants for ADHD can sometimes worsen obsessions—complicating treatment when the two coexist."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "Huntington's disease shows OCD's basal-ganglia roots: striatal degeneration produces perseverative, obsessive, and compulsive behaviors, echoing the cortico-striatal-thalamic loop that misfires in OCD—evidence this circuit can generate repetitive thought and action."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "OCD can flare from brain inflammation in PANDAS: after strep infection, activated microglia and autoantibodies inflame the basal ganglia, triggering sudden-onset obsessions and tics in children—evidence the immune system can drive the disorder."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "PANDAS ties OCD to immune genetics: streptococcal antigens presented by MHC class II can prime antibodies that cross-react with basal-ganglia neurons (molecular mimicry), an autoimmune route to abrupt childhood obsessive-compulsive symptoms."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "OCD and insomnia feed each other: intrusive obsessions and compulsive rituals delay and fragment sleep, and the resulting sleep loss worsens the anxiety and cognitive control that keep OCD going—so sleep is part of treatment."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Some childhood OCD is autoimmune, flagged by complement: in PANDAS, strep infection triggers antibodies and complement that attack basal-ganglia neurons, and complement-driven synaptic pruning is implicated in the circuit changes of OCD."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "OCD's faulty brain circuit involves astrocytes: these glial cells clear glutamate in the cortico-striatal loop that misfires in OCD, so astrocyte dysfunction may sustain the runaway excitation behind intrusive thoughts and compulsions."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Oxytocin shapes the repetitive behaviors of OCD: the bonding hormone also drives grooming and checking-type behaviors and is dysregulated in OCD, linking the social hormone to compulsive ritual."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "OCD is increasingly seen as a synapse disorder: genes for the glutamatergic synapse (like SAPAP3) disturb signaling in the cortico-striatal loop, so faulty synaptic wiring underlies the circuit that locks into obsessions and compulsions."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "OCD's signaling leans on calcium: voltage-gated calcium-channel genes implicated across psychiatric disorders shape the synaptic plasticity of the OCD circuit, tying ion flux to how compulsive habits are learned and held."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "In PANDAS, B cells turn OCD on suddenly: a strep infection makes the immune system produce cross-reactive antibodies that attack the basal ganglia, triggering abrupt-onset OCD and tics in susceptible children."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Brain imaging reveals OCD's overactive circuit: PET and fMRI photons show a hyperactive loop linking the orbitofrontal cortex, striatum and thalamus, the target even of radiosurgical capsulotomy in refractory cases."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "OCD shows altered white matter: the oligodendrocytes that myelinate the cortico-striatal tracts shape how fast the circuit signals, and changes in these connections appear in diffusion imaging studies."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut may sway OCD: emerging work ties the intestinal microbiome to anxiety and compulsive behavior through the gut-brain axis, hinting the bowel's microbes influence the disorder's severity."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "OCD's cousins attack the skin: body-focused repetitive behaviors — compulsive skin-picking and hair-pulling — sit in the OCD spectrum, driving sufferers to wound their own skin in irresistible, shame-laden rituals."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc may matter to the obsessive brain: low zinc is reported in OCD and the mineral modulates the glutamate signaling implicated in the disorder, so zinc supplementation has been trialed as an adjunct to standard treatment."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "OCD weighs on the heart over time: the chronic anxiety and stress raise cardiovascular risk, and the SSRIs that treat it can prolong the QT interval, so the heart is watched in long-term, high-dose therapy."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "OCD's most potent drug works partly on noradrenaline: clomipramine, the tricyclic that set the benchmark for treating it, blocks both serotonin and norepinephrine reuptake, a dual action that helps in cases SSRIs alone do not."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "OCD disturbs the night: insomnia and a delayed circadian rhythm with blunted melatonin are common, and the lost sleep worsens the intrusive thoughts and compulsions that already crowd the evening hours."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "OCD is increasingly seen as a glutamatergic disorder, and magnesium sits in that pathway: as a natural NMDA-receptor blocker it dampens the over-excitation of the cortico-striatal circuits, making it a studied adjunct alongside glutamate-modulating drugs."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Some childhood OCD is an autoimmune storm: in PANDAS/PANS, antibodies raised against streptococcus cross-react with basal-ganglia neurons, triggering abrupt-onset obsessions and tics that may respond to immune therapy rather than SSRIs alone."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hormonal transitions can unmask OCD: it often first appears or sharply worsens in pregnancy and the postpartum period, the perinatal form fixating on the baby's safety, while symptoms can also flare premenstrually."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut may whisper into the obsessive brain: altered microbiome composition is reported in OCD, and through the microbiome-gut-brain axis it can shape the serotonin and stress signaling implicated in the disorder."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "PANDAS makes OCD an autoimmune disease: after strep infection, molecular mimicry drives T helper cells and antibodies against basal-ganglia neurons, sparking the abrupt onset of obsessions and tics in susceptible children."
  - target: 01-human/07-system/bulimia-nervosa
    relation: connects-to
    note: "OCD and eating disorders share a compulsive core: bulimia nervosa frequently co-occurs with OCD, the binge-purge rituals echoing obsessive thoughts and compulsive acts, and the two run together in families."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation may stoke the obsessive brain: studies find raised IL-6 and other inflammatory cytokines in OCD, hinting that immune activation contributes to the disorder alongside its serotonin and glutamate disturbances."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is a disorder of a specific brain loop: OCD arises from overactivity in the cortico-striatal-thalamic circuit linking the orbitofrontal cortex and basal ganglia, the wiring whose miscommunication generates intrusive thoughts and the urge to ritualize."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "An immune arm shows up in some cases: in the PANDAS subtype where strep infection triggers OCD, dysregulated T-cell immunity — including regulatory T cells — lets autoantibodies cross-react with the basal ganglia."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The body's cannabis system modulates compulsivity: endocannabinoid signaling tunes the fear and habit circuits implicated in OCD, and cannabinoid agents are being explored for the obsessions and compulsions that resist standard drugs."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Neuroinflammation may stoke the circuits: NF-κB-driven microglial inflammation is implicated in OCD, fitting the autoimmune PANDAS subtype where strep-triggered inflammation inflames the basal ganglia behind sudden-onset symptoms."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Shared basal-ganglia wiring links them: OCD and Parkinson's both involve cortico-striatal circuits, and the dopamine-replacement therapy of Parkinson's can itself unleash obsessive-compulsive and impulse-control behaviors."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Compulsion can spill into the bottle: alcohol and other substance use disorders are over-represented in OCD, with some patients drinking to quiet relentless anxiety and intrusive thoughts."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "Compulsion can fix on food: the repetitive, hard-to-resist urges of OCD overlap with binge eating, and the two co-occur, sharing the impaired inhibitory control of cortico-striatal circuits."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Some self-medicate intrusive thoughts: cannabis is used by some with OCD to dampen anxiety and obsessions, a self-medication that can foster dependence while heavy use may worsen the underlying symptoms."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Temporal-lobe circuits can generate both: obsessive-compulsive symptoms are over-represented in epilepsy, especially temporal-lobe epilepsy, reflecting shared limbic and cortico-striatal dysfunction."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Headache keeps company with the disorder: OCD shows elevated comorbidity with migraine, the two sharing serotonergic dysregulation and a tendency toward chronic, recurrent symptom patterns."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Compulsive scratching meets chronic itch: OCD-spectrum skin-picking and the relentless itch of atopic dermatitis reinforce each other, and the two conditions co-occur more than chance."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Its long-term medications add weight: the high-dose SSRIs and antipsychotic augmentation used in OCD promote weight gain, contributing to obesity over years of treatment."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Compulsive washing wrecks the skin: repetitive handwashing in OCD causes chronic irritant contact dermatitis with cracking and bleeding, the visible toll of the contamination-and-cleaning cycle."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its strongest old drug strains the heart: clomipramine, the tricyclic uniquely effective in OCD, prolongs the QT interval and carries arrhythmia and orthostatic risk, demanding cardiac caution."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Anticholinergic therapy slows the gut: clomipramine and high-dose SSRIs used for OCD cause constipation and other anticholinergic and serotonergic gut effects that complicate long-term treatment."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Some childhood OCD is autoimmune: PANDAS/PANS describes abrupt OCD after streptococcal infection, part of a broader neuroinflammatory hypothesis implicating immune attack on basal-ganglia circuits."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its high-dose drugs unbalance sodium: the SSRIs and clomipramine central to OCD treatment can cause SIADH with hyponatraemia, a renal-electrolyte risk needing monitoring especially in older patients."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones modulate its course: OCD often emerges or worsens in pregnancy and the postpartum period, and the disorder shows dysregulation of the HPA cortisol stress axis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It overlaps tics and strains joints: OCD frequently coexists with tic disorders and Tourette syndrome, producing repetitive motor tics, and compulsive repeated actions cause repetitive-strain injury."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Compulsive cleaning irritates the airways: heavy use of bleach and disinfectants in contamination OCD can trigger asthma and airway irritation from chemical exposure."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "High-dose SSRIs are its mainstay: fluoxetine and other SSRIs, alongside clomipramine, are the pharmacological core of OCD treatment, needing higher doses and longer trials than in depression."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its post-streptococcal form starts in lymphoid tissue: in PANDAS, antibodies raised in tonsillar lymphoid tissue against streptococcus cross-react with the basal ganglia to trigger abrupt OCD."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet is studied as an adjunct: omega-3 fatty acids have been trialled for OCD and anxiety, with modest and inconsistent benefit alongside SSRIs and therapy."
  - target: 03-medicine/02-traditional/ashwagandha
    relation: connects-to
    note: "Traditional anxiolytics are tried: adaptogens such as ashwagandha are used by some for the anxiety underlying OCD, complementing rather than replacing first-line SSRIs."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Two ends of compulsivity: OCD compulsions are anxiety-driven and ego-dystonic while gambling is reward-driven, yet both engage dysfunctional cortico-striatal circuits, placing them on a shared obsessive-compulsive and impulsive spectrum."
  - target: 03-medicine/02-traditional/st-johns-wort
    relation: connects-to
    note: "A herbal serotonergic adjunct: St John's wort, which raises serotonin like the SSRIs that treat OCD, is tried for comorbid depression and anxiety — though OCD-specific evidence is weak and interactions are a concern."
  - target: 03-medicine/02-traditional/panax-ginseng
    relation: connects-to
    note: "An adaptogen for the anxiety burden: Panax ginseng is among the traditional remedies used for the chronic stress and anxiety accompanying OCD, an adjunct to the established SSRI and exposure therapy."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Its drugs watch the QT interval: high-dose SSRIs and especially clomipramine used for obsessive-compulsive disorder prolong the QT interval and can disturb cardiac conduction, requiring ECG monitoring at higher doses."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Augmentation carries metabolic cost: antipsychotics added to SSRIs in treatment-resistant OCD cause weight gain and insulin resistance, raising the risk of type 2 diabetes over time."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Shared striatal-dopamine dysregulation: obsessive-compulsive disorder and stimulant use disorder both involve dysregulated reward and habit circuits of the striatum, and stimulants can exacerbate compulsions and tics."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Lesions reveal the circuit: strokes and other injuries to the basal ganglia and orbitofrontal cortex can produce new-onset obsessive-compulsive symptoms, mapping OCD onto cortico-striatal-thalamic circuitry."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Compulsivity across disorders: obsessive-compulsive disorder and opioid use disorder share dysregulated cortico-striatal habit circuits, both marked by the shift from goal-directed to compulsive, hard-to-stop behaviour."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "An anxious, serotonergic overlap: obsessive-compulsive disorder commonly coexists with fibromyalgia, sharing serotonergic dysregulation and an anxiety-stress burden that both respond partly to SSRIs and SNRIs."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Pandemic amplifier: COVID-19 worsened obsessive-compulsive disorder, especially contamination and washing subtypes, while post-infectious immune activation is among the mechanisms linking infection to OCD."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The gut-brain axis in OCD: microbiome and intestinal-barrier signals influence the cortico-striatal circuits of obsessive-compulsive disorder, an emerging dimension of its biology beyond serotonin."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "Organic OCD: demyelinating lesions of multiple sclerosis in frontal and basal-ganglia circuits can produce secondary obsessive-compulsive symptoms, illustrating the cortico-striatal basis of the disorder."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neuroinflammation: elevated IL-1β and microglial activation in cortico-striatal circuits are increasingly implicated in OCD, linking immune signalling to symptom severity."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory cytokine: raised TNF-α in OCD supports an immune-mediated component to the disorder, consistent with its overlap with autoimmune and PANDAS-type presentations."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome link: NLRP3-driven IL-1β release from activated microglia is a proposed mechanism connecting innate immune activation to the neurocircuit dysfunction of OCD."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "First-line drug target: high-dose SSRIs blocking the serotonin transporter are the cornerstone of OCD pharmacotherapy, and SERT-gene variation is among the most studied genetic factors in the disorder."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Stress-axis dysregulation: altered CRH-driven HPA-axis reactivity accompanies OCD, linking chronic stress to symptom exacerbation in the cortico-striatal circuits underlying compulsions."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 and the blood-brain barrier: IL-17A from Th17 cells is implicated in the PANDAS subtype of OCD, where post-streptococcal autoimmunity and barrier disruption let anti-neuronal antibodies reach the basal ganglia."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormonal modulation: OCD onset and symptom severity fluctuate with reproductive events — pregnancy, postpartum and the premenstrual phase — implicating estrogen's modulation of the serotonergic circuits underlying the disorder."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Neuroinflammation: imaging shows microglial activation in the cortico-striatal circuits of OCD, and TLR4-driven innate immune signalling is a candidate mechanism linking infection and inflammation to symptom flares."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Striatal reward: opioid signalling in the striatum shapes the sense of reward and 'completeness' whose disturbance drives compulsions, and opioid-modulating agents have been explored in treatment-resistant OCD."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Striatal cholinergic tone: striatal cholinergic interneurons modulate the cortico-striato-thalamo-cortical circuit central to OCD, and their dysfunction is part of the overlap between OCD and the tic disorders that often co-occur with it."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Basal-ganglia peptide: substance P and its NK1 receptor are richly expressed in the basal-ganglia circuits implicated in OCD, a neuropeptide modulator of the striatal pathways whose dysregulation contributes to repetitive, compulsive behaviour."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitrergic signalling: neuronal nitric-oxide synthase shapes glutamatergic transmission and synaptic plasticity in the cortico-striatal circuit, and nNOS gene variants have been associated with OCD, implicating the nitrergic system in its pathophysiology."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Stress modulation: HPA-axis signalling through the glucocorticoid receptor (cortisol and CRH already mapped) modulates OCD symptom severity and the stress-triggered exacerbations characteristic of the disorder."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Synaptic plasticity: mTOR-dependent synaptic plasticity in the cortico-striatal-thalamo-cortical circuit shapes the maladaptive habit learning behind compulsions, and is implicated in rapid-acting glutamatergic treatments for OCD."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Habit-circuit plasticity: dopamine- and glutamate-driven ERK signalling in the striatum mediates the synaptic plasticity of habit formation that underlies the repetitive compulsive behaviour of OCD."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Synaptic regulation: GSK-3β regulates glutamatergic synaptic plasticity in the cortico-striato-thalamo-cortical circuits implicated in OCD, and is a target of the lithium augmentation used in refractory cases."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Neuroplastic signalling: PI3K-AKT signalling (with mTOR and ERK1/2 mapped) relays the BDNF-driven (mapped) neuroplasticity altered in the circuits underlying OCD."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "Stress axis: CRH-driven pituitary ACTH release (CRH, cortisol and the glucocorticoid receptor mapped) links stress to the symptom exacerbations of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR4-MyD88 innate neuroinflammatory signalling (TLR4 mapped) is implicated in the post-infectious/autoimmune (PANDAS) forms of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN-regulated PI3K-AKT-mTOR signalling (AKT, mTOR and GSK-3β mapped) shapes the cortico-striatal synaptic plasticity disrupted in OCD."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Striatal adenosine A2A receptors functionally oppose dopamine D2 signalling (dopamine mapped) in the cortico-striatal circuits whose dysregulation underlies OCD."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "BDNF-TrkB (NTRK) signalling shapes the cortico-striatal synaptic plasticity (BDNF already mapped) implicated in the habit-circuit dysfunction of OCD."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the neuroinflammatory tone implicated in OCD, including the autoimmune PANDAS subtype."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 released by activated microglia amplifies the neuroinflammation linked to the cortico-striatal dysfunction of OCD."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING in microglia contributes to the neuroinflammation implicated in OCD, including the autoimmune PANDAS subtype."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the inflammatory tone associated with the cortico-striatal circuit dysfunction of OCD."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT and PTEN already mapped) regulates neuronal plasticity and oxidative-stress handling relevant to OCD."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and oxidative-stress adaptation participates in the neurobiology of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the innate immune activation implicated in the neuroinflammatory (including PANDAS-associated) component of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 neuroinflammatory signaling contributes to the immune-related mechanisms proposed in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT and PTEN already mapped), downstream of BDNF-TrkB (BDNF and NTRK already mapped), participates in the cortico-striatal neuroplasticity implicated in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the neurometabolic changes associated with obsessive-compulsive disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic neurodevelopmental programming implicated in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal homeostasis of the cortico-striato-thalamo-cortical circuitry implicated in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the glutamatergic synaptic-plasticity mechanisms implicated in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation and PANDAS-associated immune mechanisms of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and neurodevelopmental interactions implicated in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neurodevelopmental gene programs implicated in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "PANDAS autoimmunity: paediatric acute-onset obsessive-compulsive symptoms can follow streptococcal infection, driven by IgG autoantibodies that cross-react with basal ganglia neurons, a distinct immune-mediated route into the CSTC circuitry."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histaminergic tone: histamine-H3 signalling modulates striatal dopamine, and histidine-decarboxylase mutations link the histaminergic system to Tourette syndrome and the obsessive-compulsive spectrum."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Perinatal course: obsessive-compulsive symptoms frequently first appear or worsen in pregnancy and the postpartum period, implicating progesterone and its neurosteroid metabolites in the hormonal triggering of symptom onset."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "PANDAS autoimmunity: in the paediatric autoimmune subtype, IL-2-driven T-cell responses to streptococcal infection help generate the anti-neuronal antibodies (MHC and IgG already mapped) that trigger abrupt-onset obsessive-compulsive symptoms."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Stress reactivity: central angiotensin II modulates stress and anxiety circuits and interacts with the HPA axis (cortisol already mapped), a neuroendocrine system implicated in the heightened stress that aggravates obsessive-compulsive symptoms."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex and development: obsessive-compulsive disorder often begins earlier and more often in boys, and androgens alongside estrogen (already mapped) are implicated in the sex differences and developmental timing of symptom onset."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune counter-regulation: IL-10 opposes the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) implicated in obsessive-compulsive disorder and its autoimmune PANDAS subtype (complement already mapped), part of the immune dimension of the disorder."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6 and IL-1 already mapped) modulate the cortico-striatal circuits implicated in obsessive-compulsive disorder, part of its immune-inflammatory contribution."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: heightened oxidative stress, to which xanthine oxidase contributes, is reported in obsessive-compulsive disorder, and the resulting reactive oxygen species (NLRP3 already mapped) may affect the neurons of the affected circuits."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation and PANDAS autoimmunity implicated in obsessive-compulsive disorder."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and monoamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the monoamine signalling of the circuits implicated in obsessive-compulsive disorder."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D and neuroimmunity: low vitamin D status has been reported in obsessive-compulsive disorder, and its modulation of neuroimmune and monoaminergic (serotonin already mapped) function is a proposed contributor."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation of the PANDAS/neuroimmune subtype of obsessive-compulsive disorder."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety-spectrum comorbidity: generalized anxiety disorder is commonly comorbid with obsessive-compulsive disorder, the two sharing the serotonergic (already mapped) treatment and the anxious-obsessional symptom overlap."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and glutamatergic modulation: synaptic zinc modulates the glutamate (already mapped)/NMDA signalling of the cortico-striatal circuit, and zinc has been trialled as an adjunct to the SSRIs in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic-inflammatory adipokine: leptin is the adipokine of the metabolic-inflammatory milieu and the neuroinflammation (TNF and IL-6 already mapped) implicated in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory milieu of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the neuroinflammation (IL-1 already mapped) of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the neuroinflammation implicated in the PANDAS (MHC and immunoglobulin already mapped) and idiopathic obsessive-compulsive disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation (IL-1 and TNF already mapped) associated with obsessive-compulsive disorder."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with obsessive-compulsive disorder."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammation associated with obsessive-compulsive disorder."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension reported in a subset with obsessive-compulsive disorder."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation implicated in obsessive-compulsive disorder."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Autoimmune arm: the cytotoxic T cells (perforin pathway), in the PANDAS/PANS autoimmune subset triggered by the streptococcus (already mapped), contribute to the basal-ganglia targeting of obsessive-compulsive disorder."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Peripheral innate arm: the NK cells (perforin pathway) are part of the peripheral innate-immune dysregulation reported in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the complement activation of the PANDAS/PANS autoimmune neuroinflammation implicated in obsessive-compulsive disorder."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) basal-ganglia neuroinflammation of obsessive-compulsive disorder."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Autoimmune priming: the dendritic cells present the streptococcal (already mapped) antigen in the PANDAS/PANS subset, priming the T cells (already mapped) of the basal-ganglia autoimmunity of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuro-immune alarmin: TSLP, released by skin (already mapped) and gut-epithelial (already mapped) barriers during PANDAS/PANS infections, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the systemic immune activation of OCD."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin neuro-vascular axis: bradykinin, generated during streptococcal (already mapped) and complement (C3, C5, C5aR1 already mapped) activation, augments blood-brain-barrier permeability and enables the autoantibody access to the basal ganglia of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) activation in the basal-ganglia neuroinflammation of obsessive-compulsive disorder."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM remodelling in the cortico-striatal circuit: periostin, expressed by astrocytes (already mapped) and microglia (already mapped) under neuroinflammation, modulates the extracellular matrix of the basal ganglia that is disrupted in OCD."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective cytokine: erythropoietin, via EPOR on neurons and astrocytes (already mapped), suppresses neuroinflammatory cytokines (TNF-α and IL-6 already mapped) and limits the oxidative damage in the fronto-striatal circuitry of OCD."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine coupling: prolactin, elevated by antipsychotic medications used as augmentation in OCD (serotonin and dopamine already mapped), modulates the T-cell (already mapped) immune function and amplifies the female-predominant endocrine skew of OCD."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "OCD vasopressin: vasopressin V1A receptors in the cortico-striatal circuit (brain already mapped) modulate the anxiety-driven repetitive behaviours of OCD; vasopressin interacts with oxytocin (already mapped) to co-regulate social threat processing and compulsivity."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "OCD transferrin: transferrin supports neuronal (already mapped) iron metabolism and myelin integrity in the fronto-striatal circuitry; iron deficiency via disordered transferrin amplifies the dopaminergic (already mapped) dysfunction and compulsivity of OCD."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "OCD factor-h: factor H regulates the alternative complement pathway (C5 and C5aR1 already mapped) over-activation in the neuroinflammatory basal-ganglia environment of OCD; reduced factor H activity amplifies the complement-driven microglial (already mapped) activation."
---

# Obsessive-Compulsive Disorder

## Overview

**Obsessive-compulsive disorder (OCD)** is a chronic, disabling neuropsychiatric condition characterized by recurrent **obsessions** (intrusive, unwanted thoughts, images, or urges causing marked anxiety) and **compulsions** (repetitive behaviors or mental acts performed to neutralize anxiety) that consume ≥1 hour per day and cause significant functional impairment [^abramowitz-2009-ocd-review].

OCD affects approximately **2–3% of the global population** (lifetime prevalence) — roughly 75–100 million people — and carries the fourth-highest burden of neuropsychiatric illness worldwide by disability-adjusted life years (DALYs). Mean age of onset is bimodal: **early-onset** (~10 years, male-predominant) and **adult-onset** (~20 years, female-predominant). Onset is usually gradual, worsens under stress, and is chronic in ~40–50% of untreated cases.

**DSM-5 diagnosis** requires:
1. Presence of obsessions, compulsions, or both
2. Time-consuming (>1 hour/day) or causing significant distress/impairment
3. Not attributable to substances or medical conditions
4. Not better explained by another psychiatric disorder

**OCD spectrum disorders** (DSM-5 "Obsessive-Compulsive and Related Disorders" chapter) include body dysmorphic disorder (BDD), hoarding disorder, trichotillomania (hair-pulling), excoriation (skin-picking), and olfactory reference disorder — all sharing CSTC circuit dysfunction.

## Structure

### OCD subtypes and common themes

| Obsession theme | Core fear | Compulsion type |
|:---|:---|:---|
| **Contamination** | Illness, dirt, spreading germs | Washing, cleaning, avoidance |
| **Checking** | Harm to self/others, incompleteness | Repeated checking (locks, stoves, light switches) |
| **Symmetry/ordering** | "Not just right" feeling, incompleteness | Arranging, counting, touching |
| **Unacceptable thoughts** | Blasphemous, sexual, violent intrusive thoughts | Mental rituals, seeking reassurance, avoidance |
| **Hoarding** | Fear of losing important items | Excessive acquisition, inability to discard |

**Y-BOCS (Yale-Brown Obsessive Compulsive Scale)** is the gold-standard severity measure: 10 items (5 obsession + 5 compulsion, each rated 0–4); total 0–40; mild 8–15, moderate 16–23, severe 24–31, extreme 32–40. Treatment response is defined as ≥35% Y-BOCS reduction.

### Cortico-striato-thalamo-cortical (CSTC) circuit model [^chamberlain-2008-ocd-neuroscience]

OCD is understood as a circuit disorder with two competing pathways:

**"Worry loop" (hyperactive in OCD):**
Orbitofrontal cortex (OFC) → caudate nucleus → globus pallidus interna (GPi) → thalamus → back to OFC (direct pathway via striatum → inhibits GPi → disinhibits thalamus → enhances OFC activity)

**Normal suppression mechanism (underactive in OCD):**
OFC → putamen → globus pallidus externa (GPe) → subthalamic nucleus → GPi → thalamus → OFC suppression (indirect pathway)

**OCD pathology:** Caudate nucleus hyperactivity disinhibits the thalamus → excess thalamocortical drive back to OFC → OFC → excessive error monitoring signals ("something is wrong" even after checking) → compulsive corrective behaviors that fail to terminate because the "error" signal persists.

**PET/fMRI evidence:**
- Pre-treatment: increased glucose metabolism in OFC (Brodmann area 11/12/13), caudate nucleus, and thalamus in untreated OCD
- Post-treatment (SSRI or CBT/ERP): normalized caudate and OFC activity, with both treatments converging on the same circuit
- Unaffected relatives of OCD patients show intermediate OFC hyperactivity [^chamberlain-2008-ocd-neuroscience], suggesting a heritable endophenotype

## Function

### Clinical presentation

**Obsessions:** Ego-dystonic (experienced as unwanted, contrary to self-concept), intrusive, and cause marked anxiety. Unlike generalized worry, obsessions are focused on specific feared outcomes and trigger compulsive responses. Common obsessions are sexual, blasphemous, or violent intrusions in ~60%, contamination fears in ~50%, and symmetry/ordering concerns in ~40% (many patients have multiple themes).

**Compulsions:** Repetitive behaviors (washing, checking, ordering) or mental acts (praying, counting, undoing) that temporarily reduce obsessional anxiety but are not pleasurable in themselves and not proportionate to any realistic threat. The temporary relief powerfully reinforces compulsive behavior via negative reinforcement — explaining the self-perpetuating nature of OCD.

**Insight:** Approximately 95% of OCD patients have good-to-fair insight (recognize obsessions as unreasonable); ~5% have poor or absent insight (may appear delusional). Poor insight predicts worse treatment response and greater functional impairment.

**OCD with tic disorder:** ~20-30% of OCD patients have comorbid Tourette syndrome or chronic tic disorder; this subgroup has earlier onset, male predominance, and modestly different treatment response (alpha-2 agonists or antipsychotic augmentation more beneficial).

### Comorbidities

| Comorbidity | Frequency | Implication |
|:---|:---|:---|
| Major depressive disorder | ~65% | Leads to earlier treatment seeking; depression secondary to OCD in most cases |
| Anxiety disorders (GAD, SAD, panic) | ~50% | Shared CSTC/serotonergic dysfunction; SSRIs treat both |
| ADHD | ~20-30% | May require stimulant treatment even in OCD; stimulants rarely worsen OCD |
| Tic disorder/Tourette | ~20-30% | Antipsychotic augmentation more effective |
| Body dysmorphic disorder | ~15% | Same neurobiology, same treatment; may require higher SSRI doses |
| Hoarding disorder | ~25% | Lower SSRI response; may benefit more from CBT/cognitive approaches |

## Pathology

### Neurobiology

**Serotonergic system:** SSRIs are uniquely effective for OCD (compared to imipramine and desipramine, which are ineffective) — establishing a privileged role for serotonin in OCD pathophysiology. High SSRI doses are typically required (fluoxetine 40-80 mg/day vs. 20-40 mg for depression), and full response takes 8-12 weeks. Clomipramine (tricyclic SNRI with dominant serotonin reuptake inhibition) is equally effective to SSRIs but has worse tolerability [^soomro-2008-ssri-ocd].

**Glutamatergic system:** OFC-striatal projections use glutamate as the primary neurotransmitter [^pittenger-2017-ocd-glutamate]. CSF glutamate levels are elevated in OCD. Riluzole (glutamate release inhibitor) reduces OCD symptoms in randomized controlled trials; memantine (NMDA antagonist) shows benefit in treatment-resistant OCD; single-dose ketamine (NMDA antagonist) produces rapid (~48 hour) anti-compulsive effects.

**Dopaminergic system:** Striatal dopamine dysregulation in OCD contributes to habitual behavior formation. PET studies show D2 receptor abnormalities in caudate. Atypical antipsychotic augmentation (risperidone 0.5-2 mg, aripiprazole 10-15 mg) of SSRI is the best-supported strategy for partial SSRI responders (NNT ~3-4 in pooled trials).

**GABAergic system:** Reduced GABA in OFC and basal ganglia (MRS studies) contributes to CSTC hyperactivity. Benzodiazepines reduce OCD anxiety acutely but do not treat core OCD; long-term use risks dependence.

**Genetics:** OCD is moderately heritable (~40-65% twin studies). First-degree relatives have 5-10× elevated risk. GWAS: no single large-effect loci; implicated pathways include glutamatergic signaling (GRIN2B, DLGAP1, SLC1A1) and serotonin metabolism (SERT/SLC6A4, HTR2A). Copy number variants: 16p13.11 microduplications; 22q11.2 deletions. OCD is genetically correlated with Tourette syndrome (common neuronal circuits) and anxiety disorders.

### Diagnosis

OCD is often underdiagnosed due to shame and secrecy. Mean time from symptom onset to diagnosis is **7-10 years**. Key diagnostic pitfalls:

- **OCD vs. GAD:** OCD obsessions are intrusive, ego-dystonic, and trigger specific compulsions; GAD worry is about realistic everyday concerns, is ego-syntonic, and is not followed by stereotyped compulsions
- **OCD vs. psychosis:** OCD patients retain insight that obsessions are products of their own mind; psychotic patients have true delusions/hallucinations with absent insight
- **Pediatric OCD:** PANS/PANDAS (Pediatric Acute-onset Neuropsychiatric Syndrome) — sudden-onset OCD following Group A streptococcal infection; autoimmune anti-basal ganglia antibodies; treated with antibiotics and immunotherapy plus standard OCD therapy

### Treatment

**First-line — Cognitive-Behavioral Therapy (CBT) with Exposure and Response Prevention (ERP):**
- Gold-standard psychotherapy: patient deliberately confronts feared stimuli (exposure) and refrains from compulsive responses (response prevention) → habituation and violation of feared predictions → CSTC circuit normalization
- Achieves ≥35% Y-BOCS improvement (treatment response) in ~60-70%; remission in ~30-40%
- Optimal delivery: individual therapist-guided sessions (typically 14-20 sessions), 90-minute exposure sessions; limited by access and patient dropout (confronting feared situations is distressing)
- D-cycloserine (partial NMDA agonist, 50 mg before exposure sessions): augments ERP by enhancing NMDA-dependent fear extinction learning; modest effect size in meta-analyses

**First-line — SSRIs (at OCD-level doses):**

| Drug | Starting dose | OCD target dose | Notes |
|:---|:---|:---|:---|
| **Fluoxetine** | 20 mg/day | 40-80 mg/day | Long half-life (active metabolite); once-daily; minimal withdrawal |
| **Fluvoxamine** | 50 mg/day | 150-300 mg/day | FDA-approved for OCD in adults and children; twice-daily; notable CYP1A2/2C19 interactions |
| **Sertraline** | 25-50 mg/day | 100-200 mg/day | FDA-approved for OCD; well-tolerated; once-daily; most-prescribed |
| **Paroxetine** | 10-20 mg/day | 40-60 mg/day | FDA-approved; anticholinergic effects; withdrawal syndrome with abrupt discontinuation |
| **Clomipramine** | 25 mg/day | 100-250 mg/day | Non-selective TCA; equivalent efficacy to SSRIs; anticholinergic + cardiac AEs limit use; reserved for SSRI failures |

**Allow 8-12 weeks** at maximal tolerated dose before declaring failure. Approximately 40-60% of patients respond partially; combination SSRI + ERP is superior to either alone.

**Second-line — Augmentation strategies for SSRI-partial response:**

| Strategy | Evidence | Notes |
|:---|:---|:---|
| **Aripiprazole** (5-15 mg) | Strong (RCT-level) | Partial D2 agonist; reduces EPS vs. risperidone; weight gain |
| **Risperidone** (0.5-2 mg) | Strong (RCT-level) | D2/5-HT2A antagonist; NNT ~3.4; weight gain, EPS possible |
| **Quetiapine** (50-150 mg) | Moderate | More sedating; used when insomnia is comorbid |
| **Riluzole** (50-100 mg) | Moderate (RCT) | Reduces OFC glutamate release; especially in pediatric OCD |
| **Memantine** (5-20 mg) | Moderate (open-label) | NMDA antagonism; reduces Y-BOCS in several small RCTs |

**Neuromodulation (treatment-resistant OCD — SSRI + ERP failures):**
- **Deep brain stimulation (DBS):** FDA Humanitarian Device Exemption (HDE) approval 2009 for treatment-resistant OCD; targets include anterior limb of internal capsule/ventral capsule–ventral striatum (VC/VS), nucleus accumbens, and subthalamic nucleus (STN); 50-60% response rate (≥35% Y-BOCS reduction) in carefully selected patients
- **Transcranial magnetic stimulation (TMS):** FDA-cleared 2018 for OCD; targets supplementary motor area (SMA) or dorsal medial PFC (dmPFC); inhibitory theta-burst or low-frequency rTMS; response ~40% in treatment-resistant patients; well-tolerated
- **Gamma Knife radiosurgery (anterior capsulotomy):** Used in extreme treatment-resistant cases; creates anterior capsule lesion to disrupt CSTC circuit; effective but irreversible

## Connections

- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — SSRIs at high doses are uniquely effective for OCD; serotonin modulates OFC-striatal CSTC signaling; clomipramine (TCA with dominant serotonin reuptake inhibition) has equivalent efficacy to SSRIs and 8-12 weeks response latency.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — striatal dopamine dysregulation contributes to compulsive habit formation in OCD; D2 receptor abnormalities in caudate on PET; atypical antipsychotic augmentation (aripiprazole, risperidone) of SSRIs is the best-supported strategy for partial SSRI responders (NNT ~3).
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — glutamatergic hyperactivity in OFC-striatum projections drives compulsive symptom circuits; CSF glutamate elevated in OCD; riluzole and memantine reduce OCD symptoms in RCTs; ketamine produces rapid anti-compulsive effects in treatment-resistant OCD.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — reduced GABAergic inhibitory tone in OFC and striatum (MRS studies) contributes to CSTC hyperactivity; benzodiazepines provide short-term relief but not disease modification; D-cycloserine (NMDA partial agonist) augments ERP via fear extinction learning.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — OCD is a CSTC circuit disorder: OFC/ACC hyperactivity drives excessive error detection; caudate nucleus hyperactivity disinhibits thalamocortical drive back to OFC; SSRIs and ERP both normalize caudate hypermetabolism on PET — converging on the same circuit.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Major depression is the most common comorbidity of OCD (~65% lifetime), usually arising secondary to the burden of obsessions and compulsions; the two share serotonergic dysfunction and both respond to SSRIs, though OCD needs higher doses and 8-12 weeks to respond.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — OCD is distinguished from generalized anxiety disorder by the form of the thoughts: OCD obsessions are intrusive, ego-dystonic, and trigger stereotyped compulsions, whereas GAD worry is about realistic everyday concerns, ego-syntonic, and not ritualized.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — PANDAS links Group A Streptococcus to abrupt-onset pediatric OCD: anti-streptococcal antibodies cross-react with basal-ganglia neurons to inflame the CSTC circuit, producing sudden obsessions and tics that may respond to antibiotics and immunotherapy.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — OCD and BPD both involve distressing, hard-to-control inner experience but differ in form: OCD is ego-dystonic intrusive thoughts and compulsions, BPD is emotional instability, impulsivity and unstable relationships; they can co-occur, with ERP/CBT central to OCD and DBT to BPD.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — OCD and autism overlap substantially: both feature repetitive behaviors and need for sameness, OCD is markedly more prevalent in autistic people, and distinguishing ego-dystonic compulsions from autistic routines (often not distressing in themselves) is a key clinical challenge.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — OCD and anorexia nervosa are closely linked: they share perfectionism, intrusive thoughts and ritualized behavior, frequently co-occur, and high premorbid OCD traits predict anorexia; orbitofrontal-striatal circuitry features in both, though anorexia's rituals center on food.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — OCD and panic disorder are anxiety-spectrum disorders that often co-occur but differ: OCD's anxiety is driven by intrusive obsessions relieved by compulsions, while panic is sudden autonomic surges of fear—both share SSRI responsiveness and exposure-based therapy.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — OCD and schizophrenia intersect in schizo-obsessive presentations: OC symptoms are common in schizophrenia and can worsen on antipsychotics like clozapine, and both involve glutamate and dopamine dysregulation—so telling obsessions from delusions guides care.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — OCD arises from dysfunction in cortico-striato-thalamo-cortical neurons: overactive loops through the orbitofrontal cortex, caudate, and thalamus generate the repetitive obsessions and compulsions, which is why SSRIs and, in refractory cases, deep brain stimulation can help.
- `connects-to` → **[PTSD](../ptsd/README.md)** — OCD and PTSD both feature intrusive, distressing thoughts but differ in origin: OCD's obsessions are recognized as one's own and neutralized by compulsions, while PTSD's intrusions are trauma memories—overlapping phenomenology with different roots.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — OCD and bipolar disorder frequently co-occur and complicate each other: comorbid OCD worsens bipolar outcomes, and SSRIs used for OCD can trigger mania in bipolar patients—so screening for bipolarity is essential before treating OCD pharmacologically.
- `connects-to` → **[Internet Gaming Disorder](../internet-gaming-disorder/README.md)** — OCD and internet gaming disorder both involve compulsive, hard-to-resist behaviors engaging fronto-striatal circuits: OCD's compulsions relieve anxiety while gaming is reward-driven, but both show the loss of behavioral control that blurs compulsion and addiction.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — OCD involves a dysregulated stress axis: HPA-axis and cortisol abnormalities accompany the disorder, and stress worsens obsessions and compulsions—so the stress system interacts with the cortico-striatal circuits that drive the repetitive, intrusive symptoms.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — OCD sits within the anxiety-related spectrum alongside social anxiety: both involve excessive fear-driven avoidance and respond to SSRIs and exposure therapy, though OCD's hallmark is intrusive obsessions and ritualized compulsions rather than social fear.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — OCD shows altered cortico-striatal-limbic circuitry including the hippocampus: imaging reveals overactive orbitofrontal-striatal loops with hippocampal and memory-circuit changes, so OCD maps to specific brain-circuit dysfunction that medication and CBT recalibrate.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF links OCD to faulty brain wiring: this neuroplasticity factor shapes the cortico-striatal circuits that misfire in OCD, and BDNF gene variants are among its genetic risk factors—helping explain why SSRIs, which raise BDNF, slowly remodel the disorder.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — OCD and ADHD frequently co-occur yet pull in opposite directions: both involve frontostriatal dysfunction, but OCD is over-controlled and ADHD impulsive, so stimulants for ADHD can sometimes worsen obsessions—complicating treatment when the two coexist.
- `connects-to` → **[Huntington Disease](../huntingtons-disease/README.md)** — Huntington's disease shows OCD's basal-ganglia roots: striatal degeneration produces perseverative, obsessive, and compulsive behaviors, echoing the cortico-striatal-thalamic loop that misfires in OCD—evidence this circuit can generate repetitive thought and action.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — OCD can flare from brain inflammation in PANDAS: after strep infection, activated microglia and autoantibodies inflame the basal ganglia, triggering sudden-onset obsessions and tics in children—evidence the immune system can drive the disorder.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — PANDAS ties OCD to immune genetics: streptococcal antigens presented by MHC class II can prime antibodies that cross-react with basal-ganglia neurons (molecular mimicry), an autoimmune route to abrupt childhood obsessive-compulsive symptoms.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — OCD and insomnia feed each other: intrusive obsessions and compulsive rituals delay and fragment sleep, and the resulting sleep loss worsens the anxiety and cognitive control that keep OCD going—so sleep is part of treatment.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Some childhood OCD is autoimmune, flagged by complement: in PANDAS, strep infection triggers antibodies and complement that attack basal-ganglia neurons, and complement-driven synaptic pruning is implicated in the circuit changes of OCD.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — OCD's faulty brain circuit involves astrocytes: these glial cells clear glutamate in the cortico-striatal loop that misfires in OCD, so astrocyte dysfunction may sustain the runaway excitation behind intrusive thoughts and compulsions.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Oxytocin shapes the repetitive behaviors of OCD: the bonding hormone also drives grooming and checking-type behaviors and is dysregulated in OCD, linking the social hormone to compulsive ritual.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — OCD is increasingly seen as a synapse disorder: genes for the glutamatergic synapse (like SAPAP3) disturb signaling in the cortico-striatal loop, so faulty synaptic wiring underlies the circuit that locks into obsessions and compulsions.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — OCD's signaling leans on calcium: voltage-gated calcium-channel genes implicated across psychiatric disorders shape the synaptic plasticity of the OCD circuit, tying ion flux to how compulsive habits are learned and held.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — In PANDAS, B cells turn OCD on suddenly: a strep infection makes the immune system produce cross-reactive antibodies that attack the basal ganglia, triggering abrupt-onset OCD and tics in susceptible children.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Brain imaging reveals OCD's overactive circuit: PET and fMRI photons show a hyperactive loop linking the orbitofrontal cortex, striatum and thalamus, the target even of radiosurgical capsulotomy in refractory cases.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — OCD shows altered white matter: the oligodendrocytes that myelinate the cortico-striatal tracts shape how fast the circuit signals, and changes in these connections appear in diffusion imaging studies.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut may sway OCD: emerging work ties the intestinal microbiome to anxiety and compulsive behavior through the gut-brain axis, hinting the bowel's microbes influence the disorder's severity.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — OCD's cousins attack the skin: body-focused repetitive behaviors — compulsive skin-picking and hair-pulling — sit in the OCD spectrum, driving sufferers to wound their own skin in irresistible, shame-laden rituals.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc may matter to the obsessive brain: low zinc is reported in OCD and the mineral modulates the glutamate signaling implicated in the disorder, so zinc supplementation has been trialed as an adjunct to standard treatment.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — OCD weighs on the heart over time: the chronic anxiety and stress raise cardiovascular risk, and the SSRIs that treat it can prolong the QT interval, so the heart is watched in long-term, high-dose therapy.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — OCD's most potent drug works partly on noradrenaline: clomipramine, the tricyclic that set the benchmark for treating it, blocks both serotonin and norepinephrine reuptake, a dual action that helps in cases SSRIs alone do not.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — OCD disturbs the night: insomnia and a delayed circadian rhythm with blunted melatonin are common, and the lost sleep worsens the intrusive thoughts and compulsions that already crowd the evening hours.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — OCD is increasingly seen as a glutamatergic disorder, and magnesium sits in that pathway: as a natural NMDA-receptor blocker it dampens the over-excitation of the cortico-striatal circuits, making it a studied adjunct alongside glutamate-modulating drugs.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Some childhood OCD is an autoimmune storm: in PANDAS/PANS, antibodies raised against streptococcus cross-react with basal-ganglia neurons, triggering abrupt-onset obsessions and tics that may respond to immune therapy rather than SSRIs alone.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hormonal transitions can unmask OCD: it often first appears or sharply worsens in pregnancy and the postpartum period, the perinatal form fixating on the baby's safety, while symptoms can also flare premenstrually.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut may whisper into the obsessive brain: altered microbiome composition is reported in OCD, and through the microbiome-gut-brain axis it can shape the serotonin and stress signaling implicated in the disorder.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — PANDAS makes OCD an autoimmune disease: after strep infection, molecular mimicry drives T helper cells and antibodies against basal-ganglia neurons, sparking the abrupt onset of obsessions and tics in susceptible children.
- `connects-to` → **[Bulimia Nervosa](../bulimia-nervosa/README.md)** — OCD and eating disorders share a compulsive core: bulimia nervosa frequently co-occurs with OCD, the binge-purge rituals echoing obsessive thoughts and compulsive acts, and the two run together in families.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation may stoke the obsessive brain: studies find raised IL-6 and other inflammatory cytokines in OCD, hinting that immune activation contributes to the disorder alongside its serotonin and glutamate disturbances.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is a disorder of a specific brain loop: OCD arises from overactivity in the cortico-striatal-thalamic circuit linking the orbitofrontal cortex and basal ganglia, the wiring whose miscommunication generates intrusive thoughts and the urge to ritualize.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — An immune arm shows up in some cases: in the PANDAS subtype where strep infection triggers OCD, dysregulated T-cell immunity — including regulatory T cells — lets autoantibodies cross-react with the basal ganglia.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The body's cannabis system modulates compulsivity: endocannabinoid signaling tunes the fear and habit circuits implicated in OCD, and cannabinoid agents are being explored for the obsessions and compulsions that resist standard drugs.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Neuroinflammation may stoke the circuits: NF-κB-driven microglial inflammation is implicated in OCD, fitting the autoimmune PANDAS subtype where strep-triggered inflammation inflames the basal ganglia behind sudden-onset symptoms.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Shared basal-ganglia wiring links them: OCD and Parkinson's both involve cortico-striatal circuits, and the dopamine-replacement therapy of Parkinson's can itself unleash obsessive-compulsive and impulse-control behaviors.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Compulsion can spill into the bottle: alcohol and other substance use disorders are over-represented in OCD, with some patients drinking to quiet relentless anxiety and intrusive thoughts.
- `connects-to` → **[Binge Eating Disorder](../binge-eating-disorder/README.md)** — Compulsion can fix on food: the repetitive, hard-to-resist urges of OCD overlap with binge eating, and the two co-occur, sharing the impaired inhibitory control of cortico-striatal circuits.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Some self-medicate intrusive thoughts: cannabis is used by some with OCD to dampen anxiety and obsessions, a self-medication that can foster dependence while heavy use may worsen the underlying symptoms.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Temporal-lobe circuits can generate both: obsessive-compulsive symptoms are over-represented in epilepsy, especially temporal-lobe epilepsy, reflecting shared limbic and cortico-striatal dysfunction.
- `connects-to` → **[Migraine](../migraine/README.md)** — Headache keeps company with the disorder: OCD shows elevated comorbidity with migraine, the two sharing serotonergic dysregulation and a tendency toward chronic, recurrent symptom patterns.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Compulsive scratching meets chronic itch: OCD-spectrum skin-picking and the relentless itch of atopic dermatitis reinforce each other, and the two conditions co-occur more than chance.
- `connects-to` → **[Obesity](../obesity/README.md)** — Its long-term medications add weight: the high-dose SSRIs and antipsychotic augmentation used in OCD promote weight gain, contributing to obesity over years of treatment.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Compulsive washing wrecks the skin: repetitive handwashing in OCD causes chronic irritant contact dermatitis with cracking and bleeding, the visible toll of the contamination-and-cleaning cycle.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its strongest old drug strains the heart: clomipramine, the tricyclic uniquely effective in OCD, prolongs the QT interval and carries arrhythmia and orthostatic risk, demanding cardiac caution.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Anticholinergic therapy slows the gut: clomipramine and high-dose SSRIs used for OCD cause constipation and other anticholinergic and serotonergic gut effects that complicate long-term treatment.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Some childhood OCD is autoimmune: PANDAS/PANS describes abrupt OCD after streptococcal infection, part of a broader neuroinflammatory hypothesis implicating immune attack on basal-ganglia circuits.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its high-dose drugs unbalance sodium: the SSRIs and clomipramine central to OCD treatment can cause SIADH with hyponatraemia, a renal-electrolyte risk needing monitoring especially in older patients.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones modulate its course: OCD often emerges or worsens in pregnancy and the postpartum period, and the disorder shows dysregulation of the HPA cortisol stress axis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It overlaps tics and strains joints: OCD frequently coexists with tic disorders and Tourette syndrome, producing repetitive motor tics, and compulsive repeated actions cause repetitive-strain injury.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Compulsive cleaning irritates the airways: heavy use of bleach and disinfectants in contamination OCD can trigger asthma and airway irritation from chemical exposure.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — High-dose SSRIs are its mainstay: fluoxetine and other SSRIs, alongside clomipramine, are the pharmacological core of OCD treatment, needing higher doses and longer trials than in depression.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its post-streptococcal form starts in lymphoid tissue: in PANDAS, antibodies raised in tonsillar lymphoid tissue against streptococcus cross-react with the basal ganglia to trigger abrupt OCD.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet is studied as an adjunct: omega-3 fatty acids have been trialled for OCD and anxiety, with modest and inconsistent benefit alongside SSRIs and therapy.
- `connects-to` → **[Ashwagandha](../../../03-medicine/02-traditional/ashwagandha/README.md)** — Traditional anxiolytics are tried: adaptogens such as ashwagandha are used by some for the anxiety underlying OCD, complementing rather than replacing first-line SSRIs.
- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — Two ends of compulsivity: OCD compulsions are anxiety-driven and ego-dystonic while gambling is reward-driven, yet both engage dysfunctional cortico-striatal circuits, placing them on a shared obsessive-compulsive and impulsive spectrum.
- `connects-to` → **[St John's Wort](../../../03-medicine/02-traditional/st-johns-wort/README.md)** — A herbal serotonergic adjunct: St John's wort, which raises serotonin like the SSRIs that treat OCD, is tried for comorbid depression and anxiety — though OCD-specific evidence is weak and interactions are a concern.
- `connects-to` → **[Panax Ginseng](../../../03-medicine/02-traditional/panax-ginseng/README.md)** — An adaptogen for the anxiety burden: Panax ginseng is among the traditional remedies used for the chronic stress and anxiety accompanying OCD, an adjunct to the established SSRI and exposure therapy.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Its drugs watch the QT interval: high-dose SSRIs and especially clomipramine used for obsessive-compulsive disorder prolong the QT interval and can disturb cardiac conduction, requiring ECG monitoring at higher doses.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Augmentation carries metabolic cost: antipsychotics added to SSRIs in treatment-resistant OCD cause weight gain and insulin resistance, raising the risk of type 2 diabetes over time.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Shared striatal-dopamine dysregulation: obsessive-compulsive disorder and stimulant use disorder both involve dysregulated reward and habit circuits of the striatum, and stimulants can exacerbate compulsions and tics.
- `connects-to` → **[Stroke](../stroke/README.md)** — Lesions reveal the circuit: strokes and other injuries to the basal ganglia and orbitofrontal cortex can produce new-onset obsessive-compulsive symptoms, mapping OCD onto cortico-striatal-thalamic circuitry.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Compulsivity across disorders: obsessive-compulsive disorder and opioid use disorder share dysregulated cortico-striatal habit circuits, both marked by the shift from goal-directed to compulsive, hard-to-stop behaviour.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — An anxious, serotonergic overlap: obsessive-compulsive disorder commonly coexists with fibromyalgia, sharing serotonergic dysregulation and an anxiety-stress burden that both respond partly to SSRIs and SNRIs.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Pandemic amplifier: COVID-19 worsened obsessive-compulsive disorder, especially contamination and washing subtypes, while post-infectious immune activation is among the mechanisms linking infection to OCD.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The gut-brain axis in OCD: microbiome and intestinal-barrier signals influence the cortico-striatal circuits of obsessive-compulsive disorder, an emerging dimension of its biology beyond serotonin.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — Organic OCD: demyelinating lesions of multiple sclerosis in frontal and basal-ganglia circuits can produce secondary obsessive-compulsive symptoms, illustrating the cortico-striatal basis of the disorder.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Neuroinflammation: elevated IL-1β and microglial activation in cortico-striatal circuits are increasingly implicated in OCD, linking immune signalling to symptom severity.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory cytokine: raised TNF-α in OCD supports an immune-mediated component to the disorder, consistent with its overlap with autoimmune and PANDAS-type presentations.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome link: NLRP3-driven IL-1β release from activated microglia is a proposed mechanism connecting innate immune activation to the neurocircuit dysfunction of OCD.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — First-line drug target: high-dose SSRIs blocking the serotonin transporter are the cornerstone of OCD pharmacotherapy, and SERT-gene variation is among the most studied genetic factors in the disorder.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Stress-axis dysregulation: altered CRH-driven HPA-axis reactivity accompanies OCD, linking chronic stress to symptom exacerbation in the cortico-striatal circuits underlying compulsions.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 and the blood-brain barrier: IL-17A from Th17 cells is implicated in the PANDAS subtype of OCD, where post-streptococcal autoimmunity and barrier disruption let anti-neuronal antibodies reach the basal ganglia.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — OCD onset and symptom severity fluctuate with reproductive events—pregnancy, postpartum, and the premenstrual phase—implicating estrogen's modulation of the serotonergic circuits that underlie the disorder and its treatment response.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Imaging shows microglial activation in the cortico-striatal circuits of OCD, and TLR4-driven innate immune signaling is a candidate mechanism linking infection and inflammation (as in PANDAS) to symptom flares.
- `connects-to` → **[μ-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Opioid signaling in the striatum shapes the sense of reward and "completeness" whose disturbance drives the need to repeat compulsions, and opioid-modulating agents have been explored in treatment-resistant OCD.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Striatal cholinergic interneurons modulate the cortico-striato-thalamo-cortical circuit central to OCD, and their dysfunction is part of the overlap between OCD and the tic disorders that often co-occur with it.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Substance P and its NK1 receptor are richly expressed in the basal-ganglia circuits implicated in OCD, a neuropeptide modulator of the striatal pathways whose dysregulation contributes to repetitive, compulsive behavior.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Neuronal nitric-oxide synthase shapes glutamatergic transmission and synaptic plasticity in the cortico-striatal circuit, and nNOS gene variants have been associated with OCD, implicating the nitrergic system in its pathophysiology.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — HPA-axis signaling through the glucocorticoid receptor (cortisol and CRH already mapped) modulates OCD symptom severity and the stress-triggered exacerbations characteristic of the disorder.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-dependent synaptic plasticity in the cortico-striatal-thalamo-cortical circuit shapes the maladaptive habit learning behind compulsions, and is implicated in rapid-acting glutamatergic treatments for OCD.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Dopamine- and glutamate-driven ERK signaling in the striatum mediates the synaptic plasticity of habit formation that underlies the repetitive compulsive behavior of OCD.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates glutamatergic synaptic plasticity in the cortico-striato-thalamo-cortical circuits implicated in OCD, and is a target of the lithium augmentation used in refractory cases.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling (with mTOR and ERK1/2 mapped) relays the BDNF-driven (mapped) neuroplasticity altered in the circuits underlying OCD.
- `connects-to` → **[ACTH](../../03-molecular/acth/README.md)** — CRH-driven pituitary ACTH release (CRH, cortisol and the glucocorticoid receptor mapped) links stress to the symptom exacerbations of obsessive-compulsive disorder.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4-MyD88 innate neuroinflammatory signaling (TLR4 mapped) is implicated in the post-infectious/autoimmune (PANDAS) forms of obsessive-compulsive disorder.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN-regulated PI3K-AKT-mTOR signaling (AKT, mTOR and GSK-3β mapped) shapes the cortico-striatal synaptic plasticity disrupted in OCD.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Striatal adenosine A2A receptors functionally oppose dopamine D2 signaling (dopamine mapped) in the cortico-striatal circuits whose dysregulation underlies OCD.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF-TrkB (NTRK) signaling shapes the cortico-striatal synaptic plasticity (BDNF already mapped) implicated in the habit-circuit dysfunction of OCD.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the neuroinflammatory tone implicated in OCD, including the autoimmune PANDAS subtype.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by activated microglia amplifies the neuroinflammation linked to the cortico-striatal dysfunction of OCD.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING in microglia contributes to the neuroinflammation implicated in OCD, including the autoimmune PANDAS subtype.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the inflammatory tone associated with the cortico-striatal circuit dysfunction of OCD.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT and PTEN already mapped) regulates neuronal plasticity and oxidative-stress handling relevant to OCD.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and oxidative-stress adaptation participates in the neurobiology of obsessive-compulsive disorder.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the innate immune activation implicated in the neuroinflammatory (including PANDAS-associated) component of obsessive-compulsive disorder.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 neuroinflammatory signaling contributes to the immune-related mechanisms proposed in obsessive-compulsive disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT and PTEN already mapped), downstream of BDNF-TrkB (BDNF and NTRK already mapped), participates in the cortico-striatal neuroplasticity implicated in obsessive-compulsive disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the neurometabolic changes associated with obsessive-compulsive disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic neurodevelopmental programming implicated in obsessive-compulsive disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal homeostasis of the cortico-striato-thalamo-cortical circuitry implicated in obsessive-compulsive disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the glutamatergic synaptic-plasticity mechanisms implicated in obsessive-compulsive disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation and PANDAS-associated immune mechanisms of obsessive-compulsive disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and neurodevelopmental interactions implicated in obsessive-compulsive disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses implicated in obsessive-compulsive disorder.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neurodevelopmental gene programs implicated in obsessive-compulsive disorder.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — PANDAS autoimmunity: paediatric acute-onset obsessive-compulsive symptoms can follow streptococcal infection, driven by IgG autoantibodies that cross-react with basal ganglia neurons, a distinct immune-mediated route into the CSTC circuitry.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histaminergic tone: histamine-H3 signalling modulates striatal dopamine, and histidine-decarboxylase mutations link the histaminergic system to Tourette syndrome and the obsessive-compulsive spectrum.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Perinatal course: obsessive-compulsive symptoms frequently first appear or worsen in pregnancy and the postpartum period, implicating progesterone and its neurosteroid metabolites in the hormonal triggering of symptom onset.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — PANDAS autoimmunity: in the paediatric autoimmune subtype, IL-2-driven T-cell responses to streptococcal infection help generate the anti-neuronal antibodies (MHC and IgG already mapped) that trigger abrupt-onset obsessive-compulsive symptoms.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Stress reactivity: central angiotensin II modulates stress and anxiety circuits and interacts with the HPA axis (cortisol already mapped), a neuroendocrine system implicated in the heightened stress that aggravates obsessive-compulsive symptoms.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex and development: obsessive-compulsive disorder often begins earlier and more often in boys, and androgens alongside estrogen (already mapped) are implicated in the sex differences and developmental timing of symptom onset.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune counter-regulation: IL-10 opposes the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) implicated in obsessive-compulsive disorder and its autoimmune PANDAS subtype (complement already mapped), part of the immune dimension of the disorder.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the low-grade neuroinflammation (IL-6 and IL-1 already mapped) modulate the cortico-striatal circuits implicated in obsessive-compulsive disorder, part of its immune-inflammatory contribution.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: heightened oxidative stress, to which xanthine oxidase contributes, is reported in obsessive-compulsive disorder, and the resulting reactive oxygen species (NLRP3 already mapped) may affect the neurons of the affected circuits.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation and PANDAS autoimmunity implicated in obsessive-compulsive disorder.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and monoamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the monoamine signalling of the circuits implicated in obsessive-compulsive disorder.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D and neuroimmunity: low vitamin D status has been reported in obsessive-compulsive disorder, and its modulation of neuroimmune and monoaminergic (serotonin already mapped) function is a proposed contributor.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation of the PANDAS/neuroimmune subtype of obsessive-compulsive disorder.
- `connects-to` → **[Generalized anxiety disorder](../generalized-anxiety-disorder/README.md)** — Anxiety-spectrum comorbidity: generalized anxiety disorder is commonly comorbid with obsessive-compulsive disorder, the two sharing the serotonergic (already mapped) treatment and the anxious-obsessional symptom overlap.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and glutamatergic modulation: synaptic zinc modulates the glutamate (already mapped)/NMDA signalling of the cortico-striatal circuit, and zinc has been trialled as an adjunct to the SSRIs in obsessive-compulsive disorder.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic-inflammatory adipokine: leptin is the adipokine of the metabolic-inflammatory milieu and the neuroinflammation (TNF and IL-6 already mapped) implicated in obsessive-compulsive disorder.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory milieu of obsessive-compulsive disorder.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the neuroinflammation (IL-1 already mapped) of obsessive-compulsive disorder.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the neuroinflammation implicated in the PANDAS (MHC and immunoglobulin already mapped) and idiopathic obsessive-compulsive disorder.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation (IL-1 and TNF already mapped) associated with obsessive-compulsive disorder.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of obsessive-compulsive disorder.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with obsessive-compulsive disorder.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammation associated with obsessive-compulsive disorder.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension reported in a subset with obsessive-compulsive disorder.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation implicated in obsessive-compulsive disorder.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Autoimmune arm: the cytotoxic T cells (perforin pathway), in the PANDAS/PANS autoimmune subset triggered by the streptococcus (already mapped), contribute to the basal-ganglia targeting of obsessive-compulsive disorder.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Peripheral innate arm: the NK cells (perforin pathway) are part of the peripheral innate-immune dysregulation reported in obsessive-compulsive disorder.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) are part of the complement activation of the PANDAS/PANS autoimmune neuroinflammation implicated in obsessive-compulsive disorder.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) basal-ganglia neuroinflammation of obsessive-compulsive disorder.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Autoimmune priming: the dendritic cells present the streptococcal (already mapped) antigen in the PANDAS/PANS subset, priming the T cells (already mapped) of the basal-ganglia autoimmunity of obsessive-compulsive disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuro-immune alarmin: TSLP, released by skin (already mapped) and gut-epithelial (already mapped) barriers during PANDAS/PANS infections, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the systemic immune activation of OCD.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin neuro-vascular axis: bradykinin, generated during streptococcal (already mapped) and complement (C3, C5, C5aR1 already mapped) activation, augments blood-brain-barrier permeability and enables the autoantibody access to the basal ganglia of obsessive-compulsive disorder.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) activation in the basal-ganglia neuroinflammation of obsessive-compulsive disorder.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM remodelling in the cortico-striatal circuit: periostin, expressed by astrocytes (already mapped) and microglia (already mapped) under neuroinflammation, modulates the extracellular matrix of the basal ganglia that is disrupted in OCD.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective cytokine: erythropoietin, via EPOR on neurons and astrocytes (already mapped), suppresses neuroinflammatory cytokines (TNF-α and IL-6 already mapped) and limits the oxidative damage in the fronto-striatal circuitry of OCD.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine coupling: prolactin, elevated by antipsychotic medications used as augmentation in OCD (serotonin and dopamine already mapped), modulates the T-cell (already mapped) immune function and amplifies the female-predominant endocrine skew of OCD.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — OCD vasopressin: vasopressin V1A receptors in the cortico-striatal circuit (brain already mapped) modulate the anxiety-driven repetitive behaviours of OCD; vasopressin interacts with oxytocin (already mapped) to co-regulate social threat processing and compulsivity.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — OCD transferrin: transferrin supports neuronal (already mapped) iron metabolism and myelin integrity in the fronto-striatal circuitry; iron deficiency via disordered transferrin amplifies the dopaminergic (already mapped) dysfunction and compulsivity of OCD.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — OCD factor-h: factor H regulates the alternative complement pathway (C5 and C5aR1 already mapped) over-activation in the neuroinflammatory basal-ganglia environment of OCD; reduced factor H activity amplifies the complement-driven microglial (already mapped) activation.

[^abramowitz-2009-ocd-review]: Abramowitz JS, Taylor S, McKay D. Obsessive-compulsive disorder. *Lancet.* 2009;374(9688):491-499. [doi:10.1016/S0140-6736(09)60240-3](https://doi.org/10.1016/S0140-6736(09)60240-3) · [PubMed 19665647](https://pubmed.ncbi.nlm.nih.gov/19665647/)
[^chamberlain-2008-ocd-neuroscience]: Chamberlain SR, Menzies L, Hampshire A, et al. Orbitofrontal dysfunction in patients with OCD and their unaffected relatives. *Science.* 2008;321(5887):421-422. [doi:10.1126/science.1154433](https://doi.org/10.1126/science.1154433) · [PubMed 18635808](https://pubmed.ncbi.nlm.nih.gov/18635808/)
[^pittenger-2017-ocd-glutamate]: Pittenger C. Glutamate and anxiety disorders. *Curr Top Behav Neurosci.* 2015;23:145-168. [doi:10.1007/7854_2014_295](https://doi.org/10.1007/7854_2014_295) · [PubMed 25091538](https://pubmed.ncbi.nlm.nih.gov/25091538/)
[^soomro-2008-ssri-ocd]: Soomro GM, Altman D, Rajagopal S, Oakley-Browne M. SSRIs versus placebo for OCD. *Cochrane Database Syst Rev.* 2008;(1):CD001765. [doi:10.1002/14651858.CD001765.pub3](https://doi.org/10.1002/14651858.CD001765.pub3) · [PubMed 18253995](https://pubmed.ncbi.nlm.nih.gov/18253995/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
