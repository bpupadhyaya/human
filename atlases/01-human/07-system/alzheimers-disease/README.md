---
schema: human-scale-entry/v1
id: alzheimers-disease
name: Alzheimer's Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Neurodegenerative disease defined by amyloid-β plaques and tau tangles; progressive memory loss and dementia. APOE4 is the major genetic risk factor. Anti-amyloid antibodies (lecanemab, donanemab) slow early-stage progression; symptomatic treatment with cholinesterase inhibitors."
aliases: ["AD", "Alzheimer disease", "senile dementia", "LOAD", "late-onset Alzheimer's"]
sources:
  - id: selkoe-2016-alzheimer
    type: peer-reviewed
    cite: "Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer's disease at 25 years. EMBO Mol Med. 2016;8(6):595-608."
    doi: "10.15252/emmm.201606210"
    pmid: "27025652"
    url: "https://doi.org/10.15252/emmm.201606210"
  - id: jack-2018-nia-aa
    type: peer-reviewed
    cite: "Jack CR Jr, Bennett DA, Blennow K, et al. NIA-AA Research Framework: Toward a biological definition of Alzheimer's disease. Alzheimers Dement. 2018;14(4):535-562."
    doi: "10.1016/j.jalz.2018.02.018"
    pmid: "29653606"
    url: "https://doi.org/10.1016/j.jalz.2018.02.018"
  - id: van-dyck-2023-lecanemab
    type: peer-reviewed
    cite: "van Dyck CH, Swanson CJ, Aisen P, et al. Lecanemab in Early Alzheimer's Disease. N Engl J Med. 2023;388(1):9-21."
    doi: "10.1056/NEJMoa2212948"
    pmid: "36449413"
    url: "https://doi.org/10.1056/NEJMoa2212948"
cross_links:
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Alzheimer's atrophies hippocampus and entorhinal cortex first (tau Braak staging I-IV), spreading to association cortex; Aβ plaques and tau tangles disrupt synaptic transmission, activate microglia, and drive progressive neuronal death from medial temporal outward."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Disease-associated microglia (DAM) upregulate TREM2 and ApoE → phagocytose Aβ plaques; sustained activation → NLRP3 inflammasome → IL-1β/IL-18 → neuroinflammation and tau spread; TREM2 R47H variant is a major AD risk factor with 2-3× elevated risk."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Aβ fibrils activate NLRP3 inflammasome in microglia → caspase-1 → IL-1β and pyroptosis → neuroinflammation and tau phosphorylation; NLRP3 inhibition (MCC950) reduces tau pathology and cognitive decline in AD mouse models."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy clears APP fragments and aggregated tau; autophagic flux declines in aging and AD; rapamycin-induced autophagy reduces plaques and tangles in mouse models; lysosomal dysfunction (impaired v-ATPase, cathepsins) is a primary AD pathomechanism."
  - target: 01-human/03-molecular/apoe
    relation: connects-to
    note: "APOE4 (frequency ~15%) confers 3-4x heterozygous and 8-12x homozygous risk for late-onset AD; APOE4 impairs microglial Aβ phagocytosis, promotes Aβ aggregation, and worsens tau pathology; APOE4 homozygotes develop AD ~10 years earlier than APOE3 carriers."
  - target: 01-human/03-molecular/app
    relation: connects-to
    note: "APP FAD mutations (V717I, Swedish K670N/M671L) and trisomy 21 increase Aβ42 via β/γ-secretase cleavage; Aβ42 oligomers are synaptotoxic and seed amyloid plaques; lecanemab (anti-Aβ protofibrils) slows cognitive decline 27% in MCI and mild AD."
  - target: 01-human/03-molecular/mapt
    relation: connects-to
    note: "Tau hyperphosphorylation at Thr181, Ser202/Thr205, Ser396 → PHF → NFT formation; Braak staging I–VI tracks NFT spread from entorhinal cortex to isocortex and correlates with cognitive decline; tau-PET (flortaucipir) predicts cognitive trajectory and guides clinical staging in AD."
  - target: 01-human/07-system/lewy-body-dementia
    relation: connects-to
    note: "DLB is commonly mistaken for AD; 50-70% of DLB cases have concurrent Aβ plaque and tau co-pathology; both share APOE4 risk; neuroleptic sensitivity in DLB is fatal (~50%) while not a concern in AD; occipital FDG-PET hypometabolism and DAT-SPECT distinguish DLB from AD."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β hyperactivation in AD hippocampus phosphorylates tau at PHF-1 (Ser396/404) and Thr231 → neurofibrillary tangles; promotes amyloid-β via APP processing; insulin resistance activates GSK-3β; tideglusib (GSK-3β inhibitor) failed Phase 2 AD trials in 2013."
  - target: 01-human/03-molecular/snca
    relation: connects-to
    note: "Alpha-synuclein (SNCA) and amyloid-β co-aggregate in DLB, an AD/PD overlap syndrome; SNCA Lewy pathology accelerates tau spreading via prion-like mechanisms; ~10-15% of AD patients have concurrent Lewy body pathology; alpha-synuclein SAA distinguishes DLB from AD."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin production declines in Alzheimer disease due to SCN atrophy; disrupted circadian rhythm → sundowning (late-day agitation); exogenous melatonin (0.5-6 mg bedtime) modestly improves AD sleep; melatonin is antioxidant and reduces Aβ aggregation in preclinical models."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Impaired brain insulin signalling (\"type 3 diabetes\") is implicated in AD: INSR hyposensitivity → reduced Akt → ↑GSK-3β → tau hyperphosphorylation; intranasal insulin improves memory in MCI/AD Phase 2 trials; T2DM doubles AD risk; GLP-1 agonists are under Phase 3 investigation."
  - target: 01-human/03-molecular/tdp-43
    relation: connects-to
    note: "LATE (limbic-predominant age-related TDP-43 encephalopathy) affects ~20% of octogenarians and mimics AD clinically; TDP-43 co-pathology in ~57% of AD brains worsens cognitive trajectory; nuclear loss → TDPBP cryptic exon inclusion in hippocampal neurons."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "GLP-1R activation reduces amyloid-β, tau phosphorylation, and neuroinflammation in preclinical AD models; semaglutide EVOKE Phase 3 trial targets early AD; GLP-1R agonists may address brain insulin resistance via Akt → reduced GSK-3β → less tau hyperphosphorylation."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Age-related IGF-1 decline contributes to AD risk: low IGF-1 impairs hippocampal neurogenesis and synaptic plasticity; INSR/IGF-1R resistance in AD neurons → reduced Akt → ↑GSK-3β → tau phosphorylation; IGF-1 restores cognition in preclinical AD models and reduces Aβ plaque load."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Alzheimer's and Parkinson's are the two commonest neurodegenerative diseases that overlap in pathology: both involve misfolded-protein aggregation (amyloid/tau vs α-synuclein) and can co-occur, with Lewy bodies in many Alzheimer brains—a proteinopathy spectrum."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Alzheimer's disease is ultimately the death of neurons and their synapses: amyloid plaques and tau tangles disrupt synaptic function and trigger neuronal loss, especially of cholinergic and hippocampal neurons—and synapse loss correlates best with the dementia."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Alzheimer's disease is sometimes called 'type 3 diabetes' for its link to insulin resistance: impaired brain insulin signaling promotes amyloid and tau pathology, and type 2 diabetes raises Alzheimer's risk—why GLP-1 drugs are being tested against dementia."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Alzheimer's classically depletes acetylcholine: early loss of basal-forebrain cholinergic neurons impairs memory, and the only long-standing symptomatic drugs—cholinesterase inhibitors—work by preserving this neurotransmitter, though they do not slow the disease."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus is where Alzheimer's begins: tau tangles and atrophy strike this memory-forming structure first, explaining the early loss of recent memory, and hippocampal shrinkage on MRI is among the earliest imaging signs of the disease."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes shape Alzheimer's neuroinflammation: reactive astrocytes cluster around amyloid plaques, and while they can help clear amyloid, their chronic activation alongside microglia releases inflammatory mediators that damage neurons and synapses."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement drives synapse loss in Alzheimer's: C3 and C1q tag vulnerable synapses, prompting microglia to prune them, so reactivating this developmental 'eat-me' signal helps explain the early synaptic loss that best correlates with memory decline."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Vascular disease and Alzheimer's intertwine: atherosclerosis and small-vessel disease reduce brain perfusion and clearance of amyloid, so most late-life dementia is 'mixed', and controlling blood pressure, cholesterol, and diabetes lowers dementia risk."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression and Alzheimer's are tangled: late-life depression can be an early prodrome of dementia and is also an independent risk factor, while AD itself often presents with apathy and low mood—so new depression in an older adult warrants cognitive assessment."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Alzheimer's overexcites neurons through glutamate: amyloid and tau disrupt glutamate clearance, causing excitotoxic overstimulation of NMDA receptors that damages synapses—the rationale for memantine, which dampens this glutamate signaling."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Alzheimer's recruits cytotoxic T cells into the brain: CD8 T cells accumulate around plaques and tau pathology, and this adaptive-immune infiltration is increasingly seen as an active contributor to neurodegeneration, not a bystander."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Metal ions like zinc shape Alzheimer's amyloid: zinc and copper bind amyloid-beta, promoting its aggregation and generating oxidative stress, so disturbed brain metal balance is one hypothesis for how plaques form and injure neurons."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron builds up in the Alzheimer's brain: amyloid plaques and degenerating neurons accumulate iron that drives oxidative stress and ferroptosis, so disordered iron handling adds to the metal-linked injury alongside zinc and copper."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Alzheimer's also frays the brain's wiring insulation: oligodendrocytes and their myelin degenerate early, and amyloid and tau pathology disrupt these cells, so white-matter breakdown contributes to cognitive decline beyond neuron loss."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Alzheimer's brains run low on BDNF: this neurotrophin that sustains synapses and hippocampal plasticity falls in the disease, so reduced BDNF support helps explain the synaptic loss and failing memory."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Alzheimer's is, at heart, a loss of synapses: their disappearance tracks cognitive decline more closely than plaques or tangles do, as amyloid and tau poison synaptic function long before neurons die."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Alzheimer's deranges neuronal calcium: amyloid forms calcium-permeable pores and overexcited circuits let calcium flood in, driving the excitotoxic damage that the NMDA blocker memantine is meant to soften."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Alzheimer's may be visible in the eye: amyloid deposits and retinal nerve thinning appear in the retina, an outgrowth of the brain, making eye imaging a promising window for early, noninvasive detection."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Alzheimer's is now imaged in life: amyloid and tau PET scans use radioactive photons to reveal the plaques and tangles directly, while MRI tracks the shrinking hippocampus over time."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "What's good for the heart is good for the brain: midlife hypertension, atherosclerosis and heart disease raise Alzheimer's risk, tying cardiovascular health to the odds of dementia."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Metals gather in Alzheimer's plaques: copper, with zinc and iron, binds amyloid-beta and can drive the oxidative damage of the disease, which is why metal-chelation has been explored as therapy."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows Alzheimer's two lesions: extracellular plaques of beta-pleated amyloid fibrils and intracellular tangles of paired helical tau filaments, choking neurons as their synapses melt away."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut may whisper to the Alzheimer's brain: a dysbiotic microbiome and the inflammatory and amyloid-like products it makes are increasingly tied, through the gut-brain axis, to the neuroinflammation that fuels the disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium thins in the aging brain: low levels weaken the synaptic plasticity and NMDA regulation that memory depends on, and raising brain magnesium is studied as a way to slow cognitive decline."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Alzheimer's first disease-modifying drugs are antibodies: lecanemab and donanemab are monoclonal antibodies that clear amyloid plaques, modestly slowing decline at the cost of ARIA — brain swelling and microbleeds seen on MRI."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Amyloid also clogs the brain's vessels: in cerebral amyloid angiopathy it deposits in the walls lined by endothelial cells, weakening them into microbleeds — the same fragile vessels that bleed when anti-amyloid antibodies are given."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Sleep and Alzheimer's feed each other through orexin: the wakefulness peptide runs high and fragments sleep, and because amyloid is cleared by the glymphatic system during deep sleep, the lost rest lets more plaque accumulate."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The brain has lymphatics, and they fail in Alzheimer's: meningeal lymphatics and the glymphatic flow drain amyloid from the brain, and their decline with age and disease lets the plaque-forming peptide build up unchecked."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Cholesterol handling shapes the risk: the APOE4 lipid-transport variant is the strongest common genetic risk factor, and disturbed brain cholesterol metabolism influences how amyloid is made and cleared."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid hides a reversible mimic: hypothyroidism causes a slowed, forgetful state that imitates dementia, so thyroid function is checked in every cognitive workup to catch a treatable cause before settling on Alzheimer's."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep is when the brain washes out amyloid: deep sleep drives the glymphatic clearance of amyloid-beta, so chronic insomnia lets it accumulate — and the disease in turn wrecks sleep, a vicious loop that may start years before memory fails."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "A gut-brain axis feeds the plaques: dysbiosis and bacterial products (LPS, microbial amyloids) can prime systemic and brain inflammation, and altered microbiomes are now linked to amyloid burden and cognitive decline in Alzheimer's."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation accelerates the decline: IL-6 from activated microglia and the body's chronic low-grade inflammation correlates with faster cognitive loss, part of the neuroinflammatory arm now seen as a driver, not just a bystander, in Alzheimer's."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement marks synapses for deletion: the cascade through C3 to C5 tags synapses that microglia then prune, an over-activation that drives the early synapse loss best correlating with cognitive decline in Alzheimer's."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Midlife blood pressure shapes late dementia: hypertension damages the small cerebral vessels and the clearance of amyloid, making it one of the strongest modifiable risk factors for Alzheimer's decades later."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate lymphocytes invade the aging brain: natural killer cells accumulate in the Alzheimer's brain and, by attacking neural cells and stoking inflammation, are emerging as contributors to the neurodegeneration."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Microglia inflame the plaques through NF-κB: amyloid-β activates NF-κB in microglia, priming the NLRP3 inflammasome and pouring out cytokines that amplify the neuroinflammation accelerating Alzheimer's."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The end stage opens the door to fatal infection: advanced Alzheimer's brings dysphagia, immobility and aspiration, so pneumonia and the sepsis it triggers are a leading cause of death in dementia."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Late-stage immobility clots the veins: as Alzheimer's confines patients to bed, venous stasis raises the risk of deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "The diseased cortex becomes hyperexcitable: Alzheimer's substantially raises seizure risk — strikingly so in early-onset disease — as amyloid and tau pathology disrupt networks into epileptiform and overt seizures."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Vascular and amyloid injury overlap: cerebral amyloid angiopathy weakens vessels toward hemorrhage while shared vascular risk factors drive ischemic stroke, and stroke and Alzheimer's pathology together produce mixed dementia."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Frail bones meet frequent falls: immobility, low vitamin D and the falls of impaired gait and cognition make osteoporotic hip fractures common and devastating in advanced Alzheimer's."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Late dementia lets food reach the lungs: progressive dysphagia in advanced Alzheimer's causes aspiration, and the resulting pneumonia — often pneumococcal — is the leading immediate cause of death."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Bedbound immobility breaks down the skin: in end-stage Alzheimer's, immobility and incontinence predispose to pressure ulcers over bony prominences that heal poorly in the frail, malnourished patient."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Confusion breeds chronic worry: anxiety and agitation are common neuropsychiatric features of Alzheimer's, fueled by the disorientation and memory loss of failing cognition."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is the archetypal neurodegeneration: Alzheimer's destroys cortical and hippocampal neurons through amyloid plaques and tau tangles, the leading neurodegenerative disease of the nervous system."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Late disease robs the body of movement: advancing Alzheimer's brings gait disturbance and falls with fractures, and end-stage immobility leaves contractures and profound sarcopenia."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Eventually it takes away swallowing: advanced Alzheimer's causes dysphagia with aspiration and progressive weight loss, raising the difficult questions around assisted and tube feeding."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Aspiration pneumonia ends it: dysphagia in end-stage Alzheimer's lets food and saliva enter the lungs, making aspiration pneumonia the most common immediate cause of death."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Innate immunity shapes the plaques: microglial neuroinflammation and risk genes like TREM2 drive amyloid clearance and damage, making the brain's immune response a central target of new therapies."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Amyloid also lines the vessels: cerebral amyloid angiopathy deposits beta-amyloid in cortical artery walls, causing lobar haemorrhages, while vascular disease adds to mixed dementia."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Brain insulin resistance earns it a nickname: impaired cerebral insulin signalling has led some to call Alzheimer's 'type 3 diabetes', and hypothalamic degeneration disturbs weight, appetite and circadian rhythm."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Oestrogen loss shifts the risk: the fall in oestrogen at menopause is implicated in women's higher Alzheimer's risk, interacting with the APOE genotype."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "End-stage immobility breaks the skin: in advanced Alzheimer's, immobility and incontinence make pressure ulcers a major preventable complication of care."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The failing kidney ages the brain: chronic kidney disease is an independent risk factor for Alzheimer's, through shared vascular damage and the accumulation of uraemic toxins that impair cognition."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "A virus implicated in its origin: herpes simplex type 1 reactivation in the brain is a long-standing hypothesis in Alzheimer's, with amyloid-beta itself acting as an antimicrobial peptide that traps the virus."
  - target: 03-medicine/02-traditional/ginkgo-biloba
    relation: connects-to
    note: "A traditional remedy long tried: Ginkgo biloba extract has been widely used and studied for dementia and Alzheimer's, though large trials show little benefit in prevention or treatment."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Anti-amyloid antibodies modify it: lecanemab and donanemab, monoclonal antibodies that clear amyloid-beta plaques, are the first disease-modifying Alzheimer's drugs, modestly slowing decline at the cost of brain-swelling and microhaemorrhage (ARIA)."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Tau wrecks the axon's railway: hyperphosphorylated tau detaches from microtubules and forms neurofibrillary tangles, collapsing the axonal transport that supplies synapses — a core mechanism of neurodegeneration in Alzheimer's."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Amyloid lines the cerebral vessels: in cerebral amyloid angiopathy, amyloid-beta deposits in the arterial wall of cortical vessels, weakening them and causing the lobar haemorrhages and microbleeds common in Alzheimer's."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "Overlapping proteinopathies: TDP-43 aggregates that define ALS-frontotemporal disease also appear in limbic-predominant age-related TDP-43 encephalopathy and many Alzheimer's brains, blurring the boundary between the neurodegenerations."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "Two faces of neurodegeneration: Alzheimer's is a sporadic amyloid-and-tau dementia of late life, while Huntington's is a monogenic CAG-repeat disease striking midlife—different drivers converging on protein aggregation and neuronal loss."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Complement-driven synapse loss in both: Alzheimer's and schizophrenia share microglial, complement-mediated pruning of synapses and neuroinflammation, and late-life psychosis blurs into Alzheimer's despite their different ages of onset."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Midlife adiposity and dementia: midlife obesity raises the later risk of Alzheimer's through insulin resistance, vascular injury and chronic neuroinflammation, tying metabolic health to brain ageing."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Infection and cognitive decline: COVID-19 can leave lasting 'brain fog' and accelerate cognitive decline in older adults, with neuroinflammation a proposed link to Alzheimer's pathology."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The peripheral amyloid sink: the liver clears circulating amyloid-beta via LRP1, and impaired hepatic clearance may raise the brain's amyloid burden—linking systemic metabolism to Alzheimer's."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Trauma and later dementia: chronic PTSD and the sustained cortisol of traumatic stress damage the hippocampus and are associated with a substantially raised risk of later Alzheimer's disease."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Orexin, sleep and amyloid: orexin governs the sleep-wake cycle that drives glymphatic amyloid clearance, tying the orexin system disrupted in narcolepsy to the sleep disturbance and amyloid accumulation of Alzheimer's."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Mood disorder and dementia risk: bipolar disorder is associated with a higher risk of later dementia, while long-term lithium appears neuroprotective—through GSK-3β inhibition—and lowers Alzheimer's incidence."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Neuroinflammation: TNF-α released by activated microglia around amyloid plaques amplifies the chronic inflammation that accelerates synaptic loss and neurodegeneration in Alzheimer's."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Microglial driver: IL-1β from plaque-associated microglia is a central inflammatory mediator in Alzheimer's, promoting tau phosphorylation and the neurotoxic glial response."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Vascular hypoxia: cerebral hypoperfusion in Alzheimer's stabilises HIF-1α, linking the vascular contribution to dementia with amyloid processing and neuronal stress responses."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA-sensing neuroinflammation: leaked mitochondrial DNA activates the cGAS-STING pathway in microglia and neurons in Alzheimer's, an emerging driver of the type-I-interferon response and tau pathology."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 produced in the Alzheimer's brain recruits peripheral monocytes and activates microglia around plaques, amplifying the neuroinflammation linked to cognitive decline."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Impaired clearance: overactive mTOR suppresses the autophagy needed to clear amyloid-β and tau aggregates, and its inhibition (rapamycin) is neuroprotective in Alzheimer's models."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Microglial amyloid sensing: aggregated amyloid-β engages microglial TLR4, triggering the NF-κB-driven neuroinflammatory cytokine response that contributes to the synaptic and neuronal injury of Alzheimer's disease."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Neuronal death and tau cleavage: caspase-3 executes the neuronal apoptosis of Alzheimer's and cleaves tau into aggregation-prone fragments, coupling cell death directly to the spread of tau pathology."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Vascular contribution: dysregulated VEGF and cerebral amyloid angiopathy impair the neurovascular unit in Alzheimer's, the vascular arm that worsens amyloid clearance and accelerates cognitive decline."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Amyloid influx: RAGE transports circulating amyloid-β across the blood-brain barrier into the brain, the influx counterpart to LRP1-mediated efflux, so RAGE upregulation tips the balance toward the amyloid accumulation of Alzheimer's."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial driver: galectin-3 released by activated microglia around amyloid plaques amplifies the neuroinflammatory response, a microglial signal increasingly seen as a driver of Alzheimer's neurodegeneration and a candidate therapeutic target."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Locus-coeruleus origin: the noradrenergic locus coeruleus is one of the earliest sites of tau pathology in Alzheimer's, and its degeneration depletes norepinephrine, removing a neuroprotective, anti-inflammatory signal and contributing to early cognitive symptoms."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Brain insulin resistance: impaired AKT signalling from brain insulin resistance disinhibits GSK3β (already mapped) to hyperphosphorylate tau, the 'type-3 diabetes' link between the insulin already mapped and Alzheimer neurodegeneration."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative defence: oxidative stress is central to Alzheimer's, and a declining NRF2 antioxidant response permits the lipid peroxidation and mitochondrial damage that injure neurons."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcium-driven synapse loss: dysregulated calcium-calcineurin signalling in Alzheimer's drives dendritic-spine retraction, synapse loss and astrocyte activation that track closely with cognitive decline."
  - target: 01-human/03-molecular/aquaporin-4
    relation: connects-to
    note: "Glymphatic clearance: astrocytic aquaporin-4 drives the glymphatic flow that clears amyloid-β during sleep, and the loss of AQP4 polarisation impairs Aβ removal in Alzheimer's disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Tau phosphorylation: MAPK-ERK, alongside GSK-3β (mapped), hyperphosphorylates tau (MAPT mapped) into the paired helical filaments that form the neurofibrillary tangles of Alzheimer's."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microglial neuroinflammation: microglial TLR4 (mapped) sensing of amyloid-β signals through MyD88 to NF-κB (mapped), driving the neuroinflammation that propagates Alzheimer's pathology."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-driven JAK-STAT signalling sustains the reactive astrogliosis and microglial activation (IL-6 mapped) that amplify Alzheimer's neuroinflammation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 activation drives the reactive-astrocyte transcriptional program around amyloid plaques, contributing to neuroinflammation in Alzheimer's disease."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN regulation of the PI3K-AKT-GSK-3β axis (AKT, mTOR and GSK-3β mapped) links insulin/IGF resistance to tau phosphorylation and neuronal vulnerability in Alzheimer's disease."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling drives the disease-associated microglial interferon response increasingly implicated in the neuroinflammation of Alzheimer's disease."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "BDNF-TrkB (NTRK) signalling (BDNF already mapped) supports the synaptic maintenance and neuronal survival whose loss accelerates degeneration in Alzheimer's disease."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the neuroprotective-versus-inflammatory balance of glia and the cerebrovascular responses relevant to Alzheimer's disease."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate neuronal autophagy and oxidative-stress defense, programs that fail in the neurodegeneration of Alzheimer's disease."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation associated with amyloid pathology in Alzheimer's disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic T-cell activity in the infiltrated brain contributes to the adaptive-immune component of neurodegeneration in Alzheimer's disease."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the neuronal insulin/IGF survival pathways whose impairment contributes to Alzheimer's disease."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, coupled to autophagy (autophagy already mapped), regulates the clearance of amyloid and tau aggregates in Alzheimer's disease."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Aberrant CDK-driven cell-cycle re-entry of postmitotic neurons contributes to the tau hyperphosphorylation and neuronal death of Alzheimer's disease."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation implicated in the late-onset risk of Alzheimer's disease."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (FYN) kinase signaling, activated downstream of amyloid-β via cellular prion protein, mediates the tau-dependent synaptotoxicity of Alzheimer's disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven microglial and monocyte recruitment contributes to the neuroinflammation of Alzheimer's disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the microglial and neural-progenitor responses of the neuroinflammation of Alzheimer's disease."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial amyloid clearance and neuroinflammatory responses of Alzheimer's disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation and blood-brain-barrier dysfunction of Alzheimer's disease."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neuronal and microglial gene programs of Alzheimer's disease."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (A2A receptor) signaling participates in the synaptic dysfunction and neuroinflammation of Alzheimer's disease."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microglial activation and neuroinflammation of Alzheimer's disease."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-amyloid immunotherapy: the first disease-modifying Alzheimer's drugs, lecanemab and donanemab, are IgG monoclonal antibodies that clear amyloid-beta (APP already mapped) from the brain, validating the amyloid target through passive immunisation."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences: women bear a disproportionate share of Alzheimer's disease, and the loss of neuroprotective estrogen at menopause is one proposed contributor to their elevated risk and the faster progression seen after diagnosis."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Microglial neuroinflammation: MHC class II is upregulated on activated microglia in Alzheimer's disease, marking the antigen-presenting, inflammatory microglial state (TREM2-driven) that shapes plaque clearance and neurodegeneration."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Brain renin-angiotensin: a central renin-angiotensin system modulates cerebral blood flow, inflammation and amyloid handling, and antihypertensives blocking angiotensin II are associated with lower dementia risk, a vascular-metabolic target in Alzheimer's disease."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid protection: progesterone and its neurosteroid metabolites are neuroprotective and support myelin, and together with estrogen (already mapped) their postmenopausal loss is proposed to contribute to women's higher Alzheimer's risk."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Cholinergic and histaminergic cognition: histaminergic H3 signalling modulates cognition and was a drug target in Alzheimer's, while the cumulative anticholinergic and antihistamine burden of many drugs is itself associated with higher dementia risk."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative neurotoxicity: reactive oxygen species, to which xanthine oxidase contributes, are central to the amyloid- and tau-driven neurotoxicity of Alzheimer's (NRF2 already mapped), and the oxidative damage compounds the mitochondrial and metal (iron already mapped) injury."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the microglial (already mapped) cyclooxygenase pathway drive the neuroinflammation of Alzheimer's (IL-6, TNF and IL-1 already mapped), and epidemiological studies link NSAID use to lower dementia risk."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonergic degeneration: loss of serotonergic neurons contributes to the depression, agitation and other behavioural symptoms of Alzheimer's (norepinephrine already mapped), and serotonergic drugs are used to manage these neuropsychiatric features."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Microglial polarisation: IL-4 polarises the microglia (already mapped) toward a neuroprotective M2 phenotype, and the balance against the pro-inflammatory activation shapes whether the neuroinflammation of Alzheimer's clears amyloid or damages neurons."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-10 counters the microglial pro-inflammatory cytokines (TNF, IL-6 and IL-1 already mapped) of Alzheimer's, part of the neuroinflammatory balance that shapes the disease."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Omega-3 and brain lipids: the omega-3 fatty acid DHA is a major structural lipid of the brain, and its pro-resolving mediators counter neuroinflammation (prostaglandins already mapped), the basis of dietary interest in omega-3 for cognitive decline."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation (TNF, IL-6 and IL-1 already mapped) of Alzheimer's disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic risk: leptin has neuroprotective and pro-cognitive actions, and leptin resistance with the metabolic dysfunction (insulin already mapped) is linked to the risk of Alzheimer's disease."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine inflammation: resistin, with leptin (already mapped), links the adipose-inflammatory and metabolic (insulin already mapped) state to the neuroinflammation implicated in the risk of Alzheimer's disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Neuroprotective adipokine: adiponectin, with leptin and resistin (already mapped), has neuroprotective actions; the adiponectin resistance and the metabolic (insulin already mapped) dysfunction are linked to Alzheimer's-disease risk."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Amyloid metal binding: copper, with zinc (already mapped), binds the amyloid-β (APP already mapped) and catalyses the oxidative damage, the metal dyshomeostasis of Alzheimer's disease."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type-3 diabetes: the brain insulin (already mapped) resistance links Alzheimer's disease to type 2 diabetes (the shared metabolic and inflammatory pathways), the 'type-3 diabetes' concept."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the cytosolic and mitochondrial DNA, drives the microglial (already mapped) neuroinflammation of Alzheimer's disease."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the adaptive immune contribution to the neuroinflammation of Alzheimer's disease."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of Alzheimer's disease."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune interaction in Alzheimer's disease."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the adaptive-immune contribution to the neuroinflammation of Alzheimer's disease."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the neuroimmune interaction in Alzheimer's disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the blood-brain-barrier dysfunction of Alzheimer's disease."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the microglial (already mapped) activation and the complement-mediated synapse loss of Alzheimer's disease."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Brain iron: transferrin, the iron carrier, is central to the brain-iron accumulation that, with the disordered iron handling, drives the oxidative stress and ferroptosis contributing to the neurodegeneration of Alzheimer's disease."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H, whose variants are Alzheimer's-risk loci, regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-mediated synapse loss of Alzheimer's disease."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway (C1q-initiated) that tags the synapses for the microglial (already mapped) pruning of Alzheimer's disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the meningeal and CNS-border compartments present antigen to the T cells (already mapped) in the neuroinflammation of Alzheimer's disease."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuro-epithelial alarmin: TSLP, released from the inflamed gut-epithelium (gut-microbiome already mapped) and skin (already mapped), activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the systemic immune activation of Alzheimer's disease."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-BBB axis: bradykinin, generated by the contact system activated by complement (C3, C5, C5aR1 already mapped) and amyloid fibrils in Alzheimer's disease, augments blood-brain-barrier permeability and amplifies the microglial (already mapped) neuroinflammation."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective cytokine: erythropoietin, acting via EPOR on neurons (already mapped) and astrocytes (already mapped), promotes neuronal survival and limits the oxidative and neuroinflammatory degeneration of Alzheimer's disease."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM remodelling in neuritic plaques: periostin, expressed by reactive astrocytes (already mapped) and microglia (already mapped) around amyloid deposits, modulates the peri-plaque extracellular matrix and promotes the fibrotic neuroinflammatory remodelling of Alzheimer's disease."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Neuroendocrine-immune coupling: prolactin, acting via PRLR on microglia (already mapped) and astrocytes (already mapped), modulates the neuroinflammatory cytokine (TNF-α and IL-6 already mapped) milieu and may influence the female-predominant prevalence of Alzheimer's disease."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Hippocampal neuroprotection: oxytocin, via oxytocin receptors on hippocampal neurons and microglia (already mapped), suppresses the NF-κB/TNF-α (already mapped) neuroinflammatory cascade and improves the synaptic plasticity impaired by amyloid in Alzheimer's disease."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "AD testosterone: testosterone suppresses NF-κB (already mapped) neuroinflammation and amyloid-β production in neurons (already mapped); androgen deficiency amplifies microglia (already mapped) and complement-C5 (already mapped) neurodegeneration in Alzheimer's."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "AD vasopressin: vasopressin, via V1/V2 receptors on neurons (already mapped), modulates brain (already mapped) fluid and synaptic homeostasis; vasopressin dysregulation amplifies NF-κB (already mapped) and microglia (already mapped) neuroinflammatory damage in Alzheimer's."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "AD selenium: selenium, via GPx/thioredoxin reductase, protects neurons (already mapped) and astrocytes (already mapped) from oxidative injury; selenium deficiency amplifies NF-κB (already mapped) and microglia (already mapped) amyloid-β-driven neurodegeneration in Alzheimer's."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "AD iodine: iodine-dependent thyroid hormones regulate neuronal (neuron already mapped) metabolism and synaptic (synapse already mapped) function; hypothyroidism amplifies NF-κB (already mapped) and NLRP3 inflammasome (already mapped) neuroinflammation and amyloid-β burden."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "AD sodium: sodium dysregulation in the brain (already mapped) drives neuronal (neuron already mapped) excitotoxicity via glutamate (already mapped) receptor overload; sodium imbalance amplifies NF-κB (already mapped) and NLRP3 inflammasome (already mapped) amyloid-β cascade."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "AD potassium: potassium efflux from neurons (already mapped) activates NLRP3 inflammasome (already mapped) in microglia (already mapped); disrupted K⁺ amplifies NF-κB (already mapped) and IL-1β (already mapped) amyloid-β neuroinflammation and hippocampal (already mapped) loss."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "AD phosphorus: phosphorus fuels neuronal (neuron already mapped) and microglia (already mapped) ATP; phosphorus deficiency impairs synaptic transmission and amplifies NLRP3 inflammasome (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) amyloid-β cascade of AD."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "AD nitrogen: nitric oxide (NO, nitrogen-derived) in microglia (already mapped) and neurons (already mapped) amplifies neuroinflammation; NO excess upregulates NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade in AD."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "AD chloride: chloride channels on microglia (already mapped) and neurons (already mapped) regulate intracellular pH; chloride dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade in AD."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "AD sulfur: sulfur-containing glutathione in neurons (already mapped) and microglia (already mapped) scavenges ROS; sulfur deficiency amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) neurodegeneration in AD."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "mitochondrial oxygen sustains ATP in neurons (already mapped) and microglia (already mapped) for amyloid-β clearance; hypoxia amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory amyloid-tau cascade in AD."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "carbon, via bicarbonate in neurons (already mapped) and microglia (already mapped), maintains pH homeostasis; carbon dioxide dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory amyloid-tau cascade in AD."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "hydrogen, via H2O2 and ROS redox balance in neurons (already mapped) and microglia (already mapped), sets oxidative tone; hydrogen excess amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory amyloid-tau cascade in AD."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "AD PD-1: PD-1 on microglia (already mapped) and t-cytotoxic-cell (already mapped) modulates neuroinflammatory homeostasis; PD-1 dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) amyloid-tau neuroinflammatory cascade in AD."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "AD WNT/β-catenin: WNT/β-catenin in neurons (already mapped) and microglia (already mapped) promotes synaptic plasticity and amyloid clearance; WNT dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory amyloid-tau cascade in AD."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "AD RANKL: RANKL from microglia (already mapped) and astrocytes (already mapped) modulates neurovascular and synaptic remodelling; RANKL dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) neuroinflammatory amyloid cascade in AD."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "AD IL-2: IL-2 signalling in regulatory-t-cell (already mapped) and microglia (already mapped) modulates neuroinflammatory homeostasis; IL-2 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) amyloid-tau cascade of AD."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "AD fibronectin: fibronectin in microglia (already mapped) and astrocytes (already mapped) promotes ECM accumulation in AD plaques; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) amyloid-tau neuroinflammatory cascade of AD."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "AD notch: notch signalling in neurons (already mapped) and microglia (already mapped) modulates synaptic plasticity and amyloid processing; notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) cascade of AD."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "AD activin-A: activin-A from microglia (already mapped) and astrocytes (already mapped) modulates neuroinflammatory responses in AD; activin-A excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) amyloid-tau cascade of Alzheimer's disease."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "AD TGF-β: TGF-β in microglia (already mapped) and astrocytes (already mapped) exerts neuroprotective and pro-fibrotic roles; TGF-β dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of Alzheimer's disease."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "AD CGRP: CGRP from trigeminal neurons (already mapped) and microglia (already mapped) modulates cerebrovascular tone in AD; CGRP dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) neurovascular cascade of Alzheimer's disease."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "AD calcitonin: calcitonin from microglia (already mapped) and neurons (already mapped) modulates cerebrovascular calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) amyloid-tau cascade of AD."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "AD substance-p: substance-P from neurons (already mapped) and microglia (already mapped) modulates AD nociceptive signalling; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of AD."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "AD insulin-receptor: insulin receptor on neurons (already mapped) and microglia (already mapped) drives metabolic neuroprotection; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) amyloid-tau cascade of AD."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "AD aldosterone: aldosterone from microglia (already mapped) and astrocytes (already mapped) modulates neuroinflammatory fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) amyloid-tau cascade of AD."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "AD androgen-receptor: androgen receptor on neurons (already mapped) and microglia (already mapped) modulates neuroprotective sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of AD."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "AD adrenomedullin: adrenomedullin from astrocytes (already mapped) and microglia (already mapped) modulates neuroinflammatory vasodilation; adrenomedullin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of AD."
---

# Alzheimer's Disease

## Overview

**Alzheimer's disease (AD)** is the most common cause of dementia — a progressive, ultimately fatal neurodegenerative disorder characterized by the pathological accumulation of **amyloid-β (Aβ) plaques** (extracellular) and **tau neurofibrillary tangles (NFTs)** (intraneuronal) in the cerebral cortex and hippocampus, leading to synaptic dysfunction, neuroinflammation, neuronal death, and cognitive decline [^selkoe-2016-alzheimer].

AD is the **sixth leading cause of death in the United States** (~6.9 million Americans, 2024; ~50 million worldwide) and the most expensive disease in terms of societal cost. Absent prevention or cure, prevalence is projected to triple by 2050 as the global population ages.

**Classification:**
- **Late-onset AD (LOAD, >65 years):** ~95% of cases; complex polygenic with APOE4 as the major risk allele; likely decades of preclinical amyloid accumulation before symptom onset
- **Early-onset AD (EOAD, <65 years):** ~5%; often familial (FAD) with autosomal dominant mutations in APP (amyloid precursor protein), PSEN1 (presenilin-1), or PSEN2 (presenilin-2) → constitutively elevated Aβ42 production

**The amyloid cascade hypothesis** (Hardy and Higgins, 1992; Selkoe and Hardy, 2016): Aβ42 overproduction or underclearing → Aβ aggregation → oligomers (toxic) → plaques (less toxic, more stable) → neuroinflammation → tau hyperphosphorylation and tangle formation → synapse loss → neurodegeneration → dementia [^selkoe-2016-alzheimer]. While this remains the dominant framework, debate continues about relative pathogenic contribution of Aβ vs. tau vs. neuroinflammation.

**Biological definition (NIA-AA A/T/(N) Framework, 2018):** AD defined by biomarkers [^jack-2018-nia-aa]:
- **A (amyloid):** Positive CSF Aβ42, or amyloid PET (florbetapir, florbetaben) — marks amyloid pathology
- **T (tau):** Positive CSF phospho-tau181, or tau PET (flortaucipir) — marks tau pathology
- **(N) (neurodegeneration):** CSF total tau, FDG-PET, brain MRI atrophy — marks neurodegeneration

## Structure

### Amyloid-β: production and aggregation [^selkoe-2016-alzheimer]

**Amyloid precursor protein (APP, 695-770 aa depending on isoform):**
- Type I transmembrane glycoprotein; expressed in neurons, synapses
- **Non-amyloidogenic pathway (normal):** α-secretase (ADAM10/ADAM17) cleaves within Aβ domain → sAPPα (soluble, neuroprotective) + C83 → γ-secretase → p3 peptide (harmless)
- **Amyloidogenic pathway (AD):** β-secretase (BACE1) cleaves APP → sAPPβ + C99 → γ-secretase (PSEN1/PSEN2 complex) → Aβ40 (more common, less pathogenic) and **Aβ42** (minority, more hydrophobic → aggregation-prone → toxic)

**Aβ aggregation cascade:**
1. Aβ42 monomers → soluble oligomers (dimers to ~50-mers) — **most neurotoxic form** (impair LTP, cause synaptic dysfunction)
2. Oligomers → protofibrils → insoluble fibrillar plaques (neuritic/senile plaques) — detectable by PET, less acutely toxic but markers of disease
3. Plaques → activate microglia and astrocytes → neuroinflammation → amplify Aβ production and tau phosphorylation

**Key genetic determinants of Aβ:**
- **APP duplication (Down syndrome/trisomy 21):** 3 copies of APP → 1.5× Aβ production → essentially universal early-onset AD by age 50-60
- **APP mutations (familial AD):** V717I (London), K670N/M671L (Swedish) → elevated Aβ42/40 ratio
- **PSEN1 mutations:** >300 known pathogenic mutations → altered γ-secretase cleavage → elevated Aβ42/40; most aggressive FAD

### Tau pathology

**Tau (MAPT gene):** Microtubule-associated protein; 6 isoforms in adult human brain (3R and 4R); normally stabilizes axonal microtubules and facilitates axonal transport.

**Hyperphosphorylation in AD:**
- Aβ oligomers → activate CDK5/p25, GSK-3β → tau hyperphosphorylation at Ser202, Thr205, Ser396, Ser404 → tau detaches from microtubules → axonal transport failure → tau aggregates into paired helical filaments (PHFs) → neurofibrillary tangles (NFTs)
- Prion-like spreading: tau aggregates released from degenerating neurons → internalized by connected neurons → seed new NFTs → Braak staging (I-VI, hippocampus → association cortex → primary cortex)

**Braak staging:** Anatomical progression of NFT spreading from entorhinal cortex (I-II) → hippocampus/amygdala (III-IV) → isocortex (V-VI); correlates better with symptom severity than amyloid burden.

## Function

### Clinical progression

**Preclinical AD:** Normal cognition; amyloid PET positive; Aβ42 in CSF low; no symptoms; may persist 10-15 years

**Mild cognitive impairment (MCI) due to AD:** Objective memory impairment (especially episodic memory — recent events) with preserved functional independence; positive amyloid biomarker; ~15% per year convert to AD dementia; target stage for anti-amyloid therapy

**AD dementia:**
- **Mild:** Memory loss affecting daily function; language, orientation, visuospatial deficits emerging; MMSE 18-24
- **Moderate:** Severe memory loss; unable to recognize family; behavioral disturbances (agitation, psychosis, wandering); requires assistance with ADLs; MMSE 10-17
- **Severe:** Bed-bound; complete ADL dependence; dysphagia → aspiration pneumonia (leading cause of death); MMSE <10

### Neuroinflammation and TREM2

Microglia play a central, dual role in AD:
- **Protective:** Disease-associated microglia (DAM) — upregulate TREM2 (triggering receptor expressed on myeloid cells 2), ApoE, and phagocytic genes → clear Aβ plaques and apoptotic neurons
- **Pathological:** Sustained activation → NLRP3 inflammasome → IL-1β, IL-18 → neuroinflammation → tau phosphorylation → neuronal death

**TREM2 as AD risk gene:** TREM2 R47H variant → 2-3× increased AD risk (comparable to one APOE4 copy); TREM2 deficiency → impaired microglial Aβ phagocytosis → increased amyloid burden in mouse models; TREM2-activating antibodies (AL002c) in Phase II trials for early AD.

**APOE4:** APOE ε4/ε4 → 8-12× increased LOAD risk vs. ε3/ε3; mechanism: ApoE4 → impaired Aβ clearance (ApoE helps LRP1-mediated Aβ transport across BBB), promotes Aβ aggregation, associated with increased tau propagation; APOE4 carriers have shorter preclinical period and younger symptom onset.

## Pathology

### Diagnosis

**Biomarker-based (research/specialist):**
- CSF: Aβ42 ↓, p-tau181/p-tau231 ↑, total tau ↑; Aβ42/Aβ40 ratio most accurate
- PET: Amyloid PET (florbetapir/florbetaben/flutemetamol) — FDA approved for clinical use; tau PET (flortaucipir, FDA approved 2020) — detects NFT staging
- Blood biomarkers (emerging, high-throughput): Plasma p-tau217 and p-tau231 — high sensitivity/specificity for amyloid and tau pathology; plasma Aβ42/Aβ40 ratio (Simoa, IP-MS); NfL (neurofilament light chain) — non-specific neurodegeneration marker

**Clinical (traditional):**
- MMSE (Mini-Mental State Examination): 0-30; ≥24 normal; 18-23 mild; 10-17 moderate; <10 severe
- MoCA (Montreal Cognitive Assessment): More sensitive for mild impairment; ≥26/30 normal; detects MCI better than MMSE
- Neuropsychological battery: verbal learning (HVLT-R), executive function (Trails-B), language (category/letter fluency), visuospatial (Rey figure)

### Treatment [^van-dyck-2023-lecanemab]

**Disease-modifying (anti-amyloid):**
- **Lecanemab (Leqembi, anti-Aβ protofibrils, BioArctic/Eisai):** FDA approved (accelerated 2023, traditional 2024, first traditional approval for an anti-amyloid therapy); CLARITY-AD Phase III: 27% slowing of clinical decline (CDR-SB) at 18 months vs. placebo in early AD (MCI/mild AD); ARIA (amyloid-related imaging abnormalities: ARIA-E edema in 12.6%, ARIA-H microhemorrhages in 17.3%) is dose-limiting
- **Donanemab (Kisunla, anti-Aβ plaque, Eli Lilly):** FDA approved July 2024; TRAILBLAZER-ALZ-2: 35% slower decline (iADRS) vs. placebo; similar ARIA rates; unique: treatment discontinued once amyloid cleared on PET (median 12 months)
- **Aducanumab (Aduhelm, Biogen):** Controversial accelerated approval 2021 (reduced amyloid on PET); withdrawn from EU; most payers limit coverage; Phase III results discordant

**Symptomatic:**
- **Cholinesterase inhibitors** (donepezil, rivastigmine, galantamine): Inhibit acetylcholinesterase → increases synaptic ACh → modest improvement in cognition/behavior; first-line for mild-moderate AD; minimal disease modification
- **Memantine (NMDA antagonist):** Moderate uncompetitive NMDA blocker → reduces glutamate excitotoxicity; approved for moderate-severe AD; combined with donepezil (Namzaric)
- **Behavioral symptoms:** Selective SSRIs for depression/anxiety; low-dose antipsychotics (aripiprazole, quetiapine) for agitation (black box warning for elderly); avoid anticholinergics
- **Non-pharmacological:** Cognitive stimulation, physical exercise (aerobic → hippocampal neurogenesis), caregiver support

## Connections

- `targets` → **[Brain](../../06-organ/brain/README.md)** — Alzheimer's preferentially atrophies the hippocampus and entorhinal cortex; amyloid plaques and tau tangles disrupt synaptic transmission, cause microglial neuroinflammation, and drive progressive neuronal death from medial temporal lobe outward.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — microglia phagocytose Aβ plaques via TREM2; sustained microglial activation drives NLRP3 inflammasome and neuroinflammation; TREM2 loss-of-function variants are major risk factors for late-onset AD.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Aβ fibrils activate NLRP3 in microglia → IL-1β and pyroptosis → neuroinflammation and tau propagation; NLRP3 inhibition reduces AD pathology in mouse models.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — autophagy clears APP fragments and aggregated tau; declining autophagic flux in aging and AD contributes to plaque and tangle accumulation; lysosomal dysfunction is a primary AD pathomechanism; rapamycin-induced autophagy is neuroprotective in mouse models.
- `connects-to` → **[APOE](../../03-molecular/apoe/README.md)** — APOE4 (frequency ~15%) confers 3-4x heterozygous and 8-12x homozygous risk for late-onset AD; APOE4 impairs microglial Aβ phagocytosis, promotes Aβ aggregation, and worsens tau pathology; APOE4 homozygotes develop AD ~10 years earlier than APOE3 carriers.
- `connects-to` → **[APP](../../03-molecular/app/README.md)** — APP FAD mutations (V717I, Swedish K670N/M671L) and trisomy 21 increase Aβ42 via β/γ-secretase cleavage; Aβ42 oligomers are synaptotoxic and seed amyloid plaques; lecanemab (anti-Aβ protofibrils) slows cognitive decline 27% in MCI and mild AD.
- `connects-to` → **[MAPT](../../03-molecular/mapt/README.md)** — tau hyperphosphorylation at Thr181, Ser202/Thr205, Ser396 → PHF → NFT formation; Braak staging I–VI tracks NFT spread from entorhinal cortex to isocortex and correlates with cognitive decline; tau-PET (flortaucipir) predicts cognitive trajectory and guides clinical staging in AD.
- `connects-to` → **[Lewy Body Dementia](../lewy-body-dementia/README.md)** — DLB is commonly mistaken for AD; 50-70% of DLB cases have concurrent Aβ plaque and tau co-pathology; both share APOE4 risk; fatal neuroleptic sensitivity in DLB (~50%) is critical to distinguish from AD where antipsychotics are used; occipital FDG-PET hypometabolism and DAT-SPECT distinguish DLB from AD.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β hyperactivation in AD hippocampus phosphorylates tau at PHF-1 (Ser396/404) and Thr231 → neurofibrillary tangles; promotes amyloid-β via APP processing; insulin resistance activates GSK-3β; the GSK-3β inhibitor tideglusib failed Phase 2 AD trials in 2013.
- `connects-to` → **[SNCA](../../03-molecular/snca/README.md)** — alpha-synuclein (SNCA) and amyloid-β co-aggregate in DLB, an AD/PD overlap syndrome; SNCA Lewy pathology accelerates tau spreading via prion-like mechanisms; ~10-15% of AD patients have concurrent Lewy body pathology; alpha-synuclein SAA distinguishes DLB from AD.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin production declines in Alzheimer disease due to SCN atrophy; disrupted circadian rhythm → sundowning (late-day agitation); exogenous melatonin (0.5-6 mg bedtime) modestly improves AD sleep; melatonin is antioxidant and reduces Aβ aggregation in preclinical models.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — impaired brain insulin signalling ("type 3 diabetes") is implicated in AD: INSR hyposensitivity → reduced Akt → ↑GSK-3β → tau hyperphosphorylation; intranasal insulin improves memory in MCI/AD Phase 2 trials; T2DM doubles AD risk; GLP-1 agonists are under Phase 3 investigation.
- `connects-to` → **[TDP-43](../../03-molecular/tdp-43/README.md)** — LATE (limbic-predominant age-related TDP-43 encephalopathy) affects ~20% of octogenarians and mimics AD clinically; TDP-43 co-pathology in ~57% of AD brains worsens cognitive trajectory; nuclear TDP-43 loss → cryptic exon inclusion in hippocampal neurons via TDPBP splicing suppression loss.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — GLP-1R activation reduces amyloid-β, tau phosphorylation, and neuroinflammation in preclinical AD models; semaglutide EVOKE Phase 3 trial targets early AD; GLP-1R agonists may address brain insulin resistance via Akt → reduced GSK-3β → less tau hyperphosphorylation.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — age-related IGF-1 decline contributes to AD risk: low IGF-1 impairs hippocampal neurogenesis and synaptic plasticity; INSR/IGF-1R resistance in AD neurons → reduced Akt → ↑GSK-3β → tau phosphorylation; IGF-1 restores cognition in preclinical AD models and reduces Aβ plaque load.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Alzheimer's and Parkinson's are the two commonest neurodegenerative diseases that overlap in pathology: both involve misfolded-protein aggregation (amyloid/tau vs α-synuclein) and can co-occur, with Lewy bodies in many Alzheimer brains—a proteinopathy spectrum.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Alzheimer's disease is ultimately the death of neurons and their synapses: amyloid plaques and tau tangles disrupt synaptic function and trigger neuronal loss, especially of cholinergic and hippocampal neurons—and synapse loss correlates best with the dementia.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Alzheimer's disease is sometimes called 'type 3 diabetes' for its link to insulin resistance: impaired brain insulin signaling promotes amyloid and tau pathology, and type 2 diabetes raises Alzheimer's risk—why GLP-1 drugs are being tested against dementia.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Alzheimer's classically depletes acetylcholine: early loss of basal-forebrain cholinergic neurons impairs memory, and the only long-standing symptomatic drugs—cholinesterase inhibitors—work by preserving this neurotransmitter, though they do not slow the disease.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus is where Alzheimer's begins: tau tangles and atrophy strike this memory-forming structure first, explaining the early loss of recent memory, and hippocampal shrinkage on MRI is among the earliest imaging signs of the disease.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes shape Alzheimer's neuroinflammation: reactive astrocytes cluster around amyloid plaques, and while they can help clear amyloid, their chronic activation alongside microglia releases inflammatory mediators that damage neurons and synapses.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement drives synapse loss in Alzheimer's: C3 and C1q tag vulnerable synapses, prompting microglia to prune them, so reactivating this developmental 'eat-me' signal helps explain the early synaptic loss that best correlates with memory decline.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Vascular disease and Alzheimer's intertwine: atherosclerosis and small-vessel disease reduce brain perfusion and clearance of amyloid, so most late-life dementia is 'mixed', and controlling blood pressure, cholesterol, and diabetes lowers dementia risk.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression and Alzheimer's are tangled: late-life depression can be an early prodrome of dementia and is also an independent risk factor, while AD itself often presents with apathy and low mood—so new depression in an older adult warrants cognitive assessment.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Alzheimer's overexcites neurons through glutamate: amyloid and tau disrupt glutamate clearance, causing excitotoxic overstimulation of NMDA receptors that damages synapses—the rationale for memantine, which dampens this glutamate signaling.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Alzheimer's recruits cytotoxic T cells into the brain: CD8 T cells accumulate around plaques and tau pathology, and this adaptive-immune infiltration is increasingly seen as an active contributor to neurodegeneration, not a bystander.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Metal ions like zinc shape Alzheimer's amyloid: zinc and copper bind amyloid-beta, promoting its aggregation and generating oxidative stress, so disturbed brain metal balance is one hypothesis for how plaques form and injure neurons.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron builds up in the Alzheimer's brain: amyloid plaques and degenerating neurons accumulate iron that drives oxidative stress and ferroptosis, so disordered iron handling adds to the metal-linked injury alongside zinc and copper.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Alzheimer's also frays the brain's wiring insulation: oligodendrocytes and their myelin degenerate early, and amyloid and tau pathology disrupt these cells, so white-matter breakdown contributes to cognitive decline beyond neuron loss.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Alzheimer's brains run low on BDNF: this neurotrophin that sustains synapses and hippocampal plasticity falls in the disease, so reduced BDNF support helps explain the synaptic loss and failing memory.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Alzheimer's is, at heart, a loss of synapses: their disappearance tracks cognitive decline more closely than plaques or tangles do, as amyloid and tau poison synaptic function long before neurons die.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Alzheimer's deranges neuronal calcium: amyloid forms calcium-permeable pores and overexcited circuits let calcium flood in, driving the excitotoxic damage that the NMDA blocker memantine is meant to soften.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Alzheimer's may be visible in the eye: amyloid deposits and retinal nerve thinning appear in the retina, an outgrowth of the brain, making eye imaging a promising window for early, noninvasive detection.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Alzheimer's is now imaged in life: amyloid and tau PET scans use radioactive photons to reveal the plaques and tangles directly, while MRI tracks the shrinking hippocampus over time.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — What's good for the heart is good for the brain: midlife hypertension, atherosclerosis and heart disease raise Alzheimer's risk, tying cardiovascular health to the odds of dementia.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Metals gather in Alzheimer's plaques: copper, with zinc and iron, binds amyloid-beta and can drive the oxidative damage of the disease, which is why metal-chelation has been explored as therapy.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows Alzheimer's two lesions: extracellular plaques of beta-pleated amyloid fibrils and intracellular tangles of paired helical tau filaments, choking neurons as their synapses melt away.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut may whisper to the Alzheimer's brain: a dysbiotic microbiome and the inflammatory and amyloid-like products it makes are increasingly tied, through the gut-brain axis, to the neuroinflammation that fuels the disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium thins in the aging brain: low levels weaken the synaptic plasticity and NMDA regulation that memory depends on, and raising brain magnesium is studied as a way to slow cognitive decline.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Alzheimer's first disease-modifying drugs are antibodies: lecanemab and donanemab are monoclonal antibodies that clear amyloid plaques, modestly slowing decline at the cost of ARIA — brain swelling and microbleeds seen on MRI.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Amyloid also clogs the brain's vessels: in cerebral amyloid angiopathy it deposits in the walls lined by endothelial cells, weakening them into microbleeds — the same fragile vessels that bleed when anti-amyloid antibodies are given.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Sleep and Alzheimer's feed each other through orexin: the wakefulness peptide runs high and fragments sleep, and because amyloid is cleared by the glymphatic system during deep sleep, the lost rest lets more plaque accumulate.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The brain has lymphatics, and they fail in Alzheimer's: meningeal lymphatics and the glymphatic flow drain amyloid from the brain, and their decline with age and disease lets the plaque-forming peptide build up unchecked.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cholesterol handling shapes the risk: the APOE4 lipid-transport variant is the strongest common genetic risk factor, and disturbed brain cholesterol metabolism influences how amyloid is made and cleared.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid hides a reversible mimic: hypothyroidism causes a slowed, forgetful state that imitates dementia, so thyroid function is checked in every cognitive workup to catch a treatable cause before settling on Alzheimer's.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep is when the brain washes out amyloid: deep sleep drives the glymphatic clearance of amyloid-beta, so chronic insomnia lets it accumulate — and the disease in turn wrecks sleep, a vicious loop that may start years before memory fails.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — A gut-brain axis feeds the plaques: dysbiosis and bacterial products (LPS, microbial amyloids) can prime systemic and brain inflammation, and altered microbiomes are now linked to amyloid burden and cognitive decline in Alzheimer's.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation accelerates the decline: IL-6 from activated microglia and the body's chronic low-grade inflammation correlates with faster cognitive loss, part of the neuroinflammatory arm now seen as a driver, not just a bystander, in Alzheimer's.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement marks synapses for deletion: the cascade through C3 to C5 tags synapses that microglia then prune, an over-activation that drives the early synapse loss best correlating with cognitive decline in Alzheimer's.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Midlife blood pressure shapes late dementia: hypertension damages the small cerebral vessels and the clearance of amyloid, making it one of the strongest modifiable risk factors for Alzheimer's decades later.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Innate lymphocytes invade the aging brain: natural killer cells accumulate in the Alzheimer's brain and, by attacking neural cells and stoking inflammation, are emerging as contributors to the neurodegeneration.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Microglia inflame the plaques through NF-κB: amyloid-β activates NF-κB in microglia, priming the NLRP3 inflammasome and pouring out cytokines that amplify the neuroinflammation accelerating Alzheimer's.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The end stage opens the door to fatal infection: advanced Alzheimer's brings dysphagia, immobility and aspiration, so pneumonia and the sepsis it triggers are a leading cause of death in dementia.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Late-stage immobility clots the veins: as Alzheimer's confines patients to bed, venous stasis raises the risk of deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — The diseased cortex becomes hyperexcitable: Alzheimer's substantially raises seizure risk — strikingly so in early-onset disease — as amyloid and tau pathology disrupt networks into epileptiform and overt seizures.
- `connects-to` → **[Stroke](../stroke/README.md)** — Vascular and amyloid injury overlap: cerebral amyloid angiopathy weakens vessels toward hemorrhage while shared vascular risk factors drive ischemic stroke, and stroke and Alzheimer's pathology together produce mixed dementia.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Frail bones meet frequent falls: immobility, low vitamin D and the falls of impaired gait and cognition make osteoporotic hip fractures common and devastating in advanced Alzheimer's.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Late dementia lets food reach the lungs: progressive dysphagia in advanced Alzheimer's causes aspiration, and the resulting pneumonia — often pneumococcal — is the leading immediate cause of death.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Bedbound immobility breaks down the skin: in end-stage Alzheimer's, immobility and incontinence predispose to pressure ulcers over bony prominences that heal poorly in the frail, malnourished patient.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Confusion breeds chronic worry: anxiety and agitation are common neuropsychiatric features of Alzheimer's, fueled by the disorientation and memory loss of failing cognition.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is the archetypal neurodegeneration: Alzheimer's destroys cortical and hippocampal neurons through amyloid plaques and tau tangles, the leading neurodegenerative disease of the nervous system.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Late disease robs the body of movement: advancing Alzheimer's brings gait disturbance and falls with fractures, and end-stage immobility leaves contractures and profound sarcopenia.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Eventually it takes away swallowing: advanced Alzheimer's causes dysphagia with aspiration and progressive weight loss, raising the difficult questions around assisted and tube feeding.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Aspiration pneumonia ends it: dysphagia in end-stage Alzheimer's lets food and saliva enter the lungs, making aspiration pneumonia the most common immediate cause of death.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Innate immunity shapes the plaques: microglial neuroinflammation and risk genes like TREM2 drive amyloid clearance and damage, making the brain's immune response a central target of new therapies.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Amyloid also lines the vessels: cerebral amyloid angiopathy deposits beta-amyloid in cortical artery walls, causing lobar haemorrhages, while vascular disease adds to mixed dementia.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Brain insulin resistance earns it a nickname: impaired cerebral insulin signalling has led some to call Alzheimer's 'type 3 diabetes', and hypothalamic degeneration disturbs weight, appetite and circadian rhythm.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Oestrogen loss shifts the risk: the fall in oestrogen at menopause is implicated in women's higher Alzheimer's risk, interacting with the APOE genotype.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — End-stage immobility breaks the skin: in advanced Alzheimer's, immobility and incontinence make pressure ulcers a major preventable complication of care.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The failing kidney ages the brain: chronic kidney disease is an independent risk factor for Alzheimer's, through shared vascular damage and the accumulation of uraemic toxins that impair cognition.
- `connects-to` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — A virus implicated in its origin: herpes simplex type 1 reactivation in the brain is a long-standing hypothesis in Alzheimer's, with amyloid-beta itself acting as an antimicrobial peptide that traps the virus.
- `connects-to` → **[Ginkgo Biloba](../../../03-medicine/02-traditional/ginkgo-biloba/README.md)** — A traditional remedy long tried: Ginkgo biloba extract has been widely used and studied for dementia and Alzheimer's, though large trials show little benefit in prevention or treatment.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Anti-amyloid antibodies modify it: lecanemab and donanemab, monoclonal antibodies that clear amyloid-beta plaques, are the first disease-modifying Alzheimer's drugs, modestly slowing decline at the cost of brain-swelling and microhaemorrhage (ARIA).
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Tau wrecks the axon's railway: hyperphosphorylated tau detaches from microtubules and forms neurofibrillary tangles, collapsing the axonal transport that supplies synapses — a core mechanism of neurodegeneration in Alzheimer's.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Amyloid lines the cerebral vessels: in cerebral amyloid angiopathy, amyloid-beta deposits in the arterial wall of cortical vessels, weakening them and causing the lobar haemorrhages and microbleeds common in Alzheimer's.
- `connects-to` → **[ALS](../als/README.md)** — Overlapping proteinopathies: TDP-43 aggregates that define ALS-frontotemporal disease also appear in limbic-predominant age-related TDP-43 encephalopathy and many Alzheimer's brains, blurring the boundary between the neurodegenerations.
- `connects-to` → **[Huntington's Disease](../huntingtons-disease/README.md)** — Two faces of neurodegeneration: Alzheimer's is a sporadic amyloid-and-tau dementia of late life, while Huntington's is a monogenic CAG-repeat disease striking midlife—different drivers converging on protein aggregation and neuronal loss.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Complement-driven synapse loss in both: Alzheimer's and schizophrenia share microglial, complement-mediated pruning of synapses and neuroinflammation, and late-life psychosis blurs into Alzheimer's despite their different ages of onset.
- `connects-to` → **[Obesity](../obesity/README.md)** — Midlife adiposity and dementia: midlife obesity raises the later risk of Alzheimer's through insulin resistance, vascular injury and chronic neuroinflammation, tying metabolic health to brain ageing.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Infection and cognitive decline: COVID-19 can leave lasting 'brain fog' and accelerate cognitive decline in older adults, with neuroinflammation a proposed link to Alzheimer's pathology.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The peripheral amyloid sink: the liver clears circulating amyloid-beta via LRP1, and impaired hepatic clearance may raise the brain's amyloid burden—linking systemic metabolism to Alzheimer's.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Trauma and later dementia: chronic PTSD and the sustained cortisol of traumatic stress damage the hippocampus and are associated with a substantially raised risk of later Alzheimer's disease.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Orexin, sleep and amyloid: orexin governs the sleep-wake cycle that drives glymphatic amyloid clearance, tying the orexin system disrupted in narcolepsy to the sleep disturbance and amyloid accumulation of Alzheimer's.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Mood disorder and dementia risk: bipolar disorder is associated with a higher risk of later dementia, while long-term lithium appears neuroprotective—through GSK-3β inhibition—and lowers Alzheimer's incidence.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Neuroinflammation: TNF-α released by activated microglia around amyloid plaques amplifies the chronic inflammation that accelerates synaptic loss and neurodegeneration in Alzheimer's.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Microglial driver: IL-1β from plaque-associated microglia is a central inflammatory mediator in Alzheimer's, promoting tau phosphorylation and the neurotoxic glial response.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Vascular hypoxia: cerebral hypoperfusion in Alzheimer's stabilises HIF-1α, linking the vascular contribution to dementia with amyloid processing and neuronal stress responses.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA-sensing neuroinflammation: leaked mitochondrial DNA activates the cGAS-STING pathway in microglia and neurons in Alzheimer's, an emerging driver of the type-I-interferon response and tau pathology.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 produced in the Alzheimer's brain recruits peripheral monocytes and activates microglia around plaques, amplifying the neuroinflammation linked to cognitive decline.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Impaired clearance: overactive mTOR suppresses the autophagy needed to clear amyloid-β and tau aggregates, and its inhibition (rapamycin) is neuroprotective in Alzheimer's models.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Aggregated amyloid-β engages microglial TLR4, triggering the NF-κB-driven neuroinflammatory cytokine response that contributes to the synaptic and neuronal injury driving cognitive decline in Alzheimer's disease.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3 executes the neuronal apoptosis of Alzheimer's and cleaves tau into aggregation-prone fragments, coupling neuronal death directly to the propagation of tau pathology through the brain.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Dysregulated VEGF and cerebral amyloid angiopathy impair the neurovascular unit in Alzheimer's, the vascular arm that worsens amyloid clearance across the blood-brain barrier and accelerates cognitive decline.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — RAGE transports circulating amyloid-β across the blood-brain barrier into the brain, the influx counterpart to LRP1-mediated efflux, so RAGE upregulation tips the balance toward the amyloid accumulation of Alzheimer's.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by activated microglia around amyloid plaques amplifies the neuroinflammatory response, a microglial signal increasingly seen as a driver of Alzheimer's neurodegeneration and a candidate therapeutic target.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — The noradrenergic locus coeruleus is one of the earliest sites of tau pathology in Alzheimer's, and its degeneration depletes norepinephrine, removing a neuroprotective, anti-inflammatory signal and contributing to early cognitive symptoms.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Impaired AKT signaling from brain insulin resistance disinhibits GSK3β (already mapped) to hyperphosphorylate tau, the "type-3 diabetes" link between the insulin already mapped and Alzheimer neurodegeneration.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Oxidative stress is central to Alzheimer's, and a declining NRF2 antioxidant response permits the lipid peroxidation and mitochondrial damage that injure neurons.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Dysregulated calcium-calcineurin signaling in Alzheimer's drives dendritic-spine retraction, synapse loss and astrocyte activation that track closely with cognitive decline.
- `connects-to` → **[Aquaporin-4](../../03-molecular/aquaporin-4/README.md)** — Astrocytic aquaporin-4 drives the glymphatic flow that clears amyloid-β during sleep, and the loss of AQP4 polarization impairs Aβ removal in Alzheimer's disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MAPK-ERK, alongside GSK-3β (mapped), hyperphosphorylates tau (MAPT mapped) into the paired helical filaments that form the neurofibrillary tangles of Alzheimer's.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Microglial TLR4 (mapped) sensing of amyloid-β signals through MyD88 to NF-κB (mapped), driving the neuroinflammation that propagates Alzheimer's pathology.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine-driven JAK-STAT signaling sustains the reactive astrogliosis and microglial activation (IL-6 mapped) that amplify Alzheimer's neuroinflammation.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 activation drives the reactive-astrocyte transcriptional program around amyloid plaques, contributing to neuroinflammation in Alzheimer's disease.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN regulation of the PI3K-AKT-GSK-3β axis (AKT, mTOR and GSK-3β mapped) links insulin/IGF resistance to tau phosphorylation and neuronal vulnerability in Alzheimer's disease.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling drives the disease-associated microglial interferon response increasingly implicated in the neuroinflammation of Alzheimer's disease.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF-TrkB (NTRK) signaling (BDNF already mapped) supports the synaptic maintenance and neuronal survival whose loss accelerates degeneration in Alzheimer's disease.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the neuroprotective-versus-inflammatory balance of glia and the cerebrovascular responses relevant to Alzheimer's disease.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate neuronal autophagy and oxidative-stress defense, programs that fail in the neurodegeneration of Alzheimer's disease.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by activated microglia amplify the neuroinflammation associated with amyloid pathology in Alzheimer's disease.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic T-cell activity in the infiltrated brain contributes to the adaptive-immune component of neurodegeneration in Alzheimer's disease.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the neuronal insulin/IGF survival pathways whose impairment contributes to Alzheimer's disease.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, coupled to autophagy (autophagy already mapped), regulates the clearance of amyloid and tau aggregates in Alzheimer's disease.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Aberrant CDK-driven cell-cycle re-entry of postmitotic neurons contributes to the tau hyperphosphorylation and neuronal death of Alzheimer's disease.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation implicated in the late-onset risk of Alzheimer's disease.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (FYN) kinase signaling, activated downstream of amyloid-β via cellular prion protein, mediates the tau-dependent synaptotoxicity of Alzheimer's disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven microglial and monocyte recruitment contributes to the neuroinflammation of Alzheimer's disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the microglial and neural-progenitor responses of the neuroinflammation of Alzheimer's disease.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial amyloid clearance and neuroinflammatory responses of Alzheimer's disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation and blood-brain-barrier dysfunction of Alzheimer's disease.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neuronal and microglial gene programs of Alzheimer's disease.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (A2A receptor) signaling participates in the synaptic dysfunction and neuroinflammation of Alzheimer's disease.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microglial activation and neuroinflammation of Alzheimer's disease.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Anti-amyloid immunotherapy: the first disease-modifying Alzheimer's drugs, lecanemab and donanemab, are IgG monoclonal antibodies that clear amyloid-beta (APP already mapped) from the brain, validating the amyloid target through passive immunisation.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences: women bear a disproportionate share of Alzheimer's disease, and the loss of neuroprotective estrogen at menopause is one proposed contributor to their elevated risk and the faster progression seen after diagnosis.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Microglial neuroinflammation: MHC class II is upregulated on activated microglia in Alzheimer's disease, marking the antigen-presenting, inflammatory microglial state (TREM2-driven) that shapes plaque clearance and neurodegeneration.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Brain renin-angiotensin: a central renin-angiotensin system modulates cerebral blood flow, inflammation and amyloid handling, and antihypertensives blocking angiotensin II are associated with lower dementia risk, a vascular-metabolic target in Alzheimer's disease.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Neurosteroid protection: progesterone and its neurosteroid metabolites are neuroprotective and support myelin, and together with estrogen (already mapped) their postmenopausal loss is proposed to contribute to women's higher Alzheimer's risk.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Cholinergic and histaminergic cognition: histaminergic H3 signalling modulates cognition and was a drug target in Alzheimer's, while the cumulative anticholinergic and antihistamine burden of many drugs is itself associated with higher dementia risk.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative neurotoxicity: reactive oxygen species, to which xanthine oxidase contributes, are central to the amyloid- and tau-driven neurotoxicity of Alzheimer's (NRF2 already mapped), and the oxidative damage compounds the mitochondrial and metal (iron already mapped) injury.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the microglial (already mapped) cyclooxygenase pathway drive the neuroinflammation of Alzheimer's (IL-6, TNF and IL-1 already mapped), and epidemiological studies link NSAID use to lower dementia risk.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonergic degeneration: loss of serotonergic neurons contributes to the depression, agitation and other behavioural symptoms of Alzheimer's (norepinephrine already mapped), and serotonergic drugs are used to manage these neuropsychiatric features.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Microglial polarisation: IL-4 polarises the microglia (already mapped) toward a neuroprotective M2 phenotype, and the balance against the pro-inflammatory activation shapes whether the neuroinflammation of Alzheimer's clears amyloid or damages neurons.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Neuroimmune balance: the anti-inflammatory IL-10 counters the microglial pro-inflammatory cytokines (TNF, IL-6 and IL-1 already mapped) of Alzheimer's, part of the neuroinflammatory balance that shapes the disease.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Omega-3 and brain lipids: the omega-3 fatty acid DHA is a major structural lipid of the brain, and its pro-resolving mediators counter neuroinflammation (prostaglandins already mapped), the basis of dietary interest in omega-3 for cognitive decline.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the neuroinflammation (TNF, IL-6 and IL-1 already mapped) of Alzheimer's disease.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic risk: leptin has neuroprotective and pro-cognitive actions, and leptin resistance with the metabolic dysfunction (insulin already mapped) is linked to the risk of Alzheimer's disease.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine inflammation: resistin, with leptin (already mapped), links the adipose-inflammatory and metabolic (insulin already mapped) state to the neuroinflammation implicated in the risk of Alzheimer's disease.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Neuroprotective adipokine: adiponectin, with leptin and resistin (already mapped), has neuroprotective actions; the adiponectin resistance and the metabolic (insulin already mapped) dysfunction are linked to Alzheimer's-disease risk.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Amyloid metal binding: copper, with zinc (already mapped), binds the amyloid-β (APP already mapped) and catalyses the oxidative damage, the metal dyshomeostasis of Alzheimer's disease.
- `connects-to` → **[Type 2 diabetes](../type-2-diabetes/README.md)** — Type-3 diabetes: the brain insulin (already mapped) resistance links Alzheimer's disease to type 2 diabetes (the shared metabolic and inflammatory pathways), the 'type-3 diabetes' concept.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the cytosolic and mitochondrial DNA, drives the microglial (already mapped) neuroinflammation of Alzheimer's disease.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the adaptive immune contribution to the neuroinflammation of Alzheimer's disease.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of Alzheimer's disease.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune interaction in Alzheimer's disease.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the adaptive-immune contribution to the neuroinflammation of Alzheimer's disease.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the neuroimmune interaction in Alzheimer's disease.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the blood-brain-barrier dysfunction of Alzheimer's disease.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the microglial (already mapped) activation and the complement-mediated synapse loss of Alzheimer's disease.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Brain iron: transferrin, the iron carrier, is central to the brain-iron accumulation that, with the disordered iron handling, drives the oxidative stress and ferroptosis contributing to the neurodegeneration of Alzheimer's disease.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H, whose variants are Alzheimer's-risk loci, regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-mediated synapse loss of Alzheimer's disease.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway (C1q-initiated) that tags the synapses for the microglial (already mapped) pruning of Alzheimer's disease.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the meningeal and CNS-border compartments present antigen to the T cells (already mapped) in the neuroinflammation of Alzheimer's disease.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuro-epithelial alarmin: TSLP, released from the inflamed gut-epithelium (gut-microbiome already mapped) and skin (already mapped), activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the systemic immune activation of Alzheimer's disease.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-BBB axis: bradykinin, generated by the contact system activated by complement (C3, C5, C5aR1 already mapped) and amyloid fibrils in Alzheimer's disease, augments blood-brain-barrier permeability and amplifies the microglial (already mapped) neuroinflammation.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective cytokine: erythropoietin, acting via EPOR on neurons (already mapped) and astrocytes (already mapped), promotes neuronal survival and limits the oxidative and neuroinflammatory degeneration of Alzheimer's disease.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM remodelling in neuritic plaques: periostin, expressed by reactive astrocytes (already mapped) and microglia (already mapped) around amyloid deposits, modulates the peri-plaque extracellular matrix and promotes the fibrotic neuroinflammatory remodelling of Alzheimer's disease.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Neuroendocrine-immune coupling: prolactin, acting via PRLR on microglia (already mapped) and astrocytes (already mapped), modulates the neuroinflammatory cytokine (TNF-α and IL-6 already mapped) milieu and may influence the female-predominant prevalence of Alzheimer's disease.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Hippocampal neuroprotection: oxytocin, via oxytocin receptors on hippocampal neurons and microglia (already mapped), suppresses the NF-κB/TNF-α (already mapped) neuroinflammatory cascade and improves the synaptic plasticity impaired by amyloid in Alzheimer's disease.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen neuroprotection: testosterone suppresses NF-κB (already mapped) neuroinflammation and amyloid-β production in neurons (already mapped); androgen deficiency amplifies microglia (already mapped) and complement-C5 (already mapped) neurodegeneration in Alzheimer's.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Brain fluid homeostasis: vasopressin, via V1/V2 receptors on neurons (already mapped), modulates brain (already mapped) fluid and synaptic homeostasis; vasopressin dysregulation amplifies NF-κB (already mapped) and microglia (already mapped) neuroinflammatory damage in Alzheimer's.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant neuroprotection: selenium, via GPx/thioredoxin reductase, protects neurons (already mapped) and astrocytes (already mapped) from oxidative injury; selenium deficiency amplifies NF-κB (already mapped) and microglia (already mapped) amyloid-β-driven neurodegeneration in Alzheimer's.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — AD iodine: iodine-dependent thyroid hormones regulate neuronal (neuron already mapped) metabolism and synaptic (synapse already mapped) function; hypothyroidism amplifies NF-κB (already mapped) and NLRP3 inflammasome (already mapped) neuroinflammation and amyloid-β burden.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — AD sodium: sodium dysregulation in the brain (already mapped) drives neuronal (neuron already mapped) excitotoxicity via glutamate (already mapped) receptor overload; sodium imbalance amplifies NF-κB (already mapped) and NLRP3 inflammasome (already mapped) amyloid-β cascade.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — AD potassium: potassium efflux from neurons (already mapped) activates NLRP3 inflammasome (already mapped) in microglia (already mapped); disrupted K⁺ amplifies NF-κB (already mapped) and IL-1β (already mapped) amyloid-β neuroinflammation and hippocampal (already mapped) loss.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — AD phosphorus: phosphorus fuels neuronal (neuron already mapped) and microglia (already mapped) ATP; phosphorus deficiency impairs synaptic transmission and amplifies NLRP3 inflammasome (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) amyloid-β cascade of AD.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — AD nitrogen: nitric oxide (NO, nitrogen-derived) in microglia (already mapped) and neurons (already mapped) amplifies neuroinflammation; NO excess upregulates NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) and NLRP3 (already mapped) cascade in AD.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — AD chloride: chloride channels on microglia (already mapped) and neurons (already mapped) regulate intracellular pH; chloride dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade in AD.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — AD sulfur: sulfur-containing glutathione in neurons (already mapped) and microglia (already mapped) scavenges ROS; sulfur deficiency amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) neurodegeneration in AD.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — mitochondrial oxygen sustains ATP in neurons (already mapped) and microglia (already mapped) for amyloid-β clearance; hypoxia amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory amyloid-tau cascade in AD.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — carbon, via bicarbonate in neurons (already mapped) and microglia (already mapped), maintains pH homeostasis; carbon dioxide dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory amyloid-tau cascade in AD.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — hydrogen, via H2O2 and ROS redox balance in neurons (already mapped) and microglia (already mapped), sets oxidative tone; hydrogen excess amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory amyloid-tau cascade in AD.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — AD PD-1: PD-1 on microglia (already mapped) and t-cytotoxic-cell (already mapped) modulates neuroinflammatory homeostasis; PD-1 dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) amyloid-tau neuroinflammatory cascade in AD.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — AD WNT/β-catenin: WNT/β-catenin in neurons (already mapped) and microglia (already mapped) promotes synaptic plasticity and amyloid clearance; WNT dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory amyloid-tau cascade in AD.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — AD RANKL: RANKL from microglia (already mapped) and astrocytes (already mapped) modulates neurovascular and synaptic remodelling; RANKL dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) neuroinflammatory amyloid cascade in AD.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — AD IL-2: IL-2 signalling in regulatory-t-cell (already mapped) and microglia (already mapped) modulates neuroinflammatory homeostasis; IL-2 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) amyloid-tau cascade of AD.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — AD fibronectin: fibronectin in microglia (already mapped) and astrocytes (already mapped) promotes ECM accumulation in AD plaques; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) amyloid-tau neuroinflammatory cascade of AD.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — AD notch: notch signalling in neurons (already mapped) and microglia (already mapped) modulates synaptic plasticity and amyloid processing; notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) cascade of AD.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — AD activin-A: activin-A from microglia (already mapped) and astrocytes (already mapped) modulates neuroinflammatory responses in AD; activin-A excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) amyloid-tau cascade of Alzheimer's disease.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — AD TGF-β: TGF-β in microglia (already mapped) and astrocytes (already mapped) exerts neuroprotective and pro-fibrotic roles; TGF-β dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of Alzheimer's disease.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — AD CGRP: CGRP from trigeminal neurons (already mapped) and microglia (already mapped) modulates cerebrovascular tone in AD; CGRP dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) neurovascular cascade of Alzheimer's disease.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — AD calcitonin: calcitonin from microglia (already mapped) and neurons (already mapped) modulates cerebrovascular calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) amyloid-tau cascade of AD.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — AD substance-p: substance-P from neurons (already mapped) and microglia (already mapped) modulates AD nociceptive signalling; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of AD.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — AD insulin-receptor: insulin receptor on neurons (already mapped) and microglia (already mapped) drives metabolic neuroprotection; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) amyloid-tau cascade of AD.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — AD aldosterone: aldosterone from microglia (already mapped) and astrocytes (already mapped) modulates neuroinflammatory fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) amyloid-tau cascade of AD.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — AD androgen-receptor: androgen receptor on neurons (already mapped) and microglia (already mapped) modulates neuroprotective sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of AD.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — AD adrenomedullin: adrenomedullin from astrocytes (already mapped) and microglia (already mapped) modulates neuroinflammatory vasodilation; adrenomedullin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of AD.

[^selkoe-2016-alzheimer]: Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer's disease at 25 years. *EMBO Mol Med.* 2016;8(6):595-608. [doi:10.15252/emmm.201606210](https://doi.org/10.15252/emmm.201606210) · [PubMed 27025652](https://pubmed.ncbi.nlm.nih.gov/27025652/)
[^jack-2018-nia-aa]: Jack CR Jr, Bennett DA, Blennow K, et al. NIA-AA Research Framework: Toward a biological definition of Alzheimer's disease. *Alzheimers Dement.* 2018;14(4):535-562. [doi:10.1016/j.jalz.2018.02.018](https://doi.org/10.1016/j.jalz.2018.02.018) · [PubMed 29653606](https://pubmed.ncbi.nlm.nih.gov/29653606/)
[^van-dyck-2023-lecanemab]: van Dyck CH, Swanson CJ, Aisen P, et al. Lecanemab in Early Alzheimer's Disease. *N Engl J Med.* 2023;388(1):9-21. [doi:10.1056/NEJMoa2212948](https://doi.org/10.1056/NEJMoa2212948) · [PubMed 36449413](https://pubmed.ncbi.nlm.nih.gov/36449413/)
