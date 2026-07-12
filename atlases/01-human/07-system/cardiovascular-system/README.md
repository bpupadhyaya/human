---
schema: human-scale-entry/v1
id: cardiovascular-system
name: Cardiovascular system
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-03
summary: "Heart, vasculature, and blood, organized into two circuits in series — pulmonary and systemic. The body's transport network: oxygen, CO₂, nutrients, waste, hormones, immune cells, heat."
aliases: ["circulatory system", "cardiovascular system"]
sources:
  - id: openstax-anatomy-19-1
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 19.1: Heart Anatomy."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy"
    accessed: "2026-06-03"
  - id: openstax-anatomy-20-1
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 20.1: Structure and Function of Blood Vessels."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/20-1-structure-and-function-of-blood-vessels"
    accessed: "2026-06-03"
  - id: openstax-anatomy-20-2
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 20.2: Blood Flow, Blood Pressure, and Resistance."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/20-2-blood-flow-blood-pressure-and-resistance"
    accessed: "2026-06-03"
  - id: nhlbi-heart-overview
    type: regulatory
    cite: "U.S. National Heart, Lung, and Blood Institute (NHLBI). How the Heart Works."
    url: "https://www.nhlbi.nih.gov/health/heart/anatomy"
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/06-organ/heart
    relation: contains
    note: "The pump driving the entire cardiovascular system."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The cardiovascular system is one of the body's principal organ systems, regulated by and embedded in the integrated whole organism."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: damaged-by
    note: "SARS-CoV-2 causes systemic cardiovascular sequelae: endothelial dysfunction, microvascular thrombosis, myocarditis, arrhythmia, and post-acute cardiovascular complications."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The cardiovascular and respiratory systems are tightly coupled via the pulmonary circuit: the right heart delivers deoxygenated blood to the alveolar capillaries, and the left heart receives oxygenated blood — making them functionally inseparable in gas exchange."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "The autonomic nervous system regulates heart rate (via SA node), contractility (β1-AR), and vascular tone; baroreceptor reflex provides moment-to-moment blood pressure feedback."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain receives ~20% of cardiac output despite being ~2% of body weight; cerebral autoregulation maintains constant CBF over MAP 60–150 mmHg; ischemic stroke results from thromboembolic occlusion or sustained hypoperfusion."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "RAAS couples renal perfusion pressure to angiotensin II and aldosterone, governing Na⁺/H₂O retention and systemic BP; cardiorenal syndrome links heart failure to acute kidney injury."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Portal circulation delivers absorbed nutrients from gut to liver; hepatic lipoprotein synthesis and coagulation factor production directly shape cardiovascular risk and thrombosis."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Portal vein drains intestinal blood to liver before reaching systemic circulation; mesenteric blood flow (~30% of cardiac output postprandially) is regulated by autonomic and local vasoactive signals."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Renal perfusion (20–25% of cardiac output) is directly coupled to cardiac output; acute heart failure reduces GFR; the RAAS axis from the kidney feeds back to regulate systemic vascular resistance and cardiac preload."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Glomerular filtration is driven entirely by systemic hydrostatic pressure from the renal artery; cardiac output and mean arterial pressure are the primary determinants of GFR."
  - target: 01-human/05-tissue/glomerulus
    relation: modulates
    note: "Systemic blood pressure modulates glomerular filtration pressure; hypertension causes hyperfiltration and eventual glomerulosclerosis; heart failure reduces GFR via low perfusion."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Hepatic lobules receive dual blood supply — portal vein (~75%, nutrient-rich) and hepatic artery (~25%, oxygenated); portal hypertension in liver disease reflects cardiovascular-hepatic coupling."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: treated-by
    note: "ARBs reduce cardiac afterload and preload via AT1 blockade; indicated for hypertension, HFrEF (if ACE-I intolerant), and post-MI LV dysfunction; reduce hospitalizations and improve survival in heart failure."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: modulated-by
    note: "AT1 receptor blockade by ARBs redirects angiotensin II to the AT2 receptor, producing vasodilation and anti-fibrotic effects; RAAS suppression reduces cardiac remodeling after MI and in heart failure."
  - target: 03-medicine/01-modern/04-cardio/calcium-channel-blockers
    relation: treated-by
    note: "CCBs reduce peripheral vascular resistance (dihydropyridines) or slow heart rate and AV conduction (non-dihydropyridines); first-line for hypertension and angina; amlodipine demonstrated CV event reduction in ALLHAT and CAMELOT trials."
  - target: 03-medicine/01-modern/04-cardio/calcium-channel-blockers
    relation: modulated-by
    note: "L-type Cav1.2 channel blockade by CCBs reduces Ca²⁺ entry into vascular smooth muscle (→ vasodilation) and cardiomyocytes (→ negative chronotropy/inotropy for non-DHPs); use-dependent block during tachycardia or increased firing."
  - target: 01-human/03-molecular/cortisol
    relation: modulated-by
    note: "Cortisol enhances vascular smooth muscle responsiveness to catecholamines and angiotensin II, maintaining vascular tone; chronic glucocorticoid excess (Cushing's) causes hypertension via Na⁺ retention and increased SVR."
  - target: 01-human/03-molecular/insulin
    relation: modulated-by
    note: "Insulin promotes endothelial nitric oxide production (via Akt → eNOS), vasodilation, and glucose uptake in vascular smooth muscle; chronic hyperinsulinemia and insulin resistance drive endothelial dysfunction and atherosclerosis."
  - target: 01-human/04-cellular/erythrocyte
    relation: contains
    evidence: openstax-anatomy-19-1
    note: "Erythrocytes circulate within the cardiovascular system delivering O₂ to tissues; ~25 trillion RBCs are in continuous transit through the cardiac and vascular loop."
  - target: 01-human/05-tissue/bone-marrow
    relation: contains
    evidence: openstax-anatomy-19-1
    note: "Bone marrow produces erythrocytes, platelets, and leukocytes that populate the cardiovascular system; the sinusoidal vasculature of marrow is part of the circulation."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: modulated-by
    evidence: openstax-anatomy-20-1
    note: "EPA/DHA lower triglycerides, reduce platelet aggregation, and decrease arterial inflammation, collectively improving cardiovascular risk profile."
  - target: 01-human/03-molecular/hemoglobin
    relation: modulated-by
    note: "Modulated by Hemoglobin."
  - target: 01-human/03-molecular/fibrinogen
    relation: modulated-by
    note: "Modulated by Fibrinogen."
  - target: 01-human/03-molecular/vasopressin
    relation: modulated-by
    note: "Modulated by Vasopressin."
  - target: 01-human/03-molecular/epinephrine
    relation: modulated-by
    note: "Modulated by Epinephrine."
  - target: 01-human/03-molecular/ampk
    relation: modulated-by
    note: "Modulated by AMPK."
  - target: 01-human/03-molecular/nitric-oxide
    relation: modulated-by
    note: "Modulated by Nitric Oxide."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: modulated-by
    note: "Modulated by Angiotensin II."
  - target: 01-human/03-molecular/albumin
    relation: modulated-by
    note: "Modulated by Albumin."
  - target: 01-human/03-molecular/erythropoietin
    relation: modulated-by
    note: "Modulated by Erythropoietin."
  - target: 01-human/03-molecular/norepinephrine
    relation: modulated-by
    note: "Modulated by Norepinephrine."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: modulated-by
    note: "Modulated by Thyroid Hormones (T3/T4)."
  - target: 01-human/03-molecular/prostaglandins
    relation: modulated-by
    note: "Modulated by Prostaglandins (Eicosanoids)."
  - target: 01-human/02-atomic/iodine
    relation: modulated-by
    note: "Modulated by Iodine."
  - target: 01-human/07-system/reproductive-system
    relation: modulated-by
    note: "Modulated by Reproductive System."
  - target: 01-human/07-system/lymphatic-system
    relation: modulated-by
    note: "Modulated by Lymphatic System."
  - target: 01-human/07-system/musculoskeletal-system
    relation: modulated-by
    note: "Modulated by Musculoskeletal System."
  - target: 01-human/07-system/endocrine-system
    relation: modulated-by
    note: "Modulated by Endocrine System."
  - target: 01-human/07-system/integumentary-system
    relation: modulated-by
    note: "Modulated by Integumentary System."
  - target: 01-human/05-tissue/cortical-bone
    relation: modulated-by
    note: "Modulated by Cortical Bone."
  - target: 01-human/05-tissue/arterial-wall
    relation: composed-of
    note: "Composed Of by Arterial Wall."
  - target: 01-human/04-cellular/endothelial-cell
    relation: composed-of
    note: "Composed Of by Endothelial Cell."
  - target: 01-human/04-cellular/platelet
    relation: modulated-by
    note: "Modulated by Platelet."
  - target: 01-human/04-cellular/mast-cell
    relation: modulated-by
    note: "Modulated by Mast Cell."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: composed-of
    note: "Composed Of by Smooth Muscle Cell."
  - target: 01-human/06-organ/adrenal-gland
    relation: modulated-by
    note: "Modulated by Adrenal Gland."
  - target: 01-human/06-organ/thyroid
    relation: modulated-by
    note: "Modulated by Thyroid Gland."
  - target: 02-pathogen/04-parasites/trypanosoma-cruzi
    relation: damaged-by
    note: "Damaged by Trypanosoma cruzi."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: damaged-by
    note: "Damaged by Streptococcus pyogenes."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: damaged-by
    note: "Damaged by Neisseria meningitidis."
  - target: 03-medicine/03-food/resveratrol
    relation: modulated-by
    note: "Modulated by Resveratrol."
  - target: 03-medicine/03-food/dietary-fiber
    relation: modulated-by
    note: "Modulated by Dietary Fiber and Butyrate."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: modulated-by
    note: "Modulated by Dietary Magnesium."
  - target: 03-medicine/02-traditional/ginkgo-biloba
    relation: modulated-by
    note: "Modulated by Ginkgo biloba (EGb 761)."
  - target: 03-medicine/02-traditional/licorice-root
    relation: modulated-by
    note: "Modulated by Licorice Root (Glycyrrhiza glabra / G. uralensis)."
  - target: 03-medicine/02-traditional/panax-ginseng
    relation: modulated-by
    note: "Modulated by Panax ginseng (Korean Red Ginseng)."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Bradykinin → B2R on endothelium → eNOS → NO and PGI2 → vasodilation; ACE inhibitors raise bradykinin → contribute to vasodilatory cardioprotective effects; angioedema (B2R-mediated) and dry cough are bradykinin-dependent adverse effects of ACE inhibitor therapy."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "SCD causes chronic haemolysis → NO scavenging → pulmonary arterial hypertension (PAH; TRV >2.5 m/s on echo predicts mortality); cardiomegaly + high-output failure from chronic anaemia; SCD-PAH treated with sildenafil + transfusion + hydroxyurea."
  - target: 01-human/03-molecular/adenosine
    relation: modulated-by
    note: "A1R on SA/AV nodes → Gi → ↑IKAch → bradycardia; IV adenosine (6–12 mg, t½ ~10 s) terminates paroxysmal SVT; A2AR on coronary arteries → vasodilation; regadenoson (A2AR agonist) enables pharmacological cardiac stress testing; methylxanthines block adenosine-mediated AV block."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Romosozumab ARCH trial: MACE increase vs. alendronate (2.5% vs. 1.9%) → FDA Black Box Warning (avoid within 12 months of MI/stroke); sclerostin in vascular smooth muscle may protect against calcification; elevated sclerostin predicts CV events in dialysis patients."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "SELECT trial (semaglutide 2.4 mg, obesity without T2DM): 20% MACE reduction vs placebo; SUSTAIN-6 and LEADER established GLP-1R agonists as antidiabetic drugs with proven CV benefit; GLP-1R on cardiomyocytes → anti-inflammatory and vasodilatory cardioprotective effects."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Cx43 gap junctions at intercalated discs create the cardiac electrical syncytium; lateralization and downregulation in heart failure → slow conduction and re-entry → VT risk; ischemia acidosis closes channels (protective); reperfusion reopens → Ca²⁺ injury propagation."
  - target: 01-human/03-molecular/phospholamban
    relation: connects-to
    note: "PLN is the molecular relay of sympathoadrenergic cardiac regulation: β1-AR → PKA → PLN-pSer16 → SERCA2a disinhibition → faster Ca²⁺ reuptake → lusitropy and inotropy; PLN hyperinhibition in HFrEF (reduced pSer16) is a core Ca²⁺ cycling defect; PLN Arg9Cys → familial DCM."
  - target: 01-human/03-molecular/hcn4
    relation: connects-to
    note: "HCN4 (funny channel) is the dominant SA node pacemaker current; cAMP directly gates HCN4 → transduces sympathetic (+10 mV shift) and vagal (-10 mV shift) chronotropic control; ivabradine (HCN4 blocker) reduces HR without negative inotropy; approved in HFrEF with HR >70 bpm."
  - target: 01-human/03-molecular/ryr2
    relation: connects-to
    note: "RyR2 CICR amplifies the L-type Ca²⁺ trigger into cardiac contraction (~75% of Ca²⁺ transient is SR-derived); PKA and CaMKII tune RyR2 gain for sympathetic inotropy; CaMKII hyperactivation in HF → diastolic RyR2 leak → arrhythmia; RYR2 GOF mutations cause CPVT."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2/CCR2 drives monocyte infiltration into atherosclerotic plaques and adventitial macrophage accumulation; elevated serum CCL2 predicts MACE in EPIC/MRFIT cohorts; CCR2 blockade reduces plaque and improves cardiac function post-MI in murine models."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Troponin complex is the molecular effector of cardiac contraction: TnC Ca²⁺ binding → TnI release → tropomyosin repositioning → actin-myosin cross-bridge cycling; PKA-mediated TnI Ser23/24 phosphorylation → ↓Ca²⁺ sensitivity → faster relaxation under β-adrenergic stimulation."
  - target: 01-human/03-molecular/ncx1
    relation: connects-to
    note: "NCX1 is the second-largest Ca²⁺ removal pathway (~28% per beat); electrogenically exchanges 3 Na⁺:1 Ca²⁺; reverse mode → Ca²⁺ entry during action potential; NCX1 upregulation in HF impairs systolic function; NCX1 is a proposed therapeutic target in heart failure."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Inflammation drives its diseases: immune cells populate atherosclerotic plaques, autoimmune and infectious myocarditis injure the heart, and anti-inflammatory therapy (canakinumab, colchicine) reduces cardiovascular events."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: connects-to
    note: "The cornerstone of prevention: statins lower LDL cholesterol and stabilise plaque, cutting heart attacks and strokes, and are foundational to both primary and secondary cardiovascular prevention."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "A leading cause of endocarditis: Staphylococcus aureus is the commonest organism in infective endocarditis, seeding and destroying heart valves from the bloodstream, especially in injection drug use and prosthetic valves."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "It sets the rhythm: the SA node, AV node and His-Purkinje system generate and route the electrical impulse that coordinates the heartbeat, and their failure produces the arrhythmias, blocks and sudden death the cardiovascular system must avoid."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "A cornerstone of cardiovascular therapy: ACE inhibitors blunt the renin-angiotensin system to lower blood pressure, unload the failing heart and protect after myocardial infarction, among the most-used cardiovascular drugs."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Its central disease: atherosclerosis — lipid-laden, inflamed plaque in artery walls — underlies coronary disease, stroke and peripheral arterial disease, the leading cause of death and the dominant pathology of the cardiovascular system."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "The contractile engine: the myocardium is the heart muscle that pumps blood through the cardiovascular system, and its failure—through infarction, cardiomyopathy or hypertrophy—drives most cardiac disease."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "The valves and inner lining: the endocardium forms the heart valves that keep blood moving in one direction and lines the chambers, the site of valvular disease, endocarditis and mural thrombus."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The common final pathway: heart failure is where cardiovascular disease converges—the heart can no longer meet the body's circulatory demand, the shared endpoint of ischaemia, hypertension and valve disease."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "The dominant modifiable risk: chronic hypertension is the single biggest driver of cardiovascular disease, accelerating atherosclerosis, hypertrophying the heart and damaging vessels throughout the circulation."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "The brain end of vascular disease: stroke is cardiovascular disease striking the brain—atherosclerosis, atrial fibrillation and hypertension throwing clots or rupturing vessels that supply neural tissue."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The venous side of circulation: deep-vein thrombosis and pulmonary embolism are the cardiovascular system's venous failure, clots forming in stagnant veins and lodging in the lungs."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "The right-heart circulation: pulmonary arterial hypertension is the cardiovascular system's pulmonary-vascular disease, raising pressure in the lungs and failing the right ventricle—distinct from systemic hypertension and left heart disease."
  - target: 02-pathogen/01-viruses/coxsackievirus-b
    relation: connects-to
    note: "Viral myocarditis: enteroviruses like Coxsackie B directly infect the heart muscle, a leading cause of acute myocarditis and dilated cardiomyopathy in young, previously healthy people."
  - target: 01-human/07-system/marfan-syndrome
    relation: connects-to
    note: "Heritable aortopathy: Marfan and related connective-tissue disorders weaken the aortic wall, causing root dilatation, aneurysm and dissection—a genetic cardiovascular disease demanding lifelong aortic surveillance."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vascular tone: endothelin-1, the body's most potent vasoconstrictor, sets vascular resistance against the nitric oxide that opposes it, and its excess drives hypertension and vascular remodelling."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Vessel growth: VEGF directs the angiogenesis that builds and repairs the vasculature, governing collateral formation after ischaemia and the neovascularisation of atherosclerotic plaque."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Vascular inflammation: IL-6 is a central mediator of the inflammation that drives atherosclerosis, and trials targeting the IL-6/CRP axis confirm inflammation as a modifiable cardiovascular risk."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "Cardiac endocrine hormone: stretched ventricles release BNP to promote natriuresis and vasodilation, opposing the renin-angiotensin system and serving as the key biomarker of heart failure."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "RAAS and remodelling: aldosterone drives sodium retention and direct cardiac and vascular fibrosis, which is why mineralocorticoid-receptor antagonists improve outcomes in heart failure and hypertension."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "Cholesterol and risk: PCSK9 sets circulating LDL by controlling hepatic LDL-receptor turnover, and PCSK9 inhibitors sharply lower LDL and cardiovascular events in the vasculature."
  - target: 01-human/03-molecular/serca2a
    relation: connects-to
    note: "Cardiac relaxation: SERCA2a pumps calcium back into the sarcoplasmic reticulum after each beat, setting the rate of cardiomyocyte relaxation and refilling the store for the next contraction, central to both systole and diastole."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: connects-to
    note: "Adrenergic control: the β1-adrenergic receptor transduces sympathetic noradrenaline into faster, stronger heartbeats, the target of the beta-blockers that are foundational drugs across heart failure, arrhythmia and ischaemic heart disease."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Atherogenic substrate: cholesterol carried in LDL accumulates in the arterial wall to seed atherosclerotic plaque, the lipid foundation of the coronary and cerebrovascular disease that dominates cardiovascular mortality."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Excitation-contraction coupling: calcium influx triggers calcium-induced calcium release to drive each heartbeat, and calcium controls vascular smooth-muscle tone — the ion central to both cardiac contraction and the regulation of blood-vessel diameter and pressure."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Endothelial haemostasis: von Willebrand factor stored in and released from the vascular endothelium captures platelets at sites of injury, the first step of haemostasis and, when the endothelium is diseased, of arterial thrombosis."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "Blood-pressure control: renin from the kidney initiates the renin-angiotensin-aldosterone cascade that sets vascular tone and blood volume, the master endocrine controller of cardiovascular pressure and the target of ACE inhibitors and ARBs."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Cardiovascular morphogenesis: NOTCH signalling governs cardiac chamber, valve and coronary-vessel development and sets arterial-venous endothelial identity, a master developmental pathway of the cardiovascular system."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Wall homeostasis and fibrosis: TGF-β controls vascular smooth-muscle and extracellular-matrix homeostasis of the arterial wall (its dysregulation causing the aortic disease of Marfan, already mapped) and drives the cardiac fibrosis of remodelling."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Hypertrophic growth: the calcineurin-NFAT pathway transduces calcium signals into the hypertrophic growth programme of cardiomyocytes, central to the heart's maladaptive response to pressure and volume overload."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Vascular inflammation: IL-1β drives the inflammatory cascade of atherosclerosis, validated clinically by the CANTOS trial in which IL-1β blockade reduced recurrent cardiovascular events independent of lipid lowering."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Growth signalling: ERK1/2 MAPK transduces growth-factor and mechanical signals into cardiomyocyte hypertrophy and vascular smooth-muscle proliferation, a core driver of cardiac remodelling and arterial restenosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival and growth: PI3K-AKT signalling mediates the IGF/insulin survival programme of cardiomyocytes and endothelial nitric-oxide production, balancing physiological adaptation against pathological hypertrophy."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signalling (downstream of the AKT axis mapped) governs cardiomyocyte growth and the hypertrophic remodelling of the heart in pressure and volume overload."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α coordinates the myocardial and vascular response to ischemia, driving angiogenesis and metabolic adaptation in the cardiovascular system."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB-driven endothelial and vascular inflammation is central to atherogenesis and the inflammatory component of cardiovascular disease."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 drives cardiac and vascular fibrosis and is an established biomarker of heart failure and adverse cardiovascular remodelling."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling mediates cardiomyocyte hypertrophy and the vascular inflammation shared across cardiovascular diseases."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the cardiac and vascular fibrosis central to adverse remodelling in cardiovascular disease."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate cardiomyocyte and endothelial oxidative-stress defense, autophagy, and metabolic homeostasis across the cardiovascular system."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the vascular and myocardial inflammatory responses shared across cardiovascular disorders."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING links cellular and mitochondrial stress to the sterile inflammation of cardiovascular disease."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the cardiac hypertrophy and vascular remodeling signaling of the cardiovascular system."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the physiological cardiac growth and endothelial survival of the cardiovascular system."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins participate in the inflammatory signaling of atherosclerosis and myocardial injury in the cardiovascular system."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the cardiomyocyte and vascular-cell protein-quality control and metabolic resilience of the cardiovascular system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the vascular endothelial and smooth-muscle mechanotransduction and remodeling of the cardiovascular system."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance participates in the immune-mediated myocardial and vascular injury relevant to the cardiovascular system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the cardiomyocyte and vascular gene programs of the cardiovascular system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment participates in the vascular inflammation and atherogenesis of the cardiovascular system."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the endothelial homeostasis, angiogenesis, and cardiac-progenitor mobilization of the cardiovascular system."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the cardiac and vascular immune responses of the cardiovascular system."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the vascular inflammation and cardiac remodeling of the cardiovascular system."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the vascular inflammation and injury responses of the cardiovascular system."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Repolarisation: potassium channels set cardiac repolarisation and resting membrane potential, so disturbances of potassium cause the QT changes and life-threatening arrhythmias that make electrolyte balance central to cardiovascular safety."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Depolarisation and pressure: sodium channels drive the cardiac action-potential upstroke and conduction, while renal sodium handling sets blood volume and long-term blood pressure, tying the ion to both electrophysiology and haemodynamics."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Cardiac energetics: the heart consumes and regenerates an enormous mass of ATP each day to power contraction, and the energy starvation of failing myocardium reflects a breakdown in this ATP supply-demand balance."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Atherosclerotic inflammation: macrophages ingest oxidised lipid to become the foam cells of the atherosclerotic plaque, and their inflammation and death drive the plaque growth and rupture behind most cardiovascular events."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pulmonary circulation: the right heart pumps blood through the lungs for gas exchange, and this pulmonary circulation is an integral loop of the cardiovascular system whose failure produces pulmonary hypertension and congestion."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Oxygen transport and deficiency: iron in haemoglobin (already mapped) carries the oxygen the circulation delivers, and iron deficiency independently worsens heart failure, linking the metal to cardiovascular function beyond anaemia."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Rhythm and vascular tone: magnesium stabilises cardiac membranes and rhythm and relaxes vascular smooth muscle (already mapped), and its deficiency predisposes to arrhythmias and hypertension, a mineral integral to cardiovascular function."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and urate risk: xanthine-oxidase-derived reactive oxygen species drive the endothelial (already mapped) dysfunction of cardiovascular disease, and the uric acid it produces is itself linked to hypertension and cardiovascular risk."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory atheroprotection: the anti-inflammatory IL-10 restrains the vascular inflammation (IL-6 and IL-1 already mapped) that drives atherosclerosis (already mapped), part of the immune balance shaping cardiovascular health."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The cardiorenal partnership: the kidney regulates blood volume and pressure through the renin-angiotensin-aldosterone system (already mapped), and the heart and kidney are locked in a bidirectional partnership central to the cardiovascular system."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Cardiac and vascular excitability: potassium sets the resting membrane potential of the cardiac and vascular smooth-muscle (already mapped) cells, and dyskalaemia causes the arrhythmias that threaten the cardiovascular system."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "The central vascular disorder: hypertension is the commonest disorder of the cardiovascular system, the raised pressure (RAAS and endothelin already mapped) driving the atherosclerosis, heart failure and stroke that dominate its disease burden."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Cardioprotective adipokine: adiponectin is an anti-atherogenic, cardioprotective adipokine of the cardiovascular system, and its fall in obesity and the metabolic syndrome (insulin and cholesterol already mapped) raises cardiovascular risk."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine and blood pressure: leptin links the obesity to the sympathetic activation (noradrenaline already mapped) and the hypertension of the cardiovascular system, part of the adipose-cardiovascular crosstalk."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Oxygen delivery: the fundamental purpose of the cardiovascular system is to deliver oxygen (carried on haemoglobin already mapped) to the tissues, the circulation matched to the metabolic demand."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Contractile cells: the cardiomyocytes are the contractile cells of the heart (the excitation-contraction — troponin and SERCA2a already mapped) that drive the circulation of the cardiovascular system."
  - target: 01-human/04-cellular/sa-node-cell
    relation: connects-to
    note: "Pacemaker cells: the sinoatrial-node cells (HCN4 already mapped, the funny current) set the heart rate and initiate the rhythm of the cardiovascular system."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Vascular-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose to the vascular inflammation and the cardiovascular risk of the cardiovascular system."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 vascular inflammation: the IFN-γ of the T cells is the type-II interferon arm of the Th1-driven atherosclerotic and myocardial inflammation of the cardiovascular system."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 vascular immunity: IL-4 and the type-2/M2 (macrophage) arm modulate the vascular inflammation and the plaque remodelling of the cardiovascular system."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 vascular immunity: IL-13, with IL-4 (already mapped), completes the type-2 immune arm of the vascular and cardiac remodelling of the cardiovascular system."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 vascular inflammation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the atherosclerotic and myocardial inflammation of the cardiovascular system."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophilia of the eosinophilic myocarditis and endocarditis of the cardiovascular system."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing, drives the innate inflammation of the myocarditis and the atherosclerosis of the cardiovascular system."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of the myocarditis and the atherosclerosis of the cardiovascular system."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the eosinophilic myocarditis and the hypersensitivity vasculitides of the cardiovascular system."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the myocarditis and the atherosclerotic inflammation of the cardiovascular system."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) generate the membrane-attack complex central to the atherosclerotic and ischaemia-reperfusion injury of the cardiovascular system."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid (macrophage already mapped) recruitment of the atherosclerotic and myocarditic inflammation of the cardiovascular system."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic infiltrate: the cytotoxic T cells (perforin already mapped) mediate the myocyte injury of the viral myocarditis and contribute to the atherosclerotic plaque inflammation of the cardiovascular system."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-vascular axis: TSLP, from injured endothelium (already mapped) and vascular smooth muscle, primes mast cells (already mapped) and dendritic cells (already mapped) and amplifies the Th2/eosinophil (already mapped) vascular inflammation of the cardiovascular system."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor regulates the contact-pathway kinin cascade (bradykinin already mapped) and the classical-complement activation (C3 and C5 already mapped) contributing to the angioedema and ischaemia-reperfusion of the cardiovascular system."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell vascular mediator: histamine, from cardiac and vascular mast cells (already mapped), amplifies the vascular permeability and the coronary vasospasm contributing to Kounis syndrome and the hypersensitivity myocarditis of the cardiovascular system."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Cardiac ECM remodelling: periostin, expressed by cardiac fibroblasts (already mapped) under mechanical and ischaemic stress, promotes collagen deposition and the adverse ventricular remodelling that drives hypertrophy and heart failure progression of the cardiovascular system."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian cardioprotection: melatonin, via MT1/MT2 receptors on cardiomyocytes (already mapped) and endothelial cells (already mapped), scavenges ROS, attenuates ischaemia-reperfusion injury and synchronises the circadian cardiac rhythms of the cardiovascular system."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine cardiac axis: prolactin, acting via PRLR on cardiomyocytes (already mapped) and macrophages (already mapped), modulates the cardiac inflammatory cytokine milieu and is linked to peripartum cardiomyopathy and heart failure of the cardiovascular system."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "CV testosterone: testosterone, via androgen receptors on cardiomyocytes (already mapped), attenuates NF-κB (already mapped) and IL-6 (already mapped) cardiomyopathic signalling; testosterone deficiency amplifies CVD risk and heart-failure (already mapped) morbidity."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "CV serotonin: serotonin, via 5-HT receptors on cardiomyocytes (already mapped) and endothelial cells (already mapped), modulates cardiac rhythm and vascular tone; serotonin excess amplifies the NF-κB (already mapped) and IL-6 (already mapped) cardiovascular inflammation."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "CV oxytocin: oxytocin, via OXTR on cardiomyocytes (already mapped) and endothelial cells (already mapped), attenuates NF-κB (already mapped) and IL-6 (already mapped) cardiac inflammation; oxytocin promotes nitric-oxide (already mapped) vasodilation and cardioprotection."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "CV selenium: selenium, via GPx and thioredoxin reductase, scavenges ROS in cardiomyocytes (already mapped) and endothelial cells (already mapped); selenium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cardiac inflammation and heart-failure severity."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "CV copper: copper, via ceruloplasmin and SOD, protects cardiomyocytes (already mapped) from oxidative injury; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cardiac inflammation and the cardiac fibrosis of heart failure (already mapped)."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "CV phosphorus: phosphorus drives ATP (already mapped) synthesis and SERCA2a (already mapped) calcium-pump function in cardiomyocytes (already mapped); hyperphosphataemia amplifies NF-κB (already mapped) vascular calcification and endothelial cell (already mapped) dysfunction."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "CV zinc: zinc, via SOD and cardiomyocyte (already mapped) metalloenzymes, quenches oxidative stress; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cardiac inflammation and endothelial-cell (already mapped) dysfunction in cardiovascular disease."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "CV nitrogen: nitric oxide (NO, nitrogen-derived) in endothelial cells (already mapped) and macrophages (already mapped) regulates vasodilation; NO deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and platelet (already mapped) aggregation cascade."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "CV chloride: chloride channels on cardiomyocytes (already mapped) and smooth muscle cells (already mapped) regulate membrane excitability; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cardiac fibrosis cascade."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "CV sulfur: sulfur-containing glutathione in cardiomyocytes (already mapped) and endothelial cells (already mapped) scavenges ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) and macrophage (already mapped) cascade."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "carbon-based fatty acids in smooth-muscle cell (already mapped) and macrophage (already mapped) fuel vascular ATP; disrupted carbon metabolism amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in cardiovascular disease."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "hydrogen ion dysregulation in smooth-muscle cell (already mapped) and macrophage (already mapped) amplifies vascular tone; proton excess disrupts NF-κB (already mapped) and mTOR (already mapped) and IL-6 (already mapped) signalling cascade in cardiovascular disease."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α from macrophage (already mapped) amplifies endothelial inflammation; TNF-α excess drives NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade worsening smooth-muscle cell (already mapped) dysfunction in cardiovascular disease."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "cardiovascular pd-1: PD-1 on t-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses immune-driven atherosclerosis; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in cardiovascular disease."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "cardiovascular wnt-beta-catenin: Wnt/β-catenin in smooth-muscle cells (already mapped) and macrophages (already mapped) regulates remodelling; wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in cardiovascular disease."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "cardiovascular rankl: RANKL from endothelial cells (already mapped) and macrophages (already mapped) modulates vascular calcification; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in cardiovascular disease."
taxonomy:
  uberon: "UBERON:0004535"
  fma: "FMA:7161"
---

# Cardiovascular system

## Overview

The cardiovascular system is the body's **transport network** — heart, blood vessels, and blood, integrated into two circuits in series that move oxygen, carbon dioxide, nutrients, metabolic waste, hormones, immune cells, and heat to and from every tissue [^openstax-anatomy-19-1]. It is the only system most cells of the body interact with directly: every cell in every other tissue lives within ~100 µm of a capillary, because beyond that distance, diffusion alone cannot keep up.

Functionally, the system has three components — a **pump** (the [heart](../../06-organ/heart/README.md)), a **distribution network** (arteries → arterioles → capillaries → venules → veins), and a **carrier fluid** (blood) — each of which has its own pathologies and its own therapeutic targets, but which function only as a coordinated whole.

## Structure

### The two circuits

The cardiovascular system is **two circuits in series**, sharing the heart as a common pump:

```
                    ┌──────────────┐
                    │  Pulmonary   │   low pressure
                    │  circulation │   (RV peak ~25 mmHg)
                    │   (lungs)    │
                    └──────────────┘
                       ↑        ↓
                  ┌─────────────────┐
                  │  Heart (4 chambers) │
                  │  R-side  ←  L-side  │
                  └─────────────────┘
                       ↑        ↓
                ┌────────────────────┐
                │     Systemic       │   high pressure
                │     circulation    │   (LV peak ~120 mmHg)
                │   (body — brain,   │
                │    muscle, gut,    │
                │    kidneys, …)     │
                └────────────────────┘
```

- **Pulmonary circuit.** Right ventricle → pulmonary trunk → pulmonary arteries → pulmonary capillaries (gas exchange) → pulmonary veins → left atrium. Low pressure, high compliance — the lung capillary bed is enormous and permeable to low driving pressures.
- **Systemic circuit.** Left ventricle → aorta → arteries → arterioles → capillaries (exchange) → venules → veins → vena cavae → right atrium. High pressure, multiple parallel beds (cerebral, coronary, renal, splanchnic, muscular, cutaneous), each with autoregulation matching local flow to local demand.

### Vessels

| Vessel class | Wall composition | Role |
|:---|:---|:---|
| **Elastic arteries** (aorta, large arteries) | Thick tunica media rich in elastin | Damp ventricular pulsations into smoother flow ("Windkessel" effect) |
| **Muscular arteries** | Smooth muscle dominant | Distribute blood; modest tone control |
| **Arterioles** | Smooth muscle dominant; small diameter | Primary site of **systemic vascular resistance** — adjustable, sympathetically innervated |
| **Capillaries** | Single endothelial cell layer + basement membrane | Site of all exchange (gas, nutrients, waste, water, immune cells) |
| **Venules / veins** | Thin walls, low pressure, valves in extremities | Capacitance reservoir — hold ~70 % of blood volume; venous return tunable via tone and pump action |

Total length of human vasculature is on the order of **~100,000 km** (rough estimate); total capillary surface area, ~5,000–7,000 m².

### Blood

About 5 L of blood, distributed roughly as:

| Compartment | Share of total blood volume |
|:---|:---:|
| Systemic veins | ~64 % |
| Pulmonary circulation | ~9 % |
| Heart chambers | ~7 % |
| Systemic arteries | ~13 % |
| Capillaries | ~7 % |

Blood is a tissue in its own right (plasma + erythrocytes + leukocytes + platelets) and will receive its own entry — at the tissue scale.

### Lymphatic system

The lymphatics return to circulation the ~3 L/day of fluid that filters out of capillaries beyond what is reabsorbed at the venous end. Functionally it is the **return-leg complement** to the cardiovascular system; anatomically it merges with venous circulation at the thoracic duct → left subclavian vein. (Lymphatic system entry pending.)

## Function

### Cardiac output

Cardiac output (CO) — the volume of blood pumped per minute — is the system's primary throughput metric:

$$
CO = HR \times SV
$$

| Variable | Resting | Peak exercise |
|:---|:---:|:---:|
| Heart rate (HR) | 60–80 bpm | 180–200 bpm |
| Stroke volume (SV) | ~70 mL | ~120–150 mL |
| **Cardiac output** | **~5 L/min** | **~25 L/min** |

This 5-fold dynamic range allows the system to scale oxygen delivery to demand — the major reason aerobic exercise capacity is set largely by cardiovascular function rather than muscle metabolism.

### Pressure, flow, resistance

Across any vascular bed, the relationship is

$$
\Delta P = Q \times R \quad\text{(an analog of Ohm's law)}
$$

where ΔP is the pressure drop across the bed, Q is flow, and R is resistance [^openstax-anatomy-20-2]. Resistance scales with viscosity (η) and inversely with the **fourth power** of vessel radius (Poiseuille):

$$
R \propto \frac{8 \eta L}{\pi r^4}
$$

This radius-to-the-fourth dependence is why **arterioles dominate systemic resistance** — small changes in arteriolar tone produce large changes in flow distribution. It is also why most cardiovascular drugs that lower blood pressure work by relaxing arterioles (or by reducing cardiac output, or both).

Mean arterial pressure is approximately:

$$
MAP \approx CO \times SVR
$$

(Strictly, MAP ≈ DBP + (1/3)(SBP − DBP); SVR is systemic vascular resistance.) Resting MAP ~93 mmHg in a healthy adult.

### Regulation

The system is regulated on three timescales — beat-to-beat, minutes-to-hours, days-to-weeks:

| Timescale | Mechanism | Effectors |
|:---|:---|:---|
| **Seconds** | Baroreceptor reflex | Carotid sinus + aortic arch baroreceptors → medullary CV centers → autonomic outflow modulating heart rate (β1, M2) and arteriolar tone (α1) |
| **Seconds** | Chemoreceptor reflex | Carotid + aortic chemoreceptors detect hypoxia/hypercapnia → reflex CV/respiratory response |
| **Minutes** | Catecholamines (adrenal medulla) | Epinephrine acts at **β1AR** (cardiac, renin), β2AR (vasodilation, bronchodilation), α1 (vasoconstriction) |
| **Hours** | Renin–angiotensin–aldosterone system (RAAS) | Renal JG cells → renin → angiotensin II (vasoconstrictor) → aldosterone (Na⁺/H₂O retention) |
| **Hours** | Antidiuretic hormone (vasopressin) | Plasma osmolality + volume sensors → posterior pituitary → renal water retention; vascular V1 receptors → vasoconstriction |
| **Days–weeks** | Pressure–natriuresis, vascular remodeling, capillary density adaptation | Kidneys, vasculature, heart |

The β1-adrenergic receptor sits at the intersection of the seconds-to-minutes layer (sympathetic tone) and the cardiac response (chronotropy + inotropy + lusitropy + renin release) — a single molecule with leverage over four of the system's main control variables.

### Local autoregulation

Each major vascular bed has **autoregulation** — a local mechanism that holds flow constant across a range of arterial pressures. Cerebral circulation autoregulates from MAP ~60–150 mmHg; coronary, renal, and splanchnic each have their own ranges. Mechanisms include myogenic responses (smooth muscle contracts when stretched), metabolic vasodilation (adenosine, CO₂, K⁺, lactate), and endothelial signaling (NO, endothelin, prostaglandins).

## Connections

- **Down (constituent organ):** the cardiovascular system `contains` the **[heart](../../06-organ/heart/README.md)** as the pump. (Vasculature and blood will be added as separate entries — large arteries, capillary network, venous network, blood as tissue.)
- **Sideways (interacting systems):**
  - **Respiratory system** — gas exchange in the pulmonary circuit (entry pending).
  - **Renal system** — fluid/electrolyte balance, RAAS regulation (entry pending).
  - **Endocrine system** — catecholamines, ANP/BNP, vasopressin, RAAS (entry pending).
  - **Nervous system** — autonomic CV regulation (entry pending).
  - **Immune system** — leukocyte trafficking via the vascular network; site of vascular inflammation (entry pending).
- **Cross-atlas (planned in Phase 3):** pathogens that act systemically (sepsis, viremia) and medicines that target the system as a whole (vasopressors, vasodilators, anticoagulants) link in here.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — bradykinin → B2R on endothelium → eNOS → NO and PGI2 → vasodilation; ACE inhibitors raise bradykinin → contribute to vasodilatory cardioprotective effects; angioedema (B2R-mediated) and dry cough are bradykinin-dependent adverse effects of ACE inhibitor therapy.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — SCD causes chronic haemolysis → NO scavenging → pulmonary arterial hypertension (PAH; TRV >2.5 m/s on echo predicts mortality); cardiomegaly + high-output failure from chronic anaemia; SCD-PAH treated with sildenafil + transfusion + hydroxyurea.
- `modulated-by` → **[Adenosine](../../03-molecular/adenosine/README.md)** — A1R on SA/AV nodes → Gi → ↑IKAch → bradycardia; IV adenosine (6–12 mg, t½ ~10 s) terminates paroxysmal SVT; A2AR on coronary arteries → vasodilation; regadenoson (A2AR agonist) enables pharmacological cardiac stress testing; methylxanthines block adenosine-mediated AV block.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — romosozumab (anti-sclerostin) ARCH trial: MACE increase vs. alendronate (2.5% vs. 1.9%) → FDA Black Box Warning (avoid within 12 months of MI/stroke); sclerostin in vascular smooth muscle may protect against vascular calcification; elevated sclerostin predicts CV events in dialysis patients.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — SELECT trial (semaglutide 2.4 mg, obesity without T2DM): 20% MACE reduction vs placebo; SUSTAIN-6 and LEADER established GLP-1R agonists as antidiabetic drugs with proven CV benefit; GLP-1R on cardiomyocytes → anti-inflammatory and vasodilatory cardioprotective effects.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Cx43 gap junctions at intercalated discs create the cardiac electrical syncytium; lateralization and downregulation in heart failure → slow conduction and re-entry → VT risk; ischemia acidosis closes channels (protective); reperfusion reopens → Ca²⁺ injury propagation.
- `connects-to` → **[Phospholamban](../../03-molecular/phospholamban/README.md)** — PLN is the molecular relay of sympathoadrenergic cardiac regulation: β1-AR → PKA → PLN-pSer16 → SERCA2a disinhibition → faster Ca²⁺ reuptake → lusitropy and inotropy; PLN hyperinhibition in HFrEF (reduced pSer16) is a core Ca²⁺ cycling defect; PLN Arg9Cys → familial DCM.
- `connects-to` → **[HCN4](../../03-molecular/hcn4/README.md)** — HCN4 (funny channel) is the dominant SA node pacemaker current; cAMP directly gates HCN4 → transduces sympathetic (+10 mV shift) and vagal (-10 mV shift) chronotropic control; ivabradine (HCN4 blocker) reduces HR without negative inotropy; approved in HFrEF with HR >70 bpm.
- `connects-to` → **[RyR2](../../03-molecular/ryr2/README.md)** — RyR2 CICR amplifies the L-type Ca²⁺ trigger into cardiac contraction (~75% of Ca²⁺ transient is SR-derived); PKA and CaMKII tune RyR2 gain for sympathetic inotropy; CaMKII hyperactivation in HF → diastolic RyR2 leak → arrhythmia; RYR2 GOF mutations cause CPVT.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2/CCR2 drives monocyte infiltration into atherosclerotic plaques and adventitial macrophage accumulation; elevated serum CCL2 predicts MACE in EPIC/MRFIT cohorts; CCR2 blockade reduces plaque and improves cardiac function post-MI in murine models.
- `connects-to` → **[Troponin Complex](../../03-molecular/troponin-complex/README.md)** — Troponin complex is the molecular effector of cardiac contraction: TnC Ca²⁺ binding → TnI release → tropomyosin repositioning → actin-myosin cross-bridge cycling; PKA-mediated TnI Ser23/24 phosphorylation → ↓Ca²⁺ sensitivity → faster relaxation under β-adrenergic stimulation.
- `connects-to` → **[NCX1](../../03-molecular/ncx1/README.md)** — NCX1 is the second-largest Ca²⁺ removal pathway (~28% per beat); electrogenically exchanges 3 Na⁺:1 Ca²⁺; reverse mode → Ca²⁺ entry during action potential; NCX1 upregulation in HF impairs systolic function; NCX1 is a proposed therapeutic target in heart failure.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Inflammation drives its diseases: immune cells populate atherosclerotic plaques, autoimmune and infectious myocarditis injure the heart, and anti-inflammatory therapy (canakinumab, colchicine) reduces cardiovascular events.
- `connects-to` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — The cornerstone of prevention: statins lower LDL cholesterol and stabilise plaque, cutting heart attacks and strokes, and are foundational to both primary and secondary cardiovascular prevention.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — A leading cause of endocarditis: Staphylococcus aureus is the commonest organism in infective endocarditis, seeding and destroying heart valves from the bloodstream, especially in injection drug use and prosthetic valves.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — It sets the rhythm: the SA node, AV node and His-Purkinje system generate and route the electrical impulse that coordinates the heartbeat, and their failure produces the arrhythmias, blocks and sudden death the cardiovascular system must avoid.
- `connects-to` → **[ACE Inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — A cornerstone of cardiovascular therapy: ACE inhibitors blunt the renin-angiotensin system to lower blood pressure, unload the failing heart and protect after myocardial infarction, among the most-used cardiovascular drugs.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Its central disease: atherosclerosis — lipid-laden, inflamed plaque in artery walls — underlies coronary disease, stroke and peripheral arterial disease, the leading cause of death and the dominant pathology of the cardiovascular system.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — The contractile engine: the myocardium is the heart muscle that pumps blood through the cardiovascular system, and its failure—through infarction, cardiomyopathy or hypertrophy—drives most cardiac disease.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — The valves and inner lining: the endocardium forms the heart valves that keep blood moving in one direction and lines the chambers, the site of valvular disease, endocarditis and mural thrombus.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The common final pathway: heart failure is where cardiovascular disease converges—the heart can no longer meet the body's circulatory demand, the shared endpoint of ischaemia, hypertension and valve disease.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — The dominant modifiable risk: chronic hypertension is the single biggest driver of cardiovascular disease, accelerating atherosclerosis, hypertrophying the heart and damaging vessels throughout the circulation.
- `connects-to` → **[Stroke](../stroke/README.md)** — The brain end of vascular disease: stroke is cardiovascular disease striking the brain—atherosclerosis, atrial fibrillation and hypertension throwing clots or rupturing vessels that supply neural tissue.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The venous side of circulation: deep-vein thrombosis and pulmonary embolism are the cardiovascular system's venous failure, clots forming in stagnant veins and lodging in the lungs.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — The right-heart circulation: pulmonary arterial hypertension is the cardiovascular system's pulmonary-vascular disease, raising pressure in the lungs and failing the right ventricle—distinct from systemic hypertension and left heart disease.
- `connects-to` → **[Coxsackievirus B](../../../02-pathogen/01-viruses/coxsackievirus-b/README.md)** — Viral myocarditis: enteroviruses like Coxsackie B directly infect the heart muscle, a leading cause of acute myocarditis and dilated cardiomyopathy in young, previously healthy people.
- `connects-to` → **[Marfan Syndrome](../marfan-syndrome/README.md)** — Heritable aortopathy: Marfan and related connective-tissue disorders weaken the aortic wall, causing root dilatation, aneurysm and dissection—a genetic cardiovascular disease demanding lifelong aortic surveillance.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vascular tone: endothelin-1, the body's most potent vasoconstrictor, sets vascular resistance against the nitric oxide that opposes it, and its excess drives hypertension and vascular remodelling.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Vessel growth: VEGF directs the angiogenesis that builds and repairs the vasculature, governing collateral formation after ischaemia and the neovascularisation of atherosclerotic plaque.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Vascular inflammation: IL-6 is a central mediator of the inflammation that drives atherosclerosis, and trials targeting the IL-6/CRP axis confirm inflammation as a modifiable cardiovascular risk.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — Cardiac endocrine hormone: stretched ventricles release BNP to promote natriuresis and vasodilation, opposing the renin-angiotensin system and serving as the key biomarker of heart failure.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — RAAS and remodelling: aldosterone drives sodium retention and direct cardiac and vascular fibrosis, which is why mineralocorticoid-receptor antagonists improve outcomes in heart failure and hypertension.
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — Cholesterol and risk: PCSK9 sets circulating LDL by controlling hepatic LDL-receptor turnover, and PCSK9 inhibitors sharply lower LDL and cardiovascular events in the vasculature.
- `connects-to` → **[SERCA2a](../../03-molecular/serca2a/README.md)** — SERCA2a pumps calcium back into the sarcoplasmic reticulum after each beat, setting the rate of cardiomyocyte relaxation and refilling the store for the next contraction—central to both systolic force and diastolic filling.
- `connects-to` → **[β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — The β1-adrenergic receptor transduces sympathetic noradrenaline into faster, stronger heartbeats, the target of the beta-blockers that are foundational drugs across heart failure, arrhythmia, and ischemic heart disease.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cholesterol carried in LDL accumulates in the arterial wall to seed atherosclerotic plaque, the lipid foundation of the coronary and cerebrovascular disease that dominates cardiovascular mortality worldwide.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium influx triggers calcium-induced calcium release to drive each heartbeat, and calcium controls vascular smooth-muscle tone—the ion central to both cardiac contraction and the regulation of blood-vessel diameter and pressure.
- `connects-to` → **[von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Von Willebrand factor stored in and released from the vascular endothelium captures platelets at sites of injury, the first step of hemostasis and, when the endothelium is diseased, of arterial thrombosis.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — Renin from the kidney initiates the renin-angiotensin-aldosterone cascade that sets vascular tone and blood volume, the master endocrine controller of cardiovascular pressure and the target of ACE inhibitors and ARBs.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling governs cardiac chamber, valve and coronary-vessel development and sets arterial-venous endothelial identity, a master developmental pathway of the cardiovascular system.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β controls vascular smooth-muscle and extracellular-matrix homeostasis of the arterial wall (its dysregulation causing the aortic disease of Marfan, already mapped) and drives the cardiac fibrosis of remodeling.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — The calcineurin-NFAT pathway transduces calcium signals into the hypertrophic growth program of cardiomyocytes, central to the heart's maladaptive response to pressure and volume overload.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β drives the inflammatory cascade of atherosclerosis, validated clinically by the CANTOS trial in which IL-1β blockade reduced recurrent cardiovascular events independent of lipid lowering.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK1/2 MAPK transduces growth-factor and mechanical signals into cardiomyocyte hypertrophy and vascular smooth-muscle proliferation, a core driver of cardiac remodelling and arterial restenosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signalling mediates the IGF/insulin survival programme of cardiomyocytes and endothelial nitric-oxide production, balancing physiological adaptation against pathological hypertrophy.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling (downstream of the AKT axis mapped) governs cardiomyocyte growth and the hypertrophic remodeling of the heart in pressure and volume overload.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α coordinates the myocardial and vascular response to ischemia, driving angiogenesis and metabolic adaptation in the cardiovascular system.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB-driven endothelial and vascular inflammation is central to atherogenesis and the inflammatory component of cardiovascular disease.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 drives cardiac and vascular fibrosis and is an established biomarker of heart failure and adverse cardiovascular remodeling.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling mediates cardiomyocyte hypertrophy and the vascular inflammation shared across cardiovascular diseases.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the cardiac and vascular fibrosis central to adverse remodeling in cardiovascular disease.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate cardiomyocyte and endothelial oxidative-stress defense, autophagy, and metabolic homeostasis across the cardiovascular system.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the vascular and myocardial inflammatory responses shared across cardiovascular disorders.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING links cellular and mitochondrial stress to the sterile inflammation of cardiovascular disease.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the cardiac hypertrophy and vascular remodeling signaling of the cardiovascular system.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the physiological cardiac growth and endothelial survival of the cardiovascular system.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins participate in the inflammatory signaling of atherosclerosis and myocardial injury in the cardiovascular system.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy maintains the cardiomyocyte and vascular-cell protein-quality control and metabolic resilience of the cardiovascular system.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the vascular endothelial and smooth-muscle mechanotransduction and remodeling of the cardiovascular system.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance participates in the immune-mediated myocardial and vascular injury relevant to the cardiovascular system.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the cardiomyocyte and vascular gene programs of the cardiovascular system.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment participates in the vascular inflammation and atherogenesis of the cardiovascular system.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the endothelial homeostasis, angiogenesis, and cardiac-progenitor mobilization of the cardiovascular system.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the cardiac and vascular immune responses of the cardiovascular system.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the vascular inflammation and cardiac remodeling of the cardiovascular system.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the vascular inflammation and injury responses of the cardiovascular system.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Repolarisation: potassium channels set cardiac repolarisation and resting membrane potential, so disturbances of potassium cause the QT changes and life-threatening arrhythmias that make electrolyte balance central to cardiovascular safety.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Depolarisation and pressure: sodium channels drive the cardiac action-potential upstroke and conduction, while renal sodium handling sets blood volume and long-term blood pressure, tying the ion to both electrophysiology and haemodynamics.
- `connects-to` → **[ATP](../../03-molecular/atp/README.md)** — Cardiac energetics: the heart consumes and regenerates an enormous mass of ATP each day to power contraction, and the energy starvation of failing myocardium reflects a breakdown in this ATP supply-demand balance.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Atherosclerotic inflammation: macrophages ingest oxidised lipid to become the foam cells of the atherosclerotic plaque, and their inflammation and death drive the plaque growth and rupture behind most cardiovascular events.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pulmonary circulation: the right heart pumps blood through the lungs for gas exchange, and this pulmonary circulation is an integral loop of the cardiovascular system whose failure produces pulmonary hypertension and congestion.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Oxygen transport and deficiency: iron in haemoglobin (already mapped) carries the oxygen the circulation delivers, and iron deficiency independently worsens heart failure, linking the metal to cardiovascular function beyond anaemia.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Rhythm and vascular tone: magnesium stabilises cardiac membranes and rhythm and relaxes vascular smooth muscle (already mapped), and its deficiency predisposes to arrhythmias and hypertension, a mineral integral to cardiovascular function.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and urate risk: xanthine-oxidase-derived reactive oxygen species drive the endothelial (already mapped) dysfunction of cardiovascular disease, and the uric acid it produces is itself linked to hypertension and cardiovascular risk.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory atheroprotection: the anti-inflammatory IL-10 restrains the vascular inflammation (IL-6 and IL-1 already mapped) that drives atherosclerosis (already mapped), part of the immune balance shaping cardiovascular health.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The cardiorenal partnership: the kidney regulates blood volume and pressure through the renin-angiotensin-aldosterone system (already mapped), and the heart and kidney are locked in a bidirectional partnership central to the cardiovascular system.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Cardiac and vascular excitability: potassium sets the resting membrane potential of the cardiac and vascular smooth-muscle (already mapped) cells, and dyskalaemia causes the arrhythmias that threaten the cardiovascular system.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — The central vascular disorder: hypertension is the commonest disorder of the cardiovascular system, the raised pressure (RAAS and endothelin already mapped) driving the atherosclerosis, heart failure and stroke that dominate its disease burden.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Cardioprotective adipokine: adiponectin is an anti-atherogenic, cardioprotective adipokine of the cardiovascular system, and its fall in obesity and the metabolic syndrome (insulin and cholesterol already mapped) raises cardiovascular risk.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine and blood pressure: leptin links the obesity to the sympathetic activation (noradrenaline already mapped) and the hypertension of the cardiovascular system, part of the adipose-cardiovascular crosstalk.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Oxygen delivery: the fundamental purpose of the cardiovascular system is to deliver oxygen (carried on haemoglobin already mapped) to the tissues, the circulation matched to the metabolic demand.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Contractile cells: the cardiomyocytes are the contractile cells of the heart (the excitation-contraction — troponin and SERCA2a already mapped) that drive the circulation of the cardiovascular system.
- `connects-to` → **[SA node cell](../../04-cellular/sa-node-cell/README.md)** — Pacemaker cells: the sinoatrial-node cells (HCN4 already mapped, the funny current) set the heart rate and initiate the rhythm of the cardiovascular system.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Vascular-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose to the vascular inflammation and the cardiovascular risk of the cardiovascular system.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 vascular inflammation: the IFN-γ of the T cells is the type-II interferon arm of the Th1-driven atherosclerotic and myocardial inflammation of the cardiovascular system.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 vascular immunity: IL-4 and the type-2/M2 (macrophage) arm modulate the vascular inflammation and the plaque remodelling of the cardiovascular system.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 vascular immunity: IL-13, with IL-4 (already mapped), completes the type-2 immune arm of the vascular and cardiac remodelling of the cardiovascular system.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 vascular inflammation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the atherosclerotic and myocardial inflammation of the cardiovascular system.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophilia of the eosinophilic myocarditis and endocarditis of the cardiovascular system.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing, drives the innate inflammation of the myocarditis and the atherosclerosis of the cardiovascular system.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of the myocarditis and the atherosclerosis of the cardiovascular system.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the eosinophilic myocarditis and the hypersensitivity vasculitides of the cardiovascular system.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the myocarditis and the atherosclerotic inflammation of the cardiovascular system.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) generate the membrane-attack complex central to the atherosclerotic and ischaemia-reperfusion injury of the cardiovascular system.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid (macrophage already mapped) recruitment of the atherosclerotic and myocarditic inflammation of the cardiovascular system.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic infiltrate: the cytotoxic T cells (perforin already mapped) mediate the myocyte injury of the viral myocarditis and contribute to the atherosclerotic plaque inflammation of the cardiovascular system.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-vascular axis: TSLP, from injured endothelium (already mapped) and vascular smooth muscle, primes mast cells (already mapped) and dendritic cells (already mapped) and amplifies the Th2/eosinophil (already mapped) vascular inflammation of the cardiovascular system.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor regulates the contact-pathway kinin cascade (bradykinin already mapped) and the classical-complement activation (C3 and C5 already mapped) contributing to the angioedema and ischaemia-reperfusion of the cardiovascular system.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell vascular mediator: histamine, from cardiac and vascular mast cells (already mapped), amplifies the vascular permeability and the coronary vasospasm contributing to Kounis syndrome and the hypersensitivity myocarditis of the cardiovascular system.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Cardiac ECM remodelling: periostin, expressed by cardiac fibroblasts (already mapped) under mechanical and ischaemic stress, promotes collagen deposition and the adverse ventricular remodelling that drives hypertrophy and heart failure progression of the cardiovascular system.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian cardioprotection: melatonin, via MT1/MT2 receptors on cardiomyocytes (already mapped) and endothelial cells (already mapped), scavenges ROS, attenuates ischaemia-reperfusion injury and synchronises the circadian cardiac rhythms of the cardiovascular system.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine cardiac axis: prolactin, acting via PRLR on cardiomyocytes (already mapped) and macrophages (already mapped), modulates the cardiac inflammatory cytokine milieu and is linked to peripartum cardiomyopathy and heart failure of the cardiovascular system.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — CV testosterone: testosterone, via androgen receptors on cardiomyocytes (already mapped), attenuates NF-κB (already mapped) and IL-6 (already mapped) cardiomyopathic signalling; testosterone deficiency amplifies CVD risk and heart-failure (already mapped) morbidity.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — CV serotonin: serotonin, via 5-HT receptors on cardiomyocytes (already mapped) and endothelial cells (already mapped), modulates cardiac rhythm and vascular tone; serotonin excess amplifies the NF-κB (already mapped) and IL-6 (already mapped) cardiovascular inflammation.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — CV oxytocin: oxytocin, via OXTR on cardiomyocytes (already mapped) and endothelial cells (already mapped), attenuates NF-κB (already mapped) and IL-6 (already mapped) cardiac inflammation; oxytocin promotes nitric-oxide (already mapped) vasodilation and cardioprotection.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — CV selenium: selenium, via GPx and thioredoxin reductase, scavenges ROS in cardiomyocytes (already mapped) and endothelial cells (already mapped); selenium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cardiac inflammation and heart-failure severity.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — CV copper: copper, via ceruloplasmin and SOD, protects cardiomyocytes (already mapped) from oxidative injury; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cardiac inflammation and the cardiac fibrosis of heart failure (already mapped).
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — CV phosphorus: phosphorus drives ATP (already mapped) synthesis and SERCA2a (already mapped) calcium-pump function in cardiomyocytes (already mapped); hyperphosphataemia amplifies NF-κB (already mapped) vascular calcification and endothelial cell (already mapped) dysfunction.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — CV zinc: zinc, via SOD and cardiomyocyte (already mapped) metalloenzymes, quenches oxidative stress; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cardiac inflammation and endothelial-cell (already mapped) dysfunction in cardiovascular disease.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — CV nitrogen: nitric oxide (NO, nitrogen-derived) in endothelial cells (already mapped) and macrophages (already mapped) regulates vasodilation; NO deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and platelet (already mapped) aggregation cascade.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — CV chloride: chloride channels on cardiomyocytes (already mapped) and smooth muscle cells (already mapped) regulate membrane excitability; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cardiac fibrosis cascade.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — CV sulfur: sulfur-containing glutathione in cardiomyocytes (already mapped) and endothelial cells (already mapped) scavenges ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) and macrophage (already mapped) cascade.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — carbon-based fatty acids in smooth-muscle cell (already mapped) and macrophage (already mapped) fuel vascular ATP; disrupted carbon metabolism amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in cardiovascular disease.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — hydrogen ion dysregulation in smooth-muscle cell (already mapped) and macrophage (already mapped) amplifies vascular tone; proton excess disrupts NF-κB (already mapped) and mTOR (already mapped) and IL-6 (already mapped) signalling cascade in cardiovascular disease.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α from macrophage (already mapped) amplifies endothelial inflammation; TNF-α excess drives NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade worsening smooth-muscle cell (already mapped) dysfunction in cardiovascular disease.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — cardiovascular pd-1: PD-1 on t-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses immune-driven atherosclerosis; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in cardiovascular disease.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — cardiovascular wnt-beta-catenin: Wnt/β-catenin in smooth-muscle cells (already mapped) and macrophages (already mapped) regulates remodelling; wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in cardiovascular disease.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — cardiovascular rankl: RANKL from endothelial cells (already mapped) and macrophages (already mapped) modulates vascular calcification; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in cardiovascular disease.

## Pathology

System-level cardiovascular disease — pathologies that can't be assigned cleanly to a single organ:

| Disease | Mechanism |
|:---|:---|
| **Hypertension** | Sustained arterial pressure elevation; multifactorial (genetic, sodium, RAAS, sympathetic tone, vascular stiffness). The single largest modifiable risk factor for cardiovascular and cerebrovascular disease globally. |
| **Atherosclerosis** | Lipid deposition + inflammation in the intima of large/medium arteries; progressive plaque growth; rupture or erosion → thrombosis → tissue infarction. The substrate of myocardial infarction, ischemic stroke, and peripheral arterial disease. |
| **Shock states** | Failure of perfusion. Subtypes: hypovolemic (volume loss), cardiogenic (pump failure), distributive (sepsis, anaphylaxis, neurogenic — vasodilation + capillary leak), obstructive (tamponade, pulmonary embolism, tension pneumothorax). |
| **Pulmonary hypertension** | Sustained elevated pulmonary artery pressure → right-heart failure. Several distinct etiologies (idiopathic, drug-induced, left-heart disease, hypoxic, thromboembolic). |
| **Cardiac arrest** | Cessation of effective circulation, typically from ventricular fibrillation or asystole. Survival depends on time-to-defibrillation. |
| **Thromboembolic disease** | Inappropriate clot formation (deep vein thrombosis, pulmonary embolism, atrial-fibrillation–related cardioembolic stroke). Antithrombotic / anticoagulant therapy targets this. |
| **Vasculitis** | Inflammation of vessel walls — broad family (Takayasu, giant cell, ANCA-associated, Kawasaki, …). |

## Variation

- **Sex.** Men have higher rates of coronary artery disease at any given age until menopause; women's risk catches up post-menopause. Some heart-failure phenotypes (HFpEF) are over-represented in women, others (HFrEF) in men.
- **Age.** Arterial stiffness increases with age; baroreceptor sensitivity declines; orthostatic hypotension becomes more common. Hypertension prevalence rises steeply.
- **Genetics + ancestry + environment.** Hypertension, lipid metabolism, and atherosclerosis all show population-level variation in prevalence and treatment response, driven by complex genetic and environmental interactions.
- **Athletic adaptation.** Endurance training produces lower resting heart rate, larger stroke volume, expanded blood volume, and greater capillary density.

## Open questions

- **HFpEF** — pathophysiology and effective therapy remain incomplete despite recent advances (SGLT2 inhibitors, MRAs).
- **Microvascular disease** — coronary microvascular dysfunction, INOCA (ischemia with no obstructive coronary artery disease), and microvascular contributions to dementia and renal disease are under-recognized and undertreated.
- **Vascular aging** — what drives the difference between "biological" and chronological vascular age, and how to slow it, is an active research frontier with implications across cardiovascular and neurological disease.

## See also

- [`heart`](../../06-organ/heart/README.md) — the pump.
- [`myocardium`](../../05-tissue/myocardium/README.md) — the contractile tissue.
- [`cardiomyocyte`](../../04-cellular/cardiomyocyte/README.md) — the contractile cell.
- [`troponin-complex`](../../03-molecular/troponin-complex/README.md) — molecular calcium switch.
- [`beta1-adrenergic-receptor`](../../03-molecular/beta1-adrenergic-receptor/README.md) — primary sympathetic relay.

[^openstax-anatomy-19-1]: OpenStax. *Anatomy & Physiology 2e*, Ch. 19.1: Heart Anatomy. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy)
[^openstax-anatomy-20-2]: OpenStax. *Anatomy & Physiology 2e*, Ch. 20.2: Blood Flow, Blood Pressure, and Resistance. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/20-2-blood-flow-blood-pressure-and-resistance)
