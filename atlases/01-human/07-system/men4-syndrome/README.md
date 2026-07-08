---
schema: human-scale-entry/v1
id: men4-syndrome
name: MEN4 Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Multiple Endocrine Neoplasia type 4 (MEN4) is caused by germline CDKN1B (p27KIP1) mutations; pituitary adenomas, parathyroid tumors, and pancreatic NETs similar to MEN1 but driven by CDK inhibitor LOF; annual biochemical and MRI surveillance; rarer than MEN1."
aliases: ["MEN4", "multiple endocrine neoplasia type 4", "MEN4 syndrome", "CDKN1B MEN4", "p27KIP1 syndrome", "MEN4 pituitary", "MEN4 parathyroid", "CDKN1B multiple endocrine neoplasia", "MEN4 CDKN1B germline"]
sources:
  - id: alrezk-2017-men4
    type: peer-reviewed
    cite: "Alrezk R, Hannah-Shmouni F, Stratakis CA. MEN4 and CDKN1B mutations: the latest of the MEN syndromes. Endocr Relat Cancer. 2017;24(10):T195-T208."
    doi: "10.1530/ERC-17-0243"
    pmid: "28894007"
    url: "https://doi.org/10.1530/ERC-17-0243"
  - id: pellegata-2006-cdkn1b-men4
    type: peer-reviewed
    cite: "Pellegata NS, Quintanilla-Martinez L, Siggelkow H, et al. Germ-line mutations in p27Kip1 cause a multiple endocrine neoplasia syndrome in rats and humans. Proc Natl Acad Sci USA. 2006;103(42):15558-15563."
    doi: "10.1073/pnas.0603306103"
    pmid: "17030811"
    url: "https://doi.org/10.1073/pnas.0603306103"
cross_links:
  - target: 01-human/03-molecular/cdkn1b
    relation: connects-to
    note: "CDKN1B (p27KIP1) LOF → CDK2-CyclinE derepressed at G1/S → neuroendocrine cell proliferation; p27 nuclear expression is prognostic in sporadic pNETs (low nuclear p27 = poor prognosis); SKP2-mediated p27 proteolysis is a druggable target in cancer; germline = MEN4."
  - target: 01-human/03-molecular/men1
    relation: connects-to
    note: "Menin (MEN1) regulates CDKN1B expression via H3K4me3 at the CDKN1B promoter; both MEN1 and CDKN1B are tumor suppressors in pituitary/parathyroid/pNET lineages; MEN4 tumors may show secondary CDKN1B loss; MEN1 negative MEN families should receive CDKN1B testing."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "MEN4 has an overlapping tumor spectrum with MEN1 (pituitary, parathyroid, pNETs); key differences: MEN4 is rarer; less frequent gastrinoma/ZES; no known skin features; CDKN1B germline LOF mechanism is distinct from menin LOF; combined MEN1+CDKN1B testing recommended."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "MEN4-associated pNETs and pituitary adenomas are driven by CDK2-CyclinE derepression due to CDKN1B LOF; p27 IHC loss in pNETs is a prognostic biomarker; CDK4/6 inhibitors (palbociclib, ribociclib) in SSTR-refractory pNETs target the same CDK cell cycle axis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Primary hyperparathyroidism is the most common MEN4 manifestation (~60-80%): CDKN1B/p27 loss drives parathyroid chief-cell proliferation → excess PTH → hypercalcemia, nephrolithiasis, and bone loss; multigland disease prompts 3.5-gland parathyroidectomy, mirroring MEN1."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Pituitary adenomas occur in ~60% of MEN4, including GH-secreting tumors causing acromegaly; p27 haploinsufficiency releases somatotroph CDK2-CyclinE → proliferation; managed like sporadic adenomas with transsphenoidal surgery and somatostatin receptor ligands."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "MEN4 produces pancreatic neuroendocrine tumors (~15-35%) like MEN1 but with less frequent gastrinoma/ZES; p27 loss derepresses islet-cell CDK2; surveillance uses annual chromogranin A and abdominal MRI, with octreotide/everolimus/sunitinib for advanced disease."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "MEN4 and Carney complex are both rare dominant multiple-endocrine-neoplasia syndromes with pituitary and other endocrine tumors, but via different genes: MEN4 from CDKN1B/p27 loss, Carney complex from PRKAR1A loss (PKA overactivity) plus cardiac myxomas and skin pigmentation."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "MEN4 is fundamentally a cell-cycle disease: loss of CDKN1B/p27 — a CDK inhibitor — releases CDK2-cyclin E (and CDK4/6) to drive G1/S transition in endocrine cells; this makes CDK4/6 inhibitors (palbociclib, ribociclib) a rational therapy for p27-deficient neuroendocrine tumors."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Pituitary adenomas occur in ~40-60% of MEN4, prolactinoma among the most common, causing hyperprolactinemia with hypogonadism and galactorrhea; p27 loss releases lactotroph proliferation, and these are managed like sporadic prolactinomas with dopamine agonists (cabergoline)."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "MEN4 is a MEN1-like multiple-endocrine-neoplasia syndrome: loss of the CDKN1B-encoded cell-cycle inhibitor p27 predisposes to parathyroid, pituitary and pancreatic-islet tumors much like menin loss, illustrating that several tumor-suppressor genes converge on endocrine neoplasia."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Pancreatic neuroendocrine tumors are part of MEN4 as in MEN1: p27 (CDKN1B) loss predisposes to islet-cell tumors (gastrinomas, insulinomas) alongside parathyroid and pituitary disease, so functional and anatomic pancreatic surveillance is recommended in CDKN1B carriers."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulinomas are among the islet tumors of MEN4: as in MEN1, p27 loss can produce a functioning pancreatic neuroendocrine tumor that oversecretes insulin, causing fasting hypoglycemia (Whipple's triad)—one reason MEN4 carriers need biochemical pancreatic-islet surveillance."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "MEN4 and pheochromocytoma rarely coincide: MEN4 (CDKN1B/p27 loss) phenocopies MEN1 with parathyroid, pituitary and pancreatic tumors but not the adrenal-medullary catecholamine tumors typical of MEN2 and VHL—so a pheochromocytoma argues against MEN4."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "MEN4 and von Hippel-Lindau are both dominant tumor-suppressor syndromes causing neuroendocrine tumors via different genes: MEN4 from CDKN1B loss, VHL from pVHL loss driving pseudohypoxia—both can produce pancreatic NETs, but their wider tumor spectra diverge."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal gland can be involved in MEN4 as in MEN1: CDKN1B loss predisposes mainly to parathyroid, pituitary and pancreatic tumors, but adrenal adenomas occur too, so surveillance of MEN4—the rare MEN1-phenocopy negative for MEN1 mutation—includes adrenal imaging."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "MEN4 can cause Cushing's like MEN1: CDKN1B (p27) loss predisposes to pituitary and adrenal tumors that raise cortisol, so MEN4—a rarer MEN1 mimic—produces overlapping hypercortisolism through a cell-cycle, rather than menin, defect."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "MEN4 broadens the endocrine tumor spectrum to the thyroid: loss of the p27 cell-cycle brake predisposes to thyroid and other endocrine tumors beyond the core parathyroid and pituitary lesions, so MEN4 surveillance, like MEN1's, spans multiple glands."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Hyperparathyroidism is MEN4's most frequent manifestation and a cause of bone loss: p27 loss drives parathyroid tumors whose excess PTH demineralizes bone, so MEN4 presents much like MEN1 with hypercalcemia and osteoporosis despite a different gene."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "MEN4 is the cell-cycle MEN: loss of the CDKN1B-encoded p27 brake removes restraint on cyclin D-CDK activity, so endocrine cells over-proliferate—a different molecular route to the parathyroid and pituitary tumors that MEN1 causes through menin."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "MEN4, like MEN1, can drive gastroenteropancreatic neuroendocrine tumors: p27 loss predisposes to gastrinomas and gastric/duodenal NETs alongside parathyroid and pituitary disease, so the stomach and gut are part of its tumor spectrum."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "MEN4 broadens the MEN tumor spectrum into reproductive and other organs: beyond parathyroid and pituitary, p27 loss has been linked to gonadal, cervical and adrenal tumors, reflecting how a single cell-cycle inhibitor guards many endocrine and reproductive tissues."
  - target: 01-human/03-molecular/ret
    relation: connects-to
    note: "MEN4 and MEN2 are different branches of the MEN family: MEN4 comes from CDKN1B loss and mimics MEN1, while MEN2 comes from RET mutations causing medullary thyroid cancer—so gene testing sorts which multiple-endocrine-neoplasia a patient has."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Like MEN1, MEN4 can harbor thymic and other neuroendocrine tumors: because CDKN1B loss produces a MEN1-like spectrum, surveillance includes imaging for thymic and bronchial carcinoids alongside the parathyroid and pituitary tumors."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "MEN4 causes hyperparathyroidism that activates osteoclasts: the resulting excess PTH drives these cells to resorb bone, releasing calcium and threatening the skeleton with osteoporosis—mirroring the bone disease of MEN1."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "MEN4's commonest feature is too much PTH: like MEN1, CDKN1B loss drives parathyroid tumors that oversecrete parathyroid hormone, raising calcium and eroding bone—hyperparathyroidism is usually the first manifestation."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "MEN4 is a broken cell-cycle brake felt through Rb: the lost p27 (CDKN1B) normally restrains the CDKs that phosphorylate Rb, so without it cells slip past the checkpoint—linking MEN4's tumors to the same Rb pathway as many cancers."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "MEN4's neuroendocrine tumors are targeted through SSTR2: like other NETs they display somatostatin receptors, so somatostatin analogs and receptor-guided radiotherapy (PRRT) can both image and treat the tumors of the syndrome."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "MEN4's hyperparathyroidism punishes the kidneys: chronic high calcium from overactive parathyroids precipitates kidney stones and nephrocalcinosis, so renal damage is a common consequence of the syndrome's commonest tumor."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "MEN4 weakens bone through parathyroid-driven osteoblast turnover: excess PTH speeds remodeling and tips the osteoblast-osteoclast balance toward loss, producing the osteoporosis that accompanies its hyperparathyroidism."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "MEN4's neuroendocrine tumors lean on VEGF for blood supply: like other NETs they drive angiogenesis to grow, so VEGF-targeted therapy is part of the toolkit alongside the somatostatin-receptor approaches."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "MEN4's overactive parathyroids unbalance phosphorus: excess PTH makes the kidneys dump phosphate while pulling calcium from bone, the mineral derangement of its hyperparathyroidism."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "MEN4 grows tumors at the base of the brain: pituitary adenomas are part of its spectrum, and as they enlarge they can press on the optic chiasm and brain, alongside its parathyroid and pancreatic tumors."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "MEN4's neuroendocrine tumors are richly vascular: their endothelial cells form the dense capillary networks that make these tumors stand out on contrast scans, aiding detection of small lesions."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Surveillance in MEN4 leans on photons: like MEN1, it uses sestamibi scintigraphy for parathyroids, Ga-68 DOTATATE PET for somatostatin-receptor-rich neuroendocrine tumors, and pituitary MRI to track adenomas across a lifetime of screening."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "MEN4 can include GH-secreting pituitary tumors, and IGF-1 is how they are caught: produced by the liver in step with growth hormone, its stable level reveals acromegaly that the pulsatile hormone would hide."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "As in MEN1, the liver shapes MEN4's outcome: its pancreatic and duodenal neuroendocrine tumors metastasize there, and progressive liver disease becomes the dominant threat once tumors have spread."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy confirms MEN4's tumors are neuroendocrine: like MEN1's, its pancreatic and pituitary growths brim with dense-core secretory granules, the hormone-packed ultrastructure of cells that signal through the bloodstream."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "MEN4's hyperparathyroidism wears down bone: excess parathyroid hormone spurs osteoclasts to resorb the skeleton into osteitis fibrosa, thinning the marrow-bearing bones much as in its MEN1 cousin."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "MEN4 can grow carcinoids in the chest: like MEN1 it predisposes to bronchial and thymic neuroendocrine tumors, foregut carcinoids that demand surveillance of the lungs alongside the pancreas and pituitary."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies pin down the diagnosis: chromogranin A and synaptophysin stains confirm MEN4's neuroendocrine tumors, while loss of the p27 protein (the CDKN1B product) on immunohistochemistry hints at the defect that DNA sequencing then confirms."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The duodenum joins the tumor map: MEN4, like MEN1, sprouts gastrinomas and other neuroendocrine tumors in the duodenum and small bowel, gut foregut lesions whose acid-driving hormones cause ulcers and diarrhea."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "High calcium dulls the nerves: MEN4's near-universal hyperparathyroidism floods the blood with calcium, and excess calcium slows neurons into the fatigue, confusion, and depressive 'moans' that are often the first clue to the parathyroid tumors."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Hyperparathyroidism puts vitamin D to work: MEN4's overactive parathyroids raise PTH, which spurs the kidney to activate vitamin D and pull up calcium, the mineral axis whose derangement causes the stones and bone disease that flag the syndrome."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Its pancreatic neuroendocrine tumors answer to mTOR: with p27's brake gone, growth signaling runs through the PI3K-mTOR axis, which is why the mTOR inhibitor everolimus is a mainstay for the advanced NETs that arise in MEN4 as in MEN1."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "The faulty gene matters beyond the glands: loss of p27 (CDKN1B), the cell-cycle brake mutated in MEN4, is also a recognized adverse feature in breast cancer, underscoring how this checkpoint protein restrains growth across many tissues."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Like its MEN1 twin, MEN4 reaches the stomach: gastrin-secreting duodeno-pancreatic neuroendocrine tumors drive Zollinger-Ellison acid disease and stimulate gastric ECL cells toward carcinoid tumors, extending the syndrome's reach into the stomach wall."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "The rare syndrome's tumor list runs wide: case reports of MEN4 include thyroid carcinoma alongside the core parathyroid, pituitary and pancreatic tumors, reflecting how losing the p27 cell-cycle brake can let many endocrine tissues turn neoplastic."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "The predisposition can touch the meninges: like MEN1, MEN4 has been reported with meningiomas, so the same p27 loss that drives the endocrine tumors also appears to relax growth control on the coverings of the brain."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO governs the p27 brake that MEN4 loses: FOXO transcription factors drive CDKN1B (p27) expression, so the regulatory network upstream of p27 ties into the cell-cycle escape that defines MEN4 endocrine tumors."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "MEN4 can share MEN1's skin signs: angiofibromas and collagenomas — fibroblast-and-collagen lesions — are reported in MEN4 as in MEN1, reflecting how convergent these near-twin syndromes are clinically."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "It joins the mTOR-linked endocrine-tumor syndromes: like tuberous sclerosis, which also seeds pancreatic neuroendocrine tumors through mTOR overactivity, MEN4 predisposes to endocrine neoplasia and is managed with overlapping surveillance."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "AKT controls the very brake MEN4 loses: AKT phosphorylates and inactivates the p27 (CDKN1B) cell-cycle inhibitor, so the germline CDKN1B loss of MEN4 mimics the unchecked proliferation that AKT signaling would otherwise drive."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Lost cell-cycle restraint meets growth signaling: with p27 gone, MEN4 neuroendocrine cells proliferate under STAT3 and other pro-growth pathways, part of the signaling that fuels its parathyroid and pituitary tumors."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its hyperparathyroidism harms the kidneys: like MEN1, MEN4's primary hyperparathyroidism causes hypercalcemia, nephrolithiasis and nephrocalcinosis that can progress to chronic kidney disease."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Its pancreatic and pituitary tumors derange glucose: MEN4's neuroendocrine tumors and any acromegaly from a growth-hormone-secreting pituitary tumor disturb glucose metabolism, while pancreatic surgery can leave a secondary diabetes."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Hormones and hereditary surveillance weigh on mood: hypercalcemia's psychiatric effects, any Cushing's from a pituitary tumor and the burden of lifelong multi-tumor monitoring contribute to depression in MEN4."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Its tumors and renal disease lower the count: advanced neuroendocrine tumors with their inflammation, plus the renal impairment from hyperparathyroidism, can produce an anemia of chronic disease."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Its hormone-secreting tumors raise blood pressure: like MEN1, MEN4's primary hyperparathyroidism and functioning pituitary and neuroendocrine tumors contribute to secondary hypertension."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Recurrent endocrine surgery taxes healing: the parathyroid, pituitary and pancreatic operations MEN4 requires leave repeated surgical wounds to heal over the patient's lifetime."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong tumor surveillance breeds worry: the constant biochemical and imaging screening for the multiple endocrine tumors of MEN4, and its hereditary nature, foster chronic health anxiety."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its hyperparathyroidism stones the kidneys: the primary hyperparathyroidism that dominates MEN4 raises calcium and causes recurrent kidney stones and nephrocalcinosis threatening renal function."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its pituitary tumours press on the brain: MEN4 pituitary adenomas can compress the optic chiasm and surrounding structures, causing visual-field loss, headache and cranial-nerve palsies."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its pancreatic tumours ulcerate the gut: gastrinomas in MEN4 secrete gastrin to cause the refractory peptic ulcers of Zollinger-Ellison syndrome, alongside other gastroenteropancreatic NETs."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Parathyroid excess dissolves bone: primary hyperparathyroidism — its most common feature — drives osteoclastic bone resorption with osteitis fibrosa and fragility fractures."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its high calcium unsettles the heart: the hypercalcaemia of MEN4 hyperparathyroidism shortens the QT interval and can cause arrhythmias and hypertension."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It can mark the skin: like MEN1, MEN4 can produce cutaneous angiofibromas and collagenomas among its varied manifestations."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Its neuroendocrine tumours get targeted drugs: like MEN1, MEN4 produces pancreatic and pituitary neuroendocrine tumours treatable with mTOR inhibitors and somatostatin analogues."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "Gastrinomas ulcer without it: MEN4 can cause Zollinger-Ellison syndrome whose severe peptic ulcers, unlike the common kind, are not driven by Helicobacter pylori."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "A fellow tumour syndrome with neuroendocrine tumours: NF1, like MEN4, can cause duodenal neuroendocrine tumours and phaeochromocytoma, overlapping its endocrine spectrum."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "Its pancreatic tumours arise here: like MEN1, MEN4 predisposes to islet-cell neuroendocrine tumours of the pancreas alongside parathyroid and pituitary tumours."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "A fellow endocrine-tumour syndrome: MEN4, like Cowden syndrome, is an inherited predisposition to multiple endocrine and other tumours requiring lifelong gland surveillance."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for advanced neuroendocrine tumours: metastatic pancreatic neuroendocrine tumours in MEN4 are treated with chemotherapy such as capecitabine-temozolomide alongside targeted agents."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Like MEN1, it starts in the parathyroids: hyperparathyroidism is the leading MEN4 feature, and the high PTH it drives resorbs cortical bone—causing osteoporosis and fractures—so the skeleton registers the endocrine tumour."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Two brakes on the cell cycle lost: MEN4 arises from loss of CDKN1B (p27), a CDK inhibitor that restrains G1→S, much as retinoblastoma arises from loss of RB1 downstream in the same checkpoint—different stops on one cell-cycle pathway."
  - target: 01-human/03-molecular/cdkn1a
    relation: connects-to
    note: "Its gene has a sibling brake: MEN4 is caused by loss of CDKN1B (p27); CDKN1A (p21) is the closely related CIP/KIP-family CDK inhibitor that enforces the same G1/S checkpoint, so the two share the job MEN4's mutation abolishes."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Hypercalcaemia and the kidney: like MEN1, MEN4's primary hyperparathyroidism raises calcium and causes kidney stones and nephrocalcinosis that scar the glomerulus."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Gastrinomas and peptic ulcers: pancreatic and duodenal gastrinomas in MEN4 can cause Zollinger-Ellison syndrome with refractory ulcers eroding the intestinal epithelium."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Germline endocrine-tumour syndromes: MEN4 (CDKN1B) and DICER1 both predispose to pituitary and other endocrine tumours, two of the autosomal-dominant syndromes warranting multi-gland surveillance."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The metastatic sink: like MEN1, the enteropancreatic neuroendocrine tumours of MEN4 spread to the liver, and this hepatic involvement through the lobule largely determines prognosis and survival."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Functional carcinoids: enteropancreatic and foregut neuroendocrine tumours in MEN4 can secrete serotonin, and once they reach the liver the hormone drives the flushing and diarrhoea of carcinoid syndrome."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "Valve scarring from hormone overflow: serotonin from liver-metastatic MEN4 carcinoids lays down fibrous plaque on the right-heart valves and endocardium, the substrate of carcinoid heart disease."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Released cell cycle: loss of the p27/CDKN1B brake in MEN4 frees the CDK-RB-E2F axis, letting E2F1 drive the cell-cycle entry of its endocrine tumours."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Vascular neuroendocrine tumours: HIF-1α-driven, VEGF-rich angiogenesis makes MEN4 neuroendocrine tumours highly vascular, supporting anti-angiogenic therapy."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative persistence: TERT reactivation maintaining telomeres accompanies the progression of MEN4 endocrine tumours toward more aggressive disease."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative oncogene: loss of the p27 (CDKN1B) brake in MEN4 permits unrestrained cell-cycle entry, with MYC driving the proliferation of its endocrine tumours."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Endocrine tumour signalling: aberrant Wnt/β-catenin activation contributes to the parathyroid and pituitary tumours of the MEN4 spectrum."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic progression: EZH2-mediated PRC2 silencing of tumour-suppressor genes contributes to the development of MEN4-associated neuroendocrine tumours."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Prolactinoma therapy: dopamine agonists treat the prolactin-secreting pituitary adenomas of the MEN4 spectrum, exploiting dopamine's tonic inhibition of pituitary prolactin release."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Gastrinoma acid: gastrinomas in the MEN4 spectrum drive gastrin-stimulated histamine release from gastric ECL cells, causing the acid hypersecretion of Zollinger-Ellison syndrome."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Hyperparathyroid bone loss: primary hyperparathyroidism, the most frequent MEN4 manifestation, drives PTH-stimulated RANKL-mediated osteoclast activity and bone resorption."
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "p27 transcriptional input: FOXO1 transcriptionally induces p27 (CDKN1B), the very CDK inhibitor whose germline loss defines MEN4 — so the FOXO-p27 axis is the regulatory pathway short-circuited in the syndrome."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Calcium counter-regulation: with primary hyperparathyroidism the most frequent MEN4 feature, calcitonin from thyroid C cells acts as the physiological counterweight to the PTH-driven hypercalcaemia that results."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Neuroendocrine metastasis: CXCR4-CXCL12 signalling drives the metastasis of the pancreatic neuroendocrine tumours of the MEN4 spectrum, the spread that worsens prognosis when these tumours progress."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Primary hyperparathyroidism: like MEN1, MEN4 most often presents with parathyroid tumours causing hypercalcaemia from excess PTH, the commonest and usually earliest manifestation that prompts the genetic testing distinguishing it from MEN1."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-p27 axis: TGF-β signalling normally induces the CDK inhibitor p27 (CDKN1B) to arrest the cell cycle, so the CDKN1B loss that causes MEN4 disables this growth-suppressive output, releasing endocrine cells to proliferate."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Functional pancreatic NETs: MEN4 predisposes to pancreatic neuroendocrine tumours that can secrete hormones such as glucagon, gastrin or insulin, the functioning tumours whose hormonal syndromes can be the presenting feature."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "pNET growth axis: PIK3CA drives the PI3K-AKT-mTOR pathway (AKT and mTOR already mapped) in the pancreatic neuroendocrine tumours of MEN4, the basis for mTOR-inhibitor therapy."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK proliferation: growth-factor-driven RAS-MAPK-ERK signalling promotes proliferation of the parathyroid, pituitary and pancreatic tumours of MEN4, complementing the loss of p27-mediated cell-cycle restraint."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Neuroendocrine signalling: NOTCH signalling shapes the differentiation and growth of neuroendocrine tumours, a pathway dysregulated in the pancreatic and pituitary tumours of MEN4."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "mTOR pathway: PTEN loss releases the PI3K-AKT-mTOR axis (AKT, PIK3CA and mTOR already mapped) driving the neuroendocrine tumours of MEN4, the p27/CDKN1B-deficient counterpart of MEN1."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "NET angiogenesis: the VEGF/PDGF angiogenic axis (VEGF already mapped) supports the vascular neuroendocrine tumours of MEN4."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Proliferative MAPK: RAS-MAPK signalling (ERK1/2 already mapped) provides a proliferative input to the parathyroid, pituitary and pancreatic tumours of MEN4."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is a marker and modulator of the neuroendocrine and parathyroid tumours arising in MEN4 syndrome."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT3 signalling (STAT3 mapped) provides a proliferative input to the endocrine tumours of MEN4 syndrome."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Disrupted TGF-β-SMAD growth-suppressive signalling (SMAD4 mapped) contributes to the endocrine tumorigenesis of MEN4, in which loss of the CDK inhibitor p27 removes a key proliferative brake."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune microenvironment of the neuroendocrine tumours that arise in MEN4 syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory microenvironment of the p27-deficient endocrine tumours of MEN4 syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated CD8 cytotoxicity contributes to the immune surveillance of the neuroendocrine tumours that arise in MEN4 syndrome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and survival signaling of the endocrine tumors of MEN4 syndrome."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation restrains apoptosis in the endocrine tumors of MEN4 syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of MEN4-associated neuroendocrine tumors."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative signaling of the endocrine tumors of MEN4 syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the neuroendocrine tumors of MEN4 syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the p27-deficient endocrine tumor cells of MEN4 syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the endocrine tumors of multiple endocrine neoplasia type 4."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of multiple endocrine neoplasia type 4."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of multiple endocrine neoplasia type 4."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of MEN4 syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of MEN4 syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of MEN4 syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of the neuroendocrine neoplasms of MEN4 syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of MEN4 syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of MEN4 syndrome."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Gastrinoma acid: like MEN1, MEN4 can include gastrinomas that drive massive gastric acid (proton) secretion (Zollinger-Ellison syndrome), causing refractory peptic ulceration managed with high-dose proton-pump inhibitors."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Insulinoma hypoglycaemia: functional pancreatic neuroendocrine tumours in MEN4 can oversecrete insulin (already mapped), which through the insulin receptor produces the fasting hypoglycaemia of an insulinoma."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Carcinoid heart disease: serotonin-secreting neuroendocrine tumours in the MEN4 spectrum (serotonin already mapped) can cause carcinoid heart disease with valvular fibrosis, and troponin marks the associated myocardial strain."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "Ectopic Cushing: neuroendocrine tumours in MEN4 can secrete ACTH ectopically, driving cortisol excess (already mapped) and Cushing syndrome, one of the functional hormone syndromes of its pituitary and pancreatic tumours."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Adrenal adenomas: adrenocortical tumours in the MEN4 spectrum (adrenal gland already mapped) can oversecrete aldosterone, causing primary aldosteronism with hypertension and hypokalaemia beyond the classic parathyroid-pituitary-pancreas triad."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with the strongly expressed VEGF (already mapped) supports the rich vasculature of the neuroendocrine tumours of MEN4, part of the angiogenic biology targeted by antiangiogenic and mTOR (already mapped) therapy."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Mineral dysregulation: the primary hyperparathyroidism of MEN4 (PTH and calcium already mapped) disturbs magnesium alongside calcium handling, part of the mineral derangement of the commonest manifestation of the syndrome."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Enteropancreatic tumours: GLP-1 and the incretin axis reflect the enteropancreatic neuroendocrine biology of the MEN4 pancreatic tumours (insulin and glucagon already mapped), part of the functional-tumour spectrum shared with MEN1 (already mapped)."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the microenvironment of the MEN4 neuroendocrine tumours dampens the anti-tumour immune response, part of the immune biology relevant to the immunotherapy of any aggressive metastatic tumour."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the MEN4 neuroendocrine tumours."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the MEN4 neuroendocrine tumours."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Islet zinc: zinc is stored with insulin (already mapped) in the islet secretory granules, and the zinc-insulin hexamer is part of the biology of the insulinomas and other pancreatic neuroendocrine tumours of MEN4."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Steroidogenesis substrate: cholesterol is the precursor of the cortisol and aldosterone (already mapped) of the adrenocortical (adrenal already mapped) tumours that occur in MEN4."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Islet-tumour metabolic adipokine: leptin reflects the metabolic disturbance of the insulinoma and glucagonoma (insulin and glucagon already mapped) and the endocrine tumours of MEN4."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic disturbance of the endocrine tumours of MEN4."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the metabolic disturbance of the endocrine tumours of MEN4."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "NET immunosurveillance: the cytotoxic T cells (perforin already mapped) provide the immune surveillance of the pancreatic and other neuroendocrine tumours of MEN4."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon and NETs: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway and historically used to treat the neuroendocrine tumours, is part of the innate-immune dimension of MEN4."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 immunosurveillance: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunosurveillance of the neuroendocrine tumours of MEN4."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the MEN4 neuroendocrine tumours."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the MEN4 tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the MEN4 neuroendocrine tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the MEN4 tumours."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the MEN4 neuroendocrine tumours."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the MEN4 neuroendocrine tumours."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the macrophages are a dominant myeloid population of the stroma of the well-vascularised (VEGF already mapped) MEN4 neuroendocrine tumours."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the MEN4 neuroendocrine tumour stroma."
---

# MEN4 Syndrome

## Overview

**Multiple Endocrine Neoplasia type 4 (MEN4)** is a rare autosomal dominant hereditary endocrine tumor predisposition syndrome caused by germline pathogenic variants in **CDKN1B** (cyclin-dependent kinase inhibitor 1B; encodes p27KIP1). MEN4 was established as a distinct clinical entity following the identification of homozygous *Cdkn1b* mutations in the MENX rat model of multiple endocrine neoplasia by Pellegata et al. in 2006, with subsequent identification of heterozygous CDKN1B mutations in MEN1-negative human patients with the MEN clinical phenotype. MEN4 is formally recognized by **WHO 2022** Classification of Endocrine and Neuroendocrine Tumors as a category distinct from MEN1, MEN2, and MEN3. The clinical syndrome resembles MEN1 in its major tumor types (pituitary adenomas, primary hyperparathyroidism, pancreatic NETs) but results from CDK inhibitor LOF (loss of p27-mediated G1/S arrest) rather than epigenetic scaffold dysfunction (menin). MEN4 is approximately **1/100 as prevalent as MEN1**, with fewer than 100 well-documented cases in the literature as of 2025 [^pellegata-2006-cdkn1b-men4] [^alrezk-2017-men4].

**MEN4 vs. MEN1 vs. MEN2A comparison:**

| Feature | MEN4 (CDKN1B) | MEN1 (MEN1) | MEN2A (RET) |
|---|---|---|---|
| Gene | CDKN1B (12p13.1) | MEN1 (11q13.1) | RET (10q11.21) |
| Mechanism | CDK inhibitor LOF | Epigenetic scaffold LOF | Receptor tyrosine kinase GOF |
| Prevalence | 1/10,000,000 (est.) | 1/20,000-30,000 | 1/35,000 |
| Parathyroid | Primary hyperparathyroidism | >95% | ~20-30% (2A only) |
| Pituitary | ~60% (all subtypes) | ~20-65% | Not characteristic |
| Pancreatic NETs | ~15-35% | ~30-80% | Not characteristic |
| MTC | No | No | ~100% (2A carriers) |
| Pheochromocytoma | Rare | Rare | ~50% (2A) |
| Gastrinoma/ZES | Rare reports | Common (~25-40%) | No |

## Structure

### Genetic basis of MEN4

**CDKN1B gene (12p13.1):**
- 3 exons (2 coding); 198 aa; 27 kDa; ubiquitously expressed with highest levels in post-mitotic and quiescent cells
- Germline pathogenic variant spectrum: frameshift/nonsense (~55%), missense in CDK inhibitory domain (~25%), splice site (~10%), 5'UTR variants altering Kozak context or translation initiation (~10%)
- Haploinsufficiency mechanism: single functional allele → reduced p27 dosage → insufficient CDK2 inhibition → neuroendocrine progenitor cell proliferation → tumor formation
- Complete CDKN1B biallelic loss: not observed in germline (homozygous LOF lethal embryonically in mice); only heterozygous germline → MEN4; somatic second hit (LOH at 12p13) may occur in tumor tissue
- Penetrance: incompletely defined (rare syndrome); estimated >50% by age 60 for at least one MEN4 manifestation; pituitary adenomas appear most penetrant

**Where to suspect CDKN1B germline testing:**
1. MEN1-negative patient with at least 2 typical MEN1 tumor types (pituitary + parathyroid, or pituitary + pNET, etc.)
2. Young-onset primary hyperparathyroidism + pituitary adenoma
3. Multiglandular primary hyperparathyroidism without MEN1 mutation
4. Family history of MEN clinical phenotype with negative MEN1 testing

Recommended testing approach: multigene panel (MEN1 + CDKN1B + other MEN genes) when clinical suspicion; CDKN1B sequencing + MLPA for deletions.

### CDKN1B molecular mechanism in MEN4

p27KIP1 haploinsufficiency → insufficient CDK2-CyclinE inhibition → premature cell cycle entry in:
- Pituitary somatotrophs → GH-secreting adenoma (acromegaly)
- Pituitary corticotrophs → ACTH-secreting adenoma (Cushing disease)
- Pituitary lactotrophs → prolactinoma
- Parathyroid chief cells → chief cell hyperplasia / adenoma → PTH-mediated hypercalcemia
- Pancreatic islet β-cells / δ-cells / α-cells → pNET

The MEN1-p27 axis: Menin (MEN1 protein) regulates CDKN1B transcription via H3K4me3 deposition at the CDKN1B promoter. MEN1 LOF → reduced CDKN1B expression → p27 falls → CDK2 derepressed → neuroendocrine proliferation. This makes p27 a **downstream effector** of menin in the same pathway, explaining the overlapping tumor spectrum of MEN1 and MEN4 despite different gene mutations.

## Function

### Clinical manifestations of MEN4

**Pituitary adenomas (~60% of MEN4 patients):**
- All subtypes reported: prolactinoma (most common in some series), GH-secreting (acromegaly), ACTH-secreting (Cushing disease), non-functioning
- Treatment: same as sporadic pituitary adenoma — dopamine agonists (prolactinoma); transsphenoidal surgery; somatostatin receptor ligands (GH adenoma); radiotherapy for residual/refractory
- MEN4 pituitary adenoma may be more aggressive than sporadic adenomas (biallelic CDK inhibitor LOF in pituitary progenitors); surveillance brain MRI every 3-5 years

**Primary hyperparathyroidism (PHPT; ~60-80% of MEN4 patients):**
- Multiglandular (chief cell hyperplasia → multigland disease) or single adenoma
- Presentation: hypercalcemia, elevated PTH, nephrolithiasis, bone loss (osteoporosis)
- Annual Ca, PTH, 24h urine calcium; neck ultrasound every 2-3 years
- Surgical management: 3.5-gland parathyroidectomy (similar to MEN1-PHPT) given multiglandular risk; intraoperative PTH monitoring

**Pancreatic NETs (~15-35% of MEN4 patients):**
- Functional (gastrinoma, insulinoma) or non-functional; similar to MEN1-pNETs but gastrinoma/ZES appears less frequent in MEN4 vs MEN1
- Surveillance: annual plasma chromogranin A, fasting glucose/insulin, gastrin (if symptoms); annual abdominal MRI ± EUS
- Management: similar to MEN1-pNETs; somatostatin analogs (octreotide/lanreotide); targeted therapy (everolimus, sunitinib) for advanced/metastatic; surgical resection for localized

**Other MEN4 features (rarer):**
- Adrenal tumors: some cases reported; adrenal CT annually
- Carcinoid tumors: bronchial, gastric; more data needed
- Renal angiomyolipoma: rare case reports; unclear if true MEN4 association
- Cervical cancer: limited data; may represent background incidence

**Features NOT characteristic of MEN4 (unlike MEN1):**
- Medullary thyroid cancer (MTC): not part of MEN4 (MTC is MEN2/RET)
- Cutaneous lipomas, angiofibromas, collagenomas: MEN1 skin features not described in MEN4
- Gastrinoma/ZES: rare in MEN4 vs. 25-40% in MEN1

## Pathology

### Surveillance and management

**Annual biochemical screening (from age 20, or 5-10 years before youngest affected family member):**
- Serum calcium, PTH → parathyroid
- Prolactin, IGF-1 (acromegaly), ACTH/cortisol (Cushing) → pituitary
- Chromogranin A, fasting glucose, insulin, gastrin (if symptoms), glucagon → pNETs
- 24h urine catecholamines/metanephrines → pheochromocytoma (uncommon but reported)

**Imaging:**
- Brain MRI (pituitary protocol): at diagnosis; every 3-5 years if no adenoma; more frequent if symptoms
- Abdominal MRI or CT: annually; pancreatic lesions ≥1 cm → surgery or close follow-up
- Neck ultrasound: every 2-3 years for parathyroid

**Genetic counseling:**
- Autosomal dominant; 50% offspring risk
- Testing of at-risk relatives from childhood (biochemical) and genetically from adolescence
- Prenatal/PGT-M testing available

### Multigene panel testing strategy for MEN syndromes

When clinical MEN features are present:
1. **First test**: MEN1 sequencing + MLPA (identifies ~70-80% of MEN1 syndrome)
2. **If MEN1 negative**: multigene panel including CDKN1B (MEN4), RET (MEN2), CDKN2B, CDKN2C, AIP (pituitary adenoma predisposition), MAX (pheochromocytoma)
3. **Pituitary adenoma isolated**: AIP (aryl hydrocarbon receptor-interacting protein) mutations cause familial isolated pituitary adenoma (FIPA), especially GH-secreting; distinct from MEN4
4. **Parathyroid alone**: germline HRPT2/CDC73 mutations (hyperparathyroidism-jaw tumor syndrome); CASR variants (FHH)

## Connections

- `connects-to` → **[CDKN1B](../../03-molecular/cdkn1b/README.md)** — CDKN1B (p27KIP1) LOF → CDK2-CyclinE derepressed at G1/S → neuroendocrine cell proliferation; p27 nuclear expression is prognostic in sporadic pNETs (low nuclear p27 = poor prognosis); SKP2-mediated p27 proteolysis is a druggable target in cancer; germline = MEN4.
- `connects-to` → **[MEN1](../../03-molecular/men1/README.md)** — Menin (MEN1) regulates CDKN1B expression via H3K4me3 at the CDKN1B promoter; both MEN1 and CDKN1B are tumor suppressors in pituitary/parathyroid/pNET lineages; MEN4 tumors may show secondary CDKN1B loss; MEN1 negative MEN families should receive CDKN1B testing.
- `connects-to` → **[MEN1 Syndrome](../../07-system/men1-syndrome/README.md)** — MEN4 has an overlapping tumor spectrum with MEN1 (pituitary, parathyroid, pNETs); key differences: MEN4 is rarer; less frequent gastrinoma/ZES; no known skin features; CDKN1B germline LOF mechanism is distinct from menin LOF; combined MEN1+CDKN1B testing recommended.
- `connects-to` → **[Neuroendocrine Tumors](../../07-system/neuroendocrine-tumors/README.md)** — MEN4-associated pNETs and pituitary adenomas are driven by CDK2-CyclinE derepression due to CDKN1B LOF; p27 IHC loss in pNETs is a prognostic biomarker; CDK4/6 inhibitors (palbociclib, ribociclib) in SSTR-refractory pNETs target the same CDK cell cycle axis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Primary hyperparathyroidism is the most common MEN4 manifestation (~60-80%): CDKN1B/p27 loss drives parathyroid chief-cell proliferation → excess PTH → hypercalcemia, nephrolithiasis, and bone loss; multigland disease prompts 3.5-gland parathyroidectomy, mirroring MEN1.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Pituitary adenomas occur in ~60% of MEN4, including GH-secreting tumors causing acromegaly; p27 haploinsufficiency releases somatotroph CDK2-CyclinE → proliferation; managed like sporadic adenomas with transsphenoidal surgery and somatostatin receptor ligands.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — MEN4 produces pancreatic neuroendocrine tumors (~15-35%) like MEN1 but with less frequent gastrinoma/ZES; p27 loss derepresses islet-cell CDK2; surveillance uses annual chromogranin A and abdominal MRI, with octreotide/everolimus/sunitinib for advanced disease.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — MEN4 and Carney complex are both rare dominant multiple-endocrine-neoplasia syndromes with pituitary and other endocrine tumors, but via different genes: MEN4 from CDKN1B/p27 loss, Carney complex from PRKAR1A loss (PKA overactivity) plus cardiac myxomas and skin pigmentation.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — MEN4 is fundamentally a cell-cycle disease: loss of CDKN1B/p27 — a CDK inhibitor — releases CDK2-cyclin E (and CDK4/6) to drive G1/S transition in endocrine cells; this makes CDK4/6 inhibitors (palbociclib, ribociclib) a rational therapy for p27-deficient neuroendocrine tumors.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Pituitary adenomas occur in ~40-60% of MEN4, prolactinoma among the most common, causing hyperprolactinemia with hypogonadism and galactorrhea; p27 loss releases lactotroph proliferation, and these are managed like sporadic prolactinomas with dopamine agonists (cabergoline).
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — MEN4 is a MEN1-like multiple-endocrine-neoplasia syndrome: loss of the CDKN1B-encoded cell-cycle inhibitor p27 predisposes to parathyroid, pituitary and pancreatic-islet tumors much like menin loss, illustrating that several tumor-suppressor genes converge on endocrine neoplasia.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Pancreatic neuroendocrine tumors are part of MEN4 as in MEN1: p27 (CDKN1B) loss predisposes to islet-cell tumors (gastrinomas, insulinomas) alongside parathyroid and pituitary disease, so functional and anatomic pancreatic surveillance is recommended in CDKN1B carriers.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulinomas are among the islet tumors of MEN4: as in MEN1, p27 loss can produce a functioning pancreatic neuroendocrine tumor that oversecretes insulin, causing fasting hypoglycemia (Whipple's triad)—one reason MEN4 carriers need biochemical pancreatic-islet surveillance.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — MEN4 and pheochromocytoma rarely coincide: MEN4 (CDKN1B/p27 loss) phenocopies MEN1 with parathyroid, pituitary and pancreatic tumors but not the adrenal-medullary catecholamine tumors typical of MEN2 and VHL—so a pheochromocytoma argues against MEN4.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — MEN4 and von Hippel-Lindau are both dominant tumor-suppressor syndromes causing neuroendocrine tumors via different genes: MEN4 from CDKN1B loss, VHL from pVHL loss driving pseudohypoxia—both can produce pancreatic NETs, but their wider tumor spectra diverge.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal gland can be involved in MEN4 as in MEN1: CDKN1B loss predisposes mainly to parathyroid, pituitary and pancreatic tumors, but adrenal adenomas occur too, so surveillance of MEN4—the rare MEN1-phenocopy negative for MEN1 mutation—includes adrenal imaging.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — MEN4 can cause Cushing's like MEN1: CDKN1B (p27) loss predisposes to pituitary and adrenal tumors that raise cortisol, so MEN4—a rarer MEN1 mimic—produces overlapping hypercortisolism through a cell-cycle, rather than menin, defect.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — MEN4 broadens the endocrine tumor spectrum to the thyroid: loss of the p27 cell-cycle brake predisposes to thyroid and other endocrine tumors beyond the core parathyroid and pituitary lesions, so MEN4 surveillance, like MEN1's, spans multiple glands.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Hyperparathyroidism is MEN4's most frequent manifestation and a cause of bone loss: p27 loss drives parathyroid tumors whose excess PTH demineralizes bone, so MEN4 presents much like MEN1 with hypercalcemia and osteoporosis despite a different gene.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — MEN4 is the cell-cycle MEN: loss of the CDKN1B-encoded p27 brake removes restraint on cyclin D-CDK activity, so endocrine cells over-proliferate—a different molecular route to the parathyroid and pituitary tumors that MEN1 causes through menin.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — MEN4, like MEN1, can drive gastroenteropancreatic neuroendocrine tumors: p27 loss predisposes to gastrinomas and gastric/duodenal NETs alongside parathyroid and pituitary disease, so the stomach and gut are part of its tumor spectrum.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — MEN4 broadens the MEN tumor spectrum into reproductive and other organs: beyond parathyroid and pituitary, p27 loss has been linked to gonadal, cervical and adrenal tumors, reflecting how a single cell-cycle inhibitor guards many endocrine and reproductive tissues.
- `connects-to` → **[RET](../../03-molecular/ret/README.md)** — MEN4 and MEN2 are different branches of the MEN family: MEN4 comes from CDKN1B loss and mimics MEN1, while MEN2 comes from RET mutations causing medullary thyroid cancer—so gene testing sorts which multiple-endocrine-neoplasia a patient has.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Like MEN1, MEN4 can harbor thymic and other neuroendocrine tumors: because CDKN1B loss produces a MEN1-like spectrum, surveillance includes imaging for thymic and bronchial carcinoids alongside the parathyroid and pituitary tumors.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — MEN4 causes hyperparathyroidism that activates osteoclasts: the resulting excess PTH drives these cells to resorb bone, releasing calcium and threatening the skeleton with osteoporosis—mirroring the bone disease of MEN1.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — MEN4's commonest feature is too much PTH: like MEN1, CDKN1B loss drives parathyroid tumors that oversecrete parathyroid hormone, raising calcium and eroding bone—hyperparathyroidism is usually the first manifestation.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — MEN4 is a broken cell-cycle brake felt through Rb: the lost p27 (CDKN1B) normally restrains the CDKs that phosphorylate Rb, so without it cells slip past the checkpoint—linking MEN4's tumors to the same Rb pathway as many cancers.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — MEN4's neuroendocrine tumors are targeted through SSTR2: like other NETs they display somatostatin receptors, so somatostatin analogs and receptor-guided radiotherapy (PRRT) can both image and treat the tumors of the syndrome.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — MEN4's hyperparathyroidism punishes the kidneys: chronic high calcium from overactive parathyroids precipitates kidney stones and nephrocalcinosis, so renal damage is a common consequence of the syndrome's commonest tumor.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — MEN4 weakens bone through parathyroid-driven osteoblast turnover: excess PTH speeds remodeling and tips the osteoblast-osteoclast balance toward loss, producing the osteoporosis that accompanies its hyperparathyroidism.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — MEN4's neuroendocrine tumors lean on VEGF for blood supply: like other NETs they drive angiogenesis to grow, so VEGF-targeted therapy is part of the toolkit alongside the somatostatin-receptor approaches.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — MEN4's overactive parathyroids unbalance phosphorus: excess PTH makes the kidneys dump phosphate while pulling calcium from bone, the mineral derangement of its hyperparathyroidism.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — MEN4 grows tumors at the base of the brain: pituitary adenomas are part of its spectrum, and as they enlarge they can press on the optic chiasm and brain, alongside its parathyroid and pancreatic tumors.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — MEN4's neuroendocrine tumors are richly vascular: their endothelial cells form the dense capillary networks that make these tumors stand out on contrast scans, aiding detection of small lesions.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Surveillance in MEN4 leans on photons: like MEN1, it uses sestamibi scintigraphy for parathyroids, Ga-68 DOTATATE PET for somatostatin-receptor-rich neuroendocrine tumors, and pituitary MRI to track adenomas across a lifetime of screening.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — MEN4 can include GH-secreting pituitary tumors, and IGF-1 is how they are caught: produced by the liver in step with growth hormone, its stable level reveals acromegaly that the pulsatile hormone would hide.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — As in MEN1, the liver shapes MEN4's outcome: its pancreatic and duodenal neuroendocrine tumors metastasize there, and progressive liver disease becomes the dominant threat once tumors have spread.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy confirms MEN4's tumors are neuroendocrine: like MEN1's, its pancreatic and pituitary growths brim with dense-core secretory granules, the hormone-packed ultrastructure of cells that signal through the bloodstream.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — MEN4's hyperparathyroidism wears down bone: excess parathyroid hormone spurs osteoclasts to resorb the skeleton into osteitis fibrosa, thinning the marrow-bearing bones much as in its MEN1 cousin.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — MEN4 can grow carcinoids in the chest: like MEN1 it predisposes to bronchial and thymic neuroendocrine tumors, foregut carcinoids that demand surveillance of the lungs alongside the pancreas and pituitary.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies pin down the diagnosis: chromogranin A and synaptophysin stains confirm MEN4's neuroendocrine tumors, while loss of the p27 protein (the CDKN1B product) on immunohistochemistry hints at the defect that DNA sequencing then confirms.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The duodenum joins the tumor map: MEN4, like MEN1, sprouts gastrinomas and other neuroendocrine tumors in the duodenum and small bowel, gut foregut lesions whose acid-driving hormones cause ulcers and diarrhea.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — High calcium dulls the nerves: MEN4's near-universal hyperparathyroidism floods the blood with calcium, and excess calcium slows neurons into the fatigue, confusion, and depressive 'moans' that are often the first clue to the parathyroid tumors.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Hyperparathyroidism puts vitamin D to work: MEN4's overactive parathyroids raise PTH, which spurs the kidney to activate vitamin D and pull up calcium, the mineral axis whose derangement causes the stones and bone disease that flag the syndrome.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Its pancreatic neuroendocrine tumors answer to mTOR: with p27's brake gone, growth signaling runs through the PI3K-mTOR axis, which is why the mTOR inhibitor everolimus is a mainstay for the advanced NETs that arise in MEN4 as in MEN1.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — The faulty gene matters beyond the glands: loss of p27 (CDKN1B), the cell-cycle brake mutated in MEN4, is also a recognized adverse feature in breast cancer, underscoring how this checkpoint protein restrains growth across many tissues.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Like its MEN1 twin, MEN4 reaches the stomach: gastrin-secreting duodeno-pancreatic neuroendocrine tumors drive Zollinger-Ellison acid disease and stimulate gastric ECL cells toward carcinoid tumors, extending the syndrome's reach into the stomach wall.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — The rare syndrome's tumor list runs wide: case reports of MEN4 include thyroid carcinoma alongside the core parathyroid, pituitary and pancreatic tumors, reflecting how losing the p27 cell-cycle brake can let many endocrine tissues turn neoplastic.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — The predisposition can touch the meninges: like MEN1, MEN4 has been reported with meningiomas, so the same p27 loss that drives the endocrine tumors also appears to relax growth control on the coverings of the brain.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO governs the p27 brake that MEN4 loses: FOXO transcription factors drive CDKN1B (p27) expression, so the regulatory network upstream of p27 ties into the cell-cycle escape that defines MEN4 endocrine tumors.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — MEN4 can share MEN1's skin signs: angiofibromas and collagenomas — fibroblast-and-collagen lesions — are reported in MEN4 as in MEN1, reflecting how convergent these near-twin syndromes are clinically.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — It joins the mTOR-linked endocrine-tumor syndromes: like tuberous sclerosis, which also seeds pancreatic neuroendocrine tumors through mTOR overactivity, MEN4 predisposes to endocrine neoplasia and is managed with overlapping surveillance.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — AKT controls the very brake MEN4 loses: AKT phosphorylates and inactivates the p27 (CDKN1B) cell-cycle inhibitor, so the germline CDKN1B loss of MEN4 mimics the unchecked proliferation that AKT signaling would otherwise drive.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Lost cell-cycle restraint meets growth signaling: with p27 gone, MEN4 neuroendocrine cells proliferate under STAT3 and other pro-growth pathways, part of the signaling that fuels its parathyroid and pituitary tumors.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its hyperparathyroidism harms the kidneys: like MEN1, MEN4's primary hyperparathyroidism causes hypercalcemia, nephrolithiasis and nephrocalcinosis that can progress to chronic kidney disease.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Its pancreatic and pituitary tumors derange glucose: MEN4's neuroendocrine tumors and any acromegaly from a growth-hormone-secreting pituitary tumor disturb glucose metabolism, while pancreatic surgery can leave a secondary diabetes.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Hormones and hereditary surveillance weigh on mood: hypercalcemia's psychiatric effects, any Cushing's from a pituitary tumor and the burden of lifelong multi-tumor monitoring contribute to depression in MEN4.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Its tumors and renal disease lower the count: advanced neuroendocrine tumors with their inflammation, plus the renal impairment from hyperparathyroidism, can produce an anemia of chronic disease.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Its hormone-secreting tumors raise blood pressure: like MEN1, MEN4's primary hyperparathyroidism and functioning pituitary and neuroendocrine tumors contribute to secondary hypertension.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Recurrent endocrine surgery taxes healing: the parathyroid, pituitary and pancreatic operations MEN4 requires leave repeated surgical wounds to heal over the patient's lifetime.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong tumor surveillance breeds worry: the constant biochemical and imaging screening for the multiple endocrine tumors of MEN4, and its hereditary nature, foster chronic health anxiety.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its hyperparathyroidism stones the kidneys: the primary hyperparathyroidism that dominates MEN4 raises calcium and causes recurrent kidney stones and nephrocalcinosis threatening renal function.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its pituitary tumours press on the brain: MEN4 pituitary adenomas can compress the optic chiasm and surrounding structures, causing visual-field loss, headache and cranial-nerve palsies.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its pancreatic tumours ulcerate the gut: gastrinomas in MEN4 secrete gastrin to cause the refractory peptic ulcers of Zollinger-Ellison syndrome, alongside other gastroenteropancreatic NETs.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Parathyroid excess dissolves bone: primary hyperparathyroidism — its most common feature — drives osteoclastic bone resorption with osteitis fibrosa and fragility fractures.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its high calcium unsettles the heart: the hypercalcaemia of MEN4 hyperparathyroidism shortens the QT interval and can cause arrhythmias and hypertension.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It can mark the skin: like MEN1, MEN4 can produce cutaneous angiofibromas and collagenomas among its varied manifestations.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Its neuroendocrine tumours get targeted drugs: like MEN1, MEN4 produces pancreatic and pituitary neuroendocrine tumours treatable with mTOR inhibitors and somatostatin analogues.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — Gastrinomas ulcer without it: MEN4 can cause Zollinger-Ellison syndrome whose severe peptic ulcers, unlike the common kind, are not driven by Helicobacter pylori.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — A fellow tumour syndrome with neuroendocrine tumours: NF1, like MEN4, can cause duodenal neuroendocrine tumours and phaeochromocytoma, overlapping its endocrine spectrum.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — Its pancreatic tumours arise here: like MEN1, MEN4 predisposes to islet-cell neuroendocrine tumours of the pancreas alongside parathyroid and pituitary tumours.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — A fellow endocrine-tumour syndrome: MEN4, like Cowden syndrome, is an inherited predisposition to multiple endocrine and other tumours requiring lifelong gland surveillance.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for advanced neuroendocrine tumours: metastatic pancreatic neuroendocrine tumours in MEN4 are treated with chemotherapy such as capecitabine-temozolomide alongside targeted agents.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Like MEN1, it starts in the parathyroids: hyperparathyroidism is the leading MEN4 feature, and the high PTH it drives resorbs cortical bone—causing osteoporosis and fractures—so the skeleton registers the endocrine tumour.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Two brakes on the cell cycle lost: MEN4 arises from loss of CDKN1B (p27), a CDK inhibitor that restrains G1→S, much as retinoblastoma arises from loss of RB1 downstream in the same checkpoint—different stops on one cell-cycle pathway.
- `connects-to` → **[CDKN1A](../../03-molecular/cdkn1a/README.md)** — Its gene has a sibling brake: MEN4 is caused by loss of CDKN1B (p27); CDKN1A (p21) is the closely related CIP/KIP-family CDK inhibitor that enforces the same G1/S checkpoint, so the two share the job MEN4's mutation abolishes.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Hypercalcaemia and the kidney: like MEN1, MEN4's primary hyperparathyroidism raises calcium and causes kidney stones and nephrocalcinosis that scar the glomerulus.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Gastrinomas and peptic ulcers: pancreatic and duodenal gastrinomas in MEN4 can cause Zollinger-Ellison syndrome with refractory ulcers eroding the intestinal epithelium.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Germline endocrine-tumour syndromes: MEN4 (CDKN1B) and DICER1 both predispose to pituitary and other endocrine tumours, two of the autosomal-dominant syndromes warranting multi-gland surveillance.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The metastatic sink: like MEN1, the enteropancreatic neuroendocrine tumours of MEN4 spread to the liver, and this hepatic involvement through the lobule largely determines prognosis and survival.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Functional carcinoids: enteropancreatic and foregut neuroendocrine tumours in MEN4 can secrete serotonin, and once they reach the liver the hormone drives the flushing and diarrhoea of carcinoid syndrome.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — Valve scarring from hormone overflow: serotonin from liver-metastatic MEN4 carcinoids lays down fibrous plaque on the right-heart valves and endocardium, the substrate of carcinoid heart disease.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Released cell cycle: loss of the p27/CDKN1B brake in MEN4 frees the CDK-RB-E2F axis, letting E2F1 drive the cell-cycle entry of its endocrine tumours.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Vascular neuroendocrine tumours: HIF-1α-driven, VEGF-rich angiogenesis makes MEN4 neuroendocrine tumours highly vascular, supporting anti-angiogenic therapy.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative persistence: TERT reactivation maintaining telomeres accompanies the progression of MEN4 endocrine tumours toward more aggressive disease.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Proliferative oncogene: loss of the p27 (CDKN1B) brake in MEN4 permits unrestrained cell-cycle entry, with MYC driving the proliferation of its endocrine tumours.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Endocrine tumour signalling: aberrant Wnt/β-catenin activation contributes to the parathyroid and pituitary tumours of the MEN4 spectrum.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic progression: EZH2-mediated PRC2 silencing of tumour-suppressor genes contributes to the development of MEN4-associated neuroendocrine tumours.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Prolactinoma therapy: dopamine agonists treat the prolactin-secreting pituitary adenomas of the MEN4 spectrum, exploiting dopamine's tonic inhibition of pituitary prolactin release.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Gastrinoma acid: gastrinomas in the MEN4 spectrum drive gastrin-stimulated histamine release from gastric ECL cells, causing the acid hypersecretion of Zollinger-Ellison syndrome.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Hyperparathyroid bone loss: primary hyperparathyroidism, the most frequent MEN4 manifestation, drives PTH-stimulated RANKL-mediated osteoclast activity and bone resorption.
- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — FOXO1 transcriptionally induces p27 (CDKN1B), the very CDK inhibitor whose germline loss defines MEN4—so the FOXO-p27 axis is the precise regulatory pathway short-circuited in the syndrome's endocrine tumors.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — With primary hyperparathyroidism the most frequent MEN4 feature, calcitonin from thyroid C cells acts as the physiological counterweight to the PTH-driven hypercalcemia that results from the parathyroid tumors.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4-CXCL12 signaling drives the metastasis of the pancreatic neuroendocrine tumors of the MEN4 spectrum, the spread that worsens prognosis when these otherwise indolent tumors progress.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Like MEN1, MEN4 most often presents with parathyroid tumors causing hypercalcemia from excess PTH, the commonest and usually earliest manifestation that prompts the genetic testing distinguishing it from MEN1.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β signaling normally induces the CDK inhibitor p27 (CDKN1B) to arrest the cell cycle, so the CDKN1B loss that causes MEN4 disables this growth-suppressive output, releasing endocrine cells to proliferate.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — MEN4 predisposes to pancreatic neuroendocrine tumors that can secrete hormones such as glucagon, gastrin or insulin, the functioning tumors whose hormonal syndromes can be the presenting feature.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA drives the PI3K-AKT-mTOR pathway (AKT and mTOR already mapped) in the pancreatic neuroendocrine tumors of MEN4, the basis for mTOR-inhibitor therapy.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Growth-factor-driven RAS-MAPK-ERK signaling promotes proliferation of the parathyroid, pituitary and pancreatic tumors of MEN4, complementing the loss of p27-mediated cell-cycle restraint.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling shapes the differentiation and growth of neuroendocrine tumors, a pathway dysregulated in the pancreatic and pituitary tumors of MEN4.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss releases the PI3K-AKT-mTOR axis (AKT, PIK3CA and mTOR already mapped) driving the neuroendocrine tumors of MEN4, the p27/CDKN1B-deficient counterpart of MEN1.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — The VEGF/PDGF angiogenic axis (VEGF already mapped) supports the vascular neuroendocrine tumors of MEN4.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-MAPK signaling (ERK1/2 already mapped) provides a proliferative input to the parathyroid, pituitary and pancreatic tumors of MEN4.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is a marker and modulator of the neuroendocrine and parathyroid tumors arising in MEN4 syndrome.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 mapped) provides a proliferative input to the endocrine tumors of MEN4 syndrome.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Disrupted TGF-β-SMAD growth-suppressive signaling (SMAD4 mapped) contributes to the endocrine tumorigenesis of MEN4, in which loss of the CDK inhibitor p27 removes a key proliferative brake.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune microenvironment of the neuroendocrine tumors that arise in MEN4 syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory microenvironment of the p27-deficient endocrine tumors of MEN4 syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated CD8 cytotoxicity contributes to the immune surveillance of the neuroendocrine tumors that arise in MEN4 syndrome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and survival signaling of the endocrine tumors of MEN4 syndrome.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation restrains apoptosis in the endocrine tumors of MEN4 syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of MEN4-associated neuroendocrine tumors.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative signaling of the endocrine tumors of MEN4 syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the neuroendocrine tumors of MEN4 syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the p27-deficient endocrine tumor cells of MEN4 syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the endocrine tumors of multiple endocrine neoplasia type 4.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of multiple endocrine neoplasia type 4.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of multiple endocrine neoplasia type 4.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of MEN4 syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of MEN4 syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of MEN4 syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of the neuroendocrine neoplasms of MEN4 syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of MEN4 syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of MEN4 syndrome.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Gastrinoma acid: like MEN1, MEN4 can include gastrinomas that drive massive gastric acid (proton) secretion (Zollinger-Ellison syndrome), causing refractory peptic ulceration managed with high-dose proton-pump inhibitors.
- `connects-to` → **[Insulin receptor](../../03-molecular/insulin-receptor/README.md)** — Insulinoma hypoglycaemia: functional pancreatic neuroendocrine tumours in MEN4 can oversecrete insulin (already mapped), which through the insulin receptor produces the fasting hypoglycaemia of an insulinoma.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Carcinoid heart disease: serotonin-secreting neuroendocrine tumours in the MEN4 spectrum (serotonin already mapped) can cause carcinoid heart disease with valvular fibrosis, and troponin marks the associated myocardial strain.
- `connects-to` → **[ACTH](../../03-molecular/acth/README.md)** — Ectopic Cushing: neuroendocrine tumours in MEN4 can secrete ACTH ectopically, driving cortisol excess (already mapped) and Cushing syndrome, one of the functional hormone syndromes of its pituitary and pancreatic tumours.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Adrenal adenomas: adrenocortical tumours in the MEN4 spectrum (adrenal gland already mapped) can oversecrete aldosterone, causing primary aldosteronism with hypertension and hypokalaemia beyond the classic parathyroid-pituitary-pancreas triad.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with the strongly expressed VEGF (already mapped) supports the rich vasculature of the neuroendocrine tumours of MEN4, part of the angiogenic biology targeted by antiangiogenic and mTOR (already mapped) therapy.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Mineral dysregulation: the primary hyperparathyroidism of MEN4 (PTH and calcium already mapped) disturbs magnesium alongside calcium handling, part of the mineral derangement of the commonest manifestation of the syndrome.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Enteropancreatic tumours: GLP-1 and the incretin axis reflect the enteropancreatic neuroendocrine biology of the MEN4 pancreatic tumours (insulin and glucagon already mapped), part of the functional-tumour spectrum shared with MEN1 (already mapped).
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the microenvironment of the MEN4 neuroendocrine tumours dampens the anti-tumour immune response, part of the immune biology relevant to the immunotherapy of any aggressive metastatic tumour.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the MEN4 neuroendocrine tumours.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the MEN4 neuroendocrine tumours.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Islet zinc: zinc is stored with insulin (already mapped) in the islet secretory granules, and the zinc-insulin hexamer is part of the biology of the insulinomas and other pancreatic neuroendocrine tumours of MEN4.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Steroidogenesis substrate: cholesterol is the precursor of the cortisol and aldosterone (already mapped) of the adrenocortical (adrenal already mapped) tumours that occur in MEN4.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Islet-tumour metabolic adipokine: leptin reflects the metabolic disturbance of the insulinoma and glucagonoma (insulin and glucagon already mapped) and the endocrine tumours of MEN4.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic disturbance of the endocrine tumours of MEN4.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the metabolic disturbance of the endocrine tumours of MEN4.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — NET immunosurveillance: the cytotoxic T cells (perforin already mapped) provide the immune surveillance of the pancreatic and other neuroendocrine tumours of MEN4.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon and NETs: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway and historically used to treat the neuroendocrine tumours, is part of the innate-immune dimension of MEN4.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 immunosurveillance: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunosurveillance of the neuroendocrine tumours of MEN4.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the MEN4 neuroendocrine tumours.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the MEN4 tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the MEN4 neuroendocrine tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the MEN4 tumours.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the MEN4 neuroendocrine tumours.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the MEN4 neuroendocrine tumours.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the macrophages are a dominant myeloid population of the stroma of the well-vascularised (VEGF already mapped) MEN4 neuroendocrine tumours.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the MEN4 neuroendocrine tumour stroma.

[^alrezk-2017-men4]: Alrezk R, Hannah-Shmouni F, Stratakis CA. MEN4 and CDKN1B mutations: the latest of the MEN syndromes. *Endocr Relat Cancer.* 2017;24(10):T195-T208. [doi:10.1530/ERC-17-0243](https://doi.org/10.1530/ERC-17-0243) · [PubMed 28894007](https://pubmed.ncbi.nlm.nih.gov/28894007/)
[^pellegata-2006-cdkn1b-men4]: Pellegata NS, Quintanilla-Martinez L, Siggelkow H, et al. Germ-line mutations in p27Kip1 cause a multiple endocrine neoplasia syndrome in rats and humans. *Proc Natl Acad Sci USA.* 2006;103(42):15558-15563. [doi:10.1073/pnas.0603306103](https://doi.org/10.1073/pnas.0603306103) · [PubMed 17030811](https://pubmed.ncbi.nlm.nih.gov/17030811/)
