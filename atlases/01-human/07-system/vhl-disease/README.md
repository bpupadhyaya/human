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

[^lonser-2003-vhl-disease]: Lonser RR, Glenn GM, Walther M, et al. von Hippel-Lindau disease. *Lancet.* 2003;361(9374):2059-2067. [doi:10.1016/S0140-6736(03)13643-4](https://doi.org/10.1016/S0140-6736(03)13643-4) · [PubMed 12814730](https://pubmed.ncbi.nlm.nih.gov/12814730/)
[^choueiri-2020-hif2-rcc]: Choueiri TK, Kaelin WG Jr. Targeting the HIF2-VEGF axis in renal cell carcinoma. *Nat Med.* 2020;26(10):1519-1530. [doi:10.1038/s41591-020-1093-z](https://doi.org/10.1038/s41591-020-1093-z) · [PubMed 33020650](https://pubmed.ncbi.nlm.nih.gov/33020650/)
