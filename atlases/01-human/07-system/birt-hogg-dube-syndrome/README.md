---
schema: human-scale-entry/v1
id: birt-hogg-dube-syndrome
name: Birt-Hogg-Dubé Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Birt-Hogg-Dubé syndrome (BHD) is caused by germline FLCN mutations; fibrofolliculomas (skin), pulmonary cysts (pneumothorax risk 7×), bilateral multifocal chromophobe/hybrid oncocytic RCC (~30% lifetime); nephron-sparing surveillance surgery; mTOR inhibitors explored."
aliases: ["BHD", "Birt-Hogg-Dubé syndrome", "Birt-Hogg-Dube", "FLCN syndrome", "BHD syndrome", "chromophobe RCC hereditary", "fibrofolliculoma syndrome", "BHD RCC", "BHD pneumothorax", "BHD kidney cancer"]
sources:
  - id: nickerson-2002-flcn-bhd
    type: peer-reviewed
    cite: "Nickerson ML, Warren MB, Toro JR, et al. Mutations in a novel gene lead to kidney tumors, lung wall defects, and benign tumors of the hair follicle in patients with the Birt-Hogg-Dubé syndrome. Cancer Cell. 2002;2(2):157-164."
    doi: "10.1016/s1535-6108(02)00104-6"
    pmid: "12204536"
    url: "https://doi.org/10.1016/s1535-6108(02)00104-6"
  - id: tsun-2013-flcn-rag
    type: peer-reviewed
    cite: "Tsun ZY, Bar-Peled L, Chantranupong L, et al. The folliculin tumor suppressor is a GAP for the RagC/D GTPases that signal amino acid levels to mTORC1. Mol Cell. 2013;52(4):495-505."
    doi: "10.1016/j.molcel.2013.09.016"
    pmid: "24095279"
    url: "https://doi.org/10.1016/j.molcel.2013.09.016"
cross_links:
  - target: 01-human/03-molecular/flcn
    relation: connects-to
    note: "Germline FLCN truncating mutations cause BHD; FLCN is a GAP for RagC/D (amino acid sensing for mTORC1); biallelic FLCN LOF in each BHD tumor (second hit LOH at 17p11.2); somatic FLCN in sporadic chromophobe RCC (~20-25%)"
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "FLCN LOF → Rag GTPase dysregulation → impaired mTORC1 lysosomal docking (RagC/D-GAP activity lost); mTOR inhibitors (everolimus) explored in BHD-associated RCC; FLCN LOF mTOR biology distinct from TSC1/TSC2 LOF (Rheb pathway) but both converge on mTORC1"
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "BHD-associated RCC (chromophobe) vs VHL-associated RCC (clear cell): distinct histology and molecular drivers; VHL → HIF-1α pseudohypoxia; FLCN → mTOR/Rag dysregulation; BHD chromophobe has better prognosis than VHL ccRCC; belzutifan for VHL (not yet BHD)"
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "BHD lifetime RCC risk ~15-30%; chromophobe + hybrid oncocytic histology; bilateral multifocal; annual MRI from age 20; nephron-sparing surgery when >3 cm; sunitinib/cabozantinib for metastatic BHD RCC; chromophobe RCC 5-year OS ~88%"
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "BHD causes bilateral basal pulmonary cysts in ~80-90% of carriers → 7× increased spontaneous pneumothorax risk; FLCN-deficient alveolar type II cells → mTOR dysregulation → cyst formation; pleurodesis recommended after second ipsilateral or first contralateral pneumothorax."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Fibrofolliculomas (hair follicle hamartomas; white facial papules) are the defining BHD skin lesion; ≥5 histologically confirmed fibrofolliculomas is a major diagnostic criterion; cosmetic laser/dermabrasion reduces lesions; topical sirolimus (off-label) may reduce formation."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "FLCN-FNIP1/2 interacts with AMPK; FNIP1/2 are AMPK-associated proteins; AMPK phosphorylates FLCN at Ser302; FLCN-FNIP-AMPK is a metabolic sensing hub at the lysosome integrating energy status with mTORC1 activity; FNIP1 null mice develop cardiomegaly and lymphoma."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Birt-Hogg-Dubé and Cowden syndrome are mTORopathies: BHD loses folliculin (a GAP for the RagC/D GTPases that gate mTORC1) while Cowden loses PTEN (which restrains PI3K-AKT-mTOR), and both cause facial hamartomatous skin papules and a heightened risk of renal cell carcinoma."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "The lung cysts of Birt-Hogg-Dubé arise in alveolar type II pneumocytes: folliculin loss dysregulates mTOR and TFE3, driving abnormal alveolar remodeling and matrix breakdown that thins the cyst walls — producing the basal subpleural cysts behind a 7-fold pneumothorax risk."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is BHD's malignant target: folliculin loss causes bilateral, multifocal chromophobe and hybrid oncocytic renal cell carcinoma (~15-30% lifetime), so carriers get annual MRI from their 20s and nephron-sparing surgery once a tumour reaches ~3 cm."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Birt-Hogg-Dubé and tuberous sclerosis converge on mTOR and cystic lung disease: BHD folliculin and TSC1/2 both normally restrain mTOR, and both cause characteristic lung cysts with pneumothorax risk (BHD basal cysts; TSC/LAM diffuse)—so mTOR inhibition is a shared theme."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "Birt-Hogg-Dubé and HLRCC are both hereditary kidney-cancer syndromes with distinct biology: BHD (folliculin) causes chromophobe/oncocytic RCC with skin fibrofolliculomas and lung cysts, while HLRCC (fumarate hydratase) causes aggressive papillary RCC and uterine leiomyomas."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "Birt-Hogg-Dubé sits alongside VHL disease among inherited renal-cancer syndromes: both cause multifocal, bilateral RCC needing nephron-sparing surgery and lifelong imaging, but differ in tumor type (BHD chromophobe/oncocytic via folliculin-mTOR; VHL clear-cell via HIF)."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The skin tumors of Birt-Hogg-Dubé are fibroblast-rich hamartomas: fibrofolliculomas and trichodiscomas are benign white facial papules where folliculin loss disrupts hair-follicle signaling, producing a fibroblast-laden stroma—often the first clue to the syndrome."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Birt-Hogg-Dubé strikes the renal system multifocally: folliculin loss drives bilateral chromophobe and hybrid oncocytic renal cell carcinomas, so the renal system needs lifelong MRI surveillance and nephron-sparing surgery to preserve kidney function over a lifetime."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The lungs are a defining target in Birt-Hogg-Dubé: folliculin loss produces multiple basal pulmonary cysts that rupture, causing recurrent spontaneous pneumothorax, often the presenting feature in a young adult—so unexplained pneumothorax should prompt BHD testing."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Birt-Hogg-Dubé overlaps with PTEN hamartoma (Cowden) syndromes: both cause skin hamartomas and cancer risk through deranged mTOR signaling—FLCN loss in BHD and PTEN loss in Cowden converge on one growth pathway, so they share dermatologic clues and tumor risk."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "FLCN loss in Birt-Hogg-Dubé disrupts autophagy and AMPK-mTOR balance: folliculin tunes the AMPK/mTOR axis controlling autophagy and metabolism, so its loss deregulates growth and energy sensing—linking the gene to BHD's renal tumors and lung cysts."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "The skin tumors of Birt-Hogg-Dubé are collagen-rich hamartomas: fibrofolliculomas are benign follicle tumors with proliferating collagen-laden stroma, and these flesh-colored facial papules are often the first clue prompting FLCN genetic testing."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Birt-Hogg-Dubé presents through the integumentary system: its skin tumors—fibrofolliculomas, trichodiscomas and skin tags on the face, neck and upper trunk—are usually how the syndrome is first recognized, before the kidney and lung disease declare themselves."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Birt-Hogg-Dubé has a debated colorectal cancer link: some FLCN families show increased colonic polyps and cancer, so colonoscopic surveillance is considered, reflecting how this single tumor-suppressor may predispose beyond the classic kidney, lung and skin triad."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Birt-Hogg-Dubé predisposes to thyroid tumors: FLCN carriers have an excess of thyroid nodules and oncocytic thyroid neoplasms, fitting the syndrome's broader tendency to oncocytic (mitochondria-rich) tumors across kidney, salivary gland and thyroid."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "Birt-Hogg-Dubé joins the family of dominant tumor-predisposition syndromes: like MEN1, a single inherited tumor-suppressor defect (here FLCN) seeds tumors across organs—so both demand lifelong, multi-organ surveillance tailored to their gene."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "FLCN, the Birt-Hogg-Dubé gene, also governs fat metabolism: through AMPK and PGC-1α it shapes adipocyte energy use and brown-fat thermogenesis, so beyond its tumor-suppressor role, FLCN links this syndrome's pathway to whole-body metabolism."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Birt-Hogg-Dubé can involve the pancreas: FLCN carriers show an excess of pancreatic cysts and rare neoplasms, extending the syndrome's pattern of hamartomas and tumors beyond the kidney, lung, and skin into abdominal organs."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "BHD's lung cysts threaten oxygen delivery: FLCN loss creates thin-walled basal lung cysts that rupture as spontaneous pneumothorax, collapsing the lung and cutting off the air exchange that loads oxygen into blood—the syndrome's most dangerous everyday risk."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "BHD sits among MET-driven hereditary kidney cancers as a contrast: hereditary papillary RCC is caused by MET activation, while BHD's FLCN loss yields chromophobe and oncocytic tumors, so the gene pinpoints which inherited renal cancer syndrome a patient has."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "FLCN normally restrains the AKT-mTOR growth axis: losing it in BHD lets AKT and mTORC1 run high, driving the kidney tumors and skin and lung lesions—why this pathway is the target of rapamycin-class drugs studied in the syndrome."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "BHD tumors are pseudo-hypoxic like VHL kidney cancers: losing FLCN deranges mTOR and stabilizes HIF, so the renal tumors behave as if starved of oxygen even when they are not, driving growth and a metabolic shift toward glycolysis."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages populate BHD's lung cysts and tumors: in the thin-walled cysts that rupture into pneumothorax and in the kidney tumor stroma, they shape inflammation and tissue remodeling around the FLCN-deficient cells."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "BHD has been linked to colon polyps in some families: beyond the classic skin, lung and kidney triad, reports of colonic polyps and possible colorectal risk mean the large intestine is sometimes watched, though the association remains debated."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "BHD lets air into the chest: its thin-walled lung cysts rupture and spill air—mostly nitrogen—into the pleural space, collapsing the lung in the recurrent spontaneous pneumothoraxes that often first reveal the syndrome."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "BHD's hallmark skin bumps are fibrous: fibrofolliculomas are benign hamartomas of fibrous tissue around hair follicles, the small white papules on the face that signal the FLCN mutation underneath."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "BHD's renal tumors lean on VEGF: losing FLCN stabilizes HIF, which drives VEGF and angiogenesis, helping feed the kidney cancers that are the syndrome's most dangerous feature."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "BHD is mapped by imaging: chest CT photons reveal the basal lung cysts that cause its recurrent collapsed lungs, and renal MRI screens for the kidney tumors it predisposes to."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "BHD's lung cysts arise in the alveolar tissue: thin-walled cysts form at the lung bases, weakening the air sacs so they rupture into the spontaneous pneumothorax that often first reveals the syndrome."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "BHD reaches the thyroid: the FLCN syndrome's tumor predisposition extends beyond the kidney to thyroid nodules and possible cancer, which is monitored alongside the lungs and kidneys."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy explains BHD's oncocytic tumors: losing FLCN unleashes mitochondrial biogenesis, so the kidney and other tumors fill with cells crammed with abnormal mitochondria — the granular oncocytes that define the syndrome's pathology."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "BHD's skin papules climb to the eyelids: the fibrofolliculomas that dot the face and neck extend onto and around the eyelids, small flesh-colored bumps that are a visible clue to the underlying FLCN mutation."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The oncocytoma spectrum can include the adrenal: BHD's FLCN loss predisposes to oncocytic tumors not just in the kidney but occasionally in the adrenal gland, extending its endocrine reach."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "BHD's lung cysts form where the wall gives way: FLCN loss weakens cell-cell adhesion in the alveolar and small-airway walls, so under the mechanical stretch of breathing the tissue tears into basal, subpleural cysts that rupture as pneumothorax."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "FLCN keeps cells stuck together: the protein helps maintain the adherens junctions linking epithelial and endothelial cells, and its loss loosens these contacts — a shared thread behind the syndrome's lung cysts and hypervascular kidney tumors."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The polyps are not confined to the colon: beyond its debated colorectal risk, BHD can stud the stomach and upper GI tract with polyps, part of the FLCN-driven overgrowth that surfaces across many epithelia."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "BHD is autosomal dominant: a single germline FLCN mutation passes to half of a carrier's children, so diagnosis triggers cascade genetic testing of relatives and the option of preimplantation or prenatal testing to keep the kidney and lung risk from reaching the next generation."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "BHD's facial papules mimic skin cancer: its fibrofolliculomas are benign hair-follicle hamartomas that can be mistaken clinically for basal cell carcinoma, so a biopsy distinguishing the two is what often first points to the underlying FLCN syndrome."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "BHD's kidney surgery costs red cells: repeated nephron-sparing resections of its recurrent renal tumors, and the loss of functioning kidney tissue that makes erythropoietin, can leave carriers anemic over a lifetime of tumor surveillance and surgery."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "FLCN reaches the pigment cells too: Birt-Hogg-Dubé carries a reported increased risk of melanoma, reflecting folliculin's role beyond the kidney and lung in the skin's melanocytes."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Losing FLCN releases the cell cycle: unrestrained mTOR signaling raises cyclin D1 to drive the proliferation behind BHD's hamartomas and renal tumors, the growth engine downstream of folliculin loss."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "It sits among the hamartoma-and-cancer syndromes: like Peutz-Jeghers, BHD is a single-gene disorder that sprouts benign hamartomas (here hair-follicle and lung) alongside a raised risk of specific cancers."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "BHD's lung cysts mimic emphysema: its basal pulmonary cysts and recurrent spontaneous pneumothoraces can be mistaken for COPD on imaging, but lung function is usually preserved — the distinction matters because BHD signals hereditary kidney-cancer risk."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Folliculin shapes TGF-β signaling: FLCN loss in BHD dysregulates the TGF-β pathway, contributing to the abnormal cell differentiation behind its fibrofolliculomas, lung cysts, and renal tumors."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Renal tumors accumulate a second hit: beyond the germline FLCN loss, secondary TP53 mutations are found in BHD-associated chromophobe and oncocytic renal carcinomas, marking progression toward malignancy."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Lost folliculin lifts a brake on NF-κB: FLCN normally restrains inflammatory and mTOR-linked signaling, so its loss in BHD engages NF-κB-driven survival pathways that support the syndrome's tumors."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "FLCN-deficient cells activate STAT3: the chromophobe and oncocytic renal tumors of BHD show STAT3 signaling that supports their proliferation, one of the pathways downstream of folliculin loss."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Saving the kidneys costs nephrons over a lifetime: recurrent BHD renal tumors demand repeated nephron-sparing surgeries, so the cumulative loss of kidney tissue can drift toward chronic kidney disease."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Its renal tumors drag the count down: the recurrent renal cell carcinomas of BHD bring tumor inflammation and surgical nephron loss that, with reduced erythropoietin, contribute an anemia of chronic disease."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Repeated cancer surgery raises the clot risk: the lifetime of renal-tumor resections and the prothrombotic state of renal cell carcinoma predispose BHD patients to perioperative venous thromboembolism."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Lifelong cancer surveillance weighs on the mind: living with an inherited risk of renal tumors, recurrent surgeries and the threat of spontaneous lung collapse imposes a real psychological burden in BHD."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its lung cysts can harbor mold: the thin-walled pulmonary cysts of Birt-Hogg-Dubé create air spaces where inhaled Aspergillus can colonize and form an aspergilloma."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Recurrent pneumothorax and surgery invite infection: repeated chest-tube drainage and pleurodesis for collapsing lungs, plus nephron-sparing renal-tumor surgery, carry a cumulative risk of serious infection and sepsis."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Unpredictable lung collapse breeds worry: the threat of a sudden spontaneous pneumothorax and the constant renal-cancer surveillance of BHD foster chronic health anxiety."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "It demands repeated surgery that must heal: BHD brings recurrent nephron-sparing renal-tumour operations and pleurodesis or surgery for recurrent pneumothorax, leaving wounds to heal over a lifetime."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "FLCN loss seeds tumours beyond the kidney: BHD is associated with colonic polyps and parotid oncocytomas, extending its hamartoma-tumour spectrum into the digestive and salivary tract."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its gene sits in the metabolic pathway: FLCN regulates the AMPK-mTOR axis that governs cellular metabolism, and BHD shows associations with thyroid and parathyroid nodules."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "A lung collapse can crash the circulation: rupture of BHD lung cysts can cause a tension pneumothorax that shifts the mediastinum and obstructs venous return, producing obstructive shock and cardiac arrest."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its hamartomas reach soft tissue: BHD's tumour spectrum includes lipomas and angiolipomas among connective-tissue lesions beyond the skin, lung and kidney."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its gene tunes immune metabolism: FLCN regulates the mTOR/TFEB axis that also governs lysosomal function and immune-cell metabolism, the molecular hub underlying BHD's varied tumours."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "A fellow skin-led tumour syndrome: like Birt-Hogg-Dubé, NF1 is autosomal-dominant and announced by skin signs — café-au-lait macules and neurofibromas — that flag inherited tumour predisposition."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "Another tumour-suppressor syndrome: NF2 joins Birt-Hogg-Dubé among inherited disorders where loss of a single tumour-suppressor gene drives characteristic tumours, here bilateral vestibular schwannomas."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "A comparator of inherited facial papules: Gorlin syndrome's multiple basal cell carcinomas enter the differential of Birt-Hogg-Dubé's fibrofolliculomas, both hereditary causes of numerous facial skin tumours."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Advanced kidney tumours need systemic drugs: the chromophobe and oncocytic renal cancers of Birt-Hogg-Dubé, when metastatic, are treated with mTOR and VEGFR-targeted agents reflecting their FLCN-mTOR biology."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "A fellow cause of inherited cystic lung disease: like Birt-Hogg-Dubé, DICER1 syndrome produces familial lung cysts prone to pneumothorax, so both demand awareness of cystic lung change in young patients."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "A shared lifetime of surveillance: like Carney complex, Birt-Hogg-Dubé commits carriers to lifelong multi-organ imaging surveillance, here annual renal MRI to catch its kidney tumours early."
  - target: 01-human/05-tissue/lung-slice
    relation: connects-to
    note: "It riddles the lung with cysts: folliculin loss produces basal, subpleural lung cysts that rupture as recurrent spontaneous pneumothorax — often the first clue to Birt-Hogg-Dubé, seen as cystic change on a lung slice."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Its kidney tumours resist chemo: the chromophobe and hybrid oncocytic renal carcinomas of Birt-Hogg-Dubé are indolent and chemoresistant, managed by surveillance and nephron-sparing surgery rather than cytotoxic chemotherapy."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Less immunotherapy-responsive than clear cell: unlike VHL-driven clear-cell kidney cancer, the chromophobe/oncocytic tumours of Birt-Hogg-Dubé have low mutational burden and respond poorly to checkpoint blockade."
  - target: 01-human/03-molecular/stk11
    relation: connects-to
    note: "The energy-sensing axis: folliculin partners with AMPK and the LKB1/STK11 kinase to sense cellular energy, mechanistically linking Birt-Hogg-Dubé to the STK11-driven Peutz-Jeghers hamartoma syndrome."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Mitochondria-packed oncocytes: folliculin loss dysregulates mitochondrial biogenesis, so BHD renal oncocytomas and hybrid tumours are crammed with mitochondria churning out ATP—the oncocytic phenotype."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Lifelong cancer surveillance: like Li-Fraumeni syndrome, Birt-Hogg-Dubé is an autosomal-dominant tumour-predisposition syndrome whose carriers need structured multi-organ screening from early adulthood."
  - target: 01-human/07-system/marfan-syndrome
    relation: connects-to
    note: "Two genetic causes of spontaneous pneumothorax: Birt-Hogg-Dubé's basal lung cysts and Marfan syndrome's apical blebs both predispose to recurrent collapsed lung, reached by different structural routes."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "Cystic lung and air leaks: like cystic fibrosis, Birt-Hogg-Dubé produces a cystic lung architecture prone to recurrent pneumothorax, though its thin-walled basal cysts differ from CF's bronchiectasis."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "A debated colon link: some studies tie Birt-Hogg-Dubé to colorectal polyps and cancer through FLCN loss in the intestinal epithelium, though the association remains controversial."
  - target: 01-human/03-molecular/tsc1-tsc2
    relation: connects-to
    note: "mTOR convergence: FLCN and the TSC1-TSC2 complex both regulate mTORC1, and the two hamartoma syndromes share cystic lung disease and renal lesions, framing BHD as a sister mTOR-pathway disorder."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo dysregulation: FLCN loss can deregulate the Hippo-YAP pathway, an additional driver implicated in the oncocytic and chromophobe renal tumours characteristic of Birt-Hogg-Dubé."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Pseudohypoxic overlap: like SDH- and VHL-driven pheochromocytoma-paraganglioma, FLCN-deficient BHD tumours show HIF-1α-driven pseudohypoxic, angiogenic signalling within the inherited renal/endocrine tumour spectrum."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "TFE3-driven MYC: FLCN loss in BHD releases the transcription factor TFE3 to the nucleus, where it upregulates MYC and the biosynthetic programme fuelling tumour growth."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Antioxidant reprogramming: FLCN-deficient BHD cells show constitutive NRF2 (NFE2L2) activation, driving the metabolic and antioxidant programme that supports their survival."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Wnt dysregulation: FLCN loss perturbs Wnt/β-catenin signalling, an additional oncogenic pathway contributing to the renal tumours of Birt-Hogg-Dubé."
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "Metabolic stress axis: the FLCN-FNIP-AMPK complex regulates FoxO transcription factors, so FLCN loss disturbs the FoxO-controlled oxidative-stress and metabolic programme of Birt-Hogg-Dubé cells."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK in renal tumours: ERK/MAPK signalling is activated downstream of FLCN loss and contributes to the proliferation of the chromophobe and oncocytic renal tumours of Birt-Hogg-Dubé."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "HIF metabolic shift: FLCN loss perturbs the EGLN1 (PHD2)-HIF axis, stabilising HIF to drive the glycolytic, Warburg-like metabolism characteristic of Birt-Hogg-Dubé renal tumours."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "Lung-cyst adhesion: FLCN regulates E-cadherin-dependent cell-cell adhesion, and impaired adhesion in the alveolar wall underlies the lung cysts and recurrent spontaneous pneumothorax that characterise Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/sdhb
    relation: connects-to
    note: "Mitochondria-rich tumours: FLCN loss boosts mitochondrial biogenesis, giving the oncocytic and chromophobe renal tumours of Birt-Hogg-Dubé a mitochondria-packed phenotype that parallels the mitochondria-rich tumours of SDH deficiency."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Renal-tumour immortalisation: TERT reactivation maintains telomeres in the renal cell carcinomas that Birt-Hogg-Dubé predisposes to, granting the replicative immortality that lets the FLCN-deficient clone proliferate."
  - target: 01-human/03-molecular/fh
    relation: connects-to
    note: "Hereditary-RCC differential: Birt-Hogg-Dubé (FLCN) sits among the inherited renal-cancer syndromes alongside VHL, SDHB and fumarate-hydratase-driven HLRCC, each producing a characteristic histology — BHD the chromophobe and hybrid oncocytic tumours."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-factor support: IGF-1R signalling, converging on the same AKT-mTOR axis dysregulated by folliculin loss, supports the proliferation of the renal tumours of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Cytostatic mTOR therapy: folliculin loss disinhibits mTOR and suppresses caspase-3 apoptosis, so mTOR inhibitors restrain rather than kill BHD tumour cells — a cytostatic effect that mirrors their action in the related mTOR-driven hamartoma syndromes."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K dysregulation: FLCN loss in Birt-Hogg-Dubé dysregulates the PI3K-AKT-mTOR axis (AKT and mTOR already mapped), driving the renal tumours and skin lesions of the syndrome."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Fibrofolliculoma origin: NOTCH governs hair-follicle development, and its dysregulation downstream of FLCN loss contributes to the fibrofolliculomas — hair-follicle hamartomas — that are the defining skin lesion of BHD."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis resistance: anti-apoptotic BCL-2 supports the survival of the slow-growing renal tumours of Birt-Hogg-Dubé, complementing the mTOR-driven suppression of caspase-3 apoptosis already mapped."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "Metabolic-RCC spectrum: oncometabolite-producing IDH mutations parallel the FH and SDHB metabolic lesions (both already mapped) within the spectrum of metabolically-driven hereditary renal tumours, where altered metabolites stabilise HIF and reprogram the epigenome."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Renal-tumour angiogenesis: VEGF/PDGF-axis angiogenesis (VEGF already mapped) supports the renal tumours that Birt-Hogg-Dubé predisposes to and is the target of the tyrosine-kinase inhibitors used in renal cell carcinoma."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Proliferative cooperation: RAS-MAPK signalling through ERK1/2 (already mapped) provides a proliferative input that cooperates with FLCN loss in driving the tumours of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "FLCN loss dysregulates HIF activity; HIF-2α (EPAS1) signalling links Birt-Hogg-Dubé syndrome to the hypoxia-driven renal tumorigenesis it shares with the VHL/MET hereditary-RCC differential (all mapped)."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is a marker and modulator of the renal tumours that arise in Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT3 signalling (STAT3 mapped) provides a proliferative and survival input cooperating with FLCN loss in Birt-Hogg-Dubé tumorigenesis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of the renal tumours that arise in Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the connective-tissue and lung-cyst phenotypes (fibrofolliculomas, pulmonary cysts) of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "FLCN loss perturbs autophagy and mitochondrial quality control, and the resulting cytosolic DNA can engage cGAS-STING in the lesions of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D1 cell-cycle entry (cyclin-D1 already mapped) drives the proliferation of the renal tumors of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the renal tumors of Birt-Hogg-Dubé syndrome must evade."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β interacts with the AMPK-mTOR axis (AMPK and mTOR already mapped) that FLCN loss dysregulates in Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the renal tumors of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of the tumors of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of MET and other receptor tyrosine kinases (MET already mapped) contributes to the survival signaling of the renal tumors of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation implicated in the tumorigenesis of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of the renal tumors of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the renal tumors of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the renal tumors of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of the renal tumors of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic reprogramming: folliculin loss dysregulates the AMPK energy sensor it partners with (AMPK already mapped) and the mTOR pathway, shifting cellular metabolism and mitochondrial biogenesis in a way that also links the syndrome to insulin-responsive energy handling."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Renal tumour invasion: the AXL receptor tyrosine kinase can drive epithelial-mesenchymal transition and invasion in the renal tumours of Birt-Hogg-Dubé, a signalling route relevant to the rare aggressive lesions beyond the usually indolent chromophobe and oncocytic tumours."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen presentation: MHC class II-restricted T-cell responses shape immune surveillance of the renal tumours of Birt-Hogg-Dubé, relevant to immunotherapy of any that progress to a more aggressive renal cell carcinoma."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Renal immunotherapy: IL-2-driven T-cell responses underlie the immunotherapy of the rare aggressive renal cell carcinomas that can arise in Birt-Hogg-Dubé (MHC class II already mapped), the treatment reserved for tumours that progress."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immune surveillance: cytotoxic CD8 T cells provide the surveillance against the renal tumours of Birt-Hogg-Dubé (perforin already mapped), and their function is central to the checkpoint immunotherapy of any that become aggressive."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Metabolic oxidative stress: loss of the FLCN-AMPK-mTOR axis (already mapped) dysregulates cellular metabolism, and the resulting oxidative stress, to which xanthine oxidase contributes, is part of the tumour-promoting milieu in Birt-Hogg-Dubé cells."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the microenvironment of any aggressive Birt-Hogg-Dubé renal tumour dampens the anti-tumour T-cell response (PD-1 and CD8 already mapped), part of the immune evasion relevant to checkpoint immunotherapy."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the renal tumours of Birt-Hogg-Dubé, part of their stromal microenvironment."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Lipid metabolism: folliculin, through the AMPK-mTOR axis (already mapped), regulates cellular lipid and cholesterol metabolism, and its loss shifts the metabolic phenotype that contributes to tumour formation in Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the renal tumours of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of the renal tumours in Birt-Hogg-Dubé syndrome."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Haematuria and anaemia: the renal tumours of Birt-Hogg-Dubé can bleed, causing the haematuria and iron-deficiency anaemia that reflect the systemic effects of the renal cancer beyond the tumour itself."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Folliculin energy metabolism: the FLCN-AMPK (already mapped) energy-sensing axis that folliculin regulates connects to the leptin adipokine signalling of the metabolic dimension of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "AMPK-activating adipokine: adiponectin, with leptin (already mapped), activates the AMPK (already mapped) energy metabolism that folliculin governs, part of the metabolic milieu of Birt-Hogg-Dubé syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the folliculin-AMPK (already mapped) energy metabolism of Birt-Hogg-Dubé syndrome."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "Hereditary-RCC differential: Birt-Hogg-Dubé and the von Hippel-Lindau (VHL already mapped) syndromes are hereditary renal-tumour syndromes in the differential, distinguished by the FLCN versus VHL genes."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "mTOR-pathway overlap: Birt-Hogg-Dubé and tuberous sclerosis are mTOR/AMPK (TSC1-TSC2 already mapped) hamartoma syndromes with renal and lung (cysts, LAM) involvement."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibrofolliculoma stroma: the fibrofolliculomas of Birt-Hogg-Dubé are benign hair-follicle tumours with a fibroblast/collagen (PDGF already mapped) stroma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity relevant to the renal tumours of Birt-Hogg-Dubé."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the Birt-Hogg-Dubé renal tumours."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the renal tumours of Birt-Hogg-Dubé."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the Birt-Hogg-Dubé renal tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the Birt-Hogg-Dubé tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of Birt-Hogg-Dubé."
---

# Birt-Hogg-Dubé Syndrome

## Overview

**Birt-Hogg-Dubé syndrome (BHD)** is an autosomal dominant hereditary cancer and hamartoma predisposition syndrome caused by germline pathogenic variants in **FLCN** (folliculin; chromosome 17p11.2), a GAP (GTPase-activating protein) for the **RagC and RagD GTPases** that regulate mTORC1 activation by amino acids at the lysosomal surface. BHD was first described in 1977 by dermatologists Birt, Hogg, and Dubé as a condition of fibrofolliculomas and trichodiscomas; the renal tumor and pulmonary cyst associations were recognized subsequently. BHD is characterized by a triad: (1) **cutaneous fibrofolliculomas** — benign white papules on the face, neck, and trunk from hair follicle origin; (2) **pulmonary cysts** — thin-walled basal cysts causing a ~7-fold increased risk of spontaneous pneumothorax; and (3) **bilateral multifocal renal tumors** — predominantly chromophobe RCC and hybrid oncocytic/chromophobe RCC, with ~15-30% lifetime risk of renal malignancy. BHD-associated RCC has a distinct biology from VHL-driven clear cell RCC (not HIF-1α-mediated; driven by mTOR-Rag GTPase-TFE3 dysregulation) and a relatively favorable prognosis within the RCC spectrum. Surveillance with annual MRI and nephron-sparing surgery for tumors >3 cm are the mainstay of management [^nickerson-2002-flcn-bhd] [^tsun-2013-flcn-rag].

**Epidemiology:**
- Prevalence: ~1/200,000; ~1,500-2,500 diagnosed patients in the USA; considerably underdiagnosed (fibrofolliculomas often mistaken for fibrous papules or adenoma sebaceum)
- Inheritance: autosomal dominant; 50% transmission per generation
- De novo mutations: ~10% of BHD cases; may present without family history
- FLCN germline pathogenic variant found in ~80-90% of clinically diagnosed BHD families; remainder may have deep intronic variants, promoter mutations, or mosaicism
- Penetrance: fibrofolliculomas ~90% by age 40; pulmonary cysts ~80-90%; renal tumors ~15-30% lifetime

**Comparison of hereditary RCC syndromes:**

| Syndrome | Gene | RCC histology | Lifetime RCC risk | Molecular driver |
|---|---|---|---|---|
| VHL disease | VHL | Clear cell | ~65-70% | HIF-1α/HIF-2α pseudohypoxia |
| BHD syndrome | FLCN | Chromophobe, hybrid oncocytic | ~15-30% | mTOR/Rag/TFE3 dysregulation |
| Hereditary papillary RCC | MET | Type 1 papillary | ~70-80% | MET kinase constitutive activation |
| HLRCC | FH | Collecting duct-like, type 2B papillary | ~15-20% | HIF-1α + fumarate oncometabolite |
| TSC | TSC1/TSC2 | Angiomyolipoma (benign) + rarely ccRCC | ~5% (malignant RCC) | mTOR via Rheb |

## Structure

### BHD clinical manifestations

**Cutaneous fibrofolliculomas:**
- Origin: from the fibrous sheath of the hair follicle (mantle/infundibulum region); distinct from sebaceous adenoma or fibrous papule
- Morphology: dome-shaped, smooth, white/skin-colored papules; 1-5 mm; occasionally larger
- Distribution: face (especially nose, perinasal, cheeks), neck, upper trunk; rarely on arms; never on palms or soles
- Age of onset: typically 3rd-5th decade (25-50 years); may be absent or sparse in young adults
- Symptoms: usually asymptomatic; cosmetic concern; may cause misdiagnosis as skin disease alone without kidney/pulmonary workup
- Histology: anastomosing epithelial strands from hair follicle mantles in a fibromyxoid stroma; distinct from trichofolliculoma, fibrous papule; FLCN IHC: reduced nuclear staining in fibrofolliculoma cells
- Dermoscopy: parallel or reticular pattern with yellowish globules
- Additional skin features: trichodiscomas (hair disc hamartomas; similar to fibrofolliculoma, sometimes considered same entity), acrochordons (skin tags — non-specific but associated)

**Pulmonary cysts:**
- Prevalence: ~80-90% of BHD gene carriers; may be asymptomatic and discovered incidentally
- Imaging (HRCT): bilateral, basal, subpleural thin-walled cysts (air-filled, no matrix); 2 mm to >20 cm; may be multifocal; cyst walls are thin (<2 mm); no ground-glass halo; variable size/number within same patient
- Histology of cyst wall: lined by type II pneumocytes or flattened cells; small FLCN-deficient cells may be present in some cysts
- Pulmonary function: usually normal (cysts are air-filled, not solid); reduced DLCO in some patients
- Spontaneous pneumothorax: ~22-38% of BHD patients (vs ~0.1-0.3% general population); risk ~7-fold higher than general population; bilateral simultaneous pneumothorax rare but described; management: observation for small, tube thoracostomy for large; after first spontaneous pneumothorax in BHD → contralateral risk ~30-50% over 10 years → pleurodesis (surgical or mechanical) recommended after first ipsilateral recurrence or bilateral event
- No treatment for asymptomatic cysts: surveillance HRCT to monitor cyst growth (rate rare); HRCT baseline recommended for all confirmed BHD carriers

### BHD-associated renal tumors

**Histological spectrum:**
- Chromophobe RCC (~50% of BHD renal tumors): large pale cells with perinuclear halo; Hale colloidal iron diffusely positive; IHC: CK7++, CD117+, parvalbumin+; nuclear TFE3 often positive; not HIF-1α-driven; 5-year OS ~88% for localized disease (better than ccRCC)
- Hybrid oncocytic/chromophobe tumor (~33%): overlapping features of chromophobe RCC and oncocytoma; eosinophilic granular cytoplasm (mitochondria-packed); perinuclear halo may be subtle; IHC: mixed CK7/CD117
- Renal oncocytoma (benign, ~5%): mahogany-brown, well-circumscribed; mitochondria-rich cells; FLCN LOF found in ~25% of sporadic oncocytomas; in BHD, oncocytomas may be adjacent to or mixed with chromophobe foci
- Clear cell RCC (~5%): less common in BHD; unclear if true association or coincidence; VHL is intact in BHD (unless coincidental second germline mutation)
- Papillary RCC (<5%): rare in BHD

**Tumor characteristics:**
- Bilateral: ~67% of BHD-associated RCC is bilateral at time of diagnosis (compared to ~1-2% in sporadic RCC)
- Multifocal: ~52% of BHD RCC patients have multifocal tumors on a single kidney
- Small at detection: surveillance-detected tumors often <3 cm; asymptomatic; favorable stage at detection

## Function

### Molecular pathogenesis of BHD

**FLCN LOF and RagC/D dysregulation:** [^tsun-2013-flcn-rag]
Normal: amino acid availability → Ragulator activates FLCN-FNIP → FLCN stimulates RagC/D GTPase → RagC/D-GDP → mTORC1 lysosomal docking → mTOR activated; in FLCN-deficient cells: RagC/D remains GTP-loaded → impaired mTORC1 lysosomal docking under some conditions; but net mTORC1 output in BHD RCC: elevated (via other inputs — AKT, ERK) — this paradox is explained by differential Rag signaling contexts and feedback loops

**TFE3/TFEB nuclear translocation:**
FLCN LOF → TFE3 and TFEB escape mTORC1-mediated cytoplasmic sequestration → nuclear TFE3/TFEB → lysosomal biogenesis genes (LAMP1, CTSD, MCOLN1), autophagy genes (BECN1, LC3), and mitochondrial biogenesis genes (PGC-1α, TFAM, NDUFA, COX subunits) upregulated; mitochondrial biogenesis → mitochondria accumulation → oncocytic appearance; TFE3 nuclear immunostaining is a practical diagnostic marker for FLCN-deficient RCC

**mTOR-Rag vs mTOR-Rheb (comparison with TSC):**
| Pathway | Regulator | mTOR activator | Tumor type |
|---|---|---|---|
| Rheb pathway | TSC1-TSC2 complex (GAP for Rheb) | Rheb-GTP | TSC-associated AML, SEGA |
| Rag pathway | FLCN-FNIP (GAP for RagC/D) | RagA/B-GTP + RagC/D-GDP | BHD-associated chromophobe RCC |
Both converge on mTORC1 but via distinct upstream signals; rapalogues active in both contexts

**Pulmonary cyst biology:**
FLCN-deficient alveolar type II cells → mTOR dysregulation + TFE3 activation → abnormal alveolar remodeling → cyst formation; mouse models (lung-specific Flcn knockout): cysts develop, similar to BHD human lung; mechanism: FLCN LOF → lysosomal exocytosis → cathepsins secreted → extracellular matrix degradation → cyst formation; similar biology may explain pulmonary LAM in TSC (smooth muscle-like LAM cells with TSC2 LOF) though distinct cell types

## Pathology

### Diagnosis

**Clinical diagnosis:**
Major diagnostic criteria:
- ≥5 fibrofolliculomas or trichodiscomas with at least 1 histologically confirmed, adult onset
- Pathogenic FLCN germline variant

Minor criteria:
- Multiple bilateral pulmonary cysts (basal, subpleural) with no other apparent cause ± spontaneous pneumothorax
- Renal tumor ≤50 years of age OR bilateral or multifocal RCC OR chromophobe/hybrid oncocytic RCC (confirmed histology)
- First-degree relative with BHD

Definite BHD: 1 major OR 2 minor criteria (European BHD Consortium definition)

**Genetic testing:**
- FLCN gene sequencing (full coding + splice sites): ~80-85% sensitivity in clinical BHD
- MLPA for large deletions: additional ~5-10%
- If all negative: repeat sequencing with attention to intragenic microsatellite repeats (c.1285dupC exon 11 most common mutation); RNA splicing analysis; somatic mosaicism testing
- Cascade testing: all first-degree relatives of pathogenic FLCN variant carrier

### Surveillance and management (NCCN/European guidelines)

**Renal:**
- Annual renal MRI (preferred) or ultrasound alternating every 6 months from age 20-21
- Any renal tumor <3 cm: active surveillance with imaging every 6-12 months
- Renal tumor ≥3 cm or growing: intervention recommended
  - **Nephron-sparing surgery (partial nephrectomy)**: gold standard; open, laparoscopic, or robot-assisted; goal: complete tumor excision with negative margins while preserving maximum renal parenchyma; critical in BHD due to bilateral/multifocal tumors
  - **Thermal ablation** (radiofrequency ablation, cryoablation): for smaller tumors (<3 cm) in selected patients; less morbidity; incomplete ablation risk; used in patients with poor surgical risk or existing renal insufficiency
  - **Radical nephrectomy**: avoided unless entire kidney is tumor-replaced; lifelong kidney function preservation is paramount
- Post-treatment surveillance: MRI every 6-12 months × 2-3 years, then annually

**Pulmonary:**
- Baseline HRCT for all confirmed BHD carriers
- Routine HRCT surveillance not necessary if cysts stable and asymptomatic
- First spontaneous pneumothorax: hospitalization, tube thoracostomy or aspiration; after resolution, discuss pleurodesis
- After 2nd ipsilateral pneumothorax OR after 1st contralateral spontaneous pneumothorax: video-assisted thoracoscopic (VATS) pleurodesis (mechanical or chemical) recommended
- Counsel BHD patients: avoid scuba diving (barotrauma → pneumothorax); pressurized aircraft OK (commercial airline pressure equivalent to 8,000 ft — minimal additional risk)
- Genetic counseling: inform family members of pneumothorax risk during air travel or diving

**Dermatologic:**
- Confirm fibrofolliculoma diagnosis by punch biopsy (histology)
- Cosmetic management: laser (CO2, Er:YAG), dermabrasion, shave excision; lesions recur after treatment
- Topical rapamycin: anecdotal reports of fibrofolliculoma reduction with topical sirolimus ointment (not FDA-approved for this indication)

**Treatment of metastatic BHD-associated RCC:**
- No FDA-approved BHD-specific therapy
- Sunitinib (VEGFR-TKI): modest activity in chromophobe RCC (ORR ~5-10%); less effective than in ccRCC
- Cabozantinib (VEGFR/MET/AXL inhibitor): higher activity in non-ccRCC including chromophobe (ORR ~15-20%)
- Checkpoint inhibitors: nivolumab + ipilimumab; chromophobe RCC has low TMB and PD-L1 → modest ICB response
- Everolimus: mTOR inhibitor; rational in FLCN-deficient RCC; case reports of activity; Phase 2 BHD-specific study ongoing
- Belzutifan (HIF-2α inhibitor): explored in chromophobe RCC (not VHL-driven but may have HIF-2α activity via mTOR); Phase 2 data emerging (NCT04924075)

**Prognosis:**
- BHD-associated RCC: when detected by surveillance at early stage (I-II), cure rate with NSS ~95%; 5-year OS for chromophobe RCC overall ~88% (significantly better than ccRCC at equivalent stage)
- Metastatic chromophobe RCC: mOS ~24-30 months (vs ~18-24 months for metastatic ccRCC in VEGF-TKI era)
- Major life impact: pulmonary (pneumothorax morbidity) and the need for lifelong renal surveillance/surgery dominate quality of life in BHD; with surveillance, premature death from BHD is rare

## Connections

- `connects-to` → **[FLCN](../../03-molecular/flcn/README.md)** — Germline FLCN truncating mutations cause BHD; FLCN is a GAP for RagC/D (amino acid sensing for mTORC1); biallelic FLCN LOF in each BHD tumor (second hit LOH at 17p11.2); somatic FLCN in sporadic chromophobe RCC (~20-25%)
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — FLCN LOF → Rag GTPase dysregulation → impaired mTORC1 lysosomal docking (RagC/D-GAP activity lost); mTOR inhibitors (everolimus) explored in BHD-associated RCC; FLCN LOF mTOR biology distinct from TSC1/TSC2 LOF (Rheb pathway) but both converge on mTORC1
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — BHD-associated RCC (chromophobe) vs VHL-associated RCC (clear cell): distinct histology and molecular drivers; VHL → HIF-1α pseudohypoxia; FLCN → mTOR/Rag dysregulation; BHD chromophobe has better prognosis than VHL ccRCC; belzutifan for VHL (not yet BHD)
- `connects-to` → **[Renal Cell Carcinoma](../../07-system/renal-cell-carcinoma/README.md)** — BHD lifetime RCC risk ~15-30%; chromophobe + hybrid oncocytic histology; bilateral multifocal; annual MRI from age 20; nephron-sparing surgery when >3 cm; sunitinib/cabozantinib for metastatic BHD RCC; chromophobe RCC 5-year OS ~88%
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — BHD causes bilateral basal pulmonary cysts in ~80-90% of carriers → 7× increased spontaneous pneumothorax risk; FLCN-deficient alveolar type II cells → mTOR dysregulation → cyst formation; pleurodesis recommended after second ipsilateral or first contralateral pneumothorax.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Fibrofolliculomas (hair follicle hamartomas; white facial papules) are the defining BHD cutaneous lesion; ≥5 histologically confirmed fibrofolliculomas is a major diagnostic criterion; cosmetic laser/dermabrasion reduces lesions; topical sirolimus (off-label) may reduce new formation.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — FLCN-FNIP1/2 complex interacts with AMPK at the lysosomal surface; FNIP1/2 are AMPK-binding partners; AMPK phosphorylates FLCN at Ser302; FLCN-FNIP-AMPK forms a metabolic sensing hub integrating energy status with mTORC1 activity; FNIP1-null mice develop cardiomegaly and lymphoma.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Birt-Hogg-Dubé and Cowden syndrome are mTORopathies: BHD loses folliculin (a GAP for the RagC/D GTPases that gate mTORC1) while Cowden loses PTEN (which restrains PI3K-AKT-mTOR), and both cause facial hamartomatous skin papules and a heightened risk of renal cell carcinoma.
- `connects-to` → **[Type II Pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — The lung cysts of Birt-Hogg-Dubé arise in alveolar type II pneumocytes: folliculin loss dysregulates mTOR and TFE3, driving abnormal alveolar remodeling and matrix breakdown that thins the cyst walls — producing the basal subpleural cysts behind a 7-fold pneumothorax risk.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is BHD's malignant target: folliculin loss causes bilateral, multifocal chromophobe and hybrid oncocytic renal cell carcinoma (~15-30% lifetime), so carriers get annual MRI from their 20s and nephron-sparing surgery once a tumour reaches ~3 cm.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Birt-Hogg-Dubé and tuberous sclerosis converge on mTOR and cystic lung disease: BHD folliculin and TSC1/2 both normally restrain mTOR, and both cause characteristic lung cysts with pneumothorax risk (BHD basal cysts; TSC/LAM diffuse)—so mTOR inhibition is a shared theme.
- `connects-to` → **[Hereditary Leiomyomatosis and Renal Cell Carcinoma](../hlrcc/README.md)** — Birt-Hogg-Dubé and HLRCC are both hereditary kidney-cancer syndromes with distinct biology: BHD (folliculin) causes chromophobe/oncocytic RCC with skin fibrofolliculomas and lung cysts, while HLRCC (fumarate hydratase) causes aggressive papillary RCC and uterine leiomyomas.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — Birt-Hogg-Dubé sits alongside VHL disease among inherited renal-cancer syndromes: both cause multifocal, bilateral RCC needing nephron-sparing surgery and lifelong imaging, but differ in tumor type (BHD chromophobe/oncocytic via folliculin-mTOR; VHL clear-cell via HIF).
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The skin tumors of Birt-Hogg-Dubé are fibroblast-rich hamartomas: fibrofolliculomas and trichodiscomas are benign white facial papules where folliculin loss disrupts hair-follicle signaling, producing a fibroblast-laden stroma—often the first clue to the syndrome.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Birt-Hogg-Dubé strikes the renal system multifocally: folliculin loss drives bilateral chromophobe and hybrid oncocytic renal cell carcinomas, so the renal system needs lifelong MRI surveillance and nephron-sparing surgery to preserve kidney function over a lifetime.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — The lungs are a defining target in Birt-Hogg-Dubé: folliculin loss produces multiple basal pulmonary cysts that rupture, causing recurrent spontaneous pneumothorax, often the presenting feature in a young adult—so unexplained pneumothorax should prompt BHD testing.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Birt-Hogg-Dubé overlaps with PTEN hamartoma (Cowden) syndromes: both cause skin hamartomas and cancer risk through deranged mTOR signaling—FLCN loss in BHD and PTEN loss in Cowden converge on one growth pathway, so they share dermatologic clues and tumor risk.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — FLCN loss in Birt-Hogg-Dubé disrupts autophagy and AMPK-mTOR balance: folliculin tunes the AMPK/mTOR axis controlling autophagy and metabolism, so its loss deregulates growth and energy sensing—linking the gene to BHD's renal tumors and lung cysts.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — The skin tumors of Birt-Hogg-Dubé are collagen-rich hamartomas: fibrofolliculomas are benign follicle tumors with proliferating collagen-laden stroma, and these flesh-colored facial papules are often the first clue prompting FLCN genetic testing.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Birt-Hogg-Dubé presents through the integumentary system: its skin tumors—fibrofolliculomas, trichodiscomas and skin tags on the face, neck and upper trunk—are usually how the syndrome is first recognized, before the kidney and lung disease declare themselves.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Birt-Hogg-Dubé has a debated colorectal cancer link: some FLCN families show increased colonic polyps and cancer, so colonoscopic surveillance is considered, reflecting how this single tumor-suppressor may predispose beyond the classic kidney, lung and skin triad.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Birt-Hogg-Dubé predisposes to thyroid tumors: FLCN carriers have an excess of thyroid nodules and oncocytic thyroid neoplasms, fitting the syndrome's broader tendency to oncocytic (mitochondria-rich) tumors across kidney, salivary gland and thyroid.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — Birt-Hogg-Dubé joins the family of dominant tumor-predisposition syndromes: like MEN1, a single inherited tumor-suppressor defect (here FLCN) seeds tumors across organs—so both demand lifelong, multi-organ surveillance tailored to their gene.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — FLCN, the Birt-Hogg-Dubé gene, also governs fat metabolism: through AMPK and PGC-1α it shapes adipocyte energy use and brown-fat thermogenesis, so beyond its tumor-suppressor role, FLCN links this syndrome's pathway to whole-body metabolism.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Birt-Hogg-Dubé can involve the pancreas: FLCN carriers show an excess of pancreatic cysts and rare neoplasms, extending the syndrome's pattern of hamartomas and tumors beyond the kidney, lung, and skin into abdominal organs.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — BHD's lung cysts threaten oxygen delivery: FLCN loss creates thin-walled basal lung cysts that rupture as spontaneous pneumothorax, collapsing the lung and cutting off the air exchange that loads oxygen into blood—the syndrome's most dangerous everyday risk.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — BHD sits among MET-driven hereditary kidney cancers as a contrast: hereditary papillary RCC is caused by MET activation, while BHD's FLCN loss yields chromophobe and oncocytic tumors, so the gene pinpoints which inherited renal cancer syndrome a patient has.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — FLCN normally restrains the AKT-mTOR growth axis: losing it in BHD lets AKT and mTORC1 run high, driving the kidney tumors and skin and lung lesions—why this pathway is the target of rapamycin-class drugs studied in the syndrome.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — BHD tumors are pseudo-hypoxic like VHL kidney cancers: losing FLCN deranges mTOR and stabilizes HIF, so the renal tumors behave as if starved of oxygen even when they are not, driving growth and a metabolic shift toward glycolysis.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages populate BHD's lung cysts and tumors: in the thin-walled cysts that rupture into pneumothorax and in the kidney tumor stroma, they shape inflammation and tissue remodeling around the FLCN-deficient cells.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — BHD has been linked to colon polyps in some families: beyond the classic skin, lung and kidney triad, reports of colonic polyps and possible colorectal risk mean the large intestine is sometimes watched, though the association remains debated.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — BHD lets air into the chest: its thin-walled lung cysts rupture and spill air—mostly nitrogen—into the pleural space, collapsing the lung in the recurrent spontaneous pneumothoraxes that often first reveal the syndrome.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — BHD's hallmark skin bumps are fibrous: fibrofolliculomas are benign hamartomas of fibrous tissue around hair follicles, the small white papules on the face that signal the FLCN mutation underneath.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — BHD's renal tumors lean on VEGF: losing FLCN stabilizes HIF, which drives VEGF and angiogenesis, helping feed the kidney cancers that are the syndrome's most dangerous feature.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — BHD is mapped by imaging: chest CT photons reveal the basal lung cysts that cause its recurrent collapsed lungs, and renal MRI screens for the kidney tumors it predisposes to.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — BHD's lung cysts arise in the alveolar tissue: thin-walled cysts form at the lung bases, weakening the air sacs so they rupture into the spontaneous pneumothorax that often first reveals the syndrome.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — BHD reaches the thyroid: the FLCN syndrome's tumor predisposition extends beyond the kidney to thyroid nodules and possible cancer, which is monitored alongside the lungs and kidneys.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy explains BHD's oncocytic tumors: losing FLCN unleashes mitochondrial biogenesis, so the kidney and other tumors fill with cells crammed with abnormal mitochondria — the granular oncocytes that define the syndrome's pathology.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — BHD's skin papules climb to the eyelids: the fibrofolliculomas that dot the face and neck extend onto and around the eyelids, small flesh-colored bumps that are a visible clue to the underlying FLCN mutation.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The oncocytoma spectrum can include the adrenal: BHD's FLCN loss predisposes to oncocytic tumors not just in the kidney but occasionally in the adrenal gland, extending its endocrine reach.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — BHD's lung cysts form where the wall gives way: FLCN loss weakens cell-cell adhesion in the alveolar and small-airway walls, so under the mechanical stretch of breathing the tissue tears into basal, subpleural cysts that rupture as pneumothorax.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — FLCN keeps cells stuck together: the protein helps maintain the adherens junctions linking epithelial and endothelial cells, and its loss loosens these contacts — a shared thread behind the syndrome's lung cysts and hypervascular kidney tumors.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The polyps are not confined to the colon: beyond its debated colorectal risk, BHD can stud the stomach and upper GI tract with polyps, part of the FLCN-driven overgrowth that surfaces across many epithelia.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — BHD is autosomal dominant: a single germline FLCN mutation passes to half of a carrier's children, so diagnosis triggers cascade genetic testing of relatives and the option of preimplantation or prenatal testing to keep the kidney and lung risk from reaching the next generation.
- `connects-to` → **[Basal Cell Carcinoma](../basal-cell-carcinoma/README.md)** — BHD's facial papules mimic skin cancer: its fibrofolliculomas are benign hair-follicle hamartomas that can be mistaken clinically for basal cell carcinoma, so a biopsy distinguishing the two is what often first points to the underlying FLCN syndrome.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — BHD's kidney surgery costs red cells: repeated nephron-sparing resections of its recurrent renal tumors, and the loss of functioning kidney tissue that makes erythropoietin, can leave carriers anemic over a lifetime of tumor surveillance and surgery.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — FLCN reaches the pigment cells too: Birt-Hogg-Dubé carries a reported increased risk of melanoma, reflecting folliculin's role beyond the kidney and lung in the skin's melanocytes.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Losing FLCN releases the cell cycle: unrestrained mTOR signaling raises cyclin D1 to drive the proliferation behind BHD's hamartomas and renal tumors, the growth engine downstream of folliculin loss.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — It sits among the hamartoma-and-cancer syndromes: like Peutz-Jeghers, BHD is a single-gene disorder that sprouts benign hamartomas (here hair-follicle and lung) alongside a raised risk of specific cancers.
- `connects-to` → **[COPD](../copd/README.md)** — BHD's lung cysts mimic emphysema: its basal pulmonary cysts and recurrent spontaneous pneumothoraces can be mistaken for COPD on imaging, but lung function is usually preserved — the distinction matters because BHD signals hereditary kidney-cancer risk.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Folliculin shapes TGF-β signaling: FLCN loss in BHD dysregulates the TGF-β pathway, contributing to the abnormal cell differentiation behind its fibrofolliculomas, lung cysts, and renal tumors.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Renal tumors accumulate a second hit: beyond the germline FLCN loss, secondary TP53 mutations are found in BHD-associated chromophobe and oncocytic renal carcinomas, marking progression toward malignancy.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Lost folliculin lifts a brake on NF-κB: FLCN normally restrains inflammatory and mTOR-linked signaling, so its loss in BHD engages NF-κB-driven survival pathways that support the syndrome's tumors.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — FLCN-deficient cells activate STAT3: the chromophobe and oncocytic renal tumors of BHD show STAT3 signaling that supports their proliferation, one of the pathways downstream of folliculin loss.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Saving the kidneys costs nephrons over a lifetime: recurrent BHD renal tumors demand repeated nephron-sparing surgeries, so the cumulative loss of kidney tissue can drift toward chronic kidney disease.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Its renal tumors drag the count down: the recurrent renal cell carcinomas of BHD bring tumor inflammation and surgical nephron loss that, with reduced erythropoietin, contribute an anemia of chronic disease.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Repeated cancer surgery raises the clot risk: the lifetime of renal-tumor resections and the prothrombotic state of renal cell carcinoma predispose BHD patients to perioperative venous thromboembolism.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Lifelong cancer surveillance weighs on the mind: living with an inherited risk of renal tumors, recurrent surgeries and the threat of spontaneous lung collapse imposes a real psychological burden in BHD.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its lung cysts can harbor mold: the thin-walled pulmonary cysts of Birt-Hogg-Dubé create air spaces where inhaled Aspergillus can colonize and form an aspergilloma.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Recurrent pneumothorax and surgery invite infection: repeated chest-tube drainage and pleurodesis for collapsing lungs, plus nephron-sparing renal-tumor surgery, carry a cumulative risk of serious infection and sepsis.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Unpredictable lung collapse breeds worry: the threat of a sudden spontaneous pneumothorax and the constant renal-cancer surveillance of BHD foster chronic health anxiety.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — It demands repeated surgery that must heal: BHD brings recurrent nephron-sparing renal-tumour operations and pleurodesis or surgery for recurrent pneumothorax, leaving wounds to heal over a lifetime.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — FLCN loss seeds tumours beyond the kidney: BHD is associated with colonic polyps and parotid oncocytomas, extending its hamartoma-tumour spectrum into the digestive and salivary tract.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its gene sits in the metabolic pathway: FLCN regulates the AMPK-mTOR axis that governs cellular metabolism, and BHD shows associations with thyroid and parathyroid nodules.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — A lung collapse can crash the circulation: rupture of BHD lung cysts can cause a tension pneumothorax that shifts the mediastinum and obstructs venous return, producing obstructive shock and cardiac arrest.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its hamartomas reach soft tissue: BHD's tumour spectrum includes lipomas and angiolipomas among connective-tissue lesions beyond the skin, lung and kidney.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its gene tunes immune metabolism: FLCN regulates the mTOR/TFEB axis that also governs lysosomal function and immune-cell metabolism, the molecular hub underlying BHD's varied tumours.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — A fellow skin-led tumour syndrome: like Birt-Hogg-Dubé, NF1 is autosomal-dominant and announced by skin signs — café-au-lait macules and neurofibromas — that flag inherited tumour predisposition.
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — Another tumour-suppressor syndrome: NF2 joins Birt-Hogg-Dubé among inherited disorders where loss of a single tumour-suppressor gene drives characteristic tumours, here bilateral vestibular schwannomas.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — A comparator of inherited facial papules: Gorlin syndrome's multiple basal cell carcinomas enter the differential of Birt-Hogg-Dubé's fibrofolliculomas, both hereditary causes of numerous facial skin tumours.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Advanced kidney tumours need systemic drugs: the chromophobe and oncocytic renal cancers of Birt-Hogg-Dubé, when metastatic, are treated with mTOR and VEGFR-targeted agents reflecting their FLCN-mTOR biology.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — A fellow cause of inherited cystic lung disease: like Birt-Hogg-Dubé, DICER1 syndrome produces familial lung cysts prone to pneumothorax, so both demand awareness of cystic lung change in young patients.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — A shared lifetime of surveillance: like Carney complex, Birt-Hogg-Dubé commits carriers to lifelong multi-organ imaging surveillance, here annual renal MRI to catch its kidney tumours early.
- `connects-to` → **[Lung Slice](../../05-tissue/lung-slice/README.md)** — It riddles the lung with cysts: folliculin loss produces basal, subpleural lung cysts that rupture as recurrent spontaneous pneumothorax — often the first clue to Birt-Hogg-Dubé, seen as cystic change on a lung slice.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Its kidney tumours resist chemo: the chromophobe and hybrid oncocytic renal carcinomas of Birt-Hogg-Dubé are indolent and chemoresistant, managed by surveillance and nephron-sparing surgery rather than cytotoxic chemotherapy.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Less immunotherapy-responsive than clear cell: unlike VHL-driven clear-cell kidney cancer, the chromophobe/oncocytic tumours of Birt-Hogg-Dubé have low mutational burden and respond poorly to checkpoint blockade.
- `connects-to` → **[STK11](../../03-molecular/stk11/README.md)** — The energy-sensing axis: folliculin partners with AMPK and the LKB1/STK11 kinase to sense cellular energy, mechanistically linking Birt-Hogg-Dubé to the STK11-driven Peutz-Jeghers hamartoma syndrome.
- `connects-to` → **[ATP](../../03-molecular/atp/README.md)** — Mitochondria-packed oncocytes: folliculin loss dysregulates mitochondrial biogenesis, so BHD renal oncocytomas and hybrid tumours are crammed with mitochondria churning out ATP—the oncocytic phenotype.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Lifelong cancer surveillance: like Li-Fraumeni syndrome, Birt-Hogg-Dubé is an autosomal-dominant tumour-predisposition syndrome whose carriers need structured multi-organ screening from early adulthood.
- `connects-to` → **[Marfan Syndrome](../marfan-syndrome/README.md)** — Two genetic causes of spontaneous pneumothorax: Birt-Hogg-Dubé's basal lung cysts and Marfan syndrome's apical blebs both predispose to recurrent collapsed lung, reached by different structural routes.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — Cystic lung and air leaks: like cystic fibrosis, Birt-Hogg-Dubé produces a cystic lung architecture prone to recurrent pneumothorax, though its thin-walled basal cysts differ from CF's bronchiectasis.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — A debated colon link: some studies tie Birt-Hogg-Dubé to colorectal polyps and cancer through FLCN loss in the intestinal epithelium, though the association remains controversial.
- `connects-to` → **[TSC1-TSC2](../../03-molecular/tsc1-tsc2/README.md)** — mTOR convergence: FLCN and the TSC1-TSC2 complex both regulate mTORC1, and the two hamartoma syndromes share cystic lung disease and renal lesions, framing BHD as a sister mTOR-pathway disorder.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Hippo dysregulation: FLCN loss can deregulate the Hippo-YAP pathway, an additional driver implicated in the oncocytic and chromophobe renal tumours characteristic of Birt-Hogg-Dubé.
- `connects-to` → **[Pheochromocytoma-Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Pseudohypoxic overlap: like SDH- and VHL-driven pheochromocytoma-paraganglioma, FLCN-deficient BHD tumours show HIF-1α-driven pseudohypoxic, angiogenic signalling within the inherited renal/endocrine tumour spectrum.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — TFE3-driven MYC: FLCN loss in BHD releases the transcription factor TFE3 to the nucleus, where it upregulates MYC and the biosynthetic programme fuelling tumour growth.
- `connects-to` → **[NFE2L2](../../03-molecular/nfe2l2/README.md)** — Antioxidant reprogramming: FLCN-deficient BHD cells show constitutive NRF2 (NFE2L2) activation, driving the metabolic and antioxidant programme that supports their survival.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt dysregulation: FLCN loss perturbs Wnt/β-catenin signalling, an additional oncogenic pathway contributing to the renal tumours of Birt-Hogg-Dubé.
- `connects-to` → **[FoxO1](../../03-molecular/foxo1/README.md)** — Metabolic stress axis: the FLCN-FNIP-AMPK complex regulates FoxO transcription factors, so FLCN loss disturbs the FoxO-controlled oxidative-stress and metabolic programme of Birt-Hogg-Dubé cells.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MAPK in renal tumours: ERK/MAPK signalling is activated downstream of FLCN loss and contributes to the proliferation of the chromophobe and oncocytic renal tumours of Birt-Hogg-Dubé.
- `connects-to` → **[EGLN1](../../03-molecular/egln1/README.md)** — HIF metabolic shift: FLCN loss perturbs the EGLN1 (PHD2)-HIF axis, stabilising HIF to drive the glycolytic, Warburg-like metabolism characteristic of Birt-Hogg-Dubé renal tumours.
- `connects-to` → **[E-cadherin (CDH1)](../../03-molecular/cdh1/README.md)** — FLCN regulates E-cadherin-dependent cell-cell adhesion, and impaired adhesion in the alveolar wall underlies the lung cysts and recurrent spontaneous pneumothorax that are often the first clue to Birt-Hogg-Dubé syndrome.
- `connects-to` → **[SDHB](../../03-molecular/sdhb/README.md)** — FLCN loss boosts mitochondrial biogenesis, giving the oncocytic and chromophobe renal tumors of Birt-Hogg-Dubé a mitochondria-packed phenotype that parallels the mitochondria-rich renal tumors of SDH deficiency.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT reactivation maintains telomeres in the renal cell carcinomas that Birt-Hogg-Dubé predisposes to, granting the replicative immortality that lets the FLCN-deficient clone proliferate into the syndrome's hybrid oncocytic tumors.
- `connects-to` → **[FH](../../03-molecular/fh/README.md)** — Birt-Hogg-Dubé (FLCN) sits among the inherited renal-cancer syndromes alongside VHL, SDHB and fumarate-hydratase-driven HLRCC, each producing a characteristic histology—BHD the chromophobe and hybrid oncocytic tumors.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IGF-1R signaling, converging on the same AKT-mTOR axis dysregulated by folliculin loss, supports the proliferation of the renal tumors of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Folliculin loss disinhibits mTOR and suppresses caspase-3 apoptosis, so mTOR inhibitors restrain rather than kill BHD tumor cells—a cytostatic effect that mirrors their action in the related mTOR-driven hamartoma syndromes.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — FLCN loss in Birt-Hogg-Dubé dysregulates the PI3K-AKT-mTOR axis (AKT and mTOR already mapped), driving the renal tumors and skin lesions of the syndrome.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH governs hair-follicle development, and its dysregulation downstream of FLCN loss contributes to the fibrofolliculomas—hair-follicle hamartomas—that are the defining skin lesion of BHD.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Anti-apoptotic BCL-2 supports survival of the slow-growing renal tumors of Birt-Hogg-Dubé, complementing the mTOR-driven suppression of caspase-3 apoptosis already mapped.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — Oncometabolite-producing IDH mutations parallel the FH and SDHB metabolic lesions (both already mapped) within the spectrum of metabolically-driven hereditary renal tumors, where altered metabolites stabilize HIF and reprogram the epigenome.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — VEGF/PDGF-axis angiogenesis (VEGF already mapped) supports the renal tumors that Birt-Hogg-Dubé predisposes to and is the target of the tyrosine-kinase inhibitors used in renal cell carcinoma.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-MAPK signaling through ERK1/2 (already mapped) provides a proliferative input that cooperates with FLCN loss in driving the tumors of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — FLCN loss dysregulates HIF activity; HIF-2α (EPAS1) signaling links Birt-Hogg-Dubé syndrome to the hypoxia-driven renal tumorigenesis it shares with the VHL/MET hereditary-RCC differential (all mapped).
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is a marker and modulator of the renal tumors that arise in Birt-Hogg-Dubé syndrome.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 mapped) provides a proliferative and survival input cooperating with FLCN loss in Birt-Hogg-Dubé tumorigenesis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of the renal tumors that arise in Birt-Hogg-Dubé syndrome.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the connective-tissue and lung-cyst phenotypes (fibrofolliculomas, pulmonary cysts) of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — FLCN loss perturbs autophagy and mitochondrial quality control, and the resulting cytosolic DNA can engage cGAS-STING in the lesions of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D1 cell-cycle entry (cyclin-D1 already mapped) drives the proliferation of the renal tumors of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the renal tumors of Birt-Hogg-Dubé syndrome must evade.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β interacts with the AMPK-mTOR axis (AMPK and mTOR already mapped) that FLCN loss dysregulates in Birt-Hogg-Dubé syndrome.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the renal tumors of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of the tumors of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of MET and other receptor tyrosine kinases (MET already mapped) contributes to the survival signaling of the renal tumors of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation implicated in the tumorigenesis of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of the renal tumors of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the renal tumors of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the renal tumors of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of the renal tumors of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic reprogramming: folliculin loss dysregulates the AMPK energy sensor it partners with (AMPK already mapped) and the mTOR pathway, shifting cellular metabolism and mitochondrial biogenesis in a way that also links the syndrome to insulin-responsive energy handling.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Renal tumour invasion: the AXL receptor tyrosine kinase can drive epithelial-mesenchymal transition and invasion in the renal tumours of Birt-Hogg-Dubé, a signalling route relevant to the rare aggressive lesions beyond the usually indolent chromophobe and oncocytic tumours.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Antigen presentation: MHC class II-restricted T-cell responses shape immune surveillance of the renal tumours of Birt-Hogg-Dubé, relevant to immunotherapy of any that progress to a more aggressive renal cell carcinoma.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Renal immunotherapy: IL-2-driven T-cell responses underlie the immunotherapy of the rare aggressive renal cell carcinomas that can arise in Birt-Hogg-Dubé (MHC class II already mapped), the treatment reserved for tumours that progress.
- `connects-to` → **[T-cytotoxic cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immune surveillance: cytotoxic CD8 T cells provide the surveillance against the renal tumours of Birt-Hogg-Dubé (perforin already mapped), and their function is central to the checkpoint immunotherapy of any that become aggressive.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Metabolic oxidative stress: loss of the FLCN-AMPK-mTOR axis (already mapped) dysregulates cellular metabolism, and the resulting oxidative stress, to which xanthine oxidase contributes, is part of the tumour-promoting milieu in Birt-Hogg-Dubé cells.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the microenvironment of any aggressive Birt-Hogg-Dubé renal tumour dampens the anti-tumour T-cell response (PD-1 and CD8 already mapped), part of the immune evasion relevant to checkpoint immunotherapy.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the renal tumours of Birt-Hogg-Dubé, part of their stromal microenvironment.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Lipid metabolism: folliculin, through the AMPK-mTOR axis (already mapped), regulates cellular lipid and cholesterol metabolism, and its loss shifts the metabolic phenotype that contributes to tumour formation in Birt-Hogg-Dubé syndrome.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the renal tumours of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of the renal tumours in Birt-Hogg-Dubé syndrome.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Haematuria and anaemia: the renal tumours of Birt-Hogg-Dubé can bleed, causing the haematuria and iron-deficiency anaemia that reflect the systemic effects of the renal cancer beyond the tumour itself.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Folliculin energy metabolism: the FLCN-AMPK (already mapped) energy-sensing axis that folliculin regulates connects to the leptin adipokine signalling of the metabolic dimension of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — AMPK-activating adipokine: adiponectin, with leptin (already mapped), activates the AMPK (already mapped) energy metabolism that folliculin governs, part of the metabolic milieu of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the folliculin-AMPK (already mapped) energy metabolism of Birt-Hogg-Dubé syndrome.
- `connects-to` → **[VHL disease](../vhl-disease/README.md)** — Hereditary-RCC differential: Birt-Hogg-Dubé and the von Hippel-Lindau (VHL already mapped) syndromes are hereditary renal-tumour syndromes in the differential, distinguished by the FLCN versus VHL genes.
- `connects-to` → **[Tuberous sclerosis complex](../tuberous-sclerosis-complex/README.md)** — mTOR-pathway overlap: Birt-Hogg-Dubé and tuberous sclerosis are mTOR/AMPK (TSC1-TSC2 already mapped) hamartoma syndromes with renal and lung (cysts, LAM) involvement.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibrofolliculoma stroma: the fibrofolliculomas of Birt-Hogg-Dubé are benign hair-follicle tumours with a fibroblast/collagen (PDGF already mapped) stroma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity relevant to the renal tumours of Birt-Hogg-Dubé.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the Birt-Hogg-Dubé renal tumours.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the renal tumours of Birt-Hogg-Dubé.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the Birt-Hogg-Dubé renal tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the Birt-Hogg-Dubé tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of Birt-Hogg-Dubé.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^nickerson-2002-flcn-bhd]: Nickerson ML, Warren MB, Toro JR, et al. Mutations in a novel gene lead to kidney tumors, lung wall defects, and benign tumors of the hair follicle in patients with the Birt-Hogg-Dubé syndrome. *Cancer Cell.* 2002;2(2):157-164. [doi:10.1016/s1535-6108(02)00104-6](https://doi.org/10.1016/s1535-6108(02)00104-6) · [PubMed 12204536](https://pubmed.ncbi.nlm.nih.gov/12204536/)
[^tsun-2013-flcn-rag]: Tsun ZY, Bar-Peled L, Chantranupong L, et al. The folliculin tumor suppressor is a GAP for the RagC/D GTPases that signal amino acid levels to mTORC1. *Mol Cell.* 2013;52(4):495-505. [doi:10.1016/j.molcel.2013.09.016](https://doi.org/10.1016/j.molcel.2013.09.016) · [PubMed 24095279](https://pubmed.ncbi.nlm.nih.gov/24095279/)
