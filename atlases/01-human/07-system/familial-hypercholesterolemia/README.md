---
schema: human-scale-entry/v1
id: familial-hypercholesterolemia
name: Familial Hypercholesterolemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Familial hypercholesterolemia (FH) is an autosomal dominant disorder; LDLR mutations (most common), APOB R3527Q, or PCSK9 GOF mutations → LDL-C >190 mg/dL; premature atherosclerosis and MI (HoFH: untreated → MI by age 20). Statins + PCSK9 inhibitors are standard treatment."
aliases: ["FH", "heterozygous FH", "HeFH", "homozygous FH", "HoFH", "familial hypercholesterolaemia", "autosomal dominant hypercholesterolemia", "ADH"]
sources:
  - id: goldstein-1985-ldlr-nobel
    type: peer-reviewed
    cite: "Goldstein JL, Brown MS. The LDL receptor. Arterioscler Thromb Vasc Biol. 2009;29(4):431-438."
    doi: "10.1161/ATVBAHA.108.179564"
    pmid: "19299327"
    url: "https://doi.org/10.1161/ATVBAHA.108.179564"
  - id: raal-2020-inclisiran-fh
    type: peer-reviewed
    cite: "Raal FJ, Kallend D, Ray KK, et al. Inclisiran for the Treatment of Heterozygous Familial Hypercholesterolemia. N Engl J Med. 2020;382(16):1520-1530."
    doi: "10.1056/NEJMoa1913805"
    pmid: "32197277"
    url: "https://doi.org/10.1056/NEJMoa1913805"
  - id: watts-2020-hzfh-guidelines
    type: clinical-guideline
    cite: "Watts GF, Gidding SS, Hegele RA, et al. International Atherosclerosis Society guidance for implementing best practice in the care of familial hypercholesterolaemia. Nat Rev Cardiol. 2023;20(12):845-869."
    doi: "10.1038/s41569-023-00892-0"
    pmid: "37322181"
    url: "https://doi.org/10.1038/s41569-023-00892-0"
cross_links:
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "PCSK9 GOF mutations cause autosomal dominant FH (ADH3); evolocumab and alirocumab reduce LDL-C 50-60% add-on to statins; inclisiran (PCSK9 siRNA) reduces LDL-C ~50% with Q6M dosing; standard of care for FH not at LDL goal on maximally tolerated statin."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "FH accelerates atherosclerosis; HeFH untreated: 20× higher CVD risk; coronary atherosclerosis, tendon xanthomas, and xanthelasma are hallmarks; cumulative LDL-C burden predicts events; early statin initiation reduces atherosclerotic events in HeFH."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "FH results from impaired LDLR-mediated cholesterol clearance; LDLR mutations → fewer surface receptors → LDL-C >190 mg/dL (HeFH) or >500 mg/dL (HoFH LDLR null); excess cholesterol in macrophages → foam cells → atheromatous plaque."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Hepatocytes express >90% of plasma LDLR; LDLR-mediated LDL endocytosis is the primary clearance route; SREBP-2 upregulates LDLR after statin treatment; liver transplant in HoFH normalizes LDL-C — confirming hepatocytic LDLR as the disease driver."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "In FH, chronically elevated LDL-C → macrophage scavenger receptor (SR-A, CD36) uptake of oxidized LDL → foam cell formation; foam cells are the histological hallmark of the atheromatous plaque; FH macrophages exhibit exaggerated ox-LDL uptake vs. normolipidemic controls."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "FH accelerates carotid and cerebrovascular atherosclerosis; HeFH patients have elevated carotid intima-media thickness (cIMT) and higher stroke risk vs. general population; statin + PCSK9 inhibitor reduces cIMT progression and ischemic stroke incidence in FH cohorts."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Familial hypercholesterolemia is defined by its toll on the heart: lifelong high LDL drives premature coronary disease — heterozygotes infarct in their 40s-50s while homozygotes can have MIs and aortic-valve stenosis in childhood; early intensive LDL lowering is lifesaving."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Atherosclerosis in FH starts at the endothelium: the lifelong excess of LDL infiltrates and is retained in the subendothelial intima, where oxidation activates endothelial cells to recruit monocytes — repeated for decades at FH's LDL levels, this builds plaque far earlier."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Vascular smooth muscle cells shape the FH atheroma: they migrate from the media into the intima, take up modified LDL to become foam cells, and lay down the collagen fibrous cap whose stability — or rupture — determines whether a plaque stays silent or causes infarction."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: treated-by
    note: "Statins are the cornerstone of FH treatment: by inhibiting HMG-CoA reductase they upregulate hepatic LDL receptors to clear LDL, but FH patients—especially homozygotes with few functional receptors—often need high-intensity statins plus ezetimibe and PCSK9 inhibitors."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is central to FH: hepatocyte LDL receptors normally clear ~70% of circulating LDL, so the LDLR (or APOB/PCSK9) mutations of FH cripple this clearance → lifelong high LDL; the liver is thus the target of statins, PCSK9 inhibitors, apheresis and gene therapy."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "FH and hypertension are multiplicative cardiovascular risk factors: lifelong high LDL accelerates atherosclerosis while raised blood pressure adds shear stress and endothelial injury, so an FH patient who is also hypertensive faces especially early coronary disease."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Familial hypercholesterolemia is a lifelong assault on the cardiovascular system: from birth very high LDL accelerates atherosclerosis, so untreated heterozygotes get coronary disease decades early and homozygotes in childhood—early statin/PCSK9 therapy is essential."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Familial hypercholesterolemia and type 2 diabetes multiply cardiovascular risk together: FH's lifelong LDL burden plus diabetic dyslipidemia compound atherosclerosis—and although statins slightly raise diabetes risk, their cardiovascular benefit in FH far outweighs it."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Familial hypercholesterolemia and NASH are distinct lipid disorders of the liver: FH is a receptor defect that floods blood with LDL but spares the liver, while NASH is hepatic fat from insulin resistance—high LDL with a normal liver differs from fatty liver."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Familial hypercholesterolemia causes premature coronary disease that leads to heart failure: lifelong sky-high LDL drives early severe atherosclerosis and heart attacks, so untreated FH causes ischemic cardiomyopathy decades early."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Familial hypercholesterolemia and obesity stack cardiovascular risk: FH is a genetic LDL-receptor defect causing very high cholesterol, while obesity adds insulin resistance and inflammation—together compounding the premature atherosclerosis FH drives."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Familial hypercholesterolemia and chronic kidney disease are both potent cardiovascular risk amplifiers: FH from extreme LDL, CKD from vascular calcification and dyslipidemia, so an FH patient who also develops CKD faces compounded atherosclerotic risk."
  - target: 01-human/03-molecular/apoe
    relation: connects-to
    note: "FH and APOE both shape blood cholesterol but differently: FH is a single-gene defect in LDL clearance causing severe lifelong hypercholesterolemia, while APOE variants modify lipid levels and cardiovascular risk—monogenic versus polygenic cholesterol disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Coronary artery calcium scoring helps gauge risk in FH: lifelong high LDL drives calcified atherosclerotic plaque, so a CT calcium score quantifies accumulated arterial damage and refines who needs the most aggressive lipid lowering."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "FH's silent arterial damage is revealed by photon-based imaging: low-dose CT uses X-ray photons to measure coronary calcium, turning invisible decades of LDL-driven plaque buildup into a number that guides how intensively to treat."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Familial hypercholesterolemia writes itself on the skin: lifelong high LDL deposits cholesterol as tendon xanthomas (Achilles, knuckles) and eyelid xanthelasma, so these fatty bumps are physical clues that prompt lipid testing and family screening."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye flags familial hypercholesterolemia: a corneal arcus—a white lipid ring around the iris—appearing before age 45 strongly suggests it, so this ocular sign, like xanthomas, helps catch the inherited high cholesterol early enough to prevent heart attacks."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cultured skin fibroblasts revealed FH's cause: studying patients' fibroblasts, Brown and Goldstein discovered the LDL receptor and how its loss blocks cholesterol uptake—the Nobel work that explained FH and led to statins and PCSK9 inhibitors."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "FH shows that LDL isn't the whole story—inflammation matters too: IL-6-driven inflammation in the artery wall adds 'residual risk' on top of high cholesterol, so anti-inflammatory therapy (colchicine, IL-targeted drugs) complements LDL-lowering in atherosclerosis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Atherosclerosis in FH is partly an immune disease: T-helper cells infiltrate the cholesterol-laden plaque and stoke inflammation that destabilizes it, so the early plaques of FH reflect adaptive immunity, not just passive lipid buildup."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Whether FH's plaques kill depends on collagen: a thick collagen fibrous cap (laid down by smooth muscle) keeps a plaque stable, while a thin one ruptures to cause heart attacks—so plaque collagen, not just cholesterol level, decides the danger."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "FH's danger is realized when platelets meet a ruptured plaque: the lifelong high LDL builds plaques whose cap can tear, exposing tissue that triggers platelets to clot and block the artery, the final step from cholesterol to heart attack or stroke."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "FH ultimately starves the heart of oxygen: narrowing coronary arteries cut blood flow, so demand outstrips supply and the muscle becomes ischemic, causing the angina and infarction that make untreated FH so deadly so young."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "FH's growing plaques sprout fragile vessels via VEGF: as plaques thicken they outgrow their oxygen supply and release VEGF to recruit leaky new microvessels, which bleed into the plaque and destabilize it, raising rupture risk."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "FH's atherosclerosis reaches the kidneys: cholesterol-laden plaque narrows the renal arteries, which can drive resistant high blood pressure and slowly starve the kidneys, adding renovascular disease to FH's vascular toll."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "FH plaques are fed from the bone marrow: it supplies the monocytes that become plaque foam cells, and age-related clonal mutations in marrow cells (clonal hematopoiesis) further inflame and accelerate the atherosclerosis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils inflame FH's arteries: drawn into cholesterol-rich plaque, they release enzymes and DNA nets (NETs) that amplify inflammation and erode the fibrous cap, helping tip a stable plaque toward the clot that causes a heart attack."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "FH's lifelong high LDL threatens the brain too: it accelerates carotid and cerebral atherosclerosis, raising the risk of ischemic stroke and vascular cognitive decline, not just heart attacks."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "FH deposits cholesterol in connective tissue: Achilles and knuckle tendon xanthomas are a hallmark, fibrous tissue infiltrated by lipid-laden cells, mirroring the fibrous cap that walls off an artery plaque."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α destabilizes FH's plaques: plaque macrophages pour out this cytokine, whose inflammation thins the fibrous cap and helps tip a quiet lesion toward the rupture that triggers a heart attack."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals where the excess cholesterol piles up: macrophages gorge on LDL until they become lipid-stuffed foam cells, and needle-shaped cholesterol clefts stud the xanthomas and plaques that scar FH's arteries and tendons."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Premature atherosclerosis can starve the gut: FH's early, severe plaque burden narrows the mesenteric arteries too, so chronic intestinal angina — abdominal pain after eating — can join its better-known heart and brain disease."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "FH's cholesterol-laden aorta can shower emboli: fragments of plaque break off as cholesterol crystals that lodge in small vessels of the spleen, kidneys, and skin, a multi-organ embolic syndrome of advanced disease."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "FH leaves cholesterol in the tendons: firm Achilles and knuckle tendon xanthomas are a near-pathognomonic sign, and the statins that treat it can in turn cause muscle aches and, rarely, breakdown — both tying the disease to the musculoskeletal system."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Lifelong statin therapy nudges the pancreas: the drugs slightly raise the risk of new-onset diabetes, and in forms with high triglycerides too, the excess fat can inflame the pancreas into pancreatitis."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy forces a treatment pause: statins are avoided in pregnancy for fear of harming the fetus, so women with FH must stop them while trying to conceive and during gestation, leaving their high LDL untreated for months."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody now slashes the LDL: PCSK9-inhibitor monoclonal antibodies (evolocumab, alirocumab) free up the liver's LDL receptors, dramatically lowering cholesterol in FH patients who can't reach target on statins alone."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid must be cleared first: hypothyroidism is a common secondary cause of high cholesterol that both mimics and worsens FH, so thyroid function is checked before and during treatment of the inherited disorder."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Diet still pulls its weight: soluble fiber binds bile acids to lower LDL, so a high-fiber, low-saturated-fat pattern is the dietary foundation on which the statins and antibodies of FH treatment build."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The gut is the body's other cholesterol tap: the small intestine absorbs dietary and biliary cholesterol via NPC1L1, the target of ezetimibe — a second lever pulled alongside statins when the liver pathway alone can't lower FH's LDL enough."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "High cholesterol travels with a sticky, clot-prone blood: FH raises fibrinogen and other prothrombotic factors, so the atherosclerotic plaques it builds are more likely to clot off into the heart attacks and strokes that strike early."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Atherosclerosis is also an immune disease: cytotoxic T cells infiltrate the lipid-laden plaque and, alongside the macrophages, drive the inflammation that destabilizes it, so FH's lifelong LDL load is fought partly in the immune cells of the artery wall."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Trapped LDL ignites a master inflammatory switch: oxidized lipid in the artery wall activates NF-κB in endothelial cells and macrophages, turning on the adhesion molecules and chemokines that recruit the inflammation accelerating FH's plaques."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells lurk in the plaque: they cluster in atherosclerotic lesions and release proteases and mediators that destabilize the fibrous cap, contributing to the rupture risk behind FH's early heart attacks."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "The thyroid sets LDL-receptor levels: thyroid hormone drives expression of the very receptor FH lacks, so hypothyroidism worsens the cholesterol and must be corrected before judging the genetic disease's severity."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The heart muscle pays for the genes: lifelong sky-high LDL gives FH patients premature coronary disease and heart attacks, killing cardiomyocytes decades early — the reason untreated homozygous FH can be fatal in childhood."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Immune cells gorge on the excess cholesterol: dendritic cells and macrophages in the artery wall engulf oxidized LDL to become lipid-laden foam cells and present lipid antigens, an immune arm of the atherogenesis FH accelerates."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its prothrombotic milieu reaches the veins too: beyond arterial disease, the raised fibrinogen and endothelial dysfunction of severe hypercholesterolemia are linked to a modestly higher risk of venous thromboembolism."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Blocked leg arteries starve the wound: the premature peripheral arterial disease of FH cuts blood flow to the limbs, producing ischemic, slow-healing ulcers and, in critical limb ischemia, gangrene."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A lifelong genetic verdict weighs on the mind: living with an inherited high risk of early heart attack, cascade family testing and lifelong therapy — sometimes with statin-related muscle symptoms — carries a real psychological burden."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Lipid and urate disturbances cluster: dyslipidemia and hyperuricemia frequently coexist, and FH patients carry the cardiometabolic context — and statin or niacin therapy effects on urate — that associate it with gout."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Cholesterol and cerebral atherosclerosis reach the mind: the lifelong high LDL of FH accelerates small- and large-vessel brain disease, contributing to vascular and mixed Alzheimer-type cognitive decline."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its long-term statins can irritate nerves: alongside the more common myalgia, prolonged high-intensity statin therapy used to control FH has been linked in some patients to a peripheral neuropathy with neuropathic pain."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A genetic verdict of early heart disease breeds worry: learning of an inherited condition that threatens premature heart attacks, often after a relative's early death, fosters chronic health anxiety in FH families."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Excess cholesterol deposits in skin and tendons: FH produces tendon xanthomas over the Achilles and knuckles, eyelid xanthelasma and a corneal arcus, visible lipid deposits that are diagnostic clues."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The liver is the organ of the disease and its treatment: hepatic LDL receptors clear cholesterol and are defective in FH, and the statins used to treat it act on and are monitored for toxicity in the liver."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Cholesterol is the substrate of the steroid hormones: the lipid metabolism deranged in FH supplies the precursor for adrenal and gonadal steroidogenesis, and statins carry a modest dysglycaemia signal."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its plaques narrow the renal arteries: premature atherosclerosis in FH affects the renal arteries, causing renovascular hypertension and ischaemic nephropathy with declining kidney function."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It hardens the arteries to the brain: lifelong high LDL drives early carotid and cerebral atherosclerosis, raising the risk of transient ischaemic attacks and ischaemic stroke at a young age."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its atherosclerosis is an inflammatory process: chronically elevated LDL is taken up by arterial macrophages into foam cells, driving the immune-cell-rich plaques that FH accelerates."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Once arteries are damaged, antiplatelet cover follows: aspirin is added for secondary prevention after the premature heart attacks and strokes that untreated FH causes."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "They protect the heart after early infarction: ACE inhibitors support left-ventricular function after the premature myocardial infarction FH produces and treat the hypertension that compounds its vascular risk."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet adds a modest lever: omega-3 supplements mainly lower triglycerides and complement statins, though they do little for the very high LDL that defines FH."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "This is where it does its damage: lifelong high LDL drives cholesterol into the arterial wall, building the atherosclerotic plaque that causes premature coronary disease in familial hypercholesterolaemia."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Cholesterol leaves tissues through it: HDL-mediated reverse cholesterol transport drains peripheral cholesterol via the lymphatics, and FH's deposits surface as tendon and skin xanthomas when that clearance is overwhelmed."
  - target: 03-medicine/02-traditional/berberine
    relation: connects-to
    note: "A natural compound that lowers LDL: berberine upregulates the LDL receptor and modestly reduces cholesterol, studied as an adjunct in people who cannot tolerate or fully respond to statins."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Modern LDL-lowering beyond statins: PCSK9-inhibitor antibodies (evolocumab, alirocumab), the siRNA inclisiran and ANGPTL3-blocking evinacumab dramatically cut LDL in familial hypercholesterolaemia when statins alone fall short."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The defect lives in the liver: FH stems from faulty LDL receptors on hepatocytes of the liver lobule that normally clear LDL from blood, so cholesterol accumulates from birth — and the liver is the target of statins and PCSK9 therapy."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It infarcts the heart young: untreated familial hypercholesterolaemia drives accelerated coronary atherosclerosis and myocardial infarction in the third to fifth decades, decades earlier than ordinary high cholesterol."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Early ischaemia hits the wiring: the premature, severe coronary atherosclerosis of untreated FH damages the conduction system, predisposing young adults to ventricular arrhythmia and sudden cardiac death."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Cholesterol feeds steroid hormones: the adrenal cortex takes up LDL cholesterol through the very LDL receptor defective in FH to build cortisol and aldosterone, tying lipoprotein handling to steroidogenesis."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Lipids injure the kidney too: chronic LDL excess drives atherosclerotic renovascular disease and lipid-mediated glomerular injury, so severe untreated FH accelerates kidney as well as heart disease."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "Cholesterol on the valves: severe (especially homozygous) familial hypercholesterolaemia deposits cholesterol in the aortic valve and root, causing supravalvular and calcific aortic stenosis of the endocardium."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Where dietary cholesterol enters: the intestinal epithelium absorbs cholesterol via NPC1L1, the target of ezetimibe—an FH therapy that complements statins by cutting absorption alongside reduced synthesis."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Compounded cardiovascular risk: when familial hypercholesterolaemia coexists with diabetes such as type 1, the lipid and glycaemic insults multiply atherosclerotic risk, demanding aggressive LDL lowering."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "Two routes to early heart attacks: familial hypercholesterolaemia drives premature atherosclerosis through lifelong high LDL, while Werner syndrome reaches the same early coronary disease through accelerated cellular ageing."
  - target: 01-human/07-system/marfan-syndrome
    relation: connects-to
    note: "Inherited cardiovascular disease, different walls: familial hypercholesterolaemia attacks the coronary arteries with cholesterol, while Marfan weakens the aortic wall through fibrillin loss—two autosomal-dominant routes to cardiac death."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Tendon xanthomas: familial hypercholesterolaemia deposits cholesterol in tendons—classically the Achilles and finger-extensor tendons at their cortical-bone insertions—forming the xanthomas that are a clinical hallmark."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Early endothelial injury: lifelong high LDL in familial hypercholesterolaemia impairs endothelial nitric oxide production from childhood, the first step toward the premature atherosclerosis that defines the disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: oxidised LDL accumulating in the arterial wall induces CCL2, drawing in the monocytes that become the foam cells of the accelerated plaques of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vascular tone imbalance: the endothelial dysfunction of familial hypercholesterolaemia shifts the balance toward endothelin-1 vasoconstriction, compounding the atherosclerotic narrowing of the arteries."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Cholesterol-crystal inflammasome: cholesterol crystals in plaque macrophages activate the NLRP3 inflammasome, releasing IL-1β that propels the accelerated atherosclerosis of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Intraplaque hypoxia: as the lipid-rich plaques of familial hypercholesterolaemia thicken, their cores turn hypoxic and stabilise HIF-1α, driving the neovascularisation and necrotic-core expansion that destabilise them."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Myeloid alarmin: S100A8/A9 from activated plaque neutrophils and monocytes amplifies arterial inflammation and is a circulating biomarker of the high cardiovascular risk of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Oxidised-LDL inflammation: oxidised LDL and AGEs signalling through RAGE on endothelium and macrophages amplify the NF-κB-driven arterial inflammation that accelerates atherosclerosis in familial hypercholesterolaemia."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Atherothrombosis: rupture of the lipid-rich plaques of familial hypercholesterolaemia exposes tissue factor that generates thrombin, the coagulation step that converts a plaque into the occlusive clot of an early myocardial infarction."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement in plaque: C3 and the complement cascade are activated within the atherosclerotic lesions of familial hypercholesterolaemia, contributing to the chronic vascular inflammation that drives plaque progression."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Residual inflammatory risk: IL-1β from cholesterol-crystal-activated plaque macrophages drives atherosclerotic inflammation, and the CANTOS trial showed IL-1β blockade cuts cardiovascular events independent of lipid lowering, relevant to FH's inflammatory burden."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Necrotic-core formation: caspase-3-mediated apoptosis of lipid-laden foam cells, when their clearance fails, builds the necrotic lipid core of the atherosclerotic plaque, the unstable centre prone to the rupture that causes the premature heart attacks of FH."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Arterial calcification: advanced atherosclerotic plaques in familial hypercholesterolaemia calcify, the calcium deposition measured by coronary-artery-calcium scoring that quantifies plaque burden and refines cardiovascular-risk prediction."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Neointima formation: PDGF drives the migration and proliferation of the vascular smooth-muscle cells (already mapped) into the atherosclerotic plaque, building the neointima of the accelerated atherosclerosis of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Plaque-cap stability: TGF-β regulates the collagen synthesis and fibrous-cap stability of atherosclerotic plaques, opposing the inflammatory destabilisation that causes the early myocardial infarctions of FH."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Plaque complement: complement activation by cholesterol-rich plaque (C3 already mapped, through C5) amplifies the vascular inflammation of the atherosclerosis driven by familial hypercholesterolaemia."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate plaque inflammation: TLR sensing of oxidised LDL signals through MyD88 to NF-κB, igniting the sterile innate-immune inflammation that converts the lipid burden of FH into progressive atherosclerotic plaque."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative defence: NRF2 mounts the antioxidant response that counters the oxidative modification of the LDL accumulating in FH — the oxidised LDL that, unopposed, drives foam-cell formation and endothelial injury."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Endothelial protection: the PI3K-AKT-eNOS axis sustains endothelial nitric-oxide production, a vasoprotective pathway statins enhance pleiotropically and that the lipid excess of FH progressively impairs."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 marks the lipid-laden plaque macrophages and promotes the vascular inflammation accelerating atherosclerosis in familial hypercholesterolemia."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signalling regulates macrophage autophagy and efferocytosis in the atherosclerotic plaque, shaping lesion progression in familial hypercholesterolemia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Oxidized-LDL and growth-factor ERK-MAPK signalling drives the smooth-muscle proliferation and foam-cell responses of accelerated atherosclerosis in FH."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the vascular inflammation that accelerates atherosclerotic plaque progression in familial hypercholesterolemia."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) shapes the fibrous-cap formation and plaque stability of the accelerated atherosclerosis of familial hypercholesterolemia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cholesterol-crystal and mitochondrial DNA engagement of cGAS-STING amplifies the sterile inflammation of the atherosclerotic plaque in familial hypercholesterolemia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate hepatic lipid metabolism and the endothelial oxidative-stress response relevant to the accelerated atherosclerosis of familial hypercholesterolemia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the macrophage inflammatory activation within the cholesterol-laden atherosclerotic plaques of familial hypercholesterolemia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2-STAT cytokine signaling (IL-6-STAT3 already mapped) amplifies the vascular inflammation driving premature atherosclerosis in familial hypercholesterolemia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the inflammatory and metabolic signaling in the vascular wall that accelerates atherosclerosis in familial hypercholesterolemia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, a regulator of hepatic and vascular lipid metabolism, participates in the metabolic context of familial hypercholesterolemia."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic T cells in the atherosclerotic plaque contribute to the vascular inflammation and plaque instability of familial hypercholesterolemia."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the endothelial and macrophage responses to the LDL burden of familial hypercholesterolemia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy (including lipophagy) modulates the macrophage cholesterol handling and foam-cell formation in familial hypercholesterolemia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte recruitment accelerates the atherosclerosis of familial hypercholesterolemia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the lipid-metabolism and vascular-inflammation gene programs relevant to familial hypercholesterolemia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the accelerated atherosclerosis of familial hypercholesterolemia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the endothelial and smooth-muscle-cell responses of the atherogenesis of familial hypercholesterolemia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the vascular inflammation of the atherosclerosis of familial hypercholesterolemia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the atherosclerotic vascular inflammation of familial hypercholesterolemia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the lipid-metabolism and vascular gene programs relevant to familial hypercholesterolemia."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Premature infarction: untreated familial hypercholesterolaemia causes early myocardial infarction, and troponin release marks the myocardial injury of the coronary events that are its leading cause of death, driving aggressive lipid lowering from childhood."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "LDL oxidation: xanthine-oxidase-derived reactive oxygen species help oxidise the excess LDL of familial hypercholesterolaemia, and oxidised LDL is the form avidly taken up by macrophages (already mapped) to form the foam cells of atheroma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Plaque adaptive immunity: atherosclerosis in familial hypercholesterolaemia has an adaptive immune component, with MHC class II presentation of oxidised-LDL and ApoB peptides to T cells shaping the inflammatory plaque beyond the lipid burden."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Plaque T-cell response: IL-2-driven T-cell activation (MHC class II already mapped) participates in the adaptive immune inflammation of the atherosclerotic plaque, contributing to lesion progression in familial hypercholesterolaemia beyond the lipid drive."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Atheroprotective regulation: the anti-inflammatory cytokine IL-10 restrains plaque inflammation, and the balance between it and the pro-inflammatory cytokines already mapped shapes the stability of the atherosclerotic lesions of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences: estrogen is cardioprotective and lowers LDL, so premenopausal women with familial hypercholesterolaemia are relatively protected until menopause, contributing to the later onset of coronary disease in affected women."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane and plaque thrombosis: the prostaglandin balance shifts toward the prothrombotic thromboxane on the atherosclerotic plaques of familial hypercholesterolaemia, part of why aspirin is used to prevent the coronary events."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Plaque-rupture thrombosis: when a plaque of familial hypercholesterolaemia ruptures, von Willebrand factor mediates the platelet adhesion that, with thrombin and fibrinogen (already mapped), forms the occlusive thrombus of myocardial infarction."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic amplification: although familial hypercholesterolaemia is a monogenic LDL disorder, coexisting insulin resistance and the metabolic syndrome compound its atherogenic risk, adding to the burden of the very high LDL."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Plaque macrophage polarisation: IL-4 polarises the plaque macrophages (already mapped) toward an M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the atherosclerotic lesions driven by the very high LDL of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine amplification: leptin, from adipose tissue, adds an inflammatory and atherogenic contribution (insulin already mapped) that compounds the cardiovascular risk of the monogenic LDL elevation in familial hypercholesterolaemia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Vasoprotective adipokine: adiponectin, with leptin (already mapped), is a vascular-protective adipokine whose fall in the metabolic syndrome removes a brake on the atherogenesis driven by familial hypercholesterolaemia."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Plaque type-2 arm: IL-13, with IL-4 (already mapped), modulates the M2 macrophage (already mapped) arm of the inflammation of the atherosclerotic plaque driven by familial hypercholesterolaemia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Atherogenic adipokine: resistin, with leptin and adiponectin (already mapped), is a pro-inflammatory adipokine that adds to the atherogenic-inflammatory (IL-6 already mapped) milieu compounding the cardiovascular risk of familial hypercholesterolaemia."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "LDL oxidation: iron catalyses the oxidation of the LDL (cholesterol already mapped) that generates the oxidised LDL taken up by the foam-cell macrophages (already mapped), part of the oxidative atherogenesis of familial hypercholesterolaemia."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial dysfunction: the LDL (cholesterol already mapped) retention in the arterial intima and the endothelial dysfunction (nitric oxide already mapped) initiate the atherosclerosis of familial hypercholesterolaemia."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "LDLR hepatocytes: the hepatocytes express the LDL receptor (PCSK9 already mapped) that clears the LDL; the hepatocyte LDLR defect is the disease of familial hypercholesterolaemia and the target of the gene therapy."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Fibrous cap: the vascular smooth-muscle cells migrate and form the fibrous cap (collagen already mapped) of the atherosclerotic plaque of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 plaque inflammation: the IFN-γ of the plaque T cells is the type-II interferon arm of the Th1-driven inflammation that destabilises the atherosclerotic plaque of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the atherosclerotic plaque inflammation of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate plaque interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the cholesterol-crystal and cellular stress, amplifies the macrophage (already mapped) inflammation of the atheroma of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of the atherosclerotic plaque of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the atherosclerotic plaque inflammation of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/mast-cell arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension whose mast cells contribute to the atheroma of familial hypercholesterolaemia."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate plaque arm: the NK cells (perforin already mapped) infiltrate the atherosclerotic plaque and are part of the innate immune contribution to the atherosclerosis of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid recruitment into the atherosclerotic plaque of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active on the oxidised LDL and the atheroma of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the oxidised LDL and C-reactive protein in the atheroma of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Atheroma matricellular: osteopontin, produced by the foam-cell macrophages (already mapped), is a matricellular mediator of the plaque inflammation and the vascular calcification of familial hypercholesterolaemia."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Plaque iron: transferrin, the iron carrier, reflects the disordered iron handling and the intraplaque-haemorrhage iron that aggravates the oxidative injury of the atheroma of familial hypercholesterolaemia."
---

# Familial Hypercholesterolemia

## Overview

**Familial hypercholesterolemia (FH)** is the most common single-gene disorder causing premature cardiovascular disease, characterized by **lifelong markedly elevated LDL-cholesterol (LDL-C)** due to impaired receptor-mediated clearance of LDL particles from the circulation [^goldstein-1985-ldlr-nobel].

FH is a **monogenic autosomal dominant disorder** caused by mutations in three genes:
1. **LDLR (LDL receptor gene; chr19p13.2):** >2,500 pathogenic variants; accounts for ~85-90% of genetically confirmed FH; loss-of-function → reduced or absent LDLR surface expression → LDL not cleared from plasma
2. **APOB (apolipoprotein B gene; chr2p24.1):** Most common variant R3527Q (European); APOB protein is the ligand for LDLR; R3527Q reduces LDLR binding affinity → LDL clearance ~50% reduced
3. **PCSK9 (chr1p32.3):** Gain-of-function mutations (D374Y most severe; S127R; F216L) → accelerated LDLR degradation → fewer surface LDLR → elevated LDL-C; accounts for ~2-3% of FH

**Prevalence:**
- **Heterozygous FH (HeFH):** 1 in 200-250 in the general population (previously estimated at 1 in 500, upward revision from genomic data); ~30 million people globally
- **Homozygous FH (HoFH):** 1 in ~300,000-400,000; biallelic LDLR mutations; two pathogenic alleles
- **Severely underdiagnosed:** Only ~10-20% of FH patients are diagnosed in most countries despite cascade screening programs
- **Founder effects:** High prevalence in Afrikaners (~1:100), French Canadians (~1:270), Lebanese (~1:170), Ashkenazi Jews — due to founder mutations in LDLR

**Clinical consequences without treatment:**
- HeFH: LDL-C typically 190-300 mg/dL; cumulative exposure → first MI at age 40-50 (men) or 50-60 (women); 20× higher CHD risk vs. age-matched general population
- HoFH: LDL-C typically 500-1000+ mg/dL; MI by age 10-20 years in null-null LDLR mutations; generalized xanthomas in childhood; aortic valve stenosis from lipid deposition

## Structure

### Genetic mechanisms — LDL receptor pathway

**Normal LDLR cycle:**
1. LDLR synthesized in ER → glycosylated → cell surface (~10,000 receptors/hepatocyte)
2. LDLR binds apoB-100 (LDL) or apoE (VLDL remnant/IDL) via EGF-precursor domain
3. LDLR-LDL complex → clathrin-coated pit → endocytosis → early endosome
4. Acidic endosomal pH → LDLR-LDL dissociation → LDLR recycled to cell surface (each LDLR recycles ~150× over its lifetime); LDL → lysosome → cholesterol release → cellular regulation of cholesterol synthesis (SREBP feedback)

**PCSK9 disruption of LDLR recycling:**
- PCSK9 binds LDLR extracellular EGF-A domain with high affinity at acidic pH → prevents LDLR conformational change needed for dissociation from ligand → LDLR-PCSK9-LDL complex → lysosomal degradation of LDLR → net loss of LDLR from cell surface
- Statins → ↑LDLR expression (SREBP-2 activation) but also → ↑PCSK9 secretion → partially offset LDLR increase (explains 50% of LDL-C reduction achievable with statins)
- PCSK9 GOF mutations (D374Y) have 5-10× higher LDLR affinity at acidic pH → maximum LDLR degradation → severe FH phenotype

**LDLR mutation classes:**
- **Class 1 (null):** No protein synthesized; most severe; frameshift/nonsense mutations
- **Class 2 (transport-defective):** LDLR synthesized but trapped in ER; can't reach cell surface
- **Class 3 (binding-defective):** LDLR reaches surface but can't bind LDL (ligand-binding domain mutations)
- **Class 4 (internalization-defective):** LDLR binds LDL but can't internalize (clathrin-coated pit targeting mutations in cytoplasmic domain)
- **Class 5 (recycling-defective):** LDLR binds and internalizes but can't recycle; degraded with ligand

**Clinical features:**
- **Tendon xanthomas:** Achilles tendon (most characteristic), extensor tendons of hand, patellar tendon; lipid-laden macrophage foam cell deposits; pathognomonic for FH when present
- **Xanthelasma:** Yellow plaques on eyelids; less specific (also in normolipidemic patients)
- **Corneal arcus:** Lipid deposit in corneal periphery; highly specific in young patients (<45 years) with elevated LDL-C
- **Premature CAD/aortic stenosis:** Family history of premature MI (first-degree male relative <55, female <65)

### Diagnostic criteria (Dutch Lipid Clinic Network)

| Criterion | Points |
|:---|:---|
| Family history of premature CAD or familial hypercholesterolemia | 1-2 |
| Clinical history of premature CAD or cerebrovascular/peripheral artery disease | 2 |
| Tendon xanthomas (patient or first-degree relative) | 6 |
| Corneal arcus <45 years | 4 |
| LDL-C ≥8.5 mmol/L (≥330 mg/dL) | 8 |
| LDL-C 6.5-8.4 mmol/L (250-329 mg/dL) | 5 |
| LDL-C 5.0-6.4 mmol/L (190-249 mg/dL) | 3 |
| LDL-C 4.0-4.9 mmol/L (155-189 mg/dL) | 1 |
| Causative mutation in LDLR, APOB, PCSK9 | 8 |
- **Definite FH:** ≥8 points; **Probable FH:** 6-7; **Possible FH:** 3-5

**Cascade screening:** Genetic testing of first-degree relatives of confirmed FH patients → most cost-effective FH detection strategy; identifying an affected parent yields 50% probability per child

## Function

### Treatment — Lipid-lowering strategy

**Goal:** LDL-C reduction to target (ESC/EAS guidelines for very high risk: <55 mg/dL or ≥50% reduction from baseline; for HoFH: as low as possible, ideally <70 mg/dL)

**High-intensity statin therapy (first-line):**
- Rosuvastatin 20-40 mg or atorvastatin 40-80 mg: ↓LDL-C ~45-55%
- Mechanism: inhibit HMG-CoA reductase → ↓cholesterol synthesis → SREBP-2 activation → ↑LDLR expression (and ↑PCSK9 — partially offsetting the benefit)
- Adverse effects: myalgia (5-10%); rare myopathy/rhabdomyolysis; statin-induced myopathy screening via CK; LFT elevation (rare)

**Ezetimibe (second-line add-on):**
- NPC1L1 inhibitor → ↓intestinal cholesterol absorption → further LDLR upregulation; adds ~20-25% LDL-C reduction to statin
- SHARP trial: simvastatin + ezetimibe → 17% RRR atherosclerotic events in CKD; IMPROVE-IT: ezetimibe + simvastatin vs. simvastatin alone → 6.4% RRR MACE at 7 years (modest incremental benefit)

**PCSK9 inhibitors (standard for FH not at goal):**
- **Evolocumab (Repatha):** 140 mg SC Q2W or 420 mg SC Q4W; FOURIER trial: 59% LDL-C reduction; 15% MACE reduction at 26 months; FDA-approved for HeFH and HoFH (reduced but not absent LDLR function)
- **Alirocumab (Praluent):** 75-150 mg SC Q2W; ODYSSEY OUTCOMES: 15% MACE reduction + 15% all-cause mortality reduction at 2.8 years; FDA-approved for HeFH
- **Inclisiran (Leqvio; siRNA):** 284 mg SC at month 0, 3, then Q6 months [^raal-2020-inclisiran-fh]; mRNA silencing of hepatic PCSK9 → ~50% sustained LDL-C reduction with twice-yearly dosing; FDA-approved 2021 for HeFH; ORION-9: primary endpoint met

**HoFH-specific therapies:**
- **LDL apheresis:** Weekly/biweekly extracorporeal LDL removal; ~60-70% acute LDL-C reduction; required for LDLR null/null patients until new therapies available
- **Lomitapide (Juxtapid):** MTP (microsomal triglyceride transfer protein) inhibitor → ↓VLDL assembly/secretion → LDL-C reduction 50%; Black Box Warning: hepatotoxicity; FDA-approved for HoFH only
- **Evinacumab (Evkeeza; anti-ANGPTL3 mAb; Regeneron):** FDA-approved 2021 for HoFH; ANGPTL3 inhibits lipoprotein lipase and endothelial lipase; evinacumab → ↓LDL-C ~49% in HoFH even with null LDLR (LPL-mediated pathway, LDLR-independent); monthly IV infusion
- **Mipomersen (Kynamro; antisense oligonucleotide targeting APOB):** Discontinued in most markets due to hepatotoxicity

## Pathology

**Accelerated atherosclerosis:**
- Lifetime elevated LDL-C drives plaque in coronary, carotid, and peripheral arteries decades earlier than in the general population; cumulative cholesterol burden (LDL-C × years = cholesterol-year score) predicts events better than single measurements
- Imaging: Coronary artery calcium (CAC) score; carotid intima-media thickness (IMT); coronary CT angiography — useful for risk stratification and treatment decision-making in FH

**Aortic valve disease in HoFH:**
- Supravalvular and valvular aortic stenosis from lipid infiltration in aortic root; progressive → aortic valve replacement may be required in 3rd-4th decade in severe HoFH

**Statin intolerance:**
- 5-10% of patients discontinue statins due to muscle symptoms; objective statin-associated myopathy (CK elevation >3-10×) is rare; nocebo effect accounts for significant proportion; management: lower dose, alternate-day dosing, hydrophilic statins (rosuvastatin, pravastatin), switch statin; if truly intolerant → bempedoic acid (ACL inhibitor, doesn't affect skeletal muscle) + ezetimibe + PCSK9 inhibitor

**Pediatric FH:**
- Current guidelines recommend statin initiation at age 8-10 years in HeFH with LDL-C >160 mg/dL; early treatment reduces subclinical atherosclerosis progression; HoFH: treatment from age 2-5 with LDL apheresis + statin ± lomitapide

## Connections

- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — PCSK9 GOF mutations cause autosomal dominant FH (ADH3); evolocumab and alirocumab reduce LDL-C 50-60% add-on to statins; inclisiran (PCSK9 siRNA) reduces LDL-C ~50% with Q6M dosing; standard of care for FH not at LDL goal on maximally tolerated statin.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — FH accelerates atherosclerosis; HeFH untreated: 20× higher CVD risk; coronary atherosclerosis, tendon xanthomas, and xanthelasma are hallmarks; cumulative LDL-C burden predicts events; early statin initiation reduces atherosclerotic events in HeFH.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — FH results from impaired LDLR-mediated cholesterol clearance; LDLR mutations → fewer surface receptors → LDL-C >190 mg/dL (HeFH) or >500 mg/dL (HoFH LDLR null); excess cholesterol in macrophages → foam cells → atheromatous plaque.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — hepatocytes express >90% of plasma LDLR; LDLR-mediated LDL endocytosis is the primary clearance route; SREBP-2 upregulates LDLR after statin treatment; liver transplant in HoFH normalizes LDL-C — confirming hepatocytic LDLR as the disease driver.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — in FH, chronically elevated LDL-C → macrophage scavenger receptor (SR-A, CD36) uptake of oxidized LDL → foam cell formation; foam cells are the histological hallmark of the atheromatous plaque; FH macrophages exhibit exaggerated ox-LDL uptake vs. normolipidemic controls.
- `connects-to` → **[Stroke](../stroke/README.md)** — FH accelerates carotid and cerebrovascular atherosclerosis; HeFH patients have elevated carotid intima-media thickness (cIMT) and higher stroke risk vs. general population; statin + PCSK9 inhibitor reduces cIMT progression and ischemic stroke incidence in FH cohorts.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Familial hypercholesterolemia is defined by its toll on the heart: lifelong high LDL drives premature coronary disease — heterozygotes infarct in their 40s-50s while homozygotes can have MIs and aortic-valve stenosis in childhood; early intensive LDL lowering is lifesaving.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Atherosclerosis in FH starts at the endothelium: the lifelong excess of LDL infiltrates and is retained in the subendothelial intima, where oxidation activates endothelial cells to recruit monocytes — repeated for decades at FH's LDL levels, this builds plaque far earlier.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Vascular smooth muscle cells shape the FH atheroma: they migrate from the media into the intima, take up modified LDL to become foam cells, and lay down the collagen fibrous cap whose stability — or rupture — determines whether a plaque stays silent or causes infarction.
- `treated-by` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — Statins are the cornerstone of FH treatment: by inhibiting HMG-CoA reductase they upregulate hepatic LDL receptors to clear LDL, but FH patients—especially homozygotes with few functional receptors—often need high-intensity statins plus ezetimibe and PCSK9 inhibitors.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is central to FH: hepatocyte LDL receptors normally clear ~70% of circulating LDL, so the LDLR (or APOB/PCSK9) mutations of FH cripple this clearance → lifelong high LDL; the liver is thus the target of statins, PCSK9 inhibitors, apheresis and gene therapy.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — FH and hypertension are multiplicative cardiovascular risk factors: lifelong high LDL accelerates atherosclerosis while raised blood pressure adds shear stress and endothelial injury, so an FH patient who is also hypertensive faces especially early coronary disease.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Familial hypercholesterolemia is a lifelong assault on the cardiovascular system: from birth very high LDL accelerates atherosclerosis, so untreated heterozygotes get coronary disease decades early and homozygotes in childhood—early statin/PCSK9 therapy is essential.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Familial hypercholesterolemia and type 2 diabetes multiply cardiovascular risk together: FH's lifelong LDL burden plus diabetic dyslipidemia compound atherosclerosis—and although statins slightly raise diabetes risk, their cardiovascular benefit in FH far outweighs it.
- `connects-to` → **[NASH](../nash/README.md)** — Familial hypercholesterolemia and NASH are distinct lipid disorders of the liver: FH is a receptor defect that floods blood with LDL but spares the liver, while NASH is hepatic fat from insulin resistance—high LDL with a normal liver differs from fatty liver.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Familial hypercholesterolemia causes premature coronary disease that leads to heart failure: lifelong sky-high LDL drives early severe atherosclerosis and heart attacks, so untreated FH causes ischemic cardiomyopathy decades early.
- `connects-to` → **[Obesity](../obesity/README.md)** — Familial hypercholesterolemia and obesity stack cardiovascular risk: FH is a genetic LDL-receptor defect causing very high cholesterol, while obesity adds insulin resistance and inflammation—together compounding the premature atherosclerosis FH drives.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Familial hypercholesterolemia and chronic kidney disease are both potent cardiovascular risk amplifiers: FH from extreme LDL, CKD from vascular calcification and dyslipidemia, so an FH patient who also develops CKD faces compounded atherosclerotic risk.
- `connects-to` → **[APOE](../../03-molecular/apoe/README.md)** — FH and APOE both shape blood cholesterol but differently: FH is a single-gene defect in LDL clearance causing severe lifelong hypercholesterolemia, while APOE variants modify lipid levels and cardiovascular risk—monogenic versus polygenic cholesterol disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Coronary artery calcium scoring helps gauge risk in FH: lifelong high LDL drives calcified atherosclerotic plaque, so a CT calcium score quantifies accumulated arterial damage and refines who needs the most aggressive lipid lowering.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — FH's silent arterial damage is revealed by photon-based imaging: low-dose CT uses X-ray photons to measure coronary calcium, turning invisible decades of LDL-driven plaque buildup into a number that guides how intensively to treat.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Familial hypercholesterolemia writes itself on the skin: lifelong high LDL deposits cholesterol as tendon xanthomas (Achilles, knuckles) and eyelid xanthelasma, so these fatty bumps are physical clues that prompt lipid testing and family screening.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye flags familial hypercholesterolemia: a corneal arcus—a white lipid ring around the iris—appearing before age 45 strongly suggests it, so this ocular sign, like xanthomas, helps catch the inherited high cholesterol early enough to prevent heart attacks.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cultured skin fibroblasts revealed FH's cause: studying patients' fibroblasts, Brown and Goldstein discovered the LDL receptor and how its loss blocks cholesterol uptake—the Nobel work that explained FH and led to statins and PCSK9 inhibitors.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — FH shows that LDL isn't the whole story—inflammation matters too: IL-6-driven inflammation in the artery wall adds 'residual risk' on top of high cholesterol, so anti-inflammatory therapy (colchicine, IL-targeted drugs) complements LDL-lowering in atherosclerosis.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Atherosclerosis in FH is partly an immune disease: T-helper cells infiltrate the cholesterol-laden plaque and stoke inflammation that destabilizes it, so the early plaques of FH reflect adaptive immunity, not just passive lipid buildup.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Whether FH's plaques kill depends on collagen: a thick collagen fibrous cap (laid down by smooth muscle) keeps a plaque stable, while a thin one ruptures to cause heart attacks—so plaque collagen, not just cholesterol level, decides the danger.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — FH's danger is realized when platelets meet a ruptured plaque: the lifelong high LDL builds plaques whose cap can tear, exposing tissue that triggers platelets to clot and block the artery, the final step from cholesterol to heart attack or stroke.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — FH ultimately starves the heart of oxygen: narrowing coronary arteries cut blood flow, so demand outstrips supply and the muscle becomes ischemic, causing the angina and infarction that make untreated FH so deadly so young.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — FH's growing plaques sprout fragile vessels via VEGF: as plaques thicken they outgrow their oxygen supply and release VEGF to recruit leaky new microvessels, which bleed into the plaque and destabilize it, raising rupture risk.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — FH's atherosclerosis reaches the kidneys: cholesterol-laden plaque narrows the renal arteries, which can drive resistant high blood pressure and slowly starve the kidneys, adding renovascular disease to FH's vascular toll.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — FH plaques are fed from the bone marrow: it supplies the monocytes that become plaque foam cells, and age-related clonal mutations in marrow cells (clonal hematopoiesis) further inflame and accelerate the atherosclerosis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils inflame FH's arteries: drawn into cholesterol-rich plaque, they release enzymes and DNA nets (NETs) that amplify inflammation and erode the fibrous cap, helping tip a stable plaque toward the clot that causes a heart attack.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — FH's lifelong high LDL threatens the brain too: it accelerates carotid and cerebral atherosclerosis, raising the risk of ischemic stroke and vascular cognitive decline, not just heart attacks.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — FH deposits cholesterol in connective tissue: Achilles and knuckle tendon xanthomas are a hallmark, fibrous tissue infiltrated by lipid-laden cells, mirroring the fibrous cap that walls off an artery plaque.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-α destabilizes FH's plaques: plaque macrophages pour out this cytokine, whose inflammation thins the fibrous cap and helps tip a quiet lesion toward the rupture that triggers a heart attack.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals where the excess cholesterol piles up: macrophages gorge on LDL until they become lipid-stuffed foam cells, and needle-shaped cholesterol clefts stud the xanthomas and plaques that scar FH's arteries and tendons.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Premature atherosclerosis can starve the gut: FH's early, severe plaque burden narrows the mesenteric arteries too, so chronic intestinal angina — abdominal pain after eating — can join its better-known heart and brain disease.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — FH's cholesterol-laden aorta can shower emboli: fragments of plaque break off as cholesterol crystals that lodge in small vessels of the spleen, kidneys, and skin, a multi-organ embolic syndrome of advanced disease.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — FH leaves cholesterol in the tendons: firm Achilles and knuckle tendon xanthomas are a near-pathognomonic sign, and the statins that treat it can in turn cause muscle aches and, rarely, breakdown — both tying the disease to the musculoskeletal system.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Lifelong statin therapy nudges the pancreas: the drugs slightly raise the risk of new-onset diabetes, and in forms with high triglycerides too, the excess fat can inflame the pancreas into pancreatitis.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy forces a treatment pause: statins are avoided in pregnancy for fear of harming the fetus, so women with FH must stop them while trying to conceive and during gestation, leaving their high LDL untreated for months.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody now slashes the LDL: PCSK9-inhibitor monoclonal antibodies (evolocumab, alirocumab) free up the liver's LDL receptors, dramatically lowering cholesterol in FH patients who can't reach target on statins alone.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid must be cleared first: hypothyroidism is a common secondary cause of high cholesterol that both mimics and worsens FH, so thyroid function is checked before and during treatment of the inherited disorder.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Diet still pulls its weight: soluble fiber binds bile acids to lower LDL, so a high-fiber, low-saturated-fat pattern is the dietary foundation on which the statins and antibodies of FH treatment build.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The gut is the body's other cholesterol tap: the small intestine absorbs dietary and biliary cholesterol via NPC1L1, the target of ezetimibe — a second lever pulled alongside statins when the liver pathway alone can't lower FH's LDL enough.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — High cholesterol travels with a sticky, clot-prone blood: FH raises fibrinogen and other prothrombotic factors, so the atherosclerotic plaques it builds are more likely to clot off into the heart attacks and strokes that strike early.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Atherosclerosis is also an immune disease: cytotoxic T cells infiltrate the lipid-laden plaque and, alongside the macrophages, drive the inflammation that destabilizes it, so FH's lifelong LDL load is fought partly in the immune cells of the artery wall.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Trapped LDL ignites a master inflammatory switch: oxidized lipid in the artery wall activates NF-κB in endothelial cells and macrophages, turning on the adhesion molecules and chemokines that recruit the inflammation accelerating FH's plaques.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells lurk in the plaque: they cluster in atherosclerotic lesions and release proteases and mediators that destabilize the fibrous cap, contributing to the rupture risk behind FH's early heart attacks.
- `connects-to` → **[Thyroid Hormones (T3/T4)](../../03-molecular/thyroid-hormones/README.md)** — The thyroid sets LDL-receptor levels: thyroid hormone drives expression of the very receptor FH lacks, so hypothyroidism worsens the cholesterol and must be corrected before judging the genetic disease's severity.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The heart muscle pays for the genes: lifelong sky-high LDL gives FH patients premature coronary disease and heart attacks, killing cardiomyocytes decades early — the reason untreated homozygous FH can be fatal in childhood.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Immune cells gorge on the excess cholesterol: dendritic cells and macrophages in the artery wall engulf oxidized LDL to become lipid-laden foam cells and present lipid antigens, an immune arm of the atherogenesis FH accelerates.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its prothrombotic milieu reaches the veins too: beyond arterial disease, the raised fibrinogen and endothelial dysfunction of severe hypercholesterolemia are linked to a modestly higher risk of venous thromboembolism.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Blocked leg arteries starve the wound: the premature peripheral arterial disease of FH cuts blood flow to the limbs, producing ischemic, slow-healing ulcers and, in critical limb ischemia, gangrene.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A lifelong genetic verdict weighs on the mind: living with an inherited high risk of early heart attack, cascade family testing and lifelong therapy — sometimes with statin-related muscle symptoms — carries a real psychological burden.
- `connects-to` → **[Gout](../gout/README.md)** — Lipid and urate disturbances cluster: dyslipidemia and hyperuricemia frequently coexist, and FH patients carry the cardiometabolic context — and statin or niacin therapy effects on urate — that associate it with gout.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Cholesterol and cerebral atherosclerosis reach the mind: the lifelong high LDL of FH accelerates small- and large-vessel brain disease, contributing to vascular and mixed Alzheimer-type cognitive decline.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its long-term statins can irritate nerves: alongside the more common myalgia, prolonged high-intensity statin therapy used to control FH has been linked in some patients to a peripheral neuropathy with neuropathic pain.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A genetic verdict of early heart disease breeds worry: learning of an inherited condition that threatens premature heart attacks, often after a relative's early death, fosters chronic health anxiety in FH families.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Excess cholesterol deposits in skin and tendons: FH produces tendon xanthomas over the Achilles and knuckles, eyelid xanthelasma and a corneal arcus, visible lipid deposits that are diagnostic clues.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The liver is the organ of the disease and its treatment: hepatic LDL receptors clear cholesterol and are defective in FH, and the statins used to treat it act on and are monitored for toxicity in the liver.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Cholesterol is the substrate of the steroid hormones: the lipid metabolism deranged in FH supplies the precursor for adrenal and gonadal steroidogenesis, and statins carry a modest dysglycaemia signal.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its plaques narrow the renal arteries: premature atherosclerosis in FH affects the renal arteries, causing renovascular hypertension and ischaemic nephropathy with declining kidney function.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It hardens the arteries to the brain: lifelong high LDL drives early carotid and cerebral atherosclerosis, raising the risk of transient ischaemic attacks and ischaemic stroke at a young age.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its atherosclerosis is an inflammatory process: chronically elevated LDL is taken up by arterial macrophages into foam cells, driving the immune-cell-rich plaques that FH accelerates.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Once arteries are damaged, antiplatelet cover follows: aspirin is added for secondary prevention after the premature heart attacks and strokes that untreated FH causes.
- `connects-to` → **[ACE inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — They protect the heart after early infarction: ACE inhibitors support left-ventricular function after the premature myocardial infarction FH produces and treat the hypertension that compounds its vascular risk.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet adds a modest lever: omega-3 supplements mainly lower triglycerides and complement statins, though they do little for the very high LDL that defines FH.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — This is where it does its damage: lifelong high LDL drives cholesterol into the arterial wall, building the atherosclerotic plaque that causes premature coronary disease in familial hypercholesterolaemia.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Cholesterol leaves tissues through it: HDL-mediated reverse cholesterol transport drains peripheral cholesterol via the lymphatics, and FH's deposits surface as tendon and skin xanthomas when that clearance is overwhelmed.
- `connects-to` → **[Berberine](../../../03-medicine/02-traditional/berberine/README.md)** — A natural compound that lowers LDL: berberine upregulates the LDL receptor and modestly reduces cholesterol, studied as an adjunct in people who cannot tolerate or fully respond to statins.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Modern LDL-lowering beyond statins: PCSK9-inhibitor antibodies (evolocumab, alirocumab), the siRNA inclisiran and ANGPTL3-blocking evinacumab dramatically cut LDL in familial hypercholesterolaemia when statins alone fall short.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The defect lives in the liver: FH stems from faulty LDL receptors on hepatocytes of the liver lobule that normally clear LDL from blood, so cholesterol accumulates from birth — and the liver is the target of statins and PCSK9 therapy.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It infarcts the heart young: untreated familial hypercholesterolaemia drives accelerated coronary atherosclerosis and myocardial infarction in the third to fifth decades, decades earlier than ordinary high cholesterol.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Early ischaemia hits the wiring: the premature, severe coronary atherosclerosis of untreated FH damages the conduction system, predisposing young adults to ventricular arrhythmia and sudden cardiac death.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Cholesterol feeds steroid hormones: the adrenal cortex takes up LDL cholesterol through the very LDL receptor defective in FH to build cortisol and aldosterone, tying lipoprotein handling to steroidogenesis.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Lipids injure the kidney too: chronic LDL excess drives atherosclerotic renovascular disease and lipid-mediated glomerular injury, so severe untreated FH accelerates kidney as well as heart disease.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — Cholesterol on the valves: severe (especially homozygous) familial hypercholesterolaemia deposits cholesterol in the aortic valve and root, causing supravalvular and calcific aortic stenosis of the endocardium.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Where dietary cholesterol enters: the intestinal epithelium absorbs cholesterol via NPC1L1, the target of ezetimibe—an FH therapy that complements statins by cutting absorption alongside reduced synthesis.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Compounded cardiovascular risk: when familial hypercholesterolaemia coexists with diabetes such as type 1, the lipid and glycaemic insults multiply atherosclerotic risk, demanding aggressive LDL lowering.
- `connects-to` → **[Werner Syndrome](../werner-syndrome/README.md)** — Two routes to early heart attacks: familial hypercholesterolaemia drives premature atherosclerosis through lifelong high LDL, while Werner syndrome reaches the same early coronary disease through accelerated cellular ageing.
- `connects-to` → **[Marfan Syndrome](../marfan-syndrome/README.md)** — Inherited cardiovascular disease, different walls: familial hypercholesterolaemia attacks the coronary arteries with cholesterol, while Marfan weakens the aortic wall through fibrillin loss—two autosomal-dominant routes to cardiac death.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Tendon xanthomas: familial hypercholesterolaemia deposits cholesterol in tendons—classically the Achilles and finger-extensor tendons at their cortical-bone insertions—forming the xanthomas that are a clinical hallmark.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Early endothelial injury: lifelong high LDL in familial hypercholesterolaemia impairs endothelial nitric oxide production from childhood, the first step toward the premature atherosclerosis that defines the disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: oxidised LDL accumulating in the arterial wall induces CCL2, drawing in the monocytes that become the foam cells of the accelerated plaques of familial hypercholesterolaemia.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vascular tone imbalance: the endothelial dysfunction of familial hypercholesterolaemia shifts the balance toward endothelin-1 vasoconstriction, compounding the atherosclerotic narrowing of the arteries.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Cholesterol-crystal inflammasome: cholesterol crystals in plaque macrophages activate the NLRP3 inflammasome, releasing IL-1β that propels the accelerated atherosclerosis of familial hypercholesterolaemia.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Intraplaque hypoxia: as the lipid-rich plaques of familial hypercholesterolaemia thicken, their cores turn hypoxic and stabilise HIF-1α, driving the neovascularisation and necrotic-core expansion that destabilise them.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Myeloid alarmin: S100A8/A9 from activated plaque neutrophils and monocytes amplifies arterial inflammation and is a circulating biomarker of the high cardiovascular risk of familial hypercholesterolaemia.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — Oxidized LDL and AGEs signaling through RAGE on endothelium and macrophages amplify the NF-κB-driven arterial inflammation that accelerates the atherosclerosis of familial hypercholesterolemia beyond the LDL burden alone.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Rupture of the lipid-rich plaques of familial hypercholesterolemia exposes tissue factor that generates thrombin, the coagulation step converting a plaque into the occlusive clot of the premature myocardial infarctions that define the disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — C3 and the complement cascade are activated within the atherosclerotic lesions of familial hypercholesterolemia, contributing to the chronic vascular inflammation that drives plaque progression alongside the lipid and myeloid mechanisms.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β from cholesterol-crystal-activated plaque macrophages drives atherosclerotic inflammation, and the CANTOS trial showed IL-1β blockade cuts cardiovascular events independent of lipid lowering, relevant to FH's inflammatory burden.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3-mediated apoptosis of lipid-laden foam cells, when their clearance fails, builds the necrotic lipid core of the atherosclerotic plaque, the unstable center prone to the rupture that causes the premature heart attacks of FH.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Advanced atherosclerotic plaques in familial hypercholesterolemia calcify, the calcium deposition measured by coronary-artery-calcium scoring that quantifies plaque burden and refines cardiovascular-risk prediction.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF drives the migration and proliferation of the vascular smooth-muscle cells (already mapped) into the atherosclerotic plaque, building the neointima of the accelerated atherosclerosis of familial hypercholesterolemia.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β regulates the collagen synthesis and fibrous-cap stability of atherosclerotic plaques, opposing the inflammatory destabilization that causes the early myocardial infarctions of FH.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement activation by cholesterol-rich plaque (C3 already mapped, through C5) amplifies the vascular inflammation of the atherosclerosis driven by familial hypercholesterolemia.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR sensing of oxidized LDL signals through MyD88 to NF-κB, igniting the sterile innate-immune inflammation that converts the lipid burden of FH into progressive atherosclerotic plaque.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 mounts the antioxidant response that counters the oxidative modification of the LDL accumulating in FH — the oxidized LDL that, unopposed, drives foam-cell formation and endothelial injury.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — The PI3K-AKT-eNOS axis sustains endothelial nitric-oxide production, a vasoprotective pathway statins enhance pleiotropically and that the lipid excess of FH progressively impairs.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 marks the lipid-laden plaque macrophages and promotes the vascular inflammation accelerating atherosclerosis in familial hypercholesterolemia.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling regulates macrophage autophagy and efferocytosis in the atherosclerotic plaque, shaping lesion progression in familial hypercholesterolemia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Oxidized-LDL and growth-factor ERK-MAPK signaling drives the smooth-muscle proliferation and foam-cell responses of accelerated atherosclerosis in FH.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the vascular inflammation that accelerates atherosclerotic plaque progression in familial hypercholesterolemia.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) shapes the fibrous-cap formation and plaque stability of the accelerated atherosclerosis of familial hypercholesterolemia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cholesterol-crystal and mitochondrial DNA engagement of cGAS-STING amplifies the sterile inflammation of the atherosclerotic plaque in familial hypercholesterolemia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate hepatic lipid metabolism and the endothelial oxidative-stress response relevant to the accelerated atherosclerosis of familial hypercholesterolemia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the macrophage inflammatory activation within the cholesterol-laden atherosclerotic plaques of familial hypercholesterolemia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2-STAT cytokine signaling (IL-6-STAT3 already mapped) amplifies the vascular inflammation driving premature atherosclerosis in familial hypercholesterolemia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the inflammatory and metabolic signaling in the vascular wall that accelerates atherosclerosis in familial hypercholesterolemia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, a regulator of hepatic and vascular lipid metabolism, participates in the metabolic context of familial hypercholesterolemia.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic T cells in the atherosclerotic plaque contribute to the vascular inflammation and plaque instability of familial hypercholesterolemia.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the endothelial and macrophage responses to the LDL burden of familial hypercholesterolemia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy (including lipophagy) modulates the macrophage cholesterol handling and foam-cell formation in familial hypercholesterolemia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte recruitment accelerates the atherosclerosis of familial hypercholesterolemia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the lipid-metabolism and vascular-inflammation gene programs relevant to familial hypercholesterolemia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the endothelial and leukocyte interactions of the accelerated atherosclerosis of familial hypercholesterolemia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the endothelial and smooth-muscle-cell responses of the atherogenesis of familial hypercholesterolemia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the vascular inflammation of the atherosclerosis of familial hypercholesterolemia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the atherosclerotic vascular inflammation of familial hypercholesterolemia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the lipid-metabolism and vascular gene programs relevant to familial hypercholesterolemia.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Premature infarction: untreated familial hypercholesterolaemia causes early myocardial infarction, and troponin release marks the myocardial injury of the coronary events that are its leading cause of death, driving aggressive lipid lowering from childhood.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — LDL oxidation: xanthine-oxidase-derived reactive oxygen species help oxidise the excess LDL of familial hypercholesterolaemia, and oxidised LDL is the form avidly taken up by macrophages (already mapped) to form the foam cells of atheroma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Plaque adaptive immunity: atherosclerosis in familial hypercholesterolaemia has an adaptive immune component, with MHC class II presentation of oxidised-LDL and ApoB peptides to T cells shaping the inflammatory plaque beyond the lipid burden.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Plaque T-cell response: IL-2-driven T-cell activation (MHC class II already mapped) participates in the adaptive immune inflammation of the atherosclerotic plaque, contributing to lesion progression in familial hypercholesterolaemia beyond the lipid drive.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Atheroprotective regulation: the anti-inflammatory cytokine IL-10 restrains plaque inflammation, and the balance between it and the pro-inflammatory cytokines already mapped shapes the stability of the atherosclerotic lesions of familial hypercholesterolaemia.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences: estrogen is cardioprotective and lowers LDL, so premenopausal women with familial hypercholesterolaemia are relatively protected until menopause, contributing to the later onset of coronary disease in affected women.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Thromboxane and plaque thrombosis: the prostaglandin balance shifts toward the prothrombotic thromboxane on the atherosclerotic plaques of familial hypercholesterolaemia, part of why aspirin is used to prevent the coronary events.
- `connects-to` → **[Von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — Plaque-rupture thrombosis: when a plaque of familial hypercholesterolaemia ruptures, von Willebrand factor mediates the platelet adhesion that, with thrombin and fibrinogen (already mapped), forms the occlusive thrombus of myocardial infarction.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic amplification: although familial hypercholesterolaemia is a monogenic LDL disorder, coexisting insulin resistance and the metabolic syndrome compound its atherogenic risk, adding to the burden of the very high LDL.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Plaque macrophage polarisation: IL-4 polarises the plaque macrophages (already mapped) toward an M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the atherosclerotic lesions driven by the very high LDL of familial hypercholesterolaemia.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine amplification: leptin, from adipose tissue, adds an inflammatory and atherogenic contribution (insulin already mapped) that compounds the cardiovascular risk of the monogenic LDL elevation in familial hypercholesterolaemia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Vasoprotective adipokine: adiponectin, with leptin (already mapped), is a vascular-protective adipokine whose fall in the metabolic syndrome removes a brake on the atherogenesis driven by familial hypercholesterolaemia.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Plaque type-2 arm: IL-13, with IL-4 (already mapped), modulates the M2 macrophage (already mapped) arm of the inflammation of the atherosclerotic plaque driven by familial hypercholesterolaemia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Atherogenic adipokine: resistin, with leptin and adiponectin (already mapped), is a pro-inflammatory adipokine that adds to the atherogenic-inflammatory (IL-6 already mapped) milieu compounding the cardiovascular risk of familial hypercholesterolaemia.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — LDL oxidation: iron catalyses the oxidation of the LDL (cholesterol already mapped) that generates the oxidised LDL taken up by the foam-cell macrophages (already mapped), part of the oxidative atherogenesis of familial hypercholesterolaemia.
- `connects-to` → **[Endothelial cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial dysfunction: the LDL (cholesterol already mapped) retention in the arterial intima and the endothelial dysfunction (nitric oxide already mapped) initiate the atherosclerosis of familial hypercholesterolaemia.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — LDLR hepatocytes: the hepatocytes express the LDL receptor (PCSK9 already mapped) that clears the LDL; the hepatocyte LDLR defect is the disease of familial hypercholesterolaemia and the target of the gene therapy.
- `connects-to` → **[Smooth muscle cell](../../04-cellular/smooth-muscle-cell/README.md)** — Fibrous cap: the vascular smooth-muscle cells migrate and form the fibrous cap (collagen already mapped) of the atherosclerotic plaque of familial hypercholesterolaemia.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 plaque inflammation: the IFN-γ of the plaque T cells is the type-II interferon arm of the Th1-driven inflammation that destabilises the atherosclerotic plaque of familial hypercholesterolaemia.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the atherosclerotic plaque inflammation of familial hypercholesterolaemia.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate plaque interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the cholesterol-crystal and cellular stress, amplifies the macrophage (already mapped) inflammation of the atheroma of familial hypercholesterolaemia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of the atherosclerotic plaque of familial hypercholesterolaemia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the atherosclerotic plaque inflammation of familial hypercholesterolaemia.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/mast-cell arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension whose mast cells contribute to the atheroma of familial hypercholesterolaemia.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate plaque arm: the NK cells (perforin already mapped) infiltrate the atherosclerotic plaque and are part of the innate immune contribution to the atherosclerosis of familial hypercholesterolaemia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid recruitment into the atherosclerotic plaque of familial hypercholesterolaemia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active on the oxidised LDL and the atheroma of familial hypercholesterolaemia.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the oxidised LDL and C-reactive protein in the atheroma of familial hypercholesterolaemia.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Atheroma matricellular: osteopontin, produced by the foam-cell macrophages (already mapped), is a matricellular mediator of the plaque inflammation and the vascular calcification of familial hypercholesterolaemia.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Plaque iron: transferrin, the iron carrier, reflects the disordered iron handling and the intraplaque-haemorrhage iron that aggravates the oxidative injury of the atheroma of familial hypercholesterolaemia.

[^goldstein-1985-ldlr-nobel]: Goldstein JL, Brown MS. The LDL receptor. *Arterioscler Thromb Vasc Biol.* 2009;29(4):431-438. [doi:10.1161/ATVBAHA.108.179564](https://doi.org/10.1161/ATVBAHA.108.179564) · [PubMed 19299327](https://pubmed.ncbi.nlm.nih.gov/19299327/)
[^raal-2020-inclisiran-fh]: Raal FJ, Kallend D, Ray KK, et al. Inclisiran for the Treatment of Heterozygous Familial Hypercholesterolemia. *N Engl J Med.* 2020;382(16):1520-1530. [doi:10.1056/NEJMoa1913805](https://doi.org/10.1056/NEJMoa1913805) · [PubMed 32197277](https://pubmed.ncbi.nlm.nih.gov/32197277/)
[^watts-2020-hzfh-guidelines]: Watts GF, Gidding SS, Hegele RA, et al. International Atherosclerosis Society guidance for implementing best practice in the care of familial hypercholesterolaemia. *Nat Rev Cardiol.* 2023;20(12):845-869. [doi:10.1038/s41569-023-00892-0](https://doi.org/10.1038/s41569-023-00892-0) · [PubMed 37322181](https://pubmed.ncbi.nlm.nih.gov/37322181/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
