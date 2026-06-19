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

[^horn-2018-impower133]: Horn L, Mansfield AS, Szczęsna A, et al. First-line atezolizumab plus chemotherapy in extensive-stage small-cell lung cancer. *N Engl J Med.* 2018;379(23):2220-2229. [doi:10.1056/NEJMoa1809064](https://doi.org/10.1056/NEJMoa1809064) · [PubMed 30280641](https://pubmed.ncbi.nlm.nih.gov/30280641/)
[^paz-ares-2019-caspian]: Paz-Ares L, Dvorkin M, Chen Y, et al. Durvalumab plus platinum-etoposide versus platinum-etoposide in first-line treatment of extensive-stage small-cell lung cancer (CASPIAN). *Lancet.* 2019;394(10212):1929-1939. [doi:10.1016/S0140-6736(19)32222-6](https://doi.org/10.1016/S0140-6736(19)32222-6) · [PubMed 31590988](https://pubmed.ncbi.nlm.nih.gov/31590988/)
