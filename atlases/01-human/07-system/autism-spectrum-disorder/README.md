---
schema: human-scale-entry/v1
id: autism-spectrum-disorder
name: Autism Spectrum Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "ASD (1-2% prevalence; 4:1 male bias) causes social communication deficits and restricted repetitive behaviors; E/I imbalance and synaptic scaffold mutations (SHANK3, NLGN3/4) are core mechanisms; ABA therapy is evidence-based; no pharmacotherapy is approved for core symptoms."
aliases: ["autism spectrum disorder", "ASD", "autism", "Asperger syndrome", "autistic disorder", "pervasive developmental disorder", "SHANK3", "NLGN3", "Fragile X", "Rett syndrome"]
sources:
  - id: maenner-2023-asd-prevalence
    type: peer-reviewed
    cite: "Maenner MJ, Warren Z, Williams AR, et al. Prevalence and characteristics of autism spectrum disorder among children aged 8 years — Autism and Developmental Disabilities Monitoring Network, 11 Sites, United States, 2020. MMWR Surveill Summ. 2023;72(2):1-14."
    doi: "10.15585/mmwr.ss7202a1"
    pmid: "36952216"
    url: "https://doi.org/10.15585/mmwr.ss7202a1"
    accessed: "2026-06-08"
  - id: lord-2020-asd-review
    type: peer-reviewed
    cite: "Lord C, Elsabbagh M, Baird G, Veenstra-Vanderweele J. Autism spectrum disorder. Lancet. 2018;392(10146):508-520."
    doi: "10.1016/S0140-6736(18)31129-2"
    pmid: "30078460"
    url: "https://doi.org/10.1016/S0140-6736(18)31129-2"
    accessed: "2026-06-08"
  - id: sanders-2012-asd-exome
    type: peer-reviewed
    cite: "Sanders SJ, Murtha MT, Gupta AR, et al. De novo mutations revealed by whole-exome sequencing are strongly associated with autism. Nature. 2012;485(7397):237-241."
    doi: "10.1038/nature10945"
    pmid: "22495306"
    url: "https://doi.org/10.1038/nature10945"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Oxytocin is reduced in subsets of ASD; OXTR methylation reduces receptor expression; intranasal OT modestly improves eye contact and social reciprocity in some RCTs; OT interventions remain experimental pending responder biomarker identification."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "E/I imbalance toward excess excitation is a core ASD mechanism; SHANK3 and NLGN3 mutations disrupt postsynaptic NMDA/AMPA scaffolding; mGluR5 hyperactivation in Fragile X drives excess dendritic protein synthesis; mGluR5 antagonists failed Phase 2 trials in FXS."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Reduced GABAergic inhibition contributes to E/I imbalance in ASD; GABA-A subunit mutations (GABRA1, GABRB3) are associated with ASD; GABA deficiency in ASD cortex may underlie sensory hypersensitivity; GABAergic circuit maturation delays are proposed as ASD endophenotype."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Syndromic ASD via mTOR hyperactivation: tuberous sclerosis (TSC1/2 LOF → mTORC1), PTEN hamartoma tumors (PTEN LOF); mTOR excess drives synaptic protein overproduction; everolimus reduces ASD severity and seizure burden in TSC; 25-35% of TSC patients have ASD."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "ASD features amygdala hyperreactivity to faces, atypical gaze via STS, reduced default mode network connectivity, and early cortical overgrowth followed by reduced long-range connectivity; atypical lateralization and local-over-global processing are consistent findings."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "AVPR1A promoter microsatellites (RS1, RS3) associate with ASD social behavior; V1aR in lateral septum mediates social recognition memory; V1aR-KO mice show impaired social memory; intranasal vasopressin is in Phase 2 trials for ASD social communication deficits."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Autism is in large part a disorder of the synapse: de novo mutations in scaffold proteins that organize the postsynaptic density tip neurons toward an excitation-inhibition imbalance, and ASD brains show early cortical neuron overgrowth then reduced long-range connectivity."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Autism and epilepsy frequently co-occur (roughly 20-30%), both reflecting cortical excitation-inhibition imbalance and often the same genes — SCN, GABA-receptor, and mTOR-pathway mutations cause both; shared E/I biology makes epilepsy one of ASD's key medical comorbidities."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Autism, bipolar disorder, and schizophrenia sit on an overlapping neurodevelopmental and genetic continuum: risk loci such as SHANK2 and the CACNA1C calcium channel are shared across all three, and bipolar disorder is a notable comorbidity in autistic people."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "Autism and ADHD are the most common neurodevelopmental comorbidity pair, co-occurring in 30-60%: they share heritability and executive-function and reward differences, DSM-5 now permits dual diagnosis, and ADHD inattention/impulsivity often complicate autistic presentations."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Tuberous sclerosis is a leading single-gene cause of syndromic autism: loss of TSC1/TSC2 disinhibits mTOR, producing cortical tubers, epilepsy and autism in up to half of patients; this links autism to the mTOR synaptic pathway and motivates mTOR-inhibitor trials."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Autism is increasingly understood as a synaptopathy: many risk genes (SHANK, neurexin/neuroligin, mTOR regulators) converge on synapse formation, pruning and the excitation/inhibition balance, so altered synaptic signaling underlies the social and sensory phenotype."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Autism and schizophrenia share neurodevelopmental origins and genetics: overlapping copy-number variants (22q11, 16p11) and synaptic genes underlie both, on a continuum of early brain miswiring—though autism presents in childhood and schizophrenia in late adolescence."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Autism and OCD share repetitive behavior but differ in drive: autistic repetitive behaviors are self-soothing and not unwanted, while OCD compulsions relieve ego-dystonic obsessions—yet the two co-occur, so telling comforting routine from distressing ritual guides care."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia are implicated in autism's altered brain wiring: as the synaptic pruners of development, dysregulated microglia may leave excess or aberrant synapses, and signs of neuroinflammation in autistic brains point to immune-neural crosstalk in early circuit formation."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Autism is linked to the gut-brain axis: many autistic people have GI symptoms and altered gut microbiomes, and microbial metabolites may influence behavior and neurodevelopment—an area of intense (if still unproven) research into diet and microbiome interventions."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes contribute to autism's altered brain wiring: beyond neurons, dysfunctional astrocytes disturb synapse formation, glutamate handling and neuroinflammation, supporting a view of autism as a disorder of brain connectivity."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Autism and anxiety disorders very frequently co-occur: a large share of autistic people have generalized anxiety, which intensifies sensory sensitivities and rigidity—so screening for and treating anxiety is central to autism care."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Elevated blood serotonin is autism's oldest biomarker: about a quarter of children with autism have platelet hyperserotonemia, and serotonin's role in early brain wiring links this neurotransmitter to the disorder's developmental origins, though its meaning stays unclear."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine circuits are implicated in autism's core features: altered mesolimbic dopamine signaling may underlie differences in social motivation and repetitive behaviors, and dopamine-blocking antipsychotics are the main drugs approved for autism-associated irritability."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Autism is a neurodevelopmental condition of the whole nervous system: altered synapse formation and excitation-inhibition balance during early brain development shape lifelong differences in perception, communication and behavior across many brain networks."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune system is woven into autism's origins: maternal infection and immune activation in pregnancy raise risk, and many autistic children show ongoing neuroinflammation with activated microglia—so immune signaling shapes the developing social brain."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF ties autism to synaptic wiring: this neurotrophin guides how synapses form and prune, and altered BDNF levels are reported in autism, fitting a model where mis-tuned synaptic growth—too many or too few connections—underlies the atypical brain development."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus is altered in autism: differences in its size and connectivity accompany the memory and spatial-learning quirks seen in the condition, and as a region of lifelong neurogenesis it links autism to how experience reshapes the developing brain."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Prenatal testosterone may bias autism risk: elevated fetal androgen exposure is one proposed factor behind the ~4:1 male predominance and the 'extreme male brain' theory, linking sex hormones in the womb to later neurodevelopment."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "The placenta is a route to autism risk: maternal immune activation, infection and exposures (like valproate) acting through the placenta during pregnancy raise ASD likelihood, pointing to a prenatal origin for much of the condition."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc helps build the synapses disrupted in autism: SHANK scaffold proteins—mutated in some autism—are zinc-dependent, and zinc concentrates at synapses, so disturbed zinc signaling is one link between trace-metal biology and synaptic ASD genes."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Autism reshapes the brain's wiring insulation: studies find altered myelin and oligodendrocyte differences underlying the atypical long- and short-range connectivity, so white-matter changes accompany the synaptic biology of ASD."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Maternal IL-6 links infection to autism risk: when the mother's immune system activates in pregnancy, IL-6 crossing to the fetal brain perturbs development in animal models, a leading mechanism behind the maternal-immune-activation hypothesis of ASD."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium tunes the glutamate signaling disturbed in autism: it blocks the NMDA receptor at rest, so altered magnesium handling can shift the excitation-inhibition balance that many ASD genes already push toward over-excitation."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Autism converges on calcium signaling: several of the strongest risk genes encode calcium channels (like CACNA1C) or calcium-handling proteins, so altered calcium flow into neurons is a recurring thread through the disorder's genetics."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Autism reaches into the gut: GI symptoms are far more common in ASD, and through the gut-brain axis the large intestine's microbes and signals can influence behavior, tying digestive health to the condition."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Autism often runs short on ATP: a subset of children show mitochondrial dysfunction that limits the cell's energy currency, and the brain's high energy demand may make developing neurons especially sensitive to this shortfall."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Brain imaging probes autism: MRI shows early brain overgrowth and altered connectivity, and fMRI photons map how differently social and sensory networks light up, sought as objective markers."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency is common in autism: restrictive eating lowers stores, and because iron is needed to make dopamine, low iron may worsen attention, sleep and restless behaviors."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Autism shows in the eyes: reduced eye contact and atypical gaze are early signs, and eye-tracking is studied as an objective measure of the social differences that define the condition."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy hints at autism's altered wiring: studies find changes in dendritic spine density and synapse structure, the fine connections between neurons that mTOR and other autism genes help build and prune."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D in pregnancy may shape the risk: low maternal vitamin D during fetal brain development is associated with a higher chance of autism, fitting the vitamin's role in neurodevelopment and immune regulation."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Autism and the heart often travel together: children with congenital heart disease have elevated rates of autism, the shared early developmental disruption and surgical-stress exposure linking the two conditions."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Sleep is a near-universal struggle in autism: disrupted melatonin rhythms leave many autistic children unable to fall or stay asleep, and melatonin is the first-line treatment, easing both the insomnia and the daytime behavior it worsens."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The gut is a frequent trouble spot: autistic children have high rates of reflux, constipation, and selective eating, the GI symptoms feeding into the gut-brain axis already implicated in the condition."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The mother's thyroid shapes the risk: adequate maternal thyroid hormone is critical for fetal brain development, and maternal hypothyroxinemia in pregnancy is a recognized risk factor for autism in the child."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "A mother's antibodies can target the fetal brain: in maternal-autoantibody-related autism, IgG against fetal brain proteins crosses the placenta and disturbs neurodevelopment, one immune route into the condition's many causes."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune genes sit among the risk loci: MHC/HLA variants and maternal immune activation in pregnancy are tied to autism, linking the brain's wiring to the same antigen-presenting machinery that runs immunity."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Much of the risk is set before birth: advanced parental age, prenatal valproate, and maternal immune activation shape autism risk, and the striking male predominance points to sex-hormone influences on the developing brain."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Maternal IL-17A is a molecular bridge from infection to autism: in maternal immune activation models, this Th17 cytokine crosses into the fetal brain and alters cortical development, producing autism-like behavior in the offspring."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Brain mast cells may stoke the neuroinflammation: they sit near the blood-brain barrier and release mediators that activate microglia, and the high rate of allergy and mast-cell activation in autism hints at a role in some cases."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "A single-gene road to autism: neurofibromatosis type 1 carries a high rate of autism features, one of the RAS-MAPK 'RASopathies' that, like tuberous sclerosis, show how one mutation can derail the social brain."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The body's cannabis system tunes the social brain: endocannabinoid signaling shapes the synaptic plasticity and reward responses to social cues, and its dysregulation in autism is the rationale behind cannabidiol trials for the condition."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "An immune imbalance shadows it: reduced regulatory T cells and a tilt toward inflammation accompany autism, fitting the maternal-immune-activation models in which prenatal inflammation reshapes brain development."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep rarely comes easy: insomnia and disrupted sleep architecture are strikingly common in autism, tied to altered melatonin rhythms, and poor sleep in turn worsens daytime behavior and core symptoms."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Neuroinflammation runs through NF-κB: maternal immune activation and microglial activation in autism converge on NF-κB-driven cytokine signaling, part of the inflammatory thread woven through its neurodevelopment."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "One gene ties autism to overgrowth: PTEN mutations cause a macrocephaly-autism syndrome, and because PTEN restrains the mTOR pathway, its loss drives the synaptic overgrowth linking this monogenic cause to the broader spectrum."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The gut speaks loudly in autism: constipation, diarrhea and abdominal pain are far more common than in peers, a GI burden tied to the gut-brain axis and to the altered microbiome that accompanies the condition."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Social difficulty breeds social fear: social anxiety is among the most common comorbidities in autism, as repeated misread interactions and rejection foster intense anticipatory fear of social situations."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Isolation and burnout darken mood: depression is markedly elevated in autistic people, driven by loneliness, the exhaustion of masking, and the cumulative toll of navigating an unaccommodating world."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Several forces tip toward weight gain: restricted food preferences, reduced physical activity, and the appetite-stimulating antipsychotics often prescribed in autism combine to raise the rate of obesity."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Antipsychotics and obesity raise the risk: the metabolic side effects of antipsychotics prescribed for irritability in autism, on top of its associated obesity and inactivity, elevate the rate of type 2 diabetes."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Selective eating starves the body of iron: the rigid, narrow food preferences and avoidant-restrictive eating common in autism frequently lead to inadequate iron intake and iron-deficiency anemia."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "Rigidity and sensory aversion feed eating disorders: autism markedly raises the risk of restrictive eating disorders like anorexia, where its inflexibility and sensory sensitivities shape and entrench the food restriction."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Movement and coordination are commonly affected: autism is frequently accompanied by hypotonia, motor dyspraxia and clumsiness, and an over-representation of joint hypermobility and connective-tissue laxity."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It shares an allergic, immune skin link: atopic dermatitis and eczema are more common in autism, reflecting the immune dysregulation tied to the condition, and self-injury can further damage the skin."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "A world of adversity raises trauma risk: autistic people face high rates of bullying, abuse and overwhelming environments, giving elevated rates of post-traumatic stress that camouflaging can hide."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its autonomic balance differs: autism is associated with altered heart-rate variability and autonomic reactivity, and several ASD-linked genetic syndromes include congenital heart disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its medications reshape metabolism: antipsychotics like risperidone and aripiprazole, used for autism-related irritability, commonly cause weight gain, hyperprolactinaemia and metabolic syndrome."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Continence comes late: nocturnal enuresis and delayed toilet training are more common in autistic children, and some ASD-associated genetic syndromes carry renal and urinary-tract anomalies."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: connects-to
    note: "Maternal infection raises the odds: severe maternal influenza and prolonged fever in pregnancy are linked to higher autism risk, an example of the maternal-immune-activation hypothesis of neurodevelopment."
  - target: 02-pathogen/01-viruses/measles-virus
    relation: connects-to
    note: "The MMR-autism scare was fraudulent: the claim linking measles vaccination to autism was retracted and disproven, and large studies show no association — vaccination does not cause autism."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet draws research interest: omega-3 supplementation has been trialled for autism symptoms, but the evidence remains weak and it is not an established treatment."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "A congenital infection that raises risk: maternal cytomegalovirus and other congenital infections are established environmental risk factors for autism, acting through fetal neuroinflammation."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "A trace-metal imbalance is described: altered copper-to-zinc ratios are reported in autism, with relative copper excess and zinc deficiency linked to oxidative stress in the developing brain."
  - target: 03-medicine/03-food/sulforaphane
    relation: connects-to
    note: "A food compound with a trial behind it: a randomised trial found broccoli-derived sulforaphane modestly improved behaviour in autism, proposed to act by reducing oxidative stress and inflammation."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Syndromic autism has druggable pathways: in TSC-, PTEN- and fragile-X-related autism the mTOR and synaptic-signalling pathways are dysregulated, making mTOR inhibitors and other targeted agents candidates for the syndromic forms."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Connectivity is altered: autism shows atypical long-range underconnectivity and local overconnectivity, with white-matter and axonal-transport differences shaping how distant brain regions communicate."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The gut-brain axis is implicated: many autistic people have GI symptoms and altered intestinal-epithelial barrier function, part of the microbiome-gut-brain signalling increasingly linked to autism."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "A PTEN route to autism: germline PTEN loss causes macrocephaly with autism spectrum disorder, linking ASD to Cowden syndrome's PTEN-hamartoma-tumour predisposition—one gene bridging neurodevelopment and cancer."
  - target: 01-human/07-system/noonan-syndrome
    relation: connects-to
    note: "RASopathies raise autism traits: like other RAS-MAPK developmental syndromes, Noonan syndrome carries an increased rate of autism spectrum features, implicating RAS signalling in social-cognitive development."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "When an ion channel links heart and brain: Timothy syndrome's CACNA1C calcium-channel mutation causes long-QT arrhythmia with autism, and antipsychotics used in ASD prolong the QT, tying ASD to cardiac conduction."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Maternal immune activation: prenatal infection and maternal autoantibodies—made by germinal-centre B cells—are linked to autism risk, implicating the maternal adaptive immune response in fetal brain development."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Pervasive sleep disruption: autism features high rates of insomnia and circadian/REM sleep abnormalities that overlap the sleep-wake dysregulation of narcolepsy, and melatonin helps the disturbed sleep in both."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Lower bone density: restricted diets, reduced weight-bearing activity and SSRI use leave many autistic individuals with reduced cortical-bone density and a higher fracture risk."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Maternal immune activation and disrupted care: maternal COVID-19 (like influenza) joins the infections studied for neurodevelopmental risk in offspring, while the pandemic disrupted autism diagnosis and therapy services."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "An overlapping differential: autism and borderline personality disorder share emotional dysregulation and social difficulty and are frequently confused, especially in autistic women diagnosed late."
  - target: 01-human/07-system/internet-gaming-disorder
    relation: connects-to
    note: "Screens as refuge and risk: autistic individuals have markedly higher rates of problematic internet and gaming use, the predictable, controllable digital world offering both comfort and a route to dependence."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Maternal immune activation: IL-1β is a key cytokine of the maternal immune activation linked to autism risk, and elevated IL-1β features in the neuroinflammation seen in autistic brains."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Neuroimmune signature: raised TNF-α is among the inflammatory markers reported in autism, reflecting the microglial activation and immune dysregulation implicated in its neurodevelopment."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Synaptic growth factor: IGF-1 promotes synapse maturation and has been trialled in autism-related disorders such as Rett and Phelan-McDermid syndromes for its neurodevelopmental effects."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "Hyperserotonemia: elevated whole-blood serotonin tied to serotonin-transporter function is the oldest and most replicated biomarker in autism, implicating serotonergic development in the disorder."
  - target: 01-human/03-molecular/tsc1-tsc2
    relation: connects-to
    note: "mTOR-pathway autism: loss of the TSC1-TSC2 complex in tuberous sclerosis unleashes mTOR and causes a high rate of autism, a defining example of the synaptic-overgrowth mechanism in syndromic ASD."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "Chromatin-remodeling risk: de novo mutations in chromatin regulators like ARID1A are a leading genetic class in autism, disrupting the gene-expression programmes that build neural circuits."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Maternal immune activation: gestational infection signalling through TLR4 raises offspring autism risk in human studies and animal models, the innate-immune trigger of the maternal-immune-activation hypothesis of ASD."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Convergent signalling node: GSK-3β is dysregulated in Fragile X syndrome and other syndromic autism, a kinase governing synaptic plasticity whose inhibition (e.g. by lithium) rescues phenotypes in ASD models."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Synaptic neurotrophin signalling: BDNF acting through its TrkB receptor shapes the synapse formation and plasticity disrupted in autism, linking neurotrophin signalling to the connectivity differences of the disorder."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium-channel signalling: gain-of-function mutations in the L-type calcium channel CACNA1C cause Timothy syndrome with autism, and broader calcium-signalling dysregulation is a recurring theme among autism risk genes affecting synaptic activity-dependent transcription."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Synaptic pruning: complement C3 tags synapses for microglial elimination during development, and dysregulated complement-mediated pruning is implicated in the altered synaptic density and connectivity seen in autism."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Maternal immune activation: prenatal type-I-interferon responses to maternal infection raise autism risk, a key strand of the neurodevelopmental immune hypothesis linking gestational inflammation to altered fetal brain development."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PTEN-AKT-mTOR convergence: the PTEN-PI3K-AKT-mTOR pathway (PTEN, mTOR and TSC1/2 already mapped) is a convergence point of syndromic autism, where excess AKT-mTOR signalling drives the synaptic overgrowth and macrocephaly of ASD."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RASopathy MAPK: RAS-MAPK-ERK signalling, hyperactivated in the RASopathies (neurofibromatosis-1 and Noonan already mapped) that carry high autism risk, regulates the synaptic plasticity disrupted in autism spectrum disorder."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Neurodevelopmental Wnt: Wnt/β-catenin signalling, regulated by high-confidence autism genes such as CHD8, governs the neuronal proliferation and synaptic development perturbed in autism spectrum disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Syndromic mTOR axis: the PTEN-PI3K-AKT-mTOR pathway (PTEN, AKT, mTOR and TSC1-TSC2 all mapped) is dysregulated in syndromic autism, driving the synaptic-protein-synthesis imbalance underlying its phenotype."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Maternal immune activation: maternal infection signals through TLR (TLR4 mapped) and MyD88, and the resulting maternal IL-6/IL-17 (mapped) shapes fetal brain development, a major environmental autism-risk pathway."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Synaptic plasticity: calcium-calcineurin-NFAT signalling regulates activity-dependent synaptic plasticity, a process disrupted in the excitatory/inhibitory imbalance of autism spectrum disorder."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Maternal IL-6 acting through STAT3 (IL-6 mapped) is a central mediator of the maternal-immune-activation pathway linked to autism risk in offspring."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-driven JAK-STAT signalling transduces the maternal and neuroinflammatory cytokine milieu implicated in the neurodevelopmental alterations of autism."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 marks the reactive-microglia state reported in autism brains, contributing to the neuroinflammatory component of the disorder."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling transduces the maternal-immune-activation interferon exposure epidemiologically linked to autism spectrum disorder."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the innate neuroinflammatory activation implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the neurodevelopmental and synaptic processes whose perturbation is implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of the PTEN-PI3K-AKT-mTOR axis (PTEN, AKT, PIK3CA, mTOR, and TSC1-TSC2 already mapped) regulates neuronal growth and synaptic programs disrupted in autism spectrum disorder."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the maternal-immune-activation and neuroinflammatory signaling implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and oxidative-stress responses are implicated in the neurodevelopmental pathophysiology of autism spectrum disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, in balance with the mTOR pathway (mTOR already mapped), regulates the neuronal metabolic and autophagy homeostasis implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of the neurodevelopmental gene expression disrupted in autism spectrum disorder."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression participates in the chromatin regulation of the neurodevelopmental programs implicated in autism spectrum disorder (ARID1A already mapped)."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the synaptic pruning and dendritic-spine homeostasis (mTOR already mapped) implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (FYN) kinase signaling participates in the NMDA-receptor and synaptic signaling implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the maternal-immune-activation and neuroinflammation implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuronal migration and neurodevelopmental processes implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial synaptic pruning and neuroinflammation implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement signaling, alongside complement-mediated synaptic pruning (complement-C3 already mapped), participates in the synaptic remodeling implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the synaptic and neuroimmune modulation implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microglial activation and neuroinflammation implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2 (MCP-1) chemokine signaling participates in the neuroinflammatory and microglial responses (including maternal immune activation) implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Female protective effect: autism is diagnosed about four times more often in males, and estrogen's neuroprotective and synaptic effects are proposed to raise the mutational threshold in females (fetal testosterone already mapped), contributing to the sex bias."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative stress: children with autism show evidence of glutathione depletion and oxidative stress, and the NRF2 antioxidant response modulated here is implicated in the redox imbalance affecting neurodevelopment."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitrosative signalling: nitric oxide is both a synaptic messenger shaping the excitatory-inhibitory balance and a source of nitrosative stress, and altered NO signalling is reported in autism spectrum disorder."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Maternal immune activation: shifts in the type-2 cytokine IL-4 balance during maternal immune activation, alongside the IL-6 and IL-17 (already mapped) implicated in animal models, are part of the prenatal immune milieu linked to autism risk."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Immune dysregulation: altered IL-2 and regulatory-T-cell function are reported in autism and in the mothers of affected children, part of the immune dysregulation that accompanies a subset of the disorder."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid modulation: progesterone-derived neurosteroids modulate GABAergic (already mapped) signalling in the developing brain, and prenatal sex-steroid exposure alongside estrogen (already mapped) is implicated in the male preponderance of autism."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the maternal immune activation and the microglial (already mapped) cyclooxygenase pathway (IL-6 and IL-17 already mapped) are implicated in the altered neurodevelopment of a subset of autism."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune counter-regulation: IL-10 opposes the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) of the maternal immune activation and the immune dysregulation reported in a subset of autism, part of its immune dimension."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: mitochondrial dysfunction and heightened oxidative stress, to which xanthine oxidase contributes, are reported in autism (NRF2 already mapped), and the resulting reactive oxygen species may affect the developing neurons (already mapped)."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Maternal immune activation: IL-13, with IL-4 (already mapped), is part of the type-2 response, and the maternal cytokine milieu (IL-6 and IL-17 already mapped) during pregnancy is implicated in the maternal-immune-activation model of autism."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histaminergic neurotransmission: histamine acting on H3 receptors modulates the neurotransmission (dopamine and serotonin already mapped) and arousal implicated in autism, and H3 ligands have been explored for its cognitive and behavioural features."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine and neurodevelopment: leptin influences neurodevelopment and is reported to be altered in autism, part of the metabolic-neurodevelopmental dimension of the disorder alongside the mTOR (already mapped) signalling."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Cholinergic neurotransmission: the cholinergic (nicotinic and muscarinic) system, implicated in the attention and social cognition (dopamine and serotonin already mapped) of autism, is a focus of the neurotransmitter research into the disorder."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine crosstalk: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-neurodevelopmental crosstalk reported altered in autism spectrum disorder."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine inflammation: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the metabolic and neuroinflammatory (IL-6 already mapped) dimension of autism spectrum disorder."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Neuronal connectivity: the altered neuronal migration, synaptogenesis (mTOR and PTEN already mapped) and the excitatory/inhibitory (glutamate and GABA already mapped) balance of the neurons underlie autism spectrum disorder."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "ADHD comorbidity: attention-deficit/hyperactivity disorder is highly comorbid with autism spectrum disorder, the two sharing the genetic and the neurodevelopmental (dopamine already mapped) overlap."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Gut-brain axis: the altered gut microbiome and the gut-brain (serotonin already mapped) signalling are implicated in the GI symptoms and the behaviour of autism spectrum disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 maternal-immune activation: the IFN-γ of the T cells is the type-II interferon arm of the maternal immune activation (IL-6 and IL-17 already mapped) implicated in the neurodevelopment of autism spectrum disorder."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune dysregulation and the maternal immune activation of autism spectrum disorder."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation and the atopy comorbidity of autism spectrum disorder."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Maternal Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm central to the maternal immune activation implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/atopy arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension and the atopy comorbidity of autism spectrum disorder."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells, including the maternal Th17 (IL-17 already mapped), are the source of the cytokines of the immune dysregulation and the maternal immune activation of autism spectrum disorder."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive neuroimmune arm: the cytotoxic T cells (perforin pathway) of the CNS-border compartments are part of the adaptive-immune contribution to the neuroinflammation implicated in autism spectrum disorder."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Maternal/innate NK: the NK cells (perforin pathway), including the maternal NK dysregulation of the maternal immune activation, are part of the innate-immune dimension of autism spectrum disorder."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the microglial (already mapped) activation and the complement-mediated synaptic pruning implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-mediated synaptic pruning implicated in autism spectrum disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway (C1q-initiated) implicated in the aberrant synaptic pruning of autism spectrum disorder."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Neuroimmune interface: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the maternal-immune-activation and neuroinflammation of autism spectrum disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-neuroimmune axis: TSLP, from skin (already mapped) and gut (already mapped) barriers, primes dendritic cells (already mapped) and mast cells (already mapped) and amplifies the Th2/Treg (already mapped) imbalance of the maternal-immune-activation of ASD."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-neuroinflammation axis: bradykinin, via the B2R on CNS microglia (already mapped) and neurons (already mapped), amplifies the neuroinflammation and the BBB permeability contributing to the immune-activation dimension of autism spectrum disorder."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective EPO: erythropoietin signals through EpoR on neurons (already mapped) and oligodendrocytes (already mapped), supporting the myelination and the synaptic plasticity (already mapped) implicated in the neurodevelopmental dimension of autism spectrum disorder."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Synapse ECM scaffold: periostin, expressed by astrocytes (already mapped) in the synaptic extracellular matrix, modulates the perineuronal nets that regulate synaptic pruning (microglia already mapped) and the excitatory/inhibitory balance of autism spectrum disorder."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Neuroimmune developmental axis: prolactin, acting via PRLR on microglia (already mapped) and astrocytes (already mapped), modulates the neuroinflammatory cytokine milieu (TNF-α and IL-6 already mapped) and may influence the sex-differential prevalence of autism spectrum disorder."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant neurodevelopment: selenium, incorporated into selenoproteins (thioredoxin reductase and GPx), scavenges ROS in developing neurons (already mapped) and supports the glutathione (already mapped) redox balance disrupted in the oxidative stress hypothesis of ASD."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "ASD iodine: iodine, via thyroid (already mapped) hormone synthesis, supports myelination and synapse (already mapped) maturation critical in ASD; iodine deficiency amplifies IL-6 (already mapped) and mTOR (already mapped) neurodevelopmental disruption of ASD."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "ASD sodium: sodium, via neuronal Na+ channels, maintains glutamate (already mapped)/GABA (already mapped) excitatory-inhibitory balance; sodium dysregulation amplifies NF-κB (already mapped) neuroinflammation and synapse (already mapped) dysfunction of ASD."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "ASD transferrin: transferrin supplies iron (already mapped) to neurons (already mapped) and oligodendrocytes (already mapped) for myelination; transferrin deficiency amplifies NF-κB (already mapped) neuroinflammation and iron-deficiency-anemia (already mapped) of ASD."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "ASD potassium: potassium channels regulate GABA (already mapped) and glutamate (already mapped) excitatory-inhibitory balance at synapses (already mapped); channel dysfunction amplifies NF-κB (already mapped) neuroinflammation and neurodevelopmental disruption of ASD."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "ASD phosphorus: phosphorus, as phospholipid and ATP, is essential for synapse (already mapped) integrity and neuronal (neuron already mapped) energy; phosphorus dysregulation impairs mTOR (already mapped) anabolic signalling and the synaptic pruning disrupted in ASD."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "ASD sulfur: glutathione (sulfur-containing) is depleted in ASD; sulfur deficiency impairs ROS quenching in neurons (already mapped) and astrocytes (already mapped), worsening oxidative stress that amplifies NF-κB (already mapped) and mTOR (already mapped) disruption."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "ASD chloride: chloride homeostasis via GABA(A) and KCC2 on neurons (already mapped) governs inhibitory tone; chloride dysregulation converts GABA to excitatory, amplifying mTOR (already mapped) and NF-κB (already mapped) hyperexcitability and the E/I imbalance of ASD."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "ASD nitrogen: nitric oxide (NO, nitrogen-derived) in neurons (already mapped) and microglia (already mapped) amplifies neuroinflammation; NO excess upregulates NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) dysregulation of ASD."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "ASD oxygen: mitochondrial oxygen metabolism in neurons (already mapped) and astrocytes (already mapped) generates ROS; ROS excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) dysregulation, worsening BDNF (already mapped) deficits in ASD."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "ASD carbon: carbon-backbone metabolites in neurons (already mapped) and astrocytes (already mapped) fuel acetyl-CoA and mTOR (already mapped) anabolic signalling; carbon metabolic imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade in ASD."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "norepinephrine from neurons (already mapped) modulates arousal and prefrontal attention; norepinephrine deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) and oxytocin (already mapped) circuit disruption in autism spectrum disorder."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF from neurons (already mapped) and astrocytes (already mapped) sustains brain (already mapped) vascular development; VEGF excess amplifies NF-κB (already mapped) and mTOR (already mapped) and IL-6 (already mapped) and IGF-1 (already mapped) neurodevelopmental cascade in ASD."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 on microglia (already mapped) and neurons (already mapped) limits brain (already mapped) neuroinflammation; PD-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and IFN-γ (already mapped) and TNF-α (already mapped) neuroinflammatory cascade in ASD."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "ASD hydrogen: hydrogen via ROS balance in neurons (already mapped) and microglia (already mapped) modulates neuroimmune oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory cascade in ASD."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "ASD glp-1: GLP-1 on neurons (already mapped) and astrocytes (already mapped) modulates synaptic metabolism; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory connectivity disruption in ASD."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "ASD angiotensin-ii: angiotensin II on astrocytes (already mapped) and microglia (already mapped) modulates cerebrovascular tone; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroimmune dysregulation in ASD."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "ASD rankl: RANKL in microglia (already mapped) and astrocytes (already mapped) modulates neuroimmune skewing; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory connectivity disruption in ASD."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "ASD fibronectin: fibronectin in astrocytes (already mapped) and neurons (already mapped) promotes ECM remodelling at synapses; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory cascade in ASD."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "ASD notch: notch signalling in neurons (already mapped) and astrocytes (already mapped) regulates synaptic development; notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) connectivity disruption in ASD."
---

# Autism Spectrum Disorder

## Overview

**Autism spectrum disorder (ASD)** is a neurodevelopmental condition characterized by deficits in **social communication and interaction** combined with **restricted, repetitive behaviors and sensory differences**, with symptoms present from early childhood. ASD is not a single disease but a spectrum of heterogeneous conditions sharing these core features — ranging from individuals with profound intellectual disability and minimal speech to those with high cognitive ability and typical language (previously termed "Asperger syndrome" in DSM-IV; now unified under ASD in DSM-5).

ASD affects approximately **1 in 44 children** in the US (2020 CDC data) — about 2% of the population [^maenner-2023-asd-prevalence] — making it one of the most prevalent neurodevelopmental conditions. The **4:1 male predominance** is genuine but the female "camouflage" phenomenon (better social masking) contributes to under-diagnosis in girls; true sex ratio may be closer to 3:1. Sibling recurrence risk is 10–20×, and monozygotic twin concordance is ~70–90%, confirming strong heritability.

The dramatic rise in ASD prevalence from ~0.05% in the 1970s to ~2% today primarily reflects **expanded diagnostic criteria** (DSM-III → DSM-5 broadening), greater awareness, and diagnostic substitution (children previously labeled with intellectual disability or language delay). True biological incidence increase may also contribute to a modest degree (advanced paternal age, prenatal environmental factors).

## Structure

### DSM-5 criteria

**Criterion A — Persistent deficits in social communication and social interaction** across multiple contexts (all three required):
1. Deficits in social-emotional reciprocity (reduced social initiation, failure to respond to social bids, absent back-and-forth conversation)
2. Deficits in nonverbal communicative behaviors (poor eye contact, reduced facial expression, atypical gesturing, absent joint attention)
3. Deficits in developing, maintaining, and understanding relationships (difficulty with make-believe play, preference for rules over flexible social interaction, absent interest in peers)

**Criterion B — Restricted, repetitive behaviors** (≥2 of 4):
1. Stereotyped/repetitive motor movements, use of objects, or speech (echolalia, hand flapping, lining up objects)
2. Insistence on sameness, inflexible adherence to routines, ritualized patterns
3. Restricted, fixated interests that are abnormal in intensity or focus
4. Hyper- or hyporeactivity to sensory input (indifference to pain/temperature, adverse response to specific sounds/textures, visual fascination)

**Severity levels (1–3):** Based on amount of support required for social communication and restricted/repetitive behaviors; Level 3 ("requiring very substantial support") is most severe.

**Specifiers:** With/without intellectual impairment; with/without language impairment; associated with genetic/medical condition; associated with catatonia.

### Syndromic vs. idiopathic ASD

**Syndromic ASD** (~25% of cases): ASD features secondary to a known genetic disorder:

| Syndrome | Gene/Locus | Mechanism | ASD Prevalence |
|:---|:---|:---|:---|
| **Fragile X syndrome** | FMR1 (CGG triplet repeat expansion, >200 repeats → methylation → silencing) | Loss of FMRP → excess mGluR5-driven dendritic protein synthesis | 30% of FXS males |
| **Tuberous sclerosis complex (TSC)** | TSC1/TSC2 LOF → mTORC1 hyperactivation | Cortical tubers, heterotopia; synaptic protein excess | 25–50% of TSC |
| **Rett syndrome** | MECP2 LOF (X-linked, almost exclusively females) | Impaired neuronal gene silencing; progressive neurodegeneration | ~75% of Rett |
| **Angelman syndrome** | UBE3A loss (maternal 15q11-q13 imprinting) | Reduced ubiquitin E3 ligase → synaptic protein accumulation | ~50% of AS |
| **PTEN hamartoma** | PTEN LOF → mTOR hyperactivation | Macrocephaly, intellectual disability | ~20% of macrocephalic ASD |
| **22q11.2 deletion** | TBX1, DGCR8, others | Haploinsufficiency of multiple neurodevelopmental genes | ~50% of 22q11.2DS |

**Idiopathic ASD** (~75%): Complex genetic architecture:
- Heritability: ~70–90% (twin studies); polygenic risk from hundreds of common variants + rare de novo mutations
- **De novo mutations**: Among the strongest ASD risk factors; detected in ~10–15% of sporadic ASD vs. <1% of controls [^sanders-2012-asd-exome]; enriched in genes encoding synaptic proteins
- Key ASD gene categories: **Synaptic scaffold proteins** (SHANK1/2/3, NRXN1, NLGN3/4X), **chromatin regulators** (CHD8 — most commonly mutated ASD gene; ARID1B; KDM5C), **RNA processing** (FMR1, CNTNAP2), **mTOR pathway** (TSC1/2, PTEN)
- Major CNVs: 16p11.2 deletion (most common ASD CNV; also found in schizophrenia); 15q11-q13 duplication; 1q21.1 deletion/duplication

### Neurobiology of ASD

**Excitation-inhibition (E/I) imbalance hypothesis:**
The dominant neurobiological framework proposes that ASD reflects excess cortical excitation relative to inhibition — or, in some cases, altered E/I balance in specific circuits:
- SHANK3, NLGN3, NRXN1 mutations → impaired postsynaptic density organization → reduced NMDA receptor clustering → compensatory AMPA receptor upregulation → E/I shift
- Parvalbumin (PV) interneuron deficits observed in postmortem ASD cortex → reduced GABAergic inhibitory tone → sensory hypersensitivity
- However, the direction of E/I imbalance is circuit-specific: some circuits show hyperexcitability; others (especially PFC) may show hypoexcitability

**Synaptic scaffold proteins:**
- **SHANK proteins** (SHANK1/2/3) are master scaffolds at the postsynaptic density (PSD), anchoring NMDA receptors, AMPA receptors, mGluRs, and Homer proteins. SHANK3 haploinsufficiency causes ASD with severe social deficits in mice and humans (Phelan-McDermid syndrome — 22q13.3 deletion)
- **Neuroligins** (NLGN3/4X): trans-synaptic adhesion molecules that organize the PSD by binding presynaptic neurexins. NLGN3 R451C knock-in mice show enhanced inhibitory transmission (paradoxical) + social deficits. NLGN4X LOF associated with ASD + intellectual disability
- **Neurexins** (NRXN1–3): presynaptic organizers that match NLGN across the synaptic cleft; deletions are among the highest-penetrance ASD CNVs

**Cortical development:**
- ASD brains show **cortical overgrowth** at 12–24 months (expanded total brain volume, especially frontal lobe) followed by **reduced long-range white matter connectivity** in adolescence
- Transient cortical overgrowth: driven by excess early neurogenesis (Marchetto 2017; organoid models show ASD iPSC-derived cortical organoids produce excess neurons via premature cell cycle exit)
- **Local-over-global processing** bias: ASD cognition shows superior detection of local features (Embedded Figures Test, block design) with reduced global gestalt processing — consistent with restricted local cortical connectivity

## Function

### Social brain network in ASD

The neural basis of ASD social deficits involves dysfunction of the **social brain network**:

| Region | Function in neurotypicals | ASD alteration |
|:---|:---|:---|
| **Amygdala** | Encodes social salience; gaze direction; emotional facial expression | Hyperreactive to faces; rapid habituation failure; inverse correlation with clinical severity |
| **Superior temporal sulcus (STS)** | Biological motion; voice recognition; joint attention | Reduced activation to social stimuli; atypical functional connectivity with amygdala |
| **Fusiform face area (FFA)** | Expert face recognition | Hypoactivation in ASD; atypical processing of eyes |
| **Inferior frontal gyrus / Broca's area** | Mirror neuron system; language; imitation | Reduced activation during observation of intentional actions |
| **mPFC / vmPFC** | Theory of Mind; mentalizing; social reward | Reduced activation during false belief tasks; impaired mentalizing network |
| **Anterior insula** | Interoception; social pain; empathy | Atypical activation; altered interoceptive awareness |

**Default mode network (DMN) in ASD:** Neurotypical brains show DMN suppression during attention-demanding tasks. ASD shows reduced task-induced DMN suppression AND reduced resting-state connectivity within the DMN — reflected in disrupted self-referential processing and mentalizing.

**Theory of Mind:** The capacity to attribute mental states to others ("mentalizing") is consistently reduced in ASD across ToM tasks (Sally-Anne false belief, Faux Pas test, Reading the Mind in the Eyes). The neural substrate is the mentalizing network (mPFC, TPJ, posterior STS), which shows reduced activation in ASD during implicit social inference tasks.

## Pathology

### Risk factors and diagnosis

**Prenatal/postnatal risk factors:**
- Advanced paternal age (>40 years) — de novo mutation rate increases 2-fold
- Advanced maternal age (>35) — independent of paternal age
- Prenatal exposure to valproate (ASD risk 10–15× in offspring of mothers treated for epilepsy in pregnancy)
- Preterm birth (<26 weeks): ~20-fold elevated ASD risk
- Maternal immune activation during pregnancy (gestational inflammation) — maternal cytokines cross placenta; preclinical evidence strong, human epidemiology mixed
- NO convincing evidence for childhood vaccination (MMR) — multiple large RCTs and cohort studies have comprehensively excluded this hypothesis

**Diagnostic tools:**
- **ADOS-2** (Autism Diagnostic Observation Schedule, 2nd edition): gold-standard observational assessment; standardized activities that elicit social, communicative, and play behaviors
- **ADI-R** (Autism Diagnostic Interview-Revised): caregiver interview covering early development and current symptoms
- **CARS-2** and **Childhood Autism Rating Scale** for dimensional severity rating
- First symptoms typically apparent before age 3; median age of diagnosis in US is ~4 years (later in girls and less affected individuals)

### Treatment and management

**Behavioral/educational interventions:**
- **Applied Behavior Analysis (ABA)**: Most evidence-based intervention; intensive (20–40 h/week) behavioral modification using positive reinforcement; greatest gains in adaptive behavior, language, and cognition when started early (before age 5); Level 1 evidence for improving functional outcomes
- **Speech-language therapy**: Augmentative and alternative communication (AAC) for minimally verbal individuals; social pragmatics training for verbal ASD
- **Occupational therapy**: Sensory integration; fine motor skills; activities of daily living
- **Social skills groups**: Evidence-based for adolescents/adults with higher-functioning ASD; PEERS program (Program for the Education and Enrichment of Relational Skills) has robust RCT evidence
- **Pivotal Response Treatment (PRT)**: Naturalistic ABA-based approach; targets "pivotal" behaviors (motivation, initiation) that have broad developmental impact

**Pharmacotherapy (note: no drug approved for ASD's core social/communication symptoms):**

| Drug | Target | Indication in ASD | Evidence |
|:---|:---|:---|:---|
| Risperidone | D2/5-HT2A antagonist | Irritability, aggression, self-injurious behavior | FDA-approved (6–17 years) |
| Aripiprazole | D2 partial agonist | Irritability | FDA-approved (6–17 years) |
| SSRIs (fluoxetine, sertraline) | SERT inhibitor | Repetitive behaviors, anxiety, OCD features | Mixed evidence; generally modest benefit |
| Melatonin | MT1/MT2 agonist | Sleep disturbances (common in 50–80% of ASD) | Consistent evidence for sleep onset |
| Oxytocin (intranasal) | OTR agonist | Social communication | Phase 2 evidence mixed; not FDA-approved |
| Everolimus | mTORC1 inhibitor | Seizures + ASD in TSC | Reduces TSC seizures; modest ASD effects |
| Bumetanide | NKCC1 blocker (chloride co-transporter) | E/I balance correction (GABA depolarizing → hyperpolarizing shift) | Phase 2 evidence; not approved; EU phase 3 failed 2021 |

**Emerging/research therapies:**
- **CRISPR correction** of SHANK3 mutations in iPSC-derived neurons (preclinical)
- **Gene therapy for Rett syndrome:** MECP2 gene replacement via AAV9 (Phase 1/2 REVEAL trial: significant improvement in Rett symptoms)
- **mGluR5 modulators:** Arbaclofen (GABA-B agonist) for social deficit in Fragile X — failed Phase 3 but responders with certain genotypes identified
- **IGF-1 (mecasermin)** for Phelan-McDermid (SHANK3 deletion): Phase 2 showed improved socialization and expressive language; Phase 3 ongoing

## Connections

- `connects-to` → **[Oxytocin](../../../03-molecular/oxytocin/README.md)** — oxytocin is reduced in subsets of ASD; OXTR methylation reduces receptor expression; intranasal OT modestly improves eye contact and social reciprocity in some RCTs; OT interventions remain experimental pending responder biomarker identification (OXTR genotype, baseline OT level).

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — E/I imbalance toward excess excitation is a core ASD mechanism; SHANK3 and NLGN3 mutations disrupt postsynaptic NMDA/AMPA scaffolding; mGluR5 hyperactivation in Fragile X syndrome drives excess dendritic protein synthesis; mGluR5 antagonists failed Phase 2 trials in FXS.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — reduced GABAergic inhibition contributes to cortical E/I imbalance in ASD; GABA-A subunit mutations (GABRA1, GABRB3) are associated with ASD; PV interneuron deficits in ASD cortex reduce GABAergic tone and contribute to sensory hypersensitivity.

- `connects-to` → **[mTOR](../../../03-molecular/mtor/README.md)** — syndromic ASD via mTOR hyperactivation: tuberous sclerosis (TSC1/2 LOF), PTEN hamartoma (PTEN LOF); excess mTOR drives synaptic protein overproduction; everolimus reduces ASD severity and seizure burden in TSC patients.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — ASD features amygdala hyperreactivity to faces, atypical gaze processing via STS, reduced DMN connectivity, early cortical overgrowth followed by reduced long-range white matter connectivity, and consistent local-over-global processing bias.
- `connects-to` → **[Vasopressin](../../../03-molecular/vasopressin/README.md)** — AVPR1A promoter microsatellites (RS1, RS3) associate with ASD social behavior; V1aR in lateral septum mediates social recognition memory; V1aR-KO mice show impaired social memory; intranasal vasopressin is in Phase 2 trials for ASD social communication deficits.

- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Autism is in large part a disorder of the synapse: de novo mutations in scaffold proteins that organize the postsynaptic density tip neurons toward an excitation-inhibition imbalance, and ASD brains show early cortical neuron overgrowth then reduced long-range connectivity.

- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Autism and epilepsy frequently co-occur (roughly 20-30%), both reflecting cortical excitation-inhibition imbalance and often the same genes — SCN, GABA-receptor, and mTOR-pathway mutations cause both; shared E/I biology makes epilepsy one of ASD's key medical comorbidities.

- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Autism, bipolar disorder, and schizophrenia sit on an overlapping neurodevelopmental and genetic continuum: risk loci such as SHANK2 and the CACNA1C calcium channel are shared across all three, and bipolar disorder is a notable comorbidity in autistic people.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — Autism and ADHD are the most common neurodevelopmental comorbidity pair, co-occurring in 30-60%: they share heritability and executive-function and reward differences, DSM-5 now permits dual diagnosis, and ADHD inattention/impulsivity often complicate autistic presentations.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Tuberous sclerosis is a leading single-gene cause of syndromic autism: loss of TSC1/TSC2 disinhibits mTOR, producing cortical tubers, epilepsy and autism in up to half of patients; this links autism to the mTOR synaptic pathway and motivates mTOR-inhibitor trials.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Autism is increasingly understood as a synaptopathy: many risk genes (SHANK, neurexin/neuroligin, mTOR regulators) converge on synapse formation, pruning and the excitation/inhibition balance, so altered synaptic signaling underlies the social and sensory phenotype.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Autism and schizophrenia share neurodevelopmental origins and genetics: overlapping copy-number variants (22q11, 16p11) and synaptic genes underlie both, on a continuum of early brain miswiring—though autism presents in childhood and schizophrenia in late adolescence.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Autism and OCD share repetitive behavior but differ in drive: autistic repetitive behaviors are self-soothing and not unwanted, while OCD compulsions relieve ego-dystonic obsessions—yet the two co-occur, so telling comforting routine from distressing ritual guides care.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia are implicated in autism's altered brain wiring: as the synaptic pruners of development, dysregulated microglia may leave excess or aberrant synapses, and signs of neuroinflammation in autistic brains point to immune-neural crosstalk in early circuit formation.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Autism is linked to the gut-brain axis: many autistic people have GI symptoms and altered gut microbiomes, and microbial metabolites may influence behavior and neurodevelopment—an area of intense (if still unproven) research into diet and microbiome interventions.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes contribute to autism's altered brain wiring: beyond neurons, dysfunctional astrocytes disturb synapse formation, glutamate handling and neuroinflammation, supporting a view of autism as a disorder of brain connectivity.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Autism and anxiety disorders very frequently co-occur: a large share of autistic people have generalized anxiety, which intensifies sensory sensitivities and rigidity—so screening for and treating anxiety is central to autism care.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Elevated blood serotonin is autism's oldest biomarker: about a quarter of children with autism have platelet hyperserotonemia, and serotonin's role in early brain wiring links this neurotransmitter to the disorder's developmental origins, though its meaning stays unclear.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine circuits are implicated in autism's core features: altered mesolimbic dopamine signaling may underlie differences in social motivation and repetitive behaviors, and dopamine-blocking antipsychotics are the main drugs approved for autism-associated irritability.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Autism is a neurodevelopmental condition of the whole nervous system: altered synapse formation and excitation-inhibition balance during early brain development shape lifelong differences in perception, communication and behavior across many brain networks.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune system is woven into autism's origins: maternal infection and immune activation in pregnancy raise risk, and many autistic children show ongoing neuroinflammation with activated microglia—so immune signaling shapes the developing social brain.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF ties autism to synaptic wiring: this neurotrophin guides how synapses form and prune, and altered BDNF levels are reported in autism, fitting a model where mis-tuned synaptic growth—too many or too few connections—underlies the atypical brain development.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus is altered in autism: differences in its size and connectivity accompany the memory and spatial-learning quirks seen in the condition, and as a region of lifelong neurogenesis it links autism to how experience reshapes the developing brain.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Prenatal testosterone may bias autism risk: elevated fetal androgen exposure is one proposed factor behind the ~4:1 male predominance and the 'extreme male brain' theory, linking sex hormones in the womb to later neurodevelopment.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — The placenta is a route to autism risk: maternal immune activation, infection and exposures (like valproate) acting through the placenta during pregnancy raise ASD likelihood, pointing to a prenatal origin for much of the condition.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc helps build the synapses disrupted in autism: SHANK scaffold proteins—mutated in some autism—are zinc-dependent, and zinc concentrates at synapses, so disturbed zinc signaling is one link between trace-metal biology and synaptic ASD genes.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Autism reshapes the brain's wiring insulation: studies find altered myelin and oligodendrocyte differences underlying the atypical long- and short-range connectivity, so white-matter changes accompany the synaptic biology of ASD.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Maternal IL-6 links infection to autism risk: when the mother's immune system activates in pregnancy, IL-6 crossing to the fetal brain perturbs development in animal models, a leading mechanism behind the maternal-immune-activation hypothesis of ASD.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium tunes the glutamate signaling disturbed in autism: it blocks the NMDA receptor at rest, so altered magnesium handling can shift the excitation-inhibition balance that many ASD genes already push toward over-excitation.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Autism converges on calcium signaling: several of the strongest risk genes encode calcium channels (like CACNA1C) or calcium-handling proteins, so altered calcium flow into neurons is a recurring thread through the disorder's genetics.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Autism reaches into the gut: GI symptoms are far more common in ASD, and through the gut-brain axis the large intestine's microbes and signals can influence behavior, tying digestive health to the condition.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Autism often runs short on ATP: a subset of children show mitochondrial dysfunction that limits the cell's energy currency, and the brain's high energy demand may make developing neurons especially sensitive to this shortfall.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Brain imaging probes autism: MRI shows early brain overgrowth and altered connectivity, and fMRI photons map how differently social and sensory networks light up, sought as objective markers.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency is common in autism: restrictive eating lowers stores, and because iron is needed to make dopamine, low iron may worsen attention, sleep and restless behaviors.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Autism shows in the eyes: reduced eye contact and atypical gaze are early signs, and eye-tracking is studied as an objective measure of the social differences that define the condition.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy hints at autism's altered wiring: studies find changes in dendritic spine density and synapse structure, the fine connections between neurons that mTOR and other autism genes help build and prune.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D in pregnancy may shape the risk: low maternal vitamin D during fetal brain development is associated with a higher chance of autism, fitting the vitamin's role in neurodevelopment and immune regulation.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Autism and the heart often travel together: children with congenital heart disease have elevated rates of autism, the shared early developmental disruption and surgical-stress exposure linking the two conditions.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Sleep is a near-universal struggle in autism: disrupted melatonin rhythms leave many autistic children unable to fall or stay asleep, and melatonin is the first-line treatment, easing both the insomnia and the daytime behavior it worsens.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The gut is a frequent trouble spot: autistic children have high rates of reflux, constipation, and selective eating, the GI symptoms feeding into the gut-brain axis already implicated in the condition.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The mother's thyroid shapes the risk: adequate maternal thyroid hormone is critical for fetal brain development, and maternal hypothyroxinemia in pregnancy is a recognized risk factor for autism in the child.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — A mother's antibodies can target the fetal brain: in maternal-autoantibody-related autism, IgG against fetal brain proteins crosses the placenta and disturbs neurodevelopment, one immune route into the condition's many causes.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Immune genes sit among the risk loci: MHC/HLA variants and maternal immune activation in pregnancy are tied to autism, linking the brain's wiring to the same antigen-presenting machinery that runs immunity.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Much of the risk is set before birth: advanced parental age, prenatal valproate, and maternal immune activation shape autism risk, and the striking male predominance points to sex-hormone influences on the developing brain.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Maternal IL-17A is a molecular bridge from infection to autism: in maternal immune activation models, this Th17 cytokine crosses into the fetal brain and alters cortical development, producing autism-like behavior in the offspring.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Brain mast cells may stoke the neuroinflammation: they sit near the blood-brain barrier and release mediators that activate microglia, and the high rate of allergy and mast-cell activation in autism hints at a role in some cases.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — A single-gene road to autism: neurofibromatosis type 1 carries a high rate of autism features, one of the RAS-MAPK 'RASopathies' that, like tuberous sclerosis, show how one mutation can derail the social brain.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The body's cannabis system tunes the social brain: endocannabinoid signaling shapes the synaptic plasticity and reward responses to social cues, and its dysregulation in autism is the rationale behind cannabidiol trials for the condition.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — An immune imbalance shadows it: reduced regulatory T cells and a tilt toward inflammation accompany autism, fitting the maternal-immune-activation models in which prenatal inflammation reshapes brain development.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep rarely comes easy: insomnia and disrupted sleep architecture are strikingly common in autism, tied to altered melatonin rhythms, and poor sleep in turn worsens daytime behavior and core symptoms.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Neuroinflammation runs through NF-κB: maternal immune activation and microglial activation in autism converge on NF-κB-driven cytokine signaling, part of the inflammatory thread woven through its neurodevelopment.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — One gene ties autism to overgrowth: PTEN mutations cause a macrocephaly-autism syndrome, and because PTEN restrains the mTOR pathway, its loss drives the synaptic overgrowth linking this monogenic cause to the broader spectrum.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The gut speaks loudly in autism: constipation, diarrhea and abdominal pain are far more common than in peers, a GI burden tied to the gut-brain axis and to the altered microbiome that accompanies the condition.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — Social difficulty breeds social fear: social anxiety is among the most common comorbidities in autism, as repeated misread interactions and rejection foster intense anticipatory fear of social situations.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Isolation and burnout darken mood: depression is markedly elevated in autistic people, driven by loneliness, the exhaustion of masking, and the cumulative toll of navigating an unaccommodating world.
- `connects-to` → **[Obesity](../obesity/README.md)** — Several forces tip toward weight gain: restricted food preferences, reduced physical activity, and the appetite-stimulating antipsychotics often prescribed in autism combine to raise the rate of obesity.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Antipsychotics and obesity raise the risk: the metabolic side effects of antipsychotics prescribed for irritability in autism, on top of its associated obesity and inactivity, elevate the rate of type 2 diabetes.
- `connects-to` → **[Iron-Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Selective eating starves the body of iron: the rigid, narrow food preferences and avoidant-restrictive eating common in autism frequently lead to inadequate iron intake and iron-deficiency anemia.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — Rigidity and sensory aversion feed eating disorders: autism markedly raises the risk of restrictive eating disorders like anorexia, where its inflexibility and sensory sensitivities shape and entrench the food restriction.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Movement and coordination are commonly affected: autism is frequently accompanied by hypotonia, motor dyspraxia and clumsiness, and an over-representation of joint hypermobility and connective-tissue laxity.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It shares an allergic, immune skin link: atopic dermatitis and eczema are more common in autism, reflecting the immune dysregulation tied to the condition, and self-injury can further damage the skin.
- `connects-to` → **[PTSD](../ptsd/README.md)** — A world of adversity raises trauma risk: autistic people face high rates of bullying, abuse and overwhelming environments, giving elevated rates of post-traumatic stress that camouflaging can hide.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its autonomic balance differs: autism is associated with altered heart-rate variability and autonomic reactivity, and several ASD-linked genetic syndromes include congenital heart disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its medications reshape metabolism: antipsychotics like risperidone and aripiprazole, used for autism-related irritability, commonly cause weight gain, hyperprolactinaemia and metabolic syndrome.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Continence comes late: nocturnal enuresis and delayed toilet training are more common in autistic children, and some ASD-associated genetic syndromes carry renal and urinary-tract anomalies.
- `connects-to` → **[Influenza A](../../../02-pathogen/01-viruses/influenza-a/README.md)** — Maternal infection raises the odds: severe maternal influenza and prolonged fever in pregnancy are linked to higher autism risk, an example of the maternal-immune-activation hypothesis of neurodevelopment.
- `connects-to` → **[Measles virus](../../../02-pathogen/01-viruses/measles-virus/README.md)** — The MMR-autism scare was fraudulent: the claim linking measles vaccination to autism was retracted and disproven, and large studies show no association — vaccination does not cause autism.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet draws research interest: omega-3 supplementation has been trialled for autism symptoms, but the evidence remains weak and it is not an established treatment.
- `connects-to` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — A congenital infection that raises risk: maternal cytomegalovirus and other congenital infections are established environmental risk factors for autism, acting through fetal neuroinflammation.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — A trace-metal imbalance is described: altered copper-to-zinc ratios are reported in autism, with relative copper excess and zinc deficiency linked to oxidative stress in the developing brain.
- `connects-to` → **[Sulforaphane](../../../03-medicine/03-food/sulforaphane/README.md)** — A food compound with a trial behind it: a randomised trial found broccoli-derived sulforaphane modestly improved behaviour in autism, proposed to act by reducing oxidative stress and inflammation.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Syndromic autism has druggable pathways: in TSC-, PTEN- and fragile-X-related autism the mTOR and synaptic-signalling pathways are dysregulated, making mTOR inhibitors and other targeted agents candidates for the syndromic forms.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Connectivity is altered: autism shows atypical long-range underconnectivity and local overconnectivity, with white-matter and axonal-transport differences shaping how distant brain regions communicate.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The gut-brain axis is implicated: many autistic people have GI symptoms and altered intestinal-epithelial barrier function, part of the microbiome-gut-brain signalling increasingly linked to autism.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — A PTEN route to autism: germline PTEN loss causes macrocephaly with autism spectrum disorder, linking ASD to Cowden syndrome's PTEN-hamartoma-tumour predisposition—one gene bridging neurodevelopment and cancer.
- `connects-to` → **[Noonan Syndrome](../noonan-syndrome/README.md)** — RASopathies raise autism traits: like other RAS-MAPK developmental syndromes, Noonan syndrome carries an increased rate of autism spectrum features, implicating RAS signalling in social-cognitive development.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — When an ion channel links heart and brain: Timothy syndrome's CACNA1C calcium-channel mutation causes long-QT arrhythmia with autism, and antipsychotics used in ASD prolong the QT, tying ASD to cardiac conduction.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Maternal immune activation: prenatal infection and maternal autoantibodies—made by germinal-centre B cells—are linked to autism risk, implicating the maternal adaptive immune response in fetal brain development.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Pervasive sleep disruption: autism features high rates of insomnia and circadian/REM sleep abnormalities that overlap the sleep-wake dysregulation of narcolepsy, and melatonin helps the disturbed sleep in both.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Lower bone density: restricted diets, reduced weight-bearing activity and SSRI use leave many autistic individuals with reduced cortical-bone density and a higher fracture risk.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Maternal immune activation and disrupted care: maternal COVID-19 (like influenza) joins the infections studied for neurodevelopmental risk in offspring, while the pandemic disrupted autism diagnosis and therapy services.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — An overlapping differential: autism and borderline personality disorder share emotional dysregulation and social difficulty and are frequently confused, especially in autistic women diagnosed late.
- `connects-to` → **[Internet Gaming Disorder](../internet-gaming-disorder/README.md)** — Screens as refuge and risk: autistic individuals have markedly higher rates of problematic internet and gaming use, the predictable, controllable digital world offering both comfort and a route to dependence.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Maternal immune activation: IL-1β is a key cytokine of the maternal immune activation linked to autism risk, and elevated IL-1β features in the neuroinflammation seen in autistic brains.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Neuroimmune signature: raised TNF-α is among the inflammatory markers reported in autism, reflecting the microglial activation and immune dysregulation implicated in its neurodevelopment.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Synaptic growth factor: IGF-1 promotes synapse maturation and has been trialled in autism-related disorders such as Rett and Phelan-McDermid syndromes for its neurodevelopmental effects.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — Hyperserotonemia: elevated whole-blood serotonin tied to serotonin-transporter function is the oldest and most replicated biomarker in autism, implicating serotonergic development in the disorder.
- `connects-to` → **[TSC1-TSC2](../../03-molecular/tsc1-tsc2/README.md)** — mTOR-pathway autism: loss of the TSC1-TSC2 complex in tuberous sclerosis unleashes mTOR and causes a high rate of autism, a defining example of the synaptic-overgrowth mechanism in syndromic ASD.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — Chromatin-remodeling risk: de novo mutations in chromatin regulators like ARID1A are a leading genetic class in autism, disrupting the gene-expression programmes that build neural circuits.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Gestational infection signaling through TLR4 raises offspring autism risk in both human studies and animal models—the innate-immune trigger central to the maternal-immune-activation hypothesis that links prenatal inflammation to ASD.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β is dysregulated in Fragile X syndrome and other syndromic autism, a kinase governing synaptic plasticity whose inhibition (e.g. by lithium) rescues phenotypes in ASD models—a convergent signaling node across genetic causes.
- `connects-to` → **[NTRK / TrkB](../../03-molecular/ntrk/README.md)** — BDNF acting through its TrkB receptor shapes the synapse formation and plasticity disrupted in autism, linking neurotrophin signaling to the altered brain connectivity that underlies the disorder's core features.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Gain-of-function mutations in the L-type calcium channel CACNA1C cause Timothy syndrome with autism, and broader calcium-signaling dysregulation is a recurring theme among autism risk genes affecting synaptic activity-dependent transcription.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 tags synapses for microglial elimination during development, and dysregulated complement-mediated pruning is implicated in the altered synaptic density and connectivity seen in autism.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Prenatal type-I-interferon responses to maternal infection raise autism risk, a key strand of the neurodevelopmental immune hypothesis linking gestational inflammation to altered fetal brain development.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — The PTEN-PI3K-AKT-mTOR pathway (PTEN, mTOR and TSC1/2 already mapped) is a convergence point of syndromic autism, where excess AKT-mTOR signaling drives the synaptic overgrowth and macrocephaly of ASD.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RAS-MAPK-ERK signaling, hyperactivated in the RASopathies (neurofibromatosis-1 and Noonan already mapped) that carry high autism risk, regulates the synaptic plasticity disrupted in autism spectrum disorder.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt/β-catenin signaling, regulated by high-confidence autism genes such as CHD8, governs the neuronal proliferation and synaptic development perturbed in autism spectrum disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — The PTEN-PI3K-AKT-mTOR pathway (PTEN, AKT, mTOR and TSC1-TSC2 all mapped) is dysregulated in syndromic autism, driving the synaptic-protein-synthesis imbalance underlying its phenotype.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Maternal infection signals through TLR (TLR4 mapped) and MyD88, and the resulting maternal IL-6/IL-17 (mapped) shapes fetal brain development, a major environmental autism-risk pathway.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcium-calcineurin-NFAT signaling regulates activity-dependent synaptic plasticity, a process disrupted in the excitatory/inhibitory imbalance of autism spectrum disorder.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Maternal IL-6 acting through STAT3 (IL-6 mapped) is a central mediator of the maternal-immune-activation pathway linked to autism risk in offspring.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine-driven JAK-STAT signaling transduces the maternal and neuroinflammatory cytokine milieu implicated in the neurodevelopmental alterations of autism.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 marks the reactive-microglia state reported in autism brains, contributing to the neuroinflammatory component of the disorder.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling transduces the maternal-immune-activation interferon exposure epidemiologically linked to autism spectrum disorder.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the innate neuroinflammatory activation implicated in autism spectrum disorder.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the neurodevelopmental and synaptic processes whose perturbation is implicated in autism spectrum disorder.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of the PTEN-PI3K-AKT-mTOR axis (PTEN, AKT, PIK3CA, mTOR, and TSC1-TSC2 already mapped) regulates neuronal growth and synaptic programs disrupted in autism spectrum disorder.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the maternal-immune-activation and neuroinflammatory signaling implicated in autism spectrum disorder.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and oxidative-stress responses are implicated in the neurodevelopmental pathophysiology of autism spectrum disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, in balance with the mTOR pathway (mTOR already mapped), regulates the neuronal metabolic and autophagy homeostasis implicated in autism spectrum disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of the neurodevelopmental gene expression disrupted in autism spectrum disorder.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression participates in the chromatin regulation of the neurodevelopmental programs implicated in autism spectrum disorder (ARID1A already mapped).
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the synaptic pruning and dendritic-spine homeostasis (mTOR already mapped) implicated in autism spectrum disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (FYN) kinase signaling participates in the NMDA-receptor and synaptic signaling implicated in autism spectrum disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the maternal-immune-activation and neuroinflammation implicated in autism spectrum disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuronal migration and neurodevelopmental processes implicated in autism spectrum disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial synaptic pruning and neuroinflammation implicated in autism spectrum disorder.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement signaling, alongside complement-mediated synaptic pruning (complement-C3 already mapped), participates in the synaptic remodeling implicated in autism spectrum disorder.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the synaptic and neuroimmune modulation implicated in autism spectrum disorder.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microglial activation and neuroinflammation implicated in autism spectrum disorder.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 (MCP-1) chemokine signaling participates in the neuroinflammatory and microglial responses (including maternal immune activation) implicated in autism spectrum disorder.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Female protective effect: autism is diagnosed about four times more often in males, and estrogen's neuroprotective and synaptic effects are proposed to raise the mutational threshold in females (fetal testosterone already mapped), contributing to the sex bias.
- `connects-to` → **[NFE2L2](../../03-molecular/nfe2l2/README.md)** — Oxidative stress: children with autism show evidence of glutathione depletion and oxidative stress, and the NRF2 antioxidant response modulated here is implicated in the redox imbalance affecting neurodevelopment.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Nitrosative signalling: nitric oxide is both a synaptic messenger shaping the excitatory-inhibitory balance and a source of nitrosative stress, and altered NO signalling is reported in autism spectrum disorder.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Maternal immune activation: shifts in the type-2 cytokine IL-4 balance during maternal immune activation, alongside the IL-6 and IL-17 (already mapped) implicated in animal models, are part of the prenatal immune milieu linked to autism risk.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Immune dysregulation: altered IL-2 and regulatory-T-cell function are reported in autism and in the mothers of affected children, part of the immune dysregulation that accompanies a subset of the disorder.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Neurosteroid modulation: progesterone-derived neurosteroids modulate GABAergic (already mapped) signalling in the developing brain, and prenatal sex-steroid exposure alongside estrogen (already mapped) is implicated in the male preponderance of autism.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the maternal immune activation and the microglial (already mapped) cyclooxygenase pathway (IL-6 and IL-17 already mapped) are implicated in the altered neurodevelopment of a subset of autism.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune counter-regulation: IL-10 opposes the pro-inflammatory signals (IL-6, TNF and IL-1 already mapped) of the maternal immune activation and the immune dysregulation reported in a subset of autism, part of its immune dimension.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: mitochondrial dysfunction and heightened oxidative stress, to which xanthine oxidase contributes, are reported in autism (NRF2 already mapped), and the resulting reactive oxygen species may affect the developing neurons (already mapped).
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Maternal immune activation: IL-13, with IL-4 (already mapped), is part of the type-2 response, and the maternal cytokine milieu (IL-6 and IL-17 already mapped) during pregnancy is implicated in the maternal-immune-activation model of autism.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histaminergic neurotransmission: histamine acting on H3 receptors modulates the neurotransmission (dopamine and serotonin already mapped) and arousal implicated in autism, and H3 ligands have been explored for its cognitive and behavioural features.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine and neurodevelopment: leptin influences neurodevelopment and is reported to be altered in autism, part of the metabolic-neurodevelopmental dimension of the disorder alongside the mTOR (already mapped) signalling.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Cholinergic neurotransmission: the cholinergic (nicotinic and muscarinic) system, implicated in the attention and social cognition (dopamine and serotonin already mapped) of autism, is a focus of the neurotransmitter research into the disorder.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine crosstalk: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-neurodevelopmental crosstalk reported altered in autism spectrum disorder.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine inflammation: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the metabolic and neuroinflammatory (IL-6 already mapped) dimension of autism spectrum disorder.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Neuronal connectivity: the altered neuronal migration, synaptogenesis (mTOR and PTEN already mapped) and the excitatory/inhibitory (glutamate and GABA already mapped) balance of the neurons underlie autism spectrum disorder.
- `connects-to` → **[ADHD](../attention-deficit-hyperactivity-disorder/README.md)** — ADHD comorbidity: attention-deficit/hyperactivity disorder is highly comorbid with autism spectrum disorder, the two sharing the genetic and the neurodevelopmental (dopamine already mapped) overlap.
- `connects-to` → **[Gut microbiome](../gut-microbiome/README.md)** — Gut-brain axis: the altered gut microbiome and the gut-brain (serotonin already mapped) signalling are implicated in the GI symptoms and the behaviour of autism spectrum disorder.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 maternal-immune activation: the IFN-γ of the T cells is the type-II interferon arm of the maternal immune activation (IL-6 and IL-17 already mapped) implicated in the neurodevelopment of autism spectrum disorder.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune dysregulation and the maternal immune activation of autism spectrum disorder.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation and the atopy comorbidity of autism spectrum disorder.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Maternal Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm central to the maternal immune activation implicated in autism spectrum disorder.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/atopy arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension and the atopy comorbidity of autism spectrum disorder.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells, including the maternal Th17 (IL-17 already mapped), are the source of the cytokines of the immune dysregulation and the maternal immune activation of autism spectrum disorder.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive neuroimmune arm: the cytotoxic T cells (perforin pathway) of the CNS-border compartments are part of the adaptive-immune contribution to the neuroinflammation implicated in autism spectrum disorder.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Maternal/innate NK: the NK cells (perforin pathway), including the maternal NK dysregulation of the maternal immune activation, are part of the innate-immune dimension of autism spectrum disorder.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the microglial (already mapped) activation and the complement-mediated synaptic pruning implicated in autism spectrum disorder.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-mediated synaptic pruning implicated in autism spectrum disorder.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway (C1q-initiated) implicated in the aberrant synaptic pruning of autism spectrum disorder.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Neuroimmune interface: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the maternal-immune-activation and neuroinflammation of autism spectrum disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-neuroimmune axis: TSLP, from skin (already mapped) and gut (already mapped) barriers, primes dendritic cells (already mapped) and mast cells (already mapped) and amplifies the Th2/Treg (already mapped) imbalance of the maternal-immune-activation of ASD.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-neuroinflammation axis: bradykinin, via the B2R on CNS microglia (already mapped) and neurons (already mapped), amplifies the neuroinflammation and the BBB permeability contributing to the immune-activation dimension of autism spectrum disorder.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective EPO: erythropoietin signals through EpoR on neurons (already mapped) and oligodendrocytes (already mapped), supporting the myelination and the synaptic plasticity (already mapped) implicated in the neurodevelopmental dimension of autism spectrum disorder.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Synapse ECM scaffold: periostin, expressed by astrocytes (already mapped) in the synaptic extracellular matrix, modulates the perineuronal nets that regulate synaptic pruning (microglia already mapped) and the excitatory/inhibitory balance of autism spectrum disorder.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Neuroimmune developmental axis: prolactin, acting via PRLR on microglia (already mapped) and astrocytes (already mapped), modulates the neuroinflammatory cytokine milieu (TNF-α and IL-6 already mapped) and may influence the sex-differential prevalence of autism spectrum disorder.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant neurodevelopment: selenium, incorporated into selenoproteins (thioredoxin reductase and GPx), scavenges ROS in developing neurons (already mapped) and supports the glutathione (already mapped) redox balance disrupted in the oxidative stress hypothesis of ASD.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-mediated myelination: iodine, via thyroid hormone synthesis, supports myelination and synapse maturation critical in ASD; iodine deficiency amplifies IL-6 and mTOR neurodevelopmental disruption of ASD.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Neuronal excitatory-inhibitory balance: sodium, via neuronal Na+ channels, maintains glutamate/GABA excitatory-inhibitory balance; sodium dysregulation amplifies NF-κB neuroinflammation and synapse dysfunction of ASD.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron delivery for myelination: transferrin supplies iron to neurons and oligodendrocytes for myelination; transferrin deficiency amplifies NF-κB neuroinflammation and iron-deficiency-anaemia burden of ASD.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — ASD potassium: potassium channels regulate GABA (already mapped) and glutamate (already mapped) excitatory-inhibitory balance at synapses (already mapped); channel dysfunction amplifies NF-κB (already mapped) neuroinflammation and neurodevelopmental disruption of ASD.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — ASD phosphorus: phosphorus, as phospholipid and ATP, is essential for synapse (already mapped) integrity and neuronal (neuron already mapped) energy; phosphorus dysregulation impairs mTOR (already mapped) anabolic signalling and the synaptic pruning disrupted in ASD.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — ASD sulfur: glutathione (sulfur-containing) is depleted in ASD; sulfur deficiency impairs ROS quenching in neurons (already mapped) and astrocytes (already mapped), worsening oxidative stress that amplifies NF-κB (already mapped) and mTOR (already mapped) disruption.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — ASD chloride: chloride homeostasis via GABA(A) and KCC2 on neurons (already mapped) governs inhibitory tone; chloride dysregulation converts GABA to excitatory, amplifying mTOR (already mapped) and NF-κB (already mapped) hyperexcitability and the E/I imbalance of ASD.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — ASD nitrogen: nitric oxide (NO, nitrogen-derived) in neurons (already mapped) and microglia (already mapped) amplifies neuroinflammation; NO excess upregulates NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) dysregulation of ASD.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — ASD oxygen: mitochondrial oxygen metabolism in neurons (already mapped) and astrocytes (already mapped) generates ROS; ROS excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) dysregulation, worsening BDNF (already mapped) deficits in ASD.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — ASD carbon: carbon-backbone metabolites in neurons (already mapped) and astrocytes (already mapped) fuel acetyl-CoA and mTOR (already mapped) anabolic signalling; carbon metabolic imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade in ASD.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — norepinephrine from neurons (already mapped) modulates arousal and prefrontal attention; norepinephrine deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) and oxytocin (already mapped) circuit disruption in autism spectrum disorder.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF from neurons (already mapped) and astrocytes (already mapped) sustains brain (already mapped) vascular development; VEGF excess amplifies NF-κB (already mapped) and mTOR (already mapped) and IL-6 (already mapped) and IGF-1 (already mapped) neurodevelopmental cascade in ASD.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 on microglia (already mapped) and neurons (already mapped) limits brain (already mapped) neuroinflammation; PD-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and IFN-γ (already mapped) and TNF-α (already mapped) neuroinflammatory cascade in ASD.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — ASD hydrogen: hydrogen via ROS balance in neurons (already mapped) and microglia (already mapped) modulates neuroimmune oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory cascade in ASD.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — ASD glp-1: GLP-1 on neurons (already mapped) and astrocytes (already mapped) modulates synaptic metabolism; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory connectivity disruption in ASD.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — ASD angiotensin-ii: angiotensin II on astrocytes (already mapped) and microglia (already mapped) modulates cerebrovascular tone; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroimmune dysregulation in ASD.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — ASD rankl: RANKL in microglia (already mapped) and astrocytes (already mapped) modulates neuroimmune skewing; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory connectivity disruption in ASD.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — ASD fibronectin: fibronectin in astrocytes (already mapped) and neurons (already mapped) promotes ECM remodelling at synapses; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) neuroinflammatory cascade in ASD.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — ASD notch: notch signalling in neurons (already mapped) and astrocytes (already mapped) regulates synaptic development; notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BDNF (already mapped) connectivity disruption in ASD.

[^maenner-2023-asd-prevalence]: Maenner MJ, Warren Z, Williams AR, et al. Prevalence and characteristics of autism spectrum disorder among children aged 8 years — ADDM Network, 2020. *MMWR Surveill Summ.* 2023;72(2):1-14. [doi:10.15585/mmwr.ss7202a1](https://doi.org/10.15585/mmwr.ss7202a1) · [PubMed 36952216](https://pubmed.ncbi.nlm.nih.gov/36952216/)
[^lord-2020-asd-review]: Lord C, Elsabbagh M, Baird G, Veenstra-Vanderweele J. Autism spectrum disorder. *Lancet.* 2018;392(10146):508-520. [doi:10.1016/S0140-6736(18)31129-2](https://doi.org/10.1016/S0140-6736(18)31129-2) · [PubMed 30078460](https://pubmed.ncbi.nlm.nih.gov/30078460/)
[^sanders-2012-asd-exome]: Sanders SJ, Murtha MT, Gupta AR, et al. De novo mutations revealed by whole-exome sequencing are strongly associated with autism. *Nature.* 2012;485(7397):237-241. [doi:10.1038/nature10945](https://doi.org/10.1038/nature10945) · [PubMed 22495306](https://pubmed.ncbi.nlm.nih.gov/22495306/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
