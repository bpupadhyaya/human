---
schema: human-scale-entry/v1
id: respiratory-system
name: Respiratory system
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-03
summary: "Airways, lungs, chest wall, and diaphragm forming the gas-exchange apparatus: ~6 L/min ventilation to 300 million alveoli. Coupled to the cardiovascular system via the pulmonary circuit. Controlled by medullary respiratory centres and chemoreceptors."
aliases: ["respiratory system", "pulmonary system", "ventilatory system"]
sources:
  - id: west-respiratory-physiology
    type: textbook
    cite: "West JB, Luks AM. West's Respiratory Physiology: The Essentials. 10th ed. Wolters Kluwer; 2016. ISBN 978-1-4963-1011-1."
    url: "https://www.lww.com/Product/9781496310118"
    accessed: "2026-06-03"
  - id: weibel-2017-alveolar-dimensions
    type: peer-reviewed
    cite: "Weibel ER. Lung morphometry: the link between structure and function. Cell Tissue Res. 2017;367(3):413-26."
    doi: "10.1007/s00441-016-2541-4"
    pmid: "27981371"
    url: "https://doi.org/10.1007/s00441-016-2541-4"
  - id: openstax-anatomy-ch22
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 22: The Respiratory System."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/22-introduction"
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/06-organ/lung
    relation: contains
    note: "The paired lungs are the gas-exchange organs of the respiratory system, containing ~300 million alveoli and a ~70 m² surface area for O₂–CO₂ exchange."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The respiratory system is one of the eleven major organ systems of the human body; it interacts most closely with the cardiovascular system via the pulmonary circuit."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "The respiratory and cardiovascular systems are functionally inseparable: the pulmonary circuit carries deoxygenated blood to the alveolar capillaries and returns oxygenated blood to the left heart, coupling gas exchange to systemic O₂ delivery."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: damaged-by
    note: "Influenza A is primarily a respiratory pathogen; severe disease causes viral pneumonitis, ARDS, and respiratory failure through destruction of the alveolar-capillary interface."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: infected-by
    note: "S. pneumoniae colonizes the nasopharynx asymptomatically in 5–70% of children; lower respiratory tract invasion causes lobar pneumonia, bacteremia (20–30% of CAP), and meningitis; the respiratory system is its primary site of pathology."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: damaged-by
    note: "Pneumococcal pneumonia causes acute alveolar consolidation, fibrinopurulent exudate, impaired gas exchange, and — in severe disease — respiratory failure; pneumolysin contributes to alveolar epithelial damage."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: treated-by
    note: "Inhaled corticosteroids (ICS) are the cornerstone maintenance therapy for persistent asthma, reducing airway inflammation and exacerbation frequency by 50–60%; systemic corticosteroids are first-line for COPD exacerbations and acute severe asthma."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: damaged-by
    evidence: west-respiratory-physiology
    note: "A. fumigatus conidia inhaled into the respiratory system germinate in the bronchi and alveoli of immunocompromised hosts, causing invasive pulmonary aspergillosis with angioinvasion and haemoptysis."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: modulated-by
    note: "Modulated by Smooth Muscle Cell."
  - target: 02-pathogen/01-viruses/respiratory-syncytial-virus
    relation: damaged-by
    note: "Damaged by Respiratory Syncytial Virus."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: damaged-by
    note: "Damaged by Pneumocystis jirovecii (formerly carinii)."
  - target: 03-medicine/01-modern/05-antiviral/oseltamivir
    relation: treated-by
    note: "Oseltamivir reduces influenza A/B symptom duration by ~17 hours (Dobson meta-analysis, Lancet 2015); reduces hospitalization in high-risk patients (elderly, immunocompromised, pregnant); must be started within 48h of symptom onset for maximal benefit."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Asthma is the commonest chronic disease of the respiratory system's airways: reversible bronchoconstriction and type-2 inflammation narrow the bronchi, causing wheeze and breathlessness—so the conducting airways, not the gas-exchange surface, bear the brunt of asthma."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "COPD is the major irreversible obstructive disease of the respiratory system: smoking-driven inflammation destroys alveoli (emphysema) and scars airways (chronic bronchitis), permanently limiting airflow—the chief cause of chronic respiratory failure in older adults."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "Type II pneumocytes keep the respiratory system's gas-exchange surface working: they secrete surfactant that prevents alveolar collapse and act as progenitors regenerating the alveolar lining after injury—so their loss in ARDS and pneumonia drives respiratory failure."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Oxygen is the gas the respiratory system exists to capture: alveoli transfer O2 across the air-blood barrier into hemoglobin for tissue delivery, while CO2 is exhaled—so lung disease that impairs this exchange causes hypoxemia, the central threat in respiratory failure."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Hemoglobin completes what the respiratory system starts: lungs load O2 onto red-cell hemoglobin, which carries it to tissues and returns CO2 for exhalation—so anemia or abnormal hemoglobin can mimic lung disease by limiting oxygen delivery despite healthy lungs."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "The alveolus is the functional unit of the respiratory system: hundreds of millions of these thin-walled sacs create the vast surface where gas exchange occurs, so diseases that flood, collapse, or stiffen alveoli directly cause the hypoxemia of respiratory failure."
  - target: 01-human/03-molecular/surfactant
    relation: connects-to
    note: "Pulmonary surfactant keeps the respiratory system inflatable: secreted by type II pneumocytes, it lowers alveolar surface tension so the lung doesn't collapse on exhalation—its deficiency causes neonatal respiratory distress and contributes to ARDS in adults."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "COVID-19 is the respiratory system's defining modern threat: SARS-CoV-2 attacks airway and alveolar cells, and severe disease causes diffuse alveolar damage and hypoxemic respiratory failure—showing how a single virus can overwhelm the gas-exchange apparatus."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Pulmonary arterial hypertension is where the respiratory and circulatory systems collide: remodeling of the lung's small arteries raises pulmonary pressure until the right heart fails, so this is a vascular disease that presents as breathlessness."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Breathing is run by the nervous system: brainstem respiratory centers set the rhythm and chemoreceptors sensing CO2 and oxygen adjust it breath by breath, so the respiratory system is only as reliable as the neural drive—lost in opioid overdose or brainstem stroke."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Respiration exists to trade carbon dioxide for oxygen: cells make CO2, blood carries it as bicarbonate, and the lungs exhale it, so the respiratory system is the body's main route to dump carbon—and CO2 levels set blood pH and the urge to breathe."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Alveolar macrophages guard the respiratory system: stationed in the air sacs, they engulf inhaled microbes and debris as the lung's first cellular defense, so their function (and dysfunction in smoking or COPD) shapes vulnerability to pneumonia."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Red cells complete the respiratory system's job: the lungs load oxygen onto erythrocyte hemoglobin and unload carbon dioxide, so breathing and the blood's red cells are one continuous gas-exchange system—lung disease and anemia both starve tissues of oxygen."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "Cystic fibrosis is the respiratory system's archetypal genetic disease: a chloride-channel defect thickens airway mucus, trapping bacteria and causing the chronic infection and bronchiectasis that destroy the lungs—now transformed by CFTR-modulator drugs."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide fine-tunes the lungs' blood flow: it dilates pulmonary vessels to match perfusion with ventilation, and inhaled NO is used to open lung vessels in pulmonary hypertension and newborn respiratory failure."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "The respiratory system is the body's fast acid-base dial: by speeding or slowing breathing it controls how much CO2—and thus acid (hydrogen ions)—leaves the blood, so the lungs and kidneys together hold blood pH in its narrow safe range."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Breathing is commanded by the brain: the brainstem's respiratory centers set the rhythm and adjust it to CO2 and oxygen sensors, so the respiratory system is only as reliable as the neural drive behind it—lost in overdose or stroke."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells make the airways reactive: lining the bronchial walls, they release histamine and other mediators that constrict and inflame airways in asthma and allergy, a key cellular trigger of the wheezing respiratory diseases."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Air is mostly nitrogen, and the lungs must reckon with it: this inert gas makes up most of each breath without being used, but under pressure it dissolves into blood and, on fast ascent from diving, bubbles out to cause decompression sickness."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils both defend and damage the airways: they swarm into infected or inflamed lungs to kill microbes, but in COPD, cystic fibrosis, and ARDS their flood of enzymes also digests lung tissue, driving chronic damage."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The lungs and right heart are one circuit: the right ventricle pumps all the blood through the lungs for gas exchange, so chronic lung disease that stiffens this circuit overloads and fails the right heart (cor pulmonale)."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "The lungs are read in X-ray photons: chest radiographs and CT reveal pneumonia, tumors, fibrosis and collapse, the first window into respiratory disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Scarring stiffens the lungs: pulmonary fibrosis thickens the alveolar walls so oxygen can't cross and the lungs lose their stretch, the end-stage of many chronic lung diseases."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Lungs and kidneys jointly guard blood pH: the lungs blow off acid as CO2 while the kidneys excrete it, so each compensates when the other fails, the core of acid-base balance."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the gossamer blood-air barrier: alveolar epithelium and capillary endothelium fuse into a membrane thin enough for oxygen to cross, while type II cells store surfactant in lamellar bodies and airway cells wave their cilia."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin betrays failing lungs: when oxygen runs short, deoxygenated hemoglobin turns the lips and fingertips blue in cyanosis, making the skin a visible readout of how well the respiratory system is working."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut and lungs share an immune conversation: through the gut-lung axis, the intestinal microbiome shapes airway immunity, so gut health influences susceptibility to asthma and respiratory infection."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The airway is a frontline of immunity: with every breath the lungs meet airborne microbes, so mucociliary clearance, alveolar macrophages, and bronchus-associated lymphoid tissue form a vast immune barrier between the outside air and the blood."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "The vagus nerve tunes the airways with acetylcholine: parasympathetic cholinergic tone constricts bronchial smooth muscle and drives mucus, which is why anticholinergics (ipratropium, tiotropium) open the airways in asthma and COPD."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "One faulty channel ties lung to pancreas: in cystic fibrosis a defective CFTR thickens secretions in both, clogging the airways with mucus while blocking the pancreatic ducts that should deliver digestive enzymes."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The airway mucosa is an antibody barrier: secretory IgA coats it to trap inhaled pathogens, while monoclonal antibodies against IgE and IL-5 now treat severe asthma — and misdirected antibody drives autoimmune lung disease like Goodpasture."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "A gut-lung axis links the two surfaces: the airway has its own microbiome, and gut flora shape lung immunity and allergic-asthma risk through circulating microbial metabolites — distant microbes tuning the respiratory tract."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Breathing bends to pregnancy and begins before birth: progesterone drives the increased ventilation and breathlessness of pregnancy, while fetal lung maturation and surfactant production set the timing of safe delivery."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "ARDS is the respiratory system's final common failure: diffuse alveolar injury floods the gas-exchange surface with fluid, collapsing oxygenation and forcing the mechanical ventilation that defines critical respiratory illness."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Tuberculosis is the archetypal chronic lung infection: Mycobacterium tuberculosis cavitates the parenchyma over months and remains among the leading infectious killers worldwide, a defining disease of the respiratory tract."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "RSV is the leading cause of infant lower-respiratory infection: it inflames and plugs the small bronchioles, the commonest reason babies are hospitalized for trouble breathing."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine narrows the airways: released from bronchial mast cells it constricts smooth muscle, swells the mucosa, and floods secretions, the rapid mediator behind allergic wheeze and a driver of airway hyper-reactivity."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Influenza is the recurring epidemic threat to the respiratory system: the virus strips the airway epithelium and can progress to viral pneumonia and ARDS, and its seasonal waves drive much of winter respiratory illness."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity mechanically loads the respiratory system: excess chest and abdominal fat restrict lung expansion and, with upper-airway crowding, cause obstructive sleep apnoea and obesity hypoventilation that blunt ventilation."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "The respiratory system's commonest fatal cancer: non-small-cell lung cancer arises from the bronchial and alveolar epithelium, the leading cancer killer worldwide and the malignant counterpart to the system's smoking-related diseases."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "Its most aggressive tumor grows from airway neuroendocrine cells: small-cell lung cancer is a fast, early-metastasizing cancer of the central airways, almost always smoking-related, defining the deadliest end of respiratory malignancy."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "Asbestos scars the lining of the lungs into cancer: mesothelioma arises from the pleura that encloses the respiratory system, decades after asbestos exposure, a malignancy of the system's serosal envelope rather than its airways."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Autoimmune fibrosis stiffens the lungs: systemic sclerosis is a leading cause of interstitial lung disease and pulmonary hypertension, scarring the respiratory system into the disorder's commonest cause of death."
  - target: 01-human/07-system/measles
    relation: connects-to
    note: "A childhood virus drowns the lungs: measles causes a giant-cell pneumonia that, especially in the malnourished or immunocompromised, is the leading fatal complication of the infection — a viral assault on the respiratory system."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Group A strep can ravage the lungs: Streptococcus pyogenes can cause a fulminant necrotizing pneumonia with empyema, a rapidly destructive bacterial infection of the respiratory system often following a viral illness."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The lungs and right heart share one circuit: chronic lung disease that stiffens the pulmonary vasculature overloads the right ventricle into cor pulmonale, a respiratory route to heart failure."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its great emergency is a lodged clot: pulmonary embolism, a venous thromboembolism that travels to the lung arteries, abruptly blocks gas exchange and strains the right heart — a leading cause of sudden respiratory collapse."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Chronic breathlessness wears on mood: the activity limitation, fear of suffocation and poor sleep of chronic respiratory disease give conditions like COPD high rates of depression."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "They share an origin and a crossroads: lungs and gut both arise from the embryonic foregut and meet at the pharynx, so swallowing disorders cause aspiration and a gut-lung axis links the two."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Lungs and kidneys jointly balance acid: the respiratory and renal systems co-regulate pH by controlling CO2 and bicarbonate, and pulmonary-renal syndromes like Goodpasture attack both at once."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Muscle and rib cage are its pump: the diaphragm and intercostals power ventilation within a bony thorax, so neuromuscular weakness and chest-wall deformity cause restrictive respiratory failure."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "The lung is also an endocrine organ: its endothelium converts angiotensin I to II via ACE, a key step in blood-pressure control, and pulmonary neuroendocrine cells secrete bioactive peptides."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It is guarded and drained by lymphatics: bronchus-associated lymphoid tissue defends the airways and a rich lymphatic network clears the lungs, so injury to it causes chylothorax."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin mirrors the lungs: finger clubbing, central cyanosis and tar staining reveal chronic respiratory disease, and skin and airway share the body's barrier defences against the environment."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "The lung is its principal home: Mycobacterium tuberculosis is inhaled into the alveoli where it sets up the granulomatous infection that remains the world's leading infectious cause of death."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "A pandemic virus that targets the airways: SARS-CoV-2 enters through ACE2 on respiratory epithelium, causing pneumonia and diffuse alveolar damage in severe COVID-19."
  - target: 02-pathogen/06-environmental/zoonosis
    relation: connects-to
    note: "Many emerging lung infections jump from animals: avian influenza, SARS, MERS and hantavirus reach the human respiratory tract from animal reservoirs, a recurring source of pandemics."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "A major cause of pneumonia: Staphylococcus aureus, including MRSA, causes severe necrotising and post-influenza pneumonia and is a leading organism in ventilator-associated lung infection."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Nutrition shapes lung defence: vitamin D supports airway immunity, and deficiency is associated with more frequent respiratory infections and worse asthma control."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "A heart drug heard in the chest: ACE inhibitors raise bradykinin in the airway, causing the dry cough and rare angioedema that are among the commonest reasons patients stop them."
  - target: 01-human/05-tissue/lung-slice
    relation: connects-to
    note: "The working tissue of breathing: the lung's conducting airways and alveolar parenchyma — seen on a lung slice — humidify, conduct and exchange air, the tissue-level substrate of every respiratory disease from asthma to fibrosis."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Biologics and TKIs target the airway: anti-IL-5/IL-4 monoclonals control severe asthma while EGFR, ALK and checkpoint therapies treat lung cancer — precision drugs reshaping respiratory medicine."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "It treats and it scars the lung: cytotoxic chemotherapy is central to lung cancer, yet agents like bleomycin and methotrexate cause drug-induced pneumonitis and pulmonary fibrosis, a toxicity unique to the respiratory system."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Mucosal immunity of the airway: bronchus-associated lymphoid tissue forms germinal-centre-like structures in the lung that mature B cells and mount local antibody responses to inhaled pathogens."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Pneumonia is the leading source of sepsis: severe respiratory infection and ARDS are the commonest trigger of sepsis, the respiratory tract as the gateway to systemic collapse."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "The lung-kidney oxygen axis: the respiratory system loads oxygen onto haemoglobin, and chronic hypoxic lung disease drives erythropoietin release and secondary polycythaemia."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Vasculitis of the airways: ANCA-associated vasculitis (granulomatosis with polyangiitis) attacks the upper and lower respiratory tract, causing sinus destruction, lung nodules and alveolar haemorrhage."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Immunodeficiency and the lung: HIV/AIDS predisposes to Pneumocystis pneumonia, tuberculosis and other respiratory infections, the lung a frequent battleground of failing immunity."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Autoimmune lung scarring: dermatomyositis (notably anti-MDA5) causes a rapidly progressive interstitial lung disease, one of the connective-tissue diseases that fibrose the respiratory system."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "The commonest CTD lung disease: rheumatoid arthritis causes interstitial lung disease, pleuritis, nodules and bronchiectasis, making it the leading connective-tissue cause of chronic lung involvement."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Bronchiolitis obliterans: chronic lung graft-versus-host disease after stem-cell transplant scars and obliterates the small airways, a major and often irreversible late respiratory complication."
  - target: 01-human/07-system/marfan-syndrome
    relation: connects-to
    note: "Spontaneous pneumothorax: connective-tissue disorders such as Marfan form apical lung blebs that rupture, making spontaneous pneumothorax a structural respiratory complication of the syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Airway inflammation: IL-6 is a central cytokine of respiratory inflammation, elevated in asthma, COPD and the pneumonias and ARDS that injure the lung."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory lung injury: TNF-α drives the neutrophilic inflammation of acute lung injury and chronic airway disease, a key mediator of respiratory pathology."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Airway sentinels: dendritic cells lining the airway epithelium sample inhaled antigens and orchestrate the immune responses—protective and allergic—of the respiratory mucosa."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Non-respiratory endocrine role: the pulmonary capillary endothelium is the body's main site of angiotensin-converting enzyme, converting angiotensin I to the vasopressor angiotensin II as blood transits the lung."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Alveolar-capillary maintenance: VEGF sustains the dense pulmonary capillary network of the gas-exchange surface, and its loss contributes to the alveolar destruction of emphysema."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Airway alarmin: airway epithelium releases TSLP on injury or allergen exposure, the upstream alarm signal that initiates the type 2 inflammation of asthma and is targeted by tezepelumab."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin metabolism: the pulmonary endothelium is the principal site of ACE-mediated bradykinin degradation, so ACE inhibitors raise airway bradykinin and cause the dry cough that is their hallmark side effect."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Airway and vascular tone: prostaglandins and related eicosanoids set bronchial tone (PGE2 dilating, leukotrienes constricting) and modulate the pulmonary circulation, central mediators of airway physiology and asthma."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Pulmonary vascular tone: endothelin-1 is the dominant constrictor of the pulmonary circulation and the mediator of hypoxic pulmonary vasoconstriction, the basis for endothelin antagonists in pulmonary hypertension."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal defence: secretory IgA coating the airway epithelium neutralises inhaled pathogens at the mucosal surface, the first line of respiratory immune defence that protects the vast air-tissue interface of the lungs from constant microbial exposure."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "Oxygen sensing: HIF-2α (EPAS1) is the master oxygen sensor of the pulmonary circulation and carotid body, driving hypoxic pulmonary vasoconstriction and the ventilatory and erythropoietic responses that adapt the respiratory system to low oxygen."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Bronchodilation: epinephrine acting on β2-adrenergic receptors relaxes airway smooth muscle to widen the bronchi, the basis of the β2-agonist inhalers that are the mainstay of relieving acute airflow obstruction."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic response: alongside the HIF-2α/EPAS1 already mapped, HIF-1α mediates the lung's response to low oxygen, including the hypoxic pulmonary vasoconstriction that diverts blood from poorly ventilated regions to match perfusion to ventilation."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Lung morphogenesis: FGF10-FGFR signalling drives the branching morphogenesis that builds the bronchial tree and alveoli, the core developmental programme of the respiratory system."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Airway cell fate: NOTCH signalling specifies the ciliated, club, goblet and neuroendocrine cell fates of the airway epithelium, patterning the conducting airways and their mucociliary defence."
  - target: 01-human/03-molecular/cftr
    relation: connects-to
    note: "Airway surface liquid: CFTR chloride and bicarbonate transport sets the airway surface liquid that enables mucociliary clearance, the frontline airway defence whose failure defines cystic fibrosis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Th2 airway response: IL-13 drives the goblet-cell mucus hypersecretion and bronchial hyperreactivity of the Th2 airway response that underlies asthma and allergic airway disease."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidant defence: NRF2 governs the antioxidant programme that protects the airway and alveolar epithelium from inhaled oxidants, pollutants and cigarette smoke at the gas-exchange surface."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β drives airway remodelling and the fibrotic repair of lung injury, a central effector across chronic respiratory disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is the master transcriptional hub of airway and alveolar inflammation across infection, asthma and COPD."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling supports alveolar and airway-epithelial survival and the repair responses that maintain the gas-exchange surface."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies airway and alveolar inflammation and drives the pulmonary fibrosis shared across chronic lung diseases of the respiratory system."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling drives the airway inflammation and mucus responses common to inflammatory diseases of the respiratory system."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING sensing of viral and damage-associated cytosolic DNA shapes the antiviral and inflammatory responses of the respiratory epithelium."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the airway epithelial oxidative-stress defense and immune-metabolic balance across respiratory disorders."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the antiviral and inflammatory responses of the airway epithelium across the respiratory system."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of growth factors (FGFR already mapped) drives airway epithelial proliferation, repair, and remodeling in the respiratory system."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the airway inflammatory and epithelial-repair signaling of the respiratory system."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the airway epithelial proliferation, survival, and immune responses of the respiratory system."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins participate in the innate inflammatory signaling of the airway and alveolar responses of the respiratory system."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the airway epithelial and alveolar energy homeostasis of the respiratory system."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the airway epithelial and alveolar-macrophage homeostasis and host defense of the respiratory system."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling coordinates the growth, surfactant metabolism, and immune responses of the respiratory system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the airway epithelial and immune gene programs of the respiratory system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment participates in the airway immune surveillance and inflammatory responses of the respiratory system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the airway epithelial junction dynamics and growth-factor responses of the respiratory system."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the airway immune-cell trafficking and repair of the respiratory system."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the airway inflammatory responses of the respiratory system."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the airway epithelial and innate immune responses of the respiratory system."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Acid-base and drive: the lungs set systemic pH by adjusting carbon-dioxide excretion, and central and peripheral chemoreceptors sensing protons and CO2 tune the ventilatory drive minute to minute."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Airway smooth muscle: calcium-dependent contraction of airway smooth muscle sets bronchomotor tone, the target of the bronchodilators and bronchoconstrictors that widen or narrow the conducting airways."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Bronchodilation and muscle: magnesium relaxes airway smooth muscle by antagonising calcium entry, the basis of intravenous magnesium in severe bronchospasm, and is required for normal respiratory-muscle function."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Central respiratory drive: opioids acting on mu-opioid receptors in the brainstem (brain already mapped) suppress the respiratory rhythm, the mechanism of opioid respiratory depression that makes the respiratory system uniquely vulnerable to these drugs."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Chemoreception and pulmonary tone: serotonergic medullary neurons contribute to central CO2 chemoreception and breathing control, while serotonin also constricts the pulmonary vasculature, linking the transmitter to both ventilation and lung perfusion."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Ventilatory drive: leptin stimulates central respiratory drive, and leptin resistance in obesity contributes to obesity hypoventilation syndrome, connecting the adipokine to the neural control of breathing."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Neurogenic airway control: CGRP released from airway sensory nerves contributes to the neurogenic inflammation, vasodilation and cough reflex of the respiratory system, part of the neuro-immune regulation of the airways."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Cough and neurogenic reflex: substance P from airway sensory nerves, with CGRP (already mapped), mediates the cough reflex and the neurogenic inflammation and bronchoconstriction of the respiratory tract."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative lung injury: xanthine-oxidase-derived reactive oxygen species contribute to the oxidative stress of respiratory disease (NRF2 already mapped), driving the epithelial injury and inflammation of the airways and alveoli."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Airway surface liquid: chloride secretion through the CFTR channel (already mapped) hydrates the airway surface liquid and mucus, and its failure causes the thick secretions of cystic fibrosis that obstruct the respiratory tract."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Airway calibre: the airway smooth muscle sets the bronchial calibre, contracting to acetylcholine and relaxing to adrenaline (already mapped), and its constriction and remodelling underlie the airflow limitation of respiratory disease."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Neural control of breathing: the nervous system's brainstem respiratory centres and the chemoreceptors sense oxygen and carbon dioxide (already mapped) to drive ventilation, and the sensory nerves (CGRP and substance P already mapped) mediate cough and airway reflexes."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 airway immunity: IL-4, with IL-13 (already mapped), drives the type-2 immunity of the airways of the respiratory system, the allergic and mucus-hypersecretory response of asthma and allergic disease."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophilic inflammation: IL-5 recruits the eosinophils of the eosinophilic airway inflammation of the respiratory system, the target of the anti-IL-5 biologics in severe asthma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Neutrophilic airway inflammation: IL-17 drives the neutrophilic, non-type-2 airway inflammation of the respiratory system, part of the severe steroid-resistant asthma and the infective and COPD neutrophilia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Respiratory-metabolic adipokine: adiponectin, with leptin (already mapped), is the adipokine of the respiratory-metabolic crosstalk; the obesity affects the ventilation and the airway inflammation of the respiratory system."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Airway-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose to the airway inflammation and the obesity-related respiratory dysfunction."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Antiviral airway interferon: the airway epithelium's type-I interferon (with the secretory-IgA already mapped) defends the respiratory system against the inhaled respiratory viruses."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 airway immunity: the IFN-γ of the airway T cells is the type-II interferon arm of the Th1 antiviral and antimycobacterial immunity of the respiratory system."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the airway immunity, counter-balancing the type-2 (IL-4, IL-5 and IL-13 already mapped) allergic response of the respiratory system."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 airway axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neutrophilic airway inflammation of the respiratory system."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Allergic airway arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), arms the mast cells (already mapped) of the allergic airway (rhinitis/asthma) response of the respiratory system."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Airway tolerance: IL-10 is the regulatory cytokine that maintains the mucosal tolerance and resolves the airway inflammation of the respiratory system."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 airway helper: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines coordinating the mucosal immunity of the respiratory system."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Type-2 remodelling: periostin, downstream of the IL-13 (already mapped) signalling, is a matricellular marker and mediator of the type-2 airway remodelling and the subepithelial fibrosis of the respiratory system."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Airway itch/cough: IL-31, a type-2 (IL-4, IL-5 and IL-13 already mapped) cytokine, is part of the neuroimmune signalling of the cough and airway sensory dimension of the respiratory system."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Airway complement: the complement C3, produced locally by the airway epithelium, is part of the innate mucosal defence and, when dysregulated, the inflammation of the respiratory system."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) generate the anaphylatoxin and membrane-attack complex of the acute lung injury and the airway inflammation of the respiratory system."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil recruitment into the airway and alveolus in the immunopathology of the respiratory system."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) on the airway surface, restraining the complement attack on the host lung of the respiratory system."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Airway kinin brake: C1-esterase inhibitor, by controlling the contact-pathway kinin cascade (bradykinin already mapped) and the classical complement, moderates the airway oedema, the bronchospasm, and the hereditary angioedema exacerbations of the respiratory system."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Antioxidant-airway axis: melatonin, from the pineal (already mapped) and local bronchial epithelium, exerts antioxidant and anti-inflammatory effects on the airway, modulating the nocturnal bronchoconstriction and the ROS-driven mucosal injury of the respiratory system."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Mucosal immunity: prolactin, from the pituitary (already mapped) and local airway epithelium, modulates the respiratory mucosal IgA (already mapped) secretion and the mast-cell (already mapped) responsiveness of the immune surveillance of the respiratory system."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone lung axis: testosterone modulates the alveolar and bronchial epithelial response; sex-based differences in respiratory mechanics, asthma (already mapped) severity, and COPD (already mapped) outcomes are in part mediated by androgen-testosterone-immune interactions."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron-lung metabolism: transferrin, the iron carrier, reflects the iron handling that governs the alveolar macrophage (already mapped) function and the mucociliary defence; iron overload and deficiency each impair the respiratory-epithelial barrier and innate immunity."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, via selenoproteins in the lung-epithelium (already mapped), protects against ROS-driven alveolar injury and modulates the type-2 and type-1 airway-immune balance of the respiratory system (asthma, COPD already mapped)."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Airway-immune neuropeptide: oxytocin, via OXTR on mast cells (already mapped) and smooth-muscle cells (already mapped), attenuates airway inflammation; oxytocin modulates the IL-5 (already mapped) and IL-13 (already mapped) type-2 airway response of the respiratory system."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Vasomotor-airway axis: vasopressin, via V1aR on smooth-muscle cells (already mapped) and endothelial cells, modulates pulmonary vascular tone; vasopressin dysregulation amplifies the pulmonary arterial hypertension (already mapped) of the respiratory system."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Thyroid-respiratory axis: iodine-dependent thyroid hormones modulate mucociliary clearance and alveolar (already mapped) surfactant (already mapped) production; iodine deficiency impairs the respiratory-epithelial defence and the macrophage (already mapped) innate immunity."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium, via ENaC-driven airway-surface liquid homeostasis in lung-epithelium (already mapped), maintains mucociliary clearance; sodium dysregulation amplifies the IL-6 (already mapped) and neutrophil (already mapped) inflammatory cascade of the respiratory system."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper, as cofactor of cytochrome-c oxidase in type-II pneumocytes (already mapped) and macrophages (already mapped), supports oxidative phosphorylation and innate immunity; copper deficiency impairs the antioxidant and phagocytic defences of the respiratory system."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium, via K⁺ channels on airway smooth-muscle cells (already mapped) and type-II pneumocytes (already mapped), sets airway tone and epithelial secretion; potassium dysregulation amplifies the bronchoconstriction and IL-6 (already mapped) cascade of the respiratory system."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc, as metalloproteinase cofactor in macrophages (already mapped) and neutrophils (already mapped), maintains innate immunity; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of the respiratory system."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron, as haem cofactor in erythrocytes (already mapped) and macrophages (already mapped), enables oxygen transport; iron deficiency impairs the NF-κB (already mapped) anti-microbial response and amplifies the IL-6 (already mapped) inflammatory cascade of the respiratory system."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Phosphorus, as ATP precursor in type-II pneumocytes (already mapped) and macrophages (already mapped), supports surfactant synthesis and innate immunity; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of the respiratory system."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Respiratory sulfur: H2S from sulfur-amino acids in type-II pneumocytes (already mapped) and endothelial cells (already mapped) promotes airway vasodilation; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Respiratory PD-1: PD-1 checkpoint on macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates airway immune surveillance; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) airway inflammatory cascade of the respiratory system."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Respiratory GLP-1: GLP-1 signalling in type-II pneumocytes (already mapped) and endothelial cells (already mapped) modulates airway metabolic homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Respiratory Wnt/β-catenin: Wnt/β-catenin signalling supports type-II pneumocyte (already mapped) repair and airway epithelial regeneration; Wnt dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrotic cascade of the respiratory system."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Respiratory RANKL: RANKL signalling in macrophages (already mapped) and type-II pneumocytes (already mapped) regulates bone-airway mineral crosstalk; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of the respiratory system."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Respiratory SMAD4: SMAD4-mediated TGF-β (already mapped) signalling in type-II pneumocytes (already mapped) and fibroblasts (already mapped) drives airway fibrosis; SMAD4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Respiratory IL-2: IL-2 expands T-cytotoxic cells (already mapped) and regulatory T-cells in airway immune surveillance; IL-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of the respiratory system."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "RS fibronectin: fibronectin in airway matrix and bronchial epithelial cells modulates lung structural repair; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) remodelling cascade of the respiratory system."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "RS IGF-1: IGF-1 from bronchial epithelium (already mapped) and lung macrophages (already mapped) sustains lung growth and repair; IGF-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "RS activin-A: activin-A from lung fibroblasts (already mapped) and macrophages (already mapped) modulates inflammation and fibrosis; activin-A excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of the respiratory system."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Resp calcitonin: calcitonin from lung cells (already mapped) and macrophages (already mapped) modulates respiratory calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Resp insulin-receptor: insulin receptor on lung cells (already mapped) and macrophages (already mapped) drives metabolic tone; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) respiratory fibrotic cascade."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Resp aldosterone: aldosterone from macrophages (already mapped) and lung fibroblasts (already mapped) modulates respiratory fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Resp androgen-receptor: androgen receptor on lung cells (already mapped) and macrophages (already mapped) modulates sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Resp norepinephrine: norepinephrine from sympathetic nerves (already mapped) and macrophages (already mapped) modulates airway tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Resp adrenomedullin: adrenomedullin from lung cells (already mapped) and macrophages (already mapped) modulates pulmonary vasodilation; adrenomedullin loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Resp bdnf: BDNF from lung cells (already mapped) and macrophages (already mapped) supports airway neural trophic tone; bdnf loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Resp osteopontin: osteopontin from lung cells (already mapped) and macrophages (already mapped) promotes airway ECM remodelling; osteopontin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Resp angiopoietin: angiopoietin from lung cells (already mapped) and macrophages (already mapped) drives pulmonary angiogenesis; angiopoietin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "Resp renin: renin from lung cells (already mapped) and macrophages (already mapped) modulates pulmonary RAAS balance; renin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "Resp myostatin: myostatin from lung cells (already mapped) and macrophages (already mapped) modulates airway fibrotic tone; myostatin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/ace2
    relation: connects-to
    note: "Resp ace2: ACE2 on lung cells (already mapped) and macrophages (already mapped) modulates airway RAAS tone; ace2 loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Resp cortisol: cortisol from macrophages (already mapped) and lung cells (already mapped) modulates airway stress response; cortisol excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Resp ghrelin: ghrelin from macrophages (already mapped) and lung cells (already mapped) modulates airway metabolic signalling; ghrelin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Resp glucagon: glucagon from macrophages (already mapped) and lung cells (already mapped) modulates airway glucose metabolism; glucagon excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system."
taxonomy:
  uberon: "UBERON:0001004"
  fma: "FMA:7161"
---

# Respiratory system

## Overview

The respiratory system is the body's **gas-exchange apparatus** — the integrated set of structures that moves O₂ from ambient air into the bloodstream and removes CO₂ in the opposite direction, maintaining the arterial blood gas tensions (PaO₂ ~100 mmHg, PaCO₂ ~40 mmHg, pH ~7.40) essential for normal cellular function. It comprises:

1. **Upper airway** — nose, mouth, pharynx, larynx: filter, warm, humidify inspired air
2. **Conducting airways** — trachea → bronchi → bronchioles: transport air; no gas exchange; anatomical dead space ~150 mL
3. **Lungs and alveoli** — the gas-exchange parenchyma: ~300 million alveoli, ~70 m² surface area [^weibel-2017-alveolar-dimensions]
4. **Chest wall and diaphragm** — the mechanical pump: inspiratory muscles (diaphragm primary; external intercostals, accessory muscles) generate negative intrapleural pressure to drive air inward
5. **Pleura** — visceral and parietal pleura, maintaining the pressure linkage between lung and chest wall

The respiratory system cannot function in isolation — it is tightly coupled to the **cardiovascular system** via the pulmonary circuit, and its rhythm is driven by medullary and pontine **respiratory centres** modulated by chemoreceptors detecting PaO₂, PaCO₂, and arterial pH.

## Structure

### Upper Airway

The upper airway filters (nasal turbinates), warms, and humidifies inspired air. Key structures:

- **Nose/nasal cavity:** Mucociliary clearance; ~3 L/min airflow at rest through both nares
- **Nasopharynx / oropharynx:** Convergence of nasal and oral airstreams; site of tonsils and adenoids
- **Larynx:** Glottis (vocal cords) — the narrowest part of the adult upper airway; site of croup, epiglottitis, and intubation
- **Eustachian tube openings, sinuses:** Connected cavities whose inflammation (sinusitis, otitis) affects the upper respiratory tract collectively

### Conducting Airways (Trachea → Terminal Bronchioles)

- **Trachea:** ~11 cm long, 18 mm diameter; 16–20 C-shaped cartilage rings; lined by pseudostratified ciliated columnar epithelium with goblet cells (mucociliary escalator)
- **Bronchi:** 23 airway generations (Weibel) branch dichotomously; cartilage present to generation ~12–14; smooth muscle present throughout; innervated by autonomic nervous system (β2-AR → bronchodilation; M3 → bronchoconstriction)
- **Terminal bronchioles (generation 16):** ~0.5 mm diameter; no cartilage; pure smooth muscle wall; the last purely conducting airway segment

### Respiratory Zone (Generations 17–23)

- **Respiratory bronchioles:** First airways with alveolar outpouchings; begin gas exchange
- **Alveolar ducts / sacs / alveoli:** Full gas exchange; alveolar surface area 70 m² (see [Alveolus](../../05-tissue/alveolus/README.md))

### Respiratory Muscles

| Muscle | Role | Innervation |
|:---|:---|:---|
| **Diaphragm** | Primary inspiratory muscle; generates ~70% of inspiratory effort at rest | Phrenic nerve (C3–C5) |
| **External intercostals** | Elevate ribs → increase chest volume → inspiration | Intercostal nerves T1–T11 |
| **Accessory muscles** (sternocleidomastoid, scalenes) | Recruited in exercise and respiratory distress | Cranial and cervical nerves |
| **Internal intercostals / abdominals** | Active expiration (normally expiration is passive via lung recoil) | Intercostal and lumbar nerves |

**Diaphragm failure** (e.g., phrenic nerve injury in high cervical SCI, C3–C5 demyelination in Guillain-Barré) requires mechanical ventilation.

### Neural Control

The respiratory rhythm originates in the **medullary respiratory centres**:

- **Pre-Bötzinger complex** (ventral respiratory group, VRG): the respiratory rhythm generator; produces the ~12–16/min oscillatory inspiratory drive
- **Pneumotaxic centre** (pontine respiratory group): modulates breath timing, limits inspiratory duration
- **Ventral and dorsal respiratory groups:** Output to phrenic and intercostal motor neurons

**Chemoreceptor feedback:**
- **Central chemoreceptors** (medullary surface): respond to PCO₂/pH in CSF; most powerful driver of ventilation; rising PCO₂ → increased ventilation within seconds
- **Peripheral chemoreceptors** (carotid body, aortic body): respond to PaO₂ (<60 mmHg triggers significant activation), PaCO₂, and pH; primary O₂ sensors; important in acclimatisation to altitude

## Function

### Ventilation and Gas Exchange

At rest:
- **Respiratory rate:** 12–16 breaths/min
- **Tidal volume (VT):** ~500 mL
- **Minute ventilation (V̇E):** ~6–8 L/min
- **Alveolar ventilation (V̇A):** ~5.25 L/min (VE - dead space ventilation)

At maximal exercise:
- V̇E rises to **100–200 L/min** (20–30× resting)
- VT increases to ~3 L; RR increases to ~40–60/min
- O₂ uptake (VO₂max): 3,000–6,000 mL/min in trained athletes

The ventilatory control loop maintains PACO₂ at ~40 mmHg (and thus PaCO₂ ~40 mmHg) across this 20–30-fold change in metabolic rate — a remarkable regulatory achievement.

### Acid-Base Regulation

The respiratory system contributes to acid-base homeostasis via CO₂ regulation. The Henderson-Hasselbalch relationship:

$$\text{pH} = 6.1 + \log\frac{[\text{HCO}_3^-]}{0.0306 \times \text{PaCO}_2}$$

- **Respiratory acidosis:** Hypoventilation → ↑PaCO₂ → ↓pH (COPD exacerbation, opioid overdose, respiratory failure)
- **Respiratory alkalosis:** Hyperventilation → ↓PaCO₂ → ↑pH (anxiety, altitude, pulmonary embolism, early sepsis)
- **Metabolic acidosis:** Compensated by hypervention → ↓PaCO₂ (Kussmaul breathing in DKA)

### Mucociliary Defence

The mucociliary escalator (ciliated cells + goblet cell mucus) continuously clears particles, bacteria, and debris from the airways. Mucociliary dysfunction (cystic fibrosis, primary ciliary dyskinesia, chronic bronchitis) predisposes to recurrent pulmonary infection.

## Connections

- **Contains** → [Lung](../../06-organ/lung/README.md): The lungs are the gas-exchange organs, housing the alveolar parenchyma and branching airways.
- **Part-of** → [Human body](../../08-whole-body/human-body/README.md): The respiratory system is one of eleven major organ systems, interdependent with all others — cardiovascular, nervous, endocrine, immune.
- **Connects-to** → [Cardiovascular system](../../07-system/cardiovascular-system/README.md): The pulmonary circuit is the anatomical link: deoxygenated blood from the right heart passes through pulmonary capillaries for gas exchange, then oxygenated blood returns to the left heart for systemic distribution. The two systems share the alveolar-capillary interface and cannot be studied or treated in isolation.
- **Connects-to** → [Asthma](../asthma/README.md): The commonest chronic airway disease of the respiratory system — reversible bronchoconstriction and type-2 inflammation narrow the bronchi, so the conducting airways, not the gas-exchange surface, bear the brunt of asthma.
- **Connects-to** → [COPD](../copd/README.md): The major irreversible obstructive disease of the respiratory system — smoking-driven inflammation destroys alveoli (emphysema) and scars airways (chronic bronchitis), permanently limiting airflow and causing chronic respiratory failure.
- **Connects-to** → [Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md): These cells keep the gas-exchange surface working — secreting surfactant that prevents alveolar collapse and acting as progenitors that regenerate the alveolar lining, so their loss in ARDS and pneumonia drives respiratory failure.
- **Connects-to** → [Oxygen](../../02-atomic/oxygen/README.md): Oxygen is the gas the respiratory system exists to capture: alveoli transfer O2 across the air-blood barrier into hemoglobin for tissue delivery, while CO2 is exhaled—so lung disease that impairs this exchange causes hypoxemia, the central threat in respiratory failure.
- **Connects-to** → [Hemoglobin](../../03-molecular/hemoglobin/README.md): Hemoglobin completes what the respiratory system starts: lungs load O2 onto red-cell hemoglobin, which carries it to tissues and returns CO2 for exhalation—so anemia or abnormal hemoglobin can mimic lung disease by limiting oxygen delivery despite healthy lungs.
- **Connects-to** → [Alveolus](../../05-tissue/alveolus/README.md): The alveolus is the functional unit of the respiratory system: hundreds of millions of these thin-walled sacs create the vast surface where gas exchange occurs, so diseases that flood, collapse, or stiffen alveoli directly cause the hypoxemia of respiratory failure.
- **Connects-to** → [Pulmonary Surfactant](../../03-molecular/surfactant/README.md): Pulmonary surfactant keeps the respiratory system inflatable: secreted by type II pneumocytes, it lowers alveolar surface tension so the lung doesn't collapse on exhalation—its deficiency causes neonatal respiratory distress and contributes to ARDS in adults.
- **Connects-to** → [COVID-19 Disease](../covid-19-disease/README.md): COVID-19 is the respiratory system's defining modern threat: SARS-CoV-2 attacks airway and alveolar cells, and severe disease causes diffuse alveolar damage and hypoxemic respiratory failure—showing how a single virus can overwhelm the gas-exchange apparatus.
- **Connects-to** → [Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md): Pulmonary arterial hypertension is where the respiratory and circulatory systems collide: remodeling of the lung's small arteries raises pulmonary pressure until the right heart fails, so this is a vascular disease that presents as breathlessness.
- **Connects-to** → [Nervous System](../nervous-system/README.md): Breathing is run by the nervous system: brainstem respiratory centers set the rhythm and chemoreceptors sensing CO2 and oxygen adjust it breath by breath, so the respiratory system is only as reliable as the neural drive—lost in opioid overdose or brainstem stroke.
- **Connects-to** → [Carbon](../../02-atomic/carbon/README.md): Respiration exists to trade carbon dioxide for oxygen: cells make CO2, blood carries it as bicarbonate, and the lungs exhale it, so the respiratory system is the body's main route to dump carbon—and CO2 levels set blood pH and the urge to breathe.
- **Connects-to** → [Macrophage](../../04-cellular/macrophage/README.md): Alveolar macrophages guard the respiratory system: stationed in the air sacs, they engulf inhaled microbes and debris as the lung's first cellular defense, so their function (and dysfunction in smoking or COPD) shapes vulnerability to pneumonia.
- **Connects-to** → [Erythrocyte](../../04-cellular/erythrocyte/README.md): Red cells complete the respiratory system's job: the lungs load oxygen onto erythrocyte hemoglobin and unload carbon dioxide, so breathing and the blood's red cells are one continuous gas-exchange system—lung disease and anemia both starve tissues of oxygen.
- **Connects-to** → [Cystic Fibrosis](../cystic-fibrosis/README.md): Cystic fibrosis is the respiratory system's archetypal genetic disease: a chloride-channel defect thickens airway mucus, trapping bacteria and causing the chronic infection and bronchiectasis that destroy the lungs—now transformed by CFTR-modulator drugs.
- **Connects-to** → [Nitric Oxide](../../03-molecular/nitric-oxide/README.md): Nitric oxide fine-tunes the lungs' blood flow: it dilates pulmonary vessels to match perfusion with ventilation, and inhaled NO is used to open lung vessels in pulmonary hypertension and newborn respiratory failure.
- **Connects-to** → [Hydrogen](../../02-atomic/hydrogen/README.md): The respiratory system is the body's fast acid-base dial: by speeding or slowing breathing it controls how much CO2—and thus acid (hydrogen ions)—leaves the blood, so the lungs and kidneys together hold blood pH in its narrow safe range.
- **Connects-to** → [Brain](../../06-organ/brain/README.md): Breathing is commanded by the brain: the brainstem's respiratory centers set the rhythm and adjust it to CO2 and oxygen sensors, so the respiratory system is only as reliable as the neural drive behind it—lost in overdose or stroke.
- **Connects-to** → [Mast Cell](../../04-cellular/mast-cell/README.md): Mast cells make the airways reactive: lining the bronchial walls, they release histamine and other mediators that constrict and inflame airways in asthma and allergy, a key cellular trigger of the wheezing respiratory diseases.
- **Connects-to** → [Nitrogen](../../02-atomic/nitrogen/README.md): Air is mostly nitrogen, and the lungs must reckon with it: this inert gas makes up most of each breath without being used, but under pressure it dissolves into blood and, on fast ascent from diving, bubbles out to cause decompression sickness.
- **Connects-to** → [Neutrophil](../../04-cellular/neutrophil/README.md): Neutrophils both defend and damage the airways: they swarm into infected or inflamed lungs to kill microbes, but in COPD, cystic fibrosis, and ARDS their flood of enzymes also digests lung tissue, driving chronic damage.
- **Connects-to** → [Heart](../../06-organ/heart/README.md): The lungs and right heart are one circuit: the right ventricle pumps all the blood through the lungs for gas exchange, so chronic lung disease that stiffens this circuit overloads and fails the right heart (cor pulmonale).
- **Connects-to** → [Photon](../../01-subatomic/photon/README.md): The lungs are read in X-ray photons: chest radiographs and CT reveal pneumonia, tumors, fibrosis and collapse, the first window into respiratory disease.
- **Connects-to** → [Fibrosis](../../05-tissue/fibrosis/README.md): Scarring stiffens the lungs: pulmonary fibrosis thickens the alveolar walls so oxygen can't cross and the lungs lose their stretch, the end-stage of many chronic lung diseases.
- **Connects-to** → [Kidney](../../06-organ/kidney/README.md): Lungs and kidneys jointly guard blood pH: the lungs blow off acid as CO2 while the kidneys excrete it, so each compensates when the other fails, the core of acid-base balance.
- **Connects-to** → [Electron](../../01-subatomic/electron/README.md): Electron microscopy reveals the gossamer blood-air barrier: alveolar epithelium and capillary endothelium fuse into a membrane thin enough for oxygen to cross, while type II cells store surfactant in lamellar bodies and airway cells wave their cilia.
- **Connects-to** → [Skin](../../06-organ/skin/README.md): The skin betrays failing lungs: when oxygen runs short, deoxygenated hemoglobin turns the lips and fingertips blue in cyanosis, making the skin a visible readout of how well the respiratory system is working.
- **Connects-to** → [Large Intestine](../../06-organ/large-intestine/README.md): The gut and lungs share an immune conversation: through the gut-lung axis, the intestinal microbiome shapes airway immunity, so gut health influences susceptibility to asthma and respiratory infection.
- **Damaged-by** → [Influenza A virus](../../../02-pathogen/01-viruses/influenza-a/README.md): Influenza A is primarily a respiratory pathogen, causing tracheobronchitis, viral pneumonitis, and ARDS; severe disease impairs the system's ventilatory and gas-exchange functions.
- **Treated-by** → [Oseltamivir](../../../03-medicine/01-modern/05-antiviral/oseltamivir/README.md): Reduces influenza A/B symptom duration by ~17 hours (Dobson, Lancet 2015); reduces hospitalization in high-risk patients; must be started within 48h of symptom onset for maximal benefit.
- **Damaged-by** → [Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md): ARDS is the respiratory system's final common failure: diffuse alveolar injury floods the gas-exchange surface with fluid, collapsing oxygenation and forcing the mechanical ventilation that defines critical respiratory illness.
- **Damaged-by** → [Tuberculosis](../tuberculosis/README.md): Tuberculosis is the archetypal chronic lung infection: Mycobacterium tuberculosis cavitates the parenchyma over months and remains among the leading infectious killers worldwide, a defining disease of the respiratory tract.
- **Damaged-by** → [RSV](../rsv/README.md): RSV is the leading cause of infant lower-respiratory infection: it inflames and plugs the small bronchioles, the commonest reason babies are hospitalized for trouble breathing.
- **Connects-to** → [Histamine](../../03-molecular/histamine/README.md): Histamine narrows the airways: released from bronchial mast cells it constricts smooth muscle, swells the mucosa, and floods secretions, the rapid mediator behind allergic wheeze and a driver of airway hyper-reactivity.
- **Connects-to** → [Influenza](../influenza/README.md): Influenza is the recurring epidemic threat to the respiratory system: the virus strips the airway epithelium and can progress to viral pneumonia and ARDS, and its seasonal waves drive much of winter respiratory illness.
- **Connects-to** → [Obesity](../obesity/README.md): Obesity mechanically loads the respiratory system: excess chest and abdominal fat restrict lung expansion and, with upper-airway crowding, cause obstructive sleep apnoea and obesity hypoventilation that blunt ventilation.
- **Connects-to** → [NSCLC](../nsclc/README.md): The respiratory system's commonest fatal cancer: non-small-cell lung cancer arises from the bronchial and alveolar epithelium, the leading cancer killer worldwide and the malignant counterpart to the system's smoking-related diseases.
- **Connects-to** → [Small Cell Lung Cancer](../sclc/README.md): Its most aggressive tumor grows from airway neuroendocrine cells: small-cell lung cancer is a fast, early-metastasizing cancer of the central airways, almost always smoking-related, defining the deadliest end of respiratory malignancy.
- **Connects-to** → [Mesothelioma](../mesothelioma/README.md): Asbestos scars the lining of the lungs into cancer: mesothelioma arises from the pleura that encloses the respiratory system, decades after asbestos exposure, a malignancy of the system's serosal envelope rather than its airways.
- **Connects-to** → [Systemic Sclerosis](../systemic-sclerosis/README.md): Autoimmune fibrosis stiffens the lungs: systemic sclerosis is a leading cause of interstitial lung disease and pulmonary hypertension, scarring the respiratory system into the disorder's commonest cause of death.
- **Connects-to** → [Measles](../measles/README.md): A childhood virus drowns the lungs: measles causes a giant-cell pneumonia that, especially in the malnourished or immunocompromised, is the leading fatal complication of the infection — a viral assault on the respiratory system.
- **Connects-to** → [Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md): Group A strep can ravage the lungs: Streptococcus pyogenes can cause a fulminant necrotizing pneumonia with empyema, a rapidly destructive bacterial infection of the respiratory system often following a viral illness.
- **Connects-to** → [Heart Failure](../heart-failure/README.md): The lungs and right heart share one circuit: chronic lung disease that stiffens the pulmonary vasculature overloads the right ventricle into cor pulmonale, a respiratory route to heart failure.
- **Connects-to** → [Venous Thromboembolism](../venous-thromboembolism/README.md): Its great emergency is a lodged clot: pulmonary embolism, a venous thromboembolism that travels to the lung arteries, abruptly blocks gas exchange and strains the right heart — a leading cause of sudden respiratory collapse.
- **Connects-to** → [Major Depressive Disorder](../major-depressive-disorder/README.md): Chronic breathlessness wears on mood: the activity limitation, fear of suffocation and poor sleep of chronic respiratory disease give conditions like COPD high rates of depression.
- **Connects-to** → [Digestive System](../digestive-system/README.md): They share an origin and a crossroads: lungs and gut both arise from the embryonic foregut and meet at the pharynx, so swallowing disorders cause aspiration and a gut-lung axis links the two.
- **Connects-to** → [Renal System](../renal-system/README.md): Lungs and kidneys jointly balance acid: the respiratory and renal systems co-regulate pH by controlling CO2 and bicarbonate, and pulmonary-renal syndromes like Goodpasture attack both at once.
- **Connects-to** → [Musculoskeletal System](../musculoskeletal-system/README.md): Muscle and rib cage are its pump: the diaphragm and intercostals power ventilation within a bony thorax, so neuromuscular weakness and chest-wall deformity cause restrictive respiratory failure.
- **Connects-to** → [Endocrine System](../endocrine-system/README.md): The lung is also an endocrine organ: its endothelium converts angiotensin I to II via ACE, a key step in blood-pressure control, and pulmonary neuroendocrine cells secrete bioactive peptides.
- **Connects-to** → [Lymphatic System](../lymphatic-system/README.md): It is guarded and drained by lymphatics: bronchus-associated lymphoid tissue defends the airways and a rich lymphatic network clears the lungs, so injury to it causes chylothorax.
- **Connects-to** → [Integumentary System](../integumentary-system/README.md): The skin mirrors the lungs: finger clubbing, central cyanosis and tar staining reveal chronic respiratory disease, and skin and airway share the body's barrier defences against the environment.
- **Connects-to** → [Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md): The lung is its principal home: Mycobacterium tuberculosis is inhaled into the alveoli where it sets up the granulomatous infection that remains the world's leading infectious cause of death.
- **Connects-to** → [SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md): A pandemic virus that targets the airways: SARS-CoV-2 enters through ACE2 on respiratory epithelium, causing pneumonia and diffuse alveolar damage in severe COVID-19.
- **Connects-to** → [Zoonosis](../../../02-pathogen/06-environmental/zoonosis/README.md): Many emerging lung infections jump from animals: avian influenza, SARS, MERS and hantavirus reach the human respiratory tract from animal reservoirs, a recurring source of pandemics.
- **Connects-to** → [Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md): A major cause of pneumonia: Staphylococcus aureus, including MRSA, causes severe necrotising and post-influenza pneumonia and is a leading organism in ventilator-associated lung infection.
- **Connects-to** → [Germinal Center](../../05-tissue/germinal-center/README.md): Mucosal immunity of the airway: bronchus-associated lymphoid tissue forms germinal-centre-like structures in the lung that mature B cells and mount local antibody responses to inhaled pathogens.
- **Connects-to** → [Sepsis](../sepsis/README.md): Pneumonia is the leading source of sepsis: severe respiratory infection and ARDS are the commonest trigger of sepsis, the respiratory tract as the gateway to systemic collapse.
- **Connects-to** → [Erythropoietin](../../03-molecular/erythropoietin/README.md): The lung-kidney oxygen axis: the respiratory system loads oxygen onto haemoglobin, and chronic hypoxic lung disease drives erythropoietin release and secondary polycythaemia.
- **Connects-to** → [ANCA Vasculitis](../anca-vasculitis/README.md): Vasculitis of the airways: ANCA-associated vasculitis (granulomatosis with polyangiitis) attacks the upper and lower respiratory tract, causing sinus destruction, lung nodules and alveolar haemorrhage.
- **Connects-to** → [HIV/AIDS](../hiv-aids/README.md): Immunodeficiency and the lung: HIV/AIDS predisposes to Pneumocystis pneumonia, tuberculosis and other respiratory infections, the lung a frequent battleground of failing immunity.
- **Connects-to** → [Dermatomyositis](../dermatomyositis/README.md): Autoimmune lung scarring: dermatomyositis (notably anti-MDA5) causes a rapidly progressive interstitial lung disease, one of the connective-tissue diseases that fibrose the respiratory system.
- **Connects-to** → [Rheumatoid Arthritis](../rheumatoid-arthritis/README.md): The commonest CTD lung disease: rheumatoid arthritis causes interstitial lung disease, pleuritis, nodules and bronchiectasis, making it the leading connective-tissue cause of chronic lung involvement.
- **Connects-to** → [GVHD](../gvhd/README.md): Bronchiolitis obliterans: chronic lung graft-versus-host disease after stem-cell transplant scars and obliterates the small airways, a major and often irreversible late respiratory complication.
- **Connects-to** → [Marfan Syndrome](../marfan-syndrome/README.md): Spontaneous pneumothorax: connective-tissue disorders such as Marfan form apical lung blebs that rupture, making spontaneous pneumothorax a structural respiratory complication of the syndrome.
- **Connects-to** → [Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md): Nutrition shapes lung defence: vitamin D supports airway immunity, and deficiency is associated with more frequent respiratory infections and worse asthma control.
- **Connects-to** → [ACE Inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md): A heart drug heard in the chest: ACE inhibitors raise bradykinin in the airway, causing the dry cough and rare angioedema that are among the commonest reasons patients stop them.
- **Connects-to** → [Lung Slice](../../05-tissue/lung-slice/README.md): The working tissue of breathing: the lung's conducting airways and alveolar parenchyma — seen on a lung slice — humidify, conduct and exchange air, the tissue-level substrate of every respiratory disease from asthma to fibrosis.
- **Connects-to** → [Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md): Biologics and TKIs target the airway: anti-IL-5/IL-4 monoclonals control severe asthma while EGFR, ALK and checkpoint therapies treat lung cancer — precision drugs reshaping respiratory medicine.
- **Connects-to** → [Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md): It treats and it scars the lung: cytotoxic chemotherapy is central to lung cancer, yet agents like bleomycin and methotrexate cause drug-induced pneumonitis and pulmonary fibrosis, a toxicity unique to the respiratory system.
- **Connects-to** → [IL-6](../../03-molecular/il-6/README.md): Airway inflammation: IL-6 is a central cytokine of respiratory inflammation, elevated in asthma, COPD and the pneumonias and ARDS that injure the lung.
- **Connects-to** → [TNF-α](../../03-molecular/tnf-alpha/README.md): Inflammatory lung injury: TNF-α drives the neutrophilic inflammation of acute lung injury and chronic airway disease, a key mediator of respiratory pathology.
- **Connects-to** → [Dendritic Cell](../../04-cellular/dendritic-cell/README.md): Airway sentinels: dendritic cells lining the airway epithelium sample inhaled antigens and orchestrate the immune responses—protective and allergic—of the respiratory mucosa.
- **Connects-to** → [Angiotensin II](../../03-molecular/angiotensin-ii/README.md): Non-respiratory endocrine role: the pulmonary capillary endothelium is the body's main site of angiotensin-converting enzyme, converting angiotensin I to the vasopressor angiotensin II as blood transits the lung.
- **Connects-to** → [VEGF](../../03-molecular/vegf/README.md): Alveolar-capillary maintenance: VEGF sustains the dense pulmonary capillary network of the gas-exchange surface, and its loss contributes to the alveolar destruction of emphysema.
- **Connects-to** → [TSLP](../../03-molecular/tslp/README.md): Airway alarmin: airway epithelium releases TSLP on injury or allergen exposure, the upstream alarm signal that initiates the type 2 inflammation of asthma and is targeted by tezepelumab.
- **Connects-to** → [Bradykinin](../../03-molecular/bradykinin/README.md): Kinin metabolism: the pulmonary endothelium is the principal site of ACE-mediated bradykinin degradation, so ACE inhibitors raise airway bradykinin and cause the dry cough that is their hallmark side effect.
- **Connects-to** → [Prostaglandins](../../03-molecular/prostaglandins/README.md): Airway and vascular tone: prostaglandins and related eicosanoids set bronchial tone (PGE2 dilating, leukotrienes constricting) and modulate the pulmonary circulation, central mediators of airway physiology and asthma.
- **Connects-to** → [Endothelin-1](../../03-molecular/endothelin-1/README.md): Pulmonary vascular tone: endothelin-1 is the dominant constrictor of the pulmonary circulation and the mediator of hypoxic pulmonary vasoconstriction, the basis for endothelin antagonists in pulmonary hypertension.
- **Connects-to** → [Secretory IgA](../../03-molecular/secretory-iga/README.md): mucosal defense: secretory IgA coating the airway epithelium neutralizes inhaled pathogens at the mucosal surface, the first line of respiratory immune defense that protects the vast air-tissue interface of the lungs from constant microbial exposure.
- **Connects-to** → [EPAS1](../../03-molecular/epas1/README.md): oxygen sensing: HIF-2α (EPAS1) is the master oxygen sensor of the pulmonary circulation and carotid body, driving hypoxic pulmonary vasoconstriction and the ventilatory and erythropoietic responses that adapt the respiratory system to low oxygen.
- **Connects-to** → [Epinephrine](../../03-molecular/epinephrine/README.md): bronchodilation: epinephrine acting on β2-adrenergic receptors relaxes airway smooth muscle to widen the bronchi, the basis of the β2-agonist inhalers that are the mainstay of relieving acute airflow obstruction.
- **Connects-to** → [HIF-1alpha](../../03-molecular/hif-1alpha/README.md): hypoxic response: alongside the HIF-2α/EPAS1 already mapped, HIF-1α mediates the lung's response to low oxygen, including the hypoxic pulmonary vasoconstriction that matches perfusion to ventilation.
- **Connects-to** → [FGFR](../../03-molecular/fgfr/README.md): lung morphogenesis: FGF10-FGFR signaling drives the branching morphogenesis that builds the bronchial tree and alveoli, the core developmental program of the respiratory system.
- **Connects-to** → [NOTCH](../../03-molecular/notch/README.md): airway cell fate: NOTCH signaling specifies the ciliated, club, goblet and neuroendocrine cell fates of the airway epithelium, patterning the conducting airways and their mucociliary defense.
- **Connects-to** → [CFTR](../../03-molecular/cftr/README.md): airway surface liquid: CFTR chloride and bicarbonate transport sets the airway surface liquid that enables mucociliary clearance, the frontline airway defense whose failure defines cystic fibrosis.
- **Connects-to** → [Interleukin-13](../../03-molecular/il-13/README.md): Th2 airway response: IL-13 drives the goblet-cell mucus hypersecretion and bronchial hyperreactivity of the Th2 airway response that underlies asthma and allergic airway disease.
- **Connects-to** → [NRF2](../../03-molecular/nfe2l2/README.md): oxidant defense: NRF2 governs the antioxidant program that protects the airway and alveolar epithelium from inhaled oxidants, pollutants and cigarette smoke at the gas-exchange surface.
- **Connects-to** → [Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md): airway remodeling: TGF-β drives airway remodeling and the fibrotic repair of lung injury, a central effector across chronic respiratory disease.
- **Connects-to** → [NF-κB](../../03-molecular/nf-kb/README.md): inflammation hub: NF-κB is the master transcriptional hub of airway and alveolar inflammation across infection, asthma and COPD.
- **Connects-to** → [AKT](../../03-molecular/akt/README.md): epithelial survival: PI3K-AKT signaling supports alveolar and airway-epithelial survival and the repair responses that maintain the gas-exchange surface.
- **Connects-to** → [Galectin-3](../../03-molecular/galectin-3/README.md): fibro-inflammation: galectin-3 amplifies airway and alveolar inflammation and drives the pulmonary fibrosis shared across chronic lung diseases.
- **Connects-to** → [STAT3](../../03-molecular/stat3/README.md): airway inflammation: IL-6-STAT3 signaling drives the airway inflammation and mucus responses common to inflammatory diseases of the respiratory system.
- **Connects-to** → [cGAS-STING](../../03-molecular/cgas-sting/README.md): pulmonary DNA sensing: cGAS-STING sensing of viral and damage-associated cytosolic DNA shapes the antiviral and inflammatory responses of the respiratory epithelium.
- **Connects-to** → [FOXO](../../03-molecular/foxo/README.md): epithelial stress defense: FOXO transcription factors regulate the airway epithelial oxidative-stress defense and immune-metabolic balance across respiratory disorders.
- **Connects-to** → [STAT1](../../03-molecular/stat1/README.md): antiviral airway response: IFN-STAT1 signaling shapes the antiviral and inflammatory responses of the airway epithelium across the respiratory system.
- **Connects-to** → [ERK1/2](../../03-molecular/erk1-2/README.md): epithelial repair: ERK-MAPK signaling downstream of growth factors (FGFR already mapped) drives airway epithelial proliferation, repair, and remodeling in the respiratory system.
- **Connects-to** → [GSK-3β](../../03-molecular/gsk-3b/README.md): airway inflammation: GSK-3β modulates the airway inflammatory and epithelial-repair signaling of the respiratory system.
- **Connects-to** → [PIK3CA](../../03-molecular/pik3ca/README.md): epithelial growth and immunity: PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the airway epithelial proliferation, survival, and immune responses of the respiratory system.
- **Connects-to** → [S100A8/A9](../../03-molecular/s100a8-a9/README.md): innate airway inflammation: S100A8/A9 alarmins participate in the innate inflammatory signaling of the airway and alveolar responses of the respiratory system.
- **Connects-to** → [AMPK](../../03-molecular/ampk/README.md): airway energy homeostasis: AMPK-linked metabolic signaling participates in the airway epithelial and alveolar energy homeostasis of the respiratory system.
- **Connects-to** → [Autophagy](../../03-molecular/autophagy/README.md): epithelial homeostasis and defense: Autophagy maintains the airway epithelial and alveolar-macrophage homeostasis and host defense of the respiratory system.
- **Connects-to** → [mTOR](../../03-molecular/mtor/README.md): growth and surfactant metabolism: mTOR signaling coordinates the growth, surfactant metabolism, and immune responses of the respiratory system.
- **Connects-to** → [DNMT3A](../../03-molecular/dnmt3a/README.md): epigenetic regulation: DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the airway epithelial and immune gene programs of the respiratory system.
- **Connects-to** → [CCR5](../../03-molecular/ccr5/README.md): airway immune recruitment: CCR5-driven leukocyte recruitment participates in the airway immune surveillance and inflammatory responses of the respiratory system.
- **Connects-to** → [SRC Kinase](../../03-molecular/src-kinase/README.md): epithelial junctions: SRC-family kinase signaling participates in the airway epithelial junction dynamics and growth-factor responses of the respiratory system.
- **Connects-to** → [CXCL12](../../03-molecular/cxcl12/README.md): immune trafficking: CXCL12-CXCR4 signaling participates in the airway immune-cell trafficking and repair of the respiratory system.
- **Connects-to** → [IL-1β](../../03-molecular/il-1b/README.md): airway inflammation: IL-1β-driven inflammation participates in the airway inflammatory responses of the respiratory system.
- **Connects-to** → [IL-33](../../03-molecular/il-33/README.md): epithelial alarmin: IL-33 alarmin signaling participates in the airway epithelial and innate immune responses of the respiratory system.
- **Connects-to** → [Proton](../../01-subatomic/proton/README.md): acid-base and drive: the lungs set systemic pH by adjusting carbon-dioxide excretion, and central and peripheral chemoreceptors sensing protons and CO2 tune the ventilatory drive minute to minute.
- **Connects-to** → [Calcium](../../02-atomic/calcium/README.md): airway smooth muscle: calcium-dependent contraction of airway smooth muscle sets bronchomotor tone, the target of the bronchodilators and bronchoconstrictors that widen or narrow the conducting airways.
- **Connects-to** → [Magnesium](../../02-atomic/magnesium/README.md): bronchodilation and muscle: magnesium relaxes airway smooth muscle by antagonising calcium entry, the basis of intravenous magnesium in severe bronchospasm, and is required for normal respiratory-muscle function.
- **Connects-to** → [Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md): central respiratory drive: opioids acting on mu-opioid receptors in the brainstem (brain already mapped) suppress the respiratory rhythm, the mechanism of opioid respiratory depression that makes the respiratory system uniquely vulnerable to these drugs.
- **Connects-to** → [Serotonin](../../03-molecular/serotonin/README.md): chemoreception and pulmonary tone: serotonergic medullary neurons contribute to central CO2 chemoreception and breathing control, while serotonin also constricts the pulmonary vasculature, linking the transmitter to both ventilation and lung perfusion.
- **Connects-to** → [Leptin](../../03-molecular/leptin/README.md): ventilatory drive: leptin stimulates central respiratory drive, and leptin resistance in obesity contributes to obesity hypoventilation syndrome, connecting the adipokine to the neural control of breathing.
- **Connects-to** → [CGRP](../../03-molecular/cgrp/README.md): neurogenic airway control: CGRP released from airway sensory nerves contributes to the neurogenic inflammation, vasodilation and cough reflex of the respiratory system, part of the neuro-immune regulation of the airways.
- **Connects-to** → [Substance P](../../03-molecular/substance-p/README.md): cough and neurogenic reflex: substance P from airway sensory nerves, with CGRP (already mapped), mediates the cough reflex and the neurogenic inflammation and bronchoconstriction of the respiratory tract.
- **Connects-to** → [Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md): oxidative lung injury: xanthine-oxidase-derived reactive oxygen species contribute to the oxidative stress of respiratory disease (NRF2 already mapped), driving the epithelial injury and inflammation of the airways and alveoli.
- **Connects-to** → [Chloride](../../02-atomic/chloride/README.md): airway surface liquid: chloride secretion through the CFTR channel (already mapped) hydrates the airway surface liquid and mucus, and its failure causes the thick secretions of cystic fibrosis that obstruct the respiratory tract.
- **Connects-to** → [Smooth muscle cell](../../04-cellular/smooth-muscle-cell/README.md): airway calibre: the airway smooth muscle sets the bronchial calibre, contracting to acetylcholine and relaxing to adrenaline (already mapped), and its constriction and remodelling underlie the airflow limitation of respiratory disease.
- **Connects-to** → [Nervous system](../nervous-system/README.md): neural control of breathing: the nervous system's brainstem respiratory centres and the chemoreceptors sense oxygen and carbon dioxide (already mapped) to drive ventilation, and the sensory nerves (CGRP and substance P already mapped) mediate cough and airway reflexes.
- **Connects-to** → [IL-4](../../03-molecular/il-4/README.md): type-2 airway immunity: IL-4, with IL-13 (already mapped), drives the type-2 immunity of the airways of the respiratory system, the allergic and mucus-hypersecretory response of asthma and allergic disease.
- **Connects-to** → [IL-5](../../03-molecular/il-5/README.md): eosinophilic inflammation: IL-5 recruits the eosinophils of the eosinophilic airway inflammation of the respiratory system, the target of the anti-IL-5 biologics in severe asthma.
- **Connects-to** → [IL-17a](../../03-molecular/il-17a/README.md): neutrophilic airway inflammation: IL-17 drives the neutrophilic, non-type-2 airway inflammation of the respiratory system, part of the severe steroid-resistant asthma and the infective and COPD neutrophilia.
- **Connects-to** → [Adiponectin](../../03-molecular/adiponectin/README.md): respiratory-metabolic adipokine: adiponectin, with leptin (already mapped), is the adipokine of the respiratory-metabolic crosstalk; the obesity affects the ventilation and the airway inflammation of the respiratory system.
- **Connects-to** → [Resistin](../../03-molecular/resistin/README.md): airway-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose to the airway inflammation and the obesity-related respiratory dysfunction.
- **Connects-to** → [Type I interferon](../../03-molecular/type-i-interferon/README.md): antiviral airway interferon: the airway epithelium's type-I interferon (with the secretory-IgA already mapped) defends the respiratory system against the inhaled respiratory viruses.
- **Connects-to** → [IFN-gamma](../../03-molecular/ifn-gamma/README.md): Th1 airway immunity: the IFN-γ of the airway T cells is the type-II interferon arm of the Th1 antiviral and antimycobacterial immunity of the respiratory system.
- **Connects-to** → [IL-12](../../03-molecular/il-12/README.md): Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the airway immunity, counter-balancing the type-2 (IL-4, IL-5 and IL-13 already mapped) allergic response of the respiratory system.
- **Connects-to** → [IL-23](../../03-molecular/il-23/README.md): Th17 airway axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neutrophilic airway inflammation of the respiratory system.
- **Connects-to** → [IgE](../../03-molecular/ige/README.md): Allergic airway arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), arms the mast cells (already mapped) of the allergic airway (rhinitis/asthma) response of the respiratory system.
- **Connects-to** → [IL-10](../../03-molecular/il-10/README.md): Airway tolerance: IL-10 is the regulatory cytokine that maintains the mucosal tolerance and resolves the airway inflammation of the respiratory system.
- **Connects-to** → [T-helper cell](../../04-cellular/t-helper-cell/README.md): CD4 airway helper: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines coordinating the mucosal immunity of the respiratory system.
- **Connects-to** → [Periostin](../../03-molecular/periostin/README.md): type-2 remodelling: periostin, downstream of the IL-13 (already mapped) signalling, is a matricellular marker and mediator of the type-2 airway remodelling and the subepithelial fibrosis of the respiratory system.
- **Connects-to** → [IL-31](../../03-molecular/il-31/README.md): airway itch/cough: IL-31, a type-2 (IL-4, IL-5 and IL-13 already mapped) cytokine, is part of the neuroimmune signalling of the cough and airway sensory dimension of the respiratory system.
- **Connects-to** → [Complement C3](../../03-molecular/complement-c3/README.md): airway complement: the complement C3, produced locally by the airway epithelium, is part of the innate mucosal defence and, when dysregulated, the inflammation of the respiratory system.
- **Connects-to** → [Complement C5](../../03-molecular/complement-c5/README.md): terminal complement: the complement C5 and its C5a (with C3 already mapped) generate the anaphylatoxin and membrane-attack complex of the acute lung injury and the airway inflammation of the respiratory system.
- **Connects-to** → [C5aR1](../../03-molecular/c5ar1/README.md): C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil recruitment into the airway and alveolus in the immunopathology of the respiratory system.
- **Connects-to** → [Factor H](../../03-molecular/factor-h/README.md): complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) on the airway surface, restraining the complement attack on the host lung of the respiratory system.
- **Connects-to** → [C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md): Airway kinin brake: C1-esterase inhibitor, by controlling the contact-pathway kinin cascade (bradykinin already mapped) and the classical complement, moderates the airway oedema, the bronchospasm, and the hereditary angioedema exacerbations of the respiratory system.
- **Connects-to** → [Melatonin](../../03-molecular/melatonin/README.md): Antioxidant-airway axis: melatonin, from the pineal (already mapped) and local bronchial epithelium, exerts antioxidant and anti-inflammatory effects on the airway, modulating the nocturnal bronchoconstriction and the ROS-driven mucosal injury of the respiratory system.
- **Connects-to** → [Prolactin](../../03-molecular/prolactin/README.md): Mucosal immunity: prolactin, from the pituitary (already mapped) and local airway epithelium, modulates the respiratory mucosal IgA (already mapped) secretion and the mast-cell (already mapped) responsiveness of the immune surveillance of the respiratory system.
- **Connects-to** → [Testosterone](../../03-molecular/testosterone/README.md): Sex-hormone lung axis: testosterone modulates the alveolar and bronchial epithelial response; sex-based differences in respiratory mechanics, asthma (already mapped) severity, and COPD (already mapped) outcomes are in part mediated by androgen-testosterone-immune interactions.
- **Connects-to** → [Transferrin](../../03-molecular/transferrin/README.md): Iron-lung metabolism: transferrin, the iron carrier, reflects the iron handling that governs the alveolar macrophage (already mapped) function and the mucociliary defence; iron overload and deficiency each impair the respiratory-epithelial barrier and innate immunity.
- **Connects-to** → [Selenium](../../02-atomic/selenium/README.md): Antioxidant micronutrient: selenium, via selenoproteins in the lung-epithelium (already mapped), protects against ROS-driven alveolar injury and modulates the type-2 and type-1 airway-immune balance of the respiratory system (asthma, COPD already mapped).
- **Connects-to** → [Oxytocin](../../03-molecular/oxytocin/README.md): Airway-immune neuropeptide: oxytocin, via OXTR on mast cells (already mapped) and smooth-muscle cells (already mapped), attenuates airway inflammation; oxytocin modulates the IL-5 (already mapped) and IL-13 (already mapped) type-2 airway response of the respiratory system.
- **Connects-to** → [Vasopressin](../../03-molecular/vasopressin/README.md): Vasomotor-airway axis: vasopressin, via V1aR on smooth-muscle cells (already mapped) and endothelial cells, modulates pulmonary vascular tone; vasopressin dysregulation amplifies the pulmonary arterial hypertension (already mapped) of the respiratory system.
- **Connects-to** → [Iodine](../../02-atomic/iodine/README.md): Thyroid-respiratory axis: iodine-dependent thyroid hormones modulate mucociliary clearance and alveolar (already mapped) surfactant (already mapped) production; iodine deficiency impairs the respiratory-epithelial defence and the macrophage (already mapped) innate immunity.
- **Connects-to** → [Sodium](../../02-atomic/sodium/README.md): ENaC-airway homeostasis: sodium, via ENaC-driven airway-surface liquid homeostasis in lung-epithelium (already mapped), maintains mucociliary clearance; sodium dysregulation amplifies the IL-6 (already mapped) and neutrophil (already mapped) inflammatory cascade of the respiratory system.
- **Connects-to** → [Copper](../../02-atomic/copper/README.md): Mitochondrial-innate immunity: copper, as cofactor of cytochrome-c oxidase in type-II pneumocytes (already mapped) and macrophages (already mapped), supports oxidative phosphorylation and innate immunity; copper deficiency impairs the antioxidant and phagocytic defences of the respiratory system.
- **Connects-to** → [Potassium](../../02-atomic/potassium/README.md): Airway-tone excitability: potassium, via K⁺ channels on airway smooth-muscle cells (already mapped) and type-II pneumocytes (already mapped), sets airway tone and epithelial secretion; potassium dysregulation amplifies the bronchoconstriction and IL-6 (already mapped) cascade of the respiratory system.
- **Connects-to** → [Zinc](../../02-atomic/zinc/README.md): Mucosal-innate immunity: zinc, as metalloproteinase cofactor in macrophages (already mapped) and neutrophils (already mapped), maintains innate immunity; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of the respiratory system.
- **Connects-to** → [Iron](../../02-atomic/iron/README.md): Oxygen-transport immunity: iron, as haem cofactor in erythrocytes (already mapped) and macrophages (already mapped), enables oxygen transport; iron deficiency impairs the NF-κB (already mapped) anti-microbial response and amplifies the IL-6 (already mapped) cascade of the respiratory system.
- **Connects-to** → [Phosphorus](../../02-atomic/phosphorus/README.md): Surfactant-ATP: phosphorus, as ATP precursor in type-II pneumocytes (already mapped) and macrophages (already mapped), supports surfactant synthesis and innate immunity; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of the respiratory system.
- **Connects-to** → [Sulfur](../../02-atomic/sulfur/README.md): Respiratory sulfur: H2S from sulfur-amino acids in type-II pneumocytes (already mapped) and endothelial cells (already mapped) promotes airway vasodilation; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of the respiratory system.
- **Connects-to** → [PD-1](../../03-molecular/pd-1/README.md): Respiratory PD-1: PD-1 checkpoint on macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates airway immune surveillance; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) airway inflammatory cascade of the respiratory system.
- **Connects-to** → [GLP-1](../../03-molecular/glp-1/README.md): Respiratory GLP-1: GLP-1 signalling in type-II pneumocytes (already mapped) and endothelial cells (already mapped) modulates airway metabolic homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of the respiratory system.
- **Connects-to** → [Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md): Respiratory Wnt/β-catenin: Wnt/β-catenin signalling supports type-II pneumocyte (already mapped) repair and airway epithelial regeneration; Wnt dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrotic cascade of the respiratory system.
- **Connects-to** → [RANKL](../../03-molecular/rankl/README.md): Respiratory RANKL: RANKL signalling in macrophages (already mapped) and type-II pneumocytes (already mapped) regulates bone-airway mineral crosstalk; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of the respiratory system.
- **Connects-to** → [SMAD4](../../03-molecular/smad4/README.md): Respiratory SMAD4: SMAD4-mediated TGF-β (already mapped) signalling in type-II pneumocytes (already mapped) and fibroblasts (already mapped) drives airway fibrosis; SMAD4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of the respiratory system.
- **Connects-to** → [IL-2](../../03-molecular/il-2/README.md): Respiratory IL-2: IL-2 expands T-cytotoxic cells (already mapped) and regulatory T-cells in airway immune surveillance; IL-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of the respiratory system.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — RS fibronectin: fibronectin in airway matrix and bronchial epithelial cells modulates lung structural repair; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) remodelling cascade of the respiratory system.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — RS IGF-1: IGF-1 from bronchial epithelium (already mapped) and lung macrophages (already mapped) sustains lung growth and repair; IGF-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — RS activin-A: activin-A from lung fibroblasts (already mapped) and macrophages (already mapped) modulates inflammation and fibrosis; activin-A excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) fibrotic cascade of the respiratory system.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Resp calcitonin: calcitonin from lung cells (already mapped) and macrophages (already mapped) modulates respiratory calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — Resp insulin-receptor: insulin receptor on lung cells (already mapped) and macrophages (already mapped) drives metabolic tone; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) respiratory fibrotic cascade.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Resp aldosterone: aldosterone from macrophages (already mapped) and lung fibroblasts (already mapped) modulates respiratory fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — Resp androgen-receptor: androgen receptor on lung cells (already mapped) and macrophages (already mapped) modulates respiratory sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Resp norepinephrine: norepinephrine from sympathetic nerves (already mapped) and macrophages (already mapped) modulates bronchomotor tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Resp adrenomedullin: adrenomedullin from lung cells (already mapped) and macrophages (already mapped) modulates pulmonary vasodilation; adrenomedullin loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Resp bdnf: BDNF from lung cells (already mapped) and macrophages (already mapped) supports airway neural trophic tone; bdnf loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Resp osteopontin: osteopontin from lung cells (already mapped) and macrophages (already mapped) promotes airway ECM remodelling; osteopontin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Resp angiopoietin: angiopoietin from lung cells (already mapped) and macrophages (already mapped) drives pulmonary angiogenesis; angiopoietin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — Resp renin: renin from lung cells (already mapped) and macrophages (already mapped) modulates pulmonary RAAS balance; renin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Myostatin](../../03-molecular/myostatin/README.md)** — Resp myostatin: myostatin from lung cells (already mapped) and macrophages (already mapped) modulates airway fibrotic tone; myostatin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[ACE2](../../03-molecular/ace2/README.md)** — Resp ace2: ACE2 on lung cells (already mapped) and macrophages (already mapped) modulates airway RAAS tone; ace2 loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Resp cortisol: cortisol from macrophages (already mapped) and lung cells (already mapped) modulates airway stress response; cortisol excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Resp ghrelin: ghrelin from macrophages (already mapped) and lung cells (already mapped) modulates airway metabolic signalling; ghrelin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Resp glucagon: glucagon from macrophages (already mapped) and lung cells (already mapped) modulates airway glucose metabolism; glucagon excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of the respiratory system.
- `prevented-by` → **[PCV13 (Prevnar 13)](../../../../04-vaccine/08-conjugate/pcv13/README.md)** — CAPiTA RCT (N=84,496 adults ≥65): PCV13 achieved 45.6% VE against vaccine-type CAP and 75% VE against invasive pneumococcal disease; prevents pneumococcal pneumonia, the leading infectious cause of respiratory hospitalisation in older adults.

## Pathology

| Disease | Mechanism | Physiological signature |
|:---|:---|:---|
| **COPD** | Smoke-induced airway inflammation, emphysema, mucus hypersecretion | Obstruction (FEV₁/FVC <0.7), air trapping, ↑RV, ↓DLCO |
| **Asthma** | Eosinophilic airway inflammation, smooth-muscle hyper-reactivity, mucus plugging | Reversible obstruction; ↑ variability in peak flow |
| **Pulmonary fibrosis** | Alveolar injury → fibroblast activation → fibrosis | Restriction (↓TLC, ↓FVC), ↓DLCO, progressive hypoxaemia |
| **Pulmonary embolism** | Thrombus in pulmonary arteries → V̇/Q̇ mismatch, dead space increase, ↑RV afterload | Acute dyspnoea, hypoxaemia, tachycardia, possible shock |
| **ARDS** | Diffuse alveolar damage → bilateral alveolar flooding → severe hypoxaemia | PaO₂/FiO₂ <300 (mild), <200 (moderate), <100 (severe); ↓compliance |
| **Obstructive sleep apnoea** | Upper airway collapse during sleep → repetitive hypoxia, hypercapnia, arousal | Daytime somnolence, cardiovascular sequelae (hypertension, AF, heart failure) |
| **Lung cancer** | Malignant transformation of bronchial/alveolar epithelium | Cough, haemoptysis, dyspnoea; systemic effects via metastases and paraneoplastic syndromes |

## See Also

- [Lung](../../06-organ/lung/README.md) — the gas-exchange organ.
- [Alveolus](../../05-tissue/alveolus/README.md) — the functional unit of gas exchange.
- [Cardiovascular system](../../07-system/cardiovascular-system/README.md) — the linked circulation system.
- [Human body](../../08-whole-body/human-body/README.md) — the whole-body scale.

[^west-respiratory-physiology]: West JB, Luks AM. *West's Respiratory Physiology: The Essentials.* 10th ed. Wolters Kluwer; 2016. [lww.com/Product/9781496310118](https://www.lww.com/Product/9781496310118)
[^weibel-2017-alveolar-dimensions]: Weibel ER. Lung morphometry: the link between structure and function. *Cell Tissue Res.* 2017;367(3):413-26. [doi:10.1007/s00441-016-2541-4](https://doi.org/10.1007/s00441-016-2541-4) · [PubMed 27981371](https://pubmed.ncbi.nlm.nih.gov/27981371/)
[^openstax-anatomy-ch22]: OpenStax. *Anatomy & Physiology 2e*, Ch. 22: The Respiratory System. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/22-introduction)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
