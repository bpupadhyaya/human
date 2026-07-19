---
schema: human-scale-entry/v1
id: hypertension
name: Hypertension
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Sustained BP ≥130/80 mmHg (AHA 2017); 1.28 billion adults globally. Primary (~95%): RAAS overactivation, sympathetic excess, endothelial NO deficiency. Complications: stroke, MI, HFpEF, CKD. First-line: ACE-I/ARBs, thiazides, CCBs."
aliases: ["hypertension", "high blood pressure", "HTN", "arterial hypertension", "essential hypertension"]
sources:
  - id: whelton-2018-acc-aha
    type: peer-reviewed
    cite: "Whelton PK, Carey RM, Aronow WS, et al. 2017 ACC/AHA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Hypertension. 2018;71(6):e13-e115."
    doi: "10.1161/HYP.0000000000000065"
    pmid: "29133356"
    url: "https://doi.org/10.1161/HYP.0000000000000065"
  - id: mills-2020-global-hypertension
    type: peer-reviewed
    cite: "Mills KT, Stefanescu A, He J. The global epidemiology of hypertension. Nat Rev Nephrol. 2020;16(4):223-237."
    doi: "10.1038/s41581-019-0244-2"
    pmid: "32024986"
    url: "https://doi.org/10.1038/s41581-019-0244-2"
cross_links:
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "Hypertension causes hypertensive nephrosclerosis via afferent arteriole wall thickening and glomerular ischemia; simultaneously, the kidney's RAAS activation and impaired pressure-natriuresis are key drivers of hypertension — a bidirectional relationship."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: modulated-by
    note: "Angiotensin II is the central effector of RAAS: causes vasoconstriction via AT1R on vascular smooth muscle, stimulates aldosterone release, promotes renal sodium retention, drives cardiac hypertrophy, and promotes endothelial dysfunction via ROS generation."
  - target: 01-human/03-molecular/aldosterone
    relation: modulated-by
    note: "Aldosterone (produced by adrenal zona glomerulosa under Ang II/K+ stimulation) acts on renal distal tubule/collecting duct to increase ENaC-mediated Na+ retention and K+ excretion, expanding plasma volume and raising BP."
  - target: 01-human/04-cellular/endothelial-cell
    relation: modulates
    note: "Endothelial dysfunction is both a cause and consequence of hypertension: reduced eNOS activity lowers NO bioavailability, impairs vasodilation, and promotes vascular remodeling; hypertensive shear stress further injures endothelial cells, perpetuating the cycle."
  - target: 01-human/03-molecular/renin
    relation: modulated-by
    note: "Renin is the rate-limiting enzyme of the RAAS: released from JG cells in response to reduced perfusion, low macula densa NaCl, and β1-adrenergic stimulation → angiotensinogen → Ang I → Ang II; aliskiren (direct renin inhibitor) reduces BP; ARR screens for primary aldosteronism."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "ET-1 is the most potent vasoconstrictor and is elevated in resistant hypertension, CKD-related hypertension, and preeclampsia; ETA receptor on vascular smooth muscle → vasoconstriction; ETB receptor on endothelium → NO and PGI2 (counterbalances); dual ERA bosentan lowers BP."
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Hypertension accelerates DR through retinal arteriolar pressure, shear stress, and RAAS activation; BP control to <130/80 mmHg reduces DR progression by ~30% (UKPDS); hypertensive retinopathy and DR frequently coexist and share pathophysiology."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Hypertension and gout reinforce each other: elevated urate raises blood pressure by impairing endothelial NO and activating the RAAS, while thiazide and loop diuretics for hypertension reduce renal urate excretion and trigger gout flares — so drug choice must be coordinated."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Hypertension is the most important modifiable risk factor for stroke: chronic high pressure drives both ischemic stroke (atherosclerosis, small-vessel lipohyalinosis) and hemorrhagic stroke (Charcot-Bouchard microaneurysm rupture); each 10 mmHg drop cuts stroke risk by ~a third."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Dietary sodium is the leading modifiable driver of hypertension: excess salt expands extracellular volume and, in salt-sensitive people, raises blood pressure via impaired renal sodium handling; cutting intake toward <2 g/day lowers BP — the basis of DASH and salt-restriction."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart is a principal victim of hypertension: chronic pressure overload drives left-ventricular hypertrophy, diastolic then systolic heart failure, atrial fibrillation and—via accelerated coronary disease—myocardial infarction; blood-pressure control best prevents these."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Hypertension and CKD are locked in a vicious cycle: high pressure damages glomeruli (nephrosclerosis) while failing kidneys retain sodium and activate renin-angiotensin to raise pressure; ACE inhibitors/ARBs break the loop and are first-line in hypertensive CKD."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Hypertension is a major driver of atherosclerosis: elevated pressure and shear stress injure the endothelium and accelerate plaque formation throughout the arterial tree, so treating blood pressure reduces myocardial infarction, stroke and peripheral arterial disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Hypertension is the leading cause of heart failure: chronic pressure overload forces the left ventricle to hypertrophy, then stiffen and fail (HFpEF) or dilate (HFrEF)—decades of high afterload remodel the heart, so controlling pressure best prevents it."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Pheochromocytoma is a classic curable cause of secondary hypertension: a catecholamine-secreting adrenal tumor drives paroxysmal high blood pressure with headache, sweating and palpitations, so resistant or episodic hypertension warrants screening—surgery can cure it."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium is the dietary counterweight to sodium in blood pressure: higher potassium intake promotes natriuresis and vasodilation, lowering pressure, while hypokalemia—often from hyperaldosteronism—signals a secondary, treatable cause of hypertension."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide failure underlies much hypertension: healthy endothelium releases NO to relax arteries, so when endothelial dysfunction cuts NO, vessels stay constricted and pressure rises—linking early vascular injury to sustained high blood pressure."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Hypertension is the leading driver of cardiovascular disease: chronic high pressure damages arteries throughout the body, accelerating atherosclerosis and straining the heart, so controlling it prevents the strokes, heart attacks and kidney failure it causes."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium handling is a key hypertension lever: calcium influx contracts vascular smooth muscle to raise pressure, which is why calcium-channel blockers are first-line antihypertensives—relaxing arteries by blocking the calcium that drives their tone."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Hypertension is driven by vascular smooth muscle: arteriolar smooth-muscle tone sets peripheral resistance, and chronic high pressure thickens these cells, stiffening vessels—so smooth-muscle relaxation is the target of calcium-channel blockers and vasodilators."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The renal system is both cause and victim of hypertension: the kidney sets long-term blood pressure through salt and renin handling, so renal disease raises pressure while sustained hypertension damages the kidney—a self-amplifying vicious loop."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Norepinephrine and sympathetic drive raise blood pressure: catecholamines constrict vessels and speed the heart, so overactive sympathetic tone elevates pressure—the rationale for beta-blockers and alpha-blockers and the cause of surges in pheochromocytoma."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal gland causes curable secondary hypertension: primary aldosteronism (Conn's), cortisol excess (Cushing's), and pheochromocytoma each drive high blood pressure, so resistant or young-onset hypertension prompts a hunt for an adrenal cause."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Hypertension in pregnancy centers on the placenta: poor placental perfusion releases factors that injure maternal blood vessels, causing pre-eclampsia—high blood pressure with organ damage that endangers mother and baby and resolves only with delivery."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome helps set blood pressure: microbes ferment fiber into short-chain fatty acids that relax vessels and modulate salt handling, so dysbiosis is emerging as a factor in hypertension beyond diet and genetics."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "The heart fights hypertension by releasing BNP: when high pressure stretches the heart, it secretes natriuretic peptide to make the kidneys dump sodium and relax vessels—a built-in counterweight to high blood pressure that doctors also measure to gauge cardiac strain."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium helps set blood pressure: the mineral relaxes vascular smooth muscle and counters calcium-driven constriction, so magnesium deficiency tightens vessels while supplementing it modestly lowers blood pressure."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance drives hypertension: high insulin levels make the kidney retain sodium and rev up the sympathetic nervous system, which is why high blood pressure clusters with obesity and diabetes in the metabolic syndrome."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain both controls and suffers from blood pressure: brainstem centers set the sympathetic tone that drives it, while severe hypertension damages cerebral vessels to cause stroke and hypertensive encephalopathy—a two-way street."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol raises blood pressure: it sensitizes vessels to constrictors and makes the kidney hold sodium, so excess—from Cushing's or chronic stress—causes hypertension, one reason endocrine causes are sought in resistant cases."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T-helper cells are an emerging player in hypertension: activated T cells infiltrate the vessel wall and kidney, releasing cytokines that stiffen arteries and impair sodium handling, recasting high blood pressure partly as an inflammatory disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Hypertension is read in the eye: high pressure narrows and damages retinal vessels (hypertensive retinopathy), a visible window onto the systemic vascular harm the disease does everywhere."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Hypertension stiffens organs with fibrosis: sustained pressure drives the heart and arteries to lay down collagen, thickening and scarring the walls, a remodeling that worsens the disease and damages the kidney too."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Hypertension forces cardiomyocytes to grow: pumping against high pressure makes heart-muscle cells enlarge, thickening the left ventricle into hypertensive heart disease that eventually stiffens and fails."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging hunts secondary and end-organ hypertension: CT and MR angiography photons find renal-artery stenosis and adrenal tumors, while echocardiography measures the thickened, straining heart."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Hypertension has an immune side: macrophages infiltrate the kidney and vessel walls, and the salt they help handle and the inflammation they drive contribute to the rise in blood pressure."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Hypertension is partly a nerve disease: overactive sympathetic peripheral nerves drive up the pressure, which is why renal denervation—burning the kidney's nerves—is a treatment for resistant cases."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows how pressure remodels the arteries: chronic hypertension thickens small-vessel walls with glassy hyaline deposits and muscle overgrowth, and in malignant disease the wall undergoes fibrinoid necrosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Hypertension's vascular damage can starve the bowel: hardened, narrowed mesenteric arteries make the gut prone to ischemic colitis, especially when blood pressure suddenly drops in an already-diseased circulation."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Untreated hypertension floods the lungs: as the pressure-strained left ventricle stiffens and fails, blood backs up into the pulmonary vessels, causing the breathlessness and flash pulmonary edema of hypertensive heart disease."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Blood pressure touches reproduction at both ends: it underlies preeclampsia and pregnancy hypertension that endanger mother and fetus, and chronic hypertension and its drugs are common causes of erectile dysfunction."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "A pressure spike can overwhelm the brain: in a hypertensive emergency, autoregulation fails and fluid leaks around neurons into hypertensive encephalopathy and the posterior reversible encephalopathy syndrome (PRES), with headache, confusion, and seizures."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid is a fixable cause: hyperthyroidism raises systolic pressure and the pulse, while hypothyroidism stiffens vessels into a diastolic hypertension, so thyroid function is checked when secondary hypertension is sought."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "High pressure shears the kidney's filter cells: chronic hypertension batters the glomerular podocytes, and as these hard-to-replace cells detach, protein leaks into the urine and nephrosclerosis sets in — a main route by which hypertension drives chronic kidney disease."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Midlife hypertension is a leading modifiable risk for dementia: years of high pressure damage small cerebral vessels, starving the brain and adding vascular injury that hastens cognitive decline and Alzheimer's, so blood-pressure control helps protect the aging brain."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Vasopressin nudges pressure up two ways: the pituitary hormone constricts vessels through V1 receptors and makes the kidney retain water through V2, expanding volume — a lesser arm of blood-pressure control beyond the renin-angiotensin system."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Excess weight is a leading driver of high pressure: obesity raises blood volume, sympathetic tone, and aldosterone while compressing the kidneys, so weight gain accounts for much of the hypertension in rich and rising populations."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Hypertension has an immune arm: CD8 cytotoxic T cells infiltrate the kidney and vessel wall and sustain the salt retention and vascular inflammation that keep blood pressure high, a mechanism that reframes part of the disease as immune-driven."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Adrenaline drives the pressure surges: epinephrine from sympathetic activation and the adrenal medulla speeds the heart and constricts vessels, behind stress-related spikes and the extreme swings of pheochromocytoma."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Hypertension and diabetes travel as a metabolic pair: shared insulin resistance links them, they co-occur in metabolic syndrome, and together they multiply the risk of the kidney, heart, and stroke disease each causes."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Fat cells push the pressure up: visceral adipocytes secrete angiotensinogen, leptin, and inflammatory adipokines while activating the sympathetic nervous system, a key link between obesity and hypertension."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Hypertension has an inflammasome arm: NLRP3 activation and the IL-1β it releases promote the vascular and renal inflammation that sustains high blood pressure, part of the immune contribution to the disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Angiotensin II inflames the vessel through NF-κB: it activates NF-κB in vascular and renal cells to drive the cytokines and oxidative stress that stiffen arteries, the inflammatory engine upstream of the NLRP3 arm of hypertension."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Poor sleep pushes the pressure up: insomnia and short sleep raise sympathetic tone and blunt the normal nocturnal dip, and obstructive sleep apnea is a leading cause of resistant hypertension."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "It shares its soil with venous clots: hypertension clusters with the metabolic and vascular risk factors of venous thromboembolism, and the two are modestly associated beyond their common arterial disease."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "The link runs both ways with the kidney's cancer: hypertension is an established risk factor for renal cell carcinoma, while the tumor's renin secretion and renal damage in turn cause secondary hypertension."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Small-vessel damage muddies the movement disorder: midlife hypertension drives the cerebral small-vessel disease behind vascular parkinsonism, which mimics and worsens Parkinson's, and orthostatic swings complicate its management."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Pressure and mood interact: depression is more common in hypertension and worsens adherence and outcomes, while chronic stress and some antihypertensives influence mood, a clinically important two-way link."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety and blood pressure feed each other: chronic anxiety and sympathetic arousal acutely raise blood pressure, and living with hypertension breeds health anxiety — a bidirectional, clinically relevant link."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "It clusters with fatty-liver disease: hypertension is a core component of the metabolic syndrome that drives NASH, the two coexisting through shared insulin resistance and visceral adiposity."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Through the kidney it lowers the blood count: hypertensive nephrosclerosis is a leading cause of chronic kidney disease, and the failing kidney's loss of erythropoietin produces a renal anemia."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones cause and control blood pressure: secondary hypertension arises from primary aldosteronism, Cushing's, thyroid disease and phaeochromocytoma, and the RAAS that drives it is an endocrine axis."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Severe spikes injure the brain: a hypertensive emergency causes encephalopathy and posterior reversible encephalopathy syndrome, and chronic hypertension is the leading cause of intracerebral haemorrhage."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Sleep-disordered breathing drives it up: obstructive sleep apnoea, with its nocturnal hypoxia and sympathetic surges, is a major reversible cause of resistant hypertension."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune system helps raise the pressure: T lymphocytes and macrophages infiltrating the vessel wall and kidney drive blood-pressure elevation, and dietary salt activates these inflammatory pathways."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its drugs surface on the skin: calcium-channel blockers cause flushing and gum hypertrophy, and hydralazine can trigger a drug-induced lupus rash."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its biology and drugs touch the gut: the liver makes angiotensinogen, the substrate of the renin-angiotensin system, while calcium-channel blockers cause constipation and ACE inhibitors can rarely cause intestinal angioedema."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "First-line blockade of the renin axis: ACE inhibitors lower blood pressure by reducing angiotensin II, protecting the heart and kidneys, a cornerstone of hypertension treatment."
  - target: 03-medicine/01-modern/04-cardio/calcium-channel-blockers
    relation: connects-to
    note: "They relax the arteries: calcium-channel blockers like amlodipine lower blood pressure by dilating arterial smooth muscle, especially effective in older and Black patients."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "They slow and calm the heart: beta-blockers lower blood pressure by reducing cardiac output and renin, particularly useful when hypertension coexists with heart disease or arrhythmia."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: connects-to
    note: "A first-line RAAS blocker: angiotensin-receptor blockers like losartan lower blood pressure by blocking angiotensin II at its receptor, used like ACE inhibitors but without the cough."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: connects-to
    note: "Treating the company it keeps: most people with hypertension also need cholesterol lowering, and statins are added to cut the shared atherosclerotic cardiovascular risk."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Diet lowers the pressure: a high-fibre DASH-style diet rich in fruit, vegetables and whole grains meaningfully reduces blood pressure alongside sodium restriction."
  - target: 03-medicine/01-modern/04-cardio/loop-diuretics
    relation: connects-to
    note: "Diuretics for tougher cases: when kidney function is reduced or heart failure coexists and thiazides fail, loop diuretics like furosemide lower blood pressure by offloading the salt and water volume that sustains hypertension."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Pressure remodels the vessel itself: sustained hypertension thickens and stiffens the arterial wall through smooth-muscle hypertrophy and hyaline arteriosclerosis, a structural change that raises pressure further and sets up aneurysm and dissection."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "High pressure scars the filter: hypertension transmitted to the glomerulus causes hyalinosis and glomerulosclerosis—hypertensive nephrosclerosis—one of the leading causes of chronic kidney disease and end-stage renal failure worldwide."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Hypertensive heart disease: chronic pressure overload thickens the left ventricular myocardium (LVH), which stiffens into heart failure with preserved ejection fraction and predisposes to arrhythmia and infarction."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "The leading cause of atrial fibrillation: hypertensive left-ventricular hypertrophy and atrial stretch remodel the conduction system, making hypertension the top modifiable driver of AF."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Vascular cognitive decline: chronic hypertension damages cerebral small vessels and the hippocampus, driving vascular dementia and accelerating Alzheimer's disease."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "Renal cause and consequence: IgA nephropathy produces secondary hypertension through glomerular injury, while the resulting hypertension accelerates the loss of kidney function—a vicious cycle demanding tight blood-pressure control."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Two circulations, two diseases: pulmonary arterial hypertension is the right-heart mirror of systemic hypertension, raising pressure in the lungs rather than the aorta and demanding entirely different vasodilator drugs."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Shared vascular pharmacology: beta-blockers, calcium-channel blockers and ARBs (candesartan) all treat hypertension and also prevent migraine, reflecting overlapping neurovascular and autonomic mechanisms."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity's blood-pressure link: leptin from excess adipose tissue activates the sympathetic nervous system, a central mechanism of obesity-related hypertension."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Fibrosis of end organs: TGF-β drives the vascular stiffening and renal fibrosis of chronic hypertension, mediating much of its long-term damage to heart, kidney and arteries."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Diabetic nephropathy and pressure: type 1 diabetes commonly causes hypertension through diabetic kidney disease, and tight blood-pressure control is central to protecting the kidneys."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Vascular inflammation: IL-6 contributes to the immune and vascular inflammation increasingly recognised as a driver of hypertension and its end-organ damage."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Immune hypertension: TNF-α from activated T cells and macrophages promotes vascular dysfunction and renal sodium retention, central to the emerging immune theory of hypertension."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes into the vessel wall and kidney in hypertension, fuelling the perivascular inflammation that stiffens arteries and raises pressure."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 vascular inflammation: IL-17A from Th17 cells promotes vascular stiffening and renal sodium retention, a specific arm of the T-cell-driven immune contribution to hypertension."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Counter-regulatory vasodilator: adrenomedullin is a potent vasodilator peptide that rises in hypertension as a compensatory brake on rising pressure and endothelial dysfunction."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Renal pressure-natriuresis: renal prostaglandins promote sodium excretion and vasodilation, which is why NSAIDs that block them raise blood pressure and blunt antihypertensive drugs."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kallikrein-kinin vasodilation: bradykinin promotes endothelial vasodilation and natriuresis, and ACE inhibitors lower blood pressure partly by raising bradykinin — the same mechanism behind their characteristic dry cough."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "Natriuretic blood-pressure lowering: SGLT2 inhibition in the proximal tubule produces a natriuresis and osmotic diuresis that lower blood pressure, a newer antihypertensive action with cardiorenal benefit."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Arterial stiffening: AGE-RAGE signalling cross-links arterial collagen and drives vascular inflammation, stiffening large arteries to raise systolic and pulse pressure, especially in diabetic and ageing hypertension."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Vascular tone: calcium influx through L-type channels triggers vascular-smooth-muscle contraction that sets peripheral resistance, the mechanism blocked by the calcium-channel-blocker drugs (amlodipine) that are a first-line treatment for hypertension."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Renal natriuresis: locally produced renal dopamine acts on proximal-tubule D1 receptors to promote sodium excretion, an intrarenal natriuretic system whose impairment contributes to the salt retention behind salt-sensitive hypertension."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Urate and oxidative stress: xanthine-oxidase activity raises uric acid and generates reactive oxygen species that impair endothelial nitric oxide, and elevated serum urate is an independent associate of hypertension, especially in the young."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic link: the low adiponectin of visceral adiposity (insulin and leptin already mapped) is associated with endothelial dysfunction and elevated blood pressure, tying obesity to the metabolic-syndrome form of hypertension."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome limb: NLRP3 inflammasome activation (mapped) generates IL-1β, which promotes vascular inflammation and renal sodium handling that contribute to hypertension."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "Cardiorenal link: FGF23 rises in chronic kidney disease and independently associates with hypertension and left-ventricular hypertrophy, connecting phosphate-regulating endocrinology to blood-pressure control."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate vascular inflammation: TLR4-driven innate immune activation by damage-associated patterns contributes to the vascular and renal inflammation that sustains salt-sensitive and essential hypertension."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Endothelial NO: the PI3K-AKT-eNOS axis maintains endothelial nitric-oxide production (NO already mapped), and its impairment produces the endothelial dysfunction underlying hypertension."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Vascular oxidative defence: NRF2 antioxidant defence counters the vascular oxidative stress (xanthine-oxidase already mapped) that drives endothelial dysfunction and vascular remodelling in hypertension."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Angiotensin-II and endothelin-1 signalling (both mapped) through ERK-MAPK drives the vascular-smooth-muscle proliferation and remodelling of hypertension."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the vascular and cardiac fibrosis that mediates hypertensive target-organ damage."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR-driven vascular-smooth-muscle hypertrophy contributes to the arterial-wall remodelling and stiffening of hypertension."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the vascular inflammation that contributes to endothelial dysfunction and arterial remodelling in hypertension."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the vascular fibrosis and arterial stiffening central to the end-organ damage of hypertension."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the vascular inflammation and immune activation implicated in hypertension."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the vascular smooth-muscle and endothelial oxidative-stress responses relevant to the vascular remodeling of hypertension."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling contributes to the T-cell-driven vascular inflammation implicated in hypertension."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α links the renal and vascular hypoxic and metabolic responses to the pathophysiology of hypertension."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β participates in the vascular smooth-muscle and cardiac hypertrophic signaling relevant to hypertension."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) transduces the angiotensin-II and growth-factor signals driving vascular remodeling in hypertension."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, coupled to nitric-oxide-dependent endothelial function (nitric-oxide already mapped), is a vasodilatory regulator dysregulated in hypertension."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the vascular-smooth-muscle and endothelial homeostasis whose dysregulation contributes to hypertension."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of angiotensin-II and other vasoactive receptors participates in the vascular remodeling of hypertension."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven immune-cell recruitment into the vasculature and kidney contributes to the inflammation of hypertension."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the vascular and renal gene programs relevant to hypertension."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the vascular inflammation and immune-cell recruitment of hypertension."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the vascular inflammation and immune activation relevant to hypertension."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the vascular and immune gene programs of hypertension."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the vascular-smooth-muscle and T-cell responses of hypertension (calcineurin-inhibitor therapy is a recognized cause of secondary hypertension)."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the vascular-tone and renal regulation relevant to hypertension."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium and vascular tone: magnesium relaxes vascular smooth muscle and modulates the sodium, potassium and calcium (all already mapped) handling that sets blood pressure, and low magnesium is associated with higher blood pressure."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Hypertensive heart disease: sustained pressure overload thickens the left ventricle and predisposes to myocardial infarction, and troponin elevation marks the cardiac injury of the hypertensive heart disease that is a major end-organ complication."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences: premenopausal women have lower blood pressure than men, an advantage attributed to estrogen's vasodilatory and RAAS-modulating effects that is lost after menopause, when hypertension prevalence rises."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Endothelial activation: the endothelial dysfunction of hypertension (nitric oxide already mapped) raises von Willebrand factor, a marker of the endothelial injury and prothrombotic state that link high blood pressure to its thrombotic complications."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Cardiometabolic overlap: GLP-1 receptor agonists modestly lower blood pressure alongside weight and glucose (SGLT2 and insulin already mapped), linking the incretin axis to the metabolic management of the hypertension that clusters with obesity and diabetes."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Secondary hypertension: primary hyperparathyroidism raises blood pressure through parathyroid hormone effects on calcium (already mapped) and vascular tone, one of the endocrine secondary causes of hypertension that are potentially curable."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic clustering: hypertension clusters with dyslipidaemia in the metabolic syndrome (insulin, leptin and adiponectin already mapped), the raised cholesterol compounding the cardiovascular risk that drives combined blood-pressure and lipid treatment."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "Shared cardiovascular risk: the LDL-cholesterol handling governed by PCSK9 (cholesterol already mapped) is the co-target of cardiovascular prevention, statins and PCSK9 inhibitors treating the atherosclerotic risk that hypertension amplifies."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Diuretic mechanism: the thiazide and loop diuretics that treat hypertension block sodium-chloride cotransport (sodium already mapped), and the resulting chloride and volume loss lowers blood pressure, sometimes causing a hypochloraemic alkalosis."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Endocrine hypertension: the adrenal gland's aldosterone (already mapped) in primary aldosteronism (Conn's) and its catecholamines (epinephrine already mapped) in phaeochromocytoma are the endocrine secondary causes of hypertension to screen for."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Central control and target organ: the brain sets the sympathetic (norepinephrine already mapped) drive to blood pressure, and it suffers the hypertensive stroke and encephalopathy that are the major target-organ damage of uncontrolled hypertension."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine hypertension: resistin, with leptin and the fall in adiponectin (already mapped), is a pro-inflammatory adipokine of the metabolic syndrome (insulin already mapped) that promotes the endothelial dysfunction and vascular inflammation raising blood pressure."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 immune counter: IL-4 and the type-2 arm counter the pro-hypertensive Th17 (IL-17 already mapped) and inflammatory T-cell (TNF and IL-6 already mapped) response implicated in the vascular inflammation of hypertension."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), is part of the type-2 immune arm balancing the T-cell-driven vascular inflammation of hypertension."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonergic vascular tone: serotonin modulates the vascular tone and the central sympathetic (norepinephrine already mapped) control of the blood pressure in hypertension."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "T-cell hypertension: the IFN-γ of the T cells (IL-17 already mapped) infiltrating the vasculature and the kidney contributes to the immune/inflammatory component of hypertension."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Isoketal antigen presentation: the dendritic cells present the isolevuglandin-modified neoantigens that activate the T cells (IFN-γ already mapped) of the immune/inflammatory hypertension."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate vascular interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune vascular inflammation implicated in hypertension."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the T-cell-mediated vascular inflammation implicated in hypertension."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune/inflammatory vascular and renal injury of hypertension."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the pro-hypertensive Th1/Th17 immunity."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension that counter-balances the pro-hypertensive Th1/Th17 immunity."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Perivascular mast cells: the mast cells infiltrate the perivascular tissue and, via the renin and chymase (angiotensin already mapped), contribute to the vascular remodelling of hypertension."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK vascular inflammation: the NK cells (perforin already mapped) contribute to the T-cell (already mapped) and innate immune vascular and renal (already mapped) injury of hypertension."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Vascular complement: the complement C3 activation contributes to the immune and endothelial (already mapped) vascular inflammation of the salt-sensitive and immune-mediated hypertension."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the end-organ (kidney and heart already mapped) damage of hypertension."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement to the myeloid (macrophage already mapped) and T-cell (already mapped) vascular inflammation of hypertension."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Renal complement regulation: factor H regulates the alternative pathway (C3, C5 and C5aR1 already mapped), protecting glomerular (already mapped) and podocyte (already mapped) cells from complement-mediated injury in hypertensive nephropathy."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement and kinin control: C1-INH regulates the classical complement pathway (C3, C5 already mapped) and the bradykinin (already mapped) kinin-kallikrein axis; deficiency amplifies complement-mediated renal injury and vascular bradykinin dysregulation in hypertension."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-mediated vasoconstriction: erythropoietin, produced by the kidney (already mapped), directly vasoconstricts endothelial cells (already mapped) and raises blood pressure; ESA therapy in CKD (already mapped) hypertension is a recognised EPO-induced side effect."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Perivascular alarmin: TSLP released by tubular epithelial cells during hypertensive nephrosclerosis primes dendritic cells (already mapped) and mast cells (already mapped) to sustain the Th2 (IL-4, IL-13 already mapped) inflammatory milieu."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Vasoactive mast-cell mediator: histamine, released by the perivascular mast cells (already mapped) in hypertension, acts on vascular H1 receptors to promote vasodilation counteracting the renin-angiotensin (angiotensin II and renin already mapped) vasoconstriction."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Profibrotic matricellular protein: periostin, secreted by cardiac fibroblasts (fibrosis already mapped) under the profibrotic TGF-β (already mapped) drive of chronic pressure overload, promotes the cardiomyocyte (already mapped) hypertrophy and cardiac fibrosis of hypertension."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-hypertension axis: melatonin, via MT1 receptors on vascular smooth-muscle cells (already mapped), suppresses renin secretion (renin already mapped), modulates the nocturnal blood-pressure dip, and attenuates angiotensin II (already mapped) vasoconstriction."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-hypertension axis: testosterone, via androgen receptor on vascular smooth-muscle cells (already mapped) and kidney (already mapped), upregulates ACE (already mapped) and promotes sodium retention, driving the male sex predominance of hypertension."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Prolactin-hypertension axis: prolactin, via prolactin receptors on endothelial (already mapped) and smooth-muscle cells (already mapped), promotes oxidative stress, endothelin (already mapped) release, and salt retention, linking hyperprolactinaemia to hypertension."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Hypertension oxytocin: oxytocin, via OXTR on cardiomyocytes (already mapped) and macrophages (already mapped), attenuates inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of hypertension."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Hypertension selenium: selenium, as an antioxidant cofactor for glutathione peroxidases, attenuates oxidative vascular stress; selenium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) endothelial (already mapped) cascade of hypertension."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Hypertension iodine: iodine, via thyroid hormone biosynthesis, modulates cardiomyocyte (already mapped) contractility and vascular tone; iodine deficiency amplifies the NF-κB (already mapped) and aldosterone (already mapped) cardiovascular cascade of hypertension."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Hypertension copper: copper, as cofactor of SOD1 in macrophages (already mapped) and mast cells (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) vascular oxidative cascade of hypertension."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Hypertension zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and mast cells (already mapped), neutralises ROS; zinc deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) vascular inflammatory cascade of hypertension."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Hypertension phosphorus: phosphorus, as ATP precursor in macrophages (already mapped) and T-cytotoxic cells (already mapped), supports immune energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of hypertension."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Hypertension iron: iron, via ferritin and ROS in macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates vascular oxidative stress; iron dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of hypertension."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Hypertension sulfur: sulfur, as hydrogen sulfide (H₂S) in macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates vascular tone; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of hypertension."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Hypertension nitrogen: nitrogen, as NO (nitric oxide) precursor in macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates vascular tone; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of hypertension."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Hypertension carbon: carbon as backbone of renin-angiotensin signalling proteins and cytokines (already mapped) sustains vasoconstrictive cascade; carbon-derived metabolites in macrophages (already mapped) amplify NF-κB (already mapped) and IL-6 (already mapped) in hypertension."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Hypertension hydrogen: hydrogen as proton gradient in vascular endothelium mitochondria drives ATP synthesis; hydrogen-ion acidosis amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular remodelling in hypertension."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypertension oxygen: ROS from NADPH-oxidase in macrophages (already mapped) and T-cytotoxic cells (already mapped) drives vascular oxidative stress; oxygen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) endothelial damage in hypertension."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Hypertension pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses vascular immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular cascade in hypertension."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Hypertension vegf: VEGF from macrophages (already mapped) and T-cytotoxic cells (already mapped) drives vascular angiogenesis and remodelling; vegf dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Hypertension wnt-beta-catenin: Wnt-β-catenin from vascular smooth-muscle cells (already mapped) and macrophages (already mapped) drives arterial remodelling; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in hypertension."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Hypertension rankl: RANKL from macrophages (already mapped) and T-cytotoxic cells (already mapped) promotes vascular inflammation; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular cascade in hypertension."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Hypertension il-2: IL-2 from macrophages (already mapped) and T-cytotoxic cells (already mapped) regulates vascular immune activation; il-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Hypertension notch: NOTCH in vascular smooth-muscle cells (already mapped) and macrophages (already mapped) drives arterial stiffness; notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Hypertension fibronectin: fibronectin in vascular smooth-muscle cells (already mapped) and macrophages (already mapped) promotes remodelling; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Hypertension igf-1: IGF-1 from macrophages (already mapped) and vascular smooth-muscle cells (already mapped) promotes arterial repair; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Hypertension activin-a: activin-A from macrophages (already mapped) and vascular smooth-muscle cells (already mapped) promotes arterial fibrosis; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Hypertension cgrp: CGRP from macrophages (already mapped) and vascular smooth-muscle cells (already mapped) modulates vascular neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Hypertension calcitonin: calcitonin from endothelial cells (already mapped) and macrophages (already mapped) modulates calcium tone; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Hypertension substance-p: substance-P from macrophages (already mapped) and vascular smooth-muscle cells (already mapped) modulates pain tone; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Hypertension insulin-receptor: insulin receptor on macrophages (already mapped) and smooth-muscle cells (already mapped) modulates metabolic tone; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular cascade."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Hypertension androgen-receptor: androgen receptor on macrophages (already mapped) and smooth-muscle cells (already mapped) modulates androgen axis; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular cascade."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Hypertension bdnf: BDNF from macrophages (already mapped) and smooth-muscle cells (already mapped) modulates vascular neuroprotective tone; bdnf deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular cascade."
---

# Hypertension

## Overview

Hypertension is the **most prevalent modifiable cardiovascular risk factor** globally, affecting approximately 1.28 billion adults in 2019 — nearly one-third of the global adult population — and directly causing an estimated 10.8 million deaths annually through cardiovascular disease, stroke, and kidney failure [^mills-2020-global-hypertension]. Despite effective pharmacological treatments, control rates remain below 25% in many regions.

The AHA/ACC 2017 guidelines [^whelton-2018-acc-aha] define hypertension as sustained systolic BP **≥130 mmHg** or diastolic BP **≥80 mmHg** (measured correctly on 2+ occasions). This threshold, lowered from the previous 140/90 mmHg, reflects the continuous cardiovascular risk relationship: for every 20 mmHg increase in systolic BP above 115 mmHg, risk of cardiovascular death doubles.

**Classification (AHA 2017):**
| Stage | SBP | DBP |
|:---|:---|:---|
| Normal | <120 | <80 |
| Elevated | 120–129 | <80 |
| Stage 1 HTN | 130–139 | 80–89 |
| Stage 2 HTN | ≥140 | ≥90 |
| Hypertensive crisis | >180 | >120 |

## Structure

### Vascular Changes in Hypertension

Sustained elevated pressure drives **structural adaptation** of the vasculature — collectively termed **hypertensive vascular remodeling**:

**Large arteries (aorta, carotids):**
- Increased wall stiffness — loss of elastic fiber compliance; increased collagen deposition in medial layer
- Reduced Windkessel function → elevated pulse wave velocity → increased systolic BP and pulse pressure
- Accelerated atherosclerosis — endothelial dysfunction, increased LDL oxidation and subendothelial accumulation

**Small arteries and arterioles (resistance vessels):**
- **Inward eutrophic remodeling** — same wall mass rearranged around smaller lumen (wall/lumen ratio ↑)
- In severe/chronic hypertension: **hypertrophic remodeling** — increased wall mass via smooth muscle cell hypertrophy
- These changes fix peripheral vascular resistance at an elevated set point even if systemic BP is pharmacologically normalized

**Microcirculation:**
- Arteriolar rarefaction — reduced capillary density (both functional and structural)
- Contributes to insulin resistance (impaired muscle glucose delivery) and target organ ischemia

### End-Organ Architecture Changes

| Organ | Structural change |
|:---|:---|
| **Heart** | Left ventricular hypertrophy (concentric LVH, increased wall:cavity ratio) — response to increased afterload |
| **Kidney** | Afferent arteriole hyalinosis; glomerulosclerosis; tubular atrophy |
| **Brain** | White matter lacunar infarcts (small vessel disease); arterial microaneurysms (Charcot-Bouchard) |
| **Eye** | Arteriolar narrowing, AV nicking, copper/silver wiring; cotton wool spots; papilledema in malignant HTN |

## Function

### Regulatory Systems Governing BP

Blood pressure is determined by: BP = Cardiac Output × Peripheral Vascular Resistance. Both components are dysregulated in hypertension:

**RAAS (Renin-Angiotensin-Aldosterone System):**
- **Renin** (juxtaglomerular cells): cleaves angiotensinogen → angiotensin I (Ang I)
- **ACE** (lung endothelium): Ang I → Ang II
- **Ang II effects**: AT1R → vasoconstriction + aldosterone release + ADH stimulation + sympathetic activation + renal Na/H₂O retention + cardiac/vascular hypertrophy
- In **primary aldosteronism** (most common secondary cause): autonomous aldosterone → Na+ retention → volume-dependent HTN

**Sympathetic Nervous System:**
- Increased sympathetic tone → increased heart rate and contractility (CO ↑) + peripheral vasoconstriction (PVR ↑)
- Chronic sympathetic overactivation in hypertension demonstrated by muscle sympathetic nerve activity (MSNA) recordings

**Renal Pressure-Natriuresis:**
- Normally: BP rise → pressure natriuresis → Na+ and water excretion → BP returns to normal
- In hypertension: pressure-natriuresis relationship is reset at a higher BP operating point — requires higher pressure to achieve the same Na+ excretion; driven by RAAS, aldosterone, renal structural changes

**Endothelial Dysfunction:**
- Reduced eNOS activity and NO bioavailability → impaired vasodilation; increased ET-1 production → vasoconstriction
- Oxidative stress (Ang II → NADPH oxidase → superoxide) scavenges NO → further NO depletion

### Primary vs. Secondary Hypertension

**Primary (essential) hypertension** (~95%): polygenic + environmental; key contributors:
- RAAS genetic variants (ACE gene insertion/deletion, AGT M235T, renin-binding protein polymorphisms)
- Salt sensitivity (variants in ENaC, WNK kinase pathway, 11β-HSD2)
- Obesity-related: increased RAAS, sympathetic tone, and mechanical compression of kidneys
- Chronic stress and hypothalamic sympathetic dysregulation

**Secondary hypertension** (~5%): identifiable cause:
| Cause | Features | Mechanism |
|:---|:---|:---|
| Primary aldosteronism | Hypokalemia, low PRA, high aldosterone | Autonomous aldosterone secretion (adenoma or bilateral hyperplasia) |
| Renovascular disease | Flash pulmonary edema, abdominal bruit | Renal artery stenosis → RAAS activation |
| Pheochromocytoma | Paroxysmal HTN, headache, sweating, palpitations | Catecholamine excess |
| CKD | Renal markers, bilateral small kidneys | Impaired Na excretion + RAAS activation |
| Obstructive sleep apnea | Obesity, nocturnal desaturations | Hypoxia → sympathetic activation |
| Cushing's syndrome | Central obesity, striae, cortisol excess | Glucocorticoid activation of mineralocorticoid receptors |

## Connections

- `modulates` → **[Kidney](../../06-organ/kidney/README.md)** — hypertension drives hypertensive nephrosclerosis and CKD; kidney RAAS dysregulation is a key hypertension driver
- `modulated-by` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — central RAAS effector driving vasoconstriction, aldosterone release, and vascular remodeling
- `modulated-by` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — promotes sodium retention and volume expansion; primary aldosteronism is the most common secondary cause of hypertension
- `modulates` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — hypertensive shear stress damages endothelium; endothelial NO deficiency sustains elevated BP
- `modulated-by` → **[Renin](../../03-molecular/renin/README.md)** — Renin is the rate-limiting enzyme of the RAAS: released from JG cells in response to reduced perfusion, low macula densa NaCl, and β1-adrenergic stimulation → angiotensinogen → Ang I → Ang II; aliskiren (direct renin inhibitor) reduces BP; ARR screens for primary aldosteronism.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — ET-1 is the most potent vasoconstrictor and is elevated in resistant hypertension, CKD-related hypertension, and preeclampsia; ETA receptor on vascular smooth muscle → vasoconstriction; ETB receptor on endothelium → NO and PGI2 (counterbalances); dual ERA bosentan lowers BP.
- `connects-to` → **[Diabetic Retinopathy](../diabetic-retinopathy/README.md)** — Hypertension accelerates DR through retinal arteriolar pressure, shear stress, and RAAS activation; BP control to <130/80 mmHg reduces DR progression by ~30% (UKPDS); hypertensive retinopathy and DR frequently coexist and share pathophysiology.
- `connects-to` → **[Gout](../gout/README.md)** — Hypertension and gout reinforce each other: elevated urate raises blood pressure by impairing endothelial NO and activating the RAAS, while thiazide and loop diuretics for hypertension reduce renal urate excretion and trigger gout flares — so drug choice must be coordinated.
- `connects-to` → **[Stroke](../stroke/README.md)** — Hypertension is the most important modifiable risk factor for stroke: chronic high pressure drives both ischemic stroke (atherosclerosis, small-vessel lipohyalinosis) and hemorrhagic stroke (Charcot-Bouchard microaneurysm rupture); each 10 mmHg drop cuts stroke risk by ~a third.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Dietary sodium is the leading modifiable driver of hypertension: excess salt expands extracellular volume and, in salt-sensitive people, raises blood pressure via impaired renal sodium handling; cutting intake toward <2 g/day lowers BP — the basis of DASH and salt-restriction.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart is a principal victim of hypertension: chronic pressure overload drives left-ventricular hypertrophy, diastolic then systolic heart failure, atrial fibrillation and—via accelerated coronary disease—myocardial infarction; blood-pressure control best prevents these.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Hypertension and CKD are locked in a vicious cycle: high pressure damages glomeruli (nephrosclerosis) while failing kidneys retain sodium and activate renin-angiotensin to raise pressure; ACE inhibitors/ARBs break the loop and are first-line in hypertensive CKD.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Hypertension is a major driver of atherosclerosis: elevated pressure and shear stress injure the endothelium and accelerate plaque formation throughout the arterial tree, so treating blood pressure reduces myocardial infarction, stroke and peripheral arterial disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Hypertension is the leading cause of heart failure: chronic pressure overload forces the left ventricle to hypertrophy, then stiffen and fail (HFpEF) or dilate (HFrEF)—decades of high afterload remodel the heart, so controlling pressure best prevents it.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Pheochromocytoma is a classic curable cause of secondary hypertension: a catecholamine-secreting adrenal tumor drives paroxysmal high blood pressure with headache, sweating and palpitations, so resistant or episodic hypertension warrants screening—surgery can cure it.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Potassium is the dietary counterweight to sodium in blood pressure: higher potassium intake promotes natriuresis and vasodilation, lowering pressure, while hypokalemia—often from hyperaldosteronism—signals a secondary, treatable cause of hypertension.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Nitric oxide failure underlies much hypertension: healthy endothelium releases NO to relax arteries, so when endothelial dysfunction cuts NO, vessels stay constricted and pressure rises—linking early vascular injury to sustained high blood pressure.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Hypertension is the leading driver of cardiovascular disease: chronic high pressure damages arteries throughout the body, accelerating atherosclerosis and straining the heart, so controlling it prevents the strokes, heart attacks and kidney failure it causes.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium handling is a key hypertension lever: calcium influx contracts vascular smooth muscle to raise pressure, which is why calcium-channel blockers are first-line antihypertensives—relaxing arteries by blocking the calcium that drives their tone.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Hypertension is driven by vascular smooth muscle: arteriolar smooth-muscle tone sets peripheral resistance, and chronic high pressure thickens these cells, stiffening vessels—so smooth-muscle relaxation is the target of calcium-channel blockers and vasodilators.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The renal system is both cause and victim of hypertension: the kidney sets long-term blood pressure through salt and renin handling, so renal disease raises pressure while sustained hypertension damages the kidney—a self-amplifying vicious loop.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Norepinephrine and sympathetic drive raise blood pressure: catecholamines constrict vessels and speed the heart, so overactive sympathetic tone elevates pressure—the rationale for beta-blockers and alpha-blockers and the cause of surges in pheochromocytoma.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal gland causes curable secondary hypertension: primary aldosteronism (Conn's), cortisol excess (Cushing's), and pheochromocytoma each drive high blood pressure, so resistant or young-onset hypertension prompts a hunt for an adrenal cause.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Hypertension in pregnancy centers on the placenta: poor placental perfusion releases factors that injure maternal blood vessels, causing pre-eclampsia—high blood pressure with organ damage that endangers mother and baby and resolves only with delivery.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome helps set blood pressure: microbes ferment fiber into short-chain fatty acids that relax vessels and modulate salt handling, so dysbiosis is emerging as a factor in hypertension beyond diet and genetics.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — The heart fights hypertension by releasing BNP: when high pressure stretches the heart, it secretes natriuretic peptide to make the kidneys dump sodium and relax vessels—a built-in counterweight to high blood pressure that doctors also measure to gauge cardiac strain.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium helps set blood pressure: the mineral relaxes vascular smooth muscle and counters calcium-driven constriction, so magnesium deficiency tightens vessels while supplementing it modestly lowers blood pressure.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance drives hypertension: high insulin levels make the kidney retain sodium and rev up the sympathetic nervous system, which is why high blood pressure clusters with obesity and diabetes in the metabolic syndrome.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain both controls and suffers from blood pressure: brainstem centers set the sympathetic tone that drives it, while severe hypertension damages cerebral vessels to cause stroke and hypertensive encephalopathy—a two-way street.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol raises blood pressure: it sensitizes vessels to constrictors and makes the kidney hold sodium, so excess—from Cushing's or chronic stress—causes hypertension, one reason endocrine causes are sought in resistant cases.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T-helper cells are an emerging player in hypertension: activated T cells infiltrate the vessel wall and kidney, releasing cytokines that stiffen arteries and impair sodium handling, recasting high blood pressure partly as an inflammatory disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Hypertension is read in the eye: high pressure narrows and damages retinal vessels (hypertensive retinopathy), a visible window onto the systemic vascular harm the disease does everywhere.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Hypertension stiffens organs with fibrosis: sustained pressure drives the heart and arteries to lay down collagen, thickening and scarring the walls, a remodeling that worsens the disease and damages the kidney too.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Hypertension forces cardiomyocytes to grow: pumping against high pressure makes heart-muscle cells enlarge, thickening the left ventricle into hypertensive heart disease that eventually stiffens and fails.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging hunts secondary and end-organ hypertension: CT and MR angiography photons find renal-artery stenosis and adrenal tumors, while echocardiography measures the thickened, straining heart.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Hypertension has an immune side: macrophages infiltrate the kidney and vessel walls, and the salt they help handle and the inflammation they drive contribute to the rise in blood pressure.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Hypertension is partly a nerve disease: overactive sympathetic peripheral nerves drive up the pressure, which is why renal denervation—burning the kidney's nerves—is a treatment for resistant cases.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows how pressure remodels the arteries: chronic hypertension thickens small-vessel walls with glassy hyaline deposits and muscle overgrowth, and in malignant disease the wall undergoes fibrinoid necrosis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Hypertension's vascular damage can starve the bowel: hardened, narrowed mesenteric arteries make the gut prone to ischemic colitis, especially when blood pressure suddenly drops in an already-diseased circulation.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Untreated hypertension floods the lungs: as the pressure-strained left ventricle stiffens and fails, blood backs up into the pulmonary vessels, causing the breathlessness and flash pulmonary edema of hypertensive heart disease.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Blood pressure touches reproduction at both ends: it underlies preeclampsia and pregnancy hypertension that endanger mother and fetus, and chronic hypertension and its drugs are common causes of erectile dysfunction.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — A pressure spike can overwhelm the brain: in a hypertensive emergency, autoregulation fails and fluid leaks around neurons into hypertensive encephalopathy and the posterior reversible encephalopathy syndrome (PRES), with headache, confusion, and seizures.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid is a fixable cause: hyperthyroidism raises systolic pressure and the pulse, while hypothyroidism stiffens vessels into a diastolic hypertension, so thyroid function is checked when secondary hypertension is sought.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — High pressure shears the kidney's filter cells: chronic hypertension batters the glomerular podocytes, and as these hard-to-replace cells detach, protein leaks into the urine and nephrosclerosis sets in — a main route by which hypertension drives chronic kidney disease.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Midlife hypertension is a leading modifiable risk for dementia: years of high pressure damage small cerebral vessels, starving the brain and adding vascular injury that hastens cognitive decline and Alzheimer's, so blood-pressure control helps protect the aging brain.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Vasopressin nudges pressure up two ways: the pituitary hormone constricts vessels through V1 receptors and makes the kidney retain water through V2, expanding volume — a lesser arm of blood-pressure control beyond the renin-angiotensin system.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Hypertension and diabetes travel as a metabolic pair: shared insulin resistance links them, they co-occur in metabolic syndrome, and together they multiply the risk of the kidney, heart, and stroke disease each causes.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Fat cells push the pressure up: visceral adipocytes secrete angiotensinogen, leptin, and inflammatory adipokines while activating the sympathetic nervous system, a key link between obesity and hypertension.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Hypertension has an inflammasome arm: NLRP3 activation and the IL-1β it releases promote the vascular and renal inflammation that sustains high blood pressure, part of the immune contribution to the disease.
- `connects-to` → **[Obesity](../obesity/README.md)** — Excess weight is a leading driver of high pressure: obesity raises blood volume, sympathetic tone, and aldosterone while compressing the kidneys, so weight gain accounts for much of the hypertension in rich and rising populations.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Hypertension has an immune arm: CD8 cytotoxic T cells infiltrate the kidney and vessel wall and sustain the salt retention and vascular inflammation that keep blood pressure high, a mechanism that reframes part of the disease as immune-driven.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Adrenaline drives the pressure surges: epinephrine from sympathetic activation and the adrenal medulla speeds the heart and constricts vessels, behind stress-related spikes and the extreme swings of pheochromocytoma.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Angiotensin II inflames the vessel through NF-κB: it activates NF-κB in vascular and renal cells to drive the cytokines and oxidative stress that stiffen arteries, the inflammatory engine upstream of the NLRP3 arm of hypertension.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Poor sleep pushes the pressure up: insomnia and short sleep raise sympathetic tone and blunt the normal nocturnal dip, and obstructive sleep apnea is a leading cause of resistant hypertension.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — It shares its soil with venous clots: hypertension clusters with the metabolic and vascular risk factors of venous thromboembolism, and the two are modestly associated beyond their common arterial disease.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — The link runs both ways with the kidney's cancer: hypertension is an established risk factor for renal cell carcinoma, while the tumor's renin secretion and renal damage in turn cause secondary hypertension.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Small-vessel damage muddies the movement disorder: midlife hypertension drives the cerebral small-vessel disease behind vascular parkinsonism, which mimics and worsens Parkinson's, and orthostatic swings complicate its management.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Pressure and mood interact: depression is more common in hypertension and worsens adherence and outcomes, while chronic stress and some antihypertensives influence mood, a clinically important two-way link.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety and blood pressure feed each other: chronic anxiety and sympathetic arousal acutely raise blood pressure, and living with hypertension breeds health anxiety — a bidirectional, clinically relevant link.
- `connects-to` → **[NASH](../nash/README.md)** — It clusters with fatty-liver disease: hypertension is a core component of the metabolic syndrome that drives NASH, the two coexisting through shared insulin resistance and visceral adiposity.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Through the kidney it lowers the blood count: hypertensive nephrosclerosis is a leading cause of chronic kidney disease, and the failing kidney's loss of erythropoietin produces a renal anemia.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones cause and control blood pressure: secondary hypertension arises from primary aldosteronism, Cushing's, thyroid disease and phaeochromocytoma, and the RAAS that drives it is an endocrine axis.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Severe spikes injure the brain: a hypertensive emergency causes encephalopathy and posterior reversible encephalopathy syndrome, and chronic hypertension is the leading cause of intracerebral haemorrhage.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Sleep-disordered breathing drives it up: obstructive sleep apnoea, with its nocturnal hypoxia and sympathetic surges, is a major reversible cause of resistant hypertension.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune system helps raise the pressure: T lymphocytes and macrophages infiltrating the vessel wall and kidney drive blood-pressure elevation, and dietary salt activates these inflammatory pathways.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its drugs surface on the skin: calcium-channel blockers cause flushing and gum hypertrophy, and hydralazine can trigger a drug-induced lupus rash.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its biology and drugs touch the gut: the liver makes angiotensinogen, the substrate of the renin-angiotensin system, while calcium-channel blockers cause constipation and ACE inhibitors can rarely cause intestinal angioedema.
- `connects-to` → **[ACE inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — First-line blockade of the renin axis: ACE inhibitors lower blood pressure by reducing angiotensin II, protecting the heart and kidneys, a cornerstone of hypertension treatment.
- `connects-to` → **[Calcium-channel Blockers](../../../03-medicine/01-modern/04-cardio/calcium-channel-blockers/README.md)** — They relax the arteries: calcium-channel blockers like amlodipine lower blood pressure by dilating arterial smooth muscle, especially effective in older and Black patients.
- `connects-to` → **[Beta-blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — They slow and calm the heart: beta-blockers lower blood pressure by reducing cardiac output and renin, particularly useful when hypertension coexists with heart disease or arrhythmia.
- `connects-to` → **[ARBs](../../../03-medicine/01-modern/04-cardio/arbs/README.md)** — A first-line RAAS blocker: angiotensin-receptor blockers like losartan lower blood pressure by blocking angiotensin II at its receptor, used like ACE inhibitors but without the cough.
- `connects-to` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — Treating the company it keeps: most people with hypertension also need cholesterol lowering, and statins are added to cut the shared atherosclerotic cardiovascular risk.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Diet lowers the pressure: a high-fibre DASH-style diet rich in fruit, vegetables and whole grains meaningfully reduces blood pressure alongside sodium restriction.
- `connects-to` → **[Loop Diuretics](../../../03-medicine/01-modern/04-cardio/loop-diuretics/README.md)** — Diuretics for tougher cases: when kidney function is reduced or heart failure coexists and thiazides fail, loop diuretics like furosemide lower blood pressure by offloading the salt and water volume that sustains hypertension.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Pressure remodels the vessel itself: sustained hypertension thickens and stiffens the arterial wall through smooth-muscle hypertrophy and hyaline arteriosclerosis, a structural change that raises pressure further and sets up aneurysm and dissection.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — High pressure scars the filter: hypertension transmitted to the glomerulus causes hyalinosis and glomerulosclerosis—hypertensive nephrosclerosis—one of the leading causes of chronic kidney disease and end-stage renal failure worldwide.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Hypertensive heart disease: chronic pressure overload thickens the left ventricular myocardium (LVH), which stiffens into heart failure with preserved ejection fraction and predisposes to arrhythmia and infarction.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — The leading cause of atrial fibrillation: hypertensive left-ventricular hypertrophy and atrial stretch remodel the conduction system, making hypertension the top modifiable driver of AF.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Vascular cognitive decline: chronic hypertension damages cerebral small vessels and the hippocampus, driving vascular dementia and accelerating Alzheimer's disease.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — Renal cause and consequence: IgA nephropathy produces secondary hypertension through glomerular injury, while the resulting hypertension accelerates the loss of kidney function—a vicious cycle demanding tight blood-pressure control.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Two circulations, two diseases: pulmonary arterial hypertension is the right-heart mirror of systemic hypertension, raising pressure in the lungs rather than the aorta and demanding entirely different vasodilator drugs.
- `connects-to` → **[Migraine](../migraine/README.md)** — Shared vascular pharmacology: beta-blockers, calcium-channel blockers and ARBs (candesartan) all treat hypertension and also prevent migraine, reflecting overlapping neurovascular and autonomic mechanisms.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity's blood-pressure link: leptin from excess adipose tissue activates the sympathetic nervous system, a central mechanism of obesity-related hypertension.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Fibrosis of end organs: TGF-β drives the vascular stiffening and renal fibrosis of chronic hypertension, mediating much of its long-term damage to heart, kidney and arteries.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Diabetic nephropathy and pressure: type 1 diabetes commonly causes hypertension through diabetic kidney disease, and tight blood-pressure control is central to protecting the kidneys.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Vascular inflammation: IL-6 contributes to the immune and vascular inflammation increasingly recognised as a driver of hypertension and its end-organ damage.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Immune hypertension: TNF-α from activated T cells and macrophages promotes vascular dysfunction and renal sodium retention, central to the emerging immune theory of hypertension.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes into the vessel wall and kidney in hypertension, fuelling the perivascular inflammation that stiffens arteries and raises pressure.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 vascular inflammation: IL-17A from Th17 cells promotes vascular stiffening and renal sodium retention, a specific arm of the T-cell-driven immune contribution to hypertension.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Counter-regulatory vasodilator: adrenomedullin is a potent vasodilator peptide that rises in hypertension as a compensatory brake on rising pressure and endothelial dysfunction.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Renal pressure-natriuresis: renal prostaglandins promote sodium excretion and vasodilation, which is why NSAIDs that block them raise blood pressure and blunt antihypertensive drugs.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Bradykinin promotes endothelial vasodilation and natriuresis, and ACE inhibitors lower blood pressure partly by raising bradykinin levels—the same mechanism behind the characteristic dry cough that limits their use.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — SGLT2 inhibition in the proximal tubule produces a natriuresis and osmotic diuresis that lower blood pressure, a newer antihypertensive action that comes with substantial cardiorenal benefit beyond glucose control.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — AGE-RAGE signaling cross-links arterial collagen and drives vascular inflammation, stiffening the large arteries to raise systolic and pulse pressure—a key mechanism of the isolated systolic hypertension of aging and diabetes.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium influx through L-type channels triggers vascular-smooth-muscle contraction that sets peripheral resistance, the mechanism blocked by the calcium-channel-blocker drugs (amlodipine) that are a first-line treatment for hypertension.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Locally produced renal dopamine acts on proximal-tubule D1 receptors to promote sodium excretion, an intrarenal natriuretic system whose impairment contributes to the salt retention behind salt-sensitive hypertension.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Xanthine-oxidase activity raises uric acid and generates reactive oxygen species that impair endothelial nitric oxide, and elevated serum urate is an independent associate of hypertension, especially in the young.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — The low adiponectin of visceral adiposity (insulin and leptin already mapped) is associated with endothelial dysfunction and elevated blood pressure, tying obesity to the metabolic-syndrome form of hypertension.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — NLRP3 inflammasome activation (mapped) generates IL-1β, which promotes vascular inflammation and renal sodium handling that contribute to hypertension.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — FGF23 rises in chronic kidney disease and independently associates with hypertension and left-ventricular hypertrophy, connecting phosphate-regulating endocrinology to blood-pressure control.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4-driven innate immune activation by damage-associated patterns contributes to the vascular and renal inflammation that sustains salt-sensitive and essential hypertension.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — The PI3K-AKT-eNOS axis maintains endothelial nitric-oxide production (NO already mapped), and its impairment produces the endothelial dysfunction underlying hypertension.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant defense counters the vascular oxidative stress (xanthine-oxidase already mapped) that drives endothelial dysfunction and vascular remodeling in hypertension.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Angiotensin-II and endothelin-1 signaling (both mapped) through ERK-MAPK drives the vascular-smooth-muscle proliferation and remodeling of hypertension.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the vascular and cardiac fibrosis that mediates hypertensive target-organ damage.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-driven vascular-smooth-muscle hypertrophy contributes to the arterial-wall remodeling and stiffening of hypertension.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the vascular inflammation that contributes to endothelial dysfunction and arterial remodeling in hypertension.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the vascular fibrosis and arterial stiffening central to the end-organ damage of hypertension.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the vascular inflammation and immune activation implicated in hypertension.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the vascular smooth-muscle and endothelial oxidative-stress responses relevant to the vascular remodeling of hypertension.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling contributes to the T-cell-driven vascular inflammation implicated in hypertension.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α links the renal and vascular hypoxic and metabolic responses to the pathophysiology of hypertension.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β participates in the vascular smooth-muscle and cardiac hypertrophic signaling relevant to hypertension.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) transduces the angiotensin-II and growth-factor signals driving vascular remodeling in hypertension.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, coupled to nitric-oxide-dependent endothelial function (nitric-oxide already mapped), is a vasodilatory regulator dysregulated in hypertension.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy maintains the vascular-smooth-muscle and endothelial homeostasis whose dysregulation contributes to hypertension.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of angiotensin-II and other vasoactive receptors participates in the vascular remodeling of hypertension.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven immune-cell recruitment into the vasculature and kidney contributes to the inflammation of hypertension.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the vascular and renal gene programs relevant to hypertension.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the vascular inflammation and immune-cell recruitment of hypertension.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the vascular inflammation and immune activation relevant to hypertension.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the vascular and immune gene programs of hypertension.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the vascular-smooth-muscle and T-cell responses of hypertension (calcineurin-inhibitor therapy is a recognized cause of secondary hypertension).
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the vascular-tone and renal regulation relevant to hypertension.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium and vascular tone: magnesium relaxes vascular smooth muscle and modulates the sodium, potassium and calcium (all already mapped) handling that sets blood pressure, and low magnesium is associated with higher blood pressure.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Hypertensive heart disease: sustained pressure overload thickens the left ventricle and predisposes to myocardial infarction, and troponin elevation marks the cardiac injury of the hypertensive heart disease that is a major end-organ complication.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences: premenopausal women have lower blood pressure than men, an advantage attributed to estrogen's vasodilatory and RAAS-modulating effects that is lost after menopause, when hypertension prevalence rises.
- `connects-to` → **[Von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — Endothelial activation: the endothelial dysfunction of hypertension (nitric oxide already mapped) raises von Willebrand factor, a marker of the endothelial injury and prothrombotic state that link high blood pressure to its thrombotic complications.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Cardiometabolic overlap: GLP-1 receptor agonists modestly lower blood pressure alongside weight and glucose (SGLT2 and insulin already mapped), linking the incretin axis to the metabolic management of the hypertension that clusters with obesity and diabetes.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Secondary hypertension: primary hyperparathyroidism raises blood pressure through parathyroid hormone effects on calcium (already mapped) and vascular tone, one of the endocrine secondary causes of hypertension that are potentially curable.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Metabolic clustering: hypertension clusters with dyslipidaemia in the metabolic syndrome (insulin, leptin and adiponectin already mapped), the raised cholesterol compounding the cardiovascular risk that drives combined blood-pressure and lipid treatment.
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — Shared cardiovascular risk: the LDL-cholesterol handling governed by PCSK9 (cholesterol already mapped) is the co-target of cardiovascular prevention, statins and PCSK9 inhibitors treating the atherosclerotic risk that hypertension amplifies.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Diuretic mechanism: the thiazide and loop diuretics that treat hypertension block sodium-chloride cotransport (sodium already mapped), and the resulting chloride and volume loss lowers blood pressure, sometimes causing a hypochloraemic alkalosis.
- `connects-to` → **[Adrenal gland](../../06-organ/adrenal-gland/README.md)** — Endocrine hypertension: the adrenal gland's aldosterone (already mapped) in primary aldosteronism (Conn's) and its catecholamines (epinephrine already mapped) in phaeochromocytoma are the endocrine secondary causes of hypertension to screen for.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Central control and target organ: the brain sets the sympathetic (norepinephrine already mapped) drive to blood pressure, and it suffers the hypertensive stroke and encephalopathy that are the major target-organ damage of uncontrolled hypertension.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine hypertension: resistin, with leptin and the fall in adiponectin (already mapped), is a pro-inflammatory adipokine of the metabolic syndrome (insulin already mapped) that promotes the endothelial dysfunction and vascular inflammation raising blood pressure.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 immune counter: IL-4 and the type-2 arm counter the pro-hypertensive Th17 (IL-17 already mapped) and inflammatory T-cell (TNF and IL-6 already mapped) response implicated in the vascular inflammation of hypertension.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), is part of the type-2 immune arm balancing the T-cell-driven vascular inflammation of hypertension.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonergic vascular tone: serotonin modulates the vascular tone and the central sympathetic (norepinephrine already mapped) control of the blood pressure in hypertension.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — T-cell hypertension: the IFN-γ of the T cells (IL-17 already mapped) infiltrating the vasculature and the kidney contributes to the immune/inflammatory component of hypertension.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Isoketal antigen presentation: the dendritic cells present the isolevuglandin-modified neoantigens that activate the T cells (IFN-γ already mapped) of the immune/inflammatory hypertension.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate vascular interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune vascular inflammation implicated in hypertension.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the T-cell-mediated vascular inflammation implicated in hypertension.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune/inflammatory vascular and renal injury of hypertension.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the pro-hypertensive Th1/Th17 immunity.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension that counter-balances the pro-hypertensive Th1/Th17 immunity.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Perivascular mast cells: the mast cells infiltrate the perivascular tissue and, via the renin and chymase (angiotensin already mapped), contribute to the vascular remodelling of hypertension.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — NK vascular inflammation: the NK cells (perforin already mapped) contribute to the T-cell (already mapped) and innate immune vascular and renal (already mapped) injury of hypertension.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Vascular complement: the complement C3 activation contributes to the immune and endothelial (already mapped) vascular inflammation of the salt-sensitive and immune-mediated hypertension.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the end-organ (kidney and heart already mapped) damage of hypertension.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement to the myeloid (macrophage already mapped) and T-cell (already mapped) vascular inflammation of hypertension.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Renal complement regulation: factor H regulates the alternative pathway (C3, C5 and C5aR1 already mapped), protecting glomerular (already mapped) and podocyte (already mapped) cells from complement-mediated injury in hypertensive nephropathy.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement and kinin control: C1-INH regulates the classical complement pathway (C3, C5 already mapped) and the bradykinin (already mapped) kinin-kallikrein axis; deficiency amplifies complement-mediated renal injury and vascular bradykinin dysregulation in hypertension.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-mediated vasoconstriction: erythropoietin, produced by the kidney (already mapped), directly vasoconstricts endothelial cells (already mapped) and raises blood pressure; ESA therapy in CKD (already mapped) hypertension is a recognised EPO-induced side effect.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Perivascular alarmin: TSLP released by tubular epithelial cells during hypertensive nephrosclerosis primes dendritic cells (already mapped) and mast cells (already mapped) to sustain the Th2 (IL-4, IL-13 already mapped) inflammatory milieu.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Vasoactive mast-cell mediator: histamine, released by the perivascular mast cells (already mapped) in hypertension, acts on vascular H1 receptors to promote vasodilation counteracting the renin-angiotensin (angiotensin II and renin already mapped) vasoconstriction.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Profibrotic matricellular protein: periostin, secreted by cardiac fibroblasts (fibrosis already mapped) under the profibrotic TGF-β drive of chronic pressure overload, promotes the cardiomyocyte (already mapped) hypertrophy and cardiac fibrosis of hypertension.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-hypertension axis: melatonin, via MT1 receptors on vascular smooth-muscle cells (already mapped), suppresses renin secretion (renin already mapped), modulates the nocturnal blood-pressure dip, and attenuates angiotensin II (already mapped) vasoconstriction.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-hypertension axis: testosterone, via androgen receptor on vascular smooth-muscle cells (already mapped) and kidney (already mapped), upregulates ACE (already mapped) and promotes sodium retention, driving the male sex predominance of hypertension.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Prolactin-hypertension axis: prolactin, via prolactin receptors on endothelial (already mapped) and smooth-muscle cells (already mapped), promotes oxidative stress, endothelin (already mapped) release, and salt retention, linking hyperprolactinaemia to hypertension.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Hypertension oxytocin: oxytocin, via OXTR on cardiomyocytes (already mapped) and macrophages (already mapped), attenuates inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of hypertension.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Hypertension selenium: selenium, as an antioxidant cofactor for glutathione peroxidases, attenuates oxidative vascular stress; selenium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) endothelial (already mapped) cascade of hypertension.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Hypertension iodine: iodine, via thyroid hormone biosynthesis, modulates cardiomyocyte (already mapped) contractility and vascular tone; iodine deficiency amplifies the NF-κB (already mapped) and aldosterone (already mapped) cardiovascular cascade of hypertension.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Hypertension copper: copper, as cofactor of SOD1 in macrophages (already mapped) and mast cells (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) vascular oxidative cascade of hypertension.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Hypertension zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and mast cells (already mapped), neutralises ROS; zinc deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) vascular inflammatory cascade of hypertension.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Hypertension phosphorus: phosphorus, as ATP precursor in macrophages (already mapped) and T-cytotoxic cells (already mapped), supports immune energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of hypertension.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Hypertension iron: iron, via ferritin and ROS in macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates vascular oxidative stress; iron dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of hypertension.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Hypertension sulfur: sulfur, as hydrogen sulfide (H₂S) in macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates vascular tone; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of hypertension.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Hypertension nitrogen: nitrogen, as NO (nitric oxide) precursor in macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates vascular tone; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of hypertension.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Hypertension carbon: carbon as backbone of renin-angiotensin signalling proteins and cytokines (already mapped) sustains vasoconstrictive cascade; carbon-derived metabolites in macrophages (already mapped) amplify NF-κB (already mapped) and IL-6 (already mapped) in hypertension.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Hypertension hydrogen: hydrogen as proton gradient in vascular endothelium mitochondria drives ATP synthesis; hydrogen-ion acidosis amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular remodelling in hypertension.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypertension oxygen: ROS from NADPH-oxidase in macrophages (already mapped) and T-cytotoxic cells (already mapped) drives vascular oxidative stress; oxygen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) endothelial damage in hypertension.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Hypertension pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses vascular immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular cascade in hypertension.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Hypertension vegf: VEGF from macrophages (already mapped) and T-cytotoxic cells (already mapped) drives vascular angiogenesis and remodelling; vegf dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension.
- `connects-to` → **[Wnt-β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Hypertension wnt-beta-catenin: Wnt-β-catenin from vascular smooth-muscle cells (already mapped) and macrophages (already mapped) drives arterial remodelling; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in hypertension.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Hypertension rankl: RANKL from macrophages (already mapped) and T-cytotoxic cells (already mapped) promotes vascular inflammation; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular cascade in hypertension.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Hypertension il-2: IL-2 from macrophages (already mapped) and T-cytotoxic cells (already mapped) regulates vascular immune activation; il-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — Hypertension notch: NOTCH in vascular smooth-muscle cells (already mapped) and macrophages (already mapped) drives arterial stiffness; notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Hypertension fibronectin: fibronectin in vascular smooth-muscle cells (already mapped) and macrophages (already mapped) promotes remodelling; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Hypertension igf-1: IGF-1 from macrophages (already mapped) and vascular smooth-muscle cells (already mapped) promotes arterial repair; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Hypertension activin-a: activin-A from macrophages (already mapped) and vascular smooth-muscle cells (already mapped) promotes arterial fibrosis; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Hypertension cgrp: CGRP from macrophages (already mapped) and vascular smooth-muscle cells (already mapped) modulates vascular neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Hypertension calcitonin: calcitonin from endothelial cells (already mapped) and macrophages (already mapped) modulates calcium tone; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — Hypertension substance-p: substance-P from macrophages (already mapped) and vascular smooth-muscle cells (already mapped) modulates pain tone; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) cascade in hypertension.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — Hypertension insulin-receptor: insulin receptor on macrophages (already mapped) and smooth-muscle cells (already mapped) modulates metabolic tone; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular cascade.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — Hypertension androgen-receptor: androgen receptor on macrophages (already mapped) and smooth-muscle cells (already mapped) modulates androgen axis; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular cascade.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Hypertension bdnf: BDNF from macrophages (already mapped) and smooth-muscle cells (already mapped) modulates vascular neuroprotective tone; bdnf deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and aldosterone (already mapped) vascular cascade.

## Pathology

### Cardiovascular Complications

Hypertension drives a spectrum of cardiovascular diseases through mechanical stress and neurohumoral activation:

**Left Ventricular Hypertrophy (LVH):**
- Concentric LVH (increased wall:cavity ratio) in chronic pressure overload
- LVH is an independent cardiovascular risk factor (beyond BP itself); associated with diastolic dysfunction → HFpEF
- Regression of LVH with BP control reduces mortality

**Coronary Artery Disease:**
- Accelerated atherosclerosis (endothelial injury → lipid accumulation → plaque → ACS)
- Hypertension doubles MI risk; the population-attributable fraction of MI from hypertension is ~35%

**Stroke:**
- Hypertension is the strongest modifiable stroke risk factor; risk is ~4-fold for ischemic, ~10-fold for hemorrhagic stroke vs. normotension
- Lacunar infarcts: small vessel disease → fibrinoid necrosis of penetrating arteries → deep white matter infarcts
- Intracerebral hemorrhage: Charcot-Bouchard microaneurysm rupture in basal ganglia/pons/cerebellum

**Heart Failure:**
- HFpEF: LVH → diastolic dysfunction → elevated filling pressures → pulmonary congestion with preserved EF
- HFrEF: chronic pressure overload → myocyte apoptosis + fibrosis → systolic dysfunction

**CKD and ESRD:**
- Hypertensive nephrosclerosis: afferent arteriole injury → glomerular ischemia → glomerulosclerosis → proteinuria → ESRD
- Hypertension is the second leading cause of ESRD (after diabetes) globally

### Hypertensive Crisis

**Hypertensive urgency** (SBP >180 or DBP >120, without end-organ damage): gradual oral BP lowering over 24–48 hours.

**Hypertensive emergency** (severe HTN + acute end-organ damage): IV therapy with target of reducing MAP by ≤25% in first hour, then to 160/100 over next 2–6 hours:
- Encephalopathy/stroke: labetalol, nicardipine (avoid nitroprusside)
- Acute MI: nitroglycerine, beta-blockade
- Aortic dissection: esmolol + nitroprusside (target SBP <120 within minutes)
- Pulmonary edema: nitroglycerine, loop diuretics
- Eclampsia: magnesium + hydralazine/labetalol

[^whelton-2018-acc-aha]: Whelton PK et al. 2017 ACC/AHA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. *Hypertension.* 2018;71(6):e13-e115. [doi:10.1161/HYP.0000000000000065](https://doi.org/10.1161/HYP.0000000000000065) · [PubMed 29133356](https://pubmed.ncbi.nlm.nih.gov/29133356/)
[^mills-2020-global-hypertension]: Mills KT, Stefanescu A, He J. The global epidemiology of hypertension. *Nat Rev Nephrol.* 2020;16(4):223-237. [doi:10.1038/s41581-019-0244-2](https://doi.org/10.1038/s41581-019-0244-2) · [PubMed 32024986](https://pubmed.ncbi.nlm.nih.gov/32024986/)
