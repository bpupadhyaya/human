---
schema: human-scale-entry/v1
id: renal-cell-carcinoma
name: Renal Cell Carcinoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Clear cell RCC (~75%) is driven by VHL loss → HIF activation → VEGF angiogenesis; papillary type driven by MET and CDKN2A. Nivolumab+ipilimumab and pembrolizumab+axitinib are first-line for advanced RCC; cabozantinib is active after ICI progression."
aliases: ["renal cell carcinoma", "RCC", "clear cell RCC", "ccRCC", "papillary RCC", "chromophobe RCC", "kidney cancer", "renal carcinoma", "VHL-mutant RCC"]
sources:
  - id: motzer-2018-checkmate214
    type: peer-reviewed
    cite: "Motzer RJ, Tannir NM, McDermott DF, et al. Nivolumab plus ipilimumab versus sunitinib in advanced renal-cell carcinoma. N Engl J Med. 2018;378(14):1277-1290."
    doi: "10.1056/NEJMoa1712126"
    pmid: "29562145"
    url: "https://doi.org/10.1056/NEJMoa1712126"
  - id: rini-2019-keynote426
    type: peer-reviewed
    cite: "Rini BI, Plimack ER, Stus V, et al. Pembrolizumab plus axitinib versus sunitinib for advanced renal-cell carcinoma. N Engl J Med. 2019;380(12):1116-1127."
    doi: "10.1056/NEJMoa1816714"
    pmid: "30779529"
    url: "https://doi.org/10.1056/NEJMoa1816714"
cross_links:
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Sunitinib and pazopanib (VEGFR TKIs) were first-line RCC standards; cabozantinib (VEGFR+MET+AXL) approved 1st-line for poor/intermediate-risk (CABOSUN) and 2nd-line (METEOR); ICI+VEGFR TKI combinations (pembro+axitinib, nivo+cabo) now preferred in first-line."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Nivolumab+ipilimumab (CheckMate 214) improved OS in intermediate/poor-risk RCC; pembrolizumab+axitinib (KEYNOTE-426) improved OS vs. sunitinib; nivolumab+cabozantinib (CheckMate 9ER) PFS 16.6 vs. 8.3 months; ICI combinations are standard first-line for advanced RCC."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Everolimus (mTOR inhibitor) approved for 2nd-line RCC after VEGFR TKI failure (RECORD-1: PFS 4.9 vs. 1.9 months); temsirolimus improved OS vs. IFN-α in poor-risk RCC; lenvatinib+everolimus approved 2nd-line; mTOR inhibitors largely displaced by ICI+VEGFR combinations."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "VHL loss → constitutive HIF-1α/HIF-2α stabilization → VEGF, GLUT1, EPO, PDGF transcription in ccRCC; HIF-2α (EPAS1) is the primary oncogenic HIF isoform; belzutifan (HIF-2α inhibitor) FDA approved 2021 for VHL disease and 2023 for 3rd-line ccRCC."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Most RCCs arise from the kidney's proximal tubule; small T1a tumors are often found incidentally on CT and cured by nephron-sparing partial nephrectomy, while VHL-null tumor cells secrete EPO, renin, or PTHrP — causing paraneoplastic polycythemia, hypertension, or hypercalcemia."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "Von Hippel-Lindau disease (germline VHL loss) predisposes to bilateral, multifocal, early-onset clear-cell RCC alongside hemangioblastomas and pheochromocytomas; the same VHL→HIF-2α pseudohypoxia drives both hereditary and the >90% of sporadic ccRCC, and belzutifan targets it."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Type 1 papillary RCC is driven by MET activation (amplification or germline mutation in hereditary papillary RCC), distinct from VHL-driven clear-cell disease; these tumors respond poorly to VEGFR TKIs, so the MET/VEGFR2 inhibitor cabozantinib is the preferred targeted agent."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Renal cell carcinoma and pheochromocytoma/paraganglioma share pseudohypoxia: VHL (or SDHx/FH) loss stabilizes HIF-2α, driving VEGF-fueled hypervascular tumors in both; VHL disease produces clear-cell RCC and PHEO together, and belzutifan (HIF-2α inhibitor) treats both."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "HLRCC (hereditary leiomyomatosis and RCC) is an aggressive inherited renal cancer: germline fumarate hydratase loss lets fumarate inhibit HIF prolyl-hydroxylases → pseudohypoxia like VHL ccRCC, but its type-2 papillary tumors are far more aggressive and resected when small."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Renal cell carcinoma is among the most immune-responsive solid tumors despite modest mutational burden: checkpoint inhibitors freeing cytotoxic CD8+ T cells (nivolumab+ipilimumab, pembrolizumab+axitinib) are first-line; RCC also historically responded to IL-2."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Tuberous sclerosis predisposes to renal cell carcinoma and angiomyolipoma: TSC1/TSC2 loss unleashes mTOR in the kidney, producing fat-rich angiomyolipomas and a distinctive RCC, so mTOR inhibitors (everolimus) shrink TSC renal lesions and also treat advanced sporadic RCC."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Renal cell carcinoma is a classic cause of paraneoplastic polycythemia: HIF stabilization in clear-cell RCC drives ectopic erythropoietin, expanding the red-cell mass—one of several paraneoplastic syndromes that can be the first sign of a kidney tumor."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Renal cell and bladder cancer are the two major urologic malignancies that differ in cell and cause: RCC arises from renal tubular epithelium and presents with a mass or paraneoplastic signs, while bladder cancer is a smoking-linked urothelial tumor with painless hematuria."
  - target: 01-human/07-system/birt-hogg-dube-syndrome
    relation: connects-to
    note: "RCC unifies several hereditary syndromes including Birt-Hogg-Dubé: BHD's FLCN loss causes chromophobe and oncocytic kidney tumors, one of the inherited RCC syndromes alongside VHL (clear cell) and HLRCC (papillary)—each gene yielding a distinct RCC histology."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "Renal clear cell carcinoma and ovarian clear-cell carcinoma share clear-cell morphology but differ in biology: RCC is VHL/HIF-driven, while ovarian clear-cell is ARID1A/PIK3CA-driven—so 'clear cell' is a convergent appearance, not a shared pathway."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Renal cell carcinoma is a classic cause of paraneoplastic polycythemia: the tumor can secrete erythropoietin, raising red-cell mass and mimicking polycythemia vera—so erythrocytosis without a JAK2 mutation warrants renal imaging to exclude an EPO-producing tumor."
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "VHL loss is the central event in clear cell RCC: inactivating the VHL tumor suppressor stabilizes HIF, driving VEGF and the angiogenic, clear-cell tumor—so both sporadic and von Hippel-Lindau-associated kidney cancers converge on this oxygen-sensing pathway."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "RCC hijacks the kidney's own erythropoietin role: the kidney normally makes EPO sensing oxygen, and VHL-mutant tumor cells, fixed in pseudohypoxia, oversecrete it—causing paraneoplastic polycythemia, a cancer co-opting an organ's native hormone."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity is a leading modifiable RCC risk factor: excess adiposity, with hypertension and chronic kidney stress, raises renal cell carcinoma risk through insulin/IGF and inflammatory signaling—making RCC one of the obesity-associated cancers."
  - target: 01-human/03-molecular/bap1
    relation: connects-to
    note: "BAP1 loss marks an aggressive renal cell carcinoma subtype: this tumor-suppressor deletion (also seen in mesothelioma and uveal melanoma) defines high-grade clear-cell RCC with worse survival, so BAP1 status refines prognosis beyond the classic VHL/HIF pathway."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Renal cell carcinoma is the principal cancer of the renal system: it arises from the kidney's tubular epithelium and can secrete erythropoietin or renin, often presenting late with hematuria, flank pain or a mass—the kidney's own physiology becoming the tumor's traits."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Renal cell carcinoma is famously immunogenic: it can spontaneously regress and was an early success for IL-2 and now checkpoint immunotherapy, so engaging the immune system—often with anti-angiogenic drugs—is central to treating advanced RCC."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "Clear-cell RCC is built on the HIF-2alpha factor EPAS1: VHL loss stabilizes EPAS1, which switches on VEGF and growth genes—so the HIF-2alpha inhibitor belzutifan directly blocks this driver, a new oral therapy for VHL-related and advanced kidney cancer."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "RCC classically causes paraneoplastic hypercalcemia: tumors secrete PTH-related peptide that raises blood calcium independent of bone metastases, so unexplained hypercalcemia can be a presenting clue to an occult kidney cancer."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lungs are RCC's favorite metastatic site: kidney cancer characteristically seeds multiple round 'cannonball' lung metastases through the bloodstream, so chest imaging is essential to staging—and lung lesions are often the first sign of spread."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Kidney cancer can fake hyperparathyroidism: RCC secretes PTH-related peptide that mimics PTH, driving paraneoplastic hypercalcemia even without bone metastases—one of the syndromes that makes RCC 'the internist's tumor.'"
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Kidney cancer is immunotherapy-sensitive yet shielded by regulatory T cells: RCC draws strong T-cell infiltrates that respond to checkpoint drugs, but Tregs in the tumor restrain them—so depleting Tregs is sought to deepen responses."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Kidney cancer is packed with tumor-associated macrophages: M2-polarized macrophages promote its angiogenesis and immune escape, and a macrophage-heavy infiltrate predicts worse outcomes in clear cell RCC."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Clear cell kidney cancer is the archetypal oxygen-sensing tumor: VHL loss makes it behave as if hypoxic even in normal oxygen, stabilizing HIF to pump out VEGF and EPO—the pseudohypoxia that defines it and guides anti-angiogenic therapy."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Kidney cancer is notorious for spreading to the brain: RCC seeds brain metastases through the blood, sometimes years after the primary, so new neurologic symptoms in a kidney-cancer survivor demand imaging."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells are central to kidney cancer's unusual immunogenicity: RCC was one of the first tumors to respond to immunotherapy, and antigen-presenting dendritic cells help prime the T-cell attack that checkpoint drugs amplify."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Kidney cancer bleeds iron into the urine: painless hematuria is a classic sign, and the chronic blood loss drains iron into anemia—though RCC can paradoxically also raise red cells via erythropoietin."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Kidney cancer haunts the pancreas late: RCC is one of the few tumors that metastasizes to the pancreas, often many years after the kidney was removed, so long-term surveillance matters."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "RCC can drive the marrow to overproduce blood: its ectopic erythropoietin spurs the bone marrow to make excess red cells, a paraneoplastic polycythemia unusual among cancers."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons diagnose RCC without a needle: contrast-enhanced CT and MRI characterize the mass so reliably that surgery often proceeds on imaging alone, while bone and brain scans hunt the lytic metastases this cancer scatters."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "RCC reaches straight for the adrenal gland sitting atop the kidney: it invades or metastasizes to the ipsilateral adrenal so readily that the gland was once removed routinely with the kidney during radical nephrectomy."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "RCC can push platelets up: a paraneoplastic thrombocytosis driven by tumor IL-6 appears in a share of patients, and a high platelet count at diagnosis is a marker of more aggressive disease and worse survival."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "The 'clear' in clear-cell RCC is an artifact of its lipids: the cytoplasm is stuffed with glycogen and fat that dissolve away in processing, leaving the empty-looking cells that electron microscopy and histology use to recognize the commonest RCC."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "RCC can derange the liver without touching it: Stauffer syndrome is a paraneoplastic hepatic dysfunction — raised enzymes and cholestasis with no metastases — driven by tumor cytokines and reversing once the kidney cancer is removed."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "RCC can wash out the blood's sodium: paraneoplastic hyponatremia, from tumor-driven ADH or cytokines, is common in advanced disease and flags a poorer prognosis, sometimes correcting after the tumor is treated."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both label and treat RCC: PAX8, CD10, and CA-IX stains confirm renal origin on biopsy, and the disease is now driven by antibody therapy — anti-PD-1 checkpoint blockade and anti-VEGF agents that exploit its rich, VHL-driven vasculature."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The blood count carries the prognosis: RCC drives a paraneoplastic leukocytosis and a high neutrophil-to-lymphocyte ratio that predicts worse survival, a marker built into the risk models that guide its targeted and immune therapies."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "RCC and its treatment both raise the pressure: the tumor can secrete renin to drive paraneoplastic hypertension, and the anti-VEGF tyrosine-kinase inhibitors used against it cause hypertension so reliably it serves as a marker that the drug is working."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "A sudden left varicocele can betray a kidney tumor: a left RCC invading the renal vein blocks the gonadal vein that drains into it, so a new, non-decompressing left varicocele in a man warrants imaging of the kidney."
  - target: 01-human/03-molecular/sdhb
    relation: connects-to
    note: "RCC has a rare metabolic-gene form: germline SDHB and related succinate-dehydrogenase mutations cause a hereditary renal cell carcinoma alongside paraganglioma, the same pseudohypoxic pathway that drives the FH-deficient and VHL kidney cancers."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "RCC can climb into the heart: its tumor thrombus grows up the renal vein and inferior vena cava, sometimes reaching the right atrium against the cardiomyocytes — while the TKIs treating it add their own cardiotoxic strain."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Its pseudohypoxic drive feeds more than VEGF: VHL loss also raises PDGF, so the tyrosine-kinase inhibitors used against RCC block PDGF receptors alongside VEGFR to starve the tumor's abundant blood supply."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "RCC is unusually immune-responsive: combining CTLA-4 blockade with anti-PD-1 unleashes T cells against the tumor and is now frontline for advanced disease, making this one of the cancers most transformed by checkpoint immunotherapy."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Diseased kidneys breed cancer: long-standing chronic kidney disease and the acquired cystic change of dialysis sharply raise RCC risk, while removing a tumor-bearing kidney can in turn push remaining function toward chronic kidney disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "RCC is one of the most vascular of tumors: VHL loss floods it with VEGF, recruiting endothelial cells into a dense blood supply that makes the tumor highly enhancing on imaging and exquisitely sensitive to anti-angiogenic drugs."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Beyond its tumor thrombus, RCC clots the blood: it carries a high rate of bland venous thromboembolism (Trousseau), so deep-vein thrombosis and pulmonary embolism complicate the disease and its surgery."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "The kidney tumor can reach the brain: RCC's hypercoagulable state, and rarely tumor embolism from IVC extension through a patent foramen, can cause ischemic stroke alongside its frequent brain metastases."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "It is a classic IL-6-producing tumor: RCC secretes IL-6, driving a paraneoplastic constitutional syndrome of fever, weight loss and raised inflammatory markers, plus Stauffer's non-metastatic hepatic dysfunction."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Despite an EPO-making kidney, the marrow can lag: the IL-6 and inflammation of RCC raise hepcidin and suppress erythropoiesis, so an anemia of chronic disease is common and paradoxically coexists with the EPO-driven polycythemia in others."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Surgery and immunotherapy open the door: major nephrectomy in often older patients and the immune perturbations of checkpoint-inhibitor therapy leave advanced-RCC patients vulnerable to serious infection and sepsis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anti-angiogenic TKIs strain the heart: sunitinib, pazopanib and other VEGF-pathway inhibitors central to RCC therapy raise blood pressure and are directly cardiotoxic, capable of precipitating heart failure."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Checkpoint immunotherapy can trigger autoimmune diabetes: the PD-1 and CTLA-4 inhibitors used for advanced RCC occasionally unleash autoimmunity against pancreatic islets, causing fulminant insulin-dependent diabetes."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An advanced cancer and its immunotherapy weigh on mood: the diagnosis, prolonged systemic therapy and the fatigue and inflammatory burden of metastatic RCC contribute to substantial depression and anxiety."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Surgery and anti-VEGF therapy heal poorly: nephrectomy is the mainstay for localised RCC, and the VEGF-targeted tyrosine-kinase inhibitors used for advanced disease impair angiogenesis, delaying wound closure."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Checkpoint immunotherapy can inflame the gut: the PD-1 and CTLA-4 inhibitors used for advanced RCC frequently trigger immune-related colitis with diarrhoea, a characteristic toxicity needing steroids."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A metastatic cancer watched scan-to-scan breeds worry: the recurrence risk, prolonged targeted and immune therapy and uncertain prognosis of advanced RCC foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It seeds the lungs with cannonballs: renal cell carcinoma metastasises classically to the lungs as multiple round 'cannonball' nodules, a defining pattern of its distant spread."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is a great paraneoplastic mimic: RCC secretes PTHrP causing hypercalcaemia, erythropoietin causing polycythaemia and renin causing hypertension, and its immunotherapy triggers endocrine irAEs."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It carves holes in bone: renal cell carcinoma metastasises to the skeleton as destructive, hypervascular osteolytic lesions that cause pain, fractures and spinal cord compression."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It grows up into the great veins: renal cell carcinoma characteristically forms a tumour thrombus that extends up the renal vein and inferior vena cava, sometimes reaching the right atrium."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It reaches the brain: renal cell carcinoma metastasises to the brain as vascular deposits prone to bleeding, and spinal metastases can compress the cord."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It spreads to the nodes: regional and retroperitoneal lymph-node involvement is a poor prognostic factor in renal cell carcinoma and guides surgical and systemic treatment."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It is a prototype of targeted and immune therapy: anti-VEGF tyrosine-kinase inhibitors, mTOR inhibitors and checkpoint immunotherapy define modern treatment of advanced renal cell carcinoma."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Another hereditary kidney-cancer syndrome: like von Hippel-Lindau and Birt-Hogg-Dubé, Cowden (PTEN) syndrome raises renal cell carcinoma risk, part of its inherited differential."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Renal tuberculosis can mimic it: genitourinary TB causes renal masses, cavitation and haematuria that enter the imaging differential of renal cell carcinoma."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "A highly immunogenic tumour: clear-cell RCC responds to checkpoint blockade — nivolumab plus ipilimumab or pembrolizumab with a VEGF TKI is now first-line for advanced disease, exploiting its heavy immune infiltrate."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Classically chemoresistant: conventional cytotoxic chemotherapy barely touches renal cell carcinoma owing to high P-glycoprotein drug efflux, which is why treatment moved to cytokines, then VEGF TKIs and immunotherapy."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It seeds destructive bone metastases: RCC frequently spreads to bone as hypervascular osteolytic lesions causing pain and pathological fractures that can bleed briskly, sometimes needing embolisation before surgery."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "Two BAP1-spectrum cancers: germline BAP1 loss predisposes to clear cell renal carcinoma alongside mesothelioma and uveal melanoma, so a BAP1 family history links a kidney cancer to a pleural one."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "It can grow into the heart: renal cell carcinoma characteristically extends as a tumour thrombus up the renal vein and inferior vena cava, sometimes reaching the right atrial endocardium and demanding cardiac surgery to remove."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Twin hypervascular, antiangiogenic-treated cancers: renal cell carcinoma and hepatocellular carcinoma are both richly vascular tumours driven by VEGF, treated with multikinase angiogenesis inhibitors (sorafenib, lenvatinib) and now immunotherapy combinations."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Cannonball lung metastases: RCC characteristically produces large, round 'cannonball' pulmonary metastases, seeding the alveolar bed—the lung being its commonest distant site."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "Two renal cancers, two ages: RCC is the adult kidney cancer arising from tubular epithelium (VHL/MET), while Wilms tumour is the childhood nephroblastoma (WT1)—the renal cancers across the lifespan."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver metastasis: beyond the lung, RCC seeds the liver, depositing in the hepatic lobule, a poor-prognosis site of distant spread."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Immunotherapy's autoimmune cost: the checkpoint inhibitors central to advanced renal cell carcinoma treatment can unleash an autoimmune colitis closely resembling inflammatory bowel disease, managed with steroids and anti-TNF biologics."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "A hypervascular tumour: VHL/HIF/VEGF make renal cell carcinoma intensely angiogenic, underlying preoperative embolization, antiangiogenic TKIs, and its hallmark growth as a tumour thrombus up the renal vein and IVC."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "The immunotherapy-responsive pair: renal cell carcinoma and melanoma were the first solid tumours to respond to high-dose IL-2 and then checkpoint blockade, sharing an unusual immunogenicity and even spontaneous regression."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "Paraneoplastic hypertension: some renal cell carcinomas secrete renin, causing hypertension and hypokalaemia—a hormonal syndrome distinct from the erythropoietin-driven polycythaemia they can also produce."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-mTOR axis: PI3K-AKT-mTOR signalling drives renal cell carcinoma, the target of mTOR inhibitors such as everolimus and temsirolimus in advanced disease."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Chromatin dysregulation: EZH2/polycomb activity, in the context of PBRM1 and BAP1 chromatin-remodeller loss, contributes to clear-cell renal carcinoma progression."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Metabolic-oncogene cooperation: the pseudohypoxic, HIF-driven state of clear-cell RCC upregulates MYC, fuelling the biosynthesis and proliferation of the tumour."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "HIF target and cell cycle: HIF-driven cyclin D1 upregulation in VHL-deficient RCC propels tumour cells through the G1 checkpoint, a hallmark of clear-cell disease."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K activation: PIK3CA mutations activate the PI3K/AKT/mTOR pathway in a subset of renal cell carcinomas, reinforcing the mTOR signalling targeted in therapy."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "TKI-resistance receptor: AXL upregulation drives resistance to VEGFR tyrosine-kinase inhibitors in RCC, which is why cabozantinib — targeting AXL and MET alongside VEGFR — outperforms pure VEGFR inhibitors in advanced disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Metastatic homing: VHL loss in RCC upregulates the CXCR4 receptor for CXCL12, directing tumour cells toward the bone, lung and brain that are the common sites of RCC metastasis."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomere maintenance: TERT promoter mutations reactivate telomerase in renal cell carcinoma, granting the replicative immortality that lets the tumour clone proliferate indefinitely."
  - target: 01-human/03-molecular/fh
    relation: connects-to
    note: "Oncometabolite RCC: germline fumarate-hydratase loss causes hereditary leiomyomatosis and renal cell cancer (HLRCC), an aggressive papillary type-2 RCC where accumulated fumarate stabilises HIF and inactivates the KEAP1-NRF2 antioxidant pathway."
  - target: 01-human/03-molecular/flcn
    relation: connects-to
    note: "Birt-Hogg-Dubé RCC: germline folliculin loss causes the Birt-Hogg-Dubé syndrome that predisposes to chromophobe renal carcinoma and hybrid oncocytic tumours, acting through dysregulated AMPK-mTOR and TFE3/TFEB signalling distinct from the VHL-HIF axis."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Progression marker: somatic CDKN2A loss, releasing the brake on the CDK4/6-cyclin-D cell cycle, is associated with sarcomatoid dedifferentiation and aggressive, poor-prognosis clear-cell renal carcinoma."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Fumarate-NRF2 axis: in fumarate-hydratase-deficient (HLRCC) renal carcinoma, accumulated fumarate succinates KEAP1 to constitutively activate NRF2, an antioxidant-response programme that fuels the aggressive growth of this hereditary RCC subtype."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: RCC recruits tumour-associated macrophages via CCL2 into an immunosuppressive, highly angiogenic stroma, complementing the VEGF-driven biology that makes it responsive to anti-angiogenic and checkpoint therapy."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "Chromatin remodelling: ARID1A and the SWI/SNF complex are recurrently mutated in clear-cell RCC alongside the 3p PBRM1/BAP1 class (BAP1 already mapped), and this chromatin dysregulation shapes the epigenetic landscape of the disease."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "Oxygen-sensing axis: EGLN1 (PHD2) hydroxylates HIF to target it for VHL-mediated degradation (VHL and EPAS1 mapped); in clear-cell RCC, VHL loss stabilises HIF-2α, the very axis the inhibitor belzutifan targets."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RTK-MAPK: MET, PDGFR and VEGFR (MET, PDGF and VEGF mapped) signal through the MAPK-ERK cascade driving proliferation and angiogenesis in renal cell carcinoma, the target of multikinase TKIs."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K restraint: PTEN limits the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped) active in renal cell carcinoma and targeted by mTOR inhibitors such as everolimus."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammatory microenvironment: IL-6-JAK-STAT signalling (IL-6 already mapped) sustains an inflammatory, immunosuppressive microenvironment in renal cell carcinoma."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint: dysregulation of the RB1-E2F checkpoint (CDKN2A and cyclin-D1 already mapped) contributes to the proliferation of renal cell carcinoma."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "Metabolic-RCC parallel: oncometabolite-producing IDH mutations parallel the FH and SDHB lesions (both already mapped) in the metabolically-driven hereditary renal cancers, where altered metabolites stabilise HIF."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is expressed in renal cell carcinoma and contributes to its invasion, metastasis and immune evasion."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-JAK-STAT3 signalling (IL-6 and JAK mapped) supports proliferation and immune modulation in renal cell carcinoma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING signalling shapes the immune microenvironment underlying the marked immunotherapy responsiveness of renal cell carcinoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling drives the antitumour immune response central to the checkpoint immunotherapy responsiveness of renal cell carcinoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the EMT and immunosuppressive microenvironment of advanced renal cell carcinoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO3 is stabilised by the pseudohypoxic, VHL-driven HIF programme of renal cell carcinoma, modulating its metabolic and survival adaptation."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells is the immune-clearance axis central to the checkpoint-immunotherapy responsiveness of renal cell carcinoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt/β-catenin signaling of renal cell carcinoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the immunosuppressive myeloid microenvironment of renal cell carcinoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of MET and AXL (both already mapped) drives the invasion of renal cell carcinoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of renal cell carcinoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival of the VHL-deficient, pseudohypoxic cells of renal cell carcinoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic reprogramming of renal cell carcinoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of renal cell carcinoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-p53 signaling participates in the cell-cycle and apoptosis control relevant to renal cell carcinoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of renal cell carcinoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of renal cell carcinoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of renal cell carcinoma."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Immunotherapy legacy: renal cell carcinoma was one of the first cancers cured in a minority by high-dose IL-2, reflecting an intrinsic immunogenicity that today underlies its strong response to checkpoint inhibitors (PD-1 already mapped)."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Osteolytic metastasis: renal cell carcinoma frequently spreads to bone as destructive lytic lesions, where tumour-driven RANKL activates osteoclasts to cause fractures and skeletal events, the rationale for denosumab in metastatic disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity risk: excess adiposity is a major modifiable risk factor for renal cell carcinoma, and the adipokine leptin, elevated in obesity, promotes tumour-cell proliferation, linking metabolic state to renal carcinogenesis."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy responsiveness: renal cell carcinoma is one of the most immunotherapy-responsive cancers, and MHC class II antigen presentation shapes the T-cell response to the checkpoint inhibitors (PD-1/CTLA-4 already mapped) that anchor its modern treatment."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Paraneoplastic blood counts: renal cell carcinoma can raise haemoglobin through ectopic erythropoietin (already mapped) causing polycythaemia, or lower it via anaemia of chronic disease, one of its characteristic paraneoplastic presentations."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Immunotherapy myocarditis: the checkpoint inhibitors central to renal cell carcinoma treatment can cause immune-mediated myocarditis, and troponin elevation helps detect this rare but often fatal adverse event."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the renal cell carcinoma microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), a mechanism of immune evasion and resistance to the checkpoint blockade central to its treatment."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with the strongly VHL-HIF-driven VEGF (already mapped) supports the rich vasculature of clear-cell renal cell carcinoma, part of the angiogenic biology targeted by the antiangiogenic tyrosine-kinase inhibitors."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: the metabolically rewired, pseudohypoxic renal cell carcinoma generates oxidative stress, to which xanthine oxidase contributes, and the NRF2 antioxidant response (already mapped) is co-opted, part of its altered redox biology."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the otherwise immunoresponsive renal cell carcinoma."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Clear-cell lipid: clear-cell renal cell carcinoma accumulates cholesterol esters and lipid, giving the clear cytoplasm that names it, and the disturbed lipid metabolism is part of the metabolically rewired biology of the VHL-HIF-driven (already mapped) tumour."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Obesity and adipokines: obesity is a major risk factor for renal cell carcinoma, and the fall in the adipokine adiponectin (leptin already mapped) is part of the metabolic milieu that promotes the tumour."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immune microenvironment of renal cell carcinoma."
  - target: 01-human/07-system/birt-hogg-dube-syndrome
    relation: connects-to
    note: "Hereditary-RCC syndromes: Birt-Hogg-Dubé (FLCN already mapped), with VHL and HLRCC (already mapped), completes the group of hereditary renal cell carcinoma syndromes causing distinct RCC subtypes requiring surveillance."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Osteolytic metastasis: renal cell carcinoma is notable for its destructive, hypervascular osteolytic bone metastases (RANKL already mapped), causing pathological fractures and requiring targeted management."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Historical immunotherapy: interferon-α was the pre-TKI/checkpoint immunotherapy of metastatic renal cell carcinoma, and the type-I interferon shapes the immunogenicity of the clear-cell tumour."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity risk (the obesity paradox) of renal cell carcinoma."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Paraneoplastic iron dysregulation: hepcidin, driven by the IL-6 (already mapped), produces the anaemia of chronic disease, while conversely the paraneoplastic erythropoietin (already mapped) causes polycythaemia in renal cell carcinoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunogenic renal cell carcinoma, exploited by the checkpoint (PD-1 already mapped) immunotherapy."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the renal-cell-carcinoma immune microenvironment."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance of the immunogenic renal cell carcinoma, complementing the T-cell (already mapped) immunotherapy."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of renal cell carcinoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of renal cell carcinoma."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the renal-cell-carcinoma microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the highly vascular renal cell carcinoma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of renal cell carcinoma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the intratumoural tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts a favourable response to the checkpoint (PD-1 already mapped) immunotherapy of renal cell carcinoma."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cancer-associated fibroblasts: the fibroblasts of the stroma remodel the extracellular matrix and shape the immune microenvironment of renal cell carcinoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Tumour complement: the complement C3, produced within the tumour, contributes to the inflammatory and immunosuppressive dimension of the renal-cell-carcinoma microenvironment."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Tumour iron: transferrin, the iron carrier, supplies the iron demand of the pseudohypoxic (HIF-1α and VHL already mapped) iron-avid renal cell carcinoma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Tumour microenvironment alarmin: TSLP released by RCC cells and the tumour stroma promotes mast-cell and DC-mediated immunosuppression, contributing to the angiogenic (VEGF already mapped) and immunologically cold microenvironment of renal cell carcinoma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell histamine: mast cells of the RCC stroma secrete histamine, promoting VEGF-driven angiogenesis and dampening the NK-cell and CD8-T-cell cytotoxicity on which immunotherapy response depends in renal cell carcinoma."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM invasion bridge: periostin, upregulated in RCC stroma and the pseudohypoxic (HIF-1α and VHL already mapped) tumour bed, promotes RCC cell invasion, bone metastasis formation and resistance to sunitinib-class therapies."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Tumour vasodilatory kinin: bradykinin generated by the kallikrein-kinin system in the RCC pseudohypoxic stroma activates B2 receptors on tumour vasculature, amplifying the VHL/HIF-1α-driven (both already mapped) angiogenesis and VEGF-driven vascular leak of RCC."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation: C1-esterase inhibitor restrains the classical complement pathway (C3 already mapped) within the RCC microenvironment, modulating the complement-driven myeloid infiltration that suppresses the checkpoint-immunotherapy (PD-1 already mapped) response."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: C5 cleavage generates C5a, which with complement C3 (already mapped) drives the myeloid and macrophage (already mapped) polarisation to an immunosuppressive phenotype in the renal-cell-carcinoma microenvironment."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "RCC melatonin: melatonin via MT1/MT2 receptors on RCC cells modulates the HIF-1α (already mapped) pseudohypoxic response and VHL (already mapped)-driven angiogenesis, and inhibits the VEGF (already mapped)-driven neovascularisation of renal-cell carcinoma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "RCC androgen axis: testosterone via androgen receptor on RCC cells modulates the mTOR (already mapped) and HIF-1α (already mapped) metabolic axes and the tumour immunosurveillance of renal-cell carcinoma, intersecting the sex-dimorphic male predominance of RCC."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "RCC serotonin: serotonin via 5-HT receptors on RCC tumour endothelium and immune infiltrate modulates the VEGF (already mapped)-driven angiogenesis and the checkpoint-immunotherapy (PD-1 already mapped) response in the renal-cell-carcinoma microenvironment."
---

# Renal Cell Carcinoma

## Overview

**Renal cell carcinoma (RCC)** is a heterogeneous group of kidney malignancies arising from the renal tubular epithelium, with **clear cell RCC (ccRCC)** accounting for ~75% of cases. The hallmark of ccRCC is biallelic inactivation of the **VHL tumor suppressor** — present in >90% of ccRCC — leading to constitutive HIF-1α/HIF-2α stabilization and a transcriptional program that drives neoangiogenesis via VEGF, PDGF, TGF-α, and EPO. This molecular dependency on HIF/VEGF has underpinned two decades of targeted therapy development: from the first VEGFR TKIs (sunitinib, 2006) through combined immunotherapy+VEGFR TKI regimens that are now standard of care in the frontline setting [^motzer-2018-checkmate214].

**Epidemiology:**
- ~81,000 new cases/year in the US; ~14,000 deaths/year; incidence rising (incidental detection on CT)
- Male:Female ~2:1; median age at diagnosis ~64 years
- 5-year survival: ~76% overall; ~93% for localized; ~15% for metastatic disease
- Risk factors: Smoking (1.5-2× risk), obesity, hypertension, occupational cadmium/trichloroethylene, analgesic nephropathy; hereditary syndromes (VHL disease, Birt-Hogg-Dubé, hereditary papillary RCC, TSC)

**RCC versus urothelial carcinoma:**
RCC arises from the renal parenchyma (tubular cells); urothelial carcinoma arises from the transitional epithelium of the renal pelvis/ureter. Both can present with hematuria but have completely different molecular biology and treatment.

## Structure

### RCC subtypes and molecular features

**Clear cell RCC (ccRCC, ~75%):**
- VHL inactivation >90%; chromosome 3p loss (VHL locus) universal
- Co-mutations: PBRM1 (~40%), BAP1 (~15%), SETD2 (~15%), KDM5C, MTOR (~5%), TP53 (~10% in sarcomatoid variant)
- Highly vascular (VEGF-driven) → VEGFR TKI-sensitive
- Sarcomatoid differentiation (~5-10%): Aggressive; TP53 mutation; PD-L1 high → especially ICI-responsive

**Papillary RCC (pRCC, ~15%):**
- Type 1: MET amplification/mutation (~80%); indolent; hereditary papillary RCC (germline MET mutation)
- Type 2: CDKN2A deletion, SETD2 mutation, CpG island methylation → fumarate hydratase (FH) mutations in hereditary leiomyomatosis and RCC (HLRCC); type 2 is more aggressive
- Fewer VEGFR TKI responders; cabozantinib (MET+VEGFR2 inhibitor) most active VEGFR TKI
- ICI active in high-grade pRCC; sunitinib inferior to ICI/cabozantinib

**Chromophobe RCC (chRCC, ~5%):**
- Monosomy of multiple chromosomes (1, 2, 6, 10, 13, 17); TP53 mutations in oncocytoma-like variants
- Birt-Hogg-Dubé (FLCN germline mutation) → multifocal chRCC/oncocytoma/hybrid tumors + lung cysts + fibrofolliculomas
- mTOR pathway activation in ~25%; generally indolent; VEGFR TKIs less effective; platinum-based in aggressive Bellini duct carcinoma (collecting duct RCC)

**Rare RCC subtypes:**
- Collecting duct (Bellini duct) carcinoma: Aggressive; cisplatin-based chemotherapy; poor prognosis
- Medullary RCC: Sickle cell trait-associated; aggressive; responds poorly to standard RCC therapies; EZH2-driven (SMARCB1 loss)
- Translocation RCC: TFE3 or TFEB fusions; ~15% of pediatric RCC; mTOR pathway activated

### IMDC risk classification (International Metastatic RCC Database Consortium)

Risk factors: Karnofsky PS <80%, time from diagnosis to systemic therapy <1 year, hemoglobin < LLN, calcium > ULN, neutrophils > ULN, platelets > ULN.
- **Favorable risk (0 factors):** Median OS ~43 months
- **Intermediate risk (1-2 factors):** Median OS ~23 months
- **Poor risk (≥3 factors):** Median OS ~7.8 months

## Function

### Normal kidney tubular biology

**Proximal tubular cells (PCT):**
Primary site of ccRCC origin. PCT reabsorbs ~67% of filtered solute; relies on oxidative phosphorylation; highly metabolically active; rich in mitochondria. VHL normally maintains oxygen homeostasis in these cells; VHL loss → pseudohypoxic state despite normal pO₂.

**Tubular-to-mesenchymal biology in ccRCC:**
ccRCC cells accumulate lipid (lipid droplets give "clear cell" appearance on H&E after lipid extraction); lipid droplets composed of cholesterol esters — driven by HIF-1α activation of lipogenic genes (FASN, ACLY); CCND1 amplification, PI3K-AKT activation cooperate with HIF → lipid-accumulating, angiogenic tumors.

**VHL-HIF in normal renal oxygen sensing:**
Kidney → primary site of EPO production under hypoxia; VHL-intact renal interstitial cells sense hypoxia → PHD inhibited → VHL cannot bind hydroxylated HIF-2α → HIF-2α stabilized → EPO transcription → erythropoiesis. RCC patients often have paraneoplastic polycythemia (excess EPO from VHL-null tumor cells).

## Pathology

### Staging and diagnosis

**TNM staging:**
- T1: ≤7 cm, confined to kidney (T1a ≤4 cm)
- T2: >7 cm, confined to kidney
- T3: Renal vein/IVC involvement or perirenal fat extension (T3a/b/c)
- T4: Beyond Gerota's fascia or invades adjacent organs
- M1: Metastatic → includes lymph node (rare hematogenous spread to lung, bone, liver, brain)

**Paraneoplastic syndromes in RCC:**
- Polycythemia: EPO secretion from tumor
- Hypercalcemia: PTHrP secretion (~5%)
- Hypertension: Renin secretion
- Stauffer syndrome (non-metastatic hepatic dysfunction): Reversible with nephrectomy
- Fever/cachexia: Cytokine (IL-6, TNF-α) secretion

**Diagnosis:**
- Incidental finding on CT (~50% of localized RCC) or presentation with hematuria, flank pain, abdominal mass (classic triad: <10% of patients)
- CT chest/abdomen/pelvis with contrast: Standard staging; RCC is hypervascular on arterial phase
- Bone scan/brain MRI: If symptomatic; ~10% brain metastasis at diagnosis
- Biopsy before systemic therapy: Recommended to confirm histology; percutaneous core biopsy under CT guidance; >95% diagnostic accuracy

**Surgical management:**
- **Partial nephrectomy:** Standard for T1a (<4 cm), favored for T1b if technically feasible; equivalent oncologic outcomes to radical nephrectomy for T1-T2; preserves renal function
- **Radical nephrectomy:** T2-T3 or technically complex tumors; laparoscopic/robotic preferred over open for most
- **Cytoreductive nephrectomy (CN):** Historical standard before targeted therapy era; CARMENA trial (2018): Sunitinib alone non-inferior to CN+sunitinib in IMDC intermediate/poor-risk; CN reserved for favorable-risk patients or symptom control
- **Metastasectomy:** Curative in select patients with solitary resectable metastasis

### Treatment

**First-line (favorable risk):**
- **Pembrolizumab + axitinib (KEYNOTE-426):** [^rini-2019-keynote426] OS and PFS benefit vs. sunitinib across all IMDC groups; FDA approved 2019; ORR 59%; OS benefit at 30 months (68% vs. 58%)
- **Sunitinib** (historically): PFS 11 months; still used in select patients; VEGFR1/2/3/PDGFR/KIT/FLT3 inhibitor; alternative to ICI-based therapy (if ICI contraindicated)

**First-line (intermediate/poor risk):**
- **Nivolumab + ipilimumab (CheckMate 214):** [^motzer-2018-checkmate214] OS 47.0 vs. 26.6 months vs. sunitinib in intermediate/poor risk; ORR 42% vs. 27%; FDA approved 2018; ~11% complete responses; 4-year OS 43% vs. 31%
- **Pembrolizumab + axitinib:** Active across risk groups; OS benefit regardless of IMDC risk
- **Nivolumab + cabozantinib (CheckMate 9ER):** PFS 16.6 vs. 8.3 months vs. sunitinib; FDA approved 2021; ORR 56%

**Second-line and beyond:**
- **Cabozantinib (CABOMETYX, METEOR trial):** VEGFR+MET+AXL+RET inhibitor; PFS 7.4 vs. 3.8 months vs. everolimus; ORR 21%; standard post-VEGFR TKI; also active after ICI (CONTACT-03 trial used as backbone)
- **Nivolumab (CheckMate 025):** OS 25 vs. 19 months vs. everolimus in 2nd-line; FDA approved 2015; first ICI in RCC; now part of 1st-line combination
- **Belzutifan (LITESPARK-005):** PFS 5.6 vs. 3.5 months vs. everolimus; ORR 22%; FDA approved 2023 for RCC after prior anti-PD-1+anti-VEGFR
- **Lenvatinib + everolimus (Study 205):** ORR 43% vs. 6% everolimus; PFS 14.6 vs. 5.5 months; 2nd-line option
- **Lenvatinib + pembrolizumab (CLEAR trial):** PFS 23.9 vs. 9.2 months vs. sunitinib; FDA approved 2021 as first-line option; ORR 71%
- **Axitinib:** 2nd/3rd-line VEGFR TKI (now primarily used with pembrolizumab in 1st line)
- **Everolimus:** mTOR inhibitor; largely supplanted; still used after 2+ TKIs or as belzutifan comparator

**Non-clear cell RCC:**
- Papillary: Cabozantinib (SWOG 1500, PAPMET) preferred VEGFR TKI; ICI combinations active
- Sarcomatoid: ICI+VEGFR TKI combinations → especially effective (ORR ~50-60% with nivo+ipi or pembro+ax in sarcomatoid component)
- Medullary/collecting duct: Platinum+gemcitabine or carboplatin+paclitaxel; experimental EZH2 inhibitors

## Connections

- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Sunitinib and pazopanib (VEGFR TKIs) were first-line RCC standards; cabozantinib (VEGFR+MET+AXL) approved 1st-line for poor/intermediate-risk (CABOSUN) and 2nd-line (METEOR); ICI+VEGFR TKI combinations (pembro+axitinib, nivo+cabo) now preferred in first-line.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Nivolumab+ipilimumab (CheckMate 214) improved OS in intermediate/poor-risk RCC; pembrolizumab+axitinib (KEYNOTE-426) improved OS vs. sunitinib; nivolumab+cabozantinib (CheckMate 9ER) PFS 16.6 vs. 8.3 months; ICI combinations are standard first-line for advanced RCC.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Everolimus (mTOR inhibitor) approved for 2nd-line RCC after VEGFR TKI failure (RECORD-1: PFS 4.9 vs. 1.9 months); temsirolimus improved OS vs. IFN-α in poor-risk RCC; lenvatinib+everolimus approved 2nd-line; mTOR inhibitors largely displaced by ICI+VEGFR combinations.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — VHL loss → constitutive HIF-1α/HIF-2α stabilization → VEGF, GLUT1, EPO, PDGF transcription in ccRCC; HIF-2α (EPAS1) is the primary oncogenic HIF isoform; belzutifan (HIF-2α inhibitor) FDA approved 2021 for VHL disease and 2023 for 3rd-line ccRCC.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Most RCCs arise from the kidney's proximal tubule; small T1a tumors are often found incidentally on CT and cured by nephron-sparing partial nephrectomy, while VHL-null tumor cells secrete EPO, renin, or PTHrP — causing paraneoplastic polycythemia, hypertension, or hypercalcemia.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — Von Hippel-Lindau disease (germline VHL loss) predisposes to bilateral, multifocal, early-onset clear-cell RCC alongside hemangioblastomas and pheochromocytomas; the same VHL→HIF-2α pseudohypoxia drives both hereditary and the >90% of sporadic ccRCC, and belzutifan targets it.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — Type 1 papillary RCC is driven by MET activation (amplification or germline mutation in hereditary papillary RCC), distinct from VHL-driven clear-cell disease; these tumors respond poorly to VEGFR TKIs, so the MET/VEGFR2 inhibitor cabozantinib is the preferred targeted agent.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Renal cell carcinoma and pheochromocytoma/paraganglioma share pseudohypoxia: VHL (or SDHx/FH) loss stabilizes HIF-2α, driving VEGF-fueled hypervascular tumors in both; VHL disease produces clear-cell RCC and PHEO together, and belzutifan (HIF-2α inhibitor) treats both.
- `connects-to` → **[Hereditary Leiomyomatosis and Renal Cell Carcinoma](../hlrcc/README.md)** — HLRCC (hereditary leiomyomatosis and RCC) is an aggressive inherited renal cancer: germline fumarate hydratase loss lets fumarate inhibit HIF prolyl-hydroxylases → pseudohypoxia like VHL ccRCC, but its type-2 papillary tumors are far more aggressive and resected when small.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Renal cell carcinoma is among the most immune-responsive solid tumors despite modest mutational burden: checkpoint inhibitors freeing cytotoxic CD8+ T cells (nivolumab+ipilimumab, pembrolizumab+axitinib) are first-line; RCC also historically responded to IL-2.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Tuberous sclerosis predisposes to renal cell carcinoma and angiomyolipoma: TSC1/TSC2 loss unleashes mTOR in the kidney, producing fat-rich angiomyolipomas and a distinctive RCC, so mTOR inhibitors (everolimus) shrink TSC renal lesions and also treat advanced sporadic RCC.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Renal cell carcinoma is a classic cause of paraneoplastic polycythemia: HIF stabilization in clear-cell RCC drives ectopic erythropoietin, expanding the red-cell mass—one of several paraneoplastic syndromes that can be the first sign of a kidney tumor.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Renal cell and bladder cancer are the two major urologic malignancies that differ in cell and cause: RCC arises from renal tubular epithelium and presents with a mass or paraneoplastic signs, while bladder cancer is a smoking-linked urothelial tumor with painless hematuria.
- `connects-to` → **[Birt-Hogg-Dubé Syndrome](../birt-hogg-dube-syndrome/README.md)** — RCC unifies several hereditary syndromes including Birt-Hogg-Dubé: BHD's FLCN loss causes chromophobe and oncocytic kidney tumors, one of the inherited RCC syndromes alongside VHL (clear cell) and HLRCC (papillary)—each gene yielding a distinct RCC histology.
- `connects-to` → **[Ovarian Clear Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — Renal clear cell carcinoma and ovarian clear-cell carcinoma share clear-cell morphology but differ in biology: RCC is VHL/HIF-driven, while ovarian clear-cell is ARID1A/PIK3CA-driven—so 'clear cell' is a convergent appearance, not a shared pathway.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Renal cell carcinoma is a classic cause of paraneoplastic polycythemia: the tumor can secrete erythropoietin, raising red-cell mass and mimicking polycythemia vera—so erythrocytosis without a JAK2 mutation warrants renal imaging to exclude an EPO-producing tumor.
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — VHL loss is the central event in clear cell RCC: inactivating the VHL tumor suppressor stabilizes HIF, driving VEGF and the angiogenic, clear-cell tumor—so both sporadic and von Hippel-Lindau-associated kidney cancers converge on this oxygen-sensing pathway.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — RCC hijacks the kidney's own erythropoietin role: the kidney normally makes EPO sensing oxygen, and VHL-mutant tumor cells, fixed in pseudohypoxia, oversecrete it—causing paraneoplastic polycythemia, a cancer co-opting an organ's native hormone.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity is a leading modifiable RCC risk factor: excess adiposity, with hypertension and chronic kidney stress, raises renal cell carcinoma risk through insulin/IGF and inflammatory signaling—making RCC one of the obesity-associated cancers.
- `connects-to` → **[BAP1](../../03-molecular/bap1/README.md)** — BAP1 loss marks an aggressive renal cell carcinoma subtype: this tumor-suppressor deletion (also seen in mesothelioma and uveal melanoma) defines high-grade clear-cell RCC with worse survival, so BAP1 status refines prognosis beyond the classic VHL/HIF pathway.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Renal cell carcinoma is the principal cancer of the renal system: it arises from the kidney's tubular epithelium and can secrete erythropoietin or renin, often presenting late with hematuria, flank pain or a mass—the kidney's own physiology becoming the tumor's traits.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Renal cell carcinoma is famously immunogenic: it can spontaneously regress and was an early success for IL-2 and now checkpoint immunotherapy, so engaging the immune system—often with anti-angiogenic drugs—is central to treating advanced RCC.
- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — Clear-cell RCC is built on the HIF-2alpha factor EPAS1: VHL loss stabilizes EPAS1, which switches on VEGF and growth genes—so the HIF-2alpha inhibitor belzutifan directly blocks this driver, a new oral therapy for VHL-related and advanced kidney cancer.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — RCC classically causes paraneoplastic hypercalcemia: tumors secrete PTH-related peptide that raises blood calcium independent of bone metastases, so unexplained hypercalcemia can be a presenting clue to an occult kidney cancer.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lungs are RCC's favorite metastatic site: kidney cancer characteristically seeds multiple round 'cannonball' lung metastases through the bloodstream, so chest imaging is essential to staging—and lung lesions are often the first sign of spread.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Kidney cancer can fake hyperparathyroidism: RCC secretes PTH-related peptide that mimics PTH, driving paraneoplastic hypercalcemia even without bone metastases—one of the syndromes that makes RCC 'the internist's tumor.'
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Kidney cancer is immunotherapy-sensitive yet shielded by regulatory T cells: RCC draws strong T-cell infiltrates that respond to checkpoint drugs, but Tregs in the tumor restrain them—so depleting Tregs is sought to deepen responses.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Kidney cancer is packed with tumor-associated macrophages: M2-polarized macrophages promote its angiogenesis and immune escape, and a macrophage-heavy infiltrate predicts worse outcomes in clear cell RCC.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Clear cell kidney cancer is the archetypal oxygen-sensing tumor: VHL loss makes it behave as if hypoxic even in normal oxygen, stabilizing HIF to pump out VEGF and EPO—the pseudohypoxia that defines it and guides anti-angiogenic therapy.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Kidney cancer is notorious for spreading to the brain: RCC seeds brain metastases through the blood, sometimes years after the primary, so new neurologic symptoms in a kidney-cancer survivor demand imaging.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are central to kidney cancer's unusual immunogenicity: RCC was one of the first tumors to respond to immunotherapy, and antigen-presenting dendritic cells help prime the T-cell attack that checkpoint drugs amplify.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Kidney cancer bleeds iron into the urine: painless hematuria is a classic sign, and the chronic blood loss drains iron into anemia—though RCC can paradoxically also raise red cells via erythropoietin.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Kidney cancer haunts the pancreas late: RCC is one of the few tumors that metastasizes to the pancreas, often many years after the kidney was removed, so long-term surveillance matters.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — RCC can drive the marrow to overproduce blood: its ectopic erythropoietin spurs the bone marrow to make excess red cells, a paraneoplastic polycythemia unusual among cancers.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons diagnose RCC without a needle: contrast-enhanced CT and MRI characterize the mass so reliably that surgery often proceeds on imaging alone, while bone and brain scans hunt the lytic metastases this cancer scatters.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — RCC reaches straight for the adrenal gland sitting atop the kidney: it invades or metastasizes to the ipsilateral adrenal so readily that the gland was once removed routinely with the kidney during radical nephrectomy.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — RCC can push platelets up: a paraneoplastic thrombocytosis driven by tumor IL-6 appears in a share of patients, and a high platelet count at diagnosis is a marker of more aggressive disease and worse survival.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — The 'clear' in clear-cell RCC is an artifact of its lipids: the cytoplasm is stuffed with glycogen and fat that dissolve away in processing, leaving the empty-looking cells that electron microscopy and histology use to recognize the commonest RCC.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — RCC can derange the liver without touching it: Stauffer syndrome is a paraneoplastic hepatic dysfunction — raised enzymes and cholestasis with no metastases — driven by tumor cytokines and reversing once the kidney cancer is removed.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — RCC can wash out the blood's sodium: paraneoplastic hyponatremia, from tumor-driven ADH or cytokines, is common in advanced disease and flags a poorer prognosis, sometimes correcting after the tumor is treated.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both label and treat RCC: PAX8, CD10, and CA-IX stains confirm renal origin on biopsy, and the disease is now driven by antibody therapy — anti-PD-1 checkpoint blockade and anti-VEGF agents that exploit its rich, VHL-driven vasculature.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The blood count carries the prognosis: RCC drives a paraneoplastic leukocytosis and a high neutrophil-to-lymphocyte ratio that predicts worse survival, a marker built into the risk models that guide its targeted and immune therapies.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — RCC and its treatment both raise the pressure: the tumor can secrete renin to drive paraneoplastic hypertension, and the anti-VEGF tyrosine-kinase inhibitors used against it cause hypertension so reliably it serves as a marker that the drug is working.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — A sudden left varicocele can betray a kidney tumor: a left RCC invading the renal vein blocks the gonadal vein that drains into it, so a new, non-decompressing left varicocele in a man warrants imaging of the kidney.
- `connects-to` → **[SDHB](../../03-molecular/sdhb/README.md)** — RCC has a rare metabolic-gene form: germline SDHB and related succinate-dehydrogenase mutations cause a hereditary renal cell carcinoma alongside paraganglioma, the same pseudohypoxic pathway that drives the FH-deficient and VHL kidney cancers.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — RCC can climb into the heart: its tumor thrombus grows up the renal vein and inferior vena cava, sometimes reaching the right atrium against the cardiomyocytes — while the TKIs treating it add their own cardiotoxic strain.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Its pseudohypoxic drive feeds more than VEGF: VHL loss also raises PDGF, so the tyrosine-kinase inhibitors used against RCC block PDGF receptors alongside VEGFR to starve the tumor's abundant blood supply.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — RCC is unusually immune-responsive: combining CTLA-4 blockade with anti-PD-1 unleashes T cells against the tumor and is now frontline for advanced disease, making this one of the cancers most transformed by checkpoint immunotherapy.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Diseased kidneys breed cancer: long-standing chronic kidney disease and the acquired cystic change of dialysis sharply raise RCC risk, while removing a tumor-bearing kidney can in turn push remaining function toward chronic kidney disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — RCC is one of the most vascular of tumors: VHL loss floods it with VEGF, recruiting endothelial cells into a dense blood supply that makes the tumor highly enhancing on imaging and exquisitely sensitive to anti-angiogenic drugs.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Beyond its tumor thrombus, RCC clots the blood: it carries a high rate of bland venous thromboembolism (Trousseau), so deep-vein thrombosis and pulmonary embolism complicate the disease and its surgery.
- `connects-to` → **[Stroke](../stroke/README.md)** — The kidney tumor can reach the brain: RCC's hypercoagulable state, and rarely tumor embolism from IVC extension through a patent foramen, can cause ischemic stroke alongside its frequent brain metastases.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — It is a classic IL-6-producing tumor: RCC secretes IL-6, driving a paraneoplastic constitutional syndrome of fever, weight loss and raised inflammatory markers, plus Stauffer's non-metastatic hepatic dysfunction.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Despite an EPO-making kidney, the marrow can lag: the IL-6 and inflammation of RCC raise hepcidin and suppress erythropoiesis, so an anemia of chronic disease is common and paradoxically coexists with the EPO-driven polycythemia in others.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Surgery and immunotherapy open the door: major nephrectomy in often older patients and the immune perturbations of checkpoint-inhibitor therapy leave advanced-RCC patients vulnerable to serious infection and sepsis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anti-angiogenic TKIs strain the heart: sunitinib, pazopanib and other VEGF-pathway inhibitors central to RCC therapy raise blood pressure and are directly cardiotoxic, capable of precipitating heart failure.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Checkpoint immunotherapy can trigger autoimmune diabetes: the PD-1 and CTLA-4 inhibitors used for advanced RCC occasionally unleash autoimmunity against pancreatic islets, causing fulminant insulin-dependent diabetes.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An advanced cancer and its immunotherapy weigh on mood: the diagnosis, prolonged systemic therapy and the fatigue and inflammatory burden of metastatic RCC contribute to substantial depression and anxiety.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Surgery and anti-VEGF therapy heal poorly: nephrectomy is the mainstay for localised RCC, and the VEGF-targeted tyrosine-kinase inhibitors used for advanced disease impair angiogenesis, delaying wound closure.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Checkpoint immunotherapy can inflame the gut: the PD-1 and CTLA-4 inhibitors used for advanced RCC frequently trigger immune-related colitis with diarrhoea, a characteristic toxicity needing steroids.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A metastatic cancer watched scan-to-scan breeds worry: the recurrence risk, prolonged targeted and immune therapy and uncertain prognosis of advanced RCC foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It seeds the lungs with cannonballs: renal cell carcinoma metastasises classically to the lungs as multiple round 'cannonball' nodules, a defining pattern of its distant spread.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is a great paraneoplastic mimic: RCC secretes PTHrP causing hypercalcaemia, erythropoietin causing polycythaemia and renin causing hypertension, and its immunotherapy triggers endocrine irAEs.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It carves holes in bone: renal cell carcinoma metastasises to the skeleton as destructive, hypervascular osteolytic lesions that cause pain, fractures and spinal cord compression.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It grows up into the great veins: renal cell carcinoma characteristically forms a tumour thrombus that extends up the renal vein and inferior vena cava, sometimes reaching the right atrium.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It reaches the brain: renal cell carcinoma metastasises to the brain as vascular deposits prone to bleeding, and spinal metastases can compress the cord.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It spreads to the nodes: regional and retroperitoneal lymph-node involvement is a poor prognostic factor in renal cell carcinoma and guides surgical and systemic treatment.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It is a prototype of targeted and immune therapy: anti-VEGF tyrosine-kinase inhibitors, mTOR inhibitors and checkpoint immunotherapy define modern treatment of advanced renal cell carcinoma.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Another hereditary kidney-cancer syndrome: like von Hippel-Lindau and Birt-Hogg-Dubé, Cowden (PTEN) syndrome raises renal cell carcinoma risk, part of its inherited differential.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Renal tuberculosis can mimic it: genitourinary TB causes renal masses, cavitation and haematuria that enter the imaging differential of renal cell carcinoma.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — A highly immunogenic tumour: clear-cell RCC responds to checkpoint blockade — nivolumab plus ipilimumab or pembrolizumab with a VEGF TKI is now first-line for advanced disease, exploiting its heavy immune infiltrate.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Classically chemoresistant: conventional cytotoxic chemotherapy barely touches renal cell carcinoma owing to high P-glycoprotein drug efflux, which is why treatment moved to cytokines, then VEGF TKIs and immunotherapy.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It seeds destructive bone metastases: RCC frequently spreads to bone as hypervascular osteolytic lesions causing pain and pathological fractures that can bleed briskly, sometimes needing embolisation before surgery.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — Two BAP1-spectrum cancers: germline BAP1 loss predisposes to clear cell renal carcinoma alongside mesothelioma and uveal melanoma, so a BAP1 family history links a kidney cancer to a pleural one.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — It can grow into the heart: renal cell carcinoma characteristically extends as a tumour thrombus up the renal vein and inferior vena cava, sometimes reaching the right atrial endocardium and demanding cardiac surgery to remove.
- `connects-to` → **[HCC](../hcc/README.md)** — Twin hypervascular, antiangiogenic-treated cancers: renal cell carcinoma and hepatocellular carcinoma are both richly vascular tumours driven by VEGF, treated with multikinase angiogenesis inhibitors (sorafenib, lenvatinib) and now immunotherapy combinations.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Cannonball lung metastases: RCC characteristically produces large, round 'cannonball' pulmonary metastases, seeding the alveolar bed—the lung being its commonest distant site.
- `connects-to` → **[Wilms Tumor](../wilms-tumor/README.md)** — Two renal cancers, two ages: RCC is the adult kidney cancer arising from tubular epithelium (VHL/MET), while Wilms tumour is the childhood nephroblastoma (WT1)—the renal cancers across the lifespan.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver metastasis: beyond the lung, RCC seeds the liver, depositing in the hepatic lobule, a poor-prognosis site of distant spread.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Immunotherapy's autoimmune cost: the checkpoint inhibitors central to advanced renal cell carcinoma treatment can unleash an autoimmune colitis closely resembling inflammatory bowel disease, managed with steroids and anti-TNF biologics.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — A hypervascular tumour: VHL/HIF/VEGF make renal cell carcinoma intensely angiogenic, underlying preoperative embolization, antiangiogenic TKIs, and its hallmark growth as a tumour thrombus up the renal vein and IVC.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — The immunotherapy-responsive pair: renal cell carcinoma and melanoma were the first solid tumours to respond to high-dose IL-2 and then checkpoint blockade, sharing an unusual immunogenicity and even spontaneous regression.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — Paraneoplastic hypertension: some renal cell carcinomas secrete renin, causing hypertension and hypokalaemia—a hormonal syndrome distinct from the erythropoietin-driven polycythaemia they can also produce.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-mTOR axis: PI3K-AKT-mTOR signalling drives renal cell carcinoma, the target of mTOR inhibitors such as everolimus and temsirolimus in advanced disease.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Chromatin dysregulation: EZH2/polycomb activity, in the context of PBRM1 and BAP1 chromatin-remodeller loss, contributes to clear-cell renal carcinoma progression.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Metabolic-oncogene cooperation: the pseudohypoxic, HIF-driven state of clear-cell RCC upregulates MYC, fuelling the biosynthesis and proliferation of the tumour.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — HIF target and cell cycle: HIF-driven cyclin D1 upregulation in VHL-deficient RCC propels tumour cells through the G1 checkpoint, a hallmark of clear-cell disease.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K activation: PIK3CA mutations activate the PI3K/AKT/mTOR pathway in a subset of renal cell carcinomas, reinforcing the mTOR signalling targeted in therapy.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — AXL upregulation drives resistance to VEGFR tyrosine-kinase inhibitors in RCC, which is why cabozantinib—targeting AXL and MET alongside VEGFR—outperforms pure VEGFR inhibitors in advanced clear-cell disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — VHL loss in RCC upregulates the CXCR4 receptor for CXCL12, directing tumor cells toward the bone, lung, and brain that are the characteristic sites of RCC metastasis—linking the founding genetic lesion to the metastatic pattern.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutations reactivate telomerase in renal cell carcinoma, granting the replicative immortality that lets the tumor clone proliferate indefinitely past the telomere-attrition limit that constrains normal cells.
- `connects-to` → **[FH](../../03-molecular/fh/README.md)** — Germline fumarate-hydratase loss causes hereditary leiomyomatosis and renal cell cancer (HLRCC), an aggressive papillary type-2 RCC where accumulated fumarate stabilizes HIF and inactivates the KEAP1-NRF2 antioxidant pathway.
- `connects-to` → **[FLCN](../../03-molecular/flcn/README.md)** — Germline folliculin loss causes Birt-Hogg-Dubé syndrome, predisposing to chromophobe renal carcinoma and hybrid oncocytic tumors through dysregulated AMPK-mTOR and TFE3/TFEB signaling distinct from the VHL-HIF axis.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Somatic CDKN2A loss, releasing the brake on the CDK4/6-cyclin-D cell cycle, is associated with sarcomatoid dedifferentiation and aggressive, poor-prognosis clear-cell renal carcinoma.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — In fumarate-hydratase-deficient (HLRCC) renal carcinoma, accumulated fumarate succinates KEAP1 to constitutively activate NRF2, an antioxidant-response program that fuels the aggressive growth of this hereditary RCC subtype.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — RCC recruits tumor-associated macrophages via CCL2 into an immunosuppressive, highly angiogenic stroma, complementing the VEGF-driven biology that makes it responsive to anti-angiogenic and checkpoint therapy.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A and the SWI/SNF complex are recurrently mutated in clear-cell RCC alongside the 3p PBRM1/BAP1 class (BAP1 already mapped), and this chromatin dysregulation shapes the epigenetic landscape of the disease.
- `connects-to` → **[EGLN1](../../03-molecular/egln1/README.md)** — EGLN1 (PHD2) hydroxylates HIF to target it for VHL-mediated degradation (VHL and EPAS1 mapped); in clear-cell RCC, VHL loss stabilizes HIF-2α, the very axis the inhibitor belzutifan targets.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MET, PDGFR and VEGFR (MET, PDGF and VEGF mapped) signal through the MAPK-ERK cascade driving proliferation and angiogenesis in renal cell carcinoma, the target of multikinase TKIs.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN limits the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped) active in renal cell carcinoma and targeted by mTOR inhibitors such as everolimus.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT signaling (IL-6 already mapped) sustains an inflammatory, immunosuppressive microenvironment in renal cell carcinoma.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (CDKN2A and cyclin-D1 already mapped) contributes to the proliferation of renal cell carcinoma.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — Oncometabolite-producing IDH mutations parallel the FH and SDHB lesions (both already mapped) in the metabolically-driven hereditary renal cancers, where altered metabolites stabilize HIF.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is expressed in renal cell carcinoma and contributes to its invasion, metastasis and immune evasion.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and JAK mapped) supports proliferation and immune modulation in renal cell carcinoma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — cGAS-STING signaling shapes the immune microenvironment underlying the marked immunotherapy responsiveness of renal cell carcinoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling drives the antitumor immune response central to the checkpoint immunotherapy responsiveness of renal cell carcinoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the EMT and immunosuppressive microenvironment of advanced renal cell carcinoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO3 is stabilized by the pseudohypoxic, VHL-driven HIF program of renal cell carcinoma, modulating its metabolic and survival adaptation.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells is the immune-clearance axis central to the checkpoint-immunotherapy responsiveness of renal cell carcinoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt/β-catenin signaling of renal cell carcinoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the immunosuppressive myeloid microenvironment of renal cell carcinoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of MET and AXL (both already mapped) drives the invasion of renal cell carcinoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of renal cell carcinoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival of the VHL-deficient, pseudohypoxic cells of renal cell carcinoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic reprogramming of renal cell carcinoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of renal cell carcinoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-p53 signaling participates in the cell-cycle and apoptosis control relevant to renal cell carcinoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of renal cell carcinoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of renal cell carcinoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of renal cell carcinoma.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Immunotherapy legacy: renal cell carcinoma was one of the first cancers cured in a minority by high-dose IL-2, reflecting an intrinsic immunogenicity that today underlies its strong response to checkpoint inhibitors (PD-1 already mapped).
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Osteolytic metastasis: renal cell carcinoma frequently spreads to bone as destructive lytic lesions, where tumour-driven RANKL activates osteoclasts to cause fractures and skeletal events, the rationale for denosumab in metastatic disease.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity risk: excess adiposity is a major modifiable risk factor for renal cell carcinoma, and the adipokine leptin, elevated in obesity, promotes tumour-cell proliferation, linking metabolic state to renal carcinogenesis.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy responsiveness: renal cell carcinoma is one of the most immunotherapy-responsive cancers, and MHC class II antigen presentation shapes the T-cell response to the checkpoint inhibitors (PD-1/CTLA-4 already mapped) that anchor its modern treatment.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Paraneoplastic blood counts: renal cell carcinoma can raise haemoglobin through ectopic erythropoietin (already mapped) causing polycythaemia, or lower it via anaemia of chronic disease, one of its characteristic paraneoplastic presentations.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Immunotherapy myocarditis: the checkpoint inhibitors central to renal cell carcinoma treatment can cause immune-mediated myocarditis, and troponin elevation helps detect this rare but often fatal adverse event.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the renal cell carcinoma microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), a mechanism of immune evasion and resistance to the checkpoint blockade central to its treatment.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with the strongly VHL-HIF-driven VEGF (already mapped) supports the rich vasculature of clear-cell renal cell carcinoma, part of the angiogenic biology targeted by the antiangiogenic tyrosine-kinase inhibitors.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: the metabolically rewired, pseudohypoxic renal cell carcinoma generates oxidative stress, to which xanthine oxidase contributes, and the NRF2 antioxidant response (already mapped) is co-opted, part of its altered redox biology.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the otherwise immunoresponsive renal cell carcinoma.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Clear-cell lipid: clear-cell renal cell carcinoma accumulates cholesterol esters and lipid, giving the clear cytoplasm that names it, and the disturbed lipid metabolism is part of the metabolically rewired biology of the VHL-HIF-driven (already mapped) tumour.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Obesity and adipokines: obesity is a major risk factor for renal cell carcinoma, and the fall in the adipokine adiponectin (leptin already mapped) is part of the metabolic milieu that promotes the tumour.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immune microenvironment of renal cell carcinoma.
- `connects-to` → **[Birt-Hogg-Dubé syndrome](../birt-hogg-dube-syndrome/README.md)** — Hereditary-RCC syndromes: Birt-Hogg-Dubé (FLCN already mapped), with VHL and HLRCC (already mapped), completes the group of hereditary renal cell carcinoma syndromes causing distinct RCC subtypes requiring surveillance.
- `connects-to` → **[Cortical bone](../../05-tissue/cortical-bone/README.md)** — Osteolytic metastasis: renal cell carcinoma is notable for its destructive, hypervascular osteolytic bone metastases (RANKL already mapped), causing pathological fractures and requiring targeted management.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Historical immunotherapy: interferon-α was the pre-TKI/checkpoint immunotherapy of metastatic renal cell carcinoma, and the type-I interferon shapes the immunogenicity of the clear-cell tumour.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity risk (the obesity paradox) of renal cell carcinoma.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Paraneoplastic iron dysregulation: hepcidin, driven by the IL-6 (already mapped), produces the anaemia of chronic disease, while conversely the paraneoplastic erythropoietin (already mapped) causes polycythaemia in renal cell carcinoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunogenic renal cell carcinoma, exploited by the checkpoint (PD-1 already mapped) immunotherapy.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the renal-cell-carcinoma immune microenvironment.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — NK surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance of the immunogenic renal cell carcinoma, complementing the T-cell (already mapped) immunotherapy.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of renal cell carcinoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of renal cell carcinoma.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the renal-cell-carcinoma microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the highly vascular renal cell carcinoma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of renal cell carcinoma.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the intratumoural tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts a favourable response to the checkpoint (PD-1 already mapped) immunotherapy of renal cell carcinoma.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cancer-associated fibroblasts: the fibroblasts of the stroma remodel the extracellular matrix and shape the immune microenvironment of renal cell carcinoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Tumour complement: the complement C3, produced within the tumour, contributes to the inflammatory and immunosuppressive dimension of the renal-cell-carcinoma microenvironment.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Tumour iron: transferrin, the iron carrier, supplies the iron demand of the pseudohypoxic (HIF-1α and VHL already mapped) iron-avid renal cell carcinoma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Tumour microenvironment alarmin: TSLP released by RCC cells and the tumour stroma promotes mast-cell and DC-mediated immunosuppression, contributing to the angiogenic (VEGF already mapped) and immunologically cold microenvironment of renal cell carcinoma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell histamine: mast cells of the RCC stroma secrete histamine, promoting VEGF-driven angiogenesis and dampening the NK-cell and CD8-T-cell cytotoxicity on which immunotherapy response depends in renal cell carcinoma.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM invasion bridge: periostin, upregulated in RCC stroma and the pseudohypoxic (HIF-1α and VHL already mapped) tumour bed, promotes RCC cell invasion, bone metastasis formation and resistance to sunitinib-class therapies.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Tumour vasodilatory kinin: bradykinin generated by the kallikrein-kinin system in the RCC pseudohypoxic stroma activates B2 receptors on tumour vasculature, amplifying the VHL/HIF-1α-driven (both already mapped) angiogenesis and VEGF-driven vascular leak of RCC.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation: C1-esterase inhibitor restrains the classical complement pathway (C3 already mapped) within the RCC microenvironment, modulating the complement-driven myeloid infiltration that suppresses the checkpoint-immunotherapy (PD-1 already mapped) response.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: C5 cleavage generates C5a, which with complement C3 (already mapped) drives the myeloid and macrophage (already mapped) polarisation to an immunosuppressive phenotype in the renal-cell-carcinoma microenvironment.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — RCC melatonin: melatonin via MT1/MT2 receptors on RCC cells modulates the HIF-1α (already mapped) pseudohypoxic response and VHL (already mapped)-driven angiogenesis, and inhibits the VEGF (already mapped)-driven neovascularisation of renal-cell carcinoma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — RCC androgen axis: testosterone via androgen receptor on RCC cells modulates the mTOR (already mapped) and HIF-1α (already mapped) metabolic axes and the tumour immunosurveillance of renal-cell carcinoma, intersecting the sex-dimorphic male predominance of RCC.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — RCC serotonin: serotonin via 5-HT receptors on RCC tumour endothelium and immune infiltrate modulates the VEGF (already mapped)-driven angiogenesis and the checkpoint-immunotherapy (PD-1 already mapped) response in the renal-cell-carcinoma microenvironment.

[^motzer-2018-checkmate214]: Motzer RJ, Tannir NM, McDermott DF, et al. Nivolumab plus ipilimumab versus sunitinib in advanced renal-cell carcinoma. *N Engl J Med.* 2018;378(14):1277-1290. [doi:10.1056/NEJMoa1712126](https://doi.org/10.1056/NEJMoa1712126) · [PubMed 29562145](https://pubmed.ncbi.nlm.nih.gov/29562145/)
[^rini-2019-keynote426]: Rini BI, Plimack ER, Stus V, et al. Pembrolizumab plus axitinib versus sunitinib for advanced renal-cell carcinoma. *N Engl J Med.* 2019;380(12):1116-1127. [doi:10.1056/NEJMoa1816714](https://doi.org/10.1056/NEJMoa1816714) · [PubMed 30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/)
