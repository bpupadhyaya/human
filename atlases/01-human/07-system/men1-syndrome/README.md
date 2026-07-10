---
schema: human-scale-entry/v1
id: men1-syndrome
name: MEN1 Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Multiple Endocrine Neoplasia type 1 (MEN1) is caused by germline MEN1 mutations; triad of parathyroid adenomas (>95%), pituitary adenomas (20-65%), and pancreatic NETs (30-80%); everolimus FDA-approved for pNETs; annual biochemical + MRI surveillance."
aliases: ["MEN1 syndrome", "multiple endocrine neoplasia type 1", "Wermer syndrome", "MEN type 1", "MEN-1", "hereditary pNET", "parathyroid-pituitary-pancreas syndrome", "MEN1 hereditary cancer"]
sources:
  - id: thakker-2012-men1-guidelines
    type: peer-reviewed
    cite: "Thakker RV, Newey PJ, Walls GV, et al. Clinical practice guidelines for multiple endocrine neoplasia type 1 (MEN1). J Clin Endocrinol Metab. 2012;97(9):2990-3011."
    doi: "10.1210/jc.2012-1174"
    pmid: "22392070"
    url: "https://doi.org/10.1210/jc.2012-1174"
  - id: chandrasekharappa-1997-men1
    type: peer-reviewed
    cite: "Chandrasekharappa SC, Guru SC, Manickam P, et al. Positional cloning of the gene for multiple endocrine neoplasia-type 1. Science. 1997;276(5311):404-407."
    doi: "10.1126/science.276.5311.404"
    pmid: "9103196"
    url: "https://doi.org/10.1126/science.276.5311.404"
cross_links:
  - target: 01-human/03-molecular/men1
    relation: connects-to
    note: "Germline MEN1 mutations cause MEN1 syndrome by haploinsufficiency; somatic second-hit (LOH at 11q13) confirms two-hit model; menin LOF depletes H3K4me3 at CDKN1B/CDKN2C → CDK4/6 activation → neuroendocrine proliferation."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Somatostatin analogs (octreotide LAR, lanreotide autogel) are first-line for functional MEN1-associated NETs; Ga-68 DOTATATE PET/CT is preferred for staging; SSTR2 expression guides peptide receptor radionuclide therapy (PRRT) eligibility."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "MEN1-associated pNETs are multifocal, arise earlier than sporadic NETs, and include functioning (insulinoma, gastrinoma) and non-functioning tumors; RADIANT-3 trial: everolimus (mTOR inhibitor) improved PFS from 4.6 to 11.0 months vs placebo in pNET."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "MEN1 pNETs are classified and treated as well-differentiated NETs, not PDAC; surgical threshold is >2 cm for non-functioning pNETs; CLARINET trial: lanreotide autogel extended PFS vs placebo (HR 0.47) in G1/G2 gastroenteropancreatic NETs."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Everolimus (mTOR inhibitor, RADIANT-3) improved PFS from 4.6 to 11.0 months vs placebo in advanced pNET; mTOR constitutively activated by menin LOF via CDK4/6 → mTORC1; everolimus FDA-approved for non-functioning progressive pNET; sunitinib is the alternative VEGFR/PDGFR option."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulinoma occurs in ~10-20% of MEN1; autonomous insulin → hypoglycemia (Whipple's triad); often multifocal, small (<2 cm); diazoxide suppresses insulin secretion; EUS is most sensitive for small insulinoma localization; everolimus is anti-secretory in MEN1 insulinoma."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Prolactinoma is the most common pituitary adenoma in MEN1 (~60% of pituitary lesions); hyperprolactinaemia → hypogonadism + galactorrhea; cabergoline/bromocriptine first-line; MEN1 prolactinomas are more cabergoline-resistant; transsphenoidal surgery for resistant cases."
  - target: 01-human/07-system/men4-syndrome
    relation: connects-to
    note: "MEN1 and MEN4 are clinically near-identical multiple endocrine neoplasia syndromes — both cause parathyroid, pituitary, and pancreatic neuroendocrine tumors — but differ in gene: MEN1 from menin loss, MEN4 from CDKN1B/p27 loss; CDKN1B testing follows a negative MEN1 result."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Primary hyperparathyroidism is the earliest and most penetrant MEN1 manifestation (~95% by age 50): menin loss drives multigland parathyroid hyperplasia → excess PTH → hypercalcemia, kidney stones, and bone loss; subtotal parathyroidectomy is standard as all glands are at risk."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The pancreas is the most dangerous MEN1 site: multifocal pancreatic neuroendocrine tumors — gastrinomas (Zollinger-Ellison), insulinomas, non-functioning pNETs — arise young and are the leading cause of MEN1 mortality; surveillance MRI and a >2 cm surgical threshold guide care."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "MEN1 and Carney complex are both hereditary multiple-endocrine-neoplasia syndromes with different drivers: MEN1 (menin loss) gives parathyroid, islet and pituitary tumors; Carney (PRKAR1A/PKA) adds cardiac myxomas, skin pigmentation and PPNAD, with overlapping pituitary disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "MEN1 is the archetypal disease of the endocrine system as a network: a single menin mutation simultaneously transforms the parathyroids, pancreatic islets and anterior pituitary (the '3 Ps'), showing how one tumor-suppressor's loss dysregulates multiple endocrine glands at once."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Pituitary adenomas are one of MEN1's three core tumors and frequently disturb growth hormone: GH-secreting somatotroph adenomas cause acromegaly, while prolactinomas are the commonest MEN1 pituitary tumor—so IGF-1/GH and prolactin screening is part of MEN1 surveillance."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "MEN1 and pheochromocytoma belong to the inherited endocrine-tumor syndromes but rarely overlap: MEN1's parathyroid, pancreatic and pituitary tumors contrast with the adrenal-medullary catecholamine tumors of MEN2 and VHL—so a pheochromocytoma points away from MEN1."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "MEN1 and von Hippel-Lindau are both dominant tumor-suppressor syndromes causing multi-organ tumors: MEN1 gives parathyroid, islet and pituitary tumors, while VHL gives pheochromocytoma, renal cancer and pancreatic NETs—overlapping in the pancreas, differing elsewhere."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal gland is a frequent but often silent MEN1 target: up to 40% of MEN1 patients develop adrenal cortical enlargement or adenomas, usually nonfunctioning, so surveillance imaging covers the adrenals even though parathyroid, pancreatic and pituitary tumors dominate."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Thyroid tumors occur in MEN1 beyond the classic three glands: while parathyroid, pituitary and pancreas dominate, menin loss also predisposes to thyroid adenomas and carcinoma, so the syndrome's reach extends across endocrine organs—warranting broad surveillance."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cushing's syndrome arises in MEN1 from two routes: ACTH-secreting pituitary tumors or adrenal/ectopic neuroendocrine tumors raise cortisol, so hypercortisolism in a MEN1 patient demands working out whether the pituitary, adrenal or a pancreatic NET is the source."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Primary hyperparathyroidism—MEN1's earliest, commonest feature—drives bone loss: excess PTH from multigland parathyroid tumors pulls calcium from bone, causing osteoporosis and stones, so early parathyroidectomy protects the skeleton in MEN1."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "MEN1 strikes the digestive system with neuroendocrine tumors: duodenopancreatic NETs—especially gastrinomas causing Zollinger-Ellison ulcers and insulinomas—are leading causes of morbidity, so menin loss makes the gut's hormone cells a major tumor site."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "MEN1 promotes gastric carcinoid tumors: gastrinoma-driven acid and hypergastrinemia stimulate stomach enterochromaffin-like cells into type-2 gastric carcinoids, so the stomach is a downstream target of the syndrome's hormone excess."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "MEN1 also shows in the skin: menin loss produces facial angiofibromas, collagenomas and lipomas in many patients, so these benign cutaneous tumors can be an accessible clue to an inherited multiple-endocrine-neoplasia syndrome."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Primary hyperparathyroidism is the hallmark of MEN1: nearly all carriers develop parathyroid hyperplasia that floods the blood with PTH, raising calcium—usually the first and most penetrant manifestation, prompting calcium and PTH screening from adolescence."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "MEN1 can grow an aggressive thymic neuroendocrine tumor: this thymic carcinoid, seen mostly in male smokers with MEN1, is a leading cause of MEN1 death, so chest imaging is part of surveillance even though the tumor is rare."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "MEN1's excess PTH drives osteoclasts: chronic hyperparathyroidism activates these bone-resorbing cells, leaching calcium from the skeleton toward osteoporosis and fractures—part of why correcting the parathyroid disease protects bone."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "MEN1's overactive parathyroids punish the kidney: near-universal primary hyperparathyroidism floods the blood with calcium, which precipitates as kidney stones and nephrocalcinosis—often the first clue that prompts genetic testing for the syndrome."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "MEN1 can grow a glucagon-secreting pancreatic tumor: glucagonomas raise blood sugar and cause a classic migrating rash and weight loss, one of several functional islet tumors—alongside insulinoma and gastrinoma—that define the syndrome."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "MEN1's deadliest turn is pancreatic NET spread to the liver: islet tumors metastasize among the hepatocytes, and this liver burden, not the hormone excess, is the leading cause of death—driving aggressive surveillance and resection."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "MEN1's earliest sign disturbs phosphate: the primary hyperparathyroidism that usually comes first floods the body with PTH, which dumps phosphate into the urine while raising calcium, so low phosphate with high calcium is a classic early clue."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Overactive parathyroids in MEN1 erode bone via osteoblasts: relentless PTH drives bone remodeling, uncoupling osteoblasts and osteoclasts so resorption wins, contributing to the osteoporosis these patients develop young."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "MEN1's pancreatic neuroendocrine tumors are highly vascular through VEGF: they recruit dense blood vessels, which is why antiangiogenic drugs like sunitinib that block VEGF signaling are used against advanced disease."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "MEN1 floods the stomach with acid: its gastrinomas pour out gastrin that drives parietal cells to secrete hydrogen ions, causing the severe, multiple ulcers of Zollinger-Ellison syndrome."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "MEN1's gastrinomas often hide in the small intestine: the duodenum is a common site for these neuroendocrine tumors, so the upper small bowel is searched carefully in Zollinger-Ellison workups."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "MEN1's neuroendocrine tumors are vessel-dense: built around proliferating endothelial cells, they light up as hypervascular 'blushes' on contrast imaging, a feature used to find the small pancreatic and duodenal tumors."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Finding MEN1's many small tumors depends on photons: sestamibi scintigraphy hunts parathyroids, Ga-68 DOTATATE PET lights up neuroendocrine tumors via their somatostatin receptors, and pituitary MRI completes the surveillance triad."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "MEN1 pituitary somatotroph adenomas cause acromegaly, and IGF-1 is the test that catches it: liver-made in proportion to growth hormone, its steady blood level screens for and tracks GH excess better than the pulsatile hormone itself."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver decides MEN1's prognosis: pancreatic and duodenal neuroendocrine tumors metastasize there, and the bulk of liver disease — not the primary tumor — is the leading cause of death in these patients."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy marks MEN1's tumors as neuroendocrine: the pancreatic and pituitary growths fill with dense-core secretory granules, packets of hormone whose ultrastructure identifies cells built to signal through the blood."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "MEN1 leaves clues on the skin: multiple facial angiofibromas, trunk collagenomas, and lipomas dot these patients, cutaneous markers that can prompt the genetic testing uncovering the syndrome."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Overactive parathyroids erode the bone: MEN1's near-universal hyperparathyroidism drives osteoclasts to resorb bone into osteitis fibrosa with brown tumors, hollowing the marrow-bearing skeleton."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies prove the tumors are neuroendocrine: chromogranin A and synaptophysin stains confirm MEN1's pancreatic and pituitary NETs on biopsy, and Ki-67 antibody staining grades how fast they divide and how aggressively to treat."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The foregut NETs reach the chest: bronchial carcinoids are part of the MEN1 spectrum, slow-growing lung neuroendocrine tumors that join the thymic and gastric carcinoids these patients are screened for over a lifetime."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "MEN1 quietly raises breast risk: women carrying a menin mutation develop breast cancer earlier and more often than the general population, an association now folding earlier mammographic screening into their surveillance."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Primary hyperparathyroidism is MEN1's earliest and commonest sign: overactive parathyroid glands push PTH and calcium up while disturbing vitamin D handling, the mineral derangement that drives the kidney stones and bone loss surveillance aims to catch."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "MEN1 passes down half the family and unsettles the reproductive axis: it is autosomal dominant so each child has a 50% risk, prompting cascade testing, while a prolactin-secreting pituitary tumor can disrupt periods and fertility."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Menin is a transcriptional scaffold that touches Wnt: beyond its MLL-histone-methylation role, menin modulates beta-catenin signaling in endocrine cells, so losing it helps unleash the proliferation behind MEN1's parathyroid and islet tumors."
  - target: 01-human/03-molecular/cdkn1b
    relation: connects-to
    note: "Menin works partly through a cell-cycle brake: it drives expression of CDKN1B (p27), so losing menin lowers p27 and lets endocrine cells divide — and germline CDKN1B mutations produce MEN4, a near-twin syndrome that helped reveal this pathway."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "The pancreatic gastrinomas reach the stomach: their relentless acid drives Zollinger-Ellison ulcers, while the high gastrin also stimulates gastric ECL cells into carcinoid tumors — so a duodeno-pancreatic tumor in MEN1 can seed neoplasia in the stomach wall."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "The tumor risk reaches the meninges: beyond its endocrine triad, menin loss raises the incidence of meningiomas and other central-nervous-system tumors, part of the broad neoplastic predisposition that follows losing this tumor-suppressor scaffold."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "MEN1 marks the skin with fibrous tumors: collagenomas and facial angiofibromas — fibroblast-and-collagen proliferations — are common cutaneous clues that, with lipomas, help flag the syndrome before the endocrine tumors declare themselves."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Calcitonin separates MEN1 from MEN2: the calcitonin-secreting medullary thyroid carcinoma that defines MEN2 is absent in MEN1, so a normal calcitonin and the parathyroid-pituitary-pancreas pattern point away from a RET syndrome."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "It shares the endocrine-tumor neighborhood: like neurofibromatosis type 1 — which carries pheochromocytoma and duodenal neuroendocrine tumors — MEN1 is a single-gene syndrome predisposing to endocrine neoplasia, distinguished by its gene and tumor pattern."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Menin loss reshapes transcriptional signaling: the menin scaffold normally tunes gene expression, and its loss in MEN1 tumors engages STAT3 among the pathways that drive neuroendocrine-cell proliferation."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Menin sits in the chromatin-writing machinery: it anchors the MLL histone-methyltransferase complex, and its loss disturbs the balance with the opposing EZH2/PRC2 mark, an epigenetic dysregulation behind MEN1 tumors."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Overactive parathyroids scar the kidneys: the primary hyperparathyroidism that is MEN1's commonest feature drives hypercalcemia, kidney stones and nephrocalcinosis that can erode renal function into chronic kidney disease."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Its pancreatic tumors derange glucose: MEN1 glucagonomas and somatostatinomas raise blood sugar, and the pancreatic surgery its tumors require removes islet tissue, together causing a secondary diabetes."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A lifetime of cancer surgery raises the clot risk: the repeated operations for MEN1's pancreatic, parathyroid and pituitary tumors, plus the hypercoagulability of its neuroendocrine cancers, predispose to venous thromboembolism."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Hormones and hereditary burden weigh on mood: Cushing's from a pituitary tumor, the psychiatric effects of hypercalcemia, and lifelong multi-tumor surveillance give MEN1 a substantial burden of depression."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Its hormone-secreting tumors raise blood pressure: the primary hyperparathyroidism, pituitary Cushing's and functioning neuroendocrine tumors of MEN1 each contribute to secondary hypertension."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Recurrent endocrine surgery taxes healing: the repeated parathyroid, pancreatic and pituitary operations MEN1 demands leave patients with multiple surgical wounds to heal over a lifetime."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong multi-organ surveillance breeds worry: the constant biochemical and imaging screening for the many tumors of MEN1, and the hereditary burden, foster chronic health anxiety."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its hyperparathyroidism stones the kidneys: primary hyperparathyroidism, the commonest MEN1 feature, raises calcium and causes recurrent kidney stones and nephrocalcinosis that threaten renal function."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its pituitary tumours press on the brain: MEN1 pituitary adenomas can grow to compress the optic chiasm and cavernous sinus, causing visual-field loss, headache and cranial-nerve palsies."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Parathyroid excess dissolves bone: the chronic hyperparathyroidism of MEN1 drives osteoclastic bone resorption toward osteitis fibrosa and fragility, beyond the osteoporosis it causes."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It seeds neuroendocrine tumours in the lungs: bronchial carcinoid tumours are part of MEN1, adding to its gastroenteropancreatic and thymic neuroendocrine neoplasms."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its high calcium unsettles the heart: chronic hypercalcaemia from hyperparathyroidism shortens the QT interval and can cause arrhythmias and hypertension."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It grows aggressive tumours in the thymus: thymic carcinoid tumours, arising in this lymphoid organ, are a leading cause of death in MEN1, especially in men."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Its pancreatic tumours get targeted drugs: mTOR inhibitors such as everolimus and the kinase inhibitor sunitinib treat the pancreatic neuroendocrine tumours of MEN1, exploiting the menin-mTOR axis."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "It causes ulcers without the usual culprit: MEN1 gastrinomas drive Zollinger-Ellison syndrome with severe peptic ulcers that, unlike common ulcers, are not due to Helicobacter pylori."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "A fellow mTOR-driven tumour syndrome: like tuberous sclerosis, MEN1 produces pancreatic neuroendocrine tumours that respond to mTOR inhibition, sharing that therapeutic axis."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "Its pancreatic tumours arise here: MEN1 predisposes to islet-cell neuroendocrine tumours — gastrinomas, insulinomas and others — that secrete hormones and dominate its morbidity alongside hyperparathyroidism."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "A fellow endocrine-tumour syndrome: like Cowden syndrome, MEN1 is an inherited predisposition to multiple endocrine and other tumours, both driving lifelong gland surveillance."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "Among the autosomal-dominant tumour syndromes: MEN1 sits with HLRCC and the other single-gene cancer-predisposition syndromes, each committing carriers to organ-specific tumour surveillance."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Overactive parathyroids dissolve the bone: primary hyperparathyroidism, the earliest and commonest MEN1 tumour, raises PTH that resorbs cortical bone—producing osteitis fibrosa, subperiosteal erosions and osteoporosis—so bone density tracks the parathyroid disease."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for advanced neuroendocrine tumours: when MEN1 pancreatic neuroendocrine tumours or thymic carcinoids progress, regimens like streptozocin-based or temozolomide-capecitabine chemotherapy are used alongside somatostatin analogues and targeted drugs."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The pituitary completes its triad: MEN1's third classic site is the anterior pituitary, where prolactinomas and growth-hormone or ACTH adenomas grow at the skull base, demanding brain imaging in surveillance alongside the parathyroid and pancreas."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Hypercalcaemia injures the kidney: MEN1's primary hyperparathyroidism—its commonest feature—raises calcium, causing kidney stones and nephrocalcinosis that scar the glomerulus and tubules."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Two germline endocrine-tumour syndromes: MEN1 and DICER1 both predispose to pituitary and other endocrine tumours under autosomal-dominant control, demanding lifelong multi-gland surveillance."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Zollinger-Ellison and peptic ulcers: gastrinomas in MEN1 flood the gut with gastrin, driving refractory, multiple peptic ulcers that erode the intestinal epithelium."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Carcinoid hormone: the foregut, thymic and bronchial carcinoids of MEN1 can secrete serotonin, and once they metastasise the hormone overflow produces the flushing and diarrhoea of carcinoid syndrome."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Where the tumours turn lethal: the pancreatic and duodenal neuroendocrine tumours of MEN1 metastasise preferentially to the liver, and this hepatic spread through the lobule is the leading cause of death in the syndrome."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "Carcinoid heart disease: serotonin from liver-metastatic MEN1 carcinoids deposits fibrous plaque on the right-sided heart valves and endocardium, scarring them into the tricuspid and pulmonary lesions of carcinoid heart disease."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Derepressed proliferation: loss of menin removes its restraint on cyclin D1, driving the cell-cycle entry of the parathyroid, pancreatic and pituitary tumours of MEN1."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-mTOR target: PI3K-AKT-mTOR signalling is active in MEN1 pancreatic neuroendocrine tumours, the rationale for everolimus therapy in advanced disease."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Angiogenic neuroendocrine tumours: HIF-1α-driven, VEGF-rich angiogenesis makes MEN1 neuroendocrine tumours highly vascular, underpinning the use of anti-angiogenic agents like sunitinib."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Menin-MLL target: menin normally restrains MYC-driven transcription, so MEN1 loss derepresses MYC, contributing to the proliferation of its endocrine tumours."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: with cyclin D1 upregulated, CDK4/6 propels MEN1 endocrine tumour cells through the G1 checkpoint, a rationale for CDK4/6 inhibition."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: TERT reactivation maintains telomeres in MEN1-associated neuroendocrine tumours, sustaining their proliferation."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Prolactinoma therapy: dopamine agonists are first-line for the prolactin-secreting pituitary adenomas of MEN1, exploiting dopamine's tonic inhibition of pituitary prolactin release."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Gastrinoma acid: the gastrinomas of MEN1 drive gastrin-stimulated histamine release from ECL cells, causing the gastric acid hypersecretion and ulcers of Zollinger-Ellison syndrome."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Hyperparathyroid bone loss: primary hyperparathyroidism, the commonest MEN1 manifestation, drives PTH-stimulated RANKL-mediated osteoclast activity that resorbs bone."
  - target: 01-human/03-molecular/cdkn1a
    relation: connects-to
    note: "Menin-regulated cell-cycle brake: menin transcriptionally activates the CDK inhibitors p21 (CDKN1A) and p27, so MEN1 loss removes these brakes on proliferation in the endocrine cells that form the syndrome's tumours."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO interaction: menin interacts with FOXO transcription factors to restrain endocrine-cell proliferation, an antiproliferative axis lost when the MEN1 tumour suppressor is inactivated."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β co-factor: menin potentiates TGF-β/SMAD growth-suppressive signalling, so MEN1 loss disables this antiproliferative pathway in parathyroid, pituitary and pancreatic endocrine cells."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Primary hyperparathyroidism: parathyroid tumours causing hypercalcaemia from excess PTH are the earliest and most penetrant manifestation of MEN1, affecting nearly all carriers by mid-adulthood and often the first clue that prompts genetic testing."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenetic tumour suppression: menin scaffolds the MLL histone-methyltransferase complexes and influences DNA methylation, so MEN1 loss disrupts the epigenetic regulation of growth-control genes — a mechanism shared with the menin-MLL dependence targeted in leukaemia."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Breast-cancer risk: women with MEN1 carry an increased risk of breast cancer, an oestrogen-responsive tumour added to the parathyroid, pancreatic and pituitary triad, extending surveillance beyond the classic endocrine organs."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "pNET growth axis: the PI3K-AKT-mTOR pathway (AKT and mTOR already mapped) drives the pancreatic neuroendocrine tumours of MEN1, the basis for the mTOR inhibitor everolimus in their treatment."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle release: menin normally restrains the cell cycle via the CDK inhibitors p21 and p27 (CDKN1A and CDKN1B mapped); its loss frees the CDK4/6-cyclin-D1-RB-E2F1 axis in MEN1 endocrine tumours."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Proliferative MAPK: growth-factor-driven RAS-MAPK-ERK signalling promotes the proliferation of the parathyroid, pancreatic and pituitary tumours of MEN1, complementing the PI3K and cell-cycle pathways."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "NET angiogenesis: the VEGF/PDGF angiogenic axis (VEGF already mapped) supports the vascular pancreatic neuroendocrine tumours of MEN1 and is targeted by the multikinase inhibitors (sunitinib) used to treat them."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "mTOR pathway: PTEN loss releases the PI3K-AKT-mTOR axis (AKT, PIK3CA and mTOR already mapped) that drives MEN1 neuroendocrine tumours and is targeted therapeutically by everolimus."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint: the RB1-E2F checkpoint (CDKN1B, CDK4/6 and cyclin-D1 already mapped) restrains proliferation, and its dysregulation contributes to the neuroendocrine tumourigenesis of MEN1."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is a marker and modulator of the neuroendocrine and parathyroid tumours arising in MEN1 syndrome."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT3 signalling (STAT3 mapped) provides a proliferative input to the endocrine tumours of MEN1 syndrome."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Menin interacts with TGF-β-SMAD signalling (SMAD4 mapped), and disruption of this growth-suppressive pathway contributes to MEN1 tumorigenesis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune microenvironment of the neuroendocrine tumours that arise in MEN1 syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory microenvironment of the MEN1-driven endocrine tumours."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Menin regulates Notch signalling, and its loss perturbs the Notch-dependent differentiation of the endocrine cells transformed in MEN1 syndrome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and survival signaling co-opted by menin loss in MEN1-syndrome tumors."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation restrains apoptosis in the endocrine tumors of MEN1 syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is the immune clearance that the multiple neuroendocrine tumors of MEN1 syndrome must evade."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative signaling of the endocrine tumors of MEN1 syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of the neuroendocrine tumors of MEN1 syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the menin-deficient endocrine tumor cells of MEN1 syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the endocrine tumors of multiple endocrine neoplasia type 1."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of multiple endocrine neoplasia type 1."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape (interacting with the menin-MLL histone-methyltransferase complex) of multiple endocrine neoplasia type 1."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the neuroendocrine tumors of MEN1 syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of MEN1 syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of MEN1 syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of the neuroendocrine neoplasms of MEN1 syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of MEN1 syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of MEN1 syndrome."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Gastrinoma acid hypersecretion: the gastrinomas of MEN1 (Zollinger-Ellison syndrome) drive massive gastric acid (proton) secretion, causing the refractory multiple peptic ulcers controlled with high-dose proton-pump inhibitors."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Insulinoma hypoglycaemia: the insulinomas of MEN1 oversecrete insulin (already mapped), which acting through the insulin receptor drives the fasting hypoglycaemia that is a classic functional pancreatic-tumour presentation."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Carcinoid heart disease: serotonin-secreting foregut and thymic neuroendocrine tumours in MEN1 (serotonin already mapped) can cause carcinoid heart disease with valvular fibrosis, and troponin marks the associated myocardial strain."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "Ectopic Cushing: neuroendocrine tumours in MEN1 can secrete ACTH ectopically, driving cortisol excess (already mapped) and Cushing syndrome, one of the functional hormone syndromes of its pancreatic and thymic tumours."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Adrenal adenomas: the adrenocortical tumours of MEN1 can oversecrete aldosterone, causing primary aldosteronism with hypertension and hypokalaemia, part of the adrenal component of the syndrome beyond the classic three glands."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with the strongly expressed VEGF (already mapped) supports the rich vasculature of the neuroendocrine tumours of MEN1, part of the angiogenic biology targeted by antiangiogenic and mTOR (already mapped) therapy."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Mineral dysregulation: the primary hyperparathyroidism of MEN1 (PTH and calcium already mapped) disturbs magnesium alongside calcium handling, part of the mineral derangement of the commonest manifestation of the syndrome."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Enteroinsular tumours: GLP-1 and the incretin axis reflect the enteropancreatic neuroendocrine biology of the MEN1 pancreatic tumours (insulin and glucagon already mapped), and GLP-1-secreting tumours are a rare functional subtype."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the microenvironment of the MEN1 neuroendocrine tumours dampens the anti-tumour immune response, part of the immune biology relevant to any immunotherapy of the aggressive metastatic tumours."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the MEN1 neuroendocrine tumours."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the MEN1 neuroendocrine tumours."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Islet zinc: zinc is stored with insulin (already mapped) in the islet secretory granules, and the zinc-insulin hexamer is part of the biology of the insulinomas and other pancreatic neuroendocrine tumours of MEN1."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Steroidogenesis substrate: cholesterol is the precursor of the cortisol and aldosterone (already mapped) of the adrenocortical (adrenal already mapped) tumours that occur in MEN1."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Islet-tumour metabolic adipokine: leptin reflects the metabolic disturbance of the insulinoma and glucagonoma (insulin and glucagon already mapped) and the endocrine tumours of MEN1."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic disturbance of the pancreatic-islet and endocrine tumours of MEN1."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the metabolic disturbance of the islet and endocrine tumours of MEN1."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "NET immunosurveillance: the cytotoxic T cells (perforin already mapped) provide the immune surveillance of the pancreatic and other neuroendocrine tumours of MEN1."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon and NETs: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway and historically used to treat the neuroendocrine tumours, is part of the innate-immune dimension of MEN1."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 immunosurveillance: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunosurveillance of the neuroendocrine tumours of MEN1."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the MEN1 neuroendocrine tumours."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the MEN1 tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the MEN1 neuroendocrine tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the MEN1 tumours."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the MEN1 neuroendocrine tumours."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the MEN1 neuroendocrine tumours."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the macrophages are a dominant myeloid population of the stroma of the well-vascularised (VEGF already mapped) MEN1 neuroendocrine tumours."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the MEN1 neuroendocrine tumour stroma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuroendocrine stroma alarmin: TSLP from the MEN1 pancreatic tumour stroma (pNETs) activates dendritic cells (already mapped) and shapes the immunological response in the neuroendocrine-tumour (already mapped) microenvironment of MEN1 pancreatic neoplasms."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Neuroendocrine tumour complement: complement C5 (with C3 already mapped) drives complement-dependent cytotoxicity against the neuroendocrine tumours of MEN1; C5a–C5aR1 signalling recruits myeloid cells into the pNET and parathyroid adenoma stroma of MEN1 syndrome."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Hormonal syndrome vasomotor: bradykinin contributes to the flushing and diarrhoea of the VIPoma and carcinoid-like syndromes of MEN1 neuroendocrine tumours; kinin-kallikrein activation (via VIP and somatostatin already mapped) amplifies the vasomotor secretory responses of MEN1."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "MEN1 complement regulation: C1-INH controls the classical-pathway arm (C3, C5 and C5aR1 already mapped) of complement in MEN1 neuroendocrine tumour stroma, modulating cytotoxicity against islet-of-Langerhans (already mapped) and pituitary neoplastic cells."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroendocrine EPO signalling: erythropoietin receptor (EPOR) on MEN1 neuroendocrine tumour cells activates JAK2/STAT3 (already mapped) pro-survival signalling, complementing the VHL (already mapped) and mTOR (already mapped) pathway dysregulation in MEN1 tumour progression."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Desmoplastic stroma: periostin, secreted by fibroblasts (already mapped) in MEN1 neuroendocrine tumour stroma, activates the integrin-AKT (already mapped) pathway and promotes tumour invasiveness across pancreatic (already mapped) and pulmonary neuroendocrine sites."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Neuroendocrine melatonin: melatonin, via MT1/MT2 receptors on MEN1 neuroendocrine tumour cells, suppresses cAMP-mediated (already mapped) proliferative signalling and promotes apoptosis in the pancreatic and pituitary (already mapped) neuroendocrine tumours of MEN1 syndrome."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-pituitary axis: testosterone, via androgen receptor on MEN1 pituitary adenoma cells (pituitary-adenoma already mapped) and hypothalamic-pituitary axis, modulates the prolactinoma and GH-secreting tumour (already mapped) development in MEN1 syndrome."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Pancreatic islet modulation: oxytocin, via OXT-R on pancreatic beta cells and MEN1 insulinoma cells (pancreatic-cancer and islet already mapped), modulates insulin secretion and amplifies the endocrine hyperactivity in the gastrinoma and insulinoma spectrum of MEN1."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "MEN1 vasopressin neuroendocrine: vasopressin, via V1bR on pituitary adenoma cells (already mapped) and macrophages (already mapped), modulates the hypothalamic-pituitary axis; dysregulation amplifies IL-6 (already mapped) and mTOR (already mapped) signalling in MEN1 syndrome."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "MEN1 selenium antioxidant: selenium, via GPx/TrxR selenoproteins in MEN1 neuroendocrine tumour cells and macrophages (already mapped), quenches oxidative stress that amplifies mTOR (already mapped) and VEGF (already mapped) pro-tumour angiogenesis in MEN1 syndrome."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "MEN1 iodine thyroid: iodine, as the key substrate for thyroid hormone biosynthesis, supports the HPT axis; iodine insufficiency amplifies the neuroendocrine IL-6 (already mapped) and mTOR (already mapped) tumour-promoting cascade in MEN1 syndrome."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "MEN1 sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of MEN1 syndrome."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "MEN1 potassium: potassium channels regulate macrophage (already mapped) and fibroblast (already mapped) function in the MEN1 tumour microenvironment; potassium depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of MEN1 syndrome."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "MEN1 copper: copper, as cofactor of SOD1 in macrophages (already mapped) and endothelial cells (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative tumour cascade of MEN1 syndrome."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "MEN1 iron: iron, via ferritin in macrophages (already mapped) and fibroblasts (already mapped), modulates redox balance in the MEN1 tumour microenvironment; iron dysregulation amplifies IL-6 (already mapped) and mTOR (already mapped) cascade of MEN1 syndrome."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "MEN1 chloride: chloride channels regulate macrophage (already mapped) and endothelial cell (already mapped) ion homeostasis in the MEN1 neuroendocrine microenvironment; chloride imbalance amplifies IL-6 (already mapped) and VEGF (already mapped) cascade."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "MEN1 sulfur: sulfur-containing amino acids in macrophages (already mapped) and fibroblasts (already mapped) maintain redox buffering; sulfur depletion amplifies IL-6 (already mapped) and mTOR (already mapped) pro-tumour cascade of MEN1 syndrome."
---

# MEN1 Syndrome

## Overview

**Multiple Endocrine Neoplasia type 1 (MEN1 syndrome)**, historically called Wermer syndrome, is an autosomal dominant hereditary cancer predisposition syndrome caused by germline pathogenic variants in the **MEN1** tumor suppressor gene (chromosome 11q13). MEN1 syndrome affects approximately **1 in 20,000-30,000** individuals and is characterized by the clinical triad of **parathyroid adenomas** (>95% penetrance), **anterior pituitary adenomas** (20-65% penetrance), and **gastroenteropancreatic neuroendocrine tumors** (GEP-NETs, 30-80% penetrance). An estimated 10% of cases arise from de novo germline mutations. MEN1 syndrome accounts for approximately 1-2% of primary hyperparathyroidism and a significant proportion of sporadic-appearing pNETs in young patients [^thakker-2012-men1-guidelines] [^chandrasekharappa-1997-men1].

**MEN1 syndrome penetrance by manifestation (cumulative by age 50):**

| Manifestation | Penetrance | Typical onset age |
|---|---|---|
| Parathyroid adenoma (pHPT) | >95% | 20-30 years |
| Gastrinoma / ZES | 40-50% | 25-35 years |
| Non-functioning pNET | 20-40% | 30-40 years |
| Insulinoma | 10-20% | 25-35 years |
| Anterior pituitary adenoma | 20-65% | 25-40 years |
| Adrenocortical tumor (non-functioning) | 20-40% | 30-50 years |
| Thymic NET | ~5-10% | 35-50 years |
| Bronchial carcinoid | ~5-10% | 35-50 years |
| Skin: angiofibroma, collagenoma | >80% | 20-40 years |

## Structure

### Genetic basis

- **Gene**: MEN1 (chromosome 11q13.1, 67 kb, 10 exons)
- **Inheritance**: autosomal dominant; 50% offspring risk from carrier parent
- **De novo rate**: ~10% of index cases
- **Mutation spectrum**: ~1,000 unique germline variants catalogued in the MEN1 database; frameshift/nonsense (~45%), missense (~35%), splice (~10%), large deletions (~10%)
- **Hotspot**: no single hotspot mutation; each family tends to have a private variant; codon 83 and exon 2 are disproportionately affected
- **Genotype-phenotype correlation**: weak; same mutation within a family can produce highly variable expression; modifier genes and somatic events drive phenotype
- **Somatic second hit**: LOH at 11q13 (most common); small deletion; rarely a second point mutation

### Parathyroid disease

Primary hyperparathyroidism (pHPT) is the **first and most common** manifestation. MEN1-associated pHPT is multiglandular (all four glands eventually involved) and distinct from sporadic adenoma (typically single gland):
- Biochemical: elevated serum calcium + elevated or inappropriately normal intact PTH
- Histology: multiple adenomas (earliest) progressing to four-gland hyperplasia (later); carcinoma is rare (<1%)
- Consequences: nephrolithiasis (most common), nephrocalcinosis, osteoporosis, neuropsychiatric symptoms (fatigue, depression), GI (constipation)
- Treatment: **3.5-gland parathyroidectomy** (subtotal) with cryopreservation of remnant, or **total parathyroidectomy with autotransplantation** to forearm; intraoperative PTH monitoring; recurrence rate ~50% at 10 years (vs <5% for sporadic adenoma); cinacalcet (calcimimetic) for medical management or post-operative recurrence

### Pancreatic/duodenal NETs (GEP-NETs)

**Gastrinoma / Zollinger-Ellison syndrome (ZES):**
Most common functional GEP-NET in MEN1; 60-90% arise in the duodenum (tiny microgastrinomas, 1-3 mm), not the pancreas; duodenal gastrinomas may metastasize to regional lymph nodes despite tiny primary size; ZES: gastric acid hypersecretion → peptic ulcers resistant to standard doses + diarrhea; treatment: high-dose PPI (omeprazole 40-60 mg BID) controls acid; surgical cure less common in MEN1-associated ZES than sporadic due to multifocality

**Insulinoma:**
- Second most common functional pNET; hypoglycemia (Whipple's triad: symptoms + glucose <55 mg/dL + relief with glucose)
- Often multifocal in MEN1; typically small (<2 cm) when symptomatic
- Localization: EUS (endoscopic ultrasound) most sensitive for small insulinomas; ⁶⁸Ga-DOTATATE PET less sensitive than EUS for insulinoma (lower SSTR2 expression)
- Treatment: diazoxide (K-ATP channel opener, suppresses insulin secretion) for inoperable; surgical enucleation for localized; everolimus (RADIANT-3) has anti-secretory effect on insulinoma

**Non-functioning pNETs (NF-pNETs):**
- Most common pNET overall; detected incidentally or by surveillance imaging
- Risk of malignancy correlates with size: >2 cm → 25-35% risk of metastasis → surgical resection recommended; <2 cm with stable growth → surveillance with annual MRI
- MEN1 pNETs generally well-differentiated (G1-G2); G3 NETs rare

**VIPoma, glucagonoma, somatostatinoma**: rare in MEN1 (<5% each); VIPoma → watery diarrhea/hypokalemia; glucagonoma → necrolytic migratory erythema, diabetes

### Pituitary tumors

- Prolactinoma (most common, ~60% of MEN1 pituitary adenomas): prolactin ↑ → hypogonadism, galactorrhea; treatment: dopamine agonists (cabergoline, bromocriptine); resistance in MEN1-associated prolactinomas is higher than sporadic
- Somatotroph adenoma (GH-secreting, ~25%): acromegaly; treatment: somatostatin analogs (octreotide LAR, lanreotide autogel), cabergoline, pegvisomant (GH receptor antagonist), transsphenoidal surgery, radiotherapy
- Corticotroph adenoma (ACTH-secreting, ~5%): Cushing disease; transsphenoidal surgery; ketoconazole/osilodrostat for medical management
- Non-functioning (gonadotroph, ~10%): detected by mass effect; visual field defects; transsphenoidal decompression

### Other manifestations

- **Adrenocortical tumors**: 20-40% of MEN1 patients; usually non-functioning; cortical adenoma or hyperplasia; rarely adrenocortical carcinoma (~2%); biochemical screen (DHEA-S, UFC, midnight cortisol, aldosterone/renin ratio)
- **Thymic NET**: most lethal MEN1 manifestation in some series; strongly male-predominant (M:F 4:1); smoking increases risk; prophylactic thymectomy at parathyroid surgery debated; surveillance: CT chest annually
- **Bronchial carcinoid**: less aggressive than thymic; female predominant; surveillance: CT chest/MRI annually
- **Skin**: facial angiofibromas (94%, pathognomonic for MEN1 in multiples), truncal collagenomas (72%), café-au-lait macules, lipomas; angiofibromas precede endocrine manifestations by years
- **Meningioma**: ~8% in some series; spinal ependymoma reported

## Function

### Disease mechanism

Menin haploinsufficiency (one functional allele) creates susceptibility: cells appear normal until the remaining wild-type MEN1 allele undergoes somatic second hit (LOH at 11q13). Biallelic MEN1 LOF → complete menin loss → H3K4me3 depletion at CDKN1B (p27) and CDKN2C (p18) promoters → CDK4/6 activation → Rb phosphorylation → E2F release → cell cycle entry → proliferation in neuroendocrine-lineage cells. Parathyroid chief cells, pituitary lactotrophs/somatotrophs, and islet β-cells/δ-cells are particularly dependent on menin for p27/p18-mediated G1 arrest.

### Distinguishing MEN1 from MEN2/MEN4

| Feature | MEN1 (Wermer) | MEN2A (Sipple) | MEN2B | MEN4 |
|---|---|---|---|---|
| Gene | MEN1 (11q13) | RET (10q11) | RET (10q11) | CDKN1B (12p13) |
| Parathyroid | >95% | 20-30% | Rare | Parathyroid tumor |
| Pituitary | 20-65% | Absent | Absent | Pituitary adenoma |
| Pancreatic NET | 30-80% | Absent | Absent | Rare |
| Thyroid | Absent | Medullary Ca (>95%) | Medullary Ca (>95%) | Absent |
| Pheochromocytoma | Absent | 50% | 50% | Absent |
| Treatment paradigm | Menin pathway | RET kinase inhibitors | RET kinase inhibitors | CDK inhibitors |

## Pathology

### Surveillance protocol (Thakker 2012 guidelines)

**Biochemical (annual from age 8-10 in gene carriers):**
- Ionized calcium + intact PTH (parathyroid)
- Fasting gastrin (gastrinoma screen); if abnormal: secretin stimulation test
- Fasting insulin/glucose (insulinoma screen)
- Chromogranin A (NF-pNET marker; ↑ = tumor burden)
- Prolactin, IGF-1/GH (pituitary)
- DHEA-S, 24h urinary free cortisol (adrenal)
- Glucagon, VIP (if symptoms suggest)

**Imaging:**
- **MRI abdomen** (preferred over CT to avoid radiation): every 1-3 years; pNET detection; liver metastasis
- **EUS (endoscopic ultrasound)**: most sensitive for small pNETs and duodenal gastrinomas; every 1-2 years
- **⁶⁸Ga-DOTATATE PET/CT**: superior functional imaging for SSTR2-positive NETs; preferred over ¹¹¹In-octreotide SPECT; staging at diagnosis of functioning NET or NF-pNET >1 cm
- **MRI pituitary** (gadolinium): at diagnosis + every 3-5 years or if symptoms
- **CT chest**: annual for thymic/bronchial carcinoid surveillance

### Surgical indications

- **Parathyroid**: symptomatic pHPT (stones, osteoporosis, calcium >1 mg/dL above normal); 3.5-gland resection or total + autotransplant
- **pNET**: NF-pNET >2 cm (resection); functioning pNET (insulinoma/glucagonoma) regardless of size; gastrinoma: surgical cure less achievable due to multifocality; pancreaticoduodenectomy (Whipple) debated for duodenal microgastrinomas
- **Pituitary**: visual field compromise; cabergoline failure for prolactinoma; transsphenoidal surgery

## Connections

- `connects-to` → **[MEN1](../../03-molecular/men1/README.md)** — Germline MEN1 mutations cause MEN1 syndrome by haploinsufficiency; somatic second-hit (LOH at 11q13) confirms two-hit model; menin LOF depletes H3K4me3 at CDKN1B/CDKN2C → CDK4/6 activation → neuroendocrine proliferation.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — Somatostatin analogs (octreotide LAR, lanreotide autogel) are first-line for functional MEN1-associated NETs; Ga-68 DOTATATE PET/CT is preferred for staging; SSTR2 expression guides peptide receptor radionuclide therapy (PRRT) eligibility.
- `connects-to` → **[Neuroendocrine Tumors](../../07-system/neuroendocrine-tumors/README.md)** — MEN1-associated pNETs are multifocal, arise earlier than sporadic NETs, and include functioning (insulinoma, gastrinoma) and non-functioning tumors; RADIANT-3 trial: everolimus (mTOR inhibitor) improved PFS from 4.6 to 11.0 months vs placebo in pNET.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — MEN1 pNETs are classified and treated as well-differentiated NETs, not PDAC; surgical threshold is >2 cm for non-functioning pNETs; CLARINET trial: lanreotide autogel extended PFS vs placebo (HR 0.47) in G1/G2 gastroenteropancreatic NETs.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Everolimus (mTOR inhibitor, RADIANT-3) improved PFS from 4.6 to 11.0 months vs placebo in advanced pNET; mTOR constitutively activated by menin LOF via CDK4/6 → mTORC1; everolimus FDA-approved for non-functioning progressive pNET; sunitinib is the alternative VEGFR/PDGFR option.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulinoma occurs in ~10-20% of MEN1; autonomous insulin → hypoglycemia (Whipple's triad); often multifocal, small (<2 cm); diazoxide suppresses insulin secretion; EUS is most sensitive for small insulinoma localization; everolimus is anti-secretory in MEN1 insulinoma.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Prolactinoma is the most common pituitary adenoma in MEN1 (~60% of pituitary lesions); hyperprolactinaemia → hypogonadism + galactorrhea; cabergoline/bromocriptine first-line; MEN1 prolactinomas are more cabergoline-resistant; transsphenoidal surgery for resistant cases.
- `connects-to` → **[MEN4 Syndrome](../men4-syndrome/README.md)** — MEN1 and MEN4 are clinically near-identical multiple endocrine neoplasia syndromes — both cause parathyroid, pituitary, and pancreatic neuroendocrine tumors — but differ in gene: MEN1 from menin loss, MEN4 from CDKN1B/p27 loss; CDKN1B testing follows a negative MEN1 result.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Primary hyperparathyroidism is the earliest and most penetrant MEN1 manifestation (~95% by age 50): menin loss drives multigland parathyroid hyperplasia → excess PTH → hypercalcemia, kidney stones, and bone loss; subtotal parathyroidectomy is standard as all glands are at risk.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The pancreas is the most dangerous MEN1 site: multifocal pancreatic neuroendocrine tumors — gastrinomas (Zollinger-Ellison), insulinomas, non-functioning pNETs — arise young and are the leading cause of MEN1 mortality; surveillance MRI and a >2 cm surgical threshold guide care.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — MEN1 and Carney complex are both hereditary multiple-endocrine-neoplasia syndromes with different drivers: MEN1 (menin loss) gives parathyroid, islet and pituitary tumors; Carney (PRKAR1A/PKA) adds cardiac myxomas, skin pigmentation and PPNAD, with overlapping pituitary disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — MEN1 is the archetypal disease of the endocrine system as a network: a single menin mutation simultaneously transforms the parathyroids, pancreatic islets and anterior pituitary (the '3 Ps'), showing how one tumor-suppressor's loss dysregulates multiple endocrine glands at once.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Pituitary adenomas are one of MEN1's three core tumors and frequently disturb growth hormone: GH-secreting somatotroph adenomas cause acromegaly, while prolactinomas are the commonest MEN1 pituitary tumor—so IGF-1/GH and prolactin screening is part of MEN1 surveillance.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — MEN1 and pheochromocytoma belong to the inherited endocrine-tumor syndromes but rarely overlap: MEN1's parathyroid, pancreatic and pituitary tumors contrast with the adrenal-medullary catecholamine tumors of MEN2 and VHL—so a pheochromocytoma points away from MEN1.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — MEN1 and von Hippel-Lindau are both dominant tumor-suppressor syndromes causing multi-organ tumors: MEN1 gives parathyroid, islet and pituitary tumors, while VHL gives pheochromocytoma, renal cancer and pancreatic NETs—overlapping in the pancreas, differing elsewhere.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal gland is a frequent but often silent MEN1 target: up to 40% of MEN1 patients develop adrenal cortical enlargement or adenomas, usually nonfunctioning, so surveillance imaging covers the adrenals even though parathyroid, pancreatic and pituitary tumors dominate.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Thyroid tumors occur in MEN1 beyond the classic three glands: while parathyroid, pituitary and pancreas dominate, menin loss also predisposes to thyroid adenomas and carcinoma, so the syndrome's reach extends across endocrine organs—warranting broad surveillance.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cushing's syndrome arises in MEN1 from two routes: ACTH-secreting pituitary tumors or adrenal/ectopic neuroendocrine tumors raise cortisol, so hypercortisolism in a MEN1 patient demands working out whether the pituitary, adrenal or a pancreatic NET is the source.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Primary hyperparathyroidism—MEN1's earliest, commonest feature—drives bone loss: excess PTH from multigland parathyroid tumors pulls calcium from bone, causing osteoporosis and stones, so early parathyroidectomy protects the skeleton in MEN1.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — MEN1 strikes the digestive system with neuroendocrine tumors: duodenopancreatic NETs—especially gastrinomas causing Zollinger-Ellison ulcers and insulinomas—are leading causes of morbidity, so menin loss makes the gut's hormone cells a major tumor site.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — MEN1 promotes gastric carcinoid tumors: gastrinoma-driven acid and hypergastrinemia stimulate stomach enterochromaffin-like cells into type-2 gastric carcinoids, so the stomach is a downstream target of the syndrome's hormone excess.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — MEN1 also shows in the skin: menin loss produces facial angiofibromas, collagenomas and lipomas in many patients, so these benign cutaneous tumors can be an accessible clue to an inherited multiple-endocrine-neoplasia syndrome.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Primary hyperparathyroidism is the hallmark of MEN1: nearly all carriers develop parathyroid hyperplasia that floods the blood with PTH, raising calcium—usually the first and most penetrant manifestation, prompting calcium and PTH screening from adolescence.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — MEN1 can grow an aggressive thymic neuroendocrine tumor: this thymic carcinoid, seen mostly in male smokers with MEN1, is a leading cause of MEN1 death, so chest imaging is part of surveillance even though the tumor is rare.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — MEN1's excess PTH drives osteoclasts: chronic hyperparathyroidism activates these bone-resorbing cells, leaching calcium from the skeleton toward osteoporosis and fractures—part of why correcting the parathyroid disease protects bone.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — MEN1's overactive parathyroids punish the kidney: near-universal primary hyperparathyroidism floods the blood with calcium, which precipitates as kidney stones and nephrocalcinosis—often the first clue that prompts genetic testing for the syndrome.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — MEN1 can grow a glucagon-secreting pancreatic tumor: glucagonomas raise blood sugar and cause a classic migrating rash and weight loss, one of several functional islet tumors—alongside insulinoma and gastrinoma—that define the syndrome.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — MEN1's deadliest turn is pancreatic NET spread to the liver: islet tumors metastasize among the hepatocytes, and this liver burden, not the hormone excess, is the leading cause of death—driving aggressive surveillance and resection.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — MEN1's earliest sign disturbs phosphate: the primary hyperparathyroidism that usually comes first floods the body with PTH, which dumps phosphate into the urine while raising calcium, so low phosphate with high calcium is a classic early clue.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Overactive parathyroids in MEN1 erode bone via osteoblasts: relentless PTH drives bone remodeling, uncoupling osteoblasts and osteoclasts so resorption wins, contributing to the osteoporosis these patients develop young.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — MEN1's pancreatic neuroendocrine tumors are highly vascular through VEGF: they recruit dense blood vessels, which is why antiangiogenic drugs like sunitinib that block VEGF signaling are used against advanced disease.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — MEN1 floods the stomach with acid: its gastrinomas pour out gastrin that drives parietal cells to secrete hydrogen ions, causing the severe, multiple ulcers of Zollinger-Ellison syndrome.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — MEN1's gastrinomas often hide in the small intestine: the duodenum is a common site for these neuroendocrine tumors, so the upper small bowel is searched carefully in Zollinger-Ellison workups.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — MEN1's neuroendocrine tumors are vessel-dense: built around proliferating endothelial cells, they light up as hypervascular 'blushes' on contrast imaging, a feature used to find the small pancreatic and duodenal tumors.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Finding MEN1's many small tumors depends on photons: sestamibi scintigraphy hunts parathyroids, Ga-68 DOTATATE PET lights up neuroendocrine tumors via their somatostatin receptors, and pituitary MRI completes the surveillance triad.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — MEN1 pituitary somatotroph adenomas cause acromegaly, and IGF-1 is the test that catches it: liver-made in proportion to growth hormone, its steady blood level screens for and tracks GH excess better than the pulsatile hormone itself.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver decides MEN1's prognosis: pancreatic and duodenal neuroendocrine tumors metastasize there, and the bulk of liver disease — not the primary tumor — is the leading cause of death in these patients.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy marks MEN1's tumors as neuroendocrine: the pancreatic and pituitary growths fill with dense-core secretory granules, packets of hormone whose ultrastructure identifies cells built to signal through the blood.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — MEN1 leaves clues on the skin: multiple facial angiofibromas, trunk collagenomas, and lipomas dot these patients, cutaneous markers that can prompt the genetic testing uncovering the syndrome.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Overactive parathyroids erode the bone: MEN1's near-universal hyperparathyroidism drives osteoclasts to resorb bone into osteitis fibrosa with brown tumors, hollowing the marrow-bearing skeleton.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies prove the tumors are neuroendocrine: chromogranin A and synaptophysin stains confirm MEN1's pancreatic and pituitary NETs on biopsy, and Ki-67 antibody staining grades how fast they divide and how aggressively to treat.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The foregut NETs reach the chest: bronchial carcinoids are part of the MEN1 spectrum, slow-growing lung neuroendocrine tumors that join the thymic and gastric carcinoids these patients are screened for over a lifetime.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — MEN1 quietly raises breast risk: women carrying a menin mutation develop breast cancer earlier and more often than the general population, an association now folding earlier mammographic screening into their surveillance.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Primary hyperparathyroidism is MEN1's earliest and commonest sign: overactive parathyroid glands push PTH and calcium up while disturbing vitamin D handling, the mineral derangement that drives the kidney stones and bone loss surveillance aims to catch.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — MEN1 passes down half the family and unsettles the reproductive axis: it is autosomal dominant so each child has a 50% risk, prompting cascade testing, while a prolactin-secreting pituitary tumor can disrupt periods and fertility.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Menin is a transcriptional scaffold that touches Wnt: beyond its MLL-histone-methylation role, menin modulates beta-catenin signaling in endocrine cells, so losing it helps unleash the proliferation behind MEN1's parathyroid and islet tumors.
- `connects-to` → **[CDKN1B](../../03-molecular/cdkn1b/README.md)** — Menin works partly through a cell-cycle brake: it drives expression of CDKN1B (p27), so losing menin lowers p27 and lets endocrine cells divide — and germline CDKN1B mutations produce MEN4, a near-twin syndrome that helped reveal this pathway.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — The pancreatic gastrinomas reach the stomach: their relentless acid drives Zollinger-Ellison ulcers, while the high gastrin also stimulates gastric ECL cells into carcinoid tumors — so a duodeno-pancreatic tumor in MEN1 can seed neoplasia in the stomach wall.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — The tumor risk reaches the meninges: beyond its endocrine triad, menin loss raises the incidence of meningiomas and other central-nervous-system tumors, part of the broad neoplastic predisposition that follows losing this tumor-suppressor scaffold.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — MEN1 marks the skin with fibrous tumors: collagenomas and facial angiofibromas — fibroblast-and-collagen proliferations — are common cutaneous clues that, with lipomas, help flag the syndrome before the endocrine tumors declare themselves.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Calcitonin separates MEN1 from MEN2: the calcitonin-secreting medullary thyroid carcinoma that defines MEN2 is absent in MEN1, so a normal calcitonin and the parathyroid-pituitary-pancreas pattern point away from a RET syndrome.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — It shares the endocrine-tumor neighborhood: like neurofibromatosis type 1 — which carries pheochromocytoma and duodenal neuroendocrine tumors — MEN1 is a single-gene syndrome predisposing to endocrine neoplasia, distinguished by its gene and tumor pattern.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Menin loss reshapes transcriptional signaling: the menin scaffold normally tunes gene expression, and its loss in MEN1 tumors engages STAT3 among the pathways that drive neuroendocrine-cell proliferation.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Menin sits in the chromatin-writing machinery: it anchors the MLL histone-methyltransferase complex, and its loss disturbs the balance with the opposing EZH2/PRC2 mark, an epigenetic dysregulation behind MEN1 tumors.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Overactive parathyroids scar the kidneys: the primary hyperparathyroidism that is MEN1's commonest feature drives hypercalcemia, kidney stones and nephrocalcinosis that can erode renal function into chronic kidney disease.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Its pancreatic tumors derange glucose: MEN1 glucagonomas and somatostatinomas raise blood sugar, and the pancreatic surgery its tumors require removes islet tissue, together causing a secondary diabetes.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A lifetime of cancer surgery raises the clot risk: the repeated operations for MEN1's pancreatic, parathyroid and pituitary tumors, plus the hypercoagulability of its neuroendocrine cancers, predispose to venous thromboembolism.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Hormones and hereditary burden weigh on mood: Cushing's from a pituitary tumor, the psychiatric effects of hypercalcemia, and lifelong multi-tumor surveillance give MEN1 a substantial burden of depression.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Its hormone-secreting tumors raise blood pressure: the primary hyperparathyroidism, pituitary Cushing's and functioning neuroendocrine tumors of MEN1 each contribute to secondary hypertension.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Recurrent endocrine surgery taxes healing: the repeated parathyroid, pancreatic and pituitary operations MEN1 demands leave patients with multiple surgical wounds to heal over a lifetime.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong multi-organ surveillance breeds worry: the constant biochemical and imaging screening for the many tumors of MEN1, and the hereditary burden, foster chronic health anxiety.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its hyperparathyroidism stones the kidneys: primary hyperparathyroidism, the commonest MEN1 feature, raises calcium and causes recurrent kidney stones and nephrocalcinosis that threaten renal function.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its pituitary tumours press on the brain: MEN1 pituitary adenomas can grow to compress the optic chiasm and cavernous sinus, causing visual-field loss, headache and cranial-nerve palsies.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Parathyroid excess dissolves bone: the chronic hyperparathyroidism of MEN1 drives osteoclastic bone resorption toward osteitis fibrosa and fragility, beyond the osteoporosis it causes.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It seeds neuroendocrine tumours in the lungs: bronchial carcinoid tumours are part of MEN1, adding to its gastroenteropancreatic and thymic neuroendocrine neoplasms.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its high calcium unsettles the heart: chronic hypercalcaemia from hyperparathyroidism shortens the QT interval and can cause arrhythmias and hypertension.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It grows aggressive tumours in the thymus: thymic carcinoid tumours, arising in this lymphoid organ, are a leading cause of death in MEN1, especially in men.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Its pancreatic tumours get targeted drugs: mTOR inhibitors such as everolimus and the kinase inhibitor sunitinib treat the pancreatic neuroendocrine tumours of MEN1, exploiting the menin-mTOR axis.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — It causes ulcers without the usual culprit: MEN1 gastrinomas drive Zollinger-Ellison syndrome with severe peptic ulcers that, unlike common ulcers, are not due to Helicobacter pylori.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — A fellow mTOR-driven tumour syndrome: like tuberous sclerosis, MEN1 produces pancreatic neuroendocrine tumours that respond to mTOR inhibition, sharing that therapeutic axis.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — Its pancreatic tumours arise here: MEN1 predisposes to islet-cell neuroendocrine tumours — gastrinomas, insulinomas and others — that secrete hormones and dominate its morbidity alongside hyperparathyroidism.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — A fellow endocrine-tumour syndrome: like Cowden syndrome, MEN1 is an inherited predisposition to multiple endocrine and other tumours, both driving lifelong gland surveillance.
- `connects-to` → **[HLRCC](../hlrcc/README.md)** — Among the autosomal-dominant tumour syndromes: MEN1 sits with HLRCC and the other single-gene cancer-predisposition syndromes, each committing carriers to organ-specific tumour surveillance.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Overactive parathyroids dissolve the bone: primary hyperparathyroidism, the earliest and commonest MEN1 tumour, raises PTH that resorbs cortical bone—producing osteitis fibrosa, subperiosteal erosions and osteoporosis—so bone density tracks the parathyroid disease.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for advanced neuroendocrine tumours: when MEN1 pancreatic neuroendocrine tumours or thymic carcinoids progress, regimens like streptozocin-based or temozolomide-capecitabine chemotherapy are used alongside somatostatin analogues and targeted drugs.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The pituitary completes its triad: MEN1's third classic site is the anterior pituitary, where prolactinomas and growth-hormone or ACTH adenomas grow at the skull base, demanding brain imaging in surveillance alongside the parathyroid and pancreas.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Hypercalcaemia injures the kidney: MEN1's primary hyperparathyroidism—its commonest feature—raises calcium, causing kidney stones and nephrocalcinosis that scar the glomerulus and tubules.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Two germline endocrine-tumour syndromes: MEN1 and DICER1 both predispose to pituitary and other endocrine tumours under autosomal-dominant control, demanding lifelong multi-gland surveillance.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Zollinger-Ellison and peptic ulcers: gastrinomas in MEN1 flood the gut with gastrin, driving refractory, multiple peptic ulcers that erode the intestinal epithelium.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Carcinoid hormone: the foregut, thymic and bronchial carcinoids of MEN1 can secrete serotonin, and once they metastasise the hormone overflow produces the flushing and diarrhoea of carcinoid syndrome.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Where the tumours turn lethal: the pancreatic and duodenal neuroendocrine tumours of MEN1 metastasise preferentially to the liver, and this hepatic spread through the lobule is the leading cause of death in the syndrome.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — Carcinoid heart disease: serotonin from liver-metastatic MEN1 carcinoids deposits fibrous plaque on the right-sided heart valves and endocardium, scarring them into the tricuspid and pulmonary lesions of carcinoid heart disease.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Derepressed proliferation: loss of menin removes its restraint on cyclin D1, driving the cell-cycle entry of the parathyroid, pancreatic and pituitary tumours of MEN1.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-mTOR target: PI3K-AKT-mTOR signalling is active in MEN1 pancreatic neuroendocrine tumours, the rationale for everolimus therapy in advanced disease.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Angiogenic neuroendocrine tumours: HIF-1α-driven, VEGF-rich angiogenesis makes MEN1 neuroendocrine tumours highly vascular, underpinning the use of anti-angiogenic agents like sunitinib.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Menin-MLL target: menin normally restrains MYC-driven transcription, so MEN1 loss derepresses MYC, contributing to the proliferation of its endocrine tumours.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: with cyclin D1 upregulated, CDK4/6 propels MEN1 endocrine tumour cells through the G1 checkpoint, a rationale for CDK4/6 inhibition.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: TERT reactivation maintains telomeres in MEN1-associated neuroendocrine tumours, sustaining their proliferation.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Prolactinoma therapy: dopamine agonists are first-line for the prolactin-secreting pituitary adenomas of MEN1, exploiting dopamine's tonic inhibition of pituitary prolactin release.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Gastrinoma acid: the gastrinomas of MEN1 drive gastrin-stimulated histamine release from ECL cells, causing the gastric acid hypersecretion and ulcers of Zollinger-Ellison syndrome.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Hyperparathyroid bone loss: primary hyperparathyroidism, the commonest MEN1 manifestation, drives PTH-stimulated RANKL-mediated osteoclast activity that resorbs bone.
- `connects-to` → **[p21 (CDKN1A)](../../03-molecular/cdkn1a/README.md)** — Menin transcriptionally activates the CDK inhibitors p21 and p27, so MEN1 loss removes these cell-cycle brakes in the endocrine cells that form the parathyroid, pituitary, and pancreatic tumors of the syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — Menin interacts with FOXO transcription factors to restrain endocrine-cell proliferation, an antiproliferative axis lost when the MEN1 tumor suppressor is inactivated and the endocrine glands become tumor-prone.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Menin potentiates TGF-β/SMAD growth-suppressive signaling, so MEN1 loss disables this antiproliferative pathway in parathyroid, pituitary, and pancreatic endocrine cells—one of the tumor-suppressor functions of menin.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Parathyroid tumors causing hypercalcemia from excess PTH are the earliest and most penetrant manifestation of MEN1, affecting nearly all carriers by mid-adulthood and often the first clue that prompts genetic testing.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Menin scaffolds the MLL histone-methyltransferase complexes and influences DNA methylation, so MEN1 loss disrupts the epigenetic regulation of growth-control genes—a mechanism shared with the menin-MLL dependence targeted in leukemia.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Women with MEN1 carry an increased risk of breast cancer, an estrogen-responsive tumor added to the parathyroid, pancreatic and pituitary triad, extending surveillance beyond the classic endocrine organs.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — The PI3K-AKT-mTOR pathway (AKT and mTOR already mapped) drives the pancreatic neuroendocrine tumors of MEN1, the basis for the mTOR inhibitor everolimus in their treatment.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Menin normally restrains the cell cycle via the CDK inhibitors p21 and p27 (CDKN1A and CDKN1B mapped); its loss frees the CDK4/6-cyclin-D1-RB-E2F1 axis in MEN1 endocrine tumors.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Growth-factor-driven RAS-MAPK-ERK signaling promotes the proliferation of the parathyroid, pancreatic and pituitary tumors of MEN1, complementing the PI3K and cell-cycle pathways.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — The VEGF/PDGF angiogenic axis (VEGF already mapped) supports the vascular pancreatic neuroendocrine tumors of MEN1 and is targeted by the multikinase inhibitors (sunitinib) used to treat them.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss releases the PI3K-AKT-mTOR axis (AKT, PIK3CA and mTOR already mapped) that drives MEN1 neuroendocrine tumors and is targeted therapeutically by everolimus.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (CDKN1B, CDK4/6 and cyclin-D1 already mapped) restrains proliferation, and its dysregulation contributes to the neuroendocrine tumorigenesis of MEN1.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is a marker and modulator of the neuroendocrine and parathyroid tumors arising in MEN1 syndrome.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 mapped) provides a proliferative input to the endocrine tumors of MEN1 syndrome.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Menin interacts with TGF-β-SMAD signaling (SMAD4 mapped), and disruption of this growth-suppressive pathway contributes to MEN1 tumorigenesis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune microenvironment of the neuroendocrine tumors that arise in MEN1 syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory microenvironment of the MEN1-driven endocrine tumors.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — Menin regulates Notch signaling, and its loss perturbs the Notch-dependent differentiation of the endocrine cells transformed in MEN1 syndrome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and survival signaling co-opted by menin loss in MEN1-syndrome tumors.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation restrains apoptosis in the endocrine tumors of MEN1 syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is the immune clearance that the multiple neuroendocrine tumors of MEN1 syndrome must evade.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative signaling of the endocrine tumors of MEN1 syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of the neuroendocrine tumors of MEN1 syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the menin-deficient endocrine tumor cells of MEN1 syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the endocrine tumors of multiple endocrine neoplasia type 1.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of multiple endocrine neoplasia type 1.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape (interacting with the menin-MLL histone-methyltransferase complex) of multiple endocrine neoplasia type 1.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the neuroendocrine tumors of MEN1 syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of MEN1 syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of MEN1 syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of the neuroendocrine neoplasms of MEN1 syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of MEN1 syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of MEN1 syndrome.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Gastrinoma acid hypersecretion: the gastrinomas of MEN1 (Zollinger-Ellison syndrome) drive massive gastric acid (proton) secretion, causing the refractory multiple peptic ulcers controlled with high-dose proton-pump inhibitors.
- `connects-to` → **[Insulin receptor](../../03-molecular/insulin-receptor/README.md)** — Insulinoma hypoglycaemia: the insulinomas of MEN1 oversecrete insulin (already mapped), which acting through the insulin receptor drives the fasting hypoglycaemia that is a classic functional pancreatic-tumour presentation.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Carcinoid heart disease: serotonin-secreting foregut and thymic neuroendocrine tumours in MEN1 (serotonin already mapped) can cause carcinoid heart disease with valvular fibrosis, and troponin marks the associated myocardial strain.
- `connects-to` → **[ACTH](../../03-molecular/acth/README.md)** — Ectopic Cushing: neuroendocrine tumours in MEN1 can secrete ACTH ectopically, driving cortisol excess (already mapped) and Cushing syndrome, one of the functional hormone syndromes of its pancreatic and thymic tumours.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Adrenal adenomas: the adrenocortical tumours of MEN1 can oversecrete aldosterone, causing primary aldosteronism with hypertension and hypokalaemia, part of the adrenal component of the syndrome beyond the classic three glands.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with the strongly expressed VEGF (already mapped) supports the rich vasculature of the neuroendocrine tumours of MEN1, part of the angiogenic biology targeted by antiangiogenic and mTOR (already mapped) therapy.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Mineral dysregulation: the primary hyperparathyroidism of MEN1 (PTH and calcium already mapped) disturbs magnesium alongside calcium handling, part of the mineral derangement of the commonest manifestation of the syndrome.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Enteroinsular tumours: GLP-1 and the incretin axis reflect the enteropancreatic neuroendocrine biology of the MEN1 pancreatic tumours (insulin and glucagon already mapped), and GLP-1-secreting tumours are a rare functional subtype.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the microenvironment of the MEN1 neuroendocrine tumours dampens the anti-tumour immune response, part of the immune biology relevant to any immunotherapy of the aggressive metastatic tumours.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the MEN1 neuroendocrine tumours.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the MEN1 neuroendocrine tumours.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Islet zinc: zinc is stored with insulin (already mapped) in the islet secretory granules, and the zinc-insulin hexamer is part of the biology of the insulinomas and other pancreatic neuroendocrine tumours of MEN1.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Steroidogenesis substrate: cholesterol is the precursor of the cortisol and aldosterone (already mapped) of the adrenocortical (adrenal already mapped) tumours that occur in MEN1.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Islet-tumour metabolic adipokine: leptin reflects the metabolic disturbance of the insulinoma and glucagonoma (insulin and glucagon already mapped) and the endocrine tumours of MEN1.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic disturbance of the pancreatic-islet and endocrine tumours of MEN1.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the metabolic disturbance of the islet and endocrine tumours of MEN1.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — NET immunosurveillance: the cytotoxic T cells (perforin already mapped) provide the immune surveillance of the pancreatic and other neuroendocrine tumours of MEN1.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon and NETs: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway and historically used to treat the neuroendocrine tumours, is part of the innate-immune dimension of MEN1.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 immunosurveillance: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunosurveillance of the neuroendocrine tumours of MEN1.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the MEN1 neuroendocrine tumours.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the MEN1 tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the MEN1 neuroendocrine tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the MEN1 tumours.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the MEN1 neuroendocrine tumours.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the MEN1 neuroendocrine tumours.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the macrophages are a dominant myeloid population of the stroma of the well-vascularised (VEGF already mapped) MEN1 neuroendocrine tumours.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the MEN1 neuroendocrine tumour stroma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuroendocrine stroma alarmin: TSLP from the MEN1 pancreatic tumour stroma (pNETs) activates dendritic cells (already mapped) and shapes the immunological response in the neuroendocrine-tumour (already mapped) microenvironment of MEN1 pancreatic neoplasms.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Neuroendocrine tumour complement: complement C5 (with C3 already mapped) drives complement-dependent cytotoxicity against the neuroendocrine tumours of MEN1; C5a–C5aR1 signalling recruits myeloid cells into the pNET and parathyroid adenoma stroma of MEN1 syndrome.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Hormonal syndrome vasomotor: bradykinin contributes to the flushing and diarrhoea of the VIPoma and carcinoid-like syndromes of MEN1 neuroendocrine tumours; kinin-kallikrein activation (via VIP and somatostatin already mapped) amplifies the vasomotor secretory responses of MEN1.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — MEN1 complement regulation: C1-INH controls the classical-pathway arm (C3, C5 and C5aR1 already mapped) of complement in MEN1 neuroendocrine tumour stroma, modulating cytotoxicity against islet-of-Langerhans (already mapped) and pituitary neoplastic cells.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroendocrine EPO signalling: erythropoietin receptor (EPOR) on MEN1 neuroendocrine tumour cells activates JAK2/STAT3 (already mapped) pro-survival signalling, complementing the VHL (already mapped) and mTOR (already mapped) pathway dysregulation in MEN1 tumour progression.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Desmoplastic stroma: periostin, secreted by fibroblasts (already mapped) in MEN1 neuroendocrine tumour stroma, activates the integrin-AKT (already mapped) pathway and promotes tumour invasiveness across pancreatic (already mapped) and pulmonary neuroendocrine sites.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Neuroendocrine melatonin: melatonin, via MT1/MT2 receptors on MEN1 neuroendocrine tumour cells, suppresses cAMP-mediated (already mapped) proliferative signalling and promotes apoptosis in the pancreatic and pituitary (already mapped) neuroendocrine tumours of MEN1 syndrome.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-pituitary axis: testosterone, via androgen receptor on MEN1 pituitary adenoma cells (pituitary-adenoma already mapped) and hypothalamic-pituitary axis, modulates the prolactinoma and GH-secreting tumour (already mapped) development in MEN1 syndrome.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Pancreatic islet modulation: oxytocin, via OXT-R on pancreatic beta cells and MEN1 insulinoma cells (pancreatic-cancer and islet already mapped), modulates insulin secretion and amplifies the endocrine hyperactivity in the gastrinoma and insulinoma spectrum of MEN1.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — MEN1 vasopressin neuroendocrine: vasopressin, via V1bR on pituitary adenoma cells (already mapped) and macrophages (already mapped), modulates the hypothalamic-pituitary axis; dysregulation amplifies IL-6 (already mapped) and mTOR (already mapped) signalling in MEN1 syndrome.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — MEN1 selenium antioxidant: selenium, via GPx/TrxR selenoproteins in MEN1 neuroendocrine tumour cells and macrophages (already mapped), quenches oxidative stress that amplifies mTOR (already mapped) and VEGF (already mapped) pro-tumour angiogenesis in MEN1 syndrome.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — MEN1 iodine thyroid: iodine, as the key substrate for thyroid hormone biosynthesis, supports the HPT axis; iodine insufficiency amplifies the neuroendocrine IL-6 (already mapped) and mTOR (already mapped) tumour-promoting cascade in MEN1 syndrome.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — MEN1 sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of MEN1 syndrome.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — MEN1 potassium: potassium channels regulate macrophage (already mapped) and fibroblast (already mapped) function in the MEN1 tumour microenvironment; potassium depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of MEN1 syndrome.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — MEN1 copper: copper, as cofactor of SOD1 in macrophages (already mapped) and endothelial cells (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative tumour cascade of MEN1 syndrome.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — MEN1 iron: iron, via ferritin in macrophages (already mapped) and fibroblasts (already mapped), modulates redox balance in the MEN1 tumour microenvironment; iron dysregulation amplifies IL-6 (already mapped) and mTOR (already mapped) cascade of MEN1 syndrome.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — MEN1 chloride: chloride channels regulate macrophage (already mapped) and endothelial cell (already mapped) ion homeostasis in the MEN1 neuroendocrine microenvironment; chloride imbalance amplifies IL-6 (already mapped) and VEGF (already mapped) cascade.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — MEN1 sulfur: sulfur-containing amino acids in macrophages (already mapped) and fibroblasts (already mapped) maintain redox buffering; sulfur depletion amplifies IL-6 (already mapped) and mTOR (already mapped) pro-tumour cascade of MEN1 syndrome.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^thakker-2012-men1-guidelines]: Thakker RV, Newey PJ, Walls GV, et al. Clinical practice guidelines for multiple endocrine neoplasia type 1 (MEN1). *J Clin Endocrinol Metab.* 2012;97(9):2990-3011. [doi:10.1210/jc.2012-1174](https://doi.org/10.1210/jc.2012-1174) · [PubMed 22392070](https://pubmed.ncbi.nlm.nih.gov/22392070/)
[^chandrasekharappa-1997-men1]: Chandrasekharappa SC, Guru SC, Manickam P, et al. Positional cloning of the gene for multiple endocrine neoplasia-type 1. *Science.* 1997;276(5311):404-407. [doi:10.1126/science.276.5311.404](https://doi.org/10.1126/science.276.5311.404) · [PubMed 9103196](https://pubmed.ncbi.nlm.nih.gov/9103196/)
