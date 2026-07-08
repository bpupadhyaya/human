---
schema: human-scale-entry/v1
id: asthma
name: Asthma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic airway hyperresponsiveness from Th2/ILC2 cytokines (IL-4, IL-5, IL-13), mast cell, and eosinophil activation; reversible bronchoconstriction and airway remodeling. ICS are first-line; dupilumab, mepolizumab, and omalizumab for severe type 2 asthma."
aliases: ["bronchial asthma", "allergic asthma", "eosinophilic asthma", "atopic asthma", "T2-high asthma"]
sources:
  - id: reddel-2022-gina
    type: peer-reviewed
    cite: "Reddel HK, Bacharier LB, Bateman ED, et al. Global Initiative for Asthma Strategy 2021: executive summary and rationale for key changes. Am J Respir Crit Care Med. 2022;205(1):17-35."
    doi: "10.1164/rccm.202109-2205PP"
    pmid: "34665667"
    url: "https://doi.org/10.1164/rccm.202109-2205PP"
  - id: wenzel-2012-asthma-phenotypes
    type: peer-reviewed
    cite: "Wenzel SE. Asthma phenotypes: the evolution from clinical to molecular approaches. Nat Med. 2012;18(5):716-725."
    doi: "10.1038/nm.2678"
    pmid: "22561835"
    url: "https://doi.org/10.1038/nm.2678"
  - id: castro-2018-dupilumab-asthma
    type: peer-reviewed
    cite: "Castro M, Corren J, Pavord ID, et al. Dupilumab efficacy and safety in moderate-to-severe uncontrolled asthma. N Engl J Med. 2018;379(26):2486-2496."
    doi: "10.1056/NEJMoa1804092"
    pmid: "30088505"
    url: "https://doi.org/10.1056/NEJMoa1804092"
cross_links:
  - target: 01-human/07-system/respiratory-system
    relation: targets
    note: "Asthma targets the lower respiratory system; allergen exposure → airway smooth muscle contraction → reversible obstruction; chronic inflammation → airway remodeling (smooth muscle hypertrophy, subepithelial fibrosis) → fixed obstruction in severe disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells are central acute asthma effectors; IgE cross-linking by allergen → degranulation → histamine, leukotrienes (LTC4), PGD2 → bronchoconstriction and vasodilation; tryptase and IL-5 amplify eosinophil recruitment; CRTh2+ mast cells sustain chronic airway inflammation."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 drives airway remodeling and neutrophilic asthma; elevated in severe disease; IL-6 trans-signaling promotes STAT3-dependent goblet cell differentiation and mucus hypersecretion; tocilizumab is under investigation for steroid-resistant neutrophilic asthma."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta1 drives asthma airway remodeling: subepithelial fibrosis, smooth muscle hypertrophy, and mucus gland hyperplasia; TGF-beta also suppresses Tregs and promotes Th17 in severe asthma; anti-TGF-beta strategies are under investigation for structural reversal."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Allergen-specific IgE binds FcεRI on airway mast cells → allergen cross-linking → degranulation → acute bronchoconstriction; omalizumab (anti-IgE mAb) binds free IgE → reduces FcεRI expression → 26-50% fewer exacerbations in severe allergic asthma."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "IL-4 drives Th2 airway inflammation, IgE production, and eosinophil recruitment in allergic asthma; type II receptor (IL-4Rα + IL-13Rα1) mediates mucus and AHR; dupilumab reduces severe asthma exacerbations by ~50% in patients with elevated eosinophils or FeNO."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "IL-5 drives eosinophilic airway inflammation; blood eosinophils ≥300/μL identifies biologic candidates; mepolizumab (MENSA 47% RRR) and benralizumab (CALIMA 28-36% RRR) block IL-5 or IL-5Rα to reduce exacerbations in severe eosinophilic asthma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "TSLP → DC and ILC2 activation upstream of the Th2/eosinophil cascade; tezepelumab (anti-TSLP mAb) reduced exacerbations 70% in NAVIGATOR trial — most effective severe asthma biologic across all eosinophil and IgE levels including T2-low patients."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 from damaged bronchial epithelium → ST2+ ILC2 and mast cells → IL-5/IL-13 → eosinophilia and mucus; works synergistically with TSLP and IL-25 as the three-alarmin cascade; itepekimab (anti-IL-33) reduced asthma exacerbations in Phase 2/3 trials."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Serum periostin >25 ng/mL identifies T2-high eosinophilic asthma regardless of blood eosinophil count; periostin from sub-epithelial fibroblasts (IL-13/IL-4 → STAT6 → POSTN) contributes to airway subepithelial fibrosis; periostin biomarker guided lebrikizumab trial design."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "A2BR on mast cells and airway smooth muscle → bronchoconstriction at high adenosine; AMP provocation test exploits this for asthma diagnosis; theophylline (adenosine antagonist + PDE inhibitor) is a bronchodilator; caffeine has mild adenosine-antagonist bronchodilator effect."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Asthma and COPD are the two great obstructive airway diseases and can overlap (ACOS): asthma is reversible, eosinophilic/Th2 inflammation in younger atopic patients, while COPD is largely irreversible, neutrophilic, smoking-driven—though many older patients share both."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Allergic asthma is a Th2 helper-T-cell disease: Th2 cells secrete IL-4, IL-5, and IL-13 that drive IgE class-switching, eosinophil recruitment, and mucus, so the type-2 inflammation they coordinate is the target of biologics like dupilumab and anti-IL-5 agents."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Asthma and atopic dermatitis are linked stages of the atopic march: many children begin with eczema and food allergy in infancy, then progress to allergic rhinitis and asthma, reflecting shared type-2 immunity and barrier defects—and both now respond to dupilumab."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Airway smooth muscle is the effector of asthma's airflow obstruction: hyperresponsive smooth muscle contracts in response to triggers, narrowing bronchi (wheeze), and over time hypertrophies—so bronchodilators relax it while bronchial thermoplasty ablates it."
  - target: 02-pathogen/01-viruses/respiratory-syncytial-virus
    relation: connects-to
    note: "Early respiratory syncytial virus infection is linked to asthma: severe RSV bronchiolitis is associated with later wheezing, and viral respiratory infections remain the commonest trigger of asthma exacerbations—tying a childhood virus to chronic airway disease."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity defines a distinct, harder-to-treat asthma phenotype: excess weight restricts lung mechanics and adipose-derived inflammation alters airway biology, so obese asthmatics often have more symptoms and worse control—and weight loss improves the disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "IL-13 drives the airway changes of asthma: this type 2 cytokine, with IL-4, fuels IgE production, mucus hypersecretion and airway hyperresponsiveness, so dupilumab (blocking IL-4/IL-13 signaling) is a mainstay biologic for type 2-high asthma."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Asthma remodels the lung over time: repeated bronchoconstriction and inflammation thicken airway smooth muscle and basement membrane, so uncontrolled asthma can leave fixed obstruction—turning a reversible disease into permanent lung damage."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells initiate the allergic asthma response: they sample inhaled allergens and prime naive T cells toward the Th2 program, sitting upstream of the IgE and eosinophil cascade—so they set whether the airway becomes sensitized in the first place."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine is a frontline mediator of the asthmatic airway: released when allergen cross-links IgE on mast cells, it triggers rapid bronchoconstriction, mucus, and vascular leak—the immediate-phase response, though antihistamines help asthma less than allergic rhinitis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Not all asthma is eosinophilic: a neutrophil-driven, type-2-low phenotype causes severe, often steroid-resistant disease, so recognizing neutrophilic asthma matters because it responds poorly to the inhaled corticosteroids and anti-IL-5 biologics that target eosinophils."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Asthma reflects how the immune system is wired: a type-2 (Th2) skew underlies allergic asthma, and the hygiene hypothesis links reduced early microbial exposure to this allergic tilt—so asthma is as much an immune-regulation disorder as an airway one."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Exhaled nitric oxide is a key asthma biomarker: airway eosinophilic inflammation raises FeNO (fractional exhaled NO), so measuring it gauges Type-2 inflammation, predicts steroid response and helps tailor and monitor asthma therapy."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D status influences asthma: deficiency is linked to more frequent exacerbations and poorer control, and as an immune modulator it supports regulatory responses—so vitamin D is studied as add-on prevention, especially in deficient patients."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Asthma reflects failed regulatory T-cell tolerance: Tregs normally restrain allergic responses to inhaled antigens, so when they are deficient or dysfunctional, the Th2 inflammation behind allergic asthma goes unchecked—a target for allergen immunotherapy."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Asthma's cornerstone controller mimics cortisol: inhaled corticosteroids damp the airway's eosinophilic, Th2 inflammation, preventing the attacks rather than just relieving them—the single most important long-term asthma therapy."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Asthma's rescue works through adrenaline's receptors: β2-agonists like albuterol (and epinephrine in anaphylaxis) relax airway smooth muscle within minutes, reversing the bronchoconstriction of an acute attack."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Asthma's bronchoconstriction runs on calcium: airway smooth muscle contracts when calcium floods its cells, so the wheeze of an attack is a calcium-driven squeeze—and relaxing that contraction is what bronchodilators achieve."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium relaxes the asthmatic airway: intravenous magnesium sulfate is given in severe attacks because it blocks calcium-driven smooth-muscle contraction and bronchodilates when standard inhalers fall short."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "A severe asthma attack ultimately starves the blood of oxygen: as airways narrow and air-trapping worsens, gas exchange fails and oxygen falls—rising CO2 in a tiring patient is an ominous sign of impending respiratory arrest."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells stoke severe and viral asthma: CD8 T cells, especially during respiratory-virus exacerbations, add to the Th2 inflammation and tissue damage, broadening the immune picture beyond the classic allergic pathway."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Treating an asthma attack can drop potassium: high-dose beta-agonists drive potassium into cells, so the salbutamol that opens airways may cause hypokalemia that needs watching in severe attacks."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Asthma is one step of the atopic march, often heralded by eczema: the same Th2/IgE allergy that inflames the skin in atopic dermatitis later inflames the airways, linking skin and lung in one allergic diathesis."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Long-standing asthma scars the airway: chronic inflammation lays down subepithelial fibrosis and thickens the wall, part of the remodeling that turns reversible wheeze into fixed, hard-to-treat airflow limitation."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons help corner asthma: the chest X-ray shows hyperinflation and excludes mimics, CT reveals mucus plugging and wall thickening, and measuring the light-based marker of exhaled nitric oxide gauges the eosinophilic inflammation guiding treatment."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Eicosanoids drive the asthmatic airway: leukotrienes and prostaglandins released by mast cells clamp the bronchi shut and recruit inflammation, so leukotriene-blocking drugs ease asthma — and aspirin, by skewing this pathway, can trigger a severe attack."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Severe chronic asthma can strain the heart: sustained airway obstruction and low oxygen raise pressure in the lung's vessels, forcing the right ventricle to labor toward cor pulmonale, while high-dose beta-agonists quicken the pulse."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Long-standing asthma reshapes the airway wall: repeated inflammation lays down extra collagen beneath the epithelium, thickening the basement membrane in the remodeling that can fix some obstruction beyond what inhalers reverse."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Vagal acetylcholine tightens the airways: released onto muscarinic receptors it constricts bronchial smooth muscle and drives mucus, which is why anticholinergics like ipratropium and tiotropium relax the airways as add-on therapy."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Fat shapes a distinct asthma: in obese-asthma the adipocyte's inflammatory adipokines drive a non-eosinophilic, often steroid-resistant disease, one reason weight loss can improve control where inhalers fall short."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies now treat severe asthma at its source: omalizumab mops up IgE, mepolizumab blocks IL-5 to starve eosinophils, and dupilumab blocks IL-4/13 signaling — monoclonal antibodies that quiet the type-2 inflammation when inhalers cannot."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hormones modulate the airways: asthma often shifts with the menstrual cycle (perimenstrual asthma) and changes in pregnancy — worsening in about a third of women — so control is actively managed through gestation to protect mother and fetus."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Early-life microbes set the allergic thermostat: a less diverse infant gut microbiome, shaped by birth mode, antibiotics, and environment, tilts the immune system toward the type-2 responses of asthma — the core of the hygiene hypothesis."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "A mould can hijack the asthmatic airway: sensitization to Aspergillus drives allergic bronchopulmonary aspergillosis, where the fungus colonizing the bronchi triggers fierce eosinophilic inflammation, mucus plugging and bronchiectasis atop the asthma."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Severe eosinophilic asthma can herald a vasculitis: eosinophilic granulomatosis with polyangiitis (Churg-Strauss) begins with adult-onset asthma and blood eosinophilia before progressing to an ANCA-associated small-vessel vasculitis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Not all asthma is type-2: a neutrophilic, often steroid-resistant phenotype is driven by Th17 cells and IL-17A rather than eosinophils, explaining why some severe asthmatics respond poorly to the usual eosinophil-targeting biologics."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Long-standing asthma remodels the airway wall: fibroblasts laying down subepithelial collagen thicken and stiffen the bronchi, a structural scarring that can fix airflow limitation even when the inflammation is controlled."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "A kinin tightens the airways: bradykinin generated in the inflamed bronchi constricts smooth muscle and stimulates mucus and cough, contributing to airway hyperreactivity — and explaining the cough that ACE inhibitors, which raise bradykinin, can provoke."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "The inflamed lung is more vulnerable to a classic pathogen: asthmatics carry a higher risk of invasive pneumococcal disease, which is why pneumococcal vaccination is recommended to protect airways already primed for trouble."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is the airway's inflammation switch: allergens, viruses and pollutants activate NF-κB in bronchial epithelium to pour out the cytokines and chemokines of an asthma attack, and quieting it is much of how inhaled steroids work."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 underlies the steroid-resistant disease: in neutrophilic and severe asthma, IL-6/IL-17-driven STAT3 signaling sustains airway inflammation that responds poorly to corticosteroids, marking it as a target in hard-to-treat cases."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Severe disease tilts the blood toward clotting: asthma — especially severe, exacerbating disease and long courses of oral steroids — is linked to a higher risk of pulmonary embolism and deep-vein thrombosis."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Its inhalers seed oral thrush: inhaled corticosteroids deposit on the oropharynx and locally suppress immunity, allowing Candida to overgrow into oral candidiasis — the reason spacers and mouth-rinsing are advised after each dose."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Steroid courses thin the bone: repeated oral-corticosteroid bursts for exacerbations, and high-dose inhaled steroids in severe asthma, accelerate bone loss and raise the long-term risk of osteoporotic fracture."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Breathlessness and anxiety feed each other: asthma carries high rates of anxiety, and the fear of an attack — plus the overlap of hyperventilation with asthma symptoms — can worsen perceived control and trigger exacerbations."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Its rescue steroid courses raise blood sugar: the repeated oral-corticosteroid bursts that severe or poorly controlled asthma requires induce insulin resistance and can precipitate steroid-induced diabetes."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Chronic breathlessness and limitation weigh on mood: alongside its well-known anxiety, asthma carries elevated depression, driven by activity restriction, poor sleep and the burden of uncontrolled symptoms."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Severe asthma tracks with cerebrovascular risk: the systemic Th2 and eosinophilic inflammation of asthma, especially severe late-onset disease, is associated in cohort studies with a modestly raised risk of stroke."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Breathlessness and panic feed each other: the air hunger of an asthma attack can trigger panic, and panic-driven hyperventilation in turn worsens bronchospasm, so the two disorders are strongly intertwined."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its steroids reach far beyond the lungs: repeated oral corticosteroid courses and high-dose inhaled steroids for asthma can suppress the adrenal axis and, in children, slow growth, an endocrine cost of control."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Respiratory viruses ignite attacks: influenza and other viral infections are leading triggers of asthma exacerbations, inflaming the airways, so annual vaccination is advised for people with asthma."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Nerves set bronchial tone: parasympathetic vagal cholinergic signalling constricts the airways and amplifies reflex bronchospasm, which is why anticholinergic bronchodilators relieve attacks."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Reflux from below stokes the airway: gastro-oesophageal reflux is a common asthma comorbidity and trigger, provoking bronchospasm through microaspiration and a vagal oesophago-bronchial reflex."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its drugs and the heart intersect: beta-blockers can precipitate bronchospasm in asthma, while inhaled and systemic beta-agonists cause tachycardia, tremor and, in overuse, arrhythmia."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It sits in the atopic spectrum: asthma travels with eczema and urticaria through shared type 2 inflammation, and anti-IgE omalizumab treats both asthma and chronic urticaria."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its steroid courses weaken bone and muscle: repeated oral corticosteroid bursts for exacerbations cause osteoporosis and proximal steroid myopathy over time."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Severe eosinophilic disease can attack the kidney: difficult eosinophilic asthma can herald eosinophilic granulomatosis with polyangiitis, which causes a pauci-immune glomerulonephritis."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Inhaled steroids are the controller: they suppress airway inflammation as the foundation of asthma maintenance, with systemic steroids for acute severe attacks."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "Some drugs can trigger an attack: non-selective beta-blockers can provoke bronchospasm and are used with caution or avoided in asthma."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Aspirin can set off asthma: in aspirin-exacerbated respiratory disease (Samter's triad), NSAIDs trigger severe bronchospasm in asthmatics with nasal polyps."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Biologics for severe type-2 disease: monoclonal antibodies against IgE (omalizumab), IL-5 (mepolizumab), IL-4Rα (dupilumab) and TSLP (tezepelumab) control severe eosinophilic and allergic asthma that escapes inhaled steroids."
  - target: 01-human/05-tissue/lung-slice
    relation: connects-to
    note: "It remodels the airway wall: chronic asthma thickens airway smooth muscle, deposits subepithelial collagen and fills the lumen with mucus — the bronchial-wall remodelling that turns reversible bronchospasm into fixed airflow obstruction."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "A contrasting chronic airway disease: asthma is reversible bronchospasm of type-2 inflammation, whereas cystic fibrosis is a genetic defect of mucus clearance causing infection and bronchiectasis — though they overlap when Aspergillus drives ABPA in both."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Cardiac asthma mimics it: left heart failure causes wheeze and breathlessness from pulmonary congestion that imitate an asthma attack, a key differential—and the beta-blockers used for heart failure can themselves provoke bronchospasm."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Its drugs and the heart's rhythm: beta-2 agonists and theophylline used in asthma can provoke tachyarrhythmias, while the beta-blockers acting on cardiac conduction are avoided in asthma because they trigger bronchospasm."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Chronic inflammation carries cardiovascular cost: severe and late-onset asthma is associated with increased atherosclerotic cardiovascular disease, driven by systemic inflammation and the metabolic effects of long-term corticosteroids."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Allergic sensitisation: the allergen-specific IgE that drives allergic asthma is class-switched by B cells in germinal centres, under IL-4/IL-13 and follicular helper T-cell help."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The eosinophil supply line: allergic asthma's IL-5 drives eosinophil production in the bone marrow, and anti-IL-5 biologics like mepolizumab cut off this source to control eosinophilic asthma."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "A surprising non-risk: well-controlled type-2-high allergic asthma did not raise COVID-19 severity—inhaled corticosteroids and lower airway ACE2 expression may even protect—unlike most other chronic lung diseases."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Clinical interplay: although type-2 asthma did not worsen COVID-19, severe COVID can present with wheeze and bronchospasm, and the pandemic reshaped asthma care toward inhaled-steroid maintenance and remote monitoring."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Neural control of the airway: vagal cholinergic tone drives bronchoconstriction (the target of anticholinergics like tiotropium), and sensory-nerve neurogenic inflammation amplifies the airway hyperresponsiveness of asthma."
  - target: 01-human/03-molecular/surfactant
    relation: connects-to
    note: "Surfactant in small-airway closure: airway surfactant becomes dysfunctional in asthma, contributing to the mucus plugging and small-airway collapse that drive severe and fatal attacks."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Airway remodelling: VEGF drives the angiogenesis and vascular remodelling of the chronically inflamed asthmatic airway wall, contributing to fixed airflow obstruction."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obese-asthma phenotype: leptin from excess adipose tissue promotes airway inflammation and links obesity to a distinct, often steroid-resistant asthma phenotype."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neutrophilic axis: IL-1β and inflammasome activation characterise the neutrophilic, non-Th2, steroid-resistant form of severe asthma, distinct from eosinophilic disease."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Severe-asthma inflammation: TNF-α drives the neutrophilic inflammation and airway hyperresponsiveness of severe, steroid-resistant asthma."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Cell recruitment: CCL2 draws monocytes and other inflammatory cells into the asthmatic airway, contributing to the chronic inflammation and remodelling."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1/neutrophilic asthma: IFN-γ from Th1 cells characterises the non-eosinophilic, often steroid-resistant asthma endotype, contrasting with the Th2 form."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Mast-cell effector: stem-cell factor signalling through KIT maintains the airway mast cells whose IgE-triggered degranulation releases the histamine and leukotrienes driving the acute bronchoconstriction of allergic asthma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine signalling: the Th2 cytokines IL-4, IL-5 and IL-13 signal through JAK-STAT, making JAK inhibitors an emerging strategy to block multiple type-2 pathways at once in asthma."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Neurogenic inflammation: substance P released from airway sensory nerves causes bronchoconstriction, mucus secretion and plasma extravasation, the neural arm of asthmatic airway inflammation and cough."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Neutrophilic endotype: S100A8/A9 from airway neutrophils marks the non-type-2, neutrophilic asthma that responds poorly to corticosteroids and eosinophil-targeted biologics, defining a distinct endotype that needs different therapeutic strategies."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Smooth-muscle remodelling: endothelin-1 from airway epithelium is a potent bronchoconstrictor and mitogen for airway smooth muscle, contributing to the smooth-muscle hyperplasia and subepithelial fibrosis of asthmatic airway remodelling."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Obese-asthma phenotype: low adiponectin in obesity removes an anti-inflammatory brake on the airways, part of why the obese-asthma phenotype is more severe and steroid-resistant, complementing the pro-inflammatory leptin of the same metabolic axis."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Severe non-T2 asthma: the NLRP3 inflammasome and IL-1β drive the neutrophilic, type-2-low inflammation of severe steroid-resistant asthma, a phenotype distinct from the eosinophilic IL-4/5/13 axis already mapped."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Tolerance brake: regulatory IL-10 from regulatory T cells normally restrains airway allergic inflammation, and deficient IL-10-mediated tolerance permits the type-2 response of asthma — the principle behind allergen immunotherapy."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate gene-environment axis: TLR4 sensing of microbial and pollutant exposures shapes asthma risk and exacerbations, the molecular substrate of the hygiene-hypothesis interaction between environment and airway immunity."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Controller mechanism: inhaled corticosteroids act through the glucocorticoid receptor to suppress airway inflammation, the cornerstone asthma controller, with steroid resistance marking severe neutrophilic disease."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Exacerbation signalling: TLR sensing of viruses and allergens (TLR4 mapped) signals through MyD88 to NF-κB (mapped), driving the innate inflammation behind asthma exacerbations."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Airway remodeling: growth-factor and TGF-β signalling (mapped) through the MAPK-ERK cascade drives the airway-smooth-muscle proliferation and remodeling of chronic asthma."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Smooth-muscle proliferation: mTOR-dependent metabolism and airway-smooth-muscle proliferation contribute to the bronchial hyperreactivity and airway remodelling of asthma."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Airway oxidative defence: NRF2 antioxidant defence protects the airway epithelium from the oxidative stress of allergic inflammation and pollutant exposure, a pathway impaired in severe asthma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Neutrophilic phenotype: IL-23 sustains the Th17 response (IL-17A already mapped) that drives the neutrophilic, often steroid-resistant phenotype of severe asthma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes eosinophil recruitment, airway inflammation and the subepithelial remodelling that characterises chronic asthma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the airway smooth-muscle hyperplasia and subepithelial fibrosis of airway remodelling in asthma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling underlies the antiviral Th1 response that drives virus-induced exacerbations of asthma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate airway smooth-muscle and T-cell programs and influence the glucocorticoid responsiveness that varies across asthma phenotypes."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoxic inflamed airway promotes angiogenesis and the airway remodeling of chronic asthma."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA, PI3Kδ) signaling drives airway inflammation, smooth-muscle proliferation, and the corticosteroid insensitivity of severe asthma."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "AKT downstream of PI3K (PIK3CA already mapped) drives airway smooth-muscle proliferation and the survival of Th2 cells in asthma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven airway inflammation and remodeling of asthma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the innate inflammatory activation of virus-induced asthma exacerbations."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the airway smooth-muscle and immune-cell metabolism of asthma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the airway epithelial and eosinophil responses and airway remodeling of asthma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of the IgE receptor (FcεRI) drives the mast-cell activation of allergic asthma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the airway inflammation of asthma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the Th2 and airway responses of asthma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 (C3a) participates in the airway inflammation and hyperresponsiveness of asthma."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the airway leukocyte recruitment and remodeling of asthma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the airway immune and structural gene programs of asthma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of the Type 2 immune response of asthma."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex-hormone modulation: asthma prevalence and severity shift at puberty and across the menstrual cycle, and estrogen modulates airway inflammation and smooth-muscle tone, underlying the female predominance of adult asthma and premenstrual exacerbations."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Anaphylatoxins: the complement fragments C3a and C5a (C3 already mapped) generated in allergic airways amplify mast-cell and eosinophil recruitment and smooth-muscle contraction, bridging innate complement to the type-2 inflammation of asthma."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal barrier: secretory IgA at the airway surface shapes the response to inhaled allergens and microbes, and altered IgA production is associated with allergic sensitisation and asthma susceptibility in early life."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Theophylline and oxidative stress: theophylline, a methylxanthine bronchodilator and phosphodiesterase inhibitor, is metabolised via xanthine oxidase, whose reactive oxygen species also contribute to the airway oxidative stress of asthma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Allergen presentation: MHC class II presentation of inhaled allergens by airway dendritic cells drives the Th2 sensitisation (IL-4/IL-13 already mapped) of allergic asthma, and HLA associations contribute to susceptibility."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Airway macrophages: alveolar and airway macrophages, polarised toward an alternatively activated phenotype in type-2 asthma, contribute to the inflammation, remodelling and impaired resolution of the disease."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Respiratory acidosis: in acute severe asthma a rising carbon dioxide as the patient tires produces respiratory acidosis, and the accumulation of protons is an ominous sign heralding respiratory failure and the need for ventilation."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Neurogenic inflammation: CGRP released from airway sensory nerves, with substance P (already mapped), contributes to the neurogenic inflammation, vasodilation and cough of asthma, part of the neuro-immune dimension of the disease."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac strain: high-dose beta-agonists and theophylline cause tachycardia and, with the hypoxaemia of acute severe asthma, can strain the heart, and troponin elevation may mark the myocardial stress of a near-fatal attack."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant defence: selenium is essential for the glutathione peroxidases that quench airway oxidative stress (xanthine oxidase already mapped), and low selenium status has been linked to asthma and worse airway inflammation."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Obesity-asthma phenotype: the adipokine resistin, with leptin and adiponectin (already mapped), links the adipose tissue of obesity to airway inflammation, part of the distinct obese-asthma phenotype that responds poorly to steroids."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Airway surface liquid: chloride transport hydrates the airway surface liquid and mucus, and its disturbance contributes to the thick mucus plugging of the airways (smooth muscle already mapped) in severe and fatal asthma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Viral exacerbation: the deficient epithelial type-I interferon response to rhinovirus in asthma permits the viral respiratory infections that are the commonest trigger of acute asthma exacerbations."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Obese-asthma metabolism: the insulin resistance of the obese-asthma phenotype (leptin, adiponectin and resistin already mapped) links the metabolic dysfunction of obesity to the airway inflammation and the poor steroid response."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and airway immunity: zinc is an antioxidant and immune-modulating trace metal, and its deficiency is associated with worse asthma control and heightened airway inflammation."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Allergen sensitisation: the airway dendritic cells sample the inhaled allergen and prime the Th2 (already mapped) response, initiating the allergic sensitisation of asthma."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Asthma-COPD overlap: the asthma-COPD overlap (ACO) shares features of both; the neutrophilic (already mapped), less steroid-responsive asthma phenotype resembles COPD."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron and inflammation: the IL-6-driven (already mapped) hepcidin and the airway iron dysregulation are linked to the severe, neutrophilic (already mapped) asthma and the anaemia of chronic inflammation."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "IgE class-switching: the B cells class-switch to the allergen-specific IgE (already mapped) under the IL-4 and IL-13 (already mapped), driving the allergic sensitisation of asthma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 counter-arm: IL-12 polarises the Th1 (IFN-γ already mapped) response that counter-regulates the dominant Th2 (IL-4, IL-5 and IL-13 already mapped) axis of allergic asthma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate antiviral surveillance: the NK cells (perforin already mapped) participate in the antiviral response to the respiratory viruses that trigger the asthma exacerbations."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "IgE plasma cells: the plasma cells secrete the allergen-specific IgE (already mapped) that arms the mast cells (already mapped) of allergic asthma."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Type-2 IL-31: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, is part of the broader type-2 immune response and the atopic itch shared across the atopic diseases of the allergic-asthma patient."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "Atopic-march overlap: asthma shares the type-2 (IL-4, IL-5, IL-13 and TSLP already mapped) immunity with prurigo nodularis, another atopic-spectrum type-2 disease treated with the shared biologics."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Anaphylatoxin receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) is part of the complement/anaphylatoxin contribution to the airway inflammation of asthma."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelet in airway: the platelets, via the platelet-eosinophil aggregates and the release of mediators, contribute to the airway inflammation and remodelling of asthma."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: connects-to
    note: "Viral exacerbation: the influenza A virus (with RSV already mapped) is a respiratory-viral trigger of the acute exacerbations of asthma."
---

# Asthma

## Overview

**Asthma** is a **heterogeneous chronic inflammatory disease of the airways** characterized by variable airflow obstruction, bronchial hyperresponsiveness (BHR), and airway remodeling. It is defined by episodic symptoms — **wheeze, cough, chest tightness, and dyspnea** — that vary over time and are associated with expiratory airflow limitation that is (at least partially) reversible spontaneously or with treatment [^gina-2023-asthma].

Asthma affects approximately **339 million people worldwide** (WHO 2019) and is the most common chronic respiratory disease in children. It accounts for ~450,000 deaths/year and enormous healthcare costs. The global prevalence has increased over 50 years, particularly in Westernized, industrialized countries — consistent with the hygiene hypothesis (insufficient early microbial exposure → impaired immune maturation → allergic sensitization).

**Clinical heterogeneity — asthma endotypes [^wenzel-2012-asthma-phenotypes]:**
- **Type 2 (T2-high) asthma (~50% of adults):** Eosinophilic, allergic, or mixed; driven by Th2/ILC2 cytokines (IL-4, IL-5, IL-13), IgE, and eosinophils; highest biomarker activity (blood eosinophils ≥300/μL, FeNO ≥25 ppb, periostin, total IgE); best biologic candidates
  - *Allergic asthma:* IgE-mediated; early sensitization (house dust mite, cat, mold, cockroach, pollen); atopic triad (asthma + allergic rhinitis + atopic dermatitis); anti-IgE (omalizumab) effective
  - *Late-onset eosinophilic:* Non-allergic; often adult-onset, severe, corticosteroid-responsive but corticosteroid-requiring; anti-IL-5/IL-5R (mepolizumab, benralizumab) most effective
- **Type 2-low (non-T2) asthma (~50% of adults):**
  - *Neutrophilic asthma:* Smoking-related, obese, occupational; IL-8, IL-17, IL-6 driven; corticosteroid-insensitive; no approved biologic
  - *Paucigranulocytic asthma:* Minimal airway inflammation; BHR driven by smooth muscle abnormalities and autonomic dysfunction

**Severity and control:**
- **Intermittent:** Daytime symptoms ≤2 days/week, nighttime awakenings ≤2/month, no daily medication required
- **Mild persistent:** Daytime symptoms >2 days/week; GINA Step 2
- **Moderate persistent:** Daily symptoms; nighttime awakenings >1/week; Step 3-4
- **Severe persistent:** Continuous daily symptoms; frequent exacerbations; Step 5; biologic candidates

## Structure

### Airway pathology

**Normal airway architecture:** Pseudostratified ciliated columnar epithelium + goblet cells; lamina propria with mast cells and sparse eosinophils; smooth muscle layer; submucosal glands; cartilaginous rings (large airways).

**Asthmatic airway changes:**
- **Epithelial damage:** Allergen proteases (HDM Der p 1 = cysteine protease) cleave tight junction proteins → epithelial barrier disruption → allergen entry → DC sampling → sensitization; fragile asthmatic epithelium → shed epithelial cells in sputum (Creola bodies)
- **Goblet cell hyperplasia:** IL-13 → JAK1/STAT6 → MUC5AC transcription → mucus hypersecretion → mucus plug formation → mucoid impaction in fatal asthma
- **Subepithelial fibrosis:** TGF-beta → fibroblast-to-myofibroblast transition → collagen III/V deposition below basement membrane → irreversible structural narrowing in severe chronic asthma
- **Smooth muscle hypertrophy/hyperplasia:** IL-4, IL-13, and TGF-beta → increased airway smooth muscle mass → increased contractile capacity → enhanced BHR
- **Increased vascularity:** VEGF-driven angiogenesis in asthmatic airway wall → increased edema and airway wall thickness → narrowed lumen

### T2 immune cascade

**Sensitization phase (first exposure):**
1. Allergen inhaled → epithelial alarm signals (TSLP, IL-25, IL-33) released
2. TSLP/IL-33 → activate DCs and ILC2 (type 2 innate lymphoid cells)
3. ILC2 → IL-5 (eosinophil recruitment) + IL-13 (smooth muscle and goblet cell activation) → innate T2 amplification
4. DCs migrate to mediastinal LN → present processed allergen peptides to naive CD4+ T cells → IL-4 (from mast cells/basophils) → Th2 polarization → IL-4, IL-5, IL-13, IL-9 cytokine production
5. Th2-driven B cells switch to IgE class → allergen-specific IgE → binds FcεRI on mast cells and basophils

**Effector phase (re-exposure):**
1. Allergen → cross-links IgE on mast cells → FcεRI → Syk kinase → PLC-gamma → Ca²⁺ → mast cell degranulation:
   - **Pre-formed mediators:** Histamine (bronchoconstriction, vasodilation), tryptase (pro-inflammatory), heparin
   - **Newly synthesized:** LTC4 → LTD4/LTE4 (cysteinyl leukotrienes, potent bronchoconstrictors → montelukast target), PGD2 (CRTh2 on Th2/eosinophils → amplification)
   - **Cytokines:** TNF-alpha, IL-5, IL-13 (late phase)
2. **Acute phase (0-2h):** Bronchoconstriction (histamine, LTC4-D4), airway edema, mucus secretion
3. **Late phase (4-12h):** Eosinophil recruitment (IL-5, eotaxin/CCL11 → CCR3) → eosinophil degranulation → MBP, ECP → epithelial damage; sustained inflammation → BHR
4. **Chronic phase:** Persistent eosinophilia, Th2 cytokine production, airway remodeling

## Function

### Clinical presentation

**Symptoms:**
- Episodic wheeze (high-pitched expiratory) — classic symptom; also productive cough, dyspnea, chest tightness
- **Triggers:** Allergens (HDM, pollen, pet dander), respiratory viruses (RV → ~80% of childhood and ~40% of adult exacerbations), exercise (especially cold air), NSAIDs (aspirin-exacerbated respiratory disease, AERD), tobacco smoke, occupational exposures, cold air, emotional stress
- **Nocturnal worsening:** Circadian decrease in cortisol and epinephrine + supine posture (increased vagal tone, decreased FRC) → nocturnal symptoms

**Objective measures:**
- **Spirometry:** FEV1/FVC <0.7 or <LLN (post-bronchodilator); significant bronchodilator reversibility (≥12% AND ≥200 mL increase in FEV1 after SABA) — hallmark of asthma
- **Peak expiratory flow (PEF) variability:** >10% diurnal variation; useful for home monitoring
- **FeNO (fractional exhaled NO):** ≥25 ppb = eosinophilic airway inflammation; correlates with ICS responsiveness; used to guide therapy step-up
- **Bronchoprovocation (methacholine challenge):** PC20 ≤16 mg/mL = BHR; used when spirometry and symptoms don't match; high sensitivity, moderate specificity for asthma
- **Allergy testing:** Skin prick test or specific IgE (ImmunoCAP) to identify sensitizing allergens; guides allergen avoidance and immunotherapy decisions

**Acute severe asthma (status asthmaticus):**
- SpO2 <92%, RR >25, HR >120, unable to complete sentences, PEF <50% predicted, silent chest → imminent respiratory failure
- Management: High-flow O2, continuous nebulized SABA + ipratropium, IV corticosteroids (methylprednisolone 40-80 mg), IV magnesium sulfate (1-2g over 20 min → smooth muscle relaxation), CPAP/HFNO; intubation if failing → severe auto-PEEP risk
- **Risk factors for fatal asthma:** Prior near-fatal attack, ≥2 hospitalizations/year, reliance on OCS, poor perception of severity, psychiatric comorbidity, under-prescription of ICS

## Pathology

### Diagnosis

**GINA definition:** Pattern of symptoms (variable wheeze, cough, dyspnea, chest tightness) + variable expiratory airflow limitation (spirometry, PEF monitoring).

**Differential diagnosis:** COPD (irreversible obstruction, smoking, age >40), vocal cord dysfunction (inspiratory stridor, young women, exercise-triggered, responds to speech therapy), cardiac asthma (heart failure), bronchiectasis, eosinophilic bronchitis, foreign body.

### Treatment [^castro-2018-dupilumab-asthma]

**GINA stepwise approach:**

*Step 1-2 (mild asthma):*
- Low-dose ICS (budesonide 200 μg/day, fluticasone propionate 100-200 μg/day) — cornerstone of all asthma therapy; suppresses Th2 eosinophilic inflammation, reduces exacerbations by ~50%, reduces BHR; no disease modification (relapse on cessation)
- SABA (salbutamol/albuterol) PRN for symptom relief; overuse predicts poor control
- GINA 2019 update: ICS-formoterol (low-dose budesonide-formoterol) PRN preferred over SABA alone for mild asthma (SYGMA 1/2 trials)

*Step 3-4 (moderate-severe):*
- Low-dose ICS + LABA (salmeterol, formoterol): Superior to ICS alone and ICS dose escalation; standard Step 3 therapy
- Medium-high dose ICS + LABA: Step 4; add leukotriene receptor antagonist (LTRA, montelukast) or tiotropium (LAMA) as add-on
- **SMART (single inhaler maintenance and reliever therapy):** ICS-formoterol (budesonide-formoterol/Symbicort or beclomethasone-formoterol) as both maintenance AND reliever → superior to ICS+LABA maintenance with SABA PRN; reduces severe exacerbations 30-50%; endorsed by GINA 2019+ as preferred Step 3-4 strategy

*Step 5 — Severe/refractory asthma:*
- High-dose ICS + LABA + biologic; oral corticosteroid (OCS) should be avoided if possible (OCS toxicity: adrenal suppression, osteoporosis, DM, cardiovascular disease, cataracts)

**Biologics for severe asthma (T2-high):**
- **Omalizumab (Xolair, anti-IgE):** Binds free IgE → reduces FcεRI expression on mast cells → less IgE-mediated activation; indicated: severe allergic asthma (total IgE 30-1500 IU/mL, skin-test positive, ≥12y); reduces exacerbations ~26-50%; also prevents severe allergic reactions/anaphylaxis
- **Mepolizumab (Nucala, anti-IL-5):** Reduces eosinophil counts by ~80-90%; indicated: severe eosinophilic asthma (blood eos ≥150/μL at initiation or ≥300/μL in prior year); 47% reduction in exacerbations (DREAM/MENSA trials); SC monthly
- **Benralizumab (Fasenra, anti-IL-5Ra/FcgammaRIII):** Direct eosinophil depletion via ADCC; near-complete eosinophil elimination; SC Q8W (after 3 Q4W doses); non-inferior/superior to mepolizumab in indirect comparison
- **Dupilumab (Dupixent, anti-IL-4Ra):** Blocks both IL-4 and IL-13 signaling (shared receptor subunit); QUEST trial: 46% exacerbation reduction vs. placebo at eos ≥300/μL or FeNO ≥25 ppb; also approved atopic dermatitis, CRS with NP, COPD, EoE; broadest T2 disease coverage; SC biweekly [^castro-2018-dupilumab-asthma]
- **Tezepelumab (Tezspire, anti-TSLP):** Targets TSLP (upstream of Th2/ILC2 activation) → reduces eosinophils, ILC2s, and T2 biomarkers; NAVIGATOR trial: 70% exacerbation reduction in patients with high blood eos AND 56% in those with <300/μL — broadest efficacy regardless of eos; SC monthly
- **Itepekimab (Regn3500, anti-IL-33):** PHASE 2 data promising; targets IL-33 upstream alarmin

**Allergen immunotherapy:**
- **Subcutaneous (SCIT) or sublingual (SLIT) immunotherapy:** Modify immune response to specific allergens → allergen tolerance; effective for allergic asthma, allergic rhinitis; 3-5 year course; reduces symptoms and medication needs; risk of anaphylaxis with SCIT → administer in clinic with epinephrine available

## Connections

- `targets` → **[Respiratory System](../respiratory-system/README.md)** — asthma causes reversible airway obstruction via smooth muscle contraction, mucosal edema, and mucus plugging; chronic inflammation drives irreversible airway remodeling (subepithelial fibrosis, smooth muscle hypertrophy) — the basis for step-up therapy to prevent structural changes.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — mast cells are the central acute asthma effectors; IgE cross-linking by allergen → degranulation → histamine, LTC4, PGD2 → acute bronchoconstriction; sustained mast cell cytokine release (IL-5, IL-13) amplifies eosinophil recruitment and late-phase inflammation.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 drives airway remodeling, neutrophilic airway inflammation, and corticosteroid-insensitive asthma; IL-6 trans-signaling promotes STAT3-dependent goblet cell differentiation and mucus hypersecretion; elevated serum IL-6 correlates with severe, uncontrolled asthma.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta1 drives airway remodeling: subepithelial fibrosis, smooth muscle hypertrophy, and goblet cell hyperplasia; also suppresses Treg function and promotes Th17 skewing in severe asthma; anti-TGF-beta strategies are under investigation to reverse established airway structural changes.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Allergen-specific IgE binds FcεRI on airway mast cells → allergen cross-linking → degranulation → acute bronchoconstriction; omalizumab (anti-IgE mAb) binds free IgE → reduces FcεRI expression → 26-50% fewer exacerbations in severe allergic asthma.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — IL-4 drives Th2 airway inflammation, IgE production, and eosinophil recruitment in allergic asthma; type II receptor (IL-4Rα + IL-13Rα1) mediates mucus and AHR; dupilumab reduces severe asthma exacerbations by ~50% in patients with elevated eosinophils or FeNO.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — IL-5 drives eosinophilic airway inflammation; blood eosinophils ≥300/μL identifies biologic candidates; mepolizumab (MENSA 47% RRR) and benralizumab (CALIMA 28-36% RRR) block IL-5 or IL-5Rα to reduce exacerbations in severe eosinophilic asthma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — TSLP → DC and ILC2 activation upstream of the Th2/eosinophil cascade; tezepelumab (anti-TSLP mAb) reduced exacerbations 70% in NAVIGATOR trial — most effective severe asthma biologic across all eosinophil and IgE levels including T2-low patients.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — A2BR on mast cells and airway smooth muscle → bronchoconstriction at high adenosine; AMP provocation test exploits this for asthma diagnosis; theophylline (adenosine antagonist + PDE inhibitor) is a bronchodilator; caffeine has mild adenosine-antagonist bronchodilator effect.
- `connects-to` → **[COPD](../copd/README.md)** — Asthma and COPD are the two great obstructive airway diseases and can overlap (ACOS): asthma is reversible, eosinophilic/Th2 inflammation in younger atopic patients, while COPD is largely irreversible, neutrophilic, smoking-driven—though many older patients share both.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Allergic asthma is a Th2 helper-T-cell disease: Th2 cells secrete IL-4, IL-5, and IL-13 that drive IgE class-switching, eosinophil recruitment, and mucus, so the type-2 inflammation they coordinate is the target of biologics like dupilumab and anti-IL-5 agents.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Asthma and atopic dermatitis are linked stages of the atopic march: many children begin with eczema and food allergy in infancy, then progress to allergic rhinitis and asthma, reflecting shared type-2 immunity and barrier defects—and both now respond to dupilumab.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Airway smooth muscle is the effector of asthma's airflow obstruction: hyperresponsive smooth muscle contracts in response to triggers, narrowing bronchi (wheeze), and over time hypertrophies—so bronchodilators relax it while bronchial thermoplasty ablates it.
- `connects-to` → **[Respiratory Syncytial Virus](../../../02-pathogen/01-viruses/respiratory-syncytial-virus/README.md)** — Early respiratory syncytial virus infection is linked to asthma: severe RSV bronchiolitis is associated with later wheezing, and viral respiratory infections remain the commonest trigger of asthma exacerbations—tying a childhood virus to chronic airway disease.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity defines a distinct, harder-to-treat asthma phenotype: excess weight restricts lung mechanics and adipose-derived inflammation alters airway biology, so obese asthmatics often have more symptoms and worse control—and weight loss improves the disease.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — IL-13 drives the airway changes of asthma: this type 2 cytokine, with IL-4, fuels IgE production, mucus hypersecretion and airway hyperresponsiveness, so dupilumab (blocking IL-4/IL-13 signaling) is a mainstay biologic for type 2-high asthma.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Asthma remodels the lung over time: repeated bronchoconstriction and inflammation thicken airway smooth muscle and basement membrane, so uncontrolled asthma can leave fixed obstruction—turning a reversible disease into permanent lung damage.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells initiate the allergic asthma response: they sample inhaled allergens and prime naive T cells toward the Th2 program, sitting upstream of the IgE and eosinophil cascade—so they set whether the airway becomes sensitized in the first place.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine is a frontline mediator of the asthmatic airway: released when allergen cross-links IgE on mast cells, it triggers rapid bronchoconstriction, mucus, and vascular leak—the immediate-phase response, though antihistamines help asthma less than allergic rhinitis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Not all asthma is eosinophilic: a neutrophil-driven, type-2-low phenotype causes severe, often steroid-resistant disease, so recognizing neutrophilic asthma matters because it responds poorly to the inhaled corticosteroids and anti-IL-5 biologics that target eosinophils.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Asthma reflects how the immune system is wired: a type-2 (Th2) skew underlies allergic asthma, and the hygiene hypothesis links reduced early microbial exposure to this allergic tilt—so asthma is as much an immune-regulation disorder as an airway one.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Exhaled nitric oxide is a key asthma biomarker: airway eosinophilic inflammation raises FeNO (fractional exhaled NO), so measuring it gauges Type-2 inflammation, predicts steroid response and helps tailor and monitor asthma therapy.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D status influences asthma: deficiency is linked to more frequent exacerbations and poorer control, and as an immune modulator it supports regulatory responses—so vitamin D is studied as add-on prevention, especially in deficient patients.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Asthma reflects failed regulatory T-cell tolerance: Tregs normally restrain allergic responses to inhaled antigens, so when they are deficient or dysfunctional, the Th2 inflammation behind allergic asthma goes unchecked—a target for allergen immunotherapy.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Asthma's cornerstone controller mimics cortisol: inhaled corticosteroids damp the airway's eosinophilic, Th2 inflammation, preventing the attacks rather than just relieving them—the single most important long-term asthma therapy.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Asthma's rescue works through adrenaline's receptors: β2-agonists like albuterol (and epinephrine in anaphylaxis) relax airway smooth muscle within minutes, reversing the bronchoconstriction of an acute attack.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Asthma's bronchoconstriction runs on calcium: airway smooth muscle contracts when calcium floods its cells, so the wheeze of an attack is a calcium-driven squeeze—and relaxing that contraction is what bronchodilators achieve.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium relaxes the asthmatic airway: intravenous magnesium sulfate is given in severe attacks because it blocks calcium-driven smooth-muscle contraction and bronchodilates when standard inhalers fall short.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — A severe asthma attack ultimately starves the blood of oxygen: as airways narrow and air-trapping worsens, gas exchange fails and oxygen falls—rising CO2 in a tiring patient is an ominous sign of impending respiratory arrest.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells stoke severe and viral asthma: CD8 T cells, especially during respiratory-virus exacerbations, add to the Th2 inflammation and tissue damage, broadening the immune picture beyond the classic allergic pathway.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Treating an asthma attack can drop potassium: high-dose beta-agonists drive potassium into cells, so the salbutamol that opens airways may cause hypokalemia that needs watching in severe attacks.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Asthma is one step of the atopic march, often heralded by eczema: the same Th2/IgE allergy that inflames the skin in atopic dermatitis later inflames the airways, linking skin and lung in one allergic diathesis.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Long-standing asthma scars the airway: chronic inflammation lays down subepithelial fibrosis and thickens the wall, part of the remodeling that turns reversible wheeze into fixed, hard-to-treat airflow limitation.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons help corner asthma: the chest X-ray shows hyperinflation and excludes mimics, CT reveals mucus plugging and wall thickening, and measuring the light-based marker of exhaled nitric oxide gauges the eosinophilic inflammation guiding treatment.
- `connects-to` → **[Prostaglandins (Eicosanoids)](../../03-molecular/prostaglandins/README.md)** — Eicosanoids drive the asthmatic airway: leukotrienes and prostaglandins released by mast cells clamp the bronchi shut and recruit inflammation, so leukotriene-blocking drugs ease asthma — and aspirin, by skewing this pathway, can trigger a severe attack.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Severe chronic asthma can strain the heart: sustained airway obstruction and low oxygen raise pressure in the lung's vessels, forcing the right ventricle to labor toward cor pulmonale, while high-dose beta-agonists quicken the pulse.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Long-standing asthma reshapes the airway wall: repeated inflammation lays down extra collagen beneath the epithelium, thickening the basement membrane in the remodeling that can fix some obstruction beyond what inhalers reverse.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Vagal acetylcholine tightens the airways: released onto muscarinic receptors it constricts bronchial smooth muscle and drives mucus, which is why anticholinergics like ipratropium and tiotropium relax the airways as add-on therapy.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Fat shapes a distinct asthma: in obese-asthma the adipocyte's inflammatory adipokines drive a non-eosinophilic, often steroid-resistant disease, one reason weight loss can improve control where inhalers fall short.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies now treat severe asthma at its source: omalizumab mops up IgE, mepolizumab blocks IL-5 to starve eosinophils, and dupilumab blocks IL-4/13 signaling — monoclonal antibodies that quiet the type-2 inflammation when inhalers cannot.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hormones modulate the airways: asthma often shifts with the menstrual cycle (perimenstrual asthma) and changes in pregnancy — worsening in about a third of women — so control is actively managed through gestation to protect mother and fetus.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Early-life microbes set the allergic thermostat: a less diverse infant gut microbiome, shaped by birth mode, antibiotics, and environment, tilts the immune system toward the type-2 responses of asthma — the core of the hygiene hypothesis.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — A mould can hijack the asthmatic airway: sensitization to Aspergillus drives allergic bronchopulmonary aspergillosis, where the fungus colonizing the bronchi triggers fierce eosinophilic inflammation, mucus plugging and bronchiectasis atop the asthma.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Severe eosinophilic asthma can herald a vasculitis: eosinophilic granulomatosis with polyangiitis (Churg-Strauss) begins with adult-onset asthma and blood eosinophilia before progressing to an ANCA-associated small-vessel vasculitis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Not all asthma is type-2: a neutrophilic, often steroid-resistant phenotype is driven by Th17 cells and IL-17A rather than eosinophils, explaining why some severe asthmatics respond poorly to the usual eosinophil-targeting biologics.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Long-standing asthma remodels the airway wall: fibroblasts laying down subepithelial collagen thicken and stiffen the bronchi, a structural scarring that can fix airflow limitation even when the inflammation is controlled.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — A kinin tightens the airways: bradykinin generated in the inflamed bronchi constricts smooth muscle and stimulates mucus and cough, contributing to airway hyperreactivity — and explaining the cough that ACE inhibitors, which raise bradykinin, can provoke.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — The inflamed lung is more vulnerable to a classic pathogen: asthmatics carry a higher risk of invasive pneumococcal disease, which is why pneumococcal vaccination is recommended to protect airways already primed for trouble.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is the airway's inflammation switch: allergens, viruses and pollutants activate NF-κB in bronchial epithelium to pour out the cytokines and chemokines of an asthma attack, and quieting it is much of how inhaled steroids work.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 underlies the steroid-resistant disease: in neutrophilic and severe asthma, IL-6/IL-17-driven STAT3 signaling sustains airway inflammation that responds poorly to corticosteroids, marking it as a target in hard-to-treat cases.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Severe disease tilts the blood toward clotting: asthma — especially severe, exacerbating disease and long courses of oral steroids — is linked to a higher risk of pulmonary embolism and deep-vein thrombosis.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Its inhalers seed oral thrush: inhaled corticosteroids deposit on the oropharynx and locally suppress immunity, allowing Candida to overgrow into oral candidiasis — the reason spacers and mouth-rinsing are advised after each dose.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Steroid courses thin the bone: repeated oral-corticosteroid bursts for exacerbations, and high-dose inhaled steroids in severe asthma, accelerate bone loss and raise the long-term risk of osteoporotic fracture.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Breathlessness and anxiety feed each other: asthma carries high rates of anxiety, and the fear of an attack — plus the overlap of hyperventilation with asthma symptoms — can worsen perceived control and trigger exacerbations.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Its rescue steroid courses raise blood sugar: the repeated oral-corticosteroid bursts that severe or poorly controlled asthma requires induce insulin resistance and can precipitate steroid-induced diabetes.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Chronic breathlessness and limitation weigh on mood: alongside its well-known anxiety, asthma carries elevated depression, driven by activity restriction, poor sleep and the burden of uncontrolled symptoms.
- `connects-to` → **[Stroke](../stroke/README.md)** — Severe asthma tracks with cerebrovascular risk: the systemic Th2 and eosinophilic inflammation of asthma, especially severe late-onset disease, is associated in cohort studies with a modestly raised risk of stroke.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Breathlessness and panic feed each other: the air hunger of an asthma attack can trigger panic, and panic-driven hyperventilation in turn worsens bronchospasm, so the two disorders are strongly intertwined.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its steroids reach far beyond the lungs: repeated oral corticosteroid courses and high-dose inhaled steroids for asthma can suppress the adrenal axis and, in children, slow growth, an endocrine cost of control.
- `connects-to` → **[Influenza](../influenza/README.md)** — Respiratory viruses ignite attacks: influenza and other viral infections are leading triggers of asthma exacerbations, inflaming the airways, so annual vaccination is advised for people with asthma.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Nerves set bronchial tone: parasympathetic vagal cholinergic signalling constricts the airways and amplifies reflex bronchospasm, which is why anticholinergic bronchodilators relieve attacks.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Reflux from below stokes the airway: gastro-oesophageal reflux is a common asthma comorbidity and trigger, provoking bronchospasm through microaspiration and a vagal oesophago-bronchial reflex.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its drugs and the heart intersect: beta-blockers can precipitate bronchospasm in asthma, while inhaled and systemic beta-agonists cause tachycardia, tremor and, in overuse, arrhythmia.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It sits in the atopic spectrum: asthma travels with eczema and urticaria through shared type 2 inflammation, and anti-IgE omalizumab treats both asthma and chronic urticaria.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its steroid courses weaken bone and muscle: repeated oral corticosteroid bursts for exacerbations cause osteoporosis and proximal steroid myopathy over time.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Severe eosinophilic disease can attack the kidney: difficult eosinophilic asthma can herald eosinophilic granulomatosis with polyangiitis, which causes a pauci-immune glomerulonephritis.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Inhaled steroids are the controller: they suppress airway inflammation as the foundation of asthma maintenance, with systemic steroids for acute severe attacks.
- `connects-to` → **[Beta-blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — Some drugs can trigger an attack: non-selective beta-blockers can provoke bronchospasm and are used with caution or avoided in asthma.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Aspirin can set off asthma: in aspirin-exacerbated respiratory disease (Samter's triad), NSAIDs trigger severe bronchospasm in asthmatics with nasal polyps.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Biologics for severe type-2 disease: monoclonal antibodies against IgE (omalizumab), IL-5 (mepolizumab), IL-4Rα (dupilumab) and TSLP (tezepelumab) control severe eosinophilic and allergic asthma that escapes inhaled steroids.
- `connects-to` → **[Lung Slice](../../05-tissue/lung-slice/README.md)** — It remodels the airway wall: chronic asthma thickens airway smooth muscle, deposits subepithelial collagen and fills the lumen with mucus — the bronchial-wall remodelling that turns reversible bronchospasm into fixed airflow obstruction.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — A contrasting chronic airway disease: asthma is reversible bronchospasm of type-2 inflammation, whereas cystic fibrosis is a genetic defect of mucus clearance causing infection and bronchiectasis — though they overlap when Aspergillus drives ABPA in both.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Cardiac asthma mimics it: left heart failure causes wheeze and breathlessness from pulmonary congestion that imitate an asthma attack, a key differential—and the beta-blockers used for heart failure can themselves provoke bronchospasm.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Its drugs and the heart's rhythm: beta-2 agonists and theophylline used in asthma can provoke tachyarrhythmias, while the beta-blockers acting on cardiac conduction are avoided in asthma because they trigger bronchospasm.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Chronic inflammation carries cardiovascular cost: severe and late-onset asthma is associated with increased atherosclerotic cardiovascular disease, driven by systemic inflammation and the metabolic effects of long-term corticosteroids.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Allergic sensitisation: the allergen-specific IgE that drives allergic asthma is class-switched by B cells in germinal centres, under IL-4/IL-13 and follicular helper T-cell help.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — The eosinophil supply line: allergic asthma's IL-5 drives eosinophil production in the bone marrow, and anti-IL-5 biologics like mepolizumab cut off this source to control eosinophilic asthma.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — A surprising non-risk: well-controlled type-2-high allergic asthma did not raise COVID-19 severity—inhaled corticosteroids and lower airway ACE2 expression may even protect—unlike most other chronic lung diseases.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Clinical interplay: although type-2 asthma did not worsen COVID-19, severe COVID can present with wheeze and bronchospasm, and the pandemic reshaped asthma care toward inhaled-steroid maintenance and remote monitoring.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Neural control of the airway: vagal cholinergic tone drives bronchoconstriction (the target of anticholinergics like tiotropium), and sensory-nerve neurogenic inflammation amplifies the airway hyperresponsiveness of asthma.
- `connects-to` → **[Surfactant](../../03-molecular/surfactant/README.md)** — Surfactant in small-airway closure: airway surfactant becomes dysfunctional in asthma, contributing to the mucus plugging and small-airway collapse that drive severe and fatal attacks.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Airway remodelling: VEGF drives the angiogenesis and vascular remodelling of the chronically inflamed asthmatic airway wall, contributing to fixed airflow obstruction.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obese-asthma phenotype: leptin from excess adipose tissue promotes airway inflammation and links obesity to a distinct, often steroid-resistant asthma phenotype.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Neutrophilic axis: IL-1β and inflammasome activation characterise the neutrophilic, non-Th2, steroid-resistant form of severe asthma, distinct from eosinophilic disease.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Severe-asthma inflammation: TNF-α drives the neutrophilic inflammation and airway hyperresponsiveness of severe, steroid-resistant asthma.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Cell recruitment: CCL2 draws monocytes and other inflammatory cells into the asthmatic airway, contributing to the chronic inflammation and remodelling.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1/neutrophilic asthma: IFN-γ from Th1 cells characterises the non-eosinophilic, often steroid-resistant asthma endotype, contrasting with the Th2 form.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — Stem-cell factor signaling through KIT maintains the airway mast cells whose IgE-triggered degranulation releases the histamine and leukotrienes driving the acute bronchoconstriction of allergic asthma—the effector cell behind the immediate response.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The type-2 cytokines IL-4, IL-5, and IL-13 all signal through JAK-STAT, making JAK inhibitors an emerging strategy to block multiple type-2 pathways at once rather than neutralizing a single cytokine as current biologics do.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Substance P released from airway sensory nerves causes bronchoconstriction, mucus secretion, and plasma extravasation—the neurogenic arm of asthmatic airway inflammation that contributes to cough and hyperresponsiveness.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 from airway neutrophils marks the non-type-2, neutrophilic asthma that responds poorly to corticosteroids and eosinophil-targeted biologics, defining a distinct endotype that needs different therapeutic strategies.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelin-1 from airway epithelium is a potent bronchoconstrictor and mitogen for airway smooth muscle, contributing to the smooth-muscle hyperplasia and subepithelial fibrosis of asthmatic airway remodeling.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Low adiponectin in obesity removes an anti-inflammatory brake on the airways, part of why the obese-asthma phenotype is more severe and steroid-resistant, complementing the pro-inflammatory leptin of the same metabolic axis.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The NLRP3 inflammasome and IL-1β drive the neutrophilic, type-2-low inflammation of severe steroid-resistant asthma, a phenotype distinct from the eosinophilic IL-4/5/13 axis already mapped.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Regulatory IL-10 from regulatory T cells normally restrains airway allergic inflammation, and deficient IL-10-mediated tolerance permits the type-2 response of asthma—the principle behind allergen immunotherapy.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of microbial and pollutant exposures shapes asthma risk and exacerbations, the molecular substrate of the hygiene-hypothesis interaction between environment and airway immunity.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Inhaled corticosteroids act through the glucocorticoid receptor to suppress airway inflammation, the cornerstone asthma controller, with steroid resistance marking severe neutrophilic disease.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR sensing of viruses and allergens (TLR4 mapped) signals through MyD88 to NF-κB (mapped), driving the innate inflammation behind asthma exacerbations.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Growth-factor and TGF-β signaling (mapped) through the MAPK-ERK cascade drives the airway-smooth-muscle proliferation and remodeling of chronic asthma.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-dependent metabolism and airway-smooth-muscle proliferation contribute to the bronchial hyperreactivity and airway remodeling of asthma.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant defense protects the airway epithelium from the oxidative stress of allergic inflammation and pollutant exposure, a pathway impaired in severe asthma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains the Th17 response (IL-17A already mapped) that drives the neutrophilic, often steroid-resistant phenotype of severe asthma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes eosinophil recruitment, airway inflammation and the subepithelial remodeling that characterizes chronic asthma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the airway smooth-muscle hyperplasia and subepithelial fibrosis of airway remodeling in asthma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling underlies the antiviral Th1 response that drives virus-induced exacerbations of asthma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate airway smooth-muscle and T-cell programs and influence the glucocorticoid responsiveness that varies across asthma phenotypes.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoxic inflamed airway promotes angiogenesis and the airway remodeling of chronic asthma.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA, PI3Kδ) signaling drives airway inflammation, smooth-muscle proliferation, and the corticosteroid insensitivity of severe asthma.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — AKT downstream of PI3K (PIK3CA already mapped) drives airway smooth-muscle proliferation and the survival of Th2 cells in asthma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven airway inflammation and remodeling of asthma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the innate inflammatory activation of virus-induced asthma exacerbations.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the airway smooth-muscle and immune-cell metabolism of asthma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the airway epithelial and eosinophil responses and airway remodeling of asthma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of the IgE receptor (FcεRI) drives the mast-cell activation of allergic asthma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the airway inflammation of asthma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the Th2 and airway responses of asthma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 (C3a) participates in the airway inflammation and hyperresponsiveness of asthma.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the airway leukocyte recruitment and remodeling of asthma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the airway immune and structural gene programs of asthma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of the Type 2 immune response of asthma.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex-hormone modulation: asthma prevalence and severity shift at puberty and across the menstrual cycle, and estrogen modulates airway inflammation and smooth-muscle tone, underlying the female predominance of adult asthma and premenstrual exacerbations.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Anaphylatoxins: the complement fragments C3a and C5a (C3 already mapped) generated in allergic airways amplify mast-cell and eosinophil recruitment and smooth-muscle contraction, bridging innate complement to the type-2 inflammation of asthma.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Mucosal barrier: secretory IgA at the airway surface shapes the response to inhaled allergens and microbes, and altered IgA production is associated with allergic sensitisation and asthma susceptibility in early life.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Theophylline and oxidative stress: theophylline, a methylxanthine bronchodilator and phosphodiesterase inhibitor, is metabolised via xanthine oxidase, whose reactive oxygen species also contribute to the airway oxidative stress of asthma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Allergen presentation: MHC class II presentation of inhaled allergens by airway dendritic cells drives the Th2 sensitisation (IL-4/IL-13 already mapped) of allergic asthma, and HLA associations contribute to susceptibility.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Airway macrophages: alveolar and airway macrophages, polarised toward an alternatively activated phenotype in type-2 asthma, contribute to the inflammation, remodelling and impaired resolution of the disease.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Respiratory acidosis: in acute severe asthma a rising carbon dioxide as the patient tires produces respiratory acidosis, and the accumulation of protons is an ominous sign heralding respiratory failure and the need for ventilation.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Neurogenic inflammation: CGRP released from airway sensory nerves, with substance P (already mapped), contributes to the neurogenic inflammation, vasodilation and cough of asthma, part of the neuro-immune dimension of the disease.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac strain: high-dose beta-agonists and theophylline cause tachycardia and, with the hypoxaemia of acute severe asthma, can strain the heart, and troponin elevation may mark the myocardial stress of a near-fatal attack.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant defence: selenium is essential for the glutathione peroxidases that quench airway oxidative stress (xanthine oxidase already mapped), and low selenium status has been linked to asthma and worse airway inflammation.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Obesity-asthma phenotype: the adipokine resistin, with leptin and adiponectin (already mapped), links the adipose tissue of obesity to airway inflammation, part of the distinct obese-asthma phenotype that responds poorly to steroids.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Airway surface liquid: chloride transport hydrates the airway surface liquid and mucus, and its disturbance contributes to the thick mucus plugging of the airways (smooth muscle already mapped) in severe and fatal asthma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Viral exacerbation: the deficient epithelial type-I interferon response to rhinovirus in asthma permits the viral respiratory infections that are the commonest trigger of acute asthma exacerbations.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Obese-asthma metabolism: the insulin resistance of the obese-asthma phenotype (leptin, adiponectin and resistin already mapped) links the metabolic dysfunction of obesity to the airway inflammation and the poor steroid response.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and airway immunity: zinc is an antioxidant and immune-modulating trace metal, and its deficiency is associated with worse asthma control and heightened airway inflammation.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Allergen sensitisation: the airway dendritic cells sample the inhaled allergen and prime the Th2 (already mapped) response, initiating the allergic sensitisation of asthma.
- `connects-to` → **[COPD](../copd/README.md)** — Asthma-COPD overlap: the asthma-COPD overlap (ACO) shares features of both; the neutrophilic (already mapped), less steroid-responsive asthma phenotype resembles COPD.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron and inflammation: the IL-6-driven (already mapped) hepcidin and the airway iron dysregulation are linked to the severe, neutrophilic (already mapped) asthma and the anaemia of chronic inflammation.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — IgE class-switching: the B cells class-switch to the allergen-specific IgE (already mapped) under the IL-4 and IL-13 (already mapped), driving the allergic sensitisation of asthma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 counter-arm: IL-12 polarises the Th1 (IFN-γ already mapped) response that counter-regulates the dominant Th2 (IL-4, IL-5 and IL-13 already mapped) axis of allergic asthma.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate antiviral surveillance: the NK cells (perforin already mapped) participate in the antiviral response to the respiratory viruses that trigger the asthma exacerbations.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — IgE plasma cells: the plasma cells secrete the allergen-specific IgE (already mapped) that arms the mast cells (already mapped) of allergic asthma.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Type-2 IL-31: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, is part of the broader type-2 immune response and the atopic itch shared across the atopic diseases of the allergic-asthma patient.
- `connects-to` → **[Prurigo nodularis](../prurigo-nodularis/README.md)** — Atopic-march overlap: asthma shares the type-2 (IL-4, IL-5, IL-13 and TSLP already mapped) immunity with prurigo nodularis, another atopic-spectrum type-2 disease treated with the shared biologics.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Anaphylatoxin receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) is part of the complement/anaphylatoxin contribution to the airway inflammation of asthma.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelet in airway: the platelets, via the platelet-eosinophil aggregates and the release of mediators, contribute to the airway inflammation and remodelling of asthma.
- `connects-to` → **[Influenza A virus](../../../02-pathogen/01-viruses/influenza-a/README.md)** — Viral exacerbation: the influenza A virus (with RSV already mapped) is a respiratory-viral trigger of the acute exacerbations of asthma.

[^gina-2023-asthma]: Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention. 2023. [ginasthma.org](https://ginasthma.org/2023-gina-main-report/)
[^wenzel-2012-asthma-phenotypes]: Wenzel SE. Asthma phenotypes: the evolution from clinical to molecular approaches. *Nat Med.* 2012;18(5):716-725. [doi:10.1038/nm.2678](https://doi.org/10.1038/nm.2678) · [PubMed 22561835](https://pubmed.ncbi.nlm.nih.gov/22561835/)
[^castro-2018-dupilumab-asthma]: Castro M, Corren J, Pavord ID, et al. Dupilumab efficacy and safety in moderate-to-severe uncontrolled asthma. *N Engl J Med.* 2018;379(26):2486-2496. [doi:10.1056/NEJMoa1804092](https://doi.org/10.1056/NEJMoa1804092) · [PubMed 30088505](https://pubmed.ncbi.nlm.nih.gov/30088505/)
