---
schema: human-scale-entry/v1
id: ckd
name: Chronic Kidney Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Progressive irreversible loss of kidney function (GFR <60 mL/min for >3 months) from diabetes, hypertension, or glomerulonephritis. Staged G1-G5 by GFR; complications include anemia, hyperparathyroidism, and uremia. End-stage managed by dialysis or transplantation."
aliases: ["CKD", "chronic renal failure", "chronic renal insufficiency", "end-stage kidney disease", "ESKD"]
sources:
  - id: kdigo-2012-ckd
    type: clinical-guideline
    cite: "Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int Suppl. 2013;3(1):1-150."
    doi: "10.1038/kisup.2012.73"
    url: "https://doi.org/10.1038/kisup.2012.73"
  - id: levey-2012-ckd-lancet
    type: peer-reviewed
    cite: "Levey AS, Coresh J. Chronic kidney disease. Lancet. 2012;379(9811):165-180."
    doi: "10.1016/S0140-6736(11)60178-5"
    pmid: "21840587"
    url: "https://doi.org/10.1016/S0140-6736(11)60178-5"
  - id: coresh-2007-prevalence
    type: peer-reviewed
    cite: "Coresh J, Selvin E, Stevens LA, et al. Prevalence of chronic kidney disease in the United States. JAMA. 2007;298(17):2038-2047."
    doi: "10.1001/jama.298.17.2038"
    pmid: "17986697"
    url: "https://doi.org/10.1001/jama.298.17.2038"
cross_links:
  - target: 01-human/06-organ/kidney
    relation: targets
    note: "CKD is the progressive structural and functional destruction of renal parenchyma — tubular atrophy, glomerulosclerosis, interstitial fibrosis, and nephron loss; the kidney is the primary target organ."
  - target: 01-human/07-system/renal-system
    relation: part-of
    note: "CKD is the defining pathological state of the renal system; GFR decline progressively impairs all renal functions including solute clearance, acid-base balance, erythropoietin secretion, and vitamin D activation."
  - target: 01-human/03-molecular/erythropoietin
    relation: modulates
    note: "CKD reduces erythropoietin (EPO) synthesis from peritubular fibroblasts as nephron mass declines; anemia of CKD is the direct consequence of EPO deficiency and is treated with recombinant EPO (darbepoetin alfa, epoetin alfa)."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "CKD and hypertension are bidirectionally causal: hypertension is the second leading cause of CKD (via nephrosclerosis); CKD causes hypertension through RAAS activation, sodium retention, and reduced nitric oxide. Controlling BP (target <130/80) slows CKD progression."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "CREDENCE (canagliflozin): 30% reduction in kidney endpoint in T2D + CKD; DAPA-CKD (dapagliflozin): 39% reduction in eGFR decline/dialysis/renal death in CKD with and without T2D; SGLT2 inhibitors slow CKD progression via tubuloglomerular feedback and anti-fibrotic effects."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "FGF23 rises 100-1000× in CKD → suppresses 1α-hydroxylase → reduced calcitriol → secondary hyperparathyroidism and CKD-MBD; very high FGF23 predicts LVH, heart failure, and mortality in dialysis patients independent of traditional risk factors."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "OPN is upregulated in injured renal tubular epithelium → integrin αvβ3 on macrophages → macrophage recruitment and pro-inflammatory activation → tubulointerstitial fibrosis; urinary OPN predicts CKD progression; OPN inhibits calcium oxalate crystal adhesion (stone inhibitor)."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "IgA nephropathy is a leading cause of CKD in young adults; mesangial IgA deposition → complement + CCL2 → tubulointerstitial fibrosis → eGFR decline; 20-40% of IgAN reach ESRD within 20 years; sparsentan (ETA/AT1R dual blocker) and iptacopan are disease-modifying therapies."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Hepcidin is elevated in CKD from reduced renal clearance and chronic inflammation; elevated hepcidin → functional iron deficiency → ESA hyporesponsiveness in CKD anemia; HIF-PHIs (roxadustat, daprodustat) suppress hepcidin via EPO→ERFE→BMP-SMAD inhibition."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "CKD anemia is the overlap of EPO deficiency and ACD mechanisms: reduced EPO from peritubular cell loss + hepcidin elevation from CKD inflammation/reduced clearance → combined functional iron deficiency + erythropoietic failure; IV iron + ESA are first-line for CKD anemia."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "aHUS from complement dysregulation (CFH/CFI mutations) causes progressive CKD; ~50% of untreated aHUS patients reach ESRD within 1 year; eculizumab/ravulizumab reverse TMA and may improve eGFR; renal transplant requires lifelong C5 inhibition in high-risk CFH mutations."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "SCD causes sickle cell nephropathy via medullary sickling (high osmolarity + low pO2 in vasa recta → medullary ischaemia) → hyposthenuria, papillary necrosis, proteinuria; progressive CKD in ~30% HbSS by age 40; ACE inhibitors + hydroxyurea slow progression."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Severe falciparum malaria causes AKI in 4-8% (haemoglobinuria + microvascular obstruction + cytokine storm); cerebral malaria + AKI → high mortality; repeated malaria episodes contribute to CKD burden in endemic populations."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Dialysis patients have elevated sclerostin from impaired renal clearance + uremic Wnt suppression → adynamic bone disease; elevated sclerostin correlates with vascular calcification and mortality in CKD; romosozumab not approved in severe CKD due to CV risk."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "CKD-associated pruritus (formerly uremic pruritus) causes PN-like nodules in dialysis patients; uremic toxins activate μ-opioid and κ-opioid receptors on pruriceptors; difelikefalin (κ-opioid agonist; FDA 2021 for CKD-aP on HD) reduces itch and may prevent PN nodule formation."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes is the leading cause of chronic kidney disease: chronic hyperglycemia damages the glomerular filter (diabetic nephropathy), causing proteinuria and progressive function loss, so diabetic kidney disease drives most dialysis need—SGLT2 inhibitors now slow it."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "CKD and atherosclerosis form a vicious cardiorenal cycle: declining kidney function accelerates vascular calcification and atherosclerosis, so cardiovascular disease—not kidney failure—is the leading cause of death in CKD."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "CKD deranges calcium and bone metabolism (CKD-MBD): failing kidneys can't activate vitamin D or excrete phosphate, lowering calcium and driving secondary hyperparathyroidism and vascular calcification—so calcium, phosphate and PTH are tightly managed in CKD."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "Podocyte loss is a key driver of progressive CKD: these non-dividing cells form the glomerular filter, and when injury (by diabetes, hypertension or FSGS) kills them, the barrier leaks protein and scars, so podocyte depletion predicts irreversible decline."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "CKD often begins in the glomerulus: damage to the filtering tuft causes proteinuria and falling filtration, and surviving glomeruli hyperfilter to compensate—a maladaptive overwork that scars them too, driving the relentless nephron loss of chronic kidney disease."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "CKD and cardiovascular disease are lethally intertwined: most people with CKD die of heart disease, not kidney failure, because uremia, fluid overload and hypertension accelerate atherosclerosis—so the failing kidney is a powerful cardiac risk factor."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Failing kidneys can't dump potassium: as filtration drops, potassium builds up, and hyperkalemia—worsened by the ACE inhibitors and ARBs used to protect the kidney—can stop the heart, so it is among CKD's most urgent, monitored complications."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Heart and kidney failure drive each other (cardiorenal syndrome): CKD's fluid overload, hypertension, and anemia strain the heart, while a failing heart underperfuses the kidney—so the two organs decline together and share treatments like SGLT2 inhibitors."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "CKD cripples vitamin D activation: damaged kidneys can't perform the final hydroxylation to active calcitriol, so calcium absorption falls and parathyroid hormone rises—driving the renal bone disease that defines CKD's mineral and bone disorder."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "CKD progresses through fibrosis: whatever the initial insult, tubulointerstitial fibrosis is the final common pathway that scars nephrons beyond repair, so the degree of fibrosis on biopsy predicts decline better than the original diagnosis."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "CKD throws phosphorus out of balance: failing kidneys can't excrete phosphate, so it rises and—with FGF23, PTH and low vitamin D—drives the bone disease and vascular calcification of CKD-mineral bone disorder."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Angiotensin II accelerates CKD and is the key drug target: it raises glomerular pressure and drives scarring, so ACE inhibitors and ARBs that block it slow progression and reduce proteinuria—the cornerstone of renoprotection."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "CKD and the heart fail together in cardiorenal syndrome: fluid overload, hypertension, anemia and mineral disturbance strain the heart, while heart failure starves the kidneys of flow, so most CKD patients die of cardiovascular causes."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Aldosterone drives the scarring that worsens CKD: beyond raising blood pressure, it promotes fibrosis and inflammation in the kidney, which is why mineralocorticoid blockers like finerenone slow progression on top of ACE inhibitors."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "CKD unleashes bone-dissolving osteoclasts: phosphate retention and secondary hyperparathyroidism overstimulate osteoclasts, the high-turnover renal osteodystrophy that weakens bone and spills calcium and phosphate into vessels."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "CKD turns the blood acidic: failing kidneys cannot excrete the body's daily acid load or regenerate bicarbonate, so hydrogen ions build up into a metabolic acidosis that wastes muscle and bone and is treated with bicarbonate."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "CKD poisons the brain: retained uremic toxins cause the confusion, fatigue, and—in advanced failure—the asterixis and seizures of uremic encephalopathy, symptoms that dialysis is meant to clear."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "CKD wrecks the endothelium: uremic toxins and mineral imbalance injure the vessel-lining cells and calcify artery walls, driving the accelerated atherosclerosis that makes heart disease, not kidney failure, the usual cause of death."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging stages CKD's structure: ultrasound and CT photons show shrunken, scarred kidneys or obstruction, while nuclear scans measure the failing filtration that blood tests only estimate."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "CKD itches relentlessly: retained toxins and mineral imbalance cause uremic pruritus, which patients scratch into prurigo nodularis, one of the most distressing symptoms of advanced kidney failure."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "CKD progresses through fibroblasts: injured kidneys activate myofibroblasts that lay down interstitial scar, the common final pathway by which any kidney disease marches toward failure."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the failing filter: as CKD advances, the glomerular basement membrane thickens and wrinkles while podocyte foot processes flatten and fuse, the ultrastructural decay that lets protein leak and filtration fall."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Failing kidneys leave the blood thin: the diseased kidney makes too little erythropoietin to tell the marrow to build red cells, so anemia is a near-universal companion of CKD, treated with EPO and iron."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "CKD upends magnesium balance: as the kidney loses its power to excrete the mineral, magnesium can build to dangerous levels — especially with magnesium-containing laxatives or antacids — risking weakness and heart-rhythm disturbance."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "CKD drives the parathyroids into overdrive: falling vitamin D and rising phosphate push PTH ever higher (secondary hyperparathyroidism), and the relentless hormone leaches bone into renal osteodystrophy — the core of CKD-mineral-bone disorder."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "The failing kidney lets the blood thin: it makes too little erythropoietin, so hemoglobin falls into the anemia of CKD, treated by replacing the missing hormone with erythropoiesis-stimulating agents."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Uremia makes the platelets sluggish: retained toxins impair platelet function, so even with a normal count CKD patients bruise and bleed more easily, a defect that dialysis and desmopressin can partly correct."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "The kidney loses its grip on salt and water: as CKD advances it cannot excrete a sodium load, so fluid builds up into edema and hypertension, making dietary salt restriction a cornerstone of slowing the disease."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies cause and define much CKD: anti-GBM, ANCA, and lupus autoantibodies attack the glomerulus, and their blood assays pinpoint the immune glomerulonephritides that, untreated, scar the kidney into failure."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Uremia dampens reproduction: it disrupts the hypothalamic-pituitary-gonadal axis into low libido, erectile dysfunction, and infertility, and pregnancy in advanced CKD carries high risk to mother and fetus."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "The failing kidney misreads its own pressure: falling perfusion drives renin and the RAAS into overdrive, raising blood pressure that further scars the kidney — a vicious loop that RAAS blockers are given to interrupt."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages turn injury into scar: they infiltrate the damaged kidney and pour out fibrogenic signals that activate fibroblasts, driving the tubulointerstitial fibrosis that paces the march to kidney failure."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Kidney and urate trap each other: failing kidneys clear less uric acid, raising it into gout, while urate crystals and the drugs for gout can in turn injure the kidney — a two-way burden in CKD."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Fibrosis is the final common path: whatever the initial insult, TGF-β drives tubular cells and fibroblasts to scar the kidney with collagen, the progressive interstitial fibrosis that determines how fast CKD advances."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Failing kidneys imperil the brain's vessels: uremic vasculopathy, hypertension and accelerated atherosclerosis make stroke far more common in CKD, while the bleeding tendency of uremia raises hemorrhagic risk too."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Long-standing damage turns malignant: years of CKD and the acquired cystic disease of dialysis sharply raise the risk of renal cell carcinoma arising in the scarred kidneys."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation scars the kidney forward: NF-κB activation in tubular and immune cells sustains the tubulointerstitial inflammation that, alongside TGF-β, drives the relentless fibrosis of progressive chronic kidney disease."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Uremia and dialysis lines invite infection: impaired uremic immunity and the catheters used for dialysis make bloodstream infection and sepsis a leading cause of death in advanced kidney disease."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Failing kidneys tip the blood toward clots: CKD, especially with heavy proteinuria, creates a hypercoagulable state that raises the risk of deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "It deranges the whole skeleton: CKD-mineral and bone disorder disturbs phosphate, vitamin D and PTH balance into renal osteodystrophy, leaving bone that is both low in density and poor in quality, with high fracture risk."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Dialysis and decline weigh on the mind: depression is the commonest psychiatric problem in CKD, driven by the burden of dialysis, lost function and uremic effects on the brain, and it worsens outcomes."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Fluid overload and uremia stiffen the lung vessels: CKD is an under-recognized cause of pulmonary hypertension, driven by volume overload, the arteriovenous dialysis fistula and uremic vascular changes."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Dialysis access is a portal for Staph: hemodialysis catheters and fistulas give Staphylococcus aureus repeated entry to the bloodstream, making access-related S. aureus bacteremia a leading infection in CKD."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Uremia stalls tissue repair: the impaired immunity, anemia and, in advanced disease, calciphylaxis of CKD leave skin ulcers and surgical wounds slow to heal, a major source of morbidity."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Retained toxins injure the nerves: uremia causes a length-dependent peripheral neuropathy and restless, painful legs, producing chronic neuropathic pain in advanced kidney disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "The kidney is itself an endocrine organ that fails: CKD causes erythropoietin deficiency, impaired vitamin D activation and secondary hyperparathyroidism, the mineral-and-hormone disorder at its core."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Uraemia poisons the gut: advanced CKD causes anorexia, nausea and uraemic gastritis with a raised risk of GI bleeding, while a uraemic foetor and altered taste worsen the malnutrition."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Uraemia cripples immune defence: CKD impairs both innate and adaptive immunity and blunts vaccine responses, leaving dialysis patients especially prone to severe infection — a leading cause of death."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Uraemic toxins poison the nerves: CKD causes uraemic encephalopathy with confusion and asterixis, peripheral and autonomic neuropathy, and restless legs that disturb sleep."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Fluid and acid reach the lungs: salt and water retention in CKD cause pulmonary oedema and pleural effusions, while metabolic acidosis drives the deep Kussmaul breathing of advanced disease."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It weakens the skeleton: by disturbing calcium, phosphate, vitamin D and parathyroid hormone, CKD causes renal osteodystrophy — the mineral and bone disorder — with bone pain and fractures."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It marks the skin: uraemia brings intractable pruritus and 'uraemic frost', while disordered calcium and phosphate can cause calciphylaxis, painful necrotic skin ulcers in advanced kidney failure."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Dialysis carries a transmission risk: shared circuits and frequent vascular access historically spread hepatitis B and C between patients, so units screen, isolate and vaccinate against HBV."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Uraemia suppresses immunity: the impaired T-cell function of advanced kidney disease and dialysis raises the risk of reactivating latent tuberculosis."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "The cornerstone of renoprotection: ACE inhibitors block angiotensin II, lowering glomerular pressure and proteinuria to slow CKD progression, the foundation of treatment in diabetic and proteinuric kidney disease."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "The gut shapes uraemic toxicity: a high-fibre diet shifts the microbiome to make fewer protein-bound uraemic toxins like indoxyl sulfate, of interest in slowing CKD and its cardiovascular complications."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "A virus that scars the kidney: chronic hepatitis C causes membranoproliferative glomerulonephritis and cryoglobulinaemic kidney disease, a treatable infectious driver of chronic kidney disease."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It deranges the skeleton: CKD-mineral-bone disorder — phosphate retention, low vitamin D and secondary hyperparathyroidism with high FGF23 — weakens cortical bone as renal osteodystrophy, raising fracture risk."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It calcifies the arteries: disturbed calcium-phosphate balance in CKD drives medial vascular calcification of the arterial wall, stiffening vessels and accelerating the cardiovascular disease that kills most CKD patients."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: connects-to
    note: "Cardiovascular risk dominates: CKD multiplies cardiovascular risk so much that statins reduce events in non-dialysis CKD (as in the SHARP trial), though the benefit attenuates once patients reach dialysis."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Uraemia weakens the heart muscle: CKD drives left ventricular hypertrophy and myocardial fibrosis through pressure-volume overload, FGF23 and uraemic toxins, making cardiac death the commonest outcome of kidney disease."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Light chains clog the kidney: multiple myeloma's monoclonal free light chains precipitate as casts (cast nephropathy) causing CKD, so unexplained renal failure with anaemia warrants a myeloma screen."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Lupus nephritis scars the kidney: immune-complex glomerulonephritis is a leading cause of chronic kidney disease in young women with SLE, sometimes progressing to end-stage failure."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Diabetic nephropathy from youth: decades of type 1 diabetes scar the glomeruli into a leading cause of end-stage kidney disease, the same diabetic mechanism as type 2 but starting earlier in life."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity-related glomerulopathy: excess adiposity drives glomerular hyperfiltration and a secondary focal segmental glomerulosclerosis, an increasingly common and independent path to chronic kidney disease."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Where renal anaemia bites: failing kidneys make too little erythropoietin, starving the bone marrow of the signal to produce red cells—the basis of the anaemia that tracks declining kidney function."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Potassium kills the rhythm: as the kidney fails to excrete potassium, hyperkalaemia peaks the T wave and can trigger fatal arrhythmia through the cardiac conduction system—a leading cause of sudden death on dialysis."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A deadly vulnerability: dialysis and advanced CKD carried among the highest COVID-19 mortality, while severe COVID-19 itself causes acute kidney injury that can leave lasting chronic kidney disease."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Uraemic seizures: accumulated uraemic toxins, electrolyte derangements and dialysis disequilibrium can provoke seizures, and CKD complicates the dosing of renally-cleared anti-seizure drugs."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: uraemic toxins and the accumulation of the eNOS inhibitor ADMA cut nitric oxide in CKD, driving the hypertension and accelerated vascular disease of kidney failure."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vasoconstrictor and fibrosis: endothelin-1 rises in CKD to constrict renal vessels, retain sodium and promote tubulointerstitial fibrosis, a target of endothelin antagonists in proteinuric disease."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Uraemic inflammation: TNF-α is a key cytokine of the chronic low-grade inflammation of CKD, contributing to its anaemia, muscle wasting and high cardiovascular risk."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Interstitial fibrosis: CCL2 recruits monocytes into the kidney interstitium, where they become macrophages driving the tubulointerstitial inflammation and fibrosis that progress chronic kidney disease."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Glomerular maintenance: podocyte-derived VEGF preserves the glomerular capillary endothelium, and its dysregulation contributes to the glomerulosclerosis and capillary rarefaction of CKD."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement injury: C3 and the alternative pathway drive glomerular damage across many CKD aetiologies, from C3 glomerulopathy to immune-complex glomerulonephritis, an emerging therapeutic target."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Anemia therapy target: HIF-prolyl-hydroxylase inhibitors (roxadustat) stabilise HIF-1α to boost endogenous erythropoietin and improve iron handling, an oral treatment for the renal anaemia of CKD."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Chronic inflammation: persistently elevated IL-6 in CKD drives hepcidin-mediated anaemia and is a major contributor to the accelerated cardiovascular risk and protein-energy wasting of advanced kidney disease."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Dyslipidaemia and CV risk: CKD causes an atherogenic dyslipidaemia, and the resulting accelerated atherosclerosis makes cardiovascular disease — not kidney failure itself — the leading cause of death in CKD."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Mineral-bone disorder: failing kidneys lose phosphate and calcium control, and the resulting hyperphosphataemia and secondary hyperparathyroidism drive both renal bone disease and the vascular calcification that worsens CKD cardiovascular mortality."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Metabolic renoprotection: GLP-1 receptor agonists reduce albuminuria and slow eGFR decline in diabetic chronic kidney disease, adding a metabolic-pathway renoprotective therapy alongside RAAS blockade and SGLT2 inhibition."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Urate retention: failing renal clearance raises serum urate, and xanthine-oxidase-generated uric acid contributes both to the gout common in CKD and, debated, to progression itself, the rationale behind urate-lowering trials in kidney disease."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Fibrogenic reactivation: sustained reactivation of Wnt/β-catenin signalling drives the myofibroblast activation and tubulointerstitial fibrosis that is the final common pathway of progressive chronic kidney disease."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD fibrosis: TGF-β signals through the SMAD pathway (SMAD4) to drive the renal fibrosis (TGF-β already mapped) that scars glomeruli and interstitium and destroys nephrons in CKD."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammatory progression: NLRP3-inflammasome activation and IL-1β in the injured kidney sustain the chronic inflammation that accelerates fibrosis and nephron loss in chronic kidney disease."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Antioxidant defence: NRF2 orchestrates the antioxidant response that protects tubular cells from the oxidative injury of CKD, and its pharmacological activation (bardoxolone) raises glomerular filtration rate in diabetic kidney disease."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Compensatory hypertrophy: mTOR drives the glomerular and tubular hypertrophy that follows nephron loss — initially adaptive but ultimately accelerating podocyte stress and progressive kidney failure."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate inflammation: TLR sensing of uremic damage-associated molecular patterns signals through MyD88 to NF-κB, sustaining the chronic innate-immune activation that propels CKD progression."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is a driver and biomarker of the renal and cardiac fibrosis that links CKD to its cardiovascular complications."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling (mTOR mapped) governs podocyte and tubular-cell survival and the hypertrophic responses that shape CKD progression."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGF drives mesangial and fibroblast proliferation, contributing to the glomerulosclerosis and tubulointerstitial fibrosis of chronic kidney disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling drives the tubulointerstitial inflammation and fibrotic progression of chronic kidney disease."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING links tubular cell injury to the sterile inflammation that drives progression of chronic kidney disease."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune-mediated and interferon-driven inflammation of chronic kidney disease."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate podocyte and tubular oxidative-stress defense whose failure accelerates the progression of chronic kidney disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of angiotensin II and growth factors (angiotensin-II and PDGF already mapped) drives the tubulointerstitial fibrosis of chronic kidney disease."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the chronic inflammation and tubular injury that drive progression of chronic kidney disease."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β, within the Wnt/β-catenin signaling that drives tubulointerstitial fibrosis (Wnt already mapped), modulates the progressive fibrosis of chronic kidney disease."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the tubular-cell survival and hypertrophic responses of chronic kidney disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic lymphocytes contribute to the immune-mediated tubulointerstitial injury of chronic kidney disease."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling maintains the tubular-cell energy homeostasis whose failure drives the progression of chronic kidney disease."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the podocyte and tubular-cell homeostasis whose decline accelerates chronic kidney disease."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the tubulointerstitial fibrosis and myofibroblast activation of chronic kidney disease."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the tubular and fibrotic gene programs of chronic kidney disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the tubulointerstitial inflammation and fibrosis of chronic kidney disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the renal fibrosis and leukocyte trafficking of chronic kidney disease."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the chronic inflammation and fibrosis of chronic kidney disease."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the renal inflammation and fibrosis of chronic kidney disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the renal inflammation and fibrosis of chronic kidney disease."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Metabolic acidosis: the failing kidney cannot excrete the daily acid load or regenerate enough bicarbonate, so protons accumulate, and the resulting metabolic acidosis accelerates bone loss and muscle wasting, treated with oral alkali."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium retention: as kidney function declines, magnesium excretion falls and hypermagnesaemia can develop, while magnesium also modulates the vascular calcification that drives cardiovascular death in chronic kidney disease."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin handling: chronic kidney disease induces peripheral insulin resistance yet also reduces renal insulin clearance, a combination that complicates glucose control and contributes to the metabolic disturbance of uraemia."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiorenal injury: cardiovascular disease is the leading cause of death in chronic kidney disease, and chronically elevated troponin reflects the ongoing myocardial injury of the cardiorenal syndrome even without acute infarction."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Drug clearance and pruritus: many opioids and their active metabolites accumulate in renal failure, requiring dose adjustment, and altered opioid signalling contributes to the distressing uraemic pruritus of advanced chronic kidney disease."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "IgA nephropathy: deposition of galactose-deficient IgA immune complexes in the glomerular mesangium causes IgA nephropathy, one of the commonest primary glomerular diseases progressing to chronic kidney disease worldwide."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron-restricted anaemia: the failing kidney's low erythropoietin (already mapped) and the raised hepcidin (already mapped) of chronic inflammation restrict iron for erythropoiesis, and intravenous iron is a mainstay of managing the anaemia of chronic kidney disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Renal prostaglandins: prostaglandins maintain afferent arteriolar tone and renal blood flow, so non-steroidal anti-inflammatory drugs that block them cause acute injury and accelerate chronic kidney disease, a common nephrotoxic exposure."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Inflammatory progression: IL-10 opposes the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) that drive the interstitial inflammation and fibrosis (TGF-beta already mapped) of progressive chronic kidney disease, part of its immune balance."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium and volume overload: the failing kidney retains sodium (aldosterone already mapped), and the resulting volume overload drives the hypertension and fluid retention that accelerate chronic kidney disease and its cardiovascular risk."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron-restricted anaemia: the raised hepcidin (already mapped) and the failing erythropoietin (already mapped) of chronic kidney disease restrict iron for erythropoiesis, producing the renal anaemia managed with iron and erythropoiesis-stimulating agents."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Cause and consequence: hypertension is both a leading cause and a near-universal consequence of chronic kidney disease, the renin-angiotensin (already mapped) activation and volume overload creating a vicious cycle that hastens renal decline."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Profibrotic type-2 cytokine: IL-13, with IL-4 (already mapped), is a profibrotic type-2 cytokine that contributes to the renal interstitial fibrosis (TGF-β already mapped) driving the progression of chronic kidney disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 fibrosis: IL-4 drives the M2 macrophages and the type-2 immunity involved in the renal interstitial fibrosis (TGF-β already mapped) that drives the progression of chronic kidney disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Renal adipokine retention: leptin is cleared by the kidney and accumulates in chronic kidney disease, contributing to the uraemic cachexia, sympathetic activation and cardiovascular risk."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Uraemic adipokine: adiponectin, with leptin (already mapped), is cleared by and accumulates in the chronic kidney disease, part of the uraemic metabolic-cardiovascular milieu."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Uraemic inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), accumulates in the chronic kidney disease and contributes to the uraemic inflammatory (IL-6 already mapped) milieu."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hepatorenal axis: the liver-kidney axis (the hepatorenal syndrome, the hepcidin already-mapped production driving the renal anaemia) links the liver to the chronic kidney disease."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate renal inflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the tubular stress and DNA damage, contributes to the chronic inflammation and fibrosis of chronic kidney disease."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 renal inflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune-mediated tubulointerstitial inflammation of chronic kidney disease."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension driving the progression of chronic kidney disease."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of chronic kidney disease (and the eosinophilic interstitial nephritis)."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-mediated tubulointerstitial inflammation of chronic kidney disease."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune milieu of chronic kidney disease."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines driving the tubulointerstitial inflammation and the fibroblast (already mapped)-mediated fibrosis of chronic kidney disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Renal mast cells: the mast cells infiltrate the interstitium and, via their profibrotic mediators, promote the tubulointerstitial fibrosis (TGF-β already mapped) of chronic kidney disease."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment and the complement-mediated tubulointerstitial injury of chronic kidney disease."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) generate the membrane-attack complex contributing to the glomerular and tubulointerstitial injury of chronic kidney disease."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation causes the C3 glomerulopathy contributing to chronic kidney disease."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Renal anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin and erythropoietin already mapped) of the renal anaemia of chronic kidney disease."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-tubular axis: TSLP, from tubular epithelium under the hypoxia and proteinuria of chronic kidney disease, primes dendritic cells (already mapped) and mast cells (already mapped) toward the Th2/Th17 (already mapped) tubulointerstitial inflammation."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-renal axis: bradykinin, via the intrarenal kallikrein-kinin system and the accumulation from reduced renal clearance, amplifies the vascular permeability and the tubular injury contributing to the progression of chronic kidney disease."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3, C5 and factor-H already mapped) contributing to the C3 glomerulopathy and the immune-complex nephritis of chronic kidney disease."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell renal effector: histamine, released by peritubular mast cells (already mapped) in the interstitium of CKD, promotes vascular permeability and amplifies the pro-inflammatory cytokine milieu (TGF-β and IL-6 already mapped) driving the tubulointerstitial fibrosis of CKD."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Fibrotic ECM scaffold: periostin, expressed by renal fibroblasts (already mapped) under TGF-β (already mapped) stimulation, is a key driver of the extracellular matrix deposition and the interstitial fibrosis-driven nephron loss of chronic kidney disease."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian renoprotection: melatonin, via MT1/MT2 receptors on tubular cells and mesangial cells (already mapped), scavenges ROS (already mapped) and attenuates the oxidative and inflammatory tubulointerstitial injury driving the progression of CKD."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "CKD testosterone: testosterone, via androgen receptors on tubular cells and mesangial cells, attenuates TGF-β (already mapped) and NF-κB (already mapped) renal fibrosis; androgen deficiency amplifies macrophage (already mapped) and IL-6 (already mapped) fibrotic injury of CKD."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "CKD serotonin: serotonin, via 5-HT receptors on mesangial cells and macrophages (already mapped), modulates glomerular (already mapped) haemodynamics; serotonin dysregulation amplifies the TGF-β (already mapped) and NF-κB (already mapped) tubulointerstitial fibrosis of CKD."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "CKD prolactin: prolactin, via PRLR on macrophages (already mapped), promotes TGF-β (already mapped) and NF-κB (already mapped) fibrotic signalling; hyperprolactinaemia amplifies the erythropoietin (already mapped) resistance and iron (already mapped) deficiency anaemia of CKD."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "CKD oxytocin: oxytocin, via OXTR on tubular cells and macrophages (already mapped), attenuates TGF-β (already mapped) and NF-κB (already mapped) fibrotic signalling; oxytocin deficiency amplifies the glomerular (already mapped) and tubulointerstitial injury cascade of CKD."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "CKD vasopressin: vasopressin, via V2 receptors on renal tubular cells, drives hyperfiltration and renin (already mapped) activation of CKD; vasopressin excess amplifies TGF-β (already mapped) and NF-κB (already mapped) glomerular (already mapped) fibrosis of CKD."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "CKD selenium: selenium, as GPx in renal tubular cells and macrophages (already mapped), scavenges CKD oxidative-stress; selenium deficiency amplifies the NF-κB (already mapped) and TGF-β (already mapped) tubulointerstitial fibrosis and hepcidin (already mapped) anaemia of CKD."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "CKD zinc: zinc supports macrophage (already mapped) anti-inflammatory resolution and tubular cell integrity; zinc deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) glomerular fibrosis and hepcidin (already mapped)-mediated anaemia in chronic kidney disease."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "CKD copper: copper-dependent SOD in renal tubular cells and macrophages (already mapped) counters ROS; copper deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) tubulointerstitial fibrosis and hepcidin (already mapped) anaemia of chronic kidney disease."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "CKD iodine: thyroid hormones regulate macrophage (already mapped) and mesangial cells (glomerulus already mapped); thyroid deficiency amplifies TGF-β (already mapped) and NF-κB (already mapped) fibrosis and erythropoietin (already mapped) suppression of CKD."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "CKD chloride: chloride, via CFTR and ClC-Ka/Kb in renal tubular cells and macrophages (already mapped), regulates acid-base balance; chloride dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) tubular injury and fibrosis of CKD."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "carbon metabolism in renal tubular cells and macrophage (already mapped) drives oxidative phosphorylation; carbon dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrosis and hepcidin (already mapped) cascade in CKD."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "sulfur, as glutathione precursor in renal tubular cells and macrophage (already mapped), counters oxidative stress; sulfur deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) tubulointerstitial fibrosis cascade in CKD."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "nitrogen, as urea-cycle substrate in renal tubular cells and macrophage (already mapped), governs uraemic toxin clearance; nitrogen retention amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrosis cascade in CKD."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "CKD oxygen: oxygen via ROS from renal tubular cells (already mapped) and macrophages (already mapped) modulates redox homeostasis; oxygen excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "CKD pd-1: PD-1 on t-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses renal immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "CKD rankl: RANKL from renal tubular cells (already mapped) and macrophages (already mapped) modulates bone-kidney mineral axis; RANKL excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "CKD il-2: IL-2 on t-cells (already mapped) and macrophages (already mapped) amplifies renal immune activation; il-2 excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "CKD fibronectin: fibronectin in renal tubular cells (already mapped) and fibroblasts (already mapped) promotes ECM deposition; fibronectin excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "CKD igf-1: IGF-1 on renal tubular cells (already mapped) and macrophages (already mapped) modulates renal hypertrophy; igf-1 excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "CKD notch: Notch in renal tubular cells (already mapped) and macrophages (already mapped) regulates renal cell fate; Notch dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "CKD activin-a: activin-A in renal tubular cells (already mapped) and fibroblasts (already mapped) promotes renal fibrosis; activin-A dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) cascade in CKD."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "CKD cgrp: CGRP in renal endothelial cells (already mapped) and macrophages (already mapped) modulates renal vascular tone; CGRP dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) cascade in CKD."
---

# Chronic Kidney Disease

## Overview

**Chronic kidney disease (CKD)** is defined by the KDIGO 2012 guidelines as persistent abnormalities of kidney structure or function (eGFR <60 mL/min/1.73 m² or markers of kidney damage) present for **>3 months** [^kdigo-2012-ckd]. It represents a global public health crisis — affecting approximately **14% of the US adult population** (37 million individuals) and **697 million** people globally — and is the leading cause of **end-stage kidney disease (ESKD)** requiring renal replacement therapy (dialysis or transplantation).

The two dominant causes are **diabetic nephropathy** (~44% of new ESKD cases) and **hypertensive nephrosclerosis** (~27%), together responsible for nearly three-quarters of ESKD. Additional causes include glomerulonephritis (IgA nephropathy, FSGS, membranous nephropathy), polycystic kidney disease, chronic tubulointerstitial disease (analgesic nephropathy, reflux nephropathy), and obstructive uropathy.

CKD is fundamentally a disease of **progressive nephron loss**: regardless of etiology, the final common pathway is tubular atrophy, glomerulosclerosis, and interstitial fibrosis driven by TGF-β, renin-angiotensin-aldosterone system (RAAS) activation, and complement-mediated injury. As the GFR declines, the remaining nephrons undergo adaptive hyperfiltration — increasing single-nephron GFR — which sustains overall clearance temporarily but accelerates glomerular injury.

## Structure

### Staging by GFR and albuminuria (KDIGO G-A classification)

CKD is classified by GFR category (G1-G5) and albuminuria category (A1-A3) [^levey-2012-ckd-lancet]:

**GFR stages:**
| Stage | eGFR (mL/min/1.73 m²) | Description |
|:---|:---|:---|
| G1 | ≥90 | Normal or high (with kidney damage marker) |
| G2 | 60–89 | Mildly decreased |
| G3a | 45–59 | Mildly-moderately decreased |
| G3b | 30–44 | Moderately-severely decreased |
| G4 | 15–29 | Severely decreased |
| G5 | <15 | Kidney failure (ESKD if treated) |

**Albuminuria categories:**
- A1: <30 mg/g creatinine (normal to mildly increased)
- A2: 30–300 mg/g (moderately increased; formerly "microalbuminuria")
- A3: >300 mg/g (severely increased; formerly "macroalbuminuria")

The combination of GFR stage + albuminuria category determines risk of progression and complications; G3b-G5 + A3 ("orange/red zone") carries the highest risk.

**eGFR estimation:** The 2021 **CKD-EPI creatinine equation** (race-free version) is the current standard for estimating GFR from serum creatinine and cystatin C in adults. Measured GFR (iohexol, inulin clearance) is reserved for borderline cases.

### Histopathology of CKD progression

The final common structural endpoint across CKD etiologies:
- **Glomerulosclerosis:** Global or segmental obliteration of glomerular capillary tufts; collagen deposition replacing mesangium; podocyte loss
- **Tubular atrophy:** Shrinkage and loss of tubular cells, with basement membrane thickening; marker of irreversible nephron loss
- **Interstitial fibrosis:** Progressive collagen deposition (types I, III, IV) in tubulointerstitium driven by TGF-β → fibroblast-to-myofibroblast transition; the extent of interstitial fibrosis correlates most strongly with GFR decline rate
- **Arterial/arteriolar thickening:** Medial hypertrophy, intimal fibrosis, hyalinosis (especially with hypertension and diabetes)

## Function

### Consequences of declining GFR

As nephron mass decreases, impaired renal functions accumulate:

**Solute accumulation (uremia):** Retained uremic solutes (urea, creatinine, β₂-microglobulin, indoxyl sulfate, p-cresyl sulfate) cause the **uremic syndrome**: nausea, pericarditis, asterixis, encephalopathy, platelet dysfunction (uremic bleeding).

**Fluid and electrolyte imbalance:** Reduced urine concentrating ability → isosthenuria; Na⁺ retention → hypertension, edema; K⁺ retention → hyperkalemia (risk of arrhythmia); impaired acid excretion → metabolic acidosis (↓HCO₃⁻, normal/high anion gap).

**Anemia of CKD:** EPO deficiency from loss of peritubular interstitial cells → normocytic normochromic anemia; target Hgb 10–11.5 g/dL with EPO-stimulating agents (ESA); iron deficiency often co-exists.

**CKD-mineral bone disease (CKD-MBD):**
- ↓GFR → ↑phosphate retention → ↓ionized Ca²⁺ → ↑PTH (secondary hyperparathyroidism)
- ↓1α-hydroxylase (renal) → ↓calcitriol (1,25-OH₂D₃) → ↓intestinal Ca absorption → worsened hypocalcemia → further ↑PTH
- Consequence: osteitis fibrosa cystica, adynamic bone disease, vascular calcification (from CaPO₄ deposition)

**Cardiovascular disease:** The leading cause of death in CKD. Mechanisms: hypertension, volume overload, uremic cardiomyopathy (LVH), accelerated atherosclerosis, endothelial dysfunction, and increased oxidative stress. CKD stages G3-G5 carry 10–100× higher CV mortality than the general population.

### Treatment and progression slowing [^coresh-2007-prevalence]

**RAAS blockade (ACEi/ARB):** First-line for proteinuric CKD — reduce intraglomerular pressure, decrease proteinuria, attenuate TGF-β-driven fibrosis; proven to slow progression in diabetic and non-diabetic CKD. Avoid combination ACEi + ARB (↑AKI/hyperkalemia risk without added benefit).

**SGLT2 inhibitors:** Second-line (now often first-line in diabetic CKD); empagliflozin, dapagliflozin reduce proteinuria and slow GFR decline by ~40% through tubuloglomerular feedback restoration, reduced hyperfiltration, and anti-inflammatory effects independent of glycemic control.

**Blood pressure control:** Target <130/80 mmHg in CKD; reduces progression rate and CV mortality.

**Renal replacement therapy (ESKD):** 
- Hemodialysis: 3× weekly × 4h sessions; removes small solutes but not middle molecules well
- Peritoneal dialysis: CAPD or APD; continuous; removes middle molecules better; preserves residual renal function longer
- Renal transplantation: Preferred; 1-year graft survival >95%; 10-year patient survival superior to dialysis; requires immunosuppression (tacrolimus + mycophenolate + steroids)

## Connections

- `targets` → **[Kidney](../../06-organ/kidney/README.md)** — CKD destroys renal parenchyma through glomerulosclerosis, tubular atrophy, and interstitial fibrosis; the kidney is the primary target organ.
- `part-of` → **[Renal System](../renal-system/README.md)** — CKD is the defining chronic pathological state of the renal system, progressively impairing all kidney functions.
- `modulates` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — CKD reduces EPO synthesis from peritubular fibroblasts; anemia of CKD requires ESA therapy to maintain hemoglobin targets.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — CKD and hypertension are bidirectionally causal; each accelerates the other. BP control to <130/80 mmHg is the cornerstone of CKD management.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — CREDENCE (canagliflozin): 30% reduction in kidney endpoint in T2D + CKD; DAPA-CKD (dapagliflozin): 39% reduction in eGFR decline/dialysis/renal death in CKD with and without T2D; SGLT2 inhibitors slow CKD progression via tubuloglomerular feedback and anti-fibrotic effects.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — FGF23 rises 100-1000× in CKD → suppresses 1α-hydroxylase → reduced calcitriol → secondary hyperparathyroidism and CKD-MBD; very high FGF23 predicts LVH, heart failure, and mortality in dialysis patients independent of traditional risk factors.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — OPN is upregulated in injured renal tubular epithelium → integrin αvβ3 on macrophages → macrophage recruitment and pro-inflammatory activation → tubulointerstitial fibrosis; urinary OPN predicts CKD progression; OPN inhibits calcium oxalate crystal adhesion (stone inhibitor).
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — IgA nephropathy is a leading cause of CKD in young adults; mesangial IgA deposition → complement + CCL2 → tubulointerstitial fibrosis → eGFR decline; 20-40% of IgAN reach ESRD within 20 years; sparsentan (ETA/AT1R dual blocker) and iptacopan are disease-modifying therapies.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Hepcidin is elevated in CKD from reduced renal clearance and chronic inflammation; elevated hepcidin → functional iron deficiency → ESA hyporesponsiveness in CKD anemia; HIF-PHIs (roxadustat, daprodustat) suppress hepcidin via EPO→ERFE→BMP-SMAD inhibition.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — CKD anemia is the overlap of EPO deficiency and ACD mechanisms: reduced EPO from peritubular cell loss + hepcidin elevation from CKD inflammation/reduced clearance → combined functional iron deficiency + erythropoietic failure; IV iron + ESA are first-line for CKD anemia.
- `connects-to` → **[Atypical HUS](../ahus/README.md)** — aHUS from complement dysregulation (CFH/CFI mutations) causes progressive CKD; ~50% of untreated aHUS patients reach ESRD within 1 year; eculizumab/ravulizumab reverse TMA and may improve eGFR; renal transplant requires lifelong C5 inhibition in high-risk CFH mutations.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — SCD causes sickle cell nephropathy via medullary sickling (high osmolarity + low pO2 in vasa recta → medullary ischaemia) → hyposthenuria, papillary necrosis, proteinuria; progressive CKD in ~30% HbSS by age 40; ACE inhibitors + hydroxyurea slow progression.
- `connects-to` → **[Malaria](../malaria/README.md)** — Severe falciparum malaria causes AKI in 4-8% (haemoglobinuria + microvascular obstruction + cytokine storm); cerebral malaria + AKI → high mortality; repeated malaria episodes contribute to CKD burden in endemic populations.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — dialysis patients have elevated sclerostin from impaired renal clearance + uremic Wnt suppression → adynamic bone disease; elevated sclerostin correlates with vascular calcification and mortality in CKD; romosozumab is not approved in severe CKD due to CV risk.
- `connects-to` → **[Prurigo Nodularis](../prurigo-nodularis/README.md)** — CKD-associated pruritus (formerly uremic pruritus) causes PN-like nodules in dialysis patients; uremic toxins activate μ-opioid and κ-opioid receptors on pruriceptors; difelikefalin (κ-opioid agonist; FDA 2021 for CKD-aP on HD) reduces itch and may prevent PN nodule formation.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes is the leading cause of chronic kidney disease: chronic hyperglycemia damages the glomerular filter (diabetic nephropathy), causing proteinuria and progressive function loss, so diabetic kidney disease drives most dialysis need—SGLT2 inhibitors now slow it.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — CKD and atherosclerosis form a vicious cardiorenal cycle: declining kidney function accelerates vascular calcification and atherosclerosis, so cardiovascular disease—not kidney failure—is the leading cause of death in CKD.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — CKD deranges calcium and bone metabolism (CKD-MBD): failing kidneys can't activate vitamin D or excrete phosphate, lowering calcium and driving secondary hyperparathyroidism and vascular calcification—so calcium, phosphate and PTH are tightly managed in CKD.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — Podocyte loss is a key driver of progressive CKD: these non-dividing cells form the glomerular filter, and when injury (by diabetes, hypertension or FSGS) kills them, the barrier leaks protein and scars, so podocyte depletion predicts irreversible decline.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — CKD often begins in the glomerulus: damage to the filtering tuft causes proteinuria and falling filtration, and surviving glomeruli hyperfilter to compensate—a maladaptive overwork that scars them too, driving the relentless nephron loss of chronic kidney disease.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — CKD and cardiovascular disease are lethally intertwined: most people with CKD die of heart disease, not kidney failure, because uremia, fluid overload and hypertension accelerate atherosclerosis—so the failing kidney is a powerful cardiac risk factor.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Failing kidneys can't dump potassium: as filtration drops, potassium builds up, and hyperkalemia—worsened by the ACE inhibitors and ARBs used to protect the kidney—can stop the heart, so it is among CKD's most urgent, monitored complications.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Heart and kidney failure drive each other (cardiorenal syndrome): CKD's fluid overload, hypertension, and anemia strain the heart, while a failing heart underperfuses the kidney—so the two organs decline together and share treatments like SGLT2 inhibitors.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — CKD cripples vitamin D activation: damaged kidneys can't perform the final hydroxylation to active calcitriol, so calcium absorption falls and parathyroid hormone rises—driving the renal bone disease that defines CKD's mineral and bone disorder.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — CKD progresses through fibrosis: whatever the initial insult, tubulointerstitial fibrosis is the final common pathway that scars nephrons beyond repair, so the degree of fibrosis on biopsy predicts decline better than the original diagnosis.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — CKD throws phosphorus out of balance: failing kidneys can't excrete phosphate, so it rises and—with FGF23, PTH and low vitamin D—drives the bone disease and vascular calcification of CKD-mineral bone disorder.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Angiotensin II accelerates CKD and is the key drug target: it raises glomerular pressure and drives scarring, so ACE inhibitors and ARBs that block it slow progression and reduce proteinuria—the cornerstone of renoprotection.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — CKD and the heart fail together in cardiorenal syndrome: fluid overload, hypertension, anemia and mineral disturbance strain the heart, while heart failure starves the kidneys of flow, so most CKD patients die of cardiovascular causes.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Aldosterone drives the scarring that worsens CKD: beyond raising blood pressure, it promotes fibrosis and inflammation in the kidney, which is why mineralocorticoid blockers like finerenone slow progression on top of ACE inhibitors.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — CKD unleashes bone-dissolving osteoclasts: phosphate retention and secondary hyperparathyroidism overstimulate osteoclasts, the high-turnover renal osteodystrophy that weakens bone and spills calcium and phosphate into vessels.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — CKD turns the blood acidic: failing kidneys cannot excrete the body's daily acid load or regenerate bicarbonate, so hydrogen ions build up into a metabolic acidosis that wastes muscle and bone and is treated with bicarbonate.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — CKD poisons the brain: retained uremic toxins cause the confusion, fatigue, and—in advanced failure—the asterixis and seizures of uremic encephalopathy, symptoms that dialysis is meant to clear.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — CKD wrecks the endothelium: uremic toxins and mineral imbalance injure the vessel-lining cells and calcify artery walls, driving the accelerated atherosclerosis that makes heart disease, not kidney failure, the usual cause of death.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging stages CKD's structure: ultrasound and CT photons show shrunken, scarred kidneys or obstruction, while nuclear scans measure the failing filtration that blood tests only estimate.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — CKD itches relentlessly: retained toxins and mineral imbalance cause uremic pruritus, which patients scratch into prurigo nodularis, one of the most distressing symptoms of advanced kidney failure.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — CKD progresses through fibroblasts: injured kidneys activate myofibroblasts that lay down interstitial scar, the common final pathway by which any kidney disease marches toward failure.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals the failing filter: as CKD advances, the glomerular basement membrane thickens and wrinkles while podocyte foot processes flatten and fuse, the ultrastructural decay that lets protein leak and filtration fall.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Failing kidneys leave the blood thin: the diseased kidney makes too little erythropoietin to tell the marrow to build red cells, so anemia is a near-universal companion of CKD, treated with EPO and iron.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — CKD upends magnesium balance: as the kidney loses its power to excrete the mineral, magnesium can build to dangerous levels — especially with magnesium-containing laxatives or antacids — risking weakness and heart-rhythm disturbance.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — CKD drives the parathyroids into overdrive: falling vitamin D and rising phosphate push PTH ever higher (secondary hyperparathyroidism), and the relentless hormone leaches bone into renal osteodystrophy — the core of CKD-mineral-bone disorder.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — The failing kidney lets the blood thin: it makes too little erythropoietin, so hemoglobin falls into the anemia of CKD, treated by replacing the missing hormone with erythropoiesis-stimulating agents.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Uremia makes the platelets sluggish: retained toxins impair platelet function, so even with a normal count CKD patients bruise and bleed more easily, a defect that dialysis and desmopressin can partly correct.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — The kidney loses its grip on salt and water: as CKD advances it cannot excrete a sodium load, so fluid builds up into edema and hypertension, making dietary salt restriction a cornerstone of slowing the disease.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies cause and define much CKD: anti-GBM, ANCA, and lupus autoantibodies attack the glomerulus, and their blood assays pinpoint the immune glomerulonephritides that, untreated, scar the kidney into failure.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Uremia dampens reproduction: it disrupts the hypothalamic-pituitary-gonadal axis into low libido, erectile dysfunction, and infertility, and pregnancy in advanced CKD carries high risk to mother and fetus.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — The failing kidney misreads its own pressure: falling perfusion drives renin and the RAAS into overdrive, raising blood pressure that further scars the kidney — a vicious loop that RAAS blockers are given to interrupt.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages turn injury into scar: they infiltrate the damaged kidney and pour out fibrogenic signals that activate fibroblasts, driving the tubulointerstitial fibrosis that paces the march to kidney failure.
- `connects-to` → **[Gout](../gout/README.md)** — Kidney and urate trap each other: failing kidneys clear less uric acid, raising it into gout, while urate crystals and the drugs for gout can in turn injure the kidney — a two-way burden in CKD.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Fibrosis is the final common path: whatever the initial insult, TGF-β drives tubular cells and fibroblasts to scar the kidney with collagen, the progressive interstitial fibrosis that determines how fast CKD advances.
- `connects-to` → **[Stroke](../stroke/README.md)** — Failing kidneys imperil the brain's vessels: uremic vasculopathy, hypertension and accelerated atherosclerosis make stroke far more common in CKD, while the bleeding tendency of uremia raises hemorrhagic risk too.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Long-standing damage turns malignant: years of CKD and the acquired cystic disease of dialysis sharply raise the risk of renal cell carcinoma arising in the scarred kidneys.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation scars the kidney forward: NF-κB activation in tubular and immune cells sustains the tubulointerstitial inflammation that, alongside TGF-β, drives the relentless fibrosis of progressive chronic kidney disease.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Uremia and dialysis lines invite infection: impaired uremic immunity and the catheters used for dialysis make bloodstream infection and sepsis a leading cause of death in advanced kidney disease.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Failing kidneys tip the blood toward clots: CKD, especially with heavy proteinuria, creates a hypercoagulable state that raises the risk of deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — It deranges the whole skeleton: CKD-mineral and bone disorder disturbs phosphate, vitamin D and PTH balance into renal osteodystrophy, leaving bone that is both low in density and poor in quality, with high fracture risk.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Dialysis and decline weigh on the mind: depression is the commonest psychiatric problem in CKD, driven by the burden of dialysis, lost function and uremic effects on the brain, and it worsens outcomes.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Fluid overload and uremia stiffen the lung vessels: CKD is an under-recognized cause of pulmonary hypertension, driven by volume overload, the arteriovenous dialysis fistula and uremic vascular changes.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Dialysis access is a portal for Staph: hemodialysis catheters and fistulas give Staphylococcus aureus repeated entry to the bloodstream, making access-related S. aureus bacteremia a leading infection in CKD.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Uremia stalls tissue repair: the impaired immunity, anemia and, in advanced disease, calciphylaxis of CKD leave skin ulcers and surgical wounds slow to heal, a major source of morbidity.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Retained toxins injure the nerves: uremia causes a length-dependent peripheral neuropathy and restless, painful legs, producing chronic neuropathic pain in advanced kidney disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — The kidney is itself an endocrine organ that fails: CKD causes erythropoietin deficiency, impaired vitamin D activation and secondary hyperparathyroidism, the mineral-and-hormone disorder at its core.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Uraemia poisons the gut: advanced CKD causes anorexia, nausea and uraemic gastritis with a raised risk of GI bleeding, while a uraemic foetor and altered taste worsen the malnutrition.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Uraemia cripples immune defence: CKD impairs both innate and adaptive immunity and blunts vaccine responses, leaving dialysis patients especially prone to severe infection — a leading cause of death.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Uraemic toxins poison the nerves: CKD causes uraemic encephalopathy with confusion and asterixis, peripheral and autonomic neuropathy, and restless legs that disturb sleep.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Fluid and acid reach the lungs: salt and water retention in CKD cause pulmonary oedema and pleural effusions, while metabolic acidosis drives the deep Kussmaul breathing of advanced disease.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It weakens the skeleton: by disturbing calcium, phosphate, vitamin D and parathyroid hormone, CKD causes renal osteodystrophy — the mineral and bone disorder — with bone pain and fractures.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It marks the skin: uraemia brings intractable pruritus and 'uraemic frost', while disordered calcium and phosphate can cause calciphylaxis, painful necrotic skin ulcers in advanced kidney failure.
- `connects-to` → **[Hepatitis B virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Dialysis carries a transmission risk: shared circuits and frequent vascular access historically spread hepatitis B and C between patients, so units screen, isolate and vaccinate against HBV.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Uraemia suppresses immunity: the impaired T-cell function of advanced kidney disease and dialysis raises the risk of reactivating latent tuberculosis.
- `connects-to` → **[ACE Inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — The cornerstone of renoprotection: ACE inhibitors block angiotensin II, lowering glomerular pressure and proteinuria to slow CKD progression, the foundation of treatment in diabetic and proteinuric kidney disease.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — The gut shapes uraemic toxicity: a high-fibre diet shifts the microbiome to make fewer protein-bound uraemic toxins like indoxyl sulfate, of interest in slowing CKD and its cardiovascular complications.
- `connects-to` → **[Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md)** — A virus that scars the kidney: chronic hepatitis C causes membranoproliferative glomerulonephritis and cryoglobulinaemic kidney disease, a treatable infectious driver of chronic kidney disease.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It deranges the skeleton: CKD-mineral-bone disorder — phosphate retention, low vitamin D and secondary hyperparathyroidism with high FGF23 — weakens cortical bone as renal osteodystrophy, raising fracture risk.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It calcifies the arteries: disturbed calcium-phosphate balance in CKD drives medial vascular calcification of the arterial wall, stiffening vessels and accelerating the cardiovascular disease that kills most CKD patients.
- `connects-to` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — Cardiovascular risk dominates: CKD multiplies cardiovascular risk so much that statins reduce events in non-dialysis CKD (as in the SHARP trial), though the benefit attenuates once patients reach dialysis.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Uraemia weakens the heart muscle: CKD drives left ventricular hypertrophy and myocardial fibrosis through pressure-volume overload, FGF23 and uraemic toxins, making cardiac death the commonest outcome of kidney disease.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Light chains clog the kidney: multiple myeloma's monoclonal free light chains precipitate as casts (cast nephropathy) causing CKD, so unexplained renal failure with anaemia warrants a myeloma screen.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Lupus nephritis scars the kidney: immune-complex glomerulonephritis is a leading cause of chronic kidney disease in young women with SLE, sometimes progressing to end-stage failure.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Diabetic nephropathy from youth: decades of type 1 diabetes scar the glomeruli into a leading cause of end-stage kidney disease, the same diabetic mechanism as type 2 but starting earlier in life.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity-related glomerulopathy: excess adiposity drives glomerular hyperfiltration and a secondary focal segmental glomerulosclerosis, an increasingly common and independent path to chronic kidney disease.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Where renal anaemia bites: failing kidneys make too little erythropoietin, starving the bone marrow of the signal to produce red cells—the basis of the anaemia that tracks declining kidney function.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Potassium kills the rhythm: as the kidney fails to excrete potassium, hyperkalaemia peaks the T wave and can trigger fatal arrhythmia through the cardiac conduction system—a leading cause of sudden death on dialysis.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A deadly vulnerability: dialysis and advanced CKD carried among the highest COVID-19 mortality, while severe COVID-19 itself causes acute kidney injury that can leave lasting chronic kidney disease.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Uraemic seizures: accumulated uraemic toxins, electrolyte derangements and dialysis disequilibrium can provoke seizures, and CKD complicates the dosing of renally-cleared anti-seizure drugs.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial dysfunction: uraemic toxins and the accumulation of the eNOS inhibitor ADMA cut nitric oxide in CKD, driving the hypertension and accelerated vascular disease of kidney failure.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vasoconstrictor and fibrosis: endothelin-1 rises in CKD to constrict renal vessels, retain sodium and promote tubulointerstitial fibrosis, a target of endothelin antagonists in proteinuric disease.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Uraemic inflammation: TNF-α is a key cytokine of the chronic low-grade inflammation of CKD, contributing to its anaemia, muscle wasting and high cardiovascular risk.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Interstitial fibrosis: CCL2 recruits monocytes into the kidney interstitium, where they become macrophages driving the tubulointerstitial inflammation and fibrosis that progress chronic kidney disease.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Glomerular maintenance: podocyte-derived VEGF preserves the glomerular capillary endothelium, and its dysregulation contributes to the glomerulosclerosis and capillary rarefaction of CKD.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement injury: C3 and the alternative pathway drive glomerular damage across many CKD aetiologies, from C3 glomerulopathy to immune-complex glomerulonephritis, an emerging therapeutic target.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — HIF-prolyl-hydroxylase inhibitors (roxadustat) stabilize HIF-1α to boost endogenous erythropoietin production and improve iron handling, an oral alternative to injectable ESAs for the renal anemia of CKD.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Persistently elevated IL-6 in CKD drives hepcidin-mediated anemia and is a major contributor to the accelerated cardiovascular risk and the protein-energy wasting that characterize advanced kidney disease.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — CKD causes an atherogenic dyslipidemia, and the resulting accelerated atherosclerosis makes cardiovascular disease—not progression to kidney failure—the leading cause of death in most patients with chronic kidney disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Failing kidneys lose phosphate and calcium control, and the resulting hyperphosphatemia and secondary hyperparathyroidism drive both renal bone disease and the vascular calcification that worsens CKD cardiovascular mortality.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — GLP-1 receptor agonists reduce albuminuria and slow eGFR decline in diabetic chronic kidney disease, adding a metabolic-pathway renoprotective therapy alongside RAAS blockade and SGLT2 inhibition.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Failing renal clearance raises serum urate, and xanthine-oxidase-generated uric acid contributes both to the gout common in CKD and, debated, to progression itself, the rationale behind urate-lowering trials in kidney disease.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Sustained reactivation of Wnt/β-catenin signaling drives the myofibroblast activation and tubulointerstitial fibrosis that is the final common pathway of progressive chronic kidney disease.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β signals through the SMAD pathway (SMAD4) to drive the renal fibrosis (TGF-β already mapped) that scars glomeruli and interstitium and destroys nephrons in CKD.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — NLRP3-inflammasome activation and IL-1β in the injured kidney sustain the chronic inflammation that accelerates fibrosis and nephron loss in chronic kidney disease.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 orchestrates the antioxidant response that protects tubular cells from the oxidative injury of CKD, and its pharmacological activation (bardoxolone) raises glomerular filtration rate in diabetic kidney disease.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR drives the glomerular and tubular hypertrophy that follows nephron loss — initially adaptive but ultimately accelerating podocyte stress and progressive kidney failure.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR sensing of uremic damage-associated molecular patterns signals through MyD88 to NF-κB, sustaining the chronic innate-immune activation that propels CKD progression.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is a driver and biomarker of the renal and cardiac fibrosis that links CKD to its cardiovascular complications.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling (mTOR mapped) governs podocyte and tubular-cell survival and the hypertrophic responses that shape CKD progression.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF drives mesangial and fibroblast proliferation, contributing to the glomerulosclerosis and tubulointerstitial fibrosis of chronic kidney disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling drives the tubulointerstitial inflammation and fibrotic progression of chronic kidney disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING links tubular cell injury to the sterile inflammation that drives progression of chronic kidney disease.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune-mediated and interferon-driven inflammation of chronic kidney disease.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate podocyte and tubular oxidative-stress defense whose failure accelerates the progression of chronic kidney disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of angiotensin II and growth factors (angiotensin-II and PDGF already mapped) drives the tubulointerstitial fibrosis of chronic kidney disease.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the chronic inflammation and tubular injury that drive progression of chronic kidney disease.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β, within the Wnt/β-catenin signaling that drives tubulointerstitial fibrosis (Wnt already mapped), modulates the progressive fibrosis of chronic kidney disease.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the tubular-cell survival and hypertrophic responses of chronic kidney disease.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic lymphocytes contribute to the immune-mediated tubulointerstitial injury of chronic kidney disease.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling maintains the tubular-cell energy homeostasis whose failure drives the progression of chronic kidney disease.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy maintains the podocyte and tubular-cell homeostasis whose decline accelerates chronic kidney disease.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the tubulointerstitial fibrosis and myofibroblast activation of chronic kidney disease.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the tubular and fibrotic gene programs of chronic kidney disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the tubulointerstitial inflammation and fibrosis of chronic kidney disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the renal fibrosis and leukocyte trafficking of chronic kidney disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the chronic inflammation and fibrosis of chronic kidney disease.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the renal inflammation and fibrosis of chronic kidney disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the renal inflammation and fibrosis of chronic kidney disease.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Metabolic acidosis: the failing kidney cannot excrete the daily acid load or regenerate enough bicarbonate, so protons accumulate, and the resulting metabolic acidosis accelerates bone loss and muscle wasting, treated with oral alkali.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium retention: as kidney function declines, magnesium excretion falls and hypermagnesaemia can develop, while magnesium also modulates the vascular calcification that drives cardiovascular death in chronic kidney disease.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin handling: chronic kidney disease induces peripheral insulin resistance yet also reduces renal insulin clearance, a combination that complicates glucose control and contributes to the metabolic disturbance of uraemia.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiorenal injury: cardiovascular disease is the leading cause of death in chronic kidney disease, and chronically elevated troponin reflects the ongoing myocardial injury of the cardiorenal syndrome even without acute infarction.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Drug clearance and pruritus: many opioids and their active metabolites accumulate in renal failure, requiring dose adjustment, and altered opioid signalling contributes to the distressing uraemic pruritus of advanced chronic kidney disease.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — IgA nephropathy: deposition of galactose-deficient IgA immune complexes in the glomerular mesangium causes IgA nephropathy, one of the commonest primary glomerular diseases progressing to chronic kidney disease worldwide.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron-restricted anaemia: the failing kidney's low erythropoietin (already mapped) and the raised hepcidin (already mapped) of chronic inflammation restrict iron for erythropoiesis, and intravenous iron is a mainstay of managing the anaemia of chronic kidney disease.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Renal prostaglandins: prostaglandins maintain afferent arteriolar tone and renal blood flow, so non-steroidal anti-inflammatory drugs that block them cause acute injury and accelerate chronic kidney disease, a common nephrotoxic exposure.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Inflammatory progression: IL-10 opposes the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) that drive the interstitial inflammation and fibrosis (TGF-beta already mapped) of progressive chronic kidney disease, part of its immune balance.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sodium and volume overload: the failing kidney retains sodium (aldosterone already mapped), and the resulting volume overload drives the hypertension and fluid retention that accelerate chronic kidney disease and its cardiovascular risk.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron-restricted anaemia: the raised hepcidin (already mapped) and the failing erythropoietin (already mapped) of chronic kidney disease restrict iron for erythropoiesis, producing the renal anaemia managed with iron and erythropoiesis-stimulating agents.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Cause and consequence: hypertension is both a leading cause and a near-universal consequence of chronic kidney disease, the renin-angiotensin (already mapped) activation and volume overload creating a vicious cycle that hastens renal decline.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Profibrotic type-2 cytokine: IL-13, with IL-4 (already mapped), is a profibrotic type-2 cytokine that contributes to the renal interstitial fibrosis (TGF-β already mapped) driving the progression of chronic kidney disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 fibrosis: IL-4 drives the M2 macrophages and the type-2 immunity involved in the renal interstitial fibrosis (TGF-β already mapped) that drives the progression of chronic kidney disease.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Renal adipokine retention: leptin is cleared by the kidney and accumulates in chronic kidney disease, contributing to the uraemic cachexia, sympathetic activation and cardiovascular risk.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Uraemic adipokine: adiponectin, with leptin (already mapped), is cleared by and accumulates in the chronic kidney disease, part of the uraemic metabolic-cardiovascular milieu.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Uraemic inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), accumulates in the chronic kidney disease and contributes to the uraemic inflammatory (IL-6 already mapped) milieu.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hepatorenal axis: the liver-kidney axis (the hepatorenal syndrome, the hepcidin already-mapped production driving the renal anaemia) links the liver to the chronic kidney disease.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate renal inflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the tubular stress and DNA damage, contributes to the chronic inflammation and fibrosis of chronic kidney disease.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 renal inflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune-mediated tubulointerstitial inflammation of chronic kidney disease.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension driving the progression of chronic kidney disease.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of chronic kidney disease (and the eosinophilic interstitial nephritis).
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-mediated tubulointerstitial inflammation of chronic kidney disease.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune milieu of chronic kidney disease.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines driving the tubulointerstitial inflammation and the fibroblast (already mapped)-mediated fibrosis of chronic kidney disease.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Renal mast cells: the mast cells infiltrate the interstitium and, via their profibrotic mediators, promote the tubulointerstitial fibrosis (TGF-β already mapped) of chronic kidney disease.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment and the complement-mediated tubulointerstitial injury of chronic kidney disease.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) generate the membrane-attack complex contributing to the glomerular and tubulointerstitial injury of chronic kidney disease.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation causes the C3 glomerulopathy contributing to chronic kidney disease.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Renal anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin and erythropoietin already mapped) of the renal anaemia of chronic kidney disease.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-tubular axis: TSLP, from tubular epithelium under the hypoxia and proteinuria of chronic kidney disease, primes dendritic cells (already mapped) and mast cells (already mapped) toward the Th2/Th17 (already mapped) tubulointerstitial inflammation.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-renal axis: bradykinin, via the intrarenal kallikrein-kinin system and the accumulation from reduced renal clearance, amplifies the vascular permeability and the tubular injury contributing to the progression of chronic kidney disease.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3, C5 and factor-H already mapped) contributing to the C3 glomerulopathy and the immune-complex nephritis of chronic kidney disease.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell renal effector: histamine, released by peritubular mast cells (already mapped) in the interstitium of CKD, promotes vascular permeability and amplifies the pro-inflammatory cytokine milieu (TGF-β and IL-6 already mapped) driving the tubulointerstitial fibrosis of CKD.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Fibrotic ECM scaffold: periostin, expressed by renal fibroblasts (already mapped) under TGF-β (already mapped) stimulation, is a key driver of the extracellular matrix deposition and the interstitial fibrosis-driven nephron loss of chronic kidney disease.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian renoprotection: melatonin, via MT1/MT2 receptors on tubular cells and mesangial cells (already mapped), scavenges ROS (already mapped) and attenuates the oxidative and inflammatory tubulointerstitial injury driving the progression of CKD.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — CKD testosterone: testosterone, via androgen receptors on tubular cells and mesangial cells, attenuates TGF-β (already mapped) and NF-κB (already mapped) renal fibrosis; androgen deficiency amplifies macrophage (already mapped) and IL-6 (already mapped) fibrotic injury of CKD.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — CKD serotonin: serotonin, via 5-HT receptors on mesangial cells and macrophages (already mapped), modulates glomerular (already mapped) haemodynamics; serotonin dysregulation amplifies the TGF-β (already mapped) and NF-κB (already mapped) tubulointerstitial fibrosis of CKD.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — CKD prolactin: prolactin, via PRLR on macrophages (already mapped), promotes TGF-β (already mapped) and NF-κB (already mapped) fibrotic signalling; hyperprolactinaemia amplifies the erythropoietin (already mapped) resistance and iron (already mapped) deficiency anaemia of CKD.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Anti-fibrotic neuropeptide: oxytocin, via OXTR on tubular cells and macrophages (already mapped), attenuates TGF-β (already mapped) and NF-κB (already mapped) fibrotic signalling; oxytocin deficiency amplifies the glomerular (already mapped) and tubulointerstitial injury cascade of CKD.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Hyperfiltration driver: vasopressin, via V2 receptors on renal tubular cells, drives hyperfiltration and renin (already mapped) activation of CKD; vasopressin excess amplifies TGF-β (already mapped) and NF-κB (already mapped) glomerular (already mapped) fibrosis of CKD.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Renal antioxidant: selenium, as GPx in renal tubular cells and macrophages (already mapped), scavenges CKD oxidative-stress; selenium deficiency amplifies the NF-κB (already mapped) and TGF-β (already mapped) tubulointerstitial fibrosis and hepcidin (already mapped) anaemia of CKD.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — CKD zinc: zinc supports macrophage (already mapped) anti-inflammatory resolution and tubular cell integrity; zinc deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) glomerular fibrosis and hepcidin (already mapped)-mediated anaemia in chronic kidney disease.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — CKD copper: copper-dependent SOD in renal tubular cells and macrophages (already mapped) counters ROS; copper deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) tubulointerstitial fibrosis and hepcidin (already mapped) anaemia of chronic kidney disease.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — CKD iodine: thyroid hormones regulate macrophage (already mapped) and mesangial cells (glomerulus already mapped); thyroid deficiency amplifies TGF-β (already mapped) and NF-κB (already mapped) fibrosis and erythropoietin (already mapped) suppression of CKD.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — CKD chloride: chloride, via CFTR and ClC-Ka/Kb in renal tubular cells and macrophages (already mapped), regulates acid-base balance; chloride dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) tubular injury and fibrosis of CKD.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — carbon metabolism in renal tubular cells and macrophage (already mapped) drives oxidative phosphorylation; carbon dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrosis and hepcidin (already mapped) cascade in CKD.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — sulfur, as glutathione precursor in renal tubular cells and macrophage (already mapped), counters oxidative stress; sulfur deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) tubulointerstitial fibrosis cascade in CKD.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — nitrogen, as urea-cycle substrate in renal tubular cells and macrophage (already mapped), governs uraemic toxin clearance; nitrogen retention amplifies NF-κB (already mapped) and TGF-β (already mapped) fibrosis cascade in CKD.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — CKD oxygen: oxygen via ROS from renal tubular cells (already mapped) and macrophages (already mapped) modulates redox homeostasis; oxygen excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — CKD pd-1: PD-1 on t-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses renal immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — CKD rankl: RANKL from renal tubular cells (already mapped) and macrophages (already mapped) modulates bone-kidney mineral axis; RANKL excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — CKD il-2: IL-2 on t-cells (already mapped) and macrophages (already mapped) amplifies renal immune activation; il-2 excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — CKD fibronectin: fibronectin in renal tubular cells (already mapped) and fibroblasts (already mapped) promotes ECM deposition; fibronectin excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — CKD igf-1: IGF-1 on renal tubular cells (already mapped) and macrophages (already mapped) modulates renal hypertrophy; igf-1 excess amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — CKD notch: Notch in renal tubular cells (already mapped) and macrophages (already mapped) regulates renal cell fate; Notch dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) fibrosis cascade in CKD.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — CKD activin-a: activin-A in renal tubular cells (already mapped) and fibroblasts (already mapped) promotes renal fibrosis; activin-A dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) cascade in CKD.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — CKD cgrp: CGRP in renal endothelial cells (already mapped) and macrophages (already mapped) modulates renal vascular tone; CGRP dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) and VEGF (already mapped) cascade in CKD.

## Pathology

**Acute-on-chronic kidney disease (AoCKD):** Superimposed AKI in CKD — from contrast, NSAIDs, ACEi in dehydration, infection, obstruction — accelerates irreversible nephron loss; prevention requires careful drug management and hydration.

**Hyperkalemia:** Life-threatening in advanced CKD (G4-G5); exacerbated by ACEi/ARB, aldosterone antagonists, acidosis; managed with dietary K⁺ restriction, patiromer/sodium zirconium cyclosilicate (K⁺ binders), correction of acidosis, and ultimately dialysis.

**Uremic encephalopathy:** End-stage uremia → asterixis, myoclonus, seizures, coma; an emergency indication for dialysis initiation.

**Nephrotic-range proteinuria:** >3.5 g/day (or >3500 mg/g Cr) → albumin loss → hypoalbuminemia → edema, thrombosis risk, hyperlipidemia; occurs with primary glomerulopathies (minimal change, membranous, FSGS).

**CKD and drug dosing:** Reduced GFR requires dose adjustment for renally cleared drugs (antibiotics, anticoagulants, digoxin, metformin [contraindicated <30 mL/min], SGLT2i [less efficacy <20-30 mL/min]).

[^kdigo-2012-ckd]: KDIGO CKD Work Group. KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. *Kidney Int Suppl.* 2013;3(1):1-150. [doi:10.1038/kisup.2012.73](https://doi.org/10.1038/kisup.2012.73)
[^levey-2012-ckd-lancet]: Levey AS, Coresh J. Chronic kidney disease. *Lancet.* 2012;379(9811):165-180. [doi:10.1016/S0140-6736(11)60178-5](https://doi.org/10.1016/S0140-6736(11)60178-5) · [PubMed 21840587](https://pubmed.ncbi.nlm.nih.gov/21840587/)
[^coresh-2007-prevalence]: Coresh J, Selvin E, Stevens LA, et al. Prevalence of chronic kidney disease in the United States. *JAMA.* 2007;298(17):2038-2047. [doi:10.1001/jama.298.17.2038](https://doi.org/10.1001/jama.298.17.2038) · [PubMed 17986697](https://pubmed.ncbi.nlm.nih.gov/17986697/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
