---
schema: human-scale-entry/v1
id: neuroendocrine-tumors
name: Neuroendocrine Tumors
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Neuroendocrine tumors arise from diffuse neuroendocrine cells; well-differentiated G1/G2 NETs are treated with SSA (octreotide/lanreotide) and lutetium-177 DOTATATE (NETTER-1); everolimus (RADIANT) and sunitinib approved for pNET; poorly differentiated NEC treated as SCLC."
aliases: ["neuroendocrine tumors", "NET", "NEN", "carcinoid tumor", "pNET", "pancreatic NET", "GEP-NET", "neuroendocrine carcinoma", "NEC", "PRRT", "Lutathera", "DOTATATE"]
sources:
  - id: yao-2011-radiant3
    type: peer-reviewed
    cite: "Yao JC, Shah MH, Ito T, et al. Everolimus for advanced pancreatic neuroendocrine tumors. N Engl J Med. 2011;364(6):514-523."
    doi: "10.1056/NEJMoa1009290"
    pmid: "21306237"
    url: "https://doi.org/10.1056/NEJMoa1009290"
  - id: raymond-2011-sunitinib-pnet
    type: peer-reviewed
    cite: "Raymond E, Dahan L, Raoul JL, et al. Sunitinib malate for the treatment of pancreatic neuroendocrine tumors. N Engl J Med. 2011;364(6):501-513."
    doi: "10.1056/NEJMoa1003825"
    pmid: "21306236"
    url: "https://doi.org/10.1056/NEJMoa1003825"
cross_links:
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "SSTR2 overexpression in well-differentiated NETs enables SSA therapy (octreotide/lanreotide; PROMID/CLARINET antiproliferative trials) and 177Lu-DOTATATE PRRT (NETTER-1: 14-month PFS benefit); DOTATATE PET/CT confirms SSTR2 expression for PRRT eligibility."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Everolimus (RADIANT-3: PFS 11.0 vs 4.6 months in pNET; RADIANT-4: PFS 11.0 vs 3.9 months in non-functional NET) is approved for progressive/metastatic NET; mTOR inhibition reduces HIF-1α, VEGF, and cell cycle progression; resistance via AKT rebound."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Sunitinib (VEGFR1/2/3/PDGFRA/B; A6181111 trial: PFS 11.4 vs 5.5 months) is approved for pancreatic NET; NETs are hypervascular tumors with high VEGF expression; bevacizumab studied in midgut NET; cabozantinib (VEGFR2+MET) under investigation."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Functioning pNETs include glucagonoma (necrolytic migratory erythema, diabetes), insulinoma (most common pNET), gastrinoma (Zollinger-Ellison), and VIPoma; SSTR2 agonists (octreotide) control glucagonoma and other secretory syndromes via α-cell glucagon inhibition."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "Germline MEN1 mutations underlie ~10% of pancreatic NETs, which in MEN1 are typically multifocal and non-functioning alongside parathyroid and pituitary tumors; menin loss (H3K4me3 at target promoters) is also the most common somatic event (~44%) in sporadic pNET."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Midgut carcinoids secrete serotonin that, once liver metastases bypass portal clearance, causes carcinoid syndrome — flushing, secretory diarrhea, and carcinoid heart disease; urinary 5-HIAA tracks it and telotristat (a tryptophan hydroxylase inhibitor) curbs refractory diarrhea."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The pancreas is a leading NET site: functioning pNETs (insulinoma, gastrinoma, glucagonoma, VIPoma) cause hormone syndromes while non-functioning pNETs grow silently; everolimus and sunitinib are pNET-specific approvals, and DAXX/ATRX-mutant pNETs use the ALT telomere pathway."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Neuroendocrine tumors and neuroblastoma are both neural-crest-derived, amine-handling cancers at opposite ends of age and behavior: NETs are well-differentiated, slow-growing adult tumors, while neuroblastoma is an aggressive MYCN-driven embryonal cancer of children."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small intestine (midgut) is a classic NET site: serotonin-secreting enterochromaffin-cell tumors of the ileum grow slowly but metastasize to the liver, producing carcinoid syndrome (flushing, diarrhea, carcinoid heart disease) and are SSTR2-positive."
  - target: 01-human/07-system/men4-syndrome
    relation: connects-to
    note: "MEN4, like MEN1, is a hereditary cause of neuroendocrine tumors: germline CDKN1B/p27 loss predisposes to pancreatic NETs alongside parathyroid and pituitary tumors, so a young or multifocal NET prompts germline MEN1 and CDKN1B testing for syndromic disease."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Pheochromocytoma/paraganglioma are neuroendocrine tumors of the adrenal medulla and sympathetic ganglia: like other NETs they express somatostatin receptors (enabling DOTATATE imaging and PRRT) but uniquely secrete catecholamines, causing paroxysmal hypertension."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "VHL disease is a major hereditary cause of neuroendocrine tumors: germline VHL loss predisposes to pancreatic neuroendocrine tumors and pheochromocytomas alongside its hemangioblastomas and clear-cell RCC, so a young patient with a panNET warrants VHL and MEN1 testing."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver dictates carcinoid syndrome in neuroendocrine tumors: a midgut NET's serotonin is normally cleared by hepatic first-pass, so flushing and diarrhea appear only once liver metastases dump vasoactive amines directly into the systemic circulation."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "Neuroendocrine tumors and small-cell lung cancer are the two ends of the neuroendocrine spectrum: well-differentiated NETs are indolent, while SCLC is a poorly differentiated, high-grade neuroendocrine carcinoma that grows explosively—same lineage, opposite tempo."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulinoma is the prototypical functional neuroendocrine tumor: a pancreatic-islet NET that autonomously secretes insulin, causing fasting hypoglycemia (Whipple's triad)—it shows how NETs are classified and treated by the hormone they produce."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is a major site of neuroendocrine tumors: from indolent typical bronchial carcinoids through atypical carcinoids to high-grade small-cell neuroendocrine carcinoma, all arising from pulmonary neuroendocrine cells—'lung NET' spans benign to lethal."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Neuroendocrine tumors share traits with neurons: they arise from diffuse-neuroendocrine-system cells that, like neurons, store and secrete signaling molecules in vesicles, so they express neuronal markers (synaptophysin, chromogranin) and can secrete hormones."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Carcinoid heart disease links NETs to the heart: serotonin from a metastatic midgut NET reaching the systemic circulation drives fibrosis of right-sided heart valves, causing tricuspid regurgitation—so an endocrine tumor's secretions remodel cardiac valves."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Functioning NETs secrete histamine and other mediators causing distinct syndromes: gastric and some foregut NETs release histamine producing atypical flushing, complementing serotonin's carcinoid syndrome—so a NET's secretory product determines its clinical picture."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Most neuroendocrine tumors arise in the digestive system: gastroenteropancreatic NETs (carcinoids, gastrinomas, insulinomas) form from the gut's diffuse hormone-secreting cells, so the GI tract and pancreas are the commonest primary sites and the cause of carcinoid syndrome."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "NETs are uniquely treated with targeted radiation: peptide receptor radionuclide therapy attaches a radioisotope to a somatostatin analog so SSTR2-rich tumors irradiate themselves, and Ga-68 PET images them the same way—radiation guided by the tumor's own receptor."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Neuroendocrine tumors straddle the nervous and endocrine systems: they arise from cells that, like the endocrine system, secrete hormones into blood, so functional NETs cause hormone syndromes (flushing, hypoglycemia, ulcers) treated by dampening that secretion."
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "Pancreatic neuroendocrine tumors are shaped by ATRX: loss of ATRX (or DAXX) switches on alternative lengthening of telomeres, marking tumors with distinct biology and a worse prognosis—part of why molecular profiling now guides NET management."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "The thymus is an aggressive site for neuroendocrine tumors: thymic carcinoids, often linked to MEN1 and seen in men who smoke, behave more aggressively than other carcinoids, so chest imaging is part of evaluating NET-prone patients."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Medullary thyroid carcinoma is a calcitonin-secreting neuroendocrine tumor: arising from thyroid C cells, it pours out calcitonin that serves as a sensitive tumor marker for diagnosis and monitoring—linking the NET family to a thyroid cancer."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Neuroendocrine tumors spin off fibrosis: serotonin from midgut carcinoids drives dense scarring—right-sided carcinoid heart-valve disease and mesenteric fibrosis that kinks the bowel—a distinctive complication of these slow but secretory tumors."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Carcinoid flushing is driven by mediators like bradykinin: NETs release vasoactive kinins and serotonin that dilate vessels, producing the episodic flushing, wheezing, and diarrhea of carcinoid syndrome when the liver can't clear them."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Neuroendocrine tumors hide in a cold immune niche shaped by regulatory T cells: low mutation burden and Treg-rich stroma make most NETs poorly responsive to checkpoint immunotherapy, steering treatment toward somatostatin analogs and PRRT instead."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Neuroendocrine tumors secrete hormones the way nerves fire—via calcium: like the normal neuroendocrine cells they arise from, they release hormones by calcium-triggered exocytosis, so this secretory machinery underlies the flushing and diarrhea of functional NETs."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Neuroendocrine tumors are richly vascular and oxygen-sensing: many, especially VHL-related ones, behave as pseudohypoxic and drive dense blood vessels, which is why their vascularity stands out on imaging and antiangiogenic drugs have a role."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages crowd the neuroendocrine tumor stroma: tumor-associated macrophages support its growth and blood supply within the immunosuppressive, Treg-rich niche, part of why these tumors resist checkpoint immunotherapy."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "A VIPoma drains the body's potassium: this pancreatic neuroendocrine tumor floods the gut with VIP, causing torrential watery diarrhea that wastes potassium (the WDHA syndrome), risking dangerous hypokalemia."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Neuroendocrine tumors flush the skin: carcinoid syndrome's serotonin and vasoactive peptides cause episodic flushing, and serotonin's drain on tryptophan can starve the skin of niacin, causing pellagra."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Neuroendocrine tumors are richly vascular: they recruit endothelial cells to build a dense blood supply, giving the bright tumor 'blush' on imaging that helps find these often-small lesions."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy defines what 'neuroendocrine' means: these tumor cells are stuffed with dense-core secretory granules — membrane-bound packets of hormone — the ultrastructural signature that marks a tumor as neuroendocrine when its tissue origin is unclear."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets hoard the serotonin these tumors spill: carcinoids release serotonin that circulating platelets soak up and store, so platelet-poor measurements and urinary 5-HIAA breakdown products are used to gauge the secreting tumor's activity."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Radioiodine hunts the catecholamine-avid ones: MIBG, a noradrenaline mimic tagged with iodine-123 or iodine-131, is taken up by these tumors to image them and, in higher doses, to deliver targeted radiation therapy."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Neuroendocrine tumors of the gut announce themselves with diarrhea: midgut carcinoids spill serotonin that speeds the bowel, and once they reach the liver the unfiltered hormones cause the flushing-and-diarrhea of carcinoid syndrome."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Neuroendocrine tumors favor bone when they spread: skeletal metastases to the marrow-bearing spine and pelvis are common in advanced disease, lighting up on the somatostatin-receptor scans used to stage them."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Carcinoid diarrhea drains the body's minerals: the relentless secretory diarrhea of a hormone-secreting neuroendocrine tumor flushes out magnesium and potassium, electrolytes that must be replaced alongside treating the tumor."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains define the tumor: chromogranin A and synaptophysin by immunohistochemistry confirm a lesion is neuroendocrine, and the Ki-67 antibody index grades how fast it divides — the single number that separates indolent NETs from aggressive carcinomas."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney limits the radioactive cure: peptide receptor radionuclide therapy with Lu-177 DOTATATE homes to SSTR2 but is filtered through and can injure the kidney, so amino-acid infusions are co-given to shield the tubules from the radiation dose."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Carcinoid hormones clench smooth muscle: serotonin and bradykinin from the tumor contract airway and gut smooth-muscle cells, causing the wheeze and cramping diarrhea of carcinoid syndrome that octreotide is given to quiet."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Serotonin scars the heart valves: in carcinoid heart disease the tumor's serotonin drives valvular fibroblasts to lay down fibrous plaques on the right-sided valves, stiffening them into the tricuspid and pulmonary lesions that cause right heart failure."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Tuberous sclerosis seeds neuroendocrine tumors: TSC1/TSC2 loss unleashes mTOR, predisposing to pancreatic neuroendocrine tumors — the same pathway that makes the mTOR inhibitor everolimus an effective therapy for advanced NETs."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "NETs grow along the PI3K-AKT-mTOR axis: signaling through AKT to mTOR sustains these tumors, the rationale behind everolimus and a resistance route when that drug is used, tying their biology to the broader growth-signaling network."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Some NETs run in cancer-predisposition families: neurofibromatosis type 1 raises the risk of duodenal somatostatinomas and other neuroendocrine tumors, one of several germline syndromes (with MEN1 and VHL) that seed these tumors decades early."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The stomach grows its own neuroendocrine tumors: gastric carcinoids arise from ECL cells, often driven by the high gastrin of atrophic gastritis or acid-suppressing drugs, a distinct and usually indolent NET tied to how the stomach regulates acid."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "One NET family floods the body with catecholamines: pheochromocytomas and paragangliomas pour out norepinephrine, causing the pounding hypertension and palpitations that set this secretory subtype apart from the serotonin-driven carcinoids."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Serotonin scars the right heart: in carcinoid heart disease, vasoactive amines from a metastatic midgut NET deposit fibrous plaques on the tricuspid and pulmonary valves, driving right-sided heart failure — a leading cause of death in carcinoid syndrome."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle control grades the tumor: CDKN2A and other cell-cycle alterations help separate indolent well-differentiated NETs from the aggressive, high-proliferation neuroendocrine carcinomas, informing grade and treatment."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The tumor and its surgery raise the clot risk: like other visceral cancers, neuroendocrine tumors and the major resections they require predispose to venous thromboembolism."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 supports the neuroendocrine clone: signaling through STAT3 backs proliferation and survival in neuroendocrine tumors, one of the pathways downstream of the mTOR and growth-factor activation that drives them."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB adds an inflammatory survival signal: neuroendocrine tumor cells engage NF-κB-dependent survival and angiogenic signaling, contributing to the growth of these often slow but persistent tumors."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Liver metastases and surgery invite infection: NETs commonly spread to the liver where biliary obstruction and tumor-debulking surgery can seed cholangitis and abdominal sepsis."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Their hormones and therapy unbalance glucose: pancreatic NETs like glucagonoma and somatostatinoma directly disturb glucose handling, and the somatostatin-analogue treatment used for most NETs suppresses insulin, together provoking diabetes."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Their radioligand therapy stresses the kidneys: peptide-receptor radionuclide therapy with lutetium-DOTATATE concentrates in the renal tubules, and the cumulative radiation can drive a slow decline into chronic kidney disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A chronic, flushing cancer wears on mood: the years-long course of metastatic NETs, the disabling diarrhea and flushing of carcinoid syndrome, and serotonin diversion away from the brain combine to raise depression risk."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Unpredictable flushing and a chronic cancer breed worry: the episodic carcinoid attacks, lifelong indolent-but-incurable course and continual imaging surveillance of NETs foster persistent health anxiety."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Resecting the tumour and its liver deposits heals slowly: surgery for primary NETs and hepatic debulking, sometimes in malnourished patients with carcinoid diarrhoea, leaves wounds prone to delayed closure."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "A smouldering tumour blunts the marrow: the chronic inflammatory state of metastatic NETs, compounded by GI blood loss from bowel primaries, produces a normocytic anemia of chronic disease."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Carcinoid shows on the skin: serotonin-secreting NETs cause the episodic flushing of carcinoid syndrome, and tryptophan diversion to serotonin depletes niacin, producing the dermatitis of pellagra."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "They grow in and squeeze the airways: bronchial carcinoids are a recognised NET, and the bronchospasm and wheeze of carcinoid syndrome are part of its vasoactive-mediator effects."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Pellagra and metastases reach the brain: the niacin deficiency of serotonin-secreting NETs causes the dementia of pellagra, and NETs can metastasise to the central nervous system."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Serotonin scars the right heart: carcinoid heart disease is a hallmark complication in which serotonin from the tumour fibroses the tricuspid and pulmonary valves, causing right heart failure."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It spreads to nodes and liver with desmoplasia: NETs metastasise to mesenteric lymph nodes, provoking a dense desmoplastic reaction that kinks the bowel, and characteristically to the liver."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It seeds the bones as dense deposits: well-differentiated neuroendocrine tumours characteristically produce osteoblastic (sclerotic) bone metastases detectable on functional imaging."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It is the model for receptor-targeted treatment: somatostatin analogues, Lu-177 DOTATATE peptide-receptor radionuclide therapy and mTOR inhibitors exploit neuroendocrine tumours' somatostatin receptors and biology."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its radionuclide therapy taxes the kidney: peptide-receptor radionuclide therapy concentrates in and can damage the kidneys, requiring amino-acid renal protection during treatment."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "They can arise in the gonads: primary neuroendocrine tumours (carcinoids) occur in the ovary and testis, and ovarian carcinoids can secrete hormones causing the carcinoid syndrome."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for pancreatic and high-grade tumours: capecitabine-temozolomide treats pancreatic neuroendocrine tumours, and platinum-etoposide treats poorly differentiated neuroendocrine carcinomas."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "Pancreatic NETs arise from these cells: insulinomas, gastrinomas and other functioning tumours of the islets of Langerhans are the pancreatic neuroendocrine tumours, secreting hormones that drive distinctive syndromes."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy for the high-grade end: poorly differentiated neuroendocrine carcinomas, like small-cell lung cancer, are treated with chemotherapy plus PD-1/PD-L1 inhibitors, while well-differentiated NETs stay immunologically cold."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "It can scar the heart valves: serotonin and vasoactive substances from metastatic carcinoid tumours deposit fibrous plaques on the right-sided endocardium and tricuspid/pulmonary valves, the carcinoid heart disease that complicates the syndrome."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "A shared somatostatin-receptor target: like meningiomas, neuroendocrine tumours strongly express somatostatin receptor 2, so both are imaged with DOTATATE PET and can be treated with peptide receptor radionuclide therapy."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Another inherited endocrine-tumour syndrome: like MEN1, Carney complex predisposes to neuroendocrine and endocrine tumours—pituitary, thyroid and adrenal—through PRKAR1A loss, joining the familial syndromes that spawn NETs."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver metastases drive carcinoid syndrome: midgut NETs spread to the hepatic lobule, and only when their serotonin bypasses hepatic first-pass clearance—via liver metastases draining to systemic veins—do flushing and diarrhoea appear."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Medullary thyroid carcinoma is a NET: arising from calcitonin-secreting C cells and driven by RET, MTC is a neuroendocrine tumour, linking the NET family to the thyroid."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Bronchial carcinoid: a well-differentiated lung neuroendocrine tumour arises in the airway and alveolar region, the indolent end of pulmonary neuroendocrine neoplasia distinct from small-cell carcinoma."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Two pancreatic tumours, opposite outlooks: well-differentiated pancreatic neuroendocrine tumours are far more indolent and treatable than pancreatic ductal adenocarcinoma, making their distinction one of the most consequential in oncology."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Gastric carcinoids: ECL-cell neuroendocrine tumours of the stomach (types 1-2 driven by hypergastrinaemia) are a distinct entity from gastric adenocarcinoma, with different drivers, behaviour and management."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The carcinoid cell of origin: midgut carcinoids arise from enterochromaffin cells scattered through the intestinal epithelium, the serotonin-secreting source whose liver metastases produce carcinoid syndrome."
  - target: 01-human/03-molecular/dll3
    relation: connects-to
    note: "High-grade target: DLL3 is expressed on poorly differentiated neuroendocrine carcinomas, the target of DLL3-directed agents like tarlatamab that extend beyond somatostatin-based therapy."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypervascular tumours: HIF-1α-driven, VEGF-rich angiogenesis makes neuroendocrine tumours strikingly vascular, the rationale for anti-angiogenic agents such as sunitinib."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Grade and progression: TERT activation maintaining telomeres accompanies the progression of neuroendocrine tumours toward higher-grade, more aggressive disease."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative drive: MYC activation drives the higher proliferative rate of poorly differentiated neuroendocrine carcinomas, marking their aggressive behaviour."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle control: with CDKN2A loss in higher-grade tumours, cyclin D-CDK4/6 activity propels neuroendocrine tumour cells through the G1 checkpoint."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic progression: EZH2 overexpression contributes to the dedifferentiation and progression of neuroendocrine tumours, an epigenetic therapeutic candidate."
  - target: 01-human/03-molecular/men1
    relation: connects-to
    note: "Menin loss: inactivation of the MEN1 tumour suppressor is the commonest genetic lesion in pancreatic neuroendocrine tumours, linking sporadic NETs to the MEN1 hereditary syndrome."
  - target: 01-human/03-molecular/ret
    relation: connects-to
    note: "RET oncogene: activating RET mutations drive medullary thyroid carcinoma, the calcitonin-secreting neuroendocrine tumour of MEN2, targeted by selective RET inhibitors."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into neuroendocrine tumours, shaping a stroma that supports growth and modulates therapy response."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Hepatic metastasis: CXCR4 on neuroendocrine tumour cells follows CXCL12 gradients to the liver, the dominant metastatic site whose tumour burden drives the carcinoid syndrome and much of NET mortality."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Radionuclide-induced apoptosis: peptide-receptor radionuclide therapy (Lutathera) delivers SSTR2-targeted radiation that kills NET cells through DNA-damage-driven caspase-3 apoptosis, a mainstay for progressive somatostatin-receptor-positive tumours."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Carcinoid fibrosis: serotonin from carcinoid tumours drives TGF-β-mediated fibrosis, producing the desmoplastic mesenteric fibrosis and the right-sided carcinoid heart disease that complicate the syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Bispecific immunotherapy: the DLL3-CD3 bispecific tarlatamab redirects cytotoxic T cells to kill DLL3-expressing high-grade neuroendocrine carcinomas through perforin and granzyme, an immunotherapy advance for tumours beyond somatostatin-based control."
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "Hereditary syndrome: von Hippel-Lindau disease predisposes to pancreatic neuroendocrine tumours, one of several inherited syndromes — with MEN1, NF1 and tuberous sclerosis — that cause NETs and prompt germline testing in young or multifocal cases."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenetic subtyping: pancreatic neuroendocrine tumours are shaped by chromatin and DNA-methylation changes (MEN1, DAXX/ATRX), and methylation profiling defines clinically distinct subgroups, making the epigenome central to their classification."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Growth axis: PIK3CA drives the PI3K-AKT-mTOR pathway (AKT and mTOR already mapped) in neuroendocrine tumours, the basis for the mTOR inhibitor everolimus in their treatment."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "DLL3-Notch axis: the Notch ligand DLL3 (mapped) is aberrantly expressed in high-grade neuroendocrine tumours, and dysregulated NOTCH signalling shapes their differentiation, with DLL3 itself a bispecific-antibody target."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Proliferative grading: the cyclin-D-CDK4/6 axis (cyclin-D1 and CDKN2A already mapped) releases E2F1 to drive the cell-cycle activity reflected in the Ki67 index that grades neuroendocrine tumours."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Antiangiogenic target: the VEGF/PDGF angiogenic axis (VEGF already mapped) sustains the characteristically vascular neuroendocrine tumours and is the target of the multikinase inhibitor sunitinib."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "mTOR pathway: PTEN loss releases the PI3K-AKT-mTOR axis (AKT, PIK3CA and mTOR already mapped) that drives neuroendocrine-tumour growth and is inhibited therapeutically by everolimus."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Grade dichotomy: combined RB1 and TP53 loss distinguishes the high-grade, poorly-differentiated neuroendocrine carcinomas from well-differentiated NETs, releasing the cell-cycle checkpoint (CDKN2A and E2F1 already mapped)."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is a marker and modulator of the survival and microenvironment interactions of neuroendocrine tumours."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RAS-ERK-MAPK signalling, engaged downstream of RET and other receptor tyrosine kinases (RET mapped), provides a proliferative input to neuroendocrine tumours."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT3 signalling (STAT3 mapped) provides a proliferative and immunomodulatory input to neuroendocrine tumours."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune microenvironment of neuroendocrine tumours, relevant to immunotherapy in the high-grade neuroendocrine carcinomas."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the differentiation and microenvironment of neuroendocrine tumours."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (cyclin-D1, CDKN2A and RB1 already mapped) drives the cell-cycle progression of neuroendocrine tumours."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-mTOR-driven FOXO inactivation (AKT, PIK3CA, and mTOR already mapped) removes a pro-apoptotic brake in neuroendocrine tumors."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and secretory-cell signaling of neuroendocrine tumors."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation restrains apoptosis in neuroendocrine tumors."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative signaling of neuroendocrine tumors."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of neuroendocrine tumors."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival of neuroendocrine tumor cells under metabolic and therapeutic stress."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of neuroendocrine tumors."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of neuroendocrine tumors."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of neuroendocrine tumors."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of neuroendocrine tumors."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of neuroendocrine tumors."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of neuroendocrine tumors."
  - target: 01-human/03-molecular/cdkn1b
    relation: connects-to
    note: "p27 gatekeeper: germline CDKN1B (p27Kip1) loss causes MEN4, an inherited pancreatic/pituitary neuroendocrine tumour syndrome, and somatic p27 loss releases the cell-cycle brake that restrains well-differentiated NET proliferation, complementing the MEN1 axis already mapped."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Syndromic co-secretion: in MEN1-associated NET the parathyroid glands hypersecrete PTH, so primary hyperparathyroidism and hypercalcaemia frequently accompany the pancreatic and pituitary neuroendocrine tumours, tying the NET syndrome to calcium-endocrine physiology."
  - target: 01-human/03-molecular/sdhb
    relation: connects-to
    note: "Pseudohypoxic driver: SDHB loss defines a metabolic subset of neuroendocrine tumours and paragangliomas where succinate accumulation stabilises HIF (HIF-1α already mapped), driving the intense vascularity and DOTATATE avidity characteristic of these lesions."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Carcinoid heart disease: serotonin-secreting midgut neuroendocrine tumours (serotonin already mapped) cause fibrotic plaques on the right-sided heart valves, and troponin marks the myocardial strain of the resulting right heart failure."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Gastrinoma acid: gastrin-secreting neuroendocrine tumours drive massive gastric acid (proton) secretion (Zollinger-Ellison syndrome), causing refractory peptic ulceration controlled with high-dose proton-pump inhibitors."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Adrenal medullary tumours: phaeochromocytomas and paragangliomas are catecholamine-secreting neuroendocrine tumours of the adrenal medulla and sympathetic ganglia (SDHB already mapped), part of the spectrum that DOTATATE and MIBG imaging localise."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "Ectopic ACTH: bronchial and pancreatic neuroendocrine tumours can secrete ACTH ectopically, driving cortisol excess and ectopic Cushing syndrome, one of the paraneoplastic hormone syndromes of the neuroendocrine tumour spectrum."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Carcinoid mediators: prostaglandins, with the serotonin, histamine and bradykinin (already mapped) released by metastatic carcinoid tumours, contribute to the flushing and diarrhoea of the carcinoid syndrome that somatostatin analogues suppress."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Flushing and vasculature: nitric oxide contributes to the vasodilatory flushing of the carcinoid syndrome and, with VEGF (already mapped), the rich vasculature of these often highly vascular neuroendocrine tumours."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment of the neuroendocrine tumours dampens the anti-tumour immune response, part of the immune biology relevant to the immunotherapy of the aggressive or metastatic tumours."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Incretin-secreting tumours: GLP-1 reflects the enteropancreatic incretin biology of the neuroendocrine tumours (insulin and glucagon already mapped), and rare GLP-1-secreting tumours cause hypoglycaemia, part of the functional-tumour spectrum."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the neuroendocrine-tumour stroma, part of its immune microenvironment."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immune microenvironment of the neuroendocrine tumours."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunotherapy: the cytotoxic T cells (PD-1 and perforin already mapped) are the target of the checkpoint immunotherapy explored in the high-grade neuroendocrine carcinomas, which the immunosuppressive stroma limits."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Islet zinc: zinc is stored with insulin (already mapped) in the islet secretory granules, and the zinc-insulin hexamer is part of the biology of the insulinomas among the pancreatic neuroendocrine tumours."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Functional-tumour metabolic adipokine: leptin reflects the metabolic disturbance of the functional (insulin and glucagon already mapped) neuroendocrine tumours and the metabolic milieu of the disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic disturbance of the functional neuroendocrine tumours."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic milieu of the neuroendocrine tumours."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon therapy: the type-I interferon, historically used (with the somatostatin analogues — SSTR2 already mapped) to treat the carcinoid/NET, shapes the innate-immune microenvironment of the neuroendocrine tumours."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the (limited) immune response to the neuroendocrine tumours."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the neuroendocrine-tumour immune microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the neuroendocrine tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the neuroendocrine-tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the neuroendocrine-tumour microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the neuroendocrine tumours."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the neuroendocrine tumours."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the tumour antigen to the T cells (already mapped) shaping the adaptive immune response against the neuroendocrine tumours."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the neuroendocrine tumours."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate cytotoxicity: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance within the immune microenvironment of the neuroendocrine tumours."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Tumour complement: the complement C3 activation contributes to the inflammatory dimension of the well-vascularised (VEGF already mapped) neuroendocrine tumour stroma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuroendocrine stroma alarmin: TSLP from the desmoplastic NET stroma activates dendritic cells (already mapped) and mast cells (already mapped), shaping the immune microenvironment and driving the type-2 inflammatory stromal response of carcinoid and pancreatic NETs."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "NET immune surveillance: complement C5 (with C3 already mapped) drives complement-dependent cytotoxicity against NETs; C5a–C5aR1 (already mapped) recruits the myeloid infiltrate into the somatostatin-receptor-expressing carcinoid tumour stroma for immune surveillance."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Carcinoid desmoplastic stroma: periostin, downstream of TGF-β (already mapped), drives the fibrotic peritoneal carcinomatosis and cardiac fibrosis (heart already mapped) of the desmoplastic response to the carcinoid syndrome of midgut neuroendocrine tumours."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "NET complement regulation: C1-INH controls the classical-pathway arm (complement C3, C5 and C5aR1 already mapped) in the NET tumour microenvironment, modulating complement-dependent cytotoxicity against somatostatin-receptor (sstr2 already mapped) NET cells."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroendocrine EPO signalling: erythropoietin receptor (EPOR) on neuroendocrine tumour cells activates the JAK2/STAT3 (already mapped) pro-survival pathway, complementing the mTOR (already mapped) and VEGF (already mapped) signalling in NET tumour growth and treatment anaemia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Alternative complement: factor H limits alternative-pathway complement activation (complement C3, C5 and C5aR1 already mapped) in the neuroendocrine-tumour stroma, preventing excessive complement-driven inflammation and protecting the carcinoid vascular endothelium."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Carcinoid melatonin: melatonin co-secreted by enterochromaffin cells alongside serotonin (already mapped) inhibits NET proliferation through MT1/MT2 receptor-mediated cAMP suppression, counteracting the mTOR (already mapped) and VEGF (already mapped) pro-survival NET signalling."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone microenvironment: testosterone modulates the NET tumour immune microenvironment through androgen receptor signalling on tumour-infiltrating mast cells (already mapped) and macrophages (already mapped), influencing the carcinoid inflammatory cascade."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Neuroendocrine prolactin: prolactin binds prolactin receptors on NET cells to activate JAK2/STAT3 (already mapped) and mTOR (already mapped) pro-proliferative signalling; pituitary prolactinomas (hypothalamus already mapped) represent the archetype NET hypersecretion syndrome."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "NET oxytocin signalling: oxytocin receptors on enterochromaffin NETs couple to Gαq-IP3-PKC, cross-activating mTOR (already mapped) and VEGF (already mapped) pro-proliferative cascades in the carcinoid microenvironment."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "NET vasopressin secretion: NETs co-secrete vasopressin-like peptides activating V1b/V2 receptors on NET stroma, promoting angiogenesis via VEGF (already mapped) upregulation and macrophage (already mapped) recruitment."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "NET selenium redox: selenium via GPX and thioredoxin reductase suppresses ROS that stabilise HIF-1α and drive VEGF (already mapped) and mTOR (already mapped) pro-angiogenic signalling in neuroendocrine tumours."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "NET sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) neuroendocrine tumour cascade."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "NET copper: copper, as cofactor of SOD1 in macrophages (already mapped) and endothelial cells (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative tumour cascade of neuroendocrine tumours."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "NET phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and macrophages (already mapped), supports neuroendocrine tumour immune surveillance; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "NET iron: iron, via ferritin in macrophages (already mapped) and fibroblasts (already mapped), modulates redox balance in the neuroendocrine tumour microenvironment; iron dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "NET chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in the neuroendocrine TME; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of NET."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "NET sulfur: sulfur-containing amino acids in macrophages (already mapped) and fibroblasts (already mapped) maintain redox buffering; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of neuroendocrine tumors."
---

# Neuroendocrine Tumors

## Overview

**Neuroendocrine tumors (NETs)** are a heterogeneous group of neoplasms arising from the diffuse neuroendocrine system — secretory cells distributed throughout the body that share features of neurons and endocrine glands (dense-core secretory granules, specific hormone production, chromogranin A/synaptophysin expression). NETs range from indolent well-differentiated tumors (G1 carcinoids) with decades-long survival to aggressive poorly differentiated neuroendocrine carcinomas (NECs) biologically similar to small cell lung cancer (SCLC) with median OS <12 months. Gastroenteropancreatic NETs (GEP-NETs) account for the majority of NETs, with the small bowel (midgut carcinoids), pancreas, and rectum being the most common primary sites. The therapeutic revolution in GEP-NET includes: somatostatin analogs (SSA) for symptom control and antiproliferative effect; peptide receptor radionuclide therapy (PRRT) with lutetium-177 DOTATATE (NETTER-1); mTOR inhibition with everolimus (RADIANT trials); and sunitinib for pancreatic NET [^yao-2011-radiant3] [^raymond-2011-sunitinib-pnet].

**Incidence and epidemiology:**
- Overall incidence: ~7/100,000/year in the USA; prevalence ~170,000 (rising due to better detection)
- Most common primary sites: Rectum (~25%), small intestine (~22%), pancreas (~15%), lung (~13%), appendix (~8%), stomach (~7%), colon (~7%)
- Small intestinal NETs (midgut carcinoids): Well-differentiated G1/G2; SSTR2+; often present with liver metastases + carcinoid syndrome; 5-year OS ~83% localized, ~32% metastatic
- Pancreatic NETs (pNET): Functioning (insulinoma, gastrinoma, glucagonoma) or non-functioning; VHL syndrome, MEN1 (MEN1 germline mutations in ~10% of pNET → multiple tumors); 5-year OS ~55-65% all stages
- Appendix NETs: Incidentally found at appendectomy; most <2 cm → appendectomy curative; >2 cm → right hemicolectomy

**WHO 2022 classification:**
- **NET G1 (Ki-67 <3%):** Well-differentiated; low mitotic rate; slowly progressive; SSA antiproliferative
- **NET G2 (Ki-67 3-20%):** Well-differentiated; intermediate; SSA + targeted therapy; PRRT
- **NET G3 (Ki-67 >20%):** Well-differentiated but high Ki-67; SSTR2 often retained; PRRT may work; distinct from NEC
- **NEC (poorly differentiated, Ki-67 >20%):** SCLC-type (small cell NEC) or large cell NEC; SSTR2 low/absent; platinum/etoposide
- **MiNEN (mixed neuroendocrine-non-neuroendocrine neoplasm):** ≥30% of each component; treat aggressive component

## Structure

### Tumor biology and neuroendocrine differentiation markers

**IHC markers of neuroendocrine differentiation:**
- **Chromogranin A (CgA):** Secreted from dense-core granules; elevated serum CgA in ~70-90% of functioning NETs; serum marker for monitoring; false positive with PPIs (chromogranin production is pH-sensitive); IHC positivity in >90% of well-differentiated NETs
- **Synaptophysin:** Presynaptic vesicle membrane protein; IHC positive in >95% of well-differentiated NETs; more sensitive than CgA for poorly differentiated NEC
- **Insulinoma-associated protein 1 (INSM1):** Nuclear transcription factor; highly specific neuroendocrine marker; positive in NET, NEC, SCLC, Merkel cell carcinoma; negative in adenocarcinoma
- **SSTR2A (IHC):** Semi-quantitative SSTR2 expression; Volante/Papotti scoring (0-3+); correlates with DOTATATE PET avidity; used for PRRT patient selection when PET not available
- **Ki-67 (MIB-1 antibody):** Proliferative index; defines WHO grade; counted in 500 cells in hotspot; critical for G1/G2/G3 classification

**Site-specific markers:**
- Midgut carcinoid: Serotonin-positive; CDX2+ (intestinal origin); SSTR2+ high
- pNET: Islet-specific markers — insulin (insulinoma), gastrin (gastrinoma), glucagon (glucagonoma), pancreatic polypeptide (PP-oma), VIP (VIPoma), somatostatin (somatostatinoma); non-functioning pNET: may be chromogranin+/synaptophysin+ without hormonal syndrome
- Lung carcinoid: TTF-1+/- (atypical carcinoid more often TTF-1+); CK7+; SSTR2/5+ (typical > atypical); DLL3 (Delta-like ligand 3) overexpression in both carcinoid and SCLC

**Molecular alterations:**
- pNET-specific: MEN1 mutations (~44%; menin → H3K4me3 loss → growth suppression); DAXX/ATRX mutations (~25% each; alternative lengthening of telomeres, ALT phenotype; poorer prognosis in pNET); VHL mutations; SETD2; mTOR pathway (TSC2, PIK3CA, PTEN) in ~15%
- Midgut carcinoid: CDKN1B (p27) mutations ~8%; MEN1/DAXX/ATRX less common; SSTR2 high; very stable genome; YY1 and EGLN1 mutations
- MEN1 syndrome (germline MEN1 mutation): Parathyroid adenoma, pituitary adenoma, pNET; pNETs in MEN1 are often multifocal, non-functioning; surveillance + surgery for functional tumors or >2 cm non-functional
- VHL syndrome: Somatostatinoma in duodenum (periampullary); pNET (non-functional, often); clear cell RCC

### Functioning syndrome pathophysiology

**Carcinoid syndrome:**
From serotonin, substance P, bradykinin, histamine secreted by midgut NETs with liver metastases (liver fails to inactivate serotonin that bypasses portal filtration in liver mets): Flushing (episodic, triggered by food/alcohol/stress), secretory diarrhea (watery, frequent), bronchospasm, carcinoid heart disease (right-sided valvular lesions from serotonin exposure to right heart = tricuspid regurgitation + pulmonary stenosis; Hedinger syndrome). Urinary 5-HIAA (24-hour urine): Elevated in ~70-85% of carcinoid syndrome patients. Treatment: SSA (octreotide/lanreotide) as backbone; telotristat ethyl (tryptophan hydroxylase-1 inhibitor, reduces serotonin synthesis, FDA 2017) for carcinoid diarrhea refractory to SSA.

**Insulinoma:**
Most common functioning pNET; unregulated insulin secretion → hypoglycemia; Whipple's triad: symptoms of hypoglycemia, glucose <45 mg/dL, relief with glucose; 90-95% benign single adenoma (<2 cm); 72-hour fast → insulin, C-peptide, proinsulin, glucose; CT/MRI/EUS for localization (small, vascular); surgical enucleation curative; diazoxide (Kfᴷ opener → reduces insulin secretion) for unresectable.

**Gastrinoma (Zollinger-Ellison Syndrome):**
Gastrin-secreting tumor → hypergastrinemia → excessive HCl → multiple peptic ulcers, refractory GERD, diarrhea; ~25% in MEN1; ~60% in pancreas (duodenal more common in sporadic); secretin stimulation test → gastrin spike (paradoxical); PPI therapy controls acid secretion; surgery for sporadic gastrinoma; somatostatin analogs reduce gastrin in ~50%.

## Function

### GEP-NET natural history and staging

**ENETS/AJCC staging (TNM, site-specific):**
Midgut and other NET: T1-T4 by tumor size and invasion; N0/N1 by regional nodal status; M0/M1a (liver only) / M1b (extrahepatic) / M1c (diffuse metastatic). Functional staging by Ki-67 grade. Prognosis: G1 midgut NET with liver mets → 10-year OS ~30-50% (slow-growing); G3 NET or NEC → 1-year OS <50%.

**Chromogranin A monitoring:**
Serum CgA correlates with tumor burden in most GEP-NETs; useful for monitoring response to therapy or progression; CgA doubling time predicts outcomes. PPI-induced hypergastrinemia → ECL cell hyperplasia → CgA elevation (false positive); hold PPI ≥2 weeks before CgA measurement.

## Pathology

### Diagnosis and imaging

**Biochemical diagnosis:**
- Carcinoid syndrome: 24-hour urine 5-HIAA (serotonin metabolite) + serum serotonin
- Insulinoma: 72-hour fast (glucose, insulin, C-peptide, proinsulin, β-hydroxybutyrate)
- Gastrinoma: Fasting serum gastrin; secretin stimulation test (>200 pg/mL increase = positive)
- Glucagonoma: Elevated fasting glucagon (>500 pg/mL); characteristic rash
- VIPoma: Watery diarrhea + hypokalemia + achlorhydria (WDHA/Verner-Morrison); elevated VIP

**Functional imaging:**
- **68Ga-DOTATATE PET/CT (preferred):** Sensitivity ~94-96% for SSTR2+ lesions; superior to conventional CT/MRI for lymph node and peritoneal deposits; replaces OctreoScan (99mTc-HYNIC-TOC) in most centers
- **FDG PET:** Useful for G3/NEC (high Ki-67, high glycolytic activity) where DOTATATE uptake is low; "flip-flop" pattern: high DOTATATE/low FDG = G1-G2; high FDG/low DOTATATE = G3/NEC
- **68Ga-DOTANOC:** Binds SSTR2, SSTR3, SSTR5; broader coverage than DOTATATE; preferred in some European centers

### Treatment algorithms

**Localized resectable disease:**
Curative-intent surgery for all localized NETs; appendix NETs <2 cm → appendectomy sufficient; pNET <2 cm, non-functioning: watchful waiting vs. surveillance (indolent biology); cytoreductive surgery ("debulking") in selected patients with liver-dominant metastatic NET for symptom control and potential survival benefit.

**Metastatic GEP-NET — systemic treatment sequence:**
1. **SSA antiproliferative (first-line, SSTR2+ G1/G2):** Octreotide LAR 30 mg q28d or lanreotide 120 mg q28d; PROMID (midgut) and CLARINET (GEP-NET) trials; telotristat for carcinoid diarrhea add-on
2. **177Lu-DOTATATE PRRT (progressive SSTR2+ NET):** NETTER-1 (midgut); also used off-label in pNET and other SSTR2+ sites; 4 cycles q8-12 weeks; requires adequate kidney function (GFR >40); after PRRT, SSA maintenance
3. **Everolimus (mTOR inhibitor):** RADIANT-3 (pNET) [^yao-2011-radiant3], RADIANT-4 (non-functional GEP/lung NET); well-tolerated orally; stomatitis, fatigue, hyperglycemia, pneumonitis toxicities
4. **Sunitinib (pNET only):** [^raymond-2011-sunitinib-pnet] 37.5 mg/day continuous; approved specifically for pNET; VEGFR/PDGFR inhibitor; hypertension, fatigue, hand-foot syndrome
5. **Chemotherapy (pNET, G3, NEC):** Streptozocin + doxorubicin (classic pNET); temozolomide + capecitabine (TEMCAP: ORR ~70% in MGMT-methylated pNET); cisplatin + etoposide (platinum-etoposide for NEC); FOLFOX/FOLFIRI for intermediate G3
6. **Hepatic-directed therapy (liver-dominant mets):** Bland embolization, TACE, SIRT (Y-90 radioembolization, SIRFLOX/TELESTAR data); ablation (RFA, MWA) for oligometastatic disease

**Poorly differentiated NEC:**
Treatment identical to SCLC: cisplatin (or carboplatin) + etoposide (4-6 cycles); ORR ~40-60% but brief duration (~6-8 months); atezolizumab + carboplatin/etoposide (IMpower133 extrapolation) used in some centers; no established immunotherapy approval specifically for extrapulmonary NEC; NTRK fusion (rare) → larotrectinib.

**Peptide receptor radionuclide therapy (PRRT) eligibility:**
- SSTR2+ (68Ga-DOTATATE PET: Krenning score ≥3, i.e., uptake ≥ liver uptake intensity)
- Well-differentiated G1/G2 (or selected G3 NET with SSTR2 retention)
- Adequate renal function (GFR >40 mL/min); adequate bone marrow (no extensive bone metastases)
- Progressive disease (typically after/concurrent with SSA)
- Dosimetry individualized; amino acid renal protection protocol

## Connections

- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — SSTR2 overexpression in well-differentiated NETs enables SSA therapy (octreotide/lanreotide; PROMID/CLARINET antiproliferative trials) and 177Lu-DOTATATE PRRT (NETTER-1: 14-month PFS benefit); DOTATATE PET/CT confirms SSTR2 expression for PRRT eligibility.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Everolimus (RADIANT-3: PFS 11.0 vs 4.6 months in pNET; RADIANT-4: PFS 11.0 vs 3.9 months in non-functional NET) is approved for progressive/metastatic NET; mTOR inhibition reduces HIF-1α, VEGF, and cell cycle progression; resistance via AKT rebound.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Sunitinib (VEGFR1/2/3/PDGFRA/B; A6181111 trial: PFS 11.4 vs 5.5 months) is approved for pancreatic NET; NETs are hypervascular tumors with high VEGF expression; bevacizumab studied in midgut NET; cabozantinib (VEGFR2+MET) under investigation.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Functioning pNETs include glucagonoma (necrolytic migratory erythema, diabetes), insulinoma (most common pNET), gastrinoma (Zollinger-Ellison), and VIPoma; SSTR2 agonists (octreotide) control glucagonoma and other secretory syndromes via α-cell glucagon inhibition.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — Germline MEN1 mutations underlie ~10% of pancreatic NETs, which in MEN1 are typically multifocal and non-functioning alongside parathyroid and pituitary tumors; menin loss (H3K4me3 at target promoters) is also the most common somatic event (~44%) in sporadic pNET.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Midgut carcinoids secrete serotonin that, once liver metastases bypass portal clearance, causes carcinoid syndrome — flushing, secretory diarrhea, and carcinoid heart disease; urinary 5-HIAA tracks it and telotristat (a tryptophan hydroxylase inhibitor) curbs refractory diarrhea.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The pancreas is a leading NET site: functioning pNETs (insulinoma, gastrinoma, glucagonoma, VIPoma) cause hormone syndromes while non-functioning pNETs grow silently; everolimus and sunitinib are pNET-specific approvals, and DAXX/ATRX-mutant pNETs use the ALT telomere pathway.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Neuroendocrine tumors and neuroblastoma are both neural-crest-derived, amine-handling cancers at opposite ends of age and behavior: NETs are well-differentiated, slow-growing adult tumors, while neuroblastoma is an aggressive MYCN-driven embryonal cancer of children.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small intestine (midgut) is a classic NET site: serotonin-secreting enterochromaffin-cell tumors of the ileum grow slowly but metastasize to the liver, producing carcinoid syndrome (flushing, diarrhea, carcinoid heart disease) and are SSTR2-positive.
- `connects-to` → **[MEN4 Syndrome](../men4-syndrome/README.md)** — MEN4, like MEN1, is a hereditary cause of neuroendocrine tumors: germline CDKN1B/p27 loss predisposes to pancreatic NETs alongside parathyroid and pituitary tumors, so a young or multifocal NET prompts germline MEN1 and CDKN1B testing for syndromic disease.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Pheochromocytoma/paraganglioma are neuroendocrine tumors of the adrenal medulla and sympathetic ganglia: like other NETs they express somatostatin receptors (enabling DOTATATE imaging and PRRT) but uniquely secrete catecholamines, causing paroxysmal hypertension.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — VHL disease is a major hereditary cause of neuroendocrine tumors: germline VHL loss predisposes to pancreatic neuroendocrine tumors and pheochromocytomas alongside its hemangioblastomas and clear-cell RCC, so a young patient with a panNET warrants VHL and MEN1 testing.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver dictates carcinoid syndrome in neuroendocrine tumors: a midgut NET's serotonin is normally cleared by hepatic first-pass, so flushing and diarrhea appear only once liver metastases dump vasoactive amines directly into the systemic circulation.
- `connects-to` → **[Small Cell Lung Cancer](../sclc/README.md)** — Neuroendocrine tumors and small-cell lung cancer are the two ends of the neuroendocrine spectrum: well-differentiated NETs are indolent, while SCLC is a poorly differentiated, high-grade neuroendocrine carcinoma that grows explosively—same lineage, opposite tempo.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulinoma is the prototypical functional neuroendocrine tumor: a pancreatic-islet NET that autonomously secretes insulin, causing fasting hypoglycemia (Whipple's triad)—it shows how NETs are classified and treated by the hormone they produce.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is a major site of neuroendocrine tumors: from indolent typical bronchial carcinoids through atypical carcinoids to high-grade small-cell neuroendocrine carcinoma, all arising from pulmonary neuroendocrine cells—'lung NET' spans benign to lethal.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Neuroendocrine tumors share traits with neurons: they arise from diffuse-neuroendocrine-system cells that, like neurons, store and secrete signaling molecules in vesicles, so they express neuronal markers (synaptophysin, chromogranin) and can secrete hormones.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Carcinoid heart disease links NETs to the heart: serotonin from a metastatic midgut NET reaching the systemic circulation drives fibrosis of right-sided heart valves, causing tricuspid regurgitation—so an endocrine tumor's secretions remodel cardiac valves.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Functioning NETs secrete histamine and other mediators causing distinct syndromes: gastric and some foregut NETs release histamine producing atypical flushing, complementing serotonin's carcinoid syndrome—so a NET's secretory product determines its clinical picture.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Most neuroendocrine tumors arise in the digestive system: gastroenteropancreatic NETs (carcinoids, gastrinomas, insulinomas) form from the gut's diffuse hormone-secreting cells, so the GI tract and pancreas are the commonest primary sites and the cause of carcinoid syndrome.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — NETs are uniquely treated with targeted radiation: peptide receptor radionuclide therapy attaches a radioisotope to a somatostatin analog so SSTR2-rich tumors irradiate themselves, and Ga-68 PET images them the same way—radiation guided by the tumor's own receptor.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Neuroendocrine tumors straddle the nervous and endocrine systems: they arise from cells that, like the endocrine system, secrete hormones into blood, so functional NETs cause hormone syndromes (flushing, hypoglycemia, ulcers) treated by dampening that secretion.
- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — Pancreatic neuroendocrine tumors are shaped by ATRX: loss of ATRX (or DAXX) switches on alternative lengthening of telomeres, marking tumors with distinct biology and a worse prognosis—part of why molecular profiling now guides NET management.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — The thymus is an aggressive site for neuroendocrine tumors: thymic carcinoids, often linked to MEN1 and seen in men who smoke, behave more aggressively than other carcinoids, so chest imaging is part of evaluating NET-prone patients.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Medullary thyroid carcinoma is a calcitonin-secreting neuroendocrine tumor: arising from thyroid C cells, it pours out calcitonin that serves as a sensitive tumor marker for diagnosis and monitoring—linking the NET family to a thyroid cancer.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Neuroendocrine tumors spin off fibrosis: serotonin from midgut carcinoids drives dense scarring—right-sided carcinoid heart-valve disease and mesenteric fibrosis that kinks the bowel—a distinctive complication of these slow but secretory tumors.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Carcinoid flushing is driven by mediators like bradykinin: NETs release vasoactive kinins and serotonin that dilate vessels, producing the episodic flushing, wheezing, and diarrhea of carcinoid syndrome when the liver can't clear them.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Neuroendocrine tumors hide in a cold immune niche shaped by regulatory T cells: low mutation burden and Treg-rich stroma make most NETs poorly responsive to checkpoint immunotherapy, steering treatment toward somatostatin analogs and PRRT instead.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Neuroendocrine tumors secrete hormones the way nerves fire—via calcium: like the normal neuroendocrine cells they arise from, they release hormones by calcium-triggered exocytosis, so this secretory machinery underlies the flushing and diarrhea of functional NETs.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Neuroendocrine tumors are richly vascular and oxygen-sensing: many, especially VHL-related ones, behave as pseudohypoxic and drive dense blood vessels, which is why their vascularity stands out on imaging and antiangiogenic drugs have a role.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages crowd the neuroendocrine tumor stroma: tumor-associated macrophages support its growth and blood supply within the immunosuppressive, Treg-rich niche, part of why these tumors resist checkpoint immunotherapy.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — A VIPoma drains the body's potassium: this pancreatic neuroendocrine tumor floods the gut with VIP, causing torrential watery diarrhea that wastes potassium (the WDHA syndrome), risking dangerous hypokalemia.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Neuroendocrine tumors flush the skin: carcinoid syndrome's serotonin and vasoactive peptides cause episodic flushing, and serotonin's drain on tryptophan can starve the skin of niacin, causing pellagra.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Neuroendocrine tumors are richly vascular: they recruit endothelial cells to build a dense blood supply, giving the bright tumor 'blush' on imaging that helps find these often-small lesions.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy defines what 'neuroendocrine' means: these tumor cells are stuffed with dense-core secretory granules — membrane-bound packets of hormone — the ultrastructural signature that marks a tumor as neuroendocrine when its tissue origin is unclear.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets hoard the serotonin these tumors spill: carcinoids release serotonin that circulating platelets soak up and store, so platelet-poor measurements and urinary 5-HIAA breakdown products are used to gauge the secreting tumor's activity.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Radioiodine hunts the catecholamine-avid ones: MIBG, a noradrenaline mimic tagged with iodine-123 or iodine-131, is taken up by these tumors to image them and, in higher doses, to deliver targeted radiation therapy.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Neuroendocrine tumors of the gut announce themselves with diarrhea: midgut carcinoids spill serotonin that speeds the bowel, and once they reach the liver the unfiltered hormones cause the flushing-and-diarrhea of carcinoid syndrome.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Neuroendocrine tumors favor bone when they spread: skeletal metastases to the marrow-bearing spine and pelvis are common in advanced disease, lighting up on the somatostatin-receptor scans used to stage them.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Carcinoid diarrhea drains the body's minerals: the relentless secretory diarrhea of a hormone-secreting neuroendocrine tumor flushes out magnesium and potassium, electrolytes that must be replaced alongside treating the tumor.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains define the tumor: chromogranin A and synaptophysin by immunohistochemistry confirm a lesion is neuroendocrine, and the Ki-67 antibody index grades how fast it divides — the single number that separates indolent NETs from aggressive carcinomas.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney limits the radioactive cure: peptide receptor radionuclide therapy with Lu-177 DOTATATE homes to SSTR2 but is filtered through and can injure the kidney, so amino-acid infusions are co-given to shield the tubules from the radiation dose.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Carcinoid hormones clench smooth muscle: serotonin and bradykinin from the tumor contract airway and gut smooth-muscle cells, causing the wheeze and cramping diarrhea of carcinoid syndrome that octreotide is given to quiet.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Serotonin scars the heart valves: in carcinoid heart disease the tumor's serotonin drives valvular fibroblasts to lay down fibrous plaques on the right-sided valves, stiffening them into the tricuspid and pulmonary lesions that cause right heart failure.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Tuberous sclerosis seeds neuroendocrine tumors: TSC1/TSC2 loss unleashes mTOR, predisposing to pancreatic neuroendocrine tumors — the same pathway that makes the mTOR inhibitor everolimus an effective therapy for advanced NETs.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — NETs grow along the PI3K-AKT-mTOR axis: signaling through AKT to mTOR sustains these tumors, the rationale behind everolimus and a resistance route when that drug is used, tying their biology to the broader growth-signaling network.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Some NETs run in cancer-predisposition families: neurofibromatosis type 1 raises the risk of duodenal somatostatinomas and other neuroendocrine tumors, one of several germline syndromes (with MEN1 and VHL) that seed these tumors decades early.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The stomach grows its own neuroendocrine tumors: gastric carcinoids arise from ECL cells, often driven by the high gastrin of atrophic gastritis or acid-suppressing drugs, a distinct and usually indolent NET tied to how the stomach regulates acid.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — One NET family floods the body with catecholamines: pheochromocytomas and paragangliomas pour out norepinephrine, causing the pounding hypertension and palpitations that set this secretory subtype apart from the serotonin-driven carcinoids.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Serotonin scars the right heart: in carcinoid heart disease, vasoactive amines from a metastatic midgut NET deposit fibrous plaques on the tricuspid and pulmonary valves, driving right-sided heart failure — a leading cause of death in carcinoid syndrome.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Cell-cycle control grades the tumor: CDKN2A and other cell-cycle alterations help separate indolent well-differentiated NETs from the aggressive, high-proliferation neuroendocrine carcinomas, informing grade and treatment.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The tumor and its surgery raise the clot risk: like other visceral cancers, neuroendocrine tumors and the major resections they require predispose to venous thromboembolism.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 supports the neuroendocrine clone: signaling through STAT3 backs proliferation and survival in neuroendocrine tumors, one of the pathways downstream of the mTOR and growth-factor activation that drives them.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB adds an inflammatory survival signal: neuroendocrine tumor cells engage NF-κB-dependent survival and angiogenic signaling, contributing to the growth of these often slow but persistent tumors.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Liver metastases and surgery invite infection: NETs commonly spread to the liver where biliary obstruction and tumor-debulking surgery can seed cholangitis and abdominal sepsis.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Their hormones and therapy unbalance glucose: pancreatic NETs like glucagonoma and somatostatinoma directly disturb glucose handling, and the somatostatin-analogue treatment used for most NETs suppresses insulin, together provoking diabetes.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Their radioligand therapy stresses the kidneys: peptide-receptor radionuclide therapy with lutetium-DOTATATE concentrates in the renal tubules, and the cumulative radiation can drive a slow decline into chronic kidney disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A chronic, flushing cancer wears on mood: the years-long course of metastatic NETs, the disabling diarrhea and flushing of carcinoid syndrome, and serotonin diversion away from the brain combine to raise depression risk.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Unpredictable flushing and a chronic cancer breed worry: the episodic carcinoid attacks, lifelong indolent-but-incurable course and continual imaging surveillance of NETs foster persistent health anxiety.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Resecting the tumour and its liver deposits heals slowly: surgery for primary NETs and hepatic debulking, sometimes in malnourished patients with carcinoid diarrhoea, leaves wounds prone to delayed closure.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — A smouldering tumour blunts the marrow: the chronic inflammatory state of metastatic NETs, compounded by GI blood loss from bowel primaries, produces a normocytic anemia of chronic disease.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Carcinoid shows on the skin: serotonin-secreting NETs cause the episodic flushing of carcinoid syndrome, and tryptophan diversion to serotonin depletes niacin, producing the dermatitis of pellagra.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — They grow in and squeeze the airways: bronchial carcinoids are a recognised NET, and the bronchospasm and wheeze of carcinoid syndrome are part of its vasoactive-mediator effects.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Pellagra and metastases reach the brain: the niacin deficiency of serotonin-secreting NETs causes the dementia of pellagra, and NETs can metastasise to the central nervous system.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Serotonin scars the right heart: carcinoid heart disease is a hallmark complication in which serotonin from the tumour fibroses the tricuspid and pulmonary valves, causing right heart failure.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It spreads to nodes and liver with desmoplasia: NETs metastasise to mesenteric lymph nodes, provoking a dense desmoplastic reaction that kinks the bowel, and characteristically to the liver.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It seeds the bones as dense deposits: well-differentiated neuroendocrine tumours characteristically produce osteoblastic (sclerotic) bone metastases detectable on functional imaging.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It is the model for receptor-targeted treatment: somatostatin analogues, Lu-177 DOTATATE peptide-receptor radionuclide therapy and mTOR inhibitors exploit neuroendocrine tumours' somatostatin receptors and biology.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its radionuclide therapy taxes the kidney: peptide-receptor radionuclide therapy concentrates in and can damage the kidneys, requiring amino-acid renal protection during treatment.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — They can arise in the gonads: primary neuroendocrine tumours (carcinoids) occur in the ovary and testis, and ovarian carcinoids can secrete hormones causing the carcinoid syndrome.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for pancreatic and high-grade tumours: capecitabine-temozolomide treats pancreatic neuroendocrine tumours, and platinum-etoposide treats poorly differentiated neuroendocrine carcinomas.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — Pancreatic NETs arise from these cells: insulinomas, gastrinomas and other functioning tumours of the islets of Langerhans are the pancreatic neuroendocrine tumours, secreting hormones that drive distinctive syndromes.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy for the high-grade end: poorly differentiated neuroendocrine carcinomas, like small-cell lung cancer, are treated with chemotherapy plus PD-1/PD-L1 inhibitors, while well-differentiated NETs stay immunologically cold.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — It can scar the heart valves: serotonin and vasoactive substances from metastatic carcinoid tumours deposit fibrous plaques on the right-sided endocardium and tricuspid/pulmonary valves, the carcinoid heart disease that complicates the syndrome.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — A shared somatostatin-receptor target: like meningiomas, neuroendocrine tumours strongly express somatostatin receptor 2, so both are imaged with DOTATATE PET and can be treated with peptide receptor radionuclide therapy.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — Another inherited endocrine-tumour syndrome: like MEN1, Carney complex predisposes to neuroendocrine and endocrine tumours—pituitary, thyroid and adrenal—through PRKAR1A loss, joining the familial syndromes that spawn NETs.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver metastases drive carcinoid syndrome: midgut NETs spread to the hepatic lobule, and only when their serotonin bypasses hepatic first-pass clearance—via liver metastases draining to systemic veins—do flushing and diarrhoea appear.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Medullary thyroid carcinoma is a NET: arising from calcitonin-secreting C cells and driven by RET, MTC is a neuroendocrine tumour, linking the NET family to the thyroid.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Bronchial carcinoid: a well-differentiated lung neuroendocrine tumour arises in the airway and alveolar region, the indolent end of pulmonary neuroendocrine neoplasia distinct from small-cell carcinoma.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Two pancreatic tumours, opposite outlooks: well-differentiated pancreatic neuroendocrine tumours are far more indolent and treatable than pancreatic ductal adenocarcinoma, making their distinction one of the most consequential in oncology.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Gastric carcinoids: ECL-cell neuroendocrine tumours of the stomach (types 1-2 driven by hypergastrinaemia) are a distinct entity from gastric adenocarcinoma, with different drivers, behaviour and management.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The carcinoid cell of origin: midgut carcinoids arise from enterochromaffin cells scattered through the intestinal epithelium, the serotonin-secreting source whose liver metastases produce carcinoid syndrome.
- `connects-to` → **[DLL3](../../03-molecular/dll3/README.md)** — High-grade target: DLL3 is expressed on poorly differentiated neuroendocrine carcinomas, the target of DLL3-directed agents like tarlatamab that extend beyond somatostatin-based therapy.
- `connects-to` → **[CDKN1B (p27)](../../03-molecular/cdkn1b/README.md)** — p27 gatekeeper: germline CDKN1B (p27Kip1) loss causes MEN4, an inherited pancreatic/pituitary neuroendocrine tumour syndrome, and somatic p27 loss releases the cell-cycle brake that restrains well-differentiated NET proliferation, complementing the MEN1 axis already mapped.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Syndromic co-secretion: in MEN1-associated NET the parathyroid glands hypersecrete PTH, so primary hyperparathyroidism and hypercalcaemia frequently accompany the pancreatic and pituitary neuroendocrine tumours, tying the NET syndrome to calcium-endocrine physiology.
- `connects-to` → **[SDHB](../../03-molecular/sdhb/README.md)** — Pseudohypoxic driver: SDHB loss defines a metabolic subset of neuroendocrine tumours and paragangliomas where succinate accumulation stabilises HIF (HIF-1α already mapped), driving the intense vascularity and DOTATATE avidity characteristic of these lesions.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Carcinoid heart disease: serotonin-secreting midgut neuroendocrine tumours (serotonin already mapped) cause fibrotic plaques on the right-sided heart valves, and troponin marks the myocardial strain of the resulting right heart failure.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Gastrinoma acid: gastrin-secreting neuroendocrine tumours drive massive gastric acid (proton) secretion (Zollinger-Ellison syndrome), causing refractory peptic ulceration controlled with high-dose proton-pump inhibitors.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Adrenal medullary tumours: phaeochromocytomas and paragangliomas are catecholamine-secreting neuroendocrine tumours of the adrenal medulla and sympathetic ganglia (SDHB already mapped), part of the spectrum that DOTATATE and MIBG imaging localise.
- `connects-to` → **[ACTH](../../03-molecular/acth/README.md)** — Ectopic ACTH: bronchial and pancreatic neuroendocrine tumours can secrete ACTH ectopically, driving cortisol excess and ectopic Cushing syndrome, one of the paraneoplastic hormone syndromes of the neuroendocrine tumour spectrum.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Carcinoid mediators: prostaglandins, with the serotonin, histamine and bradykinin (already mapped) released by metastatic carcinoid tumours, contribute to the flushing and diarrhoea of the carcinoid syndrome that somatostatin analogues suppress.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Flushing and vasculature: nitric oxide contributes to the vasodilatory flushing of the carcinoid syndrome and, with VEGF (already mapped), the rich vasculature of these often highly vascular neuroendocrine tumours.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment of the neuroendocrine tumours dampens the anti-tumour immune response, part of the immune biology relevant to the immunotherapy of the aggressive or metastatic tumours.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Incretin-secreting tumours: GLP-1 reflects the enteropancreatic incretin biology of the neuroendocrine tumours (insulin and glucagon already mapped), and rare GLP-1-secreting tumours cause hypoglycaemia, part of the functional-tumour spectrum.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the neuroendocrine-tumour stroma, part of its immune microenvironment.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immune microenvironment of the neuroendocrine tumours.
- `connects-to` → **[T-cytotoxic cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunotherapy: the cytotoxic T cells (PD-1 and perforin already mapped) are the target of the checkpoint immunotherapy explored in the high-grade neuroendocrine carcinomas, which the immunosuppressive stroma limits.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Islet zinc: zinc is stored with insulin (already mapped) in the islet secretory granules, and the zinc-insulin hexamer is part of the biology of the insulinomas among the pancreatic neuroendocrine tumours.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Functional-tumour metabolic adipokine: leptin reflects the metabolic disturbance of the functional (insulin and glucagon already mapped) neuroendocrine tumours and the metabolic milieu of the disease.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic disturbance of the functional neuroendocrine tumours.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic milieu of the neuroendocrine tumours.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon therapy: the type-I interferon, historically used (with the somatostatin analogues — SSTR2 already mapped) to treat the carcinoid/NET, shapes the innate-immune microenvironment of the neuroendocrine tumours.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the (limited) immune response to the neuroendocrine tumours.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the neuroendocrine-tumour immune microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the neuroendocrine tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the neuroendocrine-tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the neuroendocrine-tumour microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the neuroendocrine tumours.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the neuroendocrine tumours.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the tumour antigen to the T cells (already mapped) shaping the adaptive immune response against the neuroendocrine tumours.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the neuroendocrine tumours.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate cytotoxicity: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance within the immune microenvironment of the neuroendocrine tumours.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Tumour complement: the complement C3 activation contributes to the inflammatory dimension of the well-vascularised (VEGF already mapped) neuroendocrine tumour stroma.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypervascular tumours: HIF-1α-driven, VEGF-rich angiogenesis makes neuroendocrine tumours strikingly vascular, the rationale for anti-angiogenic agents such as sunitinib.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Grade and progression: TERT activation maintaining telomeres accompanies the progression of neuroendocrine tumours toward higher-grade, more aggressive disease.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Proliferative drive: MYC activation drives the higher proliferative rate of poorly differentiated neuroendocrine carcinomas, marking their aggressive behaviour.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle control: with CDKN2A loss in higher-grade tumours, cyclin D-CDK4/6 activity propels neuroendocrine tumour cells through the G1 checkpoint.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic progression: EZH2 overexpression contributes to the dedifferentiation and progression of neuroendocrine tumours, an epigenetic therapeutic candidate.
- `connects-to` → **[MEN1](../../03-molecular/men1/README.md)** — Menin loss: inactivation of the MEN1 tumour suppressor is the commonest genetic lesion in pancreatic neuroendocrine tumours, linking sporadic NETs to the MEN1 hereditary syndrome.
- `connects-to` → **[RET](../../03-molecular/ret/README.md)** — RET oncogene: activating RET mutations drive medullary thyroid carcinoma, the calcitonin-secreting neuroendocrine tumour of MEN2, targeted by selective RET inhibitors.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into neuroendocrine tumours, shaping a stroma that supports growth and modulates therapy response.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on neuroendocrine tumor cells follows CXCL12 gradients to the liver, the dominant metastatic site whose tumor burden drives the carcinoid syndrome and accounts for much of NET mortality.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Peptide-receptor radionuclide therapy (Lutathera) delivers SSTR2-targeted radiation that kills NET cells through DNA-damage-driven caspase-3 apoptosis, a mainstay treatment for progressive somatostatin-receptor-positive tumors.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Serotonin from carcinoid tumors drives TGF-β-mediated fibrosis, producing the desmoplastic mesenteric fibrosis and the right-sided carcinoid heart disease (plaque on the tricuspid and pulmonary valves) that complicate the syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — The DLL3-CD3 bispecific tarlatamab redirects cytotoxic T cells to kill DLL3-expressing high-grade neuroendocrine carcinomas through perforin and granzyme, an immunotherapy advance for tumors beyond somatostatin-based control.
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — Von Hippel-Lindau disease predisposes to pancreatic neuroendocrine tumors, one of several inherited syndromes—with MEN1, NF1 and tuberous sclerosis—that cause NETs and prompt germline testing in young or multifocal cases.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Pancreatic neuroendocrine tumors are shaped by chromatin and DNA-methylation changes (MEN1, DAXX/ATRX), and methylation profiling defines clinically distinct subgroups, making the epigenome central to their classification.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA drives the PI3K-AKT-mTOR pathway (AKT and mTOR already mapped) in neuroendocrine tumors, the basis for the mTOR inhibitor everolimus in their treatment.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — The Notch ligand DLL3 (mapped) is aberrantly expressed in high-grade neuroendocrine tumors, and dysregulated NOTCH signaling shapes their differentiation, with DLL3 itself a bispecific-antibody target.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D-CDK4/6 axis (cyclin-D1 and CDKN2A already mapped) releases E2F1 to drive the cell-cycle activity reflected in the Ki67 index that grades neuroendocrine tumors.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — The VEGF/PDGF angiogenic axis (VEGF already mapped) sustains the characteristically vascular neuroendocrine tumors and is the target of the multikinase inhibitor sunitinib.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss releases the PI3K-AKT-mTOR axis (AKT, PIK3CA and mTOR already mapped) that drives neuroendocrine-tumor growth and is inhibited therapeutically by everolimus.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Combined RB1 and TP53 loss distinguishes the high-grade, poorly-differentiated neuroendocrine carcinomas from well-differentiated NETs, releasing the cell-cycle checkpoint (CDKN2A and E2F1 already mapped).
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is a marker and modulator of the survival and microenvironment interactions of neuroendocrine tumors.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RAS-ERK-MAPK signaling, engaged downstream of RET and other receptor tyrosine kinases (RET mapped), provides a proliferative input to neuroendocrine tumors.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 mapped) provides a proliferative and immunomodulatory input to neuroendocrine tumors.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune microenvironment of neuroendocrine tumors, relevant to immunotherapy in the high-grade neuroendocrine carcinomas.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the differentiation and microenvironment of neuroendocrine tumors.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (cyclin-D1, CDKN2A and RB1 already mapped) drives the cell-cycle progression of neuroendocrine tumors.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-mTOR-driven FOXO inactivation (AKT, PIK3CA, and mTOR already mapped) removes a pro-apoptotic brake in neuroendocrine tumors.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and secretory-cell signaling of neuroendocrine tumors.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation restrains apoptosis in neuroendocrine tumors.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative signaling of neuroendocrine tumors.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of neuroendocrine tumors.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival of neuroendocrine tumor cells under metabolic and therapeutic stress.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of neuroendocrine tumors.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of neuroendocrine tumors.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of neuroendocrine tumors.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of neuroendocrine tumors.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of neuroendocrine tumors.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of neuroendocrine tumors.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuroendocrine stroma alarmin: TSLP from the desmoplastic NET stroma activates dendritic cells (already mapped) and mast cells (already mapped), shaping the immune microenvironment and driving the type-2 inflammatory stromal response of carcinoid and pancreatic NETs.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — NET immune surveillance: complement C5 (with C3 already mapped) drives complement-dependent cytotoxicity against NETs; C5a–C5aR1 (already mapped) recruits the myeloid infiltrate into the somatostatin-receptor-expressing carcinoid tumour stroma for immune surveillance.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Carcinoid desmoplastic stroma: periostin, downstream of TGF-β (already mapped), drives the fibrotic peritoneal carcinomatosis and cardiac fibrosis (heart already mapped) of the desmoplastic response to the carcinoid syndrome of midgut neuroendocrine tumours.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — NET complement regulation: C1-INH controls the classical-pathway arm (complement C3, C5 and C5aR1 already mapped) in the NET tumour microenvironment, modulating complement-dependent cytotoxicity against somatostatin-receptor (sstr2 already mapped) NET cells.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroendocrine EPO signalling: erythropoietin receptor (EPOR) on neuroendocrine tumour cells activates the JAK2/STAT3 (already mapped) pro-survival pathway, complementing the mTOR (already mapped) and VEGF (already mapped) signalling in NET tumour growth and treatment anaemia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Alternative complement: factor H limits alternative-pathway complement activation (complement C3, C5 and C5aR1 already mapped) in the neuroendocrine-tumour stroma, preventing excessive complement-driven inflammation and protecting the carcinoid vascular endothelium.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Carcinoid melatonin: melatonin co-secreted by enterochromaffin cells alongside serotonin (already mapped) inhibits NET proliferation through MT1/MT2 receptor-mediated cAMP suppression, counteracting the mTOR (already mapped) and VEGF (already mapped) pro-survival NET signalling.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex-hormone microenvironment: testosterone modulates the NET tumour immune microenvironment through androgen receptor signalling on tumour-infiltrating mast cells (already mapped) and macrophages (already mapped), influencing the carcinoid inflammatory cascade.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Neuroendocrine prolactin: prolactin binds prolactin receptors on NET cells to activate JAK2/STAT3 (already mapped) and mTOR (already mapped) pro-proliferative signalling; pituitary prolactinomas (hypothalamus already mapped) represent the archetype NET hypersecretion syndrome.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — NET oxytocin signalling: oxytocin receptors on enterochromaffin NETs couple to Gαq-IP3-PKC, cross-activating mTOR (already mapped) and VEGF (already mapped) pro-proliferative cascades in the carcinoid microenvironment.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — NET vasopressin secretion: NETs co-secrete vasopressin-like peptides activating V1b/V2 receptors on NET stroma, promoting angiogenesis via VEGF (already mapped) upregulation and macrophage (already mapped) recruitment.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — NET selenium redox: selenium via GPX and thioredoxin reductase suppresses ROS that stabilise HIF-1α and drive VEGF (already mapped) and mTOR (already mapped) pro-angiogenic signalling in neuroendocrine tumours.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — NET sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) neuroendocrine tumour cascade.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — NET copper: copper, as cofactor of SOD1 in macrophages (already mapped) and endothelial cells (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative tumour cascade of neuroendocrine tumours.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — NET phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and macrophages (already mapped), supports neuroendocrine tumour immune surveillance; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — NET iron: iron, via ferritin in macrophages (already mapped) and fibroblasts (already mapped), modulates redox balance in the neuroendocrine tumour microenvironment; iron dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — NET chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in the neuroendocrine TME; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of NET.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — NET sulfur: sulfur-containing amino acids in macrophages (already mapped) and fibroblasts (already mapped) maintain redox buffering; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of neuroendocrine tumors.

[^yao-2011-radiant3]: Yao JC, Shah MH, Ito T, et al. Everolimus for advanced pancreatic neuroendocrine tumors. *N Engl J Med.* 2011;364(6):514-523. [doi:10.1056/NEJMoa1009290](https://doi.org/10.1056/NEJMoa1009290) · [PubMed 21306237](https://pubmed.ncbi.nlm.nih.gov/21306237/)
[^raymond-2011-sunitinib-pnet]: Raymond E, Dahan L, Raoul JL, et al. Sunitinib malate for the treatment of pancreatic neuroendocrine tumors. *N Engl J Med.* 2011;364(6):501-513. [doi:10.1056/NEJMoa1003825](https://doi.org/10.1056/NEJMoa1003825) · [PubMed 21306236](https://pubmed.ncbi.nlm.nih.gov/21306236/)
