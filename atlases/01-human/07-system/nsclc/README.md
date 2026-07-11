---
schema: human-scale-entry/v1
id: nsclc
name: NSCLC
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common lung cancer subtype (~85%); adenocarcinoma (KRAS/EGFR/ALK drivers), squamous cell carcinoma, and large cell. EGFR TKIs (osimertinib) and ALK inhibitors (alectinib) are highly active; pembrolizumab + chemotherapy transforms KRAS/squamous disease."
aliases: ["non-small cell lung cancer", "lung adenocarcinoma", "squamous cell lung carcinoma", "LUAD", "LUSC", "lung cancer", "NSCLC adenocarcinoma"]
sources:
  - id: soria-2018-osimertinib-flaura
    type: peer-reviewed
    cite: "Soria JC, Ohe Y, Vansteenkiste J, et al. Osimertinib in untreated EGFR-mutated advanced non-small-cell lung cancer. N Engl J Med. 2018;378(2):113-125."
    doi: "10.1056/NEJMoa1713137"
    pmid: "29151359"
    url: "https://doi.org/10.1056/NEJMoa1713137"
  - id: reck-2016-pembrolizumab-keynote024
    type: peer-reviewed
    cite: "Reck M, Rodríguez-Abreu D, Robinson AG, et al. Pembrolizumab versus chemotherapy for PD-L1-positive non-small-cell lung cancer. N Engl J Med. 2016;375(19):1823-1833."
    doi: "10.1056/NEJMoa1606774"
    pmid: "27718347"
    url: "https://doi.org/10.1056/NEJMoa1606774"
  - id: halliday-2023-kras-nsclc
    type: peer-reviewed
    cite: "Riely GJ, Ou SHI, Rybkin I, et al. KRYSTAL-1: activity and preliminary pharmacodynamic (PD) analysis of adagrasib (MRTX849) in patients (Pts) with advanced/metastatic non-small cell lung cancer (NSCLC) harboring KRASG12C mutation. J Thorac Oncol. 2022;17(10):1248-1258."
    doi: "10.1016/j.jtho.2022.06.020"
    pmid: "35817313"
    url: "https://doi.org/10.1016/j.jtho.2022.06.020"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS G12C is the most common oncogenic driver in NSCLC adenocarcinoma (~13%); sotorasib (CodeBreaK-100) and adagrasib (KRYSTAL-1) are approved for KRAS G12C-mutant NSCLC; KRAS G12D and G12V — next-generation pan-KRAS and T cell-engaging approaches in clinical development."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR mutations (exon 19 del, L858R) drive 15-20% of NSCLC adenocarcinoma; osimertinib (FLAURA: PFS 18.9 vs. 10.2 months vs. erlotinib) is first-line; resistance via C797S and MET amplification; exon 20 insertions → amivantamab + lazertinib."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E occurs in ~2% of NSCLC adenocarcinoma; dabrafenib + trametinib (BRAF + MEK inhibition) approved for BRAF V600E-mutant NSCLC (ORR ~64%, PFS 14.6 months); non-V600E BRAF mutations require pan-RAF or ERK-directed approaches."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1/PD-L1 blockade transformed NSCLC: pembrolizumab is standard-of-care in PD-L1 ≥50% first-line (KEYNOTE-024: OS 26.3 vs. 13.8 months) and + chemotherapy in all-comers (KEYNOTE-189); atezolizumab, nivolumab, and durvalumab (post-CRT consolidation) are also approved."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "NSCLC is ~85% of lung cancer: squamous tumors arise centrally near the hilum (cough, hemoptysis) while adenocarcinomas arise peripherally and are often found incidentally; annual low-dose CT screening of heavy smokers cuts lung-cancer mortality ~20% (NLST)."
  - target: 01-human/03-molecular/alk
    relation: connects-to
    note: "ALK rearrangements (EML4-ALK, ~5-7%) define a distinct NSCLC of young never-smokers that is exquisitely targetable: alectinib and lorlatinib far outperform chemotherapy with strong CNS penetration for brain metastases; lorlatinib covers the G1202R resistance mutation."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "Lung adenocarcinoma arises from alveolar type II pneumocytes (and club cells), retaining their TTF-1 and napsin-A markers; it progresses through adenocarcinoma-in-situ → minimally invasive → invasive adenocarcinoma, the peripheral lepidic-to-solid sequence."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "NSCLC and melanoma are the twin proving grounds of checkpoint immunotherapy: both accumulate heavy carcinogen-driven mutational burdens (tobacco, UV) yielding neoantigens, so PD-1/PD-L1 (and CTLA-4) blockade gives durable responses in both, and both carry targetable BRAF V600E."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "NSCLC's response to immunotherapy hinges on cytotoxic T cells: a high tobacco-driven mutational burden generates neoantigens, and PD-1/PD-L1 blockade (pembrolizumab, first-line at PD-L1 ≥50%) reinvigorates exhausted CD8+ T cells — absent in never-smoker EGFR/ALK subsets."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "NSCLC and small-cell lung cancer are the two divisions of lung cancer: NSCLC (~85%, adeno/squamous) is driver-rich and often resectable or targetable, while SCLC is a fast neuroendocrine tumor of heavy smokers that disseminates early, is rarely operable, and is RB1/TP53-driven."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "NSCLC and mesothelioma are the two major thoracic cancers tied to inhaled carcinogens but distinct: NSCLC arises in lung parenchyma (smoking, EGFR/KRAS-driven), while mesothelioma arises from the pleura decades after asbestos exposure—different cells and treatment."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is central to NSCLC: stereotactic body photon radiotherapy can cure inoperable early-stage tumors, while conventional chemoradiation treats locally advanced disease—and consolidation immunotherapy after radiation now improves survival."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages shape the NSCLC microenvironment: M2-polarized macrophages suppress cytotoxic T cells and promote angiogenesis, contributing to immunotherapy resistance—so they are studied as both a biomarker and a target alongside PD-1 blockade."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain is a frequent NSCLC metastatic site: lung adenocarcinomas, especially EGFR/ALK-driven, commonly seed the brain, so staging includes brain MRI and CNS-penetrant targeted drugs (osimertinib, lorlatinib)—brain metastases strongly shape prognosis."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Carbon-based tobacco carcinogens are the dominant cause of NSCLC: smoke's PAHs and nitrosamines form DNA adducts that mutate KRAS and TP53, driving most squamous and many adenocarcinomas—though EGFR-mutant adenocarcinoma in never-smokers takes a distinct path."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "NSCLC and head and neck cancer share tobacco-driven field cancerization: carcinogens injure the whole aerodigestive tract, so smokers with one cancer face high risk of a second primary in the other—both demand smoking cessation and surveillance."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "MET is a targetable NSCLC driver: MET exon-14 skipping mutations and MET amplification drive a subset of non-small-cell lung cancers and confer resistance to EGFR inhibitors, so MET-directed drugs extend the precision-oncology toolkit beyond EGFR, ALK and KRAS."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal gland is a classic NSCLC metastatic site: lung cancer characteristically spreads to the adrenals (along with brain, bone and liver), so an adrenal mass in a lung-cancer patient demands staging workup—adrenal involvement often marks stage IV disease."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "NSCLC and COPD are linked by shared tobacco injury: smoking drives both, COPD independently raises lung-cancer risk through chronic inflammation, and the two coexist so often that emphysema complicates surgery and screening targets this overlapping high-risk population."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 is among the most mutated genes in NSCLC: smoking-driven DNA damage frequently inactivates p53, removing a key brake on the cell cycle and apoptosis, so its loss—often alongside KRAS—marks aggressive, treatment-resistant lung adenocarcinoma."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "NSCLC is the dominant cancer of the respiratory system: arising in bronchial and alveolar cells mostly from smoking, it accounts for ~85% of lung cancers and destroys lung function as it grows—the leading cause of cancer death worldwide."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "NSCLC staging hinges on the lymphatic system: spread to hilar and mediastinal lymph nodes (the N stage) determines whether disease is surgically curable, so nodal sampling by EBUS or mediastinoscopy is decisive in planning treatment."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Liver metastases worsen lung-cancer outlook: NSCLC commonly spreads to the liver, which carries a poorer prognosis and historically blunts the benefit of immunotherapy, so liver involvement shapes both staging and treatment expectations."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "NSCLC immunotherapy can pair two checkpoints: adding anti-CTLA-4 (ipilimumab) to anti-PD-1 therapy gives durable responses in some patients, an option especially when chemotherapy is undesirable—broadening immunotherapy beyond PD-1 blockade alone."
  - target: 01-human/03-molecular/ret
    relation: connects-to
    note: "A subset of NSCLC is driven by RET fusions: these rearrangements switch on RET kinase, and selective inhibitors like selpercatinib produce strong responses, so guidelines include RET in the molecular panel run on every lung adenocarcinoma."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Squamous lung cancers often hijack NRF2: KEAP1/NRF2 mutations switch on a permanent antioxidant program that shields the tumor from oxidative stress and chemo/radiation, marking an aggressive, treatment-resistant subset of NSCLC."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "NSCLC evades immunity with regulatory T cells: Tregs accumulate in the tumor and suppress the cytotoxic response, blunting the PD-1 checkpoint therapy that has transformed lung cancer treatment—so depleting them is a goal."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "NSCLC is shaped by cancer-associated fibroblasts: they build a stiff, desmoplastic stroma that secretes growth factors, promotes invasion, and shields tumor cells from drugs, making the fibroblast-rich niche a driver of resistance."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia hardens NSCLC against treatment: oxygen-starved tumor regions resist radiation, which needs oxygen to fix DNA damage, and they drive an aggressive, metastatic phenotype—so tumor hypoxia is both a prognostic marker and a therapeutic obstacle."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "NSCLC recruits its blood supply through VEGF: the tumor secretes this angiogenesis driver to grow and spread, so anti-VEGF bevacizumab is combined with chemotherapy and immunotherapy in eligible non-squamous lung cancers."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells decide how well NSCLC immunotherapy works: by presenting tumor antigens they prime the T cells that PD-1 blockade unleashes, so their function in the tumor shapes response to the checkpoint drugs central to lung-cancer care."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Squamous lung cancer can spike blood calcium: it secretes PTHrP that mimics parathyroid hormone, pulling calcium from bone into the blood—a paraneoplastic hypercalcemia causing confusion, thirst, and kidney injury."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "NSCLC can invade the heart's lining: a nearby tumor may breach the pericardium, filling it with malignant fluid that compresses the heart (tamponade), a dangerous complication of advanced lung cancer."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "NSCLC can grow out of lung fibrosis: adenocarcinomas may arise in scarred lung ('scar carcinoma'), and the tumor's own desmoplastic stroma stiffens the surrounding tissue."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy separates NSCLC's faces: adenocarcinoma shows microvilli and lamellar bodies betraying pneumocyte origin, while squamous cell carcinoma reveals desmosomes and bundled tonofilaments of keratin — ultrastructure that resolved subtype before immunostains."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "NSCLC favors the skeleton when it spreads: bone is among its commonest metastatic sites, and deposits reaching the marrow can crowd out blood production, causing the anemia and low counts that signal advanced disease."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "NSCLC pushes platelets up and clots out: paraneoplastic thrombocytosis is common, tumor-driven hypercoagulability makes lung cancer a leading cause of cancer-associated thrombosis, and a high platelet count tracks with worse outcomes."
  - target: 01-human/03-molecular/stk11
    relation: connects-to
    note: "STK11/LKB1 loss makes a cold tumor: this tumor suppressor is among the most frequently inactivated genes in lung adenocarcinoma, and its loss — especially alongside KRAS — predicts an immune-excluded tumor that resists checkpoint inhibitors."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "NSCLC eats into bone: skeletal metastases are common and osteolytic, with tumor-driven RANKL revving up osteoclasts to dissolve bone — causing pain, fractures, and hypercalcemia, and making osteoclast-blocking denosumab part of supportive care."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils foretell the course in NSCLC: a high neutrophil-to-lymphocyte ratio is a robust poor-prognosis marker, and tumor-associated neutrophils help build the immunosuppressive niche that lets the cancer grow."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies steer modern NSCLC care: TTF-1 and p40 stains separate adeno from squamous, PD-L1 staining selects who gets checkpoint therapy, and the drugs themselves — anti-PD-1 pembrolizumab and anti-VEGF bevacizumab — are monoclonal antibodies."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney sets limits on treatment: the cisplatin backbone of NSCLC chemotherapy is nephrotoxic, demanding hydration and dose adjustment, and the tumor can drive a paraneoplastic SIADH that drops sodium dangerously low."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Cisplatin wastes the body's magnesium: by injuring the kidney tubule that reclaims it, the platinum chemotherapy for NSCLC drops magnesium and potassium, electrolytes that must be replaced through every cycle of treatment."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Lung adenocarcinoma is among the most clot-prone cancers: tumor tissue factor and chemotherapy combine to drive deep-vein thrombosis and pulmonary embolism, a frequent complication that worsens outcomes and often needs anticoagulation."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Immunotherapy can inflame the thyroid: the checkpoint inhibitors central to modern NSCLC treatment commonly trigger autoimmune thyroiditis, causing transient hyperthyroidism then lasting hypothyroidism — one of the most frequent immune-related side effects."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "A rare but lethal immune side effect strikes the heart muscle: checkpoint-inhibitor myocarditis floods the myocardium with T cells attacking cardiomyocytes, an uncommon complication of NSCLC immunotherapy with a high fatality rate demanding urgent steroids."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "Another driver joins the targetable list: HER2 mutations and amplification power a subset of lung adenocarcinomas, now hit by antibody-drug conjugates like trastuzumab deruxtecan, extending the precision-oncology approach beyond EGFR and ALK."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "The tumor reawakens its immortality switch: TERT promoter activation restores telomerase so NSCLC cells escape the telomere erosion that limits normal divisions, a common step that lets the smoking-damaged epithelium keep proliferating."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Adenocarcinoma grows from the gas-exchange lining: NSCLC's most common subtype arises in the peripheral alveoli, spreading along the delicate walls in a lepidic pattern that can fill air sacs and erode the lung's capacity to oxygenate blood."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle brakes fail in lung cancer: CDKN2A loss is a recurrent event in NSCLC, releasing CDK4/6 to drive proliferation and marking tumors studied for CDK4/6-inhibitor combinations."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "An obstructing tumor breeds infection: NSCLC blocking a bronchus causes post-obstructive pneumonia, and chemotherapy neutropenia adds to the risk, so pneumonia and sepsis are common in the disease course."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Lung cancer clots the circulation: NSCLC is strongly pro-thrombotic (Trousseau), and tumor-driven hypercoagulability plus nonbacterial thrombotic endocarditis can throw emboli to the brain, causing ischemic stroke."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Smoking inflames the lung toward cancer through NF-κB: cigarette carcinogens activate NF-κB in bronchial epithelium, driving the survival and inflammatory signaling that underlies much of NSCLC's carcinogenesis and treatment resistance."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 feeds the tumor through STAT3: the inflamed NSCLC microenvironment activates STAT3, promoting proliferation and immune evasion, a pathway especially active in the KRAS-driven and inflamed tumors."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic disease and chemo wear down the blood: the inflammatory cytokines of NSCLC and its marrow-suppressing chemotherapy produce an anemia of chronic disease that worsens fatigue and breathlessness."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its chest radiation and immunotherapy can injure the heart: mediastinal radiation for NSCLC damages the myocardium and coronary vessels over time, and checkpoint inhibitors can trigger myocarditis, both routes toward heart failure."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A lethal, stigmatized cancer weighs heavily on mood: NSCLC carries some of the highest depression rates in oncology, driven by poor prognosis, breathlessness, and the guilt and stigma often tied to smoking."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Cavitating tumor and immunosuppression let fungus in: post-obstructive collapse, necrotic cavities, and the steroids and chemotherapy used in NSCLC give inhaled Aspergillus a foothold for invasive or saprophytic disease in the damaged lung."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "A tumour plugging the airway breeds pneumonia: a bronchus obstructed by NSCLC traps secretions distal to it, and post-obstructive pneumonia — classically pneumococcal — is a common presenting and recurring complication."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its platinum backbone scars the kidney: the cisplatin central to NSCLC chemotherapy is nephrotoxic, and the tubular injury and magnesium wasting can leave lasting chronic kidney impairment."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Breathlessness and a grim prognosis breed worry: the dyspnoea, scan-to-scan uncertainty and poor survival of NSCLC fuel chronic anxiety and panic alongside the depression that so often accompanies it."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It seeds the brain: NSCLC metastasises commonly to the brain, causing seizures, focal deficits and raised intracranial pressure, and Pancoast tumours and paraneoplastic syndromes injure nerves."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It deranges hormones and calcium: squamous NSCLC secretes PTHrP causing hypercalcaemia, and checkpoint immunotherapy triggers endocrine irAEs like thyroiditis and hypophysitis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It attacks bone from afar and up close: NSCLC metastasises to bone causing pain and fractures, and it characteristically produces hypertrophic pulmonary osteoarthropathy with clubbing and joint pain."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Immunotherapy has transformed it: NSCLC, especially with high PD-L1 expression, responds to checkpoint-inhibitor immunotherapy, now a cornerstone of treatment for advanced disease."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its targeted drugs erupt on the skin: EGFR-inhibitor therapy causes a characteristic acneiform rash and paronychia, and paraneoplastic dermatomyositis can herald the cancer."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It invades the heart and great veins: NSCLC can seed the pericardium causing malignant effusion and tamponade, and central tumours cause superior vena cava obstruction."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It is the flagship of precision oncology: NSCLC is treated by EGFR, ALK, ROS1 and KRAS-G12C targeted inhibitors plus checkpoint immunotherapy, matched to tumour genotype."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It spreads to liver and gut: NSCLC commonly metastasises to the liver and adrenal glands, and chemotherapy and rare gastrointestinal metastases affect the digestive tract."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Cisplatin and paraneoplasia reach the kidney: platinum chemotherapy is nephrotoxic, and NSCLC can cause paraneoplastic SIADH with hyponatraemia."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy is now first-line: pembrolizumab, alone or with chemotherapy by PD-L1 level, transformed advanced non-small-cell lung cancer, with adjuvant and neoadjuvant use expanding."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Platinum doublets remain a backbone: carboplatin or cisplatin with pemetrexed or a taxane is the chemotherapy foundation, given with immunotherapy or after targeted options are exhausted."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It spreads to and erodes bone: non-small-cell lung cancer frequently metastasises to the skeleton, causing lytic cortical bone destruction, pain and fractures treated with bone-protective agents."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Lymphoid islands predict its immunotherapy response: non-small-cell lung cancers bearing tertiary lymphoid structures with germinal-centre B-cell aggregates respond better to checkpoint blockade, the immunotherapy that transformed NSCLC care."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "A shared RET-fusion target: RET-rearranged non-small-cell lung cancer and RET-altered thyroid cancers both respond to selective RET inhibitors (selpercatinib, pralsetinib)—one druggable fusion across two organs."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Tobacco's twin malignancies: cigarette carcinogens that cause non-small-cell lung cancer are also excreted in urine to drive bladder cancer, so the two are classic field-cancerisation partners and a smoker often risks both."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver metastasis: NSCLC commonly spreads to the liver, seeding the hepatic lobule—a poor-prognosis site that also predicts reduced benefit from immunotherapy."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "KRAS across two cancers: KRAS—notably the G12C variant—drives lung adenocarcinoma and pancreatic cancer, and the KRAS-G12C inhibitors developed in NSCLC are now tested in pancreatic disease."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Cardiac immune toxicity and metastasis: immunotherapy for NSCLC can cause autoimmune myocarditis of the myocardium, and the tumour itself can metastasise to the heart and pericardium."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "A shared druggable kinase: ALK rearrangements in NSCLC and activating ALK mutations in neuroblastoma make the same target actionable across adult and paediatric cancer, so ALK inhibitors like lorlatinib cross between the two."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Seizures from brain spread: NSCLC is a leading source of brain metastases, and these lesions are a common cause of new-onset seizures and secondary epilepsy in patients with advanced disease."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "The benign mimic: pulmonary tuberculosis produces masses, cavities and lymphadenopathy that imitate lung cancer, the two coexist in smokers, and old TB scars can themselves seed scar carcinoma."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Rare actionable fusion: NTRK gene fusions are uncommon but highly targetable drivers in NSCLC, treated with TRK inhibitors as part of its precision-oncology landscape."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Squamous PI3K activation: PIK3CA mutation and amplification activate PI3K signalling, especially in squamous NSCLC, a candidate therapeutic target."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplified aggression: MYC amplification drives proliferation and immune evasion in NSCLC and is associated with more aggressive, treatment-resistant disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT survival: AKT, activated downstream of EGFR and PIK3CA, drives NSCLC survival and underlies resistance to EGFR-targeted therapy."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: with CDKN2A loss common in NSCLC, cyclin D1-CDK4/6 activity pushes tumour cells through the G1 checkpoint, a candidate therapeutic vulnerability."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in hypoxic NSCLC drives angiogenesis and a treatment-resistant, metastatic phenotype linked to poor prognosis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Immunosuppressive microenvironment: NSCLC tumours secrete CCL2 to recruit monocytes that become tumour-associated macrophages, building the myeloid niche that blunts T-cell responses and dampens checkpoint-inhibitor efficacy."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "EMT and immune exclusion: TGF-β in the NSCLC stroma drives epithelial-mesenchymal transition that fuels invasion and TKI resistance, while excluding T cells from the tumour to create an immunotherapy-resistant 'cold' phenotype."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Innate-immune sensing: radiation and chemotherapy in NSCLC release cytosolic DNA that activates cGAS-STING, generating type-I interferon that can prime anti-tumour T cells — the rationale for STING agonists combined with checkpoint blockade."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Squamous-cell driver: FGFR1 amplification is a recurrent oncogenic event in squamous NSCLC, the histology that lacks the EGFR/ALK targets of adenocarcinoma, making FGFR inhibitors one of the few precision options in lung squamous-cell carcinoma."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Metastatic homing: CXCR4-CXCL12 signalling directs NSCLC metastasis to CXCL12-rich bone marrow, brain and adrenal niches, and sustains an immunosuppressive microenvironment that excludes T cells from the tumour."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Checkpoint resistance: acquired loss-of-function mutations in JAK1/JAK2 render NSCLC cells unresponsive to interferon-γ, abolishing PD-L1 induction and antigen presentation — a key mechanism of acquired resistance to PD-1 blockade."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K-AKT brake: PTEN loss is a recurrent event in NSCLC that unleashes the PI3K-AKT-mTOR axis already driven by PIK3CA and EGFR, promoting survival signalling and contributing to resistance against EGFR tyrosine-kinase inhibitors."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Targeted-therapy resistance: AXL receptor tyrosine kinase drives epithelial-mesenchymal transition and is upregulated in NSCLC escaping EGFR- and ALK-targeted therapy, a bypass survival pathway that motivates AXL inhibitors in combination regimens."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle control: CDKN2A loss and cyclin-D1 overexpression in NSCLC converge on CDK4/6 to inactivate RB and force the G1-S transition, the proliferative engine that makes CDK4/6 inhibitors an emerging strategy in RB-intact disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK convergence: EGFR, ALK, KRAS, BRAF, MET, RET and FGFR (all already mapped) funnel into the MAPK-ERK cascade, the shared proliferative output of NSCLC's diverse oncogenic drivers."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth axis: mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA, AKT and PTEN already mapped) that sustains growth and survival signalling in NSCLC."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Forced S-phase: the CDK4/6-cyclin-D1 axis (mapped) inactivates RB to release E2F1, the transcription factor that executes the G1-S transition driving NSCLC proliferation."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Small-cell transformation: combined RB1 and TP53 loss drives the histologic transformation of EGFR-mutant adenocarcinoma to small-cell lung cancer, a notable mechanism of acquired resistance to EGFR inhibitors (CDK4/6 and CDKN2A already mapped)."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory microenvironment: IL-6-STAT3 signalling (STAT3 already mapped) sustains a tumour-promoting inflammatory microenvironment and contributes to therapy resistance in non-small cell lung cancer."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Smoking-driven inflammation: cigarette-smoke- and infection-driven TLR-MyD88-NF-κB signalling (NF-κB already mapped) provides a chronic inflammatory drive in lung carcinogenesis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes invasion and immune evasion in non-small-cell lung cancer."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "LKB1 (STK11 mapped) activates AMPK to restrain anabolic growth, and its loss in NSCLC drives metabolic reprogramming and immunotherapy resistance."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) drives EMT, invasion and the immunosuppressive microenvironment of non-small-cell lung cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response central to the checkpoint immunotherapy that has transformed non-small-cell lung cancer treatment."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO tumour-suppressor activity, antagonised by EGFR/KRAS-driven PI3K-AKT signalling, is lost in the proliferative progression of non-small-cell lung cancer."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression silences tumour-suppressor genes and contributes to the epigenetic dysregulation of non-small-cell lung cancer."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells is the immune-clearance axis central to the checkpoint-immunotherapy response of non-small-cell lung cancer."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in non-small-cell lung cancer."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the smoking-associated inflammatory and immunosuppressive microenvironment of non-small-cell lung cancer."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the Wnt/β-catenin and survival signaling of non-small-cell lung cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of EGFR, MET, and other receptor tyrosine kinases (all already mapped) drives the invasion of non-small-cell lung cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic silencing of tumor-suppressor genes in non-small-cell lung cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of non-small-cell lung cancer cells."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of non-small-cell lung cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of non-small-cell lung cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of non-small cell lung cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of non-small cell lung cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of non-small cell lung cancer."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Bone-metastatic niche: NSCLC frequently metastasises to bone, where tumour-driven RANKL activates osteoclasts to cause skeletal-related events, the rationale for denosumab, and RANKL blockade also intersects with the immune microenvironment relevant to checkpoint therapy."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen presentation: MHC class II on tumour and antigen-presenting cells shapes the CD4 T-cell help that underlies the checkpoint-inhibitor responses central to modern NSCLC therapy, and its loss is a mechanism of immune escape and immunotherapy resistance."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy execution: platinum-doublet chemotherapy, still a backbone of NSCLC treatment, kills tumour cells by triggering caspase-3-mediated apoptosis, and defects in this executioner pathway underlie chemoresistance."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Cellular immunotherapy: IL-2-driven T-cell expansion underlies the tumour-infiltrating-lymphocyte therapy now approved for advanced NSCLC and complements the checkpoint inhibitors (PD-1/CTLA-4 already mapped) central to its treatment."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Immunotherapy cardiotoxicity: the checkpoint inhibitors widely used in NSCLC can cause immune-mediated myocarditis, and troponin elevation helps detect this rare but often fatal complication, alongside pericardial spread of the tumour."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Paraneoplastic hypercalcaemia: squamous NSCLC commonly secretes PTH-related peptide, which acts like PTH to raise calcium (already mapped), causing the paraneoplastic hypercalcaemia that marks advanced disease."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia of malignancy: chronic disease, marrow involvement and chemotherapy lower haemoglobin in NSCLC, and the resulting anaemia adds to the breathlessness and fatigue that already burden these patients."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tobacco oxidative damage: cigarette smoke and chronic inflammation generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage (NRF2 already mapped) drives the carcinogenesis of smoking-related NSCLC."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Cancer pain and dyspnoea: opioids acting on the mu-opioid receptor relieve the pain of bone metastases and the refractory breathlessness of advanced NSCLC, a mainstay of its palliative and supportive care."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 carcinogenesis: tobacco induces cyclooxygenase-2 and prostaglandin E2 in the airway, promoting the proliferation, angiogenesis (VEGF already mapped) and immunosuppression of lung carcinogenesis, and COX-2 has been studied as a target in NSCLC."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hepatic and adrenal metastasis: NSCLC commonly metastasises to the liver and adrenal glands, the visceral spread that defines stage IV disease and shapes systemic therapy."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "PTHrP hypercalcaemia: squamous NSCLC characteristically secretes parathyroid-hormone-related peptide (PTH already mapped), raising calcium to cause the humoral hypercalcaemia of malignancy with its confusion and renal impairment."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment that the checkpoint immunotherapy central to NSCLC must overcome."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Adrenal metastasis: the adrenal glands are a characteristic site of NSCLC metastasis, the visceral spread that defines stage IV disease alongside the liver (already mapped) and brain (already mapped)."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy: stereotactic body photon radiotherapy cures early inoperable NSCLC, and concurrent chemoradiotherapy treats stage III disease, photon radiation a mainstay of the non-metastatic tumour."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 microenvironment: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the immunosuppressive microenvironment of non-small-cell lung cancer."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Cancer cachexia: leptin is the adipokine of the cancer cachexia (the weight loss) of NSCLC, and part of the obesity-paradox in the immunotherapy response."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic-cachexia adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-cachexia axis of non-small-cell lung cancer."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Cachexia-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the cancer cachexia and metabolic axis of non-small-cell lung cancer."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the checkpoint (PD-1 already mapped) immunotherapy of non-small-cell lung cancer."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm exploited by the checkpoint immunotherapy of non-small-cell lung cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the anti-tumour immune microenvironment of non-small-cell lung cancer."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of non-small-cell lung cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of non-small-cell lung cancer."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of non-small-cell lung cancer."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of non-small-cell lung cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate cytotoxicity: the NK cells (perforin already mapped) provide the innate anti-tumour surveillance complementing the CD8 (already mapped) checkpoint-immunotherapy response in non-small-cell lung cancer."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts the checkpoint-immunotherapy (PD-1 already mapped) response of non-small-cell lung cancer."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of non-small-cell lung cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Tumour complement: the complement C3 activation contributes to the inflammatory and immunosuppressive dimension of the non-small-cell-lung-cancer microenvironment."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Airway alarmin: TSLP released by the inflamed bronchial epithelium drives mast-cell and dendritic-cell activation in the non-small-cell lung cancer stroma, promoting the type-2 microenvironment that dampens anti-tumour immunity."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM invasion driver: periostin, upregulated in the non-small-cell lung cancer stroma downstream of TGF-β, promotes tumour cell adhesion, invasion and metastatic colonisation of the pleura and bone."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Immune-evasion axis: histamine H2-receptor signalling on non-small-cell lung cancer cells and their stromal mast cells promotes tumour immune evasion and angiogenesis via the PGE-2 and VEGF already mapped."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Tumour microenvironment kinin: bradykinin generated by the kallikrein-kinin system in the non-small-cell lung cancer stroma promotes vasodilation and macrophage activation, amplifying the inflammatory tumour microenvironment."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation: C1-esterase inhibitor restrains the complement and contact-activation pathways whose dysregulation in the NSCLC microenvironment sustains the C3 (already mapped) inflammatory cascade."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia correction: erythropoietin addresses cancer- and chemotherapy-induced anaemia in NSCLC; its receptor (EPOR) on tumour cells may additionally modulate tumour-cell survival and resistance to platinum regimens."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Lung tumour melatonin: melatonin inhibits NSCLC proliferation and EMT (already mapped) through MT1/MT2-mediated cAMP suppression and Wnt/β-catenin (already mapped) inhibition, sensitising NSCLC cells to EGFR-targeted (EGFR already mapped) and platinum therapies."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "NSCLC androgen axis: testosterone via androgen receptor signalling modulates PD-L1 (already mapped) expression and the immunosuppressive microenvironment in NSCLC; AR signalling intersects KRAS (already mapped) and EGFR (already mapped) tumour growth pathways."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "NSCLC neuroendocrine serotonin: serotonin co-produced by neuroendocrine-differentiated NSCLC cells activates 5-HT2 and 5-HT4 receptors to promote KRAS (already mapped)-driven proliferation and mTOR (already mapped) pro-survival signalling in non-small-cell lung cancer."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "NSCLC prolactin: prolactin via JAK2/STAT3 (already mapped) and mTOR (already mapped) activates NSCLC tumour cells and macrophages (already mapped), promoting PD-L1 (already mapped) upregulation and immunosuppressive microenvironment in non-small-cell lung cancer."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "NSCLC oxytocin: oxytocin receptors on NSCLC tumour and mast cells (already mapped) couple to Gαq-PKC, activating KRAS (already mapped) and EGFR (already mapped) downstream proliferative signalling in non-small-cell lung cancer."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "NSCLC vasopressin: vasopressin via V1a receptors on NSCLC stroma and macrophages (already mapped) activates Gαq-PLC-IP3 signalling, cross-activating VEGF (already mapped) and mTOR (already mapped) angiogenic cascades in non-small-cell lung cancer."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "NSCLC selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the NSCLC tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "NSCLC iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune surveillance; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of NSCLC."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "NSCLC sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) anti-tumour cascade of NSCLC."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "NSCLC copper: copper-dependent enzymes in macrophage (already mapped) and mast-cell (already mapped) immunity; copper imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade promoting T-cytotoxic (already mapped) exhaustion in NSCLC."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "NSCLC zinc: zinc co-factors in macrophage (already mapped) and neutrophil (already mapped) metalloproteases; zinc depletion exacerbates NF-κB (already mapped) and IL-6 (already mapped) tumour-permissive inflammation while impairing T-cytotoxic (already mapped) killing in NSCLC."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "NSCLC potassium: potassium efflux gates macrophage (already mapped) and mast-cell (already mapped) NLRP3 inflammasome; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling while suppressing T-cytotoxic (already mapped) function in NSCLC."
---

# NSCLC

## Overview

**Non-small cell lung cancer (NSCLC)** accounts for **~85% of all lung cancers** and is the leading cause of cancer-related death globally, responsible for approximately 1.8 million deaths per year worldwide. It encompasses **three major histological subtypes** — adenocarcinoma, squamous cell carcinoma, and large cell carcinoma — unified by their non-neuroendocrine biology but with distinct molecular drivers and treatment strategies.

**Histological subtypes:**
- **Adenocarcinoma (LUAD, ~40% of NSCLC):** Peripheral lung; lepidic/acinar/micropapillary/solid and mucinous growth patterns; KRAS, EGFR, ALK, ROS1, RET, MET, BRAF V600E, NTRK1/2/3 drivers; most molecularly characterized subtype; all patients should receive comprehensive molecular profiling
- **Squamous cell carcinoma (LUSC, ~25-30% of NSCLC):** Central, hilar location; FGFR1 amplification (~20%), KEAP1/NFE2L2 (oxidative stress pathway), TP53 (>80%), CDKN2A loss, DDR2 mutation; fewer targetable oncogenes; standard treatment: chemotherapy + immunotherapy (pembrolizumab); necitumumab (anti-EGFR) + cisplatin for EGFR IHC+ squamous
- **Large cell carcinoma (~10-15%):** Poorly differentiated; diagnosis of exclusion after ruling out adeno/squamous by IHC; treated as adenocarcinoma unless otherwise specified

**Genomic landscape of lung adenocarcinoma:**
- **KRAS mutations (33% overall; G12C = 13%):** Mutually exclusive with EGFR, ALK; KRAS G12C now targetable; G12D, G12V — next-generation inhibitors
- **EGFR mutations (15-20% Western; 40-50% Asian):** Exon 19 del, L858R (~85% of EGFR mutations); exon 20 insertions (~5-10%); uncommon mutations (G719X, L861Q, S768I)
- **ALK rearrangements (5-7%):** EML4-ALK most common fusion; young non-smokers; highly responsive to ALK TKIs
- **ROS1 rearrangements (1-2%):** CD74-ROS1 most common; crizotinib, entrectinib, ceritinib active
- **RET rearrangements (1-2%):** KIF5B-RET; selpercatinib (LIBRETTO-001) highly active
- **MET exon 14 skipping (3-4%):** Capmatinib (GEOMETRY), tepotinib approved
- **HER2 mutations (2-3%):** Exon 20 insertions dominant; trastuzumab deruxtecan (T-DXd) approved (DESTINY-Lung01/02)
- **BRAF V600E (~2%):** Dabrafenib + trametinib approved
- **NTRK1/2/3 fusions (<1%):** Larotrectinib and entrectinib (tissue-agnostic approval)
- **TP53 mutations (>50%):** Co-mutation with KRAS in ~30% of LUAD; no direct therapy
- **KEAP1/STK11 mutations:** Co-occur with KRAS; suppress NRF2-regulated antioxidant → immunotherapy resistance markers; STK11 loss → "cold" tumor, resistance to pembrolizumab

**Small cell lung cancer (SCLC) — distinct entity (not covered here):**
- Neuroendocrine; 15% of lung cancers; virtually universal RB1 + TP53 loss; atezolizumab + carboplatin + etoposide (first-line); extensive-stage SCLC median OS ~12 months; rapid chemosensitivity but universal relapse

## Structure

### Pathogenesis and tumor microenvironment

**Carcinogenesis:**
- **Smoking (80-85% of NSCLC):** Tobacco carcinogens (PAHs, nitrosamines) → DNA adducts → predominantly C>A transversions in TP53, KRAS G12C, and other driver genes; squamous cell carcinoma is more strongly tobacco-related than adenocarcinoma
- **Never-smoker NSCLC:** More likely to be EGFR-mutant, ALK/ROS1-rearranged, HER2-mutant; adenocarcinoma histology; younger patients; better prognosis per matched stage
- **Preinvasive lesions:** Adenocarcinoma in situ (AIS, previously BAC) → minimally invasive adenocarcinoma → invasive adenocarcinoma; squamous: normal epithelium → squamous metaplasia → dysplasia → carcinoma in situ → invasive SCC

**NSCLC tumor microenvironment (TME):**
- Variable TME composition by subtype: squamous tumors (higher TIL density, higher TMB) vs. KRAS/STK11-mutant adenocarcinoma (immune excluded/desert)
- **PD-L1 expression:** Driven by IFN-gamma signaling in TME; ~30% TPS ≥50%; ~55% TPS ≥1%; IFN-gamma → STAT1 → IRF1 → PD-L1 transcription; used for pembrolizumab mono (≥50%) and combination (≥1%) decisions
- **Tumor mutational burden (TMB):** Higher in squamous (smoking-related) vs. adenocarcinoma; TMB-H (≥10 mut/Mb) → pembrolizumab monotherapy approval (KEYNOTE-158, tumor-agnostic); modest predictive biomarker for NSCLC specifically vs. PD-L1

## Function

### Clinical presentation and staging

**Presentation:**
- Central NSCLC (squamous): Cough, hemoptysis, post-obstructive pneumonia, wheezing; occasionally endobronchial
- Peripheral NSCLC (adenocarcinoma): Often asymptomatic until advanced; chest pain, dyspnea with pleural effusion; peripheral nodule discovered incidentally on CT
- **Pancoast tumor (superior sulcus):** Shoulder/arm pain, Horner syndrome (ptosis, miosis, anhidrosis), hand atrophy — brachial plexus and sympathetic chain invasion; special treatment: concurrent chemo-RT → surgery
- **Paraneoplastic:** SIADH (squamous SCC), hypercalcemia (PTHrP from squamous), Eaton-Lambert (SCLC more common), hypertrophic pulmonary osteoarthropathy (periosteal new bone formation, clubbing → mostly adenocarcinoma)

**Staging (TNM, 8th edition):**
- Stage I-IIIA: Locoregional; curative intent with surgery ± adjuvant; landmark improvement: adjuvant osimertinib (ADAURA: DFS HR 0.17 in stage II-III EGFR-mutant) and adjuvant atezolizumab (IMpower010: PD-L1 ≥1%, stage II-IIIA after platinum chemotherapy)
- Stage IIIB-C: Unresectable locally advanced; concurrent cisplatin/etoposide + RT → durvalumab consolidation (PACIFIC trial: 5-year OS 42.9% vs. 33.4%)
- Stage IV: Metastatic; molecular-directed or immunotherapy-based; brain metastases common (especially EGFR/ALK — high CNS penetrance of osimertinib and lorlatinib important)

**Screening:**
- Low-dose CT (LDCT) annually: US Preventive Services Task Force recommends for adults 50-80 years, 20+ pack-year history, currently smoking or quit <15 years; reduces lung cancer mortality ~20% (NLST trial); widespread implementation ongoing; requires structured reporting (Lung-RADS)

## Pathology

### Diagnosis and molecular profiling

**Tissue biopsy:** CT-guided percutaneous or bronchoscopic biopsy → histology (hematoxylin/eosin), IHC (TTF-1/NapsinA for adenocarcinoma; p40/CK5/6 for squamous), and comprehensive molecular testing

**Molecular profiling — mandatory for all newly diagnosed advanced NSCLC:**
- **Comprehensive genomic profiling (CGP, e.g., FoundationOne CDx, MSK-IMPACT):** Single test provides all relevant biomarkers (EGFR, KRAS, ALK, ROS1, MET, RET, BRAF, NTRK, HER2, TMB, MSI); preferred over sequential single-gene testing
- **PD-L1 IHC (22C3 pharmDx):** TPS (tumor proportion score) 0/1-49/≥50%; guides pembrolizumab monotherapy vs. combination; required in all newly diagnosed metastatic NSCLC

### Treatment [^soria-2018-osimertinib-flaura] [^reck-2016-pembrolizumab-keynote024]

**EGFR-mutant NSCLC (exon 19 del or L858R):**
- **First-line:** Osimertinib (3rd-gen EGFR TKI, FLAURA: PFS 18.9 vs. 10.2 months vs. 1st-gen; OS 38.6 vs. 31.8 months; CNS penetrant; approved for adjuvant after resection and for stage IV first-line) [^soria-2018-osimertinib-flaura]
- **Resistance mechanisms:** On-target (C797S in cis with T790M, or new EGFR amplification), off-target (MET amplification, HER2 amplification, PIK3CA mutation, RET/ALK/RAS transformation); liquid biopsy (ctDNA) tracks resistance earlier than imaging
- **Osimertinib + chemotherapy (FLAURA2):** Improved PFS (25.5 vs. 16.7 months) but added toxicity → selected high-risk patients

**ALK-rearranged NSCLC:**
- **First-line:** Alectinib (ALEX: PFS 34.8 vs. 10.9 months vs. crizotinib; superior CNS penetration); brigatinib and lorlatinib also active first-line; lorlatinib (CROWN trial) may be preferred in patients with brain metastases (intracranial ORR 82%)
- **Resistance:** Lorlatinib covers most ALK secondary mutations (G1202R — most common alectinib resistance)

**KRAS G12C-mutant NSCLC:** [^halliday-2023-kras-nsclc]
- **Sotorasib (Lumakras, CodeBreaK-100):** ORR 37%, median DFS 6.8 months; FDA approved 2021
- **Adagrasib (Krazati, KRYSTAL-1):** ORR 43%, median PFS 6.5 months; FDA approved 2022; CNS active; MAESTRA-3 Phase 3 first-line trial vs. chemotherapy ongoing
- **Combination strategies:** KRAS G12C + SHP2, MEK, or EGFR inhibitors to overcome adaptive RAS pathway reactivation

**PD-L1 ≥50%, no oncogenic driver:**
- **Pembrolizumab monotherapy (KEYNOTE-024):** OS 26.3 vs. 13.8 months vs. chemotherapy in PD-L1 ≥50%; 5-year OS 31.9% vs. 16.3% — durable survival benefit [^reck-2016-pembrolizumab-keynote024]; approved first-line
- **Nivolumab + ipilimumab (CHECKMATE-227):** Dual checkpoint blockade; OS benefit in TMB-H subgroup; approved first-line regardless of PD-L1 based on CHECKMATE-9LA (+ 2 cycles chemotherapy)

**Squamous NSCLC or adenocarcinoma with PD-L1 1-49% or undetermined:**
- **Pembrolizumab + carboplatin + paclitaxel/nab-paclitaxel (KEYNOTE-189 [adeno], KEYNOTE-407 [squamous]):** OS benefit vs. chemotherapy alone regardless of PD-L1; OS 15.9 vs. 11.3 months (squamous); now standard-of-care for eligible patients

**BRAF V600E-mutant NSCLC:**
- **Dabrafenib + trametinib:** ORR 64%, PFS 14.6 months (BRF113928 trial); FDA approved for BRAF V600E-mutant NSCLC

**Adjuvant and consolidation therapies:**
- **Osimertinib adjuvant (ADAURA):** After resection of stage IB-IIIA EGFR-mutant; DFS HR 0.17; 5-year DFS ~85% vs. ~44% placebo → transformative; 3-year course
- **Durvalumab consolidation (PACIFIC):** After concurrent CRT for unresectable stage III NSCLC; 5-year OS 42.9% vs. 33.4%; standard of care globally
- **Pembrolizumab adjuvant (KEYNOTE-091):** After resection stages IB-IIIA, regardless of PD-L1; DFS benefit; atezolizumab adjuvant (IMpower010) in PD-L1 ≥1%

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS G12C is the most common oncogenic driver in NSCLC adenocarcinoma (~13%); sotorasib (CodeBreaK-100) and adagrasib (KRYSTAL-1) are approved for KRAS G12C-mutant NSCLC; next-generation pan-KRAS and T cell-engaging approaches in clinical development.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR mutations (exon 19 del, L858R) drive 15-20% of NSCLC; osimertinib (FLAURA: PFS 18.9 vs. 10.2 months vs. erlotinib) is first-line standard; acquired resistance via C797S and MET amplification drives second-line decisions.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E occurs in ~2% of NSCLC adenocarcinoma; dabrafenib + trametinib is approved for BRAF V600E-mutant NSCLC (ORR ~64%, PFS 14.6 months); non-V600E BRAF mutations require pan-RAF or ERK-directed approaches.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1/PD-L1 blockade transformed NSCLC: pembrolizumab is standard-of-care in PD-L1 ≥50% first-line (KEYNOTE-024: OS 26.3 vs. 13.8 months) and + chemotherapy in all-comers; atezolizumab, nivolumab, and durvalumab are also approved.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — NSCLC is ~85% of lung cancer: squamous tumors arise centrally near the hilum (cough, hemoptysis) while adenocarcinomas arise peripherally and are often found incidentally; annual low-dose CT screening of heavy smokers cuts lung-cancer mortality ~20% (NLST).
- `connects-to` → **[ALK](../../03-molecular/alk/README.md)** — ALK rearrangements (EML4-ALK, ~5-7%) define a distinct NSCLC of young never-smokers that is exquisitely targetable: alectinib and lorlatinib far outperform chemotherapy with strong CNS penetration for brain metastases; lorlatinib covers the G1202R resistance mutation.
- `connects-to` → **[Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — Lung adenocarcinoma arises from alveolar type II pneumocytes (and club cells), retaining their TTF-1 and napsin-A markers; it progresses through adenocarcinoma-in-situ → minimally invasive → invasive adenocarcinoma, the peripheral lepidic-to-solid sequence.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — NSCLC and melanoma are the twin proving grounds of checkpoint immunotherapy: both accumulate heavy carcinogen-driven mutational burdens (tobacco, UV) yielding neoantigens, so PD-1/PD-L1 (and CTLA-4) blockade gives durable responses in both, and both carry targetable BRAF V600E.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — NSCLC's response to immunotherapy hinges on cytotoxic T cells: a high tobacco-driven mutational burden generates neoantigens, and PD-1/PD-L1 blockade (pembrolizumab, first-line at PD-L1 ≥50%) reinvigorates exhausted CD8+ T cells — absent in never-smoker EGFR/ALK subsets.
- `connects-to` → **[Small Cell Lung Cancer](../sclc/README.md)** — NSCLC and small-cell lung cancer are the two divisions of lung cancer: NSCLC (~85%, adeno/squamous) is driver-rich and often resectable or targetable, while SCLC is a fast neuroendocrine tumor of heavy smokers that disseminates early, is rarely operable, and is RB1/TP53-driven.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — NSCLC and mesothelioma are the two major thoracic cancers tied to inhaled carcinogens but distinct: NSCLC arises in lung parenchyma (smoking, EGFR/KRAS-driven), while mesothelioma arises from the pleura decades after asbestos exposure—different cells and treatment.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is central to NSCLC: stereotactic body photon radiotherapy can cure inoperable early-stage tumors, while conventional chemoradiation treats locally advanced disease—and consolidation immunotherapy after radiation now improves survival.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages shape the NSCLC microenvironment: M2-polarized macrophages suppress cytotoxic T cells and promote angiogenesis, contributing to immunotherapy resistance—so they are studied as both a biomarker and a target alongside PD-1 blockade.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain is a frequent NSCLC metastatic site: lung adenocarcinomas, especially EGFR/ALK-driven, commonly seed the brain, so staging includes brain MRI and CNS-penetrant targeted drugs (osimertinib, lorlatinib)—brain metastases strongly shape prognosis.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Carbon-based tobacco carcinogens are the dominant cause of NSCLC: smoke's PAHs and nitrosamines form DNA adducts that mutate KRAS and TP53, driving most squamous and many adenocarcinomas—though EGFR-mutant adenocarcinoma in never-smokers takes a distinct path.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — NSCLC and head and neck cancer share tobacco-driven field cancerization: carcinogens injure the whole aerodigestive tract, so smokers with one cancer face high risk of a second primary in the other—both demand smoking cessation and surveillance.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — MET is a targetable NSCLC driver: MET exon-14 skipping mutations and MET amplification drive a subset of non-small-cell lung cancers and confer resistance to EGFR inhibitors, so MET-directed drugs extend the precision-oncology toolkit beyond EGFR, ALK and KRAS.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal gland is a classic NSCLC metastatic site: lung cancer characteristically spreads to the adrenals (along with brain, bone and liver), so an adrenal mass in a lung-cancer patient demands staging workup—adrenal involvement often marks stage IV disease.
- `connects-to` → **[COPD](../copd/README.md)** — NSCLC and COPD are linked by shared tobacco injury: smoking drives both, COPD independently raises lung-cancer risk through chronic inflammation, and the two coexist so often that emphysema complicates surgery and screening targets this overlapping high-risk population.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 is among the most mutated genes in NSCLC: smoking-driven DNA damage frequently inactivates p53, removing a key brake on the cell cycle and apoptosis, so its loss—often alongside KRAS—marks aggressive, treatment-resistant lung adenocarcinoma.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — NSCLC is the dominant cancer of the respiratory system: arising in bronchial and alveolar cells mostly from smoking, it accounts for ~85% of lung cancers and destroys lung function as it grows—the leading cause of cancer death worldwide.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — NSCLC staging hinges on the lymphatic system: spread to hilar and mediastinal lymph nodes (the N stage) determines whether disease is surgically curable, so nodal sampling by EBUS or mediastinoscopy is decisive in planning treatment.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Liver metastases worsen lung-cancer outlook: NSCLC commonly spreads to the liver, which carries a poorer prognosis and historically blunts the benefit of immunotherapy, so liver involvement shapes both staging and treatment expectations.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — NSCLC immunotherapy can pair two checkpoints: adding anti-CTLA-4 (ipilimumab) to anti-PD-1 therapy gives durable responses in some patients, an option especially when chemotherapy is undesirable—broadening immunotherapy beyond PD-1 blockade alone.
- `connects-to` → **[RET](../../03-molecular/ret/README.md)** — A subset of NSCLC is driven by RET fusions: these rearrangements switch on RET kinase, and selective inhibitors like selpercatinib produce strong responses, so guidelines include RET in the molecular panel run on every lung adenocarcinoma.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Squamous lung cancers often hijack NRF2: KEAP1/NRF2 mutations switch on a permanent antioxidant program that shields the tumor from oxidative stress and chemo/radiation, marking an aggressive, treatment-resistant subset of NSCLC.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — NSCLC evades immunity with regulatory T cells: Tregs accumulate in the tumor and suppress the cytotoxic response, blunting the PD-1 checkpoint therapy that has transformed lung cancer treatment—so depleting them is a goal.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — NSCLC is shaped by cancer-associated fibroblasts: they build a stiff, desmoplastic stroma that secretes growth factors, promotes invasion, and shields tumor cells from drugs, making the fibroblast-rich niche a driver of resistance.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia hardens NSCLC against treatment: oxygen-starved tumor regions resist radiation, which needs oxygen to fix DNA damage, and they drive an aggressive, metastatic phenotype—so tumor hypoxia is both a prognostic marker and a therapeutic obstacle.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — NSCLC recruits its blood supply through VEGF: the tumor secretes this angiogenesis driver to grow and spread, so anti-VEGF bevacizumab is combined with chemotherapy and immunotherapy in eligible non-squamous lung cancers.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells decide how well NSCLC immunotherapy works: by presenting tumor antigens they prime the T cells that PD-1 blockade unleashes, so their function in the tumor shapes response to the checkpoint drugs central to lung-cancer care.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Squamous lung cancer can spike blood calcium: it secretes PTHrP that mimics parathyroid hormone, pulling calcium from bone into the blood—a paraneoplastic hypercalcemia causing confusion, thirst, and kidney injury.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — NSCLC can invade the heart's lining: a nearby tumor may breach the pericardium, filling it with malignant fluid that compresses the heart (tamponade), a dangerous complication of advanced lung cancer.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — NSCLC can grow out of lung fibrosis: adenocarcinomas may arise in scarred lung ('scar carcinoma'), and the tumor's own desmoplastic stroma stiffens the surrounding tissue.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy separates NSCLC's faces: adenocarcinoma shows microvilli and lamellar bodies betraying pneumocyte origin, while squamous cell carcinoma reveals desmosomes and bundled tonofilaments of keratin — ultrastructure that resolved subtype before immunostains.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — NSCLC favors the skeleton when it spreads: bone is among its commonest metastatic sites, and deposits reaching the marrow can crowd out blood production, causing the anemia and low counts that signal advanced disease.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — NSCLC pushes platelets up and clots out: paraneoplastic thrombocytosis is common, tumor-driven hypercoagulability makes lung cancer a leading cause of cancer-associated thrombosis, and a high platelet count tracks with worse outcomes.
- `connects-to` → **[STK11](../../03-molecular/stk11/README.md)** — STK11/LKB1 loss makes a cold tumor: this tumor suppressor is among the most frequently inactivated genes in lung adenocarcinoma, and its loss — especially alongside KRAS — predicts an immune-excluded tumor that resists checkpoint inhibitors.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — NSCLC eats into bone: skeletal metastases are common and osteolytic, with tumor-driven RANKL revving up osteoclasts to dissolve bone — causing pain, fractures, and hypercalcemia, and making osteoclast-blocking denosumab part of supportive care.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils foretell the course in NSCLC: a high neutrophil-to-lymphocyte ratio is a robust poor-prognosis marker, and tumor-associated neutrophils help build the immunosuppressive niche that lets the cancer grow.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies steer modern NSCLC care: TTF-1 and p40 stains separate adeno from squamous, PD-L1 staining selects who gets checkpoint therapy, and the drugs themselves — anti-PD-1 pembrolizumab and anti-VEGF bevacizumab — are monoclonal antibodies.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney sets limits on treatment: the cisplatin backbone of NSCLC chemotherapy is nephrotoxic, demanding hydration and dose adjustment, and the tumor can drive a paraneoplastic SIADH that drops sodium dangerously low.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Cisplatin wastes the body's magnesium: by injuring the kidney tubule that reclaims it, the platinum chemotherapy for NSCLC drops magnesium and potassium, electrolytes that must be replaced through every cycle of treatment.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Lung adenocarcinoma is among the most clot-prone cancers: tumor tissue factor and chemotherapy combine to drive deep-vein thrombosis and pulmonary embolism, a frequent complication that worsens outcomes and often needs anticoagulation.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Immunotherapy can inflame the thyroid: the checkpoint inhibitors central to modern NSCLC treatment commonly trigger autoimmune thyroiditis, causing transient hyperthyroidism then lasting hypothyroidism — one of the most frequent immune-related side effects.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — A rare but lethal immune side effect strikes the heart muscle: checkpoint-inhibitor myocarditis floods the myocardium with T cells attacking cardiomyocytes, an uncommon complication of NSCLC immunotherapy with a high fatality rate demanding urgent steroids.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — Another driver joins the targetable list: HER2 mutations and amplification power a subset of lung adenocarcinomas, now hit by antibody-drug conjugates like trastuzumab deruxtecan, extending the precision-oncology approach beyond EGFR and ALK.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — The tumor reawakens its immortality switch: TERT promoter activation restores telomerase so NSCLC cells escape the telomere erosion that limits normal divisions, a common step that lets the smoking-damaged epithelium keep proliferating.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Adenocarcinoma grows from the gas-exchange lining: NSCLC's most common subtype arises in the peripheral alveoli, spreading along the delicate walls in a lepidic pattern that can fill air sacs and erode the lung's capacity to oxygenate blood.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Cell-cycle brakes fail in lung cancer: CDKN2A loss is a recurrent event in NSCLC, releasing CDK4/6 to drive proliferation and marking tumors studied for CDK4/6-inhibitor combinations.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — An obstructing tumor breeds infection: NSCLC blocking a bronchus causes post-obstructive pneumonia, and chemotherapy neutropenia adds to the risk, so pneumonia and sepsis are common in the disease course.
- `connects-to` → **[Stroke](../stroke/README.md)** — Lung cancer clots the circulation: NSCLC is strongly pro-thrombotic (Trousseau), and tumor-driven hypercoagulability plus nonbacterial thrombotic endocarditis can throw emboli to the brain, causing ischemic stroke.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Smoking inflames the lung toward cancer through NF-κB: cigarette carcinogens activate NF-κB in bronchial epithelium, driving the survival and inflammatory signaling that underlies much of NSCLC's carcinogenesis and treatment resistance.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 feeds the tumor through STAT3: the inflamed NSCLC microenvironment activates STAT3, promoting proliferation and immune evasion, a pathway especially active in the KRAS-driven and inflamed tumors.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic disease and chemo wear down the blood: the inflammatory cytokines of NSCLC and its marrow-suppressing chemotherapy produce an anemia of chronic disease that worsens fatigue and breathlessness.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its chest radiation and immunotherapy can injure the heart: mediastinal radiation for NSCLC damages the myocardium and coronary vessels over time, and checkpoint inhibitors can trigger myocarditis, both routes toward heart failure.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A lethal, stigmatized cancer weighs heavily on mood: NSCLC carries some of the highest depression rates in oncology, driven by poor prognosis, breathlessness, and the guilt and stigma often tied to smoking.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Cavitating tumor and immunosuppression let fungus in: post-obstructive collapse, necrotic cavities, and the steroids and chemotherapy used in NSCLC give inhaled Aspergillus a foothold for invasive or saprophytic disease in the damaged lung.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — A tumour plugging the airway breeds pneumonia: a bronchus obstructed by NSCLC traps secretions distal to it, and post-obstructive pneumonia — classically pneumococcal — is a common presenting and recurring complication.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its platinum backbone scars the kidney: the cisplatin central to NSCLC chemotherapy is nephrotoxic, and the tubular injury and magnesium wasting can leave lasting chronic kidney impairment.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Breathlessness and a grim prognosis breed worry: the dyspnoea, scan-to-scan uncertainty and poor survival of NSCLC fuel chronic anxiety and panic alongside the depression that so often accompanies it.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It seeds the brain: NSCLC metastasises commonly to the brain, causing seizures, focal deficits and raised intracranial pressure, and Pancoast tumours and paraneoplastic syndromes injure nerves.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It deranges hormones and calcium: squamous NSCLC secretes PTHrP causing hypercalcaemia, and checkpoint immunotherapy triggers endocrine irAEs like thyroiditis and hypophysitis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It attacks bone from afar and up close: NSCLC metastasises to bone causing pain and fractures, and it characteristically produces hypertrophic pulmonary osteoarthropathy with clubbing and joint pain.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Immunotherapy has transformed it: NSCLC, especially with high PD-L1 expression, responds to checkpoint-inhibitor immunotherapy, now a cornerstone of treatment for advanced disease.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its targeted drugs erupt on the skin: EGFR-inhibitor therapy causes a characteristic acneiform rash and paronychia, and paraneoplastic dermatomyositis can herald the cancer.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It invades the heart and great veins: NSCLC can seed the pericardium causing malignant effusion and tamponade, and central tumours cause superior vena cava obstruction.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It is the flagship of precision oncology: NSCLC is treated by EGFR, ALK, ROS1 and KRAS-G12C targeted inhibitors plus checkpoint immunotherapy, matched to tumour genotype.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It spreads to liver and gut: NSCLC commonly metastasises to the liver and adrenal glands, and chemotherapy and rare gastrointestinal metastases affect the digestive tract.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Cisplatin and paraneoplasia reach the kidney: platinum chemotherapy is nephrotoxic, and NSCLC can cause paraneoplastic SIADH with hyponatraemia.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy is now first-line: pembrolizumab, alone or with chemotherapy by PD-L1 level, transformed advanced non-small-cell lung cancer, with adjuvant and neoadjuvant use expanding.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Platinum doublets remain a backbone: carboplatin or cisplatin with pemetrexed or a taxane is the chemotherapy foundation, given with immunotherapy or after targeted options are exhausted.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It spreads to and erodes bone: non-small-cell lung cancer frequently metastasises to the skeleton, causing lytic cortical bone destruction, pain and fractures treated with bone-protective agents.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Lymphoid islands predict its immunotherapy response: non-small-cell lung cancers bearing tertiary lymphoid structures with germinal-centre B-cell aggregates respond better to checkpoint blockade, the immunotherapy that transformed NSCLC care.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — A shared RET-fusion target: RET-rearranged non-small-cell lung cancer and RET-altered thyroid cancers both respond to selective RET inhibitors (selpercatinib, pralsetinib)—one druggable fusion across two organs.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Tobacco's twin malignancies: cigarette carcinogens that cause non-small-cell lung cancer are also excreted in urine to drive bladder cancer, so the two are classic field-cancerisation partners and a smoker often risks both.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver metastasis: NSCLC commonly spreads to the liver, seeding the hepatic lobule—a poor-prognosis site that also predicts reduced benefit from immunotherapy.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — KRAS across two cancers: KRAS—notably the G12C variant—drives lung adenocarcinoma and pancreatic cancer, and the KRAS-G12C inhibitors developed in NSCLC are now tested in pancreatic disease.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Cardiac immune toxicity and metastasis: immunotherapy for NSCLC can cause autoimmune myocarditis of the myocardium, and the tumour itself can metastasise to the heart and pericardium.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — A shared druggable kinase: ALK rearrangements in NSCLC and activating ALK mutations in neuroblastoma make the same target actionable across adult and paediatric cancer, so ALK inhibitors like lorlatinib cross between the two.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Seizures from brain spread: NSCLC is a leading source of brain metastases, and these lesions are a common cause of new-onset seizures and secondary epilepsy in patients with advanced disease.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — The benign mimic: pulmonary tuberculosis produces masses, cavities and lymphadenopathy that imitate lung cancer, the two coexist in smokers, and old TB scars can themselves seed scar carcinoma.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — Rare actionable fusion: NTRK gene fusions are uncommon but highly targetable drivers in NSCLC, treated with TRK inhibitors as part of its precision-oncology landscape.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Squamous PI3K activation: PIK3CA mutation and amplification activate PI3K signalling, especially in squamous NSCLC, a candidate therapeutic target.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplified aggression: MYC amplification drives proliferation and immune evasion in NSCLC and is associated with more aggressive, treatment-resistant disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT survival: AKT, activated downstream of EGFR and PIK3CA, drives NSCLC survival and underlies resistance to EGFR-targeted therapy.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: with CDKN2A loss common in NSCLC, cyclin D1-CDK4/6 activity pushes tumour cells through the G1 checkpoint, a candidate therapeutic vulnerability.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in hypoxic NSCLC drives angiogenesis and a treatment-resistant, metastatic phenotype linked to poor prognosis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — NSCLC tumors secrete CCL2 to recruit monocytes that become tumor-associated macrophages, building the myeloid niche that blunts T-cell responses and dampens checkpoint-inhibitor efficacy—an immunosuppressive arm orthogonal to the oncogene drivers.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β in the NSCLC stroma drives the epithelial-mesenchymal transition that fuels invasion and TKI resistance, while excluding T cells from the tumor to create the immunotherapy-resistant "cold" phenotype that limits checkpoint-inhibitor benefit.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Radiation and chemotherapy in NSCLC release cytosolic DNA that activates cGAS-STING, generating type-I interferon that can prime anti-tumor T cells—the mechanistic rationale for combining STING agonists or radiation with checkpoint blockade.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGFR1 amplification is a recurrent oncogenic event in squamous NSCLC, the histology that lacks the EGFR/ALK targets of adenocarcinoma, making FGFR inhibitors one of the few precision options in lung squamous-cell carcinoma.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4-CXCL12 signaling directs NSCLC metastasis to CXCL12-rich bone marrow, brain and adrenal niches, and sustains an immunosuppressive microenvironment that excludes T cells from the tumor.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Acquired loss-of-function mutations in JAK1/JAK2 render NSCLC cells unresponsive to interferon-γ, abolishing PD-L1 induction and antigen presentation—a key mechanism of acquired resistance to PD-1 blockade.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss is a recurrent event in NSCLC that unleashes the PI3K-AKT-mTOR axis already driven by PIK3CA and EGFR, promoting survival signaling and contributing to resistance against EGFR tyrosine-kinase inhibitors.
- `connects-to` → **[AXL Receptor Tyrosine Kinase](../../03-molecular/axl-receptor/README.md)** — AXL drives epithelial-mesenchymal transition and is upregulated in NSCLC escaping EGFR- and ALK-targeted therapy, a bypass survival pathway that motivates AXL inhibitors in combination regimens.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDKN2A loss and cyclin-D1 overexpression in NSCLC converge on CDK4/6 to inactivate RB and force the G1-S transition, the proliferative engine that makes CDK4/6 inhibitors an emerging strategy in RB-intact disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EGFR, ALK, KRAS, BRAF, MET, RET and FGFR (all already mapped) funnel into the MAPK-ERK cascade, the shared proliferative output of NSCLC's diverse oncogenic drivers.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA, AKT and PTEN already mapped) that sustains growth and survival signaling in NSCLC.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The CDK4/6-cyclin-D1 axis (mapped) inactivates RB to release E2F1, the transcription factor that executes the G1-S transition driving NSCLC proliferation.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Combined RB1 and TP53 loss drives the histologic transformation of EGFR-mutant adenocarcinoma to small-cell lung cancer, a notable mechanism of acquired resistance to EGFR inhibitors (CDK4/6 and CDKN2A already mapped).
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) sustains a tumor-promoting inflammatory microenvironment and contributes to therapy resistance in non-small cell lung cancer.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Cigarette-smoke- and infection-driven TLR-MyD88-NF-κB signaling (NF-κB already mapped) provides a chronic inflammatory drive in lung carcinogenesis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes invasion and immune evasion in non-small-cell lung cancer.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — LKB1 (STK11 mapped) activates AMPK to restrain anabolic growth, and its loss in NSCLC drives metabolic reprogramming and immunotherapy resistance.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) drives EMT, invasion and the immunosuppressive microenvironment of non-small-cell lung cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response central to the checkpoint immunotherapy that has transformed non-small-cell lung cancer treatment.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO tumor-suppressor activity, antagonized by EGFR/KRAS-driven PI3K-AKT signaling, is lost in the proliferative progression of non-small-cell lung cancer.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression silences tumor-suppressor genes and contributes to the epigenetic dysregulation of non-small-cell lung cancer.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells is the immune-clearance axis central to the checkpoint-immunotherapy response of non-small-cell lung cancer.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in non-small-cell lung cancer.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the smoking-associated inflammatory and immunosuppressive microenvironment of non-small-cell lung cancer.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the Wnt/β-catenin and survival signaling of non-small-cell lung cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of EGFR, MET, and other receptor tyrosine kinases (all already mapped) drives the invasion of non-small-cell lung cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic silencing of tumor-suppressor genes in non-small-cell lung cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of non-small-cell lung cancer cells.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of non-small-cell lung cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of non-small-cell lung cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of non-small cell lung cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of non-small cell lung cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of non-small cell lung cancer.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Bone-metastatic niche: NSCLC frequently metastasises to bone, where tumour-driven RANKL activates osteoclasts to cause skeletal-related events, the rationale for denosumab, and RANKL blockade also intersects with the immune microenvironment relevant to checkpoint therapy.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Antigen presentation: MHC class II on tumour and antigen-presenting cells shapes the CD4 T-cell help that underlies the checkpoint-inhibitor responses central to modern NSCLC therapy, and its loss is a mechanism of immune escape and immunotherapy resistance.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Chemotherapy execution: platinum-doublet chemotherapy, still a backbone of NSCLC treatment, kills tumour cells by triggering caspase-3-mediated apoptosis, and defects in this executioner pathway underlie chemoresistance.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Cellular immunotherapy: IL-2-driven T-cell expansion underlies the tumour-infiltrating-lymphocyte therapy now approved for advanced NSCLC and complements the checkpoint inhibitors (PD-1/CTLA-4 already mapped) central to its treatment.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Immunotherapy cardiotoxicity: the checkpoint inhibitors widely used in NSCLC can cause immune-mediated myocarditis, and troponin elevation helps detect this rare but often fatal complication, alongside pericardial spread of the tumour.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Paraneoplastic hypercalcaemia: squamous NSCLC commonly secretes PTH-related peptide, which acts like PTH to raise calcium (already mapped), causing the paraneoplastic hypercalcaemia that marks advanced disease.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia of malignancy: chronic disease, marrow involvement and chemotherapy lower haemoglobin in NSCLC, and the resulting anaemia adds to the breathlessness and fatigue that already burden these patients.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tobacco oxidative damage: cigarette smoke and chronic inflammation generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage (NRF2 already mapped) drives the carcinogenesis of smoking-related NSCLC.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Cancer pain and dyspnoea: opioids acting on the mu-opioid receptor relieve the pain of bone metastases and the refractory breathlessness of advanced NSCLC, a mainstay of its palliative and supportive care.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 carcinogenesis: tobacco induces cyclooxygenase-2 and prostaglandin E2 in the airway, promoting the proliferation, angiogenesis (VEGF already mapped) and immunosuppression of lung carcinogenesis, and COX-2 has been studied as a target in NSCLC.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hepatic and adrenal metastasis: NSCLC commonly metastasises to the liver and adrenal glands, the visceral spread that defines stage IV disease and shapes systemic therapy.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — PTHrP hypercalcaemia: squamous NSCLC characteristically secretes parathyroid-hormone-related peptide (PTH already mapped), raising calcium to cause the humoral hypercalcaemia of malignancy with its confusion and renal impairment.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment that the checkpoint immunotherapy central to NSCLC must overcome.
- `connects-to` → **[Adrenal gland](../../06-organ/adrenal-gland/README.md)** — Adrenal metastasis: the adrenal glands are a characteristic site of NSCLC metastasis, the visceral spread that defines stage IV disease alongside the liver (already mapped) and brain (already mapped).
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy: stereotactic body photon radiotherapy cures early inoperable NSCLC, and concurrent chemoradiotherapy treats stage III disease, photon radiation a mainstay of the non-metastatic tumour.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 microenvironment: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the immunosuppressive microenvironment of non-small-cell lung cancer.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Cancer cachexia: leptin is the adipokine of the cancer cachexia (the weight loss) of NSCLC, and part of the obesity-paradox in the immunotherapy response.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic-cachexia adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-cachexia axis of non-small-cell lung cancer.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Cachexia-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the cancer cachexia and metabolic axis of non-small-cell lung cancer.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the checkpoint (PD-1 already mapped) immunotherapy of non-small-cell lung cancer.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm exploited by the checkpoint immunotherapy of non-small-cell lung cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the anti-tumour immune microenvironment of non-small-cell lung cancer.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of non-small-cell lung cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of non-small-cell lung cancer.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of non-small-cell lung cancer.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of non-small-cell lung cancer.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate cytotoxicity: the NK cells (perforin already mapped) provide the innate anti-tumour surveillance complementing the CD8 (already mapped) checkpoint-immunotherapy response in non-small-cell lung cancer.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts the checkpoint-immunotherapy (PD-1 already mapped) response of non-small-cell lung cancer.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of non-small-cell lung cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Tumour complement: the complement C3 activation contributes to the inflammatory and immunosuppressive dimension of the non-small-cell-lung-cancer microenvironment.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Airway alarmin: TSLP released by the inflamed bronchial epithelium drives mast-cell and dendritic-cell activation in the non-small-cell lung cancer stroma, promoting the type-2 microenvironment that dampens anti-tumour immunity.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM invasion driver: periostin, upregulated in the non-small-cell lung cancer stroma downstream of TGF-β, promotes tumour cell adhesion, invasion and metastatic colonisation of the pleura and bone.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Immune-evasion axis: histamine H2-receptor signalling on non-small-cell lung cancer cells and their stromal mast cells promotes tumour immune evasion and angiogenesis via the PGE-2 and VEGF already mapped.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Tumour microenvironment kinin: bradykinin generated by the kallikrein-kinin system in the non-small-cell lung cancer stroma promotes vasodilation and macrophage activation, amplifying the inflammatory tumour microenvironment.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation: C1-esterase inhibitor restrains the complement and contact-activation pathways whose dysregulation in the NSCLC microenvironment sustains the C3 (already mapped) inflammatory cascade.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia correction: erythropoietin addresses cancer- and chemotherapy-induced anaemia in NSCLC; its receptor (EPOR) on tumour cells may additionally modulate tumour-cell survival and resistance to platinum regimens.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Lung tumour melatonin: melatonin inhibits NSCLC proliferation and EMT (already mapped) through MT1/MT2-mediated cAMP suppression and Wnt/β-catenin (already mapped) inhibition, sensitising NSCLC cells to EGFR-targeted (EGFR already mapped) and platinum therapies.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — NSCLC androgen axis: testosterone via androgen receptor signalling modulates PD-L1 (already mapped) expression and the immunosuppressive microenvironment in NSCLC; AR signalling intersects KRAS (already mapped) and EGFR (already mapped) tumour growth pathways.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — NSCLC neuroendocrine serotonin: serotonin co-produced by neuroendocrine-differentiated NSCLC cells activates 5-HT2 and 5-HT4 receptors to promote KRAS (already mapped)-driven proliferation and mTOR (already mapped) pro-survival signalling in non-small-cell lung cancer.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — NSCLC prolactin: prolactin via JAK2/STAT3 (already mapped) and mTOR (already mapped) activates NSCLC tumour cells and macrophages (already mapped), promoting PD-L1 (already mapped) upregulation and immunosuppressive microenvironment in non-small-cell lung cancer.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — NSCLC oxytocin: oxytocin receptors on NSCLC tumour and mast cells (already mapped) couple to Gαq-PKC, activating KRAS (already mapped) and EGFR (already mapped) downstream proliferative signalling in non-small-cell lung cancer.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — NSCLC vasopressin: vasopressin via V1a receptors on NSCLC stroma and macrophages (already mapped) activates Gαq-PLC-IP3 signalling, cross-activating VEGF (already mapped) and mTOR (already mapped) angiogenic cascades in non-small-cell lung cancer.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — NSCLC selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the NSCLC tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — NSCLC iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune surveillance; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of NSCLC.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — NSCLC sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) anti-tumour cascade of NSCLC.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — NSCLC copper: copper-dependent enzymes in macrophage (already mapped) and mast-cell (already mapped) immunity; copper imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade promoting T-cytotoxic (already mapped) exhaustion in NSCLC.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — NSCLC zinc: zinc co-factors in macrophage (already mapped) and neutrophil (already mapped) metalloproteases; zinc depletion exacerbates NF-κB (already mapped) and IL-6 (already mapped) tumour-permissive inflammation while impairing T-cytotoxic (already mapped) killing in NSCLC.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — NSCLC potassium: potassium efflux gates macrophage (already mapped) and mast-cell (already mapped) NLRP3 inflammasome; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling while suppressing T-cytotoxic (already mapped) function in NSCLC.

[^soria-2018-osimertinib-flaura]: Soria JC, Ohe Y, Vansteenkiste J, et al. Osimertinib in untreated EGFR-mutated advanced non-small-cell lung cancer. *N Engl J Med.* 2018;378(2):113-125. [doi:10.1056/NEJMoa1713137](https://doi.org/10.1056/NEJMoa1713137) · [PubMed 29151359](https://pubmed.ncbi.nlm.nih.gov/29151359/)
[^reck-2016-pembrolizumab-keynote024]: Reck M, Rodríguez-Abreu D, Robinson AG, et al. Pembrolizumab versus chemotherapy for PD-L1-positive non-small-cell lung cancer. *N Engl J Med.* 2016;375(19):1823-1833. [doi:10.1056/NEJMoa1606774](https://doi.org/10.1056/NEJMoa1606774) · [PubMed 27718347](https://pubmed.ncbi.nlm.nih.gov/27718347/)
[^halliday-2023-kras-nsclc]: Riely GJ, Ou SHI, Rybkin I, et al. KRYSTAL-1: activity and preliminary pharmacodynamic analysis of adagrasib in patients with advanced NSCLC harboring KRAS G12C mutation. *J Thorac Oncol.* 2022;17(10):1248-1258. [doi:10.1016/j.jtho.2022.06.020](https://doi.org/10.1016/j.jtho.2022.06.020) · [PubMed 35817313](https://pubmed.ncbi.nlm.nih.gov/35817313/)
