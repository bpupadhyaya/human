---
schema: human-scale-entry/v1
id: opioid-use-disorder
name: Opioid Use Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Opioid use disorder (~2.7M US; ~80K deaths/year fentanyl) involves μ-opioid-mediated VTA disinhibition → NAcc dopamine surge, tolerance, and LC rebound withdrawal; MOUD: buprenorphine, methadone, naltrexone; naloxone reverses overdose."
aliases: ["opioid use disorder", "OUD", "heroin addiction", "opioid dependence", "buprenorphine", "methadone", "naltrexone", "Suboxone", "MOUD", "COWS", "opioid overdose", "naloxone", "fentanyl"]
sources:
  - id: volkow-2016-opioid-crisis
    type: peer-reviewed
    cite: "Volkow ND, Collins FS. The role of science in addressing the opioid crisis. N Engl J Med. 2017;377(4):391-394."
    doi: "10.1056/NEJMsr1706626"
    pmid: "28723324"
    url: "https://doi.org/10.1056/NEJMsr1706626"
    accessed: "2026-06-08"
  - id: mattick-2009-bupe-meta
    type: peer-reviewed
    cite: "Mattick RP, Breen C, Kimber J, Davoli M. Buprenorphine maintenance versus placebo or methadone maintenance for opioid dependence. Cochrane Database Syst Rev. 2014;2:CD002207."
    doi: "10.1002/14651858.CD002207.pub4"
    pmid: "24500948"
    url: "https://doi.org/10.1002/14651858.CD002207.pub4"
    accessed: "2026-06-08"
  - id: kreek-2002-opioid-neuroscience
    type: peer-reviewed
    cite: "Kreek MJ, Koob GF. Drug dependence: stress and dysregulation of brain reward pathways. Drug Alcohol Depend. 1998;51(1-2):23-47."
    doi: "10.1016/S0376-8716(98)00064-7"
    pmid: "9716926"
    url: "https://doi.org/10.1016/S0376-8716(98)00064-7"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "μ-opioid receptor activation on VTA GABAergic interneurons → disinhibition → increased VTA DA firing → NAcc dopamine surge → euphoria; chronic use → reward circuit hypofunction → anhedonia; naltrexone (MOR antagonist) blocks this disinhibition → reduces opioid reward."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "μ-opioid receptors on VTA GABAergic interneurons mediate euphoric disinhibition; chronic opioid → tolerance at MOR on GABA interneurons → blunted inhibition; buprenorphine (partial MOR agonist) provides stable DA tone without the high-reinforcement surge of full agonists."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Chronic opioid potentiates corticostriatal glutamatergic synapses → LTP underlying craving and drug-cue reactivity; AMPA receptor upregulation in NAcc drives relapse-associated excitability; mGluR5 antagonists reduce cue-triggered reinstatement of opioid seeking in rodents."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Chronic opioid drives ΔFosB accumulation in NAcc → altered BDNF expression and reward circuit plasticity; BDNF in VTA sensitizes opioid-induced reinforcement; withdrawal-phase BDNF surge in NAcc contributes to aversion; BDNF/TrkB signaling is a therapeutic target in relapse."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "μ-opioid receptors on LC suppress NE during opioid use; abrupt cessation → LC rebound → excess NE → withdrawal (diaphoresis, piloerection, tachycardia, diarrhea, anxiety); clonidine and lofexidine (α2 agonists) reduce LC hyperactivation and are FDA-approved for opioid withdrawal."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "OUD remodels VTA-NAcc reward circuits (MOR disinhibition), LC (NE rebound withdrawal), PFC control circuits (craving-driven approach), and amygdala (conditioned fear of withdrawal); buprenorphine and naltrexone normalize these circuit abnormalities over months of treatment."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Opioid use disorder centers on the μ-opioid receptor: on VTA GABA interneurons it disinhibits dopamine, on the locus coeruleus it sets up rebound withdrawal, and in the brainstem it drives respiratory depression — the target of buprenorphine, methadone, and naloxone."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Injecting opioids seeds the bloodstream with skin and needle bacteria, which lodge on heart valves — classically the tricuspid — to cause infective endocarditis, a high-mortality complication of injection drug use that may need valve surgery alongside OUD treatment."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Opioid and stimulant use disorders share the VTA-NAcc dopamine reward circuitry but pull in opposite directions, and are increasingly fatal together: 'speedball' combinations and fentanyl-contaminated stimulants drive a rising share of overdose deaths."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Injection opioid use is the leading driver of hepatitis C transmission: shared needles spread HCV efficiently and people with OUD carry a high HCV burden; opioid agonist therapy, syringe services and direct-acting antivirals (treatment-as-prevention) are the combined response."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Injection opioid use spreads HIV through shared needles, and OUD also raises sexual transmission risk; harm reduction (syringe services, naloxone), opioid agonist therapy and antiretrovirals/PrEP intersect here, and untreated OUD undermines HIV care and viral suppression."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Opioid and alcohol use disorders frequently co-occur and are dangerous together: both are CNS depressants, so combined use multiplies respiratory depression and overdose death; they share reward and stress circuitry, and concurrent alcohol complicates opioid agonist therapy."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Opioid and gambling disorders share the brain's opioid-modulated reward system: the endogenous opioid system shapes the high of both substance and behavioral addiction, which is why the antagonist naltrexone treats alcohol and opioid dependence and also curbs gambling urges."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Chronic pain is a major gateway to opioid use disorder: opioids prescribed for neuropathic and other chronic pain can lead to tolerance, dependence, and addiction—yet they work poorly for neuropathic pain, so anticonvulsants and antidepressants are preferred."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Opioid use disorder rewires reward and stress neurons: repeated mu-opioid stimulation of mesolimbic dopamine neurons drives tolerance and dependence, while withdrawal activates stress circuits—so the neural adaptations, not just the drug, sustain craving and relapse."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Respiratory depression is how opioids kill: mu-receptor activation in brainstem respiratory centers blunts the drive to breathe, so overdose causes fatal hypoventilation—the mechanism naloxone reverses and the reason fentanyl's potency makes overdose so lethal."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Opioid use disorder and depression are tightly intertwined: depression drives self-medication while chronic opioid use dysregulates reward and worsens mood, and withdrawal mimics depression—so the two conditions amplify each other and complicate treatment."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Opioids harm the lung beyond overdose: sedation promotes aspiration pneumonia, overdose can cause non-cardiogenic pulmonary edema, and injection use seeds septic emboli—so the lung suffers both acute and chronic complications of opioid use."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "Opioid and endocannabinoid systems are deeply interlinked: both engage the brain's reward and pain circuits and their receptors interact, so cannabinoids modulate opioid reward and withdrawal—part of why self-medication patterns are common in OUD."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "PTSD and opioid use disorder are tightly bound: people with PTSD use opioids to numb hyperarousal and emotional pain, raising the risk of dependence, while the chaos of addiction generates new trauma—so trauma-focused care is key to treating OUD."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Opioid use disorder rewires the nervous system: repeated mu-receptor stimulation downregulates reward circuits and upregulates stress pathways, so tolerance, craving and a brutal withdrawal are neuroadaptations—addiction as a chronic brain disease, not a moral failing."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Opioid use in pregnancy crosses the placenta: the fetus becomes dependent in utero and, after birth, suffers neonatal abstinence syndrome with tremor, irritability, and feeding problems—so opioid use disorder in pregnancy needs careful, supervised treatment."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Injection opioid use invites Staphylococcus aureus: non-sterile injecting seeds the bloodstream with S. aureus (often MRSA), causing skin abscesses, endocarditis, and bone infections—among the most dangerous medical complications of opioid use disorder."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Opioids profoundly slow the gut: mu-receptors on the bowel cause opioid-induced constipation, the most persistent side effect, since unlike other opioid effects it does not wane with tolerance—so laxatives and PAMORA drugs are routine in chronic use."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Opioid overdose kills by letting carbon dioxide build up: opioids suppress the brainstem's CO2-driven breathing reflex, so respiration slows until hypercapnia and hypoxia stop the heart—the mechanism naloxone reverses by displacing the drug."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Injection opioid use endangers the liver: shared needles transmit hepatitis C (and B), making chronic liver disease and cirrhosis common in opioid use disorder—so liver screening and HCV treatment are part of care."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Opioids wreck sleep both ways: they fragment sleep architecture and suppress breathing during it, while withdrawal causes severe insomnia—so disturbed sleep both drives continued use and complicates recovery."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Opioid overdose kills by cutting off oxygen: opioids suppress the brainstem's drive to breathe, so breathing slows and stops, starving the brain and heart of oxygen—the hypoxia that naloxone races to reverse."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Opioid addiction rewires reward synapses: repeated drug surges strengthen and reshape connections in the dopamine pathway, the lasting synaptic plasticity that entrenches craving and makes relapse easy long after the drug is gone."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Opioids inflame the brain's immune cells: they activate microglia that release cytokines, which paradoxically worsen pain sensitivity and tolerance, so this neuroinflammation helps push escalating doses and dependence."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Opioids seize up the large intestine: mu-receptors in the gut wall halt its muscular waves, causing the severe constipation that nearly every opioid user gets and that special gut-targeted drugs are made to relieve."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "An opioid overdose floods the blood with hydrogen ions: suppressed breathing lets carbon dioxide build up into a respiratory acidosis, the falling pH that compounds the hypoxia of overdose."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Opioid addiction enlists astrocytes: these glial cells help control glutamate in the reward circuit, and their changes contribute to the synaptic plasticity and craving that sustain dependence and relapse."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Brain imaging reveals opioids' grip: fMRI photons show the reward circuit firing to drug cues, and MRI can expose the anoxic brain injury left by a survived overdose."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Injection opioid use infects the endothelium: shared needles seed bacteria onto heart-valve and vessel-lining endothelial cells, causing the infective endocarditis that is a major killer in the epidemic."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Injection drug use scars and infects the skin: track marks, abscesses and cellulitis from non-sterile injection are common, sometimes the first visible clue to hidden opioid use."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "An overdose can wreck the kidneys: lying unconscious and immobile crushes muscle into rhabdomyolysis, and the released myoglobin floods the renal tubules, a common cause of acute kidney injury after a heroin overdose."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Overdose stupor can crush the nerves: hours spent motionless and unrousable compress peripheral nerves against bone, leaving the wrist-drop or foot-drop palsies that linger after the opioid wears off."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Injection seeds clots on the heart's valves: bacteria delivered straight into the blood build platelet-fibrin vegetations of infective endocarditis, which break off as septic emboli to the lungs, brain, and beyond."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The pupils give opioids away: by acting on the brainstem, they constrict the pupils to pinpoint miosis — a hallmark sign of intoxication and overdose that reverses dramatically when naloxone is given."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Chronic opioids switch off the sex hormones: they suppress the hypothalamic-pituitary-gonadal axis, dropping testosterone into an opioid-induced hypogonadism with low libido, fatigue, infertility, and bone loss."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Opioids stall the gut from the top: they trigger nausea and vomiting through the brainstem and slow gastric emptying, the upper-GI counterpart to the relentless constipation they cause lower down."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Dependence reaches the next generation: opioid use in pregnancy causes neonatal abstinence syndrome — a withdrawing newborn — and chronic use disrupts menstruation and fertility, making reproductive care part of treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "A vaccine is being built against the high: anti-opioid vaccines raise antibodies that bind fentanyl or heroin in the blood before they reach the brain, an experimental approach to blunt overdose and relapse."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Opioids reshape the gut's flora: by slowing transit and acting on gut opioid receptors they foster dysbiosis and a leaky barrier, and the altered microbiome may in turn influence tolerance and withdrawal."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "Injection use drives the HIV epidemic: shared needles transmit the virus, so opioid use disorder is a leading route of HIV spread, and needle exchange and treatment of addiction are core HIV-prevention tools."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Orexin fuels the craving and the withdrawal: this arousal-and-reward peptide is recruited by chronic opioids, and blocking it dampens drug-seeking and the misery of withdrawal — a target for new addiction therapies."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Chronic opioids quietly switch off the stress axis: they suppress ACTH and cortisol output, causing an opioid-induced adrenal insufficiency that can leave users dangerously unable to mount a stress response."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Opioids inflame the brain that craves them: morphine activates microglial TLR4 and the NLRP3 inflammasome, releasing IL-1β that paradoxically drives tolerance, hyperalgesia, and dependence — a neuroinflammatory side to addiction."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Opioids make mast cells leak histamine: morphine triggers non-immune mast-cell degranulation, producing the itch, flushing, and occasional hypotension seen with use — a pharmacological quirk distinct from true allergy."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Long-term opioids thin the bones: by suppressing gonadal hormones (opioid-induced hypogonadism) and disturbing bone turnover, chronic use lowers bone density and raises fracture risk, an under-recognized harm of maintenance opioids."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Opioids inflame the glia that fight them: chronic opioids activate microglial TLR4-NF-κB signaling, driving the neuroinflammation behind tolerance and paradoxical hyperalgesia that undermines long-term pain control."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The needle is a gateway to the bloodstream: non-sterile injection seeds skin, heart valves and blood with bacteria, so abscesses, endocarditis and sepsis are among the commonest serious infections of injection opioid use."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Injection can carry a fungus into the blood: contaminated injection drug use causes Candida bloodstream infection that seeds the eyes and heart valves, the classic candidemia and endophthalmitis of injection drug users."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Repeated injection scars and clots the veins: groin and limb injection causes deep-vein thrombosis and septic thrombophlebitis, and the venous damage of injection opioid use raises pulmonary embolism risk."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Overdose and infection injure the kidney: rhabdomyolysis from prolonged unconsciousness during overdose causes acute kidney injury, and injection-related infections and amyloidosis can leave chronic kidney disease."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety drives and follows the use: generalized anxiety commonly co-occurs with opioid use disorder, both as a reason people self-medicate and as a feature of withdrawal that perpetuates the cycle."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Injection breaks and infects the skin: non-sterile injection causes abscesses, cellulitis and necrotizing soft-tissue infections, leaving chronic wounds that heal poorly in often malnourished users."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Injection seeds the heart valves: injection drug use causes infective endocarditis that destroys heart valves, and the resulting valvular regurgitation can drive heart failure."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Injected tablet fillers lodge in the lungs: injecting crushed oral opioids introduces talc and other particulates that embolize to the pulmonary vasculature, causing granulomatosis and pulmonary hypertension."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Injection wounds and infects the skin: injecting drugs causes abscesses, cellulitis, track marks and necrotising soft-tissue infections, with skin-popping leaving chronic ulcers and scarring."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Chronic opioids suppress the hormones: long-term opioid use causes opioid-induced androgen deficiency with hypogonadism and low libido, and can suppress the adrenal cortisol axis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Injection seeds bone and joint infection: bloodborne spread from injecting drugs causes vertebral osteomyelitis, discitis, epidural abscess and septic arthritis, serious deep musculoskeletal infections."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Injection and methadone threaten the heart: injecting drug use causes right-sided infective endocarditis, and methadone prolongs the QT interval, risking dangerous arrhythmias."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Opioids themselves suppress immunity: opioid receptors on immune cells blunt their function, so opioid use disorder weakens host defence on top of the infections that injecting introduces."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Repeated injection wrecks the lymphatics: 'puffy hand syndrome' is a chronic, disfiguring lymphoedema of the hands and forearms from injection damage to lymphatic vessels in long-term users."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It reaches the kidney through the muscle: opioid overdose causes prolonged immobility and rhabdomyolysis with acute kidney injury, and heroin use is linked to a focal segmental glomerulosclerosis."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Shared needles spread blood-borne virus: alongside hepatitis C and HIV, hepatitis B is transmitted by injecting drug use, making vaccination and harm-reduction central to care."
  - target: 02-pathogen/02-bacteria/clostridium-tetani
    relation: connects-to
    note: "Contaminated injection seeds soil organisms: 'skin-popping' and dirty needles expose injectors to tetanus and wound botulism from Clostridium spores, a re-emerging cause of severe illness."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "The epidemic's biggest driver: injection opioid use is now the leading cause of new hepatitis C infections, though direct-acting antivirals can cure it once people are reached and treated."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Stress drives the relapse: corticotropin-releasing hormone and the noradrenergic stress system mediate opioid withdrawal distress and craving, a major force behind relapse in opioid use disorder."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "Shared reward wiring links them: opioid use disorder and binge eating both hijack the mu-opioid and dopamine reward system, and the opioid antagonist naltrexone is used against both."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "Injecting seeds the heart valves: injection drug use carries skin bacteria like Staphylococcus aureus to the heart, causing infective endocarditis — classically right-sided on the tricuspid valve — a major cause of OUD hospitalisation and death."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Polysubstance use is the rule: opioid and cannabis use disorders frequently co-occur, and cannabis is debated both as a relapse risk and as a harm-reduction aid during opioid tapering."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Overdose silences the breath: opioids suppress the brainstem respiratory drive, and overdose causes hypoventilation, aspiration and noncardiogenic pulmonary oedema flooding the alveoli — the proximate cause of opioid death that naloxone reverses."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Methadone and the QT interval: methadone blocks the hERG potassium channel and prolongs the QT interval, risking torsades de pointes—the reason ECG monitoring accompanies opioid agonist therapy."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The constipation no one escapes: mu-opioid receptors on the gut wall slow intestinal motility, causing the near-universal constipation of chronic opioid use, treated with peripherally-acting opioid antagonists."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Mood and opioids entangle: opioid use disorder is highly comorbid with bipolar disorder, with self-medication of mood swings and shared impulsivity and reward-circuit dysfunction driving the overlap."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Needle-borne infection: injection opioid use spreads hepatitis B alongside hepatitis C and HIV through shared needles, so chronic HBV and its liver disease are common in this population."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Deep infections of bone: injection drug use seeds vertebral osteomyelitis, discitis and septic arthritis, infections that erode the cortical bone and are notoriously hard to clear."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A pandemic of overdose: opioid overdose deaths surged during COVID-19 from disrupted services and isolation, while opioid respiratory depression compounds the lung injury of severe infection."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Injection, homelessness and TB: injection drug use, congregate housing and HIV coinfection raise the risk of tuberculosis and complicate adherence to its long treatment."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Heroin nephropathy: chronic injection drug use causes a collapsing FSGS-like glomerulopathy and, with skin-popping, AA amyloidosis—both injuring the glomerulus toward kidney failure."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Emboli and hypoxia: septic emboli from injection-related endocarditis cause ischaemic and mycotic-aneurysm strokes, while opioid overdose can leave hypoxic-ischaemic brain injury."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Glial neuroinflammation: opioids activate microglia to release TNF-α, neuroinflammation that paradoxically worsens pain (hyperalgesia) and drives tolerance and dependence."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory signalling: chronic opioid exposure raises IL-6, contributing to the glial activation and immune dysregulation that accompany dependence and withdrawal."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Stress axis in withdrawal: opioid withdrawal activates the HPA axis with surging cortisol, driving the dysphoria and physiological distress that fuel relapse."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Glial opioid signalling: opioids activate microglial TLR4 independent of the classical receptor, driving the neuroinflammation that underlies tolerance, opioid-induced hyperalgesia and reward potentiation."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Mood and withdrawal: serotonergic dysregulation contributes to the dysphoria, anxiety and depression of opioid withdrawal and the high comorbidity of mood disorders in opioid use disorder."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Opioid histamine release: many opioids trigger mast-cell histamine release, causing the pruritus, flushing and hypotension that accompany their use and the itch that marks intoxication."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Neuroinflammatory tolerance: CCL2 recruits monocytes and activates microglia in opioid exposure, part of the neuroinflammation that, alongside TLR4 signalling, drives opioid tolerance and dependence."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Reward-signalling node: dopamine D2-receptor signalling converges on GSK-3β, a kinase governing the synaptic plasticity of reward learning implicated in the compulsive drug-seeking of opioid use disorder."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Withdrawal stress: the anxiolytic neuropeptide Y system is dysregulated in opioid withdrawal, contributing to the anxiety, dysphoria and stress reactivity that drive relapse during abstinence."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Anti-craving neuropeptide: oxytocin dampens stress and reward signalling and reduces drug craving and withdrawal severity in models, an endogenous social-bonding system being studied as an adjunct to reduce relapse in opioid use disorder."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Endocrine effect: opioids suppress GnRH and raise prolactin, producing the hyperprolactinaemia and hypogonadism — low testosterone, reduced libido, menstrual disruption — that are common, under-recognised complications of chronic opioid use."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Reward enhancement: ghrelin amplifies the dopaminergic reward response to opioids and other drugs, a gut-derived hormone that increases drug reward and relapse vulnerability, linking appetite and addiction circuitry."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Reward plasticity: mu-opioid-receptor activation drives ERK-MAPK signalling in the reward circuitry, the synaptic plasticity underlying opioid reward, tolerance and the entrenched drug-seeking of opioid use disorder."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Dependence neuroadaptation: opioid signalling through the AKT-GSK3β axis (GSK3β already mapped) contributes to the neuroadaptations of dependence and to opioid-induced reward and analgesic tolerance."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Withdrawal stress: the cortisol/CRH stress response of opioid withdrawal (already mapped) acts through the glucocorticoid receptor, the HPA dysregulation that drives the dysphoria and relapse of opioid use disorder."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Glial activation: opioids engage microglial TLR4 that signals through MyD88 to NF-κB (TLR4 and NF-κB already mapped), driving the neuroinflammation that contributes to tolerance, hyperalgesia, and the reward dysregulation of opioid use disorder."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Addiction plasticity: mTOR-dependent synaptic plasticity in the mesolimbic reward circuit consolidates the maladaptive learning and drug-cue associations that entrench compulsive opioid use."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophic remodelling: BDNF signalling through its TrkB receptor (NTRK) mediates the reward-circuit synaptic remodelling that underlies opioid craving and the persistence of relapse vulnerability."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN regulation of the PI3K-AKT-mTOR axis (AKT, mTOR and GSK-3β mapped) shapes the reward-circuit synaptic plasticity underlying opioid addiction."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Opioid-driven microglial activation (TLR4 mapped) induces galectin-3, amplifying the neuroinflammation linked to opioid tolerance and dependence."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-driven JAK-STAT signalling (IL-6 mapped) transduces the neuroinflammatory milieu accompanying chronic opioid exposure and withdrawal."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling (JAK1/2 already mapped) transduces the neuroinflammatory tone implicated in the reward dysregulation of opioid use disorder."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the TLR4-associated glial neuroinflammation driven by chronic opioid exposure."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the interferon-associated microglial activation reported with chronic opioid exposure and withdrawal."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of the PTEN-PI3K-AKT axis (PTEN and AKT already mapped) regulates the neuronal plasticity and oxidative-stress handling relevant to the reward neuroadaptations of opioid use disorder."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to chronic opioid use disorder."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α responses to opioid-associated hypoxic and metabolic stress contribute to the neuroadaptations of opioid use disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) mediates the synaptic-plasticity neuroadaptations of the reward circuit in opioid use disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK metabolic signaling participates in the neuronal energetic adaptations of chronic opioid exposure in opioid use disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation in the reward circuit contributes to the persistent neuroadaptations and relapse vulnerability of opioid use disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal and reward-circuit homeostasis implicated in opioid use disorder."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the mu-opioid-receptor signaling and synaptic plasticity of opioid use disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with opioid use disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and reward-circuit processes implicated in opioid use disorder."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven neuroinflammation (glial activation) participates in the tolerance and dependence of opioid use disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory responses implicated in opioid use disorder."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with opioid use disorder."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the microglial and neuroinflammatory processes implicated in opioid use disorder."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the neuroadaptation and reward-circuit processes implicated in opioid use disorder."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tolerance mechanism: nitric oxide from neuronal nNOS drives the development of opioid tolerance and dependence through NMDA-linked signalling (glutamate already mapped), and blocking nNOS attenuates tolerance in models of opioid use."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences: estrogen modulates opioid reward and pain sensitivity, contributing to the sex differences in opioid use disorder susceptibility and treatment response beyond the testosterone axis already mapped."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Withdrawal insomnia: sleep and circadian disruption are prominent in opioid withdrawal and early recovery, and melatonin, the circadian sleep hormone, is studied as an adjunct for the insomnia that undermines abstinence."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Respiratory acidosis: opioid overdose depresses brainstem breathing, and the resulting carbon-dioxide and proton retention produce a respiratory acidosis that, with hypoxia, drives the fatal outcome reversed by naloxone."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Neuroimmune tolerance: opioids activate glia through TLR4 (already mapped), and the balance of pro-inflammatory cytokines against the anti-inflammatory IL-10 shapes the neuroinflammation implicated in opioid tolerance and hyperalgesia."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid modulation: progesterone and its metabolite allopregnanolone modulate opioid reward and withdrawal severity, contributing, with estrogen (already mapped), to the sex differences in opioid use disorder."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Glial hyperalgesia: prostaglandins from the opioid-activated glia (TLR4 already mapped) contribute to the neuroinflammation and the opioid-induced hyperalgesia and tolerance that complicate long-term opioid use."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative neuroinflammation: the glial activation and withdrawal stress of opioid use disorder generate oxidative stress, to which xanthine oxidase contributes, and the reactive oxygen species add to the neuroinflammation (NLRP3 already mapped) of tolerance."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Appetite-reward crosstalk: GLP-1 signalling links the gut-hormone (ghrelin already mapped) and reward pathways, and GLP-1 receptor agonists are being investigated to reduce the drug reward and craving of opioid use disorder."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the glial (microglia already mapped) pro-inflammatory cytokines (TNF, IL-6 and IL-1 already mapped) that drive the neuroinflammation of opioid tolerance."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium and tolerance: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) signalling that mediates opioid tolerance and withdrawal, and magnesium can attenuate these in opioid use disorder."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and opioid signalling: zinc modulates the mu-opioid receptor (already mapped) and NMDA signalling, and disturbed zinc status is linked to the mood and reward dysregulation of opioid use disorder."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Glial neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the opioid-glial (TLR4 already mapped) neuroinflammation of tolerance and dependence in opioid use disorder."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Injection endocarditis: the injection drug use of opioid use disorder causes right-sided infective endocarditis of the heart, a major and rising complication requiring prolonged antibiotics or surgery."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Blood-borne transmission: the injection drug use of opioid use disorder transmits hepatitis C (and HIV), a major public-health consequence driving the coinfection burden of the epidemic."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic adipokine: the chronic opioid use disrupts the leptin and energy balance (ghrelin already mapped) and the metabolic state, part of the neuroendocrine disturbance of opioid use disorder."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory milieu disturbed by the chronic opioid use."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the neuroinflammation (TNF and IL-6 already mapped) of opioid use disorder."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, contributes to the glial (microglia already mapped) neuroinflammation and the tolerance/hyperalgesia of opioid use disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune-inflammatory dimension (TNF and IL-1 already mapped) of chronic opioid use."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of opioid use disorder."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of chronic opioid use."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of opioid use disorder."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/mast-cell arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 dimension whose mast cells mediate the histamine (already mapped) release of opioid administration."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic opioid exposure of opioid use disorder."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Opioid-suppressed NK: the NK-cell number and cytotoxicity, suppressed by the chronic opioid exposure (mu-opioid receptor already mapped), are part of the immunosuppression of opioid use disorder."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the innate inflammatory dimension of the opioid-induced (TLR4 already mapped) neuroinflammation of opioid use disorder."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are part of the complement activation of the opioid-induced neuroinflammation of opioid use disorder."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the neuroinflammation of opioid use disorder."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the opioid-induced neuroinflammation of opioid use disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-gut axis: TSLP, from gut-epithelium (gut-microbiome already mapped) disrupted by the opioid-induced constipation and dysbiosis of opioid use disorder, primes mast cells (already mapped) and dendritic cells (already mapped) and amplifies the gut-brain neuroinflammation."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-neuroinflammatory axis: bradykinin, via B2R on CNS microglia (already mapped) and neurons (already mapped), modulates the neuroinflammation and the autonomic dysregulation contributing to the withdrawal hyperalgesia of opioid use disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor regulates the classical-complement and contact activation (C3 and C5 already mapped) contributing to the opioid-associated neuroinflammation and the microglial (already mapped) TLR4-driven immune dysregulation of opioid use disorder."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-opioid neuroprotection: erythropoietin and its receptor on neurons (already mapped) and microglia (already mapped) exert neuroprotective anti-apoptotic effects on the opioid-injured dopaminergic (dopamine already mapped) neurons of the reward circuitry."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "CNS-border ECM: periostin, from astrocytes (already mapped) and meningeal fibroblasts, contributes to the perivascular ECM remodelling and the neuroinflammation (IL-1b, IL-6 already mapped) of the opioid-remodelled reward circuitry of opioid use disorder."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Opioid-anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) common in opioid use disorder, driven by nutritional deficiency, anaemia, and the chronic inflammatory state of addiction."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "OUD vasopressin: vasopressin, via V1aR on neurons (already mapped) and microglia (already mapped), modulates HPA-axis (cortisol already mapped) tone; vasopressin dysregulation amplifies the CRH (already mapped) and norepinephrine (already mapped) cascade of opioid use disorder."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "OUD selenium: selenium, as neuroprotective GPx in neurons (already mapped) and microglia (already mapped), scavenges neuroinflammatory ROS; selenium deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of opioid use disorder."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "OUD iodine: iodine-dependent thyroid hormones regulate dopaminergic (dopamine already mapped) and serotonergic (serotonin already mapped) tone; iodine deficiency amplifies the HPA (cortisol already mapped) and CRH (already mapped) cascade of opioid use disorder."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "OUD sodium: sodium, via Na⁺/K⁺-ATPase on dopaminergic (dopamine already mapped) and glutamatergic (NMDA-receptor already mapped) neurons, maintains action-potential fidelity; sodium dysregulation amplifies the dopamine (already mapped) withdrawal cascade of opioid use disorder."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "OUD copper: copper, as cofactor of dopamine-β-hydroxylase, converts dopamine (already mapped) to norepinephrine (already mapped) and modulates the catecholamine cascade; copper dysregulation amplifies the HPA-axis (cortisol already mapped) tone of opioid use disorder."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "OUD potassium: potassium, via K⁺ channels on dopaminergic (dopamine already mapped) and GABAergic (GABA already mapped) neurons, sets membrane excitability; potassium dysregulation amplifies the withdrawal hyperalgesia of opioid use disorder."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "OUD calcium: calcium channel activation in neurons (already mapped) and microglia (already mapped) modulates opioid-dependent synaptic plasticity; calcium dysregulation by opioids amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of OUD."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "OUD phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and microglia (already mapped), sustains reward-circuit energy; phosphorus deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of opioid use disorder."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "OUD iron: iron, as cofactor of dopamine-β-hydroxylase in neurons (already mapped) and microglia (already mapped), supports dopaminergic reward tone; iron deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of OUD."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "OUD chloride: chloride, via KCC2 in GABAergic (GABA already mapped) interneurons of the reward circuit, sets inhibitory tone; chloride dysregulation amplifies NF-κB (already mapped) neuroinflammation and TNF-α (already mapped) withdrawal signalling in opioid use disorder."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "OUD nitrogen: nitrogen in amino-acid scaffold of opioid receptors (already mapped) and dopamine transporter proteins in neurons (already mapped) sustains reward-circuit signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of OUD."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "OUD sulfur: sulfur-containing amino acids sustain glutathione antioxidant defence in neurons (already mapped) and microglia (already mapped); sulfur deficiency amplifies NF-κB (already mapped) neuroinflammatory stress and TNF-α (already mapped) withdrawal cascade of OUD."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "OUD PD-1: PD-1 checkpoint expression on microglia (already mapped) and T-cells in the reward circuit modulates neuroinflammatory tone; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of opioid use disorder."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "OUD angiotensin-II: angiotensin-II in the mesolimbic dopamine (already mapped) circuit modulates stress-induced craving; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and CRH (already mapped) neuroinflammatory cascade of OUD."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "OUD VEGF: VEGF from microglia (already mapped) and astrocytes sustains neuroplasticity in dopamine (already mapped) reward circuits; VEGF dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of opioid use disorder."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "OUD WNT/β-catenin: WNT/β-catenin signalling in dopamine (already mapped) neurons supports synaptic plasticity; WNT dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and CRH (already mapped) reward-circuit cascade of opioid use disorder."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "OUD glp-1: GLP-1 from enteroendocrine cells (already mapped) and microglia (already mapped) modulates mesolimbic dopamine reward tone; glp-1 dysfunction amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "OUD rankl: RANKL from macrophages (already mapped) and microglia (already mapped) promotes neuroinflammatory immune activation in opioid circuits; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "OUD smad4: SMAD4 in neurons (already mapped) and astrocytes (already mapped) mediates TGF-β neuroplasticity repair; smad4 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "OUD il-2: IL-2 from T-cells (already mapped) and microglia (already mapped) regulates neuroinflammatory surveillance in opioid circuits; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "OUD fibronectin: fibronectin in neurons (already mapped) and astrocytes (already mapped) promotes CNS ECM remodelling in opioid circuits; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "OUD notch: Notch signalling in neurons (already mapped) and astrocytes (already mapped) regulates glial fate in opioid circuits; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "OUD igf-1: IGF-1 from neurons (already mapped) and astrocytes (already mapped) promotes opioid-circuit neuroprotection; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "OUD activin-a: activin-A from neurons (already mapped) and astrocytes (already mapped) modulates opioid-circuit neuroinflammatory tone; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "OUD tgf-beta: TGF-β from neurons (already mapped) and astrocytes (already mapped) drives opioid-circuit glial remodelling; tgf-beta excess amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD."
---

# Opioid Use Disorder

## Overview

**Opioid use disorder (OUD)** is a chronic, relapsing condition characterized by compulsive opioid use despite harmful consequences. It represents one of the most lethal substance use disorders: in the US, opioid-related overdose deaths have risen to approximately **80,000/year** (2022), primarily driven by illicitly manufactured fentanyl and fentanyl analogs — a 9-fold increase since 1999 and now the leading cause of death in Americans aged 18–45.

**Epidemiology:**
- ~2.7 million Americans with OUD (DSM-5); global opioid misuse ~56 million
- Heroin use disorder: ~750,000; prescription opioid use disorder: ~2 million; overlap significant
- Fentanyl now present in >80% of heroin samples in the US — most overdose deaths involve fentanyl
- Overdose mortality: ~80,000/year US (2022); naloxone has reversed >300,000 overdoses
- Treatment gap: Only ~20% of people with OUD receive medication-assisted treatment (MOUD)

**Opioids of abuse:**
- **Heroin:** Diacetylmorphine; rapid onset IV/nasal → euphoria; short half-life (~3h) → withdrawal within 6-12h
- **Fentanyl:** 50-100× more potent than morphine; illicit supply ("pressed pills") has replaced heroin; carfentanil (10,000× morphine): veterinary agent used as adulterant
- **Prescription opioids:** Oxycodone (OxyContin), hydrocodone (Vicodin), oxymorphone, hydromorphone, morphine; diverted or obtained via pill mills
- **Buprenorphine:** Partial agonist; used for treatment; ceiling effect on respiratory depression
- **Methadone:** Full agonist; used for treatment; long half-life; QTc risk

**DSM-5 Criteria:** Same 11-criterion framework as AUD, applied to opioids; ≥2 in 12 months; physiological indicators (tolerance, withdrawal) count toward mild even when prescribed medically (with important caveats for pain management patients).

**COWS (Clinical Opioid Withdrawal Scale):** 11-item bedside tool (heart rate, sweating, gooseflesh, pupil size, yawning, anxiety, GI, tremor, restlessness, bone/joint ache, cold/hot flashes); score 5-12: mild; 13-24: moderate; 25-36: moderately severe; ≥37: severe.

## Structure

### Opioid receptor biology

**Three main opioid receptor subtypes (GPCRs):**

| Receptor | Gene | Coupling | Endogenous ligands | Key locations | Effects |
|:---|:---|:---|:---|:---|:---|
| **μ (MOR)** | OPRM1 | Gi/Go → ↓cAMP, GIRK K⁺, ↓VGCC | β-endorphin, endomorphin | VTA, NAcc, LC, amygdala, PAG, dorsal horn | Euphoria, analgesia, respiratory depression |
| **κ (KOR)** | OPRK1 | Gi → ↓cAMP | Dynorphin | Striatum, limbic system, spinal cord | Dysphoria, analgesia, psychomimetic effects |
| **δ (DOR)** | OPRD1 | Gi | Enkephalins | Cortex, basal ganglia, limbic | Mood, reward, analgesia |

**MOR signaling (Gi-coupled):**
1. Inhibits adenylyl cyclase → ↓cAMP → reduced PKA activity
2. Activates GIRK K⁺ channels → hyperpolarization → reduced neuronal firing
3. Inhibits voltage-gated Ca²⁺ channels → reduced neurotransmitter release
4. **Arrestin pathway:** β-arrestin recruitment → receptor desensitization → endocytosis → tolerance

### VTA disinhibition mechanism

The primary mechanism by which opioids produce euphoria:

1. **Baseline:** GABAergic interneurons in VTA tonically suppress DA neuron firing via MOR on GABA interneurons
2. **Opioid administration:** MOR activation on GABA interneurons → Gi → hyperpolarizes GABA interneurons → reduces GABA release → VTA DA neurons are **disinhibited** → increased firing
3. **NAcc:** Elevated VTA DA firing → increased NAcc DA release → D1/D2 stimulation → euphoria, reinforcement
4. **Acute effect:** High-amplitude DA surge (heroin/fentanyl) >> natural rewards → powerful positive reinforcement

### Tolerance and dependence mechanisms

**Tolerance:**
- Chronic MOR activation → GRK (G protein-coupled receptor kinase) phosphorylation → β-arrestin recruitment → MOR desensitization and internalization
- Adenylyl cyclase **superactivation** (compensatory upregulation) → elevated cAMP baseline; requires increasing doses to achieve same inhibition
- Results in the same MOR-activating dose producing progressively less effect

**Physical dependence and withdrawal:**
- **LC hyperactivation:** During opioid use, MOR on LC neurons → Gi → suppressed cAMP → suppressed LC firing → reduced NE; adenylyl cyclase superactivation occurs; abrupt cessation → cAMP surge → LC hyperactivation → NE storm → withdrawal syndrome
- Withdrawal timeline:
  - **Short-acting opioids (heroin, oxycodone):** Onset 6-12h after last use; peak 36-72h; resolution 5-7 days
  - **Long-acting opioids (methadone):** Onset 24-48h; peak 72-96h; resolution 10-21 days

**Opioid overdose mechanism:**
- MOR in brainstem (pre-Bötzinger complex): respiratory rhythm generator; MOR activation → hyperpolarization → respiratory depression → death
- **Fentanyl:** Highly lipophilic → rapid CNS penetration → faster respiratory depression than heroin; multiple doses of naloxone often required
- **Naloxone (Narcan):** Competitive MOR antagonist; 2-8 mg intranasal or 0.4-2 mg IM; onset 1-2 min; duration 30-90 min (shorter than fentanyl) → repeat dosing required

## Function

### Reward circuit alterations in OUD

**Positive reinforcement → Negative reinforcement transition (Koob model):**

**Early OUD (positive reinforcement):**
- Opioid → VTA DA disinhibition → NAcc DA surge → euphoria ("high")
- Extended amygdala NOT yet dominant; goal is to achieve pleasure

**Chronic OUD (negative reinforcement — more clinically important):**
- Reward threshold rises (tolerance); same dose produces less euphoria
- Abstinence → **withdrawal dysphoria** — anhedonia, anxiety, dysphoria (kappa-opioid-mediated dynorphin release from NAcc neurons suppresses dopamine)
- **Drinking/using to feel normal** — not for pleasure but to avoid withdrawal
- CRF hyperactivation in CeA (similar to AUD) → anxiety drives opioid-seeking
- This shift from positive to negative reinforcement explains why "willpower" fails — the drug is maintaining homeostasis, not causing pleasure

**Craving and relapse (PFC-limbic imbalance):**
- Drug cues (paraphernalia, people, places) activate OFC → craving → impaired PFC inhibitory control
- Glutamatergic corticostriatal projections are potentiated by chronic opioid use → drug-cue reactivity persists for years
- PFC (dlPFC) hypofunction → impaired inhibitory control over limbic drive
- NAcc glutamate (from PFC/amygdala) during cue exposure triggers reinstatement

## Pathology

### Opioid-related complications

| Complication | Mechanism/Notes |
|:---|:---|
| **Overdose** | Respiratory depression via MOR on pre-Bötzinger; fentanyl: multiple naloxone doses; skin-popping → abscesses |
| **Infective endocarditis** | IV drug use → bacteremia; tricuspid valve most common; Staph aureus; high mortality if untreated |
| **Hepatitis C (HCV)** | Transmitted via needle sharing; 50-80% of PWID (people who inject drugs) HCV-seropositive; DAA therapy (ledipasvir, sofosbuvir) highly effective |
| **HIV** | Needle sharing; 10% of new HIV diagnoses in US linked to injection drug use |
| **Skin and soft tissue infections** | Abscesses, necrotizing fasciitis, wound botulism |
| **Neonatal opioid withdrawal syndrome (NOWS)** | In utero opioid exposure → withdrawal after birth; managed with morphine or methadone; prolonged NICU stays |
| **Opioid-induced hyperalgesia** | Paradoxical increased pain sensitivity with chronic opioid; NR2B NMDA receptor sensitization |
| **Constipation** | Peripheral MOR in GI → reduced motility; methylnaltrexone (peripherally restricted MOR antagonist) treats opioid-induced constipation |

### Treatment — MOUD (Medications for OUD)

**Evidence base:** MOUD reduces opioid use, overdose mortality (~50-70%), HIV/HCV transmission, crime, and improves social functioning [^mattick-2009-bupe-meta].

**Buprenorphine:**
- Partial μ-agonist + κ-antagonist; ceiling effect on respiratory depression (much safer than full agonists)
- **Suboxone** (buprenorphine + naloxone): naloxone prevents IV misuse — inactive sublingually, precipitates withdrawal if injected
- Sublingual or buccal; weekly/monthly injectable (Sublocade) and implants (Probuphine) available
- **Induction:** Start when COWS ≥8-12 (mild-moderate withdrawal); premature induction → precipitated withdrawal; modified low-dose induction (Bernese method) allows starting without prior withdrawal
- Superior to methadone for patient autonomy (office-based); no QTc risk

**Methadone:**
- Full μ-agonist; long half-life (24-36h) → smooth opioid maintenance without peaks
- Dispensed from federally licensed opioid treatment programs (OTPs) — requires daily attendance initially
- QTc prolongation (baseline ECG required); drug interactions via CYP3A4
- Highly effective for severe OUD, patients who fail buprenorphine, or pregnant women (reduces NOWS severity vs. illicit use)

**Naltrexone (extended-release injectable, Vivitrol):**
- Competitive MOR antagonist; monthly injection → ~100% compliance during injection period
- No abuse potential; no dependency; no diversion risk
- Requires opioid-free period (7 days short-acting; 10-14 days long-acting/methadone) before induction — barrier in US system
- Equally effective to buprenorphine when initiated; inferior retention rate due to induction challenge

**Naloxone (harm reduction):**
- Broad OTC availability (US 2023); co-prescribed with opioids; community distribution programs
- 4mg IN formulation (Narcan); 8mg IN (Kloxxado) for fentanyl; 10mg autoinjector
- Take-home naloxone programs: 2-3 doses recommended given high fentanyl naloxone resistance

**Psychosocial treatments:**
- **Contingency management (CM):** Voucher-based or monetary incentives for opioid-negative urine screens; strongest evidence base in SUD treatment (effect sizes d=0.5-0.8); not widely implemented due to funding barriers
- **Motivational interviewing (MI):** Enhances readiness to engage in treatment
- **12-step (NA, Narcotics Anonymous):** Abstinence-only model; limited evidence vs. MOUD; some conflict between NA culture and MOUD acceptance
- **Recovery housing:** Peer support; medication-friendly environments reduce relapse risk

**Harm reduction (beyond naloxone):**
- Syringe services programs (SSPs): Reduce HIV/HCV; link to treatment; legally complex
- Supervised consumption sites (SCS): North America (Vancouver, Toronto, New York 2021); no overdose deaths on site; reduce emergency department visits
- Fentanyl test strips: detect fentanyl contamination; reduce overdose risk; legal in most US states
- Medication-assisted low-threshold access (vending machines, telemedicine prescribing): Increase treatment uptake

## Connections

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — μ-opioid receptor activation on VTA GABAergic interneurons → disinhibition → increased VTA DA firing → NAcc dopamine surge → euphoria; chronic use → reward hypofunction → anhedonia; naltrexone (MOR antagonist) blocks this disinhibition → reduces opioid reward.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — μ-opioid receptors on VTA GABAergic interneurons mediate euphoric disinhibition; chronic opioid → tolerance at MOR on GABA interneurons; buprenorphine (partial MOR agonist) provides stable DA tone without the high-reinforcement surge of full agonists.

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — chronic opioid potentiates corticostriatal glutamatergic synapses → LTP underlying craving and drug-cue reactivity; AMPA receptor upregulation in NAcc drives relapse-associated excitability; mGluR5 antagonists reduce cue-triggered reinstatement of opioid seeking in rodents.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — chronic opioid drives ΔFosB accumulation in NAcc → altered BDNF expression and reward circuit plasticity; BDNF in VTA sensitizes opioid-induced reinforcement; withdrawal-phase BDNF surge in NAcc contributes to aversion; BDNF/TrkB signaling is a therapeutic target in relapse prevention.

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — μ-opioid receptors on LC suppress NE during opioid use; abrupt cessation → LC rebound → excess NE → withdrawal (diaphoresis, piloerection, tachycardia, diarrhea, anxiety); clonidine and lofexidine (α2 agonists) reduce LC hyperactivation and are FDA-approved for opioid withdrawal.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — OUD remodels VTA-NAcc reward circuits (MOR disinhibition), LC (NE rebound withdrawal), PFC control circuits (craving-driven approach behavior), and amygdala (conditioned fear of withdrawal); buprenorphine and naltrexone normalize these circuit abnormalities over months of treatment.

- `connects-to` → **[Mu-Opioid Receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Opioid use disorder centers on the μ-opioid receptor: on VTA GABA interneurons it disinhibits dopamine, on the locus coeruleus it sets up rebound withdrawal, and in the brainstem it drives respiratory depression — the target of buprenorphine, methadone, and naloxone.

- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Injecting opioids seeds the bloodstream with skin and needle bacteria, which lodge on heart valves — classically the tricuspid — to cause infective endocarditis, a high-mortality complication of injection drug use that may need valve surgery alongside OUD treatment.

- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Opioid and stimulant use disorders share the VTA-NAcc dopamine reward circuitry but pull in opposite directions, and are increasingly fatal together: 'speedball' combinations and fentanyl-contaminated stimulants drive a rising share of overdose deaths.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Injection opioid use is the leading driver of hepatitis C transmission: shared needles spread HCV efficiently and people with OUD carry a high HCV burden; opioid agonist therapy, syringe services and direct-acting antivirals (treatment-as-prevention) are the combined response.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Injection opioid use spreads HIV through shared needles, and OUD also raises sexual transmission risk; harm reduction (syringe services, naloxone), opioid agonist therapy and antiretrovirals/PrEP intersect here, and untreated OUD undermines HIV care and viral suppression.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Opioid and alcohol use disorders frequently co-occur and are dangerous together: both are CNS depressants, so combined use multiplies respiratory depression and overdose death; they share reward and stress circuitry, and concurrent alcohol complicates opioid agonist therapy.
- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — Opioid and gambling disorders share the brain's opioid-modulated reward system: the endogenous opioid system shapes the high of both substance and behavioral addiction, which is why the antagonist naltrexone treats alcohol and opioid dependence and also curbs gambling urges.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Chronic pain is a major gateway to opioid use disorder: opioids prescribed for neuropathic and other chronic pain can lead to tolerance, dependence, and addiction—yet they work poorly for neuropathic pain, so anticonvulsants and antidepressants are preferred.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Opioid use disorder rewires reward and stress neurons: repeated mu-opioid stimulation of mesolimbic dopamine neurons drives tolerance and dependence, while withdrawal activates stress circuits—so the neural adaptations, not just the drug, sustain craving and relapse.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Respiratory depression is how opioids kill: mu-receptor activation in brainstem respiratory centers blunts the drive to breathe, so overdose causes fatal hypoventilation—the mechanism naloxone reverses and the reason fentanyl's potency makes overdose so lethal.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Opioid use disorder and depression are tightly intertwined: depression drives self-medication while chronic opioid use dysregulates reward and worsens mood, and withdrawal mimics depression—so the two conditions amplify each other and complicate treatment.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Opioids harm the lung beyond overdose: sedation promotes aspiration pneumonia, overdose can cause non-cardiogenic pulmonary edema, and injection use seeds septic emboli—so the lung suffers both acute and chronic complications of opioid use.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — Opioid and endocannabinoid systems are deeply interlinked: both engage the brain's reward and pain circuits and their receptors interact, so cannabinoids modulate opioid reward and withdrawal—part of why self-medication patterns are common in OUD.
- `connects-to` → **[PTSD](../ptsd/README.md)** — PTSD and opioid use disorder are tightly bound: people with PTSD use opioids to numb hyperarousal and emotional pain, raising the risk of dependence, while the chaos of addiction generates new trauma—so trauma-focused care is key to treating OUD.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Opioid use disorder rewires the nervous system: repeated mu-receptor stimulation downregulates reward circuits and upregulates stress pathways, so tolerance, craving and a brutal withdrawal are neuroadaptations—addiction as a chronic brain disease, not a moral failing.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Opioid use in pregnancy crosses the placenta: the fetus becomes dependent in utero and, after birth, suffers neonatal abstinence syndrome with tremor, irritability, and feeding problems—so opioid use disorder in pregnancy needs careful, supervised treatment.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Injection opioid use invites Staphylococcus aureus: non-sterile injecting seeds the bloodstream with S. aureus (often MRSA), causing skin abscesses, endocarditis, and bone infections—among the most dangerous medical complications of opioid use disorder.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Opioids profoundly slow the gut: mu-receptors on the bowel cause opioid-induced constipation, the most persistent side effect, since unlike other opioid effects it does not wane with tolerance—so laxatives and PAMORA drugs are routine in chronic use.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Opioid overdose kills by letting carbon dioxide build up: opioids suppress the brainstem's CO2-driven breathing reflex, so respiration slows until hypercapnia and hypoxia stop the heart—the mechanism naloxone reverses by displacing the drug.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Injection opioid use endangers the liver: shared needles transmit hepatitis C (and B), making chronic liver disease and cirrhosis common in opioid use disorder—so liver screening and HCV treatment are part of care.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Opioids wreck sleep both ways: they fragment sleep architecture and suppress breathing during it, while withdrawal causes severe insomnia—so disturbed sleep both drives continued use and complicates recovery.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Opioid overdose kills by cutting off oxygen: opioids suppress the brainstem's drive to breathe, so breathing slows and stops, starving the brain and heart of oxygen—the hypoxia that naloxone races to reverse.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Opioid addiction rewires reward synapses: repeated drug surges strengthen and reshape connections in the dopamine pathway, the lasting synaptic plasticity that entrenches craving and makes relapse easy long after the drug is gone.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Opioids inflame the brain's immune cells: they activate microglia that release cytokines, which paradoxically worsen pain sensitivity and tolerance, so this neuroinflammation helps push escalating doses and dependence.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Opioids seize up the large intestine: mu-receptors in the gut wall halt its muscular waves, causing the severe constipation that nearly every opioid user gets and that special gut-targeted drugs are made to relieve.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — An opioid overdose floods the blood with hydrogen ions: suppressed breathing lets carbon dioxide build up into a respiratory acidosis, the falling pH that compounds the hypoxia of overdose.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Opioid addiction enlists astrocytes: these glial cells help control glutamate in the reward circuit, and their changes contribute to the synaptic plasticity and craving that sustain dependence and relapse.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Brain imaging reveals opioids' grip: fMRI photons show the reward circuit firing to drug cues, and MRI can expose the anoxic brain injury left by a survived overdose.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Injection opioid use infects the endothelium: shared needles seed bacteria onto heart-valve and vessel-lining endothelial cells, causing the infective endocarditis that is a major killer in the epidemic.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Injection drug use scars and infects the skin: track marks, abscesses and cellulitis from non-sterile injection are common, sometimes the first visible clue to hidden opioid use.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — An overdose can wreck the kidneys: lying unconscious and immobile crushes muscle into rhabdomyolysis, and the released myoglobin floods the renal tubules, a common cause of acute kidney injury after a heroin overdose.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Overdose stupor can crush the nerves: hours spent motionless and unrousable compress peripheral nerves against bone, leaving the wrist-drop or foot-drop palsies that linger after the opioid wears off.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Injection seeds clots on the heart's valves: bacteria delivered straight into the blood build platelet-fibrin vegetations of infective endocarditis, which break off as septic emboli to the lungs, brain, and beyond.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The pupils give opioids away: by acting on the brainstem, they constrict the pupils to pinpoint miosis — a hallmark sign of intoxication and overdose that reverses dramatically when naloxone is given.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Chronic opioids switch off the sex hormones: they suppress the hypothalamic-pituitary-gonadal axis, dropping testosterone into an opioid-induced hypogonadism with low libido, fatigue, infertility, and bone loss.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Opioids stall the gut from the top: they trigger nausea and vomiting through the brainstem and slow gastric emptying, the upper-GI counterpart to the relentless constipation they cause lower down.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Dependence reaches the next generation: opioid use in pregnancy causes neonatal abstinence syndrome — a withdrawing newborn — and chronic use disrupts menstruation and fertility, making reproductive care part of treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — A vaccine is being built against the high: anti-opioid vaccines raise antibodies that bind fentanyl or heroin in the blood before they reach the brain, an experimental approach to blunt overdose and relapse.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Opioids reshape the gut's flora: by slowing transit and acting on gut opioid receptors they foster dysbiosis and a leaky barrier, and the altered microbiome may in turn influence tolerance and withdrawal.
- `connects-to` → **[HIV](../hiv/README.md)** — Injection use drives the HIV epidemic: shared needles transmit the virus, so opioid use disorder is a leading route of HIV spread, and needle exchange and treatment of addiction are core HIV-prevention tools.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Orexin fuels the craving and the withdrawal: this arousal-and-reward peptide is recruited by chronic opioids, and blocking it dampens drug-seeking and the misery of withdrawal — a target for new addiction therapies.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Chronic opioids quietly switch off the stress axis: they suppress ACTH and cortisol output, causing an opioid-induced adrenal insufficiency that can leave users dangerously unable to mount a stress response.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Opioids inflame the brain that craves them: morphine activates microglial TLR4 and the NLRP3 inflammasome, releasing IL-1β that paradoxically drives tolerance, hyperalgesia, and dependence — a neuroinflammatory side to addiction.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Opioids make mast cells leak histamine: morphine triggers non-immune mast-cell degranulation, producing the itch, flushing, and occasional hypotension seen with use — a pharmacological quirk distinct from true allergy.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Long-term opioids thin the bones: by suppressing gonadal hormones (opioid-induced hypogonadism) and disturbing bone turnover, chronic use lowers bone density and raises fracture risk, an under-recognized harm of maintenance opioids.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Opioids inflame the glia that fight them: chronic opioids activate microglial TLR4-NF-κB signaling, driving the neuroinflammation behind tolerance and paradoxical hyperalgesia that undermines long-term pain control.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The needle is a gateway to the bloodstream: non-sterile injection seeds skin, heart valves and blood with bacteria, so abscesses, endocarditis and sepsis are among the commonest serious infections of injection opioid use.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Injection can carry a fungus into the blood: contaminated injection drug use causes Candida bloodstream infection that seeds the eyes and heart valves, the classic candidemia and endophthalmitis of injection drug users.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Repeated injection scars and clots the veins: groin and limb injection causes deep-vein thrombosis and septic thrombophlebitis, and the venous damage of injection opioid use raises pulmonary embolism risk.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Overdose and infection injure the kidney: rhabdomyolysis from prolonged unconsciousness during overdose causes acute kidney injury, and injection-related infections and amyloidosis can leave chronic kidney disease.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety drives and follows the use: generalized anxiety commonly co-occurs with opioid use disorder, both as a reason people self-medicate and as a feature of withdrawal that perpetuates the cycle.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Injection breaks and infects the skin: non-sterile injection causes abscesses, cellulitis and necrotizing soft-tissue infections, leaving chronic wounds that heal poorly in often malnourished users.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Injection seeds the heart valves: injection drug use causes infective endocarditis that destroys heart valves, and the resulting valvular regurgitation can drive heart failure.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Injected tablet fillers lodge in the lungs: injecting crushed oral opioids introduces talc and other particulates that embolize to the pulmonary vasculature, causing granulomatosis and pulmonary hypertension.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Injection wounds and infects the skin: injecting drugs causes abscesses, cellulitis, track marks and necrotising soft-tissue infections, with skin-popping leaving chronic ulcers and scarring.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Chronic opioids suppress the hormones: long-term opioid use causes opioid-induced androgen deficiency with hypogonadism and low libido, and can suppress the adrenal cortisol axis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Injection seeds bone and joint infection: bloodborne spread from injecting drugs causes vertebral osteomyelitis, discitis, epidural abscess and septic arthritis, serious deep musculoskeletal infections.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Injection and methadone threaten the heart: injecting drug use causes right-sided infective endocarditis, and methadone prolongs the QT interval, risking dangerous arrhythmias.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Opioids themselves suppress immunity: opioid receptors on immune cells blunt their function, so opioid use disorder weakens host defence on top of the infections that injecting introduces.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Repeated injection wrecks the lymphatics: 'puffy hand syndrome' is a chronic, disfiguring lymphoedema of the hands and forearms from injection damage to lymphatic vessels in long-term users.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It reaches the kidney through the muscle: opioid overdose causes prolonged immobility and rhabdomyolysis with acute kidney injury, and heroin use is linked to a focal segmental glomerulosclerosis.
- `connects-to` → **[Hepatitis B virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Shared needles spread blood-borne virus: alongside hepatitis C and HIV, hepatitis B is transmitted by injecting drug use, making vaccination and harm-reduction central to care.
- `connects-to` → **[Clostridium tetani](../../../02-pathogen/02-bacteria/clostridium-tetani/README.md)** — Contaminated injection seeds soil organisms: 'skin-popping' and dirty needles expose injectors to tetanus and wound botulism from Clostridium spores, a re-emerging cause of severe illness.
- `connects-to` → **[Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md)** — The epidemic's biggest driver: injection opioid use is now the leading cause of new hepatitis C infections, though direct-acting antivirals can cure it once people are reached and treated.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Stress drives the relapse: corticotropin-releasing hormone and the noradrenergic stress system mediate opioid withdrawal distress and craving, a major force behind relapse in opioid use disorder.
- `connects-to` → **[Binge-Eating Disorder](../binge-eating-disorder/README.md)** — Shared reward wiring links them: opioid use disorder and binge eating both hijack the mu-opioid and dopamine reward system, and the opioid antagonist naltrexone is used against both.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — Injecting seeds the heart valves: injection drug use carries skin bacteria like Staphylococcus aureus to the heart, causing infective endocarditis — classically right-sided on the tricuspid valve — a major cause of OUD hospitalisation and death.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Polysubstance use is the rule: opioid and cannabis use disorders frequently co-occur, and cannabis is debated both as a relapse risk and as a harm-reduction aid during opioid tapering.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Overdose silences the breath: opioids suppress the brainstem respiratory drive, and overdose causes hypoventilation, aspiration and noncardiogenic pulmonary oedema flooding the alveoli — the proximate cause of opioid death that naloxone reverses.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Methadone and the QT interval: methadone blocks the hERG potassium channel and prolongs the QT interval, risking torsades de pointes—the reason ECG monitoring accompanies opioid agonist therapy.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The constipation no one escapes: mu-opioid receptors on the gut wall slow intestinal motility, causing the near-universal constipation of chronic opioid use, treated with peripherally-acting opioid antagonists.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Mood and opioids entangle: opioid use disorder is highly comorbid with bipolar disorder, with self-medication of mood swings and shared impulsivity and reward-circuit dysfunction driving the overlap.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Needle-borne infection: injection opioid use spreads hepatitis B alongside hepatitis C and HIV through shared needles, so chronic HBV and its liver disease are common in this population.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Deep infections of bone: injection drug use seeds vertebral osteomyelitis, discitis and septic arthritis, infections that erode the cortical bone and are notoriously hard to clear.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A pandemic of overdose: opioid overdose deaths surged during COVID-19 from disrupted services and isolation, while opioid respiratory depression compounds the lung injury of severe infection.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Injection, homelessness and TB: injection drug use, congregate housing and HIV coinfection raise the risk of tuberculosis and complicate adherence to its long treatment.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Heroin nephropathy: chronic injection drug use causes a collapsing FSGS-like glomerulopathy and, with skin-popping, AA amyloidosis—both injuring the glomerulus toward kidney failure.
- `connects-to` → **[Stroke](../stroke/README.md)** — Emboli and hypoxia: septic emboli from injection-related endocarditis cause ischaemic and mycotic-aneurysm strokes, while opioid overdose can leave hypoxic-ischaemic brain injury.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Glial neuroinflammation: opioids activate microglia to release TNF-α, neuroinflammation that paradoxically worsens pain (hyperalgesia) and drives tolerance and dependence.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory signalling: chronic opioid exposure raises IL-6, contributing to the glial activation and immune dysregulation that accompany dependence and withdrawal.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Stress axis in withdrawal: opioid withdrawal activates the HPA axis with surging cortisol, driving the dysphoria and physiological distress that fuel relapse.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Glial opioid signalling: opioids activate microglial TLR4 independent of the classical receptor, driving the neuroinflammation that underlies tolerance, opioid-induced hyperalgesia and reward potentiation.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Mood and withdrawal: serotonergic dysregulation contributes to the dysphoria, anxiety and depression of opioid withdrawal and the high comorbidity of mood disorders in opioid use disorder.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Opioid histamine release: many opioids trigger mast-cell histamine release, causing the pruritus, flushing and hypotension that accompany their use and the itch that marks intoxication.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits monocytes and activates microglia during opioid exposure, part of the neuroinflammation that, alongside TLR4 signaling, drives the opioid tolerance and dependence that escalate use over time.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — Dopamine D2-receptor signaling converges on GSK-3β, a kinase governing the synaptic plasticity of reward learning implicated in the compulsive, craving-driven drug-seeking that defines opioid use disorder.
- `connects-to` → **[NPY](../../03-molecular/npy/README.md)** — The anxiolytic neuropeptide Y system is dysregulated in opioid withdrawal, contributing to the anxiety, dysphoria, and stress reactivity that drive relapse during abstinence and undermine recovery.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Oxytocin dampens stress and reward signaling and reduces drug craving and withdrawal severity in models, an endogenous social-bonding system being studied as an adjunct to reduce relapse in opioid use disorder.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Opioids suppress GnRH and raise prolactin, producing the hyperprolactinemia and hypogonadism—low testosterone, reduced libido, menstrual disruption—that are common, under-recognized complications of chronic opioid use.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Ghrelin amplifies the dopaminergic reward response to opioids and other drugs, a gut-derived hormone that increases drug reward and relapse vulnerability, linking appetite and addiction circuitry.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Mu-opioid-receptor activation drives ERK-MAPK signaling in the reward circuitry, the synaptic plasticity underlying opioid reward, tolerance and the entrenched drug-seeking of opioid use disorder.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Opioid signaling through the AKT-GSK3β axis (GSK3β already mapped) contributes to the neuroadaptations of dependence and to opioid-induced reward and analgesic tolerance.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — The cortisol/CRH stress response of opioid withdrawal (already mapped) acts through the glucocorticoid receptor, the HPA dysregulation that drives the dysphoria and relapse of opioid use disorder.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Opioids engage microglial TLR4 that signals through MyD88 to NF-κB (TLR4 and NF-κB already mapped), driving the neuroinflammation that contributes to tolerance, hyperalgesia, and the reward dysregulation of opioid use disorder.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-dependent synaptic plasticity in the mesolimbic reward circuit consolidates the maladaptive learning and drug-cue associations that entrench compulsive opioid use.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor (NTRK) mediates the reward-circuit synaptic remodeling that underlies opioid craving and the persistence of relapse vulnerability.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN regulation of the PI3K-AKT-mTOR axis (AKT, mTOR and GSK-3β mapped) shapes the reward-circuit synaptic plasticity underlying opioid addiction.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Opioid-driven microglial activation (TLR4 mapped) induces galectin-3, amplifying the neuroinflammation linked to opioid tolerance and dependence.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine-driven JAK-STAT signaling (IL-6 mapped) transduces the neuroinflammatory milieu accompanying chronic opioid exposure and withdrawal.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling (JAK1/2 already mapped) transduces the neuroinflammatory tone implicated in the reward dysregulation of opioid use disorder.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the TLR4-associated glial neuroinflammation driven by chronic opioid exposure.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the interferon-associated microglial activation reported with chronic opioid exposure and withdrawal.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of the PTEN-PI3K-AKT axis (PTEN and AKT already mapped) regulates the neuronal plasticity and oxidative-stress handling relevant to the reward neuroadaptations of opioid use disorder.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the peripheral myeloid inflammatory activation linked to chronic opioid use disorder.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α responses to opioid-associated hypoxic and metabolic stress contribute to the neuroadaptations of opioid use disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) mediates the synaptic-plasticity neuroadaptations of the reward circuit in opioid use disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK metabolic signaling participates in the neuronal energetic adaptations of chronic opioid exposure in opioid use disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation in the reward circuit contributes to the persistent neuroadaptations and relapse vulnerability of opioid use disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal and reward-circuit homeostasis implicated in opioid use disorder.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the mu-opioid-receptor signaling and synaptic plasticity of opioid use disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation associated with opioid use disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and reward-circuit processes implicated in opioid use disorder.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven neuroinflammation (glial activation) participates in the tolerance and dependence of opioid use disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory responses implicated in opioid use disorder.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with opioid use disorder.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the microglial and neuroinflammatory processes implicated in opioid use disorder.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the neuroadaptation and reward-circuit processes implicated in opioid use disorder.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tolerance mechanism: nitric oxide from neuronal nNOS drives the development of opioid tolerance and dependence through NMDA-linked signalling (glutamate already mapped), and blocking nNOS attenuates tolerance in models of opioid use.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences: estrogen modulates opioid reward and pain sensitivity, contributing to the sex differences in opioid use disorder susceptibility and treatment response beyond the testosterone axis already mapped.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Withdrawal insomnia: sleep and circadian disruption are prominent in opioid withdrawal and early recovery, and melatonin, the circadian sleep hormone, is studied as an adjunct for the insomnia that undermines abstinence.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Respiratory acidosis: opioid overdose depresses brainstem breathing, and the resulting carbon-dioxide and proton retention produce a respiratory acidosis that, with hypoxia, drives the fatal outcome reversed by naloxone.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Neuroimmune tolerance: opioids activate glia through TLR4 (already mapped), and the balance of pro-inflammatory cytokines against the anti-inflammatory IL-10 shapes the neuroinflammation implicated in opioid tolerance and hyperalgesia.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Neurosteroid modulation: progesterone and its metabolite allopregnanolone modulate opioid reward and withdrawal severity, contributing, with estrogen (already mapped), to the sex differences in opioid use disorder.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Glial hyperalgesia: prostaglandins from the opioid-activated glia (TLR4 already mapped) contribute to the neuroinflammation and the opioid-induced hyperalgesia and tolerance that complicate long-term opioid use.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative neuroinflammation: the glial activation and withdrawal stress of opioid use disorder generate oxidative stress, to which xanthine oxidase contributes, and the reactive oxygen species add to the neuroinflammation (NLRP3 already mapped) of tolerance.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Appetite-reward crosstalk: GLP-1 signalling links the gut-hormone (ghrelin already mapped) and reward pathways, and GLP-1 receptor agonists are being investigated to reduce the drug reward and craving of opioid use disorder.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the glial (microglia already mapped) pro-inflammatory cytokines (TNF, IL-6 and IL-1 already mapped) that drive the neuroinflammation of opioid tolerance.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium and tolerance: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) signalling that mediates opioid tolerance and withdrawal, and magnesium can attenuate these in opioid use disorder.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and opioid signalling: zinc modulates the mu-opioid receptor (already mapped) and NMDA signalling, and disturbed zinc status is linked to the mood and reward dysregulation of opioid use disorder.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Glial neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the opioid-glial (TLR4 already mapped) neuroinflammation of tolerance and dependence in opioid use disorder.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Injection endocarditis: the injection drug use of opioid use disorder causes right-sided infective endocarditis of the heart, a major and rising complication requiring prolonged antibiotics or surgery.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Blood-borne transmission: the injection drug use of opioid use disorder transmits hepatitis C (and HIV), a major public-health consequence driving the coinfection burden of the epidemic.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic adipokine: the chronic opioid use disrupts the leptin and energy balance (ghrelin already mapped) and the metabolic state, part of the neuroendocrine disturbance of opioid use disorder.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-inflammatory milieu disturbed by the chronic opioid use.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the neuroinflammation (TNF and IL-6 already mapped) of opioid use disorder.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, contributes to the glial (microglia already mapped) neuroinflammation and the tolerance/hyperalgesia of opioid use disorder.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune-inflammatory dimension (TNF and IL-1 already mapped) of chronic opioid use.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of opioid use disorder.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of chronic opioid use.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of opioid use disorder.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/mast-cell arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 dimension whose mast cells mediate the histamine (already mapped) release of opioid administration.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation of the psychoneuroimmunology of the chronic opioid exposure of opioid use disorder.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Opioid-suppressed NK: the NK-cell number and cytotoxicity, suppressed by the chronic opioid exposure (mu-opioid receptor already mapped), are part of the immunosuppression of opioid use disorder.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the innate inflammatory dimension of the opioid-induced (TLR4 already mapped) neuroinflammation of opioid use disorder.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are part of the complement activation of the opioid-induced neuroinflammation of opioid use disorder.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the neuroinflammation of opioid use disorder.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the opioid-induced neuroinflammation of opioid use disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-gut axis: TSLP, from gut-epithelium (gut-microbiome already mapped) disrupted by the opioid-induced constipation and dysbiosis of opioid use disorder, primes mast cells (already mapped) and dendritic cells (already mapped) and amplifies the gut-brain neuroinflammation.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-neuroinflammatory axis: bradykinin, via B2R on CNS microglia (already mapped) and neurons (already mapped), modulates the neuroinflammation and the autonomic dysregulation contributing to the withdrawal hyperalgesia of opioid use disorder.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor regulates the classical-complement and contact activation (C3 and C5 already mapped) contributing to the opioid-associated neuroinflammation and the microglial (already mapped) TLR4-driven immune dysregulation of opioid use disorder.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-opioid neuroprotection: erythropoietin and its receptor on neurons (already mapped) and microglia (already mapped) exert neuroprotective anti-apoptotic effects on the opioid-injured dopaminergic (dopamine already mapped) neurons of the reward circuitry.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — CNS-border ECM: periostin, from astrocytes (already mapped) and meningeal fibroblasts, contributes to the perivascular ECM remodelling and the neuroinflammation (IL-1b, IL-6 already mapped) of the opioid-remodelled reward circuitry of opioid use disorder.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Opioid-anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) common in opioid use disorder, driven by nutritional deficiency, anaemia, and the chronic inflammatory state of addiction.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — HPA-axis stress modulator: vasopressin, via V1aR on neurons (already mapped) and microglia (already mapped), modulates HPA-axis (cortisol already mapped) tone; vasopressin dysregulation amplifies the CRH (already mapped) and norepinephrine (already mapped) cascade of opioid use disorder.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Neuroprotective antioxidant: selenium, as neuroprotective GPx in neurons (already mapped) and microglia (already mapped), scavenges neuroinflammatory ROS; selenium deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of opioid use disorder.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-reward axis: iodine-dependent thyroid hormones regulate dopaminergic (dopamine already mapped) and serotonergic (serotonin already mapped) tone; iodine deficiency amplifies the HPA (cortisol already mapped) and CRH (already mapped) cascade of opioid use disorder.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Action-potential fidelity: sodium, via Na⁺/K⁺-ATPase on dopaminergic (dopamine already mapped) and glutamatergic (NMDA-receptor already mapped) neurons, maintains action-potential fidelity; sodium dysregulation amplifies the dopamine (already mapped) withdrawal cascade of opioid use disorder.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Catecholamine-synthesis cofactor: copper, as cofactor of dopamine-β-hydroxylase, converts dopamine (already mapped) to norepinephrine (already mapped) and modulates the catecholamine cascade; copper dysregulation amplifies the HPA-axis (cortisol already mapped) tone of opioid use disorder.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Reward-circuit excitability: potassium, via K⁺ channels on dopaminergic (dopamine already mapped) and GABAergic (GABA already mapped) neurons, sets membrane excitability; potassium dysregulation amplifies the withdrawal hyperalgesia of opioid use disorder.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — OUD calcium: calcium channel activation in neurons (already mapped) and microglia (already mapped) modulates opioid-dependent synaptic plasticity; calcium dysregulation by opioids amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of OUD.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — OUD phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and microglia (already mapped), sustains reward-circuit energy; phosphorus deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of opioid use disorder.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — OUD iron: iron, as cofactor of dopamine-β-hydroxylase in neurons (already mapped) and microglia (already mapped), supports dopaminergic reward tone; iron deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of OUD.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — OUD chloride: chloride, via KCC2 in GABAergic (GABA already mapped) interneurons of the reward circuit, sets inhibitory tone; chloride dysregulation amplifies NF-κB (already mapped) neuroinflammation and TNF-α (already mapped) withdrawal signalling in opioid use disorder.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — OUD nitrogen: nitrogen in amino-acid scaffold of opioid receptors (already mapped) and dopamine transporter proteins in neurons (already mapped) sustains reward-circuit signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of OUD.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — OUD sulfur: sulfur-containing amino acids sustain glutathione antioxidant defence in neurons (already mapped) and microglia (already mapped); sulfur deficiency amplifies NF-κB (already mapped) neuroinflammatory stress and TNF-α (already mapped) withdrawal cascade of OUD.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — OUD PD-1: PD-1 checkpoint expression on microglia (already mapped) and T-cells in the reward circuit modulates neuroinflammatory tone; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of opioid use disorder.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — OUD angiotensin-II: angiotensin-II in the mesolimbic dopamine (already mapped) circuit modulates stress-induced craving; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and CRH (already mapped) neuroinflammatory cascade of OUD.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — OUD VEGF: VEGF from microglia (already mapped) and astrocytes sustains neuroplasticity in dopamine (already mapped) reward circuits; VEGF dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of opioid use disorder.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — OUD WNT/β-catenin: WNT/β-catenin signalling in dopamine (already mapped) neurons supports synaptic plasticity; WNT dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and CRH (already mapped) reward-circuit cascade of opioid use disorder.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — OUD glp-1: GLP-1 from enteroendocrine cells (already mapped) and microglia (already mapped) modulates mesolimbic dopamine reward tone; glp-1 dysfunction amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — OUD rankl: RANKL from macrophages (already mapped) and microglia (already mapped) promotes neuroinflammatory immune activation in opioid circuits; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — OUD smad4: SMAD4 in neurons (already mapped) and astrocytes (already mapped) mediates TGF-β neuroplasticity repair; smad4 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — OUD il-2: IL-2 from T-cells (already mapped) and microglia (already mapped) regulates neuroinflammatory surveillance in opioid circuits; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — OUD fibronectin: fibronectin in neurons (already mapped) and astrocytes (already mapped) promotes CNS ECM remodelling in opioid circuits; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — OUD notch: Notch signalling in neurons (already mapped) and astrocytes (already mapped) regulates glial fate in opioid circuits; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — OUD igf-1: IGF-1 from neurons (already mapped) and astrocytes (already mapped) promotes opioid-circuit neuroprotection; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — OUD activin-a: activin-A from neurons (already mapped) and astrocytes (already mapped) modulates opioid-circuit neuroinflammatory tone; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — OUD tgf-beta: TGF-β from neurons (already mapped) and astrocytes (already mapped) drives opioid-circuit glial remodelling; tgf-beta excess amplifies nf-kb (already mapped) and il-6 (already mapped) and crh (already mapped) cascade of OUD.

[^volkow-2016-opioid-crisis]: Volkow ND, Collins FS. The role of science in addressing the opioid crisis. *N Engl J Med.* 2017;377(4):391-394. [doi:10.1056/NEJMsr1706626](https://doi.org/10.1056/NEJMsr1706626) · [PubMed 28723324](https://pubmed.ncbi.nlm.nih.gov/28723324/)
[^mattick-2009-bupe-meta]: Mattick RP, Breen C, Kimber J, Davoli M. Buprenorphine maintenance versus placebo or methadone maintenance for opioid dependence. *Cochrane Database Syst Rev.* 2014;2:CD002207. [doi:10.1002/14651858.CD002207.pub4](https://doi.org/10.1002/14651858.CD002207.pub4) · [PubMed 24500948](https://pubmed.ncbi.nlm.nih.gov/24500948/)
[^kreek-2002-opioid-neuroscience]: Kreek MJ, Koob GF. Drug dependence: stress and dysregulation of brain reward pathways. *Drug Alcohol Depend.* 1998;51(1-2):23-47. [doi:10.1016/S0376-8716(98)00064-7](https://doi.org/10.1016/S0376-8716(98)00064-7) · [PubMed 9716926](https://pubmed.ncbi.nlm.nih.gov/9716926/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
