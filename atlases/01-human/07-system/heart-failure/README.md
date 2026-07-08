---
schema: human-scale-entry/v1
id: heart-failure
name: Heart Failure
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Syndrome of impaired cardiac output inadequate for tissue metabolic demands. HFrEF (EF<40%), HFmrEF (40-49%), HFpEF (≥50%). ~64 million affected. GDMT: ACE-I/ARBs, beta-blockers, MRA, SGLT2i, ARNI (sacubitril-valsartan)."
aliases: ["heart failure", "HF", "congestive heart failure", "CHF", "HFrEF", "HFpEF", "cardiac failure"]
sources:
  - id: mcmurray-2014-paradigm-hf
    type: peer-reviewed
    cite: "McMurray JJV, Packer M, Desai AS, et al. Angiotensin-neprilysin inhibition versus enalapril in heart failure. N Engl J Med. 2014;371(11):993-1004."
    doi: "10.1056/NEJMoa1409077"
    pmid: "25176015"
    url: "https://doi.org/10.1056/NEJMoa1409077"
  - id: ponikowski-2016-esc-hf
    type: peer-reviewed
    cite: "Ponikowski P, Voors AA, Anker SD, et al. 2016 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. Eur Heart J. 2016;37(27):2129-2200."
    doi: "10.1093/eurheartj/ehw128"
    pmid: "27206819"
    url: "https://doi.org/10.1093/eurheartj/ehw128"
cross_links:
  - target: 01-human/06-organ/heart
    relation: part-of
    note: "Heart failure is the systemic manifestation of impaired cardiac pump function; the heart is the primary failing organ, with downstream consequences affecting lungs, kidneys, liver, and skeletal muscle."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: modulated-by
    note: "Angiotensin II is a central driver of heart failure progression: causes vasoconstriction (increased afterload), aldosterone-mediated sodium retention (volume overload), direct cardiac myocyte hypertrophy, and cardiac fibrosis via TGF-β induction."
  - target: 01-human/03-molecular/aldosterone
    relation: modulated-by
    note: "Aldosterone promotes sodium and water retention, myocardial fibrosis (collagen I deposition in cardiac interstitium), and potassium/magnesium depletion; MRA (spironolactone/eplerenone) blockade reduces mortality in HFrEF."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: contains
    note: "Cardiomyocytes are the primary failing cells in heart failure: adaptive hypertrophy, calcium handling dysfunction (reduced SERCA2a, elevated diastolic Ca2+), sarcomeric disarray, mitochondrial dysfunction, and ultimately apoptosis drive the progression to heart failure."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "Elevated LDL-C from PCSK9 GOF mutations accelerates coronary atherosclerosis → MI → ischemic cardiomyopathy and heart failure; PCSK9 inhibitors reduce MI risk in high-risk CVD patients; PCSK9 may also have direct myocardial effects via apoE and apoB receptor pathways."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "DAPA-HF (dapagliflozin, HFrEF): 25% reduction in worsening HF + CV death in T2D and non-T2D; EMPEROR-Reduced (empagliflozin): 25% reduction; SGLT2 inhibitors are the fourth pillar of GDMT, reducing HHF and CV death independent of diabetes status."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "Elevated FGF23 in CKD activates cardiac FGFR4 independent of αKlotho → HDAC4 nuclear translocation → cardiac hypertrophic gene program → LVH and HF; FGF23 is an independent predictor of incident heart failure and cardiovascular death in CKD and the general population."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "BNP is released by ventricular myocytes under wall stress → NPR-A → cGMP → natriuresis and vasodilation; BNP/NT-proBNP diagnose and prognosticate HF; sacubitril (neprilysin inhibitor in ARNI) raises ANP/BNP → PARADIGM-HF: 20% RRR vs. ACE-I in HFrEF."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 secreted by cardiac macrophages activates cardiac fibroblasts → collagen synthesis → myocardial fibrosis and diastolic dysfunction; serum galectin-3 ≥17.8 ng/mL is an FDA-approved HF biomarker predicting mortality; galectin-3 predicts incident HFpEF."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Serum soluble ST2 (sST2, decoy IL-33 receptor) >35 ng/mL predicts HF mortality independent of BNP; IL-33/ST2 signaling in cardiomyocytes is cardioprotective against pressure overload; sST2 is FDA-cleared for HF risk stratification and monitoring response to therapy."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Periostin from cardiac fibroblasts → integrin αvβ3 on cardiomyocytes and fibroblasts → FAK/PI3K → myofibroblast differentiation and collagen I/III deposition; periostin is required for post-MI cardiac fibrosis (periostin-null mice have impaired scar formation)."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Ventricular Cx43 is down-regulated and lateralized in heart failure → electrical uncoupling → slow conduction → re-entrant VT substrate → sudden cardiac death; Cx43 dephosphorylation (loss of pSer368) marks gap junction dysfunction and correlates with arrhythmia risk."
  - target: 01-human/03-molecular/phospholamban
    relation: connects-to
    note: "PLN hyperinhibition of SERCA2a is the central Ca²⁺ handling defect in HFrEF: elevated PP1/PP2A → reduced PLN-pSer16 → constitutive SERCA2a inhibition → slow Ca²⁺ reuptake → impaired relaxation and contractility; AAV1.SERCA2a gene therapy (CUPID) aimed to restore Ca²⁺ cycling."
  - target: 01-human/03-molecular/hcn4
    relation: connects-to
    note: "Heart failure with persistent tachycardia: ivabradine (HCN4 I_f blocker) reduces HR without negative inotropy; SHIFT trial: 18% reduction in HF hospitalization in HFrEF with HR >70 bpm; European guidelines recommend ivabradine as adjunct therapy in HFrEF with HR >70 bpm."
  - target: 01-human/03-molecular/ryr2
    relation: connects-to
    note: "CaMKII hyperactivation in HFrEF hyperphosphorylates RyR2 Ser2814 → diastolic Ca²⁺ leak → SR Ca²⁺ depletion + delayed afterdepolarizations → ventricular arrhythmia; diastolic RyR2 Ca²⁺ leak is a core mechanism linking Ca²⁺ cycling dysfunction to sudden cardiac death in HF."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "High-sensitivity cTn is elevated in HF proportional to ventricular remodeling severity; persistent cTn elevation in HFrEF reflects ongoing cardiomyocyte injury and predicts mortality; cTn elevation in acute decompensated HF and myocarditis reflects inflammation-driven release."
  - target: 01-human/03-molecular/ncx1
    relation: connects-to
    note: "NCX1 is upregulated in failing human ventricle → increased Ca²⁺ extrusion → further SR Ca²⁺ depletion (additive to SERCA2a downregulation) → reduced contractility; inward INCX during repolarization prolongs action potential → delayed afterdepolarizations → arrhythmia in HFrEF."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Heart failure and the kidney fail together as the cardiorenal syndrome: a failing heart underperfuses the kidney while congestion raises venous pressure, so renal function falls, fluid is retained, and diuretic resistance and worsening azotemia dominate management."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Hypertension is a leading cause of heart failure: chronic pressure overload drives left ventricular hypertrophy that stiffens into diastolic failure (HFpEF) or dilates into systolic failure, so blood-pressure control is the biggest preventable HF risk factor."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Heart failure is the common endpoint of cardiovascular disease: ischemia, valve disease, hypertension and arrhythmia all converge on a heart that can no longer meet the body's demands, making it the shared final pathway of the failing cardiovascular system."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Atherosclerosis is the leading road to heart failure: coronary disease and myocardial infarction kill heart muscle, and the scarred, weakened ventricle that remains can no longer pump adequately—so ischemic cardiomyopathy is the commonest cause of HF."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Heart failure is in large part a fibrotic disease: stressed myocardium replaces lost muscle with stiff collagen scar, which impairs both contraction and relaxation—so cardiac fibrosis underlies the remodeling that drives both reduced and preserved ejection fraction HF."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Heart failure floods the lungs: when the failing left ventricle can't keep up, pressure backs up into the pulmonary circulation, leaking fluid into alveoli—so breathlessness and pulmonary edema are the cardinal symptoms that bring patients to hospital."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency is common and treatable in heart failure: even without anemia, low iron impairs cardiac and muscle energetics and worsens symptoms, so intravenous iron is now recommended to improve quality of life and cut hospitalizations."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity is a major driver of heart failure, especially HFpEF: excess weight raises filling pressures, inflames and stiffens the heart, and the obese-HFpEF phenotype is now a target for GLP-1 and SGLT2 therapies that aid both weight and the heart."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Heart failure activates the sympathetic nervous system: norepinephrine initially props up output but chronically harms the failing heart, driving remodeling and arrhythmia—which is why beta-blockers that blunt it are a cornerstone of treatment."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Heart failure is a calcium-cycling failure: the sick cardiomyocyte can't pump calcium in and out fast enough (downregulated SERCA), so each beat is weaker and relaxation incomplete—the molecular basis of the failing squeeze."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "The failing heart is starved of ATP: damaged mitochondria can't supply enough energy for the constant work of pumping, so the heart runs like an engine low on fuel—an energy deficit that worsens the contractile failure."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Heart failure is driven by cardiac macrophages: after injury they shift from repair to chronic inflammation, fueling the fibrosis and adverse remodeling that stiffen and enlarge the failing heart."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Heart failure is a disease of sodium and water overload: the failing heart triggers hormones that make the kidney retain salt, causing the congestion and edema—while dilutional hyponatremia, paradoxically, marks the most severe disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Heart failure backs up into the liver: a congested, failing right heart raises venous pressure that engorges the liver and, over time, scars it into cardiac cirrhosis, so abnormal liver tests can flag worsening heart failure."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibroblasts stiffen the failing heart: after injury and under neurohormonal stress they lay down collagen scar between muscle cells, the fibrosis that hardens the ventricle and disrupts its electrical and mechanical function."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging stages heart failure: chest X-ray photons show an enlarged heart and congested lungs, while cardiac MRI and nuclear scans gauge function and viability to guide treatment."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Failing small vessels drive HFpEF: coronary microvascular endothelial dysfunction is now seen as central to heart failure with preserved ejection fraction, inflaming and stiffening the heart from its tiniest vessels."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium is a constant worry in heart failure: the disease and its drugs swing it in both directions, and either too-high or too-low potassium triggers the arrhythmias behind sudden cardiac death."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads the failing heart muscle: it shows swollen, dysfunctional mitochondria and disarrayed sarcomeres, and reveals the tangled amyloid fibrils of cardiac amyloidosis, an increasingly recognized cause of stiff-heart failure."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium quietly slips away in heart failure: loop and thiazide diuretics flush it out, and the resulting deficiency primes the heart for arrhythmias and amplifies digoxin toxicity, so it is watched alongside potassium."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Anemia haunts heart failure: low red-cell counts, driven by kidney dysfunction and iron deficiency, force the failing heart to work harder for less oxygen delivery, worsening symptoms and prognosis in the cardiorenal-anemia syndrome."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid sets the heart's tempo: hyperthyroidism drives high-output failure and atrial fibrillation while hypothyroidism weakens contraction and slows the rate, so thyroid function is checked in new or worsening heart failure — and amiodarone can derange it."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Advanced heart failure wastes the body: cardiac cachexia and a congested, protein-losing gut drop albumin, and the low level both worsens the edema through reduced oncotic pressure and marks a grim prognosis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Heart failure floods the body with water-holding hormone: the failing circulation triggers vasopressin release, which retains free water and dilutes the blood's sodium into the hyponatremia that flags severe disease and is targeted by vaptan drugs."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both diagnose and cause heart failure: BNP and NT-proBNP are read by immunoassay to confirm and grade it, while autoantibody-driven myocarditis — including the immune-checkpoint kind — is a reversible cause worth catching early."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The failing heart over-revs its nerves: baroreceptor signaling drives a maladaptive sympathetic surge from autonomic neurons that strains the myocardium further — the vicious cycle beta-blockers interrupt to improve survival."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Heart failure reaches the bedroom and the delivery room: erectile dysfunction is common from the disease and its drugs, while pregnancy's volume load is hazardous in cardiomyopathy and can itself trigger peripartum heart failure."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "The failing heart triggers a damaging feedback loop: falling output makes the kidney release renin, firing up the renin-angiotensin-aldosterone system that retains salt and water and remodels the heart — the very axis ACE inhibitors and ARBs block."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Heart and kidney fail together: in cardiorenal syndrome poor cardiac output and venous congestion injure the kidneys while fluid overload worsens the heart, a vicious cycle that complicates diuretic dosing in advanced disease."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "A weak heart throws clots to the brain: low ejection fraction and the atrial fibrillation that often accompanies heart failure let thrombi form in the stagnant chambers and embolize, raising stroke risk and prompting anticoagulation."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes weakens the heart directly: beyond accelerating coronary disease, high glucose and insulin resistance cause a diabetic cardiomyopathy that stiffens and fails the muscle — part of why the SGLT2 drugs born for diabetes now treat heart failure itself."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "A vasodilator the drugs deliberately spare: ACE inhibitors and the neprilysin component of sacubitril raise bradykinin, easing afterload and remodeling in heart failure — the same accumulation that causes their hallmark cough and angioedema."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "The failing heart outgrows its blood supply: inadequate VEGF-driven angiogenesis leaves the hypertrophied and HFpEF myocardium with coronary microvascular rarefaction, starving the muscle of the capillaries it needs."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation drives the remodeling: NF-κB activation in the stressed myocardium switches on the cytokines and hypertrophic genes that progressively scar and dilate the failing heart, a target of interest beyond the standard neurohormonal blockade."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Sluggish circulation favors clots: the low cardiac output, venous congestion and reduced mobility of heart failure create a prothrombotic state that raises the risk of deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Anemia and heart failure feed each other: chronic inflammation, kidney dysfunction and iron deficiency make anemia common in heart failure, worsening symptoms and prognosis in the cardiorenal-anemia syndrome."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Left-sided failure backs pressure into the lungs: chronically raised left-atrial pressure transmits to the pulmonary circulation, causing the post-capillary (group 2) pulmonary hypertension that complicates and worsens heart failure."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Diuretics and low output raise uric acid: loop diuretics and reduced renal perfusion in heart failure cut urate excretion, so hyperuricemia and gout flares are common, and high uric acid itself tracks with worse prognosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "It weighs heavily on mood: depression is common in heart failure, driven by the limits of breathlessness and fatigue and by shared inflammatory pathways, and it independently predicts hospitalization and death."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "A failing pump starves the brain: chronically low cardiac output and recurrent hypoperfusion reduce cerebral blood flow, and heart failure is an independent risk factor for vascular and Alzheimer-type cognitive decline."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Backed-up venous pressure congests the liver: right-sided heart failure engorges the liver, and the shared metabolic syndrome links cardiac disease with fatty-liver disease, together driving congestive hepatopathy and fibrosis."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Congestion and frailty invite severe infection: pulmonary congestion predisposes to pneumonia, and the debilitated, often hospitalized heart-failure patient is vulnerable to infections that can escalate to sepsis."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Iron deficiency is rife in failing hearts: both absolute and functional iron deficiency are very common in heart failure, worsening symptoms and exercise capacity, so intravenous iron is a recognised therapy."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "A congested gut starves the body: venous congestion and low output in heart failure cause bowel-wall oedema with malabsorption and a leaky gut, driving the cardiac cachexia that marks advanced disease."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Breathlessness and a fragile prognosis breed worry: the dyspnoea, fear of decompensation and burdensome regimen of heart failure foster chronic anxiety alongside its well-recognised depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It floods the lungs: a failing left heart backs pressure into the pulmonary circulation, causing congestion and oedema with orthopnoea, paroxysmal nocturnal dyspnoea, pleural effusions and Cheyne-Stokes breathing."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Heart and kidney fail together: in cardiorenal syndrome poor cardiac output and venous congestion impair renal function, while fluid retention worsens the heart, and diuretic resistance complicates both."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones drive its decline: neurohormonal activation of the renin-angiotensin-aldosterone and sympathetic systems propels heart failure, so blocking them with ACE inhibitors, MRAs and beta-blockers is the core of therapy."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It wastes the muscles: advanced heart failure causes cardiac cachexia with skeletal-muscle wasting and sarcopenia that reduce exercise capacity and worsen prognosis."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Low output and overdrive disturb the brain: chronic cerebral hypoperfusion impairs cognition, sympathetic overactivation drives progression, and Cheyne-Stokes breathing fragments sleep."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Inflammation feeds its decline: raised inflammatory cytokines such as TNF and IL-6 contribute to cardiac cachexia and the progression of heart failure."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "A cornerstone of treatment: ACE inhibitors reduce afterload and block harmful neurohormonal remodelling, lowering mortality in heart failure with reduced ejection fraction."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "They reverse the harmful drive: beta-blockers blunt the chronic sympathetic overactivation of heart failure, improving survival despite initially reducing contractility."
  - target: 03-medicine/01-modern/04-cardio/loop-diuretics
    relation: connects-to
    note: "They relieve the congestion: loop diuretics like furosemide remove the salt and water overload that causes the breathlessness and oedema of decompensated heart failure."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: connects-to
    note: "RAS blockade when ACE fails: angiotensin-receptor blockers replace ACE inhibitors in patients who cannot tolerate their cough, and combined with neprilysin inhibition as ARNI they are a cornerstone of heart-failure therapy."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "The failing muscle remodels: heart failure reflects diseased myocardium — dilated and thin in systolic failure, stiff and hypertrophied in HFpEF — where cardiomyocyte loss and interstitial fibrosis progressively impair contraction and filling."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "It is an electrical disease too: heart failure disrupts conduction, causing ventricular arrhythmias and sudden death that warrant ICDs, while left-bundle delay creates dyssynchrony corrected by cardiac resynchronisation therapy."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "It floods the air sacs: left heart failure raises pulmonary venous pressure until fluid leaks into the alveoli, causing the pulmonary oedema, orthopnoea and breathlessness of acute decompensation."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Cardiorenal syndrome strains the filter: falling cardiac output and venous congestion reduce glomerular perfusion and filtration, the kidney dysfunction that complicates heart failure and limits diuresis."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "A treatable cause hides in the marrow: AL (light-chain) amyloidosis from a plasma-cell clone deposits in the myocardium as a restrictive cardiomyopathy, so unexplained heart failure with thick walls warrants a myeloma workup."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Cor pulmonale: COPD raises pulmonary vascular resistance and right-heart afterload, driving right-sided heart failure, and the two diseases share smoking and systemic inflammation."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Afterload and stiffness: stiffening of the arterial wall raises the load the heart pumps against and is central to heart failure with preserved ejection fraction, coupling vascular ageing to cardiac failure."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Marrow links to the failing heart: heart failure drives a cardio-renal-anaemia syndrome, and age-related clonal haematopoiesis (CHIP) from the bone marrow fuels inflammation that accelerates its progression."
  - target: 02-pathogen/04-parasites/trypanosoma-cruzi
    relation: connects-to
    note: "Chagas cardiomyopathy: chronic Trypanosoma cruzi infection slowly destroys the myocardium and conduction system, making Chagas disease a leading cause of heart failure and sudden death in Latin America."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Cardio-oncology: anthracyclines and HER2-targeted trastuzumab used for breast cancer are cardiotoxic, causing a treatment-related cardiomyopathy and heart failure that is a major survivorship concern."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "Valvular heart failure: diseased heart valves lined by endocardium—from calcific aortic stenosis, regurgitation or rheumatic disease—impose chronic pressure or volume overload that drives the ventricle into failure."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Maladaptive vasoconstriction: endothelin-1 drives vasoconstriction and cardiac fibrosis in heart failure, a neurohormonal axis that worsens afterload and remodelling."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Cardiac cachexia: TNF-α and chronic inflammation drive the muscle and fat wasting of cardiac cachexia, a marker of advanced, poor-prognosis heart failure."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "The adiponectin paradox: adiponectin rises in advanced heart failure and, counter to its metabolic benefits, high levels track with disease severity and worse outcomes."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory prognosis: circulating IL-6 is elevated in heart failure and predicts severity and mortality, reflecting the chronic inflammation that contributes to myocardial remodelling and cachexia."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Sterile inflammation: NLRP3 inflammasome activation in cardiac macrophages and fibroblasts drives IL-1β release after injury, promoting adverse remodelling and fibrosis in heart failure — an emerging therapeutic target."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Hypertrophic growth: chronic mTOR signalling drives pathological cardiomyocyte hypertrophy and maladaptive remodelling, while its modulation is studied to limit progression to heart failure."
  - target: 01-human/03-molecular/serca2a
    relation: connects-to
    note: "Impaired calcium reuptake: SERCA2a expression and activity fall in the failing heart, slowing sarcoplasmic-reticulum calcium reuptake to produce the depressed contractility and impaired relaxation central to systolic and diastolic heart failure."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: connects-to
    note: "Adrenergic desensitisation: chronic sympathetic overdrive in heart failure downregulates and uncouples β1-adrenergic receptors, the maladaptation that beta-blockers reverse to improve survival."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "Cardiac cachexia: the failing heart releases myostatin that, with systemic inflammation, drives the skeletal-muscle wasting and cardiac cachexia marking advanced heart failure and predicting poor outcome."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron deficiency: inflammation-driven hepcidin elevation causes functional iron deficiency in heart failure, impairing exercise capacity independent of anaemia and reversed by intravenous iron, which improves symptoms and reduces admissions."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "NO-cGMP signalling: impaired nitric-oxide-cGMP signalling drives the myocardial stiffness and microvascular dysfunction of heart failure, especially HFpEF, the pathway targeted by the soluble-guanylate-cyclase stimulator vericiguat."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Obesity-HFpEF: GLP-1 receptor agonists (semaglutide) improve symptoms and exercise capacity in the obesity phenotype of heart failure with preserved ejection fraction, linking the metabolic axis to a major and growing HF subtype."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Pathological hypertrophy: the calcineurin-NFAT pathway transduces sustained cardiomyocyte calcium signals into the maladaptive hypertrophic gene programme that drives the ventricular remodelling of heart failure."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Myocardial fibrosis: TGF-β drives the cardiac-fibroblast activation and interstitial fibrosis (fibrosis and periostin already mapped) that stiffen the failing ventricle, central to heart failure with preserved ejection fraction."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Hypertrophic signalling: neurohormonal and mechanical stress signal through the MAPK-ERK1/2 cascade to drive the hypertrophic growth of cardiomyocytes during the remodelling of heart failure."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Hypertrophy switch: PI3K-AKT signalling governs cardiomyocyte growth — physiological when IGF-driven, but its sustained pathological activation (with mTOR mapped) contributes to the maladaptive hypertrophy of heart failure."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative injury: oxidative stress overwhelms NRF2 antioxidant defences in the failing myocardium, contributing to the cardiomyocyte injury and adverse remodelling of heart failure."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Cardiomyocyte loss: caspase-3-mediated apoptosis of cardiomyocytes progressively depletes contractile units, a cell-death mechanism driving the decline of the failing heart."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Sterile inflammation: TLR4 sensing of damage-associated molecular patterns from injured myocardium drives the sterile inflammation that contributes to adverse remodelling in heart failure."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammatory remodelling: IL-6-JAK-STAT signalling (IL-6 already mapped) participates in the inflammatory and hypertrophic remodelling of the failing heart, with STAT3 also mediating cardioprotection."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Myocardial hypoxia: HIF-1α responses to the hypoxia of the failing heart drive metabolic and angiogenic adaptations that are initially protective but maladaptive when sustained."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the cardiac fibrosis and adverse ventricular remodelling central to the progression of heart failure."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling mediates cardiomyocyte hypertrophy and the inflammatory remodelling of the failing myocardium in heart failure."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Mitochondrial DNA released by stressed cardiomyocytes engages cGAS-STING, driving the sterile inflammation that contributes to adverse remodelling in heart failure."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate cardiomyocyte autophagy, atrophy, and oxidative-stress defense, processes that shape adverse remodeling in heart failure."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates pathological cardiac hypertrophy and fibrosis, acting as a brake whose dysregulation contributes to heart failure remodeling."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling promotes cardiomyocyte apoptosis and the inflammatory remodeling of the failing myocardium in heart failure."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the balance between adaptive and maladaptive cardiac hypertrophy in heart failure."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released during myocardial stress amplify the inflammatory cardiac remodeling of heart failure."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic-lymphocyte perforin activity contributes to the immune-mediated myocardial injury in inflammatory heart failure."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling governs the cardiomyocyte energy homeostasis whose failure drives the metabolic remodeling of heart failure."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the cardiomyocyte survival and protein-quality control in the failing heart."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the cardiac hypertrophic and fibrotic remodeling of heart failure."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte recruitment contributes to the myocardial inflammation and adverse remodeling of heart failure."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic reprogramming of the failing myocardium in heart failure."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation contributes to the myocardial inflammation and adverse remodeling of heart failure."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the cardiac repair, inflammatory-cell recruitment, and remodeling of heart failure."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the cardiac inflammation and fibrosis of heart failure."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the cardiac remodeling gene programs of heart failure."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid cardiomyopathy: both hyper- and hypothyroidism impair cardiac output, and the low-T3 syndrome of advanced heart failure is a marker of poor prognosis, making thyroid-hormone status a modifiable contributor to the failing heart."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Diabetic cardiomyopathy: insulin resistance and hyperglycaemia produce a distinct diabetic cardiomyopathy and worsen outcomes in heart failure, the bidirectional metabolic link that underlies the cardiac benefit of SGLT2 inhibitors (already mapped)."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress and urate: xanthine oxidase generates reactive oxygen species and uric acid in the failing heart, and elevated serum urate is an independent marker of severity, reflecting the oxidative burden of impaired myocardial energetics."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia of heart failure: anaemia is common in heart failure from iron deficiency (already mapped), inflammation and renal dysfunction, and low haemoglobin worsens symptoms, exercise capacity and prognosis."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences and peripartum disease: estrogen influences the sex differences in heart failure, with women predominating in HFpEF, and its abrupt fall postpartum is implicated in peripartum cardiomyopathy."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Viral cardiac injury: COVID-19 can cause myocarditis and precipitate or worsen heart failure (troponin already mapped), one of several viral illnesses that acutely stress the failing or vulnerable myocardium."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Ischaemic lipids: the atherogenic cholesterol (PCSK9 already mapped) driving coronary disease underlies ischaemic cardiomyopathy, the commonest cause of heart failure with reduced ejection fraction, and statins are part of its prevention."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory counter-regulation: IL-10 opposes the chronic myocardial inflammation (IL-6, TNF and IL-1 already mapped) of heart failure, and the imbalance toward pro-inflammatory signalling contributes to the adverse remodelling."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine cardiometabolism: leptin, with adiponectin (already mapped), links the adipose tissue of obesity (already mapped) to the myocardial metabolism and inflammation of heart failure, especially the HFpEF phenotype."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Cardiac M2 macrophages: IL-4 polarises the cardiac macrophages toward a reparative M2 phenotype (IL-10 already mapped), part of the myocardial inflammation and remodelling (TGF-β already mapped) of heart failure."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Prostaglandins and fluid: renal prostaglandins maintain perfusion during RAAS blockade (angiotensin already mapped), and NSAIDs that block them cause fluid retention that precipitates and worsens heart failure."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial dysfunction: the angiopoietin-Tie2 axis reflects the endothelial dysfunction of heart failure (VEGF and endothelin already mapped), the congestion-driven endothelial activation contributing to the systemic and pulmonary vascular changes."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Fibrotic remodelling: IL-13, with IL-4 (already mapped), drives the M2 macrophage and profibrotic (TGF-β already mapped) response in the myocardial remodelling of heart failure."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the adipokine and inflammatory milieu of the metabolic comorbidity and cachexia (myostatin already mapped) of heart failure."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Tissue hypoxia: the low-output failing heart impairs oxygen delivery, causing the tissue hypoxia (HIF already mapped) and exertional limitation, and supplemental oxygen is used in acute decompensation."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetic HFpEF: type 2 diabetes (insulin already mapped) causes the diabetic cardiomyopathy and HFpEF, the SGLT2 (already mapped) inhibitors benefiting both conditions."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Hyponatraemia and congestion: the dilutional hyponatraemia (vasopressin already mapped) is a poor-prognosis marker in heart failure, and the dietary sodium restriction manages the fluid congestion."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Cardiac inflammation: the cardiac macrophages (the inflammation, TNF, IL-6 and NLRP3 already mapped) drive the adverse remodelling and the fibrosis (TGF-β already mapped) of heart failure."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate cardiac interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the cardiomyocyte (already mapped) stress and DNA damage, drives the sterile inflammation of the failing myocardium."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 cardiac inflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune-mediated inflammation (macrophages already mapped) of the adverse remodelling of heart failure."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the cardiac inflammation of heart failure."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune-inflammatory remodelling of heart failure (and the eosinophilic myocarditis)."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the cardiac inflammation and fibrosis of heart failure."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the cardiac inflammation of heart failure."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines driving the cardiac inflammation and fibroblast (already mapped) activation of heart failure."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Cardiac mast cells: the mast cells accumulate in the failing myocardium and, via the chymase and mediators, promote the fibrosis (TGF-β and periostin already mapped) and remodelling of heart failure."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Cardiac antigen presentation: the dendritic cells present the cardiac self-antigen to the T cells (already mapped) shaping the adaptive-immune contribution to the cardiac remodelling of heart failure."
---

# Heart Failure

## Overview

Heart failure (HF) is a **clinical syndrome** in which the heart cannot pump sufficient blood to meet the body's metabolic demands, or can only do so at the cost of elevated filling pressures. It represents the final common pathway of most cardiac diseases and is a major global health burden: approximately **64 million people** worldwide live with HF, with a 5-year mortality (~50%) comparable to many malignancies [^ponikowski-2016-esc-hf].

HF is classified by **left ventricular ejection fraction (LVEF)**:
- **HFrEF** (Heart Failure with Reduced EF, EF <40%): "systolic" heart failure; cardiomyocyte loss and contractile dysfunction; GDMT most evidence-based here
- **HFmrEF** (Mildly Reduced EF, 40–49%): intermediate phenotype; overlapping features; GDMT may benefit
- **HFpEF** (Preserved EF, ≥50%): "diastolic" heart failure; impaired ventricular relaxation and compliance; major unmet treatment need (heterogeneous syndrome)

**Leading etiologies:**
- Ischemic heart disease (CAD, prior MI) — most common in developed world
- Hypertension — LVH → diastolic dysfunction → HFpEF; also causes HFrEF
- Dilated cardiomyopathy — idiopathic, familial (TTN mutations), viral, alcohol, chemotherapy (anthracyclines, trastuzumab)
- Valvular heart disease — mitral regurgitation (volume overload), aortic stenosis (pressure overload)
- Arrhythmias — tachycardia-induced cardiomyopathy

## Structure

### Cardiac Remodeling

The failing heart undergoes **maladaptive structural remodeling** driven by neurohumoral overactivation:

**Hypertrophy patterns:**
- **Concentric hypertrophy** (pressure overload — hypertension, AS): wall thickening with normal/reduced cavity, increased wall:cavity ratio; → diastolic dysfunction
- **Eccentric hypertrophy** (volume overload — MR, AI; post-MI): cavity dilation with proportional wall thinning; → systolic dysfunction; myocyte elongation (series sarcomere addition)

**Cellular changes in failing cardiomyocytes:**
- Calcium handling: ↓ SERCA2a expression/activity → impaired SR Ca²⁺ reuptake → elevated diastolic Ca²⁺ → impaired relaxation → diastolic dysfunction; depleted SR Ca²⁺ → reduced systolic Ca²⁺ transient → reduced contractility
- Sarcomeric changes: fetal gene program reactivation (β-MHC ↑, α-MHC ↓; ANP, BNP re-expression); reduced actomyosin ATPase activity → reduced contractile velocity
- Mitochondrial dysfunction: impaired fatty acid oxidation (primary fuel) → shift to glucose; reduced ATP production → energetic deficit
- Cardiomyocyte apoptosis: via mitochondrial (cytochrome c release → caspase-9) and death receptor (TNFR1 → caspase-8) pathways

**Extracellular matrix remodeling:**
- Cardiac fibrosis: aldosterone → cardiac fibroblast activation → collagen I/III deposition → increased passive stiffness → diastolic dysfunction; reduced electrical coupling → arrhythmia risk
- MMP/TIMP imbalance: early: MMP2/9 upregulation → collagen degradation → dilation; chronic: TIMP upregulation → fibrosis

### Neurohormonal Activation

The neurohormonal response to reduced CO is **initially compensatory but ultimately maladaptive**:

| System | Compensatory effect | Maladaptive effect |
|:---|:---|:---|
| **SNS** (norepinephrine) | ↑ HR, ↑ contractility, vasoconstriction | Tachyarrhythmias; cardiomyocyte toxicity; β-receptor downregulation; ↑ myocardial O₂ demand |
| **RAAS** (Ang II/aldosterone) | Na+ and water retention (volume) | Cardiac fibrosis; hypertrophy; vasoconstriction ↑ afterload; renal dysfunction |
| **ADH (vasopressin)** | Water retention | Hyponatremia; further volume overload |
| **BNP/ANP** | Natriuresis, vasodilation, anti-fibrotic (compensatory) | Progressively overwhelmed in severe HF; used as biomarker |

## Function

### Pathophysiology of Symptoms

HF symptoms arise from two fundamental abnormalities:

**Backward failure (congestion):**
- Left-sided: elevated left ventricular filling pressure → pulmonary venous hypertension → pulmonary capillary wedge pressure ↑ → pulmonary edema → dyspnea, orthopnea, PND
- Right-sided: elevated RV filling pressure → systemic venous hypertension → JVD, hepatomegaly, ascites, peripheral edema

**Forward failure (reduced output):**
- Reduced CO → poor peripheral perfusion → fatigue, exercise intolerance, muscle wasting (cardiac cachexia), reduced renal perfusion → cardiorenal syndrome, prerenal azotemia

### Frank-Starling Mechanism (Blunted)

Normal hearts increase stroke volume with increasing preload (Starling curve). The failing heart has a **depressed, flattened Starling curve**: increases in preload yield minimal SV improvement but cause significant pulmonary and systemic congestion. This is the physiological basis for the therapeutic approach: reduce preload (diuretics, venodilators) and afterload (vasodilators, RAAS blockade) while supporting contractility.

### Exercise Physiology in HF

- Reduced peak VO₂ (maximal oxygen uptake) — primary determinant of functional capacity and prognosis in HF
- Blunted chronotropic response (reduced HR reserve) — beta-receptor downregulation; blunted SNS reserve
- Peripheral factors: skeletal muscle atrophy (sarcopenia), reduced capillary density, mitochondrial dysfunction → impaired O₂ extraction

## Connections

- `part-of` → **[Heart](../../06-organ/heart/README.md)** — heart failure is the systemic consequence of impaired cardiac pump function
- `modulated-by` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — drives vasoconstriction, volume expansion, cardiac fibrosis, and hypertrophy in HF; ACE-I/ARBs block this arm of GDMT
- `modulated-by` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — cardiac fibrosis, sodium retention, and potassium wasting; MRAs (spironolactone/eplerenone) reduce mortality in HFrEF
- `contains` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — the primary failing cell type; cardiomyocyte loss, hypertrophy, and calcium handling dysfunction are the central cellular mechanisms of HFrEF
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — elevated LDL-C from PCSK9 GOF mutations accelerates coronary atherosclerosis → MI → ischemic cardiomyopathy and heart failure; PCSK9 inhibitors reduce MI risk in high-risk CVD patients; PCSK9 may also have direct myocardial effects via apoE and apoB receptor pathways.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — DAPA-HF (dapagliflozin, HFrEF): 25% reduction in worsening HF + CV death in T2D and non-T2D; EMPEROR-Reduced (empagliflozin): 25% reduction; SGLT2 inhibitors are the fourth pillar of GDMT, reducing HHF and CV death independent of diabetes status.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — elevated FGF23 in CKD activates cardiac FGFR4 independent of αKlotho → HDAC4 nuclear translocation → cardiac hypertrophic gene program → LVH and HF; FGF23 is an independent predictor of incident heart failure and cardiovascular death in CKD and the general population.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — BNP is released by ventricular myocytes under wall stress → NPR-A → cGMP → natriuresis and vasodilation; BNP/NT-proBNP diagnose and prognosticate HF; sacubitril (neprilysin inhibitor in ARNI) raises ANP/BNP → PARADIGM-HF: 20% RRR vs. ACE-I in HFrEF.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 secreted by cardiac macrophages activates cardiac fibroblasts → collagen synthesis → myocardial fibrosis and diastolic dysfunction; serum galectin-3 ≥17.8 ng/mL is an FDA-approved HF biomarker predicting mortality; galectin-3 predicts incident HFpEF.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Ventricular Cx43 is down-regulated and lateralized in heart failure → electrical uncoupling → slow conduction → re-entrant VT substrate → sudden cardiac death; Cx43 dephosphorylation (loss of pSer368) marks gap junction dysfunction and correlates with arrhythmia risk.
- `connects-to` → **[Phospholamban](../../03-molecular/phospholamban/README.md)** — PLN hyperinhibition of SERCA2a is the central Ca²⁺ handling defect in HFrEF: elevated PP1/PP2A → reduced PLN-pSer16 → constitutive SERCA2a inhibition → slow Ca²⁺ reuptake → impaired relaxation and contractility; AAV1.SERCA2a gene therapy (CUPID) aimed to restore Ca²⁺ cycling.
- `connects-to` → **[HCN4](../../03-molecular/hcn4/README.md)** — Heart failure with persistent tachycardia: ivabradine (HCN4 I_f blocker) reduces HR without negative inotropy; SHIFT trial: 18% reduction in HF hospitalization in HFrEF with HR >70 bpm; European guidelines recommend ivabradine as adjunct therapy in HFrEF with HR >70 bpm.
- `connects-to` → **[RyR2](../../03-molecular/ryr2/README.md)** — CaMKII hyperactivation in HFrEF hyperphosphorylates RyR2 Ser2814 → diastolic Ca²⁺ leak → SR Ca²⁺ depletion + delayed afterdepolarizations → ventricular arrhythmia; diastolic RyR2 Ca²⁺ leak is a core mechanism linking Ca²⁺ cycling dysfunction to sudden cardiac death in HF.
- `connects-to` → **[Troponin Complex](../../03-molecular/troponin-complex/README.md)** — High-sensitivity cTn is elevated in HF proportional to ventricular remodeling severity; persistent cTn elevation in HFrEF reflects ongoing cardiomyocyte injury and predicts mortality; cTn elevation in acute decompensated HF and myocarditis reflects inflammation-driven release.
- `connects-to` → **[NCX1](../../03-molecular/ncx1/README.md)** — NCX1 is upregulated in failing human ventricle → increased Ca²⁺ extrusion → further SR Ca²⁺ depletion (additive to SERCA2a downregulation) → reduced contractility; inward INCX during repolarization prolongs action potential → delayed afterdepolarizations → arrhythmia in HFrEF.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Heart failure and the kidney fail together as the cardiorenal syndrome: a failing heart underperfuses the kidney while congestion raises venous pressure, so renal function falls, fluid is retained, and diuretic resistance and worsening azotemia dominate management.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Hypertension is a leading cause of heart failure: chronic pressure overload drives left ventricular hypertrophy that stiffens into diastolic failure (HFpEF) or dilates into systolic failure, so blood-pressure control is the biggest preventable HF risk factor.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Heart failure is the common endpoint of cardiovascular disease: ischemia, valve disease, hypertension and arrhythmia all converge on a heart that can no longer meet the body's demands, making it the shared final pathway of the failing cardiovascular system.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Atherosclerosis is the leading road to heart failure: coronary disease and myocardial infarction kill heart muscle, and the scarred, weakened ventricle that remains can no longer pump adequately—so ischemic cardiomyopathy is the commonest cause of HF.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Heart failure is in large part a fibrotic disease: stressed myocardium replaces lost muscle with stiff collagen scar, which impairs both contraction and relaxation—so cardiac fibrosis underlies the remodeling that drives both reduced and preserved ejection fraction HF.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Heart failure floods the lungs: when the failing left ventricle can't keep up, pressure backs up into the pulmonary circulation, leaking fluid into alveoli—so breathlessness and pulmonary edema are the cardinal symptoms that bring patients to hospital.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency is common and treatable in heart failure: even without anemia, low iron impairs cardiac and muscle energetics and worsens symptoms, so intravenous iron is now recommended to improve quality of life and cut hospitalizations.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity is a major driver of heart failure, especially HFpEF: excess weight raises filling pressures, inflames and stiffens the heart, and the obese-HFpEF phenotype is now a target for GLP-1 and SGLT2 therapies that aid both weight and the heart.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Heart failure activates the sympathetic nervous system: norepinephrine initially props up output but chronically harms the failing heart, driving remodeling and arrhythmia—which is why beta-blockers that blunt it are a cornerstone of treatment.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Heart failure is a calcium-cycling failure: the sick cardiomyocyte can't pump calcium in and out fast enough (downregulated SERCA), so each beat is weaker and relaxation incomplete—the molecular basis of the failing squeeze.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — The failing heart is starved of ATP: damaged mitochondria can't supply enough energy for the constant work of pumping, so the heart runs like an engine low on fuel—an energy deficit that worsens the contractile failure.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Heart failure is driven by cardiac macrophages: after injury they shift from repair to chronic inflammation, fueling the fibrosis and adverse remodeling that stiffen and enlarge the failing heart.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Heart failure is a disease of sodium and water overload: the failing heart triggers hormones that make the kidney retain salt, causing the congestion and edema—while dilutional hyponatremia, paradoxically, marks the most severe disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Heart failure backs up into the liver: a congested, failing right heart raises venous pressure that engorges the liver and, over time, scars it into cardiac cirrhosis, so abnormal liver tests can flag worsening heart failure.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibroblasts stiffen the failing heart: after injury and under neurohormonal stress they lay down collagen scar between muscle cells, the fibrosis that hardens the ventricle and disrupts its electrical and mechanical function.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging stages heart failure: chest X-ray photons show an enlarged heart and congested lungs, while cardiac MRI and nuclear scans gauge function and viability to guide treatment.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Failing small vessels drive HFpEF: coronary microvascular endothelial dysfunction is now seen as central to heart failure with preserved ejection fraction, inflaming and stiffening the heart from its tiniest vessels.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Potassium is a constant worry in heart failure: the disease and its drugs swing it in both directions, and either too-high or too-low potassium triggers the arrhythmias behind sudden cardiac death.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads the failing heart muscle: it shows swollen, dysfunctional mitochondria and disarrayed sarcomeres, and reveals the tangled amyloid fibrils of cardiac amyloidosis, an increasingly recognized cause of stiff-heart failure.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium quietly slips away in heart failure: loop and thiazide diuretics flush it out, and the resulting deficiency primes the heart for arrhythmias and amplifies digoxin toxicity, so it is watched alongside potassium.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Anemia haunts heart failure: low red-cell counts, driven by kidney dysfunction and iron deficiency, force the failing heart to work harder for less oxygen delivery, worsening symptoms and prognosis in the cardiorenal-anemia syndrome.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid sets the heart's tempo: hyperthyroidism drives high-output failure and atrial fibrillation while hypothyroidism weakens contraction and slows the rate, so thyroid function is checked in new or worsening heart failure — and amiodarone can derange it.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Advanced heart failure wastes the body: cardiac cachexia and a congested, protein-losing gut drop albumin, and the low level both worsens the edema through reduced oncotic pressure and marks a grim prognosis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Heart failure floods the body with water-holding hormone: the failing circulation triggers vasopressin release, which retains free water and dilutes the blood's sodium into the hyponatremia that flags severe disease and is targeted by vaptan drugs.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both diagnose and cause heart failure: BNP and NT-proBNP are read by immunoassay to confirm and grade it, while autoantibody-driven myocarditis — including the immune-checkpoint kind — is a reversible cause worth catching early.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The failing heart over-revs its nerves: baroreceptor signaling drives a maladaptive sympathetic surge from autonomic neurons that strains the myocardium further — the vicious cycle beta-blockers interrupt to improve survival.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Heart failure reaches the bedroom and the delivery room: erectile dysfunction is common from the disease and its drugs, while pregnancy's volume load is hazardous in cardiomyopathy and can itself trigger peripartum heart failure.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — The failing heart triggers a damaging feedback loop: falling output makes the kidney release renin, firing up the renin-angiotensin-aldosterone system that retains salt and water and remodels the heart — the very axis ACE inhibitors and ARBs block.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Heart and kidney fail together: in cardiorenal syndrome poor cardiac output and venous congestion injure the kidneys while fluid overload worsens the heart, a vicious cycle that complicates diuretic dosing in advanced disease.
- `connects-to` → **[Stroke](../stroke/README.md)** — A weak heart throws clots to the brain: low ejection fraction and the atrial fibrillation that often accompanies heart failure let thrombi form in the stagnant chambers and embolize, raising stroke risk and prompting anticoagulation.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes weakens the heart directly: beyond accelerating coronary disease, high glucose and insulin resistance cause a diabetic cardiomyopathy that stiffens and fails the muscle — part of why the SGLT2 drugs born for diabetes now treat heart failure itself.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — A vasodilator the drugs deliberately spare: ACE inhibitors and the neprilysin component of sacubitril raise bradykinin, easing afterload and remodeling in heart failure — the same accumulation that causes their hallmark cough and angioedema.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — The failing heart outgrows its blood supply: inadequate VEGF-driven angiogenesis leaves the hypertrophied and HFpEF myocardium with coronary microvascular rarefaction, starving the muscle of the capillaries it needs.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation drives the remodeling: NF-κB activation in the stressed myocardium switches on the cytokines and hypertrophic genes that progressively scar and dilate the failing heart, a target of interest beyond the standard neurohormonal blockade.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Sluggish circulation favors clots: the low cardiac output, venous congestion and reduced mobility of heart failure create a prothrombotic state that raises the risk of deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Anemia and heart failure feed each other: chronic inflammation, kidney dysfunction and iron deficiency make anemia common in heart failure, worsening symptoms and prognosis in the cardiorenal-anemia syndrome.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Left-sided failure backs pressure into the lungs: chronically raised left-atrial pressure transmits to the pulmonary circulation, causing the post-capillary (group 2) pulmonary hypertension that complicates and worsens heart failure.
- `connects-to` → **[Gout](../gout/README.md)** — Diuretics and low output raise uric acid: loop diuretics and reduced renal perfusion in heart failure cut urate excretion, so hyperuricemia and gout flares are common, and high uric acid itself tracks with worse prognosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — It weighs heavily on mood: depression is common in heart failure, driven by the limits of breathlessness and fatigue and by shared inflammatory pathways, and it independently predicts hospitalization and death.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — A failing pump starves the brain: chronically low cardiac output and recurrent hypoperfusion reduce cerebral blood flow, and heart failure is an independent risk factor for vascular and Alzheimer-type cognitive decline.
- `connects-to` → **[NASH](../nash/README.md)** — Backed-up venous pressure congests the liver: right-sided heart failure engorges the liver, and the shared metabolic syndrome links cardiac disease with fatty-liver disease, together driving congestive hepatopathy and fibrosis.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Congestion and frailty invite severe infection: pulmonary congestion predisposes to pneumonia, and the debilitated, often hospitalized heart-failure patient is vulnerable to infections that can escalate to sepsis.
- `connects-to` → **[Iron-Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Iron deficiency is rife in failing hearts: both absolute and functional iron deficiency are very common in heart failure, worsening symptoms and exercise capacity, so intravenous iron is a recognised therapy.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — A congested gut starves the body: venous congestion and low output in heart failure cause bowel-wall oedema with malabsorption and a leaky gut, driving the cardiac cachexia that marks advanced disease.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Breathlessness and a fragile prognosis breed worry: the dyspnoea, fear of decompensation and burdensome regimen of heart failure foster chronic anxiety alongside its well-recognised depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It floods the lungs: a failing left heart backs pressure into the pulmonary circulation, causing congestion and oedema with orthopnoea, paroxysmal nocturnal dyspnoea, pleural effusions and Cheyne-Stokes breathing.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Heart and kidney fail together: in cardiorenal syndrome poor cardiac output and venous congestion impair renal function, while fluid retention worsens the heart, and diuretic resistance complicates both.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones drive its decline: neurohormonal activation of the renin-angiotensin-aldosterone and sympathetic systems propels heart failure, so blocking them with ACE inhibitors, MRAs and beta-blockers is the core of therapy.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It wastes the muscles: advanced heart failure causes cardiac cachexia with skeletal-muscle wasting and sarcopenia that reduce exercise capacity and worsen prognosis.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Low output and overdrive disturb the brain: chronic cerebral hypoperfusion impairs cognition, sympathetic overactivation drives progression, and Cheyne-Stokes breathing fragments sleep.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Inflammation feeds its decline: raised inflammatory cytokines such as TNF and IL-6 contribute to cardiac cachexia and the progression of heart failure.
- `connects-to` → **[ACE inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — A cornerstone of treatment: ACE inhibitors reduce afterload and block harmful neurohormonal remodelling, lowering mortality in heart failure with reduced ejection fraction.
- `connects-to` → **[Beta-blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — They reverse the harmful drive: beta-blockers blunt the chronic sympathetic overactivation of heart failure, improving survival despite initially reducing contractility.
- `connects-to` → **[Loop Diuretics](../../../03-medicine/01-modern/04-cardio/loop-diuretics/README.md)** — They relieve the congestion: loop diuretics like furosemide remove the salt and water overload that causes the breathlessness and oedema of decompensated heart failure.
- `connects-to` → **[ARBs](../../../03-medicine/01-modern/04-cardio/arbs/README.md)** — RAS blockade when ACE fails: angiotensin-receptor blockers replace ACE inhibitors in patients who cannot tolerate their cough, and combined with neprilysin inhibition as ARNI they are a cornerstone of heart-failure therapy.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — The failing muscle remodels: heart failure reflects diseased myocardium — dilated and thin in systolic failure, stiff and hypertrophied in HFpEF — where cardiomyocyte loss and interstitial fibrosis progressively impair contraction and filling.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — It is an electrical disease too: heart failure disrupts conduction, causing ventricular arrhythmias and sudden death that warrant ICDs, while left-bundle delay creates dyssynchrony corrected by cardiac resynchronisation therapy.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — It floods the air sacs: left heart failure raises pulmonary venous pressure until fluid leaks into the alveoli, causing the pulmonary oedema, orthopnoea and breathlessness of acute decompensation.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Cardiorenal syndrome strains the filter: falling cardiac output and venous congestion reduce glomerular perfusion and filtration, the kidney dysfunction that complicates heart failure and limits diuresis.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — A treatable cause hides in the marrow: AL (light-chain) amyloidosis from a plasma-cell clone deposits in the myocardium as a restrictive cardiomyopathy, so unexplained heart failure with thick walls warrants a myeloma workup.
- `connects-to` → **[COPD](../copd/README.md)** — Cor pulmonale: COPD raises pulmonary vascular resistance and right-heart afterload, driving right-sided heart failure, and the two diseases share smoking and systemic inflammation.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Afterload and stiffness: stiffening of the arterial wall raises the load the heart pumps against and is central to heart failure with preserved ejection fraction, coupling vascular ageing to cardiac failure.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Marrow links to the failing heart: heart failure drives a cardio-renal-anaemia syndrome, and age-related clonal haematopoiesis (CHIP) from the bone marrow fuels inflammation that accelerates its progression.
- `connects-to` → **[Trypanosoma cruzi](../../../02-pathogen/04-parasites/trypanosoma-cruzi/README.md)** — Chagas cardiomyopathy: chronic Trypanosoma cruzi infection slowly destroys the myocardium and conduction system, making Chagas disease a leading cause of heart failure and sudden death in Latin America.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Cardio-oncology: anthracyclines and HER2-targeted trastuzumab used for breast cancer are cardiotoxic, causing a treatment-related cardiomyopathy and heart failure that is a major survivorship concern.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — Valvular heart failure: diseased heart valves lined by endocardium—from calcific aortic stenosis, regurgitation or rheumatic disease—impose chronic pressure or volume overload that drives the ventricle into failure.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Maladaptive vasoconstriction: endothelin-1 drives vasoconstriction and cardiac fibrosis in heart failure, a neurohormonal axis that worsens afterload and remodelling.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Cardiac cachexia: TNF-α and chronic inflammation drive the muscle and fat wasting of cardiac cachexia, a marker of advanced, poor-prognosis heart failure.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — The adiponectin paradox: adiponectin rises in advanced heart failure and, counter to its metabolic benefits, high levels track with disease severity and worse outcomes.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammatory prognosis: circulating IL-6 is elevated in heart failure and predicts severity and mortality, reflecting the chronic inflammation that contributes to myocardial remodelling and cachexia.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Sterile inflammation: NLRP3 inflammasome activation in cardiac macrophages and fibroblasts drives IL-1β release after injury, promoting adverse remodelling and fibrosis in heart failure — an emerging therapeutic target.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Hypertrophic growth: chronic mTOR signalling drives pathological cardiomyocyte hypertrophy and maladaptive remodelling, while its modulation is studied to limit progression to heart failure.
- `connects-to` → **[SERCA2a](../../03-molecular/serca2a/README.md)** — SERCA2a expression and activity fall in the failing heart, slowing sarcoplasmic-reticulum calcium reuptake to produce the depressed contractility and impaired relaxation central to both systolic and diastolic heart failure—a long-standing gene-therapy target.
- `connects-to` → **[β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — Chronic sympathetic overdrive in heart failure downregulates and uncouples β1-adrenergic receptors, the maladaptive desensitization that beta-blockers reverse to produce one of the few mortality benefits in the disease.
- `connects-to` → **[Myostatin](../../03-molecular/myostatin/README.md)** — The failing heart releases myostatin that, together with systemic inflammation, drives the skeletal-muscle wasting and cardiac cachexia marking advanced heart failure and independently predicting poor survival.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Inflammation-driven hepcidin elevation causes functional iron deficiency in heart failure, impairing exercise capacity independent of anemia and reversed by intravenous iron, which improves symptoms and reduces admissions.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Impaired nitric-oxide-cGMP signaling drives the myocardial stiffness and microvascular dysfunction of heart failure, especially HFpEF, the pathway targeted by the soluble-guanylate-cyclase stimulator vericiguat.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — GLP-1 receptor agonists (semaglutide) improve symptoms and exercise capacity in the obesity phenotype of heart failure with preserved ejection fraction, linking the metabolic axis to a major and growing HF subtype.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — The calcineurin-NFAT pathway transduces sustained cardiomyocyte calcium signals into the maladaptive hypertrophic gene program that drives the ventricular remodeling of heart failure.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β drives the cardiac-fibroblast activation and interstitial fibrosis (fibrosis and periostin already mapped) that stiffen the failing ventricle, central to heart failure with preserved ejection fraction.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Neurohormonal and mechanical stress signal through the MAPK-ERK1/2 cascade to drive the hypertrophic growth of cardiomyocytes during the remodeling of heart failure.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling governs cardiomyocyte growth—physiological when IGF-driven, but its sustained pathological activation (with mTOR mapped) contributes to the maladaptive hypertrophy of heart failure.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Oxidative stress overwhelms NRF2 antioxidant defenses in the failing myocardium, contributing to the cardiomyocyte injury and adverse remodeling of heart failure.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3-mediated apoptosis of cardiomyocytes progressively depletes contractile units, a cell-death mechanism driving the decline of the failing heart.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of damage-associated molecular patterns from injured myocardium drives the sterile inflammation that contributes to adverse remodeling in heart failure.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT signaling (IL-6 already mapped) participates in the inflammatory and hypertrophic remodeling of the failing heart, with STAT3 also mediating cardioprotection.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α responses to the hypoxia of the failing heart drive metabolic and angiogenic adaptations that are initially protective but maladaptive when sustained.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the cardiac fibrosis and adverse ventricular remodeling central to the progression of heart failure.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling mediates cardiomyocyte hypertrophy and the inflammatory remodeling of the failing myocardium in heart failure.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Mitochondrial DNA released by stressed cardiomyocytes engages cGAS-STING, driving the sterile inflammation that contributes to adverse remodeling in heart failure.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate cardiomyocyte autophagy, atrophy, and oxidative-stress defense, processes that shape adverse remodeling in heart failure.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates pathological cardiac hypertrophy and fibrosis, acting as a brake whose dysregulation contributes to heart failure remodeling.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling promotes cardiomyocyte apoptosis and the inflammatory remodeling of the failing myocardium in heart failure.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the balance between adaptive and maladaptive cardiac hypertrophy in heart failure.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released during myocardial stress amplify the inflammatory cardiac remodeling of heart failure.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic-lymphocyte perforin activity contributes to the immune-mediated myocardial injury in inflammatory heart failure.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling governs the cardiomyocyte energy homeostasis whose failure drives the metabolic remodeling of heart failure.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the cardiomyocyte survival and protein-quality control in the failing heart.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the cardiac hypertrophic and fibrotic remodeling of heart failure.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte recruitment contributes to the myocardial inflammation and adverse remodeling of heart failure.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic reprogramming of the failing myocardium in heart failure.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation contributes to the myocardial inflammation and adverse remodeling of heart failure.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the cardiac repair, inflammatory-cell recruitment, and remodeling of heart failure.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the cardiac inflammation and fibrosis of heart failure.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the cardiac remodeling gene programs of heart failure.
- `connects-to` → **[Thyroid hormones](../../03-molecular/thyroid-hormones/README.md)** — Thyroid cardiomyopathy: both hyper- and hypothyroidism impair cardiac output, and the low-T3 syndrome of advanced heart failure is a marker of poor prognosis, making thyroid-hormone status a modifiable contributor to the failing heart.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Diabetic cardiomyopathy: insulin resistance and hyperglycaemia produce a distinct diabetic cardiomyopathy and worsen outcomes in heart failure, the bidirectional metabolic link that underlies the cardiac benefit of SGLT2 inhibitors (already mapped).
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress and urate: xanthine oxidase generates reactive oxygen species and uric acid in the failing heart, and elevated serum urate is an independent marker of severity, reflecting the oxidative burden of impaired myocardial energetics.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia of heart failure: anaemia is common in heart failure from iron deficiency (already mapped), inflammation and renal dysfunction, and low haemoglobin worsens symptoms, exercise capacity and prognosis.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences and peripartum disease: estrogen influences the sex differences in heart failure, with women predominating in HFpEF, and its abrupt fall postpartum is implicated in peripartum cardiomyopathy.
- `connects-to` → **[COVID-19](../covid-19-disease/README.md)** — Viral cardiac injury: COVID-19 can cause myocarditis and precipitate or worsen heart failure (troponin already mapped), one of several viral illnesses that acutely stress the failing or vulnerable myocardium.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Ischaemic lipids: the atherogenic cholesterol (PCSK9 already mapped) driving coronary disease underlies ischaemic cardiomyopathy, the commonest cause of heart failure with reduced ejection fraction, and statins are part of its prevention.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory counter-regulation: IL-10 opposes the chronic myocardial inflammation (IL-6, TNF and IL-1 already mapped) of heart failure, and the imbalance toward pro-inflammatory signalling contributes to the adverse remodelling.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine cardiometabolism: leptin, with adiponectin (already mapped), links the adipose tissue of obesity (already mapped) to the myocardial metabolism and inflammation of heart failure, especially the HFpEF phenotype.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Cardiac M2 macrophages: IL-4 polarises the cardiac macrophages toward a reparative M2 phenotype (IL-10 already mapped), part of the myocardial inflammation and remodelling (TGF-β already mapped) of heart failure.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Prostaglandins and fluid: renal prostaglandins maintain perfusion during RAAS blockade (angiotensin already mapped), and NSAIDs that block them cause fluid retention that precipitates and worsens heart failure.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Endothelial dysfunction: the angiopoietin-Tie2 axis reflects the endothelial dysfunction of heart failure (VEGF and endothelin already mapped), the congestion-driven endothelial activation contributing to the systemic and pulmonary vascular changes.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Fibrotic remodelling: IL-13, with IL-4 (already mapped), drives the M2 macrophage and profibrotic (TGF-β already mapped) response in the myocardial remodelling of heart failure.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the adipokine and inflammatory milieu of the metabolic comorbidity and cachexia (myostatin already mapped) of heart failure.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Tissue hypoxia: the low-output failing heart impairs oxygen delivery, causing the tissue hypoxia (HIF already mapped) and exertional limitation, and supplemental oxygen is used in acute decompensation.
- `connects-to` → **[Type 2 diabetes](../type-2-diabetes/README.md)** — Diabetic HFpEF: type 2 diabetes (insulin already mapped) causes the diabetic cardiomyopathy and HFpEF, the SGLT2 (already mapped) inhibitors benefiting both conditions.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Hyponatraemia and congestion: the dilutional hyponatraemia (vasopressin already mapped) is a poor-prognosis marker in heart failure, and the dietary sodium restriction manages the fluid congestion.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Cardiac inflammation: the cardiac macrophages (the inflammation, TNF, IL-6 and NLRP3 already mapped) drive the adverse remodelling and the fibrosis (TGF-β already mapped) of heart failure.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate cardiac interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the cardiomyocyte (already mapped) stress and DNA damage, drives the sterile inflammation of the failing myocardium.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 cardiac inflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune-mediated inflammation (macrophages already mapped) of the adverse remodelling of heart failure.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the cardiac inflammation of heart failure.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune-inflammatory remodelling of heart failure (and the eosinophilic myocarditis).
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the cardiac inflammation and fibrosis of heart failure.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the cardiac inflammation of heart failure.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines driving the cardiac inflammation and fibroblast (already mapped) activation of heart failure.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Cardiac mast cells: the mast cells accumulate in the failing myocardium and, via the chymase and mediators, promote the fibrosis (TGF-β and periostin already mapped) and remodelling of heart failure.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Cardiac antigen presentation: the dendritic cells present the cardiac self-antigen to the T cells (already mapped) shaping the adaptive-immune contribution to the cardiac remodelling of heart failure.

## Pathology

### Guideline-Directed Medical Therapy (GDMT) for HFrEF

Four pillars of GDMT reduce mortality in HFrEF (each independently significant):

| Drug class | Example | Mortality benefit | Mechanism |
|:---|:---|:---|:---|
| **ACE-I/ARB** | Enalapril, Losartan | 16–23% RRR | RAAS blockade → reduced afterload, anti-fibrotic, anti-hypertrophic |
| **Beta-blocker** | Carvedilol, Metoprolol succinate, Bisoprolol | 34% RRR | Reduces SNS toxicity; anti-arrhythmic; allows β-receptor re-sensitization; reduces HR |
| **MRA** | Spironolactone, Eplerenone | 25–30% RRR | Aldosterone blockade → reduced cardiac fibrosis, K+/Mg2+ preservation, reduced arrhythmia |
| **ARNI** | Sacubitril-valsartan | 20% additional RRR vs. ACE-I | Neprilysin inhibition → BNP/ANP ↑ → natriuresis + vasodilation + anti-fibrotic; supersedes ACE-I in HFrEF [^mcmurray-2014-paradigm-hf] |
| **SGLT2 inhibitor** | Dapagliflozin, Empagliflozin | 25% RRR in DAPA-HF/EMPEROR-R | Volume reduction, RAAS modulation, anti-fibrotic, improved mitochondrial function; the fourth pillar |

### HFpEF: An Unmet Need

HFpEF (EF ≥50%) accounts for ~50% of all HF and has limited evidence-based therapy:
- **EMPEROR-Preserved (Empagliflozin)** and **DELIVER (Dapagliflozin)**: SGLT2i reduce HF hospitalizations in HFpEF — the first drug class with clear benefit
- Diuretics for symptom relief (decongestion); no mortality benefit demonstrated for any drug historically
- Pathophysiology: impaired myocardial relaxation, increased passive stiffness, inadequate cardiac reserve; multiple phenotypes (obesity-related, atrial fibrillation, CKD, hypertensive)

### Acute Decompensated Heart Failure (ADHF)

Acute presentation with acute-on-chronic or de novo severe congestion:
- IV diuretics (furosemide) — primary therapy for congestion relief
- Vasodilators (nitroglycerin, nesiritide) — if hypertensive
- Inotropes (dobutamine, milrinone) — for cardiogenic shock/severe low-output; bridge to advanced therapies
- Advanced HF: **LVADs** (left ventricular assist devices) as destination therapy or bridge-to-transplant; cardiac transplantation remains gold standard for refractory HF (limited by donor availability)

[^mcmurray-2014-paradigm-hf]: McMurray JJV et al. Angiotensin-neprilysin inhibition versus enalapril in heart failure. *N Engl J Med.* 2014;371(11):993-1004. [doi:10.1056/NEJMoa1409077](https://doi.org/10.1056/NEJMoa1409077) · [PubMed 25176015](https://pubmed.ncbi.nlm.nih.gov/25176015/)
[^ponikowski-2016-esc-hf]: Ponikowski P et al. 2016 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. *Eur Heart J.* 2016;37(27):2129-2200. [doi:10.1093/eurheartj/ehw128](https://doi.org/10.1093/eurheartj/ehw128) · [PubMed 27206819](https://pubmed.ncbi.nlm.nih.gov/27206819/)
