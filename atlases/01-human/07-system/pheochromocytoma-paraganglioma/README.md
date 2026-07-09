---
schema: human-scale-entry/v1
id: pheochromocytoma-paraganglioma
name: Pheochromocytoma/Paraganglioma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Pheochromocytoma/paraganglioma are chromaffin cell tumors; ~40% hereditary (SDHx, VHL, RET, NF1); biochemical diagnosis: plasma/urine metanephrines; sunitinib (FIRSTMAPPP) and 177Lu-DOTATATE for metastatic disease; alpha-adrenergic blockade mandatory preoperatively."
aliases: ["pheochromocytoma", "paraganglioma", "PHEO", "PGL", "PHEO/PGL", "chromaffin tumor", "hereditary paraganglioma", "catecholamine-secreting tumor", "adrenal pheochromocytoma", "head-neck paraganglioma", "SDHx tumor", "MEN2 pheochromocytoma"]
sources:
  - id: lenders-2014-pheo-guideline
    type: peer-reviewed
    cite: "Lenders JW, Duh QY, Eisenhofer G, et al. Pheochromocytoma and paraganglioma: an endocrine society clinical practice guideline. J Clin Endocrinol Metab. 2014;99(6):1915-1942."
    doi: "10.1210/jc.2014-1498"
    pmid: "24893135"
    url: "https://doi.org/10.1210/jc.2014-1498"
  - id: baudin-2021-firstmappp-sunitinib
    type: peer-reviewed
    cite: "Baudin E, Goichot B, Berruti A, et al. First International Randomized Study in Malignant Progressive Pheochromocytoma and Paragangliomas (FIRSTMAPPP). Ann Oncol. 2021;32(10):1245-1254."
    doi: "10.1016/j.annonc.2021.07.009"
    pmid: "34246769"
    url: "https://doi.org/10.1016/j.annonc.2021.07.009"
cross_links:
  - target: 01-human/03-molecular/sdhb
    relation: connects-to
    note: "Hereditary PHEO/PGL caused by SDHB biallelic LOF → PGL4 syndrome; SDHB germline carriers: ~30-40% develop malignant PHEO/PGL (vs <5% SDHD/SDHC); highest malignant risk of all SDHx loci; SDHB IHC (granular cytoplasmic staining) used for initial SDH-deficient tumor screening."
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "VHL-mutant PHEO/PGL: Cluster 1 pseudohypoxia; bilateral PHEO in ~10-20% VHL patients; VHL type 2C (missense): PHEO-only phenotype; VHL-mutant PHEO is predominantly norepinephrine-secreting; sunitinib active in VHL-mutant metastatic PHEO/PGL; 68Ga-DOTATATE PET for staging."
  - target: 01-human/03-molecular/ret
    relation: connects-to
    note: "RET mutations in PHEO/PGL: Cluster 2 kinase signaling; RET M918T (MEN2B, most aggressive) or C634F/Y (MEN2A) → PHEO in ~40-50% MEN2A/B; epinephrine-predominant secretion; bilateral adrenal PHEO; prophylactic adrenalectomy in MEN2B; vandetanib/cabozantinib active in MTC."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "PHEO/PGL Cluster 1 (SDHx, VHL) activate HIF-1α by pseudohypoxia → VEGF, GLUT1 transcription; HIF-1α drives tumor angiogenesis; HIF-1α target expression predicts malignant behavior; 18F-FDG PET avidity in SDHB-mutant PHEO correlates with HIF-1α-driven metabolic reprogramming."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Pheochromocytomas arise in the adrenal medulla from chromaffin cells, pouring epinephrine and norepinephrine into the adrenal vein; surgery demands 10-14 days of alpha-adrenergic blockade first (beta only after) to prevent intraoperative hypertensive crisis."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Neurofibromatosis type 1 is a Cluster 2 (kinase-signaling) hereditary pheochromocytoma syndrome: ~3-4% of NF1 patients develop adrenal, epinephrine-secreting PHEO; loss of neurofibromin's RAS-GAP activity drives the chromaffin tumor, paralleling RET-driven MEN2 PHEO."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Chromaffin tumors synthesize epinephrine and norepinephrine but are best detected by their continuously produced O-methylated metabolites — plasma free metanephrines (~97-99% sensitive); paroxysmal catecholamine surges cause episodic hypertension, palpitations, and headache."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Pheochromocytoma/paraganglioma and clear-cell RCC are linked by pseudohypoxia: VHL loss (and SDHx/FH defects) stabilizes HIF-2α even in normoxia, driving VEGF and a hypervascular tumor in both; VHL disease produces them together, and HIF-2α inhibitors like belzutifan treat both."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "VHL disease is a leading hereditary cause of pheochromocytoma/paraganglioma: germline VHL loss drives Cluster-1 pseudohypoxia, producing bilateral, often norepinephrine-secreting PHEO in 10-20% alongside clear-cell RCC — so young or bilateral PHEO warrants VHL testing."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Pheochromocytoma/paraganglioma and neuroblastoma are both neural-crest, catecholamine-handling sympathoadrenal tumors that take up MIBG and secrete catecholamine metabolites, but PPGL is an adult chromaffin tumor while neuroblastoma is an aggressive embryonal cancer of children."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Pheochromocytoma is the classic curable secondary cause of hypertension: episodic catecholamine release produces the paroxysmal triad of headache, palpitations, and sweating with severe spikes, so resistant or paroxysmal hypertension warrants plasma/urine metanephrine screening."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Paragangliomas appear in Carney-related syndromes—but not Carney complex itself: the SDH-deficient Carney triad (paraganglioma, gastric GIST, pulmonary chondroma) and Carney-Stratakis dyad are distinct from PRKAR1A-driven Carney complex, a common point of confusion."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "Pheochromocytoma/paraganglioma and HLRCC share a pseudohypoxia mechanism: both belong to the TCA-cycle tumor family where SDH or FH loss accumulates succinate/fumarate, inhibits HIF prolyl-hydroxylases, and stabilizes HIF—rarely yielding FH-mutant PPGL itself."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Pheochromocytoma is defined by the catecholamines it secretes: chromaffin tumors release norepinephrine and epinephrine, driving paroxysmal hypertension, while their breakdown products are the diagnostic test—an unregulated norepinephrine factory."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Pheochromocytoma is the organic disease that most convincingly mimics panic disorder: surges of catecholamines cause sudden palpitations and a sense of doom identical to a panic attack, so atypical 'panic' with hypertension warrants metanephrine testing."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "Paraganglioma and GIST are joined in Carney triad: SDH-deficient tumors—paragangliomas plus wild-type GISTs—arise together when succinate dehydrogenase loss drives pseudohypoxia, so finding one SDH-deficient tumor prompts a search for the other."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1 is one of several genes causing hereditary pheochromocytoma: neurofibromin loss (like RET, VHL and SDH mutations) predisposes to catecholamine-secreting tumors, so a pheochromocytoma should prompt genetic testing—up to a third are hereditary."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Pheochromocytoma can devastate the heart: catecholamine surges cause hypertensive crises, arrhythmias and a stress (Takotsubo) cardiomyopathy, so the tumor's adrenaline output threatens the heart—and alpha-blockade before surgery prevents catastrophic crises."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "Pheochromocytoma belongs to MEN2, not MEN1: it arises with medullary thyroid cancer in RET-driven MEN2, whereas MEN1 (menin) causes parathyroid, pituitary and pancreatic tumors—so the two MEN syndromes are distinguished partly by whether pheochromocytoma occurs."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Pheochromocytoma is a cardiovascular emergency in waiting: surges of catecholamines cause paroxysmal hypertension, palpitations and arrhythmia, and can trigger catecholamine cardiomyopathy or crisis—so alpha-blockade before surgery is essential to prevent fatal swings."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Paragangliomas arise along the autonomic nervous system: these tumors grow in sympathetic and parasympathetic paraganglia (from adrenal medulla to carotid body), so they are neural-crest tumors of the nervous system that happen to flood the body with catecholamines."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Pheochromocytoma is a hormone-secreting tumor of the endocrine adrenal medulla: it autonomously pours catecholamines into blood, so it belongs among the functional endocrine tumors and clusters in syndromes (MEN2, VHL, NF1) with other endocrine neoplasia."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Pheochromocytoma and paraganglioma are imaged and treated with radioactive iodine via MIBG: these catecholamine-handling tumors take up I-123/I-131 metaiodobenzylguanidine, lighting them up on scans and delivering targeted radiation in metastatic disease."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Many paragangliomas express SSTR2, opening a second nuclear-medicine route: 68Ga-DOTATATE PET often detects SDHx-related and head-and-neck tumors better than MIBG, and 177Lu-DOTATATE delivers peptide receptor radiotherapy in metastatic cases."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Pheochromocytoma and paraganglioma spring from neural-crest lineage: the chromaffin and paraganglion cells share an origin with neurons of the sympathetic nervous system, which is why these tumors secrete catecholamines like nerve cells do."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Some pheochromocytomas and paragangliomas secrete dopamine: especially SDHB-driven head-and-neck tumors release dopamine and its metabolite 3-methoxytyramine, a biochemical signature that flags a hereditary, more malignant-prone tumor."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Pheochromocytoma-paraganglioma is tied to oxygen sensing: carotid-body paragangliomas are literal oxygen sensors, and SDH/VHL mutations fake low oxygen (pseudohypoxia), stabilizing HIF to drive the 'cluster 1' hereditary tumors."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Pheochromocytomas are intensely vascular through VEGF: pseudohypoxic HIF signaling pumps out VEGF, so these tumors are richly perfused and prone to bleeding—and anti-angiogenic drugs are tried against metastatic disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Pheochromocytomas dump catecholamines via calcium: chromaffin cells release adrenaline by calcium-triggered exocytosis, so the tumor's surges of hormone—and the spells of pounding blood pressure they cause—run on this calcium-dependent machinery."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages fill the pheochromocytoma's vascular stroma: drawn into the richly perfused, pseudohypoxic tumor, they support its blood supply and shape an immune niche of interest in the hard-to-treat metastatic disease."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Pheochromocytoma punishes the kidneys through catecholamines: the surges of adrenaline and noradrenaline drive severe hypertension that damages the kidney's vessels, and extra-adrenal paragangliomas can also arise near the renal hilum."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Pheochromocytoma can stroke the brain: its surges of adrenaline spike blood pressure into hypertensive encephalopathy and hemorrhage, and skull-base paragangliomas can press directly on the brain."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Pheochromocytoma poisons heart-muscle cells: the flood of catecholamines overdrives cardiomyocytes into a stress (catecholamine) cardiomyopathy, sometimes the presenting crisis of the tumor."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Adrenaline from a pheochromocytoma shifts potassium: catecholamine surges drive potassium into cells, dropping blood levels and, with the BP spikes, fueling the dangerous arrhythmias of a crisis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons localize the catecholamine factory: CT and the bright T2 'light-bulb' on MRI find the mass, while Ga-68 DOTATATE PET and MIBG scintigraphy light up its receptors to map multifocal and metastatic disease before surgery."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals where the adrenaline is kept: the tumor cells are crammed with dense-core neurosecretory granules — membrane-bound packets of catecholamine — the ultrastructure that confirms a chromaffin-cell origin."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bone is where malignant paraganglioma goes: especially with SDHB mutations, these tumors metastasize to the skeleton, seeding the marrow-filled bones of the spine and pelvis as the commonest site of spread."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The pseudohypoxic tumors can thicken the blood: pheochromocytomas and paragangliomas driven by HIF stabilization — and the EPAS1-mutant Pacak-Zhuang form especially — overproduce erythropoietin, pushing the marrow to make excess red cells and cause polycythemia."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Besides bone, the liver takes the spread: malignant paragangliomas, again most often SDHB-mutant, seed hepatic metastases, a site that — like the skeleton — marks the tumor as having crossed from benign to malignant."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The catecholamine spells reach the skin: surges of adrenaline and noradrenaline drive the classic triad of pounding headache, palpitations, and drenching sweat, while clamped-down vessels leave the patient pale and clammy during an attack."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains confirm the chromaffin tumor: chromogranin A and synaptophysin mark its neuroendocrine nature on biopsy, and loss of SDHB staining flags the hereditary, more aggressive paragangliomas worth genetic testing."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "A catecholamine storm can strike the brain: a hypertensive crisis from the tumor spikes blood pressure into hemorrhagic stroke or the posterior reversible encephalopathy syndrome, an emergency that sometimes unmasks the hidden pheochromocytoma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium tames the surgical surge: intravenous magnesium sulfate blunts catecholamine release and the arrhythmias it provokes, making it a key adjunct during the perilous handling of the tumor at operation."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy can turn a pheochromocytoma deadly: an undiagnosed tumor unleashes catecholamine crises during labor and delivery, historically with high maternal and fetal mortality, and the many hereditary forms pass to offspring — so genetic counseling matters."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "RET ties the adrenal medulla to the thyroid: in MEN2, a germline RET mutation causes pheochromocytoma alongside medullary thyroid carcinoma, so finding one tumor triggers a hunt — and prophylactic thyroidectomy — for the other."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "One molecular cluster of these tumors runs on kinase signaling: RET, NF1, TMEM127 and MAX mutations drive PI3K-AKT-mTOR activation, the growth-signaling group that contrasts with the pseudohypoxic, HIF-driven SDH and VHL cluster."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "The catecholamine flood disrupts sugar control: adrenaline and noradrenaline suppress insulin release and drive glycogen breakdown, so pheochromocytoma often causes hyperglycemia and secondary diabetes that resolves once the tumor is removed."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomere genes flag the dangerous ones: TERT and ATRX alterations mark the pheochromocytomas and paragangliomas most likely to metastasize, helping pick out aggressive tumors in a disease where malignancy is otherwise hard to predict."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "They are intensely vascular tumors: pseudohypoxic SDH and VHL mutations crank up VEGF, so endothelial cells build a dense blood supply — making these tumors hemorrhagic at surgery and their angiogenesis a therapeutic target."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "EPAS1 anchors the pseudohypoxia cluster: gain-of-function HIF-2α (EPAS1) mutations cause pheochromocytoma/paraganglioma — sometimes with polycythemia (Pacak-Zhuang) — by mimicking a low-oxygen state that drives the tumor."
  - target: 01-human/03-molecular/fh
    relation: connects-to
    note: "Another Krebs-cycle gene joins the cluster: FH mutations, like SDH, flood the cell with an oncometabolite that stabilizes HIF, placing FH-mutant pheochromocytoma/paraganglioma in the pseudohypoxic, often aggressive subgroup."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Catecholamines can stun the heart: the adrenaline surges of pheochromocytoma cause a catecholamine cardiomyopathy (including takotsubo) that can precipitate acute heart failure, often reversible once the tumor is removed."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Some of these tumors secrete IL-6: an IL-6-producing pheochromocytoma can cause fever, weight loss and an inflammatory syndrome driven through JAK-STAT3, a paraneoplastic picture that resolves once the tumor is resected."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A pheo crisis can masquerade as septic shock: catecholamine storm produces fever, lactic acidosis and multi-organ failure that mimic sepsis, a dangerous mimicry since the usual fluids-and-pressors response can worsen the crisis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Years of catecholamine hypertension scar the kidney: sustained or paroxysmal pressure surges from the tumor drive hypertensive nephrosclerosis, and the renal damage can persist as chronic kidney disease even after cure."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its catecholamines and surgery thicken the clotting risk: chronic adrenergic stimulation activates platelets and coagulation, and the major operation to resect the tumor adds perioperative immobility, together raising venous thromboembolism risk."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Catecholamine excess unsettles the mind: the surges that cause palpitations and panic also disturb mood, and patients commonly carry anxiety and depressive symptoms before diagnosis that can linger after the tumor is removed."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Catecholamines and HIF-pathway tumors can pressurize the lungs: adrenergic surges acutely constrict the pulmonary vasculature, and the EPAS1/HIF-2α paraganglioma syndromes are described alongside pulmonary hypertension."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Removing the tumour is high-stakes surgery: adrenalectomy or paraganglioma resection requires careful alpha-blockade to prevent intra-operative hypertensive crisis, and the abdominal wound must heal afterwards."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Years of catecholamine hypertension scar the arteries: the sustained and paroxysmal blood-pressure surges of a phaeochromocytoma accelerate endothelial injury and atherosclerotic vascular damage."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Adrenergic excess paralyses the gut: high circulating catecholamines suppress intestinal motility in phaeochromocytoma, causing severe constipation and occasionally pseudo-obstruction or ischaemic colitis."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its attacks sweat and blanch the skin: the classic phaeochromocytoma triad pairs headache and palpitations with profuse diaphoresis, and adrenergic vasoconstriction causes episodic pallor of the skin."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "A catecholamine crisis floods the lungs: a phaeochromocytoma crisis can precipitate catecholamine cardiomyopathy with flash pulmonary oedema and acute respiratory distress."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Catecholamines tremble the body and tumours seed bone: adrenergic excess causes the fine tremor of phaeochromocytoma, and metastatic SDHB-related paraganglioma spreads to the skeleton."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Catecholamine surges scar the kidney: sustained and paroxysmal hypertension drives hypertensive nephrosclerosis, and paragangliomas can arise in the renal bed near the kidney."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Malignant disease spreads to the nodes: there is no benign histology — malignancy is defined by spread, and SDHB-mutated paragangliomas in particular metastasise to lymph nodes and bone."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "Order of blockade is life-or-death: beta-blockers must be given only after alpha-blockade in phaeochromocytoma, because unopposed alpha stimulation from beta-blockade first can precipitate a hypertensive crisis."
  - target: 03-medicine/01-modern/04-cardio/calcium-channel-blockers
    relation: connects-to
    note: "They help control the surges: calcium-channel blockers assist in managing the paroxysmal hypertension of phaeochromocytoma, after alpha-blockade and before any beta-blocker is added."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Metastatic disease gets targeted treatment: MIBG radiotherapy, somatostatin-receptor PRRT and kinase inhibitors such as sunitinib treat unresectable phaeochromocytoma and paraganglioma."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "It belongs to the neuroendocrine family: phaeochromocytomas and paragangliomas are catecholamine-secreting neuroendocrine tumours, sharing somatostatin-receptor imaging and PRRT with other NETs."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for malignant disease: the cyclophosphamide-vincristine-dacarbazine (CVD) regimen treats metastatic phaeochromocytoma and paraganglioma, alongside MIBG and peptide-receptor radionuclide therapy."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Two routes to too many red cells: EPAS1 (HIF2A)-mutant paragangliomas can drive erythropoietin-mediated polycythaemia (Pacak-Zhuang syndrome), a secondary erythrocytosis distinct from the JAK2-driven polycythaemia vera."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy for the aggressive few: metastatic phaeochromocytoma and paraganglioma, though rare, are being trialled with PD-1 checkpoint inhibitors when other options are exhausted."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Catecholamines poison the heart muscle: sustained adrenaline and noradrenaline from a phaeochromocytoma cause catecholamine cardiomyopathy and Takotsubo-like myocardial stunning, which can present as acute heart failure before the tumour is found."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "It also destabilises the heart's wiring: catecholamine surges from a phaeochromocytoma trigger tachyarrhythmias and dangerous blood-pressure swings, which is why alpha-blockade must precede any beta-blocker to avoid unopposed vasoconstriction."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "A pseudohypoxic, oncometabolite tumour: SDH-deficient paraganglioma accumulates succinate that, like the 2-hydroxyglutarate of IDH-mutant glioma, inhibits α-ketoglutarate dioxygenases and stabilises HIF—two cancers driven by a metabolite."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Catecholamine vasculopathy: the noradrenaline surges of phaeochromocytoma cause severe vasoconstriction and hypertensive crises that damage the arterial wall, with pressure spikes risking stroke and aortic dissection."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Hypertensive nephropathy: sustained and paroxysmal catecholamine hypertension transmits to the glomerulus, scarring it over time, while SDH and VHL also predispose to the kidney's own tumours."
  - target: 01-human/07-system/men4-syndrome
    relation: connects-to
    note: "Another endocrine-tumour syndrome: like MEN1, MEN4 (CDKN1B loss) can include phaeochromocytoma and paraganglioma among its parathyroid and pituitary tumours, joining the germline syndromes that spawn them."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Metastatic bone disease: malignant paraganglioma, especially SDHB-mutated, has a striking predilection for bone metastases, often osteolytic lesions in the cortical bone that drive functional imaging and treatment."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver as a metastatic site: alongside bone, the liver is a leading destination for malignant phaeochromocytoma and paraganglioma, the tumour seeding the hepatic lobule in metastatic SDHB-driven disease."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Crisis under stress: any severe illness including COVID-19 can precipitate a catecholamine crisis in an unrecognised phaeochromocytoma, the surge causing dangerous hypertension, arrhythmia and cardiomyopathy."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Pseudohypoxic epigenetics: in SDH-deficient PPGL, accumulated succinate inhibits histone demethylases and, with EZH2/polycomb, drives the DNA/histone hypermethylator phenotype shared with IDH- and FH-mutant tumours."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Kinase-signalling group: alongside NF1 and RET, RAS-MAPK activation defines the kinase-signalling cluster of PPGL, with HRAS/KRAS mutations in some sporadic tumours."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Angiogenic RTK target: PDGFR and VEGFR signalling drive the rich vasculature of PPGL, the basis for multikinase inhibitors such as sunitinib in metastatic disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK output: the RET, NF1 and RAS lesions of the kinase-signalling PPGL cluster converge on ERK1/2, driving the proliferation of these neuroendocrine tumours."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative oncogene: MYC activation downstream of the kinase and pseudohypoxic pathways helps drive the growth of pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: cyclin D1-CDK4/6 activity propels PPGL tumour cells through the G1 checkpoint, the proliferative output of their driver pathways."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "Oxygen-sensor pseudohypoxia: germline EGLN1/PHD2 mutations cause a pseudohypoxic PPGL subtype (sometimes with polycythaemia) by failing to hydroxylate HIF, locking in the hypoxia-response programme that drives these tumours."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Wnt-altered subtype: somatic MAML3 fusions and CSDE1 mutations define a Wnt-signalling PPGL cluster distinct from the pseudohypoxia and kinase groups, associated with more aggressive behaviour."
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "Telomere maintenance and metastasis: ATRX mutations in PPGL engage the alternative-lengthening-of-telomeres pathway and mark the aggressive, metastasis-prone tumours, often co-occurring with SDHB-related disease."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Kinase-cluster driver: loss of TMEM127 — a recurrent PPGL susceptibility gene — disinhibits mTORC1, placing a subset of these tumours in the kinase-signalling group alongside RET and NF1, distinct from the pseudohypoxic SDHx/VHL cluster."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: connects-to
    note: "Catecholamine effector: the epinephrine and norepinephrine secreted by PPGL act on β1-adrenergic receptors to drive the tachycardia and hypertension of catecholamine crisis, which is why β-blockade is added only after α-blockade to avoid unopposed vasoconstriction."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "Oncometabolite parallel: SDH-deficient PPGL accumulates succinate that inhibits 2-oxoglutarate dioxygenases and stabilises HIF, the same pseudohypoxic, epigenetic mechanism by which IDH-mutant tumours act through their oncometabolite 2-hydroxyglutarate."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Kinase-signalling subtype: the RET-, NF1- and RAS-driven cluster of PPGL activates PI3K-AKT-mTOR through PIK3CA, the proliferative arm complementing the pseudohypoxia pathway and a node addressable by PI3K/mTOR inhibition."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Catecholamine cardiotoxicity: paroxysmal catecholamine surges from PPGL can cause Takotsubo-like stress cardiomyopathy and myocardial injury, releasing troponin from damaged myocytes — the biochemical signature of the cardiac complications of pheochromocytoma crisis."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Catecholamine hyperglycaemia: excess catecholamines suppress pancreatic insulin secretion via α2-adrenergic receptors and induce insulin resistance, producing the hyperglycaemia and secondary diabetes of PPGL that typically resolve after tumour resection."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Kinase-cluster restraint: PTEN limits the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped) that is activated in the kinase-signalling (cluster 2) PPGL driven by RET, NF1 and RAS (all mapped)."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oncometabolite-NRF2: in SDH- and FH-deficient (cluster 1) PPGL, accumulated succinate and fumarate succinate KEAP1 to activate NRF2 (SDHB and FH mapped), an antioxidant programme of the pseudohypoxic tumours."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle output: the cyclin-D1 axis (mapped) releases E2F1 to drive proliferation, the engine of growth shared across the hereditary clusters of pheochromocytoma and paraganglioma."
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "Oncometabolite cluster: IDH mutations generate 2-hydroxyglutarate that, like the succinate of SDHx and fumarate of FH (both already mapped), stabilises HIF and reprograms the epigenome in the pseudohypoxia cluster of pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Metastatic progression: dysregulation of the RB1-E2F checkpoint (cyclin-D1 and E2F1 already mapped) accompanies progression toward metastatic pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "STAT3 survival: JAK-STAT3 signalling (STAT3 already mapped) contributes to the survival signalling of pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is expressed in pheochromocytoma/paraganglioma and contributes to tumour-cell survival and microenvironment interactions."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β signalling modulates the proliferation and microenvironment of pheochromocytoma and paraganglioma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment relevant to emerging immunotherapy in pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of pheochromocytoma/paraganglioma, relevant to its emerging immunotherapy."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) shapes the microenvironment of the pseudohypoxic pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate the oxidative and metabolic stress of the SDH/VHL-driven pseudohypoxia of pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt signaling of the pseudohypoxic pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation restrains apoptosis in pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is a component of the immune response to pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation, prominent in the SDH-deficient CpG-methylator subtype, of pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival of the pseudohypoxic, SDH/VHL-deficient cells of pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic (pseudohypoxic) adaptation of pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of RET and other receptor tyrosine kinases (RET already mapped) participates in the proliferative signaling of pheochromocytoma/paraganglioma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of pheochromocytoma and paraganglioma."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal and pseudohypoxic interactions of pheochromocytoma and paraganglioma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of pheochromocytoma and paraganglioma."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Secretory trigger: adrenal chromaffin cells are innervated by cholinergic splanchnic preganglionic fibres, so acetylcholine is the physiological signal that evokes catecholamine exocytosis, the pathway whose dysregulated tumour activity underlies paroxysmal secretion."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Co-secreted vasoconstrictor: neuropeptide Y is stored and released alongside catecholamines by pheochromocytoma and sympathetic paraganglia, contributing to the vasoconstriction and hypertension and serving as an additional secretory marker beyond the metanephrines."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Exocytosis and MEN2: calcium influx triggers the granule exocytosis releasing catecholamines from chromaffin cells, and in RET-driven MEN2 the tumour co-occurs with parathyroid hyperplasia and calcium dysregulation, linking secretion to syndromic mineral endocrinology."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPAS1 polycythaemia: EPAS1/HIF2-driven paragangliomas (EPAS1 already mapped) can secrete erythropoietin, causing the polycythaemia of the Pacak-Zhuang syndrome, a distinctive pseudohypoxic feature of this tumour subtype."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Metastatic immunotherapy: MHC class II antigen presentation shapes the T-cell response to metastatic pheochromocytoma/paraganglioma, for which checkpoint and other immunotherapies are being explored given the limited options for malignant disease."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell therapy: IL-2-driven T-cell expansion supports the immunotherapy approaches under investigation for metastatic paraganglioma, complementing MIBG and peptide-receptor radionuclide therapy (SSTR2 already mapped)."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Paraganglia origin: paragangliomas arise from the paraganglia distributed along the sympathetic chain and parasympathetic nerves (head, neck, thorax, abdomen), the peripheral autonomic tissue whose chromaffin and glomus cells give rise to these tumours."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Polycythaemia: some pseudohypoxic pheochromocytomas and paragangliomas secrete erythropoietin (already mapped) or activate HIF, raising haemoglobin, and the Pacak-Zhuang syndrome links EPAS1-driven tumours (already mapped) to polycythaemia."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Adrenal and RAAS context: as an adrenal cause of secondary hypertension, pheochromocytoma sits alongside the aldosterone-driven primary aldosteronism of the adrenal cortex, and catecholamines stimulate renin and the aldosterone axis (angiotensin already in the RAAS)."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "RAAS activation: catecholamines from the tumour stimulate renin and the renin-angiotensin-aldosterone system (aldosterone already mapped), and angiotensin II compounds the vasoconstriction and hypertension (already mapped) of pheochromocytoma."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "Catecholamine-driven renin: the beta-adrenergic (already mapped) stimulation of renin release by the tumour catecholamines activates the RAAS (angiotensin II and aldosterone already mapped), part of the mechanism of the hypertension in pheochromocytoma."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the microenvironment of the metastatic SDHB-driven (already mapped) pheochromocytoma-paraganglioma dampens the anti-tumour immune response, part of the immune biology relevant to its emerging immunotherapy."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Emerging immunotherapy: the cytotoxic T cells (perforin already mapped) are the target of the checkpoint immunotherapy explored in metastatic SDHB-driven (already mapped) pheochromocytoma-paraganglioma, which the immunosuppressive stroma (IL-10 already mapped) limits."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the metastatic pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of pheochromocytoma-paraganglioma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Catecholamine biosynthesis: copper is the cofactor of dopamine-β-hydroxylase, which makes the noradrenaline from the dopamine (both already mapped), the copper-dependent catecholamine biosynthesis of the chromaffin tumours."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Catecholamine hypermetabolism: leptin reflects the metabolic effects of the catecholamine (already mapped) excess — the hypermetabolism and weight loss — of pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the catecholamine-driven metabolic disturbance of pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the catecholamine-driven metabolic disturbance of pheochromocytoma-paraganglioma."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "EPO-erythrocytosis iron: the erythropoietin (already mapped)-secreting pheochromocytoma-paraganglioma (and the pseudohypoxia HIF already mapped) can drive the erythrocytosis, consuming the iron for the increased erythropoiesis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of the malignant pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity of the malignant pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 effector: IL-17A is the Th17 effector cytokine complementing the Th1/type-2 (IFN-γ, IL-4, IL-5 and IL-13 already mapped) balance of the immune microenvironment of pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 arm) of the inflammatory dimension of the pheochromocytoma-paraganglioma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of pheochromocytoma-paraganglioma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of pheochromocytoma-paraganglioma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the highly vascular pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Tumour complement: the complement C3 activation contributes to the inflammatory dimension of the pheochromocytoma-paraganglioma microenvironment."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuroendocrine–immune alarmin: TSLP released in the adrenal medullary and paraganglionic microenvironment is modulated by the catecholamine-driven (noradrenaline/adrenaline already mapped) sympathetic-immune axis of pheochromocytoma-paraganglioma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Catecholamine-co-secreted mediator: histamine is co-secreted with catecholamines by PPGL chromaffin cells and by the abundant intratumoural mast cells, contributing to the flushing and hypertensive crises that mimic carcinoid syndrome."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Vasomotor crisis amplifier: bradykinin, released from intratumoural mast cells and the kinin–kallikrein cascade activated during pheochromocytoma catecholamine surges, amplifies the vasodilation and hypotension of the post-crisis nadir."
---

# Pheochromocytoma/Paraganglioma

## Overview

**Pheochromocytoma (PHEO)** and **paraganglioma (PGL)** are rare catecholamine-secreting neuroendocrine tumors arising from **chromaffin cells** (neural crest-derived, adrenergic-lineage cells). PHEO arises in the adrenal medulla; PGL arises from extra-adrenal paraganglia and is further classified as:
- **Sympathetic PGL**: extra-adrenal abdominal (organ of Zuckerkandl, periaortic), thoracic, pelvic, bladder; catecholamine-secreting; biochemically active
- **Parasympathetic/head-neck PGL (HNPGL)**: carotid body, jugulotympanic, vagal, laryngeal; predominantly non-secretory; located adjacent to parasympathetic ganglia

**Epidemiology:**
- Incidence: ~8-12 per million/year (combined PHEO + PGL); PHEO ~80-85% of chromaffin tumors; PGL ~15-20%
- Most are diagnosed at age 40-50 years; hereditary forms present earlier (20s-30s)
- ~40% are hereditary — the highest proportion of any human tumor type, exceeding even medullary thyroid carcinoma [^lenders-2014-pheo-guideline]
- "Rule of 10s" (historical, now outdated): 10% bilateral, 10% extra-adrenal, 10% malignant, 10% hereditary — modern genetics reveals all four proportions were underestimates

**Hereditary syndromes — genetic testing recommended for ALL patients at diagnosis:**

| Gene | Syndrome | PHEO/PGL type | Malignancy risk | Co-manifestations |
|---|---|---|---|---|
| SDHB | PGL4 | Sympathetic PGL > PHEO | ~30-40% | SDH-deficient GIST (rare) |
| SDHD | PGL1 | HNPGL (parasympathetic) | <5% | Paternal imprinting |
| SDHC | PGL3 | HNPGL | <5% | Low penetrance |
| SDHA | PGL5 | Mixed | ~7-10% | GIST, pituitary adenoma |
| VHL | VHL disease | Bilateral PHEO | <5% | Hemangioblastoma, ccRCC |
| RET | MEN2A/MEN2B | Bilateral adrenal PHEO | <5% | MTC, hyperparathyroidism |
| NF1 | Neurofibromatosis 1 | Adrenal PHEO | <5% | Café-au-lait, Lisch nodules |
| TMEM127 | — | Adrenal PHEO bilateral | Low | Rare |
| MAX | — | Bilateral adrenal PHEO | Low | Paternal imprinting |

## Structure

### Molecular cluster classification

Two major cluster subtypes with distinct biology, secretory profile, and malignancy risk:

**Cluster 1 — Pseudohypoxia/Krebs cycle:**
- Genes: SDHB, SDHD, SDHC, SDHA, SDHAF2 (SDHx), VHL, FH (fumarate hydratase), MDH2
- Mechanism: SDH or VHL LOF → HIF-1α stabilized (pseudohypoxia) → VEGF, GLUT1, EPO (SDHx) or direct VHL E3 ligase failure (VHL)
- Biochemistry: predominantly **norepinephrine-secreting** (or non-secretory in HNPGL)
- Location: often extra-adrenal or bilateral; HNPGL (Cluster 1 SDHD/SDHC)
- Malignancy: highest risk (especially SDHB); multiple tumors
- Imaging: 68Ga-DOTATATE PET (SSTR2-avid); 18F-FDG PET (high avidity in SDHB-mutant due to HIF-1α-driven glycolysis)

**Cluster 2 — Kinase/RAS signaling:**
- Genes: RET, NF1, TMEM127, MAX
- Mechanism: RET tyrosine kinase activation (MEN2) or NF1/RAS hyperactivation → MAPK, PI3K/AKT
- Biochemistry: predominantly **epinephrine-secreting** (adrenal; PNMT expressed)
- Location: adrenal medulla; bilateral
- Malignancy: lower risk (<5-10%); mostly benign
- Imaging: 123I-MIBG (NET-avid, catecholamine transporter intact)

### Adrenal medulla anatomy

The adrenal medulla constitutes ~10-20% of adrenal gland volume (cortex = 80-90%):
- Chromaffin cells are neuroendocrine, modified postganglionic sympathetic neurons
- Secrete epinephrine (~80%) and norepinephrine (~20%) into venous blood (not via synaptic release)
- Chromaffin cells express: tyrosine hydroxylase (TH), dopamine β-hydroxylase (DBH), phenylethanolamine-N-methyltransferase (PNMT — converts NE→E; cortisol-dependent), SSTR2, NET (SLC6A2)
- Blood supply via adrenal vein (into inferior vena cava on right, renal vein on left)

## Function

### Catecholamine biosynthesis and release

Normal chromaffin cell catecholamine synthesis:
Tyrosine → DOPA (TH, rate-limiting) → Dopamine (DOPA decarboxylase) → Norepinephrine (DBH) → Epinephrine (PNMT)

In PHEO/PGL:
- Tumors secrete catecholamines constitutively and episodically
- Metanephrines (normetanephrine, metanephrine, methoxytyramine) are O-methylated metabolites produced continuously within the tumor (via COMT) — superior biomarkers to parent catecholamines
- Parasympathetic HNPGLs secrete dopamine or methoxytyramine (low/absent PNMT); often biochemically silent on NE/E panels

### Biochemical diagnosis

**Plasma free metanephrines** (preferred for hereditary/high-risk patients): sensitivity ~97% (normetanephrine), ~99% (metanephrine); specificity ~85-90%; gold standard for detection; posture affects NE (supine preferred)

**24-hour urinary fractionated metanephrines and catecholamines**: equivalent sensitivity for large tumors; preferred in some labs; interference: catecholamine-containing foods, labetalol, methyldopa, tricyclics

**Methoxytyramine (plasma or urine)**: elevated in dopamine-secreting PGL (often SDHx-driven, HNPGL); rises in metastatic disease; aids malignancy risk stratification

**Biochemical confirmation required before imaging** — chance adrenal incidentalomas ("incidentalomas") and beta-blocker use can cause false-positive elevations; repeat testing on standardized diet (avoid coffee, bananas, vanilla 48h before)

## Pathology

### Surgical management

**Preoperative medical preparation (mandatory, non-negotiable):** [^lenders-2014-pheo-guideline]
Alpha-adrenergic blockade must be established 10-14 days before surgery to prevent intraoperative hypertensive crisis:
- **Phenoxybenzamine** (irreversible α1+α2 blocker): 10-40 mg BID; superior preoperative preparation in most centers; side effects: orthostatic hypotension, reflex tachycardia, nasal congestion
- **Doxazosin** (selective α1 blocker): 2-16 mg QD; fewer side effects; comparable outcomes in many series
- **Beta-blockade** (propranolol, atenolol): initiated ONLY after alpha blockade established (≥3-5 days) to control tachycardia — giving beta-blocker first → unopposed alpha → hypertensive crisis
- **High-sodium diet + IV fluids**: counteract catecholamine-induced plasma volume depletion

**Surgical approach:**
- Laparoscopic adrenalectomy: standard for adrenal PHEO ≤6-8 cm; retroperitoneal endoscopic approach increasingly preferred (direct adrenal access, less bowel manipulation)
- Open adrenalectomy: PHEO >6-8 cm, suspected malignant, extra-adrenal PGL with vascular involvement
- Cortical-sparing adrenalectomy: bilateral PHEO (VHL, MEN2) → preserve adrenal cortex to avoid lifelong glucocorticoid dependence if possible

**Intraoperative management:**
- Anesthesiologist must anticipate catecholamine surges (tumor manipulation) → IV phentolamine (alpha blocker) + nitroprusside/nicardipine for hypertensive crisis; esmolol for tachycardia
- Hypotension after tumor removal (catecholamine withdrawal) → IV fluids + vasopressors

### Malignant PHEO/PGL

**Definition**: presence of metastases in sites where chromaffin tissue is not normally found (regional LN, bone, liver, lung, peritoneum) — no histologic criteria (Ki-67, mitoses, necrosis) reliably predict malignancy

**Risk stratification:**
- SDHB mutation: ~30-40% risk of metastases
- Tumor size >5 cm, extra-adrenal location, norepinephrine-only secretion: higher risk
- **PASS score** (Pheochromocytoma of Adrenal gland Scaled Score) and **GAPP** (grading system for adrenal pheochromocytoma and paraganglioma): pathological scoring systems; moderate predictive value
- 18F-FDG PET avidity: high avidity predicts malignancy in SDHB-mutant tumors

**Imaging for staging and surveillance:**
- 68Ga-DOTATATE PET: first-line functional imaging; superior to 123I-MIBG for staging, especially Cluster 1 tumors
- 123I-MIBG: required if considering 131I-MIBG therapy (must be MIBG-avid); ~30-40% of malignant PHEO are MIBG-negative
- 18F-FDG PET: best for SDHB-mutant and high-grade tumors; correlates with HIF-1α-driven metabolic activity

**Systemic therapy for malignant PHEO/PGL:**

**Sunitinib** (VEGFR1/2/3, PDGFR, KIT, RET inhibitor):
FIRSTMAPPP trial (Baudin 2021) [^baudin-2021-firstmappp-sunitinib]: N=78 progressive malignant PHEO/PGL; sunitinib 37.5 mg/day vs placebo; primary endpoint PFS; HR 0.50 (95% CI 0.28-0.88); p=0.017; 12-month PFS 35.9% vs 19.2%; OS not different (crossover confounded); standard of care for progressive disease

**177Lu-DOTATATE** (lutetium-177 PRRT):
Targets SSTR2 on chromaffin cells; eligibility: 68Ga-DOTATATE PET avid (Krenning score ≥2); ORR ~25-30% in PHEO/PGL series (retrospective); COMPETE trial ongoing; 68Ga-DOTATATE PET superior to 123I-MIBG for eligibility selection in Cluster 1 tumors

**131I-MIBG** (Azedra, high specific activity iobenguane I-131):
FDA-approved 2018 for iobenguane-avid unresectable/metastatic PHEO/PGL ≥12 years; eligibility: 123I-MIBG scan positive; ORR ~25%; main toxicity: bone marrow suppression (stem cell storage recommended); not preferred for SDHB-mutant (often MIBG-negative)

**CVD chemotherapy** (cyclophosphamide + vincristine + dacarbazine):
Oldest regimen; ORR ~37% (biochemical response); PFS ~3-4 months; partial response more common than CR; used in rapidly progressive disease when targeted/PRRT not available

**Cabozantinib** (VEGFR2/MET/RET/AXL):
Active in Cluster 1 (MET/AXL co-expressed in SDH-deficient tumors); Phase 2 CABOPHEN: ORR ~15%, PFS ~5-6 months in malignant PHEO/PGL; also active in RET-driven (Cluster 2) malignant PHEO

**Prognosis:**
- Localized PHEO: 5-year OS ~95%; curative after adrenalectomy
- Malignant PHEO/PGL (all): 5-year OS ~50-60%
- SDHB-mutant malignant: 5-year OS ~20-30%; most aggressive
- SDHD/VHL malignant: intermediate prognosis (~50-70% 5-year OS)
- 20-year surveillance recommended for all SDHx carriers (multiple primaries common)

## Connections

- `connects-to` → **[SDHB](../../03-molecular/sdhb/README.md)** — Hereditary PHEO/PGL caused by SDHB biallelic LOF → PGL4 syndrome; SDHB germline carriers: ~30-40% develop malignant PHEO/PGL (vs <5% SDHD/SDHC); highest malignant risk of all SDHx loci; SDHB IHC (granular cytoplasmic staining) used for initial SDH-deficient tumor screening.
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — VHL-mutant PHEO/PGL: Cluster 1 pseudohypoxia; bilateral PHEO in ~10-20% VHL patients; VHL type 2C (missense): PHEO-only phenotype; VHL-mutant PHEO is predominantly norepinephrine-secreting; sunitinib active in VHL-mutant metastatic PHEO/PGL; 68Ga-DOTATATE PET for staging.
- `connects-to` → **[RET](../../03-molecular/ret/README.md)** — RET mutations in PHEO/PGL: Cluster 2 kinase signaling; RET M918T (MEN2B, most aggressive) or C634F/Y (MEN2A) → PHEO in ~40-50% MEN2A/B; epinephrine-predominant secretion; bilateral adrenal PHEO; prophylactic adrenalectomy in MEN2B; vandetanib/cabozantinib active in MTC.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — PHEO/PGL Cluster 1 (SDHx, VHL) activate HIF-1α by pseudohypoxia → VEGF, GLUT1 transcription; HIF-1α drives tumor angiogenesis; HIF-1α target expression predicts malignant behavior; 18F-FDG PET avidity in SDHB-mutant PHEO correlates with HIF-1α-driven metabolic reprogramming.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Pheochromocytomas arise in the adrenal medulla from chromaffin cells, pouring epinephrine and norepinephrine into the adrenal vein; surgery demands 10-14 days of alpha-adrenergic blockade first (beta only after) to prevent intraoperative hypertensive crisis.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Neurofibromatosis type 1 is a Cluster 2 (kinase-signaling) hereditary pheochromocytoma syndrome: ~3-4% of NF1 patients develop adrenal, epinephrine-secreting PHEO; loss of neurofibromin's RAS-GAP activity drives the chromaffin tumor, paralleling RET-driven MEN2 PHEO.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Chromaffin tumors synthesize epinephrine and norepinephrine but are best detected by their continuously produced O-methylated metabolites — plasma free metanephrines (~97-99% sensitive); paroxysmal catecholamine surges cause episodic hypertension, palpitations, and headache.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Pheochromocytoma/paraganglioma and clear-cell RCC are linked by pseudohypoxia: VHL loss (and SDHx/FH defects) stabilizes HIF-2α even in normoxia, driving VEGF and a hypervascular tumor in both; VHL disease produces them together, and HIF-2α inhibitors like belzutifan treat both.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — VHL disease is a leading hereditary cause of pheochromocytoma/paraganglioma: germline VHL loss drives Cluster-1 pseudohypoxia, producing bilateral, often norepinephrine-secreting PHEO in 10-20% alongside clear-cell RCC — so young or bilateral PHEO warrants VHL testing.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Pheochromocytoma/paraganglioma and neuroblastoma are both neural-crest, catecholamine-handling sympathoadrenal tumors that take up MIBG and secrete catecholamine metabolites, but PPGL is an adult chromaffin tumor while neuroblastoma is an aggressive embryonal cancer of children.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Pheochromocytoma is the classic curable secondary cause of hypertension: episodic catecholamine release produces the paroxysmal triad of headache, palpitations, and sweating with severe spikes, so resistant or paroxysmal hypertension warrants plasma/urine metanephrine screening.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — Paragangliomas appear in Carney-related syndromes—but not Carney complex itself: the SDH-deficient Carney triad (paraganglioma, gastric GIST, pulmonary chondroma) and Carney-Stratakis dyad are distinct from PRKAR1A-driven Carney complex, a common point of confusion.
- `connects-to` → **[HLRCC](../hlrcc/README.md)** — Pheochromocytoma/paraganglioma and HLRCC share a pseudohypoxia mechanism: both belong to the TCA-cycle tumor family where SDH or FH loss accumulates succinate/fumarate, inhibits HIF prolyl-hydroxylases, and stabilizes HIF—rarely yielding FH-mutant PPGL itself.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Pheochromocytoma is defined by the catecholamines it secretes: chromaffin tumors release norepinephrine and epinephrine, driving paroxysmal hypertension, while their breakdown products are the diagnostic test—an unregulated norepinephrine factory.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Pheochromocytoma is the organic disease that most convincingly mimics panic disorder: surges of catecholamines cause sudden palpitations and a sense of doom identical to a panic attack, so atypical 'panic' with hypertension warrants metanephrine testing.
- `connects-to` → **[GIST](../gist/README.md)** — Paraganglioma and GIST are joined in Carney triad: SDH-deficient tumors—paragangliomas plus wild-type GISTs—arise together when succinate dehydrogenase loss drives pseudohypoxia, so finding one SDH-deficient tumor prompts a search for the other.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — NF1 is one of several genes causing hereditary pheochromocytoma: neurofibromin loss (like RET, VHL and SDH mutations) predisposes to catecholamine-secreting tumors, so a pheochromocytoma should prompt genetic testing—up to a third are hereditary.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Pheochromocytoma can devastate the heart: catecholamine surges cause hypertensive crises, arrhythmias and a stress (Takotsubo) cardiomyopathy, so the tumor's adrenaline output threatens the heart—and alpha-blockade before surgery prevents catastrophic crises.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — Pheochromocytoma belongs to MEN2, not MEN1: it arises with medullary thyroid cancer in RET-driven MEN2, whereas MEN1 (menin) causes parathyroid, pituitary and pancreatic tumors—so the two MEN syndromes are distinguished partly by whether pheochromocytoma occurs.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Pheochromocytoma is a cardiovascular emergency in waiting: surges of catecholamines cause paroxysmal hypertension, palpitations and arrhythmia, and can trigger catecholamine cardiomyopathy or crisis—so alpha-blockade before surgery is essential to prevent fatal swings.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Paragangliomas arise along the autonomic nervous system: these tumors grow in sympathetic and parasympathetic paraganglia (from adrenal medulla to carotid body), so they are neural-crest tumors of the nervous system that happen to flood the body with catecholamines.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Pheochromocytoma is a hormone-secreting tumor of the endocrine adrenal medulla: it autonomously pours catecholamines into blood, so it belongs among the functional endocrine tumors and clusters in syndromes (MEN2, VHL, NF1) with other endocrine neoplasia.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Pheochromocytoma and paraganglioma are imaged and treated with radioactive iodine via MIBG: these catecholamine-handling tumors take up I-123/I-131 metaiodobenzylguanidine, lighting them up on scans and delivering targeted radiation in metastatic disease.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — Many paragangliomas express SSTR2, opening a second nuclear-medicine route: 68Ga-DOTATATE PET often detects SDHx-related and head-and-neck tumors better than MIBG, and 177Lu-DOTATATE delivers peptide receptor radiotherapy in metastatic cases.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Pheochromocytoma and paraganglioma spring from neural-crest lineage: the chromaffin and paraganglion cells share an origin with neurons of the sympathetic nervous system, which is why these tumors secrete catecholamines like nerve cells do.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Some pheochromocytomas and paragangliomas secrete dopamine: especially SDHB-driven head-and-neck tumors release dopamine and its metabolite 3-methoxytyramine, a biochemical signature that flags a hereditary, more malignant-prone tumor.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Pheochromocytoma-paraganglioma is tied to oxygen sensing: carotid-body paragangliomas are literal oxygen sensors, and SDH/VHL mutations fake low oxygen (pseudohypoxia), stabilizing HIF to drive the 'cluster 1' hereditary tumors.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Pheochromocytomas are intensely vascular through VEGF: pseudohypoxic HIF signaling pumps out VEGF, so these tumors are richly perfused and prone to bleeding—and anti-angiogenic drugs are tried against metastatic disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Pheochromocytomas dump catecholamines via calcium: chromaffin cells release adrenaline by calcium-triggered exocytosis, so the tumor's surges of hormone—and the spells of pounding blood pressure they cause—run on this calcium-dependent machinery.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages fill the pheochromocytoma's vascular stroma: drawn into the richly perfused, pseudohypoxic tumor, they support its blood supply and shape an immune niche of interest in the hard-to-treat metastatic disease.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Pheochromocytoma punishes the kidneys through catecholamines: the surges of adrenaline and noradrenaline drive severe hypertension that damages the kidney's vessels, and extra-adrenal paragangliomas can also arise near the renal hilum.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Pheochromocytoma can stroke the brain: its surges of adrenaline spike blood pressure into hypertensive encephalopathy and hemorrhage, and skull-base paragangliomas can press directly on the brain.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Pheochromocytoma poisons heart-muscle cells: the flood of catecholamines overdrives cardiomyocytes into a stress (catecholamine) cardiomyopathy, sometimes the presenting crisis of the tumor.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Adrenaline from a pheochromocytoma shifts potassium: catecholamine surges drive potassium into cells, dropping blood levels and, with the BP spikes, fueling the dangerous arrhythmias of a crisis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons localize the catecholamine factory: CT and the bright T2 'light-bulb' on MRI find the mass, while Ga-68 DOTATATE PET and MIBG scintigraphy light up its receptors to map multifocal and metastatic disease before surgery.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals where the adrenaline is kept: the tumor cells are crammed with dense-core neurosecretory granules — membrane-bound packets of catecholamine — the ultrastructure that confirms a chromaffin-cell origin.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bone is where malignant paraganglioma goes: especially with SDHB mutations, these tumors metastasize to the skeleton, seeding the marrow-filled bones of the spine and pelvis as the commonest site of spread.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The pseudohypoxic tumors can thicken the blood: pheochromocytomas and paragangliomas driven by HIF stabilization — and the EPAS1-mutant Pacak-Zhuang form especially — overproduce erythropoietin, pushing the marrow to make excess red cells and cause polycythemia.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Besides bone, the liver takes the spread: malignant paragangliomas, again most often SDHB-mutant, seed hepatic metastases, a site that — like the skeleton — marks the tumor as having crossed from benign to malignant.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The catecholamine spells reach the skin: surges of adrenaline and noradrenaline drive the classic triad of pounding headache, palpitations, and drenching sweat, while clamped-down vessels leave the patient pale and clammy during an attack.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains confirm the chromaffin tumor: chromogranin A and synaptophysin mark its neuroendocrine nature on biopsy, and loss of SDHB staining flags the hereditary, more aggressive paragangliomas worth genetic testing.
- `connects-to` → **[Stroke](../stroke/README.md)** — A catecholamine storm can strike the brain: a hypertensive crisis from the tumor spikes blood pressure into hemorrhagic stroke or the posterior reversible encephalopathy syndrome, an emergency that sometimes unmasks the hidden pheochromocytoma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium tames the surgical surge: intravenous magnesium sulfate blunts catecholamine release and the arrhythmias it provokes, making it a key adjunct during the perilous handling of the tumor at operation.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy can turn a pheochromocytoma deadly: an undiagnosed tumor unleashes catecholamine crises during labor and delivery, historically with high maternal and fetal mortality, and the many hereditary forms pass to offspring — so genetic counseling matters.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — RET ties the adrenal medulla to the thyroid: in MEN2, a germline RET mutation causes pheochromocytoma alongside medullary thyroid carcinoma, so finding one tumor triggers a hunt — and prophylactic thyroidectomy — for the other.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — One molecular cluster of these tumors runs on kinase signaling: RET, NF1, TMEM127 and MAX mutations drive PI3K-AKT-mTOR activation, the growth-signaling group that contrasts with the pseudohypoxic, HIF-driven SDH and VHL cluster.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — The catecholamine flood disrupts sugar control: adrenaline and noradrenaline suppress insulin release and drive glycogen breakdown, so pheochromocytoma often causes hyperglycemia and secondary diabetes that resolves once the tumor is removed.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomere genes flag the dangerous ones: TERT and ATRX alterations mark the pheochromocytomas and paragangliomas most likely to metastasize, helping pick out aggressive tumors in a disease where malignancy is otherwise hard to predict.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — They are intensely vascular tumors: pseudohypoxic SDH and VHL mutations crank up VEGF, so endothelial cells build a dense blood supply — making these tumors hemorrhagic at surgery and their angiogenesis a therapeutic target.
- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — EPAS1 anchors the pseudohypoxia cluster: gain-of-function HIF-2α (EPAS1) mutations cause pheochromocytoma/paraganglioma — sometimes with polycythemia (Pacak-Zhuang) — by mimicking a low-oxygen state that drives the tumor.
- `connects-to` → **[FH](../../03-molecular/fh/README.md)** — Another Krebs-cycle gene joins the cluster: FH mutations, like SDH, flood the cell with an oncometabolite that stabilizes HIF, placing FH-mutant pheochromocytoma/paraganglioma in the pseudohypoxic, often aggressive subgroup.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Catecholamines can stun the heart: the adrenaline surges of pheochromocytoma cause a catecholamine cardiomyopathy (including takotsubo) that can precipitate acute heart failure, often reversible once the tumor is removed.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Some of these tumors secrete IL-6: an IL-6-producing pheochromocytoma can cause fever, weight loss and an inflammatory syndrome driven through JAK-STAT3, a paraneoplastic picture that resolves once the tumor is resected.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A pheo crisis can masquerade as septic shock: catecholamine storm produces fever, lactic acidosis and multi-organ failure that mimic sepsis, a dangerous mimicry since the usual fluids-and-pressors response can worsen the crisis.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Years of catecholamine hypertension scar the kidney: sustained or paroxysmal pressure surges from the tumor drive hypertensive nephrosclerosis, and the renal damage can persist as chronic kidney disease even after cure.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its catecholamines and surgery thicken the clotting risk: chronic adrenergic stimulation activates platelets and coagulation, and the major operation to resect the tumor adds perioperative immobility, together raising venous thromboembolism risk.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Catecholamine excess unsettles the mind: the surges that cause palpitations and panic also disturb mood, and patients commonly carry anxiety and depressive symptoms before diagnosis that can linger after the tumor is removed.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Catecholamines and HIF-pathway tumors can pressurize the lungs: adrenergic surges acutely constrict the pulmonary vasculature, and the EPAS1/HIF-2α paraganglioma syndromes are described alongside pulmonary hypertension.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Removing the tumour is high-stakes surgery: adrenalectomy or paraganglioma resection requires careful alpha-blockade to prevent intra-operative hypertensive crisis, and the abdominal wound must heal afterwards.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Years of catecholamine hypertension scar the arteries: the sustained and paroxysmal blood-pressure surges of a phaeochromocytoma accelerate endothelial injury and atherosclerotic vascular damage.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Adrenergic excess paralyses the gut: high circulating catecholamines suppress intestinal motility in phaeochromocytoma, causing severe constipation and occasionally pseudo-obstruction or ischaemic colitis.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its attacks sweat and blanch the skin: the classic phaeochromocytoma triad pairs headache and palpitations with profuse diaphoresis, and adrenergic vasoconstriction causes episodic pallor of the skin.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — A catecholamine crisis floods the lungs: a phaeochromocytoma crisis can precipitate catecholamine cardiomyopathy with flash pulmonary oedema and acute respiratory distress.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Catecholamines tremble the body and tumours seed bone: adrenergic excess causes the fine tremor of phaeochromocytoma, and metastatic SDHB-related paraganglioma spreads to the skeleton.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Catecholamine surges scar the kidney: sustained and paroxysmal hypertension drives hypertensive nephrosclerosis, and paragangliomas can arise in the renal bed near the kidney.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Malignant disease spreads to the nodes: there is no benign histology — malignancy is defined by spread, and SDHB-mutated paragangliomas in particular metastasise to lymph nodes and bone.
- `connects-to` → **[Beta-Blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — Order of blockade is life-or-death: beta-blockers must be given only after alpha-blockade in phaeochromocytoma, because unopposed alpha stimulation from beta-blockade first can precipitate a hypertensive crisis.
- `connects-to` → **[Calcium-channel Blockers](../../../03-medicine/01-modern/04-cardio/calcium-channel-blockers/README.md)** — They help control the surges: calcium-channel blockers assist in managing the paroxysmal hypertension of phaeochromocytoma, after alpha-blockade and before any beta-blocker is added.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Metastatic disease gets targeted treatment: MIBG radiotherapy, somatostatin-receptor PRRT and kinase inhibitors such as sunitinib treat unresectable phaeochromocytoma and paraganglioma.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — It belongs to the neuroendocrine family: phaeochromocytomas and paragangliomas are catecholamine-secreting neuroendocrine tumours, sharing somatostatin-receptor imaging and PRRT with other NETs.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for malignant disease: the cyclophosphamide-vincristine-dacarbazine (CVD) regimen treats metastatic phaeochromocytoma and paraganglioma, alongside MIBG and peptide-receptor radionuclide therapy.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Two routes to too many red cells: EPAS1 (HIF2A)-mutant paragangliomas can drive erythropoietin-mediated polycythaemia (Pacak-Zhuang syndrome), a secondary erythrocytosis distinct from the JAK2-driven polycythaemia vera.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy for the aggressive few: metastatic phaeochromocytoma and paraganglioma, though rare, are being trialled with PD-1 checkpoint inhibitors when other options are exhausted.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Catecholamines poison the heart muscle: sustained adrenaline and noradrenaline from a phaeochromocytoma cause catecholamine cardiomyopathy and Takotsubo-like myocardial stunning, which can present as acute heart failure before the tumour is found.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — It also destabilises the heart's wiring: catecholamine surges from a phaeochromocytoma trigger tachyarrhythmias and dangerous blood-pressure swings, which is why alpha-blockade must precede any beta-blocker to avoid unopposed vasoconstriction.
- `connects-to` → **[IDH-mutant Glioma](../idh-mutant-glioma/README.md)** — A pseudohypoxic, oncometabolite tumour: SDH-deficient paraganglioma accumulates succinate that, like the 2-hydroxyglutarate of IDH-mutant glioma, inhibits α-ketoglutarate dioxygenases and stabilises HIF—two cancers driven by a metabolite.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Catecholamine vasculopathy: the noradrenaline surges of phaeochromocytoma cause severe vasoconstriction and hypertensive crises that damage the arterial wall, with pressure spikes risking stroke and aortic dissection.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Hypertensive nephropathy: sustained and paroxysmal catecholamine hypertension transmits to the glomerulus, scarring it over time, while SDH and VHL also predispose to the kidney's own tumours.
- `connects-to` → **[MEN4 Syndrome](../men4-syndrome/README.md)** — Another endocrine-tumour syndrome: like MEN1, MEN4 (CDKN1B loss) can include phaeochromocytoma and paraganglioma among its parathyroid and pituitary tumours, joining the germline syndromes that spawn them.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Metastatic bone disease: malignant paraganglioma, especially SDHB-mutated, has a striking predilection for bone metastases, often osteolytic lesions in the cortical bone that drive functional imaging and treatment.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver as a metastatic site: alongside bone, the liver is a leading destination for malignant phaeochromocytoma and paraganglioma, the tumour seeding the hepatic lobule in metastatic SDHB-driven disease.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Crisis under stress: any severe illness including COVID-19 can precipitate a catecholamine crisis in an unrecognised phaeochromocytoma, the surge causing dangerous hypertension, arrhythmia and cardiomyopathy.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Pseudohypoxic epigenetics: in SDH-deficient PPGL, accumulated succinate inhibits histone demethylases and, with EZH2/polycomb, drives the DNA/histone hypermethylator phenotype shared with IDH- and FH-mutant tumours.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Kinase-signalling group: alongside NF1 and RET, RAS-MAPK activation defines the kinase-signalling cluster of PPGL, with HRAS/KRAS mutations in some sporadic tumours.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Angiogenic RTK target: PDGFR and VEGFR signalling drive the rich vasculature of PPGL, the basis for multikinase inhibitors such as sunitinib in metastatic disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MAPK output: the RET, NF1 and RAS lesions of the kinase-signalling PPGL cluster converge on ERK1/2, driving the proliferation of these neuroendocrine tumours.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Proliferative oncogene: MYC activation downstream of the kinase and pseudohypoxic pathways helps drive the growth of pheochromocytoma-paraganglioma.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: cyclin D1-CDK4/6 activity propels PPGL tumour cells through the G1 checkpoint, the proliferative output of their driver pathways.
- `connects-to` → **[EGLN1 (PHD2)](../../03-molecular/egln1/README.md)** — Germline EGLN1/PHD2 mutations cause a pseudohypoxic PPGL subtype (sometimes with polycythemia) by failing to hydroxylate HIF, locking in the hypoxia-response program that drives these tumors—placing the oxygen sensor itself among the susceptibility genes.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Somatic MAML3 fusions and CSDE1 mutations define a Wnt-signaling PPGL cluster distinct from the pseudohypoxia and kinase-signaling groups, associated with more aggressive behavior and metastatic potential.
- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — ATRX mutations in PPGL engage the alternative-lengthening-of-telomeres pathway and mark the aggressive, metastasis-prone tumors, often co-occurring with SDHB-related disease where they compound an already high metastatic risk.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Loss of TMEM127, a recurrent PPGL susceptibility gene, disinhibits mTORC1, placing a subset of these tumors in the kinase-signaling group alongside RET and NF1, distinct from the pseudohypoxic SDHx/VHL cluster.
- `connects-to` → **[β1-Adrenergic Receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — The epinephrine and norepinephrine secreted by PPGL act on β1-adrenergic receptors to drive the tachycardia and hypertension of catecholamine crisis, which is why β-blockade is added only after α-blockade to avoid unopposed vasoconstriction.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — SDH-deficient PPGL accumulates succinate that inhibits 2-oxoglutarate dioxygenases and stabilizes HIF, the same pseudohypoxic, epigenetic mechanism by which IDH-mutant tumors act through their oncometabolite 2-hydroxyglutarate.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — The RET-, NF1- and RAS-driven cluster of PPGL activates PI3K-AKT-mTOR through PIK3CA, the proliferative arm complementing the pseudohypoxia pathway and a node addressable by PI3K/mTOR inhibition.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Paroxysmal catecholamine surges from PPGL can cause Takotsubo-like stress cardiomyopathy and myocardial injury, releasing troponin from damaged myocytes—the biochemical signature of the cardiac complications of pheochromocytoma crisis.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Excess catecholamines suppress pancreatic insulin secretion via α2-adrenergic receptors and induce insulin resistance, producing the hyperglycemia and secondary diabetes of PPGL that typically resolve after tumor resection.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN limits the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped) that is activated in the kinase-signaling (cluster 2) PPGL driven by RET, NF1 and RAS (all mapped).
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — In SDH- and FH-deficient (cluster 1) PPGL, accumulated succinate and fumarate succinate KEAP1 to activate NRF2 (SDHB and FH mapped), an antioxidant program of the pseudohypoxic tumors.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D1 axis (mapped) releases E2F1 to drive proliferation, the engine of growth shared across the hereditary clusters of pheochromocytoma and paraganglioma.
- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — IDH mutations generate 2-hydroxyglutarate that, like the succinate of SDHx and fumarate of FH (both already mapped), stabilizes HIF and reprograms the epigenome in the pseudohypoxia cluster of pheochromocytoma-paraganglioma.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (cyclin-D1 and E2F1 already mapped) accompanies progression toward metastatic pheochromocytoma-paraganglioma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) contributes to the survival signaling of pheochromocytoma-paraganglioma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is expressed in pheochromocytoma/paraganglioma and contributes to tumor-cell survival and microenvironment interactions.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling modulates the proliferation and microenvironment of pheochromocytoma and paraganglioma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment relevant to emerging immunotherapy in pheochromocytoma/paraganglioma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of pheochromocytoma/paraganglioma, relevant to its emerging immunotherapy.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) shapes the microenvironment of the pseudohypoxic pheochromocytoma/paraganglioma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate the oxidative and metabolic stress of the SDH/VHL-driven pseudohypoxia of pheochromocytoma/paraganglioma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt signaling of the pseudohypoxic pheochromocytoma/paraganglioma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation restrains apoptosis in pheochromocytoma/paraganglioma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is a component of the immune response to pheochromocytoma/paraganglioma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of pheochromocytoma/paraganglioma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation, prominent in the SDH-deficient CpG-methylator subtype, of pheochromocytoma/paraganglioma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival of the pseudohypoxic, SDH/VHL-deficient cells of pheochromocytoma/paraganglioma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic (pseudohypoxic) adaptation of pheochromocytoma/paraganglioma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of pheochromocytoma/paraganglioma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of RET and other receptor tyrosine kinases (RET already mapped) participates in the proliferative signaling of pheochromocytoma/paraganglioma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of pheochromocytoma and paraganglioma.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal and pseudohypoxic interactions of pheochromocytoma and paraganglioma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of pheochromocytoma and paraganglioma.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Secretory trigger: adrenal chromaffin cells are innervated by cholinergic splanchnic preganglionic fibres, so acetylcholine is the physiological signal that evokes catecholamine exocytosis, the pathway whose dysregulated tumour activity underlies paroxysmal secretion.
- `connects-to` → **[NPY](../../03-molecular/npy/README.md)** — Co-secreted vasoconstrictor: neuropeptide Y is stored and released alongside catecholamines by pheochromocytoma and sympathetic paraganglia, contributing to the vasoconstriction and hypertension and serving as an additional secretory marker beyond the metanephrines.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Exocytosis and MEN2: calcium influx triggers the granule exocytosis releasing catecholamines from chromaffin cells, and in RET-driven MEN2 the tumour co-occurs with parathyroid hyperplasia and calcium dysregulation, linking secretion to syndromic mineral endocrinology.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPAS1 polycythaemia: EPAS1/HIF2-driven paragangliomas (EPAS1 already mapped) can secrete erythropoietin, causing the polycythaemia of the Pacak-Zhuang syndrome, a distinctive pseudohypoxic feature of this tumour subtype.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Metastatic immunotherapy: MHC class II antigen presentation shapes the T-cell response to metastatic pheochromocytoma/paraganglioma, for which checkpoint and other immunotherapies are being explored given the limited options for malignant disease.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell therapy: IL-2-driven T-cell expansion supports the immunotherapy approaches under investigation for metastatic paraganglioma, complementing MIBG and peptide-receptor radionuclide therapy (SSTR2 already mapped).
- `connects-to` → **[Peripheral nerve](../../05-tissue/peripheral-nerve/README.md)** — Paraganglia origin: paragangliomas arise from the paraganglia distributed along the sympathetic chain and parasympathetic nerves (head, neck, thorax, abdomen), the peripheral autonomic tissue whose chromaffin and glomus cells give rise to these tumours.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Polycythaemia: some pseudohypoxic pheochromocytomas and paragangliomas secrete erythropoietin (already mapped) or activate HIF, raising haemoglobin, and the Pacak-Zhuang syndrome links EPAS1-driven tumours (already mapped) to polycythaemia.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Adrenal and RAAS context: as an adrenal cause of secondary hypertension, pheochromocytoma sits alongside the aldosterone-driven primary aldosteronism of the adrenal cortex, and catecholamines stimulate renin and the aldosterone axis (angiotensin already in the RAAS).
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — RAAS activation: catecholamines from the tumour stimulate renin and the renin-angiotensin-aldosterone system (aldosterone already mapped), and angiotensin II compounds the vasoconstriction and hypertension (already mapped) of pheochromocytoma.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — Catecholamine-driven renin: the beta-adrenergic (already mapped) stimulation of renin release by the tumour catecholamines activates the RAAS (angiotensin II and aldosterone already mapped), part of the mechanism of the hypertension in pheochromocytoma.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the microenvironment of the metastatic SDHB-driven (already mapped) pheochromocytoma-paraganglioma dampens the anti-tumour immune response, part of the immune biology relevant to its emerging immunotherapy.
- `connects-to` → **[T-cytotoxic cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Emerging immunotherapy: the cytotoxic T cells (perforin already mapped) are the target of the checkpoint immunotherapy explored in metastatic SDHB-driven (already mapped) pheochromocytoma-paraganglioma, which the immunosuppressive stroma (IL-10 already mapped) limits.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the metastatic pheochromocytoma-paraganglioma.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of pheochromocytoma-paraganglioma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Catecholamine biosynthesis: copper is the cofactor of dopamine-β-hydroxylase, which makes the noradrenaline from the dopamine (both already mapped), the copper-dependent catecholamine biosynthesis of the chromaffin tumours.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Catecholamine hypermetabolism: leptin reflects the metabolic effects of the catecholamine (already mapped) excess — the hypermetabolism and weight loss — of pheochromocytoma-paraganglioma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the catecholamine-driven metabolic disturbance of pheochromocytoma-paraganglioma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the catecholamine-driven metabolic disturbance of pheochromocytoma-paraganglioma.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — EPO-erythrocytosis iron: the erythropoietin (already mapped)-secreting pheochromocytoma-paraganglioma (and the pseudohypoxia HIF already mapped) can drive the erythrocytosis, consuming the iron for the increased erythropoiesis.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of the malignant pheochromocytoma-paraganglioma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity of the malignant pheochromocytoma-paraganglioma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of pheochromocytoma-paraganglioma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of pheochromocytoma-paraganglioma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 effector: IL-17A is the Th17 effector cytokine complementing the Th1/type-2 (IFN-γ, IL-4, IL-5 and IL-13 already mapped) balance of the immune microenvironment of pheochromocytoma-paraganglioma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 arm) of the inflammatory dimension of the pheochromocytoma-paraganglioma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of pheochromocytoma-paraganglioma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of pheochromocytoma-paraganglioma.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the highly vascular pheochromocytoma-paraganglioma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Tumour complement: the complement C3 activation contributes to the inflammatory dimension of the pheochromocytoma-paraganglioma microenvironment.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuroendocrine–immune alarmin: TSLP released in the adrenal medullary and paraganglionic microenvironment is modulated by the catecholamine-driven (noradrenaline/adrenaline already mapped) sympathetic-immune axis of pheochromocytoma-paraganglioma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Catecholamine-co-secreted mediator: histamine is co-secreted with catecholamines by PPGL chromaffin cells and by the abundant intratumoural mast cells, contributing to the flushing and hypertensive crises that mimic carcinoid syndrome.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Vasomotor crisis amplifier: bradykinin, released from intratumoural mast cells and the kinin–kallikrein cascade activated during pheochromocytoma catecholamine surges, amplifies the vasodilation and hypotension of the post-crisis nadir.

[^lenders-2014-pheo-guideline]: Lenders JW, Duh QY, Eisenhofer G, et al. Pheochromocytoma and paraganglioma: an endocrine society clinical practice guideline. *J Clin Endocrinol Metab.* 2014;99(6):1915-1942. [doi:10.1210/jc.2014-1498](https://doi.org/10.1210/jc.2014-1498) · [PubMed 24893135](https://pubmed.ncbi.nlm.nih.gov/24893135/)
[^baudin-2021-firstmappp-sunitinib]: Baudin E, Goichot B, Berruti A, et al. First International Randomized Study in Malignant Progressive Pheochromocytoma and Paragangliomas (FIRSTMAPPP). *Ann Oncol.* 2021;32(10):1245-1254. [doi:10.1016/j.annonc.2021.07.009](https://doi.org/10.1016/j.annonc.2021.07.009) · [PubMed 34246769](https://pubmed.ncbi.nlm.nih.gov/34246769/)
