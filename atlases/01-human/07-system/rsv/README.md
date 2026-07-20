---
schema: human-scale-entry/v1
id: rsv
name: RSV
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "RSV (pneumovirus; negative-sense ssRNA) is the leading cause of infant bronchiolitis and severe LRTI in elderly/immunocompromised; NS1/NS2 block MAVS/IFN-β; nirsevimab (anti-F mAb) prevents severe infant RSV; mRNA-1345 (Abrysvo) and mResvia approved 2023 for adults 60+."
aliases: ["RSV", "respiratory syncytial virus", "RSV bronchiolitis", "infant RSV", "nirsevimab", "Beyfortus", "palivizumab", "Synagis", "Abrysvo", "mResvia", "mRNA-1345", "RSV-A", "RSV-B", "RSV pneumonia", "pneumovirus", "RSV vaccine"]
sources:
  - id: shi-2017-rsv-global-burden
    type: peer-reviewed
    cite: "Shi T, McAllister DA, O'Brien KL, et al. Global, regional, and national disease burden estimates of acute lower respiratory infections due to respiratory syncytial virus in young children in 2015: a systematic review and modelling study. Lancet. 2017;390(10098):946-958."
    doi: "10.1016/S0140-6736(17)30938-8"
    pmid: "28689664"
    url: "https://doi.org/10.1016/S0140-6736(17)30938-8"
    accessed: "2026-06-08"
  - id: hammitt-2022-nirsevimab-trial
    type: peer-reviewed
    cite: "Hammitt LL, Dagan R, Yuan Y, et al. Nirsevimab for Prevention of RSV in Healthy Late-Preterm and Term Infants. N Engl J Med. 2022;386(9):837-846."
    doi: "10.1056/NEJMoa2110275"
    pmid: "35196424"
    url: "https://doi.org/10.1056/NEJMoa2110275"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/rsv-f-protein
    relation: connects-to
    note: "RSV F (fusion) protein mediates attachment and viral-host membrane fusion → syncytium formation; prefusion F (site Ø) is the primary neutralizing epitope; nirsevimab (site Ø mAb) and mRNA vaccines (mRNA-1345) target prefusion F for RSV prevention."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "RSV NS1 degrades TRIM25 → prevents RIG-I K63-ubiquitination → impairs RIG-I/MAVS signaling; NS2 blocks STAT2 → suppresses ISGs; NS1+NS2 blunt IFN-β → RSV replicates in immunocompetent airways; IFN-λ (type III IFN) is the dominant innate mucosal antiviral defense against RSV."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "RSV airway epithelial infection → IL-33 release (DAMP) from epithelial nuclei → ST2+ ILC2 activation → IL-4/IL-5/IL-13 → type 2 inflammation, eosinophilia, mucus; RSV-IL-33 axis drives early-life wheeze and subsequent asthma sensitization."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "RSV-induced airway epithelial damage → TSLP release → TSLP receptor on ILC2/basophils → IL-4/IL-13 → Th2 polarization and IgE production; neonatal TSLP sensitization after RSV infection may explain the RSV-asthma epidemiological link in childhood; tezepelumab blocks TSLP."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "RSV NS1/NS2 cooperatively block type I IFN: NS1 targets TRIM25/IRF3; NS2 prevents STAT2 nuclear translocation → ISG suppression; IFN-λ (type III) dominates innate mucosal defense against RSV; preterm infants with immature IFN response have more severe RSV bronchiolitis."
  - target: 02-pathogen/01-viruses/respiratory-syncytial-virus
    relation: connects-to
    note: "Respiratory syncytial virus, a negative-sense RNA pneumovirus, fuses airway cells into syncytia and blunts interferon with NS1/NS2; it reinfects throughout life because the G protein varies and memory is short, yet prefusion-F antibodies and vaccines now prevent severe disease."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "RSV is the top cause of infant bronchiolitis and a major cause of pneumonia in the elderly and immunocompromised: it infects ciliated airway epithelium, sloughing cells and plugging small airways with mucus → air trapping, hypoxia, and wheeze; care is supportive."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Severe RSV bronchiolitis in infancy is the strongest environmental risk factor for childhood asthma: epithelial damage releases IL-33 and TSLP that activate ILC2s toward type-2 inflammation, biasing the developing airway toward allergic sensitization and recurrent wheeze."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "RSV and COVID-19 are enveloped respiratory RNA viruses that with influenza drive seasonal lower-respiratory disease; both cause bronchiolitis/pneumonia at the extremes of age, both evade interferon, and both are now vaccine-preventable in older adults."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "RSV is a major trigger of COPD exacerbations: it infects airway epithelium → neutrophilic inflammation and bronchospasm → acute decompensation, and is found in a substantial share of hospitalized exacerbations; older-adult RSV vaccines (Arexvy, Abrysvo) reduce this burden."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "RSV infects airway epithelium and alveolar pneumocytes including type II cells: replication plus NS1/NS2 interferon evasion drives epithelial necrosis, sloughing and syncytia that plug bronchioles → the airway obstruction of infant bronchiolitis and impaired surfactant."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "RSV and influenza are the two dominant seasonal respiratory viruses, co-circulating each winter: both cause fever, cough, and pneumonia at the extremes of age, both now have older-adult vaccines, and PCR tells them apart—but RSV adds nirsevimab prophylaxis for infants."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "RSV is the leading cause of lower respiratory infection in infants: it targets bronchiolar epithelium, causing the airway plugging and wheeze of bronchiolitis, the top cause of infant hospitalization—so the respiratory system's smallest airways bear the brunt."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "RSV skews the infant immune response toward Th2: instead of protective Th1 immunity it elicits Th2 cytokines (IL-4, IL-13) and eosinophils, which worsen disease and may link severe RSV bronchiolitis to later asthma—why early RSV is more than a transient infection."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are central to RSV defense and disease: alveolar macrophages sense the virus and make interferon, but RSV also infects and subverts them, and excessive macrophage-driven inflammation contributes to the airway damage of severe bronchiolitis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "RSV is an underrecognized trigger of heart failure decompensation: RSV respiratory infection strains the cardiovascular system, precipitating acute heart-failure exacerbations and excess cardiac deaths—why RSV vaccination is now recommended for older adults."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "Severe RSV can progress to ARDS: intense bronchiolitis and alveolar inflammation flood the lungs and collapse gas exchange, requiring ventilation—the most severe end of the RSV spectrum, where a common childhood virus becomes life-threatening."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "RSV bronchiolitis plugs the airways with neutrophils and debris: the virus and the neutrophil-rich inflammatory response slough airway cells and mucus into the tiny bronchioles, obstructing them—why infants wheeze and the smallest airways collapse in severe RSV."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "RSV is prevented with passive antibody, not a vaccine, in infants: monoclonal IgG antibodies (palivizumab, nirsevimab) against the F protein give infants immediate protection—a rare reliance on borrowed antibody for a virus where natural immunity is weak."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "RSV evades durable immunity and reinfects for life: it blunts interferon and induces only short-lived, incomplete immune memory, so people are reinfected repeatedly—and the immature or aged immune system makes RSV dangerous at both ends of life."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "RSV prevention now rests on antibodies, not active immunity: the monoclonal nirsevimab and the maternal RSVpreF vaccine both supply or elicit B-cell antibodies against the F protein, protecting infants through passive immunity during their first vulnerable season."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "The placenta is key to protecting newborns from RSV: vaccinating mothers in late pregnancy lets anti-RSV antibodies cross the placenta, so the baby is born already armed against severe bronchiolitis in its first months—passive immunity by maternal transfer."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "RSV makes airway smooth muscle the villain of wheeze: infection and inflammation make bronchiolar smooth muscle constrict and the airways narrow, causing the wheezing of bronchiolitis—and repeated early RSV is linked to later asthma and airway reactivity."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells both clear and harm in RSV: CD8 T cells eliminate infected airway cells to end infection, but their response also drives lung immunopathology—a balance central to why severe bronchiolitis injures infant airways."
  - target: 01-human/03-molecular/surfactant
    relation: connects-to
    note: "RSV cripples the airway's surfactant defense: it infects and sloughs the epithelial and type-II cells that make pulmonary surfactant, so airways collapse and plug with debris—the bronchiolitis that obstructs an infant's tiny airways."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "RSV bronchiolitis drives Th2 IL-13 and later wheeze: the infection skews immunity toward IL-13, boosting mucus and airway reactivity, which is part of why severe infant RSV is linked to later asthma."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "RSV bronchiolitis is dangerous because it starves infants of oxygen: inflamed, mucus-plugged small airways trap air and drop blood oxygen, so supplemental oxygen and breathing support—not antivirals—are the mainstay of treating a severe case."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK cells are an early shield against RSV: they kill infected airway cells before antibodies form, and weak NK responses in young infants and the elderly help explain why those age groups suffer the worst disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "RSV outwits dendritic cells: the virus blunts these antigen-presenters' ability to prime strong, lasting T-cell immunity, which helps explain why RSV reinfects people throughout life and why a durable vaccine took decades to achieve."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "RSV can hit the infant brain: in the youngest babies it triggers sudden apnea—pauses in breathing that may be the first sign—and rare cases cause seizures or encephalopathy, so very young infants are watched closely."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Severe RSV throws off sodium: bronchiolitis is a classic trigger of SIADH, in which the body retains water and dilutes blood sodium, so hyponatremia can develop and provoke seizures if IV fluids are not chosen carefully."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "RSV stirs the airway's mast cells: their release of mediators adds to the wheeze of bronchiolitis, and severe early RSV is linked to later asthma, hinting these cells help bridge infection to allergic airway disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "RSV bronchiolitis shows on chest X-ray as hyperinflation and patchy atelectasis in X-ray photons, used when a baby's breathing worsens—though imaging is not needed for the routine diagnosis."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Severe RSV reaches the alveoli: beyond plugging the small bronchioles, it inflames the alveolar units into pneumonia, flooding gas exchange and causing the worst of the hypoxia."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "A tiring RSV baby retains carbon dioxide: rising CO2 and the falling pH of respiratory acidosis signal that breathing is failing and that ventilatory support may be needed."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows how RSV earns its name: the enveloped, filamentous virions fuse infected airway cells into multinucleated giant cells — the syncytia — that slough off and plug the tiny airways in bronchiolitis."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "RSV can strain the heart at the extremes of life: in fragile infants and older adults it precipitates heart failure and, rarely, myocarditis, the cardiorespiratory stress of severe infection tipping a marginal heart over the edge."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Severe bronchiolitis unsettles the kidney's salt balance: sick RSV infants often develop SIADH with hyponatremia, while poor feeding and fever bring dehydration that can stress the kidneys."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "RSV is fought largely with antibody: the monoclonals palivizumab and the longer-acting nirsevimab passively protect high-risk infants, and a maternal vaccine now passes protective antibody across the placenta to the newborn."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "In the youngest infants RSV can stop the breath: it triggers central apnea — pauses in breathing driven by immature brainstem respiratory neurons — sometimes the first sign of infection before the wheeze appears."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Bronchiolitis makes feeding a struggle: a baby working hard to breathe cannot coordinate sucking and swallowing, so poor intake and vomiting bring dehydration and the need for nasogastric or IV fluids."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Protection now starts before birth: a maternal RSV vaccine given in pregnancy passes antibody across the placenta to shield the newborn through its risky first months, complementing the nirsevimab antibody given to infants directly."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D may temper the infection: low vitamin D in infancy is associated with more severe RSV bronchiolitis, the vitamin's role in airway immunity and barrier function making its status a studied modifier of risk."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "A key lesson is what cortisol cannot do: unlike asthma, RSV bronchiolitis does not respond to corticosteroids, because its airway plugging is driven by sloughed cells and mucus rather than the steroid-sensitive inflammation of allergic disease."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "RSV opens the door to bacteria: by stripping the airway lining and blunting defenses it primes the lung for secondary pneumococcal pneumonia, a viral-bacterial synergy that drives much of the severe illness and death in infants and the elderly."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells decide how much the infection hurts: they rein in the antiviral response so it clears RSV without shredding the airway, and too few of them tip the balance toward immunopathology and a Th2-skewed, wheezy course."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "RSV lights up IL-6 in the airway: infected epithelium and macrophages pour out this cytokine, and high IL-6 in nasal secretions tracks with the inflammation and severity of infant bronchiolitis."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "Sensing the virus flips the interferon switch: RSV RNA detected through the RIG-I/MAVS pathway activates IRF3, the transcription factor that turns on type I interferon — and which the virus's NS proteins work to suppress."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "The damaged airway invites a second germ: RSV strips the respiratory epithelium and blunts defenses, opening the door to bacterial superinfection by Staphylococcus aureus and other organisms that worsen the pneumonia."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Early infection may reshape the lung for life: RSV bronchiolitis activates airway fibroblasts and remodeling, part of why severe infant infection is linked to later wheezing and asthma."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The virus throws the airway's inflammation switch: RSV activates NF-κB in respiratory epithelium, driving the chemokine and cytokine release that recruits the neutrophils and mucus plugging behind bronchiolitis."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Severe infant disease can spiral to sepsis: RSV bronchiolitis can progress to respiratory failure, and bacterial superinfection of the damaged lung can seed bloodstream infection and a sepsis-like critical illness."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can reach beyond the lungs to the brain: severe RSV in young infants is associated with central apnea, seizures and rare encephalopathy, CNS complications that can dominate the acute illness."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "A virus can clear the way for group A strep: RSV injury to the airway epithelium can be followed by invasive Streptococcus pyogenes, causing necrotizing pneumonia, empyema and toxic shock that turn a viral illness fulminant."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "In the immunocompromised it opens a fungal door: severe RSV in transplant and leukemia patients damages the lung and prompts steroids, setting the stage for secondary invasive pulmonary aspergillosis."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Fragile hearts tolerate it worst: infants with congenital heart disease and pulmonary hypertension suffer the most severe RSV, as the bronchiolitis raises pulmonary pressures and strains an already burdened right heart."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "It turns deadly in the neutropenic host: in leukemia patients like those with AML, RSV readily progresses from the upper airway to fatal pneumonia, a major respiratory-virus threat during chemotherapy-induced immunosuppression."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Post-transplant lungs are defenseless against it: hematopoietic stem-cell recipients, especially with graft-versus-host disease on immunosuppression, suffer severe RSV pneumonia, a leading cause of post-transplant respiratory failure."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Damaged, immunosuppressed lungs fare badly: patients with lung cancer such as NSCLC, with their structural lung disease and treatment-related immunosuppression, are prone to severe RSV lower-respiratory infection."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Like influenza, it strains the heart: RSV infection in older adults triggers acute cardiovascular events and decompensation, precipitating arrhythmias, heart failure and myocardial infarction."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Bronchiolitis stops infants feeding: the tachypnoea and nasal congestion of RSV make young babies unable to feed, causing poor intake and dehydration that often drives the need for hospital admission."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Severe disease threatens the kidneys: dehydration from poor feeding and the hypoxia and sepsis of severe RSV can cause acute kidney injury, especially in infants and frail older adults."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can drop the blood sodium: severe RSV bronchiolitis is a recognised cause of SIADH with hyponatraemia in infants, requiring careful fluid management during hospital care."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It can inflame the muscles: like other respiratory viruses, RSV causes myalgia, and in children benign acute viral myositis with calf pain and raised creatine kinase can follow infection."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Distress shows on the skin: in severe infant bronchiolitis RSV causes perioral and peripheral cyanosis with mottled, poorly-perfused skin, visible warning signs of respiratory failure."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It rouses the airway's lymphoid tissue: RSV bronchiolitis provokes a brisk peribronchial lymphocytic infiltrate and reactive lymphadenopathy as the immune system responds."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "It opens the door to pneumococcus: RSV damages the airway epithelium and predisposes to secondary bacterial pneumonia, classically from Streptococcus pneumoniae."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Severe disease invites staph superinfection: severe RSV bronchiolitis can be complicated by secondary staphylococcal pneumonia, especially in young infants."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: connects-to
    note: "A fellow winter respiratory virus: influenza A co-circulates with RSV, causes overlapping bronchiolitis and pneumonia, and the two can co-infect, though influenza has antivirals and annual vaccines that RSV long lacked."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids do not help routine cases: trials show systemic corticosteroids do not shorten RSV bronchiolitis in healthy infants and are not recommended, though they treat associated viral wheeze and croup."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Nutrition shapes defence: zinc supports mucosal immunity and is studied to reduce the severity of childhood respiratory infections including RSV bronchiolitis in deficient populations."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Monoclonal antibodies prevent it: palivizumab and the long-acting nirsevimab are anti-RSV-F monoclonal antibodies given to infants for passive immunoprophylaxis, blocking the fusion protein the virus uses to enter cells."
  - target: 01-human/05-tissue/lung-slice
    relation: connects-to
    note: "It plugs the small airways: RSV bronchiolitis sloughs necrotic airway epithelium that, with mucus and inflammatory debris, obstructs the bronchioles, causing the air-trapping and wheeze of severe infection."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "A high-risk chronic airway disease: children with cystic fibrosis suffer more severe and prolonged RSV infections that accelerate their airway damage, making RSV prevention important in this group."
  - target: 01-human/07-system/measles
    relation: connects-to
    note: "A fellow paramyxovirus: respiratory syncytial virus and measles are related enveloped RNA viruses, but RSV (a pneumovirus) causes bronchiolitis in infants while measles causes a systemic rash and immune amnesia—contrasting outcomes of related viruses."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It can strain and inflame the heart: severe RSV causes myocarditis in infants and triggers acute cardiac events such as ischaemia and heart failure in older adults, so cardiac involvement adds to its respiratory toll."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Where protective antibody is made: neutralizing antibody to the RSV prefusion-F protein is generated in germinal centres, the response boosted by the maternal RSV vaccine—while nirsevimab supplies it passively."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Early infection and the atopic march: severe infant RSV bronchiolitis is linked to later recurrent wheeze and asthma within the broader atopic march that begins with atopic dermatitis."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Inflammation injures the lung: severe RSV bronchiolitis and pneumonia drive an exaggerated cytokine response that, like other cytokine storms, damages airways and alveoli beyond direct viral cytopathic effect."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Neurological complications: severe RSV in infants can cause apnoea, seizures and encephalopathy, occasionally leaving lasting neurological sequelae beyond the airway disease itself."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Microbiome shapes the response: the early-life airway and gut microbiome modulate the severity of RSV bronchiolitis and the subsequent risk of asthma, with dysbiosis tilting the immune response toward worse disease."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Acute chest syndrome trigger: RSV and other respiratory viruses precipitate acute chest syndrome in sickle cell disease, a leading cause of death, so viral lower-respiratory infection is especially dangerous in SCD."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Post-viral airway scarring: severe RSV bronchiolitis can lead to bronchiolitis obliterans, where fibrosis narrows and obliterates the small airways long after the infection clears."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "Viral RNA sensing: the RIG-I receptor detects RSV genomic RNA and signals through MAVS to launch the type-I interferon response that constrains the infection."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 skewing: RSV bronchiolitis biases the infant immune response toward IL-4-driven Th2 inflammation, a pathway linked to the later development of wheeze and asthma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil recruitment: IL-5 mobilised during the Th2 response to RSV draws eosinophils into the airways, contributing to mucus and the post-bronchiolitis wheezing phenotype."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: RSV viroporin SH and other viral proteins trigger the NLRP3 inflammasome in airway cells, releasing IL-1β that amplifies the inflammation of severe bronchiolitis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Neutrophilic airways: IL-17A drives the neutrophil-dominated airway inflammation and mucus hypersecretion that mark severe RSV bronchiolitis, distinct from the eosinophilic Th2 arm."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Inflammatory recruitment: CCL2 produced by infected airway epithelium draws monocytes and macrophages into the lung, fuelling the immunopathology that obstructs the small airways in RSV bronchiolitis."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "F-protein sensing: the RSV fusion (F) protein engages TLR4 on airway and immune cells, triggering the NF-κB-driven cytokine response that contributes to the innate inflammation of RSV infection."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 balance: IFN-γ from Th1 cells counterbalances the Th2 skew that predisposes infants to severe RSV bronchiolitis, and a weak Th1 response is associated with worse disease and later wheezing."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic clearance: perforin-mediated CD8 T-cell killing of infected airway epithelium clears RSV but also contributes to the lung injury, the double-edged cytotoxic response central to recovery and to immunopathology."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Monoclonal prophylaxis: the anti-F-protein antibody nirsevimab carries an FcRn-binding (YTE) modification that extends its half-life to protect infants across a whole RSV season with one dose, the passive-immunisation strategy that has transformed prevention."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal defence: secretory IgA on the airway surface neutralises RSV at the portal of entry, the first-line mucosal antibody whose relative immaturity in infancy is one reason the very young suffer the most severe bronchiolitis."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Neurogenic inflammation: RSV upregulates substance P and its NK1 receptor in the airways, driving neurogenic inflammation, mucus secretion and the airway hyper-reactivity that contributes to the wheeze of bronchiolitis and post-RSV wheezing."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Atopy link: RSV bronchiolitis in infancy promotes Th2 sensitisation and IgE production (with the IL-4/IL-5/IL-13 already mapped), the mechanism linking severe early RSV to later recurrent wheeze and asthma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome bronchiolitis: RSV activates the NLRP3 inflammasome (already mapped) to release IL-1β, amplifying the airway inflammation and neutrophil recruitment of severe bronchiolitis."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Epithelial death: RSV induces caspase-3 apoptosis of infected airway epithelial cells, and the resulting epithelial sloughing — with mucus and the syncytia that name the virus — plugs the small airways in bronchiolitis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate amplification: TLR4 sensing of RSV F protein (RSV-F and TLR4 mapped) signals through MyD88 to NF-κB (mapped), driving the airway inflammatory response of RSV bronchiolitis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Interferon evasion: type-I interferon signals through STAT1 to mount the antiviral response, which the RSV NS1 and NS2 proteins antagonise — blunting interferon and enabling viral replication."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune regulation: IL-10 modulates the Th2-skewed immunopathology (IL-4, IL-5 and IL-13 mapped) of severe RSV bronchiolitis, balancing viral control against airway damage."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Type-I-interferon and cytokine signalling through JAK-STAT (STAT1 mapped) governs the antiviral and Th2-skewed immune response to RSV bronchiolitis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Airway hypoxia during severe RSV bronchiolitis stabilises HIF-1α, shaping the inflammatory and epithelial response to infection."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "RSV activates PI3K-AKT signalling to promote epithelial-cell survival and support viral replication, a host pathway exploited during infection."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the airway inflammation and mucus-associated immunopathology of RSV bronchiolitis in infants."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response that contributes to the airway pathology of severe RSV infection."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the airway remodelling and the link between severe infant RSV bronchiolitis and later wheezing and asthma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates airway epithelial oxidative-stress and survival responses to RSV infection."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by recruited neutrophils amplify the airway inflammation and mucus obstruction of severe RSV bronchiolitis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling activated by RSV in airway epithelium promotes mucin production and the inflammatory response of RSV bronchiolitis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven airway inflammation and the innate immune response to respiratory syncytial virus."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling regulates the immune-cell metabolism and memory-response programming to respiratory syncytial virus."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) is exploited by respiratory syncytial virus to support its replication and modulate airway epithelial survival."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Respiratory syncytial virus modulates host autophagy, which shapes the innate immune and inflammatory response to infection."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the airway epithelial and immune-cell responses to respiratory syncytial virus."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling modulates the airway epithelial and immune-cell responses to respiratory syncytial virus."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the airways contributes to the bronchiolitis and immunopathology of RSV infection."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the immune response to respiratory syncytial virus."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the airway leukocyte trafficking of RSV infection."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the innate antiviral and inflammatory responses to respiratory syncytial virus."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the host response to respiratory syncytial virus."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation and airway immune response to respiratory syncytial virus."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Vaccine immunity: MHC class II-restricted CD4 T-cell help drives the antibody responses to the RSV F protein (already mapped) targeted by maternal and older-adult vaccines, and a Th2-skewed version of this help historically caused vaccine-enhanced disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Airway smooth muscle: RSV infection provokes bronchospasm and the recurrent wheeze that can follow bronchiolitis through calcium-dependent airway smooth muscle contraction and heightened airway responsiveness."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell response: IL-2 drives the expansion of the RSV-specific effector and memory T cells that clear infected airway epithelium, and the balance of this response shapes both protection and the immunopathology of severe bronchiolitis."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Wheeze and Th2: histamine release accompanies the type-2, allergic-like response to RSV (IL-4/IL-13 already mapped), contributing to the airway oedema and wheeze of bronchiolitis and to the post-viral airway reactivity."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Airway nitric oxide: RSV alters epithelial nitric-oxide production, and NO both participates in antiviral defence and, in excess, contributes to the airway inflammation and vascular changes of severe bronchiolitis."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory mediators: prostaglandins and other lipid mediators generated during RSV infection promote the airway inflammation, mucus secretion and bronchoconstriction that obstruct the small airways in bronchiolitis."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative airway injury: RSV infection generates reactive oxygen species, to which xanthine oxidase contributes, in the airway epithelium, and this oxidative stress amplifies the inflammation and epithelial damage of bronchiolitis."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Neurogenic inflammation: CGRP released from airway sensory nerves, with substance P (already mapped), contributes to the neurogenic inflammation and the exaggerated airway responses of RSV bronchiolitis, part of its neuro-immune dimension."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-mediated inflammation: bradykinin generated in the RSV-infected airway raises vascular permeability and stimulates the mucus secretion and bronchoconstriction that obstruct the small airways of bronchiolitis."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxaemia of bronchiolitis: the small-airway obstruction and mucus plugging of RSV bronchiolitis impair gas exchange, causing the hypoxaemia that drives the supplemental oxygen and high-flow support that are the main reason for hospital admission."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Exacerbations and adult burden: RSV causes exacerbations of COPD and severe respiratory illness in older adults, the burden that the new RSVpreF vaccines targeting the F protein (already mapped) aim to prevent."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Th2-skewing dendritic cells: the airway dendritic cells present RSV antigen and shape the type-2-skewed (IL-4, IL-5 and IL-13 already mapped) immune response that contributes to the wheeze and the immunopathology of infection."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and antiviral immunity: zinc is an antiviral and immune-modulating trace metal, and its deficiency, common in undernourished infants, worsens the severity of the respiratory viral infections including RSV."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Airway oedema: VEGF drives the vascular permeability and airway oedema that, with the epithelial debris (surfactant already mapped), plug the small bronchioles in RSV bronchiolitis."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Bronchiolitic hypoxaemia: the small-airway plugging and ventilation-perfusion mismatch of RSV bronchiolitis cause the hypoxaemia whose correction with supplemental oxygen is the mainstay of the supportive care of infants."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Nutritional-immune adipokine: leptin is the adipokine of the immune-metabolic milieu; the infant nutritional status (leptin) modulates the immune response to RSV."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of the RSV infection."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the inflammatory (IL-6 already mapped) milieu of RSV bronchiolitis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 antiviral arm: IL-12 polarises the protective Th1 (IFN-γ already mapped) antiviral response that counter-balances the pathogenic Th2 (IL-4, IL-5 and IL-13 already mapped) skewing of RSV bronchiolitis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Th2 airway remodelling: periostin, downstream of the type-2 cytokines (IL-13 already mapped) and the alarmins (IL-33 and TSLP already mapped), marks the Th2 airway remodelling linking severe RSV bronchiolitis to the later asthma (already mapped)."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement immunopathology: the complement C5 activation contributes to the RSV bronchiolitis immunopathology (and the historical enhanced disease of the formalin-inactivated vaccine)."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neutrophilic (already mapped) inflammation of severe RSV bronchiolitis."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Antibody arm: the plasma cells secrete the anti-F-protein antibodies (already mapped); the passive antibody (palivizumab/nirsevimab, maternal RSVpreF) targets the same F protein (already mapped) to protect infants from RSV."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Type-2 airway itch: IL-31, a type-2 (IL-4, IL-5 and IL-13 already mapped) cytokine, is part of the type-2 response linking the severe RSV bronchiolitis to the later atopy and asthma (already mapped)."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the complement-driven airway inflammation of severe RSV bronchiolitis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: RSV recruits the host factor H (via its G glycoprotein) to inactivate the C3 convertase (complement C3, C5 and C5aR1 already mapped) and evade the complement attack."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "Atopic-march type-2: RSV bronchiolitis shares the type-2 (IL-4, IL-5, IL-13, TSLP and IL-31 already mapped) immunity of the atopic march with prurigo nodularis, another type-2 disease of the shared-biologic era."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways (C3, C5, C5aR1 and factor H already mapped) engaged against RSV, a pathway the virus partially evades."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Airway matricellular: osteopontin, produced in the RSV-infected airway, is a matricellular cytokine amplifying the type-2 and myeloid inflammation of RSV bronchiolitis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Acute-phase iron: transferrin, the iron carrier, reflects the hypoferraemia and disordered iron handling of the acute-phase response to the RSV lower-respiratory-tract infection."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoiesis support: erythropoietin counteracts the anaemia driven by the cytokine storm (IL-6 already mapped) and NLRP3 inflammasome (already mapped) activation of severe RSV disease, supporting erythropoiesis during lower-respiratory-tract infection."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Antiviral immunomodulator: melatonin, acting via MT1/MT2 receptors on macrophages (already mapped) and NK cells (already mapped), inhibits NLRP3 inflammasome (already mapped) activation and attenuates the cytokine storm of severe RSV infection."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune stimulator: prolactin, via its receptor on NK cells (already mapped), macrophages (already mapped), and T cells (already mapped), promotes antiviral effector responses and modulates the Th1/Th2 balance of RSV immunity."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Neuroimmune antiviral modulator: oxytocin, via oxytocin receptors on macrophages (already mapped) and T cells (already mapped), suppresses the pro-inflammatory cytokine (IL-6 and TNF-α already mapped) storm and the airway hyperreactivity of severe RSV infection."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-mediated sex-differential severity: testosterone, acting via androgen receptors on innate immune cells, suppresses the pro-inflammatory cytokine (IL-6 and TNF-α already mapped) responses and underlies the greater severity of RSV disease in males vs. females."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant antiviral micronutrient: selenium, incorporated into selenoproteins (GPx and thioredoxin reductase), suppresses the ROS-driven oxidative stress and the NF-κB-mediated (already mapped) inflammatory cytokine burst in the airway epithelium during RSV infection."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "RSV serotonin: mast-cell (already mapped) serotonin amplifies the IgE (already mapped) and IL-33 (already mapped) airway hyperresponsiveness of RSV; 5-HT2 on smooth-muscle cells (already mapped) promotes bronchospasm and T-helper-cell (already mapped) Th2 skew."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "RSV vasopressin: vasopressin, released during severe RSV-induced respiratory distress, promotes SIADH and the sodium (already mapped) hyponatraemia of RSV in infants; vasopressin also modulates the lung (already mapped) vascular tone and brain (already mapped) oedema of RSV."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "RSV magnesium: magnesium acts as a bronchodilator by inhibiting calcium-mediated smooth-muscle cell (already mapped) constriction; magnesium deficiency amplifies the IL-33 (already mapped) and type-I IFN (already mapped) inflammatory airway response to RSV."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "RSV iodine: iodine-dependent thyroid hormones upregulate type-I IFN (already mapped) antiviral signalling on airway epithelium; hypothyroidism impairs the NF-κB (already mapped) response and amplifies the IL-6 (already mapped) and IL-33 (already mapped) cytokine storm of RSV."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "RSV copper: copper, as SOD and ceruloplasmin cofactor, suppresses the ROS amplifying NF-κB (already mapped) and NLRP3 inflammasome (already mapped) airway cytokine burst of RSV; copper deficiency impairs macrophage (already mapped) bactericidal and antiviral function."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "RSV potassium: potassium efflux is the canonical activating signal for NLRP3 inflammasome (already mapped) in macrophages (already mapped); disrupted K⁺ homeostasis amplifies NF-κB (already mapped) and IL-1β (already mapped) cytokine storm of severe RSV infection."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "RSV iron: iron, as cofactor for ribonucleotide reductase in type-ii-pneumocytes (already mapped) and macrophages (already mapped), supports antiviral immunity; iron overload amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative-stress cascade of RSV bronchiolitis."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "RSV phosphorus: phosphorus, as ATP precursor in neutrophils (already mapped) and macrophages (already mapped), fuels phagocytic burst; phosphorus deficiency impairs dendritic-cell (already mapped) and amplifies IL-6 (already mapped) and NF-κB (already mapped) cascade of RSV."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "RSV chloride: chloride, via CFTR in airway epithelial and type-ii-pneumocyte (already mapped) cells, regulates mucociliary clearance; chloride channel dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of RSV bronchiolitis."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "RSV sulfur: hydrogen sulfide, from sulfur-amino acids in type-ii-pneumocytes (already mapped) and macrophages (already mapped), promotes bronchodilation; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) airway inflammatory cascade of RSV bronchiolitis."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "RSV nitrogen: nitric oxide from macrophages (already mapped) and type-ii-pneumocytes (already mapped) mediates antiviral vasodilation; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 inflammasome (already mapped) cascade of RSV."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "RSV carbon: carbon, as metabolic backbone of viral envelope lipids and type-ii-pneumocytes (already mapped), enables viral replication; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) cascade of RSV bronchiolitis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "RSV PD-1: PD-1 checkpoint on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates antiviral immune tolerance; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) airway inflammatory cascade of RSV."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "RSV GLP-1: GLP-1 signalling in type-ii-pneumocytes (already mapped) and endothelial cells (already mapped) modulates airway metabolic homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of RSV bronchiolitis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "RSV angiotensin-II: angiotensin-II signalling in type-II pneumocytes (already mapped) and endothelial cells (already mapped) promotes pulmonary vascular inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "RSV Wnt/β-catenin: Wnt/β-catenin signalling in type-II pneumocytes (already mapped) supports airway epithelial repair; Wnt dysregulation amplifies NF-κB (already mapped) and TGF-β/SMAD4 (already mapped) fibrotic cascade of RSV bronchiolitis."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "RSV RANKL: RANKL signalling in macrophages (already mapped) and airway stromal cells modulates bone-immune crosstalk; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of RSV."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "RSV fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds RSV-infected airway ECM; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "RSV notch: NOTCH on macrophages (already mapped) and airway epithelial cells (already mapped) regulates RSV immune response; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "RSV igf-1: IGF-1 from macrophages (already mapped) and fibroblasts (already mapped) modulates airway repair after RSV infection; igf-1 excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "RSV activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) regulates airway immune-fibrotic balance; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "RSV calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway calcium balance; calcitonin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "RSV insulin-receptor: insulin receptor on macrophages (already mapped) and fibroblasts (already mapped) drives airway metabolic tone; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) cascade of RSV."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "RSV tgf-beta: TGF-β from fibroblasts (already mapped) and macrophages (already mapped) drives RSV airway immune-fibrotic remodelling; tgf-beta excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "RSV aldosterone: aldosterone from macrophages (already mapped) and fibroblasts (already mapped) modulates airway ion balance; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "RSV androgen-receptor: androgen receptor on macrophages (already mapped) and fibroblasts (already mapped) modulates RSV steroid tone; androgen-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "RSV norepinephrine: norepinephrine from macrophages (already mapped) and fibroblasts (already mapped) modulates airway adrenergic tone; norepinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "RSV adrenomedullin: adrenomedullin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway vascular tone; adrenomedullin loss amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "RSV bdnf: BDNF from macrophages (already mapped) and fibroblasts (already mapped) supports airway neural trophic tone; bdnf loss amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "RSV fgfr: FGFR on macrophages (already mapped) and fibroblasts (already mapped) drives airway stromal growth; fgfr dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "RSV epinephrine: epinephrine from macrophages (already mapped) and fibroblasts (already mapped) modulates airway adrenergic tone; epinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "RSV renin: renin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway RAAS balance; renin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "RSV myostatin: myostatin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway muscle balance; myostatin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "RSV angiopoietin: angiopoietin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway vascular remodelling; angiopoietin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "RSV ghrelin: ghrelin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway metabolic tone; ghrelin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV."
---

# RSV

## Overview

**Respiratory syncytial virus (RSV)** is a non-segmented, negative-sense single-stranded RNA virus of the family *Pneumoviridae* (genus *Orthopneumovirus*), formerly classified within the family *Paramyxoviridae*. RSV is the **leading cause of acute lower respiratory tract illness (LRTI) in young children worldwide** — the 2017 Global Burden of Disease analysis estimated RSV causes ~33 million LRTI episodes in children <5 years annually, accounting for approximately 100,000 deaths, primarily in low- and middle-income countries [^shi-2017-rsv-global-burden]. RSV also causes significant severe disease in elderly adults (>60 years) and immunocompromised patients.

Two major subtypes exist — **RSV-A** and **RSV-B** — distinguished primarily by sequence variation in the attachment glycoprotein G. Both subtypes co-circulate, with RSV-A tending to dominate in epidemic years with higher hospitalization rates. Nearly all children are infected with RSV by age 2, and reinfections occur throughout life due to incomplete immunological memory, particularly against the highly variable G protein.

The RSV vaccine story is one of the most dramatic in vaccinology — from the tragic **formalin-inactivated RSV (FI-RSV) vaccine failure** of the 1960s (vaccine-enhanced disease, VED, with eosinophilic immunopathology on natural RSV exposure) to the **2023 vaccine revolution** when three separate RSV vaccines targeting prefusion F protein were approved within months: Abrysvo (Pfizer, adults + maternal), Arexvy (GSK, adults), and mResvia (Moderna, mRNA-1345, adults 60+). Simultaneously, nirsevimab (Beyfortus) — a single-dose long-acting anti-F monoclonal antibody — transformed infant RSV prophylaxis.

**Clinical spectrum:**
- **Infants/toddlers**: Upper respiratory symptoms → bronchiolitis (expiratory wheeze, hyperinflation, tachypnea, hypoxia, feeding difficulty); most common cause of infant hospitalization in high-income countries; ~100,000 US hospitalizations/year in infants <12 months
- **Older children**: Cold-like illness; RSV is the most common cause of childhood wheezing illness
- **Elderly adults (60+)**: Pneumonia, exacerbations of COPD/CHF; ~14,000 deaths/year in US adults ≥65 years
- **Immunocompromised**: Prolonged shedding, high mortality in HSCT recipients (>40% if RSV-pneumonia with respiratory failure); no standard approved therapy

**Risk factors for severe infant RSV:** Prematurity (<29 weeks GA), chronic lung disease of prematurity, congenital heart disease with hemodynamic compromise, severe combined immunodeficiency, neuromuscular disorders, Down syndrome, age <6 weeks

## Structure

### RSV genome and proteins

RSV has a ~15.2 kb negative-sense ssRNA genome encoding **11 proteins** in order: 3′-NS1-NS2-N-P-M-SH-G-F-M2(1 and 2)-L-5′

| Protein | Function |
|---------|----------|
| **NS1** | Non-structural; primary IFN antagonist: degrades TRIM25 (blocks RIG-I ubiquitination); inhibits IRF3 phosphorylation; targets STAT2; suppresses MAVS signaling |
| **NS2** | Non-structural; synergizes with NS1: blocks STAT2 nuclear translocation → ISG suppression; targets RIG-I for proteasomal degradation |
| **N (nucleoprotein)** | Encapsidates genomic RNA → nucleocapsid; essential for replication |
| **P (phosphoprotein)** | L polymerase cofactor; regulatory; scaffold for replication complex |
| **M (matrix protein)** | Virion assembly and budding from cell surface |
| **SH (small hydrophobic)** | Viroporin (ion channel); blocks TNF-α-mediated apoptosis; promotes viral release |
| **G (attachment glycoprotein)** | Attachment to CX3CR1 (fractalkine receptor) on airway epithelium; highly variable sequence (immune evasion); acts as CX3CL1 mimic → misdirects NK cells |
| **F (fusion protein)** | Viral-cell membrane fusion → viral entry; syncytium formation; prefusion F (site Ø) is the dominant neutralizing epitope; target of nirsevimab and all approved RSV vaccines |
| **M2-1** | Transcription processivity factor |
| **M2-2** | Regulates shift from transcription to replication |
| **L (large protein)** | RNA-dependent RNA polymerase (RdRp) + mRNA capping enzyme |

### RSV entry

1. G protein binds CX3CR1 on airway epithelial cells and ciliated cells; also binds heparan sulfate proteoglycans
2. F protein (prefusion conformation) binds nucleolin and IGFR1 (co-receptors)
3. Viral-host membrane fusion at the cell surface (pH-independent) → nucleocapsid enters cytoplasm
4. Transcription from 3′ end of genome → mRNA synthesis by L/P complex
5. Genomic replication in cytoplasmic inclusion bodies (IBs) — inclusion body factories
6. Assembly at cell membrane → budding

## Function

### Innate immune evasion — NS1/NS2 system

RSV has evolved a two-protein innate immune evasion system unique among pneumoviruses:

**NS1** (targeting RNA sensing):
- Degrades TRIM25 (E3 ubiquitin ligase) via proteasomal pathway → prevents K63-linked ubiquitination of RIG-I CARD (Lys172) → RIG-I cannot activate MAVS
- Directly binds IRF3 → prevents TBK1-mediated IRF3 Ser396 phosphorylation → blocks IFN-β transcription
- Interacts with STAT2 at nuclear pore → reduces STAT2 function

**NS2** (targeting IFN signaling):
- Binds STAT2 and blocks its nuclear translocation after IFN-α/β stimulation → ISG expression suppressed
- Targets RIG-I for proteasomal degradation (some strains)
- NS1+NS2 together reduce IFN-β production ~10-fold and IFN-α/β signaling ~5-fold

**Net effect**: RSV can replicate in immunocompetent airway epithelium despite RIG-I/MAVS and type I IFN being present — the dominant innate defense against RSV is **IFN-λ (type III)** at mucosal surfaces, which is less impaired by NS1/NS2 and represents the main protection in immunocompetent adults.

### Type 2 immunopathology — RSV and asthma

RSV causes not just acute bronchiolitis but also sensitizes the airway toward type 2 (allergic) inflammation:

1. **Airway epithelial damage** → IL-33 (from epithelial nuclei) and TSLP → "alarm signals"
2. **IL-33 → ST2+ ILC2** → IL-4, IL-5, IL-13 → eosinophilia, mucus, airway hyperresponsiveness (AHR)
3. **TSLP → TSLP receptor on ILC2/basophils** → Th2 polarization, IgE class switching
4. **Th2 sensitization**: Neonatal RSV exposure during a critical window may bias immunity toward Th2 → risk of subsequent asthma (epidemiological association: RSV bronchiolitis in infancy is the strongest environmental risk factor for childhood asthma)
5. **G protein CX3CL1 mimicry** → attracts CX3CR1+ NK cells and T cells → misdirects innate response → promotes type 2 bias

**FI-RSV VED mechanism (historical lesson)**: Formalin destroyed prefusion F → only post-fusion F antibodies made (poor neutralization) → also primed Th2-biased immune response → on natural RSV exposure, Th2-mediated eosinophilic immunopathology occurred; no cytotoxic T cell response → enhanced disease. This explains why prefusion F stabilization is essential for safe RSV vaccines.

### Adaptive immunity and RSV-specific T cells

- Primary RSV infection in infants generates RSV-specific CD8+ T cells (CTLs) that clear infection
- However, RSV suppresses T cell responses: NS1/NS2 reduce DC function and IL-12 production
- RSV-specific memory T cells in adults are short-lived and wane rapidly → susceptibility to reinfection
- CD8+ T cells against conserved F protein epitopes provide better cross-subtype protection than anti-G responses
- In immunocompromised hosts: RSV-specific T cells critical; absence → prolonged shedding, high mortality

## Pathology

### Bronchiolitis pathophysiology

In infants, RSV bronchiolitis follows a characteristic pattern:
1. Infection of ciliated airway epithelium → loss of ciliary function → mucus pooling → peribronchiolar lymphocytic infiltrate
2. Syncytium formation (F protein-mediated) → large multinucleated cells → epithelial sloughing → airway debris
3. Submucosal edema + mucus plugs → small airway obstruction → air trapping → hyperinflation
4. Ventilation-perfusion mismatch → hypoxemia → respiratory distress

Radiological findings: Hyperinflation, peribronchial thickening, occasional atelectasis (right upper lobe common)

### Diagnosis

- **Clinical** (in infants <2 years during RSV season): No testing needed; classic presentation
- **Rapid antigen test (RAT)**: Point-of-care; ~80% sensitivity; useful in hospital triage
- **RSV PCR (multiplex respiratory panel)**: Gold standard; >95% sensitivity; preferred for immunocompromised and adults
- **RSV culture**: Research use; not clinical standard

### Treatment

**No approved antiviral therapy for standard RSV:**
- **Supportive care**: Primary treatment for bronchiolitis; oxygen, high-flow nasal cannula (HFNC) for hypoxia; minimal suctioning; feeding support (NG tube if needed)
- **Ribavirin** (aerosolized): FDA-approved for severe RSV in immunocompromised; evidence weak; used selectively (HSCT, lung transplant with respiratory failure)
- **IVIG/palivizumab IV**: Not recommended therapeutically
- **Bronchodilators (albuterol, epinephrine)**: Not recommended in bronchiolitis (no consistent benefit; 2014 AAP guidelines)
- **Corticosteroids**: Not recommended in bronchiolitis (multiple RCTs negative)
- **HFNC vs. standard O2**: HFNC preferred for moderate-severe bronchiolitis with hypoxia; reduces escalation to PICU

### Prevention — the 2023 paradigm shift

#### Nirsevimab (Beyfortus; AstraZeneca/Sanofi)

- **Class**: Long-acting monoclonal antibody targeting prefusion RSV F protein at site Ø
- **Half-life extended**: YTE (M252Y/S254T/T256E) Fc mutations → ~70-day half-life vs. ~20 days for palivizumab → single dose provides 5-month protection (one RSV season)
- **MELODY trial (healthy infants)**: 74.5% efficacy against medically attended RSV LRTI
- **NIRSEVIMAB-MEDICALLY ATTENDED trial (high-risk infants)**: 70.1% efficacy; **77% against RSV hospitalization**
- **FDA approval**: 2023; universal recommendation for all infants <8 months entering first RSV season (2023 ACIP guidance)
- **Replaces palivizumab**: Palivizumab (site II mAb; monthly injections) was limited to high-risk infants and required 5 monthly doses; nirsevimab covers all infants with one dose

#### RSV vaccines approved in 2023

| Vaccine | Platform | Approval | Population | Efficacy (LRTI) |
|---------|---------|----------|-----------|-----------------|
| **Abrysvo (Pfizer RSVpreF)** | Bivalent protein subunit (RSV-A + RSV-B preF) | May 2023 | Adults 60+; maternal (Aug 2023) | 88.9% vs. severe LRTI (adults); 82% vs. infant (maternal 0-90 days) |
| **Arexvy (GSK RSVPreF3-AS01E)** | Protein subunit + AS01E adjuvant | May 2023 | Adults 60+ | 82.6% vs. RSV-LRTD |
| **mResvia (mRNA-1345, Moderna)** | mRNA encoding prefusion-stabilized F | May 2024 | Adults 60+ | 83.7% vs. RSV-LRTD (RENOIR trial) |

**Key scientific principle**: All approved vaccines encode/contain **prefusion-stabilized F protein** with engineered proline substitutions (DS-Cav1 mutations or equivalent) that lock F in the prefusion conformation → expose site Ø → much higher neutralizing antibody titers vs. post-fusion F (the basis of the 1960s FI-RSV failure).

**Maternal immunization (Abrysvo)**: Pregnant persons at 32-36 weeks gestation → maternal IgG transfers to fetus → infant protected in first months of life; MATISSE trial showed 82% efficacy in infants 0-90 days; concern about potential RSV-specific immune interference with subsequent immunizations (under monitoring).

## Connections

**→ [RSV F Protein](../../../03-molecular/rsv-f-protein/)**: RSV F protein mediates attachment to nucleolin and heparan sulfate and viral-host membrane fusion → syncytium formation; prefusion F (site Ø) is the dominant neutralizing epitope; nirsevimab (site Ø mAb), Abrysvo (Pfizer bivalent preF), Arexvy (GSK preF3 + AS01E), and mResvia (Moderna mRNA-1345) all target prefusion F for RSV prevention.

**→ [MAVS](../../../03-molecular/mavs/)**: RSV NS1 protein degrades TRIM25 → prevents RIG-I K63-ubiquitination → impairs RIG-I/MAVS signaling → reduced IFN-β production; RSV NS2 blocks STAT2 nuclear translocation → ISGs suppressed; NS1+NS2 together reduce MAVS-driven IFN-β ~10-fold; IFN-λ (type III) at mucosal surfaces is the dominant innate mucosal defense against RSV that NS1/NS2 cannot fully block.

**→ [IL-33](../../../03-molecular/il-33/)**: RSV airway epithelial infection and syncytium-mediated mechanical damage release IL-33 from epithelial nuclei (danger signal/DAMP) → ST2+ ILC2 activation → IL-4/IL-5/IL-13 → type 2 inflammation, eosinophilia, mucus hypersecretion, and airway hyperresponsiveness; RSV-IL-33-ILC2 axis is a key mechanism linking RSV bronchiolitis to subsequent childhood asthma.

**→ [TSLP](../../../03-molecular/tslp/)**: RSV-induced airway epithelial damage and dsRNA replication intermediates trigger TSLP release from airway epithelium → TSLP receptor on ILC2 and basophils → IL-4/IL-13 → Th2 polarization and IgE class switching; neonatal RSV-driven TSLP sensitization during a critical early developmental window may explain the epidemiological RSV-asthma link; tezepelumab (anti-TSLP) is being investigated in RSV-triggered wheeze.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: RSV NS1/NS2 cooperatively suppress type I IFN at multiple levels: NS1 targets TRIM25 and IRF3, preventing IFN-β transcription; NS2 blocks STAT2 nuclear translocation, preventing ISG induction; premature infants with immature IFN signaling systems have more severe RSV bronchiolitis; IFN-λ (type III IFN at mucosal surfaces) is less susceptible to NS1/NS2 and represents the dominant innate mucosal defense.

- `connects-to` → **[Respiratory Syncytial Virus](../../../02-pathogen/01-viruses/respiratory-syncytial-virus/README.md)** — Respiratory syncytial virus, a negative-sense RNA pneumovirus, fuses airway cells into syncytia and blunts interferon with NS1/NS2; it reinfects throughout life because the G protein varies and memory is short, yet prefusion-F antibodies and vaccines now prevent severe disease.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — RSV is the top cause of infant bronchiolitis and a major cause of pneumonia in the elderly and immunocompromised: it infects ciliated airway epithelium, sloughing cells and plugging small airways with mucus → air trapping, hypoxia, and wheeze; care is supportive.
- `connects-to` → **[Asthma](../asthma/README.md)** — Severe RSV bronchiolitis in infancy is the strongest environmental risk factor for childhood asthma: epithelial damage releases IL-33 and TSLP that activate ILC2s toward type-2 inflammation, biasing the developing airway toward allergic sensitization and recurrent wheeze.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — RSV and COVID-19 are enveloped respiratory RNA viruses that with influenza drive seasonal lower-respiratory disease; both cause bronchiolitis/pneumonia at the extremes of age, both evade interferon, and both are now vaccine-preventable in older adults.
- `connects-to` → **[COPD](../copd/README.md)** — RSV is a major trigger of COPD exacerbations: it infects airway epithelium → neutrophilic inflammation and bronchospasm → acute decompensation, and is found in a substantial share of hospitalized exacerbations; older-adult RSV vaccines (Arexvy, Abrysvo) reduce this burden.
- `connects-to` → **[Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — RSV infects airway epithelium and alveolar pneumocytes including type II cells: replication plus NS1/NS2 interferon evasion drives epithelial necrosis, sloughing and syncytia that plug bronchioles → the airway obstruction of infant bronchiolitis and impaired surfactant.
- `connects-to` → **[Influenza](../influenza/README.md)** — RSV and influenza are the two dominant seasonal respiratory viruses, co-circulating each winter: both cause fever, cough, and pneumonia at the extremes of age, both now have older-adult vaccines, and PCR tells them apart—but RSV adds nirsevimab prophylaxis for infants.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — RSV is the leading cause of lower respiratory infection in infants: it targets bronchiolar epithelium, causing the airway plugging and wheeze of bronchiolitis, the top cause of infant hospitalization—so the respiratory system's smallest airways bear the brunt.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — RSV skews the infant immune response toward Th2: instead of protective Th1 immunity it elicits Th2 cytokines (IL-4, IL-13) and eosinophils, which worsen disease and may link severe RSV bronchiolitis to later asthma—why early RSV is more than a transient infection.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages are central to RSV defense and disease: alveolar macrophages sense the virus and make interferon, but RSV also infects and subverts them, and excessive macrophage-driven inflammation contributes to the airway damage of severe bronchiolitis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — RSV is an underrecognized trigger of heart failure decompensation: RSV respiratory infection strains the cardiovascular system, precipitating acute heart-failure exacerbations and excess cardiac deaths—why RSV vaccination is now recommended for older adults.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — Severe RSV can progress to ARDS: intense bronchiolitis and alveolar inflammation flood the lungs and collapse gas exchange, requiring ventilation—the most severe end of the RSV spectrum, where a common childhood virus becomes life-threatening.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — RSV bronchiolitis plugs the airways with neutrophils and debris: the virus and the neutrophil-rich inflammatory response slough airway cells and mucus into the tiny bronchioles, obstructing them—why infants wheeze and the smallest airways collapse in severe RSV.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — RSV is prevented with passive antibody, not a vaccine, in infants: monoclonal IgG antibodies (palivizumab, nirsevimab) against the F protein give infants immediate protection—a rare reliance on borrowed antibody for a virus where natural immunity is weak.
- `connects-to` → **[Immune System](../immune-system/README.md)** — RSV evades durable immunity and reinfects for life: it blunts interferon and induces only short-lived, incomplete immune memory, so people are reinfected repeatedly—and the immature or aged immune system makes RSV dangerous at both ends of life.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — RSV prevention now rests on antibodies, not active immunity: the monoclonal nirsevimab and the maternal RSVpreF vaccine both supply or elicit B-cell antibodies against the F protein, protecting infants through passive immunity during their first vulnerable season.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — The placenta is key to protecting newborns from RSV: vaccinating mothers in late pregnancy lets anti-RSV antibodies cross the placenta, so the baby is born already armed against severe bronchiolitis in its first months—passive immunity by maternal transfer.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — RSV makes airway smooth muscle the villain of wheeze: infection and inflammation make bronchiolar smooth muscle constrict and the airways narrow, causing the wheezing of bronchiolitis—and repeated early RSV is linked to later asthma and airway reactivity.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells both clear and harm in RSV: CD8 T cells eliminate infected airway cells to end infection, but their response also drives lung immunopathology—a balance central to why severe bronchiolitis injures infant airways.
- `connects-to` → **[Pulmonary Surfactant](../../03-molecular/surfactant/README.md)** — RSV cripples the airway's surfactant defense: it infects and sloughs the epithelial and type-II cells that make pulmonary surfactant, so airways collapse and plug with debris—the bronchiolitis that obstructs an infant's tiny airways.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — RSV bronchiolitis drives Th2 IL-13 and later wheeze: the infection skews immunity toward IL-13, boosting mucus and airway reactivity, which is part of why severe infant RSV is linked to later asthma.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — RSV bronchiolitis is dangerous because it starves infants of oxygen: inflamed, mucus-plugged small airways trap air and drop blood oxygen, so supplemental oxygen and breathing support—not antivirals—are the mainstay of treating a severe case.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — NK cells are an early shield against RSV: they kill infected airway cells before antibodies form, and weak NK responses in young infants and the elderly help explain why those age groups suffer the worst disease.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — RSV outwits dendritic cells: the virus blunts these antigen-presenters' ability to prime strong, lasting T-cell immunity, which helps explain why RSV reinfects people throughout life and why a durable vaccine took decades to achieve.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — RSV can hit the infant brain: in the youngest babies it triggers sudden apnea—pauses in breathing that may be the first sign—and rare cases cause seizures or encephalopathy, so very young infants are watched closely.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Severe RSV throws off sodium: bronchiolitis is a classic trigger of SIADH, in which the body retains water and dilutes blood sodium, so hyponatremia can develop and provoke seizures if IV fluids are not chosen carefully.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — RSV stirs the airway's mast cells: their release of mediators adds to the wheeze of bronchiolitis, and severe early RSV is linked to later asthma, hinting these cells help bridge infection to allergic airway disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — RSV bronchiolitis shows on chest X-ray as hyperinflation and patchy atelectasis in X-ray photons, used when a baby's breathing worsens—though imaging is not needed for the routine diagnosis.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Severe RSV reaches the alveoli: beyond plugging the small bronchioles, it inflames the alveolar units into pneumonia, flooding gas exchange and causing the worst of the hypoxia.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — A tiring RSV baby retains carbon dioxide: rising CO2 and the falling pH of respiratory acidosis signal that breathing is failing and that ventilatory support may be needed.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows how RSV earns its name: the enveloped, filamentous virions fuse infected airway cells into multinucleated giant cells — the syncytia — that slough off and plug the tiny airways in bronchiolitis.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — RSV can strain the heart at the extremes of life: in fragile infants and older adults it precipitates heart failure and, rarely, myocarditis, the cardiorespiratory stress of severe infection tipping a marginal heart over the edge.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Severe bronchiolitis unsettles the kidney's salt balance: sick RSV infants often develop SIADH with hyponatremia, while poor feeding and fever bring dehydration that can stress the kidneys.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — RSV is fought largely with antibody: the monoclonals palivizumab and the longer-acting nirsevimab passively protect high-risk infants, and a maternal vaccine now passes protective antibody across the placenta to the newborn.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — In the youngest infants RSV can stop the breath: it triggers central apnea — pauses in breathing driven by immature brainstem respiratory neurons — sometimes the first sign of infection before the wheeze appears.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Bronchiolitis makes feeding a struggle: a baby working hard to breathe cannot coordinate sucking and swallowing, so poor intake and vomiting bring dehydration and the need for nasogastric or IV fluids.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Protection now starts before birth: a maternal RSV vaccine given in pregnancy passes antibody across the placenta to shield the newborn through its risky first months, complementing the nirsevimab antibody given to infants directly.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D may temper the infection: low vitamin D in infancy is associated with more severe RSV bronchiolitis, the vitamin's role in airway immunity and barrier function making its status a studied modifier of risk.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — A key lesson is what cortisol cannot do: unlike asthma, RSV bronchiolitis does not respond to corticosteroids, because its airway plugging is driven by sloughed cells and mucus rather than the steroid-sensitive inflammation of allergic disease.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — RSV opens the door to bacteria: by stripping the airway lining and blunting defenses it primes the lung for secondary pneumococcal pneumonia, a viral-bacterial synergy that drives much of the severe illness and death in infants and the elderly.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells decide how much the infection hurts: they rein in the antiviral response so it clears RSV without shredding the airway, and too few of them tip the balance toward immunopathology and a Th2-skewed, wheezy course.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — RSV lights up IL-6 in the airway: infected epithelium and macrophages pour out this cytokine, and high IL-6 in nasal secretions tracks with the inflammation and severity of infant bronchiolitis.
- `connects-to` → **[IRF3](../../03-molecular/irf3/README.md)** — Sensing the virus flips the interferon switch: RSV RNA detected through the RIG-I/MAVS pathway activates IRF3, the transcription factor that turns on type I interferon — and which the virus's NS proteins work to suppress.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — The damaged airway invites a second germ: RSV strips the respiratory epithelium and blunts defenses, opening the door to bacterial superinfection by Staphylococcus aureus and other organisms that worsen the pneumonia.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Early infection may reshape the lung for life: RSV bronchiolitis activates airway fibroblasts and remodeling, part of why severe infant infection is linked to later wheezing and asthma.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The virus throws the airway's inflammation switch: RSV activates NF-κB in respiratory epithelium, driving the chemokine and cytokine release that recruits the neutrophils and mucus plugging behind bronchiolitis.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Severe infant disease can spiral to sepsis: RSV bronchiolitis can progress to respiratory failure, and bacterial superinfection of the damaged lung can seed bloodstream infection and a sepsis-like critical illness.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can reach beyond the lungs to the brain: severe RSV in young infants is associated with central apnea, seizures and rare encephalopathy, CNS complications that can dominate the acute illness.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — A virus can clear the way for group A strep: RSV injury to the airway epithelium can be followed by invasive Streptococcus pyogenes, causing necrotizing pneumonia, empyema and toxic shock that turn a viral illness fulminant.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — In the immunocompromised it opens a fungal door: severe RSV in transplant and leukemia patients damages the lung and prompts steroids, setting the stage for secondary invasive pulmonary aspergillosis.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Fragile hearts tolerate it worst: infants with congenital heart disease and pulmonary hypertension suffer the most severe RSV, as the bronchiolitis raises pulmonary pressures and strains an already burdened right heart.
- `connects-to` → **[Acute Myeloid Leukemia](../aml/README.md)** — It turns deadly in the neutropenic host: in leukemia patients like those with AML, RSV readily progresses from the upper airway to fatal pneumonia, a major respiratory-virus threat during chemotherapy-induced immunosuppression.
- `connects-to` → **[Graft-versus-Host Disease](../gvhd/README.md)** — Post-transplant lungs are defenseless against it: hematopoietic stem-cell recipients, especially with graft-versus-host disease on immunosuppression, suffer severe RSV pneumonia, a leading cause of post-transplant respiratory failure.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Damaged, immunosuppressed lungs fare badly: patients with lung cancer such as NSCLC, with their structural lung disease and treatment-related immunosuppression, are prone to severe RSV lower-respiratory infection.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Like influenza, it strains the heart: RSV infection in older adults triggers acute cardiovascular events and decompensation, precipitating arrhythmias, heart failure and myocardial infarction.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Bronchiolitis stops infants feeding: the tachypnoea and nasal congestion of RSV make young babies unable to feed, causing poor intake and dehydration that often drives the need for hospital admission.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Severe disease threatens the kidneys: dehydration from poor feeding and the hypoxia and sepsis of severe RSV can cause acute kidney injury, especially in infants and frail older adults.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can drop the blood sodium: severe RSV bronchiolitis is a recognised cause of SIADH with hyponatraemia in infants, requiring careful fluid management during hospital care.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It can inflame the muscles: like other respiratory viruses, RSV causes myalgia, and in children benign acute viral myositis with calf pain and raised creatine kinase can follow infection.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Distress shows on the skin: in severe infant bronchiolitis RSV causes perioral and peripheral cyanosis with mottled, poorly-perfused skin, visible warning signs of respiratory failure.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It rouses the airway's lymphoid tissue: RSV bronchiolitis provokes a brisk peribronchial lymphocytic infiltrate and reactive lymphadenopathy as the immune system responds.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — It opens the door to pneumococcus: RSV damages the airway epithelium and predisposes to secondary bacterial pneumonia, classically from Streptococcus pneumoniae.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Severe disease invites staph superinfection: severe RSV bronchiolitis can be complicated by secondary staphylococcal pneumonia, especially in young infants.
- `connects-to` → **[Influenza A](../../../02-pathogen/01-viruses/influenza-a/README.md)** — A fellow winter respiratory virus: influenza A co-circulates with RSV, causes overlapping bronchiolitis and pneumonia, and the two can co-infect, though influenza has antivirals and annual vaccines that RSV long lacked.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids do not help routine cases: trials show systemic corticosteroids do not shorten RSV bronchiolitis in healthy infants and are not recommended, though they treat associated viral wheeze and croup.
- `connects-to` → **[Zinc (Dietary)](../../../03-medicine/03-food/zinc-dietary/README.md)** — Nutrition shapes defence: zinc supports mucosal immunity and is studied to reduce the severity of childhood respiratory infections including RSV bronchiolitis in deficient populations.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Monoclonal antibodies prevent it: palivizumab and the long-acting nirsevimab are anti-RSV-F monoclonal antibodies given to infants for passive immunoprophylaxis, blocking the fusion protein the virus uses to enter cells.
- `connects-to` → **[Lung Slice](../../05-tissue/lung-slice/README.md)** — It plugs the small airways: RSV bronchiolitis sloughs necrotic airway epithelium that, with mucus and inflammatory debris, obstructs the bronchioles, causing the air-trapping and wheeze of severe infection.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — A high-risk chronic airway disease: children with cystic fibrosis suffer more severe and prolonged RSV infections that accelerate their airway damage, making RSV prevention important in this group.
- `connects-to` → **[Measles](../measles/README.md)** — A fellow paramyxovirus: respiratory syncytial virus and measles are related enveloped RNA viruses, but RSV (a pneumovirus) causes bronchiolitis in infants while measles causes a systemic rash and immune amnesia—contrasting outcomes of related viruses.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It can strain and inflame the heart: severe RSV causes myocarditis in infants and triggers acute cardiac events such as ischaemia and heart failure in older adults, so cardiac involvement adds to its respiratory toll.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Where protective antibody is made: neutralizing antibody to the RSV prefusion-F protein is generated in germinal centres, the response boosted by the maternal RSV vaccine—while nirsevimab supplies it passively.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Early infection and the atopic march: severe infant RSV bronchiolitis is linked to later recurrent wheeze and asthma within the broader atopic march that begins with atopic dermatitis.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Inflammation injures the lung: severe RSV bronchiolitis and pneumonia drive an exaggerated cytokine response that, like other cytokine storms, damages airways and alveoli beyond direct viral cytopathic effect.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Neurological complications: severe RSV in infants can cause apnoea, seizures and encephalopathy, occasionally leaving lasting neurological sequelae beyond the airway disease itself.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Microbiome shapes the response: the early-life airway and gut microbiome modulate the severity of RSV bronchiolitis and the subsequent risk of asthma, with dysbiosis tilting the immune response toward worse disease.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Acute chest syndrome trigger: RSV and other respiratory viruses precipitate acute chest syndrome in sickle cell disease, a leading cause of death, so viral lower-respiratory infection is especially dangerous in SCD.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Post-viral airway scarring: severe RSV bronchiolitis can lead to bronchiolitis obliterans, where fibrosis narrows and obliterates the small airways long after the infection clears.
- `connects-to` → **[RIG-I](../../03-molecular/rig-i/README.md)** — Viral RNA sensing: the RIG-I receptor detects RSV genomic RNA and signals through MAVS to launch the type-I interferon response that constrains the infection.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 skewing: RSV bronchiolitis biases the infant immune response toward IL-4-driven Th2 inflammation, a pathway linked to the later development of wheeze and asthma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil recruitment: IL-5 mobilised during the Th2 response to RSV draws eosinophils into the airways, contributing to mucus and the post-bronchiolitis wheezing phenotype.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: RSV viroporin SH and other viral proteins trigger the NLRP3 inflammasome in airway cells, releasing IL-1β that amplifies the inflammation of severe bronchiolitis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Neutrophilic airways: IL-17A drives the neutrophil-dominated airway inflammation and mucus hypersecretion that mark severe RSV bronchiolitis, distinct from the eosinophilic Th2 arm.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Inflammatory recruitment: CCL2 produced by infected airway epithelium draws monocytes and macrophages into the lung, fuelling the immunopathology that obstructs the small airways in RSV bronchiolitis.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — The RSV fusion (F) protein engages TLR4 on airway and immune cells, triggering the NF-κB-driven cytokine response that contributes to the innate inflammation of infection—linking the vaccine-target protein to disease pathogenesis.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — IFN-γ from Th1 cells counterbalances the Th2 skew that predisposes infants to severe RSV bronchiolitis, and a weak Th1 response is associated with worse acute disease and the later development of recurrent wheezing.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated CD8 T-cell killing of infected airway epithelium clears RSV but also contributes to the lung injury—the double-edged cytotoxic response central to both viral recovery and the immunopathology of severe bronchiolitis.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — The anti-F-protein antibody nirsevimab carries an FcRn-binding (YTE) modification that extends its half-life to protect infants across a whole RSV season with one dose, the passive-immunization strategy that has transformed prevention.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Secretory IgA on the airway surface neutralizes RSV at the portal of entry, the first-line mucosal antibody whose relative immaturity in infancy is one reason the very young suffer the most severe bronchiolitis.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — RSV upregulates substance P and its NK1 receptor in the airways, driving neurogenic inflammation, mucus secretion and the airway hyper-reactivity that contributes to the wheeze of bronchiolitis and post-RSV wheezing.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — RSV bronchiolitis in infancy promotes Th2 sensitization and IgE production (with the IL-4/IL-5/IL-13 already mapped), the mechanism linking severe early RSV to later recurrent wheeze and asthma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — RSV activates the NLRP3 inflammasome (already mapped) to release IL-1β, amplifying the airway inflammation and neutrophil recruitment of severe bronchiolitis.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — RSV induces caspase-3 apoptosis of infected airway epithelial cells, and the resulting epithelial sloughing—with mucus and the syncytia that name the virus—plugs the small airways in bronchiolitis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4 sensing of RSV F protein (RSV-F and TLR4 mapped) signals through MyD88 to NF-κB (mapped), driving the airway inflammatory response of RSV bronchiolitis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — Type-I interferon signals through STAT1 to mount the antiviral response, which the RSV NS1 and NS2 proteins antagonize—blunting interferon and enabling viral replication.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10 modulates the Th2-skewed immunopathology (IL-4, IL-5 and IL-13 mapped) of severe RSV bronchiolitis, balancing viral control against airway damage.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Type-I-interferon and cytokine signaling through JAK-STAT (STAT1 mapped) governs the antiviral and Th2-skewed immune response to RSV bronchiolitis.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Airway hypoxia during severe RSV bronchiolitis stabilizes HIF-1α, shaping the inflammatory and epithelial response to infection.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — RSV activates PI3K-AKT signaling to promote epithelial-cell survival and support viral replication, a host pathway exploited during infection.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the airway inflammation and mucus-associated immunopathology of RSV bronchiolitis in infants.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response that contributes to the airway pathology of severe RSV infection.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the airway remodeling and the link between severe infant RSV bronchiolitis and later wheezing and asthma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates airway epithelial oxidative-stress and survival responses to RSV infection.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by recruited neutrophils amplify the airway inflammation and mucus obstruction of severe RSV bronchiolitis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling activated by RSV in airway epithelium promotes mucin production and the inflammatory response of RSV bronchiolitis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven airway inflammation and the innate immune response to respiratory syncytial virus.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling regulates the immune-cell metabolism and memory-response programming to respiratory syncytial virus.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) is exploited by respiratory syncytial virus to support its replication and modulate airway epithelial survival.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Respiratory syncytial virus modulates host autophagy, which shapes the innate immune and inflammatory response to infection.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the airway epithelial and immune-cell responses to respiratory syncytial virus.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling modulates the airway epithelial and immune-cell responses to respiratory syncytial virus.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the airways contributes to the bronchiolitis and immunopathology of RSV infection.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the immune response to respiratory syncytial virus.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the airway leukocyte trafficking of RSV infection.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the innate antiviral and inflammatory responses to respiratory syncytial virus.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the host response to respiratory syncytial virus.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation and airway immune response to respiratory syncytial virus.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Vaccine immunity: MHC class II-restricted CD4 T-cell help drives the antibody responses to the RSV F protein (already mapped) targeted by maternal and older-adult vaccines, and a Th2-skewed version of this help historically caused vaccine-enhanced disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Airway smooth muscle: RSV infection provokes bronchospasm and the recurrent wheeze that can follow bronchiolitis through calcium-dependent airway smooth muscle contraction and heightened airway responsiveness.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell response: IL-2 drives the expansion of the RSV-specific effector and memory T cells that clear infected airway epithelium, and the balance of this response shapes both protection and the immunopathology of severe bronchiolitis.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Wheeze and Th2: histamine release accompanies the type-2, allergic-like response to RSV (IL-4/IL-13 already mapped), contributing to the airway oedema and wheeze of bronchiolitis and to the post-viral airway reactivity.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Airway nitric oxide: RSV alters epithelial nitric-oxide production, and NO both participates in antiviral defence and, in excess, contributes to the airway inflammation and vascular changes of severe bronchiolitis.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory mediators: prostaglandins and other lipid mediators generated during RSV infection promote the airway inflammation, mucus secretion and bronchoconstriction that obstruct the small airways in bronchiolitis.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative airway injury: RSV infection generates reactive oxygen species, to which xanthine oxidase contributes, in the airway epithelium, and this oxidative stress amplifies the inflammation and epithelial damage of bronchiolitis.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Neurogenic inflammation: CGRP released from airway sensory nerves, with substance P (already mapped), contributes to the neurogenic inflammation and the exaggerated airway responses of RSV bronchiolitis, part of its neuro-immune dimension.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-mediated inflammation: bradykinin generated in the RSV-infected airway raises vascular permeability and stimulates the mucus secretion and bronchoconstriction that obstruct the small airways of bronchiolitis.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxaemia of bronchiolitis: the small-airway obstruction and mucus plugging of RSV bronchiolitis impair gas exchange, causing the hypoxaemia that drives the supplemental oxygen and high-flow support that are the main reason for hospital admission.
- `connects-to` → **[COPD](../copd/README.md)** — Exacerbations and adult burden: RSV causes exacerbations of COPD and severe respiratory illness in older adults, the burden that the new RSVpreF vaccines targeting the F protein (already mapped) aim to prevent.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Th2-skewing dendritic cells: the airway dendritic cells present RSV antigen and shape the type-2-skewed (IL-4, IL-5 and IL-13 already mapped) immune response that contributes to the wheeze and the immunopathology of infection.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and antiviral immunity: zinc is an antiviral and immune-modulating trace metal, and its deficiency, common in undernourished infants, worsens the severity of the respiratory viral infections including RSV.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Airway oedema: VEGF drives the vascular permeability and airway oedema that, with the epithelial debris (surfactant already mapped), plug the small bronchioles in RSV bronchiolitis.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Bronchiolitic hypoxaemia: the small-airway plugging and ventilation-perfusion mismatch of RSV bronchiolitis cause the hypoxaemia whose correction with supplemental oxygen is the mainstay of the supportive care of infants.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Nutritional-immune adipokine: leptin is the adipokine of the immune-metabolic milieu; the infant nutritional status (leptin) modulates the immune response to RSV.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of the RSV infection.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the inflammatory (IL-6 already mapped) milieu of RSV bronchiolitis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 antiviral arm: IL-12 polarises the protective Th1 (IFN-γ already mapped) antiviral response that counter-balances the pathogenic Th2 (IL-4, IL-5 and IL-13 already mapped) skewing of RSV bronchiolitis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Th2 airway remodelling: periostin, downstream of the type-2 cytokines (IL-13 already mapped) and the alarmins (IL-33 and TSLP already mapped), marks the Th2 airway remodelling linking severe RSV bronchiolitis to the later asthma (already mapped).
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement immunopathology: the complement C5 activation contributes to the RSV bronchiolitis immunopathology (and the historical enhanced disease of the formalin-inactivated vaccine).
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neutrophilic (already mapped) inflammation of severe RSV bronchiolitis.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Antibody arm: the plasma cells secrete the anti-F-protein antibodies (already mapped); the passive antibody (palivizumab/nirsevimab, maternal RSVpreF) targets the same F protein (already mapped) to protect infants from RSV.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Type-2 airway itch: IL-31, a type-2 (IL-4, IL-5 and IL-13 already mapped) cytokine, is part of the type-2 response linking the severe RSV bronchiolitis to the later atopy and asthma (already mapped).
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the complement-driven airway inflammation of severe RSV bronchiolitis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: RSV recruits the host factor H (via its G glycoprotein) to inactivate the C3 convertase (complement C3, C5 and C5aR1 already mapped) and evade the complement attack.
- `connects-to` → **[Prurigo nodularis](../prurigo-nodularis/README.md)** — Atopic-march type-2: RSV bronchiolitis shares the type-2 (IL-4, IL-5, IL-13, TSLP and IL-31 already mapped) immunity of the atopic march with prurigo nodularis, another type-2 disease of the shared-biologic era.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways (C3, C5, C5aR1 and factor H already mapped) engaged against RSV, a pathway the virus partially evades.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Airway matricellular: osteopontin, produced in the RSV-infected airway, is a matricellular cytokine amplifying the type-2 and myeloid inflammation of RSV bronchiolitis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Acute-phase iron: transferrin, the iron carrier, reflects the hypoferraemia and disordered iron handling of the acute-phase response to the RSV lower-respiratory-tract infection.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoiesis support: erythropoietin counteracts the anaemia driven by the cytokine storm (IL-6 already mapped) and NLRP3 inflammasome (already mapped) activation of severe RSV disease, supporting erythropoiesis during lower-respiratory-tract infection.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Antiviral immunomodulator: melatonin, acting via MT1/MT2 receptors on macrophages (already mapped) and NK cells (already mapped), inhibits NLRP3 inflammasome (already mapped) activation and attenuates the cytokine storm of severe RSV infection.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune stimulator: prolactin, via its receptor on NK cells (already mapped), macrophages (already mapped), and T cells (already mapped), promotes antiviral effector responses and modulates the Th1/Th2 balance of RSV immunity.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Neuroimmune antiviral modulator: oxytocin, via oxytocin receptors on macrophages (already mapped) and T cells (already mapped), suppresses the pro-inflammatory cytokine (IL-6 and TNF-α already mapped) storm and the airway hyperreactivity of severe RSV infection.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-mediated sex-differential severity: testosterone, acting via androgen receptors on innate immune cells, suppresses the pro-inflammatory cytokine (IL-6 and TNF-α already mapped) responses and underlies the greater severity of RSV disease in males vs. females.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant antiviral micronutrient: selenium, incorporated into selenoproteins (GPx and thioredoxin reductase), suppresses the ROS-driven oxidative stress and the NF-κB-mediated (already mapped) inflammatory cytokine burst in the airway epithelium during RSV infection.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — RSV serotonin: mast-cell (already mapped) serotonin amplifies the IgE (already mapped) and IL-33 (already mapped) airway hyperresponsiveness of RSV; 5-HT2 on smooth-muscle cells (already mapped) promotes bronchospasm and T-helper-cell (already mapped) Th2 skew.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — RSV vasopressin: vasopressin, released during severe RSV-induced respiratory distress, promotes SIADH and the sodium (already mapped) hyponatraemia of RSV in infants; vasopressin also modulates the lung (already mapped) vascular tone and brain (already mapped) oedema of RSV.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — RSV magnesium: magnesium acts as a bronchodilator by inhibiting calcium-mediated smooth-muscle cell (already mapped) constriction; magnesium deficiency amplifies the IL-33 (already mapped) and type-I IFN (already mapped) inflammatory airway response to RSV.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — RSV iodine: iodine-dependent thyroid hormones upregulate type-I IFN (already mapped) antiviral signalling on airway epithelium; hypothyroidism impairs the NF-κB (already mapped) response and amplifies the IL-6 (already mapped) and IL-33 (already mapped) cytokine storm of RSV.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — RSV copper: copper, as SOD and ceruloplasmin cofactor, suppresses the ROS amplifying NF-κB (already mapped) and NLRP3 inflammasome (already mapped) airway cytokine burst of RSV; copper deficiency impairs macrophage (already mapped) bactericidal and antiviral function.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — RSV potassium: potassium efflux is the canonical activating signal for NLRP3 inflammasome (already mapped) in macrophages (already mapped); disrupted K⁺ homeostasis amplifies NF-κB (already mapped) and IL-1β (already mapped) cytokine storm of severe RSV infection.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — RSV iron: iron, as cofactor for ribonucleotide reductase in type-ii-pneumocytes (already mapped) and macrophages (already mapped), supports antiviral immunity; iron overload amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative-stress cascade of RSV bronchiolitis.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — RSV phosphorus: phosphorus, as ATP precursor in neutrophils (already mapped) and macrophages (already mapped), fuels phagocytic burst; phosphorus deficiency impairs dendritic-cell (already mapped) and amplifies IL-6 (already mapped) and NF-κB (already mapped) cascade of RSV.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — RSV chloride: chloride, via CFTR in airway epithelial and type-ii-pneumocyte (already mapped) cells, regulates mucociliary clearance; chloride channel dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of RSV bronchiolitis.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — RSV sulfur: hydrogen sulfide, from sulfur-amino acids in type-ii-pneumocytes (already mapped) and macrophages (already mapped), promotes bronchodilation; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) airway inflammatory cascade of RSV bronchiolitis.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — RSV nitrogen: nitric oxide from macrophages (already mapped) and type-ii-pneumocytes (already mapped) mediates antiviral vasodilation; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 inflammasome (already mapped) cascade of RSV.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — RSV carbon: carbon, as metabolic backbone of viral envelope lipids and type-ii-pneumocytes (already mapped), enables viral replication; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) cascade of RSV bronchiolitis.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — RSV PD-1: PD-1 checkpoint on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates antiviral immune tolerance; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) airway inflammatory cascade of RSV.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — RSV GLP-1: GLP-1 signalling in type-ii-pneumocytes (already mapped) and endothelial cells (already mapped) modulates airway metabolic homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of RSV bronchiolitis.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — RSV angiotensin-II: angiotensin-II signalling in type-II pneumocytes (already mapped) and endothelial cells (already mapped) promotes pulmonary vascular inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) airway cascade of RSV.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — RSV Wnt/β-catenin: Wnt/β-catenin signalling in type-II pneumocytes (already mapped) supports airway epithelial repair; Wnt dysregulation amplifies NF-κB (already mapped) and TGF-β/SMAD4 (already mapped) fibrotic cascade of RSV bronchiolitis.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — RSV RANKL: RANKL signalling in macrophages (already mapped) and airway stromal cells modulates bone-immune crosstalk; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of RSV.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — RSV fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds RSV-infected airway ECM; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — RSV notch: NOTCH on macrophages (already mapped) and airway epithelial cells (already mapped) regulates RSV immune response; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — RSV igf-1: IGF-1 from macrophages (already mapped) and fibroblasts (already mapped) modulates airway repair after RSV infection; igf-1 excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — RSV activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) regulates airway immune-fibrotic balance; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — RSV calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway calcium balance; calcitonin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — RSV insulin-receptor: insulin receptor on macrophages (already mapped) and fibroblasts (already mapped) drives airway metabolic tone; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) cascade of RSV.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — RSV tgf-beta: TGF-β from fibroblasts (already mapped) and macrophages (already mapped) drives RSV airway immune-fibrotic remodelling; tgf-beta excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — RSV aldosterone: aldosterone from macrophages (already mapped) and fibroblasts (already mapped) modulates airway ion balance; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — RSV androgen-receptor: androgen receptor on macrophages (already mapped) and fibroblasts (already mapped) modulates RSV steroid tone; androgen-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — RSV norepinephrine: norepinephrine from macrophages (already mapped) and fibroblasts (already mapped) modulates airway adrenergic tone; norepinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — RSV adrenomedullin: adrenomedullin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway vascular tone; adrenomedullin loss amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — RSV bdnf: BDNF from macrophages (already mapped) and fibroblasts (already mapped) supports airway neural trophic tone; bdnf loss amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — RSV fgfr: FGFR on macrophages (already mapped) and fibroblasts (already mapped) drives airway stromal growth; fgfr dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — RSV epinephrine: epinephrine from macrophages (already mapped) and fibroblasts (already mapped) modulates airway adrenergic tone; epinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — RSV renin: renin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway RAAS balance; renin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Myostatin](../../03-molecular/myostatin/README.md)** — RSV myostatin: myostatin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway muscle balance; myostatin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — RSV angiopoietin: angiopoietin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway vascular remodelling; angiopoietin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — RSV ghrelin: ghrelin from macrophages (already mapped) and fibroblasts (already mapped) modulates airway metabolic tone; ghrelin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and type-i-interferon (already mapped) airway cascade of RSV.
