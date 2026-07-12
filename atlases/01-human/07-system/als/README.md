---
schema: human-scale-entry/v1
id: als
name: ALS
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "ALS (30k US; 200k global) is a fatal motor neuron disease with progressive degeneration of upper and lower motor neurons; TDP-43 inclusions are the pathological hallmark in >97%; riluzole and edaravone extend survival modestly; tofersen (SOD1 ASO) is approved for familial ALS."
aliases: ["ALS", "amyotrophic lateral sclerosis", "Lou Gehrig's disease", "motor neuron disease", "MND", "SOD1 ALS", "TDP-43 ALS", "C9orf72 ALS", "FALS", "SALS"]
sources:
  - id: brown-2017-als-review
    type: peer-reviewed
    cite: "Brown RH, Al-Chalabi A. Amyotrophic lateral sclerosis. N Engl J Med. 2017;377(2):162-172."
    doi: "10.1056/NEJMra1603471"
    pmid: "28700839"
    url: "https://doi.org/10.1056/NEJMra1603471"
    accessed: "2026-06-08"
  - id: edaravone-als-2017
    type: peer-reviewed
    cite: "Writing Group on behalf of the Edaravone ALS 19 Study Group. Safety and efficacy of edaravone in well defined patients with amyotrophic lateral sclerosis: a randomised, double-blind, placebo-controlled trial. Lancet Neurol. 2017;16(7):505-512."
    doi: "10.1016/S1474-4422(17)30115-1"
    pmid: "28522180"
    url: "https://doi.org/10.1016/S1474-4422(17)30115-1"
    accessed: "2026-06-08"
  - id: miller-2023-tofersen-als
    type: peer-reviewed
    cite: "Miller TM, Cudkowicz ME, Genge A, et al. Trial of Antisense Oligonucleotide Tofersen for SOD1 ALS. N Engl J Med. 2022;387(12):1099-1110."
    doi: "10.1056/NEJMoa2204705"
    pmid: "36129998"
    url: "https://doi.org/10.1056/NEJMoa2204705"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/tdp-43
    relation: connects-to
    note: "TDP-43 cytoplasmic inclusions are the pathological hallmark of >97% of ALS; TARDBP mutations cause ~4% of familial ALS; nuclear TDP-43 loss disrupts splicing of STMN2 and UNC13A, driving axonal degeneration and synaptic failure in motor neurons."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate excitotoxicity via impaired astrocytic EAAT2 (GLT-1) uptake is a core ALS mechanism; riluzole (approved 1995) inhibits glutamate release and blocks persistent Na⁺ channels; AMPA receptor calcium permeability is increased in ALS spinal motor neurons."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Impaired autophagy (linked to mTOR hyperactivation and ULK1 dysfunction) contributes to TDP-43 and SOD1 aggregate accumulation in ALS; rapamycin reduces aggregate burden in ALS mouse models; p62/SQSTM1 (autophagy receptor) is a consistent component of ALS inclusions."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "ALS targets upper motor neurons in the primary motor cortex (Betz cells in layer V) and lower motor neurons in brainstem and spinal cord anterior horn; cortical hyperexcitability precedes clinical onset; cognitive and behavioral changes occur in ~50% (ALS-FTD continuum)."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "ALS reactive astrocytes lose EAAT2 → amplify glutamate excitotoxicity; ALS astrocytes kill co-cultured motor neurons in vitro; astrocyte-specific SOD1 removal prolongs mouse survival; non-cell-autonomous neurodegeneration via astrocytes is a core ALS mechanism."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "M1 microglia in ALS spinal cord release TNF-α, IL-1β, and NO → neurotoxic; NF-κB suppression in microglia prolongs SOD1 mouse survival; microglia transition from protective M2 to damaging M1 as ALS progresses; peripheral monocyte infiltration amplifies neuroinflammation."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "ALS causes dying-back axonopathy of peripheral motor nerves; neurofilament accumulation blocks axonal transport; EMG shows denervation (fibrillations, PSWs, giant units) in ≥3 body regions; peripheral motor nerve loss produces fasciculations, atrophy, and areflexia (LMN signs)."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "ALS is a motor neuron disease: it selectively kills the upper motor neurons of the cortex and the lower motor neurons of the brainstem and spinal cord, sparing most others; their extreme length and calcium-permeable AMPA receptors make these neurons uniquely vulnerable."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "ALS and CIDP both cause progressive weakness but at different sites: ALS is irreversible degeneration of the motor neuron itself, whereas CIDP is immune demyelination of the peripheral nerve — treatable and often reversible — so distinguishing them is critical."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "ALS shares the TDP-43 proteinopathy that also marks frontotemporal dementia and a subset of Alzheimer's: ~50% of ALS patients show cognitive change, C9orf72 expansion causes both ALS and FTD, and cytoplasmic TDP-43 aggregates link these diseases mechanistically."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: connects-to
    note: "ALS dismantles the neuromuscular junction early: as motor neurons degenerate, their axons die back and synapses retract from muscle endplates (denervation), causing fasciculations, weakness and wasting—this 'dying-back' NMJ loss may precede cell-body death."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "ALS devastates the musculoskeletal system through denervation: loss of upper and lower motor neurons produces progressive muscle weakness, wasting, spasticity and ultimately paralysis, while sparing sensation; the relentless decline in muscle function defines the disability."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Respiratory failure is the usual cause of death in ALS: degeneration of the motor neurons driving the diaphragm and accessory muscles progressively weakens ventilation, so non-invasive ventilation prolongs survival and forced vital capacity is a key prognostic and trial endpoint."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "ALS and myasthenia gravis cause weakness at opposite ends of the motor unit: ALS degenerates the motor neuron (upper and lower signs, fasciculations), while myasthenia blocks the neuromuscular junction (fatigable, treatable)—a prognosis-changing distinction."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "ALS and Parkinson's are neurodegenerations of protein misfolding hitting different neurons: ALS kills motor neurons (TDP-43), Parkinson's kills dopaminergic neurons (α-synuclein)—and ALS-parkinsonism-dementia overlaps hint at shared proteostasis failure."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Oligodendrocytes contribute to motor neuron death in ALS: beyond myelination they metabolically support axons, and dysfunctional ALS oligodendrocytes fail to supply lactate and degenerate—so glial, not just neuronal, failure drives the disease."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "ALS severs the acetylcholine signal to muscle: as motor neurons die, the terminals that release acetylcholine at the neuromuscular junction degenerate, so muscles lose stimulation and waste—unlike myasthenia gravis, where the receptor not the nerve is blocked."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Respiratory failure is how ALS kills: progressive weakness of the diaphragm and chest muscles cripples the lungs' bellows, causing hypoventilation, CO2 retention and eventual failure—so non-invasive ventilation is a mainstay that extends survival in ALS."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "ALS and multiple sclerosis both cause motor weakness but differ fundamentally: ALS is degenerative death of motor neurons, while MS is autoimmune demyelination with sensory and visual features—so ALS spares sensation and progresses without the relapses of MS."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper links the first ALS gene to oxidative stress: SOD1 is a copper-zinc superoxide dismutase, and many familial ALS mutations make the misfolded enzyme mishandle copper and generate toxic free radicals—so metal-dependent oxidative injury helps kill motor neurons."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "ALS is a relentless disease of the motor nervous system: it kills both upper motor neurons in the cortex and lower motor neurons in the brainstem and cord, so spasticity and wasting advance together until respiratory muscles fail."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Neuroinflammation drives ALS progression: activated microglia and astrocytes plus infiltrating immune cells turn from protective to toxic around dying motor neurons, so the immune system shapes how fast the disease advances—a target for emerging therapies."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "ALS is increasingly seen as a disease of failed protein clearance: motor neurons can't autophagy-degrade misfolded TDP-43 and SOD1, so toxic aggregates accumulate—linking many ALS genes (and the overlap with frontotemporal dementia) to a common disposal defect."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "ALS's SOD1 enzyme is a copper-zinc protein, and zinc is structural to it: mutations that disturb metal binding destabilize SOD1 into toxic aggregates, so the zinc (and copper) chemistry of this antioxidant enzyme sits at the heart of inherited ALS."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome is an emerging factor in ALS: altered gut flora and their metabolites may influence neuroinflammation and disease progression along the gut-brain axis, so the microbiome is being explored as a modifier of this relentless motor-neuron disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "ALS motor neurons die from calcium-driven excitotoxicity: excess glutamate floods them with calcium, and their unusually low calcium-buffering makes them especially vulnerable—the rationale for the glutamate-blunting drug riluzole."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells slow ALS: they restrain the harmful neuroinflammation of microglia, and patients with more functional Tregs progress slower—so expanding Tregs is an experimental therapy for this relentless motor neuron disease."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "ALS overlaps frontotemporal dementia in the hippocampus and cortex: TDP-43 pathology spreads beyond motor neurons to memory and behavior regions, so up to half of ALS patients develop cognitive change—uniting two diseases on one molecular spectrum."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Motor neurons in ALS run out of ATP: failing mitochondria cannot meet the huge energy demand of cells with metre-long axons, so the energy shortfall cripples transport and ion pumping and helps drive the neurons' death."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells infiltrate the dying motor regions in ALS: adaptive immunity adds to microglial inflammation, and the balance between these CD8 cells and protective regulatory T cells helps set how fast the disease advances."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "ALS motor neurons fire too easily through persistent sodium currents: this hyperexcitability stresses the cells and contributes to their loss, and it is partly why riluzole—which curbs sodium currents and glutamate—modestly slows the disease."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "ALS overwhelms the synapse with glutamate: failure to clear this excitatory transmitter floods motor-neuron synapses, and the resulting excitotoxicity helps kill the cells—the process the drug riluzole partly blunts."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages join the attack in ALS: they infiltrate the degenerating peripheral nerves and muscle, and their inflammatory signaling adds to the microglial neuroinflammation that speeds motor-neuron loss."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α inflames the dying motor regions in ALS: activated microglia and macrophages release this cytokine, and the chronic neuroinflammation it drives is thought to accelerate the loss of motor neurons."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging supports the ALS diagnosis: MRI photons rule out cord compression and other mimics, and can show corticospinal-tract changes, though the diagnosis rests on clinical and electrical findings."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron builds up in the ALS motor cortex: it deposits in the dying motor strip, visible as a dark 'motor band' on MRI, a marker that helps confirm the upper-motor-neuron degeneration."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "ALS eventually defeats swallowing: as bulbar muscles fail, food and saliva are aspirated and nutrition suffers, so a feeding tube into the stomach (PEG) becomes a key supportive step."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals ALS inside the dying motor neuron: cytoplasmic aggregates of TDP-43 protein and rod-like Bunina bodies clog the cell as its axon withers, the pathological signature of the disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eyes are ALS's last refuge: the muscles moving them are spared until the very end, so eye-tracking devices let even locked-in patients keep communicating long after the rest of the body is paralyzed."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Immobility jams the bowel in ALS: weak abdominal and pelvic muscles plus reduced movement bring stubborn constipation, a common and distressing problem as the disease robs the body of motion."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "ALS strikes only the voluntary muscles: it kills the motor neurons driving striated skeletal muscle, sparing the smooth muscle of gut, bladder, and vessels — which is why continence and circulation hold even as limbs fail."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "A treatable mimic must be excluded: multifocal motor neuropathy, driven by anti-GM1 antibodies and responsive to IVIG, can imitate ALS, so antibody testing helps separate the curable impostor from the relentless disease."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "ALS burns through the body's fat: a hypermetabolic state wastes adipose and muscle, and because faster weight loss predicts worse survival, high-calorie feeding has become part of care."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The endocannabinoid system is a symptom target: cannabinoids ease the spasticity, cramps, and excess saliva of ALS and are studied for neuroprotection, since the system also modulates the excitotoxicity that kills motor neurons."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "The mind carries a heavy load and a strange symptom: depression is common facing a terminal diagnosis, and pseudobulbar affect — uncontrollable laughing or crying out of proportion to feeling — arises from the degenerating motor pathways."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Even the heart's autonomic control frays: ALS disturbs the autonomic neurons that regulate the cardiomyocytes, reducing heart-rate variability and adding a dysautonomia to a disease usually thought of as purely motor."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "A growth factor for blood doubles as a nerve protector: VEGF keeps motor neurons alive, and animals engineered with low VEGF develop an ALS-like disease, implicating its deficiency in human motor-neuron degeneration."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The blood's inflammation tracks the decline: a rising neutrophil-to-lymphocyte ratio marks the systemic inflammation of ALS and predicts faster progression, a peripheral readout of a central disease."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "ALS sits in a family of protein-aggregation neurodegenerations: like Huntington's it stems from a toxic misfolded protein and a repeat-expansion gene (C9orf72), the two sharing mechanisms of aggregation and neuronal death."
  - target: 01-human/03-molecular/tbk1
    relation: connects-to
    note: "TBK1 mutations cause ALS-FTD: loss of this kinase, which links autophagy and innate-immune signaling, impairs clearance of aggregated TDP-43 and stokes neuroinflammation, tying a single gene to both motor and frontotemporal degeneration."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Dying motor neurons light the inflammasome: misfolded SOD1 and TDP-43 activate microglial NLRP3, and the IL-1β it releases amplifies the neuroinflammation that accelerates motor-neuron loss in ALS."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Paralysis breeds clots: the progressive immobility of ALS markedly raises the risk of deep-vein thrombosis and pulmonary embolism, a preventable complication that warrants vigilance as the limbs weaken."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Microglia inflame the dying motor neurons through NF-κB: misfolded proteins activate NF-κB in microglia, driving the cytokine output and NLRP3 priming that turn neuroinflammation into a driver of motor-neuron death."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Bulbar weakness routes food into the lungs: failing swallow and cough cause aspiration pneumonia, which together with ventilator dependence makes infection and sepsis a frequent terminal event in ALS."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Nights are broken by failing muscles: nocturnal hypoventilation, the inability to reposition, cramps and anxiety fragment sleep in ALS, so insomnia is common and worsens daytime fatigue and breathlessness."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Disuse and falls weaken the skeleton: progressive immobility and reduced weight-bearing in ALS drive bone loss, while the falls of failing limbs make osteoporotic fractures a real hazard."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Watching the body fail breeds dread: the relentless progression of paralysis and the fear of suffocation give ALS a heavy burden of anxiety alongside its depression."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Swallowing failure dries out the kidneys: dysphagia limits fluid intake while immobility and recurrent illness add prerenal stress, so chronic dehydration can erode renal function in advanced ALS."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Failing swallow and cough flood the lungs: bulbar and respiratory muscle weakness in ALS causes aspiration and an ineffective cough, and the resulting pneumonia — often pneumococcal — is the leading cause of death."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Progressive paralysis breaks down the skin: as ALS confines patients to bed or wheelchair, immobility and immobile pressure points produce pressure ulcers that heal poorly in the wasted, malnourished body."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "It is not painless as once thought: muscle cramps, spasticity, joint strain from weakness and some sensory involvement give ALS chronic pain, including a neuropathic component, that needs active management."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Bulbar weakness wrecks swallowing: ALS causes dysphagia and sialorrhoea with aspiration and weight loss, driving the need for gastrostomy feeding, while riluzole adds a risk of hepatotoxicity."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It burns fuel abnormally fast: ALS is marked by a hypermetabolic state with raised resting energy expenditure and weight loss, and aggressive nutritional and metabolic support improves survival."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chronic hypoventilation strains the right heart: the progressive respiratory failure of ALS raises pulmonary pressures toward cor pulmonale, and some patients show autonomic cardiovascular dysfunction."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It curiously spares the skin: pressure ulcers are rare in ALS even with profound immobility, attributed to altered dermal collagen, though drooling causes troublesome perioral skin irritation."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Bladder control is usually preserved: ALS characteristically spares the sphincter motor neurons of Onuf's nucleus, so continence is maintained until late, a feature distinguishing it from other neurodegeneration."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Autonomic and sexual function are spared: ALS selectively attacks motor neurons, leaving sexual function and autonomic control largely intact, which shapes counselling and care."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "A treatable mimic: HIV can cause a motor neuron syndrome resembling ALS that may improve with antiretroviral therapy, an important differential to exclude before diagnosis."
  - target: 01-human/07-system/west-nile-virus
    relation: connects-to
    note: "A virus can destroy the same neurons: West Nile virus attacks anterior-horn motor neurons, causing a poliomyelitis-like acute flaccid paralysis that mimics rapidly progressive motor neuron disease."
  - target: 02-pathogen/01-viruses/coxsackievirus-b
    relation: connects-to
    note: "Enteroviruses target motor neurons too: like poliovirus, Coxsackie and other enteroviruses can infect anterior-horn cells and cause acute flaccid paralysis, part of the infectious differential of motor neuron disease."
  - target: 01-human/07-system/lewy-body-dementia
    relation: connects-to
    note: "A shared misfolded protein: TDP-43 aggregation links ALS to the frontotemporal dementia it overlaps with and to the TDP-43 co-pathology found in Lewy body dementia, blurring the lines between neurodegenerations."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "The barrier around motor neurons leaks: blood-spinal-cord barrier breakdown and reduced VEGF-driven vascular support contribute to motor-neuron degeneration in ALS, a vascular dimension of the disease."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Body fat paradoxically protects: ALS drives a hypermetabolic, weight-losing state, and higher body-mass index and high-calorie nutrition are associated with longer survival, the opposite of most diseases."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Gene-targeted therapy arrives: tofersen, an antisense oligonucleotide silencing mutant SOD1, treats that familial ALS subtype, joining riluzole and edaravone — the vanguard of precision therapy for motor neuron disease."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Failing transport kills the motor neuron: ALS is a dying-back axonopathy in which disrupted axonal transport — many ALS genes encode transport and cytoskeletal proteins — starves the long motor axons before the cell body dies."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Immobility and falls break bone: progressive weakness in ALS causes disuse osteoporosis and frequent falls, so fractures add to the burden of a disease that steadily strips muscle and mobility."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Respiratory failure is the endgame: motor-neuron loss paralyses the diaphragm, so ventilatory failure at the alveolar gas-exchange surface—not the limb weakness—is the usual cause of death, the reason for non-invasive ventilation."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative-stress defence: motor neurons in ALS suffer oxidative damage, and the NRF2 (NFE2L2) antioxidant pathway is a neuroprotective target—edaravone, an approved ALS drug, is a free-radical scavenger."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "The metabolism paradox: ALS is a hypermetabolic, weight-losing disease, and higher BMI and type-2 diabetes are paradoxically linked to lower ALS risk and slower progression, a clue to its energetics."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Shared genetics with psychosis: C9orf72 and other ALS-FTD genes confer psychiatric features, with raised rates of schizophrenia in affected families—sometimes appearing years before motor symptoms."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Mood in the ALS-FTD spectrum: the C9orf72 expansion that links ALS to frontotemporal dementia also raises rates of mood disorders including bipolar disorder, part of its broad neuropsychiatric prodrome."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Respiratory vulnerability: ALS patients with failing respiratory muscles are at high risk of severe COVID-19, and the infection can precipitate the respiratory failure that ends the disease."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Neurotrophic support: brain-derived neurotrophic factor promotes motor neuron survival, and its decline contributes to neurodegeneration in ALS—a rationale behind neurotrophin trials."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "A neurotrophic candidate: insulin-like growth factor 1 supports motor neuron survival and axonal maintenance and has been trialled, with mixed results, as an ALS therapy."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Gut-brain and feeding: progressive dysphagia in ALS often requires gastrostomy feeding, and an altered gut microbiome and intestinal barrier are increasingly implicated in disease progression."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Innate sensing of mislocalised DNA: TDP-43 pathology in ALS releases mitochondrial DNA that activates the cGAS-STING pathway, driving the type-I interferon neuroinflammation of the disease."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Microglial cytokine: IL-1β from activated microglia around degenerating motor neurons amplifies the neuroinflammation that accelerates motor-neuron loss in ALS."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory progression: elevated IL-6 reflects the neuroinflammatory and systemic inflammatory activity that tracks with faster decline in ALS."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 is elevated in ALS CSF and recruits inflammatory monocytes to degenerating motor pathways, part of the neuroinflammation driving disease progression."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "TDP-43-driven interferon: cytoplasmic TDP-43 aggregates and leaked nucleic acids activate cGAS-STING to trigger a type-I-interferon response, an inflammatory driver of motor-neuron degeneration in ALS."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement-mediated denervation: complement activation including C3 deposits at the neuromuscular junction and on motor neurons in ALS, contributing to synapse loss and denervation."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Motor-neuron apoptosis: caspase-3 executes the apoptotic death of motor neurons in ALS, the final common pathway through which excitotoxicity, oxidative stress and protein aggregation kill the cells."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Oxidative injury: excess nitric oxide reacts with superoxide to form peroxynitrite that damages motor-neuron proteins and mitochondria, a central oxidative mechanism especially in SOD1-mutant ALS."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Microglial activation: aggregated proteins and DAMPs released by dying motor neurons engage microglial TLR4, driving the neuroinflammation that accelerates motor-neuron loss in ALS."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Excitotoxic vulnerability: motor neurons express calcium-permeable AMPA receptors and have low calcium-buffering capacity, so glutamate excitotoxicity floods them with calcium that destroys mitochondria — a selective vulnerability central to ALS neurodegeneration."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: xanthine-oxidase-derived reactive oxygen species add to the oxidative burden killing motor neurons in ALS, the free-radical injury that the antioxidant edaravone targets to slow functional decline."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial biomarker: galectin-3 released by activated microglia rises in ALS as a marker of the neuroinflammatory, neurotoxic microglial state, increasingly viewed as both a disease biomarker and a driver of motor-neuron loss."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival signalling: IGF-1/PI3K-AKT pro-survival signalling (IGF-1 already mapped) supports motor-neuron survival, and its insufficiency contributes to the motor-neuron death of ALS, a neurotrophic axis explored therapeutically."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Astrocyte toxicity: reactive astrocytes in ALS upregulate connexin-43 hemichannels, releasing toxic factors and glutamate that propagate the non-cell-autonomous motor-neuron injury of the disease."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis threshold: the balance of anti-apoptotic BCL-2 against pro-apoptotic signals sets the threshold for the caspase-3 motor-neuron apoptosis (already mapped) that executes ALS neurodegeneration."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microglial neuroinflammation: TLR-MyD88-NF-κB innate signalling in microglia (TLR4 and NF-κB already mapped) drives the chronic neuroinflammation that accelerates motor-neuron loss in ALS."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Interferon amplification: cGAS-STING-driven type-I interferon (both already mapped) signals through JAK-STAT to amplify the innate neuroinflammation increasingly implicated in ALS progression."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophic support: signalling through the TrkB receptor (NTRK), engaged by BDNF and complementing IGF-1 (both already mapped), supports motor-neuron survival whose failure contributes to ALS degeneration."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3-driven reactive astrogliosis is a prominent feature of the neuroinflammatory response in ALS motor-neuron degeneration."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling participates in the stress responses and excitotoxic injury of motor neurons in ALS."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN modulation of the PI3K-AKT-mTOR axis (AKT and mTOR mapped) influences motor-neuron survival, a candidate neuroprotective target in ALS."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling drives the interferon response of activated microglia (cGAS-STING already mapped) contributing to the neuroinflammation of ALS."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling promotes the cytoskeletal and TDP-43 pathology and motor-neuron degeneration of ALS, a candidate therapeutic target."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the astrocyte and microglial responses that balance neuroprotection against neuroinflammation in ALS."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the motor-neuron autophagy and oxidative-stress defense whose failure permits TDP-43 aggregation in ALS."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation of ALS."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and vascular stress responses contribute to motor-neuron vulnerability in ALS."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, coupled to autophagy and mTOR (both already mapped), regulates the proteostasis and metabolic stress of the degenerating motor neurons of ALS."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the neuronal survival pathways whose failure contributes to motor-neuron degeneration in ALS."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic CD8 T cells infiltrate the ALS spinal cord and contribute to motor-neuron injury."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the microglial activation and neuroinflammation of amyotrophic lateral sclerosis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation implicated in amyotrophic lateral sclerosis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven microglial and monocyte recruitment contributes to the neuroinflammation of amyotrophic lateral sclerosis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the microglial and neuroinflammatory responses of amyotrophic lateral sclerosis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses of amyotrophic lateral sclerosis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation of amyotrophic lateral sclerosis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the motor-neuron and glial gene programs of amyotrophic lateral sclerosis."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (A2A receptor) signaling participates in the glutamate-excitotoxicity modulation and neuroinflammation of amyotrophic lateral sclerosis."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microglial activation and neuroinflammation of amyotrophic lateral sclerosis."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Neuroinflammation: MHC class II is upregulated on activated microglia (already mapped) in the ALS spinal cord and motor cortex, marking the antigen-presenting inflammatory state that contributes to the non-cell-autonomous killing of motor neurons."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences: ALS is somewhat more common and earlier-onset in men, and estrogen's neuroprotective effects are proposed to contribute to the sex difference in risk and progression."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Hypermetabolism: ALS features a hypermetabolic state with altered glucose and lipid handling, and insulin resistance is associated with faster progression, a metabolic dimension increasingly targeted in trials."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Regulatory T-cell therapy: low-dose IL-2 expands regulatory T cells that restrain the neuroinflammation (microglia already mapped) driving ALS, a strategy tested in trials to slow the non-cell-autonomous motor neuron death."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Lipid and survival: higher LDL cholesterol and dyslipidaemia are paradoxically associated with longer survival in ALS, part of the hypermetabolic and lipid dysregulation (insulin already mapped) that shapes its metabolic phenotype."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid protection: progesterone-derived neurosteroids are neuroprotective for motor neurons, and together with estrogen (already mapped) may contribute to the modest sex difference in ALS risk and progression."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the activated microglia (already mapped) and the cyclooxygenase pathway contribute to the neuroinflammation (IL-6, TNF and IL-1 already mapped) that accelerates motor neuron death in ALS."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory neuroprotection: the anti-inflammatory IL-10 opposes the microglial pro-inflammatory response (TNF, IL-1 and IL-6 already mapped) driving motor neuron loss, and boosting this arm is a neuroprotective strategy of interest in ALS."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Hypermetabolism and weight loss: ALS is marked by a hypermetabolic state with weight loss, and the fall in the adipokine leptin reflects the fat depletion (cholesterol already mapped) whose faster loss predicts worse survival."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Microglial polarisation: IL-4 polarises the microglia toward a neuroprotective M2 phenotype (IL-10 already mapped), and the balance against the pro-inflammatory activation shapes the motor neuron loss of ALS."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroprotection: IL-13, with IL-4 (already mapped), supports the M2 microglial arm that can be neuroprotective in ALS, part of the neuroimmune balance shaping the progression of the disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium neuroprotection: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity that drives the motor neuron death, a proposed neuroprotective factor in ALS."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Hypermetabolism adipokine: adiponectin, with leptin (already mapped), reflects the hypermetabolism and weight loss that worsen the prognosis of ALS, part of the metabolic (insulin already mapped) dimension of the disease."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine inflammation: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the metabolic and neuroinflammatory (TNF and IL-1 already mapped) dimension of ALS."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium and motor-neuron toxicity: the selenoprotein antioxidant defence of selenium, and the selenium-linked environmental exposures, have been implicated in the oxidative motor-neuron degeneration of ALS."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Non-cell-autonomous astrocytes: the astrocyte toxicity (the impaired glutamate — already mapped — uptake, the reactive astrogliosis) contributes non-cell-autonomously to the motor-neuron death of ALS."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Motor axon degeneration: the lower-motor-neuron axons of the peripheral nerve degenerate (the denervation, the fasciculations and the muscle atrophy) in ALS."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "SOD1 copper toxicity: the mutant SOD1 (the Cu/Zn superoxide dismutase) and the copper-mediated oxidative toxicity are a cause of the familial ALS."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the neuroinflammation (type-I interferon and microglia already mapped) that accelerates the motor-neuron death of ALS."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of ALS."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with ALS."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of ALS."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation associated with ALS."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK-mediated motor-neuron injury: the NK cells (perforin already mapped) infiltrate the ALS motor cortex and spinal cord and contribute to the degeneration of the motor neurons (already mapped)."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) activation and the complement-mediated motor-neuron injury of ALS."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) deposit on the motor neurons and the neuromuscular junction, a candidate therapeutic target in ALS."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell neuroinflammation: the mast cells, with the neutrophils, accumulate along the degenerating ALS motor axons and neuromuscular junctions, contributing to the neuroinflammation of ALS."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement deposition on the motor neurons and neuromuscular junction of ALS."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Motor-neuron iron: transferrin, the iron carrier, reflects the disordered iron handling that drives the oxidative stress and ferroptosis of the degenerating motor neurons of ALS."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the neuroinflammation of ALS."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-neuroimmune axis: TSLP, from barrier epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the neuroinflammatory and neuroimmune dimension of ALS."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-neuroinflammation axis: bradykinin, via B1/B2 receptors on microglia (already mapped) and motor-neuron endothelium, amplifies the blood-spinal-cord barrier disruption and the neuroinflammation of ALS."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact/complement brake: the C1-esterase inhibitor regulates the classical complement (C3, C5 already mapped) and contact pathways, dampening the complement deposition on motor neurons and neuromuscular junctions of ALS."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell neuroinflammation: mast cells (already mapped) in the spinal-cord (nervous-system already mapped) perivascular niche release histamine that amplifies the blood-spinal-cord barrier permeability and the neuroinflammation of ALS."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Neuroprotective antioxidant: melatonin reduces mitochondrial ROS in motor neurons (already mapped), attenuates the NLRP3-inflammasome (already mapped) and NF-κB activation, and modulates the circadian-clock disruption of ALS."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Motor-neuron EPO: erythropoietin, via EpoR on motor neurons (already mapped) and microglia (already mapped), exerts anti-apoptotic neuroprotection and reduces the neuroinflammation relevant to the motor-neuron degeneration of ALS."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "ALS testosterone: testosterone, via androgen receptors on motor neurons (already mapped) and microglia (already mapped), exerts neuroprotective effects; testosterone deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of ALS."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "ALS serotonin: serotonin, via 5-HT receptors on motor neurons (already mapped) and astrocytes (already mapped), modulates neuroinflammatory tone; serotonin dysregulation amplifies the TDP-43 (already mapped) and NLRP3 (already mapped) neuroinflammatory cascade of ALS."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "ALS prolactin: prolactin, via PRLR on motor neurons (already mapped) and microglia (already mapped), modulates neuroimmune activation; prolactin deficiency amplifies the TDP-43 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of ALS."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "ALS oxytocin: oxytocin, via OXTR on motor neurons (already mapped) and microglia (already mapped), attenuates neuroinflammation; oxytocin deficiency amplifies the TDP-43 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of ALS."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "ALS vasopressin: vasopressin, via V1aR on astrocytes (already mapped) and motor neurons (already mapped), modulates glutamate (already mapped) excitotoxicity; vasopressin dysregulation amplifies the TDP-43 (already mapped) and NLRP3 (already mapped) cascade of ALS."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "ALS iodine: iodine-dependent thyroid hormones modulate motor-neuron (neuron already mapped) survival and astrocyte (already mapped) function; iodine deficiency impairs thyroid-mediated regulation of the TDP-43 (already mapped) and NF-κB (already mapped) cascade of ALS."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "ALS potassium: potassium regulates motor neuron (already mapped) membrane excitability; potassium dysregulation amplifies TDP-43 (already mapped) misfolding and NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) neuroinflammatory cascade in ALS."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "ALS phosphorus: phosphorus fuels motor neuron (already mapped) and astrocyte (already mapped) ATP; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) and TDP-43 (already mapped) neurodegeneration in ALS."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "ALS nitrogen: nitric oxide (NO, nitrogen-derived) in microglia (already mapped) and astrocytes (already mapped) amplifies neuron (already mapped) excitotoxicity; NO excess upregulates NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade in ALS."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "chloride via GABA(A) receptors and KCC2 on motor neurons (already mapped) and astrocytes (already mapped) sets inhibitory tone; chloride dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and TDP-43 (already mapped) motor neuron degeneration in ALS."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "H2S from sulfur-amino acids in motor neurons (already mapped) and astrocytes (already mapped) promotes neuroprotection via K-ATP channels; sulfur deficiency amplifies NLRP3 (already mapped) and NF-κB (already mapped) and TDP-43 (already mapped) motor neuron degeneration in ALS."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "mitochondrial oxygen sustains ATP in motor neurons (already mapped) and astrocytes (already mapped) for axonal transport; hypoxia amplifies NLRP3 (already mapped) and NF-κB (already mapped) and TDP-43 (already mapped) mitochondrial motor neuron degeneration in ALS."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "ALS carbon: carbon backbone of glutamate (already mapped) and TDP-43 (already mapped) in motor neurons (already mapped) and astrocytes (already mapped) drives neuronal metabolism; carbon dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) in ALS."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "ALS hydrogen: hydrogen, via redox homeostasis in motor neurons (already mapped) and astrocytes (already mapped), quenches ROS-driven TDP-43 (already mapped) aggregation; hydrogen dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) cascade of ALS."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "ALS PD-1: PD-1 on regulatory-t-cell (already mapped) and macrophages (already mapped) modulates neuroinflammatory homeostasis; PD-1 dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and TDP-43 (already mapped) motor neuron degeneration cascade of ALS."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "ALS GLP-1: GLP-1 receptor signalling in motor neurons (already mapped) and microglia (already mapped) modulates metabolic neuroinflammation; GLP-1 dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TDP-43 (already mapped) cascade of ALS."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "ALS angiotensin-II: angiotensin-II signalling in motor neurons (already mapped) and astrocytes (already mapped) promotes neuroinflammation; angiotensin-II excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TDP-43 (already mapped) cascade of ALS."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "ALS WNT/β-catenin: WNT/β-catenin in motor neurons (already mapped) and astrocytes (already mapped) supports neurotrophic survival; WNT dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TDP-43 (already mapped) motor neuron degeneration cascade of ALS."
---

# ALS

## Overview

**Amyotrophic lateral sclerosis (ALS)**, also known as **Lou Gehrig's disease** or motor neuron disease (MND), is a progressive, invariably fatal neurodegenerative disease that selectively destroys **upper motor neurons (UMN)** in the primary motor cortex and **lower motor neurons (LMN)** in the brainstem and spinal cord anterior horn. The result is progressive paralysis of voluntary muscles — including limb muscles, bulbar muscles (swallowing, speech), and ultimately respiratory muscles — leading to death typically from respiratory failure within **2–5 years** of onset in most patients (10–15% survive >10 years; Stephen Hawking lived 55 years — an extraordinary outlier).

**Epidemiology [^brown-2017-als-review]:**
- Prevalence: ~30,000 in the US; ~200,000 globally
- Incidence: 2–3 per 100,000 per year (Western populations); lifetime risk ~1 in 300–400
- Peak onset: age 55–75 years; male:female ~1.3–1.5:1
- Genetics: ~10–15% familial (≥1 affected first-degree relative); 85–90% sporadic
- Prognosis: median survival ~2–3 years from symptom onset; ~50% die within 30 months; bulbar-onset worse than limb-onset

**ALS-FTD continuum:** ALS and frontotemporal dementia (FTD) are now recognized as ends of a disease spectrum. ~50% of ALS patients have some cognitive/behavioral changes; ~5–15% meet criteria for full FTD. C9orf72 repeat expansion is the most common cause of both ALS and ALS-FTD.

## Structure

### Upper and lower motor neuron signs

ALS diagnosis requires evidence of **both UMN and LMN degeneration** across ≥2 body regions (El Escorial revised criteria; Gold Coast criteria 2020):

| Finding | UMN dysfunction | LMN dysfunction |
|:---|:---|:---|
| **Reflexes** | Hyperreflexia (brisk DTRs) | Hyporeflexia/areflexia |
| **Muscle tone** | Spasticity | Flaccidity |
| **Pathological signs** | Babinski sign, Hoffman's sign, jaw jerk | Absent |
| **Muscle bulk** | Preserved early | Atrophy (denervation) |
| **Fasciculations** | Absent | Present (spontaneous motor unit discharges) |
| **EMG** | Central conduction delay | Fibrillations, positive sharp waves, giant motor units |

**Clinical phenotypes:**
- **Classic limb-onset ALS:** Asymmetric limb weakness (arm or leg); spreads to other limbs and bulbar muscles; accounts for ~70% of cases
- **Bulbar-onset ALS:** Dysarthria, dysphagia first; accounts for ~25%; faster progression; more common in women and older patients
- **Respiratory-onset ALS:** Dyspnea, orthopnea without limb involvement initially; rare (~3%); very rapid progression
- **Flail arm syndrome (brachial amyotrophic diplegia):** Bilateral arm weakness with LMN predominance; slower progression
- **Primary lateral sclerosis (PLS):** Pure UMN presentation >4 years without LMN signs — favorable prognosis; some eventually develop LMN signs (ALS)
- **Progressive muscular atrophy (PMA):** Pure LMN presentation; TDP-43 inclusions found at autopsy — ALS variant

### Genetics of ALS

| Gene | Mutation type | % familial ALS | % sporadic ALS | Protein function |
|:---|:---|:---|:---|:---|
| **C9orf72** | GGGGCC hexanucleotide repeat expansion (>30 copies; normal <10) | 40% | 5–10% | Nuclear export factor; RNA granule regulation; autophagy |
| **SOD1** | Missense (>180 mutations; A4V most common/lethal in North America) | 20% | 1–2% | Cu-Zn superoxide dismutase (toxic gain-of-function, not LOF) |
| **TARDBP** | Missense (>50 mutations in glycine-rich CTD) | 4% | <1% | RNA-binding protein TDP-43 |
| **FUS** | Missense (NLS mutations most severe; juvenile-onset FUS-ALS) | 4–5% | <1% | RNA-binding protein; similar to TDP-43 |
| **TBK1** | LOF (haploinsufficiency) | 4% | <1% | Tank-binding kinase 1; autophagy and NF-κB signaling |
| **NEK1** | LOF | 3% | ~1% | NIMA-related kinase; DNA damage response |
| **CHCHD10** | Missense | 2% | <1% | Mitochondrial inner membrane protein |
| **UBQLN2** | Missense (X-linked) | ~2% | <1% | Ubiquilin-2; ubiquitin-proteasome pathway |
| **OPTN** | Missense/deletion | 2% | <1% | Optineurin; autophagy receptor; NF-κB signaling |

**C9orf72 mechanism:** The GGGGCC expansion causes toxicity via three mechanisms:
1. **RNA foci:** Repeat-containing RNA forms nuclear foci that sequester RNA-binding proteins (hnRNP A3, Pur-α) → loss of normal RBP function
2. **Dipeptide repeat proteins (DPRs):** Repeat-associated non-ATG (RAN) translation produces 5 DPR species (poly-GA, poly-GR, poly-PR, poly-GP, poly-PA); poly-GR and poly-PR are highly toxic — disrupt nucleocytoplasmic transport, stress granule dynamics, and ribosome function
3. **C9orf72 haploinsufficiency:** C9orf72 protein regulates autophagy and lysosomal function; reduced levels impair autophagy of TDP-43/FUS aggregates

### Pathology

**TDP-43 proteinopathy:** >97% of all ALS cases (sporadic and familial, with the notable exception of SOD1-ALS and FUS-ALS which have distinct inclusions) show:
- Nuclear clearance of TDP-43 from affected neurons
- Cytoplasmic inclusions of ubiquitinated, phosphorylated, C-terminally cleaved TDP-43
- Loss of nuclear TDP-43 RNA processing function → cryptic exon inclusion in STMN2 and UNC13A → axon regeneration failure and synaptic deficiency

**SOD1 ALS:** A unique subtype — SOD1 inclusions rather than TDP-43; different cell biology; unique vulnerability of fast-fatigable motor neurons; tofersen (SOD1 ASO) is the first approved targeted therapy for any ALS genetic variant.

## Function

### Motor neuron vulnerability mechanisms

Why are motor neurons uniquely vulnerable in ALS? Multiple converging factors:

**Glutamate excitotoxicity:**
- Astrocytic glutamate uptake transporter EAAT2 (GLT-1) is selectively reduced in ALS spinal cord → elevated synaptic glutamate → persistent NMDA/AMPA receptor activation → intracellular Ca²⁺ overload
- ALS motor neurons express higher levels of **Ca²⁺-permeable AMPA receptors** (lower GluA2 levels → more Ca²⁺-permeable AMPARs) than typical CNS neurons — increasing vulnerability to Ca²⁺ toxicity
- Ca²⁺ overload → mitochondrial dysfunction → ROS production → protein aggregation amplification → cell death

**Axonal transport failure:**
- Motor neuron axons are among the longest in the body (>1 meter for lumbar motor neurons) → axonal transport is critically important and energetically costly
- Dynein/kinesin motor complex dysfunction in ALS → impaired retrograde transport of neurotropic signals (BDNF, GDNF) and organelles → failure of energy supply to distal axon
- Neurofilament accumulation in cell bodies and axons (a feature of ALS) → axonal transport blockade → "dying-back" axonopathy

**Neuroinflammation:**
- Microglial activation and astrocyte reactivity are prominent in ALS spinal cord
- Reactive astrocytes lose EAAT2 expression → amplify excitotoxicity
- M1 microglia release TNF-α, IL-1β, NO → neurotoxic
- Neuroinflammation propagates disease progression (not just secondary epiphenomenon — NF-κB suppression in microglia prolongs survival in SOD1 mice)

**Mitochondrial dysfunction:**
- Mitochondrial morphology is disrupted in ALS motor neurons
- SOD1 mutation → mitochondrial mislocalization in motor neurons → impaired ATP production at nodes of Ranvier → action potential failure
- TDP-43 regulates mitochondrial RNA → TDP-43 pathology disrupts mitochondrial function

## Pathology

### Diagnosis

ALS diagnosis is **clinical** — no single definitive biomarker test (though NfL is increasingly used):

**Revised El Escorial / Gold Coast criteria (2020):**
- Gold Coast criteria simplified: clinical signs of LMN degeneration + evidence of progressive spread (additional regions or EMG evidence in asymptomatic regions)
- EMG remains essential: shows active denervation (fibrillations, PSWs) in ≥3 regions (bulbar, cervical, thoracic, lumbar) to establish LMN disease broadly

**Biomarkers:**
- **Neurofilament light chain (NfL):** Elevated in CSF and blood; correlated with disease progression rate; reduces with tofersen treatment (SOD1-ALS) proportional to clinical benefit; increasingly used as trial endpoint and prognostic marker
- **pNfH (phosphorylated neurofilament heavy chain):** Similar to NfL; ALS-specific elevations
- **TDP-43 in CSF:** Elevated in ~50% of ALS patients but less sensitive than NfL
- **Genetic testing:** Strongly recommended for all ALS patients; C9orf72 repeat expansion PCR; NGS panel for SOD1, TARDBP, FUS, and other genes — affects prognosis and treatment (tofersen for SOD1-ALS)

### Treatment

**Approved disease-modifying therapies:**

| Drug | Mechanism | Approval | Benefit |
|:---|:---|:---|:---|
| **Riluzole** | Glutamate release inhibitor; persistent Na⁺ channel blocker → reduces motor neuron excitability | FDA 1995 | ~3-month median survival extension; modestly slows decline |
| **Edaravone** | Free radical scavenger (oxidative stress reduction) | FDA 2017 (selected patients); Japan/Canada/Korea earlier | ~33% slower functional decline in selected subgroup [^edaravone-als-2017] |
| **Tofersen (Qalsody)** | SOD1-targeting antisense oligonucleotide → reduces SOD1 protein | FDA 2023 (accelerated approval; SOD1-ALS only) | Reduces NfL; slows decline in faster-progressing SOD1-ALS; some functional benefit [^miller-2023-tofersen-als] |
| **AMX0035 (Relyvrio)** | Sodium phenylbutyrate + taurursodiol → reduces ER stress + mitochondrial apoptosis | FDA 2022 (accelerated; withdrawn 2024 after confirmatory trial failed) | Initial trial showed survival benefit; failed Phase 3 PHOENIX trial |

**Symptomatic/supportive management (essential):**
- **Non-invasive ventilation (NIV/BiPAP):** Standard of care for respiratory compromise; extends survival ~7 months in median and >12 months in some patients; comfort and quality of life
- **PEG tube:** Percutaneous gastrostomy when swallowing impaired (bulbar dysfunction); maintains nutrition and weight; recommended before FVC <50%
- **Communication augmentative/alternative technology (AAC):** Text-to-speech, eye-gaze devices — life-changing for quality of life
- **Multidisciplinary ALS clinic:** Consistent evidence that multidisciplinary care (neurology, respiratory therapy, PT, OT, speech, social work, palliative care) extends survival and improves quality of life
- **Riluzole + baclofen:** Baclofen reduces spasticity
- **Mexiletine:** For muscle cramps (sodium channel stabilizer)

**Emerging therapies:**
- **C9orf72-targeting ASOs:** BIIB078 (antisense targeting C9orf72 repeat-containing RNA) — Phase 1/2; AB-105 (RAN translation inhibitor)
- **STMN2-restoring ASO (UMass/Clene):** Corrects cryptic exon to restore stathmin-2; Phase 1/2 ongoing (TDP-43 ALS strategy — applicable to >97% of cases)
- **Stem cell approaches:** NurOwn (MSC-NTF) — failed Phase 3 2023; AstroRx (healthy astrocyte transplant) — Phase 1
- **Gene therapy:** AAV-SOD1 silencing; intrathecal delivery; ongoing trials

## Connections

- `connects-to` → **[TDP-43](../../../03-molecular/tdp-43/README.md)** — TDP-43 cytoplasmic inclusions are the pathological hallmark of >97% of ALS; TARDBP mutations cause ~4% of familial ALS; nuclear TDP-43 loss disrupts STMN2 and UNC13A splicing, causing axonal degeneration and synaptic failure.

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — glutamate excitotoxicity via impaired astrocytic EAAT2 uptake is a core ALS mechanism; riluzole inhibits glutamate release; ALS motor neurons express Ca²⁺-permeable AMPA receptors (low GluA2) increasing vulnerability; NMDA Ca²⁺ overload drives mitochondrial failure.

- `connects-to` → **[mTOR](../../../03-molecular/mtor/README.md)** — impaired autophagy contributes to TDP-43 and SOD1 aggregate accumulation; rapamycin reduces aggregate burden in ALS mouse models; p62/SQSTM1 and optineurin (autophagy receptors) are consistent components of ALS inclusions, indicating failed selective autophagy.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — ALS targets upper motor neurons (Betz cells, layer V primary motor cortex) and lower motor neurons (brainstem/spinal anterior horn); cortical hyperexcitability and reduced cortical inhibition precede clinical onset; cognitive/behavioral changes occur in ~50% (ALS-FTD spectrum).
- `connects-to` → **[Astrocyte](../../../04-cellular/astrocyte/README.md)** — ALS reactive astrocytes lose EAAT2 → amplify glutamate excitotoxicity; ALS astrocytes kill co-cultured motor neurons in vitro; astrocyte-specific SOD1 removal prolongs mouse survival; non-cell-autonomous neurodegeneration via astrocytes is a core ALS mechanism.
- `connects-to` → **[Microglia](../../../04-cellular/microglia/README.md)** — M1 microglia in ALS spinal cord release TNF-α, IL-1β, and NO → neurotoxic; NF-κB suppression in microglia prolongs SOD1 mouse survival; microglia transition from protective M2 to damaging M1 as ALS progresses; peripheral monocyte infiltration amplifies neuroinflammation.
- `connects-to` → **[Peripheral Nerve](../../../05-tissue/peripheral-nerve/README.md)** — ALS causes dying-back axonopathy of peripheral motor nerves; neurofilament accumulation blocks axonal transport; EMG shows denervation (fibrillations, PSWs, giant units) in ≥3 body regions; peripheral motor nerve loss produces fasciculations, atrophy, and areflexia (LMN signs).

- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — ALS is a motor neuron disease: it selectively kills the upper motor neurons of the cortex and the lower motor neurons of the brainstem and spinal cord, sparing most others; their extreme length and calcium-permeable AMPA receptors make these neurons uniquely vulnerable.

- `connects-to` → **[CIDP](../cidp/README.md)** — ALS and CIDP both cause progressive weakness but at different sites: ALS is irreversible degeneration of the motor neuron itself, whereas CIDP is immune demyelination of the peripheral nerve — treatable and often reversible — so distinguishing them is critical.

- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — ALS shares the TDP-43 proteinopathy that also marks frontotemporal dementia and a subset of Alzheimer's: ~50% of ALS patients show cognitive change, C9orf72 expansion causes both ALS and FTD, and cytoplasmic TDP-43 aggregates link these diseases mechanistically.
- `connects-to` → **[Neuromuscular Junction](../../05-tissue/neuromuscular-junction/README.md)** — ALS dismantles the neuromuscular junction early: as motor neurons degenerate, their axons die back and synapses retract from muscle endplates (denervation), causing fasciculations, weakness and wasting—this 'dying-back' NMJ loss may precede cell-body death.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — ALS devastates the musculoskeletal system through denervation: loss of upper and lower motor neurons produces progressive muscle weakness, wasting, spasticity and ultimately paralysis, while sparing sensation; the relentless decline in muscle function defines the disability.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Respiratory failure is the usual cause of death in ALS: degeneration of the motor neurons driving the diaphragm and accessory muscles progressively weakens ventilation, so non-invasive ventilation prolongs survival and forced vital capacity is a key prognostic and trial endpoint.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — ALS and myasthenia gravis cause weakness at opposite ends of the motor unit: ALS degenerates the motor neuron (upper and lower signs, fasciculations), while myasthenia blocks the neuromuscular junction (fatigable, treatable)—a prognosis-changing distinction.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — ALS and Parkinson's are neurodegenerations of protein misfolding hitting different neurons: ALS kills motor neurons (TDP-43), Parkinson's kills dopaminergic neurons (α-synuclein)—and ALS-parkinsonism-dementia overlaps hint at shared proteostasis failure.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Oligodendrocytes contribute to motor neuron death in ALS: beyond myelination they metabolically support axons, and dysfunctional ALS oligodendrocytes fail to supply lactate and degenerate—so glial, not just neuronal, failure drives the disease.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — ALS severs the acetylcholine signal to muscle: as motor neurons die, the terminals that release acetylcholine at the neuromuscular junction degenerate, so muscles lose stimulation and waste—unlike myasthenia gravis, where the receptor not the nerve is blocked.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Respiratory failure is how ALS kills: progressive weakness of the diaphragm and chest muscles cripples the lungs' bellows, causing hypoventilation, CO2 retention and eventual failure—so non-invasive ventilation is a mainstay that extends survival in ALS.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — ALS and multiple sclerosis both cause motor weakness but differ fundamentally: ALS is degenerative death of motor neurons, while MS is autoimmune demyelination with sensory and visual features—so ALS spares sensation and progresses without the relapses of MS.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper links the first ALS gene to oxidative stress: SOD1 is a copper-zinc superoxide dismutase, and many familial ALS mutations make the misfolded enzyme mishandle copper and generate toxic free radicals—so metal-dependent oxidative injury helps kill motor neurons.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — ALS is a relentless disease of the motor nervous system: it kills both upper motor neurons in the cortex and lower motor neurons in the brainstem and cord, so spasticity and wasting advance together until respiratory muscles fail.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Neuroinflammation drives ALS progression: activated microglia and astrocytes plus infiltrating immune cells turn from protective to toxic around dying motor neurons, so the immune system shapes how fast the disease advances—a target for emerging therapies.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — ALS is increasingly seen as a disease of failed protein clearance: motor neurons can't autophagy-degrade misfolded TDP-43 and SOD1, so toxic aggregates accumulate—linking many ALS genes (and the overlap with frontotemporal dementia) to a common disposal defect.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — ALS's SOD1 enzyme is a copper-zinc protein, and zinc is structural to it: mutations that disturb metal binding destabilize SOD1 into toxic aggregates, so the zinc (and copper) chemistry of this antioxidant enzyme sits at the heart of inherited ALS.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome is an emerging factor in ALS: altered gut flora and their metabolites may influence neuroinflammation and disease progression along the gut-brain axis, so the microbiome is being explored as a modifier of this relentless motor-neuron disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — ALS motor neurons die from calcium-driven excitotoxicity: excess glutamate floods them with calcium, and their unusually low calcium-buffering makes them especially vulnerable—the rationale for the glutamate-blunting drug riluzole.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells slow ALS: they restrain the harmful neuroinflammation of microglia, and patients with more functional Tregs progress slower—so expanding Tregs is an experimental therapy for this relentless motor neuron disease.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — ALS overlaps frontotemporal dementia in the hippocampus and cortex: TDP-43 pathology spreads beyond motor neurons to memory and behavior regions, so up to half of ALS patients develop cognitive change—uniting two diseases on one molecular spectrum.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Motor neurons in ALS run out of ATP: failing mitochondria cannot meet the huge energy demand of cells with metre-long axons, so the energy shortfall cripples transport and ion pumping and helps drive the neurons' death.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells infiltrate the dying motor regions in ALS: adaptive immunity adds to microglial inflammation, and the balance between these CD8 cells and protective regulatory T cells helps set how fast the disease advances.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — ALS motor neurons fire too easily through persistent sodium currents: this hyperexcitability stresses the cells and contributes to their loss, and it is partly why riluzole—which curbs sodium currents and glutamate—modestly slows the disease.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — ALS overwhelms the synapse with glutamate: failure to clear this excitatory transmitter floods motor-neuron synapses, and the resulting excitotoxicity helps kill the cells—the process the drug riluzole partly blunts.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages join the attack in ALS: they infiltrate the degenerating peripheral nerves and muscle, and their inflammatory signaling adds to the microglial neuroinflammation that speeds motor-neuron loss.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-α inflames the dying motor regions in ALS: activated microglia and macrophages release this cytokine, and the chronic neuroinflammation it drives is thought to accelerate the loss of motor neurons.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging supports the ALS diagnosis: MRI photons rule out cord compression and other mimics, and can show corticospinal-tract changes, though the diagnosis rests on clinical and electrical findings.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron builds up in the ALS motor cortex: it deposits in the dying motor strip, visible as a dark 'motor band' on MRI, a marker that helps confirm the upper-motor-neuron degeneration.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — ALS eventually defeats swallowing: as bulbar muscles fail, food and saliva are aspirated and nutrition suffers, so a feeding tube into the stomach (PEG) becomes a key supportive step.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals ALS inside the dying motor neuron: cytoplasmic aggregates of TDP-43 protein and rod-like Bunina bodies clog the cell as its axon withers, the pathological signature of the disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eyes are ALS's last refuge: the muscles moving them are spared until the very end, so eye-tracking devices let even locked-in patients keep communicating long after the rest of the body is paralyzed.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Immobility jams the bowel in ALS: weak abdominal and pelvic muscles plus reduced movement bring stubborn constipation, a common and distressing problem as the disease robs the body of motion.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — ALS strikes only the voluntary muscles: it kills the motor neurons driving striated skeletal muscle, sparing the smooth muscle of gut, bladder, and vessels — which is why continence and circulation hold even as limbs fail.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — A treatable mimic must be excluded: multifocal motor neuropathy, driven by anti-GM1 antibodies and responsive to IVIG, can imitate ALS, so antibody testing helps separate the curable impostor from the relentless disease.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — ALS burns through the body's fat: a hypermetabolic state wastes adipose and muscle, and because faster weight loss predicts worse survival, high-calorie feeding has become part of care.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The endocannabinoid system is a symptom target: cannabinoids ease the spasticity, cramps, and excess saliva of ALS and are studied for neuroprotection, since the system also modulates the excitotoxicity that kills motor neurons.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — The mind carries a heavy load and a strange symptom: depression is common facing a terminal diagnosis, and pseudobulbar affect — uncontrollable laughing or crying out of proportion to feeling — arises from the degenerating motor pathways.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Even the heart's autonomic control frays: ALS disturbs the autonomic neurons that regulate the cardiomyocytes, reducing heart-rate variability and adding a dysautonomia to a disease usually thought of as purely motor.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — A growth factor for blood doubles as a nerve protector: VEGF keeps motor neurons alive, and animals engineered with low VEGF develop an ALS-like disease, implicating its deficiency in human motor-neuron degeneration.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The blood's inflammation tracks the decline: a rising neutrophil-to-lymphocyte ratio marks the systemic inflammation of ALS and predicts faster progression, a peripheral readout of a central disease.
- `connects-to` → **[Huntington Disease](../huntingtons-disease/README.md)** — ALS sits in a family of protein-aggregation neurodegenerations: like Huntington's it stems from a toxic misfolded protein and a repeat-expansion gene (C9orf72), the two sharing mechanisms of aggregation and neuronal death.
- `connects-to` → **[TBK1](../../03-molecular/tbk1/README.md)** — TBK1 mutations cause ALS-FTD: loss of this kinase, which links autophagy and innate-immune signaling, impairs clearance of aggregated TDP-43 and stokes neuroinflammation, tying a single gene to both motor and frontotemporal degeneration.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Dying motor neurons light the inflammasome: misfolded SOD1 and TDP-43 activate microglial NLRP3, and the IL-1β it releases amplifies the neuroinflammation that accelerates motor-neuron loss in ALS.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Paralysis breeds clots: the progressive immobility of ALS markedly raises the risk of deep-vein thrombosis and pulmonary embolism, a preventable complication that warrants vigilance as the limbs weaken.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Microglia inflame the dying motor neurons through NF-κB: misfolded proteins activate NF-κB in microglia, driving the cytokine output and NLRP3 priming that turn neuroinflammation into a driver of motor-neuron death.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Bulbar weakness routes food into the lungs: failing swallow and cough cause aspiration pneumonia, which together with ventilator dependence makes infection and sepsis a frequent terminal event in ALS.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Nights are broken by failing muscles: nocturnal hypoventilation, the inability to reposition, cramps and anxiety fragment sleep in ALS, so insomnia is common and worsens daytime fatigue and breathlessness.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Disuse and falls weaken the skeleton: progressive immobility and reduced weight-bearing in ALS drive bone loss, while the falls of failing limbs make osteoporotic fractures a real hazard.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It curiously spares the skin: pressure ulcers are rare in ALS even with profound immobility, attributed to altered dermal collagen, though drooling causes troublesome perioral skin irritation.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Bladder control is usually preserved: ALS characteristically spares the sphincter motor neurons of Onuf's nucleus, so continence is maintained until late, a feature distinguishing it from other neurodegeneration.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Autonomic and sexual function are spared: ALS selectively attacks motor neurons, leaving sexual function and autonomic control largely intact, which shapes counselling and care.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — A treatable mimic: HIV can cause a motor neuron syndrome resembling ALS that may improve with antiretroviral therapy, an important differential to exclude before diagnosis.
- `connects-to` → **[West Nile virus](../west-nile-virus/README.md)** — A virus can destroy the same neurons: West Nile virus attacks anterior-horn motor neurons, causing a poliomyelitis-like acute flaccid paralysis that mimics rapidly progressive motor neuron disease.
- `connects-to` → **[Coxsackievirus B](../../../02-pathogen/01-viruses/coxsackievirus-b/README.md)** — Enteroviruses target motor neurons too: like poliovirus, Coxsackie and other enteroviruses can infect anterior-horn cells and cause acute flaccid paralysis, part of the infectious differential of motor neuron disease.
- `connects-to` → **[Lewy Body Dementia](../lewy-body-dementia/README.md)** — A shared misfolded protein: TDP-43 aggregation links ALS to the frontotemporal dementia it overlaps with and to the TDP-43 co-pathology found in Lewy body dementia, blurring the lines between neurodegenerations.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — The barrier around motor neurons leaks: blood-spinal-cord barrier breakdown and reduced VEGF-driven vascular support contribute to motor-neuron degeneration in ALS, a vascular dimension of the disease.
- `connects-to` → **[Obesity](../obesity/README.md)** — Body fat paradoxically protects: ALS drives a hypermetabolic, weight-losing state, and higher body-mass index and high-calorie nutrition are associated with longer survival, the opposite of most diseases.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Gene-targeted therapy arrives: tofersen, an antisense oligonucleotide silencing mutant SOD1, treats that familial ALS subtype, joining riluzole and edaravone — the vanguard of precision therapy for motor neuron disease.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Failing transport kills the motor neuron: ALS is a dying-back axonopathy in which disrupted axonal transport — many ALS genes encode transport and cytoskeletal proteins — starves the long motor axons before the cell body dies.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Immobility and falls break bone: progressive weakness in ALS causes disuse osteoporosis and frequent falls, so fractures add to the burden of a disease that steadily strips muscle and mobility.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Watching the body fail breeds dread: the relentless progression of paralysis and the fear of suffocation give ALS a heavy burden of anxiety alongside its depression.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Swallowing failure dries out the kidneys: dysphagia limits fluid intake while immobility and recurrent illness add prerenal stress, so chronic dehydration can erode renal function in advanced ALS.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Failing swallow and cough flood the lungs: bulbar and respiratory muscle weakness in ALS causes aspiration and an ineffective cough, and the resulting pneumonia — often pneumococcal — is the leading cause of death.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Progressive paralysis breaks down the skin: as ALS confines patients to bed or wheelchair, immobility and immobile pressure points produce pressure ulcers that heal poorly in the wasted, malnourished body.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — It is not painless as once thought: muscle cramps, spasticity, joint strain from weakness and some sensory involvement give ALS chronic pain, including a neuropathic component, that needs active management.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Bulbar weakness wrecks swallowing: ALS causes dysphagia and sialorrhoea with aspiration and weight loss, driving the need for gastrostomy feeding, while riluzole adds a risk of hepatotoxicity.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It burns fuel abnormally fast: ALS is marked by a hypermetabolic state with raised resting energy expenditure and weight loss, and aggressive nutritional and metabolic support improves survival.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Chronic hypoventilation strains the right heart: the progressive respiratory failure of ALS raises pulmonary pressures toward cor pulmonale, and some patients show autonomic cardiovascular dysfunction.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Respiratory failure is the endgame: motor-neuron loss paralyses the diaphragm, so ventilatory failure at the alveolar gas-exchange surface—not the limb weakness—is the usual cause of death, the reason for non-invasive ventilation.
- `connects-to` → **[NFE2L2](../../03-molecular/nfe2l2/README.md)** — Oxidative-stress defence: motor neurons in ALS suffer oxidative damage, and the NRF2 (NFE2L2) antioxidant pathway is a neuroprotective target—edaravone, an approved ALS drug, is a free-radical scavenger.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — The metabolism paradox: ALS is a hypermetabolic, weight-losing disease, and higher BMI and type-2 diabetes are paradoxically linked to lower ALS risk and slower progression, a clue to its energetics.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Shared genetics with psychosis: C9orf72 and other ALS-FTD genes confer psychiatric features, with raised rates of schizophrenia in affected families—sometimes appearing years before motor symptoms.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Mood in the ALS-FTD spectrum: the C9orf72 expansion that links ALS to frontotemporal dementia also raises rates of mood disorders including bipolar disorder, part of its broad neuropsychiatric prodrome.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Respiratory vulnerability: ALS patients with failing respiratory muscles are at high risk of severe COVID-19, and the infection can precipitate the respiratory failure that ends the disease.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Neurotrophic support: brain-derived neurotrophic factor promotes motor neuron survival, and its decline contributes to neurodegeneration in ALS—a rationale behind neurotrophin trials.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — A neurotrophic candidate: insulin-like growth factor 1 supports motor neuron survival and axonal maintenance and has been trialled, with mixed results, as an ALS therapy.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Gut-brain and feeding: progressive dysphagia in ALS often requires gastrostomy feeding, and an altered gut microbiome and intestinal barrier are increasingly implicated in disease progression.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Innate sensing of mislocalised DNA: TDP-43 pathology in ALS releases mitochondrial DNA that activates the cGAS-STING pathway, driving the type-I interferon neuroinflammation of the disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Microglial cytokine: IL-1β from activated microglia around degenerating motor neurons amplifies the neuroinflammation that accelerates motor-neuron loss in ALS.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory progression: elevated IL-6 reflects the neuroinflammatory and systemic inflammatory activity that tracks with faster decline in ALS.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 is elevated in ALS CSF and recruits inflammatory monocytes to degenerating motor pathways, part of the neuroinflammation driving disease progression.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — TDP-43-driven interferon: cytoplasmic TDP-43 aggregates and leaked nucleic acids activate cGAS-STING to trigger a type-I-interferon response, an inflammatory driver of motor-neuron degeneration in ALS.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement-mediated denervation: complement activation including C3 deposits at the neuromuscular junction and on motor neurons in ALS, contributing to synapse loss and denervation.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3 executes the apoptotic death of motor neurons in ALS, the final common pathway through which excitotoxicity, oxidative stress, and protein aggregation converge to kill upper and lower motor neurons.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Excess nitric oxide reacts with superoxide to form peroxynitrite that damages motor-neuron proteins, lipids, and mitochondria—a central oxidative mechanism especially in the SOD1-mutant form of ALS.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Aggregated proteins and DAMPs released by dying motor neurons engage microglial TLR4, driving the neuroinflammation that shifts microglia to a neurotoxic phenotype and accelerates motor-neuron loss in ALS.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Motor neurons express calcium-permeable AMPA receptors and have low calcium-buffering capacity, so glutamate excitotoxicity floods them with calcium that destroys mitochondria—a selective vulnerability central to ALS neurodegeneration.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Xanthine-oxidase-derived reactive oxygen species add to the oxidative burden killing motor neurons in ALS, the free-radical injury that the antioxidant edaravone targets to slow functional decline.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by activated microglia rises in ALS as a marker of the neuroinflammatory, neurotoxic microglial state, increasingly viewed as both a disease biomarker and a driver of motor-neuron loss.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — IGF-1/PI3K-AKT pro-survival signaling (IGF-1 already mapped) supports motor-neuron survival, and its insufficiency contributes to the motor-neuron death of ALS, a neurotrophic axis explored therapeutically.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Reactive astrocytes in ALS upregulate connexin-43 hemichannels, releasing toxic factors and glutamate that propagate the non-cell-autonomous motor-neuron injury of the disease.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — The balance of anti-apoptotic BCL-2 against pro-apoptotic signals sets the threshold for the caspase-3 motor-neuron apoptosis (already mapped) that executes ALS neurodegeneration.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling in microglia (TLR4 and NF-κB already mapped) drives the chronic neuroinflammation that accelerates motor-neuron loss in ALS.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — cGAS-STING-driven type-I interferon (both already mapped) signals through JAK-STAT to amplify the innate neuroinflammation increasingly implicated in ALS progression.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — Signaling through the TrkB receptor (NTRK), engaged by BDNF and complementing IGF-1 (both already mapped), supports motor-neuron survival whose failure contributes to ALS degeneration.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3-driven reactive astrogliosis is a prominent feature of the neuroinflammatory response in ALS motor-neuron degeneration.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling participates in the stress responses and excitotoxic injury of motor neurons in ALS.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN modulation of the PI3K-AKT-mTOR axis (AKT and mTOR mapped) influences motor-neuron survival, a candidate neuroprotective target in ALS.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling drives the interferon response of activated microglia (cGAS-STING already mapped) contributing to the neuroinflammation of ALS.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling promotes the cytoskeletal and TDP-43 pathology and motor-neuron degeneration of ALS, a candidate therapeutic target.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the astrocyte and microglial responses that balance neuroprotection against neuroinflammation in ALS.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the motor-neuron autophagy and oxidative-stress defense whose failure permits TDP-43 aggregation in ALS.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation of ALS.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and vascular stress responses contribute to motor-neuron vulnerability in ALS.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, coupled to autophagy and mTOR (both already mapped), regulates the proteostasis and metabolic stress of the degenerating motor neurons of ALS.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the neuronal survival pathways whose failure contributes to motor-neuron degeneration in ALS.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic CD8 T cells infiltrate the ALS spinal cord and contribute to motor-neuron injury.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the microglial activation and neuroinflammation of amyotrophic lateral sclerosis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation implicated in amyotrophic lateral sclerosis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven microglial and monocyte recruitment contributes to the neuroinflammation of amyotrophic lateral sclerosis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the microglial and neuroinflammatory responses of amyotrophic lateral sclerosis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses of amyotrophic lateral sclerosis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation of amyotrophic lateral sclerosis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the motor-neuron and glial gene programs of amyotrophic lateral sclerosis.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (A2A receptor) signaling participates in the glutamate-excitotoxicity modulation and neuroinflammation of amyotrophic lateral sclerosis.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microglial activation and neuroinflammation of amyotrophic lateral sclerosis.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Neuroinflammation: MHC class II is upregulated on activated microglia (already mapped) in the ALS spinal cord and motor cortex, marking the antigen-presenting inflammatory state that contributes to the non-cell-autonomous killing of motor neurons.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences: ALS is somewhat more common and earlier-onset in men, and estrogen's neuroprotective effects are proposed to contribute to the sex difference in risk and progression.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Hypermetabolism: ALS features a hypermetabolic state with altered glucose and lipid handling, and insulin resistance is associated with faster progression, a metabolic dimension increasingly targeted in trials.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Regulatory T-cell therapy: low-dose IL-2 expands regulatory T cells that restrain the neuroinflammation (microglia already mapped) driving ALS, a strategy tested in trials to slow the non-cell-autonomous motor neuron death.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Lipid and survival: higher LDL cholesterol and dyslipidaemia are paradoxically associated with longer survival in ALS, part of the hypermetabolic and lipid dysregulation (insulin already mapped) that shapes its metabolic phenotype.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Neurosteroid protection: progesterone-derived neurosteroids are neuroprotective for motor neurons, and together with estrogen (already mapped) may contribute to the modest sex difference in ALS risk and progression.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the activated microglia (already mapped) and the cyclooxygenase pathway contribute to the neuroinflammation (IL-6, TNF and IL-1 already mapped) that accelerates motor neuron death in ALS.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory neuroprotection: the anti-inflammatory IL-10 opposes the microglial pro-inflammatory response (TNF, IL-1 and IL-6 already mapped) driving motor neuron loss, and boosting this arm is a neuroprotective strategy of interest in ALS.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Hypermetabolism and weight loss: ALS is marked by a hypermetabolic state with weight loss, and the fall in the adipokine leptin reflects the fat depletion (cholesterol already mapped) whose faster loss predicts worse survival.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Microglial polarisation: IL-4 polarises the microglia toward a neuroprotective M2 phenotype (IL-10 already mapped), and the balance against the pro-inflammatory activation shapes the motor neuron loss of ALS.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroprotection: IL-13, with IL-4 (already mapped), supports the M2 microglial arm that can be neuroprotective in ALS, part of the neuroimmune balance shaping the progression of the disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium neuroprotection: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity that drives the motor neuron death, a proposed neuroprotective factor in ALS.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Hypermetabolism adipokine: adiponectin, with leptin (already mapped), reflects the hypermetabolism and weight loss that worsen the prognosis of ALS, part of the metabolic (insulin already mapped) dimension of the disease.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine inflammation: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the metabolic and neuroinflammatory (TNF and IL-1 already mapped) dimension of ALS.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium and motor-neuron toxicity: the selenoprotein antioxidant defence of selenium, and the selenium-linked environmental exposures, have been implicated in the oxidative motor-neuron degeneration of ALS.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Non-cell-autonomous astrocytes: the astrocyte toxicity (the impaired glutamate — already mapped — uptake, the reactive astrogliosis) contributes non-cell-autonomously to the motor-neuron death of ALS.
- `connects-to` → **[Peripheral nerve](../../05-tissue/peripheral-nerve/README.md)** — Motor axon degeneration: the lower-motor-neuron axons of the peripheral nerve degenerate (the denervation, the fasciculations and the muscle atrophy) in ALS.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — SOD1 copper toxicity: the mutant SOD1 (the Cu/Zn superoxide dismutase) and the copper-mediated oxidative toxicity are a cause of the familial ALS.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the neuroinflammation (type-I interferon and microglia already mapped) that accelerates the motor-neuron death of ALS.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of ALS.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with ALS.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of ALS.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation associated with ALS.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — NK-mediated motor-neuron injury: the NK cells (perforin already mapped) infiltrate the ALS motor cortex and spinal cord and contribute to the degeneration of the motor neurons (already mapped).
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) activation and the complement-mediated motor-neuron injury of ALS.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) deposit on the motor neurons and the neuromuscular junction, a candidate therapeutic target in ALS.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell neuroinflammation: the mast cells, with the neutrophils, accumulate along the degenerating ALS motor axons and neuromuscular junctions, contributing to the neuroinflammation of ALS.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement deposition on the motor neurons and neuromuscular junction of ALS.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Motor-neuron iron: transferrin, the iron carrier, reflects the disordered iron handling that drives the oxidative stress and ferroptosis of the degenerating motor neurons of ALS.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the neuroinflammation of ALS.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-neuroimmune axis: TSLP, from barrier epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the neuroinflammatory and neuroimmune dimension of ALS.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-neuroinflammation axis: bradykinin, via B1/B2 receptors on microglia (already mapped) and motor-neuron endothelium, amplifies the blood-spinal-cord barrier disruption and the neuroinflammation of ALS.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Contact/complement brake: the C1-esterase inhibitor regulates the classical complement (C3, C5 already mapped) and contact pathways, dampening the complement deposition on motor neurons and neuromuscular junctions of ALS.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell neuroinflammation: mast cells (already mapped) in the spinal-cord (nervous-system already mapped) perivascular niche release histamine that amplifies the blood-spinal-cord barrier permeability and the neuroinflammation of ALS.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Neuroprotective antioxidant: melatonin reduces mitochondrial ROS in motor neurons (already mapped), attenuates the NLRP3-inflammasome (already mapped) and NF-κB activation, and modulates the circadian-clock disruption of ALS.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Motor-neuron EPO: erythropoietin, via EpoR on motor neurons (already mapped) and microglia (already mapped), exerts anti-apoptotic neuroprotection and reduces the neuroinflammation relevant to the motor-neuron degeneration of ALS.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — ALS testosterone: testosterone, via androgen receptors on motor neurons (already mapped) and microglia (already mapped), exerts neuroprotective effects; testosterone deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of ALS.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — ALS serotonin: serotonin, via 5-HT receptors on motor neurons (already mapped) and astrocytes (already mapped), modulates neuroinflammatory tone; serotonin dysregulation amplifies the TDP-43 (already mapped) and NLRP3 (already mapped) neuroinflammatory cascade of ALS.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — ALS prolactin: prolactin, via PRLR on motor neurons (already mapped) and microglia (already mapped), modulates neuroimmune activation; prolactin deficiency amplifies the TDP-43 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of ALS.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Neuroprotective attenuator: oxytocin, via OXTR on motor neurons (already mapped) and microglia (already mapped), attenuates neuroinflammation; oxytocin deficiency amplifies the TDP-43 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of ALS.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Glutamate excitotoxicity modulator: vasopressin, via V1aR on astrocytes (already mapped) and motor neurons (already mapped), modulates glutamate (already mapped) excitotoxicity; vasopressin dysregulation amplifies the TDP-43 (already mapped) and NLRP3 (already mapped) cascade of ALS.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-motor neuron axis: iodine-dependent thyroid hormones modulate motor-neuron (neuron already mapped) survival and astrocyte (already mapped) function; iodine deficiency impairs thyroid-mediated regulation of the TDP-43 (already mapped) and NF-κB (already mapped) cascade of ALS.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — ALS potassium: potassium regulates motor neuron (already mapped) membrane excitability; potassium dysregulation amplifies TDP-43 (already mapped) misfolding and NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) neuroinflammatory cascade in ALS.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — ALS phosphorus: phosphorus fuels motor neuron (already mapped) and astrocyte (already mapped) ATP; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) and TDP-43 (already mapped) neurodegeneration in ALS.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — ALS nitrogen: nitric oxide (NO, nitrogen-derived) in microglia (already mapped) and astrocytes (already mapped) amplifies neuron (already mapped) excitotoxicity; NO excess upregulates NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade in ALS.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — chloride via GABA(A) receptors and KCC2 on motor neurons (already mapped) and astrocytes (already mapped) sets inhibitory tone; chloride dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and TDP-43 (already mapped) motor neuron degeneration in ALS.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — H2S from sulfur-amino acids in motor neurons (already mapped) and astrocytes (already mapped) promotes neuroprotection via K-ATP channels; sulfur deficiency amplifies NLRP3 (already mapped) and NF-κB (already mapped) and TDP-43 (already mapped) motor neuron degeneration in ALS.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — mitochondrial oxygen sustains ATP in motor neurons (already mapped) and astrocytes (already mapped) for axonal transport; hypoxia amplifies NLRP3 (already mapped) and NF-κB (already mapped) and TDP-43 (already mapped) mitochondrial motor neuron degeneration in ALS.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — ALS carbon: carbon backbone of glutamate (already mapped) and TDP-43 (already mapped) in motor neurons (already mapped) and astrocytes (already mapped) drives neuronal metabolism; carbon dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) in ALS.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — ALS hydrogen: hydrogen, via redox homeostasis in motor neurons (already mapped) and astrocytes (already mapped), quenches ROS-driven TDP-43 (already mapped) aggregation; hydrogen dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) cascade of ALS.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — ALS PD-1: PD-1 on regulatory-t-cell (already mapped) and macrophages (already mapped) modulates neuroinflammatory homeostasis; PD-1 dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and TDP-43 (already mapped) motor neuron degeneration cascade of ALS.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — ALS GLP-1: GLP-1 receptor signalling in motor neurons (already mapped) and microglia (already mapped) modulates metabolic neuroinflammation; GLP-1 dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TDP-43 (already mapped) cascade of ALS.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — ALS angiotensin-II: angiotensin-II signalling in motor neurons (already mapped) and astrocytes (already mapped) promotes neuroinflammation; angiotensin-II excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TDP-43 (already mapped) cascade of ALS.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — ALS WNT/β-catenin: WNT/β-catenin in motor neurons (already mapped) and astrocytes (already mapped) supports neurotrophic survival; WNT dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and TDP-43 (already mapped) motor neuron degeneration cascade of ALS.

[^brown-2017-als-review]: Brown RH, Al-Chalabi A. Amyotrophic lateral sclerosis. *N Engl J Med.* 2017;377(2):162-172. [doi:10.1056/NEJMra1603471](https://doi.org/10.1056/NEJMra1603471) · [PubMed 28700839](https://pubmed.ncbi.nlm.nih.gov/28700839/)
[^edaravone-als-2017]: Writing Group, Edaravone ALS 19 Study Group. Safety and efficacy of edaravone in well defined patients with amyotrophic lateral sclerosis. *Lancet Neurol.* 2017;16(7):505-512. [doi:10.1016/S1474-4422(17)30115-1](https://doi.org/10.1016/S1474-4422(17)30115-1) · [PubMed 28522180](https://pubmed.ncbi.nlm.nih.gov/28522180/)
[^miller-2023-tofersen-als]: Miller TM, Cudkowicz ME, Genge A, et al. Trial of Antisense Oligonucleotide Tofersen for SOD1 ALS. *N Engl J Med.* 2022;387(12):1099-1110. [doi:10.1056/NEJMoa2204705](https://doi.org/10.1056/NEJMoa2204705) · [PubMed 36129998](https://pubmed.ncbi.nlm.nih.gov/36129998/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
