---
schema: human-scale-entry/v1
id: breast-cancer
name: Breast Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common cancer in women; driven by ER/PR hormone signaling, HER2 amplification, and basal TNBC subtypes. BRCA1/2 mutations drive hereditary cases; CDK4/6 inhibitors (palbociclib), anti-HER2 (trastuzumab), PARP inhibitors (olaparib), and immunotherapy are mainstays."
aliases: ["breast carcinoma", "HR+ breast cancer", "HER2+ breast cancer", "TNBC", "triple-negative breast cancer", "luminal A", "luminal B", "invasive ductal carcinoma", "invasive lobular carcinoma", "DCIS"]
sources:
  - id: siegel-2024-cancer-statistics
    type: peer-reviewed
    cite: "Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. CA Cancer J Clin. 2024;74(1):12-49."
    doi: "10.3322/caac.21820"
    pmid: "38230766"
    url: "https://doi.org/10.3322/caac.21820"
  - id: slamon-2001-trastuzumab-trial
    type: peer-reviewed
    cite: "Slamon DJ, Leyland-Jones B, Shak S, et al. Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. N Engl J Med. 2001;344(11):783-792."
    doi: "10.1056/NEJM200103153441101"
    pmid: "11248153"
    url: "https://doi.org/10.1056/NEJM200103153441101"
  - id: finn-2016-palbociclib-paloma2
    type: peer-reviewed
    cite: "Finn RS, Martin M, Rugo HS, et al. Palbociclib and letrozole in advanced breast cancer. N Engl J Med. 2016;375(20):1925-1936."
    doi: "10.1056/NEJMoa1607303"
    pmid: "27959613"
    url: "https://doi.org/10.1056/NEJMoa1607303"
cross_links:
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "HER2 amplification (~20% of breast cancers) → constitutive kinase → PI3K-AKT-mTOR and RAS-ERK → aggressive biology; trastuzumab + pertuzumab + docetaxel is first-line HER2+ metastatic (CLEOPATRA OS 57 vs. 41 months); T-DM1 and T-DXd (DESTINY-Breast03) are second-line."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA mutations occur in 30-40% of HR+/HER2- breast cancer → PI3K-AKT-mTOR activation → endocrine therapy resistance; alpelisib (PI3K-alpha inhibitor) + fulvestrant is approved for PIK3CA-mutant HR+/HER2- metastatic breast cancer (SOLAR-1, PFS 11.0 vs. 5.7 months)."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1 germline mutations confer ~70% lifetime breast cancer risk (predominantly TNBC); BRCA1 loss → HR deficiency → PARP inhibitor sensitivity; olaparib (OlympiAD) and talazoparib (EMBRACA) are approved for BRCA1/2-mutant HER2-negative metastatic breast cancer."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) + AI are standard-of-care first-line for HR+/HER2- metastatic breast cancer; ribociclib + letrozole improved OS to 63.9 vs. 51.4 months (MONALEESA-2); abemaciclib is approved adjuvantly for high-risk early-stage disease."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "ERα (ESR1) drives ~70-75% of breast cancers; aromatase inhibitors (anastrozole, letrozole) are first-line adjuvant for postmenopausal ER+ disease; fulvestrant (SERD) degrades ERα; ESR1 LBD mutations (D538G, Y537S) cause AI resistance in metastatic HR+ disease."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "PR+ breast cancers have better prognosis than PR- tumors; combined E2+progestogen HRT (WHI) increased breast cancer risk vs. estrogen-only; progestins in combined OCP contribute to VTE risk; PR agonists (megestrol, medroxyprogesterone) treat endometrial hyperplasia and EC."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Breast cancer bone metastases exploit the RANKL axis: PTHrP from tumor cells → osteoblast RANKL → osteoclast osteolysis releases TGF-β and IGF-1 → vicious cycle of tumor-bone crosstalk; denosumab (Xgeva) delays skeletal-related events by ~8.5 months vs. zoledronate (HALT-BC)."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Breast cancer overexpresses CXCR4 → homing to CXCL12-rich organs (bone marrow, lung, liver, brain) → organ-specific metastasis; stromal CXCL12 promotes primary tumor growth; CXCR4 correlates with lymph node involvement and poor prognosis; anti-CXCR4 therapy in trials."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Ang-2 promotes breast cancer angiogenesis: hypoxic tumor cells secrete Ang-2 → vessel destabilization → VEGF-driven sprouting; tumor Ang-2 correlates with lymph node metastasis and poor prognosis; Ang-2 blockade combined with anti-VEGF shows additive anti-tumor activity."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Breast and endometrial cancers are linked estrogen-driven malignancies: unopposed estrogen fuels both, and tamoxifen—an anti-estrogen in breast tissue—acts as a uterine estrogen agonist, raising endometrial cancer risk; obesity and the hormone milieu tie the two together."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Breast and ovarian cancers are the twin BRCA1/2 tumors of hereditary breast-ovarian cancer syndrome: germline BRCA loss cripples homologous-recombination repair, predisposing to both and making them exquisitely sensitive to PARP inhibitors (olaparib) and platinum chemotherapy."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Bone is the most common site of breast cancer metastasis: tumor cells secrete PTHrP that drives osteoblasts to overproduce RANKL → osteoclast activation → osteolytic destruction and a cycle releasing bone-stored growth factors; denosumab and bisphosphonates target this loop."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "Hereditary breast and ovarian cancer syndrome from germline BRCA1/2 underlies ~5-10% of breast cancers: it brings early-onset, often triple-negative or bilateral tumors, intensified screening and risk-reducing surgery, and platinum/PARP-inhibitor sensitivity."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Li-Fraumeni syndrome is a striking cause of early breast cancer: germline TP53 loss yields breast cancer (often HER2-positive) in women under 30 alongside sarcomas—and because radiotherapy can induce second cancers, treatment favors mastectomy over radiation."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Triple-negative breast cancer is the subtype most responsive to immunotherapy: its higher mutational burden and tumor-infiltrating cytotoxic T cells make it sensitive to PD-1/PD-L1 blockade (pembrolizumab), unlike the immunologically quiet hormone-receptor-positive tumors."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Breast cancer is a core feature of Cowden syndrome: germline PTEN loss unleashing PI3K-AKT gives a high lifetime breast cancer risk alongside thyroid and endometrial cancer—so Cowden is one of the hereditary syndromes screened for in familial breast cancer."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is integral to breast cancer treatment: after lumpectomy, whole-breast or partial radiation halves local recurrence, and post-mastectomy radiation treats high-risk disease—radiation made breast-conserving surgery as safe as mastectomy."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Breast and prostate cancer are the paradigm hormone-driven cancers and share BRCA biology: breast growth depends on estrogen, prostate on androgens (blocked by ADT), and BRCA2 raises risk of both—endocrine therapy is central to each."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "BRCA2 mutation strongly predisposes to breast cancer: this DNA-repair gene, when lost, leaves cells unable to fix double-strand breaks, so hereditary BRCA2 tumors arise young and are exquisitely sensitive to PARP inhibitors that exploit the repair defect."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 blockade has entered breast cancer through its most aggressive subtype: triple-negative tumors carry more mutations and immune infiltrate, so adding anti-PD-1 (pembrolizumab) to chemotherapy improves outcomes where hormonal and HER2 therapies do not apply."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Breast cancer spreads first through the lymphatic system: tumor cells drain to axillary nodes, so sentinel-node biopsy stages the disease and nodal involvement is among the strongest prognostic factors—guiding decisions on radiation and systemic therapy."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Breast cancer is a leading source of brain metastases: HER2-positive and triple-negative subtypes especially seed the brain, where the blood-brain barrier shields tumor cells from many drugs—so brain-penetrant agents like tucatinib are changing outcomes."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cancer-associated fibroblasts shape breast tumors: they build the stiff, desmoplastic stroma that aids invasion, fuels growth signals, and blocks drug delivery and immune access—so the fibroblast-rich microenvironment, not just tumor cells, drives progression."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity worsens breast cancer at both ends: after menopause, fat tissue's aromatase raises estrogen that drives hormone-receptor-positive tumors, and obesity-linked inflammation and insulin resistance worsen prognosis—so weight is a modifiable risk and outcome factor."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a frequent breast-cancer metastatic site: spread there, alongside bone, lung and brain, marks stage IV disease and worsens prognosis, so liver function and imaging are watched—and HR-positive cancers can colonize it years after the primary."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages help breast cancer spread: recruited into the tumor, they promote angiogenesis, invasion and immune evasion, and a macrophage-rich microenvironment predicts worse outcome—making them a target alongside the cancer cells."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol is a clear, modifiable breast-cancer risk: even moderate drinking raises risk by increasing estrogen and generating DNA-damaging acetaldehyde, so reducing alcohol is one of the few lifestyle levers proven to lower breast-cancer incidence."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is a frequent home for breast-cancer spread: tumor cells seeded through the blood lodge in its fine capillaries and grow, so lung metastases—as nodules or a diffuse lymphatic pattern—are a common cause of breast-cancer morbidity."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Breast fat fuels the tumor it surrounds: adipocytes in the breast make aromatase that converts androgens to estrogen, feeding hormone-driven cancer, which is part of why obesity raises postmenopausal breast-cancer risk."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Breast cancer hijacks bone's demolition crew: metastatic cells release RANKL and factors that activate osteoclasts to dissolve bone, releasing growth factors that feed the tumor in a vicious cycle behind painful osteolytic lesions."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Breast cancer in bone can flood the blood with calcium: osteolytic metastases dissolve bone faster than the body can clear the released calcium, causing the hypercalcemia of malignancy—confusion, thirst, and kidney injury needing urgent care."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Breast cancer can hide in the bone marrow: single tumor cells lodge there and lie dormant for years, a reservoir of disseminated disease that can reawaken to cause the late relapses unique to this cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help hold breast cancer in check: these innate lymphocytes can detect and destroy tumor cells without prior sensitization, and strong NK activity is linked to fewer metastases and better outcomes."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper fuels breast cancer's spread: tumors need it for new blood vessels and for enzymes that prime metastasis, so copper-lowering drugs have been trialed to keep dormant disease asleep."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Breast cancer can invade the skin: inflammatory breast cancer reddens and dimples it into peau d'orange, and chest-wall skin recurrences signal aggressive local disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Breast tumors build a fibrotic stroma: a dense, desmoplastic scar stiffens the tumor, shows as the spiculated mass on a mammogram, and helps shield the cancer from drugs."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads breast cancer's glandular roots: ductal carcinoma cells retain microvilli-lined intracytoplasmic lumina and secretory features, ultrastructure that confirms epithelial origin when a poorly differentiated tumor is hard to classify."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Breast cancer is the eye's commonest invader: it is the leading source of choroidal metastasis, the tumor seeding the back of the eye to blur vision, sometimes the first hint that the cancer has spread."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Breast cancer recruits platelets to spread: circulating tumor cells cloak themselves in platelets to hide from immune attack and lodge in distant organs, while the tumor also drives the clotting risk that haunts cancer patients."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The chemotherapy bites the nerves: taxanes like paclitaxel, central to breast cancer treatment, injure peripheral sensory neurons into a stocking-glove neuropathy that can force dose cuts and outlast the therapy."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Two breast cancer drugs strain the heart: the HER2 antibody trastuzumab and the anthracyclines can each weaken the myocardium, so cardiac function is monitored before and during treatment to catch a falling ejection fraction."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Treatment reshapes reproductive life: chemotherapy can force premature menopause and infertility, while tamoxifen — protective in the breast — stimulates the uterine lining and raises endometrial cancer risk."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies define and treat the disease: ER, PR, and HER2 immunostains classify every tumor and pick the therapy, and the targeted drugs are antibodies themselves — trastuzumab and pertuzumab against HER2, plus the newer antibody-drug conjugates."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Chemotherapy hammers the marrow: the anthracycline and taxane regimens are myelosuppressive, dropping neutrophil counts so that growth-factor support and febrile-neutropenia vigilance run through treatment."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Lobular breast cancer has a strange destination: the diffuse, single-file invasive lobular type characteristically metastasizes to the stomach and GI tract, sometimes mimicking a primary gastric cancer years after the breast tumor."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Losing p53 marks the hardest breast cancers: TP53 mutation is the rule in triple-negative and Li-Fraumeni-driven disease, unleashing genomic instability and an aggressive course that resists hormone and HER2 therapies."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The cure can wound the heart: anthracyclines and HER2-targeted trastuzumab are cardiotoxic, so cancer-therapy-related heart failure is a key survivorship concern that ties breast oncology to cardiology surveillance."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Tumors recruit Tregs to hide from immunity: regulatory T cells infiltrate the breast tumor microenvironment and suppress the cytotoxic response, a marker of worse prognosis and a barrier to immunotherapy."
  - target: 01-human/03-molecular/palb2
    relation: connects-to
    note: "Another repair gene joins BRCA: germline PALB2 mutations, which partner BRCA2 in homologous recombination, confer a high breast cancer risk and the same sensitivity to PARP inhibitors, widening who gets genetic testing."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "ER-positive tumors lean on a growth hub: PI3K-AKT-mTOR signaling drives proliferation and resistance to hormone therapy, so the mTOR inhibitor everolimus is added to endocrine treatment when the cancer escapes it."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplification marks the aggressive tumors: MYC is frequently amplified in basal and triple-negative breast cancer, powering relentless proliferation in the subtypes that lack hormonal and HER2 targets."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB drives the hardest-to-treat subtype: constitutive NF-κB signaling supports survival, inflammation and metastasis in ER-negative and triple-negative breast cancer, a pathway studied where hormonal and HER2 targets are absent."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The cancer and its therapy both clot: breast cancer raises thrombosis risk, compounded by tamoxifen and chemotherapy, so deep-vein thrombosis and pulmonary embolism are recognized complications of treatment."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Chemo strips the body's defenses: the cytotoxic regimens used against breast cancer cause neutropenia, making febrile neutropenia and sepsis a recurring hazard of treatment."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Its hormone therapy strips the bone: aromatase inhibitors and ovarian suppression for estrogen-receptor-positive breast cancer cut estrogen sharply, accelerating bone loss so that osteoporosis monitoring and treatment accompany therapy."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Tumor inflammation and chemo blunt the marrow: the IL-6 of advanced breast cancer raises hepcidin while cytotoxic therapy suppresses erythropoiesis, adding an anemia-of-chronic-disease component to treatment cytopenias."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "The diagnosis and its toll weigh on mood: depression is common across the breast-cancer journey, driven by the threat to life, the effects of surgery and chemotherapy, and the menopausal symptoms of endocrine therapy."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Treatment leaves nerves aching: taxane chemotherapy causes peripheral neuropathy, mastectomy can produce post-surgical neuropathic pain, and aromatase inhibitors bring disabling arthralgias."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Cancer and its therapy raise clot risk to the brain: the hypercoagulable state of malignancy, tamoxifen's thrombotic risk and chest radiation's vascular damage together raise the risk of ischemic stroke."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its chemotherapy opens the lung to mold: the neutropenia from breast-cancer chemotherapy can let inhaled Aspergillus invade as pulmonary aspergillosis, particularly with dose-dense regimens."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Most breast cancer is hormone-driven: oestrogen-receptor-positive tumours grow on oestrogen, so endocrine therapy with tamoxifen or aromatase inhibitors is central, bringing menopausal symptoms and bone loss."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Mastectomy and radiation heal slowly: breast surgery with reconstruction and axillary dissection leaves wounds prone to seroma and infection, and prior or adjuvant radiation impairs tissue healing."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Recurrence fear breeds chronic worry: the scan and tumour-marker surveillance, body-image change and dread of relapse in breast cancer foster persistent health anxiety alongside depression."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Bone is its favourite distant home: breast cancer most often metastasises to the skeleton, causing bone pain, pathological fractures, hypercalcaemia and spinal cord compression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads to lung and pleura: breast cancer commonly metastasises to the lungs and pleura, producing nodules and malignant pleural effusions with breathlessness."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It reaches the brain: HER2-positive and triple-negative breast cancers in particular metastasise to the brain and leptomeninges, causing headaches, seizures and focal deficits."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its treatments are cardiotoxic: anthracyclines and HER2-targeted trastuzumab can weaken the heart muscle, and radiation to the left breast raises later coronary disease."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It declares itself on the skin: inflammatory breast cancer gives a peau d'orange dimpling, Paget disease scales the nipple, and chest-wall recurrences seed skin nodules."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It can spread to the gut: lobular breast cancer in particular metastasises to the stomach and bowel, while chemotherapy and endocrine therapy bring nausea and hepatotoxicity."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Molecular subtyping drives its treatment: HER2 antibodies (trastuzumab, pertuzumab, T-DXd), CDK4/6 inhibitors for hormone-receptor-positive disease and PARP inhibitors for BRCA-mutant tumours are central to modern breast cancer care."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune microenvironment shapes outcome: tumour-infiltrating lymphocytes predict response in triple-negative breast cancer, where checkpoint inhibitors added to chemotherapy now improve survival."
  - target: 03-medicine/03-food/sulforaphane
    relation: connects-to
    note: "Diet is studied for prevention: cruciferous-vegetable sulforaphane is investigated for breast cancer chemoprevention through effects on oestrogen metabolism and tumour-cell signalling."
---

# Breast Cancer

## Overview

**Breast cancer** is the **most common cancer in women worldwide** and the second leading cause of cancer-related death in women. In 2024, approximately **310,720 new cases** of invasive breast cancer will be diagnosed in the United States, with ~42,000 deaths [^siegel-2024-cancer-statistics]. It is now surpassed by lung cancer in global cancer deaths but remains the most diagnosed cancer among women globally.

**Breast cancer is biologically heterogeneous** — it is best understood as multiple distinct diseases with different molecular drivers, natural histories, prognoses, and treatment strategies, unified by their tissue of origin in mammary epithelium.

**Intrinsic molecular subtypes (PAM50 classification):**
- **Luminal A (~40%):** ER+/PR+, HER2-, low Ki-67 (grade 1-2); best prognosis; driven by estrogen signaling; responds well to hormone therapy; chemotherapy often unnecessary; 10-year DFS >85%; endocrine therapy is sufficient in most
- **Luminal B (~20%):** ER+, HER2-/+, high Ki-67 or grade 3; more proliferative than Luminal A; may benefit from chemotherapy; worse prognosis than Luminal A; CDK4/6 inhibitors have greatest benefit
- **HER2-enriched (~15%):** HER2 amplification/overexpression; ER-negative; aggressive; transformed by advent of HER2-targeted therapy; trastuzumab + pertuzumab + chemotherapy → DFS ~90% at 3 years in early stage; T-DXd highly active in metastatic
- **Basal-like/TNBC (~15%):** ER-, PR-, HER2-; high grade; aggressive; BRCA1-associated tumors mostly in this subtype; no hormonal targets; chemotherapy, immunotherapy (pembrolizumab), PARP inhibitors (BRCA1/2-mutant); worst prognosis but higher rate of pathological complete response to neoadjuvant chemotherapy
- **Normal-like (~5-10%):** Resembles normal breast tissue; variable prognosis

**Hereditary breast cancer:**
- **BRCA1/2 (~5-10% of all breast cancers):** BRCA1 → predominantly TNBC/basal-like; BRCA2 → Luminal/HER2-enriched; BRCA1/2 mutations → 70%/45% lifetime risk respectively; management: prophylactic mastectomy, bilateral salpingo-oophorectomy (also prevents ovarian cancer), intensive surveillance (annual MRI + mammography from age 25-30)
- **Other hereditary genes:** PALB2 (40-60% lifetime risk, similar to BRCA2), ATM (20-30%), CHEK2 (15-25%), CDH1 (hereditary diffuse gastric + lobular breast cancer), TP53 (Li-Fraumeni — 50-90% lifetime risk), PTEN (Cowden syndrome), STK11 (Peutz-Jeghers)

**Epidemiology and risk factors:**
- **Age:** Incidence rises sharply after 40; peak incidence 60-70 years; younger-onset more likely hereditary or TNBC
- **Hormonal:** Early menarche, late menopause, nulliparity, late first birth, hormone replacement therapy (combined estrogen/progesterone HRT → increased risk), oral contraceptives (modest)
- **Lifestyle:** Obesity (postmenopausal), alcohol consumption, physical inactivity, dense breast tissue (imaging-based risk factor)
- **Prior breast biopsy:** ADH (atypical ductal hyperplasia), ALH → 4-5× increased risk; LCIS → 7-10× risk (marker not obligate precursor)
- **Race:** Black women have lower incidence but higher mortality (later stage at diagnosis, more TNBC, higher grade, socioeconomic/access factors)

## Structure

### Histopathology and staging

**Histological types:**
- **Invasive ductal carcinoma (IDC/NST, no special type, ~75%):** Most common; forms infiltrating cords/nests; graded by Nottingham grade (tubule formation, nuclear pleomorphism, mitotic rate; Grade 1-3)
- **Invasive lobular carcinoma (ILC, ~15%):** CDH1 (E-cadherin) loss → discohesive single-file "Indian file" infiltration; often ER+/lobular; associated with bilateral disease; may be occult on mammogram; responds to endocrine therapy
- **Special types (better prognosis):** Mucinous (colloid), tubular, medullary, cribriform, adenoid cystic (TNBC but indolent)
- **DCIS (ductal carcinoma in situ):** Non-invasive; precursor lesion; managed by excision ± radiation ± endocrine therapy (tamoxifen reduces ipsilateral invasive recurrence); controversial: subset of low-grade DCIS may never become invasive (active surveillance trials: COMET, LORIS, LORD)

**TNM staging (AJCC 8th edition — includes molecular subtype):**
- Stage I-III: Locoregional; curative intent; Stage IV: Distant metastasis (bone, lung, liver, brain most common) — generally incurable but increasingly manageable as chronic disease (median OS in HR+/HER2- metastatic: 3-4 years; HR+ HER2-: improving)
- Prognostic genomic tests (Oncotype DX [21-gene RS], MammaPrint [70-gene], PAM50/Prosigna, EndoPredict) identify which early-stage HR+ breast cancers benefit from adjuvant chemotherapy vs. endocrine therapy alone

### Molecular oncogenesis

**HR+ pathway (estrogen receptor-driven):**
- Estrogen → ER-alpha binding → ER dimerization → ERE binding → cyclin D1, MYC, BCL-2 transcription → G1-S progression
- **PI3K-AKT-mTOR axis:** PIK3CA gain-of-function (30-40% of HR+ tumors) → AKT-mTOR → ER-independent growth → endocrine resistance; PTEN loss (25-30%) → same net effect
- **CDK4/6-Rb axis:** Cyclin D1-CDK4/6 → Rb phosphorylation → E2F activation → S-phase; CDK4/6 inhibitors restore Rb-mediated G1 arrest
- **Endocrine resistance mechanisms:** ESR1 mutations (D538G, Y537S — acquired, found in cfDNA) → ligand-independent ER activation; PI3K pathway activation; CDK4/6 pathway amplification (cyclin D1, CDK4 amplification)

**HER2+ pathway:** See HER2 cross-link entry.

**TNBC/Basal-like:**
- High genomic instability, TP53 mutations (>80%), BRCA1 loss, RB1 loss; driven by PI3K-AKT, EGFR, FGFR, AR (androgen receptor — ~30% of TNBC express AR → potential therapeutic target)
- High tumor-infiltrating lymphocytes (TILs) correlate with better prognosis and immunotherapy response; high PD-L1 expression in ~40% of TNBC → pembrolizumab + chemotherapy approved in PD-L1+ metastatic TNBC (KEYNOTE-522 in early-stage regardless of PD-L1)

## Function

### Clinical presentation and screening

**Presentation:**
- Most common: painless, hard, irregular breast lump; asymmetric thickening
- Nipple discharge (bloody → suspicious), skin changes (peau d'orange = lymphatic obstruction, dimpling, nipple retraction, erythema)
- Inflammatory breast cancer (IBC, 1-3%): Rapid-onset erythema, warmth, edema, peau d'orange of breast skin without palpable mass → dermal lymphatic invasion; aggressive; requires neoadjuvant chemotherapy before surgery
- Paget's disease: Eczematous nipple rash → intraepidermal carcinoma cells (Paget cells); associated with underlying DCIS or invasive cancer in most cases

**Screening:**
- **Mammography:** Annual from age 40-74 (USPSTF updated 2024: recommends starting at 40, previously 50); reduces breast cancer mortality ~15-20% in screened populations; digital breast tomosynthesis (3D mammography) improves cancer detection and reduces false positives vs. 2D
- **MRI:** Annual breast MRI + mammography for high-risk (BRCA1/2, >20% lifetime risk); superior sensitivity in dense breasts; false-positive rate higher
- **Ultrasound:** Supplement to mammography in dense breasts; not a standalone screening tool in average risk

## Pathology

### Diagnosis and biomarkers

**Core needle biopsy:** Ultrasound or stereotactic-guided; provides histology, grade, ER/PR (IHC, % cells + Allred score), HER2 (IHC 0/1+/2+/3+; 2+ → FISH/ISH reflex), Ki-67 (proliferation index)

**Genomic testing in early-stage HR+/HER2- breast cancer:**
- **Oncotype DX (21-gene recurrence score, RS):** Predicts 10-year distant recurrence risk and chemotherapy benefit in node-negative (TAILORx trial) and 1-3 node-positive (RxPONDER) ER+/HER2- early breast cancer; RS <26 → endocrine therapy alone (chemotherapy no benefit in postmenopausal); RS ≥26 → chemotherapy benefit; now standard of care globally
- **MammaPrint (70-gene):** MINDACT trial: ~46% of clinically high-risk/genomic low-risk patients spared chemotherapy; approved in US for node-negative or 1-3 node-positive HR+/HER2-

### Treatment

**Early-stage (curative intent):**

*Surgery:*
- Breast-conserving surgery (lumpectomy + radiation) equivalent to mastectomy in OS for stages I-II; sentinel lymph node biopsy standard (avoids axillary lymph node dissection in sentinel-negative; Z0011 trial validates omission of ALND in limited nodal disease); nipple-sparing mastectomy with reconstruction increasingly used

*Radiation:*
- Post-lumpectomy whole-breast radiation reduces local recurrence 50-70%; hypofractionation (40 Gy/15 fractions) vs. conventional (50 Gy/25 fractions) equivalent efficacy; partial breast irradiation for select low-risk early-stage; regional nodal irradiation for ≥4 positive nodes

*Adjuvant systemic therapy by subtype:*
- **HR+:** Endocrine therapy 5-10 years (tamoxifen premenopausal; AI postmenopausal ± ovarian suppression); CDK4/6 inhibitors (abemaciclib × 2 years for high-risk, monarchE: significantly improved DFS)
- **HER2+:** Trastuzumab × 1 year ± pertuzumab (APHINITY); T-DM1 for residual disease after neoadjuvant (KATHERINE: iDFS 88% vs. 77% trastuzumab)
- **TNBC:** Pembrolizumab + chemotherapy neoadjuvant → pembrolizumab adjuvant (KEYNOTE-522: EFS benefit regardless of pCR); capecitabine for non-pCR; olaparib adjuvant for BRCA1/2-mutant (OlympiA: distant DFS benefit) [^slamon-2001-trastuzumab-trial]

**Metastatic HR+/HER2- (chronic disease management):**
- **First-line:** CDK4/6 inhibitor + AI (palbociclib/PALOMA-2, ribociclib/MONALEESA-2, abemaciclib/MONARCH-3); OS benefit confirmed for ribociclib (63.9 vs. 51.4 months, MONALEESA-2) [^finn-2016-palbociclib-paloma2]
- **Second-line (post-CDK4/6 + ESR1 mutation):** Elacestrant (oral SERD, EMERALD trial: PFS benefit in ESR1-mutant); fulvestrant + alpelisib (SOLAR-1, PIK3CA-mutant)
- **mTOR inhibitors:** Everolimus + exemestane (BOLERO-2: PFS 10.6 vs. 4.1 months); capivasertib (AKT inhibitor) + fulvestrant (CAPItello-291: approved for PIK3CA/AKT/PTEN-altered)
- **ADC (antibody-drug conjugate):** Sacituzumab govitecan (TROPION-Breast01 in HR+) and trastuzumab deruxtecan (T-DXd, DESTINY-Breast06 in HER2-low HR+) expanding options

**Metastatic TNBC:**
- **PD-L1+ (CPS ≥10):** Pembrolizumab + chemotherapy (KEYNOTE-355: OS 23.0 vs. 16.1 months)
- **BRCA1/2-mutant:** Olaparib (OlympiAD) or talazoparib (EMBRACA) superior to chemotherapy
- **Sacituzumab govitecan (Trodelvy, Trop-2 ADC):** ASCENT trial: OS 12.1 vs. 6.7 months vs. chemotherapy; approved for 2L+ TNBC

## Connections

- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — HER2 amplification (~20% of breast cancers) → constitutive kinase → PI3K-AKT-mTOR and RAS-ERK → aggressive biology; trastuzumab + pertuzumab + docetaxel is first-line HER2+ metastatic (CLEOPATRA: OS 57 vs. 41 months); T-DXd leads in second-line.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutations in 30-40% of HR+/HER2- breast cancer → PI3K-AKT-mTOR → endocrine therapy resistance; alpelisib + fulvestrant is approved for PIK3CA-mutant HR+/HER2- metastatic breast cancer (SOLAR-1, PFS 11.0 vs. 5.7 months).
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BRCA1 germline mutations confer ~70% lifetime breast cancer risk (predominantly TNBC); BRCA1 loss → HR deficiency → PARP inhibitor sensitivity; olaparib (OlympiAD) and talazoparib (EMBRACA) approved for BRCA1/2-mutant HER2-negative metastatic breast cancer.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) + AI are standard-of-care first-line for HR+/HER2- metastatic breast cancer; ribociclib + letrozole improved OS to 63.9 vs. 51.4 months (MONALEESA-2); abemaciclib approved adjuvantly for high-risk early-stage HR+ disease.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — ERα (ESR1) drives ~70-75% of breast cancers; aromatase inhibitors (anastrozole, letrozole) are first-line adjuvant for postmenopausal ER+ disease; fulvestrant (SERD) degrades ERα; ESR1 LBD mutations (D538G, Y537S) cause AI resistance in metastatic HR+ disease.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — PR+ breast cancers have better prognosis than PR- tumors; combined E2+progestogen HRT (WHI) increased breast cancer risk vs. estrogen-only; progestins in combined OCP contribute to VTE risk; PR agonists (megestrol, medroxyprogesterone) treat endometrial hyperplasia and EC.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — breast cancer bone metastases exploit the RANKL axis: PTHrP from tumor cells → osteoblast RANKL → osteoclast osteolysis releases TGF-β and IGF-1 → vicious cycle of tumor-bone crosstalk; denosumab (Xgeva) delays skeletal-related events by ~8.5 months vs. zoledronate (HALT-BC).
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Breast cancer overexpresses CXCR4 → homing to CXCL12-rich organs (bone marrow, lung, liver, brain) → organ-specific metastasis; stromal CXCL12 promotes primary tumor growth; CXCR4 correlates with lymph node involvement and poor prognosis; anti-CXCR4 therapy in trials.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Ang-2 promotes breast cancer angiogenesis: hypoxic tumor cells secrete Ang-2 → vessel destabilization → VEGF-driven sprouting; tumor Ang-2 correlates with lymph node metastasis and poor prognosis; Ang-2 blockade combined with anti-VEGF shows additive anti-tumor activity.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Breast and endometrial cancers are linked estrogen-driven malignancies: unopposed estrogen fuels both, and tamoxifen—an anti-estrogen in breast tissue—acts as a uterine estrogen agonist, raising endometrial cancer risk; obesity and the hormone milieu tie the two together.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Breast and ovarian cancers are the twin BRCA1/2 tumors of hereditary breast-ovarian cancer syndrome: germline BRCA loss cripples homologous-recombination repair, predisposing to both and making them exquisitely sensitive to PARP inhibitors (olaparib) and platinum chemotherapy.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Bone is the most common site of breast cancer metastasis: tumor cells secrete PTHrP that drives osteoblasts to overproduce RANKL → osteoclast activation → osteolytic destruction and a cycle releasing bone-stored growth factors; denosumab and bisphosphonates target this loop.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — Hereditary breast and ovarian cancer syndrome from germline BRCA1/2 underlies ~5-10% of breast cancers: it brings early-onset, often triple-negative or bilateral tumors, intensified screening and risk-reducing surgery, and platinum/PARP-inhibitor sensitivity.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Li-Fraumeni syndrome is a striking cause of early breast cancer: germline TP53 loss yields breast cancer (often HER2-positive) in women under 30 alongside sarcomas—and because radiotherapy can induce second cancers, treatment favors mastectomy over radiation.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Triple-negative breast cancer is the subtype most responsive to immunotherapy: its higher mutational burden and tumor-infiltrating cytotoxic T cells make it sensitive to PD-1/PD-L1 blockade (pembrolizumab), unlike the immunologically quiet hormone-receptor-positive tumors.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Breast cancer is a core feature of Cowden syndrome: germline PTEN loss unleashing PI3K-AKT gives a high lifetime breast cancer risk alongside thyroid and endometrial cancer—so Cowden is one of the hereditary syndromes screened for in familial breast cancer.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is integral to breast cancer treatment: after lumpectomy, whole-breast or partial radiation halves local recurrence, and post-mastectomy radiation treats high-risk disease—radiation made breast-conserving surgery as safe as mastectomy.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Breast and prostate cancer are the paradigm hormone-driven cancers and share BRCA biology: breast growth depends on estrogen, prostate on androgens (blocked by ADT), and BRCA2 raises risk of both—endocrine therapy is central to each.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — BRCA2 mutation strongly predisposes to breast cancer: this DNA-repair gene, when lost, leaves cells unable to fix double-strand breaks, so hereditary BRCA2 tumors arise young and are exquisitely sensitive to PARP inhibitors that exploit the repair defect.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 blockade has entered breast cancer through its most aggressive subtype: triple-negative tumors carry more mutations and immune infiltrate, so adding anti-PD-1 (pembrolizumab) to chemotherapy improves outcomes where hormonal and HER2 therapies do not apply.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Breast cancer spreads first through the lymphatic system: tumor cells drain to axillary nodes, so sentinel-node biopsy stages the disease and nodal involvement is among the strongest prognostic factors—guiding decisions on radiation and systemic therapy.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Breast cancer is a leading source of brain metastases: HER2-positive and triple-negative subtypes especially seed the brain, where the blood-brain barrier shields tumor cells from many drugs—so brain-penetrant agents like tucatinib are changing outcomes.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cancer-associated fibroblasts shape breast tumors: they build the stiff, desmoplastic stroma that aids invasion, fuels growth signals, and blocks drug delivery and immune access—so the fibroblast-rich microenvironment, not just tumor cells, drives progression.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity worsens breast cancer at both ends: after menopause, fat tissue's aromatase raises estrogen that drives hormone-receptor-positive tumors, and obesity-linked inflammation and insulin resistance worsen prognosis—so weight is a modifiable risk and outcome factor.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a frequent breast-cancer metastatic site: spread there, alongside bone, lung and brain, marks stage IV disease and worsens prognosis, so liver function and imaging are watched—and HR-positive cancers can colonize it years after the primary.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages help breast cancer spread: recruited into the tumor, they promote angiogenesis, invasion and immune evasion, and a macrophage-rich microenvironment predicts worse outcome—making them a target alongside the cancer cells.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol is a clear, modifiable breast-cancer risk: even moderate drinking raises risk by increasing estrogen and generating DNA-damaging acetaldehyde, so reducing alcohol is one of the few lifestyle levers proven to lower breast-cancer incidence.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is a frequent home for breast-cancer spread: tumor cells seeded through the blood lodge in its fine capillaries and grow, so lung metastases—as nodules or a diffuse lymphatic pattern—are a common cause of breast-cancer morbidity.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Breast fat fuels the tumor it surrounds: adipocytes in the breast make aromatase that converts androgens to estrogen, feeding hormone-driven cancer, which is part of why obesity raises postmenopausal breast-cancer risk.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Breast cancer hijacks bone's demolition crew: metastatic cells release RANKL and factors that activate osteoclasts to dissolve bone, releasing growth factors that feed the tumor in a vicious cycle behind painful osteolytic lesions.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Breast cancer in bone can flood the blood with calcium: osteolytic metastases dissolve bone faster than the body can clear the released calcium, causing the hypercalcemia of malignancy—confusion, thirst, and kidney injury needing urgent care.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Breast cancer can hide in the bone marrow: single tumor cells lodge there and lie dormant for years, a reservoir of disseminated disease that can reawaken to cause the late relapses unique to this cancer.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help hold breast cancer in check: these innate lymphocytes can detect and destroy tumor cells without prior sensitization, and strong NK activity is linked to fewer metastases and better outcomes.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper fuels breast cancer's spread: tumors need it for new blood vessels and for enzymes that prime metastasis, so copper-lowering drugs have been trialed to keep dormant disease asleep.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Breast cancer can invade the skin: inflammatory breast cancer reddens and dimples it into peau d'orange, and chest-wall skin recurrences signal aggressive local disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Breast tumors build a fibrotic stroma: a dense, desmoplastic scar stiffens the tumor, shows as the spiculated mass on a mammogram, and helps shield the cancer from drugs.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads breast cancer's glandular roots: ductal carcinoma cells retain microvilli-lined intracytoplasmic lumina and secretory features, ultrastructure that confirms epithelial origin when a poorly differentiated tumor is hard to classify.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Breast cancer is the eye's commonest invader: it is the leading source of choroidal metastasis, the tumor seeding the back of the eye to blur vision, sometimes the first hint that the cancer has spread.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Breast cancer recruits platelets to spread: circulating tumor cells cloak themselves in platelets to hide from immune attack and lodge in distant organs, while the tumor also drives the clotting risk that haunts cancer patients.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The chemotherapy bites the nerves: taxanes like paclitaxel, central to breast cancer treatment, injure peripheral sensory neurons into a stocking-glove neuropathy that can force dose cuts and outlast the therapy.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Two breast cancer drugs strain the heart: the HER2 antibody trastuzumab and the anthracyclines can each weaken the myocardium, so cardiac function is monitored before and during treatment to catch a falling ejection fraction.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Treatment reshapes reproductive life: chemotherapy can force premature menopause and infertility, while tamoxifen — protective in the breast — stimulates the uterine lining and raises endometrial cancer risk.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies define and treat the disease: ER, PR, and HER2 immunostains classify every tumor and pick the therapy, and the targeted drugs are antibodies themselves — trastuzumab and pertuzumab against HER2, plus the newer antibody-drug conjugates.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Chemotherapy hammers the marrow: the anthracycline and taxane regimens are myelosuppressive, dropping neutrophil counts so that growth-factor support and febrile-neutropenia vigilance run through treatment.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Lobular breast cancer has a strange destination: the diffuse, single-file invasive lobular type characteristically metastasizes to the stomach and GI tract, sometimes mimicking a primary gastric cancer years after the breast tumor.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Losing p53 marks the hardest breast cancers: TP53 mutation is the rule in triple-negative and Li-Fraumeni-driven disease, unleashing genomic instability and an aggressive course that resists hormone and HER2 therapies.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The cure can wound the heart: anthracyclines and HER2-targeted trastuzumab are cardiotoxic, so cancer-therapy-related heart failure is a key survivorship concern that ties breast oncology to cardiology surveillance.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Tumors recruit Tregs to hide from immunity: regulatory T cells infiltrate the breast tumor microenvironment and suppress the cytotoxic response, a marker of worse prognosis and a barrier to immunotherapy.
- `connects-to` → **[PALB2](../../03-molecular/palb2/README.md)** — Another repair gene joins BRCA: germline PALB2 mutations, which partner BRCA2 in homologous recombination, confer a high breast cancer risk and the same sensitivity to PARP inhibitors, widening who gets genetic testing.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — ER-positive tumors lean on a growth hub: PI3K-AKT-mTOR signaling drives proliferation and resistance to hormone therapy, so the mTOR inhibitor everolimus is added to endocrine treatment when the cancer escapes it.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplification marks the aggressive tumors: MYC is frequently amplified in basal and triple-negative breast cancer, powering relentless proliferation in the subtypes that lack hormonal and HER2 targets.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB drives the hardest-to-treat subtype: constitutive NF-κB signaling supports survival, inflammation and metastasis in ER-negative and triple-negative breast cancer, a pathway studied where hormonal and HER2 targets are absent.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The cancer and its therapy both clot: breast cancer raises thrombosis risk, compounded by tamoxifen and chemotherapy, so deep-vein thrombosis and pulmonary embolism are recognized complications of treatment.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Chemo strips the body's defenses: the cytotoxic regimens used against breast cancer cause neutropenia, making febrile neutropenia and sepsis a recurring hazard of treatment.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Its hormone therapy strips the bone: aromatase inhibitors and ovarian suppression for estrogen-receptor-positive breast cancer cut estrogen sharply, accelerating bone loss so that osteoporosis monitoring and treatment accompany therapy.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Tumor inflammation and chemo blunt the marrow: the IL-6 of advanced breast cancer raises hepcidin while cytotoxic therapy suppresses erythropoiesis, adding an anemia-of-chronic-disease component to treatment cytopenias.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — The diagnosis and its toll weigh on mood: depression is common across the breast-cancer journey, driven by the threat to life, the effects of surgery and chemotherapy, and the menopausal symptoms of endocrine therapy.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Treatment leaves nerves aching: taxane chemotherapy causes peripheral neuropathy, mastectomy can produce post-surgical neuropathic pain, and aromatase inhibitors bring disabling arthralgias.
- `connects-to` → **[Stroke](../stroke/README.md)** — Cancer and its therapy raise clot risk to the brain: the hypercoagulable state of malignancy, tamoxifen's thrombotic risk and chest radiation's vascular damage together raise the risk of ischemic stroke.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its chemotherapy opens the lung to mold: the neutropenia from breast-cancer chemotherapy can let inhaled Aspergillus invade as pulmonary aspergillosis, particularly with dose-dense regimens.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Most breast cancer is hormone-driven: oestrogen-receptor-positive tumours grow on oestrogen, so endocrine therapy with tamoxifen or aromatase inhibitors is central, bringing menopausal symptoms and bone loss.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Mastectomy and radiation heal slowly: breast surgery with reconstruction and axillary dissection leaves wounds prone to seroma and infection, and prior or adjuvant radiation impairs tissue healing.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Recurrence fear breeds chronic worry: the scan and tumour-marker surveillance, body-image change and dread of relapse in breast cancer foster persistent health anxiety alongside depression.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Bone is its favourite distant home: breast cancer most often metastasises to the skeleton, causing bone pain, pathological fractures, hypercalcaemia and spinal cord compression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads to lung and pleura: breast cancer commonly metastasises to the lungs and pleura, producing nodules and malignant pleural effusions with breathlessness.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It reaches the brain: HER2-positive and triple-negative breast cancers in particular metastasise to the brain and leptomeninges, causing headaches, seizures and focal deficits.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its treatments are cardiotoxic: anthracyclines and HER2-targeted trastuzumab can weaken the heart muscle, and radiation to the left breast raises later coronary disease.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It declares itself on the skin: inflammatory breast cancer gives a peau d'orange dimpling, Paget disease scales the nipple, and chest-wall recurrences seed skin nodules.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It can spread to the gut: lobular breast cancer in particular metastasises to the stomach and bowel, while chemotherapy and endocrine therapy bring nausea and hepatotoxicity.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Molecular subtyping drives its treatment: HER2 antibodies (trastuzumab, pertuzumab, T-DXd), CDK4/6 inhibitors for hormone-receptor-positive disease and PARP inhibitors for BRCA-mutant tumours are central to modern breast cancer care.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune microenvironment shapes outcome: tumour-infiltrating lymphocytes predict response in triple-negative breast cancer, where checkpoint inhibitors added to chemotherapy now improve survival.
- `connects-to` → **[Sulforaphane](../../../03-medicine/03-food/sulforaphane/README.md)** — Diet is studied for prevention: cruciferous-vegetable sulforaphane is investigated for breast cancer chemoprevention through effects on oestrogen metabolism and tumour-cell signalling.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^siegel-2024-cancer-statistics]: Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. *CA Cancer J Clin.* 2024;74(1):12-49. [doi:10.3322/caac.21820](https://doi.org/10.3322/caac.21820) · [PubMed 38230766](https://pubmed.ncbi.nlm.nih.gov/38230766/)
[^slamon-2001-trastuzumab-trial]: Slamon DJ, Leyland-Jones B, Shak S, et al. Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. *N Engl J Med.* 2001;344(11):783-792. [doi:10.1056/NEJM200103153441101](https://doi.org/10.1056/NEJM200103153441101) · [PubMed 11248153](https://pubmed.ncbi.nlm.nih.gov/11248153/)
[^finn-2016-palbociclib-paloma2]: Finn RS, Martin M, Rugo HS, et al. Palbociclib and letrozole in advanced breast cancer. *N Engl J Med.* 2016;375(20):1925-1936. [doi:10.1056/NEJMoa1607303](https://doi.org/10.1056/NEJMoa1607303) · [PubMed 27959613](https://pubmed.ncbi.nlm.nih.gov/27959613/)
