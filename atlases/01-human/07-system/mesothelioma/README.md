---
schema: human-scale-entry/v1
id: mesothelioma
name: Mesothelioma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Malignant mesothelioma arises from pleural/peritoneal mesothelial cells; asbestos exposure causes ~80% with 30-50-year latency; BAP1 (~55%) and NF2 (~40%) loss define molecular subtypes. Nivolumab+ipilimumab (CheckMate 743: OS 18.1 vs 14.1 months) is first-line standard."
aliases: ["mesothelioma", "malignant pleural mesothelioma", "MPM", "peritoneal mesothelioma", "asbestos cancer", "epithelioid mesothelioma", "sarcomatoid mesothelioma", "biphasic mesothelioma", "Krenning mesothelioma"]
sources:
  - id: baas-2021-checkmate743
    type: peer-reviewed
    cite: "Baas P, Scherpereel A, Nowak AK, et al. First-line nivolumab plus ipilimumab in unresectable malignant pleural mesothelioma (CheckMate 743): a multicentre, randomised, open-label, phase 3 trial. Lancet. 2021;397(10272):375-386."
    doi: "10.1016/S0140-6736(20)32714-8"
    pmid: "33485464"
    url: "https://doi.org/10.1016/S0140-6736(20)32714-8"
  - id: vogelzang-2003-pemetrexed
    type: peer-reviewed
    cite: "Vogelzang NJ, Rusthoven JJ, Symanowski J, et al. Phase III study of pemetrexed in combination with cisplatin versus cisplatin alone in patients with malignant pleural mesothelioma. J Clin Oncol. 2003;21(14):2636-2644."
    doi: "10.1200/JCO.2003.11.136"
    pmid: "12860938"
    url: "https://doi.org/10.1200/JCO.2003.11.136"
cross_links:
  - target: 01-human/03-molecular/bap1
    relation: connects-to
    note: "BAP1 loss (~50-60% of mesothelioma) drives polycomb-mediated epigenetic reprogramming; BAP1 IHC nuclear loss aids mesothelioma diagnosis; epithelioid BAP1-mutant mesothelioma has better prognosis; germline BAP1 mutations → BAP1-TPDS (familial mesothelioma)."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Nivolumab + ipilimumab (CheckMate 743: OS 18.1 vs 14.1 months, HR 0.74, FDA 2021) is first-line for unresectable pleural mesothelioma; benefit most pronounced in sarcomatoid/biphasic subtypes (OS 18.1 vs 8.8 months); PD-L1 expression enriched in sarcomatoid."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Bevacizumab + cisplatin/pemetrexed (MAPS trial: OS 18.8 vs 16.1 months) is used in select European centers; VEGF overexpression is common in mesothelioma; ramucirumab (VEGFR2) under investigation; anti-VEGF + IO combinations in ongoing trials."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss in ~25% of peritoneal mesothelioma and ~10% of pleural; PI3K-AKT-mTOR activation downstream of PTEN loss → mTOR inhibitors studied in mesothelioma; PTEN-CDKN2A co-deletion confers aggressive phenotype; PTEN loss is more common in sarcomatoid subtype."
  - target: 01-human/03-molecular/nf2
    relation: connects-to
    note: "NF2/merlin loss occurs in ~40% of mesothelioma (enriched in the sarcomatoid subtype) → Hippo pathway off → YAP/TAZ nuclear → TEAD-driven proliferation; this makes NF2-null mesothelioma the lead indication for TEAD and FAK inhibitors now in early-phase trials."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pleural mesothelioma grows as a rind encasing the lung after asbestos fibers inhaled decades earlier lodge in the pleura; it presents with dyspnea and a large exudative effusion, and lung-sparing pleurectomy/decortication has largely replaced extrapleural pneumonectomy."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Asbestos drives mesothelioma partly through frustrated phagocytosis of long, biopersistent fibers by mesothelial cells and macrophages → ROS and NLRP3 inflammasome activation → IL-1β-driven chronic inflammation over 30-50 years → the mutagenic milieu that seeds malignancy."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Mesothelioma and meningioma share their central driver — NF2/merlin loss switching off Hippo so YAP/TAZ-TEAD drive proliferation (NF2-null in ~40% of mesothelioma, ~50-60% of meningioma) — why both spearhead trials of TEAD inhibitors despite arising in very different tissues."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Mesothelioma is moderately immunogenic, so dual checkpoint blockade — nivolumab plus ipilimumab, freeing cytotoxic CD8+ T cells — became first-line for unresectable pleural disease (CheckMate 743), with the largest benefit in the chemo-resistant sarcomatoid subtype."
  - target: 01-human/07-system/uveal-melanoma
    relation: connects-to
    note: "Mesothelioma and uveal melanoma are linked by BAP1: germline BAP1 loss causes the BAP1 tumor-predisposition syndrome, in which one family develops mesothelioma, uveal melanoma, renal cell carcinoma, and skin tumors — a shared chromatin defect across different organs."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Mesothelioma and renal cell carcinoma are both part of the BAP1 tumor predisposition syndrome: germline BAP1 loss predisposes to mesothelioma, clear-cell RCC, uveal melanoma and atypical melanocytic tumors, so mesothelioma with a family cancer history warrants BAP1 testing."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages drive asbestos-induced mesothelioma: long fibers resist 'frustrated' macrophage phagocytosis, so they release reactive oxygen species and activate the NLRP3 inflammasome—chronic IL-1β inflammation that transforms mesothelial cells over decades."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Mesothelioma and cholangiocarcinoma both occur in the BAP1 syndrome and share a chromatin-level driver: loss of BAP1, a nuclear deubiquitinase tumor suppressor, promotes both, and the epigenetic vulnerabilities plus checkpoint approaches are being explored across these cancers."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Mesothelioma and lung cancer are the great asbestos-related thoracic malignancies but distinct: mesothelioma arises from the pleural mesothelium, while NSCLC arises from bronchial/alveolar epithelium—asbestos drives both, but only lung cancer is strongly smoking-linked."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy's role in mesothelioma is limited: the tumor's diffuse rind over the pleura makes curative irradiation hard without harming lung, so photon radiation serves mainly palliation—surgery and chemo-immunotherapy carry the main burden."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Peritoneal mesothelioma and ovarian cancer overlap closely: both arise from or mimic serous peritoneal epithelium and may share BAP1 alterations, so a woman with peritoneal carcinomatosis needs pathology to separate mesothelioma from serous ovarian carcinoma."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion is a defining mesothelioma alteration: loss of this tumor suppressor, alongside BAP1 and NF2, drives the cancer and helps distinguish malignant mesothelioma from benign reactive mesothelial proliferation on biopsy—a key diagnostic marker."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The sarcomatoid subtype of mesothelioma is fibroblast-like and grim: spindle, fibroblast-resembling cells make a dense tumor far more resistant to therapy than the epithelioid type—so histologic subtype strongly predicts survival."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Mesothelioma is responsive to immunotherapy despite few mutations: chronic asbestos inflammation and an immune-rich microenvironment make checkpoint blockade (anti-PD-1/CTLA-4) a frontline option—so engaging the immune system has improved outcomes in this cancer."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Mesothelioma is the signature cancer of the respiratory system's lining: decades after asbestos inhalation, the pleura thickens with tumor that traps the lung in a rind, causing breathlessness and effusions—an almost wholly preventable, dismal-prognosis cancer."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53-pathway disruption helps drive mesothelioma: although BAP1 and CDKN2A losses dominate, p53 inactivation contributes to the genomic chaos of asbestos-induced tumors, so the guardian-of-the-genome network features in this slow-developing malignancy."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Carbon-ion radiotherapy is explored for mesothelioma: its dense, sharply localized dose may help this radioresistant, diffusely spreading pleural tumor, complementing the surgery, chemotherapy and immunotherapy used against an asbestos-caused cancer."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Mesothelioma's immunotherapy pairs two checkpoints: combining anti-CTLA-4 (ipilimumab) with anti-PD-1 (nivolumab) became a first-line standard, extending survival in unresectable disease where chemotherapy alone had long stalled."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Asbestos scars the pleura before it causes cancer: dense pleural fibrosis and plaques mark exposure, and the desmoplastic variant of mesothelioma is so fibrous it can be mistaken for benign scarring—making biopsy interpretation difficult."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Asbestos kills mesothelial cells partly through iron: fibers adsorb iron and catalyze reactive oxygen species that damage DNA, and iron-coated 'ferruginous bodies' in tissue are the histologic fingerprint of the exposure that drives mesothelioma."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Mesothelioma is fundamentally a Hippo-pathway cancer acting through YAP1: NF2 and LATS losses release YAP1 to switch on growth genes, so this transcription co-activator is a central driver and a sought-after drug target in the disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Mesothelioma's cause is a magnesium-silicate mineral: asbestos fibers like chrysotile are magnesium silicates whose durable, needle-like shape lodges in the pleura and provokes the decades-long inflammation that seeds the cancer."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Mesothelioma defends itself with regulatory T cells: Tregs fill its immunosuppressive microenvironment and blunt anti-tumor immunity, which is why dual checkpoint blockade (nivolumab plus ipilimumab) is now frontline for the disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Mesothelioma can arise on the heart's lining: though most form on the pleura, the same asbestos-driven malignancy strikes the pericardium, where it encases the heart and impairs its filling—a rare but devastating site."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Mesothelioma hides in a hypoxic, fibrous tumor via HIF-1alpha: its dense desmoplastic stroma outstrips its oxygen supply, and the resulting HIF signaling drives survival and angiogenesis, part of why it resists chemotherapy."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells are enlisted to fight mesothelioma: because the tumor is poorly immunogenic, dendritic-cell vaccines and other antigen-presenting strategies aim to prime T-cell attack alongside the checkpoint drugs now used frontline."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Mesothelioma also strikes the belly: peritoneal mesothelioma coats the abdominal organs and bowel, including the large intestine, causing pain, ascites, and obstruction—the second most common form after pleural."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Mesothelioma recruits endothelial cells to grow: VEGF from the tumor drives these vessel-lining cells to build its blood supply, which is why anti-VEGF therapy is added to chemotherapy."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Mesothelioma steals the breath of oxygen: as it encases the lung and fills the chest with malignant effusion, it squeezes the lung shut, so worsening breathlessness and low oxygen dominate the illness."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy was the historic gold standard for mesothelioma: its cells bristle with long, slender, bushy microvilli, whose high length-to-width ratio separates them from the short, stubby microvilli of metastatic adenocarcinoma."
  - target: 01-human/03-molecular/wt1
    relation: connects-to
    note: "WT1 is a defining mesothelioma marker: strong nuclear WT1 staining is expected in mesothelial tumors and absent in lung adenocarcinoma, making it a pillar of the immunostain panel that resolves a pleural biopsy."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Mesothelioma drives up platelets: IL-6 from the tumor provokes a paraneoplastic thrombocytosis, and a high platelet count both flags advanced disease and raises the clotting risk that complicates these patients' care."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Peritoneal mesothelioma encases the abdominal organs: arising on the lining of the belly, it spreads over the surface of the liver and gut, coating them in tumor rather than invading deep, the abdominal counterpart of its pleural form."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Late mesothelioma can reach bone: though it spreads mainly by creeping along the chest and abdominal linings, advanced disease occasionally seeds distant skeletal and marrow metastases."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "A well-differentiated papillary mesothelioma leaves calcium clues: it forms psammoma bodies, concentric calcium deposits, the laminated mineral specks that help the pathologist recognize this indolent variant."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Mesothelioma is diagnosed by antibody panels: calretinin, WT1, and D2-40 stain positive while CEA, MOC-31, and claudin-4 stay negative, separating it from adenocarcinoma, and loss of BAP1 staining confirms the malignant clone."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The blood count both warns and weakens: a high neutrophil-to-lymphocyte ratio predicts poorer survival in mesothelioma, while the pemetrexed-cisplatin chemotherapy used against it is myelosuppressive, dropping neutrophils and risking infection."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Chronic disease and chemotherapy thin the red cells: the smoldering inflammation of mesothelioma plus antifolate pemetrexed depress erythrocyte production into the anemia and fatigue that shadow the long course of treatment."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Losing NF2 unleashes mTOR: merlin normally restrains both the Hippo pathway and mTORC1, so its frequent loss in mesothelioma drives growth through mTOR — a vulnerability probed alongside the Hippo-YAP axis for targeted therapy."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "BAP1 mesothelioma runs in families: germline BAP1 mutations transmit a tumor-predisposition syndrome down the generations, so a diagnosis can prompt cascade genetic testing and reproductive counseling for relatives at risk."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Asbestos keeps the pleura inflamed: the indigestible fibers provoke a chronic response in which mast cells and macrophages release mediators that, over decades, foster the mutations and microenvironment from which mesothelioma arises."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "The tumor cheats its clock: TERT promoter mutations switch telomerase back on so mesothelioma cells escape the telomere shortening that should limit their divisions, one of the few recurrent point mutations in a cancer otherwise defined by losing tumor suppressors."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Beyond Hippo, a second developmental pathway fuels it: aberrant Wnt/β-catenin signaling promotes mesothelial proliferation and survival, making the pathway a studied therapeutic target alongside the YAP/Hippo axis disrupted by NF2 loss."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate killers are part of the fight: natural killer cells can lyse mesothelioma, and the disease's heavy immunosuppression dampens them, which is why NK-engaging and CAR-NK strategies are explored alongside the checkpoint drugs now used against it."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 carries mesothelioma's systemic toll: the tumor and its asbestos-driven inflammation pour out IL-6, fueling the paraneoplastic thrombocytosis, fever, and cachexia that mark advanced disease and predict worse outcome."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Few cancers clot like mesothelioma: its pro-coagulant tumor and the surgery and chemotherapy used against it give a high venous thromboembolism risk that complicates the whole treatment course."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "It can wrap and squeeze the heart: pericardial mesothelioma — and pleural disease encasing the heart — causes effusion and constriction that impair filling, producing a restrictive heart failure."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Asbestos-driven inflammation feeds STAT3: the chronic IL-6-rich inflammation that asbestos provokes in the pleura activates STAT3, a survival and proliferation signal central to mesothelioma's inflammation-to-cancer origin."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "An infected pleural space turns dangerous: recurrent pleural effusions, indwelling drains, pleurodesis and major surgery for mesothelioma can seed empyema and bloodstream infection that progress to sepsis."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic inflammation wears down the blood: the IL-6-driven inflammatory state of mesothelioma suppresses erythropoiesis, producing an anemia of chronic disease that contributes to the fatigue of advanced disease."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "It grows into the chest wall and nerves: mesothelioma encases the pleura and invades the chest wall and intercostal nerves, causing severe, often intractable neuropathic chest pain that dominates the illness."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its chemo is hard on the kidney: the cisplatin-pemetrexed backbone of mesothelioma treatment is nephrotoxic, and pemetrexed is renally cleared, so impaired and injured kidneys both threaten and are threatened by therapy."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A dismal prognosis weighs on mood: relentless breathlessness and chest pain, a near-uniformly fatal course and often unresolved asbestos-related litigation give mesothelioma a heavy burden of depression."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Chemotherapy and damaged pleura open the lung to mold: the neutropenia from pemetrexed-platinum chemotherapy, plus a scarred, trapped lung, can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Radical chest surgery heals badly: extrapleural pneumonectomy or decortication for mesothelioma, plus repeated chest drains and pleurodesis, leave large thoracic wounds slow to heal in a cachectic patient."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Breathlessness and a grim prognosis breed worry: the air hunger, chest pain and near-uniformly fatal outlook of mesothelioma, with its asbestos-litigation stress, foster severe anxiety alongside depression."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It also grows in the belly: peritoneal mesothelioma, the second commonest form, encases the bowel and causes ascites, abdominal pain and intestinal obstruction."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It seeds the skin along procedure tracks: mesothelioma characteristically grows out along the tracts of chest drains, biopsies and surgical scars, forming painful cutaneous tumour nodules."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It eats into the chest wall: pleural mesothelioma invades the ribs and intercostal structures, causing relentless chest-wall pain and bony destruction as it spreads."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It spreads through and blocks the lymphatics: mesothelioma invades mediastinal and hilar lymph nodes, and obstruction of pleural lymphatic drainage produces the recurrent effusions that dominate its course."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It can encase and arise on the heart: pleural mesothelioma can wrap the pericardium causing constrictive physiology, and a rare primary pericardial mesothelioma exists."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It invades the chest-wall nerves: tumour growth into the intercostal nerves causes severe neuropathic chest-wall pain, the dominant and hardest-to-control symptom of advanced mesothelioma."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Chemotherapy threatens the kidney: the cisplatin-pemetrexed regimen central to mesothelioma treatment is nephrotoxic, and pemetrexed itself requires adequate renal function."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Immunotherapy extended survival: dual checkpoint blockade with nivolumab and ipilimumab is now a standard first-line option for unresectable pleural mesothelioma."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can derange metabolism: mesothelioma occasionally causes paraneoplastic hypoglycaemia or SIADH with hyponatraemia among its systemic effects."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Platinum-pemetrexed is the chemo backbone: cisplatin with pemetrexed, sometimes with bevacizumab, is the standard chemotherapy for mesothelioma not treated with immunotherapy."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "A pleural tumour to distinguish: primary pleural synovial sarcoma mimics mesothelioma radiologically and histologically, separated by its SS18 gene fusion."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Both belong to the BAP1 family: germline BAP1 loss predisposes to mesothelioma alongside uveal and cutaneous melanoma and renal cancer, a hereditary tumour-predisposition syndrome."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy moved to the front line: dual checkpoint blockade with nivolumab and ipilimumab (CheckMate-743) improves survival over chemotherapy in unresectable pleural mesothelioma, especially the chemo-resistant sarcomatoid type."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Where the fibres land and the damage starts: inhaled asbestos fibres deposit in the distal alveoli, then migrate to the pleura over decades; the same fibres scar the alveolar walls as asbestosis, the fibrotic lung disease that accompanies mesothelioma risk."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "The main mimic on a pleural biopsy: metastatic breast cancer is a common cause of malignant pleural effusion and pleural nodules that must be distinguished from mesothelioma, separated by immunohistochemistry (calretinin/WT1 versus epithelial markers)."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "Shared NF2/merlin loss: mesothelioma frequently inactivates the NF2/merlin tumour suppressor, the same gene whose germline loss defines neurofibromatosis type 2 and drives its schwannomas and meningiomas."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Pericardial mesothelioma: a rare primary mesothelioma arises from the pericardium enveloping the myocardium, causing constrictive physiology and cardiac tamponade."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Immunotherapy in an inflamed tumour: mesothelioma's chronic asbestos-driven inflammation supports tertiary lymphoid structures, and combined PD-1/CTLA-4 checkpoint blockade is now first-line for unresectable disease."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "The benign mimic: tuberculous pleurisy produces pleural thickening, effusion and a rind that can closely imitate mesothelioma on imaging, a crucial differential to exclude with biopsy especially where TB is endemic."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The peritoneal variant: about a fifth of mesotheliomas arise in the peritoneum, studding the serosal surfaces and encasing the bowel over its intestinal epithelium to cause obstruction and ascites."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Chest-wall invasion: pleural mesothelioma grows outward through the pleura into the chest wall, eroding ribs and cortical bone and seeding the tracts left by biopsy needles and chest drains."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "BAP1 synthetic lethality: BAP1 loss in mesothelioma creates a dependence on EZH2, the rationale for EZH2 inhibitors such as tazemetostat in BAP1-deficient tumours."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Receptor overexpression: EGFR is frequently overexpressed in mesothelioma, contributing to its growth signalling though single-agent EGFR inhibition has had limited success."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative drive: MYC activation contributes to the aggressive proliferation of mesothelioma, downstream of its tumour-suppressor losses."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT survival: PTEN loss and PI3K/AKT activation sustain mesothelioma cell survival, cooperating with the NF2-Hippo and BAP1 lesions that define the disease."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: CDKN2A deletion—near-universal in mesothelioma—unleashes cyclin D-CDK4/6, accelerating the cell cycle and marking poor prognosis."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Autocrine growth: mesothelioma cells secrete PDGF that acts in an autocrine loop, driving the proliferation and desmoplastic stroma of these pleural tumours."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Asbestos inflammasome carcinogenesis: asbestos fibres activate the NLRP3 inflammasome in mesothelial cells and macrophages to release IL-1β, the chronic inflammation that drives mesothelioma over decades."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Immunosuppressive desmoplasia: TGF-beta drives the desmoplastic stroma and suppresses anti-tumour immunity in mesothelioma, contributing to its poor response to therapy."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 draws the abundant tumour-associated macrophages of mesothelioma into the pleural tumour, building an immunosuppressive microenvironment."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "HMGB1-RAGE carcinogenesis: asbestos fibres cause mesothelial-cell necrosis that releases HMGB1, which signals through RAGE to sustain the chronic inflammation central to asbestos-induced mesothelial carcinogenesis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Pleural spread: CXCR4-CXCL12 signalling drives the diffuse pleural and peritoneal spread of mesothelioma, the rind-like encasement of the lung that defines the disease and resists surgical control."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis evasion: mesothelioma resists caspase-3-mediated apoptosis through high anti-apoptotic protein expression, a key reason for its notorious chemoresistance and the modest benefit of cytotoxic therapy."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy: dual checkpoint blockade (nivolumab-ipilimumab) is now first-line for unresectable mesothelioma, and mesothelin-directed CAR-T cells aim to kill the tumour through perforin and granzyme, the cytotoxic effector mechanism of these immune therapies."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "Merlin-pathway signalling: the NF2/merlin loss common in mesothelioma disinhibits Src/FAK and the Hippo-YAP pathway at the membrane, driving the proliferation and loss of contact inhibition characteristic of these tumours."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "DNA-repair vulnerability: BAP1 loss impairs homologous-recombination DNA repair in mesothelioma, leaving cells reliant on RAD51-dependent and alternative repair and raising the prospect of synthetic-lethal PARP inhibition in BAP1-deficient tumours."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Unrestrained cell cycle: homozygous CDKN2A deletion (mapped) removes p16, leaving the CDK4/6-cyclin-D1 axis (cyclin-D1 mapped) unchecked in mesothelioma and a candidate target for CDK4/6 inhibition."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K signalling: PIK3CA drives the PI3K-AKT-mTOR axis (PTEN, AKT and mTOR already mapped) that supports growth and survival in mesothelioma."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Asbestos inflammation: TNF-α released by asbestos-activated macrophages promotes the survival and malignant transformation of mesothelial cells, part of the chronic inflammation (with the IL-1β/NLRP3 axis mapped) that drives mesothelioma."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic inflammatory drive: asbestos fibres trigger sustained NF-κB-driven inflammation (NLRP3 and IL-1β already mapped) in the pleura, the inflammatory milieu central to mesothelioma development."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Asbestos oxidative stress: NRF2 antioxidant defence counters the iron-catalysed reactive-oxygen-species generation by asbestos fibres that drives the oxidative DNA damage of mesothelioma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RTK-RAS proliferation: RAS-ERK signalling downstream of EGFR and PDGFR (both already mapped) provides a proliferative input to mesothelioma growth."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is expressed in mesothelioma and contributes to its invasion and immunosuppressive microenvironment."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IL-6-JAK-STAT3 signalling (IL-6 and STAT3 mapped), driven by asbestos-induced chronic inflammation, promotes mesothelioma growth."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) shapes the immunosuppressive and fibrotic microenvironment of mesothelioma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of mesothelioma, relevant to its checkpoint immunotherapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Asbestos-induced DNA damage and chronic inflammation engage cGAS-STING, contributing to the carcinogenesis and immune microenvironment of mesothelioma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate the oxidative stress of asbestos exposure relevant to the cellular transformation of mesothelioma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and survival signaling of the BAP1-deficient cells of mesothelioma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in mesothelioma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from asbestos-recruited myeloid cells shape the chronic inflammatory microenvironment driving mesothelioma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of mesothelioma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of mesothelioma cells."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling contributes, alongside BAP1 loss (BAP1 already mapped), to the epigenetic dysregulation of mesothelioma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of mesothelioma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of mesothelioma."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the proliferation and epithelial-mesenchymal biology of mesothelioma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of mesothelioma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of mesothelioma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of mesothelioma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of mesothelioma."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of mesothelioma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin (SPP1) participates in the asbestos-related inflammation and tumor microenvironment of mesothelioma, and is a recognized biomarker."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy: mesothelioma responds to combination checkpoint blockade (PD-1/CTLA-4 already mapped), and MHC class II antigen presentation shapes the T-cell response, with mesothelin-directed CAR-T and vaccines also in trials."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Mesothelin CAR-T: IL-2-driven T-cell expansion powers the mesothelin-targeted CAR-T and adoptive-cell therapies (perforin already mapped) being tested against mesothelioma, whose surface mesothelin makes it an attractive target."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Sarcomatoid invasion: the AXL receptor tyrosine kinase drives the epithelial-mesenchymal transition of mesothelioma toward the aggressive sarcomatoid phenotype, contributing to invasion and treatment resistance."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Asbestos oxidative injury: the iron-coated asbestos fibres (iron already mapped) generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage over decades initiates the mesothelial carcinogenesis of mesothelioma."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Effusion and anaemia: mesothelioma causes recurrent, often blood-stained pleural effusions, and the chronic disease with any haemorrhage lowers haemoglobin, the anaemia of malignancy adding to the breathlessness and cachexia."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the mesothelioma microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), part of the immune evasion that the dual checkpoint blockade standard in mesothelioma aims to overcome."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Asbestos inflammation: prostaglandins from the chronic asbestos-driven inflammation (IL-6, TNF and IL-1 already mapped) promote the proliferation and immunosuppression of mesothelial carcinogenesis, part of the inflammatory pathway of the disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive microenvironment of mesothelioma."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of mesothelioma, part of the stromal biology of these often highly vascular pleural tumours."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive microenvironment of mesothelioma."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Peritoneal mesothelioma: the peritoneal mesothelium lining the large intestine is the second commonest site of mesothelioma, the peritoneal form treated with cytoreductive surgery and heated intraperitoneal chemotherapy."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Peritoneal spread: the peritoneal mesothelioma also envelops the small intestine, the mesothelial lining of the peritoneal cavity coating the bowel loops in the diffuse peritoneal form."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Omental adipose adipokine: leptin from the omental and peritoneal adipose tissue signals to the peritoneal mesothelioma, part of the metabolic microenvironment of the tumour."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Peritoneal adipokine: adiponectin, with leptin (already mapped), from the omental and peritoneal adipose signals within the microenvironment of peritoneal mesothelioma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the peritoneal mesothelioma microenvironment."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the checkpoint (PD-1 already mapped) immunotherapy of mesothelioma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity exploited by the nivolumab-ipilimumab therapy of mesothelioma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the mesothelioma immune microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the asbestos-driven inflammatory microenvironment of mesothelioma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammatory microenvironment of mesothelioma."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the mesothelioma microenvironment."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the chronic asbestos-driven inflammation and the immunosuppressive dimension of the mesothelioma microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling recruits and polarises the myeloid cells within the chronic inflammatory microenvironment of mesothelioma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the tumour-infiltrating lymphocytes of mesothelioma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, associates with the nivolumab–ipilimumab (PD-1 already mapped) immunotherapy response of mesothelioma."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the mesothelioma cells recruit factor H to regulate the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) and evade the complement attack of the chronic-inflammatory microenvironment."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-tumour antibodies (already mapped) within the asbestos-driven chronic-inflammatory microenvironment of mesothelioma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Pleural mesothelial alarmin: TSLP released by the asbestos-damaged and inflamed pleural mesothelium (respiratory system already mapped) activates the innate dendritic-cell and mast-cell response, amplifying the HMGB1-NF-kB (already mapped) inflammatory cascade of mesothelioma."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Mesothelial invasion stroma: periostin is highly expressed in the mesothelioma pleural stroma, downstream of TGF-β (already mapped) and fibroblast activation; elevated periostin promotes the integrin αV-mediated invasiveness and fibrotic pleural thickening of mesothelioma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell stroma: histamine from the mast cells infiltrating mesothelioma stroma promotes VEGF (already mapped) angiogenesis and stromal remodelling; mast-cell histamine contributes to the pleural effusion and the immune-evasion environment of mesothelioma."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Pleural effusion kinin: bradykinin, via B2 receptor, amplifies pleural vascular permeability in mesothelioma; kinin-kallikrein activation enhances VEGF-driven (already mapped) angiogenesis and mast-cell (already mapped) stromal inflammation of mesothelioma."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Tumour EPOR signalling: erythropoietin receptor (EPOR) on mesothelioma cells activates the JAK2/STAT3 (already mapped) pro-survival pathway and promotes the VEGF-driven (already mapped) angiogenesis and resistance to platinum-based chemotherapy of mesothelioma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Oncostatic melatonin: melatonin scavenges reactive oxygen species generated by asbestos-activated mesothelial cells, attenuates NF-kB (already mapped) and TGF-β (already mapped) signalling, reducing the invasiveness and VEGF (already mapped) angiogenesis of mesothelioma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-mesothelioma axis: testosterone, via androgen receptor on mesothelioma cells and macrophages (already mapped), modulates NF-κB (already mapped) and VEGF-driven (already mapped) signalling and partly explains the male-predominant incidence of pleural mesothelioma."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Neuroendocrine 5-HT axis: serotonin from mast cells (already mapped) and mesothelioma-associated neuroendocrine cells signals via 5-HT2 receptors on endothelial cells (already mapped), amplifying the VEGF-driven (already mapped) angiogenic niche of pleural mesothelioma."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-escape prolactin: prolactin, via PRL-R on mesothelioma cells and macrophages (already mapped), activates JAK2/STAT3 (already mapped) pro-survival and immune-checkpoint (already mapped) pathways, promoting the immunosuppressive phenotype of pleural mesothelioma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Mesothelioma oxytocin anti-tumour: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the NF-κB (already mapped) and VEGF (already mapped) pro-tumour immune cascade, reducing the immunosuppressive phenotype of pleural mesothelioma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Mesothelioma vasopressin vascular: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the pleural tumour vascular niche; dysregulation amplifies NF-κB (already mapped) and VEGF (already mapped) angiogenic signalling in mesothelioma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Mesothelioma selenium antioxidant: selenium, via GPx/TrxR selenoproteins in mesothelioma cells and macrophages (already mapped), quenches ROS that amplifies NF-κB (already mapped) and VEGF-driven (already mapped) angiogenesis in the pleural mesothelioma microenvironment."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Mesothelioma iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of mesothelioma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Mesothelioma sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and TNF-α (already mapped) skewing amplifies the T-cytotoxic (already mapped) cascade of mesothelioma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Mesothelioma potassium: potassium channels regulate macrophage (already mapped) and neutrophil (already mapped) function in the mesothelioma TME; potassium depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of mesothelioma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Mesothelioma copper: copper, as cofactor of SOD1 in macrophages (already mapped) and mast cells (already mapped), scavenges ROS in the mesothelioma TME; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of mesothelioma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Mesothelioma zinc: zinc, as cofactor of metalloproteinases in macrophages (already mapped) and fibroblasts (already mapped), modulates matrix invasion; zinc depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of mesothelioma."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Mesothelioma phosphorus: phosphorus, as phospholipid and ATP in macrophages (already mapped) and mast cells (already mapped), drives immune signalling; phosphorus depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of mesothelioma."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Mesothelioma chloride: chloride regulates mesothelial cells (already mapped) and macrophage (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) asbestos-driven cascade of mesothelioma."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Mesothelioma nitrogen: nitrogen in amino-acid scaffold of BAP1 (already mapped) and CDKN2A proteins modulates mesothelial cell (already mapped) growth arrest; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of mesothelioma."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Mesothelioma sulfur: sulfur, as cysteine in macrophages (already mapped) and mesothelial cells (already mapped), supports glutathione against asbestos ROS; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of mesothelioma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Mesothelioma hydrogen: hydrogen in mesothelial cells (already mapped) and macrophages (already mapped) sustains glutathione defence against ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of mesothelioma."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Mesothelioma GLP-1: GLP-1 signalling modulates macrophage (already mapped) and dendritic-cell (already mapped) activation in the tumour microenvironment; GLP-1 deficit amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of mesothelioma."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Mesothelioma angiotensin-II: angiotensin-II drives macrophage (already mapped) and endothelial (already mapped) inflammation in pleural tissue; angiotensin-II amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of mesothelioma."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Meso rankl: RANKL from macrophages (already mapped) and t-cytotoxic cells (already mapped) promotes tumour immune evasion; rankl excess amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) mesothelioma cascade."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Meso fibronectin: fibronectin in fibroblasts (already mapped) and endothelial cells (already mapped) anchors pleural tumour matrix; fibronectin dysregulation amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Meso igf-1: IGF-1 from macrophages (already mapped) and fibroblasts (already mapped) promotes mesothelioma cell survival; igf-1 dysregulation amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Meso activin-a: activin-A from macrophages (already mapped) and fibroblasts (already mapped) drives pleural fibrosis; activin-a excess amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Meso cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates pleural vascular tone; cgrp excess amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Meso calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates pleural calcium balance; calcitonin dysregulation amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Meso substance-p: substance-P from macrophages (already mapped) and fibroblasts (already mapped) modulates pleural immune tone; substance-p excess amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Meso insulin-receptor: insulin receptor on macrophages (already mapped) and fibroblasts (already mapped) drives pleural metabolic repair; insulin-receptor loss amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Meso aldosterone: aldosterone from macrophages (already mapped) and fibroblasts (already mapped) modulates pleural ion balance; aldosterone excess amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma."
---

# Mesothelioma

## Overview

**Malignant mesothelioma** is an aggressive cancer arising from the mesothelial cells lining the pleural cavities (~80%), peritoneum (~20%), pericardium (<1%), and tunica vaginalis testis (<1%). Mesothelioma is tightly linked to **asbestos exposure** (chrysotile and especially amphibole varieties — crocidolite, amosite, tremolite) in ~80% of cases, with a characteristic latency period of **30-50 years** between initial exposure and cancer diagnosis; workers in shipbuilding, construction, insulation, mining, and demolition are most affected. Despite its relative rarity (~3,000-4,000 new cases/year in the USA; declining with asbestos bans but still high in developing countries with ongoing asbestos use), mesothelioma carries a dismal prognosis — median OS of 12-18 months with current therapy. The landmark **CheckMate 743** trial established nivolumab + ipilimumab as the first-line immunotherapy regimen, improving OS over platinum/pemetrexed chemotherapy [^baas-2021-checkmate743]; cisplatin + pemetrexed remains the chemotherapy backbone [^vogelzang-2003-pemetrexed].

**Epidemiology:**
- USA: ~3,000-4,000 new cases/year; Australia, UK, Italy, Japan: Relatively high incidence from historic asbestos use; global incidence peaks expected 2020-2030 given latency from peak asbestos use in 1960s-1980s
- Asbestos fiber types: Chrysotile (white asbestos, ~90% of use) is less carcinogenic than amphiboles; crocidolite (blue asbestos) and amosite (brown asbestos) are most carcinogenic → fiber geometry (long, thin = biopersistent in lung and pleura); erionite (fibrous zeolite, Turkey) also causes mesothelioma
- **Germline BAP1 mutations (BAP1-TPDS):** Account for 1-2% of mesothelioma; BAP1-TPDS mesothelioma is often epithelioid, younger onset, longer survival; genetic counseling for young patients (<50) and those without asbestos history
- SV40 (simian virus 40): Controversial association; SV40 large T antigen found in ~50% of mesothelioma tumors in early studies; postulated co-carcinogen with asbestos; not consistently confirmed; SV40 T antigen binds RB1 and p53

**Molecular landscape:**
- **BAP1:** Loss in ~50-60% of pleural mesothelioma; predominantly epithelioid subtype; polycomb epigenetic driver
- **NF2 (merlin):** Loss in ~40%; Hippo pathway → YAP/TAZ nuclear translocation → pro-proliferative; sarcomatoid enriched
- **CDKN2A (p16/p14ARF) homozygous deletion:** ~70% of mesothelioma; chromosome 9p21 region; also deletes MTAP → MAT2A dependency; diagnostic marker by FISH
- **LATS2:** Hippo pathway kinase; mutations in ~20%; NF2-LATS2 pathway loss → YAP activation
- **TP53:** ~25%; less common than other solid tumors
- **PTEN:** ~25% peritoneal; ~10% pleural; PI3K-AKT activation
- **Rare targetable alterations:** NTRK fusions (~2%); MSI-H (<2%); NF2 → FAK inhibitor activity; MTAP deletion → MAT2A inhibitor (AG-270)

## Structure

### Histological subtypes and diagnostic approach

**Epithelioid mesothelioma (~50%):**
Cells: Polygonal, abundant cytoplasm, prominent nucleolus; architectural patterns: tubulopapillary, micropapillary, glandular, solid; nuclear grade (WHO 2021 3-tier grading: N1 monotonous, N2 moderate atypia, N3 pleomorphic) — grade predicts prognosis within epithelioid subtype. Best prognosis: mOS ~12-18 months; BAP1-loss epithelioid → slightly better immune infiltration → best IO response.

**Sarcomatoid mesothelioma (~20%):**
Cells: Spindle-shaped; minimal cytoplasm; destructive growth pattern; variants include desmoplastic mesothelioma (>50% storiform collagen stroma) and lymphohistiocytoid (rare). Most aggressive subtype: mOS ~5-7 months; frequent CDKN2A/NF2 alterations; CK7+/calretinin+ (but often focally); IHC can be challenging; PD-L1 high → IO most active in this subtype. Desmoplastic variant: Stromal response may mimic organizing pleuritis → requires CDKN2A FISH to confirm malignancy.

**Biphasic mesothelioma (~30%):**
Contains both epithelioid and sarcomatoid components (each ≥10%); prognosis intermediate (mOS ~10-15 months); IO benefit intermediate between subtypes.

**Immunohistochemistry panel:**
Positive markers (mesothelial lineage): Calretinin (nuclear+cytoplasmic, ~95% epithelioid, less in sarcomatoid), WT-1 (Wilms tumor protein, nuclear, ~90%), D2-40 (podoplanin, ~90%), CK5/6 (~80%), mesothelin (surface, ~90% epithelioid). Negative markers (to exclude adenocarcinoma): CEA (-), MOC31 (-), Ber-EP4 (-), TTF-1 (-), napsin-A (-). Note: SOX2 can be positive in mesothelioma vs. LUAD-negative pattern, but this is not standardized.

**BAP1 IHC + CDKN2A FISH (diagnostic algorithm):**
On small biopsies or effusion cell blocks: BAP1 nuclear loss (by IHC) OR CDKN2A homozygous deletion (by FISH) in a mesothelial proliferation = highly specific for malignancy (~90% specificity); combined: ~90-95% specificity. This allows diagnosis of malignant mesothelioma vs. reactive mesothelial hyperplasia without the need for surgical biopsy in selected cases.

### Staging

**AJCC 8th Edition (Pleural Mesothelioma):**
T1: Involves ipsilateral pleura only (visceral or parietal); T2: Invades diaphragm or lung parenchyma; T3: Locally advanced (involves chest wall, pericardium — resectable); T4: Unresectable (mediastinum, contralateral pleura, peritoneum, spine, brachial plexus). N1: Ipsilateral bronchopulmonary/hilar nodes; N2: Subcarinal/mediastinal nodes; N3: Contralateral or supraclavicular nodes. M1: Distant metastases. Most patients present with stage III-IV.

**Peritoneal mesothelioma staging:**
Peritoneal Cancer Index (PCI): Quantifies peritoneal disease extent (0-39); completeness of cytoreduction (CC0-CC3); PCI ≤20 with CC0/CC1 resection → HIPEC (hyperthermic intraperitoneal chemotherapy) consideration.

## Function

### Normal mesothelium physiology

Mesothelial cells form a single-layer lining of the pleural, pericardial, and peritoneal cavities, providing: frictionless surface via secretion of phosphatidylcholine-rich fluid; regulation of fluid transport (mesothelium expresses AQP1 aquaporin water channels and lymphatic drainage pores — stomata); inflammation modulation (mesothelial cells produce IL-8, MCP-1, TNF-α upon injury); fibrinolysis (mesothelium produces plasminogen activators → prevents fibrin adhesion after injury). After injury: submesothelial fibroblasts differentiate into new mesothelial cells via mesothelial-to-mesenchymal transition (MMT) — analogous to EMT in cancer; asbestos fibers trigger MMT, ROS generation, and NLRP3 inflammasome activation in mesothelial cells → chronic inflammation → carcinogenic mutagenesis.

## Pathology

### Diagnosis and clinical presentation

**Pleural mesothelioma presentation:**
- Dyspnea (from pleural effusion, most common initial symptom)
- Pleuritic or dull chest pain (encasement of lung, chest wall invasion)
- Pleural effusion: Often large, unilateral, exudative; pleural fluid cytology alone has ~30% sensitivity for malignant mesothelioma → surgical biopsy (VATS/thoracoscopy) or CT-guided biopsy preferred; pleural fluid is exudative, often serosanguineous, with low glucose and high LDH
- Constitutional symptoms: Weight loss, fatigue (especially sarcomatoid subtype)
- SVC syndrome, Horner's syndrome: Late (mediastinal invasion)

**Peritoneal mesothelioma presentation:**
- Abdominal pain, distension, ascites
- Omental cake and peritoneal nodules on CT
- Serum CA-125 elevated; misdiagnosed as ovarian peritoneal carcinoma → calretinin/WT-1 IHC and mesothelin serology distinguish

**Imaging:**
- Chest CT: Unilateral pleural thickening ± effusion; rind-like pleural thickening encasing lung (sheet-like mesothelioma); pleural plaques (asbestos-related but non-malignant); lymph nodes; mediastinal involvement
- PET/CT: Pleural uptake; mediastinal/diaphragmatic extension; peritoneal spread; FDG-avid especially sarcomatoid
- MRI chest: Diaphragm and chest wall invasion assessment (T3/T4 distinction); better soft-tissue contrast than CT

**Diagnosis:**
- Surgical biopsy (VATS thoracoscopy) preferred over CT-guided to obtain adequate tissue for IHC + FISH; VATS allows direct visualization + macroscopic assessment
- Biomarkers: Serum mesothelin (SMR, N-ERC mesothelin): Elevated in ~80% of pleural mesothelioma; sensitivity ~60-70%, specificity ~90%; useful for monitoring but not for screening; Mesomark and MESOMARK assay
- Molecular testing: BAP1 IHC, CDKN2A FISH, next-gen sequencing panel (NF2, BAP1, CDKN2A, TP53, LATS2, PTEN); germline BAP1 testing if clinical criteria met

### Systemic treatment

**First-line (unresectable MPM):**

**Nivolumab + Ipilimumab (CheckMate 743, FDA 2021):** [^baas-2021-checkmate743]
- 605 patients unresectable treatment-naive MPM; nivolumab 3 mg/kg q2w + ipilimumab 1 mg/kg q6w vs. cisplatin/carboplatin + pemetrexed × 6 cycles
- OS 18.1 vs 14.1 months overall (HR 0.74, p=0.002); benefit most pronounced in non-epithelioid (sarcomatoid/biphasic: OS 18.1 vs 8.8 months, HR 0.46); epithelioid: OS 18.7 vs 16.3 months (modest, HR 0.85, NS for epithelioid alone)
- NCCN Category 1 preferred first-line; irAE profile: rash, colitis, hepatitis, endocrinopathies

**Cisplatin + Pemetrexed (+ folic acid/B12 supplementation, FDA 2004):** [^vogelzang-2003-pemetrexed]
- 456 patients; cisplatin/pemetrexed vs. cisplatin alone: OS 12.1 vs 9.3 months; ORR 41.3% vs 16.7%; established as chemotherapy backbone for mesothelioma
- Carboplatin (AUC 5) may substitute cisplatin; pemetrexed 500 mg/m² q21d; B12 and folic acid supplementation mandatory (reduces pemetrexed toxicity)
- Bevacizumab option: MAPS trial (France): Cisplatin/pemetrexed + bevacizumab: OS 18.8 vs 16.1 months; not FDA-approved for mesothelioma in USA; used in EU in cisplatin-eligible patients

**Second-line:**
- **Ramucirumab (VEGFR2) + gemcitabine:** RAMES trial: OS benefit vs. gemcitabine alone; European guideline recommendation
- **Vinorelbine:** OS 9.9 months in 2nd-line; single-agent; well-tolerated
- **Gemcitabine ± cisplatin:** Modest activity; ORR ~10-15%
- **Lurbinectedin:** Investigational for 2nd-line; ongoing Phase 2
- **Pembrolizumab:** KEYNOTE-158: Modest activity; PD-L1 ≥1% enriched for response; ORR ~18%; 3rd-line option
- **Nivolumab monotherapy:** ORR ~18-24% in 2nd+ line (IFCT-1501); option post-chemotherapy first-line

**Peritoneal mesothelioma:**
Cytoreductive surgery (CRS) + hyperthermic intraperitoneal chemotherapy (HIPEC): Standard for eligible patients (PCI ≤20, good performance status, epithelioid); 5-year OS ~50% after CRS+HIPEC vs. <15% for systemic chemotherapy alone; cisplatin-based HIPEC at 42°C × 90 minutes.

**Surgery for pleural mesothelioma:**
- **EPP (extrapleural pneumonectomy):** Removes lung, pleura, ipsilateral diaphragm, pericardium; MARS trial (2011): No survival benefit over palliative chemotherapy → largely abandoned; associated with high morbidity (5-10% operative mortality)
- **P/D (pleurectomy/decortication):** Lung-sparing pleura removal; less morbidity; MARS-2 trial: P/D + chemo vs. chemo alone → preliminary results suggest no survival benefit; NCCN: Surgery only in highly selected LS-SCLC patients at expert centers
- **Radiation:** Hemithoracic radiation post-EPP (to prevent seeding); palliative radiation for chest wall pain, SVC syndrome

**Emerging targets:**
- **MAT2A inhibitors (MTAP-deleted):** CDKN2A deletion (9p21) co-deletes MTAP in ~70% of mesothelioma → MAT2A synthetic lethality → AG-270 (Phase 1/2, PRISM study); promising early signals
- **Tazemetostat (EZH2 inhibitor):** BAP1 loss → EZH2 dependency; CELLO-2 Phase 2 for BAP1-null pleural mesothelioma ongoing
- **Mesothelin ADC (BMS-986148):** Anetumab ravtansine Phase 2; ORR ~20%; DM4-maytansine payload; mesothelin surface expression enables targeting
- **NTRK fusions:** Larotrectinib/entrectinib for rare NTRK+ mesothelioma (tumor-agnostic)

## Connections

- `connects-to` → **[BAP1](../../03-molecular/bap1/README.md)** — BAP1 loss (~50-60% of mesothelioma) drives polycomb-mediated epigenetic reprogramming; BAP1 IHC nuclear loss aids mesothelioma diagnosis; epithelioid BAP1-mutant mesothelioma has better prognosis; germline BAP1 mutations → BAP1-TPDS (familial mesothelioma).
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Nivolumab + ipilimumab (CheckMate 743: OS 18.1 vs 14.1 months, HR 0.74, FDA 2021) is first-line for unresectable pleural mesothelioma; benefit most pronounced in sarcomatoid/biphasic subtypes (OS 18.1 vs 8.8 months); PD-L1 expression enriched in sarcomatoid.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Bevacizumab + cisplatin/pemetrexed (MAPS trial: OS 18.8 vs 16.1 months) is used in select European centers; VEGF overexpression is common in mesothelioma; ramucirumab (VEGFR2) under investigation; anti-VEGF + IO combinations in ongoing trials.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss in ~25% of peritoneal mesothelioma and ~10% of pleural; PI3K-AKT-mTOR activation downstream of PTEN loss → mTOR inhibitors studied in mesothelioma; PTEN-CDKN2A co-deletion confers aggressive phenotype; PTEN loss is more common in sarcomatoid subtype.
- `connects-to` → **[NF2](../../03-molecular/nf2/README.md)** — NF2/merlin loss occurs in ~40% of mesothelioma (enriched in the sarcomatoid subtype) → Hippo pathway off → YAP/TAZ nuclear → TEAD-driven proliferation; this makes NF2-null mesothelioma the lead indication for TEAD and FAK inhibitors now in early-phase trials.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pleural mesothelioma grows as a rind encasing the lung after asbestos fibers inhaled decades earlier lodge in the pleura; it presents with dyspnea and a large exudative effusion, and lung-sparing pleurectomy/decortication has largely replaced extrapleural pneumonectomy.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Asbestos drives mesothelioma partly through frustrated phagocytosis of long, biopersistent fibers by mesothelial cells and macrophages → ROS and NLRP3 inflammasome activation → IL-1β-driven chronic inflammation over 30-50 years → the mutagenic milieu that seeds malignancy.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — Mesothelioma and meningioma share their central driver — NF2/merlin loss switching off Hippo so YAP/TAZ-TEAD drive proliferation (NF2-null in ~40% of mesothelioma, ~50-60% of meningioma) — why both spearhead trials of TEAD inhibitors despite arising in very different tissues.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Mesothelioma is moderately immunogenic, so dual checkpoint blockade — nivolumab plus ipilimumab, freeing cytotoxic CD8+ T cells — became first-line for unresectable pleural disease (CheckMate 743), with the largest benefit in the chemo-resistant sarcomatoid subtype.
- `connects-to` → **[Uveal Melanoma](../uveal-melanoma/README.md)** — Mesothelioma and uveal melanoma are linked by BAP1: germline BAP1 loss causes the BAP1 tumor-predisposition syndrome, in which one family develops mesothelioma, uveal melanoma, renal cell carcinoma, and skin tumors — a shared chromatin defect across different organs.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Mesothelioma and renal cell carcinoma are both part of the BAP1 tumor predisposition syndrome: germline BAP1 loss predisposes to mesothelioma, clear-cell RCC, uveal melanoma and atypical melanocytic tumors, so mesothelioma with a family cancer history warrants BAP1 testing.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages drive asbestos-induced mesothelioma: long fibers resist 'frustrated' macrophage phagocytosis, so they release reactive oxygen species and activate the NLRP3 inflammasome—chronic IL-1β inflammation that transforms mesothelial cells over decades.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Mesothelioma and cholangiocarcinoma both occur in the BAP1 syndrome and share a chromatin-level driver: loss of BAP1, a nuclear deubiquitinase tumor suppressor, promotes both, and the epigenetic vulnerabilities plus checkpoint approaches are being explored across these cancers.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Mesothelioma and lung cancer are the great asbestos-related thoracic malignancies but distinct: mesothelioma arises from the pleural mesothelium, while NSCLC arises from bronchial/alveolar epithelium—asbestos drives both, but only lung cancer is strongly smoking-linked.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy's role in mesothelioma is limited: the tumor's diffuse rind over the pleura makes curative irradiation hard without harming lung, so photon radiation serves mainly palliation—surgery and chemo-immunotherapy carry the main burden.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Peritoneal mesothelioma and ovarian cancer overlap closely: both arise from or mimic serous peritoneal epithelium and may share BAP1 alterations, so a woman with peritoneal carcinomatosis needs pathology to separate mesothelioma from serous ovarian carcinoma.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion is a defining mesothelioma alteration: loss of this tumor suppressor, alongside BAP1 and NF2, drives the cancer and helps distinguish malignant mesothelioma from benign reactive mesothelial proliferation on biopsy—a key diagnostic marker.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The sarcomatoid subtype of mesothelioma is fibroblast-like and grim: spindle, fibroblast-resembling cells make a dense tumor far more resistant to therapy than the epithelioid type—so histologic subtype strongly predicts survival.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Mesothelioma is responsive to immunotherapy despite few mutations: chronic asbestos inflammation and an immune-rich microenvironment make checkpoint blockade (anti-PD-1/CTLA-4) a frontline option—so engaging the immune system has improved outcomes in this cancer.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Mesothelioma is the signature cancer of the respiratory system's lining: decades after asbestos inhalation, the pleura thickens with tumor that traps the lung in a rind, causing breathlessness and effusions—an almost wholly preventable, dismal-prognosis cancer.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — p53-pathway disruption helps drive mesothelioma: although BAP1 and CDKN2A losses dominate, p53 inactivation contributes to the genomic chaos of asbestos-induced tumors, so the guardian-of-the-genome network features in this slow-developing malignancy.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Carbon-ion radiotherapy is explored for mesothelioma: its dense, sharply localized dose may help this radioresistant, diffusely spreading pleural tumor, complementing the surgery, chemotherapy and immunotherapy used against an asbestos-caused cancer.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Mesothelioma's immunotherapy pairs two checkpoints: combining anti-CTLA-4 (ipilimumab) with anti-PD-1 (nivolumab) became a first-line standard, extending survival in unresectable disease where chemotherapy alone had long stalled.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Asbestos scars the pleura before it causes cancer: dense pleural fibrosis and plaques mark exposure, and the desmoplastic variant of mesothelioma is so fibrous it can be mistaken for benign scarring—making biopsy interpretation difficult.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Asbestos kills mesothelial cells partly through iron: fibers adsorb iron and catalyze reactive oxygen species that damage DNA, and iron-coated 'ferruginous bodies' in tissue are the histologic fingerprint of the exposure that drives mesothelioma.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Mesothelioma is fundamentally a Hippo-pathway cancer acting through YAP1: NF2 and LATS losses release YAP1 to switch on growth genes, so this transcription co-activator is a central driver and a sought-after drug target in the disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Mesothelioma's cause is a magnesium-silicate mineral: asbestos fibers like chrysotile are magnesium silicates whose durable, needle-like shape lodges in the pleura and provokes the decades-long inflammation that seeds the cancer.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Mesothelioma defends itself with regulatory T cells: Tregs fill its immunosuppressive microenvironment and blunt anti-tumor immunity, which is why dual checkpoint blockade (nivolumab plus ipilimumab) is now frontline for the disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Mesothelioma can arise on the heart's lining: though most form on the pleura, the same asbestos-driven malignancy strikes the pericardium, where it encases the heart and impairs its filling—a rare but devastating site.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Mesothelioma hides in a hypoxic, fibrous tumor via HIF-1alpha: its dense desmoplastic stroma outstrips its oxygen supply, and the resulting HIF signaling drives survival and angiogenesis, part of why it resists chemotherapy.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are enlisted to fight mesothelioma: because the tumor is poorly immunogenic, dendritic-cell vaccines and other antigen-presenting strategies aim to prime T-cell attack alongside the checkpoint drugs now used frontline.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Mesothelioma also strikes the belly: peritoneal mesothelioma coats the abdominal organs and bowel, including the large intestine, causing pain, ascites, and obstruction—the second most common form after pleural.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Mesothelioma recruits endothelial cells to grow: VEGF from the tumor drives these vessel-lining cells to build its blood supply, which is why anti-VEGF therapy is added to chemotherapy.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Mesothelioma steals the breath of oxygen: as it encases the lung and fills the chest with malignant effusion, it squeezes the lung shut, so worsening breathlessness and low oxygen dominate the illness.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy was the historic gold standard for mesothelioma: its cells bristle with long, slender, bushy microvilli, whose high length-to-width ratio separates them from the short, stubby microvilli of metastatic adenocarcinoma.
- `connects-to` → **[WT1](../../03-molecular/wt1/README.md)** — WT1 is a defining mesothelioma marker: strong nuclear WT1 staining is expected in mesothelial tumors and absent in lung adenocarcinoma, making it a pillar of the immunostain panel that resolves a pleural biopsy.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Mesothelioma drives up platelets: IL-6 from the tumor provokes a paraneoplastic thrombocytosis, and a high platelet count both flags advanced disease and raises the clotting risk that complicates these patients' care.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Peritoneal mesothelioma encases the abdominal organs: arising on the lining of the belly, it spreads over the surface of the liver and gut, coating them in tumor rather than invading deep, the abdominal counterpart of its pleural form.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Late mesothelioma can reach bone: though it spreads mainly by creeping along the chest and abdominal linings, advanced disease occasionally seeds distant skeletal and marrow metastases.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — A well-differentiated papillary mesothelioma leaves calcium clues: it forms psammoma bodies, concentric calcium deposits, the laminated mineral specks that help the pathologist recognize this indolent variant.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Mesothelioma is diagnosed by antibody panels: calretinin, WT1, and D2-40 stain positive while CEA, MOC-31, and claudin-4 stay negative, separating it from adenocarcinoma, and loss of BAP1 staining confirms the malignant clone.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The blood count both warns and weakens: a high neutrophil-to-lymphocyte ratio predicts poorer survival in mesothelioma, while the pemetrexed-cisplatin chemotherapy used against it is myelosuppressive, dropping neutrophils and risking infection.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Chronic disease and chemotherapy thin the red cells: the smoldering inflammation of mesothelioma plus antifolate pemetrexed depress erythrocyte production into the anemia and fatigue that shadow the long course of treatment.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Losing NF2 unleashes mTOR: merlin normally restrains both the Hippo pathway and mTORC1, so its frequent loss in mesothelioma drives growth through mTOR — a vulnerability probed alongside the Hippo-YAP axis for targeted therapy.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — BAP1 mesothelioma runs in families: germline BAP1 mutations transmit a tumor-predisposition syndrome down the generations, so a diagnosis can prompt cascade genetic testing and reproductive counseling for relatives at risk.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Asbestos keeps the pleura inflamed: the indigestible fibers provoke a chronic response in which mast cells and macrophages release mediators that, over decades, foster the mutations and microenvironment from which mesothelioma arises.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — The tumor cheats its clock: TERT promoter mutations switch telomerase back on so mesothelioma cells escape the telomere shortening that should limit their divisions, one of the few recurrent point mutations in a cancer otherwise defined by losing tumor suppressors.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Beyond Hippo, a second developmental pathway fuels it: aberrant Wnt/β-catenin signaling promotes mesothelial proliferation and survival, making the pathway a studied therapeutic target alongside the YAP/Hippo axis disrupted by NF2 loss.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Innate killers are part of the fight: natural killer cells can lyse mesothelioma, and the disease's heavy immunosuppression dampens them, which is why NK-engaging and CAR-NK strategies are explored alongside the checkpoint drugs now used against it.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 carries mesothelioma's systemic toll: the tumor and its asbestos-driven inflammation pour out IL-6, fueling the paraneoplastic thrombocytosis, fever, and cachexia that mark advanced disease and predict worse outcome.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Few cancers clot like mesothelioma: its pro-coagulant tumor and the surgery and chemotherapy used against it give a high venous thromboembolism risk that complicates the whole treatment course.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — It can wrap and squeeze the heart: pericardial mesothelioma — and pleural disease encasing the heart — causes effusion and constriction that impair filling, producing a restrictive heart failure.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Asbestos-driven inflammation feeds STAT3: the chronic IL-6-rich inflammation that asbestos provokes in the pleura activates STAT3, a survival and proliferation signal central to mesothelioma's inflammation-to-cancer origin.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — An infected pleural space turns dangerous: recurrent pleural effusions, indwelling drains, pleurodesis and major surgery for mesothelioma can seed empyema and bloodstream infection that progress to sepsis.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic inflammation wears down the blood: the IL-6-driven inflammatory state of mesothelioma suppresses erythropoiesis, producing an anemia of chronic disease that contributes to the fatigue of advanced disease.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — It grows into the chest wall and nerves: mesothelioma encases the pleura and invades the chest wall and intercostal nerves, causing severe, often intractable neuropathic chest pain that dominates the illness.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its chemo is hard on the kidney: the cisplatin-pemetrexed backbone of mesothelioma treatment is nephrotoxic, and pemetrexed is renally cleared, so impaired and injured kidneys both threaten and are threatened by therapy.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A dismal prognosis weighs on mood: relentless breathlessness and chest pain, a near-uniformly fatal course and often unresolved asbestos-related litigation give mesothelioma a heavy burden of depression.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Chemotherapy and damaged pleura open the lung to mold: the neutropenia from pemetrexed-platinum chemotherapy, plus a scarred, trapped lung, can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Radical chest surgery heals badly: extrapleural pneumonectomy or decortication for mesothelioma, plus repeated chest drains and pleurodesis, leave large thoracic wounds slow to heal in a cachectic patient.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Breathlessness and a grim prognosis breed worry: the air hunger, chest pain and near-uniformly fatal outlook of mesothelioma, with its asbestos-litigation stress, foster severe anxiety alongside depression.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It also grows in the belly: peritoneal mesothelioma, the second commonest form, encases the bowel and causes ascites, abdominal pain and intestinal obstruction.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It seeds the skin along procedure tracks: mesothelioma characteristically grows out along the tracts of chest drains, biopsies and surgical scars, forming painful cutaneous tumour nodules.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It eats into the chest wall: pleural mesothelioma invades the ribs and intercostal structures, causing relentless chest-wall pain and bony destruction as it spreads.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It spreads through and blocks the lymphatics: mesothelioma invades mediastinal and hilar lymph nodes, and obstruction of pleural lymphatic drainage produces the recurrent effusions that dominate its course.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It can encase and arise on the heart: pleural mesothelioma can wrap the pericardium causing constrictive physiology, and a rare primary pericardial mesothelioma exists.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It invades the chest-wall nerves: tumour growth into the intercostal nerves causes severe neuropathic chest-wall pain, the dominant and hardest-to-control symptom of advanced mesothelioma.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Chemotherapy threatens the kidney: the cisplatin-pemetrexed regimen central to mesothelioma treatment is nephrotoxic, and pemetrexed itself requires adequate renal function.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Immunotherapy extended survival: dual checkpoint blockade with nivolumab and ipilimumab is now a standard first-line option for unresectable pleural mesothelioma.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can derange metabolism: mesothelioma occasionally causes paraneoplastic hypoglycaemia or SIADH with hyponatraemia among its systemic effects.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Platinum-pemetrexed is the chemo backbone: cisplatin with pemetrexed, sometimes with bevacizumab, is the standard chemotherapy for mesothelioma not treated with immunotherapy.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — A pleural tumour to distinguish: primary pleural synovial sarcoma mimics mesothelioma radiologically and histologically, separated by its SS18 gene fusion.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Both belong to the BAP1 family: germline BAP1 loss predisposes to mesothelioma alongside uveal and cutaneous melanoma and renal cancer, a hereditary tumour-predisposition syndrome.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy moved to the front line: dual checkpoint blockade with nivolumab and ipilimumab (CheckMate-743) improves survival over chemotherapy in unresectable pleural mesothelioma, especially the chemo-resistant sarcomatoid type.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Where the fibres land and the damage starts: inhaled asbestos fibres deposit in the distal alveoli, then migrate to the pleura over decades; the same fibres scar the alveolar walls as asbestosis, the fibrotic lung disease that accompanies mesothelioma risk.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — The main mimic on a pleural biopsy: metastatic breast cancer is a common cause of malignant pleural effusion and pleural nodules that must be distinguished from mesothelioma, separated by immunohistochemistry (calretinin/WT1 versus epithelial markers).
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — Shared NF2/merlin loss: mesothelioma frequently inactivates the NF2/merlin tumour suppressor, the same gene whose germline loss defines neurofibromatosis type 2 and drives its schwannomas and meningiomas.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Pericardial mesothelioma: a rare primary mesothelioma arises from the pericardium enveloping the myocardium, causing constrictive physiology and cardiac tamponade.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Immunotherapy in an inflamed tumour: mesothelioma's chronic asbestos-driven inflammation supports tertiary lymphoid structures, and combined PD-1/CTLA-4 checkpoint blockade is now first-line for unresectable disease.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — The benign mimic: tuberculous pleurisy produces pleural thickening, effusion and a rind that can closely imitate mesothelioma on imaging, a crucial differential to exclude with biopsy especially where TB is endemic.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The peritoneal variant: about a fifth of mesotheliomas arise in the peritoneum, studding the serosal surfaces and encasing the bowel over its intestinal epithelium to cause obstruction and ascites.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Chest-wall invasion: pleural mesothelioma grows outward through the pleura into the chest wall, eroding ribs and cortical bone and seeding the tracts left by biopsy needles and chest drains.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — BAP1 synthetic lethality: BAP1 loss in mesothelioma creates a dependence on EZH2, the rationale for EZH2 inhibitors such as tazemetostat in BAP1-deficient tumours.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Receptor overexpression: EGFR is frequently overexpressed in mesothelioma, contributing to its growth signalling though single-agent EGFR inhibition has had limited success.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Proliferative drive: MYC activation contributes to the aggressive proliferation of mesothelioma, downstream of its tumour-suppressor losses.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT survival: PTEN loss and PI3K/AKT activation sustain mesothelioma cell survival, cooperating with the NF2-Hippo and BAP1 lesions that define the disease.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: CDKN2A deletion—near-universal in mesothelioma—unleashes cyclin D-CDK4/6, accelerating the cell cycle and marking poor prognosis.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Autocrine growth: mesothelioma cells secrete PDGF that acts in an autocrine loop, driving the proliferation and desmoplastic stroma of these pleural tumours.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Asbestos inflammasome carcinogenesis: asbestos fibres activate the NLRP3 inflammasome in mesothelial cells and macrophages to release IL-1β, the chronic inflammation that drives mesothelioma over decades.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Immunosuppressive desmoplasia: TGF-beta drives the desmoplastic stroma and suppresses anti-tumour immunity in mesothelioma, contributing to its poor response to therapy.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 draws the abundant tumour-associated macrophages of mesothelioma into the pleural tumour, building an immunosuppressive microenvironment.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — Asbestos fibers cause mesothelial-cell necrosis that releases HMGB1, which signals through RAGE to sustain the chronic inflammation central to asbestos-induced mesothelial carcinogenesis over the decades-long latency.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4-CXCL12 signaling drives the diffuse pleural and peritoneal spread of mesothelioma, the rind-like encasement of the lung that defines the disease and makes complete surgical resection nearly impossible.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Mesothelioma resists caspase-3-mediated apoptosis through high anti-apoptotic protein expression, a key reason for its notorious chemoresistance and the only modest survival benefit of cytotoxic therapy.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Dual checkpoint blockade (nivolumab-ipilimumab) is now first-line for unresectable mesothelioma, and mesothelin-directed CAR-T cells aim to kill the tumor through perforin and granzyme, the cytotoxic effector mechanism of these immune therapies.
- `connects-to` → **[Src kinase](../../03-molecular/src-kinase/README.md)** — The NF2/merlin loss common in mesothelioma disinhibits Src/FAK and the Hippo-YAP pathway at the membrane, driving the proliferation and loss of contact inhibition characteristic of these tumors.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — BAP1 loss impairs homologous-recombination DNA repair in mesothelioma, leaving cells reliant on RAD51-dependent and alternative repair and raising the prospect of synthetic-lethal PARP inhibition in BAP1-deficient tumors.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Homozygous CDKN2A deletion (mapped) removes p16, leaving the CDK4/6-cyclin-D1 axis (cyclin-D1 mapped) unchecked in mesothelioma and a candidate target for CDK4/6 inhibition.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA drives the PI3K-AKT-mTOR axis (PTEN, AKT and mTOR already mapped) that supports growth and survival in mesothelioma.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-α released by asbestos-activated macrophages promotes the survival and malignant transformation of mesothelial cells, part of the chronic inflammation (with the IL-1β/NLRP3 axis mapped) that drives mesothelioma.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Asbestos fibers trigger sustained NF-κB-driven inflammation (NLRP3 and IL-1β already mapped) in the pleura, the inflammatory milieu central to mesothelioma development.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant defense counters the iron-catalyzed reactive-oxygen-species generation by asbestos fibers that drives the oxidative DNA damage of mesothelioma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RAS-ERK signaling downstream of EGFR and PDGFR (both already mapped) provides a proliferative input to mesothelioma growth.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is expressed in mesothelioma and contributes to its invasion and immunosuppressive microenvironment.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 mapped), driven by asbestos-induced chronic inflammation, promotes mesothelioma growth.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) shapes the immunosuppressive and fibrotic microenvironment of mesothelioma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of mesothelioma, relevant to its checkpoint immunotherapy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Asbestos-induced DNA damage and chronic inflammation engage cGAS-STING, contributing to the carcinogenesis and immune microenvironment of mesothelioma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate the oxidative stress of asbestos exposure relevant to the cellular transformation of mesothelioma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and survival signaling of the BAP1-deficient cells of mesothelioma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in mesothelioma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from asbestos-recruited myeloid cells shape the chronic inflammatory microenvironment driving mesothelioma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of mesothelioma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of mesothelioma cells.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling contributes, alongside BAP1 loss (BAP1 already mapped), to the epigenetic dysregulation of mesothelioma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of mesothelioma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of mesothelioma.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the proliferation and epithelial-mesenchymal biology of mesothelioma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of mesothelioma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of mesothelioma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of mesothelioma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of mesothelioma.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of mesothelioma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin (SPP1) participates in the asbestos-related inflammation and tumor microenvironment of mesothelioma, and is a recognized biomarker.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy: mesothelioma responds to combination checkpoint blockade (PD-1/CTLA-4 already mapped), and MHC class II antigen presentation shapes the T-cell response, with mesothelin-directed CAR-T and vaccines also in trials.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Mesothelin CAR-T: IL-2-driven T-cell expansion powers the mesothelin-targeted CAR-T and adoptive-cell therapies (perforin already mapped) being tested against mesothelioma, whose surface mesothelin makes it an attractive target.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Sarcomatoid invasion: the AXL receptor tyrosine kinase drives the epithelial-mesenchymal transition of mesothelioma toward the aggressive sarcomatoid phenotype, contributing to invasion and treatment resistance.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Asbestos oxidative injury: the iron-coated asbestos fibres (iron already mapped) generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage over decades initiates the mesothelial carcinogenesis of mesothelioma.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Effusion and anaemia: mesothelioma causes recurrent, often blood-stained pleural effusions, and the chronic disease with any haemorrhage lowers haemoglobin, the anaemia of malignancy adding to the breathlessness and cachexia.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the mesothelioma microenvironment dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), part of the immune evasion that the dual checkpoint blockade standard in mesothelioma aims to overcome.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Asbestos inflammation: prostaglandins from the chronic asbestos-driven inflammation (IL-6, TNF and IL-1 already mapped) promote the proliferation and immunosuppression of mesothelial carcinogenesis, part of the inflammatory pathway of the disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive microenvironment of mesothelioma.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of mesothelioma, part of the stromal biology of these often highly vascular pleural tumours.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive microenvironment of mesothelioma.
- `connects-to` → **[Large intestine](../../06-organ/large-intestine/README.md)** — Peritoneal mesothelioma: the peritoneal mesothelium lining the large intestine is the second commonest site of mesothelioma, the peritoneal form treated with cytoreductive surgery and heated intraperitoneal chemotherapy.
- `connects-to` → **[Small intestine](../../06-organ/small-intestine/README.md)** — Peritoneal spread: the peritoneal mesothelioma also envelops the small intestine, the mesothelial lining of the peritoneal cavity coating the bowel loops in the diffuse peritoneal form.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Omental adipose adipokine: leptin from the omental and peritoneal adipose tissue signals to the peritoneal mesothelioma, part of the metabolic microenvironment of the tumour.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Peritoneal adipokine: adiponectin, with leptin (already mapped), from the omental and peritoneal adipose signals within the microenvironment of peritoneal mesothelioma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the peritoneal mesothelioma microenvironment.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the checkpoint (PD-1 already mapped) immunotherapy of mesothelioma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity exploited by the nivolumab-ipilimumab therapy of mesothelioma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the mesothelioma immune microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the asbestos-driven inflammatory microenvironment of mesothelioma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammatory microenvironment of mesothelioma.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the mesothelioma microenvironment.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the chronic asbestos-driven inflammation and the immunosuppressive dimension of the mesothelioma microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling recruits and polarises the myeloid cells within the chronic inflammatory microenvironment of mesothelioma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the tumour-infiltrating lymphocytes of mesothelioma.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, associates with the nivolumab–ipilimumab (PD-1 already mapped) immunotherapy response of mesothelioma.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the mesothelioma cells recruit factor H to regulate the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) and evade the complement attack of the chronic-inflammatory microenvironment.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-tumour antibodies (already mapped) within the asbestos-driven chronic-inflammatory microenvironment of mesothelioma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Pleural mesothelial alarmin: TSLP released by the asbestos-damaged and inflamed pleural mesothelium (respiratory system already mapped) activates the innate dendritic-cell and mast-cell response, amplifying the HMGB1-NF-kB (already mapped) inflammatory cascade of mesothelioma.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Mesothelial invasion stroma: periostin is highly expressed in the mesothelioma pleural stroma, downstream of TGF-β (already mapped) and fibroblast activation; elevated periostin promotes the integrin αV-mediated invasiveness and fibrotic pleural thickening of mesothelioma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell stroma: histamine from the mast cells infiltrating mesothelioma stroma promotes VEGF (already mapped) angiogenesis and stromal remodelling; mast-cell histamine contributes to the pleural effusion and the immune-evasion environment of mesothelioma.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Pleural effusion kinin: bradykinin, via B2 receptor, amplifies pleural vascular permeability in mesothelioma; kinin-kallikrein activation enhances VEGF-driven (already mapped) angiogenesis and mast-cell (already mapped) stromal inflammation of mesothelioma.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Tumour EPOR signalling: erythropoietin receptor (EPOR) on mesothelioma cells activates the JAK2/STAT3 (already mapped) pro-survival pathway and promotes the VEGF-driven (already mapped) angiogenesis and resistance to platinum-based chemotherapy of mesothelioma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Oncostatic melatonin: melatonin scavenges reactive oxygen species generated by asbestos-activated mesothelial cells, attenuates NF-kB (already mapped) and TGF-β (already mapped) signalling, reducing the invasiveness and VEGF (already mapped) angiogenesis of mesothelioma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-mesothelioma axis: testosterone, via androgen receptor on mesothelioma cells and macrophages (already mapped), modulates NF-κB (already mapped) and VEGF-driven (already mapped) signalling and partly explains the male-predominant incidence of pleural mesothelioma.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Neuroendocrine 5-HT axis: serotonin from mast cells (already mapped) and mesothelioma-associated neuroendocrine cells signals via 5-HT2 receptors on endothelial cells (already mapped), amplifying the VEGF-driven (already mapped) angiogenic niche of pleural mesothelioma.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-escape prolactin: prolactin, via PRL-R on mesothelioma cells and macrophages (already mapped), activates JAK2/STAT3 (already mapped) pro-survival and immune-checkpoint (already mapped) pathways, promoting the immunosuppressive phenotype of pleural mesothelioma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Mesothelioma oxytocin anti-tumour: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the NF-κB (already mapped) and VEGF (already mapped) pro-tumour immune cascade, reducing the immunosuppressive phenotype of pleural mesothelioma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Mesothelioma vasopressin vascular: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the pleural tumour vascular niche; dysregulation amplifies NF-κB (already mapped) and VEGF (already mapped) angiogenic signalling in mesothelioma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Mesothelioma selenium antioxidant: selenium, via GPx/TrxR selenoproteins in mesothelioma cells and macrophages (already mapped), quenches ROS that amplifies NF-κB (already mapped) and VEGF-driven (already mapped) angiogenesis in the pleural mesothelioma microenvironment.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Mesothelioma iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of mesothelioma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Mesothelioma sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and TNF-α (already mapped) skewing amplifies the T-cytotoxic (already mapped) cascade of mesothelioma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Mesothelioma potassium: potassium channels regulate macrophage (already mapped) and neutrophil (already mapped) function in the mesothelioma TME; potassium depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of mesothelioma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Mesothelioma copper: copper, as cofactor of SOD1 in macrophages (already mapped) and mast cells (already mapped), scavenges ROS in the mesothelioma TME; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of mesothelioma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Mesothelioma zinc: zinc, as cofactor of metalloproteinases in macrophages (already mapped) and fibroblasts (already mapped), modulates matrix invasion; zinc depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of mesothelioma.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Mesothelioma phosphorus: phosphorus, as phospholipid and ATP in macrophages (already mapped) and mast cells (already mapped), drives immune signalling; phosphorus depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of mesothelioma.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Mesothelioma chloride: chloride regulates mesothelial cells (already mapped) and macrophage (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) asbestos-driven cascade of mesothelioma.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Mesothelioma nitrogen: nitrogen in amino-acid scaffold of BAP1 (already mapped) and CDKN2A proteins modulates mesothelial cell (already mapped) growth arrest; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of mesothelioma.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Mesothelioma sulfur: sulfur, as cysteine in macrophages (already mapped) and mesothelial cells (already mapped), supports glutathione against asbestos ROS; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of mesothelioma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Mesothelioma hydrogen: hydrogen in mesothelial cells (already mapped) and macrophages (already mapped) sustains glutathione defence against ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of mesothelioma.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Mesothelioma GLP-1: GLP-1 signalling modulates macrophage (already mapped) and dendritic-cell (already mapped) activation in the tumour microenvironment; GLP-1 deficit amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of mesothelioma.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — Mesothelioma angiotensin-II: angiotensin-II drives macrophage (already mapped) and endothelial (already mapped) inflammation in pleural tissue; angiotensin-II amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of mesothelioma.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Meso rankl: RANKL from macrophages (already mapped) and t-cytotoxic cells (already mapped) promotes tumour immune evasion; rankl excess amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) mesothelioma cascade.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Meso fibronectin: fibronectin in fibroblasts (already mapped) and endothelial cells (already mapped) anchors pleural tumour matrix; fibronectin dysregulation amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Meso igf-1: IGF-1 from macrophages (already mapped) and fibroblasts (already mapped) promotes mesothelioma cell survival; igf-1 dysregulation amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Meso activin-a: activin-A from macrophages (already mapped) and fibroblasts (already mapped) drives pleural fibrosis; activin-a excess amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Meso cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates pleural vascular tone; cgrp excess amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Meso calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates pleural calcium balance; calcitonin dysregulation amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — Meso substance-p: substance-P from macrophages (already mapped) and fibroblasts (already mapped) modulates pleural immune tone; substance-p excess amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma.
- `connects-to` → **[Insulin receptor](../../03-molecular/insulin-receptor/README.md)** — Meso insulin-receptor: insulin receptor on macrophages (already mapped) and fibroblasts (already mapped) drives pleural metabolic repair; insulin-receptor loss amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Meso aldosterone: aldosterone from macrophages (already mapped) and fibroblasts (already mapped) modulates pleural ion balance; aldosterone excess amplifies smad4 (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of mesothelioma.

[^baas-2021-checkmate743]: Baas P, Scherpereel A, Nowak AK, et al. First-line nivolumab plus ipilimumab in unresectable malignant pleural mesothelioma (CheckMate 743). *Lancet.* 2021;397(10272):375-386. [doi:10.1016/S0140-6736(20)32714-8](https://doi.org/10.1016/S0140-6736(20)32714-8) · [PubMed 33485464](https://pubmed.ncbi.nlm.nih.gov/33485464/)
[^vogelzang-2003-pemetrexed]: Vogelzang NJ, Rusthoven JJ, Symanowski J, et al. Phase III study of pemetrexed in combination with cisplatin versus cisplatin alone in patients with malignant pleural mesothelioma. *J Clin Oncol.* 2003;21(14):2636-2644. [doi:10.1200/JCO.2003.11.136](https://doi.org/10.1200/JCO.2003.11.136) · [PubMed 12860938](https://pubmed.ncbi.nlm.nih.gov/12860938/)
