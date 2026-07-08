---
schema: human-scale-entry/v1
id: dicer1-syndrome
name: DICER1 Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "DICER1 syndrome is caused by germline DICER1 mutations with somatic RNase IIIb hotspot second hits; pleuropulmonary blastoma (PPB), cystic nephroma, ovarian Sertoli-Leydig cell tumors, multinodular goiter; PPB is the sentinel tumor; surveillance from infancy."
aliases: ["DICER1 syndrome", "DICER1 mutation syndrome", "familial PPB", "pleuropulmonary blastoma hereditary", "DICER1 PPB", "DICER1 cystic nephroma", "DICER1 SLCT", "DICER1 goiter", "DICER1 cancer predisposition"]
sources:
  - id: schultz-2018-dicer1-surveillance
    type: peer-reviewed
    cite: "Schultz KAP, Williams GM, Kamihara J, et al. DICER1 and Associated Conditions: Identification of At-risk Individuals and Recommended Surveillance Strategies. Clin Cancer Res. 2018;24(10):2251-2261."
    doi: "10.1158/1078-0432.CCR-17-3089"
    pmid: "29343557"
    url: "https://doi.org/10.1158/1078-0432.CCR-17-3089"
  - id: hill-2009-dicer1
    type: peer-reviewed
    cite: "Hill DA, Ivanovich J, Priest JR, et al. DICER1 mutations in familial pleuropulmonary blastoma. Science. 2009;325(5943):965."
    doi: "10.1126/science.1174334"
    pmid: "19556464"
    url: "https://doi.org/10.1126/science.1174334"
cross_links:
  - target: 01-human/03-molecular/dicer1
    relation: connects-to
    note: "DICER1 RNase IIIb hotspot mutations selectively deplete 5p miRNAs (let-7-5p, miR-17-5p family) → derepression of oncoproteins; germline LOF + somatic hotspot = two-hit mechanism; pathogenic hotspot residues E1705, D1709, E1813, D1810 cluster in metal-binding motif of RNase IIIb."
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "MYCN amplification is the most common cooperating somatic event in PPB type III (solid, high-grade); DICER1 5p miRNA loss → let-7/miR-17 family derepression → MYCN upregulation → RB bypass; PPB type III with MYCN amplification has ~53% 5-year OS."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Cervical embryonal rhabdomyosarcoma (ERMS) is a rare but sentinel DICER1 syndrome tumor; DICER1 hotspot mutations found in ~20% of cervical ERMS; DICER1 syndrome RMS is distinct from sporadic RMS; conservative surgery preferred in pediatric cervical ERMS."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Ovarian Sertoli-Leydig cell tumors (SLCT) are the most common ovarian manifestation of DICER1 syndrome; DICER1 hotspot mutations drive ~60% of all SLCT; DICER1 germline carriers: pelvic US surveillance from age 8; BEP chemotherapy for advanced/recurrent SLCT."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Let-7 miRNA family (depleted by DICER1 RNase IIIb hotspot) is the primary KRAS 3'UTR suppressor; DICER1 hotspot → let-7-5p loss → KRAS mRNA derepression → constitutive RAS-MAPK; KRAS upregulated in PPB via this axis; KRAS can be oncogenic without mutation when let-7 is depleted."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "DICER1 syndrome carriers have elevated DTC risk; DICER1 somatic hotspot mutations in ~10-15% of follicular and poorly differentiated thyroid carcinoma; thyroid US surveillance from age 8 in DICER1 carriers; DICER1-mutant thyroid cancer often arises in multinodular goiter."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "DICER1 hotspot mutations found in ~5% of Wilms tumor; cystic nephroma (benign DICER1 renal tumor) can contain Wilms-like blastemal elements (partially differentiated nephroblastoma); renal US surveillance in DICER1 carriers aged 0-8 detects cystic nephroma before transformation."
  - target: 01-human/07-system/bloom-syndrome
    relation: connects-to
    note: "DICER1 and Bloom are both childhood cancer-predisposition syndromes but mechanistically distinct: DICER1 is faulty microRNA processing (RNase IIIb hotspots depleting 5p miRNAs), Bloom genomic instability from a defective BLM helicase — gene dysregulation versus broken DNA repair."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pleuropulmonary blastoma is the sentinel DICER1 tumor: a rare embryonal lung cancer that begins as benign cystic lesions (type I) in infancy and can progress to solid high-grade sarcoma (type III); resecting it early is why chest imaging surveillance starts in the newborn period."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is a key DICER1 site: cystic nephroma, a benign multilocular renal cyst, can harbor Wilms-like blastemal elements and rarely progress to anaplastic sarcoma; renal ultrasound surveillance from birth to age 8 catches these before transformation."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "DICER1 syndrome reaches the CNS: germline DICER1 loss predisposes to pineoblastoma and a distinct DICER1-mutant embryonal brain tumor that overlaps morphologically with medulloblastoma—so miRNA-processing failure, not just SHH/WNT, can drive childhood embryonal CNS cancer."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "DICER1 and Li-Fraumeni are major inherited pediatric cancer-predisposition syndromes with overlapping tumors (rhabdomyosarcoma, CNS embryonal tumors) but distinct mechanisms: DICER1 disrupts microRNA processing, Li-Fraumeni loses TP53 function—both warrant surveillance."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "The lung epithelium is the cradle of DICER1's signature tumor: pleuropulmonary blastoma arises in the developing lung where DICER1 loss in the airway/alveolar epithelium (including type II pneumocytes) drives cystic then sarcomatous change, the childhood hallmark of the syndrome."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "DICER1 syndrome and retinoblastoma are inherited pediatric cancer-predisposition syndromes: DICER1 disrupts microRNA processing to cause pleuropulmonary blastoma and embryonal tumors, while RB1 loss causes retinoblastoma—both needing childhood surveillance."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "DICER1 syndrome and rhabdoid tumor predisposition both cause aggressive embryonal childhood tumors: DICER1 (microRNA processing) yields pleuropulmonary blastoma and CNS tumors, while SMARCB1 loss yields ATRT—overlapping in the infant brain-tumor differential."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "DICER1 syndrome causes a rare HPV-independent cervical cancer: embryonal rhabdomyosarcoma (sarcoma botryoides) of the cervix arises from germline DICER1 loss in young women, a distinctive non-carcinoma cervical tumor that, unlike typical cervical cancer, is unrelated to HPV."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid is a hallmark DICER1 target: carriers develop multinodular goiter and differentiated thyroid cancer at high rates, often after chemotherapy for other DICER1 tumors—so thyroid surveillance is central to managing the syndrome."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "DICER1 tumors are often mesenchymal blastomas with fibroblast-like sarcomatous cells: impaired microRNA processing drives pleuropulmonary blastoma and rhabdomyosarcoma-like growths of primitive spindle cells—unlike the epithelial cancers of most syndromes."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "DICER1 and p53 can cooperate in tumor formation: loss of microRNA maturation deregulates growth genes, and concurrent TP53 mutation accelerates malignant DICER1 tumors—so the miRNA machinery joins the classic tumor-suppressor network in controlling cancer."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "DICER1 syndrome strikes the reproductive system: it causes ovarian Sertoli-Leydig cell tumors that can virilize, plus other gonadal tumors, so a young woman with such a tumor warrants DICER1 testing and broader cancer surveillance."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "DICER1 syndrome reaches multiple endocrine glands: beyond thyroid disease it causes pituitary blastoma in infants and rare adrenal and pineal tumors, so its microRNA-processing defect disrupts hormone-producing tissues across the endocrine system."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "DICER1 syndrome affects the eye: ciliary body medulloepithelioma, a rare childhood intraocular tumor, is part of its spectrum, so an unusual eye tumor in a child can be the presenting clue to this pleiotropic tumor-predisposition syndrome."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "DICER1 syndrome seeds tumors in the brain: pineoblastoma and pituitary blastoma are characteristic CNS tumors, so unusual childhood brain tumors—especially with other DICER1 features—prompt testing for this microRNA-processing gene defect."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "DICER1's pituitary blastoma floods the body with cortisol: this rare infant tumor secretes ACTH, causing Cushing's disease in babies, so early-life Cushing's is a red flag for a DICER1 mutation behind the pituitary tumor."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "DICER1 carriers warrant caution with radiation: as in other tumor-predisposition syndromes, radiotherapy's DNA-damaging photons may raise the lifetime risk of second cancers, so treatment plans weigh radiation exposure carefully against benefit."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "DICER1 syndrome can flood a young woman with testosterone: its Sertoli-Leydig cell ovarian tumors secrete androgens, causing virilization—deepening voice, hair growth, and missed periods—a striking clue that points toward testing for the syndrome."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "DICER1's most common sign is in the iodine-trapping thyroid: it drives multinodular goiter and raises thyroid cancer risk, so the gland that concentrates iodine to make hormone overgrows into nodules that warrant lifelong ultrasound screening."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "DICER1 governs how neurons mature through microRNA: the gene's miRNA-processing job lets neural progenitors differentiate, so when it fails immature neuron-like cells can persist and seed the rare embryonal brain tumors of the syndrome."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "DICER1 tumors lean on mTOR growth signaling: the embryonal and sarcomatous tumors of the syndrome activate this pathway to fuel proliferation, making mTOR inhibition a strategy explored across its diverse childhood cancers."
  - target: 01-human/03-molecular/wt1
    relation: connects-to
    note: "DICER1 syndrome raises the risk of Wilms tumor, the cancer of the WT1 gene: though it strikes the kidney by a different route—failed microRNA processing rather than WT1 loss—it adds nephroblastoma to the syndrome's tumor spectrum."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages populate DICER1's tumors: in the pleuropulmonary blastomas and sarcomas of the syndrome they infiltrate the stroma and secrete growth and angiogenic factors, shaping the microenvironment of these embryonal cancers."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "DICER1's cystic lung tumors can burst into the chest: type I pleuropulmonary blastoma forms air-filled cysts that rupture, spilling air—mostly nitrogen—into the pleural space and collapsing the lung (pneumothorax)."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "DICER1's embryonal tumors build new vessels: endothelial cells form the dense vasculature that supplies the fast-growing pleuropulmonary blastomas and sarcomas, a feature anti-angiogenic drugs aim to cut off."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "DICER1 syndrome reaches the pancreas: rare pancreatoblastoma, a childhood pancreatic cancer, is part of its broad tumor spectrum, extending the syndrome's microRNA-driven risk to yet another organ."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "DICER1's signature tumor grows in the lung's air spaces: pleuropulmonary blastoma starts as benign-looking cysts in the alveolar regions of young children that can degenerate into aggressive sarcoma."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Losing DICER1 unleashes growth signals: without mature let-7 microRNAs to restrain them, IGF and other growth factors run high, helping drive the overgrowth and tumors of the syndrome."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "DICER1's ovarian Sertoli-Leydig tumors are hormonally active: they secrete sex steroids, so virilization or disrupted estrogen balance is often the first clue in a young woman."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals DICER1's signature tumor: pleuropulmonary blastoma forms cysts lined by primitive blastemal cells with scattered rhabdomyoblasts, the embryonal ultrastructure of a cancer of early childhood."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "DICER1's reach includes the liver: hepatoblastoma and other hepatic tumors fall within its broad spectrum, so the liver joins the long list of organs watched in children carrying the mutation."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut can sprout DICER1 growths too: juvenile-type intestinal polyps are part of the syndrome's varied tumor predisposition, adding the bowel to its head-to-pelvis surveillance."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "DICER1 can wreck an infant's hormones: its pituitary blastoma oversecretes ACTH, driving the adrenal glands into a florid Cushing syndrome in babies — a rare but striking endocrine face of the cancer predisposition."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "DICER1 seeds the female genital tract with sarcoma: embryonal rhabdomyosarcoma (botryoides) sprouts in the cervix and uterus, growing within the muscular wall as a grape-like mass that bleeds."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Treating its childhood cancers empties the marrow: the multi-agent chemotherapy for pleuropulmonary blastoma and the other DICER1 tumors drops neutrophils into febrile neutropenia, a constant hazard of the regimens."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immune surveillance shapes who gets cancer: most DICER1 carriers stay tumor-free despite the germline hit, and cytotoxic T cells policing the many tissues at risk are part of that defense — a rationale for exploring immunotherapy in DICER1 tumors."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "DICER1 tumors learn to suppress the attack: like other cancers they can recruit regulatory T cells that damp local immunity, helping the second-hit clone grow past the cytotoxic defenses that hold most carriers' tissues in check."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Its tumors can bleed and drain the blood: large pleuropulmonary blastomas and the kidney and gynecologic tumors of DICER1 cause chronic blood loss and anemia of malignancy, leaving children pale and tired before treatment even begins."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Its embryonal tumors are richly vascular: with normal microRNA control lost, angiogenic signals like VEGF run unchecked, feeding the rapid growth of pleuropulmonary blastoma and the other DICER1 tumors."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "DICER1 reaches the uterus and cervix: it causes embryonal rhabdomyosarcoma of the gynecologic tract, so a young woman's unusual cervical or uterine tumor can be the clue that points to the germline syndrome."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate immunity guards the second hit: natural killer cells help cull the genomically deranged cells of DICER1 tumors, and harnessing them is part of the immunotherapy interest in these pediatric cancers."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The lung is DICER1's signature target: pleuropulmonary blastoma, the syndrome's hallmark tumor, begins as benign lung cysts in early childhood that can transform into an aggressive sarcoma, so detecting cystic lung disease is central to surveillance."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "DICER1 doubles as a broader tumor suppressor: beyond the inherited syndrome, reduced DICER1 and disrupted microRNA biogenesis are seen in aggressive sporadic neuroblastoma, where loss of mature miRNAs lets oncogenic programs run."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Losing DICER1 derepresses developmental signals: the mature microRNAs it generates normally restrain pathways like Notch, so impaired miRNA processing in DICER1 tumors unleashes the oncogenic signaling that drives embryonal growth."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Lost microRNA control lifts the brake on STAT3: DICER1-deficient cells lose mature miRNAs that normally restrain growth pathways, derepressing signaling including STAT3 that helps drive its embryonal tumors."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its kidney tumors cost nephrons: cystic nephroma and anaplastic sarcoma of the kidney are DICER1 tumors that require nephron-sparing surgery or nephrectomy, so cumulative renal loss can reduce kidney function over time."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Treating its childhood tumors invites infection: the chemotherapy used against pleuropulmonary blastoma and other DICER1 cancers causes neutropenia, making febrile neutropenia and sepsis a treatment hazard in affected children."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Its tumors and their chemo blunt the marrow: the malignancies of DICER1 syndrome and the myelosuppressive chemotherapy they require depress erythropoiesis, adding an anemia-of-chronic-disease component to treatment cytopenias."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Cancer and its surgery raise the clot risk: the tumors of DICER1 syndrome and the operations and central lines used to treat them predispose to venous thromboembolism, as in other childhood cancers."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Lifelong tumor surveillance weighs on families and patients: living with an inherited predisposition to multiple childhood and adult tumors, and the repeated screening it demands, carries a real psychological burden."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Treating its tumors strains the heart: the anthracycline and alkylator chemotherapy for the sarcomas and blastomas DICER1 predisposes to is cardiotoxic, risking cardiomyopathy and heart failure in survivors."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its cancer chemotherapy opens the lung to mold: the neutropenia from treating DICER1-related tumors such as pleuropulmonary blastoma can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Constant multi-organ surveillance breeds worry: the lifelong screening for the many tumors of DICER1 syndrome, often beginning in childhood, fosters chronic health anxiety in patients and families."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It seeds tumours in the kidney: DICER1 syndrome causes cystic nephroma and, less often, renal sarcoma and Wilms-like tumours, part of its broad childhood-tumour spectrum."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Resecting its tumours means many wounds: surgery for pleuropulmonary blastoma, cystic nephroma, ovarian and other DICER1 tumours leaves children with operative wounds that must heal."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Chemotherapy reawakens shingles: the chemotherapy used against DICER1-related cancers suppresses a child's immunity, allowing latent or primary varicella-zoster to cause severe disease."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It seeds rare brain tumours: DICER1 predisposes to pineoblastoma and pituitary blastoma and other unusual childhood central-nervous-system tumours, warranting neurological surveillance."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It arises in cartilage and soft tissue: nasal chondromesenchymal hamartoma and the embryonal rhabdomyosarcomas of the DICER1 spectrum develop in cartilage and skeletal muscle."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its chemotherapy can scar the heart: anthracyclines used against DICER1-related cancers carry a long-term cardiotoxicity risk in the children who receive them."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It can sprout polyps in the gut: DICER1 syndrome is reported to cause gastrointestinal juvenile-type polyps and rare hepatic and pancreatic tumours among its diverse lesions."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "A fellow medulloblastoma predisposition: like Gorlin syndrome, DICER1 syndrome raises childhood brain-tumour risk, the two entering the differential of inherited medulloblastoma (pineoblastoma)."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Shared thyroid-cancer risk: DICER1 and Cowden syndrome both predispose to thyroid nodules and cancer from childhood, placing both in thyroid-surveillance guidance for inherited disease."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo treats its embryonal tumours: pleuropulmonary blastoma and other DICER1 sarcomas are treated with intensive multi-agent, often sarcoma-type, chemotherapy after surgery."
  - target: 01-human/07-system/birt-hogg-dube-syndrome
    relation: connects-to
    note: "Two inherited causes of lung cysts: like Birt-Hogg-Dubé, DICER1 syndrome produces familial cystic lung disease, though DICER1's cysts can transform into pleuropulmonary blastoma, demanding early surveillance."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "A fellow paediatric sarcoma: DICER1-related sarcomas join Ewing sarcoma among aggressive childhood sarcomas treated with multimodal therapy, entering each other's pathological differential."
  - target: 01-human/05-tissue/lung-slice
    relation: connects-to
    note: "Its hallmark tumour is cystic lung: pleuropulmonary blastoma begins as benign air-filled lung cysts in early childhood that can transform into an aggressive sarcoma, so cystic change on a lung slice triggers DICER1 surveillance."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Beyond chemotherapy: anti-angiogenic and other targeted agents are explored for the diverse DICER1 sarcomas, and the syndrome's miRNA-processing defect is itself a focus of emerging precision approaches."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Inherited multi-endocrine tumour cousins: like Carney complex, DICER1 syndrome predisposes to a spread of endocrine tumours — thyroid carcinoma and ovarian Sertoli-Leydig tumours — under germline control demanding glandular surveillance."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Renal tumours of childhood: DICER1 causes cystic nephroma and a subset of Wilms tumours, developmental kidney tumours arising in the nephron near the glomerulus."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Shared ovarian sex-cord tumours: DICER1's Sertoli-Leydig tumours and the sex-cord tumours with annular tubules of Peutz-Jeghers both arise in the ovary, two germline syndromes converging on this rare tumour family."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "A different kind of ovarian cancer: DICER1 drives sex-cord-stromal ovarian tumours of the young, biologically distinct from the BRCA-driven epithelial ovarian cancer of hereditary breast-ovarian syndrome."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Childhood kidney tumours: DICER1 syndrome causes cystic nephroma and anaplastic sarcoma of the kidney, paediatric renal tumours distinct from the clear cell renal carcinoma of adults."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Pituitary blastoma: DICER1 syndrome causes infantile pituitary blastoma, an ACTH-secreting neuroendocrine tumour driving Cushing disease, part of its broad neuroendocrine spectrum."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "A mesenchymal-tumour spectrum: beyond embryonal rhabdomyosarcoma, DICER1 syndrome can produce other sarcomas including rare osteosarcoma, reflecting its broad predisposition to mesenchymal tumours."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Let-7 brake released: DICER1 mutations impair processing of let-7 family microRNAs, derepressing oncogenes like MYC that these microRNAs normally restrain—a core mechanism of DICER1 tumours."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-mTOR activation: PIK3CA-driven PI3K signalling feeds the mTOR pathway active in DICER1-associated tumours, offering a targetable axis alongside the primary microRNA defect."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Malignant progression: TERT activation enabling replicative immortality marks the shift of DICER1 lesions from low-grade cystic tumours toward aggressive sarcomatous malignancy."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: loss of let-7 microRNA control from DICER1 dysfunction derepresses cyclin D and the cell-cycle machinery, accelerating proliferation in DICER1-associated tumours."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in growing DICER1-associated tumours such as pleuropulmonary blastoma drives the VEGF angiogenesis that supports their expansion."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic dysregulation: disrupted microRNA processing in DICER1 syndrome derepresses EZH2 and other chromatin regulators, contributing to the embryonal tumour phenotype."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Sex-cord stromal tumours: the activin-inhibin axis of gonadal stromal cells underlies the Sertoli-Leydig cell tumours of DICER1 syndrome, whose inhibin secretion serves as a tumour biomarker."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid neoplasia: DICER1 syndrome predisposes to multinodular goitre and differentiated thyroid carcinoma, one of the most common and earliest manifestations of the disorder."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival signalling: PI3K-AKT activation cooperates with the microRNA-processing defect of DICER1 syndrome to support the growth and survival of its diverse embryonal and stromal tumours."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Pineoblastoma: DICER1 syndrome predisposes to pineoblastoma, an aggressive RB-pathway-driven embryonal brain tumour that joins pleuropulmonary blastoma in the syndrome's intracranial tumour spectrum."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Embryonal proliferation: loss of DICER1-processed microRNAs derepresses growth-factor pathways including FGFR signalling, driving the proliferation of the embryonal tumours such as pleuropulmonary blastoma."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Tumour progression: CDKN2A loss accompanies the progression of pleuropulmonary blastoma from the early cystic type I to the solid, sarcomatous type III, a key step in the malignant evolution of DICER1 tumours."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Sex-cord tumours: DICER1 causes ovarian Sertoli-Leydig cell tumours that secrete androgens, producing the virilisation — hirsutism, deepening voice — that often brings these young patients to attention and declares the syndrome."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: the embryonal tumours of DICER1 syndrome, especially pleuropulmonary blastoma, are treated with intensive chemotherapy that kills cells through caspase-3-mediated apoptosis, the effector step underlying treatment response."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Developmental signalling: loss of DICER1-dependent microRNA regulation derepresses developmental pathways including Wnt/β-catenin in the embryonal DICER1 tumours, reflecting their origin in dysregulated organ development."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK proliferation: KRAS and FGFR (both already mapped) drive the MAPK-ERK cascade in DICER1-associated tumours such as pleuropulmonary blastoma and Sertoli-Leydig cell tumours."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K restraint: PTEN normally limits the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped) that is co-activated in DICER1 tumours to support their growth."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle derepression: loss of DICER1-dependent microRNA control over cell-cycle genes, alongside the RB-CDKN2A-cyclin-D1 axis already mapped, releases E2F1 to drive proliferation in embryonal DICER1 tumours."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Gonadal-stromal tumours: TGF-β/activin-superfamily signalling (activin-A already mapped) shapes the Sertoli-Leydig and other gonadal-stromal tumours characteristic of DICER1 syndrome."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Germ-cell signalling: KIT receptor-tyrosine-kinase signalling contributes to the embryonal and germ-cell-related tumours that arise in DICER1 syndrome."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis evasion: anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), supporting the survival of the diverse embryonal tumours of DICER1 syndrome."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is a marker of the thyroid neoplasia that is a hallmark of DICER1 syndrome and modulates tumour-cell behaviour."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β/activin-SMAD signalling (TGF-β and activin-A mapped) shapes the gonadal-stromal and embryonal tumours of DICER1 syndrome."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT3 signalling (STAT3 mapped) provides a proliferative input across the diverse tumours of DICER1 syndrome."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune surveillance of the diverse neoplasms that arise in DICER1 syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the immune microenvironment of the DICER1-driven tumours."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate the metabolic and oxidative stress of the proliferating cells of DICER1-syndrome tumours, downstream of the disrupted miRNA programme."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D-RB axis (cyclin-D1 and RB1 already mapped) drives the proliferation of DICER1-syndrome tumors."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in DICER1-syndrome tumors."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is the immune clearance that the multiple DICER1-associated tumors must evade."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the Wnt/β-catenin and survival signaling (Wnt already mapped) of the tumors of DICER1 syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation, alongside the miRNA-processing defect of DICER1 loss, contributes to the epigenetic dysregulation of DICER1 syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of the tumors of DICER1 syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the tumors of DICER1 syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and stress management of the tumors of DICER1 syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of DICER1 syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of DICER1 syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the neoplasms of DICER1 syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of DICER1 syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of DICER1 syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of DICER1 syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of DICER1 syndrome."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunosurveillance: MHC class II-restricted T-cell surveillance influences which of the diverse embryonal and stromal tumours of DICER1 syndrome progress, and antigen presentation is relevant to immunotherapy of the aggressive ones such as pleuropulmonary blastoma."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell expansion: IL-2-driven T-cell proliferation supports the adaptive immune responses and cellular immunotherapy approaches being considered for the childhood cancers of DICER1 syndrome (perforin already mapped)."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint context: PD-1-mediated exhaustion limits anti-tumour immunity, and checkpoint blockade is explored for the rare high-risk DICER1-associated cancers that recur or metastasise."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Chemotherapy anaemia: the intensive chemotherapy for the childhood cancers of DICER1 syndrome, such as pleuropulmonary blastoma and embryonal rhabdomyosarcoma (already mapped), is myelosuppressive and lowers haemoglobin."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: anthracyclines in the sarcoma regimens for DICER1-associated tumours are cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury threatening these young survivors."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis and oxidative stress: the high proliferative rate of the embryonal DICER1 tumours, lysed by chemotherapy, releases purines catabolised by xanthine oxidase to uric acid, contributing to tumour-lysis risk and oxidative stress."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment of the DICER1-associated tumours dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune evasion relevant to immunotherapy of any aggressive tumour."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the DICER1-associated embryonal tumours, part of their stromal microenvironment."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Transfusion and anaemia: the anaemia of the DICER1 sarcomas and their intensive chemotherapy (haemoglobin already mapped) requires transfusion support, whose repeated use can load the young survivor with iron."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the DICER1-associated embryonal tumours."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of the DICER1 sarcomas."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton radiotherapy: proton-beam radiotherapy treats the DICER1-associated sarcomas while sparing the developing tissues of the young child, though radiation is used cautiously given the germline tumour predisposition."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Cystic nephroma: the cystic nephroma (and the anaplastic sarcoma) of the kidney (WT1 already mapped) is a characteristic DICER1 renal tumour of childhood."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Ciliary-body medulloepithelioma: the intraocular ciliary-body medulloepithelioma of the eye is a rare but characteristic tumour of the DICER1 syndrome spectrum."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Pineoblastoma and CNS tumours: the pineoblastoma and the CNS sarcomas of the brain are part of the DICER1 tumour spectrum, reflecting the germline miRNA-processing (DICER1 already mapped) defect."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Multinodular goitre: the thyroid gland develops the multinodular goitre (thyroid-hormones already mapped) and the differentiated thyroid cancer of the DICER1 syndrome, especially after chemotherapy/RT."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Sertoli-Leydig tumour: the ovarian Sertoli-Leydig cell tumour (the androgen — androgen-receptor already mapped — secreting sex-cord-stromal tumour) is a characteristic DICER1 ovarian tumour."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "Renal-tumour differential: the DICER1 renal tumours (the cystic nephroma, the anaplastic sarcoma — WT1 already mapped) are in the differential of the Wilms tumour."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity relevant to the diverse DICER1 tumours (checkpoint PD-1 already mapped)."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the DICER1-syndrome tumours."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the DICER1-syndrome tumours."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the DICER1-syndrome tumours."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 arm: IL-17A drives the Th17 arm of the inflammatory dimension of the immune microenvironment of the DICER1-syndrome tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 induction: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the DICER1-syndrome tumour microenvironment."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the DICER1-syndrome tumours."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the immune microenvironment of the DICER1-syndrome tumours."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the DICER1-syndrome tumour stroma."
---

# DICER1 Syndrome

## Overview

**DICER1 syndrome** (also called **familial pleuropulmonary blastoma** or **DICER1-related tumor predisposition**) is an autosomal dominant hereditary tumor predisposition syndrome caused by germline pathogenic variants in the **DICER1** gene encoding the microRNA-processing enzyme Dicer. DICER1 syndrome is characterized by a predisposition to a spectrum of predominantly **pediatric and adolescent tumors**, most notably **pleuropulmonary blastoma (PPB)** — a rare intrathoracic malignancy that is the sentinel/index tumor for the syndrome — as well as **cystic nephroma**, **ovarian Sertoli-Leydig cell tumors (SLCT)**, **multinodular goiter**, **cervical embryonal rhabdomyosarcoma**, and **pituitary blastoma** among others. DICER1 syndrome tumors have a distinctive two-hit molecular mechanism: the somatic second hit is not a second loss-of-function mutation but a **hotspot missense mutation** in the RNase IIIb domain of DICER1 that selectively impairs processing of miRNA-5p family members. The syndrome was genetically defined by Hill et al. in 2009, with comprehensive clinical guidelines subsequently developed by Schultz et al. in 2018 [^hill-2009-dicer1] [^schultz-2018-dicer1-surveillance].

**DICER1 syndrome tumor spectrum:**

| Tumor | Median age | Lifetime risk in carriers | Key features |
|---|---|---|---|
| Pleuropulmonary blastoma (PPB) | 2-4 years | ~5% (type I-III combined) | Type I (cystic) → type II → type III (solid); lung/pleura |
| Cystic nephroma | 2-4 years | ~2% | Benign cystic renal tumor; female predominance |
| Ovarian SLCT | 15-25 years | ~3-5% (females) | Androgenic; hotspot somatic in ~60% of all SLCT |
| Multinodular goiter | Any age | ~75% (lifetime) | Usually benign; DTC risk modestly elevated |
| Cervical embryonal RMS | 5-20 years | <1% | Rare; botryoid pattern; conservative surgery |
| Pituitary blastoma | <2 years | Very rare | Infancy onset; ACTH excess |
| Ciliary body medulloepithelioma | <10 years | Very rare | Intraocular; locally invasive |
| Nasal chondromesenchymal hamartoma | Infancy | Very rare | Benign; nasal obstruction |

## Structure

### Genetic basis of DICER1 syndrome

**DICER1 gene (14q32.13):**
- 1922 aa; 218 kDa; ubiquitously expressed; essential for embryonic development and tissue homeostasis
- Germline pathogenic variant spectrum: frameshift, nonsense, splice site (~70%); missense in non-RNase IIIb domains (~15%); large deletions (~5%); some germline missense variants in RNase IIIb (these may function differently from somatic hotspot variants)
- Penetrance: variable; **5-10%** of DICER1 carriers develop PPB by age 8; most carriers never develop cancer; some develop only multinodular goiter (very high penetrance); incomplete and sex-specific (SLCT only in females)
- De novo germline: ~10-15% of DICER1 pathogenic variants arise de novo (no family history)
- **Autosomal dominant inheritance**: 50% offspring risk; families may appear to have only one affected individual because PPB is rare and penetrance is incomplete for most tumor types

**Somatic second-hit hotspot mechanism:**

DICER1 somatic hotspot mutations cluster in the RNase IIIb metal-binding residues:
- **E1705** (Glu1705): changed to K, D, G, Q — most common hotspot
- **D1709** (Asp1709): changed to N, G, V
- **E1813** (Glu1813): changed to K, D, G
- **D1810** (Asp1810): changed to V, N

All hotspot substitutions eliminate Mg²⁺ chelation in the RNase IIIb active site → 5p arm cleavage fails → pre-miRNA is cleaved on the 3p arm only (by RNase IIIa, which is intact) → only miRNA-3p strands are produced; miRNA-5p strands accumulate as unprocessed hairpin or are degraded

Downstream consequence:
- let-7-5p family depletion → KRAS, NRAS, LIN28A/B, MYCN, IGF2BP1 derepression → cell cycle entry
- miR-200-5p family depletion → ZEB1/ZEB2 derepression → mesenchymal phenotype → PPB stromal component
- miR-17-5p (oncomiR cluster) — paradoxically depleted by RNase IIIb hotspot despite being oncogenic when overexpressed; indicates complex miRNA network rewiring

## Function

### Pleuropulmonary blastoma (PPB)

PPB is the **defining sentinel tumor** of DICER1 syndrome. It is the most common primary malignant lung tumor of childhood and virtually always associated with DICER1 mutations (germline ± somatic):

**PPB type classification (Dehner):**
- **Type I (cystic)**: Pure multilocular cystic lesion; thin-walled cysts; grossly resembles congenital pulmonary airway malformation (CPAM/CCAM); malignant cells are a minor camouflaged subepithelial population (subepithelial cambium layer of malignant cells beneath bland epithelium); median age 7 months; 5-year OS ~90%; surgical resection curative if complete
- **Type Ir (regressed/spontaneously resolved cystic)**: Cyst that has involuted; no residual malignant cells; recognized retrospectively; may represent spontaneous regression of type I PPB
- **Type II (cystic-solid)**: Mixed cystic and solid components; overt malignant stroma (blastomatous, sarcomatous, rhabdoid); median age 30 months; 5-year OS ~71%; treatment: surgery + chemotherapy (vincristine-actinomycin D-cyclophosphamide or IVADo regimen)
- **Type III (solid)**: Purely solid, high-grade blastematous/sarcomatous mass; MYCN amplification common; median age 44 months; 5-year OS ~53%; treatment: surgery + aggressive chemotherapy ± consolidation

**PPB and DICER1 genetics:**
- >98% of PPB harbor DICER1 mutations (most: germline LOF + somatic hotspot); rare PPB with only somatic DICER1 hotspot (no germline); even rarer PPB without DICER1 mutations
- PPB mimics: type I PPB can be mistaken for CPAM/CCAM on imaging and even pathology; re-review of lung cysts in children → significant fraction reclassified as PPB type I; key distinction: subepithelial primitive cells in PPB type I vs mature smooth muscle lining in CPAM

**PPB chemotherapy regimens:**
- **Type I**: Complete surgical resection ± observation; chemotherapy not universally required after R0 resection; ongoing debate
- **Type II/III**: Post-resection chemotherapy: IVADo (ifosfamide-vincristine-actinomycin D-doxorubicin) or VAC (vincristine-actinomycin D-cyclophosphamide)-based; high-dose chemotherapy with autologous stem cell rescue in relapsed/refractory type III

### Ovarian Sertoli-Leydig cell tumors (SLCT)

SLCT is the most common ovarian tumor associated with DICER1:
- **Well-differentiated SLCT**: low malignant potential; primary oophorectomy often curative; uncommon
- **Intermediate/poorly differentiated SLCT**: androgenic virilization (hirsutism, clitoromegaly, amenorrhea); stage I at diagnosis ~80%; unilateral; treatment: fertility-sparing surgery (unilateral oophorectomy) if stage I + young patient; systemic chemotherapy (BEP) for advanced stage (II-IV) or recurrence
- DICER1 hotspot mutations: in ~60% of all SLCT regardless of germline status; also seen in gynandroblastomas (mixed SLCT)

### Multinodular goiter (DICER1-related)

- Present in the majority of adult DICER1 carriers (~75%); often the only clinical manifestation
- Histology: multinodular, hyperplastic, often with colloid-filled follicles; distinct from PTEN-related thyroid pathology (Cowden syndrome) which shows follicular adenoma
- Differentiated thyroid cancer: modestly elevated; surveillance with thyroid ultrasound annually from age 8

## Pathology

### Surveillance and management guidelines

**Surveillance by age (Schultz 2018 guidelines):**

**Birth to 8 years (PPB risk window):**
- Annual chest CT or MRI (for PPB detection)
- Abdominal/pelvic ultrasound (for cystic nephroma); frequency may be reduced after age 4
- Physical examination every 6-12 months

**Age 8 onward:**
- Annual thyroid ultrasound (for goiter/DTC surveillance)
- Annual pelvic ultrasound in females (for SLCT surveillance from age 8-40)
- Head/neck MRI every 3 years (for rare tumors: pituitary blastoma, DICER1-related SNUC/nasal tumors)

**At-risk individuals (family members of DICER1 germline carriers):**
- Germline DICER1 testing recommended for all first-degree relatives
- If positive: initiate surveillance protocol above
- Cascade genetic testing: 50% risk per first-degree relative

**Genetic counseling:**
- DICER1 syndrome is autosomal dominant; 50% offspring risk
- Prenatal testing/preimplantation genetic testing available
- Most DICER1 carriers have an excellent prognosis; morbidity and mortality concentrated in PPB (especially type III) and relapsed SLCT
- Incidental DICER1 variants of uncertain significance (VUS): challenge in interpretation; functional assays in development

**Differential diagnosis of childhood thoracic cysts:**

When a child is found to have a thoracic cystic lesion, DICER1 syndrome should be considered:
- CPAM/CCAM (congenital pulmonary airway malformation): histologically mature smooth muscle lining; no subepithelial primitive cells; no DICER1 mutation
- PPB type I: malignant subepithelial cells; DICER1 mutations present; subtle but critical distinction
- Key diagnostic approach: any thoracic cyst in a child <8 years → pathological review by expert PPB pathologist + DICER1 testing of tumor and germline

## Connections

- `connects-to` → **[DICER1](../../03-molecular/dicer1/README.md)** — DICER1 RNase IIIb hotspot mutations selectively deplete 5p miRNAs (let-7-5p, miR-17-5p family) → derepression of oncoproteins; germline LOF + somatic hotspot = two-hit mechanism; pathogenic hotspot residues E1705, D1709, E1813, D1810 cluster in metal-binding motif of RNase IIIb.
- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — MYCN amplification is the most common cooperating somatic event in PPB type III (solid, high-grade); DICER1 5p miRNA loss → let-7/miR-17 family derepression → MYCN upregulation → RB bypass; PPB type III with MYCN amplification has ~53% 5-year OS.
- `connects-to` → **[Rhabdomyosarcoma](../../07-system/rhabdomyosarcoma/README.md)** — Cervical embryonal rhabdomyosarcoma (ERMS) is a rare but sentinel DICER1 syndrome tumor; DICER1 hotspot mutations found in ~20% of cervical ERMS; DICER1 syndrome RMS is distinct from sporadic RMS; conservative surgery preferred in pediatric cervical ERMS.
- `connects-to` → **[Ovarian Cancer](../../07-system/ovarian-cancer/README.md)** — Ovarian Sertoli-Leydig cell tumors (SLCT) are the most common ovarian manifestation of DICER1 syndrome; DICER1 hotspot mutations drive ~60% of all SLCT; DICER1 germline carriers: pelvic US surveillance from age 8; BEP chemotherapy for advanced/recurrent SLCT.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Let-7 miRNA family (depleted by DICER1 RNase IIIb hotspot) is the primary KRAS 3'UTR suppressor; DICER1 hotspot → let-7-5p loss → KRAS mRNA derepression → constitutive RAS-MAPK; KRAS upregulated in PPB via this axis; KRAS can be oncogenic without mutation when let-7 is depleted.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — DICER1 syndrome carriers have elevated DTC risk; DICER1 somatic hotspot mutations in ~10-15% of follicular and poorly differentiated thyroid carcinoma; thyroid US surveillance from age 8 in DICER1 carriers; DICER1-mutant thyroid cancer often arises in multinodular goiter.
- `connects-to` → **[Wilms Tumor](../wilms-tumor/README.md)** — DICER1 hotspot mutations found in ~5% of Wilms tumor; cystic nephroma (benign DICER1 renal tumor) can contain Wilms-like blastemal elements (partially differentiated nephroblastoma); renal US surveillance in DICER1 carriers aged 0-8 detects cystic nephroma before transformation.
- `connects-to` → **[Bloom Syndrome](../bloom-syndrome/README.md)** — DICER1 and Bloom are both childhood cancer-predisposition syndromes but mechanistically distinct: DICER1 is faulty microRNA processing (RNase IIIb hotspots depleting 5p miRNAs), Bloom genomic instability from a defective BLM helicase — gene dysregulation versus broken DNA repair.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pleuropulmonary blastoma is the sentinel DICER1 tumor: a rare embryonal lung cancer that begins as benign cystic lesions (type I) in infancy and can progress to solid high-grade sarcoma (type III); resecting it early is why chest imaging surveillance starts in the newborn period.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is a key DICER1 site: cystic nephroma, a benign multilocular renal cyst, can harbor Wilms-like blastemal elements and rarely progress to anaplastic sarcoma; renal ultrasound surveillance from birth to age 8 catches these before transformation.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — DICER1 syndrome reaches the CNS: germline DICER1 loss predisposes to pineoblastoma and a distinct DICER1-mutant embryonal brain tumor that overlaps morphologically with medulloblastoma—so miRNA-processing failure, not just SHH/WNT, can drive childhood embryonal CNS cancer.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — DICER1 and Li-Fraumeni are major inherited pediatric cancer-predisposition syndromes with overlapping tumors (rhabdomyosarcoma, CNS embryonal tumors) but distinct mechanisms: DICER1 disrupts microRNA processing, Li-Fraumeni loses TP53 function—both warrant surveillance.
- `connects-to` → **[Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — The lung epithelium is the cradle of DICER1's signature tumor: pleuropulmonary blastoma arises in the developing lung where DICER1 loss in the airway/alveolar epithelium (including type II pneumocytes) drives cystic then sarcomatous change, the childhood hallmark of the syndrome.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — DICER1 syndrome and retinoblastoma are inherited pediatric cancer-predisposition syndromes: DICER1 disrupts microRNA processing to cause pleuropulmonary blastoma and embryonal tumors, while RB1 loss causes retinoblastoma—both needing childhood surveillance.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — DICER1 syndrome and rhabdoid tumor predisposition both cause aggressive embryonal childhood tumors: DICER1 (microRNA processing) yields pleuropulmonary blastoma and CNS tumors, while SMARCB1 loss yields ATRT—overlapping in the infant brain-tumor differential.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — DICER1 syndrome causes a rare HPV-independent cervical cancer: embryonal rhabdomyosarcoma (sarcoma botryoides) of the cervix arises from germline DICER1 loss in young women, a distinctive non-carcinoma cervical tumor that, unlike typical cervical cancer, is unrelated to HPV.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid is a hallmark DICER1 target: carriers develop multinodular goiter and differentiated thyroid cancer at high rates, often after chemotherapy for other DICER1 tumors—so thyroid surveillance is central to managing the syndrome.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — DICER1 tumors are often mesenchymal blastomas with fibroblast-like sarcomatous cells: impaired microRNA processing drives pleuropulmonary blastoma and rhabdomyosarcoma-like growths of primitive spindle cells—unlike the epithelial cancers of most syndromes.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — DICER1 and p53 can cooperate in tumor formation: loss of microRNA maturation deregulates growth genes, and concurrent TP53 mutation accelerates malignant DICER1 tumors—so the miRNA machinery joins the classic tumor-suppressor network in controlling cancer.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — DICER1 syndrome strikes the reproductive system: it causes ovarian Sertoli-Leydig cell tumors that can virilize, plus other gonadal tumors, so a young woman with such a tumor warrants DICER1 testing and broader cancer surveillance.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — DICER1 syndrome reaches multiple endocrine glands: beyond thyroid disease it causes pituitary blastoma in infants and rare adrenal and pineal tumors, so its microRNA-processing defect disrupts hormone-producing tissues across the endocrine system.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — DICER1 syndrome affects the eye: ciliary body medulloepithelioma, a rare childhood intraocular tumor, is part of its spectrum, so an unusual eye tumor in a child can be the presenting clue to this pleiotropic tumor-predisposition syndrome.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — DICER1 syndrome seeds tumors in the brain: pineoblastoma and pituitary blastoma are characteristic CNS tumors, so unusual childhood brain tumors—especially with other DICER1 features—prompt testing for this microRNA-processing gene defect.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — DICER1's pituitary blastoma floods the body with cortisol: this rare infant tumor secretes ACTH, causing Cushing's disease in babies, so early-life Cushing's is a red flag for a DICER1 mutation behind the pituitary tumor.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — DICER1 carriers warrant caution with radiation: as in other tumor-predisposition syndromes, radiotherapy's DNA-damaging photons may raise the lifetime risk of second cancers, so treatment plans weigh radiation exposure carefully against benefit.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — DICER1 syndrome can flood a young woman with testosterone: its Sertoli-Leydig cell ovarian tumors secrete androgens, causing virilization—deepening voice, hair growth, and missed periods—a striking clue that points toward testing for the syndrome.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — DICER1's most common sign is in the iodine-trapping thyroid: it drives multinodular goiter and raises thyroid cancer risk, so the gland that concentrates iodine to make hormone overgrows into nodules that warrant lifelong ultrasound screening.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — DICER1 governs how neurons mature through microRNA: the gene's miRNA-processing job lets neural progenitors differentiate, so when it fails immature neuron-like cells can persist and seed the rare embryonal brain tumors of the syndrome.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — DICER1 tumors lean on mTOR growth signaling: the embryonal and sarcomatous tumors of the syndrome activate this pathway to fuel proliferation, making mTOR inhibition a strategy explored across its diverse childhood cancers.
- `connects-to` → **[WT1](../../03-molecular/wt1/README.md)** — DICER1 syndrome raises the risk of Wilms tumor, the cancer of the WT1 gene: though it strikes the kidney by a different route—failed microRNA processing rather than WT1 loss—it adds nephroblastoma to the syndrome's tumor spectrum.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages populate DICER1's tumors: in the pleuropulmonary blastomas and sarcomas of the syndrome they infiltrate the stroma and secrete growth and angiogenic factors, shaping the microenvironment of these embryonal cancers.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — DICER1's cystic lung tumors can burst into the chest: type I pleuropulmonary blastoma forms air-filled cysts that rupture, spilling air—mostly nitrogen—into the pleural space and collapsing the lung (pneumothorax).
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — DICER1's embryonal tumors build new vessels: endothelial cells form the dense vasculature that supplies the fast-growing pleuropulmonary blastomas and sarcomas, a feature anti-angiogenic drugs aim to cut off.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — DICER1 syndrome reaches the pancreas: rare pancreatoblastoma, a childhood pancreatic cancer, is part of its broad tumor spectrum, extending the syndrome's microRNA-driven risk to yet another organ.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — DICER1's signature tumor grows in the lung's air spaces: pleuropulmonary blastoma starts as benign-looking cysts in the alveolar regions of young children that can degenerate into aggressive sarcoma.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Losing DICER1 unleashes growth signals: without mature let-7 microRNAs to restrain them, IGF and other growth factors run high, helping drive the overgrowth and tumors of the syndrome.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — DICER1's ovarian Sertoli-Leydig tumors are hormonally active: they secrete sex steroids, so virilization or disrupted estrogen balance is often the first clue in a young woman.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals DICER1's signature tumor: pleuropulmonary blastoma forms cysts lined by primitive blastemal cells with scattered rhabdomyoblasts, the embryonal ultrastructure of a cancer of early childhood.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — DICER1's reach includes the liver: hepatoblastoma and other hepatic tumors fall within its broad spectrum, so the liver joins the long list of organs watched in children carrying the mutation.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut can sprout DICER1 growths too: juvenile-type intestinal polyps are part of the syndrome's varied tumor predisposition, adding the bowel to its head-to-pelvis surveillance.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — DICER1 can wreck an infant's hormones: its pituitary blastoma oversecretes ACTH, driving the adrenal glands into a florid Cushing syndrome in babies — a rare but striking endocrine face of the cancer predisposition.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — DICER1 seeds the female genital tract with sarcoma: embryonal rhabdomyosarcoma (botryoides) sprouts in the cervix and uterus, growing within the muscular wall as a grape-like mass that bleeds.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Treating its childhood cancers empties the marrow: the multi-agent chemotherapy for pleuropulmonary blastoma and the other DICER1 tumors drops neutrophils into febrile neutropenia, a constant hazard of the regimens.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immune surveillance shapes who gets cancer: most DICER1 carriers stay tumor-free despite the germline hit, and cytotoxic T cells policing the many tissues at risk are part of that defense — a rationale for exploring immunotherapy in DICER1 tumors.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — DICER1 tumors learn to suppress the attack: like other cancers they can recruit regulatory T cells that damp local immunity, helping the second-hit clone grow past the cytotoxic defenses that hold most carriers' tissues in check.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Its tumors can bleed and drain the blood: large pleuropulmonary blastomas and the kidney and gynecologic tumors of DICER1 cause chronic blood loss and anemia of malignancy, leaving children pale and tired before treatment even begins.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Its embryonal tumors are richly vascular: with normal microRNA control lost, angiogenic signals like VEGF run unchecked, feeding the rapid growth of pleuropulmonary blastoma and the other DICER1 tumors.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — DICER1 reaches the uterus and cervix: it causes embryonal rhabdomyosarcoma of the gynecologic tract, so a young woman's unusual cervical or uterine tumor can be the clue that points to the germline syndrome.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Innate immunity guards the second hit: natural killer cells help cull the genomically deranged cells of DICER1 tumors, and harnessing them is part of the immunotherapy interest in these pediatric cancers.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — The lung is DICER1's signature target: pleuropulmonary blastoma, the syndrome's hallmark tumor, begins as benign lung cysts in early childhood that can transform into an aggressive sarcoma, so detecting cystic lung disease is central to surveillance.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — DICER1 doubles as a broader tumor suppressor: beyond the inherited syndrome, reduced DICER1 and disrupted microRNA biogenesis are seen in aggressive sporadic neuroblastoma, where loss of mature miRNAs lets oncogenic programs run.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — Losing DICER1 derepresses developmental signals: the mature microRNAs it generates normally restrain pathways like Notch, so impaired miRNA processing in DICER1 tumors unleashes the oncogenic signaling that drives embryonal growth.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Lost microRNA control lifts the brake on STAT3: DICER1-deficient cells lose mature miRNAs that normally restrain growth pathways, derepressing signaling including STAT3 that helps drive its embryonal tumors.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its kidney tumors cost nephrons: cystic nephroma and anaplastic sarcoma of the kidney are DICER1 tumors that require nephron-sparing surgery or nephrectomy, so cumulative renal loss can reduce kidney function over time.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Treating its childhood tumors invites infection: the chemotherapy used against pleuropulmonary blastoma and other DICER1 cancers causes neutropenia, making febrile neutropenia and sepsis a treatment hazard in affected children.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Its tumors and their chemo blunt the marrow: the malignancies of DICER1 syndrome and the myelosuppressive chemotherapy they require depress erythropoiesis, adding an anemia-of-chronic-disease component to treatment cytopenias.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Cancer and its surgery raise the clot risk: the tumors of DICER1 syndrome and the operations and central lines used to treat them predispose to venous thromboembolism, as in other childhood cancers.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Lifelong tumor surveillance weighs on families and patients: living with an inherited predisposition to multiple childhood and adult tumors, and the repeated screening it demands, carries a real psychological burden.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Treating its tumors strains the heart: the anthracycline and alkylator chemotherapy for the sarcomas and blastomas DICER1 predisposes to is cardiotoxic, risking cardiomyopathy and heart failure in survivors.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its cancer chemotherapy opens the lung to mold: the neutropenia from treating DICER1-related tumors such as pleuropulmonary blastoma can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Constant multi-organ surveillance breeds worry: the lifelong screening for the many tumors of DICER1 syndrome, often beginning in childhood, fosters chronic health anxiety in patients and families.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It seeds tumours in the kidney: DICER1 syndrome causes cystic nephroma and, less often, renal sarcoma and Wilms-like tumours, part of its broad childhood-tumour spectrum.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Resecting its tumours means many wounds: surgery for pleuropulmonary blastoma, cystic nephroma, ovarian and other DICER1 tumours leaves children with operative wounds that must heal.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Chemotherapy reawakens shingles: the chemotherapy used against DICER1-related cancers suppresses a child's immunity, allowing latent or primary varicella-zoster to cause severe disease.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It seeds rare brain tumours: DICER1 predisposes to pineoblastoma and pituitary blastoma and other unusual childhood central-nervous-system tumours, warranting neurological surveillance.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It arises in cartilage and soft tissue: nasal chondromesenchymal hamartoma and the embryonal rhabdomyosarcomas of the DICER1 spectrum develop in cartilage and skeletal muscle.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its chemotherapy can scar the heart: anthracyclines used against DICER1-related cancers carry a long-term cardiotoxicity risk in the children who receive them.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It can sprout polyps in the gut: DICER1 syndrome is reported to cause gastrointestinal juvenile-type polyps and rare hepatic and pancreatic tumours among its diverse lesions.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — A fellow medulloblastoma predisposition: like Gorlin syndrome, DICER1 syndrome raises childhood brain-tumour risk, the two entering the differential of inherited medulloblastoma (pineoblastoma).
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Shared thyroid-cancer risk: DICER1 and Cowden syndrome both predispose to thyroid nodules and cancer from childhood, placing both in thyroid-surveillance guidance for inherited disease.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo treats its embryonal tumours: pleuropulmonary blastoma and other DICER1 sarcomas are treated with intensive multi-agent, often sarcoma-type, chemotherapy after surgery.
- `connects-to` → **[Birt-Hogg-Dubé Syndrome](../birt-hogg-dube-syndrome/README.md)** — Two inherited causes of lung cysts: like Birt-Hogg-Dubé, DICER1 syndrome produces familial cystic lung disease, though DICER1's cysts can transform into pleuropulmonary blastoma, demanding early surveillance.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — A fellow paediatric sarcoma: DICER1-related sarcomas join Ewing sarcoma among aggressive childhood sarcomas treated with multimodal therapy, entering each other's pathological differential.
- `connects-to` → **[Lung Slice](../../05-tissue/lung-slice/README.md)** — Its hallmark tumour is cystic lung: pleuropulmonary blastoma begins as benign air-filled lung cysts in early childhood that can transform into an aggressive sarcoma, so cystic change on a lung slice triggers DICER1 surveillance.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Beyond chemotherapy: anti-angiogenic and other targeted agents are explored for the diverse DICER1 sarcomas, and the syndrome's miRNA-processing defect is itself a focus of emerging precision approaches.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — Inherited multi-endocrine tumour cousins: like Carney complex, DICER1 syndrome predisposes to a spread of endocrine tumours — thyroid carcinoma and ovarian Sertoli-Leydig tumours — under germline control demanding glandular surveillance.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Renal tumours of childhood: DICER1 causes cystic nephroma and a subset of Wilms tumours, developmental kidney tumours arising in the nephron near the glomerulus.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Shared ovarian sex-cord tumours: DICER1's Sertoli-Leydig tumours and the sex-cord tumours with annular tubules of Peutz-Jeghers both arise in the ovary, two germline syndromes converging on this rare tumour family.
- `connects-to` → **[Hereditary Breast-Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — A different kind of ovarian cancer: DICER1 drives sex-cord-stromal ovarian tumours of the young, biologically distinct from the BRCA-driven epithelial ovarian cancer of hereditary breast-ovarian syndrome.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Childhood kidney tumours: DICER1 syndrome causes cystic nephroma and anaplastic sarcoma of the kidney, paediatric renal tumours distinct from the clear cell renal carcinoma of adults.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Pituitary blastoma: DICER1 syndrome causes infantile pituitary blastoma, an ACTH-secreting neuroendocrine tumour driving Cushing disease, part of its broad neuroendocrine spectrum.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — A mesenchymal-tumour spectrum: beyond embryonal rhabdomyosarcoma, DICER1 syndrome can produce other sarcomas including rare osteosarcoma, reflecting its broad predisposition to mesenchymal tumours.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Let-7 brake released: DICER1 mutations impair processing of let-7 family microRNAs, derepressing oncogenes like MYC that these microRNAs normally restrain—a core mechanism of DICER1 tumours.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-mTOR activation: PIK3CA-driven PI3K signalling feeds the mTOR pathway active in DICER1-associated tumours, offering a targetable axis alongside the primary microRNA defect.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Malignant progression: TERT activation enabling replicative immortality marks the shift of DICER1 lesions from low-grade cystic tumours toward aggressive sarcomatous malignancy.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: loss of let-7 microRNA control from DICER1 dysfunction derepresses cyclin D and the cell-cycle machinery, accelerating proliferation in DICER1-associated tumours.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in growing DICER1-associated tumours such as pleuropulmonary blastoma drives the VEGF angiogenesis that supports their expansion.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic dysregulation: disrupted microRNA processing in DICER1 syndrome derepresses EZH2 and other chromatin regulators, contributing to the embryonal tumour phenotype.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Sex-cord stromal tumours: the activin-inhibin axis of gonadal stromal cells underlies the Sertoli-Leydig cell tumours of DICER1 syndrome, whose inhibin secretion serves as a tumour biomarker.
- `connects-to` → **[Thyroid Hormones](../../03-molecular/thyroid-hormones/README.md)** — Thyroid neoplasia: DICER1 syndrome predisposes to multinodular goitre and differentiated thyroid carcinoma, one of the most common and earliest manifestations of the disorder.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Survival signalling: PI3K-AKT activation cooperates with the microRNA-processing defect of DICER1 syndrome to support the growth and survival of its diverse embryonal and stromal tumours.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — DICER1 syndrome predisposes to pineoblastoma, an aggressive RB-pathway-driven embryonal brain tumor that joins pleuropulmonary blastoma in the syndrome's intracranial tumor spectrum and shares biology with retinoblastoma.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Loss of DICER1-processed microRNAs derepresses growth-factor pathways including FGFR signaling, driving the proliferation of the embryonal tumors such as pleuropulmonary blastoma and embryonal rhabdomyosarcoma.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss accompanies the progression of pleuropulmonary blastoma from the early cystic type I to the solid, sarcomatous type III—a key cell-cycle lesion in the malignant evolution of DICER1 tumors.
- `connects-to` → **[Androgen receptor](../../03-molecular/androgen-receptor/README.md)** — DICER1 causes ovarian Sertoli-Leydig cell tumors that secrete androgens, producing the virilization—hirsutism, deepening voice—that often brings these young patients to attention and declares the syndrome.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — The embryonal tumors of DICER1 syndrome, especially pleuropulmonary blastoma, are treated with intensive chemotherapy that kills cells through caspase-3-mediated apoptosis, the effector step underlying treatment response.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Loss of DICER1-dependent microRNA regulation derepresses developmental pathways including Wnt/β-catenin in the embryonal DICER1 tumors, reflecting their origin in dysregulated organ development.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — KRAS and FGFR (both already mapped) drive the MAPK-ERK cascade in DICER1-associated tumors such as pleuropulmonary blastoma and Sertoli-Leydig cell tumors.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN normally limits the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped) that is co-activated in DICER1 tumors to support their growth.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Loss of DICER1-dependent microRNA control over cell-cycle genes, alongside the RB-CDKN2A-cyclin-D1 axis already mapped, releases E2F1 to drive proliferation in embryonal DICER1 tumors.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β/activin-superfamily signaling (activin-A already mapped) shapes the Sertoli-Leydig and other gonadal-stromal tumors characteristic of DICER1 syndrome.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT receptor-tyrosine-kinase signaling contributes to the embryonal and germ-cell-related tumors that arise in DICER1 syndrome.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), supporting the survival of the diverse embryonal tumors of DICER1 syndrome.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is a marker of the thyroid neoplasia that is a hallmark of DICER1 syndrome and modulates tumor-cell behavior.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β/activin-SMAD signaling (TGF-β and activin-A mapped) shapes the gonadal-stromal and embryonal tumors of DICER1 syndrome.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 mapped) provides a proliferative input across the diverse tumors of DICER1 syndrome.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune surveillance of the diverse neoplasms that arise in DICER1 syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the immune microenvironment of the DICER1-driven tumors.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate the metabolic and oxidative stress of the proliferating cells of DICER1-syndrome tumors, downstream of the disrupted miRNA program.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D-RB axis (cyclin-D1 and RB1 already mapped) drives the proliferation of DICER1-syndrome tumors.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in DICER1-syndrome tumors.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is the immune clearance that the multiple DICER1-associated tumors must evade.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the Wnt/β-catenin and survival signaling (Wnt already mapped) of the tumors of DICER1 syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation, alongside the miRNA-processing defect of DICER1 loss, contributes to the epigenetic dysregulation of DICER1 syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of the tumors of DICER1 syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the tumors of DICER1 syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and stress management of the tumors of DICER1 syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of DICER1 syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of DICER1 syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the neoplasms of DICER1 syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of DICER1 syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of DICER1 syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of DICER1 syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of DICER1 syndrome.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunosurveillance: MHC class II-restricted T-cell surveillance influences which of the diverse embryonal and stromal tumours of DICER1 syndrome progress, and antigen presentation is relevant to immunotherapy of the aggressive ones such as pleuropulmonary blastoma.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell expansion: IL-2-driven T-cell proliferation supports the adaptive immune responses and cellular immunotherapy approaches being considered for the childhood cancers of DICER1 syndrome (perforin already mapped).
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint context: PD-1-mediated exhaustion limits anti-tumour immunity, and checkpoint blockade is explored for the rare high-risk DICER1-associated cancers that recur or metastasise.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Chemotherapy anaemia: the intensive chemotherapy for the childhood cancers of DICER1 syndrome, such as pleuropulmonary blastoma and embryonal rhabdomyosarcoma (already mapped), is myelosuppressive and lowers haemoglobin.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: anthracyclines in the sarcoma regimens for DICER1-associated tumours are cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury threatening these young survivors.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis and oxidative stress: the high proliferative rate of the embryonal DICER1 tumours, lysed by chemotherapy, releases purines catabolised by xanthine oxidase to uric acid, contributing to tumour-lysis risk and oxidative stress.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment of the DICER1-associated tumours dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune evasion relevant to immunotherapy of any aggressive tumour.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the DICER1-associated embryonal tumours, part of their stromal microenvironment.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Transfusion and anaemia: the anaemia of the DICER1 sarcomas and their intensive chemotherapy (haemoglobin already mapped) requires transfusion support, whose repeated use can load the young survivor with iron.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the DICER1-associated embryonal tumours.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of the DICER1 sarcomas.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton radiotherapy: proton-beam radiotherapy treats the DICER1-associated sarcomas while sparing the developing tissues of the young child, though radiation is used cautiously given the germline tumour predisposition.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Cystic nephroma: the cystic nephroma (and the anaplastic sarcoma) of the kidney (WT1 already mapped) is a characteristic DICER1 renal tumour of childhood.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Ciliary-body medulloepithelioma: the intraocular ciliary-body medulloepithelioma of the eye is a rare but characteristic tumour of the DICER1 syndrome spectrum.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Pineoblastoma and CNS tumours: the pineoblastoma and the CNS sarcomas of the brain are part of the DICER1 tumour spectrum, reflecting the germline miRNA-processing (DICER1 already mapped) defect.
- `connects-to` → **[Thyroid](../../06-organ/thyroid/README.md)** — Multinodular goitre: the thyroid gland develops the multinodular goitre (thyroid-hormones already mapped) and the differentiated thyroid cancer of the DICER1 syndrome, especially after chemotherapy/RT.
- `connects-to` → **[Ovarian cancer](../ovarian-cancer/README.md)** — Sertoli-Leydig tumour: the ovarian Sertoli-Leydig cell tumour (the androgen — androgen-receptor already mapped — secreting sex-cord-stromal tumour) is a characteristic DICER1 ovarian tumour.
- `connects-to` → **[Wilms tumor](../wilms-tumor/README.md)** — Renal-tumour differential: the DICER1 renal tumours (the cystic nephroma, the anaplastic sarcoma — WT1 already mapped) are in the differential of the Wilms tumour.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity relevant to the diverse DICER1 tumours (checkpoint PD-1 already mapped).
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the DICER1-syndrome tumours.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the DICER1-syndrome tumours.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the DICER1-syndrome tumours.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 arm: IL-17A drives the Th17 arm of the inflammatory dimension of the immune microenvironment of the DICER1-syndrome tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 induction: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the DICER1-syndrome tumour microenvironment.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the DICER1-syndrome tumours.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the immune microenvironment of the DICER1-syndrome tumours.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the DICER1-syndrome tumour stroma.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^schultz-2018-dicer1-surveillance]: Schultz KAP, Williams GM, Kamihara J, et al. DICER1 and Associated Conditions: Identification of At-risk Individuals and Recommended Surveillance Strategies. *Clin Cancer Res.* 2018;24(10):2251-2261. [doi:10.1158/1078-0432.CCR-17-3089](https://doi.org/10.1158/1078-0432.CCR-17-3089) · [PubMed 29343557](https://pubmed.ncbi.nlm.nih.gov/29343557/)
[^hill-2009-dicer1]: Hill DA, Ivanovich J, Priest JR, et al. DICER1 mutations in familial pleuropulmonary blastoma. *Science.* 2009;325(5943):965. [doi:10.1126/science.1174334](https://doi.org/10.1126/science.1174334) · [PubMed 19556464](https://pubmed.ncbi.nlm.nih.gov/19556464/)
