---
schema: human-scale-entry/v1
id: copd
name: COPD
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic obstructive pulmonary disease from cigarette smoke-induced alveolar destruction (emphysema) and airway remodeling; FEV1/FVC <0.7 defines obstruction. Bronchodilators (LABA/LAMA) are first-line; inhaled corticosteroids reduce exacerbations in eosinophilic COPD."
aliases: ["chronic obstructive pulmonary disease", "emphysema", "chronic bronchitis", "COPD-asthma overlap", "ACO"]
sources:
  - id: rabe-2017-gold-copd
    type: peer-reviewed
    cite: "Rabe KF, Watz H. Chronic obstructive pulmonary disease. Lancet. 2017;389(10082):1931-1940."
    doi: "10.1016/S0140-6736(17)31222-9"
    pmid: "28513453"
    url: "https://doi.org/10.1016/S0140-6736(17)31222-9"
  - id: vestbo-2013-gold-strategy
    type: peer-reviewed
    cite: "Vestbo J, Hurd SS, Agustí AG, et al. Global strategy for the diagnosis, management, and prevention of chronic obstructive pulmonary disease: GOLD executive summary. Am J Respir Crit Care Med. 2013;187(4):347-365."
    doi: "10.1164/rccm.201204-0596PP"
    pmid: "22878278"
    url: "https://doi.org/10.1164/rccm.201204-0596PP"
  - id: jones-2017-dupilumab-copd
    type: peer-reviewed
    cite: "Bhatt SP, Rabe KF, Hanania NA, et al. Dupilumab for COPD with Type 2 Inflammation Indicated by Eosinophil Counts. N Engl J Med. 2023;389(3):205-214."
    doi: "10.1056/NEJMoa2303966"
    pmid: "37272521"
    url: "https://doi.org/10.1056/NEJMoa2303966"
cross_links:
  - target: 01-human/07-system/respiratory-system
    relation: targets
    note: "COPD irreversibly destroys the respiratory system: emphysema enlarges and ruptures alveolar walls → reduced gas exchange surface; airway remodeling (smooth muscle hypertrophy, mucous gland hyperplasia) → chronic airflow obstruction; both processes are largely irreversible."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta1 mediates small airway fibrosis and remodeling in COPD; cigarette smoke-activated macrophages produce TGF-beta → subepithelial fibrosis → airway wall thickening → fixed obstruction; TGF-beta also impairs alveolar repair after smoke-induced damage."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Alveolar macrophages are central COPD effectors; cigarette smoke activates macrophages → MMP-9/12 secretion → elastin and collagen degradation → emphysema; COPD macrophages are also defective at clearing bacteria and apoptotic cells → susceptibility to exacerbations."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils accumulate in COPD airways (especially during exacerbations); neutrophil elastase degrades alpha-1 antitrypsin and lung matrix; NETosis releases DNA and proteases; IL-8 drives neutrophil recruitment; neutrophilic COPD does not respond to inhaled corticosteroids."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "COPD destroys lung architecture: emphysema ruptures alveolar walls → reduced gas exchange; chronic bronchitis remodels small airways → fixed obstruction; both largely irreversible; GOLD staging (FEV1/FVC <0.7, GOLD 1-4) guides risk stratification and treatment selection."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "COPD-asthma overlap (ACO) affects ~10-15% of COPD patients: combined fixed obstruction (COPD) and eosinophilia/reversibility (asthma); ACO has more frequent exacerbations; dupilumab approved for COPD with eosinophilia ≥300/µL (NOTUS/BOREAS trials: 30% exacerbation reduction)."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β is a key COPD exacerbation amplifier: NLRP3 inflammasome activation by smoke → IL-1β release → neutrophil and macrophage recruitment → airway inflammation; IL-1β promotes goblet cell hyperplasia → mucus hypersecretion; canakinumab (IL-1β mAb) studied in COPD."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "COPD and cystic fibrosis are chronic obstructive airway diseases: COPD is acquired emphysema from decades of cigarette smoke, while CF is inherited CFTR failure causing childhood bronchiectasis — yet both end in neutrophilic airway destruction and respiratory failure."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Severe COPD strains the right heart: chronic hypoxia drives pulmonary vasoconstriction and arteriolar remodeling → pulmonary hypertension (WHO Group 3) → right ventricular hypertrophy and failure (cor pulmonale), with raised JVP and peripheral edema."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Bacterial infection — often Streptococcus pneumoniae, Haemophilus influenzae, or Moraxella — drives roughly a quarter of COPD exacerbations; purulent sputum guides antibiotics, and pneumococcal vaccination is recommended to help prevent them."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "COPD and lung cancer are smoking's twin diseases that frequently coexist: shared tobacco-driven inflammation, oxidative stress and impaired DNA repair mean COPD independently raises NSCLC risk, COPD limits surgery, and both are screened together with low-dose CT in heavy smokers."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "RSV is an underappreciated driver of COPD exacerbations: it infects airway epithelium to provoke neutrophilic inflammation and bronchospasm, accounting for a notable share of hospitalized flares in older adults; new adult RSV vaccines (Arexvy, Abrysvo) help reduce this burden."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Cigarette smoke is the dominant cause of COPD: inhaled carbon-rich particulates and combustion chemicals trigger protease-antiprotease imbalance and chronic neutrophilic inflammation → emphysema and small-airway fibrosis; cessation is the only intervention that slows decline."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "COPD is a leading cause of pulmonary hypertension and cor pulmonale: chronic hypoxia constricts and remodels pulmonary arteries, raising right-heart pressure until the right ventricle fails—so a loud P2, edema, and a dilated right heart signal this grave complication."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Respiratory viruses like influenza are major triggers of COPD exacerbations: infection inflames already-damaged airways, causing the acute worsening of breathlessness and sputum that drives hospitalization—so annual flu vaccination is core to COPD care."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Osteoporosis is a frequent, underrecognized COPD comorbidity: inflammation, inactivity, low vitamin D, smoking, and corticosteroids thin the bones, so COPD patients fracture more—and vertebral fractures further impair breathing, warranting bone-density screening."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "COPD destroys the alveolus in emphysema: protease-driven breakdown of alveolar walls merges the tiny gas-exchange sacs into large, inelastic spaces, slashing surface area and trapping air—so the lung loses both the recoil to exhale and the surface to oxygenate."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "Type II pneumocytes are injured and overwhelmed in COPD: chronic smoke exposure damages these surfactant-producing, alveolus-repairing cells, impairing their regeneration of the destroyed alveolar lining—so failed epithelial repair contributes to progressive emphysema."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "COPD ultimately fails at delivering oxygen: airway obstruction and alveolar destruction cause hypoxemia and CO2 retention, which is why advanced COPD needs supplemental oxygen—the one therapy, with smoking cessation, shown to prolong survival in hypoxemic patients."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Airway smooth muscle drives the obstruction in COPD: chronic inflammation thickens and tightens bronchiolar smooth muscle, and bronchodilators that relax it are the mainstay of symptom control—targeting the reversible component of fixed airflow limitation."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "COPD and cardiovascular disease are deeply linked: shared smoking and systemic inflammation raise heart-attack and arrhythmia risk, and chronic hypoxia strains the right heart toward cor pulmonale—so cardiovascular disease is a leading cause of death in COPD."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "COPD and depression commonly coexist: breathlessness, disability and chronic hypoxia foster depression and anxiety in a large share of patients, which in turn worsen adherence and outcomes—so mental health is integral to comprehensive COPD care."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "COPD scars the small airways: chronic inflammation drives peribronchiolar fibrosis that narrows and obliterates terminal bronchioles, so airway fibrosis—alongside alveolar destruction in emphysema—causes the fixed airflow obstruction that defines COPD."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "COPD is linked to the gut-lung axis: altered gut and airway microbiomes shape lung inflammation and exacerbations, so the microbiome is emerging as a factor in disease course beyond the cigarette smoke that starts it."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "COPD and anxiety feed each other: breathlessness provokes fear, and anxiety worsens the sensation of dyspnea and triggers panic, so anxiety disorders are common and undertreated and worsen quality of life and exacerbation risk."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D deficiency worsens COPD: low levels are common in these patients and track with more frequent exacerbations and faster bone loss, so supplementing deficient patients can cut flare-ups and protect against the osteoporosis COPD brings."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Chronic low oxygen in COPD drives erythropoietin: persistent hypoxia signals the kidney to make more EPO, thickening the blood with extra red cells (secondary polycythemia) that strains the heart already burdened by lung disease."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Exhaled nitric oxide helps tell COPD from asthma: FeNO rises with the eosinophilic airway inflammation of asthma but stays low in typical neutrophilic COPD, so the gas is a breath biomarker guiding who will respond to inhaled steroids."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "COPD throws off acid-base balance by trapping CO2: failing lungs cannot exhale carbon dioxide, which becomes carbonic acid and raises blood hydrogen ions, producing the respiratory acidosis that marks advanced disease and flares."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "COPD remodels the small airways with collagen: TGF-beta-driven fibroblasts lay down collagen around the bronchioles, narrowing and stiffening them, so airway fibrosis—not just alveolar loss—drives the irreversible airflow limitation."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells help destroy the COPD lung: CD8 T cells accumulate in the airways and alveoli, and their killing of lung cells correlates with the emphysema and airflow limitation, adding adaptive immunity to the neutrophil-macrophage attack."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Severe COPD can cloud the brain: as failing lungs retain carbon dioxide and drop oxygen, the rising CO2 causes confusion and drowsiness (CO2 narcosis), a danger during exacerbations and with over-oxygenation."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "COPD scars its small airways through fibroblasts: TGF-β activates these cells to lay down collagen around the bronchioles, narrowing and stiffening them in the airway remodeling that fixes the airflow limitation."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "COPD is a body-wide inflammatory state driven by TNF-α: spilling from the inflamed lungs, this cytokine drives the muscle wasting and weight loss (cachexia) that worsen prognosis beyond the airways."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "COPD is imaged in X-ray photons: chest films show hyperinflated lungs and flattened diaphragms, and CT quantifies the emphysema, mapping where lung tissue has been destroyed."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "COPD damages the lung's vessels: hypoxia and inflammation injure endothelial cells, remodeling the pulmonary arteries into the pulmonary hypertension and cor pulmonale of advanced disease."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Chronic low oxygen in COPD drives the marrow: rising erythropoietin spurs it to overproduce red cells, the secondary polycythemia that thickens the blood of long-standing hypoxic patients."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows emphysema's ruin up close: the delicate alveolar walls dissolve as enzymes outpace their inhibitors, merging the fine air sacs into floppy enlarged spaces that collapse on exhaling and trap stale air."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "COPD shows on the surface: deoxygenated blood turns the lips and nails blue with cyanosis, fingertips club from chronic hypoxia, and the ruddy plethora of secondary polycythemia colors the 'blue bloater' face."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Failing lungs strain the kidney: chronic low oxygen and high carbon dioxide, plus the back-pressure of cor pulmonale, impair renal blood flow, so fluid retention and kidney dysfunction track with advanced COPD."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Chronic low oxygen thickens the blood: COPD's persistent hypoxia drives erythropoietin and a secondary polycythemia, raising the red-cell mass and viscosity — though systemic inflammation can also leave some patients anemic instead."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "COPD wastes the muscles it depends on: systemic inflammation, inactivity, and steroids drive a peripheral muscle dysfunction and cachexia that limit exercise and predict mortality, which pulmonary rehabilitation works to reverse."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "One inherited defect links lung and liver: alpha-1 antitrypsin deficiency leaves the lung's elastin unprotected (early emphysema) while the misfolded protein jams up hepatocytes, causing cirrhosis — COPD and liver disease from a single gene."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "COPD strains the right heart: chronic hypoxia constricts the lung's vessels, and the back-pressure of pulmonary hypertension overworks the right ventricle into cor pulmonale — right heart failure with leg swelling and congestion that worsens prognosis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "COPD lowers testosterone: chronic hypoxia, systemic inflammation and corticosteroid use suppress the gonadal axis, and the resulting low testosterone deepens the muscle wasting and fatigue, sometimes prompting replacement in selected men."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Wasting away marks severe COPD: the high work of breathing and systemic inflammation burn through fat and lean tissue, and the loss of adipocyte mass — a low BMI and fat-free mass — is a strong independent predictor of death in the disease."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T cells, not just neutrophils, scar the airway: CD4 Th1 and Th17 cells accumulate in the COPD lung and sustain the chronic inflammation, an adaptive arm that makes the disease partly autoimmune in flavor."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "COPD is hard on the arteries too: shared smoking plus the disease's systemic inflammation accelerate atherosclerosis, so cardiovascular disease — not respiratory failure — is a leading cause of death in milder COPD."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 carries the inflammation body-wide: spilling from the inflamed lung into the blood, it drives the muscle wasting, weakness, and comorbidity of COPD and rises sharply during exacerbations."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Chronic hypoxia switches on HIF-1α: low alveolar oxygen in advanced COPD stabilizes this transcription factor, driving the erythropoietin-fueled secondary polycythemia and the pulmonary-vascular remodeling that ends in cor pulmonale."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Damaged airways invite Aspergillus: structurally altered COPD lungs and inhaled-steroid use foster Aspergillus colonization, sensitization, and occasionally chronic or invasive pulmonary aspergillosis that worsens the disease."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Exacerbations carry hidden clots: COPD raises the risk of pulmonary embolism, and a PE can both mimic and precipitate an exacerbation, so unexplained worsening prompts a search for venous thromboembolism."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Cigarette smoke throws the airway's inflammation switch: oxidants and irritants activate NF-κB in bronchial epithelium and macrophages, driving the cytokine and protease output that destroys alveoli and scars airways in COPD."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Exacerbations can spiral into systemic infection: bacterial and viral exacerbations cause pneumonia and respiratory failure, and in frail COPD patients these can progress to sepsis requiring critical care."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic lung inflammation blunts the marrow: although hypoxia can raise red cells, the systemic inflammation of COPD often instead produces an anemia of chronic disease that worsens breathlessness and exercise tolerance."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Inhaled steroids seed oral thrush: the inhaled corticosteroids used in COPD deposit on the oropharynx and locally suppress immunity, allowing Candida to overgrow into oral candidiasis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Systemic inflammation reaches the brain's arteries: COPD's chronic inflammation, hypoxia and shared smoking risk accelerate atherosclerosis and raise the risk of ischemic stroke, part of its cardiovascular comorbidity."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "The same smoke breeds an aggressive cancer: COPD is an independent risk factor for lung cancer, including small cell lung cancer, beyond their shared cause in tobacco smoke."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Inflammation and steroids raise blood sugar: COPD's systemic inflammation and the corticosteroids used for exacerbations promote insulin resistance, giving it an elevated rate of type 2 diabetes."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Hypoxia and diuretics raise uric acid: chronic hypoxemia increases purine turnover and the diuretics used for cor pulmonale retain urate, so gout is a common COPD comorbidity."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Chronic low oxygen wears on the brain: the sustained hypoxemia, systemic inflammation and vascular disease of COPD are linked to accelerated cognitive decline and dementia."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The gut and lungs trouble each other: gastro-oesophageal reflux is common in COPD and triggers exacerbations through microaspiration, and advanced disease causes cachexia with muscle and fat wasting."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its steroids reach beyond the lungs: repeated systemic corticosteroid courses for COPD exacerbations cause hyperglycaemia, adrenal suppression and bone loss, the endocrine cost of control."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Failing gas exchange clouds the brain: COPD's hypoxaemia and carbon-dioxide retention can cause CO2 narcosis with confusion and drowsiness, and chronic hypoxia impairs cognition."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Damaged airways lose their defences: impaired innate and adaptive immunity invites bacterial colonisation and exacerbations, and lymphoid follicles in the airway walls drive its chronic inflammation."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It strains the kidney through hypoxia and acid-base shifts: chronic hypoxia and shared smoking damage link COPD to chronic kidney disease, and CO2 retention drives compensatory renal bicarbonate handling."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It and its treatment mark the skin: smoking accelerates skin ageing, hypoxaemia causes central cyanosis, and long-term corticosteroids thin and bruise the skin."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "A double-edged controller: inhaled corticosteroids reduce exacerbations in some COPD, while courses of systemic steroids treat flares at the cost of pneumonia risk, osteoporosis and hyperglycaemia."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Breathlessness and low oxygen reach the bedroom: COPD commonly causes sexual dysfunction and is linked to hypogonadism from chronic illness, hypoxia and steroid use."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Lymphoid follicles fuel the disease: COPD induces bronchus-associated lymphoid tissue — tertiary lymphoid follicles in the small airways — that sustain the chronic inflammation and remodelling of severe disease."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "A heart drug long feared but safe: cardioselective beta-blockers are safe and beneficial in COPD patients with heart disease, and the old blanket contraindication has been abandoned."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "A virus that hits the damaged lung hard: COPD raises the risk of severe COVID-19 and respiratory failure, and SARS-CoV-2 is now a major cause of the infective exacerbations that worsen it."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Weight cuts both ways: obesity worsens breathlessness and can overlap with obesity-hypoventilation, yet a higher body-mass index is paradoxically associated with better survival in advanced COPD."
  - target: 01-human/05-tissue/lung-slice
    relation: connects-to
    note: "It destroys the lung architecture: COPD merges emphysematous loss of alveolar walls with small-airway inflammation and mucus, the parenchymal and airway destruction on a lung slice that produces irreversible airflow obstruction."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It overloads the right heart: chronic hypoxic pulmonary vasoconstriction raises pulmonary pressure, and the resulting right-ventricular hypertrophy and failure — cor pulmonale — is a major cause of death in COPD."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Biologics reach eosinophilic COPD: dupilumab, the anti-IL-4Rα antibody, was approved for COPD with type-2 (eosinophilic) inflammation, bringing targeted biologic therapy to a disease long treated only with bronchodilators and steroids."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Arrhythmia in failing lungs: hypoxia, hyperinflation and beta-agonist bronchodilators predispose COPD patients to multifocal atrial tachycardia and atrial fibrillation through the conduction system."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Systemic inflammation hits arteries: COPD's circulating inflammatory mediators accelerate atherosclerosis of the arterial wall, making cardiovascular disease a leading cause of death in the disease."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Lungs and kidneys decline together: COPD and chronic kidney disease cluster through shared smoking, chronic hypoxia and systemic inflammation, and exacerbations can precipitate acute kidney injury."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Post-TB lung disease: prior tuberculosis is a major and under-recognised cause of COPD-like airflow obstruction worldwide, especially in high-burden regions, even in never-smokers."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Secondary erythrocytosis: chronic hypoxia in COPD raises erythropoietin and red-cell mass, a secondary polycythaemia distinct from the JAK2-driven polycythaemia vera."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Smoking, steroids and bone: COPD lowers bone density through smoking, systemic inflammation, inactivity and corticosteroid courses, fracturing the cortical bone and further impairing breathing."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Failing antioxidant defence: NRF2 (NFE2L2) drives the lung's antioxidant response, and its impairment in COPD leaves airways defenceless against cigarette-smoke oxidative stress—a therapeutic target."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Stalled repair: defective Wnt/β-catenin signalling blunts alveolar regeneration in emphysema, helping explain why destroyed lung tissue in COPD fails to repair."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Immune orchestration: dendritic cells accumulate in COPD airways, presenting smoke-modified antigens and driving the chronic T-cell inflammation and lymphoid follicles of advanced disease."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: cigarette smoke activates the NLRP3 inflammasome in airway cells, releasing IL-1β to amplify the chronic neutrophilic inflammation of COPD."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes and macrophages into the COPD lung, where their proteases and cytokines drive the alveolar destruction of emphysema."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic alveolar damage: CD8 T cells accumulating in COPD use perforin and granzyme to kill alveolar cells, contributing to the emphysematous loss of lung tissue."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Alveolar maintenance: VEGF sustains the alveolar-capillary network, and its loss drives the endothelial and epithelial apoptosis behind emphysematous alveolar destruction in COPD."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Neutrophilic airways: IL-17A drives the neutrophil recruitment and mucus hypersecretion of the chronic bronchitis phenotype of COPD, sustaining its corticosteroid-resistant airway inflammation."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Neutrophil alarmin: S100A8/A9 released by the neutrophils flooding the COPD airway amplifies inflammation and serves as a biomarker of disease activity and exacerbation."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Mucus hypersecretion: cigarette smoke activates EGFR on airway epithelium to drive goblet-cell metaplasia and MUC5AC overproduction, the mechanism of the chronic mucus hypersecretion of the chronic-bronchitis phenotype."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Emphysematous apoptosis: loss of VEGF survival signalling and oxidative injury trigger caspase-3-mediated apoptosis of alveolar endothelial and epithelial cells, the cell death that destroys alveoli in emphysema."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Smoke-driven innate inflammation: cigarette smoke and released DAMPs activate TLR4 on airway cells and macrophages, igniting the NF-κB-driven innate inflammation that sustains and amplifies COPD airway disease."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Cholinergic bronchoconstriction: vagal acetylcholine acting on airway muscarinic receptors is the dominant reversible component of airflow obstruction in COPD, the target of the long-acting muscarinic antagonist (LAMA) bronchodilators central to its treatment."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Adrenergic bronchodilation: epinephrine and β2-agonist drugs relax airway smooth muscle through β2-adrenergic receptors, the long-acting β-agonist (LABA) inhalers that, with LAMAs, form the bronchodilator backbone of COPD therapy."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Inhaled corticosteroids: glucocorticoids acting through the glucocorticoid receptor reduce exacerbations in the eosinophilic, exacerbation-prone subset of COPD, though steroid resistance limits their benefit in the predominantly neutrophilic disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Mucus hypersecretion: type-2 cytokine IL-13 drives goblet-cell metaplasia and mucin overproduction in the eosinophilic COPD subset, contributing to the chronic-bronchitis phenotype and airway obstruction."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Cytotoxic emphysema: CD8+ T cells and Th1 IFN-γ accumulate in COPD airways, driving the cytotoxic alveolar-wall destruction that produces emphysematous loss of lung parenchyma."
  - target: 01-human/03-molecular/surfactant
    relation: connects-to
    note: "Airway collapse: oxidant- and protease-mediated surfactant dysfunction in COPD raises surface tension in small airways, promoting their collapse on expiration and worsening air trapping and host-defence impairment."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate airway inflammation: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped), activated by cigarette-smoke products and bacterial colonisation, sustains the chronic airway inflammation of COPD."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Cellular senescence: dysregulated mTOR signalling and impaired autophagy promote the senescence of airway and alveolar cells that underlies the accelerated lung ageing and emphysema of COPD."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine amplification: IL-6 and IFN-γ signalling through JAK-STAT (both already mapped) amplifies the inflammatory response of COPD and is an emerging anti-inflammatory therapeutic target."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (mTOR mapped) governs alveolar-epithelial survival and the cellular senescence implicated in emphysema and COPD progression."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "EGFR-ERK-MAPK signalling (EGFR mapped) drives the airway mucus hypersecretion and epithelial remodelling of chronic bronchitis in COPD."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the macrophage-driven airway inflammation of COPD and serves as a biomarker of disease activity."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling drives the chronic airway inflammation and mucus responses central to the progression of COPD."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cigarette-smoke-induced DNA damage releases cytosolic DNA that engages cGAS-STING, amplifying the sterile inflammation and cellular senescence of COPD."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling underlies the antiviral response that drives the viral exacerbations of COPD."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the airway epithelial oxidative-stress defense and cellular senescence that drive the accelerated lung aging of COPD."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling (TGF-β already mapped) drives the small-airway fibrosis and remodeling of COPD."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β participates in the corticosteroid-insensitive inflammation and cellular senescence of COPD."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the airway inflammation and corticosteroid resistance of COPD."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, coupled to mitochondrial and autophagic quality control, is dysregulated in the cellular senescence and oxidative stress of COPD."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Dysregulated autophagy contributes to the cellular senescence and impaired clearance underlying the emphysema of COPD."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the airway epithelial and neutrophil responses of chronic obstructive pulmonary disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the airway and parenchymal inflammation of chronic obstructive pulmonary disease."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the smoking-linked epigenetic dysregulation of chronic obstructive pulmonary disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the airway leukocyte trafficking and lung-repair processes of chronic obstructive pulmonary disease."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the airway epithelial and innate immune responses of chronic obstructive pulmonary disease."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the airway inflammation of chronic obstructive pulmonary disease."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the airway-epithelial and immune gene programs of chronic obstructive pulmonary disease."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell-mediated inflammation of chronic obstructive pulmonary disease."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the airway inflammation and emphysema-related tissue remodeling of chronic obstructive pulmonary disease."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Secondary polycythaemia: chronic hypoxaemia in COPD drives erythropoietin (already mapped) and raises haemoglobin and haematocrit, a compensatory polycythaemia that increases blood viscosity and thrombotic risk."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac comorbidity: COPD strongly associates with cardiovascular disease, and troponin elevation from cor pulmonale, demand ischaemia and comorbid coronary disease marks the cardiac injury that contributes to its mortality."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Airway mucosal defence: reduced secretory IgA over the remodelled small airways of COPD weakens the mucosal barrier against inhaled microbes, promoting the bacterial colonisation and infective exacerbations that drive disease progression."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Respiratory acidosis: advanced COPD retains carbon dioxide, and the resulting proton accumulation produces the respiratory acidosis of type-2 respiratory failure, a hallmark of severe exacerbations that guides ventilatory support."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Smoking oxidative burden: cigarette smoke and the inflamed airway generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative stress (NRF2 already mapped) drives the tissue destruction and steroid resistance of COPD."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Refractory breathlessness: low-dose opioids acting on the mu-opioid receptor relieve the intractable breathlessness of advanced COPD, a mainstay of its palliative care despite the caution needed over respiratory depression."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Airway inflammatory eicosanoids: prostaglandins from the inflamed airway (IL-6, TNF and IL-1 already mapped) contribute to the inflammation and mucus of COPD, and prostaglandin E2 has complex effects on the airway smooth muscle and cough."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophilic phenotype: IL-5, with IL-13 (already mapped), drives the eosinophilic inflammation of a COPD subset, the blood eosinophil count guiding inhaled-corticosteroid (glucocorticoid receptor already mapped) use and anti-IL-5 biologic trials."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Hypoxic pulmonary hypertension: hypoxia (HIF-1-alpha already mapped) raises endothelin-1, constricting the pulmonary vasculature to produce the pulmonary hypertension and cor pulmonale (troponin already mapped) of advanced COPD."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 eosinophilic arm: IL-4, with IL-13 and IL-5 (already mapped), drives the type-2 eosinophilic inflammation of the COPD subset whose blood eosinophils guide the inhaled-corticosteroid (glucocorticoid receptor already mapped) response."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Cachexia and adipokines: the systemic inflammation (TNF and IL-6 already mapped) of COPD disturbs leptin and the adipokine balance, contributing to the muscle wasting and cachexia that worsen the prognosis of advanced disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron dysregulation: the hypoxia (HIF-1-alpha already mapped) and chronic inflammation of COPD disturb iron handling, producing either the anaemia of chronic disease or, with hypoxaemia, the secondary polycythaemia (erythropoietin already mapped)."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Elastin cross-linking: copper is the cofactor of lysyl oxidase that cross-links the elastin and collagen (already mapped) of the lung; the copper-dependent elastin repair is overwhelmed by the protease-antiprotease imbalance of the emphysema of COPD."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Cachexia adipokine: adiponectin, with leptin (already mapped), is disturbed in the cachexia and systemic inflammation (TNF and IL-6 already mapped) of advanced COPD, contributing to the muscle wasting."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Systemic inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the systemic inflammation (IL-6 already mapped) of COPD."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "ACOS overlap: the asthma-COPD overlap shares the airway inflammation (the eosinophilic — IL-5 already mapped, and the neutrophilic — IL-17 already mapped) and the bronchodilator/ICS therapy."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Cor pulmonale: the chronic hypoxia (HIF and EPO already mapped) and the vascular remodelling (endothelin already mapped) of COPD cause the pulmonary hypertension and the cor pulmonale."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Airway/vascular remodelling: the airway smooth muscle (acetylcholine already mapped — the bronchoconstriction) and the pulmonary-vascular smooth-muscle remodelling contribute to the airflow limitation and the hypertension of COPD."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 airway axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neutrophilic (already mapped) airway inflammation of COPD."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the airway inflammation, part of the mixed immune profile of COPD."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Antiviral exacerbation interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing, mediates the antiviral response to the respiratory-virus exacerbations of COPD."
---

# COPD

## Overview

**Chronic obstructive pulmonary disease (COPD)** is a common, preventable, and treatable chronic respiratory disease characterized by persistent, progressive **airflow limitation** that is not fully reversible, associated with an enhanced chronic inflammatory response in the airways and lung to noxious particles or gases — principally **cigarette smoke**. COPD is the **third leading cause of death globally** (~3.3 million deaths/year, WHO 2019) and a leading cause of disability [^rabe-2017-gold-copd].

COPD encompasses two overlapping pathological processes:
- **Emphysema:** Permanent enlargement and destruction of airspaces distal to the terminal bronchiole → loss of alveolar surface area → reduced gas exchange → hypoxemia; also destruction of elastic recoil → air trapping → hyperinflation
- **Chronic bronchitis:** Productive cough on most days for ≥3 months in ≥2 consecutive years; airway inflammation → mucus hypersecretion → small airway remodeling → fixed obstruction

**Global burden (GBD 2019):** ~390 million people affected globally; COPD is severely underdiagnosed (only ~25% of patients receive diagnosis); 90% of COPD deaths occur in low-to-middle income countries where spirometry is limited.

**Risk factors:**
- **Cigarette smoking (dominant):** ~80-90% of COPD in high-income countries; pack-year dose-response; passive smoking in childhood → accelerated lung function decline
- **Biomass fuel exposure:** Wood smoke from cooking fires → COPD in women in developing countries (accounts for ~50% of global COPD burden)
- **Occupational exposures:** Coal dust, silica, cadmium, isocyanates
- **Genetic:** Alpha-1 antitrypsin (AAT) deficiency (AATD) — Z allele (Glu342Lys) → polymerization and intracellular retention → panacinar emphysema by age 40 in smokers (earlier); SERPINA1 Pi*ZZ genotype; 1-2% of COPD
- **Early life factors:** Prematurity, low birth weight, childhood respiratory infections → reduced peak lung function → lower FEV1 trajectory → COPD risk in adulthood

## Structure

### Lung pathology in COPD

**Small airways disease (obstructive bronchiolitis):**
- Airway wall infiltrated by macrophages, CD8+ T cells (Tc1), and neutrophils
- Goblet cell hyperplasia → excess mucus → airway plugging → V/Q mismatch
- Subepithelial fibrosis (TGF-beta-driven) → irreversible narrowing of airways <2 mm diameter
- Loss of small airways (airway "pruning") is the primary determinant of FEV1 decline in early COPD

**Emphysema:**
- **Centrilobular (centriacinar):** Destruction centered on respiratory bronchioles; most common; upper-lobe predominant; smoking-related; macrophage and neutrophil elastase/MMP-12 → elastin degradation → alveolar wall rupture
- **Panacinar (panlobular):** Uniform destruction of entire acinus; lower-lobe predominant; associated with AAT deficiency (unopposed neutrophil elastase); can occur in severe smoking-related COPD
- **Paraseptal:** Subpleural; associated with spontaneous pneumothorax
- **Functional effect:** Loss of alveolar attachments → small airway collapse on exhalation → dynamic hyperinflation → increased residual volume (RV) and total lung capacity (TLC) → barrel chest; diaphragm flattened → mechanical disadvantage → dyspnea

**Pulmonary vasculature:**
- Hypoxic pulmonary vasoconstriction → remodeling of pulmonary arterioles (smooth muscle hypertrophy, intimal thickening) → **pulmonary hypertension** (COPD-PH, WHO Group 3)
- Cor pulmonale: RV hypertrophy and failure in severe COPD-PH (peripheral edema, elevated JVP, right heart strain on EKG)

### COPD inflammatory cells [^vestbo-2013-gold-strategy]

**Macrophages:** Central effectors — cigarette smoke → TLR4/TLR2 → NF-kB → MMP-9/MMP-12 → elastin degradation → emphysema; also defective phagocytosis (efferocytosis) → bacteria not cleared → exacerbations
**Neutrophils:** Elevated in airway lumen during exacerbations; neutrophil elastase overwhelms AAT → matrix destruction; NETosis in COPD exacerbations (bacterial/viral)
**CD8+ T cells (Tc1):** Predominant adaptive immune cell in COPD; release IFN-gamma, perforin → alveolar epithelial damage
**Innate lymphoid cells (ILC2, ILC3):** ILC2 → IL-5/IL-13 in eosinophilic COPD overlap; ILC3 → IL-22 in type 3 COPD responses
**Epithelial cells:** EMT (epithelial-mesenchymal transition) in COPD → fibrosis; loss of ciliary function → mucociliary clearance impairment → microbiome dysbiosis

## Function

### Clinical presentation

**Symptoms:**
- **Dyspnea:** Progressive, "more breathless than same-age peers"; initially on exertion, eventually at rest; **mMRC scale (0-4)**: grade 2 = "walks slower than peers on level ground"
- **Chronic productive cough:** With mucopurulent sputum; "smoker's cough"; worse in morning
- **Wheeze and chest tightness:** Variable
- **Extrapulmonary manifestations:** Skeletal muscle wasting (cachexia) — ubiquitin-proteasome and autophagy-mediated; osteoporosis (smoking, steroids); cardiovascular disease (systemic inflammation, shared risk factors); depression/anxiety; lung cancer (shared smoking risk)

**Physical examination:**
- Barrel chest (increased AP diameter), hyperresonance on percussion
- Reduced breath sounds, prolonged expiratory phase, crackles with secretions
- Accessory muscle use, pursed-lip breathing
- JVP elevation, peripheral edema (cor pulmonale)
- **Clubbing is NOT a feature of COPD** — its presence should prompt evaluation for lung cancer or interstitial lung disease

### Spirometry: GOLD staging [^vestbo-2013-gold-strategy]

**Diagnosis requires post-bronchodilator FEV1/FVC <0.70** (LLN [lower limit of normal] preferred in elderly to reduce over-diagnosis):

| GOLD Grade | FEV1 (% predicted) | Severity |
|:---|:---|:---|
| GOLD 1 | ≥80% | Mild |
| GOLD 2 | 50-79% | Moderate |
| GOLD 3 | 30-49% | Severe |
| GOLD 4 | <30% | Very severe |

**GOLD ABCD Group Assessment (2023 revision — symptoms + exacerbation risk):**
- **Group A (low risk, few symptoms):** GOLD 1-2, 0-1 exacerbations, CAT <10 → SABA PRN or LABA or LAMA
- **Group B (low risk, more symptoms):** GOLD 1-2, 0-1 exacerbations, CAT ≥10 → LABA+LAMA
- **Group E (high exacerbation risk):** GOLD 3-4 or ≥2 exacerbations → LABA+LAMA; add ICS if blood eosinophils ≥300/μL

### COPD exacerbations

**Acute exacerbation of COPD (AECOPD):** Acute worsening of respiratory symptoms beyond normal daily variation requiring a change in medication.

**Triggers:**
- Respiratory viruses (rhinovirus, influenza, RSV): ~50-70% of exacerbations
- Bacteria (H. influenzae, Streptococcus pneumoniae, Moraxella catarrhalis, Pseudomonas in severe COPD): ~25%
- Air pollution, temperature changes

**Impact:** Each exacerbation accelerates lung function decline; hospitalizations associated with 10% in-hospital mortality and 25% 1-year mortality; leading cause of COPD-related healthcare expenditure.

**Treatment of AECOPD:**
- **Bronchodilators:** Short-acting beta-2 agonists (salbutamol/albuterol) + short-acting muscarinic antagonists (ipratropium) via nebulizer or MDI
- **Systemic corticosteroids:** Prednisone 40 mg × 5 days (equivalent to 14 days) — reduces hospitalization duration and treatment failure
- **Antibiotics:** If purulent sputum, elevated CRP, or severity indicates bacterial cause — amoxicillin/clavulanate, azithromycin, or doxycycline (mild-moderate); tailor to local resistance patterns; anti-pseudomonal (ciprofloxacin) for frequent exacerbators with risk factors
- **Oxygen:** Target SpO2 88-92% (avoid over-oxygenation → suppress hypoxic drive in CO2 retainers)
- **Non-invasive ventilation (NIV/BiPAP):** pH <7.35 with PaCO2 >45 mmHg (hypercapnic respiratory failure) → reduces intubation rate and mortality

## Pathology

### COPD and lung cancer

- Smokers with COPD have **3-5× higher lung cancer risk** than smokers without COPD — shared carcinogenic burden AND chronic inflammation → NF-kB/STAT3 → tumor-promoting milieu
- COPD (obstructed airflow) is an independent lung cancer risk factor even after adjusting for smoking (FEV1 as predictor)
- Annual low-dose CT screening (NLST/NELSON criteria) recommended for high-risk smokers — reduces lung cancer mortality by ~20%

### Treatment [^jones-2017-dupilumab-copd]

**Chronic pharmacotherapy:**

*Bronchodilators (first-line):*
- **LABA (long-acting beta-2 agonist):** Salmeterol, formoterol, indacaterol, olodaterol; relax airway smooth muscle; QD or BID
- **LAMA (long-acting muscarinic antagonist):** Tiotropium, umeclidinium, glycopyrronium; block M3 receptors on smooth muscle → bronchodilation + mucus reduction; QD; tiotropium reduces exacerbations ~14%
- **LABA+LAMA combination:** Superior to monotherapy in all GOLD groups B/E; ICS not added unless eosinophils ≥300 or persistent exacerbations
- **Triple therapy (ICS+LABA+LAMA):** IMPACT trial → ICS/UMEC/VI (Trelegy) vs. LABA+LAMA: ORR 21% reduction in moderate/severe exacerbations; lung cancer signal with ICS overuse

*Inhaled corticosteroids (ICS):*
- Added for GOLD E with eosinophils ≥300/μL or repeated exacerbations
- Fluticasone/salmeterol (Advair), budesonide/formoterol (Symbicort)
- Risk of pneumonia (especially fluticasone at high doses in severe COPD)

*Phosphodiesterase-4 (PDE-4) inhibitor:*
- **Roflumilast (Daliresp):** Oral; reduces cyclic AMP degradation → anti-inflammatory; add in severe COPD (FEV1 <50%) with chronic bronchitis and frequent exacerbations; 17% reduction in exacerbations; side effects: nausea, diarrhea, weight loss, depression

*AAT replacement:*
- **Alpha-1 proteinase inhibitor (Prolastin, Zemaira):** Weekly IV infusion for PiZZ AATD with FEV1 35-65% → slows radiological emphysema progression (RAPID trial: CT density loss -1.45 vs -2.19 g/L/year) — expensive, modestly effective

*Oxygen therapy:*
- **Long-term oxygen therapy (LTOT):** PaO2 ≤55 mmHg or SpO2 ≤88% at rest → >15 h/day oxygen use improves survival (MRC and NOTT trials); does NOT improve survival in moderate hypoxemia (LOTT trial, PaO2 56-69)
- Ambulatory oxygen for exercise desaturation

*Biologic therapy (emerging):*
- **Dupilumab (anti-IL-4R-alpha, Dupixent):** Blocks IL-4 and IL-13 signaling; approved 2024 for COPD with type 2 inflammation (blood eosinophils ≥300/μL); BOREAS trial: 34% reduction in moderate/severe exacerbations vs. placebo; first biologic approved for COPD [^jones-2017-dupilumab-copd]

**Pulmonary rehabilitation:**
- Exercise training + education + self-management; 6-8 weeks; most effective intervention for dyspnea, exercise tolerance, and quality of life; does not alter FEV1 decline; under-utilized

**Surgical/interventional:**
- **Lung volume reduction surgery (LVRS):** Remove most diseased emphysema tissue (upper-lobe) → reduces hyperinflation → improves diaphragm mechanics; NETT trial: mortality benefit in upper-lobe predominant emphysema with low exercise capacity
- **Bronchoscopic lung volume reduction (BLVR):** Endobronchial valves (Zephyr) → lobar collapse → reduces hyperinflation; approved for heterogeneous emphysema with intact interlobar fissures; no collateral ventilation required (Chartis measurement)
- **Lung transplantation:** Single or bilateral; reserved for GOLD 4 with poor prognosis; 5-year survival ~55%

## Connections

- `targets` → **[Respiratory System](../respiratory-system/README.md)** — COPD irreversibly destroys alveolar structure (emphysema) and remodels small airways (chronic bronchiolitis), reducing gas exchange surface area and creating fixed airflow obstruction; hyperinflation flattens the diaphragm, worsening the mechanical disadvantage and dyspnea.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — cigarette smoke-activated macrophages produce TGF-beta1 → subepithelial airway fibrosis and smooth muscle hypertrophy → fixed obstruction; TGF-beta also impairs alveolar epithelial repair and drives EMT, contributing to COPD pathogenesis and lung cancer progression.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — alveolar macrophages are primary COPD effectors; cigarette smoke activates macrophages → MMP-9/MMP-12 secretion → elastin degradation → emphysema; COPD macrophages also fail at bacterial clearance → susceptibility to infectious exacerbations.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — neutrophils accumulate in COPD airways during exacerbations; neutrophil elastase overwhelms AAT → matrix proteolysis; IL-8-driven neutrophil recruitment is the dominant exacerbation amplifier; NETosis releases extracellular traps that contribute to airway inflammation.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — COPD destroys lung architecture: emphysema ruptures alveolar walls reducing gas exchange surface; chronic bronchitis remodels small airways creating fixed obstruction; GOLD spirometric staging (FEV1/FVC <0.7) classifies severity and guides treatment selection.
- `connects-to` → **[Asthma](../asthma/README.md)** — COPD-asthma overlap (ACO) affects ~10-15% of COPD patients with combined fixed obstruction and type 2 eosinophilic inflammation; ACO has higher exacerbation frequency; dupilumab (anti-IL-4Rα) is approved for COPD with eosinophils ≥300/μL.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β amplifies COPD exacerbations: NLRP3 inflammasome activated by smoke particles releases IL-1β → neutrophil and macrophage recruitment → airway inflammation and goblet cell hyperplasia → mucus hypersecretion; IL-1β blockade (canakinumab) is under investigation.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — COPD and cystic fibrosis are chronic obstructive airway diseases: COPD is acquired emphysema from decades of cigarette smoke, while CF is inherited CFTR failure causing childhood bronchiectasis — yet both end in neutrophilic airway destruction and respiratory failure.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Severe COPD strains the right heart: chronic hypoxia drives pulmonary vasoconstriction and arteriolar remodeling → pulmonary hypertension (WHO Group 3) → right ventricular hypertrophy and failure (cor pulmonale), with raised JVP and peripheral edema.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Bacterial infection — often Streptococcus pneumoniae, Haemophilus influenzae, or Moraxella — drives roughly a quarter of COPD exacerbations; purulent sputum guides antibiotics, and pneumococcal vaccination is recommended to help prevent them.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — COPD and lung cancer are smoking's twin diseases that frequently coexist: shared tobacco-driven inflammation, oxidative stress and impaired DNA repair mean COPD independently raises NSCLC risk, COPD limits surgery, and both are screened together with low-dose CT in heavy smokers.
- `connects-to` → **[RSV](../rsv/README.md)** — RSV is an underappreciated driver of COPD exacerbations: it infects airway epithelium to provoke neutrophilic inflammation and bronchospasm, accounting for a notable share of hospitalized flares in older adults; new adult RSV vaccines (Arexvy, Abrysvo) help reduce this burden.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Cigarette smoke is the dominant cause of COPD: inhaled carbon-rich particulates and combustion chemicals trigger protease-antiprotease imbalance and chronic neutrophilic inflammation → emphysema and small-airway fibrosis; cessation is the only intervention that slows decline.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — COPD is a leading cause of pulmonary hypertension and cor pulmonale: chronic hypoxia constricts and remodels pulmonary arteries, raising right-heart pressure until the right ventricle fails—so a loud P2, edema, and a dilated right heart signal this grave complication.
- `connects-to` → **[Influenza](../influenza/README.md)** — Respiratory viruses like influenza are major triggers of COPD exacerbations: infection inflames already-damaged airways, causing the acute worsening of breathlessness and sputum that drives hospitalization—so annual flu vaccination is core to COPD care.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Osteoporosis is a frequent, underrecognized COPD comorbidity: inflammation, inactivity, low vitamin D, smoking, and corticosteroids thin the bones, so COPD patients fracture more—and vertebral fractures further impair breathing, warranting bone-density screening.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — COPD destroys the alveolus in emphysema: protease-driven breakdown of alveolar walls merges the tiny gas-exchange sacs into large, inelastic spaces, slashing surface area and trapping air—so the lung loses both the recoil to exhale and the surface to oxygenate.
- `connects-to` → **[Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — Type II pneumocytes are injured and overwhelmed in COPD: chronic smoke exposure damages these surfactant-producing, alveolus-repairing cells, impairing their regeneration of the destroyed alveolar lining—so failed epithelial repair contributes to progressive emphysema.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — COPD ultimately fails at delivering oxygen: airway obstruction and alveolar destruction cause hypoxemia and CO2 retention, which is why advanced COPD needs supplemental oxygen—the one therapy, with smoking cessation, shown to prolong survival in hypoxemic patients.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Airway smooth muscle drives the obstruction in COPD: chronic inflammation thickens and tightens bronchiolar smooth muscle, and bronchodilators that relax it are the mainstay of symptom control—targeting the reversible component of fixed airflow limitation.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — COPD and cardiovascular disease are deeply linked: shared smoking and systemic inflammation raise heart-attack and arrhythmia risk, and chronic hypoxia strains the right heart toward cor pulmonale—so cardiovascular disease is a leading cause of death in COPD.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — COPD and depression commonly coexist: breathlessness, disability and chronic hypoxia foster depression and anxiety in a large share of patients, which in turn worsen adherence and outcomes—so mental health is integral to comprehensive COPD care.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — COPD scars the small airways: chronic inflammation drives peribronchiolar fibrosis that narrows and obliterates terminal bronchioles, so airway fibrosis—alongside alveolar destruction in emphysema—causes the fixed airflow obstruction that defines COPD.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — COPD is linked to the gut-lung axis: altered gut and airway microbiomes shape lung inflammation and exacerbations, so the microbiome is emerging as a factor in disease course beyond the cigarette smoke that starts it.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — COPD and anxiety feed each other: breathlessness provokes fear, and anxiety worsens the sensation of dyspnea and triggers panic, so anxiety disorders are common and undertreated and worsen quality of life and exacerbation risk.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D deficiency worsens COPD: low levels are common in these patients and track with more frequent exacerbations and faster bone loss, so supplementing deficient patients can cut flare-ups and protect against the osteoporosis COPD brings.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Chronic low oxygen in COPD drives erythropoietin: persistent hypoxia signals the kidney to make more EPO, thickening the blood with extra red cells (secondary polycythemia) that strains the heart already burdened by lung disease.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Exhaled nitric oxide helps tell COPD from asthma: FeNO rises with the eosinophilic airway inflammation of asthma but stays low in typical neutrophilic COPD, so the gas is a breath biomarker guiding who will respond to inhaled steroids.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — COPD throws off acid-base balance by trapping CO2: failing lungs cannot exhale carbon dioxide, which becomes carbonic acid and raises blood hydrogen ions, producing the respiratory acidosis that marks advanced disease and flares.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — COPD remodels the small airways with collagen: TGF-beta-driven fibroblasts lay down collagen around the bronchioles, narrowing and stiffening them, so airway fibrosis—not just alveolar loss—drives the irreversible airflow limitation.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells help destroy the COPD lung: CD8 T cells accumulate in the airways and alveoli, and their killing of lung cells correlates with the emphysema and airflow limitation, adding adaptive immunity to the neutrophil-macrophage attack.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Severe COPD can cloud the brain: as failing lungs retain carbon dioxide and drop oxygen, the rising CO2 causes confusion and drowsiness (CO2 narcosis), a danger during exacerbations and with over-oxygenation.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — COPD scars its small airways through fibroblasts: TGF-β activates these cells to lay down collagen around the bronchioles, narrowing and stiffening them in the airway remodeling that fixes the airflow limitation.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — COPD is a body-wide inflammatory state driven by TNF-α: spilling from the inflamed lungs, this cytokine drives the muscle wasting and weight loss (cachexia) that worsen prognosis beyond the airways.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — COPD is imaged in X-ray photons: chest films show hyperinflated lungs and flattened diaphragms, and CT quantifies the emphysema, mapping where lung tissue has been destroyed.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — COPD damages the lung's vessels: hypoxia and inflammation injure endothelial cells, remodeling the pulmonary arteries into the pulmonary hypertension and cor pulmonale of advanced disease.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Chronic low oxygen in COPD drives the marrow: rising erythropoietin spurs it to overproduce red cells, the secondary polycythemia that thickens the blood of long-standing hypoxic patients.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows emphysema's ruin up close: the delicate alveolar walls dissolve as enzymes outpace their inhibitors, merging the fine air sacs into floppy enlarged spaces that collapse on exhaling and trap stale air.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — COPD shows on the surface: deoxygenated blood turns the lips and nails blue with cyanosis, fingertips club from chronic hypoxia, and the ruddy plethora of secondary polycythemia colors the 'blue bloater' face.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Failing lungs strain the kidney: chronic low oxygen and high carbon dioxide, plus the back-pressure of cor pulmonale, impair renal blood flow, so fluid retention and kidney dysfunction track with advanced COPD.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Chronic low oxygen thickens the blood: COPD's persistent hypoxia drives erythropoietin and a secondary polycythemia, raising the red-cell mass and viscosity — though systemic inflammation can also leave some patients anemic instead.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — COPD wastes the muscles it depends on: systemic inflammation, inactivity, and steroids drive a peripheral muscle dysfunction and cachexia that limit exercise and predict mortality, which pulmonary rehabilitation works to reverse.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — One inherited defect links lung and liver: alpha-1 antitrypsin deficiency leaves the lung's elastin unprotected (early emphysema) while the misfolded protein jams up hepatocytes, causing cirrhosis — COPD and liver disease from a single gene.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — COPD strains the right heart: chronic hypoxia constricts the lung's vessels, and the back-pressure of pulmonary hypertension overworks the right ventricle into cor pulmonale — right heart failure with leg swelling and congestion that worsens prognosis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — COPD lowers testosterone: chronic hypoxia, systemic inflammation and corticosteroid use suppress the gonadal axis, and the resulting low testosterone deepens the muscle wasting and fatigue, sometimes prompting replacement in selected men.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Wasting away marks severe COPD: the high work of breathing and systemic inflammation burn through fat and lean tissue, and the loss of adipocyte mass — a low BMI and fat-free mass — is a strong independent predictor of death in the disease.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T cells, not just neutrophils, scar the airway: CD4 Th1 and Th17 cells accumulate in the COPD lung and sustain the chronic inflammation, an adaptive arm that makes the disease partly autoimmune in flavor.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — COPD is hard on the arteries too: shared smoking plus the disease's systemic inflammation accelerate atherosclerosis, so cardiovascular disease — not respiratory failure — is a leading cause of death in milder COPD.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 carries the inflammation body-wide: spilling from the inflamed lung into the blood, it drives the muscle wasting, weakness, and comorbidity of COPD and rises sharply during exacerbations.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Chronic hypoxia switches on HIF-1α: low alveolar oxygen in advanced COPD stabilizes this transcription factor, driving the erythropoietin-fueled secondary polycythemia and the pulmonary-vascular remodeling that ends in cor pulmonale.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Damaged airways invite Aspergillus: structurally altered COPD lungs and inhaled-steroid use foster Aspergillus colonization, sensitization, and occasionally chronic or invasive pulmonary aspergillosis that worsens the disease.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Exacerbations carry hidden clots: COPD raises the risk of pulmonary embolism, and a PE can both mimic and precipitate an exacerbation, so unexplained worsening prompts a search for venous thromboembolism.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Cigarette smoke throws the airway's inflammation switch: oxidants and irritants activate NF-κB in bronchial epithelium and macrophages, driving the cytokine and protease output that destroys alveoli and scars airways in COPD.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Exacerbations can spiral into systemic infection: bacterial and viral exacerbations cause pneumonia and respiratory failure, and in frail COPD patients these can progress to sepsis requiring critical care.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic lung inflammation blunts the marrow: although hypoxia can raise red cells, the systemic inflammation of COPD often instead produces an anemia of chronic disease that worsens breathlessness and exercise tolerance.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Inhaled steroids seed oral thrush: the inhaled corticosteroids used in COPD deposit on the oropharynx and locally suppress immunity, allowing Candida to overgrow into oral candidiasis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Systemic inflammation reaches the brain's arteries: COPD's chronic inflammation, hypoxia and shared smoking risk accelerate atherosclerosis and raise the risk of ischemic stroke, part of its cardiovascular comorbidity.
- `connects-to` → **[Small Cell Lung Cancer](../sclc/README.md)** — The same smoke breeds an aggressive cancer: COPD is an independent risk factor for lung cancer, including small cell lung cancer, beyond their shared cause in tobacco smoke.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Inflammation and steroids raise blood sugar: COPD's systemic inflammation and the corticosteroids used for exacerbations promote insulin resistance, giving it an elevated rate of type 2 diabetes.
- `connects-to` → **[Gout](../gout/README.md)** — Hypoxia and diuretics raise uric acid: chronic hypoxemia increases purine turnover and the diuretics used for cor pulmonale retain urate, so gout is a common COPD comorbidity.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Chronic low oxygen wears on the brain: the sustained hypoxemia, systemic inflammation and vascular disease of COPD are linked to accelerated cognitive decline and dementia.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The gut and lungs trouble each other: gastro-oesophageal reflux is common in COPD and triggers exacerbations through microaspiration, and advanced disease causes cachexia with muscle and fat wasting.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its steroids reach beyond the lungs: repeated systemic corticosteroid courses for COPD exacerbations cause hyperglycaemia, adrenal suppression and bone loss, the endocrine cost of control.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Failing gas exchange clouds the brain: COPD's hypoxaemia and carbon-dioxide retention can cause CO2 narcosis with confusion and drowsiness, and chronic hypoxia impairs cognition.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Damaged airways lose their defences: impaired innate and adaptive immunity invites bacterial colonisation and exacerbations, and lymphoid follicles in the airway walls drive its chronic inflammation.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It strains the kidney through hypoxia and acid-base shifts: chronic hypoxia and shared smoking damage link COPD to chronic kidney disease, and CO2 retention drives compensatory renal bicarbonate handling.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It and its treatment mark the skin: smoking accelerates skin ageing, hypoxaemia causes central cyanosis, and long-term corticosteroids thin and bruise the skin.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — A double-edged controller: inhaled corticosteroids reduce exacerbations in some COPD, while courses of systemic steroids treat flares at the cost of pneumonia risk, osteoporosis and hyperglycaemia.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Breathlessness and low oxygen reach the bedroom: COPD commonly causes sexual dysfunction and is linked to hypogonadism from chronic illness, hypoxia and steroid use.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Lymphoid follicles fuel the disease: COPD induces bronchus-associated lymphoid tissue — tertiary lymphoid follicles in the small airways — that sustain the chronic inflammation and remodelling of severe disease.
- `connects-to` → **[Beta-Blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — A heart drug long feared but safe: cardioselective beta-blockers are safe and beneficial in COPD patients with heart disease, and the old blanket contraindication has been abandoned.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — A virus that hits the damaged lung hard: COPD raises the risk of severe COVID-19 and respiratory failure, and SARS-CoV-2 is now a major cause of the infective exacerbations that worsen it.
- `connects-to` → **[Obesity](../obesity/README.md)** — Weight cuts both ways: obesity worsens breathlessness and can overlap with obesity-hypoventilation, yet a higher body-mass index is paradoxically associated with better survival in advanced COPD.
- `connects-to` → **[Lung Slice](../../05-tissue/lung-slice/README.md)** — It destroys the lung architecture: COPD merges emphysematous loss of alveolar walls with small-airway inflammation and mucus, the parenchymal and airway destruction on a lung slice that produces irreversible airflow obstruction.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It overloads the right heart: chronic hypoxic pulmonary vasoconstriction raises pulmonary pressure, and the resulting right-ventricular hypertrophy and failure — cor pulmonale — is a major cause of death in COPD.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Biologics reach eosinophilic COPD: dupilumab, the anti-IL-4Rα antibody, was approved for COPD with type-2 (eosinophilic) inflammation, bringing targeted biologic therapy to a disease long treated only with bronchodilators and steroids.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Arrhythmia in failing lungs: hypoxia, hyperinflation and beta-agonist bronchodilators predispose COPD patients to multifocal atrial tachycardia and atrial fibrillation through the conduction system.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Systemic inflammation hits arteries: COPD's circulating inflammatory mediators accelerate atherosclerosis of the arterial wall, making cardiovascular disease a leading cause of death in the disease.
- `connects-to` → **[CKD](../ckd/README.md)** — Lungs and kidneys decline together: COPD and chronic kidney disease cluster through shared smoking, chronic hypoxia and systemic inflammation, and exacerbations can precipitate acute kidney injury.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Post-TB lung disease: prior tuberculosis is a major and under-recognised cause of COPD-like airflow obstruction worldwide, especially in high-burden regions, even in never-smokers.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Secondary erythrocytosis: chronic hypoxia in COPD raises erythropoietin and red-cell mass, a secondary polycythaemia distinct from the JAK2-driven polycythaemia vera.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Smoking, steroids and bone: COPD lowers bone density through smoking, systemic inflammation, inactivity and corticosteroid courses, fracturing the cortical bone and further impairing breathing.
- `connects-to` → **[NFE2L2](../../03-molecular/nfe2l2/README.md)** — Failing antioxidant defence: NRF2 (NFE2L2) drives the lung's antioxidant response, and its impairment in COPD leaves airways defenceless against cigarette-smoke oxidative stress—a therapeutic target.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Stalled repair: defective Wnt/β-catenin signalling blunts alveolar regeneration in emphysema, helping explain why destroyed lung tissue in COPD fails to repair.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Immune orchestration: dendritic cells accumulate in COPD airways, presenting smoke-modified antigens and driving the chronic T-cell inflammation and lymphoid follicles of advanced disease.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: cigarette smoke activates the NLRP3 inflammasome in airway cells, releasing IL-1β to amplify the chronic neutrophilic inflammation of COPD.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes and macrophages into the COPD lung, where their proteases and cytokines drive the alveolar destruction of emphysema.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic alveolar damage: CD8 T cells accumulating in COPD use perforin and granzyme to kill alveolar cells, contributing to the emphysematous loss of lung tissue.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Alveolar maintenance: VEGF sustains the alveolar-capillary network, and its loss drives the endothelial and epithelial apoptosis behind emphysematous alveolar destruction in COPD.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Neutrophilic airways: IL-17A drives the neutrophil recruitment and mucus hypersecretion of the chronic bronchitis phenotype of COPD, sustaining its corticosteroid-resistant airway inflammation.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Neutrophil alarmin: S100A8/A9 released by the neutrophils flooding the COPD airway amplifies inflammation and serves as a biomarker of disease activity and exacerbation.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Cigarette smoke activates EGFR on airway epithelium to drive goblet-cell metaplasia and MUC5AC overproduction, the mechanism behind the chronic mucus hypersecretion that defines the chronic-bronchitis phenotype of COPD.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Loss of VEGF survival signaling and oxidative injury trigger caspase-3-mediated apoptosis of alveolar endothelial and epithelial cells—the cell death that progressively destroys alveolar walls to produce emphysema.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Cigarette smoke and released DAMPs activate TLR4 on airway cells and macrophages, igniting the NF-κB-driven innate inflammation that sustains COPD airway disease and amplifies exacerbations triggered by infection.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Vagal acetylcholine acting on airway muscarinic receptors is the dominant reversible component of airflow obstruction in COPD, the target of the long-acting muscarinic antagonist (LAMA) bronchodilators central to its treatment.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Epinephrine and β2-agonist drugs relax airway smooth muscle through β2-adrenergic receptors, the long-acting β-agonist (LABA) inhalers that, with LAMAs, form the bronchodilator backbone of COPD therapy.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Glucocorticoids acting through the glucocorticoid receptor reduce exacerbations in the eosinophilic, exacerbation-prone subset of COPD, though steroid resistance limits their benefit in the predominantly neutrophilic disease.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — Type-2 cytokine IL-13 drives goblet-cell metaplasia and mucin overproduction in the eosinophilic COPD subset, contributing to the chronic-bronchitis phenotype and airway obstruction.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — CD8+ T cells and Th1 IFN-γ accumulate in COPD airways, driving the cytotoxic alveolar-wall destruction that produces emphysematous loss of lung parenchyma.
- `connects-to` → **[Pulmonary Surfactant](../../03-molecular/surfactant/README.md)** — Oxidant- and protease-mediated surfactant dysfunction in COPD raises surface tension in small airways, promoting their collapse on expiration and worsening air trapping and host-defense impairment.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped), activated by cigarette-smoke products and bacterial colonization, sustains the chronic airway inflammation of COPD.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Dysregulated mTOR signaling and impaired autophagy promote the senescence of airway and alveolar cells that underlies the accelerated lung aging and emphysema of COPD.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 and IFN-γ signaling through JAK-STAT (both already mapped) amplifies the inflammatory response of COPD and is an emerging anti-inflammatory therapeutic target.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-mTOR signaling (mTOR mapped) governs alveolar-epithelial survival and the cellular senescence implicated in emphysema and COPD progression.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EGFR-ERK-MAPK signaling (EGFR mapped) drives the airway mucus hypersecretion and epithelial remodeling of chronic bronchitis in COPD.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the macrophage-driven airway inflammation of COPD and serves as a biomarker of disease activity.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling drives the chronic airway inflammation and mucus responses central to the progression of COPD.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cigarette-smoke-induced DNA damage releases cytosolic DNA that engages cGAS-STING, amplifying the sterile inflammation and cellular senescence of COPD.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling underlies the antiviral response that drives the viral exacerbations of COPD.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the airway epithelial oxidative-stress defense and cellular senescence that drive the accelerated lung aging of COPD.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the small-airway fibrosis and remodeling of COPD.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β participates in the corticosteroid-insensitive inflammation and cellular senescence of COPD.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the airway inflammation and corticosteroid resistance of COPD.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, coupled to mitochondrial and autophagic quality control, is dysregulated in the cellular senescence and oxidative stress of COPD.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Dysregulated autophagy contributes to the cellular senescence and impaired clearance underlying the emphysema of COPD.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the airway epithelial and neutrophil responses of chronic obstructive pulmonary disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the airway and parenchymal inflammation of chronic obstructive pulmonary disease.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the smoking-linked epigenetic dysregulation of chronic obstructive pulmonary disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the airway leukocyte trafficking and lung-repair processes of chronic obstructive pulmonary disease.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the airway epithelial and innate immune responses of chronic obstructive pulmonary disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the airway inflammation of chronic obstructive pulmonary disease.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the airway-epithelial and immune gene programs of chronic obstructive pulmonary disease.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell-mediated inflammation of chronic obstructive pulmonary disease.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the airway inflammation and emphysema-related tissue remodeling of chronic obstructive pulmonary disease.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Secondary polycythaemia: chronic hypoxaemia in COPD drives erythropoietin (already mapped) and raises haemoglobin and haematocrit, a compensatory polycythaemia that increases blood viscosity and thrombotic risk.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac comorbidity: COPD strongly associates with cardiovascular disease, and troponin elevation from cor pulmonale, demand ischaemia and comorbid coronary disease marks the cardiac injury that contributes to its mortality.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Airway mucosal defence: reduced secretory IgA over the remodelled small airways of COPD weakens the mucosal barrier against inhaled microbes, promoting the bacterial colonisation and infective exacerbations that drive disease progression.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Respiratory acidosis: advanced COPD retains carbon dioxide, and the resulting proton accumulation produces the respiratory acidosis of type-2 respiratory failure, a hallmark of severe exacerbations that guides ventilatory support.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Smoking oxidative burden: cigarette smoke and the inflamed airway generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative stress (NRF2 already mapped) drives the tissue destruction and steroid resistance of COPD.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Refractory breathlessness: low-dose opioids acting on the mu-opioid receptor relieve the intractable breathlessness of advanced COPD, a mainstay of its palliative care despite the caution needed over respiratory depression.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Airway inflammatory eicosanoids: prostaglandins from the inflamed airway (IL-6, TNF and IL-1 already mapped) contribute to the inflammation and mucus of COPD, and prostaglandin E2 has complex effects on the airway smooth muscle and cough.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophilic phenotype: IL-5, with IL-13 (already mapped), drives the eosinophilic inflammation of a COPD subset, the blood eosinophil count guiding inhaled-corticosteroid (glucocorticoid receptor already mapped) use and anti-IL-5 biologic trials.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Hypoxic pulmonary hypertension: hypoxia (HIF-1-alpha already mapped) raises endothelin-1, constricting the pulmonary vasculature to produce the pulmonary hypertension and cor pulmonale (troponin already mapped) of advanced COPD.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 eosinophilic arm: IL-4, with IL-13 and IL-5 (already mapped), drives the type-2 eosinophilic inflammation of the COPD subset whose blood eosinophils guide the inhaled-corticosteroid (glucocorticoid receptor already mapped) response.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Cachexia and adipokines: the systemic inflammation (TNF and IL-6 already mapped) of COPD disturbs leptin and the adipokine balance, contributing to the muscle wasting and cachexia that worsen the prognosis of advanced disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron dysregulation: the hypoxia (HIF-1-alpha already mapped) and chronic inflammation of COPD disturb iron handling, producing either the anaemia of chronic disease or, with hypoxaemia, the secondary polycythaemia (erythropoietin already mapped).
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Elastin cross-linking: copper is the cofactor of lysyl oxidase that cross-links the elastin and collagen (already mapped) of the lung; the copper-dependent elastin repair is overwhelmed by the protease-antiprotease imbalance of the emphysema of COPD.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Cachexia adipokine: adiponectin, with leptin (already mapped), is disturbed in the cachexia and systemic inflammation (TNF and IL-6 already mapped) of advanced COPD, contributing to the muscle wasting.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Systemic inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the systemic inflammation (IL-6 already mapped) of COPD.
- `connects-to` → **[Asthma](../asthma/README.md)** — ACOS overlap: the asthma-COPD overlap shares the airway inflammation (the eosinophilic — IL-5 already mapped, and the neutrophilic — IL-17 already mapped) and the bronchodilator/ICS therapy.
- `connects-to` → **[Pulmonary arterial hypertension](../pulmonary-arterial-hypertension/README.md)** — Cor pulmonale: the chronic hypoxia (HIF and EPO already mapped) and the vascular remodelling (endothelin already mapped) of COPD cause the pulmonary hypertension and the cor pulmonale.
- `connects-to` → **[Smooth muscle cell](../../04-cellular/smooth-muscle-cell/README.md)** — Airway/vascular remodelling: the airway smooth muscle (acetylcholine already mapped — the bronchoconstriction) and the pulmonary-vascular smooth-muscle remodelling contribute to the airflow limitation and the hypertension of COPD.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 airway axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neutrophilic (already mapped) airway inflammation of COPD.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the airway inflammation, part of the mixed immune profile of COPD.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Antiviral exacerbation interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing, mediates the antiviral response to the respiratory-virus exacerbations of COPD.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^rabe-2017-gold-copd]: Rabe KF, Watz H. Chronic obstructive pulmonary disease. *Lancet.* 2017;389(10082):1931-1940. [doi:10.1016/S0140-6736(17)31222-9](https://doi.org/10.1016/S0140-6736(17)31222-9) · [PubMed 28513453](https://pubmed.ncbi.nlm.nih.gov/28513453/)
[^vestbo-2013-gold-strategy]: Vestbo J, Hurd SS, Agustí AG, et al. Global strategy for the diagnosis, management, and prevention of chronic obstructive pulmonary disease: GOLD executive summary. *Am J Respir Crit Care Med.* 2013;187(4):347-365. [doi:10.1164/rccm.201204-0596PP](https://doi.org/10.1164/rccm.201204-0596PP) · [PubMed 22878278](https://pubmed.ncbi.nlm.nih.gov/22878278/)
[^jones-2017-dupilumab-copd]: Bhatt SP, Rabe KF, Hanania NA, et al. Dupilumab for COPD with Type 2 Inflammation Indicated by Eosinophil Counts. *N Engl J Med.* 2023;389(3):205-214. [doi:10.1056/NEJMoa2303966](https://doi.org/10.1056/NEJMoa2303966) · [PubMed 37272521](https://pubmed.ncbi.nlm.nih.gov/37272521/)
