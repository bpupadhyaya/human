---
schema: human-scale-entry/v1
id: melanoma
name: Melanoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Skin cancer from melanocytes; BRAF V600E (50%) and NRAS Q61 (25%) are dominant drivers. Dual checkpoint blockade (nivolumab + ipilimumab) and BRAF+MEK inhibitors (dabrafenib+trametinib) each achieve ~50-60% responses; 5-year OS ~50% in the immunotherapy era."
aliases: ["cutaneous melanoma", "malignant melanoma", "uveal melanoma", "acral melanoma", "mucosal melanoma", "BRAF-mutant melanoma", "metastatic melanoma"]
sources:
  - id: larkin-2015-checkmate067
    type: peer-reviewed
    cite: "Larkin J, Chiarion-Sileni V, Gonzalez R, et al. Combined nivolumab and ipilimumab or monotherapy in untreated melanoma. N Engl J Med. 2015;373(1):23-34."
    doi: "10.1056/NEJMoa1504030"
    pmid: "26027431"
    url: "https://doi.org/10.1056/NEJMoa1504030"
  - id: robert-2015-combi-v
    type: peer-reviewed
    cite: "Robert C, Karaszewska B, Schachter J, et al. Improved overall survival in melanoma with combined dabrafenib and trametinib. N Engl J Med. 2015;372(1):30-39."
    doi: "10.1056/NEJMoa1412690"
    pmid: "25399551"
    url: "https://doi.org/10.1056/NEJMoa1412390"
  - id: wolchok-2022-checkmate067-7yr
    type: peer-reviewed
    cite: "Wolchok JD, Chiarion-Sileni V, Gonzalez R, et al. Long-term outcomes with nivolumab plus ipilimumab or nivolumab alone versus ipilimumab in patients with advanced melanoma. J Clin Oncol. 2022;40(2):127-137."
    doi: "10.1200/JCO.21.02229"
    pmid: "34958258"
    url: "https://doi.org/10.1200/JCO.21.02229"
cross_links:
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E occurs in ~50% of melanoma; vemurafenib + cobimetinib and dabrafenib + trametinib achieve ~68-70% ORR in BRAF V600E metastatic melanoma; COMBI-D 5-year OS 34%; acquired resistance via NRAS/MEK mutations; combination prevents paradoxical ERK reactivation."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 blockade transformed advanced melanoma: pembrolizumab and nivolumab achieve 40-45% ORR; 5-year OS 44% with nivolumab monotherapy (CheckMate-003); immunotherapy is preferred over BRAF+MEK for asymptomatic disease due to durable responses and long-term survival plateau."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Ipilimumab was the first checkpoint inhibitor approved for advanced melanoma (2011); nivolumab + ipilimumab (CheckMate-067): 7-year OS 49% vs. 44% nivolumab vs. 21% ipilimumab — dual blockade delivers most durable benefit despite highest toxicity (~55% grade 3-4 irAEs)."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss occurs in ~20-30% of melanoma; PTEN loss → constitutive AKT → BRAF inhibitor resistance (alternative survival pathway); PTEN-null melanomas are relatively resistant to vemurafenib; combined BRAF + AKT inhibition is proposed for PTEN-null/BRAF V600E melanoma."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Tumor microenvironment generates adenosine via CD39 (ATP→AMP) and CD73 (AMP→adenosine); A2AR on tumor-infiltrating T cells → ↑cAMP → ↓IL-2/IFN-γ → immune evasion; anti-CD73 (oleclumab) + anti-PD-1 combination trials target adenosine-mediated immune checkpoint resistance."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Melanoma evades perforin-mediated CTL/NK cytotoxicity via MHC-I downregulation, PD-L1 upregulation, and IDO-mediated T-cell suppression; checkpoint inhibitors (anti-PD-1/CTLA-4) restore perforin-granzyme killing; TIL perforin content predicts immunotherapy response."
  - target: 01-human/01-subatomic/photon
    relation: damaged-by
    note: "UV-B and UV-A photons are the primary environmental mutagen in melanoma; CPDs and 8-oxoguanine → C→T and CC→TT signature mutations in BRAF (V600E in ~50%), NRAS, and TP53; melanoma has the highest UV mutational burden of any cancer (~10 mutations/Mb)."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Melanoma and non-small-cell lung cancer are the two flagships of cancer immunotherapy: both carry high UV- or tobacco-driven mutational burdens generating neoantigens, making them the most checkpoint-responsive solid tumors (PD-1/CTLA-4); both also harbor targetable BRAF V600E."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Cutaneous melanoma arises from melanocytes in the basal epidermis transformed by UV-induced mutations (BRAF, NRAS); unlike basal or squamous cell carcinoma it metastasizes early via lymphatics and blood — the deadliest skin cancer, where Breslow thickness drives prognosis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Melanoma is the founding model of T-cell immunotherapy: its heavy neoantigen load draws tumor-infiltrating cytotoxic CD8+ T cells whose reactivation by anti-PD-1/CTLA-4 (or adoptive TIL therapy) produces durable remissions — the proof of concept that launched the checkpoint era."
  - target: 01-human/07-system/uveal-melanoma
    relation: connects-to
    note: "Cutaneous and uveal melanoma share a melanocytic origin but are otherwise different: cutaneous is UV-driven with BRAF mutations and high mutational burden responsive to immunotherapy, while uveal has GNAQ/GNA11 mutations, liver tropism and poor checkpoint response."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Melanoma is the paradigm immunogenic cancer: its high UV-mutation neoantigen load made it the disease where checkpoint blockade (anti-CTLA-4 ipilimumab, anti-PD-1 nivolumab) first transformed survival, and spontaneous regressions and vitiligo show the immune system recognizes it."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain is a frequent and dangerous melanoma metastatic site: melanoma has a particular tropism for the CNS, so brain metastases are common and historically grim, but combined checkpoint inhibitors and stereotactic radiosurgery now achieve meaningful intracranial responses."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Melanoma spreads through the lymphatic system: tumor cells travel skin lymphatics, seeding 'in-transit' deposits and regional nodes, so sentinel-node status is the strongest prognostic factor—and the shift away from complete node dissection spares patients lymphedema."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "Melanoma and basal cell carcinoma are the deadliest and commonest skin cancers: both are UV-driven, but melanoma arises from melanocytes and metastasizes readily, while BCC arises from basal keratinocytes and almost never spreads—lethality versus indolence."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A is the major familial melanoma gene: germline loss of this tumor suppressor (p16INK4a, which restrains CDK4/6) causes familial atypical multiple mole melanoma syndrome, and somatic CDKN2A loss is common in sporadic melanoma—uniting inherited and acquired disease."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help control melanoma: they kill tumor cells that downregulate MHC to escape T cells, complementing the cytotoxic T-cell response—so melanoma immunotherapy increasingly aims to engage NK as well as T cells against the tumor."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a frequent melanoma metastatic site, especially in uveal melanoma: cutaneous melanoma spreads widely but ocular melanoma homes almost exclusively to the liver, so liver imaging dominates surveillance and liver-directed therapy is often needed."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1 loss defines a third melanoma genomic subtype beyond BRAF and NRAS: inactivating NF1 mutations drive MAPK signaling in often heavily UV-mutated tumors, so the BRAF/NRAS/NF1 triad classifies melanomas and shapes which targeted or immune therapy fits."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Melanoma is the deadliest cancer of the integumentary system: arising from pigment-making melanocytes, it can metastasize early despite small size, so the skin's most dangerous tumor is caught by watching moles for change (the ABCDE signs)."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Melanoma also arises in the eye: uveal melanoma develops from melanocytes of the choroid, and rare mucosal and other non-cutaneous melanomas show that the cancer can start wherever melanocytes reside, not only sun-exposed skin."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Melanoma has a notorious tropism for the nervous system: it is among the cancers most likely to spread to the brain, and leptomeningeal disease is feared—so CNS imaging is routine, and checkpoint immunotherapy has improved control of melanoma brain metastases."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "KIT drives the melanomas that aren't sun-driven: acral and mucosal melanomas often carry activating KIT mutations rather than BRAF, so testing KIT opens treatment with imatinib and other KIT inhibitors in these distinct subtypes."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells underlie melanoma immunotherapy: they capture tumor antigens and prime the cytotoxic T cells that checkpoint inhibitors unleash, and loading them with melanoma antigens is the basis of dendritic-cell vaccines tested against the disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Melanoma escapes targeted therapy through AKT: PTEN loss switches on the PI3K-AKT survival pathway, fueling growth and resistance to BRAF/MEK inhibitors, so AKT-pathway blockade is studied to deepen and prolong responses."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Melanoma's BRAF mutation drives the cell through ERK: BRAF feeds the MEK-ERK cascade that powers proliferation, so MEK inhibitors are paired with BRAF inhibitors—and ERK reactivation is a common route to drug resistance."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Melanoma shields itself with regulatory T cells: Tregs accumulate in the tumor and suppress the cytotoxic response, which is why CTLA-4 blockade (ipilimumab) that depletes or disables them helps unleash anti-melanoma immunity."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages help melanoma spread: M2-polarized macrophages secrete factors that suppress immunity and promote invasion and angiogenesis, making them both a marker of poor prognosis and a therapeutic target."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Melanoma is born from oxygen's reaction to UV: sunlight drives reactive oxygen species and DNA-damaging photochemistry in pigment cells, so ultraviolet oxidative injury, with direct mutation, is the root cause of most melanomas."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Melanoma spreads readily to the lungs: among the most metastatic of cancers, it seeds pulmonary nodules through the blood, a common site of distant disease that shapes staging and the move to systemic therapy."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Melanoma recruits blood vessels with VEGF: the tumor releases this angiogenesis driver to feed its growth and spread, and VEGF signaling also helps it suppress local immunity, adding to its notoriously invasive behavior."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Melanoma's pigment is forged with copper: tyrosinase, the copper-dependent enzyme, builds the melanin that colors melanocytes and the tumors they spawn, so copper sits at the heart of the cell's identity."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Desmoplastic melanoma masquerades as fibrosis: this variant forms a firm, scar-like fibrous tumor that is easily mistaken for benign and tends to track along nerves, making it treacherous to diagnose."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Melanoma is the cancer that most loves the small bowel: it is the tumor most likely to metastasize to the small intestine, where deposits bleed or obstruct, sometimes years after the original lesion."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutations are the single most common genetic change in cutaneous melanoma: UV-induced point mutations switch telomerase back on, granting the cells the unlimited replication that drives progression and marking a worse prognosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy clinches amelanotic melanoma: when a pigmentless tumor defies routine stains, the beam reveals melanosomes and striated premelanosomes — membrane-bound organelles found only in melanocytic cells — settling the diagnosis."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal gland is a favored melanoma metastatic site: these tumors seed the adrenals so reliably that a new adrenal mass in a melanoma patient is treated as a metastasis until proven otherwise, and resection of isolated deposits can prolong survival."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Melanoma loves the heart more than any other cancer: it has the highest rate of cardiac metastasis, seeding the myocardium and pericardium with deposits that can disturb rhythm or fill the pericardial sac."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Melanoma reaches the skeleton: bone metastases riddle the marrow-bearing spine and pelvis in advanced disease, painful and prone to fracture, part of its notoriously wide metastatic spread."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The gut is classic melanoma territory: it is among the cancers most likely to metastasize to the stomach and bowel, where pigmented deposits bleed or obstruct, sometimes appearing years after the skin lesion."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both name and fight melanoma: SOX10, S100, HMB-45, and Melan-A stains identify amelanotic tumors on biopsy, while the monoclonal antibodies against PD-1 and CTLA-4 unleash the immune attack that has transformed advanced-melanoma survival."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Melanoma sits at the sun's double edge: the same UV that makes vitamin D in the skin also drives the cancer, yet low vitamin D levels track with thicker tumors and worse outcomes, so repletion is studied even as sun avoidance is urged."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The blood count carries a prognosis: a high neutrophil-to-lymphocyte ratio marks an inflammatory, immunosuppressive state that predicts poorer response to checkpoint immunotherapy in melanoma, a cheap clue read straight off a routine blood test."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Immunotherapy can turn on the thyroid: the checkpoint inhibitors that transformed melanoma treatment commonly trigger autoimmune thyroiditis, causing transient hyperthyroidism then lasting hypothyroidism — one of the most frequent immune-related side effects."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Melanoma is the tumor most apt to cross the placenta: in pregnancy it can spread to the placenta and rarely the fetus, and because it is hormonally responsive, its behavior and management in pregnant patients need special care."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets help melanoma spread: circulating tumor cells cloak themselves in platelets to hide from natural killer cells and to lodge in distant vessels, a partnership that aids metastasis and makes platelets a studied antimetastatic target."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Melanoma launched modern immunotherapy: high-dose IL-2 produced the first durable remissions by goading T cells to attack, the proof-of-concept that the immune system could clear metastatic melanoma and the forerunner of today's checkpoint and cell therapies."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Unleashing the immune system has a cost: checkpoint inhibitors used against melanoma can trigger autoimmune attack on the pancreas, causing new-onset type 1 diabetes as an immune-related adverse event — the flip side of releasing the brakes on T cells."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The tumor's stroma fights back for it: cancer-associated fibroblasts remodel the matrix and secrete growth factors that shield melanoma cells, a niche that blunts BRAF-targeted drugs and helps the tumor regrow after an initial response."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 helps melanoma hide from immunity: constitutive STAT3 signaling drives survival and an immunosuppressive microenvironment, dampening the antitumor response that checkpoint inhibitors try to restore."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Immunotherapy turns on the glands: checkpoint inhibitors for melanoma commonly cause endocrine immune-related adverse events — hypophysitis, thyroiditis, and adrenal insufficiency — that can be permanent and need hormone replacement."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells stock the melanoma stroma: they accumulate around the tumor and release angiogenic and matrix-remodeling mediators that support invasion and new-vessel growth in the microenvironment."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB drives melanoma's survival and immune escape: constitutive NF-κB signaling supports proliferation and an immunosuppressive microenvironment, one of the pathways behind resistance to targeted and immune therapy."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Advanced disease clots the veins: metastatic melanoma carries tumor-driven hypercoagulability, and the surgery and systemic therapy it requires further raise the risk of venous thromboembolism."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Immunotherapy and advanced disease open the door to infection: severe immune-related colitis treated with steroids, plus the burden of metastatic disease, leave melanoma patients vulnerable to serious infection and sepsis."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Its immunotherapy can ignite the immune system: the checkpoint inhibitors central to melanoma treatment can trigger immune-related adverse events and, occasionally, a cytokine-release-like storm of systemic inflammation."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "It seeds the brain and bleeds: melanoma is among the most brain-metastatic cancers, and its metastases are characteristically hemorrhagic, causing intracranial bleeding and stroke."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Its therapies and threat weigh on mood: historically interferon-α treatment caused depression, and the diagnosis, disfiguring surgery and metastatic threat of melanoma carry a substantial psychological burden."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its immunotherapy can inflame the heart: the checkpoint inhibitors central to melanoma treatment occasionally cause an immune-mediated myocarditis, a rare but often fatal route to acute heart failure."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Checkpoint immunotherapy can scar the kidneys: the PD-1 and CTLA-4 inhibitors used for advanced melanoma can provoke an immune-mediated interstitial nephritis that, if recurrent, leaves chronic kidney impairment."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Recurrence risk and skin surveillance breed worry: the threat of metastasis and the lifelong monitoring for new primaries in melanoma foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Checkpoint immunotherapy inflames the gut: the PD-1 and CTLA-4 inhibitors used for melanoma frequently cause immune-related colitis with severe diarrhoea and autoimmune hepatitis, the commonest serious irAEs."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads to and inflames the lungs: melanoma metastasises readily to the lungs, and checkpoint immunotherapy can cause an immune-mediated pneumonitis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its surgery is wide and node-sampling: melanoma is treated with wide local excision and sentinel-node biopsy or lymph-node dissection, leaving wounds and lymphatic disruption that heal slowly."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It favours the heart among metastases: melanoma is the tumour most likely to metastasise to the heart and pericardium, and its checkpoint-inhibitor therapy can cause life-threatening myocarditis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It spreads to bone and inflames joints: melanoma metastasises to the skeleton causing pain and fractures, and checkpoint-inhibitor immunotherapy can trigger inflammatory arthritis and myositis."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its immunotherapy can inflame the kidney: checkpoint inhibitors used for melanoma can cause immune-related interstitial nephritis with acute kidney injury."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It pioneered modern oncology drugs: melanoma is the prototype for both BRAF/MEK-targeted therapy and immune checkpoint blockade, transforming the outlook for advanced disease."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Inherited risk runs in some families: germline TP53 (Li-Fraumeni) and CDKN2A mutations raise melanoma risk, part of the hereditary predisposition behind a minority of cases."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "BRCA2 widens its reach: carriers of BRCA2 mutations have an increased melanoma risk, linking this skin cancer to the hereditary breast-ovarian cancer spectrum."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "The breakthrough that defined immunotherapy: ipilimumab (anti-CTLA-4) and anti-PD-1 antibodies transformed metastatic melanoma from rapidly fatal to often durably controlled, the disease where checkpoint blockade first proved itself."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "A surprising two-way link: melanoma and Parkinson's disease show a bidirectional epidemiological association, thought to reflect shared biology of melanin and neuromelanin in pigment-cell pathways."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo that history left behind: melanoma is notoriously chemoresistant, and dacarbazine-based chemotherapy has been largely abandoned in favour of immunotherapy and targeted drugs."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Lymphoid islands forecast its immunotherapy response: melanomas that contain tertiary lymphoid structures with germinal-centre-like B-cell aggregates respond better to checkpoint blockade, marking the cancer where immunotherapy first proved transformative."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "KIT links a skin cancer to a gut tumour: acral and mucosal melanomas often carry activating KIT mutations like gastrointestinal stromal tumours, so these melanoma subtypes can respond to the KIT inhibitor imatinib that defines GIST therapy."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "A shared BRAF driver: papillary thyroid cancer and melanoma both frequently harbour the BRAF V600E mutation, and BRAF/MEK inhibitors developed in melanoma are now used in BRAF-mutant thyroid cancer—one mutation across two organs."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "CDKN2A and the FAMMM syndrome: germline CDKN2A mutation causes familial atypical multiple mole melanoma, raising the risk of both melanoma and pancreatic cancer—one gene linking skin and pancreas."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Checkpoint myocarditis: the immune checkpoint inhibitors that revolutionised melanoma treatment can trigger a rare but often fatal autoimmune myocarditis of the myocardium, a feared immune-related adverse event."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver is a favoured metastatic site: melanoma—especially ocular melanoma—spreads to the liver, seeding the hepatic lobule, a pattern that dominates uveal melanoma's course."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Same mutation, different response: BRAF V600E drives both melanoma and a colorectal cancer subset, yet BRAF inhibitors alone work in melanoma but fail in colon cancer because EGFR feedback reactivates the pathway—a lesson in context-dependent oncogene targeting."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Immunotherapy's autoimmune cost: the checkpoint inhibitors that revolutionised melanoma treatment unleash an autoimmune colitis closely resembling inflammatory bowel disease, managed with the same steroids and anti-TNF biologics."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Seizures from brain spread: melanoma is among the cancers most prone to forming brain metastases, often haemorrhagic, making it a notable cause of secondary seizures and epilepsy in advanced disease."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Phenotype switch and immune escape: Wnt/β-catenin signalling controls melanoma phenotype switching and, when active, excludes T cells from the tumour—a driver of resistance to immunotherapy."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle amplification: CCND1 (cyclin D1) amplification, common in acral and mucosal melanoma, partners CDK4/6 to drive proliferation, supporting CDK4/6-inhibitor strategies."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Survival and resistance: PI3K-AKT-mTOR signalling from PTEN loss sustains melanoma survival and contributes to acquired resistance to BRAF/MEK-targeted therapy."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplified oncogene: MYC amplification drives the proliferation and metabolism of melanoma and is implicated in resistance to targeted therapy."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic invasion: HIF-1α stabilised in hypoxic melanoma drives angiogenesis, the invasive phenotype switch and metastasis to distant organs."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic driver: EZH2 is frequently activated in melanoma, silencing tumour-suppressor genes and promoting metastasis and immune evasion."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Immune response and resistance: an IFN-γ-driven T-cell signature predicts melanoma's response to checkpoint inhibitors, while loss of IFN-γ signalling (JAK/STAT) is a key route to immunotherapy resistance."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Immunosuppression and invasion: TGF-beta dampens anti-tumour immunity and drives the phenotype switch toward an invasive, mesenchymal melanoma state that resists therapy."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 draws tumour-associated macrophages into melanoma, building an immunosuppressive microenvironment that supports growth and metastasis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "UV-mutational immunogenicity: the high UV-driven mutational burden of melanoma generates cytosolic DNA and neoantigens that engage cGAS-STING — central to why melanoma is the paradigm immunotherapy-responsive cancer and the rationale for intratumoral STING agonists."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Widespread metastasis: the CXCL12-CXCR4 axis drives the broad metastatic spread of melanoma, including its notorious dissemination to the brain, the pattern that historically made advanced melanoma so lethal."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Targeted-therapy apoptosis: BRAF and MEK inhibitors kill melanoma cells by relieving the mutant-BRAF block on caspase-3-mediated apoptosis, the mechanism behind the rapid responses to targeted therapy in BRAF-mutant disease."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Melanocyte-lineage signalling: melanoma cells express the endothelin-B receptor inherited from their melanocyte origin, and EDNRB signalling promotes their proliferation, survival and invasion — a lineage-survival pathway being explored as a therapeutic target."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenetic reprogramming: DNA-methylation changes silence tumour-suppressor and antigen-presentation genes in melanoma, contributing to its plasticity and immune escape, and DNA-methyltransferase inhibitors are being combined with immunotherapy to re-sensitise resistant tumours."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Resistance signalling: IGF-1R signalling provides a survival and growth input that helps melanoma cells escape BRAF/MEK inhibition, a bypass pathway implicated in acquired resistance to targeted therapy."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle target: the CDK4/6-cyclin-D1 axis (cyclin-D1 mapped, with CDKN2A loss mapped) drives melanoma proliferation, a node combined with BRAF/MEK inhibition to deepen responses."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Resistance pathway: PI3K-AKT activation (PTEN, AKT and mTOR already mapped) is a major mechanism by which melanoma escapes BRAF/MEK inhibition, the rationale for combined pathway blockade."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS-driven subtype: NRAS mutation is the second-commonest melanoma driver after BRAF, activating the RAS-MAPK cascade (ERK1/2 mapped) in a subgroup that resists BRAF inhibitors."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Immunotherapy resistance: interferon-γ signalling through JAK-STAT (IFN-γ already mapped) drives the antitumour immune response in melanoma, and loss-of-function JAK1/2 mutations are a key mechanism of acquired resistance to checkpoint immunotherapy."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative defence: NRF2 antioxidant signalling counters the ultraviolet- and metabolism-derived oxidative stress of melanoma and contributes to its therapy resistance."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate microenvironment: UV-induced and TLR-MyD88-NF-κB innate signalling (NF-κB already mapped) shapes the inflammatory microenvironment that promotes melanoma initiation and progression."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes melanoma invasion, metastasis and immune evasion."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) drives immunosuppression and the invasive/metastatic phenotype switch in melanoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ-STAT1 signalling (IFN-γ mapped) shapes both the antitumour immune response and the adaptive immune resistance of melanoma to checkpoint therapy."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulation of the Wnt/β-catenin axis and of MITF shapes the proliferative-versus-invasive phenotype switch of melanoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by the BRAF-MAPK and PI3K-AKT axes, regulate the oxidative-stress balance and survival of melanoma cells."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "YAP1 activity drives the invasive, drug-tolerant phenotype and contributes to BRAF/MEK-inhibitor resistance in melanoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2 restrains p53-mediated apoptosis in melanoma, a survival axis often intact given melanoma's typically wild-type TP53."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from myeloid-derived suppressor cells shape the immunosuppressive premetastatic niche of melanoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling contributes to the invasion and metastatic dissemination of melanoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and BRAF-inhibitor resistance of melanoma cells."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation and immunotherapy response of melanoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic plasticity of melanoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of melanoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and immune-evasion signaling of melanoma."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the proliferation and phenotype-switching biology of melanoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of melanoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of melanoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of melanoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of melanoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of melanoma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin (SPP1) participates in the tumor microenvironment, invasion, and metastasis of melanoma, and is a recognized prognostic marker."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Neoantigen immunotherapy: melanoma's ultraviolet-driven high mutational burden (photon already mapped) yields abundant MHC-presented neoantigens, underlying its landmark responsiveness to checkpoint inhibitors (PD-1/CTLA-4 already mapped) and neoantigen vaccines."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Targeted-therapy resistance: an AXL-high dedifferentiated cell state drives resistance to BRAF/MEK inhibitors (BRAF already mapped) in melanoma, a phenotype-switching escape route beyond secondary genetic mutations."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Immunotherapy myocarditis: checkpoint inhibitors, the mainstay of melanoma therapy, can cause immune-mediated myocarditis, a rare but often fatal adverse event that troponin elevation helps detect early."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the melanoma microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), a mechanism of immune evasion and resistance to the checkpoint blockade central to its treatment."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Ultraviolet oxidative damage: ultraviolet light and the inflamed skin generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage (NRF2 already mapped) adds to the mutational burden driving cutaneous melanoma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 help: helper T cells polarised to Th1 (interferon-gamma and IL-2 already mapped) support the cytotoxic CD8 (already mapped) response against melanoma, part of the anti-tumour immunity that checkpoint blockade and vaccines amplify."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "UV and immunosuppression: ultraviolet-induced cyclooxygenase-2 and prostaglandin E2 promote the inflammation and local immunosuppression of photocarcinogenesis, part of the microenvironment that fosters melanoma and blunts anti-tumour immunity."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive microenvironment that checkpoint immunotherapy must overcome in melanoma."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF and endothelin-1 (already mapped) regulates the angiogenesis and vascular tone of melanoma, and it also modulates the melanocyte and immune biology of the tumour."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment that checkpoint immunotherapy must overcome in melanoma."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Ferroptosis vulnerability: the iron-dependent lipid peroxidation of ferroptosis is a vulnerability of the drug-tolerant, dedifferentiated melanoma cells (NRF2 already mapped), an emerging angle against treatment-resistant disease."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Melanocyte metals: zinc supports the melanocyte enzymes of melanogenesis and the skin's zinc-dependent function, part of the trace-metal biology of the melanocytes from which melanoma arises."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon adjuvant immunotherapy: interferon-α was the historical adjuvant immunotherapy of high-risk melanoma, and the type-I interferon signalling shapes the immunogenicity and the checkpoint (PD-1 already mapped) response of the tumour."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic-immune adipokine: leptin, part of the obesity-melanoma metabolic axis, modulates the tumour and the T-cell (already mapped) immune response of melanoma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Microenvironment adipokine: adiponectin, with leptin (already mapped), is part of the adipokine modulation of the melanoma microenvironment and the immunotherapy response."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Microenvironment adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the obesity-melanoma axis and the immunotherapy microenvironment."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the immunogenic melanoma, augmenting the checkpoint (PD-1 already mapped) immunotherapy."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil biomarker: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophilia associated with the favourable response to the melanoma checkpoint immunotherapy."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Tertiary lymphoid B-cell response: the plasma cells and B cells of the intratumoural tertiary lymphoid structures produce antibody (already mapped) and predict a favourable response to the checkpoint (PD-1 already mapped) immunotherapy of melanoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the melanoma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/AllergoOncology arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), is the antibody arm explored in the AllergoOncology anti-tumour response against melanoma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the intratumoural tertiary lymphoid structures whose presence predicts the response to the checkpoint (PD-1 already mapped) immunotherapy of melanoma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the inflammatory and immunosuppressive dimension of the melanoma microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling recruits and polarises the myeloid cells to an immunosuppressive phenotype in the melanoma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the melanoma cells recruit factor H to regulate the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) and evade the complement attack of the melanoma microenvironment."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-tumour antibodies (already mapped) within the melanoma microenvironment."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Tumour iron: transferrin, the iron carrier, supplies the iron demand of the proliferating melanoma cells, which overexpress the transferrin receptor."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Immune-polarisation alarmin: TSLP from keratinocytes and stromal cells skews the melanoma microenvironment toward Th2, suppressing the anti-tumour Th1 and NK-cell (already mapped) immunity and reducing the efficacy of the PD-1 (already mapped) checkpoint inhibitors."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Melanoma invasion stroma: periostin secreted by cancer-associated fibroblasts and TGF-β (already mapped) signalling promotes the stromal remodelling and integrin αV-mediated invasiveness of melanoma cells, facilitating the locoregional spread and metastasis of melanoma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell immunosuppression: histamine from the mast cells (already mapped) infiltrating melanoma stroma promotes VEGF (already mapped) angiogenesis and suppresses NK-cell cytotoxicity via H2 receptor signalling, contributing to the immune-evasion of melanoma."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Tumour vascular permeability: bradykinin, via B2 receptor, amplifies VEGF-driven (already mapped) angiogenesis and peritumoral oedema in melanoma; kinin-kallikrein activation enhances mast-cell (already mapped) and fibroblast (already mapped) stromal recruitment."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Tumour EPOR signalling: erythropoietin receptor (EPOR) on melanoma cells activates JAK2/STAT3 (already mapped) pro-survival signalling, promotes VEGF (already mapped) angiogenesis, and blunts the apoptotic response to checkpoint-inhibitor (already mapped) immunotherapy."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Oncostatic melatonin: melatonin, via MT1/MT2 receptors on melanoma cells, suppresses BRAF (already mapped) and VEGF-driven (already mapped) proliferation and invasion, reduces MMP activity and augments NK-cell (already mapped) cytotoxicity against melanoma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-melanoma axis: testosterone, via androgen receptor on melanoma cells and macrophages (already mapped), modulates BRAF/VEGF (both already mapped) proliferative signalling and contributes to the sex-dimorphic incidence and checkpoint-inhibitor response of melanoma."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Melanocyte 5-HT axis: serotonin from UV-induced tryptophan metabolism in melanocytes (already mapped) activates 5-HT2 receptors on melanoma cells and tumour-infiltrating lymphocytes (already mapped), modulating immune evasion and the BRAF (already mapped) proliferative cascade."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Tumour-promoting prolactin: prolactin, via PRL-R on melanoma cells and tumour-associated macrophages (already mapped), activates the JAK2/STAT3 (already mapped) pro-survival pathway and promotes the VEGF-driven (already mapped) angiogenesis and immune evasion of melanoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Melanoma oxytocin anti-tumour: oxytocin, via OXTR on tumour-associated macrophages (already mapped) and mast cells (already mapped), attenuates the NF-κB (already mapped) and VEGF (already mapped) pro-tumour cascade, reducing immune evasion and angiogenesis in melanoma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Melanoma vasopressin vascular: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the tumour vascular niche; dysregulation amplifies NF-κB (already mapped) and VEGF (already mapped) pro-tumour angiogenic signalling in melanoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Melanoma selenium antioxidant: selenium, via GPx/TrxR selenoproteins in melanoma cells and macrophages (already mapped), quenches ROS that amplifies BRAF (already mapped) and NF-κB (already mapped) proliferative signalling, reducing the oxidative-stress phenotype of melanoma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Melanoma iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive tumour cascade of melanoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Melanoma sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of melanoma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Melanoma magnesium: magnesium, as cofactor of antioxidant enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped), attenuates oxidative stress; magnesium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of melanoma."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Melanoma calcium: calcium signals in macrophages (already mapped) and mast cells (already mapped) regulate immune activation; calcium flux amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of melanoma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Melanoma potassium: potassium channels regulate macrophage (already mapped) and T-cytotoxic (already mapped) antitumour function; potassium depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of melanoma."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Melanoma phosphorus: phosphorus, as phospholipid and ATP in macrophages (already mapped) and mast cells (already mapped), supports antitumour signalling; phosphorus depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of melanoma."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Melanoma carbon: carbon as backbone of BRAF (already mapped) and MITF signalling proteins in melanocytes (already mapped) sustains proliferative control; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) oncogenic cascade of melanoma."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Melanoma chloride: chloride regulates melanocyte (already mapped) and macrophage (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) immunosuppressive tumour cascade of melanoma."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Melanoma nitrogen: nitrogen in amino-acid scaffold of BRAF (already mapped) and PD-L1 proteins modulates T-cell (already mapped) immune evasion; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of melanoma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Melanoma hydrogen: hydrogen in redox chemistry of melanocytes (already mapped) sustains glutathione defence against UV-driven oxidative stress; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of melanoma."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Melanoma sulfur: sulfur in cysteine residues of BRAF (already mapped) and MITF proteins sustains redox stability in melanocytes; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) oncogenic cascade of melanoma."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Melanoma GLP-1: GLP-1 signalling modulates macrophage (already mapped) and dendritic-cell (already mapped) activation in the tumour microenvironment; GLP-1 deficit amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) oncogenic cascade of melanoma."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Melanoma angiotensin-ii: angiotensin-II from macrophages (already mapped) and fibroblast (already mapped) drives tumour vascular remodelling; angiotensin-ii excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) cascade of melanoma."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Melanoma rankl: RANKL from macrophages (already mapped) and t-cytotoxic cells (already mapped) promotes melanoma immune evasion; rankl excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Melanoma fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) anchors tumour-invasive matrix; fibronectin dysregulation amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) cascade of melanoma."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Melanoma activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) drives tumour fibrotic remodelling; activin-a excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Melanoma cgrp: CGRP from fibroblasts (already mapped) and macrophages (already mapped) modulates melanoma vascular tone; cgrp excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Melanoma calcitonin: calcitonin from fibroblasts (already mapped) and macrophages (already mapped) modulates calcium signalling; calcitonin dysregulation amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Melanoma notch: NOTCH in fibroblasts (already mapped) and macrophages (already mapped) regulates melanoma cell fate; notch dysregulation amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Melanoma igf-1: IGF-1 from fibroblasts (already mapped) and macrophages (already mapped) promotes melanoma metabolic growth; igf-1 excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Melanoma tgf-beta: TGF-β from fibroblasts (already mapped) and macrophages (already mapped) drives melanoma immunosuppression; TGF-β excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Melanoma substance-p: substance-P from fibroblasts (already mapped) and macrophages (already mapped) modulates pain tone; substance-P excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Melanoma insulin-receptor: insulin-receptor on fibroblasts (already mapped) and macrophages (already mapped) modulates metabolic axis; insulin resistance amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Melanoma aldosterone: aldosterone from fibroblasts (already mapped) and macrophages (already mapped) modulates electrolyte tone; aldosterone excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma."
---

# Melanoma

## Overview

**Melanoma** is a malignant tumor arising from **melanocytes** — neural crest-derived cells that produce melanin pigment in the skin, uveal tract, mucous membranes, and meninges. While accounting for only ~5% of skin cancers, melanoma is responsible for ~75% of skin cancer deaths due to its high metastatic potential and historically poor prognosis in advanced stages. However, the discovery of **BRAF V600E** as a targetable oncogene (2002) and the development of **immune checkpoint inhibitors** (2011-present) have transformed metastatic melanoma from a disease with median OS of ~8 months to one where ~50% of patients are alive at 5 years with modern therapy [^larkin-2015-checkmate067].

**Melanoma subtypes (anatomical):**
- **Cutaneous melanoma (~90%):** Arising from skin melanocytes; further subdivided:
  - **Superficial spreading melanoma (SSM, ~70%):** Most common; horizontal growth phase → vertical (invasive); most strongly associated with UV exposure; BRAF V600E frequent
  - **Nodular melanoma (~15%):** Aggressive; no radial growth phase → rapid vertical invasion; often amelanotic (no pigment) → delayed diagnosis
  - **Lentigo maligna melanoma (LMM, ~10%):** In sun-damaged skin (head/neck, elderly); BRAF mutations less common; NF1 and triple wild-type more frequent
  - **Acral lentiginous melanoma (ALM, ~5%):** Palms, soles, nail beds; under-diagnosed in dark skin; no UV association; KIT mutations in ~30%; different treatment implications
- **Uveal (ocular) melanoma (~5%):** GNAQ/GNA11 mutations (in >90%) — not BRAF; BAP1 loss → high metastatic potential; hepatic metastasis predominant; different biology and treatment (KIT pathway unimportant; tebentafusp — bispecific targeting gp100 — FDA approved 2022)
- **Mucosal melanoma (~1%):** Anorectal, vulvovaginal, sinonasal; poor prognosis; KIT mutations (~25%); distinct from cutaneous; imatinib/sunitinib occasionally active in KIT-mutant mucosal melanoma
- **Meningeal (rare):** CNS-primary; associated with congenital melanocytic nevi and NRAS mutations

**Molecular genetic landscape of cutaneous melanoma:**
- **BRAF V600E/K (~50%):** Dominant oncogenic driver; V600E (~90% of BRAF mutations); constitutive BRAF kinase → MEK-ERK → proliferation; mutually exclusive with NRAS (but can co-occur with NF1 loss); targetable with BRAF inhibitors
- **NRAS Q61R/K/L (~25%):** RAS GTPase lock in GTP-bound → RAF-MEK-ERK; harder to target than BRAF; binimetinib (MEK inhibitor) modestly active; no direct NRAS inhibitors approved; NRAS-mutant melanoma has higher Ki-67, worse prognosis
- **NF1 loss (~15%):** NF1 = RAS-GAP; loss → RAS hyperactivation → MEK-ERK; MEK inhibitors (cobimetinib, binimetinib) have activity; "NF1 subtype" enriched in older patients, heavy UV damage
- **Triple wild-type (~10%):** Wild-type for BRAF, NRAS, NF1; KIT mutations, CDK4 amplification, CCND1 amplification; more heterogeneous; uncommon in superficial spreading; acral/mucosal subtypes overrepresented
- **Tumor mutational burden (TMB):** Cutaneous melanoma has among the highest TMB of all cancers (~17 mut/Mb median, up to 100+ in chronic sun-damaged melanoma) due to UV-induced C>T and CC>TT transitions — **UV mutational signature** (COSMIC SBS7a/7b); high TMB correlates with neoantigens → immunogenicity → checkpoint inhibitor response

## Structure

### UV carcinogenesis and melanocyte biology

**UV-induced melanocyte transformation:**
- UV-B (290-315 nm) → cyclobutane pyrimidine dimers (CPDs) and 6-4 photoproducts in melanocyte DNA → if misrepaired → C>T transitions at dipyrimidine sequences; CC>TT doublet mutations are UV-signature hallmarks; UV directly activates the BRAF pathway (short-term) and mutates BRAF, NRAS, TP53 (long-term carcinogenesis)
- **Melanocyte-specific biology:** Melanocytes express MC1R (melanocortin 1 receptor) → activated by alpha-MSH → cAMP → CREB → MITF (microphthalmia-associated transcription factor) → tyrosinase, DCT, TYRP1 → melanin synthesis; MITF is the "master regulator" of melanocyte identity; in melanoma, MITF switches from a differentiation factor to a proliferation/survival factor depending on expression level
- **Melanoma invasion:** Melanocytes are normally anchored by E-cadherin to keratinocytes; in melanoma, E-cadherin → N-cadherin switch → loss of keratinocyte anchor → invasion through dermis; MMP (matrix metalloproteinase) production → basement membrane degradation; VEGF → neoangiogenesis → hematogenous dissemination

**BRAF-MEK-ERK pathway in melanoma:**
- Normal melanocyte: UV → receptor activation → transient ERK activation → cell cycle entry → melanin synthesis
- BRAF V600E melanoma: Constitutive BRAF kinase activity (independent of RAS) → constitutive MEK-ERK → cyclin D1, MYC → proliferation; ERK → transcriptional activation of MITF → complex between proliferative and differentiating signals; BRAF V600E drives both proliferative advantage and some aspects of melanocyte identity (pigmentation) → melanoma retains some melanocytic gene expression

**Immune microenvironment:**
- Cutaneous melanoma has the highest TIL (tumor-infiltrating lymphocyte) density of most solid tumors; TILs — CD8+ T cells predominating — are recruited by CXCL9/10 (IFN-gamma-driven); PD-L1 expression on melanoma cells and macrophages → T cell exhaustion; checkpoint inhibitor response directly correlates with: TIL density, IFN-gamma signature, PD-L1 expression, and TMB
- **BRAF V600E → immune exclusion:** Vemurafenib-treated tumors show increased T cell infiltration within weeks (BRAF inhibition → MEK-ERK suppression → decreased immunosuppressive VEGF and IL-10 production → increased T cell access); this is why BRAF+MEK → immunotherapy sequencing or combinations are being explored

## Function

### Clinical presentation, staging, and surveillance

**ABCDE criteria (early detection):**
- **A**symmetry, **B**order irregularity, **C**olor variation (multiple hues), **D**iameter >6 mm, **E**volution (change over time); melanoma often presents as a new or changing pigmented lesion; clinician examination + dermoscopy → biopsy threshold

**Staging (AJCC 8th edition):**
- **Stage I-II:** Primary melanoma with/without ulceration and mitotic rate; 5-year OS >90% (Stage I) to 60-70% (Stage IIc)
- **Stage III:** Regional lymph node metastasis; subdivided by nodal burden (IIIA/B/C/D); 5-year OS 40-78%
- **Stage IV:** Distant metastasis; M1a (skin/subcutaneous/lymph node), M1b (lung), M1c (visceral), M1d (brain); 5-year OS 15-30% with modern therapy

**Sentinel lymph node biopsy (SLNB):**
- Recommended for melanomas ≥0.8 mm Breslow thickness (or 0.6-0.8 mm with ulceration); provides staging information (SLN positive → Stage III); completion lymph node dissection (CLND) no longer standard (DeCOG, MSLT-II trials); adjuvant therapy guided by SLN status

## Pathology

### Diagnosis

**Excisional biopsy** (preferred, 1-2 mm margins) with histopathology: Breslow thickness (depth in mm, most important prognostic factor), Clark level (anatomical level), ulceration, mitotic rate, satellitosis, lymphovascular invasion — all reported in standardized format.

**BRAF mutation testing:** Required before initiating targeted therapy; BRAF V600E/K testing by RT-PCR (cobas, THxID) or next-generation sequencing; extended BRAF/NRAS/NF1/KIT molecular profiling on metastatic disease for treatment planning.

### Treatment [^larkin-2015-checkmate067] [^robert-2015-combi-v]

**Early-stage (adjuvant therapy after resection of Stage III-IIA disease):**
- **Pembrolizumab adjuvant (KEYNOTE-716):** 18 months; reduces recurrence in Stage IIb-IIc (high-risk) and Stage III; 2-year RFS 83.4% vs. 77.1%
- **Nivolumab adjuvant (CheckMate-238):** vs. ipilimumab in Stage IIIB-IV; 5-year RFS 50% vs. 39%; OS benefit at 5 years
- **Dabrafenib + trametinib adjuvant (COMBI-AD):** For BRAF V600E/K Stage III; 5-year RFS 52% vs. 36% placebo; OS not significantly different from checkpoint inhibitor adjuvant in cross-trial comparison (no head-to-head data)

**Metastatic melanoma — immune checkpoint blockade:**
- **Nivolumab + ipilimumab (CheckMate-067):** 7-year OS 49% vs. 44% (nivo alone) vs. 21% (ipi alone); dual blockade achieves the deepest and most durable responses; recommended for symptomatic/rapid-progression/high-volume disease [^wolchok-2022-checkmate067-7yr]; grade 3-4 irAEs ~55% (discontinuation rate high)
- **Pembrolizumab monotherapy (KEYNOTE-006):** OS 38.7% at 5 years; 5-year PFS 21%; landmark data establishing checkpoint immunotherapy as a dominant first-line strategy
- **Relatlimab + nivolumab (Opdualag — anti-LAG-3 + anti-PD-1):** RELATIVITY-047: PFS 10.1 vs. 4.6 months vs. nivolumab; FDA approved 2022; less toxicity than nivo + ipi; LAG-3 is the third checkpoint after PD-1 and CTLA-4

**Metastatic melanoma — BRAF-targeted therapy:**
- **Dabrafenib + trametinib (COMBI-D/V):** ORR ~68%; median PFS ~12-15 months; 5-year OS 34% (COMBI-D); superior to BRAF inhibitor monotherapy; approved for BRAF V600E/K metastatic melanoma; preferred in rapidly progressive, high-burden, or LDH-elevated disease where rapid response needed [^robert-2015-combi-v]
- **Encorafenib + binimetinib (COLUMBUS):** PFS 14.9 months; OS 33.6 months; lower pyrexia than dabrafenib/trametinib; approved for BRAF V600E/K metastatic melanoma
- **Vemurafenib + cobimetinib (coBRIM):** PFS 12.3 months; first approved BRAF+MEK combination

**Resistance to BRAF+MEK inhibitors:**
- Acquired resistance after median 12-15 months; mechanisms: NRAS mutation (10-20%), MEK1/2 mutations (5-10%), BRAF V600E amplification (5-10%), BRAF splice variants, NF1 loss, PI3K activation (PTEN loss), MAP3K/COT1 → ERK reactivation; immunotherapy after BRAF+MEK failure (cross-resistance uncommon)

**Brain metastases:**
- ~40-50% of metastatic melanoma develop brain metastases; ipilimumab + nivolumab (CheckMate-204: intracranial ORR 57%); dabrafenib + trametinib (intracranial ORR 58% in BRAF V600E); SRS (stereotactic radiosurgery) for ≤4 lesions; whole-brain RT generally avoided (neurotoxicity); targeted + IO combinations under investigation for leptomeningeal disease

**Uveal melanoma:**
- **Tebentafusp (Kimmtrak):** First approved therapy for uveal melanoma (2022); bispecific T cell engager (TCE) targeting gp100 (melanocytic antigen) × CD3; requires HLA-A*02:01 (40% of patients); IMCgp100-202 trial: OS 73% vs. 59% at 1 year vs. investigator choice — first survival benefit in uveal melanoma; cytokine release syndrome manageable

## Connections

- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E occurs in ~50% of melanoma; vemurafenib + cobimetinib and dabrafenib + trametinib achieve ~68-70% ORR; COMBI-D 5-year OS 34%; acquired resistance via NRAS/MEK mutations; combination prevents paradoxical ERK reactivation from single-agent BRAF inhibition.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 blockade transformed advanced melanoma: pembrolizumab and nivolumab achieve 40-45% ORR; 5-year OS 44% with nivolumab; immunotherapy preferred for asymptomatic disease due to durable responses and long-term survival plateau not seen with BRAF+MEK.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Ipilimumab was the first checkpoint inhibitor approved in advanced melanoma (2011); nivolumab + ipilimumab (CheckMate-067): 7-year OS 49% vs. 21% ipilimumab — dual blockade delivers the most durable benefit despite highest toxicity (~55% grade 3-4 irAEs).
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss occurs in ~20-30% of melanoma → constitutive AKT → BRAF inhibitor resistance; PTEN-null melanomas are relatively resistant to vemurafenib; combined BRAF + AKT inhibition is proposed and under investigation for PTEN-null/BRAF V600E melanoma.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — tumor microenvironment generates adenosine via CD39 (ATP→AMP) and CD73 (AMP→adenosine) on melanoma cells and MDSCs; A2AR on tumor-infiltrating T cells → ↑cAMP → ↓IL-2/IFN-γ → immune evasion; anti-CD73 (oleclumab) + anti-PD-1 combination trials target adenosine-mediated immune checkpoint resistance.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Melanoma evades perforin-mediated CTL/NK cytotoxicity via MHC-I downregulation, PD-L1 upregulation, and IDO-mediated T-cell suppression; checkpoint inhibitors (anti-PD-1/CTLA-4) restore perforin-granzyme killing; TIL perforin content predicts immunotherapy response.
- `damaged-by` → **[Photon](../../01-subatomic/photon/README.md)** — UV-B and UV-A photons are the primary environmental mutagen in melanoma; CPDs and 8-oxoguanine → C→T and CC→TT signature mutations in BRAF (V600E in ~50%), NRAS, and TP53; melanoma has the highest UV mutational burden of any cancer (~10 mutations/Mb).
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Melanoma and non-small-cell lung cancer are the two flagships of cancer immunotherapy: both carry high UV- or tobacco-driven mutational burdens generating neoantigens, making them the most checkpoint-responsive solid tumors (PD-1/CTLA-4); both also harbor targetable BRAF V600E.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Cutaneous melanoma arises from melanocytes in the basal epidermis transformed by UV-induced mutations (BRAF, NRAS); unlike basal or squamous cell carcinoma it metastasizes early via lymphatics and blood — the deadliest skin cancer, where Breslow thickness drives prognosis.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Melanoma is the founding model of T-cell immunotherapy: its heavy neoantigen load draws tumor-infiltrating cytotoxic CD8+ T cells whose reactivation by anti-PD-1/CTLA-4 (or adoptive TIL therapy) produces durable remissions — the proof of concept that launched the checkpoint era.
- `connects-to` → **[Uveal Melanoma](../uveal-melanoma/README.md)** — Cutaneous and uveal melanoma share a melanocytic origin but are otherwise different: cutaneous is UV-driven with BRAF mutations and high mutational burden responsive to immunotherapy, while uveal has GNAQ/GNA11 mutations, liver tropism and poor checkpoint response.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Melanoma is the paradigm immunogenic cancer: its high UV-mutation neoantigen load made it the disease where checkpoint blockade (anti-CTLA-4 ipilimumab, anti-PD-1 nivolumab) first transformed survival, and spontaneous regressions and vitiligo show the immune system recognizes it.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain is a frequent and dangerous melanoma metastatic site: melanoma has a particular tropism for the CNS, so brain metastases are common and historically grim, but combined checkpoint inhibitors and stereotactic radiosurgery now achieve meaningful intracranial responses.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Melanoma spreads through the lymphatic system: tumor cells travel skin lymphatics, seeding 'in-transit' deposits and regional nodes, so sentinel-node status is the strongest prognostic factor—and the shift away from complete node dissection spares patients lymphedema.
- `connects-to` → **[Basal Cell Carcinoma](../basal-cell-carcinoma/README.md)** — Melanoma and basal cell carcinoma are the deadliest and commonest skin cancers: both are UV-driven, but melanoma arises from melanocytes and metastasizes readily, while BCC arises from basal keratinocytes and almost never spreads—lethality versus indolence.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A is the major familial melanoma gene: germline loss of this tumor suppressor (p16INK4a, which restrains CDK4/6) causes familial atypical multiple mole melanoma syndrome, and somatic CDKN2A loss is common in sporadic melanoma—uniting inherited and acquired disease.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help control melanoma: they kill tumor cells that downregulate MHC to escape T cells, complementing the cytotoxic T-cell response—so melanoma immunotherapy increasingly aims to engage NK as well as T cells against the tumor.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a frequent melanoma metastatic site, especially in uveal melanoma: cutaneous melanoma spreads widely but ocular melanoma homes almost exclusively to the liver, so liver imaging dominates surveillance and liver-directed therapy is often needed.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — NF1 loss defines a third melanoma genomic subtype beyond BRAF and NRAS: inactivating NF1 mutations drive MAPK signaling in often heavily UV-mutated tumors, so the BRAF/NRAS/NF1 triad classifies melanomas and shapes which targeted or immune therapy fits.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Melanoma is the deadliest cancer of the integumentary system: arising from pigment-making melanocytes, it can metastasize early despite small size, so the skin's most dangerous tumor is caught by watching moles for change (the ABCDE signs).
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Melanoma also arises in the eye: uveal melanoma develops from melanocytes of the choroid, and rare mucosal and other non-cutaneous melanomas show that the cancer can start wherever melanocytes reside, not only sun-exposed skin.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Melanoma has a notorious tropism for the nervous system: it is among the cancers most likely to spread to the brain, and leptomeningeal disease is feared—so CNS imaging is routine, and checkpoint immunotherapy has improved control of melanoma brain metastases.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT drives the melanomas that aren't sun-driven: acral and mucosal melanomas often carry activating KIT mutations rather than BRAF, so testing KIT opens treatment with imatinib and other KIT inhibitors in these distinct subtypes.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells underlie melanoma immunotherapy: they capture tumor antigens and prime the cytotoxic T cells that checkpoint inhibitors unleash, and loading them with melanoma antigens is the basis of dendritic-cell vaccines tested against the disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Melanoma escapes targeted therapy through AKT: PTEN loss switches on the PI3K-AKT survival pathway, fueling growth and resistance to BRAF/MEK inhibitors, so AKT-pathway blockade is studied to deepen and prolong responses.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Melanoma's BRAF mutation drives the cell through ERK: BRAF feeds the MEK-ERK cascade that powers proliferation, so MEK inhibitors are paired with BRAF inhibitors—and ERK reactivation is a common route to drug resistance.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Melanoma shields itself with regulatory T cells: Tregs accumulate in the tumor and suppress the cytotoxic response, which is why CTLA-4 blockade (ipilimumab) that depletes or disables them helps unleash anti-melanoma immunity.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages help melanoma spread: M2-polarized macrophages secrete factors that suppress immunity and promote invasion and angiogenesis, making them both a marker of poor prognosis and a therapeutic target.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Melanoma is born from oxygen's reaction to UV: sunlight drives reactive oxygen species and DNA-damaging photochemistry in pigment cells, so ultraviolet oxidative injury, with direct mutation, is the root cause of most melanomas.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Melanoma spreads readily to the lungs: among the most metastatic of cancers, it seeds pulmonary nodules through the blood, a common site of distant disease that shapes staging and the move to systemic therapy.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Melanoma recruits blood vessels with VEGF: the tumor releases this angiogenesis driver to feed its growth and spread, and VEGF signaling also helps it suppress local immunity, adding to its notoriously invasive behavior.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Melanoma's pigment is forged with copper: tyrosinase, the copper-dependent enzyme, builds the melanin that colors melanocytes and the tumors they spawn, so copper sits at the heart of the cell's identity.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Desmoplastic melanoma masquerades as fibrosis: this variant forms a firm, scar-like fibrous tumor that is easily mistaken for benign and tends to track along nerves, making it treacherous to diagnose.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Melanoma is the cancer that most loves the small bowel: it is the tumor most likely to metastasize to the small intestine, where deposits bleed or obstruct, sometimes years after the original lesion.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutations are the single most common genetic change in cutaneous melanoma: UV-induced point mutations switch telomerase back on, granting the cells the unlimited replication that drives progression and marking a worse prognosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy clinches amelanotic melanoma: when a pigmentless tumor defies routine stains, the beam reveals melanosomes and striated premelanosomes — membrane-bound organelles found only in melanocytic cells — settling the diagnosis.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal gland is a favored melanoma metastatic site: these tumors seed the adrenals so reliably that a new adrenal mass in a melanoma patient is treated as a metastasis until proven otherwise, and resection of isolated deposits can prolong survival.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Melanoma loves the heart more than any other cancer: it has the highest rate of cardiac metastasis, seeding the myocardium and pericardium with deposits that can disturb rhythm or fill the pericardial sac.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Melanoma reaches the skeleton: bone metastases riddle the marrow-bearing spine and pelvis in advanced disease, painful and prone to fracture, part of its notoriously wide metastatic spread.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The gut is classic melanoma territory: it is among the cancers most likely to metastasize to the stomach and bowel, where pigmented deposits bleed or obstruct, sometimes appearing years after the skin lesion.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both name and fight melanoma: SOX10, S100, HMB-45, and Melan-A stains identify amelanotic tumors on biopsy, while the monoclonal antibodies against PD-1 and CTLA-4 unleash the immune attack that has transformed advanced-melanoma survival.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Melanoma sits at the sun's double edge: the same UV that makes vitamin D in the skin also drives the cancer, yet low vitamin D levels track with thicker tumors and worse outcomes, so repletion is studied even as sun avoidance is urged.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The blood count carries a prognosis: a high neutrophil-to-lymphocyte ratio marks an inflammatory, immunosuppressive state that predicts poorer response to checkpoint immunotherapy in melanoma, a cheap clue read straight off a routine blood test.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Immunotherapy can turn on the thyroid: the checkpoint inhibitors that transformed melanoma treatment commonly trigger autoimmune thyroiditis, causing transient hyperthyroidism then lasting hypothyroidism — one of the most frequent immune-related side effects.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Melanoma is the tumor most apt to cross the placenta: in pregnancy it can spread to the placenta and rarely the fetus, and because it is hormonally responsive, its behavior and management in pregnant patients need special care.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets help melanoma spread: circulating tumor cells cloak themselves in platelets to hide from natural killer cells and to lodge in distant vessels, a partnership that aids metastasis and makes platelets a studied antimetastatic target.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Melanoma launched modern immunotherapy: high-dose IL-2 produced the first durable remissions by goading T cells to attack, the proof-of-concept that the immune system could clear metastatic melanoma and the forerunner of today's checkpoint and cell therapies.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Unleashing the immune system has a cost: checkpoint inhibitors used against melanoma can trigger autoimmune attack on the pancreas, causing new-onset type 1 diabetes as an immune-related adverse event — the flip side of releasing the brakes on T cells.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The tumor's stroma fights back for it: cancer-associated fibroblasts remodel the matrix and secrete growth factors that shield melanoma cells, a niche that blunts BRAF-targeted drugs and helps the tumor regrow after an initial response.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 helps melanoma hide from immunity: constitutive STAT3 signaling drives survival and an immunosuppressive microenvironment, dampening the antitumor response that checkpoint inhibitors try to restore.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Immunotherapy turns on the glands: checkpoint inhibitors for melanoma commonly cause endocrine immune-related adverse events — hypophysitis, thyroiditis, and adrenal insufficiency — that can be permanent and need hormone replacement.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells stock the melanoma stroma: they accumulate around the tumor and release angiogenic and matrix-remodeling mediators that support invasion and new-vessel growth in the microenvironment.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB drives melanoma's survival and immune escape: constitutive NF-κB signaling supports proliferation and an immunosuppressive microenvironment, one of the pathways behind resistance to targeted and immune therapy.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Advanced disease clots the veins: metastatic melanoma carries tumor-driven hypercoagulability, and the surgery and systemic therapy it requires further raise the risk of venous thromboembolism.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Immunotherapy and advanced disease open the door to infection: severe immune-related colitis treated with steroids, plus the burden of metastatic disease, leave melanoma patients vulnerable to serious infection and sepsis.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Its immunotherapy can ignite the immune system: the checkpoint inhibitors central to melanoma treatment can trigger immune-related adverse events and, occasionally, a cytokine-release-like storm of systemic inflammation.
- `connects-to` → **[Stroke](../stroke/README.md)** — It seeds the brain and bleeds: melanoma is among the most brain-metastatic cancers, and its metastases are characteristically hemorrhagic, causing intracranial bleeding and stroke.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Its therapies and threat weigh on mood: historically interferon-α treatment caused depression, and the diagnosis, disfiguring surgery and metastatic threat of melanoma carry a substantial psychological burden.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its immunotherapy can inflame the heart: the checkpoint inhibitors central to melanoma treatment occasionally cause an immune-mediated myocarditis, a rare but often fatal route to acute heart failure.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Checkpoint immunotherapy can scar the kidneys: the PD-1 and CTLA-4 inhibitors used for advanced melanoma can provoke an immune-mediated interstitial nephritis that, if recurrent, leaves chronic kidney impairment.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Recurrence risk and skin surveillance breed worry: the threat of metastasis and the lifelong monitoring for new primaries in melanoma foster chronic health anxiety alongside depression.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Checkpoint immunotherapy inflames the gut: the PD-1 and CTLA-4 inhibitors used for melanoma frequently cause immune-related colitis with severe diarrhoea and autoimmune hepatitis, the commonest serious irAEs.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads to and inflames the lungs: melanoma metastasises readily to the lungs, and checkpoint immunotherapy can cause an immune-mediated pneumonitis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its surgery is wide and node-sampling: melanoma is treated with wide local excision and sentinel-node biopsy or lymph-node dissection, leaving wounds and lymphatic disruption that heal slowly.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It favours the heart among metastases: melanoma is the tumour most likely to metastasise to the heart and pericardium, and its checkpoint-inhibitor therapy can cause life-threatening myocarditis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It spreads to bone and inflames joints: melanoma metastasises to the skeleton causing pain and fractures, and checkpoint-inhibitor immunotherapy can trigger inflammatory arthritis and myositis.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its immunotherapy can inflame the kidney: checkpoint inhibitors used for melanoma can cause immune-related interstitial nephritis with acute kidney injury.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It pioneered modern oncology drugs: melanoma is the prototype for both BRAF/MEK-targeted therapy and immune checkpoint blockade, transforming the outlook for advanced disease.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Inherited risk runs in some families: germline TP53 (Li-Fraumeni) and CDKN2A mutations raise melanoma risk, part of the hereditary predisposition behind a minority of cases.
- `connects-to` → **[Hereditary Breast-Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — BRCA2 widens its reach: carriers of BRCA2 mutations have an increased melanoma risk, linking this skin cancer to the hereditary breast-ovarian cancer spectrum.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — The breakthrough that defined immunotherapy: ipilimumab (anti-CTLA-4) and anti-PD-1 antibodies transformed metastatic melanoma from rapidly fatal to often durably controlled, the disease where checkpoint blockade first proved itself.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — A surprising two-way link: melanoma and Parkinson's disease show a bidirectional epidemiological association, thought to reflect shared biology of melanin and neuromelanin in pigment-cell pathways.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo that history left behind: melanoma is notoriously chemoresistant, and dacarbazine-based chemotherapy has been largely abandoned in favour of immunotherapy and targeted drugs.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Lymphoid islands forecast its immunotherapy response: melanomas that contain tertiary lymphoid structures with germinal-centre-like B-cell aggregates respond better to checkpoint blockade, marking the cancer where immunotherapy first proved transformative.
- `connects-to` → **[GIST](../gist/README.md)** — KIT links a skin cancer to a gut tumour: acral and mucosal melanomas often carry activating KIT mutations like gastrointestinal stromal tumours, so these melanoma subtypes can respond to the KIT inhibitor imatinib that defines GIST therapy.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — A shared BRAF driver: papillary thyroid cancer and melanoma both frequently harbour the BRAF V600E mutation, and BRAF/MEK inhibitors developed in melanoma are now used in BRAF-mutant thyroid cancer—one mutation across two organs.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — CDKN2A and the FAMMM syndrome: germline CDKN2A mutation causes familial atypical multiple mole melanoma, raising the risk of both melanoma and pancreatic cancer—one gene linking skin and pancreas.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Checkpoint myocarditis: the immune checkpoint inhibitors that revolutionised melanoma treatment can trigger a rare but often fatal autoimmune myocarditis of the myocardium, a feared immune-related adverse event.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver is a favoured metastatic site: melanoma—especially ocular melanoma—spreads to the liver, seeding the hepatic lobule, a pattern that dominates uveal melanoma's course.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Same mutation, different response: BRAF V600E drives both melanoma and a colorectal cancer subset, yet BRAF inhibitors alone work in melanoma but fail in colon cancer because EGFR feedback reactivates the pathway—a lesson in context-dependent oncogene targeting.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Immunotherapy's autoimmune cost: the checkpoint inhibitors that revolutionised melanoma treatment unleash an autoimmune colitis closely resembling inflammatory bowel disease, managed with the same steroids and anti-TNF biologics.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Seizures from brain spread: melanoma is among the cancers most prone to forming brain metastases, often haemorrhagic, making it a notable cause of secondary seizures and epilepsy in advanced disease.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Phenotype switch and immune escape: Wnt/β-catenin signalling controls melanoma phenotype switching and, when active, excludes T cells from the tumour—a driver of resistance to immunotherapy.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle amplification: CCND1 (cyclin D1) amplification, common in acral and mucosal melanoma, partners CDK4/6 to drive proliferation, supporting CDK4/6-inhibitor strategies.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Survival and resistance: PI3K-AKT-mTOR signalling from PTEN loss sustains melanoma survival and contributes to acquired resistance to BRAF/MEK-targeted therapy.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplified oncogene: MYC amplification drives the proliferation and metabolism of melanoma and is implicated in resistance to targeted therapy.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic invasion: HIF-1α stabilised in hypoxic melanoma drives angiogenesis, the invasive phenotype switch and metastasis to distant organs.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic driver: EZH2 is frequently activated in melanoma, silencing tumour-suppressor genes and promoting metastasis and immune evasion.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Immune response and resistance: an IFN-γ-driven T-cell signature predicts melanoma's response to checkpoint inhibitors, while loss of IFN-γ signalling (JAK/STAT) is a key route to immunotherapy resistance.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Immunosuppression and invasion: TGF-beta dampens anti-tumour immunity and drives the phenotype switch toward an invasive, mesenchymal melanoma state that resists therapy.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 draws tumour-associated macrophages into melanoma, building an immunosuppressive microenvironment that supports growth and metastasis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The high UV-driven mutational burden of melanoma generates cytosolic DNA and neoantigens that engage cGAS-STING—central to why melanoma is the paradigm immunotherapy-responsive cancer and the rationale for intratumoral STING agonists.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — The CXCL12-CXCR4 axis drives the broad metastatic spread of melanoma, including its notorious dissemination to the brain—the pattern that historically made advanced melanoma one of the most lethal solid tumors.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — BRAF and MEK inhibitors kill melanoma cells by relieving the mutant-BRAF block on caspase-3-mediated apoptosis, the mechanism behind the rapid, dramatic responses to targeted therapy in BRAF-V600-mutant disease.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Melanoma cells express the endothelin-B receptor inherited from their melanocyte origin, and EDNRB signaling promotes their proliferation, survival and invasion—a lineage-survival pathway being explored as a therapeutic target.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNA-methylation changes silence tumor-suppressor and antigen-presentation genes in melanoma, contributing to its plasticity and immune escape, and DNA-methyltransferase inhibitors are being combined with immunotherapy to re-sensitize resistant tumors.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IGF-1R signaling provides a survival and growth input that helps melanoma cells escape BRAF/MEK inhibition, a bypass pathway implicated in acquired resistance to targeted therapy.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — The CDK4/6-cyclin-D1 axis (cyclin-D1 mapped, with CDKN2A loss mapped) drives melanoma proliferation, a node combined with BRAF/MEK inhibition to deepen responses.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT activation (PTEN, AKT and mTOR already mapped) is a major mechanism by which melanoma escapes BRAF/MEK inhibition, the rationale for combined pathway blockade.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — NRAS mutation is the second-commonest melanoma driver after BRAF, activating the RAS-MAPK cascade (ERK1/2 mapped) in a subgroup that resists BRAF inhibitors.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Interferon-γ signaling through JAK-STAT (IFN-γ already mapped) drives the antitumor immune response in melanoma, and loss-of-function JAK1/2 mutations are a key mechanism of acquired resistance to checkpoint immunotherapy.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling counters the ultraviolet- and metabolism-derived oxidative stress of melanoma and contributes to its therapy resistance.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — UV-induced and TLR-MyD88-NF-κB innate signaling (NF-κB already mapped) shapes the inflammatory microenvironment that promotes melanoma initiation and progression.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes melanoma invasion, metastasis and immune evasion.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) drives immunosuppression and the invasive/metastatic phenotype switch in melanoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ-STAT1 signaling (IFN-γ mapped) shapes both the antitumor immune response and the adaptive immune resistance of melanoma to checkpoint therapy.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulation of the Wnt/β-catenin axis and of MITF shapes the proliferative-versus-invasive phenotype switch of melanoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by the BRAF-MAPK and PI3K-AKT axes, regulate the oxidative-stress balance and survival of melanoma cells.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — YAP1 activity drives the invasive, drug-tolerant phenotype and contributes to BRAF/MEK-inhibitor resistance in melanoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 restrains p53-mediated apoptosis in melanoma, a survival axis often intact given melanoma's typically wild-type TP53.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from myeloid-derived suppressor cells shape the immunosuppressive premetastatic niche of melanoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling contributes to the invasion and metastatic dissemination of melanoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and BRAF-inhibitor resistance of melanoma cells.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation and immunotherapy response of melanoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic plasticity of melanoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of melanoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and immune-evasion signaling of melanoma.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the proliferation and phenotype-switching biology of melanoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of melanoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of melanoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of melanoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of melanoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of melanoma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin (SPP1) participates in the tumor microenvironment, invasion, and metastasis of melanoma, and is a recognized prognostic marker.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Neoantigen immunotherapy: melanoma's ultraviolet-driven high mutational burden (photon already mapped) yields abundant MHC-presented neoantigens, underlying its landmark responsiveness to checkpoint inhibitors (PD-1/CTLA-4 already mapped) and neoantigen vaccines.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Targeted-therapy resistance: an AXL-high dedifferentiated cell state drives resistance to BRAF/MEK inhibitors (BRAF already mapped) in melanoma, a phenotype-switching escape route beyond secondary genetic mutations.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Immunotherapy myocarditis: checkpoint inhibitors, the mainstay of melanoma therapy, can cause immune-mediated myocarditis, a rare but often fatal adverse event that troponin elevation helps detect early.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the melanoma microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), a mechanism of immune evasion and resistance to the checkpoint blockade central to its treatment.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Ultraviolet oxidative damage: ultraviolet light and the inflamed skin generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage (NRF2 already mapped) adds to the mutational burden driving cutaneous melanoma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 help: helper T cells polarised to Th1 (interferon-gamma and IL-2 already mapped) support the cytotoxic CD8 (already mapped) response against melanoma, part of the anti-tumour immunity that checkpoint blockade and vaccines amplify.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — UV and immunosuppression: ultraviolet-induced cyclooxygenase-2 and prostaglandin E2 promote the inflammation and local immunosuppression of photocarcinogenesis, part of the microenvironment that fosters melanoma and blunts anti-tumour immunity.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive microenvironment that checkpoint immunotherapy must overcome in melanoma.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF and endothelin-1 (already mapped) regulates the angiogenesis and vascular tone of melanoma, and it also modulates the melanocyte and immune biology of the tumour.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment that checkpoint immunotherapy must overcome in melanoma.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Ferroptosis vulnerability: the iron-dependent lipid peroxidation of ferroptosis is a vulnerability of the drug-tolerant, dedifferentiated melanoma cells (NRF2 already mapped), an emerging angle against treatment-resistant disease.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Melanocyte metals: zinc supports the melanocyte enzymes of melanogenesis and the skin's zinc-dependent function, part of the trace-metal biology of the melanocytes from which melanoma arises.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon adjuvant immunotherapy: interferon-α was the historical adjuvant immunotherapy of high-risk melanoma, and the type-I interferon signalling shapes the immunogenicity and the checkpoint (PD-1 already mapped) response of the tumour.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic-immune adipokine: leptin, part of the obesity-melanoma metabolic axis, modulates the tumour and the T-cell (already mapped) immune response of melanoma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Microenvironment adipokine: adiponectin, with leptin (already mapped), is part of the adipokine modulation of the melanoma microenvironment and the immunotherapy response.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Microenvironment adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the obesity-melanoma axis and the immunotherapy microenvironment.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the immunogenic melanoma, augmenting the checkpoint (PD-1 already mapped) immunotherapy.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil biomarker: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophilia associated with the favourable response to the melanoma checkpoint immunotherapy.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Tertiary lymphoid B-cell response: the plasma cells and B cells of the intratumoural tertiary lymphoid structures produce antibody (already mapped) and predict a favourable response to the checkpoint (PD-1 already mapped) immunotherapy of melanoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the melanoma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/AllergoOncology arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), is the antibody arm explored in the AllergoOncology anti-tumour response against melanoma.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the intratumoural tertiary lymphoid structures whose presence predicts the response to the checkpoint (PD-1 already mapped) immunotherapy of melanoma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the inflammatory and immunosuppressive dimension of the melanoma microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling recruits and polarises the myeloid cells to an immunosuppressive phenotype in the melanoma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the melanoma cells recruit factor H to regulate the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) and evade the complement attack of the melanoma microenvironment.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-tumour antibodies (already mapped) within the melanoma microenvironment.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Tumour iron: transferrin, the iron carrier, supplies the iron demand of the proliferating melanoma cells, which overexpress the transferrin receptor.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Immune-polarisation alarmin: TSLP from keratinocytes and stromal cells skews the melanoma microenvironment toward Th2, suppressing the anti-tumour Th1 and NK-cell (already mapped) immunity and reducing the efficacy of the PD-1 (already mapped) checkpoint inhibitors.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Melanoma invasion stroma: periostin secreted by cancer-associated fibroblasts and TGF-β (already mapped) signalling promotes the stromal remodelling and integrin αV-mediated invasiveness of melanoma cells, facilitating the locoregional spread and metastasis of melanoma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell immunosuppression: histamine from the mast cells (already mapped) infiltrating melanoma stroma promotes VEGF (already mapped) angiogenesis and suppresses NK-cell cytotoxicity via H2 receptor signalling, contributing to the immune-evasion of melanoma.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Tumour vascular permeability: bradykinin, via B2 receptor, amplifies VEGF-driven (already mapped) angiogenesis and peritumoral oedema in melanoma; kinin-kallikrein activation enhances mast-cell (already mapped) and fibroblast (already mapped) stromal recruitment.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Tumour EPOR signalling: erythropoietin receptor (EPOR) on melanoma cells activates JAK2/STAT3 (already mapped) pro-survival signalling, promotes VEGF (already mapped) angiogenesis, and blunts the apoptotic response to checkpoint-inhibitor (already mapped) immunotherapy.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Oncostatic melatonin: melatonin, via MT1/MT2 receptors on melanoma cells, suppresses BRAF (already mapped) and VEGF-driven (already mapped) proliferation and invasion, reduces MMP activity and augments NK-cell (already mapped) cytotoxicity against melanoma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-melanoma axis: testosterone, via androgen receptor on melanoma cells and macrophages (already mapped), modulates BRAF/VEGF (both already mapped) proliferative signalling and contributes to the sex-dimorphic incidence and checkpoint-inhibitor response of melanoma.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Melanocyte 5-HT axis: serotonin from UV-induced tryptophan metabolism in melanocytes (already mapped) activates 5-HT2 receptors on melanoma cells and tumour-infiltrating lymphocytes (already mapped), modulating immune evasion and the BRAF (already mapped) proliferative cascade.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Tumour-promoting prolactin: prolactin, via PRL-R on melanoma cells and tumour-associated macrophages (already mapped), activates the JAK2/STAT3 (already mapped) pro-survival pathway and promotes the VEGF-driven (already mapped) angiogenesis and immune evasion of melanoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Melanoma oxytocin anti-tumour: oxytocin, via OXTR on tumour-associated macrophages (already mapped) and mast cells (already mapped), attenuates the NF-κB (already mapped) and VEGF (already mapped) pro-tumour cascade, reducing immune evasion and angiogenesis in melanoma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Melanoma vasopressin vascular: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the tumour vascular niche; dysregulation amplifies NF-κB (already mapped) and VEGF (already mapped) pro-tumour angiogenic signalling in melanoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Melanoma selenium antioxidant: selenium, via GPx/TrxR selenoproteins in melanoma cells and macrophages (already mapped), quenches ROS that amplifies BRAF (already mapped) and NF-κB (already mapped) proliferative signalling, reducing the oxidative-stress phenotype of melanoma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Melanoma iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive tumour cascade of melanoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Melanoma sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of melanoma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Melanoma magnesium: magnesium, as cofactor of antioxidant enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped), attenuates oxidative stress; magnesium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of melanoma.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Melanoma calcium: calcium signals in macrophages (already mapped) and mast cells (already mapped) regulate immune activation; calcium flux amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of melanoma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Melanoma potassium: potassium channels regulate macrophage (already mapped) and T-cytotoxic (already mapped) antitumour function; potassium depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of melanoma.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Melanoma phosphorus: phosphorus, as phospholipid and ATP in macrophages (already mapped) and mast cells (already mapped), supports antitumour signalling; phosphorus depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of melanoma.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Melanoma carbon: carbon as backbone of BRAF (already mapped) and MITF signalling proteins in melanocytes (already mapped) sustains proliferative control; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) oncogenic cascade of melanoma.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Melanoma chloride: chloride regulates melanocyte (already mapped) and macrophage (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) immunosuppressive tumour cascade of melanoma.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Melanoma nitrogen: nitrogen in amino-acid scaffold of BRAF (already mapped) and PD-L1 proteins modulates T-cell (already mapped) immune evasion; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of melanoma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Melanoma hydrogen: hydrogen in redox chemistry of melanocytes (already mapped) sustains glutathione defence against UV-driven oxidative stress; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of melanoma.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Melanoma sulfur: sulfur in cysteine residues of BRAF (already mapped) and MITF proteins sustains redox stability in melanocytes; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) oncogenic cascade of melanoma.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Melanoma GLP-1: GLP-1 signalling modulates macrophage (already mapped) and dendritic-cell (already mapped) activation in the tumour microenvironment; GLP-1 deficit amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) oncogenic cascade of melanoma.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — Melanoma angiotensin-ii: angiotensin-II from macrophages (already mapped) and fibroblast (already mapped) drives tumour vascular remodelling; angiotensin-ii excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) cascade of melanoma.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Melanoma rankl: RANKL from macrophages (already mapped) and t-cytotoxic cells (already mapped) promotes melanoma immune evasion; rankl excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Melanoma fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) anchors tumour-invasive matrix; fibronectin dysregulation amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) cascade of melanoma.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Melanoma activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) drives tumour fibrotic remodelling; activin-a excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Melanoma cgrp: CGRP from fibroblasts (already mapped) and macrophages (already mapped) modulates melanoma vascular tone; cgrp excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Melanoma calcitonin: calcitonin from fibroblasts (already mapped) and macrophages (already mapped) modulates calcium signalling; calcitonin dysregulation amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Melanoma notch: NOTCH in fibroblasts (already mapped) and macrophages (already mapped) regulates melanoma cell fate; notch dysregulation amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Melanoma igf-1: IGF-1 from fibroblasts (already mapped) and macrophages (already mapped) promotes melanoma metabolic growth; igf-1 excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Melanoma tgf-beta: TGF-β from fibroblasts (already mapped) and macrophages (already mapped) drives melanoma immunosuppression; TGF-β excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — Melanoma substance-p: substance-P from fibroblasts (already mapped) and macrophages (already mapped) modulates pain tone; substance-P excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma.
- `connects-to` → **[Insulin-receptor](../../03-molecular/insulin-receptor/README.md)** — Melanoma insulin-receptor: insulin-receptor on fibroblasts (already mapped) and macrophages (already mapped) modulates metabolic axis; insulin resistance amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Melanoma aldosterone: aldosterone from fibroblasts (already mapped) and macrophages (already mapped) modulates electrolyte tone; aldosterone excess amplifies il-6 (already mapped) and vegf (already mapped) and wnt-beta-catenin (already mapped) tumour cascade of melanoma.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^larkin-2015-checkmate067]: Larkin J, Chiarion-Sileni V, Gonzalez R, et al. Combined nivolumab and ipilimumab or monotherapy in untreated melanoma. *N Engl J Med.* 2015;373(1):23-34. [doi:10.1056/NEJMoa1504030](https://doi.org/10.1056/NEJMoa1504030) · [PubMed 26027431](https://pubmed.ncbi.nlm.nih.gov/26027431/)
[^robert-2015-combi-v]: Robert C, Karaszewska B, Schachter J, et al. Improved overall survival in melanoma with combined dabrafenib and trametinib. *N Engl J Med.* 2015;372(1):30-39. [doi:10.1056/NEJMoa1412690](https://doi.org/10.1056/NEJMoa1412690) · [PubMed 25399551](https://pubmed.ncbi.nlm.nih.gov/25399551/)
[^wolchok-2022-checkmate067-7yr]: Wolchok JD, Chiarion-Sileni V, Gonzalez R, et al. Long-term outcomes with nivolumab plus ipilimumab or nivolumab alone versus ipilimumab in patients with advanced melanoma. *J Clin Oncol.* 2022;40(2):127-137. [doi:10.1200/JCO.21.02229](https://doi.org/10.1200/JCO.21.02229) · [PubMed 34958258](https://pubmed.ncbi.nlm.nih.gov/34958258/)
