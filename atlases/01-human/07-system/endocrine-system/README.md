---
schema: human-scale-entry/v1
id: endocrine-system
name: Endocrine System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-05
summary: "Network of glands releasing hormones into blood to regulate metabolism, growth, reproduction, stress, and water balance. Integrates nervous and immune systems via hypothalamic-pituitary axes (HPA, HPT, HPG). Encompasses peptide, steroid, and tyrosine-derived hormone classes."
aliases: ["hormonal system", "endocrine glands", "HPA axis", "HPT axis", "HPG axis"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/pancreas
    relation: contains
    note: "Pancreatic islets of Langerhans (insulin [β-cells], glucagon [α-cells], somatostatin [δ-cells]) are central glucose regulators; T1DM = autoimmune β-cell destruction; T2DM = insulin resistance + progressive β-cell failure."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Hypothalamus integrates nervous and endocrine systems; CRH, TRH, GnRH, GHRH control anterior pituitary; AVP and oxytocin store in posterior pituitary; glucocorticoids, thyroid hormones, and sex steroids feed back to regulate CNS and behaviour."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Cortisol, oestrogens, and androgens regulate immune cell trafficking, cytokine production, and lymphocyte apoptosis; HPA-axis cortisol → immunosuppression; thymic involution driven by sex steroids reduces T-cell output with age."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "ANP/BNP (heart), aldosterone (adrenal), ADH (posterior pituitary), EPO (kidney), and catecholamines (adrenal medulla) together regulate blood pressure, volume, and cardiac output; hyperthyroidism, Cushing's, and phaeochromocytoma cause CVD."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin (β-cell peptide) coordinates fed-state metabolism: ↑GLUT4 in muscle/adipose, ↑glycogen synthesis, ↓hepatic gluconeogenesis, ↑lipogenesis; GLP-1 agonists (semaglutide, tirzepatide) amplify insulin secretion; insulin resistance drives T2DM, metabolic syndrome, and NAFLD."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol (adrenal glucocorticoid, HPA axis: CRH→ACTH→cortisol) is the key stress hormone: ↑gluconeogenesis, ↑lipolysis, anti-inflammatory (↓NF-κB, ↓COX-2), permissive for catecholamine action; Cushing's syndrome = chronic cortisol excess; Addison's disease = cortisol deficiency."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Glucagon (α-cell peptide) opposes insulin in fasting: ↑hepatic glycogenolysis and gluconeogenesis via PKA/CREB; hypersecretion amplifies hyperglycemia in T2DM; GLP-1 agonists (semaglutide) suppress glucagon release; glucagon receptor antagonists in clinical trials for T2DM."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Carney complex shows how one signaling defect can derange the endocrine system: germline PRKAR1A loss leaves protein kinase A constitutively active, spawning tumors across adrenal, pituitary, thyroid, and gonad — a model of the cAMP-PKA cascade driving multi-gland neoplasia."
  - target: 01-human/06-organ/adrenal-gland
    relation: contains
    note: "The adrenal gland is a dual endocrine organ: its cortex makes steroid hormones (cortisol, aldosterone, androgens) under HPA and RAAS control, while its medulla — modified sympathetic tissue — secretes catecholamines; disorders span Cushing's, Addison's, Conn's, and pheo."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes is the most common endocrine disease: insulin resistance plus progressive β-cell failure dysregulate the body's central metabolic hormone, and its complications (retinopathy, nephropathy, neuropathy) make it a leading cause of blindness, kidney failure, and CVD."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "MEN1 shows how the endocrine system fails as a network: a single germline MEN1 mutation predisposes to synchronous tumors of the parathyroids, pancreatic islets and pituitary, illustrating that endocrine glands share pathways whose disruption causes multi-gland hyperfunction."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Growth hormone exemplifies the endocrine system's hierarchical axes: the hypothalamus and pituitary release GH, which acts via hepatic IGF-1 on growth and metabolism under feedback control; its excess (acromegaly) or deficiency shows how one hormone integrates the network."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The reproductive system is a major endocrine organ: the hypothalamic-pituitary-gonadal axis secretes sex steroids (estrogen, testosterone) that drive puberty, fertility and secondary sexual characteristics and feed back on the brain, weaving reproduction into hormonal control."
  - target: 01-human/06-organ/thyroid
    relation: contains
    note: "The thyroid is the body's metabolic thermostat: hypothalamic TRH and pituitary TSH drive it to release T3/T4 that set metabolic rate, heart rate and thermogenesis, feedback closing the HPT axis—hyper- and hypothyroidism are among the commonest endocrine disorders."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Thyroid cancer is the most common endocrine malignancy: most are papillary tumors that retain TSH responsiveness and iodine uptake, allowing radioactive-iodine therapy and thyroglobulin monitoring—a rare cancer treated through its own hormonal physiology."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium homeostasis is a core endocrine task: parathyroid hormone, calcitonin and calcitriol tune blood calcium via bone, gut and kidney—disorders like hyperparathyroidism or vitamin-D deficiency show the endocrine system guarding one ion's narrow range."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid hormones show how the endocrine system runs on feedback loops: the hypothalamic-pituitary-thyroid axis tunes T3/T4 to set metabolic rate, and disrupting any level causes hypo- or hyperthyroidism—a model for the feedback that governs all endocrine glands."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Type 1 diabetes is autoimmune destruction within the endocrine system: T cells kill pancreatic beta cells, eliminating insulin and proving how loss of a single endocrine cell type disrupts whole-body fuel metabolism—an organ-specific failure of the endocrine network."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen shows the endocrine system's reach beyond metabolism: this gonadal steroid, set by the hypothalamic-pituitary-gonadal axis, controls reproduction but also bone, cardiovascular and brain function—so endocrine signaling integrates far-flung organ systems."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Testosterone is a central output of the endocrine system: the testes make it under pituitary LH control, and it drives male sexual development, muscle and bone—so it exemplifies the hypothalamic-pituitary-gonadal axis that the endocrine system coordinates."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Aldosterone shows the endocrine system regulating salt and blood pressure: the adrenal cortex secretes it under the renin-angiotensin system to retain sodium, so its excess (Conn syndrome) or deficiency (Addison's) are classic endocrine electrolyte and pressure disorders."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Osteoporosis is largely an endocrine disease of bone: estrogen, testosterone, thyroid, parathyroid and cortisol all govern bone turnover, so hormonal shifts—menopause, hyperthyroidism, steroid excess—are leading causes, tying the skeleton to the endocrine system."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "The pineal gland completes the endocrine system with melatonin: this hormone translates darkness into a sleep-timing signal, so the endocrine system governs not just metabolism and growth but the body's daily clock."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is a hidden endocrine organ: it secretes erythropoietin to drive red-cell production, renin to control blood pressure, and activates vitamin D, so kidney failure causes anemia, hypertension, and bone disease through lost hormones."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Fat is an endocrine organ, and obesity disrupts it: adipose tissue secretes leptin, adiponectin, and estrogen, so excess fat rewires hormonal signaling—driving insulin resistance, reproductive disturbance, and hormone-sensitive cancers."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "The endocrine system depends on dietary iodine: the thyroid traps iodine to build thyroid hormones that set the body's metabolic rate, so iodine deficiency produces goiter and hypothyroidism—a mineral shortage with system-wide hormonal consequences."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "The endocrine system runs on feedback loops like ACTH's: the pituitary releases ACTH to drive adrenal cortisol, which loops back to shut off ACTH—the kind of hormonal thermostat that keeps every endocrine axis in balance."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "The gut is an endocrine organ too, via ghrelin: the stomach releases ghrelin before meals to signal hunger to the brain, showing the endocrine system reaches into the digestive tract—not just the classic hormone glands."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Fat is an endocrine organ in its own right: adipocytes secrete leptin, adiponectin and other hormones that report energy stores and tune metabolism, so the endocrine system extends well beyond the classic glands into body fat."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain is the endocrine system's command center: the hypothalamus and pituitary it houses release the master hormones that drive the thyroid, adrenal and gonadal axes, so neural signals set the rhythm of the whole hormonal orchestra."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Parathyroid hormone runs the body's calcium thermostat: when blood calcium dips, the parathyroid glands release PTH to pull calcium from bone and kidney, a tightly regulated endocrine loop essential to nerves, muscle and bone."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "The endocrine system runs partly on zinc: pancreatic beta cells store insulin in zinc-containing crystals, and the metal is needed to make and stabilize the hormone, tying a trace element to blood-sugar control."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Light tunes the endocrine clock through photons: light striking the eye signals the pineal gland to halt melatonin by day and release it by night, so the sun sets the hormonal rhythm of the whole body."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The stomach is a hormone gland too: it secretes ghrelin, the hunger hormone that signals the brain to eat, making the gut a full member of the endocrine system beyond the classic glands."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus reins in the hormonal stress axis: dense in cortisol receptors, it provides the negative feedback that switches off the HPA axis, so chronic stress that damages it lets cortisol run high."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The endocrine system begins in neurons: hypothalamic neurosecretory cells release hormones that command the pituitary, and the adrenal medulla is itself made of modified neurons, blurring nerve and gland."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "The endocrine system guards sodium: aldosterone from the adrenal cortex tells the kidney to retain salt and water, the hormonal control of blood volume and pressure."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals what makes a cell endocrine: its cytoplasm is packed with dense-core secretory granules, membrane-bound stores of hormone poised for release — the universal signature of the glands that signal through the blood."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart is a gland in its own right: stretched by a full circulation, it secretes natriuretic peptides that order the kidney to dump salt and water, making the heart an endocrine organ that regulates blood volume."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Hormones tune phosphate as well as calcium: parathyroid hormone, vitamin D, and bone-derived FGF23 form a feedback loop that balances phosphorus, the endocrine control of the mineral that builds bone and powers ATP."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The endocrine glands are favorite autoimmune targets: antibodies against the thyroid (Hashimoto, Graves), pancreatic islets (type 1 diabetes), and adrenal cortex (Addison) cause much endocrine disease, sometimes clustering as autoimmune polyglandular syndromes."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is an endocrine organ in its own right: it makes IGF-1 under growth hormone's command, angiotensinogen, hepcidin, and thrombopoietin, and it clears and activates hormones — a hub of the body's chemical signaling."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Endocrine disease declares itself in the eye: Graves disease pushes the eyes forward into orbitopathy, and a pituitary tumor pressing the optic chiasm carves out the classic bitemporal loss of peripheral vision."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Fat itself is an endocrine organ: adipocytes secrete leptin in proportion to fat stores, and the hormone signals the hypothalamus to curb appetite — the discovery that recast adipose tissue as part of the endocrine system rather than inert storage."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D is really a hormone: the skin and kidney convert it to calcitriol, a steroid hormone that acts through nuclear receptors to raise calcium absorption, placing this 'vitamin' squarely within the endocrine system's calcium control."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "A tumor can hijack the stress hormones: pheochromocytoma of the adrenal medulla floods the body with catecholamines, causing pounding spells of hypertension, palpitations and sweating — endocrine signaling turned into a dangerous excess."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Prolactin shows the pituitary's reach: this anterior-pituitary hormone drives lactation under hypothalamic dopamine control, and its overproduction — the commonest pituitary tumor — causes infertility and milk discharge."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The gut is the body's largest endocrine organ: scattered enteroendocrine cells of the small intestine secrete incretins, ghrelin, secretin, and cholecystokinin that tune digestion, appetite, and insulin release."
  - target: 01-human/07-system/men4-syndrome
    relation: connects-to
    note: "One gene can derail many glands: MEN4, like MEN1, is a hereditary syndrome that spawns synchronous tumors across the parathyroid, pituitary, and pancreas, the endocrine system failing along an inherited fault line."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Oxytocin is a posterior-pituitary output of the system: synthesized in the hypothalamus and released from the neurohypophysis, it drives labor contractions and milk ejection, a neuroendocrine hormone bridging brain and body."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Vasopressin completes the posterior-pituitary pair: this hypothalamic hormone conserves water at the kidney and raises blood pressure, and its deficiency or resistance causes diabetes insipidus — an endocrine axis distinct from the anterior pituitary's."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Calcitonin rounds out calcium control: secreted by thyroid C-cells it lowers blood calcium opposite parathyroid hormone, and as a tumor marker it flags medullary thyroid carcinoma within the endocrine system."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Its hormone-making cells can turn into tumors: neuroendocrine tumors arise from the dispersed endocrine cells of the gut, pancreas and lungs, sometimes secreting hormones that cause florid syndromes — the malignant face of the endocrine system."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "The gut is the body's largest endocrine organ: L-cells release the incretin GLP-1 after meals to spur insulin and curb appetite, the gut-hormone axis now harnessed by blockbuster diabetes and weight drugs."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "Bone is an endocrine organ too: osteocytes secrete FGF23 to tell the kidney to excrete phosphate and curb active vitamin D, a bone-kidney hormonal axis that fails early in chronic kidney disease."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "An old infection can shut down the adrenals: tuberculosis is a classic cause of primary adrenal insufficiency (Addison's), destroying the adrenal cortex and crippling the body's cortisol and aldosterone output."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "It seeds tumors across endocrine glands: VHL disease causes pheochromocytomas of the adrenal medulla and pancreatic neuroendocrine tumors, a hereditary disorder striking multiple endocrine organs at once."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "It targets the thyroid above all: Cowden syndrome causes goiter, benign thyroid nodules and a high risk of thyroid cancer, one of its defining endocrine manifestations alongside breast and uterine tumors."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Hormone excess drives secondary hypertension: Cushing's, primary aldosteronism, pheochromocytoma and thyroid disorders raise blood pressure, making the endocrine system a key source of treatable secondary hypertension."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its hormones shape the heart: thyroid excess or deficiency, acromegaly and catecholamine-secreting tumors all remodel the myocardium, so endocrine disease is an important reversible cause of heart failure."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Hormones set the tenor of mood: thyroid dysfunction, cortisol excess or deficiency and sex-hormone shifts profoundly affect mood, so endocrine disorders frequently present with depression."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The gut is a vast endocrine organ: incretins, gastrin, ghrelin and other gut hormones regulate digestion and metabolism, and the pancreas is both an endocrine and a digestive gland."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The kidney is itself an endocrine gland: it secretes erythropoietin and renin and activates vitamin D, while it is also the target of aldosterone, ADH and parathyroid hormone."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Hormones are written on the skin: endocrine disease shows as acanthosis nigricans of insulin resistance, the hyperpigmentation of Addison's, myxoedema of thyroid disease and vitiligo of autoimmunity."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Hormones build and maintain the frame: parathyroid hormone, vitamin D, sex steroids, growth hormone and cortisol govern bone and muscle, so endocrine disease causes osteoporosis, acromegalic arthropathy and steroid myopathy."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It reaches into the lungs: the pulmonary endothelium activates angiotensin via ACE, and endocrine disorders affect breathing — acromegaly causes sleep apnoea and hypothyroidism causes hypoventilation."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The thymus is an endocrine-immune organ: it secretes thymic hormones that direct T-cell maturation, and thyroid autoimmunity such as Graves' disease drives thymic hyperplasia."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "The commonest Cushing's is iatrogenic: exogenous glucocorticoids like prednisolone and dexamethasone suppress the hypothalamic-pituitary-adrenal axis and cause Cushing syndrome, the archetype of drug-induced endocrine disease."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "A mineral the hormones need: magnesium is required for insulin sensitivity and parathyroid-hormone secretion, so deficiency disturbs glucose and calcium regulation."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Zinc underpins hormone signalling: it is essential for insulin storage in the pancreas and for testosterone and thyroid-hormone production, so deficiency impairs growth and reproduction."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "The most-prescribed endocrine drug: metformin lowers hepatic glucose output as first-line therapy for type 2 diabetes and is also used in polycystic ovary syndrome, an everyday tool of endocrinology."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "It can destroy the glands: tuberculosis is a classic cause of primary adrenal insufficiency (Addison's disease) through bilateral adrenal destruction, and can also trigger SIADH."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy unleashes endocrinopathy: PD-1 and CTLA-4 inhibitors commonly cause immune-related thyroiditis, hypophysitis, adrenalitis and autoimmune diabetes, among the most frequent toxicities of cancer immunotherapy."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "The pancreas is an endocrine organ too: the islets of Langerhans secrete insulin, glucagon and somatostatin to govern blood glucose, making the endocrine pancreas central to the system and the seat of diabetes."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Bone is both target and gland: PTH, calcitonin, vitamin D, oestrogen and thyroid hormone remodel cortical bone, while bone itself secretes FGF23 and osteocalcin — a two-way endocrine relationship governing calcium and phosphate."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Hormone pathways are drug targets: somatostatin analogues and peptide-receptor radionuclide therapy treat neuroendocrine tumours, while mTOR inhibitors and hormone-receptor-directed agents act on endocrine tumours and their hormone axes."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "The growth-hormone effector: most of growth hormone's actions work through liver-made IGF-1, the axis disrupted in acromegaly and gigantism—a core endocrine feedback loop measured to diagnose GH excess."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "A temporary endocrine organ: in pregnancy the placenta becomes a massive hormone factory, secreting hCG, progesterone, oestrogen and placental lactogen that reshape maternal metabolism."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Inherited endocrine tumours: DICER1 predisposes to thyroid cancer, pituitary blastoma and ovarian sex-cord tumours, one of the germline syndromes that strike multiple endocrine glands."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Endocrine tumours in a neurocutaneous syndrome: neurofibromatosis type 1 predisposes to phaeochromocytoma and other endocrine tumours, linking a nerve-sheath disorder to the endocrine system."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "Starvation reshapes hormones: anorexia nervosa suppresses the hypothalamic-pituitary axes—amenorrhoea, low thyroid and sex hormones, high cortisol—a functional endocrine disorder driven by energy deficit."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Infection hits the glands: COVID-19 can trigger subacute thyroiditis, new-onset diabetes and adrenal dysfunction, the virus reaching multiple endocrine organs that express ACE2."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Top of the stress axis: corticotropin-releasing hormone from the hypothalamus drives ACTH and cortisol release, the apex of the hypothalamic-pituitary-adrenal endocrine cascade."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "Blood-pressure hormone cascade: renin initiates the renin-angiotensin-aldosterone system, the endocrine loop controlling blood pressure, sodium and potassium balance."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Reproductive steroid axis: progesterone, with estrogen and testosterone, is a core gonadal steroid hormone of the endocrine system governing the menstrual cycle and pregnancy."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Adrenal medulla hormone: epinephrine is the endocrine system's fast-response hormone, released from the adrenal medulla to drive the fight-or-flight metabolic and cardiovascular surge."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Prolactin brake: hypothalamic dopamine tonically inhibits pituitary prolactin release, an endocrine control point whose loss—or dopamine-blocking drugs—causes hyperprolactinaemia."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Renal endocrine hormone: erythropoietin from the kidney shows the endocrine system extends beyond classic glands, the hormone tying oxygen sensing to red-cell production."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "RAAS effector hormone: angiotensin II is the active hormone of the renin-angiotensin-aldosterone system, raising blood pressure and driving aldosterone release in the endocrine control of fluid and salt."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipose endocrine organ: adiponectin from fat exemplifies adipose tissue as an endocrine organ, its hormones signalling insulin sensitivity and energy balance to the rest of the body."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "Cardiac endocrine hormone: BNP secreted by the stretched heart shows even the cardiovascular system is endocrine, the natriuretic hormone that signals volume status to the kidney."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Steroid signal transduction: the glucocorticoid receptor is the intracellular receptor through which cortisol exerts its wide-ranging metabolic, immune and stress effects — the effector arm of the HPA endocrine axis."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Androgen signal transduction: the androgen receptor mediates the actions of testosterone and DHT across reproductive and somatic tissues, the nuclear-receptor endpoint of the male endocrine axis."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Inhibitory regulation: somatostatin acting on SSTR2 broadly suppresses the secretion of growth hormone, insulin, glucagon and gut hormones — the basis for octreotide's use across endocrine tumours and acromegaly."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Mineral homeostasis: serum calcium is the regulated variable of a dedicated endocrine axis — parathyroid hormone and vitamin D raise it, calcitonin lowers it — the tightly controlled ion essential for nerve, muscle and bone whose dysregulation causes endocrine disease."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Peptide gonadal feedback: the activin-inhibin system provides a peptide feedback loop, distinct from the steroid hormones, that tunes pituitary FSH secretion and gonadal function, layered onto the classic steroid-hormone axes of the endocrine system."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Vasoactive endocrine peptide: adrenomedullin, secreted widely including by the adrenal medulla and endothelium, is a potent vasodilator and part of the endocrine control of vascular tone and fluid balance, integrating the hormonal and cardiovascular systems."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Hormone-receptor coupling: the insulin receptor transduces the signal of insulin (already mapped) into target cells, the prototypical endocrine receptor linking a circulating hormone to cellular metabolism."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Energy-balance peptide: neuropeptide Y is a hypothalamic orexigenic signal that integrates the endocrine control of appetite and energy balance alongside the adipokine and gut hormones leptin and ghrelin (both mapped)."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vascular endocrine tone: endothelin-1 is a potent paracrine and endocrine vasoconstrictor that, with the renin-angiotensin and adrenomedullin systems already mapped, helps set the hormonal control of vascular tone and fluid balance."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Hormone signal transduction: AKT is the central kinase transducing insulin and IGF-1 receptor signalling (both already mapped) into the metabolic and growth actions of these hormones throughout the endocrine system."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Anabolic integration: mTOR integrates hormonal (insulin, IGF-1) and nutrient signals to govern the anabolic growth responses coordinated by the endocrine system."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "Energy-sensing counterbalance: AMPK is the cellular energy sensor that counterbalances the insulin/mTOR anabolic axis (both already mapped), integrating the metabolic hormones with cellular energy status."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Growth hormone, prolactin and leptin signal through JAK-STAT (their receptors are cytokine-receptor-family members), a core transduction mechanism of the endocrine system."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK transduces the receptor-tyrosine-kinase and GPCR signals of many hormones into the proliferative and trophic responses of endocrine target tissues."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β, inhibited by insulin-AKT signalling (insulin, insulin-receptor and AKT mapped), couples endocrine signalling to glycogen and metabolic control."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 transduces the growth-hormone, leptin and cytokine signals of the endocrine system and drives proliferation in many endocrine tumours."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β/activin-SMAD signalling (activin-A already mapped) provides feedback control of pituitary and gonadal hormone axes across the endocrine system."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is a marker of malignancy in thyroid and other endocrine tumours and modulates their inflammatory microenvironment."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate insulin/IGF and stress signaling across endocrine tissues, governing metabolism and hormone-secreting-cell homeostasis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the autoimmune and inflammatory processes that target endocrine glands across the endocrine system."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α couples the oxygen and metabolic status of endocrine glands to their hormone-secretory and proliferative responses."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) transduces the growth-factor and insulin signals that govern endocrine-cell proliferation and hormone secretion across the endocrine system."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING links cellular stress to the autoimmune and inflammatory endocrinopathies of the endocrine system."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB inflammatory signaling participates in the autoimmune and stress-related dysregulation of the endocrine glands."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the endocrine-cell homeostasis and hormone-secretory-granule turnover of the endocrine system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the growth-factor and hormone-receptor signal transduction of the endocrine system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of hormone-gene expression and endocrine-cell identity of the endocrine system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment participates in the immune surveillance and endocrine-autoimmune responses of the endocrine system."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the endocrine-gland vascularization and cell homeostasis of the endocrine system."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the neuroendocrine-immune interactions of the endocrine system."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β signaling participates in the neuroendocrine-immune regulation of the hypothalamic-pituitary-adrenal axis of the endocrine system."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroendocrine-immune interactions of the endocrine system."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the immune-endocrine interactions of the endocrine system."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Neuroendocrine signalling: serotonin is a neuroendocrine hormone made by gut enterochromaffin cells and the pineal gland, and its overproduction by neuroendocrine (carcinoid) tumours illustrates the diffuse endocrine tissue beyond the classic glands."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Paracrine hormones: prostaglandins are locally acting lipid mediators that, alongside the circulating hormones, exemplify the paracrine and autocrine signalling that broadens the endocrine system beyond gland-to-bloodstream secretion."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Gasotransmitter signalling: nitric oxide is a diffusible gaseous messenger released by endothelium and neurons, a non-classical endocrine/paracrine signal that regulates vascular tone and complements peptide and steroid hormone systems."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Steroid precursor: cholesterol is the common precursor of every steroid hormone, converted in the adrenal cortex and gonads to cortisol, aldosterone and the sex steroids (all already mapped), the biochemical root of the steroid endocrine axes."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Thyroid activation: selenium-dependent deiodinase enzymes convert thyroxine to the active triiodothyronine (thyroid hormones already mapped), making this trace element essential to the peripheral regulation of thyroid hormone action."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Cutaneous endocrine function: the skin synthesises vitamin D from cholesterol under ultraviolet light, an endocrine role that feeds the calcium-regulating axis (PTH and FGF23 already mapped) and illustrates hormone production beyond the classical glands."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron as a hormonal axis: iron homeostasis is itself an endocrine system, governed by the liver hormone hepcidin and by erythropoietin (already mapped), illustrating hormonal control extending to a trace-metal balance."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Hormone secretion cofactor: magnesium is a cofactor for the secretion and action of many hormones, including parathyroid hormone (already mapped) and insulin (already mapped), so its deficiency disturbs the endocrine calcium and glucose axes."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Thymic endocrine role: the thymus secretes thymic hormones such as thymosin and thymulin that regulate T-cell maturation, an endocrine function of a lymphoid organ that links the endocrine and immune systems."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hepatic endocrine hub: the liver produces IGF-1 (already mapped) under growth hormone (already mapped), metabolises and clears hormones, and secretes hepatokines, an endocrine hub of the body's hormonal and metabolic network."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Osmoregulatory axis: the endocrine control of sodium and water balance runs through aldosterone and vasopressin (already mapped), the renin-angiotensin (already mapped) and osmoreceptor axes governing the body's sodium homeostasis."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "The commonest endocrine disease: type 2 diabetes is the insulin (already mapped) resistance disorder of the endocrine pancreas, the most prevalent disease of the endocrine system."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium homeostasis: the endocrine control of the potassium balance runs through aldosterone (already mapped) and the insulin (already mapped) shift, core electrolyte functions of the endocrine system."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose as endocrine organ: resistin, with leptin and adiponectin (already mapped), is an adipokine of the adipose tissue acting as an endocrine organ that regulates the systemic metabolism."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Enteroendocrine amine: histamine from the enterochromaffin-like cells of the gastric mucosa drives the acid-secretion axis, one of the paracrine/endocrine amine signals of the endocrine system."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Hepatic hormone hub: the hepatocytes produce the IGF-1 under GH (already mapped) control and the angiotensinogen (renin and angiotensin already mapped), and metabolise the steroid and thyroid hormones of the endocrine system."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Bone as endocrine organ: the osteoblasts secrete the osteocalcin (a hormone modulating the insulin — already mapped — sensitivity and energy metabolism) and the FGF23 (already mapped), responding to the PTH (already mapped)."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Metabolic-syndrome disease: NASH is the hepatic manifestation of the metabolic syndrome (the insulin — already mapped — resistance and the adipokines already mapped), an endocrine/metabolic disease."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Autoimmune endocrinopathy: the IFN-γ of the T cells is the type-II interferon arm of the autoimmune destruction underlying the autoimmune endocrine diseases (type-1 diabetes, Hashimoto, Graves, Addison) of the endocrine system."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm that drives the autoimmune endocrinopathies of the endocrine system."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate autoimmune interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is implicated in the autoimmune endocrine diseases (e.g. type-1 diabetes) of the endocrine system."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 endocrinopathy: IL-17A drives the Th17 arm of the autoimmune endocrinopathies (autoimmune thyroiditis, type-1 diabetes) of the endocrine system."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 endocrine autoimmunity: IL-4 is the prototypical type-2 cytokine of the humoral autoimmunity (e.g. the Graves TSH-receptor antibodies) of the endocrine system."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Endocrine tolerance: IL-10 is the regulatory cytokine that maintains the immune tolerance and restrains the autoimmune endocrinopathies of the endocrine system."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Autoreactive CD4: the CD4 T-helper cells drive the autoreactive response (Th1/Th17, IFN-γ and IL-17 already mapped) of the autoimmune endocrinopathies (Hashimoto, Graves, type-1 diabetes) of the endocrine system."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Endocrine autoantibodies: the plasma cells secrete the autoantibodies (anti-TPO, TSH-receptor, anti-GAD) of the autoimmune endocrinopathies of the endocrine system."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the autoimmune endocrinopathies of the endocrine system."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the complement-mediated glandular injury of the autoimmune endocrinopathies of the endocrine system."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid recruitment into the inflamed endocrine glands of the autoimmune endocrinopathies."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Glandular macrophages: the macrophages infiltrate the endocrine glands and, in the autoimmune endocrinopathies, contribute to the destruction of the hormone-producing cells of the endocrine system."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-endocrine axis: TSLP, from the thymic (already mapped) and thyroid (already mapped) epithelium, primes dendritic-cell (not yet mapped) Th2 polarisation and amplifies the autoimmune attack on the hormone-producing cells of the endocrine system."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-endocrine axis: bradykinin, via B1/B2 receptors on the vasculature of the adrenal gland (already mapped), thyroid (already mapped) and pancreas (already mapped), modulates glandular blood flow and the inflammatory response in the autoimmune endocrinopathies."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement (C3 already mapped) and the contact-kinin system (bradykinin above) at the glandular vasculature of the endocrine organs, tempering autoimmune endocrine injury."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation-endocrine axis: factor H, produced by the liver and adrenal gland, limits alternative-pathway complement amplification at endocrine glandular surfaces, protecting the thyroid, pancreas, and adrenal cortex from complement-mediated autoimmune injury."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Periostin-endocrine axis: periostin, expressed in the stromal matrix of the thyroid, adrenal gland, and pancreatic islets, promotes epithelial-mesenchymal crosstalk and glandular fibrosis in autoimmune and neoplastic endocrine disease."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron-endocrine axis: transferrin shuttles iron to the thyroid for thyroid-peroxidase-catalysed thyroid-hormone synthesis and to the adrenal gland for steroidogenesis, linking systemic iron metabolism to endocrine hormone output."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Endocrine prolactin: prolactin, via PRLR on macrophages (already mapped) and osteoblasts (already mapped), modulates the adrenal-gonadal axis; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) autoimmune cascade of endocrine disease."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Endocrine oxytocin: oxytocin, via OXTR on macrophages (already mapped) and hepatocytes (already mapped), attenuates adrenal and thyroid autoimmune inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) endocrine cascade."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Endocrine vasopressin: vasopressin, via V2R on macrophages (already mapped) and hepatocytes (already mapped), modulates fluid-hormone homeostasis; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) endocrine inflammatory cascade."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Endocrine copper: copper, as cofactor of cuproenzymes in hepatocytes (already mapped) and thyroid follicular cells, supports thyroid hormone synthesis; copper deficiency impairs the NF-κB (already mapped) and IL-6 (already mapped) endocrine immune-regulation cascade."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Endocrine sulfur: sulfur, as component of glutathione in hepatocytes (already mapped) and macrophages (already mapped), scavenges ROS; sulfur deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative endocrine inflammatory cascade."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Endocrine chloride: chloride, via chloride channels in thyroid follicular cells and macrophages (already mapped), regulates thyroid hormone secretion and immune activation; chloride dysregulation amplifies the NF-κB (already mapped) endocrine cascade."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Endocrine nitrogen: nitric oxide (NO, nitrogen-derived) in endothelial cells and macrophages (already mapped) regulates hormone secretion; NO dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and adrenal-gland (already mapped) endocrine cascade."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Endocrine oxygen: mitochondrial ROS in hepatocytes (already mapped) and macrophages (already mapped) amplifies oxidative stress; ROS excess worsens NF-κB (already mapped) and IL-6 (already mapped) and thyroid (already mapped) endocrine inflammatory cascade."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Endocrine carbon: carbon-backbone metabolites in hepatocytes (already mapped) fuel acetyl-CoA and steroid hormone biosynthesis; carbon metabolic imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and adrenal-gland (already mapped) endocrine cascade."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Endocrine hydrogen: hydrogen ions regulate intracellular pH in hepatocytes (already mapped) and macrophages (already mapped); acid-base imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in endocrine gland tissue."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Endocrine TNF-α: TNF-α from macrophages (already mapped) amplifies the NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade, driving autoimmune attack on thyroid, pancreatic islet, and adrenal endocrine glands; TNF-α excess exacerbates endocrine destruction."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Endocrine TGF-β: TGF-β from macrophages (already mapped) and hepatocytes (already mapped) promotes endocrine gland fibrosis; TGF-β excess amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade in autoimmune endocrinopathies."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Endocrine pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses autoimmune endocrine surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and adrenal-gland (already mapped) cascade."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Endocrine vegf: VEGF from macrophages (already mapped) and hepatocytes (already mapped) drives endocrine gland angiogenesis; VEGF excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and adrenal-gland (already mapped) endocrine cascade."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Endocrine wnt-beta-catenin: Wnt/β-catenin in macrophages (already mapped) and hepatocytes (already mapped) regulates endocrine gland development; wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and adrenal-gland (already mapped) cascade."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "endocrine-system rankl: RANKL from osteoblasts (already mapped) and macrophages (already mapped) modulates bone-hormone crosstalk; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and IGF-1 (already mapped) endocrine cascade of the endocrine system."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "endocrine-system il-2: IL-2 on T-cells (already mapped) and macrophages (already mapped) amplifies endocrine immune regulation; il-2 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and GLP-1 (already mapped) cascade of the endocrine system."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "endocrine-system fibronectin: fibronectin in endocrine cells (already mapped) and macrophages (already mapped) maintains gland ECM; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of the endocrine system."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "endocrine-system notch: Notch signalling on endocrine cells (already mapped) and macrophages (already mapped) regulates gland development; notch excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of the endocrine system."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "endocrine-system cgrp: CGRP from endocrine cells (already mapped) and macrophages (already mapped) modulates neuroendocrine communication; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of the endocrine system."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "endocrine-system substance-p: substance-P from endocrine cells (already mapped) and macrophages (already mapped) modulates nociception; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of the endocrine system."
---

# Endocrine System

## Overview

The endocrine system is the body's long-range chemical communication network — a distributed collection of specialised secretory cells, tissues, and glands that synthesise and release **hormones** (from Greek *hormao* — to set in motion) directly into the bloodstream, enabling the regulation of distant target organs and tissues [^guyton-hall]. This distinguishes endocrine signalling (blood-borne, systemic, acting minutes to hours) from:
- **Paracrine signalling** — local mediators acting on adjacent cells (prostaglandins, NO, histamine)
- **Autocrine signalling** — cell acts on itself
- **Exocrine secretion** — secreted via ducts to body surfaces (saliva, pancreatic enzymes, bile)
- **Neurotransmitter signalling** — rapid, point-to-point (milliseconds), synaptic cleft

The endocrine system regulates virtually every physiological process: **metabolism** (thyroid hormones, insulin, glucagon, cortisol), **growth and development** (GH, IGF-1, thyroid hormones, sex steroids), **reproduction** (LH, FSH, oestrogen, progesterone, testosterone), **stress response** (cortisol, epinephrine, norepinephrine), **water and electrolyte balance** (ADH/vasopressin, aldosterone, ANP, PTH), and **circadian rhythms** (melatonin, cortisol diurnal cycle) [^stryer-biochemistry].

Critically, the endocrine system does not operate in isolation. It is deeply integrated with:
- **The nervous system** (neuroendocrine integration: hypothalamus is both a brain region and the apex of endocrine axes; autonomic nerves directly control adrenal medulla)
- **The immune system** (immunoendocrine crosstalk: glucocorticoids suppress inflammation; cytokines IL-1β and IL-6 activate the HPA axis; thymus produces thymic hormones; sex steroids modulate immune cell trafficking)
- **The cardiovascular and renal systems** (RAAS — renin-angiotensin-aldosterone system; ANP/BNP; EPO; ADH)

## Structure

### Major Endocrine Glands and Their Hormones

#### Hypothalamus

The hypothalamus is the neuroendocrine master controller, receiving neural inputs from limbic cortex, brainstem, retina, and peripheral sensors, and translating them into peptide hormone outputs [^guyton-hall]:

| Hypothalamic hormone | Target | Effect |
|:---|:---|:---|
| CRH (corticotropin-releasing hormone) | Anterior pituitary | ↑ ACTH release |
| TRH (thyrotropin-releasing hormone) | Anterior pituitary | ↑ TSH release |
| GnRH (gonadotropin-releasing hormone) | Anterior pituitary | ↑ LH and FSH release (pulsatile) |
| GHRH (GH-releasing hormone) | Anterior pituitary | ↑ GH release |
| Somatostatin (SST/SRIF) | Anterior pituitary, pancreas | ↓ GH, TSH, insulin, glucagon |
| Dopamine (DA) | Anterior pituitary | ↓ Prolactin |
| ADH/Vasopressin (AVP) | Posterior pituitary (storage), kidney | ↑ Water reabsorption (V2R → AQP2) |
| Oxytocin | Posterior pituitary (storage), uterus, breast | Uterine contraction, milk letdown, bonding |

Parvocellular neuroendocrine neurons in the paraventricular nucleus (PVN) and arcuate nucleus project to the median eminence → release into the hypophyseal portal system → reach the anterior pituitary. Magnocellular neurons (PVN + supraoptic nucleus) project axons directly to the posterior pituitary neurohaemal region → store and release AVP and OXT.

#### Anterior Pituitary (Adenohypophysis)

Six main cell types and their hormones [^guyton-hall]:

| Cell type | Hormone | Primary targets and effects |
|:---|:---|:---|
| Somatotroph (50%) | GH (growth hormone) | Liver (IGF-1 production), bone (long bone growth), adipose (lipolysis), muscle (protein synthesis) |
| Corticotroph (20%) | ACTH (adrenocorticotropin) | Adrenal cortex → cortisol and DHEA |
| Thyrotroph (5%) | TSH (thyroid-stimulating hormone) | Thyroid → T3 and T4 synthesis and secretion |
| Gonadotroph (10%) | LH, FSH | Gonads → steroid and gamete production |
| Lactotroph (15%) | Prolactin | Breast → lactation; reproductive axis suppression |
| Melanotroph | MSH (α-MSH) | Melanocytes → pigmentation; MC4R in hypothalamus → satiety |

#### Posterior Pituitary (Neurohypophysis)

Not a true gland — a storage and release site for AVP and oxytocin synthesised in hypothalamic magnocellular neurons and transported down axons [^guyton-hall].

| Hormone | Stimuli | Effects |
|:---|:---|:---|
| ADH/AVP | ↑plasma osmolarity (>285 mOsm/kg), ↓blood volume, pain, nausea | V2R on collecting duct → cAMP → AQP2 insertion → water reabsorption; V1aR on VSM → vasoconstriction |
| Oxytocin | Cervical stretch (Ferguson reflex), suckling | Uterine contraction (positive feedback with PGE2); myoepithelial cell contraction → milk ejection; CNS: pair bonding, trust, social behaviour |

#### Thyroid Gland

Follicular cells synthesise T3 (3,5,3'-triiodothyronine — the active form) and T4 (thyroxine — prohormone, 99.97% protein-bound [TBG, albumin, transthyretin]); peripheral tissues convert T4 → T3 via iodothyronine deiodinases (D1/D2/D3) [^stryer-biochemistry].

Synthesis: dietary iodide → thyroid → NIS (Na+/I- symporter) uptake → oxidised by TPO → organification of thyroglobulin (iodination of Tyr residues → MIT, DIT → T3, T4) → colloid storage → TSH → pinocytosis → lysosomal proteolysis → T3/T4 secretion.

Parafollicular C-cells: calcitonin (↓serum Ca²⁺ by inhibiting osteoclasts; marker for medullary thyroid carcinoma).

Thyroid hormone actions (via nuclear receptor TR-α/β → gene transcription):
- ↑ BMR (↑Na⁺/K⁺-ATPase expression, ↑mitochondrial uncoupling, ↑β-oxidation)
- ↑ Cardiac output (↑heart rate, ↑contractility, ↑CO)
- ↑ GI motility; ↑bone turnover; ↑catecholamine sensitivity
- CNS maturation (critical in fetal/neonatal period — deficiency → cretinism)

#### Parathyroid Glands (×4)

Chief cells secrete PTH (parathyroid hormone) in response to ↓[Ca²⁺] sensed by calcium-sensing receptor (CaSR on parathyroid cell membrane) [^guyton-hall]:
- **Bone:** PTH → osteoblast RANKL → osteoclast activation → bone resorption → ↑Ca²⁺, ↑Pi (paradoxically — intermittent PTH is anabolic: teriparatide)
- **Kidney (DCT/collecting duct):** ↑Ca²⁺ reabsorption (TRPV5), ↑phosphate excretion (↓NaPi IIa/IIc), ↑1α-hydroxylase → ↑1,25-VitD synthesis
- **Gut (indirect):** via ↑1,25-VitD → ↑Ca²⁺ absorption (TRPV6 + calbindin)

#### Adrenal Glands

**Adrenal cortex** (three zones) [^stryer-biochemistry]:
- *Zona glomerulosa* (outermost): Aldosterone (mineralocorticoid) — regulated by angiotensin II and K⁺, NOT by ACTH. Actions: ↑Na⁺ reabsorption (ENaC), ↑K⁺ and H⁺ secretion in collecting duct (principal cells). Net: ↑blood volume, ↑blood pressure.
- *Zona fasciculata* (middle): Cortisol (glucocorticoid) — regulated by ACTH. Actions: ↑gluconeogenesis + ↑proteolysis + ↑lipolysis (peripheral) = ↑blood glucose; anti-inflammatory (↓NF-κB, ↓COX-2, ↓cytokines); permissive for catecholamine action; ↑PHMT (epinephrine synthesis in medulla). Negative feedback to hypothalamus (↓CRH) and pituitary (↓ACTH).
- *Zona reticularis* (inner): DHEA/DHEAS (weak androgens) → converted peripherally to testosterone and oestradiol; regulated by ACTH; important for adrenarche (pubic/axillary hair) and post-menopausal oestrogen.

**Adrenal medulla** (chromaffin cells — modified postganglionic sympathetic neurons): Epinephrine (Epi, ~80%) and norepinephrine (NE, ~20%) released en masse via preganglionic sympathetic ACh → nicotinic receptor → catecholamine secretion. Actions: ↑HR, ↑CO, ↑bronchodilation (β2), ↑glycogenolysis, ↑lipolysis, ↑sweating, ↑alertness [^guyton-hall].

#### Pancreatic Islets of Langerhans

~1 million islets (~2% of pancreatic mass) scattered within exocrine pancreas [^stryer-biochemistry]:

| Cell type | Hormone | Stimulus | Effect |
|:---|:---|:---|:---|
| β-cells (~70%) | Insulin | ↑glucose (GLUT2 → glucokinase → ATP/K+ channel closure → depolarisation → Ca²⁺ → exocytosis); amino acids; GLP-1, GIP (incretins) | ↓blood glucose (↑GLUT4 in muscle/fat, ↑glycogen synthesis, ↑glycolysis, ↑lipogenesis, ↓gluconeogenesis) |
| α-cells (~20%) | Glucagon | ↓glucose; amino acids; sympathetic NS | ↑blood glucose (↑hepatic glycogenolysis, ↑gluconeogenesis) |
| δ-cells (~5%) | Somatostatin | ↑glucose, ↑amino acids | Paracrine ↓insulin and glucagon secretion |
| γ-cells (<5%) | Pancreatic polypeptide (PP) | Meals, fasting | ↓pancreatic exocrine secretion, ↓appetite |
| ε-cells (<1%) | Ghrelin | Fasting | ↑appetite (hypothalamic NPY/AgRP) |

#### Gonads

**Testes:** Leydig cells → testosterone (LH-stimulated → CYP17A1/CYP11A1 pathway from cholesterol); Sertoli cells → inhibin B (suppresses FSH), AMH (Müllerian inhibiting substance), activin, oestradiol (from aromatase). Testosterone: male secondary sexual characteristics, spermatogenesis (high intratesticular concentration via Sertoli SHBG), anabolism, bone mineralisation, erythropoiesis (↑EPO), CNS (aggression, libido, spatial cognition).

**Ovaries:** Granulosa cells → oestradiol (FSH-stimulated, aromatase) → endometrial proliferation, vaginal epithelium, breast development, positive feedback on LH surge (mid-cycle). Luteal corpus luteum → progesterone (LH-stimulated) → endometrial secretory phase, decidualisation, thermogenesis. Granulosa/theca → inhibin A, activin, AMH (follicle reserve marker).

#### Other Endocrine Sources

| Gland/Tissue | Hormone | Function |
|:---|:---|:---|
| Pineal gland | Melatonin (from serotonin, light-suppressed) | Circadian entrainment; sleep onset signal |
| Thymus | Thymosin α1, thymulin | T-cell maturation; declines with age (thymic involution) |
| Adipose tissue | Leptin (adiponectin, resistin) | Leptin: hypothalamic satiety (JAK2/STAT3 → ↓NPY/AgRP, ↑POMC); adiponectin: ↑insulin sensitivity (AMPK) |
| Heart | ANP, BNP | ↓Na⁺ reabsorption (inhibit ENaC, RAAS), ↓preload, ↑GFR |
| Kidney | EPO (juxta-glomerular cells), 1,25-VitD, Renin | EPO: ↑RBC production; Renin: RAAS cascade → Ang II → aldosterone → ↑BP/volume |
| GI tract | GLP-1, GIP (incretins); Gastrin; CCK; Secretin; GIP; PYY; Ghrelin (stomach) | Incretin effect (↑insulin post-meal); digestion coordination; appetite regulation |
| Liver | IGF-1 (GH-stimulated), angiotensinogen, thrombopoietin, hepcidin, FGF21 | Growth mediation; RAAS precursor; platelet production; iron regulation |

### Hormone Chemistry and Receptor Mechanisms

**Peptide/protein hormones** (water-soluble; cannot cross cell membranes; membrane receptors): insulin, GH, PTH, LH, FSH, glucagon, prolactin, ACTH, ADH, oxytocin, GLP-1, leptin. Receptors: GPCRs (→ cAMP, IP3/Ca²⁺, DAG/PKC), RTKs (insulin → IR/IRS-1→PI3K→Akt; GH → JAK2→STAT5), cytokine receptors. Rapid onset (seconds to minutes) via second messenger cascades [^stryer-biochemistry].

**Steroid hormones** (lipophilic; derived from cholesterol; freely cross cell membranes; nuclear/cytoplasmic receptors): cortisol (GR), aldosterone (MR), testosterone (AR), oestradiol (ERα/ERβ), progesterone (PR), calcitriol/1,25-VitD (VDR), DHEA. Nuclear receptor superfamily: ligand-binding domain + zinc-finger DNA-binding domain + AF-2 transactivation domain → bind GREs (glucocorticoid response elements) or HREs → gene transcription (hours to days). Also rapid non-genomic signalling via membrane-associated steroid receptors [^stryer-biochemistry].

**Tyrosine-derived hormones:** Catecholamines (dopamine, NE, epinephrine — synthesised from Tyr → DOPA → dopamine → NE → Epi; water-soluble → membrane receptors [α/β-adrenergic GPCRs]). Thyroid hormones (T3/T4 — iodinated Tyr residues on thyroglobulin; lipophilic → nuclear receptors TRα/TRβ; major genomic effects) [^guyton-hall].

**Gaseous mediators:** NO (eNOS/nNOS/iNOS — from Arg; → sGC → cGMP → vasodilation), CO (HO-1/2 — from haem → cGMP), H₂S (CSE/CBS — paracrine mediators).

## Function

### Feedback Regulation

Most endocrine axes operate under **negative feedback** — the classical servo-control mechanism preventing hormone excess [^guyton-hall]:

- **HPA axis:** Stressor → hypothalamus CRH → anterior pituitary ACTH → adrenal cortex cortisol → cortisol feeds back to hypothalamus (↓CRH) and pituitary (↓ACTH). Long-loop negative feedback; short-loop feedback (ACTH → hypothalamus); ultra-short-loop (CRH → CRH neurons).
- **HPT axis:** TRH → TSH → T3/T4 → T3 (more potent) feeds back to pituitary (↓TSH) and hypothalamus (↓TRH).
- **RAAS:** ↓BP/↓Na⁺/↑renal sympathetics → renin (JGA) → Ang I → ACE (lung) → Ang II → aldosterone → ↑Na⁺ reabsorption → ↑blood volume → ↑BP → ↓renin.
- **Calcium homeostasis:** ↓Ca²⁺ → CaSR on parathyroid → ↑PTH → ↑Ca²⁺ (bone, kidney, gut) → ↑Ca²⁺ → CaSR → ↓PTH.

**Positive feedback** (uncommon; amplifies a deviation rather than correcting it): Mid-cycle LH surge — rising oestradiol (day 12) → switches pituitary gonadotrophs from negative to positive feedback → massive LH surge → ovulation. Oxytocin + cervical distension (Ferguson reflex) → more oxytocin → more contractions → more distension (until delivery breaks the loop).

**Circadian and ultradian rhythms:** Cortisol peaks at 06:00–08:00 (driven by CRH/ACTH pulse amplitude), nadir ~00:00; GH secreted in pulses (especially first hour of slow-wave sleep); LH/FSH pulsatile (GnRH pulse frequency: every 60–90 min follicular phase; every 3–4 h luteal phase); melatonin rises at dusk (~21:00) under dim light conditions, peaks 02:00–03:00, suppressed by light [^guyton-hall].

**Permissive effects:** Cortisol is permissive for catecholamine responsiveness (upregulates β-adrenergic receptor expression and sensitises vascular smooth muscle) — explains why Addisonian patients are poorly responsive to pressor agents. T3 is permissive for GH secretion and normal growth.

### Metabolic Coordination

The endocrine system coordinates fuel metabolism across multiple organs in response to feeding and fasting [^stryer-biochemistry]:

**Fed state (post-prandial):** ↑blood glucose → ↑insulin secretion (β-cells) + GLP-1 (incretin, L-cells in ileum) → insulin: ↑GLUT4 in muscle and adipose (→ glucose uptake), ↑glycogen synthesis (muscle + liver), ↓hepatic gluconeogenesis, ↑lipogenesis (adipose), ↓lipolysis, ↑protein synthesis.

**Fasted state:** ↓blood glucose → ↓insulin, ↑glucagon (α-cells) → glucagon: ↑hepatic glycogenolysis (PKA → phosphorylase kinase → glycogen phosphorylase), ↑gluconeogenesis (↑PEPCK, ↑FBPase), ↑lipolysis in adipose (PKA → HSL) → ↑FFA → hepatic β-oxidation → ketogenesis. After 12–16 h: GH + cortisol amplify lipolysis and gluconeogenesis.

**Stress response:** CRH → ACTH → cortisol + sympathetic → epinephrine → combined: ↑blood glucose, ↑cardiac output, ↑bronchodilation, ↑alertness, ↑pain threshold — the "fight-or-flight" + HPA arm of stress physiology.

## Connections

- `contains` → **[Pancreas](../../06-organ/pancreas/README.md)** — Islets of Langerhans (insulin [β-cells], glucagon [α-cells], somatostatin [δ-cells]) are central glucose regulators; T1DM = autoimmune β-cell destruction; T2DM = insulin resistance + progressive β-cell failure.
- `modulates` → **[Nervous System](../nervous-system/README.md)** — Hypothalamus integrates nervous and endocrine systems; CRH, TRH, GnRH, GHRH control anterior pituitary; glucocorticoids, thyroid hormones, and sex steroids feed back to regulate CNS and behaviour.
- `modulates` → **[Immune System](../immune-system/README.md)** — Cortisol, oestrogens, and androgens regulate immune cell trafficking, cytokine production, and lymphocyte apoptosis; HPA-axis cortisol → immunosuppression; thymic involution driven by sex steroids reduces T-cell output with age.
- `modulates` → **[Cardiovascular System](../cardiovascular-system/README.md)** — ANP/BNP (heart), aldosterone (adrenal), ADH (posterior pituitary), EPO (kidney), and catecholamines (adrenal medulla) regulate blood pressure, volume, and cardiac output; hyperthyroidism, Cushing's, and phaeochromocytoma cause CVD.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin (β-cell peptide) coordinates fed-state metabolism: ↑GLUT4 in muscle/adipose, ↑glycogen synthesis, ↓hepatic gluconeogenesis, ↑lipogenesis; GLP-1 agonists (semaglutide, tirzepatide) amplify insulin secretion; insulin resistance drives T2DM, metabolic syndrome, and NAFLD.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol (adrenal glucocorticoid, HPA axis: CRH→ACTH→cortisol) is the key stress hormone: ↑gluconeogenesis, ↑lipolysis, anti-inflammatory (↓NF-κB, ↓COX-2), permissive for catecholamine action; Cushing's syndrome = chronic cortisol excess; Addison's disease = cortisol deficiency.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Glucagon (α-cell peptide) opposes insulin in fasting: ↑hepatic glycogenolysis and gluconeogenesis via PKA/CREB; hypersecretion amplifies hyperglycemia in T2DM; GLP-1 agonists (semaglutide) suppress glucagon release; glucagon receptor antagonists in clinical trials for T2DM.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — Carney complex shows how one signaling defect can derange the endocrine system: germline PRKAR1A loss leaves protein kinase A constitutively active, spawning tumors across adrenal, pituitary, thyroid, and gonad — a model of the cAMP-PKA cascade driving multi-gland neoplasia.
- `contains` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal gland is a dual endocrine organ: its cortex makes steroid hormones (cortisol, aldosterone, androgens) under HPA and RAAS control, while its medulla — modified sympathetic tissue — secretes catecholamines; disorders span Cushing's, Addison's, Conn's, and pheo.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes is the most common endocrine disease: insulin resistance plus progressive β-cell failure dysregulate the body's central metabolic hormone, and its complications (retinopathy, nephropathy, neuropathy) make it a leading cause of blindness, kidney failure, and CVD.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — MEN1 shows how the endocrine system fails as a network: a single germline MEN1 mutation predisposes to synchronous tumors of the parathyroids, pancreatic islets and pituitary, illustrating that endocrine glands share pathways whose disruption causes multi-gland hyperfunction.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Growth hormone exemplifies the endocrine system's hierarchical axes: the hypothalamus and pituitary release GH, which acts via hepatic IGF-1 on growth and metabolism under feedback control; its excess (acromegaly) or deficiency shows how one hormone integrates the network.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The reproductive system is a major endocrine organ: the hypothalamic-pituitary-gonadal axis secretes sex steroids (estrogen, testosterone) that drive puberty, fertility and secondary sexual characteristics and feed back on the brain, weaving reproduction into hormonal control.
- `contains` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid is the body's metabolic thermostat: hypothalamic TRH and pituitary TSH drive it to release T3/T4 that set metabolic rate, heart rate and thermogenesis, feedback closing the HPT axis—hyper- and hypothyroidism are among the commonest endocrine disorders.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Thyroid cancer is the most common endocrine malignancy: most are papillary tumors that retain TSH responsiveness and iodine uptake, allowing radioactive-iodine therapy and thyroglobulin monitoring—a rare cancer treated through its own hormonal physiology.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium homeostasis is a core endocrine task: parathyroid hormone, calcitonin and calcitriol tune blood calcium via bone, gut and kidney—disorders like hyperparathyroidism or vitamin-D deficiency show the endocrine system guarding one ion's narrow range.
- `connects-to` → **[Thyroid Hormones (T3/T4)](../../03-molecular/thyroid-hormones/README.md)** — Thyroid hormones show how the endocrine system runs on feedback loops: the hypothalamic-pituitary-thyroid axis tunes T3/T4 to set metabolic rate, and disrupting any level causes hypo- or hyperthyroidism—a model for the feedback that governs all endocrine glands.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Type 1 diabetes is autoimmune destruction within the endocrine system: T cells kill pancreatic beta cells, eliminating insulin and proving how loss of a single endocrine cell type disrupts whole-body fuel metabolism—an organ-specific failure of the endocrine network.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen shows the endocrine system's reach beyond metabolism: this gonadal steroid, set by the hypothalamic-pituitary-gonadal axis, controls reproduction but also bone, cardiovascular and brain function—so endocrine signaling integrates far-flung organ systems.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Testosterone is a central output of the endocrine system: the testes make it under pituitary LH control, and it drives male sexual development, muscle and bone—so it exemplifies the hypothalamic-pituitary-gonadal axis that the endocrine system coordinates.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Aldosterone shows the endocrine system regulating salt and blood pressure: the adrenal cortex secretes it under the renin-angiotensin system to retain sodium, so its excess (Conn syndrome) or deficiency (Addison's) are classic endocrine electrolyte and pressure disorders.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Osteoporosis is largely an endocrine disease of bone: estrogen, testosterone, thyroid, parathyroid and cortisol all govern bone turnover, so hormonal shifts—menopause, hyperthyroidism, steroid excess—are leading causes, tying the skeleton to the endocrine system.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — The pineal gland completes the endocrine system with melatonin: this hormone translates darkness into a sleep-timing signal, so the endocrine system governs not just metabolism and growth but the body's daily clock.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is a hidden endocrine organ: it secretes erythropoietin to drive red-cell production, renin to control blood pressure, and activates vitamin D, so kidney failure causes anemia, hypertension, and bone disease through lost hormones.
- `connects-to` → **[Obesity](../obesity/README.md)** — Fat is an endocrine organ, and obesity disrupts it: adipose tissue secretes leptin, adiponectin, and estrogen, so excess fat rewires hormonal signaling—driving insulin resistance, reproductive disturbance, and hormone-sensitive cancers.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — The endocrine system depends on dietary iodine: the thyroid traps iodine to build thyroid hormones that set the body's metabolic rate, so iodine deficiency produces goiter and hypothyroidism—a mineral shortage with system-wide hormonal consequences.
- `connects-to` → **[ACTH](../../03-molecular/acth/README.md)** — The endocrine system runs on feedback loops like ACTH's: the pituitary releases ACTH to drive adrenal cortisol, which loops back to shut off ACTH—the kind of hormonal thermostat that keeps every endocrine axis in balance.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — The gut is an endocrine organ too, via ghrelin: the stomach releases ghrelin before meals to signal hunger to the brain, showing the endocrine system reaches into the digestive tract—not just the classic hormone glands.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Fat is an endocrine organ in its own right: adipocytes secrete leptin, adiponectin and other hormones that report energy stores and tune metabolism, so the endocrine system extends well beyond the classic glands into body fat.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain is the endocrine system's command center: the hypothalamus and pituitary it houses release the master hormones that drive the thyroid, adrenal and gonadal axes, so neural signals set the rhythm of the whole hormonal orchestra.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Parathyroid hormone runs the body's calcium thermostat: when blood calcium dips, the parathyroid glands release PTH to pull calcium from bone and kidney, a tightly regulated endocrine loop essential to nerves, muscle and bone.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — The endocrine system runs partly on zinc: pancreatic beta cells store insulin in zinc-containing crystals, and the metal is needed to make and stabilize the hormone, tying a trace element to blood-sugar control.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Light tunes the endocrine clock through photons: light striking the eye signals the pineal gland to halt melatonin by day and release it by night, so the sun sets the hormonal rhythm of the whole body.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The stomach is a hormone gland too: it secretes ghrelin, the hunger hormone that signals the brain to eat, making the gut a full member of the endocrine system beyond the classic glands.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus reins in the hormonal stress axis: dense in cortisol receptors, it provides the negative feedback that switches off the HPA axis, so chronic stress that damages it lets cortisol run high.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The endocrine system begins in neurons: hypothalamic neurosecretory cells release hormones that command the pituitary, and the adrenal medulla is itself made of modified neurons, blurring nerve and gland.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — The endocrine system guards sodium: aldosterone from the adrenal cortex tells the kidney to retain salt and water, the hormonal control of blood volume and pressure.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals what makes a cell endocrine: its cytoplasm is packed with dense-core secretory granules, membrane-bound stores of hormone poised for release — the universal signature of the glands that signal through the blood.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart is a gland in its own right: stretched by a full circulation, it secretes natriuretic peptides that order the kidney to dump salt and water, making the heart an endocrine organ that regulates blood volume.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Hormones tune phosphate as well as calcium: parathyroid hormone, vitamin D, and bone-derived FGF23 form a feedback loop that balances phosphorus, the endocrine control of the mineral that builds bone and powers ATP.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Fat itself is an endocrine organ: adipocytes secrete leptin in proportion to fat stores, and the hormone signals the hypothalamus to curb appetite — the discovery that recast adipose tissue as part of the endocrine system rather than inert storage.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D is really a hormone: the skin and kidney convert it to calcitriol, a steroid hormone that acts through nuclear receptors to raise calcium absorption, placing this 'vitamin' squarely within the endocrine system's calcium control.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — A tumor can hijack the stress hormones: pheochromocytoma of the adrenal medulla floods the body with catecholamines, causing pounding spells of hypertension, palpitations and sweating — endocrine signaling turned into a dangerous excess.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Prolactin shows the pituitary's reach: this anterior-pituitary hormone drives lactation under hypothalamic dopamine control, and its overproduction — the commonest pituitary tumor — causes infertility and milk discharge.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The gut is the body's largest endocrine organ: scattered enteroendocrine cells of the small intestine secrete incretins, ghrelin, secretin, and cholecystokinin that tune digestion, appetite, and insulin release.
- `connects-to` → **[MEN4 Syndrome](../men4-syndrome/README.md)** — One gene can derail many glands: MEN4, like MEN1, is a hereditary syndrome that spawns synchronous tumors across the parathyroid, pituitary, and pancreas, the endocrine system failing along an inherited fault line.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Oxytocin is a posterior-pituitary output of the system: synthesized in the hypothalamus and released from the neurohypophysis, it drives labor contractions and milk ejection, a neuroendocrine hormone bridging brain and body.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Vasopressin completes the posterior-pituitary pair: this hypothalamic hormone conserves water at the kidney and raises blood pressure, and its deficiency or resistance causes diabetes insipidus — an endocrine axis distinct from the anterior pituitary's.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Calcitonin rounds out calcium control: secreted by thyroid C-cells it lowers blood calcium opposite parathyroid hormone, and as a tumor marker it flags medullary thyroid carcinoma within the endocrine system.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Its hormone-making cells can turn into tumors: neuroendocrine tumors arise from the dispersed endocrine cells of the gut, pancreas and lungs, sometimes secreting hormones that cause florid syndromes — the malignant face of the endocrine system.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — The gut is the body's largest endocrine organ: L-cells release the incretin GLP-1 after meals to spur insulin and curb appetite, the gut-hormone axis now harnessed by blockbuster diabetes and weight drugs.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — Bone is an endocrine organ too: osteocytes secrete FGF23 to tell the kidney to excrete phosphate and curb active vitamin D, a bone-kidney hormonal axis that fails early in chronic kidney disease.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — An old infection can shut down the adrenals: tuberculosis is a classic cause of primary adrenal insufficiency (Addison's), destroying the adrenal cortex and crippling the body's cortisol and aldosterone output.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — It seeds tumors across endocrine glands: VHL disease causes pheochromocytomas of the adrenal medulla and pancreatic neuroendocrine tumors, a hereditary disorder striking multiple endocrine organs at once.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — It targets the thyroid above all: Cowden syndrome causes goiter, benign thyroid nodules and a high risk of thyroid cancer, one of its defining endocrine manifestations alongside breast and uterine tumors.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Hormone excess drives secondary hypertension: Cushing's, primary aldosteronism, pheochromocytoma and thyroid disorders raise blood pressure, making the endocrine system a key source of treatable secondary hypertension.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its hormones shape the heart: thyroid excess or deficiency, acromegaly and catecholamine-secreting tumors all remodel the myocardium, so endocrine disease is an important reversible cause of heart failure.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Hormones set the tenor of mood: thyroid dysfunction, cortisol excess or deficiency and sex-hormone shifts profoundly affect mood, so endocrine disorders frequently present with depression.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The gut is a vast endocrine organ: incretins, gastrin, ghrelin and other gut hormones regulate digestion and metabolism, and the pancreas is both an endocrine and a digestive gland.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The kidney is itself an endocrine gland: it secretes erythropoietin and renin and activates vitamin D, while it is also the target of aldosterone, ADH and parathyroid hormone.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Hormones are written on the skin: endocrine disease shows as acanthosis nigricans of insulin resistance, the hyperpigmentation of Addison's, myxoedema of thyroid disease and vitiligo of autoimmunity.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Hormones build and maintain the frame: parathyroid hormone, vitamin D, sex steroids, growth hormone and cortisol govern bone and muscle, so endocrine disease causes osteoporosis, acromegalic arthropathy and steroid myopathy.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It reaches into the lungs: the pulmonary endothelium activates angiotensin via ACE, and endocrine disorders affect breathing — acromegaly causes sleep apnoea and hypothyroidism causes hypoventilation.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The thymus is an endocrine-immune organ: it secretes thymic hormones that direct T-cell maturation, and thyroid autoimmunity such as Graves' disease drives thymic hyperplasia.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — The commonest Cushing's is iatrogenic: exogenous glucocorticoids like prednisolone and dexamethasone suppress the hypothalamic-pituitary-adrenal axis and cause Cushing syndrome, the archetype of drug-induced endocrine disease.
- `connects-to` → **[Dietary Magnesium](../../../03-medicine/03-food/magnesium-dietary/README.md)** — A mineral the hormones need: magnesium is required for insulin sensitivity and parathyroid-hormone secretion, so deficiency disturbs glucose and calcium regulation.
- `connects-to` → **[Dietary Zinc](../../../03-medicine/03-food/zinc-dietary/README.md)** — Zinc underpins hormone signalling: it is essential for insulin storage in the pancreas and for testosterone and thyroid-hormone production, so deficiency impairs growth and reproduction.
- `connects-to` → **[Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — The most-prescribed endocrine drug: metformin lowers hepatic glucose output as first-line therapy for type 2 diabetes and is also used in polycystic ovary syndrome, an everyday tool of endocrinology.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — It can destroy the glands: tuberculosis is a classic cause of primary adrenal insufficiency (Addison's disease) through bilateral adrenal destruction, and can also trigger SIADH.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy unleashes endocrinopathy: PD-1 and CTLA-4 inhibitors commonly cause immune-related thyroiditis, hypophysitis, adrenalitis and autoimmune diabetes, among the most frequent toxicities of cancer immunotherapy.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — The pancreas is an endocrine organ too: the islets of Langerhans secrete insulin, glucagon and somatostatin to govern blood glucose, making the endocrine pancreas central to the system and the seat of diabetes.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Bone is both target and gland: PTH, calcitonin, vitamin D, oestrogen and thyroid hormone remodel cortical bone, while bone itself secretes FGF23 and osteocalcin — a two-way endocrine relationship governing calcium and phosphate.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Hormone pathways are drug targets: somatostatin analogues and peptide-receptor radionuclide therapy treat neuroendocrine tumours, while mTOR inhibitors and hormone-receptor-directed agents act on endocrine tumours and their hormone axes.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — The growth-hormone effector: most of growth hormone's actions work through liver-made IGF-1, the axis disrupted in acromegaly and gigantism—a core endocrine feedback loop measured to diagnose GH excess.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — A temporary endocrine organ: in pregnancy the placenta becomes a massive hormone factory, secreting hCG, progesterone, oestrogen and placental lactogen that reshape maternal metabolism.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Inherited endocrine tumours: DICER1 predisposes to thyroid cancer, pituitary blastoma and ovarian sex-cord tumours, one of the germline syndromes that strike multiple endocrine glands.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Endocrine tumours in a neurocutaneous syndrome: neurofibromatosis type 1 predisposes to phaeochromocytoma and other endocrine tumours, linking a nerve-sheath disorder to the endocrine system.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — Starvation reshapes hormones: anorexia nervosa suppresses the hypothalamic-pituitary axes—amenorrhoea, low thyroid and sex hormones, high cortisol—a functional endocrine disorder driven by energy deficit.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Infection hits the glands: COVID-19 can trigger subacute thyroiditis, new-onset diabetes and adrenal dysfunction, the virus reaching multiple endocrine organs that express ACE2.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Top of the stress axis: corticotropin-releasing hormone from the hypothalamus drives ACTH and cortisol release, the apex of the hypothalamic-pituitary-adrenal endocrine cascade.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — Blood-pressure hormone cascade: renin initiates the renin-angiotensin-aldosterone system, the endocrine loop controlling blood pressure, sodium and potassium balance.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Reproductive steroid axis: progesterone, with estrogen and testosterone, is a core gonadal steroid hormone of the endocrine system governing the menstrual cycle and pregnancy.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Adrenal medulla hormone: epinephrine is the endocrine system's fast-response hormone, released from the adrenal medulla to drive the fight-or-flight metabolic and cardiovascular surge.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Prolactin brake: hypothalamic dopamine tonically inhibits pituitary prolactin release, an endocrine control point whose loss—or dopamine-blocking drugs—causes hyperprolactinaemia.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Renal endocrine hormone: erythropoietin from the kidney shows the endocrine system extends beyond classic glands, the hormone tying oxygen sensing to red-cell production.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — RAAS effector hormone: angiotensin II is the active hormone of the renin-angiotensin-aldosterone system, raising blood pressure and driving aldosterone release in the endocrine control of fluid and salt.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipose endocrine organ: adiponectin from fat exemplifies adipose tissue as an endocrine organ, its hormones signalling insulin sensitivity and energy balance to the rest of the body.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — Cardiac endocrine hormone: BNP secreted by the stretched heart shows even the cardiovascular system is endocrine, the natriuretic hormone that signals volume status to the kidney.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — The glucocorticoid receptor is the intracellular receptor through which cortisol exerts its wide-ranging metabolic, immune, and stress effects—the effector arm of the HPA endocrine axis and the target of all glucocorticoid drugs.
- `connects-to` → **[Androgen receptor](../../03-molecular/androgen-receptor/README.md)** — The androgen receptor mediates the actions of testosterone and DHT across reproductive and somatic tissues, the nuclear-receptor endpoint of the male endocrine axis and the target of anti-androgen therapy.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — Somatostatin acting on SSTR2 broadly suppresses the secretion of growth hormone, insulin, glucagon, and gut hormones—the inhibitory regulator of the endocrine system and the basis for octreotide in acromegaly and neuroendocrine tumors.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Serum calcium is the regulated variable of a dedicated endocrine axis—parathyroid hormone and vitamin D raise it, calcitonin lowers it—the tightly controlled ion essential for nerve, muscle and bone whose dysregulation causes endocrine disease.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Growth hormone, prolactin and leptin signal through JAK-STAT (their receptors are cytokine-receptor-family members), a core transduction mechanism of the endocrine system.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK transduces the receptor-tyrosine-kinase and GPCR signals of many hormones into the proliferative and trophic responses of endocrine target tissues.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β, inhibited by insulin-AKT signaling (insulin, insulin-receptor and AKT mapped), couples endocrine signaling to glycogen and metabolic control.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — The activin-inhibin system provides a peptide feedback loop, distinct from the steroid hormones, that tunes pituitary FSH secretion and gonadal function, layered onto the classic steroid-hormone axes of the endocrine system.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Adrenomedullin, secreted widely including by the adrenal medulla and endothelium, is a potent vasodilator and part of the endocrine control of vascular tone and fluid balance, integrating the hormonal and cardiovascular systems.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — The insulin receptor transduces the signal of insulin (already mapped) into target cells, the prototypical endocrine receptor linking a circulating hormone to cellular metabolism.
- `connects-to` → **[Neuropeptide Y](../../03-molecular/npy/README.md)** — Neuropeptide Y is a hypothalamic orexigenic signal that integrates the endocrine control of appetite and energy balance alongside the adipokine and gut hormones leptin and ghrelin (both mapped).
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelin-1 is a potent paracrine and endocrine vasoconstrictor that, with the renin-angiotensin and adrenomedullin systems already mapped, helps set the hormonal control of vascular tone and fluid balance.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — AKT is the central kinase transducing insulin and IGF-1 receptor signaling (both already mapped) into the metabolic and growth actions of these hormones throughout the endocrine system.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR integrates hormonal (insulin, IGF-1) and nutrient signals to govern the anabolic growth responses coordinated by the endocrine system.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK is the cellular energy sensor that counterbalances the insulin/mTOR anabolic axis (both already mapped), integrating the metabolic hormones with cellular energy status.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 transduces the growth-hormone, leptin and cytokine signals of the endocrine system and drives proliferation in many endocrine tumors.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β/activin-SMAD signaling (activin-A already mapped) provides feedback control of pituitary and gonadal hormone axes across the endocrine system.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is a marker of malignancy in thyroid and other endocrine tumors and modulates their inflammatory microenvironment.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate insulin/IGF and stress signaling across endocrine tissues, governing metabolism and hormone-secreting-cell homeostasis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the autoimmune and inflammatory processes that target endocrine glands across the endocrine system.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α couples the oxygen and metabolic status of endocrine glands to their hormone-secretory and proliferative responses.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) transduces the growth-factor and insulin signals that govern endocrine-cell proliferation and hormone secretion across the endocrine system.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING links cellular stress to the autoimmune and inflammatory endocrinopathies of the endocrine system.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB inflammatory signaling participates in the autoimmune and stress-related dysregulation of the endocrine glands.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy maintains the endocrine-cell homeostasis and hormone-secretory-granule turnover of the endocrine system.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the growth-factor and hormone-receptor signal transduction of the endocrine system.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of hormone-gene expression and endocrine-cell identity of the endocrine system.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment participates in the immune surveillance and endocrine-autoimmune responses of the endocrine system.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the endocrine-gland vascularization and cell homeostasis of the endocrine system.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the neuroendocrine-immune interactions of the endocrine system.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β signaling participates in the neuroendocrine-immune regulation of the hypothalamic-pituitary-adrenal axis of the endocrine system.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroendocrine-immune interactions of the endocrine system.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the immune-endocrine interactions of the endocrine system.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Neuroendocrine signalling: serotonin is a neuroendocrine hormone made by gut enterochromaffin cells and the pineal gland, and its overproduction by neuroendocrine (carcinoid) tumours illustrates the diffuse endocrine tissue beyond the classic glands.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Paracrine hormones: prostaglandins are locally acting lipid mediators that, alongside the circulating hormones, exemplify the paracrine and autocrine signalling that broadens the endocrine system beyond gland-to-bloodstream secretion.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Gasotransmitter signalling: nitric oxide is a diffusible gaseous messenger released by endothelium and neurons, a non-classical endocrine/paracrine signal that regulates vascular tone and complements peptide and steroid hormone systems.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Steroid precursor: cholesterol is the common precursor of every steroid hormone, converted in the adrenal cortex and gonads to cortisol, aldosterone and the sex steroids (all already mapped), the biochemical root of the steroid endocrine axes.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Thyroid activation: selenium-dependent deiodinase enzymes convert thyroxine to the active triiodothyronine (thyroid hormones already mapped), making this trace element essential to the peripheral regulation of thyroid hormone action.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Cutaneous endocrine function: the skin synthesises vitamin D from cholesterol under ultraviolet light, an endocrine role that feeds the calcium-regulating axis (PTH and FGF23 already mapped) and illustrates hormone production beyond the classical glands.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron as a hormonal axis: iron homeostasis is itself an endocrine system, governed by the liver hormone hepcidin and by erythropoietin (already mapped), illustrating hormonal control extending to a trace-metal balance.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Hormone secretion cofactor: magnesium is a cofactor for the secretion and action of many hormones, including parathyroid hormone (already mapped) and insulin (already mapped), so its deficiency disturbs the endocrine calcium and glucose axes.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Thymic endocrine role: the thymus secretes thymic hormones such as thymosin and thymulin that regulate T-cell maturation, an endocrine function of a lymphoid organ that links the endocrine and immune systems.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hepatic endocrine hub: the liver produces IGF-1 (already mapped) under growth hormone (already mapped), metabolises and clears hormones, and secretes hepatokines, an endocrine hub of the body's hormonal and metabolic network.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Osmoregulatory axis: the endocrine control of sodium and water balance runs through aldosterone and vasopressin (already mapped), the renin-angiotensin (already mapped) and osmoreceptor axes governing the body's sodium homeostasis.
- `connects-to` → **[Type 2 diabetes](../type-2-diabetes/README.md)** — The commonest endocrine disease: type 2 diabetes is the insulin (already mapped) resistance disorder of the endocrine pancreas, the most prevalent disease of the endocrine system.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Potassium homeostasis: the endocrine control of the potassium balance runs through aldosterone (already mapped) and the insulin (already mapped) shift, core electrolyte functions of the endocrine system.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose as endocrine organ: resistin, with leptin and adiponectin (already mapped), is an adipokine of the adipose tissue acting as an endocrine organ that regulates the systemic metabolism.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Enteroendocrine amine: histamine from the enterochromaffin-like cells of the gastric mucosa drives the acid-secretion axis, one of the paracrine/endocrine amine signals of the endocrine system.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Hepatic hormone hub: the hepatocytes produce the IGF-1 under GH (already mapped) control and the angiotensinogen (renin and angiotensin already mapped), and metabolise the steroid and thyroid hormones of the endocrine system.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Bone as endocrine organ: the osteoblasts secrete the osteocalcin (a hormone modulating the insulin — already mapped — sensitivity and energy metabolism) and the FGF23 (already mapped), responding to the PTH (already mapped).
- `connects-to` → **[NASH](../nash/README.md)** — Metabolic-syndrome disease: NASH is the hepatic manifestation of the metabolic syndrome (the insulin — already mapped — resistance and the adipokines already mapped), an endocrine/metabolic disease.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Autoimmune endocrinopathy: the IFN-γ of the T cells is the type-II interferon arm of the autoimmune destruction underlying the autoimmune endocrine diseases (type-1 diabetes, Hashimoto, Graves, Addison) of the endocrine system.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm that drives the autoimmune endocrinopathies of the endocrine system.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate autoimmune interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is implicated in the autoimmune endocrine diseases (e.g. type-1 diabetes) of the endocrine system.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 endocrinopathy: IL-17A drives the Th17 arm of the autoimmune endocrinopathies (autoimmune thyroiditis, type-1 diabetes) of the endocrine system.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 endocrine autoimmunity: IL-4 is the prototypical type-2 cytokine of the humoral autoimmunity (e.g. the Graves TSH-receptor antibodies) of the endocrine system.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Endocrine tolerance: IL-10 is the regulatory cytokine that maintains the immune tolerance and restrains the autoimmune endocrinopathies of the endocrine system.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Autoreactive CD4: the CD4 T-helper cells drive the autoreactive response (Th1/Th17, IFN-γ and IL-17 already mapped) of the autoimmune endocrinopathies (Hashimoto, Graves, type-1 diabetes) of the endocrine system.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Endocrine autoantibodies: the plasma cells secrete the autoantibodies (anti-TPO, TSH-receptor, anti-GAD) of the autoimmune endocrinopathies of the endocrine system.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the autoimmune endocrinopathies of the endocrine system.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the complement-mediated glandular injury of the autoimmune endocrinopathies of the endocrine system.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid recruitment into the inflamed endocrine glands of the autoimmune endocrinopathies.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Glandular macrophages: the macrophages infiltrate the endocrine glands and, in the autoimmune endocrinopathies, contribute to the destruction of the hormone-producing cells of the endocrine system.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-endocrine axis: TSLP, from the thymic (already mapped) and thyroid (already mapped) epithelium, primes dendritic-cell Th2 polarisation and amplifies the autoimmune attack on the hormone-producing cells of the endocrine system.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-endocrine axis: bradykinin, via B1/B2 receptors on the vasculature of the adrenal gland (already mapped), thyroid (already mapped) and pancreas (already mapped), modulates glandular blood flow and the inflammatory response in the autoimmune endocrinopathies.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement (C3 already mapped) and the contact-kinin system (bradykinin above) at the glandular vasculature of the endocrine organs, tempering autoimmune endocrine injury.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation-endocrine axis: factor H, produced by the liver and adrenal gland, limits alternative-pathway complement amplification at endocrine glandular surfaces, protecting the thyroid, pancreas, and adrenal cortex from complement-mediated autoimmune injury.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Periostin-endocrine axis: periostin, expressed in the stromal matrix of the thyroid, adrenal gland, and pancreatic islets, promotes epithelial-mesenchymal crosstalk and glandular fibrosis in autoimmune and neoplastic endocrine disease.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron-endocrine axis: transferrin shuttles iron to the thyroid for thyroid-peroxidase-catalysed thyroid-hormone synthesis and to the adrenal gland for steroidogenesis, linking systemic iron metabolism to endocrine hormone output.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Endocrine prolactin: prolactin, via PRLR on macrophages (already mapped) and osteoblasts (already mapped), modulates the adrenal-gonadal axis; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) autoimmune cascade of endocrine disease.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Endocrine oxytocin: oxytocin, via OXTR on macrophages (already mapped) and hepatocytes (already mapped), attenuates adrenal and thyroid autoimmune inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) endocrine cascade.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Endocrine vasopressin: vasopressin, via V2R on macrophages (already mapped) and hepatocytes (already mapped), modulates fluid-hormone homeostasis; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) endocrine inflammatory cascade.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Endocrine copper: copper, as cofactor of cuproenzymes in hepatocytes (already mapped) and thyroid follicular cells, supports thyroid hormone synthesis; copper deficiency impairs the NF-κB (already mapped) and IL-6 (already mapped) endocrine immune-regulation cascade.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Endocrine sulfur: sulfur, as component of glutathione in hepatocytes (already mapped) and macrophages (already mapped), scavenges ROS; sulfur deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative endocrine inflammatory cascade.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Endocrine chloride: chloride, via chloride channels in thyroid follicular cells and macrophages (already mapped), regulates thyroid hormone secretion and immune activation; chloride dysregulation amplifies the NF-κB (already mapped) endocrine cascade.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Endocrine nitrogen: nitric oxide (NO, nitrogen-derived) in endothelial cells and macrophages (already mapped) regulates hormone secretion; NO dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and adrenal-gland (already mapped) endocrine cascade.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Endocrine oxygen: mitochondrial ROS in hepatocytes (already mapped) and macrophages (already mapped) amplifies oxidative stress; ROS excess worsens NF-κB (already mapped) and IL-6 (already mapped) and thyroid (already mapped) endocrine inflammatory cascade.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Endocrine carbon: carbon-backbone metabolites in hepatocytes (already mapped) fuel acetyl-CoA and steroid hormone biosynthesis; carbon metabolic imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and adrenal-gland (already mapped) endocrine cascade.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Endocrine hydrogen: hydrogen ions regulate intracellular pH in hepatocytes (already mapped) and macrophages (already mapped); acid-base imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in endocrine gland tissue.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Endocrine TNF-α: TNF-α from macrophages (already mapped) amplifies the NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade, driving autoimmune attack on thyroid, pancreatic islet, and adrenal endocrine glands; TNF-α excess exacerbates endocrine destruction.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Endocrine TGF-β: TGF-β from macrophages (already mapped) and hepatocytes (already mapped) promotes endocrine gland fibrosis; TGF-β excess amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade in autoimmune endocrinopathies.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Endocrine pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses autoimmune endocrine surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and adrenal-gland (already mapped) cascade.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Endocrine vegf: VEGF from macrophages (already mapped) and hepatocytes (already mapped) drives endocrine gland angiogenesis; VEGF excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and adrenal-gland (already mapped) endocrine cascade.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Endocrine wnt-beta-catenin: Wnt/β-catenin in macrophages (already mapped) and hepatocytes (already mapped) regulates endocrine gland development; wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and adrenal-gland (already mapped) cascade.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — endocrine-system rankl: RANKL from osteoblasts (already mapped) and macrophages (already mapped) modulates bone-hormone crosstalk; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and IGF-1 (already mapped) endocrine cascade of the endocrine system.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — endocrine-system il-2: IL-2 on T-cells (already mapped) and macrophages (already mapped) amplifies endocrine immune regulation; il-2 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and GLP-1 (already mapped) cascade of the endocrine system.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — endocrine-system fibronectin: fibronectin in endocrine cells (already mapped) and macrophages (already mapped) maintains gland ECM; fibronectin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of the endocrine system.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — endocrine-system notch: Notch signalling on endocrine cells (already mapped) and macrophages (already mapped) regulates gland development; notch excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of the endocrine system.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — endocrine-system cgrp: CGRP from endocrine cells (already mapped) and macrophages (already mapped) modulates neuroendocrine communication; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of the endocrine system.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — endocrine-system substance-p: substance-P from endocrine cells (already mapped) and macrophages (already mapped) modulates nociception; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade of the endocrine system.

## Pathology

### Diabetes Mellitus

The most prevalent endocrine disorder globally [^guyton-hall]:

**Type 1 DM (T1DM):** Autoimmune destruction of pancreatic β-cells (CD8+ CTL-mediated, Th1-driven; HLA-DR4/DQ8 association) → absolute insulin deficiency → hyperglycaemia + ketoacidosis (DKA). Requires exogenous insulin. Complications: retinopathy (non-proliferative → proliferative, tractional RD), nephropathy (Kimmelstiel-Wilson nodular glomerulosclerosis), peripheral neuropathy (stocking-glove), autonomic neuropathy, accelerated CVD.

**Type 2 DM (T2DM):** Peripheral insulin resistance (↓IRS-1/PI3K/Akt signalling in muscle and liver; ↑FFA → DAG → PKC-ε → inhibits IR kinase) → compensatory ↑insulin → progressive β-cell failure (ER stress, glucolipotoxicity, IL-1β-mediated apoptosis, islet amyloid [IAPP]) → absolute insulin deficiency (late stage). Strongly linked to obesity, sedentary lifestyle, metabolic syndrome.

**Treatment targets:** insulin resistance (metformin/AMPK → ↑GLUT4; pioglitazone/PPARγ); β-cell stimulation (sulfonylureas → KATP closure); GLP-1 receptor agonists (semaglutide, liraglutide → ↑insulin, ↓glucagon, ↓appetite, ↓weight); SGLT2 inhibitors (empagliflozin → ↑urinary glucose excretion → ↓blood glucose, ↑diuresis, cardioprotection) [^stryer-biochemistry].

### Thyroid Disorders

**Hypothyroidism:** Most common cause — Hashimoto's thyroiditis (autoimmune — anti-TPO and anti-thyroglobulin antibodies → lymphocytic infiltration → Hürthle cell metaplasia → gland destruction → ↓T3/T4 → ↑TSH). Clinical: fatigue, weight gain, cold intolerance, constipation, bradycardia, depression, myxoedema. Treatment: levothyroxine (L-T4).

**Hyperthyroidism:** Graves' disease (TSI/TSAb — thyroid-stimulating immunoglobulins, IgG activating TSH receptor → autonomous thyroid hormone synthesis → ↓TSH [suppressed], ↑FT4, ↑FT3). Clinical: weight loss, heat intolerance, tremor, palpitations, exophthalmos (orbital GAG accumulation), pretibial myxoedema, onycholysis. Treatment: antithyroids (methimazole/PTU), radioiodine (I-131), thyroidectomy.

### Adrenal Disorders

**Addison's disease (primary adrenal insufficiency):** Autoimmune (anti-21-hydroxylase antibodies) → adrenal cortical destruction → ↓cortisol + ↓aldosterone → hypotension, hyponatraemia, hyperkalaemia, hyperpigmentation (↑ACTH → ↑α-MSH via POMC cleavage → melanocyte MC1R). Life-threatening adrenal crisis (hypotension, vomiting, collapse) on stress. Treatment: hydrocortisone + fludrocortisone [^guyton-hall].

**Cushing's syndrome:** Excess cortisol. Causes: Cushing's disease (pituitary ACTH-secreting adenoma — ~70%), ectopic ACTH (small cell lung cancer, carcinoid — ~10%), adrenal adenoma/carcinoma (~20%), iatrogenic (glucocorticoid therapy — most common). Features: central obesity (visceral fat ↑), moon face, buffalo hump, striae, skin thinning, hypertension, osteoporosis, insulin resistance, immune suppression, proximal myopathy, psychiatric disturbance.

**Phaeochromocytoma:** Chromaffin cell tumour of adrenal medulla (or paraganglioma if extra-adrenal) → paroxysmal catecholamine secretion → hypertensive crisis, headache, sweating, palpitations ("rule of 10s": 10% malignant, 10% bilateral, 10% extra-adrenal, 10% in children, 10% familial). Associated with MEN2A/2B (RET mutation), VHL (von Hippel-Lindau), NF1 (neurofibromatosis), SDH mutations. Diagnosis: plasma metanephrines + 24h urine catecholamines [^guyton-hall].

### Pituitary Adenomas

Benign pituitary tumours (~10% prevalence on MRI):
- **Prolactinoma** (most common, 40%): hyperprolactinaemia → amenorrhoea, galactorrhoea (women); hypogonadism, erectile dysfunction (men); ↓GnRH pulsatility via TIDA neurons. Treatment: dopamine agonists (cabergoline, bromocriptine — dopamine = physiological prolactin inhibitor).
- **GH-secreting adenoma** (15–20%): acromegaly (in adults — enlarged hands, feet, jaw, soft tissue; ↑IGF-1; ↑glucose; cardiovascular complications; sleep apnoea); gigantism (in children — linear growth before epiphyseal fusion).
- **ACTH-secreting adenoma** (Cushing's disease, 10–15%): see above.
- **Non-functioning adenomas** (30–40%): mass effects (bitemporal hemianopia via optic chiasm compression; hypopituitarism from pituitary stalk compression).

### Multiple Endocrine Neoplasia (MEN) Syndromes

Autosomal dominant cancer predisposition syndromes [^guyton-hall]:

| Syndrome | Gene | Tumours |
|:---|:---|:---|
| MEN1 | MEN1 (menin — tumour suppressor) | Parathyroid adenomas (>95%), pituitary adenomas (prolactinoma common), pancreatic NETs (gastrinoma/Zollinger-Ellison, insulinoma, VIPoma) |
| MEN2A | RET (gain-of-function — codon 634) | Medullary thyroid carcinoma (MTC; 95%), phaeochromocytoma (50%), primary hyperparathyroidism (25%) |
| MEN2B | RET (codon 918) | MTC (aggressive, early), phaeochromocytoma, marfanoid habitus, mucosal neuromas, ganglioneuromatosis of GI tract |
| MEN4 | CDKN1B (p27) | Similar to MEN1 but RET/MEN1 mutation-negative |

### Metabolic Syndrome

Cluster of insulin resistance-driven metabolic abnormalities (WHO/NCEP-ATP III criteria: central obesity [waist >102 cm M, >88 cm F] + ≥2 of: TG ≥1.7 mmol/L; HDL <1.0/1.3 mmol/L; BP ≥130/85; fasting glucose ≥5.6 mmol/L) [^stryer-biochemistry]. Underlying mechanism: visceral adipose tissue ↑FFA + ↑TNF-α + ↓adiponectin → hepatic/peripheral insulin resistance → hyperinsulinaemia → dyslipidaemia (↑VLDL, ↓HDL, ↑small dense LDL) + hypertension (↑RAAS + SNS) + T2DM risk. Strongly predicts T2DM, cardiovascular disease, NAFLD, PCOS, sleep apnoea, and certain cancers.

## See Also

- [pancreas](../../06-organ/pancreas/README.md)
- [liver](../../06-organ/liver/README.md)
- [thymus](../../06-organ/thymus/README.md)
- [nervous-system](../nervous-system/README.md)
- [immune-system](../immune-system/README.md)
- [cardiovascular-system](../cardiovascular-system/README.md)
- [renal-system](../renal-system/README.md)
- [insulin](../../03-molecular/insulin/README.md)
- [cortisol](../../03-molecular/cortisol/README.md)
- [glucocorticoid-receptor](../../03-molecular/glucocorticoid-receptor/README.md)
- [dopamine](../../03-molecular/dopamine/README.md)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [Publisher →](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [Publisher →](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
