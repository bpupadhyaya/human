---
schema: human-scale-entry/v1
id: meningioma
name: Meningioma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Meningioma is the most common intracranial tumor; WHO grades 1-3; NF2 LOF ~50-60%, AKT1 E17K ~10-12%, TRAF7 ~25%; grade 1 5-year recurrence: GTR ~7%; grade 2 ~40%; grade 3 ~80%; surgery ± SRS for grade 1-2; RT for grade 3; bevacizumab and mTOR inhibitors for recurrent disease."
aliases: ["meningioma", "intracranial meningioma", "benign meningioma", "atypical meningioma", "anaplastic meningioma", "NF2 meningioma", "skull base meningioma", "convexity meningioma", "spinal meningioma"]
sources:
  - id: brastianos-2013-akt1-meningioma
    type: peer-reviewed
    cite: "Brastianos PK, Horowitz PM, Santagata S, et al. Genomic sequencing of meningiomas identifies oncogenic SMO and AKT1 mutations. Nat Genet. 2013;45(3):285-289."
    doi: "10.1038/ng.2526"
    pmid: "23334667"
    url: "https://doi.org/10.1038/ng.2526"
  - id: nassiri-2021-meningioma-classification
    type: peer-reviewed
    cite: "Nassiri F, Liu J, Patil V, et al. A clinically applicable integrative molecular classification of meningiomas. Nature. 2021;597(7874):119-125."
    doi: "10.1038/s41586-021-03850-3"
    pmid: "34385709"
    url: "https://doi.org/10.1038/s41586-021-03850-3"
cross_links:
  - target: 01-human/03-molecular/nf2
    relation: connects-to
    note: "NF2 biallelic LOF in ~50-60% sporadic meningioma; NF2 loss → Hippo inactivation → YAP/TAZ nuclear → TEAD-driven proliferation; NF2-mutant meningiomas are convexity-predominant; germline NF2 → bilateral VS, meningiomas, ependymomas; TEAD inhibitors in Phase 1 trials."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "AKT1 E17K (~10-12% skull base meningioma, grade 1) directly activates mTORC1/mTORC2; NF2 loss → Hippo off → YAP/TAZ nuclear → upstream mTOR activators; mTOR inhibitors (everolimus/sirolimus) in NF2 syndrome VS (REACT trial, 2012): volumetric reduction of VS in 30-44% of patients."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "AKT1 E17K and NF2 loss both engage EGFR/ErbB signaling in meningioma; NF2-null → ErbB2 surface overexpression → sustained RAS/MAPK; erlotinib and gefitinib explored in recurrent meningioma with modest activity; ErbB2 amplification is rare in meningioma."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss in ~10-15% meningioma; NF2 and PTEN both suppress PI3K/AKT/mTOR → NF2+PTEN co-loss is synergistic; AKT1 E17K (skull base meningioma, ~10-12%) activates PI3K/mTOR without PTEN loss; mTOR inhibitors target the convergent PI3K/mTOR axis in meningioma."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Meningioma is the most common intracranial tumor, arising not from brain but from arachnoid cap cells of the meninges; it compresses brain and cranial nerves, and location (convexity, skull base, parasagittal) dictates resectability and surgical morbidity more than grade."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "Germline NF2 loss (neurofibromatosis type 2) predisposes to multiple meningiomas alongside bilateral vestibular schwannomas and ependymomas; sporadic meningiomas carry biallelic NF2 loss in ~50-60%, making merlin/Hippo inactivation the central driver in both settings."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Grade 1 meningiomas show a 2-3:1 female predominance and express progesterone receptors, with growth during pregnancy and on medroxyprogesterone exposure; yet anti-progesterone mifepristone failed in Phase 3, so PR positivity does not predict hormone-blockade response."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "Meningioma and mesothelioma are unrelated tumors united by one driver: biallelic NF2/merlin loss inactivates Hippo, freeing YAP/TAZ-TEAD to drive proliferation in ~50-60% of meningiomas and ~40% of mesotheliomas — making both lead indications for TEAD inhibitors now in trials."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Meningioma growth runs through YAP: NF2/merlin loss releases YAP/TAZ to partner with TEAD and transcribe proliferative genes; this Hippo-YAP axis, not a classic oncogene, drives most meningiomas, and TEAD-palmitoylation inhibitors are the first targeted therapy in trials."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Meningioma is the most common primary CNS tumor, but it arises from the meninges (arachnoid cap cells), not neural tissue — growing outside the brain and spinal cord and causing symptoms by compression; its dural-based, extra-axial location makes many curable by resection."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Ionizing radiation is the best-established environmental cause of meningioma: prior cranial radiotherapy (even low-dose scalp irradiation) markedly raises risk, often producing higher-grade, multiple tumors decades later—while focused radiosurgery also treats inaccessible ones."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "Meningioma and glioblastoma are the two commonest primary brain tumors but opposite: meningioma is an extra-axial, dural-based, usually benign and resectable tumor of arachnoid cells, while glioblastoma is intra-axial, diffusely infiltrative and malignant—distinguished on MRI."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Meningioma and breast cancer are linked through hormones and co-occurrence: most meningiomas express progesterone (and some estrogen) receptors, grow in pregnancy and the luteal phase, and the two are epidemiologically associated—a breast-cancer history can accompany meningioma."
  - target: 01-human/07-system/chordoma
    relation: connects-to
    note: "Meningioma and chordoma are both slow-growing extra-axial tumors of the skull base and spine: meningioma arises from arachnoid cap cells, chordoma from notochord remnants in the clivus or sacrum—both treated by resection plus radiotherapy and prone to local recurrence."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Meningioma and primary CNS lymphoma can both appear as enhancing masses but differ: meningioma is an extra-axial dural tumor cured by resection, while PCNSL is an intra-axial B-cell lymphoma treated with methotrexate, not surgery—so location and biopsy decide."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Meningioma and IDH-mutant glioma sit in opposite brain compartments: meningioma is extra-axial, dural-based and usually benign, while IDH-mutant glioma is intra-axial and infiltrative—MRI location (the dural tail) distinguishes the resectable from the diffuse."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Meningiomas threaten the brain by compression, not invasion: arising from arachnoid cap cells of the meninges, they grow slowly and push on neurons and cortex, causing seizures and focal deficits—so symptoms come from mass effect, not infiltration of the brain."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "Meningioma sits in the NF2/schwannomatosis tumor family: NF2 (merlin) loss drives sporadic meningiomas and the multiple meningiomas, schwannomas and ependymomas of NF2, so a young patient with several meningiomas should prompt NF2-spectrum genetic testing."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Meningiomas are often hormone-responsive: many express progesterone and estrogen receptors, can enlarge during pregnancy or with hormonal therapy, and are commoner in women—so hormonal status influences their growth and is weighed in management."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy refines radiation for meningioma: many sit at the skull base wrapped around nerves and vessels, so protons' sharp dose stop point delivers high dose to the tumor while sparing the adjacent brain, optic nerves and brainstem."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Some meningiomas are fibroblastic: arising from arachnoid cap cells, these benign tumors can take a spindle-cell, collagen-rich (fibroblastic) form, one of several histologic subtypes that, with grade and location, guide whether surgery alone or added radiation is needed."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF drives the brain swelling around meningiomas: tumor VEGF makes vessels leaky, producing the peritumoral edema that often causes symptoms more than the mass itself, so anti-VEGF bevacizumab is tried for edema and recurrent disease."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Meningiomas light up with somatostatin imaging: they strongly express SSTR2, so 68Ga-DOTATATE PET pinpoints tumor and residual disease better than MRI alone, and somatostatin analogues are tried in tumors that recur after surgery and radiation."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT marks the dangerous meningiomas: TERT promoter mutations reactivate telomerase and now define a higher WHO grade, flagging tumors likely to recur aggressively regardless of how benign they look under the microscope."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Meningiomas can remodel the overlying skull: en plaque tumors signal osteoblasts to thicken adjacent bone (hyperostosis), a radiologic clue to the diagnosis and a reason surgery sometimes must remove involved bone."
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "A subset of meningiomas is driven by Hedgehog through SMO: skull-base tumors often carry SMO mutations rather than NF2 loss, defining a molecular subgroup that—like basal cell carcinoma—might respond to smoothened inhibitors."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion marks the most dangerous meningiomas: losing this tumor-suppressor now defines WHO grade 3 regardless of how the cells look, so molecular testing for CDKN2A reclassifies aggressive tumors that histology alone would underestimate."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Meningiomas are infiltrated mainly by macrophages: these tumor-associated immune cells are the dominant inflammatory population in the tumor and may support its growth, making the meningioma's immune niche a target of interest."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Meningiomas lay down calcium as psammoma bodies: these concentric calcified whorls are a histologic hallmark and make many meningiomas visibly calcified on imaging, a clue that helps distinguish them from other brain tumors."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Some meningiomas are driven by AKT mutations: recurrent AKT1 changes switch on the PI3K-AKT-mTOR growth pathway in non-NF2 tumors, defining a molecular subgroup that AKT and mTOR inhibitors are being tested against."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Meningiomas largely evade cytotoxic T cells: beyond their dominant macrophages, they keep a T-cell-poor, immunosuppressive microenvironment, which is part of why checkpoint immunotherapy has had limited success in the tumor."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Meningiomas can blind through the eye: those arising on the optic nerve sheath or near the orbit compress the nerve and push the eye forward (proptosis), causing slow, painless vision loss."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Meningiomas calcify with calcium phosphate: their hallmark psammoma bodies are concentric whorls of calcium-phosphate mineral, a histologic signature also visible as flecks of calcification on imaging."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Meningiomas are vascular tumors fed by endothelial cells: they recruit a rich blood supply, giving the bright contrast enhancement and 'dural tail' seen on MRI, and making them prone to bleed during surgery."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy fingerprints meningiomas: their meningothelial cells interlock through elaborate interdigitating processes joined by desmosomes — an ultrastructural signature that confirms the diagnosis when light microscopy is ambiguous."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Meningiomas run on a PDGF autocrine loop: the tumor cells make platelet-derived growth factor and carry its receptor, driving their own proliferation — a pathway studied as a target for the aggressive grades that resist surgery and radiation."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "When a meningioma defies expectation and metastasizes, the lung is its commonest destination: though nearly all are benign and stay local, malignant variants spread hematogenously, with pulmonary deposits the classic distant site."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Meningiomas can thicken the skull they sit against: en plaque tumors provoke reactive hyperostosis of the overlying bone, and some arise within the marrow-bearing skull itself as intraosseous meningiomas."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Rarely a meningioma breaks through to the scalp: extracranial extension or a primary cutaneous meningioma forms a firm scalp nodule, the tumor reaching the skin from the meninges beneath the skull."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "If a malignant meningioma spreads, the liver is among its targets: after the lungs, hematogenous metastases can lodge in the liver and bone, the unusual distant spread of an aggressive grade."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies grade and target the tumor: EMA, SSTR2, and progesterone-receptor stains confirm a meningioma and a high Ki-67 antibody index flags the aggressive grades, while the SSTR2 it displays makes it visible on DOTATATE imaging and a peptide-therapy target."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Though it grows outside the brain, a meningioma still irritates it: the slow dural mass compresses cortex and provokes peritumoral edema and reactive astrocyte gliosis in the underlying brain, the swelling that causes seizures and focal deficits."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy can wake a meningioma: many carry progesterone receptors and visibly enlarge under the hormone surge that the placenta drives, sometimes turning symptomatic in the third trimester and shrinking again after delivery."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hormones explain meningioma's female slant: it is far commoner in women, and long-term high-dose progestins like cyproterone acetate are now a recognized, dose-dependent cause — an iatrogenic link that has reshaped how these drugs are prescribed."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Few cancers clot like a brain tumor patient: meningioma carries a high risk of deep-vein thrombosis and pulmonary embolism from the tumor's procoagulant tissue factor, the immobility around craniotomy, and steroid use, demanding careful prophylaxis."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets feed the meningioma's clotting tendency: the tumor's tissue factor activates them into the hypercoagulable state behind its thrombosis risk, and they also help build the rich vasculature that makes these tumors bleed at surgery."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Meningiomas split into molecular flavors: alongside NF2 loss, a subset is driven by activating PIK3CA mutations that fire the PI3K-AKT growth pathway, marking tumors that may respond to PI3K-pathway inhibitors rather than NF2-targeted approaches."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Sitting on the cortex, they spark seizures: convexity meningiomas irritate and compress the brain surface, so epilepsy is a common presenting sign and often persists, requiring anticonvulsants even after the tumor is removed."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Higher-grade meningiomas wall themselves off immunologically: their microenvironment fills with regulatory T cells and exhausted infiltrate that suppress attack, a feature that worsens with grade and is studied as a target for immunotherapy in aggressive tumors."
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "Chromatin-remodeling genes drive familial meningiomas: germline SMARCB1 and SMARCE1 (SWI-SNF) mutations cause multiple and clear-cell/spinal meningiomas, a distinct genetic route apart from the common NF2-loss tumors."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "Hedgehog-pathway syndromes seed them too: a subset of meningiomas is driven by SMO/SHH activation, the same pathway deranged in Gorlin syndrome, linking these dural tumors to hedgehog-pathway predisposition."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "A meningioma can choke the brain's drainage: parasagittal tumors invade the dural venous sinuses, and the resulting venous obstruction (or peritumoral edema) can precipitate venous infarction and stroke-like deficits."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Merlin loss activates STAT3: NF2/merlin-deficient meningiomas show STAT3 signaling that supports their growth, paralleling the schwannoma biology of the same tumor-suppressor loss."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Merlin normally restrains NF-κB: its loss in meningioma lifts that brake, engaging NF-κB-driven survival and inflammatory signaling among the pathways downstream of NF2 inactivation."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Craniotomy carries infectious risk: the surgery used to resect meningiomas can be complicated by wound infection or meningitis, which in the postoperative patient can progress to sepsis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Its location and surveillance weigh on the mind: frontal meningiomas can directly alter mood and personality, and the anxiety of watchful waiting over a brain tumor contributes to depression."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Steroids for brain swelling thin the bones: the corticosteroids used to control peritumoral edema around meningiomas, especially with prolonged or repeated courses, accelerate bone loss and fracture risk."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Aggressive disease and its treatment blunt the marrow: atypical and anaplastic meningiomas that recur and require radiation or chemotherapy carry an inflammatory burden that can produce an anemia of chronic disease."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Skull-base tumors compress cranial nerves: meningiomas near the cavernous sinus or skull base entrap the trigeminal and other cranial nerves, producing facial and neuropathic pain."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Its steroids raise blood sugar: the dexamethasone used to control peritumoral edema around a meningioma induces insulin resistance and can precipitate steroid-induced diabetes."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Craniotomy and steroids hinder repair: the surgery to resect a meningioma, often with chronic dexamethasone, leaves scalp and dural wounds prone to CSF leak and slow healing."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is hormone-sensitive and presses on the pituitary: meningiomas express progesterone receptors and can grow in pregnancy, and skull-base tumours compress the pituitary and hypothalamus."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It reshapes the skull bone: meningiomas characteristically provoke hyperostosis of the overlying calvarium and can invade and remodel the cranial bones, a recognised radiological hallmark."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An incidental brain tumour under watch breeds worry: the surveillance of a slow-growing meningioma, fear of growth or recurrence and neurological symptoms foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Scalp radiation seeds it and it can reach the scalp: meningiomas are a recognised late effect of childhood cranial radiation, and large convexity tumours can erode the skull toward the scalp."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Skull-base tumours press on the breathing centres: posterior-fossa and skull-base meningiomas can compress the brainstem, impairing the control of breathing and swallowing."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "These vascular tumours engage the circulation: meningiomas are often embolised before surgery to reduce bleeding, and parasagittal tumours can invade and occlude the dural venous sinuses."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It carries an immune microenvironment: high-grade meningiomas harbour tumour-infiltrating immune cells, and checkpoint immunotherapy is under trial for aggressive, treatment-resistant disease."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It expresses somatostatin receptors: refractory meningiomas are treated in trials with somatostatin-analogue and SSTR-targeted radionuclide (DOTATATE) therapy, alongside anti-VEGF agents."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It can rarely spread to the liver: although usually benign, malignant grade-3 meningioma can metastasise outside the skull, including to the liver and lungs."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It thickens the overlying skull: meningiomas characteristically provoke reactive hyperostosis of the adjacent skull bone, a radiological clue, and can invade bone directly."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo barely helps: meningioma is largely chemoresistant, so surgery and radiation dominate, with somatostatin analogues and hydroxyurea giving only modest benefit in refractory disease."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Trials in the aggressive grades: low-grade meningiomas are immunologically quiet, but PD-1 checkpoint inhibitors are being trialled for the rarer high-grade and recurrent meningiomas."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "A shared SWI/SNF lesion: rhabdoid meningiomas and atypical teratoid/rhabdoid tumours both lose SMARCB1, a subunit of the SWI/SNF chromatin-remodelling complex, so the same epigenetic machinery failure produces an aggressive meningioma and a malignant childhood CNS tumour."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "A late price of curing leukaemia: cranial irradiation for childhood acute lymphoblastic leukaemia is a leading cause of radiation-induced meningiomas, which emerge as second tumours decades later—so survivors need long-term neuro-imaging surveillance."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "It shares a theranostic target with carcinoids: meningiomas strongly express somatostatin receptor 2, so like neuroendocrine tumours they light up on DOTATATE PET and can be treated with peptide receptor radionuclide therapy."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Radiation-induced meningioma: childhood cranial radiotherapy—for medulloblastoma or leukaemia—is a leading cause of secondary meningiomas arising decades after treatment."
  - target: 01-human/07-system/men4-syndrome
    relation: connects-to
    note: "An endocrine-syndrome association: MEN4 (CDKN1B loss) raises the risk of meningiomas alongside its parathyroid and pituitary tumours, one of the germline syndromes that predispose to them."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Compression of the neural axis: as it grows from the dura, a meningioma compresses the brain, cranial nerves and their axons, and the resulting axonal dysfunction produces its focal deficits and seizures."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Radiation-induced and predisposed: meningioma is the commonest radiation-induced brain tumour, and Li-Fraumeni patients given radiotherapy face a high rate of them—one reason radiation is avoided in the syndrome wherever possible."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "The malignant mimic: lung and breast cancers commonly seed dura-based metastases that radiologically imitate a meningioma, the key malignant differential of a dural mass in a patient with known cancer."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "A vascular tumour: meningiomas parasitise dural arterial feeders such as the middle meningeal artery, vessels often embolised before surgery to shrink the tumour and reduce intraoperative bleeding."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle target: CDKN2A loss in high-grade meningioma unleashes CDK4/6-driven proliferation, making CDK4/6 inhibition a candidate strategy for aggressive tumours."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic progression: EZH2 and polycomb activity contribute to the malignant progression of higher-grade meningiomas, an emerging epigenetic vulnerability."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Developmental signalling: dysregulated Notch signalling participates in meningioma tumorigenesis, interacting with the NF2-Hippo axis that defines many of these tumours."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: with CDKN2A loss marking higher-grade tumours, cyclin D1-CDK4/6 activity pushes meningioma cells through the G1 checkpoint."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative oncogene: MYC activation drives the proliferation of atypical and anaplastic meningiomas, contributing to their aggressive, recurrent behaviour."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the highly vascular meningioma drives the VEGF angiogenesis that supplies these dural-based tumours and the peritumoural oedema they cause."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK-pathway meningiomas: RAF-MEK-ERK signalling downstream of TRAF7/KLF4 and AKT1 mutations drives the proliferation of a major non-NF2 molecular subgroup of meningiomas."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-factor signalling: IGF-1/IGF-1R signalling supports meningioma proliferation and survival, contributing to the growth of these slow but recurrence-prone dural tumours."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into meningiomas, which make up a substantial fraction of the tumour mass and shape its growth."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Invasion and recurrence: CXCR4-CXCL12 signalling promotes the brain and bone invasion of higher-grade meningiomas, the infiltrative growth that drives the recurrences which dominate meningioma morbidity."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Hyperostosis: meningiomas invading the adjacent skull stimulate RANKL-driven bone remodelling, producing the reactive bony thickening (hyperostosis) that is a characteristic radiological sign of the tumour."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Radiation response: stereotactic radiosurgery and radiotherapy for residual or high-grade meningiomas kill tumour cells through caspase-3-mediated apoptosis, whose evasion contributes to the recurrence of aggressive tumours."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "Merlin-pathway signalling: the NF2/merlin loss that drives most meningiomas disinhibits Src/FAK at the membrane, since merlin normally restrains them — the loss of contact inhibition that lets the meningothelial cells proliferate."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Methylation grading: DNA-methylation profiling stratifies meningiomas into prognostic classes that predict recurrence better than histological grade alone, making the methylome an increasingly central tool in their classification and management."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Psammoma bodies: many meningiomas form psammoma bodies — concentric, calcified laminated structures — a characteristic histological hallmark, and the tumour's calcification can be visible on imaging."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Grade progression: the CDK4/6-cyclin-D1 axis (mapped, with CDKN2A loss marking higher grade) releases E2F1 to drive the accelerated proliferation of atypical and anaplastic meningioma."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Anaplastic transformation: TP53 inactivation accompanies the progression of meningioma to the anaplastic grade-3 tumour, removing an apoptotic and cell-cycle brake on the malignant clone."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Stromal phenotype: TGF-β signalling shapes the fibroblastic and transitional phenotypes of meningioma and the collagenous stroma of these dura-derived tumours."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Grade progression: deregulation of the RB1-E2F checkpoint (E2F1, CDK4/6, CDKN2A and cyclin-D1 already mapped) marks the progression of meningioma toward higher WHO grade."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Proliferative MAPK: RAS-MAPK signalling (ERK1/2 already mapped) contributes a proliferative input to meningioma growth."
  - target: 01-human/03-molecular/sufu
    relation: connects-to
    note: "Hedgehog subgroup: SUFU is a negative regulator of the Sonic-Hedgehog pathway (SMO already mapped), the pathway recurrently activated in the non-NF2 molecular subgroup of skull-base meningiomas."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 expression marks higher-grade meningiomas and modulates their invasive and immune behaviour."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) modulates the proliferation and stromal interactions of meningioma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT3 signalling (STAT3 mapped) provides a proliferative input contributing to meningioma growth."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune microenvironment of meningioma, relevant to immunotherapy in aggressive higher-grade tumours."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory microenvironment and radiation response of meningioma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by the AKT signalling activated by NF2/merlin loss, modulate the survival of meningioma cells."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and Hedgehog signaling co-opted in the tumorigenesis of meningioma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the progression toward higher-grade meningioma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of meningioma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is relevant to the immune response against meningioma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the NF2/merlin-deficient cells of meningioma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A and the SWI/SNF machinery (SMARCB1 already mapped) contribute to the epigenetic dysregulation of meningioma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of meningioma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of meningioma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of meningioma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of meningioma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of meningioma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of meningioma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the tumor microenvironment of meningioma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of meningioma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the tumor microenvironment and progression of meningioma."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Hormone-receptor expression: meningiomas express progesterone (already mapped) and androgen receptors, and their tendency to grow during pregnancy and in women reflects the hormone responsiveness of these tumours."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy: MHC class II antigen presentation shapes the T-cell response to meningioma, of growing interest for the higher-grade and recurrent tumours that resist surgery and radiation and are being explored for checkpoint therapy."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: IL-2-driven T-cell expansion supports the immunotherapy approaches under investigation for aggressive grade 2-3 meningiomas, which have a more immunosuppressive microenvironment than benign lesions."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the microenvironment of higher-grade meningiomas dampens the anti-tumour T-cell response (IL-2 and MHC class II already mapped), part of the immune evasion that motivates the checkpoint strategies explored for aggressive tumours."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of meningiomas, part of the stromal biology supporting these often highly vascular extra-axial tumours."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Fibrous stroma: the fibroblastic and transitional meningioma variants (fibroblast already mapped) lay down a collagen-rich stroma with psammoma bodies, the dense connective tissue that gives these tumours their firm texture."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the meningioma stroma, part of the immune microenvironment of these often indolent tumours."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Peritumoral inflammation: prostaglandins from the tumour and infiltrating cells (IL-6 and IL-1 already mapped) contribute to the peritumoral brain oedema and inflammation that shape the symptoms of meningiomas."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative microenvironment: the meningioma generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species are part of the tumour microenvironment beyond the growth-factor (already mapped) drivers."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immune microenvironment of meningioma."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the macrophages (CCL2 already mapped) form a large part of the immune infiltrate of meningioma, and their M2 polarisation (IL-4 already mapped) shapes the tumour microenvironment."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibrous meningioma: the fibroblastic (fibrous) meningioma is a WHO grade-1 variant of spindled, fibroblast-like cells in a collagen-rich (already mapped) matrix, one of the histological subtypes of the tumour."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity-risk adipokine: leptin links the obesity risk factor to meningioma, alongside the hormone-responsive (progesterone and estrogen already mapped) biology of the tumour."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity-related meningioma risk."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity-related meningioma risk."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the emerging immunotherapy of meningioma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of meningioma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the meningioma immune microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of meningioma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the meningioma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the meningioma microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Peritumoural oedema: the mast cells of the meningioma stroma are associated with the peritumoural brain (already mapped) oedema and contribute to the angiogenesis (VEGF already mapped) and type-2 microenvironment."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate cytotoxicity: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance within the immune microenvironment of meningioma."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the tumour antigen to the T cells (already mapped) shaping the adaptive immune response against meningioma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of meningioma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of meningioma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the macrophage-rich (already mapped) meningioma stroma."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Peritumoral oedema: bradykinin (B2 receptor) increases blood–brain barrier permeability in the peritumoral zone, driving the cerebral oedema that is a major cause of neurological symptoms in meningioma; bradykinin blockade reduces the vasogenic oedema around meningioma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell stroma: histamine from the mast cells that are notably abundant in meningioma stroma promotes VEGF (already mapped) angiogenesis and matrix-remodelling; mast-cell-derived histamine contributes to the peritumoral oedema and dural invasiveness of meningioma."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Invasive meningeal stroma: periostin secreted by the meningioma-associated fibroblasts and TGF-β (already mapped) signalling promotes the dural adhesion and invasiveness of meningioma; elevated periostin in skull-base meningioma correlates with the WHO grade and recurrence risk."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Meningeal alarmin: TSLP released by the meningioma-associated stromal cells activates dendritic cells and mast cells in the tumour microenvironment, amplifying the TGF-β (already mapped) and VEGF (already mapped) driven peritumoral inflammation and angiogenesis of meningioma."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: C1-INH controls the classical-pathway arm (C3, C5 and C5aR1 already mapped) in the meningioma microenvironment, modulating complement-mediated tumour-cell lysis and the tumour-associated macrophage (already mapped) inflammatory response."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Meningeal EPO signalling: erythropoietin receptor (EPOR) on meningioma cells activates the JAK2/STAT3 (already mapped) pathway, upregulates VEGF-driven (already mapped) angiogenesis and promotes the hypervascular phenotype of WHO grade II-III meningioma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Meningeal oncostasis: melatonin, via MT1/MT2 receptors on meningioma cells and the dural tumour vasculature (already mapped), suppresses VEGF-driven (already mapped) angiogenesis and NF-κB (already mapped) signalling, reducing the peritumoral oedema burden of meningioma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-meningioma axis: testosterone, via androgen receptor on meningioma cells, modulates VEGF-driven (already mapped) and AKT1 (already mapped) proliferative signalling and contributes to the sex-dimorphic incidence and hormone-receptor positivity of meningioma."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Meningeal 5-HT signalling: serotonin from mast cells (already mapped) in meningioma stroma signals via 5-HT2 receptors on meningioma cells and endothelial cells (already mapped), amplifying the VEGF (already mapped) angiogenic and peritumoral oedema cascade."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Meningioma prolactin receptor: prolactin, via PRL-R on meningioma cells and macrophages (already mapped), upregulates NF-κB (already mapped) and IL-6 (already mapped) pro-survival signalling and promotes VEGF-driven (already mapped) angiogenesis in meningioma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Meningioma oxytocin anti-tumour: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling in the peritumoral meningeal microenvironment of meningioma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Meningioma vasopressin vascular: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates dural tumour vascular tone; dysregulation amplifies NF-κB (already mapped) and VEGF (already mapped) angiogenic signalling in meningioma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Meningioma selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the meningioma TME; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory tumour cascade of meningioma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Meningioma iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of meningioma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Meningioma sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of meningioma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Meningioma magnesium: magnesium, as cofactor of antioxidant enzymes in macrophages (already mapped) and fibroblasts (already mapped), supports matrix homeostasis; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of meningioma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Meningioma copper: copper, as cofactor of SOD1 in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges TME ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of meningioma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Meningioma zinc: zinc, as cofactor of metalloproteinases in macrophages (already mapped) and fibroblasts (already mapped), modulates matrix remodelling; zinc depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of meningioma."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Meningioma carbon: carbon as backbone of NF2 (already mapped) and merlin structural proteins in meningeal cells (already mapped) sustains tumour suppression; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) meningioma cascade."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Meningioma chloride: chloride regulates meningeal cells (already mapped) and macrophage (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) protumorigenic cascade of meningioma."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Meningioma nitrogen: nitrogen in amino-acid scaffold of NF2 (already mapped) and TRAF7 proteins sustains meningeal cell (already mapped) proliferation control; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of meningioma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Meningioma hydrogen: hydrogen in meningeal cells (already mapped) and macrophages (already mapped) modulates NF2 (already mapped) protein stability; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of meningioma."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Meningioma iron: iron supports haem metabolism in meningeal cells (already mapped) and macrophages (already mapped) for tumour proliferation; iron dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) oncogenic cascade of meningioma."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Meningioma oxygen: oxygen supports aerobic metabolism in meningeal cells (already mapped) and macrophages (already mapped); oxygen deficit amplifies HIF and NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) angiogenic cascade of meningioma."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Meningioma pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates meningeal immune evasion; pd-1 dysregulation amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Meningioma glp-1: GLP-1 from macrophages (already mapped) and fibroblasts (already mapped) modulates metabolic-inflammatory tone; glp-1 dysfunction amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) meningeal tumour cascade of meningioma."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Meningioma angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and macrophages (already mapped) drives vascular remodelling; angiotensin-ii excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Meningioma wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and fibroblasts (already mapped) regulates meningeal fate; wnt-beta-catenin dysregulation amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Meningioma fibronectin: fibronectin in macrophages (already mapped) and fibroblasts (already mapped) promotes meningeal ECM remodelling; fibronectin excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Meningioma activin-a: activin-A from macrophages (already mapped) and fibroblasts (already mapped) drives meningeal fibrosis; activin-a excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Meningioma tgf-beta: TGF-β from macrophages (already mapped) and fibroblasts (already mapped) modulates meningeal fibrotic resolution; TGF-β excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Meningioma cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates meningeal neuroimmune tone; cgrp excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Meningioma calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates meningeal calcium balance; calcitonin excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma."
---

# Meningioma

## Overview

**Meningioma** is the most common primary intracranial tumor in adults, accounting for ~37-40% of all primary brain tumors. Approximately 40,000 new cases are diagnosed per year in the USA. Meningiomas arise from **arachnoidal cap cells** (meningothelial cells of the arachnoid layer) and are most commonly benign (WHO grade 1); however, grade 2 (atypical) and grade 3 (anaplastic) variants carry significant morbidity and mortality. The female-to-male ratio is ~2-3:1 for grade 1 (suggesting hormonal influence via progesterone receptor expression), equalizing at grade 2 and reversing at grade 3 (~1.5:1 M:F for grade 3).

**Epidemiology and risk factors:**
- **Radiation**: prior cranial or head/neck radiation → radiation-induced meningioma at latency 10-35 years; higher incidence of grade 2-3; multiple synchronous lesions
- **NF2 syndrome** (germline NF2 mutation): ~50% develop multiple meningiomas; usually grade 1-2; often skull base and spinal; bilateral vestibular schwannomas are the hallmark
- **Schwannomatosis** (SMARCB1 or LZTR1 germline): rare meningiomas
- **Female hormonal factors**: breast cancer and meningioma co-occurrence (shared PR/ER signaling); medroxyprogesterone acetate exposure → meningioma growth; postmenopausal HRT association
- **Incidental meningiomas** (~1-2% of adult brain MRIs): overwhelming majority grade 1; active surveillance unless symptomatic or growing

**WHO 2021 histological grades:**
- **Grade 1** (~75-80%): 15 recognized histological subtypes; fibrous, meningothelial, transitional, psammomatous (calcified whorl-forming), angiomatous, microcystic, lymphoplasmacyte-rich, secretory (CEA+ intracytoplasmic lumina), metaplastic; 5-year recurrence GTR ~7%, STR ~25%
- **Grade 2 / Atypical** (~18-22%): mitoses ≥4/10 HPF, OR brain invasion, OR ≥3 of: increased cellularity, small cells with high N:C ratio, prominent nucleoli, sheet-like growth, necrosis (not around blood vessels); 5-year recurrence GTR ~30-40%, STR ~60-70%
- **Grade 3 / Anaplastic** (~1-3%): mitoses ≥20/10 HPF, OR focal dedifferentiation (loss of meningothelial morphology), OR carcinoma/melanoma/high-grade sarcoma histology; 5-year OS ~35-60%
- **WHO 2021 molecular upgrades**: TERT promoter mutation → grade 3 regardless of histology; H3K27me3 loss by IHC (EZH2 mutation) → methylation class-defined aggressive meningioma treated as grade 3

## Structure

### Neuroanatomical locations

**Convexity (~25-30%)**: parasagittal, over cerebral hemispheres; most accessible surgically; >90% NF2-mutant

**Skull base (~30-35%)**: 
- Sphenoid ridge: medial (encasing carotid/MCA), lateral (more resectable)
- Sella/suprasellar: AKT1 E17K, TRAF7 mutations predominant; high PR expression; women >men (~4:1)
- Cerebellopontine angle (CPA): usually NF2-mutant; must distinguish from VS (VS has no arachnoid cap cells on histology)
- Olfactory groove: often large at diagnosis; anosmia (often unnoticed); AKT1 or NF2

**Posterior fossa (~20%)**: petroclival (POLR2A mutations), cerebellar convexity (NF2-mutant)

**Spinal (~5-10%)**: thoracic > cervical; women >> men; fibrous/psammomatous; NF2-mutant; usually grade 1; complete resection curative in ~90%

**Intraventricular (~2%)**: trigone of lateral ventricle; often large, difficult resection; NF2-mutant

### WHO 2021 Molecular classification

DNA methylation profiling (Nassiri 2021) [^nassiri-2021-meningioma-classification] defines **6 methylation classes** that predict recurrence risk better than histologic grade alone:

| Methylation class | Molecular features | 12-year PFS | Key histology |
|---|---|---|---|
| Merlin-intact | NF2 intact; TRAF7/AKT1/KLF4/SMO | ~95% | Meningothelial/transitional/secretory |
| Immune-enriched | Lymphocyte-rich TME; NF2 varied | ~90% | Lymphoplasmacyte-rich |
| Hypermetabolic | High metabolic activity | ~80% | Varied |
| Merlin-lost | NF2 LOF, 22q loss | ~55% | Fibrous/transitional/grade 2 |
| CDKN2A-del | CDKN2A/B deletion | ~15% | Grade 2-3, anaplastic |
| TERT/EZH2 | TERT pC228T/C250T or EZH2/H3K27me3-loss | ~5% | Grade 3, anaplastic |

**Key molecular alterations by location:**
- **Convexity/parasagittal**: NF2 biallelic LOF (~70-75%); 22q deletion; CDKN2A/B deletion in grade 2-3
- **Skull base / meningothelial**: AKT1 E17K (~25-35% of non-NF2 skull base), TRAF7 (~50% of AKT1-mutant co-mutated), KLF4 K409Q (secretory meningioma), SMO (~5%), PIK3CA (~5%)
- **Petroclival**: POLR2A mutations (RNA Pol II largest subunit, WHO grade 1, non-recurrent)
- **Pediatric meningioma**: YAP1-MAML2 fusions, TRAF7 mutations; distinct biology from adult; often require molecular testing
- **Rhabdoid meningioma** (WHO grade 3): BAP1 mutations, SMARCB1 loss rare; H3K27me3 loss; worst OS (~15% 5-year)

## Function

### Normal arachnoid cap cell biology

Arachnoid cap cells are epithelioid cells forming arachnoid granulations (Pacchionian bodies) that protrude into dural sinuses → facilitate CSF resorption into venous blood via vesicular transcytosis. Normal arachnoid cap cells:
- Express vimentin, EMA, PR (progesterone receptor), somatostatin receptors (SSTR2-5) — the latter explaining octreotide uptake on PET
- Form whorls → psammoma bodies (calcium deposition within necrotic whorl centers)
- Are highly adherent and contact-inhibited (NF2-Hippo pathway active in normal state)
- Do not cross the dura (making meningiomas non-infiltrative in grade 1)

Meningioma genesis: NF2 LOF or oncogenic activation (AKT1 E17K, SMO) → Hippo off (NF2 pathway) or PI3K/mTOR on (AKT1) → unchecked proliferation while retaining arachnoid cap cell identity.

## Pathology

### Treatment

**Surgery:**
Maximal safe resection is the cornerstone; Simpson grading of resection:
- Simpson grade 1 (GTR + coagulation of dural attachment + bone excision): lowest recurrence
- Simpson grade 2 (GTR + coagulation): adequate for most convexity tumors
- Simpson grade 3 (GTR, no dural treatment): acceptable if dura not involved
- Simpson grade 4 (STR/debulking): deliberate STR for skull base to preserve neurovascular structures; followed by SRS or observation
- Simpson grade 5 (biopsy only): very rare; for inaccessible deep lesions

Surgical morbidity is location-dependent: skull base (CN palsy, CSF leak), parasagittal (venous thrombosis if SSS invaded), cavernous sinus (CN III/IV/VI/V1/V2; often intentionally subtotally resected).

**Stereotactic radiosurgery (SRS):**
- Gamma Knife / CyberKnife / LINAC-based SRS; single fraction 12-16 Gy (grade 1) or 15-18 Gy (grade 2-3)
- Grade 1 residual after STR: SRS achieves ~92-95% local control at 5 years
- Primary SRS (for small symptomatic meningiomas not amenable to surgery): 5-year control ~95%
- NF2-associated VS: SRS 11-13 Gy → 97% tumor control at 5 years; hearing preservation in ~50%
- Limitations: max diameter ~3-3.5 cm; proximity to optic apparatus, brainstem

**Fractionated radiotherapy (FSRT/IMRT/proton):**
- Grade 2 post-op STR or recurrent grade 1: FSRT 54 Gy/30 fx
- Grade 3 post-op: FSRT 60 Gy/30 fx ± boost; adjuvant RT regardless of extent of resection
- Proton for skull base (reduce dose to optic chiasm, brainstem, cochlea); PTCOG studies ongoing

**Bevacizumab:**
VEGF overexpression in meningioma (YAP target); Phase 2 COMBIT (Huang 2019, N=40): ORR 40%, PFS 18.7 months (vs historical 6 months); predominantly grade 2-3 refractory; not FDA-approved for meningioma; used off-label.

**Systemic therapies (investigational):**
- Nivolumab/pembrolizumab: ~10-15% ORR in grade 3; PD-L1 variable expression; low TMB limits immunotherapy
- Octreotide/pasireotide: SSTR2-positive meningiomas; octreotide PET (Ga-68-DOTATATE) for staging/recurrence; SSA as palliative therapy for symptom control but not proven anti-tumor in controlled trials
- Mifepristone (anti-progesterone): SWOG-S9005 Phase 3: no benefit in unresectable PR+ meningioma vs placebo; PR expression does not predict hormone-blocking response
- AKT inhibitors (capivasertib): AKT1 E17K meningioma → Phase 2 (ACNS1920 for NF2 with AKT1 mutation; Lumiere trial)
- mTOR inhibitors: everolimus for NF2-associated VS (REACT, off-label); CERN Foundation trials in recurrent grade 2-3 meningioma ongoing
- TEAD inhibitors (VT3989, IAG933, TED-347): Phase 1 in NF2-null mesothelioma (most advanced) → expansion into NF2-null meningioma anticipated
- CDK4/6 inhibitors (palbociclib): CDKN2A-deleted grade 2-3 meningioma → Phase 2 (NCT04452214); CDKN2A/B deletions confer worst prognosis

**Prognosis:**
- WHO grade 1: 10-year OS ~90%; death often from co-morbidities
- WHO grade 2: 10-year OS ~65-70%; death from tumor progression or PTBE
- WHO grade 3: 5-year OS ~35-60%; median OS ~24-36 months from grade 3 diagnosis
- CDKN2A/B-deleted meningioma (any grade): median OS ~5 years
- TERT/EZH2 methylation class: median OS ~2-3 years

## Connections

- `connects-to` → **[NF2](../../03-molecular/nf2/README.md)** — NF2 biallelic LOF in ~50-60% sporadic meningioma; NF2 loss → Hippo inactivation → YAP/TAZ nuclear → TEAD-driven proliferation; NF2-mutant meningiomas are convexity-predominant; germline NF2 → bilateral VS, meningiomas, ependymomas; TEAD inhibitors in Phase 1 trials.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — AKT1 E17K (~10-12% skull base meningioma, grade 1) directly activates mTORC1/mTORC2; NF2 loss → Hippo off → YAP/TAZ nuclear → upstream mTOR activators; mTOR inhibitors (everolimus/sirolimus) in NF2 syndrome VS (REACT trial, 2012): volumetric reduction of VS in 30-44% of patients.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — AKT1 E17K and NF2 loss both engage EGFR/ErbB signaling in meningioma; NF2-null → ErbB2 surface overexpression → sustained RAS/MAPK; erlotinib and gefitinib explored in recurrent meningioma with modest activity; ErbB2 amplification is rare in meningioma.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss in ~10-15% meningioma; NF2 and PTEN both suppress PI3K/AKT/mTOR → NF2+PTEN co-loss is synergistic; AKT1 E17K (skull base meningioma, ~10-12%) activates PI3K/mTOR without PTEN loss; mTOR inhibitors target the convergent PI3K/mTOR axis in meningioma.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Meningioma is the most common intracranial tumor, arising not from brain but from arachnoid cap cells of the meninges; it compresses brain and cranial nerves, and location (convexity, skull base, parasagittal) dictates resectability and surgical morbidity more than grade.
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — Germline NF2 loss (neurofibromatosis type 2) predisposes to multiple meningiomas alongside bilateral vestibular schwannomas and ependymomas; sporadic meningiomas carry biallelic NF2 loss in ~50-60%, making merlin/Hippo inactivation the central driver in both settings.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Grade 1 meningiomas show a 2-3:1 female predominance and express progesterone receptors, with growth during pregnancy and on medroxyprogesterone exposure; yet anti-progesterone mifepristone failed in Phase 3, so PR positivity does not predict hormone-blockade response.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — Meningioma and mesothelioma are unrelated tumors united by one driver: biallelic NF2/merlin loss inactivates Hippo, freeing YAP/TAZ-TEAD to drive proliferation in ~50-60% of meningiomas and ~40% of mesotheliomas — making both lead indications for TEAD inhibitors now in trials.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Meningioma growth runs through YAP: NF2/merlin loss releases YAP/TAZ to partner with TEAD and transcribe proliferative genes; this Hippo-YAP axis, not a classic oncogene, drives most meningiomas, and TEAD-palmitoylation inhibitors are the first targeted therapy in trials.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Meningioma is the most common primary CNS tumor, but it arises from the meninges (arachnoid cap cells), not neural tissue — growing outside the brain and spinal cord and causing symptoms by compression; its dural-based, extra-axial location makes many curable by resection.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Ionizing radiation is the best-established environmental cause of meningioma: prior cranial radiotherapy (even low-dose scalp irradiation) markedly raises risk, often producing higher-grade, multiple tumors decades later—while focused radiosurgery also treats inaccessible ones.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — Meningioma and glioblastoma are the two commonest primary brain tumors but opposite: meningioma is an extra-axial, dural-based, usually benign and resectable tumor of arachnoid cells, while glioblastoma is intra-axial, diffusely infiltrative and malignant—distinguished on MRI.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Meningioma and breast cancer are linked through hormones and co-occurrence: most meningiomas express progesterone (and some estrogen) receptors, grow in pregnancy and the luteal phase, and the two are epidemiologically associated—a breast-cancer history can accompany meningioma.
- `connects-to` → **[Chordoma](../chordoma/README.md)** — Meningioma and chordoma are both slow-growing extra-axial tumors of the skull base and spine: meningioma arises from arachnoid cap cells, chordoma from notochord remnants in the clivus or sacrum—both treated by resection plus radiotherapy and prone to local recurrence.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Meningioma and primary CNS lymphoma can both appear as enhancing masses but differ: meningioma is an extra-axial dural tumor cured by resection, while PCNSL is an intra-axial B-cell lymphoma treated with methotrexate, not surgery—so location and biopsy decide.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — Meningioma and IDH-mutant glioma sit in opposite brain compartments: meningioma is extra-axial, dural-based and usually benign, while IDH-mutant glioma is intra-axial and infiltrative—MRI location (the dural tail) distinguishes the resectable from the diffuse.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Meningiomas threaten the brain by compression, not invasion: arising from arachnoid cap cells of the meninges, they grow slowly and push on neurons and cortex, causing seizures and focal deficits—so symptoms come from mass effect, not infiltration of the brain.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — Meningioma sits in the NF2/schwannomatosis tumor family: NF2 (merlin) loss drives sporadic meningiomas and the multiple meningiomas, schwannomas and ependymomas of NF2, so a young patient with several meningiomas should prompt NF2-spectrum genetic testing.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Meningiomas are often hormone-responsive: many express progesterone and estrogen receptors, can enlarge during pregnancy or with hormonal therapy, and are commoner in women—so hormonal status influences their growth and is weighed in management.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy refines radiation for meningioma: many sit at the skull base wrapped around nerves and vessels, so protons' sharp dose stop point delivers high dose to the tumor while sparing the adjacent brain, optic nerves and brainstem.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Some meningiomas are fibroblastic: arising from arachnoid cap cells, these benign tumors can take a spindle-cell, collagen-rich (fibroblastic) form, one of several histologic subtypes that, with grade and location, guide whether surgery alone or added radiation is needed.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF drives the brain swelling around meningiomas: tumor VEGF makes vessels leaky, producing the peritumoral edema that often causes symptoms more than the mass itself, so anti-VEGF bevacizumab is tried for edema and recurrent disease.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — Meningiomas light up with somatostatin imaging: they strongly express SSTR2, so 68Ga-DOTATATE PET pinpoints tumor and residual disease better than MRI alone, and somatostatin analogues are tried in tumors that recur after surgery and radiation.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT marks the dangerous meningiomas: TERT promoter mutations reactivate telomerase and now define a higher WHO grade, flagging tumors likely to recur aggressively regardless of how benign they look under the microscope.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Meningiomas can remodel the overlying skull: en plaque tumors signal osteoblasts to thicken adjacent bone (hyperostosis), a radiologic clue to the diagnosis and a reason surgery sometimes must remove involved bone.
- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — A subset of meningiomas is driven by Hedgehog through SMO: skull-base tumors often carry SMO mutations rather than NF2 loss, defining a molecular subgroup that—like basal cell carcinoma—might respond to smoothened inhibitors.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion marks the most dangerous meningiomas: losing this tumor-suppressor now defines WHO grade 3 regardless of how the cells look, so molecular testing for CDKN2A reclassifies aggressive tumors that histology alone would underestimate.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Meningiomas are infiltrated mainly by macrophages: these tumor-associated immune cells are the dominant inflammatory population in the tumor and may support its growth, making the meningioma's immune niche a target of interest.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Meningiomas lay down calcium as psammoma bodies: these concentric calcified whorls are a histologic hallmark and make many meningiomas visibly calcified on imaging, a clue that helps distinguish them from other brain tumors.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Some meningiomas are driven by AKT mutations: recurrent AKT1 changes switch on the PI3K-AKT-mTOR growth pathway in non-NF2 tumors, defining a molecular subgroup that AKT and mTOR inhibitors are being tested against.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Meningiomas largely evade cytotoxic T cells: beyond their dominant macrophages, they keep a T-cell-poor, immunosuppressive microenvironment, which is part of why checkpoint immunotherapy has had limited success in the tumor.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Meningiomas can blind through the eye: those arising on the optic nerve sheath or near the orbit compress the nerve and push the eye forward (proptosis), causing slow, painless vision loss.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Meningiomas calcify with calcium phosphate: their hallmark psammoma bodies are concentric whorls of calcium-phosphate mineral, a histologic signature also visible as flecks of calcification on imaging.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Meningiomas are vascular tumors fed by endothelial cells: they recruit a rich blood supply, giving the bright contrast enhancement and 'dural tail' seen on MRI, and making them prone to bleed during surgery.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy fingerprints meningiomas: their meningothelial cells interlock through elaborate interdigitating processes joined by desmosomes — an ultrastructural signature that confirms the diagnosis when light microscopy is ambiguous.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Meningiomas run on a PDGF autocrine loop: the tumor cells make platelet-derived growth factor and carry its receptor, driving their own proliferation — a pathway studied as a target for the aggressive grades that resist surgery and radiation.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — When a meningioma defies expectation and metastasizes, the lung is its commonest destination: though nearly all are benign and stay local, malignant variants spread hematogenously, with pulmonary deposits the classic distant site.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Meningiomas can thicken the skull they sit against: en plaque tumors provoke reactive hyperostosis of the overlying bone, and some arise within the marrow-bearing skull itself as intraosseous meningiomas.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Rarely a meningioma breaks through to the scalp: extracranial extension or a primary cutaneous meningioma forms a firm scalp nodule, the tumor reaching the skin from the meninges beneath the skull.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — If a malignant meningioma spreads, the liver is among its targets: after the lungs, hematogenous metastases can lodge in the liver and bone, the unusual distant spread of an aggressive grade.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies grade and target the tumor: EMA, SSTR2, and progesterone-receptor stains confirm a meningioma and a high Ki-67 antibody index flags the aggressive grades, while the SSTR2 it displays makes it visible on DOTATATE imaging and a peptide-therapy target.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Though it grows outside the brain, a meningioma still irritates it: the slow dural mass compresses cortex and provokes peritumoral edema and reactive astrocyte gliosis in the underlying brain, the swelling that causes seizures and focal deficits.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy can wake a meningioma: many carry progesterone receptors and visibly enlarge under the hormone surge that the placenta drives, sometimes turning symptomatic in the third trimester and shrinking again after delivery.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hormones explain meningioma's female slant: it is far commoner in women, and long-term high-dose progestins like cyproterone acetate are now a recognized, dose-dependent cause — an iatrogenic link that has reshaped how these drugs are prescribed.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Few cancers clot like a brain tumor patient: meningioma carries a high risk of deep-vein thrombosis and pulmonary embolism from the tumor's procoagulant tissue factor, the immobility around craniotomy, and steroid use, demanding careful prophylaxis.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets feed the meningioma's clotting tendency: the tumor's tissue factor activates them into the hypercoagulable state behind its thrombosis risk, and they also help build the rich vasculature that makes these tumors bleed at surgery.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Meningiomas split into molecular flavors: alongside NF2 loss, a subset is driven by activating PIK3CA mutations that fire the PI3K-AKT growth pathway, marking tumors that may respond to PI3K-pathway inhibitors rather than NF2-targeted approaches.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Sitting on the cortex, they spark seizures: convexity meningiomas irritate and compress the brain surface, so epilepsy is a common presenting sign and often persists, requiring anticonvulsants even after the tumor is removed.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Higher-grade meningiomas wall themselves off immunologically: their microenvironment fills with regulatory T cells and exhausted infiltrate that suppress attack, a feature that worsens with grade and is studied as a target for immunotherapy in aggressive tumors.
- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — Chromatin-remodeling genes drive familial meningiomas: germline SMARCB1 and SMARCE1 (SWI-SNF) mutations cause multiple and clear-cell/spinal meningiomas, a distinct genetic route apart from the common NF2-loss tumors.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — Hedgehog-pathway syndromes seed them too: a subset of meningiomas is driven by SMO/SHH activation, the same pathway deranged in Gorlin syndrome, linking these dural tumors to hedgehog-pathway predisposition.
- `connects-to` → **[Stroke](../stroke/README.md)** — A meningioma can choke the brain's drainage: parasagittal tumors invade the dural venous sinuses, and the resulting venous obstruction (or peritumoral edema) can precipitate venous infarction and stroke-like deficits.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Merlin loss activates STAT3: NF2/merlin-deficient meningiomas show STAT3 signaling that supports their growth, paralleling the schwannoma biology of the same tumor-suppressor loss.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Merlin normally restrains NF-κB: its loss in meningioma lifts that brake, engaging NF-κB-driven survival and inflammatory signaling among the pathways downstream of NF2 inactivation.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Craniotomy carries infectious risk: the surgery used to resect meningiomas can be complicated by wound infection or meningitis, which in the postoperative patient can progress to sepsis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Its location and surveillance weigh on the mind: frontal meningiomas can directly alter mood and personality, and the anxiety of watchful waiting over a brain tumor contributes to depression.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Steroids for brain swelling thin the bones: the corticosteroids used to control peritumoral edema around meningiomas, especially with prolonged or repeated courses, accelerate bone loss and fracture risk.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Aggressive disease and its treatment blunt the marrow: atypical and anaplastic meningiomas that recur and require radiation or chemotherapy carry an inflammatory burden that can produce an anemia of chronic disease.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Skull-base tumors compress cranial nerves: meningiomas near the cavernous sinus or skull base entrap the trigeminal and other cranial nerves, producing facial and neuropathic pain.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Its steroids raise blood sugar: the dexamethasone used to control peritumoral edema around a meningioma induces insulin resistance and can precipitate steroid-induced diabetes.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Craniotomy and steroids hinder repair: the surgery to resect a meningioma, often with chronic dexamethasone, leaves scalp and dural wounds prone to CSF leak and slow healing.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is hormone-sensitive and presses on the pituitary: meningiomas express progesterone receptors and can grow in pregnancy, and skull-base tumours compress the pituitary and hypothalamus.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It reshapes the skull bone: meningiomas characteristically provoke hyperostosis of the overlying calvarium and can invade and remodel the cranial bones, a recognised radiological hallmark.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An incidental brain tumour under watch breeds worry: the surveillance of a slow-growing meningioma, fear of growth or recurrence and neurological symptoms foster chronic health anxiety alongside depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Scalp radiation seeds it and it can reach the scalp: meningiomas are a recognised late effect of childhood cranial radiation, and large convexity tumours can erode the skull toward the scalp.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Skull-base tumours press on the breathing centres: posterior-fossa and skull-base meningiomas can compress the brainstem, impairing the control of breathing and swallowing.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — These vascular tumours engage the circulation: meningiomas are often embolised before surgery to reduce bleeding, and parasagittal tumours can invade and occlude the dural venous sinuses.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It carries an immune microenvironment: high-grade meningiomas harbour tumour-infiltrating immune cells, and checkpoint immunotherapy is under trial for aggressive, treatment-resistant disease.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It expresses somatostatin receptors: refractory meningiomas are treated in trials with somatostatin-analogue and SSTR-targeted radionuclide (DOTATATE) therapy, alongside anti-VEGF agents.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It can rarely spread to the liver: although usually benign, malignant grade-3 meningioma can metastasise outside the skull, including to the liver and lungs.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It thickens the overlying skull: meningiomas characteristically provoke reactive hyperostosis of the adjacent skull bone, a radiological clue, and can invade bone directly.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo barely helps: meningioma is largely chemoresistant, so surgery and radiation dominate, with somatostatin analogues and hydroxyurea giving only modest benefit in refractory disease.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Trials in the aggressive grades: low-grade meningiomas are immunologically quiet, but PD-1 checkpoint inhibitors are being trialled for the rarer high-grade and recurrent meningiomas.
- `connects-to` → **[Atypical Teratoid Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — A shared SWI/SNF lesion: rhabdoid meningiomas and atypical teratoid/rhabdoid tumours both lose SMARCB1, a subunit of the SWI/SNF chromatin-remodelling complex, so the same epigenetic machinery failure produces an aggressive meningioma and a malignant childhood CNS tumour.
- `connects-to` → **[ALL](../all/README.md)** — A late price of curing leukaemia: cranial irradiation for childhood acute lymphoblastic leukaemia is a leading cause of radiation-induced meningiomas, which emerge as second tumours decades later—so survivors need long-term neuro-imaging surveillance.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — It shares a theranostic target with carcinoids: meningiomas strongly express somatostatin receptor 2, so like neuroendocrine tumours they light up on DOTATATE PET and can be treated with peptide receptor radionuclide therapy.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Radiation-induced meningioma: childhood cranial radiotherapy—for medulloblastoma or leukaemia—is a leading cause of secondary meningiomas arising decades after treatment.
- `connects-to` → **[MEN4 Syndrome](../men4-syndrome/README.md)** — An endocrine-syndrome association: MEN4 (CDKN1B loss) raises the risk of meningiomas alongside its parathyroid and pituitary tumours, one of the germline syndromes that predispose to them.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Compression of the neural axis: as it grows from the dura, a meningioma compresses the brain, cranial nerves and their axons, and the resulting axonal dysfunction produces its focal deficits and seizures.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Radiation-induced and predisposed: meningioma is the commonest radiation-induced brain tumour, and Li-Fraumeni patients given radiotherapy face a high rate of them—one reason radiation is avoided in the syndrome wherever possible.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — The malignant mimic: lung and breast cancers commonly seed dura-based metastases that radiologically imitate a meningioma, the key malignant differential of a dural mass in a patient with known cancer.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — A vascular tumour: meningiomas parasitise dural arterial feeders such as the middle meningeal artery, vessels often embolised before surgery to shrink the tumour and reduce intraoperative bleeding.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle target: CDKN2A loss in high-grade meningioma unleashes CDK4/6-driven proliferation, making CDK4/6 inhibition a candidate strategy for aggressive tumours.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic progression: EZH2 and polycomb activity contribute to the malignant progression of higher-grade meningiomas, an emerging epigenetic vulnerability.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Developmental signalling: dysregulated Notch signalling participates in meningioma tumorigenesis, interacting with the NF2-Hippo axis that defines many of these tumours.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: with CDKN2A loss marking higher-grade tumours, cyclin D1-CDK4/6 activity pushes meningioma cells through the G1 checkpoint.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Proliferative oncogene: MYC activation drives the proliferation of atypical and anaplastic meningiomas, contributing to their aggressive, recurrent behaviour.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the highly vascular meningioma drives the VEGF angiogenesis that supplies these dural-based tumours and the peritumoural oedema they cause.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MAPK-pathway meningiomas: RAF-MEK-ERK signalling downstream of TRAF7/KLF4 and AKT1 mutations drives the proliferation of a major non-NF2 molecular subgroup of meningiomas.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Growth-factor signalling: IGF-1/IGF-1R signalling supports meningioma proliferation and survival, contributing to the growth of these slow but recurrence-prone dural tumours.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into meningiomas, which make up a substantial fraction of the tumour mass and shape its growth.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4-CXCL12 signaling promotes the brain and bone invasion of higher-grade meningiomas, the infiltrative growth that drives the recurrences dominating the morbidity of these otherwise often-benign dural tumors.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Meningiomas invading the adjacent skull stimulate RANKL-driven bone remodeling, producing the reactive bony thickening (hyperostosis) that is a characteristic radiological sign and a route of local spread.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Stereotactic radiosurgery and radiotherapy for residual or high-grade meningiomas kill tumor cells through caspase-3-mediated apoptosis, whose evasion contributes to the recurrence of the aggressive grade 2 and 3 tumors.
- `connects-to` → **[Src kinase](../../03-molecular/src-kinase/README.md)** — The NF2/merlin loss that drives most meningiomas disinhibits Src/FAK at the membrane, since merlin normally restrains them—the loss of contact inhibition that lets the meningothelial cells proliferate.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNA-methylation profiling stratifies meningiomas into prognostic classes that predict recurrence better than histological grade alone, making the methylome an increasingly central tool in their classification and management.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Many meningiomas form psammoma bodies—concentric, calcified laminated structures—a characteristic histological hallmark, and the tumor's calcification can be visible on imaging.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The CDK4/6-cyclin-D1 axis (mapped, with CDKN2A loss marking higher grade) releases E2F1 to drive the accelerated proliferation of atypical and anaplastic meningioma.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 inactivation accompanies the progression of meningioma to the anaplastic grade-3 tumor, removing an apoptotic and cell-cycle brake on the malignant clone.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling shapes the fibroblastic and transitional phenotypes of meningioma and the collagenous stroma of these dura-derived tumors.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Deregulation of the RB1-E2F checkpoint (E2F1, CDK4/6, CDKN2A and cyclin-D1 already mapped) marks the progression of meningioma toward higher WHO grade.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-MAPK signaling (ERK1/2 already mapped) contributes a proliferative input to meningioma growth.
- `connects-to` → **[SUFU](../../03-molecular/sufu/README.md)** — SUFU is a negative regulator of the Sonic-Hedgehog pathway (SMO already mapped), the pathway recurrently activated in the non-NF2 molecular subgroup of skull-base meningiomas.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 expression marks higher-grade meningiomas and modulates their invasive and immune behavior.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) modulates the proliferation and stromal interactions of meningioma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 mapped) provides a proliferative input contributing to meningioma growth.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune microenvironment of meningioma, relevant to immunotherapy in aggressive higher-grade tumors.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory microenvironment and radiation response of meningioma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by the AKT signaling activated by NF2/merlin loss, modulate the survival of meningioma cells.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and Hedgehog signaling co-opted in the tumorigenesis of meningioma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the progression toward higher-grade meningioma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of meningioma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is relevant to the immune response against meningioma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the NF2/merlin-deficient cells of meningioma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A and the SWI/SNF machinery (SMARCB1 already mapped) contribute to the epigenetic dysregulation of meningioma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of meningioma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of meningioma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of meningioma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of meningioma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of meningioma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of meningioma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the tumor microenvironment of meningioma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of meningioma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the tumor microenvironment and progression of meningioma.
- `connects-to` → **[Androgen receptor](../../03-molecular/androgen-receptor/README.md)** — Hormone-receptor expression: meningiomas express progesterone (already mapped) and androgen receptors, and their tendency to grow during pregnancy and in women reflects the hormone responsiveness of these tumours.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy: MHC class II antigen presentation shapes the T-cell response to meningioma, of growing interest for the higher-grade and recurrent tumours that resist surgery and radiation and are being explored for checkpoint therapy.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: IL-2-driven T-cell expansion supports the immunotherapy approaches under investigation for aggressive grade 2-3 meningiomas, which have a more immunosuppressive microenvironment than benign lesions.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the microenvironment of higher-grade meningiomas dampens the anti-tumour T-cell response (IL-2 and MHC class II already mapped), part of the immune evasion that motivates the checkpoint strategies explored for aggressive tumours.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of meningiomas, part of the stromal biology supporting these often highly vascular extra-axial tumours.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Fibrous stroma: the fibroblastic and transitional meningioma variants (fibroblast already mapped) lay down a collagen-rich stroma with psammoma bodies, the dense connective tissue that gives these tumours their firm texture.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the meningioma stroma, part of the immune microenvironment of these often indolent tumours.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Peritumoral inflammation: prostaglandins from the tumour and infiltrating cells (IL-6 and IL-1 already mapped) contribute to the peritumoral brain oedema and inflammation that shape the symptoms of meningiomas.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative microenvironment: the meningioma generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species are part of the tumour microenvironment beyond the growth-factor (already mapped) drivers.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immune microenvironment of meningioma.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the macrophages (CCL2 already mapped) form a large part of the immune infiltrate of meningioma, and their M2 polarisation (IL-4 already mapped) shapes the tumour microenvironment.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibrous meningioma: the fibroblastic (fibrous) meningioma is a WHO grade-1 variant of spindled, fibroblast-like cells in a collagen-rich (already mapped) matrix, one of the histological subtypes of the tumour.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity-risk adipokine: leptin links the obesity risk factor to meningioma, alongside the hormone-responsive (progesterone and estrogen already mapped) biology of the tumour.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity-related meningioma risk.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity-related meningioma risk.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the emerging immunotherapy of meningioma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of meningioma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the meningioma immune microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of meningioma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the meningioma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the meningioma microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Peritumoural oedema: the mast cells of the meningioma stroma are associated with the peritumoural brain (already mapped) oedema and contribute to the angiogenesis (VEGF already mapped) and type-2 microenvironment.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate cytotoxicity: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance within the immune microenvironment of meningioma.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the tumour antigen to the T cells (already mapped) shaping the adaptive immune response against meningioma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of meningioma.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of meningioma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the macrophage-rich (already mapped) meningioma stroma.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Peritumoral oedema: bradykinin (B2 receptor) increases blood–brain barrier permeability in the peritumoral zone, driving the cerebral oedema that is a major cause of neurological symptoms in meningioma; bradykinin blockade reduces the vasogenic oedema around meningioma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell stroma: histamine from the mast cells that are notably abundant in meningioma stroma promotes VEGF (already mapped) angiogenesis and matrix-remodelling; mast-cell-derived histamine contributes to the peritumoral oedema and dural invasiveness of meningioma.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Invasive meningeal stroma: periostin secreted by the meningioma-associated fibroblasts and TGF-β (already mapped) signalling promotes the dural adhesion and invasiveness of meningioma; elevated periostin in skull-base meningioma correlates with the WHO grade and recurrence risk.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Meningeal alarmin: TSLP released by the meningioma-associated stromal cells activates dendritic cells and mast cells in the tumour microenvironment, amplifying the TGF-β (already mapped) and VEGF (already mapped) driven peritumoral inflammation and angiogenesis of meningioma.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: C1-INH controls the classical-pathway arm (C3, C5 and C5aR1 already mapped) in the meningioma microenvironment, modulating complement-mediated tumour-cell lysis and the tumour-associated macrophage (already mapped) inflammatory response.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Meningeal EPO signalling: erythropoietin receptor (EPOR) on meningioma cells activates the JAK2/STAT3 (already mapped) pathway, upregulates VEGF-driven (already mapped) angiogenesis and promotes the hypervascular phenotype of WHO grade II-III meningioma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Meningeal oncostasis: melatonin, via MT1/MT2 receptors on meningioma cells and the dural tumour vasculature (already mapped), suppresses VEGF-driven (already mapped) angiogenesis and NF-κB (already mapped) signalling, reducing the peritumoral oedema burden of meningioma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-meningioma axis: testosterone, via androgen receptor on meningioma cells, modulates VEGF-driven (already mapped) and AKT1 (already mapped) proliferative signalling and contributes to the sex-dimorphic incidence and hormone-receptor positivity of meningioma.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Meningeal 5-HT signalling: serotonin from mast cells (already mapped) in meningioma stroma signals via 5-HT2 receptors on meningioma cells and endothelial cells (already mapped), amplifying the VEGF (already mapped) angiogenic and peritumoral oedema cascade.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Meningioma prolactin receptor: prolactin, via PRL-R on meningioma cells and macrophages (already mapped), upregulates NF-κB (already mapped) and IL-6 (already mapped) pro-survival signalling and promotes VEGF-driven (already mapped) angiogenesis in meningioma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Meningioma oxytocin anti-tumour: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling in the peritumoral meningeal microenvironment of meningioma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Meningioma vasopressin vascular: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates dural tumour vascular tone; dysregulation amplifies NF-κB (already mapped) and VEGF (already mapped) angiogenic signalling in meningioma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Meningioma selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the meningioma TME; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory tumour cascade of meningioma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Meningioma iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of meningioma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Meningioma sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of meningioma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Meningioma magnesium: magnesium, as cofactor of antioxidant enzymes in macrophages (already mapped) and fibroblasts (already mapped), supports matrix homeostasis; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of meningioma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Meningioma copper: copper, as cofactor of SOD1 in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges TME ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of meningioma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Meningioma zinc: zinc, as cofactor of metalloproteinases in macrophages (already mapped) and fibroblasts (already mapped), modulates matrix remodelling; zinc depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of meningioma.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Meningioma carbon: carbon as backbone of NF2 (already mapped) and merlin structural proteins in meningeal cells (already mapped) sustains tumour suppression; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) meningioma cascade.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Meningioma chloride: chloride regulates meningeal cells (already mapped) and macrophage (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) protumorigenic cascade of meningioma.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Meningioma nitrogen: nitrogen in amino-acid scaffold of NF2 (already mapped) and TRAF7 proteins sustains meningeal cell (already mapped) proliferation control; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of meningioma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Meningioma hydrogen: hydrogen in meningeal cells (already mapped) and macrophages (already mapped) modulates NF2 (already mapped) protein stability; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of meningioma.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Meningioma iron: iron supports haem metabolism in meningeal cells (already mapped) and macrophages (already mapped) for tumour proliferation; iron dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) oncogenic cascade of meningioma.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Meningioma oxygen: oxygen supports aerobic metabolism in meningeal cells (already mapped) and macrophages (already mapped); oxygen deficit amplifies HIF and NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) angiogenic cascade of meningioma.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Meningioma pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates meningeal immune evasion; pd-1 dysregulation amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Meningioma glp-1: GLP-1 from macrophages (already mapped) and fibroblasts (already mapped) modulates metabolic-inflammatory tone; glp-1 dysfunction amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) meningeal tumour cascade of meningioma.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — Meningioma angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and macrophages (already mapped) drives vascular remodelling; angiotensin-ii excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Meningioma wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and fibroblasts (already mapped) regulates meningeal fate; wnt-beta-catenin dysregulation amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Meningioma fibronectin: fibronectin in macrophages (already mapped) and fibroblasts (already mapped) promotes meningeal ECM remodelling; fibronectin excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Meningioma activin-a: activin-A from macrophages (already mapped) and fibroblasts (already mapped) drives meningeal fibrosis; activin-a excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Meningioma tgf-beta: TGF-β from macrophages (already mapped) and fibroblasts (already mapped) modulates meningeal fibrotic resolution; TGF-β excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Meningioma cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates meningeal neuroimmune tone; cgrp excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Meningioma calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates meningeal calcium balance; calcitonin excess amplifies vegf (already mapped) and smad4 (already mapped) and il-6 (already mapped) cascade of meningioma.

[^brastianos-2013-akt1-meningioma]: Brastianos PK, Horowitz PM, Santagata S, et al. Genomic sequencing of meningiomas identifies oncogenic SMO and AKT1 mutations. *Nat Genet.* 2013;45(3):285-289. [doi:10.1038/ng.2526](https://doi.org/10.1038/ng.2526) · [PubMed 23334667](https://pubmed.ncbi.nlm.nih.gov/23334667/)
[^nassiri-2021-meningioma-classification]: Nassiri F, Liu J, Patil V, et al. A clinically applicable integrative molecular classification of meningiomas. *Nature.* 2021;597(7874):119-125. [doi:10.1038/s41586-021-03850-3](https://doi.org/10.1038/s41586-021-03850-3) · [PubMed 34385709](https://pubmed.ncbi.nlm.nih.gov/34385709/)
