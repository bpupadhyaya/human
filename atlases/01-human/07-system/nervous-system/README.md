---
schema: human-scale-entry/v1
id: nervous-system
name: Nervous System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-04
summary: "CNS (brain + spinal cord) + PNS (somatic, autonomic, enteric) — the master regulatory system for sensation, movement, cognition, and homeostasis. Signal velocity 0.5–120 m/s. Neurological diseases are the leading cause of global disability."
aliases: ["CNS", "PNS", "central nervous system", "peripheral nervous system", "autonomic nervous system", "somatic nervous system"]
sources:
  - id: kandel-principles-ns
    type: textbook
    cite: "Kandel ER, Koester JD, Mack SH, Siegelbaum SA. Principles of Neural Science. 6th ed. McGraw-Hill; 2021."
    url: "https://www.mhprofessional.com/principles-of-neural-science-sixth-edition-9781259642234-usa"
    accessed: "2026-06-04"
  - id: guyton-hall-physiology
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2020."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-04"
  - id: who-neurological-2006
    type: regulatory
    cite: "World Health Organization. Neurological Disorders: Public Health Challenges. WHO Press; 2006."
    url: "https://www.who.int/publications/i/item/9241563362"
    accessed: "2026-06-04"
  - id: purves-neuroscience-ns
    type: textbook
    cite: "Purves D, Augustine GJ, Fitzpatrick D, et al. Neuroscience. 6th ed. Sinauer Associates; 2018."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK10792/"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The nervous system is one of the 11 major organ systems of the human body."
  - target: 01-human/06-organ/brain
    relation: contains
    note: "The brain is the primary organ of the nervous system and CNS."
  - target: 01-human/04-cellular/neuron
    relation: contains
    note: "Neurons are the fundamental computational cells of the nervous system throughout CNS and PNS."
  - target: 01-human/03-molecular/dopamine
    relation: contains
    note: "Dopamine is a core neurotransmitter operating within multiple CNS circuits of the nervous system."
  - target: 01-human/03-molecular/glutamate
    relation: contains
    note: "Glutamate is the dominant excitatory neurotransmitter throughout CNS circuits."
  - target: 01-human/03-molecular/gaba
    relation: contains
    note: "GABA is the dominant inhibitory neurotransmitter throughout CNS circuits."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Autonomic nervous system controls heart rate, vascular tone, and blood pressure; baroreceptor reflex links the two systems bidirectionally."
  - target: 01-human/03-molecular/serotonin
    relation: modulated-by
    note: "CNS serotonin (5-HT) from raphe nuclei projects broadly to limbic, prefrontal cortex, and cerebellar circuits; regulates mood, sleep-wake cycles, appetite, cognition, and thermoregulation via 14+ receptor subtypes."
  - target: 01-human/03-molecular/cortisol
    relation: modulated-by
    note: "Cortisol crosses the blood-brain barrier and acts on hippocampal, amygdalar, and prefrontal GRs, modulating memory consolidation, fear conditioning, and mood; chronic cortisol excess causes hippocampal atrophy and depression-like states."
  - target: 01-human/03-molecular/cortisol
    relation: modulates
    note: "The CNS drives cortisol secretion via the HPA axis: hypothalamic CRH → anterior pituitary ACTH → adrenal cortex cortisol; hippocampal GRs provide negative feedback to terminate the cortisol response after acute stress."
  - target: 01-human/03-molecular/insulin
    relation: modulated-by
    note: "Insulin crosses the BBB via receptor-mediated transcytosis; acts in hypothalamus to suppress appetite and food intake; modulates hippocampal synaptic plasticity and memory; central insulin resistance contributes to neurodegeneration risk."
  - target: 03-medicine/02-traditional/ashwagandha
    relation: modulated-by
    evidence: kandel-principles-ns
    note: "Ashwagandha withanolides cross the blood-brain barrier and modulate GABA-A receptors and cortisol-driven HPA axis activity, reducing anxiety and neuroinflammation."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: modulated-by
    note: "SERT sets ambient 5-HT tone across the CNS; SSRI inhibition of SERT elevates synaptic 5-HT at serotonergic synapses throughout the nervous system, mediating antidepressant, anxiolytic, and other CNS effects over weeks."
  - target: 02-pathogen/02-bacteria/clostridium-tetani
    relation: damaged-by
    note: "Tetanospasmin blocks inhibitory interneurons throughout the CNS, causing generalised rigidity (risus sardonicus, opisthotonos), trismus, and autonomic instability; untreated case fatality exceeds 50% without ICU support."
  - target: 02-pathogen/02-bacteria/clostridium-tetani
    relation: prevented-by
    note: "Tetanus toxoid (DTP/Td/TT) prevents nervous system damage by inducing neutralising IgG against TeNT; childhood primary series plus boosters every 10 years maintain protective antibody titres (>0.1 IU/mL)."
  - target: 02-pathogen/02-bacteria/clostridium-tetani
    relation: treated-by
    note: "Tetanus treatment includes TIG to neutralise unbound toxin, wound debridement, metronidazole (kills vegetative C. tetani), benzodiazepines for spasm control, and ICU supportive care with mechanical ventilation if needed."
  - target: 01-human/03-molecular/vasopressin
    relation: modulated-by
    note: "Modulated by Vasopressin."
  - target: 01-human/03-molecular/nitric-oxide
    relation: modulated-by
    note: "Modulated by Nitric Oxide."
  - target: 01-human/03-molecular/histamine
    relation: modulated-by
    note: "Modulated by Histamine."
  - target: 01-human/03-molecular/norepinephrine
    relation: modulated-by
    note: "Modulated by Norepinephrine."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: modulated-by
    note: "Modulated by Thyroid Hormones (T3/T4)."
  - target: 01-human/03-molecular/acetylcholine
    relation: modulated-by
    note: "Modulated by Acetylcholine."
  - target: 01-human/03-molecular/leptin
    relation: modulated-by
    note: "Modulated by Leptin."
  - target: 01-human/02-atomic/iodine
    relation: modulated-by
    note: "Modulated by Iodine."
  - target: 01-human/02-atomic/copper
    relation: modulated-by
    note: "Modulated by Copper."
  - target: 01-human/07-system/reproductive-system
    relation: modulated-by
    note: "Modulated by Reproductive System."
  - target: 01-human/07-system/musculoskeletal-system
    relation: modulated-by
    note: "Modulated by Musculoskeletal System."
  - target: 01-human/07-system/endocrine-system
    relation: modulated-by
    note: "Modulated by Endocrine System."
  - target: 01-human/07-system/integumentary-system
    relation: modulated-by
    note: "Modulated by Integumentary System."
  - target: 01-human/04-cellular/microglia
    relation: modulated-by
    note: "Modulated by Microglia."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: modulated-by
    note: "Modulated by Oligodendrocyte."
  - target: 01-human/04-cellular/astrocyte
    relation: modulated-by
    note: "Modulated by Astrocyte."
  - target: 01-human/04-cellular/mast-cell
    relation: modulated-by
    note: "Modulated by Mast Cell."
  - target: 01-human/06-organ/large-intestine
    relation: modulated-by
    note: "Modulated by Large Intestine."
  - target: 01-human/06-organ/stomach
    relation: modulated-by
    note: "Modulated by Stomach."
  - target: 01-human/06-organ/thyroid
    relation: modulated-by
    note: "Modulated by Thyroid Gland."
  - target: 02-pathogen/01-viruses/rabies-virus
    relation: damaged-by
    note: "Damaged by Rabies Virus (RABV)."
  - target: 02-pathogen/01-viruses/zika-virus
    relation: damaged-by
    note: "Damaged by Zika Virus (ZIKV)."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: damaged-by
    note: "Damaged by Varicella-Zoster Virus."
  - target: 02-pathogen/03-fungi/cryptococcus-neoformans
    relation: damaged-by
    note: "Damaged by Cryptococcus neoformans."
  - target: 02-pathogen/04-parasites/trypanosoma-brucei
    relation: damaged-by
    note: "Damaged by Trypanosoma brucei."
  - target: 02-pathogen/04-parasites/trypanosoma-cruzi
    relation: damaged-by
    note: "Damaged by Trypanosoma cruzi."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: damaged-by
    note: "Damaged by Toxoplasma gondii."
  - target: 02-pathogen/02-bacteria/listeria-monocytogenes
    relation: damaged-by
    note: "Damaged by Listeria monocytogenes."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: modulated-by
    note: "Modulated by Dietary Magnesium."
  - target: 03-medicine/02-traditional/ginkgo-biloba
    relation: modulated-by
    note: "Modulated by Ginkgo biloba (EGb 761)."
  - target: 03-medicine/02-traditional/panax-ginseng
    relation: modulated-by
    note: "Modulated by Panax ginseng (Korean Red Ginseng)."
  - target: 03-medicine/02-traditional/st-johns-wort
    relation: modulated-by
    note: "Modulated by St. John's Wort (Hypericum perforatum)."
  - target: 02-pathogen/05-prions/prion-protein
    relation: damaged-by
    note: "PrPSc propagates via axonal transport along synaptic networks; spongiform degeneration (vacuolation, neuronal dropout) spreads anatomically through the nervous system; thalamus in FFI, cerebellar cortex in GSS, cerebral cortex/basal ganglia in sCJD; uniformly fatal."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "The synapse is where the nervous system computes: chemical and electrical junctions between neurons transmit and weight signals, and their plasticity underlies learning, memory, and the disorders that disrupt connectivity."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium carries the nerve impulse: the inrush of sodium ions through voltage-gated channels generates the action potential, the electrical signal on which all nervous-system communication depends."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Stroke is the nervous system starved of blood: a blocked or burst cerebral vessel kills neurons within minutes, the leading cause of acquired neurological disability and a prime example of the brain's dependence on its circulation."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "The commonest way the nervous system degenerates: Alzheimer's disease destroys cortical and hippocampal neurons through amyloid and tau pathology, the leading cause of dementia and the archetypal neurodegenerative disease."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "A movement disorder of dying neurons: Parkinson's disease kills the dopaminergic neurons of the substantia nigra through α-synuclein pathology, the second commonest neurodegenerative disease of the nervous system."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "Autoimmunity strips the nervous system's insulation: multiple sclerosis is an immune attack on central myelin, the leading non-traumatic cause of neurological disability in young adults."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Hyperexcitable circuits misfire: epilepsy is the nervous system's paroxysmal disorder, in which synchronized neuronal discharge produces seizures, arising from injury, tumor, malformation or channel dysfunction."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "Its own glia turn malignant: glioblastoma is the commonest and deadliest primary brain cancer, arising from the astrocytic support cells of the nervous system and diffusely infiltrating the brain."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Mood is a function of its circuits: major depression reflects dysregulation across the monoaminergic and limbic networks of the nervous system, the neurobiological basis of a leading cause of disability."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It runs a second brain in the gut: the enteric nervous system governs motility and secretion, and the bidirectional gut-brain axis links nervous-system signalling to digestion, microbiome and mood."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Nerves and immunity converse constantly: the nervous system shapes inflammation through the vagal cholinergic anti-inflammatory pathway and sympathetic tone, while neuroinflammation in turn drives neurological disease."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "A classic assault on its protective membranes: Neisseria meningitidis crosses into the cerebrospinal fluid to cause acute bacterial meningitis, inflaming the meninges that sheath the brain and spinal cord."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It drives every breath: brainstem respiratory centres set the rhythm of breathing and the diaphragm obeys the phrenic nerve, so brainstem injury, high spinal cord damage and neuromuscular disease cause respiratory failure."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It governs the bladder: the autonomic and somatic innervation of the bladder coordinates storage and voiding, so spinal cord and autonomic injury cause neurogenic bladder with retention and incontinence."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The brain has its own drainage: the glymphatic system and meningeal lymphatic vessels clear waste and immune cells from the central nervous system, a route increasingly tied to neurodegeneration."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "A common virus can inflame the brain: herpes simplex is the leading cause of sporadic viral encephalitis, with a predilection for the temporal lobes, and varicella-zoster causes the painful neuralgia of shingles."
  - target: 02-pathogen/01-viruses/measles-virus
    relation: connects-to
    note: "Measles can smoulder in the brain for years: subacute sclerosing panencephalitis is a fatal degenerative brain disease emerging years after measles infection, from persistent virus in neurons."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Tuberculosis can besiege the meninges: tuberculous meningitis is a slow, devastating infection of the basal meninges causing cranial nerve palsies, hydrocephalus and stroke."
  - target: 02-pathogen/01-viruses/coxsackievirus-b
    relation: connects-to
    note: "Enteroviruses inflame the nervous system: Coxsackie and other enteroviruses are leading causes of viral (aseptic) meningitis and can cause encephalitis and acute flaccid paralysis."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "The brain is built from dietary fat: docosahexaenoic acid (DHA), an omega-3, is the dominant structural fatty acid of neuronal membranes, essential for brain development and function."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "Drugs reshape its chemistry: SSRIs like fluoxetine raise synaptic serotonin to treat depression and anxiety, exemplifying how the nervous system is modulated pharmacologically."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "Motor neurons degenerate: amyotrophic lateral sclerosis progressively destroys upper and lower motor neurons of the nervous system, causing relentless paralysis while sparing sensation and cognition until late."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "A virus that invades the brain: HIV enters the central nervous system early, infecting microglia and macrophages to cause HIV encephalitis and the cognitive decline of HIV-associated neurocognitive disorder."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids quiet neuro-inflammation: corticosteroids reduce cerebral oedema around tumours, treat acute multiple-sclerosis relapses and autoimmune encephalitis, a mainstay across inflammatory nervous-system disease."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Its reach beyond the brain and cord: the peripheral nerves carry the nervous system's motor commands out to muscle and sensory signals back in, and their axons—wrapped in Schwann-cell myelin—are where neuropathies and nerve injuries strike."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: connects-to
    note: "Where nerve commands muscle: the neuromuscular junction is the cholinergic synapse through which the nervous system drives every voluntary movement, the target of myasthenia gravis, botulinum toxin and curare."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "A hereditary neurodegeneration of the nervous system: Huntington's disease, from a CAG-repeat expansion in HTT, destroys striatal neurons to cause chorea, cognitive decline and psychiatric change—one of the system's monogenic degenerative diseases."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "The plasticity neurotrophin: brain-derived neurotrophic factor supports neuron survival and synaptic plasticity, the molecular substrate of learning and a node where exercise, stress and antidepressants converge on the nervous system."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The seat of memory: the hippocampus encodes new memories and is one of the few sites of adult neurogenesis, selectively vulnerable to Alzheimer's, ischaemia and chronic stress."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "When the wiring itself hurts: damage to the nervous system's own pain pathways produces neuropathic pain, a maladaptive output of an injured nervous system distinct from ordinary nociceptive pain."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Sleep is a brain state: narcolepsy is a focal nervous-system disease in which loss of hypothalamic orexin neurons destabilises the sleep-wake switch, intruding REM and cataplexy into waking life."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut-brain axis: the nervous system is in constant two-way dialogue with the gut microbiome via the vagus nerve, immune signalling and microbial metabolites, shaping mood, appetite and even neurodegeneration."
  - target: 02-pathogen/04-parasites/plasmodium-falciparum
    relation: connects-to
    note: "Cerebral malaria: Plasmodium falciparum sequesters in the brain's microvasculature, causing the coma and seizures of cerebral malaria—one of the deadliest infections of the nervous system worldwide."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Long-distance logistics: fast axonal transport along microtubules ferries cargo across the vast lengths of neurons, and its failure underlies many neurodegenerative and peripheral nerve diseases."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "A window on the brain: the retina and optic nerve are direct extensions of the central nervous system, so the eye reveals neurological disease and shares its developmental and degenerative biology."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "Retrograde neuromodulation: the endocannabinoid system acts as a widespread retrograde messenger that tunes synaptic transmission throughout the nervous system."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Pain neurotransmission: substance P is a key neuropeptide of nociceptive signalling in the nervous system, transmitting pain from sensory neurons to the spinal cord and brain."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Sensory neuropeptide: CGRP, released by sensory neurons, mediates pain and neurogenic vasodilation, a nervous-system signal central to migraine and now targeted by CGRP-blocking drugs."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Sleep and inhibition: adenosine accumulates with neural activity to promote sleep pressure and dampen neurotransmission, the brake that caffeine blocks to sustain wakefulness."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian output: the pineal gland of the nervous system secretes melatonin under suprachiasmatic-nucleus control, the hormonal signal that entrains the body's circadian rhythm to the light-dark cycle."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Purinergic signalling and energy: ATP serves both as the brain's principal energy currency and as a fast purinergic co-transmitter and glial signalling molecule across the nervous system."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Neurovascular unit: VEGF couples blood-vessel growth to the nervous system, maintaining the cerebral microvasculature and blood-brain barrier and supporting adult neurogenesis."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophin receptors: the Trk family of receptors transduces BDNF, NGF and other neurotrophin signals that govern neuronal survival, differentiation and synaptic plasticity throughout the developing and adult nervous system."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Central neuropeptide: oxytocin acts as a neuromodulator in the brain shaping social behaviour, bonding and stress responses, alongside its classic neurohypophyseal hormonal release, a window onto the nervous system's endocrine reach."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Synaptic pruning: complement C3 tags weak synapses for elimination by microglia, the developmental sculpting of neural circuits whose reactivation contributes to the synapse loss of neurodegenerative disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Excitation and transmission: calcium influx triggers neurotransmitter-vesicle fusion at the synapse and shapes neuronal excitability and plasticity, the ion that converts an electrical action potential into the chemical signalling on which the nervous system runs."
  - target: 01-human/03-molecular/aquaporin-4
    relation: connects-to
    note: "Glymphatic clearance: aquaporin-4 water channels on astrocyte endfeet drive the glymphatic flow that washes metabolic waste — including amyloid — from the brain during sleep, the CNS's fluid-clearance system in place of conventional lymphatics."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Neuroimmune surveillance: microglia and border-associated macrophages present antigen on MHC class II within the CNS, the neuroimmune interface whose dysregulation links the nervous and immune systems in neuroinflammatory and neurodegenerative disease."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Endogenous opioid system: the mu-opioid receptor transduces the endorphin and enkephalin signals that modulate pain and reward, a core neuromodulatory system of the nervous system and the target of opioid analgesics."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Arousal switch: hypothalamic orexin (hypocretin) neurons stabilise wakefulness and gate the sleep-wake transition, the arousal system whose loss causes narcolepsy."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Stress neuroendocrine link: hypothalamic CRH initiates the neuroendocrine stress response, the bridge by which the nervous system drives the HPA axis and cortisol (mapped) output."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Synaptic plasticity: mTOR signalling governs the activity-dependent protein synthesis underlying synaptic plasticity, neuronal growth, and the developmental wiring of the nervous system."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Plasticity signal transduction: ERK-MAPK signalling, engaged downstream of neurotrophin (BDNF-TrkB) and neurotransmitter receptors (both mapped), transduces neuronal activity into the gene expression of long-term plasticity and memory."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Microglial surveillance: microglial TLR4 innate sensing surveys the CNS for danger signals, initiating the neuroinflammatory responses that shape both defence and disease in the nervous system."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (mTOR mapped) is a central survival and growth pathway for neurons, governing plasticity and the response to neurotrophins (BDNF/NTRK mapped)."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 is a key effector of the neuroinflammatory responses that shape injury and disease across the nervous system."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β is a pivotal neuronal kinase regulating synaptic plasticity, neuronal polarity and survival, and a target of the mood-stabiliser lithium."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 drives the reactive astrogliosis and glial-scar formation that are a core response to injury across the nervous system."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING sensing of cytosolic and mitochondrial DNA links neuronal damage to the innate neuroinflammation common to neurodegeneration and CNS injury."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling drives the interferon-responsive microglial activation that shapes neuroinflammation across the nervous system."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate neuronal oxidative-stress defense, autophagy, and metabolic homeostasis across the nervous system."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α couples the neuronal and glial responses to hypoxic and metabolic stress across the nervous system."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation shared across nervous-system disorders."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of neurotrophin-TrkB (BDNF and NTRK already mapped), governs the neuronal survival and synaptic plasticity of the nervous system."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB signaling in neurons and glia regulates the neuroinflammatory and synaptic-plasticity responses of the nervous system."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK integrates the energy status of neurons and glia to their metabolic and autophagic homeostasis across the nervous system."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the neuronal proteostasis and synaptic homeostasis of the nervous system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of neurotrophin and glutamate receptors participates in the synaptic plasticity of the nervous system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of neuronal identity and synaptic-plasticity gene expression of the nervous system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven chemokine signaling participates in the neuroimmune trafficking and microglial responses of the nervous system."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neural-progenitor migration and neuroimmune interactions of the nervous system."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the glial and neuroinflammatory responses of the nervous system."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β signaling participates in the neuroinflammatory responses of the nervous system."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the neuroinflammatory and neuromodulatory responses of the nervous system."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammatory responses of the nervous system."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Repolarisation and resting potential: potassium efflux through voltage-gated and leak channels repolarises the neuron after each action potential and sets the resting membrane potential, complementing the sodium influx (already mapped) that fires the nervous system."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "NMDA-receptor gate: magnesium blocks the NMDA glutamate receptor at rest, and its voltage-dependent removal makes the receptor a coincidence detector, a mechanism central to the synaptic plasticity and learning of the nervous system."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Synaptic modulation: zinc is co-released with glutamate (already mapped) at many synapses and modulates NMDA and other receptors, a trace-metal neuromodulator important to signalling and to neural development."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Pain and fever: prostaglandins sensitise nociceptors and act on the hypothalamus to raise the temperature set-point, the eicosanoid signalling through which the nervous system generates pain and fever, targeted by NSAIDs."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Neuroinflammation and plasticity: TNF from glia (IL-6 and IL-1 already mapped) both drives neuroinflammation and, at low levels, tunes synaptic strength through homeostatic scaling, a cytokine link between the immune and nervous systems."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Gut-brain axis: GLP-1 acts on receptors in the hypothalamus and brainstem to signal satiety and modulate reward (leptin and insulin already mapped), a gut-derived hormone integrated by the nervous system to regulate feeding."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Sympathetic medulla: the adrenal medulla is a modified sympathetic ganglion of the nervous system, releasing adrenaline and noradrenaline (norepinephrine already mapped) into the blood as the hormonal arm of the fight-or-flight response."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Autonomic cardiac control: the sympathetic and parasympathetic nerves of the autonomic nervous system control the heart rate and contractility (noradrenaline and acetylcholine already mapped), the neural regulation of the circulation."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Somatosensory innervation: the skin is densely innervated with the sensory receptors and free nerve endings (substance P and CGRP already mapped) that convey touch, temperature and pain to the central nervous system."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Microglial polarisation: IL-4 polarises the microglia (already mapped) toward an anti-inflammatory M2 phenotype, the neuroimmune arm that shapes neural repair and the resolution of neuroinflammation in the nervous system."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Synaptic zinc: zinc is co-released with glutamate (already mapped) at many excitatory synapses, where it modulates the NMDA receptors and synaptic plasticity, a signalling trace metal of the nervous system."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Neuroimmune interface: the nervous and immune systems signal bidirectionally — the microglia (already mapped), the neuroinflammation (TNF, IL-1 and IL-6 already mapped) and the neural control of immunity — a deep integration of the two systems."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Inhibitory signalling: the chloride influx through the GABA-A (GABA already mapped) and glycine receptors hyperpolarises the neurons, the fundamental inhibitory signal of the nervous system."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Neuropeptide Y: NPY is an abundant CNS neuropeptide regulating the appetite (leptin already mapped), anxiety and autonomic function of the nervous system."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Gut-brain appetite hormone: ghrelin acts on the hypothalamic appetite circuits and the reward pathways of the nervous system, linking the gut hormone to the central control of feeding."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmune: IL-13, with IL-4 (already mapped), is part of the type-2 neuroimmune signalling at the interface of the immune system and the nervous system."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "CNS interferon: the type-I interferon defends the nervous system against the neurotropic viruses, and its dysregulation causes the interferonopathies affecting the brain."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Neuroinflammatory Th1: the IFN-γ of the infiltrating T cells drives the Th1 neuroinflammation (TNF and IL-1 already mapped) implicated in the neurological disease of the nervous system."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the neuroinflammation implicated in the neurological disease of the nervous system."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammation of the autoimmune and demyelinating diseases of the nervous system."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune balance of the nervous system."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 dimension of the neuroimmune balance of the nervous system."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CNS-border cytotoxicity: the cytotoxic T cells (perforin already mapped) of the meningeal and perivascular compartments mediate the adaptive neuroinflammation of the nervous system."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS antigen presentation: the dendritic cells of the meninges and choroid plexus present antigen to the T cells (already mapped) at the borders of the nervous system."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Border-associated macrophages: the CNS-border and perivascular macrophages, alongside the microglia (already mapped), form the myeloid immune interface of the nervous system."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) activation and the complement-mediated synaptic pruning of the nervous system."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the innate complement arm of the neuroinflammation of the nervous system."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuroimmune alarmin: TSLP released at the mucosal and peripheral immune interfaces activates the neuroimmune axis via vagal afferents and dural immune cells; TSLP-driven type-2 signals modulate the glial (already mapped) and microglial response of the central nervous system."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotection: erythropoietin (EPO) receptors on neurons and astrocytes (already mapped) mediate JAK2/STAT5 anti-apoptotic survival signalling; EPO is neuroprotective in hypoxic-ischaemic injury, stroke (already mapped) and neurodegenerative diseases of the nervous system."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Pain nociception: bradykinin is the canonical peripheral pain mediator; B2 receptor activation on sensory neurons amplifies prostaglandin-driven neuroinflammation (already mapped) and is the molecular basis of acute and chronic nociception in the peripheral nervous system."
---

# Nervous System

## Overview

The nervous system is the **master regulatory and integrative system** of the human body — responsible for detecting stimuli from the internal and external environment, processing and integrating that information, and coordinating appropriate responses ranging from voluntary skeletal muscle movement to unconscious visceral homeostasis. It is the biological substrate of all perception, thought, emotion, language, and behavior.

Broadly organized into two anatomical divisions — the **Central Nervous System (CNS)** and the **Peripheral Nervous System (PNS)** — the nervous system comprises the brain, spinal cord, 12 pairs of cranial nerves, 31 pairs of spinal nerves, and extensive networks of autonomic ganglia and plexuses distributed throughout the body. Together these structures contain approximately **86 billion neurons** in the brain alone [^kandel-principles-ns], with additional hundreds of millions in the spinal cord, enteric system, and peripheral ganglia.

Neurological and psychiatric disorders constitute the **leading cause of disability** and the second leading cause of death globally — affecting over 1 billion people according to the World Health Organization [^who-neurological-2006]. The nervous system's central role in virtually all physiological functions means that neurological disease has cascading consequences across every organ system.

## Structure

### Central Nervous System (CNS)

The CNS consists of the **brain** and **spinal cord**, enclosed and protected by the bony skull and vertebral column, the three-layer meninges (dura mater, arachnoid mater, pia mater), and the cerebrospinal fluid (CSF) that circulates in the subarachnoid space and ventricular system.

**Brain** (~1.4 kg): Cerebral cortex (4 lobes × 2 hemispheres), subcortical structures (basal ganglia, hippocampus, amygdala, thalamus, hypothalamus), cerebellum, and brainstem. See the [brain](../../06-organ/brain/README.md) entry for full detail.

**Spinal cord** (~45 cm, ~30 g): A segmented cylindrical structure (31 segments: 8 cervical, 12 thoracic, 5 lumbar, 5 sacral, 1 coccygeal). Cross-section shows butterfly-shaped **gray matter** (dorsal horn: sensory processing; ventral horn: lower motor neurons; lateral horn: sympathetic preganglionic neurons in T1–L2/L3) surrounded by **white matter** (ascending sensory tracts: spinothalamic, dorsal columns; descending motor tracts: corticospinal, rubrospinal, vestibulospinal).

### Peripheral Nervous System (PNS)

Everything outside the skull and vertebral canal — the nerves, ganglia, and sensory receptors that connect the CNS to the body.

**Somatic PNS:**
- **Afferent (sensory):** Dorsal root ganglia neurons carry signals from skin (mechanoreceptors, thermoreceptors, nociceptors), muscle spindles, Golgi tendon organs, and joints → spinal cord dorsal horn or brainstem.
- **Efferent (motor):** Lower motor neurons (alpha motor neurons in ventral horn) → neuromuscular junction → skeletal muscle (voluntary movement).

**Autonomic Nervous System (ANS):**

| Division | Ganglia location | Transmitter (pre/post) | Effect on target organs |
|:---|:---|:---|:---|
| **Sympathetic** | Paravertebral chain ganglia (T1–L2/3) | ACh (preganglionic) / NE (postganglionic) | Fight-or-flight: ↑HR, ↑BP, bronchodilation, ↓GI motility, pupil dilation, adrenal catecholamine release |
| **Parasympathetic** | Terminal ganglia near or within target organ | ACh / ACh | Rest-and-digest: ↓HR, ↑GI motility, bronchoconstriction, pupil constriction, bladder/bowel contraction, erection |
| **Enteric** | Myenteric (Auerbach's) plexus + submucosal (Meissner's) plexus | Multiple (ACh, NO, serotonin, VIP, substance P) | Semi-autonomous GI motility, secretion, blood flow; ~500 million neurons — the "gut brain" |

### Nerve fiber classification

| Fiber class | Myelin | Diameter | Conduction velocity | Sensory modality |
|:---|:---|:---|:---|:---|
| **Aα** | Heavily myelinated | 13–20 μm | 70–120 m/s | Proprioception (muscle spindle Ia, Ib), motor efferents |
| **Aβ** | Myelinated | 6–12 μm | 30–70 m/s | Touch, pressure, vibration |
| **Aδ** | Lightly myelinated | 1–5 μm | 5–30 m/s | Fast/sharp pain; cold thermoreception |
| **C** | Unmyelinated | 0.2–1.5 μm | 0.5–2 m/s | Slow/burning pain, warmth, itch, autonomic postganglionic |

### Glial cells

Non-neuronal support cells outnumber neurons approximately 1:1 in the brain:

| Glia | Location | Function |
|:---|:---|:---|
| **Astrocytes** | CNS | Metabolic support; BBB formation; K⁺ and glutamate buffering; tripartite synapse participant; reactive gliosis |
| **Oligodendrocytes** | CNS | Myelin production (one oligo myelinates up to 50 axon segments) |
| **Microglia** | CNS | Resident immune cells; synaptic pruning; phagocytosis; neuroinflammation |
| **Schwann cells** | PNS | Myelin for single PNS axon segments; guide axon regeneration |
| **Satellite glia** | PNS ganglia | Support and modulate sensory and autonomic neurons |

## Function

### Sensorimotor integration

The nervous system's fundamental function is the **sensorimotor loop**: sense → integrate → respond. At the simplest level, the monosynaptic stretch reflex (patellar tendon reflex) completes this loop in the spinal cord within ~25–50 ms. At the most complex level, the entirety of cortical processing, memory retrieval, planning, and learned motor skill underlies a skilled voluntary action.

**Sensory processing** is hierarchical: primary sensory areas (S1, V1, A1) represent basic features; secondary and association areas (STS, PPC, PFC) build increasingly abstract representations. The somatosensory homunculus in S1 represents the body surface with cortical area proportional to tactile receptor density (fingertips and lips are disproportionately large).

**Motor control** uses parallel hierarchical pathways: cortex (planning) → brainstem (postural reflexes) → spinal cord (pattern generators) → muscle. The cerebellum provides real-time error correction; the basal ganglia select and gate which motor program executes.

### Autonomic and homeostatic control

The hypothalamus is the **supreme autonomic center**: it integrates hormonal signals (leptin, ghrelin, cortisol), temperature information, and limbic inputs to coordinate sympathetic/parasympathetic balance, HPA axis activity, circadian rhythms (via the suprachiasmatic nucleus), and hunger/satiety. The **nucleus tractus solitarius (NTS)** in the medulla processes baroreceptor, chemoreceptor, and visceral afferent inputs, providing the primary interface between peripheral autonomic signals and CNS integration.

The **baroreceptor reflex** — a classic example of autonomic homeostasis — continuously monitors carotid sinus and aortic arch pressure, feeding back via cranial nerves IX and X to the NTS, which adjusts sympathetic outflow to heart and vasculature to maintain arterial blood pressure within narrow bounds (~120/80 mmHg).

### Higher cognitive functions

Distributed cortical networks underlie language (Broca's area, Wernicke's area, arcuate fasciculus), spatial attention (right parietal), face recognition (fusiform face area), emotion regulation (PFC-amygdala circuit), and social cognition (mirror neuron system, temporoparietal junction). The integration of these networks, coordinated through synchronized oscillations and the thalamic "broadcasting" function, gives rise to the unified experience of consciousness.

## Connections

- `part-of` → **[human-body](../../08-whole-body/human-body/README.md)** — the nervous system is one of the 11 major organ systems
- `contains` → **[brain](../../06-organ/brain/README.md)** — the brain is the primary CNS organ
- `contains` → **[neuron](../../04-cellular/neuron/README.md)** — neurons are the functional units throughout the nervous system
- `contains` → **[dopamine](../../03-molecular/dopamine/README.md)** — dopaminergic circuits operate within CNS pathways
- `contains` → **[glutamate](../../03-molecular/glutamate/README.md)** — glutamate is the CNS's dominant excitatory transmitter
- `contains` → **[gaba](../../03-molecular/gaba/README.md)** — GABA is the CNS's dominant inhibitory transmitter
- `connects-to` → **[cardiovascular-system](../../07-system/cardiovascular-system/README.md)** — autonomic nervous system governs cardiac rate, contractility, and vascular tone; the baroreceptor reflex and cerebral autoregulation link the two systems bidirectionally
- `damaged-by` → **[Prion Protein (PrP)](../../../02-pathogen/05-prions/prion-protein/README.md)** — PrPSc spreads via axonal transport along synaptic networks; spongiform vacuolation propagates through thalamus (FFI), cerebellar cortex (GSS), and cerebral cortex + basal ganglia (sCJD); no disease-modifying treatment exists.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — The synapse is where the nervous system computes: chemical and electrical junctions between neurons transmit and weight signals, and their plasticity underlies learning, memory, and the disorders that disrupt connectivity.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sodium carries the nerve impulse: the inrush of sodium ions through voltage-gated channels generates the action potential, the electrical signal on which all nervous-system communication depends.
- `connects-to` → **[Stroke](../stroke/README.md)** — Stroke is the nervous system starved of blood: a blocked or burst cerebral vessel kills neurons within minutes, the leading cause of acquired neurological disability and a prime example of the brain's dependence on its circulation.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — The commonest way the nervous system degenerates: Alzheimer's disease destroys cortical and hippocampal neurons through amyloid and tau pathology, the leading cause of dementia and the archetypal neurodegenerative disease.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — A movement disorder of dying neurons: Parkinson's disease kills the dopaminergic neurons of the substantia nigra through α-synuclein pathology, the second commonest neurodegenerative disease of the nervous system.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — Autoimmunity strips the nervous system's insulation: multiple sclerosis is an immune attack on central myelin, the leading non-traumatic cause of neurological disability in young adults.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Hyperexcitable circuits misfire: epilepsy is the nervous system's paroxysmal disorder, in which synchronized neuronal discharge produces seizures, arising from injury, tumor, malformation or channel dysfunction.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — Its own glia turn malignant: glioblastoma is the commonest and deadliest primary brain cancer, arising from the astrocytic support cells of the nervous system and diffusely infiltrating the brain.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Mood is a function of its circuits: major depression reflects dysregulation across the monoaminergic and limbic networks of the nervous system, the neurobiological basis of a leading cause of disability.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It runs a second brain in the gut: the enteric nervous system governs motility and secretion, and the bidirectional gut-brain axis links nervous-system signalling to digestion, microbiome and mood.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Nerves and immunity converse constantly: the nervous system shapes inflammation through the vagal cholinergic anti-inflammatory pathway and sympathetic tone, while neuroinflammation in turn drives neurological disease.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — A classic assault on its protective membranes: Neisseria meningitidis crosses into the cerebrospinal fluid to cause acute bacterial meningitis, inflaming the meninges that sheath the brain and spinal cord.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It drives every breath: brainstem respiratory centres set the rhythm of breathing and the diaphragm obeys the phrenic nerve, so brainstem injury, high spinal cord damage and neuromuscular disease cause respiratory failure.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It governs the bladder: the autonomic and somatic innervation of the bladder coordinates storage and voiding, so spinal cord and autonomic injury cause neurogenic bladder with retention and incontinence.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The brain has its own drainage: the glymphatic system and meningeal lymphatic vessels clear waste and immune cells from the central nervous system, a route increasingly tied to neurodegeneration.
- `connects-to` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — A common virus can inflame the brain: herpes simplex is the leading cause of sporadic viral encephalitis, with a predilection for the temporal lobes, and varicella-zoster causes the painful neuralgia of shingles.
- `connects-to` → **[Measles Virus](../../../02-pathogen/01-viruses/measles-virus/README.md)** — Measles can smoulder in the brain for years: subacute sclerosing panencephalitis is a fatal degenerative brain disease emerging years after measles infection, from persistent virus in neurons.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Tuberculosis can besiege the meninges: tuberculous meningitis is a slow, devastating infection of the basal meninges causing cranial nerve palsies, hydrocephalus and stroke.
- `connects-to` → **[Coxsackievirus B](../../../02-pathogen/01-viruses/coxsackievirus-b/README.md)** — Enteroviruses inflame the nervous system: Coxsackie and other enteroviruses are leading causes of viral (aseptic) meningitis and can cause encephalitis and acute flaccid paralysis.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — The brain is built from dietary fat: docosahexaenoic acid (DHA), an omega-3, is the dominant structural fatty acid of neuronal membranes, essential for brain development and function.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — Drugs reshape its chemistry: SSRIs like fluoxetine raise synaptic serotonin to treat depression and anxiety, exemplifying how the nervous system is modulated pharmacologically.
- `connects-to` → **[ALS](../../07-system/als/README.md)** — Motor neurons degenerate: amyotrophic lateral sclerosis progressively destroys upper and lower motor neurons of the nervous system, causing relentless paralysis while sparing sensation and cognition until late.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — A virus that invades the brain: HIV enters the central nervous system early, infecting microglia and macrophages to cause HIV encephalitis and the cognitive decline of HIV-associated neurocognitive disorder.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids quiet neuro-inflammation: corticosteroids reduce cerebral oedema around tumours, treat acute multiple-sclerosis relapses and autoimmune encephalitis, a mainstay across inflammatory nervous-system disease.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Its reach beyond the brain and cord: the peripheral nerves carry the nervous system's motor commands out to muscle and sensory signals back in, and their axons—wrapped in Schwann-cell myelin—are where neuropathies and nerve injuries strike.
- `connects-to` → **[Neuromuscular Junction](../../05-tissue/neuromuscular-junction/README.md)** — Where nerve commands muscle: the neuromuscular junction is the cholinergic synapse through which the nervous system drives every voluntary movement, the target of myasthenia gravis, botulinum toxin and curare.
- `connects-to` → **[Huntington's Disease](../huntingtons-disease/README.md)** — A hereditary neurodegeneration of the nervous system: Huntington's disease, from a CAG-repeat expansion in HTT, destroys striatal neurons to cause chorea, cognitive decline and psychiatric change—one of the system's monogenic degenerative diseases.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — The plasticity neurotrophin: brain-derived neurotrophic factor supports neuron survival and synaptic plasticity, the molecular substrate of learning and a node where exercise, stress and antidepressants converge on the nervous system.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The seat of memory: the hippocampus encodes new memories and is one of the few sites of adult neurogenesis, selectively vulnerable to Alzheimer's, ischaemia and chronic stress.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — When the wiring itself hurts: damage to the nervous system's own pain pathways produces neuropathic pain, a maladaptive output of an injured nervous system distinct from ordinary nociceptive pain.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Sleep is a brain state: narcolepsy is a focal nervous-system disease in which loss of hypothalamic orexin neurons destabilises the sleep-wake switch, intruding REM and cataplexy into waking life.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut-brain axis: the nervous system is in constant two-way dialogue with the gut microbiome via the vagus nerve, immune signalling and microbial metabolites, shaping mood, appetite and even neurodegeneration.
- `connects-to` → **[Plasmodium falciparum](../../../02-pathogen/04-parasites/plasmodium-falciparum/README.md)** — Cerebral malaria: Plasmodium falciparum sequesters in the brain's microvasculature, causing the coma and seizures of cerebral malaria—one of the deadliest infections of the nervous system worldwide.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Long-distance logistics: fast axonal transport along microtubules ferries cargo across the vast lengths of neurons, and its failure underlies many neurodegenerative and peripheral nerve diseases.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — A window on the brain: the retina and optic nerve are direct extensions of the central nervous system, so the eye reveals neurological disease and shares its developmental and degenerative biology.
- `connects-to` → **[Endocannabinoid](../../03-molecular/endocannabinoid/README.md)** — Retrograde neuromodulation: the endocannabinoid system acts as a widespread retrograde messenger that tunes synaptic transmission throughout the nervous system.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Pain neurotransmission: substance P is a key neuropeptide of nociceptive signalling in the nervous system, transmitting pain from sensory neurons to the spinal cord and brain.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Sensory neuropeptide: CGRP, released by sensory neurons, mediates pain and neurogenic vasodilation, a nervous-system signal central to migraine and now targeted by CGRP-blocking drugs.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Sleep and inhibition: adenosine accumulates with neural activity to promote sleep pressure and dampen neurotransmission, the brake that caffeine blocks to sustain wakefulness.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian output: the pineal gland of the nervous system secretes melatonin under suprachiasmatic-nucleus control, the hormonal signal that entrains the body's circadian rhythm to the light-dark cycle.
- `connects-to` → **[ATP](../../03-molecular/atp/README.md)** — Purinergic signalling and energy: ATP serves both as the brain's principal energy currency and as a fast purinergic co-transmitter and glial signalling molecule across the nervous system.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Neurovascular unit: VEGF couples blood-vessel growth to the nervous system, maintaining the cerebral microvasculature and blood-brain barrier and supporting adult neurogenesis.
- `connects-to` → **[NTRK / Trk](../../03-molecular/ntrk/README.md)** — The Trk family of receptors transduces BDNF, NGF, and other neurotrophin signals that govern neuronal survival, differentiation, and synaptic plasticity throughout the developing and adult nervous system.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Oxytocin acts as a neuromodulator in the brain shaping social behavior, bonding, and stress responses, alongside its classic neurohypophyseal hormonal release—a window onto the nervous system's endocrine reach.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 tags weak synapses for elimination by microglia, the developmental synaptic pruning that sculpts neural circuits—and whose pathological reactivation contributes to the synapse loss of neurodegenerative disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium influx triggers neurotransmitter-vesicle fusion at the synapse and shapes neuronal excitability and plasticity, the ion that converts an electrical action potential into the chemical signaling on which the nervous system runs.
- `connects-to` → **[Aquaporin-4](../../03-molecular/aquaporin-4/README.md)** — Aquaporin-4 water channels on astrocyte endfeet drive the glymphatic flow that washes metabolic waste—including amyloid—from the brain during sleep, the CNS's fluid-clearance system in place of conventional lymphatics.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Microglia and border-associated macrophages present antigen on MHC class II within the CNS, the neuroimmune interface whose dysregulation links the nervous and immune systems in neuroinflammatory and neurodegenerative disease.
- `connects-to` → **[Mu-Opioid Receptor](../../03-molecular/mu-opioid-receptor/README.md)** — The mu-opioid receptor transduces the endorphin and enkephalin signals that modulate pain and reward, a core neuromodulatory system of the nervous system and the target of opioid analgesics.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Hypothalamic orexin (hypocretin) neurons stabilize wakefulness and gate the sleep-wake transition, the arousal system whose loss causes narcolepsy.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Hypothalamic CRH initiates the neuroendocrine stress response, the bridge by which the nervous system drives the HPA axis and cortisol (mapped) output.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling governs the activity-dependent protein synthesis underlying synaptic plasticity, neuronal growth, and the developmental wiring of the nervous system.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling, engaged downstream of neurotrophin (BDNF-TrkB) and neurotransmitter receptors (both mapped), transduces neuronal activity into the gene expression of long-term plasticity and memory.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Microglial TLR4 innate sensing surveys the CNS for danger signals, initiating the neuroinflammatory responses that shape both defense and disease in the nervous system.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-mTOR signaling (mTOR mapped) is a central survival and growth pathway for neurons, governing plasticity and the response to neurotrophins (BDNF/NTRK mapped).
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 is a key effector of the neuroinflammatory responses that shape injury and disease across the nervous system.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β is a pivotal neuronal kinase regulating synaptic plasticity, neuronal polarity and survival, and a target of the mood-stabilizer lithium.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 drives the reactive astrogliosis and glial-scar formation that are a core response to injury across the nervous system.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — cGAS-STING sensing of cytosolic and mitochondrial DNA links neuronal damage to the innate neuroinflammation common to neurodegeneration and CNS injury.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling drives the interferon-responsive microglial activation that shapes neuroinflammation across the nervous system.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate neuronal oxidative-stress defense, autophagy, and metabolic homeostasis across the nervous system.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α couples the neuronal and glial responses to hypoxic and metabolic stress across the nervous system.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation shared across nervous-system disorders.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of neurotrophin-TrkB (BDNF and NTRK already mapped), governs the neuronal survival and synaptic plasticity of the nervous system.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB signaling in neurons and glia regulates the neuroinflammatory and synaptic-plasticity responses of the nervous system.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK integrates the energy status of neurons and glia to their metabolic and autophagic homeostasis across the nervous system.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy maintains the neuronal proteostasis and synaptic homeostasis of the nervous system.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of neurotrophin and glutamate receptors participates in the synaptic plasticity of the nervous system.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of neuronal identity and synaptic-plasticity gene expression of the nervous system.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven chemokine signaling participates in the neuroimmune trafficking and microglial responses of the nervous system.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neural-progenitor migration and neuroimmune interactions of the nervous system.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the glial and neuroinflammatory responses of the nervous system.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β signaling participates in the neuroinflammatory responses of the nervous system.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the neuroinflammatory and neuromodulatory responses of the nervous system.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammatory responses of the nervous system.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Repolarisation and resting potential: potassium efflux through voltage-gated and leak channels repolarises the neuron after each action potential and sets the resting membrane potential, complementing the sodium influx (already mapped) that fires the nervous system.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — NMDA-receptor gate: magnesium blocks the NMDA glutamate receptor at rest, and its voltage-dependent removal makes the receptor a coincidence detector, a mechanism central to the synaptic plasticity and learning of the nervous system.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Synaptic modulation: zinc is co-released with glutamate (already mapped) at many synapses and modulates NMDA and other receptors, a trace-metal neuromodulator important to signalling and to neural development.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Pain and fever: prostaglandins sensitise nociceptors and act on the hypothalamus to raise the temperature set-point, the eicosanoid signalling through which the nervous system generates pain and fever, targeted by NSAIDs.
- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — Neuroinflammation and plasticity: TNF from glia (IL-6 and IL-1 already mapped) both drives neuroinflammation and, at low levels, tunes synaptic strength through homeostatic scaling, a cytokine link between the immune and nervous systems.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Gut-brain axis: GLP-1 acts on receptors in the hypothalamus and brainstem to signal satiety and modulate reward (leptin and insulin already mapped), a gut-derived hormone integrated by the nervous system to regulate feeding.
- `connects-to` → **[Adrenal gland](../../06-organ/adrenal-gland/README.md)** — Sympathetic medulla: the adrenal medulla is a modified sympathetic ganglion of the nervous system, releasing adrenaline and noradrenaline (norepinephrine already mapped) into the blood as the hormonal arm of the fight-or-flight response.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Autonomic cardiac control: the sympathetic and parasympathetic nerves of the autonomic nervous system control the heart rate and contractility (noradrenaline and acetylcholine already mapped), the neural regulation of the circulation.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Somatosensory innervation: the skin is densely innervated with the sensory receptors and free nerve endings (substance P and CGRP already mapped) that convey touch, temperature and pain to the central nervous system.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Microglial polarisation: IL-4 polarises the microglia (already mapped) toward an anti-inflammatory M2 phenotype, the neuroimmune arm that shapes neural repair and the resolution of neuroinflammation in the nervous system.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Synaptic zinc: zinc is co-released with glutamate (already mapped) at many excitatory synapses, where it modulates the NMDA receptors and synaptic plasticity, a signalling trace metal of the nervous system.
- `connects-to` → **[Immune system](../immune-system/README.md)** — Neuroimmune interface: the nervous and immune systems signal bidirectionally — the microglia (already mapped), the neuroinflammation (TNF, IL-1 and IL-6 already mapped) and the neural control of immunity — a deep integration of the two systems.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Inhibitory signalling: the chloride influx through the GABA-A (GABA already mapped) and glycine receptors hyperpolarises the neurons, the fundamental inhibitory signal of the nervous system.
- `connects-to` → **[NPY](../../03-molecular/npy/README.md)** — Neuropeptide Y: NPY is an abundant CNS neuropeptide regulating the appetite (leptin already mapped), anxiety and autonomic function of the nervous system.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Gut-brain appetite hormone: ghrelin acts on the hypothalamic appetite circuits and the reward pathways of the nervous system, linking the gut hormone to the central control of feeding.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmune: IL-13, with IL-4 (already mapped), is part of the type-2 neuroimmune signalling at the interface of the immune system and the nervous system.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — CNS interferon: the type-I interferon defends the nervous system against the neurotropic viruses, and its dysregulation causes the interferonopathies affecting the brain.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Neuroinflammatory Th1: the IFN-γ of the infiltrating T cells drives the Th1 neuroinflammation (TNF and IL-1 already mapped) implicated in the neurological disease of the nervous system.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the neuroinflammation implicated in the neurological disease of the nervous system.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammation of the autoimmune and demyelinating diseases of the nervous system.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune balance of the nervous system.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 dimension of the neuroimmune balance of the nervous system.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CNS-border cytotoxicity: the cytotoxic T cells (perforin already mapped) of the meningeal and perivascular compartments mediate the adaptive neuroinflammation of the nervous system.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS antigen presentation: the dendritic cells of the meninges and choroid plexus present antigen to the T cells (already mapped) at the borders of the nervous system.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Border-associated macrophages: the CNS-border and perivascular macrophages, alongside the microglia (already mapped), form the myeloid immune interface of the nervous system.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) activation and the complement-mediated synaptic pruning of the nervous system.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the innate complement arm of the neuroinflammation of the nervous system.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuroimmune alarmin: TSLP released at the mucosal and peripheral immune interfaces activates the neuroimmune axis via vagal afferents and dural immune cells; TSLP-driven type-2 signals modulate the glial (already mapped) and microglial response of the central nervous system.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotection: erythropoietin (EPO) receptors on neurons and astrocytes (already mapped) mediate JAK2/STAT5 anti-apoptotic survival signalling; EPO is neuroprotective in hypoxic-ischaemic injury, stroke (already mapped) and neurodegenerative diseases of the nervous system.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Pain nociception: bradykinin is the canonical peripheral pain mediator; B2 receptor activation on sensory neurons amplifies prostaglandin-driven neuroinflammation (already mapped) and is the molecular basis of acute and chronic nociception in the peripheral nervous system.

## Pathology

| Disease | CNS/PNS | Mechanism | Global burden |
|:---|:---|:---|:---|
| **Alzheimer's disease** | CNS | Amyloid-β + tau aggregation → synaptic loss → cortical and hippocampal neurodegeneration | ~50 million affected; >$1 trillion annual cost |
| **Parkinson's disease** | CNS | Selective SNc dopaminergic neuron loss → nigrostriatal pathway failure → basal ganglia circuit dysfunction | ~10 million; 2nd most common neurodegenerative disease |
| **Stroke** | CNS | Ischemic or hemorrhagic → focal neuronal death → acute neurological deficit | ~15 million/year; #2 cause of death globally |
| **Multiple sclerosis (MS)** | CNS | Autoimmune demyelination of CNS white matter tracts → conduction failure and neurodegeneration | ~2.8 million worldwide; peak onset 20–40 yr |
| **ALS** | CNS/PNS | Progressive degeneration of upper and lower motor neurons → paralysis, respiratory failure | ~300,000 globally; median survival ~2–4 yr |
| **Epilepsy** | CNS | Recurrent unprovoked seizures from E/I imbalance; 30+ genetic, structural, metabolic causes | ~50 million; 30% drug-resistant |
| **Depression** | CNS | Monoaminergic, glutamatergic, neuroinflammatory dysregulation; PFC-limbic circuit impairment | ~280 million; #1 cause of global disability |
| **Schizophrenia** | CNS | DA dysregulation, NMDA hypofunction, PV interneuron loss → psychosis and cognitive deficit | ~24 million; lifetime prevalence ~0.5–1% |
| **Peripheral neuropathy** | PNS | Axonal degeneration/demyelination from diabetes, chemotherapy, autoimmune causes | >20 million in USA alone; diabetic neuropathy most common |
| **Guillain-Barré syndrome** | PNS | Autoimmune demyelination of peripheral nerves → ascending paralysis | ~1–2/100,000/year; often post-infectious |

[^kandel-principles-ns]: Kandel ER, Koester JD, Mack SH, Siegelbaum SA. *Principles of Neural Science.* 6th ed. McGraw-Hill; 2021.
[^guyton-hall-physiology]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2020.
[^who-neurological-2006]: World Health Organization. *Neurological Disorders: Public Health Challenges.* WHO Press; 2006. [who.int/publications/i/item/9241563362](https://www.who.int/publications/i/item/9241563362)
[^purves-neuroscience-ns]: Purves D, Augustine GJ, Fitzpatrick D, et al. *Neuroscience.* 6th ed. Sinauer Associates; 2018. [ncbi.nlm.nih.gov/books/NBK10792/](https://www.ncbi.nlm.nih.gov/books/NBK10792/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
