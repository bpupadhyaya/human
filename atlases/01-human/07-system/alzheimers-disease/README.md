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

[^selkoe-2016-alzheimer]: Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer's disease at 25 years. *EMBO Mol Med.* 2016;8(6):595-608. [doi:10.15252/emmm.201606210](https://doi.org/10.15252/emmm.201606210) · [PubMed 27025652](https://pubmed.ncbi.nlm.nih.gov/27025652/)
[^jack-2018-nia-aa]: Jack CR Jr, Bennett DA, Blennow K, et al. NIA-AA Research Framework: Toward a biological definition of Alzheimer's disease. *Alzheimers Dement.* 2018;14(4):535-562. [doi:10.1016/j.jalz.2018.02.018](https://doi.org/10.1016/j.jalz.2018.02.018) · [PubMed 29653606](https://pubmed.ncbi.nlm.nih.gov/29653606/)
[^van-dyck-2023-lecanemab]: van Dyck CH, Swanson CJ, Aisen P, et al. Lecanemab in Early Alzheimer's Disease. *N Engl J Med.* 2023;388(1):9-21. [doi:10.1056/NEJMoa2212948](https://doi.org/10.1056/NEJMoa2212948) · [PubMed 36449413](https://pubmed.ncbi.nlm.nih.gov/36449413/)
