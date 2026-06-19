---
schema: human-scale-entry/v1
id: bladder-cancer
name: Bladder Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Urothelial carcinoma of the bladder; FGFR3 mutations in ~25-35% and TERT promoter mutations in ~75%; PD-L1 expression guides immunotherapy. BCG is standard for non-muscle-invasive disease; enfortumab vedotin + pembrolizumab is first-line for metastatic urothelial carcinoma."
aliases: ["urothelial carcinoma", "bladder urothelial carcinoma", "transitional cell carcinoma", "NMIBC", "MIBC", "metastatic urothelial carcinoma", "mUC", "bladder TCC"]
sources:
  - id: bellmunt-2017-keynote045
    type: peer-reviewed
    cite: "Bellmunt J, de Wit R, Vaughn DJ, et al. Pembrolizumab as second-line therapy for advanced urothelial carcinoma. N Engl J Med. 2017;376(11):1015-1026."
    doi: "10.1056/NEJMoa1613683"
    pmid: "28212060"
    url: "https://doi.org/10.1056/NEJMoa1613683"
  - id: powles-2024-ev302
    type: peer-reviewed
    cite: "Powles T, Valderrama BP, Gupta S, et al. Enfortumab vedotin and pembrolizumab in untreated advanced urothelial cancer. N Engl J Med. 2024;390(10):875-888."
    doi: "10.1056/NEJMoa2312117"
    pmid: "38261487"
    url: "https://doi.org/10.1056/NEJMoa2312117"
  - id: loriot-2019-erdafitinib
    type: peer-reviewed
    cite: "Loriot Y, Necchi A, Park SH, et al. Erdafitinib in locally advanced or metastatic urothelial carcinoma. N Engl J Med. 2019;381(4):338-348."
    doi: "10.1056/NEJMoa1817323"
    pmid: "31340094"
    url: "https://doi.org/10.1056/NEJMoa1817323"
cross_links:
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "FGFR3 is mutated or fused in ~25-35% of urothelial carcinoma (S249C, FGFR3-TACC3 common); mutated FGFR3 drives proliferation and is enriched in low-grade NMIBC; erdafitinib (THOR trial: OS 12.1 vs. 7.8 months vs. pembrolizumab) is FDA-approved for FGFR-altered bladder cancer."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-L1 drives immune evasion in urothelial carcinoma; pembrolizumab improves OS vs. chemotherapy in post-platinum mUC (KEYNOTE-045: OS 10.3 vs. 7.4 months); enfortumab vedotin + pembrolizumab (EV-302) is now first-line standard for metastatic urothelial carcinoma."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutations (C228T/C250T) occur in ~75% of urothelial carcinoma — among the highest frequencies in any cancer; TERT mutation is one of the earliest carcinogenic events (present in dysplasia and NMIBC); urine TERT mutation detection enables non-invasive surveillance."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB1 loss occurs in ~20% of muscle-invasive bladder cancer (MIBC), co-occurring with TP53 mutation; RB1 deletion correlates with basal-squamous MIBC subtype and poor prognosis; RB pathway disruption also mediated by CDKN2A homozygous deletion in ~30% of MIBC."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 is mutated in ~48% of MIBC; co-deletion with RB1 defines the basal/squamous MIBC subtype (high PD-L1, cisplatin-sensitive); TERT promoter + TP53 mutations co-occur in high-grade UC; TP53 mutation in CIS is an early checkpoint failure enabling invasive progression."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Lynch syndrome (germline MLH1/MSH2) confers ~5× lifetime bladder UC risk; dMMR bladder cancer (~3-4% of UC) has high TMB → pembrolizumab active regardless of PD-L1 (KEYNOTE-158); dMMR IHC/MSI-H testing recommended for early-onset or Lynch-suspected urothelial carcinoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A mutations in ~25% of MIBC; SWI/SNF chromatin remodeler; ARID1A LOF → impaired nucleosome remodeling at tumor suppressor promoters; co-mutated with TP53 and KDM6A; ARID1A-mutant MIBC may have synthetic lethality with EZH2 inhibition (tazemetostat combinations under study)."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Bladder cancer is one disease across the whole urinary-tract lining: the same urothelium covers the renal pelvis and ureters, so ~5% of bladder-cancer patients harbour synchronous upper-tract urothelial carcinoma, and a tumour obstructing a ureter causes hydronephrosis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Bladder cancer pioneered immunotherapy: intravesical BCG provokes a Th1 response that recruits CD8+ cytotoxic T cells to patrol the urothelium and prevent recurrence of non-muscle-invasive disease — and the same T cells are reactivated by PD-1/PD-L1 checkpoint blockade."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Cervical and bladder cancer are linked through the pelvis: pelvic radiotherapy for cervical cancer is itself a risk factor for later bladder cancer, both are strongly smoking- or carcinogen-associated, and both are driven by insults delivered to a vulnerable epithelium."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Bladder and prostate cancers are the commonest genitourinary malignancies and frequent neighbors: they co-occur in older men, share smoking and age risk, and locally advanced disease of one can invade the other; pelvic surgery and shared follow-up imaging link their care."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Bladder cancer is a disease of the whole urothelial lining: the same field-effect carcinogens (smoking, aromatic amines) that transform the bladder can produce synchronous or metachronous tumors of the renal pelvis and ureter, so the entire upper urinary tract needs surveillance."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Bladder cancer is the birthplace of cancer immunotherapy: intravesical BCG—live attenuated mycobacteria—triggers a local immune response that has prevented recurrence of non-muscle-invasive bladder cancer for decades, and PD-1/PD-L1 inhibitors now treat advanced disease."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Bladder and renal cell carcinoma are the two major urologic cancers but differ in cell and cause: bladder cancer is a smoking-linked urothelial tumor with painless hematuria, while RCC arises from renal tubular epithelium—both can shed cells detectable in urine."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Bladder cancer and lung cancer are the paradigm smoking-caused epithelial cancers: tobacco carcinogens excreted in urine bathe and transform the bladder urothelium just as inhaled smoke transforms the bronchus, so the two often coexist and both are reshaped by immunotherapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Bladder cancer pioneered macrophage-based immunotherapy: intravesical BCG provokes a local immune response in which macrophages and T cells attack residual tumor, making early non-muscle-invasive bladder cancer one of the first cancers cured by harnessing innate immunity."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Invasion of the bladder's smooth muscle defines bladder cancer staging: whether the tumor breaches the muscularis propria (muscle-invasive vs non-muscle-invasive) drives management—cystectomy for muscle-invasive disease versus local therapy for superficial tumors."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "HER2 is an emerging target in bladder cancer: a subset of urothelial tumors overexpress HER2, and HER2-directed antibody-drug conjugates like trastuzumab deruxtecan show activity—extending the breast/gastric HER2 paradigm to bladder cancer therapy."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Bladder tumors depend on VEGF-driven angiogenesis: urothelial cancers secrete VEGF to grow new vessels, high VEGF predicts worse outcomes, and anti-angiogenic strategies are explored alongside chemotherapy and immunotherapy in advanced disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy enables bladder preservation in muscle-invasive bladder cancer: photon-beam chemoradiation as part of trimodality therapy can spare the bladder as an alternative to cystectomy in selected patients, controlling the tumor while keeping the organ."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion is common in bladder cancer: loss of this cell-cycle tumor-suppressor (often with FGFR3 or TP53 changes) helps drive urothelial proliferation, marking one of the genetic routes from carcinogen exposure to invasive disease."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Bladder and lung cancer share tobacco as a top cause: carcinogens excreted in urine bathe the urothelium just as inhaled smoke hits the airway, so the two smoking-driven cancers carry high mutation loads and both respond to PD-1 immunotherapy."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Bladder cancer is treated with a TB vaccine: intravesical BCG—live attenuated Mycobacterium bovis, the tuberculosis vaccine strain—instilled into the bladder triggers a local immune response that prevents recurrence of non-muscle-invasive tumors."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Bladder cancer is the classic occupational chemical cancer: carbon-based aromatic amines from dye, rubber, and leather industries are activated by the liver and concentrated in urine, where they mutate the urothelium—a link that founded industrial cancer epidemiology."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "BCG immunotherapy for bladder cancer works through dendritic cells: the mycobacteria are taken up by urothelial and antigen-presenting cells, activating dendritic cells that prime a tumor-killing immune response—innate immunity turned against cancer."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Bladder cancer often overexpresses EGFR-family receptors: urothelial tumors signal through EGFR and HER2 to grow, making the ErbB pathway a studied target alongside the FGFR inhibitors already used in this cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "BCG immunotherapy for bladder cancer mobilizes NK cells: instilling live bacteria into the bladder triggers an innate immune assault in which natural killer cells help destroy superficial tumor cells, a decades-old immunotherapy that predates checkpoint drugs."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Bladder tumors recruit regulatory T cells to evade attack: Tregs accumulate in the bladder wall and suppress cytotoxic immunity, blunting both BCG and PD-1 checkpoint therapy and marking a target to make immunotherapy work better."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Bladder cancer's classic carcinogens are nitrogen-bearing aromatic amines: dyes, rubber and industrial chemicals excreted in urine bathe the bladder lining, which is why occupational aromatic-amine exposure is a textbook cause of the disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "BCG immunotherapy for bladder cancer works through NF-kB: the bacterial vaccine instilled in the bladder ignites NF-kB-driven inflammation that recruits immune cells to kill tumor cells, the oldest and still-used cancer immunotherapy."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils flood the bladder during BCG therapy: the instilled vaccine triggers an acute neutrophil-rich inflammation that helps clear superficial tumor cells, an innate-immune burst central to how this old immunotherapy works."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Bladder cancer spends the body's iron: painless blood in the urine is its cardinal sign, and the ongoing loss drains iron into a deficiency anemia that often prompts the workup that finds the tumor."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Bladder cancer favors the lungs when it spreads: the lung is among its commonest metastatic sites, so chest imaging is part of staging, and lung lesions often mark advanced, incurable disease."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Bladder cancer enlists fibroblasts to invade: cancer-associated fibroblasts in the tumor stroma secrete signals that drive the tumor through the bladder wall, the muscle invasion that separates lethal from curable disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Bladder cancer and its treatment scar the bladder: a desmoplastic tumor stroma and radiation-induced fibrosis stiffen the wall, shrinking capacity and complicating function after therapy."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Bladder cancer is vascular: VEGF recruits endothelial cells to feed the tumor, and the painless visible hematuria that first reveals it comes partly from these fragile new vessels bleeding into the urine."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Bladder cancer spreads to the liver: along with lung and bone, the liver is a common metastatic site, so its imaging is part of staging advanced, incurable disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads bladder cancer's lineage: urothelial carcinoma keeps the surface umbrella cells' specialized membrane plaques and tight junctions, while the squamous type from schistosomiasis shows desmosomes and keratin instead."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bladder cancer favors the skeleton when it spreads: bone is a leading metastatic site after lung and liver, and deposits in the marrow-filled vertebrae and pelvis cause the pain of advanced disease."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "An advanced bladder tumor can breach the bowel: invasion through the bladder wall into the adjacent rectum or sigmoid colon can open a vesicocolic fistula, leaking gas and stool into the urine."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Blood in the urine is the warning sign: painless hematuria — red cells shed into the urine by the friable tumor — is the cardinal presentation of bladder cancer, and chronic loss can leave the patient iron-deficient and anemic."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Engineered antibodies now treat bladder cancer: checkpoint inhibitors like pembrolizumab release the immune brakes, and the antibody-drug conjugate enfortumab vedotin delivers a toxin to nectin-4 on the tumor cells."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The platinum chemotherapy frays the nerves: cisplatin, the backbone of bladder cancer regimens, injures peripheral sensory neurons and the cochlear nerve, leaving numbness and hearing loss that can outlast treatment."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Bladder cancer is treated with a live mycobacterium: intravesical BCG — the attenuated M. bovis strain kin to the TB bacillus — is the standard adjuvant for high-risk non-muscle-invasive disease, igniting a Th1 response that clears tumor cells and can resemble disseminated TB."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Radical cystectomy reaches the reproductive organs: removing the bladder for muscle-invasive cancer usually takes the prostate and seminal vesicles in men, or the uterus and ovaries in women, costing fertility and sexual function alongside urinary diversion."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Bladder cancer drives a clotting state: paraneoplastic thrombocytosis is common and marks worse prognosis, and the tumor's pro-coagulant milieu raises the risk of venous thromboembolism that complicates surgery and chemotherapy."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K signaling is a core bladder-cancer driver: PIK3CA mutations are among the commonest in luminal urothelial tumors, switching on the AKT-mTOR growth pathway and marking a targetable vulnerability."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells gathered in the tumor predict response: tertiary lymphoid structures rich in B cells within bladder tumors forecast better outcomes with immune-checkpoint therapy, a sign the local antibody response matters."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "Smoking sows cancer across many linings: bladder and head-and-neck squamous cancers share tobacco and carcinogen exposure, so a field-cancerized patient with one carries a raised risk of the other."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "The same smoke that scars the lungs lines the bladder: most bladder-cancer patients are smokers and carry COPD as a comorbidity, which raises the anesthetic and surgical risk of the cystectomy their cancer demands."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Lynch syndrome ties bladder to bowel: the mismatch-repair defect that drives colorectal cancer also raises the risk of upper-tract and bladder urothelial cancer, so a Lynch family history changes urologic surveillance."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The urinary microbiome shapes the response: the bladder is not sterile, and its microbial community influences both carcinogenesis and the inflammatory clearance that intravesical BCG immunotherapy relies on."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Chronic inflammation drives the urothelium through STAT3: IL-6-fueled STAT3 signaling supports bladder-cancer cell survival and proliferation, tying the disease's strong inflammatory and smoking-related carcinogenesis to a targetable hub."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Pelvic cancer surgery clots the veins: bladder cancer's tumor-driven hypercoagulability, compounded by radical cystectomy — one of the highest-VTE-risk operations in oncology — makes thromboembolism a major perioperative hazard."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The urinary tract is a direct line to the blood: obstructing tumors, instrumentation and intravesical BCG can seed urosepsis, and rarely BCG itself disseminates into a systemic infection mimicking sepsis."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Blood in the urine drains the iron: painless hematuria is the cardinal sign of bladder cancer, and chronic or recurrent bleeding steadily depletes iron stores into an iron-deficiency anemia."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Obstruction and surgery threaten the kidneys: tumor at the ureteric orifices causes hydronephrosis, and radical cystectomy with urinary diversion alters renal drainage, together risking chronic kidney disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Cystectomy and a stoma reshape life: the loss of the bladder, a urinary diversion or stoma and the demands of intravesical therapy impose a heavy psychological burden, with high rates of depression."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its cisplatin chemo leaves nerves raw: the platinum-based regimens central to muscle-invasive bladder cancer cause a dose-limiting peripheral neuropathy with chronic neuropathic pain."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Bleeding tumor and chemo drain the blood: chronic hematuria, the inflammatory burden of the cancer and marrow-suppressing chemotherapy combine to produce anemia of chronic disease."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Chemotherapy opens the lung to mold: the neutropenia from cisplatin-based bladder-cancer chemotherapy can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Cystectomy and urinary diversion are major wounds: removing the bladder and building an ileal conduit or neobladder is extensive pelvic surgery whose anastomoses and wounds are prone to leak and slow healing."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It borrows the bowel and irradiates it: urinary diversion is fashioned from a segment of intestine, risking metabolic and bowel complications, while pelvic radiation for bladder cancer inflames the gut into radiation enteritis."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Frequent cystoscopy surveillance breeds worry: the high recurrence rate and lifelong surveillance cystoscopies of bladder cancer, plus living with a stoma, foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Pelvic nodes decide its stage: lymph-node involvement is a key prognostic factor in bladder cancer, so pelvic lymphadenectomy accompanies radical cystectomy."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It spreads to bone: the skeleton is a common site of distant metastasis in advanced bladder cancer, causing painful osteolytic lesions and pathological fractures."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can reach the brain and pelvic nerves: advanced bladder cancer occasionally metastasises to the brain, and pelvic tumour or radical surgery can injure nerves controlling continence and sexual function."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It shares its main cause with lung cancer: smoking is the leading risk factor for bladder cancer, and advanced disease metastasises to the lungs."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Treatment burdens the heart: cisplatin-based chemotherapy for muscle-invasive bladder cancer carries cardiovascular and thromboembolic risk, compounding the smoking-related vascular disease these patients often have."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It rarely reaches the skin: cutaneous metastases are an uncommon, late sign, and intravesical BCG immunotherapy can trigger systemic and skin hypersensitivity reactions."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy treats advanced disease: PD-1/PD-L1 inhibitors such as pembrolizumab, with avelumab maintenance, are central to advanced and BCG-unresponsive bladder cancer, which is highly mutated and immunogenic."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Molecular alterations open drug options: erdafitinib targets FGFR3-altered tumours, and antibody-drug conjugates like enfortumab vedotin (Nectin-4) and anti-HER2 agents extend treatment."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Platinum remains the backbone: cisplatin-based chemotherapy, given before cystectomy or for metastatic disease, is the long-standing foundation of bladder cancer treatment."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Lynch links them: mismatch-repair-deficient Lynch syndrome raises the risk of both endometrial and urothelial (bladder and upper-tract) cancers, and their MSI-high tumours share dramatic checkpoint-inhibitor responsiveness."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "A shared FGFR target: FGFR alterations drive a subset of both bladder cancer (FGFR3) and cholangiocarcinoma (FGFR2 fusions), so FGFR inhibitors like erdafitinib and pemigatinib treat these otherwise unrelated cancers."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Advanced disease seeds bone: muscle-invasive and metastatic urothelial carcinoma spreads to bone as painful osteolytic lesions, a common site of distant relapse after cystectomy."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Where it spreads: the lung is a common metastatic site for urothelial bladder cancer, tumour emboli lodging in the alveolar capillary bed to seed pulmonary nodules."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "The oldest cancer immunotherapy: intravesical BCG provokes a strong Th1 immune response in the bladder wall, recruiting lymphoid aggregates and germinal-centre reactions that clear early urothelial cancer."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Two smoking-driven cancers: tobacco carcinogens excreted in urine drive bladder cancer while the same smoking exposure is a leading risk factor for pancreatic cancer—shared chemical carcinogenesis."
---

# Bladder Cancer

## Overview

**Bladder cancer** is the most common malignancy of the urinary tract and the **fourth most common cancer in men** in the United States (~82,000 new cases and ~17,000 deaths annually). Approximately **90% are urothelial carcinoma (UC)**, arising from the urothelium lining the bladder; the remainder include squamous cell carcinoma (SCC), adenocarcinoma, and small cell/neuroendocrine carcinoma. The disease spans two biologically distinct entities: **non-muscle-invasive bladder cancer (NMIBC)** — highly recurrent but rarely lethal, and **muscle-invasive bladder cancer (MIBC)** — life-threatening with ~50% 5-year OS after radical cystectomy [^powles-2024-ev302].

**Incidence and risk factors:**
- **Smoking:** The dominant risk factor (~50% of bladder cancers attributable to tobacco); tobacco carcinogens (polycyclic aromatic hydrocarbons, aromatic amines) are excreted in urine → prolonged urothelial exposure; risk 2-4× vs. non-smokers; cessation reduces but does not eliminate risk
- **Occupational exposures:** Aromatic amines (benzidine, beta-naphthylamine) in dye, rubber, leather, paint, and hairdressing industries; latency period of 20-40 years; OSHA regulations have reduced but not eliminated occupational risk
- **Chronic bladder irritation:** Schistosoma haematobium infection → squamous cell carcinoma (endemic in sub-Saharan Africa and Egypt; ~50% of bladder cancers in high-prevalence regions are SCC)
- **Radiation:** Prior pelvic radiotherapy (cervical, prostate cancer) → increased bladder cancer risk (latency 10-20 years)
- **Cyclophosphamide:** Alkylating agent → acrolein (toxic metabolite) accumulates in urine → urothelial DNA damage; MESNA (2-mercaptoethane sulfonate) administered with cyclophosphamide to prevent urothelial acrolein exposure
- **Arsenic in drinking water:** Strong epidemiological association, particularly in areas with high well-water arsenic
- **Hereditary:** Lynch syndrome (*MLH1, MSH2* mutations) → ~5× lifetime bladder cancer risk; otherwise hereditary risk is rare and not well-defined

**Molecular subtypes:**

NMIBC and MIBC have distinct molecular landscapes:

*NMIBC molecular features:*
- **FGFR3 mutation (~60% of low-grade NMIBC):** FGFR3 S249C (most common), R248C, Y375C → constitutive homodimerization; FGFR3 mutation is a low-grade feature (inversely correlated with grade); FGFR3 and RAS/MAPK mutations are largely mutually exclusive
- **TERT promoter mutation (~75% of all UC):** C228T and C250T; the most frequent alteration across all stages; telomerase reactivation → cellular immortalization; detectable in urine → liquid biopsy potential
- **CCND1 amplification:** ~10-15% of NMIBC; cyclin D1 overexpression → CDK4/6-RB → E2F-driven proliferation

*MIBC molecular subtypes (TCGA 2017):*
- **Luminal papillary (35%):** FGFR3 fusions, FGFR3/ERB-B2 alterations; Wnt pathway active; best prognosis; responds to FGFR inhibitors and anti-PD-L1 (though lower TIL density)
- **Luminal unstable (5%):** RB1 alterations, highly genomically unstable; intermediate
- **Luminal non-specified (6%):** High immune infiltration
- **Stroma-rich (15%):** PDGFRA/DGK signatures; smooth muscle and stroma dominant; resistant to chemotherapy and immunotherapy
- **Basal/squamous (35%):** TP53 + RB1 co-deletion; high squamous differentiation; high PD-L1; high TIL; high cisplatin sensitivity; responds well to neoadjuvant chemotherapy
- **Neuronal (5%):** Neuroendocrine features; SCLC-like; worst prognosis; platinum + etoposide

**Key somatic alterations in MIBC (TCGA):**
- *TERT* promoter: ~75%
- *TP53*: ~48%
- *KDM6A*: ~26% (lysine demethylase; chromatin regulator; the most common tumor suppressor in UC after TP53)
- *FGFR3* (mutation + fusion): ~20%
- *RB1*: ~20%
- *CDKN2A*: ~31% (homozygous deletion)
- *ERBB2 (HER2)*: ~11% amplification; ~6% mutation
- *PIK3CA*: ~22%
- *MLL2/KMT2D*: ~27%
- *ARID1A*: ~25%

## Structure

### Bladder anatomy and urothelial biology

**Bladder anatomy:**
- Hollow muscular organ (~500 mL capacity) in the pelvis; collects and stores urine from the ureters; three layers: **urothelium** (transitional epithelium, the target of UC), **lamina propria** (vascular/connective tissue; muscularis mucosae — a thin muscle layer used for staging), **muscularis propria (detrusor muscle)** — invasion of detrusor = muscle-invasive
- **Trigone:** Base of bladder; ureteral orifices and urethral opening; cancers here are common (intersection of urine flow); proximal ureter/UPJ may be involved

**Urothelium histology:**
- 3-7 cell layers; **umbrella cells** (superficial; binucleated; glycocalyx-rich); **intermediate cells**; **basal cells** (stem cell compartment; KRT5+/KRT14+/TP63+)
- **Urothelial differentiation markers:** FOXA1, GATA3 (transcription factors); uroplakins (UPKI/II/III) → tight junctions and impermeability; cytokeratin 20 (KRT20) — luminal marker
- **Carcinogenesis:** Two parallel pathways: (1) FGFR3-activated → papillary low-grade NMIBC (high recurrence, low invasion risk); (2) TP53/RB1-disrupted → flat high-grade CIS → MIBC (high invasion, poor prognosis)

**Staging (TNM, 8th edition):**
- **Ta:** Non-invasive papillary (urothelium only); NMIBC
- **Tis (CIS):** Flat high-grade carcinoma in situ; not papillary; NMIBC but aggressive
- **T1:** Invades lamina propria (not muscularis propria); NMIBC
- **T2:** Invades muscularis propria (inner T2a, outer T2b); MIBC — key threshold
- **T3:** Perivesical fat (T3a microscopic, T3b macroscopic); MIBC
- **T4:** Adjacent organ invasion (T4a prostate/uterus/vagina; T4b pelvic/abdominal wall)
- **N:** Regional lymph nodes
- **M:** Distant metastasis

## Function

### Clinical presentation and diagnosis

**Presentation:**
- **Hematuria:** The hallmark of bladder cancer; gross (visible) or microscopic; painless gross hematuria requires cystoscopy; microscopic hematuria (≥3 RBC/HPF) in a patient >35 with risk factors → evaluation; hematuria is intermittent — a "negative" episode does not rule out cancer
- **Irritative symptoms (CIS):** Urgency, frequency, dysuria without UTI — classic presentation of bladder CIS (carcinoma in situ); often misdiagnosed as recurrent UTI; urine cytology → atypical or malignant cells → cystoscopy
- **Obstructive symptoms:** Ureteral involvement → hydronephrosis; urethral involvement → urinary retention; advanced MIBC/metastatic symptoms (flank pain, lower extremity edema from lymph node involvement)

**Diagnostic workup:**
- **Cystoscopy:** The definitive diagnostic tool; flexible cystoscopy (outpatient) → evaluate bladder mucosa; lesion identified → rigid cystoscopy under anesthesia → transurethral resection of bladder tumor (TURBT)
- **Urine cytology:** High sensitivity for high-grade UC and CIS (sensitivity ~70-80%); low sensitivity for low-grade papillary tumors (~20-30%); used for surveillance and initial evaluation; Paris System for Reporting Urinary Cytology standardizes reporting (atypical urothelial cells, SHGUC, HGUC, etc.)
- **Urine-based biomarkers:** FDA-approved tests (UroVysion FISH, NMP22, BTA test); NMP22 (nuclear matrix protein 22) — elevated in UC; none are sensitive enough to replace cystoscopy; urine TERT mutation PCR assay (clinical research) — high sensitivity/specificity for UC detection and surveillance
- **CT urography (CTU):** Contrast CT evaluating upper urinary tract + bladder; recommended for all new UC diagnosis to exclude upper tract UC (UTUC) — 5% of bladder UC patients have synchronous UTUC; also evaluates lymphadenopathy and metastases in MIBC

**TURBT (transurethral resection of bladder tumor):**
- Diagnostic and therapeutic for NMIBC; complete TURBT with muscularis propria in specimen critical (absence of muscularis propria → re-TURBT required); 2nd TURBT at 4-6 weeks for high-grade T1 disease to rule out understaging
- Histopathology: Grade (WHO 2004: low-grade/high-grade; or PUNLMP [papillary urothelial neoplasm of low malignant potential]), depth of invasion (Ta/Tis/T1/T2+), muscularis propria presence, lymphovascular invasion, variant histology (SCC, micropapillary, plasmacytoid, nested — all high-risk)

## Pathology

### Diagnosis and risk stratification (NMIBC)

**NMIBC risk stratification (EAU guidelines):**
- **Low risk:** Single, Ta, LG, <3 cm, no prior recurrence
- **Intermediate risk:** Ta/T1 LG, multifocal, >3 cm, or recurrence
- **High risk:** High-grade Ta/T1, CIS, T1HG with multiple/large/recurrent lesions, variant histology

**BCG (Bacillus Calmette-Guérin) immunotherapy for NMIBC:**
- Intravesical BCG (Connaught, TICE strains) is standard for intermediate-high risk NMIBC after TURBT; induction 6 weeks → maintenance (3-year schedule: 3 weeks at 3, 6, 12, 18, 24, 30, 36 months); BCG activates Th1 immune response → NK cells and CD8+ T cells → anti-urothelial immune surveillance
- BCG-unresponsive NMIBC (recurrence within 6 months of adequate BCG): **Pembrolizumab** (KEYNOTE-057: ORR 41%, CR 20% — FDA approved 2020); **nadofaragene firadenovec** (rAd-IFN/Syn3; intravesical adenovirus vector expressing IFN-alpha2b — FDA approved 2023 for BCG-unresponsive CIS); **nogapendekin alfa inbakicept** (IL-15 superagonist + pembrolizumab, LIO-1 trial — approved 2024 for BCG-unresponsive NMIBC)

### Treatment (MIBC and metastatic)

**Muscle-invasive bladder cancer (MIBC, T2-T4a) — localized:**
- **Neoadjuvant cisplatin-based chemotherapy (NAC) → radical cystectomy:** Standard for cisplatin-eligible MIBC; MVAC (methotrexate, vinblastine, doxorubicin, cisplatin) or GC (gemcitabine + cisplatin) → 5% absolute OS improvement (SWOG S8710); pathological complete response (pT0) is the strongest predictor of cure
- **Radical cystectomy:** Gold standard — cystoprostatectomy in men, anterior pelvic exenteration in women; extended lymph node dissection → ≥16 nodes; urinary diversion (ileal conduit or orthotopic neobladder); robotic-assisted increasingly used
- **Bladder preservation (TMT):** Trimodal therapy = maximal TURBT + concurrent chemoradiation (cisplatin or 5-FU + mitomycin + EBRT); for selected patients (unifocal T2, no CIS, complete TURBT, normal upper tracts); TMT-10 trial: 5-year OS ~57%; cystoscopy + biopsy to confirm complete response
- **Adjuvant nivolumab (CheckMate 274):** Pathological high-risk stage (pT3/T4 or pN+) after cystectomy; DFS benefit (HR 0.70); FDA approved 2021 for PD-L1 ≥1% and for cisplatin-ineligible patients regardless of PD-L1

**Metastatic urothelial carcinoma (mUC):**
- **First-line cisplatin-eligible:** Gemcitabine + cisplatin (GC; OS 14 months) OR dose-dense MVAC + G-CSF; **maintenance avelumab** after platinum-based chemotherapy (JAVELIN Bladder 100: OS benefit in PD-L1+ disease; FDA approved 2020) — now standard first-line approach after 4-6 cycles of GC
- **First-line enfortumab vedotin + pembrolizumab (EV-302) — NEW STANDARD [^powles-2024-ev302]:** Phase 3 trial in cisplatin-eligible and ineligible mUC; OS 31.5 vs. 16.1 months; PFS 12.5 vs. 6.3 months; ORR 67.7% vs. 44.4% vs. platinum + gemcitabine; FDA-approved December 2023; now the **preferred first-line regimen** for most patients with metastatic UC regardless of cisplatin eligibility or PD-L1 status
  - **Enfortumab vedotin (EV, Padcev):** Anti-Nectin-4 ADC; Nectin-4 is highly expressed on urothelial carcinoma; MMAE (monomethyl auristatin E) payload → microtubule disruption; hyperglycemia and peripheral neuropathy are key toxicities; skin rash (Nectin-4 expressed in skin)
- **Second-line pembrolizumab (KEYNOTE-045) [^bellmunt-2017-keynote045]:** OS 10.3 vs. 7.4 months vs. chemotherapy in post-platinum UC; FDA-approved 2017; now largely superseded by earlier pembrolizumab use in the EV-302 era
- **Erdafitinib (FGFR-altered mUC) [^loriot-2019-erdafitinib]:** Pan-FGFR1-4 inhibitor; THOR trial (2023): erdafitinib vs. pembrolizumab in FGFR3/2-altered cisplatin-pretreated UC → OS 12.1 vs. 7.8 months; FDA-approved; FGFR testing required (PCR or NGS for FGFR3 mutations/fusions, FGFR2 fusions)
- **Sacituzumab govitecan (Trodelvy):** Anti-Trop-2 ADC; SN-38 payload; TROPiCS-04 trial: OS benefit vs. chemotherapy in post-platinum/post-checkpoint mUC; FDA-approved
- **Cisplatin-ineligible first-line alternatives (pre-EV-302 era):** Carboplatin + gemcitabine; atezolizumab or pembrolizumab (accelerated approval withdrawn for PD-L1-unselected in 2021, retained for cisplatin-ineligible/PD-L1+ subsets)

**Upper tract urothelial carcinoma (UTUC):**
- Renal pelvis and ureter; managed with nephroureterectomy (gold standard); PYELOVAR trial: pemetrexed + cisplatin neoadjuvant for UTUC; adjuvant nivolumab (TCGA data) not yet standard; erdafitinib active (FGFR3 alterations in ~35% of UTUC)
- **Mitomycin C endoluminal delivery (Jelmyto):** FDA-approved 2020 for low-grade UTUC; novel silicone gel formulation allows prolonged upper tract contact

## Connections

- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGFR3 is mutated or fused in ~25-35% of urothelial carcinoma (S249C, FGFR3-TACC3 common); mutated FGFR3 drives proliferation and is enriched in low-grade NMIBC; erdafitinib (THOR trial: OS 12.1 vs. 7.8 months vs. pembrolizumab) is FDA-approved for FGFR-altered bladder cancer.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-L1 drives immune evasion in urothelial carcinoma; pembrolizumab improves OS vs. chemotherapy in post-platinum mUC (KEYNOTE-045: OS 10.3 vs. 7.4 months); enfortumab vedotin + pembrolizumab (EV-302) is now first-line standard for metastatic urothelial carcinoma.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutations (C228T/C250T) occur in ~75% of urothelial carcinoma — among the highest frequencies in any cancer; TERT mutation is one of the earliest carcinogenic events (present in dysplasia and NMIBC); urine TERT mutation detection enables non-invasive surveillance.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 loss occurs in ~20% of muscle-invasive bladder cancer (MIBC), co-occurring with TP53 mutation; RB1 deletion correlates with basal-squamous MIBC subtype and poor prognosis; RB pathway disruption also mediated by CDKN2A homozygous deletion in ~30% of MIBC.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 is mutated in ~48% of MIBC; co-deletion with RB1 defines the basal/squamous MIBC subtype (high PD-L1, cisplatin-sensitive); TERT promoter + TP53 mutations co-occur in high-grade UC; TP53 mutation in flat CIS is an early checkpoint failure enabling invasive progression.
- `connects-to` → **[Lynch Syndrome](../../07-system/lynch-syndrome/README.md)** — Lynch syndrome (germline MLH1/MSH2) confers ~5× lifetime bladder UC risk; dMMR bladder cancer (~3-4% of UC) has high TMB → pembrolizumab active regardless of PD-L1 (KEYNOTE-158); dMMR IHC/MSI-H testing recommended for early-onset or Lynch-suspected urothelial carcinoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A mutations in ~25% of MIBC; SWI/SNF chromatin remodeler; ARID1A LOF → impaired nucleosome remodeling at tumor suppressor promoters; co-mutated with TP53 and KDM6A; ARID1A-mutant MIBC may have synthetic lethality with EZH2 inhibition (tazemetostat combinations under study).
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Bladder cancer is one disease across the whole urinary-tract lining: the same urothelium covers the renal pelvis and ureters, so ~5% of bladder-cancer patients harbour synchronous upper-tract urothelial carcinoma, and a tumour obstructing a ureter causes hydronephrosis.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Bladder cancer pioneered immunotherapy: intravesical BCG provokes a Th1 response that recruits CD8+ cytotoxic T cells to patrol the urothelium and prevent recurrence of non-muscle-invasive disease — and the same T cells are reactivated by PD-1/PD-L1 checkpoint blockade.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Cervical and bladder cancer are linked through the pelvis: pelvic radiotherapy for cervical cancer is itself a risk factor for later bladder cancer, both are strongly smoking- or carcinogen-associated, and both are driven by insults delivered to a vulnerable epithelium.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Bladder and prostate cancers are the commonest genitourinary malignancies and frequent neighbors: they co-occur in older men, share smoking and age risk, and locally advanced disease of one can invade the other; pelvic surgery and shared follow-up imaging link their care.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Bladder cancer is a disease of the whole urothelial lining: the same field-effect carcinogens (smoking, aromatic amines) that transform the bladder can produce synchronous or metachronous tumors of the renal pelvis and ureter, so the entire upper urinary tract needs surveillance.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Bladder cancer is the birthplace of cancer immunotherapy: intravesical BCG—live attenuated mycobacteria—triggers a local immune response that has prevented recurrence of non-muscle-invasive bladder cancer for decades, and PD-1/PD-L1 inhibitors now treat advanced disease.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Bladder and renal cell carcinoma are the two major urologic cancers but differ in cell and cause: bladder cancer is a smoking-linked urothelial tumor with painless hematuria, while RCC arises from renal tubular epithelium—both can shed cells detectable in urine.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Bladder cancer and lung cancer are the paradigm smoking-caused epithelial cancers: tobacco carcinogens excreted in urine bathe and transform the bladder urothelium just as inhaled smoke transforms the bronchus, so the two often coexist and both are reshaped by immunotherapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Bladder cancer pioneered macrophage-based immunotherapy: intravesical BCG provokes a local immune response in which macrophages and T cells attack residual tumor, making early non-muscle-invasive bladder cancer one of the first cancers cured by harnessing innate immunity.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Invasion of the bladder's smooth muscle defines bladder cancer staging: whether the tumor breaches the muscularis propria (muscle-invasive vs non-muscle-invasive) drives management—cystectomy for muscle-invasive disease versus local therapy for superficial tumors.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — HER2 is an emerging target in bladder cancer: a subset of urothelial tumors overexpress HER2, and HER2-directed antibody-drug conjugates like trastuzumab deruxtecan show activity—extending the breast/gastric HER2 paradigm to bladder cancer therapy.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Bladder tumors depend on VEGF-driven angiogenesis: urothelial cancers secrete VEGF to grow new vessels, high VEGF predicts worse outcomes, and anti-angiogenic strategies are explored alongside chemotherapy and immunotherapy in advanced disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy enables bladder preservation in muscle-invasive bladder cancer: photon-beam chemoradiation as part of trimodality therapy can spare the bladder as an alternative to cystectomy in selected patients, controlling the tumor while keeping the organ.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion is common in bladder cancer: loss of this cell-cycle tumor-suppressor (often with FGFR3 or TP53 changes) helps drive urothelial proliferation, marking one of the genetic routes from carcinogen exposure to invasive disease.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Bladder and lung cancer share tobacco as a top cause: carcinogens excreted in urine bathe the urothelium just as inhaled smoke hits the airway, so the two smoking-driven cancers carry high mutation loads and both respond to PD-1 immunotherapy.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Bladder cancer is treated with a TB vaccine: intravesical BCG—live attenuated Mycobacterium bovis, the tuberculosis vaccine strain—instilled into the bladder triggers a local immune response that prevents recurrence of non-muscle-invasive tumors.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Bladder cancer is the classic occupational chemical cancer: carbon-based aromatic amines from dye, rubber, and leather industries are activated by the liver and concentrated in urine, where they mutate the urothelium—a link that founded industrial cancer epidemiology.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — BCG immunotherapy for bladder cancer works through dendritic cells: the mycobacteria are taken up by urothelial and antigen-presenting cells, activating dendritic cells that prime a tumor-killing immune response—innate immunity turned against cancer.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Bladder cancer often overexpresses EGFR-family receptors: urothelial tumors signal through EGFR and HER2 to grow, making the ErbB pathway a studied target alongside the FGFR inhibitors already used in this cancer.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — BCG immunotherapy for bladder cancer mobilizes NK cells: instilling live bacteria into the bladder triggers an innate immune assault in which natural killer cells help destroy superficial tumor cells, a decades-old immunotherapy that predates checkpoint drugs.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Bladder tumors recruit regulatory T cells to evade attack: Tregs accumulate in the bladder wall and suppress cytotoxic immunity, blunting both BCG and PD-1 checkpoint therapy and marking a target to make immunotherapy work better.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Bladder cancer's classic carcinogens are nitrogen-bearing aromatic amines: dyes, rubber and industrial chemicals excreted in urine bathe the bladder lining, which is why occupational aromatic-amine exposure is a textbook cause of the disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — BCG immunotherapy for bladder cancer works through NF-kB: the bacterial vaccine instilled in the bladder ignites NF-kB-driven inflammation that recruits immune cells to kill tumor cells, the oldest and still-used cancer immunotherapy.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils flood the bladder during BCG therapy: the instilled vaccine triggers an acute neutrophil-rich inflammation that helps clear superficial tumor cells, an innate-immune burst central to how this old immunotherapy works.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Bladder cancer spends the body's iron: painless blood in the urine is its cardinal sign, and the ongoing loss drains iron into a deficiency anemia that often prompts the workup that finds the tumor.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Bladder cancer favors the lungs when it spreads: the lung is among its commonest metastatic sites, so chest imaging is part of staging, and lung lesions often mark advanced, incurable disease.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Bladder cancer enlists fibroblasts to invade: cancer-associated fibroblasts in the tumor stroma secrete signals that drive the tumor through the bladder wall, the muscle invasion that separates lethal from curable disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Bladder cancer and its treatment scar the bladder: a desmoplastic tumor stroma and radiation-induced fibrosis stiffen the wall, shrinking capacity and complicating function after therapy.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Bladder cancer is vascular: VEGF recruits endothelial cells to feed the tumor, and the painless visible hematuria that first reveals it comes partly from these fragile new vessels bleeding into the urine.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Bladder cancer spreads to the liver: along with lung and bone, the liver is a common metastatic site, so its imaging is part of staging advanced, incurable disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads bladder cancer's lineage: urothelial carcinoma keeps the surface umbrella cells' specialized membrane plaques and tight junctions, while the squamous type from schistosomiasis shows desmosomes and keratin instead.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bladder cancer favors the skeleton when it spreads: bone is a leading metastatic site after lung and liver, and deposits in the marrow-filled vertebrae and pelvis cause the pain of advanced disease.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — An advanced bladder tumor can breach the bowel: invasion through the bladder wall into the adjacent rectum or sigmoid colon can open a vesicocolic fistula, leaking gas and stool into the urine.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Blood in the urine is the warning sign: painless hematuria — red cells shed into the urine by the friable tumor — is the cardinal presentation of bladder cancer, and chronic loss can leave the patient iron-deficient and anemic.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Engineered antibodies now treat bladder cancer: checkpoint inhibitors like pembrolizumab release the immune brakes, and the antibody-drug conjugate enfortumab vedotin delivers a toxin to nectin-4 on the tumor cells.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The platinum chemotherapy frays the nerves: cisplatin, the backbone of bladder cancer regimens, injures peripheral sensory neurons and the cochlear nerve, leaving numbness and hearing loss that can outlast treatment.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Bladder cancer is treated with a live mycobacterium: intravesical BCG — the attenuated M. bovis strain kin to the TB bacillus — is the standard adjuvant for high-risk non-muscle-invasive disease, igniting a Th1 response that clears tumor cells and can resemble disseminated TB.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Radical cystectomy reaches the reproductive organs: removing the bladder for muscle-invasive cancer usually takes the prostate and seminal vesicles in men, or the uterus and ovaries in women, costing fertility and sexual function alongside urinary diversion.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Bladder cancer drives a clotting state: paraneoplastic thrombocytosis is common and marks worse prognosis, and the tumor's pro-coagulant milieu raises the risk of venous thromboembolism that complicates surgery and chemotherapy.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K signaling is a core bladder-cancer driver: PIK3CA mutations are among the commonest in luminal urothelial tumors, switching on the AKT-mTOR growth pathway and marking a targetable vulnerability.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells gathered in the tumor predict response: tertiary lymphoid structures rich in B cells within bladder tumors forecast better outcomes with immune-checkpoint therapy, a sign the local antibody response matters.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — Smoking sows cancer across many linings: bladder and head-and-neck squamous cancers share tobacco and carcinogen exposure, so a field-cancerized patient with one carries a raised risk of the other.
- `connects-to` → **[COPD](../copd/README.md)** — The same smoke that scars the lungs lines the bladder: most bladder-cancer patients are smokers and carry COPD as a comorbidity, which raises the anesthetic and surgical risk of the cystectomy their cancer demands.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Lynch syndrome ties bladder to bowel: the mismatch-repair defect that drives colorectal cancer also raises the risk of upper-tract and bladder urothelial cancer, so a Lynch family history changes urologic surveillance.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The urinary microbiome shapes the response: the bladder is not sterile, and its microbial community influences both carcinogenesis and the inflammatory clearance that intravesical BCG immunotherapy relies on.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Chronic inflammation drives the urothelium through STAT3: IL-6-fueled STAT3 signaling supports bladder-cancer cell survival and proliferation, tying the disease's strong inflammatory and smoking-related carcinogenesis to a targetable hub.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Pelvic cancer surgery clots the veins: bladder cancer's tumor-driven hypercoagulability, compounded by radical cystectomy — one of the highest-VTE-risk operations in oncology — makes thromboembolism a major perioperative hazard.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The urinary tract is a direct line to the blood: obstructing tumors, instrumentation and intravesical BCG can seed urosepsis, and rarely BCG itself disseminates into a systemic infection mimicking sepsis.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Blood in the urine drains the iron: painless hematuria is the cardinal sign of bladder cancer, and chronic or recurrent bleeding steadily depletes iron stores into an iron-deficiency anemia.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Obstruction and surgery threaten the kidneys: tumor at the ureteric orifices causes hydronephrosis, and radical cystectomy with urinary diversion alters renal drainage, together risking chronic kidney disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Cystectomy and a stoma reshape life: the loss of the bladder, a urinary diversion or stoma and the demands of intravesical therapy impose a heavy psychological burden, with high rates of depression.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its cisplatin chemo leaves nerves raw: the platinum-based regimens central to muscle-invasive bladder cancer cause a dose-limiting peripheral neuropathy with chronic neuropathic pain.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Bleeding tumor and chemo drain the blood: chronic hematuria, the inflammatory burden of the cancer and marrow-suppressing chemotherapy combine to produce anemia of chronic disease.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Chemotherapy opens the lung to mold: the neutropenia from cisplatin-based bladder-cancer chemotherapy can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Cystectomy and urinary diversion are major wounds: removing the bladder and building an ileal conduit or neobladder is extensive pelvic surgery whose anastomoses and wounds are prone to leak and slow healing.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It borrows the bowel and irradiates it: urinary diversion is fashioned from a segment of intestine, risking metabolic and bowel complications, while pelvic radiation for bladder cancer inflames the gut into radiation enteritis.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Frequent cystoscopy surveillance breeds worry: the high recurrence rate and lifelong surveillance cystoscopies of bladder cancer, plus living with a stoma, foster chronic health anxiety alongside depression.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Pelvic nodes decide its stage: lymph-node involvement is a key prognostic factor in bladder cancer, so pelvic lymphadenectomy accompanies radical cystectomy.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It spreads to bone: the skeleton is a common site of distant metastasis in advanced bladder cancer, causing painful osteolytic lesions and pathological fractures.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can reach the brain and pelvic nerves: advanced bladder cancer occasionally metastasises to the brain, and pelvic tumour or radical surgery can injure nerves controlling continence and sexual function.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It shares its main cause with lung cancer: smoking is the leading risk factor for bladder cancer, and advanced disease metastasises to the lungs.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Treatment burdens the heart: cisplatin-based chemotherapy for muscle-invasive bladder cancer carries cardiovascular and thromboembolic risk, compounding the smoking-related vascular disease these patients often have.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It rarely reaches the skin: cutaneous metastases are an uncommon, late sign, and intravesical BCG immunotherapy can trigger systemic and skin hypersensitivity reactions.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy treats advanced disease: PD-1/PD-L1 inhibitors such as pembrolizumab, with avelumab maintenance, are central to advanced and BCG-unresponsive bladder cancer, which is highly mutated and immunogenic.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Molecular alterations open drug options: erdafitinib targets FGFR3-altered tumours, and antibody-drug conjugates like enfortumab vedotin (Nectin-4) and anti-HER2 agents extend treatment.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Platinum remains the backbone: cisplatin-based chemotherapy, given before cystectomy or for metastatic disease, is the long-standing foundation of bladder cancer treatment.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Lynch links them: mismatch-repair-deficient Lynch syndrome raises the risk of both endometrial and urothelial (bladder and upper-tract) cancers, and their MSI-high tumours share dramatic checkpoint-inhibitor responsiveness.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — A shared FGFR target: FGFR alterations drive a subset of both bladder cancer (FGFR3) and cholangiocarcinoma (FGFR2 fusions), so FGFR inhibitors like erdafitinib and pemigatinib treat these otherwise unrelated cancers.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Advanced disease seeds bone: muscle-invasive and metastatic urothelial carcinoma spreads to bone as painful osteolytic lesions, a common site of distant relapse after cystectomy.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Where it spreads: the lung is a common metastatic site for urothelial bladder cancer, tumour emboli lodging in the alveolar capillary bed to seed pulmonary nodules.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — The oldest cancer immunotherapy: intravesical BCG provokes a strong Th1 immune response in the bladder wall, recruiting lymphoid aggregates and germinal-centre reactions that clear early urothelial cancer.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Two smoking-driven cancers: tobacco carcinogens excreted in urine drive bladder cancer while the same smoking exposure is a leading risk factor for pancreatic cancer—shared chemical carcinogenesis.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^bellmunt-2017-keynote045]: Bellmunt J, de Wit R, Vaughn DJ, et al. Pembrolizumab as second-line therapy for advanced urothelial carcinoma. *N Engl J Med.* 2017;376(11):1015-1026. [doi:10.1056/NEJMoa1613683](https://doi.org/10.1056/NEJMoa1613683) · [PubMed 28212060](https://pubmed.ncbi.nlm.nih.gov/28212060/)
[^powles-2024-ev302]: Powles T, Valderrama BP, Gupta S, et al. Enfortumab vedotin and pembrolizumab in untreated advanced urothelial cancer. *N Engl J Med.* 2024;390(10):875-888. [doi:10.1056/NEJMoa2312117](https://doi.org/10.1056/NEJMoa2312117) · [PubMed 38261487](https://pubmed.ncbi.nlm.nih.gov/38261487/)
[^loriot-2019-erdafitinib]: Loriot Y, Necchi A, Park SH, et al. Erdafitinib in locally advanced or metastatic urothelial carcinoma. *N Engl J Med.* 2019;381(4):338-348. [doi:10.1056/NEJMoa1817323](https://doi.org/10.1056/NEJMoa1817323) · [PubMed 31340094](https://pubmed.ncbi.nlm.nih.gov/31340094/)
