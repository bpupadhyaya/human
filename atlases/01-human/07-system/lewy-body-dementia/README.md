---
schema: human-scale-entry/v1
id: lewy-body-dementia
name: Lewy Body Dementia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "DLB (dementia with Lewy bodies) is the 2nd most common neurodegenerative dementia; core features: fluctuating cognition, visual hallucinations, RBD, parkinsonism; cortical alpha-synuclein Lewy body pathology; fatal neuroleptic sensitivity; rivastigmine for cognition."
aliases: ["DLB", "dementia with Lewy bodies", "Lewy body disease", "LBD", "diffuse Lewy body disease", "Lewy body dementia", "PDD", "Parkinson's disease dementia", "synucleinopathy dementia"]
sources:
  - id: mckeith-2017-dlb-criteria
    type: peer-reviewed
    cite: "McKeith IG, Boeve BF, Dickson DW, et al. Diagnosis and management of dementia with Lewy bodies: Fourth consensus report of the DLB Consortium. Neurology. 2017;89(1):88-100."
    doi: "10.1212/WNL.0000000000004058"
    pmid: "28592453"
    url: "https://doi.org/10.1212/WNL.0000000000004058"
    accessed: "2026-06-08"
  - id: spillantini-1997-lewy-body
    type: peer-reviewed
    cite: "Spillantini MG, Schmidt ML, Lee VM, Trojanowski JQ, Jakes R, Goedert M. Alpha-synuclein in Lewy bodies. Nature. 1997;388(6645):839-840."
    doi: "10.1038/42166"
    pmid: "9278044"
    url: "https://doi.org/10.1038/42166"
    accessed: "2026-06-08"
  - id: walker-2015-dlb-review
    type: peer-reviewed
    cite: "Walker Z, Possin KL, Boeve BF, Aarsland D. Lewy body dementias. Lancet. 2015;386(10004):1683-1697."
    doi: "10.1016/S0140-6736(15)00462-6"
    pmid: "26595642"
    url: "https://doi.org/10.1016/S0140-6736(15)00462-6"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "DLB and PD are both alpha-synuclein synucleinopathies; 1-year rule: dementia ≤1 year of parkinsonism → DLB; parkinsonism >1 year before dementia → PDD; SNCA pathology distribution differs — DLB has early cortical Lewy bodies while PD follows Braak brainstem→cortex staging."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "50-70% of DLB cases have concurrent Alzheimer co-pathology (Aβ plaques, tau tangles); AD and DLB share APOE4 as a risk factor; DLB with high AD co-pathology has faster cognitive decline; anti-amyloid antibodies (lecanemab) may have a role in DLB with concurrent Aβ pathology."
  - target: 01-human/03-molecular/snca
    relation: connects-to
    note: "Alpha-synuclein (SNCA) Lewy body pathology in limbic cortex and neocortex is the defining neuropathology of DLB; SNCA seed amplification assay (SAA/RT-QuIC) in CSF or skin is >90% sensitive for DLB; SNCA S129 phosphorylation marks Lewy body alpha-synuclein in DLB and PD equally."
  - target: 01-human/03-molecular/mapt
    relation: connects-to
    note: "Tau co-pathology is present in 50-70% of DLB brains; MAPT H1 haplotype is a risk factor for DLB; tau and alpha-synuclein co-aggregate via cross-seeding; DLB cases with high tau burden have faster progression and worse cognitive outcomes than pure alpha-synuclein pathology."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "DLB Lewy bodies accumulate in limbic cortex, cingulate, and occipital cortex → visual hallucinations (occipital hypometabolism); brainstem (substantia nigra) involvement causes parkinsonism; diffuse cortical cholinergic denervation (80% ChAT loss) drives cognitive fluctuations."
  - target: 01-human/03-molecular/tdp-43
    relation: connects-to
    note: "TDP-43 co-pathology in ~50% of DLB brains drives hippocampal atrophy and memory impairment independent of Lewy body burden; TDP-43 inclusions in hippocampal CA1 and entorhinal cortex accelerate cognitive decline; co-pathology predicts faster dementia progression in DLB patients."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Lewy body dementia carries the most severe cholinergic deficit — ~80% loss of cortical choline acetyltransferase, worse than Alzheimer's — driving fluctuating attention and visual hallucinations, and explaining why cholinesterase inhibitors help DLB more than AD."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Treating the parkinsonism of Lewy body dementia with dopamine agonists can unleash impulse-control disorders (gambling, hypersexuality, compulsive shopping) by over-stimulating mesolimbic reward circuits; recognizing and dose-reducing is essential."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Lewy bodies are intraneuronal inclusions of misfolded alpha-synuclein; in DLB they fill cortical and limbic neurons, and selective loss of cholinergic, dopaminergic, and noradrenergic neurons produces the dementia, parkinsonism, and dysautonomia."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep disorder is a core, often first feature of Lewy body dementia: REM sleep behavior disorder—acting out dreams from loss of REM atonia—can precede dementia by years and strongly predicts a synucleinopathy; LBD also brings fragmented sleep and daytime somnolence."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression is common and often early in Lewy body dementia: degeneration of monoaminergic brainstem nuclei (serotonin, noradrenaline) plus cognitive and motor decline drive mood symptoms that can predate the dementia, complicating the distinction from late-life depression."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Neuroinflammation accompanies Lewy body dementia: microglia activated by misfolded α-synuclein release pro-inflammatory cytokines and reactive species that amplify neuronal injury and may spread pathology; PET shows microglial activation tracking disease, a therapeutic target."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "REM sleep behavior disorder bridges Lewy body dementia and narcolepsy: RBD—acting out dreams from lost REM muscle atonia—is an early marker that often precedes Lewy body dementia by years, while narcolepsy disrupts the same REM gating from orexin loss."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes participate in Lewy body dementia's α-synuclein pathology: reactive astrocytes accumulate α-synuclein and, with microglia, drive the neuroinflammation that accompanies the spreading synucleinopathy, so glial dysfunction contributes alongside neuronal loss."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine loss links Lewy body dementia to its parkinsonism: α-synuclein degeneration of nigrostriatal dopamine neurons produces the rigidity and bradykinesia, and a DaT scan showing reduced striatal dopamine transporter helps distinguish LBD from Alzheimer's disease."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "Lewy body dementia and Huntington's are neurodegenerative movement-and-cognition disorders with distinct causes: LBD from α-synuclein (parkinsonism, hallucinations), Huntington's from a CAG repeat (chorea)—different proteins, overlapping decline."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Lewy body dementia is defined partly by psychosis that mimics schizophrenia: visual hallucinations and delusions are core features, but unlike schizophrenia they arise in older adults with parkinsonism, and antipsychotics can cause life-threatening sensitivity in LBD."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Lewy body dementia spares the hippocampus more than Alzheimer's early on: memory is relatively preserved while attention, visuospatial function and alertness fluctuate, reflecting cortical and brainstem Lewy pathology not hippocampal degeneration."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Lewy body dementia is a multisystem nervous-system synucleinopathy: alpha-synuclein deposits spread beyond cortex to autonomic and brainstem neurons, so beyond cognition it causes dysautonomia, REM sleep behavior disorder and parkinsonism—a whole-nervous-system disease."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Norepinephrine loss drives Lewy body dementia's autonomic and cognitive features: degeneration of the noradrenergic locus coeruleus contributes to orthostatic hypotension, attention fluctuations and arousal problems that distinguish LBD from Alzheimer's."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "REM sleep behavior disorder is a hallmark of Lewy body dementia: loss of normal REM atonia lets patients act out dreams, often years before dementia, and melatonin is a first-line treatment—making this sleep disturbance an early diagnostic clue."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Lewy body dementia is a failure of protein clearance: when autophagy can't degrade misfolded alpha-synuclein, it aggregates into the Lewy bodies that poison neurons, so boosting this cellular recycling system is a target shared with Parkinson's disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Lewy body dementia often starts in the gut: constipation and alpha-synuclein deposits in enteric nerves can precede cognitive and motor signs by years, echoing Parkinson's 'gut-first' route along the vagus nerve into the brain."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart helps diagnose Lewy body dementia: alpha-synuclein damages cardiac sympathetic nerves, so a MIBG scan shows reduced cardiac uptake—a marker that distinguishes Lewy body disease from Alzheimer's and other dementias."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Vivid visual hallucinations set Lewy body dementia apart: degeneration in visual-processing pathways makes well-formed hallucinations (often of people or animals) a core early feature, helping distinguish it from Alzheimer's at the bedside."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Lewy body dementia is treated partly by tuning glutamate: the NMDA-blocker memantine dampens excitotoxic glutamate signaling to modestly help cognition, complementing the cholinesterase inhibitors that target the disease's severe acetylcholine loss."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Brain iron accumulation feeds Lewy body disease: iron builds up in vulnerable neurons and catalyzes oxidative stress that promotes alpha-synuclein aggregation, linking a metal imbalance to the protein clumping at the disease's core."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Lewy body disease may begin in the gut: alpha-synuclein clumps appear in the intestinal nerves years before dementia, and constipation is a common early warning, supporting the idea that the pathology can climb the vagus nerve from gut to brain."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Lewy body dementia injures the brain's white matter: alpha-synuclein and degeneration affect oligodendrocytes and myelinated tracts, so disrupted connectivity between regions adds to the cholinergic loss behind the fluctuating cognition."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper binds alpha-synuclein directly: the protein has a copper-grabbing site, and disordered copper handling shifts synuclein toward the misfolded, aggregation-prone form, so a second metal beyond iron is tied to the Lewy body's core protein."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Lewy body dementia is a disease of failing synapses: alpha-synuclein normally works at the presynaptic terminal, and its misfolding cripples neurotransmitter release before cells die, so synaptic breakdown underlies the fluctuating cognition."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Lewy body dementia can be found in the skin: misfolded alpha-synuclein deposits in the tiny nerves of the skin, so a simple skin biopsy can now help confirm the synuclein disease behind the dementia."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Lewy body dementia starves neurons of ATP: like Parkinson's, it carries mitochondrial dysfunction that limits cellular energy, and the brain's demanding neurons falter as their power supply fails."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging helps pin down Lewy body dementia: a DaTscan's photons show the dopamine loss, and cardiac MIBG scintigraphy reveals the sympathetic denervation that helps separate it from Alzheimer's."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Lewy body dementia attacks the autonomic nerves: synuclein in the peripheral autonomic system causes orthostatic hypotension, constipation and bladder trouble, often years before the dementia appears."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Aspiration pneumonia is the common end of Lewy body dementia: as swallowing fails late in the disease, inhaled food infects the lungs, the frequent immediate cause of death."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the disease's namesake: Lewy bodies, dense spherical cores of aggregated alpha-synuclein filaments, fill neurons across the cortex — the same protein clumps as Parkinson's, but spread widely enough to steal cognition."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium handling fails in the dying neurons: misfolded alpha-synuclein disrupts the cell's calcium balance and the mitochondria that buffer it, an energy-and-calcium crisis that helps drive the widespread neuronal death."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Lewy body disease wrecks the autonomic system: synuclein deposits damage the sympathetic nerves that command the adrenal-driven blood-pressure response, so fainting orthostatic hypotension is a prominent, early feature."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Lewy body disease unsettles sleep and wakefulness: synuclein damage to orexin-related arousal systems brings excessive daytime sleepiness and the dream-enacting REM sleep behavior disorder that often heralds it years early."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Autonomic failure stalls the body's smooth muscle: beyond fainting blood pressure, Lewy body disease slows gut and bladder smooth muscle into constipation and urinary trouble — non-motor features that often precede the dementia."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Treatment may one day come as antibody, and mimics must be excluded: anti-α-synuclein antibodies are being trialed to clear the aggregates, while autoimmune (antibody-mediated) encephalitis is a treatable mimic ruled out in rapidly progressive cases."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The heart helps make the diagnosis: Lewy body disease degenerates the cardiac sympathetic nerves supplying the cardiomyocytes, so reduced MIBG uptake on a cardiac scan is a distinctive marker separating it from Alzheimer's."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The gut shows it early: Lewy pathology in the enteric nerves slows the stomach into gastroparesis and early satiety years before dementia, and α-synuclein found on gut biopsy may become an early clue."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The disease may begin in the gut: under the gut-first hypothesis, misfolded α-synuclein arises in the enteric nervous system and climbs the vagus to the brain, with gut dysbiosis a suspected early player."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "The immune system reads α-synuclein as foreign: cytotoxic T cells recognizing synuclein peptides are found in synucleinopathies and may help kill the neurons, adding an autoimmune arm to Lewy body disease."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Lewy pathology dims more than dopamine: degeneration of the serotonergic raphe lowers serotonin, contributing to the depression, anxiety, and REM-sleep disturbance that often shadow the cognitive decline."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Synucleinopathies and melanoma travel together: as in Parkinson's, Lewy body disease carries a higher melanoma risk, a bidirectional link rooted in shared pigment and α-synuclein biology."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Misfolded α-synuclein is a danger signal: it activates microglial NLRP3, driving IL-1β release and chronic neuroinflammation that amplifies neuronal loss — making NLRP3 a candidate target to slow Lewy body disease."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The immune brake is loosened in synucleinopathy: regulatory T cells normally restrain microglial reactivity to α-synuclein, and their declining number and function lets neuroinflammation run unchecked, accelerating degeneration."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pain is an under-recognized burden of Lewy body disease: α-synuclein degeneration of small autonomic and sensory fibres plus central pain-modulation deficits produce neuropathic and central pain alongside the parkinsonism."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Microglia inflame the synuclein-laden brain: α-synuclein activates NF-κB in microglia, driving the cytokine output and NLRP3 priming that accelerate the neuronal loss of Lewy body disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Falls meet fragile bones: the parkinsonism, orthostatic hypotension and cognitive lapses of Lewy body dementia cause frequent falls, while immobility and low vitamin D thin the bones — a combination that makes fractures common."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Swallowing fails late in the disease: advancing Lewy body dementia brings dysphagia and aspiration, so aspiration pneumonia and the sepsis it triggers are a frequent terminal event."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its autonomic failure reaches the heart: Lewy body disease causes cardiac sympathetic denervation and severe orthostatic hypotension, and the dysautonomia complicates and overlaps with heart failure in these frail patients."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Vascular injury muddies the picture: cerebrovascular disease frequently coexists with Lewy body pathology, and stroke can add to or be mistaken for its fluctuating cognition in a mixed dementia."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety rides the cognitive fluctuations: marked anxiety is common in Lewy body dementia, worsened by the disease's fluctuating attention, visual hallucinations and autonomic instability."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Swallowing fails as the disease advances: dysphagia in Lewy body dementia causes aspiration, and the resulting pneumonia — often pneumococcal — is a leading immediate cause of death."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "Infection unmasks the fluctuating brain: a urinary tract infection, commonly E. coli, can abruptly worsen the cognition and hallucinations of Lewy body dementia, triggering florid delirium beyond its usual fluctuations."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Late immobility breaks down the skin: as Lewy body dementia advances to a bedbound state, pressure ulcers form over bony prominences and heal poorly in the frail, malnourished patient."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Autonomic failure drops the blood pressure: Lewy body dementia disrupts cardiovascular autonomic control, causing orthostatic hypotension and syncope that lead to falls, a hallmark of its dysautonomia."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Parkinsonism and falls batter the skeleton: the rigidity, bradykinesia and postural instability of Lewy body dementia cause frequent falls with fractures, and late immobility brings contractures and sarcopenia."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Autonomic dysfunction unsettles the bladder: Lewy body dementia impairs autonomic bladder control, causing urinary urgency, incontinence and retention with recurrent infection."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Swallowing failure floods the lungs: dysphagia in Lewy body dementia causes aspiration pneumonia, a leading cause of death, while REM sleep behaviour disorder disrupts breathing and sleep."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Misfolded protein stirs brain inflammation: alpha-synuclein aggregation provokes microglial neuroinflammation, an immune response implicated in the progression of Lewy body dementia."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Immobility and drug sensitivity reach the skin: it brings pressure sores and seborrhoeic skin changes, while its severe neuroleptic sensitivity can trigger rigidity and neuroleptic malignant syndrome."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Like other dementias it may fail to clear its waste protein: impaired glymphatic drainage during sleep is implicated in the build-up of alpha-synuclein that defines Lewy body disease."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Early autonomic failure reaches the pelvis: erectile dysfunction and urinary disturbance often precede the cognitive decline of Lewy body dementia by years."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "Mood symptoms are common but drugs need care: SSRIs like fluoxetine treat the frequent depression, while antipsychotics must be used with great caution given the severe neuroleptic sensitivity of Lewy body dementia."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Autonomic and circadian control fails: Lewy pathology in the hypothalamus and autonomic ganglia disrupts blood-pressure regulation, temperature and circadian rhythm, producing the orthostatic hypotension and sleep-wake disturbance of DLB."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Seizures complicate the failing brain: like other neurodegenerative dementias, Lewy body dementia carries a raised risk of seizures and myoclonus as cortical networks degenerate."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "A shared misfolded protein: TDP-43 co-pathology is found in a large minority of Lewy body dementia brains, linking it to the TDP-43 proteinopathy that defines amyotrophic lateral sclerosis."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It denervates the heart: like Parkinson's, Lewy body dementia causes cardiac sympathetic denervation, so reduced MIBG uptake in the myocardium helps distinguish it from Alzheimer's and contributes to orthostatic hypotension."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "α-synuclein clogs the axon: Lewy bodies are aggregates of α-synuclein that impair axonal transport in neurons, contributing to the synaptic failure and degeneration that drive its fluctuating cognition and hallucinations."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "It may begin in the gut: α-synuclein pathology is found in the enteric nerves of the gut wall years before dementia, supporting a body-first route where the protein ascends the vagus to the brain (the Braak hypothesis)."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "The synucleinopathy autonomic clue: LBD damages cardiac sympathetic nerves and autonomic control, causing orthostatic hypotension and heart-rate dysregulation—cardiac sympathetic denervation is a diagnostic marker."
  - target: 01-human/03-molecular/lrrk2
    relation: connects-to
    note: "Shared genetics with Parkinson's: LRRK2 mutations cause familial parkinsonism and contribute to Lewy-body pathology, tying the genetics of synucleinopathy across Parkinson's disease and dementia with Lewy bodies."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Inflammation that prunes synapses: activated microglia and complement C3 tag and eliminate synapses in Lewy-body dementia, a mechanism of the synaptic loss that drives the cognitive decline."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Infection unmasks fragility: COVID-19 commonly precipitates delirium and accelerates cognitive decline in Lewy-body dementia, whose patients are acutely vulnerable to any systemic insult."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Metabolism and the ageing brain: type 2 diabetes and insulin resistance raise the risk and pace of dementias including Lewy-body disease, through vascular injury and impaired neuronal glucose handling."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Falls and fractures: the parkinsonism, orthostatic hypotension and cognitive fluctuations of Lewy-body dementia cause frequent falls, fracturing the cortical bone of already osteoporotic elderly patients."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Aspiration ends it: dysphagia in advanced Lewy-body dementia leads to aspiration pneumonia, seeding the alveoli with oral flora—the leading cause of death as in other neurodegenerative diseases."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Anxiety as a prodrome: prominent anxiety and panic are common non-motor and prodromal features of Lewy-body dementia, often preceding the cognitive and motor signs by years."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Late-life mood instability: new-onset mood disturbance in older adults can herald an emerging synucleinopathy like Lewy-body dementia, blurring the line between primary mood disorder and neurodegeneration."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neuroinflammation: IL-1β from microglia activated around α-synuclein aggregates amplifies the inflammatory cascade that drives neuronal loss in Lewy-body dementia."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory neurodegeneration: elevated TNF-α reflects the chronic microglial activation accompanying the synucleinopathy of Lewy-body dementia, contributing to progressive neuronal injury."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Cortical inhibition: loss of GABAergic interneurons contributes to the fluctuating attention, visual hallucinations and cognitive instability characteristic of Lewy-body dementia."
  - target: 01-human/03-molecular/apoe
    relation: connects-to
    note: "Shared genetic risk: the APOE4 allele raises risk not only for Alzheimer's but also for Lewy-body dementia, linking lipid handling and amyloid co-pathology to the synucleinopathy."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Microglial recruitment: CCL2 released in the synuclein-burdened brain draws monocytes and amplifies the microglial neuroinflammation that accelerates neurodegeneration in Lewy-body dementia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA-sensing inflammation: mitochondrial DNA leaked from stressed neurons activates cGAS-STING in microglia, an emerging driver of the neuroinflammatory response to α-synuclein pathology."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "α-Synuclein sensing: aggregated α-synuclein released from dying neurons activates microglial TLR4, propagating the chronic neuroinflammation that spreads Lewy pathology through the cortex in Lewy-body dementia."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Iron accumulation: dysregulated ferroportin-controlled iron handling lets iron accumulate in vulnerable neurons of Lewy-body dementia, sensitising them to the oxidative and ferroptotic death that accompanies synuclein pathology."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Neuronal apoptosis: caspase-3 executes the apoptotic death of cortical and brainstem neurons in Lewy-body dementia, the cell-loss endpoint of α-synuclein toxicity, mitochondrial failure and neuroinflammation."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium dyshomeostasis: α-synuclein aggregates form membrane pores and disrupt calcium handling, and the resulting calcium overload stresses mitochondria — a mechanism of neuronal vulnerability shared with the substantia-nigra neurons lost in Parkinson's."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial driver: galectin-3 released by microglia activated around Lewy pathology amplifies the neuroinflammatory response, a microglial signal increasingly implicated as a driver of α-synucleinopathy neurodegeneration."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Lost trophic support: declining BDNF removes neurotrophic support for the cortical and brainstem neurons targeted in Lewy-body dementia, contributing to the synaptic loss behind the fluctuating cognition and visual hallucinations."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative defence: oxidative stress drives the α-synuclein aggregation and neurodegeneration of Lewy-body dementia, and a declining NRF2 antioxidant response permits this damage, as in the related Parkinson's disease."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "α-synuclein clearance: mTOR restrains the autophagy (already mapped) that clears α-synuclein, and its dysregulation impairs the lysosomal clearance whose failure allows Lewy bodies to accumulate."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Neuroinflammation: IL-6 from the activated microglia (already mapped) contributes to the neuroinflammation, with IL-1β and TNF-α, that accelerates the neurodegeneration of Lewy-body dementia."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate neuroinflammation: aggregated α-synuclein (SNCA already mapped) engages microglial TLRs that signal through MyD88 to NF-κB, sustaining the chronic innate-immune activation that drives Lewy-body neurodegeneration."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Dual proteinopathy: GSK-3β phosphorylates tau (MAPT already mapped) and modulates α-synuclein toxicity, mechanistically linking the combined tau and synuclein pathology characteristic of Lewy body dementia."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophic decline: BDNF signalling through its TrkB receptor (NTRK) supports neuronal survival, and the loss of this trophic support accelerates the cholinergic and cortical degeneration of Lewy body dementia."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling (GSK-3β and mTOR mapped) maintains neuronal survival and regulates α-synuclein-related autophagy, its decline contributing to neurodegeneration in Lewy body dementia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-driven JAK-STAT signalling sustains the microglial and astrocytic neuroinflammation accompanying α-synuclein pathology in Lewy body dementia."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3-driven reactive astrogliosis is part of the neuroinflammatory response to Lewy pathology in Lewy body dementia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling drives the interferon-responsive microglial activation contributing to the neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling transduces the cytokine and growth-factor stimuli that modulate neuronal stress and glial activation in Lewy body dementia."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN regulation of PI3K-AKT survival signalling (AKT already mapped) shapes the autophagy and neuronal vulnerability relevant to α-synuclein clearance in Lewy body dementia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the neuronal autophagy and oxidative-stress defense whose failure permits α-synuclein accumulation in Lewy body dementia."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and mitochondrial stress responses contribute to the neurodegeneration of Lewy body dementia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, coupled to autophagy (autophagy already mapped), regulates the clearance of α-synuclein aggregates in Lewy body dementia."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the neuronal survival pathways whose failure contributes to Lewy body dementia."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic CD8 T cells infiltrate the brain and contribute to the neurodegeneration of Lewy body dementia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (FYN) kinase signaling participates in the α-synuclein-linked synaptotoxicity and neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation (including SNCA regulation) implicated in Lewy body dementia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven microglial and monocyte recruitment contributes to the neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the microglial and neuroinflammatory responses of Lewy body dementia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses of Lewy body dementia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neuronal gene programs of Lewy body dementia."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (A2A receptor) signaling participates in the synaptic dysfunction and neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microglial activation and neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Urate and oxidative stress: low serum urate, a product of xanthine oxidase with antioxidant properties, is associated with increased risk and faster progression of synucleinopathies, implicating oxidative stress in Lewy body dementia."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences: Lewy body dementia is more common in men, and estrogen's neuroprotective effects on dopaminergic and cholinergic neurons (acetylcholine already mapped) are proposed to contribute to the sex difference in risk."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Brain insulin resistance: impaired cerebral insulin signalling is common across the dementias, including Lewy body dementia, where it worsens neuronal energetics and may accelerate the alpha-synuclein neurodegeneration."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Adaptive autoimmunity: alpha-synuclein-specific T cells expanded through IL-2 signalling are found in the synucleinopathies, implicating an adaptive immune response against the aggregating protein (already mapped) in the neurodegeneration of Lewy body dementia."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid protection: progesterone-derived neurosteroids are neuroprotective and support cholinergic (already mapped) neurons, and together with estrogen (already mapped) may contribute to the sex differences in Lewy body dementia."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Microglial polarisation: IL-4 shifts microglia (already mapped) toward a reparative, anti-inflammatory phenotype, and enhancing this arm against the pro-inflammatory TNF/IL-1 response is a neuroprotective strategy of interest in Lewy body dementia."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the activated microglia (already mapped) contribute to the neuroinflammation that drives the alpha-synuclein pathology (already mapped) and neuronal loss of Lewy body dementia."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "APOE lipid handling: cholesterol metabolism, governed by APOE (already mapped), influences alpha-synuclein aggregation and membrane biology, part of the lipid dimension of the neurodegeneration in Lewy body dementia."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory neuroprotection: IL-10, with IL-4 (already mapped), opposes the microglial pro-inflammatory response (TNF, IL-1 and IL-6 already mapped) driving neuronal loss, and boosting this arm is a neuroprotective strategy of interest in Lewy body dementia."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and synuclein: zinc, with the copper and iron (already mapped), binds alpha-synuclein (already mapped) and modulates its aggregation and the oxidative stress, part of the metal dyshomeostasis of the neurodegeneration in Lewy body dementia."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium neuroprotection: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity on the vulnerable neurons, a proposed neuroprotective factor in Lewy body dementia."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Omega-3 and brain lipids: the omega-3 fatty acid DHA is a major brain membrane lipid (cholesterol and APOE already mapped), and its pro-resolving mediators counter the neuroinflammation of Lewy body dementia, of dietary interest for neuroprotection."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation (NLRP3, TNF and IL-1 already mapped) of Lewy body dementia."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic neuroprotection: leptin has neurotrophic and neuroprotective actions on the neurons (already mapped), and the metabolic dysregulation (insulin already mapped) it reflects is linked to the neurodegeneration of Lewy body dementia."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Brain-iron regulation: hepcidin governs the iron (already mapped) handling whose dysregulation contributes to the brain-iron accumulation (ferroportin already mapped) and the metal-catalysed oxidative injury of Lewy body dementia."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Neuroinflammation: the microglial activation and the neuroinflammation (TNF, IL-1 and NLRP3 already mapped) drive the α-synuclein (already mapped) neurodegeneration of Lewy body dementia."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Neuronal loss: the cortical and the cholinergic/dopaminergic (acetylcholine and dopamine already mapped) neurons, laden with the Lewy bodies (α-synuclein already mapped), degenerate in Lewy body dementia."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Brain-iron oxidative injury: the iron accumulates in the degenerating brain (ferroportin and hepcidin already mapped) and catalyses the oxidative injury and the α-synuclein aggregation of Lewy body dementia."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the mitochondrial DNA, drives the microglial (already mapped) neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu of Lewy body dementia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the neuroinflammation (IL-6 and TNF already mapped) of Lewy body dementia."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the adaptive-immune contribution to the α-synuclein (already mapped) neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune interaction in Lewy body dementia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) activation and the complement-mediated synapse loss of Lewy body dementia."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the complement-driven neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Brain iron: transferrin, the iron carrier, is central to the brain-iron dysregulation (ferroportin already mapped) that drives the oxidative stress and ferroptosis of the α-synucleinopathy of Lewy body dementia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-mediated synapse loss of Lewy body dementia."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway (C1q-initiated) implicated in the synaptic pruning of the α-synucleinopathy of Lewy body dementia."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments present the alpha-synuclein (already mapped) antigen to the T cells (already mapped) in the neuroinflammation of Lewy body dementia."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-neuroinflammatory axis: TSLP, from gut-epithelium (gut-microbiome already mapped) under the autonomic dysfunction and dysbiosis of Lewy body dementia, primes dendritic cells (already mapped) and mast cells (already mapped) and amplifies the gut-brain neuroinflammation."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-neuroinflammatory axis: bradykinin, via B2R on CNS microglia (already mapped) and neurons (already mapped), amplifies the BBB permeability and the neuroinflammation contributing to the α-synuclein (already mapped) propagation of Lewy body dementia."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective EPO: erythropoietin, via EpoR on neurons (already mapped) and oligodendrocytes (already mapped), exerts neuroprotective and anti-apoptotic effects relevant to the dopaminergic (dopamine already mapped) and non-dopaminergic neurodegeneration of Lewy body dementia."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histaminergic sleep-wake: histamine, from the tuberomammillary nucleus (already mapped as hypothalamus-linked brain circuit), is a principal wake-promoting transmitter; the severe REM-sleep-behaviour disorder of Lewy body dementia disrupts the histaminergic arousal circuit."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "CNS-border ECM: periostin, from astrocytes (already mapped) and meningeal fibroblasts, contributes to the perivascular ECM remodelling and the neuroinflammation (IL-1b, TNF already mapped) of the Lewy body dementia brain."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Neuroprotective androgen: testosterone and its metabolite DHT exert neuroprotective effects on dopaminergic neurons (already mapped); falling testosterone in ageing is associated with greater α-synuclein (already mapped) pathology and Lewy body dementia risk."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "LBD prolactin: prolactin, via PRLR on neurons (already mapped) and microglia (already mapped), modulates neuroinflammation; prolactin deficiency amplifies the dopamine (already mapped) dysregulation and the melatonin (already mapped) sleep-wake disruption of Lewy body dementia."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "LBD oxytocin: oxytocin, via OXTR on neurons (already mapped) and microglia (already mapped), reduces neuroinflammation and α-synuclein (already mapped) spread; oxytocin attenuates the norepinephrine (already mapped) and IL-6 (already mapped) hyperarousal of Lewy body dementia."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "LBD vasopressin: vasopressin, via V1aR on neurons (already mapped) and microglia (already mapped), modulates CSF osmolality; vasopressin dysregulation amplifies norepinephrine (already mapped) and NLRP3 (already mapped) neuroinflammation of Lewy body dementia."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "LBD selenium: selenium, via GPx and NRF2 (already mapped) antioxidants, protects neurons (already mapped) from ROS and α-synuclein (already mapped) aggregation-driven injury; selenium deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) neuroinflammation of LBD."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "LBD iodine: iodine-dependent thyroid hormones regulate neuronal (neuron already mapped) metabolism and dopamine (already mapped) synthesis; hypothyroidism amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and α-synuclein (already mapped) burden in LBD."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "LBD sodium: sodium, via voltage-gated channels on neurons (already mapped), regulates action-potential firing; dysregulated sodium from microglial (already mapped) NLRP3 (already mapped) neuroinflammation amplifies NF-κB (already mapped) and dopamine (already mapped) in LBD."
---

# Lewy Body Dementia

## Overview

**Lewy body dementia (LBD)** encompasses two closely related synucleinopathy syndromes — **dementia with Lewy bodies (DLB)** and **Parkinson's disease dementia (PDD)** — that share the same neuropathological substrate (alpha-synuclein Lewy bodies in cortex and brainstem) but differ in the temporal relationship between dementia and parkinsonism onset. Together, the Lewy body dementias are the **second most common neurodegenerative dementia** after Alzheimer's disease, accounting for 15–20% of all dementia cases and affecting approximately **1.4 million Americans** [^walker-2015-dlb-review].

**The 1-year rule (DLB vs PDD distinction):**
- **DLB**: Dementia onset precedes parkinsonism, or dementia and parkinsonism appear within 1 year of each other
- **PDD**: Parkinson's disease diagnosed >1 year before dementia onset

This arbitrary temporal distinction reflects the same underlying pathological spectrum, and both syndromes are now grouped clinically as "Lewy body dementia" in practice, though they retain distinct diagnostic criteria (McKeith DLB Consortium criteria for DLB; MDS criteria for PDD). The shared pathomechanism — alpha-synuclein aggregation and Lewy body formation — makes DLB and PDD distinct from Alzheimer's disease (amyloid-β/tau), despite significant clinical overlap and frequent co-pathology.

Lewy body dementia is severely underdiagnosed — the mean time from symptom onset to diagnosis exceeds 1.5 years, and misdiagnosis (most often as Alzheimer's disease) leads to **potentially fatal treatment errors**, particularly iatrogenic neuroleptic sensitivity reactions.

## Structure

### Neuropathological substrate

The defining pathology of DLB is the accumulation of **alpha-synuclein Lewy bodies** in the cerebral cortex and brainstem [^spillantini-1997-lewy-body]. Unlike Parkinson's disease (where Braak staging predicts early brainstem → late cortical spread), DLB typically shows early and prominent **cortical and limbic** Lewy body pathology:

**LB distribution in DLB (McKeith pathological staging):**

| Stage | Lewy body distribution | Clinical correlation |
|:---|:---|:---|
| **Brainstem predominant** | Dorsal motor nucleus of vagus, locus coeruleus, substantia nigra | Autonomic dysfunction, parkinsonism (often absent at DLB onset) |
| **Limbic (transitional)** | Amygdala, hippocampus, entorhinal cortex, cingulate gyrus | Memory impairment, visual hallucinations |
| **Neocortical** | Temporal, parietal, frontal association cortex | Global cognitive impairment, psychiatric features, severe dementia |

Most DLB patients have **neocortical Lewy body burden at diagnosis** — explaining why cognitive impairment rather than parkinsonism is the presenting feature.

**Co-pathology:** 50–70% of DLB cases have concurrent Alzheimer co-pathology (amyloid-β plaques, tau neurofibrillary tangles), which accelerates cognitive decline and reduces response to cholinesterase inhibitors. DLB with high amyloid co-pathology may benefit from anti-amyloid antibody therapy (clinical trials ongoing).

### Neurotransmitter deficits

| Neurotransmitter | Deficit | Clinical consequence |
|:---|:---|:---|
| **Acetylcholine** | Most severe of all dementia types (80% cortical ChAT activity loss) | Cognitive fluctuations, hallucinations, memory impairment; responds to rivastigmine |
| **Dopamine** | SNpc degeneration → striatal dopamine loss | Parkinsonism (bradykinesia, rigidity, postural instability; tremor less common than PD) |
| **Norepinephrine** | Locus coeruleus degeneration | Orthostatic hypotension, REM sleep behavior disorder |
| **Serotonin** | Raphe nuclei involvement | Depression, sleep disturbance |

The profound **cholinergic deficit** in DLB — more severe than in Alzheimer's disease — explains both the cognitive fluctuations and visual hallucinations, and underlies the marked response to cholinesterase inhibitors (rivastigmine shows significant benefit in DLB, unlike the more modest effects in AD).

## Function

### Core diagnostic features (McKeith 2017 criteria) [^mckeith-2017-dlb-criteria]

**Four core clinical features (2+ required for probable DLB; 1 for possible DLB):**

1. **Fluctuating cognition**: Day-to-day or hour-to-hour oscillations in alertness and attention — "clouding" episodes lasting minutes to hours; lucid intervals followed by periods of confusion; ~80% of DLB patients; assessed by Clinician Assessment of Fluctuation (CAF) scale or Mayo Clinic Fluctuations Scale

2. **Recurrent well-formed visual hallucinations**: Typically detailed, complex, often of people or animals; present in ~70-80% of DLB patients; often non-threatening (patient may recognize them as "not real"); distinguish from Alzheimer's psychosis (which tends to be fragmented and paranoid)

3. **REM sleep behavior disorder (RBD)**: Loss of normal REM muscle atonia → patients physically act out dreams (shouting, punching, kicking); may predate dementia by years; >80% specificity for synucleinopathy; confirmed by polysomnography (PSG) with video monitoring

4. **Parkinsonism**: Bradykinesia, rigidity, and/or rest tremor; mild in most DLB (less prominent than idiopathic PD); responds partially to levodopa

**Supportive biomarkers:**
- **DAT-SPECT (DaTscan)**: Reduced dopamine transporter uptake in striatum (positive in ~80% DLB vs. ~10% AD); FDA-approved for distinguishing DLB from non-DLB dementias
- **MIBG cardiac scintigraphy**: Reduced cardiac sympathetic innervation (abnormal in ~70% DLB, ~10% AD); heart-to-mediastinum ratio <1.60 is highly specific
- **FDG-PET**: Occipital hypometabolism (visual cortex) — characteristic of DLB; distinguishes from AD (posterior parietal/temporal hypometabolism); "cingulate island sign" (preserved posterior cingulate vs. occipital loss)
- **Alpha-synuclein SAA (RT-QuIC)**: In CSF or skin biopsy; >90% sensitivity and specificity for DLB/PD; emerging as central diagnostic test
- **EEG**: Prominent slow waves, temporal sharp waves; may oscillate with fluctuating consciousness

### Clinical presentation — distinguishing DLB from Alzheimer's disease

| Feature | DLB | Alzheimer's Disease |
|:---|:---|:---|
| Memory at onset | Relatively preserved early | Prominent episodic memory loss (hippocampal) |
| Visuospatial | Severely impaired early | Impaired but less severe than DLB |
| Fluctuations | Prominent | Uncommon |
| Visual hallucinations | Spontaneous, complex, frequent | Less common; psychotic if present |
| Parkinsonism | Present in majority | Absent (late gait changes only) |
| Neuroleptic sensitivity | Fatal in ~50% | Not a major concern |
| RBD | Common | Uncommon |
| DAT-SPECT | Abnormal | Normal |
| FDG-PET | Occipital hypometabolism | Posterior parietal/temporal hypometabolism |

### Neuroleptic sensitivity — critical clinical warning

**DLB patients who receive typical or atypical antipsychotics** (especially haloperidol, risperidone, olanzapine) may develop **severe and potentially fatal neuroleptic sensitivity reactions** in ~50% of cases:
- Severe extrapyramidal rigidity, immobility
- Impaired consciousness, neuroleptic malignant syndrome-like picture
- Aspiration pneumonia, rapid functional decline
- Case fatality rate ~25-50% in affected patients

**Safe alternatives** for managing DLB psychosis:
- **Quetiapine** (relatively safe; weak D2 blockade)
- **Clozapine** (most effective; requires weekly CBC monitoring for agranulocytosis)
- **Pimavanserin** (5-HT2A inverse agonist; no dopamine blockade; FDA-approved for PD psychosis; trials in DLB ongoing)

## Pathology

### Neuropathological diagnosis

DLB diagnosis requires post-mortem demonstration of **neocortical alpha-synuclein Lewy bodies** by immunohistochemistry (anti-pSer129 SNCA antibody) in cingulate, parahippocampal, and frontal/temporal neocortex, combined with clinical features. The McKeith 2017 framework classifies neuropathological changes as:
- **High likelihood DLB**: Neocortical Lewy body pathology (with or without Alzheimer co-pathology)
- **Intermediate likelihood DLB**: Limbic Lewy body pathology
- **Low likelihood DLB**: Brainstem-predominant Lewy body pathology

Approximately 25-50% of clinically diagnosed DLB cases have significant AD co-pathology meeting neuropathological AD criteria — the "LBD-AD overlap" subtype.

### Treatment

**Cognitive symptoms:**
- **Rivastigmine (Exelon)** — the only FDA-approved treatment for PDD; also used off-label for DLB; inhibits both AChE and BChE; randomized trial (EXPRESS): 2.1-point MMSE improvement vs. placebo; cholinergic benefit reflects the profound ChAT deficit in DLB; side effects (nausea, vomiting) common with oral formulation → transdermal patch preferred
- **Donepezil** — evidence in DLB (open-label data); less RCT evidence than for AD or PDD
- **Memantine** — NMDA antagonist; modest benefit in open-label DLB studies; can worsen confusion in some patients

**Motor symptoms:**
- **Levodopa/carbidopa** — trial warranted for parkinsonism in DLB; response is less robust than in idiopathic PD (~50% respond); risk of worsening hallucinations and psychosis limits dose escalation; start low
- **Deep brain stimulation**: Limited evidence in DLB; generally avoided due to cognitive risk

**REM sleep behavior disorder:**
- **Clonazepam** (0.25–0.5 mg at bedtime): Reduces injurious dream enactment; first-line despite lack of large RCTs; not disease-modifying
- **Melatonin** (3–12 mg at bedtime): Safer than clonazepam; restores REM atonia; preferred in elderly

**Autonomic dysfunction:**
- Midodrine, droxidopa, fludrocortisone for neurogenic orthostatic hypotension
- Pyridostigmine for orthostatic hypotension (augments peripheral sympathetic tone)

**Disease-modifying therapies (investigational):**
- **Alpha-synuclein immunotherapy**: Prasinezumab (anti-SNCA mAb; Phase 2b in PD, signals in fast progressors); cinpanemab — negative Phase 2; ABBV-0805 (anti-aggregated synuclein) — Phase 2 ongoing
- **Alpha-synuclein SAA screening**: Pre-symptomatic identification of synucleinopathy enables future neuroprotective trials
- **GLP-1 agonists**: Semaglutide/liraglutide associated with lower PD risk in T2DM populations; neuroprotective mechanism investigation ongoing; Phase 2 trials in DLB planned

## Connections

- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — DLB and PD are both alpha-synuclein Lewy body diseases distinguished by the 1-year rule; SNCA pathology distribution differs — DLB has early cortical Lewy bodies while PD follows Braak staging from brainstem to cortex; motor symptoms are less prominent in DLB than idiopathic PD.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — 50-70% of DLB cases have concurrent Aβ plaques and tau tangles (AD co-pathology); both share APOE4 as a risk factor; distinguishing DLB from AD is critical due to fatal neuroleptic sensitivity; anti-amyloid antibodies may have emerging role in DLB with high amyloid burden.
- `connects-to` → **[SNCA](../../03-molecular/snca/README.md)** — cortical and limbic alpha-synuclein Lewy body pathology (SNCA S129-phosphorylated fibrils) defines DLB; alpha-synuclein SAA (RT-QuIC) in CSF or skin is >90% sensitive for DLB and emerging as the key antemortem biomarker; SNCA G51D mutation causes early-onset DLB-like syndrome.
- `connects-to` → **[MAPT](../../03-molecular/mapt/README.md)** — tau co-pathology present in 50-70% of DLB brains; MAPT H1 haplotype is a risk factor; alpha-synuclein and tau cross-seed each other; high tau burden in DLB predicts faster cognitive decline and worse prognosis.
- `targets` → **[Brain](../../06-organ/brain/README.md)** — DLB Lewy bodies accumulate in limbic cortex, parahippocampal gyrus, cingulate, and occipital cortex → visual hallucinations and cognitive fluctuations; SNpc degeneration causes parkinsonism; diffuse cholinergic denervation (80% ChAT activity loss) underlies cognitive impairment responsive to rivastigmine.
- `connects-to` → **[TDP-43](../../03-molecular/tdp-43/README.md)** — TDP-43 co-pathology in ~50% of DLB brains drives hippocampal atrophy and memory impairment independent of Lewy body burden; TDP-43 inclusions in hippocampal CA1 and entorhinal cortex accelerate cognitive decline; co-pathology predicts faster dementia progression in DLB.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Lewy body dementia carries the most severe cholinergic deficit — ~80% loss of cortical choline acetyltransferase, worse than Alzheimer's — driving fluctuating attention and visual hallucinations, and explaining why cholinesterase inhibitors help DLB more than AD.
- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — Treating the parkinsonism of Lewy body dementia with dopamine agonists can unleash impulse-control disorders (gambling, hypersexuality, compulsive shopping) by over-stimulating mesolimbic reward circuits; recognizing and dose-reducing is essential.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Lewy bodies are intraneuronal inclusions of misfolded alpha-synuclein; in DLB they fill cortical and limbic neurons, and selective loss of cholinergic, dopaminergic, and noradrenergic neurons produces the dementia, parkinsonism, and dysautonomia.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep disorder is a core, often first feature of Lewy body dementia: REM sleep behavior disorder—acting out dreams from loss of REM atonia—can precede dementia by years and strongly predicts a synucleinopathy; LBD also brings fragmented sleep and daytime somnolence.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Misfolded α-synuclein is a danger signal: it activates microglial NLRP3, driving IL-1β release and chronic neuroinflammation that amplifies neuronal loss — making NLRP3 a candidate target to slow Lewy body disease.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The immune brake is loosened in synucleinopathy: regulatory T cells normally restrain microglial reactivity to α-synuclein, and their declining number and function lets neuroinflammation run unchecked, accelerating degeneration.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pain is an under-recognized burden of Lewy body disease: α-synuclein degeneration of small autonomic and sensory fibres plus central pain-modulation deficits produce neuropathic and central pain alongside the parkinsonism.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression is common and often early in Lewy body dementia: degeneration of monoaminergic brainstem nuclei (serotonin, noradrenaline) plus cognitive and motor decline drive mood symptoms that can predate the dementia, complicating the distinction from late-life depression.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Neuroinflammation accompanies Lewy body dementia: microglia activated by misfolded α-synuclein release pro-inflammatory cytokines and reactive species that amplify neuronal injury and may spread pathology; PET shows microglial activation tracking disease, a therapeutic target.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — REM sleep behavior disorder bridges Lewy body dementia and narcolepsy: RBD—acting out dreams from lost REM muscle atonia—is an early marker that often precedes Lewy body dementia by years, while narcolepsy disrupts the same REM gating from orexin loss.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes participate in Lewy body dementia's α-synuclein pathology: reactive astrocytes accumulate α-synuclein and, with microglia, drive the neuroinflammation that accompanies the spreading synucleinopathy, so glial dysfunction contributes alongside neuronal loss.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine loss links Lewy body dementia to its parkinsonism: α-synuclein degeneration of nigrostriatal dopamine neurons produces the rigidity and bradykinesia, and a DaT scan showing reduced striatal dopamine transporter helps distinguish LBD from Alzheimer's disease.
- `connects-to` → **[Huntington Disease](../huntingtons-disease/README.md)** — Lewy body dementia and Huntington's are neurodegenerative movement-and-cognition disorders with distinct causes: LBD from α-synuclein (parkinsonism, hallucinations), Huntington's from a CAG repeat (chorea)—different proteins, overlapping decline.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Lewy body dementia is defined partly by psychosis that mimics schizophrenia: visual hallucinations and delusions are core features, but unlike schizophrenia they arise in older adults with parkinsonism, and antipsychotics can cause life-threatening sensitivity in LBD.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Lewy body dementia spares the hippocampus more than Alzheimer's early on: memory is relatively preserved while attention, visuospatial function and alertness fluctuate, reflecting cortical and brainstem Lewy pathology not hippocampal degeneration.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Lewy body dementia is a multisystem nervous-system synucleinopathy: alpha-synuclein deposits spread beyond cortex to autonomic and brainstem neurons, so beyond cognition it causes dysautonomia, REM sleep behavior disorder and parkinsonism—a whole-nervous-system disease.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Norepinephrine loss drives Lewy body dementia's autonomic and cognitive features: degeneration of the noradrenergic locus coeruleus contributes to orthostatic hypotension, attention fluctuations and arousal problems that distinguish LBD from Alzheimer's.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — REM sleep behavior disorder is a hallmark of Lewy body dementia: loss of normal REM atonia lets patients act out dreams, often years before dementia, and melatonin is a first-line treatment—making this sleep disturbance an early diagnostic clue.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Lewy body dementia is a failure of protein clearance: when autophagy can't degrade misfolded alpha-synuclein, it aggregates into the Lewy bodies that poison neurons, so boosting this cellular recycling system is a target shared with Parkinson's disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Lewy body dementia often starts in the gut: constipation and alpha-synuclein deposits in enteric nerves can precede cognitive and motor signs by years, echoing Parkinson's 'gut-first' route along the vagus nerve into the brain.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart helps diagnose Lewy body dementia: alpha-synuclein damages cardiac sympathetic nerves, so a MIBG scan shows reduced cardiac uptake—a marker that distinguishes Lewy body disease from Alzheimer's and other dementias.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Vivid visual hallucinations set Lewy body dementia apart: degeneration in visual-processing pathways makes well-formed hallucinations (often of people or animals) a core early feature, helping distinguish it from Alzheimer's at the bedside.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Lewy body dementia is treated partly by tuning glutamate: the NMDA-blocker memantine dampens excitotoxic glutamate signaling to modestly help cognition, complementing the cholinesterase inhibitors that target the disease's severe acetylcholine loss.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Brain iron accumulation feeds Lewy body disease: iron builds up in vulnerable neurons and catalyzes oxidative stress that promotes alpha-synuclein aggregation, linking a metal imbalance to the protein clumping at the disease's core.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Lewy body disease may begin in the gut: alpha-synuclein clumps appear in the intestinal nerves years before dementia, and constipation is a common early warning, supporting the idea that the pathology can climb the vagus nerve from gut to brain.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Lewy body dementia injures the brain's white matter: alpha-synuclein and degeneration affect oligodendrocytes and myelinated tracts, so disrupted connectivity between regions adds to the cholinergic loss behind the fluctuating cognition.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper binds alpha-synuclein directly: the protein has a copper-grabbing site, and disordered copper handling shifts synuclein toward the misfolded, aggregation-prone form, so a second metal beyond iron is tied to the Lewy body's core protein.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Lewy body dementia is a disease of failing synapses: alpha-synuclein normally works at the presynaptic terminal, and its misfolding cripples neurotransmitter release before cells die, so synaptic breakdown underlies the fluctuating cognition.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Lewy body dementia can be found in the skin: misfolded alpha-synuclein deposits in the tiny nerves of the skin, so a simple skin biopsy can now help confirm the synuclein disease behind the dementia.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Lewy body dementia starves neurons of ATP: like Parkinson's, it carries mitochondrial dysfunction that limits cellular energy, and the brain's demanding neurons falter as their power supply fails.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging helps pin down Lewy body dementia: a DaTscan's photons show the dopamine loss, and cardiac MIBG scintigraphy reveals the sympathetic denervation that helps separate it from Alzheimer's.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Lewy body dementia attacks the autonomic nerves: synuclein in the peripheral autonomic system causes orthostatic hypotension, constipation and bladder trouble, often years before the dementia appears.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Aspiration pneumonia is the common end of Lewy body dementia: as swallowing fails late in the disease, inhaled food infects the lungs, the frequent immediate cause of death.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals the disease's namesake: Lewy bodies, dense spherical cores of aggregated alpha-synuclein filaments, fill neurons across the cortex — the same protein clumps as Parkinson's, but spread widely enough to steal cognition.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium handling fails in the dying neurons: misfolded alpha-synuclein disrupts the cell's calcium balance and the mitochondria that buffer it, an energy-and-calcium crisis that helps drive the widespread neuronal death.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Lewy body disease wrecks the autonomic system: synuclein deposits damage the sympathetic nerves that command the adrenal-driven blood-pressure response, so fainting orthostatic hypotension is a prominent, early feature.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Lewy body disease unsettles sleep and wakefulness: synuclein damage to orexin-related arousal systems brings excessive daytime sleepiness and the dream-enacting REM sleep behavior disorder that often heralds it years early.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Autonomic failure stalls the body's smooth muscle: beyond fainting blood pressure, Lewy body disease slows gut and bladder smooth muscle into constipation and urinary trouble — non-motor features that often precede the dementia.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Treatment may one day come as antibody, and mimics must be excluded: anti-α-synuclein antibodies are being trialed to clear the aggregates, while autoimmune (antibody-mediated) encephalitis is a treatable mimic ruled out in rapidly progressive cases.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The heart helps make the diagnosis: Lewy body disease degenerates the cardiac sympathetic nerves supplying the cardiomyocytes, so reduced MIBG uptake on a cardiac scan is a distinctive marker separating it from Alzheimer's.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The gut shows it early: Lewy pathology in the enteric nerves slows the stomach into gastroparesis and early satiety years before dementia, and α-synuclein found on gut biopsy may become an early clue.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The disease may begin in the gut: under the gut-first hypothesis, misfolded α-synuclein arises in the enteric nervous system and climbs the vagus to the brain, with gut dysbiosis a suspected early player.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — The immune system reads α-synuclein as foreign: cytotoxic T cells recognizing synuclein peptides are found in synucleinopathies and may help kill the neurons, adding an autoimmune arm to Lewy body disease.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Lewy pathology dims more than dopamine: degeneration of the serotonergic raphe lowers serotonin, contributing to the depression, anxiety, and REM-sleep disturbance that often shadow the cognitive decline.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Synucleinopathies and melanoma travel together: as in Parkinson's, Lewy body disease carries a higher melanoma risk, a bidirectional link rooted in shared pigment and α-synuclein biology.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Microglia inflame the synuclein-laden brain: α-synuclein activates NF-κB in microglia, driving the cytokine output and NLRP3 priming that accelerate the neuronal loss of Lewy body disease.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Falls meet fragile bones: the parkinsonism, orthostatic hypotension and cognitive lapses of Lewy body dementia cause frequent falls, while immobility and low vitamin D thin the bones — a combination that makes fractures common.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Swallowing fails late in the disease: advancing Lewy body dementia brings dysphagia and aspiration, so aspiration pneumonia and the sepsis it triggers are a frequent terminal event.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its autonomic failure reaches the heart: Lewy body disease causes cardiac sympathetic denervation and severe orthostatic hypotension, and the dysautonomia complicates and overlaps with heart failure in these frail patients.
- `connects-to` → **[Stroke](../stroke/README.md)** — Vascular injury muddies the picture: cerebrovascular disease frequently coexists with Lewy body pathology, and stroke can add to or be mistaken for its fluctuating cognition in a mixed dementia.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety rides the cognitive fluctuations: marked anxiety is common in Lewy body dementia, worsened by the disease's fluctuating attention, visual hallucinations and autonomic instability.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Swallowing fails as the disease advances: dysphagia in Lewy body dementia causes aspiration, and the resulting pneumonia — often pneumococcal — is a leading immediate cause of death.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — Infection unmasks the fluctuating brain: a urinary tract infection, commonly E. coli, can abruptly worsen the cognition and hallucinations of Lewy body dementia, triggering florid delirium beyond its usual fluctuations.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Late immobility breaks down the skin: as Lewy body dementia advances to a bedbound state, pressure ulcers form over bony prominences and heal poorly in the frail, malnourished patient.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Autonomic failure drops the blood pressure: Lewy body dementia disrupts cardiovascular autonomic control, causing orthostatic hypotension and syncope that lead to falls, a hallmark of its dysautonomia.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Parkinsonism and falls batter the skeleton: the rigidity, bradykinesia and postural instability of Lewy body dementia cause frequent falls with fractures, and late immobility brings contractures and sarcopenia.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Autonomic dysfunction unsettles the bladder: Lewy body dementia impairs autonomic bladder control, causing urinary urgency, incontinence and retention with recurrent infection.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Swallowing failure floods the lungs: dysphagia in Lewy body dementia causes aspiration pneumonia, a leading cause of death, while REM sleep behaviour disorder disrupts breathing and sleep.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Misfolded protein stirs brain inflammation: alpha-synuclein aggregation provokes microglial neuroinflammation, an immune response implicated in the progression of Lewy body dementia.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Immobility and drug sensitivity reach the skin: it brings pressure sores and seborrhoeic skin changes, while its severe neuroleptic sensitivity can trigger rigidity and neuroleptic malignant syndrome.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Like other dementias it may fail to clear its waste protein: impaired glymphatic drainage during sleep is implicated in the build-up of alpha-synuclein that defines Lewy body disease.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Early autonomic failure reaches the pelvis: erectile dysfunction and urinary disturbance often precede the cognitive decline of Lewy body dementia by years.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — Mood symptoms are common but drugs need care: SSRIs like fluoxetine treat the frequent depression, while antipsychotics must be used with great caution given the severe neuroleptic sensitivity of Lewy body dementia.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Autonomic and circadian control fails: Lewy pathology in the hypothalamus and autonomic ganglia disrupts blood-pressure regulation, temperature and circadian rhythm, producing the orthostatic hypotension and sleep-wake disturbance of DLB.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Seizures complicate the failing brain: like other neurodegenerative dementias, Lewy body dementia carries a raised risk of seizures and myoclonus as cortical networks degenerate.
- `connects-to` → **[ALS](../als/README.md)** — A shared misfolded protein: TDP-43 co-pathology is found in a large minority of Lewy body dementia brains, linking it to the TDP-43 proteinopathy that defines amyotrophic lateral sclerosis.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It denervates the heart: like Parkinson's, Lewy body dementia causes cardiac sympathetic denervation, so reduced MIBG uptake in the myocardium helps distinguish it from Alzheimer's and contributes to orthostatic hypotension.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — α-synuclein clogs the axon: Lewy bodies are aggregates of α-synuclein that impair axonal transport in neurons, contributing to the synaptic failure and degeneration that drive its fluctuating cognition and hallucinations.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — It may begin in the gut: α-synuclein pathology is found in the enteric nerves of the gut wall years before dementia, supporting a body-first route where the protein ascends the vagus to the brain (the Braak hypothesis).
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — The synucleinopathy autonomic clue: LBD damages cardiac sympathetic nerves and autonomic control, causing orthostatic hypotension and heart-rate dysregulation—cardiac sympathetic denervation is a diagnostic marker.
- `connects-to` → **[LRRK2](../../03-molecular/lrrk2/README.md)** — Shared genetics with Parkinson's: LRRK2 mutations cause familial parkinsonism and contribute to Lewy-body pathology, tying the genetics of synucleinopathy across Parkinson's disease and dementia with Lewy bodies.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Inflammation that prunes synapses: activated microglia and complement C3 tag and eliminate synapses in Lewy-body dementia, a mechanism of the synaptic loss that drives the cognitive decline.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Infection unmasks fragility: COVID-19 commonly precipitates delirium and accelerates cognitive decline in Lewy-body dementia, whose patients are acutely vulnerable to any systemic insult.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Metabolism and the ageing brain: type 2 diabetes and insulin resistance raise the risk and pace of dementias including Lewy-body disease, through vascular injury and impaired neuronal glucose handling.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Falls and fractures: the parkinsonism, orthostatic hypotension and cognitive fluctuations of Lewy-body dementia cause frequent falls, fracturing the cortical bone of already osteoporotic elderly patients.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Aspiration ends it: dysphagia in advanced Lewy-body dementia leads to aspiration pneumonia, seeding the alveoli with oral flora—the leading cause of death as in other neurodegenerative diseases.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Anxiety as a prodrome: prominent anxiety and panic are common non-motor and prodromal features of Lewy-body dementia, often preceding the cognitive and motor signs by years.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Late-life mood instability: new-onset mood disturbance in older adults can herald an emerging synucleinopathy like Lewy-body dementia, blurring the line between primary mood disorder and neurodegeneration.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Neuroinflammation: IL-1β from microglia activated around α-synuclein aggregates amplifies the inflammatory cascade that drives neuronal loss in Lewy-body dementia.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory neurodegeneration: elevated TNF-α reflects the chronic microglial activation accompanying the synucleinopathy of Lewy-body dementia, contributing to progressive neuronal injury.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Cortical inhibition: loss of GABAergic interneurons contributes to the fluctuating attention, visual hallucinations and cognitive instability characteristic of Lewy-body dementia.
- `connects-to` → **[ApoE](../../03-molecular/apoe/README.md)** — Shared genetic risk: the APOE4 allele raises risk not only for Alzheimer's but also for Lewy-body dementia, linking lipid handling and amyloid co-pathology to the synucleinopathy.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Microglial recruitment: CCL2 released in the synuclein-burdened brain draws monocytes and amplifies the microglial neuroinflammation that accelerates neurodegeneration in Lewy-body dementia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA-sensing inflammation: mitochondrial DNA leaked from stressed neurons activates cGAS-STING in microglia, an emerging driver of the neuroinflammatory response to α-synuclein pathology.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Aggregated α-synuclein released from dying neurons activates microglial TLR4, propagating the chronic neuroinflammation that helps spread Lewy pathology through the cortex in Lewy-body dementia.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Dysregulated ferroportin-controlled iron handling lets iron accumulate in vulnerable neurons of Lewy-body dementia, sensitizing them to the oxidative and ferroptotic death that accompanies synuclein pathology.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3 executes the apoptotic death of cortical and brainstem neurons in Lewy-body dementia, the cell-loss endpoint of α-synuclein toxicity, mitochondrial failure, and chronic neuroinflammation.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — α-Synuclein aggregates form membrane pores and disrupt calcium handling, and the resulting calcium overload stresses mitochondria—a mechanism of neuronal vulnerability shared with the substantia-nigra neurons lost in Parkinson's.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by microglia activated around Lewy pathology amplifies the neuroinflammatory response, a microglial signal increasingly implicated as a driver of α-synucleinopathy neurodegeneration.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Declining BDNF removes neurotrophic support for the cortical and brainstem neurons targeted in Lewy-body dementia, contributing to the synaptic loss behind the fluctuating cognition and visual hallucinations.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Oxidative stress drives the α-synuclein aggregation and neurodegeneration of Lewy-body dementia, and a declining NRF2 antioxidant response permits this damage, as in the related Parkinson's disease.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR restrains the autophagy (already mapped) that clears α-synuclein, and its dysregulation impairs the lysosomal clearance whose failure allows Lewy bodies to accumulate.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 from the activated microglia (already mapped) contributes to the neuroinflammation, with IL-1β and TNF-α, that accelerates the neurodegeneration of Lewy-body dementia.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Aggregated α-synuclein (SNCA already mapped) engages microglial TLRs that signal through MyD88 to NF-κB, sustaining the chronic innate-immune activation that drives Lewy-body neurodegeneration.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β phosphorylates tau (MAPT already mapped) and modulates α-synuclein toxicity, mechanistically linking the combined tau and synuclein pathology characteristic of Lewy body dementia.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor (NTRK) supports neuronal survival, and the loss of this trophic support accelerates the cholinergic and cortical degeneration of Lewy body dementia.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling (GSK-3β and mTOR mapped) maintains neuronal survival and regulates α-synuclein-related autophagy, its decline contributing to neurodegeneration in Lewy body dementia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine-driven JAK-STAT signaling sustains the microglial and astrocytic neuroinflammation accompanying α-synuclein pathology in Lewy body dementia.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3-driven reactive astrogliosis is part of the neuroinflammatory response to Lewy pathology in Lewy body dementia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling drives the interferon-responsive microglial activation contributing to the neuroinflammation of Lewy body dementia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling transduces the cytokine and growth-factor stimuli that modulate neuronal stress and glial activation in Lewy body dementia.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN regulation of PI3K-AKT survival signaling (AKT already mapped) shapes the autophagy and neuronal vulnerability relevant to α-synuclein clearance in Lewy body dementia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the neuronal autophagy and oxidative-stress defense whose failure permits α-synuclein accumulation in Lewy body dementia.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation of Lewy body dementia.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and mitochondrial stress responses contribute to the neurodegeneration of Lewy body dementia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, coupled to autophagy (autophagy already mapped), regulates the clearance of α-synuclein aggregates in Lewy body dementia.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the neuronal survival pathways whose failure contributes to Lewy body dementia.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic CD8 T cells infiltrate the brain and contribute to the neurodegeneration of Lewy body dementia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (FYN) kinase signaling participates in the α-synuclein-linked synaptotoxicity and neuroinflammation of Lewy body dementia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation (including SNCA regulation) implicated in Lewy body dementia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven microglial and monocyte recruitment contributes to the neuroinflammation of Lewy body dementia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the microglial and neuroinflammatory responses of Lewy body dementia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and neuroinflammatory responses of Lewy body dementia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation of Lewy body dementia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neuronal gene programs of Lewy body dementia.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (A2A receptor) signaling participates in the synaptic dysfunction and neuroinflammation of Lewy body dementia.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microglial activation and neuroinflammation of Lewy body dementia.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Urate and oxidative stress: low serum urate, a product of xanthine oxidase with antioxidant properties, is associated with increased risk and faster progression of synucleinopathies, implicating oxidative stress in Lewy body dementia.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences: Lewy body dementia is more common in men, and estrogen's neuroprotective effects on dopaminergic and cholinergic neurons (acetylcholine already mapped) are proposed to contribute to the sex difference in risk.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Brain insulin resistance: impaired cerebral insulin signalling is common across the dementias, including Lewy body dementia, where it worsens neuronal energetics and may accelerate the alpha-synuclein neurodegeneration.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Adaptive autoimmunity: alpha-synuclein-specific T cells expanded through IL-2 signalling are found in the synucleinopathies, implicating an adaptive immune response against the aggregating protein (already mapped) in the neurodegeneration of Lewy body dementia.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Neurosteroid protection: progesterone-derived neurosteroids are neuroprotective and support cholinergic (already mapped) neurons, and together with estrogen (already mapped) may contribute to the sex differences in Lewy body dementia.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Microglial polarisation: IL-4 shifts microglia (already mapped) toward a reparative, anti-inflammatory phenotype, and enhancing this arm against the pro-inflammatory TNF/IL-1 response is a neuroprotective strategy of interest in Lewy body dementia.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the activated microglia (already mapped) contribute to the neuroinflammation that drives the alpha-synuclein pathology (already mapped) and neuronal loss of Lewy body dementia.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — APOE lipid handling: cholesterol metabolism, governed by APOE (already mapped), influences alpha-synuclein aggregation and membrane biology, part of the lipid dimension of the neurodegeneration in Lewy body dementia.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory neuroprotection: IL-10, with IL-4 (already mapped), opposes the microglial pro-inflammatory response (TNF, IL-1 and IL-6 already mapped) driving neuronal loss, and boosting this arm is a neuroprotective strategy of interest in Lewy body dementia.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and synuclein: zinc, with the copper and iron (already mapped), binds alpha-synuclein (already mapped) and modulates its aggregation and the oxidative stress, part of the metal dyshomeostasis of the neurodegeneration in Lewy body dementia.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium neuroprotection: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity on the vulnerable neurons, a proposed neuroprotective factor in Lewy body dementia.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Omega-3 and brain lipids: the omega-3 fatty acid DHA is a major brain membrane lipid (cholesterol and APOE already mapped), and its pro-resolving mediators counter the neuroinflammation of Lewy body dementia, of dietary interest for neuroprotection.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation (NLRP3, TNF and IL-1 already mapped) of Lewy body dementia.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic neuroprotection: leptin has neurotrophic and neuroprotective actions on the neurons (already mapped), and the metabolic dysregulation (insulin already mapped) it reflects is linked to the neurodegeneration of Lewy body dementia.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Brain-iron regulation: hepcidin governs the iron (already mapped) handling whose dysregulation contributes to the brain-iron accumulation (ferroportin already mapped) and the metal-catalysed oxidative injury of Lewy body dementia.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Neuroinflammation: the microglial activation and the neuroinflammation (TNF, IL-1 and NLRP3 already mapped) drive the α-synuclein (already mapped) neurodegeneration of Lewy body dementia.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Neuronal loss: the cortical and the cholinergic/dopaminergic (acetylcholine and dopamine already mapped) neurons, laden with the Lewy bodies (α-synuclein already mapped), degenerate in Lewy body dementia.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Brain-iron oxidative injury: the iron accumulates in the degenerating brain (ferroportin and hepcidin already mapped) and catalyses the oxidative injury and the α-synuclein aggregation of Lewy body dementia.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the mitochondrial DNA, drives the microglial (already mapped) neuroinflammation of Lewy body dementia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu of Lewy body dementia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the neuroinflammation (IL-6 and TNF already mapped) of Lewy body dementia.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the adaptive-immune contribution to the α-synuclein (already mapped) neuroinflammation of Lewy body dementia.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the neuroinflammation of Lewy body dementia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune interaction in Lewy body dementia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) activation and the complement-mediated synapse loss of Lewy body dementia.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the complement-driven neuroinflammation of Lewy body dementia.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Brain iron: transferrin, the iron carrier, is central to the brain-iron dysregulation (ferroportin already mapped) that drives the oxidative stress and ferroptosis of the α-synucleinopathy of Lewy body dementia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-mediated synapse loss of Lewy body dementia.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway (C1q-initiated) implicated in the synaptic pruning of the α-synucleinopathy of Lewy body dementia.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments present the alpha-synuclein (already mapped) antigen to the T cells (already mapped) in the neuroinflammation of Lewy body dementia.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-neuroinflammatory axis: TSLP, from gut-epithelium (gut-microbiome already mapped) under the autonomic dysfunction and dysbiosis of Lewy body dementia, primes dendritic cells (already mapped) and mast cells (already mapped) and amplifies the gut-brain neuroinflammation.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-neuroinflammatory axis: bradykinin, via B2R on CNS microglia (already mapped) and neurons (already mapped), amplifies the BBB permeability and the neuroinflammation contributing to the α-synuclein (already mapped) propagation of Lewy body dementia.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective EPO: erythropoietin, via EpoR on neurons (already mapped) and oligodendrocytes (already mapped), exerts neuroprotective and anti-apoptotic effects relevant to the dopaminergic (dopamine already mapped) and non-dopaminergic neurodegeneration of Lewy body dementia.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histaminergic sleep-wake: histamine, from the tuberomammillary nucleus (already mapped as hypothalamus-linked brain circuit), is a principal wake-promoting transmitter; the severe REM-sleep-behaviour disorder of Lewy body dementia disrupts the histaminergic arousal circuit.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — CNS-border ECM: periostin, from astrocytes (already mapped) and meningeal fibroblasts, contributes to the perivascular ECM remodelling and the neuroinflammation (IL-1b, TNF already mapped) of the Lewy body dementia brain.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Neuroprotective androgen: testosterone and its metabolite DHT exert neuroprotective effects on dopaminergic neurons (already mapped); falling testosterone in ageing is associated with greater α-synuclein (already mapped) pathology and Lewy body dementia risk.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Neuroinflammatory neuroendocrine: prolactin, via PRLR on neurons (already mapped) and microglia (already mapped), modulates neuroinflammation; prolactin deficiency amplifies the dopamine (already mapped) dysregulation and the melatonin (already mapped) sleep-wake disruption of Lewy body dementia.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Anti-neuroinflammatory: oxytocin, via OXTR on neurons (already mapped) and microglia (already mapped), reduces neuroinflammation and α-synuclein (already mapped) spread; oxytocin attenuates the norepinephrine (already mapped) and IL-6 (already mapped) hyperarousal of Lewy body dementia.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — CSF osmolality modulator: vasopressin, via V1aR on neurons (already mapped) and microglia (already mapped), modulates CSF osmolality; vasopressin dysregulation amplifies norepinephrine (already mapped) and NLRP3 (already mapped) neuroinflammation of Lewy body dementia.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — LBD selenium: selenium, via GPx and NRF2 (already mapped) antioxidants, protects neurons (already mapped) from ROS and α-synuclein (already mapped) aggregation-driven injury; selenium deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) neuroinflammation of LBD.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — LBD iodine: iodine-dependent thyroid hormones regulate neuronal (neuron already mapped) metabolism and dopamine (already mapped) synthesis; hypothyroidism amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and α-synuclein (already mapped) burden in LBD.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — LBD sodium: sodium, via voltage-gated channels on neurons (already mapped), regulates action-potential firing; dysregulated sodium from microglial (already mapped) NLRP3 (already mapped) neuroinflammation amplifies NF-κB (already mapped) and dopamine (already mapped) in LBD.

[^mckeith-2017-dlb-criteria]: McKeith IG, Boeve BF, Dickson DW, et al. Diagnosis and management of dementia with Lewy bodies: Fourth consensus report of the DLB Consortium. *Neurology.* 2017;89(1):88-100. [doi:10.1212/WNL.0000000000004058](https://doi.org/10.1212/WNL.0000000000004058) · [PubMed 28592453](https://pubmed.ncbi.nlm.nih.gov/28592453/)
[^spillantini-1997-lewy-body]: Spillantini MG, Schmidt ML, Lee VM, Trojanowski JQ, Jakes R, Goedert M. Alpha-synuclein in Lewy bodies. *Nature.* 1997;388(6645):839-840. [doi:10.1038/42166](https://doi.org/10.1038/42166) · [PubMed 9278044](https://pubmed.ncbi.nlm.nih.gov/9278044/)
[^walker-2015-dlb-review]: Walker Z, Possin KL, Boeve BF, Aarsland D. Lewy body dementias. *Lancet.* 2015;386(10004):1683-1697. [doi:10.1016/S0140-6736(15)00462-6](https://doi.org/10.1016/S0140-6736(15)00462-6) · [PubMed 26595642](https://pubmed.ncbi.nlm.nih.gov/26595642/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
