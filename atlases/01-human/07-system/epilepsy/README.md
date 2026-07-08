---
schema: human-scale-entry/v1
id: epilepsy
name: Epilepsy
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Epilepsy (recurrent unprovoked seizures; 50M affected) comprises focal and generalized types; causes: structural, genetic (SCN1A-Dravet, KCNQ2, TSC1/2), autoimmune (anti-NMDAR), metabolic; valproate and levetiracetam are first-line; surgery and VNS for drug-refractory disease."
aliases: ["epilepsy", "seizure disorder", "Dravet syndrome", "temporal lobe epilepsy", "MTLE", "absence epilepsy", "childhood absence", "juvenile myoclonic epilepsy", "JME", "status epilepticus", "GEFS+", "West syndrome", "Lennox-Gastaut syndrome", "focal epilepsy", "generalized epilepsy"]
sources:
  - id: fisher-2017-ilae-classification
    type: peer-reviewed
    cite: "Fisher RS, Cross JH, D'Souza C, et al. Instruction manual for the ILAE 2017 operational classification of seizure types. Epilepsia. 2017;58(4):531-542."
    doi: "10.1111/epi.13671"
    pmid: "28276060"
    url: "https://doi.org/10.1111/epi.13671"
    accessed: "2026-06-08"
  - id: devinsky-2018-epilepsy-review
    type: peer-reviewed
    cite: "Devinsky O, Vezzani A, O'Brien TJ, et al. Epilepsy. Nat Rev Dis Primers. 2018;4:18024."
    doi: "10.1038/nrdp.2018.24"
    pmid: "29722352"
    url: "https://doi.org/10.1038/nrdp.2018.24"
    accessed: "2026-06-08"
  - id: engel-2012-mtle-surgery
    type: peer-reviewed
    cite: "Engel J Jr, McDermott MP, Wiebe S, et al. Early surgical therapy for drug-resistant temporal lobe epilepsy: a randomized trial. JAMA. 2012;307(9):922-930."
    doi: "10.1001/jama.2012.220"
    pmid: "22396514"
    url: "https://doi.org/10.1001/jama.2012.220"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/scn1a
    relation: connects-to
    note: "SCN1A encodes Nav1.1; de novo LOF mutations cause Dravet syndrome (SMEI) — the most severe genetic epilepsy; gain-of-function → GEFS+; Nav1.1 haploinsufficiency in GABAergic interneurons → cortical disinhibition → seizures; sodium channel blockers worsen Dravet."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "GABAergic interneurons maintain cortical inhibitory balance — the fundamental seizure brake; GABA-A receptor potentiators (benzodiazepines, phenobarbital, clobazam) and GABA-T inhibitors (valproate, vigabatrin) are the most widely used antiepileptic drugs."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR pathway gain-of-function mutations cause structural epilepsies: TSC1/TSC2 → tuberous sclerosis (seizures in 80-90% of patients); somatic PIK3CA/MTOR mutations → focal cortical dysplasia type IIb (FCDII); mTOR inhibitor everolimus reduces TSC-associated seizures by ~50%."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Epilepsy arises from focal or generalized cortical networks; MTLE involves hippocampal sclerosis; absence seizures arise from 3 Hz cortical-thalamic spike-wave; brainstem involvement explains autonomic seizure features and SUDEP; epilepsy surgery targets the epileptogenic zone."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Epilepsy risk is 2-3× elevated in AD; amyloid-driven cortical hyperexcitability precedes clinical dementia; anti-NMDAR and LGI1 autoimmune encephalitides cause encephalitis with new-onset epilepsy mimicking rapid-onset dementia; LGI1 faciobrachial seizures are pathognomonic."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Allopregnanolone (progesterone metabolite) is a potent GABA-A PAM via delta subunit extrasynaptic receptors → sedation, anxiolysis, anticonvulsant; progesterone withdrawal → allopregnanolone decline → GABA-A downregulation → seizure threshold reduction in catamenial epilepsy."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Epilepsy and migraine are comorbid disorders of cortical hyperexcitability that share genetics: gain-of-function SCN1A causes familial hemiplegic migraine while loss-of-function causes Dravet epilepsy, and valproate and topiramate treat both."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Seizures are an excitation-inhibition imbalance, and glutamate is the excitatory side: AMPA/NMDA over-activity drives synchronous bursting, and the AMPA antagonist perampanel is an antiseizure drug — the counterpart to GABA's brake."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "A seizure is hypersynchronous neuronal firing: bursting pyramidal neurons and recurrent excitatory collaterals overwhelm GABAergic interneurons → a paroxysmal depolarizing shift; most genetic epilepsies are neuronal ion-channelopathies that tip this balance."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Tuberous sclerosis is a paradigmatic genetic epilepsy: cortical tubers and TSC1/TSC2-driven mTOR overactivation cause early, often drug-resistant seizures (including infantile spasms), so mTOR inhibitors (everolimus) reduce seizures and early EEG-guided treatment is studied."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Stroke is a leading cause of acquired epilepsy in older adults: cortical infarcts and hemorrhages leave a gliotic, hyperexcitable scar that generates late-onset focal seizures months to years later; post-stroke epilepsy worsens outcomes and is managed with antiseizure medication."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes are active players in epilepsy, not bystanders: reactive astrogliosis impairs glutamate and potassium buffering and disrupts the blood-brain barrier, lowering seizure threshold; aberrant gap-junction coupling and inflammation sustain epileptogenesis."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Epilepsy and autism frequently co-occur and share biology: up to a third of autistic people have epilepsy, and both arise from disrupted excitation/inhibition balance and overlap in genes like SCN, TSC, and SHANK—often the same neurodevelopmental lesion."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Seizures are the commonest first sign of an IDH-mutant glioma: these slow-growing cortical tumors irritate neurons (partly via the oncometabolite 2-hydroxyglutarate altering glutamate), so new focal epilepsy in a young adult should prompt imaging for a low-grade glioma."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Epilepsy and depression have a bidirectional relationship: depression is the commonest psychiatric comorbidity of epilepsy and also raises the risk of developing it, shared limbic and serotonergic mechanisms link them, and depression strongly degrades quality of life."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "Brain tumors are an important cause of epilepsy: glioblastoma and other gliomas irritate surrounding cortex, so new-onset seizures in an adult mandate brain imaging—seizures are often the presenting sign of a glioma, and tumor-related epilepsy can be hard to control."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus is the seat of the commonest focal epilepsy: mesial temporal sclerosis—hippocampal scarring and neuron loss—generates temporal-lobe seizures, and surgically removing the sclerotic hippocampus can cure drug-resistant cases."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Epilepsy and schizophrenia are bidirectionally linked: temporal-lobe epilepsy can produce a schizophrenia-like psychosis, each roughly doubles the risk of the other, and they share disturbances of glutamate and GABA—so a first psychotic episode sometimes warrants EEG."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Voltage-gated sodium channels are epilepsy's central target: sodium influx fires the action potentials that, when runaway, become seizures, so many first-line drugs (phenytoin, lamotrigine) work by blocking these channels—and SCN1A mutations cause epilepsy."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Epilepsy is fundamentally a disorder of the synapse: seizures arise when synaptic excitation (glutamate) overwhelms inhibition (GABA), so the tipped excitation-inhibition balance at synapses is the common final pathway across epilepsy's many causes."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Epilepsy is a disorder of the whole nervous system's electrical stability: hypersynchronous neuronal discharges can start focally or generalize across networks, so seizures are a shared symptom of countless insults—from genetics to stroke, tumor and infection."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium channels set the brain's seizure threshold: by repolarizing neurons and damping excitability, Kv7/KCNQ channels guard against runaway firing, so their mutations cause familial epilepsies—and openers that boost potassium currents are an anticonvulsant strategy."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The endocannabinoid system tempers seizures: cannabinoid signaling dampens excitatory transmission, and purified cannabidiol is now approved for severe childhood epilepsies like Dravet and Lennox-Gastaut—turning a cannabis compound into a proven anticonvulsant."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome helps the ketogenic diet fight epilepsy: this high-fat diet controls drug-resistant seizures partly by reshaping gut bacteria and their metabolites, so the gut-brain axis is part of how a dietary therapy calms the epileptic brain."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium channels generate the rhythm of absence seizures: thalamic T-type calcium currents drive the 3-Hz spike-wave discharges of absence epilepsy, which is why the T-type blocker ethosuximide specifically treats them—not the sodium-channel drugs used elsewhere."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Epilepsy is fueled by microglial neuroinflammation: seizures activate microglia that release cytokines lowering seizure threshold, creating a feed-forward loop of epileptogenesis—so inflammation is both a consequence and a driver of recurrent seizures."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Epilepsy's deadliest complication strikes the heart: in SUDEP (sudden unexpected death in epilepsy), a seizure triggers fatal cardiac arrhythmia or asystole and respiratory arrest, making seizure control a matter of preventing sudden death, not just fits."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF helps rewire the brain into an epileptic one: after injury or seizures, surging BDNF promotes the abnormal sprouting and excitability that turn normal circuits epileptogenic, so it is studied as a driver of how epilepsy develops."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine is the brain's built-in seizure brake: it accumulates during intense firing and damps neurons, ending seizures, and the ketogenic diet's anticonvulsant effect works partly by boosting this adenosine tone."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Epilepsy involves the brain's myelin too: oligodendrocyte and white-matter abnormalities accompany many epilepsies, and seizures in turn disrupt myelination, linking impaired connectivity to the seizure-prone network."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Light itself can trigger seizures: in photosensitive epilepsy, flashing lights and certain patterns drive abnormal synchronous firing through the visual system, so the photons hitting the retina set off a seizure—why strobe effects carry warnings."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Epilepsy treatment runs through the liver: most antiseizure drugs are metabolized there, inducing or inhibiting enzymes that cause drug interactions, and some (like valproate) can injure the liver, so liver function shapes the choice of medication."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "GABA calms the brain by moving chloride: opening chloride channels normally quiets neurons, but when the chloride gradient is immature or disrupted GABA can instead excite them, a switch that underlies hard-to-treat neonatal seizures."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium calms overexcited neurons: intravenous magnesium is the treatment for eclamptic seizures, and a low magnesium level can itself lower the seizure threshold, tying the mineral to seizure control."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Diet and the gut shape epilepsy: the ketogenic diet controls many drug-resistant seizures, and the gut microbiome it reshapes appears to mediate part of that protection through the gut-brain axis."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "When drugs fail, epilepsy is treated through a nerve: vagus nerve stimulation sends regular pulses along this peripheral nerve to the brain, reducing seizure frequency in refractory cases."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the scarred epileptic focus: in mesial temporal sclerosis the hippocampus loses neurons and gliosis takes over, while surviving granule cells sprout aberrant mossy fibers that wire the runaway circuits of seizures."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Long-term seizure drugs quietly weaken bone: enzyme-inducing antiepileptics speed the liver's breakdown of vitamin D, so deficiency, osteomalacia, and fractures are a recognized hazard of years on treatment."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "A prolonged seizure can poison the kidney: violent muscle activity in status epilepticus breaks down muscle, and the released myoglobin clogs the renal tubules, threatening acute kidney injury."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Anti-seizure drugs can erupt on the skin: carbamazepine, lamotrigine, and phenytoin can trigger Stevens-Johnson syndrome and toxic epidermal necrolysis, a risk so tied to the HLA-B*1502 allele that some patients are genotyped first."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Epilepsy and its drugs reach into reproduction: valproate is strongly teratogenic, enzyme-inducing drugs undercut hormonal contraception, and many women have catamenial seizures that cluster with the menstrual cycle's hormone swings."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Some anti-seizure drugs strike the marrow: carbamazepine can cause agranulocytosis and aplastic anemia, while phenytoin interferes with folate to produce a megaloblastic anemia — so blood counts are monitored."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Some seizures are autoimmune: antibodies against NMDA-receptor or LGI1 cause an encephalitis whose seizures resist standard drugs but respond to immunotherapy, a treatable cause now sought in new-onset, unexplained epilepsy."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Long-term seizure drugs thin the bones: enzyme-inducing anti-seizure medicines speed vitamin D breakdown, lowering calcium and driving the osteomalacia and osteoporosis that leave epilepsy patients prone to fractures."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Valproate quietly drops the platelets: the widely used anti-seizure drug causes a dose-related thrombocytopenia and platelet dysfunction, watched especially before surgery or when bleeding appears."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "A slow-growing tumor can announce itself as a seizure: a meningioma pressing on the cortex irritates the neurons beneath it, so a new seizure in an adult prompts brain imaging to find such a structural cause."
  - target: 01-human/07-system/west-nile-virus
    relation: connects-to
    note: "Brain infection sparks seizures: West Nile and other encephalitides inflame the cortex into acute seizures, and the scar they leave can become a focus for later epilepsy."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation lowers the seizure threshold: seizures trigger a surge of IL-6 and other cytokines, and this neuroinflammation in turn makes neurons more excitable, a feed-forward loop now seen as part of epileptogenesis."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "An inflammasome fuels the feed-forward loop: NLRP3 activation in microglia releases IL-1β that heightens neuronal excitability, a driver of epileptogenesis being targeted to halt seizures that resist standard drugs."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "A parasite is a major global cause: cerebral malaria seizes the brain acutely and leaves many survivors with chronic epilepsy, making it — with neurocysticercosis — a leading cause of acquired seizures in endemic regions."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Sometimes the immune system causes the seizures: in autoimmune epilepsy, T cells and the antibodies they help generate against neuronal proteins inflame the cortex, a treatable cause distinct from the structural and genetic forms."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Seizures inflame the brain that feeds them: NF-κB activation in neurons and glia after seizures drives the cytokine output and NLRP3 priming of epileptogenesis, a self-reinforcing neuroinflammatory loop that lowers the seizure threshold."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep and seizures pull on each other: sleep deprivation is a classic seizure trigger while epilepsy and its drugs fragment sleep, a bidirectional tangle in which insomnia worsens seizure control."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Fear of the next seizure breeds anxiety: generalized anxiety is among the commonest psychiatric comorbidities of epilepsy, driven both by the unpredictability of attacks and by shared limbic circuitry."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Prolonged seizures invite critical illness: status epilepticus and recurrent seizures cause aspiration and require intensive care, so aspiration pneumonia and sepsis are recognized complications of severe epilepsy."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Mood and seizure disorders overlap: bipolar disorder is over-represented in epilepsy, sharing neuronal-excitability mechanisms — which is why several anticonvulsants double as mood stabilizers."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Seizures reach the heart: ictal autonomic surges and arrhythmias underlie sudden unexpected death in epilepsy (SUDEP), and repeated seizure-related cardiac stress can contribute to cardiomyopathy and heart failure."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Seizures send secretions into the lungs: impaired consciousness during and after a seizure causes aspiration, and the resulting pneumonia — often pneumococcal — is a frequent and dangerous complication."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Falls and convulsions wound the body: sudden loss of control causes burns, lacerations, head injuries and fractures, leaving wounds whose healing competes with the next seizure's risk of re-injury."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Some of its drugs skew metabolism: valproate and other antiseizure medications cause weight gain and insulin resistance, raising the risk of type 2 diabetes over years of treatment."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones modulate seizures and the drugs disrupt hormones: catamenial epilepsy worsens with the menstrual cycle, and enzyme-inducing antiseizure drugs lower sex hormones, vitamin D and contraceptive efficacy."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its drugs can trigger life-threatening rashes: lamotrigine, carbamazepine and phenytoin are leading causes of Stevens-Johnson syndrome and toxic epidermal necrolysis, severe cutaneous drug reactions."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Convulsions and their drugs damage the skeleton: violent seizures cause vertebral compression fractures and posterior shoulder dislocations, and chronic enzyme-inducing drugs thin bone toward osteoporosis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It can stop the heart: ictal bradycardia, asystole and arrhythmias occur around seizures and contribute to sudden unexpected death in epilepsy (SUDEP)."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Seizures suppress breathing: peri-ictal central apnoea and aspiration are common, and the resulting hypoxia is a leading mechanism in sudden unexpected death in epilepsy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune system can ignite seizures: autoimmune encephalitis with anti-NMDA-receptor or LGI1 antibodies causes seizures that respond to immunotherapy rather than to anti-seizure drugs alone."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Treatment touches the gut and liver: valproate can be hepatotoxic, many antiepileptics induce liver enzymes, and the ketogenic diet used for refractory epilepsy works through gut metabolism."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Some drugs stone the kidney: carbonic-anhydrase-inhibiting antiepileptics like topiramate and zonisamide promote kidney stones and a metabolic acidosis."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Anticonvulsants can swell the nodes: phenytoin and aromatic antiepileptics cause hypersensitivity reactions (DRESS) with fever, rash and lymphadenopathy."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "A parasite that sparks seizures: cerebral toxoplasmosis, especially in HIV, and congenital infection produce brain lesions that are a common infectious cause of epilepsy worldwide."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "A leaky barrier feeds seizures: blood-brain-barrier breakdown lets serum proteins like albumin into the cortex, where they activate astrocytes and lower the seizure threshold, a driver of epileptogenesis."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Encephalitis leaves an epileptic scar: herpes simplex encephalitis damages the temporal lobe and is a classic cause of acquired, often drug-resistant temporal-lobe epilepsy."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Precision drugs for genetic epilepsy: the mTOR inhibitor everolimus reduces seizures in tuberous sclerosis, and gene-specific therapies are emerging for channelopathies — treating the cause rather than only suppressing seizures."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Cannabidiol became an anticonvulsant: purified cannabidiol (Epidiolex) is approved for Dravet, Lennox-Gastaut and TSC-related epilepsy, derived from the same plant whose heavy THC use causes cannabis use disorder."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Seizures can stop the heart: ictal and post-ictal disturbances of cardiac conduction — bradyarrhythmia and asystole — are implicated in SUDEP, the leading epilepsy-specific cause of death."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "Treating the depression that shadows seizures: depression is the commonest psychiatric comorbidity in epilepsy, and SSRIs like fluoxetine are first-line—the old fear that they meaningfully lower the seizure threshold is largely unfounded."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "Cortical lesions that spark seizures: epilepsy is several-fold more common in multiple sclerosis, where demyelinating plaques reaching the cerebral cortex create irritable, hyperexcitable foci that discharge as seizures."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Lupus that fires the brain: neuropsychiatric SLE can present with seizures, as immune-complex vasculopathy, autoantibodies and inflammation lower the cortical seizure threshold—epilepsy as a manifestation of systemic autoimmunity."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Seizures that aren't epileptic: psychogenic non-epileptic seizures, often rooted in trauma and PTSD, closely mimic epileptic events and frequently coexist with epilepsy, making video-EEG essential to tell them apart."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Shared central hyperexcitability: epilepsy and fibromyalgia both reflect a hyperexcitable nervous system with disturbed glutamate/GABA balance, and the gabapentinoids pregabalin and gabapentin treat both."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Antiepileptic bone disease: enzyme-inducing antiseizure drugs accelerate vitamin D catabolism, lowering cortical-bone density and raising fracture risk with long-term use—compounded by seizure-related falls."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Seizures with infection: COVID-19 causes acute symptomatic seizures through encephalopathy, hypoxia and inflammation, and new-onset epilepsy has been reported after infection."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "Paraneoplastic seizures: small-cell lung cancer triggers seizures through brain metastases and anti-Hu paraneoplastic limbic encephalitis, an oncological cause of new-onset epilepsy in smokers."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Paroxysmal-event mimics: cataplexy and sleep attacks of narcolepsy can be mistaken for seizures, making it part of the differential of episodic neurological events alongside epilepsy."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Pro-seizure cytokine: IL-1β released by activated glia lowers seizure threshold and promotes epileptogenesis, a central mediator of the neuroinflammation that sustains chronic epilepsy."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory excitability: TNF-α modulates glutamate and GABA receptor trafficking to enhance neuronal excitability, linking brain inflammation to seizure generation."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Cholinergic seizures: excess cholinergic activity, as in organophosphate poisoning or autosomal-dominant nocturnal frontal-lobe epilepsy, can trigger seizures and status epilepticus."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Neuroinflammatory recruitment: CCL2 released after seizures recruits monocytes and helps breach the blood-brain barrier, part of the neuroinflammation that lowers seizure threshold and drives epileptogenesis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Barrier breakdown: VEGF surges after seizures, opening the blood-brain barrier and driving aberrant angiogenesis, a vascular contribution to the epileptogenic remodelling of the brain."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Stress and seizures: CRH is a proconvulsant neuropeptide in the developing brain, part of why stress lowers seizure threshold and underlies the early-life seizures of conditions like infantile spasms."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "DAMP-driven epileptogenesis: HMGB1 released by injured neurons signals through TLR4 to lower seizure threshold and promote epileptogenesis, a neuroinflammatory pathway under study as an anti-epileptogenic drug target."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "TrkB epileptogenesis: BDNF signalling through TrkB drives the aberrant synaptic sprouting and network remodelling that convert a normal brain into an epileptic one, making TrkB a target to prevent epilepsy after injury."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Proconvulsant hormone: estrogen lowers the seizure threshold, the counterpart to progesterone's protective effect, underlying the catamenial pattern in which seizures cluster around the high-estrogen phases of the menstrual cycle."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium-channel seizures: T-type voltage-gated calcium channels generate the thalamocortical rhythms of absence seizures — the target of ethosuximide — and other calcium-channel mutations cause genetic epilepsies, making calcium currents a second ionic axis beyond sodium."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonergic control: serotonin raises the seizure threshold and is the mechanism of fenfluramine, now a key drug for Dravet and Lennox-Gastaut syndromes, while serotonergic brainstem dysfunction is implicated in sudden unexpected death in epilepsy (SUDEP)."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "Hormonal therapy: ACTH (corticotropin) is a first-line treatment for infantile spasms (West syndrome), uniquely effective at stopping the epileptic encephalopathy through mechanisms beyond its glucocorticoid induction."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "mTORopathy epilepsy: the PI3K-AKT-mTOR pathway (mTOR already mapped) is hyperactivated in the mTORopathies — tuberous sclerosis and focal cortical dysplasia (already mapped) — that cause drug-resistant focal epilepsy."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Network synchronisation: astrocytic connexin-43 gap junctions synchronise neuronal networks and buffer extracellular potassium and glutamate, and their dysregulation contributes to seizure generation and spread in epilepsy."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Excitotoxic death: prolonged seizures and status epilepticus trigger caspase-3-mediated neuronal apoptosis, the excitotoxic cell death contributing to the hippocampal sclerosis and progression of epilepsy."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Seizure-induced inflammation: seizures induce COX-2 and prostaglandin synthesis in the brain, amplifying neuroinflammation and blood-brain-barrier breakdown that lower seizure threshold and drive epileptogenesis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate epileptogenesis: the TLR4-MyD88-NF-κB axis, activated by HMGB1 and other damage signals released during seizures, sustains the neuroinflammatory loop that promotes hyperexcitability and recurrent seizures."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative epileptogenesis: seizures generate oxidative stress that NRF2-driven antioxidant defences counter, and NRF2 activation is neuroprotective against the mitochondrial injury and neuronal loss of chronic epilepsy."
  - target: 01-human/03-molecular/tsc1-tsc2
    relation: connects-to
    note: "Loss of TSC1-TSC2 control of mTOR (mTOR mapped) causes the cortical malformations and mTORopathy epilepsies such as tuberous sclerosis."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN regulation of the PI3K-AKT-mTOR axis (AKT and mTOR mapped) underlies the malformations of cortical development that cause refractory epilepsy."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling is activated during epileptogenesis, contributing to the neuronal hyperexcitability and network reorganisation of chronic epilepsy."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 released by activated microglia amplifies the neuroinflammation that contributes to epileptogenesis and seizure progression."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK-STAT3 signalling drives the reactive astrogliosis that remodels neural networks during the development of chronic epilepsy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA released by neuronal injury can engage cGAS-STING, contributing to the neuroinflammation that promotes epileptogenesis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of the PTEN-PI3K-AKT-mTOR axis (PTEN, AKT, mTOR, and TSC1-TSC2 already mapped) regulates neuronal excitability and the structural plasticity implicated in epileptogenesis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 neuroinflammatory signaling contributes to the glial activation and seizure susceptibility of epilepsy."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α responses to seizure-induced metabolic and hypoxic stress shape the neurovascular remodeling and epileptogenesis of epilepsy."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the neuronal excitability, survival signaling, and mTOR crosstalk (mTOR already mapped) relevant to epileptogenesis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-mTOR metabolic signaling regulates the neuronal energetics and mTORopathy-driven cortical hyperexcitability of epilepsy."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the neuroinflammatory activation that lowers the seizure threshold in epilepsy."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT-mTOR signaling (AKT and mTOR already mapped; PTEN and TSC already mapped) drives the mTOR-pathway (mTORopathy) focal epilepsies."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal homeostasis and mTOR-linked mechanisms implicated in epilepsy."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic reprogramming during epileptogenesis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the NMDA-receptor and synaptic-plasticity mechanisms of the hyperexcitability of epilepsy."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation that promotes epileptogenesis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroinflammation and blood-brain-barrier dysfunction of epilepsy."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the glial and neuroinflammatory responses of epilepsy."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation of epilepsy."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the microglial synaptic remodeling and neuroinflammation of epilepsy."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Synaptic zinc: zinc is co-released with glutamate at hippocampal mossy-fibre synapses and modulates GABA-A and NMDA receptors, so disturbances of synaptic zinc alter seizure susceptibility in temporal lobe epilepsy."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Chronobiology: seizures often cluster with circadian and sleep-wake patterns, and melatonin, which regulates sleep and shows anticonvulsant properties, is used adjunctively in some epilepsy syndromes."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Seizure signalling: nitric oxide has a dual, context-dependent role in seizure generation and termination through its modulation of the glutamatergic and GABAergic transmission already mapped."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Noradrenergic seizure threshold: the noradrenergic system raises the seizure threshold, and vagus-nerve stimulation exerts part of its anticonvulsant effect through norepinephrine, complementing the serotonergic modulation (already mapped) of seizure control."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histaminergic modulation: central histamine raises the seizure threshold, which is why H1-antihistamines that cross into the brain can lower it, implicating the histaminergic system in seizure susceptibility."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic seizures: hypoglycaemia from excess insulin provokes seizures, and the metabolic fuel switch underlies the ketogenic diet's efficacy, linking glucose and insulin handling to seizure control in epilepsy."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative epileptogenesis: seizures and the underlying injury generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative stress (NRF2 already mapped) promotes the epileptogenesis and neuronal damage of recurrent seizures."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Neuroinflammatory balance: the anti-inflammatory IL-10 opposes the pro-inflammatory cytokines (IL-1, TNF and IL-6 already mapped) of the neuroinflammation that promotes epileptogenesis, part of the immune dimension of epilepsy."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopaminergic threshold: dopamine modulates the seizure threshold, with D1 receptors tending to be proconvulsant and D2 anticonvulsant (serotonin and norepinephrine already mapped), part of the neuromodulatory control of seizure susceptibility."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroinflammatory balance: the anti-inflammatory IL-4 counters the pro-inflammatory cytokines (IL-1, TNF and IL-6 already mapped) of the neuroinflammation that promotes epileptogenesis (IL-10 already mapped), part of the immune dimension of epilepsy."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic seizure threshold: leptin has anticonvulsant effects and links the energy state to neuronal excitability, part of the metabolic regulation of the seizure threshold exploited by the ketogenic diet used in refractory epilepsy."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Dietary anticonvulsants: the omega-3 fatty acids have anticonvulsant properties and, with the ketogenic diet, form part of the dietary approaches to epilepsy that modulate neuronal excitability and neuroinflammation (prostaglandins already mapped)."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Neuroinflammation balance: IL-13, with IL-4 (already mapped), supports the M2 microglial anti-inflammatory arm that balances the neuroinflammation (TNF, IL-6 and IL-1 already mapped) which lowers the seizure threshold in epilepsy."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic seizure threshold: adiponectin, with leptin (already mapped), has neuroprotective and anticonvulsant effects, part of the metabolic regulation of the seizure threshold exploited by the ketogenic diet."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Incretin neuroprotection: GLP-1 and its receptor agonists have neuroprotective and possible anticonvulsant effects, linking the metabolic state (insulin already mapped) to the seizure threshold in epilepsy."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Neuroinflammatory epileptogenesis: the microglial activation and the neuroinflammation (IL-1, TNF and IL-6 already mapped) drive the epileptogenesis and are a target of the anti-inflammatory antiseizure approaches."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "ASD comorbidity: epilepsy and autism spectrum disorder are highly comorbid, sharing the mTOR, channel and excitatory/inhibitory (glutamate and GABA already mapped) mechanisms."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "NMDA and eclampsia: magnesium blocks the NMDA/glutamate (already mapped) receptor and is the treatment of the eclamptic seizures; the hypomagnesaemia lowers the seizure threshold."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, contributes to the neuroinflammation (IL-1 and IL-6 already mapped) that lowers the seizure threshold and drives the epileptogenesis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune contribution to the epileptogenesis of epilepsy."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the metabolic-inflammatory dimension linked to epilepsy."
---

# Epilepsy

## Overview

**Epilepsy** is a chronic neurological disorder characterized by a predisposition to generate **recurrent unprovoked seizures** — the result of abnormal, excessive, or synchronous neuronal activity in the brain. The International League Against Epilepsy (ILAE) definition requires at least two unprovoked seizures occurring >24 hours apart, or one unprovoked seizure with ≥60% recurrence risk (e.g., a seizure after a stroke, cortical malformation, or certain EEG patterns) [^fisher-2017-ilae-classification].

Epilepsy affects approximately **50 million people worldwide** (~1% of the global population), making it the most common serious neurological condition after stroke and Alzheimer's disease. The annual incidence is 50-70 per 100,000 in developed countries; higher in low-income countries (120+ per 100,000) due to higher rates of birth asphyxia, infections (neurocysticercosis, cerebral malaria), and traumatic brain injury. **Drug-refractory epilepsy** — failure of two appropriately chosen antiepileptic drugs — affects ~30% of patients and represents the highest unmet need in epilepsy management [^devinsky-2018-epilepsy-review].

The biological basis of epilepsy is an imbalance between **neuronal excitation** (primarily glutamatergic, via AMPA and NMDA receptors) and **inhibition** (primarily GABAergic, via GABA-A chloride channels and GABA-B metabotropic receptors). Seizures arise when excitation transiently overwhelms inhibition in a pathologically susceptible network — due to ion channel mutations, cortical malformations, hippocampal sclerosis, autoimmune neuronal antibodies, metabolic derangements, or unknown causes.

## Structure

### ILAE 2017 seizure classification [^fisher-2017-ilae-classification]

**Focal seizures** (originate in a discrete cortical network in one hemisphere):
- **Focal aware** (formerly simple partial): Consciousness preserved; symptoms reflect the affected cortical region (motor, sensory, autonomic, psychic)
- **Focal impaired awareness** (formerly complex partial): Consciousness impaired; automatisms (lip-smacking, hand fumbling) common; most often from temporal lobe
- **Focal to bilateral tonic-clonic**: Focal seizure generalizes to involve both hemispheres → tonic-clonic convulsion; post-ictal confusion (Todd's paralysis possible if motor cortex involved)

**Generalized seizures** (involve both hemispheres from onset via cortical-subcortical networks):
- **Generalized tonic-clonic (GTC)**: Tonic phase (stiffening) → clonic phase (rhythmic jerking) → post-ictal stupor; highest injury/SUDEP risk
- **Absence (petit mal)**: 3 Hz spike-wave discharge on EEG; brief (5–30 s) staring with eye flicker; no post-ictal phase; childhood absence epilepsy (CAE) peak onset 4-8 years; often remits by puberty
- **Myoclonic**: Brief, shock-like muscle jerks; often in upper limbs; occur in juvenile myoclonic epilepsy (JME), Dravet syndrome, progressive myoclonic epilepsies
- **Atonic**: Sudden loss of muscle tone → drop attacks; associated with Lennox-Gastaut syndrome
- **Tonic, clonic**: Single-phase variants of GTC

### Epilepsy classification by etiology

| Etiology | Key examples | Mechanism | Seizure type |
|:---|:---|:---|:---|
| **Structural** | Hippocampal sclerosis (MTLE), cortical malformations (FCD), stroke, tumor | Focal cortical excitability ↑ from scarring/reorganization | Focal (±generalization) |
| **Genetic** | SCN1A (Dravet), KCNQ2 (neonatal), TSC1/2 (TSC), CDKL5, PCDH19 | Ion channel/scaffolding protein dysfunction | Focal or generalized |
| **Autoimmune** | Anti-NMDAR, anti-LGI1, anti-CASPR2, anti-GAD65 | Autoantibodies impair synaptic function | Focal (faciobrachial in LGI1), GTC |
| **Infectious** | Neurocysticercosis, cerebral malaria, HIV encephalitis | Perilesional inflammation/gliosis | Focal |
| **Metabolic** | Hypoglycemia, hyponatremia, GLUT1 deficiency, pyridoxine dependency | Altered ionic milieu or cofactor deficiency | Generalized |
| **Unknown** | ~30% of all epilepsies | Not yet identified | Focal or generalized |

### Key genetic epilepsy syndromes

| Gene | Channel/Protein | Syndrome | Key feature |
|:---|:---|:---|:---|
| **SCN1A** | Nav1.1 (GABAergic interneurons) | Dravet syndrome (SMEI) | Fever-sensitive; avoid Na-channel blockers |
| **SCN2A** | Nav1.2 (excitatory neurons) | Neonatal-onset encephalopathy | LOF early-onset; GOF late-onset; precision Na-channel therapy |
| **KCNQ2** | Kv7.2/Kv7.3 (M-current) | Neonatal epileptic encephalopathy | K+ channel LOF → neonatal seizures; carbamazepine beneficial |
| **CDKL5** | CDK-like kinase 5 | CDKL5 deficiency disorder | X-linked; spasms + severe encephalopathy; no effective treatment |
| **TSC1/TSC2** | Hamartin/Tuberin (mTOR) | Tuberous sclerosis complex | Cortical tubers + seizures (80%); everolimus reduces seizures |
| **PCDH19** | Protocadherin-19 | PCDH19 epilepsy | X-linked; affects only females; fever-sensitive clusters |
| **MECP2** | MeCP2 transcription factor | Rett syndrome | Progressive; loss of hand use; regression; after normal infancy |

### Autoimmune epilepsy

Neuronal autoantibodies cause acute encephalitis with new-onset epilepsy — often confused with viral encephalitis or new-onset psychiatric illness:

| Antibody target | Clinical syndrome | Seizure type | Treatment |
|:---|:---|:---|:---|
| **NMDA receptor (GluN1)** | Anti-NMDAR encephalitis | Complex focal, GTC; movement disorder | IVIG + methylprednisolone + rituximab |
| **LGI1** | Limbic encephalitis; faciobrachial dystonic seizures (FBDS) | FBDS (pathognomonic); complex focal | IVIG + steroids; FBDS responds dramatically |
| **CASPR2** | Morvan syndrome; limbic encephalitis | Complex focal; tonic | IVIG + steroids; thymoma association |
| **GAD65** | Stiff-person syndrome; limbic encephalitis | Complex focal; rarely GTC | Steroids; often poorly responsive |
| **AMPA receptor** | Limbic encephalitis | Complex focal | Steroids + rituximab |

Anti-NMDAR encephalitis is the most common autoimmune encephalitis (~37% of autoimmune encephalitis cases); predominantly affects young women; ovarian teratoma in ~50% of adult women; recovery possible with immunotherapy.

## Function

### Seizure initiation and spread

**Focal seizure initiation**: Abnormal synchronous burst firing (intrinsic bursting neurons + excitatory recurrent collaterals) overwhelms local inhibitory GABAergic interneurons → ictal discharge → spreads via cortical-cortical U-fibers and white matter tracts to ipsilateral, then contralateral networks.

**Absence seizure mechanism (cortical-thalamic model):**
1. Cortical focus → thalamic relay nuclei → reticular thalamic nucleus (RTN, GABAergic) → suppresses relay nuclei → synchronized 3 Hz oscillation; thalamic hyperpolarization → T-type calcium channel activation → low-threshold calcium spikes → rhythmic 3 Hz spike-wave
2. Valproate, ethosuximide, and lamotrigine inhibit T-type calcium channels → suppress absence seizures

**EEG signatures:**
- **3 Hz generalized spike-wave**: Childhood absence epilepsy, juvenile absence epilepsy
- **3-5.5 Hz polyspike-wave**: Juvenile myoclonic epilepsy (JME)
- **Hypsarrhythmia** (chaotic high-amplitude pattern): West syndrome (infantile spasms)
- **Slow spike-wave (<2.5 Hz)**: Lennox-Gastaut syndrome
- **Focal interictal epileptiform discharges (IEDs)**: Focal epilepsy; location reveals seizure focus
- **Temporal lobe theta/alpha**: Mesial temporal lobe epilepsy

### Mesial temporal lobe epilepsy (MTLE) — the most common adult focal epilepsy

**MTLE with hippocampal sclerosis (HS)** — the predominant adult focal epilepsy:
- **Pathology**: Selective loss of CA1 and CA3 hippocampal pyramidal neurons + mossy fiber sprouting (aberrant glutamatergic recurrent collaterals) → hyperexcitable hippocampus
- **Clinical features**: Aura (rising epigastric sensation, déjà vu, fear), complex partial seizures with oroalimentary automatisms, post-ictal confusion lasting minutes
- **Triggers**: Febrile seizures in early childhood (FS-HS relationship controversial), TBI, encephalitis
- **MRI findings**: T2/FLAIR hippocampal signal increase, CA1 atrophy, loss of internal structure on coronal MRI
- **Surgery**: Temporal lobectomy (anterior temporal + amygdalohippocampectomy) → 65-70% seizure-free at 2 years; superior to medical therapy in RCTs [^engel-2012-mtle-surgery]

## Pathology

### Status epilepticus (SE)

**Definition:** Seizure lasting >5 minutes (convulsive SE) or >30 minutes (non-convulsive SE) OR recurrent seizures without return to baseline.

**Emergency management (time-critical):**
1. **0–5 min**: Airway, breathing, circulation; check glucose; lorazepam (0.1 mg/kg IV, max 4 mg) or midazolam (IM/buccal/nasal) — benzodiazepine first-line
2. **5–20 min**: If benzodiazepine fails: levetiracetam (60 mg/kg IV), valproate (40 mg/kg IV), or fosphenytoin (20 mg/kg PE IV)
3. **20–40 min**: If refractory: repeat the above; anesthesia consultation
4. **>40 min (super-refractory SE)**: Midazolam or propofol infusion; ketamine (NMDA antagonist); phenobarbital; EEG monitoring

**Morbidity:** Each 10 minutes of convulsive SE increases neuronal injury; NCSE (nonconvulsive) can cause hippocampal atrophy with diagnostic delay.

### Diagnostic evaluation

**EEG:** Interictal discharges; ictal pattern; prolonged monitoring (video-EEG) for seizure capture; sleep deprivation activates discharges.

**MRI:** 3T MRI with thin-slice coronal FLAIR; MTLE shows hippocampal sclerosis; FCD appears as cortical thickening/blurring; tuberous sclerosis shows cortical tubers.

**Advanced evaluation (presurgical):**
- **FDG-PET**: Interictal hypometabolism identifies seizure focus even when MRI is negative
- **SPECT ictal/interictal subtraction (SISCOM)**: Captures hyperperfusion of ictal focus
- **SEEG (stereo-EEG)**: Invasive recording via depth electrodes for multi-lobar or deep foci
- **Wada test (IATC sodium amobarbital procedure)**: Determines dominant hemisphere for language before temporal surgery
- **fMRI language/memory lateralization**: Non-invasive Wada alternative

**Genetic testing:**
- Gene panel (50-100 epilepsy genes) for early-onset epileptic encephalopathy
- Whole exome sequencing for unexplained epilepsy in children
- **Dravet workup**: SCN1A sequencing (80% yield); if negative → PCDH19 (females), SCN1B, GABRG2
- Autoimmune workup: CSF + serum NMDAR, LGI1, CASPR2, AMPAR, GABA-B panels

### Treatment

**First-line antiepileptic drugs (AEDs):**

| Drug | Mechanism | Best for | Avoid in |
|:---|:---|:---|:---|
| **Valproate** | Na-channel, GABA-T inhibitor, T-Ca²⁺ | Broad-spectrum; generalized + focal | Pregnancy (teratogen); hepatic disease; do NOT stop abruptly |
| **Levetiracetam** | SV2A synaptic vesicle protein | Broad-spectrum; fewest interactions | Psychiatric side effects (irritability) |
| **Lamotrigine** | Na-channel (slow inactivation) | Focal + generalized; pregnancy-preferred; absence | Dravet syndrome (worsen); ramp slowly (Stevens-Johnson risk) |
| **Carbamazepine** | Na-channel | Focal epilepsy first-line; trigeminal neuralgia | Generalized/absence (worsen); HLA-B*1502 risk (Asian) → SJS |
| **Oxcarbazepine** | Na-channel | Focal; well-tolerated | Hyponatremia; Dravet |
| **Ethosuximide** | T-type Ca²⁺ channel | Absence ONLY; first-line absence | GTC (not effective) |
| **Topiramate** | Multiple (AMPA, Na, CA) | Focal; migraine prophylaxis; weight loss | Cognition ("dopamax"); renal stones |
| **Zonisamide** | Na-channel + T-Ca²⁺ | Focal + generalized; Parkinson's (adjunct) | Weight loss; renal stones |
| **Lacosamide** | Na-channel (slow inactivation) | Focal adjunct; IV available | Cardiac conduction (avoid with PR prolongation) |
| **Perampanel** | AMPA antagonist | Focal + GTC adjunct | Aggression/psychiatric; CYP450 interactions |

**Dravet-specific AEDs** (see SCN1A entry): valproate, clobazam, stiripentol, fenfluramine, cannabidiol.

**Drug-refractory epilepsy interventions:**

- **Temporal lobectomy**: For MTLE with hippocampal sclerosis; 65-70% seizure-free [^engel-2012-mtle-surgery]; memory risk on dominant side (assess with Wada/fMRI)
- **Focal cortical resection**: For FCD, tumor-related epilepsy, post-traumatic focal epilepsy
- **Corpus callosotomy**: For atonic/tonic drop attacks in Lennox-Gastaut; anterior 2/3 reduces falls without memory risk
- **VNS (vagus nerve stimulation)**: Left cervical vagus → nucleus tractus solitarius → cortical activation/inhibition; implanted stimulator; ~50% responder rate (≥50% seizure reduction); rescue magnetic stimulation available
- **RNS (responsive neurostimulation)**: Cortical-depth electrode array → closed-loop electrical stimulation on seizure detection; approved for drug-refractory focal epilepsy
- **Ketogenic diet (KD)**: High-fat (4:1 fat:carbohydrate+protein); starvation ketosis → ketone body metabolism → GABAergic mechanisms; most effective in: GLUT1 deficiency (first-line), PDH deficiency, Dravet syndrome; ~50% responder rate in drug-refractory childhood epilepsy
- **LITT (laser interstitial thermal therapy)**: MRI-guided laser ablation of hippocampus or seizure focus; minimally invasive alternative to open surgery; ~55% seizure-free for MTLE

## Connections

- `connects-to` → **[SCN1A](../../03-molecular/scn1a/README.md)** — SCN1A LOF mutations cause Dravet syndrome (most severe genetic epilepsy; Nav1.1 haploinsufficiency in GABAergic interneurons → cortical disinhibition → fever-sensitive seizures); SCN1A gain-of-function causes GEFS+; sodium channel blockers worsen Dravet; fenfluramine and cannabidiol are FDA-approved.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — cortical inhibitory balance maintained by GABAergic interneurons is the fundamental seizure brake; GABA-A receptor potentiators (benzodiazepines, phenobarbital, clobazam) and GABA-T inhibitors (valproate) are the most widely used antiepileptic drugs; GABA-A receptor subunit mutations (GABRG2, GABRA1) cause genetic generalized epilepsies.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — TSC1/TSC2 LOF → mTOR hyperactivation → cortical tubers → epilepsy in 80-90% of TSC patients; somatic PIK3CA/MTOR mutations cause focal cortical dysplasia IIb; mTOR inhibitor everolimus reduces TSC-associated seizures by ~50% (EXIST-3 trial); mTOR pathway is the major therapeutic target for structural genetic epilepsies.
- `targets` → **[Brain](../../06-organ/brain/README.md)** — epilepsy arises from focal or generalized cortical networks; hippocampal sclerosis in MTLE causes the most common adult focal epilepsy; EEG captures ictal/interictal cortical discharges; epilepsy surgery (temporal lobectomy) directly resects the epileptogenic zone.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — epilepsy risk is 2-3× elevated in AD; amyloid-driven cortical hyperexcitability precedes clinical dementia; anti-NMDAR and LGI1 autoimmune encephalitides present with epilepsy and cognitive decline, mimicking rapid-onset dementia and requiring different treatment.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Allopregnanolone (progesterone metabolite) is a potent GABA-A PAM via delta subunit extrasynaptic receptors → sedation, anxiolysis, anticonvulsant; progesterone withdrawal → allopregnanolone decline → GABA-A downregulation → seizure threshold reduction in catamenial epilepsy.
- `connects-to` → **[Migraine](../migraine/README.md)** — Epilepsy and migraine are comorbid disorders of cortical hyperexcitability that share genetics: gain-of-function SCN1A causes familial hemiplegic migraine while loss-of-function causes Dravet epilepsy, and valproate and topiramate treat both.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Seizures are an excitation-inhibition imbalance, and glutamate is the excitatory side: AMPA/NMDA over-activity drives synchronous bursting, and the AMPA antagonist perampanel is an antiseizure drug — the counterpart to GABA's brake.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — A seizure is hypersynchronous neuronal firing: bursting pyramidal neurons and recurrent excitatory collaterals overwhelm GABAergic interneurons → a paroxysmal depolarizing shift; most genetic epilepsies are neuronal ion-channelopathies that tip this balance.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Tuberous sclerosis is a paradigmatic genetic epilepsy: cortical tubers and TSC1/TSC2-driven mTOR overactivation cause early, often drug-resistant seizures (including infantile spasms), so mTOR inhibitors (everolimus) reduce seizures and early EEG-guided treatment is studied.
- `connects-to` → **[Stroke](../stroke/README.md)** — Stroke is a leading cause of acquired epilepsy in older adults: cortical infarcts and hemorrhages leave a gliotic, hyperexcitable scar that generates late-onset focal seizures months to years later; post-stroke epilepsy worsens outcomes and is managed with antiseizure medication.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes are active players in epilepsy, not bystanders: reactive astrogliosis impairs glutamate and potassium buffering and disrupts the blood-brain barrier, lowering seizure threshold; aberrant gap-junction coupling and inflammation sustain epileptogenesis.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — Epilepsy and autism frequently co-occur and share biology: up to a third of autistic people have epilepsy, and both arise from disrupted excitation/inhibition balance and overlap in genes like SCN, TSC, and SHANK—often the same neurodevelopmental lesion.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — Seizures are the commonest first sign of an IDH-mutant glioma: these slow-growing cortical tumors irritate neurons (partly via the oncometabolite 2-hydroxyglutarate altering glutamate), so new focal epilepsy in a young adult should prompt imaging for a low-grade glioma.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Epilepsy and depression have a bidirectional relationship: depression is the commonest psychiatric comorbidity of epilepsy and also raises the risk of developing it, shared limbic and serotonergic mechanisms link them, and depression strongly degrades quality of life.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — Brain tumors are an important cause of epilepsy: glioblastoma and other gliomas irritate surrounding cortex, so new-onset seizures in an adult mandate brain imaging—seizures are often the presenting sign of a glioma, and tumor-related epilepsy can be hard to control.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus is the seat of the commonest focal epilepsy: mesial temporal sclerosis—hippocampal scarring and neuron loss—generates temporal-lobe seizures, and surgically removing the sclerotic hippocampus can cure drug-resistant cases.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Epilepsy and schizophrenia are bidirectionally linked: temporal-lobe epilepsy can produce a schizophrenia-like psychosis, each roughly doubles the risk of the other, and they share disturbances of glutamate and GABA—so a first psychotic episode sometimes warrants EEG.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Voltage-gated sodium channels are epilepsy's central target: sodium influx fires the action potentials that, when runaway, become seizures, so many first-line drugs (phenytoin, lamotrigine) work by blocking these channels—and SCN1A mutations cause epilepsy.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Epilepsy is fundamentally a disorder of the synapse: seizures arise when synaptic excitation (glutamate) overwhelms inhibition (GABA), so the tipped excitation-inhibition balance at synapses is the common final pathway across epilepsy's many causes.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Epilepsy is a disorder of the whole nervous system's electrical stability: hypersynchronous neuronal discharges can start focally or generalize across networks, so seizures are a shared symptom of countless insults—from genetics to stroke, tumor and infection.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Potassium channels set the brain's seizure threshold: by repolarizing neurons and damping excitability, Kv7/KCNQ channels guard against runaway firing, so their mutations cause familial epilepsies—and openers that boost potassium currents are an anticonvulsant strategy.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The endocannabinoid system tempers seizures: cannabinoid signaling dampens excitatory transmission, and purified cannabidiol is now approved for severe childhood epilepsies like Dravet and Lennox-Gastaut—turning a cannabis compound into a proven anticonvulsant.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome helps the ketogenic diet fight epilepsy: this high-fat diet controls drug-resistant seizures partly by reshaping gut bacteria and their metabolites, so the gut-brain axis is part of how a dietary therapy calms the epileptic brain.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium channels generate the rhythm of absence seizures: thalamic T-type calcium currents drive the 3-Hz spike-wave discharges of absence epilepsy, which is why the T-type blocker ethosuximide specifically treats them—not the sodium-channel drugs used elsewhere.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Epilepsy is fueled by microglial neuroinflammation: seizures activate microglia that release cytokines lowering seizure threshold, creating a feed-forward loop of epileptogenesis—so inflammation is both a consequence and a driver of recurrent seizures.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Epilepsy's deadliest complication strikes the heart: in SUDEP (sudden unexpected death in epilepsy), a seizure triggers fatal cardiac arrhythmia or asystole and respiratory arrest, making seizure control a matter of preventing sudden death, not just fits.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF helps rewire the brain into an epileptic one: after injury or seizures, surging BDNF promotes the abnormal sprouting and excitability that turn normal circuits epileptogenic, so it is studied as a driver of how epilepsy develops.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine is the brain's built-in seizure brake: it accumulates during intense firing and damps neurons, ending seizures, and the ketogenic diet's anticonvulsant effect works partly by boosting this adenosine tone.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Epilepsy involves the brain's myelin too: oligodendrocyte and white-matter abnormalities accompany many epilepsies, and seizures in turn disrupt myelination, linking impaired connectivity to the seizure-prone network.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Light itself can trigger seizures: in photosensitive epilepsy, flashing lights and certain patterns drive abnormal synchronous firing through the visual system, so the photons hitting the retina set off a seizure—why strobe effects carry warnings.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Epilepsy treatment runs through the liver: most antiseizure drugs are metabolized there, inducing or inhibiting enzymes that cause drug interactions, and some (like valproate) can injure the liver, so liver function shapes the choice of medication.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — GABA calms the brain by moving chloride: opening chloride channels normally quiets neurons, but when the chloride gradient is immature or disrupted GABA can instead excite them, a switch that underlies hard-to-treat neonatal seizures.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium calms overexcited neurons: intravenous magnesium is the treatment for eclamptic seizures, and a low magnesium level can itself lower the seizure threshold, tying the mineral to seizure control.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Diet and the gut shape epilepsy: the ketogenic diet controls many drug-resistant seizures, and the gut microbiome it reshapes appears to mediate part of that protection through the gut-brain axis.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — When drugs fail, epilepsy is treated through a nerve: vagus nerve stimulation sends regular pulses along this peripheral nerve to the brain, reducing seizure frequency in refractory cases.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the scarred epileptic focus: in mesial temporal sclerosis the hippocampus loses neurons and gliosis takes over, while surviving granule cells sprout aberrant mossy fibers that wire the runaway circuits of seizures.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Long-term seizure drugs quietly weaken bone: enzyme-inducing antiepileptics speed the liver's breakdown of vitamin D, so deficiency, osteomalacia, and fractures are a recognized hazard of years on treatment.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — A prolonged seizure can poison the kidney: violent muscle activity in status epilepticus breaks down muscle, and the released myoglobin clogs the renal tubules, threatening acute kidney injury.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Anti-seizure drugs can erupt on the skin: carbamazepine, lamotrigine, and phenytoin can trigger Stevens-Johnson syndrome and toxic epidermal necrolysis, a risk so tied to the HLA-B*1502 allele that some patients are genotyped first.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Epilepsy and its drugs reach into reproduction: valproate is strongly teratogenic, enzyme-inducing drugs undercut hormonal contraception, and many women have catamenial seizures that cluster with the menstrual cycle's hormone swings.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Some anti-seizure drugs strike the marrow: carbamazepine can cause agranulocytosis and aplastic anemia, while phenytoin interferes with folate to produce a megaloblastic anemia — so blood counts are monitored.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Some seizures are autoimmune: antibodies against NMDA-receptor or LGI1 cause an encephalitis whose seizures resist standard drugs but respond to immunotherapy, a treatable cause now sought in new-onset, unexplained epilepsy.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Long-term seizure drugs thin the bones: enzyme-inducing anti-seizure medicines speed vitamin D breakdown, lowering calcium and driving the osteomalacia and osteoporosis that leave epilepsy patients prone to fractures.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Valproate quietly drops the platelets: the widely used anti-seizure drug causes a dose-related thrombocytopenia and platelet dysfunction, watched especially before surgery or when bleeding appears.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — A slow-growing tumor can announce itself as a seizure: a meningioma pressing on the cortex irritates the neurons beneath it, so a new seizure in an adult prompts brain imaging to find such a structural cause.
- `connects-to` → **[West Nile Virus](../west-nile-virus/README.md)** — Brain infection sparks seizures: West Nile and other encephalitides inflame the cortex into acute seizures, and the scar they leave can become a focus for later epilepsy.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation lowers the seizure threshold: seizures trigger a surge of IL-6 and other cytokines, and this neuroinflammation in turn makes neurons more excitable, a feed-forward loop now seen as part of epileptogenesis.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — An inflammasome fuels the feed-forward loop: NLRP3 activation in microglia releases IL-1β that heightens neuronal excitability, a driver of epileptogenesis being targeted to halt seizures that resist standard drugs.
- `connects-to` → **[Malaria](../malaria/README.md)** — A parasite is a major global cause: cerebral malaria seizes the brain acutely and leaves many survivors with chronic epilepsy, making it — with neurocysticercosis — a leading cause of acquired seizures in endemic regions.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Sometimes the immune system causes the seizures: in autoimmune epilepsy, T cells and the antibodies they help generate against neuronal proteins inflame the cortex, a treatable cause distinct from the structural and genetic forms.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Seizures inflame the brain that feeds them: NF-κB activation in neurons and glia after seizures drives the cytokine output and NLRP3 priming of epileptogenesis, a self-reinforcing neuroinflammatory loop that lowers the seizure threshold.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep and seizures pull on each other: sleep deprivation is a classic seizure trigger while epilepsy and its drugs fragment sleep, a bidirectional tangle in which insomnia worsens seizure control.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Fear of the next seizure breeds anxiety: generalized anxiety is among the commonest psychiatric comorbidities of epilepsy, driven both by the unpredictability of attacks and by shared limbic circuitry.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Prolonged seizures invite critical illness: status epilepticus and recurrent seizures cause aspiration and require intensive care, so aspiration pneumonia and sepsis are recognized complications of severe epilepsy.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Mood and seizure disorders overlap: bipolar disorder is over-represented in epilepsy, sharing neuronal-excitability mechanisms — which is why several anticonvulsants double as mood stabilizers.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Seizures reach the heart: ictal autonomic surges and arrhythmias underlie sudden unexpected death in epilepsy (SUDEP), and repeated seizure-related cardiac stress can contribute to cardiomyopathy and heart failure.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Seizures send secretions into the lungs: impaired consciousness during and after a seizure causes aspiration, and the resulting pneumonia — often pneumococcal — is a frequent and dangerous complication.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Falls and convulsions wound the body: sudden loss of control causes burns, lacerations, head injuries and fractures, leaving wounds whose healing competes with the next seizure's risk of re-injury.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Some of its drugs skew metabolism: valproate and other antiseizure medications cause weight gain and insulin resistance, raising the risk of type 2 diabetes over years of treatment.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones modulate seizures and the drugs disrupt hormones: catamenial epilepsy worsens with the menstrual cycle, and enzyme-inducing antiseizure drugs lower sex hormones, vitamin D and contraceptive efficacy.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its drugs can trigger life-threatening rashes: lamotrigine, carbamazepine and phenytoin are leading causes of Stevens-Johnson syndrome and toxic epidermal necrolysis, severe cutaneous drug reactions.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Convulsions and their drugs damage the skeleton: violent seizures cause vertebral compression fractures and posterior shoulder dislocations, and chronic enzyme-inducing drugs thin bone toward osteoporosis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It can stop the heart: ictal bradycardia, asystole and arrhythmias occur around seizures and contribute to sudden unexpected death in epilepsy (SUDEP).
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Seizures suppress breathing: peri-ictal central apnoea and aspiration are common, and the resulting hypoxia is a leading mechanism in sudden unexpected death in epilepsy.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune system can ignite seizures: autoimmune encephalitis with anti-NMDA-receptor or LGI1 antibodies causes seizures that respond to immunotherapy rather than to anti-seizure drugs alone.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Treatment touches the gut and liver: valproate can be hepatotoxic, many antiepileptics induce liver enzymes, and the ketogenic diet used for refractory epilepsy works through gut metabolism.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Some drugs stone the kidney: carbonic-anhydrase-inhibiting antiepileptics like topiramate and zonisamide promote kidney stones and a metabolic acidosis.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Anticonvulsants can swell the nodes: phenytoin and aromatic antiepileptics cause hypersensitivity reactions (DRESS) with fever, rash and lymphadenopathy.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — A parasite that sparks seizures: cerebral toxoplasmosis, especially in HIV, and congenital infection produce brain lesions that are a common infectious cause of epilepsy worldwide.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — A leaky barrier feeds seizures: blood-brain-barrier breakdown lets serum proteins like albumin into the cortex, where they activate astrocytes and lower the seizure threshold, a driver of epileptogenesis.
- `connects-to` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Encephalitis leaves an epileptic scar: herpes simplex encephalitis damages the temporal lobe and is a classic cause of acquired, often drug-resistant temporal-lobe epilepsy.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Precision drugs for genetic epilepsy: the mTOR inhibitor everolimus reduces seizures in tuberous sclerosis, and gene-specific therapies are emerging for channelopathies — treating the cause rather than only suppressing seizures.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Cannabidiol became an anticonvulsant: purified cannabidiol (Epidiolex) is approved for Dravet, Lennox-Gastaut and TSC-related epilepsy, derived from the same plant whose heavy THC use causes cannabis use disorder.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Seizures can stop the heart: ictal and post-ictal disturbances of cardiac conduction — bradyarrhythmia and asystole — are implicated in SUDEP, the leading epilepsy-specific cause of death.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — Treating the depression that shadows seizures: depression is the commonest psychiatric comorbidity in epilepsy, and SSRIs like fluoxetine are first-line—the old fear that they meaningfully lower the seizure threshold is largely unfounded.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — Cortical lesions that spark seizures: epilepsy is several-fold more common in multiple sclerosis, where demyelinating plaques reaching the cerebral cortex create irritable, hyperexcitable foci that discharge as seizures.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Lupus that fires the brain: neuropsychiatric SLE can present with seizures, as immune-complex vasculopathy, autoantibodies and inflammation lower the cortical seizure threshold—epilepsy as a manifestation of systemic autoimmunity.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Seizures that aren't epileptic: psychogenic non-epileptic seizures, often rooted in trauma and PTSD, closely mimic epileptic events and frequently coexist with epilepsy, making video-EEG essential to tell them apart.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Shared central hyperexcitability: epilepsy and fibromyalgia both reflect a hyperexcitable nervous system with disturbed glutamate/GABA balance, and the gabapentinoids pregabalin and gabapentin treat both.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Antiepileptic bone disease: enzyme-inducing antiseizure drugs accelerate vitamin D catabolism, lowering cortical-bone density and raising fracture risk with long-term use—compounded by seizure-related falls.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Seizures with infection: COVID-19 causes acute symptomatic seizures through encephalopathy, hypoxia and inflammation, and new-onset epilepsy has been reported after infection.
- `connects-to` → **[SCLC](../sclc/README.md)** — Paraneoplastic seizures: small-cell lung cancer triggers seizures through brain metastases and anti-Hu paraneoplastic limbic encephalitis, an oncological cause of new-onset epilepsy in smokers.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Paroxysmal-event mimics: cataplexy and sleep attacks of narcolepsy can be mistaken for seizures, making it part of the differential of episodic neurological events alongside epilepsy.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Pro-seizure cytokine: IL-1β released by activated glia lowers seizure threshold and promotes epileptogenesis, a central mediator of the neuroinflammation that sustains chronic epilepsy.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory excitability: TNF-α modulates glutamate and GABA receptor trafficking to enhance neuronal excitability, linking brain inflammation to seizure generation.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Cholinergic seizures: excess cholinergic activity, as in organophosphate poisoning or autosomal-dominant nocturnal frontal-lobe epilepsy, can trigger seizures and status epilepticus.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Neuroinflammatory recruitment: CCL2 released after seizures recruits monocytes and helps breach the blood-brain barrier, part of the neuroinflammation that lowers seizure threshold and drives epileptogenesis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Barrier breakdown: VEGF surges after seizures, opening the blood-brain barrier and driving aberrant angiogenesis, a vascular contribution to the epileptogenic remodelling of the brain.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Stress and seizures: CRH is a proconvulsant neuropeptide in the developing brain, part of why stress lowers seizure threshold and underlies the early-life seizures of conditions like infantile spasms.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — HMGB1 released by injured neurons signals through TLR4 to lower seizure threshold and promote epileptogenesis, a neuroinflammatory pathway under active study as an anti-epileptogenic drug target distinct from symptomatic seizure suppression.
- `connects-to` → **[NTRK / TrkB](../../03-molecular/ntrk/README.md)** — BDNF signaling through TrkB drives the aberrant synaptic sprouting and network remodeling that convert a normal brain into an epileptic one, making TrkB a target to prevent epilepsy from developing after brain injury.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen lowers the seizure threshold, the counterpart to progesterone's protective effect, underlying the catamenial pattern in which seizures cluster around the high-estrogen phases of the menstrual cycle.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — T-type voltage-gated calcium channels generate the thalamocortical rhythms of absence seizures—the target of ethosuximide—and other calcium-channel mutations cause genetic epilepsies, making calcium currents a second ionic axis beyond sodium.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin raises the seizure threshold and is the mechanism of fenfluramine, now a key drug for Dravet and Lennox-Gastaut syndromes, while serotonergic brainstem dysfunction is implicated in sudden unexpected death in epilepsy (SUDEP).
- `connects-to` → **[ACTH](../../03-molecular/acth/README.md)** — ACTH (corticotropin) is a first-line treatment for infantile spasms (West syndrome), uniquely effective at stopping the epileptic encephalopathy through mechanisms beyond its glucocorticoid induction.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — The PI3K-AKT-mTOR pathway (mTOR already mapped) is hyperactivated in the mTORopathies—tuberous sclerosis and focal cortical dysplasia (already mapped)—that cause drug-resistant focal epilepsy.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Astrocytic connexin-43 gap junctions synchronize neuronal networks and buffer extracellular potassium and glutamate, and their dysregulation contributes to seizure generation and spread in epilepsy.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Prolonged seizures and status epilepticus trigger caspase-3-mediated neuronal apoptosis, the excitotoxic cell death contributing to the hippocampal sclerosis and progression of epilepsy.
- `connects-to` → **[Prostaglandins (Eicosanoids)](../../03-molecular/prostaglandins/README.md)** — Seizures induce COX-2 and prostaglandin synthesis in the brain, amplifying neuroinflammation and blood-brain-barrier breakdown that lower seizure threshold and drive epileptogenesis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — The TLR4-MyD88-NF-κB axis, activated by HMGB1 and other damage signals released during seizures, sustains the neuroinflammatory loop that promotes hyperexcitability and recurrent seizures.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Seizures generate oxidative stress that NRF2-driven antioxidant defenses counter, and NRF2 activation is neuroprotective against the mitochondrial injury and neuronal loss of chronic epilepsy.
- `connects-to` → **[TSC1-TSC2](../../03-molecular/tsc1-tsc2/README.md)** — Loss of TSC1-TSC2 control of mTOR (mTOR mapped) causes the cortical malformations and mTORopathy epilepsies such as tuberous sclerosis.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN regulation of the PI3K-AKT-mTOR axis (AKT and mTOR mapped) underlies the malformations of cortical development that cause refractory epilepsy.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling is activated during epileptogenesis, contributing to the neuronal hyperexcitability and network reorganization of chronic epilepsy.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by activated microglia amplifies the neuroinflammation that contributes to epileptogenesis and seizure progression.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — JAK-STAT3 signaling drives the reactive astrogliosis that remodels neural networks during the development of chronic epilepsy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA released by neuronal injury can engage cGAS-STING, contributing to the neuroinflammation that promotes epileptogenesis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of the PTEN-PI3K-AKT-mTOR axis (PTEN, AKT, mTOR, and TSC1-TSC2 already mapped) regulates neuronal excitability and the structural plasticity implicated in epileptogenesis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 neuroinflammatory signaling contributes to the glial activation and seizure susceptibility of epilepsy.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α responses to seizure-induced metabolic and hypoxic stress shape the neurovascular remodeling and epileptogenesis of epilepsy.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the neuronal excitability, survival signaling, and mTOR crosstalk (mTOR already mapped) relevant to epileptogenesis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-mTOR metabolic signaling regulates the neuronal energetics and mTORopathy-driven cortical hyperexcitability of epilepsy.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the neuroinflammatory activation that lowers the seizure threshold in epilepsy.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT-mTOR signaling (AKT and mTOR already mapped; PTEN and TSC already mapped) drives the mTOR-pathway (mTORopathy) focal epilepsies.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal homeostasis and mTOR-linked mechanisms implicated in epilepsy.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic reprogramming during epileptogenesis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the NMDA-receptor and synaptic-plasticity mechanisms of the hyperexcitability of epilepsy.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation that promotes epileptogenesis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroinflammation and blood-brain-barrier dysfunction of epilepsy.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the glial and neuroinflammatory responses of epilepsy.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation of epilepsy.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the microglial synaptic remodeling and neuroinflammation of epilepsy.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Synaptic zinc: zinc is co-released with glutamate at hippocampal mossy-fibre synapses and modulates GABA-A and NMDA receptors, so disturbances of synaptic zinc alter seizure susceptibility in temporal lobe epilepsy.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Chronobiology: seizures often cluster with circadian and sleep-wake patterns, and melatonin, which regulates sleep and shows anticonvulsant properties, is used adjunctively in some epilepsy syndromes.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Seizure signalling: nitric oxide has a dual, context-dependent role in seizure generation and termination through its modulation of the glutamatergic and GABAergic transmission already mapped.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Noradrenergic seizure threshold: the noradrenergic system raises the seizure threshold, and vagus-nerve stimulation exerts part of its anticonvulsant effect through norepinephrine, complementing the serotonergic modulation (already mapped) of seizure control.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histaminergic modulation: central histamine raises the seizure threshold, which is why H1-antihistamines that cross into the brain can lower it, implicating the histaminergic system in seizure susceptibility.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic seizures: hypoglycaemia from excess insulin provokes seizures, and the metabolic fuel switch underlies the ketogenic diet's efficacy, linking glucose and insulin handling to seizure control in epilepsy.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative epileptogenesis: seizures and the underlying injury generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative stress (NRF2 already mapped) promotes the epileptogenesis and neuronal damage of recurrent seizures.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Neuroinflammatory balance: the anti-inflammatory IL-10 opposes the pro-inflammatory cytokines (IL-1, TNF and IL-6 already mapped) of the neuroinflammation that promotes epileptogenesis, part of the immune dimension of epilepsy.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopaminergic threshold: dopamine modulates the seizure threshold, with D1 receptors tending to be proconvulsant and D2 anticonvulsant (serotonin and norepinephrine already mapped), part of the neuromodulatory control of seizure susceptibility.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroinflammatory balance: the anti-inflammatory IL-4 counters the pro-inflammatory cytokines (IL-1, TNF and IL-6 already mapped) of the neuroinflammation that promotes epileptogenesis (IL-10 already mapped), part of the immune dimension of epilepsy.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic seizure threshold: leptin has anticonvulsant effects and links the energy state to neuronal excitability, part of the metabolic regulation of the seizure threshold exploited by the ketogenic diet used in refractory epilepsy.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Dietary anticonvulsants: the omega-3 fatty acids have anticonvulsant properties and, with the ketogenic diet, form part of the dietary approaches to epilepsy that modulate neuronal excitability and neuroinflammation (prostaglandins already mapped).
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Neuroinflammation balance: IL-13, with IL-4 (already mapped), supports the M2 microglial anti-inflammatory arm that balances the neuroinflammation (TNF, IL-6 and IL-1 already mapped) which lowers the seizure threshold in epilepsy.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic seizure threshold: adiponectin, with leptin (already mapped), has neuroprotective and anticonvulsant effects, part of the metabolic regulation of the seizure threshold exploited by the ketogenic diet.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Incretin neuroprotection: GLP-1 and its receptor agonists have neuroprotective and possible anticonvulsant effects, linking the metabolic state (insulin already mapped) to the seizure threshold in epilepsy.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Neuroinflammatory epileptogenesis: the microglial activation and the neuroinflammation (IL-1, TNF and IL-6 already mapped) drive the epileptogenesis and are a target of the anti-inflammatory antiseizure approaches.
- `connects-to` → **[Autism spectrum disorder](../autism-spectrum-disorder/README.md)** — ASD comorbidity: epilepsy and autism spectrum disorder are highly comorbid, sharing the mTOR, channel and excitatory/inhibitory (glutamate and GABA already mapped) mechanisms.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — NMDA and eclampsia: magnesium blocks the NMDA/glutamate (already mapped) receptor and is the treatment of the eclamptic seizures; the hypomagnesaemia lowers the seizure threshold.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, contributes to the neuroinflammation (IL-1 and IL-6 already mapped) that lowers the seizure threshold and drives the epileptogenesis.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune contribution to the epileptogenesis of epilepsy.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the metabolic-inflammatory dimension linked to epilepsy.

[^fisher-2017-ilae-classification]: Fisher RS, Cross JH, D'Souza C, et al. Instruction manual for the ILAE 2017 operational classification of seizure types. *Epilepsia.* 2017;58(4):531-542. [doi:10.1111/epi.13671](https://doi.org/10.1111/epi.13671) · [PubMed 28276060](https://pubmed.ncbi.nlm.nih.gov/28276060/)
[^devinsky-2018-epilepsy-review]: Devinsky O, Vezzani A, O'Brien TJ, et al. Epilepsy. *Nat Rev Dis Primers.* 2018;4:18024. [doi:10.1038/nrdp.2018.24](https://doi.org/10.1038/nrdp.2018.24) · [PubMed 29722352](https://pubmed.ncbi.nlm.nih.gov/29722352/)
[^engel-2012-mtle-surgery]: Engel J Jr, McDermott MP, Wiebe S, et al. Early surgical therapy for drug-resistant temporal lobe epilepsy: a randomized trial. *JAMA.* 2012;307(9):922-930. [doi:10.1001/jama.2012.220](https://doi.org/10.1001/jama.2012.220) · [PubMed 22396514](https://pubmed.ncbi.nlm.nih.gov/22396514/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
