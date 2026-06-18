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

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^thakker-2012-men1-guidelines]: Thakker RV, Newey PJ, Walls GV, et al. Clinical practice guidelines for multiple endocrine neoplasia type 1 (MEN1). *J Clin Endocrinol Metab.* 2012;97(9):2990-3011. [doi:10.1210/jc.2012-1174](https://doi.org/10.1210/jc.2012-1174) · [PubMed 22392070](https://pubmed.ncbi.nlm.nih.gov/22392070/)
[^chandrasekharappa-1997-men1]: Chandrasekharappa SC, Guru SC, Manickam P, et al. Positional cloning of the gene for multiple endocrine neoplasia-type 1. *Science.* 1997;276(5311):404-407. [doi:10.1126/science.276.5311.404](https://doi.org/10.1126/science.276.5311.404) · [PubMed 9103196](https://pubmed.ncbi.nlm.nih.gov/9103196/)
