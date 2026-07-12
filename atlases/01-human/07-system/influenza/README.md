---
schema: human-scale-entry/v1
id: influenza
name: Influenza
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Influenza A/B (orthomyxovirus; segmented negative-sense RNA) causes seasonal epidemics (H1N1, H3N2) and pandemics (1918 H1N1 killed ~50M; H5N1 mortality 60%); NS1 evades RIG-I/MAVS/STAT1; oseltamivir inhibits neuraminidase; baloxavir targets PA; annual vaccines 40-60% effective."
aliases: ["influenza", "flu", "influenza A", "influenza B", "H1N1", "H3N2", "H5N1", "avian influenza", "seasonal flu", "pandemic influenza", "orthomyxovirus", "hemagglutinin", "neuraminidase", "oseltamivir", "Tamiflu", "baloxavir"]
sources:
  - id: taubenberger-2006-influenza-pandemics
    type: peer-reviewed
    cite: "Taubenberger JK, Morens DM. 1918 Influenza: the mother of all pandemics. Emerg Infect Dis. 2006;12(1):15-22."
    doi: "10.3201/eid1201.050979"
    pmid: "16494711"
    url: "https://doi.org/10.3201/eid1201.050979"
    accessed: "2026-06-08"
  - id: who-influenza-seasonal
    type: clinical-guideline
    cite: "World Health Organization. Influenza (Seasonal) Fact Sheet. Geneva: WHO; 2023."
    url: "https://www.who.int/news-room/fact-sheets/detail/influenza-(seasonal)"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "Influenza 5′ppp ssRNA activates RIG-I → TRIM25 → MAVS → TBK1/IRF3 → IFN-β; NS1 blocks TRIM25-mediated RIG-I ubiquitination and sequesters dsRNA → impairs MAVS activation; RIG-I/MAVS is the primary innate sensor for influenza A in respiratory epithelium."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Influenza RIG-I/MAVS → IRF3 → IFN-β in epithelial cells; pDC TLR7 → IFN-α; NS1 blocks IRF3 and dsRNA sensing; H5N1 paradoxically induces high IFN-β → cytokine storm; pandemic strains differ from seasonal strains primarily in NS1 IFN antagonism potency."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Influenza NS1 blocks ISGF3 (STAT1/STAT2/IRF9) by dsRNA sequestration and TRIM25 inhibition; PA-X degrades host mRNAs; H5N1 overcomes STAT1/SOCS1 feedback → hyperinflammation; NS1 IFN antagonism is the primary virulence difference between pandemic and seasonal influenza strains."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Influenza M2 proton channel and PB1-F2 (mitochondrial targeting) activate NLRP3 → IL-1β + IL-18; NLRP3-mediated IL-1β amplifies cytokine storm in H5N1 and 1918 H1N1 pneumonia; NLRP3 genetic variants are associated with influenza severity and ASC speck formation in macrophages."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "Influenza A 5′ppp genomic ssRNA and dsRNA replication intermediates are the canonical RIG-I ligands; NS1 blocks RIG-I by sequestering dsRNA and inhibiting TRIM25-mediated K63-ubiquitination of RIG-I CARDs; NS1 IFN antagonism strength correlates with pandemic potential."
  - target: 01-human/03-molecular/influenza-ha
    relation: connects-to
    note: "HA is the primary influenza vaccine antigen; HA1 head antigenic sites A-E undergo annual drift requiring reformulation; HA2 stalk BNAbs are the basis of universal influenza vaccine strategies; α2,6-SA vs α2,3-SA receptor binding specificity determines human transmissibility."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Severe influenza is a disease of the lung: the virus infects alveolar epithelium → diffuse alveolar damage and ARDS (primary viral pneumonia), and by stripping mucociliary defenses it opens the door to the secondary bacterial pneumonia that caused most 1918 deaths."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "Influenza infects alveolar type I and type II pneumocytes; killing surfactant-producing type II cells collapses alveoli and slashes lung compliance → the diffuse alveolar damage and hyaline membranes of influenza ARDS, most severe with H5N1 and the 1918 strain."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Influenza paves the way for Streptococcus pneumoniae: viral damage to airway epithelium and mucociliary clearance lets pneumococcus colonize the lung, producing the secondary bacterial pneumonia that peaks 5-10 days in and drives much influenza mortality."
  - target: 01-human/07-system/measles
    relation: connects-to
    note: "Both are vaccine-preventable respiratory viruses but distinct: influenza (orthomyxovirus) drifts and shifts antigenically, needing annual reformulated vaccines, while measles (paramyxovirus) is antigenically stable—one MMR series gives lifelong immunity—yet far more contagious."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Influenza and COVID-19 are the dominant pandemic-capable respiratory viruses, overlapping in presentation but with distinct antivirals (oseltamivir/baloxavir vs nirmatrelvir/remdesivir); they co-circulate seasonally ('flurona' occurs) and both have annually updated vaccines."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Influenza is a potent cardiac trigger: in the week after infection the risk of myocardial infarction rises about six-fold, and the virus can cause myocarditis and decompensate heart failure; influenza vaccination reduces cardiovascular events, so it doubles as cardioprotection."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "Influenza and RSV are the two dominant seasonal respiratory viruses co-circulating each winter: both cause fever, cough, and pneumonia at the extremes of age, both now have older-adult vaccines, and multiplex PCR distinguishes them to guide antivirals and isolation."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Influenza has a striking link to narcolepsy: the 2009 H1N1 pandemic and its Pandemrix vaccine both raised type 1 narcolepsy in HLA-DQB1*06:02 carriers, apparently via molecular mimicry between an H1N1 hemagglutinin epitope and orexin—an infection-triggered autoimmunity."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells clear influenza and shape its vaccines: CD8 T cells recognizing conserved internal viral proteins kill infected cells and give cross-strain protection, which is why universal flu vaccines aim to harness T-cell immunity beyond strain-specific antibodies."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "Severe influenza can cause ARDS: viral pneumonia and an overwhelming inflammatory response flood the alveoli, collapsing gas exchange and requiring ventilation—the lethal end of influenza, often worsened by secondary bacterial pneumonia."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "Influenza is a recognized trigger of Guillain-Barré syndrome: the post-infectious autoimmune attack on peripheral-nerve myelin can follow flu (rarely the vaccine, far less than infection)—a reminder that the immune response, not just the virus, causes harm."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells provide early defense against influenza: NK cells kill virus-infected respiratory cells before adaptive immunity engages, and waning NK function with age contributes to the severe influenza and high mortality seen in the elderly."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Alveolar macrophages are central to influenza's outcome: they help clear virus and dead cells but, when overactivated in severe flu, pour out cytokines that injure the lung—so the macrophage response can mean recovery or fatal inflammatory pneumonia."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Influenza is the archetypal acute infection of the respiratory system: the virus infects airway and alveolar epithelium from nose to lung, causing tracheobronchitis and, in severe cases, viral pneumonia—and damaging mucosa enough to invite bacterial superinfection."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Severe and pandemic influenza can trigger a cytokine storm: excessive innate immune activation (notably in H5N1 and 1918-type strains) floods the lungs with inflammatory mediators, causing diffuse alveolar damage and ARDS out of proportion to viral load."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells are the basis of flu vaccination: antibodies against hemagglutinin block infection, but the virus's constant antigenic drift forces yearly reformulated vaccines, and rare antigenic shift—a new HA—can outrun B-cell memory to spark a pandemic."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Influenza opens the door to Staphylococcus aureus: viral damage to the airway lining lets S. aureus (including MRSA) cause severe, sometimes necrotizing secondary pneumonia—one of the deadliest complications, alongside pneumococcal superinfection."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Influenza occasionally strikes the brain: it can cause encephalitis and acute necrotizing encephalopathy, especially in children, and aspirin use during flu risks Reye's syndrome—so neurological symptoms in influenza are a red flag."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy makes influenza dangerous, and the placenta is why protection matters: immune and physiological changes raise the risk of severe flu, so maternal vaccination is recommended—antibodies cross the placenta to shield the newborn too."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Influenza immunity rests on anti-HA antibodies: IgG against hemagglutinin blocks the virus from entering cells, and the flu vaccine works by inducing it—so antigenic drift that changes HA is what forces yearly reformulation."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T-helper cells orchestrate influenza defense and vaccine response: CD4 cells drive the antibody and cytotoxic responses that clear the virus and build memory, so their decline with age partly explains why flu is deadlier and vaccines weaker in the elderly."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Severe influenza recruits neutrophils that injure the lung: swarming to the infected airways, they release enzymes and NETs that, beyond killing virus, damage the delicate gas-exchange surface and worsen the pneumonia."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Severe influenza can damage the kidneys: high fever, dehydration, and muscle breakdown (rhabdomyolysis) plus the systemic inflammatory storm can precipitate acute kidney injury, a marker of severe disease needing hospital care."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 tracks how dangerous a flu has become: this cytokine rises sharply in severe influenza, driving fever and the inflammatory cascade that can tip into cytokine storm and ARDS, so its level helps gauge severity."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Severe influenza starves the blood of oxygen: viral pneumonia and the ARDS it can trigger flood the alveoli, so gas exchange fails and hypoxemic respiratory failure becomes the main threat to life in serious flu."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Influenza and aspirin can wreck a child's liver: giving aspirin during flu can trigger Reye syndrome, a sudden failure of the liver with brain swelling, which is why aspirin is avoided in children with viral illness."
  - target: 01-human/03-molecular/surfactant
    relation: connects-to
    note: "Influenza strips the lungs of surfactant: the virus kills the type II pneumocytes that make this alveolar soap, so without it the air sacs collapse and stiffen, deepening the lung injury of severe flu pneumonia."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Severe flu shows on chest X-ray: photons reveal the bilateral infiltrates of viral pneumonia or the lobar consolidation of the bacterial pneumonia that often follows the infection."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Influenza pneumonia floods the alveoli: viral and immune damage to these air sacs fills them with fluid and debris—the diffuse alveolar damage of ARDS that starves the blood of oxygen."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Severe flu ends in acidosis: as gas exchange fails, carbon dioxide and acid build up, and the falling pH of respiratory failure is an ominous sign in flu-related ARDS."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the flu's machinery: spherical virions bristle with two spikes — hemagglutinin to latch onto cells and neuraminidase to escape them — the H and N proteins that name strains like H1N1 and that the vaccines target."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Severe influenza can drop the sodium: the inflammatory stress triggers SIADH, retaining water and diluting blood sodium, a hyponatremia that worsens the confusion and weakness of serious infection."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Flu can hit the gut too: especially in children and with influenza B, the infection brings nausea, vomiting, and diarrhea, the 'stomach flu' symptoms that accompany the classic respiratory illness."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The flu vaccine is a bet on antibody: it teaches the body to make anti-hemagglutinin antibodies, but the virus's antigenic drift keeps changing that target, which is why the shot must be reformulated and given every year."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The aching muscles are flu's signature: cytokines and direct infection produce the deep myalgia of the illness, and in children influenza can cause a benign acute myositis or, rarely, muscle-breaking rhabdomyolysis."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Influenza's spike clumps red cells: hemagglutinin binds the sialic acid on erythrocytes, agglutinating them — the reaction behind the classic hemagglutination and hemagglutination-inhibition assays used to type the virus and gauge immunity."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy makes flu more dangerous: the immune and lung changes of pregnancy raise the risk of severe influenza and preterm birth, so vaccination in pregnancy protects both mother and, through transferred antibody, the newborn."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Flu can reach the brain: influenza-associated encephalopathy and encephalitis injure neurons, mostly in children, and aspirin given during infection risks the brain-and-liver damage of Reye syndrome."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "In children flu often hits the gut: influenza B especially brings nausea, vomiting, and diarrhea alongside the respiratory illness — true gastrointestinal flu, distinct from the unrelated 'stomach flu' of norovirus."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells set the immune response: they carry flu antigen from the airway to the lymph nodes to prime T and B cells, and plasmacytoid DCs pour out the type I interferon that mounts the early antiviral defense."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Flu is hard on a failing heart: the infection triggers acute decompensation, myocardial infarction, and myocarditis in the weeks after onset, which is why influenza vaccination measurably cuts cardiovascular events."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye can be flu's doorway: avian strains like H7 bind receptors on the conjunctiva, causing conjunctivitis and offering the virus a route of entry that bypasses the airway."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Flu can stop the heart: the acute inflammation of influenza sharply raises the risk of heart attack and stroke in the days after infection, which is why flu vaccination measurably lowers cardiovascular events."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "It tips chronic lungs over the edge: influenza is a leading trigger of COPD exacerbations, turning manageable airflow limitation into respiratory failure — the reason annual vaccination is urged in these patients."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "It sets off the wheeze: influenza is a common trigger of severe asthma attacks, inflaming already twitchy airways, so asthmatics are a priority group for the flu vaccine."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The virus throws the inflammatory switch — and rides it: influenza activates NF-κB to drive the cytokine response, yet the virus also exploits NF-κB signaling for its own efficient replication, a double-edged host pathway."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Severe flu opens the lung to a mold: influenza-associated pulmonary aspergillosis strikes critically ill patients days into ICU care, the damaged airway epithelium and immune paralysis letting Aspergillus invade."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Acute infection can trigger a stroke: in the weeks after influenza, the risk of ischemic stroke and heart attack transiently rises as systemic inflammation destabilizes plaques and tips the blood toward clotting."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Secondary bacterial pneumonia turns deadly: influenza strips the airway epithelium, letting Staphylococcus and pneumococcus invade into a post-influenza bacterial pneumonia that can progress to sepsis and shock."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Severe flu can injure the kidney: influenza can cause rhabdomyolysis and, in critical illness, acute kidney injury, and the insult can leave or worsen chronic kidney disease in vulnerable patients."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes and flu worsen each other: people with type 2 diabetes have more severe influenza and complications, while the infection's stress hormones destabilize glycemic control — a reason yearly vaccination is urged."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "It is historically tied to parkinsonism: the encephalitis lethargica that followed the 1918 pandemic left post-encephalitic parkinsonism, and influenza is studied as one infectious contributor to Parkinson's risk."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "It leaves a low-mood aftermath: the post-viral fatigue and neuroinflammation of influenza can produce weeks of depressed mood, part of the broader post-infectious malaise."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Infections may nudge dementia risk: severe influenza and its systemic inflammation are studied as contributors to cognitive decline, and influenza vaccination is associated with lower dementia incidence."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can strike the nervous system: influenza causes febrile seizures and acute encephalopathy, especially in children, and is a recognised trigger of Guillain-Barré syndrome and the rare Reye syndrome."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its outcome is decided by immunity: the immune response clears influenza but its overshoot causes the cytokine-driven damage, and immunocompromised and elderly patients suffer the most severe disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It can upset the gut and liver: influenza, particularly in children, causes nausea, vomiting and diarrhoea, and aspirin use during infection risks the hepatic failure of Reye syndrome."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Severe flu can injure the kidney: influenza-associated rhabdomyolysis and the systemic insult of severe infection can cause acute kidney injury needing supportive care."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It destabilises diabetes: the stress of influenza raises blood glucose and can precipitate diabetic ketoacidosis or hyperosmolar crises, a key reason vaccination is urged in diabetes."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It can deplete the lymphocytes: severe influenza, especially avian H5N1, causes marked lymphopenia — a poor-prognosis marker — alongside the reactive lymphoid response to infection."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Aspirin is dangerous in childhood flu: giving it to children during influenza or chickenpox can trigger Reye syndrome, acute liver failure with encephalopathy, so it is avoided."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Acute infection is prothrombotic: influenza transiently raises the risk of venous thromboembolism, heart attack and stroke in the weeks after illness."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D status nudges susceptibility: deficiency is associated with more respiratory infection, and supplementation may give a small protective effect against influenza-like illness."
  - target: 03-medicine/01-modern/05-antiviral/oseltamivir
    relation: connects-to
    note: "The mainstay antiviral: oseltamivir, a neuraminidase inhibitor, shortens influenza when started early and is used for treatment and prophylaxis, alongside the newer endonuclease inhibitor baloxavir."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "It opens the door to invasive strep: post-influenza airway damage predisposes to severe group A streptococcal pneumonia and toxic shock, a less common but devastating secondary infection."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "Two pandemic respiratory viruses meet: influenza and SARS-CoV-2 co-circulate and can co-infect, share airborne spread and overlapping severe pneumonia, but differ in antivirals and vaccine strategy."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Newer antivirals beyond oseltamivir: baloxavir, a cap-dependent endonuclease inhibitor, and monoclonal antibodies against haemagglutinin target distinct steps of the influenza life cycle for treatment and prophylaxis."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It strains and inflames the heart: influenza causes myocarditis and sharply raises the risk of acute myocardial infarction in the days after infection — risk that influenza vaccination measurably reduces."
  - target: 02-pathogen/06-environmental/zoonosis
    relation: connects-to
    note: "Pandemics come from animals: influenza A reservoirs in wild birds and pigs reassort to create novel strains (avian H5N1, swine H1N1) against which humans have little immunity — the zoonotic antigenic shift behind pandemics."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "It tips blood toward clotting: influenza causes thrombocytopenia and a prothrombotic, inflamed endothelium, part of why heart attacks, strokes and venous thrombosis spike in the weeks after infection."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Not just a respiratory virus: influenza—especially avian strains and infection in children—can infect the gut epithelium, causing the vomiting and diarrhoea of so-called stomach flu."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Why flu shots protect the heart: influenza can rupture atherosclerotic plaques and trigger myocardial infarction, and vaccination measurably lowers post-infection cardiovascular events."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Where flu immunity is built and outpaced: antibody to influenza haemagglutinin matures in germinal centres, but the virus's antigenic drift escapes prior responses, forcing annual revaccination."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Neurological influenza: influenza can cause febrile seizures, encephalopathy and rarely acute necrotising encephalitis in children, occasionally triggering or unmasking epilepsy."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "Dangerous in chronic lung disease: influenza causes severe exacerbations and bacterial superinfection in cystic fibrosis and other chronic lung diseases, making annual vaccination essential."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Viral myositis: influenza is a leading cause of the diffuse myalgia of acute illness and, in children, benign acute viral myositis with calf pain and raised creatine kinase, occasionally with rhabdomyolysis."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Flu and the heartbeat: influenza can cause myocarditis and, through systemic inflammation and hypoxia, precipitate atrial fibrillation and other arrhythmias of the cardiac conduction system."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Severe in pregnancy: pregnant women are at high risk of severe influenza and complications, the basis for prioritising vaccination, which also protects the newborn through transferred antibodies."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Cytokine storm: TNF-α is a leading driver of the hyperinflammatory cytokine storm that, in severe influenza, injures the lung and causes the systemic illness beyond direct viral damage."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Antiviral T-cell signal: IFN-γ from T and NK cells activates macrophages and supports viral clearance in influenza, while contributing to the immunopathology of severe infection."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome response: NLRP3-driven IL-1β release amplifies airway inflammation and fever in influenza, balancing protective antiviral immunity against lung injury."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte influx: CCL2 recruits inflammatory monocytes into the influenza-infected lung, where they aid clearance but in severe disease drive the immunopathology behind viral pneumonia and ARDS."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic clearance: CD8 T cells eliminate influenza-infected airway cells through perforin and granzyme, essential for recovery but a source of the epithelial damage in severe infection."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Neutrophilic lung injury: IL-17A drives neutrophil recruitment to the influenza-infected airway, contributing to the excessive inflammation and tissue damage of severe and secondary-bacterial pneumonia."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "DAMP-driven lung injury: oxidised phospholipids and HMGB1 from influenza-damaged lung engage TLR4 on innate cells, a pathway driving the acute lung injury of severe influenza that TLR4 antagonism mitigates in models."
  - target: 01-human/03-molecular/tbk1
    relation: connects-to
    note: "Interferon-induction node: RIG-I sensing of influenza RNA signals through MAVS to TBK1, the kinase that phosphorylates IRF3 to launch the type-I-interferon response central to antiviral defence against the virus."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Regulatory restraint: IL-10 dampens the influenza immune response to limit immunopathology, a protective brake whose balance with effector cytokines determines whether the host clears the virus or suffers a damaging cytokine storm."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal protection: secretory IgA on the respiratory epithelium neutralises influenza at the airway surface and provides cross-protective mucosal immunity, the rationale behind intranasal live-attenuated vaccines that induce it better than injected vaccines."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Endosomal sensing: plasmacytoid dendritic cells detect influenza RNA through TLR7 signalling via MyD88 to make large amounts of type-I interferon, the endosomal innate-sensing arm complementing the cytosolic RIG-I pathway."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative lung injury: xanthine-oxidase activity surges during severe influenza, generating reactive oxygen species that damage the alveolar epithelium and contribute to the acute lung injury of severe and fatal infection."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "Interferon induction: IRF3, activated by the RIG-I/MAVS/TBK1 sensing pathway already mapped, drives the type-I interferon front-line defence against influenza, the response the viral NS1 protein antagonises."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Epithelial apoptosis: influenza induces caspase-3 apoptosis of infected respiratory epithelial cells, both an antiviral defence and a cause of the epithelial damage that opens the airway to secondary bacterial pneumonia."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Severe-flu hypoxia: the diffuse alveolar damage and hypoxaemia of severe influenza pneumonia drive HIF-mediated responses in the injured lung, part of the pathophysiology of influenza ARDS."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Interferon signal transduction: type-I interferon produced through the RIG-I-MAVS-IRF3 axis (all already mapped) signals via JAK-STAT to STAT1 (mapped), inducing the antiviral interferon-stimulated genes that restrict influenza replication."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1/NK antiviral arm: IL-12 from activated dendritic cells drives NK-cell and Th1 IFN-γ responses (already mapped) that augment the cellular clearance of influenza-infected respiratory epithelium."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement antiviral and immunopathology: complement C3 opsonises influenza virions and enhances neutralisation, while excessive activation also contributes to the lung immunopathology of severe influenza."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Influenza activates the Raf-MEK-ERK pathway to drive nuclear export of viral ribonucleoproteins, a host-directed antiviral target."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "The influenza NS1 protein activates PI3K-AKT signalling to delay apoptosis and support efficient viral replication."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Influenza modulates mTOR-regulated translation to favour viral protein synthesis during infection."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the macrophage-driven cytokine storm and lung inflammation of severe influenza pneumonia."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response that contributes to the lung pathology of severe influenza."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the lung epithelial repair and fibrosis that follow the diffuse alveolar damage of severe influenza."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic nucleic-acid sensing through cGAS-STING, including mitochondrial DNA from damaged cells, augments the innate antiviral and inflammatory response to influenza."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by recruited neutrophils amplify the lung inflammation and severity of influenza pneumonia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the airway epithelial oxidative-stress and survival responses to influenza infection."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the innate antiviral signaling and inflammatory response to influenza and is also exploited by the virus for replication."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) is activated by influenza NS1 to support viral replication and modulate apoptosis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Influenza modulates host autophagy through its M2 and NS1 proteins to favor its replication and evade degradation."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the airway epithelial and immune-cell responses to influenza and in viral entry."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling, exploited by influenza for its replication, participates in the host response to influenza."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the pulmonary inflammation of severe influenza."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the host immune response to influenza."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the airway leukocyte trafficking and immune responses of influenza."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the airway epithelial and innate immune responses to influenza."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the host antiviral response to influenza."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of the antiviral immune response to influenza."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the leukocyte recruitment and pulmonary inflammation of influenza."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Vaccine and clearance: MHC class II-restricted CD4 help drives the antibody response to haemagglutinin (already mapped) elicited by influenza vaccines, and cross-reactive T-cell help contributes to the heterosubtypic immunity sought by universal-vaccine efforts."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac complications: influenza can cause myocarditis and sharply raises the short-term risk of myocardial infarction, with troponin release marking the cardiac injury that contributes to influenza-associated deaths."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell response: IL-2 drives the expansion of the effector and memory T cells (perforin already mapped) that clear influenza-infected airway epithelium, and the strength of this response shapes recovery and cross-protection."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Fever response: prostaglandin E2 generated during influenza acts on the hypothalamus to produce the fever and malaise of the illness, which is why cyclooxygenase-inhibiting antipyretics relieve these systemic symptoms."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Airway nitric oxide: inducible nitric oxide rises in the influenza-infected airway, contributing both to antiviral defence and, in excess, to the airway inflammation and lung injury of severe infection."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Antibody help: IL-4 and type-2 T-cell help drive the B-cell (already mapped) production of the neutralising antibodies (IgG already mapped) against haemagglutinin that mediate influenza immunity and vaccine protection."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Respiratory acidosis: in severe influenza pneumonia and acute respiratory distress, failing gas exchange retains carbon dioxide, and the accumulation of protons produces the respiratory acidosis that signals impending respiratory failure."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-mediated inflammation: bradykinin generated in the influenza-infected airway raises vascular permeability and stimulates the mucus and inflammation that obstruct the airways, part of the kinin contribution to the respiratory symptoms."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Neurogenic inflammation: CGRP released from airway sensory nerves, with substance-P-type neuropeptides, contributes to the neurogenic inflammation and cough of influenza, part of the neuro-immune dimension of the respiratory infection."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium and virulence: selenium deficiency increases the virulence of influenza and worsens the disease, the antioxidant selenoproteins limiting the viral mutation and the oxidative lung injury (xanthine oxidase already mapped) of infection."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and antiviral immunity: zinc supports the interferon (already mapped) antiviral response and impairs influenza replication, and zinc status influences the immunity that determines the severity of infection."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Omega-3 inflammation resolution: the omega-3 fatty acids give rise to pro-resolving mediators such as protectin D1 that limit the excessive lung inflammation (prostaglandins already mapped) of severe influenza, aiding recovery."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 airway arm: IL-13, with IL-4 (already mapped), is part of the type-2 response that modulates the airway epithelium and contributes to the post-influenza wheeze and the asthma exacerbations it can trigger."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Alveolar oedema: VEGF drives the vascular permeability and the alveolar-capillary oedema of the severe influenza pneumonia (surfactant already mapped), part of the lung injury and ARDS."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and severity: obesity, signalled through the adipokine leptin, is an independent risk factor for severe influenza, the adipose-immune dysfunction impairing the antiviral response."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity (a severe-influenza risk) and the immune-metabolic milieu of the influenza response."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the cytokine (IL-6 already mapped) response to influenza."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Inflammation iron: the IL-6-driven (already mapped) hepcidin of the severe influenza inflammation contributes to the anaemia and the iron dysregulation of the acute illness."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: connects-to
    note: "Causative virus: the influenza is caused by the influenza virus (the influenza A the pandemic-capable type; the haemagglutinin already mapped), the segmented orthomyxovirus of the antigenic drift and shift."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune response and the asthma-exacerbation link of influenza."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune response to influenza."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the antiviral and antibacterial mucosal defence against influenza and its bacterial superinfection."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Antibody arm: the plasma cells secrete the anti-haemagglutinin (HA already mapped) antibodies that provide the vaccine-induced and convalescent protection against influenza."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Type-2 airway arm: the mast cells, armed by the IgE (already mapped), contribute to the type-2 airway inflammation and the asthma exacerbation (already mapped) triggered by influenza."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the innate inflammatory injury of the severe influenza pneumonia and the cytokine storm."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling drives the neutrophil (already mapped) recruitment and the immunopathology of the severe influenza lung injury."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Immunopathology control: the regulatory T cells restrain the antiviral inflammation and promote the resolution and tissue repair after the influenza infection."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-driven immunopathology of the severe influenza lung injury."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Lectin/classical regulation: the C1-esterase inhibitor regulates the classical and lectin (mannose-binding) complement pathways activated against the influenza virus, a candidate modulator of the lung immunopathology."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Acute-phase iron: transferrin, the iron carrier, reflects the hypoferraemia and disordered iron handling (hepcidin already mapped) of the acute-phase response to the influenza infection."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-lung axis: TSLP, from airway epithelium (already mapped) damaged by influenza, primes dendritic cells (already mapped) and mast cells (already mapped) and amplifies the Th2/eosinophil (already mapped) airway inflammation during and after influenza infection."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Post-influenza anaemia: erythropoietin drives red-cell recovery after the influenza-associated haemophagocytic lymphohistiocytosis (bone-marrow already mapped) and the cytokine-storm (IL-6 already mapped) -driven anaemia of severe influenza."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell-histamine axis: histamine, from mast cells (already mapped) degranulated by the influenza NA protein, amplifies the bronchospasm and the vascular permeability of the influenza-associated airway inflammation and post-viral asthma (already mapped) exacerbation."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Post-viral airway remodelling: periostin, induced in airway epithelium and fibroblasts by the IL-4/IL-13 (already mapped) Th2 response to influenza, drives the ECM remodelling and the post-influenza asthma-exacerbation (already mapped) airway hyperresponsiveness."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian antiviral immunity: melatonin has antiviral and immunomodulatory properties; influenza follows a circadian pattern of severity, and melatonin modulates the innate antiviral type-I-interferon (already mapped) and the NLRP3-inflammasome (already mapped) responses."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Stress-immune neuroendocrine: prolactin, elevated by the febrile stress of influenza infection, enhances lymphocyte (T-helper-cell and B-cell already mapped) activation and the antibody (already mapped) response against the influenza virus."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Influenza testosterone: testosterone, via androgen receptors on macrophages (already mapped) and T-helper cells (already mapped), attenuates the cytokine-storm (already mapped) and IL-6 (already mapped) immunopathology; androgen deficiency worsens influenza ARDS severity."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Influenza serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and neurons (already mapped), modulates the cytokine-storm (already mapped) and NLRP3-inflammasome (already mapped) inflammatory axes; serotonin sets the influenza innate immune response severity."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Influenza oxytocin: oxytocin, via OXTR on macrophages (already mapped) and regulatory T cells (already mapped), attenuates the cytokine-storm (already mapped) and IL-6 (already mapped) immunopathology; oxytocin promotes immune resolution after severe influenza infection."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Influenza vasopressin: vasopressin, via V1aR on macrophages (already mapped) and neurons (already mapped), modulates cytokine-storm (already mapped) and NF-κB (already mapped) immunopathology; vasopressin excess amplifies IL-6 (already mapped) and NLRP3 (already mapped) cascade."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Influenza iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and dendritic-cell (already mapped) antiviral innate immunity; iodine deficiency impairs type-I-interferon (already mapped) and NF-κB (already mapped) antiviral responses against influenza."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Influenza magnesium: magnesium stabilises NLRP3 inflammasome (already mapped) and attenuates NF-κB (already mapped) and cytokine-storm (already mapped) immunopathology; magnesium deficiency impairs macrophage (already mapped) and NK-cell (already mapped) antiviral function."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Influenza calcium: calcium, as second messenger in macrophages (already mapped) and neutrophils (already mapped), coordinates antiviral signalling; calcium dysregulation amplifies the NF-κB (already mapped) and cytokine-storm (already mapped) cascade of influenza."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Influenza iron: iron, regulating innate immune enzyme activity in macrophages (already mapped) and NK cells (already mapped), supports antiviral defence; iron deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cytokine cascade of influenza."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Influenza potassium: potassium depletion promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; potassium deficiency amplifies the NF-κB (already mapped) and NLRP3 (already mapped) cytokine-storm (already mapped) cascade of influenza."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Influenza copper: copper, in macrophages (already mapped) and NK cells (already mapped), scavenges viral-driven ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cytokine cascade of influenza."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Influenza phosphorus: phosphorus, as ATP in macrophages (already mapped) and NK cells (already mapped), fuels antiviral immune responses; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and cytokine-storm (already mapped) cascade of influenza."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Influenza chloride: chloride regulates macrophage (already mapped) and NK cells (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and cytokine-storm (already mapped) innate immune cascade of influenza."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Influenza carbon: carbon as backbone of viral glycoproteins and cytokines (already mapped) sustains replicative signalling; carbon metabolites in macrophages (already mapped) and NK cells (already mapped) amplify NF-κB (already mapped) and IL-6 (already mapped) in influenza."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Influenza nitrogen: nitrogen in viral proteins and cytokines (already mapped) sustains signalling; nitrogen-derived RNS from macrophages (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) and cytokine-storm (already mapped) cascade of influenza."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Influenza sulfur: sulfur-containing amino acids in macrophages (already mapped) and NK cells (already mapped) regulate redox signalling; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and cytokine-storm (already mapped) cascade of influenza."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Influenza pd-1: PD-1 on T-cytotoxic cells (already mapped) and NK cells (already mapped) suppresses antiviral immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and cytokine-storm (already mapped) cascade of influenza."
---

# Influenza

## Overview

**Influenza** is an acute respiratory infection caused by **influenza viruses** (family *Orthomyxoviridae*), with four types recognized in humans: influenza A, B, C, and D. Influenza A and B cause clinically significant human disease: **influenza A** (with subtypes defined by hemagglutinin H1-H18 and neuraminidase N1-N11) is responsible for all documented pandemics and the most severe seasonal epidemics; **influenza B** (lineages Yamagata and Victoria) causes significant seasonal morbidity, especially in children.

Globally, seasonal influenza causes an estimated **3–5 million severe cases** and **290,000–650,000 respiratory deaths** annually (WHO). The 1918 Spanish influenza pandemic (H1N1) — the most catastrophic acute infectious disease event in recorded history — killed an estimated 50–100 million people worldwide [^taubenberger-2006-influenza-pandemics]. The ongoing threat of **highly pathogenic avian influenza H5N1** (case fatality rate ~60% in confirmed human cases) represents one of the highest-priority pandemic preparedness concerns.

**Clinical spectrum:**
- **Uncomplicated influenza**: Abrupt-onset fever (38–40°C), myalgia ("flu"), headache, malaise, dry cough, sore throat; self-limiting 5–7 days
- **Complicated influenza**: Primary viral pneumonia, secondary bacterial pneumonia (*S. aureus*, *S. pneumoniae*, *H. influenzae*), myocarditis, encephalitis
- **Severe/fatal influenza**: ARDS, multi-organ failure; cytokine storm (particularly H5N1 and 1918 H1N1); Reye syndrome (children: aspirin + influenza → mitochondrial dysfunction)

High-risk groups: elderly (≥65), children <2 years, pregnancy, immunocompromised, obesity, chronic cardiopulmonary/metabolic disease.

## Structure

### Influenza virus biology

Influenza A is an enveloped virus (~120 nm diameter) with an **8-segment negative-sense ssRNA genome**:

| Segment | Protein(s) | Function |
|---------|-----------|----------|
| 1 | PB2 | Cap-binding subunit of RdRp; binds 5′ m7GTP cap of host mRNAs for cap-snatching |
| 2 | PB1, PB1-F2 | PB1: RNA polymerase catalytic subunit; PB1-F2: mitochondria-targeting pro-apoptotic peptide; activates NLRP3 |
| 3 | PA | Endonuclease subunit of RdRp; cleaves snatched host cap primers; target of baloxavir |
| 4 | HA (hemagglutinin) | Sialic acid receptor binding (α2,6 SA — human upper airway; α2,3 SA — avian/lower airway); membrane fusion; neutralizing antibody target; 18 subtypes |
| 5 | NP (nucleoprotein) | Encapsidates genomic RNA; vRNP nuclear import/export |
| 6 | NA (neuraminidase) | Sialidase: cleaves sialic acid → virion release from cells and mucus barrier penetration; target of oseltamivir, zanamivir, peramivir; 11 subtypes |
| 7 | M1, M2 | M1: matrix protein, virion structure; M2: proton channel, endosomal uncoating; amantadine target (now largely resistant) |
| 8 | NS1, NEP/NS2 | NS1: multifunctional IFN antagonist; NEP: nuclear export of vRNPs |

### Key surface glycoproteins

**Hemagglutinin (HA):**
- HA0 precursor cleaved to HA1+HA2 (disulfide-linked) by host serine proteases (TMPRSS2, plasmin, furin for highly pathogenic strains)
- HA1 globular head: receptor binding domain; hypervariable; target of strain-specific neutralizing antibodies
- HA2 stalk: membrane fusion domain; conserved; target of broadly neutralizing antibodies (research/universal vaccine focus)
- HA binding specificity: α2,6-linked sialic acid (human upper respiratory epithelium) vs α2,3-linked (avian intestinal epithelium; human lower respiratory) — key determinant of human transmissibility

**Neuraminidase (NA):**
- Box-shaped tetramer on virion surface
- Sialidase activity cleaves sialic acid from HA-receptor complexes → releases new virions; also cleaves mucus glycoproteins allowing viral spread through mucus layer
- Active site is highly conserved across subtypes → druggable target with oseltamivir, zanamivir, peramivir, laninamivir

### Antigenic variation

- **Antigenic drift**: Accumulation of point mutations in HA/NA surface epitopes → immune evasion; basis for annual vaccine reformulation
- **Antigenic shift**: Reassortment of genome segments between human and animal (avian, swine) influenza A strains → novel HA/NA subtypes → pandemic potential (no pre-existing population immunity)

## Function

### Viral entry and replication cycle

1. **Attachment**: HA1 binds sialic acid on respiratory epithelium → endocytosis via clathrin-mediated pathway
2. **Fusion**: Endosomal acidification (pH 5–6) → HA conformational change (HA2 spring-loaded) → membrane fusion → vRNP release into cytoplasm; M2 proton channel acidifies virion interior simultaneously
3. **Nuclear import**: vRNPs transported to nucleus via importin-α/β
4. **Transcription/Replication**: Cap-snatching by PB2/PA → capped viral mRNA synthesis by PB1; cRNA synthesis (antigenomic positive-sense) → vRNA amplification
5. **Assembly**: vRNPs exported via NEP/M1 to cytoplasm → transported to apical plasma membrane; HA and NA traffic via Golgi
6. **Budding/Release**: Virion buds from plasma membrane; NA cleaves sialic acid → virion released (without NA: virion clusters on cell surface)

### Innate immune response

| Time | Host response | Viral countermeasure |
|------|---------------|---------------------|
| 0–6 h | RIG-I detects 5′ppp ssRNA → MAVS → IRF3 → IFN-β | NS1 sequesters dsRNA, blocks TRIM25-mediated RIG-I ubiquitination |
| 6–24 h | IFN-β → IFNAR → STAT1/STAT2 → ISGs (MX1, OAS1, PKR) | NS1 blocks ISGF3; PA-X degrades host mRNAs |
| 24–48 h | NK cells, pDC IFN-α; macrophage/DC activation | NS1 binds CPSF30 → blocks host mRNA polyadenylation |
| Day 2–5 | Virus-specific CD8+ T cells (M1 peptide dominant); CD4+ Tfh | — |
| Day 5–7 | Neutralizing IgM (anti-HA); IgA (mucosal) | Antigenic drift in subsequent infections |

### NS1 multi-function IFN antagonism

NS1 is the dominant virulence factor for IFN evasion:
- **dsRNA sequestration**: NS1 RNA-binding domain sequesters dsRNA replication intermediates → RIG-I and PKR not activated
- **TRIM25 inhibition**: NS1 binds TRIM25 → prevents K63-ubiquitination of RIG-I CARDs → MAVS not activated
- **IRF3 blockade**: NS1 inhibits TBK1/IKKε → impairs IRF3 phosphorylation
- **Host mRNA processing block**: NS1 C-terminal ESAV/EPEV motif binds CPSF30 → blocks polyadenylation of host mRNAs (including IFN-β) → selectively reduces host mRNA stability
- **STAT2 evasion** (some strains): NS1 reported to block STAT1/STAT2 signaling

Highly pathogenic H5N1 NS1 has stronger multi-functional IFN antagonism than seasonal H1N1/H3N2, contributing to the paradoxically high cytokine response.

## Pathology

### Primary viral pneumonia

Influenza A infects alveolar epithelial cells (type I and II pneumocytes) → massive cell death → impaired surfactant production → reduced lung compliance → ARDS. Highly pathogenic H5N1 causes diffuse alveolar damage (DAD) with hyaline membrane formation, similar to ARDS from other causes.

### Cytokine storm

H5N1 and the 1918 pandemic strain drive disproportionate innate immune activation in the lower respiratory tract:
- NLRP3 inflammasome activation (M2 ion channel, PB1-F2 mitochondrial damage) → IL-1β + IL-18
- Macrophage activation → TNF-α, IL-6, CXCL10, IL-8 → neutrophil infiltration
- Paradoxically high IFN-β → may amplify rather than resolve inflammation in severe disease
- STAT1-mediated transcription overwhelmed → tissue destruction rather than pathogen clearance

### Secondary bacterial pneumonia

Influenza damages mucociliary clearance and exposes basal lamina glycoproteins → bacterial colonization by *S. aureus* (including MRSA), *S. pneumoniae*, *H. influenzae* → secondary pneumonia peaks at Day 5–10; responsible for majority of 1918 influenza deaths

### Diagnosis

- **Rapid antigen detection tests (RADTs)**: Sensitivity 50-70% for influenza A; faster and cheaper but miss many cases
- **RT-PCR (multiplex respiratory panel)**: Gold standard; highly sensitive; distinguishes A/B and subtypes (H1, H3, H5)
- **DFA/IFA**: Direct fluorescent antibody; moderate sensitivity
- Point-of-care molecular tests (ID NOW, Cepheid): Near RT-PCR sensitivity with 15-min turnaround

### Treatment

**Antivirals:**
- **Oseltamivir (Tamiflu)**: Oral NA inhibitor; reduces symptom duration by ~1 day and hospitalizations; most effective ≤48 h from symptom onset; prophylactic use post-exposure; oseltamivir resistance (H275Y in NA) in some H1N1 strains
- **Zanamivir (Relenza)**: Inhaled NA inhibitor; alternative to oseltamivir; contraindicated in asthma/COPD
- **Peramivir (Rapivab)**: IV NA inhibitor for hospitalized patients
- **Baloxavir marboxil (Xofluza)**: PA cap-dependent endonuclease inhibitor; single oral dose; active against oseltamivir-resistant strains; I38T resistance emerging with H3N2
- Amantadine/rimantadine: M2 channel blockers; virtually all circulating influenza A strains are resistant (S31N in M2)

**Severe disease:** ICU support, mechanical ventilation for ARDS; IV NAI (peramivir or inhaled zanamivir via ventilator); no proven benefit of corticosteroids

### Vaccines

- **IIV4 (inactivated influenza vaccine, quadrivalent)**: Standard-dose IM; annual; includes two influenza A strains (H1N1, H3N2) + two B strains (Yamagata, Victoria lineages); efficacy 40-60% depending on antigenic match
- **LAIV (live attenuated, FluMist)**: Intranasal; cold-adapted (25°C restricted replication); superior mucosal IgA induction; approved for ages 2-49
- **Adjuvanted (Fluad MF59)**: For adults ≥65; MF59 oil-in-water emulsion activates NLRP3 → depot effect + improved immunogenicity in elderly
- **High-dose (Fluzone HD)**: 4× antigen dose for adults ≥65; superior seroconversion
- **Recombinant HA (Flublok)**: Cell-culture independent; broader HA representation; approved for immunogenicity in elderly
- **mRNA influenza vaccines (investigational)**: Moderna/Pfizer in Phase II; potential for rapid pandemic strain updates and universal HA stalk targeting

## Connections

**→ [MAVS](../../../03-molecular/mavs/)**: Influenza 5′ppp negative-sense genomic ssRNA activates RIG-I → TRIM25 K63-ubiquitination → MAVS filament formation → TBK1 → IRF3 → IFN-β; NS1 suppresses MAVS by blocking TRIM25 and sequestering dsRNA replication intermediates; RIG-I/MAVS is the primary innate sensor for influenza in respiratory epithelium.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: Influenza RIG-I/MAVS → IRF3/IRF7 → IFN-β in epithelial cells; pDC TLR7 → IFN-α (systemic); NS1 suppresses IFN by blocking IRF3 and dsRNA sensing; highly pathogenic H5N1 induces paradoxically high IFN-β contributing to cytokine storm; pandemic strains differ from seasonal in NS1 IFN antagonism potency.

**→ [STAT1](../../../03-molecular/stat1/)**: Influenza NS1 blocks ISGF3 formation (STAT1/STAT2/IRF9) by dsRNA sequestration and TRIM25 inhibition; PA-X endonuclease degrades host mRNAs including STAT1; H5N1 overcomes STAT1/SOCS1 negative feedback → hyperinflammation; NS1 IFN antagonism distinguishes highly pathogenic from seasonal strains.

**→ [NLRP3 Inflammasome](../../../03-molecular/nlrp3-inflammasome/)**: Influenza M2 proton channel and PB1-F2 (mitochondrial targeting) activate NLRP3 → caspase-1 → IL-1β + IL-18; NLRP3-mediated IL-1β amplifies cytokine storm in severe H5N1 and 1918 H1N1 pneumonia; NLRP3 genetic variants associated with influenza severity; ASC speck formation observed in infected macrophages.

**→ [RIG-I](../../../03-molecular/rig-i/)**: Influenza A 5′ppp genomic ssRNA and dsRNA replication intermediates are the canonical RIG-I ligands; NS1 blocks RIG-I by sequestering dsRNA and inhibiting TRIM25-mediated K63-ubiquitination of RIG-I CARDs; NS1 IFN antagonism strength correlates with pandemic potential.

**→ [Influenza Hemagglutinin](../../../03-molecular/influenza-ha/)**: HA1 head antigenic sites A-E undergo annual drift requiring vaccine reformulation; HA2 stalk BNAbs (CR6261, MEDI8852, FI6v3) are the basis of universal influenza vaccine strategies; α2,6-SA vs α2,3-SA receptor binding specificity determines human transmissibility and pandemic potential.

- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Severe influenza is a disease of the lung: the virus infects alveolar epithelium → diffuse alveolar damage and ARDS (primary viral pneumonia), and by stripping mucociliary defenses it opens the door to the secondary bacterial pneumonia that caused most 1918 deaths.
- `connects-to` → **[Type II Pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — Influenza infects alveolar type I and type II pneumocytes; killing surfactant-producing type II cells collapses alveoli and slashes lung compliance → the diffuse alveolar damage and hyaline membranes of influenza ARDS, most severe with H5N1 and the 1918 strain.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Influenza paves the way for Streptococcus pneumoniae: viral damage to airway epithelium and mucociliary clearance lets pneumococcus colonize the lung, producing the secondary bacterial pneumonia that peaks 5-10 days in and drives much influenza mortality.
- `connects-to` → **[Measles](../measles/README.md)** — Both are vaccine-preventable respiratory viruses but distinct: influenza (orthomyxovirus) drifts and shifts antigenically, needing annual reformulated vaccines, while measles (paramyxovirus) is antigenically stable—one MMR series gives lifelong immunity—yet far more contagious.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Influenza and COVID-19 are the dominant pandemic-capable respiratory viruses, overlapping in presentation but with distinct antivirals (oseltamivir/baloxavir vs nirmatrelvir/remdesivir); they co-circulate seasonally ('flurona' occurs) and both have annually updated vaccines.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Influenza is a potent cardiac trigger: in the week after infection the risk of myocardial infarction rises about six-fold, and the virus can cause myocarditis and decompensate heart failure; influenza vaccination reduces cardiovascular events, so it doubles as cardioprotection.
- `connects-to` → **[RSV](../rsv/README.md)** — Influenza and RSV are the two dominant seasonal respiratory viruses co-circulating each winter: both cause fever, cough, and pneumonia at the extremes of age, both now have older-adult vaccines, and multiplex PCR distinguishes them to guide antivirals and isolation.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Influenza has a striking link to narcolepsy: the 2009 H1N1 pandemic and its Pandemrix vaccine both raised type 1 narcolepsy in HLA-DQB1*06:02 carriers, apparently via molecular mimicry between an H1N1 hemagglutinin epitope and orexin—an infection-triggered autoimmunity.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells clear influenza and shape its vaccines: CD8 T cells recognizing conserved internal viral proteins kill infected cells and give cross-strain protection, which is why universal flu vaccines aim to harness T-cell immunity beyond strain-specific antibodies.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — Severe influenza can cause ARDS: viral pneumonia and an overwhelming inflammatory response flood the alveoli, collapsing gas exchange and requiring ventilation—the lethal end of influenza, often worsened by secondary bacterial pneumonia.
- `connects-to` → **[Guillain-Barré Syndrome](../../05-tissue/guillain-barre/README.md)** — Influenza is a recognized trigger of Guillain-Barré syndrome: the post-infectious autoimmune attack on peripheral-nerve myelin can follow flu (rarely the vaccine, far less than infection)—a reminder that the immune response, not just the virus, causes harm.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells provide early defense against influenza: NK cells kill virus-infected respiratory cells before adaptive immunity engages, and waning NK function with age contributes to the severe influenza and high mortality seen in the elderly.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Alveolar macrophages are central to influenza's outcome: they help clear virus and dead cells but, when overactivated in severe flu, pour out cytokines that injure the lung—so the macrophage response can mean recovery or fatal inflammatory pneumonia.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Influenza is the archetypal acute infection of the respiratory system: the virus infects airway and alveolar epithelium from nose to lung, causing tracheobronchitis and, in severe cases, viral pneumonia—and damaging mucosa enough to invite bacterial superinfection.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Severe and pandemic influenza can trigger a cytokine storm: excessive innate immune activation (notably in H5N1 and 1918-type strains) floods the lungs with inflammatory mediators, causing diffuse alveolar damage and ARDS out of proportion to viral load.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells are the basis of flu vaccination: antibodies against hemagglutinin block infection, but the virus's constant antigenic drift forces yearly reformulated vaccines, and rare antigenic shift—a new HA—can outrun B-cell memory to spark a pandemic.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Influenza opens the door to Staphylococcus aureus: viral damage to the airway lining lets S. aureus (including MRSA) cause severe, sometimes necrotizing secondary pneumonia—one of the deadliest complications, alongside pneumococcal superinfection.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Influenza occasionally strikes the brain: it can cause encephalitis and acute necrotizing encephalopathy, especially in children, and aspirin use during flu risks Reye's syndrome—so neurological symptoms in influenza are a red flag.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy makes influenza dangerous, and the placenta is why protection matters: immune and physiological changes raise the risk of severe flu, so maternal vaccination is recommended—antibodies cross the placenta to shield the newborn too.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Influenza immunity rests on anti-HA antibodies: IgG against hemagglutinin blocks the virus from entering cells, and the flu vaccine works by inducing it—so antigenic drift that changes HA is what forces yearly reformulation.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T-helper cells orchestrate influenza defense and vaccine response: CD4 cells drive the antibody and cytotoxic responses that clear the virus and build memory, so their decline with age partly explains why flu is deadlier and vaccines weaker in the elderly.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Severe influenza recruits neutrophils that injure the lung: swarming to the infected airways, they release enzymes and NETs that, beyond killing virus, damage the delicate gas-exchange surface and worsen the pneumonia.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Severe influenza can damage the kidneys: high fever, dehydration, and muscle breakdown (rhabdomyolysis) plus the systemic inflammatory storm can precipitate acute kidney injury, a marker of severe disease needing hospital care.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 tracks how dangerous a flu has become: this cytokine rises sharply in severe influenza, driving fever and the inflammatory cascade that can tip into cytokine storm and ARDS, so its level helps gauge severity.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Severe influenza starves the blood of oxygen: viral pneumonia and the ARDS it can trigger flood the alveoli, so gas exchange fails and hypoxemic respiratory failure becomes the main threat to life in serious flu.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Influenza and aspirin can wreck a child's liver: giving aspirin during flu can trigger Reye syndrome, a sudden failure of the liver with brain swelling, which is why aspirin is avoided in children with viral illness.
- `connects-to` → **[Pulmonary Surfactant](../../03-molecular/surfactant/README.md)** — Influenza strips the lungs of surfactant: the virus kills the type II pneumocytes that make this alveolar soap, so without it the air sacs collapse and stiffen, deepening the lung injury of severe flu pneumonia.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Severe flu shows on chest X-ray: photons reveal the bilateral infiltrates of viral pneumonia or the lobar consolidation of the bacterial pneumonia that often follows the infection.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Influenza pneumonia floods the alveoli: viral and immune damage to these air sacs fills them with fluid and debris—the diffuse alveolar damage of ARDS that starves the blood of oxygen.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Severe flu ends in acidosis: as gas exchange fails, carbon dioxide and acid build up, and the falling pH of respiratory failure is an ominous sign in flu-related ARDS.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the flu's machinery: spherical virions bristle with two spikes — hemagglutinin to latch onto cells and neuraminidase to escape them — the H and N proteins that name strains like H1N1 and that the vaccines target.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Severe influenza can drop the sodium: the inflammatory stress triggers SIADH, retaining water and diluting blood sodium, a hyponatremia that worsens the confusion and weakness of serious infection.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Flu can hit the gut too: especially in children and with influenza B, the infection brings nausea, vomiting, and diarrhea, the 'stomach flu' symptoms that accompany the classic respiratory illness.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — The flu vaccine is a bet on antibody: it teaches the body to make anti-hemagglutinin antibodies, but the virus's antigenic drift keeps changing that target, which is why the shot must be reformulated and given every year.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The aching muscles are flu's signature: cytokines and direct infection produce the deep myalgia of the illness, and in children influenza can cause a benign acute myositis or, rarely, muscle-breaking rhabdomyolysis.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Influenza's spike clumps red cells: hemagglutinin binds the sialic acid on erythrocytes, agglutinating them — the reaction behind the classic hemagglutination and hemagglutination-inhibition assays used to type the virus and gauge immunity.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy makes flu more dangerous: the immune and lung changes of pregnancy raise the risk of severe influenza and preterm birth, so vaccination in pregnancy protects both mother and, through transferred antibody, the newborn.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Flu can reach the brain: influenza-associated encephalopathy and encephalitis injure neurons, mostly in children, and aspirin given during infection risks the brain-and-liver damage of Reye syndrome.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — In children flu often hits the gut: influenza B especially brings nausea, vomiting, and diarrhea alongside the respiratory illness — true gastrointestinal flu, distinct from the unrelated 'stomach flu' of norovirus.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells set the immune response: they carry flu antigen from the airway to the lymph nodes to prime T and B cells, and plasmacytoid DCs pour out the type I interferon that mounts the early antiviral defense.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Flu is hard on a failing heart: the infection triggers acute decompensation, myocardial infarction, and myocarditis in the weeks after onset, which is why influenza vaccination measurably cuts cardiovascular events.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye can be flu's doorway: avian strains like H7 bind receptors on the conjunctiva, causing conjunctivitis and offering the virus a route of entry that bypasses the airway.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Flu can stop the heart: the acute inflammation of influenza sharply raises the risk of heart attack and stroke in the days after infection, which is why flu vaccination measurably lowers cardiovascular events.
- `connects-to` → **[COPD](../copd/README.md)** — It tips chronic lungs over the edge: influenza is a leading trigger of COPD exacerbations, turning manageable airflow limitation into respiratory failure — the reason annual vaccination is urged in these patients.
- `connects-to` → **[Asthma](../asthma/README.md)** — It sets off the wheeze: influenza is a common trigger of severe asthma attacks, inflaming already twitchy airways, so asthmatics are a priority group for the flu vaccine.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The virus throws the inflammatory switch — and rides it: influenza activates NF-κB to drive the cytokine response, yet the virus also exploits NF-κB signaling for its own efficient replication, a double-edged host pathway.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Severe flu opens the lung to a mold: influenza-associated pulmonary aspergillosis strikes critically ill patients days into ICU care, the damaged airway epithelium and immune paralysis letting Aspergillus invade.
- `connects-to` → **[Stroke](../stroke/README.md)** — Acute infection can trigger a stroke: in the weeks after influenza, the risk of ischemic stroke and heart attack transiently rises as systemic inflammation destabilizes plaques and tips the blood toward clotting.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Secondary bacterial pneumonia turns deadly: influenza strips the airway epithelium, letting Staphylococcus and pneumococcus invade into a post-influenza bacterial pneumonia that can progress to sepsis and shock.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Severe flu can injure the kidney: influenza can cause rhabdomyolysis and, in critical illness, acute kidney injury, and the insult can leave or worsen chronic kidney disease in vulnerable patients.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes and flu worsen each other: people with type 2 diabetes have more severe influenza and complications, while the infection's stress hormones destabilize glycemic control — a reason yearly vaccination is urged.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — It is historically tied to parkinsonism: the encephalitis lethargica that followed the 1918 pandemic left post-encephalitic parkinsonism, and influenza is studied as one infectious contributor to Parkinson's risk.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — It leaves a low-mood aftermath: the post-viral fatigue and neuroinflammation of influenza can produce weeks of depressed mood, part of the broader post-infectious malaise.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Infections may nudge dementia risk: severe influenza and its systemic inflammation are studied as contributors to cognitive decline, and influenza vaccination is associated with lower dementia incidence.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can strike the nervous system: influenza causes febrile seizures and acute encephalopathy, especially in children, and is a recognised trigger of Guillain-Barré syndrome and the rare Reye syndrome.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its outcome is decided by immunity: the immune response clears influenza but its overshoot causes the cytokine-driven damage, and immunocompromised and elderly patients suffer the most severe disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It can upset the gut and liver: influenza, particularly in children, causes nausea, vomiting and diarrhoea, and aspirin use during infection risks the hepatic failure of Reye syndrome.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Severe flu can injure the kidney: influenza-associated rhabdomyolysis and the systemic insult of severe infection can cause acute kidney injury needing supportive care.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It destabilises diabetes: the stress of influenza raises blood glucose and can precipitate diabetic ketoacidosis or hyperosmolar crises, a key reason vaccination is urged in diabetes.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It can deplete the lymphocytes: severe influenza, especially avian H5N1, causes marked lymphopenia — a poor-prognosis marker — alongside the reactive lymphoid response to infection.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Aspirin is dangerous in childhood flu: giving it to children during influenza or chickenpox can trigger Reye syndrome, acute liver failure with encephalopathy, so it is avoided.
- `connects-to` → **[Venous thromboembolism](../venous-thromboembolism/README.md)** — Acute infection is prothrombotic: influenza transiently raises the risk of venous thromboembolism, heart attack and stroke in the weeks after illness.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D status nudges susceptibility: deficiency is associated with more respiratory infection, and supplementation may give a small protective effect against influenza-like illness.
- `connects-to` → **[Oseltamivir](../../../03-medicine/01-modern/05-antiviral/oseltamivir/README.md)** — The mainstay antiviral: oseltamivir, a neuraminidase inhibitor, shortens influenza when started early and is used for treatment and prophylaxis, alongside the newer endonuclease inhibitor baloxavir.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — It opens the door to invasive strep: post-influenza airway damage predisposes to severe group A streptococcal pneumonia and toxic shock, a less common but devastating secondary infection.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — Two pandemic respiratory viruses meet: influenza and SARS-CoV-2 co-circulate and can co-infect, share airborne spread and overlapping severe pneumonia, but differ in antivirals and vaccine strategy.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Newer antivirals beyond oseltamivir: baloxavir, a cap-dependent endonuclease inhibitor, and monoclonal antibodies against haemagglutinin target distinct steps of the influenza life cycle for treatment and prophylaxis.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It strains and inflames the heart: influenza causes myocarditis and sharply raises the risk of acute myocardial infarction in the days after infection — risk that influenza vaccination measurably reduces.
- `connects-to` → **[Zoonosis](../../../02-pathogen/06-environmental/zoonosis/README.md)** — Pandemics come from animals: influenza A reservoirs in wild birds and pigs reassort to create novel strains (avian H5N1, swine H1N1) against which humans have little immunity — the zoonotic antigenic shift behind pandemics.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — It tips blood toward clotting: influenza causes thrombocytopenia and a prothrombotic, inflamed endothelium, part of why heart attacks, strokes and venous thrombosis spike in the weeks after infection.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Not just a respiratory virus: influenza—especially avian strains and infection in children—can infect the gut epithelium, causing the vomiting and diarrhoea of so-called stomach flu.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Why flu shots protect the heart: influenza can rupture atherosclerotic plaques and trigger myocardial infarction, and vaccination measurably lowers post-infection cardiovascular events.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Where flu immunity is built and outpaced: antibody to influenza haemagglutinin matures in germinal centres, but the virus's antigenic drift escapes prior responses, forcing annual revaccination.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Neurological influenza: influenza can cause febrile seizures, encephalopathy and rarely acute necrotising encephalitis in children, occasionally triggering or unmasking epilepsy.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — Dangerous in chronic lung disease: influenza causes severe exacerbations and bacterial superinfection in cystic fibrosis and other chronic lung diseases, making annual vaccination essential.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Viral myositis: influenza is a leading cause of the diffuse myalgia of acute illness and, in children, benign acute viral myositis with calf pain and raised creatine kinase, occasionally with rhabdomyolysis.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Flu and the heartbeat: influenza can cause myocarditis and, through systemic inflammation and hypoxia, precipitate atrial fibrillation and other arrhythmias of the cardiac conduction system.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Severe in pregnancy: pregnant women are at high risk of severe influenza and complications, the basis for prioritising vaccination, which also protects the newborn through transferred antibodies.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Cytokine storm: TNF-α is a leading driver of the hyperinflammatory cytokine storm that, in severe influenza, injures the lung and causes the systemic illness beyond direct viral damage.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Antiviral T-cell signal: IFN-γ from T and NK cells activates macrophages and supports viral clearance in influenza, while contributing to the immunopathology of severe infection.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammasome response: NLRP3-driven IL-1β release amplifies airway inflammation and fever in influenza, balancing protective antiviral immunity against lung injury.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte influx: CCL2 recruits inflammatory monocytes into the influenza-infected lung, where they aid clearance but in severe disease drive the immunopathology behind viral pneumonia and ARDS.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic clearance: CD8 T cells eliminate influenza-infected airway cells through perforin and granzyme, essential for recovery but a source of the epithelial damage in severe infection.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Neutrophilic lung injury: IL-17A drives neutrophil recruitment to the influenza-infected airway, contributing to the excessive inflammation and tissue damage of severe and secondary-bacterial pneumonia.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Oxidized phospholipids and HMGB1 from influenza-damaged lung engage TLR4 on innate cells, a pathway driving the acute lung injury of severe influenza that TLR4 antagonism mitigates in animal models.
- `connects-to` → **[TBK1](../../03-molecular/tbk1/README.md)** — RIG-I sensing of influenza RNA signals through MAVS to TBK1, the kinase that phosphorylates IRF3 to launch the type-I-interferon response central to antiviral defence—a node the virus's NS1 protein works to suppress.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — IL-10 dampens the influenza immune response to limit immunopathology, a protective brake whose balance with effector cytokines determines whether the host clears the virus or suffers the damaging cytokine storm of severe disease.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Secretory IgA on the respiratory epithelium neutralizes influenza at the airway surface and provides cross-protective mucosal immunity, the rationale behind intranasal live-attenuated vaccines that induce it better than injected vaccines.
- `connects-to` → **[MyD88](../../03-molecular/myd88/README.md)** — Plasmacytoid dendritic cells detect influenza RNA through TLR7 signaling via MyD88 to make large amounts of type-I interferon, the endosomal innate-sensing arm complementing the cytosolic RIG-I pathway.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Xanthine-oxidase activity surges during severe influenza, generating reactive oxygen species that damage the alveolar epithelium and contribute to the acute lung injury of severe and fatal infection.
- `connects-to` → **[IRF3](../../03-molecular/irf3/README.md)** — IRF3, activated by the RIG-I/MAVS/TBK1 sensing pathway already mapped, drives the type-I interferon front-line defense against influenza, the response the viral NS1 protein antagonizes.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Influenza induces caspase-3 apoptosis of infected respiratory epithelial cells, both an antiviral defense and a cause of the epithelial damage that opens the airway to secondary bacterial pneumonia.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — The diffuse alveolar damage and hypoxemia of severe influenza pneumonia drive HIF-mediated responses in the injured lung, part of the pathophysiology of influenza ARDS.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Type-I interferon produced through the RIG-I-MAVS-IRF3 axis (all already mapped) signals via JAK-STAT to STAT1 (mapped), inducing the antiviral interferon-stimulated genes that restrict influenza replication.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 from activated dendritic cells drives NK-cell and Th1 IFN-γ responses (already mapped) that augment the cellular clearance of influenza-infected respiratory epithelium.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 opsonizes influenza virions and enhances neutralization, while excessive activation also contributes to the lung immunopathology of severe influenza.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Influenza activates the Raf-MEK-ERK pathway to drive nuclear export of viral ribonucleoproteins, a host-directed antiviral target.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — The influenza NS1 protein activates PI3K-AKT signaling to delay apoptosis and support efficient viral replication.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Influenza modulates mTOR-regulated translation to favor viral protein synthesis during infection.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the macrophage-driven cytokine storm and lung inflammation of severe influenza pneumonia.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response that contributes to the lung pathology of severe influenza.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the lung epithelial repair and fibrosis that follow the diffuse alveolar damage of severe influenza.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic nucleic-acid sensing through cGAS-STING, including mitochondrial DNA from damaged cells, augments the innate antiviral and inflammatory response to influenza.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by recruited neutrophils amplify the lung inflammation and severity of influenza pneumonia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the airway epithelial oxidative-stress and survival responses to influenza infection.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the innate antiviral signaling and inflammatory response to influenza and is also exploited by the virus for replication.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) is activated by influenza NS1 to support viral replication and modulate apoptosis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Influenza modulates host autophagy through its M2 and NS1 proteins to favor its replication and evade degradation.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the airway epithelial and immune-cell responses to influenza and in viral entry.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling, exploited by influenza for its replication, participates in the host response to influenza.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the pulmonary inflammation of severe influenza.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the host immune response to influenza.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the airway leukocyte trafficking and immune responses of influenza.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the airway epithelial and innate immune responses to influenza.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the host antiviral response to influenza.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of the antiviral immune response to influenza.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the leukocyte recruitment and pulmonary inflammation of influenza.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Vaccine and clearance: MHC class II-restricted CD4 help drives the antibody response to haemagglutinin (already mapped) elicited by influenza vaccines, and cross-reactive T-cell help contributes to the heterosubtypic immunity sought by universal-vaccine efforts.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac complications: influenza can cause myocarditis and sharply raises the short-term risk of myocardial infarction, with troponin release marking the cardiac injury that contributes to influenza-associated deaths.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell response: IL-2 drives the expansion of the effector and memory T cells (perforin already mapped) that clear influenza-infected airway epithelium, and the strength of this response shapes recovery and cross-protection.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Fever response: prostaglandin E2 generated during influenza acts on the hypothalamus to produce the fever and malaise of the illness, which is why cyclooxygenase-inhibiting antipyretics relieve these systemic symptoms.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Airway nitric oxide: inducible nitric oxide rises in the influenza-infected airway, contributing both to antiviral defence and, in excess, to the airway inflammation and lung injury of severe infection.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Antibody help: IL-4 and type-2 T-cell help drive the B-cell (already mapped) production of the neutralising antibodies (IgG already mapped) against haemagglutinin that mediate influenza immunity and vaccine protection.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Respiratory acidosis: in severe influenza pneumonia and acute respiratory distress, failing gas exchange retains carbon dioxide, and the accumulation of protons produces the respiratory acidosis that signals impending respiratory failure.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-mediated inflammation: bradykinin generated in the influenza-infected airway raises vascular permeability and stimulates the mucus and inflammation that obstruct the airways, part of the kinin contribution to the respiratory symptoms.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Neurogenic inflammation: CGRP released from airway sensory nerves, with substance-P-type neuropeptides, contributes to the neurogenic inflammation and cough of influenza, part of the neuro-immune dimension of the respiratory infection.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium and virulence: selenium deficiency increases the virulence of influenza and worsens the disease, the antioxidant selenoproteins limiting the viral mutation and the oxidative lung injury (xanthine oxidase already mapped) of infection.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and antiviral immunity: zinc supports the interferon (already mapped) antiviral response and impairs influenza replication, and zinc status influences the immunity that determines the severity of infection.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Omega-3 inflammation resolution: the omega-3 fatty acids give rise to pro-resolving mediators such as protectin D1 that limit the excessive lung inflammation (prostaglandins already mapped) of severe influenza, aiding recovery.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 airway arm: IL-13, with IL-4 (already mapped), is part of the type-2 response that modulates the airway epithelium and contributes to the post-influenza wheeze and the asthma exacerbations it can trigger.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Alveolar oedema: VEGF drives the vascular permeability and the alveolar-capillary oedema of the severe influenza pneumonia (surfactant already mapped), part of the lung injury and ARDS.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and severity: obesity, signalled through the adipokine leptin, is an independent risk factor for severe influenza, the adipose-immune dysfunction impairing the antiviral response.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity (a severe-influenza risk) and the immune-metabolic milieu of the influenza response.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the cytokine (IL-6 already mapped) response to influenza.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Inflammation iron: the IL-6-driven (already mapped) hepcidin of the severe influenza inflammation contributes to the anaemia and the iron dysregulation of the acute illness.
- `connects-to` → **[Influenza A](../../../02-pathogen/01-viruses/influenza-a/README.md)** — Causative virus: the influenza is caused by the influenza virus (the influenza A the pandemic-capable type; the haemagglutinin already mapped), the segmented orthomyxovirus of the antigenic drift and shift.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune response and the asthma-exacerbation link of influenza.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune response to influenza.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the antiviral and antibacterial mucosal defence against influenza and its bacterial superinfection.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Antibody arm: the plasma cells secrete the anti-haemagglutinin (HA already mapped) antibodies that provide the vaccine-induced and convalescent protection against influenza.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Type-2 airway arm: the mast cells, armed by the IgE (already mapped), contribute to the type-2 airway inflammation and the asthma exacerbation (already mapped) triggered by influenza.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the innate inflammatory injury of the severe influenza pneumonia and the cytokine storm.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling drives the neutrophil (already mapped) recruitment and the immunopathology of the severe influenza lung injury.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Immunopathology control: the regulatory T cells restrain the antiviral inflammation and promote the resolution and tissue repair after the influenza infection.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-driven immunopathology of the severe influenza lung injury.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Lectin/classical regulation: the C1-esterase inhibitor regulates the classical and lectin (mannose-binding) complement pathways activated against the influenza virus, a candidate modulator of the lung immunopathology.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Acute-phase iron: transferrin, the iron carrier, reflects the hypoferraemia and disordered iron handling (hepcidin already mapped) of the acute-phase response to the influenza infection.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-lung axis: TSLP, from airway epithelium (already mapped) damaged by influenza, primes dendritic cells (already mapped) and mast cells (already mapped) and amplifies the Th2/eosinophil (already mapped) airway inflammation during and after influenza infection.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Post-influenza anaemia: erythropoietin drives red-cell recovery after the influenza-associated haemophagocytic lymphohistiocytosis (bone-marrow already mapped) and the cytokine-storm (IL-6 already mapped) -driven anaemia of severe influenza.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell-histamine axis: histamine, from mast cells (already mapped) degranulated by the influenza NA protein, amplifies the bronchospasm and the vascular permeability of the influenza-associated airway inflammation and post-viral asthma (already mapped) exacerbation.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Post-viral airway remodelling: periostin, induced in airway epithelium and fibroblasts by the IL-4/IL-13 (already mapped) Th2 response to influenza, drives the ECM remodelling and the post-influenza asthma-exacerbation (already mapped) airway hyperresponsiveness.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian antiviral immunity: melatonin has antiviral and immunomodulatory properties; influenza follows a circadian pattern of severity, and melatonin modulates the innate antiviral type-I-interferon (already mapped) and the NLRP3-inflammasome (already mapped) responses.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Stress-immune neuroendocrine: prolactin, elevated by the febrile stress of influenza infection, enhances lymphocyte (T-helper-cell and B-cell already mapped) activation and the antibody (already mapped) response against the influenza virus.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen immunomodulation: testosterone, via androgen receptors on macrophages (already mapped) and T-helper cells (already mapped), attenuates the cytokine-storm (already mapped) and IL-6 (already mapped) immunopathology; androgen deficiency worsens influenza ARDS severity.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonergic innate axis: serotonin, via 5-HT receptors on macrophages (already mapped) and neurons (already mapped), modulates the cytokine-storm (already mapped) and NLRP3-inflammasome (already mapped) inflammatory axes; serotonin sets the influenza innate immune response severity.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Tolerogenic neuropeptide: oxytocin, via OXTR on macrophages (already mapped) and regulatory T cells (already mapped), attenuates the cytokine-storm (already mapped) and IL-6 (already mapped) immunopathology; oxytocin promotes immune resolution after severe influenza infection.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Influenza vasopressin: vasopressin, via V1aR on macrophages (already mapped) and neurons (already mapped), modulates cytokine-storm (already mapped) and NF-κB (already mapped) immunopathology; vasopressin excess amplifies IL-6 (already mapped) and NLRP3 (already mapped) cascade.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Influenza iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and dendritic-cell (already mapped) antiviral innate immunity; iodine deficiency impairs type-I-interferon (already mapped) and NF-κB (already mapped) antiviral responses against influenza.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Influenza magnesium: magnesium stabilises NLRP3 inflammasome (already mapped) and attenuates NF-κB (already mapped) and cytokine-storm (already mapped) immunopathology; magnesium deficiency impairs macrophage (already mapped) and NK-cell (already mapped) antiviral function.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Influenza calcium: calcium, as second messenger in macrophages (already mapped) and neutrophils (already mapped), coordinates antiviral signalling; calcium dysregulation amplifies the NF-κB (already mapped) and cytokine-storm (already mapped) cascade of influenza.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Influenza iron: iron, regulating innate immune enzyme activity in macrophages (already mapped) and NK cells (already mapped), supports antiviral defence; iron deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cytokine cascade of influenza.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Influenza potassium: potassium depletion promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; potassium deficiency amplifies the NF-κB (already mapped) and NLRP3 (already mapped) cytokine-storm (already mapped) cascade of influenza.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Influenza copper: copper, in macrophages (already mapped) and NK cells (already mapped), scavenges viral-driven ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cytokine cascade of influenza.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Influenza phosphorus: phosphorus, as ATP in macrophages (already mapped) and NK cells (already mapped), fuels antiviral immune responses; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and cytokine-storm (already mapped) cascade of influenza.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Influenza chloride: chloride regulates macrophage (already mapped) and NK cells (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and cytokine-storm (already mapped) innate immune cascade of influenza.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Influenza carbon: carbon as backbone of viral glycoproteins and cytokines (already mapped) sustains replicative signalling; carbon metabolites in macrophages (already mapped) and NK cells (already mapped) amplify NF-κB (already mapped) and IL-6 (already mapped) in influenza.

- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Influenza nitrogen: nitrogen in viral proteins and cytokines (already mapped) sustains signalling; nitrogen-derived RNS from macrophages (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) and cytokine-storm (already mapped) cascade of influenza.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Influenza sulfur: sulfur-containing amino acids in macrophages (already mapped) and NK cells (already mapped) regulate redox signalling; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and cytokine-storm (already mapped) cascade of influenza.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Influenza pd-1: PD-1 on T-cytotoxic cells (already mapped) and NK cells (already mapped) suppresses antiviral immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and cytokine-storm (already mapped) cascade of influenza.