---
schema: human-scale-entry/v1
id: pulmonary-arterial-hypertension
name: Pulmonary Arterial Hypertension
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "PAH (WHO Group 1) is progressive obliterative pulmonary vascular disease; mPAP >20 mmHg + PVR ≥2 WU; BMPR2/BMP9 mutations in heritable PAH. Three pathways (endothelin/NO/prostacyclin) targeted by ERAs, PDE5i/sGCi, and prostacyclin analogues."
aliases: ["PAH", "Group 1 pulmonary hypertension", "pulmonary hypertension", "idiopathic PAH", "IPAH", "heritable PAH", "HPAH", "connective tissue disease PAH", "CTD-PAH"]
sources:
  - id: galie-2015-esc-pah-guidelines
    type: clinical-guideline
    cite: "Galie N, Humbert M, Vachiery JL, et al. 2015 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Heart J. 2016;37(1):67-119."
    doi: "10.1093/eurheartj/ehv317"
    pmid: "26320113"
    url: "https://doi.org/10.1093/eurheartj/ehv317"
  - id: simonneau-2019-pah-classification
    type: peer-reviewed
    cite: "Simonneau G, Montani D, Celermajer DS, et al. Haemodynamic definitions and updated clinical classification of pulmonary hypertension. Eur Respir J. 2019;53(1):1801913."
    doi: "10.1183/13993003.01913-2018"
    pmid: "30545968"
    url: "https://doi.org/10.1183/13993003.01913-2018"
  - id: sitbon-2015-selexipag-griphon
    type: peer-reviewed
    cite: "Sitbon O, Channick R, Chin KM, et al. Selexipag for the Treatment of Pulmonary Arterial Hypertension. N Engl J Med. 2015;373(26):2522-2533."
    doi: "10.1056/NEJMoa1503184"
    pmid: "26579977"
    url: "https://doi.org/10.1056/NEJMoa1503184"
cross_links:
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "ET-1 overproduction by PAH endothelium → ETA on pulmonary VSM → vasoconstriction + medial hypertrophy + adventitial fibrosis → elevated PVR; ERAs (bosentan, ambrisentan, macitentan) are first-line oral therapy for PAH; macitentan reduces morbidity/mortality 45% (SERAPHIN trial)."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Impaired eNOS and NO bioavailability in PAH endothelium → cGMP vasodilation failure; PDE5 inhibitors (sildenafil, tadalafil) prevent cGMP degradation → sustained vasodilation + anti-proliferative; sGC stimulators (riociguat) amplify NO-sGC-cGMP independent of endogenous NO."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "PAH endothelium produces insufficient PGI2 (prostacyclin) → IP receptor → cAMP → vasodilation and anti-proliferative; IV epoprostenol (Flolan) reduces mortality in severe PAH; inhaled iloprost, SC/IV treprostinil; selexipag (oral IP agonist) reduces morbidity 40% (GRIPHON trial)."
  - target: 01-human/06-organ/lung
    relation: targets
    note: "PAH is a disease of the pulmonary vasculature; medial hypertrophy, intimal fibrosis, adventitial fibrosis, and plexiform lesions in pulmonary arterioles (<500 µm) → fixed obliterative vascular disease → RV pressure overload → cor pulmonale → right heart failure."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "SSc is the most common cause of CTD-PAH (10-15% of SSc patients); SSc-PAH treated with ERAs + PDE5i (macitentan, ambrisentan + tadalafil); worse prognosis than IPAH; annual echocardiographic screening recommended for all SSc patients."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Ang-1/Ang-2 imbalance in PAH: Ang-2 overexpression in pulmonary endothelium → Tie2 destabilization → endothelial mesenchymal transition → vascular remodeling; Ang-2 overexpressing mice develop PAH; plasma Ang-2 correlates with hemodynamic severity in PAH patients."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Activin A/B are elevated in PAH pulmonary vasculature; activin → VSMC ActRIIB/ALK4 → SMAD2/3 → proliferation and vasoconstriction → vascular remodeling; sotatercept (ActRIIB-Fc; FDA 2024) traps activin A/B → reverses vascular remodeling; STELLAR trial: +34.4 m 6MWD, p<0.001."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "PAH kills through the right heart: obliterated pulmonary arterioles raise vascular resistance until the thin-walled right ventricle, never built for high afterload, hypertrophies, dilates, and fails (cor pulmonale) — so RV function, not pulmonary pressure, best predicts survival."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Pulmonary endothelial dysfunction initiates PAH: injured endothelium underproduces vasodilators (NO, prostacyclin) and overproduces endothelin-1, and apoptosis-resistant clones form the plexiform lesions — so all three drug classes target endothelial signaling pathways."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Pulmonary artery smooth muscle cells drive PAH remodeling: under endothelin, activin, and growth-factor signaling they proliferate and resist apoptosis, thickening the media and muscularizing non-muscular arterioles — sotatercept (activin trap) reverses this remodeling."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Unresolved pulmonary emboli cause a distinct, surgically curable pulmonary hypertension: chronic thromboembolic PH (CTEPH) arises when organized clots obstruct and remodel pulmonary arteries, so every PAH workup includes a V/Q scan—CTEPH is cured by endarterectomy."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV is an established cause of pulmonary arterial hypertension: even with controlled viral loads, HIV proteins like Tat and Nef injure pulmonary endothelium and drive the same plexiform remodeling as idiopathic PAH, so HIV-PAH is a recognized WHO Group 1 subtype."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Pulmonary hypertension is a deadly complication of sickle cell disease: chronic hemolysis scavenges nitric oxide and releases free hemoglobin and arginase, so pulmonary vascular tone rises—an elevated tricuspid regurgitant jet marks patients at high mortality risk."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "PAH and juvenile polyposis converge on the BMP/TGF-β pathway: heritable PAH is most often caused by BMPR2 loss, and SMAD4/BMPR1A mutations can yield a combined JPS-HHT syndrome with PAH—BMP disruption linking gut polyps and pulmonary vascular disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "PAH ultimately kills through right heart failure: the thickened, narrowed pulmonary arteries raise resistance the right ventricle must pump against, so it hypertrophies, dilates and fails—right-heart function, not lung pressure alone, determines survival in PAH."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "PAH is a feared complication of connective-tissue disease, including lupus: immune-mediated injury remodels the pulmonary arteries, so SLE and systemic sclerosis patients are screened with echocardiography—CTD-associated PAH is a major cause of their mortality."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin drives pulmonary arterial hypertension: it constricts and remodels pulmonary arteries, and the appetite suppressants (fen-phen) that flooded the circulation with serotonin caused an epidemic of PAH—cementing the serotonin pathway as a disease driver."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia worsens pulmonary hypertension via a unique reflex: unlike systemic vessels, pulmonary arteries constrict when oxygen is low, so chronic hypoxia sustains vasoconstriction and vascular remodeling—why supplemental oxygen helps."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Pulmonary hypertension ultimately kills through the right ventricle: the right heart's cardiomyocytes hypertrophy then fail against the high pulmonary pressure, so cor pulmonale and right heart failure—not the lung itself—are the usual cause of death in PAH."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF marks the disordered vessels of pulmonary arterial hypertension: the plexiform lesions that obstruct small pulmonary arteries are foci of dysregulated VEGF-driven endothelial proliferation, reflecting how PAH is a vascular-remodeling, not just vasoconstrictive, disease."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Pulmonary arterial hypertension is the vascular disease of the respiratory system: remodeling of the lung's small arteries raises pulmonary pressure, so breathlessness and hypoxemia arise even though the airways and alveoli themselves may be normal."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Pulmonary arterial hypertension is a disease of the lesser circulation within the cardiovascular system: it raises pressure in the pulmonary arteries, not the systemic circuit, so its targeted vasodilators relax the lung's vessels rather than lowering body-wide pressure."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Liver disease can cause pulmonary hypertension: portal hypertension from cirrhosis leads to portopulmonary hypertension, where vasoactive substances bypassing the liver remodel the pulmonary arteries—an important PAH subtype affecting transplant eligibility."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Heritable PAH is a TGF-beta/BMP imbalance: loss of BMPR2 signaling tips the balance toward TGF-beta-driven proliferation of pulmonary vascular cells, the core lesion behind the disease and the target of activin-pathway drugs like sotatercept."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Adventitial fibroblasts complete PAH's vascular remodeling: alongside thickening endothelium and smooth muscle, activated fibroblasts in the outer arterial wall proliferate and stiffen the vessel, narrowing the lumen that raises pulmonary pressure."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Pulmonary arterial hypertension can begin with a potassium channel: KCNK3 mutations cause heritable PAH, and closing potassium channels constricts pulmonary artery smooth muscle—the same switch that drives hypoxic pulmonary vasoconstriction."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Pulmonary arterial hypertension involves in-situ platelet thrombosis: platelets clump in the narrowed small pulmonary arteries and release serotonin and thromboxane that further constrict and remodel them, adding clotting to the vascular disease."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Low oxygen drives pulmonary hypertension through HIF: hypoxia stabilizes HIF-1alpha, which reprograms pulmonary artery cells toward proliferation and constriction—why lung disease and high altitude raise pulmonary pressure."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGF drives the artery-thickening of pulmonary hypertension: it pushes pulmonary smooth muscle cells to proliferate and migrate, narrowing the vessels, which is why PDGF-blocking kinase inhibitors like imatinib were tested for the disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Perivascular macrophages inflame the pulmonary hypertension vessel: they cuff the remodeling arteries and pour out cytokines and growth factors that drive the proliferation, adding inflammation to the vasoconstriction and remodeling."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Pulmonary hypertension drags down the kidneys: as the failing right heart backs blood up into the veins, congestion and low forward flow injure the kidneys (cardiorenal syndrome), and worsening renal function marks a poor prognosis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Pulmonary vessels constrict through calcium: calcium entry contracts the arterial smooth muscle, and calcium-channel blockers can help the vasoreactive minority of PAH patients who respond to them."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Pulmonary hypertension can black out the brain: a failing right heart cannot raise output on exertion, so the brain is briefly starved of blood, causing the exertional dizziness and syncope of advanced disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Pulmonary hypertension scars its arteries: the remodeling thickens and fibroses the pulmonary arterial walls, narrowing them in the obliterative arteriopathy that raises the pressure relentlessly."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons measure and classify the pressure: echocardiography estimates it noninvasively, right heart catheterization under fluoroscopy confirms it, and a V/Q scan distinguishes clot-driven chronic thromboembolic disease from true arterial hypertension."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen drives pulmonary hypertension's female bias: the disease strikes women far more often, and the 'estrogen paradox' — the hormone and its metabolites both protecting the heart yet promoting the arterial remodeling — is central to its puzzling sex difference."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Losing the spleen can set the stage: splenectomy is a recognized risk factor for pulmonary hypertension, as the platelets and abnormal red cells no longer filtered by the spleen promote the in-situ thrombosis that remodels the lung arteries."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency haunts PAH even without anemia: it is common in these patients and independently predicts worse exercise capacity and survival, making iron status a routine thing to measure and correct."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Remodeling stiffens the lung's arteries with matrix: the diseased vessels lay down excess collagen and elastin in their walls, a fibrotic thickening that narrows the lumen and hardens the pulmonary circuit the right heart must push against."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "When PAH springs from a heart defect, the blood thickens: the chronic hypoxia of Eisenmenger physiology spurs the marrow to overproduce red cells, and the resulting secondary erythrocytosis adds viscosity and clot risk to the strained circulation."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Autoantibodies point to a cause: much PAH is connective-tissue-disease-associated, so an ANA panel with anti-centromere and anti-Scl-70 antibodies is checked to uncover the scleroderma or lupus driving the pulmonary vessels' disease."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy is perilous in PAH: the volume and output demands overwhelm the fixed, narrowed pulmonary circuit, carrying a maternal mortality so high that pregnancy is strongly discouraged and reliable contraception is part of management."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Fainting marks a failing circuit: when the right heart can no longer push enough blood through the stiffened lungs, exertion starves the brain's neurons of flow, and the exertional syncope that results is an ominous, late-stage warning sign."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation remodels the lung vessels: IL-6 is elevated in pulmonary arterial hypertension and drives the smooth-muscle and endothelial proliferation that narrows the arteries, an inflammatory arm of the disease that tracks with severity and is a therapeutic target."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Thyroid disease keeps company with PAH: both autoimmune hypo- and hyperthyroidism are over-represented in pulmonary arterial hypertension, so thyroid function is checked, since correcting it can ease the cardiovascular strain."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells gather in the diseased arteries: they accumulate around the remodeled pulmonary vessels and plexiform lesions of PAH, releasing mediators that fuel the proliferation and fibrosis narrowing the lumen."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "A developmental switch drives the vessel narrowing: Notch3 signaling pushes pulmonary smooth-muscle cells to proliferate and resist apoptosis, thickening the arterial wall — a remodeling pathway being explored as a therapeutic target in PAH."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Faulty immune restraint lets the arteries inflame: a deficiency of regulatory T cells permits the perivascular inflammation that drives pulmonary vascular remodeling, one reason PAH clusters with autoimmune diseases like scleroderma and lupus."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Chronic lung disease raises the pressure too: in COPD, alveolar destruction and chronic hypoxia constrict and remodel the pulmonary arteries, producing the group-3 pulmonary hypertension that worsens breathlessness and strains the right heart."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "The inflammasome stokes vascular remodeling: NLRP3-driven IL-1β release in the pulmonary artery wall promotes the perivascular inflammation and smooth-muscle proliferation that narrow the vessels in PAH."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Chronic hemolysis drives pulmonary hypertension: like sickle cell disease, thalassemia releases cell-free hemoglobin that scavenges nitric oxide, and with post-splenectomy thrombosis it produces a hemolysis-associated PAH."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Stimulants can scar the lung vessels: methamphetamine and other stimulants are an established cause of pulmonary arterial hypertension, producing a drug-induced form indistinguishable from the idiopathic disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 remodels the vessel through it: the elevated IL-6 of PAH signals via JAK-STAT3 in pulmonary artery smooth muscle and endothelium, driving the proliferative obliteration of small vessels that raises pressure."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "A failing right heart backs up into the kidneys: the venous congestion and low output of advanced PAH and cor pulmonale impair renal perfusion, a cardiorenal mechanism that drives chronic kidney disease."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic inflammation drags the hemoglobin down: the IL-6 milieu of PAH raises hepcidin and blunts erythropoiesis, and the resulting anemia of chronic disease worsens oxygen delivery and is a marker of poor prognosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A breathless, life-limiting disease weighs on mood: the relentless exertional limitation, poor prognosis and demanding therapy of PAH give it among the highest depression and anxiety rates in chronic cardiopulmonary illness."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Right-heart pressure can shunt clots to the brain: when PAH opens a patent foramen ovale into a right-to-left shunt, venous clots bypass the lungs and reach the cerebral arteries, causing paradoxical embolic stroke."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Its continuous prostacyclin needs a permanent line: severe PAH is treated with non-stop intravenous epoprostenol through an indwelling central catheter, which is a standing portal for bloodstream infection and catheter-related sepsis."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Clonal blood disease is a recognised cause: myeloproliferative neoplasms feature in Group 5 pulmonary hypertension, driving PAH through abnormal cells, splenectomy and high-output states."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "Chronic hypoxic lung damage pressurises the pulmonary bed: the bronchiectasis and persistent hypoxaemia of advanced cystic fibrosis cause hypoxic pulmonary vasoconstriction and Group 3 pulmonary hypertension with cor pulmonale."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A breathless, life-limiting disease breeds worry: the relentless dyspnoea, fear of right-heart failure and burdensome continuous therapy of PAH foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The liver both causes and suffers it: cirrhosis with portal hypertension causes portopulmonary hypertension, and right-heart failure from PAH congests the liver and gut, causing ascites and malabsorption."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It clusters with thyroid disease: both hyper- and hypothyroidism are over-represented in pulmonary arterial hypertension, and thyroid dysfunction can worsen its haemodynamics."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "A fixed low output starves the brain: severe PAH cannot raise cardiac output on exertion, so exertional syncope and presyncope from cerebral hypoperfusion are ominous warning signs."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The failing right heart backs up into the kidney: systemic venous congestion and reduced cardiac output in PAH impair renal function as a cardiorenal syndrome, worsening fluid overload."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Autoimmunity is a major cause: connective-tissue diseases such as scleroderma and lupus drive PAH through inflammatory and immune-mediated remodelling of the pulmonary arteries."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It shows on skin and at the drip site: connective-tissue-disease PAH brings sclerodactyly and telangiectasia, hypoxaemia causes cyanosis and clubbing, and continuous prostacyclin infusions cause skin and line-site reactions."
  - target: 03-medicine/01-modern/04-cardio/calcium-channel-blockers
    relation: connects-to
    note: "A subset responds to vasodilators: the minority of idiopathic PAH patients who are vasoreactive on testing benefit from high-dose calcium-channel blockers."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: connects-to
    note: "Anticoagulation has a historical role: warfarin was traditionally used in idiopathic pulmonary arterial hypertension to counter in-situ thrombosis, though its benefit is now debated."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Breathlessness wastes the muscles: severe PAH causes profound exercise limitation and peripheral muscle deconditioning, and advanced right-heart failure brings cardiac cachexia."
  - target: 03-medicine/01-modern/04-cardio/loop-diuretics
    relation: connects-to
    note: "They unload the failing right heart: as PAH causes right-ventricular failure, loop diuretics like furosemide relieve peripheral oedema, ascites, and congestion, though over-diuresis can drop the preload-dependent RV output."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It is a disease of the arterial wall: PAH remodels small pulmonary arteries with intimal fibrosis, medial smooth-muscle hypertrophy, and plexiform lesions that progressively narrow the lumen and raise pulmonary pressures."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Myeloproliferative disease can drive it: polycythaemia vera and related MPNs cause group-5 pulmonary hypertension through hyperviscosity, splenomegaly, and chronic thromboembolic obstruction of the pulmonary vasculature."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It kills through the right heart: pulmonary arterial hypertension forces the right ventricle to pump against high resistance, driving RV hypertrophy then dilatation and failure (cor pulmonale)—the myocardial decline that determines survival."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "It loosens the tricuspid valve: as the right ventricle dilates under pulmonary arterial hypertension, the tricuspid annulus stretches and the valve leaks, and the severity of this functional regurgitation tracks the pressure overload."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "A rare route to PAH: tuberous sclerosis causes lymphangioleiomyomatosis (LAM), whose smooth-muscle proliferation destroys lung tissue and can produce pulmonary hypertension, linking the mTOR-driven syndrome to the pulmonary vasculature."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "The gas-exchange interface: PAH's remodelled small pulmonary arteries sit beside the alveoli, and hypoxic pulmonary vasoconstriction—the alveolar oxygen response—drives the pressure rise in lung-disease-associated PAH."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Right-heart arrhythmia: progressive right-ventricular strain and dilatation in PAH cause atrial arrhythmias and conduction delay (right bundle branch block), worsening an already failing right heart."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "A rare NF1 association: neurofibromatosis type 1 is a recognised, often severe cause of pulmonary arterial hypertension, adding a vasculopathy to its tumour and skin features."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Portopulmonary hypertension: cirrhosis and portal hypertension arising in the hepatic lobule can drive Group 1 pulmonary arterial hypertension, a complication that critically affects candidacy for liver transplantation."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Pulmonary vascular insult: severe COVID-19 injures the pulmonary microvasculature and strains the right heart, and established PAH patients tolerate the added load poorly, making infection especially dangerous."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Cardiorenal backflow: the failing right ventricle of advanced PAH raises systemic venous pressure, congesting the kidney and injuring the glomerulus in a cardiorenal syndrome that worsens fluid overload."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis then resistance: early caspase-3-mediated endothelial apoptosis, followed by emergence of apoptosis-resistant proliferating cells, drives the plexiform vascular remodelling of PAH."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Proliferative signalling: PI3K-AKT-mTOR activation drives the smooth-muscle and endothelial proliferation that narrows pulmonary arterioles in PAH."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "Right-heart strain marker: BNP and NT-proBNP rise as the pressure-loaded right ventricle stretches in PAH, serving as key biomarkers for risk stratification and treatment response."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Vascular inflammation: TNF-α contributes to the perivascular inflammation and pulmonary-artery remodelling that narrow the vessels in PAH."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome-driven remodelling: IL-1β from the activated NLRP3 inflammasome promotes the pulmonary-arterial inflammation and remodelling of PAH, an emerging therapeutic target."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes and macrophages into the remodelling pulmonary-artery wall in PAH, fuelling the inflammation that drives vascular narrowing."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Compensatory vasodilator: adrenomedullin rises in PAH as a counter-regulatory pulmonary vasodilator and anti-proliferative peptide, and its levels track right-ventricular strain and disease severity."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Neurohormonal activation: RAAS-driven aldosterone excess in PAH promotes pulmonary-vascular and right-ventricular fibrosis and impairs endothelial function, the rationale for mineralocorticoid-receptor antagonists in the disease."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron deficiency: inflammation-driven hepcidin elevation causes the functional iron deficiency common in PAH, which independently predicts worse exercise capacity and survival regardless of anaemia."
  - target: 01-human/03-molecular/serca2a
    relation: connects-to
    note: "Right-ventricular failure: as the pressure-loaded right ventricle decompensates in PAH, SERCA2a is downregulated and calcium reuptake fails, impairing RV contractility and relaxation — the maladaptive remodelling that ultimately determines survival in the disease."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: xanthine oxidase activity is raised in PAH, generating reactive oxygen species and the hyperuricaemia whose serum urate level correlates with pulmonary haemodynamic severity and prognosis."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Endothelial dysfunction: the diseased pulmonary endothelium of PAH releases von Willebrand factor and supports the in-situ thrombosis of small pulmonary arteries, with raised vWF levels marking endothelial injury and adverse outcome."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "Hypoxic remodelling: HIF-2α/EPAS1 is a master driver of the pulmonary vascular remodelling of PAH and hypoxic pulmonary hypertension, and gain-of-function EPAS1 variants cause heritable pulmonary hypertension."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "BMP/TGF-β imbalance: BMPR2 and TGF-β signals converge on SMAD4, and the loss of BMP-SMAD signalling with preserved TGF-β-SMAD signalling drives the proliferative vasculopathy that sotatercept (rebalancing the activin-A arm already mapped) aims to correct."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Plexiform proliferation: FGF2-FGFR signalling drives the endothelial and smooth-muscle-cell proliferation of the plexiform lesions of PAH, an angiogenic growth-factor axis acting alongside the PDGF and VEGF already mapped."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Proliferative MAPK: PDGF and FGF (both mapped) signal through the MAPK-ERK cascade to drive the pulmonary-artery smooth-muscle proliferation of PAH, the rationale behind PDGFR-inhibitor (imatinib) trials."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Remodelling axis: PI3K-AKT-mTOR signalling (AKT already mapped) sustains the survival and proliferation of the remodelled pulmonary vascular cells in PAH."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Quasi-neoplastic growth: the apoptosis-resistant, proliferative pulmonary-artery smooth-muscle and endothelial cells of PAH show E2F-driven cell-cycle activity reminiscent of a cancer-like phenotype."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Remodelling cytokine axis: IL-6-JAK-STAT3 signalling (IL-6 and STAT3 already mapped) drives the proliferative pulmonary vascular remodelling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Vascular inflammation: NF-κB-driven inflammation in the pulmonary vasculature sustains the perivascular immune-cell recruitment and cytokine production that promote the vascular remodelling of PAH."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative dysfunction: NRF2 antioxidant signalling counters the oxidative stress (xanthine-oxidase already mapped) that contributes to endothelial dysfunction and smooth-muscle proliferation in pulmonary arterial hypertension."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 drives the pulmonary-vascular and right-ventricular fibrosis of pulmonary arterial hypertension and is a biomarker of disease severity."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT and mTOR mapped) promotes the pulmonary-arterial-smooth-muscle proliferation that obliterates the vessel lumen in PAH."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement activation in the pulmonary vascular wall contributes to the perivascular inflammation and remodelling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING amplifies the perivascular inflammation that drives the vascular remodelling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "Downregulation of FOXO1 in pulmonary-artery smooth-muscle cells drives the apoptosis-resistant, proliferative phenotype central to pulmonary arterial hypertension."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling contributes to the interferon and immune component of the pulmonary vascular inflammation of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signaling contributes to the proliferative, apoptosis-resistant phenotype of the pulmonary-artery smooth-muscle cells in pulmonary arterial hypertension."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the perivascular inflammation that drives the vascular remodeling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D-driven proliferation of pulmonary-artery smooth-muscle cells contributes to the occlusive vascular remodeling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the proliferation and apoptosis resistance of the pulmonary-artery smooth-muscle and endothelial cells in pulmonary arterial hypertension."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of PDGFR and other receptors (PDGF already mapped) contributes to the vascular remodeling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the Warburg-like metabolic shift of the remodeled pulmonary vasculature in pulmonary arterial hypertension."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the pulmonary-vascular-cell survival and proliferation in the vascular remodeling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the perivascular inflammation of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the pulmonary-vascular-cell phenotype in pulmonary arterial hypertension."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the perivascular inflammatory-cell recruitment and vascular remodeling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the vascular gene programs relevant to pulmonary arterial hypertension."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the perivascular inflammation and vascular remodeling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "Serotonin hypothesis: the serotonin transporter (SERT) delivers 5-HT (serotonin already mapped) into pulmonary artery smooth muscle to drive proliferation, and SERT is the mechanistic link behind anorexigen (fenfluramine)-associated pulmonary arterial hypertension."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Channelopathy: loss-of-function mutations in the KCNK3/TASK-1 potassium channel cause heritable pulmonary arterial hypertension, since impaired potassium efflux depolarises smooth muscle to raise calcium and promote vasoconstriction and remodeling."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Right-heart failure: pulmonary arterial hypertension ultimately kills through right ventricular failure, and troponin released from the strained, ischaemic RV myocardium is a prognostic biomarker linking the pulmonary vasculopathy to cardiac decompensation."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Vasodilator deficit: calcitonin gene-related peptide is a potent pulmonary vasodilator, and its relative deficiency contributes to the vasoconstriction of pulmonary arterial hypertension, complementing the endothelin/nitric-oxide/prostacyclin pathways already mapped."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "RAAS activation: the renin-angiotensin-aldosterone system (aldosterone already mapped) is activated in pulmonary arterial hypertension, and angiotensin II promotes the vascular remodelling and right-ventricular fibrosis that worsen the disease."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic dysfunction: pulmonary arterial hypertension is associated with insulin resistance and a shift toward glycolytic metabolism in the pulmonary vessels and right ventricle, a metabolic dimension increasingly recognised in its pathobiology."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Hypoxaemia and iron: chronic hypoxaemia in pulmonary arterial hypertension can raise haemoglobin through secondary erythrocytosis, while the common iron deficiency (hepcidin already mapped) impairs oxygen delivery and worsens outcomes."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "In-situ thrombosis: the pulmonary arteriopathy of pulmonary arterial hypertension carries a prothrombotic tendency with in-situ microthrombi, and reduced natural anticoagulants such as protein C (von Willebrand factor already mapped) contribute to this thrombotic component."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 vascular remodelling: IL-13 and the type-2 inflammatory response promote the pulmonary vascular smooth-muscle (already mapped) proliferation and remodelling, adding to the inflammatory drive (IL-6 already mapped) of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 inflammation: IL-4, with IL-13 (already mapped), drives the type-2 inflammatory arm that promotes the pulmonary vascular smooth-muscle (already mapped) remodelling, part of the inflammatory pathobiology of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "RAAS in right-heart failure: the renin-angiotensin-aldosterone system (angiotensin II and aldosterone already mapped) is activated in the right-heart failure of pulmonary arterial hypertension, contributing to the fluid retention and remodelling."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Vasoreactivity and calcium channels: the small vasoreactive subset of pulmonary arterial hypertension responds to calcium-channel blockers, and calcium handling in the pulmonary-artery smooth muscle (already mapped) underlies the vasoconstriction targeted."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine and sex bias: leptin, with the oestrogen (already mapped) metabolism, is implicated in the female predominance and the metabolic dimension of pulmonary arterial hypertension, part of its adipokine dysregulation."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Protective adipokine: adiponectin, with leptin (already mapped), modulates the pulmonary-vascular remodelling, and its dysregulation is part of the metabolic contribution to pulmonary arterial hypertension."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Vascular inflammation: resistin, with leptin and adiponectin (already mapped), is a pro-inflammatory adipokine implicated in the pulmonary-vascular inflammation and remodelling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "In-situ thrombosis: the in-situ thrombosis of the small pulmonary arteries (von Willebrand factor and protein C already mapped) contributes to the vascular occlusion of pulmonary arterial hypertension, the historical rationale for anticoagulation."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon-associated PAH: type-I interferon, both the therapy-induced and the connective-tissue-disease (systemic sclerosis already mapped) associated, is linked to the pulmonary vascular remodelling of pulmonary arterial hypertension."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Autoimmune vascular inflammation: the CD4 T cells and the Th17/regulatory dysregulation are implicated in the pulmonary-vascular inflammation of PAH, especially the connective-tissue-disease (systemic sclerosis already mapped) associated form."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 vascular inflammation: the IL-17 of the Th17 cells (T-helper cell already mapped) drives the perivascular inflammation and the remodelling of the pulmonary arteries in PAH."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 vascular inflammation: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the immune-mediated pulmonary-vascular inflammation of PAH."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the pulmonary-vascular inflammation of PAH."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune-mediated pulmonary-vascular inflammation of PAH."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the pulmonary-vascular inflammation and remodelling of PAH."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the pulmonary-vascular inflammation of PAH."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the pulmonary-vascular inflammation and endothelial (already mapped) injury of PAH."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement to the perivascular myeloid recruitment in the pulmonary-vascular remodelling of PAH."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Perivascular antigen presentation: the dendritic cells accumulate in the perivascular infiltrates and present antigen to the T cells (already mapped) in the inflammatory pulmonary-vascular remodelling of PAH."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active on the remodelling pulmonary vasculature of PAH."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron deficiency: transferrin, the iron carrier, reflects the iron-deficiency (hepcidin already mapped) that is a common, prognostically important comorbidity of pulmonary arterial hypertension."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Perivascular T cells: the cytotoxic T cells (perforin pathway) of the perivascular infiltrates contribute to the adaptive-immune component of the pulmonary-vascular remodelling of PAH."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Perivascular alarmin: TSLP released by inflamed pulmonary vascular endothelium promotes mast-cell degranulation and Th2 skewing within the perivascular infiltrates that drive the vascular remodelling of pulmonary arterial hypertension."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Vasodilatory paradox: bradykinin, whose pulmonary degradation by ACE is impaired in PAH, accumulates at the remodelling vascular wall, driving the cough and paradoxical vasodilation that limits ACE-inhibitor use in this condition."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Hypoxia erythrocytosis: erythropoietin, upregulated by the chronic pulmonary hypoxia (HIF-1α already mapped) of PAH, drives the secondary polycythaemia that initially compensates oxygen delivery but ultimately worsens blood viscosity."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement and contact-activation brake: C1-esterase inhibitor restrains the complement (C3, C5 and C5aR1 already mapped) and kallikrein-kinin (bradykinin already mapped) pathways that amplify the endothelial injury and perivascular inflammation of PAH."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Perivascular mast-cell mediator: histamine released by perivascular mast cells (already mapped) promotes endothelial permeability (endothelin-1 already mapped), smooth muscle cell (already mapped) proliferation and angiogenesis in PAH lesions."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Vascular remodelling ECM: periostin, induced by TGF-β and PDGF (both already mapped) in the PAH vascular wall, promotes smooth muscle cell (already mapped) migration and the matrix stiffness that drives the progressive vascular occlusion of PAH."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "PAH melatonin: melatonin via MT1/MT2 on pulmonary arterial smooth muscle cells (already mapped) and endothelium (endothelin-1 already mapped) modulates circadian vasoconstriction and ROS (xanthine-oxidase already mapped)-driven vascular remodelling of PAH."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "PAH androgen axis: testosterone via androgen receptor on pulmonary vascular smooth muscle cells (already mapped) exerts vasodilatory effects that contrast the estrogen (already mapped)-driven PAH susceptibility and female sex predominance."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "PAH prolactin: prolactin, via JAK2 (already mapped) signalling on pulmonary arterial smooth muscle cells (already mapped), promotes their survival and proliferation, amplifying the anti-apoptotic vascular remodelling driven by PDGF (already mapped) in PAH."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "PAH oxytocin: oxytocin via OXTR on pulmonary vascular endothelium (endothelin-1 already mapped) and smooth muscle cells (already mapped) promotes vasodilation, counteracting the endothelin-1 and PDGF (already mapped)-driven vascular remodelling of PAH."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "PAH vasopressin: vasopressin via V1aR on pulmonary arterial smooth muscle cells (already mapped) promotes vasoconstriction and proliferation, amplifying the endothelin-1 (already mapped) and PDGF (already mapped)-driven pulmonary vascular remodelling of PAH."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "PAH selenium: selenium-dependent glutathione peroxidase (GPX) quenches endothelial reactive-oxygen-species driving eNOS (nitric oxide already mapped) uncoupling and PDGF (already mapped)-mediated smooth muscle cell (already mapped) proliferation in PAH."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "PAH iodine: iodine-dependent thyroid hormones regulate endothelial cells (already mapped) and smooth muscle cells (already mapped); thyroid-hormone deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) vascular remodelling cascade of PAH."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "PAH sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the PDGF (already mapped) and endothelin-1 (already mapped) vascular remodelling cascade of PAH."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "PAH magnesium: magnesium, as eNOS (nitric-oxide already mapped) cofactor in endothelial cells (already mapped) and smooth muscle cells (already mapped), supports vasodilation; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PAH."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "PAH copper: copper, as lysyl oxidase cofactor in endothelial cells (already mapped) and smooth muscle cells (already mapped), drives pulmonary vascular ECM remodelling; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PAH."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "PAH phosphorus: phosphorus-dependent ATP in endothelial cells (already mapped) and smooth muscle cells (already mapped) sustains vascular-tone signalling; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) vascular-remodelling cascade of PAH."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "PAH zinc: zinc, as metalloproteinase cofactor in macrophages (already mapped) and smooth muscle cells (already mapped), regulates pulmonary ECM remodelling; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) vascular-remodelling cascade of PAH."
---

# Pulmonary Arterial Hypertension

## Overview

**Pulmonary arterial hypertension (PAH)** is a severe, progressive, and ultimately fatal disease of the **pulmonary vasculature** characterized by obliterative remodeling of small pulmonary arterioles, leading to increased pulmonary vascular resistance (PVR), right ventricular (RV) pressure overload, and — without treatment — RV failure and death [^galie-2015-esc-pah-guidelines].

**Updated hemodynamic definition (2018 World Symposium):**
- Mean pulmonary artery pressure (mPAP) **>20 mmHg** at rest (lowered from previous ≥25 mmHg)
- Pulmonary vascular resistance (PVR) **≥2 Wood Units** (corrected for normal post-capillary pressure)
- Pulmonary artery wedge pressure (PAWP) **≤15 mmHg** (distinguishes pre-capillary/arteriolar from post-capillary disease)
- Right heart catheterization (RHC) is the **gold standard** — required for definitive diagnosis

**WHO Clinical Classification of Pulmonary Hypertension (Group 1 = PAH):**

| Group | Etiology |
|:---|:---|
| **Group 1 (PAH)** | Idiopathic (IPAH), heritable (HPAH; BMPR2/BMP9), drug/toxin-induced (anorexigens), CTD (SSc most common), CHD (Eisenmenger), portal hypertension, HIV |
| Group 2 | Left heart disease (most common cause of PH overall) |
| Group 3 | Lung disease/hypoxia (COPD, IPF, OSA) |
| Group 4 | Chronic thromboembolic PH (CTEPH) |
| Group 5 | Multifactorial (sarcoidosis, myeloproliferative) |

**Epidemiology:**
- PAH (Group 1) prevalence: ~15-50 cases/million in Western countries; incidence 2-5/million/year
- **Gender:** Female predominance 2-4:1 in IPAH; female-to-male ratio narrows in HPAH (BMPR2 mutations)
- **Age:** Median age at diagnosis ~50 years (bimodal: young women for connective tissue disease PAH; older for IPAH)
- **Prognosis:** Without treatment, median survival 2.8 years from diagnosis (historical NIH registry); with modern combination therapy, 5-year survival ~60-70% in low/intermediate-risk patients
- **Systemic sclerosis (SSc-PAH):** PAH develops in 10-15% of SSc patients; worst prognosis of all PAH subgroups (5-year survival ~40-50%)

## Structure

### Pulmonary vascular pathobiology

**Three-layer vascular remodeling:**
1. **Intimal layer:** Endothelial cell proliferation + smooth muscle-like myofibroblast infiltration → eccentric intimal fibrosis → progressive luminal narrowing; **plexiform lesions** (pathognomonic): disorganized endothelial cell proliferation resembling a glomerulus — found in advanced IPAH/HPAH (not CTEPH)
2. **Medial layer:** Smooth muscle cell (SMC) hypertrophy and proliferation; abnormal extension of SMC into normally non-muscularized distal arterioles (<100 µm); driven by ET-1, PDGF, FGF-2
3. **Adventitial layer:** Fibroblast → myofibroblast activation; collagen deposition; pericyte loss; mast cell infiltration

**Three vasoactive pathway imbalances (the PAH triad):**
- **ET-1 excess:** Endothelial ET-1 production ↑ → ETA-mediated vasoconstriction + SMC proliferation; ETB-mediated endothelial clearance of ET-1 is also reduced (compound effect)
- **NO deficiency:** eNOS uncoupling + ↑PDE5 expression in pulmonary arteries → ↓cGMP → ↑vasoconstriction + proliferation; sGC expression also reduced
- **PGI2 deficiency:** ↓Prostacyclin synthase (PTGIS/CYP8A1) → ↓PGI2 → ↓IP receptor-cAMP signaling → ↑SMC proliferation + ↑platelet aggregation (thrombus in situ)

**BMPR2/BMP9 genetic axis (heritable PAH):**
- **BMPR2 (BMP receptor type 2):** Chromosome 2q33; ~75% of familial PAH and ~15-25% of IPAH carry pathogenic BMPR2 mutations (autosomal dominant, ~20% penetrance); BMPR2 → SMAD1/5/8 → ID1/2 target genes → anti-proliferative + anti-apoptotic programs in pulmonary endothelium; BMPR2 loss → endothelial apoptosis + SMC proliferation → PAH
- **BMP9 (GDF2; chr10q11.22):** Circulating BMP ligand for BMPR2; BMP9 mutations (loss-of-function) → PAH (classified as HPAH type 5); BMP9/BMPR2 axis is the primary anti-remodeling pathway in pulmonary endothelium
- Sotatercept (ActRIIA-Fc fusion; Merck): binds BMP9 ligand trap (traps activin A/B, ligands that compete with BMP9 for BMPR2) → restores BMPR2 pro-survival signaling; **STELLAR trial** (NEJM 2023): 38% improvement in 6MWD; first therapy showing modified RV remodeling; FDA-approved March 2024

**In situ thrombosis:** Platelet-rich microthrombi in small pulmonary arteries (platelet ↓PGI2 sensitivity + ↑TXA2) → contributes to vascular obliteration; anticoagulation historically recommended for IPAH/HPAH (current guidelines selective — not universal)

### Risk stratification (ESC/ERS 2022)

**Four-strata model (low/intermediate-low/intermediate-high/high risk):**
Key variables: WHO functional class (I-IV), 6-minute walk distance (6MWD), NT-proBNP/BNP, echocardiographic RV parameters, hemodynamics (PVR, CI, mRAP), and exercise capacity

**Low risk targets** (goal of therapy):
- WHO FC I-II
- 6MWD >440 m
- NT-proBNP <300 pg/mL (or BNP <50 pg/mL)
- Cardiac index ≥2.5 L/min/m²; mRAP <8 mmHg; PVR <4 WU
- No pericardial effusion

## Function

### Treatment — Three-pathway combination

**Initial combination therapy (standard of care for newly diagnosed treatment-naive WHO FC II-III):**

**ERA + PDE5i dual therapy:**
- **AMBITION trial:** Ambrisentan (ERA) + tadalafil (PDE5i) vs. either monotherapy → 50% reduction in clinical failure events at 24 weeks (primary endpoint); combination superior to monotherapy
- Now guideline-recommended as initial oral combination for most PAH patients

**Endothelin receptor antagonists (ERA):**
- **Ambrisentan (Letairis):** ETA-selective; 5-10 mg QD; FDA-approved 2007; ARIES-1/2 trials: +44 m 6MWD
- **Bosentan (Tracleer):** Dual ETA+ETB; 62.5-125 mg BID; FDA-approved 2001 (first oral PAH therapy); BREATHE-1: +54 m 6MWD; hepatotoxicity monitoring required monthly
- **Macitentan (Opsumit):** Dual ETA+ETB; highly lipophilic → tissue penetration; 10 mg QD; SERAPHIN trial: 45% reduction in morbidity/mortality composite (primary endpoint) vs. placebo

**PDE5 inhibitors:**
- **Sildenafil (Revatio):** 20 mg TID; inhibits PDE5 (predominant in pulmonary vasculature) → ↓cGMP degradation → ↑NO-mediated vasodilation; SUPER-1 trial: +45 m 6MWD
- **Tadalafil (Adcirca):** 40 mg QD; longer half-life (t½ 17.5h); PHIRST trial: +33 m 6MWD; preferred for daily dosing

**sGC stimulators:**
- **Riociguat (Adempas; Bayer):** Directly stimulates soluble guanylate cyclase (sGC) independent of NO and sensitizes sGC to endogenous NO → ↑cGMP; FDA-approved 2013 for both PAH and CTEPH (unique dual approval); PATENT-1 trial: +36 m 6MWD + significant PVR reduction; contraindicated with PDE5 inhibitors (additive hypotension risk)

**Prostacyclin pathway:**
- **Epoprostenol (Flolan, Veletri; IV PGI2):** Continuous IV infusion via tunneled catheter; t½ ~3-5 min (requires continuous pump); first PAH therapy to demonstrate mortality reduction (McLaughlin 2002); ORR ~80% in WHO FC III-IV; still gold standard for severe disease
- **Treprostinil (Remodulin; SC/IV; Orenitram; oral; Tyvaso; inhaled):** Chemically stable PGI2 analog; multiple formulations; subcutaneous infusion most common
- **Iloprost (Ventavis; inhaled):** 2.5-5 µg Q2-3h during waking hours; 6-9 inhalations/day
- **Selexipag (Uptravi; oral non-prostanoid IP receptor agonist):** [^sitbon-2015-selexipag-griphon]: IP receptor selectivity (avoids EP3 receptor — cardiac); GRIPHON trial (1156 patients, largest PAH outcome trial): 40% reduction in morbidity/mortality composite at a median ~1.4 years; FDA-approved Dec 2015; selexipag is a prodrug hydrolyzed to active MRE-269 (ACT-333679) — 37× more potent at IP receptor vs. selexipag

**Novel agents:**
- **Sotatercept (Winrevair; ActRIIA-Fc; Merck):** Trap for activin A/B → restoration of BMPR2/BMP9 → rebalanced pro/anti-proliferative signaling in pulmonary endothelium; STELLAR trial: +34.4 m 6MWD (mean difference vs. placebo); significant NT-proBNP reduction, PVR reduction; **FDA approval March 2024** for WHO FC II-III PAH; adds to ERAs + PDE5i
- **Ralinepag (oral IP agonist):** Phase 3 ADVANCE trial (vs. selexipag)

**Initial triple combination (WHO FC IV or rapid clinical deterioration):**
- ERA + PDE5i + IV epoprostenol; aggressive up-front approach in high-risk PAH
- Sequential addition vs. initial combination: AMBITION shows initial combination superior

**Lung transplantation:**
- For patients unresponsive to maximal combination therapy; bilateral sequential lung transplant preferred; 5-year survival ~50%; PAH recurs in 10-20% of transplanted lungs if immune-mediated mechanisms persist

### Supportive management

- **Supplemental O2:** Target SpO2 >92%; reduces hypoxic vasoconstriction (important in Group 3 overlap)
- **Diuretics:** For RV volume overload and edema; careful to avoid preload reduction impairing RV output
- **Digoxin:** Improves cardiac output in acute RV failure; limited evidence for chronic use
- **Supervised rehabilitation:** Exercise training (low-resistance aerobic) → improved 6MWD and QoL; safe in stable WHO FC II-III PAH

## Pathology

**RV failure (cor pulmonale):**
- Progressive PVR elevation → RV dilation and hypertrophy → tricuspid regurgitation → reduced cardiac output → systemic venous hypertension → ascites, edema, hepatic congestion
- **Pericardial effusion:** Present in 33-50% of advanced PAH; sign of poor prognosis; large effusions can cause tamponade
- RV failure is the primary cause of death in PAH; management: IV inotropy (milrinone, dobutamine), atrial septostomy (palliative; creates right-to-left shunt to decompress RV)

**CTEPH (Group 4) vs. PAH (Group 1):**
- CTEPH: organized thrombus and fibrous tissue obstruction of major pulmonary arteries; diagnosed by V/Q scan + CT pulmonary angiography; treatment: pulmonary endarterectomy (PEA; surgical — first-line for operable CTEPH), balloon pulmonary angioplasty (BPA for inoperable), riociguat (only approved medical therapy for CTEPH)
- Key distinction: PAH has plexiform lesions and microvascular disease; CTEPH has macrovascular organized thrombus

**Pulmonary veno-occlusive disease (PVOD) and PCH:**
- Rare subtypes of Group 1 PAH: PVOD (postcapillary component; pulmonary venous involvement); PCH (pulmonary capillary hemangiomatosis); both have BMPR2/EIF2AK4 mutations; prone to pulmonary edema with vasodilator therapy; poor prognosis; lung transplant recommended

## Connections

- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — ET-1 overproduction by PAH endothelium → ETA on pulmonary VSM → vasoconstriction + medial hypertrophy + adventitial fibrosis → elevated PVR; ERAs (bosentan, ambrisentan, macitentan) are first-line oral therapy for PAH; macitentan reduces morbidity/mortality 45% (SERAPHIN trial).
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Impaired eNOS and NO bioavailability in PAH endothelium → cGMP vasodilation failure; PDE5 inhibitors (sildenafil, tadalafil) prevent cGMP degradation → sustained vasodilation + anti-proliferative; sGC stimulators (riociguat) amplify NO-sGC-cGMP independent of endogenous NO.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — PAH endothelium produces insufficient PGI2 (prostacyclin) → IP receptor → cAMP → vasodilation and anti-proliferative; IV epoprostenol (Flolan) reduces mortality in severe PAH; inhaled iloprost, SC/IV treprostinil; selexipag (oral IP agonist) reduces morbidity 40% (GRIPHON trial).
- `targets` → **[Lung](../../06-organ/lung/README.md)** — PAH is a disease of the pulmonary vasculature; medial hypertrophy, intimal fibrosis, adventitial fibrosis, and plexiform lesions in pulmonary arterioles (<500 µm) → fixed obliterative vascular disease → RV pressure overload → cor pulmonale → right heart failure.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — SSc is the most common cause of CTD-PAH (10-15% of SSc patients); SSc-PAH treated with ERAs + PDE5i (macitentan, ambrisentan + tadalafil); worse prognosis than IPAH; annual echocardiographic screening recommended for all SSc patients.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Ang-1/Ang-2 imbalance in PAH: Ang-2 overexpression in pulmonary endothelium → Tie2 destabilization → endothelial mesenchymal transition → vascular remodeling; Ang-2 overexpressing mice develop PAH; plasma Ang-2 correlates with hemodynamic severity in PAH patients.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Activin A/B are elevated in PAH pulmonary vasculature; activin → VSMC ActRIIB/ALK4 → SMAD2/3 → proliferation and vasoconstriction → vascular remodeling; sotatercept (ActRIIB-Fc; FDA 2024) traps activin A/B → reverses vascular remodeling; STELLAR trial: +34.4 m 6MWD, p<0.001.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — PAH kills through the right heart: obliterated pulmonary arterioles raise vascular resistance until the thin-walled right ventricle, never built for high afterload, hypertrophies, dilates, and fails (cor pulmonale) — so RV function, not pulmonary pressure, best predicts survival.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Pulmonary endothelial dysfunction initiates PAH: injured endothelium underproduces vasodilators (NO, prostacyclin) and overproduces endothelin-1, and apoptosis-resistant clones form the plexiform lesions — so all three drug classes target endothelial signaling pathways.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Pulmonary artery smooth muscle cells drive PAH remodeling: under endothelin, activin, and growth-factor signaling they proliferate and resist apoptosis, thickening the media and muscularizing non-muscular arterioles — sotatercept (activin trap) reverses this remodeling.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Unresolved pulmonary emboli cause a distinct, surgically curable pulmonary hypertension: chronic thromboembolic PH (CTEPH) arises when organized clots obstruct and remodel pulmonary arteries, so every PAH workup includes a V/Q scan—CTEPH is cured by endarterectomy.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV is an established cause of pulmonary arterial hypertension: even with controlled viral loads, HIV proteins like Tat and Nef injure pulmonary endothelium and drive the same plexiform remodeling as idiopathic PAH, so HIV-PAH is a recognized WHO Group 1 subtype.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Pulmonary hypertension is a deadly complication of sickle cell disease: chronic hemolysis scavenges nitric oxide and releases free hemoglobin and arginase, so pulmonary vascular tone rises—an elevated tricuspid regurgitant jet marks patients at high mortality risk.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — PAH and juvenile polyposis converge on the BMP/TGF-β pathway: heritable PAH is most often caused by BMPR2 loss, and SMAD4/BMPR1A mutations can yield a combined JPS-HHT syndrome with PAH—BMP disruption linking gut polyps and pulmonary vascular disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — PAH ultimately kills through right heart failure: the thickened, narrowed pulmonary arteries raise resistance the right ventricle must pump against, so it hypertrophies, dilates and fails—right-heart function, not lung pressure alone, determines survival in PAH.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — PAH is a feared complication of connective-tissue disease, including lupus: immune-mediated injury remodels the pulmonary arteries, so SLE and systemic sclerosis patients are screened with echocardiography—CTD-associated PAH is a major cause of their mortality.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin drives pulmonary arterial hypertension: it constricts and remodels pulmonary arteries, and the appetite suppressants (fen-phen) that flooded the circulation with serotonin caused an epidemic of PAH—cementing the serotonin pathway as a disease driver.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia worsens pulmonary hypertension via a unique reflex: unlike systemic vessels, pulmonary arteries constrict when oxygen is low, so chronic hypoxia sustains vasoconstriction and vascular remodeling—why supplemental oxygen helps.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Pulmonary hypertension ultimately kills through the right ventricle: the right heart's cardiomyocytes hypertrophy then fail against the high pulmonary pressure, so cor pulmonale and right heart failure—not the lung itself—are the usual cause of death in PAH.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF marks the disordered vessels of pulmonary arterial hypertension: the plexiform lesions that obstruct small pulmonary arteries are foci of dysregulated VEGF-driven endothelial proliferation, reflecting how PAH is a vascular-remodeling, not just vasoconstrictive, disease.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Pulmonary arterial hypertension is the vascular disease of the respiratory system: remodeling of the lung's small arteries raises pulmonary pressure, so breathlessness and hypoxemia arise even though the airways and alveoli themselves may be normal.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Pulmonary arterial hypertension is a disease of the lesser circulation within the cardiovascular system: it raises pressure in the pulmonary arteries, not the systemic circuit, so its targeted vasodilators relax the lung's vessels rather than lowering body-wide pressure.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Liver disease can cause pulmonary hypertension: portal hypertension from cirrhosis leads to portopulmonary hypertension, where vasoactive substances bypassing the liver remodel the pulmonary arteries—an important PAH subtype affecting transplant eligibility.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Heritable PAH is a TGF-beta/BMP imbalance: loss of BMPR2 signaling tips the balance toward TGF-beta-driven proliferation of pulmonary vascular cells, the core lesion behind the disease and the target of activin-pathway drugs like sotatercept.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Adventitial fibroblasts complete PAH's vascular remodeling: alongside thickening endothelium and smooth muscle, activated fibroblasts in the outer arterial wall proliferate and stiffen the vessel, narrowing the lumen that raises pulmonary pressure.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Pulmonary arterial hypertension can begin with a potassium channel: KCNK3 mutations cause heritable PAH, and closing potassium channels constricts pulmonary artery smooth muscle—the same switch that drives hypoxic pulmonary vasoconstriction.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Pulmonary arterial hypertension involves in-situ platelet thrombosis: platelets clump in the narrowed small pulmonary arteries and release serotonin and thromboxane that further constrict and remodel them, adding clotting to the vascular disease.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Low oxygen drives pulmonary hypertension through HIF: hypoxia stabilizes HIF-1alpha, which reprograms pulmonary artery cells toward proliferation and constriction—why lung disease and high altitude raise pulmonary pressure.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF drives the artery-thickening of pulmonary hypertension: it pushes pulmonary smooth muscle cells to proliferate and migrate, narrowing the vessels, which is why PDGF-blocking kinase inhibitors like imatinib were tested for the disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Perivascular macrophages inflame the pulmonary hypertension vessel: they cuff the remodeling arteries and pour out cytokines and growth factors that drive the proliferation, adding inflammation to the vasoconstriction and remodeling.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Pulmonary hypertension drags down the kidneys: as the failing right heart backs blood up into the veins, congestion and low forward flow injure the kidneys (cardiorenal syndrome), and worsening renal function marks a poor prognosis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Pulmonary vessels constrict through calcium: calcium entry contracts the arterial smooth muscle, and calcium-channel blockers can help the vasoreactive minority of PAH patients who respond to them.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Pulmonary hypertension can black out the brain: a failing right heart cannot raise output on exertion, so the brain is briefly starved of blood, causing the exertional dizziness and syncope of advanced disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Pulmonary hypertension scars its arteries: the remodeling thickens and fibroses the pulmonary arterial walls, narrowing them in the obliterative arteriopathy that raises the pressure relentlessly.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons measure and classify the pressure: echocardiography estimates it noninvasively, right heart catheterization under fluoroscopy confirms it, and a V/Q scan distinguishes clot-driven chronic thromboembolic disease from true arterial hypertension.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen drives pulmonary hypertension's female bias: the disease strikes women far more often, and the 'estrogen paradox' — the hormone and its metabolites both protecting the heart yet promoting the arterial remodeling — is central to its puzzling sex difference.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Losing the spleen can set the stage: splenectomy is a recognized risk factor for pulmonary hypertension, as the platelets and abnormal red cells no longer filtered by the spleen promote the in-situ thrombosis that remodels the lung arteries.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency haunts PAH even without anemia: it is common in these patients and independently predicts worse exercise capacity and survival, making iron status a routine thing to measure and correct.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Remodeling stiffens the lung's arteries with matrix: the diseased vessels lay down excess collagen and elastin in their walls, a fibrotic thickening that narrows the lumen and hardens the pulmonary circuit the right heart must push against.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — When PAH springs from a heart defect, the blood thickens: the chronic hypoxia of Eisenmenger physiology spurs the marrow to overproduce red cells, and the resulting secondary erythrocytosis adds viscosity and clot risk to the strained circulation.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Autoantibodies point to a cause: much PAH is connective-tissue-disease-associated, so an ANA panel with anti-centromere and anti-Scl-70 antibodies is checked to uncover the scleroderma or lupus driving the pulmonary vessels' disease.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy is perilous in PAH: the volume and output demands overwhelm the fixed, narrowed pulmonary circuit, carrying a maternal mortality so high that pregnancy is strongly discouraged and reliable contraception is part of management.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Fainting marks a failing circuit: when the right heart can no longer push enough blood through the stiffened lungs, exertion starves the brain's neurons of flow, and the exertional syncope that results is an ominous, late-stage warning sign.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation remodels the lung vessels: IL-6 is elevated in pulmonary arterial hypertension and drives the smooth-muscle and endothelial proliferation that narrows the arteries, an inflammatory arm of the disease that tracks with severity and is a therapeutic target.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Thyroid disease keeps company with PAH: both autoimmune hypo- and hyperthyroidism are over-represented in pulmonary arterial hypertension, so thyroid function is checked, since correcting it can ease the cardiovascular strain.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells gather in the diseased arteries: they accumulate around the remodeled pulmonary vessels and plexiform lesions of PAH, releasing mediators that fuel the proliferation and fibrosis narrowing the lumen.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — A developmental switch drives the vessel narrowing: Notch3 signaling pushes pulmonary smooth-muscle cells to proliferate and resist apoptosis, thickening the arterial wall — a remodeling pathway being explored as a therapeutic target in PAH.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Faulty immune restraint lets the arteries inflame: a deficiency of regulatory T cells permits the perivascular inflammation that drives pulmonary vascular remodeling, one reason PAH clusters with autoimmune diseases like scleroderma and lupus.
- `connects-to` → **[COPD](../copd/README.md)** — Chronic lung disease raises the pressure too: in COPD, alveolar destruction and chronic hypoxia constrict and remodel the pulmonary arteries, producing the group-3 pulmonary hypertension that worsens breathlessness and strains the right heart.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The inflammasome stokes vascular remodeling: NLRP3-driven IL-1β release in the pulmonary artery wall promotes the perivascular inflammation and smooth-muscle proliferation that narrow the vessels in PAH.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Chronic hemolysis drives pulmonary hypertension: like sickle cell disease, thalassemia releases cell-free hemoglobin that scavenges nitric oxide, and with post-splenectomy thrombosis it produces a hemolysis-associated PAH.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Stimulants can scar the lung vessels: methamphetamine and other stimulants are an established cause of pulmonary arterial hypertension, producing a drug-induced form indistinguishable from the idiopathic disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 remodels the vessel through it: the elevated IL-6 of PAH signals via JAK-STAT3 in pulmonary artery smooth muscle and endothelium, driving the proliferative obliteration of small vessels that raises pressure.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — A failing right heart backs up into the kidneys: the venous congestion and low output of advanced PAH and cor pulmonale impair renal perfusion, a cardiorenal mechanism that drives chronic kidney disease.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic inflammation drags the hemoglobin down: the IL-6 milieu of PAH raises hepcidin and blunts erythropoiesis, and the resulting anemia of chronic disease worsens oxygen delivery and is a marker of poor prognosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A breathless, life-limiting disease weighs on mood: the relentless exertional limitation, poor prognosis and demanding therapy of PAH give it among the highest depression and anxiety rates in chronic cardiopulmonary illness.
- `connects-to` → **[Stroke](../stroke/README.md)** — Right-heart pressure can shunt clots to the brain: when PAH opens a patent foramen ovale into a right-to-left shunt, venous clots bypass the lungs and reach the cerebral arteries, causing paradoxical embolic stroke.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Its continuous prostacyclin needs a permanent line: severe PAH is treated with non-stop intravenous epoprostenol through an indwelling central catheter, which is a standing portal for bloodstream infection and catheter-related sepsis.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Clonal blood disease is a recognised cause: myeloproliferative neoplasms feature in Group 5 pulmonary hypertension, driving PAH through abnormal cells, splenectomy and high-output states.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — Chronic hypoxic lung damage pressurises the pulmonary bed: the bronchiectasis and persistent hypoxaemia of advanced cystic fibrosis cause hypoxic pulmonary vasoconstriction and Group 3 pulmonary hypertension with cor pulmonale.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A breathless, life-limiting disease breeds worry: the relentless dyspnoea, fear of right-heart failure and burdensome continuous therapy of PAH foster chronic health anxiety alongside depression.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The liver both causes and suffers it: cirrhosis with portal hypertension causes portopulmonary hypertension, and right-heart failure from PAH congests the liver and gut, causing ascites and malabsorption.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It clusters with thyroid disease: both hyper- and hypothyroidism are over-represented in pulmonary arterial hypertension, and thyroid dysfunction can worsen its haemodynamics.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — A fixed low output starves the brain: severe PAH cannot raise cardiac output on exertion, so exertional syncope and presyncope from cerebral hypoperfusion are ominous warning signs.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The failing right heart backs up into the kidney: systemic venous congestion and reduced cardiac output in PAH impair renal function as a cardiorenal syndrome, worsening fluid overload.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Autoimmunity is a major cause: connective-tissue diseases such as scleroderma and lupus drive PAH through inflammatory and immune-mediated remodelling of the pulmonary arteries.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It shows on skin and at the drip site: connective-tissue-disease PAH brings sclerodactyly and telangiectasia, hypoxaemia causes cyanosis and clubbing, and continuous prostacyclin infusions cause skin and line-site reactions.
- `connects-to` → **[Calcium-channel Blockers](../../../03-medicine/01-modern/04-cardio/calcium-channel-blockers/README.md)** — A subset responds to vasodilators: the minority of idiopathic PAH patients who are vasoreactive on testing benefit from high-dose calcium-channel blockers.
- `connects-to` → **[Warfarin](../../../03-medicine/01-modern/09-hematology/warfarin/README.md)** — Anticoagulation has a historical role: warfarin was traditionally used in idiopathic pulmonary arterial hypertension to counter in-situ thrombosis, though its benefit is now debated.
- `connects-to` → **[Loop Diuretics](../../../03-medicine/01-modern/04-cardio/loop-diuretics/README.md)** — They unload the failing right heart: as PAH causes right-ventricular failure, loop diuretics like furosemide relieve peripheral oedema, ascites, and congestion, though over-diuresis can drop the preload-dependent RV output.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It is a disease of the arterial wall: PAH remodels small pulmonary arteries with intimal fibrosis, medial smooth-muscle hypertrophy, and plexiform lesions that progressively narrow the lumen and raise pulmonary pressures.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Myeloproliferative disease can drive it: polycythaemia vera and related MPNs cause group-5 pulmonary hypertension through hyperviscosity, splenomegaly, and chronic thromboembolic obstruction of the pulmonary vasculature.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Breathlessness wastes the muscles: severe PAH causes profound exercise limitation and peripheral muscle deconditioning, and advanced right-heart failure brings cardiac cachexia.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It kills through the right heart: pulmonary arterial hypertension forces the right ventricle to pump against high resistance, driving RV hypertrophy then dilatation and failure (cor pulmonale)—the myocardial decline that determines survival.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — It loosens the tricuspid valve: as the right ventricle dilates under pulmonary arterial hypertension, the tricuspid annulus stretches and the valve leaks, and the severity of this functional regurgitation tracks the pressure overload.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — A rare route to PAH: tuberous sclerosis causes lymphangioleiomyomatosis (LAM), whose smooth-muscle proliferation destroys lung tissue and can produce pulmonary hypertension, linking the mTOR-driven syndrome to the pulmonary vasculature.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — The gas-exchange interface: PAH's remodelled small pulmonary arteries sit beside the alveoli, and hypoxic pulmonary vasoconstriction—the alveolar oxygen response—drives the pressure rise in lung-disease-associated PAH.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Right-heart arrhythmia: progressive right-ventricular strain and dilatation in PAH cause atrial arrhythmias and conduction delay (right bundle branch block), worsening an already failing right heart.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — A rare NF1 association: neurofibromatosis type 1 is a recognised, often severe cause of pulmonary arterial hypertension, adding a vasculopathy to its tumour and skin features.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Portopulmonary hypertension: cirrhosis and portal hypertension arising in the hepatic lobule can drive Group 1 pulmonary arterial hypertension, a complication that critically affects candidacy for liver transplantation.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Pulmonary vascular insult: severe COVID-19 injures the pulmonary microvasculature and strains the right heart, and established PAH patients tolerate the added load poorly, making infection especially dangerous.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Cardiorenal backflow: the failing right ventricle of advanced PAH raises systemic venous pressure, congesting the kidney and injuring the glomerulus in a cardiorenal syndrome that worsens fluid overload.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Apoptosis then resistance: early caspase-3-mediated endothelial apoptosis, followed by emergence of apoptosis-resistant proliferating cells, drives the plexiform vascular remodelling of PAH.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Proliferative signalling: PI3K-AKT-mTOR activation drives the smooth-muscle and endothelial proliferation that narrows pulmonary arterioles in PAH.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — Right-heart strain marker: BNP and NT-proBNP rise as the pressure-loaded right ventricle stretches in PAH, serving as key biomarkers for risk stratification and treatment response.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Vascular inflammation: TNF-α contributes to the perivascular inflammation and pulmonary-artery remodelling that narrow the vessels in PAH.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammasome-driven remodelling: IL-1β from the activated NLRP3 inflammasome promotes the pulmonary-arterial inflammation and remodelling of PAH, an emerging therapeutic target.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes and macrophages into the remodelling pulmonary-artery wall in PAH, fuelling the inflammation that drives vascular narrowing.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Adrenomedullin rises in PAH as a counter-regulatory pulmonary vasodilator and anti-proliferative peptide, and its circulating levels track right-ventricular strain and disease severity—making it both a compensatory mediator and a prognostic marker.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — RAAS-driven aldosterone excess in PAH promotes pulmonary-vascular and right-ventricular fibrosis and impairs endothelial nitric-oxide signaling, the rationale for mineralocorticoid-receptor antagonists being studied in the disease.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Inflammation-driven hepcidin elevation causes the functional iron deficiency common in PAH, which independently predicts worse exercise capacity and survival regardless of anemia—linking the disease's inflammatory state to a treatable comorbidity.
- `connects-to` → **[SERCA2a](../../03-molecular/serca2a/README.md)** — As the pressure-loaded right ventricle decompensates in PAH, SERCA2a is downregulated and calcium reuptake fails, impairing RV contractility and relaxation—the maladaptive remodeling that ultimately determines survival in the disease.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Xanthine oxidase activity is raised in PAH, generating reactive oxygen species and the hyperuricemia whose serum urate level correlates with pulmonary hemodynamic severity and prognosis.
- `connects-to` → **[von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — The diseased pulmonary endothelium of PAH releases von Willebrand factor and supports the in-situ thrombosis of small pulmonary arteries, with raised vWF levels marking endothelial injury and adverse outcome.
- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — HIF-2α/EPAS1 is a master driver of the pulmonary vascular remodeling of PAH and hypoxic pulmonary hypertension, and gain-of-function EPAS1 variants cause heritable pulmonary hypertension.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — BMPR2 and TGF-β signals converge on SMAD4, and the loss of BMP-SMAD signaling with preserved TGF-β-SMAD signaling drives the proliferative vasculopathy that sotatercept (rebalancing the activin-A arm already mapped) aims to correct.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGF2-FGFR signaling drives the endothelial and smooth-muscle-cell proliferation of the plexiform lesions of PAH, an angiogenic growth-factor axis acting alongside the PDGF and VEGF already mapped.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — PDGF and FGF (both mapped) signal through the MAPK-ERK cascade to drive the pulmonary-artery smooth-muscle proliferation of PAH, the rationale behind PDGFR-inhibitor (imatinib) trials.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K-AKT-mTOR signaling (AKT already mapped) sustains the survival and proliferation of the remodeled pulmonary vascular cells in PAH.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The apoptosis-resistant, proliferative pulmonary-artery smooth-muscle and endothelial cells of PAH show E2F-driven cell-cycle activity reminiscent of a cancer-like phenotype.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 already mapped) drives the proliferative pulmonary vascular remodeling of pulmonary arterial hypertension.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB-driven inflammation in the pulmonary vasculature sustains the perivascular immune-cell recruitment and cytokine production that promote the vascular remodeling of PAH.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling counters the oxidative stress (xanthine-oxidase already mapped) that contributes to endothelial dysfunction and smooth-muscle proliferation in pulmonary arterial hypertension.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 drives the pulmonary-vascular and right-ventricular fibrosis of pulmonary arterial hypertension and is a biomarker of disease severity.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT and mTOR mapped) promotes the pulmonary-arterial-smooth-muscle proliferation that obliterates the vessel lumen in PAH.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation in the pulmonary vascular wall contributes to the perivascular inflammation and remodeling of pulmonary arterial hypertension.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING amplifies the perivascular inflammation that drives the vascular remodeling of pulmonary arterial hypertension.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — Downregulation of FOXO1 in pulmonary-artery smooth-muscle cells drives the apoptosis-resistant, proliferative phenotype central to pulmonary arterial hypertension.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling contributes to the interferon and immune component of the pulmonary vascular inflammation of pulmonary arterial hypertension.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling contributes to the proliferative, apoptosis-resistant phenotype of the pulmonary-artery smooth-muscle cells in pulmonary arterial hypertension.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the perivascular inflammation that drives the vascular remodeling of pulmonary arterial hypertension.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D-driven proliferation of pulmonary-artery smooth-muscle cells contributes to the occlusive vascular remodeling of pulmonary arterial hypertension.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the proliferation and apoptosis resistance of the pulmonary-artery smooth-muscle and endothelial cells in pulmonary arterial hypertension.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of PDGFR and other receptors (PDGF already mapped) contributes to the vascular remodeling of pulmonary arterial hypertension.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the Warburg-like metabolic shift of the remodeled pulmonary vasculature in pulmonary arterial hypertension.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the pulmonary-vascular-cell survival and proliferation in the vascular remodeling of pulmonary arterial hypertension.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the perivascular inflammation of pulmonary arterial hypertension.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the pulmonary-vascular-cell phenotype in pulmonary arterial hypertension.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the perivascular inflammatory-cell recruitment and vascular remodeling of pulmonary arterial hypertension.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the vascular gene programs relevant to pulmonary arterial hypertension.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the perivascular inflammation and vascular remodeling of pulmonary arterial hypertension.
- `connects-to` → **[Serotonin transporter](../../03-molecular/serotonin-transporter/README.md)** — Serotonin hypothesis: the serotonin transporter (SERT) delivers 5-HT (serotonin already mapped) into pulmonary artery smooth muscle to drive proliferation, and SERT is the mechanistic link behind anorexigen (fenfluramine)-associated pulmonary arterial hypertension.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Channelopathy: loss-of-function mutations in the KCNK3/TASK-1 potassium channel cause heritable pulmonary arterial hypertension, since impaired potassium efflux depolarises smooth muscle to raise calcium and promote vasoconstriction and remodeling.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Right-heart failure: pulmonary arterial hypertension ultimately kills through right ventricular failure, and troponin released from the strained, ischaemic RV myocardium is a prognostic biomarker linking the pulmonary vasculopathy to cardiac decompensation.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Vasodilator deficit: calcitonin gene-related peptide is a potent pulmonary vasodilator, and its relative deficiency contributes to the vasoconstriction of pulmonary arterial hypertension, complementing the endothelin/nitric-oxide/prostacyclin pathways already mapped.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — RAAS activation: the renin-angiotensin-aldosterone system (aldosterone already mapped) is activated in pulmonary arterial hypertension, and angiotensin II promotes the vascular remodelling and right-ventricular fibrosis that worsen the disease.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic dysfunction: pulmonary arterial hypertension is associated with insulin resistance and a shift toward glycolytic metabolism in the pulmonary vessels and right ventricle, a metabolic dimension increasingly recognised in its pathobiology.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Hypoxaemia and iron: chronic hypoxaemia in pulmonary arterial hypertension can raise haemoglobin through secondary erythrocytosis, while the common iron deficiency (hepcidin already mapped) impairs oxygen delivery and worsens outcomes.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — In-situ thrombosis: the pulmonary arteriopathy of pulmonary arterial hypertension carries a prothrombotic tendency with in-situ microthrombi, and reduced natural anticoagulants such as protein C (von Willebrand factor already mapped) contribute to this thrombotic component.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 vascular remodelling: IL-13 and the type-2 inflammatory response promote the pulmonary vascular smooth-muscle (already mapped) proliferation and remodelling, adding to the inflammatory drive (IL-6 already mapped) of pulmonary arterial hypertension.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 inflammation: IL-4, with IL-13 (already mapped), drives the type-2 inflammatory arm that promotes the pulmonary vascular smooth-muscle (already mapped) remodelling, part of the inflammatory pathobiology of pulmonary arterial hypertension.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — RAAS in right-heart failure: the renin-angiotensin-aldosterone system (angiotensin II and aldosterone already mapped) is activated in the right-heart failure of pulmonary arterial hypertension, contributing to the fluid retention and remodelling.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Vasoreactivity and calcium channels: the small vasoreactive subset of pulmonary arterial hypertension responds to calcium-channel blockers, and calcium handling in the pulmonary-artery smooth muscle (already mapped) underlies the vasoconstriction targeted.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine and sex bias: leptin, with the oestrogen (already mapped) metabolism, is implicated in the female predominance and the metabolic dimension of pulmonary arterial hypertension, part of its adipokine dysregulation.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Protective adipokine: adiponectin, with leptin (already mapped), modulates the pulmonary-vascular remodelling, and its dysregulation is part of the metabolic contribution to pulmonary arterial hypertension.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Vascular inflammation: resistin, with leptin and adiponectin (already mapped), is a pro-inflammatory adipokine implicated in the pulmonary-vascular inflammation and remodelling of pulmonary arterial hypertension.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — In-situ thrombosis: the in-situ thrombosis of the small pulmonary arteries (von Willebrand factor and protein C already mapped) contributes to the vascular occlusion of pulmonary arterial hypertension, the historical rationale for anticoagulation.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon-associated PAH: type-I interferon, both the therapy-induced and the connective-tissue-disease (systemic sclerosis already mapped) associated, is linked to the pulmonary vascular remodelling of pulmonary arterial hypertension.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Autoimmune vascular inflammation: the CD4 T cells and the Th17/regulatory dysregulation are implicated in the pulmonary-vascular inflammation of PAH, especially the connective-tissue-disease (systemic sclerosis already mapped) associated form.
- `connects-to` → **[IL-17a](../../03-molecular/il-17a/README.md)** — Th17 vascular inflammation: the IL-17 of the Th17 cells (T-helper cell already mapped) drives the perivascular inflammation and the remodelling of the pulmonary arteries in PAH.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 vascular inflammation: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the immune-mediated pulmonary-vascular inflammation of PAH.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the pulmonary-vascular inflammation of PAH.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune-mediated pulmonary-vascular inflammation of PAH.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the pulmonary-vascular inflammation and remodelling of PAH.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the pulmonary-vascular inflammation of PAH.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the pulmonary-vascular inflammation and endothelial (already mapped) injury of PAH.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement to the perivascular myeloid recruitment in the pulmonary-vascular remodelling of PAH.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Perivascular antigen presentation: the dendritic cells accumulate in the perivascular infiltrates and present antigen to the T cells (already mapped) in the inflammatory pulmonary-vascular remodelling of PAH.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active on the remodelling pulmonary vasculature of PAH.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron deficiency: transferrin, the iron carrier, reflects the iron-deficiency (hepcidin already mapped) that is a common, prognostically important comorbidity of pulmonary arterial hypertension.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Perivascular T cells: the cytotoxic T cells (perforin pathway) of the perivascular infiltrates contribute to the adaptive-immune component of the pulmonary-vascular remodelling of PAH.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Perivascular alarmin: TSLP released by inflamed pulmonary vascular endothelium promotes mast-cell degranulation and Th2 skewing within the perivascular infiltrates that drive the vascular remodelling of pulmonary arterial hypertension.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Vasodilatory paradox: bradykinin, whose pulmonary degradation by ACE is impaired in PAH, accumulates at the remodelling vascular wall, driving the cough and paradoxical vasodilation that limits ACE-inhibitor use in this condition.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Hypoxia erythrocytosis: erythropoietin, upregulated by the chronic pulmonary hypoxia (HIF-1α already mapped) of PAH, drives the secondary polycythaemia that initially compensates oxygen delivery but ultimately worsens blood viscosity.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement and contact-activation brake: C1-esterase inhibitor restrains the complement (C3, C5 and C5aR1 already mapped) and kallikrein-kinin (bradykinin already mapped) pathways that amplify the endothelial injury and perivascular inflammation of PAH.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Perivascular mast-cell mediator: histamine released by perivascular mast cells (already mapped) promotes endothelial permeability (endothelin-1 already mapped), smooth muscle cell (already mapped) proliferation and angiogenesis in PAH lesions.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Vascular remodelling ECM: periostin, induced by TGF-β and PDGF (both already mapped) in the PAH vascular wall, promotes smooth muscle cell (already mapped) migration and the matrix stiffness that drives the progressive vascular occlusion of PAH.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — PAH melatonin: melatonin via MT1/MT2 on pulmonary arterial smooth muscle cells (already mapped) and endothelium (endothelin-1 already mapped) modulates circadian vasoconstriction and ROS (xanthine-oxidase already mapped)-driven vascular remodelling of PAH.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — PAH androgen axis: testosterone via androgen receptor on pulmonary vascular smooth muscle cells (already mapped) exerts vasodilatory effects that contrast the estrogen (already mapped)-driven PAH susceptibility and female sex predominance.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — PAH prolactin: prolactin, via JAK2 (already mapped) signalling on pulmonary arterial smooth muscle cells (already mapped), promotes their survival and proliferation, amplifying the anti-apoptotic vascular remodelling driven by PDGF (already mapped) in PAH.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — PAH oxytocin: oxytocin via OXTR on pulmonary vascular endothelium (endothelin-1 already mapped) and smooth muscle cells (already mapped) promotes vasodilation, counteracting the endothelin-1 and PDGF (already mapped)-driven vascular remodelling of PAH.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — PAH vasopressin: vasopressin via V1aR on pulmonary arterial smooth muscle cells (already mapped) promotes vasoconstriction and proliferation, amplifying the endothelin-1 (already mapped) and PDGF (already mapped)-driven pulmonary vascular remodelling of PAH.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — PAH selenium: selenium-dependent glutathione peroxidase (GPX) quenches endothelial reactive-oxygen-species driving eNOS (nitric oxide already mapped) uncoupling and PDGF (already mapped)-mediated smooth muscle cell (already mapped) proliferation in PAH.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — PAH iodine: iodine-dependent thyroid hormones regulate endothelial cells (already mapped) and smooth muscle cells (already mapped); thyroid-hormone deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) vascular remodelling cascade of PAH.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — PAH sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the PDGF (already mapped) and endothelin-1 (already mapped) vascular remodelling cascade of PAH.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — PAH magnesium: magnesium, as eNOS (nitric-oxide already mapped) cofactor in endothelial cells (already mapped) and smooth muscle cells (already mapped), supports vasodilation; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PAH.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — PAH copper: copper, as lysyl oxidase cofactor in endothelial cells (already mapped) and smooth muscle cells (already mapped), drives pulmonary vascular ECM remodelling; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PAH.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — PAH phosphorus: phosphorus-dependent ATP in endothelial cells (already mapped) and smooth muscle cells (already mapped) sustains vascular-tone signalling; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) vascular-remodelling cascade of PAH.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — PAH zinc: zinc, as metalloproteinase cofactor in macrophages (already mapped) and smooth muscle cells (already mapped), regulates pulmonary ECM remodelling; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) vascular-remodelling cascade of PAH.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^galie-2015-esc-pah-guidelines]: Galie N, Humbert M, Vachiery JL, et al. 2015 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. *Eur Heart J.* 2016;37(1):67-119. [doi:10.1093/eurheartj/ehv317](https://doi.org/10.1093/eurheartj/ehv317) · [PubMed 26320113](https://pubmed.ncbi.nlm.nih.gov/26320113/)
[^simonneau-2019-pah-classification]: Simonneau G, Montani D, Celermajer DS, et al. Haemodynamic definitions and updated clinical classification of pulmonary hypertension. *Eur Respir J.* 2019;53(1):1801913. [doi:10.1183/13993003.01913-2018](https://doi.org/10.1183/13993003.01913-2018) · [PubMed 30545968](https://pubmed.ncbi.nlm.nih.gov/30545968/)
[^sitbon-2015-selexipag-griphon]: Sitbon O, Channick R, Chin KM, et al. Selexipag for the Treatment of Pulmonary Arterial Hypertension. *N Engl J Med.* 2015;373(26):2522-2533. [doi:10.1056/NEJMoa1503184](https://doi.org/10.1056/NEJMoa1503184) · [PubMed 26579977](https://pubmed.ncbi.nlm.nih.gov/26579977/)
