---
schema: human-scale-entry/v1
id: thyroid-cancer
name: Thyroid Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Malignant thyroid tumors: papillary (BRAF V600E ~60%, RET/PTC fusions ~20%), follicular, medullary (RET mutation MEN2), and anaplastic; differentiated thyroid cancer treated with RAI and lenvatinib/sorafenib; RET-mutant MTC → selpercatinib; BRAF+ ATC → dabrafenib+trametinib."
aliases: ["thyroid cancer", "thyroid carcinoma", "papillary thyroid carcinoma", "medullary thyroid carcinoma", "anaplastic thyroid carcinoma", "differentiated thyroid cancer", "PTC", "MTC", "ATC", "DTC"]
sources:
  - id: schlumberger-2015-lenvatinib
    type: peer-reviewed
    cite: "Schlumberger M, Tahara M, Wirth LJ, et al. Lenvatinib versus placebo in radioiodine-refractory differentiated thyroid cancer. N Engl J Med. 2015;372(7):621-630."
    doi: "10.1056/NEJMoa1406470"
    pmid: "25671254"
    url: "https://doi.org/10.1056/NEJMoa1406470"
  - id: subbiah-2018-atc-dabrafenib
    type: peer-reviewed
    cite: "Subbiah V, Kreitman RJ, Wainberg ZA, et al. Dabrafenib and trametinib treatment in patients with locally advanced or metastatic BRAF V600-mutant anaplastic thyroid cancer. J Clin Oncol. 2018;36(1):7-13."
    doi: "10.1200/JCO.2017.73.6785"
    pmid: "28892432"
    url: "https://doi.org/10.1200/JCO.2017.73.6785"
cross_links:
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E in ~60% of papillary thyroid carcinoma → ERK activation → dedifferentiation → radioiodine resistance; dabrafenib+trametinib approved for BRAF V600E-mutant ATC (2018, first targeted therapy for ATC); vemurafenib+cobimetinib in radioiodine-refractory DTC under study."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Differentiated thyroid cancer is highly vascular; VEGF and VEGFR2 overexpressed in PTC and FTC → promotes metastasis; lenvatinib (multikinase: VEGFR1-3, RET, FGFR, PDGFRβ) approved for RAI-refractory DTC; sorafenib (VEGFR2/3 + BRAF + RET) also approved for RAI-refractory DTC."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PTEN loss and PIK3CA mutations activate mTOR in follicular thyroid carcinoma and ATC; everolimus (mTORC1 inhibitor) studied in RAI-refractory DTC; mTOR pathway activation mediates resistance to VEGFR-targeted TKIs (lenvatinib, sorafenib) in DTC → mTOR combination strategies."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-L1 expressed in ~30-50% of papillary and ~50-70% of anaplastic thyroid carcinoma → T cell exclusion; pembrolizumab studied with lenvatinib for RAI-refractory DTC and ATC; spartalizumab + dabrafenib+trametinib in BRAF+ ATC; anti-PD-1 active in radioiodine-refractory DTC."
  - target: 01-human/03-molecular/ret
    relation: connects-to
    note: "RET drives the C-cell lineage of thyroid cancer: germline RET mutations cause MEN2 medullary thyroid carcinoma, somatic RET ~40% of sporadic MTC, and RET/PTC fusions ~20% of papillary cancer; selective RET inhibitors selpercatinib and pralsetinib are highly active."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Differentiated thyroid cancers retain the sodium-iodide symporter (NIS), letting them concentrate radioiodine (I-131) whose beta emission ablates tumor — a targeted therapy; BRAF V600E silences NIS, causing radioiodine refractoriness that MEK inhibitors can partly reverse."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Medullary thyroid carcinoma arises from calcitonin-secreting C cells, so serum calcitonin (and CEA) is both a screen before thyroid surgery and the key tumor marker afterward; a calcitonin doubling time under 6 months signals aggressive disease and prompts early systemic therapy."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Medullary thyroid carcinoma is a neuroendocrine tumor: it arises from calcitonin-secreting parafollicular C cells (neural-crest-derived), not iodine-handling follicular cells, so it ignores radioiodine and is tracked by calcitonin/CEA — closer to other NETs than papillary cancer."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "FAP confers a distinctive thyroid risk: cribriform-morular thyroid carcinoma, a rare papillary variant occurring almost exclusively in young women with germline APC mutations, can be the presenting sign of undiagnosed FAP — prompting colonoscopy and APC testing."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunotherapy is reshaping the worst thyroid cancers: anaplastic and radioiodine-refractory tumors express PD-L1 and exclude cytotoxic T cells, so anti-PD-1 (pembrolizumab), often with lenvatinib or BRAF/MEK inhibitors, reactivates CD8+ killing in these rapidly fatal cancers."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Medullary thyroid carcinoma and pheochromocytoma are the linked tumors of MEN2: a germline RET mutation drives both, so a patient with medullary thyroid cancer must be screened for pheochromocytoma before any surgery to avoid an intraoperative hypertensive crisis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Thyroid cancer is the commonest endocrine malignancy: most are differentiated (papillary/follicular) tumors of iodine-avid follicular cells curable with surgery and radioiodine, while medullary (C-cell, calcitonin) and anaplastic types behave very differently."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Cowden syndrome is a hereditary cause of thyroid cancer: germline PTEN loss unleashes PI3K/mTOR signaling, predisposing to follicular thyroid carcinoma alongside breast and endometrial cancer, so multinodular goiter in a Cowden patient warrants close thyroid surveillance."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Thyroid cancer arises within the thyroid gland and exploits its physiology: most are differentiated tumors that still take up iodine and respond to TSH, so thyroidectomy plus radioiodine and TSH suppression treat it through the gland's own biology."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiation has a dual relationship with thyroid cancer: childhood external radiation is a leading cause of papillary thyroid cancer, yet radioactive iodine is a treatment mainstay, and external photon radiotherapy is reserved for anaplastic or unresectable disease."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "Thyroid cancer and head and neck squamous cancer are the two main neck malignancies: thyroid cancer is a usually indolent endocrine tumor curable with surgery and radioiodine, while HNSCC is an aggressive smoking/HPV-driven mucosal carcinoma—neck radiation links them."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Differentiated thyroid cancer keeps the gland's hormone machinery, enabling unique therapy: it still takes up iodine and responds to TSH, so radioactive iodine ablates residual tumor and thyroid-hormone (TSH suppression) therapy starves it—treatment exploiting normal physiology."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Papillary thyroid cancer spreads through the lymphatic system: it characteristically metastasizes to cervical lymph nodes (often the presenting sign) yet remains highly curable, so nodal spread shapes surgery but, unusually for cancer, rarely dooms the patient."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Follicular thyroid cancer spreads hematogenously to the lung and bone: unlike papillary's nodal route, it invades blood vessels to seed distant organs—so the lung is a classic metastatic site, treatable with radioactive iodine if the deposits still take up iodine."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune system frames several thyroid cancers: chronic Hashimoto's autoimmune thyroiditis predisposes to papillary cancer and primary thyroid lymphoma, while checkpoint inhibitors are tried in aggressive anaplastic disease that resists radioiodine."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Bone metastases make thyroid cancer a musculoskeletal disease too: spinal and pelvic deposits cause pathological fractures, cord compression, and pain, so management adds bisphosphonates, surgery, and targeted radiotherapy beyond radioiodine to protect the skeleton."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "Thyroid tumors sit within inherited endocrine neoplasia: medullary thyroid cancer defines MEN2 via RET, and although MEN1 centers on parathyroid, pituitary, and pancreas, both syndromes prompt the familial work-up any endocrine tumor demands."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutations mark dangerous thyroid cancer: reactivating telomerase, they predict aggressive behavior and—combined with BRAF—drive the dedifferentiation toward lethal anaplastic thyroid cancer, refining prognosis beyond histology alone."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "A subset of thyroid cancers is driven by NTRK fusions: these rearrangements, more common in radiation-exposed and pediatric tumors, are targetable with TRK inhibitors like larotrectinib—so molecular testing finds patients beyond the usual BRAF and RET."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Aggressive thyroid cancers fill with tumor-associated macrophages: especially in anaplastic disease, these immune cells dominate the stroma and promote invasion and immune escape, a microenvironment feature tied to poor prognosis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "The thyroid runs on selenium, and so does its cancer biology: selenium-dependent enzymes activate thyroid hormone and shield thyrocytes from the hydrogen peroxide of hormone synthesis, so selenium status influences thyroid disease and oxidative damage."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Thyroid cancer turns lethal when it loses p53: TP53 mutation drives the leap from a usually-curable differentiated cancer to anaplastic thyroid carcinoma, one of the most aggressive human tumors—explaining the dedifferentiation step."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Thyroid cancer shelters in a regulatory T-cell-rich niche: Tregs infiltrate aggressive and anaplastic tumors and suppress immunity, a barrier the checkpoint immunotherapy now tried in advanced thyroid cancer must overcome."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Medullary thyroid cancer is a tumor of the calcium thermostat: it arises from the C cells that make calcitonin, so the hormone serves as its tumor marker, and its calcium-regulating lineage defines this distinct, often inherited subtype."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells shape immunotherapy for aggressive thyroid cancer: as antigen-presenters they prime the T-cell response that checkpoint drugs amplify in anaplastic disease, and their dysfunction helps the tumor evade immunity."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Thyroid cancer can spread to the brain: though usually indolent, advanced or anaplastic disease seeds brain metastases through the blood, a sign of aggressive spread that shifts care toward systemic and targeted therapy."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Thyroid cancer can spread to the liver: medullary and advanced or anaplastic disease seed hepatic metastases, extending beyond the usual neck nodes, lung, and bone."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Papillary thyroid cancer recruits fibroblasts: cancer-associated fibroblasts build a desmoplastic stroma around the tumor, the firm scarring that helps it invade and trap calcifications."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Papillary thyroid cancer leaves calcium-phosphate fingerprints: its psammoma bodies are concentric calcium-phosphate calcifications, a histologic clue that also shows as microcalcifications on ultrasound."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy sharpens the diagnosis: it confirms papillary cancer's irregular nuclei with cytoplasm-filled pseudoinclusions and grooves, and reveals the dense-core neurosecretory granules that mark the medullary type as neuroendocrine."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "The sodium-iodide symporter is thyroid cancer's Achilles' heel: well-differentiated tumors keep this pump that hauls iodine into the cell on a sodium gradient, so radioactive iodine slips in to image and irradiate the cancer wherever it has spread."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Follicular thyroid cancer travels in the blood to bone: unlike the papillary type that creeps through lymph nodes, it spreads hematogenously, seeding lytic deposits in the marrow-filled bones of the spine, pelvis, and skull."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The voice hangs on a nerve beside the gland: the recurrent laryngeal nerve runs along the thyroid, so tumor invasion or surgical injury paralyzes a vocal cord, leaving the hoarseness that can be the first sign of an aggressive thyroid cancer."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Treatment puts the heart under strain: the multikinase inhibitors (lenvatinib, sorafenib) used for radioiodine-refractory disease drive hypertension and cardiac dysfunction, while the deliberate TSH-suppressing thyroid hormone dose risks atrial fibrillation."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Keeping the cancer quiet thins the bones: the long-term high-dose thyroid hormone given to suppress TSH after thyroidectomy pushes the body toward a subclinical hyperthyroidism that accelerates bone loss and osteoporosis, especially in older women."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both monitor and identify the tumor: serum thyroglobulin, measured by immunoassay, is the surveillance marker for recurrence (confounded by anti-thyroglobulin antibodies), while TTF-1, thyroglobulin, and calcitonin stains type a tumor on biopsy."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Thyroid cancer strikes women in their fertile years: it is far more common in young women, and radioactive-iodine therapy temporarily impairs fertility and demands contraception, so reproductive planning is woven into treatment."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Advanced therapy taxes the marrow: the multikinase inhibitors for radioiodine-refractory disease and the chemotherapy for anaplastic thyroid cancer suppress the blood counts, dropping neutrophils and raising the risk of infection."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Follicular thyroid cancer leans on PI3K-AKT: PIK3CA mutation or PTEN loss — the latter underlying Cowden-related thyroid tumors — drives this axis, distinct from the BRAF/RAS-MAPK route of papillary cancer and a target in dedifferentiated disease."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Differentiated thyroid cancer favors bone: follicular and papillary tumors seed osteolytic metastases that recruit osteoclasts to resorb bone, and the lifelong TSH-suppressing thyroxine adds its own push toward bone loss."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Its drugs and isotopes pass through the kidney: radioactive iodine is cleared renally, and the multikinase inhibitors for advanced disease cause hypertension and proteinuria, so kidney function shapes both treatments."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "A second oncogene family sorts the subtypes: where BRAF drives most papillary cancers, RAS mutations like KRAS underlie follicular thyroid cancer, a molecular split that increasingly guides diagnosis and targeted treatment."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Excess weight raises the risk: obesity is a consistent risk factor for thyroid cancer, contributing through insulin resistance, chronic inflammation and hormonal changes to the steep rise in its incidence."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Its treatment targets the blood supply: differentiated thyroid cancers are vascular, so the multikinase inhibitors lenvatinib and sorafenib work largely by blocking VEGF receptors on endothelial cells to choke off new vessels."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 helps the aggressive forms grow: anaplastic and advanced thyroid cancers show STAT3 activation that supports proliferation and immune evasion, a pathway studied as a target where BRAF and kinase inhibitors fall short."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB drives the deadliest variant: anaplastic thyroid carcinoma relies heavily on NF-κB signaling for its rapid, invasive growth, making the pathway a candidate target in a cancer that otherwise resists therapy."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Advanced disease raises the clot risk: like other solid cancers, progressive thyroid cancer carries tumor-driven hypercoagulability, and the antiangiogenic kinase inhibitors used to treat it add their own thrombotic and bleeding hazards."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Its targeted drugs spike the pressure: the VEGF-pathway kinase inhibitors lenvatinib and sorafenib used for RAI-refractory thyroid cancer cause prominent hypertension, an on-target vascular effect needing active management."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Antiangiogenic therapy injures the kidney: the same VEGF-targeted inhibitors used in advanced thyroid cancer cause proteinuria and glomerular injury that can progress to chronic kidney disease over prolonged treatment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Advanced disease and its therapy lower the count: progressive metastatic thyroid cancer with its inflammatory burden, compounded by kinase-inhibitor toxicity, can produce an anemia of chronic disease in the minority with aggressive disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "TSH-suppression and kinase inhibitors strain the heart: the lifelong thyroxine used to suppress TSH keeps patients mildly thyrotoxic, risking atrial fibrillation, while lenvatinib and sorafenib raise blood pressure and are cardiotoxic — all routes toward heart failure."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Long-term TSH-suppression can throw clots to the brain: the subclinical hyperthyroidism from suppressive thyroxine promotes atrial fibrillation, and the resulting cardioembolism raises the risk of ischemic stroke."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Cancer and altered thyroid hormone unsettle mood: the diagnosis plus the deliberately abnormal thyroid-hormone levels of suppression therapy and post-thyroidectomy state contribute to depression and impaired quality of life in survivors."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Thyroidectomy and anti-angiogenic drugs heal slowly: total thyroidectomy leaves a neck wound at risk to the recurrent laryngeal nerve and parathyroids, and the multikinase inhibitors for refractory disease impair wound healing."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Some thyroid cancers churn the gut: medullary thyroid cancer secretes calcitonin that causes secretory diarrhoea, and the multikinase inhibitors used for advanced disease commonly cause diarrhoea too."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong recurrence monitoring breeds worry: the thyroglobulin checks, neck ultrasounds and scan-anxiety of thyroid-cancer surveillance foster chronic health anxiety even in this often indolent cancer."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It invades the airway and spreads to the lungs: locally advanced thyroid cancer can infiltrate the trachea causing airway compromise, and differentiated thyroid cancer metastasises to the lungs."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Surgery threatens the voice and the nerves: thyroidectomy risks recurrent laryngeal nerve injury with hoarseness, and the resulting hypoparathyroidism causes hypocalcaemic tetany and paraesthesiae."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Aggressive disease reaches the skin: anaplastic thyroid cancer invades the overlying neck skin, and the radioiodine and surgery used for thyroid cancer leave their own cutaneous and scar effects."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its hormone-suppression and targeted drugs strain the heart: long-term TSH-suppressive levothyroxine can cause atrial fibrillation, and multikinase inhibitors like lenvatinib cause hypertension and QT prolongation."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its targeted drugs reach the kidney: the multikinase inhibitors used for advanced thyroid cancer cause proteinuria and hypertension that affect renal function."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "It travels with breast cancer: thyroid and breast cancer co-occur more often than chance, so survivors of one carry a modestly raised risk of the other."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It is treated by isotope and kinase drugs: radioactive iodine ablates differentiated thyroid cancer, while multikinase and RET-specific inhibitors (selpercatinib) treat advanced and medullary disease."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "A fellow thyroid-tumour syndrome: Carney complex predisposes to thyroid adenomas and carcinoma, joining the inherited syndromes that raise thyroid-cancer risk."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "It runs in DICER1 families: DICER1 syndrome predisposes to differentiated thyroid carcinoma and multinodular goitre from childhood, part of inherited thyroid-cancer surveillance."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Mostly chemoresistant except anaplastic: differentiated thyroid cancer responds poorly to cytotoxic chemotherapy, relying on surgery and radioiodine, whereas aggressive anaplastic thyroid cancer is treated with chemotherapy alongside radiation and targeted agents."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy for anaplastic disease: the high mutational burden and immune infiltrate of anaplastic thyroid cancer make PD-1 inhibitors like pembrolizumab active, increasingly combined with BRAF/MEK-targeted therapy in this rapidly fatal tumour."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Follicular cancer seeds bone: follicular thyroid carcinoma characteristically spreads to bone as osteolytic metastases that take up radioiodine, allowing both imaging detection and radioiodine treatment of the skeletal deposits."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Shared targetable fusions: RET, NTRK and BRAF alterations drive both thyroid cancer and non-small-cell lung cancer, so selpercatinib, larotrectinib and dabrafenib cross over between the two—one druggable lesion, two organs."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "A BRAF V600E partnership: papillary thyroid cancer and melanoma both frequently carry BRAF V600E, and the BRAF/MEK inhibitors developed for melanoma now treat BRAF-mutant (including anaplastic) thyroid cancer."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Follicular thyroid cancer reaches the lung: differentiated thyroid cancers spread haematogenously to the lungs, seeding miliary or nodular deposits in the alveolar parenchyma that often still take up radioactive iodine for treatment."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Hashimoto's link: chronic lymphocytic thyroiditis fills the gland with germinal centres, both predisposing to papillary thyroid cancer and forming the soil from which primary thyroid lymphoma arises."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Lymphoma in the same gland: a rapidly enlarging thyroid mass in long-standing Hashimoto's thyroiditis is often a primary thyroid diffuse large B-cell lymphoma, not a carcinoma—a crucial distinction with a very different treatment."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "A late cost of cure: high cumulative radioactive-iodine doses for thyroid cancer slightly raise the risk of secondary leukaemias such as AML, a marrow consequence of the radioisotope that treats the thyroid tumour."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Surgical hypoparathyroidism: total thyroidectomy can inadvertently remove or devascularise the parathyroid glands, dropping PTH and causing hypocalcaemia—the commonest complication of thyroid cancer surgery."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Haematogenous spread: follicular and medullary thyroid cancers disseminate through the bloodstream to the liver, bone and lung, seeding the hepatic lobule unlike the lymph-node-spreading papillary type."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Two routes to arrhythmia: post-thyroidectomy hypocalcaemia prolongs the QT interval, while the long-term TSH-suppressive thyroxine used after surgery raises the risk of atrial fibrillation in the conduction system."
  - target: 01-human/03-molecular/alk
    relation: connects-to
    note: "Rare targetable fusion: ALK gene fusions are an uncommon but actionable driver in papillary and more aggressive thyroid cancers, treatable with ALK inhibitors."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Progression driver: PIK3CA mutation and amplification mark the progression of thyroid cancer toward poorly differentiated and anaplastic disease."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Anaplastic transformation: CDKN2A loss, releasing the cell-cycle brake, accompanies the dedifferentiation of thyroid cancer into its lethal anaplastic form."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: with CDKN2A loss in anaplastic disease, cyclin D1-CDK4/6 activity propels thyroid cancer cells through the G1 checkpoint."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Dedifferentiation oncogene: MYC activation drives the proliferation and dedifferentiation of poorly differentiated and anaplastic thyroid cancer."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in hypoxic thyroid tumours drives the VEGF angiogenesis and invasive phenotype of more aggressive disease."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Neuroendocrine imaging: medullary thyroid cancer expresses somatostatin receptor 2, enabling DOTATATE PET to stage disease and peptide-receptor radionuclide therapy in progressive metastatic cases."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Anaplastic dedifferentiation: EZH2 is upregulated in anaplastic thyroid cancer, where its epigenetic silencing of differentiation and tumour-suppressor genes drives the loss of thyroid identity and aggressive growth."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Tumour-associated macrophages: CCL2 recruits monocytes that become the dense macrophage infiltrate of papillary and especially anaplastic thyroid cancer, where high TAM density correlates with invasion and poor prognosis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Diagnostic marker: galectin-3 is strongly expressed in malignant thyroid follicular cells but not benign ones, making its immunohistochemistry a key adjunct for distinguishing papillary and follicular carcinoma from benign nodules on indeterminate biopsies."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Anaplastic dedifferentiation: aberrant Wnt/β-catenin activation accompanies the progression of differentiated thyroid cancer to anaplastic carcinoma, contributing to the loss of iodine-handling differentiation that makes anaplastic disease radioiodine-refractory."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Invasion and EMT: TGF-β drives the epithelial-mesenchymal transition that underlies extrathyroidal extension and nodal metastasis in papillary thyroid cancer, while also shaping the immunosuppressive stroma of aggressive tumours."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK convergence: the BRAF, RET and RAS lesions of thyroid cancer all converge on the MAPK cascade to activate ERK1/2, the central proliferative pathway targeted by BRAF/MEK inhibitors and exploited in redifferentiation therapy to restore iodine uptake."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K axis: PTEN loss — germline in the Cowden syndrome already mapped — activates the PI3K-AKT-mTOR pathway that drives follicular and anaplastic thyroid carcinoma, complementing the AKT and mTOR already mapped."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Differentiation control: NOTCH signalling governs thyroid follicular- and C-cell differentiation and is dysregulated in thyroid carcinoma, where restoring NOTCH activity can re-induce the differentiated, iodine-handling phenotype."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: the cyclin-D1-CDK4/6 axis (cyclin-D1 mapped, with CDKN2A loss in aggressive disease) releases E2F1 to drive thyroid-carcinoma proliferation."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "EMT and dedifferentiation: loss of E-cadherin during epithelial-mesenchymal transition promotes invasion and the dedifferentiation toward the aggressive, RAI-refractory anaplastic thyroid carcinoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Anaplastic transformation: MDM2-mediated suppression and outright TP53 mutation (p53 mapped) inactivate p53 in the progression to anaplastic thyroid carcinoma, removing its apoptotic and cell-cycle brake."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Dedifferentiation: dysregulation of the RB1-E2F checkpoint (CDKN2A, cyclin-D1 and E2F1 already mapped) accompanies the dedifferentiation of thyroid cancer toward the aggressive anaplastic phenotype."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammatory microenvironment: IL-6-JAK-STAT3 signalling (STAT3 already mapped) contributes to an inflammatory, pro-tumorigenic microenvironment in thyroid cancer."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Radioiodine resistance: NRF2 antioxidant signalling modulates the oxidative balance of thyroid follicular cells and contributes to resistance against radioiodine and oxidative therapy."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) drives EMT and dedifferentiation in the progression toward aggressive and anaplastic thyroid cancer."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of thyroid cancer, relevant to immunotherapy in anaplastic disease."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response and immune-evasion balance of thyroid cancer."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6 acting on the cyclin-D1-RB1 axis (both mapped) drives the cell-cycle entry that sustains proliferation in thyroid cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-mediated FOXO inactivation removes a pro-apoptotic, growth-restraining brake, favoring survival in thyroid cancer."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic granule killing by CD8 T and NK cells mediates immune clearance that thyroid cancer must evade."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and survival signaling of thyroid cancer."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory tumor microenvironment of thyroid cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling downstream of RET and receptor tyrosine kinases contributes to the invasion of thyroid cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of thyroid cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of thyroid cancer cells, including dedifferentiated forms."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of thyroid cancer."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of thyroid cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of thyroid cancer."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of thyroid cancer."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions and invasion of thyroid cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of thyroid cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of thyroid cancer."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Dedifferentiation and RAI-resistance: the AXL receptor tyrosine kinase is upregulated as thyroid cancers dedifferentiate and lose iodine uptake, driving the invasion and radioiodine-refractory phenotype that pushes treatment toward kinase inhibitors."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Female predominance: thyroid cancer is roughly threefold more common in women, and estrogen-receptor signalling promotes thyroid follicular-cell proliferation, a hormonal contribution to the sex bias in its incidence."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Anaplastic immunotherapy: antigen presentation via MHC class II shapes the T-cell response now targeted with checkpoint inhibitors in anaplastic thyroid cancer, and its loss contributes to immune escape in this most aggressive thyroid malignancy."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Anaplastic T-cell therapy: IL-2-driven T-cell expansion supports the immunotherapy of anaplastic thyroid cancer (MHC class II already mapped), combined with BRAF/MEK-targeted therapy in this rapidly lethal but sometimes immunoresponsive tumour."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "TKI cardiotoxicity: the multikinase and VEGFR inhibitors (lenvatinib, sorafenib; VEGF already mapped) used in radioactive-iodine-refractory thyroid cancer cause hypertension and cardiac events, and troponin elevation helps detect the resulting myocardial injury."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Checkpoint combination: CTLA-4 blockade, with PD-1 inhibition (already mapped), is being tested to deepen responses in anaplastic thyroid cancer, whose few but sometimes striking immunotherapy responses have prompted combination trials."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), part of the immune evasion that shapes the limited but occasionally striking immunotherapy responses of anaplastic thyroid cancer."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: the thyroid's active iodine and hydrogen-peroxide chemistry, with reactive oxygen species to which xanthine oxidase contributes, generates oxidative DNA damage (NRF2 already mapped) that contributes to thyroid carcinogenesis."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the highly vascular thyroid cancers, part of the biology targeted by the antiangiogenic multikinase inhibitors."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of thyroid cancer, especially the aggressive anaplastic type."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia and TKI therapy: the advanced thyroid cancers and the multikinase-inhibitor therapy cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-factor signalling: IGF-1 and its receptor drive the proliferation of thyroid cancer cells (VEGF and RET already mapped), part of the growth-factor signalling that supports the tumour alongside the driver kinases."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immune microenvironment of thyroid cancer."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and thyroid cancer: the adipokine leptin links obesity — a risk factor for differentiated thyroid cancer — to the proliferation of the tumour, part of its metabolic dimension."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine risk: adiponectin, with leptin (already mapped), links the obesity and metabolic state to the risk and biology of thyroid cancer, part of the adipokine influence on the tumour."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity risk of differentiated thyroid cancer."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and produces the anaemia of chronic disease of the advanced and anaplastic thyroid cancer."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Immunogenic signalling: type-I interferon, downstream of the cGAS-STING (already mapped) innate sensing, is relevant to the immunogenicity and the immunotherapy of the aggressive anaplastic thyroid cancer."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, exploited by the checkpoint (PD-1 already mapped) immunotherapy of anaplastic thyroid cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the thyroid-cancer immune microenvironment."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance of the thyroid cancer, complementing the T-cell (already mapped) immunity of the aggressive anaplastic subtype."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of thyroid cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of thyroid cancer (and the thyroiditis-associated background)."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the thyroid-cancer microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma promote the invasiveness and the angiogenesis (VEGF already mapped) of the papillary and anaplastic thyroid-cancer microenvironment."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the thyroiditis-associated background and the immune microenvironment of thyroid cancer."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Lymphocytic infiltrate: the B cells form the lymphocytic infiltrates and tertiary lymphoid structures of the thyroiditis-associated background of thyroid cancer."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Anti-thyroid antibodies: the plasma cells secrete the anti-thyroglobulin/anti-TPO antibodies (already mapped) of the Hashimoto-thyroiditis background associated with the papillary thyroid cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement: the complement C3 activation contributes to the inflammatory dimension of the thyroiditis-associated background and the immune microenvironment of thyroid cancer."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid (macrophage already mapped) recruitment into the thyroid-cancer stroma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Stromal alarmin: TSLP released from the thyroid-cancer stroma (fibroblast already mapped) activates mast cells (already mapped) and dendritic cells (already mapped), promoting the type-2 immunosuppressive microenvironment that blunts cytotoxic anti-tumour immunity."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell effector: histamine, released by the mast cells (already mapped) infiltrating the thyroid-cancer stroma, amplifies the type-2 immune bias and modulates angiogenesis (VEGF already mapped) in the thyroid-cancer microenvironment."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM invasion scaffold: periostin, an extracellular matrix glycoprotein, is upregulated in the thyroid-cancer stroma (fibroblast already mapped) and promotes the invasion and the epithelial-mesenchymal transition (TGF-β already mapped) of papillary and anaplastic thyroid cancer."
---

# Thyroid Cancer

## Overview

**Thyroid cancer** encompasses a spectrum of malignancies arising from follicular epithelial cells (papillary, follicular, Hürthle cell, anaplastic) or parafollicular C cells (medullary). The majority (~90%) are **well-differentiated thyroid cancers (DTC)** — papillary (PTC) and follicular (FTC) — with excellent prognosis: 10-year survival >95% for low-risk PTC. In sharp contrast, **anaplastic thyroid carcinoma (ATC)** is one of the most lethal solid tumors, with median OS of 3-7 months. The molecular landscape of each histotype is now well-characterized, enabling targeted therapy for advanced/refractory disease [^schlumberger-2015-lenvatinib].

**Epidemiology:**
- ~43,000 new cases/year in the United States; most common endocrine malignancy
- 3:1 female predominance (follicular-derived cancers); no sex predilection in MTC
- Incidence rising (largely due to detection of small papillary cancers on imaging)
- Risk factors: ionizing radiation (especially childhood cranial/neck RT), iodine deficiency (FTC), obesity (PTC), family history; MEN2 for MTC (RET germline)

**Histological classification:**

| Type | Frequency | Cell of origin | Molecular drivers | 10-yr survival |
|------|-----------|---------------|-------------------|----------------|
| Papillary (PTC) | ~80% | Follicular epithelium | BRAF V600E (~60%), RET/PTC fusions (~20%), RAS mutations (~10%) | >95% (intrathyroidal) |
| Follicular (FTC) | ~10% | Follicular epithelium | RAS mutations (~50%), PAX8-PPARγ fusion (~30%), PIK3CA/PTEN | ~85% |
| Hürthle cell | ~3% | Oncocytic follicular cell | mtDNA mutations, TERT, NF2 | ~75% |
| Medullary (MTC) | ~4% | C cell (calcitonin) | RET mutation (germline MEN2 ~25%; somatic ~40%), RAS | ~80% |
| Anaplastic (ATC) | ~2% | Dedifferentiated | BRAF V600E (~50%), TP53 (~70%), TERT, PIK3CA, NF1 | ~10% at 1 year |
| Poorly differentiated (PDTC) | ~1-2% | Follicular | TERT (~50%), BRAF, RAS, TP53 | ~50% at 5yr |

## Structure

### Thyroid gland architecture

**Follicular cells:**
- Cuboidal-to-columnar epithelial cells surrounding thyroid follicles containing colloid (thyroglobulin)
- Function: thyroglobulin synthesis → iodination → T3/T4 production → secretion (TSH-dependent)
- Express NIS (Na/I symporter) → iodide uptake → basis for radioiodine (RAI) therapy in DTC
- TSH receptor (TSHR) → cAMP → thyroglobulin synthesis and NIS expression → RAI uptake

**C cells (parafollicular cells):**
- Derived from neural crest; ~0.1% of thyroid cells
- Secrete calcitonin (serum calcitonin → MTC biomarker and monitoring tool)
- RET expression in normal C cells → GDNF-GFRα → C cell survival

### Molecular landscape by histotype

**Papillary thyroid carcinoma (PTC):**
- **BRAF V600E (~60%):** MAPK activation without RAS involvement; associated with aggressive features (extrathyroidal extension, lymph node metastasis), higher recurrence, and radioiodine refractoriness; standard BRAF+ PTC treated with RAI still unless refractory
- **RET/PTC fusions (~20%):** RET/PTC1 (CCDC6-RET), RET/PTC3 (NCOA4-RET); enriched in radiation-associated PTC; generally favorable prognosis; targetable with selpercatinib
- **RAS mutations (~10%):** NRAS Q61R/K most common; associated with less aggressive PTC; also seen in FTC
- **TERT promoter mutation:** C228T/C250T; associated with older age, larger tumor, and poor prognosis when co-occurring with BRAF V600E (BRAF + TERT co-mutation → significantly higher recurrence and mortality)
- **NTRKfusions (~1-2%):** NTRK1/3 fusions; targetable with larotrectinib/entrectinib

**Follicular thyroid carcinoma (FTC):**
- RAS mutations (NRAS Q61, HRAS Q61, KRAS): Common; FTC biologically distinct from PTC → hematogenous metastasis (bone, lung) > lymph node
- PAX8-PPARγ rearrangement (~30%): t(2;3) → fusion oncoprotein; dominant negative for PPARγ tumor suppressor; minimally invasive FTC with good prognosis
- PTEN/PIK3CA mutations: PI3K-AKT-mTOR pathway activation; associated with more aggressive FTC

**Anaplastic thyroid carcinoma (ATC):**
- Likely dedifferentiated from preexisting PTC (BRAF+ ATC) or FTC/PDTC (RAS+ ATC)
- BRAF V600E (~45-50%): targetable — the discovery that led to the first ATC targeted therapy approval [^subbiah-2018-atc-dabrafenib]
- TP53 mutation (~70%): loss of p53 checkpoint → rapid progression
- TERT promoter (~50%), PIK3CA (~20%), NF1 (~15%), CDKN2A deletion (~40%)
- Co-occurring with PTC/FTC elements in the same specimen → confirms dedifferentiation pathway

## Function

### Thyroid hormone biosynthesis and cancer biology

**Normal thyroid function:**
TSH → TSHR → adenylyl cyclase → cAMP → PKA → (1) NIS expression and thyroglobulin synthesis, (2) T3/T4 synthesis and secretion. Differentiated thyroid cancers partially retain this axis — the basis for TSH suppression (levothyroxine) and RAI therapy.

**Radioiodine (RAI) therapy mechanism:**
DTC cells retain NIS expression → concentrate iodine-131 → beta emission → DNA double-strand breaks → tumor cell death. RAI is effective in metastatic DTC with NIS expression. BRAF V600E → MAPK → transcriptional downregulation of NIS, pendrin, and thyroglobulin → RAI refractoriness. MEK inhibitors (selumetinib) can restore RAI uptake in BRAF-mutant DTC (ASTRA trial).

**TSH-driven growth:**
Elevated TSH → TSHR → proliferation of thyroid cancer cells; TSH suppression (levothyraxine to TSH <0.1 mU/L) slows DTC growth — a pillar of post-thyroidectomy management in high-risk DTC.

## Pathology

### Diagnosis and staging

**Initial workup:**
- Thyroid ultrasound: size, composition, calcifications, lymphadenopathy (ACR TI-RADS, ATA sonographic risk classification)
- Fine needle aspiration (FNA) biopsy: Bethesda system reporting (I-VI); Bethesda IV/V/VI → thyroidectomy; Bethesda III/IV → molecular testing (ThyroSeq, Afirma GSC) to guide surgery
- Serum calcitonin: screen for MTC before thyroid surgery; baseline monitoring post-thyroidectomy
- CEA: MTC marker; elevated CEA with normal calcitonin → aggressive dedifferentiated MTC
- Genetic testing: RET germline testing in all MTC patients; if positive → screen family members

**TNM staging (AJCC 8th edition):**
- All differentiated thyroid cancers: age ≥55 at diagnosis → more aggressive staging (reflects biology)
- PTC/FTC ≥55: pT3-T4/N1/M1 → stage III-IV; <55 → even M1 disease = stage II
- MTC: standard TNM; calcitonin doubling time predicts survival

**Surveillance post-thyroidectomy (DTC):**
- Stimulated thyroglobulin (sTg) + anti-Tg antibody: Biochemical disease detection
- RAI whole-body scan (post-remnant ablation): Anatomic disease localization
- Neck ultrasound at 6-12 months: structural recurrence
- Response-adapted follow-up: Excellent response (suppressed Tg undetectable, negative imaging) → decreasing surveillance intensity

### Treatment

**Differentiated thyroid cancer (DTC):**

*Surgery:*
- Total thyroidectomy for tumors >1 cm, bilateral, aggressive features, or prior neck RT
- Hemithyroidectomy for unifocal T1 tumors (<4 cm) with low-risk features
- Prophylactic central neck dissection in high-risk PTC (controversial)

*Radioiodine adjuvant therapy:*
- Post-thyroidectomy RAI ablation for remnant thyroid and residual cancer
- Indications: high-risk features (T3/T4, N1, M1, aggressive histology)
- Preparation: thyroid hormone withdrawal (TSH stimulation) or recombinant TSH (Thyrogen)
- Activity: 30-100 mCi for remnant ablation; 100-200 mCi for high-risk/metastatic DTC

*RAI-refractory DTC (systemic therapy):*
- **Lenvatinib (SELECT trial):** PFS 18.3 vs. 3.6 months vs. placebo; 65% ORR; FDA approved 2015 for RAI-refractory DTC [^schlumberger-2015-lenvatinib]
- **Sorafenib (DECISION trial):** PFS 10.8 vs. 5.8 months; 12% ORR; approved 2013 for RAI-refractory DTC
- **Lenvatinib + pembrolizumab (LEAP-018):** Under investigation

*Targeted therapy for molecular alterations:*
- RET fusion/mutation → selpercatinib or pralsetinib (LIBRETTO-001)
- NTRK fusion → larotrectinib or entrectinib (basket trials)
- BRAF V600E (non-ATC DTC refractory) → dabrafenib+trametinib or vemurafenib+cobimetinib

**Medullary thyroid carcinoma (MTC):**

*Surgery:*
- Total thyroidectomy + bilateral central neck dissection; lateral neck dissection if N1b
- MEN2B → prophylactic thyroidectomy in neonatal period
- Prophylactic adrenalectomy for pheochromocytoma before thyroid surgery (pheo must be treated first)

*Systemic therapy (advanced MTC):*
- **Vandetanib (ZETA trial):** PFS 30.5 vs. 19.3 months; ORR 45%; approved 2011 [^wells-2012-vandetanib reference — indirectly, via RET entry]
- **Cabozantinib (EXAM trial):** PFS 7.2 vs. 4.0 months; active after vandetanib
- **Selpercatinib (LIBRETTO-001):** ORR 69% in pretreated RET-mutant MTC; 73% treatment-naive; now preferred first-line selective option for RET-mutant MTC
- **Pralsetinib (ARROW trial):** ORR 60% pretreated; alternative to selpercatinib

*Calcitonin monitoring:*
Calcitonin doubling time <6 months → poor prognosis → early systemic therapy; CEA doubling time provides independent prognostic information

**Anaplastic thyroid carcinoma (ATC):**
- **BRAF V600E (~50% of ATC):** Dabrafenib (BRAF inhibitor) + trametinib (MEK inhibitor); ORR 69%; 1-year OS 80% in BRAF+ ATC vs. historical ~5%; FDA approved 2018 [^subbiah-2018-atc-dabrafenib]
- **BRAF wild-type ATC:** No targeted therapy; may use pembrolizumab ± lenvatinib; clinical trial strongly recommended
- Multimodal approach: surgery (if feasible) + RT + systemic therapy; IMRT for unresectable local disease
- Immunotherapy: Pembrolizumab alone (~12% ORR in ATC); higher responses in combination

## Connections

- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E in ~60% of papillary thyroid carcinoma → ERK activation → dedifferentiation → radioiodine resistance; dabrafenib+trametinib approved for BRAF V600E-mutant ATC (2018, first targeted therapy for ATC); vemurafenib+cobimetinib in radioiodine-refractory DTC under study.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Differentiated thyroid cancer is highly vascular; VEGF and VEGFR2 overexpressed in PTC and FTC → promotes metastasis; lenvatinib (multikinase: VEGFR1-3, RET, FGFR, PDGFRβ) approved for RAI-refractory DTC; sorafenib (VEGFR2/3 + BRAF + RET) also approved for RAI-refractory DTC.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PTEN loss and PIK3CA mutations activate mTOR in follicular thyroid carcinoma and ATC; everolimus (mTORC1 inhibitor) studied in RAI-refractory DTC; mTOR pathway activation mediates resistance to VEGFR-targeted TKIs (lenvatinib, sorafenib) in DTC → mTOR combination strategies.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-L1 expressed in ~30-50% of papillary and ~50-70% of anaplastic thyroid carcinoma → T cell exclusion; pembrolizumab studied with lenvatinib for RAI-refractory DTC and ATC; spartalizumab + dabrafenib+trametinib in BRAF+ ATC; anti-PD-1 active in radioiodine-refractory DTC.
- `connects-to` → **[RET](../../03-molecular/ret/README.md)** — RET drives the C-cell lineage of thyroid cancer: germline RET mutations cause MEN2 medullary thyroid carcinoma, somatic RET ~40% of sporadic MTC, and RET/PTC fusions ~20% of papillary cancer; selective RET inhibitors selpercatinib and pralsetinib are highly active.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Differentiated thyroid cancers retain the sodium-iodide symporter (NIS), letting them concentrate radioiodine (I-131) whose beta emission ablates tumor — a targeted therapy; BRAF V600E silences NIS, causing radioiodine refractoriness that MEK inhibitors can partly reverse.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Medullary thyroid carcinoma arises from calcitonin-secreting C cells, so serum calcitonin (and CEA) is both a screen before thyroid surgery and the key tumor marker afterward; a calcitonin doubling time under 6 months signals aggressive disease and prompts early systemic therapy.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Medullary thyroid carcinoma is a neuroendocrine tumor: it arises from calcitonin-secreting parafollicular C cells (neural-crest-derived), not iodine-handling follicular cells, so it ignores radioiodine and is tracked by calcitonin/CEA — closer to other NETs than papillary cancer.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — FAP confers a distinctive thyroid risk: cribriform-morular thyroid carcinoma, a rare papillary variant occurring almost exclusively in young women with germline APC mutations, can be the presenting sign of undiagnosed FAP — prompting colonoscopy and APC testing.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunotherapy is reshaping the worst thyroid cancers: anaplastic and radioiodine-refractory tumors express PD-L1 and exclude cytotoxic T cells, so anti-PD-1 (pembrolizumab), often with lenvatinib or BRAF/MEK inhibitors, reactivates CD8+ killing in these rapidly fatal cancers.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Medullary thyroid carcinoma and pheochromocytoma are the linked tumors of MEN2: a germline RET mutation drives both, so a patient with medullary thyroid cancer must be screened for pheochromocytoma before any surgery to avoid an intraoperative hypertensive crisis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Thyroid cancer is the commonest endocrine malignancy: most are differentiated (papillary/follicular) tumors of iodine-avid follicular cells curable with surgery and radioiodine, while medullary (C-cell, calcitonin) and anaplastic types behave very differently.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Cowden syndrome is a hereditary cause of thyroid cancer: germline PTEN loss unleashes PI3K/mTOR signaling, predisposing to follicular thyroid carcinoma alongside breast and endometrial cancer, so multinodular goiter in a Cowden patient warrants close thyroid surveillance.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Thyroid cancer arises within the thyroid gland and exploits its physiology: most are differentiated tumors that still take up iodine and respond to TSH, so thyroidectomy plus radioiodine and TSH suppression treat it through the gland's own biology.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiation has a dual relationship with thyroid cancer: childhood external radiation is a leading cause of papillary thyroid cancer, yet radioactive iodine is a treatment mainstay, and external photon radiotherapy is reserved for anaplastic or unresectable disease.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — Thyroid cancer and head and neck squamous cancer are the two main neck malignancies: thyroid cancer is a usually indolent endocrine tumor curable with surgery and radioiodine, while HNSCC is an aggressive smoking/HPV-driven mucosal carcinoma—neck radiation links them.
- `connects-to` → **[Thyroid Hormones (T3/T4)](../../03-molecular/thyroid-hormones/README.md)** — Differentiated thyroid cancer keeps the gland's hormone machinery, enabling unique therapy: it still takes up iodine and responds to TSH, so radioactive iodine ablates residual tumor and thyroid-hormone (TSH suppression) therapy starves it—treatment exploiting normal physiology.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Papillary thyroid cancer spreads through the lymphatic system: it characteristically metastasizes to cervical lymph nodes (often the presenting sign) yet remains highly curable, so nodal spread shapes surgery but, unusually for cancer, rarely dooms the patient.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Follicular thyroid cancer spreads hematogenously to the lung and bone: unlike papillary's nodal route, it invades blood vessels to seed distant organs—so the lung is a classic metastatic site, treatable with radioactive iodine if the deposits still take up iodine.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune system frames several thyroid cancers: chronic Hashimoto's autoimmune thyroiditis predisposes to papillary cancer and primary thyroid lymphoma, while checkpoint inhibitors are tried in aggressive anaplastic disease that resists radioiodine.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Bone metastases make thyroid cancer a musculoskeletal disease too: spinal and pelvic deposits cause pathological fractures, cord compression, and pain, so management adds bisphosphonates, surgery, and targeted radiotherapy beyond radioiodine to protect the skeleton.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — Thyroid tumors sit within inherited endocrine neoplasia: medullary thyroid cancer defines MEN2 via RET, and although MEN1 centers on parathyroid, pituitary, and pancreas, both syndromes prompt the familial work-up any endocrine tumor demands.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutations mark dangerous thyroid cancer: reactivating telomerase, they predict aggressive behavior and—combined with BRAF—drive the dedifferentiation toward lethal anaplastic thyroid cancer, refining prognosis beyond histology alone.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — A subset of thyroid cancers is driven by NTRK fusions: these rearrangements, more common in radiation-exposed and pediatric tumors, are targetable with TRK inhibitors like larotrectinib—so molecular testing finds patients beyond the usual BRAF and RET.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Aggressive thyroid cancers fill with tumor-associated macrophages: especially in anaplastic disease, these immune cells dominate the stroma and promote invasion and immune escape, a microenvironment feature tied to poor prognosis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — The thyroid runs on selenium, and so does its cancer biology: selenium-dependent enzymes activate thyroid hormone and shield thyrocytes from the hydrogen peroxide of hormone synthesis, so selenium status influences thyroid disease and oxidative damage.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Thyroid cancer turns lethal when it loses p53: TP53 mutation drives the leap from a usually-curable differentiated cancer to anaplastic thyroid carcinoma, one of the most aggressive human tumors—explaining the dedifferentiation step.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Thyroid cancer shelters in a regulatory T-cell-rich niche: Tregs infiltrate aggressive and anaplastic tumors and suppress immunity, a barrier the checkpoint immunotherapy now tried in advanced thyroid cancer must overcome.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Medullary thyroid cancer is a tumor of the calcium thermostat: it arises from the C cells that make calcitonin, so the hormone serves as its tumor marker, and its calcium-regulating lineage defines this distinct, often inherited subtype.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells shape immunotherapy for aggressive thyroid cancer: as antigen-presenters they prime the T-cell response that checkpoint drugs amplify in anaplastic disease, and their dysfunction helps the tumor evade immunity.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Thyroid cancer can spread to the brain: though usually indolent, advanced or anaplastic disease seeds brain metastases through the blood, a sign of aggressive spread that shifts care toward systemic and targeted therapy.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Thyroid cancer can spread to the liver: medullary and advanced or anaplastic disease seed hepatic metastases, extending beyond the usual neck nodes, lung, and bone.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Papillary thyroid cancer recruits fibroblasts: cancer-associated fibroblasts build a desmoplastic stroma around the tumor, the firm scarring that helps it invade and trap calcifications.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Papillary thyroid cancer leaves calcium-phosphate fingerprints: its psammoma bodies are concentric calcium-phosphate calcifications, a histologic clue that also shows as microcalcifications on ultrasound.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy sharpens the diagnosis: it confirms papillary cancer's irregular nuclei with cytoplasm-filled pseudoinclusions and grooves, and reveals the dense-core neurosecretory granules that mark the medullary type as neuroendocrine.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — The sodium-iodide symporter is thyroid cancer's Achilles' heel: well-differentiated tumors keep this pump that hauls iodine into the cell on a sodium gradient, so radioactive iodine slips in to image and irradiate the cancer wherever it has spread.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Follicular thyroid cancer travels in the blood to bone: unlike the papillary type that creeps through lymph nodes, it spreads hematogenously, seeding lytic deposits in the marrow-filled bones of the spine, pelvis, and skull.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The voice hangs on a nerve beside the gland: the recurrent laryngeal nerve runs along the thyroid, so tumor invasion or surgical injury paralyzes a vocal cord, leaving the hoarseness that can be the first sign of an aggressive thyroid cancer.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Treatment puts the heart under strain: the multikinase inhibitors (lenvatinib, sorafenib) used for radioiodine-refractory disease drive hypertension and cardiac dysfunction, while the deliberate TSH-suppressing thyroid hormone dose risks atrial fibrillation.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Keeping the cancer quiet thins the bones: the long-term high-dose thyroid hormone given to suppress TSH after thyroidectomy pushes the body toward a subclinical hyperthyroidism that accelerates bone loss and osteoporosis, especially in older women.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both monitor and identify the tumor: serum thyroglobulin, measured by immunoassay, is the surveillance marker for recurrence (confounded by anti-thyroglobulin antibodies), while TTF-1, thyroglobulin, and calcitonin stains type a tumor on biopsy.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Thyroid cancer strikes women in their fertile years: it is far more common in young women, and radioactive-iodine therapy temporarily impairs fertility and demands contraception, so reproductive planning is woven into treatment.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Advanced therapy taxes the marrow: the multikinase inhibitors for radioiodine-refractory disease and the chemotherapy for anaplastic thyroid cancer suppress the blood counts, dropping neutrophils and raising the risk of infection.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Follicular thyroid cancer leans on PI3K-AKT: PIK3CA mutation or PTEN loss — the latter underlying Cowden-related thyroid tumors — drives this axis, distinct from the BRAF/RAS-MAPK route of papillary cancer and a target in dedifferentiated disease.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Differentiated thyroid cancer favors bone: follicular and papillary tumors seed osteolytic metastases that recruit osteoclasts to resorb bone, and the lifelong TSH-suppressing thyroxine adds its own push toward bone loss.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Its drugs and isotopes pass through the kidney: radioactive iodine is cleared renally, and the multikinase inhibitors for advanced disease cause hypertension and proteinuria, so kidney function shapes both treatments.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — A second oncogene family sorts the subtypes: where BRAF drives most papillary cancers, RAS mutations like KRAS underlie follicular thyroid cancer, a molecular split that increasingly guides diagnosis and targeted treatment.
- `connects-to` → **[Obesity](../obesity/README.md)** — Excess weight raises the risk: obesity is a consistent risk factor for thyroid cancer, contributing through insulin resistance, chronic inflammation and hormonal changes to the steep rise in its incidence.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Its treatment targets the blood supply: differentiated thyroid cancers are vascular, so the multikinase inhibitors lenvatinib and sorafenib work largely by blocking VEGF receptors on endothelial cells to choke off new vessels.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 helps the aggressive forms grow: anaplastic and advanced thyroid cancers show STAT3 activation that supports proliferation and immune evasion, a pathway studied as a target where BRAF and kinase inhibitors fall short.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB drives the deadliest variant: anaplastic thyroid carcinoma relies heavily on NF-κB signaling for its rapid, invasive growth, making the pathway a candidate target in a cancer that otherwise resists therapy.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Advanced disease raises the clot risk: like other solid cancers, progressive thyroid cancer carries tumor-driven hypercoagulability, and the antiangiogenic kinase inhibitors used to treat it add their own thrombotic and bleeding hazards.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Its targeted drugs spike the pressure: the VEGF-pathway kinase inhibitors lenvatinib and sorafenib used for RAI-refractory thyroid cancer cause prominent hypertension, an on-target vascular effect needing active management.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Antiangiogenic therapy injures the kidney: the same VEGF-targeted inhibitors used in advanced thyroid cancer cause proteinuria and glomerular injury that can progress to chronic kidney disease over prolonged treatment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Advanced disease and its therapy lower the count: progressive metastatic thyroid cancer with its inflammatory burden, compounded by kinase-inhibitor toxicity, can produce an anemia of chronic disease in the minority with aggressive disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — TSH-suppression and kinase inhibitors strain the heart: the lifelong thyroxine used to suppress TSH keeps patients mildly thyrotoxic, risking atrial fibrillation, while lenvatinib and sorafenib raise blood pressure and are cardiotoxic — all routes toward heart failure.
- `connects-to` → **[Stroke](../stroke/README.md)** — Long-term TSH-suppression can throw clots to the brain: the subclinical hyperthyroidism from suppressive thyroxine promotes atrial fibrillation, and the resulting cardioembolism raises the risk of ischemic stroke.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Cancer and altered thyroid hormone unsettle mood: the diagnosis plus the deliberately abnormal thyroid-hormone levels of suppression therapy and post-thyroidectomy state contribute to depression and impaired quality of life in survivors.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Thyroidectomy and anti-angiogenic drugs heal slowly: total thyroidectomy leaves a neck wound at risk to the recurrent laryngeal nerve and parathyroids, and the multikinase inhibitors for refractory disease impair wound healing.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Some thyroid cancers churn the gut: medullary thyroid cancer secretes calcitonin that causes secretory diarrhoea, and the multikinase inhibitors used for advanced disease commonly cause diarrhoea too.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong recurrence monitoring breeds worry: the thyroglobulin checks, neck ultrasounds and scan-anxiety of thyroid-cancer surveillance foster chronic health anxiety even in this often indolent cancer.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It invades the airway and spreads to the lungs: locally advanced thyroid cancer can infiltrate the trachea causing airway compromise, and differentiated thyroid cancer metastasises to the lungs.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Surgery threatens the voice and the nerves: thyroidectomy risks recurrent laryngeal nerve injury with hoarseness, and the resulting hypoparathyroidism causes hypocalcaemic tetany and paraesthesiae.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Aggressive disease reaches the skin: anaplastic thyroid cancer invades the overlying neck skin, and the radioiodine and surgery used for thyroid cancer leave their own cutaneous and scar effects.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its hormone-suppression and targeted drugs strain the heart: long-term TSH-suppressive levothyroxine can cause atrial fibrillation, and multikinase inhibitors like lenvatinib cause hypertension and QT prolongation.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its targeted drugs reach the kidney: the multikinase inhibitors used for advanced thyroid cancer cause proteinuria and hypertension that affect renal function.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — It travels with breast cancer: thyroid and breast cancer co-occur more often than chance, so survivors of one carry a modestly raised risk of the other.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It is treated by isotope and kinase drugs: radioactive iodine ablates differentiated thyroid cancer, while multikinase and RET-specific inhibitors (selpercatinib) treat advanced and medullary disease.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — A fellow thyroid-tumour syndrome: Carney complex predisposes to thyroid adenomas and carcinoma, joining the inherited syndromes that raise thyroid-cancer risk.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — It runs in DICER1 families: DICER1 syndrome predisposes to differentiated thyroid carcinoma and multinodular goitre from childhood, part of inherited thyroid-cancer surveillance.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Mostly chemoresistant except anaplastic: differentiated thyroid cancer responds poorly to cytotoxic chemotherapy, relying on surgery and radioiodine, whereas aggressive anaplastic thyroid cancer is treated with chemotherapy alongside radiation and targeted agents.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy for anaplastic disease: the high mutational burden and immune infiltrate of anaplastic thyroid cancer make PD-1 inhibitors like pembrolizumab active, increasingly combined with BRAF/MEK-targeted therapy in this rapidly fatal tumour.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Follicular cancer seeds bone: follicular thyroid carcinoma characteristically spreads to bone as osteolytic metastases that take up radioiodine, allowing both imaging detection and radioiodine treatment of the skeletal deposits.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Shared targetable fusions: RET, NTRK and BRAF alterations drive both thyroid cancer and non-small-cell lung cancer, so selpercatinib, larotrectinib and dabrafenib cross over between the two—one druggable lesion, two organs.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — A BRAF V600E partnership: papillary thyroid cancer and melanoma both frequently carry BRAF V600E, and the BRAF/MEK inhibitors developed for melanoma now treat BRAF-mutant (including anaplastic) thyroid cancer.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Follicular thyroid cancer reaches the lung: differentiated thyroid cancers spread haematogenously to the lungs, seeding miliary or nodular deposits in the alveolar parenchyma that often still take up radioactive iodine for treatment.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Hashimoto's link: chronic lymphocytic thyroiditis fills the gland with germinal centres, both predisposing to papillary thyroid cancer and forming the soil from which primary thyroid lymphoma arises.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Lymphoma in the same gland: a rapidly enlarging thyroid mass in long-standing Hashimoto's thyroiditis is often a primary thyroid diffuse large B-cell lymphoma, not a carcinoma—a crucial distinction with a very different treatment.
- `connects-to` → **[AML](../aml/README.md)** — A late cost of cure: high cumulative radioactive-iodine doses for thyroid cancer slightly raise the risk of secondary leukaemias such as AML, a marrow consequence of the radioisotope that treats the thyroid tumour.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Surgical hypoparathyroidism: total thyroidectomy can inadvertently remove or devascularise the parathyroid glands, dropping PTH and causing hypocalcaemia—the commonest complication of thyroid cancer surgery.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Haematogenous spread: follicular and medullary thyroid cancers disseminate through the bloodstream to the liver, bone and lung, seeding the hepatic lobule unlike the lymph-node-spreading papillary type.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Two routes to arrhythmia: post-thyroidectomy hypocalcaemia prolongs the QT interval, while the long-term TSH-suppressive thyroxine used after surgery raises the risk of atrial fibrillation in the conduction system.
- `connects-to` → **[ALK](../../03-molecular/alk/README.md)** — Rare targetable fusion: ALK gene fusions are an uncommon but actionable driver in papillary and more aggressive thyroid cancers, treatable with ALK inhibitors.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Progression driver: PIK3CA mutation and amplification mark the progression of thyroid cancer toward poorly differentiated and anaplastic disease.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Anaplastic transformation: CDKN2A loss, releasing the cell-cycle brake, accompanies the dedifferentiation of thyroid cancer into its lethal anaplastic form.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: with CDKN2A loss in anaplastic disease, cyclin D1-CDK4/6 activity propels thyroid cancer cells through the G1 checkpoint.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Dedifferentiation oncogene: MYC activation drives the proliferation and dedifferentiation of poorly differentiated and anaplastic thyroid cancer.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in hypoxic thyroid tumours drives the VEGF angiogenesis and invasive phenotype of more aggressive disease.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — Medullary thyroid cancer expresses somatostatin receptor 2, enabling DOTATATE PET to stage disease and peptide-receptor radionuclide therapy in progressive metastatic cases not controlled by RET-targeted kinase inhibitors.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2 is upregulated in anaplastic thyroid cancer, where its epigenetic silencing of differentiation and tumor-suppressor genes drives the loss of thyroid identity—including the sodium-iodide symporter—and the explosive growth that makes anaplastic disease nearly uniformly fatal.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits monocytes that become the dense macrophage infiltrate of papillary and especially anaplastic thyroid cancer, where high tumor-associated-macrophage density correlates with extrathyroidal invasion and poor prognosis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is strongly expressed in malignant thyroid follicular cells but not benign ones, making its immunohistochemistry a key adjunct for distinguishing papillary and follicular carcinoma from benign nodules on indeterminate biopsies.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Aberrant Wnt/β-catenin activation accompanies the progression of differentiated thyroid cancer to anaplastic carcinoma, contributing to the loss of iodine-handling differentiation that makes anaplastic disease radioiodine-refractory.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β drives the epithelial-mesenchymal transition that underlies extrathyroidal extension and nodal metastasis in papillary thyroid cancer, while also shaping the immunosuppressive stroma of aggressive tumors.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — The BRAF, RET and RAS lesions of thyroid cancer all converge on the MAPK cascade to activate ERK1/2, the central proliferative pathway targeted by BRAF/MEK inhibitors and exploited in redifferentiation therapy to restore iodine uptake.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss—germline in the Cowden syndrome already mapped—activates the PI3K-AKT-mTOR pathway that drives follicular and anaplastic thyroid carcinoma, complementing the AKT and mTOR already mapped.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling governs thyroid follicular- and C-cell differentiation and is dysregulated in thyroid carcinoma, where restoring NOTCH activity can re-induce the differentiated, iodine-handling phenotype.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D1-CDK4/6 axis (cyclin-D1 mapped, with CDKN2A loss in aggressive disease) releases E2F1 to drive thyroid-carcinoma proliferation.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Loss of E-cadherin during epithelial-mesenchymal transition promotes invasion and the dedifferentiation toward the aggressive, RAI-refractory anaplastic thyroid carcinoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated suppression and outright TP53 mutation (p53 mapped) inactivate p53 in the progression to anaplastic thyroid carcinoma, removing its apoptotic and cell-cycle brake.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (CDKN2A, cyclin-D1 and E2F1 already mapped) accompanies the dedifferentiation of thyroid cancer toward the aggressive anaplastic phenotype.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (STAT3 already mapped) contributes to an inflammatory, pro-tumorigenic microenvironment in thyroid cancer.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling modulates the oxidative balance of thyroid follicular cells and contributes to resistance against radioiodine and oxidative therapy.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) drives EMT and dedifferentiation in the progression toward aggressive and anaplastic thyroid cancer.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of thyroid cancer, relevant to immunotherapy in anaplastic disease.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response and immune-evasion balance of thyroid cancer.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6 acting on the cyclin-D1-RB1 axis (both mapped) drives the cell-cycle entry that sustains proliferation in thyroid cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-mediated FOXO inactivation removes a pro-apoptotic, growth-restraining brake, favoring survival in thyroid cancer.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic granule killing by CD8 T and NK cells mediates immune clearance that thyroid cancer must evade.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and survival signaling of thyroid cancer.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory tumor microenvironment of thyroid cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling downstream of RET and receptor tyrosine kinases contributes to the invasion of thyroid cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of thyroid cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of thyroid cancer cells, including dedifferentiated forms.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of thyroid cancer.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of thyroid cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of thyroid cancer.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of thyroid cancer.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions and invasion of thyroid cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of thyroid cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of thyroid cancer.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Dedifferentiation and RAI-resistance: the AXL receptor tyrosine kinase is upregulated as thyroid cancers dedifferentiate and lose iodine uptake, driving the invasion and radioiodine-refractory phenotype that pushes treatment toward kinase inhibitors.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Female predominance: thyroid cancer is roughly threefold more common in women, and estrogen-receptor signalling promotes thyroid follicular-cell proliferation, a hormonal contribution to the sex bias in its incidence.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Anaplastic immunotherapy: antigen presentation via MHC class II shapes the T-cell response now targeted with checkpoint inhibitors in anaplastic thyroid cancer, and its loss contributes to immune escape in this most aggressive thyroid malignancy.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Anaplastic T-cell therapy: IL-2-driven T-cell expansion supports the immunotherapy of anaplastic thyroid cancer (MHC class II already mapped), combined with BRAF/MEK-targeted therapy in this rapidly lethal but sometimes immunoresponsive tumour.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — TKI cardiotoxicity: the multikinase and VEGFR inhibitors (lenvatinib, sorafenib; VEGF already mapped) used in radioactive-iodine-refractory thyroid cancer cause hypertension and cardiac events, and troponin elevation helps detect the resulting myocardial injury.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Checkpoint combination: CTLA-4 blockade, with PD-1 inhibition (already mapped), is being tested to deepen responses in anaplastic thyroid cancer, whose few but sometimes striking immunotherapy responses have prompted combination trials.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), part of the immune evasion that shapes the limited but occasionally striking immunotherapy responses of anaplastic thyroid cancer.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: the thyroid's active iodine and hydrogen-peroxide chemistry, with reactive oxygen species to which xanthine oxidase contributes, generates oxidative DNA damage (NRF2 already mapped) that contributes to thyroid carcinogenesis.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the highly vascular thyroid cancers, part of the biology targeted by the antiangiogenic multikinase inhibitors.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of thyroid cancer, especially the aggressive anaplastic type.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia and TKI therapy: the advanced thyroid cancers and the multikinase-inhibitor therapy cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Growth-factor signalling: IGF-1 and its receptor drive the proliferation of thyroid cancer cells (VEGF and RET already mapped), part of the growth-factor signalling that supports the tumour alongside the driver kinases.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immune microenvironment of thyroid cancer.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and thyroid cancer: the adipokine leptin links obesity — a risk factor for differentiated thyroid cancer — to the proliferation of the tumour, part of its metabolic dimension.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine risk: adiponectin, with leptin (already mapped), links the obesity and metabolic state to the risk and biology of thyroid cancer, part of the adipokine influence on the tumour.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity risk of differentiated thyroid cancer.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and produces the anaemia of chronic disease of the advanced and anaplastic thyroid cancer.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Immunogenic signalling: type-I interferon, downstream of the cGAS-STING (already mapped) innate sensing, is relevant to the immunogenicity and the immunotherapy of the aggressive anaplastic thyroid cancer.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, exploited by the checkpoint (PD-1 already mapped) immunotherapy of anaplastic thyroid cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the thyroid-cancer immune microenvironment.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — NK surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance of the thyroid cancer, complementing the T-cell (already mapped) immunity of the aggressive anaplastic subtype.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of thyroid cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of thyroid cancer (and the thyroiditis-associated background).
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the thyroid-cancer microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma promote the invasiveness and the angiogenesis (VEGF already mapped) of the papillary and anaplastic thyroid-cancer microenvironment.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the thyroiditis-associated background and the immune microenvironment of thyroid cancer.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Lymphocytic infiltrate: the B cells form the lymphocytic infiltrates and tertiary lymphoid structures of the thyroiditis-associated background of thyroid cancer.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Anti-thyroid antibodies: the plasma cells secrete the anti-thyroglobulin/anti-TPO antibodies (already mapped) of the Hashimoto-thyroiditis background associated with the papillary thyroid cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement: the complement C3 activation contributes to the inflammatory dimension of the thyroiditis-associated background and the immune microenvironment of thyroid cancer.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid (macrophage already mapped) recruitment into the thyroid-cancer stroma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Stromal alarmin: TSLP released from the thyroid-cancer stroma (fibroblast already mapped) activates mast cells (already mapped) and dendritic cells (already mapped), promoting the type-2 immunosuppressive microenvironment that blunts cytotoxic anti-tumour immunity.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell effector: histamine, released by the mast cells (already mapped) infiltrating the thyroid-cancer stroma, amplifies the type-2 immune bias and modulates angiogenesis (VEGF already mapped) in the thyroid-cancer microenvironment.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM invasion scaffold: periostin, an extracellular matrix glycoprotein, is upregulated in the thyroid-cancer stroma (fibroblast already mapped) and promotes the invasion and the epithelial-mesenchymal transition (TGF-β already mapped) of papillary and anaplastic thyroid cancer.

[^schlumberger-2015-lenvatinib]: Schlumberger M, Tahara M, Wirth LJ, et al. Lenvatinib versus placebo in radioiodine-refractory differentiated thyroid cancer. *N Engl J Med.* 2015;372(7):621-630. [doi:10.1056/NEJMoa1406470](https://doi.org/10.1056/NEJMoa1406470) · [PubMed 25671254](https://pubmed.ncbi.nlm.nih.gov/25671254/)
[^subbiah-2018-atc-dabrafenib]: Subbiah V, Kreitman RJ, Wainberg ZA, et al. Dabrafenib and trametinib treatment in patients with locally advanced or metastatic BRAF V600-mutant anaplastic thyroid cancer. *J Clin Oncol.* 2018;36(1):7-13. [doi:10.1200/JCO.2017.73.6785](https://doi.org/10.1200/JCO.2017.73.6785) · [PubMed 28892432](https://pubmed.ncbi.nlm.nih.gov/28892432/)
