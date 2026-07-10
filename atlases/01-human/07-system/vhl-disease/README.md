---
schema: human-scale-entry/v1
id: vhl-disease
name: VHL Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary VHL disease is caused by germline VHL mutations; clear cell RCC, CNS and retinal hemangioblastomas, pheochromocytoma (type 2), and pancreatic NETs; belzutifan (HIF-2α inhibitor) is FDA-approved for VHL-related tumors; type 1/2A/2B/2C classification by pheo risk."
aliases: ["VHL disease", "von Hippel-Lindau disease", "VHL syndrome", "VHL hemangioblastoma", "VHL RCC", "hereditary VHL", "VHL pheochromocytoma", "VHL belzutifan", "von Hippel-Lindau syndrome"]
sources:
  - id: lonser-2003-vhl-disease
    type: peer-reviewed
    cite: "Lonser RR, Glenn GM, Walther M, et al. von Hippel-Lindau disease. Lancet. 2003;361(9374):2059-2067."
    doi: "10.1016/S0140-6736(03)13643-4"
    pmid: "12814730"
    url: "https://doi.org/10.1016/S0140-6736(03)13643-4"
  - id: choueiri-2020-hif2-rcc
    type: peer-reviewed
    cite: "Choueiri TK, Kaelin WG Jr. Targeting the HIF2-VEGF axis in renal cell carcinoma. Nat Med. 2020;26(10):1519-1530."
    doi: "10.1038/s41591-020-1093-z"
    pmid: "33020650"
    url: "https://doi.org/10.1038/s41591-020-1093-z"
cross_links:
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "Germline VHL LOF causes VHL disease via constitutive HIF-1α/2α accumulation; VHL β-domain recognizes EGLN1-hydroxylated HIF → ubiquitination; missense VHL variants predict pheo risk (type 2A/2B/2C) vs truncating (type 1, high RCC); belzutifan targets HIF-2α downstream."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "EGLN1 (PHD2) hydroxylates HIF-1α/2α under normoxia for VHL-mediated degradation; in VHL disease, VHL LOF renders HIF constitutively stable regardless of EGLN1 activity; EGLN1 inhibitors (PHD inhibitors) activate HIF for CKD anemia treatment by the same mechanism as VHL LOF."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Clear cell RCC (ccRCC) is the most common VHL disease tumor (~25-45% lifetime risk); VHL LOF → HIF-2α/VEGF → neovascularization → ccRCC; NSS (nephron-sparing surgery) for ≤3 cm tumors; belzutifan (HIF-2α inhibitor) FDA-approved for VHL disease-associated ccRCC since 2021."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "VHL disease type 2 (missense variants) carries pheochromocytoma risk (~8-20%); VHL pheo is typically bilateral, benign, adrenal, and normetanephrine-secreting; VHL-pheo driven by HIF-2α pseudohypoxia → catecholamine biosynthesis upregulation; resection curative."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "VHL disease is fundamentally a HIF disease: without functional pVHL, HIF-1α/2α escape degradation and constitutively switch on VEGF, EPO, PDGF, and GLUT1, producing the hypervascular hemangioblastomas, clear-cell RCC, and pheochromocytomas; belzutifan blocks HIF-2α directly."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Hemangioblastomas — benign but hypervascular cystic tumors with a HIF-2α-driven mural nodule — are the hallmark CNS lesions of VHL, clustering in cerebellum (~55%), spinal cord (~44%), and brainstem; annual brain and spine MRI from age 11 catches them."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Retinal hemangioblastoma is often the earliest VHL tumor, appearing around age 25 and frequently bilateral; peripheral lesions are treated with laser or cryotherapy and intravitreal anti-VEGF, so dilated fundus screening begins in the first year of life."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Von Hippel-Lindau and tuberous sclerosis are both dominant phakomatosis syndromes whose tumors need a second hit, but differ in driver: VHL loss stabilizes HIF to fuel angiogenic tumors (hemangioblastoma, ccRCC, pheo) while TSC loss hyperactivates mTOR — both hit the kidney."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The pancreas is a major VHL site: most carriers develop pancreatic cysts and serous cystadenomas (usually benign), but pancreatic neuroendocrine tumors arise in ~10-17% and can metastasize, so pancreatic imaging is part of lifelong VHL surveillance, guided by size and growth."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "VHL disease can cause polycythemia: pVHL loss stabilizes HIF, so hemangioblastomas (and hypomorphic germline VHL, as in Chuvash polycythemia) drive excess erythropoietin → high hematocrit; the same VHL-HIF-EPO axis is exploited by PHD inhibitors that raise EPO to treat anemia."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "VHL disease and HLRCC are hereditary kidney-cancer syndromes converging on pseudohypoxia: VHL loss stabilizes HIF directly, while HLRCC's FH loss raises fumarate that blocks HIF prolyl-hydroxylases—but VHL causes clear-cell RCC and HLRCC an aggressive papillary type."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "VHL disease predisposes to pancreatic neuroendocrine tumors: alongside its hemangioblastomas, clear-cell RCC, and pheochromocytomas, germline VHL loss drives often-multifocal panNETs, so a young patient with a panNET warrants VHL (and MEN1) testing."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Hemangioblastoma, the signature VHL tumor, is a richly vascular tumor of endothelial proliferation: VHL loss stabilizes HIF and floods the tissue with VEGF, driving the capillary-dense masses of the retina and cerebellum that define the syndrome."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "VHL and MEN1 are both dominant tumor-suppressor syndromes producing pancreatic tumors via different genes: VHL gives hemangioblastomas, clear-cell RCC, pheochromocytoma and pancreatic NETs, while MEN1 gives parathyroid, islet and pituitary tumors."
  - target: 01-human/07-system/birt-hogg-dube-syndrome
    relation: connects-to
    note: "VHL and Birt-Hogg-Dubé are hereditary kidney-cancer syndromes with distinct histologies: VHL's pVHL loss drives clear-cell RCC, while BHD's FLCN loss gives chromophobe/oncocytic tumors, lung cysts and skin fibrofolliculomas—each a different RCC."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "VHL connects to polycythemia through the HIF pathway: pVHL normally degrades HIF, so its loss stabilizes HIF and drives erythropoietin—and the germline VHL mutation of Chuvash polycythemia causes congenital erythrocytosis, a primary cause of high red-cell mass."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is VHL disease's most lethal target: VHL loss stabilizes HIF, so carriers develop multiple, recurrent clear cell renal cell carcinomas—the leading cause of death—prompting lifelong renal imaging and nephron-sparing surgery to preserve kidney function."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VHL disease is the prototype of VEGF-driven tumors: losing VHL stabilizes HIF, which floods tissue with VEGF to build the vessel-rich hemangioblastomas and renal cancers—so HIF-2a (belzutifan) and anti-VEGF drugs directly target the syndrome's core defect."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "VHL sits at the heart of cellular oxygen sensing: the VHL protein normally tags HIF for destruction when oxygen is plentiful, so its loss makes cells behave as if hypoxic—pseudohypoxia driving erythropoietin, angiogenesis and tumor growth even in normal oxygen."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal gland is a key VHL target: pheochromocytomas of the adrenal medulla, often bilateral and noradrenaline-secreting, arise in VHL and demand lifelong surveillance—a different organ lesion from the renal and CNS tumors that dominate the syndrome."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "VHL leaves a quiet mark on the reproductive system: epididymal cystadenomas in men and broad-ligament cystadenomas in women are characteristic benign tumors—rarely symptomatic but, when bilateral, near-diagnostic clues to the syndrome."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "VHL's broken oxygen sensing inflates red cells: failure to degrade HIF raises erythropoietin, driving excess erythrocyte production—the basis of Chuvash polycythemia, a milder VHL variant where the bone marrow overmakes red cells without a tumor."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "VHL disease is fundamentally a HIF-2alpha (EPAS1) disorder: losing pVHL stops degradation of EPAS1, so it constitutively drives VEGF and growth—the basis for belzutifan, a HIF-2alpha inhibitor now treating VHL-related kidney tumors and hemangioblastomas."
  - target: 01-human/03-molecular/sdhb
    relation: connects-to
    note: "VHL and SDHB cause 'pseudohypoxia' the same way: pVHL loss and SDHB loss both stabilize HIF as if oxygen were low, driving pheochromocytoma and paraganglioma—so two different genes converge on one hypoxia-mimicking cancer mechanism."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "HIF-2alpha links VHL to iron and red cells: the EPAS1 factor that accumulates in VHL governs erythropoietin and intestinal iron absorption, explaining the polycythemia seen when this hypoxia pathway runs unchecked."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "VHL tumors lean on mTOR alongside HIF: pseudohypoxic HIF signaling and mTOR together drive the clear cell kidney cancers and hemangioblastomas, so mTOR inhibitors—and now the HIF-2α blocker belzutifan—are used against VHL disease."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "VHL clear cell kidney cancers are immune-hot yet shielded by regulatory T cells: they draw T-cell infiltrates that respond to checkpoint drugs, but Tregs restrain the attack, shaping how immunotherapy works in VHL-related RCC."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "VHL tumors face NK-cell surveillance: their HIF-driven stress and altered MHC can expose them to natural killer cells, an innate defense being explored to complement checkpoint therapy against the syndrome's vascular tumors."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "VHL tumors lean on the mTOR-AKT growth axis alongside their HIF defect: pseudohypoxic signaling pairs with PI3K-AKT-mTOR activity to fuel the kidney cancers and hemangioblastomas, so mTOR-pathway drugs join the HIF inhibitor belzutifan."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells are enlisted against VHL's tumors: as belzutifan and immunotherapy enter VHL care, antigen-presenting dendritic cells help prime the T-cell response to the HIF-driven kidney and brain tumors."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "VHL studs the abdominal organs with cysts and tumors, including the liver: alongside the classic kidney, pancreas and adrenal lesions, hepatic cysts and hemangiomas occur, reflecting the syndrome's vascular, cyst-forming tendency."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "VHL drives the bone marrow to overproduce red cells: unchecked HIF raises erythropoietin, so the marrow churns out erythrocytes, causing the polycythemia that can accompany the syndrome and its EPO-secreting tumors."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "VHL's hemangioblastomas grow within the nervous system: these vascular tumors of the cerebellum, brainstem and spinal cord compress neurons, producing the headaches, ataxia and neurological deficits that often first signal the disease."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Losing VHL switches on PDGF among its HIF-driven growth factors: this angiogenic signal helps build the tumors' rich vasculature, and is one of the targets of the kinase inhibitors used against VHL-related kidney cancer."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "VHL is managed through a lifetime of photons: MRI tracks the hemangioblastomas studding the brain and spinal cord, ophthalmoscopy spots retinal angiomas, and CT watches the kidneys and pancreas — a relentless imaging surveillance that catches tumors early."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "VHL's kidney cancer heads for the lung when it spreads: the clear cell renal carcinomas these patients grow metastasize hematogenously, with the lungs a favored landing site for the disease that most threatens their survival."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "VHL's hemangioblastomas grow in a bed of glia: arising in the cerebellum, spinal cord, and retina, these vascular tumors are surrounded by reactive astrocytes, the brain's scar-forming cells responding to the slow-growing mass."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "VHL spills the body's red-cell signal: with the HIF brake gone, kidney and tumor pour out erythropoietin, raising the hemoglobin and hematocrit into polycythemia — while the HIF-2α drug belzutifan reverses it, often into anemia."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "The hemangioblastoma's signature cell is fat-laden: between its dense capillaries sit vacuolated 'stromal cells' stuffed with lipid, the neoplastic VHL-mutant cells that electron microscopy resolves and that define the tumor."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "VHL studs the pancreas with islet-cell tumors: its pancreatic neuroendocrine tumors are usually silent, but as tumors of the islets they can rarely oversecrete hormones such as glucagon, adding an endocrine twist to the syndrome."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains read VHL's tumors: inhibin-α and NSE confirm a cerebellar or retinal hemangioblastoma, while loss of carbonic anhydrase IX or characteristic markers helps tell its clear-cell kidney cancer from look-alikes on biopsy."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "VHL can drive the pressure up: its pheochromocytomas pour out catecholamines for episodic, dangerous hypertension, and the kidney tumors and their surgery add their own pressure effects — a reason these patients are screened for catecholamine excess."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Targeted therapy taxes the marrow: the VEGF tyrosine-kinase inhibitors long used for VHL kidney cancer suppress blood counts, dropping neutrophils, while the newer HIF-2α inhibitor belzutifan instead causes the anemia of switched-off erythropoietin."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "HIF turns on a growth gene in VHL tumors: with pVHL gone, stabilized HIF-2alpha drives cyclin D1, pushing the renal cells through the cell cycle — one way the loss of a single brake gene seeds the syndrome's kidney cancers."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "VHL's clear cell kidney cancers respond to immunotherapy: their HIF-driven biology and immune microenvironment make checkpoint inhibitors that unleash cytotoxic T cells a mainstay for advanced VHL-related renal cell carcinoma."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Two VHL features threaten the brain's circulation: EPO-driven polycythemia thickens the blood toward thrombosis, and CNS hemangioblastomas can bleed, both routes by which the syndrome can cause a stroke."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Losing VHL turns up an invasion receptor: HIF accumulation upregulates the MET receptor for hepatocyte growth factor, driving the scattering and invasiveness of VHL clear cell kidney cancer and offering another targetable kinase."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Saving the kidneys is a balancing act: recurrent clear cell cancers force repeated nephron-sparing surgeries, so the cumulative loss of kidney tissue across a lifetime of VHL pushes many patients toward chronic kidney disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Its hallmark brain tumor is built oddly: hemangioblastomas are a tangle of vessels, stromal cells and infiltrating mast cells, whose presence is a recognized histologic feature of these VHL-driven, EPO-secreting growths."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Lost pVHL turns on STAT3: in VHL-deficient cells HIF stabilization and STAT3 activation cooperate to drive the proliferation and vascular growth of clear-cell renal cancers and hemangioblastomas."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "pVHL normally restrains NF-κB: the von Hippel-Lindau protein suppresses NF-κB signaling, so its loss lifts that brake and adds pro-survival, pro-inflammatory signaling to the HIF-driven growth of VHL tumors."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its tumors and thick blood favor clotting: VHL drives clear-cell renal cancer and EPO-driven polycythemia, both of which raise blood viscosity and cancer-associated hypercoagulability, increasing thrombosis risk."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Its brain tumors and their surgery can spark seizures: CNS hemangioblastomas and the repeated neurosurgery they require can irritate the cortex into a seizure focus, adding epilepsy to the neurological toll of VHL."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A lifetime of surveillance wears on the mind: living with VHL's lifelong scans, repeated tumor surgeries and the inherited risk of multiple cancers across organs carries a heavy psychological burden and high rates of depression."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Repeated major surgery invites infection: the recurrent neurosurgery for hemangioblastomas and nephron-sparing operations for renal tumors that VHL demands carry cumulative perioperative risk of serious infection and sepsis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its pheochromocytomas can flood and stun the heart: the catecholamine-secreting adrenal tumors of VHL drive paroxysmal hypertension and can precipitate a catecholamine cardiomyopathy, a route toward acute heart failure."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Pancreatic tumors and surgery disturb glucose: VHL's pancreatic neuroendocrine tumors and cysts, and the resections they require, can damage islet function enough to produce diabetes."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Spinal hemangioblastomas press on the cord: VHL's recurrent tumors of the spinal cord and nerve roots compress neural tissue, producing chronic neuropathic pain and sensory loss alongside weakness."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Its HIF-2α inhibitor flips erythropoiesis to anemia: belzutifan, used to shrink VHL tumours, blocks the HIF pathway that drives EPO, commonly causing anemia — the mirror image of VHL's polycythemia."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "A lifetime of tumour surgery means a lifetime of wounds: the repeated craniotomies, spinal operations and partial nephrectomies VHL demands leave many surgical wounds that must heal over the years."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Endless tumours in many organs breed worry: the lifelong surveillance of brain, eye, kidney, adrenal and pancreas and the certainty of new tumours in VHL foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its hallmark tumours are in the CNS: haemangioblastomas of the cerebellum, brainstem and spinal cord — and of the retina — are the defining VHL lesions, causing headache, ataxia and cord compression."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is a multi-endocrine tumour syndrome: VHL produces catecholamine-secreting pheochromocytomas and pancreatic neuroendocrine tumours, demanding hormonal screening and careful perioperative blood-pressure control."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It fills the pancreas with lesions: serous cystadenomas and multiple pancreatic cysts are common in VHL, and the exocrine pancreas can be progressively replaced, complicating surgery for its neuroendocrine tumours."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its pheochromocytomas and HIF pathway hit the vessels: catecholamine surges cause hypertensive crises and cardiomyopathy, and VHL-loss HIF/VEGF activation drives the marked vascularity of its tumours."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its kidney cancer climbs to the lungs: the clear-cell renal cell carcinomas of VHL metastasise to the lungs, the commonest site of distant spread."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its renal cancer spreads to the nodes: metastatic VHL renal cell carcinoma involves regional and retroperitoneal lymph nodes, a poor prognostic feature."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A HIF inhibitor now treats it: belzutifan, which blocks HIF-2α stabilised by VHL loss, shrinks the renal cancers and haemangioblastomas of von Hippel-Lindau disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its kidney cancers respond to immunotherapy: VHL-driven clear-cell renal carcinoma is treated with checkpoint immunotherapy, and the pseudohypoxic HIF state shapes its immune microenvironment."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "A fellow CNS-and-eye tumour syndrome: like NF2 with its schwannomas and retinal hamartomas, VHL produces nervous-system and retinal tumours (haemangioblastomas) in an autosomal-dominant pattern."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "It grows pancreatic islet tumours: VHL causes pancreatic neuroendocrine tumours arising from islet cells, alongside the more common serous cysts, requiring imaging surveillance because larger lesions can metastasise."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Its tumours resist cytotoxics: the renal cancers, haemangioblastomas and neuroendocrine tumours of VHL respond poorly to conventional chemotherapy, so care centres on surgery, ablation and HIF-2α-targeted belzutifan instead."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "A shared pseudohypoxia pathway: SDH-deficient GIST, like VHL tumours, stabilises HIF through a pseudohypoxic state — the hypoxia-signalling axis that, via VHL and SDHB defects, unifies VHL pheochromocytomas, paragangliomas and these stromal tumours."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Two routes to pseudohypoxia: VHL loss directly stabilises HIF, while IDH-mutant glioma's 2-hydroxyglutarate inhibits the dioxygenases that degrade it—convergent HIF-driven, pseudohypoxic oncogenesis from different lesions."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It is a disease of runaway vessels: unrestrained HIF/VEGF in VHL drives the florid capillary proliferation of CNS and retinal hemangioblastomas and the hypervascularity of its renal cancers, vessel growth gone unchecked."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Congenital versus acquired polycythaemia: VHL and its pathway partners (EPAS1, EGLN1) cause hereditary HIF-driven erythrocytosis, the inherited mirror of the acquired, JAK2-driven erythrocytosis of myeloproliferative neoplasms."
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Two VEGF-driven retinal diseases: VHL retinal haemangioblastomas, like diabetic retinopathy, leak and proliferate under HIF-driven VEGF and are managed with laser photocoagulation and anti-VEGF therapy."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "Vascularity, opposite fates: VHL haemangioblastomas and glioblastoma are both intensely VEGF-driven, microvascular-rich CNS tumours, but the haemangioblastoma is benign and curable by resection while glioblastoma is relentlessly malignant."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Shared phaeochromocytoma risk: VHL and neurofibromatosis type 1 both predispose to phaeochromocytoma, two of the hereditary syndromes—with MEN2 and SDHx—behind catecholamine-secreting adrenal tumours."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Hemangioblastomas on the nerve roots: VHL's vascular tumours stud not only the cerebellum and retina but the spinal cord and its nerve roots, compressing them to cause pain and neurological deficits."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Metastatic renal cancer in bone: the clear-cell renal carcinomas of VHL metastasise to the skeleton, producing the highly vascular, osteolytic cortical-bone lesions typical of renal cell carcinoma."
  - target: 01-human/07-system/men4-syndrome
    relation: connects-to
    note: "Hereditary endocrine-tumour syndromes: like MEN1 and MEN4, VHL predisposes to pancreatic neuroendocrine tumours, one of several germline syndromes demanding lifelong surveillance of multiple endocrine organs."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "HIF-MYC interplay: stabilised HIF cooperates with MYC activity to drive the proliferation and metabolism of the clear-cell renal carcinomas of VHL disease."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Chromatin dysregulation: EZH2/polycomb activity, in the context of PBRM1 and BAP1 loss accompanying VHL inactivation, contributes to clear-cell renal carcinoma."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo activation: deregulated Hippo-YAP signalling contributes to the renal carcinomas and hemangioblastomas of VHL disease, alongside its dominant HIF axis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: HIF-driven cyclin D1 with CDK4/6 propels the clear-cell renal carcinoma cells of VHL disease through the G1 checkpoint."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: TERT reactivation maintains telomeres in the renal carcinomas of VHL disease, sustaining their proliferation."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K activation: PI3K/AKT/mTOR signalling, reinforced in VHL-deficient tumours, drives the growth of clear-cell renal carcinoma and hemangioblastoma."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "HIF-driven migration: loss of VHL stabilises HIF, which transcriptionally upregulates the CXCR4 receptor for CXCL12, promoting the invasive and metastatic behaviour of VHL-associated clear-cell renal carcinoma."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Neuroendocrine receptor: the pancreatic neuroendocrine tumours of VHL disease express somatostatin receptor 2, enabling DOTATATE PET surveillance and peptide-receptor radionuclide therapy of progressive lesions."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Hemangioblastoma peptide: adrenomedullin is a HIF target strongly expressed in VHL hemangioblastomas, where it contributes to the vascular permeability and cyst formation that produce the symptomatic mass effect."
  - target: 01-human/03-molecular/fh
    relation: connects-to
    note: "Pseudohypoxia parallel: VHL loss stabilises HIF directly, whereas fumarate-hydratase loss does so via accumulated fumarate — convergent pseudohypoxic routes that both cause hereditary phaeochromocytoma-paraganglioma and renal tumours through the same HIF endpoint."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Tumour vasculature: angiopoietin-Tie2 signalling, driven downstream of the constitutive HIF activation in VHL, helps build the strikingly vascular hemangioblastomas and clear-cell renal carcinomas that characterise the syndrome."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Noradrenergic phaeochromocytoma: VHL adrenal phaeochromocytomas secrete predominantly norepinephrine because they lack PNMT, a biochemical phenotype distinct from the epinephrine-producing RET/MEN2 tumours, useful in directing genetic testing."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "HIF-EGFR autocrine loop: VHL loss stabilises HIF, which induces TGF-α to drive an autocrine EGFR loop that sustains proliferation of VHL-deficient renal carcinoma and hemangioblastoma."
  - target: 01-human/03-molecular/bap1
    relation: connects-to
    note: "3p co-driver: BAP1, like VHL on chromosome 3p, is a renal tumour-suppressor, and its loss cooperates with VHL inactivation to drive the aggressive, high-grade clear-cell renal carcinoma of the disease."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Vascular phenotype: NOTCH signalling activated downstream of HIF in VHL-deficient hemangioblastomas and clear-cell renal carcinoma promotes their vascular, stem-like phenotype."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: HIF-driven cyclin-D1 (mapped) and CDK4/6 release E2F1 to push the proliferation of VHL-deficient tumours such as clear-cell renal carcinoma."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K restraint: PTEN limits the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped) that cooperates with HIF activation in the growth of VHL-associated tumours."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RTK-MAPK: MET, EGFR and PDGFR (all mapped) signal through the MAPK-ERK cascade in VHL-deficient tumours, complementing the pseudohypoxic HIF programme."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "Metabolic-RCC parallel: oncometabolite-producing IDH mutations parallel the FH and SDHB lesions (both already mapped) within the metabolically-driven hereditary renal tumours related to the VHL-HIF pseudohypoxia axis."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint: dysregulation of the RB1-E2F checkpoint (cyclin-D1, CDK4/6 and E2F1 already mapped) contributes to the proliferation of the renal and CNS tumours of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Survival signalling: JAK-STAT3 signalling (STAT3 already mapped) contributes to the survival and angiogenic signalling of VHL-associated tumours."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of VHL-associated clear-cell renal carcinoma, relevant to its immunotherapy responsiveness."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling governs the antitumour immune response and immune-evasion balance of the highly vascular, immunogenic VHL-associated renal carcinoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports angiogenesis and immune evasion in the HIF-driven, hypervascular tumours of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-mediated FOXO inactivation removes a pro-apoptotic brake, supporting survival of VHL-deficient clear-cell renal carcinoma cells (PI3K-AKT already mapped)."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling drives EMT and stromal remodeling in the progression of VHL-associated clear-cell renal carcinoma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunogenic VHL-associated renal carcinoma must evade."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt/β-catenin signaling of the pseudohypoxic VHL-deficient tumors."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation restrains apoptosis in the VHL-associated tumors."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of VHL-associated tumors."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of MET and other receptors (MET already mapped) contributes to the invasion of the tumors of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the tumors of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival of the VHL-deficient, pseudohypoxic cells of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the pseudohypoxic metabolic reprogramming of the tumors of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of the tumors of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of von Hippel-Lindau disease."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "RCC immunotherapy: the clear cell renal cell carcinomas that dominate VHL disease are immunogenic, historically responsive to high-dose IL-2 and now to checkpoint inhibitors, an immune-targetable dimension complementing the HIF-directed belzutifan."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Chromaffin secretion: the phaeochromocytomas of VHL disease release catecholamines by calcium-triggered granule exocytosis, tying the syndrome's adrenal tumours to the same secretory physiology as sporadic phaeochromocytoma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron and erythrocytosis: HIF stabilisation in VHL disease drives erythropoietin (already mapped) and reshapes iron handling, with transferrin-delivered iron supplying the erythrocytosis and the intensely vascular hemangioblastomas."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "RCC immunotherapy: the clear-cell renal cell carcinoma of VHL disease is among the most immunotherapy-responsive cancers, and MHC class II antigen presentation shapes the T-cell response to the checkpoint inhibitors used in its metastatic form."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint blockade: PD-1 inhibitors, alone or with antiangiogenics targeting the HIF-driven VEGF (already mapped), are standard for advanced VHL-associated clear-cell renal cell carcinoma, exploiting its immunogenicity."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Combination immunotherapy: CTLA-4 blockade combined with PD-1 inhibition (already mapped) is a frontline option for the metastatic clear-cell renal cell carcinoma that develops in VHL disease, deepening responses in this immunoresponsive tumour."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Haemangioblastoma vasculature: nitric oxide with the strongly HIF-driven VEGF and angiopoietin (already mapped) shapes the rich vasculature of the haemangioblastomas that characterise VHL disease, part of their angiogenic biology."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), part of the immune evasion of the VHL-associated clear-cell renal cell carcinoma that checkpoint blockade targets."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Erythropoietin and iron: the stabilised HIF of VHL disease drives erythropoietin (already mapped) and polycythaemia, raising the demand for iron, and paraneoplastic erythropoietin from haemangioblastomas can worsen the erythrocytosis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the VHL-associated clear-cell renal cell carcinoma, part of its immune microenvironment."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Clear-cell lipid: the VHL-driven clear-cell renal cell carcinoma accumulates cholesterol esters and lipid, giving the clear cytoplasm that names it, part of the metabolic rewiring downstream of the constitutive HIF (already mapped)."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Obesity and adipokines: obesity is a risk factor for renal cell carcinoma, and the fall in the adipokine adiponectin is part of the metabolic milieu that can promote the clear-cell renal cell carcinoma of VHL disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immune microenvironment of the VHL-associated tumours, including the clear-cell renal cell carcinoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and RCC risk: the adipokine leptin, with the fall in adiponectin (already mapped), links the obesity that raises renal-cell-carcinoma risk to the metabolic milieu promoting the clear-cell RCC of VHL disease."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the pro-inflammatory adipokine milieu of the obesity implicated in the renal-cell-carcinoma risk of VHL disease."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "EPO-hepcidin axis: the erythropoietin (already mapped)-driven erythroferrone suppresses the hepcidin to mobilise the iron (already mapped) for the polycythaemia of the HIF-activated (already mapped) VHL disease."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "RCC immunogenicity: type-I interferon, downstream of the cGAS-STING (already mapped) innate sensing, shapes the immunogenicity and the checkpoint (PD-1 already mapped) response of the clear-cell renal cell carcinoma of VHL disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the M2 (IL-4 and IL-13 already mapped) tumour-associated macrophages of the immunosuppressive microenvironment of the clear-cell renal cell carcinoma of VHL disease."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity of the immunogenic clear-cell renal cell carcinoma of VHL disease."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the renal-cell-carcinoma immune microenvironment of VHL disease."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the immune microenvironment of the VHL-associated tumours."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4/IL-5 and IL-17 already mapped) cytokines shaping the immune microenvironment of the VHL-associated tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the VHL-associated tumours."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the VHL-associated tumours."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts the checkpoint (PD-1 already mapped) response of the VHL-associated clear-cell renal cell carcinoma (already mapped)."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a contribute to the inflammatory and immunosuppressive dimension of the highly vascular VHL-associated tumour microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling recruits and polarises the myeloid cells to an immunosuppressive phenotype in the VHL-associated tumour microenvironment."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Central complement: the complement C3, upstream of the C5 and C5aR1 (already mapped), is the pivot of the complement activation within the highly vascular VHL-associated tumour microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the VHL-associated tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), evading the complement attack within the tumour microenvironment."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways within the VHL-associated tumour microenvironment, complementing the alternative-pathway control by factor H (already mapped)."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Stromal alarmin: TSLP from the VHL tumour stroma (fibroblast, VEGF already mapped) activates mast cells (already mapped) and dendritic cells (already mapped), sustaining the immunosuppressive type-2 microenvironment of haemangioblastoma and ccRCC."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "HIF-driven kinin axis: bradykinin production is enhanced by the HIF-1α (already mapped) driven upregulation of tissue kallikrein in VHL-disease tumours, amplifying the vascular permeability and angiogenesis (VEGF, angiopoietin already mapped) of the haemangioblastomas."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Hypoxic ECM remodelling: periostin expression is upregulated by HIF-1α (already mapped) in the VHL-associated tumour stroma, contributing to the desmoplastic ECM and invasion of the clear-cell RCC and pNET lesions of VHL disease."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell vascular niche: histamine released by mast cells (already mapped) in the haemangioblastoma and ccRCC microenvironment of VHL disease amplifies local vascular permeability and the VEGF-driven (already mapped) neo-angiogenesis of the tumour stroma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian antioxidant in hypoxia: melatonin reduces the oxidative stress generated by the HIF-1α (already mapped) driven hypermetabolic state of VHL-disease tumours; melatonin receptor signalling may modulate haemangioblastoma growth."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Hypoxic prolactin axis: HIF-1α (already mapped) upregulates prolactin secretion; elevated prolactin in VHL-associated polycythaemia and tumour states stimulates haematopoiesis and may modulate the immune microenvironment of ccRCC lesions."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "VHL testosterone: androgen receptor (AR) signalling promotes the growth of VHL-associated clear cell renal cell carcinoma (kidney already mapped); testosterone-driven AR activity upregulates HIF-1α (already mapped) target genes and the VEGF (already mapped) angiogenic axis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "VHL serotonin: serotonin-secreting pNETs (pancreatic neuroendocrine tumours) are a manifestation of VHL disease; 5-HT receptor signalling on ccRCC cells (kidney already mapped) promotes tumour proliferation and modulates HIF-1α (already mapped) driven therapeutic resistance."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "VHL oxytocin: oxytocin receptor expression on VHL-associated clear cell renal carcinoma (kidney already mapped) and haemangioblastoma cells may modulate tumour angiogenesis via VEGF (already mapped) suppression and immune microenvironment remodelling in VHL-disease."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "VHL vasopressin: vasopressin modulates renal tubular water reabsorption via aquaporin-2 (kidney already mapped); in VHL disease, AVP V2 receptor signalling intersects HIF-1α (already mapped) and VEGF (already mapped) axes in ccRCC and pNET-associated ectopic hormone secretion."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "VHL selenium: selenium-dependent GPX4 protects VHL-deficient ccRCC cells from ferroptosis; GPX4 upregulation is a resistance mechanism downstream of the HIF-1α (already mapped)-VEGF (already mapped) axis in VHL tumours, and selenium status modulates tumour oxidative stress."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "VHL iodine: iodine-dependent thyroid hormones modulate VEGF (already mapped) and HIF-1α (already mapped) pathway activity in VHL-associated ccRCC and haemangioblastoma; hypothyroidism may alter the angiogenic milieu and metabolic rate of VHL tumour cells."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "VHL sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplify HIF-1α (already mapped) and VEGF (already mapped) and mTOR (already mapped) angiogenic cascade of VHL disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "VHL magnesium: magnesium, as mTOR (already mapped) cofactor in endothelial-cell (already mapped) and macrophages (already mapped), supports angiogenesis; magnesium deficiency amplifies HIF-1α (already mapped) and VEGF (already mapped) and NF-κB (already mapped) cascade of VHL."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "VHL copper: copper, as lysyl oxidase cofactor in endothelial-cell (already mapped), drives VEGF (already mapped) angiogenesis in VHL tumours; copper deficiency impairs macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour immunity in VHL disease."
---

# VHL Disease

## Overview

**VHL disease** (von Hippel-Lindau disease) is an autosomal dominant hereditary cancer predisposition syndrome caused by germline pathogenic variants in the **VHL** tumor suppressor gene (chromosome 3p25.3; 3 exons; encodes 213 aa pVHL). VHL disease is characterized by a predisposition to a distinctive set of hypervascular tumors and cysts including **hemangioblastomas** of the CNS (cerebellum, spinal cord, brainstem) and retina, **clear cell renal cell carcinoma (ccRCC)**, **pheochromocytoma** (in type 2 VHL), **pancreatic serous cystadenomas and neuroendocrine tumors (pNET)**, and **endolymphatic sac tumors (ELST)**. The molecular basis is loss of pVHL function → constitutive HIF-1α/2α accumulation → HIF target gene overexpression (VEGF, EPO, PDGF, GLUT1) driving the highly vascularized tumor phenotype. VHL disease affects approximately **1 in 36,000** individuals, with a new mutation rate of ~20%. The 2021 FDA approval of **belzutifan** — the first HIF-2α inhibitor — for treatment of VHL disease-related tumors represents a paradigm shift from surgical to targeted medical management [^lonser-2003-vhl-disease] [^choueiri-2020-hif2-rcc].

**VHL disease type classification (genotype-phenotype):**

| Type | VHL mutation | Pheochromocytoma | CNS hemangioblastoma | ccRCC | Key notes |
|---|---|---|---|---|---|
| Type 1 | Truncating (nonsense, frameshift, deletion) | No (<1%) | Yes | Yes (high risk ~45%) | Most common; no pheo; high RCC |
| Type 2A | Missense (C162F, V166A, etc.) | Yes | Yes | No/low | Pheo + hemangioblastoma; low RCC |
| Type 2B | Missense (R167Q, L188V, W117R) | Yes | Yes | Yes | Pheo + RCC + hemangioblastoma; worst |
| Type 2C | Missense (L188V some, others) | Yes only | No/minimal | No | Pheo only; rare subtype |

The genotype-phenotype correlation reflects the degree of pVHL function retained: truncating variants = complete LOF = no VHL function = type 1; certain missense variants retain some VHL function in non-pheochromocytoma contexts but specifically impair pVHL interaction with a different substrate that suppresses catecholamine synthesis → pheo risk.

## Structure

### Genetic basis

**VHL gene (3p25.3):**
- 3 exons; 213 aa (pVHL30, cytoplasmic/nuclear) and a shorter isoform (pVHL19, 160 aa) initiated from internal Met; both functional
- Germline pathogenic variant spectrum: missense (~45%), nonsense (~25%), frameshift (~18%), partial deletions (~11%; MLPA required), splice (~1%), complete gene deletion (<1%)
- Penetrance: ~97% lifetime penetrance for at least one VHL manifestation by age 65 (essentially complete)
- De novo rate: ~20% of VHL disease; test parents of a proband
- Somatic second hit: LOH at 3p25 detectable in >90% of VHL-associated tumors; somatic promoter methylation as alternative second hit in sporadic ccRCC (~10%)

**pVHL structure:**
- pVHL contains an **α-domain** (scaffold domain) and a **β-domain** (hydroxyproline-binding substrate recognition domain)
- β-domain: forms a deep hydrophobic pocket that accommodates the LXXLAP-OH (hydroxyproline) motif of HIF-α; Tyr98, His115 and other residues in the pocket contact the hydroxyproline directly
- α-domain: binds Elongin C (ELOC) → ELOC-ELOB-CUL2-RBX1 assembled into the E3 ubiquitin ligase complex → RING domain (RBX1) activates E2 ubiquitin-conjugating enzyme → HIF-α poly-ubiquitination → 26S proteasome degradation
- pVHL has functions beyond HIF degradation: stabilizes microtubules, regulates primary ciliogenesis, modulates fibronectin matrix assembly, promotes differentiation of renal tubular epithelium — many of these contribute to tumor suppression beyond HIF pathway

**Somatic VHL in sporadic ccRCC:**
- VHL somatic biallelic inactivation in ~90% of sporadic clear cell RCC; most common mechanism: one allele lost by LOH at 3p, second allele mutated or methylated
- Sporadic ccRCC VHL mutations: same types as germline but both hits are somatic; no other VHL disease features in sporadic VHL-mutant RCC patients

## Function

### CNS and retinal hemangioblastomas

**Hemangioblastoma biology:**
- Highly vascularized cystic tumors with a mural nodule; the cyst wall is benign but the nodule contains the actual neoplastic stromal cells (pVHL-LOH confirmed in stromal cells)
- Cell of origin debated: hemangioblast (primitive vascular progenitor) vs neural/glial progenitor; gene expression profiling suggests embryonic mesodermal origin
- VHL LOF in stromal cells → HIF-2α/EPAS1 stabilization → massive VEGF overexpression → recruitment of surrounding vasculature → the characteristic hemangioblastoma blood vessel-rich cystic structure
- HIF-2α appears to be the dominant HIF isoform in hemangioblastoma stromal cells (unlike other VHL-related tumors where HIF-1α also contributes)

**CNS hemangioblastoma locations (VHL disease):**
- Cerebellum: ~55% of CNS hemangioblastomas; most common location; often in posterior fossa
- Spinal cord: ~44%; all spinal levels; may cause myelopathy, syringomyelia
- Brainstem: ~18%; medulla most common; high surgical risk
- Supratentorial: ~5%; rare; may involve cerebrum

**Presentation and management:**
- Symptoms: cerebellar ataxia, headache (cerebellar); limb weakness, sensory loss, bladder dysfunction (spinal); dysphagia, dysarthria (brainstem)
- Polycythemia: hemangioblastoma stromal cells produce EPO (HIF-2α-driven) → paraneoplastic erythrocytosis; rare (more common in VHL type 1)
- Surveillance: annual brain + spine MRI from age 11
- Treatment: symptomatic or enlarging hemangioblastoma → surgical resection (mural nodule excision); stereotactic radiosurgery (SRS) for small, surgically inaccessible lesions; belzutifan (see below) stabilizes or shrinks hemangioblastomas

**Retinal hemangioblastoma (retinal capillary hemangioma, RCH):**
- Present in ~25-60% of VHL patients; often the earliest presenting tumor (mean age 25); may be bilateral (multiple lesions in one or both eyes)
- Peripheral lesion: treatable with laser photocoagulation or cryotherapy; anti-VEGF (bevacizumab intravitreal) for some lesions
- Juxtapapillary lesion: difficult to treat; can affect optic disc → optic atrophy; higher risk of vision loss
- Surveillance: annual dilated fundus exam from age 1 (or at diagnosis of VHL); fluorescein angiography to define lesion boundaries

### Clear cell renal cell carcinoma (ccRCC)

- **Lifetime risk**: ~25-45% for VHL type 1 and type 2B; lower for type 2A/2C
- **Biology**: VHL LOF → HIF-2α → VEGF → angiogenesis; PDGF → stromal growth; CXCR4/CXCL12 → invasion; metabolic reprogramming (Warburg shift, lipid accumulation — clear cell morphology = glycogen and lipid-filled cytoplasm)
- **Bilaterality and multifocality**: VHL ccRCC is characteristically bilateral and multifocal; dozens to hundreds of early lesions may be present; risk of developing new lesions over decades
- **3 cm threshold**: standard surveillance/surgical rule — lesions ≤3 cm: active surveillance (annual MRI/CT); lesions >3 cm: nephron-sparing surgery (NSS) recommended due to metastatic risk rising sharply above 3 cm; RFA/cryoablation as alternatives in bilateral disease to preserve renal function
- **Belzutifan (Welireg)**: oral HIF-2α inhibitor (PT2977; MK-6482); FDA approved August 2021; LITESPARK-004 trial: ORR ~49% for RCC (23% CR, 26% PR), ~93% ORR for CNS hemangioblastoma; indicated for VHL disease-associated RCC, CNS hemangioblastoma, and pNET (not requiring immediate surgery)
- **Advanced/metastatic VHL-ccRCC**: VEGF pathway inhibitors (sunitinib, pazopanib, cabozantinib); PD-1/PD-L1 + VEGF combination (nivolumab+cabozantinib, pembrolizumab+axitinib) effective in VHL-associated metastatic ccRCC similar to sporadic ccRCC

### Pancreatic manifestations

- **Serous cystadenomas**: most common pancreatic lesion (~70% of VHL patients); benign honeycomb cyst clusters; monitoring with MRI; rare complication (biliary obstruction if very large)
- **Pancreatic NETs (pNET)**: ~15% of VHL patients; typically non-functional (no excess hormone production); risk of malignancy correlates with size; ≥3 cm or doubling time <2 years → resection; belzutifan approved for VHL-related pNET requiring no immediate surgery

### Pheochromocytoma (VHL type 2)

- VHL type 2 pheo: median age at diagnosis ~30 years; often bilateral (>50% of VHL pheo); usually adrenal (rarely extra-adrenal); typically secretes normetanephrine (norepinephrine-producing; NMN elevated, MN not elevated)
- Plasma free metanephrines: annual screening from age 8 in type 2 families
- Treatment: surgical adrenalectomy; cortical-sparing adrenalectomy for bilateral pheo (to avoid permanent Addison's)

### Endolymphatic sac tumor (ELST)

- Present in ~10-15% of VHL patients; locally invasive tumor of the endolymphatic sac (posterior petrous bone); hearing loss (sensorineural), tinnitus, vertigo → mimics Menière's disease
- Surveillance: MRI of temporal bones at diagnosis and every 3-5 years; audiologic testing
- Treatment: surgical excision; early detection and resection preserves hearing better than late treatment

## Pathology

### Surveillance program (VHL disease)

| Age | Screening modality | Target |
|---|---|---|
| Annual, from age 1 | Dilated funduscopy | Retinal hemangioblastoma |
| Annual, from age 8 | Plasma free metanephrines | Pheochromocytoma (type 2) |
| Annual, from age 11 | Brain + spine MRI | CNS hemangioblastoma |
| Annual, from age 15 | Abdominal MRI or CT | RCC, pancreatic NETs/cysts |
| Annual, from age 11 | Audiologic testing + petrous MRI | ELST |

**Surgical principles:**
- NSS (nephron-sparing surgery): bilateral multifocal RCC → preserve nephrons; laparoscopic/robotic approaches preferred; R0 resection of mural nodule only in hemangioblastoma
- Cortical-sparing adrenalectomy: bilateral pheo → preserve cortex where possible to avoid Addison's
- Belzutifan as bridge therapy: used to stabilize lesions before surgery or as an alternative to surgery in patients with multiple lesions not yet requiring intervention

**VHL disease vs. other hereditary RCC syndromes:**

| Syndrome | Gene | RCC histology | Other features |
|---|---|---|---|
| VHL disease | VHL | Clear cell | Hemangioblastoma, pheo, pNET |
| BHD | FLCN | Chromophobe, hybrid oncocytic | Fibrofolliculoma, lung cysts |
| HLRCC | FH | Type 2 papillary | Cutaneous/uterine leiomyoma |
| Hereditary papillary RCC | MET | Type 1 papillary | Multifocal type 1 pRCC only |
| SDH-related | SDHB/C/D | Clear cell or chromophobe | Paraganglioma, pheo, GIST |

## Connections

- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — Germline VHL LOF causes VHL disease via constitutive HIF-1α/2α accumulation; VHL β-domain recognizes EGLN1-hydroxylated HIF → ubiquitination; missense VHL variants predict pheo risk (type 2A/2B/2C) vs truncating (type 1, high RCC); belzutifan targets HIF-2α downstream.
- `connects-to` → **[EGLN1](../../03-molecular/egln1/README.md)** — EGLN1 (PHD2) hydroxylates HIF-1α/2α under normoxia for VHL-mediated degradation; in VHL disease, VHL LOF renders HIF constitutively stable regardless of EGLN1 activity; EGLN1 inhibitors (PHD inhibitors) activate HIF for CKD anemia treatment by the same mechanism as VHL LOF.
- `connects-to` → **[Renal Cell Carcinoma](../../07-system/renal-cell-carcinoma/README.md)** — Clear cell RCC (ccRCC) is the most common VHL disease tumor (~25-45% lifetime risk); VHL LOF → HIF-2α/VEGF → neovascularization → ccRCC; NSS (nephron-sparing surgery) for ≤3 cm tumors; belzutifan (HIF-2α inhibitor) FDA-approved for VHL disease-associated ccRCC since 2021.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../../07-system/pheochromocytoma-paraganglioma/README.md)** — VHL disease type 2 (missense variants) carries pheochromocytoma risk (~8-20%); VHL pheo is typically bilateral, benign, adrenal, and normetanephrine-secreting; VHL-pheo driven by HIF-2α pseudohypoxia → catecholamine biosynthesis upregulation; resection curative.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — VHL disease is fundamentally a HIF disease: without functional pVHL, HIF-1α/2α escape degradation and constitutively switch on VEGF, EPO, PDGF, and GLUT1, producing the hypervascular hemangioblastomas, clear-cell RCC, and pheochromocytomas; belzutifan blocks HIF-2α directly.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Hemangioblastomas — benign but hypervascular cystic tumors with a HIF-2α-driven mural nodule — are the hallmark CNS lesions of VHL, clustering in cerebellum (~55%), spinal cord (~44%), and brainstem; annual brain and spine MRI from age 11 catches them.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Retinal hemangioblastoma is often the earliest VHL tumor, appearing around age 25 and frequently bilateral; peripheral lesions are treated with laser or cryotherapy and intravitreal anti-VEGF, so dilated fundus screening begins in the first year of life.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Von Hippel-Lindau and tuberous sclerosis are both dominant phakomatosis syndromes whose tumors need a second hit, but differ in driver: VHL loss stabilizes HIF to fuel angiogenic tumors (hemangioblastoma, ccRCC, pheo) while TSC loss hyperactivates mTOR — both hit the kidney.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The pancreas is a major VHL site: most carriers develop pancreatic cysts and serous cystadenomas (usually benign), but pancreatic neuroendocrine tumors arise in ~10-17% and can metastasize, so pancreatic imaging is part of lifelong VHL surveillance, guided by size and growth.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — VHL disease can cause polycythemia: pVHL loss stabilizes HIF, so hemangioblastomas (and hypomorphic germline VHL, as in Chuvash polycythemia) drive excess erythropoietin → high hematocrit; the same VHL-HIF-EPO axis is exploited by PHD inhibitors that raise EPO to treat anemia.
- `connects-to` → **[HLRCC](../hlrcc/README.md)** — VHL disease and HLRCC are hereditary kidney-cancer syndromes converging on pseudohypoxia: VHL loss stabilizes HIF directly, while HLRCC's FH loss raises fumarate that blocks HIF prolyl-hydroxylases—but VHL causes clear-cell RCC and HLRCC an aggressive papillary type.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — VHL disease predisposes to pancreatic neuroendocrine tumors: alongside its hemangioblastomas, clear-cell RCC, and pheochromocytomas, germline VHL loss drives often-multifocal panNETs, so a young patient with a panNET warrants VHL (and MEN1) testing.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Hemangioblastoma, the signature VHL tumor, is a richly vascular tumor of endothelial proliferation: VHL loss stabilizes HIF and floods the tissue with VEGF, driving the capillary-dense masses of the retina and cerebellum that define the syndrome.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — VHL and MEN1 are both dominant tumor-suppressor syndromes producing pancreatic tumors via different genes: VHL gives hemangioblastomas, clear-cell RCC, pheochromocytoma and pancreatic NETs, while MEN1 gives parathyroid, islet and pituitary tumors.
- `connects-to` → **[Birt-Hogg-Dubé Syndrome](../birt-hogg-dube-syndrome/README.md)** — VHL and Birt-Hogg-Dubé are hereditary kidney-cancer syndromes with distinct histologies: VHL's pVHL loss drives clear-cell RCC, while BHD's FLCN loss gives chromophobe/oncocytic tumors, lung cysts and skin fibrofolliculomas—each a different RCC.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — VHL connects to polycythemia through the HIF pathway: pVHL normally degrades HIF, so its loss stabilizes HIF and drives erythropoietin—and the germline VHL mutation of Chuvash polycythemia causes congenital erythrocytosis, a primary cause of high red-cell mass.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is VHL disease's most lethal target: VHL loss stabilizes HIF, so carriers develop multiple, recurrent clear cell renal cell carcinomas—the leading cause of death—prompting lifelong renal imaging and nephron-sparing surgery to preserve kidney function.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VHL disease is the prototype of VEGF-driven tumors: losing VHL stabilizes HIF, which floods tissue with VEGF to build the vessel-rich hemangioblastomas and renal cancers—so HIF-2a (belzutifan) and anti-VEGF drugs directly target the syndrome's core defect.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — VHL sits at the heart of cellular oxygen sensing: the VHL protein normally tags HIF for destruction when oxygen is plentiful, so its loss makes cells behave as if hypoxic—pseudohypoxia driving erythropoietin, angiogenesis and tumor growth even in normal oxygen.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal gland is a key VHL target: pheochromocytomas of the adrenal medulla, often bilateral and noradrenaline-secreting, arise in VHL and demand lifelong surveillance—a different organ lesion from the renal and CNS tumors that dominate the syndrome.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — VHL leaves a quiet mark on the reproductive system: epididymal cystadenomas in men and broad-ligament cystadenomas in women are characteristic benign tumors—rarely symptomatic but, when bilateral, near-diagnostic clues to the syndrome.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — VHL's broken oxygen sensing inflates red cells: failure to degrade HIF raises erythropoietin, driving excess erythrocyte production—the basis of Chuvash polycythemia, a milder VHL variant where the bone marrow overmakes red cells without a tumor.
- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — VHL disease is fundamentally a HIF-2alpha (EPAS1) disorder: losing pVHL stops degradation of EPAS1, so it constitutively drives VEGF and growth—the basis for belzutifan, a HIF-2alpha inhibitor now treating VHL-related kidney tumors and hemangioblastomas.
- `connects-to` → **[SDHB](../../03-molecular/sdhb/README.md)** — VHL and SDHB cause 'pseudohypoxia' the same way: pVHL loss and SDHB loss both stabilize HIF as if oxygen were low, driving pheochromocytoma and paraganglioma—so two different genes converge on one hypoxia-mimicking cancer mechanism.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — HIF-2alpha links VHL to iron and red cells: the EPAS1 factor that accumulates in VHL governs erythropoietin and intestinal iron absorption, explaining the polycythemia seen when this hypoxia pathway runs unchecked.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — VHL tumors lean on mTOR alongside HIF: pseudohypoxic HIF signaling and mTOR together drive the clear cell kidney cancers and hemangioblastomas, so mTOR inhibitors—and now the HIF-2α blocker belzutifan—are used against VHL disease.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — VHL clear cell kidney cancers are immune-hot yet shielded by regulatory T cells: they draw T-cell infiltrates that respond to checkpoint drugs, but Tregs restrain the attack, shaping how immunotherapy works in VHL-related RCC.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — VHL tumors face NK-cell surveillance: their HIF-driven stress and altered MHC can expose them to natural killer cells, an innate defense being explored to complement checkpoint therapy against the syndrome's vascular tumors.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — VHL tumors lean on the mTOR-AKT growth axis alongside their HIF defect: pseudohypoxic signaling pairs with PI3K-AKT-mTOR activity to fuel the kidney cancers and hemangioblastomas, so mTOR-pathway drugs join the HIF inhibitor belzutifan.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are enlisted against VHL's tumors: as belzutifan and immunotherapy enter VHL care, antigen-presenting dendritic cells help prime the T-cell response to the HIF-driven kidney and brain tumors.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — VHL studs the abdominal organs with cysts and tumors, including the liver: alongside the classic kidney, pancreas and adrenal lesions, hepatic cysts and hemangiomas occur, reflecting the syndrome's vascular, cyst-forming tendency.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — VHL drives the bone marrow to overproduce red cells: unchecked HIF raises erythropoietin, so the marrow churns out erythrocytes, causing the polycythemia that can accompany the syndrome and its EPO-secreting tumors.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — VHL's hemangioblastomas grow within the nervous system: these vascular tumors of the cerebellum, brainstem and spinal cord compress neurons, producing the headaches, ataxia and neurological deficits that often first signal the disease.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Losing VHL switches on PDGF among its HIF-driven growth factors: this angiogenic signal helps build the tumors' rich vasculature, and is one of the targets of the kinase inhibitors used against VHL-related kidney cancer.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — VHL is managed through a lifetime of photons: MRI tracks the hemangioblastomas studding the brain and spinal cord, ophthalmoscopy spots retinal angiomas, and CT watches the kidneys and pancreas — a relentless imaging surveillance that catches tumors early.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — VHL's kidney cancer heads for the lung when it spreads: the clear cell renal carcinomas these patients grow metastasize hematogenously, with the lungs a favored landing site for the disease that most threatens their survival.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — VHL's hemangioblastomas grow in a bed of glia: arising in the cerebellum, spinal cord, and retina, these vascular tumors are surrounded by reactive astrocytes, the brain's scar-forming cells responding to the slow-growing mass.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — VHL spills the body's red-cell signal: with the HIF brake gone, kidney and tumor pour out erythropoietin, raising the hemoglobin and hematocrit into polycythemia — while the HIF-2α drug belzutifan reverses it, often into anemia.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — The hemangioblastoma's signature cell is fat-laden: between its dense capillaries sit vacuolated 'stromal cells' stuffed with lipid, the neoplastic VHL-mutant cells that electron microscopy resolves and that define the tumor.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — VHL studs the pancreas with islet-cell tumors: its pancreatic neuroendocrine tumors are usually silent, but as tumors of the islets they can rarely oversecrete hormones such as glucagon, adding an endocrine twist to the syndrome.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains read VHL's tumors: inhibin-α and NSE confirm a cerebellar or retinal hemangioblastoma, while loss of carbonic anhydrase IX or characteristic markers helps tell its clear-cell kidney cancer from look-alikes on biopsy.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — VHL can drive the pressure up: its pheochromocytomas pour out catecholamines for episodic, dangerous hypertension, and the kidney tumors and their surgery add their own pressure effects — a reason these patients are screened for catecholamine excess.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Targeted therapy taxes the marrow: the VEGF tyrosine-kinase inhibitors long used for VHL kidney cancer suppress blood counts, dropping neutrophils, while the newer HIF-2α inhibitor belzutifan instead causes the anemia of switched-off erythropoietin.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — HIF turns on a growth gene in VHL tumors: with pVHL gone, stabilized HIF-2alpha drives cyclin D1, pushing the renal cells through the cell cycle — one way the loss of a single brake gene seeds the syndrome's kidney cancers.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — VHL's clear cell kidney cancers respond to immunotherapy: their HIF-driven biology and immune microenvironment make checkpoint inhibitors that unleash cytotoxic T cells a mainstay for advanced VHL-related renal cell carcinoma.
- `connects-to` → **[Stroke](../stroke/README.md)** — Two VHL features threaten the brain's circulation: EPO-driven polycythemia thickens the blood toward thrombosis, and CNS hemangioblastomas can bleed, both routes by which the syndrome can cause a stroke.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — Losing VHL turns up an invasion receptor: HIF accumulation upregulates the MET receptor for hepatocyte growth factor, driving the scattering and invasiveness of VHL clear cell kidney cancer and offering another targetable kinase.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Saving the kidneys is a balancing act: recurrent clear cell cancers force repeated nephron-sparing surgeries, so the cumulative loss of kidney tissue across a lifetime of VHL pushes many patients toward chronic kidney disease.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Its hallmark brain tumor is built oddly: hemangioblastomas are a tangle of vessels, stromal cells and infiltrating mast cells, whose presence is a recognized histologic feature of these VHL-driven, EPO-secreting growths.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Lost pVHL turns on STAT3: in VHL-deficient cells HIF stabilization and STAT3 activation cooperate to drive the proliferation and vascular growth of clear-cell renal cancers and hemangioblastomas.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — pVHL normally restrains NF-κB: the von Hippel-Lindau protein suppresses NF-κB signaling, so its loss lifts that brake and adds pro-survival, pro-inflammatory signaling to the HIF-driven growth of VHL tumors.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its tumors and thick blood favor clotting: VHL drives clear-cell renal cancer and EPO-driven polycythemia, both of which raise blood viscosity and cancer-associated hypercoagulability, increasing thrombosis risk.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Its brain tumors and their surgery can spark seizures: CNS hemangioblastomas and the repeated neurosurgery they require can irritate the cortex into a seizure focus, adding epilepsy to the neurological toll of VHL.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A lifetime of surveillance wears on the mind: living with VHL's lifelong scans, repeated tumor surgeries and the inherited risk of multiple cancers across organs carries a heavy psychological burden and high rates of depression.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Repeated major surgery invites infection: the recurrent neurosurgery for hemangioblastomas and nephron-sparing operations for renal tumors that VHL demands carry cumulative perioperative risk of serious infection and sepsis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its pheochromocytomas can flood and stun the heart: the catecholamine-secreting adrenal tumors of VHL drive paroxysmal hypertension and can precipitate a catecholamine cardiomyopathy, a route toward acute heart failure.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Pancreatic tumors and surgery disturb glucose: VHL's pancreatic neuroendocrine tumors and cysts, and the resections they require, can damage islet function enough to produce diabetes.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Spinal hemangioblastomas press on the cord: VHL's recurrent tumors of the spinal cord and nerve roots compress neural tissue, producing chronic neuropathic pain and sensory loss alongside weakness.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Its HIF-2α inhibitor flips erythropoiesis to anemia: belzutifan, used to shrink VHL tumours, blocks the HIF pathway that drives EPO, commonly causing anemia — the mirror image of VHL's polycythemia.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — A lifetime of tumour surgery means a lifetime of wounds: the repeated craniotomies, spinal operations and partial nephrectomies VHL demands leave many surgical wounds that must heal over the years.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Endless tumours in many organs breed worry: the lifelong surveillance of brain, eye, kidney, adrenal and pancreas and the certainty of new tumours in VHL foster chronic health anxiety alongside depression.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its hallmark tumours are in the CNS: haemangioblastomas of the cerebellum, brainstem and spinal cord — and of the retina — are the defining VHL lesions, causing headache, ataxia and cord compression.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is a multi-endocrine tumour syndrome: VHL produces catecholamine-secreting pheochromocytomas and pancreatic neuroendocrine tumours, demanding hormonal screening and careful perioperative blood-pressure control.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It fills the pancreas with lesions: serous cystadenomas and multiple pancreatic cysts are common in VHL, and the exocrine pancreas can be progressively replaced, complicating surgery for its neuroendocrine tumours.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its pheochromocytomas and HIF pathway hit the vessels: catecholamine surges cause hypertensive crises and cardiomyopathy, and VHL-loss HIF/VEGF activation drives the marked vascularity of its tumours.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its kidney cancer climbs to the lungs: the clear-cell renal cell carcinomas of VHL metastasise to the lungs, the commonest site of distant spread.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its renal cancer spreads to the nodes: metastatic VHL renal cell carcinoma involves regional and retroperitoneal lymph nodes, a poor prognostic feature.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A HIF inhibitor now treats it: belzutifan, which blocks HIF-2α stabilised by VHL loss, shrinks the renal cancers and haemangioblastomas of von Hippel-Lindau disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its kidney cancers respond to immunotherapy: VHL-driven clear-cell renal carcinoma is treated with checkpoint immunotherapy, and the pseudohypoxic HIF state shapes its immune microenvironment.
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — A fellow CNS-and-eye tumour syndrome: like NF2 with its schwannomas and retinal hamartomas, VHL produces nervous-system and retinal tumours (haemangioblastomas) in an autosomal-dominant pattern.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — It grows pancreatic islet tumours: VHL causes pancreatic neuroendocrine tumours arising from islet cells, alongside the more common serous cysts, requiring imaging surveillance because larger lesions can metastasise.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Its tumours resist cytotoxics: the renal cancers, haemangioblastomas and neuroendocrine tumours of VHL respond poorly to conventional chemotherapy, so care centres on surgery, ablation and HIF-2α-targeted belzutifan instead.
- `connects-to` → **[GIST](../gist/README.md)** — A shared pseudohypoxia pathway: SDH-deficient GIST, like VHL tumours, stabilises HIF through a pseudohypoxic state — the hypoxia-signalling axis that, via VHL and SDHB defects, unifies VHL pheochromocytomas, paragangliomas and these stromal tumours.
- `connects-to` → **[IDH-mutant Glioma](../idh-mutant-glioma/README.md)** — Two routes to pseudohypoxia: VHL loss directly stabilises HIF, while IDH-mutant glioma's 2-hydroxyglutarate inhibits the dioxygenases that degrade it—convergent HIF-driven, pseudohypoxic oncogenesis from different lesions.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It is a disease of runaway vessels: unrestrained HIF/VEGF in VHL drives the florid capillary proliferation of CNS and retinal hemangioblastomas and the hypervascularity of its renal cancers, vessel growth gone unchecked.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Congenital versus acquired polycythaemia: VHL and its pathway partners (EPAS1, EGLN1) cause hereditary HIF-driven erythrocytosis, the inherited mirror of the acquired, JAK2-driven erythrocytosis of myeloproliferative neoplasms.
- `connects-to` → **[Diabetic Retinopathy](../diabetic-retinopathy/README.md)** — Two VEGF-driven retinal diseases: VHL retinal haemangioblastomas, like diabetic retinopathy, leak and proliferate under HIF-driven VEGF and are managed with laser photocoagulation and anti-VEGF therapy.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — Vascularity, opposite fates: VHL haemangioblastomas and glioblastoma are both intensely VEGF-driven, microvascular-rich CNS tumours, but the haemangioblastoma is benign and curable by resection while glioblastoma is relentlessly malignant.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Shared phaeochromocytoma risk: VHL and neurofibromatosis type 1 both predispose to phaeochromocytoma, two of the hereditary syndromes—with MEN2 and SDHx—behind catecholamine-secreting adrenal tumours.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Hemangioblastomas on the nerve roots: VHL's vascular tumours stud not only the cerebellum and retina but the spinal cord and its nerve roots, compressing them to cause pain and neurological deficits.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Metastatic renal cancer in bone: the clear-cell renal carcinomas of VHL metastasise to the skeleton, producing the highly vascular, osteolytic cortical-bone lesions typical of renal cell carcinoma.
- `connects-to` → **[MEN4 Syndrome](../men4-syndrome/README.md)** — Hereditary endocrine-tumour syndromes: like MEN1 and MEN4, VHL predisposes to pancreatic neuroendocrine tumours, one of several germline syndromes demanding lifelong surveillance of multiple endocrine organs.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — HIF-MYC interplay: stabilised HIF cooperates with MYC activity to drive the proliferation and metabolism of the clear-cell renal carcinomas of VHL disease.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Chromatin dysregulation: EZH2/polycomb activity, in the context of PBRM1 and BAP1 loss accompanying VHL inactivation, contributes to clear-cell renal carcinoma.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Hippo activation: deregulated Hippo-YAP signalling contributes to the renal carcinomas and hemangioblastomas of VHL disease, alongside its dominant HIF axis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: HIF-driven cyclin D1 with CDK4/6 propels the clear-cell renal carcinoma cells of VHL disease through the G1 checkpoint.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: TERT reactivation maintains telomeres in the renal carcinomas of VHL disease, sustaining their proliferation.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K activation: PI3K/AKT/mTOR signalling, reinforced in VHL-deficient tumours, drives the growth of clear-cell renal carcinoma and hemangioblastoma.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Loss of VHL stabilizes HIF, which transcriptionally upregulates the CXCR4 receptor for CXCL12, promoting the invasive and metastatic behavior of VHL-associated clear-cell renal carcinoma—tying the founding lesion directly to metastatic potential.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — The pancreatic neuroendocrine tumors of VHL disease express somatostatin receptor 2, enabling DOTATATE PET surveillance of this multifocal tumor syndrome and peptide-receptor radionuclide therapy of progressive pancreatic lesions.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Adrenomedullin is a HIF target strongly expressed in VHL hemangioblastomas, where it contributes to the vascular permeability and peritumoral cyst formation that produce the symptomatic mass effect in the cerebellum and spinal cord.
- `connects-to` → **[FH](../../03-molecular/fh/README.md)** — VHL loss stabilizes HIF directly, whereas fumarate-hydratase loss does so via accumulated fumarate—convergent pseudohypoxic routes that both cause hereditary pheochromocytoma-paraganglioma and renal tumors through the same HIF endpoint.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Angiopoietin-Tie2 signaling, driven downstream of the constitutive HIF activation in VHL, helps build the strikingly vascular hemangioblastomas and clear-cell renal carcinomas that characterize the syndrome.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — VHL adrenal pheochromocytomas secrete predominantly norepinephrine because they lack PNMT, a biochemical phenotype distinct from the epinephrine-producing RET/MEN2 tumors, useful in directing genetic testing.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — VHL loss stabilizes HIF, which induces TGF-α to drive an autocrine EGFR loop that sustains proliferation of VHL-deficient renal carcinoma and hemangioblastoma.
- `connects-to` → **[BAP1](../../03-molecular/bap1/README.md)** — BAP1, like VHL on chromosome 3p, is a renal tumor-suppressor, and its loss cooperates with VHL inactivation to drive the aggressive, high-grade clear-cell renal carcinoma of the disease.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling activated downstream of HIF in VHL-deficient hemangioblastomas and clear-cell renal carcinoma promotes their vascular, stem-like phenotype.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — HIF-driven cyclin-D1 (mapped) and CDK4/6 release E2F1 to push the proliferation of VHL-deficient tumors such as clear-cell renal carcinoma.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN limits the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped) that cooperates with HIF activation in the growth of VHL-associated tumors.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MET, EGFR and PDGFR (all mapped) signal through the MAPK-ERK cascade in VHL-deficient tumors, complementing the pseudohypoxic HIF program.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — Oncometabolite-producing IDH mutations parallel the FH and SDHB lesions (both already mapped) within the metabolically-driven hereditary renal tumors related to the VHL-HIF pseudohypoxia axis.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (cyclin-D1, CDK4/6 and E2F1 already mapped) contributes to the proliferation of the renal and CNS tumors of von Hippel-Lindau disease.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) contributes to the survival and angiogenic signaling of VHL-associated tumors.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of VHL-associated clear-cell renal carcinoma, relevant to its immunotherapy responsiveness.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling governs the antitumor immune response and immune-evasion balance of the highly vascular, immunogenic VHL-associated renal carcinoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports angiogenesis and immune evasion in the HIF-driven, hypervascular tumors of von Hippel-Lindau disease.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-mediated FOXO inactivation removes a pro-apoptotic brake, supporting survival of VHL-deficient clear-cell renal carcinoma cells (PI3K-AKT already mapped).
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling drives EMT and stromal remodeling in the progression of VHL-associated clear-cell renal carcinoma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunogenic VHL-associated renal carcinoma must evade.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt/β-catenin signaling of the pseudohypoxic VHL-deficient tumors.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation restrains apoptosis in the VHL-associated tumors.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of VHL-associated tumors.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of MET and other receptors (MET already mapped) contributes to the invasion of the tumors of von Hippel-Lindau disease.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the tumors of von Hippel-Lindau disease.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival of the VHL-deficient, pseudohypoxic cells of von Hippel-Lindau disease.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the pseudohypoxic metabolic reprogramming of the tumors of von Hippel-Lindau disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of von Hippel-Lindau disease.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of von Hippel-Lindau disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of the tumors of von Hippel-Lindau disease.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of von Hippel-Lindau disease.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of von Hippel-Lindau disease.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — RCC immunotherapy: the clear cell renal cell carcinomas that dominate VHL disease are immunogenic, historically responsive to high-dose IL-2 and now to checkpoint inhibitors, an immune-targetable dimension complementing the HIF-directed belzutifan.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Chromaffin secretion: the phaeochromocytomas of VHL disease release catecholamines by calcium-triggered granule exocytosis, tying the syndrome's adrenal tumours to the same secretory physiology as sporadic phaeochromocytoma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron and erythrocytosis: HIF stabilisation in VHL disease drives erythropoietin (already mapped) and reshapes iron handling, with transferrin-delivered iron supplying the erythrocytosis and the intensely vascular hemangioblastomas.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — RCC immunotherapy: the clear-cell renal cell carcinoma of VHL disease is among the most immunotherapy-responsive cancers, and MHC class II antigen presentation shapes the T-cell response to the checkpoint inhibitors used in its metastatic form.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint blockade: PD-1 inhibitors, alone or with antiangiogenics targeting the HIF-driven VEGF (already mapped), are standard for advanced VHL-associated clear-cell renal cell carcinoma, exploiting its immunogenicity.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Combination immunotherapy: CTLA-4 blockade combined with PD-1 inhibition (already mapped) is a frontline option for the metastatic clear-cell renal cell carcinoma that develops in VHL disease, deepening responses in this immunoresponsive tumour.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Haemangioblastoma vasculature: nitric oxide with the strongly HIF-driven VEGF and angiopoietin (already mapped) shapes the rich vasculature of the haemangioblastomas that characterise VHL disease, part of their angiogenic biology.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), part of the immune evasion of the VHL-associated clear-cell renal cell carcinoma that checkpoint blockade targets.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Erythropoietin and iron: the stabilised HIF of VHL disease drives erythropoietin (already mapped) and polycythaemia, raising the demand for iron, and paraneoplastic erythropoietin from haemangioblastomas can worsen the erythrocytosis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the VHL-associated clear-cell renal cell carcinoma, part of its immune microenvironment.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Clear-cell lipid: the VHL-driven clear-cell renal cell carcinoma accumulates cholesterol esters and lipid, giving the clear cytoplasm that names it, part of the metabolic rewiring downstream of the constitutive HIF (already mapped).
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Obesity and adipokines: obesity is a risk factor for renal cell carcinoma, and the fall in the adipokine adiponectin is part of the metabolic milieu that can promote the clear-cell renal cell carcinoma of VHL disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immune microenvironment of the VHL-associated tumours, including the clear-cell renal cell carcinoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and RCC risk: the adipokine leptin, with the fall in adiponectin (already mapped), links the obesity that raises renal-cell-carcinoma risk to the metabolic milieu promoting the clear-cell RCC of VHL disease.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the pro-inflammatory adipokine milieu of the obesity implicated in the renal-cell-carcinoma risk of VHL disease.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — EPO-hepcidin axis: the erythropoietin (already mapped)-driven erythroferrone suppresses the hepcidin to mobilise the iron (already mapped) for the polycythaemia of the HIF-activated (already mapped) VHL disease.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — RCC immunogenicity: type-I interferon, downstream of the cGAS-STING (already mapped) innate sensing, shapes the immunogenicity and the checkpoint (PD-1 already mapped) response of the clear-cell renal cell carcinoma of VHL disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the M2 (IL-4 and IL-13 already mapped) tumour-associated macrophages of the immunosuppressive microenvironment of the clear-cell renal cell carcinoma of VHL disease.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity of the immunogenic clear-cell renal cell carcinoma of VHL disease.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the renal-cell-carcinoma immune microenvironment of VHL disease.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the immune microenvironment of the VHL-associated tumours.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4/IL-5 and IL-17 already mapped) cytokines shaping the immune microenvironment of the VHL-associated tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the VHL-associated tumours.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the VHL-associated tumours.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts the checkpoint (PD-1 already mapped) response of the VHL-associated clear-cell renal cell carcinoma (already mapped).
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a contribute to the inflammatory and immunosuppressive dimension of the highly vascular VHL-associated tumour microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling recruits and polarises the myeloid cells to an immunosuppressive phenotype in the VHL-associated tumour microenvironment.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Central complement: the complement C3, upstream of the C5 and C5aR1 (already mapped), is the pivot of the complement activation within the highly vascular VHL-associated tumour microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the VHL-associated tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), evading the complement attack within the tumour microenvironment.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways within the VHL-associated tumour microenvironment, complementing the alternative-pathway control by factor H (already mapped).
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Tumour stromal alarmin: TSLP, released from the VHL-associated tumour stroma (fibroblast, VEGF already mapped), activates mast cells (already mapped) and dendritic cells (already mapped), sustaining the type-2 immunosuppressive microenvironment of the haemangioblastomas and ccRCC lesions.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — HIF-driven kinin axis: bradykinin production is enhanced by the HIF-1α (already mapped) driven upregulation of tissue kallikrein in VHL-disease tumours, amplifying the vascular permeability and angiogenesis (VEGF, angiopoietin already mapped) of the haemangioblastomas.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Hypoxic ECM remodelling: periostin expression is upregulated by HIF-1α (already mapped) in the VHL-associated tumour stroma, contributing to the desmoplastic ECM and invasion of the clear-cell RCC and pNET lesions of VHL disease.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell vascular niche: histamine released by mast cells (already mapped) in the haemangioblastoma and ccRCC microenvironment of VHL disease amplifies local vascular permeability and the VEGF-driven (already mapped) neo-angiogenesis of the tumour stroma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian antioxidant in hypoxia: melatonin reduces the oxidative stress generated by the HIF-1α (already mapped) driven hypermetabolic state of VHL-disease tumours; melatonin receptor signalling may modulate haemangioblastoma growth.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Hypoxic prolactin axis: HIF-1α (already mapped) upregulates prolactin secretion; elevated prolactin in VHL-associated polycythaemia and tumour states stimulates haematopoiesis and may modulate the immune microenvironment of ccRCC lesions.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — VHL testosterone: androgen receptor (AR) signalling promotes the growth of VHL-associated clear cell renal cell carcinoma (kidney already mapped); testosterone-driven AR activity upregulates HIF-1α (already mapped) target genes and the VEGF (already mapped) angiogenic axis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — VHL serotonin: serotonin-secreting pNETs (pancreatic neuroendocrine tumours) are a manifestation of VHL disease; 5-HT receptor signalling on ccRCC cells (kidney already mapped) promotes tumour proliferation and modulates HIF-1α (already mapped) driven therapeutic resistance.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — VHL oxytocin: oxytocin receptor expression on VHL-associated clear cell renal carcinoma (kidney already mapped) and haemangioblastoma cells may modulate tumour angiogenesis via VEGF (already mapped) suppression and immune microenvironment remodelling in VHL-disease.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — VHL vasopressin: vasopressin modulates renal tubular water reabsorption via aquaporin-2 (kidney already mapped); in VHL disease, AVP V2 receptor signalling intersects HIF-1α (already mapped) and VEGF (already mapped) axes in ccRCC and pNET-associated ectopic hormone secretion.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — VHL selenium: selenium-dependent GPX4 protects VHL-deficient ccRCC cells from ferroptosis; GPX4 upregulation is a resistance mechanism downstream of the HIF-1α (already mapped)-VEGF (already mapped) axis in VHL tumours, and selenium status modulates tumour oxidative stress.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — VHL iodine: iodine-dependent thyroid hormones modulate VEGF (already mapped) and HIF-1α (already mapped) pathway activity in VHL-associated ccRCC and haemangioblastoma; hypothyroidism may alter the angiogenic milieu and metabolic rate of VHL tumour cells.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — VHL sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplify HIF-1α (already mapped) and VEGF (already mapped) and mTOR (already mapped) angiogenic cascade of VHL disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — VHL magnesium: magnesium, as mTOR (already mapped) cofactor in endothelial-cell (already mapped) and macrophages (already mapped), supports angiogenesis; magnesium deficiency amplifies HIF-1α (already mapped) and VEGF (already mapped) and NF-κB (already mapped) cascade of VHL.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — VHL copper: copper, as lysyl oxidase cofactor in endothelial-cell (already mapped), drives VEGF (already mapped) angiogenesis in VHL tumours; copper deficiency impairs macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour immunity in VHL disease.

[^lonser-2003-vhl-disease]: Lonser RR, Glenn GM, Walther M, et al. von Hippel-Lindau disease. *Lancet.* 2003;361(9374):2059-2067. [doi:10.1016/S0140-6736(03)13643-4](https://doi.org/10.1016/S0140-6736(03)13643-4) · [PubMed 12814730](https://pubmed.ncbi.nlm.nih.gov/12814730/)
[^choueiri-2020-hif2-rcc]: Choueiri TK, Kaelin WG Jr. Targeting the HIF2-VEGF axis in renal cell carcinoma. *Nat Med.* 2020;26(10):1519-1530. [doi:10.1038/s41591-020-1093-z](https://doi.org/10.1038/s41591-020-1093-z) · [PubMed 33020650](https://pubmed.ncbi.nlm.nih.gov/33020650/)
