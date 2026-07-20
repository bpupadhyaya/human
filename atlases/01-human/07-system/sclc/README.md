---
schema: human-scale-entry/v1
id: sclc
name: Small Cell Lung Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Small cell lung cancer is a high-grade neuroendocrine carcinoma with near-universal RB1 and TP53 loss; atezolizumab or durvalumab + carboplatin/etoposide is first-line for extensive stage; DLL3-targeting tarlatamab is approved for relapsed disease; 5-year OS <10%."
aliases: ["SCLC", "small cell lung cancer", "small cell carcinoma", "limited stage SCLC", "extensive stage SCLC", "oat cell carcinoma", "SCLC-A", "neuroendocrine lung cancer", "lurbinectedin SCLC", "tarlatamab SCLC"]
sources:
  - id: horn-2018-impower133
    type: peer-reviewed
    cite: "Horn L, Mansfield AS, Szczęsna A, et al. First-line atezolizumab plus chemotherapy in extensive-stage small-cell lung cancer. N Engl J Med. 2018;379(23):2220-2229."
    doi: "10.1056/NEJMoa1809064"
    pmid: "30280641"
    url: "https://doi.org/10.1056/NEJMoa1809064"
  - id: paz-ares-2019-caspian
    type: peer-reviewed
    cite: "Paz-Ares L, Dvorkin M, Chen Y, et al. Durvalumab plus platinum-etoposide versus platinum-etoposide in first-line treatment of extensive-stage small-cell lung cancer (CASPIAN): a randomised, controlled, open-label, phase 3 trial. Lancet. 2019;394(10212):1929-1939."
    doi: "10.1016/S0140-6736(19)32222-6"
    pmid: "31590988"
    url: "https://doi.org/10.1016/S0140-6736(19)32222-6"
cross_links:
  - target: 01-human/03-molecular/dll3
    relation: connects-to
    note: "DLL3 overexpressed in >80% of SCLC (especially ASCL1-high subtype); drives Notch cis-inhibition → neuroendocrine identity; tarlatamab (DLL3×CD3 bispecific, FDA 2024): ORR 40%, CNS response 52%; first immunotherapy specifically approved for relapsed SCLC."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB1 biallelic loss in >90% of SCLC is the defining molecular event; RB1 loss releases E2F → ASCL1 → neuroendocrine program (DLL3, synaptophysin, chromogranin); RB1 loss also confers vulnerability to CDK4/6 inhibitor combinations in experimental models."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Atezolizumab (PD-L1) + carboplatin/etoposide (IMpower133: OS 12.3 vs 10.3 months) and durvalumab + platinum/etoposide (CASPIAN: OS 12.9 vs 10.5 months) are approved first-line regimens; PD-L1 expression does not predict benefit in SCLC; SCLC is immunologically cold."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 biallelic mutation co-occurs with RB1 loss in >90% of SCLC; p53 loss → unchecked DNA damage response → rapid proliferation; platinum/etoposide sensitivity partly attributable to p53-null apoptotic priming; SCLC lacks targetable TP53 restoration options."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Small cell lung cancer (~13-15% of lung cancer) is the most aggressive subtype, smoking-driven, arising centrally as a bulky hilar mass that often causes superior vena cava syndrome; it disseminates early, so ~70% present extensive-stage with brain, liver, or bone metastases."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "SCLC and NSCLC are the two divisions of lung cancer with opposite therapeutic logic: NSCLC is rich in targetable drivers, whereas SCLC has near-universal RB1 and TP53 loss with no actionable oncogene, relying on platinum-etoposide, immunotherapy, and DLL3-directed tarlatamab."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "SCLC is the poorly differentiated, high-grade end of the pulmonary neuroendocrine spectrum (Ki-67 >50%, synaptophysin/INSM1+), unlike indolent carcinoid NETs; whereas SSTR2-high NETs use somatostatin analogs and PRRT, SCLC is treated as a chemo-driven carcinoma."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Small cell lung cancer and tuberculosis both present as a cavitary lung lesion with weight loss, cough, and hemoptysis in older smokers, sharing a radiographic differential — neuroendocrine tumor versus granulomatous infection — resolved by biopsy and microbiology."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "SCLC's neuroendocrine identity drives paraneoplastic neurology: tumor cells express neuronal antigens, so anti-neuronal antibodies attack the nervous system — anti-Hu encephalomyelitis and Lambert-Eaton myasthenic syndrome (anti-VGCC) — often before the cancer is found."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain is a defining SCLC battleground: ~50% develop brain metastases from its early spread, so prophylactic cranial irradiation is offered to responders; SCLC also causes paraneoplastic limbic encephalitis, and DLL3-targeted tarlatamab achieves CNS responses."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is integral to small cell lung cancer: concurrent thoracic photon radiation with platinum chemotherapy is standard for limited-stage disease (often twice-daily), exploiting SCLC's marked radiosensitivity—with cranial irradiation added for brain spread."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Small cell lung cancer and retinoblastoma are linked by RB1 loss: the tumor-suppressor that, germline-mutated, causes childhood retinoblastoma is inactivated (with TP53) in nearly all SCLC—one gene whose loss drives cancers in utterly different tissues and ages."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages populate the immunosuppressive SCLC microenvironment: despite its high mutational burden from smoking, SCLC responds only modestly to immunotherapy, partly because M2 macrophages and an exhausted, 'cold' immune milieu blunt T-cell attack."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Small-cell lung cancer is the most tobacco-driven lung cancer: carbon-based smoke carcinogens (PAHs, nitrosamines) cause near-universal TP53 and RB1 loss, so SCLC almost never arises in never-smokers—the tightest smoking-cancer link among lung tumors."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "SCLC and head and neck cancer arise from the same tobacco field cancerization: heavy smoking injures the entire aerodigestive epithelium, so a patient with one is at high risk of the other—both smoking-driven cancers whose prevention rests on cessation."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "SCLC and esophageal squamous cancer share smoking and alcohol as drivers: both stem from carcinogen exposure of the aerodigestive tract, and esophageal small-cell carcinoma is a rare aggressive variant—reminders that tobacco's reach spans the chest's epithelia."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC amplification drives the most aggressive SCLC: alongside near-universal TP53 and RB1 loss, MYC-family amplification defines a fast-proliferating subtype, so SCLC's relentless growth and early metastasis trace to these few but powerful genetic hits."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "SCLC metastasizes early to the adrenal glands: it spreads widely at diagnosis—to liver, brain, bone and characteristically the adrenals—so an adrenal mass with a lung primary signals extensive-stage disease, and SCLC can also ectopically secrete ACTH."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "SCLC is the classic cause of paraneoplastic neurological syndromes: it provokes antibodies (anti-Hu, anti-VGCC) that attack the nervous system, causing Lambert-Eaton myasthenic syndrome and encephalitis—sometimes appearing before the tumor is found."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Beyond its tumor biology, SCLC drives paraneoplastic autoimmunity: it expresses neuronal antigens the immune system attacks, while its high mutational burden makes it responsive to checkpoint immunotherapy—so immunity both harms (autoimmunity) and helps (treatment)."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "SCLC's neuroendocrine cells secrete ectopic hormones, causing endocrine paraneoplastic syndromes: ADH drives SIADH with hyponatremia and ACTH produces Cushing's—so metabolic disturbances often herald or complicate the cancer before imaging finds it."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a common SCLC metastatic site: this aggressive cancer spreads early and widely, and liver involvement marks extensive-stage disease, worsens prognosis, and can impair drug metabolism—so staging scans routinely scrutinize the liver."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "SCLC is now attacked with T-cell engagers: tarlatamab, a bispecific antibody linking the tumor's DLL3 to CD3 on cytotoxic T cells, redirects them to kill small-cell lung cancer—a new option after chemotherapy in this aggressive disease."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Small-cell lung cancer classically causes SIADH: the tumor ectopically secretes vasopressin (ADH), driving water retention and hyponatremia, so unexplained low sodium in a smoker can be the presenting clue to SCLC."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "SCLC is a leading cause of ectopic ACTH syndrome: the neuroendocrine tumor secretes ACTH, producing a rapid-onset paraneoplastic Cushing's with hypokalemia and hyperglycemia rather than the classic body changes—signaling aggressive disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Small cell lung cancer can paralyze through calcium channels: in Lambert-Eaton syndrome, antibodies against the tumor's calcium channels cross-react at nerve terminals, cutting calcium-triggered acetylcholine release and causing the weakness that often precedes diagnosis."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Small cell lung cancer is shaped by Notch and its ligand DLL3: Notch is largely silenced in these neuroendocrine tumors, and the resulting high DLL3 on the cell surface is the target of new drugs like tarlatamab."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Small cell lung cancer hides behind regulatory T cells: a suppressive microenvironment limits the immune attack, so although checkpoint immunotherapy now adds to chemo, Tregs are part of why responses are often brief in this aggressive cancer."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Small cell lung cancer classically drops the blood sodium: ectopic vasopressin from the tumor causes SIADH, so unexplained hyponatremia in a smoker is a clue that can lead to the diagnosis and tracks with tumor burden."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: connects-to
    note: "Small cell lung cancer attacks the neuromuscular junction from afar: antibodies against the tumor cross-react with calcium channels there, causing Lambert-Eaton myasthenic syndrome—a paraneoplastic weakness that can precede the cancer's discovery."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells shape the immune fight against small cell lung cancer: as antigen-presenters they prime the T-cell response checkpoint drugs now add to chemo, and their dysfunction helps explain the brief responses in this aggressive tumor."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Small cell lung cancer can drop potassium: by secreting ectopic ACTH it drives a paraneoplastic Cushing's whose cortisol excess makes the kidneys waste potassium into hypokalemia."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Small cell lung cancer can blind through the eye: cancer-associated retinopathy, a paraneoplastic autoimmune attack on the retina, causes progressive vision loss that can precede the tumor's discovery."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Small cell lung cancer floods the bone marrow: this aggressive tumor frequently metastasizes to the marrow, crowding out blood production and marking the widespread disease typical at diagnosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals SCLC's neuroendocrine soul: scattered dense-core neurosecretory granules — tiny membrane-bound packets of hormone — mark these small dark cells as neuroendocrine, the trait behind their paraneoplastic syndromes."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "SCLC can flood the body with cortisol: its ectopic ACTH drives the adrenals to overproduce cortisol, causing a rapidly evolving Cushing syndrome of weakness, swelling, and low potassium rather than the classic slow body changes."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "SCLC turns the immune system against the nerves: anti-Hu and related antibodies meant for the tumor also strike peripheral neurons, producing a paraneoplastic sensory neuronopathy that can appear before the cancer is found."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "SCLC's intense chemotherapy empties the marrow: the platinum-etoposide that this fast-growing cancer demands drops neutrophils into a neutropenia, so febrile neutropenia and growth-factor support are constant concerns of treatment."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "The platinum backbone leaks magnesium away: cisplatin injures the kidney's tubules, which then waste magnesium, so levels are checked and repleted through the rounds of SCLC chemotherapy."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Immunotherapy now joins the attack on SCLC: adding a PD-L1 checkpoint inhibitor to first-line chemotherapy releases the brakes on T cells, letting helper and cytotoxic T cells mount a response that modestly extends survival in extensive-stage disease."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies pervade SCLC: synaptophysin, chromogranin, and TTF-1 stains with a high Ki-67 confirm the neuroendocrine tumor, anti-Hu and anti-VGCC autoantibodies drive its paraneoplastic syndromes, and an anti-PD-L1 antibody is now added to chemotherapy."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The aggressive tumor and its chemotherapy thin the red cells: marrow infiltration plus the cisplatin-etoposide regimen depress erythrocyte production into an anemia that, with the disease's rapid course, often needs transfusion support."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "A central SCLC can throttle the great vein: a bulky mediastinal tumor compresses the superior vena cava, swelling the face and neck with engorged skin veins, while paraneoplastic dermatomyositis can rash the skin as a clue to the hidden cancer."
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "MYC-family amplification splits SCLC into subtypes: alongside MYC, amplification of MYCN or MYCL defines molecular groups with distinct biology and drug sensitivities, layered on the near-universal loss of both RB1 and p53."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Few cancers clot like SCLC: this aggressive tumor pours out procoagulants and, with chemotherapy and central venous catheters, drives one of the highest rates of deep-vein thrombosis and pulmonary embolism among solid cancers."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "The platinum-etoposide chemotherapy empties the marrow: it suppresses platelet production into thrombocytopenia, a dose-limiting toxicity that raises bleeding risk through the rapid, intensive cycles SCLC demands."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Immunotherapy reached even this hard target: blocking CTLA-4 alongside PD-L1 adds a modest survival gain in extensive-stage SCLC, releasing T cells against a tumor whose heavy smoking-driven mutation load makes it visible to the immune system."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "It shares its cause with the airways' disease: the same heavy tobacco smoking that drives SCLC produces COPD, so the two frequently coexist, and the reduced lung reserve of COPD complicates treating the cancer."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "It grows a fast, leaky blood supply: SCLC is intensely angiogenic, pushing endothelial cells to build the vasculature that fuels its rapid doubling and early spread — the rationale behind testing antiangiogenic drugs against it."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 sustains the neuroendocrine tumor: JAK-STAT3 signaling drives SCLC proliferation and immune evasion, part of the signaling that keeps this fast-growing cancer alive between its near-universal RB1 and p53 losses."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB feeds chemoresistance: after an initial dramatic chemo response, SCLC relapses with NF-κB-supported survival signaling, part of why this tumor so reliably returns resistant within months."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A central tumor and intense chemo invite sepsis: post-obstructive pneumonia behind a bronchial SCLC, plus the deep neutropenia of platinum-etoposide cycles, make pneumonia and sepsis frequent complications."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Tumor cytokines waste the body: SCLC secretes IL-6 and related cytokines that drive the profound cachexia, fever and inflammatory markers typical of this aggressive neuroendocrine cancer at presentation."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Inflammation and marrow involvement drop the hemoglobin: the IL-6 milieu of SCLC raises hepcidin while frequent bone-marrow metastases crowd the marrow, producing an anemia of chronic disease layered on chemotherapy myelosuppression."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "A hypercoagulable cancer can strike the brain: SCLC's strong Trousseau-type prothrombotic state, with non-bacterial thrombotic endocarditis and arterial emboli, can cause ischemic stroke alongside its common brain metastases."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its platinum chemotherapy scars the kidneys: cisplatin, central to SCLC regimens, is directly nephrotoxic, and the tubular and electrolyte injury it causes can leave lasting chronic kidney impairment."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Cavitating tumor and chemo neutropenia open the lung to mold: post-obstructive collapse plus the deep neutropenia of platinum-etoposide therapy let inhaled Aspergillus invade as pulmonary aspergillosis in the damaged lung."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An aggressive, smoking-related cancer weighs on mood: SCLC's rapid course, poor prognosis and breathlessness, with the stigma of smoking and frequent brain metastases, contribute to high rates of depression."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "A tumour plugging the airway breeds pneumonia: a bronchus obstructed by central SCLC traps secretions distal to it, and post-obstructive pneumonia — classically pneumococcal — is a common complication."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Both the tumour and its chemo attack the nerves: SCLC causes paraneoplastic sensory neuropathy via anti-Hu antibodies, and the platinum chemotherapy adds its own painful peripheral neuropathy."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A fast, breathless, relapsing cancer breeds dread: the rapid growth, near-inevitable relapse and dyspnoea of SCLC fuel intense anxiety alongside the depression it so often brings."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It is a central lung cancer that strangles the airway: SCLC arises centrally and grows fast, causing bronchial obstruction, post-obstructive pneumonia and superior vena cava syndrome."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It floods the liver with deposits: SCLC metastasises early and avidly to the liver, a common site at presentation that drives its dismal prognosis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It spreads to bone and weakens muscle: SCLC metastasises to the skeleton causing pain and fractures, and its paraneoplastic Lambert-Eaton myasthenic syndrome causes proximal muscle weakness."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It floods the nodes early: small cell lung cancer spreads rapidly and extensively to mediastinal and distant lymph nodes, central to its limited-versus-extensive staging."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Central tumours strangle the great veins: a central SCLC commonly causes superior vena cava obstruction with facial swelling and distended veins, and can invade the pericardium causing effusion."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its drugs and hormones strain the kidney: the platinum chemotherapy for SCLC is nephrotoxic, and paraneoplastic SIADH causes profound hyponatraemia needing careful correction."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Immunotherapy joined its chemo: checkpoint inhibitors such as atezolizumab and durvalumab added to platinum-etoposide chemotherapy modestly extend survival in small cell lung cancer."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It signals through paraneoplastic skin signs: small cell lung cancer can cause dermatomyositis and acanthosis nigricans, cutaneous clues to the underlying tumour."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Treatment threatens fertility: the intensive platinum chemotherapy for small cell lung cancer can impair fertility, and the cancer rarely metastasises to the ovaries."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Platinum-etoposide is the backbone: SCLC is exquisitely chemosensitive at first, with platinum-etoposide producing rapid responses, but it almost always relapses within months as chemoresistant disease, when topotecan or lurbinectedin follow."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "It triggers Lambert-Eaton: about half of Lambert-Eaton myasthenic syndrome is paraneoplastic to SCLC, with anti-VGCC antibodies causing proximal weakness that improves with use — the mirror image of, and key differential for, myasthenia gravis."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "First-line immunotherapy adds months: adding atezolizumab or durvalumab to chemotherapy and continuing it as maintenance is now standard in extensive-stage SCLC, giving a real but modest survival gain that proves durable in only a minority."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The price of protecting the brain: SCLC metastasises early to the brain, so prophylactic cranial irradiation is offered—but it damages the hippocampus and impairs memory, driving hippocampal-avoidance techniques."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It floods the liver fast: small-cell lung cancer metastasises early and widely, with the liver a frequent site where deposits fill the hepatic lobules and herald the extensive-stage disease that dominates at diagnosis."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Two MYCN-driven neuroendocrine cancers: small-cell lung cancer and neuroblastoma are both small-round-blue-cell tumours with neuroendocrine differentiation and frequent MYC/MYCN amplification, explaining their aggressive, chemo-sensitive-but-relapsing course."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Central origin, early spread: SCLC arises centrally near the bronchi and disseminates early, seeding the alveolar bed and distant organs—the most aggressive lung cancer, usually widespread at diagnosis."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Two heavily-smoking cancers: SCLC and bladder cancer share tobacco causation, and small-cell neuroendocrine carcinoma can also arise in the bladder, mirroring the lung tumour's aggressive histology."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Why immunotherapy helps: SCLC's heavy smoking-driven mutation load and tertiary lymphoid structures make it visible to T cells, so adding PD-L1 (and CTLA-4) blockade improves survival in extensive-stage disease."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Seizures from two directions: SCLC frequently metastasises to the brain and also causes paraneoplastic limbic encephalitis (anti-Hu), both producing seizures and secondary epilepsy in advanced disease."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Paraneoplastic neuronopathy: anti-Hu antibodies in SCLC destroy dorsal-root-ganglion neurons and their axonal transport, causing a severe subacute sensory neuronopathy that can precede the cancer's discovery."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Electrolytes and the heart: SCLC's ectopic hormones disturb the heart's conduction—SIADH-driven hyponatraemia and ectopic-ACTH hypokalaemia destabilise rhythm—while paraneoplastic autonomic neuropathy adds to the risk."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Molecular subtype: YAP1 defines a distinct SCLC subgroup (SCLC-Y) with a more inflamed, mesenchymal phenotype and differing chemotherapy sensitivity."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic dependency: EZH2 is a key epigenetic vulnerability in SCLC, enforcing the neuroendocrine programme and chemoresistance—an actionable target."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis evasion: SCLC strongly expresses anti-apoptotic BCL-2, a long-standing therapeutic target exploited by BH3-mimetic drugs."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT survival: PI3K/AKT activation sustains the survival of small-cell lung cancer cells, contributing to its rapid relapse after initial chemosensitivity."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Unrestrained cell cycle: with RB1 loss near-universal in SCLC, the cell cycle runs unchecked, and the MYC-driven proliferation makes it one of the fastest-growing cancers."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the rapidly growing, hypoxic SCLC drives angiogenesis and the aggressive, metastatic phenotype that defines the disease."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: SCLC reactivates telomerase (TERT) to maintain telomeres through its breakneck proliferation, granting the unlimited replicative capacity that complements its RB1 and TP53 loss."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Neuroendocrine RTK: SCLC commonly expresses c-KIT (CD117), a receptor tyrosine kinase reflecting its neuroendocrine lineage; although imatinib trials failed, KIT marks the stem-like, treatment-resistant biology of the tumour."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Replication-stress immunity: the high replication stress and DNA damage of SCLC generate cytosolic DNA that activates cGAS-STING, the innate-immune rationale for combining PARP inhibitors or chemotherapy with checkpoint blockade."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "DNA-repair dependence: the genomic instability of RB1/TP53-null SCLC leaves it reliant on homologous-recombination and replication-stress repair, the basis for the high PARP expression that makes SCLC a leading candidate for PARP inhibition."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Neuroendocrine receptor: as a high-grade neuroendocrine tumour SCLC can express somatostatin receptor SSTR2, the target for DOTATATE imaging and a rationale for peptide-receptor radionuclide approaches in the neuroendocrine fraction of these tumours."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Lambert-Eaton syndrome: SCLC is the classic trigger of Lambert-Eaton myasthenic syndrome, where antibodies against presynaptic P/Q-type calcium channels reduce acetylcholine release at the neuromuscular junction, causing the paraneoplastic proximal weakness."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Unrestrained proliferation: near-universal RB1 loss in SCLC (RB1 already mapped) releases E2F1-driven transcription, the engine of unchecked cell-cycle entry behind the explosive growth of this neuroendocrine carcinoma."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemo-response then resistance: SCLC is strikingly chemosensitive at first, undergoing caspase-3-mediated apoptosis to etoposide-platinum, but rapidly evolves apoptotic resistance that drives its near-universal relapse."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K survival axis: PI3K-AKT-mTOR signalling (AKT already mapped) is recurrently activated in SCLC and supports growth and survival, a targetable dependency beyond the defining RB1/TP53 loss."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR effector: mTOR is the growth-controlling output of the PI3K-AKT axis (PIK3CA and AKT mapped) recurrently activated in SCLC, integrating the survival signalling layered on its RB1/TP53 loss."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Angiogenesis: SCLC is a highly vascular, rapidly growing tumour driven by VEGF-mediated angiogenesis, the basis for anti-angiogenic agents combined with chemotherapy."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy killing: the DLL3-CD3 bispecific tarlatamab (DLL3 mapped) and checkpoint inhibitors redirect cytotoxic T cells to kill SCLC through perforin and granzyme."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Survival microenvironment: IL-6-JAK-STAT3 signalling (IL-6 and STAT3 already mapped) supports the survival and immunosuppressive microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Smoking oxidative defence: NRF2 antioxidant signalling, induced by cigarette-smoke oxidants, contributes to the rapid proliferation and chemoresistance of small cell lung cancer."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Smoking-driven inflammation: cigarette-smoke-driven TLR-MyD88-NF-κB signalling (NF-κB already mapped) provides a chronic inflammatory drive in the lung carcinogenesis underlying small cell lung cancer."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 contributes to the invasion, metastasis and immune evasion of small cell lung cancer."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β signalling shapes the immunosuppressive microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling provides a proliferative input to small cell lung cancer downstream of receptor tyrosine kinases including KIT (KIT mapped)."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of small cell lung cancer, relevant to its checkpoint immunotherapy."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the neuroendocrine differentiation and immunosuppressive microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by PI3K-AKT signalling, modulate the survival and chemoresistance of small cell lung cancer."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the MYC stability and survival signaling of small cell lung cancer."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the smoking-associated inflammatory and immunosuppressive microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling contributes to the invasive and metastatic behavior of small cell lung cancer."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 regulation (p53 already mapped) participates in the apoptotic control of the near-universally TP53-mutant small cell lung cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of small cell lung cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and chemoresistance of small cell lung cancer cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of small cell lung cancer."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of small cell lung cancer."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of small cell lung cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy target: small cell lung cancer is now treated with checkpoint inhibitors added to chemotherapy, and MHC class II antigen presentation shapes the T-cell response, with its frequent downregulation contributing to the tumour's immune evasion."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Autocrine growth loop: small cell lung cancer cells express IGF-1 receptor and drive an autocrine IGF-1/IGF-1R signalling loop that sustains proliferation and survival, a growth-factor dependency explored as a therapeutic vulnerability."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Ectopic neuroendocrine secretion: as a neuroendocrine tumour small cell lung cancer can ectopically secrete calcitonin alongside ACTH and vasopressin (both already mapped), a paraneoplastic hormone output reflecting its chromaffin-like differentiation."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Immunotherapy: IL-2-driven T-cell expansion complements the checkpoint inhibitors (PD-1/CTLA-4 already mapped) now added to chemotherapy for small cell lung cancer, one of the few advances in a disease with otherwise poor durable control."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis: small cell lung cancer is highly chemosensitive with rapid, bulky responses, and the resulting tumour-lysis syndrome releases purines that xanthine oxidase converts to uric acid, managed with allopurinol or rasburicase."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia: the intensive chemotherapy and marrow involvement of small cell lung cancer suppress erythropoiesis, lowering haemoglobin and causing the anaemia that adds to the fatigue of this aggressive disease."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Tumour-lysis acidosis: the rapid, bulky response of chemosensitive small cell lung cancer releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate already mapped), part of its acute metabolic risk."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), part of the immune evasion that limits the durability of checkpoint benefit in small cell lung cancer."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Cancer pain and dyspnoea: opioids acting on the mu-opioid receptor relieve the pain of bone metastases and the refractory breathlessness of advanced small cell lung cancer, a mainstay of its palliative care."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 carcinogenesis: tobacco induces cyclooxygenase-2 and prostaglandin E2 in the airway, promoting the proliferation and immunosuppression of the carcinogenesis of small cell lung cancer, whose universal TP53 and RB1 loss (already mapped) it compounds."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive microenvironment of small cell lung cancer."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia of malignancy: the chronic disease and the platinum-etoposide chemotherapy of small cell lung cancer cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Cancer cachexia: the profound weight loss and cancer cachexia (IL-6 already mapped) of small cell lung cancer are reflected in the fall in the adipokine leptin as the adipose tissue is depleted."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine crosstalk: adiponectin, with leptin (already mapped), links the metabolic and adipose state to the systemic effects and cachexia of small cell lung cancer."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Cachexia adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the cachexia (IL-6 already mapped) of small cell lung cancer."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Bone metastases: the cortical bone is a common site of small cell lung cancer metastasis, causing the bone pain and pathological fractures of the extensive-stage disease."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and produces the anaemia of chronic disease (haemoglobin already mapped) of the small cell lung cancer cachexia."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the checkpoint (PD-1 already mapped) immunotherapy of small cell lung cancer."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune response to small cell lung cancer, engaged by the tarlatamab (DLL3 already mapped) T-cell engager."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the small-cell-lung-cancer immune microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immunologically cold small-cell-lung-cancer microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of small cell lung cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate cytotoxicity: the NK cells (perforin already mapped) provide the innate anti-tumour surveillance within the immunologically cold microenvironment of small cell lung cancer."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling recruits and polarises the myeloid-derived suppressor cells that reinforce the immunosuppression of the small-cell-lung-cancer microenvironment."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Central complement: the complement C3, upstream of the C5aR1 (already mapped), is the pivot of the complement activation within the immunosuppressive small-cell-lung-cancer microenvironment."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 (with C3 and C5aR1 already mapped) generates the C5a that recruits the myeloid-derived suppressor cells of the small-cell-lung-cancer microenvironment."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the sparse tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, marks the rare immune-responsive subset of the immunologically cold small cell lung cancer."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Bronchial epithelial alarmin: TSLP released from the bronchial epithelium activates mast cells and dendritic cells, promoting the immunosuppressive microenvironment of small cell lung cancer and the type-2 cytokine skewing that limits anti-tumour immunity."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Chemotherapy anaemia: erythropoietin corrects the severe anaemia from etoposide/platinum chemotherapy in small cell lung cancer, with EPOR expression on neuroendocrine SCLC cells raising the question of direct trophic signalling."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Neuroendocrine histamine: small cell lung cancer cells, as neuroendocrine tumours, can co-secrete histamine alongside the ectopic ACTH, ADH and other hormones causing the paraneoplastic syndromes characteristic of the disease."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin paraneoplastic crosstalk: bradykinin, generated by the kallikrein-kinin system in the SCLC tumour microenvironment, amplifies vascular permeability and neurogenic pain via B2 receptors on neuroendocrine cells, contributing to paraneoplastic neuropathy."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement-contact regulation: C1-esterase inhibitor restrains the classical complement C1 (C3/C5/C5aR1 already mapped) and the contact system activated in the SCLC microenvironment, modulating complement-dependent tumour immune surveillance."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Neuroendocrine ECM scaffold: periostin secreted by fibroblastic stroma of small cell lung cancer promotes SCLC-cell integrin-αv signalling and survival, reinforcing the desmoplastic tumour-microenvironment architecture of the disease."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "SCLC melatonin: melatonin, co-secreted by neuroendocrine SCLC cells, suppresses tumour proliferation via MT1/MT2 receptor-mediated inhibition of cAMP/PKA signalling; it also amplifies NK-cell (already mapped) cytotoxicity against the immunologically cold tumour microenvironment."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "SCLC testosterone: androgen receptor in a subset of SCLC drives tumour proliferation through MYC (already mapped) upregulation and Rb1 (already mapped) pathway crosstalk; androgen-axis suppression is a candidate therapeutic strategy for AR-positive small cell lung cancer."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SCLC serotonin: serotonin is co-produced by neuroendocrine SCLC cells alongside ectopic ACTH (already mapped), and autocrine 5-HT1/2 receptor signalling amplifies tumour-cell proliferation and survival, contributing to carcinoid-like paraneoplastic manifestations."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "SCLC oxytocin: oxytocin modulates neuroendocrine SCLC cell differentiation and NK-cell immune response (NK-cell already mapped) against this cold tumour; receptor expression on neuroendocrine cells intersects cAMP/PKA and NF-κB (already mapped) axes of SCLC."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "SCLC prolactin: prolactin via JAK2/STAT3 (already mapped) signalling on neuroendocrine SCLC cells promotes tumour-cell survival, amplifying the MYC (already mapped) and Rb1 (already mapped)-pathway oncogenic drive of small cell lung cancer."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "SCLC selenium: selenium-dependent glutathione peroxidase (GPX) quenches reactive-oxygen-species driving NF-κB (already mapped)-mediated genomic instability and MYC (already mapped) amplification in the highly proliferative small cell lung cancer tumour cells."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "SCLC iodine: thyroid hormones regulate macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour immunity; thyroid deficiency amplifies VEGF (already mapped) and mTOR (already mapped) and NF-κB (already mapped) cascade of SCLC."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "SCLC copper: copper, as lysyl oxidase cofactor in macrophages (already mapped), drives tumour angiogenesis; copper amplifies VEGF (already mapped); copper deficiency impairs dendritic-cell (already mapped) and T-cytotoxic-cell (already mapped) immunity in SCLC."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "SCLC zinc: zinc, as metalloproteinase cofactor in macrophages (already mapped), supports tumour invasion; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade and impairs T-cytotoxic-cell (already mapped) cytotoxicity in SCLC."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "SCLC phosphorus: phosphorus, as ATP donor in mTOR (already mapped) kinase signalling in macrophages (already mapped) and T-cytotoxic-cell (already mapped), fuels proliferation; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of SCLC."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "SCLC chloride: chloride channels in macrophages (already mapped) and T-cytotoxic-cell (already mapped) regulate tumour-immune tone; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) angiogenic cascade of SCLC."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "SCLC sulfur: hydrogen sulfide from macrophages (already mapped) and tumour vasculature promotes HIF-1α (already mapped)-driven angiogenesis; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of SCLC."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "SCLC hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and T-cytotoxic-cell (already mapped), modulates tumour oxidative stress; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of SCLC."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "SCLC nitrogen: nitric oxide from macrophages (already mapped) and T-cytotoxic-cell (already mapped) modulates tumour immune tone; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of SCLC."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "SCLC oxygen: HIF-1α (already mapped) senses tumour hypoxia in macrophages (already mapped) and tumour vasculature; oxygen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) angiogenic cascade of SCLC."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "SCLC GLP-1: GLP-1 receptor signalling in tumour cells and macrophages (already mapped) modulates metabolic and inflammatory tumour risk; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of SCLC."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "SCLC angiotensin-II: angiotensin-II signalling in tumour vasculature and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of SCLC."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "SCLC Wnt/β-catenin: Wnt/β-catenin signalling in tumour cells and macrophages (already mapped) sustains cell survival; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of SCLC."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "SCLC rankl: RANKL from macrophages (already mapped) and tumour cells (already mapped) promotes bone metastasis and immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "SCLC fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds SCLC tumour ECM; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "SCLC activin-a: activin-A from macrophages (already mapped) and fibroblasts (already mapped) regulates neuroendocrine tumour proliferation; activin-a loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "SCLC cgrp: CGRP from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC vascular tone; cgrp dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "SCLC substance-p: substance-P from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC neuroinflammatory signalling; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "SCLC insulin-receptor: insulin receptor on neuroendocrine cells (already mapped) and macrophages (already mapped) drives SCLC metabolic tone; insulin-receptor excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "SCLC aldosterone: aldosterone from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates ion balance in SCLC; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "SCLC androgen-receptor: androgen receptor on neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC steroid tone; androgen-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "SCLC adrenomedullin: adrenomedullin from neuroendocrine cells (already mapped) and macrophages (already mapped) promotes SCLC vasodilation; adrenomedullin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "SCLC norepinephrine: norepinephrine from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates adrenergic vascular tone; norepinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "SCLC bdnf: BDNF from neuroendocrine cells (already mapped) and macrophages (already mapped) supports tumour neural trophic tone; bdnf loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "SCLC osteopontin: osteopontin from neuroendocrine cells (already mapped) and macrophages (already mapped) promotes SCLC ECM remodelling; osteopontin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "SCLC fgfr: FGFR on neuroendocrine cells (already mapped) and macrophages (already mapped) drives tumour proliferation; fgfr dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "SCLC epinephrine: epinephrine from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates adrenergic tumour tone; epinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "SCLC renin: renin from neuroendocrine cells (already mapped) and macrophages (already mapped) links RAAS to tumour vascular remodelling; renin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "SCLC myostatin: myostatin from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC tumour muscle wasting; myostatin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "SCLC angiopoietin: angiopoietin from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC tumour vascular remodelling; angiopoietin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "SCLC ghrelin: ghrelin from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC metabolic tone; ghrelin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC."
---

# Small Cell Lung Cancer

## Overview

**Small cell lung cancer (SCLC)** is a high-grade neuroendocrine carcinoma of the lung characterized by rapid growth, early metastasis, and initial chemosensitivity followed by near-universal relapse and drug resistance. SCLC accounts for ~13-15% of all lung cancers (~35,000 new cases/year in the USA), with a dismal 5-year overall survival of <10% for extensive-stage disease. Pathologically, SCLC is a poorly differentiated neuroendocrine carcinoma (WHO: NEC) with characteristic small cells, scant cytoplasm, salt-and-pepper chromatin, high mitotic rate (Ki-67 typically >50-70%), and necrosis. The defining molecular events — **biallelic RB1 loss** (>90%) and **TP53 biallelic mutation** (>90%) — cooperate to eliminate the two fundamental barriers to uncontrolled proliferation; no actionable oncogene driver (EGFR, ALK, RAS) is present. The treatment paradigm has been transformed by addition of anti-PD-L1/PD-1 immunotherapy to platinum/etoposide (IMpower133 and CASPIAN trials) in first-line, and by approval of **tarlatamab** (DLL3×CD3 bispecific) for relapsed disease [^horn-2018-impower133] [^paz-ares-2019-caspian].

**Epidemiology and risk factors:**
- Incidence: ~35,000 cases/year USA; declining with smoking reduction; accounts for 13-15% of all lung cancers
- **Smoking causation:** >95% of SCLC attributable to cigarette smoking; among the strongest smoking-cancer associations; typically develops after 30+ pack-years; rare in never-smokers
- Presentation: Rapid onset; hilar/mediastinal mass; superior vena cava syndrome; paraneoplastic syndromes (SIADH from ectopic ADH in ~10%; ACTH from ectopic CRH/ACTH → Cushing's in ~5%; Lambert-Eaton myasthenic syndrome from VGCC autoantibodies; paraneoplastic encephalitis from Hu/Ri antibodies)
- Staging: Two-stage system (Veterans Affairs): Limited stage (LS-SCLC, ~30%): Tumor confined to one hemithorax + regional nodes, can be encompassed in one radiation field; Extensive stage (ES-SCLC, ~70%): Beyond limited stage; includes most patients with liver, adrenal, bone, and brain metastases; TNM staging also used per AJCC 8th

**Molecular landscape:**
- RB1 biallelic loss (deletion, frameshift, missense): >90% of SCLC; the central molecular driver
- TP53 biallelic mutation: >90%; near-universal alongside RB1
- MYCL1/MYCN amplification: ~20% of SCLC; associated with SCLC-A subtype; poor prognosis
- SOX2 amplification: ~30%; squamous-like feature
- CREBBP/EP300 mutations: ~20%; chromatin regulators
- PTEN loss: ~10%
- FGFR1 amplification: ~6%; gefitinib active in preclinical models
- PIK3CA: ~6%
- No EGFR, KRAS, ALK, ROS1 driver alterations in SCLC (these define non-SCLC adenocarcinoma)

## Structure

### Pathological features and molecular subtypes

**Histopathology:**
- Tumor cells: Small (2× lymphocyte size), round-to-oval, scant cytoplasm, finely granular nuclear chromatin (salt-and-pepper), indistinct nucleoli, nuclear molding, numerous mitoses (>11 per 2 mm²), geographic necrosis
- IHC: Synaptophysin+, chromogranin A+ (variable), INSM1+ (highly specific), CD56/NCAM+; TTF-1+ in ~80%; Ki-67 >50-70%; CK AE1/3+ (dot-like pattern); RB1 protein absent/dim (correlates with RB1 gene loss)
- DLL3 IHC: >80% of SCLC; especially SCLC-A; semi-quantitative scoring
- Distinguishing SCLC from LCNEC: SCLC has smaller cells, no prominent nucleolus, nuclear molding; LCNEC has large cells, vesicular chromatin, prominent nucleoli; both are NEC; CD56/synaptophysin/chromogranin distinguish from non-NEC; Ki-67 >40% in both
- Crush artifact: SCLC is fragile → bronchoscopic biopsy specimens often show crush artifact (basophilic smeared nuclei) → diagnosis still possible from minimal material with IHC

**SCLC molecular subtypes (Rudin 2019):**
- **SCLC-A (ASCL1-high, ~70%):** DLL3+ high; Notch-low; synaptophysin/CgA+; most common; first-line chemo-responsive; tarlatamab most active
- **SCLC-N (NEUROD1-high, ~18%):** Less neuroendocrine; DLL3 intermediate; brain metastasis-prone; MYC high; responds to checkpoint inhibitors (higher TMB subgroup)
- **SCLC-P (POU2F3-high, ~10%):** Tuft cell-like; distinct from NE subtypes; DLL3 low/absent; FGFR1 amplification enriched; response to tarlatamab lower
- **SCLC-Y (YAP1-high, ~2%):** Non-NE, mesenchymal-like; aggressive; platinum-resistant; DLL3 low

**Paraneoplastic syndromes:**
- **SIADH (~10-15%):** Ectopic vasopressin (ADH) from SCLC → hyponatremia; fluid restriction + treatment of SCLC
- **Ectopic ACTH (~5%):** Ectopic CRH/ACTH → pituitary-independent Cushing's → severe hypokalemia, proximal myopathy, hyperglycemia; metyrapone or ketoconazole for cortisol control; treat SCLC
- **Lambert-Eaton myasthenic syndrome (LEMS, ~3%):** Autoimmodies to P/Q-type voltage-gated calcium channels (VGCC) → impaired neuromuscular transmission → proximal limb weakness, hyporeflexia, autonomic dysfunction; VGCC antibodies (anti-VGCC-α1); 3,4-diaminopyridine + immunosuppression; treat SCLC
- **Paraneoplastic encephalitis/limbic encephalitis (~1-2%):** Anti-Hu (ANNA-1) antibodies → encephalitis, sensory neuropathy; anti-CV2/CRMP5; MRI limbic changes; IVIG/steroids + SCLC treatment

### Diagnosis and staging

**Workup:**
- Chest CT + contrast: Hilar/mediastinal mass (central tumor typical); effusion; SVC obstruction
- PET/CT: Staging; brain MRI (mandatory for all SCLC due to high rate of occult brain mets ~10% at diagnosis)
- Bronchoscopy + biopsy: Central lesions; bronchoscopic sampling with cytology
- Bone marrow biopsy: No longer routine (PET/CT adequate for staging)
- Serum: LDH (prognostic); sodium (SIADH); ACTH/cortisol (ectopic ACTH)
- Endobronchial ultrasound (EBUS): Mediastinal lymph node sampling if limited stage considered

**Limited Stage SCLC (LS-SCLC) — concurrent chemoradiation:**
- Cisplatin + etoposide × 4 cycles + concurrent thoracic radiation (45 Gy BID or 60-66 Gy daily); NCCN preferred approach; concurrent = superior to sequential
- Prophylactic cranial irradiation (PCI): For patients with CR/PR to first-line therapy → 25 Gy/10 fractions; reduces CNS relapse from ~50% to ~25%; controversy: MRI surveillance vs. PCI (Japanese JIROG trial showed MRI surveillance non-inferior with preserved cognitive function → shifting practice toward MRI surveillance)
- 5-year OS: ~20-30% for LS-SCLC; curative intent

## Function

### Tumor biology — chemosensitivity and resistance

**Initial chemosensitivity:**
SCLC is initially highly sensitive to platinum-based chemotherapy (ORR ~80% for ES-SCLC) due to: RB1 loss → constitutive proliferation → more cells in S/G2/M phase (chemo-sensitive phases); p53 loss → reduced G1 checkpoint → cells do not arrest before lethal DNA damage; high apoptotic priming (BCL-2 high → venetoclax active in preclinical models); rapid tumor doubling time (~30-60 days).

**Acquired resistance ("transformation" and relapse):**
SCLC almost universally relapses within 6-12 months of first-line therapy; resistant SCLC has acquired: SLFN11 (Schlafen 11) downregulation (SLFN11 is a DNA/RNA helicase that promotes replication fork collapse under DNA damage → SLFN11 loss → SCLC cells repair platinum damage more effectively → chemo-resistance); phenotypic subtype switching (SCLC-A → SCLC-P or SCLC-Y → DLL3 downregulation → tarlatamab resistance); MYC amplification (acquired) → CDK1-dependent G2/M checkpoint reliance.

## Pathology

### First-line and relapsed treatment

**Extensive Stage SCLC — First-line:**

**Carboplatin (AUC 5) + etoposide × 4-6 cycles** (or cisplatin + etoposide for cisplatin-eligible patients): Standard backbone.

**+ Atezolizumab (anti-PD-L1, IMpower133):** [^horn-2018-impower133]
- 403 patients ES-SCLC; carboplatin/etoposide ± atezolizumab; maintenance atezolizumab
- OS 12.3 vs 10.3 months (HR 0.70); PFS 5.2 vs 4.3 months; ORR 60.2% vs 64.4%
- FDA approved March 2019; first immunotherapy + chemo regimen for SCLC; PD-L1 expression did NOT predict benefit
- Atezolizumab maintenance (16 cycles or progression) added to OS benefit

**+ Durvalumab (anti-PD-L1, CASPIAN):** [^paz-ares-2019-caspian]
- 805 patients ES-SCLC; platinum/etoposide ± durvalumab ± tremelimumab (CTLA-4)
- OS 12.9 vs 10.5 months (HR 0.75) for durvalumab + chemo vs. chemo alone
- FDA approved March 2020; durvalumab ± tremelimumab arm did not improve further over durvalumab alone
- Both atezolizumab and durvalumab + carbo/etoposide are NCCN Category 1 preferred regimens

**Second-line (relapsed within 6 months = platinum-resistant):**
- **Lurbinectedin (Zepzelca):** FDA accelerated approval July 2020; 105 patients R/R SCLC; ORR 35.2%; mDOR 5.3 months; mechanism: RNA polymerase II inhibitor → transcription addiction in SCLC → DNA damage; platinum-resistant ORR ~22%, platinum-sensitive ~45%
- **Topotecan:** Standard 2nd-line (OS ~6 months); modest activity; hematologic toxicity; FDA approved 1998; oral and IV formulations
- **Tarlatamab (FDA accelerated approval May 2024):** DLL3×CD3 BiTE; DeLLphi-301 Phase 2 (R/R ≥2 lines): 10 mg cohort ORR 40%, 100 mg ORR 32%; mDOR 9.7 months (10 mg); CNS ORR 52% (10 mg) — exceptional CNS activity; PFS 4.9 months; OS 14.3 months; approved for ≥2 prior lines; CRS management critical
- **Reinduction with platinum/etoposide:** For platinum-sensitive relapse (>6 months post-platinum); ORR ~50-60% for re-treatment; not standard after immunotherapy era
- **Nivolumab + ipilimumab:** CheckMate 032 basket: ORR 21.7% for combination in R/R SCLC; FDA approved 2020 for 3rd+ line (withdrawn from market 2023 due to CheckMate 451 maintenance failure)

**Third-line and beyond:**
- Tarlatamab (if not yet used): ORR ~40% in biomarker-unselected SCLC
- Temozolomide: Active in SCLC with brain metastases (CNS-penetrant)
- Irinotecan: ORR ~15-20% in R/R SCLC (Japan: cisplatin + irinotecan equivalent to cisplatin + etoposide in first-line for Japanese population)
- Clinical trial preferred

**Brain metastases:**
SCLC has highest rate of brain metastases among solid tumors (~50% at 2 years); SRS (stereotactic radiosurgery) for oligometastatic; WBRT (whole-brain RT) for multiple brain mets; tarlatamab shows 52% CNS ORR → may reduce need for WBRT in R/R SCLC; temozolomide for CNS-only progression.

## Connections

- `connects-to` → **[DLL3](../../03-molecular/dll3/README.md)** — DLL3 overexpressed in >80% of SCLC (especially ASCL1-high subtype); drives Notch cis-inhibition → neuroendocrine identity; tarlatamab (DLL3×CD3 bispecific, FDA 2024): ORR 40%, CNS response 52%; first immunotherapy specifically approved for relapsed SCLC.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 biallelic loss in >90% of SCLC is the defining molecular event; RB1 loss releases E2F → ASCL1 → neuroendocrine program (DLL3, synaptophysin, chromogranin); RB1 loss also confers vulnerability to CDK4/6 inhibitor combinations in experimental models.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Atezolizumab (PD-L1) + carboplatin/etoposide (IMpower133: OS 12.3 vs 10.3 months) and durvalumab + platinum/etoposide (CASPIAN: OS 12.9 vs 10.5 months) are approved first-line regimens; PD-L1 expression does not predict benefit in SCLC; SCLC is immunologically cold.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 biallelic mutation co-occurs with RB1 loss in >90% of SCLC; p53 loss → unchecked DNA damage response → rapid proliferation; platinum/etoposide sensitivity partly attributable to p53-null apoptotic priming; SCLC lacks targetable TP53 restoration options.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Small cell lung cancer (~13-15% of lung cancer) is the most aggressive subtype, smoking-driven, arising centrally as a bulky hilar mass that often causes superior vena cava syndrome; it disseminates early, so ~70% present extensive-stage with brain, liver, or bone metastases.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — SCLC and NSCLC are the two divisions of lung cancer with opposite therapeutic logic: NSCLC is rich in targetable drivers, whereas SCLC has near-universal RB1 and TP53 loss with no actionable oncogene, relying on platinum-etoposide, immunotherapy, and DLL3-directed tarlatamab.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — SCLC is the poorly differentiated, high-grade end of the pulmonary neuroendocrine spectrum (Ki-67 >50%, synaptophysin/INSM1+), unlike indolent carcinoid NETs; whereas SSTR2-high NETs use somatostatin analogs and PRRT, SCLC is treated as a chemo-driven carcinoma.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Small cell lung cancer and tuberculosis both present as a cavitary lung lesion with weight loss, cough, and hemoptysis in older smokers, sharing a radiographic differential — neuroendocrine tumor versus granulomatous infection — resolved by biopsy and microbiology.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — SCLC's neuroendocrine identity drives paraneoplastic neurology: tumor cells express neuronal antigens, so anti-neuronal antibodies attack the nervous system — anti-Hu encephalomyelitis and Lambert-Eaton myasthenic syndrome (anti-VGCC) — often before the cancer is found.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain is a defining SCLC battleground: ~50% develop brain metastases from its early spread, so prophylactic cranial irradiation is offered to responders; SCLC also causes paraneoplastic limbic encephalitis, and DLL3-targeted tarlatamab achieves CNS responses.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is integral to small cell lung cancer: concurrent thoracic photon radiation with platinum chemotherapy is standard for limited-stage disease (often twice-daily), exploiting SCLC's marked radiosensitivity—with cranial irradiation added for brain spread.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Small cell lung cancer and retinoblastoma are linked by RB1 loss: the tumor-suppressor that, germline-mutated, causes childhood retinoblastoma is inactivated (with TP53) in nearly all SCLC—one gene whose loss drives cancers in utterly different tissues and ages.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages populate the immunosuppressive SCLC microenvironment: despite its high mutational burden from smoking, SCLC responds only modestly to immunotherapy, partly because M2 macrophages and an exhausted, 'cold' immune milieu blunt T-cell attack.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Small-cell lung cancer is the most tobacco-driven lung cancer: carbon-based smoke carcinogens (PAHs, nitrosamines) cause near-universal TP53 and RB1 loss, so SCLC almost never arises in never-smokers—the tightest smoking-cancer link among lung tumors.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — SCLC and head and neck cancer arise from the same tobacco field cancerization: heavy smoking injures the entire aerodigestive epithelium, so a patient with one is at high risk of the other—both smoking-driven cancers whose prevention rests on cessation.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — SCLC and esophageal squamous cancer share smoking and alcohol as drivers: both stem from carcinogen exposure of the aerodigestive tract, and esophageal small-cell carcinoma is a rare aggressive variant—reminders that tobacco's reach spans the chest's epithelia.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC amplification drives the most aggressive SCLC: alongside near-universal TP53 and RB1 loss, MYC-family amplification defines a fast-proliferating subtype, so SCLC's relentless growth and early metastasis trace to these few but powerful genetic hits.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — SCLC metastasizes early to the adrenal glands: it spreads widely at diagnosis—to liver, brain, bone and characteristically the adrenals—so an adrenal mass with a lung primary signals extensive-stage disease, and SCLC can also ectopically secrete ACTH.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — SCLC is the classic cause of paraneoplastic neurological syndromes: it provokes antibodies (anti-Hu, anti-VGCC) that attack the nervous system, causing Lambert-Eaton myasthenic syndrome and encephalitis—sometimes appearing before the tumor is found.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Beyond its tumor biology, SCLC drives paraneoplastic autoimmunity: it expresses neuronal antigens the immune system attacks, while its high mutational burden makes it responsive to checkpoint immunotherapy—so immunity both harms (autoimmunity) and helps (treatment).
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — SCLC's neuroendocrine cells secrete ectopic hormones, causing endocrine paraneoplastic syndromes: ADH drives SIADH with hyponatremia and ACTH produces Cushing's—so metabolic disturbances often herald or complicate the cancer before imaging finds it.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a common SCLC metastatic site: this aggressive cancer spreads early and widely, and liver involvement marks extensive-stage disease, worsens prognosis, and can impair drug metabolism—so staging scans routinely scrutinize the liver.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — SCLC is now attacked with T-cell engagers: tarlatamab, a bispecific antibody linking the tumor's DLL3 to CD3 on cytotoxic T cells, redirects them to kill small-cell lung cancer—a new option after chemotherapy in this aggressive disease.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Small-cell lung cancer classically causes SIADH: the tumor ectopically secretes vasopressin (ADH), driving water retention and hyponatremia, so unexplained low sodium in a smoker can be the presenting clue to SCLC.
- `connects-to` → **[ACTH](../../03-molecular/acth/README.md)** — SCLC is a leading cause of ectopic ACTH syndrome: the neuroendocrine tumor secretes ACTH, producing a rapid-onset paraneoplastic Cushing's with hypokalemia and hyperglycemia rather than the classic body changes—signaling aggressive disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Small cell lung cancer can paralyze through calcium channels: in Lambert-Eaton syndrome, antibodies against the tumor's calcium channels cross-react at nerve terminals, cutting calcium-triggered acetylcholine release and causing the weakness that often precedes diagnosis.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — Small cell lung cancer is shaped by Notch and its ligand DLL3: Notch is largely silenced in these neuroendocrine tumors, and the resulting high DLL3 on the cell surface is the target of new drugs like tarlatamab.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Small cell lung cancer hides behind regulatory T cells: a suppressive microenvironment limits the immune attack, so although checkpoint immunotherapy now adds to chemo, Tregs are part of why responses are often brief in this aggressive cancer.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Small cell lung cancer classically drops the blood sodium: ectopic vasopressin from the tumor causes SIADH, so unexplained hyponatremia in a smoker is a clue that can lead to the diagnosis and tracks with tumor burden.
- `connects-to` → **[Neuromuscular Junction](../../05-tissue/neuromuscular-junction/README.md)** — Small cell lung cancer attacks the neuromuscular junction from afar: antibodies against the tumor cross-react with calcium channels there, causing Lambert-Eaton myasthenic syndrome—a paraneoplastic weakness that can precede the cancer's discovery.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells shape the immune fight against small cell lung cancer: as antigen-presenters they prime the T-cell response checkpoint drugs now add to chemo, and their dysfunction helps explain the brief responses in this aggressive tumor.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Small cell lung cancer can drop potassium: by secreting ectopic ACTH it drives a paraneoplastic Cushing's whose cortisol excess makes the kidneys waste potassium into hypokalemia.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Small cell lung cancer can blind through the eye: cancer-associated retinopathy, a paraneoplastic autoimmune attack on the retina, causes progressive vision loss that can precede the tumor's discovery.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Small cell lung cancer floods the bone marrow: this aggressive tumor frequently metastasizes to the marrow, crowding out blood production and marking the widespread disease typical at diagnosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals SCLC's neuroendocrine soul: scattered dense-core neurosecretory granules — tiny membrane-bound packets of hormone — mark these small dark cells as neuroendocrine, the trait behind their paraneoplastic syndromes.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — SCLC can flood the body with cortisol: its ectopic ACTH drives the adrenals to overproduce cortisol, causing a rapidly evolving Cushing syndrome of weakness, swelling, and low potassium rather than the classic slow body changes.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — SCLC turns the immune system against the nerves: anti-Hu and related antibodies meant for the tumor also strike peripheral neurons, producing a paraneoplastic sensory neuronopathy that can appear before the cancer is found.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — SCLC's intense chemotherapy empties the marrow: the platinum-etoposide that this fast-growing cancer demands drops neutrophils into a neutropenia, so febrile neutropenia and growth-factor support are constant concerns of treatment.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — The platinum backbone leaks magnesium away: cisplatin injures the kidney's tubules, which then waste magnesium, so levels are checked and repleted through the rounds of SCLC chemotherapy.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Immunotherapy now joins the attack on SCLC: adding a PD-L1 checkpoint inhibitor to first-line chemotherapy releases the brakes on T cells, letting helper and cytotoxic T cells mount a response that modestly extends survival in extensive-stage disease.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies pervade SCLC: synaptophysin, chromogranin, and TTF-1 stains with a high Ki-67 confirm the neuroendocrine tumor, anti-Hu and anti-VGCC autoantibodies drive its paraneoplastic syndromes, and an anti-PD-L1 antibody is now added to chemotherapy.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The aggressive tumor and its chemotherapy thin the red cells: marrow infiltration plus the cisplatin-etoposide regimen depress erythrocyte production into an anemia that, with the disease's rapid course, often needs transfusion support.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — A central SCLC can throttle the great vein: a bulky mediastinal tumor compresses the superior vena cava, swelling the face and neck with engorged skin veins, while paraneoplastic dermatomyositis can rash the skin as a clue to the hidden cancer.
- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — MYC-family amplification splits SCLC into subtypes: alongside MYC, amplification of MYCN or MYCL defines molecular groups with distinct biology and drug sensitivities, layered on the near-universal loss of both RB1 and p53.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Few cancers clot like SCLC: this aggressive tumor pours out procoagulants and, with chemotherapy and central venous catheters, drives one of the highest rates of deep-vein thrombosis and pulmonary embolism among solid cancers.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — The platinum-etoposide chemotherapy empties the marrow: it suppresses platelet production into thrombocytopenia, a dose-limiting toxicity that raises bleeding risk through the rapid, intensive cycles SCLC demands.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Immunotherapy reached even this hard target: blocking CTLA-4 alongside PD-L1 adds a modest survival gain in extensive-stage SCLC, releasing T cells against a tumor whose heavy smoking-driven mutation load makes it visible to the immune system.
- `connects-to` → **[COPD](../copd/README.md)** — It shares its cause with the airways' disease: the same heavy tobacco smoking that drives SCLC produces COPD, so the two frequently coexist, and the reduced lung reserve of COPD complicates treating the cancer.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — It grows a fast, leaky blood supply: SCLC is intensely angiogenic, pushing endothelial cells to build the vasculature that fuels its rapid doubling and early spread — the rationale behind testing antiangiogenic drugs against it.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 sustains the neuroendocrine tumor: JAK-STAT3 signaling drives SCLC proliferation and immune evasion, part of the signaling that keeps this fast-growing cancer alive between its near-universal RB1 and p53 losses.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB feeds chemoresistance: after an initial dramatic chemo response, SCLC relapses with NF-κB-supported survival signaling, part of why this tumor so reliably returns resistant within months.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A central tumor and intense chemo invite sepsis: post-obstructive pneumonia behind a bronchial SCLC, plus the deep neutropenia of platinum-etoposide cycles, make pneumonia and sepsis frequent complications.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Tumor cytokines waste the body: SCLC secretes IL-6 and related cytokines that drive the profound cachexia, fever and inflammatory markers typical of this aggressive neuroendocrine cancer at presentation.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Inflammation and marrow involvement drop the hemoglobin: the IL-6 milieu of SCLC raises hepcidin while frequent bone-marrow metastases crowd the marrow, producing an anemia of chronic disease layered on chemotherapy myelosuppression.
- `connects-to` → **[Stroke](../stroke/README.md)** — A hypercoagulable cancer can strike the brain: SCLC's strong Trousseau-type prothrombotic state, with non-bacterial thrombotic endocarditis and arterial emboli, can cause ischemic stroke alongside its common brain metastases.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its platinum chemotherapy scars the kidneys: cisplatin, central to SCLC regimens, is directly nephrotoxic, and the tubular and electrolyte injury it causes can leave lasting chronic kidney impairment.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Cavitating tumor and chemo neutropenia open the lung to mold: post-obstructive collapse plus the deep neutropenia of platinum-etoposide therapy let inhaled Aspergillus invade as pulmonary aspergillosis in the damaged lung.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An aggressive, smoking-related cancer weighs on mood: SCLC's rapid course, poor prognosis and breathlessness, with the stigma of smoking and frequent brain metastases, contribute to high rates of depression.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — A tumour plugging the airway breeds pneumonia: a bronchus obstructed by central SCLC traps secretions distal to it, and post-obstructive pneumonia — classically pneumococcal — is a common complication.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Both the tumour and its chemo attack the nerves: SCLC causes paraneoplastic sensory neuropathy via anti-Hu antibodies, and the platinum chemotherapy adds its own painful peripheral neuropathy.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A fast, breathless, relapsing cancer breeds dread: the rapid growth, near-inevitable relapse and dyspnoea of SCLC fuel intense anxiety alongside the depression it so often brings.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It is a central lung cancer that strangles the airway: SCLC arises centrally and grows fast, causing bronchial obstruction, post-obstructive pneumonia and superior vena cava syndrome.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It floods the liver with deposits: SCLC metastasises early and avidly to the liver, a common site at presentation that drives its dismal prognosis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It spreads to bone and weakens muscle: SCLC metastasises to the skeleton causing pain and fractures, and its paraneoplastic Lambert-Eaton myasthenic syndrome causes proximal muscle weakness.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It floods the nodes early: small cell lung cancer spreads rapidly and extensively to mediastinal and distant lymph nodes, central to its limited-versus-extensive staging.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Central tumours strangle the great veins: a central SCLC commonly causes superior vena cava obstruction with facial swelling and distended veins, and can invade the pericardium causing effusion.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its drugs and hormones strain the kidney: the platinum chemotherapy for SCLC is nephrotoxic, and paraneoplastic SIADH causes profound hyponatraemia needing careful correction.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Immunotherapy joined its chemo: checkpoint inhibitors such as atezolizumab and durvalumab added to platinum-etoposide chemotherapy modestly extend survival in small cell lung cancer.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It signals through paraneoplastic skin signs: small cell lung cancer can cause dermatomyositis and acanthosis nigricans, cutaneous clues to the underlying tumour.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Treatment threatens fertility: the intensive platinum chemotherapy for small cell lung cancer can impair fertility, and the cancer rarely metastasises to the ovaries.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Platinum-etoposide is the backbone: SCLC is exquisitely chemosensitive at first, with platinum-etoposide producing rapid responses, but it almost always relapses within months as chemoresistant disease, when topotecan or lurbinectedin follow.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — It triggers Lambert-Eaton: about half of Lambert-Eaton myasthenic syndrome is paraneoplastic to SCLC, with anti-VGCC antibodies causing proximal weakness that improves with use — the mirror image of, and key differential for, myasthenia gravis.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — First-line immunotherapy adds months: adding atezolizumab or durvalumab to chemotherapy and continuing it as maintenance is now standard in extensive-stage SCLC, giving a real but modest survival gain that proves durable in only a minority.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The price of protecting the brain: SCLC metastasises early to the brain, so prophylactic cranial irradiation is offered—but it damages the hippocampus and impairs memory, driving hippocampal-avoidance techniques.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It floods the liver fast: small-cell lung cancer metastasises early and widely, with the liver a frequent site where deposits fill the hepatic lobules and herald the extensive-stage disease that dominates at diagnosis.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Two MYCN-driven neuroendocrine cancers: small-cell lung cancer and neuroblastoma are both small-round-blue-cell tumours with neuroendocrine differentiation and frequent MYC/MYCN amplification, explaining their aggressive, chemo-sensitive-but-relapsing course.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Central origin, early spread: SCLC arises centrally near the bronchi and disseminates early, seeding the alveolar bed and distant organs—the most aggressive lung cancer, usually widespread at diagnosis.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Two heavily-smoking cancers: SCLC and bladder cancer share tobacco causation, and small-cell neuroendocrine carcinoma can also arise in the bladder, mirroring the lung tumour's aggressive histology.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Why immunotherapy helps: SCLC's heavy smoking-driven mutation load and tertiary lymphoid structures make it visible to T cells, so adding PD-L1 (and CTLA-4) blockade improves survival in extensive-stage disease.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Seizures from two directions: SCLC frequently metastasises to the brain and also causes paraneoplastic limbic encephalitis (anti-Hu), both producing seizures and secondary epilepsy in advanced disease.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Paraneoplastic neuronopathy: anti-Hu antibodies in SCLC destroy dorsal-root-ganglion neurons and their axonal transport, causing a severe subacute sensory neuronopathy that can precede the cancer's discovery.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Electrolytes and the heart: SCLC's ectopic hormones disturb the heart's conduction—SIADH-driven hyponatraemia and ectopic-ACTH hypokalaemia destabilise rhythm—while paraneoplastic autonomic neuropathy adds to the risk.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Molecular subtype: YAP1 defines a distinct SCLC subgroup (SCLC-Y) with a more inflamed, mesenchymal phenotype and differing chemotherapy sensitivity.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic dependency: EZH2 is a key epigenetic vulnerability in SCLC, enforcing the neuroendocrine programme and chemoresistance—an actionable target.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Apoptosis evasion: SCLC strongly expresses anti-apoptotic BCL-2, a long-standing therapeutic target exploited by BH3-mimetic drugs.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT survival: PI3K/AKT activation sustains the survival of small-cell lung cancer cells, contributing to its rapid relapse after initial chemosensitivity.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Unrestrained cell cycle: with RB1 loss near-universal in SCLC, the cell cycle runs unchecked, and the MYC-driven proliferation makes it one of the fastest-growing cancers.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the rapidly growing, hypoxic SCLC drives angiogenesis and the aggressive, metastatic phenotype that defines the disease.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — SCLC reactivates telomerase to maintain telomeres through its breakneck proliferation, granting the unlimited replicative capacity that complements the universal RB1 and TP53 loss—an immortality switch fundamental to its aggressive course.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — SCLC commonly expresses c-KIT (CD117), a receptor tyrosine kinase reflecting its neuroendocrine lineage; although imatinib trials failed, KIT marks the stem-like, treatment-resistant biology that makes the cancer so prone to relapse.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The high replication stress and DNA damage of SCLC generate cytosolic DNA that activates cGAS-STING, the innate-immune rationale for combining PARP inhibitors or chemotherapy with the checkpoint blockade now standard in extensive-stage disease.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — The genomic instability of RB1/TP53-null SCLC leaves it reliant on homologous-recombination and replication-stress repair, the basis for the high PARP expression that makes SCLC a leading candidate for PARP inhibition.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — As a high-grade neuroendocrine tumor SCLC can express somatostatin receptor SSTR2, the target for DOTATATE imaging and a rationale for peptide-receptor radionuclide approaches in the neuroendocrine fraction of these tumors.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — SCLC is the classic trigger of Lambert-Eaton myasthenic syndrome, where antibodies against presynaptic P/Q-type calcium channels reduce acetylcholine release at the neuromuscular junction, causing the paraneoplastic proximal weakness.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Near-universal RB1 loss in SCLC (RB1 already mapped) releases E2F1-driven transcription, the engine of unchecked cell-cycle entry behind the explosive growth of this neuroendocrine carcinoma.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — SCLC is strikingly chemosensitive at first, undergoing caspase-3-mediated apoptosis to etoposide-platinum, but rapidly evolves apoptotic resistance that drives its near-universal relapse.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-mTOR signaling (AKT already mapped) is recurrently activated in SCLC and supports growth and survival, a targetable dependency beyond the defining RB1/TP53 loss.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR is the growth-controlling output of the PI3K-AKT axis (PIK3CA and AKT mapped) recurrently activated in SCLC, integrating the survival signaling layered on its RB1/TP53 loss.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — SCLC is a highly vascular, rapidly growing tumor driven by VEGF-mediated angiogenesis, the basis for anti-angiogenic agents combined with chemotherapy.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — The DLL3-CD3 bispecific tarlatamab (DLL3 mapped) and checkpoint inhibitors redirect cytotoxic T cells to kill SCLC through perforin and granzyme.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 already mapped) supports the survival and immunosuppressive microenvironment of small cell lung cancer.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling, induced by cigarette-smoke oxidants, contributes to the rapid proliferation and chemoresistance of small cell lung cancer.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Cigarette-smoke-driven TLR-MyD88-NF-κB signaling (NF-κB already mapped) provides a chronic inflammatory drive in the lung carcinogenesis underlying small cell lung cancer.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 contributes to the invasion, metastasis and immune evasion of small cell lung cancer.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling shapes the immunosuppressive microenvironment of small cell lung cancer.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling provides a proliferative input to small cell lung cancer downstream of receptor tyrosine kinases including KIT (KIT mapped).
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of small cell lung cancer, relevant to its checkpoint immunotherapy.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the neuroendocrine differentiation and immunosuppressive microenvironment of small cell lung cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by PI3K-AKT signaling, modulate the survival and chemoresistance of small cell lung cancer.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the MYC stability and survival signaling of small cell lung cancer.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the smoking-associated inflammatory and immunosuppressive microenvironment of small cell lung cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling contributes to the invasive and metastatic behavior of small cell lung cancer.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 regulation (p53 already mapped) participates in the apoptotic control of the near-universally TP53-mutant small cell lung cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of small cell lung cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and chemoresistance of small cell lung cancer cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of small cell lung cancer.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of small cell lung cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of small cell lung cancer.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of small cell lung cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of small cell lung cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of small cell lung cancer.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy target: small cell lung cancer is now treated with checkpoint inhibitors added to chemotherapy, and MHC class II antigen presentation shapes the T-cell response, with its frequent downregulation contributing to the tumour's immune evasion.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Autocrine growth loop: small cell lung cancer cells express IGF-1 receptor and drive an autocrine IGF-1/IGF-1R signalling loop that sustains proliferation and survival, a growth-factor dependency explored as a therapeutic vulnerability.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Ectopic neuroendocrine secretion: as a neuroendocrine tumour small cell lung cancer can ectopically secrete calcitonin alongside ACTH and vasopressin (both already mapped), a paraneoplastic hormone output reflecting its chromaffin-like differentiation.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Immunotherapy: IL-2-driven T-cell expansion complements the checkpoint inhibitors (PD-1/CTLA-4 already mapped) now added to chemotherapy for small cell lung cancer, one of the few advances in a disease with otherwise poor durable control.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis: small cell lung cancer is highly chemosensitive with rapid, bulky responses, and the resulting tumour-lysis syndrome releases purines that xanthine oxidase converts to uric acid, managed with allopurinol or rasburicase.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia: the intensive chemotherapy and marrow involvement of small cell lung cancer suppress erythropoiesis, lowering haemoglobin and causing the anaemia that adds to the fatigue of this aggressive disease.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Tumour-lysis acidosis: the rapid, bulky response of chemosensitive small cell lung cancer releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate already mapped), part of its acute metabolic risk.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), part of the immune evasion that limits the durability of checkpoint benefit in small cell lung cancer.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Cancer pain and dyspnoea: opioids acting on the mu-opioid receptor relieve the pain of bone metastases and the refractory breathlessness of advanced small cell lung cancer, a mainstay of its palliative care.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 carcinogenesis: tobacco induces cyclooxygenase-2 and prostaglandin E2 in the airway, promoting the proliferation and immunosuppression of the carcinogenesis of small cell lung cancer, whose universal TP53 and RB1 loss (already mapped) it compounds.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive microenvironment of small cell lung cancer.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia of malignancy: the chronic disease and the platinum-etoposide chemotherapy of small cell lung cancer cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of small cell lung cancer.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Cancer cachexia: the profound weight loss and cancer cachexia (IL-6 already mapped) of small cell lung cancer are reflected in the fall in the adipokine leptin as the adipose tissue is depleted.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine crosstalk: adiponectin, with leptin (already mapped), links the metabolic and adipose state to the systemic effects and cachexia of small cell lung cancer.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Cachexia adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the cachexia (IL-6 already mapped) of small cell lung cancer.
- `connects-to` → **[Cortical bone](../../05-tissue/cortical-bone/README.md)** — Bone metastases: the cortical bone is a common site of small cell lung cancer metastasis, causing the bone pain and pathological fractures of the extensive-stage disease.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and produces the anaemia of chronic disease (haemoglobin already mapped) of the small cell lung cancer cachexia.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the checkpoint (PD-1 already mapped) immunotherapy of small cell lung cancer.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune response to small cell lung cancer, engaged by the tarlatamab (DLL3 already mapped) T-cell engager.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the small-cell-lung-cancer immune microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of small cell lung cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of small cell lung cancer.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immunologically cold small-cell-lung-cancer microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of small cell lung cancer.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate cytotoxicity: the NK cells (perforin already mapped) provide the innate anti-tumour surveillance within the immunologically cold microenvironment of small cell lung cancer.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling recruits and polarises the myeloid-derived suppressor cells that reinforce the immunosuppression of the small-cell-lung-cancer microenvironment.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Central complement: the complement C3, upstream of the C5aR1 (already mapped), is the pivot of the complement activation within the immunosuppressive small-cell-lung-cancer microenvironment.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 (with C3 and C5aR1 already mapped) generates the C5a that recruits the myeloid-derived suppressor cells of the small-cell-lung-cancer microenvironment.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the sparse tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, marks the rare immune-responsive subset of the immunologically cold small cell lung cancer.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Bronchial epithelial alarmin: TSLP released from the bronchial epithelium activates mast cells and dendritic cells, promoting the immunosuppressive microenvironment of small cell lung cancer and the type-2 cytokine skewing that limits anti-tumour immunity.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Chemotherapy anaemia: erythropoietin corrects the severe anaemia from etoposide/platinum chemotherapy in small cell lung cancer, with EPOR expression on neuroendocrine SCLC cells raising the question of direct trophic signalling.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Neuroendocrine histamine: small cell lung cancer cells, as neuroendocrine tumours, can co-secrete histamine alongside the ectopic ACTH, ADH and other hormones causing the paraneoplastic syndromes characteristic of the disease.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin paraneoplastic crosstalk: bradykinin, generated by the kallikrein-kinin system in the SCLC tumour microenvironment, amplifies vascular permeability and neurogenic pain via B2 receptors on neuroendocrine cells, contributing to paraneoplastic neuropathy.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement-contact regulation: C1-esterase inhibitor restrains the classical complement C1 (C3/C5/C5aR1 already mapped) and the contact system activated in the SCLC microenvironment, modulating complement-dependent tumour immune surveillance.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Neuroendocrine ECM scaffold: periostin secreted by fibroblastic stroma of small cell lung cancer promotes SCLC-cell integrin-αv signalling and survival, reinforcing the desmoplastic tumour-microenvironment architecture of the disease.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — SCLC melatonin: melatonin, co-secreted by neuroendocrine SCLC cells, suppresses tumour proliferation via MT1/MT2 receptor-mediated inhibition of cAMP/PKA signalling; it also amplifies NK-cell (already mapped) cytotoxicity against the immunologically cold tumour microenvironment.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — SCLC testosterone: androgen receptor in a subset of SCLC drives tumour proliferation through MYC (already mapped) upregulation and Rb1 (already mapped) pathway crosstalk; androgen-axis suppression is a candidate therapeutic strategy for AR-positive small cell lung cancer.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — SCLC serotonin: serotonin is co-produced by neuroendocrine SCLC cells alongside ectopic ACTH (already mapped), and autocrine 5-HT1/2 receptor signalling amplifies tumour-cell proliferation and survival, contributing to carcinoid-like paraneoplastic manifestations.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — SCLC oxytocin: oxytocin modulates neuroendocrine SCLC cell differentiation and NK-cell immune response (NK-cell already mapped) against this cold tumour; receptor expression on neuroendocrine cells intersects cAMP/PKA and NF-κB (already mapped) axes of SCLC.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — SCLC prolactin: prolactin via JAK2/STAT3 (already mapped) signalling on neuroendocrine SCLC cells promotes tumour-cell survival, amplifying the MYC (already mapped) and Rb1 (already mapped)-pathway oncogenic drive of small cell lung cancer.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — SCLC selenium: selenium-dependent glutathione peroxidase (GPX) quenches reactive-oxygen-species driving NF-κB (already mapped)-mediated genomic instability and MYC (already mapped) amplification in the highly proliferative small cell lung cancer tumour cells.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — SCLC iodine: thyroid hormones regulate macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour immunity; thyroid deficiency amplifies VEGF (already mapped) and mTOR (already mapped) and NF-κB (already mapped) cascade of SCLC.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — SCLC copper: copper, as lysyl oxidase cofactor in macrophages (already mapped), drives tumour angiogenesis; copper amplifies VEGF (already mapped); copper deficiency impairs dendritic-cell (already mapped) and T-cytotoxic-cell (already mapped) immunity in SCLC.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — SCLC zinc: zinc, as metalloproteinase cofactor in macrophages (already mapped), supports tumour invasion; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade and impairs T-cytotoxic-cell (already mapped) cytotoxicity in SCLC.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — SCLC phosphorus: phosphorus, as ATP donor in mTOR (already mapped) kinase signalling in macrophages (already mapped) and T-cytotoxic-cell (already mapped), fuels proliferation; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of SCLC.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — SCLC chloride: chloride channels in macrophages (already mapped) and T-cytotoxic-cell (already mapped) regulate tumour-immune tone; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) angiogenic cascade of SCLC.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — SCLC sulfur: hydrogen sulfide from macrophages (already mapped) and tumour vasculature promotes HIF-1α (already mapped)-driven angiogenesis; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of SCLC.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — SCLC hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and T-cytotoxic-cell (already mapped), modulates tumour oxidative stress; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of SCLC.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — SCLC nitrogen: nitric oxide from macrophages (already mapped) and T-cytotoxic-cell (already mapped) modulates tumour immune tone; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of SCLC.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — SCLC oxygen: HIF-1α (already mapped) senses tumour hypoxia in macrophages (already mapped) and tumour vasculature; oxygen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) angiogenic cascade of SCLC.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — SCLC GLP-1: GLP-1 receptor signalling in tumour cells and macrophages (already mapped) modulates metabolic and inflammatory tumour risk; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of SCLC.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — SCLC angiotensin-II: angiotensin-II signalling in tumour vasculature and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of SCLC.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — SCLC Wnt/β-catenin: Wnt/β-catenin signalling in tumour cells and macrophages (already mapped) sustains cell survival; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of SCLC.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — SCLC rankl: RANKL from macrophages (already mapped) and tumour cells (already mapped) promotes bone metastasis and immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — SCLC fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds SCLC tumour ECM; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — SCLC activin-a: activin-A from macrophages (already mapped) and fibroblasts (already mapped) regulates neuroendocrine tumour proliferation; activin-a loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — SCLC cgrp: CGRP from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC vascular tone; cgrp dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — SCLC substance-p: substance-P from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC neuroinflammatory signalling; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — SCLC insulin-receptor: insulin receptor on neuroendocrine cells (already mapped) and macrophages (already mapped) drives SCLC metabolic tone; insulin-receptor excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — SCLC aldosterone: aldosterone from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates ion balance in SCLC; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — SCLC androgen-receptor: androgen receptor on neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC steroid tone; androgen-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — SCLC adrenomedullin: adrenomedullin from neuroendocrine cells (already mapped) and macrophages (already mapped) promotes SCLC vasodilation; adrenomedullin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — SCLC norepinephrine: norepinephrine from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates adrenergic vascular tone; norepinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — SCLC bdnf: BDNF from neuroendocrine cells (already mapped) and macrophages (already mapped) supports tumour neural trophic tone; bdnf loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — SCLC osteopontin: osteopontin from neuroendocrine cells (already mapped) and macrophages (already mapped) promotes SCLC ECM remodelling; osteopontin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — SCLC fgfr: FGFR on neuroendocrine cells (already mapped) and macrophages (already mapped) drives tumour proliferation; fgfr dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — SCLC epinephrine: epinephrine from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates adrenergic tumour tone; epinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — SCLC renin: renin from neuroendocrine cells (already mapped) and macrophages (already mapped) links RAAS to tumour vascular remodelling; renin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Myostatin](../../03-molecular/myostatin/README.md)** — SCLC myostatin: myostatin from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC tumour muscle wasting; myostatin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — SCLC angiopoietin: angiopoietin from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC tumour vascular remodelling; angiopoietin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — SCLC ghrelin: ghrelin from neuroendocrine cells (already mapped) and macrophages (already mapped) modulates SCLC metabolic tone; ghrelin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of SCLC.

[^horn-2018-impower133]: Horn L, Mansfield AS, Szczęsna A, et al. First-line atezolizumab plus chemotherapy in extensive-stage small-cell lung cancer. *N Engl J Med.* 2018;379(23):2220-2229. [doi:10.1056/NEJMoa1809064](https://doi.org/10.1056/NEJMoa1809064) · [PubMed 30280641](https://pubmed.ncbi.nlm.nih.gov/30280641/)
[^paz-ares-2019-caspian]: Paz-Ares L, Dvorkin M, Chen Y, et al. Durvalumab plus platinum-etoposide versus platinum-etoposide in first-line treatment of extensive-stage small-cell lung cancer (CASPIAN). *Lancet.* 2019;394(10212):1929-1939. [doi:10.1016/S0140-6736(19)32222-6](https://doi.org/10.1016/S0140-6736(19)32222-6) · [PubMed 31590988](https://pubmed.ncbi.nlm.nih.gov/31590988/)
